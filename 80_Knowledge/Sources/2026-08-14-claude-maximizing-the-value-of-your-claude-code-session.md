---
url: https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions
autor: Lydia Hallie (Claude Blog)
datum: 2026-08-14
erfasst: 2026-09-14
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-08-14-claude-maximizing-the-value-of-your-claude-code-session.md
thema: KI-Kosten
zeitkritisch: ja
---

# Token-Kosten in Claude Code: Prompt Cache, Kontextgröße und Sitzungsdisziplin

Anthropic erklärt, was den Preis einer Claude-Code-Sitzung bestimmt: Modell, Input vs. Output (Output laut Quelle etwa 5x teurer) und Prompt Cache (Lesen `0.1x`, Schreiben bis `2x`; Stand 2026-08-14). Herstellerangaben, mechanisch nachvollziehbar, aber ohne Messreihen.

## Kernaussagen
- Jeder Tool-Output bleibt in jedem Folgeturn im Kontext; darum `/clear` zwischen Aufgaben, Dateien per @-Mention, laute Befehle mit Quiet-Flags oder im Subagent → [[Kontext-Hygiene-Entscheidungsbaum]]
- `/model`, `/effort`, Fast Mode und `/compact` entwerten den Cache; Wechsel nur am Sitzungsanfang oder nach `/clear`. Cache läuft nach einer Stunde (Subscription) bzw. fünf Minuten (API-Key) ab.
- Subagents mit `model: haiku` oder `sonnet` für wiederkehrende laute Jobs → [[Modell-Eskalation-von-guenstig-nach-teuer]]

## Einordnung
Belastbare Kostenmechanik für Abo und API. Grenze: Ein Subagent liest bereits bekannte Inhalte neu ein und ist bei kleinen Jobs reiner Overhead.

## Verbindungen
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[2026-04-15-trq212-claude-code-session-management-1m-context-primaer]]
- [[2026-04-29-wiki-compiler-claude-usage-limits-token-strategien]]
