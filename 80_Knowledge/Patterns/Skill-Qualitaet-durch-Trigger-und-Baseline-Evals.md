# Skill-Qualitaet-durch-Trigger-und-Baseline-Evals

**Konfidenz:** verifiziert

## Zweck

Behandelt Skills als messbare Produkte statt als Dateien mit Frontmatter, die nach Gefühl bewertet werden. Adressiert typische Fehler beim Skill-Bau: Skills werden zu früh geschrieben, Trigger-Beschreibungen sind zu vage (Skill wird zu selten oder falsch aktiviert), und die Iteration endet nach dem ersten brauchbaren Entwurf.

## Funktionsweise

Der Lebenszyklus eines Skills läuft über: Ziel/Scope klären → Entwurf schreiben → 2-3 realistische Testprompts definieren → dieselben Prompts mit UND ohne Skill fahren (Baseline-Vergleich) → auswerten, ob der Skill wirklich etwas verbessert oder nur Tokens kostet → iterativ verbessern → erneut testen. Innerhalb eines Skills gilt Progressive Disclosure: Metadaten (Name, Beschreibung) sind immer sichtbar, der `SKILL.md`-Body wird erst bei Aktivierung geladen, weitere Ressourcen (`scripts/`, `references/`, `assets/`) nur bei tatsächlichem Bedarf. Die `description` ist der primäre Trigger-Mechanismus — da Modelle Skills eher untertriggern als übertriggern, sollte sie bewusst klar und „pushig“ formulieren, was der Skill tut, wann er relevant ist, und ähnliche Formulierungen/Kontexte mit abdecken. Wiederholt neu geschriebene Hilfslogik in Testläufen ist ein Signal, sie als deterministisches Skript in `scripts/` zu bündeln statt sie dem Modell immer wieder neu erfinden zu lassen. Should-trigger- und should-not-trigger-Fälle werden als eigene Qualitätsdimension explizit getestet.

## Vorteile

- Der Baseline-Vergleich (mit/ohne Skill) macht sichtbar, ob ein Skill wirklich etwas verbessert, statt seinen Nutzen anzunehmen.
- Der explizite Fokus auf Trigger-Qualität adressiert einen Fehlermodus, der sonst leicht übersehen wird: ein inhaltlich guter Skill, der einfach zu selten aktiviert wird.
- Bundled Scripts für wiederholt neu erfundene Hilfslogik reduzieren Tokenverbrauch und Inkonsistenz gegenüber wiederholter Modellgenerierung derselben Logik.

## Nachteile & Grenzen

- Der volle Evaluationsprozess (Testprompts, Baseline, Benchmarking) ist aufwendig und lohnt sich nicht für jeden kleinen, einmaligen Skill.
- Quantitative Metriken helfen nur, wenn die Eval-Prompts und Assertions sinnvoll gewählt sind — schlecht gewählte Testfälle täuschen Sicherheit vor.
- Dogmatische Anwendung des vollen Prozesses kann bei kleinen, explorativen Skills mehr Prozess als Nutzen erzeugen.

## Wann einsetzen, wann nicht

- Einsetzen: Skills, die wiederkehrend im Team genutzt werden sollen und bei denen falsches oder ausbleibendes Triggern teuer wäre.
- Nicht einsetzen: sehr kleine Einmal-Skills oder rein subjektive Kreativ-Skills ohne klar prüfbares Ergebnis — dort reicht ein einfacherer, iterativer Entwurf ohne vollen Eval-Prozess.

## Belege

