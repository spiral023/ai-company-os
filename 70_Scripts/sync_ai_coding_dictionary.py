"""AI Coding Dictionary (Matt Pocock / AI Hero) in den Quellen-Eingang spiegeln.

Quelle ist der lokale Klon des GitHub-Repos, nicht die Website:

    external_repos/mattpocock/dictionary-of-ai-coding/
        dictionary/<Begriff>.md        ← ein Eintrag pro Begriff
        internal/Curriculum.md         ← Sektionen und Reihenfolge

Ziel ist eine Ordnerstruktur wie auf https://www.aihero.dev/ai-coding-dictionary:

    00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/
        00-index.md                    ← Übersicht, trägt `status` für die ganze Sammlung
        01-the-model/Parameters.md
        03-tools-environment/MCP.md
        ...

Die Querverweise der Einträge (`./Harness.md`) werden auf die Sektionsordner
umgeschrieben, damit sie in Obsidian und auf GitHub funktionieren. Die
Begriffsdateien tragen bewusst kein `status`-Feld: Die Sammlung ist eine Quelle,
nicht 71.

Update-Ablauf:

    git -C external_repos/mattpocock/dictionary-of-ai-coding pull --ff-only
    python 70_Scripts/sync_ai_coding_dictionary.py

Begriffsdateien sind reine Spiegel und werden bei Änderungen neu geschrieben.
Im Index bleiben `status`, `source_notiz`, `notiz` und `erfasst` erhalten.
Entfernte Begriffe werden nur gemeldet, nie gelöscht.

Das Dictionary-Repo hat keine Lizenzdatei, dieses Repo ist öffentlich: Der
Zielordner steht deshalb in `.gitignore` und existiert nur lokal.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
import urllib.parse
from dataclasses import dataclass
from pathlib import Path

# Konsistente Ausgabe in PowerShell, Pipes und Agent-Terminals unter Windows.
for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parents[1]
QUELLE = REPO_ROOT / "external_repos" / "mattpocock" / "dictionary-of-ai-coding"
ZIEL = REPO_ROOT / "00_Inbox" / "Quellen" / "URL" / "aihero-ai-coding-dictionary"
INDEX_NAME = "00-index.md"

WEB_BASIS = "https://www.aihero.dev/ai-coding-dictionary"
REPO_URL = "https://github.com/mattpocock/dictionary-of-ai-coding"
AUTOR = "Matt Pocock"

# Felder im Index, die nach dem Erfassen von Hand oder von quellen-verarbeiten
# gepflegt werden und ein erneuter Sync nicht überschreiben darf.
INDEX_ERHALTEN = ("status", "source_notiz", "notiz", "erfasst")

SEKTION_RE = re.compile(r"^##\s+Section\s+(\d+)\s+[—-]\s+(.+?)\s*$")
EINTRAG_RE = re.compile(r"^-\s+(.+?)\s*$")
LINK_RE = re.compile(r"\]\(\./([^)#]+?\.md)(#[^)]*)?\)")


@dataclass
class Begriff:
    name: str
    sektion_nr: int
    sektion: str
    ordner: str
    datei: Path  # Quelldatei im Repo


def slugify(wert: str) -> str:
    wert = wert.lower().replace("&", " ")
    return re.sub(r"[^a-z0-9]+", "-", wert).strip("-")


def web_slug(name: str) -> str:
    # Entspricht den Website-Pfaden: "AGENTS.md" → agents-md,
    # "Next-token prediction" → next-token-prediction.
    return slugify(name)


def git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(QUELLE), *args],
        capture_output=True, text=True, encoding="utf-8", check=True,
    ).stdout.strip()


def yaml_str(wert: str) -> str:
    return '"' + wert.replace("\\", "\\\\").replace('"', '\\"') + '"'


def trenne_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    ende = text.find("\n---\n", 4)
    if ende == -1:
        return {}, text
    felder: dict[str, str] = {}
    for zeile in text[4:ende].splitlines():
        if ":" in zeile and not zeile.startswith(" "):
            key, _, wert = zeile.partition(":")
            felder[key.strip()] = wert.strip()
    return felder, text[ende + 5:]


def unquote_yaml(wert: str) -> str:
    if len(wert) >= 2 and wert[0] == wert[-1] == '"':
        return wert[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    return wert


def lies_curriculum() -> list[Begriff]:
    begriffe: list[Begriff] = []
    nr, titel = 0, ""
    for zeile in (QUELLE / "internal" / "Curriculum.md").read_text(encoding="utf-8").splitlines():
        if m := SEKTION_RE.match(zeile):
            nr, titel = int(m.group(1)), m.group(2)
        elif nr and (m := EINTRAG_RE.match(zeile)):
            name = m.group(1)
            begriffe.append(Begriff(
                name=name,
                sektion_nr=nr,
                sektion=titel,
                ordner=f"{nr:02d}-{slugify(titel)}",
                datei=QUELLE / "dictionary" / f"{name}.md",
            ))
    return begriffe


def link_ziel(von: Begriff, nach: Begriff) -> str:
    datei = urllib.parse.quote(nach.datei.name)
    return f"./{datei}" if von.ordner == nach.ordner else f"../{nach.ordner}/{datei}"


def schreibe_links_um(text: str, von: Begriff, nach_datei: dict[str, Begriff]) -> tuple[str, list[str]]:
    unbekannt: list[str] = []

    def ersetze(m: re.Match[str]) -> str:
        dateiname = urllib.parse.unquote(m.group(1))
        ziel = nach_datei.get(dateiname)
        if ziel is None:
            unbekannt.append(dateiname)
            return m.group(0)
        return f"]({link_ziel(von, ziel)}{m.group(2) or ''})"

    return LINK_RE.sub(ersetze, text), unbekannt


def baue_begriff(b: Begriff, nach_datei: dict[str, Begriff], commit: str, erfasst: str) -> tuple[str, str, list[str]]:
    felder, body = trenne_frontmatter(b.datei.read_text(encoding="utf-8"))
    body, unbekannt = schreibe_links_um(body.strip(), b, nach_datei)
    beschreibung = unquote_yaml(felder.get("description", ""))
    datum = git("log", "-1", "--format=%cs", "--", f"dictionary/{b.datei.name}")
    url = f"{WEB_BASIS}/{web_slug(b.name)}"
    kopf = [
        "---",
        f"url: {url}",
        f"begriff: {yaml_str(b.name)}",
        f"beschreibung: {yaml_str(beschreibung)}",
        f"kategorie: {yaml_str(b.sektion)}",
        f"autor: {yaml_str(AUTOR)}",
        f"datum: {datum}",
        f"erfasst: {erfasst}",
        "typ: url",
        "quelle: url",
        f"teil_von: {yaml_str('AI Coding Dictionary')}",
        f"repo: {REPO_URL}",
        f"repo_pfad: {yaml_str('dictionary/' + b.datei.name)}",
        f"commit: {commit}",
        "---",
        "",
        f"# {b.name}",
        "",
        f"> Teil des [AI Coding Dictionary](../{INDEX_NAME}) · Sektion {b.sektion_nr}: {b.sektion} · [Online]({url})",
        "",
        body,
        "",
    ]
    return "\n".join(kopf), beschreibung, unbekannt


def baue_index(begriffe: list[Begriff], beschreibungen: dict[str, str], commit: str,
               datum: str, erhalten: dict[str, str]) -> str:
    kopf = [
        "---",
        f"url: {WEB_BASIS}",
        f"titel: {yaml_str('AI Coding Dictionary')}",
        f"autor: {yaml_str(AUTOR)}",
        f"datum: {datum}",
        f"erfasst: {erhalten.get('erfasst', dt.date.today().isoformat())}",
        "typ: url",
        "quelle: url",
        f"status: {erhalten.get('status', 'neu')}",
    ]
    for feld in ("source_notiz", "notiz"):
        if feld in erhalten:
            kopf.append(f"{feld}: {erhalten[feld]}")
    kopf += [
        f"repo: {REPO_URL}",
        f"commit: {commit}",
        f"begriffe: {len(begriffe)}",
        "---",
        "",
        "# AI Coding Dictionary",
        "",
        f"> Gespiegelt aus [{REPO_URL.removeprefix('https://github.com/')}]({REPO_URL}) "
        f"(Commit `{commit[:7]}`) per `python 70_Scripts/sync_ai_coding_dictionary.py`. "
        f"Online: [{WEB_BASIS.removeprefix('https://www.')}]({WEB_BASIS})",
        "",
        f"Nachschlagewerk von {AUTOR} (AI Hero): {len(begriffe)} Begriffe der KI-gestützten "
        "Softwareentwicklung in einfachem Englisch, in sieben Sektionen. Jeder Eintrag folgt "
        "demselben Aufbau: Definition, Mechanik, woran man das Problem erkennt, kurzer Usage-Dialog.",
        "",
        "Das Repo hat keine Lizenzdatei (alle Rechte vorbehalten). Die Kopie ist "
        "nur lokal (per `.gitignore` ausgeschlossen); Inhalte nicht wörtlich in eigene, "
        "versionierte Artefakte übernehmen.",
        "",
    ]
    aktuell = 0
    for b in begriffe:
        if b.sektion_nr != aktuell:
            aktuell = b.sektion_nr
            if kopf[-1]:
                kopf.append("")
            kopf += [f"## {b.sektion_nr}. {b.sektion}", ""]
        pfad = f"./{b.ordner}/{urllib.parse.quote(b.datei.name)}"
        kopf.append(f"- [{b.name}]({pfad}) — {beschreibungen[b.name]}")
    kopf.append("")
    return "\n".join(kopf)


def schreibe(pfad: Path, inhalt: str, dry_run: bool) -> str:
    if pfad.exists() and pfad.read_text(encoding="utf-8") == inhalt:
        return "unverändert"
    art = "geändert" if pfad.exists() else "neu"
    if not dry_run:
        pfad.parent.mkdir(parents=True, exist_ok=True)
        pfad.write_text(inhalt, encoding="utf-8", newline="\n")
    return art


def main() -> int:
    parser = argparse.ArgumentParser(description="AI Coding Dictionary nach 00_Inbox/Quellen/URL/ spiegeln")
    parser.add_argument("--dry-run", action="store_true", help="nur anzeigen, nichts schreiben")
    args = parser.parse_args()

    if not (QUELLE / "dictionary").is_dir():
        print(f"Repo fehlt: {QUELLE}\n  git clone {REPO_URL} {QUELLE.relative_to(REPO_ROOT).as_posix()}")
        return 1

    begriffe = lies_curriculum()
    nach_datei = {b.datei.name: b for b in begriffe}
    fehler = [b.name for b in begriffe if not b.datei.exists()]
    if fehler:
        print("Im Curriculum, aber ohne Datei:", ", ".join(fehler))
        return 1
    nicht_einsortiert = sorted(p.name for p in (QUELLE / "dictionary").glob("*.md") if p.name not in nach_datei)
    if nicht_einsortiert:
        print("Warnung: Datei ohne Curriculum-Eintrag, nicht gespiegelt:", ", ".join(nicht_einsortiert))

    commit = git("rev-parse", "HEAD")
    datum = git("log", "-1", "--format=%cs")
    heute = dt.date.today().isoformat()

    index_pfad = ZIEL / INDEX_NAME
    erhalten: dict[str, str] = {}
    if index_pfad.exists():
        felder, _ = trenne_frontmatter(index_pfad.read_text(encoding="utf-8"))
        erhalten = {k: v for k, v in felder.items() if k in INDEX_ERHALTEN}

    zaehler: dict[str, int] = {"neu": 0, "geändert": 0, "unverändert": 0}
    beschreibungen: dict[str, str] = {}
    geschrieben: set[Path] = set()
    for b in begriffe:
        ziel = ZIEL / b.ordner / b.datei.name
        erfasst = heute
        if ziel.exists():
            erfasst = trenne_frontmatter(ziel.read_text(encoding="utf-8"))[0].get("erfasst", heute)
        inhalt, beschreibungen[b.name], unbekannt = baue_begriff(b, nach_datei, commit, erfasst)
        for u in unbekannt:
            print(f"Warnung: {b.name} verlinkt auf unbekannte Datei {u}")
        art = schreibe(ziel, inhalt, args.dry_run)
        zaehler[art] += 1
        geschrieben.add(ziel.resolve())
        if art != "unverändert":
            print(f"{art:>11}  {b.ordner}/{b.datei.name}")

    art = schreibe(index_pfad, baue_index(begriffe, beschreibungen, commit, datum, erhalten), args.dry_run)
    print(f"{art:>11}  {INDEX_NAME}")

    verwaist = sorted(
        p.relative_to(ZIEL).as_posix() for p in ZIEL.glob("*/*.md")
        if p.resolve() not in geschrieben
    ) if ZIEL.exists() else []
    for p in verwaist:
        print(f"Warnung: nicht mehr im Repo, bitte prüfen (nicht gelöscht): {p}")

    print(f"\n{len(begriffe)} Begriffe · neu {zaehler['neu']} · geändert {zaehler['geändert']} · "
          f"unverändert {zaehler['unverändert']} · Commit {commit[:7]}"
          + (" · DRY-RUN" if args.dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
