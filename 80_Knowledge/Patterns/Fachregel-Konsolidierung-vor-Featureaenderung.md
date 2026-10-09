# Fachregel-Konsolidierung-vor-Featureaenderung

**Konfidenz:** meinung

## Zweck

Verhindern, dass eine Featureänderung nur eine von mehreren Implementierungen derselben Fachregel aktualisiert.

## Funktionsweise

Betroffene Regelimplementierungen, Aufrufer und Ergebnisse für identische Eingaben kartieren. Bei abweichenden Ergebnissen zuerst fachlich klären, welche Variante gelten soll. Eine Verhaltenskorrektur getrennt von struktureller Konsolidierung beschreiben. Bestehendes Verhalten durch Tests absichern und verhaltensgleiche Refactors klein halten. Regel und Aufrufer anschließend zentralisieren; definierte Architektur- oder Lint-Checks sollen erneute Kopien erkennen. Danach das Feature ändern und prüfen.

## Vorteile

- Macht divergierende Regeln vor einer weiteren Änderung sichtbar.
- Trennt fachliche Entscheidungen von Strukturänderungen und erleichtert Review.

## Nachteile & Grenzen

- Gleiche Eingaben können in verschiedenen fachlichen Kontexten berechtigt unterschiedliche Regeln haben.
- Unveränderte Assertions beweisen Erhaltung nur für abgedeckte Fälle.
- Eine semantisch anders geschriebene Kopie lässt sich nicht allein durch Textsuche zuverlässig erkennen.

## Wann einsetzen, wann nicht

- Einsetzen: wiederholte Berechnungen, Validierungen und andere geteilte Fachregeln.
- Nicht einsetzen: ohne Prüfung von Kontext, Datenvertrag und Aufrufern oder als pauschale Zusammenlegung ähnlichen Codes.

## Belege

- 2026-10-02 · [[2026-10-02-voxyz_ai-2106104334035435572]] · meinung — Vox kartiert Kopien einer Fachregel vor der Featureänderung, klärt divergierende Ergebnisse fachlich und trennt Verhaltenskorrektur von erhaltendem Refactor; das Rabattbild ist eine Illustration mit drei Kopien und zwei Abweichungen.

## Spannungen & offene Fragen

- Das Quellenbild illustriert drei Rabattkopien und zwei Fehler; es ist kein gemessener Projektbefund.
- Ein Verbot weiterer Implementierungen braucht eine konkrete Erkennungsregel und muss tatsächliche Ausnahmen berücksichtigen.

## Verwandte Patterns

- [[TDD-als-Verifikationshebel]]
- [[Helper-Nutzung-durch-Lint-erzwingen]]
- [[Abstraktionswert-mit-Deletion-Test-pruefen]]
