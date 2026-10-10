---
titel: "Vom Auftrag bis zum Betrieb: ein kompletter Ablauf mit Coding Agents"
datum: 2026-10-09
kategorie: arbeitsweisen
zusammenfassung: "Ein konkreter Coding-Agent-Workflow führt ein kleines Feature vom klaren Auftrag über Tests und Freigaben bis zur Live-Prüfung und zum Betriebsfeedback."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-07-21-claude-how-anthropic-secures-its-ai-native-software-dev
  - 2026-09-27-anthropic-academy-sdlc-playbook
---

## Kurz gesagt

- Beschreibe vor dem Coding das gewünschte Verhalten und seine Abnahmekriterien.
- Lass jede Phase ein nachvollziehbares Ergebnis für den nächsten Schritt hinterlassen.
- Lege Review und Produktionsfreigabe vor der Umsetzung fest; prüfe das Feature nach dem Deployment live.
- Führe beobachtete Fehler in einen neuen Auftrag und einen passenden Test zurück.

## Wähle einen Ablauf, den du vollständig abschließen kannst

Du möchtest einer vorhandenen Aufgabenliste einen Filter für offene und erledigte Aufgaben hinzufügen. Dieses erfundene Feature dient hier als Beispiel für einen vollständigen Coding-Agent-Workflow. Der Umfang ist klein genug, um Auftrag, Umsetzung und Betrieb gemeinsam zu betrachten.

Für einen ersten Durchlauf empfiehlt sich eine Aufgabe mit klaren Grenzen, sichtbarem Ergebnis und vorhandener Testumgebung. Überlege vorab, wer fachliche Fragen beantwortet, wer den Pull Request freigibt und wer die Veröffentlichung auslöst. Ein Pull Request bündelt die vorgeschlagenen Codeänderungen zur Prüfung.

Anthropics Academy-Playbook beschreibt Übergaben durch versionierte Arbeitsartefakte: vom gewünschten Ergebnis über Spezifikation und Plan bis zu Tests, Review und Betriebsfeedback. Für das kleine Beispiel kannst du diese Struktur auf kurze Dateien und einen überschaubaren Pull Request reduzieren. {q:2}

## Schreibe den Auftrag so, dass jemand ihn abnehmen kann

In einer vorgeschlagenen `intent.md` hältst du fest: Nutzer sollen in einer langen Aufgabenliste gezielt offene oder erledigte Einträge sehen. Der Auftrag umfasst den Filter und seine Darstellung innerhalb der bestehenden Liste. Offene Fragen stehen direkt daneben, etwa ob die Auswahl nach einem Neuladen erhalten bleibt.

Diese Frage klärst du vor dem Coding. Für unser Beispiel gilt: Die Auswahl wird beim Neuladen zurückgesetzt. Anschließend beschreibt eine kurze `spec.md` das vereinbarte Verhalten:

| Situation | Erwartetes Verhalten im Beispiel |
|---|---|
| Liste erstmals öffnen | Alle Aufgaben anzeigen |
| „Offen“ auswählen | Aufgaben ohne Erledigt-Markierung anzeigen |
| „Erledigt“ auswählen | Erledigte Aufgaben anzeigen |
| Filter liefert keine Treffer | Verständlichen Hinweis mit Möglichkeit zum Zurücksetzen zeigen |
| Aufgabe bei aktivem Filter erledigen | Sichtbare Liste sofort passend aktualisieren |

Lass die fachlich zuständige Person diese Kriterien prüfen. Eine spätere Übergabe kann nun auf konkrete Situationen verweisen. Vermeide zusätzliche Wünsche während der Umsetzung: Wenn auch Suche oder gespeicherte Ansichten gewünscht sind, bekommen sie einen eigenen Auftrag.

## Lass den Plan zuerst die vorhandenen Bausteine finden

Der Agent untersucht nun gezielt die Listenkomponente, ihren Datenfluss und vorhandene Tests. Die vorgeschlagene `plan.md` nennt die betroffenen Stellen, den geplanten Filterzustand und die erforderlichen Prüfungen. Der Filter verwendet dabei die vorhandenen Aufgaben und deren Erledigt-Markierung.

Prüfe den Plan auf unnötige Erweiterungen. Für das Beispiel sollte er erklären, wie die gefilterte Ansicht aus den bestehenden Daten entsteht und wie sich eine Statusänderung auf die Anzeige auswirkt. Ein neuer Service oder ein zusätzliches Datenmodell bräuchte eine nachvollziehbare Begründung.

Hier liegt der technische Freigabepunkt: Stimmen Vorgehen, Umfang und Prüfungen, beginnt die Umsetzung. Entdeckt der Agent eine fehlende Statusdefinition oder widersprüchliche Daten, muss diese Entscheidung zurück zur Spezifikation.

## Begrenze die Umsetzung auf einen prüfbaren Change

