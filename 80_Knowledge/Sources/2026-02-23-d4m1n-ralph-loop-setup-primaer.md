---
url: https://x.com/d4m1n/status/2026032801322356903
autor: "Dan (@d4m1n)"
datum: 2026-02-23
erfasst: 2026-07-13
typ: tweet
---

# Dan (@d4m1n) zu „Ralph Loop: Das ultimative Setup“ (Primärquelle)

## Inhalt

Primärquelle zum Ralph Loop, das bereits über eine Sekundärsynthese (vibe-repo-Wiki) erfasst war ([[2026-04-17-wiki-compiler-ralph-loop]]). Diese Notiz ergänzt die dort fehlenden operativen Details.

Konkrete Nutzungsdaten des Autors: ein Lauf dauerte **37 Stunden am Stück** und erledigte **250 Aufgaben** aus einem 2.000-zeiligen Anforderungsdokument, während der Autor AFK war — vier Projekte wurden so erfolgreich "geshippt".

Setup-Details: Bootstrapping mit Standard-Stack (z.B. `npx @tanstack/cli@v0.59.0 create lib --add-ons shadcn,eslint,form,tanstack-query`), Playwright + Vitest zwingend installiert (ohne Tests „halluziniert“ der Agent Fortschritt). Installation via `npx @pageai/ralph-loop`, erzeugt `.agent/`-Verzeichnis mit `PROMPT.md` (Hauptanweisungen), `SUMMARY.md` (Projektzusammenfassung für Kontext), `STEERING.md` (Steuerung während des Laufs), `tasks.json`, `tasks/`, `prd/`, `logs/`. PRD-Erstellung über mitgelieferten `prd-creator`-Skill; bei Unsicherheit: „Interview me about the payment integration“ — der Agent stellt dann gezielte Rückfragen. Drittanbieter-Doku wird als Markdown im Projekt gespeichert und mit `@docs/FILE.md` referenziert, damit der Agent nicht raten muss. Review-Regel: jede generierte Aufgabenspezifikation sorgfältig lesen, da eine Korrektur der Spec viel günstiger ist als 10 schlechte Commits rückgängig zu machen.

Start: `docker sandbox run claude .` zur einmaligen Autorisierung, dann `./ralph.sh -n 2` (klein anfangen), hochskalieren auf `-n 10`, bei Vertrauen `-n 30` über Nacht. Steering während des Laufs: `.agent/STEERING.md` editieren, wird zu Beginn jeder Iteration gelesen — so lassen sich Prioritäten/kritische Bugs einspeisen, ohne den Lauf zu unterbrechen. Nachvollziehbarkeit: `.agent/logs/LOG.md`, `.agent/history/` (voller Output jeder Iteration), `git log` (jede Aufgabe ein Commit) — bei Fehlern einfach `git revert`, die zugehörigen Tests schlagen beim nächsten Lauf fehl und Ralph korrigiert erneut.

Stärken: Prototyping/MVPs, automatisierte Tests, Migrationen, repetitive Massenrefactorings. Schwächen: Pixel-perfektes Design, neuartige Architekturen ohne bestehende Muster, sicherheitskritischer Code mit ausgeschlossenen Edge-Cases.

## Kernaussagen

- Konkrete Belegzahlen für die Tragfähigkeit des Musters: 37 Stunden autonomer Lauf, 250 Aufgaben aus einem 2.000-Zeilen-PRD, AFK abgeschlossen → [[Ralph-Loop-Frischer-Kontext-pro-Iteration]]
- Der `.agent/`-Verzeichnisaufbau (PROMPT/SUMMARY/STEERING/tasks.json/prd/logs) ist die konkrete Umsetzung von „Zustand in Dateien statt im Modell“ — jede Datei hat eine klar abgegrenzte Rolle → [[Ralph-Loop-Frischer-Kontext-pro-Iteration]]
- Review der generierten Aufgabenspezifikation vor dem Lauf ist deutlich günstiger als das Zurückrollen vieler schlechter Commits danach → [[Ralph-Loop-Frischer-Kontext-pro-Iteration]], [[Fable-Unknowns-vor-Prompt-Qualitaet]]
