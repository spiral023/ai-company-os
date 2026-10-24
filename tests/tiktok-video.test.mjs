import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { downloadTiktokVideo, transcribeMissingTiktok, TIKTOK_VIDEO_FILE } from '../scripts/lib/tiktok-video.mjs';

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

function transcriptFixture(t, transcript = 'nicht verfügbar') {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'tiktok-whisper-test-'));
  t.after(() => {
    assert.equal(path.dirname(path.resolve(root)), path.resolve(os.tmpdir()));
    assert.ok(path.basename(root).startsWith('tiktok-whisper-test-'));
    fs.rmSync(root, { recursive: true, force: true });
  });
  const note = path.join(root, 'quelle.md');
  const media = path.join(root, 'medien', 'quelle');
  fs.mkdirSync(media, { recursive: true });
  fs.writeFileSync(path.join(media, TIKTOK_VIDEO_FILE), 'Video');
  fs.writeFileSync(note, `---\nstatus: verarbeitet\ntranskript: ${transcript}\n---\n\n# Original\n`);
  return { root, note };
}

test('Whisper ergänzt nur eine fehlende Spur über die lokale CLI', async t => {
  const { root, note } = transcriptFixture(t);
  const url = 'https://www.tiktok.com/@a/video/7699871396729507105';
  const result = await transcribeMissingTiktok(note, url, root, { run: async (exe, args, options) => {
    assert.deepEqual(args, [path.join(root, 'ai.py'), 'transkribieren', url]);
    assert.equal(options.cwd, root);
    assert.equal(options.windowsHide, true);
    fs.writeFileSync(note, fs.readFileSync(note, 'utf8').replace('nicht verfügbar', 'automatisch') + '\n## Transkript\n\nGesprochener Text.\n');
    return { stdout: '[OK]' };
  } });
  assert.equal(result.ok, true);
  assert.match(fs.readFileSync(note, 'utf8'), /status: verarbeitet/);
});

test('Native Untertitel und --no-whisper starten keine Transkription', async t => {
  for (const [native, enabled] of [[true, true], [false, false]]) {
    const { root, note } = transcriptFixture(t, native ? 'automatisch' : 'nicht verfügbar');
    const before = fs.readFileSync(note);
    const result = await transcribeMissingTiktok(note, 'url', root, {
      whisper: enabled, run: async () => { throw new Error('Darf nicht laufen'); },
    });
    assert.equal(result.skipped, true);
    assert.deepEqual(fs.readFileSync(note), before);
  }
});

test('Fehler und leere Erfolgsantworten melden keine erfolgreiche Transkription', async t => {
  for (const fail of [true, false]) {
    const { root, note } = transcriptFixture(t);
    const before = fs.readFileSync(note);
    const result = await transcribeMissingTiktok(note, 'url', root, { run: async () => {
      if (fail) throw new Error('Keine GPU verfügbar');
      return { stdout: '[OK]' };
    } });
    assert.equal(result.ok, false);
    assert.deepEqual(fs.readFileSync(note), before);
  }
});
