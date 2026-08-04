export function parseArgs(argv) {
  // --force schreibt die Notiz neu (aus dem Cache, kostenlos).
  // --refetch holt zusätzlich die API-Antwort neu und kostet einen Request.
  const args = {
    input: undefined,
    thread: false,
    force: false,
    refetch: false,
    maxThread: 50,
    media: true,
  };
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    if (a === '--thread') args.thread = true;
    else if (a === '--force') args.force = true;
    else if (a === '--refetch') {
      args.refetch = true;
      args.force = true;
    } else if (a === '--no-media') args.media = false;
    else if (a === '--max-thread') {
      const n = Number.parseInt(argv[i + 1], 10);
      args.maxThread = Number.isFinite(n) && n > 0 ? n : 50;
      i += 1;
    } else if (!a.startsWith('--') && args.input === undefined) {
      args.input = a;
    }
  }
  return args;
}

export function parseTweetId(input) {
  const trimmed = (input ?? '').trim();
  if (/^\d+$/.test(trimmed)) return trimmed;
  const match = trimmed.match(/(?:twitter\.com|x\.com)\/[^/]+\/status\/(\d+)/i);
  if (match) return match[1];
  throw new Error(
    `Konnte keine Tweet-ID aus "${input}" lesen. Erwartet: Tweet-URL oder numerische ID.`,
  );
}

export function extractTweetText(tweet) {
  return tweet?.note_tweet?.text ?? tweet?.text ?? '';
}

export function extractArticleText(tweet) {
  return tweet?.article?.plain_text ?? '';
}

export function extractLinks(tweet) {
  const entities = tweet?.note_tweet?.entities ?? tweet?.entities ?? {};
  const urls = Array.isArray(entities.urls) ? entities.urls : [];
  const seen = new Set();
  const links = [];
  for (const u of urls) {
    const expanded = u.expanded_url ?? u.url;
    if (!expanded || seen.has(expanded)) continue;
    seen.add(expanded);
    links.push({ url: expanded, display: u.display_url ?? expanded });
  }
  return links;
}

export function extractMedia(mediaList) {
  if (!Array.isArray(mediaList)) return [];
  return mediaList.map((m) => ({
    type: m.type ?? 'unknown',
    alt: m.alt_text ?? '',
    url: m.url ?? m.preview_image_url ?? '',
  }));
}

// Native X-Artikel referenzieren ihre Bilder über cover_media + media_entities
// als bloße media_keys. Diese Keys gegen includes.media auflösen (Expansions
// article.cover_media / article.media_entities liefern die Objekte dort).
export function extractArticleMedia(tweet, mediaIncludes) {
  const article = tweet?.article;
  if (!article) return [];
  const byKey = new Map(
    (Array.isArray(mediaIncludes) ? mediaIncludes : []).map((m) => [m.media_key, m]),
  );
  const refs = [];
  if (typeof article.cover_media === 'string') refs.push({ key: article.cover_media, cover: true });
  const entities = Array.isArray(article.media_entities) ? article.media_entities : [];
  for (const e of entities) {
    const key = typeof e === 'string' ? e : e?.media_key;
    if (key) refs.push({ key, cover: false });
  }
  const seen = new Set();
  const out = [];
  for (const { key, cover } of refs) {
    if (seen.has(key)) continue;
    seen.add(key);
    const m = byKey.get(key);
    if (m) {
      out.push({
        type: m.type ?? 'unknown',
        alt: m.alt_text ?? '',
        url: m.url ?? m.preview_image_url ?? '',
        cover,
      });
    } else {
      out.push({ type: 'unknown', alt: '', url: '', cover, key });
    }
  }
  return out;
}

export function isThreadStart(tweet) {
  return Boolean(tweet?.id && tweet.id === tweet.conversation_id);
}

export function orderThreadChronologically(tweets) {
  return [...tweets].sort((a, b) => {
    const ta = a?.created_at ? Date.parse(a.created_at) : 0;
    const tb = b?.created_at ? Date.parse(b.created_at) : 0;
    return ta - tb;
  });
}

// Die Ausgabe-Formatierung lebt in lib/inbox-store.mjs (formatInboxNote) —
// eine Quelle wird direkt als Inbox-Notiz geschrieben, nicht als Zwischen-Dump.
