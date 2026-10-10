---
titel: "Passt ein lokales Coding-Modell auf deinen Rechner?"
datum: 2026-10-09
kategorie: tools
zusammenfassung: "Schätze Modellgewichte ab und prüfe Kontext, RAM und Grafikspeicher getrennt. Mit einer kleinen Erfassungsvorlage für deinen lokalen Coding-Versuch."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-08-16-floknowsai-in-einem-jahr-ersetzt-ein-lokales-modell-dein-claude-abo
  - 2026-10-09-ollama-kontext-speicher
---

## Kurz gesagt

- Rechne den Speicher für Modellgewichte als erste Untergrenze aus; Kontext und Laufzeit kommen hinzu.
- Prüfe beim tatsächlichen Lauf, wie das Modell auf CPU und GPU verteilt ist und welchen Kontext es verwendet.
- Wähle eine kleine, bekannte Coding-Aufgabe und beurteile sowohl die Antwort als auch das Verhalten deines Rechners.
- Halte Modellversion, Quantisierung und Einstellungen fest, damit du Varianten sinnvoll vergleichen kannst.

## Beginne mit deiner Aufgabe

Ein lokales Modell soll dir beim Programmieren helfen. Vielleicht möchtest du eine Funktion erklären lassen, einen Test ergänzen oder eine kleine Änderung vorbereiten. Diese Aufgaben benötigen unterschiedlich viel Projektkontext. Vor der Hardwarefrage lohnt sich deshalb ein konkreter Auftrag: Welche Dateien muss das Modell lesen, welches Ergebnis erwartest du, und wie prüfst du es?

Für einen ersten Versuch eignet sich eine überschaubare Funktion, die du selbst beurteilen kannst. Bitte um eine Erklärung mit einem Eingabebeispiel und um einen passenden Testvorschlag. So erkennst du Fehler leichter als bei einem großen, unbekannten Umbau.

Die folgende Anleitung ist eine Vorabprüfung mit anschließendem eigenen Versuch. Ich habe dafür kein Modell auf einer bestimmten Grafikkarte vermessen. Die Speicherrechnung beschreibt eine theoretische Untergrenze; die Erfassungsvorlage enthält bewusst keine fertigen Leistungswerte.

## Rechne zuerst nur die Modellgewichte

Modellgewichte sind die gespeicherten Zahlen, mit denen das Modell rechnet. Quantisierung verkleinert ihre Darstellung. Die grobe Rechnung aus dem Video von FloKnowsAI lautet: Parameterzahl mal Bits pro Gewicht, geteilt durch acht. Sie hilft bei einer ersten Größenordnung, erfasst aber kein vollständiges Laufzeitbudget.{q:1}

Ein eigenes theoretisches Beispiel mit acht Milliarden Parametern und vier Bits pro Gewicht ergibt vier Milliarden Bytes, also vier GB in dezimaler Schreibweise. In GiB sind das rund 3,73. Diese Rechnung behandelt ausschließlich die idealisierten Gewichte. Dateiformat, Zusatzinformationen und eine konkrete Quantisierung können den tatsächlichen Umfang verändern; die Zahl ist deshalb keine Zusage, dass ein solches Modell auf einer Grafikkarte mit vier GB vollständig läuft.{q:1}

Für deine Vorauswahl kannst du drei Werte nebeneinander schreiben:

| Wert | Was du damit beurteilst |
|---|---|
| Theoretischer Gewichtsspeicher | Erste Größenordnung aus Parameterzahl und Darstellung |
| Tatsächliche Größe der gewählten Modelldatei | Umfang genau dieser angebotenen Variante |
| Speicherbelegung während deiner Aufgabe | Bedarf des konkreten Laufs mit deinen Einstellungen |

RAM bezeichnet den Arbeitsspeicher des Rechners, VRAM den Grafikspeicher. Eine freie Kapazität in einem dieser Bereiche ersetzt die andere nicht automatisch. Entscheidend ist auch, welche Hardware dein Laufzeitprogramm tatsächlich verwendet. Eine Werbeangabe zur Gesamtgröße allein beantwortet diese Frage kaum.

## Gib dem Kontext ein eigenes Budget

Zum Modell kommen die Eingaben: Auftrag, Dateien, bisherige Antworten und gegebenenfalls Werkzeugergebnisse. Die konfigurierte Kontextlänge bestimmt, wie viele Tokens der Lauf verarbeiten kann. Tokens sind die Texteinheiten, mit denen das Modell arbeitet.

