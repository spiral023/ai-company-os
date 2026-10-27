# Zielarchitektur: Wissensfundament einer Agentic Software Factory

**Stand:** 2026-10-25 · **Status:** begründeter Architekturentwurf; Katalog als erste technische Grundlage implementiert. Auswahl der Factory-Laufzeit ist offen.

**Fortschritt 2026-10-26:** Der [semantische Pilot](../../80_Knowledge/Factory/README.md) implementiert die begrenzte Aussage-/Beziehungsschicht, drei Synthesen, fünf Fähigkeitskandidaten und deren Kontextabruf. Quellenfrische und technische Ableitungen sind geprüft; eine vollständige semantische Baseline und reale Factory-Evals bleiben offen.

## Ziel und Abgrenzung

Philipps Auftrag ist, das AI-Company-OS zur gemeinsamen Wissensquelle einer Agentic Software Factory auszubauen. Das gesamte verfügbare Material soll bei Bedarf erneut im Zusammenhang untersucht werden können: Firmenwissen und Entscheidungen, X-/YouTube-/TikTok-/Artikelquellen, Patterns, externe Repos, Skills, Prompts, Workflows und spätere Erfahrungen aus der Factory.

Die Wissensbasis liefert dem Factory-System begründete Optionen, passende Methoden und nachvollziehbare Belege. Der Zustand laufender Jobs, Tickets, Worktrees und Deployments gehört der späteren Factory-Laufzeit. Projektcode bleibt in seinen Projekt-Repos; referenzierte, konkrete Versionsstände können Wissenseingänge sein. Das verhindert, dass ein Wissensindex versehentlich zur zweiten Betriebsdatenbank wird.

Die Architektur ergänzt das [bestehende Wissensfabrik-Konzept](konzept.md). Dessen Forderungen nach Verdichtung, unabhängigen Primärquellen, Fakten-Frische und einem Spannungs-Radar bleiben relevant. Die neue Perspektive verbindet diese Arbeit mit wiederholbaren Gesamtanalysen und der Auswahl praktisch einsetzbarer Factory-Fähigkeiten.

## Befund im vorhandenen Bestand

Am Beginn der Untersuchung lagen 499 Source-Notizen, 91 Patterns, 21 Themencluster und 72 externe Git-Checkouts vor; zusätzlich die separate AI-LLM-Wiki-Kopie. Diese Zahlen sind eine datierte Beobachtung, keine Sollwerte. Die vorhandene Themenzuordnung und TF-IDF-Ähnlichkeit in `70_Scripts/themen.py` erschließen Sources und Patterns. Externe Skills/Prompts und Firmenentscheidungen teilen diesen Suchraum bisher nicht vollständig.

Eine Source-Notiz mit Verweis auf ihren Rohtext und ein Thema mit Quellenliste sind bereits gute Provenienz und Navigation. Was fehlt, ist die durchgängige Kette von einer konkreten Quellenaussage über ihre Bedingungen und Gegenargumente bis zur Auswahl einer Factory-Methode. Ein Pattern mit vielen angehängten Belegen muss bei jeder Entscheidung erneut interpretiert werden. Seine globale Konfidenz beschreibt außerdem nicht automatisch jede spätere Einzelaussage.

Auch die Factory-Idee steht bereits in den eigenen Quellen:

