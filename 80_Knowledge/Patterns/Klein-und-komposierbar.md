# Klein-und-komposierbar

**Konfidenz:** verifiziert

## Zweck

Bewahrt die Kontrolle über den Entwicklungsprozess beim Menschen, statt sie an ein Framework abzugeben. Adressiert das Risiko, dass umfassende, prozess-diktierende Systeme zwar Struktur geben, dabei aber Fehler im Prozess selbst schwer auffindbar und korrigierbar machen.

## Funktionsweise

Jeder Skill wird bewusst klein, leicht anpassbar und modellunabhängig gehalten, statt ihn in ein großes, alles umfassendes Framework einzubetten. Das README des Referenz-Repos setzt diese Grenze explizit: Ansätze wie GSD, BMAD und Spec-Kit „try to help by owning the process", nehmen dabei aber Kontrolle weg und machen Bugs im Prozess schwer auflösbar. Die eigenen Skills sollen stattdessen „small, easy to adapt, and composable" sein, mit jedem Modell funktionieren und explizit zum Selbst-Hacken einladen.

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

- 2026-07-10 · [[2026-07-10-voxyz-mattpocock-skills]] · meinung — Tweet: „the readme sets the boundary up front: skills stay small, composable, easy to hack. control of the process stays with you."
- 2026-07-11 · external_repos/mattpocock/skills/README.md · verifiziert — README bestätigt wörtlich: „These skills are designed to be small, easy to adapt, and composable. They work with any model." sowie die explizite Abgrenzung: „Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve."

## Spannungen & offene Fragen

- Gegenposition zu schwereren Frameworks: `open-gsd/gsd-core` (siehe `external_repos/INDEX.md`) adressiert gezielt „Context Rot" durch frische Subagent-Kontexte pro Ausführungsschritt und persistente `STATE.md`/`CONTEXT.md` — ein strukturell eingebauter Vorteil, den rein kleine, komponierbare Skills nicht automatisch mitbringen, weil der Nutzer den Gesamtworkflow selbst zusammensetzen muss. Trade-off: Kontrolle & Einfachheit (mattpocock) vs. eingebaute Disziplin gegen Kontext-Verschlechterung (GSD). Offene Frage: Ab welcher Vorhabengröße kippt der Vorteil zugunsten des schwereren, prozess-eigenen Frameworks? Siehe auch `80_Knowledge/Vergleiche/Workflow-Frameworks.md`.

## Verwandte Patterns

- [[Skill-Call-Hierarchie]]
- [[One-File-per-Failure-Mode]]
