---
titel: "Deep Modules: Weniger Aufruferwissen für Coding Agents"
datum: 2026-10-29
kategorie: arbeitsweisen
zusammenfassung: "Wie du Modulgrenzen am nötigen Aufruferwissen prüfst: Ein hypothetischer Dateiimport zeigt Deep Modules, versteckte Abhängigkeiten und einen konkreten Reviewauftrag für Coding Agents."
status: freigegeben
geprueft_am: 2026-10-29
freigabe: automatisch
quellen:
  - 2021-07-01-pdf-a-philosophy-of-software-design-2nd-edition
---

## Kurz gesagt

- Schreibe auf, was ein Aufrufer für die korrekte Nutzung deines Moduls wissen muss.
- Bündle gemeinsam veränderliche Entscheidungen bei einem klaren Verantwortlichen.
- Prüfe neue Grenzen an einem konkreten Änderungsfall und am erhaltenen Verhalten.

John Ousterhout beschreibt in [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php) Deep Modules: Bausteine, die viel Funktionalität hinter einer verständlichen Schnittstelle bereitstellen. Für die Arbeit mit einem Coding Agent, also einem KI-System zur Bearbeitung von Entwicklungsaufgaben, lässt sich daraus eine hilfreiche Frage ableiten: Wie viel Wissen verlangt eine Änderung von ihm? Diese Übertragung auf Agenten ist eine eigene Anwendung der Entwurfsprinzipien des Buchs. Sie enthält kein Versprechen über Geschwindigkeit oder eingesparte Tokens. {q:1}

## Was deine Aufrufer wissen müssen

Eine Schnittstelle umfasst alle Bedingungen ihrer Benutzung. Dazu gehören Rückgabewerte, erlaubte Reihenfolgen, Nebenwirkungen und mögliche Fehler. Eine kurze Methodensignatur kann einen beträchtlichen Lernaufwand verbergen. Vielleicht darfst du die Methode erst nach einer Initialisierung aufrufen. Vielleicht wird ein übergebenes Objekt verändert. Vielleicht liefert ein leeres Ergebnis zwei verschiedene Zustände, die du zusätzlich unterscheiden musst.

Ousterhout zählt solche informellen Verpflichtungen zu den Kosten einer Schnittstelle. Ein tiefes Modul hält diese Kosten im Verhältnis zu seiner Funktionalität gering. Seine Implementierung darf dafür anspruchsvoll sein. Die Darstellung auf den PDF-Seiten 30–39 liefert einen Entwurfsmaßstab, keine Formel, mit der du aus Dateigrößen die Qualität berechnest. {q:1}

Für deinen Review bedeutet das: Lass dir die Verwendung erklären, bevor du über die Zahl der Hilfsfunktionen entscheidest. Ein verständlicher normaler Aufruf und ein klarer Fehlerfall zeigen oft mehr als eine Liste wohlklingender Klassennamen.

## Ein Import als Gedankenexperiment

Stell dir einen hypothetischen Dienst vor, der Lieferantenlisten importiert. Heute muss jeder Aufrufer die Zeichenkodierung erkennen, Spaltennamen vereinheitlichen, Pflichtfelder kontrollieren und Datumswerte umwandeln. Anschließend übergibt er die bereinigten Daten an ein Speichermodul.

Du beauftragst einen Agenten, ein weiteres Eingabeformat zu unterstützen. Er findet drei bisherige Aufrufer und ergänzt die neue Regel jeweils dort. Die einzelnen Änderungen wirken überschaubar. Künftig muss jede Korrektur der Formatregel dieselben Stellen berücksichtigen. Wer einen Aufrufer übersieht, hinterlässt ein anderes Verhalten.

Eine mögliche tiefere Grenze wäre ein Importmodul, das Eingangsdaten entgegennimmt und verständliche Fachdaten oder konkrete Ablehnungsgründe zurückgibt. Die Bedeutung der Datumsfelder und die erlaubten Formate liegen dann an einem erkennbaren Ort. Ob diese Grenze passt, müsstest du an den tatsächlichen Aufrufen prüfen. Das Beispiel beschreibt einen Entwurf, keinen durchgeführten Umbau.

## Wer die Formatentscheidung besitzt

