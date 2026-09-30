"""Themencluster für das Knowledge-System (80_Knowledge/Themen/).

Verknüpft Sources und Patterns thematisch, damit beim Ingest verwandte Notizen
gefunden werden und Blog-Beiträge auf einem sauberen Keyword- und Quellenbriefing
aufbauen. Führende Dateien: 80_Knowledge/Themen/themen.yaml (Taxonomie) und
80_Knowledge/Themen/zuordnung.yaml (Zuordnung je Notiz). Die Notizen selbst
bleiben unverändert (README-Invariante 2).

Befehle:
    check                        Zuordnung prüfen (jede Notiz zugeordnet, IDs gültig)
    check --abgleich             zusätzlich Textscoring gegen die Zuordnung halten
    zuordnen <datei>...          Cluster, Keywords, verwandte Notizen vorschlagen
    zuordnen --neu               alle Sources ohne Eintrag vorschlagen
      --uebernehmen              Vorschlag in zuordnung.yaml schreiben
      --haupt ID --neben ID --kw "a;b"   Vorschlag überschreiben (nur mit einer Datei)
    verwandt <slug>              verwandte Sources und Patterns (TF-IDF)
    luecken                      Patterns, die thematisch zusammengehören, sich aber nicht verlinken
    index                        Hub-Notizen unter 80_Knowledge/Themen/ neu erzeugen
    blog <cluster-id|Suchbegriff>  Briefing für einen Blogbeitrag

Nutzung: python 70_Scripts/themen.py <befehl>. Standardbibliothek und PyYAML.
"""

from __future__ import annotations

import argparse
import collections
import math
import re
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "80_Knowledge"
THEMEN = KNOWLEDGE / "Themen"
TAXONOMIE = THEMEN / "themen.yaml"
ZUORDNUNG = THEMEN / "zuordnung.yaml"
POSTS = ROOT / "blog" / "posts"

MIN_SCORE = 6.0          # darunter: Quelle passt vermutlich in keinen Cluster
NEBEN_ANTEIL = 0.55      # Nebencluster ab diesem Anteil des besten Scores
MAX_NEBEN = 2
GROSSER_CLUSTER = 35

STOP = set("""
aber alle allem allen aller alles als also auch auf aus bei bin bis bist damit dann das dass dein deine dem den der des die dies diese diesem diesen dieser dieses doch dort durch ein eine einem einen einer eines einfach er es etwa euch für gegen gibt hat hier hin ihr ihre immer im in ist ja jede jedem jeden jeder jedes kann kein keine man mehr mit muss nach nicht noch nun nur ob oder ohne sehr sein seine sich sie sind so über um und uns unter vom von vor war was weil wenn wer wie wieder wir wird wo zu zum zur
the and for that with this from are was were you your not but can will has have its into than then they them their there what when which who how also more most other some such only own same too very just about over under out
""".split())


# ---------- Laden ----------

def lade_yaml(pfad: Path) -> dict:
    return yaml.safe_load(pfad.read_text(encoding="utf-8")) or {}


def lade_taxonomie() -> dict:
    return lade_yaml(TAXONOMIE)["cluster"]


def lade_zuordnung() -> dict:
    d = lade_yaml(ZUORDNUNG)
    d.setdefault("quellen", {})
    d.setdefault("muster", {})
    return d


def speichere_zuordnung(d: dict) -> None:
    text = ZUORDNUNG.read_text(encoding="utf-8")
    kopf = []
    for zeile in text.splitlines():
        if zeile.startswith("muster:") or zeile.startswith("quellen:"):
            break
        kopf.append(zeile)
    body = yaml.safe_dump(d, allow_unicode=True, sort_keys=True, width=200, default_flow_style=None)
    ZUORDNUNG.write_text("\n".join(kopf).rstrip("\n") + "\n\n" + body, encoding="utf-8", newline="\n")


def notizen(art: str) -> list[Path]:
    return sorted((KNOWLEDGE / art).glob("*.md"))


def lese(pfad: Path) -> str:
    return pfad.read_text(encoding="utf-8").replace("\r\n", "\n")


def ohne_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        ende = text.find("\n---", 4)
        if ende != -1:
            return text[ende + 4:]
    return text


def titel_von(text: str, fallback: str) -> str:
    for zeile in ohne_frontmatter(text).splitlines():
        if zeile.startswith("# "):
            return zeile[2:].strip()
    return fallback


