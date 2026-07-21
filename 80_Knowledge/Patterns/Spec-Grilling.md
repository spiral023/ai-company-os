# Spec-Grilling

**Konfidenz:** verifiziert

## Zweck

Schließt die Verständigungslücke zwischen Nutzer und Agent, bevor Code oder Inhalt entsteht. Das häufigste Scheitern bei agentischer Arbeit ist nicht schlechte Umsetzung, sondern Umsetzung des Falschen — der Agent hat angenommen statt nachgefragt.

## Funktionsweise

Ein eigener Skill verhört den Nutzer gezielt zu einem Vorhaben, bis jeder Ast des Entscheidungsbaums geklärt ist, bevor überhaupt umgesetzt wird. Der Agent stellt so lange präzisierende Rückfragen, bis die Spezifikation eindeutig ist — statt bei Unklarheit einfach eine plausible Annahme zu treffen und loszulegen. Verwandte Umsetzungen: gstack `/office-hours` (Produktinterview mit gezielten Rückfragen, erzeugt ein Design-Doc), Superpowers `brainstorming` (sokratisches Nachfragen statt sofortigem Coden) — siehe `external_repos/INDEX.md`.

## Vorteile

- Reduziert Fehlbauten und Nacharbeit durch frühzeitig aufgedeckte Fehlannahmen.
- Zwingt auch den Menschen, sein eigenes Vorhaben zu Ende zu denken.
- Funktioniert unabhängig vom Modell, da es reine Gesprächsführung ist.

## Nachteile & Grenzen

- Kostet Zeit/Session-Budget vor dem eigentlichen Start; bei trivialen Änderungen unverhältnismäßig.
- Garantiert nicht automatisch die richtigen Fragen — Qualität hängt von der Skill-Formulierung ab.
- Kann als lästig empfunden werden, wenn der Nutzer schon eine klare, vollständige Vorgabe mitbringt.

## Wann einsetzen, wann nicht

- Einsetzen: zu Beginn nichttrivialer Vorhaben, bei mehrdeutigen oder offen formulierten Aufträgen, bei Features mit vielen Entscheidungsästen.
- Nicht einsetzen: bei trivialen, eindeutig spezifizierten Änderungen oder bereits fertig ausformulierten Tickets.

## Belege

- 2026-07-10 · [[2026-07-10-voxyz-mattpocock-skills]] · meinung — Tweet nennt `/grill-me` als Interview-Skill, der so lange fragt, bis die Spec klar ist.
- 2026-07-11 · external_repos/mattpocock/skills/skills/productivity/grill-me/SKILL.md · verifiziert — Skill `grill-me` existiert im Repo unter `skills/productivity/`; das README beschreibt ihn unter „#1: The Agent Didn't Do What I Want“ explizit als „grilling session — getting the agent to ask you detailed questions about what you're building“, ergänzt um `grill-with-docs` (`skills/engineering/grill-with-docs/SKILL.md`) und den zugrunde liegenden Loop `grilling` (`skills/productivity/grilling/SKILL.md`).
- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/spec-driven-dev-tip-008.md (M. Contieri) · meinung — Unabhängige Bestätigung als „Interview Method": „Ask the AI to interview you (e.g., Ask me 10 clarifying questions) to uncover edge cases before drafting the spec"; Rahmung „Waterfall in 15 Minutes" — 15 Minuten Planung sparen Stunden Debugging.
- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/spec-to-code-velocity-trap.md · meinung — Liefert die Begründung, warum Grilling vor dem Code stattfinden muss: ambige Specs erzeugen „Contextual Debt" (implizite Annahmen im Fundament, teurer umzukehren als Technical Debt); empfohlener Workflow explizit mit eigenem Schritt: Spec → **Assumption Extraction** → Clarification → Plan → Code → Validation.

## Spannungen & offene Fragen

- Keine bekannt. Die verwandten Umsetzungen (gstack `/office-hours`, Superpowers `brainstorming`) unterscheiden sich im Detail (Design-Doc vs. reines Gespräch), widersprechen sich aber nicht im Grundprinzip.

## Verwandte Patterns

- [[CONTEXT-Glossar]]
- [[One-File-per-Failure-Mode]]
- [[Skill-Call-Hierarchie]]
