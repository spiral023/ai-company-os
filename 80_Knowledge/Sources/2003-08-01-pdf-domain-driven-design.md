---
titel: "Domain-Driven Design: Fachmodelle, gemeinsame Sprache und kontrollierte Bedeutungsgrenzen"
url: file:///C:/Users/asi/Documents/GitHub/ai-company-os/00_Inbox/Quellen/PDF/lokal/evans/Domain-Driven-Design.pdf
autor: Eric Evans
datum: 2003-08-01
datum_genauigkeit: monat
datum_herkunft: Verlagskatalog, August 2003; Tag 01 ausschließlich Sortierwert
erfasst: 2026-10-29
typ: artikel
rohquelle: 00_Inbox/Quellen/PDF/2003-08-01-pdf-domain-driven-design.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Domain-Driven Design: Fachmodelle, gemeinsame Sprache und kontrollierte Bedeutungsgrenzen

Eric Evans beschreibt Softwareentwicklung für komplexe Fachdomänen als fortlaufendes gemeinsames Lernen. Ein nützliches Modell verbindet Fachwissen, Sprache und ausführbares Verhalten. Die bekannten DDD-Bausteine unterstützen diese Verbindung; sie sind kein Pflichtkatalog für jede Anwendung. (PDF-S. 2–11, 41–42, 313–314.)

## Modell, Sprache und Implementierung

Ein Modell abstrahiert ausgewählte Aspekte einer Domäne für konkrete Aufgaben. Knowledge Crunching verbindet Fachgespräche, Szenarien, Prototypen und Code. Ubiquitous Language umfasst dabei Beziehungen, Regeln und Operationen, die tatsächlich in Gesprächen, Tests und Implementierung verwendet werden. Ein Glossar mit Substantiven allein reicht nicht. (PDF-S. 2–24.)

Model-Driven Design lässt Modell und Implementierung gemeinsam entstehen und sich gegenseitig korrigieren. Vollständige Trennung von Modellierern und bloßen Ausführern schwächt diesen Lernkreislauf. Technische Probleme können fachliche Modellannahmen widerlegen. Dokumente sollen Orientierung und Kommunikation leisten, ohne eine ungenutzte parallele Wahrheit aufzubauen. (PDF-S. 25–35, 305–309.)

## Fachliche Verantwortung und Konsistenz

Die Domäne braucht eine erkennbare Trennung von Oberfläche, Ablaufkoordination und Infrastruktur. Entities drücken fachlich bedeutsame Identität aus, Value Objects austauschbare begriffliche Werte, Domain Services eigenständige fachliche Operationen. Stateless bedeutet keine relevante eigene Instanzhistorie und ist nicht gleichbedeutend mit Nebenwirkungsfreiheit. Module sollen fachliche Zusammenhänge kommunizieren. (PDF-S. 36–69, 320.)

Aggregate begrenzen gemeinsam zu schützende Invarianten und den kontrollierten Änderungszugang über eine Root. Das Preisbeispiel zeigt, warum fachlich passende Werte und Grenzen wichtiger sein können als immer umfassendere Sperrmechanismen. Eine Aggregate-Grenze ist nicht automatisch eine Tabelle, ein Bounded Context oder ein Deployment. Factory und Repository unterscheiden komplexe Erstellung von Zugriff auf vorhandene fachliche Gegenstände. (PDF-S. 70–95.)

## Specifications und veränderbarer Entwurf

Specifications machen Kriterien explizit und können begrifflich Validierung, Auswahl und Erzeugungsbedingungen verbinden. Ihre technischen Umsetzungen dürfen verschieden sein. Ein einfacher regelkonformer Prototyp kann frühe Integration ermöglichen, ohne bereits ein vollständiger Optimierer zu sein. Schnittstellen und Assertions entwickeln sich dabei mit dem Lernen weiter. (PDF-S. 135–146.)

Supple Design verbindet verständliche Schnittstellen, nebenwirkungsfreie Berechnungen, einfache Zustandsänderungen und explizite Vorbedingungen, Nachbedingungen und Invarianten. Fachliche Konturen bestimmen die sinnvolle Granularität. Zusätzliche Abstraktion, allgemeine Rule Engines oder Codegenerierung sind nur nützlich, wenn ihr konkreter Nutzen die Kosten überwiegt. (PDF-S. 147–180.)

