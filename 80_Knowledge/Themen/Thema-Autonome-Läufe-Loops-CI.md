# Autonome Läufe, Loops & CI

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-09-30. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Agents ohne Aufsicht: Ralph Loop, /goal, Nachtläufe, Headless-Betrieb, CI-Agents, Autonomiestufen und ihre Grenzen.

## Suchbegriffe

- **Hauptkeyword:** Ralph Loop
- **Long-Tail:** Ralph Loop einrichten; Claude Code Headless CI; Claude Code über Nacht; Autonomiestufen Coding Agent; Claude Code GitHub Action; Loop Engineering
- **Fragen:** Kann ich einen Agent über Nacht laufen lassen? / Wie viel Autonomie ist sicher?
- **Häufig in den Quellen:** ralph loop (5), steering.md (3), git worktree (2), sandboxed runner (2), long-running agents (2), playwright vitest (2), overnight agents (2), --output-format json, @-referenzen, plan mode headless, claude code common workflows, extended thinking, unix-pipe, claude -p, @claude merge request, oidc, claude code gitlab ci/cd, review gate, aws bedrock, google vertex ai

## Verwandte Themen

- [[Thema-Multi-Agent-Parallelisierung]] — Multi-Agent & Parallelisierung
- [[Thema-Verifikation-Tests-Review]] — Verifikation, Tests & Review
- [[Thema-Sicherheit-Sandboxing]] — Sicherheit & Sandboxing
- [[Thema-Kontext-Management]] — Kontext-Management

## Patterns (3)

- [[CI-Agent-mit-Review-Gate]] · mehrfach-belegt · 7 Belege
- [[Metrikband-gestufte-Agent-Autonomie]] · meinung · 1 Belege
- [[Ralph-Loop-Frischer-Kontext-pro-Iteration]] · mehrfach-belegt · 11 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Advisor-Agent-gegen-Drift]], [[Testharness-als-staerkster-Hebel]]

## Quellen (9)

- [[2026-08-12-voxyz_ai-2087579867139264681]] — Ungenutztes Agent-Kontingent lässt sich über einen reinen Kandidatenbericht verplanen, wenn nur umkehrbare Aufgaben mit Prüfbefehl in isolierten Branches zugelassen sind.
- [[2026-07-24-agenticjames-the-creator-of-claude-code-released-a-guide-to-the-4-levels-of-ai-coding]] — Das Vier-Stufen-Modell von Pair Programming bis Agentenflotte trägt nur mit automatischer Verifikation, und Fehlläufe sollten systematisch in besseren Startkontext übersetzt werden.
- [[2026-07-03-calebwritescode-loop-engineering-explained-in-7-min-and-simplified]] — Loop Engineering ist als vierte Schicht über Prompt, Context und Harness eingeordnet, lässt Agenten sich selbst anstoßen; der Nutzen ist laut Autor unbewiesen.
- [[2026-05-18-agenticjames-using-goal-with-a-task-management-system-is-the-most-overpowered-way-to]] — Ein Task pro Datei plus fest vorgegebene Prozedur im /goal-Befehl macht Reihenfolge und Laufzeit eines Agenten-Loops steuerbar, Kosten und Abbruchkriterium bleiben offen.
- [[2026-04-17-wiki-compiler-ralph-loop]] — Beim Ralph Loop liegt der Fortschritt in Dateien und Git statt im Modellkontext, jede Iteration startet frisch, und ohne echte Tests halluziniert der Agent Fortschritt.
- [[2026-02-23-d4m1n-ralph-loop-setup-primaer]] — Der Ralph Loop trägt Zustand in Dateien statt im Modell und läuft mit Tests und Steering-Datei stundenlang autonom; die Spec-Prüfung vorab ist billiger als Rollbacks.
- [[2026-02-05-carlini-anthropic-c-compiler]] — Der stärkste Hebel für lang laufende Agent-Teams ist ein präzises, maschinenlesbares Testharness; ein unpräziser Verifier erzeugt zuverlässig falschen Erfolg.
- [[2026-02-01-anthropic-docs-claude-code-gitlab-ci]] — Ein Coding Agent läuft als sandboxed, event-getriggerter CI-Job, dessen Output ausschließlich über das bestehende Merge-Request-Review läuft.
- [[2026-02-01-anthropic-docs-claude-code-common-workflows]] — Worktrees, @-Referenzen, Pipes mit JSON-Ausgabe und headless Plan Mode machen Claude Code zu einer komponierbaren Unix-Utility.

## Quellen mit diesem Thema als Nebenthema

- [[2026-08-09-natebjones-decision-exhaustion-is-real-discuss]]
- [[2026-08-02-promptgefluester-wenn-ihr-versucht-euer-software-projekt-mit-fable-five-oder-o-plus-5]]
- [[2026-07-09-n3sonline-wayfinder]]
- [[2026-06-02-trq212-2061907337154367865]]
- [[2026-05-21-christophmagnussen-ki-agenten-weichen-ab]]
- [[2026-02-20-boris-tane-sdlc-is-dead]]
- [[2026-02-05-d4m1n-docker-sandboxes]]
- [[2026-02-02-unsloth-team-claude-code-local-llm]]
- [[2026-01-15-avasdr34m-its-not-easy-but-it-is-simple-kontext-nutzung-in-claude-code-entscheidet]]
