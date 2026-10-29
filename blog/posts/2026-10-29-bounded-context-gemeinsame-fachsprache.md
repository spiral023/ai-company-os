---
titel: "Bounded Context: Wo die gemeinsame Fachsprache gilt"
datum: 2026-10-29
kategorie: arbeitsweisen
zusammenfassung: "Ein Bounded Context begrenzt die Bedeutung eines Fachmodells. Kläre Begriffe, Verantwortliche und Übersetzungen, bevor Coding Agents vermeintlich gleiche Daten zusammenführen."
status: freigegeben
geprueft_am: 2026-10-29
freigabe: automatisch
quellen:
  - 2003-08-01-pdf-domain-driven-design
---

## Kurz gesagt

- Beschreibe für einen wichtigen Begriff seine Regeln und Zustandswechsel mit einem Beispiel und einem Gegenbeispiel.
- Halte fest, in welchem Produktbereich diese Bedeutung gilt und wer ihre Änderungen entscheidet.
- Prüfe beim Datenaustausch, welche Bedeutung tatsächlich übertragen werden muss und welche Information dabei verloren geht.

Ein Coding Agent findet zweimal ein Feld namens `confirmed` und schlägt vor, beide Zustände zusammenzuführen. Das wirkt aufgeräumt. Ob der Vorschlag sinnvoll ist, hängt jedoch davon ab, was jede Bestätigung zusagt.

