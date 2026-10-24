"""Tests for the root AI-Company-OS CLI."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def load_ai_module():
    """Load ai.py from the repository root."""
    spec = importlib.util.spec_from_file_location("ai", ROOT / "ai.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("ai.py konnte nicht geladen werden")
    module = importlib.util.module_from_spec(spec)
    sys.modules["ai"] = module
    spec.loader.exec_module(module)
    return module


class AiCliTest(unittest.TestCase):
    """Check that ai.py forwards commands to existing scripts."""

    def test_source_statistics_forwards_snapshot_and_filters(self) -> None:
        ai = load_ai_module()
        with patch.object(ai, "run_subprocess", return_value=0) as run:
            self.assertEqual(ai.main(["quellen", "statistik", "--snapshot", "--autor", "matt-pocock",
                                      "--thema", "verifikation", "--keyword", "TDD", "--bestand", "sources"]), 0)
        command = run.call_args.args[0]
        self.assertEqual(command[:4], [sys.executable, "-X", "utf8", str(ROOT / "70_Scripts/quellen_statistik.py")])
        self.assertIn("--snapshot", command)
        for flag, value in (("--autor", "matt-pocock"), ("--thema", "verifikation"), ("--keyword", "TDD"), ("--bestand", "sources")):
            self.assertEqual(command[command.index(flag) + 1], value)

    def test_local_transcription_uses_isolated_environment(self) -> None:
        ai = load_ai_module()
        with patch.object(Path, "is_file", return_value=True), patch.object(ai, "run_subprocess", return_value=0) as run:
            result = ai.main(["transkribieren", "2EoNRuFJfBo", "--audio", "pilot.webm", "--batch-size", "2", "--hls"])
        self.assertEqual(result, 0)
        command, label = run.call_args.args
        self.assertIn("youtube-transcription", command[0])
        self.assertEqual(command[1:4], ["-X", "utf8", str(ROOT / "70_Scripts/youtube_transcribe.py")])
        self.assertIn("2EoNRuFJfBo", command)
        self.assertIn("--hls", command)
        self.assertEqual(command[command.index("--batch-size") + 1], "2")
        self.assertEqual(command[-2:], ["--audio", "pilot.webm"])
        self.assertEqual(label, "Video lokal transkribieren")

    def test_tiktok_transcription_uses_the_same_local_environment(self) -> None:
        ai = load_ai_module()
        url = "https://www.tiktok.com/@a/video/7699871396729507105"
        with patch.object(Path, "is_file", return_value=True), patch.object(ai, "run_subprocess", return_value=0) as run:
            self.assertEqual(ai.main(["transkribieren", url]), 0)
        self.assertIn(url, run.call_args.args[0])
        self.assertIn("youtube-transcription", run.call_args.args[0][0])

    def test_ingest_can_disable_the_automatic_audio_fallback(self) -> None:
        ai = load_ai_module()
        with patch.object(ai, "run_subprocess", return_value=0) as run:
            self.assertEqual(ai.main(["ingest", "https://youtu.be/2EoNRuFJfBo", "--no-whisper"]), 0)
        self.assertIn("--no-whisper", run.call_args.args[0])

    def test_feed_check_forwards_filter_and_limit(self) -> None:
        ai = load_ai_module()
        with patch.object(ai, "run_subprocess", return_value=0) as run:
            result = ai.main(["feeds", "check", "--url", "https://example.org/rss.xml", "--limit", "5"])
        self.assertEqual(result, 0)
        run.assert_called_once_with(
            [sys.executable, str(ROOT / "70_Scripts" / "feeds.py"), "check",
             "--limit", "5", "--url", "https://example.org/rss.xml"], "Feeds verwalten")

    def test_feed_add_forwards_name(self) -> None:
        ai = load_ai_module()
        with patch.object(ai, "run_subprocess", return_value=0) as run:
            result = ai.main(["feeds", "add", "https://example.org/rss.xml", "--name", "Beispiel"])
        self.assertEqual(result, 0)
        run.assert_called_once_with(
            [sys.executable, str(ROOT / "70_Scripts" / "feeds.py"), "add",
             "https://example.org/rss.xml", "--name", "Beispiel"], "Feeds verwalten")

    def test_feed_selection_options_are_forwarded(self) -> None:
        ai = load_ai_module()
        with patch.object(ai, "run_subprocess", return_value=0) as run:
            result = ai.main(["feeds", "check", "--thema", "verifikation", "--alle", "--ausgabe", "Auswahl.md"])
        self.assertEqual(result, 0)
        run.assert_called_once_with(
            [sys.executable, str(ROOT / "70_Scripts" / "feeds.py"), "check", "--limit", "10",
             "--thema", "verifikation", "--alle", "--ausgabe", "Auswahl.md"], "Feeds verwalten")

    def test_health_forwards_to_healthcheck_script(self) -> None:
        ai = load_ai_module()

        with patch.object(ai, "run_subprocess", return_value=0) as run_subprocess:
            result = ai.main(["health"])

        self.assertEqual(result, 0)
        run_subprocess.assert_called_once_with(
            [sys.executable, str(ROOT / "70_Scripts" / "company_os_healthcheck.py")],
            "Health Check",
        )

    def test_external_source_is_forwarded(self) -> None:
        ai = load_ai_module()

        with patch.object(ai, "run_subprocess", return_value=0) as run_subprocess:
            result = ai.main(["external", "--source", "marketingskills"])

        self.assertEqual(result, 0)
        run_subprocess.assert_called_once_with(
            [
                sys.executable,
                str(ROOT / "70_Scripts" / "external_skill_review.py"),
                "--source",
                "marketingskills",
            ],
            "Externe Skills prüfen",
        )

    def test_skills_without_options_lists_skills(self) -> None:
        ai = load_ai_module()

        with patch.object(ai, "run_subprocess", return_value=0) as run_subprocess:
            result = ai.main(["skills"])

        self.assertEqual(result, 0)
        run_subprocess.assert_called_once_with(
            [sys.executable, str(ROOT / "70_Scripts" / "install_project_skills.py"), "--list"],
            "Skills anzeigen oder installieren",
        )

    def test_ingest_forwards_source_options(self) -> None:
        ai = load_ai_module()

        with patch.object(ai, "run_subprocess", return_value=0) as run_subprocess:
            result = ai.main(
                [
                    "ingest",
                    "https://youtu.be/dQw4w9WgXcQ",
                    "--typ",
                    "youtube",
                    "--force",
                    "--titel",
                    "Testvideo",
                ]
            )

        self.assertEqual(result, 0)
        run_subprocess.assert_called_once_with(
            [
                sys.executable,
                str(ROOT / "70_Scripts" / "ingest_source.py"),
                "https://youtu.be/dQw4w9WgXcQ",
                "--typ",
                "youtube",
                "--force",
                "--titel",
                "Testvideo",
            ],
            "Quelle erfassen",
        )

    def test_new_noninteractive_forwards_project_creation(self) -> None:
        ai = load_ai_module()

        with patch.object(ai, "run_subprocess", return_value=0) as run_subprocess:
            result = ai.main(
                [
                    "new",
                    "--kit",
                    "saas-webapp",
                    "--name",
                    "teambridge",
                    "--target",
                    "../teambridge",
                    "--copy-skills",
                ]
            )

        self.assertEqual(result, 0)
        run_subprocess.assert_called_once_with(
            [
                sys.executable,
                str(ROOT / "70_Scripts" / "create_project_kit.py"),
                "--kit",
                "saas-webapp",
                "--name",
                "teambridge",
                "--target",
                "../teambridge",
                "--copy-skills",
            ],
            "Projekt erstellen",
        )


if __name__ == "__main__":
    unittest.main()
