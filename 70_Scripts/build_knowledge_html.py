"""Einen bestehenden Wissensbericht als eigenständigen HTML-Atlas darstellen.

Nutzt den vorhandenen, escaped Markdown-Renderer. Keine externen Abhängigkeiten,
keine Netzwerkzugriffe; der Bericht bleibt unverändert. Aufruf vom Repo-Root:
python 70_Scripts/build_knowledge_html.py reports/2026-10-28-gesamtes-wissen-ai-company-os.md
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

from repo_library.markdown import anchor, plain, render, table_cells


GROUPS = [
    {"name": "Ziele & Steuerung", "description": "Aus einer Absicht einen klaren, ausführbaren Auftrag machen.", "chapters": [3, 4, 8, 18]},
    {"name": "Kontext & Werkzeuge", "description": "Die richtigen Informationen und Fähigkeiten zur richtigen Zeit.", "chapters": [2, 5, 6, 7, 14]},
    {"name": "Qualität & Verantwortung", "description": "Ergebnisse belegen, Grenzen setzen und Entscheidungen abwägen.", "chapters": [1, 9, 10, 11, 19, 20]},
    {"name": "Produkt & Gestaltung", "description": "Software, Interaktion und Kommunikation bewusst entwickeln.", "chapters": [12, 13, 15, 16, 17]},
]


def excerpt(text: str, limit: int = 210) -> str:
    """Ersten inhaltlichen Absatz als unveränderten Vorschautext verwenden."""
    paragraphs = re.split(r"\n\s*\n", text.strip())
    for paragraph in paragraphs:
        if paragraph.startswith(("#", "|", "**Q", "[GitHub]")):
            continue
        value = plain(paragraph).replace("\n", " ")
        if value:
            return value if len(value) <= limit else value[:limit].rsplit(" ", 1)[0] + " …"
    return ""


def pattern_title(value: str) -> str:
    """Dateinamensschreibweisen nur für die Anzeige lesbar machen."""
    value = value.replace("-", " ").replace("AGENTS md", "AGENTS.md").replace("CLAUDE md", "CLAUDE.md")
    for before, after in [("pruef", "prüf"), ("Pruef", "Prüf"), ("faehig", "fähig"),
                          ("hoehe", "höhe"), ("flaeche", "fläche"), ("haengig", "hängig"),
                          ("Aenderung", "Änderung"), ("aenderung", "änderung"), ("Domaenen", "Domänen"),
                          ("Qualitaet", "Qualität"), ("Fragilitaet", "Fragilität"), ("verstaendnis", "verständnis"),
                          ("Befaehig", "Befähig"), ("Haeufig", "Häufig"), ("Widerspruech", "Widersprüch"),
                          ("guenstig", "günstig"), ("waehlen", "wählen"), ("klaeren", "klären"),
                          ("staerkster", "stärkster"), ("Grenzfaelle", "Grenzfälle")]:
        value = value.replace(before, after)
    return re.sub(r"\bfuer\b", "für", value)


def make_data(source: Path) -> dict:
    raw = source.read_text(encoding="utf-8-sig")
    headings = list(re.finditer(r"^## (\d+)\. (.+)$", raw, re.M))
    chapters, sections, records = [], {}, []
    for index, match in enumerate(headings):
        number, title = int(match[1]), match[2]
        body = raw[match.end():headings[index + 1].start() if index + 1 < len(headings) else len(raw)].strip()
        sections[number] = body
        group = next((g["name"] for g in GROUPS if number in g["chapters"]), "Register & Nachweise")
        chapter = {"id": f"kapitel-{number}", "kind": "chapters", "number": number,
                   "title": title, "group": group, "excerpt": excerpt(body),
                   "text": plain(body), "html": render(body),
                   "headings": [{"title": m[1], "anchor": anchor(m[1])} for m in re.finditer(r"^### (.+)$", body, re.M)],
                   "anchor": anchor(f"{number}. {title}")}
        chapters.append(chapter)

    # Repo-Profile: Die ###-Überschrift liefert die fachliche Gruppe.
    repo_matches = list(re.finditer(r"^#### (R\d+) [·–—] (.+)$", sections[21], re.M))
    for index, match in enumerate(repo_matches):
        body = sections[21][match.end():repo_matches[index + 1].start() if index + 1 < len(repo_matches) else len(sections[21])]
        body = re.split(r"^### ", body, flags=re.M)[0].strip()
        groups = re.findall(r"^### (.+)$", sections[21][:match.start()], re.M)
        records.append({"id": match[1].lower(), "kind": "repos", "title": match[2],
                        "group": groups[-1], "code": match[1], "excerpt": excerpt(body),
                        "text": plain(body), "html": render(body), "chapter": 21,
                        "anchor": anchor(match[0][5:])})

    # Quellen sind bewusst Lektüreeinheiten, keine Anzahl unabhängiger Belege.
    source_matches = list(re.finditer(r"^\*\*(Q\d+) [·–—] (\d{4}-\d{2}-\d{2}) [·–—] (.+)\*\*$", sections[22], re.M))
    for index, match in enumerate(source_matches):
        body = sections[22][match.end():source_matches[index + 1].start() if index + 1 < len(source_matches) else len(sections[22])]
        body = re.split(r"^### ", body, flags=re.M)[0].strip()
        label = match[3]
        paths = re.findall(r"\]\(<?([^)>]+)>?\)", label + "\n" + body)
        source_type = next((kind for kind in ["X", "TikTok", "YouTube", "URL", "PDF"] if any(f"/Quellen/{kind}/" in p for p in paths)), "Source-Notiz")
        records.append({"id": match[1].lower(), "kind": "sources", "title": plain(label),
                        "group": source_type, "code": match[1], "date": match[2],
                        "excerpt": excerpt(body), "text": plain(body),
                        "html": render(label + "\n\n" + body), "chapter": 22,
                        "path": paths[0] if paths else ""})

    for number, kind in [(23, "patterns"), (24, "glossary")]:
        for line in sections[number].splitlines():
            if not line.startswith("| ["):
                continue
            cells = table_cells(line)
            link = re.search(r"\[([^\]]+)\]\(<?([^)>]+)>?\)", cells[0])
            if not link:
                raise ValueError(f"Nicht erkannter Registereintrag: {line}")
            title, path = link.groups()
            relations = [int(n) for n in re.findall(r"\d+", cells[2])] if kind == "patterns" else []
            group = "Methoden" if kind == "patterns" else unquote(path).split("/")[-2].split("-", 1)[-1].replace("-", " ").capitalize()
            records.append({"id": f"{'p' if kind == 'patterns' else 'g'}{1 + sum(r['kind'] == kind for r in records):03}",
                            "kind": kind, "title": pattern_title(title) if kind == "patterns" else title,
                            "group": group, "excerpt": plain(cells[1]), "text": plain(cells[1]),
                            "html": render(cells[1] + "\n\n" + cells[0]), "path": path,
                            "related": relations, "chapter": number})

    counts = {kind: sum(r["kind"] == kind for r in records) for kind in ["repos", "sources", "patterns", "glossary"]}
    # Der Builder ist absichtlich auf die fünf Lesepfade dieses Berichts begrenzt.
    expected = {"repos": 74, "sources": 604, "patterns": 93, "glossary": 71}
    if counts != expected or [c["number"] for c in chapters] != list(range(1, 26)):
        raise ValueError(f"Berichtsstruktur weicht ab; keine unvollständige Ausgabe schreiben: {counts}")
    ids = [r["id"] for r in records] + [c["id"] for c in chapters]
    if len(ids) != len(set(ids)):
        raise ValueError("Doppelte IDs im Register")
    # Roh-Markdown eingebettet: Rückweg zum vollständigen Eingangsartefakt auch offline.
    return {"chapters": chapters, "records": records, "groups": GROUPS, "counts": counts,
            "source": source.name, "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "raw": raw}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Wissensbericht mit 25 Kapiteln")
    parser.add_argument("--output", type=Path, help="Standard: gleicher Pfad mit .html")
    args = parser.parse_args()
    source = args.source.resolve()
    output = (args.output or source.with_suffix(".html")).resolve()
    if source == output:
        parser.error("Eingabe und Ausgabe müssen verschieden sein")
    data = make_data(source)
    # Relative Belegpfade gelten weiterhin vom Verzeichnis des Berichts aus.
    if output.parent != source.parent:
        parser.error("Die HTML-Datei muss für lokale Beleglinks neben dem Bericht liegen")
    template = Path(__file__).with_name("knowledge_atlas.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    payload = payload.replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    result = template.replace("/*__ATLAS_DATA__*/", payload)
    output.write_text(result, encoding="utf-8")
    print(f"Erstellt: {output}\n25 Kapitel; {data['counts']}\n{len(result.encode('utf-8')):,} Bytes; offline ohne Laufzeit-Abhängigkeiten")


if __name__ == "__main__":
    main()
