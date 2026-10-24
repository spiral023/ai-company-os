"""Zählregeln, Verknüpfungen und Verlauf anhand kleiner, unabhängiger Bestände."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("quellen_statistik", ROOT / "70_Scripts/quellen_statistik.py")
stats = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stats)


class StatistikTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.save("80_Knowledge/Themen/themen.yaml", {"cluster": {"tests": {"name": "Tests"}}})
        self.save("80_Knowledge/Themen/zuordnung.yaml", {"quellen": {
            "aufarbeitung": {"haupt": "tests", "keywords": ["TDD", "tdd", "Code Review"]}}, "muster": {}})
        self.save("70_Scripts/quellen_dashboard/autoren.yaml", {"matt-pocock": {
            "name": "Matt Pocock", "aliases": ["X:mattpocockuk", "YouTube:matt pocock"]}})

    def save(self, path, data, body=""):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        if p.suffix == ".md":
            p.write_text("---\n" + yaml.safe_dump(data, allow_unicode=True) + "---\n# Titel\n" + body, encoding="utf-8")
        else:
            p.write_text(yaml.safe_dump(data), encoding="utf-8")

    def test_posts_deduplicated_list_links_and_keywords_count_once(self):
        a = "00_Inbox/Quellen/X/a.md"
        b = "00_Inbox/Quellen/X/b.md"
        s = "80_Knowledge/Sources/aufarbeitung.md"
        self.save(a, {"url": "https://x.com/mattpocockuk/status/123?s=20", "autor": "@MattPocockUK",
                      "status": "verarbeitet", "source_notiz": s, "erfasst": "2026-10-20"})
        self.save(b, {"url": "https://twitter.com/mattpocockuk/status/123", "status": "verarbeitet",
                      "source_notiz": s, "erfasst": "2026-10-21"})
        self.save(s, {"url": "https://x.com/mattpocockuk/status/123", "autor": "@mattpocockuk",
                      "rohquelle": [a, b], "erfasst": "2026-10-22", "typ": "tweet"})
        # Nested media/archives must never be counted as additional source files.
        self.save("00_Inbox/Quellen/X/medien/copy.md", {"url": "https://x.com/a/status/9"})
        report = stats.collect(self.root)
        self.assertEqual(report["counts"]["raw_files"], 2)
        self.assertEqual(report["counts"]["raw_unique"], 1)
        self.assertEqual(report["counts"]["sources_without_raw_link"], 0)
        row = report["rows"]["raw"][0]
        self.assertEqual(row["captured"], "2026-10-20")
        self.assertEqual(row["keywords"], ["code review", "tdd"])
        self.assertEqual(report["summary"]["raw"]["authors"], {"matt-pocock": 1})
        self.assertEqual(len(stats.select_rows(report, "raw", "matt-pocock", "Tests", "TDD")), 1)
        self.assertEqual(len(stats.select_rows(report, "raw", "mattpocockuk")), 1)
        self.assertEqual(len(stats.select_rows(report, "raw", keyword="missing")), 0)

    def test_missing_urls_do_not_merge_and_unknown_authors_remain_visible(self):
        for name in ("a", "b"):
            self.save(f"00_Inbox/Quellen/URL/{name}.md", {"url": "keine", "status": "ignoriert"})
        report = stats.collect(self.root)
        self.assertEqual(report["counts"]["raw_unique"], 2)
        self.assertEqual(report["summary"]["raw"]["authors"], {"unbekannt": 2})

    def test_canonical_urls_preserve_meaningful_query_parameters(self):
        key = lambda u: stats.canonical_id({"url": u}, "fallback")
        self.assertEqual(key("https://www.example.org/a/?utm_source=x#anchor"), key("https://example.org/a"))
        self.assertNotEqual(key("https://example.org/?id=1"), key("https://example.org/?id=2"))
        self.assertEqual(key("https://youtu.be/abc?t=10"), key("https://www.youtube.com/watch?v=abc"))
        self.assertEqual(key("https://youtube.com/shorts/abc"), key("https://www.youtube.com/watch?v=abc"))

    def test_no_fuzzy_author_merges_and_explicit_cross_platform_alias(self):
        aliases = {"matt": {"name": "Matt Pocock", "aliases": ["X:mattpocockuk", "YouTube:matt pocock"]}}
        self.assertEqual(stats.author_identity("@MattPocockUK", "X", aliases), stats.author_identity("Matt Pocock", "YouTube", aliases))
        self.assertNotEqual(stats.author_identity("alex", "X", aliases)[0], stats.author_identity("alex", "TikTok", aliases)[0])

    def test_snapshots_append_and_incompatible_rules_are_not_compared(self):
        report = stats.collect(self.root)
        folder = self.root / "snapshots"
        first = stats.write_snapshot(folder, report)
        original = first.read_bytes()
        report["counts"]["raw_files"] = 1
        stats.write_snapshot(folder, report)
        history, excluded = stats.load_history(folder, report)
        self.assertEqual(len(history), 2)
        self.assertFalse(excluded)
        self.assertEqual(first.read_bytes(), original)
        (folder / "broken.json").write_text("{", encoding="utf-8")
        report["rules_fingerprint"] = "new aliases"
        history, excluded = stats.load_history(folder, report)
        self.assertFalse(history)
        self.assertEqual(len(excluded), 3)

    def test_render_cannot_close_embedded_json_script(self):
        template = self.root / "70_Scripts/quellen_dashboard/index.html"
        template.write_text('<script type="application/json">__REPORT_JSON__</script>', encoding="utf-8")
        output = stats.render({"title": '</script><img src=x onerror="alert(1)">'}, self.root / "reports", self.root)
        self.assertEqual(output.count("</script>"), 1)
        decoded = json.loads(output.split('>', 1)[1].rsplit('</script>', 1)[0])
        self.assertIn("</script>", decoded["title"])

    def test_incomplete_snapshot_does_not_break_dashboard_history(self):
        report = stats.collect(self.root)
        folder = self.root / "snapshots"
        path = stats.write_snapshot(folder, report)
        broken = json.loads(path.read_text(encoding="utf-8"))
        del broken["counts"]["raw_unique"]
        path.write_text(json.dumps(broken), encoding="utf-8")
        history, excluded = stats.load_history(folder, report)
        self.assertFalse(history)
        self.assertEqual(len(excluded), 1)

    def test_existing_nested_archive_is_out_of_scope_but_not_a_broken_link(self):
        archive = "00_Inbox/Quellen/URL/unterarchiv/index.md"
        self.save(archive, {"url": "https://example.org"})
        self.save("80_Knowledge/Sources/aufarbeitung.md", {"rohquelle": archive, "autor": "Autor"})
        report = stats.collect(self.root)
        self.assertEqual(report["counts"]["raw_files"], 0)
        self.assertEqual(report["counts"]["sources_without_raw_link"], 1)
        self.assertNotIn("Rohquellen-Verweis fehlt", [i["kind"] for i in report["issues"]])


if __name__ == "__main__":
    unittest.main()
