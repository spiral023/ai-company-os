#!/usr/bin/env python3
"""Quellen erfassen: Artikel-URLs, YouTube-Transkripte und PDFs.

Schreibt typabhängig in dieselbe Ablage wie X- und TikTok-Ingest:

    00_Inbox/Quellen/<Quelltyp>/<slug>.md
    00_Inbox/Quellen/<Quelltyp>/medien/<slug>/

Die Ablage-Konvention ist in 00_Inbox/Quellen/README.md beschrieben und gilt
fuer beide Implementierungen (dieses Script und scripts/lib/inbox-store.mjs).

Nutzung:
    python 70_Scripts/ingest_source.py <url-oder-pfad> [--typ auto|url|youtube|pdf]
                                       [--no-media] [--force] [--titel "..."]
"""

from __future__ import annotations

import argparse
import datetime as dt
import mimetypes
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

# Konsistente Ausgabe in PowerShell, Pipes und Agent-Terminals unter Windows.
for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, "reconfigure"):
        stream.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
INBOX = REPO_ROOT / "00_Inbox" / "Quellen"
MEDIA_DIRNAME = "medien"
QUELLTYP_ORDNER = {
    "youtube": "YouTube",
    "url": "URL",
    "pdf": "PDF",
}
# Verwaltungsdateien im Quellenordner sind keine Quellen. Ohne diese Liste
# würden sie bei Dubletten- und Statusprüfungen mitgezählt.
KEINE_QUELLEN = {"README.md", "VERARBEITUNGSPLAN.md"}
USER_AGENT = "Mozilla/5.0 (compatible; ai-company-os ingest)"
# Bilder unter dieser Groesse sind praktisch immer Icons, Spacer oder Tracking-Pixel.
MIN_IMAGE_BYTES = 15_000


# ---------------------------------------------------------------- Datenmodell


@dataclass
class Medium:
    url: str
    alt: str = ""
    local: str | None = None
    error: str | None = None
    # Bereits im Speicher liegende Bilddaten (PDF-Extraktion). Sie werden erst
    # geschrieben, wenn der endgültige Slug feststeht — sonst bräuchte es ein
    # Provisorium, das bei Abbruch als Müll zurückbliebe.
    daten: bytes | None = None


@dataclass
class Quelle:
    url: str
    typ: str
    titel: str
    text: str
    autor: str = ""
    datum: str = ""
    beschreibung: str = ""
    medien: list[Medium] = field(default_factory=list)
    extra: dict[str, str] = field(default_factory=dict)


# ------------------------------------------------------------------ Hilfsmittel


def heute() -> str:
    return dt.date.today().isoformat()


def iso_datum(wert: str | None) -> str:
    """Datum aus verschiedenen Formaten auf YYYY-MM-DD normalisieren."""
    if not wert:
        return heute()
    treffer = re.search(r"(\d{4})-(\d{2})-(\d{2})", wert)
    if treffer:
        return treffer.group(0)
    # PDF-Metadaten nutzen "D:YYYYMMDDHHmmSS" ohne Trennzeichen.
    treffer = re.match(r"D?:?(\d{4})(\d{2})(\d{2})", wert.strip())
    if treffer:
        jahr, monat, tag = treffer.groups()
        if 1 <= int(monat) <= 12 and 1 <= int(tag) <= 31:
            return f"{jahr}-{monat}-{tag}"
    for muster in ("%d.%m.%Y", "%d/%m/%Y", "%B %d, %Y", "%b %d, %Y"):
        try:
            return dt.datetime.strptime(wert.strip(), muster).date().isoformat()
        except ValueError:
            continue
    return heute()


def slugify(wert: str, maxlen: int = 60) -> str:
    wert = wert.lower()
    ersatz = {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "à": "a", "é": "e", "è": "e"}
    for k, v in ersatz.items():
        wert = wert.replace(k, v)
    wert = re.sub(r"[^a-z0-9]+", "-", wert).strip("-")
    return wert[:maxlen].strip("-") or "quelle"


def domain_slug(url: str) -> str:
    host = urllib.parse.urlparse(url).netloc.lower()
    host = re.sub(r"^www\.", "", host)
    return slugify(host.split(".")[0] if host else "quelle", 24)


