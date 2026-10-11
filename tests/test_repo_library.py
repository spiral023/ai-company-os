"""Contracts for a complete, safe and reproducible single-file library."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "70_Scripts"))
from repo_library.builder import build_library, render_library
from repo_library.markdown import inline, plain, render
from repo_library.parser import parse_index


FIXTURE = """# Bibliothek

Einführung und Pflegehinweise.

## Was möchtest du tun?

| Aufgabe | Gute Startpunkte | Was du dort konkret findest |
|---|---|---|
| Ein UI verbessern | [a/one](#aone), [b/two](#btwo) | Gestaltung und Reviews |

## Repos nach Kategorie

### Design

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [a/one](#aone) | UI gestalten | Design-Tokens | Skill / Tool | `external_repos/a/one/skills/` |

### Wissen

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [a/one](#aone) | Dokumentation | Diagramme | Tool | `external_repos/a/one/docs/` |

## Empfohlene Startpunkte

### Für Entwickler

1. **[a/one](#aone)** lesen und dann [b/two](#btwo) vergleichen.

**Praktische Kombination:** Erst verstehen, dann verbessern.

## Sicher und sinnvoll übernehmen

Hinweise mit `Code`, **Hervorhebung** und [Link](https://example.com).

## Übersicht

- **Stand:** 2026-10-11

## Detail-Einträge

## a/one

- **URL:** https://github.com/a/one
- **Stars:** ⭐ 1.234
- **Heruntergeladen:** 2026-10-11
- **Struktur:** `src/` <!-- manual -->

Ein vollständiger Beschreibungstext. Weitere Details bleiben erhalten.

---

## b/two

- **URL:** https://github.com/b/two
- **Stars:** ⭐ n/a (privates Repo)
- **Ablage (abweichend):** `external_knowledge/b-two/` — manuell gepflegt <!-- manual -->
- **Unbekanntes Feld:** Wird ebenfalls übernommen.

Ein unkategorisiertes Profil mit besonderen Angaben.

## Weitere Hinweise

Auch zusätzliche Abschnitte bleiben vollständig verfügbar.
"""


def test_complete_source_and_many_to_many_navigation():
    data = parse_index(FIXTURE)
    assert data["sourceMarkdown"] == FIXTURE
    assert data["coverage"] == {"repos":2,"tasks":1,"categories":2,"routes":1,"sections":7}
    first, second = data["repos"]
    assert first["stars"] == 1234
    assert first["categories"] == ["design", "wissen"]
    assert first["types"] == ["Skill", "Tool"]
    assert first["entryPaths"][0] == "external_repos/a/one/skills/"
    assert second["stars"] is None
    assert second["categories"] == []
    assert second["localPath"] == "external_knowledge/b-two/"
    assert any(field["label"] == "Unbekanntes Feld" for field in second["fields"])
    assert data["tasks"][0]["repoIds"] == ["aone", "btwo"]
    assert "Auch zusätzliche Abschnitte" in data["sourceHtml"]
    assert "Praktische Kombination" in data["routes"][0]["html"]


def test_broken_repo_references_and_duplicate_profiles_fail():
    with pytest.raises(ValueError, match="Repo-Verweis"):
        parse_index(FIXTURE.replace("[a/one](#aone),", "[a/missing](#amissing),", 1))
    with pytest.raises(ValueError, match="Doppeltes Repo"):
        parse_index(FIXTURE + "\n## a/one\n\n- **URL:** https://github.com/a/one\n")


def test_markdown_cannot_execute_html_or_fetch_images():
    output = render('<script>alert(1)</script>\n\n[x](javascript:alert)\n\n![remote](https://example.com/image.png)')
    assert "<script>" not in output
    assert "&lt;script&gt;" in output
    assert 'href="javascript:' not in output
    assert "<img" not in output
    assert 'href="https://example.com/image.png"' in output
    assert plain("`external_repos/my_owner/my_repo/`") == "external_repos/my_owner/my_repo/"
    assert "<code>src/test_file.py</code>" in inline("[`src/test_file.py`](README.md)")


def test_builder_is_single_file_and_check_detects_stale_source(tmp_path):
    source, output = tmp_path / "INDEX.md", tmp_path / "INDEX.html"
    source.write_text(FIXTURE + '\n{{DATA}} {{SCRIPTS}} </script>\n', encoding="utf-8")
    coverage = build_library(source, output)
    first = output.read_bytes()
    assert coverage["repos"] == 2
    build_library(source, output)
    assert output.read_bytes() == first
    build_library(source, output, check=True)
    html = output.read_text(encoding="utf-8")
    encoded = re.search(r'<script id="libraryData" type="application/json">(.*?)</script>', html, re.DOTALL)[1]
    assert "</script>" not in encoded
    assert json.loads(encoded)["sourceMarkdown"] == source.read_text(encoding="utf-8")
    assert not re.search(r'<(?:script|link|img)\b[^>]*(?:src|href)=["\']https?://', html)
    source.write_text(FIXTURE + "\nNeue Information.\n", encoding="utf-8")
    with pytest.raises(ValueError, match="veraltet"):
        build_library(source, output, check=True)
    assert output.read_bytes() == first


def test_check_detects_a_template_change(tmp_path, monkeypatch):
    import shutil
    from repo_library import builder
    modules = tmp_path / "modules"
    shutil.copytree(builder.MODULE_ROOT / "templates", modules / "templates")
    shutil.copy2(builder.MODULE_ROOT / "discovery.json", modules / "discovery.json")
    monkeypatch.setattr(builder, "MODULE_ROOT", modules)
    source, output = tmp_path / "INDEX.md", tmp_path / "INDEX.html"
    source.write_text(FIXTURE, encoding="utf-8")
    build_library(source, output)
    css = modules / "templates/library.css"
    css.write_text(css.read_text(encoding="utf-8") + "\n/* Changed layout */\n", encoding="utf-8")
    with pytest.raises(ValueError, match="veraltet"):
        build_library(source, output, check=True)


def test_current_index_has_no_omitted_profile_or_original_content(tmp_path):
    source = ROOT / "external_repos/INDEX.md"
    html, coverage = render_library(source, tmp_path / "INDEX.html")
    encoded = re.search(r'<script id="libraryData" type="application/json">(.*?)</script>', html, re.DOTALL)[1]
    data = json.loads(encoded)
    original = source.read_text(encoding="utf-8")
    assert data["sourceMarkdown"] == original
    headings = re.findall(r"^## ([\w.-]+/[\w.-]+)$", original, re.MULTILINE)
    assert {repo["label"] for repo in data["repos"]} == set(headings)
    assert coverage["repos"] == len(headings)
    assert all(repo["html"] for repo in data["repos"])
    assert all(task["repoIds"] for task in data["tasks"])
