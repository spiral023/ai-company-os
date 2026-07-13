---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-17
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Ralph Loop für langlaufende AI Coding Agents“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/02-agent-guides-und-templates/wka-ralph-loop-fuer-langlaufende-ai-coding-agents-2026-04-17.md`), Zusammenfassung eines X-Posts (@d4m1n).

Kernpunkte (kondensiert):

- Ralph Loop ist ein Betriebsmodus für lange autonome Läufe: jede Iteration startet mit frischem Kontext, der Arbeitszustand liegt in Dateien und Git-Commits, Fortschritt wird über Aufgabenlisten und Tests abgesichert. Gedächtnis wird damit aus dem Modell ins Dateisystem/Git verlagert.
- Typischer Zyklus: nächste priorisierte Aufgabe wählen → Spezifikation lesen → Änderung implementieren → Tests ausführen → committen → nächste Iteration mit frischem Kontext.
- Operativer Speicher liegt in einem `.agent/`-Verzeichnis: `PROMPT.md`, `SUMMARY.md`, `STEERING.md`, `tasks.json`, `tasks/`, `prd/`, `logs/`.
- Voraussetzungen: brauchbarer Projekt-Scaffold, realistische Verifikationspfade (idealerweise Playwright/Vitest), klares PRD, Secrets nur in `.env`. Ohne Tests halluziniert der Agent Fortschritt statt ihn zu belegen.
- Steering über Dateiänderungen (v.a. `STEERING.md`) statt Unterbrechen — Prioritäten können verschoben werden, ohne den Lauf abzubrechen.
- Stark bei: viele kleine bis mittlere Aufgaben mit klarer Prüfbarkeit, testgetriebene Arbeit, Boilerplate/Migrationen, MVP-Bau mit vielen Tasks. Schwach bei: pixelgenaue UI-Arbeit, neuartige Architekturentscheidungen, hochsicherheitskritischer Code, viel implizites Fachurteil.
- Operative Empfehlung: Mensch plant/schärft die Aufgaben, Loop führt mechanisch aus, Mensch reviewt Commits und korrigiert die Spezifikation.

## Kernaussagen

- Fortschritt bei langen autonomen Läufen liegt in Dateien/Git statt im Modellkontext; jede Iteration startet mit frischem Kontext gegen Kontextsättigung und Qualitätsdegradation → [[Ralph-Loop-Frischer-Kontext-pro-Iteration]]
- Ohne echte Tests/Verifikationspfade halluziniert der Loop Fortschritt statt ihn zu belegen → [[Ralph-Loop-Frischer-Kontext-pro-Iteration]]
- Steering über eine Datei (`STEERING.md`) statt Unterbrechen erlaubt Prioritätsänderungen ohne Abbruch des Laufs → [[Ralph-Loop-Frischer-Kontext-pro-Iteration]]