def baue_slug(quelle: Quelle) -> str:
    """<datum>-<herkunft>-<titel>. Herkunft ist Kanal, Domain oder 'pdf'."""
    if quelle.typ == "youtube":
        herkunft = slugify(quelle.autor or "youtube", 24)
    elif quelle.typ == "pdf":
        herkunft = "pdf"
    else:
        herkunft = domain_slug(quelle.url)
    return f"{iso_datum(quelle.datum)}-{herkunft}-{slugify(quelle.titel, 48)}"


def quelltyp_ordner(typ: str) -> Path:
    """Zielordner für einen technischen Inbox-Typ bestimmen."""
    return INBOX / QUELLTYP_ORDNER.get(typ.lower(), "Sonstige")


def pdf_dateien_ordner() -> Path:
    """Ablage für heruntergeladene PDF-Originaldateien."""
    return quelltyp_ordner("pdf") / "dateien"


def hole(url: str, timeout: int = 30) -> bytes:
    anfrage = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(anfrage, timeout=timeout) as antwort:
        return antwort.read()


def erkenne_typ(eingabe: str) -> str:
    if re.search(r"(youtube\.com|youtu\.be)", eingabe, re.I):
        return "youtube"
    if eingabe.lower().endswith(".pdf") or Path(eingabe).suffix.lower() == ".pdf":
        return "pdf"
    if re.match(r"^https?://", eingabe, re.I):
        return "url"
    if Path(eingabe).exists():
        return "pdf"
    raise SystemExit(f"[FEHLER] Typ nicht erkennbar: {eingabe}. --typ setzen.")


# ------------------------------------------------------------------- Artikel-URL


def lade_artikel(url: str) -> Quelle:
    from bs4 import BeautifulSoup

    html = hole(url).decode("utf-8", errors="replace")
    suppe = BeautifulSoup(html, "html.parser")

    for tag in suppe(["script", "style", "noscript", "nav", "footer", "aside", "form", "iframe"]):
        tag.decompose()

    def meta(*namen: str) -> str:
        for name in namen:
            for attr in ("property", "name", "itemprop"):
                tag = suppe.find("meta", attrs={attr: name})
                if tag and tag.get("content"):
                    return tag["content"].strip()
        return ""

    # og:title trägt auf manchen Seiten nur den Site-Namen. Ein längeres <h1>
    # im Dokument ist dann der bessere Titel — ein zu generischer Titel führt
    # sonst zu Slug-Kollisionen zwischen verschiedenen Artikeln derselben Seite.
    titel = meta("og:title", "twitter:title") or (suppe.title.get_text(strip=True) if suppe.title else "")
    h1 = suppe.find("h1")
    h1_text = h1.get_text(" ", strip=True) if h1 else ""
    if h1_text and len(h1_text) > len(titel) and len(titel) < 30:
        titel = h1_text
    autor = meta("author", "article:author", "og:site_name")
    datum = meta("article:published_time", "datePublished", "og:updated_time")

    # Hauptinhalt: bevorzugt semantische Container, sonst der Block mit dem
    # meisten Text. Boilerplate ist oben schon entfernt.
    haupt = suppe.find("article") or suppe.find("main") or suppe.find(attrs={"role": "main"})
    if haupt is None:
        kandidaten = suppe.find_all(["div", "section"], recursive=True)
        haupt = max(kandidaten, key=lambda t: len(t.get_text(" ", strip=True)), default=None) or suppe.body or suppe

    absaetze: list[str] = []
    for element in haupt.find_all(["h1", "h2", "h3", "h4", "p", "li", "pre", "blockquote"]):
        text = element.get_text(" ", strip=True)
        if not text or len(text) < 2:
            continue
        name = element.name
        if name.startswith("h") and name[1:].isdigit():
            absaetze.append(f"{'#' * min(int(name[1:]) + 1, 6)} {text}")
        elif name == "li":
            absaetze.append(f"- {text}")
        elif name == "pre":
            absaetze.append(f"```\n{element.get_text()}\n```")
        elif name == "blockquote":
            absaetze.append(f"> {text}")
        else:
            absaetze.append(text)

    medien: list[Medium] = []
    basis = url
    for img in haupt.find_all("img"):
        quelle_attr = img.get("src") or img.get("data-src") or img.get("data-lazy-src") or ""
        if not quelle_attr or quelle_attr.startswith("data:"):
            continue
        medien.append(Medium(url=urllib.parse.urljoin(basis, quelle_attr), alt=(img.get("alt") or "").strip()))

    return Quelle(
        url=url,
        typ="url",
        titel=titel or url,
        text="\n\n".join(absaetze),
        autor=autor,
        datum=iso_datum(datum),
        medien=medien,
    )


