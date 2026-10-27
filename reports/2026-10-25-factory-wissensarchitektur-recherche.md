# Wissensarchitektur für die Agentic Software Factory

**Stand:** 25.10.2026 · **Status:** Recherche und Architekturvorschlag; keine Installation oder Integrationsentscheidung

Untersucht wurden offizielle Dokumentation und Quellcode von Microsoft GraphRAG, HKUDS/LightRAG und LlamaIndex. Die Mechanismen wurden gelesen, jedoch nicht mit Philipps Daten ausgeführt. Aussagen der Projekte über Qualität und Geschwindigkeit sind keine hier gemessenen Ergebnisse.

## Ergebnis

Das Ziel braucht zwei getrennte Fähigkeiten: einen belegbaren Zugriff auf passende Details während einer Aufgabe und eine wiederholbare Synthese über den gesamten erfassten Bestand. Ein Vektorindex allein bildet die zweite Fähigkeit nicht ab. Ein Knowledge Graph allein garantiert ebenfalls weder vollständige Erfassung noch korrekte Schlussfolgerungen. Als Entwurf empfiehlt sich eine gemeinsame, versionierte Quellenbasis mit mehreren abgeleiteten Such- und Syntheseansichten.

## Vergleich der Primärquellen

| Ansatz | Nachgelesener Mechanismus | Für dieses Repo übertragbar | Grenze |
|---|---|---|---|
| Microsoft GraphRAG | Globale Fragen werden über hierarchische Community Reports beantwortet; lokale Fragen über Entitäten, Nachbarn und Originaltext | Mehrstufige Synthesen vom einzelnen Beleg bis zur Gesamtsicht | Generierte Reports sind Verdichtungen; sie ersetzen keine Vollständigkeitsprüfung |
| GraphRAG DRIFT | Breiter Einstieg über Community Reports, daraus Folgefragen und lokale Vertiefung | Eine Analyse kann andere Themen entdecken, als die anfängliche Suchfrage vermuten ließ | Mehr Such- und Generierungsschritte brauchen begrenzte Budgets und Abbruchkriterien |
| HKUDS/LightRAG | Gemeinsames Retrieval aus Graph, Vektoren und Text-Chunks; getrennte Dokumentzustände und Caches | Kontextdaten unabhängig von der Antwort abrufen; inkrementelle Pflege | Der Modusname `global` bedeutet keine nachgewiesene Gesamtbestandsanalyse |
| LlamaIndex Property Graph | Schemafähige Extraktion und kombinierbare Retriever für Graphpfade und Quelltext | Wenige fachlich definierte Relationstypen und kontrollierte Kontexterweiterung | Ein eingehaltenes Schema beweist keine inhaltlich richtige Beziehung |

Die Tabelle verdichtet die nachfolgenden Einzelbefunde; die Empfehlung ist eine eigene Ableitung.

## GraphRAG: Gesamtsicht und Detailzugriff unterscheiden

