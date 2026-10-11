---
url: https://developers.openai.com/blog/codex-as-a-platform
autor: "OpenAI Developers"
datum: 2026-10-11
datum_unsicher: true
erfasst: 2026-10-11
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-10-11-developers-codex-as-a-platform-build-on-the-open-agent-harn.md
thema: Tools & Releases
zeitkritisch: ja
---

# Ein wiederverwendbarer Agent-Harness lässt Produktverantwortung bei der Anwendung

OpenAI beschreibt Codex als offene Ausführungsschicht für eigene Produkte, nicht nur als App, CLI oder IDE-Erweiterung. Übertragbar ist die Aufteilung: Codex trägt Agent-Loop und Lifecycle; die Anwendung trägt Fachkontext, Daten, Business-Regeln und Freigaben. Der archivierte Text ist eine Herstellerbeschreibung; sein Veröffentlichungsdatum ist nicht gesichert, das Datum im Frontmatter stammt aus der Inbox.

## Was der Harness übernimmt

Ein Agent benötigt neben Prompt und Modell Kontextpflege, Werkzeuge, Fortschrittsereignisse, Fehlerbehandlung, Freigaben und Fortsetzung über mehrere Turns. Der offene Codex-Harness verwaltet Gesprächszustand, streamt Ausführung, nutzt Tools und setzt konfigurierte Sandbox- und Approval-Regeln durch. Über den dokumentierten `app-server`-Client-Protocol können Anwendungen Threads erzeugen, Turns starten, Ereignisse empfangen und Freigabeanfragen behandeln.

OpenAI nennt auf `ARC-AGI-3` für `GPT-5.6 Sol` einen Anstieg von `13,3 %` auf `38,3 %` durch erhaltenes Reasoning und Context-Compaction, bei sechsmal weniger Output-Tokens. Das illustriert den möglichen Einfluss des Harness, liefert im Artikel aber keine vollständige reproduzierbare Testkonfiguration und keinen allgemeinen Produktivitätsnachweis.

CLI, `app-server` und offizielles SDK werden als Open Source beschrieben. Diese Aussage bezieht sich auf Harness und Integrationsflächen; Modellzugang und Managed Services bleiben davon getrennt.

## Die Integrationsschicht folgt dem benötigten Lifecycle

| Bedarf | Im Artikel empfohlene Schicht |
|---|---|
| Begrenztes Skript, CI-Job oder einmaliger Hintergrundlauf mit strukturiertem Ergebnis | `codex exec` |
| Aufgaben aus Anwendungscode starten, fortsetzen oder streamen | Offizielles Codex SDK |
| Agent als Teil eines Produkts mit offenen Gesprächen, Ereignissen, Unterbrechungen, Tools und Freigabe-UI | Codex `app-server` |

Das SDK vereinfacht übliche programmatische Workflows. `app-server` verbindet das Produkt mit einem lokalen Codex-Prozess und gibt ihm direktere Kontrolle über Lifecycle und Benutzererlebnis. Ein Bedarf an vollständiger Produktinteraktion rechtfertigt diese zusätzliche Integration; ein begrenzter Job benötigt sie nicht automatisch.

## Was das Produkt weiterhin selbst trägt

Die Anwendung bewahrt ihre Dashboards, Dokumente, Karten, Warteschlangen und Datensätze. Sie liefert ausgewählte Entität, Nutzeraktion und sichtbaren Zustand als Kontext. Sie entscheidet über Ausführungsort, zugängliche Dateien und Tools, beobachtbare Arbeit, Freigaben und Rückgabe in das führende System. Eigene MCP-Dienste verbinden den Agenten mit aktuellen Daten und fachlichen Aktionen.

![Anwendung, Agent-Lifecycle und eigene MCP-Dienste mit Rückkopplung genehmigter Änderungen](../../00_Inbox/Quellen/URL/medien/2026-10-11-developers-codex-as-a-platform-build-on-the-open-agent-harn/01-bild.webp)

Das geprüfte Diagramm trennt Produktinterface, Business-Kontext und Zustimmung vom Agent-Loop und dessen sandboxed Execution sowie von den anwendungseigenen Daten und Aktionen. Genehmigte Änderungen aktualisieren anschließend die Produktansicht.

## Relay veranschaulicht den Ablauf mit fiktiven Daten

Die Beispielanwendung Relay zeigt Sendungen und Ausnahmen. Ein Klick wie „Compare recovery“ übergibt passenden Kontext; der Agent ruft aktuelle operative Daten über eigene MCP-Tools ab, erklärt Optionen und benötigt Zustimmung vor einer Umbuchung. Nach einer fachlichen Änderung wird die Ansicht aktualisiert.

Der geprüfte Screenshot macht eine zusätzliche Grenze sichtbar: Der initiale Bildschirmzustand erklärt den Klick, gilt aber nicht als maßgeblicher Live-Datensatz. Der Agent soll den aktuellen Stand separat abrufen. Die dargestellten Sendungs-, Zeit- und Geldwerte sind Beispieldaten, keine reale Betriebskennzahl.

OpenAI nennt außerdem IDE-Integrationen von GitHub/JetBrains, Ciscos SDK-Nutzung und einen Thrive-/Crete-Pilot mit `7.000` Steuerfällen und rund einem Drittel weniger Vorbereitungszeit. Das sind referenzierte Herstellerangaben ohne im Artikel offengelegte Vergleichsmethodik; sie begründen keine eigene Leistungszusage.

## Einordnung

Die nützliche Architekturentscheidung ist, Agent-Runtime und Produktverantwortung explizit zu trennen. UI-Auswahl ersetzt dabei weder aktuelle Datenabfrage noch eine fachliche Freigabe. Konfigurierte Sandbox- und Approval-Fähigkeiten sind keine hier geprüfte produktive Sicherheitsgrenze. Die Beispiele helfen bei der Auswahl einer Integrationsfläche, während Benchmark und Pilotzahlen nur in ihrem beschriebenen Kontext gelten. Diese Notiz dokumentiert Wissen und führt keine Integration aus.

## Kernaussagen

- [[Erweiterungs-Ebenen-Zuordnung]]: Runtime, eigene MCP-Dienste und Produktregeln erhalten unterschiedliche Zuständigkeiten.
- [[Freigaben-und-Isolation-getrennt-steuern]]: Fachliche Zustimmung und technische Ausführungsgrenzen getrennt planen.
- [[Klein-und-komposierbar]]: Die kleinste zum benötigten Lifecycle passende Integrationsfläche wählen.

## Verbindungen

- [[Agent-Rechte-umfassen-Kommunikationswege]]
- [[Task-basierte-Steuerung]]