# ---------------------------------------------------------------------- YouTube


def youtube_id(url: str) -> str:
    treffer = re.search(r"(?:v=|youtu\.be/|/shorts/|/embed/)([A-Za-z0-9_-]{11})", url)
    if not treffer:
        raise SystemExit(f"[FEHLER] Keine YouTube-Video-ID in {url}")
    return treffer.group(1)


def lade_youtube(url: str) -> Quelle:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        raise SystemExit(
            "[FEHLER] youtube-transcript-api fehlt. Installieren:\n"
            "  python -m pip install youtube-transcript-api"
        )

    vid = youtube_id(url)
    api = YouTubeTranscriptApi()
    try:
        liste = api.list(vid)
        # Deutsche oder englische Originalspur bevorzugen, sonst irgendeine.
        try:
            spur = liste.find_transcript(["de", "en"])
        except Exception:
            spur = next(iter(liste))
        eintraege = spur.fetch()
        sprache = getattr(spur, "language_code", "?")
        generiert = getattr(spur, "is_generated", None)
    except Exception as err:  # noqa: BLE001 — API wirft heterogene Fehler
        raise SystemExit(f"[FEHLER] Kein Transkript verfuegbar für {vid}: {err}")

    segmente: list[str] = []
    for eintrag in eintraege:
        text = (getattr(eintrag, "text", "") or "").replace("\n", " ").strip()
        if not text:
            continue
        segmente.append(re.sub(r"\s+", " ", text))

    titel, autor, datum, beschreibung = youtube_metadaten(url, vid)
    return Quelle(
        url=f"https://www.youtube.com/watch?v={vid}",
        typ="youtube",
        titel=titel,
        text=formatiere_transkript(segmente),
        autor=autor,
        datum=datum,
        beschreibung=beschreibung,
        extra={
            "video_id": vid,
            "transkript_sprache": sprache,
            "transkript_generiert": "ja" if generiert else "nein",
            "transkript_segmente": str(len(segmente)),
        },
    )


def formatiere_transkript(segmente: list[str], min_absatzlaenge: int = 600) -> str:
    """Untertitel-Segmente ohne Zeitstempel zu lesbaren Absätzen verbinden."""
    absaetze: list[str] = []
    aktueller_absatz: list[str] = []
    aktuelle_laenge = 0

    for segment in segmente:
        aktueller_absatz.append(segment)
        aktuelle_laenge += len(segment) + 1
        ist_satzende = re.search(r'[.!?…]["”\)]?$', segment)
        ist_abkuerzung = re.search(
            r"\b(?:z\.\s?B\.|bzw\.|ca\.|d\.\s?h\.|u\.\s?a\.|etc\.)$",
            segment,
            re.I,
        )
        if aktuelle_laenge >= min_absatzlaenge and ist_satzende and not ist_abkuerzung:
            absaetze.append(" ".join(aktueller_absatz))
            aktueller_absatz = []
            aktuelle_laenge = 0

    if aktueller_absatz:
        absaetze.append(" ".join(aktueller_absatz))

    return "\n\n".join(absaetze)


