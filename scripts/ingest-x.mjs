import fs from 'fs';
import path from 'path';
import {
  parseArgs,
  parseTweetId,
  extractMedia,
  extractArticleMedia,
  extractTweetText,
  extractArticleText,
  isThreadStart,
  orderThreadChronologically,
  threadIdentity,
} from './lib/x-ingest.mjs';
import {
  createClient,
  fetchTweet,
  resolveThreadForward,
  resolveThreadBackward,
} from './lib/x-client.mjs';
import {
  buildSlug,
  downloadMedia,
  formatInboxNote,
  writeInboxNote,
  mediaTargetDir,
  sourceInboxRel,
} from './lib/inbox-store.mjs';

const rootDir = process.cwd();
const ingestDir = path.join(rootDir, 'scripts/.ingest');

function usage() {
  console.log(
    'Usage: npm run ingest:x -- <tweet-url-oder-id> [--thread] [--force] [--refetch] [--max-thread <n>] [--no-media]',
  );
  console.log(`  Ablage: ${sourceInboxRel('x')}/<slug>.md · Medien: ${sourceInboxRel('x')}/medien/<slug>/`);
  console.log('  --force    Notiz neu schreiben (aus dem Cache, kein API-Call).');
  console.log('  --refetch  API-Antwort neu holen — kostet einen Request. Impliziert --force.');
}

function loadEnv() {
  try {
    process.loadEnvFile(path.join(rootDir, '.env.local'));
  } catch {
    // .env.local optional — Variable kann extern gesetzt sein
  }
}

function findAuthor(includes, authorId) {
  const users = includes?.users ?? [];
  return users.find((u) => u.id === authorId) ?? users[0] ?? null;
}

function formatApiError(err) {
  const code = err?.code ?? err?.data?.status;
  if (code === 401) return '✖ 401 Unauthorized — Bearer Token ungültig oder abgelaufen.';
  if (code === 402) {
    const detail = err?.data?.detail ? ` (${err.data.detail})` : '';
    return `✖ 402 Payment Required — Guthaben der X-API aufgebraucht${detail}. Im X Developer Portal Credits aufladen und erneut versuchen.`;
  }
  if (code === 403) return '✖ 403 Forbidden — App fehlt die Berechtigung für diesen Endpoint/Tweet.';
  if (code === 404) return '✖ 404 — Tweet gelöscht, privat oder ID falsch.';
  if (code === 429) {
    const reset = err?.rateLimit?.reset
      ? ` Reset: ${new Date(err.rateLimit.reset * 1000).toLocaleTimeString()}`
      : '';
    return `✖ 429 Rate-Limit erreicht.${reset} Kein Auto-Retry (Pay-per-use).`;
  }
  if (typeof code === 'number' && code >= 500) {
    return `✖ ${code} — temporärer Serverfehler bei X. Kein Code-Problem; in ein paar Minuten erneut versuchen.`;
  }
  return `✖ API-Fehler: ${err?.message ?? String(err)}`;
}

