"""Tests für blog/build_blog.py — Freigabe-Schranke, Prüfungen, Navigation, Glossar."""

import importlib.util
import sys
from datetime import date, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("build_blog", REPO / "blog" / "build_blog.py")
bb = importlib.util.module_from_spec(SPEC)
sys.modules["build_blog"] = bb
SPEC.loader.exec_module(bb)

HEUTE = date(2026, 9, 29)
CFG = {
    "titel": "Testblog", "beschreibung": "b", "base_url": "https://x.test", "autor": "Anna",
    "fusszeile": "f", "ueber": "über",
    "kategorien": {"modelle": "Modelle", "tools": "Tools", "kurz": "Kurzmeldungen"},
}


def post(slug="a", status="freigegeben", datum=HEUTE, body="## Kurz gesagt\n\n- x\n", quellen=None, **kw):
    return {
        "titel": "T", "datum": datum, "kategorie": "modelle", "zusammenfassung": "z", "status": status,
        "quellen": quellen if quellen is not None else [{"titel": "Q"}], "body": body,
        "slug": slug, "datei": f"2026-09-29-{slug}.md", "geprueft_am": HEUTE, **kw,
    }


class TestFreigabe:
    def test_entwurf_ist_nicht_sichtbar(self):
        assert not bb.ist_sichtbar(post(status="entwurf"), HEUTE)

    def test_zukunft_ist_nicht_sichtbar(self):
        assert not bb.ist_sichtbar(post(datum=HEUTE + timedelta(days=1)), HEUTE)

    def test_freigegeben_heute_ist_sichtbar(self):
        assert bb.ist_sichtbar(post(), HEUTE)

    def test_link_auf_entwurf_ist_fehler(self):
        digest = post("digest", body="Siehe [x](post:einzel).")
        einzel = post("einzel", status="entwurf")
        fehler = bb.check_freigabe([digest, einzel], HEUTE)
        assert len(fehler) == 1 and "post:einzel" in fehler[0]

    def test_link_auf_sichtbaren_beitrag_ist_ok(self):
        digest = post("digest", body="Siehe [x](post:einzel).")
        assert bb.check_freigabe([digest, post("einzel")], HEUTE) == []

    def test_entwurf_darf_auf_entwurf_verlinken(self):
        a = post("a", status="entwurf", body="[x](post:b)")
        assert bb.check_freigabe([a, post("b", status="entwurf")], HEUTE) == []

    def test_doppelter_slug(self):
        fehler = bb.check_freigabe([post("a"), post("a")], HEUTE)
        assert any("doppelt" in f for f in fehler)


class TestQuellen:
    def test_ungenutzte_quelle_ist_fehler(self):
        p = post(quellen=[{"titel": "A"}, {"titel": "B"}], body="## Kurz gesagt\n\n- x\n\nText.{q:1}")
        fehler = bb.check_post(p, CFG)
        assert any("Quelle 2 wird nie zitiert" in f for f in fehler)
        assert not any("Quelle 1 wird nie" in f for f in fehler)

    def test_alle_zitiert_ist_ok(self):
        p = post(body="## Kurz gesagt\n\n- x\n\nText.{q:1}")
        assert bb.check_post(p, CFG) == []

    def test_unbekannte_source_notiz_faellt_im_check_auf(self):
        p = post(quellen=["gibt-es-nicht"], body="## Kurz gesagt\n\n- x\n\nText.{q:1}")
        assert any("Source-Notiz nicht gefunden" in f for f in bb.check_post(p, CFG))

    def test_quelle_ohne_titel(self):
        p = post(quellen=[{"url": "https://a"}], body="## Kurz gesagt\n\n- x\n\nText.{q:1}")
        assert any("ohne 'titel'" in f for f in bb.check_post(p, CFG))

    def test_zahl_ohne_beleg_ist_hinweis(self):
        p = post(body="## Kurz gesagt\n\n- 50 %\n\n## Text\n\nDer Preis sinkt um 20 %.\n\nBelegt: 5 Mio. Tokens.{q:1}")
        w = [x for x in bb.warn_post(p) if "Zahl ohne" in x]
        assert len(w) == 1 and "Der Preis" in w[0]  # Kurz gesagt und zitierter Absatz bleiben still


