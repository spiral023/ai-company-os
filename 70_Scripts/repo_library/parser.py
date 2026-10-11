"""Extract structured navigation while retaining every source section."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

from .markdown import anchor, inline, plain, render, table_cells


REPO_HEADING = re.compile(r"^## ([\w.-]+/[\w.-]+)$", re.MULTILINE)
FIELD = re.compile(r"^- \*\*([^*]+):\*\*\s*(.+)$", re.MULTILINE)
LINK = re.compile(r"\[([^\]]+)\]\(#([^)]+)\)")


def sections(markdown: str, level: int = 2) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^" + "#" * level + r" (.+)$", markdown, re.MULTILINE))
    return [(match[1], markdown[match.end():matches[i+1].start() if i+1 < len(matches) else None].strip()) for i, match in enumerate(matches)]


def rows(markdown: str) -> list[list[str]]:
    result = []
    for line in markdown.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = table_cells(line)
        if not all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            result.append(cells)
    return result


def references(value: str, repos: dict[str, dict]) -> list[str]:
    ids = []
    for label, ref in LINK.findall(value):
        if ref not in repos:
            raise ValueError(f"Repo-Verweis ohne Detailprofil: {label} (#{ref})")
        if ref not in ids:
            ids.append(ref)
    return ids


def parse_index(markdown: str) -> dict:
    repo_matches = list(REPO_HEADING.finditer(markdown))
    if not repo_matches:
        raise ValueError("Der Index enthält keine Repo-Detailprofile.")
    repo_sections = dict(sections(markdown))
    repos: dict[str, dict] = {}
    for match in repo_matches:
        label = match[1]
        identifier = anchor(label)
        if identifier in repos:
            raise ValueError(f"Doppeltes Repo oder kollidierender Anker: {label}")
        body = repo_sections[label]
        fields = [{"label": field[1], "value": plain(field[2]), "html": inline(field[2])} for field in FIELD.finditer(body)]
        values = {field["label"]: field["value"] for field in fields}
        url = values.get("URL", "")
        if not re.fullmatch(r"https://github\.com/[\w.-]+/[\w.-]+/?", url):
            raise ValueError(f"GitHub-URL fehlt oder ist ungültig: {label}")
        description = FIELD.sub("", body).strip().removesuffix("---").strip()
        star_match = re.fullmatch(r"(?:⭐\s*)?([\d.]+)", values.get("Stars", ""))
        stars = int(star_match[1].replace(".", "")) if star_match else None
        location = values.get("Ablage (abweichend)", "")
        location_match = re.search(r"(?:external_repos|external_knowledge)/[^\s—]+", location)
        local_path = location_match[0].rstrip("/") + "/" if location_match else f"external_repos/{label}/"
        repos[identifier] = {
            "id": identifier, "label": label, "owner": label.split("/", 1)[0], "name": label.split("/", 1)[1],
            "url": url, "fields": fields, "stars": stars, "downloaded": values.get("Heruntergeladen"),
            "updated": values.get("Zuletzt aktualisiert"), "localPath": local_path,
            "markdown": description, "html": render(description), "text": plain(description),
            "categories": [], "types": [], "purposes": [], "features": [], "entryPaths": [], "taskIds": [],
        }

    category_source = repo_sections.get("Repos nach Kategorie", "")
    categories = []
    for title, body in sections(category_source, 3):
        identifier = anchor(title)
        category_repos = []
        for row in rows(body)[1:]:
            if len(row) != 5:
                raise ValueError(f"Kategorietabelle hat nicht fünf Spalten: {title}")
            for repo_id in references(row[0], repos):
                repo = repos[repo_id]
                repo["categories"].append(identifier)
                repo["purposes"].append(plain(row[1]))
                repo["features"].append(plain(row[2]))
                repo["entryPaths"].append(plain(row[4]))
                repo["types"].extend(part.strip() for part in plain(row[3]).split("/"))
                category_repos.append(repo_id)
        categories.append({"id":identifier,"title":title,"repoIds":category_repos,"html":render(body)})

    tasks = []
    for row in rows(repo_sections.get("Was möchtest du tun?", ""))[1:]:
        if len(row) != 3:
            raise ValueError("Aufgabentabelle hat nicht drei Spalten.")
        identifier = "task-" + anchor(plain(row[0]))
        repo_ids = references(row[1], repos)
        task = {"id":identifier,"title":plain(row[0]),"description":plain(row[2]),"html":inline(row[2]),"repoIds":repo_ids}
        tasks.append(task)
        for repo_id in repo_ids:
            repos[repo_id]["taskIds"].append(identifier)
    if len({task["id"] for task in tasks}) != len(tasks):
        raise ValueError("Doppelte Aufgaben-Anker im Index.")

    routes = []
    for title, body in sections(repo_sections.get("Empfohlene Startpunkte", ""), 3):
        routes.append({"id":anchor(title),"title":title,"markdown":body,"html":render(body),"repoIds":references(body,repos)})

    general = [{"id":anchor(title),"title":title,"markdown":body,"html":render(body)} for title,body in sections(markdown) if not re.fullmatch(r"[\w.-]+/[\w.-]+", title)]
    introduction = markdown[:markdown.find("\n## ")] if "\n## " in markdown else markdown
    for repo in repos.values():
        for field in ["categories","types","purposes","features","entryPaths","taskIds"]:
            repo[field] = list(dict.fromkeys(repo[field]))
        first_sentence = repo["text"].split(". ", 1)[0]
        excerpt = first_sentence[:180].rstrip() + "…" if len(first_sentence) > 180 else first_sentence.rstrip(".") + "."
        repo["purpose"] = next(iter(repo["purposes"]), excerpt)
    overview = repo_sections.get("Übersicht", "")
    date_match = re.search(r"^- \*\*Stand:\*\* (.+)$", overview, re.MULTILINE)
    return {
        "schemaVersion":1,"repos":list(repos.values()),"categories":categories,"tasks":tasks,"routes":routes,
        "general":general,"introductionHtml":render(introduction),"sourceMarkdown":markdown,
        "sourceHtml":render(markdown),"sourceDigest":hashlib.sha256(markdown.encode("utf-8")).hexdigest(),
        "sourceDate":date_match[1] if date_match else None,
        "coverage":{"repos":len(repos),"tasks":len(tasks),"categories":len(categories),"routes":len(routes),"sections":len(general)},
    }