Global Search verwendet generierte Community Reports einer gewählten Hierarchieebene. Ein Map-Schritt erzeugt bewertete Teilantworten; ein Reduce-Schritt verdichtet ausgewählte Punkte. Detailliertere Ebenen können mehr Reports und Modellarbeit benötigen. Das ist ein brauchbares Vorbild für eine Synthesehierarchie: Quellenbefunde → Teilthemen → übergreifende Erkenntnisse → Factory-Empfehlungen. Dass ein Report auf dieser Hierarchie liegt, beweist allerdings nicht, dass jede wichtige Aussage einer Quelle erhalten blieb. [Offizielle Global-Search-Dokumentation](https://microsoft.github.io/graphrag/query/global_search/)

Local Search kombiniert Entitäten und Beziehungen mit den zugeordneten Originaltexten und priorisiert diese innerhalb eines Kontextbudgets. Für eine konkrete Entwicklungsaufgabe sollten deshalb sowohl ausgewählte Regeln und Skills als auch ihre Herkunft und Grenzen abrufbar bleiben. [Offizielle Local-Search-Dokumentation](https://microsoft.github.io/graphrag/query/local_search/)

DRIFT erweitert den Einstieg durch Community-Informationen und erzeugt Folgefragen zur lokalen Vertiefung. Übertragbar ist die kontrollierte Erweiterung einer Recherche: von einer UI-Frage etwa zu Abnahmeverfahren, Grenzen autonomer Änderungen und passenden Review-Skills. Dies ist eine Analogie für die Factory, keine dokumentierte Leistung mit diesem Repo. [Offizielle DRIFT-Beschreibung](https://github.com/microsoft/graphrag/blob/c600ff80b77b9b62c47d539a3ac9569e95d8949b/docs/query/drift_search.md)

Die Ausgabetabellen besitzen IDs und Verbindungen zwischen Text Units, Communities und Reports. Die Factory sollte entsprechend jede Synthese mit ihren Eingaben verbinden, statt nur den fertigen Fließtext abzulegen. [GraphRAG-Ausgabeschema](https://microsoft.github.io/graphrag/index/outputs/)

**Aktuelle Produktgrenze:** Das offizielle README erklärt das Projekt inzwischen als weitgehend im Maintenance-Modus; neue Features und PRs sind nicht vorgesehen. Es bezeichnet die Implementierung als Forschungsdemonstration und warnt vor teurer Indexierung. GraphRAG ist deshalb eine wichtige Architekturquelle, aber ohne Pilotvergleich keine begründete Festlegung als Kernplattform. [README am geprüften Commit](https://github.com/microsoft/graphrag/blob/c600ff80b77b9b62c47d539a3ac9569e95d8949b/README.md)

## Inkrementelle Verarbeitung braucht eigene Aktualitätsregeln

Die aktuelle GraphRAG-CLI führt Update-Methoden als `standard-update` und `fast-update`. Ältere Beispiele mit `graphrag update` sollten daher nicht ungeprüft als aktuelle Schnittstelle übernommen werden. [CLI-Referenz](https://microsoft.github.io/graphrag/cli/)

Der gelesene Delta-Detektor vergleicht Dokumenttitel und erkennt daraus neue sowie fehlende Dokumente. Eine Inhaltsänderung bei unverändertem Titel wird an dieser Stelle nicht als neuer Eingang erkannt. Die Aussage bezieht sich genau auf diesen Codepfad, nicht auf einen vollständigen Laufzeittest aller Update-Wege. Für die Factory folgt daraus eine eigene Anforderung: Dateipfad oder Titel reichen nicht als Version; nötig sind Inhalts-Hash und bei Repos Commit plus Dateiversion. [Delta-Detektor am geprüften Commit](https://github.com/microsoft/graphrag/blob/c600ff80b77b9b62c47d539a3ac9569e95d8949b/packages/graphrag/graphrag/index/update/incremental_index.py)

Standard GraphRAG nutzt LLMs unter anderem für Entitäten, Beziehungen und Reports. FastGraphRAG ersetzt Teile der Extraktion durch NLP und Ko-Vorkommen. Die Dokumentation beschreibt einen Kosten-/Detailtrade-off; die Standard-NLP-Konfiguration ist hauptsächlich für Englisch ausgelegt. Ein gemischt deutsch-englischer Bestand mit Code, Prompts und Transkripten braucht einen eigenen Pilotvergleich. [Indexierungsmethoden](https://microsoft.github.io/graphrag/index/methods/)

## LightRAG: Abrufdaten, Budgets und Quellenpflege

Im Quellcode bezeichnet `local` ein entitätenorientiertes, `global` ein beziehungsorientiertes Retrieval; `hybrid` kombiniert diese, `mix` ergänzt Graph- und Vektorabruf. Die Optionen enthalten getrennte Budgets für Entitäten, Beziehungen und Gesamtkontext sowie reine Kontextausgabe und Referenzlisten. Diese Unterschiede sind wichtiger als der Name „global“: Eine Top-k-Auswahl über Beziehungen ist kein Beleg dafür, dass alle Dokumente geprüft wurden. [QueryParam am geprüften Commit](https://github.com/HKUDS/LightRAG/blob/aaebfe1bb8d55deb6a4304d357a3bf4c92fcd40a/lightrag/base.py)

`aquery_data` gibt strukturierte Retrieval-Ergebnisse ohne abschließende LLM-Antwort zurück. Der Code enthält außerdem dokumentbezogene Entfernung und Verfahren für betroffene Graphbeiträge. Für die Factory ist die Trennung hilfreich: Der Wissensdienst liefert Fundstellen und Kontext; der ausführende Agent übernimmt die aufgabenbezogene Schlussfolgerung. Das Vorhandensein dieser Methoden ist durch Quellcode belegt, ihre Zuverlässigkeit im eigenen Betrieb wurde nicht geprüft. [Core-Implementierung am geprüften Commit](https://github.com/HKUDS/LightRAG/blob/aaebfe1bb8d55deb6a4304d357a3bf4c92fcd40a/lightrag/lightrag.py)

LightRAG trennt KV-, Vektor-, Graph- und Dokumentstatusspeicher. Die Standardvarianten halten den Bestand im Prozessspeicher und persistieren lokal; die Dokumentation begrenzt diese auf kleine Tests. Für ein dauerhaft wachsendes Factory-System wäre die Speicherauswahl somit ein eigener Betriebsschritt. Caches können wiederholte Extraktionen vermeiden, ersetzen aber kein korrektes Invalidierungsverfahren. [Offizielle Core-Dokumentation](https://github.com/HKUDS/LightRAG/blob/aaebfe1bb8d55deb6a4304d357a3bf4c92fcd40a/docs/ProgramingWithCore.md)

Die Datei-Pipeline beschreibt Zwischenartefakte mit Block-, Abschnitts- und Medieninformationen sowie separate Verarbeitungszustände. Ihr Dokumentationskopf verweist auf eine v1.5-/Development-Linie; Verfügbarkeit und gewählte Version müssen deshalb vor Nutzung abgeglichen werden. Übertragbar ist das Datenmodell: Transkriptsegment, Bild, Tabelle und Volltext benötigen einen gemeinsamen Quellenanker und einen sichtbaren Verarbeitungsstatus. [Offizielle Pipeline-Spezifikation](https://github.com/HKUDS/LightRAG/blob/aaebfe1bb8d55deb6a4304d357a3bf4c92fcd40a/docs/FileProcessingPipeline.md)

Die README-Aussagen über höhere Qualität und niedrigere Kosten wurden nicht als allgemeine Tatsachen übernommen. Dafür fehlen vergleichbare Messungen mit Philipps Bestand, Aufgaben und Modellen. [Projekt-README](https://github.com/HKUDS/LightRAG/blob/aaebfe1bb8d55deb6a4304d357a3bf4c92fcd40a/README.md)

## LlamaIndex: Kontrollierte Beziehungen statt beliebiger Graphgröße

Der Property Graph Index erlaubt Extraktoren mit einem strikten Schema für Entitäts- und Beziehungstypen. Er kann vorhandene Beziehungen ohne LLM lesen und mehrere Retriever kombinieren; bei Vektorabruf lässt sich die Pfadtiefe begrenzen und Quelltext ergänzen. Für dieses Repo passen fachliche Typen wie `belegt`, `setzt_voraus`, `steht_in_spannung_zu`, `implementiert` und `evaluiert_durch`. Solche Typen müssten im eigenen Datenmodell definiert und fachlich geprüft werden. Die Dokumentation bietet außerdem eingeschränkte Cypher-Vorlagen; frei generierte Datenbankabfragen brauchen eine gesonderte Ausführungsgrenze. [Offizielle Property-Graph-Dokumentation](https://developers.llamaindex.ai/python/framework/module_guides/indexing/lpg_index_guide/)

## Empfohlener Entwurf für die Factory

Die folgenden Punkte sind ein Vorschlag aus der Recherche, keine bereits vorhandenen Funktionen:

1. **Reproduzierbares Inventar:** Rohquellen, Source-Notizen, Patterns, Entscheidungen und externe Repo-Dateien erhalten stabile IDs. Je Repo werden Commit, Dirty-Status und Dateihashes erfasst. Medien und Transkripte bleiben derselben Quelle zugeordnet. Fehlende oder gescheiterte Eingänge bleiben sichtbar.
2. **Getrennte Inhaltsarten:** Eine externe Anweisung bleibt ein untersuchter Prompt oder Skill. Sie wird durch Aufnahme in den Index nicht zur geltenden Factory-Regel. Eigene Entscheidungen, fremde Aussagen, Erfahrungsberichte und getestete Verfahren bleiben unterscheidbar.
3. **Aussagen mit Herkunft:** Eine Erkenntnis referenziert konkrete Abschnitte oder Zeitsegmente, Anwendungsbedingungen und Gegenbelege. Mehrere Weiterveröffentlichungen derselben Ursprungsquelle zählen nicht automatisch als unabhängige Bestätigung.
4. **Mehrere Suchwege:** Exakte Textsuche für Identifier und Promptteile, semantische Suche für anders formulierte Fragen und begrenzte Graphnachbarschaft für Voraussetzungen und Spannungen. Die Kombination wird anhand echter Aufgaben bewertet.
5. **Gesamtsynthese als eigener Lauf:** Ein Manifest legt den gesamten betrachteten Snapshot fest. Jedes eingeschlossene Objekt erhält einen Bearbeitungsstatus. Teilanalysen werden entlang mehrerer Perspektiven verdichtet: Entwicklungsphase, Fähigkeit, Kosten, Qualität, Autonomie und offene Konflikte. Ein Abschlussbericht nennt Abdeckung, Auslassungen und neue Hypothesen. Ein Top-k-Ergebnis darf nicht als Vollanalyse ausgegeben werden.
6. **Abhängige Artefakte gezielt erneuern:** Geänderte Quelle → betroffene Aussagen → betroffene Synthesen → betroffene Factory-Profile. Abgeleitete Artefakte speichern Eingabehashes, Modell-/Promptversion und Erzeugungszeit. Das schafft die Grundlage für inkrementelle Wiederholung, ohne vollständige Wiederholung auszuschließen.
7. **Factory-Pakete getrennt freigeben:** Aus Synthesen entstehen Vorschläge für Rollen, Skills, Prompts und Prüfverfahren. Erst ein Vergleichslauf rechtfertigt die Übernahme in ein aktives Factory-Profil. Recherche und laufende Wissenspflege dürfen bestehende Arbeitsregeln nicht stillschweigend ersetzen.

Als ersten technischen Schritt empfiehlt sich ein frameworkunabhängiges Inventar mit Fundstellen und Aktualitätsdaten. Anschließend sollten eine Gesamtanalyse und ein aufgabenbezogener Abruf denselben Snapshot nutzen. GraphRAG-ähnliche Synthese und LightRAG-/Property-Graph-ähnliches Retrieval können darauf als austauschbare Verfahren erprobt werden. Eine sofortige Festlegung auf drei vollständige Frameworks würde zusätzliche Pflege erzeugen, ohne ihren Nutzen zu belegen.

## Pilot und Abnahme

Ein gemeinsamer Prüfsatz sollte konkrete Datei-/Promptfragen, mehrere Quellen verbindende Entscheidungen, widersprüchliche Empfehlungen und echte Gesamtfragen enthalten. Beispiel: „Welche zusammenhängenden Verfahren aus unseren Quellen und Repo-Skills können Planung, Umsetzung und Abnahme einer neuen SaaS-Funktion verbessern, und welche davon sind schon durch eigene Tests belegt?“

Zu messen sind Fundstellenabdeckung, korrekte Herkunft, erkannte Gegenbelege, Aktualität nach einer geänderten Repo-Datei, Nutzen des vorgeschlagenen Arbeitsablaufs sowie Laufzeit und Modellaufwand. Ein gezielt übersehener, aber entscheidungsrelevanter Gegenbeleg ist ein aussagekräftigerer Test als nur eine gut klingende Zusammenfassung. Ein Vollanalyse-Test muss zusätzlich bestätigen, dass kein Eingang unbemerkt ausgelassen wurde.

## Geprüfte Repository-Stände

Die folgenden HEAD-Werte wurden am 25.10.2026 über die GitHub-API gelesen. Dokumentationsseiten können unabhängig davon fortgeschrieben werden; entscheidende Codebelege sind oben an den jeweiligen Commit gebunden.

| Repository | HEAD | Commitdatum UTC | Rolle in dieser Recherche |
|---|---|---|---|
| `microsoft/graphrag` | `c600ff80b77b9b62c47d539a3ac9569e95d8949b` | 20.10.2026 | Global-/Local-/DRIFT-Architektur und Delta-Erkennung |
| `HKUDS/LightRAG` | `aaebfe1bb8d55deb6a4304d357a3bf4c92fcd40a` | 14.10.2026 | Query-Vertrag, Kontextdaten, Status und Quellenpflege |
| `run-llama/llama_index` | `619d74664e8404612038bc15a1a40c686037277c` | 14.10.2026 | Stand erfasst; Property-Graph-Funktionen anhand offizieller Dokumentation gelesen |

Es wurden keine externen Scripts ausgeführt, keine Abhängigkeiten installiert und keine produktive Übernahme vorgenommen.
