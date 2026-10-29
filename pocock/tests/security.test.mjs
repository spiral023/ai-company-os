import test from "node:test";
import assert from "node:assert/strict";
import { pbkdf2Sync } from "node:crypto";
import worker, { handleRequest, createSession, authenticated, COOKIE_NAME, SESSION_TTL } from "../worker.mjs";
import { CONTENT, SCRIPT_HASHES } from "../content-manifest.mjs";

const ORIGIN = "https://pocock.sp23.online";
const PASSWORD = "test-only-passphrase";
const salt = "1a".repeat(16);
const verifier = "pbkdf2_sha256$100000$" + salt + "$" + pbkdf2Sync(PASSWORD, Buffer.from(salt, "hex"), 100000, 32, "sha256").toString("hex");
const entriesByKey = new Map(Object.values(CONTENT).map((entry) => [entry.key, entry]));

function environment() {
  const reads = [];
  const env = {
    SITE_ORIGIN: ORIGIN,
    SESSION_KEY: "test-only-session-key-".repeat(3),
    PASSWORD_VERIFIER: verifier,
    LOGIN_LIMITER: { async limit() { return { success: true }; } },
    COURSE_BUCKET: {
      async head(key) {
        reads.push(["head", key]);
        const entry = entriesByKey.get(key);
        return entry ? { size: entry.bytes, httpEtag: '"' + entry.md5 + '"', uploaded: new Date("2026-10-29T10:00:00.321Z") } : null;
      },
      async get(key, options) {
        reads.push(["get", key, options]);
        const entry = entriesByKey.get(key);
        const offset = options?.range?.offset || 0;
        const length = options?.range?.length || 19;
        // Streaming-Doppel mit bekanntem Byte-Muster, ohne komplette Videos zu puffern.
        const body = new Uint8Array(length);
        body.forEach((_, index) => { body[index] = (offset + index) % 251; });
        return { body, size: entry.bytes };
      },
    },
  };
  return { env, reads };
}

function request(path = "/", { cookie, method = "GET", headers = {}, body } = {}) {
  return new Request(ORIGIN + path, { method, headers: { ...(cookie ? { cookie } : {}), ...headers }, body });
}

async function cookie(env) { return COOKIE_NAME + "=" + await createSession(env); }
function login(body = new URLSearchParams({ password: PASSWORD, next: "/" }), origin = ORIGIN) {
  return request("/login", { method: "POST", body, headers: { origin, "content-type": "application/x-www-form-urlencoded", "cf-connecting-ip": "192.0.2.10" } });
}

test("Anonyme Kurs- und Medienzugriffe lesen niemals R2", async () => {
  const { env, reads } = environment();
  for (const path of ["/", "/analyse/", "/medien/001.png", "/videos/001.mp4", "/worker.mjs", "/index.html"]) {
    const response = await handleRequest(request(path, { headers: { range: "bytes=0-10", "if-none-match": "*" } }), env);
    assert.ok([200, 303, 401].includes(response.status));
    assert.match(response.headers.get("cache-control"), /no-store/);
    assert.equal(response.headers.get("content-range"), null);
  }
  assert.deepEqual(reads, []);
});

test("Falsches Passwort erzeugt keine Session und keinen Objektzugriff", async () => {
  const { env, reads } = environment();
  const response = await handleRequest(login(new URLSearchParams({ password: "incorrect" })), env);
  assert.equal(response.status, 401);
  assert.equal(response.headers.get("set-cookie"), null);
  assert.match(await response.text(), /nicht korrekt/);
  assert.deepEqual(reads, []);
});

test("Anmeldung setzt nur eine geschützte Host-Session", async () => {
  const { env } = environment();
  const response = await handleRequest(login(), env);
  assert.equal(response.status, 303);
  assert.equal(response.headers.get("location"), "/");
  const setCookie = response.headers.get("set-cookie");
  for (const flag of [COOKIE_NAME + "=", "Path=/", "Secure", "HttpOnly", "SameSite=Strict", "Max-Age=" + SESSION_TTL]) assert.ok(setCookie.includes(flag));
  assert.equal(setCookie.includes("Domain="), false);
  assert.equal(await authenticated(request("/", { cookie: setCookie.split(";")[0] }), env), true);
});