- 2026-04-16 · [[2026-04-16-wiki-compiler-skill-creator-skill]] · meinung — Wiki-Artikel (Quelle: offizieller `skill-creator`-Skill im Repo `anthropics/skills`) beschreibt Baseline-Vergleich, Trigger-Optimierung, Progressive Disclosure innerhalb eines Skills und Bundled Scripts.
- 2026-07-14 · external_repos/anthropics/skills/skills/skill-creator/SKILL.md · verifiziert — Direkte Lektüre bestätigt alle Aussagen und ergänzt Details: Benchmarking mit Varianzanalyse (Pass-Rate/Zeit/Tokens, Mittelwert ± Stddev vs. Baseline), automatisierter Description-Optimierungsloop (60/40 Train/Test-Split, 3 Läufe pro Query, bis 5 Iterationen, Auswahl nach Test-Score), Blind-Vergleich zweier Skill-Versionen, Packaging als `.skill`-Datei. Siehe [[2026-07-01-anthropic-skill-creator-skill-md]].
- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/agentskills-best-practices.md (agentskills.io) · meinung — Ergänzt harte Budgets und Iterationsregeln: `SKILL.md` unter 500 Zeilen und 5.000 Tokens (Detailmaterial nach `references/` auslagern); Skills als „coherent units“ schneiden (weder zu eng noch zu breit); Gotchas-Regel: „When an agent makes a mistake you have to correct, add the correction to the gotchas section“ — einer der direktesten iterativen Verbesserungswege; Skills aus echten Incident-Reports schlagen generische Artikel.
- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/agentskills-using-scripts.md (agentskills.io) · meinung — Vertieft die Bundled-Scripts-Regel: keine interaktiven Prompts (Agent-Shell hängt sonst), `--help` als primäre Schnittstellendoku, strukturierte Ausgabe (JSON/CSV an stdout, Diagnostik an stderr), Idempotenz („create if not exists“), Versionen pinnen, PEP-723-Inline-Dependencies mit `uv run`.
- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/opencode-agent-skills-practical-guide.md (JP Caparas) · meinung — Ergänzt Testmethodik: Zwei-Instanzen-Ansatz — Instanz A schreibt/verfeinert den Skill, Instanz B validiert ihn mit frischem Kontext an realen Aufgaben; Description muss *was* UND *wann* enthalten, mit spezifischen Trigger-Keywords.
- 2026-02-09 · [[2026-02-09-pdrmnvd-how-claude-code-skills-work]] · meinung — Unabhängige Bestätigung des Drei-Ebenen-Ladesystems (Layer 1 Name+Description ~100 Wörter immer im Kontext, Layer 2 `SKILL.md`-Body bei Trigger, Layer 3 Referenzen/Skripte/Assets unbegrenzt on-demand) und der zwei Aktivierungswege (Slash-Command, automatischer Description-Match); verweist auf den offiziellen `skill-creator`-Skill als beste Lernquelle für reale Umsetzungen.
- 2026-01-21 · [[2026-01-21-tempoimmaterial-agent-skills-vs-rules-vs-commands]] · meinung — Benennt vier konkrete Skill-Fehlermodi mit einprägsamen Namen: The Encyclopedia (zu lang, nicht in `references/` zerlegt), The Everything Bagel (gehört als Rule/Repo-Konvention, nicht als Skill), The Secret Handshake (Description zu abstrakt, wird nie geladen), The Fragile Skill (Spezifika direkt im Skill statt ausgelagert).
- 2026-01-21 · [[2026-01-21-meta-alchemist-claude-skills-deep-dive]] · meinung — Negatives Vergleichsbeispiel für die Beleg-Qualität: Ein selbstberichteter Vendor-Benchmark (57,8 %→94,3 %, +36,4 Punkte im Schnitt) nutzt zwar eine Sechs-Modelle-Jury statt reinem Selbsturteil, bleibt aber ohne Angaben zu Stichprobengröße, Testfällen oder Varianz deutlich unter dem hier bereits verifizierten `skill-creator`-Standard (Mittelwert ± Stddev, 60/40-Split, mehrere Läufe) — zusätzlich ist die einzige Quelle für die „Skilled“-Variante das eigene Repo des Autors.
- 2026-06-04 · [[2026-06-04-agenticjames-most-people-have-not-touched-the-best-parts-of-claude-code-skills-forked]] · meinung — Empfiehlt imperative Descriptions („You must use this skill when …“) plus explizite Trigger-Wörter für zuverlässigeres Auslösen. Keine Messung der Trigger-Rate, also Erfahrungsregel statt Eval-Beleg.
- 2026-09-04 · [[2026-09-04-pvncher-2095991462416490862]] · meinung — Beschreibt, dass Skill-Descriptions dauerhaft im Context liegen und bei Überfüllung gekürzt werden, und zeigt ein Bad/Good-Paar (Datenbank-Themenfeld vs. Migrations-Trigger). Selbstberichtete Praxis ohne Eval-Messung.
- 2026-09-07 · [[2026-09-07-sairahul1-2096902575035683147]] · meinung — Skill-Beschreibungen sollen nur Auslösebedingungen nennen, zu viele Skills kürzen die Beschreibungen und führen zur Fehlwahl; Prompt-Rewrites sind an echten Aufgaben zu vergleichen. Erfahrungsaussage ohne Zahlen.
- 2026-09-14 · [[2026-09-14-developers-rethinking-skills-and-prompts-for-gpt-6-astra-op]] · meinung — OpenAI empfiehlt kurze Skill-Beschreibungen mit engem Auslöser (Migration statt alles mit Datenbank) und nennt automatische Kürzung bei zu vielen Skills als Fehlerquelle; ohne Eval oder Messung, reine Herstellerempfehlung.
- 2026-02-11 · [[2026-02-11-rohit4verse-guide-building-agent-skills]] · meinung — Erfolgskriterien vor dem Bau (Trigger-Quote über 90 %, Tool-Effizienz, Konsistenz); Zielwerte ohne Messgrundlage.
- 2026-08-21 · [[2026-08-21-promptgefluester-wie-macht-man-refactering-bei-einer-richtig-grossen-code-base-mit-aeh]] · meinung — Refactoring-Skill vor Einsatz mit 3 bis 4 Testszenarien und Analyseläufen prüfen. Selbstberichtet, ohne Kriterien.
- 2026-09-14 · [[2026-09-14-code-test-plugins-with-evals-claude-code-docs]] · meinung — Offizielles Tooling `claude plugin eval` mit No-Plugin-Baseline, tool_used-Grader und CI-Threshold; Herstellerdoku, Datum unsicher, Judge-Läufe kosten Nutzung.
- 2026-02-04 · [[2026-02-04-meer-aiit-claude-skills-complete-guide]] · meinung — Bestätigt Trigger-Logik in der Description statt im Body und Progressive Disclosure; Sekundärquelle, kaum Neues gegenüber Bestand.
- 2026-02-09 · [[2026-02-09-tom-crawshaw-claude-code-insights-guide]] · meinung — Vorgeschlagener Agent optimiert Skills mit generierten Testszenarien, bis alle bestehen. Nur Vorschlag, kein gezeigtes Ergebnis.

