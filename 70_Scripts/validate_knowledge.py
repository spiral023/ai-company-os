"""Deterministischer Validator für das Knowledge-System unter 80_Knowledge/.

Prüft Formatregeln, die kein LLM-Urteil brauchen: Frontmatter der Sources,
Pflicht-Abschnitte und Belege-Format der Patterns, Konfidenz-Konsistenz,
Wiki-Link-Ziele, Index-Vollständigkeit, Stand-Datum der Vergleiche sowie
Encoding und Typografie (BOM, CRLF, gemischte Anführungszeichen).

Nutzung:
    python 70_Scripts/validate_knowledge.py [--root 80_Knowledge]

Exit-Code 0 bei fehlerfreiem Lauf, sonst 1. Nur Standardbibliothek.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SOURCE_REQUIRED_FIELDS = ["url", "autor", "datum", "erfasst", "typ"]
SOURCE_TYP_VALUES = {"tweet", "artikel", "repo", "video", "notiz"}
DATE_FIELDS = {"datum", "erfasst"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

PATTERN_REQUIRED_SECTIONS = [
    "## Zweck",
    "## Funktionsweise",
    "## Vorteile",
    "## Nachteile & Grenzen",
    "## Wann einsetzen, wann nicht",
    "## Belege",
    "## Spannungen & offene Fragen",
    "## Verwandte Patterns",
]

KONFIDENZ_ORDER = {"meinung": 1, "mehrfach-belegt": 2, "verifiziert": 3}
KONFIDENZ_RE = re.compile(r"^\*\*Konfidenz:\*\*\s+(meinung|mehrfach-belegt|verifiziert)\b")

BELEG_RE = re.compile(
    r"^- \d{4}-\d{2}-\d{2} · "
    r"(\[\[[^\]]+\]\]|external_repos/\S+) · "
    r"(meinung|mehrfach-belegt|verifiziert) — .+$"
)

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
MIXED_QUOTE_RE = re.compile(r"„[^“\n]*\"")
STAND_RE = re.compile(r"^\*\*Stand:\*\*\s+\d{4}-\d{2}-\d{2}", re.MULTILINE)


def read_text(path: Path, errors: list[str]) -> str:
    """Datei lesen und Encoding-/Zeilenenden-Regeln prüfen."""
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        errors.append(f"{path.name}: UTF-8 BOM am Dateianfang")
        raw = raw[3:]
    text = raw.decode("utf-8")
    if "\r" in text:
        errors.append(f"{path.name}: CRLF-Zeilenenden (erwartet: LF)")
        text = text.replace("\r\n", "\n")
    return text


def check_typography(name: str, text: str, errors: list[str]) -> None:
    for match in MIXED_QUOTE_RE.finditer(text):
        errors.append(
            f"{name}: gemischte Anführungszeichen (ASCII \" nach „): {match.group(0)!r}"
        )


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip().strip('"')
    return fields


def check_source(path: Path, text: str, errors: list[str]) -> None:
    fields = parse_frontmatter(text)
    if fields is None:
        errors.append(f"{path.name}: Frontmatter fehlt oder ist unvollständig")
        return
    for field in SOURCE_REQUIRED_FIELDS:
        if not fields.get(field):
            errors.append(f"{path.name}: Pflichtfeld '{field}' fehlt im Frontmatter")
    typ = fields.get("typ")
    if typ and typ not in SOURCE_TYP_VALUES:
        errors.append(
            f"{path.name}: ungültiger typ '{typ}' (erlaubt: {', '.join(sorted(SOURCE_TYP_VALUES))})"
        )
    for field in DATE_FIELDS:
        value = fields.get(field)
        if value and not DATE_RE.match(value):
            errors.append(f"{path.name}: Feld '{field}' ist kein YYYY-MM-DD-Datum: '{value}'")


def beleg_lines(text: str) -> list[str]:
    """Listenzeilen im Abschnitt '## Belege' extrahieren."""
    lines: list[str] = []
    in_belege = False
    for line in text.splitlines():
        if line.startswith("## "):
            in_belege = line.strip() == "## Belege"
            continue
        if in_belege and line.startswith("- "):
            lines.append(line)
    return lines


def check_pattern(path: Path, text: str, errors: list[str]) -> None:
    for section in PATTERN_REQUIRED_SECTIONS:
        if not re.search(rf"^{re.escape(section)}\s*$", text, re.MULTILINE):
            errors.append(f"{path.name}: Pflicht-Abschnitt '{section}' fehlt")

    konfidenz_match = None
    for line in text.splitlines():
        konfidenz_match = KONFIDENZ_RE.match(line)
        if konfidenz_match:
            break
    if konfidenz_match is None:
        errors.append(
            f"{path.name}: Konfidenz-Zeile fehlt oder ungültig "
            "(erwartet: '**Konfidenz:** meinung|mehrfach-belegt|verifiziert')"
        )

    belege = beleg_lines(text)
    if not belege:
        errors.append(f"{path.name}: keine Beleg-Zeile unter '## Belege' (Invariante 4)")
    max_typ = 0
    for line in belege:
        match = BELEG_RE.match(line)
        if not match:
            errors.append(
                f"{path.name}: Beleg-Zeile entspricht keinem erlaubten Format: '{line}'"
            )
            continue
        max_typ = max(max_typ, KONFIDENZ_ORDER[match.group(2)])

    if konfidenz_match and max_typ:
        stated = KONFIDENZ_ORDER[konfidenz_match.group(1)]
        if stated != max_typ:
            expected = next(k for k, v in KONFIDENZ_ORDER.items() if v == max_typ)
            errors.append(
                f"{path.name}: Konfidenz '{konfidenz_match.group(1)}' passt nicht zum "
                f"höchsten Beleg-Typ '{expected}'"
            )


def check_vergleich(path: Path, text: str, errors: list[str]) -> None:
    if not STAND_RE.search(text):
        errors.append(f"{path.name}: '**Stand:** YYYY-MM-DD'-Zeile fehlt")


def check_wikilinks(name: str, text: str, root: Path, known: set[str], errors: list[str]) -> None:
    for match in WIKILINK_RE.finditer(text):
        target = match.group(1).strip()
        if "/" in target:
            if not (root.parent / f"{target}.md").is_file():
                errors.append(f"{name}: Wiki-Link-Ziel nicht gefunden: [[{target}]]")
        elif target not in known:
            errors.append(f"{name}: Wiki-Link-Ziel nicht gefunden: [[{target}]]")


def check_index(root: Path, known_index_targets: list[str], errors: list[str]) -> None:
    index_path = root / "Index.md"
    if not index_path.is_file():
        errors.append("Index.md fehlt")
        return
    index_text = index_path.read_bytes().decode("utf-8")
    linked = {m.group(1).strip() for m in WIKILINK_RE.finditer(index_text)}
    for target in known_index_targets:
        if target not in linked:
            errors.append(f"Index.md: Eintrag für '{target}' fehlt")


def validate(root: Path) -> list[str]:
    """Alle Prüfungen ausführen; Liste der Fehler zurückgeben (leer = OK)."""
    errors: list[str] = []
    if not root.is_dir():
        return [f"Ordner nicht gefunden: {root}"]

    known = {path.stem for path in root.rglob("*.md")}
    index_targets: list[str] = []

    for path in sorted(root.rglob("*.md")):
        text = read_text(path, errors)
        if path.name == "README.md":
            continue  # Regel-/Template-Datei: enthält Platzhalter-Links und Beispiel-Zitate
        check_typography(path.name, text, errors)
        check_wikilinks(path.name, text, root, known, errors)
        parent = path.parent.name
        if parent == "Sources":
            check_source(path, text, errors)
        elif parent == "Patterns":
            check_pattern(path, text, errors)
            index_targets.append(path.stem)
        elif parent == "Vergleiche":
            check_vergleich(path, text, errors)
            index_targets.append(path.stem)

    check_index(root, index_targets, errors)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validiert das Knowledge-System (80_Knowledge).")
    default_root = Path(__file__).resolve().parents[1] / "80_Knowledge"
    parser.add_argument(
        "--root",
        type=Path,
        default=default_root,
        help="Pfad zum Knowledge-Ordner (Standard: 80_Knowledge im Repo)",
    )
    args = parser.parse_args(argv)

    errors = validate(args.root)
    if errors:
        for error in errors:
            print(f"FEHLER  {error}")
        print(f"\n{len(errors)} Fehler gefunden.")
        return 1
    file_count = len(list(args.root.rglob("*.md")))
    print(f"OK: {args.root.name} konsistent ({file_count} Dateien geprüft).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
