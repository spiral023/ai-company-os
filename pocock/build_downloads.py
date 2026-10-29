"""Vollständige private Leseexporte ohne Videos aus beiden Kursarchiven erzeugen."""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt
from markdownify import MarkdownConverter

from build_course import APP, ARCHIVE, INVENTORY, hashes

IMAGE_MODES = ("html-embedded-md-links", "embedded", "text-only")


class CourseMarkdown(MarkdownConverter):
    def convert_pre(self, el, text, parent_tags):
        raw = el.get_text()
        fence = "`" * max(3, max((len(match[0]) + 1 for match in re.finditer(r"`+", raw)), default=3))
        return "\n\n" + fence + "\n" + raw + ("" if raw.endswith("\n") else "\n") + fence + "\n\n"

    def convert_label(self, el, text, parent_tags):
        if "task" in el.get("class", []):
            return "[ ] " + text.strip() if el.find_parent("li") else "\n\n- [ ] " + text.strip() + "\n\n"
        return text


def prepare_content(source_html: str, language: str) -> BeautifulSoup:
    source = BeautifulSoup(source_html, "html.parser")
    wrap = source.select_one(".wrap")
    if wrap is None:
        raise ValueError("Kursinhalt .wrap fehlt.")
    soup = BeautifulSoup(str(wrap), "html.parser")
    for node in list(soup.select(".video-local, .course-video, video, audio, iframe, object, embed, script, .pager, .anchor, .colophon, .course-actions")):
        node.decompose()
    # Bild-Schaltflächen dürfen beim Entfernen der Bedienoberfläche keine Bilder verlieren.
    for button in list(soup.select("button.shot")):
        button.unwrap()
    for question in soup.select(".q"):
        choices = question.select_one(".choices")
        if choices:
            choices.name = "ol"
        for choice in question.select("button.choice"):
            choice.name = "li"
            choice.attrs.pop("type", None)
            key = choice.select_one(".key")
            if key:
                key.insert_after(" ")
            if choice.get("data-choice") == question.get("data-correct"):
                choice["class"] = list(choice.get("class", [])) + ["correct"]
        answer = soup.new_tag("p", attrs={"class": "export-answer"})
        answer.string = ("Richtige Antwort: " if language == "de" else "Correct answer: ") + question.get("data-correct", "").upper()
        if choices:
            choices.insert_after(answer)
    for button in list(soup.select("button")):
        button.decompose()
    for node in soup.select("[hidden]"):
        del node["hidden"]
    for checkbox in soup.select('input[type="checkbox"]'):
        checkbox["disabled"] = ""
    return soup


def configure_images(soup: BeautifulSoup, images: list[dict], mode: str, encoded: dict[int, str]) -> None:
    nodes = soup.select("article.chapter img")
    if len(nodes) != len(images):
        raise ValueError("Bildanzahl weicht vom Inventar ab.")
    for node, image in zip(nodes, images):
        # Die fortlaufende Nummer ist zusätzlich zur Position durch Quelle bzw. lokalen Pfad belegt.
        if node.get("src") not in (image["url"], f"medien/{image['nr']:03d}.png"):
            raise ValueError("Bildreihenfolge weicht vom Inventar ab.")
        if mode == "embedded":
            node["src"] = encoded[image["nr"]]
        elif mode == "links":
            node["src"] = image["url"]
        else:
            node.replace_with(soup.new_string(node.get("alt", "")))
            continue
        node["loading"] = "lazy"
        node["decoding"] = "async"
        node["width"], node["height"] = str(image.get("breite", 1)), str(image.get("hoehe", 1))
        for attr in ["srcset", "sizes"]:
            node.attrs.pop(attr, None)


