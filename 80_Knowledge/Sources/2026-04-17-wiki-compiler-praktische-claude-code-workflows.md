---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-17
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Praktische Claude-Code-Workflows für Planung, Ausführung und Review“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/02-agent-guides-und-templates/wka-praktische-claude-code-workflows-2026-04-17.md`), synthetisiert aus mehreren X-Posts und offizieller Claude-Code-Doku (`best-practices`, `common-workflows`).

Kernpunkte (kondensiert):

- Robuster Default-Workflow für mittelgroße bis große Änderungen: (1) Discovery nur lesend, (2) Plan als Artefakt festhalten (betroffene Dateien, Risiken, offene Fragen, Prüfschritte), (3) Plan iterativ schärfen (Nutzer annotiert), (4) Umsetzung gegen Checkliste, (5) Review getrennt von der Erstellung (zweite Session, Subagent oder expliziter Schritt).
- Ein persistentes Plan-Dokument (`plan.md`/`research.md`) hat mehr Wert als ein nur im Chat formulierter Plan: Annahmen bleiben sichtbar, Korrekturen sind zeilenweise annotierbar, neue Sessions/Reviewer können an einem stabilen Zwischenstand ansetzen.
- Rollentrennung gegen Single-Model-Blindheit: Builder (schreibt Plan/Code), Reviewer (prüft Architektur/Edge-Cases/Sicherheit/Testlücken), Verifier (validiert nur Nachweise/Regressionen). Bei hoher Tragweite: adversarialer Review-Loop, bei dem ein zweiter Agent den Plan zurückweist, bis offene Punkte weg sind.
- Parallelisierung nur mit klaren Grenzen: nach Modulen/Dateien parallelisieren, nicht über gemeinsam editierte Kernartefakte.
- Session-Hygiene als Teil des Workflows: früh stoppen bei falscher Richtung, `/clear` bei Themenwechsel, Checkpoints/Rewind aktiv nutzen statt schlechte Zwischenstände mitzuschleppen.
- Produktive Artefakte am Ende: Ziel-/Scope-Plan, Liste geänderter Dateien/PR, Verifikationsnachweis, offene Restrisiken.

## Kernaussagen

- Robuster Fünf-Schritte-Workflow (lesende Discovery → Plan als Artefakt → iteratives Schärfen → Umsetzung gegen Checkliste → getrenntes Review) → [[Plan-first-mit-getrenntem-Review]]
- Rollentrennung Builder/Reviewer/Verifier gegen Single-Model-Blindheit, adversarialer Review-Loop bei hoher Tragweite → [[Plan-first-mit-getrenntem-Review]]
- Parallelisierung nur entlang Modul-/Dateigrenzen, nie über gemeinsam editierte Kernartefakte → [[Kontrollierte-Agent-Parallelisierung]]
