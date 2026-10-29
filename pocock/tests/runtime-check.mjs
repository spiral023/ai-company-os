// Integration gegen Wrangler oder den Live-Worker; Passwort nur als Funktionsparameter.
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import { CONTENT } from "../content-manifest.mjs";
import { PUBLIC_ASSETS, PWA_HEAD } from "../pwa.mjs";
import { DOWNLOAD_PANEL, DOWNLOAD_STYLE } from "../downloads.mjs";
import { DOWNLOADS } from "../download-manifest.mjs";

export async function checkRuntime(origin, password) {
  const report = { origin, publicAssets: 0, html: [], downloads: [], mediaRequiresLogin: false };
  for (const path of Object.keys(PUBLIC_ASSETS)) {
    const response = await fetch(origin + path);
    assert.equal(response.status, 200, path);
    assert.equal(response.headers.get("content-type"), PUBLIC_ASSETS[path]);
    const expected = await readFile(new URL("../public" + path, import.meta.url));
    const actual = Buffer.from(await response.arrayBuffer());
    if (path === "/manifest.webmanifest") assert.deepEqual(JSON.parse(actual.toString("utf8")), JSON.parse(expected.toString("utf8")));
    else assert.deepEqual(actual, expected);
    report.publicAssets++;
  }
  const anonymous = await fetch(origin + "/videos/001.mp4", { headers: { Range: "bytes=0-63" } });
  assert.equal(anonymous.status, 401);
  assert.equal(anonymous.headers.get("content-range"), null);
  report.mediaRequiresLogin = true;
  const loginPage = await fetch(origin + "/login");
  assert.equal(loginPage.status, 200);
  assert.ok((await loginPage.text()).includes(PWA_HEAD));
  const login = await fetch(origin + "/login", {
    method: "POST", redirect: "manual",
    headers: { Origin: origin, "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ password }),
  });
  assert.equal(login.status, 303);
  const cookie = login.headers.get("set-cookie").split(";")[0];
  for (const [route, entry] of Object.entries(DOWNLOADS)) {
    const denied = await fetch(origin + route, { method: "HEAD", redirect: "manual" });
    assert.equal(denied.status, 401, route + " ist ohne Sitzung erreichbar");
    const head = await fetch(origin + route, { method: "HEAD", headers: { Cookie: cookie } });
    assert.equal(head.status, 200, route);
    assert.equal(head.headers.get("content-disposition"), `attachment; filename="${entry.filename}"`);
    assert.equal(Number(head.headers.get("content-length")), entry.bytes);
    assert.equal(head.headers.get("etag"), '"' + entry.md5 + '"');
    assert.match(head.headers.get("cache-control"), /private, no-store/);
    const part = await fetch(origin + route, { headers: { Cookie: cookie, Range: "bytes=0-63" } });
    assert.equal(part.status, 206);
    assert.equal(part.headers.get("content-range"), `bytes 0-63/${entry.bytes}`);
    assert.equal((await part.arrayBuffer()).byteLength, 64);
    if (route.endsWith(".md")) {
      const response = await fetch(origin + route, { headers: { Cookie: cookie } });
      assert.equal(createHash("sha256").update(Buffer.from(await response.arrayBuffer())).digest("hex"), entry.sha256);
    }
    report.downloads.push({ route, bytes: entry.bytes, attachment: true, range: 206, requiresLogin: true });
  }
  for (const route of ["/", "/analyse/"]) {
    const response = await fetch(origin + route, { headers: { Cookie: cookie, "If-None-Match": "*", Range: "bytes=0-63" } });
    assert.equal(response.status, 200, route);
    assert.equal(response.headers.get("etag"), null);
    assert.equal(response.headers.get("accept-ranges"), null);
    assert.match(response.headers.get("cache-control"), /private, no-store/);
    const html = await response.text();
    assert.ok(html.includes(PWA_HEAD), route + " hat keinen vollständigen PWA-Head");
    assert.equal(html.split("<!--pocock-pwa:start-->").length, 2);
    assert.ok(html.includes(DOWNLOAD_PANEL), route + " hat keinen Downloadbereich");
    const original = html.replace(PWA_HEAD, "").replace(DOWNLOAD_STYLE, "").replace(DOWNLOAD_PANEL, "");
    assert.equal(createHash("sha256").update(original).digest("hex"), CONTENT[route].sha256, route + " hat neben dem App-Head veränderte Kursdaten");
    for (const script of html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/g)) {
      const hash = "sha256-" + createHash("sha256").update(script[1]).digest("base64");
      assert.ok(response.headers.get("content-security-policy").includes(hash), "CSP blockiert ein Reader-Script");
    }
    report.html.push({ route, originalSha256Matches: true, pwaHeadPresent: true });
  }
  const logout = await fetch(origin + "/logout", { method: "POST", redirect: "manual", headers: { Origin: origin, Cookie: cookie } });
  assert.equal(logout.status, 303);
  assert.match(logout.headers.get("set-cookie"), /Max-Age=0/);
  return report;
}
