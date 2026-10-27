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


def run_subprocess(command: list[str], label: str, *, error_stream=None) -> int:
    """Run a command in the repository root with understandable errors."""
    try:
        result = subprocess.run(command, cwd=ROOT, check=False)
    except FileNotFoundError as error:
        print(f"{label} konnte nicht gestartet werden: {error.filename} wurde nicht gefunden.", file=error_stream)
        return 1
    except OSError as error:
        print(f"{label} konnte nicht gestartet werden: {error}", file=error_stream)
        return 1

    if result.returncode != 0:
        print(f"{label} wurde mit Fehler beendet (Exit {result.returncode}).", file=error_stream)
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


def run_wissen(args: argparse.Namespace) -> int:
    """Den lokalen Wissenskatalog ohne Modell- oder Netzwerkaufrufe bedienen."""
    if args.aktion in {"pilot-check", "karten", "kontext"}:
        command = [sys.executable, "-X", "utf8", script_path("wissens_pilot.py"), args.aktion]
        if args.aktion == "kontext":
            command.append(args.frage)
            if args.thema:
                command.extend(["--thema", args.thema])
        elif args.aktion == "karten" and args.check:
            command.append("--check")
        return run_subprocess(command, "Wissenspilot", error_stream=sys.stderr)
    command = [sys.executable, "-X", "utf8", script_path("wissen.py"), args.aktion]
    if args.aktion == "index":
        command.extend(["--max-bytes", str(args.max_bytes)])
        if args.progress:
            command.append("--progress")
    elif args.aktion == "suche":
        command.extend([args.frage, "--limit", str(args.limit)])
        for option in ("repo", "art"):
            value = getattr(args, option, None)
            if value:
                command.extend([f"--{option}", value])
    elif args.aktion == "analyse-plan":
        command.extend(["--ausgabe", args.ausgabe, "--budget", str(args.budget)])
    elif args.aktion == "analyse-check":
        command.extend(["--plan", args.plan, "--ergebnisse", args.ergebnisse])
    elif args.aktion == "lesen":
        command.extend([args.pfad, "--von", str(args.von)])
        if args.bis is not None:
            command.extend(["--bis", str(args.bis)])
    return run_subprocess(command, "Wissenskatalog")


def run_social(args: argparse.Namespace) -> int:
    """Build or check the local social-media directory."""
    command = [sys.executable, script_path("build_social_directory.py")]
    if args.check:
        command.append("--check")
    return run_subprocess(command, "KI-Kanalliste erstellen oder prüfen")


def run_repos(args: argparse.Namespace) -> int:
    """Build or verify the self-contained repository library."""
    command = [sys.executable, script_path("build_repo_library.py")]
    if args.aktion == "check":
        command.append("--check")
    return run_subprocess(command, "Repo-Bibliothek erstellen oder prüfen")


def run_quellen_statistik(args: argparse.Namespace) -> int:
    """Quellenbestand lokal auswerten und das HTML-Dashboard aktualisieren."""
    command = [sys.executable, "-X", "utf8", script_path("quellen_statistik.py")]
    if args.snapshot:
        command.append("--snapshot")
    for name in ("autor", "thema", "keyword", "bestand", "ausgabe"):
        value = getattr(args, name, None)
        if value:
            command.extend([f"--{name}", str(value)])
    return run_subprocess(command, "Quellenstatistik erstellen")


def run_quellen_feed(args: argparse.Namespace) -> int:
    """Quellenfeed bauen und optional den lokalen Server starten."""
    command = [sys.executable, "-X", "utf8", script_path("build_quellen_feed.py"), "--port", str(args.port)]
    if args.build:
        command.append("--build")
    if args.kopieren:
        command.append("--kopieren")
    if args.avatare_aktualisieren:
        command.append("--avatare-aktualisieren")
    if args.ausgabe:
        command.extend(["--ausgabe", args.ausgabe])
    return run_subprocess(command, "Quellenfeed erstellen")


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


def run_ingest(args: argparse.Namespace) -> int:
    """Archive an article, YouTube video or PDF in the source inbox."""
    command = [sys.executable, script_path("ingest_source.py"), args.eingabe]
    if args.typ != "auto":
        command.extend(["--typ", args.typ])
    if args.no_media:
        command.append("--no-media")
    if args.force:
        command.append("--force")
    if args.titel:
        command.extend(["--titel", args.titel])
    if args.no_whisper:
        command.append("--no-whisper")
    return run_subprocess(command, "Quelle erfassen")


