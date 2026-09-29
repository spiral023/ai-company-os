"""Lebende Wissensseite „Modelle und Preise“ aus dem Fakten-Register.

Liest 80_Knowledge/Fakten/Modelle-und-Preise.md (Tabellen mit Datum, Gegenstand, Aussage,
Einschränkung, Quelle) und macht daraus eine Seite mit Stand-Datum, Filter und Quellenliste.
Die Seite ändert sich, sobald das Register sich ändert. Keine Zahl steht in diesem Modul.
"""

from __future__ import annotations

import html
import re
from datetime import date

KOPF = ["datum", "gegenstand", "aussage", "einschraenkung", "quelle"]
QUELLE_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
STAND_RE = re.compile(r"\*\*Stand:\*\*\s*(\d{4}-\d{2}-\d{2})")
ISO_RE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
DOLLAR_RE = re.compile(r"\$(\d+)\.(\d+)")
INTERN_RE = re.compile(r"\b(Source-Notiz\w*|Notiz\w*|Patterns?|Konfidenz(?!intervall)\w*|Wiki\w*|Fakten-Register|Wissensbasis)\b")
STAND_FRIST_TAGE = 14


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def de_datum(iso: str) -> str:
    m = ISO_RE.fullmatch(iso.strip())
    return f"{m.group(3)}.{m.group(2)}.{m.group(1)}" if m else iso


def bereinigen(text: str) -> str:
    """Register-Schreibweise für Leser: kein Code-Format, deutsches Datum, Dollar mit Komma."""
    t = text.replace("`", "").strip()
    t = ISO_RE.sub(lambda m: f"{m.group(3)}.{m.group(2)}.{m.group(1)}", t)
    return DOLLAR_RE.sub(lambda m: f"${m.group(1)},{m.group(2)}", t)


