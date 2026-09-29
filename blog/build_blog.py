#!/usr/bin/env python3
"""Statischer Blog-Generator: Markdown-Beiträge -> HTML, RSS, Sitemap.

Nutzung:
    python blog/build_blog.py                 # nur status: freigegeben nach blog/_site
    python blog/build_blog.py --drafts        # Entwürfe zusätzlich, nach blog/_preview
    python blog/build_blog.py --check         # nur prüfen, nichts schreiben

Beiträge liegen in blog/posts/*.md. Nur Beiträge mit `status: freigegeben` und einem
Datum bis heute erscheinen im öffentlichen Build. Das ist die Freigabe-Schranke:
Ein Entwurf kann nicht versehentlich in Seite oder Feed landen.

Abhängigkeiten: markdown-it-py, PyYAML (pip install markdown-it-py pyyaml).
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
from datetime import date, datetime, time, timezone
from email.utils import format_datetime
from pathlib import Path

try:
    import yaml
    from markdown_it import MarkdownIt
except ImportError:  # pragma: no cover
    sys.exit("Fehlende Abhängigkeit: pip install markdown-it-py pyyaml")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
POSTS = HERE / "posts"
SOURCES = ROOT / "80_Knowledge" / "Sources"
GLOSSAR = HERE / "glossar.yaml"

CSS = """
:root{--bg:#fbfaf7;--fg:#1c1b19;--muted:#6b675f;--line:#e4e0d6;--accent:#b4451f;--chip:#f0ece1;--code:#f3f0e7;color-scheme:light}
:root[data-theme=dark]{--bg:#151412;--fg:#ece8df;--muted:#a09a8d;--line:#2d2a25;--accent:#ee8b5f;--chip:#221f1b;--code:#1e1c19;color-scheme:dark}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#151412;--fg:#ece8df;--muted:#a09a8d;--line:#2d2a25;--accent:#ee8b5f;--chip:#221f1b;--code:#1e1c19;color-scheme:dark}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:1.0625rem/1.65 ui-serif,"Iowan Old Style","Palatino Linotype",Georgia,serif;padding:0 1rem}
a{color:var(--accent);text-underline-offset:.18em}a:hover{text-decoration-thickness:2px}
.wrap{max-width:44rem;margin:0 auto;padding-block:1.25rem 4rem}
header.site{display:flex;flex-wrap:wrap;gap:.5rem 1.25rem;align-items:baseline;justify-content:space-between;border-bottom:1px solid var(--line);padding-bottom:.9rem;margin-bottom:2rem;font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif}
header.site .name{font-weight:700;font-size:1.15rem;color:var(--fg);text-decoration:none;letter-spacing:-.01em}
header.site nav{display:flex;gap:1rem;flex-wrap:wrap;font-size:.9rem}header.site nav a{color:var(--muted);text-decoration:none}header.site nav a:hover{color:var(--accent)}
h1,h2,h3{font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.2;letter-spacing:-.02em}
h1{font-size:clamp(1.75rem,4.5vw,2.4rem);margin:.4rem 0 .6rem}h2{font-size:1.4rem;margin:2.2rem 0 .6rem}h3{font-size:1.12rem;margin:1.6rem 0 .4rem}
.meta{font:.85rem/1.4 ui-sans-serif,system-ui,sans-serif;color:var(--muted);display:flex;flex-wrap:wrap;gap:.35rem .8rem;align-items:center}
.chip{display:inline-block;background:var(--chip);border:1px solid var(--line);border-radius:999px;padding:.08rem .6rem;font-size:.78rem;color:var(--muted);text-decoration:none}
.lead{font-size:1.2rem;color:var(--muted);margin:.2rem 0 1.4rem}
.list{list-style:none;padding:0;margin:0}.list li{padding:1.15rem 0;border-bottom:1px solid var(--line)}
.list h2{font-size:1.28rem;margin:.3rem 0 .3rem}.list h2 a{color:var(--fg);text-decoration:none}.list h2 a:hover{color:var(--accent)}
.list p{margin:.2rem 0 0;color:var(--muted)}
table{border-collapse:collapse;width:100%;font:.92rem/1.45 ui-sans-serif,system-ui,sans-serif;margin:1.2rem 0;display:block;overflow-x:auto}
th,td{border:1px solid var(--line);padding:.45rem .65rem;text-align:left;vertical-align:top}th{background:var(--chip)}
code{background:var(--code);padding:.08em .3em;border-radius:4px;font:.9em ui-monospace,SFMono-Regular,Consolas,monospace}
pre{background:var(--code);padding:.9rem 1rem;border-radius:6px;overflow-x:auto}pre code{background:none;padding:0}
blockquote{margin:1.2rem 0;padding:.1rem 1rem;border-left:3px solid var(--accent);color:var(--muted)}
.tldr{background:var(--chip);border:1px solid var(--line);border-radius:8px;padding:.2rem 1.1rem;margin:1.2rem 0}
.quellen{margin-top:2.6rem;border-top:1px solid var(--line);padding-top:1rem;font:.9rem/1.5 ui-sans-serif,system-ui,sans-serif}.quellen h2{font-size:1rem;margin:0 0 .5rem}
.quellen ul{padding-left:1.1rem;margin:.3rem 0}.hinweis{color:var(--muted);font-size:.85rem;margin-top:.8rem}
footer.site{margin-top:3.5rem;border-top:1px solid var(--line);padding-top:1rem;font:.85rem/1.5 ui-sans-serif,system-ui,sans-serif;color:var(--muted)}
.tldr h2{font-size:1rem;margin:.9rem 0 .3rem;text-transform:uppercase;letter-spacing:.04em;color:var(--muted)}.tldr ul{padding-left:1.1rem;margin:.3rem 0 .9rem}
details.toc{font:.92rem/1.5 ui-sans-serif,system-ui,sans-serif;margin:1.2rem 0;color:var(--muted)}details.toc summary{cursor:pointer}details.toc ol{margin:.4rem 0;padding-left:1.3rem}details.toc a{color:var(--muted)}
sup.q{font:.7rem ui-sans-serif,system-ui,sans-serif;margin-left:.1em}sup.q a{text-decoration:none}
.weiter{margin-top:2.6rem;border-top:1px solid var(--line);padding-top:1rem;font:.95rem/1.5 ui-sans-serif,system-ui,sans-serif}.weiter h2{font-size:1rem;margin:0 0 .5rem}.weiter ul{list-style:none;padding:0;margin:0}.weiter li{margin:.35rem 0}
.abo{margin-top:2rem;background:var(--chip);border:1px solid var(--line);border-radius:8px;padding:.7rem 1.1rem;font:.9rem/1.5 ui-sans-serif,system-ui,sans-serif}
a.gl{color:inherit;text-decoration:underline dotted var(--muted);text-underline-offset:.2em}a.gl:hover{color:var(--accent);text-decoration-style:solid}
.gl-index{display:flex;flex-wrap:wrap;gap:.4rem;margin:1rem 0 1.6rem}
dl.glossar dt{font:700 1.05rem ui-sans-serif,system-ui,sans-serif;margin-top:1.6rem;scroll-margin-top:1rem}dl.glossar dd{margin:.25rem 0 0}dl.glossar dd p{margin:.3rem 0}
dl.glossar .siehe{font:.88rem ui-sans-serif,system-ui,sans-serif;color:var(--muted)}
.draft{background:#fff3cd;color:#664d03;border:1px solid #ffe69c;padding:.4rem .8rem;border-radius:6px;font:.85rem ui-sans-serif,system-ui,sans-serif;margin-bottom:1rem}
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
INTERN_RE = re.compile(r"\b(Source-Notiz\w*|Notizen?|Patterns?|Konfidenz\w*|Wiki\w*|Fakten-Register|Wissensbasis)\b")


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


def source_entries(post: dict) -> list[dict]:
    """Quellenangaben aus Source-Notizen des Wissenssystems (Titel, Autor, URL)."""
    out = []
    for q in post.get("quellen") or []:
        if isinstance(q, dict):
            out.append(q)
            continue
        note = SOURCES / f"{q}.md"
        if not note.exists():
            raise ValueError(f"{post['datei']}: Source-Notiz nicht gefunden: {q}")
        t = note.read_text(encoding="utf-8")
        fm = re.match(r"---\n(.*?)\n---\n(.*)", t, re.S)
        meta = yaml.safe_load(fm.group(1)) if fm else {}
        h1 = re.search(r"^# (.+)$", fm.group(2) if fm else t, re.M)
        url = str(meta.get("url") or "")
        out.append({
            "titel": h1.group(1).strip() if h1 else q,
            "autor": str(meta.get("autor") or ""),
            "datum": str(meta.get("datum") or ""),
            "url": url if url.startswith("http") else "",
        })
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
    if not post.get("quellen"):
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
    return fehler


def render_body(md: MarkdownIt, p: dict, base: str = "") -> str:
    """Markdown -> HTML. `post:slug` wird zum Beitragslink, `{q:n}` zum Quellenverweis.

    Mit `base` (Feed) werden Links absolut und Quellenverweise zu Klartext.
    """
    body = POST_LINK_RE.sub(lambda m: f"]({base}/p/{m.group(1)}/)", p["body"])
    out = md.render(body)
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
    return head + sep + toc + rest


def word_count(body: str) -> int:
    return len(re.findall(r"\w+", body))


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def page(cfg: dict, title: str, body: str, *, desc: str, path: str, og_type: str = "website",
         extra_head: str = "", draft: bool = False) -> str:
    base = cfg["base_url"].rstrip("/")
    canon = f"{base}{path}"
    full_title = f"{title} · {cfg['titel']}" if title != cfg["titel"] else cfg["titel"]
    nav = "".join(f'<a href="/k/{k}/">{esc(v)}</a>' for k, v in cfg["kategorien"].items() if k != "kurz") + \
        '<a href="/k/kurz/">Kurzmeldungen</a><a href="/glossar/">Glossar</a><a href="/ueber/">Über</a><a href="/feed.xml">RSS</a>'
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
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%23b4451f'/%3E%3Ctext x='16' y='22' font-family='sans-serif' font-size='16' font-weight='700' text-anchor='middle' fill='white'%3Esp%3C/text%3E%3C/svg%3E">
{extra_head}
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header class="site"><a class="name" href="/">{esc(cfg['titel'])}</a><nav>{nav}</nav></header>
<main>{banner}{body}</main>
<footer class="site">{esc(cfg['fusszeile'])} · <a href="/feed.xml">RSS-Feed</a></footer>
</div>
</body>
</html>
"""


def meta_line(cfg: dict, p: dict, wc: int) -> str:
    kat = cfg["kategorien"][p["kategorie"]]
    minuten = max(1, round(wc / 220))
    a = p.get("aktualisiert")
    aktual = f'<span>aktualisiert {a.strftime("%d.%m.%Y")}</span>' if isinstance(a, date) else ""
    return (f'<div class="meta"><a class="chip" href="/k/{p["kategorie"]}/">{esc(kat)}</a>'
            f'<time datetime="{p["datum"].isoformat()}">{p["datum"].strftime("%d.%m.%Y")}</time>'
            f'{aktual}<span>{minuten} Min. Lesezeit</span></div>')


def de_datum(d: str) -> str:
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", d.strip())
    return f"{m.group(3)}.{m.group(2)}.{m.group(1)}" if m else d


def quellen_html(cfg: dict, p: dict) -> str:
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
    body_html = decorate(render_body(md, p), wc)
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
        body_html = render_body(md, p, base) + quellen_html(cfg, p)
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
            f'<atom:link href="{base}{selfpath}" rel="self" type="application/rss+xml"/>{"".join(items)}</channel></rss>\n')


def write(out: Path, rel: str, text: str) -> None:
    target = out / rel.lstrip("/")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--drafts", action="store_true", help="Entwürfe einbeziehen (Ausgabe nach blog/_preview)")
    ap.add_argument("--check", action="store_true", help="nur prüfen")
    args = ap.parse_args()

    cfg = load_config()
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
    if fehler:
        print("FEHLER:\n - " + "\n - ".join(fehler), file=sys.stderr)
        return 1

    heute = date.today()
    sichtbar = [p for p in posts if (args.drafts or (p["status"] == "freigegeben" and p["datum"] <= heute))]
    sichtbar.sort(key=lambda p: (p["datum"], p["slug"]), reverse=True)
    n_draft = sum(1 for p in sichtbar if p["status"] != "freigegeben")
    print(f"{len(posts)} Beiträge, {len(sichtbar)} im Build ({n_draft} Entwürfe)")
    if args.check:
        # Quellen auflösen, damit fehlende Source-Notizen auffallen
        for p in sichtbar:
            source_entries(p)
        print("Prüfung bestanden.")
        return 0

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
    if glossar["begriffe"]:
        write(out, "glossar/index.html", page(cfg, glossar.get("titel", "Glossar"), glossar_html(cfg, glossar, verwendet),
                                              desc=glossar.get("einleitung", cfg["beschreibung"]), path="/glossar/",
                                              extra_head=glossar_ld(cfg, glossar)))
        ungenutzt = [e["begriff"] for e in glossar["begriffe"] if e["slug"] not in verwendet]
        print(f"Glossar: {len(glossar['begriffe'])} Begriffe, {len(verwendet)} in Beiträgen verlinkt"
              + (f"; ohne Vorkommen: {', '.join(ungenutzt)}" if ungenutzt else ""))
    write(out, "feed.xml", feed_xml(cfg, md, sichtbar, "/feed.xml", cfg["titel"]))
    base = cfg["base_url"].rstrip("/")
    urls = [f"{base}/", f"{base}/ueber/"] + ([f"{base}/glossar/"] if glossar["begriffe"] else []) + [f"{base}/p/{p['slug']}/" for p in sichtbar]
    write(out, "sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
          + "".join(f"<url><loc>{u}</loc></url>" for u in urls) + "</urlset>\n")
    write(out, "robots.txt", f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n")
    write(out, "404.html", page(cfg, "Nicht gefunden", '<h1>Seite nicht gefunden</h1><p><a href="/">Zur Startseite</a></p>',
                                desc="Seite nicht gefunden", path="/404.html"))
    print(f"Geschrieben nach {out.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
