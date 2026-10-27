"""Belegfrische, Herkunftsfamilien und gesperrte Ableitungen des Piloten."""

from __future__ import annotations

from copy import deepcopy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location("wissens_pilot", Path(__file__).resolve().parents[1] / "70_Scripts/wissens_pilot.py")
pilot = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pilot)


class WissensPilotTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        evidence = []
        for number in range(1, 5):
            path = self.root / f"quellen/{number}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"# Quelle {number}\nBelegzeile\n", encoding="utf-8", newline="\n")
            evidence.append({"id": f"b0{number}", "pfad": path.relative_to(self.root).as_posix(), "von": 2, "bis": 2,
                             "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "bereich_sha256": hashlib.sha256(b"Belegzeile\n").hexdigest(),
                             "familie": "original-und-aufarbeitung" if number < 3 else f"familie-{number}"})
        claims = [{"id": f"c0{n}", "aussage": f"Aussage {n}", "grenze": "Keine Wirksamkeitsmessung", "nachweisart": "quellenaussage", "beleg_ids": [f"b0{n}"], "aus": []} for n in range(1, 5)]
        claims[0]["beleg_ids"] = ["b01", "b02"]
        claims[1].update(beleg_ids=[], aus=["c01"], nachweisart="eigene-ableitung")
        syntheses = [{"id": "s-review", "titel": "Review", "kurzfassung": "Reviewfrage", "pfad": "80_Knowledge/Vergleiche/Review.md", "tags": ["review"], "aussage_ids": ["c02"], "faehigkeit_ids": ["f-review"]},
                     {"id": "s-kontext", "titel": "Kontext", "kurzfassung": "Andere Frage", "pfad": "80_Knowledge/Vergleiche/Kontext.md", "tags": ["kontext"], "aussage_ids": ["c04"], "faehigkeit_ids": ["f-kontext"]}]
        cards = []
        for name, ids in (("review", ["c02", "c03"]), ("kontext", ["c04"])):
            item = {"id": f"f-{name}", "titel": name, "pfad": f"80_Knowledge/Faehigkeiten/{name}.md", "status": "kandidat", "zweck": "Pilot", "experiment": "Nicht ausgeführter Versuch", "aussage_ids": ids}
            item.update({key: ["Testvertrag"] for key in ("eingaben", "ausgaben", "voraussetzungen", "vorgehen", "pruefung", "stop", "laufzeit", "grenzen")})
            cards.append(item)
        self.data = {"schema_version": 1, "status": "semantischer-pilot", "stand": "2026-10-26", "belege": evidence, "aussagen": claims, "synthesen": syntheses, "faehigkeiten": cards,
                     "beziehungen": [{"id": "r01", "von": "c02", "nach": "c03", "typ": "steht-in-spannung", "begruendung": "Die Gegenposition muss mitgeliefert werden"}], "offene_fragen": ["Praktischer Nutzen offen"]}
        for synthesis in syntheses:
            path = self.root / synthesis["pfad"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Test\n" + " ".join(synthesis["aussage_ids"]), encoding="utf-8")
        pilot.cards(self.root, self.data)

    def test_context_adds_counterargument_and_deduplicates_origin_family(self):
        result = pilot.context(self.root, self.data, "Review")
        self.assertEqual(result["status"], "bereit")
        self.assertEqual({c["id"] for c in result["aussagen"]}, {"c01", "c02", "c03"})
        self.assertEqual([s["id"] for s in result["synthesen"]], ["s-review"])
        self.assertEqual(next(c for c in result["aussagen"] if c["id"] == "c02")["familienzahl"], 1)
        derived = next(c for c in result["aussagen"] if c["id"] == "c02")
        self.assertEqual(derived["beleg_ids"], [])
        self.assertEqual(set(derived["aufgeloeste_beleg_ids"]), {"b01", "b02"})
        self.assertEqual([c["id"] for c in result["faehigkeiten"]], ["f-review"])

    def test_changed_source_propagates_and_blocks_only_affected_context(self):
        (self.root / "quellen/2.md").write_text("# Quelle\nGeänderter Beleg\n", encoding="utf-8")
        report = pilot.audit(self.root, self.data)
        states = {r["id"]: r for r in report["aussagen"] + report["ableitungen"]}
        for key in ("c01", "c02", "s-review", "f-review"):
            self.assertEqual(states[key]["status"], "pruefbedarf")
        result = pilot.context(self.root, self.data, "Review")
        self.assertEqual(result["status"], "belege-pruefen")
        self.assertEqual(result["aussagen"], [])
        self.assertEqual(result["faehigkeiten"], [])
        self.assertEqual(result["beziehungen"], [])
        self.assertNotIn("kurzfassung", result["synthesen"][0])
        self.assertEqual(next(e for e in result["belege"] if e["id"] == "b02")["status"], "datei-geaendert")
        self.assertEqual(pilot.context(self.root, self.data, "Kontext")["status"], "bereit")

    def test_missing_evidence_is_distinct_from_modified_evidence(self):
        (self.root / "quellen/1.md").unlink()
        report = pilot.audit(self.root, self.data)
        self.assertEqual(next(e for e in report["belege"] if e["id"] == "b01")["status"], "nicht-aufloesbar")

    def test_cli_returns_parseable_blocked_bundle_with_nonzero_exit(self):
        registry = self.root / pilot.REGISTRY
        registry.parent.mkdir(parents=True, exist_ok=True)
        registry.write_text(json.dumps(self.data), encoding="utf-8")
        (self.root / "quellen/2.md").write_text("Geändert\n", encoding="utf-8")
        result = subprocess.run([sys.executable, str(Path(pilot.__file__)), "--root", str(self.root), "kontext", "Review"], capture_output=True, check=False)
        self.assertEqual(result.returncode, 1)
        data = json.loads(result.stdout.decode("utf-8"))
        self.assertEqual(data["status"], "belege-pruefen")
        self.assertEqual(data["aussagen"], [])
        self.assertEqual(data["beziehungen"], [])
        self.assertEqual(result.stderr, b"")

    def test_prerequisite_change_propagates_without_a_direct_derivation(self):
        self.data["beziehungen"].append({"id": "r02", "von": "c03", "nach": "c04", "typ": "setzt-voraus", "begruendung": "Notwendige Voraussetzung"})
        (self.root / "quellen/4.md").write_text("Geänderte Voraussetzung\n", encoding="utf-8")
        report = pilot.audit(self.root, self.data)
        self.assertEqual(next(c for c in report["aussagen"] if c["id"] == "c03")["status"], "pruefbedarf")
        self.assertEqual(pilot.context(self.root, self.data, "Review")["status"], "belege-pruefen")

    def test_cycles_across_derivation_and_prerequisite_edges_are_rejected(self):
        self.data["beziehungen"].append({"id": "r02", "von": "c01", "nach": "c02", "typ": "setzt-voraus", "begruendung": "Unzulässiger Rückweg"})
        with self.assertRaisesRegex(ValueError, "Zyklische"):
            pilot.validate(self.data, self.root)

    def test_repo_head_change_triggers_review_even_if_file_is_unchanged(self):
        item = self.data["belege"][0]
        item.update(repo="quellen", revision="a" * 40)
        with patch.object(pilot, "revision", return_value="a" * 40):
            self.assertEqual(pilot.audit(self.root, self.data)["status"], "aktuell")
        with patch.object(pilot, "revision", return_value="b" * 40):
            result = pilot.context(self.root, self.data, "Review")
        self.assertEqual(result["status"], "belege-pruefen")
        self.assertEqual(next(e for e in result["belege"] if e["id"] == "b01")["status"], "repo-revision-geaendert")

    def test_invalid_reference_duplicate_and_cycle_are_rejected(self):
        broken = deepcopy(self.data)
        broken["aussagen"][0]["aus"] = ["c02"]
        with self.assertRaisesRegex(ValueError, "Zyklische"):
            pilot.validate(broken, self.root)
        broken = deepcopy(self.data)
        broken["faehigkeiten"][0]["aussage_ids"] = ["erfunden"]
        with self.assertRaisesRegex(ValueError, "unbekannte Referenz"):
            pilot.validate(broken, self.root)
        broken = deepcopy(self.data)
        broken["belege"].append(broken["belege"][0])
        with self.assertRaisesRegex(ValueError, "doppelte ID"):
            pilot.validate(broken, self.root)

    def test_card_drift_is_detected_and_foreign_file_is_preserved(self):
        path = self.root / self.data["faehigkeiten"][0]["pfad"]
        path.write_text("Manuell gepflegte fremde Datei\n", encoding="utf-8")
        self.assertFalse(pilot.cards(self.root, self.data, check=True)["aktuell"])
        with self.assertRaisesRegex(ValueError, "Ansichten"):
            pilot.context(self.root, self.data, "Review")
        with self.assertRaisesRegex(ValueError, "überschrieben"):
            pilot.cards(self.root, self.data)
        self.assertEqual(path.read_text(encoding="utf-8"), "Manuell gepflegte fremde Datei\n")

    def test_pilot_cannot_activate_skills_or_write_views_outside_their_folder(self):
        broken = deepcopy(self.data)
        broken["faehigkeiten"][0]["status"] = "active"
        with self.assertRaisesRegex(ValueError, "nur Kandidaten"):
            pilot.validate(broken, self.root)
        broken = deepcopy(self.data)
        broken["faehigkeiten"][0]["pfad"] = "AGENTS.md"
        with self.assertRaisesRegex(ValueError, "außerhalb"):
            pilot.validate(broken, self.root)
        with self.assertRaises(ValueError):
            pilot.resolve(self.root, "../outside.md")

    def test_fallback_is_explicitly_limited_to_pilot_and_topic_is_checked(self):
        result = pilot.context(self.root, self.data, "Unbekanntes Spezialwort")
        self.assertEqual(result["auswahl"], "pilot-gesamtueberblick")
        self.assertIn("keine vollständige Analyse", result["scope"])
        self.assertFalse(result["vollanalyse"])
        self.assertFalse(result["wirksamkeit_gemessen"])
        self.assertEqual(len(result["synthesen"]), 2)
        with self.assertRaisesRegex(ValueError, "Unbekannte Synthese"):
            pilot.context(self.root, self.data, "Review", topic="erfunden")


if __name__ == "__main__":
    unittest.main()
