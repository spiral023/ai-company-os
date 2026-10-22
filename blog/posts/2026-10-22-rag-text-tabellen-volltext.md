---
titel: "Wissensmanagement mit KI: RAG braucht für Tabellen einen eigenen Weg"
datum: 2026-10-22
kategorie: arbeitsweisen
zusammenfassung: "Wissensmanagement mit KI braucht passende Zugriffe: Textsuche für Inhalte, Tabellenabfragen für Summen und vollständige Dokumente für Zusammenhang. So prüfst du dein RAG-System."
status: freigegeben
geprueft_am: 2026-10-22
freigabe: automatisch
quellen:
  - 2025-09-22-julian-ivanov-ki-automat-das-ultimative-rag-system-n8n-nextcloud-mistral
---

## Kurz gesagt

- Ordne Fragen dem passenden Zugriff zu: Text suchen, Tabellen berechnen oder ein vollständiges Dokument laden.
- Verbinde Textabschnitte und Tabellen mit ihrer Originaldatei, damit Antworten und Aktualisierungen nachvollziehbar bleiben.
- Prüfe geänderte und entfernte Dokumente ebenso wie die erste erfolgreiche Antwort.
- Beginne mit bekannten Fragen und Sollantworten, bevor du weitere Dienste in deinen Ablauf einbaust.

## RAG mit OCR und Tabellen braucht unterschiedliche Zugriffe

Du fragst deinen Dokumentenchat nach den gesamten Ausgaben eines Projekts. Er findet einen Absatz mit einem passenden Betrag und formuliert eine überzeugende Antwort. Die übrigen Zeilen der Tabelle hat er dabei möglicherweise gar nicht ausgewertet.

Für Wissensmanagement mit KI musst du festlegen, welche Informationsarbeit die Frage verlangt. Eine Textstelle finden, eine Summe berechnen und einen Ablauf vollständig erklären brauchen unterschiedliche Zugriffe.

Julian Ivanov beschreibt in seinem RAG-Tutorial vom 22. September 2025 einen Aufbau mit getrennten Werkzeugen für Textsuche, Tabellenabfragen und vollständige Dokumente. Die Dienstekombination stammt aus dem damaligen Tutorial; hier geht es um die Aufteilung der Aufgaben. Die gezeigten Beispiele liefern keinen allgemeinen Qualitätsvergleich.{q:1}

Die folgende Zuordnung ist ein Vorschlag für deinen eigenen Einstieg:

| Frage | Passender Zugriff | Was du am Ergebnis prüfen solltest |
|---|---|---|
| „Wo wird die Lieferfrist erklärt?“ | Relevante Textabschnitte suchen | Gehört die Passage zum richtigen Dokument und Vorgang? |
| „Wie hoch sind die Ausgaben für dieses Projekt?“ | Strukturierte Tabellen abfragen | Stimmen Projektfilter, Zeitraum, Einheit und einbezogene Zeilen? |
| „Welche Schritte gehören zur Inbetriebnahme?“ | Gefundene Anleitung bei Bedarf vollständig laden | Fehlen Voraussetzungen, Warnungen oder spätere Schritte? |

## Tabellenabfragen müssen die richtige Frage berechnen

Im Tutorial landen Tabellenzeilen zusätzlich als strukturierte Datensätze in einer Datenbank. Der Agent wählt einen Abfrageweg; die Datenbank führt die Berechnung aus. Textdokumente erhalten einen eigenen Verarbeitungspfad.{q:1}

Damit kannst du eine Summe über den relevanten Tabellenbestand berechnen lassen. Eine Suche nach ähnlichen Textabschnitten beantwortet zunächst, welche Ausschnitte zur Frage passen. Aus dieser Auswahl ergibt sich noch keine vollständige Berechnungsgrundlage.

Auch eine ausgeführte Tabellenabfrage kann die falsche Frage beantworten. In einem synthetischen Projektbeispiel könnte sie alle Ausgaben erfassen, obwohl nur bereits bezahlte Positionen gefragt sind. Oder sie addiert Werte mit verschiedenen Einheiten. Der Rechenweg kann technisch funktionieren und fachlich danebenliegen.

