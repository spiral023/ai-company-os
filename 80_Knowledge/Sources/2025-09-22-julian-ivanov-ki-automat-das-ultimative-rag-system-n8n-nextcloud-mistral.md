---
url: https://www.youtube.com/watch?v=tFANS8Fn2ao
autor: "Julian Ivanov | KI-Automatisierung"
datum: 2025-09-22
erfasst: 2026-10-11
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2025-09-22-julian-ivanov-ki-automat-das-ultimative-rag-system-n8n-nextcloud-mistral.md
thema: Arbeitsweisen
zeitkritisch: ja
---

# RAG für Texte, Bilder und Tabellen: getrennte Verarbeitung, gemeinsame Quellenidentität

Julian Ivanov demonstriert am 22. September 2025 ein RAG-System, das Dokumente nach Datentyp verarbeitet und Antworten über mehrere Zugriffswege erzeugt. Der übertragbare Kern ist die Trennung von Textsuche, vollständigem Dokumentabruf und berechenbaren Tabellenabfragen, verbunden durch dieselbe Datei-ID. Das Tutorial zeigt ausgewählte Beispiele und erklärt den Workflow; es liefert keinen systematischen Vergleich der Antwortqualität oder Nachweis für die beworbene Datenschutzkonformität. Grundlage dieser Notiz ist ein automatisch erzeugtes Transkript, keine manuell geprüfte Abschrift.

## Dokumente erfassen und ihre Ableitungen verbinden

Im gezeigten Aufbau hält `Nextcloud` die Originaldateien, `n8n` orchestriert die Verarbeitung, `Supabase` speichert Daten und Bilder, und `OpenWebUI` stellt den Chat dar. OCR, Embeddings, Sprachmodell und Reranking werden über weitere Dienste eingebunden. Die konkrete Dienstekombination beschreibt den damaligen Aufbau; wichtiger ist die Zuordnung jeder Ableitung zu ihrem Original.

Eine Metadatentabelle enthält Datei-ID, Titel und Pfad. Text-Chunks, tabellarische Zeilen und der Synchronisationszustand beziehen sich auf diese Identität. So kann der Agent einen gefundenen Abschnitt einem Dokument zuordnen, weitere Abschnitte nachladen und die verwendete Datei nennen. Die Chat-Historie ist davon getrennt: Ein gespeichertes Gespräch ersetzt keinen aktuellen Dokumentenbestand.

Tabellen gehen durch einen eigenen Verarbeitungspfad. Excel- oder CSV-Zeilen werden als strukturierte Datensätze in eine Tabelle aufgenommen. Text- und PDF-Dokumente gehen dagegen durch den OCR-Pfad. `Mistral OCR` liefert im Tutorial Text und annotierte Bilder; eine nachgelagerte Verarbeitung lädt die Bilder in einen Storage-Bucket und verbindet ihre Links mit den passenden Textstellen. Der Agent kann dadurch Text und Bilder im Zusammenhang ausgeben. Eine einfache Textextraktion, die Bilder oder komplexes Layout verliert, beschneidet bereits vor dem Retrieval die Informationsbasis.

## Textsuche begrenzen, ohne Zusammenhang zu verlieren

Ivanov setzt auf modellgestütztes Chunking statt ausschließlich auf feste Zeichenlängen. Überschriften und zusammengehörige Gedankengänge sollen möglichst im selben Abschnitt bleiben. Der Prompt lässt sich auf den Dokumententyp abstimmen; die Methode garantiert jedoch keine fehlerfreien Abschnittsgrenzen und verursacht zusätzliche Modellarbeit.

Embeddings ermöglichen zunächst die Suche nach ähnlichen Abschnitten. Ein Reranker bewertet die gefundenen Kandidaten anschließend im Verhältnis zur Frage und verkleinert die Auswahl für den Antwort-Agenten. Im gezeigten Beispiel werden 25 Kandidaten auf vier reduziert. Das ist eine Konfiguration der Demo, kein allgemein optimaler Wert und keine gemessene Qualitätssteigerung. Die Behauptung, Vektorresultate seien grundsätzlich ungeordnet, bleibt zu pauschal; entscheidend ist hier die zusätzliche Relevanzbewertung.

## Drei Zugriffswege für unterschiedliche Fragen

