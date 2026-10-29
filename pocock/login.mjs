import { PWA_HEAD } from "./pwa.mjs";

export function loginPage({ error = "", next = "/" } = {}) {
  const escape = (text) => text.replaceAll("&", "&amp;").replaceAll('"', "&quot;").replaceAll("<", "&lt;");
  return `<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>Kurs öffnen · Software Factories</title>${PWA_HEAD}
<style>
:root{color-scheme:light;--paper:#f3eee4;--ink:#1c1712;--muted:#70675d;--accent:#9a4523;--line:#d9cebd}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:18px/1.65 Georgia,serif;min-height:100svh;display:grid;grid-template-columns:minmax(24px,1fr) minmax(0,460px) minmax(24px,1fr)}
main{grid-column:2;align-self:center;padding:60px 0}header{margin-bottom:42px}.eyebrow{font:700 11px/1.4 ui-sans-serif,sans-serif;letter-spacing:.21em;text-transform:uppercase;color:var(--accent)}
h1{font-size:clamp(42px,8vw,64px);line-height:1.03;letter-spacing:-.045em;font-weight:600;margin:16px 0 22px}p{color:var(--muted);margin:0}.rule{width:48px;height:3px;background:var(--accent);margin-bottom:28px}
label{display:block;font:600 14px/1.5 ui-sans-serif,sans-serif;margin-bottom:10px}input{display:block;width:100%;padding:16px;border:1px solid var(--line);border-radius:8px;background:#fffaf2;color:var(--ink);font:18px/1.4 ui-sans-serif,sans-serif}
input:focus-visible,button:focus-visible{outline:2px solid var(--accent);outline-offset:4px}button{margin-top:18px;min-height:54px;width:100%;border:0;border-radius:8px;background:var(--ink);color:#fff8ed;font:600 15px/1.4 ui-sans-serif,sans-serif;cursor:pointer}button:hover{background:#3a2e24}
.error{color:#a02c22;margin:14px 0 0;font:14px/1.5 ui-sans-serif,sans-serif}.foot{margin-top:30px;font:12px/1.5 ui-sans-serif,sans-serif;color:var(--muted)}
.install{margin-top:22px;font:13px/1.6 ui-sans-serif,sans-serif}.install summary{color:var(--accent);cursor:pointer}.install-preview{display:flex;gap:14px;align-items:flex-start;margin-top:14px}.install-preview img{border-radius:12px;flex-shrink:0}.install-preview strong{color:var(--ink)}.install summary:focus-visible{outline:2px solid var(--accent);outline-offset:4px}@media(display-mode:standalone){.install{display:none}}
</style></head><body><main><header><div class="rule"></div><div class="eyebrow">Privater Kursbereich</div><h1>Software<br>Factories</h1><p>Matt Pococks Kurs auf Deutsch.<br>Mit Videos und ausführlicher Analyse.</p></header>
<form method="post" action="/login"><label for="password">Passwort</label><input id="password" name="password" type="password" autocomplete="current-password" required autofocus maxlength="256" aria-describedby="login-error"><input type="hidden" name="next" value="${escape(next)}"><button type="submit">Kurs öffnen <span aria-hidden="true">→</span></button>
<p id="login-error" class="error" role="alert">${escape(error)}</p></form><p class="foot">Dein Lernfortschritt bleibt in diesem Browser gespeichert.</p><details class="install"><summary>Auf dem iPhone installieren</summary><div class="install-preview"><img src="/icons/apple-touch-icon-v1.png" alt="" width="48" height="48"><p><strong>Pocock Kurs</strong><br>In Safari: Teilen → Zum Home-Bildschirm. „Als Web-App öffnen“ aktivieren und auf „Hinzufügen“ tippen.</p></div></details></main></body></html>`;
}
