---
titel: "Kosten eines fertigen Features erfassen"
datum: 2026-10-09
kategorie: arbeitsweisen
zusammenfassung: "Feature-Kosten erfassen heißt, Modellaufrufe, Fehlversuche, Reviewzeit und Gesamtdauer bis zur Abnahme gemeinsam sichtbar zu machen. Eine leere Vorlage hilft beim Start."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-10-08-voxyz_ai-haiku-subagents-und-opus-worker
  - 2026-09-24-artificialanlys-2102932119995756613
---

## Kurz gesagt

- Lege fest, wann das Feature als fertig gilt und wann seine Erfassung beginnt.
- Erfasse sämtliche Agent-Läufe einschließlich Fehlversuchen und Korrekturen.
- Halte Modellkosten, aktive menschliche Arbeitszeit und verstrichene Gesamtdauer getrennt fest.
- Kennzeichne unbekannte Beträge und ordne Abo-Ausgaben nach einer ausdrücklich gewählten Methode zu.

## Definiere die Grenze des fertigen Features

Du möchtest wissen, was die Umsetzung eines kleinen Features tatsächlich beansprucht. Als synthetisches Beispiel dient ein Statusfilter in einer vorhandenen Aufgabenliste. Für diesen Beitrag wurden keine eigenen Feature-Kosten gemessen; der Ablauf und die Vorlage sind Vorschläge für deine nächste Erfassung.

Schreibe zuerst die Abnahmekriterien auf. Im Beispiel gehören funktionierender Filter, passende Tests, geprüftes Bedienverhalten und die Freigabe durch die zuständige Person dazu. Soll auch die Veröffentlichung mit Live-Prüfung erfasst werden, nimm sie ausdrücklich in die Grenze auf.

Der Startpunkt ist ebenso wichtig. Beginnt die Erfassung beim ersten Agent-Auftrag, beim Schreiben der Spezifikation oder bereits bei der Recherche? Wähle eine Regel und dokumentiere sie. Ein Vergleich wird schwer lesbar, wenn ein Feature Planung und Deployment enthält, das andere nur den erfolgreichen Coding-Lauf.

Artificial Analysis betrachtet Coding Agents als Kombination aus Modell und Arbeitsumgebung und weist Kosten pro Benchmark-Aufgabe aus. Das verdeutlicht die Bedeutung einer definierten Aufgabe. Ein solcher Benchmark enthält jedoch nicht automatisch deine Planung, menschliche Prüfung oder Veröffentlichung. {q:2}

## Erfasse jeden Lauf bis zur Abnahme

Gib dem Feature eine eindeutige Kennung und ordne ihr alle zugehörigen Läufe zu: Recherche, Umsetzung, Tests, Review und Korrekturen. Erfasse bei delegierten Aufgaben auch die Unterläufe. Ein Subagent ist ein zusätzlich gestarteter Agent mit einer begrenzten Teilaufgabe.

Vox empfiehlt eine Rollenteilung mit leichteren Modellen für Recherche und stärkeren Modellen für Umsetzung und Prüfung. Die angeführte Demo gehört zu einem anderen Versuchsaufbau als der vorgeschlagene Coding-Ablauf. Ihr Ergebnis beantwortet deshalb nicht, was dein fertiges Feature kostet. {q:1}

Für einen eigenen Vergleich hältst du pro Lauf Rolle, tatsächlich verwendetes Modell, Einstellungen, Beginn, Ende und Ergebnis fest. Nutze die angezeigten Nutzungsdaten, wenn sie verfügbar sind. Dokumentiere, ob der Lauf weiterverwendbare Arbeit geliefert hat, korrigiert werden musste oder verworfen wurde.

Ein Fehlversuch bleibt Teil des Features. Dazu gehören auch zusätzliche Recherchen nach einem falschen Ansatz und erneute Tests nach einer Korrektur. Die getrennte Kennzeichnung macht sichtbar, wo Aufwand entsteht, ohne ihn aus der Gesamtrechnung zu entfernen.

## Trenne Geld, Arbeitszeit und Wartezeit

Direkte Modellkosten sind Beträge, die sich einem Lauf nachvollziehbar zuordnen lassen. Eine API ist die Programmierschnittstelle zum Anbieter; bei nutzungsabhängiger Abrechnung können deren Abrechnungsdaten eine Grundlage liefern. Halte Anbieter, Abrechnungsweg, Währung und Herkunft jedes Betrags fest.

Bei einem Abo ist die Zuordnung häufig anders. Erfasse die Abo-Ausgabe zunächst separat. Wenn du einen Anteil dem Feature zurechnen möchtest, beschreibe die gewählte Verteilung, beispielsweise nach erfasster aktiver Nutzung. Das ist eine interne Zuordnung und kann von den zusätzlichen Ausgaben dieses Features abweichen.

