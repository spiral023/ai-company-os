---
url: https://www.youtube.com/watch?v=g0vqT_wZtXA
autor: Matt Pocock (AI Engineer Paris 2026)
datum: 2026-09-24
erfasst: 2026-09-27
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# PR-Engpass lösen: Checks, Review-Agent mit Commits, risikobasiertes Human Review

Pocock argumentiert, dass mehr Agent-Output den Review-Flaschenhals verschärft. Gegenmittel sind drei Bremsen: deterministische Checks, automatisiertes Review, dann Human Review. Praxisbericht eines Einzelnen, keine Messdaten.

## Kernaussagen
- Grüne Checks können lügen (tautologische Tests, Tests gegen Quelltext-Reihenfolge, wegmockende Tests); tiefe Module mit kleinen Interfaces erschweren das → [[Testharness-als-staerkster-Hebel]]
- Coding Standards nicht in den Implement-Agent oder `AGENTS.md`, sondern in `coding-standards.md` für einen separaten Review-Subagent, der Fixes committet statt zu kommentieren → [[Plan-first-mit-getrenntem-Review]]
- One-Way- vs. Two-Way-Door plus Blast Radius bestimmen Review-Tiefe; `/retro` überführt Review-Funde in Checks und Standards.

## Einordnung
Der Zwei-Kontext-Split (Implement, dann Refactor/Review) entspricht Red-Green-Refactor über getrennte Context Windows. Kosten: zusätzliche Review-Tokens pro PR.

## Verbindungen
- [[TDD-als-Verifikationshebel]]
- [[AGENTS-md-Onboarding-Design]]
- [[2026-07-06-mattpocock-writing-great-skills-beyond-skills]]
