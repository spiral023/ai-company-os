---
url: https://claude.com/de/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
autor: Claude
datum: 2026-10-22
erfasst: 2026-10-24
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-10-22-claude-building-agents-when-to-fold-subagents-into-your.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Subagents anhand von Kontextgrenzen und Ende-zu-Ende-Evals zusammenlegen

Anthropics Artikel berichtet Erfahrungen aus Enterprise-Agenten und empfiehlt, geeignete Spezialisten schrittweise in einen gemeinsamen Agent-Loop zu überführen. Die Belastbarkeit bleibt begrenzt: Vergleichsdaten, Stichprobengrößen und vollständige Eval-Sets fehlen. Ein einzelner Kunde habe ungefähr doppelte Geschwindigkeit erreicht; das ist ein berichteter Einzelfall, keine übertragbare Benchmark. Die Rohmetadaten nennen „Claude“, der Artikel selbst Diane Sarkis.

## Nach Kontext statt Organigramm aufteilen

Ein Agent pro Team oder Problemtyp führt laut Artikel häufig zu überlappenden Spezialisten, widersprüchlichen Prompts, lokal optimierten Evals und verlustbehafteten Übergaben. Wenn zwei Spezialisten dieselben Daten verwenden oder regelmäßig aufeinander folgen, sind sie Kandidaten für eine Zusammenlegung.

Subagents bleiben sinnvoll bei messbarer Verschlechterung durch Kontextfülle, unabhängiger Parallelität, Problemen mit Werkzeugwahl oder kollidierenden Instruktionen. Geeignete Grenzen brauchen wenig Wissen aus dem restlichen System und liefern kompakte Resultate, etwa unabhängige Recherche oder Black-Box-Verifikation.

![Aufteilung nach Problemtyp verliert Kontext; Aufteilung nach Kontext hält Implementierung und Testentwurf zusammen.](../../00_Inbox/Quellen/URL/medien/2026-10-22-claude-building-agents-when-to-fold-subagents-into-your/02-bild.png)

Die Grafik verdeutlicht den Unterschied: Feature und zugehörige Tests entstehen im selben Kontext; ein separater Verifier führt Tests aus und berichtet Ergebnisse. Sie illustriert die Empfehlung, misst aber keinen Qualitätsgewinn.

## Progressive Disclosure im gemeinsamen Loop

Der vorgeschlagene Loop hält Planung, Ausführung und Rohresultate im selben Kontext. Werkzeuge können parallel laufen; das Modell entscheidet anschließend über weitere Arbeit. Skills laden Verfahren und Regeln bei Bedarf, Tool Search lädt Werkzeugdefinitionen bedarfsabhängig. Referenzwissen liegt hinter Suchwerkzeugen oder in Skill-Referenzen.

Harte Grenzen wie Budget, Validierung und Freigaben bleiben im Harness beziehungsweise in Werkzeugen. Mechanische Schritte können weiterhin Code übernehmen. Die berichtete Kürzung des `Claude Code`-Systemprompts um über 80 Prozent betraf auch Progressive Disclosure; der Artikel isoliert dessen Anteil nicht. Modellbezogene Begründungen sind zeitgebundene Herstelleraussagen und kein Beweis, dass eine konkrete Architektur überflüssig ist.

## Migration als überprüfbares Experiment

1. Ein gemeinsames Ende-zu-Ende-Eval aufbauen; zehn gute Beispiele nennt der Artikel als möglichen Start.
2. Jede produktiv genutzte Agentenkette und jede unverletzliche Regel abdecken; Aufgaben mehrfach ausführen.
3. Jeweils einen Subagenten zusammenlegen oder seine Instruktionen in Skills und API-Aufrufe in Tools überführen.
4. Einzelne Aufgabenwechsel zwischen bestanden und fehlgeschlagen prüfen, zusätzlich zu Gesamtqualität, Kosten und Latenz.

Im berichteten Support-Beispiel sank die Latenz, zugleich wurde ein Liefertermin ohne den vorgesehenen Spezialisten beantwortet. Der Fehler zeigte sich nur in einem von zwei Läufen. Das begründet wiederholte Tests und Fallanalyse statt alleiniger Durchschnittsnoten.

Subagents zunächst als Tools aufzurufen ist ein Zwischenschritt: Der Hauptagent behält die Unterhaltung und kann ein gemeinsames Antwortschema nutzen. Eigene Kontexte, verlustbehaftete Zusammenfassungen und verschachtelte Laufzeit bleiben bestehen. Ein kleines zentrales Team soll Systemprompt und Gesamtqualität verantworten; Fachteams pflegen Skills, Tools und lokale Evals.

## Einordnung

[[2026-04-07-claude-how-and-when-to-use-subagents-in-claude-code]] betont Isolation und unabhängige Arbeit, während Oktober Kontext- und Latenzkosten stärker gewichtet. Beide erlauben Subagents dort, wo Kontextgrenzen tatsächlich trennbar sind. Der neue Schwerpunkt ist eine evalgestützte Entscheidung zwischen isoliertem Spezialisten und bedarfsabhängig geladenem Wissen im gemeinsamen Loop. Die beworbenen Migrationswerkzeuge sind Hilfsangebote des Herstellers, keine unabhängige Validierung der Empfehlung.

## Kernaussagen

- Gekoppelte Arbeit nach gemeinsamem Kontext zusammenführen.
- Progressive Disclosure kann Spezialisten ersetzen, ohne alles vorab zu laden.
- Einzelne Regressionen und wiederholte Läufe entscheiden mit über die Architektur.
- Parallelität und begrenzte Verifikation bleiben sinnvolle Subagent-Einsätze.

## Verbindungen

- [[Kontrollierte-Agent-Parallelisierung]] — ergänzt Kontextgrenzen und überprüfbare Gründe für separate Agenten.
- [[Kontext-Hygiene-Entscheidungsbaum]] — setzt Kontextentlastung gegen Informationsverluste beim Auslagern.
- [[Erweiterungs-Ebenen-Zuordnung]] — überführt Spezialistenwissen in Skills und Aktionen in Tools.
