"""Tests für 70_Scripts/ingest_source.py — reine Logik, kein Netzwerk."""

import importlib.util
import json
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "ingest_source", REPO / "70_Scripts" / "ingest_source.py"
)
ingest = importlib.util.module_from_spec(SPEC)
sys.modules["ingest_source"] = ingest
SPEC.loader.exec_module(ingest)


class TestDatum:
    def test_iso_bleibt(self):
        assert ingest.iso_datum("2026-07-28T10:00:00Z") == "2026-07-28"

    def test_pdf_format_ohne_trenner(self):
        # PyMuPDF liefert "D:YYYYMMDDHHmmSS" — ohne diese Behandlung fiel das
        # Datum still auf "heute" zurück und der Slug wurde falsch.
        assert ingest.iso_datum("D:20260728012555Z00'00'") == "2026-07-28"

    def test_deutsches_format(self):
        assert ingest.iso_datum("28.07.2026") == "2026-07-28"

    def test_unbrauchbar_faellt_auf_heute(self):
        assert ingest.iso_datum("völlig unklar") == ingest.heute()

    def test_ungueltiger_monat_faellt_auf_heute(self):
        assert ingest.iso_datum("D:20261399") == ingest.heute()

    def test_parse_datum_bleibt_leer_statt_heute(self):
        # Der Unterschied zu iso_datum: hier muss erkennbar bleiben, dass gar
        # kein Datum gefunden wurde — sonst wird der Abruftag zum vermeintlichen
        # Veröffentlichungsdatum.
        assert ingest.parse_datum("völlig unklar") == ""
        assert ingest.parse_datum(None) == ""

    def test_parse_datum_erkennt_die_gleichen_formate(self):
        assert ingest.parse_datum("2026-07-28T10:00:00Z") == "2026-07-28"
        assert ingest.parse_datum("Aug 14, 2026") == "2026-08-14"


class TestJsonLdDatum:
    """Viele Seiten führen das Datum nur im JSON-LD — dort muss es herkommen."""

    def test_iso_wert(self):
        html = (
            '<script type="application/ld+json">'
            '{"@type":"NewsletterIssue","datePublished":"2026-08-05T14:03:23+00:00"}'
            "</script>"
        )
        assert ingest.json_ld_datum(html) == "2026-08-05T14:03:23+00:00"

    def test_nicht_iso_wert_wird_durchgereicht(self):
        # claude.com schreibt "Aug 14, 2026"; das Normalisieren macht parse_datum.
        html = (
            '<script type="application/ld+json">'
            '{"@type":"BlogPosting","datePublished":"Aug 14, 2026"}'
            "</script>"
        )
        assert ingest.parse_datum(ingest.json_ld_datum(html)) == "2026-08-14"

    def test_verschachtelt_in_graph(self):
        html = (
            '<script type="application/ld+json">'
            '{"@graph":[{"@type":"WebSite"},{"@type":"Article","datePublished":"2026-03-09"}]}'
            "</script>"
        )
        assert ingest.json_ld_datum(html) == "2026-03-09"

    def test_kaputter_block_blockiert_den_naechsten_nicht(self):
        html = (
            '<script type="application/ld+json">{kein json</script>'
            '<script type="application/ld+json">{"datePublished":"2026-05-01"}</script>'
        )
        assert ingest.json_ld_datum(html) == "2026-05-01"

    def test_ohne_datum_leer(self):
        html = '<script type="application/ld+json">{"@type":"WebPage"}</script>'
        assert ingest.json_ld_datum(html) == ""

    def test_ohne_json_ld_leer(self):
        assert ingest.json_ld_datum("<html><body>Text</body></html>") == ""


class TestSlug:
    def test_umlaute_und_sonderzeichen(self):
        assert ingest.slugify("Modell & Effort: Größe zählt!") == "modell-effort-groesse-zaehlt"

    def test_laenge_begrenzt(self):
        assert len(ingest.slugify("a" * 200)) <= 60

    def test_leerer_wert(self):
        assert ingest.slugify("!!!") == "quelle"

    def test_pfad_traversal_wird_entschaerft(self):
        assert "/" not in ingest.slugify("../../etc/passwd")
        assert ".." not in ingest.slugify("../../etc/passwd")

    def test_domain_slug(self):
        assert ingest.domain_slug("https://www.anthropic.com/engineering/x") == "anthropic"

    def test_baue_slug_youtube_nutzt_kanal(self):
        q = ingest.Quelle(
            url="https://youtu.be/abc", typ="youtube", titel="Mein Video",
            text="", autor="Ada Lovelace", datum="2026-03-01",
        )
        assert ingest.baue_slug(q) == "2026-03-01-ada-lovelace-mein-video"

    def test_baue_slug_pdf_nutzt_pdf_marker(self):
        q = ingest.Quelle(url="file:///x.pdf", typ="pdf", titel="Report", text="", datum="2026-01-05")
        assert ingest.baue_slug(q) == "2026-01-05-pdf-report"


