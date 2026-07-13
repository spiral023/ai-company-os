---
url: https://x.com/Mnilax/status/2050261839653556522
autor: "Mnimiy (@Mnilax)"
datum: 2026-05-01
erfasst: 2026-07-13
typ: tweet
---

# Mnimiy (@Mnilax) zu „73% Overhead in Claude Code: 9 Patterns, die Tokens verbrennen“

## Inhalt

90-Tage-Audit mit HTTP-Proxy vor der Anthropic-API: 430 Stunden Nutzung, 6 Mio. Input-Tokens, 1.340 USD Kosten. Zentraler Befund: **nur 27% der Tokens waren produktiv, 73% gingen in neun unsichtbare Overhead-Muster** — nicht in Modellwahl, sondern in Kontext-Bloat, Session-Architektur, Hook-Injection und dauerhaft mitgeladenes Tooling.

Die neun Muster: (1) Zu große `CLAUDE.md` (Beispiel: 4.800 Tokens, bei jedem Turn neu geladen — Ziel: kombiniert unter 1.200 Wörter/~1.500 Tokens; Audit per `wc -w`); (2) lange Chats = teures Wiedereinlesen der History (Fix: frühere Nachricht editieren statt nachschieben, bei ~20 Nachrichten hart kappen, `/compact` statt `/clear` wenn Kontinuität nötig); (3) `UserPromptSubmit`-Hooks mehrerer Plugins summieren sich zu „Prompt-Wänden“ (Audit via `jq '.hooks.UserPromptSubmit'`, `/plugin disable`); (4) kurze Prompt-Cache-Lebensdauer erzeugt teure Resume-Misses nach Pausen (Fix: kleiner Ping vor Pausen, längere Cache-Pläne); (5) zu viele Skills werden „just in case“ konservativ geladen (Audit: `grep skill_invoked` in Logs, ungenutzte deaktivieren); (6) zu viele MCP-Server blasen jede Anfrage mit Tool-Schemas auf, unabhängig vom Bedarf (`/mcp disable`); (7) Extended Thinking als globaler Default statt gezielt pro Nachricht; (8) schlechte Antworten zu lange auslaufen lassen statt früh abzubrechen („Stupid Tax“); (9) `SessionStart`-Hooks und Plugin-Noise, die bei jeder Session wieder auftauchen.

Explizite Abgrenzung von Standardratschlägen: billigeres Modell hilft nur begrenzt; aggressives `/clear` nach jeder Aufgabe ist oft kontraproduktiv; alle Skills pauschal abschalten führt dazu, dass dieselben Instruktionen manuell in Prompts wandern; Off-Peak-Nutzung ist real, aber ein kleinerer Hebel als Kontext-Overhead. Kernaussage: „Produktive Tokens sind nicht der Standardzustand, sondern der Restbetrag nach allen Basiskosten.“ Enthält ein fertiges Audit-Script (`claude-audit.sh`), das alle neun Muster an einer Stelle prüft, mit konkreten Zielwerten (CLAUDE.md < 1.200 Wörter, 3-5 aktive Plugins, 3-5 aktive Skills, 3 always-on MCPs).

## Kernaussagen

- Ein 90-Tage-Audit zeigt konkret: nur 27% der Claude-Code-Tokens sind produktiv, 73% verteilen sich auf neun strukturelle Overhead-Muster (CLAUDE.md-Größe, History-Re-Read, Hook-Injection, Cache-Misses, ungenutzte Skills/MCPs, Extended Thinking, spätes Abbrechen, Session-Noise) → [[Kontext-Hygiene-Entscheidungsbaum]]
- `UserPromptSubmit`-Hooks sind nicht neutral: sie sind wiederkehrender Kontext bei jedem einzelnen Prompt und damit wiederkehrende Kosten, auch wenn jeder einzelne Hook klein wirkt → [[Erweiterungs-Ebenen-Zuordnung]]
- Prompt-Cache hat eine kurze Lebensdauer — nach einer Pause wird System Prompt/CLAUDE.md/Tool-Schema wieder voll bepreist statt als Cache-Read; ein kleiner Ping vor der Pause hält den Cache warm → [[Kontext-Hygiene-Entscheidungsbaum]]
- Explizite Gegenposition zu Standardratschlägen: billigeres Modell und aggressives `/clear` sind kleinere Hebel als schlankere Session-Architektur (CLAUDE.md-Größe, Hooks, Skills, MCP-Auswahl) → [[Kontext-Hygiene-Entscheidungsbaum]]
