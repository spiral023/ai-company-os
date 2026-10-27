# Wissensbasis für die Agentic Software Factory

**Stand:** 2026-10-26. Ziel ist ein gemeinsames, nachvollziehbares Wissensfundament für eine noch nicht auf ein Framework festgelegte Software Factory.

## Einstieg nach Aufgabe

- **Architektur oder nächste Ausbaustufe planen:** [Zielarchitektur und Ausbauplan](agentic-factory-architektur.md).
- **Den späteren Factory-Ablauf konkretisieren:** [erster Entwurf des Kernmodells](factory-kernmodell.md) verbindet eigene Quellen mit den untersuchten Referenzmethoden.
- **Wissen aus eigenen Quellen und externen Repos finden:** [Wissenskatalog bedienen](wissenskatalog.md).
- **Aussagen, Spannungen und Fähigkeitskandidaten gemeinsam abrufen:** [semantischen Pilot nutzen](../../80_Knowledge/Factory/README.md); `python ai.py wissen kontext "<Frage>"` und `python ai.py wissen pilot-check`.
- **Den Bestand erneut als Ganzes beurteilen:** im Katalog einen neuen Analyseplan erzeugen und nach dem [Ablauf für Gesamtanalysen](gesamtanalyse.md) bearbeiten. Ein Analyseplan enthält zunächst ausschließlich offene Arbeit.
- **Verbesserung der Wissensnutzung prüfen:** [fachübergreifende Abnahmefragen](../../60_Evals/Wissensbasis_Factory_Eval.md).
- **Bisherige Wissensprodukte und frühere Entscheidungen nachvollziehen:** [Konzept vom 29.09.2026](konzept.md). Die dortigen Mengen, offenen Punkte und Termine beschreiben den damaligen Stand.

## Bereits umgesetzt

Ein lokaler SQLite-Katalog verbindet die definierten Wissensbereiche dieses Repos, externe Git-Checkouts und die separate AI-LLM-Wiki-Kopie. Er bietet Abschnittssuche, Herkunftsangaben, Inhaltshashes, Commitstände und einen lückenlosen Prüfplan für die indexierten Textpassagen. Die Bedienung erfolgt über `python ai.py wissen`.

Der semantische Pilot ergänzt 24 kuratierte Aussagen, 27 Belegbereiche aus zwölf Herkunftsfamilien, drei Quersynthesen und fünf Fähigkeitskarten. Der direkte Kontextabruf liefert Voraussetzungen und Spannungen mit und sperrt betroffene Aussagen/Kandidaten bei geänderten Belegen. Die Karten sind aus einer gemeinsamen Registry erzeugte Ansichten. [Umfang, Prüfung und Grenzen](../../80_Knowledge/Factory/README.md) sind dort dokumentiert.

[Pilotbericht vom 26.10.2026](../../reports/2026-10-26-factory-semantischer-pilot.md) enthält die konkreten neuen Zusammenhänge, sieben technische Abnahmefragen und den Prüfstand.

## Weitere Ausbaustufen

Die vollständige Bestandsanalyse, ein Vergleich tatsächlicher Agentenantworten und die Anbindung einer Factory-Laufzeit stehen weiter aus. Der Pilot belegt technische Nachvollziehbarkeit und ausgewählte fachliche Verbindungen; praktische Wirkung ist noch nicht gemessen. Ein gefundener externer Skill erhält durch seine Katalogisierung keine Projektfreigabe; dafür bleibt die bestehende Skill-Registry maßgeblich.

Die drei Rechercheberichte belegen die Entwurfsgrundlage:

- [GraphRAG, LightRAG und Property Graph Retrieval](../../reports/2026-10-25-factory-wissensarchitektur-recherche.md)
- [OpenWiki, Graphify, Understand Anything, Claude-Mem und AI-LLM-Wiki](../../reports/2026-10-25-factory-referenzsysteme.md)
- [pstack, gstack, Matt Pocock, GSD und Paperclip](../../reports/2026-10-25-factory-methoden-recherche.md)
