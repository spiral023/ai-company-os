---
url: https://www.youtube.com/watch?v=cKgbU_wWWts
autor: Alex Sprogis
datum: 2026-10-25
erfasst: 2026-10-28
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-10-25-alex-sprogis-die-qualitaet-von-ki-code-ist-nicht-so-gut-wie-d.md
thema: Arbeitsweisen
zeitkritisch: ja
---

# Entwicklungsqualität an Fehlerfolgen und Abhängigkeiten ausrichten

Alex Sprogis verbindet Verständlichkeit und Änderbarkeit mit dem Risiko eines Softwareprojekts. Sein Beitrag vom 25.10.2026 erläutert eine Auswahlheuristik und den eigenen Entwicklungsablauf; die angeführten Modell- und Sicherheitsstatistiken sind hier nur sekundär über ein automatisches Transkript erfasst.

## Qualitätsaufwand über vier Fragen bestimmen

Sprogis übernimmt den Rahmen aus einem verlinkten Talk von Max Kanat-Alexander. Entscheidend sind Ausfallfolgen, Kosten eines Neubaus, abhängige Menschen oder Systeme und laufender Wartungsbedarf. Wenig Abhängigkeit und geringe Wiederherstellungskosten sprechen in seiner Darstellung für ein kurzlebiges Hilfswerkzeug; mit steigenden Folgen und längerer Nutzung wächst der Bedarf an planbarer Änderung und Prüfung.

Dabei greift ein Rückkopplungseffekt: Schwer verständlicher Code erschwert die nächste Änderung. Diese Änderung kann wiederum Fehler verursachen und das Verständnis weiter erschweren. Ein Coding Agent kann die Menge der Änderungen erhöhen; schnelleres Schreiben ist deshalb kein Ersatz für eine überprüfbare Struktur.

## Den Prüfaufwand in den Ablauf einbauen

Der beschriebene Zyklus beginnt bei einer Spezifikation mit Sonderfällen und Akzeptanzkriterien, führt über Aufgabenplanung zur Implementierung und endet mit einer gesonderten Prüfung. Ein Prüf-Agent soll nur Spezifikation und fertiges Ergebnis erhalten und jedes Akzeptanzkriterium untersuchen. Der Autor nennt Tests vor oder nach der Implementierung sowie automatisch ausgeführte Linter, Typprüfungen und Tests. Ein Bericht soll dem Menschen die Ergebnisbewertung ermöglichen.

Dies ist ein Vorschlag, wiederholte Sorgfalt durch gemeinsame Standards und automatisierte Prüfungen zu erleichtern. Eine Reduktion des tatsächlichen Gesamtaufwands oder eine verlässliche Erkennungsquote wird nicht gemessen.

## Grenzen der zitierten Zahlen

Das Video verweist auf Sonar, Veracode, Endor Labs und eine Auswertung der Software Improvement Group. Aufgaben, Bezugsgrößen und vollständige Methoden wurden in diesem Quellenlauf nicht an den Originalberichten geprüft. Die Zahlen werden deshalb nicht als gesicherte Einzelangaben ins Faktenregister übernommen. Eigenwerbung, Sponsoring und Vertriebsinteressen der erwähnten Analyseanbieter sind Teil des Quellenkontexts.

## Einordnung

Die vier Fragen helfen, Prüfaufwand anhand konkreter Folgen zu begründen. Die pauschale Aussage, Qualität sei bei Wegwerfsoftware egal, ist zu weit: Auch ein schnell ersetzbares Werkzeug kann folgenreiche Aktionen ausführen oder auf wichtige Daten zugreifen. Ein separater Agent und grüne Tests belegen jeweils nur die tatsächlich geprüften Eigenschaften; die Auswahl der Akzeptanzkriterien bleibt entscheidend. Diese Aufarbeitung beruht auf Beschreibung und automatischem Transkript, nicht auf einer erneuten vollständigen Bild- oder Tonprüfung.

## Kernaussagen

- Ausfallfolgen, Neubaukosten, Abhängigkeiten und Wartung gemeinsam betrachten → [[Qualitaetsaufwand-nach-Folgen-und-Abhaengigkeiten-staffeln]].
- Spezifikation, Umsetzung und Ergebnisprüfung mit eigener Informationsgrenze führen → [[Plan-first-mit-getrenntem-Review]].
- Wiederkehrende Fehler durch konkrete automatisierte Prüfungen erfassbar machen → [[Testharness-als-staerkster-Hebel]].

## Verbindungen

- [[Qualitaetsaufwand-nach-Folgen-und-Abhaengigkeiten-staffeln]]
- [[Produktreife-durch-echte-Testnutzer]]
- [[Pruefungen-nach-Feedbackzeitpunkt-staffeln]]
