#!/usr/bin/env python3
"""Erzeuge die offline nutzbare HTML-Kanalliste aus Guide und Profilmetadaten."""

from __future__ import annotations

import argparse
import base64
import html
import json
import mimetypes
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "80_Knowledge/Guides/AI-Coding-Agents-Social-Media-Uebersicht.md"
SITE = ROOT / "docs/ki-quellen"


def escape(value: str) -> str:
    return html.escape(value, quote=True)


def icon(name: str) -> str:
    return f'<svg class="icon" aria-hidden="true"><use href="#{name}"></use></svg>'


def read_guide(path: Path) -> dict[str, dict]:
    sections = {}
    current = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("### "):
            raw = line[4:]
            current = re.split(r" — \[", raw)[0]
            if current in sections:
                raise ValueError(f"Doppelte Überschrift: {current}")
            links = []
            for handle, url in re.findall(r"\[([^]]+)\]\(([^)]+)\)", raw):
                platform = "TikTok" if "tiktok.com" in url else "X"
                links.append({"platform": platform, "url": url, "handle": handle})
            sections[current] = {"description": [], "links": links}
        elif line.startswith("## "):
            current = None
        elif current and line.strip():
            sections[current]["description"].append(line.strip())
    for heading, section in sections.items():
        if len(section["description"]) != 1:
            raise ValueError(f"Genau ein Beschreibungsabsatz erwartet: {heading}")
        section["description"] = section["description"][0]
    return sections


def validate_url(url: str, hosts: set[str] | None = None) -> str:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError(f"Ungültiger HTTPS-Link: {url}")
    if hosts and parsed.hostname not in hosts:
        raise ValueError(f"Unerwartete Kanal-Domain: {url}")
    return url


def load_profiles() -> tuple[dict, list[dict]]:
    metadata = json.loads((SITE / "profiles.json").read_text(encoding="utf-8"))
    research_file = SITE / "image-research.json"
    research = json.loads(research_file.read_text(encoding="utf-8")) if research_file.exists() else {}
    sections = read_guide(GUIDE)
    covered = []
    ids = set()
    profiles = []
    for item in metadata["profiles"]:
        profile = dict(item)
        if not re.fullmatch(r"[a-z0-9-]+", profile["id"]) or profile["id"] in ids:
            raise ValueError(f"Ungültige oder doppelte ID: {profile['id']}")
        ids.add(profile["id"])
        if profile["language"] not in {"DE", "EN", "DE/EN"}:
            raise ValueError(f"Sprache fehlt: {profile['id']}")
        if not set(profile["topics"]).issubset(metadata["topics"]):
            raise ValueError(f"Unbekannte Themen: {profile['id']}")
        source = sections[profile["sourceHeadings"][0]]
        profile["description"] = profile.get("description") or source["description"]
        if not 300 <= len(profile["description"]) <= 500:
            raise ValueError(f"Beschreibung außerhalb von 300–500 Zeichen: {profile['id']}")
        profile["links"] = []
        asset = research.get(profile["id"], {})
        for heading in profile["sourceHeadings"]:
            covered.append(heading)
            links = sections[heading]["links"]
            if not links:
                url = asset.get("channelUrl")
                if not url:
                    raise ValueError(f"Verifizierter YouTube-Kanallink fehlt: {heading}")
                links = [{"platform": "YouTube", "url": url, "handle": ""}]
            for link in links:
                validate_url(link["url"], {"x.com", "www.tiktok.com", "www.youtube.com", "youtube.com"})
                if link["url"] not in {entry["url"] for entry in profile["links"]}:
                    profile["links"].append(link)
        profile["image"] = ""
        profile["imageSource"] = ""
        if asset.get("image"):
            image_path = (SITE / asset["image"]).resolve()
            if not image_path.is_relative_to((SITE / "images").resolve()):
                raise ValueError("Bild liegt außerhalb des Bildordners")
            mime = mimetypes.guess_type(image_path.name)[0]
            if mime not in {"image/jpeg", "image/png", "image/webp"}:
                raise ValueError(f"Unzulässiger Bildtyp: {image_path}")
            profile["image"] = f"data:{mime};base64," + base64.b64encode(image_path.read_bytes()).decode()
            profile["imageSource"] = validate_url(asset["imageSource"])
        profile["followers"] = asset.get("followers")
        if profile["followers"]:
            followers = profile["followers"]
            validate_url(followers["source"])
            date.fromisoformat(followers["checkedAt"])
            if followers["platform"] not in {link["platform"] for link in profile["links"]}:
                raise ValueError(f"Follower-Plattform ohne Kanallink: {profile['id']}")
        profiles.append(profile)
    if len(covered) != len(set(covered)) or set(covered) != set(sections):
        raise ValueError(f"Guide-Abdeckung unvollständig: {set(sections) ^ set(covered)}")
    return metadata, profiles


