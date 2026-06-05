"""Review local skills and print non-mutating quality hints."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "30_Skills" / "local"
LONG_SKILL_THRESHOLD = 200
SHORT_DESCRIPTION_THRESHOLD = 80
LONG_DESCRIPTION_THRESHOLD = 600
SECRET_KEYWORDS = ("api_key", "secret", "password", "token")
SECRET_VALUE_PATTERN = re.compile(
    r"(?i)\b(api_key|secret|password|token)\b\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}"
)


def find_skill_files() -> list[Path]:
    """Return all local SKILL.md files."""
    if not SKILL_ROOT.exists():
        return []
    return sorted(SKILL_ROOT.rglob("SKILL.md"))


def extract_frontmatter(text: str) -> dict[str, str] | None:
    """Extract simple YAML frontmatter fields."""
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return fields


def review_skill(skill_path: Path) -> list[str]:
    """Return review hints for one skill file."""
    text = skill_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    hints: list[str] = []

    if len(lines) > LONG_SKILL_THRESHOLD:
        hints.append(f"Länger als {LONG_SKILL_THRESHOLD} Zeilen")

    frontmatter = extract_frontmatter(text)
    if frontmatter is None:
        hints.append("Frontmatter fehlt")
    else:
        description = frontmatter.get("description", "")
        if not description:
            hints.append("Description fehlt")
        elif len(description) < SHORT_DESCRIPTION_THRESHOLD:
            hints.append("Description sehr kurz")
        elif len(description) > LONG_DESCRIPTION_THRESHOLD:
            hints.append("Description sehr lang")

    if "## Ausgabeformat" not in text:
        hints.append("Ausgabeformat fehlt")

    if "TODO" in text:
        hints.append("Enthält TODO")

    if "BEGIN PRIVATE KEY" in text:
        hints.append("Potenzieller Secret-Leak: BEGIN PRIVATE KEY")

    for line in lines:
        if SECRET_VALUE_PATTERN.search(line):
            hints.append("Potenzieller Secret-Leak: Credential-ähnlicher Wert")
            break

    lower_text = text.lower()
    if any(keyword in lower_text for keyword in SECRET_KEYWORDS) and not any(
        hint.startswith("Potenzieller Secret-Leak") for hint in hints
    ):
        pass

    return hints


def main() -> int:
    """Print a compact skill autoreview."""
    skill_files = find_skill_files()
    print("Skill Autoreview\n")

    for skill_path in skill_files:
        hints = review_skill(skill_path)
        status = "Warnung" if hints else "OK"
        print(f"Skill: {skill_path.parent.name}")
        print(f"Status: {status}")
        print("Hinweise:")
        if hints:
            for hint in hints:
                print(f"- {hint}")
        else:
            print("- Keine")
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
