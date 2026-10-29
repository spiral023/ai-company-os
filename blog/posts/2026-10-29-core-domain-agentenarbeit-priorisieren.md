---
titel: "Core Domain: Agentenarbeit auf den Produktkern richten"
datum: 2026-10-29
kategorie: arbeitsweisen
zusammenfassung: "Richte Agentenarbeit auf den besonderen fachlichen Wert deines Produkts. Prüfe früh das Kernrisiko und entwickle generische Unterstützung nur im tatsächlich benötigten Umfang."
status: freigegeben
geprueft_am: 2026-10-29
freigabe: automatisch
quellen:
  - 2003-08-01-pdf-domain-driven-design
---

## Kurz gesagt

- Beschreibe in wenigen Sätzen, welchen besonderen fachlichen Nutzen dein Produkt liefern soll.
- Wähle den ersten ausführbaren Durchstich so, dass er eine schwierige Annahme über diesen Nutzen prüft.
- Begrenze unterstützende Funktionen auf den aktuellen Bedarf und halte ihre Integrationskosten sichtbar.

Ein Agent kann ein neues Dashboard, eine flexible Exportbibliothek oder eine zusätzliche Konfiguration vorbereiten. Alle drei Aufgaben liefern sichtbare Ergebnisse. Ob sie das Produkt voranbringen, hängt davon ab, welche Unsicherheit gerade seinen eigentlichen Nutzen bedroht.

