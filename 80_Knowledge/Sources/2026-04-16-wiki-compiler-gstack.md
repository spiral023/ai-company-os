---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-16
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „gstack für AI Coding Agents“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/03-tool-profile/01-coding-agent-werkzeuge/wka-gstack-fuer-ai-coding-agents-2026-04-16.md`), Einordnung von `garrytan/gstack` (~73,2k Stars, Version 0.16.2.0, Stand 16.04.2026) per README/ETHOS.md/BROWSER.md-Zugriff.

Kernpunkte, die über den bereits im eigenen Vergleich erfassten Stand hinausgehen:

- gstack ist persona- und command-getrieben statt spec-/artefaktgetrieben: 23 Rollen/Slash-Commands (CEO-Review, Eng-Review, Design-Review, QA, Security Officer, Release Engineer) simulieren ein virtuelles Engineering-Team.
- Eigener persistenter Browser-/QA-Stack (`BROWSER.md`): kompilierter CLI-Client spricht mit einem persistenten lokalen Chromium-Daemon über HTTP (Playwright-basiert), Snapshot-/Ref-System für deterministische Interaktion, Batch-Endpunkte für geringere Round-Trip-Kosten. Das ist ein operatives QA-/UI-Prüfwerkzeug, kein reiner „Browser öffnen“-Skill.
- `ETHOS.md`-Prinzipien werden automatisch in Workflow-Preambles injiziert: „Boil the Lake“ (Vollständigkeit bevorzugen, wenn AI-Kosten dafür gering sind), „Search Before Building“, „User Sovereignty“ (Modell empfiehlt, Nutzer entscheidet).
- Codex-Support explizit (`~/.codex/skills/gstack-*/`); zusätzlich Rolle als „Methodology Source“ für die Orchestrierungsplattform OpenClaw (liefert Planungsdisziplin/Prompt-Brücken, keine eigene Laufzeit).

## Kernaussagen

- gstack ist ein persona- und command-getriebenes Software-Factory-System mit eigenem persistentem Browser-/QA-Stack, nicht primär ein Spezifikations-/Artefaktsystem → [[Workflow-Frameworks]]
- Ein Browser-Daemon mit Snapshot-/Ref-System für deterministische UI-Interaktion ist eine ungewöhnliche, konkrete Umsetzung von „echte QA-Prüfung als fester Bestandteil des Agent-Workflows“ → [[Workflow-Frameworks]]
