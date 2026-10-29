---
titel: "Aggregate schützen fachliche Invarianten"
datum: 2026-10-29
kategorie: arbeitsweisen
zusammenfassung: "Ein Aggregate bündelt Änderungen, die eine fachliche Regel gemeinsam schützen müssen. Bestimme Invarianten, kontrolliere Zugriffe über eine Root und prüfe konkurrierende Vorgänge."
status: freigegeben
geprueft_am: 2026-10-29
freigabe: automatisch
quellen:
  - 2003-08-01-pdf-domain-driven-design
---

## Kurz gesagt

- Formuliere zuerst die fachliche Eigenschaft, die nach einer abgeschlossenen Änderung gelten muss.
- Bestimme eine Root, also einen kontrollierten Zugang zu den zusammengehörigen Änderungen, und kläre erlaubte Verweise auf innere Objekte.
- Prüfe normale Ablehnung, konkurrierende Änderungen und beschädigte Zustände als unterschiedliche Fälle.

Zwei Agenten bearbeiten verschiedene Dateien. Einer ergänzt die Buchung eines Platzes, der andere verändert die Kapazität. Beide Änderungen können für sich plausibel aussehen und gemeinsam einen unzulässigen Zustand erzeugen.

Eric Evans beschreibt in [Domain-Driven Design](https://www.domainlanguage.com/ddd/) Aggregate als Einheiten für Datenänderungen mit einer klaren Grenze und einem kontrollierten Zugang. Entscheidend sind die fachlichen Regeln, die innerhalb dieser Grenze zusammen erhalten bleiben müssen. Die zentrale Erläuterung steht auf PDF-Seiten 70–78.{q:1}

## Zuerst die Invariante formulieren

Eine Invariante ist eine Eigenschaft, die an vereinbarten Grenzen einer Änderung gelten muss. Während eines gekapselten Vorgangs können interne Zwischenzustände entstehen. Beim Abschluss muss die zugesagte Konsistenz wieder hergestellt sein.{q:1}

Stell dir als eigenes, hypothetisches Beispiel ein System für kleine Kochkurse vor. Ein Termin besitzt zwölf Plätze. Die fachlich Verantwortlichen legen fest: Die Summe bestätigter Plätze und noch gültiger Vormerkungen darf die verfügbare Kapazität nicht überschreiten.

Schon diese Formulierung verlangt Entscheidungen. Wann läuft eine Vormerkung ab? Zählt ihre Ablaufzeit aus Sicht der Datenbank oder des aufrufenden Geräts? Darf die Kapazität unter die bereits bestätigte Menge sinken? Diese Antworten müssen aus dem konkreten Produkt kommen.

Für einen Agentenauftrag leite ich daraus ab: Eine Invariante braucht bestätigte Begriffe und konkrete Fälle. Der Satz „Verhindere Überbuchung“ lässt zu viel Raum für unterschiedliche Auslegungen.

## Die Root kontrolliert den Zugang

Ein Aggregate enthält zusammengehörige Entities und Value Objects. Eine Entity besitzt eine fachlich relevante Identität über Änderungen hinweg. Ein Value Object beschreibt einen austauschbaren Wert, etwa eine Menge mit ihrer Einheit. Die Root ist die Entity, die den Zugang zum Aggregate kontrolliert.{q:1}

Im Kochkursbeispiel könntest du ein Platzkontingent mit seinen Vormerkungen als möglichen Entwurf untersuchen. Eine Operation wie `plaetzeVormerken` entscheidet innerhalb dieser Grenze, ob der Auftrag angenommen werden darf. Andere Aufrufer verändern einzelne Vormerkungen nicht beliebig an dieser Kontrolle vorbei.

Evans geht über die reine Schreibkontrolle hinaus: Dauerhafte externe Referenzen, also gespeicherte Verweise auf Entities innerhalb des Aggregates, sind auf die Root beschränkt. Referenzen auf interne Entities dürfen nur vorübergehend herausgegeben werden. Dadurch soll die Root ihren Zusammenhang wirksam schützen können.{q:1}

Das erfordert keine bestimmte Programmiersprache. Entscheidend ist, ob deine tatsächlichen Zugriffspfade diese Verantwortung respektieren. Ein sauber benanntes Objekt schützt wenig, wenn ein Importscript dieselben Daten unabhängig überschreibt.

## Die Grenze braucht eine fachliche Begründung

Nicht jede Beziehung gehört in dasselbe Aggregate. Im Beispiel könnte ein Platzkontingent eine Referenz auf den zugehörigen Kurstermin benötigen. Daraus folgt noch nicht, dass Kursbeschreibung, Lehrperson und sämtliche Rechnungen bei jeder Vormerkung gemeinsam geladen und verändert werden müssen.

Evans zeigt, wie zu kleine Grenzen gemeinsame Regeln verletzen können und wie zu weit gefasste Sperrbereiche unnötige Konkurrenz verursachen. Die Wahl braucht Wissen über die fachliche Bedeutung und das Änderungsverhalten der beteiligten Gegenstände.{q:1}

Eine Tabelle allein beantwortet diese Frage nicht. Ein Aggregate kann mehrere gespeicherte Strukturen umfassen. Umgekehrt können technisch eng verbundene Datensätze verschiedene fachliche Lebenszyklen haben.

Auch die [Grenze eines Bounded Context](post:bounded-context-gemeinsame-fachsprache) hat eine andere Aufgabe: Sie bestimmt, wo ein Modell eine konsistente Bedeutung besitzt. Innerhalb dieses Bereichs können viele Aggregate liegen. Eine automatische Aufteilung in eigenständig bereitgestellte Dienste, sogenannte Microservices, ergibt sich aus keiner dieser Grenzen.

## Ablehnung und Inkonsistenz unterscheiden

Im erfundenen Kochkurssystem sind noch zwei Plätze frei. Eine Anfrage für drei Plätze wird regulär abgelehnt. Das ist ein erwartbares Ergebnis einer gültigen Operation. Der Vertrag sollte erklären, dass dabei keine Vormerkung entsteht.

Findet das System dagegen bereits dreizehn bestätigte Plätze bei einer Kapazität von zwölf, ist die angenommene Invariante verletzt. Eine gewöhnliche Meldung „Leider ausgebucht“ würde diesen Zustand verdecken. Hier braucht das Produkt einen ausdrücklich entschiedenen Umgang mit dem Fehler.

Diese Unterscheidung ist eine eigene Anwendung der Zustandszusagen aus dem Buch. Evans beschreibt Invarianten und Nachbedingungen als Aussagen über korrekte Zustände und Wirkungen. Sie lassen sich durch Tests und geeignete Prüfungen ausdrücken; daraus folgt kein vollständiger Korrektheitsbeweis.{q:1}

Ein Agent sollte deshalb erfolgreiche Änderung, zulässige Ablehnung und vorhandene Inkonsistenz jeweils an einem eigenen Fall prüfen. Ein technisch erfolgreicher Datenbankaufruf sagt noch nicht, ob die erforderliche fachliche Wirkung eingetreten ist.

## Konkurrenz gehört in die Prüfung

Für den letzten freien Platz reichen zwei nacheinander ausgeführte Tests nicht aus. Beide Anfragen könnten zuerst freie Kapazität lesen und anschließend jeweils eine Vormerkung speichern. Wenn dein realer Ablauf solche Konkurrenz erlaubt, muss die technische Sicherung dazu passen.

Ob du dafür eine geeignete Transaktion, eine Versionsprüfung oder eine atomare Bedingung nutzt, entscheidet der vorhandene Entwurf. Der Buchgedanke liefert die fachliche Konsistenzpflicht; die konkrete Datenbanklösung ist zusätzliche Engineeringarbeit.

Gib dem Agenten daher die tatsächlich gemeinsam genutzten Daten und erlaubten Abläufe mit. Prüfe anschließend, dass von zwei konkurrierenden Anfragen höchstens die zulässige Menge angenommen wird. Der [Beitrag über API-Verträge](post:api-vertraege-schema-coding-agents) erklärt ergänzend, warum passende Eingabeformen solche Zustandsfragen noch nicht lösen.

## Mit einer gefährdeten Regel beginnen

Aggregate verursachen Aufwand. Große Grenzen können Änderungen blockieren und viele Daten in eine Operation ziehen. Kleine Grenzen können notwendige Abstimmung auf mehrere Stellen verteilen. Zwischen Aggregaten brauchen fachliche Beziehungen gegebenenfalls eigene, ausdrücklich verstandene Konsistenzregeln.{q:1}

Du musst deshalb weder jeden Datensatz in ein neues Objektmodell verpacken noch jede Beziehung sofort umbauen. Wähle eine Änderung, bei der eine konkrete Regel gefährdet ist. Formuliere ihre Invariante, benenne die kontrollierende Root und verfolge alle bestehenden Schreibpfade. Lass den Agenten dann einen Erfolgsfall, eine reguläre Ablehnung und die relevante Konkurrenzsituation prüfen. Danach kannst du die Grenze anhand ihres tatsächlichen Nutzens beurteilen.
