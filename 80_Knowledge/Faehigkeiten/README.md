# Fähigkeitskandidaten

**Stand:** 2026-10-26. Fachliche Verträge für den semantischen Factory-Pilot; alle fünf sind Kandidaten und praktisch noch nicht im Factory-Betrieb evaluiert.

| Kandidat | Ausgangsfrage |
|---|---|
| [Spec-Klärung](spec-klaerung.md) | Welche Entscheidung fehlt, und welcher Kontext kann bereits zur Spec verdichtet werden? |
| [Implementierungsplanung](implementierungsplanung.md) | Welche prüfbaren Arbeitseinheiten und tatsächlichen Blocker folgen aus der Spec? |
| [Spec-Review](spec-review.md) | Welche Anforderung erfüllt der Diff, welche fehlt oder bleibt ungeklärt? |
| [Standards-Review](standards-review.md) | Welche dokumentierte Projektregel wird verletzt, und was ist lediglich eine Heuristik? |
| [Ergebnisverifikation](ergebnisverifikation.md) | Welches tatsächliche Verhalten wurde unter welchen Bedingungen nachgewiesen? |

Die Karten werden mit `python ai.py wissen karten` aus [pilot.json](../Factory/pilot.json) erzeugt. Fachliche Änderungen dort pflegen und mit `python ai.py wissen karten --check` abgleichen. [Pilot-Regeln](../Factory/README.md) beschreiben Herkunft, Aktualität und Kontextabruf.

Die Karten sind keine ausführbaren Skills und ersetzen keine Freigabe oder Runtime-Anbindung. Sie erhalten eigene Inputs, Outputs, Grenzen und einen vorbereiteten Vergleichsversuch, damit ihre spätere Verwendung überprüfbar wird.
