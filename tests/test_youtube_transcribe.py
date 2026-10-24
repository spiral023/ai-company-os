"""Schutz vorhandener Rohquellen beim Nachholen von Transkripten; ohne GPU/Netz."""
import importlib.util
import hashlib
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "70_Scripts"))
SPEC = importlib.util.spec_from_file_location("youtube_transcribe", ROOT / "70_Scripts/youtube_transcribe.py")
transcribe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(transcribe)


def example():
    note = "Historischer Stand. " + transcribe.MISSING_NOTE + " Manuelle Ergänzung: üben."
    return (
        '---\nurl: https://www.youtube.com/watch?v=2EoNRuFJfBo\n'
        'datum: 2025-04-09\nerfasst: 2026-10-11\nstatus: verarbeitet\n'
        'source_notiz: 80_Knowledge/Sources/beispiel.md\n'
        'notiz: ' + json.dumps(note, ensure_ascii=False) + '\n---\n'
        '# Originaltitel\n\n## Beschreibung\n\nOriginalbeschreibung mit Umlauten.\n\n'
        + transcribe.MISSING_BODY + '\n'
    )


def result():
    return dict(video_id="2EoNRuFJfBo", model="large-v3", version="1.2.1",
                language="de", date="2026-10-11", segments=[
                    {"text": "Dies ist ein vollständiger gesprochener Beispielsatz mit technischen Details. " * 4}
                ])


def test_preserves_description_date_processing_and_manual_notes():
    text = transcribe.supplement(example(), result())
    fm, body = transcribe.frontmatter(text)
    for key, value in (("datum", "2025-04-09"), ("erfasst", "2026-10-11"),
                       ("status", "verarbeitet"), ("source_notiz", "80_Knowledge/Sources/beispiel.md")):
        assert transcribe.field(fm, key) == value
    assert transcribe.field(fm, "notiz") == "Historischer Stand.  Manuelle Ergänzung: üben."
    assert "Originalbeschreibung mit Umlauten." in body
    assert transcribe.MISSING_BODY not in body
    assert transcribe.field(fm, "transkript_quelle") == "lokale Audio-Transkription"
    assert transcribe.has_transcript(text)


def test_existing_transcript_is_unchanged():
    text = transcribe.supplement(example(), result())
    assert transcribe.supplement(text, {"segments": []}) == text


def test_short_existing_subtitles_are_never_replaced():
    text = example() + "\n## Transkript\n\nEin kurzes Originaltranskript.\n"
    assert transcribe.supplement(text, result()) == text


def tiktok_example():
    return (
        '---\nurl: https://www.tiktok.com/@autor/video/7699871396729507105\n'
        'video_id: "7699871396729507105"\nquelle: tiktok\ntyp: video\n'
        'datum: 2026-10-23\nerfasst: 2026-10-24\nstatus: verarbeitet\n'
        'source_notiz: 80_Knowledge/Sources/bestand.md\ntranskript: nicht verfügbar\n'
        'notiz: "Manuelle Einordnung erhalten"\n---\n\n# Titel\n\n'
        '## Caption\n\nUnveränderte Caption mit Links.\n\n'
        '## Lokales Video\n\n[Video](medien/quelle/02-video.mp4)\n'
    )


def test_tiktok_supplement_keeps_processing_caption_and_video():
    data = result() | {"video_id": "7699871396729507105"}
    text = transcribe.supplement(tiktok_example(), data)
    fm, body = transcribe.frontmatter(text)
    assert transcribe.field(fm, "status") == "verarbeitet"
    assert transcribe.field(fm, "source_notiz") == "80_Knowledge/Sources/bestand.md"
    assert transcribe.field(fm, "notiz") == "Manuelle Einordnung erhalten"
    assert transcribe.field(fm, "sprache") == "de"
    assert transcribe.field(fm, "transkript") == "automatisch"
    assert "Unveränderte Caption mit Links." in body
    assert "[Video](medien/quelle/02-video.mp4)" in body
    with pytest.raises(ValueError, match="Video-ID"):
        transcribe.supplement(tiktok_example(), result())


