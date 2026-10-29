---
titel: "Parallele Agents brauchen freie Reviewkapazität"
datum: 2026-10-29
kategorie: arbeitsweisen
zusammenfassung: "Mehr parallele Agents erzeugen auch mehr Ergebnisse zum Prüfen. Plane Review und Integration mit ein und entscheide offene Restarbeit nach ihrem zukünftigen Nutzen."
status: freigegeben
geprueft_am: 2026-10-29
freigabe: automatisch
quellen:
  - 2025-08-18-pdf-beyond-vibe-coding
---

## Kurz gesagt

- Starte weitere Agents erst, wenn jemand ihre Ergebnisse zeitnah prüfen und zusammenführen kann.
- Vereinbare getrennte Aufgabenbereiche und eine sinnvolle Reihenfolge für die Zusammenführung.
- Bewerte fast fertige Änderungen nach verbleibendem Nutzen und künftigem Aufwand.

## Wenn die Ergebnisse schneller eintreffen als dein Review

Mehrere Coding Agents können gleichzeitig Aufgaben bearbeiten. Das sind KI-gestützte Programme, die Dateien ändern und Entwicklungswerkzeuge aufrufen können. Danach warten ihre Änderungen auf das Review, die Prüfung der Änderungsvorschläge: Passt das Verhalten? Welche Prüfungen liefen wirklich? Wie wirken die Beiträge zusammen?