| Quelle im Bestand | Übertragbarer Mechanismus | Grenze des vorliegenden Nachweises |
|---|---|---|
| [Alex Sprogis: Loop und Graph Engineering](../../80_Knowledge/Sources/2026-08-30-alex-sprogis-loop-graph-engineering-das-letzte-video-was-du-s.md) | Erfolgskriterium je Loop, Iterationsgrenze, getrennter Prüfer, Übergabe konkreter Artefakte | Erfahrungsbericht; beschriebene Dark Factory wird im Video nicht aufgebaut |
| [ZazenCodes: Factory-Durchlauf](../../80_Knowledge/Sources/2026-10-19-zazencodes-factory-works-in-this-loop-a-feature-comes-through-the-spec-writer-which.md) | Spec-Writer → Builder → Fachreviews → Approver; Reparaturschleife und menschliche Eskalation | Gesponserte Demo eines erfolgreichen Durchlaufs; Review-Vollständigkeit nicht belegt |
| [Itamar Friedman: begrenzte Autonomie](../../80_Knowledge/Sources/2026-10-22-itamar_mar-2113255396299128887.md) | Autorisierten Arbeitsbereich, getrennte Abnahme und sicheren Fehlerpfad vor dem Lauf festlegen | Zielbild und Analogie, kein Industriestandard oder gemessenes Factory-Ergebnis |
| [Matt Pocock: Factory vor Infrastrukturwahl klären](../../80_Knowledge/Sources/2026-10-22-mattpocockuk-2113196247964074322.md) | Nutzen und Arbeitsklasse vor Auswahl von Orchestrator, Runner und Tracker klären | Ankündigung/Prompt; lokaler Snapshot belegt keinen fertigen Software-Factory-Skill |
| [Julian Ivanov: KI-Betriebssystem](../../80_Knowledge/Sources/2026-06-18-julian-ivanov-ki-automat-bau-dir-dein-ki-betriebssystem-mit-claude-code-k.md) | Wissen, Skills, Tool-Verbindungen und Routinen mit verschiedenen Aufgaben pflegen | Demo; Dauerbetrieb und konfliktfreie Synchronisation folgen daraus nicht |
| [Boris Tane: Kontext zur Laufzeit](../../80_Knowledge/Sources/2025-06-23-boristane-context-engineering-is-what-makes-ai-magical.md) | Aufgabe, Dokumentstruktur, Absicht, Zustand und Umgebung für die Kontextauswahl verbinden | Illustrative Beispiele, keine Vergleichsmessung |

Die Source-Notizen bewahren die Einordnung und verweisen auf die archivierten Originale. Automatische Videotranskripte sind keine verlässliche Grundlage für wörtliche Zitate; im vorliegenden Entwurf wurde keine erneute Sichtung aller Videos vorgenommen.

## Fünf Schichten mit klaren Verantwortungen

| Schicht | Verantwortung | Führende Daten |
|---|---|---|
| 1. Eingänge und Katalog | Verfügbares Material, Herkunft, Versionsstand, Lesegrenzen und Änderungen erfassen | Unveränderte Archive und Git-Checkouts; abgeleiteter lokaler Katalog |
| 2. Aussagen und Beziehungen | Einzelne Aussagen, Bedingungen, Belege, Abhängigkeiten und Widersprüche beschreiben | Geprüfte Markdown-/YAML-/JSON-Datensätze mit Quellenbereichen |
| 3. Synthesen und Methoden | Themenübergreifende Schlüsse, Alternativen und Einsatzbedingungen verdichten | Versionierte Synthesen, Fähigkeitskarten und eigene Entscheidungen |
| 4. Wissenszugriff | Aufgabenretrieval, explorative Recherche und Gesamtanalyse passend auswählen | Abgeleitete Suche/Graphansichten, Kontextpakete und Abdeckungsnachweise |
| 5. Factory-Anbindung und Lernen | Für einen Lauf passende Fähigkeiten auswählen, Ergebnisse zurückmelden und bewerten | Freigegebene Factory-Profile, Eval-Ergebnisse und referenzierte Laufartefakte |

Markdown bleibt das lesbare und mit Obsidian nutzbare Format. SQLite ist zunächst eine rekonstruierbare Such- und Inventarsicht. Ein Graph kann später ebenfalls daraus abgeleitet werden. Ein Datenbankprodukt oder Agent-Framework muss dafür jetzt nicht festgelegt werden.

## Wissensobjekte und Provenienz

Eine gemeinsame Objektidentität verbindet unterschiedliche Sichten. Mindestfelder für künftige semantische Objekte:

| Feldgruppe | Inhalt |
|---|---|
| Identität | Stabile ID, Objekttyp, Titel und normalisierte Begriffe |
| Herkunft | Ursprüngliche URL/Repo, Originaldatum, Erfassungsdatum, Pfad, Inhalts-Hash und gegebenenfalls Git-Commit |
| Beleg | Konkreter Text-/Codebereich oder Videozeitpunkt; Art des Nachweises und letzter Prüfstand |
| Geltung | Aufgabe, Projektart, Stack, Laufzeit, Voraussetzungen und Ausschlussbedingungen |
| Ableitung | IDs und Versionen der Eingänge, Extraktor-/Promptversion, Modell und Lauf-ID |
| Bewertung | Quelle behauptet / statisch nachgelesen / praktisch getestet; Gegenbelege, Unsicherheit und Reviewstatus |

