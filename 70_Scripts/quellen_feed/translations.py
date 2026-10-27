"""Geprüfte Feed-Übersetzungen; Roharchiv und API-Caches bleiben Originalbelege."""
import json
from pathlib import Path
import re
import unicodedata

SUPPORTED = {"de", "en"}
NEUTRAL = {"und", "zxx", "qme", "qst"}
LANGUAGES = {"de": "Deutsch", "en": "Englisch", "ja": "Japanisch", "zh": "Chinesisch",
             "fr": "Französisch", "es": "Spanisch", "pt": "Portugiesisch", "ru": "Russisch"}

# Nur bekannte Archivgrenzen: Überschriften innerhalb eines Originalposts bleiben Inhalt.
ARCHIVE_SECTIONS = re.compile(
    r"^## (Post-Text|Artikel-Volltext|Thread|Caption|Inhalt|Volltext|Links|Bilder|"
    r"Erfassungsnachweis[^\n]*|Ergänzende Thread-[^\n]*|Ergänz(?:te|ungen aus) Artikel-[^\n]*|"
    r"Eingebettete Tweets|Zitierte Posts innerhalb der Einbettungen|Weitere Zitatverweise aus der API-Antwort|"
    r"Archivierungsstand und Grenzen|Archivierte Bilder aus dem Thread|Folge-Post \(nachgetragen\)|"
    r"Medien des geteilten Posts|Medien der Thread-Fortsetzungen)[ \t]*\n", re.M,
)
POST_SECTIONS = {"Post-Text", "Artikel-Volltext", "Caption", "Inhalt", "Volltext"}


def content_units(body: str) -> list[tuple[int, int, str]]:
    """Aktuelle vollständige Posts abgrenzen; gleiche Haupt-/Threadposts bleiben erkennbar."""
    units = []

    def add(start: int, end: int, label: str) -> None:
        text = body[start:end]
        if text.strip():
            units.append((start + len(text) - len(text.lstrip()), start + len(text.rstrip()), label))

    headers = list(ARCHIVE_SECTIONS.finditer(body))
    for index, header in enumerate(headers):
        start, end = header.end(), headers[index + 1].start() if index + 1 < len(headers) else len(body)
        title = header[1].strip()
        if title in POST_SECTIONS:
            add(start, end, title)
        elif title == "Thread":
            posts = list(re.finditer(r"^### (\d+/\d+)[^\n]*\n", body[start:end], re.M))
            add(start, start + posts[0].start() if posts else end, "Thread-Einleitung")
            for position, post in enumerate(posts):
                stop = start + posts[position + 1].start() if position + 1 < len(posts) else end
                add(start + post.end(), stop, f"Thread-Post {post[1]}")
    if not units:
        add(0, len(body), "Archivtext")
    return units


def neutral_content(text: str) -> bool:
    text = re.sub(r"https?://\S+|@[\w]+", "", text)
    return not any(char.isalpha() for char in text)


def foreign_script(text: str) -> bool:
    # NFKC macht auch dekorative englische Unicode-Schrift zu lateinischem Text.
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"https?://\S+|@[\w]+", "", text)
    letters = [c for c in text if c.isalpha() and "LATIN" not in unicodedata.name(c, "")]
    return len(letters) >= 5


class TranslationCatalog:
    def __init__(self, root: Path):
        self.root = root
        file = root / "feed/translations/x.json"
        data = json.loads(file.read_text(encoding="utf-8")) if file.is_file() else {"version": 1, "notes": {}}
        if data.get("version") != 1:
            raise ValueError("Unbekanntes Format für X-Übersetzungen")
        self.notes = data["notes"]
        self.translated = set()
        for name, record in self.notes.items():
            if record["target_language"] not in SUPPORTED or not record.get("source_language"):
                raise ValueError(f"Ungültige Übersetzungssprache: {name}")
            for segment in record["segments"]:
                if not segment["original"].strip() or not segment["translated"].strip():
                    raise ValueError(f"Leeres Übersetzungssegment: {name}")
            for segment in record.get("unchanged_segments", []):
                if segment.get("language") not in SUPPORTED or not segment["original"].strip() or foreign_script(segment["original"]):
                    raise ValueError(f"Ungültige Freigabe für unveränderten Inhalt: {name}")

    def apply(self, note: Path, meta: dict, body: str) -> tuple[str, dict]:
        key = note.relative_to(self.root).as_posix()
        record = self.notes.get(key)
        languages = meta.get("inhalt_sprachen") or [meta.get("sprache", "")]
        if isinstance(languages, str):
            languages = [languages]
        foreign = any(str(lang).split("-")[0].lower() not in SUPPORTED | NEUTRAL | {""} for lang in languages)
        def missing(detail: str) -> ValueError:
            return ValueError(f"X-Übersetzung fehlt oder passt nicht mehr: {key} ({detail}). "
                              "Bitte den vollständigen Inhalt in feed/translations/x.json auf Deutsch oder Englisch ergänzen.")

        if not record:
            if foreign or foreign_script(body):
                raise missing("kein Übersetzungseintrag")
            return body, {}

        replacements = {}
        for segment in record["segments"]:
            original = segment["original"].replace("\r\n", "\n").strip()
            if original in replacements:
                raise missing("mehrdeutiges Originalsegment")
            replacements[original] = segment["translated"].replace("\r\n", "\n").strip()
        unchanged = {segment["original"].replace("\r\n", "\n").strip()
                     for segment in record.get("unchanged_segments", [])}
        if unchanged & replacements.keys():
            raise missing("Inhalt gleichzeitig übersetzt und unverändert freigegeben")

        result = body.replace("\r\n", "\n")
        used, edits = set(), []
        for start, end, label in content_units(result):
            original = result[start:end]
            if original in replacements:
                edits.append((start, end, replacements[original]))
                used.add(original)
            elif original in unchanged:
                used.add(original)
            elif not neutral_content(original):
                raise missing(f"{label} ist nicht vollständig abgedeckt")
        if (replacements.keys() | unchanged) - used:
            raise missing("veraltetes oder nicht zuordenbares Originalsegment")
        if not edits:
            raise missing("kein vollständiger Post übersetzt")
        for start, end, translated in reversed(edits):
            result = result[:start] + translated + result[end:]
        if foreign_script(result):
            raise missing("nicht unterstützte Schrift bleibt im Archivtext")
        self.translated.add(key)
        source = LANGUAGES.get(record["source_language"], record["source_language"])
        target = LANGUAGES[record["target_language"]]
        notice = f"{source} → {target} · Übersetzung des archivierten Originaltexts."
        if unchanged:
            notice += " Bereits deutsch- oder englischsprachige Bestandteile bleiben unverändert."
        return result, {"language": record["target_language"],
                        "notice": notice}
