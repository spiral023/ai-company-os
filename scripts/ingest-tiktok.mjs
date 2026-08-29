// TikTok-Video als Quelle erfassen: Transkript über den Apify-Actor
// scrape-creators/best-tiktok-transcripts-scraper, Metadaten über TikTok
// oEmbed, Ablage nach 00_Inbox/Quellen/ wie bei `npm run ingest:x`.
//
// Nutzung:
//   npm run ingest:tiktok -- <video-url-oder-id> [--force] [--refetch]
//                            [--no-media] [--gap <sekunden>]
//
// Benötigt APIFY_TOKEN in .env.local (Vorlage: .env.example).

import fs from 'fs';
import path from 'path';
import {
  parseArgs,
  parseTiktokUrl,
  dateFromVideoId,
  handleFromAuthorUrl,
  detectLanguage,
  parseVtt,
  splitCaption,
  formatTiktokNote,
} from './lib/tiktok-ingest.mjs';
import { runTranscriptActor, fetchOembed, resolveShortUrl } from './lib/tiktok-client.mjs';
import { buildSlug, downloadMedia, writeInboxNote, mediaTargetDir, INBOX_REL } from './lib/inbox-store.mjs';

const rootDir = process.cwd();
const ingestDir = path.join(rootDir, 'scripts/.ingest');

function usage() {
  console.log(
    'Usage: npm run ingest:tiktok -- <video-url-oder-id> [--force] [--refetch] [--no-media] [--gap <sek>]',
  );
  console.log(`  Ablage: ${INBOX_REL}/<slug>.md · Cover: ${INBOX_REL}/medien/<slug>/`);
  console.log('  --force    Notiz neu schreiben (aus dem Cache, kein Actor-Run).');
  console.log('  --refetch  Transkript neu holen — kostet $0.001. Impliziert --force.');
  console.log('  --gap      Sprechpause in Sekunden, ab der ein neuer Absatz beginnt (Default 0.8).');
}

function loadEnv() {
  try {
    process.loadEnvFile(path.join(rootDir, '.env.local'));
  } catch {
    // .env.local optional — Variable kann extern gesetzt sein
  }
}

