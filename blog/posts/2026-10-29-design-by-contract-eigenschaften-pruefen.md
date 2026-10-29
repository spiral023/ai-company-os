---
titel: "Design by Contract: Erst die Zusage, dann der Code"
datum: 2026-10-29
kategorie: arbeitsweisen
zusammenfassung: "Design by Contract macht Aufruferpflichten, Ergebniszusagen und Invarianten sichtbar. Nutze diese Verträge, um Agentencode und seine Tests an fachlichen Erwartungen zu prüfen."
status: freigegeben
geprueft_am: 2026-10-29
freigabe: automatisch
quellen:
  - 2019-09-13-pdf-the-pragmatic-programmer-20th-anniversary-edition
---

## Kurz gesagt

- Beschreibe vor der Implementierung erlaubte Eingaben, zugesicherte Ergebnisse und beständige fachliche Eigenschaften.
- Prüfe normale Ablehnungen und unerwartete interne Fehler über passende unterschiedliche Fehlerwege.
- Ergänze Beispiele durch sinnvolle allgemeine Eigenschaften und behalte gefundene Gegenbeispiele als Regressionstests.

## Ein grüner Test braucht eine richtige Erwartung

Ein Agent ergänzt eine Funktion und erzeugt anschließend passende Tests. Wenn beide auf derselben falschen Annahme beruhen, können sie übereinstimmen und trotzdem das gewünschte Verhalten verfehlen. Du brauchst deshalb eine fachliche Zusage, an der sich Code und Tests unabhängig von ihrer Entstehungsreihenfolge prüfen lassen.

David Thomas und Andrew Hunt behandeln diese Frage in [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) unter Design by Contract. Ein Vertrag beschreibt Pflichten des Aufrufers, zugesicherte Ergebnisse und Invarianten. Er dient dem Entwurf auch dann, wenn die Programmiersprache keine vollständige technische Vertragsprüfung anbietet. Der Abschnitt steht auf den PDF-Seiten 191 bis 202.{q:1}

Auf Coding Agents übertragen hilft diese Sicht, die gewünschte Bedeutung vor dem Lesen ihrer Implementierung festzuhalten. Ein verständlicher Vertrag ist dabei noch keine Garantie für korrekten Code. Er macht die zu prüfende Zusage ausdrücklich.

## Trenne Aufruferpflicht, Ergebnis und Invariante

Nehmen wir einen gedachten Ablauf, der einen Datensatz zur Veröffentlichung vorbereitet. Die Vorbedingung legt fest, in welchem Ausgangszustand die Operation aufgerufen werden darf. Die Nachbedingung sagt, welches Ergebnis der erfolgreiche Aufruf zusichert. Eine Invariante beschreibt eine Eigenschaft, die an den vereinbarten Beobachtungsgrenzen gültig bleiben muss.

Eine mögliche fachliche Entscheidung lautet: Ein freigegebener Datensatz besitzt eine ausgewählte Sprache und einen vollständigen Titel. Diese Regel muss zuerst mit den Verantwortlichen geklärt werden. Ein Agent darf sie nicht allein deshalb verbindlich machen, weil sie plausibel klingt.

Nach der Bestätigung lässt sich untersuchen, an welcher Stelle die Änderung kontrolliert wird und welche Zugänge sie auslösen können. Die Invariante muss nicht nach jeder internen Zuweisung gelten. Ein gekapselter Ablauf darf einen Zwischenzustand besitzen, solange er an der zugesicherten Grenze wieder konsistent ist. Thomas und Hunt benennen diese zeitliche Bedeutung ausdrücklich.{q:1}

## Normale Ablehnung gehört in den beschriebenen Ablauf

Ein fehlender Titel kann eine erwartbare Eingabe sein. Dann braucht der Aufrufer ein verständliches Ablehnungsergebnis. Er sollte erfahren, weshalb die gewünschte Operation nicht stattgefunden hat und welcher Zustand erhalten blieb.

Ein intern unmöglicher Zustand ist eine andere Situation. Die Autoren empfehlen, beschädigte Zustände früh sichtbar zu machen, statt mit verfälschten Ergebnissen weiterzuarbeiten. Ressourcenpflege, hilfreiche Diagnose und eine geeignete Wiederherstellung bleiben dabei erforderlich.{q:1}