Die fachliche Einheit ist eine überprüfbare Aussage. „Dieses Repo enthält Skill X“ ist mit einer Datei belegbar. „Skill X verbessert unsere Releases“ braucht einen Vergleichslauf. Das beobachtete Vorhandensein eines Skills trägt die zweite Aussage nicht.

Mehrere Wiederholungen derselben Herstellerbehauptung bilden eine gemeinsame Primärquellenfamilie. Rohquelle, Source-Notiz, Pattern-Beleg und externe Zusammenfassung werden als Ableitungskette verknüpft; sie zählen nicht als vier unabhängige Bestätigungen. Bestehende Quellen und append-only Patterns bleiben erhalten. Eine neue Synthese kann historische Aussagen datiert einordnen, ohne die Archive umzuschreiben.

Die ersten Beziehungstypen sollten einen fachlichen Zweck haben: `belegt`, `widerspricht`, `setzt-voraus`, `gilt-fuer`, `implementiert`, `abgeleitet-aus`. Extrahierte Links, statisch bestätigte Abhängigkeiten und semantisch vorgeschlagene Beziehungen brauchen getrennte Nachweisarten. Ein Zahlengewicht allein begründet keine Beziehung.

## Drei Arten des Wissenszugriffs

### Aufgabenbezogener Abruf

Beispiel: „Welche Review-Methode passt zu diesem kleinen React-Feature?“ Zuerst gelten eigene Projektregeln und Entscheidungen. Danach folgen passende Methoden, Voraussetzungen, relevante Gegenargumente und wenige Belege. Fundstellen erlauben gezieltes Nachladen. Die tatsächliche Codeversion und die Aufgabe begrenzen die Auswahl.

Der jetzt verfügbare Befehl `wissen suche` liefert dafür eine einfache wörtliche Abschnittssuche. Semantische Suche, Reranking, automatische Regelpriorisierung und das fertige Kontextpaket sind weitere Ausbaustufen.

### Explorative Recherche

Beispiel: „Wie könnten wir Wartbarkeit vor einer Factory-Umsetzung berücksichtigen?“ Ein breiter Einstieg über mehrere Synthesen erzeugt Teilfragen. Danach werden Gegenbeispiele, Methoden und Implementierungen gezielt gelesen. Der Bericht dokumentiert die untersuchten Bereiche und offenen Lücken. Dieser Modus darf mit einer sinnvollen Teilmenge arbeiten, muss deren Umfang benennen.

### Wiederholbare Gesamtanalyse

Beispiel: „Welche neuen Möglichkeiten entstehen aus dem gesamten Wissensbestand für unsere Factory?“ Ein Snapshot und ein Arbeitsmanifest legen zuerst den Umfang fest. Jede eingeschlossene Passage erhält einen Bearbeitungsstatus. Einzelbefunde werden pro Thema und Repo verdichtet und anschließend **quer zwischen den Themen und Repos** geprüft. Nur Themenzusammenfassungen nebeneinanderzustellen genügt nicht.

Der Vergleich untersucht insbesondere: gemeinsame Voraussetzungen, konkurrierende Annahmen, neue Kombinationen von Fähigkeiten, fehlende Belege und Änderungen gegenüber dem vorigen Lauf. Das Ergebnis enthält priorisierte Experimente oder Verbesserungsentwürfe samt Herkunft. Der konkrete Ablauf und sein Abschlusskriterium stehen in [Gesamtanalyse](gesamtanalyse.md).

**Vollständig** bedeutet immer vollständig relativ zum dokumentierten Scope und Snapshot. Inventarisierte Binärdateien, ausgeschlossene große Texte, nur als Dateiname erfasster Code und nicht gesichtete Videobilder bleiben erkennbare Lücken. Ein Suchergebnis oder ein global benannter Retriever ist kein Vollständigkeitsnachweis.

## Externe Skills, Prompts und Factory-Fähigkeiten

