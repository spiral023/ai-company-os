"""Quellenfeed aus dem Markdown-Archiv bauen und lokal bereitstellen.

python ai.py quellen feed [--build] [--port 8766] [--ausgabe feed/_site]
Keine Abrufe beim Build. Die Ausgabe enthält nur ausgewählte Quellen und Medien.
"""
from __future__ import annotations

import argparse
import hashlib
import html
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import re
import shutil
from urllib.parse import unquote, urlsplit, parse_qs, quote

from markdown_it import MarkdownIt
from PIL import Image
import yaml

from quellen_statistik import ROOT, collect
from quellen_feed.avatars import local_author_images, refresh_avatars, author_profile_links
from quellen_feed.translations import TranslationCatalog

TEMPLATES = Path(__file__).with_name("quellen_feed")
MEDIA_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".mp4", ".pdf", ".vtt", ".txt"}


def read_note(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        raise ValueError(f"Frontmatter fehlt: {path.name}")
    return yaml.safe_load(match[1]), text[match.end():]


def section(body: str, name: str) -> str:
    """Abschnitt samt Unterüberschriften; ähnliche Titel wie Transkript (Ausschnitt)."""
    match = re.search(r"^## " + re.escape(name) + r"[^\n]*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    return match[1].strip() if match else ""


def title_of(body: str) -> str:
    match = re.search(r"^# (.+)$", body, re.M)
    return match[1].strip() if match else ""


def plain(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"!?\[([^\]]*)\]\([^\n]*?\)", r"\1", text)
    text = re.sub(r"[\[\]#*`>_]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def source_excerpt(body: str) -> tuple[str, str]:
    """Vorhandene Kernaussagen verwenden, ohne neue Zusammenfassungen zu erzeugen."""
    highlights = section(body, "Kernaussagen")
    tokens = MarkdownIt("commonmark").parse(highlights)
    lines = highlights.splitlines()
    items = ["\n".join(lines[t.map[0]:t.map[1]]) for t in tokens
             if t.type == "list_item_open" and t.level == 1 and t.map]
    if items:
        # Pattern-Dateinamen sind Querverweise, keine Kernaussagen. Im Volltext
        # bleiben sie verlinkt; die Vorschau beginnt direkt mit der Aussage.
        items = [re.sub(r"^([-*]\s+)\[\[[^\]]+\]\]\s*:\s*", r"\1", item) for item in items]
        items = [re.sub(r"\s*→\s*\[\[[^\]]+\]\]\s*$", "", item) for item in items]
        return "\n".join(items[:3]), "Kernaussagen"
    for token in MarkdownIt("commonmark").parse(body):
        if token.type == "paragraph_open" and token.level == 0 and token.map:
            return "\n".join(body.splitlines()[token.map[0]:token.map[1]]), "Aus der Aufarbeitung"
    return "", "Aufarbeitung"


def external_url(value: str) -> str:
    try:
        parts = urlsplit(value)
        if parts.scheme in {"http", "https"} and parts.netloc and not parts.username and not any(ord(c) < 32 for c in value):
            return value
    except ValueError:
        pass
    return ""


class Assets:
    """Nur referenzierte Dateien aus den zwei Wissensordnern in den Build aufnehmen."""

    def __init__(self, root: Path):
        self.root = root.resolve()
        self.allowed = [(root / p).resolve() for p in ("00_Inbox/Quellen", "80_Knowledge/Sources")]
        self.files: dict[str, Path] = {}
        self.missing: set[str] = set()

    def register(self, value: str, note: Path) -> str:
        try:
            url = urlsplit(value)
            if url.scheme not in {"", "file"} or url.netloc or value.startswith("//"):
                return ""
            local = unquote(url.path)
            if url.scheme == "file":
                local = re.sub(r"^/([A-Za-z]:/)", r"\1", local)
            path = (note.parent / local).resolve()
            if not any(path.is_relative_to(base) for base in self.allowed) or path.suffix.lower() not in MEDIA_SUFFIXES:
                return ""
            if not path.is_file():
                self.missing.add(path.relative_to(self.root).as_posix())
                return ""
            return self.remember(path)
        except (ValueError, OSError):
            return ""

    def remember(self, path: Path) -> str:
        stat = path.stat()
        key = f"{path.relative_to(self.root).as_posix()}:{stat.st_size}:{stat.st_mtime_ns}"
        name = hashlib.sha256(key.encode()).hexdigest()[:24] + path.suffix.lower()
        self.files[name] = path
        return "media/" + name

    def avatar(self, path: Path) -> str:
        path = path.resolve()
        allowed = [(self.root / p).resolve() for p in ("docs/ki-quellen/images", "feed/avatars/images")]
        if not any(path.is_relative_to(base) for base in allowed) or path.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"} or not path.is_file():
            return ""
        return self.remember(path)


def renderer(note: Path, assets: Assets, links: dict[str, str], wiki_topics: dict | None = None) -> MarkdownIt:
    md = MarkdownIt("commonmark", {"html": False, "breaks": True}).enable("table")

    def image_rule(tokens, index, options, env):
        token = tokens[index]
        src = token.attrGet("src") or ""
        local = assets.register(src, note)
        alt = html.escape(token.content or "Abbildung", quote=True)
        if local and Path(local).suffix in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
            return f'<a href="{local}" target="_blank" rel="noopener"><img src="{local}" alt="{alt}" loading="lazy" decoding="async"></a>'
        safe = external_url(src)
        return f'<a href="{html.escape(safe, quote=True)}" target="_blank" rel="noopener noreferrer">{alt} ↗</a>' if safe else f"<span>{alt}</span>"

    def link_rule(tokens, index, options, env):
        token = tokens[index]
        dest = token.attrGet("href") or ""
        safe = external_url(dest)
        topic = parse_qs(urlsplit(dest).query).get("topic", [""])[0] if dest.startswith("?topic=") else ""
        if topic and topic in (wiki_topics or {}).values():
            safe = "?topic=" + quote(topic, safe="")
        if not safe and dest.startswith("#"):
            safe = dest
        if not safe:
            try:
                path = (note.parent / unquote(urlsplit(dest).path)).resolve()
                key = path.relative_to(assets.root).as_posix()
                safe = f"#quelle={links[key]}" if key in links else assets.register(dest, note)
            except (ValueError, OSError):
                pass
        token.attrs = {"href": safe or "#"}
        if topic and safe.startswith("?topic="):
            token.attrSet("data-topic-link", topic)
        if external_url(safe) or safe.startswith("media/"):
            token.attrSet("target", "_blank")
            token.attrSet("rel", "noopener noreferrer")
        return md.renderer.renderToken(tokens, index, options, env)

    md.add_render_rule("image", lambda self, *args: image_rule(*args))
    md.add_render_rule("link_open", lambda self, *args: link_rule(*args))
    return md


def render_text(text: str, note: Path, assets: Assets, links: dict[str, str], wiki_topics: dict | None = None) -> str:
    # Wiki-Links bleiben lesbar; kein Zugriff auf den gesamten Vault aus dem Feed.
    def wiki(match):
        label = match[2] or match[1]
        topic = (wiki_topics or {}).get(match[1])
        return f"[{label}](?topic={quote(topic, safe='')})" if topic else label
    text = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", wiki, text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return renderer(note, assets, links, wiki_topics).render(text)


def media_of(body: str, note: Path, assets: Assets) -> list[dict]:
    found = []
    md = MarkdownIt("commonmark")
    for block in md.parse(body):
        for token in block.children or []:
            dest = token.attrGet("src") if token.type == "image" else token.attrGet("href") if token.type == "link_open" else ""
            if not dest:
                continue
            src = assets.register(dest, note)
            if not src or any(item["src"] == src for item in found):
                continue
            suffix = Path(src).suffix
            if suffix not in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".mp4", ".pdf"}:
                continue
            item = {"src": src, "kind": "video" if suffix == ".mp4" else "pdf" if suffix == ".pdf" else "image", "alt": token.content or "Abbildung"}
            if item["kind"] == "image":
                try:
                    with Image.open(assets.files[Path(src).name]) as image:
                        item["width"], item["height"] = image.size
                except OSError:
                    continue
            found.append(item)
    return found


def build(root: Path, out: Path, copy_media: bool = False) -> dict:
    report = collect(root)
    alias_file = root / "70_Scripts/quellen_dashboard/autoren.yaml"
    aliases = (yaml.safe_load(alias_file.read_text(encoding="utf-8")) or {}) if alias_file.is_file() else {}
    translations = TranslationCatalog(root)
    assets = Assets(root)
    image_info = local_author_images(root, report)
    author_images = {author: assets.avatar(item["path"]) for author, item in image_info.items()}
    profiles = author_profile_links(root, report, image_info)
    assignments = yaml.safe_load((root / "80_Knowledge/Themen/zuordnung.yaml").read_text(encoding="utf-8")) or {}
    wiki_topics = {name: item["haupt"] for name, item in assignments.get("muster", {}).items() if item.get("haupt") in report["topics"]}
    rows = report["rows"]["raw"]
    links = {path: hashlib.sha256(row["id"].encode()).hexdigest()[:16]
             for row in rows for path in row["paths"] + row["source_paths"]}
    entries, details = [], {}
    for row in rows:
        versions = [(root / path, *read_note(root / path)) for path in row["paths"]]
        platform = row["platforms"][0]
        translated_versions = {}
        if platform == "X":
            displayed = []
            for path, metadata, original_body in versions:
                translated_body, info = translations.apply(path, metadata, original_body)
                displayed.append((path, metadata, translated_body))
                if info:
                    translated_versions[path] = info
            versions = displayed
        # Eine Originalfassung gewinnt gegen ältere importierte deutsche Aufarbeitungen.
        versions.sort(key=lambda v: ("Sekundärquelle:" in v[2], -len(v[2])))
        note, meta, body = versions[0]
        translation = translated_versions.get(note, {})
        secondary = "Sekundärquelle:" in body
        sources = [(root / p, *read_note(root / p)) for p in row["source_paths"]]
        source_title = title_of(sources[0][2]) if sources else ""
        excerpt, excerpt_label = source_excerpt(sources[0][2]) if sources else ("", "")
        primary = section(body, "Artikel-Volltext") or section(body, "Post-Text") or section(body, "Caption") or section(body, "Inhalt") or section(body, "Volltext") or section(body, "Videobeschreibung")
        if not primary:
            primary = re.sub(r"\A# [^\n]+\n", "", body).strip() if secondary else ""
        transcript = section(body, "Transkript")
        media = media_of(body, note, assets)
        pdf = assets.register(str(meta.get("url", "")), note) if platform == "PDF" else ""
        if pdf and not any(m["src"] == pdf for m in media):
            media.insert(0, {"kind": "pdf", "src": pdf, "alt": "Original-PDF"})
        entry_id = links[row["paths"][0]]
        url = external_url(row["url"])
        video_id = str(meta.get("video_id") or "")
        if platform == "YouTube" and not re.fullmatch(r"[\w-]{11}", video_id):
            video_id = row["id"].removeprefix("youtube:") if re.fullmatch(r"youtube:[\w-]{11}", row["id"]) else ""
        if platform == "TikTok" and not re.fullmatch(r"\d+", video_id):
            video_id = row["id"].removeprefix("tiktok:") if re.fullmatch(r"tiktok:\d+", row["id"]) else ""
        start = meta.get("segment_start_sekunden", meta.get("angefragter_start_sekunden", 0))
        end = meta.get("segment_ende_sekunden", 0)
        start = int(start) if str(start).isdigit() else 0
        end = int(end) if str(end).isdigit() else 0
        display_title = source_title if platform == "X" and source_title else str(meta.get("titel") or title_of(body) or row["title"])
        for author_id in row["authors"]:
            if report["authors"].get(author_id, "").startswith("@") and meta.get("autor_name"):
                report["authors"][author_id] = str(meta["autor_name"])
        entry = {"id": entry_id, "platform": platform, "title": display_title,
                 "source_title": source_title, "show_title": platform != "X" or bool(source_title or meta.get("titel")),
                 "authors": row["authors"], "author": " · ".join(report["authors"].get(a, a) for a in row["authors"]),
                 "profile_url": external_url(profiles.get((row["authors"][0], platform), "")) if len(row["authors"]) == 1 else "",
                 "handle": str(meta.get("autor", "")) if platform in {"X", "TikTok"} else "",
                 "published": row["published"], "captured": row["captured"], "uncertain_date": row["uncertain_date"],
                 "statuses": row["statuses"], "topics": row["topics"], "main_topics": row["main_topics"], "keywords": row["keywords"],
                 "url": url, "video_id": video_id, "start": start, "end": end,
                 "segment": str(meta.get("segment_titel") or ""), "shorts": "/shorts/" in url,
                 "secondary": secondary, "has_transcript": bool(transcript), "has_source": bool(sources),
                 "translated": bool(translation), "translation_notice": translation.get("notice", ""),
                 "display_language": translation.get("language", ""),
                 "thread_posts": int(meta.get("thread_posts") or 0), "versions": len(versions), "media": media,
                 "original_label": ("Deutsche" if translation.get("language") == "de" else "Englische") + " Übersetzung des Originaltexts" if translation else "Sekundärfassung" if secondary else "Original-Caption" if platform == "TikTok" else "Videobeschreibung" if platform == "YouTube" else "Archivierter Originaltext",
                 "preview_html": render_text(primary[:1800], note, assets, links),
                 "summary_html": render_text(excerpt, sources[0][0], assets, links, wiki_topics) if sources else "",
                 "summary_label": excerpt_label,
                 "search": plain(" ".join([display_title] + [v[2] for v in versions] + [s[2] for s in sources]))}
        entries.append(entry)
        archive_html = "".join(f'<section><h2>Archivfassung {i + 1}</h2>'
                               + (f'<p class="notice">{html.escape(translated_versions[v[0]]["notice"])}</p>' if v[0] in translated_versions else "")
                               + render_text(v[2], v[0], assets, links) + '</section>' for i, v in enumerate(versions))
        source_html = "".join(render_text(s[2], s[0], assets, links, wiki_topics) for s in sources)
        transcript_info = str(meta.get("transkript_quelle") or meta.get("transkript") or "Nicht näher bezeichnet")
        transcript_lang = str(meta.get("transkript_sprache") or meta.get("sprache") or "")
        transcript_info += f" · Sprache: {transcript_lang}" if transcript_lang else ""
        details[entry_id] = {"original_html": render_text(primary, note, assets, links), "archive_html": archive_html,
                             "source_html": source_html, "transcript_html": render_text(transcript, note, assets, links),
                             "transcript_info": transcript_info,
                             "transcript_warning": "Automatisch erzeugte oder übersetzte Transkripte können vom Originalton abweichen.",
                             "thread_html": render_text(section(body, "Thread"), note, assets, links)}
    out.mkdir(parents=True, exist_ok=True)
    (out / "data").mkdir(exist_ok=True)
    (out / "media").mkdir(exist_ok=True)
    for name in ("index.html", "feed.css", "feed.js", "model.mjs", "viewer.mjs"):
        shutil.copyfile(TEMPLATES / name, out / name)
    # index.json trägt den Suchtext; Detail-HTML wird erst bei Bedarf geladen.
    taxonomy = yaml.safe_load((root / "80_Knowledge/Themen/themen.yaml").read_text(encoding="utf-8"))["cluster"]
    topic_details = {key: {"description": value.get("beschreibung", ""), "related": [other for other in value.get("verwandt", []) if other in taxonomy]} for key, value in taxonomy.items()}
    index = {"entries": entries, "authors": report["authors"], "author_images": author_images,
             "author_aliases": {alias: key for key, value in aliases.items() for alias in value.get("aliases", [])},
             "topics": report["topics"], "topic_details": topic_details,
             "counts": {"files": report["counts"]["raw_files"], "unique": len(entries)}, "missing_media": len(assets.missing)}
    (out / "index.json").write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")
    for key, value in details.items():
        (out / "data" / f"{key}.json").write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
    copied = 0
    for name, source in assets.files.items():
        destination = out / "media" / name
        if destination.exists():
            continue
        try:
            if copy_media:
                raise OSError("Kopie angefordert")
            os.link(source, destination)
        except OSError:
            shutil.copyfile(source, destination)
            copied += 1
    return {"entries": len(entries), "media": len(assets.files), "missing": sorted(assets.missing), "copied": copied,
            "translated": len(translations.translated)}


class FeedHandler(SimpleHTTPRequestHandler):
    """Statische Dateien mit Range-Unterstützung für lokale Videos bereitstellen."""

    def list_directory(self, path):
        self.send_error(404)
        return None

    def send_head(self):
        self.byte_range = None
        path = Path(self.translate_path(self.path))
        if path.is_symlink() or not path.resolve().is_relative_to(Path(self.directory).resolve()):
            self.send_error(404)
            return None
        header = self.headers.get("Range", "")
        if header and path.is_file():
            size = path.stat().st_size
            match = re.fullmatch(r"bytes=(\d*)-(\d*)", header)
            if not match or not any(match.groups()):
                self.send_error(416)
                return None
            start = int(match[1]) if match[1] else max(0, size - int(match[2]))
            end = min(size - 1, int(match[2])) if match[1] and match[2] else size - 1
            if start > end or start >= size:
                self.send_response(416)
                self.send_header("Content-Range", f"bytes */{size}")
                self.send_header("Content-Length", "0")
                self.end_headers()
                return None
            stream = path.open("rb")
            stream.seek(start)
            self.send_response(206)
            self.send_header("Content-Type", self.guess_type(str(path)))
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
            self.send_header("Content-Length", str(end - start + 1))
            self.end_headers()
            self.byte_range = end - start + 1
            return stream
        return super().send_head()

    def end_headers(self):
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def copyfile(self, source, outputfile):
        if self.byte_range is None:
            return super().copyfile(source, outputfile)
        remaining = self.byte_range
        while remaining:
            chunk = source.read(min(65536, remaining))
            if not chunk:
                break
            outputfile.write(chunk)
            remaining -= len(chunk)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build", action="store_true", help="Nur statische Website erzeugen")
    parser.add_argument("--port", type=int, default=8766)
    parser.add_argument("--ausgabe", type=Path, default=ROOT / "feed/_site")
    parser.add_argument("--kopieren", action="store_true", help="Medien kopieren statt lokale Hardlinks zu verwenden")
    parser.add_argument("--avatare-aktualisieren", action="store_true", help="Fehlende echte Profilbilder von öffentlichen Originalquellen laden")
    args = parser.parse_args(argv)
    out = args.ausgabe.resolve()
    if not 1 <= args.port <= 65535:
        parser.error("Port muss zwischen 1 und 65535 liegen")
    if out == ROOT or any(out.is_relative_to(ROOT / p) for p in ("00_Inbox", "80_Knowledge", "70_Scripts")):
        parser.error("Bitte einen eigenen Ausgabeordner verwenden")
    try:
        if args.avatare_aktualisieren:
            avatars = refresh_avatars(ROOT, collect(ROOT))
            print(f"Autorenbilder: {avatars['existing']} vorhanden, {avatars['loaded']} neu, {avatars['unavailable']} nicht abrufbar.", flush=True)
        result = build(ROOT, out, args.kopieren)
        print(f"Quellenfeed: {result['entries']} Quellen, {result['media']} Medien ({result['copied']} kopiert).", flush=True)
        if result["translated"]:
            print(f"X-Quellen mit Übersetzung: {result['translated']}", flush=True)
        if result["missing"]:
            print(f"Hinweis: {len(result['missing'])} referenzierte lokale Medien fehlen.", flush=True)
        print(f"Website: {out}", flush=True)
        if not args.build:
            from functools import partial
            with ThreadingHTTPServer(("127.0.0.1", args.port), partial(FeedHandler, directory=str(out))) as server:
                print(f"Lokal: http://127.0.0.1:{args.port}/ (Beenden: Strg+C)", flush=True)
                try:
                    server.serve_forever()
                except KeyboardInterrupt:
                    pass
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(f"Quellenfeed konnte nicht erstellt oder gestartet werden: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