def parse_register(text: str) -> dict:
    """Register -> {stand, abschnitte: [{titel, id, zeilen: [{datum, gegenstand, ..., quellen}]}]}."""
    m = STAND_RE.search(text)
    stand = date.fromisoformat(m.group(1)) if m else None
    abschnitte = []
    aktuell = None
    for zeile in text.splitlines():
        if zeile.startswith("## "):
            aktuell = {"titel": zeile[3:].strip(), "zeilen": []}
            abschnitte.append(aktuell)
            continue
        if aktuell is None or not zeile.startswith("|"):
            continue
        zellen = [c.strip() for c in zeile.strip().strip("|").split("|")]
        if len(zellen) != len(KOPF) or set("".join(zellen)) <= set("-: "):
            continue
        if zellen[0].lower() == "datum":
            continue
        d = dict(zip(KOPF, zellen))
        d["quellen"] = QUELLE_RE.findall(d.pop("quelle"))
        aktuell["zeilen"].append(d)
    abschnitte = [a for a in abschnitte if a["zeilen"]]
    for a in abschnitte:
        a["id"] = re.sub(r"[^a-z0-9]+", "-", a["titel"].lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")).strip("-")
        a["zeilen"].sort(key=lambda z: z["datum"], reverse=True)  # stabil: gleiche Tage behalten Registerreihenfolge
    return {"stand": stand, "abschnitte": abschnitte}


def pruefen(reg: dict, quelle_vorhanden) -> list[str]:
    """Fehler, die die Seite blockieren. `quelle_vorhanden(slug)` sagt, ob die Quelle existiert."""
    fehler = []
    if reg["stand"] is None:
        fehler.append("Fakten-Register: Zeile „**Stand:** JJJJ-MM-TT“ fehlt")
    if not reg["abschnitte"]:
        fehler.append("Fakten-Register: keine Tabelle gefunden")
    for a in reg["abschnitte"]:
        for z in a["zeilen"]:
            wo = f"Fakten-Register ({a['titel']}, {z['datum']} {z['gegenstand'][:40]})"
            if not ISO_RE.fullmatch(z["datum"]):
                fehler.append(f"{wo}: Datum ungültig")
            if not z["quellen"]:
                fehler.append(f"{wo}: keine Quelle")
            for q in z["quellen"]:
                if not quelle_vorhanden(q):
                    fehler.append(f"{wo}: Quelle nicht gefunden: {q}")
            for feld in ("gegenstand", "aussage", "einschraenkung"):
                for mm in INTERN_RE.finditer(z[feld]):
                    fehler.append(f"{wo}: interner Begriff „{mm.group(0)}“ in {feld}")
    return fehler


def hinweise(reg: dict, heute: date) -> list[str]:
    if reg["stand"] and (heute - reg["stand"]).days > STAND_FRIST_TAGE:
        return [f"Fakten-Register: Stand {de_datum(reg['stand'].isoformat())} ist älter als {STAND_FRIST_TAGE} Tage, Seite „Modelle und Preise“ prüfen"]
    return []


FILTER_JS = """<script>
(function(){var f=document.getElementById('fakten-filter');if(!f)return;f.hidden=false;
var rows=[].slice.call(document.querySelectorAll('table.fakten tbody tr'));
var secs=[].slice.call(document.querySelectorAll('section.fakten-abschnitt'));
f.addEventListener('input',function(){var q=f.value.trim().toLowerCase();
rows.forEach(function(r){r.hidden=q&&r.textContent.toLowerCase().indexOf(q)<0});
secs.forEach(function(s){s.hidden=!s.querySelector('tbody tr:not([hidden])')})})})();
</script>"""


def render(cfg_seite: dict, reg: dict, eintrag) -> str:
    """HTML der Seite. `eintrag(slug)` liefert {titel, autor, datum, url} der Quelle."""
    reihenfolge: list[str] = []  # Quellen in Reihenfolge des ersten Auftretens

    def nr(slug: str) -> int:
        if slug not in reihenfolge:
            reihenfolge.append(slug)
        return reihenfolge.index(slug) + 1

    chips = "".join(f'<a class="chip" href="#{a["id"]}">{esc(a["titel"])}</a>' for a in reg["abschnitte"])
    teile = []
    for a in reg["abschnitte"]:
        zeilen = []
        for z in a["zeilen"]:
            q = " ".join(f'<a href="#q{nr(s)}" title="{esc(eintrag(s)["titel"])}">{esc(eintrag(s).get("autor") or "Quelle")}</a>'
                         for s in dict.fromkeys(z["quellen"]))
            hint = "" if z["einschraenkung"] in ("", "-") else esc(bereinigen(z["einschraenkung"]))
            zeilen.append(
                f'<tr><td class="datum"><time datetime="{esc(z["datum"])}">{esc(de_datum(z["datum"]))}</time></td>'
                f'<td class="gegenstand">{esc(bereinigen(z["gegenstand"]))}</td>'
                f'<td class="aussage">{esc(bereinigen(z["aussage"]))}</td>'
                f'<td class="hinweis">{hint}</td><td class="quelle">{q}</td></tr>')
        teile.append(
            f'<section class="fakten-abschnitt" id="{a["id"]}"><h2>{esc(a["titel"])}</h2>'
            f'<table class="fakten"><thead><tr><th>Datum</th><th>Gegenstand</th><th>Aussage</th><th>Hinweis</th><th>Quelle</th></tr></thead>'
            f'<tbody>{"".join(zeilen)}</tbody></table></section>')
    quellen = []
    for i, s in enumerate(reihenfolge, 1):
        e = eintrag(s)
        label = esc(e["titel"])
        if e.get("url"):
            label = f'<a href="{esc(e["url"])}" rel="noopener">{label}</a>'
        zusatz = " · ".join(x for x in (esc(e.get("autor", "")), esc(de_datum(e.get("datum", "")))) if x)
        quellen.append(f'<li id="q{i}">{label}{f" ({zusatz})" if zusatz else ""}</li>')
    stand = de_datum(reg["stand"].isoformat()) if reg["stand"] else ""
    hinweis = "".join(f"<li>{esc(h)}</li>" for h in cfg_seite.get("hinweise", []))
    return (f'<h1>{esc(cfg_seite.get("titel", "Modelle und Preise"))}</h1>'
            f'<p class="meta"><span>Stand {esc(stand)}</span><span>{sum(len(a["zeilen"]) for a in reg["abschnitte"])} Angaben</span></p>'
            f'<p class="lead">{esc(cfg_seite.get("einleitung", ""))}</p>'
            + (f'<ul class="lesehinweise">{hinweis}</ul>' if hinweis else "")
            + f'<div class="gl-index">{chips}</div>'
            f'<input id="fakten-filter" class="fakten-filter" type="search" placeholder="Filtern, zum Beispiel Opus oder Kosten" '
            f'aria-label="Angaben filtern" hidden>'
            + "".join(teile)
            + f'<section class="quellen"><h2>Quellen</h2><ol>{"".join(quellen)}</ol></section>' + FILTER_JS)
