---
url: https://tweag.github.io/agentic-coding-handbook/WORKFLOW_TDD/
autor: Tweag
datum: 2026-02-04
erfasst: 2026-08-04
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-04-tweag-tdd-agentic-coding.md
thema: Arbeitsweisen
zeitkritisch: nein
beleg_art: sekundaerquelle
---

# TDD im Agentic Coding: Tests als kleinteilige Spezifikation

Sekundärquelle: deutsche vibedeck-Aufarbeitung des Tweag Agentic Coding Handbook. Die These: Ein Test ist ein präziser Prompt, der den Agenten auf ein kleines, prüfbares Verhalten fokussiert. Statt alles auf einmal zu generieren, baut der Agent Logik Test für Test. Besonders geeignet für regelreiche Logik wie Pricing-Engines oder Validatoren. Belegt wird das nur durch ein Beispiel (Rechnungssumme mit Steuer- und Rabattregeln), nicht durch Messung.

## Kernaussagen
- Zuerst das wichtigste Verhalten, dann Edge Cases; ein Verhalten pro Prompt → [[TDD-als-Verifikationshebel]]
- Ein Agent kann aus Geschäftsregeln eine Markdown-Checkliste (`tdd-plan.md`) mit abwechselnd Test- und Implementierungsschritten erzeugen → [[Task-basierte-Steuerung]]
- Refactoring nur bei grünen Tests; Pre-Commit-Hooks führen Tests aus.

## Einordnung
Deckt sich mit dem Bestand; die Behauptung „weniger Halluzinationen“ ist plausibel, aber unbelegt. Kosten: Die Testqualität liegt bei Dir, denn der Agent kann Tests passend zur Implementierung schreiben.

## Verbindungen
- [[TDD-als-Verifikationshebel]]
- [[Testharness-als-staerkster-Hebel]]
- [[2026-02-14-matt-pocock-skill-tdd-claude-code]]
