import test from 'node:test';
import assert from 'node:assert/strict';

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
  formatDump,
} from '../scripts/lib/x-ingest.mjs';

test('parseArgs liest Eingabe und Thread-Optionen', () => {
  assert.deepEqual(parseArgs(['https://x.com/user/status/123', '--thread', '--force', '--max-thread', '12']), {
    input: 'https://x.com/user/status/123',
    thread: true,
    force: true,
    maxThread: 12,
  });
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

test('Threads werden erkannt, chronologisch sortiert und im Dump ausgegeben', () => {
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

  const dump = formatDump({
    tweet,
    author: { name: 'Ada', username: 'ada' },
    media: [],
    articleMedia: [],
    thread: [earlier, tweet],
  });
  assert.match(dump, /^# X-Ingest: Ada \(@ada\)/);
  assert.match(dump, /## Thread/);
  assert.match(dump, /### 2\/2\n\nStart/);
});