In [Domain-Driven Design](https://www.domainlanguage.com/ddd/) beschreibt Eric Evans, wie ein gemeinsames Fachmodell die Entwicklung trägt. Dazu gehört eine gemeinsame Sprache, die Beziehungen, Regeln und Operationen ausdrückt. Ihre Bedeutung wird innerhalb eines ausdrücklich bestimmten Bereichs konsistent gehalten. Diesen Geltungsbereich nennt Evans Bounded Context.{q:1}

## Was ein Begriff im Produkt zusagt

Ein Glossar kann den Einstieg erleichtern. Der Eintrag „Reservierung: eine vorübergehende Vormerkung“ lässt aber wesentliche Fragen offen. Hält sie bereits Kapazität? Wann endet sie? Kann sie nach ihrem Ablauf noch bestätigt werden?

Evans nennt die tatsächlich verwendete gemeinsame Fachsprache Ubiquitous Language. Sie verbindet Gespräche mit Fachleuten, Modell, Code und Tests. Ein vollständiger Satz wie „Eine aktive Reservierung hält zwei Plätze bis zum Ablaufzeitpunkt“ trägt deshalb mehr Entwurfswissen als eine alleinstehende Definition. Änderungen dieser Sprache können Änderungen des Modells und seines Verhaltens bedeuten.{q:1}

Für die Arbeit mit Agents leite ich daraus ab: Gib neben Begriffen auch konkrete Zusagen mit. Sonst kann eine konsequente Umbenennung dieselbe Unklarheit durch alle Dateien tragen. Verwende außerdem dieselben Formulierungen in den Beispielen, mit denen du die Änderung abnimmst.

## Eine Grenze für die Bedeutung ziehen

Ein Bounded Context umfasst den Bereich, in dem ein bestimmtes Modell gelten und konsistent bleiben soll. Dazu gehören die beteiligte Software und die Menschen, die mit diesem Modell arbeiten. Evans erläutert diese Abgrenzung besonders auf PDF-Seiten 205–210.{q:1}

Diese Grenze beantwortet eine fachliche Frage. Sie legt noch keine Aufteilung in getrennte Dienste fest. Ein Bounded Context kann viele fachliche Module enthalten. Ebenso kann ein Team mehrere Modelle betreuen, wenn deren Unterschiede und Kontakte verstanden werden.{q:1}

Ein unternehmensweit einheitliches Wortverständnis ist deshalb kein sinnvolles Ziel für jeden Begriff. Verschiedene Bereiche können berechtigt andere Modelle benötigen. Du musst die Unterschiede erkennen können, wenn du zwischen ihnen wechselst. Erst dann lässt sich entscheiden, ob eine gemeinsame Bedeutung nützlich und bezahlbar wäre.

## Ein hypothetisches Kursportal

Stell dir ein erfundenes Portal für berufliche Fortbildungen vor. Im Vertrieb bedeutet „bestätigt“, dass ein Unternehmen ein Angebot für eine Gruppe angenommen hat. In der Kursorganisation bedeutet derselbe Ausdruck, dass genügend Anmeldungen für eine konkrete Durchführung vorhanden sind.

Beide Bereiche benötigen eine Bestätigung. Die erste sagt aber noch nicht zu, dass der Kurs bereits stattfinden kann. Würde ein Agent beide Zustände durch ein gemeinsames Ja-Nein-Feld ersetzen, könnte die Annahme eines Angebots plötzlich eine Durchführung als gesichert erscheinen lassen.

Du beschreibst deshalb zunächst beide Bedeutungen. Das Vertriebsmodell enthält angenommene Angebote. Das Organisationsmodell enthält Durchführungen mit ihren eigenen Bedingungen. Für den Übergang wird geklärt, welche Information ein angenommenes Angebot liefert: etwa gewünschte Teilnehmerzahl, Zeitraum und Kursart. Die Entscheidung über die Durchführung bleibt davon unterscheidbar.

Diese Gestaltung ist ein eigener Anwendungsvorschlag. Das Beispiel prüft eine konkrete Bedeutungsgrenze; es behauptet keine notwendige Architektur für reale Kursplattformen.

## Die Karte beginnt beim heutigen Zustand

Eine Context Map ist eine Übersicht der vorhandenen Modellbereiche und ihrer Beziehungen. Sie zeigt, wo Modelle geteilt werden, wo eine Übersetzung stattfindet und wo die Zusammenarbeit noch widersprüchlich ist. Evans verlangt ausdrücklich, zunächst die tatsächliche Lage darzustellen. Ein gewünschter Umbau darf nicht als bereits vorhandene Ordnung erscheinen.{q:1}

Für das Kursportal reichen zum Einstieg die beiden Bereiche, ihre Verantwortlichen und ein benannter Übergang. Falls heute dieselbe Tabelle von beiden Anwendungen verändert wird, gehört auch das in die Beschreibung. Die Zeichnung erhält durch eine saubere Trennlinie noch keine entsprechende Umsetzung.

Du kannst danach eine kleine Änderung auswählen: beispielsweise die irreführende Weitergabe von `confirmed` durch eine Operation ersetzen, deren Name und Ergebnis die fachliche Absicht erklären. Größere Umbauten werden erst entschieden, wenn ihre Folgen sichtbar sind.

## Was du einem Agenten mitgibst

Ein passender Auftrag benennt den betroffenen Context, seine maßgeblichen Begriffe und die Nachbarbereiche. Im Kursbeispiel erhält der Agent zwei bestätigte Fälle: Ein angenommenes Angebot erzeugt noch keine gesicherte Durchführung. Eine gesicherte Durchführung kann dagegen auf mehreren angenommenen Angeboten beruhen.

Zusätzlich beschreibst du die gewünschte Übersetzung. Welche Daten werden benötigt? Welche Information fehlt auf der anderen Seite? Kann ein Ergebnis eindeutig zurückübersetzt werden? Evans zeigt am Routingbeispiel, dass Übersetzungen nur in den benötigten Richtungen funktionieren müssen und die Gegenrichtung mehrdeutig sein kann.{q:1}

Der [Beitrag über API-Verträge](post:api-vertraege-schema-coding-agents) ergänzt die strukturelle Seite. Ein Schema kann Feldnamen und erlaubte Formen festlegen. Die fachliche Bedeutung eines Status braucht weiterhin eigene Erklärung und passende Verhaltenstests.

## Mit einem Grenzfall anfangen

Übersetzung kostet Entwicklung und Pflege. Auch ein gutes Modell muss mit Änderungen der Nachbarbereiche Schritt halten. Bei einer kleinen Erweiterung kann es günstiger sein, ein passendes fremdes Modell bewusst zu übernehmen. Wenn zwischen zwei Funktionen kein notwendiger Austausch besteht, kann sogar ein gemeinsamer Zugang über die Oberfläche ausreichen. Evans behandelt solche Entscheidungen ausdrücklich als Abwägungen.{q:1}

Beginne deshalb bei einem Begriff, der bereits Missverständnisse verursacht. Schreibe für beide Seiten auf, was er zusagt, wer diese Bedeutung verantwortet und welcher Grenzfall die Differenz sichtbar macht. Gib dem Agenten anschließend genau diesen begrenzten Übergang. Beurteile seine Änderung daran, ob die fachliche Zusage erhalten bleibt.
