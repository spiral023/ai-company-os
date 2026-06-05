"""Prepare a new external skill source intake entry."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Any


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "30_Skills" / "registry.yaml"
INTAKE_ROOT = ROOT / "30_Skills" / "external" / "intake"
REVIEW_ROOT = ROOT / "30_Skills" / "external" / "reviews"


def load_registry() -> dict[str, Any] | None:
    """Load registry YAML when PyYAML is available."""
    try:
        import yaml  # type: ignore[import-not-found]
    except ImportError:
        return None

    if not REGISTRY_PATH.exists():
        return None

    loaded = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    if not isinstance(loaded, dict):
        return None
    return loaded


def source_exists(registry: dict[str, Any] | None, source_id: str) -> bool:
    """Return whether an external source id already exists."""
    if registry is None:
        return source_id in REGISTRY_PATH.read_text(encoding="utf-8")
    return any(
        isinstance(source, dict) and source.get("id") == source_id
        for source in registry.get("external_sources", [])
    )


def build_source_entry(source_id: str, name: str, source_url: str) -> dict[str, Any]:
    """Build a default external source entry."""
    return {
        "id": source_id,
        "name": name,
        "source": source_url,
        "local_path": f"30_Skills/external/sources/{source_id}",
        "install_mode": "submodule-or-copy",
        "status": "planned",
        "trust": "unreviewed",
        "allowed_use": ["none"],
        "blocked_use": ["automatic_project_copy", "script_execution"],
        "license": "unknown",
        "review_file": f"30_Skills/external/reviews/{source_id}.md",
        "notes": "Neue externe Skill-Quelle. Vor Nutzung prüfen.",
    }


def review_template(source: dict[str, Any]) -> str:
    """Return a review template for an external source."""
    return f"""# Review: {source["name"]}

## Status

- Quelle: {source["source"]}
- Lokaler Pfad: {source["local_path"]}
- Status: {source["status"]}
- Trust-Level: {source["trust"]}
- Lizenz: {source["license"]}
- Letzte Prüfung:

## Zweck

Kurzbeschreibung.

## Inhaltliche Sichtung

- Welche Skill-Typen sind enthalten?
- Wofür sind sie nützlich?
- Welche Überschneidungen gibt es mit lokalen Skills?

## Sicherheitsprüfung

- Werden Scripts mitgeliefert?
- Werden externe Tools oder APIs vorausgesetzt?
- Gibt es riskante Anweisungen?
- Gibt es Hinweise auf Secrets, Tokens oder Credential Handling?
- Gibt es Prompt-Injection- oder Supply-Chain-Risiken?

## Lizenzprüfung

- Lizenz gefunden: ja / nein
- Lizenztyp:
- Nutzung im eigenen Repo erlaubt: unklar / ja / nein
- Hinweise:

## Integrationsentscheidung

- Nicht verwenden
- Nur als Referenz nutzen
- Einzelne Skills kopieren
- Als Submodule einbinden
- Fork erstellen und anpassen

## Empfehlung

Kurze Empfehlung.

## Philipp-Freigabe

- Erforderlich: ja
- Status: offen
"""


def write_registry_with_pyyaml(registry: dict[str, Any], source: dict[str, Any]) -> bool:
    """Append a source entry to the registry using PyYAML."""
    try:
        import yaml  # type: ignore[import-not-found]
    except ImportError:
        return False

    registry.setdefault("external_sources", []).append(source)
    REGISTRY_PATH.write_text(
        yaml.safe_dump(registry, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    return True


def write_intake_note(source: dict[str, Any]) -> Path:
    """Write an intake note when registry writing is unavailable."""
    INTAKE_ROOT.mkdir(parents=True, exist_ok=True)
    path = INTAKE_ROOT / f"{source['id']}.md"
    block = "\n".join(
        [
            "```yaml",
            "  - id: " + source["id"],
            f"    name: \"{source['name']}\"",
            f"    source: \"{source['source']}\"",
            f"    local_path: \"{source['local_path']}\"",
            "    install_mode: \"submodule-or-copy\"",
            "    status: \"planned\"",
            "    trust: \"unreviewed\"",
            "    allowed_use:",
            "      - \"none\"",
            "    blocked_use:",
            "      - \"automatic_project_copy\"",
            "      - \"script_execution\"",
            "    license: \"unknown\"",
            f"    review_file: \"{source['review_file']}\"",
            f"    notes: \"{source['notes']}\"",
            "```",
        ]
    )
    path.write_text(f"# Intake: {source['name']}\n\n{block}\n", encoding="utf-8")
    return path


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI parser."""
    parser = argparse.ArgumentParser(description="Externe Skill-Quelle vorbereiten")
    parser.add_argument("--id", required=True, help="Eindeutige Quellen-ID")
    parser.add_argument("--name", required=True, help="Anzeigename")
    parser.add_argument("--source", required=True, help="Quell-URL")
    return parser


def main() -> int:
    """Run the external source intake CLI."""
    args = build_parser().parse_args()
    registry = load_registry()

    if source_exists(registry, args.id):
        logging.error("Externe Quelle existiert bereits: %s", args.id)
        return 1

    source = build_source_entry(args.id, args.name, args.source)

    if registry is not None:
        write_registry_with_pyyaml(registry, source)
        logging.info("Registry aktualisiert: %s", REGISTRY_PATH.relative_to(ROOT))
    else:
        intake_path = write_intake_note(source)
        logging.warning("PyYAML nicht verfügbar. Intake-Datei erstellt: %s", intake_path.relative_to(ROOT))

    REVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    review_path = REVIEW_ROOT / f"{args.id}.md"
    if not review_path.exists():
        review_path.write_text(review_template(source), encoding="utf-8")
        logging.info("Review-Datei erstellt: %s", review_path.relative_to(ROOT))

    logging.info("Nächste Schritte: Quelle prüfen, Lizenz prüfen, Review ausfüllen, Philipp-Freigabe einholen.")
    logging.info("Keine externen Repos geklont.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
