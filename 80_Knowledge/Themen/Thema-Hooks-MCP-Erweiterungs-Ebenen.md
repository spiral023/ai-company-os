# Hooks, MCP & Erweiterungs-Ebenen

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-02. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Welche Anforderung in welche Schicht gehört (Regeldatei, Skill, Subagent, Hook, MCP, Plugin) und wie Hooks, MCP-Server und Plugins konfiguriert werden.

## Suchbegriffe

- **Hauptkeyword:** Claude Code Hooks
- **Long-Tail:** Claude Code Hooks Beispiele; MCP Server Kontextkosten; MCP Code Execution; Hook vs. Skill vs. CLAUDE.md; PreToolUse Hook; Claude Code Plugins
- **Fragen:** Wann nehme ich einen Hook statt einer Regel? / Was kosten MCP-Server im Kontext?
- **Häufig in den Quellen:** claude code hooks (6), subagents (4), progressive disclosure (4), claude code skills (3), pretooluse (3), claude.md (3), slash commands (3), context window (2), prompt-based hooks (2), model context protocol (2), mcp (2), plugins (2), skill description (2), explore plan general-purpose, claude mcp add, mcp connectors, hook matcher, agent-based hooks, .env schutz, exit-code 2

## Verwandte Themen

- [[Thema-Skill-Design]] — Skill-Design
- [[Thema-Sicherheit-Sandboxing]] — Sicherheit & Sandboxing
- [[Thema-Agent-Dateien-Memory]] — Agent-Dateien & Memory
- [[Thema-Kontext-Management]] — Kontext-Management

## Patterns (4)

- [[Action-Space-Design-nach-Modellfaehigkeit]] · mehrfach-belegt · 2 Belege
- [[Erweiterungs-Ebenen-Zuordnung]] · meinung · 18 Belege
- [[Hook-Entscheidungstyp-nach-Pruefbarkeit]] · meinung · 6 Belege
- [[MCP-Code-Execution-statt-Tool-Definitionen]] · meinung · 4 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Deny-Rules-statt-CLAUDE-md-Empfehlung]], [[Hook-erzwungene-Skill-Aktivierung]], [[Trainingsdaten-Dichte-als-Stack-Kriterium]]

## Quellen (10)

- [[2026-09-17-agenticjames-i-think-code-mode-mcps-are-probably-the-best-way-to-give-agents-access]] — Ein einzelnes Skript-Tool vor vielen MCP-Servern macht Aufrufe komposierbar und filtert große Ausgaben, bevor sie das Context Window füllen; Sandbox und Gateway-Vertrauen kosten zusätzlich.
- [[2026-08-21-promptgefluester-agent-plug-ins-das-ist-der-neue-standard-mit-dem-die-grossen-ai]] — Ein gemeinsames Plugin-Paketformat aus Manifest, Skills und MCP-Konfiguration würde Erweiterungen zwischen Coding Agents portierbar machen; der Standard ist bisher nur schwach belegt.
- [[2026-05-09-zodchiii-15-claude-code-settings-most-developers]] — Viele Qualitätsprobleme in Claude Code stammen aus schlechten Defaults und losen Permissions; Effort, Deny-Regeln, Modell-Routing und Hooks lassen sich konfigurieren.
- [[2026-04-17-wiki-compiler-skills-subagents-hooks-mcp-pragmatisch]] — Jede Anforderung gehört auf genau eine Ebene (CLAUDE.md, Skill, Subagent, Hook, MCP); Mehrfachmodellierung ist ein Designfehler, Einführung schrittweise vom knappen Kern aus.
- [[2026-02-04-affaanmustafa-shorthand-guide-primaer]] — Viele MCPs installieren, aber unter zehn aktivieren: Zu viele aktive Tools schrumpfen das effektive Kontextfenster drastisch.
- [[2026-02-01-anthropic-docs-extend-claude-code]] — Jede Erweiterungsebene hat ihren Zweck und Kontext-Preis: CLAUDE.md für immer geltende Regeln, Skills bei Bedarf, Subagents isoliert, MCP extern, Hooks kostenlos.
- [[2026-02-01-anthropic-docs-create-custom-subagents]] — Subagents mit eigenem Kontext, Tool-Rechten und Modell halten laute Exploration aus dem Hauptthread und begrenzen Rechte deterministisch.
- [[2026-02-01-anthropic-docs-connect-claude-code-to-mcp]] — MCP-Server lassen sich per HTTP oder stdio in drei Scopes einbinden; Tool Search lädt Definitionen dynamisch, damit sie den Kontext nicht füllen.
- [[2026-02-01-anthropic-docs-automate-workflows-with-hooks]] — Hooks blockieren per Exit-Code 2 deterministisch vor der Tool-Ausführung; prompt- und agentbasierte Hooks bilden eine flexiblere Stufe dazwischen.
- [[2026-01-12-eyad-khrais-claude-code-tutorial-level-2]] — Skills, Subagents und MCP ergänzen sich zu einem System, das Claude Code vom Chat-Werkzeug zum autonomen Entwicklungssystem macht.

## Quellen mit diesem Thema als Nebenthema

- [[2026-08-21-openknowledge-open-knowledge-format-plugin-for-llm-wikis-openk]]
- [[2026-04-30-zodchiii-claude-code-env-security]]
- [[2026-02-01-anthropic-docs-extend-claude-with-skills]]
- [[2026-02-01-anthropic-docs-claude-code-gitlab-ci]]
- [[2026-01-22-hooeem-claude-code-7-schritte-plan]]
- [[2026-01-21-tempoimmaterial-agent-skills-vs-rules-vs-commands]]
- [[2026-01-20-ben-tossell-agent-coding]]
