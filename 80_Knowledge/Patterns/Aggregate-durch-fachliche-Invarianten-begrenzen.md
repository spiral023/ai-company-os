# Aggregate-durch-fachliche-Invarianten-begrenzen

**Konfidenz:** meinung

## Zweck

Zusammengehörige fachliche Änderungen so begrenzen, dass notwendige Konsistenz nicht zwischen beliebigen Aufrufern und Objektzugriffen verloren geht.

## Funktionsweise

Zuerst die Invarianten und erlaubten Änderungen formulieren. Danach eine Gruppe von Entities und Value Objects mit einer fachlichen Grenze und einer Root bestimmen. Änderungen aus dem Außenbereich werden über diese Root kontrolliert; interne Objekte werden nicht als frei veränderbarer öffentlicher Objektgraph angeboten. Dauerhafte externe Referenzen auf Entities innerhalb des Aggregates sind auf die Root beschränkt. Referenzen auf interne Entities dürfen nur vorübergehend herausgegeben werden; Änderungen bleiben unter Kontrolle der Root. Identität und Lebenszyklus unterscheiden Entities von austauschbaren Werten.

Nicht jede Beziehung bedeutet Zugehörigkeit zum selben Aggregate. Entscheidend ist, welche Regeln bei einer Änderung zusammen eingehalten werden müssen. Die Grenze sollte tragfähig klein bleiben. Beziehungen zu anderen Aggregates, parallele Änderungen und deren Konsistenzanforderungen brauchen eine ausdrückliche Entscheidung; bloßes Nachladen des gesamten Objektgraphen löst sie nicht.

**Übertragung auf Agents:** Den Auftrag mit konkreten Invarianten und beobachtbaren Erfolgs- und Ablehnungsfällen versehen. Eine Transaktion oder ein fehlerfreier SQL-Aufruf allein beweist nicht, dass die fachlich notwendigen Datensätze geändert wurden. Technische Konkurrenzkontrolle wird passend zum Projekt entworfen und separat geprüft.

## Vorteile

- Lenkt den Entwurf auf fachlich verbotene Zustände.
- Begrenzt unkontrollierte Schreibzugriffe und macht Verantwortlichkeit überprüfbar.
- Liefert Anknüpfungspunkte für Verträge, Beispiele und konkurrierende Testfälle.

## Nachteile & Grenzen

- Zu große Aggregates erschweren Änderungen und Nebenläufigkeit; zu kleine verteilen zusammengehörige Regeln.
- Fachliche Konsistenz und technische Atomarität müssen zusammenpassen.
- Die Auswahl ist Modellarbeit; aus Tabellenstruktur, JSON-Form oder vorhandenen Klassen ergibt sich keine automatische Antwort.

## Wann einsetzen, wann nicht

- Einsetzen: Zustandsänderungen mit zusammenhängenden Invarianten und komplexen Lebenszyklen.
- Nicht einsetzen: als zusätzliche Repository- und Factory-Schicht ohne fachlichen Bedarf oder als Synonym für Microservice.

## Belege

- 2003-08-01 · [[2003-08-01-pdf-domain-driven-design]] · meinung — Kapitel 5–6, besonders PDF-S. 70–78, unterscheiden Entities, Values und Services und erläutern Aggregates als kontrollierte fachliche Lebenszyklus- und Konsistenzgrenzen. Diese Entwurfslehre ersetzt keinen ausgeführten Parallelitäts- oder Datenbanktest; der bibliografische Tageswert 01 dient der Sortierung.

## Spannungen & offene Fragen

- 2026-10-29: Ein vollständiger fachlicher Vertrag darf notwendige Ablehnungen und Fehler nicht verbergen. Ousterhouts vereinfachte Schnittstelle und Evans' kontrollierte Invarianten müssen gemeinsam erhalten bleiben.
- Context-, Modul- und Aggregategrenzen beantworten verschiedene Fragen. Ihre Gleichsetzung würde Modellentscheidungen vorwegnehmen.

## Verwandte Patterns

- [[Bounded-Contexts-und-Uebersetzungsgrenzen-kartieren]]
- [[Vertraege-mit-Vorbedingungen-Nachbedingungen-und-Invarianten]]
- [[Domaenen-Harness-mit-Daten-Evals-Rechten-und-Review]]
