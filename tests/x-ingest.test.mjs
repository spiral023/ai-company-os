import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

import {
  parseArgs,
  parseTweetId,
  extractTweetText,
  extractArticleText,
  extractLinks,
  extractMedia,
  extractArticleMedia,
  isThreadStart,
  orderThreadChronologically,
  threadIdentity,
} from '../scripts/lib/x-ingest.mjs';
import {
  buildSlug,
  mediaFileName,
  originalSizeUrl,
  downloadMedia,
  formatInboxNote,
  sourceInboxRel,
  writeInboxNote,
  mediaTargetDir,
} from '../scripts/lib/inbox-store.mjs';

test('parseArgs liest Eingabe und Thread-Optionen', () => {
  assert.deepEqual(parseArgs(['https://x.com/user/status/123', '--thread', '--force', '--max-thread', '12']), {
    input: 'https://x.com/user/status/123',
    thread: true,
    force: true,
    refetch: false,
    maxThread: 12,
    media: true,
  });
  assert.equal(parseArgs(['123', '--no-media']).media, false);
  // --refetch impliziert --force: neu geholte Daten sollen auch die Notiz erneuern.
  const refetch = parseArgs(['123', '--refetch']);
  assert.equal(refetch.refetch, true);
  assert.equal(refetch.force, true);
});

test('parseTweetId akzeptiert X-URLs und numerische IDs', () => {
  assert.equal(parseTweetId('123456'), '123456');
  assert.equal(parseTweetId('https://x.com/example/status/987654?s=20'), '987654');
  assert.throws(() => parseTweetId('kein Tweet'), /Konnte keine Tweet-ID/);
});

test('Text und Links bevorzugen note_tweet und entfernen Link-Duplikate', () => {
  const tweet = {
    text: 'kurz',
    note_tweet: {
      text: 'lang',
      entities: {
        urls: [
          { url: 'https://t.co/a', expanded_url: 'https://example.com', display_url: 'example.com' },
          { url: 'https://t.co/b', expanded_url: 'https://example.com', display_url: 'example.com' },
        ],
      },
    },
    article: { plain_text: 'Artikeltext' },
  };

  assert.equal(extractTweetText(tweet), 'lang');
  assert.equal(extractArticleText(tweet), 'Artikeltext');
  assert.deepEqual(extractLinks(tweet), [{ url: 'https://example.com', display: 'example.com' }]);
});

test('Tweet- und Artikel-Medien werden normalisiert und per media_key aufgelöst', () => {
  const includes = [
    { media_key: 'cover', type: 'photo', alt_text: 'Titelbild', url: 'https://pbs.twimg.com/cover.jpg' },
    { media_key: 'inline', type: 'photo', preview_image_url: 'https://pbs.twimg.com/inline.jpg' },
  ];
  const tweet = { article: { cover_media: 'cover', media_entities: [{ media_key: 'inline' }] } };

  assert.deepEqual(extractMedia(includes)[0], {
    type: 'photo',
    alt: 'Titelbild',
    url: 'https://pbs.twimg.com/cover.jpg',
  });
  assert.deepEqual(extractArticleMedia(tweet, includes), [
    {
      type: 'photo',
      alt: 'Titelbild',
      url: 'https://pbs.twimg.com/cover.jpg',
      cover: true,
    },
    {
      type: 'photo',
      alt: '',
      url: 'https://pbs.twimg.com/inline.jpg',
      cover: false,
    },
  ]);
});

test('Threads werden erkannt und chronologisch sortiert', () => {
  const tweet = {
    id: '2',
    conversation_id: '2',
    author_id: 'u1',
    created_at: '2026-01-02T00:00:00.000Z',
    text: 'Start',
  };
  const earlier = { id: '1', created_at: '2026-01-01T00:00:00.000Z', text: 'Früher' };
  assert.equal(isThreadStart(tweet), true);
  assert.deepEqual(orderThreadChronologically([tweet, earlier]).map((item) => item.id), ['1', '2']);
});