Ein unbekannter Anteil am Nutzungslimit bleibt unbekannt. Aus verbleibenden Prozentwerten oder einer Limitmeldung kannst du ohne dokumentierte Umrechnung weder Tokenkosten noch einen Geldbetrag ableiten. Fehlende Angaben werden als „unbekannt“ markiert.

Aktive menschliche Zeit umfasst zum Beispiel Spezifikation, Review und Fehlerklärung. Die Gesamtdauer reicht vom gewählten Start bis zur Abnahme und enthält auch Warten auf CI oder Rückmeldungen. CI bezeichnet die automatischen Prüfungen von Codeänderungen. Bei parallel laufenden Agents darfst du ihre Laufzeiten nicht einfach zur verstrichenen Gesamtdauer addieren.

## Beginne mit einer leeren Erfassungsvorlage

Die folgende Vorlage enthält bewusst keine Messwerte. Du kannst sie für einen eigenen Versuch in eine Tabelle oder eine einfache Datei übernehmen.

| Feld | Einzutragen |
|---|---|
| Feature und Umfang | Kennung, gewünschtes Verhalten, Abnahmegrenze |
| Beginn und Abnahme | Zeitpunkte mit derselben Zeitzone |
| Lauf und Rolle | Kennung, Aufgabe, Modell, Einstellungen |
| Ergebnis des Laufs | Übernommen, korrigiert oder verworfen |
| Direkter Betrag | Wert, Währung, Herkunft oder „unbekannt“ |
| Abo-Zuordnung | Methode, Anteil oder „unbekannt“ |
| Menschliche Arbeit | Tätigkeit und aktive Dauer |
| Weitere Ausgaben | Zum Beispiel eindeutig zurechenbare Runner-Nutzung |
| Abnahme | Erfüllte Kriterien und verbleibende Einschränkungen |

Ergänze einen kurzen Grund für zusätzliche Läufe. „Review fand falsches Filterverhalten“ erklärt die Ausgabe besser als eine weitere Laufkennung allein. So kannst du später zwischen notwendigen Prüfungen, unklaren Aufträgen und technischen Problemen unterscheiden.

Prüfe die Einträge während der Arbeit in kurzen Abständen. Nachträglich erinnerte Arbeitszeit kennzeichnest du als Schätzung. Ein Betrag aus der Abrechnung und eine geschätzte Reviewdauer haben unterschiedliche Herkunft und sollten entsprechend erkennbar bleiben.

## Werte das Ergebnis mit seiner Vollständigkeit aus

Summiere eindeutig zurechenbare direkte Ausgaben zunächst je Währung. Wenn du Euro und Dollar zusammenführen möchtest, halte Umrechnungskurs, Datum und Herkunft fest. Übernimm diese Umrechnung als eigenen nachvollziehbaren Schritt in die Rechnung.

Eine vollständige Gesamtrechnung kann direkte Ausgaben, gewählte Abo-Anteile und intern bewertete Arbeitszeit enthalten. Für Letztere legst du einen eigenen Kostensatz fest und kennzeichnest ihn als Annahme. Zeige die Bestandteile daneben weiter einzeln, damit eine andere Bewertung der Arbeitszeit möglich bleibt.

Fehlen Modellbeträge oder Nutzungsanteile, berichte die bekannte Summe und die offenen Bestandteile. Ein fertig abgenommenes Feature macht eine unvollständige Kostenaufstellung nicht vollständig. Die Lücke selbst ist ein nützliches Ergebnis für die nächste Erfassung.

Halte außerdem fest, wie viel Review und Korrektur nötig waren. Ein Modell kann im einzelnen Lauf günstiger erscheinen und zusätzliche Fehlversuche auslösen. Der Vergleich muss bis zur gleichen Abnahmegrenze reichen, damit dieser Aufwand sichtbar wird.

## Verbessere anschließend einen konkreten Schritt

Suche nach dem größten beeinflussbaren Aufwand. Viele verworfene Ansätze können auf einen unklaren Auftrag hinweisen. Lange menschliche Prüfzeit kann mit großen Änderungen oder fehlenden Ausführungsnachweisen zusammenhängen. Zusätzliche Wartezeit verlangt wiederum eine andere Untersuchung als hohe direkte Modellkosten.

Verändere für den nächsten Versuch einen klar benannten Teil des Ablaufs und behalte Erfassung sowie Abnahmegrenze bei. Unterschiedlich schwierige Features bleiben nur eingeschränkt vergleichbar. Die erste brauchbare Aufgabe ist deshalb überschaubar: Fülle die leere Vorlage für ein tatsächlich fertiggestelltes Feature aus und berichte bekannte Kosten, aktive Arbeitszeit, Gesamtdauer und offene Beträge gemeinsam.
