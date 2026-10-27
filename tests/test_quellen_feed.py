"""Datenherkunft, Dateigrenzen, Duplikate und Video-Range-Anfragen des Feeds."""
from functools import partial
from http.server import ThreadingHTTPServer
import importlib.util
import json
from pathlib import Path
import sys
from threading import Thread
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from unittest.mock import patch

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "70_Scripts"))
spec = importlib.util.spec_from_file_location("quellen_feed", ROOT / "70_Scripts/build_quellen_feed.py")
feed = importlib.util.module_from_spec(spec)
spec.loader.exec_module(feed)
from quellen_feed.avatars import avatar_from_page, local_author_images
from quellen_feed.translations import TranslationCatalog, foreign_script


def note(path, meta, body):
    import yaml
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + yaml.safe_dump(meta, allow_unicode=True) + "---\n\n" + body, encoding="utf-8")


def test_section_keeps_subheadings_and_stops_before_next_section():
    body = "## Transkript (Ausschnitt)\nText\n### Segment\nMehr\n## Lokales Video\nDatei"
    assert feed.section(body, "Transkript") == "Text\n### Segment\nMehr"


def test_source_excerpt_uses_existing_key_points_with_qualifications():
    body = "# Titel\n\nEinleitung.\n\n## Kernaussagen\n\n- Nur ein Selbstbericht, keine Wirkungsmessung.\n- Zweiter Punkt mit\n  Fortsetzung.\n- Dritter Punkt.\n- Vierter Punkt.\n\n## Einordnung\nKontext."
    excerpt, label = feed.source_excerpt(body)
    assert label == "Kernaussagen"
    assert "keine Wirkungsmessung" in excerpt and "Fortsetzung" in excerpt
    assert "Vierter" not in excerpt and "Einordnung" not in excerpt
    assert feed.source_excerpt("# Titel\n\nVorhandener Einstieg.\n\nWeiterer Absatz.") == ("Vorhandener Einstieg.", "Aus der Aufarbeitung")
    assert feed.source_excerpt("## Kernaussagen\n- [[Pattern-Datei]]: Autor behauptet einen Vorteil, ohne Messung.\n- Zweite Aussage. → [[Anderes-Pattern]]")[0] == "- Autor behauptet einen Vorteil, ohne Messung.\n- Zweite Aussage."


def test_confirmed_author_aliases_preserve_cached_avatar_and_original_profile(tmp_path):
    from PIL import Image
    aliases = tmp_path / "70_Scripts/quellen_dashboard/autoren.yaml"
    aliases.parent.mkdir(parents=True)
    aliases.write_text('boris-cherny:\n  name: Boris Cherny\n  aliases: ["X:bcherny", "X:boris cherny (@bcherny)"]\n', encoding="utf-8")
    raw = tmp_path / "00_Inbox/Quellen/X"
    for index, author in enumerate(["@bcherny", "Boris Cherny (@bcherny)"], 1):
        note(raw / f"{index}.md", {"url": f"https://x.com/bcherny/status/{index}", "autor": author, "datum": "2026-10-22", "erfasst": "2026-10-25", "status": "neu", "quelle": "x"}, "# Post\n\n## Post-Text\nOriginal text.")
    cache = tmp_path / "feed/avatars"
    (cache / "images").mkdir(parents=True)
    Image.new("RGB", (10, 10)).save(cache / "images/boris.jpg")
    (cache / "manifest.json").write_text(json.dumps({"authors": {"X:bcherny": {"image": "images/boris.jpg", "source": "https://x.com/bcherny"}}}), encoding="utf-8")
    themes = tmp_path / "80_Knowledge/Themen"
    themes.mkdir(parents=True)
    (themes / "themen.yaml").write_text("cluster: {}\n")
    (themes / "zuordnung.yaml").write_text("quellen: {}\n")
    out = tmp_path / "out"
    feed.build(tmp_path, out)
    index = json.loads((out / "index.json").read_text(encoding="utf-8"))
    assert index["author_aliases"]["X:bcherny"] == "boris-cherny"
    assert index["author_images"]["boris-cherny"].startswith("media/")
    assert len(index["authors"]) == 1
    assert all(e["authors"] == ["boris-cherny"] and e["profile_url"] == "https://x.com/bcherny" for e in index["entries"])


