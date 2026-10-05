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
- [[Modell-Eskalation-von-guenstig-nach-teuer]] — beim günstigsten tragfähigen Modell starten und erst bei ausbleibendem Fortschritt hochschalten; Reasoning-Stufe ist die zweite, unabhängige Achse.
- [[Advisor-Agent-gegen-Drift]] — zweiter Agent mit einem einzigen Auftrag: Ziel und Constraints überwachen und bei Abweichung während des Laufs eingreifen.
- [[Voice-Prompting-fuer-Kontextreichtum]] — gesprochene statt getippte Prompts liefern beiläufig mehr Kontext, Details und Constraints.
- [[CI-Agent-mit-Review-Gate]] — Coding Agent läuft sandboxed und event-getriggert in CI, Output läuft ausschließlich über das bestehende Team-Review-Gate (MR/PR).
- [[Sandbox-Komposition-aus-OS-Primitiven]] — kein einzelnes natives OS-Feature deckt den offenen Zugriffsbedarf eines Coding Agents; die Sandbox-Grenze entsteht aus mehreren komponierten Primitiven.
- [[Freiheitsgrad-nach-Aufgaben-Fragilitaet]] — Instruktions-Spezifität (Prosa/Pseudocode/Skript) an die Fehleranfälligkeit der gesteuerten Operation koppeln, das Warum statt nur das Was erklären.
- [[Blockierende-Task-Abhaengigkeiten]] — Tasks blockieren Tasks über `addBlockedBy`/`addBlocks`; abhängige Tasks werden erst nach erfüllten Voraussetzungen automatisch freigegeben.
- [[Hook-erzwungene-Skill-Aktivierung]] — UserPromptSubmit-Hook prüft Prompt technisch auf Trigger-Keywords, statt sich allein auf die Description-Heuristik zu verlassen.
- [[MCP-Code-Execution-statt-Tool-Definitionen]] — Sandbox + vom Modell geschriebener Aufruf-Code statt viele dauerhaft geladene MCP-Tool-Schemas.
- [[Trainingsdaten-Dichte-als-Stack-Kriterium]] — populäre, etwas ältere Stacks statt Bleeding-Edge wählen, weil Modelle auf trainingsdaten-dichtem Code zuverlässiger sind.
- [[Spec-Ordner-pro-Feature]] — fünf feste Dateien (design/implementation/decisions/prompts/future-work) als dauerhaftes, dateibasiertes Gedächtnis pro Feature.
- [[Skill-aus-Demonstration-statt-Beschreibung]] — Skill aus gezeigtem Beispiel (Screenshot, aufgezeichneter Ablauf) statt aus verbaler Spezifikation ableiten.
- [[Skill-Schwellenwert-institutionelles-Wissen]] — Faustregel „>1x/Tag → Skill“; git-eingecheckte Skills werden zu geteiltem Team-Wissen statt persönlichem Werkzeug.
- [[Claude-als-Lernwerkzeug]] — Explanatory-Modus, Diagramme und Spaced-Repetition-Skill nutzen, um unbekannten Code zu verstehen statt nur zu produzieren.
- [[Agent-generierte-Schulung-mit-Curriculum-Gate]] — Briefing und Curriculum prüfen, bevor ein Agent Medien erzeugt und eine interaktive Single-File-HTML-Schulung montiert.
- [[Hook-Entscheidungstyp-nach-Pruefbarkeit]] — deterministisches Skript, Prompt-Hook oder Agent-Hook je nach Prüfbarkeit der Hook-Bedingung wählen.
- [[Screenshot-als-Spezifikationsmedium]] — Bild statt Prosa als Kontext für UI-Analyse, Fehlerdiagnose und Design-zu-Code-Generierung.
- [[Metrikband-gestufte-Agent-Autonomie]] — Rechte des Agents wachsen mit der Schwere einer Metrik-Abweichung (1σ loggen, 2σ read-only, 3σ PR); Erkennung deterministisch ohne Modell.
- [[Hillclimbing-mit-Holdout-Split]] — Prompt, Skill oder Modellwahl gegen ein Eval verbessern: Train/Test-Split, eine Änderung pro Runde, Revert wenn nur Train steigt.
- [[Entscheidung-per-Scoring-statt-Generierung]] — bei festem Antwortraum Label-Logits auslesen statt Text erzeugen; Verteilung plus Schwellen im Code entscheiden über Automatik oder Review.
- [[Adversarialer-Pre-Launch-Check]] — vor dem Release read-only Prüfagenten mit festen Fragenkatalogen die eigene App in einer sicheren Testumgebung brechen lassen.
- [[Review-Autonomie-mit-Shadow-Mode-und-Stichproben]] — automatische Review-Freigaben nur in abgegrenzten Risikobereichen, mit Shadow Mode, protokollierten Entscheidungen und menschlichen Stichproben.
- [[Agent-Rechte-umfassen-Kommunikationswege]] — direkte Rechte reichen nicht: erreichbare Agents und delegierte Aktionen gehören zur Berechtigungsgrenze.

## Themen

Quer zu Patterns und Sources: [[Themen-Übersicht]] bündelt alle Notizen in 16 Themenclustern mit Suchbegriffen für Blog-Beiträge, das [[Keyword-Register]] zeigt mehrfach belegte Begriffe. Beim Ingest verknüpft `python 70_Scripts/themen.py zuordnen <datei>` neue Notizen mit dem Bestand.

## Guides

- [[Matt-Pocock-Skills-Praxisguide]] — Praxisanleitung für Skill-Auswahl, Wayfinder und den Coding-Lifecycle von Exploration bis Code Review.
- [[AI-Coding-Agents-Social-Media-Uebersicht]] — kuratierte Liste von X/Twitter-Accounts, YouTube- und TikTok-Kanälen zu AI Coding Agents (Anthropic, OpenAI, Vordenker, DACH-Creators).
- [[Corporate-Baseline-AI-Coding-Agents]] — Besprechungsgrundlage für unternehmensweite Workspace-, Repo- und Rule-Vorgaben zu Claude Code und OpenAI Codex, inkl. Baseline-Vorschlägen in drei Stufen.

## Vergleiche

- [[Workflow-Frameworks]] — Gegenüberstellung von mattpocock/skills, Superpowers, GSD Core, gstack, addyosmani/agent-skills und Squad mit ersten Empfehlungen.

## Fakten

- [[Modelle-und-Preise]] — datierte Angaben zu Modellen, Preisen, Benchmarks und Markt mit Quelle und Einschränkung; Stand 2026-10-02.
