---
titel: "Agentencode prüfen: Wenn alles zur falschen Annahme passt"
datum: 2026-10-29
kategorie: arbeitsweisen
zusammenfassung: "API, Oberfläche und Tests können denselben fachlichen Irrtum übernehmen. So findest du gemeinsame Fehlannahmen und prüfst Agentencode mit unabhängigen Beispielen."
status: freigegeben
geprueft_am: 2026-10-29
freigabe: automatisch
quellen:
  - 2025-08-18-pdf-beyond-vibe-coding
---

## Kurz gesagt

- Suche vor der Codeprüfung die fachlichen Entscheidungen hinter der erzeugten Lösung.
- Prüfe entscheidende Fälle gegen Regeln, die außerhalb derselben Generierung bestätigt wurden.
- Verfolge einen solchen Fall durch Speicherung, Schnittstelle, Oberfläche und Tests.

## Wie eine falsche Annahme ein ganzes Ergebnis prägt

Ein Coding Agent liefert zusammenpassenden Code. Ein solcher KI-Assistent kann Dateien bearbeiten und Entwicklungswerkzeuge aufrufen. Die Oberfläche verwendet die Felder der Schnittstelle, die Speicherung übernimmt dieselben Werte, und die Tests laufen erfolgreich. Beim Ausprobieren fällt trotzdem auf: Die Anwendung behandelt den eigentlichen Vorgang falsch.

