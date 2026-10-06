#!/usr/bin/env python3
"""RSS-/Atom-Feeds registrieren und thematisch passende Artikel vorschlagen.

Artikel werden separat über `python ai.py ingest <url>` erfasst.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from fnmatch import fnmatchcase
from html import unescape
from pathlib import Path
import re
import sys
from urllib.error import URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

import yaml

from ingest_source import normalisiere_url
import themen


ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "00_Inbox" / "Feeds" / "feeds.yaml"
ATOM = "{http://www.w3.org/2005/Atom}"
MAX_BYTES = 4 * 1024 * 1024
MIN_AUSWAHL = 6
GENERISCH = {"ai", "ki", "agent", "agents", "skill", "skills", "code", "coding", "claude",
             "claude code", "token", "tokens", "tool", "tools", "workflow", "test", "tests",
             "plan", "review", "prompt", "session", "python", "typescript"}


@dataclass
class Eintrag:
    titel: str
    url: str
    datum: datetime | None
    beschreibung: str = ""


@dataclass
class Empfehlung:
    eintrag: Eintrag
    score: int
    cluster: list[str]
    gruende: list[str]
    ausschluss: str = ""


def text_ohne_html(text: str) -> str:
    text = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", text, flags=re.I | re.S)
    return " ".join(unescape(re.sub(r"<[^>]+>", " ", text)).split())


def themen_regeln() -> tuple[dict, dict]:
    """Bestehende Taxonomie und gepflegte Keywords, ohne neue Themenzuordnung."""
    taxo = themen.lade_taxonomie()
    begriffe = {cid: {str(t).lower(): w for w, feld in ((1, "weit"), (3, "kern"))
                     for t in c.get(feld, [])} for cid, c in taxo.items()}
    zuordnung = themen.lade_zuordnung()
    for art in ("quellen", "muster"):
        for notiz in zuordnung.get(art, {}).values():
            cid = notiz.get("haupt")
            if cid not in begriffe:
                continue
            for term in notiz.get("keywords", []) + notiz.get("synonyme", []):
                term = str(term).lower()
                begriffe[cid][term] = max(2, begriffe[cid].get(term, 0))
    regeln = {cid: [(t, w, re.compile(r"(?<!\w)" + re.escape(t) + r"(?!\w)"))
                    for t, w in sorted(terme.items()) if len(t) >= 3 and t not in GENERISCH]
              for cid, terme in begriffe.items()}
    return taxo, regeln


def bewerte_eintrag(eintrag: Eintrag, feed: dict, regeln: dict, thema: str | None = None) -> Empfehlung:
    pfad = urlsplit(eintrag.url).path.rstrip("/") or "/"
    ausschluss = ""
    for muster in feed.get("auswahl", {}).get("ausschliessen_pfade", []):
        if fnmatchcase(pfad, muster):
            ausschluss = f"Auswahlregel: {muster}"
            break
    titel = text_ohne_html(eintrag.titel).lower()
    beschreibung = eintrag.beschreibung.lower()
    scores = []
    for cid, terms in regeln.items():
        if thema and cid != thema:
            continue
        extra = feed.get("auswahl", {}).get("themen_keywords", {}).get(cid, [])
        terms = terms + [(t.lower(), 3, re.compile(r"(?<!\w)" + re.escape(t.lower()) + r"(?!\w)")) for t in extra]
        treffer = [(t, w * (2 if rx.search(titel) else 1)) for t, w, rx in terms
                   if rx.search(titel) or rx.search(beschreibung)]
        score = sum(w for _, w in treffer)
        scores.append((cid, score, sorted(treffer, key=lambda t: (-t[1], t[0]))))
    scores.sort(key=lambda s: (-s[1], s[0]))
    best = scores[0] if scores else ("", 0, [])
    praktische_hilfe = bool(re.search(
        r"/[-\w]+|\b(how to|guide|tutorial|workflow|changelog|retrospective|debugging|benchmark|case study)\b", titel))
    bonus = 2 if best[1] >= 4 and praktische_hilfe else 0
    cluster = [cid for cid, score, _ in scores[:3] if score >= 4 and score >= best[1] * 0.55]
    gruende = ["Treffer: " + ", ".join(t for t, _ in best[2][:3])] if best[2] else ["Kein konkreter Themen-Treffer"]
    if bonus:
        gruende.append("Anleitung, Skill oder Erfahrungsbericht im Titel")
    return Empfehlung(eintrag, best[1] + bonus, cluster, gruende, ausschluss)


def vorauswahl(eintraege: list[Eintrag], feed: dict, regeln: dict, limit: int,
               thema: str | None = None, alle: bool = False) -> tuple[list[Empfehlung], int, int]:
    bewertet = [bewerte_eintrag(i, feed, regeln, thema) for i in eintraege]
    kandidaten = [e for e in bewertet if not e.ausschluss and e.score >= MIN_AUSWAHL]
    ausgeschlossen = sum(bool(e.ausschluss) for e in bewertet)
    if alle:
        return bewertet[:limit], len(kandidaten), ausgeschlossen
    kandidaten.sort(key=lambda e: e.eintrag.url)
    kandidaten.sort(key=lambda e: (e.eintrag.datum or datetime.min.replace(tzinfo=timezone.utc), e.score), reverse=True)
    if thema:
        return kandidaten[:limit], len(kandidaten), ausgeschlossen
    # Zunächst höchstens zwei Beiträge je Hauptthema, damit ein Thema die Liste nicht füllt.
    auswahl, vertreten = [], {}
    for e in kandidaten:
        haupt = e.cluster[0] if e.cluster else ""
        if vertreten.get(haupt, 0) < 2:
            auswahl.append(e)
            vertreten[haupt] = vertreten.get(haupt, 0) + 1
        if len(auswahl) == limit:
            break
    for e in kandidaten:
        if len(auswahl) == limit:
            break
        if e not in auswahl:
            auswahl.append(e)
    return auswahl[:limit], len(kandidaten), ausgeschlossen


def http_url(url: str) -> bool:
    teile = urlsplit(url)
    return teile.scheme in {"http", "https"} and bool(teile.netloc)


def datum_lesen(wert: str) -> datetime | None:
    if not wert:
        return None
    try:
        datum = datetime.fromisoformat(wert.replace("Z", "+00:00"))
    except ValueError:
        try:
            datum = parsedate_to_datetime(wert)
        except (ValueError, TypeError, OverflowError):
            return None
    return datum.replace(tzinfo=timezone.utc) if datum.tzinfo is None else datum


def atom_link(element: ET.Element) -> str:
    for link in element.findall(f"{ATOM}link"):
        if link.get("rel", "alternate") == "alternate" and link.get("href"):
            return link.get("href", "")
    return ""


def inhalt_text(element: ET.Element, pfad: str) -> str:
    inhalt = element.find(pfad)
    return " ".join(inhalt.itertext()) if inhalt is not None else ""


def parse_feed(daten: bytes, url: str) -> tuple[str, str, str, list[Eintrag]]:
    root = ET.fromstring(daten)
    if root.tag == "rss" and (channel := root.find("channel")) is not None:
        titel = channel.findtext("title", "").strip()
        website = urljoin(url, channel.findtext("link", "").strip())
        format_name = "rss"
        roh = [(i.findtext("title", ""), i.findtext("link", ""),
                i.findtext("pubDate", ""), inhalt_text(i, "description")) for i in channel.findall("item")]
    elif root.tag == f"{ATOM}feed":
        titel = root.findtext(f"{ATOM}title", "").strip()
        website = urljoin(url, atom_link(root))
        format_name = "atom"
        roh = [(i.findtext(f"{ATOM}title", ""), atom_link(i),
                i.findtext(f"{ATOM}published", "") or i.findtext(f"{ATOM}updated", ""),
                inhalt_text(i, f"{ATOM}summary") or inhalt_text(i, f"{ATOM}content"))
               for i in root.findall(f"{ATOM}entry")]
    else:
        raise ValueError("Kein unterstützter Feed (erwartet RSS 2.0 oder Atom).")
    eintraege = []
    gesehen = set()
    for name, link, datum, beschreibung in roh:
        if not link.strip():
            continue
        ziel = urljoin(url, link.strip())
        key = normalisiere_url(ziel)
        if not http_url(ziel) or key in gesehen:
            continue
        gesehen.add(key)
        eintraege.append(Eintrag(name.strip() or ziel, ziel, datum_lesen(datum.strip()),
                                text_ohne_html(beschreibung)[:2000]))
    eintraege.sort(key=lambda i: i.datum or datetime.min.replace(tzinfo=timezone.utc), reverse=True)
    return titel or url, website, format_name, eintraege


def abrufen(url: str) -> tuple[str, str, str, list[Eintrag]]:
    if not http_url(url):
        raise ValueError("Eine HTTP- oder HTTPS-Feed-URL ist erforderlich.")
    request = Request(url, headers={"User-Agent": "AI-Company-OS/1.0 (RSS reader)"})
    with urlopen(request, timeout=30) as antwort:
        daten = antwort.read(MAX_BYTES + 1)
        if len(daten) > MAX_BYTES:
            raise ValueError("Feed überschreitet die Größenbegrenzung von 4 MiB.")
        return parse_feed(daten, antwort.geturl())


def lade_register() -> list[dict]:
    if not REGISTER.exists():
        return []
    daten = yaml.safe_load(REGISTER.read_text(encoding="utf-8"))
    if not isinstance(daten, dict) or not isinstance(daten.get("feeds"), list):
        raise ValueError("Ungültiges Feed-Register: erwartet wird eine Liste unter feeds.")
    for feed in daten["feeds"]:
        if not isinstance(feed, dict) or not isinstance(feed.get("url"), str) or not http_url(feed["url"]):
            raise ValueError("Ungültiger Eintrag im Feed-Register.")
        aliases = feed.get("url_aliases", {})
        if not isinstance(aliases, dict) or any(
            not isinstance(alias, str) or not isinstance(original, str)
            or not http_url(alias) or not http_url(original) for alias, original in aliases.items()
        ):
            raise ValueError("Ungültige URL-Zuordnung im Feed-Register.")
        auswahl = feed.get("auswahl", {})
        if not isinstance(auswahl, dict) or not isinstance(auswahl.get("ausschliessen_pfade", []), list) or any(
            not isinstance(p, str) for p in auswahl.get("ausschliessen_pfade", [])
        ):
            raise ValueError("Ungültige Auswahlregeln im Feed-Register.")
        keywords = auswahl.get("themen_keywords", {})
        if not isinstance(keywords, dict) or any(
            not isinstance(cid, str) or not isinstance(terms, list) or any(not isinstance(t, str) or not t.strip() for t in terms)
            for cid, terms in keywords.items()
        ):
            raise ValueError("Ungültige Themen-Keywords im Feed-Register.")
    return daten["feeds"]


def bekannte_urls() -> set[str]:
    urls = set()
    for ordner in (ROOT / "00_Inbox" / "Quellen", ROOT / "80_Knowledge" / "Sources"):
        for datei in ordner.rglob("*.md"):
            text = datei.read_text(encoding="utf-8")
            if not text.startswith("---\n"):
                continue
            frontmatter = text.split("---", 2)[1]
            treffer = re.search(r"^url:.*$", frontmatter, re.M)
            if treffer:
                try:
                    wert = yaml.safe_load(treffer.group()).get("url")
                except yaml.YAMLError:
                    continue
                if isinstance(wert, str) and http_url(wert):
                    urls.add(normalisiere_url(wert))
    return urls


def bekannte_feed_urls(feed: dict, bekannt: set[str]) -> set[str]:
    """Nur geprüfte Feed-Aliase ergänzen, deren Original wirklich archiviert ist."""
    return bekannt | {
        normalisiere_url(alias) for alias, original in feed.get("url_aliases", {}).items()
        if normalisiere_url(original) in bekannt
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="aktion", required=True)
    add = sub.add_parser("add", help="Feed prüfen und registrieren")
    add.add_argument("url")
    add.add_argument("--name", help="Anzeigename im Register")
    sub.add_parser("list", help="Registrierte Feeds anzeigen")
    check = sub.add_parser("check", help="Thematisch passende Artikel vorschlagen")
    check.add_argument("--url", help="Nur diesen registrierten Feed abrufen")
    check.add_argument("--limit", type=int, default=10, help="Einträge pro Feed (Standard: 10)")
    check.add_argument("--thema", help="Nur Beiträge für diese Themencluster-ID")
    check.add_argument("--alle", action="store_true", help="Alle offenen Einträge nach Datum, mit Auswahlbegründung")
    check.add_argument("--ausgabe", type=Path, help="Vorauswahl zusätzlich als Markdown speichern")
    args = parser.parse_args(argv)
    try:
        feeds = lade_register()
        if args.aktion == "add":
            if any(normalisiere_url(f["url"]) == normalisiere_url(args.url) for f in feeds):
                print("Feed ist bereits registriert.")
                return 0
            titel, website, format_name, eintraege = abrufen(args.url)
            feeds.append({"name": args.name or titel, "url": args.url, "website": website,
                          "format": format_name, "hinzugefuegt": date.today().isoformat()})
            REGISTER.parent.mkdir(parents=True, exist_ok=True)
            text = "# Feed-Register; einzelne Artikel werden separat als Quellen archiviert.\n"
            text += yaml.safe_dump({"feeds": feeds}, allow_unicode=True, sort_keys=False)
            temp = REGISTER.with_suffix(".tmp")
            temp.write_bytes(text.encode("utf-8"))
            temp.replace(REGISTER)
            print(f"Feed registriert: {args.name or titel} ({len(eintraege)} Einträge)")
            return 0
        if args.aktion == "list":
            for feed in feeds:
                print(f"{feed.get('name', feed['url'])}\n  {feed['url']}")
            if not feeds:
                print("Noch keine Feeds registriert.")
            return 0
        if args.limit < 1:
            raise ValueError("--limit muss mindestens 1 sein.")
        if args.url:
            feeds = [f for f in feeds if normalisiere_url(f["url"]) == normalisiere_url(args.url)]
            if not feeds:
                raise ValueError("Feed ist nicht registriert. Zuerst feeds add verwenden.")
        bekannt = bekannte_urls()
        taxo, regeln = themen_regeln()
        if args.thema and args.thema not in taxo:
            raise ValueError("Unbekanntes Thema. Gültig: " + ", ".join(taxo))
        for feed in feeds:
            unbekannt = set(feed.get("auswahl", {}).get("themen_keywords", {})) - set(taxo)
            if unbekannt:
                raise ValueError("Unbekannte Themen in den Feed-Regeln: " + ", ".join(sorted(unbekannt)))
        bericht = ["# Feed-Vorauswahl", "", f"Stand: {date.today().isoformat()}", "",
                   "Vorauswahl anhand von Titel, Feed-Beschreibung und Themen-Keywords. "
                   "Vor dem Ingest den Volltext prüfen; die Bewertung ist kein Qualitätsnachweis.", ""]
        fehler = False
        for feed in feeds:
            print(f"\n{feed.get('name', feed['url'])}")
            try:
                _, _, _, eintraege = abrufen(feed["url"])
            except (OSError, ValueError, ET.ParseError) as error:
                print(f"Abruf fehlgeschlagen: {error}", file=sys.stderr)
                bericht.extend([f"## {feed.get('name', feed['url'])}", "", f"Abruf fehlgeschlagen: {error}", ""])
                fehler = True
                continue
            feed_bekannt = bekannte_feed_urls(feed, bekannt)
            offen = [i for i in eintraege if normalisiere_url(i.url) not in feed_bekannt]
            auswahl, passend, ausgeschlossen = vorauswahl(offen, feed, regeln, args.limit, args.thema, args.alle)
            zusammenfassung = (f"{len(eintraege)} Einträge, {len(offen)} noch nicht archiviert, "
                               f"{passend} Themen-Kandidaten, {ausgeschlossen} durch Auswahlregeln zurückgestellt.")
            print(zusammenfassung)
            bericht.extend([f"## {feed.get('name', feed['url'])}", "", zusammenfassung, ""])
            for empfehlung in auswahl:
                eintrag = empfehlung.eintrag
                datum = eintrag.datum.date().isoformat() if eintrag.datum else "Datum unbekannt"
                themen_namen = ", ".join(taxo[cid]["name"] for cid in empfehlung.cluster) or "offen"
                status = "zurückgestellt" if empfehlung.ausschluss else "Kandidat" if empfehlung.score >= MIN_AUSWAHL else "manuell prüfen"
                grund = empfehlung.ausschluss or "; ".join(empfehlung.gruende)
                print(f"  {datum} | {eintrag.titel}\n    {status} · Themen: {themen_namen}\n    {grund}\n    {eintrag.url}")
                titel = text_ohne_html(eintrag.titel).replace("[", "(").replace("]", ")")
                bericht.extend([f"### {titel}", "", f"{datum} · {status} · Themen: {themen_namen}", "",
                                f"[Originalbeitrag](<{eintrag.url}>)", "", grund, ""])
            if not auswahl:
                print("Keine passenden Kandidaten. Mit --alle die übrigen Einträge prüfen.")
                bericht.extend(["Keine passenden Kandidaten; übrige Einträge mit `--alle` prüfen.", ""])
        if not feeds:
            print("Noch keine Feeds registriert.")
        if args.ausgabe:
            args.ausgabe.parent.mkdir(parents=True, exist_ok=True)
            args.ausgabe.write_bytes(("\n".join(bericht).rstrip() + "\n").encode("utf-8"))
            print(f"Vorauswahl gespeichert: {args.ausgabe}")
        return int(fehler)
    except (OSError, ValueError, ET.ParseError, yaml.YAMLError, URLError) as error:
        print(f"Feed-Verwaltung: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
