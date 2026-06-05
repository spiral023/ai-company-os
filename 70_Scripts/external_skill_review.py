"""Review external skill sources without activating or executing them."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Any


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "30_Skills" / "registry.yaml"
EXTERNAL_ROOT = ROOT / "30_Skills" / "external"
REQUIRED_FIELDS = (
    "id",
    "name",
    "source",
    "local_path",
    "status",
    "trust",
    "allowed_use",
    "blocked_use",
    "license",
    "review_file",
)
SCRIPT_SUFFIXES = {".py", ".sh", ".ps1", ".js", ".ts"}


def load_registry() -> dict[str, Any] | None:
    """Load the registry with a friendly PyYAML message."""
    try:
        import yaml  # type: ignore[import-not-found]
    except ImportError:
        logging.error("PyYAML fehlt. Bitte installieren: python -m pip install PyYAML")
        return None

    if not REGISTRY_PATH.exists():
        logging.error("Registry fehlt: %s", REGISTRY_PATH.relative_to(ROOT))
        return None

    loaded = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    if not isinstance(loaded, dict):
        logging.error("Registry YAML hat kein erwartetes Objektformat")
        return None
    return loaded


def count_local_external_files(local_path: str) -> tuple[int, int, int]:
    """Count Markdown, SKILL.md, and script files in a local external source folder."""
    folder = ROOT / local_path
    if not folder.exists() or not folder.is_dir():
        return 0, 0, 0

    markdown_files = list(folder.rglob("*.md"))
    skill_files = [path for path in markdown_files if path.name == "SKILL.md"]
    script_files = [path for path in folder.rglob("*") if path.suffix.lower() in SCRIPT_SUFFIXES]
    return len(markdown_files), len(skill_files), len(script_files)


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI parser."""
    parser = argparse.ArgumentParser(description="Externe Skill-Quellen prüfen")
    parser.add_argument("--source", help="Nur eine externe Quelle per ID prüfen")
    return parser


def main() -> int:
    """Print an external skill source review."""
    args = build_parser().parse_args()
    registry = load_registry()
    if registry is None:
        return 1

    external_sources = registry.get("external_sources", [])
    if not isinstance(external_sources, list):
        logging.error("`external_sources` ist keine Liste")
        return 1

    if args.source:
        external_sources = [
            source
            for source in external_sources
            if isinstance(source, dict) and source.get("id") == args.source
        ]
        if not external_sources:
            logging.error("Externe Quelle nicht gefunden: %s", args.source)
            return 1

    ok: list[str] = []
    warnings: list[str] = []
    hints: list[str] = []

    logging.info("Externe Skill-Quellen: %d", len(external_sources))
    for source in external_sources:
        if not isinstance(source, dict):
            warnings.append("Ungültiger external_sources Eintrag")
            continue

        source_id = str(source.get("id", "unbekannt"))
        source_url = str(source.get("source", ""))
        local_path = str(source.get("local_path", ""))
        review_file = str(source.get("review_file", ""))
        markdown_count, skill_count, script_count = count_local_external_files(local_path)

        for field in REQUIRED_FIELDS:
            if field not in source:
                warnings.append(f"{source_id}: Feld fehlt: {field}")

        if "TODO" in source_url:
            hints.append(f"{source_id}: Quelle ist noch TODO")

        if review_file and not (ROOT / review_file).exists():
            warnings.append(f"{source_id}: Review-Datei fehlt: {review_file}")

        if local_path and (ROOT / local_path).exists():
            ok.append(f"{source_id}: lokaler Pfad vorhanden")
        else:
            hints.append(f"{source_id}: lokaler Pfad noch nicht vorhanden")

        logging.info("Quelle: %s (%s)", source_id, source.get("name", "-"))
        logging.info("  Status: %s", source.get("status", "-"))
        logging.info("  Trust-Level: %s", source.get("trust", "-"))
        logging.info("  Source: %s", source_url)
        logging.info("  Local Path: %s", local_path or "-")
        logging.info("  Allowed Use: %s", ", ".join(source.get("allowed_use", [])))
        logging.info("  Blocked Use: %s", ", ".join(source.get("blocked_use", [])))
        logging.info("  Lizenz: %s", source.get("license", "-"))
        logging.info("  Review: %s", review_file or "-")
        logging.info("  Lokale Markdown-Dateien: %d", markdown_count)
        logging.info("  Mögliche SKILL.md Dateien: %d", skill_count)
        logging.info("  Mögliche Scripts: %d", script_count)

    logging.info("OK: %d", len(ok))
    for item in ok:
        logging.info("OK: %s", item)

    logging.info("Warnungen: %d", len(warnings))
    for warning in warnings:
        logging.warning(warning)

    logging.info("Hinweise: %d", len(hints))
    for hint in hints:
        logging.info("Hinweis: %s", hint)

    logging.info("Keine externen Scripts ausgeführt. Keine externen Skills aktiviert.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