Der System-Prompt beschreibt die verfügbaren Tools und ihre Einsatzfälle. Für normale Inhaltsfragen beginnt der Agent mit RAG. Reicht der Ausschnitt nicht aus, kann er die Dokumentenliste prüfen und anhand einer Datei-ID den vollständigen Inhalt abrufen. Fragen nach Summen, Maxima oder ausgewählten Tabellenzeilen gehen direkt an ein SQL-Tool. Damit bestimmt das Modell den Abfrageweg, während die Datenbank die eigentliche Berechnung ausführt.

In der Demo beantwortet das System Fragen zu einer bebilderten Kaffeemaschinenanleitung, zu Preisen in einem Word-Dokument und zu aggregierten Excel-Werten. Der Agent wird angewiesen, fehlendes Wissen offen zu benennen und Bilder passend zwischen Textabschnitten auszugeben. Die ausgewählten erfolgreichen Beispiele zeigen die beabsichtigte Nutzung, prüfen aber weder schwierige OCR-Fälle noch falsch formulierte SQL-Abfragen oder systematische Halluzinationsraten.

## Aktualisierung und Entfernung gehören zum Retrieval

Der gezeigte `Nextcloud`-Pfad vergleicht Originalbestand und Synchronisationstabelle anhand vorhandener Dateien und Änderungszeitpunkten. Neue oder veränderte Dateien werden erneut verarbeitet; alte Dokumentableitungen werden dabei entfernt. Ein eigener Lauf erkennt entfernte Originale durch Bestandsvergleich und löscht ihre gespeicherten Informationen. Die im Video genannten Intervalle sind Einstellungen dieses Workflows, keine Zusage sofortiger Aktualität.

Dieser Lebenszyklus ist genauso wichtig wie die Suchmethode: Eine präzise Antwort aus einem veralteten Dokument kann sachlich falsch sein. Das Tutorial zeigt den erfolgreichen Normalfall, behandelt aber keine vollständige Fehler- oder Wiederanlaufstrategie.

## Einordnung

Eigene Bewertung: Der Aufbau liefert einen konkreten Ansatz für gemischte Wissensbestände, weil semantische Suche, Volltext und strukturierte Berechnung unterschiedliche Aufgaben übernehmen. Vor einer Übernahme wären OCR-Ergebnisse, Quellenzuordnung, SQL-Filter und Aktualisierung mit bekannten Sollantworten zu prüfen. Aus der beschriebenen Reihenfolge lässt sich außerdem ein möglicher Fehlerfall ableiten: Wird der Synchronisationsstand vor erfolgreicher Neuverarbeitung fortgeschrieben oder der Altbestand vorzeitig gelöscht, braucht der Ablauf nachvollziehbare Wiederholung und Fehlerbehandlung. Öffentlich erreichbare Bildlinks und externe OCR-, Modell- und Reranking-Dienste passen nicht ohne weitere Prüfung zur pauschalen Zusage vollständiger Datenkontrolle. Die beworbene DSGVO-Konformität wird deshalb nicht übernommen. Toolverfügbarkeit, Hostingbedingungen und Preise stammen aus 2025 und müssten vor einer heutigen Umsetzung neu geprüft werden.

## Kernaussagen

- Die Agent-Tools sollten die tatsächlichen Informationsaufgaben trennen: Text suchen, fehlenden Kontext nachladen und Tabellen berechnen; Anschluss an [[Action-Space-Design-nach-Modellfaehigkeit]].
- OCR und Chunking beeinflussen, welche Informationen überhaupt auffindbar sind; eine erfolgreiche Antwort-Demo beweist keine robuste Gesamtpipeline.
- Datei-ID und Synchronisationszustand verbinden Originale mit ihren Ableitungen; Änderungen und entfernte Dateien müssen im Antwortbestand ankommen.
- Als eigene Prüffolgerung brauchen Retrieval, Berechnung und Aktualisierung bekannte Sollfälle; Anschluss an [[Testharness-als-staerkster-Hebel]].

## Verbindungen

- [[Action-Space-Design-nach-Modellfaehigkeit]] — Die spezialisierten Zugriffswege begrenzen die Aufgaben des Modells und übertragen Berechnungen an ein dafür vorgesehenes Tool.
- [[Testharness-als-staerkster-Hebel]] — Die Demo liefert konkrete Ausgangsfälle für eine spätere Prüfung, ersetzt diese aber nicht.
- [[Kontext-Hygiene-Entscheidungsbaum]] — Die begrenzte Abschnittsauswahl und das gezielte Nachladen betreffen den Kontextaufbau; das bestehende Pattern behandelt zusätzlich die Pflege laufender Sessions.
- [[RAG-mit-Text-Tabellen-und-Volltextpfad]]