class TestPlatzhalter:
    def test_platzhalter_in_ueber(self):
        cfg = {**CFG, "ueber": "Kontakt: [hier ergänzen, bevor der Blog live geht]"}
        assert any("ueber" in f for f in bb.platzhalter(cfg, []))

    def test_sp23_platzhalter(self):
        assert bb.platzhalter({**CFG, "autor": "sp23"}, [])

    def test_sauber(self):
        cfg = {**CFG, "impressum": {"medieninhaber": "Anna", "wohnort": "Linz"}}
        assert bb.platzhalter(cfg, [post()]) == []

    def test_todo_im_beitrag(self):
        assert bb.platzhalter(CFG, [post(body="TODO: Zahl prüfen")])


class TestNavigation:
    def test_nur_aktive_kategorien(self):
        html = bb.page({**CFG, "_aktiv": {"modelle"}}, "T", "b", desc="d", path="/")
        assert '/k/modelle/' in html
        assert '/k/tools/' not in html and '/k/kurz/' not in html

    def test_kurz_kommt_zuletzt(self):
        html = bb.page({**CFG, "_aktiv": {"kurz", "modelle"}}, "T", "b", desc="d", path="/")
        assert html.index("/k/modelle/") < html.index("/k/kurz/")

    def test_ohne_angabe_alle(self):
        html = bb.page(CFG, "T", "b", desc="d", path="/")
        assert "/k/tools/" in html


class TestGlossar:
    def _gl(self):
        g = {"begriffe": [{"begriff": "Harness", "aliase": [], "text": "Ein Rahmen. Mehr."}]}
        for e in g["begriffe"]:
            e["slug"] = bb.slugify(e["begriff"])
            e["formen"] = [e["begriff"]]
            e["kurz"] = "Ein Rahmen."
        formen = bb.glossar_formen(g)
        return bb.glossar_regex(formen), formen

    def test_erste_nennung_verlinkt(self):
        out, gesehen = bb.link_terms("<p>Harness und Harness</p>", *self._gl())
        assert out.count('class="gl"') == 1 and gesehen == {"harness"}

    def test_ueberschrift_und_link_bleiben(self):
        out, _ = bb.link_terms('<h2>Harness</h2><a href="/">Harness</a><code>Harness</code>', *self._gl())
        assert 'class="gl"' not in out

    def test_plural(self):
        out, _ = bb.link_terms("<p>Harnessen</p>", *self._gl())
        assert 'class="gl"' in out


class TestHinweise:
    def test_unbekanntes_feld(self):
        w = bb.warn_post(post(aktualisert=HEUTE), HEUTE)
        assert any("aktualisert" in x for x in w)

    def test_pruefen_bis_ueberschritten(self):
        w = bb.warn_post(post(pruefen_bis=HEUTE - timedelta(days=1)), HEUTE)
        assert any("pruefen_bis" in x for x in w)

    def test_pruefen_bis_in_zukunft_ist_still(self):
        assert not any("pruefen_bis" in x for x in bb.warn_post(post(pruefen_bis=HEUTE + timedelta(days=5)), HEUTE))

    def test_box_zu_lang(self):
        body = "## Kurz gesagt\n\n" + "\n".join(f"- p{i}" for i in range(6)) + "\n"
        assert any("6 Stichpunkte" in x for x in bb.warn_post(post(body=body), HEUTE))