def abschnitt(text: str, ueberschrift: str) -> list[str]:
    zeilen, drin = [], False
    for zeile in text.splitlines():
        if zeile.startswith("## "):
            drin = zeile.strip() == ueberschrift
            continue
        if drin:
            zeilen.append(zeile)
    return zeilen


def datum_von(slug: str) -> str:
    m = re.match(r"(\d{4}-\d{2}-\d{2})", slug)
    return m.group(1) if m else ""


# ---------- Scoring ----------

def _regex(term: str) -> re.Pattern:
    return re.compile(r"(?<![a-zäöüß0-9])" + re.escape(term.lower()))


def kompiliere(taxo: dict) -> dict:
    return {
        cid: {
            "kern": [(t, _regex(t)) for t in c.get("kern", [])],
            "weit": [(t, _regex(t)) for t in c.get("weit", [])],
        }
        for cid, c in taxo.items()
    }


def bewerte(text: str, regeln: dict) -> dict[str, tuple[float, list[tuple[str, int]]]]:
    text = text.lower()
    ergebnis = {}
    for cid, r in regeln.items():
        summe, treffer = 0.0, []
        for gewicht, liste in ((3, r["kern"]), (1, r["weit"])):
            for term, rx in liste:
                n = len(rx.findall(text))
                if n:
                    summe += gewicht * (1 + math.log(n))
                    treffer.append((gewicht, term, n))
        treffer.sort(key=lambda x: (-x[0], -x[2]))   # trennscharfe Kern-Begriffe vor weiten
        ergebnis[cid] = (summe, [(t, n) for _, t, n in treffer])
    return ergebnis


def rangliste(scores: dict) -> list[tuple[str, float]]:
    return sorted(((c, s) for c, (s, _) in scores.items()), key=lambda x: -x[1])


# ---------- TF-IDF ----------

def tokens(text: str) -> list[str]:
    woerter = [w for w in re.findall(r"[a-zäöüß][a-zäöüß0-9_.\-]{2,}", text.lower()) if w not in STOP]
    return woerter + [f"{a} {b}" for a, b in zip(woerter, woerter[1:])]


class Korpus:
    def __init__(self) -> None:
        self.docs: dict[str, tuple[str, str]] = {}   # slug -> (art, text)
        for art in ("Sources", "Patterns"):
            for p in notizen(art):
                self.docs[p.stem] = (art, ohne_frontmatter(lese(p)))
        df = collections.Counter()
        self.tf: dict[str, collections.Counter] = {}
        for slug, (_, text) in self.docs.items():
            c = collections.Counter(tokens(text))
            self.tf[slug] = c
            df.update(c.keys())
        n = len(self.docs)
        self.idf = {t: math.log((n + 1) / (d + 1)) + 1 for t, d in df.items() if d <= 0.5 * n}
        self.vec = {s: self._vec(c) for s, c in self.tf.items()}

    def _vec(self, c: collections.Counter) -> dict[str, float]:
        v = {t: (1 + math.log(n)) * self.idf[t] for t, n in c.items() if t in self.idf}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        return {t: x / norm for t, x in v.items()}

    def aehnlich(self, text: str, ausser: str = "", art: str = "", n: int = 5) -> list[tuple[str, float]]:
        v = self._vec(collections.Counter(tokens(text)))
        treffer = []
        for slug, w in self.vec.items():
            if slug == ausser or (art and self.docs[slug][0] != art):
                continue
            kleiner, groesser = (v, w) if len(v) < len(w) else (w, v)
            sim = sum(x * groesser.get(t, 0.0) for t, x in kleiner.items())
            treffer.append((slug, sim))
        treffer.sort(key=lambda x: -x[1])
        return treffer[:n]


# ---------- Hilfen ----------

def notiz_pfad(arg: str) -> Path:
    p = Path(arg)
    if p.is_file():
        return p.resolve()
    for art in ("Sources", "Patterns"):
        kandidat = KNOWLEDGE / art / (Path(arg).stem + ".md")
        if kandidat.is_file():
            return kandidat
    raise SystemExit(f"Notiz nicht gefunden: {arg}")


def art_von(pfad: Path) -> str:
    return "quellen" if pfad.parent.name == "Sources" else "muster"


