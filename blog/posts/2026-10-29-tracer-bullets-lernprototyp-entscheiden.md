---
titel: "Tracer Bullets oder Lernprototyp: Was soll weiterleben?"
datum: 2026-10-29
kategorie: arbeitsweisen
zusammenfassung: "Tracer Bullets prüfen einen schmalen echten Integrationspfad. Lernprototypen beantworten eine begrenzte Frage. Entscheide vor dem Agentenauftrag, welcher Code weiterleben soll."
status: freigegeben
geprueft_am: 2026-10-29
freigabe: automatisch
quellen:
  - 2019-09-13-pdf-the-pragmatic-programmer-20th-anniversary-edition
  - 2025-08-18-pdf-beyond-vibe-coding
---

## Kurz gesagt

- Schreibe vor dem ersten Agentenauftrag auf, welche Unsicherheit der Versuch klären soll und ob sein Code weiterverwendet wird.
- Wähle einen Tracer Bullet, wenn du einen schmalen Weg durch die echte technische Umgebung prüfen und weiterentwickeln willst.
- Halte bei einem Lernprototyp fest, welche Teile simuliert sind und welche Aussage die Vorführung überhaupt erlaubt.

## Die erste Demo legt Erwartungen fest

Du willst eine Anwendung bauen, die hochgeladene Dateien prüft und einen Bericht erzeugt. Ein Coding Agent liefert schnell einen überzeugenden Bildschirm. Die Dateiauswahl funktioniert, ein Fortschrittsbalken läuft, anschließend erscheint ein Ergebnis. Ob darin bereits ein nutzbarer Verarbeitungspfad steckt, lässt sich an der Oberfläche kaum erkennen.

David Thomas und Andrew Hunt unterscheiden in [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) deshalb zwei unterschiedliche Versuche: Tracer Bullets und Prototypen. Beide begrenzen den Umfang. Sie stellen aber andere Ansprüche an den entstandenen Code und seine spätere Verwendung. Ihre Unterscheidung steht in den Abschnitten über Tracer Bullets und Prototypen, auf den PDF-Seiten 109 bis 123.{q:1}

Für einen Agentenauftrag lässt sich daraus eine konkrete Entscheidung ableiten: Soll der Versuch eine Frage beantworten, oder soll er bereits das tragfähige Gerüst der Anwendung bilden? Diese Entscheidung gehört vor die Vorführung. Sonst entsteht leicht die Erwartung, dass nur noch weitere Funktionen ergänzt werden müssen.

## Ein Lernprototyp beantwortet eine bestimmte Frage

In unserem gedachten Importprojekt könnte zunächst unklar sein, ob die vorgesehene Bibliothek schwierige Dateien überhaupt lesen kann. Dafür reicht ein isolierter Versuch mit geeigneten Beispieldateien. Eine Benutzerverwaltung, eine Datenbank und ein fertiger Berichtseditor helfen bei dieser Frage wenig.

Der Prototyp darf Eigenschaften weglassen, die für seinen Lernzweck keine Rolle spielen. Thomas und Hunt nennen unter anderem Vollständigkeit, Robustheit und Gestaltung. In ihrer Begriffsverwendung wird der Versuchscode verworfen; die gewonnene Erkenntnis bleibt. Auch ein erfolgreicher Versuch wird dadurch nicht automatisch zur Produktbasis.{q:1}

Der Abschluss dieses Auftrags müsste erklären, welche Dateien untersucht wurden, welche Fälle funktionierten und wo die Grenzen liegen. Eine attraktive Oberfläche allein würde die Bibliotheksfrage offenlassen. Umgekehrt wäre ein schmuckloser Versuch ausreichend, wenn er genau diese Unsicherheit nachvollziehbar verringert.

## Ein Tracer Bullet verbindet die echten Teile

Eine andere Frage lautet, ob Upload, Verarbeitung, Speicherung und Ergebnisabruf im geplanten Stack zusammenspielen. Hier bietet sich ein Tracer Bullet an: ein dünner funktionierender Durchstich durch den technischen Gesamtpfad. Er besitzt wenig Funktionsbreite, erhält aber eine angemessene Struktur, Fehlerbehandlung und Prüfung. Sein Code wird anschließend weitergebaut.{q:1}

Für unser Beispiel könnte zunächst ein begrenztes Dateiformat genügen. Der Upload erreicht die Verarbeitung, der Bericht wird gespeichert und lässt sich später wieder abrufen. Ein unzulässiger Eingang erhält eine verständliche Ablehnung. Ob der Bericht bereits alle gewünschten Ansichten hat, ist für diesen ersten Integrationsnachweis zweitrangig.

