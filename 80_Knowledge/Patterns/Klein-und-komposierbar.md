# Klein-und-komposierbar

**Konfidenz:** verifiziert

## Zweck

Bewahrt die Kontrolle über den Entwicklungsprozess beim Menschen, statt sie an ein Framework abzugeben. Adressiert das Risiko, dass umfassende, prozess-diktierende Systeme zwar Struktur geben, dabei aber Fehler im Prozess selbst schwer auffindbar und korrigierbar machen.

## Funktionsweise

Jeder Skill wird bewusst klein, leicht anpassbar und modellunabhängig gehalten, statt ihn in ein großes, alles umfassendes Framework einzubetten. Das README des Referenz-Repos setzt diese Grenze explizit: Ansätze wie GSD, BMAD und Spec-Kit „try to help by owning the process“, nehmen dabei aber Kontrolle weg und machen Bugs im Prozess schwer auflösbar. Die eigenen Skills sollen stattdessen „small, easy to adapt, and composable“ sein, mit jedem Modell funktionieren und explizit zum Selbst-Hacken einladen.

Die Komposition umfasst auch Infrastruktur: `/setup-matt-pocock-skills` schreibt die projektspezifische Tracker-Konvention in `docs/agents/issue-tracker.md`. GitHub und lokale Markdown-Issues sind vorgefertigt; GitLab sowie frei beschriebene Systeme wie Jira oder Linear können angebunden werden, ohne die fachlichen Workflow-Skills umzuschreiben. `research` und `prototype` können innerhalb von Wayfinder oder unabhängig davon eingesetzt werden.

## Vorteile

- Einzelne Teile lassen sich leicht anpassen, debuggen oder ersetzen, ohne das Gesamtsystem zu verstehen.
- Kein Vendor-/Framework-Lock-in; funktioniert modellunabhängig.
- Der Mensch behält die Kontrolle über den Ablauf und kann bei Fehlern gezielt eingreifen.

## Nachteile & Grenzen

- Weniger eingebaute Koordination/State-Management als bei schwereren, prozess-eigenen Frameworks.
- Der Gesamtworkflow muss vom Nutzer selbst aus einzelnen Skills zusammengesetzt werden.
- Bietet von sich aus keine Leitplanken, die größere Teams evtl. brauchen, um konsistent zu arbeiten.

## Wann einsetzen, wann nicht

- Einsetzen: Einzelpersonen/kleine Teams, die Kontrolle und Flexibilität über einen vorgegebenen Prozess stellen.
- Nicht einsetzen: Teams, die einen vollständig gemanagten, durchgängig opinionated Ende-zu-Ende-Prozess wollen und dafür bewusst Kontrolle abgeben möchten.

## Belege

- 2026-07-10 · [[2026-07-10-voxyz-mattpocock-skills]] · meinung — Tweet: „the readme sets the boundary up front: skills stay small, composable, easy to hack. control of the process stays with you.“
- 2026-07-11 · external_repos/mattpocock/skills/README.md · verifiziert — README bestätigt wörtlich: „These skills are designed to be small, easy to adapt, and composable. They work with any model.“ sowie die explizite Abgrenzung: „Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve.“
- 2026-07-09 · [[2026-07-09-n3sonline-wayfinder]] · meinung — Unabhängiger Tweet-Beleg: „A lot of other frameworks are HUGE. This one is small.“
- 2026-07-08 · [[2026-07-08-mattpocock-custom-issue-tracker]] · meinung — Matt beschreibt die Tracker-Anbindung als Setup-Aufgabe statt Änderung der Skills.
- 2026-07-08 · [[2026-07-08-mattpocock-skills-v1-1]] · meinung — Release-Ankündigung nennt `research` und `prototype` sowohl als Wayfinder-Unterstützung als auch als eigenständig nutzbar.
- 2026-07-13 · external_repos/mattpocock/skills/skills/engineering/setup-matt-pocock-skills/SKILL.md · verifiziert — Setup dokumentiert Tracker, Triage-Labels und Domain-Docs; GitHub, GitLab, lokale Dateien und frei beschriebene andere Tracker sind vorgesehen.
- 2026-07-13 · external_repos/mattpocock/skills/skills/engineering/research/SKILL.md · verifiziert — `research` ist model-invoked und delegiert Primärquellen-Recherche an einen Hintergrundagenten.
- 2026-07-13 · external_repos/mattpocock/skills/skills/engineering/prototype/SKILL.md · verifiziert — `prototype` ist model-invoked und erzeugt bewusst wegwerfbare Artefakte zur Beantwortung einer Designfrage.
- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/agentskills-best-practices.md (agentskills.io) · meinung — Unabhängige Bestätigung der Größendisziplin mit konkreten Grenzen: `SKILL.md` unter 500 Zeilen/5.000 Tokens, Skills als „coherent units" schneiden — weder zu eng (mehrere Skills müssen für eine Aufgabe laden) noch zu breit (schwer präzise zu aktivieren).
- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/opencode-cloudflare-skill-anatomy.md (D. Mulroy) · meinung — Zeigt, wie Komposition bei großen Domänen (60+ Produkte) skaliert, ohne monolithisch zu werden: Decision-Trees statt flacher Listen, 5-Datei-Struktur pro Produkt (README/api/configuration/patterns/gotchas), Cross-References bewusst nur eine Ebene tief — verschachtelte Ladeketten (`SKILL.md → A.md → B.md`) verwirren das Laden.

## Spannungen & offene Fragen

- Gegenposition zu schwereren Frameworks: `open-gsd/gsd-core` (siehe `external_repos/INDEX.md`) adressiert gezielt „Context Rot“ durch frische Subagent-Kontexte pro Ausführungsschritt und persistente `STATE.md`/`CONTEXT.md` — ein strukturell eingebauter Vorteil, den rein kleine, komponierbare Skills nicht automatisch mitbringen, weil der Nutzer den Gesamtworkflow selbst zusammensetzen muss. Trade-off: Kontrolle & Einfachheit (mattpocock) vs. eingebaute Disziplin gegen Kontext-Verschlechterung (GSD). Offene Frage: Ab welcher Vorhabengröße kippt der Vorteil zugunsten des schwereren, prozess-eigenen Frameworks? Siehe auch [[Workflow-Frameworks]].

## Verwandte Patterns

- [[Skill-Call-Hierarchie]]
- [[One-File-per-Failure-Mode]]
