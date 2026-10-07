#!/usr/bin/env python3
"""Statischer Blog-Generator: Markdown-Beiträge -> HTML, RSS, Sitemap.

Nutzung:
    python blog/build_blog.py                 # nur status: freigegeben nach blog/_site
    python blog/build_blog.py --drafts        # Entwürfe zusätzlich, nach blog/_preview
    python blog/build_blog.py --check         # nur prüfen, nichts schreiben
    python blog/build_blog.py --freigeben SLUG  # prüfen, dann status: freigegeben und geprueft_am setzen
    python blog/build_blog.py --auto-freigeben  # alle Entwürfe ohne Fehler und Hinweise freigeben (sofort)
    python blog/build_blog.py --ping            # nach dem Deployment: WebSub-Hub über neue Feeds informieren

Beiträge liegen in blog/posts/*.md. Nur Beiträge mit `status: freigegeben` und einem
Datum bis heute erscheinen im öffentlichen Build. Das ist die Freigabe-Schranke:
Ein Entwurf kann nicht versehentlich in Seite oder Feed landen.

Abhängigkeiten: markdown-it-py, PyYAML (pip install markdown-it-py pyyaml).
"""

from __future__ import annotations

import argparse
import functools
import html
import re
import shutil
import sys
import urllib.parse
import urllib.request
from datetime import date, datetime, time, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path

try:
    import yaml
    from markdown_it import MarkdownIt
except ImportError:  # pragma: no cover
    sys.exit("Fehlende Abhängigkeit: pip install markdown-it-py pyyaml")

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fakten_seite  # noqa: E402
ROOT = HERE.parent
POSTS = HERE / "posts"
SOURCES = ROOT / "80_Knowledge" / "Sources"
GLOSSAR = HERE / "glossar.yaml"

