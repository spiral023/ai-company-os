---
url: https://claude.com/de/resources/articles/subagents-in-claude-code
autor: Claude
datum: 2026-04-07
erfasst: 2026-10-24
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-04-07-claude-how-and-when-to-use-subagents-in-claude-code.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Subagents gezielt für Isolation, Parallelität und unabhängige Prüfung einsetzen

Anthropics Praxisartikel beschreibt Einsatzentscheidungen für `Claude Code`. Belastbar ist die dokumentierte Arbeitsweise als Herstellerempfehlung; er liefert keine kontrollierte Messung von Qualität, Geschwindigkeit oder Tokenkosten. Die archivierte Textfassung kündigt mehrfach Code- und Promptbeispiele an, enthält deren Inhalt aber nicht. Sie trägt daher die konzeptionelle Auswertung, keine Rekonstruktion dieser Beispiele.

## Isolation als gezielter Kontextfilter

Ein Subagent arbeitet laut Artikel mit eigenem Kontextfenster und gibt relevante Ergebnisse an die Hauptkonversation zurück. Das eignet sich für umfangreiche Code-Recherche, deren Zwischenmaterial für die Umsetzung nicht dauerhaft benötigt wird. Der Nutzen liegt im kompakten Ergebnis statt vieler gelesener Dateien im Hauptkontext.

Eine zweite Anwendung ist die frische Perspektive: Ein Review ohne vorherige Implementierungsdiskussion soll Annahmen und Vertrautheitseffekte reduzieren. Das ist eine Empfehlung für unabhängige Prüfung, kein Nachweis objektiver oder fehlerfreier Ergebnisse.

## Parallelisieren, wenn die Arbeit unabhängig ist

Mehrere Agenten passen zu getrennten Dateien oder Komponenten ohne gegenseitige Abhängigkeiten. Der Auftrag sollte Umfang, Parallelität und Rückgabeformat explizit nennen. Der Artikel nennt zehn zu untersuchende Dateien oder drei unabhängige Teilaufgaben als Orientierung; diese Zahlen sind Heuristiken, keine evaluierten Schwellenwerte.

Gleichzeitige Änderungen an derselben Datei und eng verkettete Schritte gehören nach der Empfehlung in einen gemeinsamen Kontext. Delegation erzeugt selbst Tokenverbrauch, Anlaufaufwand und zusätzliche Indirektion. Bei kleinen Aufgaben kann dieser Aufwand den Nutzen übersteigen. Die behauptete Zeitersparnis durch drei parallele Agenten wird nicht mit Messdaten belegt.

## Wiederholung schrittweise standardisieren

Der Einstieg erfolgt mit klaren Gesprächsaufträgen. Wiederkehrende Spezialisten lassen sich über Agent-Dateien mit enger Beschreibung, Prompt und Werkzeugrechten definieren. Die Beschreibung soll konkrete Auslöser nennen, damit automatische Delegation zielgerichtet bleibt.

`CLAUDE.md` hält dauerhaft geltende Delegationsregeln; Skills bündeln wiederkehrende Abläufe und werden bedarfsabhängig geladen. Hooks können Prüfungen an Ereignisse koppeln. Das beschriebene `Stop`-Hook-Beispiel blockiert bei fehlgeschlagenen Tests und enthält einen Schutz gegen wiederholte Hook-Schleifen; ausführbarer Beispielcode fehlt im Archiv. Der Artikel empfiehlt, diese Automatisierung erst aus beobachteten Wiederholungen abzuleiten.

## Einordnung

Der April-Text begründet Subagents mit isolierbarem Kontext, unabhängiger Arbeit und frischen Reviews. Der Oktober-Artikel [[2026-10-22-claude-building-agents-when-to-fold-subagents-into-your]] ergänzt die Kosten verlorener Details und zusätzlicher Latenz. Das ist keine pauschale Umkehr: Bereits April warnt vor stark abhängigen Aufgaben und gemeinsamen Dateien. Eine Design-Implementierungs-Test-Pipeline ist deshalb nur dann sinnvoll, wenn ihre Übergaben den nötigen Kontext tatsächlich erhalten; Oktober verlangt dafür ausdrücklich eine Prüfung der Kontextgrenzen. Beide Quellen sind Herstellerberatung, keine allgemeingültige Architekturregel.

## Kernaussagen

- Umfangreiche Zwischenrecherche auslagern, wenn später nur das Ergebnis zählt.
- Parallelität verlangt unabhängige Teilaufgaben und klare Ergebnisverträge.
- Frischer Review-Kontext kann nützlich sein, ersetzt aber keine Verifikation.
- Kleine oder stark gekoppelte Aufgaben rechtfertigen Delegation oft nicht.
- Erst klare Aufträge erproben, dann wiederkehrende Abläufe automatisieren.

## Verbindungen

- [[Kontrollierte-Agent-Parallelisierung]] — begrenzt Parallelität auf unabhängige Arbeitsflächen.
- [[Kontext-Hygiene-Entscheidungsbaum]] — ordnet Auslagerung ein, wenn umfangreicher Zwischenoutput nicht erhalten bleiben muss.
- [[Erweiterungs-Ebenen-Zuordnung]] — unterscheidet dauerhafte Regeln, Skills, isolierte Agenten und ereignisgebundene Hooks.