@pytest.mark.parametrize("language,first,second,third", [
    ("fr", "Bonjour, premier message.", "Suite française avec une précision.", "Encore une nouvelle précision."),
    ("es", "Hola, primer mensaje.", "Continuación española con una aclaración.", "Otra aclaración nueva."),
])
@pytest.mark.parametrize("change", ["missing", "changed", "added"])
def test_translation_rejects_uncovered_latin_script_thread_content(tmp_path, language, first, second, third, change):
    raw = tmp_path / "00_Inbox/Quellen/X/post.md"
    segments = [{"original": first, "translated": "Erster Beitrag."}]
    if change != "missing":
        segments.append({"original": second, "translated": "Zweiter Beitrag."})
    current_second = second + " Aktualisiert." if change == "changed" else second
    body = f"## Post-Text\n\n{first}\n\n## Thread\n\n### 1/2\n\n{first}\n\n### 2/2\n\n{current_second}"
    if change == "added":
        body += f"\n\n### 3/3\n\n{third}"
    catalog = tmp_path / "feed/translations/x.json"
    catalog.parent.mkdir(parents=True)
    catalog.write_text(json.dumps({"version": 1, "notes": {raw.relative_to(tmp_path).as_posix(): {
        "source_language": language, "target_language": "de", "segments": segments,
    }}}), encoding="utf-8")
    translations = TranslationCatalog(tmp_path)
    with pytest.raises(ValueError, match="Übersetzung"):
        translations.apply(raw, {"sprache": language}, body)
    assert not translations.translated


def test_translation_requires_exact_content_and_rejects_stale_catalog_segments(tmp_path):
    raw = tmp_path / "00_Inbox/Quellen/X/post.md"
    first, second = "Bonjour, premier message.", "Suite française complète."
    catalog = tmp_path / "feed/translations/x.json"
    catalog.parent.mkdir(parents=True)
    record = {"source_language": "fr", "target_language": "de", "segments": [
        {"original": first, "translated": "Erster Beitrag."},
        {"original": second, "translated": "Vollständige Fortsetzung."},
    ]}
    key = raw.relative_to(tmp_path).as_posix()
    catalog.write_text(json.dumps({"version": 1, "notes": {key: record}}), encoding="utf-8")
    body = f"## Post-Text\n\n{first}\n\n## Thread\n\n### 1/2\n\n{first}\n\n### 2/2\n\n{second}"
    result, info = TranslationCatalog(tmp_path).apply(raw, {"sprache": "fr"}, body)
    assert "Vollständige Fortsetzung." in result and first not in result and second not in result
    assert info["language"] == "de"
    record["segments"].append({"original": "Ancienne phrase supprimée.", "translated": "Entfernter Satz."})
    catalog.write_text(json.dumps({"version": 1, "notes": {key: record}}), encoding="utf-8")
    with pytest.raises(ValueError, match="Übersetzung"):
        TranslationCatalog(tmp_path).apply(raw, {"sprache": "fr"}, body)


@pytest.mark.parametrize("original,unchanged", [
    ("Bonjour", []),
    ("Bonjour, premier message.", [{"original": "Technical clarification.", "language": "fr"}]),
])
def test_translation_rejects_partial_matches_and_unapproved_passthrough(tmp_path, original, unchanged):
    raw = tmp_path / "00_Inbox/Quellen/X/post.md"
    catalog = tmp_path / "feed/translations/x.json"
    catalog.parent.mkdir(parents=True)
    catalog.write_text(json.dumps({"version": 1, "notes": {raw.relative_to(tmp_path).as_posix(): {
        "source_language": "fr", "target_language": "de",
        "segments": [{"original": original, "translated": "Erster Beitrag."}],
        "unchanged_segments": unchanged,
    }}}), encoding="utf-8")
    with pytest.raises(ValueError, match="Übersetzung|Freigabe"):
        TranslationCatalog(tmp_path).apply(raw, {"sprache": "fr"}, "## Post-Text\n\nBonjour, premier message.")


def test_translation_preserves_post_headings_neutral_links_and_line_endings(tmp_path):
    raw = tmp_path / "00_Inbox/Quellen/X/post.md"
    catalog = tmp_path / "feed/translations/x.json"
    catalog.parent.mkdir(parents=True)
    original = "Bonjour.\n\n## Ground rules\nVérifier chaque modification."
    translated = "Guten Tag.\n\n## Ground rules\nJede Änderung prüfen."
    catalog.write_text(json.dumps({"version": 1, "notes": {raw.relative_to(tmp_path).as_posix(): {
        "source_language": "fr", "target_language": "de",
        "segments": [{"original": original, "translated": translated}],
    }}}), encoding="utf-8")
    body = f"## Post-Text\n\n{original}\n\n## Thread\n\n### 1/2\n\n{original}\n\n### 2/2\n\nhttps://example.com/bonjour"
    result, info = TranslationCatalog(tmp_path).apply(raw, {"sprache": "fr"}, body.replace("\n", "\r\n"))
    assert result.count(translated) == 2
    assert "https://example.com/bonjour" in result
    assert info["language"] == "de"