class TestFreigeben:
    def _setup(self, tmp_path, monkeypatch, status="entwurf", body="Text.", datum=HEUTE):
        monkeypatch.setattr(bb, "POSTS", tmp_path)
        f = tmp_path / "2026-09-29-a.md"
        f.write_text(f"---\ntitel: T\nstatus: {status}\nquellen:\n  - x\n---\n{body}\n", encoding="utf-8", newline="")
        return f, post("a", status=status, body=body, datum=datum)

    def test_setzt_status_und_datum(self, tmp_path, monkeypatch):
        f, p = self._setup(tmp_path, monkeypatch)
        ok, _ = bb.freigeben(p, [p], HEUTE)
        text = f.read_text(encoding="utf-8")
        assert ok and "status: freigegeben\ngeprueft_am: 2026-09-29\n" in text

    def test_zweimal_ersetzt_datum(self, tmp_path, monkeypatch):
        f, p = self._setup(tmp_path, monkeypatch)
        bb.freigeben(p, [p], HEUTE)
        ok, msg = bb.freigeben({**p, "status": "entwurf"}, [p], HEUTE + timedelta(days=1))
        assert ok and f.read_text(encoding="utf-8").count("geprueft_am") == 1

    def test_lehnt_platzhalter_ab(self, tmp_path, monkeypatch):
        f, p = self._setup(tmp_path, monkeypatch, body="TODO Zahl")
        ok, msg = bb.freigeben(p, [p], HEUTE)
        assert not ok and "status: entwurf" in f.read_text(encoding="utf-8")

    def test_lehnt_link_auf_entwurf_ab(self, tmp_path, monkeypatch):
        f, p = self._setup(tmp_path, monkeypatch, body="[x](post:b)")
        ok, msg = bb.freigeben(p, [p, post("b", status="entwurf")], HEUTE)
        assert not ok and "post:b" in msg

    def test_zukunftsdatum_wird_gemeldet(self, tmp_path, monkeypatch):
        f, p = self._setup(tmp_path, monkeypatch, datum=HEUTE + timedelta(days=3))
        ok, msg = bb.freigeben(p, [p], HEUTE)
        assert ok and "erscheint ab 02.10.2026" in msg

    def test_freigegeben_ohne_pruefdatum_ist_fehler(self):
        p = post(body="## Kurz gesagt\n\n- x\n\nT.{q:1}", geprueft_am=None)
        assert any("geprueft_am" in f for f in bb.check_post(p, CFG))
        assert not any("geprueft_am" in f for f in bb.check_post({**p, "geprueft_am": HEUTE}, CFG))

    def test_aktualisiert_vor_datum_ist_fehler(self):
        p = post(body="## Kurz gesagt\n\n- x\n\nT.{q:1}", aktualisiert=HEUTE - timedelta(days=1))
        assert any("aktualisiert" in f for f in bb.check_post(p, CFG))
        assert bb.check_post({**p, "aktualisiert": HEUTE}, CFG) == []

    def test_aktualisiert_ohne_gueltiges_datum_ist_fehler(self):
        p = post(body="## Kurz gesagt\n\n- x\n\nT.{q:1}", aktualisiert="5.10.2026")
        assert any("aktualisiert" in f for f in bb.check_post(p, CFG))


class TestImpressum:
    def test_ohne_impressum_blockiert(self):
        assert any("Impressum" in f for f in bb.platzhalter(CFG, []))

    def test_platzhalter_im_impressum(self):
        cfg = {**CFG, "impressum": {"medieninhaber": "A", "wohnort": "[hier ergänzen: Wohnort]"}}
        assert any("'impressum'" in f for f in bb.platzhalter(cfg, []))

    def test_vollstaendig_ist_ok(self):
        cfg = {**CFG, "impressum": {"medieninhaber": "A", "wohnort": "Linz"}}
        assert bb.platzhalter(cfg, []) == []

    def test_seite_und_fusszeile(self):
        imp = {"medieninhaber": "A", "wohnort": "Linz", "kontakt": "x@y.at"}
        assert "Linz" in bb.impressum_html(imp) and "§ 25 Mediengesetz" in bb.impressum_html(imp)
        assert '/impressum/' in bb.page({**CFG, "impressum": imp}, "T", "b", desc="d", path="/")


