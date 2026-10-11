"""Build or verify external_repos/INDEX.html without installing dependencies."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from repo_library.builder import build_library


ROOT = Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Offline-Repo-Bibliothek aus INDEX.md erzeugen")
    parser.add_argument("--input", type=Path, default=ROOT / "external_repos/INDEX.md")
    parser.add_argument("--output", type=Path, default=ROOT / "external_repos/INDEX.html")
    parser.add_argument("--check", action="store_true", help="Vollständigkeit und Aktualität prüfen, nichts schreiben")
    args = parser.parse_args(argv)
    try:
        counts = build_library(args.input.resolve(), args.output.resolve(), check=args.check)
    except (OSError, ValueError, KeyError) as error:
        print(f"Repo-Bibliothek: {error}", file=sys.stderr)
        return 1
    print(f"HTML {'geprüft' if args.check else 'erstellt'}: {args.output}")
    print(f"{counts['repos']} Profile · {counts['tasks']} Aufgaben · {counts['categories']} Themen · {counts['routes']} Arbeitsrouten; Originaltext vollständig eingebettet.")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
