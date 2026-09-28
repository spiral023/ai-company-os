# TDD-als-Verifikationshebel

**Konfidenz:** mehrfach-belegt

## Zweck

Zwingt agentische Umsetzung zu ehrlichem, belegbarem Fortschritt statt spekulativem Code. Adressiert, dass Agenten bei großen generativen Sprüngen leicht in „Wunschdenken“ enden — Code sieht fertig aus, ist aber nicht gegen echtes Verhalten geprüft.

## Funktionsweise

Kontextmenge, Prüfbarkeit und Arbeitspaketgröße bestimmen gemeinsam die Qualität agentischer Arbeit: Kippt einer der drei Faktoren, kippt der Workflow (zu viel Kontext → Drift, fehlende Prüfschritte → Scheinfortschritt, zu große Pakete → spekulativer Code). Verifikation ist dabei der stärkste Hebel — starke Prüfformen sind explizite Testfälle, reproduzierbare Shell-Befehle, erwartete Ausgaben, Screenshots bei UI-Arbeit; schwache Prüfformen sind vage Aufträge wie „mach das sauberer“ oder „fix den Bug“ ohne Fehlerbild. Das robuste TDD-Muster für Agenten: genau **einen** fehlschlagenden Test schreiben → nur minimalen Code ergänzen, damit er grün wird → erst danach aufräumen/abstrahieren. Diese vertikalen Slices („Tracer-Bullets“) verhindern, dass der Agent zuerst eine breite Implementierung fantasiert und die Tests danach passend umformt (horizontal statt vertikal). Gute Tests prüfen Verhalten über öffentliche Schnittstellen, überleben Refactorings und minimieren Mocks; schlechte Tests binden sich an interne Aufrufe oder bestätigen nur Mock-Interaktionen. Für riskante Vorhaben eskaliert die Prüfung: Selbstverifikation → zweite Session → separater Reviewer-Subagent → modellübergreifende Review-Schleife.

## Vorteile

- Erzwingt belegbaren statt behauptetem Fortschritt — ein grüner Test ist ein härterer Nachweis als eine plausible Erklärung.
- Vertikale Slices (ein Test, minimaler Code, dann Refactor) verhindern, dass große spekulative Implementierungen erst hinterher gegen passend gemachte Tests „bestätigt“ werden.
- Die Unterscheidung guter/schlechter Tests (Verhalten vs. Implementierungsdetails) schützt vor Mock-Illusion, bei der alles grün wirkt, aber nur innerhalb künstlicher Testdoubles.

## Nachteile & Grenzen

- TDD als Pflichtdisziplin ist nicht in jedem Tech- oder Prototyping-Kontext gleich praktikabel, besonders bei explorativer oder visueller Arbeit ohne klaren Vorab-Test.
- Setzt voraus, dass überhaupt ein reproduzierbarer Prüfpfad existiert (Tests, Builds, Screenshots) — bei rein qualitativen Aufgaben fehlt diese Grundlage.
- Häufige Fehlmuster bleiben trotz TDD-Disziplin möglich, wenn sie nicht aktiv vermieden werden: Kitchen-Sink-Session, Horizontal Slicing, Symptom-statt-Ursache, Patchen-statt-Neustart.

## Wann einsetzen, wann nicht

- Einsetzen: Aufgaben mit klar definierbarem, automatisiert prüfbarem Verhalten (Bugfixes, Features mit Tests, Refactorings mit Regressionsschutz).
- Nicht einsetzen: rein explorative Prototypen oder Aufgaben ohne sinnvoll definierbaren automatisierten Prüfpfad — dort ersetzen Screenshots/manuelle Prüfung den Test, ohne die Grundidee (Verifikation vor Behauptung) aufzugeben.

## Belege

