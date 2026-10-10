---
titel: "Plan Mode oder direkt loslegen? So viel Planung braucht deine Änderung"
datum: 2026-10-09
kategorie: arbeitsweisen
zusammenfassung: "Entscheide anhand von Umfang, offenen Fragen und Änderungsrisiko, wann Plan Mode hilft. Mit Entscheidungsbaum, Änderungsbeispielen und einem Ablauf für prüfbare Pläne."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-10-08-mattpocockuk-2108216899439894574
  - 2026-02-10-boris-tane-plan-annotation-workflow
  - 2026-07-03-trq212-2073100352921215386
---

## Kurz gesagt

- Setze kleine, eindeutige Änderungen direkt um, wenn du den Diff schnell prüfen und einen Fehlversuch leicht zurücknehmen kannst.
- Kläre zuerst die wichtigste offene Entscheidung, sobald Umfang oder gewünschtes Verhalten unklar sind.
- Schreibe einen prüfbaren Plan, wenn mehrere Bereiche zusammenwirken oder Fehler erhebliche Folgen hätten.
- Wechsle während der Arbeit zurück zur Planung, wenn neue Abhängigkeiten den vereinbarten Umfang verändern.

## Entscheide vor dem ersten Auftrag

Du willst einen Button umbenennen, einen Export ergänzen oder einen ganzen Ablauf umbauen. Alle Aufgaben an einen Coding-Agent können mit einem kurzen Prompt beginnen. Wie viel Vorarbeit sie brauchen, hängt davon ab, was bei einer falschen Annahme passieren würde.

Matt Pocock empfiehlt in seinem Beitrag vom 8. Oktober 2026 für winzige, schnell prüfbare Änderungen einen direkten Versuch. Bei größerem oder unbekanntem Umfang sollen gezielte Rückfragen das Vorhaben klären. Umfangreiche Planung folgt bei ihm erst, wenn dabei tatsächlich mehr Komplexität auftaucht. Das ist eine Heuristik aus seiner Arbeitsweise, keine Produktivitätsmessung.{q:1}

Mein Vorschlag ergänzt diese Entscheidung um das Änderungsrisiko. Ein kleiner Diff, also die Ansicht der geänderten Codezeilen, kann eine zentrale Berechnung beeinflussen. Die Zahl betroffener Dateien allein reicht deshalb als Maßstab kaum aus.

Nutze vor dem Start diesen Entscheidungsbaum:

1. **Kannst du gewünschtes Verhalten und Prüfung konkret benennen?** Wenn nein, beginne mit einer gezielten Klärungsfrage oder einer lesenden Untersuchung der vorhandenen Umsetzung.
2. **Ist die Änderung lokal begrenzt und leicht rückgängig zu machen?** Wenn ja und die Folgen überschaubar sind, kannst du direkt einen kleinen Umsetzungsversuch starten.
3. **Berührt sie mehrere Schnittstellen oder folgenreiche Entscheidungen?** Wenn ja, halte den Ablauf, die betroffenen Bereiche und die Prüfung schriftlich fest.
4. **Bleibt die Umsetzung trotzdem unklar?** Verkleinere den ersten Schritt. Ein Prototyp oder eine Untersuchung kann die fehlende Information liefern.

## Drei Beispiele für unterschiedlich viel Planung

Die folgenden Beispiele sind Vorschläge zur Einordnung deiner eigenen Aufgaben. Sie beschreiben keine gemessenen Ergebnisse.

| Änderung | Offene Entscheidung | Passender Einstieg |
|---|---|---|
| Buttontext in einer vorhandenen Ansicht ändern | Keine, Text und Stelle stehen fest | Direkt umsetzen, Ansicht und Diff prüfen |
| CSV-Export um eine Spalte ergänzen | Welcher Wert, welche Reihenfolge, wie mit fehlenden Daten umgehen? | Diese Fragen klären, dann einen kurzen Plan schreiben |
| Einen bisherigen Einzelablauf auf mehrere Organisationen erweitern | Datenzuordnung, Zugriffsgrenzen, Migration, bestehende Nutzerflüsse | Erst untersuchen, Entscheidungen festhalten und Plan separat prüfen |

Beim Button wäre ein langes Interview unverhältnismäßig. Beim Export verhindert schon die Frage nach fehlenden Werten eine fachlich falsche Ausgabe. Beim organisationsübergreifenden Umbau kann die gewünschte Ansicht einfach aussehen, während die darunterliegenden Entscheidungen viele Bereiche betreffen.

