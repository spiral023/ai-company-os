# Knowledge-Index

Einstieg ins Knowledge-System. Regeln und Templates: [[80_Knowledge/README|README]] (80_Knowledge/README.md).

## Patterns

- [[Spec-Grilling]] — Agent verhört den Nutzer vor der Umsetzung, bis die Spec klar ist.
- [[CONTEXT-Glossar]] — geteiltes Projekt-Vokabular in `CONTEXT.md` komprimiert Kommunikation und spart Thinking-Tokens.
- [[Handoff-Doc]] — Konversation wird in ein Übergabe-Dokument kompaktiert, der nächste Agent macht nahtlos weiter.
- [[Skill-Call-Hierarchie]] — user-invoked Skills orchestrieren, model-invoked Skills tragen die Disziplin; Orchestrator ruft nie Orchestrator.
- [[Klein-und-komposierbar]] — Skills bleiben klein, komponierbar, leicht hackbar; Prozesskontrolle bleibt beim Menschen.
- [[One-File-per-Failure-Mode]] — pro typischem Fehlermodus des Agenten genau ein fokussierter Skill.
- [[Task-basierte-Steuerung]] — iterative Schleife „Set Goal → Task → Adjust → …“ statt linearem „Research → Plan → Implement“; Agent als PM und Developer zugleich.
- [[AGENTS-md-Onboarding-Design]] — Agent-Onboarding-Dateien kurz und universell halten, Spezialwissen per Progressive Disclosure auslagern.
- [[Erweiterungs-Ebenen-Zuordnung]] — CLAUDE.md/Skill/Subagent/Hook/MCP tragen unterschiedliche Verantwortung; dieselbe Anforderung nicht mehrfach modellieren.
- [[Kontext-Hygiene-Entscheidungsbaum]] — bewusste Entscheidung Continue/rewind/compact/clear/Subagent nach jedem Arbeitsblock statt reflexhaftem Weiterreden.
- [[Plan-first-mit-getrenntem-Review]] — lesende Discovery, Plan als Artefakt, getrennte Builder/Reviewer/Verifier-Rollen.
- [[TDD-als-Verifikationshebel]] — vertikale Slices (ein Test, minimaler Code, Refactor) als Tracer-Bullets gegen spekulativen Code.
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]] — Skills als messbare Produkte mit Baseline-Vergleich und Trigger-Optimierung statt Bauchgefühl.
- [[Ralph-Loop-Frischer-Kontext-pro-Iteration]] — jede Iteration mit frischem Kontext, Zustand in Dateien/Git statt im Modell.
- [[Kontrollierte-Agent-Parallelisierung]] — Parallelisierung nur bei klaren Modulgrenzen, kurzem gemeinsamem Kontext und klaren Verifikationssignalen.
- [[Lovable-Prototyp-dann-lokaler-Handoff]] — Lovable für schnelle UI-Prototypen, früher Export zu lokalem Coding Agent für Backend/Tests/Security.
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]] — Secret-Schutz braucht technisch erzwungene Deny-Regeln statt bloßer Hinweise in der Agent-Datei.
- [[Great-Decoupling-Rollenverstaendnis]] — Programming und Engineering entkoppeln sich; neue Rolle ist Tech Lead + QA Lead statt Zeile-für-Zeile-Reviewer.
- [[Testharness-als-staerkster-Hebel]] — bei autonomen Agenten entscheidet die Qualität des Verifiers über echten Fortschritt, nicht der Prompt.
- [[Intent-Engineering-als-dritte-Schicht]] — nach Prompt- und Context Engineering fehlt oft die explizite Zielhierarchie/Trade-off-Logik für Agenten.
- [[Fable-Unknowns-vor-Prompt-Qualitaet]] — der Engpass ist nicht der Prompt, sondern unaufgeschriebene Annahmen; acht Techniken zum systematischen Aufdecken.
- [[Action-Space-Design-nach-Modellfaehigkeit]] — Agent-Tools am tatsächlichen Fähigkeitsprofil des Modells ausrichten statt an Feature-Vollständigkeit.
- [[Lokale-Modell-Umleitung-Muster]] — Claude Code per Umgebungsvariablen auf lokale oder alternative Cloud-Modelle umleiten, CLI bleibt gleich.
- [[Anti-Rationalization-Tables]] — vorformulierte Widerlegungen typischer Ausreden verhindern, dass Agenten disziplin-tragende Workflows überspringen.

## Guides

- [[Matt-Pocock-Skills-Praxisguide]] — Praxisanleitung für Skill-Auswahl, Wayfinder und den Coding-Lifecycle von Exploration bis Code Review.
- [[AI-Coding-Agents-Social-Media-Uebersicht]] — kuratierte Liste von X/Twitter-Accounts, YouTube- und TikTok-Kanälen zu AI Coding Agents (Anthropic, OpenAI, Vordenker, DACH-Creators).

## Vergleiche

- [[Workflow-Frameworks]] — Gegenüberstellung von mattpocock/skills, Superpowers, GSD Core, gstack, addyosmani/agent-skills und Squad mit ersten Empfehlungen.
