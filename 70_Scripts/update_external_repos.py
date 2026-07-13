"""Update all cloned external repos under external_repos/<owner>/<repo>.

Two jobs in one run:

1. `git pull --ff-only` per repo and report which repos got new commits, so an
   agent knows where it is worth re-reading README/CHANGELOG.
2. Refresh the mechanical metadata in external_repos/INDEX.md automatically:
   file count, size, a detected "Struktur" hint (where skills/agents/commands
   live), the overview table, and the totals. This removes the manual
   find/du toil.

The ~200-word summaries stay untouched (they need human/LLM judgement). A
`Struktur` line ending in `<!-- manual -->` is treated as hand-authored and is
never overwritten — use it where a raw folder scan would mislead (e.g. source
in packages/ vs. generated .codex/ mirrors).

Flags:
  --repo <owner>/<repo>   only this repo (still refreshes the whole index)
  --index-only            skip git pull, only rescan + rewrite the index
  --no-index              only git pull, do not touch INDEX.md
  --dry-run               show what would change in INDEX.md, write nothing
"""

from __future__ import annotations

import argparse
import logging
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

ROOT = Path(__file__).resolve().parents[1]
EXTERNAL_ROOT = ROOT / "external_repos"
INDEX_PATH = EXTERNAL_ROOT / "INDEX.md"

# Folder basenames that signal where a repo's actual "intelligence" lives.
KEY_DIRS = ["skills", "agents", "commands", "hooks", "rules", "plugins", "references"]
KEY_DIR_SET = set(KEY_DIRS)


# --------------------------------------------------------------------------- #
# git pull
# --------------------------------------------------------------------------- #
def find_repos() -> list[Path]:
    """Find all <owner>/<repo> git checkouts under external_repos/."""
    if not EXTERNAL_ROOT.exists():
        return []
    return sorted(
        repo_dir
        for owner_dir in EXTERNAL_ROOT.iterdir()
        if owner_dir.is_dir()
        for repo_dir in owner_dir.iterdir()
        if repo_dir.is_dir() and (repo_dir / ".git").exists()
    )


def git_output(repo: Path, *args: str) -> str:
    """Run a git command in repo and return stripped stdout."""
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def pull_repo(repo: Path) -> tuple[str, str]:
    """Pull one repo. Returns (state, message) where state is new/unchanged/error."""
    label = repo.relative_to(EXTERNAL_ROOT).as_posix()
    try:
        before = git_output(repo, "rev-parse", "HEAD")
        git_output(repo, "pull", "--ff-only", "--quiet")
        after = git_output(repo, "rev-parse", "HEAD")
    except subprocess.CalledProcessError as exc:
        return "error", f"{label}: FEHLER beim Update ({exc.stderr.strip() or exc})"

    if before == after:
        return "unchanged", f"{label}: unverändert ({after[:8]})"
    return "new", f"{label}: NEU ({before[:8]} -> {after[:8]})"


# --------------------------------------------------------------------------- #
# scan (files / size / structure)
# --------------------------------------------------------------------------- #
def de_int(n: int) -> str:
    """Format an integer with German thousands separators (1234 -> '1.234')."""
    return f"{n:,}".replace(",", ".")


def human_size(num_bytes: int) -> str:
    """Format bytes into the K/M/G style used in the index (e.g. '9,8M')."""
    kb = num_bytes / 1024
    if kb < 1024:
        return f"{round(kb)}K"
    mb = kb / 1024
    if mb < 10:
        return f"{mb:.1f}".replace(".", ",") + "M"
    if mb < 1024:
        return f"{round(mb)}M"
    gb = mb / 1024
    return f"{gb:.1f}".replace(".", ",") + "G"


def scan_repo(repo: Path) -> tuple[int, int, str]:
    """Walk a repo (excluding .git) and return (file_count, size_bytes, struktur)."""
    file_count = 0
    size_bytes = 0
    skillmd_visible = 0
    key_visible: set[str] = set()
    mirror_roots: set[str] = set()

    for current, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d != ".git"]
        rel = os.path.relpath(current, repo)
        parts = [] if rel == "." else rel.split(os.sep)
        path_hidden = any(p.startswith(".") for p in parts)
        # docs/ subtrees hold documentation and translated copies (e.g.
        # docs/<lang>/skills/) — not the canonical source. Exclude them from
        # key-folder detection and SKILL.md counting so counts stay honest.
        path_doc = any(p.lower() == "docs" for p in parts)

        for d in dirs:
            if d.lower() in KEY_DIR_SET:
                full_parts = parts + [d]
                if any(p.lower() == "docs" for p in full_parts):
                    continue
                first_hidden = next((p for p in full_parts if p.startswith(".")), None)
                if first_hidden:
                    mirror_roots.add(first_hidden)
                else:
                    key_visible.add(d.lower())

        for f in files:
            file_count += 1
            try:
                size_bytes += os.path.getsize(os.path.join(current, f))
            except OSError:
                pass
            if f.lower() == "skill.md" and not path_hidden and not path_doc:
                skillmd_visible += 1

    struktur = render_struktur(skillmd_visible, key_visible, mirror_roots)
    return file_count, size_bytes, struktur


