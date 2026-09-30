"""Tests für themen.py (Themencluster des Knowledge-Systems)."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_themen():
    """themen.py aus 70_Scripts laden."""
    spec = importlib.util.spec_from_file_location("themen", ROOT / "70_Scripts" / "themen.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("themen.py konnte nicht geladen werden")
    module = importlib.util.module_from_spec(spec)
    sys.modules["themen"] = module
    spec.loader.exec_module(module)
    return module


themen = load_themen()

TAXO = {
    "kontext": {"kern": ["context rot", "/compact"], "weit": ["session"]},
    "skills": {"kern": ["skill.md"], "weit": ["trigger", "test"]},
}


class BewertungTest(unittest.TestCase):
    def setUp(self) -> None:
        self.regeln = themen.kompiliere(TAXO)

    def test_kern_begriff_schlaegt_weite_treffer(self) -> None:
        text = "Context Rot entsteht in langen Sessions. Nutze /compact früh."
        rang = themen.rangliste(themen.bewerte(text, self.regeln))
        self.assertEqual(rang[0][0], "kontext")
        self.assertGreater(rang[0][1], rang[1][1])

    def test_treffer_beginnt_am_wortanfang(self) -> None:
        # "test" darf nicht in "latest" treffen, wohl aber in "Tests".
        scores = themen.bewerte("The latest release", self.regeln)
        self.assertEqual(scores["skills"][0], 0.0)
        scores = themen.bewerte("Tests laufen grün", self.regeln)
        self.assertGreater(scores["skills"][0], 0.0)

    def test_kern_treffer_stehen_vor_weiten_in_der_trefferliste(self) -> None:
        text = "trigger trigger trigger und SKILL.md"
        treffer = themen.bewerte(text, self.regeln)["skills"][1]
        self.assertEqual(treffer[0][0], "skill.md")


class HilfenTest(unittest.TestCase):
    def test_frontmatter_und_titel(self) -> None:
        text = "---\nurl: x\n---\n\n# Ein Titel\n\nErster Satz. Zweiter Satz.\n"
        self.assertEqual(themen.titel_von(text, "fallback"), "Ein Titel")
        self.assertEqual(themen.kernaussage(text), "Erster Satz.")

    def test_datum_aus_slug(self) -> None:
        self.assertEqual(themen.datum_von("2026-07-10-autor-thema"), "2026-07-10")
        self.assertEqual(themen.datum_von("Handoff-Doc"), "")

    def test_hub_dateiname(self) -> None:
        self.assertEqual(themen.dateiname_hub("Hooks, MCP & Erweiterungs-Ebenen"), "Thema-Hooks-MCP-Erweiterungs-Ebenen")


class RepoBestandTest(unittest.TestCase):
    def test_taxonomie_ist_konsistent(self) -> None:
        taxo = themen.lade_taxonomie()
        for cid, c in taxo.items():
            for feld in ("name", "beschreibung", "kern", "weit", "blog"):
                self.assertIn(feld, c, f"{cid}: Feld {feld} fehlt")
            for term in c["kern"] + c["weit"]:
                self.assertIsInstance(term, str, f"{cid}: Begriff {term!r} ist kein Text (YAML-Doppelpunkt quoten?)")
            for v in c.get("verwandt", []):
                self.assertIn(v, taxo, f"{cid}: verwandt verweist auf unbekanntes {v}")

    def test_alle_notizen_sind_zugeordnet(self) -> None:
        self.assertEqual(themen.main(["check"]), 0)


if __name__ == "__main__":
    unittest.main()
