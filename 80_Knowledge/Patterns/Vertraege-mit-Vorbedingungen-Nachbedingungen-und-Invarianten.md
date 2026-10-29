# Vertraege-mit-Vorbedingungen-Nachbedingungen-und-Invarianten

**Konfidenz:** meinung

## Zweck

Den erlaubten Aufruf, das zugesicherte Ergebnis und beständige fachliche Eigenschaften einer Operation von ihrer zufälligen Implementierung unterscheiden.

## Funktionsweise

Vorbedingungen benennen die Pflicht des Aufrufers, Nachbedingungen die Zusage der Operation und Invarianten die an vereinbarten Grenzen gültigen Eigenschaften. Intern darf eine gekapselte Änderung einen Zwischenzustand besitzen, solange die öffentliche Beobachtung und das Verlassen der Grenze die zugesicherte Konsistenz erhalten. Fachliche Grundbedingungen sind von bewusst änderbarer Geschäftspolitik zu unterscheiden.

Verträge formulieren Zustandszusagen und können durch Typen, API-Dokumentation, Tests und geeignete Laufzeitprüfungen unterstützt werden. Evans verwendet Assertions für solche Zusagen, insbesondere Nachbedingungen und Invarianten. Laufzeit-`assert`-Anweisungen prüfen interne Annahmen und dürfen keine notwendigen Seiteneffekte besitzen. Normale ungültige Eingaben und erwartbare Dienstfehler brauchen einen regulären Fehlerpfad; eine möglicherweise abgeschaltete Laufzeitassertion ersetzt diesen nicht.

**Übertragung auf Agents:** Erst die fachlich bestätigte Zusage festhalten, dann Implementierung und Prüfungen davon ableiten. Getrennt prüfen, ob die behauptete Regel richtig ist und ob der Code sie tatsächlich erfüllt. Laufzeitassertions beweisen weder alle Eingaben noch Terminierung oder korrekte externe Wirkungen.

## Vorteile

- Macht verdeckte Erwartungen an Aufrufer und Ergebnisse sichtbar.
- Verbindet Entwurf mit Beispielen, Randfällen und Property-Based Tests.
- Unterscheidet normale Ablehnung von einem intern beschädigten Zustand.

## Nachteile & Grenzen

- Ein formal formulierter falscher Vertrag bleibt fachlich falsch.
- Laufzeit- und Sprachunterstützung unterscheiden sich; Nebenläufigkeit kann zusätzliche Sicherung verlangen.
- Eine Invariante ist nur nützlich, wenn die gewählte Grenze ihre Einhaltung tatsächlich kontrolliert.

## Wann einsetzen, wann nicht

- Einsetzen: öffentliche Operationen, Fachregeln, Zustandsübergänge und schwer erkennbare Aufruferpflichten.
- Nicht einsetzen: als generische Assertion auf jede Zeile oder als Ersatz für Eingabevalidierung und Integrationsprüfung.

## Belege

- 2019-09-13 · [[2019-09-13-pdf-the-pragmatic-programmer-20th-anniversary-edition]] · meinung — PDF-S. 191–202 unterscheiden Vorbedingungen, Nachbedingungen und Invarianten sowie semantische Grundbedingungen und Geschäftspolitik; PDF-S. 207–210 grenzen Assertions von normaler Fehlerbehandlung ab. Der Transfer auf aktuelle Coding Agents ist redaktionell.
- 2003-08-01 · [[2003-08-01-pdf-domain-driven-design]] · meinung — Kapitel 10, besonders PDF-S. 156–159, verbindet explizite Assertions über Operationen und Invarianten mit vorhersehbaren Seiteneffekten und verständlicher Modellbenutzung; kein experimenteller Wirksamkeitsbeleg.

## Spannungen & offene Fragen

- 2026-10-29: Die zwei Bücher liefern verwandte Entwurfsgrundlagen. Die konkrete Agentenarbeitsweise ist hier nicht praktisch verifiziert; gemeinsame Empfehlungen werden nicht zu einer gemessenen Qualitätsgarantie hochgestuft.
- Nachbedingungen beschreiben eine Zusage. Das Prüfen einer Bedingung nach einem Aufruf beweist für sich keine Beendigung beliebiger Programmläufe.

## Verwandte Patterns

- [[Aggregate-durch-fachliche-Invarianten-begrenzen]]
- [[Kommentare-als-Schnittstellenwissen-pflegen]]
- [[TDD-als-Verifikationshebel]]
- [[Testharness-als-staerkster-Hebel]]
