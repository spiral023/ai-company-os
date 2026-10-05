---
url: https://github.com/bmad-code-org/BMAD-METHOD/tree/main/skills/bmad-retrospective
autor: bmad-code-org
datum: 2026-10-05
erfasst: 2026-10-05
typ: repo
thema: Arbeitsweisen
zeitkritisch: nein
---

# BMAD `bmad-retrospective`: Epic-Retro mit Quellenpflicht und Abnahmeentscheidung

Im Klon von bmad-code-org/BMAD-METHOD (Stand Commit `8f2c13d`) liegt `skills/bmad-retrospective/` mit `workflow.md` und fünf Referenzdateien. Der Skill setzt ein eingerichtetes BMad-Projekt voraus (`_bmad/`, Aufruf über `uv run`). Gelesen, nichts ausgeführt.

## Kernaussagen
- Gegenstand ist ein abgeschlossenes Epic: Epic-Datei, Ticket-Pläne, Diffs und Commits zwischen den Plan-Ständen, Session-Logs falls vorhanden.
- Jeder Befund braucht eine Quellenangabe (Datei, Zeile, Commit oder Log). Eine Ursache, auf die man nicht zeigen kann, wird gestrichen.
- Jeder Befund bekommt zwei Einordnungen: was mit diesem Fall passiert (sofort beheben, später, akzeptieren) und was den nächsten verhindert (Spec-Formulierung, Story-Zuschnitt, fehlende Konvention oder Prüfung).
- Ergebnis sind Aktionspunkte mit Verantwortlichem und eine Abnahmeentscheidung, ob das Epic seine eigenen Kriterien erfüllt. Code-Fixes und Spec-Anpassungen werden nur vorgeschlagen, nie automatisch angewendet.
- Die Aktionspunkte der vorigen Retro werden geprüft, ob sie umgesetzt wurden. Ein Headless-Modus (`-H`) läuft ohne Rückfragen für Orchestrierung.

## Einordnung
Gründlichste der verglichenen Retro-Varianten, aber an das BMad-Ticketsystem gebunden. Die Prüfung der vorigen Aktionspunkte adressiert, dass Retro-Ergebnisse sonst versanden.

## Verbindungen
- [[Spec-Ordner-pro-Feature]]
- [[Plan-first-mit-getrenntem-Review]]
