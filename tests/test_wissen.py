"""Integrationstests für Herkunft, Suchbarkeit und ehrliche Analyseabdeckung."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location("wissen", Path(__file__).resolve().parents[1] / "70_Scripts/wissen.py")
wissen = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(wissen)


class WissenTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.init_repo(self.root)
        self.write(".gitignore", ".wissen/\nexternal_repos/\n.env*\n00_Inbox/Quellen/URL/mirrored/\n")
        self.write("00_Inbox/Quellen/URL/mirrored/lexikon.md", "# Lexikon\n\nMirroredKnowledgeRecord trotz Gitignore.\n")
        self.write("80_Knowledge/Sources/prompt-source.md", "---\nurl: https://example.org/original\nrohquelle: 00_Inbox/Quellen/X/original.md\n---\n# Ursprung\n\nWissensherkunft und Fallback.\n")
        self.write("00_Inbox/Quellen/X/original.md", "# Original\n\nFactory Originaltext.\n")
        self.write("80_Knowledge/Patterns/pattern.md", "# Muster\n\nSicherer Fallback mit Prüfer.\n")
        self.external = self.root / "external_repos/example/tool"
        self.external.mkdir(parents=True)
        self.init_repo(self.external)
        self.write("external_repos/example/tool/skills/review/SKILL.md", "---\nname: review\n---\n# Review\n\nWissensherkunft extern mit Prüfer.\n")
        self.write("external_repos/example/tool/prompts/review.json", '{"task":"JsonPromptFinder"}\n')
        self.write("external_repos/example/tool/src/main.py", "print('NICHT_AUSFUEHREN')\n")
        self.write("external_repos/example/tool/.env", "TESTWERT_NICHT_LESEN=example\n")
        self.commit(self.external)
        self.commit(self.root)

    def init_repo(self, path):
        for args in (("init", "-q"), ("config", "user.email", "test@example.invalid"), ("config", "user.name", "Wissen Test")):
            self.run_git(path, *args)

    def run_git(self, path, *args):
        subprocess.run(["git", "-C", str(path), *args], check=True, capture_output=True)

    def commit(self, path):
        self.run_git(path, "add", ".")
        self.run_git(path, "-c", "core.hooksPath=", "commit", "-qm", "Testbestand")

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return target

    def build(self, **kwargs):
        return wissen.build_index(self.root, self.root / ".wissen", **kwargs)

    def test_search_crosses_corpora_and_preserves_provenance(self):
        status = self.build()
        self.assertEqual(len(status["repositories"]), 2)
        with wissen.connect(self.root / ".wissen/index.sqlite") as db:
            hits = wissen.search(db, "Wissensherkunft")
            self.assertEqual({h["repo"] for h in hits}, {"company-os", "example/tool"})
            source = next(h for h in hits if h["repo"] == "company-os")
            self.assertEqual(source["kind"], "source")
            self.assertEqual(wissen.kind_of("80_Knowledge/Patterns/Prompting.md", False), "pattern")
            self.assertEqual(wissen.kind_of("00_Inbox/Quellen/X/prompt.md", False), "rohquelle")
            self.assertEqual(source["url"], "https://example.org/original")
            self.assertEqual(source["raw_source"], "00_Inbox/Quellen/X/original.md")
            self.assertEqual(len(source["sha256"]), 64)
            self.assertEqual(len(source["head"]), 40)
            self.assertGreaterEqual(source["start"], 1)
            self.assertEqual(len(wissen.search(db, "Wissensherkunft", repo="example/tool", kind="skill")), 1)
            self.assertEqual(len(wissen.search(db, "JsonPromptFinder", repo="example/tool")), 1)
            self.assertEqual(len(wissen.search(db, "MirroredKnowledgeRecord", kind="rohquelle")), 1)

    def test_changed_content_at_same_path_invalidates_snapshot(self):
        first = self.build()
        self.write("80_Knowledge/Patterns/pattern.md", "# Muster\n\nEin neuer Inhalt bei gleichem Titel.\n")
        second = self.build()
        self.assertNotEqual(first["snapshot"], second["snapshot"])
        third = self.build()
        self.assertEqual(second["snapshot"], third["snapshot"])

    def test_read_rejects_unknown_paths_and_changed_original(self):
        self.build()
        with wissen.connect(self.root / ".wissen/index.sqlite") as db:
            read = wissen.read_document(db, "80_Knowledge/Patterns/pattern.md", 3, 3)
            self.assertIn("Sicherer Fallback", read["text"])
            with self.assertRaises(RuntimeError):
                wissen.read_document(db, "../outside.md")
            self.write("80_Knowledge/Patterns/pattern.md", "# Muster\n\nGeändert.\n")
            with self.assertRaisesRegex(RuntimeError, "geändert"):
                wissen.read_document(db, "80_Knowledge/Patterns/pattern.md")

    def test_plan_covers_every_passage_once_without_claiming_analysis(self):
        status = self.build()
        output = self.root / ".wissen/plan.json"
        with wissen.connect(self.root / ".wissen/index.sqlite") as db:
            result = wissen.analysis_plan(db, output, budget=110)
            expected = {(r[0], int(r[1]), int(r[2])) for r in db.execute("SELECT path,start,end FROM passages")}
        plan = json.loads(output.read_text(encoding="utf-8"))
        actual = [(p["path"], p["start"], p["end"]) for batch in plan["batches"] for p in batch["passages"]]
        self.assertEqual(len(actual), len(set(actual)))
        self.assertEqual(set(actual), expected)
        self.assertEqual(len(actual), status["passages"])
        self.assertEqual(result["status"], "geplant-nicht-analysiert")
        self.assertTrue(all(b["status"] == "offen" for b in plan["batches"]))
        self.assertTrue(any(e["reason"] == "code-nur-inventar" for e in plan["excluded"]))
        with wissen.connect(self.root / ".wissen/index.sqlite") as db:
            with self.assertRaisesRegex(RuntimeError, "existiert"):
                wissen.analysis_plan(db, output)

    def test_secrets_binary_and_oversized_content_are_not_searchable(self):
        self.write("80_Knowledge/.env", "SENSITIVER_TESTINHALT=example\n")
        self.write("80_Knowledge/large.md", "GROESSE_TESTINHALT" * 100)
        self.write("80_Knowledge/binary.md", "BINAER_TESTINHALT\x00abc")
        self.write("80_Knowledge/invalid.md", "dummy").write_bytes(b"ungueltig\xff")
        status = self.build(max_bytes=1000)
        self.assertIn("vertraulicher-dateityp", status["exclusions"])
        self.assertIn("ueber-groessenlimit", status["exclusions"])
        self.assertIn("binaerinhalt", status["exclusions"])
        self.assertIn("kein-utf8", status["exclusions"])
        with wissen.connect(self.root / ".wissen/index.sqlite") as db:
            self.assertEqual(wissen.search(db, "SENSITIVER_TESTINHALT GROESSE_TESTINHALT BINAER_TESTINHALT"), [])
            self.assertEqual(wissen.search(db, '\" OR NEAR(a b) **'), [])

    def test_sections_preserve_all_lines_even_with_fences_and_long_line(self):
        text = "---\ntitle: Beispiel\n---\n# Eins\na\n```md\n# kein Titel\n```\n" + "x" * 100 + "\n## Zwei\nz\n"
        parts = wissen.sections(text, max_chars=30)
        self.assertEqual("".join(p[3] for p in parts), text)
        expected_start = 1
        for _, start, end, body in parts:
            self.assertEqual(start, expected_start)
            self.assertEqual(end - start + 1, len(body.splitlines()))
            expected_start = end + 1

    def test_missing_external_git_snapshot_is_reported(self):
        empty = self.root / "external_repos/example/empty"
        empty.mkdir()
        self.init_repo(empty)
        status = self.build()
        self.assertEqual(len(status["repository_errors"]), 1)
        self.assertIn("example/empty", status["repository_errors"][0])

    def test_analysis_check_rejects_gaps_duplicates_and_changed_sources(self):
        self.build()
        plan_path = self.root / ".wissen/plan.json"
        result_path = self.root / ".wissen/results.jsonl"
        with wissen.connect(self.root / ".wissen/index.sqlite") as db:
            wissen.analysis_plan(db, plan_path)
            plan = json.loads(plan_path.read_text(encoding="utf-8"))
            rows = [dict(p, status="analysiert", beurteilung="Testdatensatz für die formale Abdeckungsprüfung.") for b in plan["batches"] for p in b["passages"]]
            def save(entries):
                result_path.write_text("\n".join(json.dumps(r) for r in entries), encoding="utf-8")
            save(rows[:-1])
            self.assertFalse(wissen.analysis_check(db, plan_path, result_path)["complete"])
            save([*rows, rows[0]])
            self.assertFalse(wissen.analysis_check(db, plan_path, result_path)["complete"])
            save(rows)
            self.assertTrue(wissen.analysis_check(db, plan_path, result_path)["complete"])
            self.write("80_Knowledge/Patterns/pattern.md", "# Muster\n\nGeändert nach dem Snapshot.\n")
            changed = wissen.analysis_check(db, plan_path, result_path)
            self.assertFalse(changed["complete"])
            self.assertIn("80_Knowledge/Patterns/pattern.md", changed["changed_inputs"])
            plan["batches"][0]["passages"].pop()
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "nicht genau einmal"):
                wissen.analysis_check(db, plan_path, result_path)


if __name__ == "__main__":
    unittest.main()