def kernaussage(text: str) -> str:
    absaetze = [a.strip() for a in ohne_frontmatter(text).split("\n\n")]
    for a in absaetze:
        if a and not a.startswith("#") and not a.startswith("!") and not a.startswith("-"):
            satz = re.split(r"(?<=[.!?])\s", a.replace("\n", " "))[0]
            return satz[:200].rstrip()
    return ""


def vorschlag(pfad: Path, regeln: dict, taxo: dict, korpus: Korpus) -> dict:
    text = ohne_frontmatter(lese(pfad))
    scores = bewerte(text, regeln)
    rang = rangliste(scores)
    top, top_score = rang[0]
    neben = [c for c, s in rang[1:1 + MAX_NEBEN] if s >= NEBEN_ANTEIL * top_score and s >= MIN_SCORE]
    treffer = scores[top][1]
    kw = [t for t, _ in treffer[:8]]
    for c in neben:
        kw += [t for t, _ in scores[c][1][:2]]
    return {
        "haupt": top if top_score >= MIN_SCORE else None,
        "neben": neben if top_score >= MIN_SCORE else [],
        "keywords": kw[:10],
        "kernaussage": kernaussage(lese(pfad)),
        "rang": rang[:4],
        "top_score": top_score,
        "aehnlich_quellen": korpus.aehnlich(text, ausser=pfad.stem, art="Sources", n=5),
        "aehnlich_muster": korpus.aehnlich(text, ausser=pfad.stem, art="Patterns", n=3),
    }


# ---------- Befehle ----------

def cmd_check(args) -> int:
    taxo, zu = lade_taxonomie(), lade_zuordnung()
    ids = set(taxo)
    fehler, hinweise = [], []
    for art, ordner in (("quellen", "Sources"), ("muster", "Patterns")):
        dateien = {p.stem for p in notizen(ordner)}
        for slug in sorted(dateien - set(zu[art])):
            fehler.append(f"{ordner}/{slug}: keine Zuordnung in zuordnung.yaml (themen.py zuordnen --neu)")
        for slug in sorted(set(zu[art]) - dateien):
            fehler.append(f"zuordnung.yaml: {slug} existiert nicht in {ordner}/")
        for slug, e in zu[art].items():
            if e.get("haupt") not in ids:
                fehler.append(f"{slug}: unbekannter Haupt-Cluster '{e.get('haupt')}'")
            for n in e.get("neben", []):
                if n not in ids:
                    fehler.append(f"{slug}: unbekannter Nebencluster '{n}'")
            if len(e.get("neben", [])) > MAX_NEBEN:
                hinweise.append(f"{slug}: mehr als {MAX_NEBEN} Nebencluster")
            if not e.get("keywords"):
                hinweise.append(f"{slug}: keine Keywords")
    zaehl = collections.Counter(e["haupt"] for e in zu["quellen"].values() if e.get("haupt"))
    for cid in ids:
        if zaehl[cid] == 0:
            hinweise.append(f"Cluster {cid}: keine Quelle als Haupt-Cluster")
        elif zaehl[cid] > GROSSER_CLUSTER:
            hinweise.append(f"Cluster {cid}: {zaehl[cid]} Quellen, Aufteilung prüfen")
    if args.abgleich:
        regeln, korpus = kompiliere(taxo), Korpus()
        abweichend = 0
        for slug, e in sorted(zu["quellen"].items()):
            art, text = korpus.docs.get(slug, ("", ""))
            if not text:
                continue
            rang = rangliste(bewerte(text, regeln))
            top3 = [c for c, _ in rang[:3]]
            if e.get("haupt") not in top3:
                abweichend += 1
                hinweise.append(f"Abgleich {slug}: zugeordnet {e['haupt']}, Scoring {', '.join(top3)}")
        print(f"Abgleich: {abweichend} von {len(zu['quellen'])} Quellen mit Haupt-Cluster außerhalb der Scoring-Top-3")
    for h in hinweise:
        print(f"HINWEIS {h}")
    for f in fehler:
        print(f"FEHLER  {f}")
    if fehler:
        print(f"\n{len(fehler)} Fehler.")
        return 1
    print(f"OK: {len(zu['quellen'])} Quellen und {len(zu['muster'])} Patterns in {len(ids)} Clustern zugeordnet.")
    return 0


