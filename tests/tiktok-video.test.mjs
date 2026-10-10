import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { downloadTiktokVideo, TIKTOK_VIDEO_FILE } from '../scripts/lib/tiktok-video.mjs';

function directory(t) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'tiktok-video-test-'));
  t.after(() => {
    for (const file of fs.readdirSync(dir)) fs.unlinkSync(path.join(dir, file));
    fs.rmdirSync(dir);
  });
  return dir;
}

test('Vorhandene MP4 wird ohne Downloader-Aufruf wiederverwendet', async (t) => {
  const dir = directory(t);
  fs.writeFileSync(path.join(dir, TIKTOK_VIDEO_FILE), 'vorhandenes Video');
  const result = await downloadTiktokVideo('https://www.tiktok.com/@a/video/123', dir, {
    run: () => { throw new Error('soll nicht aufgerufen werden'); },
  });
  assert.equal(result.ok, true);
  assert.equal(result.skipped, true);
});

test('Unvollständiger Download erhält keinen erfolgreichen Video-Verweis', async (t) => {
  const dir = directory(t);
  const result = await downloadTiktokVideo('https://www.tiktok.com/@a/video/123', dir, {
    run: async () => {
      fs.writeFileSync(path.join(dir, `${TIKTOK_VIDEO_FILE}.part`), 'unvollständig');
      throw Object.assign(new Error('Abruf gescheitert'), { stderr: 'HTTP 403' });
    },
  });
  assert.equal(result.ok, false);
  assert.equal(result.error, 'HTTP 403');
  assert.equal(fs.existsSync(path.join(dir, TIKTOK_VIDEO_FILE)), false);
});

test('Fehlendes yt-dlp gibt eine konkrete Installationsanweisung', async (t) => {
  const result = await downloadTiktokVideo('https://www.tiktok.com/@a/video/123', directory(t), {
    run: async () => { throw Object.assign(new Error('fehlt'), { stderr: 'No module named yt_dlp' }); },
  });
  assert.equal(result.ok, false);
  assert.match(result.error, /python -m pip install/);
});
