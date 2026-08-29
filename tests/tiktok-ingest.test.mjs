import test from 'node:test';
import assert from 'node:assert/strict';

import {
  parseArgs,
  parseTiktokUrl,
  dateFromVideoId,
  parseVtt,
  cuesToParagraphs,
  transcriptDuration,
  formatTimestamp,
  splitCaption,
  handleFromAuthorUrl,
  detectLanguage,
  shortenTitle,
  titleFromTranscript,
  formatTiktokNote,
} from '../scripts/lib/tiktok-ingest.mjs';

const VTT = [
  'WEBVTT',
  '',
  '00:00:00.520 --> 00:00:02.920',
  'prompt Engineering ist tot',
  '',
  '00:00:02.960 --> 00:00:04.000',
  'und keiner hat es gemerkt',
  '',
  '00:00:06.000 --> 00:00:08.500',
  'so viel Kontext wie moeglich',
].join('\n');

test('parseArgs liest Eingabe und Optionen', () => {
  assert.deepEqual(parseArgs(['https://www.tiktok.com/@a/video/123', '--force', '--gap', '1.5']), {
    input: 'https://www.tiktok.com/@a/video/123',
    force: true,
    refetch: false,
    media: true,
    gap: 1.5,
  });
});

test('parseArgs: --refetch impliziert --force, --no-media schaltet Medien ab', () => {
  const args = parseArgs(['123', '--refetch', '--no-media']);
  assert.equal(args.refetch, true);
  assert.equal(args.force, true);
  assert.equal(args.media, false);
});

test('parseTiktokUrl liest Handle und ID, auch mit Query-Parametern', () => {
  assert.deepEqual(
    parseTiktokUrl('https://www.tiktok.com/@kzfadez/video/7477698081920748830?is_from_webapp=1'),
    {
      id: '7477698081920748830',
      username: 'kzfadez',
      url: 'https://www.tiktok.com/@kzfadez/video/7477698081920748830',
    },
  );
});

test('parseTiktokUrl akzeptiert eine nackte Video-ID und /photo/-URLs', () => {
  assert.equal(parseTiktokUrl('7664997418081062177').id, '7664997418081062177');
  assert.equal(parseTiktokUrl('https://www.tiktok.com/@a/photo/7664997418081062177').id, '7664997418081062177');
});

test('parseTiktokUrl meldet Kurzlinks gesondert, damit sie aufgelöst werden können', () => {
  assert.throws(() => parseTiktokUrl('https://vm.tiktok.com/ZGdabc123/'), /Kurzlink/);
  assert.throws(() => parseTiktokUrl('https://example.com/video/1'), /Keine TikTok-Video-URL/);
});

test('dateFromVideoId liest den Timestamp aus den oberen 32 Bit', () => {
  assert.equal(dateFromVideoId('7664997418081062177').slice(0, 10), '2026-07-21');
  assert.equal(dateFromVideoId('nonsense'), null);
  assert.equal(dateFromVideoId('123'), null);
});

test('parseVtt liest Cues mit Start und Ende', () => {
  const cues = parseVtt(VTT);
  assert.equal(cues.length, 3);
  assert.deepEqual(cues[0], { start: 0.52, end: 2.92, text: 'prompt Engineering ist tot' });
  assert.equal(parseVtt('').length, 0);
  assert.equal(parseVtt(null).length, 0);
});

test('cuesToParagraphs trennt an Sprechpausen', () => {
  const cues = parseVtt(VTT);
  assert.deepEqual(cuesToParagraphs(cues, 0.4), [
    'prompt Engineering ist tot und keiner hat es gemerkt',
    'so viel Kontext wie moeglich',
  ]);
  // Große Schwelle: alles bleibt ein Absatz.
  assert.equal(cuesToParagraphs(cues, 5).length, 1);
});

test('transcriptDuration und formatTimestamp', () => {
  assert.equal(transcriptDuration(parseVtt(VTT)), 8.5);
  assert.equal(transcriptDuration([]), null);
  assert.equal(formatTimestamp(8.5), '00:09');
  assert.equal(formatTimestamp(150), '02:30');
});

