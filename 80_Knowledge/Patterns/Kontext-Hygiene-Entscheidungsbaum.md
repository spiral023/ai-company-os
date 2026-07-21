# Kontext-Hygiene-Entscheidungsbaum

**Konfidenz:** mehrfach-belegt

## Zweck

Verhindert, dass lange Agent-Sessions durch anwachsenden, veralteten oder irrelevanten Kontext („Context Rot“/„Context Pollution“) an Präzision verlieren, und dass Tokenverbrauch durch reflexhaftes Weiterreden im selben Thread unnötig quadratisch wächst statt linear mit dem tatsächlichen Arbeitsaufwand.

## Funktionsweise

Nach jedem abgeschlossenen Arbeitsblock wird bewusst zwischen fünf Optionen entschieden, statt reflexhaft im selben Thread weiterzumachen (`Continue`, die riskante Default-Reaktion): **`Continue`**, wenn dieselbe Aufgabe weiterläuft und der Detailkontext noch nützlich ist; **`rewind`**, wenn ein falscher Lösungsweg eingeschlagen wurde — ein Rücksprung ist sauberer als eine nachgeschobene Korrektur, weil Korrekturen den Fehlversuch im Kontext belassen; **`/compact`**, wenn derselbe Problemraum bleibt, aber das Kontextgewicht reduziert werden muss (nur mit explizitem Fokus, was erhalten bleiben soll — sonst gehen wichtige Nebenaspekte verloren); **`/clear`**, wenn eine neue Phase oder Aufgabe eine saubere, bewusst formulierte Rahmung braucht; **Subagent/neue Session**, wenn viel Zwischenoutput entsteht, aber später nur die Schlussfolgerung gebraucht wird. Faustregel: eine neue Aufgabe bedeutet meistens eine neue Session. Der Tokenverbrauch einer Konversation wächst näherungsweise quadratisch mit der Nachrichtenzahl (`S · N(N+1)/2`), weil jede neue Antwort den gesamten bisherigen Verlauf mitverarbeitet — auch bei sehr großen Context-Windows (Heuristik: ab ca. 300k-400k Tokens wird Context Rot spürbar, keine harte Grenze).

## Vorteile

- Macht die Entscheidung „wie geht es weiter“ explizit statt sie dem Default `Continue` zu überlassen, der Fehlversuche und Rauschen im Kontext anhäuft.
- `rewind` vor `/compact` vor `/clear` als gestufte Eskalation passt die Intervention an die tatsächliche Kontextverschmutzung an, statt immer die stärkste (oder immer keine) Maßnahme zu wählen.
- Reduziert sowohl Tokenkosten als auch das Risiko, dass alte Hypothesen und Fehlversuche spätere Antworten verzerren.

## Nachteile & Grenzen

- `/compact` bleibt grundsätzlich verlustbehaftet — das Modell entscheidet, was wichtig war, und kann dabei später relevante Nebenaspekte verwerfen, besonders wenn die künftige Richtung noch nicht absehbar ist.
- Die 300k-400k-Token-Heuristik und die genaue quadratische Kostenformel sind aus zeitgebundenen Sekundärquellen und plattformabhängig — sie sollten gegen aktuelle Anbieter-Dokumentation und eigene Workloads geprüft werden, bevor sie als feste Regel gilt.
- Erfordert bei jedem Turn eine bewusste Zusatzentscheidung, was bei sehr kurzen, einfachen Aufgaben unnötigen Overhead erzeugt.

## Wann einsetzen, wann nicht

- Einsetzen: längere Agent-Sessions, Debugging mit mehreren Fehlversuchen, Phasenwechsel zwischen Analyse/Umsetzung/Review, jede Session die erkennbar in Richtung Kontextüberladung läuft.
- Nicht einsetzen: kurze, in wenigen Turns abgeschlossene Aufgaben ohne Fehlversuche — dort lohnt sich die explizite Entscheidung pro Turn nicht.

## Belege