def render_struktur(
    skillmd: int,
    key_visible: set[str],
    mirror_roots: set[str],
) -> str:
    """Build a concise, human-readable structure hint from the scan results."""
    segments: list[str] = []
    if skillmd:
        segments.append(f"{de_int(skillmd)}× SKILL.md")

    visible = [k for k in KEY_DIRS if k in key_visible]
    if visible:
        segments.append("Ordner: " + ", ".join(visible))

    if not segments:
        # No skills and no canonical key folders: source code / CLI or pure docs.
        segments.append("keine Standard-Skill-/Agent-Ordner (Quellcode/CLI oder reine Doku)")

    if mirror_roots:
        shown = sorted(mirror_roots)
        label = ", ".join(shown[:4])
        if len(shown) > 4:
            label += f", … (+{len(shown) - 4})"
        segments.append(f"Spiegelordner: {label} (generiert)")

    return " · ".join(segments)


# --------------------------------------------------------------------------- #
# index rewriting
# --------------------------------------------------------------------------- #
def replace_field(section: str, field: str, new_line: str) -> tuple[str, bool]:
    """Replace a '- **field:** ...' bullet line within a repo section."""
    pattern = re.compile(rf"^- \*\*{re.escape(field)}:\*\*.*$", re.MULTILINE)
    if not pattern.search(section):
        return section, False
    # Function replacement avoids backslash/group-reference escaping in new_line.
    updated, count = pattern.subn(lambda _: new_line, section, count=1)
    return updated, count > 0 and updated != section


def upsert_field(section: str, field: str, new_line: str, after_field: str) -> tuple[str, bool]:
    """Replace an index field or insert it immediately after a known field."""
    field_pattern = re.compile(rf"^- \*\*{re.escape(field)}:\*\*.*$", re.MULTILINE)
    if field_pattern.search(section):
        return replace_field(section, field, new_line)

    anchor = re.search(rf"^- \*\*{re.escape(after_field)}:\*\*.*$", section, re.MULTILINE)
    if not anchor:
        return section, False
    return section[: anchor.end()] + "\n" + new_line + section[anchor.end() :], True


def update_index(
    scans: dict[str, tuple[int, int, str]],
    changed: set[str],
    today: str,
    dry_run: bool,
) -> bool:
    """Rewrite mechanical fields + overview in INDEX.md. Returns True if changed."""
    if not INDEX_PATH.exists():
        logging.error("INDEX.md fehlt: %s", INDEX_PATH)
        return False

    text = INDEX_PATH.read_text(encoding="utf-8")
    original = text
    notes: list[str] = []

    # --- per-repo sections ------------------------------------------------- #
    heading_re = re.compile(r"^## (\S+/\S+)$", re.MULTILINE)
    matches = list(heading_re.finditer(text))
    # Rebuild the text section by section (process from last to first to keep
    # earlier match offsets valid).
    for i in range(len(matches) - 1, -1, -1):
        label = matches[i].group(1)
        start = matches[i].start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        section = text[start:end]

        if label not in scans:
            continue
        file_count, size_bytes, struktur = scans[label]

        new_meta = f"- **Dateien:** {de_int(file_count)} · **Größe:** {human_size(size_bytes)}"
        section, _ = upsert_field(section, "Dateien", new_meta, "Zuletzt aktualisiert")

        # Struktur: only auto-update if not hand-pinned with <!-- manual -->.
        struktur_line = re.search(r"^- \*\*Struktur:\*\*.*$", section, re.MULTILINE)
        if not struktur_line:
            section, _ = upsert_field(section, "Struktur", f"- **Struktur:** {struktur}", "Dateien")
        elif "<!-- manual -->" not in struktur_line.group(0):
            section, _ = replace_field(section, "Struktur", f"- **Struktur:** {struktur}")

        # Zuletzt aktualisiert: bump only for repos that got new commits.
        if label in changed:
            section, _ = replace_field(
                section, "Zuletzt aktualisiert", f"- **Zuletzt aktualisiert:** {today}"
            )

        text = text[:start] + section + text[end:]

    # --- overview block ---------------------------------------------------- #
    overview = build_overview(scans, today)
    overview_re = re.compile(
        r"(<!-- OVERVIEW:START.*?-->\n).*?(\n<!-- OVERVIEW:END -->)",
        re.DOTALL,
    )
    if overview_re.search(text):
        text = overview_re.sub(lambda m: m.group(1) + overview + m.group(2), text)
    else:
        notes.append("OVERVIEW-Marker nicht gefunden — Übersicht nicht aktualisiert.")

    for note in notes:
        logging.warning(note)

    if text == original:
        logging.info("INDEX.md: keine Änderungen nötig.")
        return False

    if dry_run:
        logging.info("INDEX.md: Änderungen erkannt (dry-run, nichts geschrieben).")
        return True

    INDEX_PATH.write_text(text, encoding="utf-8")
    logging.info("INDEX.md aktualisiert.")
    return True


