---
url: https://code.claude.com/docs/en/how-claude-code-works
autor: Anthropic Docs
datum: 2026-02-01
erfasst: 2026-08-04
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-how-claude-code-works.md
thema: Tools & Releases
zeitkritisch: nein
beleg_art: sekundaerquelle
---

# Claude Code im Überblick: Agentic Loop, Sessions und Rechte

Deutsche Aufarbeitung (vibedeck, Sekundärquelle) der offiziellen Doku; Stand der Doku 2026-02, Details zu Befehlen können sich geändert haben. Beschreibt den Loop Kontext sammeln, handeln, Ergebnis prüfen.

## Kernaussagen
- Tools machen aus dem Modell einen Agenten; Skills und MCP-Tools verbrauchen Context, sichtbar über `/context`. → [[Kontext-Hygiene-Entscheidungsbaum]]
- Sessions sind ephemer; `--continue`, `--resume`, `--fork-session` und Checkpoints (`/rewind`) steuern Fortsetzung und Rückgriff.
- Permission-Modi (Default, Auto-Accept, Plan Mode) begrenzen Schreibrechte; Verifikation über Tests oder Screenshots ist der empfohlene Hebel. → [[Plan-first-mit-getrenntem-Review]]

## Einordnung
Grundlagentext, nützlich als Referenz, ohne neue Arbeitsweise. Der Verifikationsschritt im Loop stützt den Bestand zu Tests als Hebel.

## Verbindungen
- [[Testharness-als-staerkster-Hebel]]
- [[2026-02-01-anthropic-docs-claude-code-best-practices]]
