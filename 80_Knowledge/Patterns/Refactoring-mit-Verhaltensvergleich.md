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
- 2026-10-05 · [[2026-10-05-venelin-valkov-stop-ai-code-slop-yes-you-still-need-to-refactor]] · meinung — Der Autor koppelt den Umbau des Streaming-Zustands an Renderzählungen vor und nach der Änderung und prüft anschließend sichtbare Antwortaktualisierung. Die behauptete Reduktion betrifft bestimmte Komponenten; vollständige funktionale Gleichheit und entsprechend kürzere Gesamtlaufzeit sind damit nicht nachgewiesen.
- 2026-10-17 · [[2026-10-17-developers-maintaining-software-with-the-gpt-6-family-opena]] · meinung — Kleine Draft-PRs mit Produktionswerten und Belegen sollen das Verhalten erhalten; als „Permanent“ markierte Flags werden trotz möglicher Einsparung zur menschlichen Prüfung eskaliert, und komplexitätssteigernde Optimierungen können unvorteilhaft sein. Interner Praxisbericht mit unsicherem Publikationsdatum.
- 2026-10-25 · [[2026-10-25-mattpocockuk-2114311664069718370]] · meinung — Als Ideal nennt Pocock unveränderten Bundle-Output bei Quellcode-Refactorings und schließt dafür import.meta.glob, laufzeitabhängige Quellpositionen und globalen Zustand aus. Die unvollständige, vom Autor später selbst bezweifelte Ideenskizze liefert Prüfgrenzen; gleiche Testabdeckung beweist keine Semantikerhaltung.
- 2026-10-20 · [[2026-10-20-anthropic-using-claude-to-reduce-the-attack-surface-of-cod]] · meinung — Bei Gates gegen unnötige Default-Erreichbarkeit verlangt Anthropic identische Ergebnisse der Projekt- und Black-Box-Regressionstests gegenüber einer unveränderten Baseline. Nichtstandardmäßige Konfigurationen mit Verhaltensänderung werden zur menschlichen Entscheidung ausgesondert; die Tests belegen nur den geprüften Verhaltensumfang.

## Spannungen & offene Fragen

- Fehlende dokumentierte Fachregeln erschweren die Entscheidung, welche Alt-Ergebnisse gelten sollen.

- 2026-10-25 · [[2026-10-25-mattpocockuk-2114311664069718370]] und 2026-10-20 · [[2026-10-20-anthropic-using-claude-to-reduce-the-attack-surface-of-cod]]: Unveränderte Coverage und identische Regressionsergebnisse sichern unterschiedliche, jeweils begrenzte Eigenschaften. Weder daraus noch aus nicht beobachteten Ausführungspfaden folgt vollständige Semantikgleichheit oder Unerreichbarkeit; Änderungen anderer Konfigurationen brauchen eine eigene Entscheidung.

## Verwandte Patterns

- [[Codepfad-vor-Aenderung-nachvollziehen]]
