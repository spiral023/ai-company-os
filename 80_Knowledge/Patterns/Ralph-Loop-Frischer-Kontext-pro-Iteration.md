# Ralph-Loop-Frischer-Kontext-pro-Iteration

**Konfidenz:** mehrfach-belegt

## Zweck

Umgeht die Hauptschwäche langer, autonomer Agent-Sessions: Kontextsättigung und schleichende Qualitätsdegradation über viele aufeinanderfolgende Schritte hinweg. Zielt speziell auf lange, weitgehend unbeaufsichtigte Läufe (Nachtläufe, große Migrationspakete, MVP-Bau mit vielen kleinen Tasks), nicht auf einzelne interaktive Sessions.

## Funktionsweise

Jede Iteration eines Laufs startet mit vollständig frischem Kontext statt einer wachsenden Chat-Historie. Der Arbeitszustand liegt stattdessen in Dateien und Git-Commits — das Gedächtnis wird aus dem Modell in Dateisystem und Versionierung verlagert. Typischer Zyklus pro Iteration: nächste priorisierte Aufgabe auswählen → relevante Spezifikation lesen → Änderung implementieren → Tests ausführen → Ergebnis committen → nächste Iteration mit erneut frischem Kontext. Der operative Speicher liegt in einer festen Verzeichnisstruktur (z.B. `.agent/` mit `PROMPT.md`, `SUMMARY.md`, `STEERING.md`, `tasks.json`, `tasks/`, `prd/`, `logs/`). Steering erfolgt über Dateiänderungen (insbesondere eine `STEERING.md`) statt über ein Unterbrechen des Laufs — Prioritäten lassen sich so verschieben, ohne den gesamten Prozess anzuhalten. Voraussetzung für sinnvollen Einsatz: ein brauchbarer Projekt-Scaffold, echte oder realistische Verifikationspfade (installierte Tests), ein klares PRD und Secrets ausschließlich in `.env`. Ohne harte Prüfschritte halluziniert der Loop Fortschritt, statt ihn zu belegen.

## Vorteile

- Umgeht Context Rot strukturell, weil kein wachsender Chatverlauf mitgeschleppt wird — jede Iteration beginnt „sauber“.
- Zustand in Dateien/Git macht Fortschritt jederzeit inspizierbar und nachvollziehbar, auch für einen Menschen, der den Lauf zwischendurch prüft.
- Steering über eine Datei erlaubt Kurskorrekturen, ohne den Lauf zu unterbrechen oder neu starten zu müssen.

## Nachteile & Grenzen

- Funktioniert nur mit echten, automatisierten Verifikationspfaden (Tests, Builds) — ohne diese halluziniert der Agent belegten Fortschritt.
- Schwach bei pixelgenauer UI-/Interaktionsarbeit, neuartigen Architekturentscheidungen, hochsicherheitskritischem Code und generell Aufgaben mit viel implizitem Fachurteil und wenig automatisierbarer Verifikation.
- Erfordert vorab sauber vorbereitete Eingangslage (Scaffold, PRD, Tests) — bei unklaren Anforderungen produziert der Loop mechanisch, aber am falschen Ziel vorbei.

## Wann einsetzen, wann nicht

- Einsetzen: viele kleine bis mittlere, klar prüfbare Aufgaben mit echtem Testsetup — Boilerplate, Migrationen, repetitive Refactorings, MVP-Bau mit klaren PRDs, Nachtläufe.
- Nicht einsetzen: Aufgaben mit hohem implizitem Fachurteil, neuartigen Architekturentscheidungen, sicherheitskritischem Code oder fehlendem automatisierten Prüfpfad.

## Belege

