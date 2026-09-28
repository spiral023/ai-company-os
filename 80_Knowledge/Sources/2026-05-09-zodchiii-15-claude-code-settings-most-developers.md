---
url: https://x.com/zodchiii/status/2053042131111927976
autor: darkzodchi (@zodchiii)
datum: 2026-05-09
erfasst: 2026-08-04
typ: tweet
rohquelle: 00_Inbox/Quellen/X/2026-05-09-zodchiii-15-claude-code-settings-most-developers.md
thema: Tools & Releases
zeitkritisch: ja
beleg_art: sekundaerquelle
---

# 15 selten genutzte Claude-Code-Einstellungen als Checkliste

Deutsche Aufarbeitung (vibedeck) eines X-Posts: Qualitätsprobleme seien oft schlechte Defaults, lockere Permissions und fehlende Automation statt Modellschwäche. Alle Empfehlungen sind Autorenmeinung ohne Messwerte; Settings-Namen und Flags mit Stand Mai 2026 vor Nutzung gegen die Docs prüfen.

## Kernaussagen
- Reasoning fixieren (`/effort high`, `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1`): teurer pro Turn, laut Autor billiger pro gelöstem Problem. → [[Modell-Eskalation-von-guenstig-nach-teuer]]
- Permissions mit expliziten Allow-/Deny-Regeln (`.env`, `.ssh`, `rm -rf`, `git push` gesperrt). → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- Modelle nach Task routen, Fan-Out auf feste Subagent-Zahl begrenzen, `--max-budget-usd` bei Headless-Runs. → [[Kontrollierte-Agent-Parallelisierung]]
- Hooks für Formatierung und Log-Vorfilterung; MCP-Server regelmäßig mit `/mcp` ausmisten. → [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]

## Einordnung
Kein neues Konzept, sondern Bestätigung bekannter Muster als Konfigurationsliste. Hochsetzen von Effort erhöht Kosten und Latenz; `acceptEdits` senkt Reibung, aber auch die Kontrolle.

## Verbindungen
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
- [[2026-04-30-zodchiii-claude-code-env-security]]
