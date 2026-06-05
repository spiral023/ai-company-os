"""Run the core AI-Company-OS health checks."""

from __future__ import annotations

import logging
import argparse
import subprocess
import sys
from pathlib import Path


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_ROOT = ROOT / "70_Scripts"


def run_command(label: str, command: list[str]) -> tuple[str, int]:
    """Run one command and return its label and exit code."""
    logging.info("Starte: %s", label)
    result = subprocess.run(command, cwd=ROOT, check=False)
    if result.returncode == 0:
        logging.info("OK: %s", label)
    else:
        logging.error("Fehler: %s (Exit %d)", label, result.returncode)
    return label, result.returncode


def compile_scripts() -> tuple[str, int]:
    """Compile all Python scripts under 70_Scripts."""
    script_paths = sorted(str(path) for path in SCRIPT_ROOT.glob("*.py"))
    return run_command("Python Compile", [sys.executable, "-m", "py_compile", *script_paths])


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    return argparse.ArgumentParser(description="Zentrale AI-Company-OS Checks ausführen")


def main(argv: list[str] | None = None) -> int:
    """Run all health checks and return 0 only if all pass."""
    parser = build_parser()
    parser.parse_args(argv)

    checks = [
        ("Registry Check", [sys.executable, "70_Scripts/skill_registry_check.py"]),
        ("Skill Autoreview", [sys.executable, "70_Scripts/skill_autoreview.py"]),
        ("External Skill Review", [sys.executable, "70_Scripts/external_skill_review.py"]),
        ("Project Kit List", [sys.executable, "70_Scripts/create_project_kit.py", "--list"]),
        ("Install Project Skills List", [sys.executable, "70_Scripts/install_project_skills.py", "--list"]),
    ]

    results = [run_command(label, command) for label, command in checks]
    results.append(compile_scripts())

    failed = [(label, code) for label, code in results if code != 0]
    if failed:
        logging.error("Health Check: Fehler")
        for label, code in failed:
            logging.error("- %s: Exit %d", label, code)
        return 1

    logging.info("Health Check: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
