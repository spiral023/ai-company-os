# Blog-Themenauswahl und neue Beiträge

Stand: 22.10.2026. Ausgangsbestand: 46 Beiträge, alle freigegeben. Der Blog-Check bestand bereits vor den Änderungen ohne Fehler oder Hinweise.

## Auswahl

Die vorhandenen Beiträge decken Prompts, Agent-Dateien, Kontextpflege, Parallelisierung, Tests und UI-Arbeit bereits breit ab. Die folgenden Themen ergänzen eigenständige praktische Fragen. Die Priorität ist eine redaktionelle Einschätzung aus Bestand, Nutzwert und verfügbaren Quellen; Suchvolumen oder Nachfrage wurden nicht gemessen.

| Priorität | Thema | Warum sinnvoll | Abgrenzung zum Bestand |
|---|---|---|---|
| Hoch | RAG für Text, Tabellen und vollständige Dokumente | Hilft beim Entwurf und Prüfen eines Dokumentenchats; der Themencluster Wissensarbeit hatte vor diesem Lauf keinen eigenen Beitrag. | Behandelt Informationszugriff und Quellenaktualisierung, während bestehende Kontextartikel die Agent-Session betreffen. |
| Hoch | API-Verträge mit Schema und generierten Clients | Gibt eine konkrete Antwort auf wiederholt falsch aufgebaute Requests und veraltete Clients. | Ergänzt Verhaltenstests um die Struktur und Versionsbindung einer Schnittstelle. |
| Hoch | Agent-Tracing nach Beobachtungsebene | Hilft, eine erfolgreiche Tool-Rückgabe bis zur erwarteten Wirkung zu untersuchen. | Ergänzt Codepfad-Erkundung und Handoff um aufgezeichnete Ausführung und ihre Beobachtungsgrenzen. |
| Später | Weitere Memory- und Agent-Datei-Tipps | Sinnvoll, wenn eine neue Quelle eine konkrete bisher offene Entscheidung verändert. | Bereits eigene Beiträge zu AGENTS.md, Kontextpflege und Handoff vorhanden. |
| Später | Weiterer allgemeiner Test- oder Review-Ratgeber | Ein neuer Beitrag sollte eine andere Fehlerklasse oder einen ausgearbeiteten Versuch liefern. | Grüne Tests, Refactoring, adversariale Prüfung und Review-Prompts sind bereits behandelt. |

Verwendete Briefings: `themen.py blog wissensarbeit`, `themen.py blog verifikation`, `themen.py blog erweiterungen`; ergänzende Keyword-Suchen nach Schema und Tracing. Bei API-Verträgen und Tracing wurden die spezifischen Themenbegriffe gewählt, statt die breiteren Cluster-Keywords künstlich in Titel zu setzen.

## Erstellte Artikel

Alle Beiträge gehören zur Kategorie `arbeitsweisen`, enthalten eine Kurzfassung, konkrete Beispiele oder Auswahlhilfen, Grenzen sowie eine abschließende Handlungsempfehlung.

| Datei in `blog/posts/` | Umfang ungefähr | Quellen |
|---|---|---|
| `2026-10-22-rag-text-tabellen-volltext.md` | 830 Wörter | Julian Ivanovs RAG-Tutorial, 22.09.2025 |
| `2026-10-22-api-vertraege-schema-coding-agents.md` | 840 Wörter | Boris Tane, „Ship types, not docs“; @sarahfim zum agententauglichen Repository |
| `2026-10-22-agent-tracing-aufruf-ausfuehrung-wirkung.md` | 890 Wörter | Josh Rosen zur Architektur von Agent-Tracing |

Die Quellen sind als vorhandene Source-Dateien im Frontmatter verknüpft und im Text referenziert. Es wurden keine neuen Knowledge-Quellen angelegt oder vorhandene Quellenstatus geändert.

Zusätzlich enthält `blog/glossar.yaml` zehn neue, selbst formulierte Begriffe: RAG, OCR, Chunk, API-Schema, OpenAPI, Laufzeitvalidierung, Typecheck, Trace, Instrumentierung und OpenTelemetry.

## Einordnung der Quellen

- Das RAG-Tutorial wurde über die vorhandene Auswertung und das archivierte automatische Transkript geprüft. Eine neue Videosichtung fand nicht statt. Der Artikel übernimmt weder Anbieterempfehlungen noch damalige Preise, Datenschutzversprechen oder gemessene Qualitätsgewinne.
- Das Veröffentlichungsdatum von „Ship types, not docs“ ist im Archiv unsicher. Der Beitrag nennt deshalb keinen vermeintlichen Erscheinungstag. Die Originalseite wurde erneut geöffnet; Einsparungsfaktoren und die Gleichsetzung von Compile-Erfolg mit korrektem Verhalten werden nicht übernommen.
- Der Tracing-Artikel liefert eine technische Systematik. Daraus werden Diagnosehilfen abgeleitet; vollständige Beobachtbarkeit oder exakte Wiederholbarkeit werden nicht behauptet.
- Die Beispiele und vorgeschlagenen Prüfabläufe sind als solche erkennbar. Es wurde kein RAG-System, API-Client oder Agent-Tracing-System implementiert oder im Betrieb abgenommen.

Ergänzender Begriffsabgleich mit den offiziellen Beschreibungen von [OpenAPI](https://www.openapis.org/what-is-openapi) und [OpenTelemetry Traces](https://opentelemetry.io/docs/concepts/signals/traces/). Die Blog-Quellenlisten bleiben an die vorhandenen ausgewerteten Quellen gebunden.

## Prüfung und Freigabestand

- `python blog/build_blog.py --check`: vor der Bearbeitung 46 Beiträge, danach 49 Beiträge; jeweils ohne Fehler oder Hinweise.
- `python blog/build_blog.py --drafts`: Vorschau mit allen neuen Artikeln erzeugt; anschließend vollständig gegen die Slop-Regeln gelesen und sprachlich gestrafft.
- Lokale Browserprüfung über Playwright: alle neuen Artikel bei 1440 Pixeln und 390 Pixeln Breite geprüft. Überschriften, Kurzfassung, Tabellen beziehungsweise JSON-Beispiel sowie Quellen- und Glossarlinks dargestellt. Keine überbreite Gesamtseite; breite Tabellen bleiben innerhalb ihres horizontal scrollbaren Bereichs. Keine sichtbaren `{q:n}`-Marker oder unaufgelösten `post:`-Verweise.
- Screenshots liegen lokal und Git-ignoriert unter `.playwright-mcp/blog-{rag,api,tracing}-{desktop,mobile}.png`. Der eingebaute Browser war nicht erreichbar; die Sichtprüfung erfolgte im verfügbaren Playwright-Browser.
- `python blog/build_blog.py --auto-freigeben`: alle drei neuen Beiträge automatisch freigegeben, keiner zurückgehalten.
- `python blog/build_blog.py`: lokale Ausgabe mit 49 freigegebenen Beiträgen unter `blog/_site/` erzeugt. Neue Artikel in HTML, Startseite, Sitemap und Feed kontrolliert; beide XML-Dateien erfolgreich geparst.
- `git diff --check -- blog`: bestanden. Vorhandene Änderungen außerhalb dieses Auftrags bleiben unberührt.

Die Freigabe ist lokal. Es gab keinen Commit, Push, WebSub-Ping oder Deployment; die öffentliche Website wurde nicht verändert.