def run_transcribe(args: argparse.Namespace) -> int:
    """Optionalen lokalen Audio-Fallback in seiner eigenen Umgebung ausführen."""
    executable = ROOT / ".venv" / "youtube-transcription" / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
    if not executable.is_file():
        print("Lokale Transkriptionsumgebung fehlt. Einrichtung: 00_Inbox/Quellen/README.md → Fehlende YouTube- und TikTok-Transkripte lokal nachholen")
        return 1
    command = [str(executable), "-X", "utf8", script_path("youtube_transcribe.py"), *args.eingaben,
               "--modell", args.modell, "--batch-size", str(args.batch_size), "--pause", str(args.pause)]
    if args.hls:
        command.append("--hls")
    if args.audio:
        command.extend(["--audio", args.audio])
    if args.titel:
        command.extend(["--titel", args.titel])
    return run_subprocess(command, "Video lokal transkribieren")


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


def run_feeds(args: argparse.Namespace) -> int:
    """Register feeds or list entries for the existing ingest workflow."""
    command = [sys.executable, script_path("feeds.py"), args.aktion]
    if args.aktion == "add":
        command.append(args.url)
        if args.name:
            command.extend(["--name", args.name])
    elif args.aktion == "check":
        command.extend(["--limit", str(args.limit)])
        if args.url:
            command.extend(["--url", args.url])
        if args.thema:
            command.extend(["--thema", args.thema])
        if args.alle:
            command.append("--alle")
        if args.ausgabe:
            command.extend(["--ausgabe", args.ausgabe])
    return run_subprocess(command, "Feeds verwalten")


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
        print("5) Quelle erfassen")
        print("6) Git-Status anzeigen")
        print("7) Beenden")
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
            eingabe = prompt_text("URL oder PDF-Pfad")
            return run_ingest(
                argparse.Namespace(
                    eingabe=eingabe,
                    typ="auto",
                    no_media=False,
                    force=False,
                    titel=None,
                )
            )
        if choice == "6":
            return run_status(argparse.Namespace())
        if choice == "7":
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

    wissen = subparsers.add_parser("wissen", help="Gesamtbestand durchsuchen und Wissensanalysen vorbereiten")
    wissen_sub = wissen.add_subparsers(dest="aktion", required=True)
    pilotcheck = wissen_sub.add_parser("pilot-check", help="Versionierte Aussagen und Fähigkeitskarten prüfen")
    pilotcheck.set_defaults(handler=run_wissen)
    pilotkarten = wissen_sub.add_parser("karten", help="Fähigkeitskandidaten aus der Pilot-Registry erzeugen")
    pilotkarten.add_argument("--check", action="store_true")
    pilotkarten.set_defaults(handler=run_wissen)
    pilotkontext = wissen_sub.add_parser("kontext", help="Aussagen, Spannungen und Kandidaten aus dem semantischen Pilot abrufen")
    pilotkontext.add_argument("frage")
    pilotkontext.add_argument("--thema", help="Explizite Synthese-ID aus der Pilot-Registry")
    pilotkontext.set_defaults(handler=run_wissen)
    wissensindex = wissen_sub.add_parser("index", help="Lokalen Katalog einschließlich externer Repos erzeugen")
    wissensindex.add_argument("--max-bytes", type=int, default=1_000_000)
    wissensindex.add_argument("--progress", action="store_true")
    wissensindex.set_defaults(handler=run_wissen)
    wissensstatus = wissen_sub.add_parser("status", help="Abdeckung des gespeicherten Katalogs anzeigen")
    wissensstatus.set_defaults(handler=run_wissen)
    wissenssuche = wissen_sub.add_parser("suche", help="Abschnitte mit Quellen und Versionsständen finden")
    wissenssuche.add_argument("frage")
    wissenssuche.add_argument("--limit", type=int, default=10)
    wissenssuche.add_argument("--repo")
    wissenssuche.add_argument("--art")
    wissenssuche.set_defaults(handler=run_wissen)
    wissenslesen = wissen_sub.add_parser("lesen", help="Textbereich eines Treffers mit geprüftem Hash nachladen")
    wissenslesen.add_argument("pfad")
    wissenslesen.add_argument("--von", type=int, default=1)
    wissenslesen.add_argument("--bis", type=int)
    wissenslesen.set_defaults(handler=run_wissen)
    wissensplan = wissen_sub.add_parser("analyse-plan", help="Offene Prüfpakete für alle indexierten Inhalte planen")
    wissensplan.add_argument("--ausgabe", required=True)
    wissensplan.add_argument("--budget", type=int, default=60000)
    wissensplan.set_defaults(handler=run_wissen)
    wissenscheck = wissen_sub.add_parser("analyse-check", help="Bearbeitungsnachweise gegen einen Gesamtprüfplan prüfen")
    wissenscheck.add_argument("--plan", required=True)
    wissenscheck.add_argument("--ergebnisse", required=True)
    wissenscheck.set_defaults(handler=run_wissen)

    quellen = subparsers.add_parser("quellen", help="Quellenbestand auswerten")
    quellen_sub = quellen.add_subparsers(dest="aktion", required=True)
    statistik = quellen_sub.add_parser("statistik", help="HTML, JSON und Markdown erzeugen")
    statistik.add_argument("--snapshot", action="store_true", help="Bestandsmessung für den Verlauf speichern")
    statistik.add_argument("--autor")
    statistik.add_argument("--thema")
    statistik.add_argument("--keyword")
    statistik.add_argument("--bestand", choices=["raw", "sources"], default="raw")
    statistik.add_argument("--ausgabe", help="Anderer Ausgabeordner")
    statistik.set_defaults(handler=run_quellen_statistik)

    feed = quellen_sub.add_parser("feed", help="Originalquellen im lokalen chronologischen Feed lesen")
    feed.add_argument("--build", action="store_true", help="Nur die statische Website erzeugen")
    feed.add_argument("--port", type=int, default=8766, help="Lokaler Port (Standard: 8766)")
    feed.add_argument("--ausgabe", help="Anderer Ausgabeordner")
    feed.add_argument("--kopieren", action="store_true", help="Medien kopieren statt Hardlinks verwenden")
    feed.add_argument("--avatare-aktualisieren", action="store_true", help="Fehlende Profilbilder öffentlich abrufen und lokal speichern")
    feed.set_defaults(handler=run_quellen_feed)

    social = subparsers.add_parser("social", help="Lokale HTML-Liste der KI-Kanäle erstellen")
    social.add_argument("--check", action="store_true", help="HTML-Liste auf Aktualität prüfen")
    social.set_defaults(handler=run_social)

    repos = subparsers.add_parser("repos", help="Offline-HTML der Repo-Bibliothek erstellen oder prüfen")
    repos.add_argument("aktion", choices=["build", "check"], nargs="?", default="build")
    repos.set_defaults(handler=run_repos)

    external = subparsers.add_parser("external", help="Externe Skills prüfen")
    external.add_argument("--source", help="Nur eine externe Quelle per ID prüfen")
    external.set_defaults(handler=run_external)

    ingest = subparsers.add_parser(
        "ingest", help="Artikel, YouTube-Video oder PDF als Quelle erfassen"
    )
    ingest.add_argument("eingabe", help="URL oder Pfad zu einer PDF")
    ingest.add_argument(
        "--typ", choices=["auto", "url", "youtube", "pdf"], default="auto"
    )
    ingest.add_argument("--no-media", action="store_true", help="Keine Bilder laden")
    ingest.add_argument("--force", action="store_true", help="Bestehende Notiz überschreiben")
    ingest.add_argument("--titel", help="Automatisch erkannten Titel überschreiben")
    ingest.add_argument("--no-whisper", action="store_true", help="Kein lokaler Whisper-Fallback bei fehlenden Untertiteln")
    ingest.set_defaults(handler=run_ingest)

    transcribe = subparsers.add_parser("transkribieren", help="Fehlende YouTube-/TikTok-Transkripte lokal aus Audio ergänzen")
    transcribe.add_argument("eingaben", nargs="+", help="YouTube-/TikTok-IDs oder URLs")
    transcribe.add_argument("--audio", help="Vorhandene Tonspur für ein Video")
    transcribe.add_argument("--modell", default="large-v3")
    transcribe.add_argument("--batch-size", type=int, default=4)
    transcribe.add_argument("--pause", type=float, default=10)
    transcribe.add_argument("--hls", action="store_true", help="Alternative HLS-Tonspur bei HTTP 403 verwenden")
    transcribe.add_argument("--titel", help="Titel beim erstmaligen Anlegen der YouTube-Rohquelle")
    transcribe.set_defaults(handler=run_transcribe)

    feeds = subparsers.add_parser("feeds", help="RSS-/Atom-Feeds registrieren und prüfen")
    feeds_sub = feeds.add_subparsers(dest="aktion", required=True)
    feeds_add = feeds_sub.add_parser("add", help="Feed registrieren")
    feeds_add.add_argument("url")
    feeds_add.add_argument("--name", help="Anzeigename")
    feeds_add.set_defaults(handler=run_feeds)
    feeds_list = feeds_sub.add_parser("list", help="Feeds anzeigen")
    feeds_list.set_defaults(handler=run_feeds)
    feeds_check = feeds_sub.add_parser("check", help="Thematisch passende Artikel vorschlagen")
    feeds_check.add_argument("--url", help="Nur diesen Feed prüfen")
    feeds_check.add_argument("--limit", type=int, default=10, help="Einträge pro Feed")
    feeds_check.add_argument("--thema", help="Themencluster-ID, z. B. verifikation")
    feeds_check.add_argument("--alle", action="store_true", help="Alle offenen Einträge nach Datum anzeigen")
    feeds_check.add_argument("--ausgabe", help="Vorauswahl als Markdown speichern")
    feeds_check.set_defaults(handler=run_feeds)

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
