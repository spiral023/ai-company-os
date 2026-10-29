---
url: keine
autor: Matt Pocock
datum: 2026-10-29
datum_unsicher: true
erfasst: 2026-10-29
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-10-29-matt-pocock-software-factories-real-engineers.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Entscheidungen klären und Agentenarbeit prüfbar machen

Eine gemeinsame Fachsprache, explizite Entscheidungen und überprüfbare Übergaben bilden den Zusammenhang zwischen Planung und Review. Die vom Nutzer Matt Pocock zugeordnete Kurs-Leseausgabe zeigt diese Arbeit an einem Kursprodukt namens Cadence. Analysiert wurden die 38 HTML-Kapitel mit Übungen und Lösungen; die 38 Videos sind lokal archiviert und inventarisiert, aber nicht angesehen oder transkribiert. Das Veröffentlichungsdatum ist unbekannt; das Datum im Dateinamen bezeichnet die Erfassung. Die Herkunft der zusammengestellten HTML-Leseausgabe ist darüber hinaus nicht unabhängig belegt.

## Sprache erklärt Bedeutung, ADRs erklären Entscheidungen

Im Beispiel verdecken unterschiedliche Bezeichnungen denselben Erstattungsprozess. Grilling arbeitet durch konkrete Szenarien heraus, welche Zustände fachlich verschieden sind: Eine Refund Request ist eine Anfrage, die Genehmigung eine Entscheidung und die tatsächliche Auszahlung ein weiterer Vorgang. Die Lösung gleicht Glossar, UI und Code ab. Ein neuer Default migriert dabei bestehende Daten noch nicht.

Das Glossar soll Domänenwissen enthalten, das einem fachkundigen Menschen ohne Produktkenntnis fehlt. Allgemeine Programmierbegriffe, Implementierungsdetails und ausführliche Entscheidungen belasten seinen Zweck. Im Q&A werden mehrere Glossare bei tatsächlich unterschiedlichen Bounded Contexts zugelassen; die Fachverantwortung bleibt beim Menschen. Ein einziges Vokabular für die gesamte Firma ist damit keine pauschale Vorgabe.

ADRs bewahren nicht offensichtliche, schwer umkehrbare Trade-offs. Der Kurs zeigt auch, wie Produktanforderungen oder veraltete Erläuterungen ein ADR-Verzeichnis aufblähen. Der Nutzen liegt im bewahrten Grund, nicht in einem ausgefüllten Formular.

## Erst den Entscheidungsweg klären, dann die Umsetzung planen

Wayfinder hält Destination, offene Decision Tickets, Abhängigkeiten und noch unscharfe Fragen in einer Map fest. Research, Grilling, Prototype und vorbereitende Tasks lösen verschiedene Arten von Unklarheit. Sie sind keine austauschbaren Namen für Implementierungstickets.

Die Notification-Demo verbindet Vendor Research, manuelle Einrichtung und einen Funktionsprototyp. Erst ein konkreter Versuch zeigt Probleme mit Preferences und Integrationsabläufen. Die Map wird mit den Ergebnissen aktualisiert; aus geklärten Entscheidungen folgen Spec und Umsetzungstickets. Die Ausführung benötigt anschließend weiterhin menschliche Zuarbeit und Browser-QA. Eine fertige Map beweist keine fertige Integration.

Für einen winzigen, leicht prüfbaren Diff kann direktes Umsetzen angemessen sein. Normale Unklarheit beginnt mit Grilling; Wayfinder wird relevant, wenn die Klärung mehrere Sessions braucht. Die Wahl hängt vom tatsächlichen Erkenntnisbedarf ab.

## Review liefert Belege und verbessert den nächsten Lauf

Der Kurs unterscheidet deterministische Checks, Agent-Review und menschliches Review. PR-Beschreibungen sollen die Verhaltensänderung erklären, Vorher-Nachher-Belege liefern und Reversibilität sowie Blast Radius benennen. Ein grüner Test ohne passenden Verhaltensnachweis bleibt schwache Evidenz.

Das Code Review trennt Standards und Spec-Erfüllung. Retro untersucht anschließend Sessions und menschliche Kommentare, um fehlende Informationen, Navigation oder Regeln zu finden. Vorschläge werden beurteilt und ausgewählt. Auch Korrekturcommits benötigen einen passenden Reviewpfad.

## Einordnung

Das Material ist eine ausführliche Lehrdemonstration einer Herkunftsfamilie und kein kontrollierter Wirksamkeitsvergleich. Anbieterpreise, Features und konkrete Kommandos gelten zunächst nur für die Kursfassung. Der lokale Skill-Checkout bestätigt zentrale Methoden statisch; er macht die Videos nicht zu ausgewerteten Quellen und belegt keine Erfolgsquote. Gegenüber der Demo bevorzugt der geprüfte Retro-Skill bei mechanischen Verstößen ausdrücklich deterministische Checks. Für dieses Repo sind die Methoden Kandidaten für einen begrenzten Versuch, keine automatisch aktivierten Workflowänderungen.

## Kernaussagen

- Glossar, UI und Code durch fachliche Szenarien zusammenführen → [[CONTEXT-Glossar]]
- Entscheidungsgründe nach klaren Kriterien bewahren → [[ADRs-auf-tragende-Entscheidungen-begrenzen]]
- Ungeklärte Entscheidungen vor Implementierungsslices organisieren → [[Wayfinder-als-Karte-offener-Entscheidungen]]
- Spec, Ausführung und Review mit erkennbaren Übergaben verbinden → [[Plan-first-mit-getrenntem-Review]]
- Prüftiefe anhand Folgen und Reversibilität beurteilen → [[Qualitaetsaufwand-nach-Folgen-und-Abhaengigkeiten-staffeln]]
- Reviewfehler gezielt in Verbesserungen des Agentenumfelds überführen → [[Review-Findings-in-Agent-Verbesserungen-ueberfuehren]]

## Verbindungen

- [[2026-10-08-mattpocockuk-2108216899439894574]]
- [[2026-07-11-mattpocock-wayfinder-to-implementation]]
- [[Softwaregrundlagen-fuer-Agentic-Engineering]]
- [[Matt-Pocock-Software-Factories-Kurstransfer]]

Die [ausführliche Kursanalyse mit Kapitelbelegen](../../reports/2026-10-29-matt-pocock-software-factories-kursanalyse.md) und das [lokale Kursinventar](../../docs/kurse/matt-pocock-software-factories/README.md) ergänzen diese kompakte Source-Notiz.