class TestOhneQuellen:
    def test_redaktion_braucht_keine_quellen(self):
        cfg = {**CFG, "kategorien": {**CFG["kategorien"], "redaktion": "Über"}, "ohne_quellen": ["redaktion"]}
        p = post(quellen=[], kategorie="redaktion")
        assert bb.check_post(p, cfg) == []
        assert bb.quellen_html(cfg, p) == ""

    def test_andere_kategorie_braucht_quellen(self):
        assert any("keine Quellen" in f for f in bb.check_post(post(quellen=[]), CFG))


def schreibe(pfad, slug, status="entwurf", body="## Kurz gesagt\n\n- a\n- b\n\n## Text\n\nEin Satz.{q:1}", extra=""):
    f = pfad / f"2026-09-29-{slug}.md"
    f.write_text(f"---\ntitel: T\ndatum: 2026-09-29\nkategorie: modelle\nzusammenfassung: z\nstatus: {status}\n{extra}"
                 f"quellen:\n  - titel: Q\n---\n{body}\n", encoding="utf-8", newline="")
    return f


def lade(pfad):
    return [bb.parse_post(f) for f in sorted(pfad.glob("*.md"))]


class TestAutoFreigeben:
    def test_gibt_sauberen_entwurf_sofort_frei(self, tmp_path, monkeypatch):
        monkeypatch.setattr(bb, "POSTS", tmp_path)
        f = schreibe(tmp_path, "a")
        posts = lade(tmp_path)
        meldungen = bb.auto_freigeben(posts, CFG, HEUTE)
        text = f.read_text(encoding="utf-8")
        assert "status: freigegeben" in text and "freigabe: automatisch" in text
        assert "datum: 2026-09-29" in text and "sofort sichtbar" in meldungen[0]
        assert bb.ist_sichtbar(bb.parse_post(f), HEUTE)

    def test_vergangenes_datum_wird_auf_heute_gesetzt(self, tmp_path, monkeypatch):
        monkeypatch.setattr(bb, "POSTS", tmp_path)
        f = schreibe(tmp_path, "a")
        bb.auto_freigeben(lade(tmp_path), CFG, HEUTE + timedelta(days=2))
        assert "datum: 2026-10-01" in f.read_text(encoding="utf-8")

    def test_hinweis_blockiert(self, tmp_path, monkeypatch):
        monkeypatch.setattr(bb, "POSTS", tmp_path)
        f = schreibe(tmp_path, "a", body="## Kurz gesagt\n\n- a\n- b\n\n## Text\n\nDas ist belegt.{q:1}")
        meldungen = bb.auto_freigeben(lade(tmp_path), CFG, HEUTE)
        assert "status: entwurf" in f.read_text(encoding="utf-8")
        assert any("übersprungen" in m and "Beleg-Meta" in m for m in meldungen)

    def test_zahl_ohne_beleg_blockiert(self, tmp_path, monkeypatch):
        monkeypatch.setattr(bb, "POSTS", tmp_path)
        f = schreibe(tmp_path, "a", body="## Kurz gesagt\n\n- a\n- b\n\n## Text\n\nKostet 20 % mehr.\n\nQuelle.{q:1}")
        bb.auto_freigeben(lade(tmp_path), CFG, HEUTE)
        assert "status: entwurf" in f.read_text(encoding="utf-8")

    def test_fehler_blockiert_nur_diesen_beitrag(self, tmp_path, monkeypatch):
        monkeypatch.setattr(bb, "POSTS", tmp_path)
        kaputt = schreibe(tmp_path, "kaputt", body="## Kurz gesagt\n\n- a\n- b\n\nOhne Zitat.")
        gut = schreibe(tmp_path, "gut")
        bb.auto_freigeben(lade(tmp_path), CFG, HEUTE)
        assert "status: entwurf" in kaputt.read_text(encoding="utf-8")
        assert "status: freigegeben" in gut.read_text(encoding="utf-8")

    def test_digest_folgt_seinen_einzelbeitraegen(self, tmp_path, monkeypatch):
        monkeypatch.setattr(bb, "POSTS", tmp_path)
        digest = schreibe(tmp_path, "a-digest", body="## Kurz gesagt\n\n- a\n- b\n\n## Text\n\nSiehe [x](post:einzel).{q:1}")
        einzel = schreibe(tmp_path, "einzel")
        bb.auto_freigeben(lade(tmp_path), CFG, HEUTE)
        assert "status: freigegeben" in digest.read_text(encoding="utf-8")
        assert "status: freigegeben" in einzel.read_text(encoding="utf-8")

    def test_digest_bleibt_liegen_wenn_einzelbeitrag_haengt(self, tmp_path, monkeypatch):
        monkeypatch.setattr(bb, "POSTS", tmp_path)
        digest = schreibe(tmp_path, "digest", body="## Kurz gesagt\n\n- a\n- b\n\n## Text\n\nSiehe [x](post:einzel).{q:1}")
        schreibe(tmp_path, "einzel", body="## Kurz gesagt\n\n- a\n- b\n\nOhne Zitat.")
        bb.auto_freigeben(lade(tmp_path), CFG, HEUTE)
        assert "status: entwurf" in digest.read_text(encoding="utf-8")

    def test_bereits_freigegebene_bleiben(self, tmp_path, monkeypatch):
        monkeypatch.setattr(bb, "POSTS", tmp_path)
        f = schreibe(tmp_path, "a", status="freigegeben", extra="geprueft_am: 2026-09-01\n")
        assert bb.auto_freigeben(lade(tmp_path), CFG, HEUTE) == []
        assert "freigabe:" not in f.read_text(encoding="utf-8")

    def test_link_auf_spaeter_datierten_beitrag_ist_fehler(self):
        a = post("a", body="[x](post:b)")
        b = post("b", datum=HEUTE + timedelta(days=1))
        assert bb.check_freigabe([a, b], HEUTE)