def build_overview(scans: dict[str, tuple[int, int, str]], today: str) -> str:
    """Render the overview block content (between the markers)."""
    total_files = sum(fc for fc, _, _ in scans.values())
    total_bytes = sum(sb for _, sb, _ in scans.values())
    total_mb = round(total_bytes / 1024 / 1024)

    rows = sorted(scans.items(), key=lambda kv: kv[1][1], reverse=True)
    lines = [
        "## Übersicht",
        "",
        f"- **Repos gesamt:** {len(scans)}",
        f"- **Gesamtgröße:** ca. {de_int(total_mb)} MB",
        f"- **Dateien gesamt:** ca. {de_int(total_files)} (ohne `.git`)",
        f"- **Stand:** {today}",
        "",
        "| Repo | Dateien | Größe |",
        "|---|---:|---:|",
    ]
    for label, (fc, sb, _) in rows:
        lines.append(f"| {label} | {de_int(fc)} | {human_size(sb)} |")
    lines.append("")
    lines.append(
        "Dateianzahl, Größe und Struktur pro Repo (ohne `.git`-Verzeichnis) stehen "
        "zusätzlich in jedem Eintrag unten und werden von "
        "`70_Scripts/update_external_repos.py` automatisch aufgefrischt."
    )
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def build_parser() -> argparse.ArgumentParser:
    """Create the CLI parser."""
    parser = argparse.ArgumentParser(
        description="Externe Repos aktualisieren (git pull) + INDEX.md-Metadaten auffrischen"
    )
    parser.add_argument(
        "--repo",
        help="Nur ein Repo pullen, Format <owner>/<repo> (Index wird trotzdem gesamt neu gescannt)",
    )
    parser.add_argument("--index-only", action="store_true", help="Kein git pull, nur Index neu scannen")
    parser.add_argument("--no-index", action="store_true", help="Nur git pull, INDEX.md nicht anfassen")
    parser.add_argument("--dry-run", action="store_true", help="Index-Änderungen nur anzeigen, nichts schreiben")
    return parser


def main() -> int:
    """Pull external repos and refresh INDEX.md metadata."""
    args = build_parser().parse_args()
    repos = find_repos()

    if not repos:
        logging.warning("Keine geklonten Repos unter external_repos/ gefunden.")
        return 0

    pull_targets = repos
    if args.repo:
        pull_targets = [r for r in repos if r.relative_to(EXTERNAL_ROOT).as_posix() == args.repo]
        if not pull_targets:
            logging.error("Repo nicht gefunden unter external_repos/: %s", args.repo)
            return 1

    changed: set[str] = set()
    failed: list[str] = []

    if not args.index_only:
        logging.info("Pull: %d Repo(s) ...", len(pull_targets))
        for repo in pull_targets:
            label = repo.relative_to(EXTERNAL_ROOT).as_posix()
            state, message = pull_repo(repo)
            if state == "error":
                failed.append(message)
                logging.error(message)
            else:
                logging.info(message)
                if state == "new":
                    changed.add(label)

    index_changed = False
    if not args.no_index:
        logging.info("Scan: Dateien/Größe/Struktur für %d Repo(s) ...", len(repos))
        scans: dict[str, tuple[int, int, str]] = {}
        for repo in repos:
            label = repo.relative_to(EXTERNAL_ROOT).as_posix()
            scans[label] = scan_repo(repo)
        index_changed = update_index(scans, changed, date.today().isoformat(), args.dry_run)

    logging.info(
        "Zusammenfassung: %d neu, %d Fehler, Index %s",
        len(changed),
        len(failed),
        "geändert" if index_changed else "unverändert",
    )
    if changed:
        logging.info("Reprüfen (README/CHANGELOG lesen, Zusammenfassung in INDEX.md prüfen):")
        for label in sorted(changed):
            logging.info("  - %s", label)

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
