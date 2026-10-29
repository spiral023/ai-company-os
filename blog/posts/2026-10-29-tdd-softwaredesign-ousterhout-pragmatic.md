---
titel: "TDD und Softwaredesign: Wo Ousterhout widerspricht"
datum: 2026-10-29
kategorie: duell
zusammenfassung: "Ousterhout kritisiert TDD als Entwurfsroutine, Thomas und Hunt bevorzugen häufig Test-first. So trennst du bei Coding Agents Verhaltensprüfung, Fachziel und die Qualität einer Schnittstelle."
status: freigegeben
geprueft_am: 2026-10-29
freigabe: automatisch
quellen:
  - 2021-07-01-pdf-a-philosophy-of-software-design-2nd-edition
  - 2019-09-13-pdf-the-pragmatic-programmer-20th-anniversary-edition
---

## Kurz gesagt

- Prüfe bei neuen Funktionen den gewünschten Vertrag und den tatsächlichen Lösungsfortschritt.
- Schreibe für einen reproduzierbaren Bug zuerst einen Test, der am Fehler scheitert.
- Beurteile die Qualität einer Schnittstelle zusätzlich zum Ergebnis ihrer Tests.

John Ousterhout lehnt in [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php) TDD als allgemeine Entwurfsroutine ausdrücklich ab. TDD, kurz für Test-driven Development, bezeichnet einen Ablauf aus zuerst geschriebenem Test, minimaler Umsetzung und anschließender Strukturverbesserung. {q:1} David Thomas und Andrew Hunt stehen Test-first in [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) aufgeschlossener gegenüber. Auch sie warnen vor grünen Tests ohne Fortschritt zum eigentlichen Problem. {q:2}

## Welche Entscheidung Ousterhout schützen möchte

Ousterhout sieht die Gefahr, dass Entwickler jeweils nur die nächste verlangte Fähigkeit ergänzen. Eine zunächst passende Abstraktion kann dadurch aus immer neuen Spezialfällen entstehen. Die Aufmerksamkeit bleibt beim nächsten erfolgreichen Test, während die zusammenhängende Gestaltung der Schnittstelle zu wenig Raum bekommt.

Sein Vorschlag ist, eine gegenwärtig benötigte Abstraktion mit einem kohärenten Kern zu entwerfen. Dazu gehören die wesentlichen Operationen und ein verständlicher Vertrag. Hypothetische spätere Funktionen müssen dafür keine vorsorgliche Implementierung erhalten. Diese Position steht auf den PDF-Seiten 163–165. {q:1}

Zugleich schätzt er Unit-Tests, also Prüfungen begrenzter Softwarebausteine, als Schutz für strukturelle Änderungen. Für Bugfixes empfiehlt er ausdrücklich einen zuerst fehlschlagenden Regressionstest. Ein solcher Test hält den konkreten Fehlerfall dauerhaft fest. Seine Kritik betrifft damit einen bestimmten Weg zum Entwurf und lässt den Wert dieser Prüfungen bestehen.

## Welches Feedback Thomas und Hunt suchen

Thomas und Hunt betrachten einen Test als ersten Benutzer der neuen Schnittstelle. Schon beim Schreiben fällt auf, welche Umgebung benötigt wird und welche Begriffe unklar sind. Das kann Abhängigkeiten und Mehrdeutigkeiten vor der Implementierung sichtbar machen.

Sie bevorzugen Test-first in vielen Situationen und beschreiben kleine Schritte mit anschließendem Refactoring, einer Strukturverbesserung bei erhaltenem äußerem Verhalten. Zugleich kritisieren sie redundante Tests und ein ritualisiertes Streben nach vollständiger Zeilenabdeckung. Eine ausgeführte Zeile sagt schließlich wenig darüber, welche Eingabekombinationen geprüft wurden. {q:2}

Auf den PDF-Seiten 364–373 verlangen sie zudem den Blick auf die ganze Aufgabe. Kleine End-to-End-Schritte, also nutzbare Durchstiche durch den beteiligten technischen Ablauf, sollen Erkenntnisse liefern. Ein lange verfeinertes Teilmodell kann dabei am eigentlichen Ziel vorbeigehen. Ihr Einwand gegen sinnloses Testgrün berührt Ousterhouts Sorge, führt aber zu einer anderen allgemeinen Empfehlung.

## Eine Rabattfunktion als Gedankenexperiment

Stell dir einen hypothetischen Shop vor. Ein Coding Agent, ein KI-System zur Bearbeitung von Entwicklungsaufgaben, soll einen Rabatt für bestimmte Bestellungen ergänzen. Unklar ist, ob Versandkosten zur Berechnungsbasis zählen und wie die Rundung erfolgt.

