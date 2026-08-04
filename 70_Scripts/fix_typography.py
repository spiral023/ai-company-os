#!/usr/bin/env python3
"""Gemischte Anführungszeichen in Markdown-Dateien korrigieren.

Der häufigste Validator-Fehler im Knowledge-System ist ein mit U+201E („)
geöffnetes und mit ASCII (") geschlossenes Zitat. Der Fehler entsteht beim
Schreiben immer wieder neu, weil die öffnende Form aus der Tastatur- oder
Modellgewohnheit kommt und die schließende nicht. Eine Regel in der
Dokumentation genügt dagegen nicht — deshalb dieses Werkzeug.

Nutzung:
    python 70_Scripts/fix_typography.py <datei-oder-ordner> [...] [--dry-run]
    python 70_Scripts/fix_typography.py 80_Knowledge --dry-run
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

OEFFNEND = "„"  # „
SCHLIESSEND = "“"  # "
# „…" ohne schließendes U+201C dazwischen — dieselbe Logik wie im Validator.
MUSTER = re.compile(f"{OEFFNEND}([^{SCHLIESSEND}\n]*?)\"")


def sammle(pfade: list[str]) -> list[Path]:
    dateien: list[Path] = []
    for eintrag in pfade:
        p = Path(eintrag)
        if p.is_dir():
            dateien.extend(sorted(p.rglob("*.md")))
        elif p.is_file():
            dateien.append(p)
        else:
            print(f"⚠ nicht gefunden: {p}")
    return dateien


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pfade", nargs="+", help="Dateien oder Ordner")
    parser.add_argument("--dry-run", action="store_true", help="nur anzeigen")
    args = parser.parse_args()

    gesamt = 0
    betroffen = 0
    for datei in sammle(args.pfade):
        text = datei.read_text(encoding="utf-8")
        neu, anzahl = MUSTER.subn(lambda m: OEFFNEND + m.group(1) + SCHLIESSEND, text)
        if not anzahl:
            continue
        betroffen += 1
        gesamt += anzahl
        print(f"{'[dry-run] ' if args.dry_run else ''}{datei}: {anzahl}")
        if not args.dry_run:
            with datei.open("w", encoding="utf-8", newline="\n") as f:
                f.write(neu)

    if gesamt:
        wort = "würden korrigiert" if args.dry_run else "korrigiert"
        print(f"\n{gesamt} Zitate in {betroffen} Dateien {wort}.")
    else:
        print("Keine gemischten Anführungszeichen gefunden.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
