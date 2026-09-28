#!/usr/bin/env python3
"""Pipeline-Werkzeug für die Verarbeitung von Inbox-Quellen (Skill quellen-verarbeiten).

Schritte eines Laufs (Arbeitsordner: tmp/quellen-lauf/<lauf>/):

    prep    Auszüge offener Quellen (status: neu) für die Triage erzeugen
    plan    Triage-Ergebnisse auswerten, Batch-Listen für die Subagents schreiben
    apply   Reports der Subagents übernehmen: Inbox-Status, Beleg-Zeilen, Fakten, Befunde
    fakten  Fakten-Register aus den gesammelten Faktenzeilen fortschreiben
    check   Konsistenz zwischen Inbox-Status und Source-Notizen prüfen

Beispiel:
    python 70_Scripts/quellen_pipeline.py prep --lauf 2026-10-06
    python 70_Scripts/quellen_pipeline.py plan --lauf 2026-10-06
    python 70_Scripts/quellen_pipeline.py apply --lauf 2026-10-06 voll01 kurz01 --dry
    python 70_Scripts/quellen_pipeline.py apply --lauf 2026-10-06 --alle
    python 70_Scripts/quellen_pipeline.py check

`apply` bricht ab, wenn ein genannter Report nicht existiert. Ein Fehler in einer
Shell-Schleife (z. B. `seq -w` ohne führende Nullen) darf keinen Report still überspringen.
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUELLEN = ROOT / "00_Inbox" / "Quellen"
SOURCES = ROOT / "80_Knowledge" / "Sources"
PATTERNS = ROOT / "80_Knowledge" / "Patterns"
FAKTEN = ROOT / "80_Knowledge" / "Fakten" / "Modelle-und-Preise.md"
LAUF_ROOT = ROOT / "tmp" / "quellen-lauf"

BELEG_RE = re.compile(
    r"^- \d{4}-\d{2}-\d{2} · (\[\[[^\]]+\]\]|external_repos/\S+) · "
    r"(meinung|mehrfach-belegt|verifiziert) — .+$"
)
STUFEN = ("VOLL", "KURZ", "FAKT", "IGNORIEREN", "OFFEN")
FAKT_KATEGORIEN = ("Modell", "Preis", "Benchmark", "Markt")
FAKT_TITEL = {
    "Modell": "Modelle und Releases",
    "Preis": "Preise",
    "Benchmark": "Benchmarks und Messungen",
    "Markt": "Markt und Adoption",
}


def lauf_dir(name: str | None) -> Path:
    name = name or date.today().isoformat()
    path = LAUF_ROOT / name
    path.mkdir(parents=True, exist_ok=True)
    return path


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def inbox_notizen() -> list[Path]:
    """Direkte Notizen in den Typordnern; Unterordner (z. B. Wörterbuch-Kopien) sind keine Quellen."""
    return sorted(p for p in QUELLEN.glob("*/*.md") if p.parent != QUELLEN)


def frontmatter(text: str) -> tuple[str, str]:
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    return (m.group(1), m.group(2)) if m else ("", text)


def feld(fm: str, name: str) -> str | None:
    m = re.search(rf"^{name}: (.+)$", fm, re.M)
    return m.group(1).strip().strip('"') if m else None


# ---------------------------------------------------------------- prep

def cmd_prep(args: argparse.Namespace) -> int:
    lauf = lauf_dir(args.lauf)
    items = []
    ohne_inhalt = []
    for p in inbox_notizen():
        fm, body = frontmatter(read(p))
        if feld(fm, "status") != "neu":
            continue
        if feld(fm, "transkript") == "nicht verfügbar":
            ohne_inhalt.append(rel(p))  # nur Caption: erst erneut erfassen, nicht triagieren
            continue
        keep = [f"{k}: {feld(fm, k)}" for k in ("url", "autor", "datum", "typ", "titel") if feld(fm, k)]
        body = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)
        body = re.sub(r"\s+", " ", body).strip()
        items.append((rel(p), len(read(p)), " | ".join(keep), body[: args.zeichen]))
    if ohne_inhalt:
        write(lauf / "offen.txt", "\n".join(ohne_inhalt) + "\n")
        print(f"{len(ohne_inhalt)} Quellen ohne Transkript nicht triagiert (Liste: {rel(lauf / 'offen.txt')}); erneut erfassen.")
    if not items:
        print("Keine triagierbaren offenen Quellen. Nichts zu tun.")
        return 0
    n = max(1, -(-len(items) // args.batch))
    size = -(-len(items) // n)
    for i in range(n):
        block = items[i * size : (i + 1) * size]
        text = "".join(f"### {f}\nBYTES: {b}\n{k}\nAUSZUG: {a}\n\n" for f, b, k, a in block)
        write(lauf / "triage" / f"batch{i + 1}.txt", text)
    print(f"{len(items)} offene Quellen in {n} Triage-Batches unter {rel(lauf / 'triage')}")
    print("Nächster Schritt: pro Batch einen Haiku-Subagent mit references/triage-auftrag.md starten;")
    print(f"Ergebnis je Batch nach {rel(lauf / 'triage')}/triageN.txt schreiben lassen, dann `plan`.")
    return 0


# ---------------------------------------------------------------- plan

def parse_triage(lauf: Path) -> list[dict]:
    rows = []
    for f in sorted((lauf / "triage").glob("triage*.txt")):
        for line in read(f).splitlines():
            if not line.strip():
                continue
            p = [x.strip() for x in line.split(" | ")]
            if len(p) < 6:
                print(f"WARNUNG: Zeile unlesbar in {f.name}: {line[:80]}", file=sys.stderr)
                continue
            rows.append(dict(path=p[0], stufe=p[1], pattern=p[2], thema=p[3], aktuell=p[4], warum=" | ".join(p[5:])))
    return rows


def cmd_plan(args: argparse.Namespace) -> int:
    lauf = lauf_dir(args.lauf)
    rows = parse_triage(lauf)
    if not rows:
        print("Keine Triage-Ergebnisse gefunden.", file=sys.stderr)
        return 1
    by_path = {r["path"]: r for r in rows}
    # Handkorrekturen: overrides.tsv mit `pfad<TAB>stufe[<TAB>pattern]`
    ov = lauf / "overrides.tsv"
    if ov.exists():
        for line in read(ov).splitlines():
            parts = line.split("\t")
            if len(parts) >= 2 and parts[0] in by_path and parts[1] in STUFEN:
                by_path[parts[0]]["stufe"] = parts[1]
                if len(parts) > 2:
                    by_path[parts[0]]["pattern"] = parts[2]
    write(lauf / "worklist.json", json.dumps(rows, ensure_ascii=False, indent=1))
    z = collections.Counter(r["stufe"] for r in rows)
    print("Triage:", dict(z))
    for stufe in ("FAKT", "OFFEN", "IGNORIEREN"):
        for r in rows:
            if r["stufe"] == stufe:
                print(f"  {stufe:10} {Path(r['path']).name[:70]}  ({r['warum'][:50]})")

    def liste(name: str, pfade: list[str]) -> None:
        write(lauf / "lists" / f"{name}.txt", "\n".join(pfade) + "\n")

    fakt = [r["path"] for r in rows if r["stufe"] == "FAKT"]
    for i in range(0, len(fakt), 5):
        liste(f"fakt{i // 5 + 1}", fakt[i : i + 5])
    voll = sorted((r for r in rows if r["stufe"] == "VOLL"), key=lambda r: (r["thema"], r["path"]))
    for i, r in enumerate(voll, 1):
        liste(f"voll{i:02d}", [r["path"]])
    kurz = sorted((r for r in rows if r["stufe"] == "KURZ"), key=lambda r: (r["pattern"], r["path"]))
    if kurz:
        n = -(-len(kurz) // 8)
        size = -(-len(kurz) // n)
        for i in range(n):
            liste(f"kurz{i + 1:02d}", [r["path"] for r in kurz[i * size : (i + 1) * size]])
    (lauf / "reports").mkdir(exist_ok=True)
    listen = sorted(p.stem for p in (lauf / "lists").glob("*.txt"))
    write(lauf / "erwartet.txt", "\n".join(listen) + "\n")
    print(f"{len(listen)} Batches: {', '.join(listen)}")
    print(f"Listen: {rel(lauf / 'lists')}; Reports werden in {rel(lauf / 'reports')} erwartet.")
    return 0


# ---------------------------------------------------------------- apply

def set_status(pfad: Path, status: str, *, note: str | None, source: str | None, heute: str, dry: bool) -> str | None:
    text = read(pfad)
    m = re.match(r"(---\n)(.*?)(\n---\n)", text, re.S)
    if not m:
        return f"kein Frontmatter: {rel(pfad)}"
    fm = m.group(2)
    if len(re.findall(r"^status:", fm, re.M)) != 1:
        return f"status-Feld nicht eindeutig: {rel(pfad)}"
    fm = re.sub(r"^(verarbeitet_am|source_notiz|notiz):.*\n?", "", fm, flags=re.M).rstrip("\n")
    if status == "verarbeitet":
        zusatz = f"\nverarbeitet_am: {heute}\nsource_notiz: {source}"
    else:
        zusatz = '\nnotiz: "%s"' % (note or "").replace('"', "'")
    fm = re.sub(r"^status:.*$", "status: " + status + zusatz, fm, flags=re.M)
    if not dry:
        write(pfad, m.group(1) + fm + m.group(3) + text[m.end():])
    return None


def append_beleg(pattern: str, zeile: str, dry: bool, probleme: list[str]) -> str:
    p = PATTERNS / f"{pattern}.md"
    if not p.exists():
        return "nopattern"
    if not BELEG_RE.match(zeile):
        probleme.append(f"Beleg-Format ({pattern}): {zeile[:90]}")
        return "format"
    text = read(p)
    if zeile in text:
        return "dup"
    lk = re.search(r"\[\[([^\]]+)\]\]", zeile)
    if lk and not (SOURCES / f"{lk.group(1)}.md").exists():
        probleme.append(f"Source-Notiz fehlt für Beleg: {lk.group(1)}")
        return "nosource"
    m = re.search(r"(## Belege\n)(.*?)(\n## )", text, re.S)
    if not m:
        probleme.append(f"Abschnitt '## Belege' fehlt: {pattern}")
        return "nosection"
    neu = text[: m.start(2)] + m.group(2).rstrip("\n") + "\n" + zeile + "\n" + text[m.end(2):]
    if not dry:
        write(p, neu)
    return "ok"


def cmd_apply(args: argparse.Namespace) -> int:
    lauf = lauf_dir(args.lauf)
    reports_dir = lauf / "reports"
    erwartet = read(lauf / "erwartet.txt").split() if (lauf / "erwartet.txt").exists() else []
    if args.alle:
        namen = sorted(p.name.split(".")[0] for p in reports_dir.glob("*.report.md"))
    else:
        namen = args.namen
    if not namen:
        print("Keine Reports angegeben (Namen oder --alle).", file=sys.stderr)
        return 2
    fehlend = [n for n in namen if not (reports_dir / f"{n}.report.md").exists()]
    if fehlend:
        print(f"ABBRUCH: Reports nicht gefunden: {', '.join(fehlend)}", file=sys.stderr)
        return 2
    state_p = lauf / "applied.json"
    state = json.loads(read(state_p)) if state_p.exists() else {"reports": [], "triage_ignoriert": False}
    heute = date.today().isoformat()
    worklist = {Path(r["path"]).name: r for r in json.loads(read(lauf / "worklist.json"))} if (lauf / "worklist.json").exists() else {}
    probleme: list[str] = []
    z = collections.Counter()

    if not state["triage_ignoriert"]:
        for r in worklist.values():
            if r["stufe"] == "IGNORIEREN":
                err = set_status(ROOT / r["path"], "ignoriert", note="Triage: " + r["warum"], source=None, heute=heute, dry=args.dry)
                if err:
                    probleme.append(err)
                else:
                    z["ignoriert_triage"] += 1
        if not args.dry:
            state["triage_ignoriert"] = True

    with (lauf / "fakten.tsv").open("a", encoding="utf-8", newline="\n") as fakten_out, \
         (lauf / "neue_patterns.md").open("a", encoding="utf-8", newline="\n") as neu_out, \
         (lauf / "befunde.txt").open("a", encoding="utf-8", newline="\n") as befund_out:
        for name in namen:
            rid = f"{name}.report.md"
            if rid in state["reports"]:
                continue
            z["reports"] += 1
            cur, blk = None, []

            def flush() -> None:
                nonlocal cur, blk
                if cur and cur[0] == "NEUESPATTERN":
                    neu_out.write(f"## {cur[1]} (aus {rid})\n" + "\n".join(blk) + "\n\n")
                    z["neue_patterns"] += 1
                cur, blk = None, []

            for ln in read(reports_dir / rid).splitlines():
                m = re.match(r"@@(\w+)\s*(.*)$", ln)
                if m:
                    flush()
                    kind, rest = m.group(1), m.group(2).strip()
                    if kind == "STATUS":
                        sm = re.match(r"(VERARBEITET|IGNORIERT|KEIN_MEHRWERT)\s+(\S+\.md)(?:\s*=>\s*(\S+\.md))?(?:\s*::\s*(.*))?$", rest)
                        if not sm:
                            probleme.append(f"STATUS unlesbar ({rid}): {rest[:80]}")
                            continue
                        st, base, ziel, note = sm.groups()
                        pfad = next((ROOT / r["path"] for n, r in worklist.items() if n == base), None)
                        if pfad is None:
                            pfad = next((p for p in inbox_notizen() if p.name == base), None)
                        if pfad is None:
                            probleme.append(f"Inbox-Datei unbekannt: {base}")
                            continue
                        if st == "VERARBEITET":
                            src = "80_Knowledge/Sources/" + (ziel or base)
                            if not (ROOT / src).exists():
                                probleme.append(f"Source-Notiz fehlt: {src}")
                                continue
                            err = set_status(pfad, "verarbeitet", note=None, source=src, heute=heute, dry=args.dry)
                            z["verarbeitet"] += 0 if err else 1
                        else:
                            err = set_status(pfad, "ignoriert", note=note or st, source=None, heute=heute, dry=args.dry)
                            z["ignoriert"] += 0 if err else 1
                        if err:
                            probleme.append(err)
                    elif kind == "BELEG":
                        cur = ("BELEG", rest)
                    elif kind == "NEUESPATTERN":
                        cur = ("NEUESPATTERN", rest)
                    elif kind == "FAKT":
                        fakten_out.write(rest.lstrip("| ").replace(" | ", "\t") + "\n")
                        z["fakten"] += 1
                    elif kind == "BEFUND":
                        befund_out.write(f"[{rid}] {rest}\n")
                    continue
                if cur and cur[0] == "BELEG" and ln.startswith("- "):
                    r = append_beleg(cur[1], ln.strip(), args.dry, probleme)
                    z["belege" if r == "ok" else ("belege_dup" if r == "dup" else "belege_offen")] += 1
                    if r == "nopattern":
                        probleme.append(f"Beleg für unbekanntes Pattern {cur[1]}: {ln.strip()[:80]}")
                elif cur and cur[0] == "NEUESPATTERN":
                    blk.append(ln)
            flush()
            if not args.dry:
                state["reports"].append(rid)

    if not args.dry:
        write(state_p, json.dumps(state))
    if probleme:
        with (lauf / "probleme.txt").open("a", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(probleme) + "\n")

    print(dict(z))
    offen = [n for n in erwartet if n not in {p.name.split(".")[0] for p in reports_dir.glob("*.report.md")}]
    if offen and args.alle:
        print(f"HINWEIS: Für diese geplanten Batches gibt es noch keinen Report: {', '.join(offen)}")
    print(f"Probleme: {len(probleme)}")
    for p in probleme[:15]:
        print(" -", p)
    return 1 if probleme else 0


# ---------------------------------------------------------------- fakten

def cmd_fakten(args: argparse.Namespace) -> int:
    lauf = lauf_dir(args.lauf)
    tsv = lauf / "fakten.tsv"
    neu = [l.split("\t") for l in read(tsv).splitlines() if l.strip()] if tsv.exists() else []
    bestand: list[list[str]] = []
    if FAKTEN.exists():
        kat = None
        rueck = {v: k for k, v in FAKT_TITEL.items()}
        for line in read(FAKTEN).splitlines():
            if line.startswith("## "):
                kat = rueck.get(line[3:].strip())
            m = re.match(r"\| (\d{4}-\d{2}-\d{2}) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$", line)
            if m and kat:
                bestand.append([m.group(1), kat, m.group(2), m.group(3), m.group(4), m.group(5)])
    alle, seen = [], set()
    for r in bestand + [r for r in neu if len(r) >= 6]:
        key = tuple(x.strip() for x in r[:6])
        if key not in seen:
            seen.add(key)
            alle.append(list(key))
    if not alle:
        print("Keine Fakten vorhanden.")
        return 0
    esc = lambda s: s.replace("|", "/").strip()
    zeilen = [
        "# Fakten: Modelle, Preise, Benchmarks", "", f"**Stand:** {date.today().isoformat()}", "",
        "Datierte Einzelangaben aus den verarbeiteten Quellen (`80_Knowledge/Sources/`). Anders als ein Pattern beschreibt dieses Register keine Arbeitsweise, sondern hält fest, **wer was wann gemessen oder angekündigt hat**. Jede Zeile führt Datum, Gegenstand, Aussage, Einschränkung und Quelle.",
        "", "## Lesehinweise", "",
        "- Zahlen sind **nur innerhalb derselben Messung vergleichbar**. Artificial-Analysis-Indizes tragen Versionsnummern (der Juli-Bericht nennt Opus 5 mit 61 Punkten im Intelligence Index v4.1, die September-Posts nennen 51 Punkte in v4.3). Kosten pro Task im Intelligence Index und im Coding Agent Index sind verschiedene Messungen.",
        "- Herstellerangaben und Drittmessungen stehen in der Spalte „Einschränkung“. Ein Eintrag ohne Vermerk ist keine Bestätigung.",
        "- Preise und Modellnamen verfallen. Neue Angaben werden als neue Zeile ergänzt, alte bleiben mit ihrem Datum stehen.", "",
    ]
    for kat in FAKT_KATEGORIEN:
        rs = [r for r in alle if r[1] == kat]
        if not rs:
            continue
        zeilen += [f"## {FAKT_TITEL[kat]}", "", "| Datum | Gegenstand | Aussage | Einschränkung | Quelle |", "|---|---|---|---|---|"]
        for r in sorted(rs, key=lambda x: (x[0], x[2]), reverse=True):
            zeilen.append(f"| {r[0]} | {esc(r[2])} | {esc(r[3])} | {esc(r[4])} | {r[5]} |")
        zeilen.append("")
    if not args.dry:
        write(FAKTEN, "\n".join(zeilen))
    print(f"Fakten-Register: {len(alle)} Zeilen ({len(bestand)} bestehend, {len(alle) - len(bestand)} neu)")
    return 0


# ---------------------------------------------------------------- check

def cmd_check(args: argparse.Namespace) -> int:
    st = collections.Counter()
    fehler = []
    referenziert = set()
    for p in inbox_notizen():
        fm, _ = frontmatter(read(p))
        s = feld(fm, "status")
        if not s:
            continue
        st[s] += 1
        if s == "verarbeitet":
            sn = feld(fm, "source_notiz")
            if not sn or not (ROOT / sn).exists():
                fehler.append(f"verarbeitet ohne Source-Datei: {rel(p)}")
    for s in SOURCES.glob("*.md"):
        fm, _ = frontmatter(read(s))
        for k in ("rohquelle", "zweitquelle"):
            v = feld(fm, k)
            if v:
                referenziert.add(v)
    for p in inbox_notizen():
        fm, _ = frontmatter(read(p))
        if feld(fm, "status") == "neu" and rel(p) in referenziert:
            fehler.append(f"status neu, aber Source-Notiz existiert: {rel(p)}")
    print("Inbox-Status:", dict(st))
    for f in fehler:
        print(" -", f)
    print("Konsistent." if not fehler else f"{len(fehler)} Inkonsistenzen.")
    return 1 if fehler else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("prep", "plan", "apply", "fakten", "check"):
        sp = sub.add_parser(name)
        sp.add_argument("--lauf", help="Name des Laufs (Standard: heutiges Datum)")
        if name == "prep":
            sp.add_argument("--batch", type=int, default=32, help="Quellen pro Triage-Batch")
            sp.add_argument("--zeichen", type=int, default=700, help="Länge des Auszugs")
        if name == "apply":
            sp.add_argument("namen", nargs="*", help="Report-Namen, z. B. voll01 kurz02")
            sp.add_argument("--alle", action="store_true", help="alle vorhandenen Reports")
            sp.add_argument("--dry", action="store_true")
        if name == "fakten":
            sp.add_argument("--dry", action="store_true")
    args = ap.parse_args()
    return {"prep": cmd_prep, "plan": cmd_plan, "apply": cmd_apply, "fakten": cmd_fakten, "check": cmd_check}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
