"""Verifizierte Autorenbilder wiederverwenden und optional öffentlich abrufen.

Der normale Feed-Build bleibt offline. Neue Bilder werden nur mit
--avatare-aktualisieren geladen; niemals Video-Cover als Profilbild verwenden.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from io import BytesIO
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit, quote
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

from PIL import Image, ImageOps
import yaml


def author_cache(root: Path, cache: dict) -> dict:
    """Verifizierte Bilder/Profil-Links auch nach einer Alias-Zusammenführung nutzen."""
    file = root / "70_Scripts/quellen_dashboard/autoren.yaml"
    aliases = (yaml.safe_load(file.read_text(encoding="utf-8")) or {}) if file.is_file() else {}
    result = dict(cache)
    for author, entry in aliases.items():
        if author not in result:
            previous = next((cache[a] for a in entry.get("aliases", []) if a in cache), None)
            if previous:
                result[author] = previous
    return result


def normalized(value: str) -> str:
    return re.sub(r"[^\w]", "", str(value).casefold())


def profile_identity(url: str) -> str:
    parts = urlsplit(url)
    host = (parts.hostname or "").removeprefix("www.").casefold()
    if host in {"x.com", "twitter.com"}:
        return "x:" + parts.path.strip("/").split("/")[0].casefold()
    if host in {"tiktok.com", "youtube.com"} and parts.path.startswith("/@"):
        return host.split(".")[0] + ":" + parts.path.split("/")[1][1:].casefold()
    return ""


def read_json(path: Path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def profile_url(platform: str, source_url: str, known: str = "") -> str:
    """Profil statt Post verlinken; YouTube-Kanäle nur aus verifizierten Metadaten."""
    parts = urlsplit(source_url)
    host = (parts.hostname or "").removeprefix("www.").casefold()
    if parts.scheme not in {"https", "http"} or parts.username:
        return ""
    if platform == "X" and host in {"x.com", "twitter.com", "mobile.twitter.com"}:
        handle = parts.path.strip("/").split("/")[0]
        if re.fullmatch(r"[A-Za-z0-9_]+", handle) and handle.casefold() not in {"i", "intent", "home", "search"}:
            return "https://x.com/" + handle
    if platform == "TikTok" and host in {"tiktok.com", "m.tiktok.com"}:
        match = re.match(r"/@([A-Za-z0-9_.]+)(?:/|$)", parts.path)
        if match:
            return "https://www.tiktok.com/@" + match[1]
    if known:
        target = urlsplit(known)
        if target.scheme not in {"https", "http"} or target.username:
            return ""
        if platform == "YouTube":
            if (target.hostname or "").removeprefix("www.") not in {"youtube.com", "m.youtube.com"} or not re.match(r"^/(?:@[^/]+|(?:channel|user|c)/[^/]+)(?:/|$)", target.path):
                return ""
        return known
    return ""


def author_profile_links(root: Path, report: dict, images: dict | None = None) -> dict:
    images = images if images is not None else local_author_images(root, report)
    site = root / "docs/ki-quellen"
    research = read_json(site / "image-research.json", {})
    profiles = read_json(site / "profiles.json", {}).get("profiles", [])
    curated = {}
    for item in profiles:
        channel = research.get(item["id"], {}).get("channelUrl", "")
        if channel:
            for name in [item["id"], item["name"], *item.get("sourceHeadings", [])]:
                curated[normalized(name)] = channel
    cached = author_cache(root, read_json(root / "feed/avatars/manifest.json", {}).get("profile_links", {}))
    result = {}
    for row in report["rows"]["raw"]:
        if len(row["authors"]) != 1:
            continue
        author, platform = row["authors"][0], row["platforms"][0]
        known = cached.get(author, {}).get("url") if platform == "YouTube" else ""
        if not known and platform == "YouTube":
            known = curated.get(normalized(author)) or curated.get(normalized(report["authors"].get(author, "")))
        if not known:
            known = images.get(author, {}).get("source", "")
        link = profile_url(platform, row["url"], known or "")
        if link:
            result[(author, platform)] = link
    return result


def refresh_profile_links(root: Path, report: dict) -> int:
    """Fehlende YouTube-Kanallinks aus den öffentlichen Video-Metadaten erfassen."""
    known = author_profile_links(root, report)
    path = root / "feed/avatars/manifest.json"
    manifest = read_json(path, {"authors": {}})
    added = 0
    checked = set()
    for row in report["rows"]["raw"]:
        if row["platforms"] != ["YouTube"] or len(row["authors"]) != 1:
            continue
        author = row["authors"][0]
        if (author, "YouTube") in known or author in checked:
            continue
        checked.add(author)
        try:
            if urlsplit(row["url"]).hostname not in {"youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be"}:
                continue
            data = json.loads(fetch("https://www.youtube.com/oembed?format=json&url=" + quote(row["url"], safe="")))
            expected = [report["authors"].get(author, ""), *row["author_original"]]
            if normalized(data.get("author_name", "")) not in {normalized(name) for name in expected}:
                continue
            link = profile_url("YouTube", row["url"], data.get("author_url", ""))
            if link:
                manifest.setdefault("profile_links", {})[author] = {"url": link, "source": row["url"], "checked_at": datetime.now(ZoneInfo("Europe/Vienna")).date().isoformat()}
                added += 1
        except (ValueError, OSError):
            continue
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return added


def local_author_images(root: Path, report: dict) -> dict[str, dict]:
    """Exakte kuratierte Identitäten; keine unscharfen Namens-Zusammenführungen."""
    site = root / "docs/ki-quellen"
    profiles = read_json(site / "profiles.json", {}).get("profiles", [])
    research = read_json(site / "image-research.json", {})
    guide = root / "80_Knowledge/Guides/AI-Coding-Agents-Social-Media-Uebersicht.md"
    headings = {}
    if guide.exists():
        for line in guide.read_text(encoding="utf-8").splitlines():
            if line.startswith("### "):
                title = re.split(r" — \[", line[4:])[0]
                headings[title] = re.findall(r"\[[^]]+\]\((https?://[^)]+)\)", line)
    by_id, by_name, by_profile = {}, {}, {}
    for profile in profiles:
        asset = research.get(profile["id"], {})
        if not asset.get("image"):
            continue
        path = (site / asset["image"]).resolve()
        if not path.is_relative_to((site / "images").resolve()) or not path.is_file():
            continue
        item = {"path": path, "source": asset.get("imageSource", "")}
        by_id[profile["id"]] = item
        for name in [profile["name"], *profile.get("sourceHeadings", [])]:
            by_name[normalized(name)] = item
        urls = [asset.get("imageSource", ""), asset.get("channelUrl", "")]
        for heading in profile.get("sourceHeadings", []):
            urls.extend(headings.get(heading, []))
        for url in urls:
            if identity := profile_identity(url):
                by_profile[identity] = item
    cache_root = root / "feed/avatars"
    cached = author_cache(root, read_json(cache_root / "manifest.json", {}).get("authors", {}))
    result = {}
    for row in report["rows"]["raw"]:
        for author in row["authors"]:
            name_match = by_name.get(normalized(report["authors"].get(author, ""))) if row["platforms"][0] in {"YouTube", "URL"} else None
            item = by_id.get(author) or by_profile.get(profile_identity(row["url"])) or name_match
            previous = cached.get(author, {})
            if previous.get("image"):
                path = (cache_root / previous["image"]).resolve()
                if path.is_relative_to((cache_root / "images").resolve()) and path.is_file():
                    item = {"path": path, "source": previous.get("source", "")}
            if item:
                result[author] = item
    return result


def fetch(url: str, limit: int = 5_000_000) -> bytes:
    request = Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.9"})
    with urlopen(request, timeout=15) as response:
        data = response.read(limit + 1)
    if len(data) > limit:
        raise ValueError("Antwort ist größer als das Abruflimit")
    return data


def avatar_from_page(platform: str, url: str, expected: str) -> tuple[str, str]:
    """Nur explizite Profilbildfelder der tatsächlichen Post-Autoren lesen."""
    parts = urlsplit(url)
    allowed = {"X": {"x.com", "www.x.com", "twitter.com", "www.twitter.com", "mobile.twitter.com"},
               "YouTube": {"youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be"},
               "TikTok": {"tiktok.com", "www.tiktok.com", "m.tiktok.com"}}
    if parts.scheme != "https" or parts.username or parts.hostname not in allowed.get(platform, set()):
        raise ValueError("Keine öffentliche Originalquelle der Plattform")
    if platform == "X":
        match = re.search(r"/status/(\d+)", urlsplit(url).path)
        if not match:
            raise ValueError("Post-ID fehlt")
        payload = json.loads(fetch(f"https://cdn.syndication.twimg.com/tweet-result?id={match[1]}&lang=en&token=0"))
        user = payload.get("user", {})
        handle = urlsplit(url).path.strip("/").split("/")[0]
        if str(user.get("screen_name", "")).casefold() != handle.casefold():
            raise ValueError("Post-Autor stimmt nicht mit dem Profil überein")
        return user.get("profile_image_url_https", ""), f"https://x.com/{handle}"
    if platform == "YouTube":
        text = fetch(url).decode("utf-8", "replace")
        match = re.search(r'"videoOwnerRenderer"\s*:\s*', text)
        owner = json.JSONDecoder().raw_decode(text[match.end():])[0] if match else {}
        runs = owner.get("title", {}).get("runs", [])
        name = "".join(run.get("text", "") for run in runs)
        if normalized(name) != normalized(expected):
            raise ValueError("Videokanal stimmt nicht mit dem archivierten Autor überein")
        thumbs = owner.get("thumbnail", {}).get("thumbnails", [])
        source = "https://www.youtube.com" + runs[0].get("navigationEndpoint", {}).get("browseEndpoint", {}).get("canonicalBaseUrl", "")
        return max(thumbs, key=lambda t: t.get("width", 0)).get("url", "") if thumbs else "", source
    if platform == "TikTok":
        handle = urlsplit(url).path.split("/")[1]
        source = "https://www.tiktok.com/" + handle
        text = fetch(source).decode("utf-8", "replace")
        match = re.search(r'<script[^>]+id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>', text, re.S)
        payload = json.loads(match[1]) if match else {}
        user = payload.get("__DEFAULT_SCOPE__", {}).get("webapp.user-detail", {}).get("userInfo", {}).get("user", {})
        if str(user.get("uniqueId", "")).casefold() != handle[1:].casefold():
            raise ValueError("TikTok-Profil konnte nicht zugeordnet werden")
        return user.get("avatarMedium") or user.get("avatarLarger") or user.get("avatarThumb") or "", source
    raise ValueError("Keine unterstützte Profilquelle")


def download_avatar(url: str, platform: str) -> bytes:
    parts = urlsplit(url)
    host = parts.hostname or ""
    allowed = {"X": ("pbs.twimg.com",), "YouTube": ("yt3.ggpht.com", "yt3.googleusercontent.com"),
               "TikTok": ("tiktokcdn.com", "tiktokcdn-eu.com", "tiktokcdn-us.com")}[platform]
    if parts.scheme != "https" or parts.username or not any(host == domain or host.endswith("." + domain) for domain in allowed):
        raise ValueError("Unerwartete Profilbild-Domain")
    data = fetch(url, limit=3_000_000)
    with Image.open(BytesIO(data)) as original:
        if original.width > 4096 or original.height > 4096:
            raise ValueError("Profilbild zu groß")
        image = ImageOps.fit(ImageOps.exif_transpose(original).convert("RGB"), (128, 128), method=Image.Resampling.LANCZOS)
        output = BytesIO()
        image.save(output, format="JPEG", quality=88)
        return output.getvalue()


def refresh_avatars(root: Path, report: dict) -> dict:
    """Fehlende soziale Profilbilder abrufen, mit Herkunft lokal zwischenspeichern."""
    known = local_author_images(root, report)
    folder = root / "feed/avatars"
    (folder / "images").mkdir(parents=True, exist_ok=True)
    manifest = read_json(folder / "manifest.json", {"authors": {}})
    jobs = {}
    for row in sorted(report["rows"]["raw"], key=lambda r: r["published"], reverse=True):
        if len(row["authors"]) != 1 or row["platforms"][0] not in {"X", "TikTok", "YouTube"}:
            continue
        author = row["authors"][0]
        if author not in known and author not in jobs:
            jobs[author] = row
    checked = datetime.now(ZoneInfo("Europe/Vienna")).date().isoformat()

    def load(author, row):
        platform = row["platforms"][0]
        expected = row["author_original"][0] if row["author_original"] else report["authors"][author]
        image_url, source = avatar_from_page(platform, row["url"], expected)
        if not image_url:
            raise ValueError("Kein öffentliches Profilbild gefunden")
        data = download_avatar(image_url, platform)
        relative = "images/" + hashlib.sha256(author.encode()).hexdigest()[:20] + ".jpg"
        (folder / relative).write_bytes(data)
        return {"image": relative, "source": source, "image_url": image_url, "checked_at": checked, "verified_via": row["url"]}

    loaded, failures = 0, []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(load, author, row): author for author, row in jobs.items()}
        for count, future in enumerate(as_completed(futures), 1):
            author = futures[future]
            try:
                manifest["authors"][author] = future.result()
                loaded += 1
            except Exception as error:
                failures.append({"author": author, "reason": str(error)[:180]})
            if count % 10 == 0 or count == len(jobs):
                print(f"Autorenbilder: {count}/{len(jobs)} geprüft, {loaded} neue Bilder.", flush=True)
    manifest["last_checked"] = checked
    manifest["unavailable"] = failures
    temp = folder / "manifest.json.tmp"
    temp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(folder / "manifest.json")
    refresh_profile_links(root, report)
    return {"existing": len(known), "loaded": loaded, "unavailable": len(failures)}
