# Ralph-Loop-Frischer-Kontext-pro-Iteration

**Konfidenz:** meinung

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

## Spannungen & offene Fragen

- Beide Ralph-Loop-Quellen stammen vom selben Autor (@d4m1n) — Konfidenz bleibt bei „meinung“, bis eine unabhängige Zweitquelle oder eigene Erfahrung hinzukommt. Die Docker-Sandbox-Quelle ist zwar vom selben Autor, behandelt aber ein technisch eigenständiges Thema (Isolation statt Kontextmanagement).
- Bezug zu GSDs `STATE.md`-Mechanik (bereits in [[Handoff-Doc]] erwähnt) und zu [[Kontext-Hygiene-Entscheidungsbaum]]: Ralph Loop geht über beide hinaus, indem es *jede* Iteration komplett neu startet statt nur bei Bedarf zu kompaktieren/zu wechseln — offene Frage, ab welcher Aufgabengröße sich der volle Ralph-Loop-Overhead gegenüber einem einzelnen gut geführten Handoff lohnt.

## Verwandte Patterns

- [[Handoff-Doc]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Task-basierte-Steuerung]]