def render_card(profile: dict, index: int) -> str:
    name = escape(profile["name"])
    identifier = escape(profile["id"])
    platform_order = {"X": 0, "YouTube": 1, "TikTok": 2}
    links = sorted(profile["links"], key=lambda entry: platform_order[entry["platform"]])
    handle = next((link["handle"] for link in links if link["handle"]), "")
    subtitle = escape(profile.get("subtitle") or handle or "KI-Wissen & praktische Arbeitsweisen")
    initials = "".join(word[0] for word in profile["name"].split()[:2])
    avatar = f'<span class="initials" aria-hidden="true">{escape(initials)}</span>'
    if profile["image"]:
        avatar = f'<img src="{profile["image"]}" width="76" height="76" alt="" loading="lazy" decoding="async">'
    tags = "".join(f'<span class="tag tag-{i % 3}">{escape(tag)}</span>' for i, tag in enumerate(profile["tags"]))
    buttons = "".join(
        f'<a class="platform-link" href="{escape(link["url"])}" target="_blank" rel="noopener noreferrer" '
        f'aria-label="{name} auf {link["platform"]} öffnen (neuer Tab)">'
        f'{icon(link["platform"].lower())}<span>{link["platform"]} öffnen</span>{icon("external")}</a>'
        for link in links
    )
    audience = ""
    if profile["followers"]:
        followers = profile["followers"]
        audience = f'<span class="audience" title="Stand {escape(followers["checkedAt"])} · {escape(followers["platform"])}">{icon("people")}{escape(followers["label"])} · {escape(followers["platform"])}</span>'
    search = " ".join([profile["name"], subtitle, profile["description"], *profile["tags"], *profile["topics"]])
    return f'''<article class="profile-card" data-id="{identifier}" data-order="{index}" data-name="{name}"
      data-language="{profile["language"]}" data-topics="{escape('|'.join(profile['topics']))}"
      data-platforms="{'|'.join(link['platform'] for link in links)}" data-search="{escape(search)}">
      <header class="profile-heading"><div class="avatar avatar-{index % 5}">{avatar}</div>
        <div class="profile-identity"><h3>{name}</h3><p class="handle">{subtitle}</p></div>
        <span class="language" title="{' / '.join('Deutsch' if lang == 'DE' else 'Englisch' for lang in profile['language'].split('/'))}">{profile['language']}</span>
        <button class="bookmark icon-button" type="button" aria-label="{name} merken" aria-pressed="false">{icon('bookmark')}</button>
      </header>
      <div class="tags">{tags}</div>
      <p class="description">{escape(profile['description'])}</p>
      {audience}<div class="profile-links">{buttons}</div>
    </article>'''


def build() -> str:
    metadata, profiles = load_profiles()
    template = (SITE / "template.html").read_text(encoding="utf-8")
    topic_buttons = '<button type="button" class="topic-chip" data-topic="" aria-pressed="true">Alle Themen</button>'
    topic_buttons += "".join(
        f'<button type="button" class="topic-chip" data-topic="{escape(topic)}" aria-pressed="false">{escape(topic)}</button>'
        for topic in metadata["topics"]
    )
    sources = []
    for profile in profiles:
        if profile["imageSource"]:
            sources.append(f'<li><span>{escape(profile["name"])}</span><a href="{escape(profile["imageSource"])}" target="_blank" rel="noopener noreferrer">Bildquelle {icon("external")}</a></li>')
        if profile["followers"]:
            followers = profile["followers"]
            sources.append(f'<li><span>{escape(profile["name"])} · {escape(followers["label"])} · {escape(followers["checkedAt"])}</span><a href="{escape(followers["source"])}" target="_blank" rel="noopener noreferrer">{escape(followers["platform"])} {icon("external")}</a></li>')
    updated = date.fromisoformat(metadata["updated"]).strftime("%d.%m.%Y")
    replacements = {
        "@@CARDS@@": "\n".join(render_card(profile, i) for i, profile in enumerate(profiles)),
        "@@TOPICS@@": topic_buttons,
        "@@COUNT@@": str(len(profiles)),
        "@@CHANNEL_COUNT@@": str(sum(len(profile["links"]) for profile in profiles)),
        "@@UPDATED@@": updated,
        "@@SOURCES@@": "\n".join(sources),
    }
    for token, value in replacements.items():
        template = template.replace(token, value)
    if re.search(r"@@[A-Z_]+@@", template):
        raise ValueError("Unersetzte Template-Platzhalter")
    return template


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Vorhandene HTML-Datei auf Aktualität prüfen")
    args = parser.parse_args()
    try:
        page = build()
        target = SITE / "index.html"
        if args.check:
            if not target.exists() or target.read_text(encoding="utf-8") != page:
                raise ValueError("HTML-Datei fehlt oder ist veraltet; Build ohne --check ausführen")
            print("OK: Guide, Metadaten, Bilder und HTML stimmen überein.")
        else:
            target.write_text(page, encoding="utf-8", newline="\n")
            print(f"Erstellt: {target} ({len(page.encode('utf-8')):,} Bytes)")
    except (ValueError, KeyError, OSError) as error:
        parser.exit(1, f"Fehler: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
