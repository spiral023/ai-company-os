---
url: https://claude.dev/blog/getting-the-most-out-of-opus-5-5/
autor: Addy Osmani
datum: 2026-09-22
erfasst: 2026-09-27
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-09-22-claude-getting-the-most-out-of-opus-5-5-in-claude-and-c.md
thema: Arbeitsweisen
zeitkritisch: ja
---

# Opus 5.5 führen: Zielzustand, Stopp-Regeln und Task-Datei für lange Läufe

Nutzungsleitfaden zu Opus 5.5 (Stand 2026-09-22, Herstellerblog). Kernaussage: Das Modell arbeitet länger autonom, denkt vor jeder Antwort selbst und meldet klar, was es getan hat. Die Empfehlungen sind Herstellerangaben aus eigenen Tests und Tester-Berichten, ohne veröffentlichte Messwerte.

## Kernaussagen
- Definiere „done“ in einer Nachricht (z. B. Tests grün, alter Client gelöscht) und nenne die einzige Stopp-Bedingung; „think carefully“-Zeilen streichen → [[Freiheitsgrad-nach-Aufgaben-Fragilitaet]]
- Stopp-Regeln in `CLAUDE.md`: weitermachen, wenn keine Eingabe nötig ist; nur vor Destruktivem (Löschen, Force-Push, Änderungen außerhalb des Repos) fragen; Permission Prompts bleiben an → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- Große Audits/Migrationen pro Einheit an ein Subagent geben, Belege prüfen, Ergebnis als Tabelle; Task-Liste in `TASKS.md` statt im Scrollback → [[Kontrollierte-Agent-Parallelisierung]], [[Task-basierte-Steuerung]]

## Einordnung
Die Task-Datei überlebt die Kontext-Zusammenfassung; das ist die belastbarste Empfehlung. „Weniger Stopps“ erhöht das Risiko und braucht Gates. Aussagen zu Bugfunden (niedrigster Effort schlägt Opus 5 bei hohem) sind ein einzelner Tester.

## Verbindungen
- [[Kontrollierte-Agent-Parallelisierung]]
- [[Task-basierte-Steuerung]]
- [[2026-07-03-trq212-2073100352921215386]]
