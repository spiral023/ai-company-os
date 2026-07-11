---
url: https://x.com/Voxyz_ai/status/2075603005143924959
autor: "@Voxyz_ai (Vox)"
datum: 2026-07-10
erfasst: 2026-07-11
typ: tweet
---

# Vox zu mattpocock/skills

## Inhalt

the most irreplaceable layer of the agent stack is now a folder of markdown files.

best reference is mattpocock's skills repo: one md folder straight from his .claude directory, 164k stars.

1. /grill-me interrogates you until the spec is clear. /tdd locks in red-green-refactor. /improve-codebase-architecture treats codebase rot, he recommends running it every few days. one file per failure mode.
2. CONTEXT.md holds the project's shared vocabulary. once the glossary exists, a bug that took a full sentence to describe (a course lesson getting materialized into the file system) shrinks to one term: materialization cascade. the agent spends fewer thinking tokens.
3. /handoff compacts the current conversation into a handoff doc, the next agent continues in place. /wayfinder turns work too big for one session into a map of tickets to chew through.
4. the md files have a call hierarchy. user-invoked skills orchestrate, model-invoked skills hold the discipline. an orchestrator may call the discipline files, never another orchestrator. a dependency architecture growing out of plain text files.
5. npx skills@latest add mattpocock/skills. pick the skills, pick which agents to install them on, 30 seconds in. installs like an npm package.
6. the readme sets the boundary up front: skills stay small, composable, easy to hack. control of the process stays with you.

## Kernaussagen

- /grill-me verhört den Nutzer, bis die Spezifikation klar ist; ein Skill pro typischem Fehlermodus → [[Spec-Grilling]], [[One-File-per-Failure-Mode]]
- CONTEXT.md hält das gemeinsame Projekt-Vokabular fest und komprimiert Kommunikation (Beispiel „materialization cascade"), spart Thinking-Tokens → [[CONTEXT-Glossar]]
- /handoff kompaktiert die laufende Konversation in ein Übergabe-Dokument, der nächste Agent macht nahtlos weiter; /wayfinder zerlegt zu große Arbeit in eine Landkarte aus Tickets → [[Handoff-Doc]]
- Die Skill-Dateien bilden eine Aufruf-Hierarchie: user-invoked Skills orchestrieren, model-invoked Skills tragen die Disziplin; ein Orchestrator ruft nie einen anderen Orchestrator → [[Skill-Call-Hierarchie]]
- Das README setzt die Grenze bewusst: Skills bleiben klein, komponierbar, leicht hackbar; die Prozesskontrolle bleibt beim Menschen → [[Klein-und-komposierbar]]

## Anmerkungen

- Die im Tweet genannte Zahl „164k stars" konnte nicht bestätigt werden: ein WebFetch-Abruf des Repos vom 2026-07-11 zeigt rund 16.400 Stars. Die Diskrepanz (Faktor ~10) bleibt als offene Unsicherheit stehen — möglicherweise ein Tippfehler des Autors (16,4k vs. 164k) oder eine seither veraltete Angabe. Nicht weiter verifizierbar aus dem lokal geklonten Repo (`external_repos/mattpocock/skills/`), da dieses keine Star-Zahl enthält.
