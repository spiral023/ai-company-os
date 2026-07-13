# Task-basierte-Steuerung

**Konfidenz:** verifiziert

## Zweck

Ersetzt den linearen Dreischritt „Research → Plan → Implement“ durch eine iterative Schleife, die sich der tatsächlichen Unschärfe realer Arbeit anpasst — nicht jedes Vorhaben lässt sich vorab vollständig in Recherche, Planung und Umsetzung zerlegen.

## Funktionsweise

Statt eines festen Phasenablaufs steuert der Agent das Vorhaben iterativ: „Set Goal → Task → Adjust → Task → Adjust → …“. Jeder „Task“ kann eine Recherche, eine Planungs-/Grilling-Runde, eine Implementierung oder ein Prototyp sein — welche Art von Task als Nächstes ansteht, ergibt sich erst aus der Anpassung nach dem vorherigen Task, nicht aus einem vorab fixierten Plan. Der Agent übernimmt dabei sowohl die Rolle des PM (Ziel setzen, Fortschritt bewerten, nächsten Schritt wählen) als auch die des Developers (den gewählten Task ausführen).

Im verifizierten Wayfinder-Skill ist die Map standardmäßig jedoch **Exploration und Planung, nicht Delivery**: Jedes Investigation Ticket löst eine Entscheidung; ausgeführt wird höchstens eine vorbereitende Aufgabe, die eine Entscheidung erst möglich macht. Die Map bleibt absichtlich unvollständig („fog of war“) und wird nach jeder Antwort angepasst. Ein Ticket ist auf eine Agent-Session dimensioniert, und pro Session wird höchstens ein Ticket gelöst. Für große Coding-Vorhaben empfiehlt Matt Pocock anschließend die Übergabe `wayfinder → to-spec → to-tickets → implement`; für nicht-codierende Arbeit darf die Ausführung ausdrücklich Teil der Map bleiben.

## Vorteile

- Passt sich der tatsächlichen Unschärfe realer Arbeit an, statt Recherche/Planung/Umsetzung künstlich in eine feste Reihenfolge zu zwingen.
- Der Agent kann selbst entscheiden, ob als Nächstes recherchiert, geplant, prototypisiert oder umgesetzt werden muss.
- Nach Erfahrungsbericht die bislang beste Lösung für das Sizing einzelner Tasks auf eine Agent-Session.

## Nachteile & Grenzen

- Einzige bisherige Quelle ist ein Erfahrungsbericht nach „Day 1“ der Nutzung — Langzeiterfahrung fehlt noch.
- Weniger vorab planbar/nachvollziehbar als ein fester Phasenablauf; die Reihenfolge der Tasks steht erst im Nachhinein fest.
- Setzt voraus, dass der Agent die Art des nächsten Tasks (Recherche/Planung/Umsetzung/Prototyp) selbst zuverlässig einschätzen kann.
- Wer Wayfinder bei Coding als vollständige Delivery-Pipeline nutzt, vermischt Entscheidungen und Lieferartefakte; dies widerspricht dem Planungs-Default des Skills, sofern die Map-Notes keine Ausnahme festlegen.

## Wann einsetzen, wann nicht

- Einsetzen: Vorhaben mit hoher Unschärfe, bei denen sich Recherche-, Planungs- und Umsetzungsbedarf erst im Verlauf zeigen.
- Nicht einsetzen: Vorhaben mit von Anfang an klarem, stabilem Ablauf, bei denen ein fester Phasenplan (Research → Plan → Implement) ausreicht und mehr Nachvollziehbarkeit bietet.

## Belege

- 2026-07-09 · [[2026-07-09-n3sonline-wayfinder]] · meinung — Tweet nach „Day 1“ der Wayfinder-Nutzung: „Your agent can now be both a PM and a developer“ und die Schleife „Set Goal -> Task -> Adjust -> Task -> Adjust -> Task -> Adjust -> ...“ statt „Research -> Plan -> Implement“; zudem „The best solution I have used for 'sizing' tasks for a single agent session.“
- 2026-07-06 · [[2026-07-06-nightmoon-wayfinder]] · meinung — Früher Erfahrungsbericht beschreibt weniger menschliche Koordinationsarbeit, bewertet eine mögliche höhere Agent-Autonomie aber ausdrücklich als unsichere Beobachtung.
- 2026-07-11 · [[2026-07-11-mattpocock-wayfinder-to-implementation]] · meinung — Matt grenzt den Coding-Flow als `/wayfinder → /to-spec → /to-tickets → /implement` vom möglichen End-to-End-Einsatz für nicht-codierende Arbeit ab.
- 2026-07-13 · external_repos/mattpocock/skills/skills/engineering/wayfinder/SKILL.md · verifiziert — Skill definiert Wayfinder als planende Fog-of-War-Map, dimensioniert jedes Ticket auf eine 100K-Token-Session und verbietet mehr als ein gelöstes Ticket pro Session; Delivery ist nur per expliziter Notes-Ausnahme Teil der Map.
- 2026-07-13 · external_repos/mattpocock/skills/skills/engineering/to-spec/SKILL.md · verifiziert — `/to-spec` synthetisiert den bereits geklärten Kontext ohne neues Interview in eine Spec auf dem konfigurierten Tracker.
- 2026-07-13 · external_repos/mattpocock/skills/skills/engineering/to-tickets/SKILL.md · verifiziert — `/to-tickets` zerlegt Spec oder Plan in vertikale Tracer-Bullet-Tickets mit Blocking Edges und verweist für die Abarbeitung auf `/implement`.

## Spannungen & offene Fragen

- Spannung zum linearen Phasen-Ansatz: GSD Core (Discuss → Plan → Execute → Verify → Ship) und die Superpowers-Skill-Kette (brainstorming → worktrees → writing-plans → TDD → Review → finishing, siehe [[Skill-Call-Hierarchie]]) folgen beide einer festen Phasenreihenfolge, während die Task-basierte-Steuerung Reihenfolge und Art jedes Schritts erst iterativ nach jedem „Adjust“ festlegt. Trade-off: Planbarkeit/Disziplin (linearer Ablauf, klare Nachvollziehbarkeit) vs. Flexibilität (iteratives Modell, passt sich unvorhersehbarer Arbeit an). Offene Frage: Lässt sich das iterative Modell mit der Disziplin eines festen Phasenablaufs kombinieren, oder schließen sich beide grundsätzlich aus? Siehe auch [[Workflow-Frameworks]].
- Matts Klarstellung löst einen Teil dieser Spannung praktisch: Wayfinder bleibt innerhalb der unscharfen Exploration iterativ; sobald der Weg klar ist, wechselt Coding in einen linearen Delivery-Flow. Die Flexibilität gilt damit nicht zwingend für den gesamten Software-Lifecycle.

## Verwandte Patterns

- [[Spec-Grilling]]
- [[Handoff-Doc]]
- [[Klein-und-komposierbar]]
