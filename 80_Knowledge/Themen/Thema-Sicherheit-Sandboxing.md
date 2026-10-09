# Sicherheit & Sandboxing

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-09. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Technisch erzwungene Grenzen statt Empfehlungen: Deny-Regeln, Sandboxes, Secrets, Permissions, Plugin-Vertrauen, Sicherheit bei Vibe-Coding-Apps. Berichte über Gefahren, Missbrauch und konkrete KI-Vorfälle stehen in ki-risiken.

## Suchbegriffe

- **Hauptkeyword:** Claude Code Sicherheit
- **Long-Tail:** Deny Rules statt CLAUDE.md; .env Secrets Claude Code schützen; Agent Sandbox einrichten; Docker Sandbox Claude Code; Codex Execpolicy; Vibe Coding Sicherheit
- **Fragen:** Wie verhindere ich, dass der Agent meine .env liest? / Reicht eine Regel in CLAUDE.md?
- **Häufig in den Quellen:** row level security (3), os-level sandboxing (3), security checker (2), docker sandboxes (2), command smuggling (2), agent sandbox (2), security (2), playwright (2), sicherheit (2), sandbox (2), prompt injection (2), process isolation (2), sandbox permissions (2), mxc (2), vibe coding security (2), agent-identität (2), agent-to-agent-kommunikation (2), least agency (2), risikobasiertes human review (2), menschliche freigabe (2)

## Verwandte Themen

- [[Thema-Hooks-MCP-Erweiterungs-Ebenen]] — Hooks, MCP & Erweiterungs-Ebenen
- [[Thema-Autonome-Läufe-Loops-CI]] — Autonome Läufe, Loops & CI
- [[Thema-Prototyping-UI-Design]] — Prototyping & UI-Design
- [[Thema-AI-nativer-SDLC]] — AI-nativer SDLC
- [[Thema-KI-Risiken-Sicherheitsvorfälle]] — KI-Risiken & Sicherheitsvorfälle

## Patterns (5)

- [[Adversarialer-Pre-Launch-Check]] · meinung · 4 Belege
- [[Agent-Rechte-umfassen-Kommunikationswege]] · meinung · 1 Belege
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]] · mehrfach-belegt · 13 Belege
- [[Freigaben-und-Isolation-getrennt-steuern]] · meinung · 1 Belege
- [[Sandbox-Komposition-aus-OS-Primitiven]] · meinung · 5 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[CI-Agent-mit-Review-Gate]], [[Hook-Entscheidungstyp-nach-Pruefbarkeit]], [[Metrikband-gestufte-Agent-Autonomie]], [[Review-Autonomie-mit-Shadow-Mode-und-Stichproben]]

## Quellen (10)

- [[2026-10-08-unslothai-windows-sandboxing-mxc]] — Unsloth kündigt eine Integration von Microsoft eXecution Container (`MXC`) für die Ausführung von Code unter Windows an.
- [[2026-09-29-suraj_sharma14-2104790775397830755]] — Suraj Sharma listet 30 knappe Sicherheitsmaßnahmen für KI-generierte Apps.
- [[2026-09-29-openclaw-openclaw-enterprise-the-open-agent-platform-open]] — Herstellerankündigung der OpenClaw Foundation: Open-Source-Control-Plane für persistente Agenten in sensiblen Umgebungen, vor 1.0, nutzbar für interne Piloten.
- [[2026-09-27-voxyz_ai-2104224555040452925]] — Vox beschreibt einen Pre-Launch-Check für Claude Code (Modellname im Tweet: Opus 5.5): Vier Subagents haben nur die Aufgabe, die eigene App zu brechen, und teilen sich 16 feste Prüffragen.
- [[2026-08-18-docker-2089789519788728379]] — MicroVM-Isolation mit eigenem Kernel pro Sandbox gilt laut Docker inzwischen als empfohlener Standardpfad für Claude Code, ist aber nur als Herstellermeldung belegt.
- [[2026-05-13-david-wiesen-openai-codex-windows-sandbox]] — Kein einzelnes OS-Feature reichte für eine Agent-Sandbox; sie wurde aus mehreren Primitiven komponiert, und rein advisory Netzwerkschutz genügt nicht.
- [[2026-04-30-zodchiii-claude-code-env-security]] — Nur Deny-Regeln in settings.json erzwingen Zugriffssperren, CLAUDE.md-Hinweise sind Empfehlungen; Secrets lecken auch über Runtime-Output und Grep-Treffer.
- [[2026-02-28-openai-codex-rules-guide]] — Eine Grenze wirkt nur, wenn eine Regel-Engine sie vor der Ausführung erzwingt; Codex Rules zerlegen verpackte Shell-Aufrufe, um Command Smuggling zu verhindern.
- [[2026-02-05-d4m1n-docker-sandboxes]] — Docker Sandboxes isolieren Agent-CLIs per Micro-VM und machen YOLO-Modus und nächtliche Ralph-Loop-Läufe sicher, ohne den Host zu gefährden.
- [[2026-02-04-lovable-docs-lovable-security-guide]] — Secrets und Autorisierung gehören ins Backend, Row Level Security früh setzen; die Verantwortung für Sicherheit bleibt beim Builder, nicht beim Tool.

## Quellen mit diesem Thema als Nebenthema

- [[2026-10-02-repo-thedaviddias-front-end-checklist]]
- [[2026-09-27-anthropic-academy-sdlc-playbook]]
- [[2026-09-18-akshay_pachaar-2101037514945597645]]
- [[2026-07-21-claude-how-anthropic-secures-its-ai-native-software-dev]]
- [[2026-07-16-amasad-2077802290304684404]]
- [[2026-04-17-wiki-compiler-lovable-design-debugging-sicherheit]]
- [[2026-04-16-wiki-compiler-superpowers]]
- [[2026-02-28-openai-codex-multi-agents-guide]]
