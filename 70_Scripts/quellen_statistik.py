"""Lokale Quellenstatistik mit eigenständigem HTML und unveränderlichen Snapshots.

Bedienung: python ai.py quellen statistik [--snapshot] [--autor ...] [--thema ...]
Nur Metadaten lesen; keine API-Aufrufe und keine Änderungen an Quellen.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import date, datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
from urllib.parse import parse_qs, quote, urlencode, urlsplit, urlunsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = 1
RULES = "quellen-v1"  # Bei geänderten Zählregeln erhöhen; Verlauf bleibt vergleichbar.


def norm(value) -> str:
    return str(value or "").strip().removeprefix("@").casefold()


def values(value) -> list:
    return value if isinstance(value, list) else [value] if value else []


def valid_date(value) -> str:
    try:
        return date.fromisoformat(str(value)).isoformat()
    except (ValueError, TypeError):
        return ""


def read_note(path: Path) -> dict:
    """Nur Frontmatter und die erste Titelzeile lesen, nicht den Quellen-Volltext."""
    with path.open(encoding="utf-8-sig") as stream:
        if stream.readline().strip() != "---":
            raise ValueError(f"Frontmatter fehlt: {path}")
        lines = []
        for line in stream:
            if line.strip() == "---":
                break
            lines.append(line)
        else:
            raise ValueError(f"Frontmatter nicht geschlossen: {path}")
        data = yaml.safe_load("".join(lines))
        if not isinstance(data, dict):
            raise ValueError(f"Frontmatter ist kein Mapping: {path}")
        if not data.get("titel"):
            for line in stream:
                if line.startswith("# "):
                    data["titel"] = line[2:].strip()
                    break
    return data


def canonical_id(data: dict, fallback: str) -> str:
    """Posts/Videos über ID; Artikel über URL ohne Fragment und Trackingparameter."""
    url = str(data.get("url") or "").strip()
    if not url or url.casefold() in {"keine", "unbekannt"}:
        return "datei:" + fallback
    u = urlsplit(url)
    host = (u.hostname or "").lower().removeprefix("www.")
    path = u.path.rstrip("/")
    if host in {"x.com", "twitter.com", "mobile.twitter.com"}:
        match = re.search(r"/status/(\d+)", path)
        if match:
            return "x:" + match[1]
    if host in {"youtube.com", "m.youtube.com", "youtu.be"}:
        video = parse_qs(u.query).get("v", [""])[0]
        if host == "youtu.be":
            video = path.strip("/")
        elif path.startswith(("/shorts/", "/embed/")):
            video = path.split("/")[-1]
        if video:
            return "youtube:" + video
    if "tiktok.com" == host or host.endswith(".tiktok.com"):
        match = re.search(r"/video/(\d+)", path)
        video = str(data.get("video_id") or (match[1] if match else ""))
        if video:
            return "tiktok:" + video
    if u.scheme not in {"http", "https", "file"}:
        return "datei:" + fallback
    query = parse_qs(u.query, keep_blank_values=True)
    query = {k: sorted(v) for k, v in query.items()
             if not k.lower().startswith("utm_") and k.lower() not in {"fbclid", "gclid"}}
    return urlunsplit((u.scheme.lower(), host, path, urlencode(sorted(query.items()), doseq=True), ""))


def platform_for(data: dict) -> str:
    host = (urlsplit(str(data.get("url") or "")).hostname or "").lower()
    if host in {"x.com", "twitter.com", "www.x.com", "www.twitter.com"}:
        return "X"
    if host in {"youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be"}:
        return "YouTube"
    if host == "tiktok.com" or host.endswith(".tiktok.com"):
        return "TikTok"
    return {"repo": "Repository", "notiz": "Notiz"}.get(data.get("typ"), "URL")


def author_identity(name, platform: str, aliases: dict) -> tuple[str, str]:
    key = f"{platform}:{norm(name)}"
    for identifier, entry in aliases.items():
        if key in entry.get("aliases", []):
            return identifier, entry["name"]
    return (key, str(name).strip()) if norm(name) else ("unbekannt", "Unbekannt")


def aggregate(rows: list[dict]) -> dict:
    result = {"total": len(rows)}
    for output, field in (("authors", "authors"), ("topics", "topics"),
                          ("keywords", "keywords"), ("platforms", "platforms"), ("status", "statuses")):
        counts = Counter()
        for row in rows:
            counts.update(set(row[field]))
        result[output] = dict(sorted(counts.items(), key=lambda x: (-x[1], x[0])))
    return result


def collect(root: Path = ROOT) -> dict:
    raw = {p.relative_to(root).as_posix(): read_note(p)
           for p in sorted((root / "00_Inbox/Quellen").glob("*/*.md"))}
    sources = {p.relative_to(root).as_posix(): read_note(p)
               for p in sorted((root / "80_Knowledge/Sources").glob("*.md"))}
    topic_dir = root / "80_Knowledge/Themen"
    assignment = yaml.safe_load((topic_dir / "zuordnung.yaml").read_text(encoding="utf-8")) or {}
    taxonomy = yaml.safe_load((topic_dir / "themen.yaml").read_text(encoding="utf-8"))["cluster"]
    alias_path = root / "70_Scripts/quellen_dashboard/autoren.yaml"
    aliases = yaml.safe_load(alias_path.read_text(encoding="utf-8")) if alias_path.exists() else {}
    aliases = aliases or {}
    # Referenzen können skalar oder Liste sein; Dateinamen sind keine zuverlässigen Joins.
    links = defaultdict(set)
    issues = []
    for p, data in raw.items():
        for s in values(data.get("source_notiz")):
            if s in sources:
                links[p].add(s)
            else:
                issues.append({"kind": "Source-Verweis fehlt", "paths": [p, str(s)]})
        if data.get("status") not in {"neu", "verarbeitet", "ignoriert"}:
            issues.append({"kind": "Unbekannter Status", "paths": [p]})
        if data.get("status") == "verarbeitet" and not links[p]:
            issues.append({"kind": "Verarbeitet ohne gültige Source", "paths": [p]})
    for s, data in sources.items():
        for field in ("rohquelle", "zweitquelle"):
            for p in values(data.get(field)):
                if p in raw:
                    links[p].add(s)
                elif not (root / p).is_file():
                    issues.append({"kind": "Rohquellen-Verweis fehlt", "paths": [s, str(p)]})
    authors = {}

    def make_row(p, data, platform, source_paths, scope):
        names = values(data.get("autor"))
        if not names:
            names = sorted({str(sources[s]["autor"]) for s in source_paths if sources[s].get("autor")})
        identities = [author_identity(n, platform, aliases) for n in names] or [("unbekannt", "Unbekannt")]
        for key, name in identities:
            authors[key] = aliases.get(key, {}).get("name", name)
        main, secondary, keywords = set(), set(), set()
        for s in source_paths:
            entry = assignment.get("quellen", {}).get(Path(s).stem, {})
            if entry.get("haupt") in taxonomy:
                main.add(entry["haupt"])
            secondary.update(n for n in entry.get("neben", []) if n in taxonomy)
            keywords.update(str(k).strip().casefold() for k in entry.get("keywords", []) if str(k).strip())
        return {"id": canonical_id(data, p) if scope == "raw" else p,
                "title": str(data.get("titel") or Path(p).stem), "paths": [p],
                "source_paths": sorted(source_paths), "url": str(data.get("url") or ""),
                "authors": sorted({i[0] for i in identities}), "author_original": [str(n) for n in names],
                "platforms": [platform], "statuses": [str(data.get("status") or "ohne Status") if scope == "raw" else "Source"],
                "main_topics": sorted(main), "topics": sorted(main | secondary), "keywords": sorted(keywords),
                "captured": valid_date(data.get("erfasst")), "published": valid_date(data.get("datum")),
                "uncertain_date": bool(data.get("datum_unsicher"))}

    grouped = {}
    for p, data in raw.items():
        row = make_row(p, data, Path(p).parent.name, links[p], "raw")
        if not data.get("autor"):
            issues.append({"kind": "Autor fehlt im Roharchiv", "paths": [p]})
        if not row["captured"]:
            issues.append({"kind": "Erfassungsdatum fehlt/ungültig", "paths": [p]})
        if row["uncertain_date"]:
            issues.append({"kind": "Veröffentlichungsdatum unsicher", "paths": [p]})
        if row["id"] in grouped:
            previous = grouped[row["id"]]
            for field in ("paths", "source_paths", "authors", "author_original", "platforms", "statuses", "main_topics", "topics", "keywords"):
                previous[field] = sorted(set(previous[field]) | set(row[field]))
            previous["captured"] = min(filter(None, [previous["captured"], row["captured"]]), default="")
            previous["uncertain_date"] |= row["uncertain_date"]
        else:
            grouped[row["id"]] = row
    raw_rows = list(grouped.values())
    for row in raw_rows:
        if len(row["paths"]) > 1:
            issues.append({"kind": "Mehrfach archivierte Quelle", "paths": row["paths"]})
        if len(row["statuses"]) > 1:
            issues.append({"kind": "Widersprüchlicher Duplikat-Status", "paths": row["paths"]})
    source_rows = []
    for p, data in sources.items():
        row = make_row(p, data, platform_for(data), [p], "sources")
        source_rows.append(row)
        if not row["main_topics"]:
            issues.append({"kind": "Source ohne gültiges Hauptthema", "paths": [p]})
        if not row["keywords"]:
            issues.append({"kind": "Source ohne Keywords", "paths": [p]})
    patterns = list((root / "80_Knowledge/Patterns").glob("*.md"))
    linked_sources = set(s for ss in links.values() for s in ss)
    return {"schema": SCHEMA, "rules": RULES,
            "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "counts": {"raw_files": len(raw), "raw_unique": len(raw_rows), "sources": len(sources),
                       "patterns": len(patterns), "clusters": len(taxonomy),
                       "raw_status": dict(Counter(d.get("status", "ohne Status") for d in raw.values())),
                       "raw_platforms": dict(Counter(Path(p).parent.name for p in raw)),
                       "sources_without_raw_link": len(set(sources) - linked_sources)},
            "topics": {k: v["name"] for k, v in taxonomy.items()}, "authors": authors,
            "rows": {"raw": raw_rows, "sources": source_rows},
            "summary": {"raw": aggregate(raw_rows), "sources": aggregate(source_rows)},
            "issues": issues,
            "rules_fingerprint": hashlib.sha256(json.dumps(aliases, sort_keys=True).encode()).hexdigest()[:16]}


def snapshot_of(report: dict) -> dict:
    return {k: report[k] for k in ("schema", "rules", "rules_fingerprint", "generated_at", "counts", "summary")}


def write_snapshot(folder: Path, report: dict) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%S%fZ")
    path = folder / f"{stamp}.json"
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(snapshot_of(report), ensure_ascii=False, indent=2) + "\n")
    return path


def load_history(folder: Path, report: dict) -> tuple[list, list]:
    history, excluded = [], []
    for path in sorted(folder.glob("*.json")):
        try:
            item = json.loads(path.read_text(encoding="utf-8"))
            stamp = datetime.fromisoformat(item["generated_at"])
            if stamp.tzinfo is None:
                raise ValueError("Zeitzone fehlt")
            for metric in ("raw_files", "raw_unique", "sources", "patterns", "clusters"):
                if type(item["counts"][metric]) is not int or item["counts"][metric] < 0:
                    raise ValueError("Ungültige Bestandszahl")
            for scope in ("raw", "sources"):
                if type(item["summary"][scope]["total"]) is not int:
                    raise ValueError("Ungültige Gesamtzahl")
                for metric in ("authors", "topics", "keywords", "platforms", "status"):
                    distribution = item["summary"][scope][metric]
                    if not isinstance(distribution, dict) or any(type(v) is not int or v < 0 for v in distribution.values()):
                        raise ValueError("Ungültige Verteilung")
            if (item.get("schema"), item.get("rules"), item.get("rules_fingerprint")) != (SCHEMA, RULES, report["rules_fingerprint"]):
                excluded.append(path.name + ": andere Zählregeln/Autoren-Aliase")
            else:
                history.append(item)
        except (ValueError, KeyError, TypeError) as error:
            excluded.append(f"{path.name}: {error}")
    return sorted(history, key=lambda x: x["generated_at"]), excluded


def select_rows(report: dict, scope: str, author="", topic="", keyword="") -> list:
    return [r for r in report["rows"][scope]
            if (not author or any(norm(author) in norm(a) or norm(author) in norm(report["authors"][a])
                                  for a in r["authors"])
                or any(norm(author) in norm(a) for a in r["author_original"]))
            and (not topic or any(norm(topic) in norm(t) or norm(topic) in norm(report["topics"][t])
                                  for t in r["topics"]))
            and (not keyword or any(norm(keyword) in norm(k) for k in r["keywords"]))]


def render(report: dict, out: Path, root: Path = ROOT) -> str:
    template = (root / "70_Scripts/quellen_dashboard/index.html").read_text(encoding="utf-8")
    if "__ACTIVITY_MODEL__" in template:
        model = (root / "70_Scripts/quellen_dashboard/activity.js").read_text(encoding="utf-8")
        template = template.replace("__ACTIVITY_MODEL__", model)
    report = {**report, "repo_base": quote(os.path.relpath(root, out).replace("\\", "/"), safe="/.") + "/"}
    # Auch eingebettetes JSON muss ein schließendes script-Tag neutralisieren.
    encoded = json.dumps(report, ensure_ascii=False).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    return template.replace("__REPORT_JSON__", encoded)


def markdown(report: dict) -> str:
    counts = report["counts"]
    lines = ["# Quellenstatistik", "", f"Stand (UTC): {report['generated_at']}", "",
             f"- Rohdateien: {counts['raw_files']}; eindeutige Rohquellen: {counts['raw_unique']}",
             f"- Source-Notizen: {counts['sources']}; Patterns: {counts['patterns']}; Themen: {counts['clusters']}",
             f"- Gespeicherte vergleichbare Messungen: {len(report['history'])}", "",
             "[Interaktive HTML-Auswertung](index.html)", "",
             "## Autoren im eindeutigen Roharchiv", "", "| Autor/Kanal | Quellen |", "|---|---:|"]
    for key, count in list(report["summary"]["raw"]["authors"].items())[:20]:
        name = report["authors"][key].replace("|", "\\|")
        lines.append(f"| {name} | {count} |")
    lines += ["", "## Hinweise", "", "Roharchiv und Source-Notizen getrennt zählen. Topics und Keywords sind Mehrfachzuordnungen.",
              "Erfassungsaktivität wird aus dem heutigen Bestand rekonstruiert; Bestandsverlauf nur aus gespeicherten Snapshots.",
              "Importarchive und external_repos gehören nicht zu diesen Zählmengen.", ""]
    for kind, count in Counter(i["kind"] for i in report["issues"]).items():
        lines.append(f"- {kind}: {count}")
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", action="store_true", help="Unveränderliche Bestandsmessung speichern")
    parser.add_argument("--autor", default="")
    parser.add_argument("--thema", default="")
    parser.add_argument("--keyword", default="")
    parser.add_argument("--bestand", choices=["raw", "sources"], default="raw")
    parser.add_argument("--ausgabe", type=Path, default=ROOT / "reports/quellen", help="Zielordner für HTML, JSON und Markdown")
    args = parser.parse_args(argv)
    out = args.ausgabe.resolve()
    try:
        report = collect()
        if args.snapshot:
            write_snapshot(out / "snapshots", report)
        report["history"], report["excluded_history"] = load_history(out / "snapshots", report)
        report["initial"] = {"scope": args.bestand, "author": args.autor, "topic": args.thema, "keyword": args.keyword}
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(render(report, out), encoding="utf-8", newline="\n")
        (out / "aktuell.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        (out / "Uebersicht.md").write_text(markdown(report), encoding="utf-8", newline="\n")
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(f"Quellenstatistik abgebrochen: {error}")
        return 1
    counts = report["counts"]
    print(f"{counts['raw_files']} Rohdateien / {counts['raw_unique']} eindeutige Rohquellen; {counts['sources']} Source-Notizen; {counts['patterns']} Patterns.")
    rows = select_rows(report, args.bestand, args.autor, args.thema, args.keyword)
    print(f"Auswahl ({args.bestand}): {len(rows)}; gespeicherte Messungen: {len(report['history'])}.")
    if args.autor or args.thema or args.keyword:
        for row in rows:
            print(f"- {row['title']} ({row['paths'][0]})")
    print(f"HTML: {out / 'index.html'}")
    for warning in report["excluded_history"]:
        print(f"HINWEIS Snapshot nicht vergleichbar/lesbar: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
