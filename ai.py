"""User-friendly root CLI for the AI-Company-OS."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Sequence


ROOT = Path(__file__).resolve().parent
SCRIPT_ROOT = ROOT / "70_Scripts"
PROJECT_KITS = {
    "1": "saas-webapp",
    "2": "shopify-app",
    "3": "website-redesign",
}


def script_path(name: str) -> str:
    """Return an absolute path to a script in 70_Scripts."""
    return str(SCRIPT_ROOT / name)


def run_subprocess(command: list[str], label: str) -> int:
    """Run a command in the repository root with understandable errors."""
    try:
        result = subprocess.run(command, cwd=ROOT, check=False)
    except FileNotFoundError as error:
        print(f"{label} konnte nicht gestartet werden: {error.filename} wurde nicht gefunden.")
        return 1
    except OSError as error:
        print(f"{label} konnte nicht gestartet werden: {error}")
        return 1

    if result.returncode != 0:
        print(f"{label} wurde mit Fehler beendet (Exit {result.returncode}).")
    return result.returncode


def prompt_choice(prompt: str, choices: dict[str, str]) -> str:
    """Prompt until the user selects one of the available choices."""
    while True:
        value = input(prompt).strip()
        selected = choices.get(value)
        if selected:
            return selected
        print("Bitte eine gültige Option wählen.")


def prompt_text(prompt: str, default: str | None = None) -> str:
    """Prompt for text and optionally use a default."""
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt}{suffix}: ").strip()
    if value:
        return value
    if default is not None:
        return default
    print("Dieser Wert ist erforderlich.")
    return prompt_text(prompt, default)


def prompt_yes_no(prompt: str, default: bool) -> bool:
    """Prompt for a yes/no answer."""
    default_hint = "J/n" if default else "j/N"
    while True:
        value = input(f"{prompt} [{default_hint}]: ").strip().lower()
        if not value:
            return default
        if value in {"j", "ja", "y", "yes"}:
            return True
        if value in {"n", "nein", "no"}:
            return False
        print("Bitte mit ja oder nein antworten.")


def run_health(_args: argparse.Namespace) -> int:
    """Run the central health check."""
    return run_subprocess(
        [sys.executable, script_path("company_os_healthcheck.py")],
        "Health Check",
    )


def run_status(_args: argparse.Namespace) -> int:
    """Show git status in short format."""
    if shutil.which("git") is None:
        print("Git ist nicht verfügbar. Bitte Git installieren oder den Status manuell prüfen.")
        return 1
    return run_subprocess(["git", "status", "--short"], "Git-Status")


def run_external(args: argparse.Namespace) -> int:
    """Run the external skill review."""
    command = [sys.executable, script_path("external_skill_review.py")]
    if args.source:
        command.extend(["--source", args.source])
    return run_subprocess(command, "Externe Skills prüfen")


def run_skills(args: argparse.Namespace) -> int:
    """List or install local project skills."""
    command = [sys.executable, script_path("install_project_skills.py")]
    if not args.project_type and not args.skills:
        command.append("--list")
    else:
        if not args.target:
            print("--target ist erforderlich, wenn Skills installiert werden.")
            return 1
        if args.project_type:
            command.extend(["--project-type", args.project_type])
        if args.skills:
            command.append("--skills")
            command.extend(args.skills)
        command.extend(["--target", args.target])
        if args.force:
            command.append("--force")

    return run_subprocess(command, "Skills anzeigen oder installieren")


def print_project_created(name: str, target: str) -> None:
    """Print next steps after a project was created."""
    print()
    print("Projekt wurde erstellt.")
    print()
    print("Nächste Schritte:")
    print(f"cd {target}")
    print("git init")
    print("git add .")
    print(f'git commit -m "Initialisiere {name}"')


def build_new_command(
    kit: str,
    name: str,
    target: str,
    copy_skills: bool,
    force: bool,
) -> list[str]:
    """Build the create_project_kit.py command."""
    command = [
        sys.executable,
        script_path("create_project_kit.py"),
        "--kit",
        kit,
        "--name",
        name,
        "--target",
        target,
    ]
    if copy_skills:
        command.append("--copy-skills")
    if force:
        command.append("--force")
    return command


def run_new(args: argparse.Namespace) -> int:
    """Create a new project through the project-kit script."""
    has_options = any([args.kit, args.name, args.target, args.copy_skills, args.force])
    if not has_options:
        print("Projektart:")
        print("1) SaaS Webapp")
        print("2) Shopify App")
        print("3) Website-Redesign")
        kit = prompt_choice("Auswahl: ", PROJECT_KITS)
        name = prompt_text("Projektname")
        target = prompt_text("Zielordner", f"../{name}")
        copy_skills = prompt_yes_no("Skills kopieren?", True)
        force = prompt_yes_no("Überschreiben mit --force?", False)
    else:
        if not args.kit or not args.name or not args.target:
            print("--kit, --name und --target sind erforderlich, außer im interaktiven Wizard.")
            return 1
        kit = args.kit
        name = args.name
        target = args.target
        copy_skills = args.copy_skills
        force = args.force

    result = run_subprocess(
        build_new_command(kit, name, target, copy_skills, force),
        "Projekt erstellen",
    )
    if result == 0:
        print_project_created(name, target)
    return result


def run_menu() -> int:
    """Show the interactive root menu."""
    while True:
        print("AI-Company-OS")
        print()
        print("1) Neues Projekt erstellen")
        print("2) Health Check ausführen")
        print("3) Skills anzeigen oder installieren")
        print("4) Externe Skills prüfen")
        print("5) Git-Status anzeigen")
        print("6) Beenden")
        choice = input("Auswahl: ").strip()

        if choice == "1":
            return run_new(argparse.Namespace(kit=None, name=None, target=None, copy_skills=False, force=False))
        if choice == "2":
            return run_health(argparse.Namespace())
        if choice == "3":
            return run_skills(argparse.Namespace(project_type=None, skills=None, target=None, force=False))
        if choice == "4":
            return run_external(argparse.Namespace(source=None))
        if choice == "5":
            return run_status(argparse.Namespace())
        if choice == "6":
            return 0
        print("Bitte eine gültige Option wählen.")
        print()


def build_parser() -> argparse.ArgumentParser:
    """Create the root CLI argument parser."""
    parser = argparse.ArgumentParser(description="AI-Company-OS bedienen")
    subparsers = parser.add_subparsers(dest="command")

    health = subparsers.add_parser("health", help="Health Check ausführen")
    health.set_defaults(handler=run_health)

    status = subparsers.add_parser("status", help="Git-Status anzeigen")
    status.set_defaults(handler=run_status)

    external = subparsers.add_parser("external", help="Externe Skills prüfen")
    external.add_argument("--source", help="Nur eine externe Quelle per ID prüfen")
    external.set_defaults(handler=run_external)

    skills = subparsers.add_parser("skills", help="Skills anzeigen oder installieren")
    skills.add_argument("--project-type", help="Projektart für Default-Skills")
    skills.add_argument("--skills", nargs="+", help="Explizite Skill-IDs")
    skills.add_argument("--target", help="Zielprojekt")
    skills.add_argument("--force", action="store_true", help="Bestehende Skills überschreiben")
    skills.set_defaults(handler=run_skills)

    new = subparsers.add_parser("new", help="Neues Projekt erstellen")
    new.add_argument("--kit", choices=sorted(PROJECT_KITS.values()), help="Projekt-Kit auswählen")
    new.add_argument("--name", help="Projektname")
    new.add_argument("--target", help="Zielordner")
    new.add_argument("--copy-skills", action="store_true", help="Passende lokale Skills kopieren")
    new.add_argument("--force", action="store_true", help="Bestehende Dateien überschreiben")
    new.set_defaults(handler=run_new)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the AI-Company-OS CLI."""
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        return run_menu()

    parser = build_parser()
    args = parser.parse_args(list(argv))
    handler = getattr(args, "handler", None)
    if handler is None:
        parser.print_help()
        return 0
    return int(handler(args))


if __name__ == "__main__":
    raise SystemExit(main())
