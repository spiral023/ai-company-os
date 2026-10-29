import { loginPage } from "./login.mjs";
import { CONTENT, SCRIPT_HASHES } from "./content-manifest.mjs";

export const COOKIE_NAME = "__Host-pocock-session";
export const SESSION_TTL = 8 * 60 * 60;
const encoder = new TextEncoder();

function base64url(bytes) {
  return btoa(String.fromCharCode(...new Uint8Array(bytes))).replaceAll("+", "-").replaceAll("/", "_").replaceAll("=", "");
}

function unbase64url(text) {
  if (!/^[A-Za-z0-9_-]+$/.test(text)) throw new Error("Invalid encoding");
  return Uint8Array.from(atob(text.replaceAll("-", "+").replaceAll("_", "/")), (char) => char.charCodeAt(0));
}

function fromHex(text) {
  return Uint8Array.from(text.match(/../g), (pair) => Number.parseInt(pair, 16));
}

export async function verifyPassword(password, verifier) {
  const match = /^pbkdf2_sha256\$100000\$([a-f0-9]{32})\$([a-f0-9]{64})$/.exec(verifier || "");
  if (!match || typeof password !== "string" || password.length > 256) return false;
  const key = await crypto.subtle.importKey("raw", encoder.encode(password), "PBKDF2", false, ["deriveBits"]);
  const bits = await crypto.subtle.deriveBits({ name: "PBKDF2", hash: "SHA-256", salt: fromHex(match[1]), iterations: 100000 }, key, 256);
  const expected = fromHex(match[2]);
  let difference = 0;
  new Uint8Array(bits).forEach((byte, index) => { difference |= byte ^ expected[index]; });
  return difference === 0;
}

async function sessionKey(env) {
  // Eine Passwortrotation macht dadurch auch bestehende Sessions ungültig.
  return crypto.subtle.importKey("raw", encoder.encode(env.SESSION_KEY + ":" + env.PASSWORD_VERIFIER), { name: "HMAC", hash: "SHA-256" }, false, ["sign", "verify"]);
}

export async function createSession(env, now = Math.floor(Date.now() / 1000)) {
  const nonce = base64url(crypto.getRandomValues(new Uint8Array(16)));
  const payload = `v1.${now + SESSION_TTL}.${nonce}`;
  const signature = await crypto.subtle.sign("HMAC", await sessionKey(env), encoder.encode(payload));
  return payload + "." + base64url(signature);
}

export async function authenticated(request, env, now = Math.floor(Date.now() / 1000)) {
  const cookies = (request.headers.get("cookie") || "").split(";").map((value) => value.trim()).filter((value) => value.startsWith(COOKIE_NAME + "="));
  if (cookies.length !== 1) return false;
  const token = cookies[0].slice(COOKIE_NAME.length + 1);
  if (token.length > 256) return false;
  const parts = token.split(".");
  if (parts.length !== 4 || parts[0] !== "v1" || !/^\d{10}$/.test(parts[1]) || !/^[A-Za-z0-9_-]{22}$/.test(parts[2])) return false;
  const expires = Number(parts[1]);
  if (expires <= now || expires > now + SESSION_TTL) return false;
  try {
    return await crypto.subtle.verify("HMAC", await sessionKey(env), unbase64url(parts[3]), encoder.encode(parts.slice(0, 3).join(".")));
  } catch {
    return false;
  }
}

function securityHeaders() {
  return new Headers({
    "cache-control": "private, no-store, no-transform",
    "cdn-cache-control": "no-store",
    "cloudflare-cdn-cache-control": "no-store",
    "vary": "Cookie",
    "x-content-type-options": "nosniff",
    "x-frame-options": "DENY",
    // Native Form-POSTs brauchen ihre Origin; no-referrer würde sie auf null setzen.
    "referrer-policy": "same-origin",
    "cross-origin-resource-policy": "same-origin",
    "cross-origin-opener-policy": "same-origin",
    "permissions-policy": "camera=(), microphone=(), geolocation=(), payment=()",
    "strict-transport-security": "max-age=31536000",
    "x-robots-tag": "noindex, nofollow, noarchive",
    "content-security-policy": `default-src 'none'; script-src ${SCRIPT_HASHES.length ? SCRIPT_HASHES.map((hash) => `'${hash}'`).join(" ") : "'none'"}; style-src 'unsafe-inline'; img-src 'self' data:; media-src 'self'; font-src 'self'; connect-src 'self'; form-action 'self'; base-uri 'none'; object-src 'none'; frame-ancestors 'none'`,
  });
}

function respond(body, status = 200, extra = {}) {
  const headers = securityHeaders();
  Object.entries(extra).forEach(([name, value]) => headers.set(name, value));
  return new Response(body, { status, headers });
}

function redirect(location, cookie) {
  return respond(null, 303, { location, ...(cookie ? { "set-cookie": cookie } : {}) });
}

