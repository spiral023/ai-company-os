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

## Spannungen & offene Fragen

- Einzige bisherige Quelle, unbelegte Team-Selbstauskunft ohne Vorher-Nachher-Messung.
- Offene Frage: Wie unterscheidet sich dieser Schwellenwert-Ansatz von der bereits belegten Faustregel „Skill vs. Rule“ in [[Erweiterungs-Ebenen-Zuordnung]] (Litmus-Test „würde ich wollen, dass die Instruktion auch gilt, wenn ich nicht aktiv daran denke?“) — beide adressieren, wann etwas ein Skill wird, aber aus unterschiedlichen Richtungen (Häufigkeit vs. Geltungsbereich).

## Verwandte Patterns

- [[Klein-und-komposierbar]]
- [[Erweiterungs-Ebenen-Zuordnung]]
- [[AGENTS-md-Onboarding-Design]]
