---
titel: "Vibe Coding: Von der Demo zur Produktreife"
datum: 2026-10-29
kategorie: arbeitsweisen
zusammenfassung: "Eine überzeugende KI-Demo lässt wichtige Fragen offen. So erkennst du den Wechsel zum Engineering, hältst Abkürzungen fest und prüfst den Weg zur echten Nutzung."
status: freigegeben
geprueft_am: 2026-10-29
freigabe: automatisch
quellen:
  - 2025-08-18-pdf-beyond-vibe-coding
---

## Kurz gesagt

- Lege fest, welche Frage deine Demo beantworten soll und was sie noch simulieren darf.
- Führe ein kurzes Register der Abkürzungen, bevor sich Attrappen wie fertige Funktionen anfühlen.
- Prüfe beim Übergang zur echten Nutzung konkrete Abläufe, Fehler und Folgen.

## Was du aus einer schnellen Demo erfahren kannst

Du beschreibst eine Anwendung, ein Coding Agent erzeugt die Oberfläche, und wenige Anpassungen später lässt sie sich vorführen. Ein Coding Agent ist ein KI-gestütztes Programm, das Dateien bearbeiten und Entwicklungswerkzeuge aufrufen kann. Das ist wertvoll: Eine Idee wird sichtbar, und du kannst früh herausfinden, ob der Ablauf verständlich ist.

