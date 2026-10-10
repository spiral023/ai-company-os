---
titel: "Refactoring mit Codex: Prüfe, dass das Verhalten gleich bleibt"
datum: 2026-10-09
kategorie: arbeitsweisen
zusammenfassung: "Prüfe Verhaltenserhalt beim Refactoring mit identischen Eingaben vor und nach der Änderung. Kleine Schritte, stabile Schnittstellen und gezielte Sonderfälle halten den Vergleich nachvollziehbar."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-10-09-openai-refactoring
  - 2026-02-04-tweag-tdd-agentic-coding
---

## Kurz gesagt

- Beschreibe vor dem Refactoring die beobachtbaren Ausgaben und öffentlichen Schnittstellen.
- Vergleiche alte und neue Umsetzung mit denselben Eingaben, einschließlich relevanter Sonderfälle.
- Ändere pro Schritt ein strukturelles Thema und prüfe anschließend den betroffenen Ablauf.
- Trenne gewünschte Verhaltensänderungen, Abhängigkeitswechsel und Migrationen in eigene Aufträge.

## Lege fest, was gleich bleiben soll

Eine große Funktion in kleinere Teile zu zerlegen klingt überschaubar. Trotzdem kann dabei eine leere Eingabe anders behandelt werden, eine Fehlermeldung verschwinden oder eine bestehende Reihenfolge wechseln. Deshalb braucht „Verhalten erhalten“ eine konkrete Beschreibung.

OpenAIs Anleitung zum Refactoring empfiehlt, den betroffenen Bereich zuerst zu untersuchen. Vor einer Änderung soll Codex das aktuelle Verhalten, die gewünschte strukturelle Verbesserung und eine passende Prüfung nennen. Die Umsetzung erfolgt in kleinen, überprüfbaren Schritten; größere Architekturwechsel und Migrationen bleiben separate Aufgaben.{q:1}

Mein Vorschlag: Schreibe zuerst auf, was andere Teile des Systems an dieser Stelle beobachten. Dazu gehören Rückgabewerte, Fehler, veränderte Daten und ausgelöste Nebenwirkungen. Eine öffentliche Schnittstelle ist dabei ein Vertrag, auf den aufrufender Code angewiesen ist, etwa die Parameter und Rückgabewerte einer exportierten Funktion oder das Format einer API-Antwort.

Wenn du dabei ein bestehendes Fehlverhalten entdeckst, entscheide über dessen Korrektur separat. Sonst lässt sich am fertigen Diff schwer erkennen, welche Unterschiede beabsichtigt waren und welche beim Umbau entstanden sind.

## Das synthetische Beispiel: CSV-Formatierung herauslösen

Die folgende Situation ist ein synthetisches Beispiel. Eine bestehende Exportfunktion lädt Kontakte, formatiert ihre Felder und schreibt die fertige CSV-Datei. Du möchtest die Formatierung in eine eigene Funktion verschieben, damit der Ablauf leichter lesbar wird. Das Dateiformat soll dabei gleich bleiben.

Als Beispielvertrag legen wir fest: Die Spalten heißen weiterhin `name`, `email` und `notes`, ihre Reihenfolge bleibt gleich, und fehlende Anmerkungen werden als leeres Feld ausgegeben. Sonderzeichen behalten die bisherige Maskierung. Maskierung bedeutet hier, dass Zeichen wie ein Spaltentrenner eindeutig als Feldinhalt dargestellt werden.

Der kleinste passende Schritt wäre, die vorhandene Formatierung ohne fachliche Anpassung herauszulösen und ihren bisherigen Aufrufer umzuleiten. Eine neue Bibliothek, andere Spaltennamen oder eine veränderte Behandlung fehlender Werte würden zusätzliche Entscheidungen eröffnen.

Bitte den Agent vorab zu erklären, welche Werte die Funktion erhält und welchen Einfluss sie auf ihre Eingaben hat. Falls sie die Kontaktliste bisher sortiert oder verändert, gehört auch das zum Vergleich. Eine formal gleiche Ausgabe kann trotzdem mit einem anderen Zustand für den aufrufenden Code einhergehen.

## Vergleiche identische Eingaben vor und nach dem Umbau

Das folgende Prüfverfahren ist mein Vorschlag für diesen Beispielvertrag. Es beschreibt keinen bereits ausgeführten Test.

Lege die Eingaben vor der Änderung fest und verwende sie unverändert für beide Implementierungen. Halte die Ausgabe des bisherigen Ablaufs fest. Nach dem Refactoring vergleichst du die neue Ausgabe mit dieser Ausgangsausgabe und zusätzlich mit dem vereinbarten Vertrag.

