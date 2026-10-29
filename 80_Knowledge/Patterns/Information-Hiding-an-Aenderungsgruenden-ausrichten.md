# Information-Hiding-an-Aenderungsgruenden-ausrichten

**Konfidenz:** meinung

## Zweck

Verhindern, dass dieselbe Format-, Darstellungs- oder Fachentscheidung von vielen Modulen unabhängig verstanden und nachgeführt werden muss.

## Funktionsweise

Zuerst eine konkrete Änderung durchspielen und ihre Wissensstellen ermitteln. Dann die gemeinsame Entwurfsentscheidung einem Modul zuordnen, dessen öffentliche Schnittstelle den benötigten Nutzen ohne dieses interne Wissen anbietet. Zum Vertrag zählen neben Typen und Signaturen auch Reihenfolgen, Fehler, Nebenwirkungen und Besitzregeln. Ein `private`-Feld mit öffentlich durchgereichter Darstellung kann weiterhin Wissen offenlegen.

Lesen, Verarbeiten und Schreiben beschreiben eine zeitliche Folge. Ob sie geeignete Modulgrenzen bilden, hängt davon ab, welches Wissen sie teilen. Eine gemeinsam benötigte Formatregel gehört nicht allein wegen verschiedener Ausführungszeitpunkte in mehrere unabhängige Implementierungen. Umgekehrt rechtfertigt eine gemeinsame Pipeline nicht die Zusammenlegung fachlich unabhängiger Schritte.

**Übertragung auf Agents:** Vor der Extraktion zeigen, welches Aufruferwissen entfällt und an welchen Stellen die nächste Regeländerung vorgenommen werden müsste. Diese Anwendung ist aus Ousterhout abgeleitet und hier nicht in einem Produktrepo erprobt.

## Vorteile

- Macht Änderungsausbreitung und verdeckte Verpflichtungen sichtbar.
- Bewertet eine Abstraktion anhand ihrer Benutzung statt anhand der Dateilänge.
- Ergänzt die Suche nach dupliziertem Wissen um einen konkreten Informationsbesitzer.

## Nachteile & Grenzen

- Erfordert reale Aufrufe und Verständnis des Änderungsgrunds.
- Nicht jede Abhängigkeit lässt sich entfernen; benötigte Fachzusagen müssen sichtbar bleiben.
- Eine schwer verständliche große Schnittstelle wird durch viel verborgenen Code nicht automatisch gut.

## Wann einsetzen, wann nicht

- Einsetzen: verstreute Formatregeln, wiederkehrende Aufruferpflichten und Refactoring von Durchreichungen.
- Nicht einsetzen: als pauschale Forderung nach einer einzigen Datei oder zur mechanischen Zusammenlegung ähnlichen Codes.

## Belege

- 2021-07-01 · [[2021-07-01-pdf-a-philosophy-of-software-design-2nd-edition]] · meinung — PDF-S. 30–49 und 61–70 beschreiben vollständige Schnittstellen, Informationsbesitz, zeitliche Zerlegung und Durchreichungen; Juli 2021 ist monatsgenau, der Tag 01 ein Sortierwert. Begründete Entwurfslehre, keine eigene Wirksamkeitsmessung.

## Spannungen & offene Fragen

- 2026-10-29: Eine besser gekapselte allgemeine Schnittstelle kann den heutigen Bedarf vereinfachen; spekulative Parameter und zusätzliche Schichten können ihn erschweren. Der Entwurf muss an konkreten Aufrufen bestehen.
- Der bekannte Deletion Test ist eine verwandte spätere Prüfmethode, kein hier als wörtliche Ousterhout-Methode behaupteter Buchinhalt.

## Verwandte Patterns

- [[Abstraktionswert-mit-Deletion-Test-pruefen]]
- [[Fachregel-Konsolidierung-vor-Featureaenderung]]
- [[Kommentare-als-Schnittstellenwissen-pflegen]]
- [[Designalternativen-vor-Festlegung-vergleichen]]
