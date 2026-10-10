# Refactoring mit Verhaltensvergleich

**Konfidenz:** meinung

## Zweck

Strukturelle Umbauten so begrenzen, dass das vereinbarte Verhalten gezielt vor und nach der Änderung geprüft werden kann.

## Funktionsweise

Altes Verhalten, geplante Strukturverbesserung und konkrete Prüfung pro Umbau dokumentieren. Öffentliches Interface stabil halten. Für den eigenen Blog-Ablauf dieselben Testeingaben verwenden und vereinbarte Sollwerte zusätzlich prüfen. Funktionale Änderungen und Migrationen gesondert behandeln.

## Vorteile

- Kleine Änderungen bleiben einzeln prüfbar und rücknehmbar.
- Verhalten und technische Struktur bekommen eigene Abnahmekriterien.

## Nachteile & Grenzen

- Übernommenes Altverhalten kann bereits fehlerhaft sein.
- Ein Vergleich endlich vieler Eingaben beweist keine allgemeine Äquivalenz.

## Wann einsetzen, wann nicht

- Einsetzen: strukturelle Änderungen an bestehender Logik.
- Nicht einsetzen: beauftragte neue Funktion; hierfür neue Sollkriterien festlegen.

## Belege

- 2026-10-09 · [[2026-10-09-openai-refactoring]] · meinung — offizielle Anleitung für kleine Umbauten und explizite Prüfungen des Verhaltenserhalts; identische Eingaben sind die eigene konkretisierende Methode.
- 2026-07-21 · [[2026-07-21-claudedevs-2079654423828304282]] · meinung — Die Sprachmigration verwendet identische Eingaben und externe Assertions gegen Original und Port als Verhaltensreferenz. Dieser Prüfgedanke ergänzt das Pattern, während Migration und mögliche Architekturänderungen gesonderte Scope- und Abnahmekriterien benötigen; das Original ist zudem nicht automatisch fachlich fehlerfrei.

## Spannungen & offene Fragen

- Fehlende dokumentierte Fachregeln erschweren die Entscheidung, welche Alt-Ergebnisse gelten sollen.

## Verwandte Patterns

- [[Codepfad-vor-Aenderung-nachvollziehen]]
