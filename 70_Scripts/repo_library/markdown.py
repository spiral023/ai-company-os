"""Small, escaped Markdown renderer for the index's documented syntax.

Raw HTML is displayed as text. Images become links rather than network requests.
The original Markdown is also embedded, so unsupported syntax never loses data.
"""
from __future__ import annotations

import html
import re
import unicodedata
from urllib.parse import quote, urlsplit


def anchor(value: str) -> str:
    return re.sub(r"[^\w\- ]", "", value.lower(), flags=re.UNICODE).replace(" ", "-")


def plain(value: str) -> str:
    value = re.sub(r"<!--.*?-->", "", value, flags=re.DOTALL)
    value = re.sub(r"!?\[([^\]]+)\]\(([^)]+)\)", r"\1", value)
    return re.sub(r"[`*]", "", value).strip()


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value.lower().replace("ß", "ss"))
    return "".join(char for char in value if not unicodedata.combining(char))


def safe_url(value: str) -> str:
    value = html.unescape(value.strip().strip("<>"))
    if any(ord(char) < 32 for char in value) or value.startswith("//"):
        return "#"
    try:
        scheme = urlsplit(value).scheme.lower()
    except ValueError:
        return "#"
    if scheme and scheme not in {"https", "http", "mailto"}:
        return "#"
    return quote(value, safe="/:#?=&%+@-._~")


def inline(value: str) -> str:
    value = value.replace("\x00", "\ufffd")
    value = re.sub(r"<!--.*?-->", "", value)
    tokens: list[str] = []

    def keep(markup: str) -> str:
        tokens.append(markup)
        return f"\x00{len(tokens)-1}\x00"

    value = re.sub(r"`([^`]+)`", lambda m: keep(f"<code>{html.escape(m[1])}</code>"), value)

    def link(match: re.Match[str]) -> str:
        label, destination = match[1], match[2]
        url = safe_url(destination)
        external = url.startswith(("https://", "http://"))
        attributes = ' target="_blank" rel="noopener noreferrer"' if external else ""
        label_html = html.escape(label)
        label_html = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", label_html)
        label_html = re.sub(r"\x00(\d+)\x00", lambda item: tokens[int(item[1])], label_html)
        return keep(f'<a href="{html.escape(url, quote=True)}"{attributes}>{label_html}</a>')

    value = re.sub(r"!?\[([^\]]+)\]\((<[^>]+>|[^)]+)\)", link, value)
    value = html.escape(value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", value)
    # A code span inside a link belongs to an earlier token; expand recursively.
    for _ in range(len(tokens) + 1):
        expanded = re.sub(r"\x00(\d+)\x00", lambda m: tokens[int(m[1])], value)
        if expanded == value:
            break
        value = expanded
    return value


def table_cells(line: str) -> list[str]:
    """Respect escaped pipes and pipes inside inline code."""
    return [cell.strip().replace(r"\|", "|") for cell in re.split(r"(?<!\\)\|(?=(?:[^`]*`[^`]*`)*[^`]*$)", line.strip().strip("|"))]


def render(value: str) -> str:
    lines = value.splitlines()
    result: list[str] = []
    paragraph: list[str] = []
    list_kind = ""
    index = 0

    def flush() -> None:
        if paragraph:
            result.append("<p>" + inline(" ".join(paragraph)) + "</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_kind
        if list_kind:
            result.append(f"</{list_kind}>")
            list_kind = ""

    while index < len(lines):
        line = lines[index].strip()
        index += 1
        if not line or line.startswith("<!--"):
            flush()
            close_list()
            continue
        if line.startswith("```"):
            flush()
            close_list()
            code: list[str] = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code.append(lines[index])
                index += 1
            index += 1
            result.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
            continue
        heading = re.match(r"^(#{1,6}) (.+)$", line)
        if heading:
            flush()
            close_list()
            level, title = len(heading[1]), heading[2]
            result.append(f'<h{level} id="{html.escape(anchor(title), quote=True)}">{inline(title)}</h{level}>')
            continue
        if line.startswith("|"):
            flush()
            close_list()
            rows = [table_cells(line)]
            while index < len(lines) and lines[index].strip().startswith("|"):
                row = table_cells(lines[index])
                index += 1
                if all(re.fullmatch(r":?-+:?", cell) for cell in row):
                    continue
                rows.append(row)
            result.append('<div class="table-scroll"><table><thead><tr>' + "".join(f"<th>{inline(cell)}</th>" for cell in rows[0]) + "</tr></thead><tbody>")
            for row in rows[1:]:
                result.append("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in row) + "</tr>")
            result.append("</tbody></table></div>")
            continue
        item = re.match(r"^(?:([-*]) |(\d+)\. )(.+)$", line)
        if item:
            flush()
            kind = "ul" if item[1] else "ol"
            if list_kind != kind:
                close_list()
                result.append(f"<{kind}>")
                list_kind = kind
            result.append("<li>" + inline(item[3]) + "</li>")
            continue
        close_list()
        if re.fullmatch(r"[-*_]{3,}", line):
            flush()
            result.append("<hr>")
        elif line.startswith(">"):
            flush()
            text = re.sub(r"^>\s*", "", line)
            if not re.fullmatch(r"\[![A-Z]+\]", text):
                result.append("<blockquote>" + inline(text) + "</blockquote>")
        else:
            paragraph.append(line)
    flush()
    close_list()
    return "\n".join(result)
