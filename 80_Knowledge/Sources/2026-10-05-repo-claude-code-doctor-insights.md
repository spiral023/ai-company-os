---
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
autor: anthropics
datum: 2026-10-05
erfasst: 2026-10-05
typ: repo
thema: Tools & Releases
zeitkritisch: ja
---

# Claude Code: `/doctor`, `/skill-doctor` und `/insights` als eingebaute Diagnose

Aus `CHANGELOG.md` von anthropics/claude-code (Stand 2.1.289). Gelesen, nichts ausgeführt.

## Kernaussagen
- Seit 2.1.205 ist `/doctor` (Alias `/checkup`) ein vollständiger Setup-Check, der Probleme diagnostizieren und beheben kann. Er meldet u.a. fehlerhafte Plugins, Hooks, MCP-Konfigurationen und Sandbox-Reste.
- Seit 2.1.206 schlägt `/doctor` vor, eingecheckte `CLAUDE.md`-Dateien zu kürzen, indem er Inhalte streicht, die Claude aus dem Code ableiten kann.
- Seit 2.1.283 prüft `/doctor prompt-audit` `CLAUDE.md`, Skills, Agents und Commands auf Prompt-Muster, die für ältere Modelle geschrieben wurden.
- Seit 2.1.261 zeigt `/skill-doctor`, welche geladenen Skills ungenutzt bleiben und wie viel Kontext sie kosten.
- Seit 2.1.281 schätzt `/insights` zusätzlich, wie viele Berechtigungsabfragen der Auto Mode in den letzten Sessions hätte übernehmen können.

## Einordnung
Die eingebauten Befehle prüfen Einrichtung, Kontextkosten und Nutzungsmuster. Keiner davon fragt, welcher konkrete Fehler einer Session sich mit einem Check hätte verhindern lassen.

## Verbindungen
- [[AGENTS-md-Onboarding-Design]]
- [[2026-02-09-tom-crawshaw-claude-code-insights-guide]]
- [[2026-09-04-julian-ivanov-ki-automat-so-nutzt-du-claude-code-nach-anthropics-neuen-re]]
- [[2026-10-02-repo-anthropics-claude-code]]