def youtube_metadaten(url: str, vid: str) -> tuple[str, str, str, str]:
    """Titel, Kanal, Datum und Beschreibung ohne YouTube-API-Key abrufen."""
    titel = vid
    autor = ""
    datum = heute()
    beschreibung = ""
    videoseite = ""

    try:
        videoseite = hole(f"https://www.youtube.com/watch?v={vid}").decode(
            "utf-8", errors="replace"
        )
        marker = "var ytInitialPlayerResponse = "
        start = videoseite.find(marker)
        if start >= 0:
            start += len(marker)
            ende = videoseite.find(";</script>", start)
            if ende >= 0:
                import json

                player = json.loads(videoseite[start:ende])
                details = player.get("videoDetails", {})
                microformat = player.get("microformat", {}).get(
                    "playerMicroformatRenderer", {}
                )
                titel = details.get("title") or titel
                autor = details.get("author") or autor
                beschreibung = (details.get("shortDescription") or "").strip()
                datum = iso_datum(microformat.get("publishDate") or datum)
    except Exception:  # noqa: BLE001 — Metadaten haben einen oEmbed-Fallback
        pass

    if titel == vid or not autor:
        try:
            import json

            ziel = "https://www.youtube.com/oembed?format=json&url=" + urllib.parse.quote(
                f"https://www.youtube.com/watch?v={vid}", safe=""
            )
            daten = json.loads(hole(ziel).decode("utf-8", errors="replace"))
            titel = daten.get("title") or titel
            autor = daten.get("author_name") or autor
        except Exception:  # noqa: BLE001 — Metadaten sind optional
            pass

    if datum == heute():
        treffer = re.search(
            r'itemprop="datePublished"\s+content="(\d{4}-\d{2}-\d{2})', videoseite
        )
        if treffer:
            datum = treffer.group(1)

    return titel, autor, datum, beschreibung


# -------------------------------------------------------------------------- PDF


def lade_pdf(eingabe: str, medien_laden: bool) -> Quelle:
    try:
        import fitz
    except ImportError:
        raise SystemExit("[FEHLER] PyMuPDF fehlt. Installieren:\n  python -m pip install pymupdf")

    lokal = Path(eingabe)
    quell_url = eingabe
    if re.match(r"^https?://", eingabe, re.I):
        ziel = pdf_dateien_ordner() / Path(urllib.parse.urlparse(eingabe).path).name
        if not ziel.exists():
            ziel.parent.mkdir(parents=True, exist_ok=True)
            ziel.write_bytes(hole(eingabe, timeout=120))
        lokal = ziel
    else:
        quell_url = lokal.resolve().as_uri()
    if not lokal.exists():
        raise SystemExit(f"[FEHLER] PDF nicht gefunden: {lokal}")

    dok = fitz.open(lokal)
    meta = dok.metadata or {}
    seiten: list[str] = []
    for nummer, seite in enumerate(dok, 1):
        text = seite.get_text().strip()
        if text:
            seiten.append(f"### Seite {nummer}\n\n{text}")

    medien: list[Medium] = []
    if medien_laden:
        gesehen: set[int] = set()
        for nummer, seite in enumerate(dok, 1):
            for treffer in seite.get_images(full=True):
                xref = treffer[0]
                if xref in gesehen:
                    continue
                gesehen.add(xref)
                try:
                    bild = dok.extract_image(xref)
                except Exception as err:  # noqa: BLE001
                    medien.append(Medium(url=f"xref:{xref}", error=str(err)))
                    continue
                daten = bild["image"]
                if len(daten) < MIN_IMAGE_BYTES:
                    continue
                medien.append(
                    Medium(
                        url=f"xref:{xref}",
                        alt=f"Abbildung von Seite {nummer}",
                        local=f"s{nummer:02d}-{xref}.{bild.get('ext', 'png')}",
                        daten=daten,
                    )
                )

    titel = (meta.get("title") or "").strip() or lokal.stem.replace("-", " ")
    return Quelle(
        url=quell_url,
        typ="pdf",
        titel=titel,
        text="\n\n".join(seiten),
        autor=(meta.get("author") or "").strip(),
        datum=iso_datum(meta.get("creationDate")),
        medien=medien,
        extra={"seiten": str(dok.page_count), "datei": str(lokal.relative_to(REPO_ROOT)) if lokal.is_relative_to(REPO_ROOT) else lokal.name},
    )


# ------------------------------------------------------------- Medien & Ausgabe