def test_translated_x_content_replaces_original_on_every_feed_surface(tmp_path):
    raw = tmp_path / "00_Inbox/Quellen/X/post.md"
    original = "最近のワークフロー：まず仕様を確認する。\n\n/grill-with-docs https://example.com/spec"
    translated = "Mein aktueller Workflow: zuerst die Spezifikation klären.\n\n/grill-with-docs https://example.com/spec"
    body = f"# Autor (@author)\n\n## Post-Text\n{original}\n\n## Thread\n### 1/2\n{original}\n### 2/2\nTechnical clarification."
    note(raw, {"url": "https://x.com/author/status/123456", "autor": "@author", "datum": "2026-10-22", "erfasst": "2026-10-25", "status": "neu", "quelle": "x", "sprache": "ja", "thread_posts": 2}, body)
    before = raw.read_bytes()
    catalog = tmp_path / "feed/translations/x.json"
    catalog.parent.mkdir(parents=True)
    catalog.write_text(json.dumps({"version": 1, "notes": {raw.relative_to(tmp_path).as_posix(): {"source_language": "ja", "target_language": "de", "segments": [{"original": original, "translated": translated}], "unchanged_segments": [{"original": "Technical clarification.", "language": "en"}]}}}, ensure_ascii=False), encoding="utf-8")
    themes = tmp_path / "80_Knowledge/Themen"
    themes.mkdir(parents=True)
    (themes / "themen.yaml").write_text("cluster: {}\n")
    (themes / "zuordnung.yaml").write_text("quellen: {}\n")
    out = tmp_path / "out"
    result = feed.build(tmp_path, out)
    entry = json.loads((out / "index.json").read_text(encoding="utf-8"))["entries"][0]
    detail = json.loads((out / "data" / f"{entry['id']}.json").read_text(encoding="utf-8"))
    assert result["translated"] == 1
    assert entry["translated"] and entry["display_language"] == "de"
    assert entry["original_label"] == "Deutsche Übersetzung des Originaltexts"
    assert "Japanisch → Deutsch" in entry["translation_notice"]
    assert "zuerst die Spezifikation klären" in entry["search"]
    for field in (entry["preview_html"], detail["original_html"], detail["thread_html"], detail["archive_html"]):
        assert "zuerst die Spezifikation klären" in field
        assert "https://example.com/spec" in field
        assert "/grill-with-docs" in field
        assert "最近" not in field
    assert "Technical clarification." in detail["thread_html"]
    assert raw.read_bytes() == before
    # Geänderte Quelltexte dürfen keine veraltete Übersetzung erhalten.
    note(raw, {"url": "https://x.com/author/status/123456", "autor": "@author", "datum": "2026-10-22", "quelle": "x"}, "# Autor\n\n## Post-Text\n別の内容で翻訳を更新する必要があります。")
    previous_index = (out / "index.json").read_bytes()
    with pytest.raises(ValueError, match="X-Übersetzung fehlt oder passt nicht mehr"):
        feed.build(tmp_path, out)
    assert (out / "index.json").read_bytes() == previous_index


def test_language_metadata_catches_latin_languages_without_new_dependencies(tmp_path):
    catalog = TranslationCatalog(tmp_path)
    path = tmp_path / "00_Inbox/Quellen/X/post.md"
    with pytest.raises(ValueError, match="X-Übersetzung fehlt"):
        catalog.apply(path, {"sprache": "fr"}, "Voici une méthode pour vérifier les changements.")
    with pytest.raises(ValueError, match="X-Übersetzung fehlt"):
        catalog.apply(path, {"inhalt_sprachen": ["en", "es"]}, "English root with a Spanish continuation.")
    for lang, text in [("de", "Änderungen vor dem Commit prüfen."), ("en", "Review changes before committing.")]:
        assert catalog.apply(path, {"sprache": lang}, text) == (text, {})
    assert not foreign_script("𝗪𝗿𝗶𝘁𝗲 𝘀𝗶𝗺𝗽𝗹𝗲 𝗰𝗼𝗱𝗲")


def test_knowledge_connections_link_to_their_assigned_topic(tmp_path):
    source = tmp_path / "80_Knowledge/Sources/source.md"
    assets = feed.Assets(tmp_path)
    rendered = feed.render_text("[[Review-Pattern|Review]] und [[Unbekannt]]", source, assets, {}, {"Review-Pattern":"verifikation"})
    assert 'href="?topic=verifikation"' in rendered
    assert 'data-topic-link="verifikation"' in rendered
    assert '>Review</a>' in rendered
    assert '[[Unbekannt]]' not in rendered


