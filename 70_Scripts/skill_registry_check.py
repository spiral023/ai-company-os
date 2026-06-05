"""Check the local AI-Company-OS skill registry."""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "30_Skills" / "registry.yaml"
EXTERNAL_REQUIRED_FIELDS = (
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


def load_registry() -> dict[str, Any] | None:
    """Load registry YAML or print a friendly error."""
    if not REGISTRY_PATH.exists():
        logging.error("Registry fehlt: %s", REGISTRY_PATH.relative_to(ROOT))
        return None

    try:
        import yaml  # type: ignore[import-not-found]
    except ImportError:
        logging.error("PyYAML fehlt. Bitte installieren: python -m pip install PyYAML")
        return None

    try:
        loaded = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        logging.error("Registry YAML kann nicht geladen werden: %s", exc)
        return None

    if not isinstance(loaded, dict):
        logging.error("Registry YAML hat kein erwartetes Objektformat")
        return None

    return loaded


def extract_frontmatter(skill_path: Path) -> dict[str, str] | None:
    """Return frontmatter fields from a SKILL.md file."""
    text = skill_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return fields


def expected_folder_name(skill_path: Path) -> str:
    """Return the parent folder name for a skill path."""
    return skill_path.parent.name


def main() -> int:
    """Print a short registry overview and return a process exit code."""
    logging.info("Prüfe Skill Registry")

    registry = load_registry()
    if registry is None:
        return 1

    warnings: list[str] = []
    hints: list[str] = []
    errors: list[str] = []
    skills = registry.get("skills", [])
    external_sources = registry.get("external_sources", [])

    if not isinstance(skills, list):
        errors.append("`skills` ist keine Liste")
        skills = []

    for skill in skills:
        if not isinstance(skill, dict):
            errors.append("Ungültiger Skill-Eintrag in Registry")
            continue

        skill_id = str(skill.get("id", ""))
        skill_type = str(skill.get("type", ""))
        raw_path = str(skill.get("path", ""))

        if skill_type != "local":
            continue

        if not raw_path:
            errors.append(f"{skill_id}: Pfad fehlt")
            continue

        skill_path = ROOT / raw_path
        relative_path = skill_path.relative_to(ROOT)
        if not skill_path.exists():
            errors.append(f"{skill_id}: Pfad fehlt: {relative_path}")
            continue

        if skill_path.name != "SKILL.md":
            errors.append(f"{skill_id}: Datei heißt nicht SKILL.md: {relative_path}")

        if skill_id and skill_id != expected_folder_name(skill_path):
            warnings.append(
                f"{skill_id}: ID passt nicht zum Ordnernamen {expected_folder_name(skill_path)}"
            )

        frontmatter = extract_frontmatter(skill_path)
        if frontmatter is None:
            errors.append(f"{skill_id}: Frontmatter fehlt")
            continue

        if not frontmatter.get("name"):
            errors.append(f"{skill_id}: Frontmatter `name` fehlt")
        if not frontmatter.get("description"):
            errors.append(f"{skill_id}: Frontmatter `description` fehlt")

    if isinstance(external_sources, list):
        for source in external_sources:
            if not isinstance(source, dict):
                warnings.append("Ungültiger external_sources Eintrag")
                continue
            source_id = str(source.get("id", "external"))
            for field in EXTERNAL_REQUIRED_FIELDS:
                if field not in source:
                    warnings.append(f"{source_id}: externes Feld fehlt: {field}")
            source_text = str(source.get("source", ""))
            if "TODO" in source_text:
                hints.append(f"{source_id}: externe Quelle enthält TODO")
            review_file = str(source.get("review_file", ""))
            if review_file and not (ROOT / review_file).exists():
                warnings.append(f"{source_id}: Review-Datei fehlt: {review_file}")
            if "automatic_project_copy" not in source.get("blocked_use", []):
                warnings.append(f"{source_id}: automatic_project_copy sollte blockiert sein")
            if "script_execution" not in source.get("blocked_use", []):
                warnings.append(f"{source_id}: script_execution sollte blockiert sein")

    logging.info("OK: Registry YAML geladen")
    logging.info("OK: Lokale Skills geprüft: %d", len([s for s in skills if isinstance(s, dict) and s.get("type") == "local"]))

    logging.info("Warnungen: %d", len(warnings))
    for warning in warnings:
        logging.warning(warning)

    logging.info("Hinweise: %d", len(hints))
    for hint in hints:
        logging.info("Hinweis: %s", hint)

    logging.info("Fehler: %d", len(errors))
    for error in errors:
        logging.error(error)

    if errors:
        logging.error("Registry-Check nicht bestanden")
        return 1

    logging.info("Registry-Check bestanden")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