Der Agent könnte zuerst einen Test für eine einzige Bestellung schreiben und anschließend genau diesen Fall erfüllen. Danach kommen weitere Fälle hinzu. Alle bisherigen Tests können zu den gewählten Regeln passen, obwohl die fachliche Bedeutung noch offen ist. Die Tests würden dann die anfängliche Annahme des Agenten fortschreiben.

Ein früher Vertragsentwurf würde die fehlenden Entscheidungen sichtbar machen: Berechnungsbasis, berechtigte Bestellungen, Rundung und Ergebnis. Konkrete Beispiele helfen dir anschließend, diese Semantik mit der zuständigen Person zu klären. Diese Anwendung auf Agenten ist eine eigene Ableitung aus beiden Büchern. Sie beschreibt kein durchgeführtes Shopprojekt und keine gemessene Überlegenheit eines Verfahrens.

## Warum der rote Test beim Bugfix zählt

Nehmen wir innerhalb desselben Gedankenexperiments an, die Rundungsregel sei längst festgelegt. Bei einer bestimmten Bestellung entsteht trotzdem ein falscher Betrag. Nun kannst du den Fehler zuerst mit einem gezielten Test reproduzieren.

Ousterhout begründet diese Reihenfolge ausdrücklich: Wenn du den Test erst nach der Reparatur schreibst, könnte er das ursprüngliche Problem gar nicht treffen. Sein beobachteter Fehlschlag liefert die entscheidende Gegenprobe. Die Passage findest du auf PDF-Seite 165. {q:1}

Für deinen Agentenauftrag bedeutet das, den fehlerauslösenden Fall, das bestätigte erwartete Ergebnis und denselben Test nach der Änderung festzuhalten. Sobald ein anderer Fehler oder eine zusätzliche Fachentscheidung auftaucht, wird sie gesondert bewertet. So bleibt erkennbar, welche Wirkung die Reparatur tatsächlich geprüft hat.

## Zwei Reviews beantworten unterschiedliche Fragen

Aus dem Vergleich leite ich für agentische Arbeit zwei zusammengehörige Prüfungen ab. Die erste betrachtet das Verhalten: Entsprechen Ergebnisse und Fehlerfälle der bestätigten Anforderung? Die zweite betrachtet die Abstraktion: Ist ihre Verwendung verständlich, und welche Kenntnisse verlangt sie von Aufrufern?

Für die gedachte Rabattfunktion könnte ein einzelner sinnvoller End-to-End-Schritt die Berechnung einer Bestellung bis zur angezeigten Summe führen. Daneben prüfst du, ob jeder Aufrufer selbst Rundungswissen besitzen muss oder ob dieses Wissen bei der passenden Komponente liegt.

Die [Erklärung zu Deep Modules](post:deep-modules-weniger-wissen-fuer-coding-agents) hilft beim zweiten Teil. Der [Beitrag über API-Verträge](post:kommentare-api-vertraege-softwaredesign) zeigt, wie du die nötige Benutzungssemantik früh beschreibst. Ein grüner Test und eine klare Schnittstelle tragen jeweils einen eigenen Teil zur Beurteilung bei.

## Welche Grenze der Vergleich hat

Beide Bücher argumentieren aus Erfahrung und Entwurfsüberzeugungen. Der Vergleich liefert keine kontrollierte Aussage darüber, welches Vorgehen heutige Coding Agents generell zuverlässiger macht. Die Bedeutung des Fachziels, verfügbare Prüfmöglichkeiten und die Folgekosten einer falschen Entscheidung bleiben entscheidend.

Auch die vorgeschlagene Verbindung aus früher Vertragsskizze und kleinen Testschritten ist eine eigene Anwendung. Du solltest sie an einem konkreten Auftrag bewerten. Zusätzliche Formulare und Tests müssen einen erkennbaren Informationsgewinn liefern. Sonst wächst der Ablauf, ohne die offene Frage besser zu beantworten.

## Kläre beim nächsten Auftrag zuerst die offene Frage

Nimm eine anstehende Änderung und unterscheide drei Fragen: Welches Verhalten ist bestätigt? Welche Entwurfsentscheidung ist noch offen? Welcher kleinste ausführbare Schritt liefert dafür brauchbares Feedback?

Bei einem reproduzierbaren Fehler beginne mit dessen scheiternder Prüfung. Bei einer neuen Abstraktion lass zuerst ihre Verwendung und wesentlichen Regeln beschreiben. Führe danach Verhaltenstest und Schnittstellenreview zusammen.
