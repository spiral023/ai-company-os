---
titel: "Decision-Modelle selbst trainieren: Was ein guter Test zeigen muss"
datum: 2026-10-09
kategorie: arbeitsweisen
zusammenfassung: "Decision-Modelle trainieren lohnt sich bei klaren Auswahlentscheidungen. Ein eigener Test trennt Trainingsdaten, Kalibrierung und Bewertung und macht Fehlerkosten sichtbar."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-10-07-unslothai-decision-model-finetuning
---

## Kurz gesagt

- Definiere die erlaubten Antworten und prüfe die Qualität ihrer Zuordnung in deinen Beispielen.
- Trenne Training, Entwicklungsprüfung, Kalibrierung und abschließenden Test vor dem ersten Versuch.
- Vergleiche das trainierte Modell mit einer einfachen Ausgangslösung auf denselben zurückgehaltenen Fällen.
- Bewerte Fehlentscheidungen, menschlichen Prüfaufwand und Betriebskosten gemeinsam.

## Wann lohnt sich ein eigenes Decision-Modell?

Du möchtest eingehende Supportanfragen an das passende Team weiterleiten. Die möglichen Ziele stehen vorher fest: technische Fehler, Bedienungsfragen, Produktberatung oder manuelle Klärung. Dieses synthetische Routing-Beispiel dient im Artikel als Vorschlag für einen eigenen Versuch; es beschreibt keine durchgeführten Messungen.

Ein Decision-Modell bewertet vorgegebene Optionen und liefert eine Auswahl mit Wahrscheinlichkeiten. Das passt zu Routing oder Klassifikation, bei der Eingaben einer festgelegten Kategorie zugeordnet werden. Für eine ausformulierte Supportantwort brauchst du einen zusätzlichen Schritt.

Eigenes Training kommt infrage, wenn eine vorhandene Lösung an wiederkehrenden Fällen scheitert und du verlässliche Beispiele mit gewünschten Antworten hast. Prüfe zuerst, ob eindeutigere Kategorien, verständlichere Auswahlkriterien oder eine einfache Regel das Problem bereits lösen. Den grundlegenden Auswahlansatz erklärt [Routing per Scoring](post:routing-per-scoring-statt-text).

## Was Clef-Head und LoRA beitragen

Unsloth beschreibt eine Umsetzung mit einem Sprachmodell als Grundlage und einem Clef-Head. Dieser zusätzliche Modellteil bewertet die Optionen zu den gestellten Fragen. LoRA passt das Modell über zusätzliche trainierbare Parameter an die Aufgabe an. Der Guide kombiniert beide Bausteine für eigenes Training. {q:1}

Der feste Labelraum ist die Menge der erlaubten Antworten. In unserem Beispiel gehören dazu die vier Teamziele. Diese Begrenzung macht die Ausgabe für den nächsten Programmschritt handhabbar. Die inhaltliche Qualität hängt weiterhin von den Kategorien, Trainingsfällen und späteren Eingaben ab.

Eine hohe Wahrscheinlichkeit für „technische Fehler“ beantwortet dabei die definierte Routing-Frage. Aus ihr lassen sich weder die Zufriedenheit eines Kunden noch dessen persönliche Präferenzen ableiten. Auch die Option „manuelle Klärung“ muss in den Daten mit verständlichen Beispielen vorkommen.

## Lege einen Datenvertrag fest

Schreibe vor dem Sammeln der Beispiele auf, welche Eingabe das Modell erhält und was jede Antwort bedeutet. Ein vorgeschlagener Datenvertrag enthält Anfrage, Routing-Frage, erlaubte Optionen, gewünschte Antwort und eine Gruppenzuordnung für die spätere Datentrennung.

| Erfundenes Beispiel | Gewünschtes Ziel | Grund für die Zuordnung |
|---|---|---|
| „Beim Export erscheint eine Fehlermeldung.“ | Technische Fehler | Eine vorhandene Funktion funktioniert fehlerhaft |
| „Wo kann ich die Ansicht wechseln?“ | Bedienungsfragen | Die Anfrage betrifft die Nutzung einer Funktion |
| „Unterstützt ihr auch mehrere Projektbereiche?“ | Produktberatung | Gefragt wird nach dem Funktionsumfang |
| „Export geht komisch, außerdem brauche ich eine andere Ansicht.“ | Manuelle Klärung | Mehrere Anliegen und unklare Beschreibung |

Lass die gewünschten Antworten fachlich prüfen. Wenn zwei Personen denselben Fall unterschiedlich einordnen, klärt ihr die Kategorien oder markiert den Fall für eine gesonderte Bewertung. Solche Unklarheiten landen sonst im Training und später in einer schwer interpretierbaren Fehlerquote.

Synthetische Beispiele helfen, das Format auszuprobieren. Für eine Entscheidung über den echten Einsatz sollten fachlich geprüfte Fälle aus dem erwarteten Aufgabenbereich hinzukommen. Achte auf kurze, lange, mehrdeutige und seltene Anfragen.

