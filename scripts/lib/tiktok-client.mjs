// Netzwerkzugriffe für den TikTok-Ingest.
//
// Zwei Quellen, weil keine allein reicht:
//   1. Apify-Actor scrape-creators/best-tiktok-transcripts-scraper — liefert
//      das Transkript, aber trotz Actor-Beschreibung KEINE Metadaten
//      (geprüft am 2026-08-29: nur id, url, transcript, credits_charged).
//   2. TikTok oEmbed — liefert Caption, Autorname und Cover, kostenlos und
//      ohne Key. Das Veröffentlichungsdatum steckt in der Video-ID selbst
//      (siehe dateFromVideoId in tiktok-ingest.mjs).

const ACTOR_ID = 'scrape-creators~best-tiktok-transcripts-scraper';
const API = 'https://api.apify.com/v2';
const POLL_MS = 3000;
const MAX_WAIT_MS = 5 * 60 * 1000;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function apifyRequest(url, options = {}) {
  const res = await fetch(url, options);
  const text = await res.text();
  if (!res.ok) {
    const detail = text.slice(0, 400);
    if (res.status === 401) throw new Error('401 — APIFY_TOKEN ungültig oder abgelaufen.');
    if (res.status === 402) {
      throw new Error(`402 — Apify-Guthaben aufgebraucht. In der Console aufladen. ${detail}`);
    }
    if (res.status === 404) throw new Error(`404 — Actor oder Run nicht gefunden. ${detail}`);
    throw new Error(`${res.status} ${res.statusText} — ${detail}`);
  }
  if (!text) throw new Error(`${res.status} — leere Antwort von ${url.split('?')[0]}`);
  return JSON.parse(text);
}

// Async starten und pollen statt run-sync: run-sync liefert den OUTPUT-Record
// des Key-Value-Stores, den dieser Actor nicht schreibt. Über den Run-Status
// bekommen wir zusätzlich die real abgerechneten Kosten.
export async function runTranscriptActor(token, urls, { onRunId } = {}) {
  const started = await apifyRequest(`${API}/acts/${ACTOR_ID}/runs?token=${token}`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ videos: urls }),
  });
  const run = started.data;
  if (onRunId) onRunId(run.id);

  const deadline = Date.now() + MAX_WAIT_MS;
  let current = run;
  while (['READY', 'RUNNING'].includes(current.status)) {
    if (Date.now() > deadline) {
      throw new Error(`Timeout nach 5 Minuten — Run ${run.id} steht auf ${current.status}.`);
    }
    await sleep(POLL_MS);
    current = (await apifyRequest(`${API}/actor-runs/${run.id}?token=${token}`)).data;
  }
  if (current.status !== 'SUCCEEDED') {
    throw new Error(`Actor-Run endete mit Status ${current.status} (Run-ID ${run.id}).`);
  }

  const items = await apifyRequest(
    `${API}/datasets/${current.defaultDatasetId}/items?token=${token}&clean=false&format=json`,
  );
  return { run: current, items: Array.isArray(items) ? items : [] };
}

// Caption, Autorname und Cover. Kein Key, keine Kosten. Schlägt der Abruf
// fehl, läuft der Ingest ohne diese Felder weiter — das Transkript ist der
// teure Teil und soll nicht an einer Nebenquelle scheitern.
export async function fetchOembed(videoUrl) {
  const target = `https://www.tiktok.com/oembed?url=${encodeURIComponent(videoUrl)}`;
  const res = await fetch(target, { headers: { accept: 'application/json' } });
  if (!res.ok) throw new Error(`oEmbed HTTP ${res.status}`);
  return res.json();
}

// vm.tiktok.com-Kurzlinks tragen keine Video-ID. Der Redirect führt auf die
// kanonische URL, aus der ID und Handle hervorgehen.
export async function resolveShortUrl(url) {
  const res = await fetch(url, { redirect: 'follow' });
  return res.url || url;
}
