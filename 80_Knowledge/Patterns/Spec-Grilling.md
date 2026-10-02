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
- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/spec-driven-dev-tip-008.md (M. Contieri) · meinung — Unabhängige Bestätigung als „Interview Method“: „Ask the AI to interview you (e.g., Ask me 10 clarifying questions) to uncover edge cases before drafting the spec“; Rahmung „Waterfall in 15 Minutes“ — 15 Minuten Planung sparen Stunden Debugging.
- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/spec-to-code-velocity-trap.md · meinung — Liefert die Begründung, warum Grilling vor dem Code stattfinden muss: ambige Specs erzeugen „Contextual Debt“ (implizite Annahmen im Fundament, teurer umzukehren als Technical Debt); empfohlener Workflow explizit mit eigenem Schritt: Spec → **Assumption Extraction** → Clarification → Plan → Code → Validation.
- 2026-01-06 · [[2026-01-06-jarrodwatts-context-engineering-guide]] · meinung — Unabhängige Bestätigung aus anderem Themenschwerpunkt (Context Engineering statt Skills): Plan Mode mit gezielten Rückfragen zum Vorhaben, bevor umgesetzt wird.
- 2026-07-30 · [[2026-07-30-julian-ivanov-interaktive-schulungen-mit-claude-code]] · meinung — Überträgt das Interview-Muster auf Kursproduktion: Der Agent klärt Zielgruppe, Vorwissen, Dauer, Sprache und visuellen Stil, bevor er Curriculum und Assets erzeugt.
- 2026-07-21 · [[2026-07-21-promptgefluester-prompt-engineering-ist-tot-und-keiner-hats-gemerkt-was-meine-ich-damit]] · meinung — Rückfrage-Skills (Superpowers Brainstorming, ein im Transkript als „Grammy“ wiedergegebener Skill) sollen den Basis-Kontext erzeugen und Prompt Engineering ersetzen. Reine Praxisaussage, keine Evidenz.
- 2026-09-19 · [[2026-09-19-voxyz_ai-2101355643882065971]] · meinung — Der Requirements-Lead-Prompt stellt die wichtigste Frage zuerst statt eines Fragebogens und mündet in einen eigenständigen Task Brief mit Nicht-Zielen und Done-Kriterien. Nur Prompt-Vorlage, keine Evidenz zur Wirkung.
- 2026-09-25 · [[2026-09-25-trq212-2103576349499855160]] · meinung — Thariq lässt Claude vor der Implementierung zu Spec-Lücken interviewen; mit Interview-Spec konvergieren Ergebnisse über Effort-Stufen, ohne Spec wächst der Umfang eigener Annahmen. Anekdotisch an einer Toy-App, keine Messreihe.
- 2026-08-05 · [[2026-08-05-floknowsai-dein-vibe-coding-projekt-bricht-nicht-am-coding-agent-zusammen-sondern]] · meinung — Architektur, Schnittstellenformate und Fehlerfallverhalten vor der ersten Codezeile festlegen; drei Monate Aufwand für echtes Produktivsystem ist Schätzung des Autors.
- 2026-05-02 · [[2026-05-02-vincentmumme-das-muesst-ihr-unbedingt-testen]] · meinung — Pre-Mortem-Prompt (Projekt ist in 6 Monaten gescheitert) als Gegenmittel gegen Zustimmungsneigung des Agenten bei Ideenbewertung. Unbelegte Einzelerfahrung.
- 2026-07-14 · [[2026-07-14-fredrikharkort-5-prompts-die-weh-tun]] · meinung — Self-Interview und Board-Member-Prompt lassen die KI Widersprüche und unbequeme Themen aufdecken; fünf Prompts, alle aus Entscheidungs- statt Coding-Kontext. Ohne Auswertung.
- 2026-02-03 · [[2026-02-03-god-of-prompt-karpathy-ai-coding-system-prompt]] · meinung — Prompt erzwingt Annahmen-Offenlegung und Anhalten bei Widersprüchen; Sekundärquelle, Wirkung nicht getestet.
- 2026-02-25 · [[2026-02-25-heynavtoor-claude-cowork-setup-guide]] · meinung — Vor der Arbeit `AskUserQuestion` erzwingen, statt zu raten; Sekundärquelle, Büro-Kontext statt Code.
- 2026-07-03 · [[2026-07-03-trq212-2073100352921215386]] · meinung — Interview-Technik: Claude fragt eine Frage nach der anderen, priorisiert nach Architekturwirkung. Nur ein Beispielprompt, keine Evaluation.

## Spannungen & offene Fragen

- Keine bekannt. Die verwandten Umsetzungen (gstack `/office-hours`, Superpowers `brainstorming`) unterscheiden sich im Detail (Design-Doc vs. reines Gespräch), widersprechen sich aber nicht im Grundprinzip.

## Verwandte Patterns

- [[CONTEXT-Glossar]]
- [[One-File-per-Failure-Mode]]
- [[Skill-Call-Hierarchie]]