## Trenne die Daten vor den Experimenten

Für den eigenen Versuch empfiehlt sich folgende Aufteilung: Trainingsdaten passen die Modellparameter an. Entwicklungsdaten helfen dir bei der Auswahl von Einstellungen. Kalibrierungsdaten dienen dazu, Wahrscheinlichkeiten und Entscheidungsschwellen zu beurteilen. Der abschließende Testsatz bleibt bis zur festgelegten Auswertung unangetastet.

Ein Holdout ist ein zurückgehaltener Teil der Daten. Seine Aussagekraft hängt davon ab, ob er tatsächlich neue Fälle repräsentiert. Halte Anfragen desselben Kunden im selben Teil und gruppiere ähnliche Duplikate sowie Varianten desselben Vorgangs zusammen. Sonst kann das Modell beim Test auf Formulierungen treffen, die es in fast gleicher Form bereits gelernt hat.

Prüfe nach dieser Gruppierung die Verteilung der Kategorien. Fehlt eine seltene Kategorie im Test, kannst du deren Qualität damit nicht einschätzen. Halte diese Lücke im Ergebnis fest. Die Trennung vor wiederholten Experimenten vertieft [Hillclimbing mit Holdout](post:hillclimbing-mit-holdout).

## Dokumentiere den Trainingslauf als eigene Konfiguration

Der Unsloth-Guide enthält unterschiedliche Einstellungen: Sein Benchmark-Abschnitt nennt LoRA-Rang `r=64` und eine Epoche. Setup und Codebeispiel verwenden `r=16` und zwei Epochen. Eine Epoche ist ein Durchlauf durch die Trainingsdaten; der Rang beeinflusst den Umfang der LoRA-Anpassung. Diese Konfigurationen dürfen beim Nachbauen nicht zu einer vermeintlich exakten Benchmark-Reproduktion vermischt werden. {q:1}

Im Code des Guides werden zurückgehaltene `eval_items` während des Trainings ausgewertet und anschließend zur Kalibrierung verwendet. {q:1} Für den hier vorgeschlagenen Versuch reservierst du zusätzlich einen eigenen Testsatz. Dokumentiere Modell, Datenstand, Kategorien, Trainingsparameter und Kalibrierungsverfahren zusammen.

Unsloth berichtet Genauigkeitsgewinne auf den genannten Benchmarks. Das gibt einen Anlass für einen eigenen Vergleich; der Gewinn auf deinen Supportanfragen bleibt zu messen. Eine Herstellerangabe zur Hardware beantwortet ebenso wenig, ob dein Datenumfang und deine Eingabelängen auf deinem Gerät praktikabel sind. {q:1}

## Was der abschließende Test zeigen sollte

Vergleiche die eingefrorene Ausgangslösung und das trainierte Modell auf denselben Testfällen. Accuracy, der Anteil korrekt ausgewählter Antworten, ist ein erster Überblick. Ergänze Ergebnisse je Kategorie und eine Tabelle, die tatsächliche Ziele den gewählten Zielen gegenüberstellt. So erkennst du, welche Verwechslungen häufig auftreten.

Lege vor der Auswertung fest, welche Fehler besonders teuer sind. Im Beispiel könnte eine technische Störung in der Produktberatung länger liegen bleiben. Ein vorsichtiger Fall in der manuellen Klärung verursacht dagegen zusätzliche Prüfarbeit. Beide Folgen gehören in die Bewertung.

Prüfe auch die Kalibrierung: Unter Fällen mit ähnlich hoher ausgegebener Wahrscheinlichkeit sollte die beobachtete Trefferhäufigkeit dazu passen. Lege Schwellen anhand der dafür vorgesehenen Daten fest und friere sie vor dem Abschlusstest ein. Berichte anschließend gemeinsam, wie viele Fälle automatisch weitergeleitet werden, wie oft das falsch geschieht und wie viel manuelle Klärung übrig bleibt.

## Entscheide anhand von Nutzen und Aufwand

Zum Aufwand gehören das Prüfen der Antworten in den Daten, Trainingsläufe, Kalibrierung, Modellbetrieb und die Bearbeitung verbleibender Fehler. Miss außerdem Antwortzeit und Speicherbedarf unter deinen Bedingungen. Eine bessere Gesamtgenauigkeit kann unattraktiv sein, wenn eine wichtige seltene Kategorie schlechter wird oder die Betreuung stark wächst.

Starte mit einem Offline-Vergleich ohne Weiterleitung echter Anfragen. Formuliere dafür noch vor dem Training die Entscheidungskriterien. Speichere die einzelnen Fehlentscheidungen für eine gezielte Durchsicht. Erst wenn dieser Vergleich einen brauchbaren Nutzen zeigt, ist ein begrenzter Probelauf mit menschlicher Kontrolle der nächste Schritt. Die konkrete nächste Aufgabe lautet daher: Kategorien definieren, Fälle fachlich prüfen und einen gruppierten Testsatz zurückhalten.
