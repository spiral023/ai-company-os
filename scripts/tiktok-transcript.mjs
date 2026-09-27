// Testlauf: TikTok-Transkript über den Apify-Actor
// scrape-creators/best-tiktok-transcripts-scraper abrufen und die vollstaendige
// Antwort roh nach tmp/ schreiben. Noch keine Anbindung an 00_Inbox/Quellen —
// erst pruefen, was der Actor tatsaechlich liefert.
//
// Nutzung:
//   node scripts/tiktok-transcript.mjs <tiktok-url> [weitere-urls...]
//
// Benoetigt APIFY_TOKEN in .env.local (oder in der Umgebung).

import fs from 'fs';
import path from 'path';

const ACTOR_ID = 'scrape-creators~best-tiktok-transcripts-scraper';
const API = 'https://api.apify.com/v2';
const POLL_MS = 3000;
const MAX_WAIT_MS = 5 * 60 * 1000;
const rootDir = process.cwd();
const outDir = path.join(rootDir, 'tmp', 'apify');

function loadEnv() {
  try {
    process.loadEnvFile(path.join(rootDir, '.env.local'));
  } catch {
    // .env.local optional — Variable kann extern gesetzt sein
  }
}

function slugFromUrl(url) {
  const m = url.match(/@([^/]+)\/video\/(\d+)/);
  return m ? `${m[1]}-${m[2]}` : `tiktok-${Date.now()}`;
}

async function apify(url, options = {}) {
  const res = await fetch(url, options);
  const text = await res.text();
  if (!res.ok) {
    throw new Error(`${res.status} ${res.statusText} — ${text.slice(0, 400)}`);
  }
  if (!text) throw new Error(`${res.status} — leere Antwort von ${url.split('?')[0]}`);
  return JSON.parse(text);
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// Async starten und pollen statt run-sync: run-sync liefert den OUTPUT-Record
// des Key-Value-Stores, den dieser Actor nicht schreibt. Über den Run-Status
// bekommen wir zusaetzlich die real abgerechneten Kosten.
async function runActor(token, urls) {
  const started = await apify(`${API}/acts/${ACTOR_ID}/runs?token=${token}`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ videos: urls }),
  });
  const runId = started.data.id;
  console.log(`  Run-ID:   ${runId}`);

  const deadline = Date.now() + MAX_WAIT_MS;
  let run = started.data;
  while (['READY', 'RUNNING'].includes(run.status)) {
    if (Date.now() > deadline) throw new Error(`Timeout — Run ${runId} noch ${run.status}`);
    await sleep(POLL_MS);
    run = (await apify(`${API}/actor-runs/${runId}?token=${token}`)).data;
  }
  return run;
}

async function main() {
  loadEnv();
  const token = process.env.APIFY_TOKEN;
  if (!token) {
    console.error('✖ APIFY_TOKEN fehlt. In .env.local eintragen:  APIFY_TOKEN=apify_api_...');
    process.exitCode = 1;
    return;
  }

  const urls = process.argv.slice(2).filter((a) => a.startsWith('http'));
  if (!urls.length) {
    console.error('Usage: node scripts/tiktok-transcript.mjs <tiktok-url> [...]');
    process.exitCode = 1;
    return;
  }

  console.log(`→ Actor-Run für ${urls.length} URL(s) …`);
  const run = await runActor(token, urls);
  const items = await apify(
    `${API}/datasets/${run.defaultDatasetId}/items?token=${token}&clean=false&format=json`,
  );

  fs.mkdirSync(outDir, { recursive: true });
  const slug = slugFromUrl(urls[0]);
  const stamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
  const target = path.join(outDir, `${stamp}-${slug}.json`);
  fs.writeFileSync(
    target,
    JSON.stringify({ input: { videos: urls }, run, items }, null, 2),
    'utf8',
  );

  console.log(`  Status:   ${run.status}`);
  console.log(`  Dauer:    ${run.stats?.runTimeSecs ?? '?'}s`);
  console.log(`  Kosten:   $${run.usageTotalUsd ?? '?'}`);
  console.log(`  Items:    ${Array.isArray(items) ? items.length : '?'}`);
  console.log(`✓ Vollständige Antwort: ${path.relative(rootDir, target)}`);
}

main().catch((err) => {
  console.error(`✖ ${err.message}`);
  process.exitCode = 1;
});
