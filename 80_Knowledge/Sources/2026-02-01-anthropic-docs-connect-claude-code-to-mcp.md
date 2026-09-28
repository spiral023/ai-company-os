---
url: https://code.claude.com/docs/en/mcp
autor: Anthropic Docs
datum: 2026-02-01
erfasst: 2026-08-04
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-connect-claude-code-to-mcp.md
thema: Tools & Releases
zeitkritisch: ja
beleg_art: sekundaerquelle
---

# MCP-Anbindung in Claude Code: Transporte, Scopes und Tool Search

Deutsche Aufarbeitung (vibedeck) der Anthropic-Docs zu MCP in Claude Code, Stand Februar 2026. Herstellerdoku, aber hier nur als Zweitfassung; Befehle vor Nutzung gegen die aktuelle Doku prüfen.

## Kernaussagen
- Drei Wege: Remote HTTP (empfohlen), lokales stdio, SSE (veraltet). Auf Windows braucht `npx` den Wrapper `cmd /c`.
- Scopes: Local und User in `~/.claude.json`, Project in `.mcp.json` (wird committet, teamweit).
- Tool Search lädt Tool-Definitionen dynamisch, sobald sie mehr als 10 % des Context Window belegen würden. → [[MCP-Code-Execution-statt-Tool-Definitionen]]
- Enterprise: zentrale `managed-mcp.json` mit Allow-/Denylists. → [[Erweiterungs-Ebenen-Zuordnung]]

## Einordnung
Ohne Tool Search kosten MCP-Definitionen bei jedem Request Kontext. Ein `.mcp.json` im Repo verteilt Server ans Team, damit auch deren Vertrauensfrage.

## Verbindungen
- [[MCP-Code-Execution-statt-Tool-Definitionen]]
- [[Erweiterungs-Ebenen-Zuordnung]]
