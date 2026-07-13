---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-17
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Agent Teams in Claude Code“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/02-agent-guides-und-templates/wka-agent-teams-in-claude-code-2026-04-17.md`), Zusammenfassung zweier X-Posts (@dani_avila7, @jasonzhou1993).

Kernpunkte (kondensiert):

- Agent Teams sind die eskalierte Form von Subagent-Nutzung: mehrere eigenständige Instanzen arbeiten koordiniert am selben Problemraum. Mehrwert entsteht durch parallele Untersuchung, getrennte Kontextfenster, explizite Aufgabenkoordination — nicht durch „mehr Intelligenz“.
- Mentales Modell: ein Lead zerlegt die Arbeit, mehrere Teammates bearbeiten Teilaufgaben, Koordination läuft über Struktur, nicht über freie Konversation.
- Drei entscheidende Voraussetzungen: (1) klare Modulgrenzen — sonst steigen Edit-Kollisionen und Tokenverbrauch; (2) kurzer gemeinsamer Laufzeitkontext — ein überladenes `CLAUDE.md` skaliert bei Teams besonders schlecht, da alle denselben Grundkontext laden; (3) klare Verifikationssignale, damit Teammitglieder ihre Ergebnisse selbst validieren können.
- Geeignete Einsatzszenarien: tiefes Debugging mit konkurrierenden Hypothesen, größere Refactorings über getrennte Modulflächen, Architekturuntersuchungen aus mehreren Blickwinkeln, langlaufende Analyseaufgaben. Weniger sinnvoll: kleine Einzeländerungen, stark gekoppelte Dateien, ohnehin nur sequentiell lösbare Aufgaben.
- Beobachtbare Risiken: höherer Tokenverbrauch, langsamere Gesamtkoordination, mehr Setup-/Kontrollaufwand, falsche Parallelisierung bei gemeinsam bearbeiteten Dateien.
- Sinnvolle Eskalationsreihenfolge: erst normaler Hauptthread, dann spezialisierte Subagents, erst bei echter Parallelität Agent Teams.

## Kernaussagen

- Agent Teams brauchen klare Modulgrenzen, kurzen gemeinsamen Kontext und klare Verifikationssignale, um sich zu lohnen — sonst steigen Edit-Kollisionen und Tokenverbrauch ohne Nutzen → [[Kontrollierte-Agent-Parallelisierung]]
- Sinnvolle Eskalationsreihenfolge: Hauptthread → Subagents → erst bei echter Parallelität Agent Teams, nicht als Default-Modus → [[Kontrollierte-Agent-Parallelisierung]]