## Spannungen & offene Fragen

- ~~Die Quelle bezieht sich auf den offiziellen Anthropic-Skill, wurde aber über eine Sekundärsynthese (vibe-repo-Wiki) bezogen, nicht direkt aus dem geklonten `anthropics/skills`-Repo verifiziert.~~ Erledigt 2026-07-14: direkt in der geklonten SKILL.md verifiziert ([[2026-07-01-anthropic-skill-creator-skill-md]]); die Sekundärsynthese war inhaltlich korrekt.
- Ergänzung 2026-07-14: Die SKILL.md nennt eine wichtige Triggering-Nuance — Claude konsultiert Skills nur bei Aufgaben, die es nicht trivial selbst löst; simple Ein-Schritt-Queries triggern auch bei perfekter Description nicht. Trigger-Evals müssen daher substanzielle Queries verwenden.
- Ergänzung 2026-07-14 (Quelle: Addy Osmani, external_knowledge/ai-llm-wiki/raw/addyosmani-agent-skills-blog.md): Neben Trigger- und Baseline-Qualität eine dritte Dimension — **Anti-Rationalization-Tables**: Jede Skill listet typische Ausreden, mit denen ein Agent den Workflow überspringen würde, plus vorformulierte Gegenargumente („pre-written rebuttals to lies the agent hasn't yet told“). Seit 2026-07-14 eigenes Pattern: [[Anti-Rationalization-Tables]].
- Offene Frage: Wie verhält sich diese Trigger-/Baseline-Disziplin zu unserer eigenen [[Skill-Call-Hierarchie]] — sollte die Aufruf-Klassifizierung (user-invoked/model-invoked) selbst Teil der Trigger-Tests sein?

## Verwandte Patterns

- [[Skill-Call-Hierarchie]]
- [[Klein-und-komposierbar]]
- [[One-File-per-Failure-Mode]]