def test_assets_cannot_escape_archive_even_with_encoding(tmp_path):
    source = tmp_path / "00_Inbox/Quellen/X/post.md"
    source.parent.mkdir(parents=True)
    (tmp_path / "secret.txt").write_text("privat")
    assets = feed.Assets(tmp_path)
    assert not assets.register("../../../secret.txt", source)
    assert not assets.register("%2E%2E/%2E%2E/%2E%2E/secret.txt", source)
    assert not assets.register("//example.com/secret.txt", source)
    assert not assets.files


def test_markdown_displays_html_without_executing_and_never_loads_remote_images(tmp_path):
    source = tmp_path / "00_Inbox/Quellen/X/post.md"
    source.parent.mkdir(parents=True)
    assets = feed.Assets(tmp_path)
    rendered = feed.render_text('<script>alert(1)</script>\n\n![Bild](https://remote.example/image.jpg)\n\n[Link](javascript:alert%281%29)', source, assets, {})
    assert "<script>" not in rendered
    assert "&lt;script&gt;" in rendered
    assert '<img src="https:' not in rendered
    assert 'href="javascript:' not in rendered
    assert not assets.files


def test_build_prefers_original_and_preserves_all_duplicate_versions(tmp_path):
    base = {"url": "https://x.com/person/status/123456", "autor": "@person", "datum": "2026-10-16", "erfasst": "2026-10-24", "status": "ignoriert", "typ": "tweet", "quelle": "x"}
    raw = tmp_path / "00_Inbox/Quellen/X"
    note(raw / "a-secondary.md", base, "# Übersetzter Titel\n\n> Sekundärquelle: importiert\n\nDeutsche Bearbeitung")
    note(raw / "b-original.md", {**base,"thread_posts":2}, "# Original\n\n## Post-Text\nReal original text\n\n## Thread\n### 1/2\nReal original text\n### 2/2\nReply")
    themes = tmp_path / "80_Knowledge/Themen"
    themes.mkdir(parents=True)
    (themes / "themen.yaml").write_text("cluster: {}\n")
    (themes / "zuordnung.yaml").write_text("quellen: {}\n")
    out = tmp_path / "output"
    result = feed.build(tmp_path, out)
    assert result["entries"] == 1
    index = json.loads((out / "index.json").read_text(encoding="utf-8"))
    row = index["entries"][0]
    assert row["versions"] == 2
    assert not row["secondary"]
    assert "Real original text" in row["preview_html"]
    assert row["statuses"] == ["ignoriert"]  # Kein heimlicher Statusfilter.
    assert "Reply" in row["search"]  # Gespräch und alternative Fassung sind ebenfalls durchsuchbar.
    assert "Deutsche Bearbeitung" in row["search"]
    detail = json.loads((out / "data" / f"{row['id']}.json").read_text(encoding="utf-8"))
    assert "Deutsche Bearbeitung" in detail["archive_html"]
    assert "Real original text" in detail["archive_html"]
    assert "Reply" in detail["thread_html"]
    assert str(tmp_path) not in json.dumps(index)


def test_file_pdf_and_internal_note_links_use_portable_paths(tmp_path):
    source = tmp_path / "00_Inbox/Quellen/PDF/report.md"
    source.parent.mkdir(parents=True)
    document = source.parent / "document.pdf"
    document.write_bytes(b"%PDF-test")
    assets = feed.Assets(tmp_path)
    assert assets.register(document.as_uri(), source).startswith("media/")
    rendered = feed.render_text("[Notiz](report.md)", source, assets, {source.relative_to(tmp_path).as_posix():"test-id"})
    assert 'href="#quelle=test-id"' in rendered


def test_static_export_copies_media_independently_of_archive(tmp_path):
    raw = tmp_path / "00_Inbox/Quellen/TikTok"
    (raw / "medien").mkdir(parents=True)
    video = raw / "medien/original.mp4"
    video.write_bytes(b"original-video")
    note(raw / "post.md", {"url":"https://www.tiktok.com/@person/video/123456789", "autor":"@person", "video_id":"123456789", "datum":"2026-10-19", "erfasst":"2026-10-24", "status":"verarbeitet"}, "# Beispiel\n\n## Caption\nOriginal-Caption\n\n## Lokales Video\n[Video](medien/original.mp4)")
    themes = tmp_path / "80_Knowledge/Themen"
    themes.mkdir(parents=True)
    (themes / "themen.yaml").write_text("cluster: {}\n")
    (themes / "zuordnung.yaml").write_text("quellen: {}\n")
    out = tmp_path / "export"
    result = feed.build(tmp_path, out, copy_media=True)
    assert result["copied"] == 1
    index = json.loads((out / "index.json").read_text(encoding="utf-8"))
    src = index["entries"][0]["media"][0]["src"]
    assert src.startswith("media/")
    assert (out / src).read_bytes() == video.read_bytes()
    (out / src).write_bytes(b"separate-copy")
    assert video.read_bytes() == b"original-video"


