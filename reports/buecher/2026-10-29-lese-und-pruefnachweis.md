# Vier Softwarebücher: Leseumfang, Herkunft und Verarbeitung

**Stand:** 2026-10-29

Die Auswertung umfasst den gesamten vorhandenen Seitentext der vier bereitgestellten PDF-Dateien: **1.267 PDF-Seiten**, darunter 1.254 Seiten mit mindestens einem extrahierten Zeichen. Die übrigen Seiten enthalten beispielsweise reine Bilder oder sind leer. Zusätzlich wurden **83 ausgewählte Seiten tatsächlich gerendert und angesehen**. Textlektüre und visuelle Sichtprüfung werden getrennt ausgewiesen. Eine vollständige visuelle Prüfung jeder Seite oder eine Wiederherstellung fehlender Originalabbildungen wird nicht behauptet.

Der inhaltliche Einstieg ist [[Softwaregrundlagen-fuer-Agentic-Engineering]]. Die vier ausführlichen Buchanalysen behandeln sämtliche vorhandenen Hauptkapitel beziehungsweise Topics und enthalten Seitenbelege, eigene Anwendungsvorschläge, Bestandsbezüge und Quellenkritik.

Die vier Buchanalysen umfassen zusammen rund **21.700 Wörter**, die gemeinsame Synthese weitere **3.850 Wörter**. Zusätzlich stehen knappe Source-Notizen und die Pattern-Ergänzungen bereit. Die internen Belegregister enthalten **228 Aussagen**: 52 zu Ousterhout, 64 zu Evans, 52 zu Osmani und 60 zu Pragmatic. Kennungen, Pflichtfelder und gültige PDF-Seitenbereiche wurden zentral geprüft; jeder Datensatz trennt Buchaussage, Mechanismus, Bedingungen, Grenzen und eigene Übertragung.

## Umfang je Datei

| Buch | PDF-Seiten | Seiten mit Text | Vollständig gelesener Textbereich | Tatsächlich betrachtete Seitenbilder | Themenabdeckung |
|---|---:|---:|---|---:|---|
| [Ousterhout](2026-10-29-ousterhout.md) | 191 | 190 | 1–191 | 20 | Alle 22 Kapitel, Vorwerk, Index und Zusammenfassungen |
| [Evans](2026-10-29-evans.md) | 324 | 323 | 1–324; Cover zusätzlich als Bild | 18 | Alle 17 Kapitel, Schluss, Pattern-Anhang, Glossar und Nachweise der vorhandenen Datei |
| [Osmani](2026-10-29-osmani.md) | 255 | 246 | 1–255 | 19 | Alle elf Kapitel, Vorwerk, Register und Schluss |
| [Thomas und Hunt](2026-10-29-pragmatic.md) | 497 | 495 | 1–497, arbeitsteilig 1–235 und 236–497 | 26 | Alle 53 Topics, Kapiteleinführungen, Vor-/Nachspann, Literatur und sämtliche Übungslösungen |
| **Summe** | **1.267** | **1.254** | **Keine offene Textstrecke** | **83** | **Abdeckungstabellen stehen in den Einzelanalysen** |

„Seite mit Text“ bedeutet hier mindestens ein Zeichen, nicht eine Mindestlänge. Dadurch unterscheidet sich diese Zahl von einem Inventar, das sehr kurze Seiten ausfiltert. Die Extraktion enthält insgesamt 2.385.461 Zeichen. Diese Umfangszahlen sind ein technischer Nachweis, keine Qualitätsmetrik für die Interpretation.

## Identität und bibliografische Präzision

| Buch | Lokale kanonische Datei | SHA-256 der bereitgestellten Originaldatei und ihrer lokalen Kopie |
|---|---|---|
| Ousterhout | [PDF](../../00_Inbox/Quellen/PDF/lokal/ousterhout/A-Philosophy-of-Software-Design-2nd-Edition.pdf) | `b66f0968468446df5c47dc26bbf2e5a41fad82ea4f02bb0cada461deb915429b` |
| Evans | [PDF](../../00_Inbox/Quellen/PDF/lokal/evans/Domain-Driven-Design.pdf) | `929eed35e94a268a36d7e807aab79ad11f413a6fde3afcdb6bce07abb0c6c740` |
| Osmani | [PDF](../../00_Inbox/Quellen/PDF/lokal/osmani/Beyond-Vibe-Coding.pdf) | `cb63499630c2f0f7ace300de68b952f9f87c1cb238168ed6bb5e3103bcfabeb2` |
| Thomas und Hunt | [PDF](../../00_Inbox/Quellen/PDF/lokal/the-pragmatic-programmer-20th-anniversary-edition/The-Pragmatic-Programmer-20th-Anniversary-Edition.pdf) | `3930d0e9bd47c2cc1da2ea44c82bafe0003e23f7187bde195c3585d541f097e3` |

