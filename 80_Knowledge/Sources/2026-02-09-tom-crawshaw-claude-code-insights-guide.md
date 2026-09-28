---
url: https://x.com/tomcrawshaw01/status/2020866308230009189
autor: Tom Crawshaw
datum: 2026-02-09
erfasst: 2026-08-04
typ: tweet
rohquelle: 00_Inbox/Quellen/X/2026-02-09-tom-crawshaw-claude-code-insights-guide.md
thema: Tools & Releases
zeitkritisch: nein
beleg_art: sekundaerquelle
---

# `/insights` als Feedback-Schleife für den eigenen Claude-Code-Workflow

Sekundärquelle: deutsche vibedeck-Aufarbeitung eines Threads von Tom Crawshaw. Der Befehl `/insights` analysierte laut ihm 2.555 Nachrichten aus 318 Sessions der letzten 30 Tage und lieferte einen Diagnosebericht. Alle Zahlen sind Selbstberichte eines einzelnen Nutzers und wurden nicht am Original geprüft.

## Kernaussagen
- Gefundene Reibung: mehrdeutige Projektverweise, 91 % von 90 Sessions nur „größtenteils erreicht“ wegen unklarer Definition von „Done“, über 7.700 Bash-Befehle (etwa 4x mehr als Dateiedits) durch Exploration ohne Startkontext → [[AGENTS-md-Onboarding-Design]]
- Vorgeschlagene Fixes: wenige Zeilen Kontext in `CLAUDE.md`, häufige Abläufe als Slash Commands, ein MCP-Server für API-Zugriff.
- Vorgeschlagen wird auch ein Agent, der Skills mit generierten Testszenarien iterativ verbessert → [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]

## Einordnung
Nutzungsdaten auszuwerten ist ein sinnvoller Hebel, die Diagnose bleibt aber Modellinterpretation. Selbstoptimierende Skills sind ein Vorschlag, kein gezeigtes Ergebnis.

## Verbindungen
- [[AGENTS-md-Onboarding-Design]]
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- [[2026-01-31-bcherny-claude-code-team-tips]]
