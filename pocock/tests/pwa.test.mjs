import test from "node:test";
import assert from "node:assert/strict";
import { readFile, readdir } from "node:fs/promises";
import { PUBLIC_ASSETS, PWA_HEAD } from "../pwa.mjs";
import { loginPage } from "../login.mjs";
import { handleRequest, createSession, COOKIE_NAME } from "../worker.mjs";
import { CONTENT } from "../content-manifest.mjs";

const ORIGIN = "https://pocock.sp23.online";
const publicRoot = new URL("../public/", import.meta.url);
const manifest = JSON.parse(await readFile(new URL("manifest.webmanifest", publicRoot), "utf8"));

function environment() {
  const requests = [];
  return { requests, env: {
    SITE_ORIGIN: ORIGIN,
    SESSION_KEY: "pwa-test-only-signing-key-".repeat(3),
    PASSWORD_VERIFIER: "pwa-test-only-verifier",
    LOGIN_LIMITER: { limit() { throw new Error("Öffentliche Assets benötigen kein Login-Limit"); } },
    COURSE_BUCKET: { head() { throw new Error("Öffentliche Assets dürfen R2 nicht lesen"); } },
    PUBLIC_FILES: { async fetch(request) {
      requests.push(request);
      const path = new URL(request.url).pathname;
      const bytes = await readFile(new URL(path.slice(1), publicRoot));
      return new Response(request.method === "HEAD" ? null : bytes, { headers: { "content-length": String(bytes.length), etag: '"public-icon-fixture"' } });
    } },
  } };
}

test("Manifest startet im geschützten Stammverzeichnis als deutsche Standalone-App", () => {
  assert.equal(manifest.id, "/");
  assert.equal(manifest.scope, "/");
  assert.equal(manifest.start_url, "/");
  assert.equal(manifest.display, "standalone");
  assert.equal(manifest.lang, "de");
  assert.equal(manifest.short_name, "Pocock Kurs");
  assert.deepEqual(manifest.icons.map(icon => icon.sizes), ["192x192", "512x512"]);
  assert.ok(manifest.icons.every(icon => Object.hasOwn(PUBLIC_ASSETS, icon.src) && icon.purpose === "any"));
});

test("Alle PNG-Icons haben die angegebenen Abmessungen und einen deckenden Hintergrund", async () => {
  for (const [name, size] of [["favicon-16-v1", 16], ["favicon-32-v1", 32], ["apple-touch-icon-v1", 180], ["icon-192-v1", 192], ["icon-512-v1", 512]]) {
    const bytes = await readFile(new URL("icons/" + name + ".png", publicRoot));
    assert.equal(bytes.subarray(0, 8).toString("hex"), "89504e470d0a1a0a");
    assert.equal(bytes.readUInt32BE(16), size);
    assert.equal(bytes.readUInt32BE(20), size);
    assert.equal(bytes[25], 2, "RGB ohne Alphakanal für " + name);
  }
  const ico = await readFile(new URL("favicon.ico", publicRoot));
  assert.equal(ico.readUInt16LE(2), 1);
  assert.equal(ico.readUInt16LE(4), 3);
  assert.deepEqual([ico[6], ico[22], ico[38]], [16, 32, 48]);
});

test("Die öffentliche Auslieferung enthält ausschließlich Manifest und freigegebene Icons", async () => {
  const actual = (await readdir(publicRoot, { recursive: true, withFileTypes: true })).filter(entry => entry.isFile()).map(entry => {
    const directory = entry.parentPath.replaceAll("\\", "/");
    return (directory.endsWith("/icons") ? "/icons/" : "/") + entry.name;
  });
  assert.deepEqual(actual.sort(), Object.keys(PUBLIC_ASSETS).sort());
  assert.ok(!actual.some(path => /\.(html|mp4|mjs|jsonc)$/.test(path)));
});

test("Manifest und Icons funktionieren ohne Sitzung und ohne konfigurierte Kurs-Secrets", async () => {
  const { env, requests } = environment();
  for (const path of Object.keys(PUBLIC_ASSETS)) {
    const response = await handleRequest(new Request(ORIGIN + path), { SITE_ORIGIN: ORIGIN, PUBLIC_FILES: env.PUBLIC_FILES });
    assert.equal(response.status, 200);
    assert.equal(response.headers.get("content-type"), PUBLIC_ASSETS[path]);
    assert.equal(response.headers.get("set-cookie"), null);
    assert.match(response.headers.get("cache-control"), /^public/);
    assert.equal(response.headers.get("vary"), "Accept-Encoding");
    const expected = await readFile(new URL(path.slice(1), publicRoot));
    assert.deepEqual(Buffer.from(await response.arrayBuffer()), expected);
  }
  assert.equal(requests.length, Object.keys(PUBLIC_ASSETS).length);
});