def test_tiktok_cached_audio_is_local_atomic_and_idempotent(tmp_path, monkeypatch):
    monkeypatch.setattr(transcribe, "ROOT", tmp_path)
    monkeypatch.setattr(transcribe, "CACHE", tmp_path / "cache")
    monkeypatch.setattr(transcribe, "configure_cuda", lambda: [])
    monkeypatch.setattr(transcribe, "download_audio", lambda *a: pytest.fail("Kein Netzwerkabruf"))
    note = tmp_path / "00_Inbox/Quellen/TikTok/quelle.md"
    note.parent.mkdir(parents=True)
    note.write_text(tiktok_example(), encoding="utf-8", newline="\n")
    media = note.parent / "medien/quelle"
    media.mkdir(parents=True)
    video = media / "02-video.mp4"
    video.write_bytes(b"lokale Videodatei")
    directory = transcribe.CACHE / "tiktok-7699871396729507105"
    directory.mkdir(parents=True)
    data = result() | dict(video_id="7699871396729507105", audio_duration=12,
        elapsed_seconds=1, audio_sha256=hashlib.sha256(video.read_bytes()).hexdigest())
    (directory / "large-v3-transcript.json").write_text(json.dumps(data), encoding="utf-8")
    assert transcribe.main(["https://www.tiktok.com/@autor/video/7699871396729507105"]) == 0
    updated = note.read_bytes()
    assert transcribe.has_transcript(updated.decode("utf-8"))
    assert json.loads((media / "transkript-whisper.json").read_text(encoding="utf-8"))["video_id"] == data["video_id"]
    assert transcribe.main(["7699871396729507105"]) == 0
    assert note.read_bytes() == updated


def test_tiktok_missing_audio_does_not_touch_the_note(tmp_path, monkeypatch):
    monkeypatch.setattr(transcribe, "ROOT", tmp_path)
    monkeypatch.setattr(transcribe, "CACHE", tmp_path / "cache")
    monkeypatch.setattr(transcribe, "configure_cuda", lambda: [])
    note = tmp_path / "00_Inbox/Quellen/TikTok/quelle.md"
    note.parent.mkdir(parents=True)
    note.write_text(tiktok_example(), encoding="utf-8", newline="\n")
    before = note.read_bytes()
    assert transcribe.main(["7699871396729507105"]) == 1
    assert note.read_bytes() == before


@pytest.mark.parametrize("changes", [{"segments": []}, {"video_id": "dX0a9L4f_Lc"}])
def test_invalid_result_is_rejected(changes):
    data = result() | changes
    with pytest.raises(ValueError):
        transcribe.supplement(example(), data)


def test_empty_transcript_placeholder_does_not_create_duplicate_section():
    original = example() + '\n## Transkript\n\n_(kein Text extrahiert)_\n'
    text = transcribe.supplement(original, result())
    assert text.count("## Transkript") == 1


def test_new_raw_note_references_existing_source_and_preserves_historic_date(tmp_path, monkeypatch):
    monkeypatch.setattr(transcribe, "ROOT", tmp_path)
    source = tmp_path / "80_Knowledge/Sources/existing.md"
    source.parent.mkdir(parents=True)
    source.write_text('---\ndatum: 2026-02-24\n---\nOriginalwissen\n', encoding="utf-8")
    before = source.read_bytes()
    cache = tmp_path / "cache"
    cache.mkdir()
    (cache / "metadata.json").write_text(json.dumps(dict(
        title="Originalvideo", uploader="Autor", description="Beschreibung",
        upload_date="20260225")), encoding="utf-8")
    path, text = transcribe.new_note("2EoNRuFJfBo", cache, source)
    fm, _ = transcribe.frontmatter(text)
    assert transcribe.field(fm, "datum") == "2026-02-24"
    assert transcribe.field(fm, "status") == "verarbeitet"
    assert (tmp_path / transcribe.field(fm, "source_notiz")) == source
    assert "Historischer Quellenstand" in transcribe.field(fm, "notiz")
    assert source.read_bytes() == before
    assert not path.exists()


@pytest.mark.parametrize("duration,expected_code", [(1000, 0), (4, 1)])
def test_cached_audio_duration_controls_atomic_note_update(tmp_path, monkeypatch, duration, expected_code):
    monkeypatch.setattr(transcribe, "ROOT", tmp_path)
    monkeypatch.setattr(transcribe, "CACHE", tmp_path / "cache")
    monkeypatch.setattr(transcribe, "configure_cuda", lambda: [])
    note = tmp_path / "original.md"
    original = example()
    note.write_text(original, encoding="utf-8")
    monkeypatch.setattr(transcribe, "find_notes", lambda _: (note, None))
    audio = tmp_path / "audio.mp4"
    audio.write_bytes(b"bereits decodierte und gecachte Tonspur")
    directory = transcribe.CACHE / "2EoNRuFJfBo"
    directory.mkdir(parents=True)
    cached = result() | dict(audio_duration=duration, elapsed_seconds=2,
                             audio_sha256=hashlib.sha256(audio.read_bytes()).hexdigest())
    (directory / "large-v3-transcript.json").write_text(json.dumps(cached), encoding="utf-8")
    (directory / "metadata.json").write_text('{"duration": 1000}', encoding="utf-8")
    code = transcribe.main(["2EoNRuFJfBo", "--audio", str(audio)])
    assert code == expected_code
    if expected_code:
        assert note.read_text(encoding="utf-8") == original
        assert not (directory / "before.md").exists()
    else:
        assert transcribe.has_transcript(note.read_text(encoding="utf-8"))
        assert (directory / "before.md").read_text(encoding="utf-8") == original