class TestTypErkennung:
    @pytest.mark.parametrize(
        "eingabe,erwartet",
        [
            ("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "youtube"),
            ("https://youtu.be/dQw4w9WgXcQ", "youtube"),
            ("https://example.com/paper.pdf", "pdf"),
            ("https://example.com/artikel", "url"),
        ],
    )
    def test_erkennung(self, eingabe, erwartet):
        assert ingest.erkenne_typ(eingabe) == erwartet

    def test_unbekannt_bricht_ab(self):
        with pytest.raises(SystemExit):
            ingest.erkenne_typ("weder url noch datei")

    @pytest.mark.parametrize(
        "typ,ordner",
        [("youtube", "YouTube"), ("url", "URL"), ("pdf", "PDF"), ("unbekannt", "Sonstige")],
    )
    def test_quelltyp_bestimmt_unterordner(self, tmp_path, monkeypatch, typ, ordner):
        monkeypatch.setattr(ingest, "INBOX", tmp_path)
        assert ingest.quelltyp_ordner(typ) == tmp_path / ordner

    def test_pdf_originaldateien_liegen_im_pdf_typordner(self, tmp_path, monkeypatch):
        monkeypatch.setattr(ingest, "INBOX", tmp_path)
        assert ingest.pdf_dateien_ordner() == tmp_path / "PDF" / "dateien"


class TestYoutubeId:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "https://youtu.be/dQw4w9WgXcQ",
            "https://www.youtube.com/shorts/dQw4w9WgXcQ",
            "https://www.youtube.com/embed/dQw4w9WgXcQ",
        ],
    )
    def test_varianten(self, url):
        assert ingest.youtube_id(url) == "dQw4w9WgXcQ"

    def test_ohne_id(self):
        with pytest.raises(SystemExit):
            ingest.youtube_id("https://www.youtube.com/")


class TestYoutubeAufbereitung:
    def test_transkript_wird_zu_absatz_ohne_zeitstempel(self):
        text = ingest.formatiere_transkript(
            ["Das ist z.B.", "ein vollständiger Satz.", "Noch ein Satz."],
            min_absatzlaenge=5,
        )
        assert text == "Das ist z.B. ein vollständiger Satz.\n\nNoch ein Satz."
        assert "**[" not in text

    def test_metadaten_enthalten_beschreibung_und_datum(self, monkeypatch):
        player = {
            "videoDetails": {
                "title": "Mein Video",
                "author": "Ada",
                "shortDescription": "Beschreibung mit Link: https://example.com",
            },
            "microformat": {
                "playerMicroformatRenderer": {"publishDate": "2026-07-30T10:41:23-07:00"}
            },
        }
        seite = f"<script>var ytInitialPlayerResponse = {json.dumps(player)};</script>"
        monkeypatch.setattr(ingest, "hole", lambda *_args, **_kwargs: seite.encode("utf-8"))

        assert ingest.youtube_metadaten("https://youtu.be/dQw4w9WgXcQ", "dQw4w9WgXcQ") == (
            "Mein Video",
            "Ada",
            "2026-07-30",
            "Beschreibung mit Link: https://example.com",
        )


