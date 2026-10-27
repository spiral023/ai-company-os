# Quellenfeed

Lokaler chronologischer Reader für die Originalquellen aus `00_Inbox/Quellen/`. Gestaltung nach der im Chat ausgewählten hellen Vorschau: ein Feed, standardmäßig die deutsche Aufarbeitung links und das Original daneben, Plattformfilter oberhalb und Autoren/Themen in der Seitenleiste. Markdown und Medien im Archiv bleiben führend.

## Starten

```powershell
python ai.py quellen feed
```

Danach [http://127.0.0.1:8766/](http://127.0.0.1:8766/) öffnen. Der Server bindet ausschließlich an `127.0.0.1`. Beenden mit **Strg+C**. Ein erneuter Start baut den aktuellen Bestand neu; zum Übernehmen anschließend die Browserseite neu laden.

```powershell
python ai.py quellen feed --port 8770
python ai.py quellen feed --build
```

`--build` erzeugt nur die Website unter `feed/_site/`. Die Seite über HTTP öffnen; `file://` unterstützt die nachgeladenen JSON-Dateien nicht zuverlässig. Andere Ausgabe: `--ausgabe <Ordner>`.

## Inhalte und Bedienung

- Alle Rohquellen inklusive `ignoriert` und gegebenenfalls `neu`. Mehrfach archivierte Originalquellen werden über die vorhandenen kanonischen IDs zusammengeführt; jede Archivfassung bleibt im Reiter **Archivfassung** erhalten.
- Standard: Original-Veröffentlichung, neueste zuerst. Alternativ Erfassungsdatum. Bei fehlendem Veröffentlichungsdatum dient die Erfassung als Ersatz; unsichere Datumsangaben werden gekennzeichnet.
- **Aufarbeitung** ist die erste und standardmäßig aktive Ansicht. Auf großen Bildschirmen steht sie links neben dem Original, auf schmalen Bildschirmen davor. Lange Aufarbeitungen lassen sich vollständig aufklappen. Ohne zugehörige Source-Notiz bleibt das Original sichtbar; es werden keine Aufarbeitungen erfunden.
- Themenlabels sind echte Links in die Themenauswahl. Sie öffnen bewusst alle passenden Autoren und Plattformen; die Filter in der Seitenleiste bleiben kombinierbar. Die Themenübersicht enthält die vorhandene Beschreibung und verwandte Cluster aus der Taxonomie. Unter **Verbindungen** erscheinen andere Quellen mit gemeinsamen Themen samt Begründung. Pattern-Verweise in Aufarbeitungen führen zu ihrem tatsächlich zugeordneten Hauptthema; unbekannte Wiki-Verweise bleiben lesbarer Text.
- Lokale Volltextsuche über erfasste Texte, Transkripte und zugehörige deutsche Aufarbeitungen. Autoren-, Plattform-, Themen-, Monats- und Statusfilter lassen sich kombinieren. `Strg+K` beziehungsweise `Cmd+K` fokussiert die Suche.
- Echte Profilbilder erscheinen an den Quellen und in der Autorenliste. Vorhandene verifizierte Bilder werden aus der Kanalliste übernommen; zusätzlich abgerufene Bilder samt Herkunft liegen unter `feed/avatars/`. Ist kein zuordenbares Bild verfügbar oder eine Datei defekt, bleiben Initialen als Rückfall erhalten. Video-Cover werden nicht als Autorenbilder verwendet.
- Anzeigename, @Username und Avatar im Beitragskopf öffnen das zugehörige Originalprofil in einem neuen Tab. YouTube verwendet verifizierte Kanallinks; unbekannte Profiladressen werden nicht geraten. Die Autorennamen in der Seitenleiste bleiben Filter.
- Erst zwölf Quellen, weitere per Button. Filter sind in der URL teilbar; die letzte Auswahl und Leseposition werden im jeweiligen Browser gespeichert. Kein Account und keine Synchronisierung zwischen Geräten.
- Lokale Originalvideos spielen mit nativen Controls ohne Autoplay. Das Bild wird nicht beschnitten oder gestreckt; nach Laden der Metadaten wird bei Querformatvideos auch das Kartenlayout angepasst.
- **YouTube/TikTok-Video laden** beziehungsweise **Originalpost einbetten** lädt den offiziellen Player oder das X-Widget bei Bedarf. Diese Dienste benötigen Internet. Der Original-Link und die Archivfassung bleiben unabhängig davon verfügbar. Embeds können durch Plattformen, Browser-Erweiterungen oder entfernte Originale blockiert werden.
- YouTube-Ausschnitte berücksichtigen vorhandene Start-/Endmarken. Eine Shorts-URL erhält einen Hochkantplayer. Nicht als Shorts gekennzeichnete Videos verwenden zunächst 16:9; das Originalbild selbst wird durch den Plattformplayer dargestellt.
- Transkripte tragen ihre Erfassungsart und einen Hinweis auf mögliche automatische Übersetzungen/Erkennungsfehler. Ältere importierte Sekundärfassungen werden ausdrücklich nicht als Originaltext bezeichnet.
- X zeigt Hauptpost und belegte Fortsetzungen des Autors. Einzeln geprüfte fachliche Ergänzungen sind gekennzeichnet; Gesprächsantworten und Fremdposts werden ausgefiltert. `thread_posts` zählt die übernommene Auswahl und ist kein Vollständigkeitsnachweis.
- X-Texte außerhalb von Deutsch und Englisch erscheinen als gekennzeichnete Übersetzung auf Deutsch oder Englisch, auch unter „Original“, „Archivfassung“, in Threads und in der Suche. Die vollständigen Übersetzungen liegen mit ihrem exakten Ausgangstext unter `feed/translations/x.json`. Der Build prüft diese gegen die aktuellen Rohnotizen. Fehlende beziehungsweise veraltete Übersetzungen erkannter Fremdsprachen stoppen den Build vor dem Schreiben; es gibt keinen kostenpflichtigen Übersetzungsdienst und keine Netzabrufe beim Build. Neue Übersetzungen müssen beim Quellenlauf ergänzt werden. Die Rohbelege bleiben unverändert archiviert. Bei übersetzten X-Posts führt ein externer Link zum Original; eine X-Einbettung würde wieder die Ausgangssprache zeigen.
- Die Übersetzungsprüfung vergleicht den vollständigen aktuellen Hauptpost, Artikeltext und jede Thread-Fortsetzung mit den Originalsegmenten im Katalog. Teiltreffer reichen nicht; fehlende, geänderte, neu hinzugefügte oder nicht mehr vorhandene Segmente stoppen den Build. Zeilenenden und äußere Leerzeilen werden normalisiert, der Inhalt selbst nicht. Reine Links können unverändert bleiben.
- Bereits deutsche oder englische Bestandteile eines übersetzten Threads können unter `unchanged_segments` mit ihrem vollständigen `original`-Text und `language: de` beziehungsweise `language: en` ausdrücklich freigegeben werden. Auch diese Einträge müssen zum aktuellen Inhalt passen. Der Sprachhinweis im Feed nennt solche unveränderten Bestandteile; die Freigabe erfolgt nicht automatisch durch eine Schrifterkennung.
- Bilder, Video- und PDF-Dateien werden ausschließlich aus referenzierten Dateien im Roharchiv beziehungsweise Sources-Ordner übernommen. Remote-Bilder werden in Markdown als Links dargestellt. Rohes HTML in Quellen wird nicht ausgeführt.

## Lesen und Wiederfinden

- Quellenkarten zeigen bis zu drei vorhandene Kernaussagen aus der Aufarbeitung; fehlen solche, dient der vorhandene Einstieg als Vorschau. Es werden keine neuen Zusammenfassungen erzeugt. „Aufarbeitung weiterlesen“ öffnet den vollständigen Text im Feed.
- Bilder erscheinen als kompakte Vorschau. Die Galerie zeigt alle referenzierten Bilder, unterstützt Pfeiltasten und schließt mit Escape. Der Fokus kehrt zum Auslöser zurück.
- „Lesemodus“ öffnet den vollständigen Text mit Inhaltsverzeichnis und optionalem Originalvergleich. Bei Videos ohne Aufarbeitung wird ein verfügbares Transkript bevorzugt und mit dem Herkunftshinweis angezeigt.
- „Merken“ und „Als gelesen markieren“ sind persönliche Leseflags, getrennt vom Verarbeitungsstatus des Wissensarchivs. Die Merkliste enthält alle gemerkten Quellen; „Später lesen“ nur gemerkte, noch nicht gelesene Quellen. Speicherung lokal in diesem Browser und für diese Website-Adresse, ohne Konto oder Serverdatenbank. Ein tatsächlich blockierter Browserspeicher wird als reine Sitzungsspeicherung gemeldet.
- Autorenvarianten werden ausschließlich über die bestätigten Aliase in `70_Scripts/quellen_dashboard/autoren.yaml` zusammengeführt. Vorhandene Profilbilder und alte Autorenfilter-Links werden weiterverwendet. Gleichnamige, nicht zugeordnete Autoren bleiben getrennt.

## Statische Ausgabe und späteres Hosting

Fehlende Profilbilder einmalig über die öffentlichen Originalquellen abrufen:

```powershell
python ai.py quellen feed --build --avatare-aktualisieren
```

Dabei werden Post-/Kanalidentitäten abgeglichen, Originalavatare lokal gespeichert und ihre Herkunft in `feed/avatars/manifest.json` dokumentiert. Der normale Build lädt weiterhin nichts aus dem Netz. Bereits vorhandene Bilder werden wiederverwendet.

Die Website benötigt im Betrieb nur einen statischen HTTP-Server. `index.html`, CSS, JavaScript, `index.json`, `data/` und `media/` bilden die Ausgabe; keine Datenbank, API-Schlüssel oder Python-Laufzeit auf dem späteren Host nötig. Alle internen Ressourcenpfade sind relativ. Damit ist auch eine eigene Subdomain wie `feed.sp23.online` möglich.

Lokal nutzt der Build für Medien nach Möglichkeit Hardlinks auf demselben Dateisystem, ansonsten Kopien. Die Dateien unter `_site/media/` deshalb als Build-Artefakte behandeln und nicht bearbeiten: Änderungen an einem Hardlink würden auch die Archivdatei verändern. `--kopieren` verwendet für neue Ausgaben unabhängige Kopien. Es werden keine Medien aus dem Internet nachgeladen und keine Archivdateien verändert.

Für eine spätere Übergabe an einen Hoster einen **neuen, leeren Ausgabeordner** verwenden:

```powershell
python ai.py quellen feed --build --kopieren --ausgabe C:/Pfad/zum/neuen/feed-export
```

Ein neuer Ordner verhindert, dass alte, nicht mehr referenzierte Build-Dateien mitgegeben werden. Builds löschen keine alten Dateien. Für lokale Videowiedergabe sollte der spätere Webserver Byte-Range-Anfragen unterstützen; der mitgelieferte lokale Server tut dies bereits. Bei großen Videos sind die Datei- und Speicherlimits des konkreten Hosters zu prüfen.

**Aktuell ist nichts veröffentlicht und keine Domain konfiguriert.** Ein Export enthält auch vollständige archivierte Inhalte und deutsche Aufarbeitungen. Vor einem öffentlichen Hosting sind die konkrete Auswahl, gewünschte öffentliche Zugänglichkeit und Medienbereitstellung festzulegen. Der Ordner `_site/` ist vom Git-Tracking ausgeschlossen.

## Dateien und Checks

- `70_Scripts/build_quellen_feed.py`: Quellen, Aufarbeitungen und Medien zusammenführen; statische Ausgabe und lokaler Server.
- `70_Scripts/quellen_feed/`: HTML, CSS, Browserlogik und reine Auswahlfunktionen.
- Wiederverwendet: Metadaten, Autoren-Aliase und Themenzuordnungen aus `quellen_statistik.py`.
- Bereits genutzte Python-Pakete: `PyYAML`, `markdown-it-py`, `Pillow`.

```powershell
python -m py_compile ai.py 70_Scripts/build_quellen_feed.py
python -m pytest tests/test_quellen_feed.py tests/test_ai_cli.py -q
node --test tests/quellen-feed.test.mjs
python ai.py quellen feed --build
```
