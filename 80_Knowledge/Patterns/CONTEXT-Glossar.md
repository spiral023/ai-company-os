# CONTEXT-Glossar

**Konfidenz:** verifiziert

## Zweck

Löst das Problem zu weitschweifiger, ungenauer Agent-Kommunikation: Ohne geteiltes Vokabular müssen Nutzer und Agent komplexe Sachverhalte jedes Mal neu in ganzen Sätzen umschreiben. Ein Glossar komprimiert das auf einzelne Begriffe.

## Funktionsweise

Eine Datei `CONTEXT.md` im Projekt hält das gemeinsame Vokabular des Projekts fest — die „ubiquitous language" im Sinne von Domain-Driven Design. Ist ein Begriff einmal definiert, ersetzt er ganze Beschreibungssätze: aus „ein Kurs-Lesson-Objekt wird im Dateisystem materialisiert" wird schlicht „materialization cascade". Das spart nicht nur Zeichen, sondern auch Denk-Token, weil der Agent den Begriff nachschlagen statt neu herleiten kann.

## Vorteile

- Variablen, Funktionen und Dateien werden konsistent nach dem geteilten Vokabular benannt.
- Codebasis wird für den Agenten leichter navigierbar.
- Agent verbraucht weniger Token für Denkprozesse, weil er auf ein präziseres, kürzeres Vokabular zugreifen kann.

## Nachteile & Grenzen

- Erfordert Pflegeaufwand: Das Glossar muss aktiv gepflegt werden, sonst veraltet es und wird irreführend statt hilfreich.
- Bloßes Vorhandensein einer `CONTEXT.md` ist nicht dasselbe wie die aktive Pflege-Disziplin — im Referenz-Repo wird explizit zwischen passivem Lesen (ein Zeiler-Verweis) und der aktiven `domain-modeling`-Disziplin (Begriffe hinterfragen, Edge Cases stresstesten, `CONTEXT.md`/ADRs inline aktualisieren) unterschieden.
- Nutzen entfaltet sich erst über mehrere Sessions/Konversationen hinweg; bei Einmal-Aufgaben lohnt sich der Aufbau kaum.

## Wann einsetzen, wann nicht

- Einsetzen: Projekte mit wiederkehrenden, komplexen Fachbegriffen über mehrere Sessions hinweg.
- Nicht einsetzen: einmalige Skripte oder sehr kleine Projekte ohne wiederkehrenden Jargon.

## Belege

- 2026-07-10 · [[2026-07-10-voxyz-mattpocock-skills]] · meinung — Tweet beschreibt `CONTEXT.md` als geteiltes Vokabular, Beispiel „materialization cascade", spart Thinking-Tokens.
- 2026-07-11 · external_repos/mattpocock/skills/CONTEXT.md · verifiziert — Datei existiert im Repo-Root; README-Abschnitt „#2: The Agent Is Way Too Verbose" bestätigt Zweck und exakt das Beispiel „materialization cascade" (verlinkt auf `course-video-manager`-Repo) sowie den Hinweis, dass der Agent dadurch „fewer tokens on thinking" verbraucht.
- 2026-07-11 · external_repos/mattpocock/skills/.agents/invocation.md · verifiziert — Abschnitt „Passive vs active domain work" bestätigt die Unterscheidung zwischen bloßem Lesen von `CONTEXT.md` und der aktiven `domain-modeling`-Pflegedisziplin.

## Spannungen & offene Fragen

- Keine inhaltliche Spannung zu anderen Quellen bekannt; offene Frage: Wie viel Pflegeaufwand ist realistisch, bevor das Glossar veraltet? (aus dem Repo nicht beantwortbar, nur aus eigener Erfahrung zu klären.)

## Verwandte Patterns

- [[Spec-Grilling]]
- [[Skill-Call-Hierarchie]]