Addy Osmani beschreibt dieses Risiko in [Beyond Vibe Coding: From Coder to AI-Era Developer](https://www.oreilly.com/library/view/beyond-vibe-coding/9798341634749/). Er nennt es „coherent incorrectness“: Eine falsche Anfangsannahme wird über mehrere Entscheidungen und Dateien hinweg konsistent ausgebaut. Dadurch kann der Irrtum später schwerer zu erkennen und aufwendiger zu korrigieren sein. (PDF-S. 213–214.){q:1}

Das Buch von 2025 liefert damit einen hilfreichen Blick auf das Review, also die Prüfung eines Änderungsvorschlags. Du prüfst sowohl das Zusammenspiel der Teile als auch die Bedeutung, die sie gemeinsam umsetzen.

## Finde die Entscheidung hinter dem Feld

Ein Datenfeld sieht oft wie eine technische Einzelheit aus. Dahinter kann eine Fachentscheidung stecken: Wann gilt etwas als abgeschlossen? Darf eine Änderung rückgängig gemacht werden? Welche Zeitzone bestimmt einen Tageswechsel?

Wenn der Auftrag diese Frage offenlässt, muss jemand eine Antwort ergänzen. Der Agent kann eine verbreitete Konvention wählen und sie anschließend überall verwenden. Osmani warnt auch allgemein vor der „majority solution“: Eine typische Lösung muss für den konkreten Zusammenhang nicht passen. (PDF-S. 113–115.){q:1}

Mein Vorgehensvorschlag ist, vor dem Lesen langer Änderungen wenige solche Entscheidungen zu sammeln. Suche besonders nach Statuswerten, Grenzwerten, Standardwerten und automatisch ausgeführten Folgeschritten. Frage jeweils, woher ihre Bedeutung kommt und wer sie für diesen Anwendungsfall bestätigt hat.

## Eine ausgeliehene Kamera als hypothetisches Beispiel

Stell dir eine erfundene Anwendung für den Geräteverleih eines Fotoclubs vor. Eine Kamera soll nach der Rückgabe erst kontrolliert werden, bevor ein anderes Mitglied sie ausleihen kann.

Der Auftrag an den Agenten lautet zu knapp: „Ergänze die Rückgabe.“ Der Agent nimmt an, dass Rückgabe sofortige Verfügbarkeit bedeutet. Er speichert den Status „verfügbar“, liefert ihn über die Programmierschnittstelle aus und zeigt einen grünen Verfügbarkeitsindikator an. Seine Tests erwarten nach der Rückgabe ebenfalls „verfügbar“.

Alle Teile stimmen überein. Der Club braucht jedoch einen Zwischenzustand für die Kontrolle. Diese Regel fehlt in der gesamten Umsetzung.

Das Beispiel ist bewusst erfunden. Es zeigt, warum selbst ein sorgfältiger technischer Review den Fachirrtum übersehen kann, wenn er nur die erzeugten Teile miteinander vergleicht.

## Bestätige einen entscheidenden Fall unabhängig

Unabhängig bedeutet hier: Die erwartete Antwort entsteht außerhalb derselben ungeprüften Annahme. Im Beispiel könnte die zuständige Person für den Verleih den Ablauf bestätigen. Vielleicht existiert bereits eine verbindliche Beschreibung des Kontrollschritts.

Mein Vorschlag wäre ein konkreter Fall: Die Kamera wird zurückgegeben, ist aber noch nicht geprüft. Ein weiteres Mitglied darf sie noch nicht reservieren. Erst eine bestätigte Kontrolle ändert ihre Verfügbarkeit.

Halte auch fest, was eine Ablehnung bewirkt. Bleibt die Kamera im passenden Zustand? Erhält das Mitglied eine verständliche Rückmeldung? Dadurch wird die Fachregel zu überprüfbarem Verhalten.

Osmani betont, dass generierte Tests falsche Erwartungen enthalten können. Sie sollen gegen das beabsichtigte Verhalten geprüft werden. Das aktuelle Programm ist dafür kein ausreichender Maßstab. (PDF-S. 168, 219–220.){q:1}

## Verfolge den Fall durch den tatsächlichen Ablauf

Beginne bei der bestätigten Erwartung und gehe dann durch die Umsetzung. Welcher Zustand wird gespeichert? Was meldet die Schnittstelle? Welche Aktion bietet die Oberfläche an? Was passiert beim nächsten Aufruf?

Im Kamerabeispiel sollte die Kontrolle auch nach einem Neuladen noch ausstehen. Eine ausgeblendete Schaltfläche allein würde nicht zeigen, ob die Anwendungslogik die Regel ebenfalls berücksichtigt.

Osmani zeigt an unterschiedlichen Datumsformaten, dass Komponenten ihre eigenen Tests bestehen können und beim Datenaustausch trotzdem verschiedene Bedeutungen verwenden. Deshalb ist eine Prüfung des tatsächlichen Datenflusses wichtig. (PDF-S. 170–171.){q:1}

Für deinen Review folgt daraus: Wähle wenige Fälle, die unterschiedliche Interpretationen sichtbar machen. Zehn gewöhnliche Rückgaben liefern weniger Aufschluss über den fehlenden Kontrollschritt als eine einzige Rückgabe, die anschließend ausdrücklich noch nicht freigegeben wird.

## Gib einem zweiten Reviewer einen eigenen Maßstab

Ein weiterer Mensch oder ein anderes Modell kann zusätzliche Fragen finden. Wenn beide aber nur den fertigen Code sehen, können sie seine Ausgangsannahme übernehmen.

Osmani beschreibt zusätzliche KI-Reviewer und mehrere spezialisierte Modelle als mögliche Ergänzung. Er behandelt KI-Prüfungen zugleich als Hinweise, die weitere Prüfung brauchen. Unterschiedliche Modelle garantieren keine voneinander unabhängigen Fehler. (PDF-S. 164, 209–211.){q:1}

Mein Vorschlag: Gib dem zweiten Reviewer die bestätigte Fachregel, die entscheidenden Fälle und den ursprünglichen Auftrag. Bitte ihn, die Umsetzung daran zu prüfen und offene Bedeutungen ausdrücklich zu benennen.

Für das Kamerabeispiel lautet die zentrale Frage dann: „Kann ein ungeprüft zurückgegebenes Gerät irgendwo wieder als ausleihbar erscheinen?“ Diese Frage richtet die Aufmerksamkeit auf den Clubablauf und seine Grenzen.

## Beginne beim nächsten Review mit einer Fachfrage

Wähle bei deiner nächsten Agentenänderung eine Entscheidung aus, deren falsche Interpretation Folgen hätte. Kläre zuerst ihre Bedeutung. Formuliere dann einen Fall, der die richtige von einer naheliegenden falschen Umsetzung unterscheidet.

Prüfe diesen Fall im gemeinsamen Ablauf und kontrolliere die Erwartung der zugehörigen Tests. Der Beitrag [Grüne Tests, aber der Bug bleibt](post:gruene-tests-bug-bleibt) hilft dir, einen Test am ursprünglichen Fehler auszurichten.

Wenn dabei eine offene Fachentscheidung sichtbar wird, kläre sie vor weiteren großflächigen Änderungen. Du begrenzt damit die Reichweite des Irrtums und gibst dem Agenten einen präziseren nächsten Auftrag.