def schreibe_vorhandene(medien: list[Medium], ziel: Path) -> None:
    """Bereits extrahierte Bilddaten (PDF) ablegen, sobald der Slug feststeht."""
    zu_schreiben = [m for m in medien if m.daten and m.local]
    if not zu_schreiben:
        return
    ziel.mkdir(parents=True, exist_ok=True)
    for medium in zu_schreiben:
        (ziel / medium.local).write_bytes(medium.daten)
        medium.daten = None  # Speicher freigeben, Zustand eindeutig halten


def lade_medien(medien: list[Medium], ziel: Path) -> None:
    """Remote-Bilder holen. Fehlschlag ist nie fatal — die URL bleibt erhalten."""
    if not medien:
        return
    index = 0
    for medium in medien:
        if medium.local or medium.url.startswith("xref:"):
            continue
        index += 1
        ziel.mkdir(parents=True, exist_ok=True)
        try:
            daten = hole(medium.url, timeout=30)
            if len(daten) < MIN_IMAGE_BYTES:
                medium.error = f"zu klein ({len(daten)} Bytes) — wohl Icon oder Tracking-Pixel"
                continue
            endung = Path(urllib.parse.urlparse(medium.url).path).suffix.lower()
            if endung not in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".avif"}:
                endung = mimetypes.guess_extension(
                    mimetypes.guess_type(medium.url)[0] or "image/jpeg"
                ) or ".jpg"
            name = f"{index:02d}-bild{endung}"
            (ziel / name).write_bytes(daten)
            medium.local = name
        except (urllib.error.URLError, OSError, ValueError) as err:
            medium.error = str(err)


def yaml_str(wert: str) -> str:
    return '"' + str(wert).replace("\\", "\\\\").replace('"', '\\"') + '"'


def baue_notiz(quelle: Quelle, slug: str) -> str:
    geladen = [m for m in quelle.medien if m.local]
    zeilen = [
        "---",
        f"url: {quelle.url}",
        f"titel: {yaml_str(quelle.titel)}",
    ]
    if quelle.autor:
        zeilen.append(f"autor: {yaml_str(quelle.autor)}")
    zeilen += [
        f"datum: {iso_datum(quelle.datum)}",
        f"erfasst: {heute()}",
        f"typ: {quelle.typ}",
        f"quelle: {quelle.typ}",
        "status: neu",
    ]
    if quelle.medien:
        zeilen.append(f'medien: "{len(geladen)}/{len(quelle.medien)} lokal"')
    for schluessel, wert in quelle.extra.items():
        zeilen.append(f"{schluessel}: {yaml_str(wert)}")
    zeilen += ["---", "", f"# {quelle.titel}", ""]

    herkunft = (
        f"[{quelle.url}]({quelle.url})" if quelle.url.startswith("http") else f"`{quelle.url}`"
    )
    zeilen += [
        f"> Automatisch per `python ai.py ingest` erfasst. Quelle: {herkunft}",
        "",
    ]

    if quelle.typ == "youtube":
        if quelle.beschreibung:
            zeilen += ["## Videobeschreibung", "", quelle.beschreibung, ""]
        zeilen += ["## Transkript", ""]
    elif quelle.typ == "pdf":
        zeilen += ["## Volltext", ""]
    else:
        zeilen += ["## Inhalt", ""]
    zeilen += [quelle.text or "_(kein Text extrahiert)_", ""]

    if quelle.medien:
        zeilen += ["## Bilder", ""]
        for medium in quelle.medien:
            alt = medium.alt or "Abbildung"
            if medium.local:
                zeilen += [f"![{alt}]({MEDIA_DIRNAME}/{slug}/{medium.local})", ""]
            elif medium.error:
                zeilen += [f"- ⚠️ nicht gespeichert ({medium.error}): {medium.url}", ""]
            else:
                zeilen += [f"- {medium.url}", ""]
    return "\n".join(zeilen)


def quellen_dateien() -> list[Path]:
    """Alle Quellnotizen rekursiv, ohne Verwaltungsdateien."""
    if not INBOX.exists():
        return []
    return [p for p in sorted(INBOX.rglob("*.md")) if p.name not in KEINE_QUELLEN]


