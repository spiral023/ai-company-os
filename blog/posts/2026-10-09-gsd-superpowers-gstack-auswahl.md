---
titel: "GSD, Superpowers oder gstack: Welches Problem soll dein Framework lösen?"
datum: 2026-10-09
kategorie: tools
zusammenfassung: "Vergleiche GSD Core, Superpowers und gstack anhand ihrer dokumentierten Abläufe. Mit einer Auswahlmatrix und einem kleinen Pilotauftrag für deinen tatsächlichen Engpass."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-10-09-repo-gsd-workflow
  - 2026-10-09-repo-superpowers-workflow
  - 2026-10-09-repo-gstack-workflow
---

## Kurz gesagt

- Benenne zuerst den Engpass: unklare Anforderungen, verlorener Arbeitsstand, schwache Tests oder fehlende Browserprüfung.
- Vergleiche die dokumentierten Arbeitsschritte und Ergebnisse, die zu diesem Engpass passen.
- Prüfe einen begrenzten Auftrag, bevor du den gesamten Entwicklungsablauf umstellst.
- Rechne Einrichtung, zusätzliche Dateien, Rechte und spätere Updates in deine Entscheidung ein.

## Wähle nach einer beobachteten Schwierigkeit

Du hast einen Coding-Agent, kannst Änderungen erstellen lassen und prüfst sie vor der Veröffentlichung. Trotzdem geht etwas regelmäßig schief: Der Agent beginnt zu früh mit Code, eine längere Aufgabe verliert ihren Stand oder eine fertige Oberfläche funktioniert im Browser schlecht. Für diese Probleme gibt es unterschiedliche Ansätze.

GSD Core, Superpowers und gstack beschreiben umfangreichere Abläufe mit eigenen Rollen, Dateien und Prüfschritten. Der folgende Vergleich beruht auf ihren bei konkreten Commits gesichteten READMEs. Der Stand wurde am 9. Oktober 2026 geprüft. Ich habe die Frameworks für diesen Artikel weder installiert noch gegeneinander ausgeführt; Aussagen über Geschwindigkeit oder gemessene Qualität lassen sich daraus nicht ableiten.{q:1}{q:2}{q:3}

Meine Empfehlung ist deshalb eine Auswahl nach deinem Engpass. Schreibe ihn möglichst konkret auf: „Bei Aufgaben über mehrere Arbeitssitzungen fehlt mir die nächste Aktion“ lässt sich leichter prüfen als „Meine Agents sollen autonomer werden“.

## Was die Projekte dokumentieren

GSD Core strukturiert die Arbeit in Discuss, Plan, Execute, Verify und Ship. Entscheidungen entstehen vor der Umsetzung, Recherche und Ausführung nutzen frische Subagent-Kontexte. Dateien wie `STATE.md` und `CONTEXT.md` halten Stand und Entscheidungen über Phasen hinweg fest. Das passt als Ansatz zu längeren Aufgaben mit wiederholten Übergaben.{q:1}

Superpowers beschreibt Brainstorming, Designfreigabe, Worktrees, kleine Implementierungspläne und anschließende Umsetzung. Ein eigener TDD-Skill fordert RED–GREEN–REFACTOR: erst ein sinnvoll fehlschlagender Test, dann die Umsetzung, anschließend das Überarbeiten. Reviews beziehen sich auf den Plan; der Branch-Abschluss behandelt die Integration. Das Projekt setzt damit einen stark strukturierten Entwicklungsablauf voraus.{q:2}

gstack ordnet die Arbeit nach Think, Plan, Build, Review, Test, Ship und Reflect. Commands wie `/office-hours`, `/plan-eng-review`, `/review` und `/qa` übernehmen unterschiedliche Rollen. `/qa-only` beschreibt Browserprüfung und Berichte ohne Produktänderungen. `/qa` umfasst zusätzlich Reproduktion, Regressionstests und Reparatur. Welche dieser Schritte tatsächlich ausführbar sind, hängt auch von deiner Projektumgebung ab.{q:3}

Die beschriebenen Abläufe überlappen. Allein der Name einer Phase beantwortet jedoch nicht, ob du nach ihr eine verwertbare Entscheidung oder ein reproduzierbares Prüfergebnis bekommst. Genau diese Übergaben gehören in deinen Versuch.

## Eine Matrix für die Vorauswahl

Die Tabelle ist meine Einordnung der dokumentierten Methoden. Sie zeigt mögliche Einstiege, keine Rangliste oder gemessenen Gewinner.{q:1}{q:2}{q:3}

