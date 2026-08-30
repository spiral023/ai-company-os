#!/usr/bin/env python3
"""vibedeck-Knowledge-Artikel als Sekundärquellen in die Inbox importieren.

Die Artikel in vibedeck sind bereits redaktionelle deutsche Aufarbeitungen, also
fremde Synthesen und keine Rohquellen. Sie werden deshalb mit `sekundaerquelle: true`
markiert — die Verarbeitung muss wissen, dass hier nicht die Primärquelle vorliegt.

Bildpositionen: vibedeck referenziert Bilder inline an der inhaltlich passenden
Stelle. Diese Information wird bewahrt — die Bilder werden kopiert und nur die
Pfade umgeschrieben (`/images/knowledge/<slug>/x.jpg` → `medien/<slug>/x.jpg`).
Tweet-/Thread-Quellen landen unter `00_Inbox/Quellen/X/`, Webquellen unter
`00_Inbox/Quellen/URL/`.

Nutzung:
    python 70_Scripts/import_vibedeck_knowledge.py [--dry-run] [--only <slug>]
                                                   [--skip-vorhandene-urls]
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VIBEDECK = Path(r"C:\Users\asi\Documents\GitHub\vibedeck")
QUELLE_DIR = VIBEDECK / "src" / "content" / "knowledge"
BILD_DIR = VIBEDECK / "public" / "images" / "knowledge"
INBOX = REPO / "00_Inbox" / "Quellen"
SOURCES = REPO / "80_Knowledge" / "Sources"
MEDIA_DIRNAME = "medien"

# vibedeck sourceType → Inbox-typ (Source-Notiz-Mapping macht der Skill)
TYP_MAP = {"tweet": "tweet", "thread": "tweet", "blog": "url", "docs": "url", "article": "url"}
ORDNER_MAP = {"tweet": "X", "url": "URL"}
BILD_RE = re.compile(r"!\[([^\]]*)\]\(/images/knowledge/([^/)]+)/([^)]+)\)")


def frontmatter_und_body(text: str) -> tuple[dict[str, object], str]:
    """Minimaler Frontmatter-Parser: Skalare und einfache Listen."""
    treffer = re.match(r"(?s)^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", text)
    if not treffer:
        return {}, text
    daten: dict[str, object] = {}
    schluessel: str | None = None
    for zeile in treffer.group(1).splitlines():
        if re.match(r"^\s*-\s+", zeile) and schluessel:
            wert = re.sub(r"^\s*-\s+", "", zeile).strip().strip('"').strip("'")
            daten.setdefault(schluessel, [])
            if isinstance(daten[schluessel], list):
                daten[schluessel].append(wert)
            continue
        paar = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", zeile)
        if paar:
            schluessel = paar.group(1)
            wert = paar.group(2).strip()
            if wert:
                daten[schluessel] = wert.strip('"').strip("'")
            else:
                daten[schluessel] = []
    return daten, treffer.group(2)


def slugify(wert: str, maxlen: int = 40) -> str:
    wert = wert.lower()
    for k, v in {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}.items():
        wert = wert.replace(k, v)
    wert = re.sub(r"[^a-z0-9]+", "-", wert).strip("-")
    return wert[:maxlen].strip("-") or "unbekannt"


def autor_slug(autor: str) -> str:
    """"elvis (@omarsar0)" → "omarsar0"; sonst Name-Slug."""
    handle = re.search(r"@([A-Za-z0-9_]+)", autor or "")
    if handle:
        return slugify(handle.group(1), 24)
    return slugify(autor or "unbekannt", 24)


def normalisiere_url(url: str) -> str:
    url = (url or "").split("?")[0].rstrip("/")
    return url.lower()


def vorhandene_urls() -> dict[str, str]:
    """Normalisierte URLs aus Sources und Inbox, um Dubletten zu erkennen."""
    treffer: dict[str, str] = {}
    for ordner, muster in ((SOURCES, r"(?m)^url:\s*(.+)$"), (INBOX, r"(?m)^url:\s*(.+)$")):
        if not ordner.exists():
            continue
        for datei in ordner.rglob("*.md"):
            if datei.name == "README.md":
                continue
            gefunden = re.search(muster, datei.read_text(encoding="utf-8"))
            if gefunden:
                treffer[normalisiere_url(gefunden.group(1))] = str(
                    datei.relative_to(REPO)
                ).replace("\\", "/")
    return treffer


def yaml_str(wert: object) -> str:
    return '"' + str(wert).replace("\\", "\\\\").replace('"', '\\"') + '"'


def baue_notiz(fm: dict[str, object], body: str, slug: str, bilder: list[str]) -> str:
    typ = TYP_MAP.get(str(fm.get("sourceType", "")), "notiz")
    zeilen = [
        "---",
        f"url: {fm.get('sourceURL', 'keine')}",
        f"titel: {yaml_str(fm.get('title', slug))}",
    ]
    if fm.get("author"):
        zeilen.append(f"autor: {yaml_str(fm['author'])}")
    zeilen += [
        f"datum: {fm.get('sourceDate', fm.get('addedDate', dt.date.today().isoformat()))}",
        f"erfasst: {dt.date.today().isoformat()}",
        f"typ: {typ}",
        "quelle: vibedeck",
        "sekundaerquelle: true",
        "status: neu",
    ]
    if bilder:
        zeilen.append(f'medien: "{len(bilder)} lokal"')
    if fm.get("description"):
        zeilen.append(f"beschreibung: {yaml_str(fm['description'])}")
    for feld, ziel in (("category", "vibedeck_category"), ("level", "vibedeck_level")):
        if fm.get(feld):
            zeilen.append(f"{ziel}: {fm[feld]}")
    for feld, ziel in (("tags", "vibedeck_tags"), ("topics", "vibedeck_topics")):
        werte = fm.get(feld)
        if isinstance(werte, list) and werte:
            zeilen.append(f"{ziel}:")
            zeilen += [f"  - {yaml_str(w)}" for w in werte]
    zeilen += ["---", "", f"# {fm.get('title', slug)}", ""]
    zeilen += [
        "> Sekundärquelle: aus vibedeck übernommene deutsche Aufarbeitung "
        f"(`src/content/knowledge/{slug}.md`). Primärquelle: {fm.get('sourceURL', 'unbekannt')}",
        "",
        body.strip(),
        "",
    ]
    return "\n".join(zeilen)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--only", help="nur diesen vibedeck-Slug")
    parser.add_argument(
        "--skip-vorhandene-urls",
        action="store_true",
        help="Artikel überspringen, deren URL schon als Source/Inbox existiert",
    )
    args = parser.parse_args()

    if not QUELLE_DIR.exists():
        print(f"✖ vibedeck-Knowledge nicht gefunden: {QUELLE_DIR}")
        return 1

    bekannt = vorhandene_urls()
    statistik = {"importiert": 0, "uebersprungen_url": 0, "uebersprungen_da": 0, "bilder": 0}
    dubletten: list[tuple[str, str]] = []

    for datei in sorted(QUELLE_DIR.glob("*.md")):
        slug = datei.stem
        if args.only and slug != args.only:
            continue
        fm, body = frontmatter_und_body(datei.read_text(encoding="utf-8"))
        url = str(fm.get("sourceURL", "")) or "keine"
        norm = normalisiere_url(url)

        if norm in bekannt and url != "keine":
            dubletten.append((slug, bekannt[norm]))
            if args.skip_vorhandene_urls:
                statistik["uebersprungen_url"] += 1
                continue

        datum = str(fm.get("sourceDate") or fm.get("addedDate") or dt.date.today().isoformat())[:10]
        ziel_slug = f"{datum}-{autor_slug(str(fm.get('author', '')))}-{slugify(slug)}"
        inbox_typ = TYP_MAP.get(str(fm.get("sourceType", "")), "notiz")
        ziel_ordner = INBOX / ORDNER_MAP.get(inbox_typ, "Sonstige")
        ziel_notiz = ziel_ordner / f"{ziel_slug}.md"
        if ziel_notiz.exists():
            statistik["uebersprungen_da"] += 1
            continue

        # Bilder kopieren und Pfade umschreiben — Position im Text bleibt erhalten.
        kopiert: list[str] = []
        ziel_medien = ziel_ordner / MEDIA_DIRNAME / ziel_slug

        def ersetze(treffer: re.Match[str]) -> str:
            alt_text, bild_slug, dateiname = treffer.groups()
            quelle = BILD_DIR / bild_slug / dateiname
            if not quelle.exists():
                return f"![{alt_text}](FEHLT:{bild_slug}/{dateiname})"
            if not args.dry_run:
                ziel_medien.mkdir(parents=True, exist_ok=True)
                shutil.copy2(quelle, ziel_medien / dateiname)
            kopiert.append(dateiname)
            return f"![{alt_text}]({MEDIA_DIRNAME}/{ziel_slug}/{dateiname})"

        neuer_body = BILD_RE.sub(ersetze, body)
        notiz = baue_notiz(fm, neuer_body, slug, kopiert)

        if args.dry_run:
            print(
                f"[dry-run] {ziel_notiz.relative_to(REPO)} ({len(kopiert)} Bilder)"
            )
        else:
            ziel_ordner.mkdir(parents=True, exist_ok=True)
            ziel_notiz.write_text(notiz, encoding="utf-8", newline="\n")
        statistik["importiert"] += 1
        statistik["bilder"] += len(kopiert)

    print(f"\n✔ Importiert: {statistik['importiert']} · Bilder: {statistik['bilder']}")
    if statistik["uebersprungen_url"]:
        print(f"  Übersprungen (URL bereits bekannt): {statistik['uebersprungen_url']}")
    if statistik["uebersprungen_da"]:
        print(f"  Übersprungen (Notiz existiert): {statistik['uebersprungen_da']}")
    if dubletten:
        print(f"\n⚠ {len(dubletten)} Artikel mit bereits bekannter URL:")
        for slug, wo in dubletten:
            print(f"  {slug} → {wo}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
