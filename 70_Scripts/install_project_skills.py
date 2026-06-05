"""Install local skills from this repository into a target project."""

from __future__ import annotations

import argparse
import logging
import shutil
from pathlib import Path
from typing import Any


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "30_Skills" / "registry.yaml"


def parse_registry() -> dict[str, Any]:
    """Parse registry skill fields."""
    if not REGISTRY_PATH.exists():
        return {"skills": []}

    try:
        import yaml  # type: ignore[import-not-found]

        loaded = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
        if isinstance(loaded, dict):
            return loaded
    except ImportError:
        pass

    skills: list[dict[str, Any]] = []
    section = ""
    current: dict[str, Any] | None = None
    active_list_field = ""

    for raw_line in REGISTRY_PATH.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        if not raw_line.startswith(" "):
            section = raw_line.rstrip(":")
            current = None
            active_list_field = ""
            continue

        stripped = raw_line.strip()
        if section != "skills":
            continue

        if stripped.startswith("- id:"):
            current = {"id": stripped.split(":", 1)[1].strip()}
            skills.append(current)
            active_list_field = ""
            continue

        if current is None:
            continue

        if stripped.startswith("- ") and active_list_field:
            current.setdefault(active_list_field, []).append(stripped[2:].strip())
            continue

        if ":" not in stripped:
            continue

        key, value = stripped.split(":", 1)
        value = value.strip()
        active_list_field = ""

        if value == "[]":
            current[key] = []
        elif not value:
            current[key] = []
            active_list_field = key
        elif value in {"true", "false"}:
            current[key] = value == "true"
        elif value.startswith("[") and value.endswith("]"):
            current[key] = [
                item.strip().strip('"')
                for item in value[1:-1].split(",")
                if item.strip()
            ]
        else:
            current[key] = value.strip('"')

    return {"skills": skills}


def local_skills() -> list[dict[str, Any]]:
    """Return all local skills from the registry."""
    return [
        skill
        for skill in parse_registry().get("skills", [])
        if skill.get("type") == "local"
    ]


def skills_for_project_type(project_type: str) -> list[dict[str, Any]]:
    """Return copyable default skills for a project type."""
    return [
        skill
        for skill in local_skills()
        if skill.get("copy_to_project") is True
        and project_type in skill.get("default_for_project_types", [])
    ]


def selected_skills(skill_ids: list[str]) -> tuple[list[dict[str, Any]], list[str]]:
    """Return explicitly selected local skills and unknown ids."""
    by_id = {str(skill["id"]): skill for skill in local_skills()}
    found: list[dict[str, Any]] = []
    missing: list[str] = []

    for skill_id in skill_ids:
        skill = by_id.get(skill_id)
        if skill is None:
            missing.append(skill_id)
        else:
            found.append(skill)

    return found, missing


def copy_skills(skills: list[dict[str, Any]], target: Path, force: bool) -> tuple[list[str], list[str]]:
    """Copy selected skills into the target project."""
    copied: list[str] = []
    skipped: list[str] = []

    for skill in skills:
        skill_id = str(skill["id"])
        source = ROOT / str(skill["path"])
        destination = target / ".agents" / "skills" / skill_id / "SKILL.md"

        if not source.exists():
            skipped.append(f"{skill_id} (Quelle fehlt)")
            continue

        if destination.exists() and not force:
            skipped.append(skill_id)
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        copied.append(skill_id)

    return copied, skipped


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(description="Lokale Skills in ein Projekt kopieren")
    parser.add_argument("--list", action="store_true", help="Lokale Skills anzeigen")
    parser.add_argument("--project-type", help="Projektart für Default-Skills")
    parser.add_argument("--skills", nargs="+", help="Explizite Skill-IDs")
    parser.add_argument("--target", help="Zielprojekt")
    parser.add_argument("--force", action="store_true", help="Bestehende Skills überschreiben")
    return parser


def main() -> int:
    """Run the skill installer CLI."""
    parser = build_parser()
    args = parser.parse_args()

    if args.list:
        for skill in local_skills():
            default_types = ", ".join(skill.get("default_for_project_types", [])) or "-"
            logging.info("%s | defaults: %s", skill.get("id"), default_types)
        return 0

    if not args.target:
        parser.error("--target ist erforderlich")

    if args.skills:
        skills, missing = selected_skills(args.skills)
        for skill_id in missing:
            logging.error("Skill nicht gefunden oder nicht lokal: %s", skill_id)
        if missing:
            return 1
    elif args.project_type:
        skills = skills_for_project_type(args.project_type)
        if not skills:
            logging.error("Keine lokalen Default-Skills für Projektart: %s", args.project_type)
            return 1
    else:
        parser.error("--project-type oder --skills ist erforderlich")

    target = Path(args.target).resolve()
    target.mkdir(parents=True, exist_ok=True)
    copied, skipped = copy_skills(skills, target, args.force)

    logging.info("Ziel: %s", target)
    logging.info("Kopiert: %s", ", ".join(copied) or "keine")
    logging.info("Übersprungen: %s", ", ".join(skipped) or "keine")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