test('splitCaption trennt Text und Hashtags und dedupliziert', () => {
  assert.deepEqual(splitCaption('Skills erklärt #prompt #coding ##ki #prompt'), {
    text: 'Skills erklärt',
    tags: ['prompt', 'coding', 'ki'],
  });
  assert.deepEqual(splitCaption('#nur #tags'), { text: '', tags: ['nur', 'tags'] });
});

test('titleFromTranscript kürzt an der Wortgrenze', () => {
  const cues = parseVtt(VTT);
  assert.equal(titleFromTranscript(cues, 200), 'prompt Engineering ist tot und keiner hat es gemerkt so viel Kontext wie moeglich');
  assert.equal(titleFromTranscript(cues, 30), 'prompt Engineering ist tot …');
  assert.equal(titleFromTranscript([]), '');
});

test('shortenTitle bevorzugt den ersten abgeschlossenen Satz', () => {
  const caption =
    'Du wirst gerade von KI abgehängt, weil jedes neue Modell beschleunigt. Das solltest du beherrschen. Wann ein Cloud-Modell besser ist.';
  assert.equal(
    shortenTitle(caption),
    'Du wirst gerade von KI abgehängt, weil jedes neue Modell beschleunigt.',
  );
});

test('shortenTitle kappt an der Wortgrenze, wenn der erste Satz zu lang ist', () => {
  const lang = 'wort '.repeat(60).trim();
  const kurz = shortenTitle(lang);
  assert.ok(kurz.length <= 82, `zu lang: ${kurz.length}`);
  assert.match(kurz, / …$/);
  assert.doesNotMatch(kurz, /wor …$/);
});

test('shortenTitle lässt kurze Titel unangetastet', () => {
  assert.equal(shortenTitle('Kurz und knapp.'), 'Kurz und knapp.');
  assert.equal(shortenTitle(''), '');
  assert.equal(shortenTitle(null), '');
});

test('handleFromAuthorUrl liest den Handle, nicht den Anzeigenamen', () => {
  assert.equal(handleFromAuthorUrl('https://www.tiktok.com/@floknowsai'), 'floknowsai');
  assert.equal(handleFromAuthorUrl('https://www.tiktok.com/@a.b_c/'), 'a.b_c');
  assert.equal(handleFromAuthorUrl(null), null);
  assert.equal(handleFromAuthorUrl('https://example.com/x'), null);
});