def eindeutiger_slug(basis: str, url: str, ordner: Path | None = None) -> str:
    """Kollision verhindern: Zwei verschiedene Quellen können denselben Slug
    erzeugen (etwa wenn beide Seiten denselben og:title tragen). Ohne diese
    Prüfung würde die zweite Quelle die erste überschreiben — auch mit --force,
    das nur das Überschreiben derselben Quelle erlauben soll."""
    normalisiert = url.split("?")[0].rstrip("/")
    ordner = ordner or INBOX
    kandidat = basis
    zaehler = 2
    while True:
        notiz = ordner / f"{kandidat}.md"
        if not notiz.exists():
            return kandidat
        treffer = re.search(r"(?m)^url:\s*(.+)$", notiz.read_text(encoding="utf-8"))
        if treffer and treffer.group(1).strip().split("?")[0].rstrip("/") == normalisiert:
            return kandidat  # dieselbe Quelle — darf überschrieben werden
        kandidat = f"{basis}-{zaehler}"
        zaehler += 1


def finde_dublette(url: str) -> Path | None:
    normalisiert = url.split("?")[0].rstrip("/")
    for datei in quellen_dateien():
        treffer = re.search(r"(?m)^url:\s*(.+)$", datei.read_text(encoding="utf-8"))
        if treffer and treffer.group(1).strip().split("?")[0].rstrip("/") == normalisiert:
            return datei
    return None


# -------------------------------------------------------------------------- CLI


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Quelle nach 00_Inbox/Quellen/<Quelltyp>/ erfassen"
    )
    parser.add_argument("eingabe", help="URL oder Pfad zu einer PDF")
    parser.add_argument("--typ", choices=["auto", "url", "youtube", "pdf"], default="auto")
    parser.add_argument("--no-media", action="store_true", help="keine Bilder laden")
    parser.add_argument("--force", action="store_true", help="bestehende Notiz überschreiben")
    parser.add_argument("--titel", help="Titel überschreiben (falls schlecht erkannt)")
    args = parser.parse_args()

    typ = args.typ if args.typ != "auto" else erkenne_typ(args.eingabe)
    medien_laden = not args.no_media

    if not args.force:
        vorhanden = finde_dublette(args.eingabe)
        if vorhanden:
            print(f"[INFO] Quelle bereits erfasst: {vorhanden.relative_to(REPO_ROOT)}")
            print("  Unverändert gelassen. --force überschreibt sie.")
            return 0

    if typ == "pdf":
        quelle = lade_pdf(args.eingabe, medien_laden)
    elif typ == "youtube":
        quelle = lade_youtube(args.eingabe)
    else:
        quelle = lade_artikel(args.eingabe)

    if args.titel:
        quelle.titel = args.titel
    ziel_ordner = quelltyp_ordner(quelle.typ)
    slug = eindeutiger_slug(baue_slug(quelle), quelle.url, ziel_ordner)
    medien_ziel = ziel_ordner / MEDIA_DIRNAME / slug

    notiz = ziel_ordner / f"{slug}.md"
    if notiz.exists() and not args.force:
        print(f"[INFO] Notiz existiert bereits: {notiz.relative_to(REPO_ROOT)}")
        print("  Unverändert gelassen. --force überschreibt sie.")
        return 0

    # Erst schreiben, wenn feststeht, dass die Notiz auch entsteht — sonst
    # bleiben Medienordner ohne zugehörige Notiz zurück.
    if medien_laden:
        schreibe_vorhandene(quelle.medien, medien_ziel)
        lade_medien(quelle.medien, medien_ziel)

    ziel_ordner.mkdir(parents=True, exist_ok=True)
    notiz.write_text(baue_notiz(quelle, slug), encoding="utf-8")

    geladen = len([m for m in quelle.medien if m.local])
    for medium in (m for m in quelle.medien if m.error):
        print(f"[WARNUNG] Medium übersprungen: {medium.error}")
    print(f"[OK] Quelle: {notiz.relative_to(REPO_ROOT)}")
    info = f"  Typ: {typ} · {len(quelle.text)} Zeichen"
    if quelle.autor:
        info += f" · Autor: {quelle.autor}"
    if quelle.medien:
        info += f" · Medien: {geladen}/{len(quelle.medien)} lokal"
    print(info)
    print("  status: neu — wird beim nächsten Sammel-Lauf verarbeitet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