CSS = """
:root{--bg:#f4f5f2;--fg:#12161a;--muted:#59616a;--line:#d8dcd6;--accent:#2540d9;--surface:#e9ecf1;--code:#eaece8;--shadow:0 0 0 1px rgba(18,22,26,.06),0 1px 2px rgba(18,22,26,.05),0 6px 16px -6px rgba(18,22,26,.10);--ja:#1b6e46;--nein:#b3261e;--offen:#8a5a00;color-scheme:light}
:root[data-theme=dark]{--bg:#0f1317;--fg:#e6e9ec;--muted:#9aa3ab;--line:#2a3138;--accent:#8fa2ff;--surface:#182029;--code:#182029;--shadow:0 0 0 1px rgba(255,255,255,.07),0 1px 2px rgba(0,0,0,.4),0 6px 16px -6px rgba(0,0,0,.5);--ja:#5fc48f;--nein:#f2867f;--offen:#e0b45a;color-scheme:dark}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0f1317;--fg:#e6e9ec;--muted:#9aa3ab;--line:#2a3138;--accent:#8fa2ff;--surface:#182029;--code:#182029;--shadow:0 0 0 1px rgba(255,255,255,.07),0 1px 2px rgba(0,0,0,.4),0 6px 16px -6px rgba(0,0,0,.5);--ja:#5fc48f;--nein:#f2867f;--offen:#e0b45a;color-scheme:dark}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:1.0625rem/1.65 system-ui,-apple-system,"Segoe UI Variable Text","Segoe UI",Roboto,sans-serif;padding:0 1rem;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;text-wrap:pretty}
a{color:var(--accent);text-underline-offset:.18em;text-decoration-thickness:1px;transition-property:color,text-decoration-color;transition-duration:.15s}a:hover{text-decoration-thickness:2px}
a:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:4px}
.wrap{max-width:46rem;margin:0 auto;padding-block:1.25rem 4rem}
header.site{display:flex;flex-wrap:wrap;gap:.25rem 1.5rem;align-items:baseline;justify-content:space-between;padding-bottom:1rem;margin-bottom:2.5rem;box-shadow:0 1px 0 var(--line)}
header.site .name{font:700 1.3rem/1 Charter,"Iowan Old Style","Sitka Heading",Georgia,serif;color:var(--fg);text-decoration:none;letter-spacing:-.02em;padding-block:.4rem}
header.site nav{display:flex;gap:0 .3rem;flex-wrap:wrap;font-size:.9rem;margin-inline:-.55rem}
header.site nav a{color:var(--muted);text-decoration:none;padding:.5rem .55rem;border-radius:6px}header.site nav a:hover{color:var(--fg)}
h1,h2,h3{font-family:Charter,"Iowan Old Style","Sitka Heading",Georgia,serif;line-height:1.15;letter-spacing:-.02em;text-wrap:balance}
h1{font-size:clamp(2rem,5.5vw,2.9rem);font-weight:700;margin:.5rem 0 .8rem;letter-spacing:-.03em}h2{font-size:1.55rem;font-weight:700;margin:2.6rem 0 .7rem}h3{font-size:1.2rem;font-weight:700;margin:1.8rem 0 .4rem}
p,li{max-width:68ch}
.meta{font:.85rem/1.4 system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--muted);display:flex;flex-wrap:wrap;gap:.3rem 1rem;align-items:center;font-variant-numeric:tabular-nums}
.chip{display:inline-flex;align-items:center;gap:.45rem;color:var(--fg);font-weight:600;text-decoration:none}.chip:hover{color:var(--accent)}
.chip::before{content:"";width:.6rem;height:.6rem;border-radius:2px;background:var(--kc,var(--muted))}
.k-modelle{--kc:#2540d9}.k-arbeitsweisen{--kc:#0f8a5f}.k-tools{--kc:#7c3fc9}.k-duell{--kc:#d4570f}.k-check{--kc:#c48a00}.k-digest{--kc:#0e8aa8}.k-kurz{--kc:#7a838b}.k-redaktion{--kc:#7a838b}
:root[data-theme=dark] .chip::before{filter:brightness(1.35)}@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .chip::before{filter:brightness(1.35)}}
.lead{font-size:1.2rem;line-height:1.5;color:var(--muted);margin:.4rem 0 1.6rem}
.list{list-style:none;padding:0;margin:0}.list li{padding:1.5rem 0;box-shadow:0 1px 0 var(--line);max-width:none}
.list h2{font-size:1.5rem;margin:.45rem 0 .4rem}.list h2 a{color:var(--fg);text-decoration:none;background:linear-gradient(currentColor,currentColor) 0 100%/0 2px no-repeat;transition:background-size .2s cubic-bezier(.2,0,0,1)}.list h2 a:hover{background-size:100% 2px}
.list p{margin:.2rem 0 0;color:var(--muted)}
table{border-collapse:collapse;width:100%;font:.93rem/1.45 system-ui,-apple-system,"Segoe UI",sans-serif;margin:1.4rem 0;display:block;overflow-x:auto;font-variant-numeric:tabular-nums}
th,td{border:0;border-bottom:1px solid var(--line);padding:.6rem .8rem .6rem 0;text-align:left;vertical-align:top}th{font-weight:600;color:var(--muted);font-size:.85rem;border-bottom:2px solid var(--fg)}td.num,th.num{text-align:right;padding-right:.9rem;white-space:nowrap}td:first-child{font-weight:600}
code{background:var(--code);padding:.1em .35em;border-radius:5px;font:.88em ui-monospace,SFMono-Regular,Consolas,monospace}
pre{background:var(--code);padding:.9rem 1rem;border-radius:10px;overflow-x:auto}pre code{background:none;padding:0}
blockquote{margin:1.4rem 0;padding:.1rem 1.1rem;border-left:3px solid var(--accent);color:var(--muted)}
.tldr{background:var(--surface);border-radius:14px;box-shadow:var(--shadow);padding:.3rem 1.4rem .4rem;margin:1.6rem 0 2rem}
.tldr h2{font:700 1.05rem/1.3 system-ui,-apple-system,"Segoe UI",sans-serif;letter-spacing:0;margin:1rem 0 .3rem}.tldr ul{padding-left:1.15rem;margin:.4rem 0 .9rem}.tldr li{margin:.4rem 0}
.urteil{border-left:3px solid var(--offen);padding:.1rem 0 .1rem 1rem}.urteil>strong:first-child{color:var(--offen)}
.urteil-ja{border-color:var(--ja)}.urteil-ja>strong:first-child{color:var(--ja)}.urteil-nein{border-color:var(--nein)}.urteil-nein>strong:first-child{color:var(--nein)}
.quellen{margin-top:3rem;padding-top:1.2rem;box-shadow:0 -1px 0 var(--line);font:.9rem/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--muted)}.quellen h2{font-size:1.1rem;margin:0 0 .6rem;color:var(--fg)}
.quellen ol{padding-left:1.2rem;margin:.3rem 0}.quellen li{margin:.3rem 0}.hinweis{color:var(--muted);font-size:.85rem;margin-top:.8rem}
footer.site{margin-top:3.5rem;padding-top:1.2rem;box-shadow:0 -1px 0 var(--line);font:.85rem/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--muted)}
details.toc{font:.92rem/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;margin:1.2rem 0;color:var(--muted)}details.toc summary{cursor:pointer;padding-block:.4rem}details.toc ol{margin:.4rem 0;padding-left:1.3rem}details.toc a{color:var(--muted)}details.toc a:hover{color:var(--accent)}
sup.q{font:.7rem system-ui,sans-serif;margin-left:.1em}sup.q a{text-decoration:none}
.weiter{margin-top:3rem;padding-top:1.2rem;box-shadow:0 -1px 0 var(--line);font:.97rem/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}.weiter h2{font-size:1.1rem;margin:0 0 .6rem}.weiter ul{list-style:none;padding:0;margin:0}.weiter li{margin:.5rem 0}
.abo{margin-top:2.2rem;background:var(--surface);border-radius:12px;box-shadow:var(--shadow);padding:.9rem 1.2rem;font:.9rem/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}
a.gl{color:inherit;text-decoration:underline dotted var(--muted);text-underline-offset:.2em}a.gl:hover{color:var(--accent);text-decoration-style:solid}
.gl-index{display:flex;flex-wrap:wrap;gap:.5rem;margin:1rem 0 1.8rem}
.gl-index .chip{background:var(--surface);border-radius:999px;padding:.5rem .9rem;font-size:.88rem;font-weight:500;box-shadow:var(--shadow);transition-property:scale,color;transition-duration:.15s}.gl-index .chip::before{display:none}.gl-index .chip:active{scale:.96}
dl.impressum dt{font:700 .95rem system-ui,sans-serif;margin-top:1.2rem}dl.impressum dd{margin:.2rem 0 0}
dl.glossar dt{font:700 1.2rem Charter,"Iowan Old Style","Sitka Heading",Georgia,serif;margin-top:1.8rem;scroll-margin-top:1rem}dl.glossar dd{margin:.25rem 0 0}dl.glossar dd p{margin:.3rem 0}
dl.glossar .siehe{font:.88rem system-ui,sans-serif;color:var(--muted)}
.draft{background:#fff3cd;color:#664d03;padding:.5rem .9rem;border-radius:8px;font:.85rem system-ui,sans-serif;margin-bottom:1rem;box-shadow:0 0 0 1px #ffe69c}
.wrap.wide{max-width:64rem}
.fakten-filter{width:100%;max-width:26rem;font:inherit;font-size:.95rem;padding:.6rem .9rem;border:0;border-radius:10px;background:var(--surface);color:var(--fg);box-shadow:var(--shadow);margin:0 0 1rem}.fakten-filter:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.lesehinweise{color:var(--muted);font-size:.95rem;padding-left:1.1rem;margin:0 0 1.2rem}.lesehinweise li{margin:.25rem 0;max-width:80ch}
table.fakten{display:table;font-size:.88rem;table-layout:auto}table.fakten td{padding-right:1rem}table.fakten td.datum{white-space:nowrap;color:var(--muted);font-weight:400}table.fakten td.gegenstand{font-weight:600;min-width:9rem}table.fakten td.hinweis{color:var(--muted);font-size:.84rem;min-width:10rem}table.fakten td.quelle{font-size:.84rem;white-space:nowrap}
table.fakten thead th{position:sticky;top:0;background:var(--bg)}
@media (max-width:48rem){table.fakten,table.fakten tbody,table.fakten tr,table.fakten td{display:block}table.fakten thead{display:none}table.fakten tr{padding:.9rem 0;box-shadow:0 1px 0 var(--line)}table.fakten td{border:0;padding:.1rem 0;min-width:0!important;white-space:normal!important}table.fakten td.datum,table.fakten td.quelle{display:inline-block;margin-right:.8rem}table.fakten td.hinweis:not(:empty)::before{content:"Hinweis: "}}
@media (max-width:40rem){header.site nav{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;white-space:nowrap;width:calc(100% + 1.1rem)}header.site nav::-webkit-scrollbar{display:none}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition-duration:0s!important}}
"""


def load_config() -> dict:
    return yaml.safe_load((HERE / "site.yaml").read_text(encoding="utf-8"))


