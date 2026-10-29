"""Privaten Kurs für R2 vorbereiten; Volltexte und Videos bleiben außerhalb von Git."""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import re
import os
import shutil
from pathlib import Path
from urllib.parse import quote

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "pocock"
ARCHIVE = ROOT / "00_Inbox/Quellen/URL/lokal/matt-pocock-software-factories-real-engineers"
INVENTORY = ROOT / "docs/kurse/matt-pocock-software-factories/inventar.json"
REPORT = ROOT / "reports/2026-10-29-matt-pocock-software-factories-kursanalyse.md"


def hashes(path: Path) -> tuple[str, str]:
    sha, md5 = hashlib.sha256(), hashlib.md5(usedforsecurity=False)
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            sha.update(chunk)
            md5.update(chunk)
    return sha.hexdigest(), md5.hexdigest()


def inline_script_hashes(soup: BeautifulSoup) -> list[str]:
    # get_text() lässt per .string gesetzte NavigableStrings in Script-Tags aus.
    # .string entspricht dagegen dem tatsächlich serialisierten Script-Inhalt.
    return sorted({"sha256-" + base64.b64encode(hashlib.sha256(str(tag.string or "").encode("utf-8")).digest()).decode("ascii") for tag in soup.find_all("script")})


def analysis_html() -> str:
    content = MarkdownIt("commonmark", {"html": False}).enable("table").render(REPORT.read_text(encoding="utf-8"))
    soup = BeautifulSoup(content, "html.parser")
    used, toc = set(), []
    for heading in soup.find_all(["h2", "h3", "h4"]):
        title = heading.get_text(" ", strip=True)
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower().translate(str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}))).strip("-")
        unique = slug
        counter = 2
        while unique in used:
            unique = slug + "-" + str(counter)
            counter += 1
        used.add(unique)
        heading["id"] = unique
        if heading.name == "h2":
            item = soup.new_tag("li")
            link = soup.new_tag("a", href="#" + unique)
            link.string = title
            item.append(link)
            toc.append(str(item))
    for table in list(soup.find_all("table")):
        wrapper = soup.new_tag("div", attrs={"class": "table-wrap"})
        table.wrap(wrapper)
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.startswith(("https://", "http://", "#")):
            continue
        if "index.de.html" in href:
            link["href"] = "/" + ("#" + href.split("#", 1)[1] if "#" in href else "")
        elif "lokal/" in href:
            del link["href"]
            link["title"] = "Das unveränderte Original liegt im lokalen Kursarchiv."
        else:
            relative = (REPORT.parent / href).resolve()
            if relative.is_relative_to(ROOT) and relative.exists():
                link["href"] = "https://github.com/spiral023/ai-company-os/blob/main/" + quote(relative.relative_to(ROOT).as_posix(), safe="/")
            else:
                del link["href"]
    template = (APP / "templates/analysis.html").read_text(encoding="utf-8")
    return template.replace("{{TOC}}", "".join(toc)).replace("{{BODY}}", str(soup))