Grilling bezeichnet das gezielte Befragen zu Lücken in der Anforderung. Du brauchst dafür keinen vollständigen Fragenkatalog für jede Kleinigkeit. Thariq beschreibt am 3. Juli 2026 Interviews mit jeweils einer Frage, priorisiert nach ihrem Einfluss auf die Architektur. Er empfiehlt außerdem Prototypen für Anforderungen, die du erst beim Sehen präzise beurteilen kannst.{q:3}

## Ein kurzer Plan für den Export

Mit Plan Mode ist hier die Arbeitsphase gemeint, in der du den Ansatz vor der Umsetzung prüfst. Ob du dafür den Planungsmodus deines Tools oder eine Markdown-Datei verwendest, entscheidest du nach der Aufgabe. Wichtig sind nachvollziehbare Entscheidungen und eine klare Übergabe an die Umsetzung.

Für den beispielhaften CSV-Export könntest du so beginnen:

> Untersuche den vorhandenen Export zunächst lesend. Zeige, wo die Spalten festgelegt werden und wie fehlende Werte behandelt werden. Kläre mit mir die offene Entscheidung mit der größten Auswirkung. Erstelle anschließend einen kurzen Plan mit betroffenen Dateien und Prüfschritten. Beginne die Umsetzung erst nach der Prüfung des Plans.

Nach der Klärung könnte dein Plan diese Punkte enthalten:

- Ziel: Eine zusätzliche Spalte „Kostenstelle“ erscheint an der vereinbarten Position.
- Verhalten: Fehlende Kostenstellen bleiben leer; vorhandene Werte werden unverändert ausgegeben.
- Umfang: Exportzuordnung und passende Prüfung anpassen; die Tabellenansicht bleibt außerhalb des Auftrags.
- Umsetzung: Bestehende Formatierung und Datenquelle verwenden, doppelte Zuordnungslogik vermeiden.
- Prüfung: Beispiel mit vorhandener und fehlender Kostenstelle exportieren; Spaltenreihenfolge und bisherige Inhalte vergleichen.

Das ist bereits genug Material, um einen falschen Ansatz zu erkennen. Falls der Agent dafür plötzlich das Datenmodell umbauen will, frag nach der konkreten Notwendigkeit. Der neue Befund kann eine zusätzliche Untersuchung rechtfertigen; er muss den Auftrag jedoch sichtbar verändern.

## Prüfe den Plan an den entscheidenden Stellen

Boris Tane beschreibt in seinem Workflow vom 10. Februar 2026 separate Dateien für Recherche und Planung. Er ergänzt Korrekturen direkt am Plan und lässt ihn vor der Umsetzung überarbeiten. Diese editierbare Zwischenstufe ist besonders nützlich, wenn du Fachwissen einbringen musst, das im Repository fehlt. Seine Wirkungseinschätzungen stammen aus persönlicher Erfahrung.{q:2}

Mein Vorschlag für dein Review: Suche zuerst nach Entscheidungen, deren spätere Korrektur weitere Änderungen auslösen würde. Beim Export ist das die Herkunft der Kostenstelle. Bei einem größeren Feature können es Datenmodell, Schnittstellen oder Nutzerablauf sein. Prüfe danach die mechanischen Schritte.

Ein separater Reviewer kann anschließend Anforderungen, Randfälle und fehlende Prüfungen betrachten. Formuliere dafür einen engen Auftrag: „Welche konkrete Anforderung fehlt, welche Annahme ist falsch, und wie lässt sich das prüfen?“ Anregungen dafür findest du in den [Prompts für Review und Abnahme](post:prompts-fuer-review-und-abnahme).

## Woran du zu viel oder zu wenig Planung erkennst

Planung kostet Aufmerksamkeit und zusätzliche Modellaufrufe. Ein Dokument wird aufwendig, wenn jede kleine Entscheidung darin gepflegt werden muss. Frage bei jedem Abschnitt: Ändert diese Information den Ansatz, den Umfang oder die spätere Prüfung? Wenn du das nicht erklären kannst, kürze ihn.

Zu wenig Planung erkennst du an wiederholten Annahmenkorrekturen: Der Agent versteht eine Fachregel anders, erweitert laufend den Auftrag oder baut dieselbe Schnittstelle mehrfach um. Stoppe dann die Umsetzung, sammle die neu entdeckten Fragen und prüfe den Ansatz erneut. Ein ausführlicher Plan kann diese Probleme ebenfalls enthalten. Prüfe deshalb die entscheidenden Annahmen auch bei umfangreichen Dokumenten.

Wähle für deine nächste Änderung einen Einstieg und begründe ihn in einem Satz: „Ich setze direkt um, weil …“ oder „Ich kläre zuerst …, weil davon … abhängt.“ Halte danach fest, welche Annahme tatsächlich Nacharbeit ausgelöst hat. So passt du den Planungsaufwand schrittweise an deine eigenen Aufgaben an.