def parse_post(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        raise ValueError(f"{path.name}: Frontmatter fehlt")
    fm = yaml.safe_load(m.group(1)) or {}
    d = fm.get("datum")
    if isinstance(d, str):
        d = date.fromisoformat(d)
    fm["datum"] = d
    fm["body"] = m.group(2).strip()
    fm["slug"] = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
    fm["datei"] = path.name
    return fm


Q_RE = re.compile(r"\{q:(\d+)\}")
POST_LINK_RE = re.compile(r"\]\(post:([a-z0-9-]+)\)")
# Wörter aus dem internen Wissenssystem, die Leser nicht kennen
INTERN_RE = re.compile(r"\b(Source-Notiz\w*|Notiz\w*|Patterns?|Konfidenz\w*|Wiki\w*|Fakten-Register|Wissensbasis)\b")


def slugify(text: str) -> str:
    t = re.sub(r"<[^>]+>", "", text).lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-") or "abschnitt"


def prose_only(body: str) -> str:
    """Fließtext ohne Codeblöcke, Inline-Code und Link-Ziele (für Stilprüfungen)."""
    t = re.sub(r"```.*?```", "", body, flags=re.S)
    t = re.sub(r"`[^`]*`", "", t)
    return re.sub(r"\]\([^)]*\)", "]", t)


@functools.lru_cache(maxsize=None)
def _note_entry(q: str) -> dict:
    note = SOURCES / f"{q}.md"
    if not note.exists():
        raise ValueError(f"Source-Notiz nicht gefunden: {q}")
    t = note.read_text(encoding="utf-8")
    fm = re.match(r"---\n(.*?)\n---\n(.*)", t, re.S)
    meta = yaml.safe_load(fm.group(1)) if fm else {}
    h1 = re.search(r"^# (.+)$", fm.group(2) if fm else t, re.M)
    url = str(meta.get("url") or "")
    return {
        "titel": h1.group(1).strip() if h1 else q,
        "autor": str(meta.get("autor") or ""),
        "datum": str(meta.get("datum") or ""),
        "url": url if url.startswith("http") else "",
    }


def source_entries(post: dict) -> list[dict]:
    """Quellenangaben aus Source-Notizen des Wissenssystems (Titel, Autor, URL)."""
    out = []
    for q in post.get("quellen") or []:
        if isinstance(q, dict):
            if not q.get("titel"):
                raise ValueError(f"{post['datei']}: Quelle ohne 'titel': {q}")
            out.append(q)
            continue
        try:
            out.append(_note_entry(str(q)))
        except ValueError as e:
            raise ValueError(f"{post['datei']}: {e}") from None
    return out


# ---------------------------------------------------------------- Glossar

GL_SUFFIX = r"(?:s|n|en|es)?"
GL_SKIP_TAGS = {"a", "code", "pre", "sup", "h1", "h2", "h3", "h4", "h5", "h6", "th", "script", "style"}


def load_glossar() -> dict:
    """glossar.yaml laden; jeder Eintrag bekommt Anker und alle Schreibweisen."""
    if not GLOSSAR.exists():
        return {"begriffe": [], "beobachten": []}
    g = yaml.safe_load(GLOSSAR.read_text(encoding="utf-8")) or {}
    eintraege = g.get("begriffe") or []
    for e in eintraege:
        e["slug"] = slugify(str(e.get("begriff", "")))
        e["formen"] = [str(e.get("begriff", "")), *map(str, e.get("aliase") or [])]
        e["kurz"] = re.split(r"(?<=[.!?])\s", str(e.get("text", "")).strip())[0]
    eintraege.sort(key=lambda e: str(e.get("begriff", "")).lower())
    g["begriffe"] = eintraege
    return g


def glossar_formen(g: dict) -> dict[str, dict]:
    return {f: e for e in g["begriffe"] for f in e["formen"] if f}


def glossar_regex(formen: dict[str, dict]):
    if not formen:
        return None
    alt = "|".join(re.escape(f) for f in sorted(formen, key=len, reverse=True))
    return re.compile(rf"(?<![\w-])({alt}){GL_SUFFIX}(?!\w)")


def link_terms(out: str, rx, formen: dict[str, dict]) -> tuple[str, set[str]]:
    """Erste Nennung jedes Glossarbegriffs im Fließtext verlinken.

    Überschriften, Links, Code, Fußnotenmarken und Tabellenköpfe bleiben unberührt.
    """
    if rx is None:
        return out, set()
    gesehen: set[str] = set()

    def repl(m: re.Match) -> str:
        e = formen[m.group(1)]
        if e["slug"] in gesehen:
            return m.group(0)
        gesehen.add(e["slug"])
        return f'<a class="gl" href="/glossar/#{e["slug"]}" title="{esc(e["kurz"])}">{m.group(0)}</a>'

    teile = re.split(r"(<[^>]+>)", out)
    tiefe = 0
    for i, t in enumerate(teile):
        if t.startswith("<"):
            m = re.match(r"<(/?)([a-z0-9]+)", t)
            if m and m.group(2) in GL_SKIP_TAGS:
                tiefe = max(0, tiefe + (-1 if m.group(1) else 1))
        elif not tiefe:
            teile[i] = rx.sub(repl, t)
    return "".join(teile), gesehen


def check_glossar(g: dict, posts: list[dict]) -> list[str]:
    fehler = []
    formen: dict[str, dict] = {}
    namen = {str(e.get("begriff", "")) for e in g["begriffe"]}
    for e in g["begriffe"]:
        n = e.get("begriff")
        if not n or not e.get("text"):
            fehler.append(f"glossar.yaml: Eintrag ohne begriff oder text: {n or e}")
            continue
        for f in e["formen"]:
            if f in formen and formen[f] is not e:
                fehler.append(f"glossar.yaml: Schreibweise „{f}“ doppelt ({formen[f]['begriff']} und {n})")
            formen[f] = e
        prosa = prose_only(str(e["text"]))
        for m in sorted({m.group(0) for m in INTERN_RE.finditer(prosa)}):
            fehler.append(f"glossar.yaml: {n}: interner Begriff im Text: „{m}“")
        if "[[" in e["text"]:
            fehler.append(f"glossar.yaml: {n}: Wiki-Links nicht erlaubt")
        for s in e.get("siehe") or []:
            if s not in namen:
                fehler.append(f"glossar.yaml: {n}: „siehe“ verweist auf unbekannten Begriff „{s}“")
    for t in g.get("beobachten") or []:
        if t in formen:
            continue
        rx = re.compile(rf"(?<![\w-]){re.escape(t)}{GL_SUFFIX}(?!\w)")
        for p in posts:
            if rx.search(prose_only(p["body"])):
                fehler.append(f"{p['datei']}: Fachbegriff „{t}“ steht im Text, aber nicht im Glossar")
    return fehler


def glossar_html(cfg: dict, g: dict, verwendet: dict[str, int]) -> str:
    eintraege = g["begriffe"]
    chips = "".join(f'<a class="chip" href="#{e["slug"]}">{esc(e["begriff"])}</a>' for e in eintraege)
    items = []
    for e in eintraege:
        siehe = ""
        if e.get("siehe"):
            by_name = {x["begriff"]: x["slug"] for x in eintraege}
            links = ", ".join(f'<a href="#{by_name[s]}">{esc(s)}</a>' for s in e["siehe"] if s in by_name)
            siehe = f'<p class="siehe">Siehe auch: {links}</p>'
        items.append(f'<dt id="{e["slug"]}">{esc(e["begriff"])}</dt><dd><p>{esc(e["text"])}</p>{siehe}</dd>')
    hinweis = esc(g.get("hinweis", ""))
    if g.get("hinweis_url"):
        hinweis += f' <a href="{esc(g["hinweis_url"])}" rel="noopener">AI Coding Dictionary</a>'
    return (f'<h1>{esc(g.get("titel", "Glossar"))}</h1><p class="lead">{esc(g.get("einleitung", ""))}</p>'
            f'<div class="gl-index">{chips}</div><dl class="glossar">{"".join(items)}</dl>'
            f'<p class="hinweis">{hinweis}</p>')


def glossar_ld(cfg: dict, g: dict) -> str:
    base = cfg["base_url"].rstrip("/")
    terms = [{"@type": "DefinedTerm", "name": e["begriff"], "description": e["text"],
              "url": f'{base}/glossar/#{e["slug"]}'} for e in g["begriffe"]]
    doc = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": g.get("titel", "Glossar"),
           "inLanguage": "de", "hasDefinedTerm": terms}
    return f'<script type="application/ld+json">{_j(doc)}</script>'