Addy Osmani beschreibt diese verstärkte Reviewlast in [Beyond Vibe Coding: From Coder to AI-Era Developer](https://www.oreilly.com/library/view/beyond-vibe-coding/9798341634749/). Große, gleichzeitig eintreffende Änderungsvorschläge können die prüfende Person stark beanspruchen. Hinzu kommen mögliche Konflikte und Unterschiede zwischen den Arbeitsumgebungen. (PDF-S. 214–215.){q:1}

Das Buch von 2025 enthält dafür keine allgemeine Skalierungskurve. Es zeigt einen nachvollziehbaren Engpass: Eine erzeugte Änderung braucht noch die passende Prüfung und einen Platz im gemeinsamen Projektstand. Dafür musst du Zeit und Aufmerksamkeit einplanen.

## Plane die gesamte Strecke bis zur Fertigstellung

Mein Vorschlag ist, Parallelität entlang des vollständigen Arbeitsablaufs zu betrachten. Dazu gehören Aufgabenbeschreibung, Agentenlauf, Review, Nacharbeit und Integration. Integration bedeutet hier das Zusammenführen der Änderungen und die Prüfung ihres gemeinsamen Verhaltens.

Ein schneller Agentenlauf verkürzt nur einen Teil dieser Strecke. Wenn Ergebnisse länger warten, müssen Reviewer später ihren Zusammenhang wiederherstellen. Hat sich die gemeinsame Grundlage inzwischen geändert, kann zusätzliche Anpassung nötig werden.

Frage deshalb vor einem weiteren Start: Wer prüft das Ergebnis? Wann ist dafür Raum? Welche andere Änderung muss vorher vorliegen? Diese einfachen Fragen machen den zu erwartenden Aufwand sichtbar.

Für einen kleinen Einstieg kannst du zunächst zwei voneinander trennbare Aufgaben wählen und ihre vollständige Fertigstellung beobachten. Das ist mein praktischer Vorschlag, keine im Buch gemessene optimale Agentenzahl.

## Ein Export und eine Formularänderung als hypothetisches Beispiel

Stell dir ein erfundenes Team vor, das eine Kontaktverwaltung pflegt. Ein Agent ergänzt eine vorhandene Spalte im Export. Ein zweiter verbessert die Anzeige bestehender Formularfehler. Eine Person übernimmt das Review.

Die Aufgaben wirken zunächst gut getrennt. Während der Arbeit entscheidet der Formular-Agent jedoch, das gemeinsame Fehlerformat zu verändern. Der Export-Agent verwendet dieses Format weiterhin wie zuvor.

Jetzt braucht das Team eine zusätzliche Schnittstellenentscheidung. Würde gleichzeitig ein dritter Agent auf dem alten Format aufbauen, wüchse die Nacharbeit weiter.

Im Beispiel wäre es sinnvoll, die Änderung am gemeinsamen Vertrag zuerst zu klären. Anschließend kann das Team entscheiden, welche Beiträge auf welcher Grundlage fertiggestellt werden. Mehr laufende Aufgaben würden die offene Entscheidung nur auf weitere Stellen verteilen.

## Gib jedem Auftrag eine klare Integrationsfolge

Osmani empfiehlt abgegrenzte Arbeitsbereiche und eine bewusste Reihenfolge beim Zusammenführen. Ein Agent, der neue Funktionen ergänzt, kann von der Infrastrukturänderung eines anderen abhängen. Solche Abhängigkeiten gehören in die Planung. (PDF-S. 216–217.){q:1}

Mein Vorschlag für das Beispiel: Das bestehende Fehlerformat bleibt zunächst verbindlich. Der Formular-Agent verbessert ausschließlich seine Darstellung. Falls eine Vertragsänderung erforderlich wird, meldet er sie vor der Umsetzung. Das Team bestimmt dann einen eigenen gemeinsamen Schritt.

Für jeden Beitrag brauchst du außerdem einen verständlichen Abschluss: Was wurde verändert? Welche Fälle wurden geprüft? Welche Prüfung konnte nicht ausgeführt werden? Was ist noch offen?

Die technische Trennung der Arbeitsverzeichnisse behandelt [Parallele Coding-Agents mit Git Worktrees](post:parallele-agents-worktrees-integration). Ergänze diese Trennung um Zuständigkeit und Zusammenführungsreihenfolge, damit der gemeinsame Projektstand überprüfbar bleibt.

## Begrenze die Warteschlange anhand deiner tatsächlichen Arbeit

Eine Warteschlange entsteht, wenn Ergebnisse auf ihre nächste Bearbeitung warten. Bei Agenten kann das der Review, eine Fachentscheidung oder die Integration sein.

Mein Vorschlag ist eine einfache Übersicht mit drei Zuständen: in Bearbeitung, zur Prüfung bereit und abgeschlossen. Schau besonders auf die mittlere Gruppe. Wenn dort Aufgaben liegen bleiben, untersuche zuerst den Grund, bevor du zusätzliche Starts einplanst.

Vielleicht ist der Auftrag zu groß. Vielleicht fehlt eine Testumgebung. Vielleicht muss jemand eine Fachfrage beantworten. Jeder dieser Gründe verlangt eine andere Reaktion.

Osmani verbindet sinnvolle Agentenarbeit mit klaren Erfolgskriterien, passender Umgebung und frühen Eingriffsmöglichkeiten. Er beschreibt auch Fälle, in denen eine unpassende Umgebung die Testprüfung behindert. (PDF-S. 203–204, 216–218.){q:1} Eine zusätzliche Agenteninstanz löst einen solchen gemeinsamen Engpass nicht automatisch.

## Entscheide Restarbeit nach dem zukünftigen Nutzen

Ein Agent liefert einen umfangreichen Vorschlag. Vieles sieht brauchbar aus, einige wichtige Fälle fehlen. Gerade bei einer ursprünglich kleinen Aufgabe kann das Team nun viel Zeit aufwenden, weil bereits so viel entstanden ist.

Osmani nennt dies ein Sunk-Cost-Dilemma: Bereits investierter Aufwand beeinflusst die Entscheidung, einen fast brauchbaren Vorschlag weiterzuverfolgen. Ob sich die Restarbeit lohnt, hängt vom Wert der Änderung und ihrem Zusammenhang ab. (PDF-S. 205.){q:1}

Meine daraus abgeleitete Frage lautet: Würdest du den jetzt sichtbaren Restauftrag heute für seinen erwarteten Nutzen einplanen? Berücksichtige Korrektur, erneute Prüfung, Integration und spätere Pflege.

Du kannst den Vorschlag fertigstellen, verkleinern oder vorerst zurückstellen. Halte die hilfreichen Erkenntnisse und den Grund der Entscheidung fest. So bleibt die Erfahrung nutzbar, auch wenn die Änderung gerade keine Priorität erhält.

## Starte mit einem kleinen, vollständig verfolgten Durchlauf

Wähle zwei überschaubare Aufgaben, bestätige ihre Grenzen und reserviere einen konkreten Reviewtermin. Führe die Ergebnisse nacheinander zusammen und prüfe den gemeinsamen Ablauf.

Erfasse dabei wenige Größen: Zeit bis zur bestätigten Fertigstellung, Wartezeit vor dem Review, notwendige Nacharbeit und zusätzlichen Integrationsaufwand. Diese Größen sind ein Vorschlag für deine eigene Beobachtung. Aus dem Buch lässt sich kein bestimmter Zeit- oder Kostenvorteil für dein Projekt ableiten.

Entscheide danach, ob ein weiterer paralleler Auftrag sinnvoll wäre. Wenn die Ergebnisse bereits zügig geprüft werden und ihre Grenzen tragen, kannst du den Umfang vorsichtig erweitern. Wenn sich Arbeit staut, verbessere zuerst den erkennbaren Engpass.
