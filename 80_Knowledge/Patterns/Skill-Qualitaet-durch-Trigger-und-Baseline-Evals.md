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

## Spannungen & offene Fragen

- ~~Die Quelle bezieht sich auf den offiziellen Anthropic-Skill, wurde aber über eine Sekundärsynthese (vibe-repo-Wiki) bezogen, nicht direkt aus dem geklonten `anthropics/skills`-Repo verifiziert.~~ Erledigt 2026-07-14: direkt in der geklonten SKILL.md verifiziert ([[2026-07-01-anthropic-skill-creator-skill-md]]); die Sekundärsynthese war inhaltlich korrekt.
- Ergänzung 2026-07-14: Die SKILL.md nennt eine wichtige Triggering-Nuance — Claude konsultiert Skills nur bei Aufgaben, die es nicht trivial selbst löst; simple Ein-Schritt-Queries triggern auch bei perfekter Description nicht. Trigger-Evals müssen daher substanzielle Queries verwenden.
- Offene Frage: Wie verhält sich diese Trigger-/Baseline-Disziplin zu unserer eigenen [[Skill-Call-Hierarchie]] — sollte die Aufruf-Klassifizierung (user-invoked/model-invoked) selbst Teil der Trigger-Tests sein?

## Verwandte Patterns

- [[Skill-Call-Hierarchie]]
- [[Klein-und-komposierbar]]
- [[One-File-per-Failure-Mode]]