| Dein Engpass | Ansatz für einen ersten Versuch | Was du konkret beurteilst |
|---|---|---|
| Mehrere Sitzungen verlieren Stand und Entscheidungen | GSD Core: persistente Phasenartefakte | Findet der nächste Bearbeiter den aktuellen Stand und nächsten Schritt? |
| Implementierung startet vor geklärtem Design | Superpowers: Brainstorming und Designfreigabe | Werden wichtige offene Entscheidungen vor dem Code sichtbar? |
| Änderungen kommen mit wenig aussagekräftigen Tests | Superpowers: TDD und planbezogenes Review | Prüfen die Tests die geforderte Wirkung und erkennen sie einen Fehler? |
| Die Oberfläche wurde nach dem Build kaum benutzt | gstack: Browserprüfung mit `/qa-only` | Ist der Fehler reproduzierbar und der Bericht für eine Reparatur brauchbar? |
| Nur eine kleine Übergabe ist regelmäßig schlecht | Eigene kurze lokale Anweisung | Reicht eine klare Vorlage für Auftrag, Ergebnis und Prüfung? |

Wenn dein Entwicklungsablauf bereits Designfreigaben und TDD enthält, kann ein weiterer Pflichtablauf doppelte Arbeit erzeugen. Wenn die Browserprüfung fehlt, bringt dir ein zusätzlicher Plan allein keinen Befund zur Oberfläche. Beurteile daher auch, welche Schritte du bereits zuverlässig erledigst.

## Verwende einen begrenzten Pilotauftrag

Als synthetisches Beispiel dient eine Listenansicht mit einem Suchfeld. Der Auftrag lautet: Eine leere Trefferliste soll einen verständlichen Hinweis anzeigen; ein bestehender Eintrag muss weiterhin auswählbar sein. Betroffen sind eine Ansicht, ihre Datenabfrage und die Prüfung des Auswahlverhaltens.

Vor dem Versuch legst du gewünschtes Verhalten, verfügbare Testdaten und den Rückweg fest. Wähle anschließend den Teil des Ansatzes, der deinen Engpass adressiert. Für verlorene Übergaben kannst du den Arbeitsstand dokumentieren und in einer neuen Sitzung daraus weiterarbeiten lassen. Für schwache Tests prüfst du, ob ein absichtlich falsches Auswahlverhalten erkannt wird. Für die Browserprüfung brauchst du eine tatsächlich laufende, erreichbare Testumgebung.

Halte fest, was passiert ist:

- Welche Entscheidung musste ein Mensch nachholen?
- Welche Dateien und Anweisungen kamen zum Projekt hinzu?
- Welche Prüfung lief tatsächlich und welches Verhalten deckte sie ab?
- Welche Nacharbeit war erforderlich, bevor die Änderung brauchbar wurde?
- Welche Einstellungen müsstest du bei einem Update erneut kontrollieren?

Das sind Prüffragen für deinen eigenen Versuch. Der beschriebene Auftrag wurde hier nicht ausgeführt. Weitere Prüfschritte für eine fertige Anwendung findest du im [Artikel zum Pre-Launch-Check](post:pre-launch-app-angreifen).

## Plane die Pflege gleich mit

Ein Skill ist eine wiederverwendbare Arbeitsanweisung für einen Agent. Mehrere Skills können zusätzliche Dateien, Commands und Abhängigkeiten mitbringen. Prüfe, welche Laufzeit und Werkzeuge dein gewählter Ansatz voraussetzt und welche Rechte du tatsächlich erteilen willst. Ein benannter Browser-Schritt hilft erst, wenn der Agent den vorgesehenen Browser erreichen kann.

Halte außerdem den überprüften Versionsstand fest. Ein Update kann Schritte, Rollen oder Referenzen verändern; lokale Anpassungen müssen weiterhin auffindbar bleiben. Für diesen Artikel sind die README-Links in den Quellen an konkrete Commits gebunden. Dein später installierter Stand kann davon abweichen.{q:1}{q:2}{q:3}

Wenn dein Engpass klein bleibt, ist eine eigene Anweisung eine ernsthafte Option. Sie könnte verlangen: Ziel und offene Entscheidungen klären, Änderungen begrenzen, Prüfungen tatsächlich ausführen und den Arbeitsstand kurz übergeben. Du musst dann allerdings selbst festlegen, wann welcher Schritt gilt, und die Anweisung pflegen.

## Triff die Entscheidung am Ergebnis

Nach dem Pilotauftrag kannst du sagen, welches Problem besser bearbeitet wurde und welcher zusätzliche Aufwand entstanden ist. „Der nächste Bearbeiter konnte den Stand finden“ oder „Die Browserprüfung lieferte einen reproduzierbaren Fehler“ sind konkrete Beobachtungen. Eine gelungene Kleinaufgabe erlaubt weiterhin keine allgemeine Aussage über große Umbauten.

Übernimm den Ansatz schrittweise, wenn der beobachtete Nutzen zu deinem Projekt passt. Bleiben die wichtigen Übergaben unklar, präzisiere zuerst Auftrag und Prüfkriterium. Einen Einstieg dafür bietet der [Vergleich zwischen Plan Mode und direkter Umsetzung](post:plan-mode-oder-direkt-loslegen).
