# Anti-Rationalization-Tables

**Konfidenz:** verifiziert

## Zweck

Verhindert, dass ein Agent (oder ein müder Engineer) einen vorgeschriebenen Workflow mit einer plausibel klingenden Begründung überspringt. LLMs sind exzellent im Rationalisieren — sie produzieren überzeugende Absätze, warum genau diese Aufgabe ausnahmsweise keine Spec, keinen Test oder keine Verifikation braucht. Das Pattern adressiert diesen Fehlermodus präventiv statt reaktiv.

## Funktionsweise

Jede Skill (oder jeder Workflow) enthält eine Tabelle mit zwei Spalten: links die typischen Ausreden, mit denen der Workflow übersprungen würde, rechts die vorformulierte Widerlegung. Beispiele aus der Praxis: „This task is too simple to need a spec." → „Acceptance criteria still apply. Five lines is fine. Zero lines is not." / „I'll write tests later." → „Later is the load-bearing word. There is no later." / „Tests pass, ship it." → „Passing tests are evidence, not proof." Die Widerlegungen sind „pre-written rebuttals to lies the agent hasn't yet told" — sie stehen bereits im Kontext, wenn die Rationalisierung entsteht, statt erst nach dem Fehler nachgereicht zu werden. Die Tabelle wird iterativ gepflegt: Jede real beobachtete Ausrede, die zum Überspringen geführt hat, wird als neue Zeile ergänzt (analog zur Gotchas-Regel in [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]). Das Muster funktioniert ausdrücklich auch für menschliche Teams: „Write down the lies your team tells itself. Pair each with the rebuttal."

## Vorteile

- Fängt den Fehlermodus an seiner Wurzel: Die Widerlegung ist schon im Kontext, bevor die Rationalisierung formuliert wird.
- Billig umzusetzen (eine Markdown-Tabelle) und iterativ verbesserbar aus real beobachteten Ausreden.
- Doppelt nutzbar: dieselbe Tabelle diszipliniert Agenten und dokumentiert Team-Anti-Patterns für Menschen.

## Nachteile & Grenzen

- Wirkt nur gegen bekannte, bereits aufgeschriebene Ausreden — neue Rationalisierungsvarianten erfordern Pflege.
- Verbraucht Tokens in jeder Skill-Aktivierung; bei sehr langen Tabellen konkurriert das mit dem Skill-Budget (siehe 500-Zeilen/5k-Token-Grenze in [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]).
- Ersetzt keine harte Verifikation: Die Tabelle senkt die Wahrscheinlichkeit des Überspringens, erzwingt aber nichts — deterministische Gates (Hooks, CI) bleiben die härtere Schicht (siehe [[Erweiterungs-Ebenen-Zuordnung]]).

## Wann einsetzen, wann nicht

- Einsetzen: in disziplin-tragenden Skills, deren Wert genau darin liegt, nicht übersprungen zu werden (TDD, Spec-Pflicht, Review-Gates, Debugging-Methodik).
- Nicht einsetzen: in rein informativen Referenz-Skills ohne Workflow-Charakter — dort gibt es nichts zu überspringen, die Tabelle wäre totes Gewicht.

## Belege

- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/addyosmani-agent-skills-blog.md (Addy Osmani, Google) · meinung — Primärbeschreibung des Patterns als eines von fünf Kernprinzipien, mit den drei Beispielzeilen und der Begründung „LLMs are excellent at rationalisation"; empfiehlt es explizit auch als Team-Praxis.
- 2026-07-14 · external_repos/addyosmani/agent-skills/skills/ · verifiziert — 22 der Skills im geklonten Repo enthalten eine solche Tabelle; z. B. `test-driven-development/SKILL.md` („Common Rationalizations": „I'll write tests after the code works" → „You won't. And tests written after the fact test implementation, not behavior.").
- 2026-07-14 · external_repos/obra/superpowers/skills/ · verifiziert — Unabhängige zweite Umsetzung (anderer Autor, Jesse Vincent): `test-driven-development/SKILL.md` enthält eine „Common Rationalizations"-Tabelle (Excuse/Reality) plus Red-Flag-Liste („Rationalizing ‚just this once'"); auch `using-superpowers` und `systematic-debugging` nutzen das Muster.

## Spannungen & offene Fragen

- Gegenposition implizit bei [[Klein-und-komposierbar]]: Jede zusätzliche Disziplin-Tabelle macht Skills länger und „prozess-eigener" — der mattpocock-Ansatz setzt eher auf kleine Skills ohne eingebaute Selbstverteidigung. Offene Frage: Ab welcher Skill-Kritikalität lohnt die Tabelle den Token-Overhead?
- Offene Frage: Wirkt die Tabelle messbar? Ein Baseline-Eval (Skill mit vs. ohne Anti-Rationalization-Tabelle, gleiche Aufgaben) nach [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]] steht aus.

## Verwandte Patterns

- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- [[One-File-per-Failure-Mode]]
- [[TDD-als-Verifikationshebel]]
- [[Erweiterungs-Ebenen-Zuordnung]]