def check_post(post: dict, cfg: dict, slugs: set[str] | None = None) -> list[str]:
    fehler = []
    for f in ("titel", "datum", "kategorie", "zusammenfassung", "status"):
        if not post.get(f):
            fehler.append(f"{post['datei']}: Feld '{f}' fehlt")
    if post.get("kategorie") and post["kategorie"] not in cfg["kategorien"]:
        fehler.append(f"{post['datei']}: unbekannte Kategorie '{post['kategorie']}'")
    if post.get("status") not in ("entwurf", "freigegeben"):
        fehler.append(f"{post['datei']}: status muss entwurf oder freigegeben sein")
    if post.get("status") == "freigegeben" and not isinstance(post.get("geprueft_am"), date):
        fehler.append(f"{post['datei']}: freigegeben ohne 'geprueft_am' (Freigabe mit --freigeben setzen)")
    akt = post.get("aktualisiert")
    if akt is not None and not isinstance(akt, date):
        fehler.append(f"{post['datei']}: 'aktualisiert' ist kein Datum im Format JJJJ-MM-TT: {akt}")
    elif isinstance(akt, date) and isinstance(post.get("datum"), date) and akt < post["datum"]:
        fehler.append(f"{post['datei']}: 'aktualisiert' ({akt.isoformat()}) liegt vor 'datum' ({post['datum'].isoformat()})")
    if not post.get("quellen") and post.get("kategorie") not in cfg.get("ohne_quellen", []):
        fehler.append(f"{post['datei']}: keine Quellen angegeben (Quellenangabe ist Pflicht)")
    if "[[" in post["body"]:
        fehler.append(f"{post['datei']}: Wiki-Links im Text (Doppelklammern) nicht erlaubt")
    n_q = len(post.get("quellen") or [])
    for m in Q_RE.finditer(post["body"]):
        if not 1 <= int(m.group(1)) <= n_q:
            fehler.append(f"{post['datei']}: Quellenverweis {{q:{m.group(1)}}} ohne passende Quelle (1 bis {n_q})")
    if slugs is not None:
        for m in POST_LINK_RE.finditer(post["body"]):
            if m.group(1) not in slugs:
                fehler.append(f"{post['datei']}: Verweis auf unbekannten Beitrag post:{m.group(1)}")
    prosa = prose_only(post["body"])
    for m in sorted({m.group(0) for m in INTERN_RE.finditer(prosa)}):
        fehler.append(f"{post['datei']}: interner Begriff im Text: „{m}“ (Leser kennen das Wissenssystem nicht)")
    for m in re.finditer(r"[a-zäöüß]{2}[.!?][A-ZÄÖÜ][a-zäöüß]", prosa):
        fehler.append(f"{post['datei']}: fehlendes Leerzeichen nach Satzende: „{m.group(0)}“")
    for m in re.finditer(r"\b\d{4}-\d{2}-\d{2}\b", prosa):
        fehler.append(f"{post['datei']}: ISO-Datum im Fließtext: {m.group(0)} (schreibe 22.09.2026)")
    if re.search(r"\$\d+\.\d", post["body"]):
        fehler.append(f"{post['datei']}: Dollar-Betrag mit Dezimalpunkt (deutsch: $0,068, nicht $0.068)")
    if post.get("kategorie") != "kurz" and "## Kurz gesagt" not in post["body"]:
        fehler.append(f"{post['datei']}: Abschnitt „## Kurz gesagt“ fehlt")
    try:
        source_entries(post)
    except ValueError as e:
        fehler.append(str(e))
    zitiert = {int(m.group(1)) for m in Q_RE.finditer(post["body"])}
    for i in range(1, n_q + 1):
        if i not in zitiert:
            fehler.append(f"{post['datei']}: Quelle {i} wird nie zitiert (setze {{q:{i}}} an die belegte Aussage)")
    return fehler


BEKANNTE_FELDER = {"titel", "datum", "kategorie", "zusammenfassung", "status", "quellen", "aktualisiert",
                   "geprueft_am", "pruefen_bis", "freigabe", "body", "slug", "datei"}
META_RE = re.compile(r"\b(?:un)?belegt\w*|Belegstärke|Primärquelle\w*|Quellenlage|Selbstbericht\w*", re.I)
ZAHL_RE = re.compile(r"\d[\d.,]*\s?(?:Prozent|%|Mio\.?|Tokens?|US-Dollar|Punkte\w*)|\$\d")


def ist_sichtbar(p: dict, heute: date) -> bool:
    return p["status"] == "freigegeben" and p["datum"] <= heute


def warn_post(post: dict, heute: date | None = None) -> list[str]:
    """Weiche Hinweise: Absätze mit Zahlen, aber ohne Quellenverweis."""
    out = []
    for k in post:
        if k not in BEKANNTE_FELDER:
            out.append(f"{post['datei']}: unbekanntes Frontmatter-Feld '{k}' (Tippfehler?)")
    bis = post.get("pruefen_bis")
    if isinstance(bis, date) and bis < (heute or date.today()):
        out.append(f"{post['datei']}: pruefen_bis {bis.strftime('%d.%m.%Y')} ist überschritten, Zahlen und Preise erneut prüfen")
    box = re.search(r"## Kurz gesagt\n(.*?)(?=\n## |\Z)", post["body"], re.S)
    if box:
        n = len(re.findall(r"^[-*] ", box.group(1), re.M))
        if not 2 <= n <= 4:
            out.append(f"{post['datei']}: „Kurz gesagt“ hat {n} Stichpunkte (vorgesehen: 2 bis 4)")
    meta = META_RE.findall(prose_only(post["body"]))
    if meta:
        out.append(f"{post['datei']}: {len(meta)}x Beleg-Meta im Text ({', '.join(sorted({m.lower() for m in meta}))}): "
                   "Blogstil verlangt Aussage statt Belegdiskussion, Quellen stehen am Ende")
    body = re.sub(r"```.*?```", "", post["body"], flags=re.S)
    body = re.sub(r"## Kurz gesagt\n.*?(?=\n## |\Z)", "", body, flags=re.S)  # Zusammenfassung belegt der Text
    for block in re.split(r"\n\s*\n", body):
        b = block.strip()
        if not b or b.startswith("#") or Q_RE.search(b):
            continue
        if ZAHL_RE.search(prose_only(b)):
            out.append(f"{post['datei']}: Zahl ohne Quellenverweis in „{b[:50].replace(chr(10), ' ')}…“")
    return out


def check_freigabe(posts: list[dict], heute: date) -> list[str]:
    """Regeln über mehrere Beiträge: Slug eindeutig, freigegebene verlinken nur Sichtbares."""
    fehler = []
    von: dict[str, list[str]] = {}
    for p in posts:
        von.setdefault(p["slug"], []).append(p["datei"])
    for slug, dateien in von.items():
        if len(dateien) > 1:
            fehler.append(f"Slug „{slug}“ doppelt: {', '.join(dateien)}")
    by_slug = {p["slug"]: p for p in posts}
    for p in posts:
        if p["status"] != "freigegeben":
            continue
        for m in POST_LINK_RE.finditer(p["body"]):
            z = by_slug.get(m.group(1))
            if z is not None and (z["status"] != "freigegeben" or z["datum"] > p["datum"]):
                fehler.append(f"{p['datei']}: verlinkt post:{m.group(1)}, der nicht freigegeben oder später datiert ist (toter Link)")
    return fehler


