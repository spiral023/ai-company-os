import fs from 'fs';
import path from 'path';
import { extractTweetText, extractArticleText, extractLinks } from './x-ingest.mjs';

// Ablage nach Quelltyp, Medien jeweils neben den Notizen des Typs:
//   00_Inbox/Quellen/X/<slug>.md
//   00_Inbox/Quellen/X/medien/<slug>/01-cover.jpg
export const INBOX_REL = '00_Inbox/Quellen';
export const MEDIA_DIR = 'medien';
export const SOURCE_FOLDERS = Object.freeze({
  x: 'X',
  tiktok: 'TikTok',
});

export function sourceInboxRel(sourceType) {
  return `${INBOX_REL}/${SOURCE_FOLDERS[sourceType] ?? 'Sonstige'}`;
}

export function isoDate(value) {
  const d = value ? new Date(value) : new Date();
  if (Number.isNaN(d.getTime())) return new Date().toISOString().slice(0, 10);
  return d.toISOString().slice(0, 10);
}

export function slugifyHandle(username) {
  const cleaned = (username ?? 'unbekannt')
    .toLowerCase()
    .replace(/[^a-z0-9_-]/g, '')
    .replace(/^_+|_+$/g, '');
  return cleaned || 'unbekannt';
}

// Slug = Veröffentlichungsdatum + Handle + Tweet-ID. Die ID hält den Slug
// eindeutig, auch wenn ein Autor am selben Tag mehrfach postet.
export function buildSlug({ createdAt, username, id }) {
  return `${isoDate(createdAt)}-${slugifyHandle(username)}-${id}`;
}

function extensionFor(url, type) {
  const clean = (url ?? '').split('?')[0];
  const ext = path.extname(clean).toLowerCase();
  if (/^\.(jpe?g|png|gif|webp|mp4)$/.test(ext)) return ext;
  return type === 'video' || type === 'animated_gif' ? '.mp4' : '.jpg';
}

export function mediaFileName(index, item) {
  const label = item.cover ? 'cover' : (item.type ?? 'media').replace(/[^a-z0-9]/gi, '') || 'media';
  return `${String(index + 1).padStart(2, '0')}-${label}${extensionFor(item.url, item.type)}`;
}

// pbs.twimg.com liefert per Default eine verkleinerte Variante. Charts und
// Preistabellen sind darin oft unlesbar, deshalb Originalgröße anfordern.
export function originalSizeUrl(url) {
  if (!url || !/pbs\.twimg\.com/.test(url)) return url;
  if (/[?&]name=/.test(url)) return url;
  return `${url}${url.includes('?') ? '&' : '?'}name=orig`;
}

// Lädt Medien nach targetDir. Bereits vorhandene Dateien werden nicht erneut
// geladen. Ein fehlgeschlagener Download bricht den Ingest nicht ab — die
// Remote-URL bleibt in der Notiz erhalten, damit nichts still verloren geht.
export async function downloadMedia(items, targetDir, options = {}) {
  const fetchImpl = options.fetch ?? globalThis.fetch;
  const results = [];
  if (!Array.isArray(items) || !items.length) return results;
  fs.mkdirSync(targetDir, { recursive: true });

  for (let i = 0; i < items.length; i += 1) {
    const item = items[i];
    const file = mediaFileName(i, item);
    const dest = path.join(targetDir, file);
    const entry = { ...item, file, ok: false, skipped: false };

    if (!item.url) {
      entry.error = `keine URL (media_key: ${item.key ?? '?'})`;
      results.push(entry);
      continue;
    }
    if (fs.existsSync(dest) && fs.statSync(dest).size > 0) {
      results.push({ ...entry, ok: true, skipped: true });
      continue;
    }

    try {
      const res = await fetchImpl(originalSizeUrl(item.url));
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const buf = Buffer.from(await res.arrayBuffer());
      if (!buf.length) throw new Error('leere Antwort');
      fs.writeFileSync(dest, buf);
      results.push({ ...entry, ok: true, bytes: buf.length });
    } catch (err) {
      results.push({ ...entry, error: err?.message ?? String(err) });
    }
  }
  return results;
}

function yamlString(value) {
  const s = String(value ?? '');
  return `"${s.replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`;
}

