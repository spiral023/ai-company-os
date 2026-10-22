# Multi-Agent & Parallelisierung

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-22. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Mehrere Agents oder Sessions zusammen: Subagents, Agent Teams, Worktrees, Task-Abhängigkeiten, Rollen, Advisor. Dauerläufe ohne Aufsicht stehen in autonomie.

## Suchbegriffe

- **Hauptkeyword:** Claude Code Subagents
- **Long-Tail:** Agent Teams Claude Code; Git Worktrees parallele Agents; Subagents vs. Agent Teams; Multi-Agent Orchestrierung; Task-Abhängigkeiten Claude Code; Kosten paralleler Agents
- **Fragen:** Wann lohnt sich Parallelisierung? / Subagent oder Agent Team?
- **Häufig in den Quellen:** subagents (6), claude code subagents (5), git worktrees (4), paperclip (4), effort (4), openclaw (3), heartbeats (3), agent-organisation (3), addblockedby (2), multi-agent (2), claude code tasks (2), claude code agent teams (2), modulgrenzen (2), codex cli (2), rollen (2), budgets (2), freigaben (2), parallel agents (2), agent teams (2), edit-kollisionen (2)

## Verwandte Themen

- [[Thema-Autonome-Läufe-Loops-CI]] — Autonome Läufe, Loops & CI
- [[Thema-Kontext-Management]] — Kontext-Management
- [[Thema-Modelle-Kosten-Limits]] — Modelle, Kosten & Limits
- [[Thema-Verifikation-Tests-Review]] — Verifikation, Tests & Review

## Patterns (4)

- [[Advisor-Agent-gegen-Drift]] · meinung · 3 Belege
- [[Agent-Organisation-mit-Rollen-Budgets-und-Heartbeats]] · meinung · 3 Belege
- [[Blockierende-Task-Abhaengigkeiten]] · meinung · 5 Belege
- [[Kontrollierte-Agent-Parallelisierung]] · mehrfach-belegt · 50 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Adversarialer-Pre-Launch-Check]], [[Agent-Rechte-umfassen-Kommunikationswege]], [[Bedarfsorientierter-Repositoryzugriff]], [[Prompt-Cache-TTL-nach-Agent-Pausen-waehlen]]

## Quellen (21)

- [[2026-10-09-git-worktree]] — Getrennte Worktrees teilen das Repository, isolieren aber keine Laufzeitressourcen.
- [[2026-10-06-promptgefluester-vielleicht-mal-zur-begruendung-warum-ich-euch-zeig-wie-ich-280-website]] — `@promptgefluester` beschreibt eine zusätzliche Koordinationsebene über einzelnen Projekt-Orchestratoren.
- [[2026-10-02-matt-pocock-live-poteto-creator-of-pstack-on-shipping-1-000]] — Verifikations-CLIs und gebündelte Befunde stützen parallele Agent-Arbeit; PR-Mengen bleiben Selbstauskunft und automatische Merges werden nur stichprobenartig geprüft.
- [[2026-09-29-voxyz_ai-2105012597796057438]] — Vox beschreibt für GPT-6.1 Sol (Stand 2026-09-29) einen Agent-Tree in Codex: Orchestrator `high`, explorer/worker/researcher auf `medium`, `gpt-6-astra` auf `xhigh` nur als Reviewer vor großen Änderun
- [[2026-09-27-voxyz_ai-2104254744722383210]] — Vox lässt Opus 5.5 aus 1.500+ eigenen Posts ein Repo mit 66 Skills bauen: Mining (71 Agenten), Planning (9), Scaffold (1), Build (21), QA (3).
- [[2026-09-26-voxyz_ai-2103977414711767244]] — Ein read-only Subagent pro Prüfgruppe erstellt Befunde, der Hauptagent behebt sie nach Freigabe allein, damit nie zwei Agents dieselbe Datei editieren.
- [[2026-09-25-promptgefluester-weil-mich-viele-danach-gefragt-haben-wollt-ich-jetzt-kurz-noch-n]] — `@promptgefluester` erläutert ein Terminal-Setup, in dem ein Orchestrator laufende Sessions betreut und ein separater Aufgabenmanager Prioritäten und Aufgabenstand hält.
- [[2026-09-09-voxyz_ai-2097814698204832116]] — Günstige Modelle explorieren, ein mittleres implementiert, das stärkste prüft nur bei Bedarf; Rollen gehören per Konfiguration statt Prosa festgelegt und in den Logs verifiziert.
- [[2026-08-30-alex-sprogis-loop-graph-engineering-das-letzte-video-was-du-s]] — Ein Agent-Loop braucht ein binäres Erfolgskriterium, ein Iterationslimit und einen unabhängigen Prüfer; große Aufträge laufen als Schritte mit frischem Kontext und Artefakt-Übergaben.
- [[2026-06-02-trq212-2061907337154367865]] — Claude erzeugt pro Aufgabe ein Skript mit Subagents in eigenen Kontexten; Verifier und Classifier vermeiden Selbstbewertung, kosten aber deutlich mehr Tokens.
- [[2026-05-21-christophmagnussen-ki-agenten-weichen-ab]] — Agent Drift entsteht unbemerkt bei Subagent- und Tool-Aufrufen; Prävention durch vorab definierte Entscheidungsregeln schlägt reine Sichtbarkeit.
- [[2026-04-17-wiki-compiler-agent-teams-in-claude-code]] — Agent Teams lohnen sich nur bei klaren Modulgrenzen, kurzem gemeinsamem Kontext und Verifikationssignalen, und erst nach Hauptthread und Subagents.
- [[2026-04-12-digitale-profis-so-ersetzt-du-dein-unternehmen-mit-ki-agenten-pa]] — Organigramm, Issues und Heartbeats machen Agent-Aufgaben sichtbar; rollenabhängige Auslösung ist kein Nachweis einer funktionierenden menschenfreien Firma.
- [[2026-04-03-julian-ivanov-ki-automat-ich-habe-eine-firma-ohne-menschen-gebaut-papercl]] — Eine dauerhafte Agent-Organisation erhält Aufgaben und Freigaben; unvollständige Ergebnisse und manuelles Setup begrenzen die Autonomiebehauptung.
- [[2026-04-01-ai-mit-arnie-claude-code-und-paperclip-aendern-alles]] — Paperclip verbindet Agent-Rollen, Aufgaben, Budgets und Heartbeats; die Demo zeigt auch nicht beauftragte Arbeit und manuelle Eingriffe.
- [[2026-02-28-openai-codex-multi-agents-guide]] — Codex Sub-Agenten haben eng gefasste Rollen, begrenzte Parallelität und erben die Sandbox, laufen aber mit non-interaktiven Approvals.
- [[2026-02-23-elvis-openclaw-codex-agent-swarm]] — Business-Kontext und Code-Kontext gehören in getrennte Agent-Ebenen; parallele Agents brauchen Worktrees, Task-Registry, mehrstufige AI-Reviews und einen Rechteschnitt.
- [[2026-02-07-jasonzhou-claude-code-agent-teams]] — Agent Teams ersetzen isolierte Sub-Agents durch geteilte Task-Liste und Messaging; sie kosten mehr Tokens und lohnen sich vor allem für Deep Debugging.
- [[2026-02-07-daniel-san-agent-teams-praxismuster]] — Agent Teams laufen kollisionsfrei bei klaren Modulgrenzen, kurzem operationalem CLAUDE.md und definierten Verifikationssignalen; N Teammates kosten N-fachen Kontext.
- [[2026-01-31-bcherny-claude-code-team-tips]] — Das Claude-Code-Team parallelisiert per Worktrees, lässt Pläne gegenreviewen, pflegt CLAUDE.md nach jedem Fehler und macht wiederkehrende Aufgaben zu Skills.
- [[2026-01-23-nummanali-claude-task-system]] — Das Task-System bildet Abhängigkeiten als Graph ab, speichert Zustand in Dateien und koordiniert parallele Agenten über eine gemeinsame Liste.