PLATZHALTER_RE = re.compile(r"\[hier ergänzen[^\]]*\]|\bTODO\b|\bXXX\b|Lorem ipsum", re.I)


def platzhalter(cfg: dict, live: list[dict]) -> list[str]:
    """Platzhalter in Konfiguration und veröffentlichten Beiträgen, die nicht live gehen dürfen."""
    fehler = []
    if cfg and not (cfg.get("impressum") or {}).get("medieninhaber"):
        fehler.append("site.yaml: Impressum (Medieninhaber) fehlt, Offenlegung nach § 25 Mediengesetz")
    for feld in ("titel", "beschreibung", "autor", "fusszeile", "ueber", "impressum", "datenschutz"):
        for m in PLATZHALTER_RE.finditer(str(cfg.get(feld, ""))):
            fehler.append(f"site.yaml: Platzhalter in '{feld}': {m.group(0)}")
    if str(cfg.get("autor", "")).strip().lower() == "sp23" or "sp23 ·" in str(cfg.get("titel", "")):
        fehler.append("site.yaml: Blogtitel oder Autor sind noch die Platzhalter „sp23“")
    for p in live:
        for m in PLATZHALTER_RE.finditer(p["body"]):
            fehler.append(f"{p['datei']}: Platzhalter im Text: {m.group(0)}")
    return fehler


def render_body(md: MarkdownIt, p: dict, base: str = "", zeige_q: bool = True) -> str:
    """Markdown -> HTML. `post:slug` wird zum Beitragslink, `{q:n}` zum Quellenverweis.

    Mit `base` (Feed) werden Links absolut und Quellenverweise zu Klartext.
    """
    body = POST_LINK_RE.sub(lambda m: f"]({base}/p/{m.group(1)}/)", p["body"])
    out = md.render(body)
    if not zeige_q:
        return re.sub(r" ?\{q:\d+\}", "", out)
    if base:
        return Q_RE.sub(lambda m: f"[{m.group(1)}]", out)
    return Q_RE.sub(lambda m: f'<sup class="q"><a href="#q{m.group(1)}" title="Quelle {m.group(1)}">[{m.group(1)}]</a></sup>', out)


def decorate(out: str, wc: int) -> str:
    """Kurz-gesagt-Box, Überschriften-Anker und Inhaltsverzeichnis für lange Beiträge."""
    out = re.sub(r"<h2>Kurz gesagt</h2>\s*(<ul>.*?</ul>)",
                 lambda m: f'<div class="tldr"><h2>Kurz gesagt</h2>{m.group(1)}</div>', out, count=1, flags=re.S)
    head, sep, rest = out.partition("</div>") if out.startswith('<div class="tldr">') else ("", "", out)
    heads: list[tuple[str, str]] = []

    def anchor(m: re.Match) -> str:
        sid = slugify(m.group(1))
        heads.append((sid, m.group(1)))
        return f'<h2 id="{sid}">{m.group(1)}</h2>'

    rest = re.sub(r"<h2>(.*?)</h2>", anchor, rest)
    toc = ""
    if wc >= 600 and len(heads) >= 4:
        lis = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in heads)
        toc = f'<details class="toc"><summary>Inhalt</summary><ol>{lis}</ol></details>'
    rest = zahlenzellen(rest)
    rest = re.sub(r"<p>(<strong>(Stimmt nicht|Stimmt|Nicht prüfbar)[.,:]?[^<]*</strong>)",
                  lambda m: '<p class="urteil urteil-' + {"Stimmt": "ja", "Stimmt nicht": "nein"}.get(m.group(2), "offen") + '">' + m.group(1), rest)
    return head + sep + toc + rest


NUM_CELL_RE = re.compile(r"^[~≈]?[+\-−]?[$€]?\s?\d[\d.,]*(\s?(%|Mio\.?|Mrd\.?|Min\.?))?(\s*/\s*[$€]?\d[\d.,]*)*$")


def zahlenzellen(html_text: str) -> str:
    """Zellen, die nur eine Zahl enthalten, rechtsbündig setzen (Klasse num)."""
    def cell(m: re.Match) -> str:
        inner = re.sub(r"<[^>]+>", "", m.group(3)).strip()
        return f'<{m.group(1)} class="num"{m.group(2)}>{m.group(3)}</{m.group(1)}>' if NUM_CELL_RE.match(inner) else m.group(0)
    return re.sub(r"<(td|th)((?: [^>]*)?)>(.*?)</\1>", cell, html_text, flags=re.S)