def zeige_vorschlag(pfad: Path, v: dict, taxo: dict) -> None:
    print(f"\n● {pfad.stem}")
    rang = ", ".join(f"{taxo[c]['name']} ({s:.0f})" for c, s in v["rang"])
    print(f"  Scoring: {rang}")
    if v["haupt"]:
        print(f"  Vorschlag: haupt={v['haupt']}  neben={v['neben'] or '-'}")
    else:
        print(f"  ⚠ Kein Cluster über der Schwelle ({MIN_SCORE:.0f}): vermutlich neues Thema oder Taxonomie-Lücke → Frage an Philipp")
    print(f"  Keywords: {'; '.join(v['keywords'])}")
    print("  Verwandte Sources: " + ", ".join(f"[[{s}]] ({x:.2f})" for s, x in v["aehnlich_quellen"][:5]))
    print("  Verwandte Patterns: " + ", ".join(f"[[{s}]] ({x:.2f})" for s, x in v["aehnlich_muster"][:3]))


def cmd_zuordnen(args) -> int:
    taxo, zu = lade_taxonomie(), lade_zuordnung()
    regeln, korpus = kompiliere(taxo), Korpus()
    if args.neu:
        pfade = [p for p in notizen("Sources") if p.stem not in zu["quellen"]]
        pfade += [p for p in notizen("Patterns") if p.stem not in zu["muster"]]
        if not pfade:
            print("Alle Notizen sind zugeordnet.")
            return 0
    else:
        pfade = [notiz_pfad(a) for a in args.dateien]
    if not pfade:
        raise SystemExit("Datei angeben oder --neu verwenden.")
    if len(pfade) > 1 and (args.haupt or args.neben or args.kw):
        raise SystemExit("--haupt/--neben/--kw nur mit genau einer Datei.")
    geschrieben = 0
    for pfad in pfade:
        v = vorschlag(pfad, regeln, taxo, korpus)
        zeige_vorschlag(pfad, v, taxo)
        if not args.uebernehmen:
            continue
        haupt = args.haupt or v["haupt"]
        if not haupt:
            print("  → nicht übernommen (kein Cluster); mit --haupt ID erzwingen")
            continue
        neben = [n for n in (args.neben or ",".join(v["neben"])).split(",") if n and n != haupt]
        for cid in [haupt, *neben]:
            if cid not in taxo:
                raise SystemExit(f"Unbekannte Cluster-ID: {cid}")
        kw = [k.strip() for k in args.kw.split(";")] if args.kw else v["keywords"]
        eintrag = {"haupt": haupt, "neben": neben[:MAX_NEBEN], "keywords": kw}
        if art_von(pfad) == "quellen":
            eintrag["kernaussage"] = v["kernaussage"]
        else:
            eintrag["synonyme"] = []
        zu[art_von(pfad)][pfad.stem] = eintrag
        geschrieben += 1
        print(f"  → übernommen: haupt={haupt} neben={neben or '-'}")
    if geschrieben:
        speichere_zuordnung(zu)
        print(f"\n{geschrieben} Eintrag/Einträge in zuordnung.yaml geschrieben. Danach: themen.py index")
    return 0


def cmd_verwandt(args) -> int:
    korpus = Korpus()
    pfad = notiz_pfad(args.slug)
    text = ohne_frontmatter(lese(pfad))
    zu = lade_zuordnung()
    e = zu[art_von(pfad)].get(pfad.stem, {})
    print(f"{pfad.stem}  (haupt={e.get('haupt', '?')}, neben={e.get('neben', [])})")
    print("Sources:  " + ", ".join(f"[[{s}]] ({x:.2f})" for s, x in korpus.aehnlich(text, pfad.stem, "Sources", 8)))
    print("Patterns: " + ", ".join(f"[[{s}]] ({x:.2f})" for s, x in korpus.aehnlich(text, pfad.stem, "Patterns", 5)))
    return 0


def verwandte_links(text: str) -> set[str]:
    return {m.group(1).strip() for m in re.finditer(r"\[\[([^\]|]+)", "\n".join(abschnitt(text, "## Verwandte Patterns")))}