test("Öffentliche HEAD-Anfragen liefern Größe ohne Body", async () => {
  const { env } = environment();
  const response = await handleRequest(new Request(ORIGIN + "/icons/apple-touch-icon-v1.png", { method: "HEAD" }), env);
  assert.equal(response.status, 200);
  assert.ok(Number(response.headers.get("content-length")) > 0);
  assert.equal((await response.arrayBuffer()).byteLength, 0);
});

test("Öffentliche Asset-Anfragen übertragen keine Sitzung oder Authorization weiter", async () => {
  const { env, requests } = environment();
  await handleRequest(new Request(ORIGIN + "/manifest.webmanifest", { headers: { cookie: "private-cookie-fixture", authorization: "Bearer test-only", "if-none-match": '"old-manifest"' } }), env);
  assert.equal(requests[0].headers.get("cookie"), null);
  assert.equal(requests[0].headers.get("authorization"), null);
  assert.equal(requests[0].headers.get("if-none-match"), '"old-manifest"');
});

test("Öffentliche Ausnahmen gelten weder für Schreibmethoden noch fremde Origins", async () => {
  const { env, requests } = environment();
  assert.equal((await handleRequest(new Request(ORIGIN + "/manifest.webmanifest", { method: "POST" }), env)).status, 405);
  assert.equal((await handleRequest(new Request("https://foreign.example/manifest.webmanifest"), env)).status, 404);
  assert.equal((await handleRequest(new Request("http://pocock.sp23.online/manifest.webmanifest"), env)).status, 308);
  assert.equal(requests.length, 0);
});

test("Nicht freigegebene App-Dateien und Kursmedien bleiben hinter der Anmeldung", async () => {
  const { env, requests } = environment();
  for (const path of ["/icons/private.html", "/assets/portrait-source.png", "/public/manifest.webmanifest", "/sw.js", "/videos/001.mp4", "/medien/001.png"]) {
    const response = await handleRequest(new Request(ORIGIN + path), env);
    assert.equal(response.status, 401, path);
    assert.match(response.headers.get("cache-control"), /private, no-store/);
  }
  assert.equal(requests.length, 0);
});

test("Anmeldeansicht referenziert Manifest, Apple-Icon und deutsche Installationshilfe", () => {
  const html = loginPage();
  assert.ok(html.includes(PWA_HEAD));
  assert.match(html, /name="apple-mobile-web-app-capable" content="yes"/);
  assert.match(html, /name="apple-mobile-web-app-title" content="Pocock Kurs"/);
  assert.match(html, /Auf dem iPhone installieren/);
  assert.match(html, /manifest\.webmanifest/);
  assert.match(html, /@media\(display-mode:standalone\)/);
  assert.equal(/serviceWorker|caches\.open/.test(html), false);
});

test("Transformierte HTML-HEAD-Antworten verwenden weder rohe R2-ETags noch deren Länge", async () => {
  const { env } = environment();
  let reads = 0;
  env.COURSE_BUCKET = { async head(key) {
    reads++;
    const entry = Object.values(CONTENT).find(entry => entry.key === key);
    return { size: entry.bytes, httpEtag: '"raw-r2-html"' };
  }, get() { throw new Error("HEAD darf keinen HTML-Stream starten"); } };
  const session = COOKIE_NAME + "=" + await createSession(env);
  for (const path of ["/", "/analyse/"]) {
    const response = await handleRequest(new Request(ORIGIN + path, { method: "HEAD", headers: { cookie: session, "if-none-match": "*", range: "bytes=0-20" } }), env);
    assert.equal(response.status, 200);
    assert.equal(response.headers.get("etag"), null);
    assert.equal(response.headers.get("content-length"), null);
    assert.equal(response.headers.get("accept-ranges"), null);
    assert.match(response.headers.get("content-security-policy"), /manifest-src 'self'/);
    assert.match(response.headers.get("cache-control"), /private, no-store/);
  }
  assert.equal(reads, 2);
});