// Notiz für die Inbox: Frontmatter mit Verarbeitungsstatus, dann der
// vollständige Inhalt. `status: neu` ist der Marker, den der Sammel-Lauf sucht.
export function formatInboxNote({
  tweet,
  author,
  slug,
  media,
  articleMedia,
  thread,
  threadMethod,
  downloads,
  fetchedAt,
}) {
  const username = author?.username ?? 'i';
  const title = tweet?.article?.title ?? '';
  const articleText = extractArticleText(tweet);
  const tweetText = extractTweetText(tweet);
  const localByUrl = new Map(
    (downloads ?? []).filter((d) => d.ok && d.url).map((d) => [d.url, `${MEDIA_DIR}/${slug}/${d.file}`]),
  );

  const fm = [
    '---',
    `url: https://x.com/${username}/status/${tweet.id}`,
    `autor: "@${username}"`,
    `autor_name: ${yamlString(author?.name ?? 'Unbekannt')}`,
    `datum: ${isoDate(tweet.created_at)}`,
    `erfasst: ${isoDate(fetchedAt)}`,
    `typ: ${tweet.article ? 'artikel' : 'tweet'}`,
    'quelle: x',
    'status: neu',
  ];
  if (title) fm.push(`titel: ${yamlString(title)}`);
  fm.push(`tweet_id: "${tweet.id}"`);
  const m = tweet.public_metrics;
  if (m) {
    fm.push(
      `metriken: "${m.like_count ?? 0} Likes · ${m.retweet_count ?? 0} Retweets · ${m.reply_count ?? 0} Replies · ${m.impression_count ?? '?'} Views"`,
    );
  }
  const okCount = (downloads ?? []).filter((d) => d.ok).length;
  const total = (downloads ?? []).length;
  if (total) fm.push(`medien: "${okCount}/${total} lokal"`);
  if (thread?.length) fm.push(`thread_posts: ${thread.length}`, `thread_methode: ${threadMethod ?? '?'}`);
  fm.push('---', '');

  const lines = [...fm];
  lines.push(`# ${title || `${author?.name ?? 'Unbekannt'} (@${username})`}`, '');
  lines.push(
    `> Automatisch per \`npm run ingest:x\` erfasst. Quelle: [x.com/${username}/status/${tweet.id}](https://x.com/${username}/status/${tweet.id})`,
    '',
  );

  if (tweet.article) {
    if (articleText) {
      lines.push('## Artikel-Volltext', '', articleText, '');
    } else {
      lines.push(
        `> ⚠️ Nativer X-Artikel „${title}" — Volltext nicht über die API verfügbar; bei Bedarf Sekundärquelle prüfen.`,
        '',
      );
    }
  }

  const allMedia = [...(articleMedia ?? []), ...(media ?? [])];
  const seen = new Set();
  const rendered = [];
  for (const item of allMedia) {
    const key = item.url || item.key;
    if (!key || seen.has(key)) continue;
    seen.add(key);
    rendered.push(item);
  }
  if (rendered.length) {
    lines.push('## Bilder', '');
    lines.push(
      '<!-- Reihenfolge wie von der API geliefert (Cover zuerst). Die Position im Artikeltext gibt die API nicht mit. -->',
      '',
    );
    for (const item of rendered) {
      const local = localByUrl.get(item.url);
      const label = item.cover ? 'Cover' : (item.type ?? 'media');
      const alt = item.alt ? item.alt : label;
      if (local) {
        lines.push(`**${label}**${item.alt ? ` — ${item.alt}` : ''}`, '', `![${alt}](${local})`, '');
      } else if (item.url) {
        lines.push(
          `**${label}**${item.alt ? ` — ${item.alt}` : ''} · ⚠️ nicht lokal gespeichert`,
          '',
          `![${alt}](${item.url})`,
          '',
        );
      } else {
        lines.push(`**${label}** — nicht aufgelöst (media_key: ${item.key ?? '?'})`, '');
      }
    }
  }

  if (tweetText.trim()) lines.push('## Post-Text', '', tweetText, '');

  const links = extractLinks(tweet);
  if (links.length) {
    lines.push('## Links', '');
    for (const l of links) lines.push(`- [${l.display}](${l.url})`);
    lines.push('');
  }

  if (thread?.length) {
    lines.push('## Thread', '');
    thread.forEach((t, i) => {
      const text = extractTweetText(t).trim();
      lines.push(`### ${i + 1}/${thread.length}`, '', text || '(kein Text)', '');
    });
  }

  return lines.join('\n');
}

export function writeInboxNote(rootDir, sourceType, slug, content) {
  const dir = path.join(rootDir, sourceInboxRel(sourceType));
  fs.mkdirSync(dir, { recursive: true });
  const file = path.join(dir, `${slug}.md`);
  fs.writeFileSync(file, content, 'utf8');
  return file;
}

export function mediaTargetDir(rootDir, sourceType, slug) {
  return path.join(rootDir, sourceInboxRel(sourceType), MEDIA_DIR, slug);
}
