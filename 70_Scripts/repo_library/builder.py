"""Compose modular sources into one deterministic, self-contained HTML file."""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

from .parser import parse_index


MODULE_ROOT = Path(__file__).resolve().parent
SCRIPT_MODULES = ("search.js", "state.js", "views.js", "app.js")


def render_library(index_path: Path, output_path: Path) -> tuple[str, dict]:
    data = parse_index(index_path.read_text(encoding="utf-8-sig"))
    config = json.loads((MODULE_ROOT / "discovery.json").read_text(encoding="utf-8"))
    data["discovery"] = config
    data["libraryRoot"] = os.path.relpath(index_path.parent.parent, output_path.parent).replace("\\", "/")
    encoded = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    templates = MODULE_ROOT / "templates"
    result = (templates / "index.html").read_text(encoding="utf-8")
    replacements = {
        "{{STYLES}}": (templates / "library.css").read_text(encoding="utf-8"),
        "{{DATA}}": encoded,
        "{{SCRIPTS}}": "\n".join((templates / name).read_text(encoding="utf-8") for name in SCRIPT_MODULES),
        "{{NOSCRIPT}}": data["sourceHtml"],
    }
    for token in replacements:
        if result.count(token) != 1:
            raise ValueError(f"Vorlage benötigt genau einen Platzhalter {token}.")
    result = re.sub(r"\{\{(?:STYLES|DATA|SCRIPTS|NOSCRIPT)\}\}", lambda match: replacements[match[0]], result)
    return result, data["coverage"]


def build_library(index_path: Path, output_path: Path, *, check: bool = False) -> dict:
    result, coverage = render_library(index_path, output_path)
    if check:
        if not output_path.exists() or output_path.read_text(encoding="utf-8") != result:
            raise ValueError("HTML fehlt oder ist veraltet. Aktualisieren: python ai.py repos build")
    else:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        temporary = output_path.with_suffix(output_path.suffix + ".tmp")
        temporary.write_text(result, encoding="utf-8", newline="\n")
        temporary.replace(output_path)
    return coverage
