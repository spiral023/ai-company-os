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