def html_export(source_html: str, content: BeautifulSoup, language: str, image_mode: str) -> str:
    source = BeautifulSoup(source_html, "html.parser")
    css = str(source.find("style").string or "")
    note = {"de": "Deutsche Leseausgabe · alle 38 Kapitel · ohne Videos", "en": "Original English text · all 38 lessons · no videos"}[language]
    image_note = ("Alle Abbildungen sind in dieser Datei eingebettet." if language == "de" else "All illustrations are embedded in this file.") if image_mode != "text-only" else ("Textausgabe ohne Bilddateien." if language == "de" else "Text edition without image files.")
    override = """
.main{margin-left:0!important}.wrap{max-width:960px!important;margin:0 auto!important;padding:48px 24px!important}.chapter{display:block!important;content-visibility:visible!important}.explain{display:block!important}.choices{list-style:none;padding:0}.choice{cursor:default}.export-answer{font-weight:700}.export-note{font:14px/1.6 system-ui,sans-serif;padding:20px 0;border-bottom:1px solid #dcd1c0}.export-toc{margin:30px 0}.export-toc a{color:inherit}.export-toc li{margin:8px 0}.anchor,.pager,.colophon{display:none!important}figure img{cursor:default;max-width:100%;height:auto}@media print{.wrap{padding:0!important}.chapter{break-before:page}pre,figure{break-inside:avoid}}
"""
    toc = BeautifulSoup("<nav class='export-toc'><ol></ol></nav>", "html.parser")
    for chapter in content.select("article.chapter"):
        item = toc.new_tag("li")
        link = toc.new_tag("a", href="#" + chapter["id"])
        link.string = chapter.select_one("h1").get_text(" ", strip=True)
        item.append(link)
        toc.ol.append(item)
    document = BeautifulSoup('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title></title><style></style></head><body><main class="main"></main></body></html>', "html.parser")
    document.html["lang"] = language
    document.title.string = "Software Factories – " + ("Deutsch" if language == "de" else "English original")
    document.style.string = css + override
    note_element = document.new_tag("p", attrs={"class": "export-note"})
    note_element.string = note + ". " + image_note
    root = content.select_one(".wrap")
    root.insert(0, toc.nav)
    root.insert(0, note_element)
    document.main.append(root)
    return str(document)


def markdown_export(content: BeautifulSoup, language: str, image_mode: str) -> str:
    soup = BeautifulSoup(str(content), "html.parser")
    for chapter in soup.select("article.chapter"):
        for heading in chapter.find_all(re.compile(r"^h[1-6]$")):
            heading.name = "h" + str(min(6, int(heading.name[1]) + 1))
    for kicker in soup.select(".kicker"):
        kicker.string = kicker.get_text(" ", strip=True)
    note = "Deutsche Leseausgabe. Alle 38 Kapitel, ohne Videos." if language == "de" else "Original English text. All 38 lessons, no videos."
    if image_mode == "html-embedded-md-links":
        note += " Die Abbildungen sind über ihre Original-URLs verlinkt und benötigen Internet." if language == "de" else " Illustrations link to their original URLs and require an internet connection."
    elif image_mode == "embedded":
        note += " Die Abbildungen sind als Data-URLs eingebettet; der Markdown-Viewer muss diese unterstützen." if language == "de" else " Illustrations use embedded data URLs; your Markdown viewer must support them."
    text = CourseMarkdown(heading_style="ATX", bullets="-", wrap=False).convert(str(soup))
    return note + "\n\n" + text.strip() + "\n"


def validate_markdown(source: BeautifulSoup, text: str) -> None:
    tokens = MarkdownIt("commonmark").enable("table").parse(text)
    actual_code = [token.content.rstrip("\n") for token in tokens if token.type == "fence"]
    expected_code = [pre.get_text().rstrip("\n") for pre in source.select("article.chapter pre")]
    if actual_code != expected_code:
        raise ValueError("Markdown hat Codeblöcke verloren oder verändert.")
    if sum(token.type == "inline" and token.content.startswith("[ ] ") for token in tokens) != len(source.select(".task")):
        raise ValueError("Markdown-Checklisten sind unvollständig.")
    rendered = BeautifulSoup(MarkdownIt("commonmark").enable("table").render(text), "html.parser")
    normalize = lambda value: " ".join(value.split())
    if [normalize(heading.get_text(" ", strip=True)) for heading in rendered.select("h2")] != [normalize(chapter.select_one("h1").get_text(" ", strip=True)) for chapter in source.select("article.chapter")]:
        raise ValueError("Markdown hat Kapitelüberschriften verloren oder umsortiert.")
    actual_images = [child.attrGet("src") for token in tokens for child in (token.children or []) if child.type == "image"]
    if actual_images != [image["src"] for image in source.select("article.chapter img")]:
        raise ValueError("Markdown hat Abbildungen verloren oder verändert.")
    rendered_text = normalize(rendered.get_text(" ", strip=True))
    for paragraph in source.select("article.chapter p, article.chapter figcaption, article.chapter .choice .label"):
        value = normalize(paragraph.get_text(" ", strip=True))
        if value and value not in rendered_text:
            raise ValueError("Markdown hat einen Textabschnitt verändert: " + value[:80])