test('formatTiktokNote baut Frontmatter, Caption und Transkript', () => {
  const note = formatTiktokNote({
    video: {
      id: '7664997418081062177',
      username: 'promptgefluester',
      url: 'https://www.tiktok.com/@promptgefluester/video/7664997418081062177',
    },
    oembed: { title: 'Skills erklärt #prompt #ki', author_name: 'Prompt Geflüster' },
    transcript: VTT,
    slug: '2026-07-21-promptgefluester-7664997418081062177',
    downloads: [{ ok: true, cover: true, file: '01-cover.jpg', url: 'https://p19.tiktokcdn.com/x.jpg' }],
    fetchedAt: '2026-08-30T08:00:00.000Z',
  });

  assert.match(note, /^---\n/);
  assert.match(note, /url: https:\/\/www\.tiktok\.com\/@promptgefluester\/video\/7664997418081062177\n/);
  assert.match(note, /datum: 2026-07-21\n/);
  assert.match(note, /erfasst: 2026-08-30\n/);
  assert.match(note, /quelle: tiktok\n/);
  assert.match(note, /status: neu\n/);
  assert.match(note, /autor_name: "Prompt Geflüster"\n/);
  assert.match(note, /hashtags: "prompt, ki"\n/);
  assert.match(note, /transkript: "3 Cues/);
  assert.match(note, /laenge: "00:09"/);
  assert.match(note, /# Skills erklärt\n/);
  assert.match(note, /!\[Cover\]\(medien\/2026-07-21-promptgefluester-7664997418081062177\/01-cover\.jpg\)/);
  assert.match(note, /## Transkript\n/);
  assert.match(note, /prompt Engineering ist tot und keiner hat es gemerkt/);
  // Der Text steht genau einmal in der Notiz — keine zweite Fassung mit Zeitmarken.
  assert.doesNotMatch(note, /Zeitmarken|<details>|`00:0/);
});

test('detectLanguage unterscheidet Deutsch und Englisch, schweigt bei zu wenig Text', () => {
  const deutsch =
    'Anthropic hat die Claude Academy veröffentlicht und ich muss ehrlich sagen das ist eine richtig gute Grundlage für alle die mit KI durchstarten wollen';
  const englisch =
    'Anthropic has published the Claude Academy and I must say honestly this is a really good basis for all who want to take off with AI today';
  assert.equal(detectLanguage(deutsch), 'de');
  assert.equal(detectLanguage(englisch), 'en');
  assert.equal(detectLanguage('zu kurz'), null);
  assert.equal(detectLanguage(''), null);
  assert.equal(detectLanguage(null), null);
});

test('formatTiktokNote markiert ein übersetztes Transkript gegen die Caption', () => {
  const englischesVtt = [
    'WEBVTT',
    '',
    '00:00:00.000 --> 00:00:04.000',
    'stop reading the code of your AI agents at least that is what the man who wrote clean code says',
    '',
    '00:00:04.100 --> 00:00:08.000',
    'and in July he declared why he no longer reads through the code of his agents in this case',
  ].join('\n');

  const note = formatTiktokNote({
    video: { id: '7675431688024984865', username: 'floknowsai', url: 'https://www.tiktok.com/@floknowsai/video/7675431688024984865' },
    oembed: {
      title:
        'Hör auf, den Code deines KI-Agenten zu lesen. Das sagt der Autor von Clean Code, nicht weil er den Code für fehlerfrei hält, sondern weil er seinem Testing vertraut und das ist der Punkt.',
    },
    transcript: englischesVtt,
    slug: 's',
    downloads: [],
    fetchedAt: '2026-08-30T08:00:00.000Z',
  });

  assert.match(note, /sprache: en\n/);
  assert.match(note, /sprache_abweichung: true\n/);
  assert.match(note, /Rückübersetzung, nicht der Originalton/);
});

test('formatTiktokNote markiert nichts, wenn Transkript und Caption dieselbe Sprache haben', () => {
  const deutschesVtt = [
    'WEBVTT',
    '',
    '00:00:00.000 --> 00:00:04.000',
    'hör auf den Code deines KI Agenten zu lesen das sagt der Autor von Clean Code und das ist',
    '',
    '00:00:04.100 --> 00:00:08.000',
    'nicht weil er den Code für fehlerfrei hält sondern weil er seinem Testing vertraut wie man sieht',
  ].join('\n');

  const note = formatTiktokNote({
    video: { id: '7675431688024984865', username: 'floknowsai', url: 'https://www.tiktok.com/@floknowsai/video/7675431688024984865' },
    oembed: {
      title:
        'Hör auf, den Code deines KI-Agenten zu lesen. Das sagt der Autor von Clean Code, nicht weil er den Code für fehlerfrei hält, sondern weil er seinem Testing vertraut und das ist der Punkt.',
    },
    transcript: deutschesVtt,
    slug: 's',
    downloads: [],
    fetchedAt: '2026-08-30T08:00:00.000Z',
  });

  assert.match(note, /sprache: de\n/);
  assert.doesNotMatch(note, /sprache_abweichung/);
  assert.doesNotMatch(note, /Rückübersetzung/);
});

test('formatTiktokNote hält fest, wenn kein Transkript vorliegt', () => {
  const note = formatTiktokNote({
    video: { id: '7664997418081062177', username: 'a', url: 'https://www.tiktok.com/@a/video/7664997418081062177' },
    oembed: null,
    transcript: '',
    slug: 's',
    downloads: [],
    fetchedAt: '2026-08-30T08:00:00.000Z',
  });
  assert.match(note, /transkript: "keins verfügbar"/);
  assert.match(note, /kein Transkript bereit/);
});

test('formatTiktokNote markiert ein unsicheres Datum statt still zu raten', () => {
  const note = formatTiktokNote({
    video: { id: '123', username: 'a', url: 'https://www.tiktok.com/@a/video/123' },
    oembed: null,
    transcript: '',
    slug: 's',
    downloads: [],
    fetchedAt: '2026-08-30T08:00:00.000Z',
  });
  assert.match(note, /datum: 2026-08-30\n/);
  assert.match(note, /datum_unsicher: true/);
});
