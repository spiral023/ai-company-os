# Sicherheit & Sandboxing

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-09-30. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Technisch erzwungene Grenzen statt Empfehlungen: Deny-Regeln, Sandboxes, Secrets, Permissions, Plugin-Vertrauen, Sicherheit bei Vibe-Coding-Apps.

## Suchbegriffe

- **Hauptkeyword:** Claude Code Sicherheit
- **Long-Tail:** Deny Rules statt CLAUDE.md; .env Secrets Claude Code schützen; Agent Sandbox einrichten; Docker Sandbox Claude Code; Codex Execpolicy; Vibe Coding Sicherheit
- **Fragen:** Wie verhindere ich, dass der Agent meine .env liest? / Reicht eine Regel in CLAUDE.md?
- **Häufig in den Quellen:** security checker (2), docker sandboxes (2), command smuggling (2), agent sandbox (2), ki-generierte apps absichern, secrets im frontend, lovable security, row level security, vibe coding sicherheit, supabase edge functions, agent-isolation, yolo-modus, micro-vm, ralph loop über nacht, claude code dangerously-skip-permissions, docker sandbox run claude, codex rules, starlark, prefix_rule, codex execpolicy

## Verwandte Themen

- [[Thema-Hooks-MCP-Erweiterungs-Ebenen]] — Hooks, MCP & Erweiterungs-Ebenen
- [[Thema-Autonome-Läufe-Loops-CI]] — Autonome Läufe, Loops & CI
- [[Thema-Prototyping-UI-Design]] — Prototyping & UI-Design

## Patterns (2)

- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]] · mehrfach-belegt · 12 Belege
- [[Sandbox-Komposition-aus-OS-Primitiven]] · meinung · 2 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[CI-Agent-mit-Review-Gate]], [[Hook-Entscheidungstyp-nach-Pruefbarkeit]], [[Metrikband-gestufte-Agent-Autonomie]]

## Quellen (6)

- [[2026-08-18-docker-2089789519788728379]] — MicroVM-Isolation mit eigenem Kernel pro Sandbox gilt laut Docker inzwischen als empfohlener Standardpfad für Claude Code, ist aber nur als Herstellermeldung belegt.
- [[2026-05-13-david-wiesen-openai-codex-windows-sandbox]] — Kein einzelnes OS-Feature reichte für eine Agent-Sandbox; sie wurde aus mehreren Primitiven komponiert, und rein advisory Netzwerkschutz genügt nicht.
- [[2026-04-30-zodchiii-claude-code-env-security]] — Nur Deny-Regeln in settings.json erzwingen Zugriffssperren, CLAUDE.md-Hinweise sind Empfehlungen; Secrets lecken auch über Runtime-Output und Grep-Treffer.
- [[2026-02-28-openai-codex-rules-guide]] — Eine Grenze wirkt nur, wenn eine Regel-Engine sie vor der Ausführung erzwingt; Codex Rules zerlegen verpackte Shell-Aufrufe, um Command Smuggling zu verhindern.
- [[2026-02-05-d4m1n-docker-sandboxes]] — Docker Sandboxes isolieren Agent-CLIs per Micro-VM und machen YOLO-Modus und nächtliche Ralph-Loop-Läufe sicher, ohne den Host zu gefährden.
- [[2026-02-04-lovable-docs-lovable-security-guide]] — Secrets und Autorisierung gehören ins Backend, Row Level Security früh setzen; die Verantwortung für Sicherheit bleibt beim Builder, nicht beim Tool.

## Quellen mit diesem Thema als Nebenthema

- [[2026-09-27-anthropic-academy-sdlc-playbook]]
- [[2026-09-18-akshay_pachaar-2101037514945597645]]
- [[2026-04-17-wiki-compiler-lovable-design-debugging-sicherheit]]
- [[2026-04-16-wiki-compiler-superpowers]]
- [[2026-02-28-openai-codex-multi-agents-guide]]
