# Prüfungen nach Feedbackzeitpunkt staffeln

**Konfidenz:** meinung

## Zweck

Automatische Prüfungen zu einem Zeitpunkt zurückmelden, an dem der Agent sinnvoll auf das Ergebnis reagieren kann, ohne bekannte Edit-Zwischenfehler wiederholt einzuspeisen.

## Funktionsweise

Stand der Ausarbeitung: 2026-10-22. Prüfungen nach benötigtem Feedbackzeitpunkt und Laufzeit ordnen. Pocock unterscheidet Prüfungen nach jeder Dateiänderung, kurze Pre-Commit-Checks und umfangreiche CI vor dem Merge. Bei zusammenhängenden Refactorings kann der Zwischenstand mehrerer Dateien absichtlich inkonsistent sein; dieselbe Fehlermeldung nach jedem Edit bringt dann wenig neue Information.

Kurze, aussagekräftige Checks vor einem Commit bündeln und aufwendige Suiten vor dem Merge ausführen. Schnelles Feedback nach einzelnen Änderungen bleibt eine gezielt zu beurteilende Option. Weniger als drei Sekunden für Pre-Commit ist Pococks Zielheuristik vom 13. Oktober 2026, kein universelles Zeitlimit. Dieses Pattern behandelt den Zeitpunkt; [[Hook-Entscheidungstyp-nach-Pruefbarkeit]] behandelt die Implementierung der Entscheidung.

## Vorteile

- Rückmeldungen beziehen sich auf eine zusammenhängende Arbeitseinheit.
- Wiederholte Meldungen über bereits bekannte Zwischenfehler und die damit verbundenen Feedback-Tokens lassen sich begrenzen.

## Nachteile & Grenzen

- Späteres Feedback kann den Ort einer neu eingeführten Regression schwerer erkennbar machen.
- Lokale Hooks können umgangen werden; notwendige Prüfungen brauchen einen verlässlichen abschließenden Ausführungsort.
- Die Empfehlung belegt weder eine bestimmte Zeitersparnis noch, dass Prüfungen nach jedem Edit generell falsch sind.
- Eine notwendige Sicherheitsprüfung entfällt nicht wegen ihrer Laufzeit.

## Wann einsetzen, wann nicht

- Einsetzen: wenn häufige Zwischenchecks bei zusammenhängenden Agent-Änderungen wiederholt dieselben bekannten Fehler melden.
- Nicht einsetzen: als pauschalen Anlass, schnelles hilfreiches Feedback oder erforderliche Freigabeschritte zu entfernen.

## Belege

- 2026-10-13 · [[2026-10-13-matt-pocock-stop-running-your-checks-in-harness-hooks]] · meinung — Schnelle Pre-Commit-Checks und umfangreiche CI sollen wiederholte Rückmeldungen zu absichtlich inkonsistenten Edit-Zwischenständen begrenzen; keine gemessene Beschleunigung.

## Spannungen & offene Fragen

- 2026-10-22: Frühzeitige Fehlererkennung konkurriert mit dem Wunsch, zusammenhängende Änderungen zunächst abzuschließen. Der sinnvolle Zeitpunkt hängt vom Prüfsignal und der Aufgabe ab; ein starres Laufzeitlimit löst diesen Zielkonflikt nicht.

## Verwandte Patterns

- [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]
- [[Testharness-als-staerkster-Hebel]]
- [[CI-Agent-mit-Review-Gate]]