- 2026-04-17 · [[2026-04-17-wiki-compiler-kontextsteuerung-verifikation-tdd]] · meinung — Wiki-Artikel (synthetisiert aus mehreren X-Posts, aihero.dev, tweag.github.io Agentic Coding Handbook, offizieller Claude-Code-Doku) beschreibt Tracer-Bullets, gute vs. schlechte Tests und die vierstufige Review-Eskalation.
- 2026-02-14 · [[2026-02-14-matt-pocock-skill-tdd-claude-code]] · meinung — Primärquelle (Matt Pocock, aihero.dev) liefert den Begriff „Tracer Bullets“ im Original, konkrete Code-Beispiele für gute vs. schlechte Tests und Planungsfragen vor dem ersten Test (Interface-Änderungen, Deep Modules, Testbarkeit durch Dependency Injection).
- 2026-01-20 · [[2026-01-20-mrexodia-vibe-engineering]] · meinung — Unabhängige Quelle bestätigt: TDD ist für Agenten (anders als laut Autor für Menschen) kein Scam, sondern Goldstandard, weil es eine Feedback-Schleife per Design ist.
- 2026-01-26 · [[2026-01-26-karpathy-coding-workflow-2026]] · meinung — Dritte unabhängige Quelle (Karpathy) beschreibt denselben Mechanismus als Teil von „Leverage“: Tests schreiben und bestehen lassen als deklarative Erfolgskriterien statt imperativer Anweisungen.
- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/addyosmani-agent-skills-blog.md (Addy Osmani, Google) · meinung — Vierte unabhängige Quelle, generalisiert das Prinzip auf Skill-Ebene: „Verification is Non-Negotiable — every skill terminates in concrete evidence. 'Seems right' is never sufficient.“ Ergänzt eine wichtige Nuance über den grünen Test hinaus: „Passing tests are evidence, not proof. Did you check the runtime? Did a human read the diff?“ — und die Praxisregel, „produce evidence“ als harten Exit-Schritt jeder Aufgabe zu definieren (Testlauf, Screenshot, Log oder Review-Approval).
- 2026-01-12 · [[2026-01-12-dhruv1103-lessons-learned-500k-lines-claude-code]] · meinung — Konkrete Werkzeug-Ergänzung: Testcontainers validiert Tests gegen einen echten (Dummy-)Postgres-Container statt gegen Mocks — passt zur bereits belegten Regel, Mocks zu minimieren und Verhalten über echte Schnittstellen zu prüfen, bleibt aber selbst ohne Vorher-Nachher-Zahl.
- 2026-01-14 · [[2026-01-14-ashpreetbedi-claude-code-spec-first]] · meinung — Eine in der `CLAUDE.md` erzwungene Faustregel (Pull-Request-Review unter zehn Minuten) diszipliniert die Arbeitspaketgröße technisch statt nur durch Empfehlung — konkrete Umsetzung des „kleine, prüfbare Pakete“-Prinzips.
- 2026-08-30 · [[2026-08-30-alex-sprogis-loop-graph-engineering-das-letzte-video-was-du-s]] · meinung — Konkrete Regel „jeder Test muss einmal rot gewesen sein“ (Erwartung umdrehen, Fehlschlag bestätigen, wiederherstellen) gegen wirkungslose Tests und Reward Hacking; Prüfszenarien vor der Umsetzung geschrieben und dem Entwickler-Agent verborgen. Selbstberichtet.
- 2026-08-14 · [[2026-08-14-floknowsai-ueber-achtzig-prozent-des-codes-von-claude-code-und-codex-sieht-kein]] · meinung — Test pro geändertem Verhalten, Refactoring muss unter unveränderten Tests grün bleiben; keine Messung, nur Regel.
- 2026-02-03 · [[2026-02-03-svpino-claude-code-md-tips]] · meinung — Bugfix nur nach reproduzierendem Test, als CLAUDE.md-Regel formuliert. Sekundärquelle, keine Messung.
- 2026-02-04 · [[2026-02-04-tweag-tdd-agentic-coding]] · meinung — Sekundärquelle des Tweag-Handbuchs: Test als präziser Prompt, ein Verhalten pro Prompt, Refactoring nur bei grünen Tests. Deckt sich mit dem Bestand; kein Messwert.

## Spannungen & offene Fragen

- Vier unabhängige Autoren (Matt Pocock, Duncan Ogilvie, Andrej Karpathy, Addy Osmani — Stand 2026-07-14) konvergieren unabhängig auf TDD/Verifikation als zentralen Mechanismus für Agenten — stützt die Kernaussage über bloße Einzelmeinung hinaus, auch wenn keine kontrollierte Studie vorliegt.
- Spannung 2026-07-14 (Osmani): Grüne Tests allein können selbst zur Scheinverifikation werden („evidence, not proof“) — der Agent kann Tests passend machen. Konsequenz: Runtime-Check und menschlicher Diff-Read bleiben Teil der Eskalationskette, TDD ersetzt sie nicht.
- Offene Frage: Wie lässt sich TDD-Pflicht mit sehr frühen, explorativen Prototyping-Phasen (siehe [[Lovable-Prototyp-dann-lokaler-Handoff]]) vereinbaren, wo noch kein stabiler Prüfpfad existiert?

## Verwandte Patterns

- [[Plan-first-mit-getrenntem-Review]]
- [[Spec-Grilling]]
- [[Anti-Rationalization-Tables]]