def build(source: Path = ARCHIVE) -> dict:
    output = APP / "_site"
    output.mkdir(exist_ok=True)
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    original = source / "index.de.html"
    source_sha, _ = hashes(original)
    if source_sha != inventory["deutsche_ausgabe"]["sha256"]:
        raise ValueError("Die deutsche HTML-Quelle weicht vom geprüften Inventar ab.")
    soup = BeautifulSoup(original.read_text(encoding="utf-8"), "html.parser")
    chapters = soup.select("article.chapter")
    if len(chapters) != 38 or len(soup.select(".video-local")) != 38:
        raise ValueError("38 Kapitel mit eindeutig zugeordneten Videolinks erforderlich.")
    images = inventory["abbildungen"]
    input_videos = [entry for entry in inventory["originale"] if entry["name"].lower().endswith(".mp4")]
    if len(input_videos) != 38 or len(images) != 156:
        raise ValueError("Unvollständiges Kursinventar.")
    uploads = []
    content = {}

    def asset(route: str, file: Path, mime: str, expected: str | None = None) -> None:
        sha, md5 = hashes(file)
        if expected and sha != expected:
            raise ValueError("Archivdatei weicht vom Inventar ab: " + file.name)
        stem = Path(route).stem
        key = f"kurs/media/{Path(route).parts[1]}/{stem}-{sha[:16]}{file.suffix.lower()}"
        entry = {"key": key, "type": mime, "bytes": file.stat().st_size, "sha256": sha, "md5": md5}
        content[route] = entry
        uploads.append({"route": route, "file": str(file.resolve()), **entry})

    for number, video in enumerate(input_videos, 1):
        file = source / "videos" / video["name"]
        if not file.name.startswith(f"{number:03d} "):
            raise ValueError("Videonummer stimmt nicht mit Kapitel überein.")
        asset(f"/videos/{number:03d}.mp4", file, "video/mp4", video["sha256"])
    for image in images:
        file = source / "medien" / f"{image['nr']:03d}.png"
        asset(f"/medien/{image['nr']:03d}.png", file, "image/png", image["sha256"])
    for number, chapter in enumerate(chapters, 1):
        holder = chapter.select_one(".video-local")
        holder.name = "div"
        holder["class"] = "course-video"
        holder.clear()
        video = soup.new_tag("video", controls="", playsinline="", preload="none", attrs={"data-lesson": str(number), "aria-label": chapter["data-title"]})
        video.append(soup.new_tag("source", src=f"/videos/{number:03d}.mp4", type="video/mp4"))
        holder.append(video)
    for image in soup.find_all("img", src=True):
        if image["src"].startswith("medien/"):
            image["src"] = "/" + image["src"]
    actions = soup.new_tag("nav", attrs={"class": "course-actions", "aria-label": "Kursbereich"})
    actions.append(BeautifulSoup('<a href="/" aria-current="page">Kurs</a><a href="/analyse/">Ausführliche Analyse</a><form method="post" action="/logout"><button type="submit">Abmelden</button></form>', "html.parser"))
    soup.select_one(".wrap").insert(0, actions)
    side_link = soup.new_tag("a", href="/analyse/", attrs={"class": "analysis-link"})
    side_link.string = "Ausführliche Analyse →"
    soup.select_one(".brand").insert_after(side_link)
    soup.style.append("\n.course-actions{display:flex;gap:1.1rem;align-items:center;flex-wrap:wrap;font:13px/1.5 ui-sans-serif,sans-serif;margin:0 0 2.1rem}.course-actions a{color:var(--ink-soft);text-decoration:none}.course-actions a[aria-current]{color:var(--copper-deep);font-weight:700}.course-actions form{margin-left:auto}.course-actions button{background:none;border:1px solid var(--line);border-radius:6px;padding:7px 11px;color:var(--ink-soft);font-size:12px;cursor:pointer}.analysis-link{display:block;color:#e7c2b0;margin:0 1.2rem 1rem;font:13px/1.5 ui-sans-serif,sans-serif;text-decoration:none}.course-video{margin:1.1rem 0 1.6rem}.course-video video{width:100%;aspect-ratio:16/9;display:block;object-fit:contain;background:#14110e;border-radius:12px}.chapter-head .course-video{margin-bottom:1.1rem}\n")
    script = soup.new_tag("script")
    reader_script = soup.find("script")
    visibility = 'chapters.forEach(function (chapter) { chapter.hidden = selected ? chapter !== selected : chapter !== chapters[0]; });'
    if reader_script.get_text().count(visibility) != 1:
        raise ValueError("Die Kapitelsteuerung hat sich geändert; Video-Pausenlogik prüfen.")
    reader_script.string = reader_script.get_text().replace(visibility, visibility + "\n    document.querySelectorAll('video').forEach(function (video) { if (video.closest('.chapter').hidden) video.pause(); });")
    script.string = """
(function () {
  window.addEventListener('pageshow', function (event) { if (event.persisted) location.reload(); });
})();
"""
    soup.body.append(script)
    (output / "index.html").write_text(str(soup), encoding="utf-8", newline="\n")
    (output / "analyse").mkdir(exist_ok=True)
    (output / "analyse/index.html").write_text(analysis_html(), encoding="utf-8", newline="\n")
    script_hashes = inline_script_hashes(soup)
    fingerprint = hashlib.sha256((output / "index.html").read_bytes() + (output / "analyse/index.html").read_bytes()).hexdigest()[:20]
    release = "releases/" + fingerprint
    for route, relative in [("/", "index.html"), ("/analyse/", "analyse/index.html")]:
        file = output / relative
        sha, md5 = hashes(file)
        entry = {"key": "kurs/" + release + "/" + relative, "type": "text/html; charset=utf-8", "bytes": file.stat().st_size, "sha256": sha, "md5": md5}
        content[route] = entry
        uploads.append({"route": route, "file": str(file.resolve()), **entry})
    module = "// Automatisch erzeugte R2-Zuordnung; enthält keine Kursvolltexte oder Secrets.\n"
    module += "export const RELEASE_ID = " + json.dumps(fingerprint) + ";\n"
    module += "export const SCRIPT_HASHES = " + json.dumps(script_hashes) + ";\n"
    module += "export const CONTENT = " + json.dumps(dict(sorted(content.items())), ensure_ascii=False, indent=2) + ";\n"
    (APP / "content-manifest.mjs").write_text(module, encoding="utf-8", newline="\n")
    manifest = {"bucket": "sp23-pocock-kurs", "release": fingerprint, "objects": uploads}
    (output / "upload-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    assert len(content) == len(uploads) == 196
    assert len(soup.find_all("video")) == 38
    assert not soup.select(".video-local")
    print(f"Kurs gebaut: 38 Videos, 156 Bilder, Kurs und Analyse; Release {fingerprint}")
    return manifest


def prepare_browser_upload(manifest: dict) -> list[Path]:
    """Dashboard-Limit von 100 Dateien pro Auswahl beachten; Videos nicht duplizieren."""
    batch_size = 75
    target = APP / "_site/browser-upload" / manifest["release"] / f"dashboard-{batch_size}"
    ordered = sorted(manifest["objects"], key=lambda item: (0 if item["route"].startswith("/medien/") else 1 if item["route"].startswith("/videos/") else 2, item["route"]))
    folders = []
    for index, entry in enumerate(ordered):
        batch = target / f"batch-{index // batch_size + 1:02d}"
        original = Path(entry["file"])
        link = batch / entry["key"]
        link.parent.mkdir(parents=True, exist_ok=True)
        if not link.exists():
            if entry["type"].startswith("text/html"):
                shutil.copyfile(original, link)
            else:
                os.link(original, link)
        elif hashes(link)[0] != entry["sha256"]:
            raise ValueError("Vorhandene Upload-Datei stimmt nicht mit dem Manifest überein: " + str(link))
        if index % batch_size == 0:
            folders.append(batch / "kurs")
    for folder in folders:
        print("Browser-Uploadordner:", folder)
    return folders


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ARCHIVE, help="Lokales, bereits inventarisiertes Kursarchiv")
    parser.add_argument("--browser-upload", action="store_true", help="Passende Ordnerstruktur als lokale Hardlinks vorbereiten")
    args = parser.parse_args()
    manifest = build(args.source)
    if args.browser_upload:
        prepare_browser_upload(manifest)
