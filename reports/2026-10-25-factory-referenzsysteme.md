# Referenzsysteme für die Wissensbasis der Software Factory

**Stand:** 2026-10-25. **Methode:** statische, lesende Untersuchung von fünf bereits vorhandenen lokalen Analysekopien. Keine Aktualisierung, Installation oder Ausführung fremder Scripts; keine Laufzeit- oder Qualitätsmessung. Die unten verlinkten Commitstände sind die untersuchten Stände, keine Behauptung über den neuesten Upstream-Stand.

## Ergebnis

Die vorhandenen Repos enthalten bereits mehrere Bausteine für Philipps Ziel. Die stärkste Kombination ist: OpenWikis aussagebezogene Provenienz und Aktualitätsprüfung, Understand-Anythings Trennung zwischen deterministischer Struktur und interpretierter Semantik, Graphifys versionierte Extraktions-Caches sowie Claude-Mems gestufter Abruf. Keines der untersuchten Systeme belegt für sich, dass der gesamte heterogene Bestand zuverlässig verstanden oder die Software Factory dadurch besser wird. Das muss ein eigener Eval mit Aufgaben aus diesem Repo zeigen.

| Referenz | Untersuchte Kopie | Lokal beobachtete Lizenzdatei | Integrationsform |
|---|---|---|---|
| langchain-ai/openwiki | `305599f8e44203f9ca6b74bb6b38eebaf0b0405e`, sauber | MIT | Nur Referenz |
| Graphify-Labs/graphify | `92741d162b2094ffc2fed58cfbd8ee823e9da62c`, zwei unversionierte `tests/fixtures/.../obj/`-Verzeichnisse | Apache-2.0; `NOTICE` nennt frühere MIT-Beiträge und `LICENSE-MIT` | Nur Referenz |
| Egonex-AI/Understand-Anything | `e24fcf6d371bcfa529bc110bacb1bb43de1b8d33`, sauber | MIT | Nur Referenz |
| thedotmack/claude-mem | `bab040941390f6c1e82c0508ec806f2fc8255cbb`, sauber | Apache-2.0 | Nur Referenz |
| external_knowledge/ai-llm-wiki | `93d390f0e5f6d74173bf5fd57be2077ca076d354`, sauber | Keine Lizenzdatei im Root vorgefunden | Nur Referenz; keine Freigabe zur Inhaltsübernahme abgeleitet |

„Sauber“ bezieht sich auf `git status --short` zum Untersuchungszeitpunkt. Lizenzangaben beschreiben vorgefundene Dateien und ersetzen keine Prüfung konkreter zu übernehmender Dateien. Es wird hier weder Code noch ein fremder Skill übernommen. Für produktive Übernahme bleiben Repo-Import-Review und Philipps Freigabe erforderlich.

## 1. OpenWiki: Wissen braucht versionierte Belege je Aussage

