import { DOWNLOAD_PANEL, DOWNLOAD_STYLE } from "./downloads.mjs";

// Nur diese öffentlichen Metadaten und selbst erzeugten Icons sind ohne Sitzung erreichbar.
export const PUBLIC_ASSETS = Object.freeze({
  "/manifest.webmanifest": "application/manifest+json; charset=utf-8",
  "/favicon.ico": "image/vnd.microsoft.icon",
  "/icons/favicon-16-v1.png": "image/png",
  "/icons/favicon-32-v1.png": "image/png",
  "/icons/apple-touch-icon-v1.png": "image/png",
  "/icons/icon-192-v1.png": "image/png",
  "/icons/icon-512-v1.png": "image/png",
});

export const PWA_HEAD = `<!--pocock-pwa:start-->
<link rel="manifest" href="/manifest.webmanifest">
<link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48">
<link rel="icon" href="/icons/favicon-32-v1.png" type="image/png" sizes="32x32">
<link rel="icon" href="/icons/favicon-16-v1.png" type="image/png" sizes="16x16">
<link rel="apple-touch-icon" href="/icons/apple-touch-icon-v1.png" sizes="180x180">
<meta name="theme-color" content="#f3eee4">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Pocock Kurs">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<!--pocock-pwa:end-->`;

export function addPwaHead(response) {
  return new HTMLRewriter().on("head", {
    element(head) { head.append(PWA_HEAD + DOWNLOAD_STYLE, { html: true }); },
  }).on('nav[aria-label="Kursbereich"] > form', {
    element(form) { form.before(DOWNLOAD_PANEL, { html: true }); },
  }).transform(response);
}