test('Slug und Medien-Dateinamen sind stabil und dateisystemsicher', () => {
  assert.equal(
    buildSlug({ createdAt: '2026-07-27T19:44:39.000Z', username: 'Cerebras', id: '208182' }),
    '2026-07-27-cerebras-208182',
  );
  // Kaputter Handle darf keinen Pfad erzeugen, der aus dem Zielordner ausbricht.
  assert.equal(buildSlug({ createdAt: '2026-01-01', username: '../evil', id: '1' }), '2026-01-01-evil-1');
  assert.equal(mediaFileName(0, { cover: true, type: 'photo', url: 'https://x/a.png' }), '01-cover.png');
  assert.equal(mediaFileName(9, { type: 'photo', url: 'https://x/a.jpg?name=small' }), '10-photo.jpg');
  assert.equal(mediaFileName(1, { type: 'video', url: 'https://x/clip' }), '02-video.mp4');
});

test('Quelltypen werden in feste Inbox-Unterordner geroutet', () => {
  assert.equal(sourceInboxRel('x'), '00_Inbox/Quellen/X');
  assert.equal(sourceInboxRel('tiktok'), '00_Inbox/Quellen/TikTok');
  assert.equal(sourceInboxRel('unbekannt'), '00_Inbox/Quellen/Sonstige');
});

test('Notizen und Medienziele werden im Typordner angelegt', (t) => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'inbox-routing-test-'));
  t.after(() => fs.rmSync(dir, { recursive: true, force: true }));

  const note = writeInboxNote(dir, 'x', 'slug', 'Inhalt');
  assert.equal(note, path.join(dir, '00_Inbox/Quellen/X/slug.md'));
  assert.equal(fs.readFileSync(note, 'utf8'), 'Inhalt');
  assert.equal(
    mediaTargetDir(dir, 'tiktok', 'video-slug'),
    path.join(dir, '00_Inbox/Quellen/TikTok/medien/video-slug'),
  );
});

test('originalSizeUrl fordert bei twimg die Originalgröße, sonst nichts', () => {
  assert.equal(originalSizeUrl('https://pbs.twimg.com/media/a.jpg'), 'https://pbs.twimg.com/media/a.jpg?name=orig');
  assert.equal(originalSizeUrl('https://pbs.twimg.com/media/a.jpg?name=small'), 'https://pbs.twimg.com/media/a.jpg?name=small');
  assert.equal(originalSizeUrl('https://example.com/a.jpg'), 'https://example.com/a.jpg');
});

test('downloadMedia schreibt Dateien und übersteht einzelne Fehlschläge', async (t) => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'x-ingest-test-'));
  t.after(() => fs.rmSync(dir, { recursive: true, force: true }));

  const fakeFetch = async (url) => {
    if (url.includes('kaputt')) return { ok: false, status: 404 };
    return { ok: true, arrayBuffer: async () => new TextEncoder().encode('BILD').buffer };
  };
  const results = await downloadMedia(
    [
      { type: 'photo', cover: true, url: 'https://pbs.twimg.com/media/ok.jpg' },
      { type: 'photo', url: 'https://pbs.twimg.com/media/kaputt.jpg' },
      { type: 'photo', url: '', key: 'ungeloest' },
    ],
    dir,
    { fetch: fakeFetch },
  );

  assert.equal(results[0].ok, true);
  assert.equal(fs.readFileSync(path.join(dir, '01-cover.jpg'), 'utf8'), 'BILD');
  assert.equal(results[1].ok, false);
  assert.match(results[1].error, /HTTP 404/);
  assert.match(results[2].error, /media_key: ungeloest/);

  // Zweiter Lauf lädt vorhandene Dateien nicht erneut.
  const again = await downloadMedia(
    [{ type: 'photo', cover: true, url: 'https://pbs.twimg.com/media/ok.jpg' }],
    dir,
    {
      fetch: async () => {
        throw new Error('darf nicht aufgerufen werden');
      },
    },
  );
  assert.equal(again[0].skipped, true);
});