Information Hiding bedeutet, Entwurfswissen so zu kapseln, dass andere Teile es für ihre Arbeit nicht kennen müssen. Private Felder allein erreichen das kaum, wenn mehrere Module dieselben Formatregeln unabhängig umsetzen. Ousterhout warnt auf den PDF-Seiten 40–49 insbesondere vor einer Zerlegung, die lediglich dem zeitlichen Ablauf folgt. Lesen und Schreiben können etwa dieselbe Formatentscheidung benötigen. {q:1}

Beim gedachten Import würdest du deshalb untersuchen, welche Regeln gemeinsam geändert werden. Die Phasen Einlesen, Prüfen und Speichern können weiterhin sichtbar sein. Ihre Grenzen sollten aber mit dem Besitz des nötigen Wissens zusammenpassen.

Auch fachlich relevante Information muss zugänglich bleiben. Wenn ein Import Werte ablehnt, braucht der Aufrufer möglicherweise Feld, Zeile und Grund, um eine Korrektur anzubieten. Eine bequeme Schnittstelle, die diese Information verschluckt, lässt eine notwendige Benutzungsbedingung offen. Den Vertrag einer API, also einer Programmierschnittstelle, kannst du dazu im [Beitrag über API-Verträge und Schemas](post:api-vertraege-schema-coding-agents) weiterverfolgen.

## Jede zusätzliche Ebene braucht eine Aufgabe

Ein Agent könnte vor jede vorhandene Importfunktion einen neuen Wrapper setzen, also eine zusätzliche umhüllende Funktion. Wenn diese nur dieselben Argumente weiterreicht, entstehen weitere Namen und Übergänge. Ousterhout behandelt solche Pass-through-Methoden auf den PDF-Seiten 61–70 als Warnsignal. Eine Schicht sollte einen eigenen verständlichen Beitrag leisten. {q:1}

Das kann die Auswahl einer passenden Implementierung sein. Es kann auch eine Übersetzung fremder Daten in einen stabilen Vertrag sein. Du brauchst dafür eine konkrete Erklärung: Welche Entscheidung trifft diese Ebene, und welches Wissen entfällt dadurch für ihre Benutzer?

Eine gemeinsame Schnittstelle mit mehreren Implementierungen kann denselben Methodennamen sinnvoll verwenden. Prüfe den verborgenen Mechanismus und die Benutzung. Eine automatische Regel, die kurze Weiterleitungen löscht, würde auch nützliche Grenzen treffen.

## So formulierst du einen Auftrag für den Agenten

Für die agentische Umsetzung leite ich daraus einen begrenzten Arbeitsauftrag ab. Lass zuerst die vorhandenen Aufrufer und ihre Pflichten beschreiben. Danach soll der Agent zwei mögliche Modulgrenzen anhand derselben benötigten Verwendung vergleichen. Eine Variante darf bestehende Teile zusammenführen; die andere kann eine klarere Schnittstelle innerhalb der heutigen Struktur suchen.

Verlange zu beiden Varianten den normalen Ablauf, einen relevanten Fehlerfall und eine plausible Änderung der Formatregel. Dadurch wird sichtbar, wo Wissen gebündelt wird und wo neue Verpflichtungen entstehen. Diese Skizzen benötigen noch keine vollständige Implementierung.

Erst für die ausgewählte Variante folgt ein Refactoring, eine Änderung der inneren Struktur bei erhaltenem äußerem Verhalten. Dazu brauchst du passende Verhaltensprüfungen. Ein überzeugender Entwurfstext liefert für sich noch keine Gewissheit, dass Datumswerte, Fehlermeldungen oder Nebenwirkungen erhalten bleiben.

## Prüfe eine echte Änderung

Nimm einen Baustein, den dein Team regelmäßig verändert. Beschreibe einen gegenwärtigen Änderungswunsch und alle Informationen, die du dafür zusammensuchen musst. Bitte den Agenten anschließend um eine Schnittstelle, die diesen Informationsbedarf nachvollziehbar begrenzt.

Bewerte den Vorschlag an zwei realen Aufrufen. Kannst du beide verstehen, ohne die Implementierung mitzulesen? Sind Fehler, Zuständigkeiten und Nebenwirkungen erkennbar? Lass danach genau die ausgewählte Änderung umsetzen und das relevante Verhalten prüfen.
