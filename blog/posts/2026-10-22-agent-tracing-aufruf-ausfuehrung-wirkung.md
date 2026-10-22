---
titel: "Agent-Tracing: Verfolge Aufruf, Ausführung und Wirkung getrennt"
datum: 2026-10-22
kategorie: arbeitsweisen
zusammenfassung: "Agent-Tracing hilft bei der Fehlersuche, wenn Modellaufrufe, Werkzeugausführung und Ergebnis zusammenpassen. So erkennst du Beobachtungslücken und ordnest Diffs und Tests dem richtigen Lauf zu."
status: freigegeben
geprueft_am: 2026-10-22
freigabe: automatisch
quellen:
  - 2026-10-12-josharosen-2109649928276341191
---

## Kurz gesagt

- Beginne mit einer Diagnosefrage und prüfe, auf welcher Ebene du dafür Ereignisse brauchst.
- Unterscheide angeforderte Werkzeuge, ihre tatsächliche Ausführung und den danach beobachteten Zustand.
- Verbinde einen Lauf mit den relevanten Diffs, Testergebnissen oder Browserzuständen.
- Kennzeichne fehlende Beobachtungen ausdrücklich. Eine leere Ereignisliste erklärt noch nicht, was passiert ist.

## Die Abschlussmeldung erklärt den Fehler nicht

Der Agent meldet eine erfolgreiche Änderung. Im Browser erscheint weiterhin das alte Verhalten. Du öffnest das Protokoll und findest einen Werkzeugaufruf sowie eine erfolgreiche Rückgabe. Trotzdem bleibt unklar, welche Datei geändert wurde und welchen Stand der Browser zeigt.

Agent-Tracing soll den Ablauf untersuchbar machen. Dafür brauchst du eine Aufzeichnung, die zur konkreten Frage passt: Hat das Modell die falsche Operation gewählt, ist ihre Ausführung fehlgeschlagen oder kam die Änderung im betrachteten Ergebnis nicht an?

Josh Rosen unterscheidet in seiner Architekturübersicht Modellaufrufe, Agent-Laufzeit, gespeicherte Sitzungen, verteilte Ausführung und Artefakte aus der Umgebung. Er beschreibt ihre jeweiligen Blickwinkel; einen vergleichenden Test ihrer Vollständigkeit liefert der Artikel nicht.{q:1}

## Wähle die Beobachtungsebene nach deiner Frage

Ein Trace verbindet aufgezeichnete Schritte eines Ablaufs. Welche Schritte darin enthalten sind, hängt von der Instrumentierung ab. Die folgende Auswahlhilfe ist aus Rosens Systematik abgeleitet.{q:1}

| Diagnosefrage | Benötigter Ausschnitt | Was zusätzlich offenbleiben kann |
|---|---|---|
| Warum wurde dieses Werkzeug angefordert? | Modellnachrichten und Tool-Anforderung | Ob und wie das Werkzeug anschließend lief |
| Ist der Aufruf ausgeführt worden? | Start, Ende und Ergebnis in der Agent-Laufzeit | Was innerhalb eines externen Dienstes geschah |
| Welche Dateien wurden verändert? | Dateizustand und zugeordneter Diff | Ob die Änderung das gewünschte Verhalten erzeugt |
| Warum zeigt die App noch den alten Zustand? | Geprüfter Build, Browserzustand und Umgebung | Ob die bisherigen Logs diese Verbindung überhaupt erfassen |

Für eine lokale Dateiänderung kann ein begrenzter Vergleich bereits genügen. Verläuft die Arbeit über mehrere Dienste oder delegierte Agents, musst du gegebenenfalls zusätzliche Übergänge verbinden. Mehr Ereignisse helfen nur, wenn sie deine offene Frage eingrenzen.

## Ein angefordertes Werkzeug ist noch keine ausgeführte Aktion

Der Modelloutput kann einen Tool-Aufruf enthalten. Erst das ausführende System entscheidet über die weitere Behandlung und liefert ein Ergebnis. Rosen weist darauf hin, dass die Beobachtung am Modellzugang allein die tatsächliche Werkzeugwirkung nicht erfasst.{q:1}

Ein erfolgreich beendeter Befehl wiederum sagt zunächst etwas über diesen Befehl aus. Ob die erwartete Datei geändert wurde, ein Test den betroffenen Code erreichte oder der Browser den neuen Stand geladen hat, benötigt passende Beobachtungen.

