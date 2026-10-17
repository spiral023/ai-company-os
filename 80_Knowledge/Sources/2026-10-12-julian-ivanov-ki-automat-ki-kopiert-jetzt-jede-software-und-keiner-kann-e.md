---
url: https://www.youtube.com/watch?v=flfoVkkOLL0
autor: "Julian Ivanov | KI-Automatisierung"
datum: 2026-10-12
erfasst: 2026-10-17
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-10-12-julian-ivanov-ki-automat-ki-kopiert-jetzt-jede-software-und-keiner-kann-e.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Software-Nachbauten nach Rekonstruktionsweg und geprüftem Funktionsumfang beurteilen

Julian Ivanov unterscheidet zwei Arbeitsweisen: ausgelieferte Programmdateien analysieren oder ein bestehendes Programm bedienen und sein beobachtetes Verhalten neu implementieren. Für eine praktische Entscheidung zählt, welche Funktionen tatsächlich untersucht und geprüft wurden. Die Grundlage dieser Notiz sind Videobeschreibung und automatisch erzeugtes deutsches Transkript; eine eigene Sichtprüfung der Videobilder oder Durchführung mit REA fehlt.

## Was das Material konkret beschreibt

Die Einleitung schildert eine PhotoCraft-Demonstration mit Ebenen, Verschieben, Zeichnen und Effekten sowie eine Agentenschnittstelle. Das Transkript dokumentiert, dass der Sprecher diese Aktionen beschreibt; es ersetzt keine eigene Prüfung ihrer Bedienbarkeit oder Ergebnisqualität. Daraus folgt weder ein vollständiger Adobe-Ersatz noch ein im Video nachgewiesener Produktionsprozess für sieben Anwendungen.

Für REA und Ghidra erklärt Ivanov die Verbindung zu Coding-Agenten und das Fragen nach einzelnen Funktionen. Im archivierten Material ist jedoch kein vollständiger eigener Lauf von untersuchter Eingabedatei über belegte Befunde bis zu gebautem und getestetem Nachbau dokumentiert. Spiele-Mashups und ArtCraft dienen überwiegend als angeführte Beispiele anderer Entwickler.

## Zwei Rekonstruktionswege brauchen unterschiedliche Belege

**Analyse ausgelieferter Artefakte:** Ghidra soll aus Binärdateien rekonstruierte Programmlogik zugänglich machen; ein Agent hilft beim Zuordnen und Benennen. REA wird als Untersuchungsschicht mit verständlicher Frage, konkreten Fundstellen und optionalem Nachbau beschrieben. Bei klassischen Binärdateien nennt Ivanov zusätzliche Analysewerkzeuge, bei manchen Desktop-Anwendungen einen direkteren Zugang.

Das Transkript erklärt den Fortschritt anhand sogenannter Matching-Projekte: Code schreiben, erneut kompilieren und mit dem Original vergleichen. Eigene Einordnung: Dieses Vergleichsziel ist enger als die pauschale Wiedergewinnung des ursprünglichen Quellcodes. Verlorene Namen, Kommentare und Struktur werden durch einen passenden Ausgabevergleich nicht automatisch wiederhergestellt. Auch die Behauptung, ein rekonstruiertes Spiel lasse sich für jedes Gerät neu übersetzen, wird hier nicht als geprüfte Portabilität übernommen.

**Beobachtung von außen:** Der Sprecher beschreibt, wie Agenten Anwendungen bedienen, Screenshots auswerten und Eingaben, Ausgaben und Regeln festhalten. Daraus soll eine eigene Implementierung entstehen. Bei ArtCraft nennt er zusätzlich öffentliche Dateiformatdokumentation als Grundlage. Das ist seine Darstellung des Entstehungswegs, kein unabhängig geprüfter Nachweis über sämtliche verwendeten Quellen oder implementierten Funktionen.

## Übertragbarer Ablauf für Altsoftware

Aus der beschriebenen Verhaltensaufnahme lässt sich eine begrenzte Routine ableiten:

1. Einen benötigten Ablauf auswählen, statt das gesamte Altprodukt zum Ziel zu erklären.
2. Eingaben, sichtbare Ausgaben und dazwischen beobachtete Regeln festhalten.
3. Fundstellen und offene Annahmen auseinanderhalten; unzugängliche Serverfunktionen nicht als verstanden behandeln.
4. Einen eigenen Funktionsumfang definieren und den Nachbau gegen dieselben Beobachtungsfälle prüfen.

Der letzte Schritt ist eine methodische Ableitung, kein im Material nachgewiesener Abnahmelauf. Als Anlass nennt Ivanov Anwendungen ohne zeitgemäße Schnittstellen und mit hohem Erneuerungsbedarf. Die erwähnte Unternehmensstudie und sein Einsparpotenzial sind im Archiv nicht unabhängig geprüft; daraus entsteht keine belastbare Wirtschaftlichkeitsrechnung.

## Grenzen des Ersatzversprechens

Ivanov nennt selbst fehlende Funktionen und Tastenkürzel sowie serverabhängige Funktionen wie Generative Fill. Spiele-Mashups bezeichnet er als fehlerbehaftet und noch nicht fertig. Seine Prognose, solche Produkte könnten etablierte Abos ersetzen, geht damit über die gezeigten beziehungsweise beschriebenen Einzelfunktionen hinaus.

Die Videobeschreibung bewirbt eine Unterscheidung der Rechtslage. Im Transkript werden Dekompilieren pauschal als verboten und Beobachten mit Nachbauen pauschal als erlaubt dargestellt; diese Aussagen sind ungeprüfte Rechtsbehauptungen des Sprechers. Die Notiz übernimmt daraus keine rechtliche Freigabe. Lokale Artefaktanalyse und Datenverarbeitung durch den angeschlossenen Agenten sind zudem getrennte Fragen; Datenabflussfreiheit wird durch das Material nicht belegt.

## Einordnung

Der Titel verspricht mehr Allgemeingültigkeit, als die im Transkript beschriebenen Einzelfunktionen tragen. Nutzbar ist die Trennung von Artefaktanalyse und Verhaltensaufnahme. Ein eigener Nachbau benötigt einen abgegrenzten Funktionsvertrag und Vergleichsfälle; Produktnamen und Codeumfang ersetzen diese nicht. Automatische Untertitel verfälschen mehrfach Modell-, Werkzeug- und Projektnamen, weshalb daraus keine wörtlichen technischen Zitate übernommen werden. Die Rechtsaussagen und Zukunftsprognosen bleiben ausdrücklich Aussagen der Quelle.

## Kernaussagen

- [[Codepfad-vor-Aenderung-nachvollziehen]]: Bei Artefaktanalyse die konkrete Funktion und ihre Belege verfolgen; bei äußerer Beobachtung innere Logik als unbekannt erhalten.
- [[Testharness-als-staerkster-Hebel]]: Matching-Vergleiche erklären einen überprüfbaren Teil der Rekonstruktion, belegen jedoch weder Vollständigkeit eines Produkts noch allgemeine Portabilität.

## Verbindungen

- [[Codepfad-vor-Aenderung-nachvollziehen]] hilft, aus dem Gesamtnachbauversprechen eine begrenzte Untersuchungsfrage zu machen.
- [[Testharness-als-staerkster-Hebel]] liefert den Maßstab für nachvollziehbare Vergleichsfälle statt bloßer Nachbauetiketten.
- [[2026-10-12-0xcodila-2109623431763292649]] greift dieselben REA-/ArtCraft-Erzählungen auf; diese Überschneidung ist keine unabhängige Bestätigung der Showcase-Ergebnisse.
