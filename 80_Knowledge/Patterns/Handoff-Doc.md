# Handoff-Doc

**Konfidenz:** verifiziert

## Zweck

Erhält den Arbeitszustand über das Ende einer Session oder eines Kontextfensters hinaus, damit ein neuer Agent (oder derselbe nach einem Neustart) nahtlos weitermachen kann, statt bei null anzufangen.

## Funktionsweise

Ein Skill komprimiert die laufende Konversation in ein Übergabe-Dokument („Handoff Doc"): die relevanten Entscheidungen, der aktuelle Stand, offene Fragen. Der nächste Agent liest dieses Dokument statt der vollständigen Historie und setzt die Arbeit an derselben Stelle fort. Für Vorhaben, die den Rahmen einer einzelnen Session sprengen, gibt es einen verwandten, aber eigenständigen Mechanismus: eine „Landkarte" aus Untersuchungs-Tickets auf dem Issue-Tracker, die nacheinander abgearbeitet werden, bis der Weg zum Ziel klar ist — statt eines einzelnen Übergabe-Dokuments wird hier der große Auftrag in kleine, session-große Entscheidungs-Häppchen zerlegt. Verwandte Umsetzungen außerhalb des Referenz-Repos: `planning-with-files` (`task_plan.md`/`findings.md`/`progress.md` als persistente Dateien), GSD Core `STATE.md` (überlebt Session-Grenzen) — siehe `external_repos/INDEX.md`.

## Vorteile

- Übersteht Kontextfenster-Limits, `/clear` und Session-Abbrüche.
- Reduziert Einarbeitungskosten für eine neue Session erheblich.
- Macht den Übergabepunkt explizit und nachvollziehbar statt implizit im Gedächtnis des vorherigen Agenten.

## Nachteile & Grenzen

- Verdichtung ist verlustbehaftet: Was ins Handoff-Doc aufgenommen wird, entscheidet, was der nächste Agent weiß — Nuancen können verloren gehen.
- Zusätzlicher Schritt/Overhead, der sich bei kurzen Aufgaben innerhalb einer Session nicht lohnt.
- Für Vorhaben, die viele Sessions brauchen, reicht ein einzelnes Handoff-Doc oft nicht — dafür ist die tickets-basierte Landkarte gedacht (siehe Funktionsweise).

## Wann einsetzen, wann nicht

- Einsetzen: lange Sessions kurz vor dem Kontextlimit, Mehr-Sessions-Vorhaben, geplante Übergaben zwischen Agenten.
- Nicht einsetzen: kurze, in einer Session abschließbare Aufgaben.

## Belege

- 2026-07-10 · [[2026-07-10-voxyz-mattpocock-skills]] · meinung — Tweet beschreibt `/handoff` (Konversation → Übergabe-Dokument) und `/wayfinder` (zu große Arbeit → Ticket-Landkarte).
- 2026-07-11 · external_repos/mattpocock/skills/skills/productivity/handoff/SKILL.md · verifiziert — Skill `handoff` existiert im Repo unter `skills/productivity/`.
- 2026-07-11 · external_repos/mattpocock/skills/skills/engineering/wayfinder/SKILL.md · verifiziert — Skill `wayfinder` existiert unter `skills/engineering/`; Beschreibung bestätigt exakt das Tweet-Motiv „Plan a huge chunk of work — more than one agent session can hold — as a shared map of investigation tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear."

## Spannungen & offene Fragen

- Keine Spannung zu `planning-with-files` oder GSD `STATE.md` bekannt — beide verfolgen dasselbe Grundprinzip (Zustand auf Platte statt im flüchtigen Kontext), mit unterschiedlicher Formatwahl.

## Verwandte Patterns

- [[Skill-Call-Hierarchie]]