class TestNormalisiereUrl:
    """Der Vergleichsschluessel muss die Identität einer Quelle treffen."""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.youtube.com/watch?v=gz0PBC2P9eg",
            "https://youtu.be/gz0PBC2P9eg?t=42",
            "https://www.youtube.com/shorts/gz0PBC2P9eg",
            "https://www.youtube.com/embed/gz0PBC2P9eg",
        ],
    )
    def test_youtube_varianten_fallen_zusammen(self, url):
        assert ingest.normalisiere_url(url) == "https://www.youtube.com/watch?v=gz0PBC2P9eg"

    def test_verschiedene_videos_bleiben_verschieden(self):
        # Der alte Code schnitt alles ab "?" weg. Damit normalisierte jedes
        # Video auf ".../watch" und ein neues galt als Dublette des ersten.
        a = ingest.normalisiere_url("https://www.youtube.com/watch?v=gz0PBC2P9eg")
        b = ingest.normalisiere_url("https://www.youtube.com/watch?v=AAAAAAAAAAA")
        assert a != b

    def test_tracking_faellt_weg_inhaltsparameter_bleibt(self):
        assert (
            ingest.normalisiere_url("https://example.com/x/?utm_source=rss&id=7&fbclid=z")
            == "https://example.com/x?id=7"
        )

    def test_www_und_schema_vereinheitlicht(self):
        assert ingest.normalisiere_url(
            "https://www.example.com/x?id=7"
        ) == ingest.normalisiere_url("https://example.com/x/?id=7")

    def test_parameterreihenfolge_egal(self):
        assert ingest.normalisiere_url("https://example.com/x?b=2&a=1") == ingest.normalisiere_url(
            "https://example.com/x?a=1&b=2"
        )

    def test_kurzparameter_nur_bei_x(self):
        # ?s=/?t= stammen vom Teilen-Dialog von X. Anderswo können es echte
        # Parameter sein, die zwei Quellen unterscheiden.
        assert (
            ingest.normalisiere_url("https://x.com/a/status/1?s=20&t=xy")
            == "https://x.com/a/status/1"
        )
        assert ingest.normalisiere_url("https://example.com/suche?s=agenten").endswith("?s=agenten")

    def test_lokaler_pfad_bleibt_unveraendert(self):
        assert ingest.normalisiere_url("C:/tmp/paper.pdf") == "C:/tmp/paper.pdf"


class TestEindeutigerSlug:
    """Zwei verschiedene Quellen dürfen sich nie gegenseitig überschreiben."""

    def test_kollision_bekommt_suffix(self, tmp_path, monkeypatch):
        monkeypatch.setattr(ingest, "INBOX", tmp_path)
        (tmp_path / "basis.md").write_text("---\nurl: https://a.example\n---\n", encoding="utf-8")
        assert ingest.eindeutiger_slug("basis", "https://b.example") == "basis-2"

    def test_gleiche_quelle_behaelt_slug(self, tmp_path, monkeypatch):
        monkeypatch.setattr(ingest, "INBOX", tmp_path)
        (tmp_path / "basis.md").write_text("---\nurl: https://a.example\n---\n", encoding="utf-8")
        assert ingest.eindeutiger_slug("basis", "https://a.example/") == "basis"

    def test_freier_slug_unveraendert(self, tmp_path, monkeypatch):
        monkeypatch.setattr(ingest, "INBOX", tmp_path)
        assert ingest.eindeutiger_slug("neu", "https://a.example") == "neu"


class TestQuellenErkennung:
    def test_verwaltungsdateien_zaehlen_nicht(self, tmp_path, monkeypatch):
        monkeypatch.setattr(ingest, "INBOX", tmp_path)
        for name in ("README.md", "VERARBEITUNGSPLAN.md", "echte-quelle.md"):
            (tmp_path / name).write_text("---\nurl: https://x\n---\n", encoding="utf-8")
        namen = [p.name for p in ingest.quellen_dateien()]
        assert namen == ["echte-quelle.md"]

    def test_dublette_ignoriert_query_und_slash(self, tmp_path, monkeypatch):
        monkeypatch.setattr(ingest, "INBOX", tmp_path)
        (tmp_path / "a.md").write_text(
            "---\nurl: https://example.com/x\n---\n", encoding="utf-8"
        )
        assert ingest.finde_dublette("https://example.com/x/?utm_source=rss") is not None
        assert ingest.finde_dublette("https://example.com/anders") is None

    def test_neues_youtube_video_ist_keine_dublette(self, tmp_path, monkeypatch):
        monkeypatch.setattr(ingest, "INBOX", tmp_path)
        (tmp_path / "video.md").write_text(
            "---\nurl: https://www.youtube.com/watch?v=gz0PBC2P9eg\n---\n", encoding="utf-8"
        )
        assert ingest.finde_dublette("https://www.youtube.com/watch?v=AAAAAAAAAAA") is None
        assert ingest.finde_dublette("https://youtu.be/gz0PBC2P9eg") is not None

    def test_quellen_werden_in_typordnern_rekursiv_gefunden(self, tmp_path, monkeypatch):
        monkeypatch.setattr(ingest, "INBOX", tmp_path)
        youtube = tmp_path / "YouTube"
        x = tmp_path / "X"
        youtube.mkdir()
        x.mkdir()
        (youtube / "video.md").write_text("---\nurl: https://youtu.be/x\n---\n", encoding="utf-8")
        (x / "post.md").write_text("---\nurl: https://x.com/a/status/1\n---\n", encoding="utf-8")
        assert [pfad.name for pfad in ingest.quellen_dateien()] == ["post.md", "video.md"]