function safeNext(value) {
  if (typeof value !== "string" || !/^\/(?:analyse\/)?(?:#[A-Za-z0-9_-]+)?$/.test(value)) return "/";
  return value;
}

async function readForm(request) {
  if ((request.headers.get("content-type") || "").split(";")[0].trim() !== "application/x-www-form-urlencoded") return null;
  const reader = request.body?.getReader();
  if (!reader) return null;
  const chunks = [];
  let length = 0;
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    length += value.length;
    if (length > 2048) { await reader.cancel(); return null; }
    chunks.push(value);
  }
  const bytes = new Uint8Array(length);
  let offset = 0;
  chunks.forEach((chunk) => { bytes.set(chunk, offset); offset += chunk.length; });
  return new URLSearchParams(new TextDecoder().decode(bytes));
}

export function parseRange(header, size) {
  if (!header) return null;
  const match = /^bytes=(\d*)-(\d*)$/.exec(header);
  if (!match || (!match[1] && !match[2]) || size === 0) return false;
  let start, end;
  if (!match[1]) {
    const suffix = Number(match[2]);
    if (!Number.isSafeInteger(suffix) || suffix <= 0) return false;
    start = Math.max(0, size - suffix); end = size - 1;
  } else {
    start = Number(match[1]); end = match[2] ? Number(match[2]) : size - 1;
    if (!Number.isSafeInteger(start) || !Number.isSafeInteger(end) || start >= size || start > end) return false;
    end = Math.min(end, size - 1);
  }
  return { offset: start, length: end - start + 1 };
}

function etagMatches(value, etag) {
  return value && value.split(",").some((part) => part.trim() === "*" || part.trim().replace(/^W\//, "") === etag);
}

async function serveContent(request, env, path) {
  if (!Object.hasOwn(CONTENT, path)) return respond("Nicht gefunden.", 404, { "content-type": "text/plain; charset=utf-8" });
  const entry = CONTENT[path];
  const metadata = await env.COURSE_BUCKET.head(entry.key);
  if (!metadata || metadata.size !== entry.bytes) return respond("Der Kursinhalt ist vorübergehend nicht verfügbar.", 503);
  const headers = { "content-type": entry.type, "etag": metadata.httpEtag, "last-modified": metadata.uploaded.toUTCString(), "accept-ranges": "bytes" };
  if (etagMatches(request.headers.get("if-none-match"), metadata.httpEtag)) return respond(null, 304, headers);
  if (request.method === "HEAD") return respond(null, 200, { ...headers, "content-length": String(metadata.size) });
  let rangeHeader = request.headers.get("range");
  const ifRange = request.headers.get("if-range");
  if (ifRange && ifRange !== metadata.httpEtag && !(Number.isFinite(Date.parse(ifRange)) && Math.floor(metadata.uploaded.getTime() / 1000) <= Math.floor(Date.parse(ifRange) / 1000))) rangeHeader = null;
  const range = parseRange(rangeHeader, metadata.size);
  if (range === false) return respond(null, 416, { ...headers, "content-range": `bytes */${metadata.size}` });
  const object = await env.COURSE_BUCKET.get(entry.key, range ? { range } : undefined);
  if (!object?.body) return respond("Der Kursinhalt ist vorübergehend nicht verfügbar.", 503);
  const length = range ? range.length : object.size;
  if (range) headers["content-range"] = `bytes ${range.offset}-${range.offset + range.length - 1}/${metadata.size}`;
  headers["content-length"] = String(length);
  return respond(object.body, range ? 206 : 200, headers);
}

export async function handleRequest(request, env) {
  const url = new URL(request.url);
  const origin = env.SITE_ORIGIN || "https://pocock.sp23.online";
  if (url.origin !== origin) {
    if (url.protocol === "http:" && url.hostname === new URL(origin).hostname) return respond(null, 308, { location: origin + url.pathname + url.search });
    return respond("Nicht gefunden.", 404);
  }
  if (!env.SESSION_KEY || env.SESSION_KEY.length < 32 || !env.PASSWORD_VERIFIER || !env.COURSE_BUCKET || !env.LOGIN_LIMITER) return respond("Der Kursbereich wird vorbereitet.", 503);
  if (request.method === "POST" && (url.pathname === "/login" || url.pathname === "/logout")) {
    if (request.headers.get("origin") !== origin) return respond("Anfrage nicht erlaubt.", 403);
    if (url.pathname === "/logout") return redirect("/login", `${COOKIE_NAME}=; Path=/; Secure; HttpOnly; SameSite=Strict; Max-Age=0`);
    const ip = request.headers.get("cf-connecting-ip") || "unknown";
    const { success } = await env.LOGIN_LIMITER.limit({ key: "pocock-login:" + ip });
    if (!success) return respond(loginPage({ error: "Zu viele Versuche. Bitte warte eine Minute." }), 429, { "content-type": "text/html; charset=utf-8", "retry-after": "60" });
    const form = await readForm(request);
    if (!form || form.getAll("password").length !== 1) return respond("Ungültige Anmeldung.", 400);
    const next = safeNext(form.get("next"));
    if (!await verifyPassword(form.get("password"), env.PASSWORD_VERIFIER)) return respond(loginPage({ error: "Das Passwort ist nicht korrekt.", next }), 401, { "content-type": "text/html; charset=utf-8" });
    const token = await createSession(env);
    return redirect(next, `${COOKIE_NAME}=${token}; Path=/; Secure; HttpOnly; SameSite=Strict; Max-Age=${SESSION_TTL}`);
  }
  if (!["GET", "HEAD"].includes(request.method)) return respond("Methode nicht erlaubt.", 405, { allow: "GET, HEAD, POST" });
  const loggedIn = await authenticated(request, env);
  if (url.pathname === "/login" || (!loggedIn && url.pathname === "/")) {
    if (loggedIn) return redirect("/");
    return respond(request.method === "HEAD" ? null : loginPage({ next: safeNext(url.searchParams.get("next")) }), 200, { "content-type": "text/html; charset=utf-8" });
  }
  if (!loggedIn) {
    if (url.pathname === "/analyse/" || url.pathname === "/analyse") return redirect("/login?next=%2Fanalyse%2F");
    return respond("Anmeldung erforderlich.", 401, { "content-type": "text/plain; charset=utf-8" });
  }
  if (url.pathname === "/analyse") return redirect("/analyse/");
  return serveContent(request, env, url.pathname);
}

export default {
  async fetch(request, env) {
    try { return await handleRequest(request, env); }
    catch { return respond("Der Kursbereich ist vorübergehend nicht verfügbar.", 503); }
  },
};
