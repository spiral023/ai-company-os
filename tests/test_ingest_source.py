"""Tests für 70_Scripts/ingest_source.py — reine Logik, kein Netzwerk."""

import importlib.util
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