test('Inbox-Notiz trägt Status, lokale Bildpfade und Thread', () => {
  const tweet = {
    id: '42',
    conversation_id: '42',
    created_at: '2026-07-27T19:44:39.000Z',
    text: 'https://t.co/x',
    article: { title: 'Mein Artikel', plain_text: 'Volltext hier' },
    public_metrics: { like_count: 5, retweet_count: 1, reply_count: 0, impression_count: 99 },
  };
  const note = formatInboxNote({
    tweet,
    author: { name: 'Ada "Lovelace"', username: 'ada' },
    slug: '2026-07-27-ada-42',
    media: [],
    articleMedia: [{ type: 'photo', cover: true, alt: 'Chart', url: 'https://pbs.twimg.com/media/a.jpg' }],
    thread: [tweet, { id: '43', text: 'Zweiter Post' }],
    threadMethod: 'backward-walk',
    downloads: [{ url: 'https://pbs.twimg.com/media/a.jpg', file: '01-cover.jpg', ok: true }],
    fetchedAt: '2026-08-04T10:00:00.000Z',
  });

  assert.match(note, /^---\n/);
  assert.match(note, /\nstatus: neu\n/);
  assert.match(note, /\ndatum: 2026-07-27\n/);
  assert.match(note, /\nerfasst: 2026-08-04\n/);
  assert.match(note, /typ: artikel/);
  assert.match(note, /autor_name: "Ada \\"Lovelace\\""/);
  assert.match(note, /medien: "1\/1 lokal"/);
  assert.match(note, /thread_posts: 2/);
  assert.match(note, /## Artikel-Volltext\n\nVolltext hier/);
  assert.match(note, /!\[Chart\]\(medien\/2026-07-27-ada-42\/01-cover\.jpg\)/);
  assert.match(note, /### 2\/2\n\nZweiter Post/);
});

test('Nicht geladene Bilder behalten die Remote-URL und werden markiert', () => {
  const note = formatInboxNote({
    tweet: { id: '7', text: 'Post' },
    author: { name: 'Ada', username: 'ada' },
    slug: '2026-01-01-ada-7',
    media: [{ type: 'photo', alt: '', url: 'https://pbs.twimg.com/media/b.jpg' }],
    articleMedia: [],
    downloads: [{ url: 'https://pbs.twimg.com/media/b.jpg', file: '01-photo.jpg', ok: false, error: 'HTTP 404' }],
    fetchedAt: '2026-01-02T00:00:00.000Z',
  });
  assert.match(note, /nicht lokal gespeichert/);
  assert.match(note, /!\[photo\]\(https:\/\/pbs\.twimg\.com\/media\/b\.jpg\)/);
});

test('threadIdentity ankert einen Einzelpost an sich selbst', () => {
  const tweet = { id: '5', author_id: 'a', conversation_id: '5', created_at: '2026-01-01T00:00:00.000Z' };
  const { anker, ids } = threadIdentity(tweet, null);
  assert.equal(anker.id, '5');
  assert.deepEqual([...ids].sort(), ['5']);
});

test('threadIdentity ankert einen Thread am aeltesten eigenen Post', () => {
  // Rueckwaerts-Walk vom letzten Post: Die Notiz soll unter dem Start liegen,
  // damit ein Nachlauf ueber den letzten Post dieselbe Datei trifft.
  const start = { id: '1', author_id: 'a', conversation_id: '1', created_at: '2026-01-01T10:00:00.000Z' };
  const mitte = { id: '2', author_id: 'a', conversation_id: '1', created_at: '2026-01-01T10:05:00.000Z' };
  const letzter = { id: '3', author_id: 'a', conversation_id: '1', created_at: '2026-01-01T10:09:00.000Z' };
  const { anker, ids } = threadIdentity(letzter, [letzter, start, mitte]);
  assert.equal(anker.id, '1');
  assert.deepEqual([...ids].sort(), ['1', '2', '3']);
});

test('threadIdentity laesst fremde Posts der Kette aussen vor', () => {
  // Antwort auf einen fremden Tweet: Dessen conversation_id gehoert nicht zu
  // dieser Quelle, sonst wuerden zwei verschiedene Quellen verschmelzen.
  const fremd = { id: '1', author_id: 'b', conversation_id: '1', created_at: '2026-01-01T10:00:00.000Z' };
  const eigen = { id: '2', author_id: 'a', conversation_id: '1', created_at: '2026-01-01T10:05:00.000Z' };
  const { anker, ids } = threadIdentity(eigen, [fremd, eigen]);
  assert.equal(anker.id, '2');
  assert.deepEqual([...ids].sort(), ['2']);
  assert.equal(ids.has('1'), false);
});

test('Frontmatter traegt die conversation_id des Strangs', () => {
  const note = formatInboxNote({
    tweet: { id: '3', conversation_id: '1', text: 'Letzter Post', created_at: '2026-01-01T10:09:00.000Z' },
    author: { name: 'Ada', username: 'ada' },
    slug: '2026-01-01-ada-1',
    media: [],
    articleMedia: [],
    fetchedAt: '2026-01-02T00:00:00.000Z',
  });
  assert.match(note, /\ntweet_id: "3"\n/);
  assert.match(note, /\nconversation_id: "1"\n/);
});

test('Ohne conversation_id faellt das Feld auf die Tweet-ID zurueck', () => {
  const note = formatInboxNote({
    tweet: { id: '9', text: 'Einzelpost', created_at: '2026-01-01T10:00:00.000Z' },
    author: { name: 'Ada', username: 'ada' },
    slug: '2026-01-01-ada-9',
    media: [],
    articleMedia: [],
    fetchedAt: '2026-01-02T00:00:00.000Z',
  });
  assert.match(note, /\nconversation_id: "9"\n/);
});

test('Posts Dritter im Thread werden ihrem Urheber zugeschrieben', () => {
  // Der Rueckwaerts-Walk nimmt Antworten Dritter mit. Ohne Kennzeichnung
  // laesen sie sich wie Aussagen des Autors.
  const note = formatInboxNote({
    tweet: { id: '1', author_id: 'a', conversation_id: '1', text: 'Erstpost', created_at: '2026-01-01T10:00:00.000Z' },
    author: { name: 'Ada', username: 'ada' },
    slug: '2026-01-01-ada-1',
    media: [],
    articleMedia: [],
    thread: [
      { id: '1', author_id: 'a', text: 'Erstpost' },
      { id: '2', author_id: 'b', text: 'Fremde Antwort' },
      { id: '3', author_id: 'a', text: 'Antwort des Autors' },
    ],
    threadMethod: 'backward-walk',
    threadUsers: [
      { id: 'a', username: 'ada' },
      { id: 'b', username: 'grace' },
    ],
    fetchedAt: '2026-01-02T00:00:00.000Z',
  });

  assert.match(note, /### 1\/3\n/);
  assert.match(note, /### 2\/3 · Reply von @grace \(nicht vom Autor\)/);
  assert.match(note, /### 3\/3\n/);
});

test('Ohne bekannten Handle bleibt der fremde Post trotzdem markiert', () => {
  const note = formatInboxNote({
    tweet: { id: '1', author_id: 'a', text: 'Erstpost', created_at: '2026-01-01T10:00:00.000Z' },
    author: { name: 'Ada', username: 'ada' },
    slug: '2026-01-01-ada-1',
    media: [],
    articleMedia: [],
    thread: [
      { id: '1', author_id: 'a', text: 'Erstpost' },
      { id: '2', author_id: 'b', text: 'Fremde Antwort' },
    ],
    threadMethod: 'backward-walk',
    fetchedAt: '2026-01-02T00:00:00.000Z',
  });
  assert.match(note, /### 2\/2 · Reply von @unbekannt \(nicht vom Autor\)/);
});