Für den gedachten Veröffentlichungsablauf bedeutet das als eigene Anwendung: Eine gewöhnliche Eingabeablehnung darf nicht als erfolgreicher Statuswechsel erscheinen. Gleichzeitig sollte ein interner Fehler nicht mit derselben Meldung wie ein fehlendes Formularfeld verborgen werden. Die beiden Ergebnisse verlangen unterschiedliche Reaktionen.

## Laufzeitprüfungen sind nur eine Darstellung des Vertrags

Ein Vertrag kann in Typen, verständlicher API-Dokumentation, Tests und Laufzeitprüfungen ausgedrückt werden. Diese Darstellungen erreichen unterschiedliche Eigenschaften. Eine Typprüfung macht beispielsweise nicht jede erlaubte Zustandsfolge sichtbar.

Gewöhnliche assert-Anweisungen prüfen interne Annahmen. Abhängig von Sprache und Laufzeit können sie abgeschaltet sein. Notwendige Zustandsänderungen dürfen deshalb nicht als Seiteneffekt innerhalb einer solchen Prüfung versteckt werden. Normale Eingabevalidierung und erwartbare Fehler brauchen einen regulären Fehlerpfad.{q:1}

Auch eine erfolgreiche Laufzeitprüfung untersucht nur die erreichten Zustände. Sie beweist weder alle möglichen Aufrufe noch die Beendigung beliebiger Abläufe. Gib dem Agenten deshalb einen klaren Prüfauftrag: Welche Zusage soll welche konkrete Prüfung untersuchen, und welche Annahmen bleiben außerhalb davon?

## Beispiele und Eigenschaften finden verschiedene Fehler

Ein Beispieltest kann zeigen, dass ein vollständiger Datensatz den erwarteten Zustand erreicht und ein unvollständiger unverändert abgelehnt wird. Damit sind konkrete Entscheidungen beschrieben. Andere Eingaben oder längere Operationsfolgen sind dadurch noch nicht automatisch untersucht.

Property-Based Testing ergänzt solche Fälle durch allgemeine Eigenschaften und erzeugte Eingaben. Eine Property ist eine Aussage, die für den vereinbarten Eingabebereich gelten soll. Die Autoren zeigen, wie solche Tests falsche Annahmen aufdecken können. Sie betonen zugleich, dass die erwarteten Eigenschaften selbst richtig gewählt sein müssen.{q:1}

Eine eigene mögliche Eigenschaft wäre: Das erneute Prüfen desselben unveränderten Datensatzes verändert seinen Inhalt nicht. Ob das für deine Anwendung richtig ist, hängt vom Vertrag ab. Eine Prüfung könnte etwa bewusst einen Zeitstempel aktualisieren; dann wäre die pauschale Eigenschaft falsch.

Wähle also Eigenschaften aus bestätigten Regeln. Übernimmt ein Test nur den Ausgang einer vorhandenen Funktion als Erwartung, fehlt die unabhängige Entscheidung. Der [Beitrag über grüne Tests und echte Codepfade](post:gruene-tests-bug-bleibt) zeigt eine weitere Ursache scheinbar erfolgreicher Prüfungen.

## Gegenbeispiele werden zu dauerhaften Regressionen

Findet eine erzeugte Eingabe einen Fehler, soll dieser konkrete Fall reproduzierbar bleiben. Thomas und Hunt empfehlen, ihn zusätzlich als festen Regressionstest aufzunehmen. Damit hängt die Wiedererkennung des Fehlers nicht davon ab, ob ein späterer Generierungslauf zufällig dieselbe Eingabe auswählt.{q:1}

Halte dabei fest, welche fachliche Zusage verletzt wurde. Ein bloß gespeicherter Fehlerfall mit unverständlichem Sollwert ist für spätere Änderungen schwer zu beurteilen. Wenn die Geschäftsregel bewusst geändert wird, muss erkennbar sein, welche Erwartungen ebenfalls neu zu entscheiden sind.

Die Autoren empfehlen außerdem, die Tests selbst mit gezielten Defekten zu kontrollieren. Ein absichtlich falscher Vergleich muss die dazugehörige Prüfung scheitern lassen. Auch diese Gegenprobe beantwortet eine begrenzte Frage über die Aussagekraft des Tests und ersetzt keine vollständige Abnahme.{q:1}

Wähle für deinen nächsten Agentenauftrag eine wichtige Operation. Formuliere ihre Vorbedingung, Ergebniszusage und Invariante mit einem fachlich bestätigten Beispiel. Lass anschließend Implementierung und Test getrennt gegen diesen Vertrag prüfen und behalte jeden dabei gefundenen Fehler als nachvollziehbare Regression.
