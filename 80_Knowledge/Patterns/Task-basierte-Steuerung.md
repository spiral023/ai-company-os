# Task-basierte-Steuerung

**Konfidenz:** meinung

## Zweck

Ersetzt den linearen Dreischritt „Research → Plan → Implement“ durch eine iterative Schleife, die sich der tatsächlichen Unschärfe realer Arbeit anpasst — nicht jedes Vorhaben lässt sich vorab vollständig in Recherche, Planung und Umsetzung zerlegen.

## Funktionsweise

Statt eines festen Phasenablaufs steuert der Agent das Vorhaben iterativ: „Set Goal → Task → Adjust → Task → Adjust → …“. Jeder „Task“ kann eine Recherche, eine Planungs-/Grilling-Runde, eine Implementierung oder ein Prototyp sein — welche Art von Task als Nächstes ansteht, ergibt sich erst aus der Anpassung nach dem vorherigen Task, nicht aus einem vorab fixierten Plan. Der Agent übernimmt dabei sowohl die Rolle des PM (Ziel setzen, Fortschritt bewerten, nächsten Schritt wählen) als auch die des Developers (den gewählten Task ausführen).

## Vorteile

- Passt sich der tatsächlichen Unschärfe realer Arbeit an, statt Recherche/Planung/Umsetzung künstlich in eine feste Reihenfolge zu zwingen.
- Der Agent kann selbst entscheiden, ob als Nächstes recherchiert, geplant, prototypisiert oder umgesetzt werden muss.
- Nach Erfahrungsbericht die bislang beste Lösung für das Sizing einzelner Tasks auf eine Agent-Session.

## Nachteile & Grenzen

- Einzige bisherige Quelle ist ein Erfahrungsbericht nach „Day 1“ der Nutzung — Langzeiterfahrung fehlt noch.
- Weniger vorab planbar/nachvollziehbar als ein fester Phasenablauf; die Reihenfolge der Tasks steht erst im Nachhinein fest.
- Setzt voraus, dass der Agent die Art des nächsten Tasks (Recherche/Planung/Umsetzung/Prototyp) selbst zuverlässig einschätzen kann.

## Wann einsetzen, wann nicht

- Einsetzen: Vorhaben mit hoher Unschärfe, bei denen sich Recherche-, Planungs- und Umsetzungsbedarf erst im Verlauf zeigen.
- Nicht einsetzen: Vorhaben mit von Anfang an klarem, stabilem Ablauf, bei denen ein fester Phasenplan (Research → Plan → Implement) ausreicht und mehr Nachvollziehbarkeit bietet.

## Belege

- 2026-07-09 · [[2026-07-09-n3sonline-wayfinder]] · meinung — Tweet nach „Day 1“ der Wayfinder-Nutzung: „Your agent can now be both a PM and a developer“ und die Schleife „Set Goal -> Task -> Adjust -> Task -> Adjust -> Task -> Adjust -> ...“ statt „Research -> Plan -> Implement“; zudem „The best solution I have used for 'sizing' tasks for a single agent session.“

## Spannungen & offene Fragen

- Spannung zum linearen Phasen-Ansatz: GSD Core (Discuss → Plan → Execute → Verify → Ship) und die Superpowers-Skill-Kette (brainstorming → worktrees → writing-plans → TDD → Review → finishing, siehe [[Skill-Call-Hierarchie]]) folgen beide einer festen Phasenreihenfolge, während die Task-basierte-Steuerung Reihenfolge und Art jedes Schritts erst iterativ nach jedem „Adjust“ festlegt. Trade-off: Planbarkeit/Disziplin (linearer Ablauf, klare Nachvollziehbarkeit) vs. Flexibilität (iteratives Modell, passt sich unvorhersehbarer Arbeit an). Offene Frage: Lässt sich das iterative Modell mit der Disziplin eines festen Phasenablaufs kombinieren, oder schließen sich beide grundsätzlich aus? Siehe auch [[Workflow-Frameworks]].

## Verwandte Patterns

- [[Spec-Grilling]]
- [[Handoff-Doc]]
- [[Klein-und-komposierbar]]