Der Coding Agent implementiert den vereinbarten Filter und ergänzt Tests für dessen Verhalten. Sinnvolle Prüfungen im Beispiel betreffen die Auswahl, eine leere Ergebnismenge und das Erledigen einer Aufgabe bei aktivem Filter. Sie beschreiben Nutzerverhalten und wichtige Randfälle.

Zusätzlich lässt du vorhandene relevante Checks laufen. CI, die automatische Prüfung von Änderungen, führt anschließend die für das Repository vorgeschriebenen Prüfungen aus. Der Abschlussbericht des Agents nennt deren Ergebnisse und verbleibende Unsicherheiten.

Für die Übergabe gehören Diff, Testergebnisse und ein kurzer sichtbarer Nachweis zusammen. Der Diff zeigt die einzelnen Codeänderungen. Bei diesem UI-Feature helfen ein Screenshot und eine Beschreibung des geprüften Ablaufs. Ein erfolgreiches Testergebnis sagt jeweils etwas über die ausgeführte Prüfung; die Abnahmekriterien bleiben der Bezugspunkt.

## Lege das Review nach dem Risiko fest

Ein Reviewer prüft, ob die Änderung die vereinbarte Funktion erfüllt, bestehende Bedienung stört oder ungewöhnliche Eingaben falsch behandelt. Für unseren ersten Durchlauf bleibt die menschliche PR-Freigabe ein fester Schritt. Der schreibende Agent liefert die Vorbereitung dafür.

Anthropic beschreibt eine weitergehende Herstellerpraxis: Codebereiche werden nach Risiko eingestuft, neue AI-Reviewer starten im Shadow Mode und ihre Ergebnisse werden zunächst von Menschen geprüft. Ausgewählte automatische Freigaben werden protokolliert und durch risikogewichtete menschliche Stichproben kontrolliert. Kritische Bereiche behalten menschliche Freigaben. Der Bericht nennt keine allgemein anwendbare Freigabeschwelle. {q:1}

Shadow Mode bedeutet hier, dass der Reviewer mitläuft und Vorschläge liefert, während die bestehende Freigabe entscheidet. Eine solche Phase kann dir helfen, Fehlalarme und übersehene Fehler an eigenen Änderungen zu sammeln. Mehr Autonomie wäre erst nach dieser Auswertung eine gesonderte Entscheidung für einen klar abgegrenzten Bereich.

Für Änderungen an Datenzugriff, Anmeldung oder anderen kritischen Funktionen planst du zusätzliche fachkundige Prüfung ein. Die Frage nach der passenden Reviewer-Rolle vertieft [Adversarial Agent oder Review](post:duell-adversarial-agent-oder-review).

## Prüfe Build, Deployment und Live-Verhalten getrennt

Nach dem Review erzeugt der Build das auslieferbare Ergebnis. Anschließend bringt das Deployment genau diesen Stand in die Zielumgebung. Die Produktionsfreigabe liegt im vorgeschlagenen Ablauf bei der zuständigen Person; der Agent bereitet Releasebeschreibung, Prüfschritte und Rücknahmeweg vor.

Prüfe danach, welche Revision, also welcher Code-Stand, tatsächlich läuft. Öffne die veröffentlichte Aufgabenliste und gehe die vereinbarten Situationen durch: Filter wechseln, Aufgabe erledigen, leere Auswahl zurücksetzen. Prüfe auch die Bedienung auf einer schmalen Ansicht. Halte Ergebnis und beobachtete Fehler beim Release fest.

Der Rücknahmeweg muss zur Änderung passen. Für unser Beispiel kann das die erneute Auslieferung des zuvor funktionierenden Stands sein. Kläre vorab, wer sie auslösen darf und welche Beobachtung sie erforderlich macht.

## Schließe den Ablauf mit Betriebsfeedback

Eine mögliche spätere Meldung lautet: Nach dem Erledigen bleibt eine Aufgabe im Filter „Offen“ sichtbar. Das ist ein erfundenes Fehlerbeispiel. Du dokumentierst den auslösenden Ablauf, reproduzierst ihn und ergänzt eine Prüfung, die den Fehler erkennt. Daraus entsteht der nächste begrenzte Auftrag.

Anthropic beschreibt Agents, die Produktionsmeldungen untersuchen und Fixes vorbereiten. Der im Bericht vorgestellte Incident-Agent kann den Fix selbst nicht deployen. Auch der Zugang zu anderen Agents gehört dabei zur betrachteten Berechtigungsgrenze. {q:1}

Plane für diesen Ablauf Zeit für Spezifikation, Checks, Review, Live-Prüfung und Pflege ein. Zusätzliche Agent-Läufe verbrauchen Rechenzeit und können weitere Befunde erzeugen, die jemand beurteilen muss. Starte deshalb mit einem kleinen Feature und dokumentiere die offenen Übergaben. Der nächste sinnvolle Schritt ist eine kurze Auftragsskizze mit Abnahmekriterien, benannter Freigabe und vorbereitetem Live-Prüfablauf.