| Eingabefall | Was du vergleichst |
|---|---|
| Vollständiger Kontakt | Inhalt und Reihenfolge sämtlicher Spalten |
| Fehlende Anmerkung | Leeres Feld und weiterhin vorhandene Spaltenposition |
| Leere Zeichenfolge | Unterschied oder Gleichbehandlung gegenüber einem fehlenden Wert |
| Umlaut im Namen | Unveränderte Zeichen und passende Dateikodierung |
| Spaltentrenner oder Zeilenumbruch im Feld | Bisherige Maskierung und Struktur der Ausgabe |
| Leere Kontaktliste | Verhalten von Kopfzeile und Dateiinhalt |

Bei einer reinen Formatierungsfunktion kannst du direkt deren Rückgabewert vergleichen. Prüfe bei einem vollständigen Export außerdem den tatsächlich erzeugten Dateiinhalt. Achte darauf, dass beide Varianten dieselben Voraussetzungen erhalten, etwa dieselbe Sortierung und dieselben Beispielkontakte.

Variable Bestandteile wie Zeitstempel oder zufällige IDs erschweren den Vergleich. Verwende dafür im Test kontrollierte Werte oder prüfe eine klar festgelegte Eigenschaft. Erkläre jede Auslassung: Wenn du einen Teil der Ausgabe aus dem Vergleich entfernst, bleibt dessen Verhalten dort ungeprüft.

## Halte die Prüfung unabhängig von der neuen Lösung

Ein neu geschriebener Test kann die neue Implementierung ungewollt nachbilden. Zum Beispiel übernimmt er dieselbe fehlerhafte Umwandlung fehlender Werte. Leite die Erwartungen deshalb aus dem beschriebenen Vertrag und dem bisherigen Verhalten ab.

Das Tweag-Handbuch behandelt Tests als kleinteilige Beschreibung des gewünschten Verhaltens und empfiehlt Refactoring bei grünen Tests. Die im Bestand erfasste Darstellung weist zugleich darauf hin, dass die Qualität dieser Tests beim Anwender liegt.{q:2}

Mein Vorschlag für deinen Ablauf: Führe die passende Prüfung bereits am Ausgangszustand aus. Falls sie dort fehlschlägt, untersuche die Ursache, bevor du daraus eine Bewertung der strukturellen Änderung ableitest. Nach jedem kleinen Schritt verwendest du dieselbe Prüfung erneut.

Grüne Tests decken nur ihre erfassten Fälle ab. Ein Vergleich vieler Ausgaben kann ebenso wichtige Fehlerwege übersehen. Ergänze deshalb gezielt die Stellen, an denen du Code verschiebst: etwa Ausnahmebehandlung, veränderte Eingaben oder die Reihenfolge ausgelöster Aktionen.

## Prüfe auch die Aufrufer und öffentlichen Schnittstellen

Eine herausgelöste Hilfsfunktion kann korrekt arbeiten, während ihr Aufrufer einen Rückgabewert falsch weiterverwendet. Lies deshalb die bisherigen Aufrufstellen und prüfe, ob Parameter, Fehler und Nebenwirkungen weiterhin gleich ankommen.

Bewahre im Beispiel die bisherige öffentliche Exportfunktion. Die neue interne Formatierungsfunktion kann darunterliegen. Andere Module müssen dann ihren bekannten Aufruf nicht gleichzeitig ändern. Falls du die öffentliche Schnittstelle bewusst verändern willst, ist dafür ein eigener Plan mit den betroffenen Aufrufern sinnvoll.

OpenAI empfiehlt, pro Durchgang ein Aufräumthema zu wählen und nach jedem Schritt die kleinste nützliche Prüfung auszuführen. Ein Wechsel von Framework oder Abhängigkeiten erweitert den Umfang und soll separat behandelt werden.{q:1}

Für ein anschließendes Review eignen sich die [Prompts für Review und Abnahme](post:prompts-fuer-review-und-abnahme). Gib dem Reviewer dazu den ursprünglichen Vertrag und den fertigen Diff, damit er gezielt nach beobachtbaren Abweichungen suchen kann.

## Ein Auftrag für den nächsten Refactoring-Schritt

Dieser selbst formulierte Auftrag verbindet Umfang und Prüfung:

> Untersuche die bestehende CSV-Exportfunktion und ihre Aufrufer. Beschreibe das aktuelle Ausgabeformat, Fehlerverhalten und mögliche Änderungen an Eingaben. Schlage den kleinsten Schritt vor, um ausschließlich die Formatierung herauszulösen. Öffentliche Parameter und Rückgabewerte bleiben stabil. Lege vor der Umsetzung identische Vergleichseingaben und passende Sonderfälle fest. Prüfe den Ausgangszustand und anschließend denselben Ablauf nach der Änderung. Berichte die tatsächlichen Ergebnisse, Unterschiede und ungeprüften Bereiche. Behandle gewünschte Verhaltensänderungen separat.

Übernimm den nächsten Schritt erst, wenn du erklären kannst, welche Struktur verbessert wurde und welches Verhalten geprüft ist. Wenn der Umbau neue fachliche Entscheidungen verlangt, grenze diese aus und plane sie eigenständig. Damit bleibt jeder Vergleich verständlich, auch wenn später weitere Refactoring-Schritte folgen.