Lege deshalb zu einer wichtigen Frage fest, welche Zeilen dazugehören und welche ausgeschlossen sind. Lass dir den verwendeten Filter und die Quelldatei nennen. Prüfe die Antwort gegen eine unabhängig bestimmte Erwartung. Eine plausible Zahl allein erklärt ihren Geltungsbereich nicht.

## Lade Zusammenhang gezielt nach

Textsuche arbeitet häufig mit Chunks, also Ausschnitten eines Dokuments. Das begrenzt den Inhalt, den der Agent für eine Antwort verarbeiten muss. Ivanovs Ablauf erlaubt zusätzlich, über die Datei-ID den vollständigen Dokumenttext zu laden, wenn die gefundenen Ausschnitte nicht genügen.{q:1}

Bei einer Anleitung kann der relevante Treffer mitten im Ablauf beginnen. Die Voraussetzung steht weiter oben, eine Ausnahme im nächsten Abschnitt. Nimm solche Fragen in deine Prüfung auf: Kann das System den fehlenden Zusammenhang nachladen und seine Antwort danach korrigieren?

Volltextzugriff ersetzt keine richtige Extraktion. Wenn OCR eine Tabellenüberschrift falsch erkennt oder eine Abbildung verloren geht, kann der nachgeladene Text denselben Fehler enthalten. Prüfe bei einem strittigen Ergebnis zuerst den extrahierten Inhalt gegen das Original. Mehr Kontext hilft nur bei Informationen, die im zugänglichen Bestand vorhanden sind.

Für eine gezielte Frage genügt oft ein kurzer Ausschnitt. Lade zusätzliche Inhalte, wenn sie für die Antwort gebraucht werden. Ein vollständiges Handbuch bei jeder Nachfrage erhöht die zu verarbeitende Textmenge, ohne automatisch die entscheidende Passage besser auffindbar zu machen.

## RAG-Quellen aktualisieren gehört zur Antwortqualität

Im Tutorial verbindet eine gemeinsame Datei-ID Original, Metadaten und abgeleitete Inhalte. Änderungen und entfernte Originale werden mit dem gespeicherten Bestand abgeglichen. Wie der Ablauf nach einem Teilfehler zuverlässig wieder ansetzt, bleibt jedoch offen.{q:1}

Prüfe diesen Lebenszyklus mit einem begrenzten Testbestand. Ändere eine bekannte Aussage im Original und stelle die passende Frage erneut. Kontrolliere anschließend, ob die Antwort den neuen Inhalt verwendet und weiterhin zur richtigen Datei führt.

Entferne danach eine dafür angelegte Testdatei aus dem aktiven Bestand. Ihre alten Textabschnitte und Tabellenzeilen dürfen bei einer Frage nach dem aktuellen Bestand nicht unbemerkt weiterverwendet werden. Falls historische Inhalte gewollt sind, muss ihr Stand erkennbar bleiben.

Unterbrich außerdem eine Aktualisierung an einer kontrollierten Stelle. Untersuche, ob der alte Inhalt erhalten bleibt, ein unvollständiger Stand sichtbar wird oder ein erneuter Lauf die Verarbeitung sauber abschließt. Das ist ein vorgeschlagener Testablauf; hier wurde kein RAG-System damit abgenommen.

## Begrenze den Aufbau auf die Fragen deiner Nutzer

Getrennte Verarbeitungspfade brauchen Pflege: Dokumente extrahieren, Tabellen zuordnen, Aktualisierungen verfolgen und Ergebnisse prüfen. Für einen überschaubaren Bestand mit reinen Textfragen kann eine einfache Suche ausreichen.

Wähle zunächst typische Fragen aus deiner Arbeit. Halte die erwarteten Dokumente, Filter und Antworten fest. Ergänze einen fehlenden Inhalt, eine mehrdeutige Frage und eine geänderte Datei. So prüfst du, ob dein System sinnvoll antwortet, nachfragt oder seine Grenze nennt.

Wenn du diese Fälle später automatisiert vergleichst, hilft der [Beitrag zu Evals mit getrennten Testfällen](post:hillclimbing-mit-holdout). Beginne für dein RAG-System mit einer konkreten Fehlantwort und verfolge sie bis zur Quelldatei, zum gewählten Zugriff und zum verwendeten Datenstand.
