# Skill-Schwellenwert-institutionelles-Wissen

**Konfidenz:** meinung

## Zweck

Verhindert, dass nützliche, wiederkehrende Automatisierung implizites Einzelwissen einer Person bleibt, statt zu geteiltem Teamwissen zu werden. Adressiert die Lücke zwischen „ich habe dafür ein persönliches Skript“ und „das Team nutzt dafür einen Skill“.

## Funktionsweise

Faustregel für den Zeitpunkt der Skill-Erstellung: Alles, was mehr als einmal am Tag getan wird, wird ein Skill statt eine wiederholte manuelle Aktion zu bleiben. Der eigentliche Hebel liegt aber nicht in der Erstellung selbst, sondern im Git-Check-in: Ein Skill, der ins Repository eingecheckt ist, wird dadurch zu geteiltem Team-Wissen statt zum persönlichen Werkzeug einer einzelnen Person — jeder, der das Repo checkt, bekommt den Skill automatisch mit. Konkretes Beispiel: ein eingecheckter BigQuery-Skill für Analytics-Abfragen lässt einen Praktiker seit über sechs Monaten keine Zeile SQL mehr selbst schreiben; der eigentliche Vorteil dabei ist nicht, dass das Modell SQL beherrscht, sondern dass man im eigenen fachlichen Kontext (Produktfrage) bleibt, während der Skill die Übersetzungsschicht in die technische Syntax übernimmt.

## Vorteile

- Klare, leicht anwendbare Schwelle („>1x/Tag“) statt einer vagen Einschätzung, wann sich ein Skill lohnt.
- Git-Check-in verwandelt individuelle Automatisierung in kumulatives Team-Wissen, ohne zusätzlichen Verteilungsaufwand.
- Verschiebt den fachlichen Fokus vom Erlernen einer Syntax (z. B. SQL) zurück auf die eigentliche Fragestellung.

## Nachteile & Grenzen

- Die 1x/Tag-Schwelle ist eine unbelegte Faustregel ohne Messung, ob sie tatsächlich die richtige Grenze markiert.
- Setzt eine Repo-/Skill-Infrastruktur voraus, in die sich ein Skill sinnvoll einchecken lässt — ohne diese Infrastruktur bleibt der Vorteil theoretisch.
- Ein einmal eingechecktes, aber veraltetes Skill kann falsches Wissen genauso team-weit verbreiten wie richtiges — Pflegeverantwortung wird nicht automatisch mitgeliefert.

## Wann einsetzen, wann nicht

- Einsetzen: wiederkehrende Abfragen, Checks oder Übersetzungsaufgaben, die mehrfach täglich von einer oder mehreren Personen im Team manuell wiederholt werden.
- Nicht einsetzen: einmalige oder sehr seltene Aufgaben, bei denen sich der Aufwand für Skill-Bau und -Pflege gegenüber der reinen Wiederholung nicht lohnt.

## Belege

- 2026-01-31 · [[2026-01-31-bcherny-claude-code-team-tips]] · meinung — Boris Chernys Team (laut Tweet-Sekundärquelle) nennt die 1x/Tag-Schwelle explizit als Faustregel und den eingecheckten BigQuery-Skill als konkretes Beispiel für den Team-Wissen-Effekt (>6 Monate keine eigene SQL-Zeile mehr).
- 2026-09-27 · [[2026-09-27-anthropic-academy-sdlc-playbook]] · meinung — Anthropic nennt dieselbe Faustregel (Skill nur für konsistent anzuwendendes institutionelles Wissen) und ergänzt, dass Skills beratend sind und Pflichtregeln zusätzlich einen Hook oder Review-Durchgang brauchen. Herstellerleitfaden ohne Messdaten.
- 2025-10-31 · [[2025-10-31-agenticjames-best-claude-skills-for-agentic-coding]] · meinung — Brand- und Debugging-Skills als dynamisch geladene Dokumente; reine Empfehlung ohne Belege.
- 2026-07-03 · [[2026-07-03-neilzegh-2072977540193378428]] · meinung — Pflichtfrage in `CLAUDE.md` nach jeder Aufgabe, ob wiederverwendbares Wissen entstand; Erfahrungsaussage ohne Messung, Filterkriterium fehlt.
- 2026-10-12 · [[2026-10-12-promptgefluester-wisst-ihr-was-der-krasseste-trick-is-der-ziemlich-einfach-is-aber-den]] · meinung — Eine Retrospektive nach abgeschlossenen Prozessen soll wiederholt neu ausgeführte Aufgaben erkennen und daraus Skill-Kandidaten vorschlagen; damit wird die Wiederholung als beobachtbares Signal in einen laufenden Reviewprozess eingebaut. Die behaupteten Migrationserleichterungen sind unkontrollierte Selbstberichte beziehungsweise Prognosen; weder Wirksamkeit neuer Skills noch automatische Qualitätssteigerung ist belegt.
- 2026-07-17 · [[2026-07-17-matt-pocock-framework-hell-tutorial-hell-now-skill-hell]] · meinung — Skills sollen vom Nutzer ausgewählte Abläufe und Schleifen wiederholbar machen; auch unbeaufsichtigte Ausführung lässt die Prozessverantwortung beim Nutzer, ohne Wirksamkeitsnachweis.
- 2026-10-23 · [[2026-10-23-julian-ivanov-ki-automat-die-5-level-von-ki-nutzern-auf-welchem-bist-du]] · meinung — Nach einer gelungenen gemeinsamen Aufgabe hält Ivanov individuelle Vorgaben, Geschmack, Werkzeuge und Beispiele als Skill fest; daraus folgt weder automatische Ergebnisqualität noch vollständige Prozessdokumentation.
- 2026-10-26 · [[2026-10-26-voxyz_ai-2114746374059381186]] · meinung — Vox begrenzt die Erhebung wiederkehrender Wochenaufgaben und Nutzerkorrekturen auf höchstens sechs einzelne Fragen und fünf ausgewählte Aufgaben. Diese sollen als projektspezifische Skills mit Regeln und Beispielen erfasst werden; die Mengen sind heuristische Arbeitsgrenzen und keine nachgewiesene optimale Skill-Aufteilung.

## Spannungen & offene Fragen

- 2026-10-22: [[2026-10-12-promptgefluester-wisst-ihr-was-der-krasseste-trick-is-der-ziemlich-einfach-is-aber-den]] verspricht Verbesserung durch Retrospektiven und Skill-Vorschläge; [[2026-10-12-promptgefluester-mit-diesem-video-geh-ich-in-risiko-1]] berichtet vom selben Autor wiederkehrende Fehler trotz Retrospektiven. Wiederholung ist ein Signal für einen Kandidaten, kein Nachweis der Wirksamkeit des erzeugten Skills.

- Einzige bisherige Quelle, unbelegte Team-Selbstauskunft ohne Vorher-Nachher-Messung.
- Offene Frage: Wie unterscheidet sich dieser Schwellenwert-Ansatz von der bereits belegten Faustregel „Skill vs. Rule“ in [[Erweiterungs-Ebenen-Zuordnung]] (Litmus-Test „würde ich wollen, dass die Instruktion auch gilt, wenn ich nicht aktiv daran denke?“) — beide adressieren, wann etwas ein Skill wird, aber aus unterschiedlichen Richtungen (Häufigkeit vs. Geltungsbereich).

## Verwandte Patterns

- [[Klein-und-komposierbar]]
- [[Erweiterungs-Ebenen-Zuordnung]]
- [[AGENTS-md-Onboarding-Design]]