**Tatsächlich implementiert:** `Claim` besteht aus stabiler ID, atomarer Aussage und mehreren `Evidence`-Einträgen. Ein Beleg hat eine vom Resolver vergebene Ressourcenidentität und einen undurchsichtigen Versionstoken. Der Agent schlägt Ressourcen vor; er vergibt die Belegversion nicht selbst. [Typen, Zeilen 1–164](https://github.com/langchain-ai/openwiki/blob/305599f8e44203f9ca6b74bb6b38eebaf0b0405e/src/claims/core/types.ts#L1-L164).

Der globale Preflight lädt die persistierten Claims, löst ihre Belege auf und unterscheidet `stale` von `unresolved`. Geänderte Belegversionen sind damit auch dann sichtbar, wenn die generierte Wiki-Seite selbst unverändert ist. Allgemeine Auflösungsfehler werden weitergereicht und nicht als gelöschte Quelle interpretiert. [Preflight](https://github.com/langchain-ai/openwiki/blob/305599f8e44203f9ca6b74bb6b38eebaf0b0405e/src/claims/brains/code/preflight.ts#L26-L109).

Der Repository-Resolver unterstützt ganze Dateien und Zeilenbereiche sowie Hash-Anker, um verschobene Quellenbereiche wiederzufinden. [Resolver](https://github.com/langchain-ai/openwiki/blob/305599f8e44203f9ca6b74bb6b38eebaf0b0405e/src/claims/evidence/repository/resolver.ts#L288-L323).

**Abruf:** Wiki-Abschnitte werden lokal über SQLite FTS5/BM25 durchsucht; die Suche gibt kompakte Referenzen zurück, ein separater Read lädt ausgewählte vollständige Abschnitte. Das ist im Retrieval-Modul implementiert und benötigt für den Abruf keine Modellgenerierung. [Retrieval](https://github.com/langchain-ai/openwiki/blob/305599f8e44203f9ca6b74bb6b38eebaf0b0405e/src/retrieval/wiki.ts#L425-L630).

**Heterogene Quellen:** Connector-Typen und Ingestion-Code existieren u. a. für lokale Git-Repos, X, Notion, Google, Slack, Custom MCP und Websuche. Die README grenzt aber ausdrücklich ein: Grounded Claims gelten derzeit für Repository-Wikis mit Repository-Belegen; diese Garantie wird nicht auf Connector-Fakten übertragen. [Connector-Typen](https://github.com/langchain-ai/openwiki/blob/305599f8e44203f9ca6b74bb6b38eebaf0b0405e/src/connectors/types.ts#L1-L62), [README, Grounded Claims und Connectors](https://github.com/langchain-ai/openwiki/blob/305599f8e44203f9ca6b74bb6b38eebaf0b0405e/README.md#grounded-claims).

**Übertragbare Entscheidung:** Für jede tragende Empfehlung im AI-Company-OS Quellenidentität, konkreten Ausschnitt und Fingerprint festhalten. Bei Änderung einer Rohquelle oder eines externen Repos zunächst betroffene Aussagen und Synthesen markieren; erst danach gezielt neu analysieren. Das ist mehr als ein Erstellungsdatum pro Markdown-Datei.

**Grenze:** Eine stabile Belegversion belegt die unveränderte Quelle, nicht automatisch die Wahrheit der Aussage oder die Korrektheit ihrer Interpretation. Globale Aktualitätsprüfung ist noch keine globale inhaltliche Synthese.

## 2. Understand Anything: Struktur zuerst, Semantik als überprüfbare Ergänzung

**Tatsächlich implementiert:** `parse-knowledge-base.py` erkennt eine Wiki-Struktur anhand von Index und Markdown-Bestand, extrahiert Frontmatter, Überschriften und Wikilinks und erstellt einen deterministischen Scan-Manifest. Die Wiki-Wurzel kann das Zielverzeichnis oder dessen `wiki/`-Unterordner sein. [Parser](https://github.com/Egonex-AI/Understand-Anything/blob/e24fcf6d371bcfa529bc110bacb1bb43de1b8d33/understand-anything-plugin/skills/understand-knowledge/parse-knowledge-base.py#L67-L103), [Aufbau des Manifests](https://github.com/Egonex-AI/Understand-Anything/blob/e24fcf6d371bcfa529bc110bacb1bb43de1b8d33/understand-anything-plugin/skills/understand-knowledge/parse-knowledge-base.py#L323-L457).

Der Merge lädt diesen Grundbestand und getrennte Analyse-Batches. Er akzeptiert u. a. `article`, `entity`, `topic`, `claim`, `source` sowie Beziehungen `cites`, `contradicts`, `builds_on`, `exemplifies`. Er normalisiert Typen, führt gleich benannte Entitäten zusammen und verwirft Kanten ohne existierende Endpunkte. [Merge und Typvokabular](https://github.com/Egonex-AI/Understand-Anything/blob/e24fcf6d371bcfa529bc110bacb1bb43de1b8d33/understand-anything-plugin/skills/understand-knowledge/merge-knowledge-graph.py#L55-L217).

**Deklarierter Workflow, nicht von uns ausgeführt:** Der Skill organisiert DETECT → SCAN → ANALYZE → MERGE → SAVE; der semantische Schritt liest Artikel in Batches und soll eingebettete Anweisungen ausdrücklich als untrusted Quelldaten behandeln. [Skill, Phasen und Grenzen](https://github.com/Egonex-AI/Understand-Anything/blob/e24fcf6d371bcfa529bc110bacb1bb43de1b8d33/understand-anything-plugin/skills/understand-knowledge/SKILL.md#L24-L137).

**Übertragbare Entscheidung:** Den bestehenden Markdown-/Wiki-Link-Bestand deterministisch erfassen; interpretierte Entitäten, Widersprüche und Transferregeln als eigene Ableitungen mit Belegen hinzufügen. Den semantischen Graphen nicht mit der Quellstruktur verwechseln.

**Grenzen:** Das Schema unterstützt Widerspruchskanten, beweist aber keine korrekte Widerspruchserkennung. Der Merge setzt fehlende Gewichte auf `0.5` und bildet unbekannte Beziehungstypen auf `related` ab; diese Gewichte sind keine kalibrierte Konfidenz. Rohquellenknoten enthalten laut Skill nur Dateiname und Größe; PDFs und Binärdateien werden in diesem Wiki-Workflow nicht inhaltlich geparst. Die README-Aussage „incremental by default“ für Codeanalyse darf nicht ungeprüft auf eine inkrementelle globale Wissenssynthese übertragen werden.

## 3. Graphify: Graphbeziehungen und Extraktionsstände müssen erklärbar bleiben

**Tatsächlich implementiert:** Markdown-Verweise auf Codesymbole werden nach der Extraktion gegen den Gesamtbestand aufgelöst. Ein eindeutiger pfadqualifizierter Verweis gilt als `EXTRACTED`; ein eindeutig aufgelöster nackter Name als `INFERRED`. Mehrdeutige Namen werden nicht durch willkürliches Tie-Breaking zu Kanten gemacht. [Markdown-Resolver](https://github.com/Graphify-Labs/graphify/blob/92741d162b2094ffc2fed58cfbd8ee823e9da62c/graphify/markdown_resolution.py#L1-L46).

Der Extraktions-Cache berücksichtigt für AST-Ergebnisse Paket-, Schema- und Grammar-Versionen. Für semantische Ergebnisse kann der Extraktionsprompt einen eigenen Fingerprint erhalten, damit eine Promptänderung keine alten Extraktionen stillschweigend wiederverwendet. [Cache](https://github.com/Graphify-Labs/graphify/blob/92741d162b2094ffc2fed58cfbd8ee823e9da62c/graphify/cache.py#L23-L125).

Das Clustering enthält deterministische Community-Labels und Hashes über die sortierte Community-Mitgliedschaft; damit kann eine Ableitung an die tatsächlichen Mitglieder gebunden werden. [Community-Fingerprints](https://github.com/Graphify-Labs/graphify/blob/92741d162b2094ffc2fed58cfbd8ee823e9da62c/graphify/cluster.py#L188-L235).

**Übertragbare Entscheidung:** Im eigenen Wissensgraphen zwischen aus der Quelle extrahierten Links und interpretierten Beziehungen unterscheiden. Neben Quellhash auch Parser-, Schema- und Promptstand speichern. Eine Themenzusammenfassung benötigt einen Fingerprint ihrer Eingangsmenge, sonst ist „aktuell“ nicht überprüfbar.

**Grenzen:** Das Modell ist stark auf Codebeziehungen ausgerichtet. Dokument-/Mediensemantik braucht laut README einen gesonderten Modellschritt; „Code ohne LLM“ ist keine Zusage für X, YouTube oder Prompts. Die prominenten Cloud- und Tokenersparnis-Aussagen werden hier nicht als nachgewiesene Wirkung für unser Repo übernommen. Lokale Community-Erkennung ergibt noch keine fachlich geprüften Software-Factory-Empfehlungen. [README](https://github.com/Graphify-Labs/graphify/blob/92741d162b2094ffc2fed58cfbd8ee823e9da62c/README.md), [Lizenzhinweis](https://github.com/Graphify-Labs/graphify/blob/92741d162b2094ffc2fed58cfbd8ee823e9da62c/NOTICE).

## 4. Claude-Mem: Episodisches Gedächtnis und Wissensbasis erfüllen verschiedene Aufgaben

**Tatsächlich implementiert:** Der progressive Suchvertrag unterscheidet kompakte Indexzeilen von Details und organisiert die Schritte `search`, `timeline`, `fetch`. Er setzt Antwort- und Eingabegrenzen. [Progressive Search](https://github.com/thedotmack/claude-mem/blob/bab040941390f6c1e82c0508ec806f2fc8255cbb/src/shared/progressive-search.ts#L1-L100).

Der Search-Orchestrator wählt bei reinen Filtern SQLite, bei verfügbarer Chroma-Konfiguration semantischen Abruf und bei ausgeschalteter Chroma-Konfiguration SQLite/FTS5. Ein tatsächlich fehlgeschlagener Chroma-Aufruf wird als Fehler weitergereicht; er wird nicht stillschweigend zu einem leeren Suchergebnis. [Search-Orchestrator](https://github.com/thedotmack/claude-mem/blob/bab040941390f6c1e82c0508ec806f2fc8255cbb/src/services/worker/search/SearchOrchestrator.ts#L47-L150).

**Übertragbare Entscheidung:** Agenten erhalten zuerst eine begrenzte Trefferliste, danach benachbarten fachlichen oder zeitlichen Kontext und zuletzt benötigte Volltexte. Erfahrungen aus Factory-Läufen können als eigener Wissensbereich hinzukommen: Aufgabe, eingesetzte Methode/Skill-Version, Ergebnis und beobachtete Fehler.

**Grenzen:** Der Schwerpunkt liegt auf Beobachtungen, Prompts und Sitzungszusammenfassungen. Das ersetzt weder die Kuratierung externer Quellen noch den Vergleich von Frameworks oder die inhaltliche Analyse des Gesamtbestands. Die aktuelle README beschreibt zudem mehrere lokale und gehostete Betriebs-/Providerpfade; aus „Memory“ darf kein pauschal vollständig lokaler Datenfluss abgeleitet werden. [README, Architektur und Suchworkflow](https://github.com/thedotmack/claude-mem/blob/bab040941390f6c1e82c0508ec806f2fc8255cbb/README.md#how-it-works).

## 5. AI-LLM-Wiki: nützliche Syntheseform, kein ausführbares Wissenssystem

**Vorhanden:** Rohmaterial liegt unter `raw/`, verdichtete Notizen unter `wiki/`. Die Agent-Datei beschreibt Entitäten-, Konzept- und Paper-Seiten mit Rohquellenzitaten sowie ein- und ausgehenden Links. Beispiel `concept-advanced-rag.md` verbindet Pre-, Retrieval- und Post-Retrieval-Techniken und nennt den Rohbeleg direkt an Aussagen. Das sind tatsächlich vorhandene Inhaltsstrukturen, keine Laufzeitfunktionen. Lokale Belege: `external_knowledge/ai-llm-wiki/agents.md`, Zeilen 1–96; `external_knowledge/ai-llm-wiki/wiki/concept-advanced-rag.md`, Zeilen 1–41; untersuchter Commit `93d390f0e5f6d74173bf5fd57be2077ca076d354`.

**Übertragbare Entscheidung:** Wiederverwendbare Konzepte und Querverbindungen aus vielen Quellen verdichten; Links gehören zu konkreten Aussagen und zu verwandten Konzepten. Der vorhandene Source-/Pattern-Ansatz im AI-Company-OS ist damit bereits gut vereinbar.

**Grenzen:** Die gelesene Agent-Datei ist eine Arbeitsanweisung an einen Agenten, kein Nachweis eines deterministischen Validators oder Retrieval-Services. Sie enthält außerdem Lösch- sowie automatische Commit-/Push-Regeln, die den Regeln des AI-Company-OS widersprechen und ausdrücklich nicht übernommen werden. Eine Lizenzdatei wurde im Root nicht gefunden; Übernahmerechte sind aus dieser Sichtung nicht geklärt.

## Konsequenzen für die eigene Architektur

1. **Vollständiger Katalog vor globaler Interpretation:** Rohquellen, Source-Notizen, Patterns, externe Repo-Dateien, Skills und Prompts erhalten eindeutige IDs, Hashes und Herkunftsangaben. Im Bericht muss sichtbar sein, welcher Anteil erfasst und welcher nur katalogisiert ist.
2. **Mehrere Wissensebenen:** Quelldaten → extrahierte Aussagen/Fähigkeiten → geprüfte Beziehungen → thematische Synthesen → Factory-Entscheidungen. Jeder Übergang bleibt nachvollziehbar.
3. **Eigener globaler Analysemodus:** Alle Themen- und Repo-Synthesen werden gemeinsam auf Ergänzungen, Spannungen, veränderte Empfehlungen und Lücken geprüft. Bei unzureichender Abdeckung werden konkrete Originale nachgeladen. Eine Graphansicht oder die Top-10 einer Suche genügt dafür nicht.
4. **Änderungen wirken entlang von Abhängigkeiten:** Dateihash, Repo-Commit und Extraktionsversion bestimmen, welche Aussagen und Synthesen erneut geprüft werden müssen. Historische Quellen bleiben erhalten; veraltete Ableitungen werden markiert.
5. **Wissen von ausführbaren Fähigkeiten trennen:** Ein gefundenes `SKILL.md` oder ein Prompt ist zunächst ein analysiertes Artefakt. Nutzung als Anweisung erfordert getrennte Herkunfts-, Lizenz-, Inhalts- und Freigabeprüfung.
6. **Erst Wirkung messen, dann Infrastruktur ausbauen:** Mit fachübergreifenden Factory-Fragen prüfen, ob der Agent passende Belege, Gegenargumente, eigene Entscheidungen und eine begründete Methodenauswahl liefert. Eine Graphdatenbank, ein zweites Wiki oder ein Memory-Daemon ist aus den untersuchten Quellen allein noch nicht gerechtfertigt.

## Prüfung und offene Grenzen

Geprüft wurden lokale HEADs, Dirty-Status, Root-Lizenzdateien und gezielt relevante README-/Implementierungsabschnitte. Fremder Code wurde nicht ausgeführt. Die verlinkten Implementierungen belegen Mechanismen; sie belegen keine Qualitätssteigerung für Philipps Bestand. Kein vollständiger Security-Audit, keine Produktionsfreigabe, keine Bewertung sämtlicher Dateien dieser Repos. Repo-weite Validatoren wurden für diese reine Referenzrecherche nicht gestartet.