## Quellen mit diesem Thema als Nebenthema

- [[2026-10-19-voxyz_ai-2112302775547679169]]
- [[2026-10-18-ai-news-strategy-daily-n-what-really-happens-when-ai-agents-meet-in-the-w]]
- [[2026-10-15-floknowsai-mit-tea-free-code-steuere-ich-alle-meine-cloud-code-und-kodex-abos-aus]]
- [[2026-10-13-vincentmumme-wenn-du-das-problem-kennst-dass-du-2-chat-gpt-abos-hast-1-clot-abo-open]]
- [[2026-10-13-anthropic-redesigning-source-control-at-anthropic]]
- [[2026-10-12-promptgefluester-ich-werde-oft-gefragt-was-arbeite-ich-denn-eigentlich-noch-wenn-die-ki]]
- [[2026-10-12-0xmovez-2109604520770548146]]
- [[2026-10-10-voxyz_ai-2109056129884123370]]
- [[2026-10-08-voxyz_ai-haiku-subagents-und-opus-worker]]
- [[2026-10-07-alex-sprogis-t3-code-endlich-eine-steuerzentrale-fuer-alle-de]]
- [[2026-09-27-voxyz_ai-2104224555040452925]]
- [[2026-09-25-voxyz_ai-2103586663393853636]]
- [[2026-09-24-floknowsai-open-claw-ist-zurueck-und-spielt-jetzt-wieder-in-einer-liga-mit-kodex]]
- [[2026-09-22-claude-getting-the-most-out-of-opus-5-5-in-claude-and-c]]
- [[2026-09-19-voxyz_ai-2101355643882065971]]
- [[2026-09-07-sairahul1-2096902575035683147]]
- [[2026-07-21-claudedevs-2079654423828304282]]
- [[2026-04-17-wiki-compiler-praktische-claude-code-workflows]]
- [[2026-04-17-wiki-compiler-codex-claude-code-lovable-workflow]]
- [[2026-03-17-zerotopete-never-use-terminal-again]]
- [[2026-02-20-aseem-shrey-claude-codex-plan-review]]
- [[2026-02-14-gmoney-eth-25-claude-code-lessons]]
- [[2026-02-01-anthropic-docs-create-custom-subagents]]
- [[2026-02-01-aiedge-claude-code-starter-pack]]
- [[2026-01-25-sankalp-claude-code-experience]]
- [[2026-01-12-dhruv1103-lessons-learned-500k-lines-claude-code]]
- [[2026-01-04-ai-news-strategy-daily-n-why-andrej-karpathy-feels-behind-and-what-it-mea]]
