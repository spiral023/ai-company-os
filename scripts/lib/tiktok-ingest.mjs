import { isoDate, MEDIA_DIR } from './inbox-store.mjs';

// Reine Funktionen für den TikTok-Ingest: URL/ID, WEBVTT-Transkript, Notiz.
// Netzwerkzugriffe liegen in tiktok-client.mjs.

export function parseArgs(argv) {
  const args = {
    input: null,
    force: false,
    refetch: false,
    media: true,
    gap: 0.4,
  };
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    if (a === '--force') args.force = true;
    else if (a === '--refetch') {
      args.refetch = true;
      args.force = true;
    } else if (a === '--no-media') args.media = false;
    else if (a === '--gap') {
      const v = Number(argv[i + 1]);
      if (Number.isFinite(v) && v >= 0) args.gap = v;
      i += 1;
    } else if (!a.startsWith('--') && !args.input) args.input = a;
  }
  return args;
}

// Akzeptiert die volle Video-URL oder eine reine Video-ID. Kurzlinks
// (vm.tiktok.com) tragen keine ID und werden vorher aufgelöst.
export function parseTiktokUrl(input) {
  const raw = String(input ?? '').trim();
  if (/^\d{15,25}$/.test(raw)) return { id: raw, username: null, url: null };

  const m = raw.match(/tiktok\.com\/@([^/?#]+)\/(?:video|photo)\/(\d+)/i);
  if (m) {
    return {
      id: m[2],
      username: m[1],
      url: `https://www.tiktok.com/@${m[1]}/video/${m[2]}`,
    };
  }
  if (/vm\.tiktok\.com|\/t\//i.test(raw)) {
    throw new Error(`Kurzlink erkannt: ${raw} — konnte nicht aufgelöst werden.`);
  }
  throw new Error(
    `Keine TikTok-Video-URL erkennbar: ${raw}\n  Erwartet: https://www.tiktok.com/@handle/video/1234567890`,
  );
}

// TikTok-Video-IDs sind Snowflake-artig: die oberen 32 Bit sind der
// Unix-Timestamp der Veröffentlichung. Der Transkript-Actor liefert kein
// Datum mit, deshalb kommt das Veröffentlichungsdatum aus der ID selbst.
export function dateFromVideoId(id) {
  let n;
  try {
    n = BigInt(id);
  } catch {
    return null;
  }
  const seconds = Number(n >> 32n);
  if (!Number.isFinite(seconds) || seconds < 1300000000 || seconds > 4102444800) return null;
  return new Date(seconds * 1000).toISOString();
}

// oEmbed liefert den Handle nur in author_url ("…/@floknowsai"); author_name
// ist der frei gewählte Anzeigename und taugt nicht für Slug oder Frontmatter.
export function handleFromAuthorUrl(authorUrl) {
  const m = String(authorUrl ?? '').match(/tiktok\.com\/@([^/?#]+)/i);
  return m ? m[1] : null;
}

function vttTimeToSeconds(stamp) {
  const m = String(stamp).trim().match(/^(?:(\d+):)?(\d{1,2}):(\d{2})[.,](\d{1,3})$/);
  if (!m) return null;
  const [, h, min, s, ms] = m;
  return Number(h ?? 0) * 3600 + Number(min) * 60 + Number(s) + Number(ms.padEnd(3, '0')) / 1000;
}

// WEBVTT in Cues zerlegen. Der Actor liefert das Transkript ausschließlich in
// diesem Format; Cue-Nummern und Styling-Blöcke gibt es dort nicht.
export function parseVtt(vtt) {
  if (!vtt || typeof vtt !== 'string') return [];
  const cues = [];
  const blocks = vtt.replace(/\r\n/g, '\n').split(/\n{2,}/);
  for (const block of blocks) {
    const lines = block.split('\n').filter((l) => l.trim());
    if (!lines.length) continue;
    const idx = lines.findIndex((l) => l.includes('-->'));
    if (idx === -1) continue;
    const [from, to] = lines[idx].split('-->');
    const start = vttTimeToSeconds(from ?? '');
    const end = vttTimeToSeconds((to ?? '').trim().split(/\s/)[0] ?? '');
    const text = lines
      .slice(idx + 1)
      .join(' ')
      .replace(/<[^>]+>/g, '')
      .trim();
    if (start === null || !text) continue;
    cues.push({ start, end: end ?? start, text });
  }
  return cues;
}

export function formatTimestamp(seconds) {
  const total = Math.max(0, Math.round(seconds ?? 0));
  const m = Math.floor(total / 60);
  const s = total % 60;
  return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
}

// Die Spracherkennung liefert keine Satzzeichen. Einziger belastbarer
// Strukturhinweis sind Sprechpausen — ab `gapSeconds` beginnt ein neuer
// Absatz, damit der Fließtext lesbar bleibt. Der Default 0.4 stammt aus der
// gemessenen Pausenverteilung: TikTok-Cues liegen dicht beieinander, die
// größte Lücke in einem 2:30-Video lag bei 0,72s.
export function cuesToParagraphs(cues, gapSeconds = 0.4) {
  const paragraphs = [];
  let current = [];
  let prevEnd = null;
  for (const cue of cues) {
    if (prevEnd !== null && cue.start - prevEnd >= gapSeconds && current.length) {
      paragraphs.push(current.join(' '));
      current = [];
    }
    current.push(cue.text);
    prevEnd = cue.end;
  }
  if (current.length) paragraphs.push(current.join(' '));
  return paragraphs;
}

export function transcriptDuration(cues) {
  if (!cues.length) return null;
  return cues[cues.length - 1].end;
}

// TikTok hinterlegt zu manchen Videos eine automatisch ins Englische
// übersetzte Untertitelspur und liefert sie statt des Originals aus. Der
// Actor kennt keinen Sprachparameter, also wird die Sprache hier gemessen und
// gegen die Caption gehalten — sonst landet eine Rückübersetzung unbemerkt in
// der Inbox ("Anthropic hat die Claude Academy veröffentlicht" wird zu
// "1 Tropic has the cloud Academy published").
const STOPWORDS = {
  de: ['der', 'die', 'das', 'und', 'ist', 'nicht', 'für', 'mit', 'ein', 'eine', 'auch', 'dass', 'ich', 'du', 'sich', 'wie', 'was', 'dann', 'schon', 'noch'],
  en: ['the', 'and', 'is', 'not', 'for', 'with', 'a', 'an', 'also', 'that', 'i', 'you', 'how', 'what', 'then', 'this', 'of', 'to', 'in', 'it'],
};

export function detectLanguage(text) {
  const words = String(text ?? '').toLowerCase().match(/[a-zA-ZäöüÄÖÜß']+/g);
  if (!words || words.length < 15) return null;
  const score = (list) => words.filter((w) => list.includes(w)).length;
  const de = score(STOPWORDS.de);
  const en = score(STOPWORDS.en);
  if (de === en) return null;
  // Knappe Abstände sind bei kurzen Texten Rauschen, nicht Signal.
  if (Math.abs(de - en) < Math.max(3, words.length * 0.01)) return null;
  return de > en ? 'de' : 'en';
}

function yamlString(value) {
  const s = String(value ?? '');
  return `"${s.replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`;
}

// Caption und Hashtags trennen: TikTok liefert im oEmbed-Titel beides
// vermischt. Getrennt sind die Hashtags als Schlagwortliste brauchbar.
export function splitCaption(title) {
  const raw = String(title ?? '').trim();
  const tags = [...raw.matchAll(/#+([\p{L}\p{N}_]+)/gu)].map((m) => m[1]);
  const text = raw.replace(/#+[\p{L}\p{N}_]+/gu, ' ').replace(/\s+/g, ' ').trim();
  return { text, tags: [...new Set(tags)] };
}

// Titel für Frontmatter und Überschrift. Captions sind bei manchen Accounts
// ganze Fließtexte (gemessen: bis 1045 Zeichen) — ungekürzt sprengen sie die
// Notizliste. Ein abgeschlossener erster Satz ist der beste Titel; sonst wird
// an der Wortgrenze gekappt.
export function shortenTitle(input, maxLength = 80, sentenceLimit = 110) {
  const text = String(input ?? '').replace(/\s+/g, ' ').trim();
  if (!text) return '';
  if (text.length <= maxLength) return text;

  const sentenceEnd = text.search(/[.!?](\s|$)/);
  if (sentenceEnd > 20 && sentenceEnd + 1 <= sentenceLimit) {
    return text.slice(0, sentenceEnd + 1).trim();
  }

  const cut = text.slice(0, maxLength);
  const lastSpace = cut.lastIndexOf(' ');
  return `${(lastSpace > 20 ? cut.slice(0, lastSpace) : cut).trim()} …`;
}

// Viele Captions bestehen nur aus Hashtags. Dann ist der Einstieg des
// gesprochenen Texts der aussagekräftigere Titel — in der Notizliste steht
// sonst überall nur "TikTok von @handle".
export function titleFromTranscript(cues, maxLength = 80) {
  return shortenTitle(cues.map((c) => c.text).join(' '), maxLength);
}

export function formatTiktokNote({
  video,
  oembed,
  transcript,
  slug,
  downloads,
  fetchedAt,
  gap = 0.4,
}) {
  const username = video.username ?? 'unbekannt';
  const url = video.url ?? `https://www.tiktok.com/@${username}/video/${video.id}`;
  const publishedAt = dateFromVideoId(video.id);
  const caption = splitCaption(oembed?.title);
  const cues = parseVtt(transcript);
  const paragraphs = cuesToParagraphs(cues, gap);
  const duration = transcriptDuration(cues);
  const cover = (downloads ?? []).find((d) => d.ok && d.cover);

  const title =
    shortenTitle(caption.text) || titleFromTranscript(cues) || `TikTok von @${username}`;

  const fm = [
    '---',
    `url: ${url}`,
    `autor: "@${username}"`,
    `autor_name: ${yamlString(oembed?.author_name ?? username)}`,
    `datum: ${publishedAt ? isoDate(publishedAt) : isoDate(fetchedAt)}`,
    `erfasst: ${isoDate(fetchedAt)}`,
    'typ: video',
    'quelle: tiktok',
    'status: neu',
    `titel: ${yamlString(title)}`,
    `video_id: "${video.id}"`,
  ];
  if (!publishedAt) fm.push('datum_unsicher: true');
  if (caption.tags.length) fm.push(`hashtags: "${caption.tags.join(', ')}"`);
  const transcriptText = cues.map((c) => c.text).join(' ');
  const transcriptLang = detectLanguage(transcriptText);
  const captionLang = detectLanguage(caption.text);
  const langMismatch = Boolean(transcriptLang && captionLang && transcriptLang !== captionLang);

  if (cues.length) {
    fm.push(`transkript: "${cues.length} Cues · ${transcript.length} Zeichen"`);
    if (duration) fm.push(`laenge: "${formatTimestamp(duration)}"`);
    if (transcriptLang) fm.push(`sprache: ${transcriptLang}`);
    if (langMismatch) fm.push('sprache_abweichung: true');
  } else {
    fm.push('transkript: "keins verfügbar"');
  }
  const total = (downloads ?? []).length;
  if (total) fm.push(`medien: "${(downloads ?? []).filter((d) => d.ok).length}/${total} lokal"`);
  fm.push('---', '');

  const lines = [...fm];
  lines.push(`# ${title}`, '');
  lines.push(
    `> Automatisch per \`npm run ingest:tiktok\` erfasst. Quelle: [tiktok.com/@${username}/video/${video.id}](${url})`,
    '',
  );

  if (cover) {
    lines.push(`![Cover](${MEDIA_DIR}/${slug}/${cover.file})`, '');
  } else if (oembed?.thumbnail_url) {
    lines.push('> ⚠️ Cover nicht lokal gespeichert.', '', `![Cover](${oembed.thumbnail_url})`, '');
  }

  if (caption.text || caption.tags.length) {
    lines.push('## Caption', '');
    if (caption.text) lines.push(caption.text, '');
    if (caption.tags.length) lines.push(caption.tags.map((t) => `#${t}`).join(' '), '');
  }

  if (paragraphs.length) {
    lines.push('## Transkript', '');
    lines.push(
      '> ⚠️ Automatische Spracherkennung von TikTok. Eigennamen und Zahlwörter sind regelmäßig falsch erkannt — vor der Übernahme als Zitat gegen das Video prüfen.',
      '',
    );
    if (langMismatch) {
      lines.push(
        `> ⚠️ **Rückübersetzung, nicht der Originalton.** TikTok hat statt der Originalspur eine maschinell nach *${transcriptLang}* übersetzte Fassung geliefert (Caption ist *${captionLang}*). Für Zitate die Caption nutzen oder mit \`--refetch\` einen neuen Abruf versuchen.`,
        '',
      );
    }
    for (const p of paragraphs) lines.push(p, '');
  } else {
    lines.push('## Transkript', '');
    lines.push(
      '> ⚠️ TikTok stellt für dieses Video kein Transkript bereit. Der Actor liefert Transkripte nur, wenn TikTok selbst Untertitel erzeugt hat.',
      '',
    );
  }

  return lines.join('\n');
}
