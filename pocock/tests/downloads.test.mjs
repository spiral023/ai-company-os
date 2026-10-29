import test from "node:test";
import assert from "node:assert/strict";
import { DOWNLOADS } from "../download-manifest.mjs";
import { DOWNLOAD_PANEL } from "../downloads.mjs";
import worker, { handleRequest, createSession, COOKIE_NAME } from "../worker.mjs";

const ORIGIN = "https://pocock.sp23.online";
function fixture() {
  const reads = [];
  const byKey = new Map(Object.values(DOWNLOADS).map(entry => [entry.key, entry]));
  const env = {
    SITE_ORIGIN: ORIGIN, SESSION_KEY: "download-test-only-signing-key-".repeat(2), PASSWORD_VERIFIER: "download-test-only-verifier",
    LOGIN_LIMITER: { limit() { throw new Error("GET benötigt kein Login-Limit"); } },
    PUBLIC_FILES: { fetch() { throw new Error("Kursdownloads dürfen nicht aus der öffentlichen Ablage kommen"); } },
    COURSE_BUCKET: {
      async head(key) {
        reads.push(["head", key]);
        const entry = byKey.get(key);
        return entry ? { size: entry.bytes, httpEtag: '"' + entry.md5 + '"', uploaded: new Date("2026-10-29T12:00:00Z") } : null;
      },
      async get(key, options) {
        reads.push(["get", key]);
        const entry = byKey.get(key);
        const offset = options?.range?.offset || 0, length = options?.range?.length || 32;
        return { size: entry.bytes, body: Uint8Array.from({ length }, (_, index) => (offset + index) % 251) };
      },
    },
  };
  return { env, reads };
}
async function request(path, env, method = "GET", headers = {}) {
  const cookie = COOKIE_NAME + "=" + await createSession(env);
  return new Request(ORIGIN + path, { method, headers: { cookie, ...headers } });
}

test("Downloadbereich bietet genau Deutsch und Originalenglisch als HTML und Markdown", () => {
  assert.deepEqual(Object.keys(DOWNLOADS).sort(), ["/downloads/de.html", "/downloads/de.md", "/downloads/en.html", "/downloads/en.md"]);
  for (const [path, entry] of Object.entries(DOWNLOADS)) {
    assert.ok(DOWNLOAD_PANEL.includes(`href="${path}" download="${entry.filename}"`));
    assert.match(entry.filename, /^software-factories-(de|en)\.(html|md)$/);
    assert.match(entry.key, /^kurs\/downloads\/[a-f0-9]{20}\//);
  }
  assert.match(DOWNLOAD_PANEL, /ohne Videos/);
  assert.match(DOWNLOAD_PANEL, /Originaltext/);
});

test("Alle vier Downloads verweigern anonyme, manipulierte und abgelaufene Sitzungen vor R2", async () => {
  const { env, reads } = fixture();
  for (const path of Object.keys(DOWNLOADS)) {
    for (const cookie of ["", COOKIE_NAME + "=forged", COOKIE_NAME + "=" + await createSession(env, 1)]) {
      const response = await handleRequest(new Request(ORIGIN + path, { headers: { cookie, Range: "bytes=0-31", "If-None-Match": "*" } }), env);
      assert.equal(response.status, 401);
      assert.equal(response.headers.get("content-disposition"), null);
      assert.equal(response.headers.get("content-range"), null);
      assert.match(response.headers.get("cache-control"), /no-store/);
    }
  }
  assert.deepEqual(reads, []);
});

test("HEAD liefert alle Exportdateien als private Attachments mit exakter Dateigröße", async () => {
  const { env, reads } = fixture();
  for (const [path, entry] of Object.entries(DOWNLOADS)) {
    const response = await handleRequest(await request(path, env, "HEAD"), env);
    assert.equal(response.status, 200);
    assert.equal(response.headers.get("content-type"), entry.type);
    assert.equal(response.headers.get("content-disposition"), `attachment; filename="${entry.filename}"`);
    assert.equal(response.headers.get("content-length"), String(entry.bytes));
    assert.match(response.headers.get("cache-control"), /private, no-store/);
    assert.equal(response.headers.get("content-security-policy").includes("script-src"), false);
    assert.equal(await response.text(), "");
  }
  assert.ok(reads.every(([method]) => method === "head"));
});

test("HTML- und Markdown-Bytebereiche bleiben unveränderte Attachments ohne HTML-Injektion", async () => {
  const { env } = fixture();
  for (const [path, entry] of Object.entries(DOWNLOADS)) {
    const response = await handleRequest(await request(path, env, "GET", { Range: "bytes=10-41" }), env);
    assert.equal(response.status, 206);
    assert.equal(response.headers.get("content-range"), `bytes 10-41/${entry.bytes}`);
    assert.equal(response.headers.get("content-disposition"), `attachment; filename="${entry.filename}"`);
    assert.deepEqual([...new Uint8Array(await response.arrayBuffer())], Array.from({ length: 32 }, (_, index) => index + 10));
  }
});

test("Unbekannte Exportpfade und Schreibmethoden können keine R2-Dateien auswählen", async () => {
  const { env, reads } = fixture();
  for (const path of ["/downloads/de.zip", "/downloads/private.mp4", "/downloads/en.pdf", "/downloads/"]) {
    assert.equal((await handleRequest(await request(path, env), env)).status, 404);
  }
  assert.equal((await handleRequest(await request("/downloads/de.md", env, "POST"), env)).status, 405);
  assert.deepEqual(reads, []);
});

test("Fehlende Exportdateien scheitern geschlossen ohne interne Details", async () => {
  const { env } = fixture();
  env.COURSE_BUCKET.head = async () => null;
  const response = await worker.fetch(await request("/downloads/de.html", env), env);
  assert.equal(response.status, 503);
  assert.equal(response.headers.get("content-disposition"), null);
  assert.match(response.headers.get("cache-control"), /no-store/);
});
