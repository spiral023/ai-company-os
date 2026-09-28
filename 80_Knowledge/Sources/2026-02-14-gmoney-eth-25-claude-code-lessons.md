---
url: https://x.com/gmoneyNFT/status/2022454519741767800
autor: gmoney.eth
datum: 2026-02-14
erfasst: 2026-08-04
typ: tweet
rohquelle: 00_Inbox/Quellen/X/2026-02-14-gmoney-eth-25-claude-code-lessons.md
thema: Arbeitsweisen
zeitkritisch: nein
beleg_art: sekundaerquelle
---

# 25 Praxis-Lektionen zu Claude Code: Kontext, Subagents, parallele Sessions

Deutsche Aufarbeitung (vibedeck, Sekundärquelle) eines Erfahrungs-Threads nach monatelanger Nutzung. Selbstberichtet, ohne Messwerte; vieles ist bekanntes Standardwissen.

## Kernaussagen
- Context Window wie RAM behandeln: `/clear`, frischer Kontext pro Iteration; Subagents halten den Hauptkontext sauber → [[Kontext-Hygiene-Entscheidungsbaum]]
- 3 bis 5 parallele Sessions, je in eigenem Git-Worktree → [[Kontrollierte-Agent-Parallelisierung]]
- Bei misslungenem Ergebnis neu ansetzen statt patchen; nach Korrektur bricht man ab und plant neu → [[Plan-first-mit-getrenntem-Review]]
- Regel „nie simulierte Daten verwenden“; Rollen trennen in `AGENTS.md`, `TOOLS.md`, `USER.md`

## Einordnung
Die „SOUL.md“-Persönlichkeitsdatei und Heartbeats sind unbelegte Einzelpraxis. Parallelisierung kostet Tokens und Review-Aufwand, was der Thread nur streift.

## Verbindungen
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Kontrollierte-Agent-Parallelisierung]]
- [[2026-01-31-bcherny-claude-code-team-tips]]
