---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-17
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Best Practices für Frontend-Rapid-Prototyping mit Lovable“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/03-tool-profile/02-design-und-ui-tools/wka-lovable-frontend-rapid-prototyping-2026-04-17.md`).

Kernpunkte (kondensiert; RAITEC-spezifische Preise/Workshop-Referenzen ausgelassen):

- Lovable ist stark für den schnellen Start eines Webapp-Prototyps, aber nicht der beste Ort für den langen Mittelteil oder stabilen Endausbau. Sinnvolle Reihenfolge: Idee/Scope/UX in Lovable verdichten → klickbaren Prototyp im Standardstack erzeugen → früh in ein lokales Repo wechseln → dort mit einem Coding Agent (Architektur, Tests, APIs, Deployment) weiterentwickeln.
- Empfohlener Zielstack für den Export: React, Vite, TypeScript, shadcn/ui, Tailwind CSS.
- Vor dem ersten Prompt klären: Problem, Nutzer, 2-4 Hauptabläufe im MVP, Nicht-Ziele, Datenobjekte, Aktionen, Screens, Fehlerfälle.
- Mock-first statt Backend-first: nur synthetische Beispieldaten, keine echten sensiblen Daten/Secrets im Prototyp; später ersetzt das Team Mock-Daten schrittweise durch echte APIs.
- Der erste Prompt ist ein Produktbriefing (durchaus 2000-4000 Wörter), keine Kurzanweisung: Rolle, Produktziel, Nutzergruppen, Hauptabläufe, UI-Struktur, Datenmodell, Beispielschemas, Screens, Status-/Fehlerfälle, Design-Richtung, technische Zielsetzung, MVP-Abgrenzung, klare Verbote.
- Was nicht in Lovable hängen bleiben sollte: echte API-Integration, Auth, Rollen/Rechte, persistente Datenhaltung, Deployment, Testabdeckung, Security-Härtung, feinere Git-Historie.
- Handoff-Checkliste vor Export: Hauptscreen vorhanden, 1-3 Kernflows klickbar, Mock-Daten sichtbar, keine sensiblen Daten im Projekt.

## Kernaussagen

- Lovable ist der Prototyp-Bereich, lokale Coding Agents sind das Hauptwerkzeug für die weitere Umsetzung — mit definierter Handoff-Checkliste für den Übergang → [[Lovable-Prototyp-dann-lokaler-Handoff]]
- Der erste Prompt sollte ein vollständiges Produktbriefing sein (Problem, Nutzer, Flows, Datenmodell, Nicht-Ziele), nicht eine Kurzanweisung → [[Lovable-Prototyp-dann-lokaler-Handoff]]
- Mock-first statt Backend-first: synthetische Daten im Prototyp, echte APIs erst nach dem Export → [[Lovable-Prototyp-dann-lokaler-Handoff]]
