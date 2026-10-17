---
url: https://www.youtube.com/watch?v=UGwj6WaZoxQ
autor: "Alex Sprogis"
datum: 2026-10-13
erfasst: 2026-10-17
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-10-13-alex-sprogis-so-nutzt-du-rea-um-jede-app-in-minuten-zu-kopier.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Reverse Engineering erst bei einer konkreten Erkenntnislücke einsetzen

Alex Sprogis stellt REA als Verbindung zwischen Coding Agent und Analysewerkzeugen vor und berichtet von zwei eigenen Versuchen. Der interessante Befund ist begrenzter als das Titelversprechen, jede App in Minuten zu kopieren: Bei einer einfachen Electron-Anwendung half die zusätzliche Werkzeugschicht wenig, bei einer nativen App lieferte sie nach seinem Bericht mehr Strukturwissen. Grundlage dieser Notiz sind Videobeschreibung und vollständig gelesenes automatisches Transkript; weder sichtbare Ergebnisse noch Laufzeiten wurden hier unabhängig geprüft.

## Die Werkzeugschicht ist kein fertiger Nachbau

Sprogis unterscheidet Disassembly und lesbareren dekompilierten Pseudocode. Letzterer ist nach seiner Erklärung kein wiedergewonnener Originalquellcode; Namen, Kommentare und ursprüngliche Struktur können fehlen. REA beschreibt er als MCP-/CLI-Schnittstelle zu Werkzeugen wie Hopper, Ghidra und IDA für native Programme sowie anderen Analysewegen für JavaScript, Electron und Websites.

Der Agent benötigt demnach nicht nur eine Frage, sondern passende zugängliche Artefakte und ein zum Ziel passendes Analysewerkzeug. Dokumentierte Unterstützung weiterer Zieltypen erwähnt der Sprecher, führt dafür aber keine eigenen Beispiele aus. Kosten der Agent-Nutzung und zusätzlicher Werkzeuge werden nicht beziffert; seine Aussage kostenloser Open-Source-Nutzung ist keine vollständige Kostenrechnung.

## Zwei berichtete Versuche mit unterschiedlichem Erkenntnisgewinn

**Electron-Diktierapp:** Der Sprecher beschreibt eine nicht namentlich genannte Anwendung, die Sprache aufnimmt, aufbereitet und in ein Textfeld einfügt. Er wollte den Aufbau verstehen und anschließend eine einfachere eigene Version erstellen. Der JavaScript-Bestand sei stark komprimiert und über mehr als 180 Dateien verteilt gewesen. Die erste MCP-Analyse sei nach etwa 30 Minuten abgebrochen; über die Kommandozeile habe die Analyse ungefähr fünf Minuten benötigt. Die wichtigsten Informationen habe der Agent schließlich durch einfache Textsuche gefunden. Diese Angaben sind ein einzelner Erfahrungsbericht, kein kontrollierter Vergleich von MCP, CLI oder REA.

**Native macOS-Erinnerungen-App:** Hier habe REA mehr über Datenmodell, Berechtigungen, Funktionsbereiche und Architektur samt Fundstellen geliefert. Die Kernlogik habe jedoch außerhalb des untersuchten App-Bestands in einem gemeinsam genutzten macOS-Systembestand gelegen und sei unzugänglich geblieben. Die genaue technische Ablage lässt sich aus der unsicheren Transkription nicht verlässlich bestimmen. Eine Strukturübersicht ist damit nicht gleichbedeutend mit vollständig rekonstruierter Funktionalität.

## Der Minimalweg beginnt vor REA

Für die Diktierfunktion hält Sprogis eine verständliche Verhaltensbeschreibung, gegebenenfalls ergänzt um Screenshots, für wahrscheinlich ausreichend. Nach seiner Schilderung ergänzte der Agent fehlende Analyseinformationen ohnehin durch Annahmen. Diese Unterscheidung ist für die eigene Einordnung entscheidend: Eine plausibel funktionierende Neuentwicklung beweist nicht, dass die interne Logik der Vorlage rekonstruiert wurde.

Der übertragbare Ablauf lautet deshalb: gewünschtes Verhalten und Zielumfang beschreiben, vorhandene Informationen auswerten und erst die verbleibende konkrete Frage mit Spezialwerkzeugen verfolgen. Liegt die wesentliche Logik auf einem nicht zugänglichen Backend, begrenzt der Sprecher die Erkenntnis auf beobachtbares UI-Verhalten. Aus lokal vorliegenden Dateien folgt kein Zugriff auf diese Implementierung.

## Analyse in einen begrenzten Entwicklungsauftrag überführen

Sprogis empfiehlt vor der Umsetzung Anforderungsdokumente und eine Spezifikation statt unmittelbarer Eins-zu-eins-Übernahme. Der Funktionsumfang soll feststehen, die Umsetzung geplant werden und eine Definition of Done erkennbar machen, wann die eigene Funktion fertig ist. Das ist eine Empfehlung für eine prüfbare Übergabe; ein vollständiger Plan, Tests oder Verhaltensvergleich werden im Transkript nicht dokumentiert.

Seine Einschätzungen zu zulässiger Nutzung, Lizenzen und Clean-Room-Nachbauten sind ungeprüfte Aussagen der Quelle. Die erwähnten ArtCraft-Nachbauten und Popularitätszahlen dienen als Einleitung und sind keine zusätzlichen eigenen Testfälle oder unabhängigen Bestätigungen derselben Produktversprechen.

## Einordnung

Die Stärke der Quelle liegt in der ausdrücklichen Frage, ob das zusätzliche Tool überhaupt nötig war. Sie liefert einen Anlass, Analyseaufwand am Erkenntnisgewinn statt an der Zahl verfügbarer Tools zu messen. Die beiden berichteten Versuche belegen weder allgemeine Geschwindigkeit noch vollständige Kopierbarkeit beliebiger Apps. Die Backend-Grenze und fehlende native Kernlogik schränken den Anspruch weiter ein. Es wurden hier keine Programme installiert, REA-Funktionen ausgeführt oder Video-Frames geprüft; das Roharchiv referenziert keine Bilder.

## Kernaussagen

- [[Codepfad-vor-Aenderung-nachvollziehen]]: Zielverhalten, Fundstellen und offene Fragen eingrenzen; Textsuche kann bereits genügen, Spezialanalyse braucht einen konkreten Mehrwert.
- [[Plan-first-mit-getrenntem-Review]]: Erkannte Funktionalität zuerst in Spezifikation, Scope und Definition of Done übertragen; die Quelle dokumentiert keinen separaten Review-Nachweis.

## Verbindungen

- [[2026-10-12-0xmovez-2109604520770548146]] stellt REA als umfassenderen Kurs vor; Sprogis’ Einzelfälle begrenzen solche pauschalen Versprechen, bestätigen gemeinsame Showcases aber nicht unabhängig.
- [[Freiheitsgrad-nach-Aufgaben-Fragilitaet]] hilft, kreative Eigenimplementierung von der exakten Prüfung vermuteter Originalmechanismen zu unterscheiden.