class TestBlogStil:
    def test_meta_wort_ist_hinweis(self):
        w = bb.warn_post(post(body="## Kurz gesagt\n\n- a\n- b\n\n## T\n\nDas ist unbelegt und belegt.{q:1}"), HEUTE)
        assert any("Beleg-Meta" in x for x in w)

    def test_sauberer_text_ohne_hinweis(self):
        w = bb.warn_post(post(body="## Kurz gesagt\n\n- a\n- b\n\n## T\n\nGPT-6 wird billiger.{q:1}"), HEUTE)
        assert w == []

    def test_quellenverweise_ausgeblendet(self):
        from markdown_it import MarkdownIt
        md = MarkdownIt("commonmark")
        p = post(body="Kostet 5 %.{q:1} Und mehr {q:1}.")
        assert "[1]" not in bb.render_body(md, p, zeige_q=False) and "{q:" not in bb.render_body(md, p, zeige_q=False)
        assert 'class="q"' in bb.render_body(md, p)


class TestFaktenSeite:
    REG = """# Fakten

**Stand:** 2026-09-29

## Lesehinweise

- Text

## Preise

| Datum | Gegenstand | Aussage | Einschränkung | Quelle |
|---|---|---|---|---|
| 2026-09-20 | Modell A | `$0.10`/`$0.50` pro 1M | - | [[quelle-a]] |
| 2026-09-22 | Modell B | 5 % mehr | Herstellerangabe | [[quelle-a]] [[quelle-b]] |
"""

    def test_register_wird_gelesen_und_neueste_zuerst_sortiert(self):
        fs = bb.fakten_seite
        reg = fs.parse_register(self.REG)
        assert reg["stand"] == date(2026, 9, 29)
        assert [a["titel"] for a in reg["abschnitte"]] == ["Preise"]
        assert [z["gegenstand"] for z in reg["abschnitte"][0]["zeilen"]] == ["Modell B", "Modell A"]
        assert reg["abschnitte"][0]["zeilen"][0]["quellen"] == ["quelle-a", "quelle-b"]

    def test_schreibweise_fuer_leser(self):
        fs = bb.fakten_seite
        assert fs.bereinigen("`$0.10`/`$13.04`") == "$0,10/$13,04"
        assert fs.bereinigen("Stand 2026-09-22") == "Stand 22.09.2026"

    def test_fehlende_quelle_und_interner_begriff_sind_fehler(self):
        fs = bb.fakten_seite
        reg = fs.parse_register(self.REG.replace("[[quelle-b]]", "[[fehlt]]").replace("Herstellerangabe", "laut Notiz"))
        fehler = fs.pruefen(reg, lambda q: q != "fehlt")
        assert any("Quelle nicht gefunden: fehlt" in f for f in fehler)
        assert any("interner Begriff" in f for f in fehler)

    def test_konfidenzintervall_ist_kein_interner_begriff(self):
        fs = bb.fakten_seite
        reg = fs.parse_register(self.REG.replace("Herstellerangabe", "Konfidenzintervalle überlappen"))
        assert fs.pruefen(reg, lambda q: True) == []

    def test_alter_stand_ergibt_hinweis(self):
        fs = bb.fakten_seite
        reg = fs.parse_register(self.REG)
        assert fs.hinweise(reg, date(2026, 10, 5)) == []
        assert fs.hinweise(reg, date(2026, 10, 20))

    def test_seite_zeigt_stand_datum_und_quellenliste(self):
        fs = bb.fakten_seite
        reg = fs.parse_register(self.REG)
        eintrag = lambda q: {"titel": f"Titel {q}", "autor": "Anna", "datum": "2026-09-01", "url": "https://x.test"}
        html = fs.render({"titel": "Modelle und Preise"}, reg, eintrag)
        assert "Stand 29.09.2026" in html and "22.09.2026" in html and "$0,10" in html
        assert 'id="q1"' in html and 'id="q2"' in html