Der Katalog macht fremde Methoden auffindbar. Die produktive Auswahl ist eine eigene Entscheidung auf Grundlage der bestehenden Registry und des Import-Reviews. Die neue Architektur führt keine zusätzliche pauschale Freigabe ein.

Eine künftige **Fähigkeitskarte** verbindet:

- Ziel, typischen Aufgabentyp und Trigger;
- erforderliche Eingaben und klar prüfbare Ausgaben;
- Quelle, Commit, Dateibereich, Hash und vorgefundene Lizenz;
- Runtime-/Modell-/Tool-Abhängigkeiten sowie benötigte Zugriffe;
- mögliche Datei-, Netzwerk- und Betriebswirkungen;
- Geltungsgrenzen, Alternativen und Konflikte mit anderen Methoden;
- Prüfverfahren, Baseline, beobachtete Ergebnisse und Adoption-Status.

Dadurch lässt sich beispielsweise ein pstack-Reviewverfahren untersuchen und dessen Prinzip in einem eigenen Profil nutzen, ohne pstack-Autonomieannahmen oder sämtliche Prompts gleichzeitig zu aktivieren. Gegensätzliche Framework-Anweisungen bleiben vergleichbare Entwürfe, bis eine bewusste Auswahl erfolgt. Versionsänderungen an einem übernommenen Skill machen sein Profil und abhängige Evals prüfbedürftig.

## Übertragbare Referenzmechanismen

Die Details einschließlich Commit- und Lizenzbelegen stehen in den verlinkten Rechercheberichten. Es wurde Fremdcode gelesen, nicht ausgeführt oder übernommen.

| Referenz | Übertragenes Prinzip | Grenze / Entwurfsentscheidung |
|---|---|---|
| [Microsoft GraphRAG](../../reports/2026-10-25-factory-wissensarchitektur-recherche.md) | Globale Map/Reduce-Verdichtung von Communities neben lokalem Originaltextzugriff | Indexierung kann teuer sein; README meldet Maintenance-Modus. Eigenes Hash-Inventar statt blinder Abhängigkeit vom Delta-Detektor |
| [LightRAG und LlamaIndex](../../reports/2026-10-25-factory-wissensarchitektur-recherche.md) | Graph- und Textabruf kombinieren; Beziehungsschema und Pfadtiefe begrenzen | Ein `global`-Modus garantiert keine Verarbeitung des gesamten Bestands; Schema beweist keine Wahrheit |
| [OpenWiki](../../reports/2026-10-25-factory-referenzsysteme.md) | Versionierte Evidence je Claim, stale/unresolved-Prüfung, getrennte Suche und Read | Grounded Claims gelten im untersuchten Stand für Repository-Belege, nicht pauschal für alle Connector-Inhalte |
| [Graphify / Understand Anything](../../reports/2026-10-25-factory-referenzsysteme.md) | Deterministische Extraktion und semantische Ableitung trennen; Cache um Schema/Prompt/Version ergänzen | Roh-PDF-Dateiknoten oder plausibel wirkende Kanten sind keine Inhaltsprüfung |
| [Claude-Mem](../../reports/2026-10-25-factory-referenzsysteme.md) | Suche → zeitliche Einordnung → gezieltes Nachladen | Episodisches Sitzungswissen ergänzt kuratiertes Firmenwissen |
| [Paperclip](../../reports/2026-10-25-factory-methoden-recherche.md) | Katalogeintrag und Agent-Zuweisung trennen; Skill-Versionen führen | Das Control-Plane-Konzept ersetzt keine eigene Wissenssynthese |
| [pstack / Matt Pocock](../../reports/2026-10-25-factory-methoden-recherche.md) | Aufgabenrouter, verblindete Methoden-Evals, getrennte Spec-/Standards-Prüfung | Tool- und Autonomieannahmen jeweils für den eigenen Einsatz prüfen |
| [GSD / gstack](../../reports/2026-10-25-factory-methoden-recherche.md) | Rekonstruierbarer Status neben kuratierten Entscheidungen, konkrete Checkpoints | Laufzustand ist keine allgemeingültige Wissensaussage |

Das ist ein Entwurf aus nachgelesenen Mechanismen. Eine hier gemessene Überlegenheit eines Gesamtsystems wird daraus nicht abgeleitet.