- 2026-04-29 · [[2026-04-29-wiki-compiler-claude-code-session-management-1m-context]] · meinung — Wiki-Artikel (Quelle: X-Artikel von @trq212, 15.04.2026) beschreibt die Fünf-Optionen-Entscheidung, die Context-Rot-Heuristik und `rewind`-vor-Korrektur.
- 2026-04-29 · [[2026-04-29-wiki-compiler-claude-usage-limits-token-strategien]] · meinung — Unabhängige Quelle (X-Thread von @0x_kaize, 29.03.2026) bestätigt das quadratische Tokenkosten-Modell und ergänzt zehn konkrete Strategien (u.a. Modellwahl nach Aufgabenschwere, Chat nach 15-20 Nachrichten kritisch prüfen).
- 2026-05-04 · [[2026-05-04-wiki-compiler-claude-session-und-token-management]] · meinung — Synthese-Artikel verdichtet beide Quellen zu einem gemeinsamen Sieben-Schritte-Arbeitsmuster und einer Entscheidungscheckliste vor jedem Prompt.
- 2026-04-15 · [[2026-04-15-trq212-claude-code-session-management-1m-context-primaer]] · meinung — Primärquelle ergänzt die Beobachtung, dass schlechte Compacts gerade dann entstehen, wenn der automatische Trigger erst bei bereits vollem Kontext greift (Modell fasst nicht im besten Zustand zusammen) — Konsequenz: früh und aktiv statt automatisch kompaktieren.
- 2026-03-29 · [[2026-03-29-0x-kaize-claude-usage-limits-primaer]] · meinung — Primärquelle liefert die exakte Zahlentabelle (Nachricht 30 kostet 31× mehr als Nachricht 1, bis 98,5% Wiedereinlese-Anteil) und die rollende 5-Stunden-Fenster-/Peak-Hours-Mechanik.
- 2026-05-01 · [[2026-05-01-mnilax-claude-code-overhead-9-patterns]] · meinung — 90-Tage-API-Audit (430h, 6 Mio. Tokens) zeigt, dass nur 27% der Tokens produktiv waren; ergänzt Cache-Lebensdauer/Resume-Miss als eigenständigen Kostenfaktor neben reiner History-Länge, mit konkretem Audit-Script.
- 2026-01-20 · [[2026-01-20-mrexodia-vibe-engineering]] · meinung — Unabhängige Quelle bestätigt „Context Window als knappste Ressource“ (unter 50-75% Kapazität bleiben) mit dem Commodore-64-Mentalmodell als zusätzlicher Heuristik.
- 2026-02-27 · [[2026-02-27-thariq-lessons-building-claude-code]] · meinung — Ergänzt Progressive Disclosure beim Kontextaufbau selbst (Datei verweist auf Datei statt alles upfront zu laden) als konkrete Umsetzung von Kontext-Sparsamkeit.
- 2026-05-27 · external_knowledge/ai-llm-wiki/raw/drowning-in-context.md (G. Vetukuri, towardsai.net) · meinung — Unabhängige Bestätigung von Context Rot als „Self-Generated Noise" (Agent begräbt sein eigenes Ziel unter Tool-Outputs) und „Lost in the Middle"; ergänzt drei Architektur-Mitigationen: Intent-Pickers, Structured Handoff Packets (Checkpoints statt Roh-History), Resume Contracts.
- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/context-compaction-tip-009.md (M. Contieri, hackernoon.com) · meinung — Unabhängige Bestätigung der Kernregeln: oft neu starten statt stundenlanger Threads, State-Summary vor Session-Ende erzwingen, Stack-Traces auf ~5 relevante Zeilen trimmen statt 200-Zeilen-Dumps, kleine injizierbare `context.md` pflegen. Fazit dort: „You are the curator of the AI's memory."

## Spannungen & offene Fragen

- Mehrere unabhängige Autoren (@trq212, @0x_kaize, Mnimiy, mrexodia, Thariq) konvergieren auf dieselbe Kernaussage „Kontext ist die knappste Ressource, mehr Fenster löst das Problem nicht“ — bei ausschließlich sekundärer Beschaffung über vibedeck/vibe-repo, nicht von uns unabhängig gegen die Original-Posts nachgeprüft.
- Offene Frage: Wie genau lässt sich dieser Entscheidungsbaum mit [[Handoff-Doc]] kombinieren — wann reicht `/compact` mit Fokusangabe, und wann braucht es stattdessen ein explizites Handoff-Dokument vor `/clear`? (Vetukuri 2026-05-27 stützt die Handoff-Seite: „Structured Handoff Packets" statt Roh-History als Architekturprinzip.)

## Verwandte Patterns

- [[Handoff-Doc]]
- [[Plan-first-mit-getrenntem-Review]]
- [[Ralph-Loop-Frischer-Kontext-pro-Iteration]]
