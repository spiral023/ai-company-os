#!/usr/bin/env python3
"""Fehlende YouTube-Transkripte aus lokalem Audio ergänzen, ohne Notizen zu ersetzen.

Benötigt die optionale Umgebung .venv/youtube-transcription; Einrichtung und
normaler Einstieg über `python ai.py transkribieren --help`.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

import ingest_source as ingest

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "tmp" / "youtube-transcription"
MISSING_NOTE = "Unvollständiger Abruf: Am 11.10.2026 blockierte YouTube den Transkriptabruf im Batch (RequestBlocked / HTTP 429). Nur Metadaten und Videobeschreibung archiviert; der gesprochene Inhalt ist noch nicht erfasst."
MISSING_BODY = "## Abrufstatus\n\nDas Transkript wurde wegen der YouTube-Abrufsperre nicht archiviert. Diese Notiz enthält nur Metadaten und die Videobeschreibung und ist keine vollständige Erfassung des gesprochenen Inhalts. Vor der Knowledge-Einarbeitung das Transkript nachholen."


def frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not match:
        raise ValueError("Notiz hat kein gültiges Frontmatter")
    return match.group(1), match.group(2)


def field(fm: str, key: str) -> str:
    import yaml
    return str((yaml.safe_load(fm) or {}).get(key, ""))


def set_field(fm: str, key: str, value: str | None) -> str:
    pattern = rf"(?m)^{re.escape(key)}:.*(?:\n|$)"
    line = f"{key}: {json.dumps(value, ensure_ascii=False)}\n" if value is not None else ""
    if re.search(pattern, fm):
        return re.sub(pattern, lambda _: line, fm, count=1).rstrip("\n")
    return (fm.rstrip("\n") + "\n" + line).rstrip("\n")


def has_transcript(text: str) -> bool:
    _, body = frontmatter(text)
    section = re.search(r"(?ms)^## Transkript\n(.*?)(?=^## |\Z)", body)
    return bool(section and len(section[1].strip()) >= 100 and "_(kein Text extrahiert)_" not in section[1])


def supplement(text: str, result: dict) -> str:
    """Erhält Originaltext und alle fachlichen Felder; ergänzt nur fehlenden Inhalt."""
    if has_transcript(text):
        return text
    segments = result.get("segments", [])
    words = [str(s["text"]).strip() for s in segments if str(s.get("text", "")).strip()]
    if not words or len(" ".join(words)) < 100:
        raise ValueError("Transkription leer oder zu kurz; Notiz bleibt unverändert")
    fm, body = frontmatter(text)
    original_url = ingest.normalisiere_url(field(fm, "url"))
    if original_url != f'https://www.youtube.com/watch?v={result["video_id"]}':
        raise ValueError("Video-ID der Transkription passt nicht zur Notiz")
    updates = {
        "video_id": result["video_id"], "transkript": "automatisch",
        "transkript_quelle": "lokale Audio-Transkription",
        "transkript_werkzeug": "faster-whisper " + result["version"],
        "transkript_modell": result["model"], "transkript_sprache": result["language"],
        "transkript_generiert": "ja", "transkript_segmente": str(len(words)),
        "transkript_erfasst": result["date"],
    }
    for key, value in updates.items():
        fm = set_field(fm, key, value)
    note = field(fm, "notiz")
    if MISSING_NOTE in note:
        note = note.replace(MISSING_NOTE, "", 1).strip()
        fm = set_field(fm, "notiz", note or None)
    body = body.replace(MISSING_BODY, "").rstrip()
    body = body.replace("## Transkript\n\n_(kein Text extrahiert)_", "").rstrip()
    body = body.replace(
        "> Metadaten über den lokalen YouTube-Abruf aus `ingest_source.py` erfasst; Transkriptabruf blockiert.",
        "> Metadaten lokal erfasst; Transkript mit `faster-whisper` aus der vollständigen Tonspur erzeugt.",
    )
    body += "\n\n## Transkript\n\n" + ingest.formatiere_transkript(words) + "\n"
    return "---\n" + fm + "\n---\n" + body


def find_notes(video: str) -> tuple[Path | None, Path | None]:
    url = f"https://www.youtube.com/watch?v={video}"
    matches = []
    for directory in (ROOT / "00_Inbox/Quellen/YouTube", ROOT / "80_Knowledge/Sources"):
        hits = []
        for path in directory.glob("*.md"):
            text = path.read_text(encoding="utf-8")
            try:
                fm, _ = frontmatter(text)
            except ValueError:
                continue
            if ingest.normalisiere_url(field(fm, "url")) == url:
                hits.append(path)
        if len(hits) > 1:
            raise ValueError(f"Mehrere Notizen zu {video} in {directory}; manuell prüfen")
        matches.append(hits[0] if hits else None)
    return tuple(matches)


def configure_cuda() -> list:
    handles = []
    if os.name == "nt":
        directories = sorted((Path(sys.prefix) / "Lib/site-packages/nvidia").glob("*/bin"))
        os.environ["PATH"] = os.pathsep.join(str(p) for p in directories) + os.pathsep + os.environ.get("PATH", "")
        for directory in directories:
            handles.append(os.add_dll_directory(str(directory)))
    return handles


def download_audio(video: str, directory: Path, hls: bool = False) -> Path:
    import yt_dlp
    directory.mkdir(parents=True, exist_ok=True)
    # Nur Dateien aus diesem ID-Cache wiederverwenden, nie unfertige Downloads.
    audio = list(directory.glob("audio.*"))
    audio = [p for p in audio if p.suffix in {".webm", ".m4a", ".mp4", ".opus", ".mp3"}]
    if len(audio) == 1 and audio[0].stat().st_size > 10_000:
        return audio[0]
    opts = {"format": "bestaudio[protocol*=m3u8]" if hls else "bestaudio",
            "outtmpl": str(directory / "audio.%(ext)s"),
            "js_runtimes": {"deno": {}, "node": {}},
            "noplaylist": True, "socket_timeout": 20, "retries": 0,
            "fragment_retries": 0, "extractor_retries": 0, "noprogress": True,
            "sleep_interval_requests": 1, "sleep_interval": 5, "max_sleep_interval": 8}
    with yt_dlp.YoutubeDL(opts) as downloader:
        info = downloader.extract_info(f"https://www.youtube.com/watch?v={video}", download=True)
        audio_path = Path(downloader.prepare_filename(info))
        (directory / "metadata.json").write_text(json.dumps({
            key: info.get(key) for key in ("id", "title", "uploader", "upload_date", "description", "duration")
        }, ensure_ascii=False, indent=2), encoding="utf-8")
    return audio_path


def transcribe(model, audio: Path, video: str, model_name: str, batch_size: int) -> dict:
    import importlib.metadata
    from faster_whisper import BatchedInferencePipeline
    from faster_whisper.audio import decode_audio
    started = time.monotonic()
    # HLS/AAC kann ohne verlässliche Container-Dauer vorliegen. Die tatsächlich
    # decodierten PCM-Frames liefern die Dauer und denselben Modell-Input.
    samples = decode_audio(str(audio), sampling_rate=16000)
    duration = len(samples) / 16000
    segments, info = BatchedInferencePipeline(model=model).transcribe(
        samples, batch_size=batch_size, beam_size=5, vad_filter=True,
        condition_on_previous_text=False,
    )
    rows = []
    last_progress = time.monotonic()
    for segment in segments:
        rows.append({key: getattr(segment, key) for key in (
            "start", "end", "text", "avg_logprob", "no_speech_prob", "compression_ratio")})
        if time.monotonic() - last_progress >= 20:
            print(f"[FORTSCHRITT] {video}: {segment.end:.0f}/{duration:.0f} Sekunden Audio", flush=True)
            last_progress = time.monotonic()
    return {"video_id": video, "model": model_name,
            "version": importlib.metadata.version("faster-whisper"),
            "date": ingest.heute(), "language": info.language,
            "language_probability": info.language_probability,
            "audio_duration": duration, "speech_duration": info.duration_after_vad,
            "audio_sha256": hashlib.sha256(audio.read_bytes()).hexdigest(),
            "elapsed_seconds": time.monotonic() - started, "segments": rows}


def new_note(video: str, directory: Path, source: Path | None) -> tuple[Path, str]:
    data_path = directory / "metadata.json"
    data = json.loads(data_path.read_text(encoding="utf-8"))
    published = ingest.parse_datum(data.get("upload_date"))
    if source:
        source_fm, _ = frontmatter(source.read_text(encoding="utf-8"))
        published = field(source_fm, "datum") or published
    obj = ingest.Quelle(url=f"https://www.youtube.com/watch?v={video}", typ="youtube",
                       titel=data["title"], text="", autor=data.get("uploader") or "",
                       datum=published, beschreibung=data.get("description") or "")
    target_dir = ROOT / "00_Inbox/Quellen/YouTube"
    slug = ingest.eindeutiger_slug(ingest.baue_slug(obj), obj.url, target_dir)
    text = ingest.baue_notiz(obj, slug).replace("## Transkript\n\n_(kein Text extrahiert)_\n", "")
    text = text.replace("> Automatisch per `python ai.py ingest` erfasst.",
                        "> Metadaten mit `yt-dlp` erfasst; Transkript lokal aus der Tonspur erzeugt.")
    fm, body = frontmatter(text)
    if published and (dt.date.fromisoformat(ingest.heute()) - dt.date.fromisoformat(published)).days >= 90:
        fm = set_field(fm, "notiz", f"Historischer Quellenstand vom {published}. Zeitabhängige Tool-, Modell-, Preis- und API-Aussagen vor heutiger Anwendung neu prüfen.")
    if source:
        fm = set_field(fm, "status", "verarbeitet")
        fm = set_field(fm, "source_notiz", source.relative_to(ROOT).as_posix())
    text = "---\n" + fm + "\n---\n" + body
    return target_dir / f"{slug}.md", text


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("eingaben", nargs="+", help="YouTube-IDs oder URLs")
    parser.add_argument("--audio", type=Path, help="Vorhandene Tonspur für genau ein Video")
    parser.add_argument("--modell", default="large-v3")
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--pause", type=float, default=10, help="Pause zwischen Videos in Sekunden")
    parser.add_argument("--hls", action="store_true", help="Alternative HLS-Tonspur bei HTTP 403 verwenden")
    args = parser.parse_args(argv)
    if args.audio and len(args.eingaben) != 1:
        parser.error("--audio ist nur für ein Video zulässig")
    videos = []
    for value in args.eingaben:
        video = value if re.fullmatch(r"[\w-]{11}", value, flags=re.ASCII) else ingest.youtube_id(value)
        if video not in videos:
            videos.append(video)
    handles = configure_cuda()
    model = None
    for index, video in enumerate(videos):
        path, source = find_notes(video)
        before = path.read_text(encoding="utf-8") if path else None
        if before and has_transcript(before):
            print(f"[BESTAND] {video}: vorhandenes Transkript unverändert", flush=True)
            continue
        directory = CACHE / video
        directory.mkdir(parents=True, exist_ok=True)
        try:
            audio = args.audio.resolve() if args.audio else download_audio(video, directory, args.hls)
            result_path = directory / f"{args.modell}-transcript.json"
            digest = hashlib.sha256(audio.read_bytes()).hexdigest()
            result = json.loads(result_path.read_text(encoding="utf-8")) if result_path.exists() else None
            if not result or result.get("audio_sha256") != digest or result.get("model") != args.modell:
                if model is None:
                    from faster_whisper import WhisperModel
                    print(f"[MODELL] Lade {args.modell} auf CUDA", flush=True)
                    # Nach dem ersten Download ohne erneute Hub-Anfrage laden.
                    cached_model = list((CACHE / "models").glob(
                        f"models--Systran--faster-whisper-{args.modell}/snapshots/*/model.bin"))
                    model = WhisperModel(args.modell, device="cuda", compute_type="float16",
                                         download_root=str(CACHE / "models"), local_files_only=bool(cached_model))
                print(f"[TRANSKRIPTION] {video}", flush=True)
                result = transcribe(model, audio, video, args.modell, args.batch_size)
                result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            metadata_path = directory / "metadata.json"
            if metadata_path.exists():
                expected_duration = json.loads(metadata_path.read_text(encoding="utf-8")).get("duration")
                if expected_duration and abs(expected_duration - result["audio_duration"]) > 3:
                    raise ValueError("Decodierte Tonspur passt zeitlich nicht zur Videodauer; Notiz bleibt unverändert")
            if before is None:
                path, before = new_note(video, directory, source)
            after = supplement(before, result)
            if path.exists() and path.read_text(encoding="utf-8") != before:
                raise ValueError("Notiz während des Abrufs verändert; Schreiben abgebrochen")
            (directory / "before.md").write_text(before, encoding="utf-8")
            path.parent.mkdir(parents=True, exist_ok=True)
            temporary = path.with_suffix(".md.tmp")
            temporary.write_text(after, encoding="utf-8", newline="\n")
            temporary.replace(path)
            (directory / "result.json").write_text(json.dumps({"video_id": video,
                "path": path.relative_to(ROOT).as_posix(), "segments": len(result["segments"]),
                "language": result["language"], "duration": result["audio_duration"],
                "seconds": result["elapsed_seconds"]}, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f'[OK] {video}: {len(result["segments"])} Segmente, {result["language"]}, {result["elapsed_seconds"]:.1f}s → {path.name}', flush=True)
        except Exception as error:
            (directory / "error.txt").write_text(str(error), encoding="utf-8")
            print(f"[FEHLER] {video}: {error}", file=sys.stderr, flush=True)
            return 1  # Kein weiterer Batch-Abruf nach Rate-Limit oder beschädigtem Ergebnis.
        if index < len(videos) - 1:
            time.sleep(max(0, args.pause))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