def test_verified_profile_picture_matches_handle_not_just_same_display_name(tmp_path):
    images = tmp_path / "docs/ki-quellen/images"
    images.mkdir(parents=True)
    (images / "person.jpg").write_bytes(b"test-picture")
    (images.parent / "profiles.json").write_text(json.dumps({"profiles":[{"id":"curated-person","name":"Person","sourceHeadings":[]}]}))
    (images.parent / "image-research.json").write_text(json.dumps({"curated-person":{"image":"images/person.jpg","imageSource":"https://x.com/correct_handle"}}))
    report = {"authors":{"X:correct_handle":"Person","X:another_handle":"Person"},"rows":{"raw":[
        {"authors":["X:correct_handle"],"url":"https://x.com/correct_handle/status/123","platforms":["X"]},
        {"authors":["X:another_handle"],"url":"https://x.com/another_handle/status/456","platforms":["X"]}]}}
    matched = local_author_images(tmp_path, report)
    assert matched["X:correct_handle"]["path"] == images / "person.jpg"
    assert "X:another_handle" not in matched


def test_x_quoted_author_cannot_be_mistaken_for_actual_poster():
    payload = {"user":{"screen_name":"quoted_person","profile_image_url_https":"https://pbs.twimg.com/wrong.jpg"}}
    with patch("quellen_feed.avatars.fetch", return_value=json.dumps(payload).encode()):
        with pytest.raises(ValueError, match="Post-Autor"):
            avatar_from_page("X", "https://x.com/poster/status/123", "Poster")


def test_youtube_avatar_comes_from_channel_owner_not_video_thumbnail():
    owner = {"thumbnail":{"thumbnails":[{"url":"https://yt3.ggpht.com/actual.jpg","width":176}]},"title":{"runs":[{"text":"Actual Author","navigationEndpoint":{"browseEndpoint":{"canonicalBaseUrl":"/@actual"}}}]}}
    payload = ('{"videoDetails":{"thumbnail":"video-cover.jpg"},"videoOwnerRenderer":' + json.dumps(owner) + '}').encode()
    with patch("quellen_feed.avatars.fetch", return_value=payload):
        url, source = avatar_from_page("YouTube", "https://youtube.com/watch?v=abcdefghi12", "Actual Author")
        assert url == "https://yt3.ggpht.com/actual.jpg"
        assert source == "https://www.youtube.com/@actual"
        with pytest.raises(ValueError, match="Videokanal"):
            avatar_from_page("YouTube", "https://youtube.com/watch?v=abcdefghi12", "Another Author")


def test_avatar_lookup_never_fetches_an_unrelated_or_local_url():
    with patch("quellen_feed.avatars.fetch") as fetch:
        for url in ("file:///private.txt", "http://127.0.0.1/", "https://unrelated.example/"):
            with pytest.raises(ValueError, match="Originalquelle"):
                avatar_from_page("YouTube", url, "Author")
        fetch.assert_not_called()


@pytest.fixture
def local_server(tmp_path):
    (tmp_path / "video.mp4").write_bytes(b"0123456789")
    server = ThreadingHTTPServer(("127.0.0.1",0), partial(feed.FeedHandler,directory=str(tmp_path)))
    thread = Thread(target=server.serve_forever,daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_port}"
    server.shutdown()
    server.server_close()
    thread.join()


@pytest.mark.parametrize("header,expected,range_value", [("bytes=2-5",b"2345","bytes 2-5/10"),("bytes=-3",b"789","bytes 7-9/10"),("bytes=7-",b"789","bytes 7-9/10")])
def test_video_ranges_support_seeking(local_server,header,expected,range_value):
    with urlopen(Request(local_server+"/video.mp4",headers={"Range":header})) as response:
        assert response.status == 206
        assert response.read() == expected
        assert response.headers["Content-Range"] == range_value
        assert response.headers["Accept-Ranges"] == "bytes"


def test_invalid_video_range_and_directory_listing(local_server):
    for path,headers,status in [("/video.mp4",{"Range":"bytes=20-30"},416),("/",{},404)]:
        with pytest.raises(HTTPError) as error:
            urlopen(Request(local_server+path,headers=headers))
        assert error.value.code == status