def cmd_luecken(args) -> int:
    zu = lade_zuordnung()["muster"]
    links = {p.stem: verwandte_links(lese(p)) for p in notizen("Patterns")}
    namen = sorted(links)

    def begriffe(slug: str) -> set[str]:
        e = zu.get(slug, {})
        return {w.lower() for w in e.get("keywords", []) + e.get("synonyme", [])}

    kandidaten = []
    for i, a in enumerate(namen):
        for b in namen[i + 1:]:
            if b in links[a] or a in links[b]:
                continue
            ea, eb = zu.get(a, {}), zu.get(b, {})
            cl_a, cl_b = {ea.get("haupt"), *ea.get("neben", [])}, {eb.get("haupt"), *eb.get("neben", [])}
            gemeinsam_cl = len(cl_a & cl_b)
            gemeinsam_kw = begriffe(a) & begriffe(b)
            punkte = 2 * (ea.get("haupt") == eb.get("haupt")) + gemeinsam_cl + 2 * len(gemeinsam_kw)
            if punkte >= args.min:
                kandidaten.append((punkte, a, b, sorted(gemeinsam_kw)))
    kandidaten.sort(key=lambda x: (-x[0], x[1], x[2]))
    print(f"{len(kandidaten)} Paare ohne gegenseitigen Link (Mindestpunkte {args.min}); die obersten {args.top}:\n")
    for punkte, a, b, kw in kandidaten[: args.top]:
        print(f"  {punkte:>2}  [[{a}]] ↔ [[{b}]]" + (f"   gemeinsam: {', '.join(kw)}" if kw else ""))
    return 0


def blog_posts() -> list[dict]:
    posts = []
    for p in sorted(POSTS.glob("*.md")):
        text = lese(p)
        if not text.startswith("---\n"):
            continue
        fm = yaml.safe_load(text[4:text.find("\n---", 4)]) or {}
        fm["_slug"] = p.stem
        posts.append(fm)
    return posts


def mitglieder(zu: dict, cid: str) -> dict[str, list[str]]:
    return {
        art: [s for s, e in zu[art].items() if e.get("haupt") == cid] for art in ("quellen", "muster")
    } | {
        "quellen_neben": [s for s, e in zu["quellen"].items() if cid in e.get("neben", []) and e.get("haupt") != cid],
        "muster_neben": [s for s, e in zu["muster"].items() if cid in e.get("neben", []) and e.get("haupt") != cid],
    }


def haeufige_keywords(zu: dict, slugs: list[str], n: int = 25) -> list[tuple[str, int]]:
    c = collections.Counter()
    for s in slugs:
        e = zu["quellen"].get(s) or zu["muster"].get(s) or {}
        c.update({k.strip().lower() for k in e.get("keywords", [])})
    return c.most_common(n)


def konfidenz(slug: str) -> str:
    for zeile in lese(KNOWLEDGE / "Patterns" / f"{slug}.md").splitlines():
        m = re.match(r"\*\*Konfidenz:\*\*\s+(\S+)", zeile)
        if m:
            return m.group(1)
    return "?"


def beleganzahl(slug: str) -> int:
    return sum(1 for z in abschnitt(lese(KNOWLEDGE / "Patterns" / f"{slug}.md"), "## Belege") if z.startswith("- "))


def dateiname_hub(name: str) -> str:
    return "Thema-" + re.sub(r"[^\wäöüÄÖÜß]+", "-", name).strip("-")