function noteIds(notePath) {
  try {
    const text = fs.readFileSync(notePath, 'utf8');
    return [
      text.match(/^tweet_id:\s*["']?(\d+)/m)?.[1],
      text.match(/^conversation_id:\s*["']?(\d+)/m)?.[1],
    ].filter(Boolean);
  } catch {
    return [];
  }
}

// Sucht die Notiz zu diesem Strang. Notizen aus der Zeit vor dem
// conversation_id-Feld tragen nur tweet_id — die IDs der Kette decken sie ab.
function findNoteByIds(ids) {
  const dir = path.join(rootDir, sourceInboxRel('x'));
  if (!fs.existsSync(dir)) return null;
  return (
    fs
      .readdirSync(dir, { withFileTypes: true })
      .filter((entry) => entry.isFile() && entry.name.endsWith('.md'))
      .map((entry) => path.join(dir, entry.name))
      .find((file) => noteIds(file).some((id) => ids.has(id))) ?? null
  );
}

function threadPostsInNote(notePath) {
  try {
    return Number(fs.readFileSync(notePath, 'utf8').match(/^thread_posts:\s*(\d+)/m)?.[1] ?? 1);
  } catch {
    return 1;
  }
}

async function resolveThread(client, tweet, author, maxThread, includes) {
  if (isThreadStart(tweet)) {
    if (!author?.username) {
      console.warn('⚠ Thread-Start ohne auflösbaren Autor-Username — Thread wird nicht aufgelöst.');
      return { thread: null, method: null };
    }
    const fwd = await resolveThreadForward(client, tweet, author.username);
    if (fwd) {
      return {
        thread: orderThreadChronologically(fwd.tweets),
        method: fwd.method,
        includes: fwd.includes,
      };
    }
    // Ohne Antworten kann es keinen Thread geben — dann ist die leere Suche
    // das erwartete Ergebnis und keine Warnung wert. Sonst bleibt offen, ob
    // der Strang fehlt oder der Post schlicht allein steht.
    if ((tweet.public_metrics?.reply_count ?? 0) > 0) {
      console.warn(
        '⚠ Thread nicht über Search auflösbar (>7 Tage & kein Full-Archive-Zugang). Hat der Post Folge-Posts, die URL des LETZTEN übergeben — der Rückwärts-Walk kommt ohne Search aus und trifft dieselbe Notiz.',
      );
    }
    return { thread: null, method: null };
  }
  const walk = await resolveThreadBackward(client, tweet, maxThread, includes);
  const chain = walk.tweets;
  const oldest = chain[chain.length - 1];
  const hasMoreParents = (oldest?.referenced_tweets ?? []).some((r) => r.type === 'replied_to');
  if (chain.length >= maxThread && hasMoreParents) {
    console.warn(`⚠ Rückwärts-Walk bei --max-thread=${maxThread} gekappt (weitere Vorgänger vorhanden).`);
  }
  return {
    thread: orderThreadChronologically(chain),
    method: 'backward-walk',
    includes: walk.includes,
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.input) {
    usage();
    process.exit(1);
  }

  let id;
  try {
    id = parseTweetId(args.input);
  } catch (err) {
    console.error(`✖ ${err.message}`);
    process.exit(1);
  }

  fs.mkdirSync(ingestDir, { recursive: true });
  const jsonPath = path.join(ingestDir, `${id}.json`);

  let payload;
  if (fs.existsSync(jsonPath) && !args.refetch) {
    console.log(
      `● Cache-Treffer: ${path.relative(rootDir, jsonPath)} (kein API-Call). --refetch lädt neu.`,
    );
    payload = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  } else {
    loadEnv();
    const token = process.env.X_BEARER_TOKEN;
    if (!token) {
      console.error(
        '✖ X_BEARER_TOKEN fehlt. Lege .env.local an mit:\n  X_BEARER_TOKEN=dein_bearer_token\n(Vorlage: .env.example)',
      );
      process.exit(1);
    }

    const client = createClient(token);
    let res;
    try {
      res = await fetchTweet(client, id);
    } catch (err) {
      console.error(formatApiError(err));
      process.exit(1);
    }
    if (!res?.data) {
      console.error('✖ Kein Tweet in der Antwort (gelöscht, privat oder ID falsch?).');
      process.exit(1);
    }

    const tweet = res.data;
    const author = findAuthor(res.includes, tweet.author_id);
    let thread = null;
    let threadMethod = null;
    let threadIncludes = null;
    if (args.thread) {
      ({
        thread,
        method: threadMethod,
        includes: threadIncludes,
      } = await resolveThread(client, tweet, author, args.maxThread, res.includes));
    }

    payload = {
      fetchedAt: new Date().toISOString(),
      id,
      tweet,
      // Die includes der Kette decken auch die Bilder des Ankers ab, an dem
      // die Notiz später hängt — der muss nicht der abgerufene Post sein.
      includes: threadIncludes ?? res.includes ?? {},
      thread,
      threadMethod,
    };
    fs.writeFileSync(jsonPath, JSON.stringify(payload, null, 2), 'utf8');
  }

  const abgerufen = payload.tweet;
  const author = findAuthor(payload.includes, abgerufen.author_id);
  // Der Strang ankert an seinem ältesten eigenen Post, nicht an der übergebenen
  // URL. Ein Nachlauf über den letzten Post landet dadurch auf derselben Notiz.
  // Der Anker trägt auch Kopf, url und Metriken: Zitiert wird der Erstpost,
  // nicht die Antwort, über die man zufällig in den Strang eingestiegen ist.
  const { anker, ids } = threadIdentity(abgerufen, payload.thread);
  const tweet = anker;
  // Bei einem Strang tragen die includes die Bilder aller Posts. Unter dem Kopf
  // dürfen nur die des Ankers stehen — die übrigen gehören zu ihren Posts.
  const ankerKeys = new Set(tweet.attachments?.media_keys ?? []);
  const media = extractMedia(
    payload.thread?.length
      ? (payload.includes?.media ?? []).filter((m) => ankerKeys.has(m?.media_key))
      : payload.includes?.media,
  );
  const articleMedia = extractArticleMedia(tweet, payload.includes?.media);
  const slug = buildSlug({ createdAt: anker.created_at, username: author?.username, id: anker.id });
  const notePath = path.join(rootDir, sourceInboxRel('x'), `${slug}.md`);

  // Eine bestehende Notiz kann manuell ergänzt oder auf status:verarbeitet
  // gesetzt sein — die darf ein erneuter Lauf nicht stillschweigend verwerfen.
  const existingNote = findNoteByIds(ids);
  if (existingNote && !args.force) {
    console.log(`● Notiz existiert bereits: ${path.relative(rootDir, existingNote)}`);
    const jetzt = payload.thread?.length ?? 1;
    const bisher = threadPostsInNote(existingNote);
    if (jetzt > bisher) {
      console.log(`  Dieser Lauf hätte ${jetzt} statt ${bisher} Posts — --force schreibt sie neu.`);
    } else {
      console.log('  Unverändert gelassen. --force überschreibt sie.');
    }
    return;
  }

  // --force schreibt den Strang neu. Lag die Notiz noch unter der ID eines
  // späteren Posts, zieht der Dateiname samt Medienordner auf den Anker nach,
  // statt eine zweite Notiz derselben Quelle anzulegen.
  if (existingNote && path.resolve(existingNote) !== path.resolve(notePath)) {
    const altSlug = path.basename(existingNote, '.md');
    const altMedien = mediaTargetDir(rootDir, 'x', altSlug);
    const neuMedien = mediaTargetDir(rootDir, 'x', slug);
    if (fs.existsSync(neuMedien)) {
      throw new Error(`Ziel-Medienordner existiert bereits: ${path.relative(rootDir, neuMedien)}`);
    }
    if (fs.existsSync(altMedien)) fs.renameSync(altMedien, neuMedien);
    fs.renameSync(existingNote, notePath);
    console.log(`  Umbenannt: ${altSlug}.md → ${slug}.md`);
  }

  // Medien für Deduplizierung in derselben Reihenfolge wie in der Notiz.
  const mediaToLoad = [];
  const seenMedia = new Set();
  for (const item of [...articleMedia, ...media]) {
    const key = item.url || item.key;
    if (!key || seenMedia.has(key)) continue;
    seenMedia.add(key);
    mediaToLoad.push(item);
  }

  let downloads = [];
  if (args.media && mediaToLoad.length) {
    downloads = await downloadMedia(mediaToLoad, mediaTargetDir(rootDir, 'x', slug));
    for (const d of downloads.filter((x) => !x.ok)) {
      console.warn(`⚠ Medien-Download fehlgeschlagen (${d.file}): ${d.error}`);
    }
  }

  const note = formatInboxNote({
    tweet,
    author,
    slug,
    media,
    articleMedia,
    thread: payload.thread,
    threadMethod: payload.threadMethod,
    threadUsers: payload.includes?.users,
    downloads,
    fetchedAt: payload.fetchedAt,
  });
  writeInboxNote(rootDir, 'x', slug, note);

  const articleText = extractArticleText(tweet);
  const contentLen = articleText ? articleText.length : extractTweetText(tweet).length;
  const contentNote = articleText ? ' Zeichen (Artikel)' : ' Zeichen';
  const threadNote = payload.thread
    ? ` · Thread: ${payload.thread.length} Posts (${payload.threadMethod})`
    : '';
  const okCount = downloads.filter((d) => d.ok).length;
  const skipped = downloads.filter((d) => d.skipped).length;
  const mediaNote = mediaToLoad.length
    ? ` · Medien: ${okCount}/${mediaToLoad.length} lokal${skipped ? ` (${skipped} bereits vorhanden)` : ''}`
    : '';

  console.log(`✔ Quelle: ${path.relative(rootDir, notePath)}`);
  console.log(
    `  Autor: ${author?.name ?? '?'} (@${author?.username ?? '?'}) · ${contentLen}${contentNote}${threadNote}${mediaNote}`,
  );
  console.log('  status: neu — wird beim nächsten Sammel-Lauf verarbeitet.');
}

main().catch((err) => {
  console.error(`✖ Unerwarteter Fehler: ${err?.message ?? err}`);
  process.exit(1);
});