In [Domain-Driven Design](https://www.domainlanguage.com/ddd/) nennt Eric Evans den spezialisierten fachlichen Kern einer Anwendung Core Domain. Dort liegt der besondere Wert, für den sich die eigene Entwicklung lohnt. Er empfiehlt, qualifizierte Fähigkeiten und langfristigen Wissensaufbau gezielt auf diesen Bereich zu richten.{q:1}

## Den besonderen Nutzen konkret benennen

Der Produktkern ergibt sich aus den Zielen der Anwendung. Eine Funktion kann notwendig sein und trotzdem eine unterstützende Rolle haben. Umgekehrt kann ein vergleichsweise kleiner Teil des Codes genau die Entscheidung ermöglichen, für die Menschen das Produkt verwenden. Evans beschreibt diese Priorisierung auf PDF-Seiten 247–251.{q:1}

Stell dir als hypothetisches Beispiel eine Anwendung für Reparaturwerkstätten vor. Ihr versprochener Nutzen ist, aus unvollständigen Schadensbeschreibungen einen brauchbaren Arbeitsvorschlag abzuleiten. Das System soll passende Arbeitsschritte zusammenstellen und offene Fragen sichtbar machen.

Ein übersichtlicher Login und ein tabellarischer Dateiexport können dafür erforderlich sein. Der besondere Nutzen hängt aber zunächst daran, ob die vorgeschlagenen Schritte fachlich brauchbar sind. Wenn diese Entscheidung unverständlich bleibt, kann eine schöne Oberfläche das zentrale Problem nur schwer ausgleichen.

Schreibe deshalb genauer als „Wir automatisieren Werkstattarbeit“. Welchen Vorgang erleichterst du? Welche Entscheidung unterstützt du? Woran würden Fachleute einen unbrauchbaren Vorschlag erkennen?

## Ein früher Durchstich durch das Kernrisiko

Ein ausführbarer Durchstich ist ein kleiner realer Ablauf durch die benötigten Teile der Anwendung. Im Werkstattbeispiel könnte eine eingegebene Schadensbeschreibung zu einem gespeicherten Arbeitsvorschlag führen, den eine Fachperson anhand festgelegter Fragen beurteilt.

Dieser erste Ablauf braucht noch keine große Bibliothek möglicher Werkstätten. Er muss die schwierige Annahme erreichbar machen: Kann das System die fachlich wichtigen Informationen unterscheiden und fehlende Angaben sinnvoll behandeln?

Evans warnt davor, mit einer technisch angenehmen Randfunktion den Eindruck zu erzeugen, das eigentliche Projektrisiko sei bereits bearbeitet. Ein frühes durchgängiges System mindert fachliches Risiko nur, soweit es einen schwierigen Teil des tatsächlichen Kerns enthält.{q:1}

Für Agents ist das meine Ableitung: Formuliere den ersten Auftrag um eine Erkenntnis, die deine weitere Entscheidung verändert. Ein funktionsfähiger Export beantwortet die Frage nach brauchbaren Arbeitsvorschlägen nicht.

## Unterstützung im benötigten Umfang entwickeln

Generic Subdomains sind fachliche Teilbereiche, die das Produkt unterstützen, ohne seinen besonderen Nutzen auszumachen. Das kann beispielsweise eine einfache Kontaktverwaltung sein. Ob ein Bereich generisch ist, hängt vom Produkt ab: Für eine andere Anwendung könnte gerade dort der Kern liegen.{q:1}

Im erfundenen Werkstattsystem braucht ein Arbeitsvorschlag zunächst eine Kontaktzuordnung und eine verständliche Darstellung seiner Schritte. Daraus folgt noch kein Bedarf an einer universellen Organisationsverwaltung oder einer frei konfigurierbaren Dokumentenplattform.

Evans unterscheidet ausdrücklich zwischen generischem Fachwissen und maximal wiederverwendbarem Code. Du kannst eine passende Teilmenge entwickeln, die deinen Bedarf erfüllt. Weitergehende Allgemeinheit kostet Entwurf, Verständnis und Wartung. Ebenso haben vorhandene Lösungen Integrationskosten und müssen beurteilt werden.{q:1}

Ein Agentenauftrag sollte deshalb den unterstützenden Zweck und seine Grenze nennen: „Ordne den Vorschlag einem vorhandenen Kontakt zu“ ist genauer als „Baue eine flexible Kundenplattform“. Du kannst die Aufgabe später erweitern, wenn ein tatsächlicher Fall es verlangt.

## Lernaufwand bewusst zuweisen

Im Kern entsteht wertvolles Wissen darüber, welche Regeln zusammengehören, welche Ausnahmen wichtig sind und welche Begriffe die Fachleute tatsächlich verwenden. Evans empfiehlt, diese Arbeit mit qualifizierten Entwicklern und Domänenexperten zu verbinden. Wenn dieselben Menschen dauerhaft nur Infrastruktur bearbeiten, bleibt dieser Wissensaufbau aus.{q:1}

Die Übertragung auf Agentenarbeit braucht eine eigene Entscheidung. Ein Agent kann vorhandene Abläufe untersuchen, Alternativen formulieren und einen kleinen Versuch implementieren. Die fachliche Gültigkeit eines neuen Reparaturvorschlags muss aus einer dafür zuständigen, unabhängigen Beurteilung kommen.

Bewerte deshalb vor einer Delegation zwei Fragen: Welche Arbeit kann anhand eines bestehenden Vertrags abgenommen werden? Welche Arbeit muss erst die Bedeutung dieses Vertrags klären? Für die zweite Frage brauchst du erreichbare Fachleute und Zeit für Rückmeldung.

Die [gemeinsame Fachsprache innerhalb eines Bounded Context](post:bounded-context-gemeinsame-fachsprache) hilft, diese Bedeutung verständlich zu halten. Bei zusammenhängenden Zustandsregeln ergänzt die [Arbeit mit Aggregaten](post:aggregate-fachliche-invarianten-schuetzen) die nötige Konsistenzgrenze.

## Den Kern sichtbar halten

Ein knappes Domain Vision Statement beschreibt den besonderen fachlichen Wert des Modells. Evans schlägt außerdem vor, seine wesentlichen Konzepte und Interaktionen leicht auffindbar zu machen. Dafür muss nicht zuerst das gesamte System umgebaut werden.{q:1}

Für das Werkstattbeispiel könntest du auf einer Seite festhalten: Welche Eingaben beschreibt das Modell? Was bedeutet ein Arbeitsvorschlag? Welche Unsicherheiten bleiben ausdrücklich sichtbar? Welche Entscheidungen trifft weiterhin eine Fachperson?

Diese Seite führt anschließend zu den relevanten Beispielen und Codestellen. Sie soll den Einstieg erleichtern und bei neuen Erkenntnissen aktualisiert werden. Wenn ein Agent eine Änderung vorschlägt, die den beschriebenen Kern verändert, wird damit eine fachliche Entscheidung sichtbar.

Ein solcher Überblick kann veralten. Er braucht tatsächliche Verwendung im Gespräch und bei der Abnahme. Eine weitere lange Beschreibung ohne erkennbare Aufgabe erhöht den Pflegeaufwand.

## Den nächsten Auftrag am verbleibenden Risiko wählen

Die Aufmerksamkeit für den Kern darf notwendige Unterstützung nicht unsichtbar machen. Eine fehlerhafte Datenhaltung kann den ganzen Ablauf blockieren. Auch die Zuordnung zum Core Domain bleibt veränderbar: Neue Erkenntnisse können zeigen, dass ein bisher nebensächlich behandelter Mechanismus den besonderen Wert trägt. Evans versteht die Verdichtung des Modells als fortlaufende Arbeit.{q:1}

Nimm für deine nächste Planung drei offene Aufgaben. Beschreibe jeweils, welches Produktproblem sie lösen, welche Unsicherheit sie beseitigen und was du anschließend besser entscheiden kannst. Wähle dann einen kleinen ausführbaren Schritt durch die wichtigste noch offene Kernannahme.

Gib dem Agenten das gewünschte Verhalten, die bestätigten Beispiele und den erlaubten Umfang mit. Nach der Prüfung entscheidest du anhand des verbleibenden Risikos, welche Unterstützung als Nächstes nötig ist.