Die Originale wurden nicht überschrieben. Ihre Hashes und die kanonischen Kopien wurden zentral erneut verglichen. Auch die 1.267 extrahierten Seitentexte stimmen mit ihren gespeicherten Texthashes überein. Deren Definition ist UTF-8 der extrahierten Zeichenfolge mit LF; die beim lokalen Windows-Schreiben entstandenen CRLF werden für diesen Textvergleich normalisiert. Das ist von einem Bytehash der PDF zu unterscheiden.

- **Ousterhout:** Zweite Auflage, Juli 2021 laut Impressum; der bibliografische Tageswert `2021-07-01` ist ausdrücklich nur ein Sortierwert mit Monatsgenauigkeit. Die [Autorseite](https://web.stanford.edu/~ouster/cgi-bin/book.php) dient als ergänzende Editionsreferenz.
- **Evans:** August 2003; `2003-08-01` ist ebenfalls Monatssortierwert. Verlagskataloge unterscheiden je nach Format genaue Tagesangaben. Die lokale Datei besitzt keinen vollständigen Impressumsapparat; der [Verlagskatalog](https://www.oreilly.com/library/view/domain-driven-design-tackling/0321125215/toc.html) ergänzt die bibliografische Zuordnung.
- **Osmani:** Erstausgabe vom 18.08.2025 laut Impressum auf PDF-S. 4. Das technische PDF-Erstellungsdatum 15.08. ist kein Ersatz für das Veröffentlichungsdatum.
- **Thomas und Hunt:** Die vorliegende Datei nennt auf PDF-S. 2 Version P1.0 vom 13.09.2019. Das Copyrightjahr 2020 bezeichnet etwas anderes. Ihre Identität mit dem bereits am 28.10.2026 verarbeiteten Exemplar wurde bestätigt.

Die Seitenbelege sämtlicher Analysen verwenden die PDF-Zählung ab der ersten Dateiseite. Sie sind nicht als gedruckte Seitenzahlen anderer Ausgaben zu verwenden.

## Tatsächlich angesehene Bilder

| Buch | PDF-Seiten |
|---|---|
| Ousterhout | 2, 18, 20, 27, 30, 34, 64, 68, 84, 95, 96, 119, 165, 173, 175, 176, 177, 188, 189, 190 |
| Evans | 1, 19, 73, 78, 137, 143, 158, 170, 207, 215, 228, 241, 255, 267, 282, 291, 294, 302 |
| Osmani | 18, 21, 36, 54, 58, 61, 63, 65, 66, 84, 87, 116, 119, 127, 133, 158, 196, 206, 231 |
| Thomas und Hunt | 1, 2, 69, 95, 112, 134, 241, 242, 243, 257, 295, 318, 344, 346, 347, 350, 364, 365, 366, 373, 383, 420, 457, 458, 494, 497 |

Ousterhouts Auswahl umfasst unter anderem Editionsangabe, Komplexitätsformel, qualitative Kurve, Deep Modules, Schichten, Fehlerhandler, Buffer-Performance und die zusammenfassenden Prinzipien. Die OCR/ClearScan-Schicht hat erkennbare Fehler. Kritische verwendete Aussagen wurden deshalb gezielt gegen Seitenbilder geprüft; eine buchstabengetreue Neuübertragung aller Codebeispiele wurde nicht erstellt.

Bei Evans wurden fachlich wichtige Diagramme und Tabellen ausgewählt: gemeinsame Sprache, Aggregate, Specifications, Assertions, Kontextbeziehungen, ACL, Core Domain und große Strukturen. Die Datei beginnt nach dem bildbasierten Cover unmittelbar mit Kapitel 1. Vorwort, reguläres Inhaltsverzeichnis und normaler Stichwortindex fehlen. Das ist eine Grenze der bereitgestellten Fassung; ihre Textlektüre ist kein Nachweis, dass sie jede Seite einer anderen Verlagsausgabe enthält.

Bei Osmani erfassen die 19 betrachteten Seiten **alle 14 nummerierten Abbildungen** und fünf weitere Hinweisseiten. Dazu gehören Screenshot, Promptvergleich, Agentenloop und Multiagentenskizze. Diese Darstellungen sind überwiegend didaktische Vereinfachungen. Sie sind keine gemessenen Produktivitätsdiagramme.

Bei Pragmatic sind mehrere Darstellungen tatsächlich in der Datei defekt. Bestätigt fehlen Tracergrafik 112, FSM-Darstellungen 241–243, Pipelinebild 257, Aktivitätsdiagramm 295, Blackboardbild 318, Big-O-Grafik 347, Puzzle 420, Laufzeitgrafik 494 und Puzzlelösung 497. Auf 95, 344, 346 und 350 fehlen mathematische Zeichen oder Formeln. Leere Kästen und Bildpfade bleiben auch im gerenderten PDF sichtbar. Der verfügbare Begleittext wurde ausgewertet; die fehlenden Inhalte wurden nicht aus Vorwissen als vermeintlich vorhandene Buchinhalte rekonstruiert. Nicht jedes weitere Referenzbild wurde einzeln geprüft.

## Wie aus Lektüre Wissen wurde

Die drei neuen Bücher wurden über `python ai.py ingest` in das lokale Quellenarchiv aufgenommen. Technische Erstellungsdaten wurden bei der bibliografischen Zuordnung korrigiert und die Monatsgenauigkeit ausdrücklich festgehalten. Die bestehende Pragmatic-Source wurde wiederverwendet und ausschließlich um drei Pattern-Links ergänzt. Es entstand keine zweite Source für dieselbe Datei.

Die tiefen Analysen stehen außerhalb der knappen Source-Registry. Neue Source-Notizen bleiben jeweils unter 1.000 Wörtern. Sie verbinden Original, deutsche Einordnung, Grenzen und weiterführende Analyse. Die gemeinsame Synthese führt die unterschiedlichen Buchpositionen zusammen und kennzeichnet eigene Agentenübertragungen.

**Sieben neue Patterns:**

- [[Information-Hiding-an-Aenderungsgruenden-ausrichten]]
- [[Bounded-Contexts-und-Uebersetzungsgrenzen-kartieren]]
- [[Aggregate-durch-fachliche-Invarianten-begrenzen]]
- [[Vertraege-mit-Vorbedingungen-Nachbedingungen-und-Invarianten]]
- [[Tracer-Bullet-und-Lernprototyp-bewusst-waehlen]]
- [[Kommentare-als-Schnittstellenwissen-pflegen]]
- [[Designalternativen-vor-Festlegung-vergleichen]]

**13 bestehende Patterns wurden um Belege, Spannungen oder Verbindungen ergänzt:** [[Abstraktionswert-mit-Deletion-Test-pruefen]], [[TDD-als-Verifikationshebel]], [[Klein-und-komposierbar]], [[CONTEXT-Glossar]], [[Plan-first-mit-getrenntem-Review]], [[Testharness-als-staerkster-Hebel]], [[Kontrollierte-Agent-Parallelisierung]], [[Lovable-Prototyp-dann-lokaler-Handoff]], [[Refactoring-mit-Verhaltensvergleich]], [[Schema-als-Vertrag-mit-generierten-Clients]], [[Domaenen-Harness-mit-Daten-Evals-Rechten-und-Review]], [[Claude-als-Lernwerkzeug]] und [[Qualitaetsaufwand-nach-Folgen-und-Abhaengigkeiten-staffeln]]. Frühere inhaltliche Aussagen blieben erhalten.

Die neuen Patterns führen konservativ `meinung`: Sie formulieren begründetes Entscheidungswissen und eigenen Agententransfer, der in diesem Lauf nicht in einem Produktprojekt erprobt wurde. Ein Dateihash oder vollständige Buchlektüre ist keine Verifikation seiner Wirksamkeit. Sekundärdarstellungen einer Buchidee, eigene Essays desselben Autors und die Wiederlektüre derselben PDF zählen nicht als zusätzliche unabhängige Belege.

## Zentrale Prüfungen

- Leseintervalle aller vier Dateien einschließlich der Zeichenoffsets zentral auf Lücken geprüft: vollständige Abdeckung 1–191, 1–324, 1–255 und 1–497.
- Durch Ausgabelimits abgeschnittene Bereiche erneut vollständig gelesen; allein der Abruf oder Ledger-Eintrag wurde nicht als ausreichender Lektürenachweis behandelt.
- Dateihashes von Originalen und kanonischen Kopien sowie die extrahierten Seitentexte abgeglichen.
- Kapitel-/Topic-Abdeckung und kritische Bilder in den Einzelanalysen ausgewiesen. Fachliche Kernbezüge von Evans und Osmani in der gemeinsamen Synthese zusätzlich durch die jeweiligen Analysen geprüft; Aggregate-Referenzen und Assertions wurden dabei präzisiert.
- Alle drei neuen Sources und sieben neuen Patterns mit geprüften Haupt-/Nebenclustern sowie spezifischen Keywords zugeordnet; Themenindex zentral neu erzeugt. Die bestehenden Cluster haben keinen eigenen Architektur-/DDD-Bereich. Fachmodelle wurden deshalb bewusst Planung beziehungsweise Verifikation zugeordnet, statt das Schlagwort Modell fälschlich als LLM-Kosten einzuordnen.
- Themenprüfung: **540 Sources, 102 Patterns, 21 Cluster**, alle zugeordnet. Vier Hinweise auf große bestehende Cluster bleiben bestehen.
- Quellenpipeline: **483 verarbeitet, 50 ignoriert**, konsistent; gegenüber dem Ausgangsstand drei zusätzlich verarbeitete Quellen.
- Knowledge-Validator gegen den vorher gespeicherten Zustand verglichen: **53 vorherige Fehler, dieselben 53 nachher, keine neuen Fehler**. Der Gesamtlauf ist deshalb weiterhin nicht fehlerfrei; die Altfehler wurden nicht als Teil der Buchaufgabe umgeschrieben.
- Format, neue Verlinkungen, UTF-8/LF und Diff-Whitespace der bearbeiteten Inhalte geprüft. Original-PDFs und vollständige Rohbuchtexte bleiben lokal ignoriert; die zusätzlichen Ignore-Regeln beziehen sich gezielt auf die drei neuen Bücher.

Die deterministischen Prüfungen belegen Struktur, Herkunft und Konsistenz. Sie beweisen keine vollständige fachliche Fehlerfreiheit der Zusammenfassungen. Besonders wichtige Aussagen sind deshalb mit Seitenbereichen und Anwendungsgrenzen nachvollziehbar gemacht.

## Arbeitsartefakte und offene Grenzen

Seitentexte, Extraktionsmetadaten, Leseintervalle, interne Claim-Register, gerenderte Prüfseiten und Konsolidierungsberichte liegen lokal unter `.wissen/analysen/buecher-2026-10-29/`. Diese Arbeitsdateien gehören nicht zum versionierten Wissensbestand. Die eigenständig formulierten Analysen, Sources, Patterns und diese Herkunftsnotiz sind die dauerhaft nutzbaren Ergebnisse; Originalvolltexte und Originalbilder werden nicht in diese Dateien kopiert.

Historische Modell-/Toolaussagen, Sicherheitsempfehlungen und Rechtspassagen wurden nicht zu aktuellen Regeln erhoben. Osmanis simulierter Promptvergleich, gedachte Entwicklerin und zusammengesetzte Fallgeschichten bleiben als solche eingeordnet. Fachliche Schwächen einzelner Beispiele stehen in seiner Analyse. Keine Buchbenchmarks oder Produktivitätsversprechen wurden reproduziert.

Die Auswertung verändert keine aktiven Skills, Produktarchitekturen oder Freigabegrenzen. Ihre konkreten Anwendungsvorschläge stehen in der Synthese und brauchen für eine Umsetzung einen ausgewählten Projektfall. Der vorherige Gesamtbericht bleibt eine historische Momentaufnahme. Der zusätzliche Neuaufbau des lokalen Suchkatalogs dient der Auffindbarkeit dieser Ergebnisse; er ist eine mechanische Bestandserfassung und keine erneute inhaltliche Vollanalyse sämtlicher externer Repositories. Katalogumfang und tatsächlich gelesener Analyseumfang bleiben getrennte Angaben.