class TestNotizAufbau:
    def test_frontmatter_pflichtfelder_und_escaping(self):
        q = ingest.Quelle(
            url="https://example.com/a",
            typ="url",
            titel='Titel mit "Anführung"',
            text="Inhalt",
            autor="Ada",
            datum="2026-02-01",
        )
        notiz = ingest.baue_notiz(q, "2026-02-01-example-titel")
        assert notiz.startswith("---\n")
        for feld in ("url:", "titel:", "autor:", "datum:", "erfasst:", "typ:", "status: neu"):
            assert f"\n{feld}" in f"\n{notiz}"
        # Anführungszeichen im Titel dürfen das YAML nicht zerlegen.
        assert '\\"Anführung\\"' in notiz

    def test_unbekanntes_datum_wird_als_unsicher_gekennzeichnet(self):
        q = ingest.Quelle(url="https://example.com/a", typ="url", titel="T", text="x", datum="")
        notiz = ingest.baue_notiz(q, "slug-x")
        # Der Abruftag steht im Feld, damit Slug und Sortierung funktionieren —
        # aber er ist als unsicher markiert.
        assert f"datum: {ingest.heute()}" in notiz
        assert "\ndatum_unsicher: true\n" in notiz

    def test_bekanntes_datum_ohne_unsicher_marke(self):
        q = ingest.Quelle(
            url="https://example.com/a", typ="url", titel="T", text="x", datum="2026-02-01"
        )
        notiz = ingest.baue_notiz(q, "slug-x")
        assert "datum: 2026-02-01" in notiz
        assert "datum_unsicher" not in notiz

    def test_medien_werden_relativ_referenziert(self):
        q = ingest.Quelle(
            url="https://example.com/a", typ="url", titel="T", text="x", datum="2026-02-01",
            medien=[ingest.Medium(url="https://example.com/b.jpg", alt="Chart", local="01-bild.jpg")],
        )
        notiz = ingest.baue_notiz(q, "slug-x")
        assert "![Chart](medien/slug-x/01-bild.jpg)" in notiz

    def test_fehlgeschlagenes_medium_behaelt_url(self):
        q = ingest.Quelle(
            url="https://example.com/a", typ="url", titel="T", text="x", datum="2026-02-01",
            medien=[ingest.Medium(url="https://example.com/b.jpg", error="HTTP 404")],
        )
        notiz = ingest.baue_notiz(q, "slug-x")
        assert "https://example.com/b.jpg" in notiz
        assert "HTTP 404" in notiz

    def test_youtube_notiz_enthaelt_beschreibung_vor_transkript(self):
        q = ingest.Quelle(
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            typ="youtube",
            titel="Video",
            text="Lesbarer Transkripttext.",
            datum="2026-07-30",
            beschreibung="Die Videobeschreibung.",
        )
        notiz = ingest.baue_notiz(q, "video")
        assert "## Videobeschreibung\n\nDie Videobeschreibung." in notiz
        assert notiz.index("## Videobeschreibung") < notiz.index("## Transkript")


class TestMedienSchreiben:
    def test_pdf_daten_erst_beim_schreiben_abgelegt(self, tmp_path):
        medien = [ingest.Medium(url="xref:1", local="s01-1.png", daten=b"BILD")]
        ziel = tmp_path / "medien" / "slug"
        ingest.schreibe_vorhandene(medien, ziel)
        assert (ziel / "s01-1.png").read_bytes() == b"BILD"
        # Nach dem Schreiben ist der Speicher freigegeben.
        assert medien[0].daten is None

    def test_ohne_daten_kein_ordner(self, tmp_path):
        ziel = tmp_path / "medien" / "leer"
        ingest.schreibe_vorhandene([ingest.Medium(url="https://x/a.jpg")], ziel)
        assert not ziel.exists()
