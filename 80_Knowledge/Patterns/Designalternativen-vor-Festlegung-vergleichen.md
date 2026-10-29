# Designalternativen-vor-Festlegung-vergleichen

**Konfidenz:** meinung

## Zweck

Die erste plausible Implementierung nicht ungeprüft zum dauerhaften Schnittstellen- oder Architekturentscheid werden lassen.

## Funktionsweise

Für eine folgenreiche Entscheidung mindestens zwei tatsächlich unterschiedliche Entwürfe knapp skizzieren. Dafür genügen oft Schnittstellen, charakteristische Aufrufe und die jeweils schwierigen internen Entscheidungen. Beide Varianten am gleichen Normalfall, relevanten Fehlerfall und schwierigen Benutzungsfall vergleichen. Kriterien sind je nach Aufgabe Aufruferwissen, Implementierungskomplexität, Änderungskosten und gegebenenfalls gemessene Performance.

Die zweite Variante darf keine absichtlich schlechte Karikatur sein. Auch eine dritte Kombination kann aus dem Vergleich entstehen. Eine schriftliche Begründung hält fest, welche Kosten akzeptiert wurden und welche Annahme die Wahl später ändern würde. Es müssen nicht zwei vollständige Systeme gebaut werden.

**Übertragung auf Agents:** Vor umfangreicher Generierung die APIs und Aufrufbeispiele prüfen lassen. Die ausgewählte Variante wird anschließend implementiert und gegen ihren Vertrag verifiziert. Ein Modellranking mehrerer eigener Vorschläge ist noch kein unabhängiger Nachweis.

## Vorteile

- Macht Trade-offs vor einer teuren Implementierung sichtbar.
- Verhindert, dass Fertigstellungsgrad die Entwurfswahl dominiert.
- Liefert einen begrenzten Anlass, die erste Abstraktion zu hinterfragen.

## Nachteile & Grenzen

- Zusätzlicher Vergleichsaufwand lohnt nicht bei jeder trivialen Änderung.
- Ohne gleiche Kriterien kann die favorisierte Variante nur sprachlich besser aussehen.
- Unbekannte künftige Anforderungen dürfen nicht als sichere Vorteile eingerechnet werden.

## Wann einsetzen, wann nicht

- Einsetzen: neue öffentliche API, schwer revidierbare Modellentscheidung und wesentliches Refactoring.
- Nicht einsetzen: Routinefix mit eindeutig bestätigtem Fehlerpfad oder bloßer Wunsch nach Variantenmenge.

## Belege

- 2021-07-01 · [[2021-07-01-pdf-a-philosophy-of-software-design-2nd-edition]] · meinung — PDF-S. 101–103 erläutern Design it twice als Vergleich unterschiedlicher Ansätze ohne zwingend zwei vollständige Implementierungen; PDF-S. 139–143 verknüpfen frühe Verträge mit der Entwurfsprüfung. Keine eigene Agentenvergleichsmessung.

## Spannungen & offene Fragen

- 2026-10-29: Strategische Entwurfsarbeit steht unter Zeitdruck. Ein begrenzter Vergleich heutiger Fälle soll konkrete Fehlentscheidungen vermeiden; eine spekulative Rahmenarchitektur für viele unbekannte Zukünfte folgt daraus nicht.
- Das bestehende UI-Variantenpattern verlangt eine Auswahl am bedienbaren Ergebnis. API-Skizzen prüfen andere Eigenschaften und ersetzen diese visuelle Abnahme nicht.

## Verwandte Patterns

- [[Information-Hiding-an-Aenderungsgruenden-ausrichten]]
- [[Kommentare-als-Schnittstellenwissen-pflegen]]
- [[Variantenvergleich-vor-Produktionsabnahme]]
- [[Plan-first-mit-getrenntem-Review]]