class TestWebSub:
    def _md(self):
        return bb.MarkdownIt("commonmark", {"html": False}).enable(["table"])

    def test_feed_nennt_hub(self):
        xml = bb.feed_xml({**CFG, "websub_hub": "https://hub.test/"}, self._md(), [], "/feed.xml", "T")
        assert '<atom:link href="https://hub.test/" rel="hub"/>' in xml

    def test_feed_ohne_hub(self):
        assert 'rel="hub"' not in bb.feed_xml(CFG, self._md(), [], "/feed.xml", "T")

    def test_ping_meldet_jeden_feed(self, tmp_path):
        (tmp_path / "feed").mkdir()
        (tmp_path / "feed.xml").write_text("x", encoding="utf-8")
        (tmp_path / "feed" / "tools.xml").write_text("x", encoding="utf-8")
        gesendet = []
        ok, _ = bb.websub_ping({**CFG, "websub_hub": "https://hub.test/"}, tmp_path,
                               senden=lambda hub, daten: gesendet.append((hub, daten)) or 204)
        assert ok and len(gesendet) == 2
        assert b"hub.mode=publish" in gesendet[0][1]
        assert b"hub.url=https%3A%2F%2Fx.test%2Ffeed.xml" in gesendet[0][1]
        assert b"hub.url=https%3A%2F%2Fx.test%2Ffeed%2Ftools.xml" in gesendet[1][1]

    def test_ping_fehler_wird_gemeldet(self, tmp_path):
        (tmp_path / "feed.xml").write_text("x", encoding="utf-8")
        ok, meldungen = bb.websub_ping({**CFG, "websub_hub": "https://hub.test/"}, tmp_path,
                                       senden=lambda hub, daten: 500)
        assert not ok and "fehlgeschlagen" in meldungen[0]

    def test_ping_ohne_hub(self, tmp_path):
        ok, meldungen = bb.websub_ping(CFG, tmp_path)
        assert not ok and "websub_hub" in meldungen[0]