Refactoring soll auch neu gewonnene fachliche Einsichten umsetzen. Analysis und Design Patterns liefern Erfahrungswissen samt Konsequenzen; sie werden an den konkreten Zweck angepasst. Eine Strategy oder ein Composite braucht eine tatsächliche fachliche Entsprechung. (PDF-S. 181–204.)

## Grenzen und strategischer Wert

Ein Bounded Context begrenzt die Gültigkeit eines konsistenten Modells. Eine Context Map zeigt die tatsächlichen Modelle und Beziehungen. Continuous Integration integriert sowohl Begriffe als auch Code, Build und Tests. Shared Kernel, Customer/Supplier, Conformist, Anticorruption Layer, Separate Ways, Open Host Service und Published Language beschreiben unterschiedliche Kosten, Kooperation und Modellfreiheit. Eine ACL übersetzt fachliche Bedeutung; ein API-Transport oder Schema allein erfüllt diese Aufgabe nicht. (PDF-S. 205–246.)

Distillation konzentriert starke Fähigkeiten und Lernaufwand auf den besonderen fachlichen Wert des Core Domain. Generic Subdomains brauchen keine maximale Wiederverwendbarkeit. Ein knappes Kerndokument kann vor einem teuren Umbau bereits Orientierung schaffen. Große Strukturen wie Responsibility Layers, Knowledge Level oder Pluggable Component Framework sind optionale, anspruchsvolle Mittel; sie sollen mit Erfahrung evolvieren. (PDF-S. 247–309.)

## Einordnung und Kernaussagen

Die Quelle ist ein argumentiertes Autorenmodell aus Projekterfahrung, vereinfachten und teilweise ausdrücklich fiktiven Beispielen, kein kontrollierter Wirksamkeitsversuch. Technik- und Marktbeispiele stammen aus der damaligen Zeit. Aussagen über heutige KI-Agenten sind eigene Ableitungen; Evans fordert hier keinen heutigen Microservices-, Event-Sourcing- oder CQRS-Methodenkatalog. (PDF-S. 186, 310–314.)

- Ein Modell muss relevante fachliche Entscheidungen ausdrücken.
- Gemeinsame Sprache umfasst Verhalten und Kontext.
- Modell und Code brauchen einen fortlaufenden Rückkanal.
- Konsistenz-, Bedeutungs-, Modul- und Deploymentgrenzen unterscheiden sich.
- Der Kern verdient Priorität; Muster und Plattformen müssen ihren Aufwand rechtfertigen.

## Verbindungen

- [[CONTEXT-Glossar]]: um Beziehungen, Operationen und Geltungsbereich der Begriffe ergänzen.
- [[Fachregel-Konsolidierung-vor-Featureaenderung]]: bestehende Regeln und ihre Verantwortung vor Änderung klären.
- [[Plan-first-mit-getrenntem-Review]]: Implementierungserkenntnisse müssen den Plan revidieren können.
- [[Blockierende-Task-Abhaengigkeiten]]: ein begrenzter funktionierender Ersatz kann frühe Integration ermöglichen.
- [[Schema-als-Vertrag-mit-generierten-Clients]]: strukturellen Vertrag um semantische Übersetzungsregeln ergänzen.

## Quellen- und Abdeckungsnotiz

Die lokale Fassung hat 324 PDF-Seiten; der gesamte vorhandene native Text wurde gelesen. 18 Seiten wurden zusätzlich als Bild angesehen. Das Cover ist bildbasiert; Kapitel 1 folgt auf PDF-Seite 2. Vorspann/Vorwort und regulärer Index fehlen in dieser Datei. Die detaillierte Kapitel- und Bildabdeckung steht in der zugehörigen Analyse. August 2003 ist die bibliografische Monatsangabe; der erste Monatstag ist nur ein Sortierwert. Die technische Vollständigkeit dieser Datei beweist keine Gleichheit mit jeder Verlagsausgabe.


## Vertiefung

Die [ausführliche Buchanalyse](../../reports/buecher/2026-10-29-evans.md) enthält Themenabdeckung, Seitenbelege, Anwendung und Quellenkritik. [[Softwaregrundlagen-fuer-Agentic-Engineering]] ordnet sie neben den drei anderen Büchern ein.

- [[Bounded-Contexts-und-Uebersetzungsgrenzen-kartieren]]
- [[Aggregate-durch-fachliche-Invarianten-begrenzen]]
- [[Vertraege-mit-Vorbedingungen-Nachbedingungen-und-Invarianten]]
