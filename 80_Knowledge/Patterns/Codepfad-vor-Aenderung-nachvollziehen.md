# Codepfad vor Änderung nachvollziehen

**Konfidenz:** meinung

## Zweck

Vor einer Änderung die Zuständigkeiten und Nebenwirkungen eines begrenzten Ablaufs verstehen.

## Funktionsweise

Den Ablauf von UI oder Eingangsdaten durch Validierung, Business-Logik und Persistenz verfolgen. Jede Verbindung an Dateien festmachen. Offene Annahmen ausweisen und nächste Lesestellen sowie Prüfungen bestimmen.

## Vorteile

- Liefert konkrete Einstiegspunkte für eine kleine Änderung.
- Macht übersehene Zustandswechsel und Abhängigkeiten sichtbar.

## Nachteile & Grenzen

- Ein Agent kann den Ablauf falsch rekonstruieren; Dateiverweise müssen kontrolliert werden.
- Eine gesamte Codebase zu erklären erzeugt schnell zu unspezifische Ergebnisse.

## Wann einsetzen, wann nicht

- Einsetzen: unbekannter Systembereich vor einer Änderung.
- Nicht einsetzen: bekannte triviale Stelle ohne relevante offene Abhängigkeiten.

## Belege

- 2026-10-09 · [[2026-10-09-openai-codebase-onboarding]] · meinung — offizielle Anleitung zu begrenzter Analyse von Datenfluss und Zuständigkeiten, ohne eigene Qualitätsmessung.

## Spannungen & offene Fragen

- Architekturerklärungen brauchen Rückprüfung am Code; Dokumentation allein zeigt keinen tatsächlichen Lauf.
- 2026-10-10: [[Architektur-in-Perspektiven-dokumentieren]] ergänzt die begrenzte Ablaufanalyse um eine dauerhaft gepflegte Gesamtkarte. Die rekursive Analyse jedes Knotens aus [[2026-10-10-repo-oh-my-mermaid-architektur]] ist zusätzlicher Aufwand und nicht für jeden kleinen Änderungsanlass nötig.

## Verwandte Patterns

- [[Refactoring-mit-Verhaltensvergleich]]
- [[Architektur-in-Perspektiven-dokumentieren]]