async function resolveInput(input) {
  try {
    return parseTiktokUrl(input);
  } catch (err) {
    if (!/Kurzlink/.test(err.message)) throw err;
    const resolved = await resolveShortUrl(input);
    return parseTiktokUrl(resolved);
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.input) {
    usage();
    process.exitCode = 1;
    return;
  }

  let video = await resolveInput(args.input);

  fs.mkdirSync(ingestDir, { recursive: true });
  const jsonPath = path.join(ingestDir, `tiktok-${video.id}.json`);

  let payload;
  if (fs.existsSync(jsonPath) && !args.refetch) {
    console.log(
      `● Cache-Treffer: ${path.relative(rootDir, jsonPath)} (kein Actor-Run). --refetch lädt neu.`,
    );
    payload = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
    // Wird nur die Video-ID übergeben, fehlt der Handle im Argument. Der
    // Cache kennt ihn aus dem ersten Lauf — sonst bekäme dieselbe Quelle beim
    // zweiten Lauf einen anderen Slug und läge doppelt in der Inbox.
    if (payload.video?.username) video = { ...video, ...payload.video };
  } else {
    loadEnv();
    const token = process.env.APIFY_TOKEN;
    if (!token) {
      console.error(
        '✖ APIFY_TOKEN fehlt. Lege .env.local an mit:\n  APIFY_TOKEN=apify_api_...\n(Vorlage: .env.example)',
      );
      process.exitCode = 1;
      return;
    }

    const requestUrl = video.url ?? `https://www.tiktok.com/@i/video/${video.id}`;
    console.log(`→ Apify-Actor für ${requestUrl} …`);
    const { run, items } = await runTranscriptActor(token, [requestUrl], {
      onRunId: (id) => console.log(`  Run-ID: ${id}`),
    });
    const item = items.find((x) => String(x.id) === video.id) ?? items[0] ?? {};

    let oembed = null;
    try {
      oembed = await fetchOembed(requestUrl);
    } catch (err) {
      console.warn(`⚠ oEmbed nicht abrufbar (${err.message}) — Notiz ohne Caption und Cover.`);
    }

    // Wurde nur die ID übergeben, liefert oEmbed den Handle nach.
    if (!video.username) {
      const handle = handleFromAuthorUrl(oembed?.author_url);
      if (handle) video = { ...video, username: handle, url: `https://www.tiktok.com/@${handle}/video/${video.id}` };
    }

    payload = {
      fetchedAt: new Date().toISOString(),
      video: { ...video, url: video.url ?? requestUrl },
      item,
      oembed,
      run: {
        id: run.id,
        status: run.status,
        usageTotalUsd: run.usageTotalUsd,
        runTimeSecs: run.stats?.runTimeSecs,
      },
    };
    fs.writeFileSync(jsonPath, JSON.stringify(payload, null, 2), 'utf8');
    console.log(`  Kosten: $${run.usageTotalUsd ?? 0} · ${run.stats?.runTimeSecs ?? '?'}s`);
  }

  const transcript = payload.item?.transcript ?? '';
  const videoUrl = video.url ?? payload.video?.url ?? `https://www.tiktok.com/@i/video/${video.id}`;
  const publishedAt = dateFromVideoId(video.id);
  // Nur der Handle taugt für den Slug — der Anzeigename aus oEmbed ist ein
  // anderer Wert ("Florian Schnemann" statt "floknowsai") und würde dieselbe
  // Quelle unter zwei Dateinamen ablegen.
  const slug = buildSlug({
    createdAt: publishedAt ?? payload.fetchedAt,
    username: video.username ?? handleFromAuthorUrl(payload.oembed?.author_url),
    id: video.id,
  });
  const notePath = path.join(rootDir, INBOX_REL, `${slug}.md`);

  // Eine bestehende Notiz kann manuell ergänzt oder auf status:verarbeitet
  // gesetzt sein — die darf ein erneuter Lauf nicht stillschweigend verwerfen.
  if (fs.existsSync(notePath) && !args.force) {
    console.log(`● Notiz existiert bereits: ${path.relative(rootDir, notePath)}`);
    console.log('  Unverändert gelassen. --force überschreibt sie.');
    return;
  }

  let downloads = [];
  const cover = payload.oembed?.thumbnail_url;
  if (args.media && cover) {
    downloads = await downloadMedia(
      [{ url: cover, type: 'photo', cover: true }],
      mediaTargetDir(rootDir, slug),
    );
    for (const d of downloads.filter((x) => !x.ok)) {
      console.warn(`⚠ Cover-Download fehlgeschlagen (${d.file}): ${d.error}`);
    }
  }

  const note = formatTiktokNote({
    video: { ...video, url: videoUrl },
    oembed: payload.oembed,
    transcript,
    slug,
    downloads,
    fetchedAt: payload.fetchedAt,
    gap: args.gap,
  });
  writeInboxNote(rootDir, slug, note);

  if (!transcript) {
    console.warn('⚠ Kein Transkript verfügbar — TikTok hat für dieses Video keine Untertitel.');
  } else {
    const transcriptLang = detectLanguage(parseVtt(transcript).map((c) => c.text).join(' '));
    const captionLang = detectLanguage(splitCaption(payload.oembed?.title).text);
    if (transcriptLang && captionLang && transcriptLang !== captionLang) {
      console.warn(
        `⚠ Transkript ist ${transcriptLang}, Caption ist ${captionLang} — TikTok hat eine übersetzte Untertitelspur geliefert. --refetch versuchen (kostet $0.001).`,
      );
    }
  }
  const okCount = downloads.filter((d) => d.ok).length;
  const mediaNote = downloads.length ? ` · Cover: ${okCount}/${downloads.length} lokal` : '';
  console.log(
    `✔ Quelle: ${path.relative(rootDir, notePath)} · ${transcript.length} Zeichen Transkript${mediaNote}`,
  );
}

main().catch((err) => {
  console.error(`✖ ${err.message}`);
  process.exitCode = 1;
});
