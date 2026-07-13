# TDD-als-Verifikationshebel

**Konfidenz:** meinung

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

## Spannungen & offene Fragen

- Drei unabhängige Autoren (Matt Pocock, Duncan Ogilvie, Andrej Karpathy) konvergieren unabhängig auf TDD als zentralen Verifikationsmechanismus für Agenten — stützt die Kernaussage über bloße Einzelmeinung hinaus, auch wenn keine kontrollierte Studie vorliegt.
- Offene Frage: Wie lässt sich TDD-Pflicht mit sehr frühen, explorativen Prototyping-Phasen (siehe [[Lovable-Prototyp-dann-lokaler-Handoff]]) vereinbaren, wo noch kein stabiler Prüfpfad existiert?

## Verwandte Patterns

- [[Plan-first-mit-getrenntem-Review]]
- [[Spec-Grilling]]