Ein synthetischer Diagnosefall macht diese Trennung greifbar: Ein Agent ändert eine Filterregel, startet einen Test und meldet Erfolg. Der Test verwendete jedoch einen anderen Datenpfad. Die Dateiänderung ist vorhanden und der Test erfolgreich; die erwartete Filterwirkung bleibt ungeprüft.

Bewahre in so einem Fall den ausgeführten Befehl, seine Ausgabe und den zugehörigen Arbeitsstand auf. Prüfe dann den konkreten Testpfad. Eine zusätzliche Zusammenfassung derselben Meldungen kann diese fehlende Verbindung nicht nachträglich beobachten.

## Ordne Ergebnisse dem richtigen Lauf zu

Rosen schlägt vor, Traces mit Diffs, Testergebnissen und Browserzuständen zu verbinden. Solche Artefakte zeigen weitere Ausschnitte der Wirkung und passen nicht immer direkt in ein gewöhnliches Ereignisprotokoll.{q:1}

Für einen eigenen, begrenzten Diagnosebericht kannst du folgende Zuordnung verwenden. Sie ist eine redaktionelle Vorlage, kein vorgeschriebenes Exportformat:

| Angabe | Zweck |
|---|---|
| Lauf und Operation | Den verantwortlichen Arbeitsschritt wiederfinden |
| Repository und Arbeitsstand | Ergebnis einer konkreten Revision samt lokalen Änderungen zuordnen |
| Werkzeug mit Ergebnis | Angeforderte und tatsächlich ausgeführte Aktion abgleichen |
| Ergebnisdatei oder Ansicht | Diff, Testbericht oder sichtbaren Zustand auffinden |
| Nicht erfasster Bereich | Die Grenze der Untersuchung ausdrücklich festhalten |

Ein Screenshot ohne bekannte Umgebung kann den falschen Stand zeigen. Ein Testbericht ohne Zuordnung zur Änderung kann aus einem früheren Lauf stammen. Ergänze nur ermittelte Angaben; ein unbekannter Arbeitsstand bleibt unbekannt.

Für die Übergabe an eine spätere Session kannst du diese Informationen in ein [kurzes Session-Handoff](post:session-handoff-morgen-weiterarbeiten) übernehmen. Verweise auf die erhaltenen Ergebnisse, statt aus ihnen eine pauschale Erfolgsmeldung zu machen.

## Verteilte Traces verbinden vorhandene Beobachtungen

Wenn ein Werkzeug intern einen weiteren Dienst aufruft, kann dieser Teil innerhalb eines einzigen sichtbaren Schritts verborgen bleiben. Rosen beschreibt OpenTelemetry als Möglichkeit, vorhandene Beobachtungen über Prozesse und Werkzeuge hinweg zu verbinden. Eine gemeinsame Konvention gleicht die Beobachtungstiefe der beteiligten Systeme nicht automatisch an.{q:1}

Prüfe an einem konkreten Ablauf, ob du den Übergang in den anderen Prozess wiederfindest und dessen Ergebnis dem ursprünglichen Auftrag zuordnen kannst. Untersuche auch, ob mehrere Schichten dieselbe Operation aufzeichnen. Doppelte Einträge dürfen bei der Auswertung nicht unbemerkt als zusätzliche Aktionen zählen.

Unterscheide dabei fehlende Ereignisse von negativen Ergebnissen. „Kein Eintrag vorhanden“ kann bedeuten, dass der Bereich nicht instrumentiert war. Erst eine passende Aufzeichnung kann zeigen, dass eine erwartete Aktion tatsächlich ausblieb.

## Überführe den gefundenen Fehler in eine gezielte Prüfung

Ein untersuchter Lauf kann Material für einen Regressionstest liefern. Rosen nennt außerdem den Vergleich veränderter Prompts, Modelle und Werkzeuge als Nutzung solcher Abläufe. Die ursprüngliche Umgebung und Modellantwort lassen sich dabei nicht zwingend exakt wiederholen.{q:1}

Extrahiere deshalb den auslösenden Fall und das erwartete Verhalten. Beim Filterbeispiel wäre das eine bekannte Eingabe mit der erwarteten Ergebnisliste. Führe die Prüfung über den betroffenen Pfad aus, damit sie denselben Fehler künftig erkennen kann.

Beginne bei deinem nächsten unklaren Agent-Ergebnis mit der engsten offenen Frage. Sammle die dafür erforderlichen Ereignisse und Ergebnisartefakte. Ergänze weitere Instrumentierung erst dort, wo die Untersuchung an einer benannten Beobachtungslücke endet.
