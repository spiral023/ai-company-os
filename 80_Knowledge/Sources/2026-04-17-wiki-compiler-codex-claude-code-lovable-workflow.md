---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-17
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Codex, Claude Code und Lovable im Entwickler-Workflow“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/04-vergleiche-und-einordnung/wka-codex-claude-code-lovable-im-entwickler-workflow-2026-04-17.md`). Enthält viel zeitgebundene Preis-/Limit-Information (Stand 17.04.2026, laut Quelle selbst veränderlich) — hier nur der übertragbare Workflow-Kern übernommen, Preise/Limits bewusst nicht ins Wissenssystem übertragen.

Kernpunkte (kondensiert, nur übertragbarer Teil):

- Empfohlener Default für Webapps: Prompt gut vorbereiten → in Lovable starten → visuell schärfen → lokal exportieren → mit einem lokalen Coding Agent weiterbauen.
- Lovable: sehr stark für UI-Iteration, Layout, Mock-Daten, große visuelle Kurswechsel; schwach für lokale Repo-Arbeit, Backend, Tests, Deployment.
- Lokale Coding Agents: schwächer für schnelle visuelle Kurswechsel, sehr stark für Repo-Arbeit, Backend, Tests/Refactoring/Review, Deployment/CI, Kontrolltiefe im Terminal.
- Interne Faustregel: Wenn der erste Entwurf nicht passt, zuerst den Prompt schärfen statt sofort lokal umzubauen; große frühe Änderungen an Design/Informationsarchitektur/Mock-Daten passieren zuerst in Lovable, erst wenn die Richtung stimmt geht der Code ins lokale Repo.
- Doppelnutzung zweier Coding Agents parallel ist möglich, aber nur mit klarer Rollentrennung: ein Hauptagent arbeitet am Code, der andere übernimmt Review/zweite Meinung/getrenntes Teilpaket — nicht beide gleichzeitig dieselben Dateien.

## Kernaussagen

- Empfohlener Standard-Handoff für Webapp-Prototypen: Prompt vorbereiten → Lovable → visuell schärfen → Export → lokaler Coding Agent für Backend/Tests/Deployment → [[Lovable-Prototyp-dann-lokaler-Handoff]]
- Bei unpassendem Entwurf zuerst den Prompt schärfen statt sofort lokal umzubauen; große Design-/IA-Änderungen bleiben zuerst in Lovable → [[Lovable-Prototyp-dann-lokaler-Handoff]]
- Zwei Coding Agents parallel nur mit klarer Rollentrennung (ein Hauptagent, der andere Review/getrenntes Paket), nie gemeinsam an denselben Dateien → [[Kontrollierte-Agent-Parallelisierung]]