Addy Osmani behandelt diesen Nutzen und seine Grenzen in [Beyond Vibe Coding: From Coder to AI-Era Developer](https://www.oreilly.com/library/view/beyond-vibe-coding/9798341634749/). Sein Buch von 2025 beschreibt Vibe Coding als explorative Arbeit im Gespräch mit KI. Systematisches Engineering ergänzt Anforderungen, bewusste Entwurfsentscheidungen und Prüfungen. Beide Arbeitsweisen können im selben Projekt aufeinanderfolgen. Entscheidend sind Zweck und Folgen der Aufgabe. (PDF-S. 18–26.){q:1}

Mein Vorschlag: Beurteile eine Demo zuerst danach, welche Unsicherheit sie tatsächlich verkleinert hat. Vielleicht verstehst du jetzt die Navigation besser. Ob Daten zuverlässig gespeichert werden, bleibt eine eigene Frage.

## Warum die 70 Prozent keine Fertigstellungsquote sind

Osmani nennt die Lücke zwischen schnell erzeugter Hauptfunktion und belastbarer Anwendung das „70%-Problem“. Die schwierige Restarbeit betrifft unter anderem Randfälle, Wartbarkeit und Integration: das Zusammenführen der Teile und die Prüfung ihres gemeinsamen Verhaltens. Erfahrene Entwickler erledigen einen Teil davon bereits während der scheinbar mühelosen Generierung. (PDF-S. 81–90.){q:1}

Die Zahl ist eine Metapher. Das Buch gibt dafür keine einheitliche Messgröße oder gemeinsame Aufgabenmenge an. Du kannst daraus weder eine feste Modellgrenze noch einen erwartbaren Restaufwand berechnen.

Für deine Planung helfen beschreibbare Zustände: Die Oberfläche ist vorführbar. Ein Ablauf mit echten Daten wurde geprüft. Fehlerfälle sind untersucht. Die Anwendung wurde unter den vorgesehenen Bedingungen ausprobiert. Jeder Zustand beantwortet andere Fragen und macht den nächsten Arbeitsschritt greifbarer.

## Wechsle den Arbeitsmodus, wenn die Folgen wachsen

Ein Prototyp ist ein vorläufiger Entwurf, mit dem du eine Idee untersuchst. Ein Experiment mit synthetischen Daten kann dir schnelle Rückmeldung geben. Sobald Menschen sich auf gespeicherte Informationen, versandte Nachrichten oder gemeinsam genutzte Zustände verlassen, entstehen weitere Anforderungen.

Osmani empfiehlt den bewussten Übergang vom schnellen Prototyp zur belastbaren Umsetzung. Dafür kommen ein Neubau anhand der gewonnenen Erkenntnisse und eine schrittweise Überarbeitung infrage. Welche Variante passt, hängt vom Zustand des Entwurfs ab. (PDF-S. 129–132.){q:1}

Meine daraus abgeleitete Regel: Prüfe den Moduswechsel bei einer neuen Verpflichtung. Muss etwas nach einem Neustart vorhanden sein? Können zwei Personen denselben Zustand verändern? Hat ein Fehler Auswirkungen außerhalb der Demo? Diese Fragen machen den zusätzlichen Qualitätsbedarf sichtbar.

Ein anderes Werkzeug oder ein lokaler Projektordner kann den Übergang unterstützen. Die offenen Anforderungen musst du trotzdem einzeln bearbeiten.

## Ein Terminplaner als hypothetisches Beispiel

Stell dir einen erfundenen Prototyp für die Reservierung von Vereinsräumen vor. Du willst zunächst herausfinden, ob Mitglieder einen freien Raum und einen passenden Zeitraum auswählen können.

Der Agent erzeugt einen Kalender mit Beispieldaten. Nach dem Klick erscheint eine Bestätigung. Die Auswahl liegt nur im Browser und verschwindet nach dem Neuladen. Für einen ersten Verständlichkeitstest kann das ausreichen, wenn du den Versuchsstatus klar benennst.

Nun soll der Vorstand echte Reservierungen entgegennehmen. Damit ändern sich die Fragen: Was passiert bei zwei gleichzeitigen Anfragen? Wie wird ein geänderter Zeitraum behandelt? Welche Zeitzone gilt? Können Mitglieder eine Bestätigung später wiederfinden?

Die schöne Kalenderansicht beantwortet diese Fragen noch nicht. Ein sinnvoller nächster Schritt wäre ein kleiner, echter Reservierungsablauf in einer geeigneten Testumgebung. Sein Verhalten wird anhand vorher vereinbarter Fälle geprüft.

## Halte jede bewusste Abkürzung fest

Osmani empfiehlt, vereinfachte Teile während der Prototypentwicklung zu erfassen. Er nennt etwa Daten im Speicher, simulierte Anmeldung oder E-Mails, die lediglich in einer Konsole erscheinen. So bleiben die offenen Aufgaben beim Übergang zur echten Anwendung sichtbar. Ein klares Prototypziel begrenzt zugleich zusätzliche Funktionen. (PDF-S. 133–134.){q:1}

Für den Terminplaner könnte dein Register drei kurze Einträge enthalten:

| Abkürzung | Was du damit untersuchen kannst | Was noch offen ist |
|---|---|---|
| Erfundene Termine | Verständlichkeit der Kalenderansicht | Laden und Aktualisieren echter Reservierungen |
| Bestätigung nur auf dem Bildschirm | Verständlichkeit der Rückmeldung | Dauerhaftes Wiederfinden der Reservierung |
| Einzelne Testsitzung | Ablauf für eine Person | Verhalten bei gleichzeitiger Nutzung |

Mein Zusatz ist die mittlere Spalte. Sie hält den Wert des Experiments fest und verhindert zugleich, dass sein Ergebnis über den untersuchten Bereich hinaus verallgemeinert wird.

## Prüfe den Übergang an einem vollständigen Ablauf

Für die Übernahme würde ich einen normalen Vorgang und wenige entscheidende Abweichungen auswählen. Im Beispiel wird eine Reservierung angelegt, nach einem Neuladen wiedergefunden und anschließend geändert. Ein zweiter Versuch betrifft einen bereits vergebenen Zeitraum. Bei einer Ablehnung sollte der gespeicherte Zustand nachvollziehbar bleiben.

Osmani betont, dass lokale Komponentenprüfungen und vollständige Abläufe unterschiedliche Probleme sichtbar machen. Auch langsame Verbindungen, hilfreiche Fehler und tatsächliche Bedienung gehören zur Lücke zwischen Demo und Produkt. (PDF-S. 86–90, 146–151.){q:1}

Generierte Tests kannst du dabei nutzen. Ihre Erwartungen müssen zu den vereinbarten Regeln passen. Der Beitrag [Grüne Tests, aber der Bug bleibt](post:gruene-tests-bug-bleibt) erklärt diese Grenze genauer.

## Entscheide den nächsten Schritt ausdrücklich

Nimm deinen aktuellen Prototyp und schreibe heute drei Dinge auf: seine ursprüngliche Lernfrage, seine bewussten Abkürzungen und den nächsten Ablauf, den echte Nutzung verlangt.

Entscheide anschließend, ob die vorhandene Struktur diesen Ablauf sinnvoll tragen kann. Falls ja, überarbeite sie in kleinen prüfbaren Schritten. Falls ein Neubau klarer ist, übernimm die gewonnenen Erkenntnisse und bestätigten Interaktionen in den neuen Auftrag.
