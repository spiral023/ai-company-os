---
url: https://www.youtube.com/watch?v=91hD4U4e-Jc
autor: "Alex Sprogis"
datum: 2026-04-13
erfasst: 2026-10-11
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-04-13-alex-sprogis-superkraefte-fuer-claude-code.md
thema: Arbeitsweisen
zeitkritisch: ja
---

# Superpowers: Tests aus Akzeptanzkriterien und getrennte Prüfrollen

Der Praxistest vom 13. April 2026 beschreibt Superpowers als TDD-Workflow. Wertvoll sind klare Prüfschritte; der demonstrierte Ablauf zeigt zugleich reale Ausfälle.

## Kernaussagen

- Zuerst Spezifikation und Akzeptanzkriterien, dann fehlschlagender Test, minimale Implementierung und Refactoring: [[TDD-als-Verifikationshebel]].
- Häufige Begründungen zum Überspringen von Tests ausdrücklich mit Gegenargumenten behandeln: [[Anti-Rationalization-Tables]].
- Pro Aufgabe Implementierung, Spezifikationsprüfung und Codequalitätsprüfung sequenziell durchführen; abschließend die Gesamtänderung prüfen: [[Kontrollierte-Agent-Parallelisierung]].

## Einordnung

Die Demo überspringt die Worktree-Phase, stockt bei der Planung und setzt mit einem vorbereiteten Projekt fort; außerdem werden zunächst nicht existierende API-Endpunkte implementiert. Promptregeln sind keine technisch erzwungene Sperre, und grüne Tests bestätigen nur die erfassten Anforderungen. Framework- und Installationshinweise gelten für April 2026.

## Verbindungen

- [[TDD-als-Verifikationshebel]] koppelt Änderungen an überprüfbares Verhalten.
- [[Anti-Rationalization-Tables]] macht typische Ausweichargumente explizit.