def cmd_index(args) -> int:
    taxo, zu = lade_taxonomie(), lade_zuordnung()
    THEMEN.mkdir(exist_ok=True)
    hub = {cid: dateiname_hub(c["name"]) for cid, c in taxo.items()}
    heute = date.today().isoformat()
    quellen_titel = {s: titel_von(lese(KNOWLEDGE / "Sources" / f"{s}.md"), s) for s in zu["quellen"]}
    zeilen_uebersicht = []
    for cid, c in taxo.items():
        m = mitglieder(zu, cid)
        alle = m["quellen"] + m["muster"]
        kw = haeufige_keywords(zu, alle + m["quellen_neben"], 20)
        out = [f"# {c['name']}", "",
               f"*Automatisch erzeugt von `70_Scripts/themen.py index` am {heute}. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*", "",
               c["beschreibung"], "",
               "## Suchbegriffe", "",
               f"- **Hauptkeyword:** {c['blog']['hauptkeyword']}",
               "- **Long-Tail:** " + "; ".join(c["blog"]["longtail"]),
               "- **Fragen:** " + " / ".join(c["blog"]["fragen"]),
               "- **Häufig in den Quellen:** " + ", ".join(f"{k} ({n})" if n > 1 else k for k, n in kw), "",
               "## Verwandte Themen", ""]
        out += [f"- [[{hub[v]}]] — {taxo[v]['name']}" for v in c.get("verwandt", [])]
        out += ["", f"## Patterns ({len(m['muster'])})", ""]
        for s in sorted(m["muster"]):
            out.append(f"- [[{s}]] · {konfidenz(s)} · {beleganzahl(s)} Belege")
        if m["muster_neben"]:
            out += ["", "Weitere Patterns mit diesem Thema als Nebenthema: " + ", ".join(f"[[{s}]]" for s in sorted(m["muster_neben"]))]
        out += ["", f"## Quellen ({len(m['quellen'])})", ""]
        for s in sorted(m["quellen"], reverse=True):
            k = zu["quellen"][s].get("kernaussage", "")
            out.append(f"- [[{s}]] — {k}" if k else f"- [[{s}]] — {quellen_titel[s]}")
        if m["quellen_neben"]:
            out += ["", "## Quellen mit diesem Thema als Nebenthema", ""]
            out += [f"- [[{s}]]" for s in sorted(m["quellen_neben"], reverse=True)]
        (THEMEN / f"{hub[cid]}.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
        zeilen_uebersicht.append((c["name"], hub[cid], len(m["quellen"]), len(m["muster"]), c["blog"]["hauptkeyword"]))

    uebersicht = ["# Themen-Übersicht", "",
                  f"*Automatisch erzeugt von `70_Scripts/themen.py index` am {heute}.*", "",
                  "Jede Source und jedes Pattern hat einen Haupt-Cluster und höchstens zwei Nebencluster. Ein Cluster bündelt die Notizen eines Themas samt Suchbegriffen für Blog-Beiträge. Beim Ingest schlägt `python 70_Scripts/themen.py zuordnen <datei>` Cluster und verwandte Notizen vor.", "",
                  "| Thema | Hub-Notiz | Quellen | Patterns | Hauptkeyword |", "|---|---|---|---|---|"]
    for name, h, nq, nm, kw in sorted(zeilen_uebersicht, key=lambda x: -x[2]):
        uebersicht.append(f"| {name} | [[{h}]] | {nq} | {nm} | {kw} |")
    (THEMEN / "Themen-Übersicht.md").write_text("\n".join(uebersicht) + "\n", encoding="utf-8", newline="\n")

    kw_cluster: dict[str, set[str]] = collections.defaultdict(set)
    kw_zahl = collections.Counter()
    for art in ("quellen", "muster"):
        for s, e in zu[art].items():
            for k in {x.strip().lower() for x in e.get("keywords", [])}:
                kw_zahl[k] += 1
                kw_cluster[k].add(taxo[e["haupt"]]["name"])
    reg = ["# Keyword-Register", "",
           f"*Automatisch erzeugt von `70_Scripts/themen.py index` am {heute}.*", "",
           "Begriffe, die in mindestens zwei Notizen vorkommen. Sie zeigen, worüber das Wissen schon mehrfach belegt ist, und taugen als Suchbegriffe für Blog-Beiträge.", "",
           "| Keyword | Notizen | Themen |", "|---|---|---|"]
    for k, n in sorted(kw_zahl.items(), key=lambda x: (-x[1], x[0])):
        if n >= 2:
            reg.append(f"| {k} | {n} | {', '.join(sorted(kw_cluster[k]))} |")
    (THEMEN / "Keyword-Register.md").write_text("\n".join(reg) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(taxo)} Hub-Notizen, Themen-Übersicht und Keyword-Register in {THEMEN.relative_to(ROOT)} geschrieben.")
    return 0


def cmd_blog(args) -> int:
    taxo, zu = lade_taxonomie(), lade_zuordnung()
    such = args.thema.lower()
    cid = such if such in taxo else next(
        (i for i, c in taxo.items() if such in c["name"].lower() or such == c["blog"]["hauptkeyword"].lower()), None)
    if cid is None:
        treffer = sorted(
            [(sum(such in k.lower() for k in e.get("keywords", [])), s, art)
             for art in ("quellen", "muster") for s, e in zu[art].items()], reverse=True)
        treffer = [t for t in treffer if t[0]]
        print(f"Kein Cluster '{args.thema}'. Notizen mit passendem Keyword:")
        for _, s, art in treffer[:15]:
            print(f"  [{'Source' if art == 'quellen' else 'Pattern'}] {s}  (haupt={zu[art][s]['haupt']})")
        return 1 if not treffer else 0
    c = taxo[cid]
    m = mitglieder(zu, cid)
    posts = blog_posts()
    genutzt: dict[str, list[str]] = collections.defaultdict(list)
    for p in posts:
        for q in p.get("quellen") or []:
            genutzt[q].append(p["_slug"])
    print(f"# Blog-Briefing: {c['name']} ({cid})\n\n{c['beschreibung']}\n")
    print(f"Hauptkeyword: {c['blog']['hauptkeyword']}")
    print("Long-Tail:    " + "; ".join(c["blog"]["longtail"]))
    print("Fragen:       " + " / ".join(c["blog"]["fragen"]))
    kw = haeufige_keywords(zu, m["quellen"] + m["muster"] + m["quellen_neben"], 30)
    print("\nBegriffe aus den Quellen (Häufigkeit): " + ", ".join(f"{k} ({n})" if n > 1 else k for k, n in kw))
    print("Verwandte Themen (für interne Verweise): " + ", ".join(taxo[v]["name"] for v in c.get("verwandt", [])))
    print(f"\n## Patterns ({len(m['muster'])})")
    for s in sorted(m["muster"], key=lambda x: -beleganzahl(x)):
        print(f"- {s} · {konfidenz(s)} · {beleganzahl(s)} Belege")
        spann = [z[2:].strip() for z in abschnitt(lese(KNOWLEDGE / 'Patterns' / f'{s}.md'), "## Spannungen & offene Fragen")
                 if z.startswith("- ") and "keine bekannt" not in z.lower()]
        if spann:
            print(f"    Spannung (Duell-Stoff): {spann[0][:180]}")
    print(f"\n## Quellen ({len(m['quellen'])}, neueste zuerst; ✓ = schon in einem Beitrag)")
    for s in sorted(m["quellen"], reverse=True):
        marke = "✓ " + ", ".join(genutzt[s]) if s in genutzt else "· offen"
        print(f"- {s} [{marke}]\n    {zu['quellen'][s].get('kernaussage', '')}")
    if m["quellen_neben"]:
        print(f"\n## Nebenthema-Quellen ({len(m['quellen_neben'])})")
        for s in sorted(m["quellen_neben"], reverse=True)[:12]:
            print(f"- {s} [{'✓' if s in genutzt else '· offen'}]")
    vorhandene = [p for p in posts if set(p.get("quellen") or []) & set(m["quellen"] + m["quellen_neben"])]
    print(f"\n## Bestehende Beiträge zum Thema ({len(vorhandene)})")
    for p in vorhandene:
        print(f"- {p['_slug']} ({p.get('kategorie')}, {p.get('status')})")
    offen = [s for s in m["quellen"] if s not in genutzt]
    print(f"\n→ {len(offen)} von {len(m['quellen'])} Haupt-Quellen noch in keinem Beitrag. Zahlen und Preise vor Verwendung gegen das Fakten-Register prüfen.")
    return 0


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("check")
    p.add_argument("--abgleich", action="store_true")
    p.set_defaults(fn=cmd_check)
    p = sub.add_parser("zuordnen")
    p.add_argument("dateien", nargs="*")
    p.add_argument("--neu", action="store_true")
    p.add_argument("--uebernehmen", action="store_true")
    p.add_argument("--haupt")
    p.add_argument("--neben")
    p.add_argument("--kw")
    p.set_defaults(fn=cmd_zuordnen)
    p = sub.add_parser("verwandt")
    p.add_argument("slug")
    p.set_defaults(fn=cmd_verwandt)
    p = sub.add_parser("luecken")
    p.add_argument("--min", type=int, default=3)
    p.add_argument("--top", type=int, default=25)
    p.set_defaults(fn=cmd_luecken)
    p = sub.add_parser("index")
    p.set_defaults(fn=cmd_index)
    p = sub.add_parser("blog")
    p.add_argument("thema")
    p.set_defaults(fn=cmd_blog)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
