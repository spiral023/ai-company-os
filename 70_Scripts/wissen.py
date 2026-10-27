"""Lokaler Wissenskatalog: Bestand, Abschnittssuche und vollständiger Prüfplan.

Nur Standardbibliothek; keine Modelle, Downloads oder Ausführung fremder Inhalte.
Der Index ist eine abgeleitete Sicht, keine inhaltliche Analyse oder Skill-Freigabe.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import stat
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
VERSION = 1
OWN_ROOTS = (
    "00_Inbox", "10_Company", "20_Workflows", "30_Skills", "40_Project_Kits",
    "50_Memory", "60_Evals", "70_Scripts", "80_Knowledge", "90_Archive", "docs", "reports",
    "AGENTS.md", "CLAUDE.md", "README.md", "ai.py", "external_repos/INDEX.md",
    "external_repos/changelog",
)
TEXT_EXTENSIONS = {".md", ".mdx", ".rst", ".txt", ".prompt", ".jinja", ".jinja2", ".j2", ".vtt", ".srt", ".yaml", ".yml", ".toml"}
CODE_EXTENSIONS = {".py", ".js", ".mjs", ".ts", ".tsx", ".jsx", ".rs", ".go", ".sh", ".ps1"}
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", ".pytest_cache", "_site", "dist", "build", "coverage", ".next", ".wissen", "secrets"}
CAPABILITY_DIRS = {"skills", "prompts", "agents", "commands", "playbooks", "rules"}


@lru_cache(maxsize=32768)
def linked_directory(path: Path) -> bool:
    """Gemeinsame Elternpfade je Scan einmal prüfen statt je einzelner Datei."""
    if path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction()):
        return True
    return path.parent != path and linked_directory(path.parent)


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, check=False, timeout=90)
    if result.returncode:
        raise RuntimeError(f"Git-Abfrage fehlgeschlagen: {repo} ({' '.join(args[:2])})")
    return result.stdout.decode("utf-8", errors="surrogateescape")


def repositories(root: Path) -> list[tuple[str, Path, bool]]:
    result = [("company-os", root, False)]
    external = root / "external_repos"
    if external.exists():
        for owner in sorted(external.iterdir()):
            if owner.is_dir() and not owner.is_symlink():
                for repo in sorted(owner.iterdir()):
                    if repo.is_dir() and not repo.is_symlink() and (repo / ".git").exists():
                        result.append((f"{owner.name}/{repo.name}", repo, True))
    separate = root / "external_knowledge" / "ai-llm-wiki"
    if (separate / ".git").exists():
        result.append(("external-knowledge/ai-llm-wiki", separate, True))
    return result


def own_files(root: Path) -> set[str]:
    """Der definierte Wissensscope gilt unabhängig von der Git-Versionierung."""
    result = set()
    for relative in OWN_ROOTS:
        path = root / relative
        if path.is_file():
            result.add(path.relative_to(root).as_posix())
        elif path.is_dir() and not linked_directory(path):
            for directory, dirs, files in os.walk(path, followlinks=False):
                current = Path(directory)
                dirs[:] = [name for name in dirs if name.lower() not in SKIP_DIRS and not linked_directory(current / name)]
                result.update((current / name).relative_to(root).as_posix() for name in files)
    return result


def kind_of(path: str, external: bool) -> str:
    p = Path(path)
    parts = {part.lower() for part in p.parts}
    if p.name.lower() == "skill.md":
        return "skill"
    for prefix, kind in (("00_Inbox/Quellen/", "rohquelle"), ("80_Knowledge/Sources/", "source"),
                         ("80_Knowledge/Patterns/", "pattern"), ("80_Knowledge/Themen/", "thema"),
                         ("50_Memory/", "memory"), ("20_Workflows/", "workflow"),
                         ("10_Company/", "firmenwissen"), ("60_Evals/", "eval"),
                         ("90_Archive/", "historisch")):
        if not external and path.startswith(prefix):
            return kind
    if parts & CAPABILITY_DIRS or "prompt" in p.stem.lower():
        return "prompt-regel-playbook"
    if external:
        return "repo-dokument"
    return "internes-dokument"


def exclusion(path: Path, relative: str, max_bytes: int) -> str:
    parts = {p.lower() for p in Path(relative).parts[:-1]}
    name = path.name.lower()
    if name.startswith(".env") or path.suffix.lower() in {".pem", ".key", ".p12", ".pfx"} or "secrets" in parts:
        return "vertraulicher-dateityp"
    if parts & SKIP_DIRS:
        return "generiert-oder-abhaengigkeit"
    ext = path.suffix.lower()
    documented = ext in TEXT_EXTENSIONS or name.startswith(("readme", "license", "licence", "notice"))
    capability = bool(parts & CAPABILITY_DIRS or "prompt" in name)
    if not documented and not (capability and ext in CODE_EXTENSIONS | {".json", ".jsonl", ".xml", ".html"}):
        return "code-nur-inventar" if ext in CODE_EXTENSIONS else "format-nur-inventar"
    # Externe Symlinks und Windows-Junctions niemals in den Index hinein verfolgen.
    try:
        info = path.lstat()
    except FileNotFoundError:
        return "fehlt-oder-keine-datei"
    if stat.S_ISLNK(info.st_mode) or linked_directory(path.parent):
        return "dateiverweis"
    if not stat.S_ISREG(info.st_mode):
        return "fehlt-oder-keine-datei"
    if info.st_size > max_bytes:
        return "ueber-groessenlimit"
    return ""


def sections(text: str, max_chars: int = 10000) -> list[tuple[str, int, int, str]]:
    """Lückenlose Zeilenbereiche; auch lange Abschnitte vollständig aufteilen."""
    lines = text.splitlines(keepends=True)
    result = []
    title = "Dokumentanfang"
    start = 1
    buffer: list[str] = []
    length = 0
    fenced = False
    for number, line in enumerate(lines, 1):
        heading = re.match(r"^#{1,6}\s+(.+)", line) if not fenced else None
        if buffer and (heading or length + len(line) > max_chars):
            result.append((title, start, number - 1, "".join(buffer)))
            buffer, length, start = [], 0, number
        if heading:
            title = heading.group(1).strip()
        buffer.append(line)
        length += len(line)
        if re.match(r"^\s*(```|~~~)", line):
            fenced = not fenced
    if buffer:
        result.append((title, start, len(lines), "".join(buffer)))
    return result


def metadata(text: str) -> tuple[str, str, str]:
    """Nur einfache skalare Herkunftsfelder lesen; keine YAML-Ausführung."""
    front = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    fields = {}
    if front:
        for key in ("url", "rohquelle", "status"):
            match = re.search(rf"^{key}:\s*(.+)$", front.group(1), re.M)
            fields[key] = match.group(1).strip().strip("\"'") if match else ""
    return fields.get("url", ""), fields.get("rohquelle", ""), fields.get("status", "")


def fingerprint_of(db: sqlite3.Connection, errors: list[str]) -> str:
    fingerprint = hashlib.sha256(f"wissen:{VERSION}".encode())
    for row in db.execute("SELECT path,kind,state,reason,size,sha256 FROM documents ORDER BY path"):
        fingerprint.update(json.dumps(tuple(row), ensure_ascii=True).encode())
    for row in db.execute("SELECT * FROM repos ORDER BY name"):
        fingerprint.update(json.dumps(tuple(row), ensure_ascii=True).encode())
    for error in errors:
        fingerprint.update(error.encode())
    return fingerprint.hexdigest()


@contextmanager
def connect(path: Path):
    if not path.exists():
        raise RuntimeError("Wissensindex fehlt. Zuerst: python ai.py wissen index")
    db = sqlite3.connect(f"{path.resolve().as_uri()}?mode=ro", uri=True)
    db.row_factory = sqlite3.Row
    version = db.execute("SELECT value FROM meta WHERE key='version'").fetchone()
    if not version or int(version[0]) != VERSION:
        db.close()
        raise RuntimeError("Indexversion passt nicht. Wissensindex neu erzeugen.")
    try:
        yield db
    finally:
        db.close()


def build_index(root: Path, output: Path, max_bytes: int = 1_000_000, progress: bool = False) -> dict:
    linked_directory.cache_clear()
    output.mkdir(parents=True, exist_ok=True)
    handle, temporary = tempfile.mkstemp(prefix="index-", suffix=".sqlite", dir=output)
    os.close(handle)
    db = sqlite3.connect(temporary)
    try:
        # Ausschließlich der neue, rekonstruierbare Index: ein größerer Cache
        # vermeidet zufällige Seitenzugriffe bei großen FTS-Beständen.
        db.executescript("PRAGMA journal_mode=MEMORY; PRAGMA cache_size=-65536; PRAGMA temp_store=MEMORY;")
        db.executescript("""
            CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);
            CREATE TABLE repos (name TEXT PRIMARY KEY, path TEXT, head TEXT, dirty INTEGER, status_hash TEXT, external INTEGER);
            CREATE TABLE documents (path TEXT PRIMARY KEY, repo TEXT, kind TEXT, state TEXT, reason TEXT,
                size INTEGER, sha256 TEXT, title TEXT, url TEXT, raw_source TEXT, source_status TEXT);
            CREATE VIRTUAL TABLE passages USING fts5(path UNINDEXED, repo UNINDEXED, kind UNINDEXED,
                start UNINDEXED, end UNINDEXED, heading, body, tokenize='unicode61 remove_diacritics 2');
        """)
        errors = []
        for name, repo, external in repositories(root):
            if progress:
                print(f"Katalog: {name}", file=sys.stderr, flush=True)
            try:
                head = git(repo, "rev-parse", "HEAD").strip()
                status = git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=normal")
                args = ["ls-files", "-z", "--cached", "--others", "--exclude-standard"]
                if not external:
                    args += ["--", *OWN_ROOTS]
                names = sorted(set(git(repo, *args).split("\0")) - {""})
                if not external:
                    names = sorted(set(names) | own_files(root))
                db.execute("INSERT INTO repos VALUES (?,?,?,?,?,?)", (name, repo.relative_to(root).as_posix() or ".", head, bool(status), hashlib.sha256(status.encode("utf-8", errors="surrogateescape")).hexdigest(), external))
            except (RuntimeError, subprocess.TimeoutExpired, OSError) as error:
                errors.append(f"{name}: {error}")
                continue
            for file_number, filename in enumerate(names, 1):
                if progress and file_number % 250 == 0:
                    print(f"  {file_number}/{len(names)} Dateien", file=sys.stderr, flush=True)
                path = repo / filename
                relative = path.relative_to(root).as_posix()
                kind = kind_of(relative if not external else filename, external)
                size, digest, title, url, raw, source_status = -1, "", path.stem, "", "", ""
                try:
                    reason = exclusion(path, filename, max_bytes)
                    if reason == "ueber-groessenlimit":
                        size = path.lstat().st_size
                    text = ""
                    if not reason:
                        content = path.read_bytes()
                        size = len(content)
                        digest = hashlib.sha256(content).hexdigest()
                        if b"\0" in content:
                            reason = "binaerinhalt"
                        else:
                            try:
                                text = content.decode("utf-8-sig")
                            except UnicodeDecodeError:
                                reason = "kein-utf8"
                    if not reason:
                        title_match = re.search(r"^#\s+(.+)$", text, re.M)
                        title = title_match.group(1).strip() if title_match else title
                        url, raw, source_status = metadata(text)
                        if not text.strip():
                            reason = "leer"
                    if not reason:
                        for heading, start, end, body in sections(text):
                            db.execute("INSERT INTO passages VALUES (?,?,?,?,?,?,?)", (relative, name, kind, start, end, heading, body))
                    state = "indexed" if not reason else "excluded"
                except (OSError, ValueError) as error:
                    state, reason = "error", type(error).__name__
                db.execute("INSERT INTO documents VALUES (?,?,?,?,?,?,?,?,?,?,?)", (relative, name, kind, state, reason, size, digest, title, url, raw, source_status))
        # Der Snapshot hängt von Inhalten und Dateistatus ab, nicht vom Erzeugungszeitpunkt.
        values = {"version": VERSION, "created": datetime.now(timezone.utc).isoformat(), "root": str(root.resolve()),
                  "snapshot": fingerprint_of(db, errors), "max_bytes": max_bytes, "repository_errors": errors,
                  "scope": "Eigene definierte Wissensordner einschließlich ignorierter Archive; externe Checkouts über Git-erfasste und nicht ignorierte Dateien."}
        db.executemany("INSERT INTO meta VALUES (?,?)", [(key, json.dumps(value, ensure_ascii=False)) for key, value in values.items()])
        db.commit()
        db.close()
        os.replace(temporary, output / "index.sqlite")
    except BaseException:
        db.close()
        Path(temporary).unlink(missing_ok=True)
        raise
    with connect(output / "index.sqlite") as indexed:
        return status_of(indexed)


def status_of(db: sqlite3.Connection) -> dict:
    meta = {row[0]: json.loads(row[1]) for row in db.execute("SELECT key,value FROM meta")}
    counts = dict(db.execute("SELECT state, count(*) FROM documents GROUP BY state"))
    return {**meta, "documents": counts, "passages": db.execute("SELECT count(*) FROM passages").fetchone()[0],
            "repositories": [dict(row) for row in db.execute("SELECT name,head,dirty FROM repos ORDER BY name")],
            "exclusions": dict(db.execute("SELECT reason,count(*) FROM documents WHERE state!='indexed' GROUP BY reason")),
            "analysis": "nicht-im-katalog-erhoben", "activation": "keine-durch-diesen-katalog"}


def search(db: sqlite3.Connection, query: str, limit: int = 10, repo: str | None = None, kind: str | None = None) -> list[dict]:
    words = list(dict.fromkeys(re.findall(r"[^\W_]+", query, re.UNICODE)))[:30]
    if not words:
        return []
    expression = " OR ".join('"' + word + '"' for word in words)
    where, params = ["passages MATCH ?"], [expression]
    if repo:
        where.append("p.repo = ?")
        params.append(repo)
    if kind:
        where.append("p.kind = ?")
        params.append(kind)
    params.append(limit)
    rows = db.execute("SELECT p.path,p.repo,p.kind,p.start,p.end,p.heading,"
                      "snippet(passages,6,'[',']',' … ',32) AS excerpt,d.sha256,d.url,d.raw_source,"
                      "r.head,r.dirty FROM passages p JOIN documents d ON d.path=p.path "
                      "JOIN repos r ON r.name=p.repo WHERE " + " AND ".join(where) + " ORDER BY bm25(passages,0,0,0,0,0,3,1) LIMIT ?", params)
    return [dict(row) for row in rows]


def read_document(db: sqlite3.Connection, path: str, start: int = 1, end: int | None = None) -> dict:
    row = db.execute("SELECT d.*,r.head,r.dirty FROM documents d JOIN repos r ON r.name=d.repo WHERE d.path=? AND d.state='indexed'", (path,)).fetchone()
    if not row:
        raise RuntimeError("Datei ist nicht als lesbarer Text im Index enthalten.")
    snapshot = status_of(db)
    source = Path(snapshot["root"]) / row["path"]
    linked_directory.cache_clear()
    if exclusion(source, row["path"], snapshot["max_bytes"]):
        raise RuntimeError("Quelle ist inzwischen nicht mehr als Text lesbar; neu indexieren.")
    content = source.read_bytes()
    if hashlib.sha256(content).hexdigest() != row["sha256"]:
        raise RuntimeError("Quelle wurde seit der Indexierung geändert; neu indexieren.")
    lines = content.decode("utf-8-sig").splitlines(keepends=True)
    stop = min(end if end is not None else len(lines), len(lines))
    if start < 1 or start > stop:
        raise RuntimeError("Ungültiger Zeilenbereich.")
    text = "".join(lines[start - 1:stop])
    if len(text) > 30000:
        raise RuntimeError("Mehr als 30.000 Zeichen angefragt; einen kleineren Zeilenbereich wählen.")
    return {"path": path, "repo": row["repo"], "head": row["head"], "dirty": row["dirty"], "sha256": row["sha256"],
            "start": start, "end": stop, "url": row["url"], "raw_source": row["raw_source"], "text": text}


def analysis_plan(db: sqlite3.Connection, output: Path, budget: int = 60000) -> dict:
    """Alle indexierten Passagen einplanen; kein vorgetäuschter Analysestatus."""
    if output.exists():
        raise RuntimeError("Ausgabe existiert bereits; für einen neuen Lauf einen neuen Pfad wählen.")
    meta = status_of(db)
    batches, current, length = [], [], 0
    for row in db.execute("SELECT p.path,p.repo,p.kind,p.start,p.end,length(p.body) AS characters,d.sha256 "
                          "FROM passages p JOIN documents d ON d.path=p.path ORDER BY p.repo,p.path,CAST(p.start AS INTEGER)"):
        entry = dict(row)
        if current and length + entry["characters"] > budget:
            batches.append({"id": len(batches) + 1, "status": "offen", "characters": length, "passages": current})
            current, length = [], 0
        entry["status"] = "offen"
        current.append(entry)
        length += entry["characters"]
    if current:
        batches.append({"id": len(batches) + 1, "status": "offen", "characters": length, "passages": current})
    exclusions = [dict(row) for row in db.execute("SELECT path,repo,state,reason,size FROM documents WHERE state!='indexed' ORDER BY path")]
    result = {"schema_version": VERSION, "snapshot": meta["snapshot"], "created": datetime.now(timezone.utc).isoformat(),
              "root": meta["root"], "status": "geplant-nicht-analysiert", "coverage": meta["documents"],
              "repository_errors": meta["repository_errors"], "repositories": meta["repositories"],
              "character_budget": budget, "batches": batches, "excluded": exclusions,
              "completion": "Jede Passage am Hash-Stand lesen und bewerten; fehlende/abweichende Inhalte offen lassen. Danach Themen- und Repo-Ergebnisse quer vergleichen. Indexierung und Planung belegen keine inhaltliche Analyse."}
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    return {"snapshot": meta["snapshot"], "batches": len(batches), "passages": meta["passages"], "output": str(output), "status": result["status"]}


def analysis_check(db: sqlite3.Connection, plan_path: Path, results_path: Path) -> dict:
    """Abdeckung und Quellenversionen prüfen; fachliche Urteile separat reviewen."""
    linked_directory.cache_clear()
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    snapshot = status_of(db)
    if plan.get("snapshot") != snapshot["snapshot"]:
        raise RuntimeError("Analyseplan gehört zu einem anderen Indexsnapshot.")
    def key(row):
        return (row["path"], int(row["start"]), int(row["end"]), row["sha256"])
    expected = {key(dict(row)) for row in db.execute("SELECT p.path,p.start,p.end,d.sha256 FROM passages p JOIN documents d ON d.path=p.path")}
    planned = [key(p) for batch in plan["batches"] for p in batch["passages"]]
    if len(planned) != len(set(planned)) or set(planned) != expected:
        raise RuntimeError("Analyseplan deckt die indexierten Passagen nicht genau einmal ab.")
    seen, done, invalid = set(), set(), []
    for number, line in enumerate(results_path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
            entry = key(row)
        except (ValueError, KeyError, TypeError) as error:
            raise RuntimeError(f"Ungültiger Ergebnisdatensatz in Zeile {number}.") from error
        if entry not in expected or entry in seen:
            invalid.append(number)
        elif row.get("status") == "analysiert" and isinstance(row.get("beurteilung"), str) and row["beurteilung"].strip():
            done.add(entry)
        seen.add(entry)
    changed = []
    root = Path(snapshot["root"])
    for row in db.execute("SELECT path,sha256 FROM documents WHERE state='indexed'"):
        path = root / row[0]
        try:
            reason = exclusion(path, row[0], snapshot["max_bytes"])
            digest = hashlib.sha256(path.read_bytes()).hexdigest() if not reason else ""
        except OSError:
            digest = ""
        if digest != row[1]:
            changed.append(row[0])
    complete = not (expected - done or invalid or changed or snapshot["repository_errors"])
    return {"snapshot": snapshot["snapshot"], "complete": complete, "expected": len(expected), "analysed": len(done),
            "open": len(expected - done), "invalid_result_lines": invalid, "changed_inputs": changed,
            "repository_errors": snapshot["repository_errors"], "known_exclusions": snapshot["exclusions"],
            "scope": "Abdeckungsnachweis im indexierten Textscope. Fachliche Richtigkeit und Quersynthese separat prüfen; neue Dateien werden erst durch erneute Indexierung erkannt."}


def positive(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("Wert muss positiv sein.")
    return number


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    sub = parser.add_subparsers(dest="command", required=True)
    index = sub.add_parser("index", help="Gesamtkatalog lokal neu erzeugen")
    index.add_argument("--max-bytes", type=positive, default=1_000_000)
    index.add_argument("--progress", action="store_true", help="Fortschritt auf stderr ausgeben")
    sub.add_parser("status", help="Abdeckung des gespeicherten Snapshots, ohne Aktualitätsbehauptung")
    find = sub.add_parser("suche", help="Wörtliche Abschnittssuche mit Herkunft")
    find.add_argument("frage")
    find.add_argument("--limit", type=positive, default=10)
    find.add_argument("--repo")
    find.add_argument("--art")
    read = sub.add_parser("lesen", help="Gefundene Textbereiche am geprüften Dateihash nachladen")
    read.add_argument("pfad")
    read.add_argument("--von", type=positive, default=1)
    read.add_argument("--bis", type=positive)
    plan = sub.add_parser("analyse-plan", help="Alle indexierten Passagen in offene Prüfpakete aufteilen")
    plan.add_argument("--ausgabe", type=Path, required=True)
    plan.add_argument("--budget", type=positive, default=60000, help="Zeichenbudget je Paket; eine überlange Einzelzeile bleibt vollständig")
    check = sub.add_parser("analyse-check", help="Ergebnisabdeckung und unveränderte Quelltexte gegen einen Prüfplan prüfen")
    check.add_argument("--plan", type=Path, required=True)
    check.add_argument("--ergebnisse", type=Path, required=True, help="JSONL mit einem Datensatz je Passage")
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve()
        if args.command == "index":
            result = build_index(root, root / ".wissen", args.max_bytes, args.progress)
        else:
            with connect(root / ".wissen" / "index.sqlite") as db:
                if args.command == "status":
                    result = status_of(db)
                elif args.command == "suche":
                    result = {"query": args.frage, "results": search(db, args.frage, args.limit, args.repo, args.art),
                              "scope": "Wörtliche Suche im gespeicherten Snapshot; keine vollständige Recherche oder semantische Synthese."}
                elif args.command == "lesen":
                    result = read_document(db, args.pfad, args.von, args.bis)
                elif args.command == "analyse-plan":
                    result = analysis_plan(db, args.ausgabe.resolve(), args.budget)
                else:
                    result = analysis_check(db, args.plan.resolve(), args.ergebnisse.resolve())
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if isinstance(result, dict) and (result.get("repository_errors") or result.get("documents", {}).get("error") or result.get("complete") is False) else 0
    except (RuntimeError, OSError, sqlite3.Error, subprocess.TimeoutExpired, ValueError, KeyError, TypeError) as error:
        print(f"Wissenskatalog: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