- 2026-04-17 · [[2026-04-17-wiki-compiler-ralph-loop]] · meinung — Wiki-Artikel (Quelle: einzelner X-Post @d4m1n) beschreibt den `.agent/`-Verzeichnisaufbau, den Iterationszyklus und die Steering-über-Datei-Praxis.
- 2026-02-23 · [[2026-02-23-d4m1n-ralph-loop-setup-primaer]] · meinung — Primärquelle desselben Autors liefert konkrete Nutzungsdaten (37 Stunden Dauerlauf, 250 Aufgaben aus einem 2.000-Zeilen-PRD, AFK abgeschlossen) und das vollständige Setup (Bootstrapping, `prd-creator`-Skill, Review-Pflicht der generierten Aufgabenspezifikation vor dem Lauf).
- 2026-02-05 · [[2026-02-05-d4m1n-docker-sandboxes]] · meinung — Ergänzt die sicherheitstechnische Voraussetzung: Docker Sandboxes (`docker sandbox run claude .`) isolieren den Lauf in einer Micro-VM, damit YOLO-Modus/Ralph-Loop-Läufe über Nacht laufen können, ohne das Host-System zu gefährden.
- 2026-06-01 · external_knowledge/ai-llm-wiki/raw/i-chose-a-good-harness.md (Gentle-AI) · meinung — Unabhängige Bestätigung des Kernprinzips durch anderen Autor und anderes System: Spec-Driven Development als „break a feature into discrete phases, give each phase its own agent with its own context, and persist artifacts between them via Engram (a SQLite-backed memory layer)“ — frischer Kontext pro Phase, Zustand außerhalb des Modells persistiert (dort SQLite statt Dateien/Git).
- 2026-06-09 · external_knowledge/ai-llm-wiki/raw/not-every-codebase-deserves-loops.md (Mark, Limestone Digital) · meinung — Wichtige Gegenposition für Brownfield: „Your legacy codebase is the actual prompt.“ Ein Loop shippte vier Features, die alle ein zu deprecatendes Security-Pattern replizierten, weil das alte Muster in 40+ Dateien dominierte und das neue nur in 6 — der Loop lernt das dominante Muster, nicht das gewollte.
- 2026-01-23 · [[2026-01-23-nummanali-claude-task-system]] · meinung — Verwandter, aber nativer Plattform-Mechanismus für die Zustandspersistenz-Hälfte desselben Grundgedankens: Jeder Claude-Code-Task ist eine eigene JSON-Datei unter `~/.claude/tasks/<list-id>/`, git-versionierbar und über `CLAUDE_CODE_TASK_LIST_ID` session-übergreifend persistent — anders als beim bewusst gebauten `.agent/`-Verzeichnisaufbau hier eine eingebaute Plattform-Funktion. Bestätigt nicht den Aspekt „frischer Kontext pro Iteration“ (nicht Teil der Quelle), nur die Zustand-in-Dateien-Hälfte des Prinzips.
- 2026-08-30 · [[2026-08-30-alex-sprogis-loop-graph-engineering-das-letzte-video-was-du-s]] · meinung — Erweitert das Loop-Muster um vier Typen (turn-, goal-, time-based, proaktiv) mit Ja/Nein-Erfolgskriterium und Iterationslimit sowie Artefakt-Übergaben zwischen Loops mit frischem Kontext. Rein selbstberichtet, ohne Messwerte.
- 2026-02-23 · [[2026-02-23-elvis-openclaw-codex-agent-swarm]] · meinung — Beschreibt eine proaktive Variante, in der ein Orchestrator selbst Arbeit findet (Sentry, Meeting-Notizen, Git-Log) und nach Fehlschlag den Prompt anpasst. Selbstberichtet; kein Beleg für Qualität der Ergebnisse.
- 2026-01-15 · [[2026-01-15-avasdr34m-its-not-easy-but-it-is-simple-kontext-nutzung-in-claude-code-entscheidet]] · meinung — Bash-Schleife über Aufgabenliste mit frischer Session je Aufgabe; Selbstbehauptung ohne Messung.
- 2026-07-03 · [[2026-07-03-calebwritescode-loop-engineering-explained-in-7-min-and-simplified]] · meinung — Ordnet Harness als Task-Schleife außerhalb des Context Window ein; Loop Engineering als Selbst-Anstoß darüber. Nutzen laut Autor unbewiesen.
- 2026-05-18 · [[2026-05-18-agenticjames-using-goal-with-a-task-management-system-is-the-most-overpowered-way-to]] · meinung — Loop bis Zielerreichung mit vorgegebener Prozedur; anders als beim Ralph Loop wird nichts zum Kontext-Reset gesagt, Kosten und Abbruchkriterium fehlen.
- 2026-07-03 · [[2026-07-03-emanueledpt-2073013891752251574]] · meinung — Loop-Variante mit Prompt-Schärfung durch ein stärkeres Modell vorab; kein Beleg für frischen Kontext pro Iteration.
- 2026-06-08 · [[2026-06-08-mvanhorn-2063865685558903149]] · meinung — Ordnet Ralph Loop als Stufe drei einer Lineage (ReAct, AutoGPT, Ralph, `/goal`, Orchestrierungs-Loop) ein und nennt drei harte Stopps (max. Iterationen, Stillstandserkennung, Budget). Einschränkung: Kompilat mit Eigenwerbung, Zahlen zitiert und nicht geprüft.
- 2026-07-01 · [[2026-07-01-0xcodila-2072329149520232639]] · meinung — Nennt State-Datei (Erledigt/Gescheitert/Nächstes) und harte Stop-Bedingung („nach N Versuchen stoppen und berichten“) als Pflichtteile eines Loops. Dazu ein Vier-Punkte-Eignungstest (wöchentlich wiederkehrend, automatisierte Verifikation, Token-Budget, echte Tools).
- 2026-07-06 · [[2026-07-06-claudedevs-2074208949205881033]] · meinung — Offizielle Claude-Code-Taxonomie von Loops (turn-, goal-, time-based, proactive) mit Stop-Kriterium je Typ; `/goal` nutzt ein Evaluator-Modell und Turn-Cap als herstellerseitiges Pendant zur Shell-Schleife. Selbstberichtet, keine Messdaten; frischer Kontext pro Iteration wird nicht thematisiert.

## Spannungen & offene Fragen

- ~~Beide Ralph-Loop-Quellen stammen vom selben Autor (@d4m1n) — Konfidenz bleibt bei „meinung“, bis eine unabhängige Zweitquelle oder eigene Erfahrung hinzukommt.~~ Erledigt 2026-07-14: Gentle-AI (anderer Autor, anderes System) bestätigt das Kernprinzip „frischer Kontext pro Phase + externe Zustandspersistenz“ unabhängig → mehrfach-belegt. Die d4m1n-spezifische `.agent/`-Verzeichnisstruktur bleibt Einzelmeinung.
- Ergänzung 2026-07-14: Die Brownfield-Gegenposition (Limestone Digital) verschärft „Wann nicht einsetzen“: In Legacy-Codebasen mit bekannten Anti-Patterns repliziert der Loop das dominante (falsche) Muster — vor einem Loop-Lauf müssen deprecated Patterns explizit in Steering/PRD ausgeschlossen werden.
- Bezug zu GSDs `STATE.md`-Mechanik (bereits in [[Handoff-Doc]] erwähnt) und zu [[Kontext-Hygiene-Entscheidungsbaum]]: Ralph Loop geht über beide hinaus, indem es *jede* Iteration komplett neu startet statt nur bei Bedarf zu kompaktieren/zu wechseln — offene Frage, ab welcher Aufgabengröße sich der volle Ralph-Loop-Overhead gegenüber einem einzelnen gut geführten Handoff lohnt.

## Verwandte Patterns

- [[Handoff-Doc]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Task-basierte-Steuerung]]
