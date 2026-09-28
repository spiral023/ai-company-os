---
url: https://code.claude.com/docs/en/features-overview
autor: Anthropic Docs
datum: 2026-02-01
erfasst: 2026-08-04
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-extend-claude-code.md
thema: Tools & Releases
zeitkritisch: ja
beleg_art: sekundaerquelle
---

# Erweiterungsebenen in Claude Code und ihre Kontext-Kosten

Deutsche Aufarbeitung (vibedeck) der Anthropic-Übersicht zu CLAUDE.md, Skills, Subagents, MCP, Hooks und Plugins (Stand Februar 2026). Herstellerangaben, hier nur als Zweitfassung.

## Kernaussagen
- Zuordnung: CLAUDE.md für immer geltende Regeln, Skill für Wissen und Workflows bei Bedarf, Subagent für isolierte Arbeit, MCP für externe Dienste, Hook für deterministische Automation. → [[Erweiterungs-Ebenen-Zuordnung]]
- Kontext-Kosten: CLAUDE.md und MCP-Definitionen bei jedem Request, Skills nur als Beschreibung bis zur Nutzung, Hooks null. Richtwert: CLAUDE.md unter ca. 500 Zeilen. → [[AGENTS-md-Onboarding-Design]]
- Kombinationen: Skill erklärt, wie MCP-Tools zu nutzen sind; Skill kann Subagents starten. → [[Skill-Call-Hierarchie]]

## Einordnung
Deckt sich mit dem Bestand; der Mehrwert liegt in der Kostentabelle und dem Ladeverhalten (Hooks mergen, Skills überschreiben nach Name).

## Verbindungen
- [[Erweiterungs-Ebenen-Zuordnung]]
- [[Skill-Call-Hierarchie]]
- [[2026-04-17-wiki-compiler-skills-subagents-hooks-mcp-pragmatisch]]