Dieser Weg kostet mehr als eine rein visuelle Attrappe. Dafür prüft er eine andere Unsicherheit. Wer einen echten Durchstich beauftragt, sollte sich deshalb auch den Datenfluss und einen passenden Fehlerfall zeigen lassen. Ein vorgefülltes Ergebnis im Browser ersetzt diese Verbindung nicht.

## Das Wort Prototyp reicht als Übergabevertrag nicht

Addy Osmani verwendet den Begriff in Beyond Vibe Coding weiter. Für den Übergang zur dauerhaften Nutzung erlaubt er sowohl einen Neubau anhand des Prototyps als auch eine schrittweise Überarbeitung. In beiden Fällen müssen fehlende Architektur, Persistenz, Fehlerbehandlung und Prüfungen bewusst ergänzt werden. Das unterscheidet sich von der ausdrücklichen Wegwerfregel bei Thomas und Hunt.{q:2}

Die Entscheidung hängt deshalb an der tatsächlichen Verwendung des Wortes. Ein Team kann einen vorläufigen Stand bewusst härten. Es sollte dabei jedoch sagen können, welche Eigenschaften bereits tragfähig sind und welche noch fehlen. Der bloße Satz „Wir machen aus dem Prototyp das Produkt“ liefert diese Information nicht.

Übertrage die Begriffe nicht ungeprüft zwischen Aufträgen. Wenn du Versuchscode übernehmen möchtest, beschreibe die Übernahmeentscheidung und ihre Qualitätsanforderungen ausdrücklich. So bleibt erkennbar, ob der Code weiterentwickelt, ersetzt oder nur als Anschauung benutzt wird.

## Übergib bekannte Attrappen mit ihrer Bedeutung

Osmani empfiehlt, bewusste Abkürzungen beim Entstehen festzuhalten. Dazu zählen etwa Daten im Arbeitsspeicher, simulierte Anmeldung oder eine Konsolenausgabe anstelle einer versandten E-Mail. Sein Register soll verhindern, dass solche Vereinfachungen beim Übergang verloren gehen.{q:2}

Im Importbeispiel könnte die Übergabe folgende Unterschiede sichtbar machen:

| Bestandteil | Was der Versuch zeigt | Was damit offenbleibt |
|---|---|---|
| Bericht aus vorbereiteten Daten | Ob die Darstellung verständlich ist | Ob eine reale Datei korrekt verarbeitet wird |
| Speicherung nur im Browserzustand | Ob der Ablauf bedienbar ist | Ob ein Bericht nach einem Neustart verfügbar bleibt |
| Echter Upload mit vereinbartem Fehlerfall | Ob dieser technische Pfad zusammenarbeitet | Ob weitere Formate und große Datenmengen funktionieren |

Diese Tabelle ist eine eigene Anwendung auf das gedachte Projekt. Sie verhindert, dass unterschiedliche Ergebnisse als derselbe Fortschritt gemeldet werden. Beschreibe bei jeder Attrappe, welche Beobachtung sie trotzdem erlaubt und vor welcher Nutzung sie ersetzt werden muss.

## Gib dem Agenten einen passenden ersten Auftrag

Für einen Lernversuch kannst du verlangen: „Untersuche, ob die Bibliothek unsere schwierigen Beispieldateien korrekt liest. Begrenze den Versuch auf diese Frage und beschreibe seine Grenzen.“ Für einen Tracer Bullet lautet der Auftrag eher: „Verbinde Upload, Verarbeitung und gespeicherten Ergebnisabruf für das vereinbarte Format. Zeige den Erfolgsweg und die vorgesehene Ablehnung.“

Beide Aufträge brauchen ein klares Ende. Der erste endet mit einer nachvollziehbaren Erkenntnis, der zweite zusätzlich mit einem weiterverwendbaren Integrationspfad. Weitere Funktionen kommen erst dazu, wenn der bisherige Versuch seine Frage beantwortet hat.

Wähle für deinen nächsten Entwicklungsstart die schwierigste aktuelle Unsicherheit. Entscheide anschließend über Lernprototyp oder Tracer Bullet und schreibe die erlaubte Weiterverwendung des Codes in den Auftrag. Bei einem übernommenen Gerüst hilft dir später der [Verhaltensvergleich beim Refactoring](post:refactoring-verhalten-gleich-pruefen).
