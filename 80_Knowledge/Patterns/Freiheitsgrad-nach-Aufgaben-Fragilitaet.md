# Freiheitsgrad-nach-Aufgaben-Fragilitaet

**Konfidenz:** meinung

## Zweck

Verhindert, dass Skill- oder Subagent-Instruktionen unabhängig davon formuliert werden, wie fehleranfällig die gesteuerte Operation ist. Zu vage Anweisungen bei fragilen Operationen (Git, Deployments) erzeugen unzuverlässige Ergebnisse; zu starre Skripte bei robusten, kreativen Aufgaben (Blogposts, Explainer) verschwenden Flexibilität und Kontext, die dort eigentlich hilfreich wäre.

## Funktionsweise

Instruktions-Spezifität wird entlang einer Skala von High Freedom bis Low Freedom an die Fragilität der Operation angepasst: **Prosa-Anweisungen** („Write a report with these sections…“) für robuste Aufgaben mit vielen gültigen Lösungswegen wie Blogposts; **Pseudocode-Muster** („Use this template, adapt as needed“) für mittelfeste Fälle wie Excel-Modelle; **exakte Skripte** („Run this Python file with these args“) für fragile Operationen mit wenig Fehlertoleranz wie Git-Befehle oder Deployments. Die begleitende Faustregel lautet, das **Warum** zu erklären statt nur das **Was**: Versteht das Modell die Logik hinter einer Anweisung, generalisiert es auch auf Grenzfälle, die der Autor nicht vorhergesehen hat. Starre „Tue IMMER X“-Regeln ohne Begründung sind ein Warnsignal für zu wenig erklärte Motivation.

## Vorteile

- Kalibriert Kontextkosten gegen Fehlertoleranz, statt für jede Instruktion denselben Detailgrad zu wählen.
- Das Warum-vor-Was-Prinzip lässt das Modell auf unvorhergesehene Grenzfälle generalisieren, die eine starre Regel nicht abdecken würde.
- Liefert eine konkrete Faustregel für eine sonst rein intuitive Schreibentscheidung beim Bau von Skills und Subagent-Prompts.

## Nachteile & Grenzen

- Unbelegte Autorenmeinung ohne Messung, welche Stufe tatsächlich zu besseren Ergebnissen führt.
- Die Dreiteilung ist eine Heuristik; viele reale Aufgaben liegen zwischen den Stufen und erfordern eigenes Urteil.
- Setzt voraus, dass die Fragilität der Operation korrekt eingeschätzt wird — eine fälschlich als robust eingestufte fragile Operation bekommt zu lockere Anweisungen.

## Wann einsetzen, wann nicht

- Einsetzen: beim Formulieren von `SKILL.md`-Body-Anweisungen oder Subagent-Prompts, wenn die gesteuerte Operation erkennbar unterschiedlich fehlertolerant ist.
- Nicht einsetzen: bei durchgängig gleich fehlertoleranten Aufgaben (rein kreative Skills, rein deterministische Skript-Wrapper) — dort ist die Kalibrierungsfrage bereits durch die Aufgabenart entschieden.

## Belege

- 2026-02-09 · [[2026-02-09-pdrmnvd-how-claude-code-skills-work]] · meinung — X-Artikel von @pdrmnvd beschreibt die Skala High Freedom/Low Freedom (Prosa/Pseudocode/exaktes Skript) und die Warum-vor-Was-Faustregel, mit Verweis auf den offiziellen `skill-creator`-Skill als Lernquelle für reale Umsetzungen.
- 2026-01-31 · [[2026-01-31-bcherny-claude-code-team-tips]] · meinung — Team-Praxis bestätigt die hohe-Freiheit-Seite der Skala konkret: Ein per Slack-MCP kopierter Bug-Thread plus dem Wort „fix“, oder „geh, behebe die CI-Tests“ ohne weitere Detaillierung — Mikromanagement wird explizit als kontraproduktiv benannt, dem Modell wird die Pfadfindung überlassen.
- 2026-09-04 · [[2026-09-04-pvncher-2095991462416490862]] · meinung — Rezeptartige Skill-Anweisungen können ein nuancenfähigeres Modell behindern; Repo-Anweisungen müssen auch für andere Modelle der Contributors passen. Erfahrungsaussage ohne Beleg durch Vergleichstests.
- 2026-09-14 · [[2026-09-14-developers-rethinking-skills-and-prompts-for-gpt-6-astra-op]] · meinung — Bei stärkeren Modellen können überspezifische Skill-Rezepte Ergebnisse verschlechtern; Guidance sollte zum Modell passen. Keine Zahlen, nur Erfahrungsaussage.
- 2026-09-22 · [[2026-09-22-claude-getting-the-most-out-of-opus-5-5-in-claude-and-c]] · meinung — Herstellerleitfaden: Zielzustand plus einzige Stopp-Bedingung statt Schritt-Anweisungen, „think carefully“ streichen. Selbstberichtet, modellspezifisch für Opus 5.5.
- 2026-02-04 · [[2026-02-04-lovable-docs-prompting-debugging]] · meinung — Bei Auth/Payment explizit Vorsicht und Änderungsgrenzen im Prompt; weiche Anweisung ohne harte Absicherung.
- 2026-02-04 · [[2026-02-04-meer-aiit-claude-skills-complete-guide]] · meinung — Strikte Regeln bei fragilen Aufgaben, Spielraum bei kreativen; nur als Faustregel genannt, ohne Beleg.
- 2026-10-01 · [[2026-10-01-julian-ivanov-ki-automat-claude-code-ist-unglaublich-gut-in-motion-graphi]] · meinung — Ziel, Referenzen und Geschmack statt Weg vorgeben; Ergebnis als Code (HyperFrames) statt Pixel, daher gezielt nachbesserbar. Selbstbericht eines Creators, Transkript automatisch erzeugt, keine Messung.
- 2026-07-15 · [[2026-07-15-xudong07452910-2077246527756775933]] · meinung — Fasst die GPT-5.6-Prompt-Guidance als Task-Vertrag zusammen (Ziel, Erfolgskriterium, Pflichtbelege, Stopp-Regel, Bestätigungsaktionen) statt Schrittvorgaben. Stützt den Gradienten bei robusten Aufgaben, sagt aber nichts zu fragilen Operationen; Zweitverwertung ohne Messdaten.

## Spannungen & offene Fragen

- Keine bekannt.

## Verwandte Patterns

- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- [[Klein-und-komposierbar]]