## Erneuerung und Rückfluss aus der Factory

Neue Quellen durchlaufen weiterhin den bestehenden Ingest. Repo-Updates bleiben beim bestehenden External-Repos-Workflow. Nach einer Änderung weist ein neuer Katalogsnapshot geänderte Inhalte aus. In der nächsten Stufe führen Abhängigkeiten von diesen Eingängen zu prüfbedürftigen Claims, Synthesen und Fähigkeitskarten. Eine geänderte Datei kann relevante Aussagen verschieben; ein stabiler Pfad oder Titel reicht als Aktualitätsprüfung nicht.

Gesamtanalysen laufen auf ausdrücklichen Bedarf oder später über einen gesondert beauftragten Zeitplan. Zuerst wird eine vollständige Baseline benötigt. Danach kann ein Delta-Lauf betroffene Ableitungen und ihre Gegenargumente erneuern. In größeren Abständen bleibt eine erneute Gesamtbetrachtung sinnvoll, weil neue Kombinationen über die bisher bekannten Abhängigkeiten hinausgehen können.

Factory-Läufe melden Aufgabenklasse, verwendete Wissensversion, Fähigkeit, Ergebnis, Prüfnachweise, menschliche Korrekturen und Kosten zurück. Ein fehlgeschlagener Lauf erzeugt einen Lernkandidaten. Erst Review und wiederholte Prüfung machen daraus eine Methode oder eigene Entscheidung. So wird ein Einzelfehler nicht als universelle Regel gespeichert.

## Ausbau in überprüfbaren Schritten

| Stufe | Ergebnis | Abnahme |
|---|---|---|
| 0 — umgesetzt | Gemeinsamer Katalog, Originalbezüge, Textsuche und offener Gesamtprüfplan | Suchtreffer aus mehreren Beständen; Hashwechsel bei gleicher Datei; jede indexierte Passage einmal geplant; Auslassungen sichtbar |
| 1 — Pilot vorhanden | Aussagen, explizite Beziehungen, drei querschnittliche Synthesen und fünf Fähigkeitskarten | Jede Aussage auf aktuelle Fundstelle zurückführbar; Quellenfamilien dedupliziert; Unsicherheiten und methodische Konflikte sichtbar; praktische Wirkung separat evaluieren |
| 2 — vollständige Baseline | Nach Manifest bearbeiteter Gesamtbestand mit Themen-/Repo- und Quersynthese | Bearbeitungsnachweis je Eingang; überprüfte Auslassungen; zwölf fachübergreifende Fragen gegen Baseline beantwortet |
| 3 — Factory-Pilot | Adapter zu einer ausgewählten Laufzeit und eine begrenzte Aufgabenklasse | Wiederholbare Ergebnisse, Prüfvertrag, Kosten-/Iterationsgrenzen und dokumentierte menschliche Eingriffe |
| 4 — laufendes Lernen | Hashabhängige Erneuerung, Delta-Analysen und geprüfter Rückfluss | Änderungen machen betroffene Ableitungen sichtbar; alter Snapshot bleibt nachvollziehbar; Wiederanlauf ist getestet |

Die ersten Synthesen sollten **Kontextbereitstellung**, **Spec–Build–Review-Ablauf** und **Wissenspflege/Methodenauswahl** verbinden. Als erste Fähigkeitskarten bieten sich Spec-Klärung, Implementierungsplanung, Spec-Review, Standards-Review und Ergebnisverifikation an. Diese Auswahl ist eine Arbeitshypothese; der Pilot kann fehlende Voraussetzungen aufdecken.

## Noch zu entscheiden

- Erste wertvolle Aufgabenklasse und repräsentatives Projekt für den Factory-Pilot.
- Modell-/Kostenrahmen für vollständige semantische Analyse und unabhängige Prüfung.
- Benötigte Code- und Bild-/Videotiefe; aktuell werden Medien nicht visuell untersucht.
- Factory-Laufzeit, Runner, Tracker und Betriebsumgebung nach dem fachlichen Pilot.

Bis diese Entscheidungen anstehen, ist der lokale Katalog ohne neue Dienste nutzbar. Die Bibliothek bleibt das gemeinsame Wissensfundament, während die Ausführung austauschbar vorbereitet wird.