def word_count(body: str) -> int:
    return len(re.findall(r"\w+", body))


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def page(cfg: dict, title: str, body: str, *, desc: str, path: str, og_type: str = "website",
         extra_head: str = "", draft: bool = False, wide: bool = False) -> str:
    base = cfg["base_url"].rstrip("/")
    canon = f"{base}{path}"
    full_title = f"{title} · {cfg['titel']}" if title != cfg["titel"] else cfg["titel"]
    aktiv = cfg.get("_aktiv")  # Kategorien mit sichtbaren Beiträgen; ohne Angabe alle
    kats = sorted(((k, v) for k, v in cfg["kategorien"].items() if k != "redaktion" and (aktiv is None or k in aktiv)),
                  key=lambda kv: kv[0] == "kurz")  # Kurzmeldungen zuletzt
    seite = cfg.get("modelle_preise")
    nav = (f'<a href="/modelle-und-preise/">{esc(seite.get("titel", "Modelle und Preise"))}</a>' if seite else "") + \
        "".join(f'<a href="/k/{k}/">{esc(v)}</a>' for k, v in kats) + \
        '<a href="/glossar/">Glossar</a><a href="/ueber/">Über</a><a href="/feed.xml">RSS</a>'
    rechtliches = (' · <a href="/impressum/">Impressum</a>' if cfg.get("impressum") else "") +         (' · <a href="/datenschutz/">Datenschutz</a>' if cfg.get("datenschutz") else "")
    banner = '<div class="draft">Entwurf, nicht veröffentlicht</div>' if draft else ""
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{esc(canon)}">
<link rel="alternate" type="application/rss+xml" title="{esc(cfg['titel'])}" href="{base}/feed.xml">
<meta property="og:type" content="{og_type}"><meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{esc(canon)}">
<meta property="og:site_name" content="{esc(cfg['titel'])}"><meta property="og:locale" content="de_DE">
<meta name="twitter:card" content="summary">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232540d9'/%3E%3Ctext x='16' y='22' font-family='sans-serif' font-size='16' font-weight='700' text-anchor='middle' fill='white'%3Esp%3C/text%3E%3C/svg%3E">
{extra_head}
<style>{CSS}</style>
</head>
<body>
<div class="wrap{" wide" if wide else ""}">
<header class="site"><a class="name" href="/">{esc(cfg['titel'])}</a><nav>{nav}</nav></header>
<main>{banner}{body}</main>
<footer class="site">{esc(cfg['fusszeile'])} · <a href="/feed.xml">RSS-Feed</a>{rechtliches}</footer>
</div>
</body>
</html>
"""


def meta_line(cfg: dict, p: dict, wc: int) -> str:
    kat = cfg["kategorien"][p["kategorie"]]
    minuten = max(1, round(wc / 220))
    a = p.get("aktualisiert")
    aktual = f'<span>aktualisiert {a.strftime("%d.%m.%Y")}</span>' if isinstance(a, date) else ""
    return (f'<div class="meta"><a class="chip k-{p["kategorie"]}" href="/k/{p["kategorie"]}/">{esc(kat)}</a>'
            f'<time datetime="{p["datum"].isoformat()}">{p["datum"].strftime("%d.%m.%Y")}</time>'
            f'{aktual}<span>{minuten} Min. Lesezeit</span></div>')


def de_datum(d: str) -> str:
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", d.strip())
    return f"{m.group(3)}.{m.group(2)}.{m.group(1)}" if m else d


def quellen_html(cfg: dict, p: dict) -> str:
    if not p.get("quellen"):
        return ""
    items = []
    for i, q in enumerate(source_entries(p), 1):
        label = esc(q["titel"])
        if q.get("url"):
            label = f'<a href="{esc(q["url"])}" rel="noopener">{label}</a>'
        zusatz = " · ".join(x for x in (esc(q.get("autor", "")), esc(de_datum(q.get("datum", "")))) if x)
        items.append(f'<li id="q{i}">{label}{(" (" + zusatz + ")") if zusatz else ""}</li>')
    hinweis = cfg.get("quellenhinweis", "")
    return f'<section class="quellen"><h2>Quellen</h2><ol>{"".join(items)}</ol><p class="hinweis">{esc(hinweis)}</p></section>'


def related(p: dict, posts: list[dict], n: int = 3) -> list[dict]:
    """Verwandte Beiträge: nur mit mindestens einer gemeinsamen Quelle; die Kategorie sortiert nach."""
    mine = set(map(str, p.get("quellen") or []))
    scored = []
    for o in posts:
        if o["slug"] == p["slug"]:
            continue
        gemeinsam = len(mine & set(map(str, o.get("quellen") or [])))
        score = 2 * gemeinsam + (1 if o["kategorie"] == p["kategorie"] else 0)
        if gemeinsam:  # gleiche Kategorie allein ist kein Grund für einen Vorschlag
            scored.append((score, o["datum"], o["slug"], o))
    scored.sort(key=lambda t: t[:3], reverse=True)
    return [t[3] for t in scored[:n]]


def weiter_html(p: dict, posts: list[dict]) -> str:
    rel = related(p, posts)
    if not rel:
        return ""
    lis = "".join(f'<li><a href="/p/{o["slug"]}/">{esc(o["titel"])}</a></li>' for o in rel)
    return f'<section class="weiter"><h2>Weiterlesen</h2><ul>{lis}</ul></section>'


def abo_html(cfg: dict) -> str:
    return (f'<p class="abo">{esc(cfg.get("abo_text", ""))} <a href="/feed.xml">RSS-Feed</a>'
            f' · <a href="/ueber/">Über diesen Blog</a></p>')


def post_page(cfg: dict, md: MarkdownIt, p: dict, draft: bool, posts: list[dict],
              gl: tuple | None = None) -> tuple[str, str, int]:
    wc = word_count(p["body"])
    body_html = decorate(render_body(md, p, zeige_q=cfg.get("quellenverweise_im_text", True)), wc)
    if gl:
        body_html, _ = link_terms(body_html, *gl)
    path = f"/p/{p['slug']}/"
    ld = (f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BlogPosting",'
          f'"headline":{_j(p["titel"])},"datePublished":"{p["datum"].isoformat()}",'
          + (f'"dateModified":"{p["aktualisiert"].isoformat()}",' if isinstance(p.get("aktualisiert"), date) else "")
          + f'"description":{_j(p["zusammenfassung"])},"inLanguage":"de",'
          f'"author":{{"@type":"Person","name":{_j(cfg["autor"])}}},'
          f'"mainEntityOfPage":{_j(cfg["base_url"].rstrip("/") + path)}}}</script>')
    # Ohne Kurz-gesagt-Box (Kurzmeldung) übernimmt die Zusammenfassung die Rolle des Einstiegs
    lead = "" if 'class="tldr"' in body_html else f'<p class="lead">{esc(p["zusammenfassung"])}</p>'
    body = (f'<article><h1>{esc(p["titel"])}</h1>{meta_line(cfg, p, wc)}{lead}{body_html}'
            f'{quellen_html(cfg, p)}</article>{weiter_html(p, posts)}{abo_html(cfg)}')
    return path, page(cfg, p["titel"], body, desc=p["zusammenfassung"], path=path, og_type="article",
                      extra_head=ld, draft=draft and p["status"] != "freigegeben"), wc


def _j(s: str) -> str:
    import json
    return json.dumps(s, ensure_ascii=False)


def list_html(cfg: dict, posts: list[dict]) -> str:
    rows = []
    for p in posts:
        wc = word_count(p["body"])
        rows.append(f'<li>{meta_line(cfg, p, wc)}<h2><a href="/p/{p["slug"]}/">{esc(p["titel"])}</a></h2>'
                    f'<p>{esc(p["zusammenfassung"])}</p></li>')
    return f'<ul class="list">{"".join(rows)}</ul>'


def rfc822(d: date) -> str:
    return format_datetime(datetime.combine(d, time(8, 0), tzinfo=timezone.utc))


def feed_xml(cfg: dict, md: MarkdownIt, posts: list[dict], selfpath: str, title: str) -> str:
    base = cfg["base_url"].rstrip("/")
    items = []
    for p in posts[: cfg.get("feed_max", 30)]:
        url = f"{base}/p/{p['slug']}/"
        body_html = render_body(md, p, base, cfg.get("quellenverweise_im_text", True)) + quellen_html(cfg, p)
        items.append(
            f"<item><title>{esc(p['titel'])}</title><link>{url}</link><guid isPermaLink=\"true\">{url}</guid>"
            f"<pubDate>{rfc822(p['datum'])}</pubDate><category>{esc(cfg['kategorien'][p['kategorie']])}</category>"
            f"<description>{esc(p['zusammenfassung'])}</description>"
            f"<content:encoded><![CDATA[{body_html.replace(']]>', ']]&gt;')}]]></content:encoded></item>")
    latest = posts[0]["datum"] if posts else date.today()
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/">'
            f'<channel><title>{esc(title)}</title><link>{base}/</link><description>{esc(cfg["beschreibung"])}</description>'
            f'<language>de-de</language><lastBuildDate>{rfc822(latest)}</lastBuildDate>'
            f'<atom:link href="{base}{selfpath}" rel="self" type="application/rss+xml"/>'
            + (f'<atom:link href="{esc(cfg["websub_hub"])}" rel="hub"/>' if cfg.get("websub_hub") else "")
            + f'{"".join(items)}</channel></rss>\n')


def _hub_post(hub: str, daten: bytes) -> int:
    req = urllib.request.Request(hub, data=daten, method="POST",
                                 headers={"Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.status


def websub_ping(cfg: dict, site: Path, senden=_hub_post) -> tuple[bool, list[str]]:
    """Meldet dem WebSub-Hub jeden gebauten Feed als aktualisiert, damit Reader wie Feedly sofort abrufen."""
    hub = cfg.get("websub_hub")
    if not hub:
        return False, ["site.yaml: websub_hub fehlt, kein Ping gesendet"]
    base = cfg["base_url"].rstrip("/")
    feeds = sorted(site.glob("feed.xml")) + sorted(site.glob("feed/*.xml"))
    if not feeds:
        return False, [f"Keine Feeds in {site} gefunden, zuerst bauen und deployen"]
    ok, meldungen = True, []
    for f in feeds:
        url = f"{base}/{f.relative_to(site).as_posix()}"
        try:
            status, grund = senden(hub, urllib.parse.urlencode({"hub.mode": "publish", "hub.url": url}).encode()), ""
        except Exception as e:  # Netzwerkfehler einzeln melden, die übrigen Feeds trotzdem pingen
            status, grund = None, str(e)
        if status is not None and 200 <= status < 300:
            meldungen.append(f"Ping {url}: {status}")
        else:
            ok = False
            meldungen.append(f"Ping {url} fehlgeschlagen: {grund or status}")
    return ok, meldungen


def impressum_html(imp: dict) -> str:
    zeilen = [("Medieninhaber und Herausgeber", "medieninhaber"), ("Wohnort", "wohnort"),
              ("Unternehmensgegenstand", "gegenstand"), ("Grundlegende Richtung", "richtung"),
              ("Beteiligungen", "beteiligungen"), ("Kontakt", "kontakt")]
    items = "".join(f"<dt>{t}</dt><dd>{esc(imp[k])}</dd>" for t, k in zeilen if imp.get(k))
    return (f'<h1>Impressum</h1><p class="lead">Offenlegung nach § 25 Mediengesetz</p>'
            f'<dl class="impressum">{items}</dl>')


def write(out: Path, rel: str, text: str) -> None:
    target = out / rel.lstrip("/")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8", newline="\n")


AUTO_VERZOEGERUNG_TAGE = 0  # automatisch freigegebene Beiträge erscheinen sofort (Beschluss Philipp, 07.10.2026)


def freigeben(post: dict, posts: list[dict], heute: date, automatisch: bool = False) -> tuple[bool, str]:
    """Beitrag freigeben: erneut prüfen, status und geprueft_am im Frontmatter setzen.

    Automatisch: Datum frühestens heute plus AUTO_VERZOEGERUNG_TAGE, Vermerk `freigabe: automatisch`,
    und der Beitrag darf keine Hinweise haben.
    """
    if post["status"] == "freigegeben":
        return False, f"{post['datei']} ist schon freigegeben"
    datum = post["datum"]
    if automatisch:
        datum = max(datum, heute + timedelta(days=AUTO_VERZOEGERUNG_TAGE))
    neu = {**post, "status": "freigegeben", "geprueft_am": heute, "datum": datum}
    probe = [neu if q is post else q for q in posts]
    fehler = check_freigabe(probe, heute) + platzhalter({}, [post])
    if automatisch:
        fehler += warn_post(post, heute)
    if fehler:
        return False, "Freigabe abgelehnt:\n - " + "\n - ".join(fehler)
    path = POSTS / post["datei"]
    text = path.read_text(encoding="utf-8", newline="")
    text = re.sub(r"^(geprueft_am|freigabe):.*?\r?\n", "", text, flags=re.M)
    zusatz = lambda nl: f"geprueft_am: {heute.isoformat()}{nl}" + (f"freigabe: automatisch{nl}" if automatisch else "")
    text, n = re.subn(r"^status:.*?(\r?\n)", lambda m: f"status: freigegeben{m.group(1)}{zusatz(m.group(1))}",
                      text, count=1, flags=re.M)
    if not n:
        return False, f"{post['datei']}: status-Zeile nicht gefunden"
    if datum != post["datum"]:
        text = re.sub(r"^datum:.*?(\r?\n)", lambda m: f"datum: {datum.isoformat()}{m.group(1)}", text, count=1, flags=re.M)
    path.write_text(text, encoding="utf-8", newline="")
    post.update(status="freigegeben", geprueft_am=heute, datum=datum)
    wann = "sofort sichtbar" if datum <= heute else f"erscheint ab {datum.strftime('%d.%m.%Y')}"
    return True, f"{post['datei']} freigegeben (geprueft_am {heute.strftime('%d.%m.%Y')}), {wann}"


def auto_freigeben(posts: list[dict], cfg: dict, heute: date) -> list[str]:
    """Alle Entwürfe freigeben, die jede automatische Prüfung bestehen. Rückgabe: Meldungen."""
    meldungen: list[str] = []
    offen = []
    slugs = {p["slug"] for p in posts}
    for p in posts:
        if p["status"] != "entwurf":
            continue
        fehler = check_post({**p, "status": "freigegeben", "geprueft_am": heute}, cfg, slugs)
        if fehler:
            meldungen.append(f"übersprungen {p['datei']}: " + "; ".join(fehler))
        else:
            offen.append(p)
    while True:  # Reihenfolge egal: ein Digest folgt, sobald die verlinkten Beiträge frei sind
        fortschritt = False
        for p in list(offen):
            ok, msg = freigeben(p, posts, heute, automatisch=True)
            if ok:
                meldungen.append(msg)
                offen.remove(p)
                fortschritt = True
        if not fortschritt:
            break
    for p in offen:
        ok, msg = freigeben(p, posts, heute, automatisch=True)
        meldungen.append(f"übersprungen {p['datei']}: {msg.replace(chr(10), ' ')}")
    return meldungen


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--drafts", action="store_true", help="Entwürfe einbeziehen (Ausgabe nach blog/_preview)")
    ap.add_argument("--check", action="store_true", help="nur prüfen")
    ap.add_argument("--freigeben", metavar="SLUG", help="Beitrag prüfen und freigeben (setzt status und geprueft_am)")
    ap.add_argument("--auto-freigeben", action="store_true",
                    help="alle Entwürfe freigeben, die jede Prüfung ohne Hinweise bestehen (erscheinen sofort)")
    ap.add_argument("--ping", action="store_true",
                    help="nach dem Deployment den WebSub-Hub über alle Feeds in blog/_site informieren")
    args = ap.parse_args()

    cfg = load_config()
    if args.ping:
        ok, meldungen = websub_ping(cfg, HERE / "_site")
        print("\n".join(meldungen), file=sys.stdout if ok else sys.stderr)
        return 0 if ok else 1
    posts = []
    fehler = []
    for f in sorted(POSTS.glob("*.md")):
        try:
            p = parse_post(f)
        except ValueError as e:
            fehler.append(str(e))
            continue
        posts.append(p)
    slugs = {p["slug"] for p in posts}
    for p in posts:
        fehler += check_post(p, cfg, slugs)
    glossar = load_glossar()
    fehler += check_glossar(glossar, posts)
    heute = date.today()
    fehler += check_freigabe(posts, heute)
    fakten = None
    if cfg.get("modelle_preise"):
        pfad = ROOT / cfg["modelle_preise"]["pfad"]
        if pfad.exists():
            fakten = fakten_seite.parse_register(pfad.read_text(encoding="utf-8"))
            fehler += fakten_seite.pruefen(fakten, lambda q: (SOURCES / f"{q}.md").exists())
        else:
            fehler.append(f"site.yaml: Fakten-Register nicht gefunden: {cfg['modelle_preise']['pfad']}")
    if args.auto_freigeben:  # einzelne fehlerhafte Entwürfe blockieren nicht die anderen
        fehler = [f for f in fehler if f.startswith(("glossar.yaml", "Slug"))]
    if fehler:
        print("FEHLER:\n - " + "\n - ".join(fehler), file=sys.stderr)
        return 1

    if args.auto_freigeben:
        for m in auto_freigeben(posts, cfg, heute):
            print(m)
        return 0

    if args.freigeben:
        ziel = next((p for p in posts if p["slug"] == args.freigeben), None)
        if ziel is None:
            print(f"Beitrag nicht gefunden: {args.freigeben}", file=sys.stderr)
            return 1
        ok, meldung = freigeben(ziel, posts, heute)
        print(meldung, file=sys.stdout if ok else sys.stderr)
        return 0 if ok else 1

    sichtbar = [p for p in posts if (args.drafts or ist_sichtbar(p, heute))]
    sichtbar.sort(key=lambda p: (p["datum"], p["slug"]), reverse=True)
    n_draft = sum(1 for p in sichtbar if p["status"] != "freigegeben")
    print(f"{len(posts)} Beiträge, {len(sichtbar)} im Build ({n_draft} Entwürfe)")
    warnungen = [w for p in posts for w in warn_post(p, heute)] + (fakten_seite.hinweise(fakten, heute) if fakten else [])
    if warnungen:
        print("HINWEISE:\n - " + "\n - ".join(warnungen), file=sys.stderr)
    offen = platzhalter(cfg, [p for p in posts if ist_sichtbar(p, heute)])
    if args.check:
        if offen:
            print("Vor dem Livegang offen:\n - " + "\n - ".join(offen), file=sys.stderr)
        print("Prüfung bestanden.")
        return 0
    if offen and not args.drafts:
        print("FEHLER (Platzhalter im öffentlichen Build):\n - " + "\n - ".join(offen), file=sys.stderr)
        return 1
    if not sichtbar and not args.drafts:
        print("FEHLER: Kein freigegebener Beitrag. Der öffentliche Build würde eine leere Seite erzeugen.", file=sys.stderr)
        return 1
    cfg["_aktiv"] ={p["kategorie"] for p in sichtbar}

    out = HERE / ("_preview" if args.drafts else "_site")
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    md = MarkdownIt("commonmark", {"html": False}).enable(["table", "strikethrough"])

    formen = glossar_formen(glossar)
    gl = (glossar_regex(formen), formen)
    verwendet: dict[str, int] = {}
    for p in sichtbar:
        path, doc, _ = post_page(cfg, md, p, args.drafts, sichtbar, gl)
        write(out, f"{path}index.html", doc)
        for slug in link_terms(md.render(p["body"]), *gl)[1]:
            verwendet[slug] = verwendet.get(slug, 0) + 1
    intro = f'<h1>{esc(cfg["titel"])}</h1><p class="lead">{esc(cfg["beschreibung"])}</p>'
    if fakten:
        n = sum(len(a["zeilen"]) for a in fakten["abschnitte"])
        intro += (f'<p class="abo"><a href="/modelle-und-preise/">{esc(cfg["modelle_preise"].get("titel", "Modelle und Preise"))}</a>: '
                  f'{n} datierte Angaben zu Preisen, Benchmarks und Markt, Stand {fakten_seite.de_datum(fakten["stand"].isoformat())}.</p>')
    write(out, "index.html", page(cfg, cfg["titel"], intro + list_html(cfg, sichtbar) + abo_html(cfg), desc=cfg["beschreibung"], path="/"))
    for k, name in cfg["kategorien"].items():
        sel = [p for p in sichtbar if p["kategorie"] == k]
        if not sel:
            continue
        write(out, f"k/{k}/index.html", page(cfg, name, f"<h1>{esc(name)}</h1>" + list_html(cfg, sel),
                                             desc=f"{name}: {cfg['beschreibung']}", path=f"/k/{k}/"))
        write(out, f"feed/{k}.xml", feed_xml(cfg, md, sel, f"/feed/{k}.xml", f"{cfg['titel']}: {name}"))
    ueber = md.render(cfg.get("ueber", "")) + '<p><a href="/feed.xml">RSS-Feed abonnieren</a></p>'
    write(out, "ueber/index.html", page(cfg, "Über diesen Blog", "<h1>Über diesen Blog</h1>" + ueber,
                                        desc=cfg["beschreibung"], path="/ueber/"))
    if cfg.get("impressum"):
        write(out, "impressum/index.html", page(cfg, "Impressum", impressum_html(cfg["impressum"]),
                                                desc="Impressum und Offenlegung", path="/impressum/"))
    if cfg.get("datenschutz"):
        write(out, "datenschutz/index.html", page(cfg, "Datenschutz", "<h1>Datenschutz</h1>" + md.render(cfg["datenschutz"]),
                                                  desc="Datenschutzerklärung", path="/datenschutz/"))
    if glossar["begriffe"]:
        write(out, "glossar/index.html", page(cfg, glossar.get("titel", "Glossar"), glossar_html(cfg, glossar, verwendet),
                                              desc=glossar.get("einleitung", cfg["beschreibung"]), path="/glossar/",
                                              extra_head=glossar_ld(cfg, glossar)))
        ungenutzt = [e["begriff"] for e in glossar["begriffe"] if e["slug"] not in verwendet]
        print(f"Glossar: {len(glossar['begriffe'])} Begriffe, {len(verwendet)} in Beiträgen verlinkt"
              + (f"; ohne Vorkommen: {', '.join(ungenutzt)}" if ungenutzt else ""))
    if fakten:
        write(out, "modelle-und-preise/index.html",
              page(cfg, cfg["modelle_preise"].get("titel", "Modelle und Preise"),
                   fakten_seite.render(cfg["modelle_preise"], fakten, _note_entry),
                   desc=cfg["modelle_preise"].get("beschreibung", cfg["beschreibung"]), path="/modelle-und-preise/", wide=True))
    write(out, "feed.xml", feed_xml(cfg, md, sichtbar, "/feed.xml", cfg["titel"]))
    base = cfg["base_url"].rstrip("/")
    urls = [f"{base}/", f"{base}/ueber/", f"{base}/impressum/", f"{base}/datenschutz/"] + ([f"{base}/glossar/"] if glossar["begriffe"] else []) + ([f"{base}/modelle-und-preise/"] if fakten else []) + [f"{base}/p/{p['slug']}/" for p in sichtbar]
    write(out, "sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
          + "".join(f"<url><loc>{u}</loc></url>" for u in urls) + "</urlset>\n")
    write(out, "robots.txt", f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n")
    write(out, "404.html", page(cfg, "Nicht gefunden", '<h1>Seite nicht gefunden</h1><p><a href="/">Zur Startseite</a></p>',
                                desc="Seite nicht gefunden", path="/404.html"))
    print(f"Geschrieben nach {out.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
