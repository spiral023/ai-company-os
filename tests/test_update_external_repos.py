"""Regression tests for the external repository index updater."""

from __future__ import annotations

import importlib.util
from pathlib import Path


SCRIPT_PATH = Path(__file__).parents[1] / "70_Scripts" / "update_external_repos.py"
SPEC = importlib.util.spec_from_file_location("update_external_repos", SCRIPT_PATH)
assert SPEC and SPEC.loader
updater = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(updater)


def test_update_index_adds_missing_mechanical_metadata(tmp_path, monkeypatch):
    """New manually documented repos receive the metadata maintained by the script."""
    index = tmp_path / "INDEX.md"
    index.write_text(
        """# Index

<!-- OVERVIEW:START -->
<!-- OVERVIEW:END -->

## owner/repo

- **URL:** https://github.com/owner/repo
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-07-13

Zusammenfassung.
""",
        encoding="utf-8",
    )
    monkeypatch.setattr(updater, "INDEX_PATH", index)

    updater.update_index({"owner/repo": (3, 2048, "1× SKILL.md · Ordner: skills")}, set(), "2026-07-13", False)

    content = index.read_text(encoding="utf-8")
    assert "- **Dateien:** 3 · **Größe:** 2K" in content
    assert "- **Struktur:** 1× SKILL.md · Ordner: skills" in content