test("Manipulierte, abgelaufene und doppelte Cookies werden abgewiesen", async () => {
  const { env, reads } = environment();
  const valid = await createSession(env);
  const parts = valid.split(".");
  parts[1] = String(Number(parts[1]) + 30);
  for (const value of [parts.join("."), valid.slice(0, -2) + "aa", await createSession(env, Math.floor(Date.now() / 1000) - SESSION_TTL - 1), "v1.invalid.invalid.invalid"]) {
    const response = await handleRequest(request("/videos/001.mp4", { cookie: COOKIE_NAME + "=" + value }), env);
    assert.equal(response.status, 401);
  }
  const duplicate = `${COOKIE_NAME}=${valid}; ${COOKIE_NAME}=${valid}`;
  assert.equal(await authenticated(request("/", { cookie: duplicate }), env), false);
  assert.deepEqual(reads, []);
});

test("Passwort- und Signaturschlüsselrotation widerrufen bestehende Sessions", async () => {
  const { env } = environment();
  const session = await cookie(env);
  assert.equal(await authenticated(request("/", { cookie: session }), { ...env, PASSWORD_VERIFIER: verifier + "changed" }), false);
  assert.equal(await authenticated(request("/", { cookie: session }), { ...env, SESSION_KEY: "another-secret-".repeat(4) }), false);
});

test("Login und Logout erfordern die genaue Origin", async () => {
  const { env } = environment();
  for (const origin of ["https://other.sp23.online", "https://evil.example", "null", ""]) {
    assert.equal((await handleRequest(login(undefined, origin), env)).status, 403);
    assert.equal((await handleRequest(request("/logout", { method: "POST", headers: { origin } }), env)).status, 403);
  }
});

test("Das nächste Ziel kann keine fremde Adresse einschleusen", async () => {
  const { env } = environment();
  for (const next of ["https://evil.example", "//evil.example", "/\\evil.example", "/%2f%2fevil.example", '/" onfocus="alert(1)']) {
    const response = await handleRequest(login(new URLSearchParams({ password: PASSWORD, next })), env);
    assert.equal(response.headers.get("location"), "/");
  }
  const response = await handleRequest(login(new URLSearchParams({ password: PASSWORD, next: "/analyse/#kurstransfer" })), env);
  assert.equal(response.headers.get("location"), "/analyse/#kurstransfer");
});

test("Rate-Limit verhindert Passwortprüfung und R2-Zugriff", async () => {
  const { env, reads } = environment();
  env.LOGIN_LIMITER.limit = async () => ({ success: false });
  const response = await handleRequest(login(), env);
  assert.equal(response.status, 429);
  assert.equal(response.headers.get("retry-after"), "60");
  assert.equal(response.headers.get("set-cookie"), null);
  assert.deepEqual(reads, []);
});

test("Fehlende Sicherheitskonfiguration bleibt geschlossen", async () => {
  const { env, reads } = environment();
  for (const name of ["SESSION_KEY", "PASSWORD_VERIFIER", "LOGIN_LIMITER", "COURSE_BUCKET"]) {
    assert.equal((await handleRequest(request("/videos/001.mp4"), { ...env, [name]: undefined })).status, 503);
  }
  assert.deepEqual(reads, []);
});

test("Nicht unterstützte Schreibmethoden erreichen den Bucket nicht", async () => {
  const { env, reads } = environment();
  for (const method of ["PUT", "DELETE", "PATCH", "OPTIONS"]) assert.equal((await handleRequest(request("/videos/001.mp4", { cookie: await cookie(env), method }), env)).status, 405);
  assert.deepEqual(reads, []);
});

test("Überlange oder mehrdeutige Login-Daten werden abgewiesen", async () => {
  const { env } = environment();
  assert.equal((await handleRequest(login(new URLSearchParams({ password: "a".repeat(3000) })), env)).status, 400);
  assert.equal((await handleRequest(login(new URLSearchParams([["password", PASSWORD], ["password", PASSWORD]])), env)).status, 400);
  assert.equal((await handleRequest(request("/login", { method: "POST", body: '{}', headers: { origin: ORIGIN, "content-type": "application/json" } }), env)).status, 400);
});

test("Video-Range liefert genau den angefragten Bytebereich", async () => {
  const { env, reads } = environment();
  const response = await handleRequest(request("/videos/001.mp4", { cookie: await cookie(env), headers: { range: "bytes=10-19" } }), env);
  assert.equal(response.status, 206);
  assert.equal(response.headers.get("content-range"), `bytes 10-19/${CONTENT["/videos/001.mp4"].bytes}`);
  assert.equal(response.headers.get("content-length"), "10");
  assert.deepEqual([...new Uint8Array(await response.arrayBuffer())], Array.from({ length: 10 }, (_, i) => i + 10));
  assert.deepEqual(reads[1][2], { range: { offset: 10, length: 10 } });
});

