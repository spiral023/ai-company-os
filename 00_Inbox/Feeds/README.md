# RSS- und Atom-Feeds

`feeds.yaml` registriert wiederkehrende Quellen für neue Artikel. Der Feed selbst dient der Entdeckung; einzelne Beiträge werden wie bisher vollständig unter `00_Inbox/Quellen/URL/` archiviert und anschließend ins Knowledge-System eingearbeitet.

## Bedienung

```powershell
python ai.py feeds add https://www.aihero.dev/rss.xml --name "Matt Pocock / AI Hero"
python ai.py feeds list
python ai.py feeds check
python ai.py feeds check --url https://www.aihero.dev/rss.xml --limit 5
python ai.py feeds check --thema verifikation --limit 10
python ai.py feeds check --ausgabe 00_Inbox/Feeds/Auswahl.md
python ai.py feeds check --alle --limit 20
```

`add` prüft den Feed vor dem Eintragen und verhindert doppelte Feed-URLs. Unterstützt werden RSS 2.0 und Atom ohne zusätzliche Abhängigkeiten gegenüber dem bestehenden Python-Setup.

`check` zeigt standardmäßig eine thematische Vorauswahl aus den noch nicht archivierten Einträgen. Der Abgleich berücksichtigt Rohquellen und `80_Knowledge/Sources/`, einschließlich bereits verarbeiteter oder ignorierter Quellen. Tracking-Parameter werden für den Vergleich entfernt. Ein unbekanntes Datum bleibt unbekannt.

## Auswahl statt Vollimport

Die Vorauswahl nutzt Titel und Beschreibung aus dem Feed sowie die bestehende Taxonomie und die gepflegten Keywords aus `80_Knowledge/Themen/`. Allgemeine Wörter wie „AI“, „Agent“ oder „Skill“ reichen allein nicht aus. Konkrete Treffer im Titel wiegen stärker als in der Beschreibung. Hinweise auf Anleitungen, benannte Skills oder Erfahrungsberichte verstärken eine bereits vorhandene Themenpassung.

Die interne Schwelle von sechs Punkten ist eine Suchheuristik: Ein Kernbegriff im Titel reicht beispielsweise aus. Sie misst weder Qualität noch Neuigkeitswert des Volltexts. Zu jedem Kandidaten stehen die vorgeschlagenen Themen und die auslösenden Begriffe. Fehlende oder knappe Feed-Beschreibungen können passende Beiträge übersehen.

Unter den passenden Kandidaten werden neuere Beiträge bevorzugt. Die allgemeine Liste berücksichtigt zunächst höchstens zwei Artikel pro Hauptthema und füllt anschließend freie Plätze mit weiteren Kandidaten. So verdrängt ein einzelnes Thema nicht alle anderen. `--thema <cluster-id>` konzentriert die Vorauswahl auf ein Thema. `--limit` begrenzt die angezeigte Liste pro Feed, nicht die Zahl grundsätzlich relevanter Artikel.

`--alle` zeigt alle offenen Einträge nach Datum bis zum gewählten Limit, einschließlich schwacher Treffer und zurückgestellter Seiten mit Begründung. Bei zusätzlichem `--thema` erfolgt die Bewertung für dieses Thema; die vollständige Liste bleibt einsehbar. `--ausgabe` speichert die angezeigte Liste als generierte Markdown-Datei für die redaktionelle Prüfung. Erneute Ausgabe an denselben Pfad ersetzt diesen Bericht.

Feed-spezifische Regeln stehen unter `auswahl` im Register:

- `ausschliessen_pfade`: genaue URL-Pfade oder Muster mit `*`, die aus der normalen Vorauswahl genommen werden. Sie bleiben über `--alle` sichtbar.
- `themen_keywords`: zusätzliche konkrete Begriffe je bestehender Cluster-ID, etwa `/pr` und `pull request` für `verifikation`. Damit lassen sich kurze englische Feed-Beschreibungen ergänzen.

Bei AI Hero werden Newsletter- und Kurs-Landingpages sowie eine Kurs-Vorschau zurückgestellt. Die Dictionary-Einträge werden als Sammlung über `sync_ai_coding_dictionary.py` gepflegt und deshalb nicht einzeln vorgeschlagen.

Vor der Übernahme prüft der Agent den Originalbeitrag: Enthält er eine konkrete, übertragbare Arbeitsweise, eine relevante Änderung oder eine begründete neue Perspektive? Ergänzt er unseren Bestand oder wiederholt er ihn? Nur die ausgewählten Beiträge werden archiviert und verarbeitet. Eine gute Themenpassung kann viele Kandidaten ergeben; die Liste ist keine Pflicht, alle zu übernehmen. Bei größeren Auswahlen in Schritten von höchstens fünf Beiträgen vorgehen.

Bei mehreren URLs für denselben Artikel kann ein Feed unter `url_aliases` eine geprüfte Zuordnung `Feed-URL: archivierte URL` führen. Der Alias gilt erst als bekannt, wenn die zugehörige Original-URL tatsächlich archiviert ist. Bei AI Hero zeigen der flache Pfad und der Pfad mit `/skills/` denselben Beitrag zum Update 1.3; der flache Pfad ergänzt einen Kurztext und einen Share-Link. Diese Zuordnung ist hinterlegt. Weitere Aliase erst nach Inhaltsvergleich ergänzen, nicht allein wegen eines ähnlichen Titels.

„Noch nicht archiviert“ bedeutet nicht „seit dem letzten Abruf veröffentlicht“. Ein Feed kann ältere Beiträge, Kursseiten und Newsletter-Landingpages enthalten. Sein Umfang bestimmt außerdem, wie weit der Rückblick reicht. Deshalb erst auswählen, dann erfassen:

```powershell
python ai.py ingest <artikel-url>
```

Danach gelten `knowledge-ingest` beziehungsweise `quellen-verarbeiten`, einschließlich Themenzuordnung und Quellenprüfung. Ein Feed-Auszug ersetzt den Artikelvolltext nicht. Feed-Datum und Titel sind Hinweise; maßgeblich bleibt die Originalseite.

Die Befehle laufen manuell. `check` verändert weder das Register noch den Quellenstatus und importiert keine Artikel. Eine zeitgesteuerte Prüfung ist bisher nicht eingerichtet.
