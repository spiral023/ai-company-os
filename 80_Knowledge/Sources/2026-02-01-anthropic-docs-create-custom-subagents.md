---
url: https://code.claude.com/docs/en/sub-agents
autor: Anthropic Docs
datum: 2026-02-01
erfasst: 2026-08-04
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-create-custom-subagents.md
thema: Tools & Releases
zeitkritisch: ja
beleg_art: sekundaerquelle
---

# Claude-Code-Subagents: Konfiguration, Tool-Rechte und Modellwahl

Deutsche Aufarbeitung (vibedeck, Sekundärquelle) der offiziellen Subagent-Doku, Stand Februar 2026. Subagents laufen im eigenen Context Window mit eigenem Systemprompt, Tool-Allowlist und Permission Mode; als Markdown-Datei mit Frontmatter (`name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `skills`, `hooks`) unter `.claude/agents/` oder `~/.claude/agents/`. Herstellerdoku, Details können veraltet sein.

## Kernaussagen
- Zweck: Exploration und laute Outputs aus dem Haupt-Thread halten, Rechte begrenzen, leichte Tasks an `haiku` delegieren; der eingebaute Explore-Agent ist read-only auf Haiku. → [[Modell-Eskalation-von-guenstig-nach-teuer]]
- Delegation läuft über das `description`-Feld; Subagents erben keine Skills, sondern bekommen sie per `skills:` injiziert. → [[Kontext-Hygiene-Entscheidungsbaum]]
- Tool-Rechte lassen sich per Allowlist, Denylist und Hooks im Frontmatter deterministisch begrenzen. → [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]

## Einordnung
Belastbare Referenz für Mechanik, aber keine Aussage zu Wirksamkeit oder Kosten; `bypassPermissions` wird selbst als riskant markiert. Über die Sekundärquelle nicht am Original geprüft.

## Verbindungen
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[2026-04-17-wiki-compiler-skills-subagents-hooks-mcp-pragmatisch]]