test("Suffix-Range funktioniert und ungültige Ranges liefern 416", async () => {
  const { env, reads } = environment();
  const session = await cookie(env), size = CONTENT["/videos/001.mp4"].bytes;
  const response = await handleRequest(request("/videos/001.mp4", { cookie: session, headers: { range: "bytes=-8" } }), env);
  assert.equal(response.status, 206);
  assert.equal(response.headers.get("content-range"), `bytes ${size - 8}-${size - 1}/${size}`);
  for (const range of [`bytes=${size}-`, "bytes=8-2", "bytes=0-1,5-6", "bytes=-0", "bytes=999999999999999999999-", "invalid"]) {
    const result = await handleRequest(request("/videos/001.mp4", { cookie: session, headers: { range } }), env);
    assert.equal(result.status, 416);
    assert.equal(result.headers.get("content-range"), `bytes */${size}`);
  }
  assert.equal(reads.filter(([method]) => method === "get").length, 1);
});

test("HEAD liefert Metadaten und startet keinen Objektstream", async () => {
  const { env, reads } = environment();
  const response = await handleRequest(request("/videos/001.mp4", { cookie: await cookie(env), method: "HEAD" }), env);
  assert.equal(response.status, 200);
  assert.equal(response.headers.get("content-length"), String(CONTENT["/videos/001.mp4"].bytes));
  assert.equal(await response.text(), "");
  assert.equal(reads.length, 1);
});

test("Conditional Requests werden erst nach Authentifizierung ausgewertet", async () => {
  const { env, reads } = environment();
  const response = await handleRequest(request("/videos/001.mp4", { cookie: await cookie(env), headers: { "if-none-match": "*" } }), env);
  assert.equal(response.status, 304);
  assert.equal(await response.text(), "");
  assert.equal(reads.length, 1);
});

test("If-Range akzeptiert das ausgegebene HTTP-Datum mit Sekundenpräzision", async () => {
  const { env } = environment();
  const response = await handleRequest(request("/videos/001.mp4", { cookie: await cookie(env), headers: { range: "bytes=0-7", "if-range": "Thu, 29 Oct 2026 10:00:00 GMT" } }), env);
  assert.equal(response.status, 206);
});

test("Ausgefallenes R2 liefert keine Details oder gespeicherte Fehlseiten", async () => {
  const { env } = environment();
  env.COURSE_BUCKET.head = async () => { throw new Error("private provider internals"); };
  const response = await worker.fetch(request("/", { cookie: await cookie(env) }), env);
  assert.equal(response.status, 503);
  assert.equal((await response.text()).includes("provider internals"), false);
  assert.match(response.headers.get("cache-control"), /no-store/);
});

test("Nur freigegebene Objektrouten sind erreichbar", async () => {
  const { env, reads } = environment();
  for (const path of ["/index.de.html", "/content-manifest.mjs", "/videos/999.mp4", "/medien/999.png", "/releases/private/index.html", "/.dev.vars"]) assert.equal((await handleRequest(request(path, { cookie: await cookie(env) }), env)).status, 404);
  assert.deepEqual(reads, []);
  assert.equal(Object.keys(CONTENT).length, 196);
  assert.ok(SCRIPT_HASHES.every((hash) => /^sha256-[A-Za-z0-9+/]+=*$/.test(hash)));
});

test("Logout löscht die geschützte Session und bleibt gegen GET geschützt", async () => {
  const { env } = environment();
  const response = await handleRequest(request("/logout", { method: "POST", headers: { origin: ORIGIN }, cookie: await cookie(env) }), env);
  assert.equal(response.status, 303);
  assert.ok(response.headers.get("set-cookie").includes("Max-Age=0"));
  assert.ok(response.headers.get("set-cookie").includes("HttpOnly; SameSite=Strict"));
  assert.equal((await handleRequest(request("/logout", { cookie: await cookie(env) }), env)).status, 404);
});

test("Geschützte Antworten erlauben weder Einbettung noch öffentliche Caches", async () => {
  const { env } = environment();
  const response = await handleRequest(request("/medien/001.png", { cookie: await cookie(env), method: "HEAD" }), env);
  assert.equal(response.status, 200);
  assert.equal(response.headers.get("access-control-allow-origin"), null);
  assert.equal(response.headers.get("cross-origin-resource-policy"), "same-origin");
  assert.equal(response.headers.get("referrer-policy"), "same-origin");
  assert.match(response.headers.get("content-security-policy"), /frame-ancestors 'none'/);
  assert.equal(response.headers.get("content-security-policy").includes("script-src 'unsafe-inline'"), false);
  assert.match(response.headers.get("cache-control"), /private, no-store/);
  assert.equal(response.headers.get("cloudflare-cdn-cache-control"), "no-store");
});
