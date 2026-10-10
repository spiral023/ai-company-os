import fs from 'node:fs';
import path from 'node:path';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';

const run = promisify(execFile);
export const TIKTOK_VIDEO_FILE = '02-video.mp4';

// Gemeinsame MP4 mit Bild und Ton, ohne ffmpeg. yt-dlp benennt die .part-
// Datei erst nach abgeschlossenem Download zur fertigen MP4 um.
export async function downloadTiktokVideo(url, targetDir, options = {}) {
  const dest = path.join(targetDir, TIKTOK_VIDEO_FILE);
  const entry = { file: TIKTOK_VIDEO_FILE, ok: false, skipped: false };
  if (fs.existsSync(dest) && fs.statSync(dest).size > 0) {
    return { ...entry, ok: true, skipped: true, bytes: fs.statSync(dest).size };
  }
  fs.mkdirSync(targetDir, { recursive: true });
  try {
    await (options.run ?? run)(process.env.TIKTOK_PYTHON ?? 'python', [
      '-m', 'yt_dlp', '--ignore-config', '--no-playlist', '--no-overwrites',
      '--no-progress', '--socket-timeout', '20', '--retries', '1',
      '--format', 'best[ext=mp4][vcodec=h264][acodec!=none]/best[ext=mp4][acodec!=none]',
      '--output', dest, '--', url,
    ], { windowsHide: true, timeout: 120_000, maxBuffer: 1024 * 1024 });
    if (!fs.existsSync(dest) || fs.statSync(dest).size === 0) {
      throw new Error('Downloader hat keine vollständige MP4-Datei angelegt.');
    }
    return { ...entry, ok: true, bytes: fs.statSync(dest).size };
  } catch (err) {
    const detail = String(err.stderr || err.message || err).trim();
    const missing = err.code === 'ENOENT' || /No module named yt_dlp/.test(detail);
    return {
      ...entry,
      error: missing
        ? 'Python/yt-dlp fehlt. Installieren: python -m pip install --user "yt-dlp[default,curl-cffi]"'
        : detail.slice(-700),
    };
  }
}
