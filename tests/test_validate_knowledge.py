"""Tests für den 80_Knowledge-Validator."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_validator():
    """validate_knowledge.py aus 70_Scripts laden."""
    spec = importlib.util.spec_from_file_location(
        "validate_knowledge", ROOT / "70_Scripts" / "validate_knowledge.py"
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("validate_knowledge.py konnte nicht geladen werden")
    module = importlib.util.module_from_spec(spec)
    sys.modules["validate_knowledge"] = module
    spec.loader.exec_module(module)
    return module


VALID_SOURCE = """---
url: https://x.com/beispiel/status/123
autor: "@beispiel (Beispiel)"
datum: 2026-07-10
erfasst: 2026-07-11
typ: tweet
---

# Beispiel zu Testthema

## Inhalt

Ein Beispieltext mit korrekter Typografie: „so sieht das aus“.

## Kernaussagen

- Aussage eins → [[Test-Pattern]]
"""

VALID_PATTERN = """# Test-Pattern

**Konfidenz:** verifiziert

## Zweck

Testzweck.

## Funktionsweise

Testablauf.

## Vorteile

- Ein Vorteil.

## Nachteile & Grenzen

- Eine Grenze.

## Wann einsetzen, wann nicht

- Einsetzen: im Test.
- Nicht einsetzen: produktiv.

## Belege

- 2026-07-11 · [[2026-07-10-beispiel-testthema]] · meinung — Beispielbeleg.
- 2026-07-11 · external_repos/owner/repo/README.md · verifiziert — Dort bestätigt.

## Spannungen & offene Fragen

- keine bekannt

## Verwandte Patterns

- [[Zweit-Pattern]]
"""

SECOND_PATTERN = """# Zweit-Pattern

**Konfidenz:** meinung

## Zweck

Zweck.

## Funktionsweise

Ablauf.

## Vorteile

- Vorteil.

## Nachteile & Grenzen

- Grenze.

## Wann einsetzen, wann nicht

- Einsetzen: hier.
- Nicht einsetzen: dort.

## Belege

- 2026-07-11 · [[2026-07-10-beispiel-testthema]] · meinung — Beleg.

## Spannungen & offene Fragen

- keine bekannt

## Verwandte Patterns

- [[Test-Pattern]]
"""

VALID_VERGLEICH = """# Vergleich: Testfeld

**Stand:** 2026-07-11

## Übersicht

| Framework/Pattern | Kernidee | Stärken | Schwächen | Quelle/Repo |
|---|---|---|---|---|
| Test | Idee | Stärke | Schwäche | Repo |

## Empfehlungen

- Testfall: Test nehmen, weil Test ([[Test-Pattern]]).

## Offene Fragen

- keine
"""

VALID_INDEX = """# Knowledge-Index

Einstieg. Regeln: [[80_Knowledge/README|README]].

## Patterns

- [[Test-Pattern]] — Einzeiler.
- [[Zweit-Pattern]] — Einzeiler.

## Vergleiche

- [[Testfeld]] — Einzeiler.
"""


class ValidateKnowledgeTest(unittest.TestCase):
    """Prüft den Validator gegen einen synthetischen Mini-Vault."""

    def setUp(self) -> None:
        self.module = load_validator()
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "80_Knowledge"
        (self.root / "Sources").mkdir(parents=True)
        (self.root / "Patterns").mkdir()
        (self.root / "Vergleiche").mkdir()
        self.write("Sources/2026-07-10-beispiel-testthema.md", VALID_SOURCE)
        self.write("Patterns/Test-Pattern.md", VALID_PATTERN)
        self.write("Patterns/Zweit-Pattern.md", SECOND_PATTERN)
        self.write("Vergleiche/Testfeld.md", VALID_VERGLEICH)
        self.write("Index.md", VALID_INDEX)
        self.write("README.md", "# Knowledge-System\n\nRegeln.\n")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write(self, relative: str, content: str) -> None:
        path = self.root / relative
        path.write_bytes(content.encode("utf-8"))

    def errors(self):
        return self.module.validate(self.root)

    def assert_error_containing(self, fragment: str) -> None:
        errors = self.errors()
        self.assertTrue(
            any(fragment in error for error in errors),
            f"Erwarteter Fehler mit '{fragment}' fehlt. Fehler: {errors}",
        )

    def test_valid_vault_passes(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_source_missing_frontmatter_field(self) -> None:
        self.write(
            "Sources/2026-07-10-beispiel-testthema.md",
            VALID_SOURCE.replace("erfasst: 2026-07-11\n", ""),
        )
        self.assert_error_containing("erfasst")

    def test_source_invalid_typ(self) -> None:
        self.write(
            "Sources/2026-07-10-beispiel-testthema.md",
            VALID_SOURCE.replace("typ: tweet", "typ: podcast"),
        )
        self.assert_error_containing("typ")

    def test_pattern_missing_section(self) -> None:
        self.write(
            "Patterns/Test-Pattern.md",
            VALID_PATTERN.replace("## Spannungen & offene Fragen\n\n- keine bekannt\n\n", ""),
        )
        self.assert_error_containing("Spannungen")

    def test_pattern_invalid_beleg_line(self) -> None:
        self.write(
            "Patterns/Test-Pattern.md",
            VALID_PATTERN.replace(
                "- 2026-07-11 · [[2026-07-10-beispiel-testthema]] · meinung — Beispielbeleg.",
                "- irgendwann mal gesehen",
            ),
        )
        self.assert_error_containing("Beleg")

    def test_pattern_konfidenz_inconsistent(self) -> None:
        self.write(
            "Patterns/Zweit-Pattern.md",
            SECOND_PATTERN.replace("**Konfidenz:** meinung", "**Konfidenz:** verifiziert"),
        )
        self.assert_error_containing("Konfidenz")

    def test_broken_wikilink(self) -> None:
        self.write(
            "Patterns/Test-Pattern.md",
            VALID_PATTERN.replace("[[Zweit-Pattern]]", "[[Gibt-Es-Nicht]]"),
        )
        self.assert_error_containing("Gibt-Es-Nicht")

    def test_index_missing_pattern(self) -> None:
        self.write(
            "Index.md",
            VALID_INDEX.replace("- [[Zweit-Pattern]] — Einzeiler.\n", ""),
        )
        self.assert_error_containing("Zweit-Pattern")

    def test_mixed_quotes_flagged(self) -> None:
        self.write(
            "Patterns/Test-Pattern.md",
            VALID_PATTERN.replace("## Zweck\n\nTestzweck.", '## Zweck\n\nEin „falsches" Zitat.'),
        )
        self.assert_error_containing("Anführungszeichen")

    def test_bom_flagged(self) -> None:
        self.write("Patterns/Test-Pattern.md", "﻿" + VALID_PATTERN)
        self.assert_error_containing("BOM")

    def test_crlf_flagged(self) -> None:
        self.write("Patterns/Test-Pattern.md", VALID_PATTERN.replace("\n", "\r\n"))
        self.assert_error_containing("CRLF")

    def test_vergleich_missing_stand(self) -> None:
        self.write(
            "Vergleiche/Testfeld.md",
            VALID_VERGLEICH.replace("**Stand:** 2026-07-11\n\n", ""),
        )
        self.assert_error_containing("Stand")


if __name__ == "__main__":
    unittest.main()
