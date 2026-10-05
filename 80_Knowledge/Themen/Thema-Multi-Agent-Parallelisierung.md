# Multi-Agent & Parallelisierung

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-05. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Mehrere Agents oder Sessions zusammen: Subagents, Agent Teams, Worktrees, Task-Abhängigkeiten, Rollen, Advisor. Dauerläufe ohne Aufsicht stehen in autonomie.

## Suchbegriffe

- **Hauptkeyword:** Claude Code Subagents
- **Long-Tail:** Agent Teams Claude Code; Git Worktrees parallele Agents; Subagents vs. Agent Teams; Multi-Agent Orchestrierung; Task-Abhängigkeiten Claude Code; Kosten paralleler Agents
- **Fragen:** Wann lohnt sich Parallelisierung? / Subagent oder Agent Team?
- **Häufig in den Quellen:** subagents (6), git worktrees (4), claude code subagents (4), effort (4), addblockedby (2), claude code tasks (2), multi-agent (2), modulgrenzen (2), claude code agent teams (2), openclaw (2), codex cli (2), edit-kollisionen (2), agent teams (2), parallel agents (2), agent drift (2), goal drift (2), context rot (2), parallel (2), subagent (2), /clear (2)

## Verwandte Themen

- [[Thema-Autonome-Läufe-Loops-CI]] — Autonome Läufe, Loops & CI
- [[Thema-Kontext-Management]] — Kontext-Management
- [[Thema-Modelle-Kosten-Limits]] — Modelle, Kosten & Limits
- [[Thema-Verifikation-Tests-Review]] — Verifikation, Tests & Review

## Patterns (3)

- [[Advisor-Agent-gegen-Drift]] · meinung · 3 Belege
- [[Blockierende-Task-Abhaengigkeiten]] · meinung · 1 Belege
- [[Kontrollierte-Agent-Parallelisierung]] · mehrfach-belegt · 37 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Adversarialer-Pre-Launch-Check]], [[Agent-Rechte-umfassen-Kommunikationswege]]

## Quellen (14)

- [[2026-09-29-voxyz_ai-2105012597796057438]] — Vox beschreibt für GPT-6.1 Sol (Stand 2026-09-29) einen Agent-Tree in Codex: Orchestrator `high`, explorer/worker/researcher auf `medium`, `gpt-6-astra` auf `xhigh` nur als Reviewer vor großen Änderun
- [[2026-09-27-voxyz_ai-2104254744722383210]] — Vox lässt Opus 5.5 aus 1.500+ eigenen Posts ein Repo mit 66 Skills bauen: Mining (71 Agenten), Planning (9), Scaffold (1), Build (21), QA (3).
- [[2026-09-26-voxyz_ai-2103977414711767244]] — Ein read-only Subagent pro Prüfgruppe erstellt Befunde, der Hauptagent behebt sie nach Freigabe allein, damit nie zwei Agents dieselbe Datei editieren.
- [[2026-09-09-voxyz_ai-2097814698204832116]] — Günstige Modelle explorieren, ein mittleres implementiert, das stärkste prüft nur bei Bedarf; Rollen gehören per Konfiguration statt Prosa festgelegt und in den Logs verifiziert.
- [[2026-08-30-alex-sprogis-loop-graph-engineering-das-letzte-video-was-du-s]] — Ein Agent-Loop braucht ein binäres Erfolgskriterium, ein Iterationslimit und einen unabhängigen Prüfer; große Aufträge laufen als Schritte mit frischem Kontext und Artefakt-Übergaben.
- [[2026-06-02-trq212-2061907337154367865]] — Claude erzeugt pro Aufgabe ein Skript mit Subagents in eigenen Kontexten; Verifier und Classifier vermeiden Selbstbewertung, kosten aber deutlich mehr Tokens.
- [[2026-05-21-christophmagnussen-ki-agenten-weichen-ab]] — Agent Drift entsteht unbemerkt bei Subagent- und Tool-Aufrufen; Prävention durch vorab definierte Entscheidungsregeln schlägt reine Sichtbarkeit.
- [[2026-04-17-wiki-compiler-agent-teams-in-claude-code]] — Agent Teams lohnen sich nur bei klaren Modulgrenzen, kurzem gemeinsamem Kontext und Verifikationssignalen, und erst nach Hauptthread und Subagents.
- [[2026-02-28-openai-codex-multi-agents-guide]] — Codex Sub-Agenten haben eng gefasste Rollen, begrenzte Parallelität und erben die Sandbox, laufen aber mit non-interaktiven Approvals.
- [[2026-02-23-elvis-openclaw-codex-agent-swarm]] — Business-Kontext und Code-Kontext gehören in getrennte Agent-Ebenen; parallele Agents brauchen Worktrees, Task-Registry, mehrstufige AI-Reviews und einen Rechteschnitt.
- [[2026-02-07-jasonzhou-claude-code-agent-teams]] — Agent Teams ersetzen isolierte Sub-Agents durch geteilte Task-Liste und Messaging; sie kosten mehr Tokens und lohnen sich vor allem für Deep Debugging.
- [[2026-02-07-daniel-san-agent-teams-praxismuster]] — Agent Teams laufen kollisionsfrei bei klaren Modulgrenzen, kurzem operationalem CLAUDE.md und definierten Verifikationssignalen; N Teammates kosten N-fachen Kontext.
- [[2026-01-31-bcherny-claude-code-team-tips]] — Das Claude-Code-Team parallelisiert per Worktrees, lässt Pläne gegenreviewen, pflegt CLAUDE.md nach jedem Fehler und macht wiederkehrende Aufgaben zu Skills.
- [[2026-01-23-nummanali-claude-task-system]] — Das Task-System bildet Abhängigkeiten als Graph ab, speichert Zustand in Dateien und koordiniert parallele Agenten über eine gemeinsame Liste.

## Quellen mit diesem Thema als Nebenthema

- [[2026-09-27-voxyz_ai-2104224555040452925]]
- [[2026-09-25-voxyz_ai-2103586663393853636]]
- [[2026-09-22-claude-getting-the-most-out-of-opus-5-5-in-claude-and-c]]
- [[2026-09-19-voxyz_ai-2101355643882065971]]
- [[2026-09-07-sairahul1-2096902575035683147]]
- [[2026-04-17-wiki-compiler-praktische-claude-code-workflows]]
- [[2026-04-17-wiki-compiler-codex-claude-code-lovable-workflow]]
- [[2026-03-17-zerotopete-never-use-terminal-again]]
- [[2026-02-20-aseem-shrey-claude-codex-plan-review]]
- [[2026-02-14-gmoney-eth-25-claude-code-lessons]]
- [[2026-02-01-anthropic-docs-create-custom-subagents]]
- [[2026-02-01-aiedge-claude-code-starter-pack]]
- [[2026-01-25-sankalp-claude-code-experience]]
- [[2026-01-12-dhruv1103-lessons-learned-500k-lines-claude-code]]