def build_downloads(source: Path = ARCHIVE, image_mode: str = IMAGE_MODES[0]) -> dict:
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    output = APP / "_site/downloads"
    output.mkdir(parents=True, exist_ok=True)
    images = inventory["abbildungen"]
    encoded = {}
    for image in images:
        path = source / "medien" / f"{image['nr']:03d}.png"
        if hashes(path)[0] != image["sha256"]:
            raise ValueError("Bild weicht vom Inventar ab: " + path.name)
        if image_mode != "text-only":
            encoded[image["nr"]] = "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode("ascii")
    objects, coverage = [], {}
    for language, name in [("de", "index.de.html"), ("en", "index.html")]:
        path = source / name
        expected = inventory["deutsche_ausgabe"]["sha256"] if language == "de" else next(entry["sha256"] for entry in inventory["originale"] if entry["name"] == name)
        if hashes(path)[0] != expected:
            raise ValueError("HTML-Quelle weicht vom Inventar ab: " + name)
        original = path.read_text(encoding="utf-8")
        content = prepare_content(original, language)
        chapters = content.select("article.chapter")
        if len(chapters) != 38 or len(content.select(".q")) != 22 or len(content.select(".task")) != 98 or len(content.select("pre")) != 175:
            raise ValueError("Unvollständige Kapitel, Quizfragen oder Aufgaben.")
        coverage[language] = {"kapitel": len(chapters), "quizfragen": len(content.select(".q")), "aufgaben": len(content.select(".task")), "codebloecke": len(content.select("pre")), "bilder": len(content.select("article.chapter img")), "quelle_sha256": expected}
        md_content = BeautifulSoup(str(content), "html.parser")
        configure_images(md_content, images, "embedded" if image_mode == "embedded" else "none" if image_mode == "text-only" else "links", encoded)
        markdown = markdown_export(md_content, language, image_mode)
        validate_markdown(md_content, markdown)
        configure_images(content, images, "none" if image_mode == "text-only" else "embedded", encoded)
        html = html_export(original, content, language, image_mode)
        for extension, payload, mime in [("html", html, "text/html; charset=utf-8"), ("md", markdown, "text/markdown; charset=utf-8")]:
            filename = f"software-factories-{language}.{extension}"
            file = output / filename
            file.write_text(payload, encoding="utf-8", newline="\n")
            sha, md5 = hashes(file)
            objects.append({"route": f"/downloads/{language}.{extension}", "file": str(file.resolve()), "filename": filename, "type": mime, "bytes": file.stat().st_size, "sha256": sha, "md5": md5})
        print(f"{language}: 38 Kapitel, 22 Quizfragen, 98 Aufgaben und 175 Codeblöcke exportiert.")
    fingerprint = hashlib.sha256("".join(item["sha256"] for item in objects).encode("ascii")).hexdigest()[:20]
    for entry in objects:
        entry["key"] = "kurs/downloads/" + fingerprint + "/" + entry["filename"]
    manifest = {"bucket": "sp23-pocock-kurs", "release": fingerprint, "image_mode": image_mode, "abdeckung": coverage, "objects": objects}
    (APP / "_site/download-upload-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    metadata = {entry["route"]: {key: value for key, value in entry.items() if key not in ("file", "route")} for entry in objects}
    module = "// Automatisch erzeugte Download-Metadaten; keine Kursvolltexte oder Zugangsdaten.\n"
    module += "export const DOWNLOAD_IMAGE_MODE = " + json.dumps(image_mode) + ";\n"
    module += "export const DOWNLOADS = " + json.dumps(metadata, ensure_ascii=False, indent=2) + ";\n"
    (APP / "download-manifest.mjs").write_text(module, encoding="utf-8", newline="\n")
    print("Vier Downloads gebaut; Release " + fingerprint)
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ARCHIVE)
    parser.add_argument("--image-mode", choices=IMAGE_MODES, default=IMAGE_MODES[0])
    args = parser.parse_args()
    build_downloads(args.source, args.image_mode)