Ollama dokumentiert ausdrücklich, dass eine größere Kontextlänge mehr Speicher benötigt. Die Dokumentation nennt außerdem unterschiedliche Voreinstellungen abhängig vom verfügbaren Grafikspeicher. Die Angaben sind ein am 9. Oktober 2026 gesichteter Dokumentationsstand, keine Messung für dein Modell oder deinen Rechner.{q:2}

Für den ersten Versuch würde ich nur die Funktion und ihre direkten Aufrufer bereitstellen. Danach kannst du eine weitere relevante Datei ergänzen. Halte dabei fest, ob das Ergebnis fachlich besser wird und ob der Lauf weiterhin brauchbar reagiert. Viel unpassender Text kann die Untersuchung zusätzlich erschweren.

Eine große nominelle Kontextkapazität beantwortet auch nicht, ob dein Coding-Auftrag gelingt. Wenn das Modell Namen verwechselt oder eine wichtige Bedingung übersieht, prüfe zunächst die Eingaben und die Antwort. Mehr zugewiesener Kontext allein bestätigt keine korrekte Umsetzung.

## Prüfe den tatsächlichen Lauf

Wenn du Ollama bereits eingerichtet hast und ein Modell geladen ist, zeigt dieser lesende Befehl den aktuellen Laufzustand:

```text
ollama ps
```

Die offizielle Dokumentation beschreibt dabei unter anderem die Spalten `PROCESSOR` und `CONTEXT`: Du kannst die CPU/GPU-Zuordnung und die konfigurierte Kontextgröße prüfen. Bei CPU-Offloading übernimmt die CPU Teile der Modellberechnung. Ollama empfiehlt für Leistung, diese Auslagerung zu vermeiden. Wie stark sich die Aufteilung bei deinem Auftrag auswirkt, musst du selbst beobachten.{q:2}

Ergänze die Ausgabe um die Speicheranzeige deines Betriebssystems. Interessant sind die Belegung während der Aufgabe und die Nutzbarkeit anderer Anwendungen. Prüfe das unter den Bedingungen, in denen du später entwickeln willst: Ein leerer Rechner und ein Rechner mit Editor, Browser und laufender Anwendung sind unterschiedliche Ausgangslagen.

Wenn der Versuch stockt, ändere jeweils eine Einstellung. Verkleinere zunächst die Eingabe oder nutze eine kleinere Modellvariante. Prüfe nach jeder Änderung erneut, ob der gewünschte Code noch verständlich und richtig bearbeitet wird. Eine speichersparende Variante kann andere Antworten liefern.

## Erfasse einen brauchbaren Vergleich

Diese Vorlage ist ein Vorschlag für deinen eigenen Versuch. Sie behauptet keine bereits erhobenen Ergebnisse:

```text
Aufgabe und erwartetes Verhalten:
Modellname und genaue Version:
Quantisierung / gewählte Variante:
Laufzeitprogramm und Version:
Hardware und freie Ausgangskapazität:
Kontextgröße und bereitgestellte Dateien:
CPU/GPU-Zuordnung während des Laufs:
Beobachtete Speicherbelegung:
Wartezeit und Störungen anderer Anwendungen:
Fehler in Erklärung oder Code:
Tatsächlich ausgeführte Prüfung:
```

Verwende beim nächsten Versuch denselben Auftrag und dieselben Dateien. Behalte den Vorschlag des Modells im Original, damit du fachliche Unterschiede nachvollziehen kannst. Wenn du anschließend korrigierst, erfasse diese Nacharbeit separat. Ein schnell erzeugter, aufwendig zu reparierender Vorschlag ist für deine Auswahl anders zu bewerten als eine direkt brauchbare Erklärung.

## Entscheide nach dem Engpass

Du kannst nach diesem Versuch gezielter auswählen. Scheitert bereits das Laden, braucht die Variante mehr verfügbaren Speicher oder eine andere Darstellung. Läuft das Modell, bearbeitet aber den relevanten Kontext unzuverlässig, ist die fachliche Eignung offen. Bleibt die Qualität brauchbar, während der Rechner im Alltag stockt, prüfe eine kleinere Variante mit derselben Aufgabe.

Eine Hardwareempfehlung entsteht erst aus diesen Beobachtungen und deinem tatsächlichen Einsatz. Ein lokales Modell kann für eine begrenzte Aufgabe nützlich sein, ohne alle Aufgaben deines bisherigen Coding-Tools zu übernehmen. Für die Aufteilung größerer Aufträge bietet der [Artikel über unterschiedliche Subagent-Rollen](post:haiku-recherche-opus-code-subagents) einen ergänzenden Einstieg.
