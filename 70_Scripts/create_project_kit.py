"""Create a new project folder from a local project kit."""

from __future__ import annotations

import argparse
import logging
import shutil
from pathlib import Path
from typing import Any


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

ROOT = Path(__file__).resolve().parents[1]
KIT_ROOT = ROOT / "40_Project_Kits"
REGISTRY_PATH = ROOT / "30_Skills" / "registry.yaml"
CREATED_FROM = "ai-company-os"


def available_project_kits() -> list[Path]:
    """Return available project-kit directories."""
    if not KIT_ROOT.exists():
        return []
    return sorted(path for path in KIT_ROOT.iterdir() if path.is_dir())


def list_project_kits() -> None:
    """Print available project kits."""
    kits = available_project_kits()
    logging.info("Verfügbare Projekt-Kits: %d", len(kits))
    for kit in kits:
        logging.info("- %s", kit.name)


def parse_registry() -> dict[str, Any]:
    """Parse the registry fields needed by this script."""
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


def local_skills_for_project_type(project_type: str) -> list[dict[str, Any]]:
    """Return local copyable skills matching a project type."""
    registry = parse_registry()
    matches: list[dict[str, Any]] = []

    for skill in registry.get("skills", []):
        defaults = skill.get("default_for_project_types", [])
        if (
            skill.get("type") == "local"
            and skill.get("copy_to_project") is True
            and project_type in defaults
        ):
            matches.append(skill)

    return matches


def replace_placeholders(path: Path, project_name: str, project_type: str) -> None:
    """Replace supported placeholders in a copied text file."""
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return

    updated = (
        text.replace("{{PROJECT_NAME}}", project_name)
        .replace("{{PROJECT_TYPE}}", project_type)
        .replace("{{CREATED_FROM}}", CREATED_FROM)
    )
    if updated != text:
        path.write_text(updated, encoding="utf-8")


def copy_tree(
    source: Path,
    target: Path,
    project_name: str,
    project_type: str,
    force: bool,
) -> tuple[list[Path], list[Path]]:
    """Copy a kit tree and return copied and skipped target paths."""
    copied: list[Path] = []
    skipped: list[Path] = []

    for source_path in source.rglob("*"):
        relative_path = source_path.relative_to(source)
        target_path = target / relative_path

        if source_path.is_dir():
            target_path.mkdir(parents=True, exist_ok=True)
            continue

        if target_path.exists() and not force:
            skipped.append(target_path)
            continue

        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target_path)
        replace_placeholders(target_path, project_name, project_type)
        copied.append(target_path)

    return copied, skipped


def copy_project_skills(project_type: str, target: Path, force: bool) -> tuple[list[str], list[str]]:
    """Copy default local skills into the target project."""
    copied: list[str] = []
    skipped: list[str] = []
    skills_target = target / ".agents" / "skills"

    for skill in local_skills_for_project_type(project_type):
        skill_id = str(skill["id"])
        source = ROOT / str(skill["path"])
        destination = skills_target / skill_id / "SKILL.md"

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
    parser = argparse.ArgumentParser(description="Projekt-Kit kopieren")
    parser.add_argument("--list", action="store_true", help="Verfügbare Projekt-Kits anzeigen")
    parser.add_argument("--kit", help="Projekt-Kit auswählen")
    parser.add_argument("--name", help="Projektname")
    parser.add_argument("--target", help="Zielordner")
    parser.add_argument("--force", action="store_true", help="Bestehende Dateien überschreiben")
    parser.add_argument("--copy-skills", action="store_true", help="Passende lokale Skills kopieren")
    return parser


def main() -> int:
    """Run the project-kit CLI."""
    parser = build_parser()
    args = parser.parse_args()

    if args.list:
        list_project_kits()
        return 0

    if not args.kit or not args.name or not args.target:
        parser.error("--kit, --name und --target sind erforderlich, außer bei --list")

    source = KIT_ROOT / args.kit
    if not source.exists() or not source.is_dir():
        logging.error("Projekt-Kit nicht gefunden: %s", args.kit)
        list_project_kits()
        return 1

    target = Path(args.target).resolve()
    target.mkdir(parents=True, exist_ok=True)

    copied, skipped = copy_tree(source, target, args.name, args.kit, args.force)
    skill_copied: list[str] = []
    skill_skipped: list[str] = []
    if args.copy_skills:
        skill_copied, skill_skipped = copy_project_skills(args.kit, target, args.force)

    logging.info("Projekt-Kit: %s", args.kit)
    logging.info("Projektname: %s", args.name)
    logging.info("Ziel: %s", target)
    logging.info("Dateien kopiert: %d", len(copied))
    logging.info("Dateien übersprungen: %d", len(skipped))
    if args.copy_skills:
        logging.info("Skills kopiert: %s", ", ".join(skill_copied) or "keine")
        logging.info("Skills übersprungen: %s", ", ".join(skill_skipped) or "keine")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
