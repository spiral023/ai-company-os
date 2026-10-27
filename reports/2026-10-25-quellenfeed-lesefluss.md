# Quellenfeed: Lesen und Wiederfinden

Stand: 25.10.2026. Lokal implementiert und neu gebaut.

## Änderungen

- Vorschau aus höchstens drei vorhandenen Kernaussagen, ansonsten dem vorhandenen Einstieg. Keine neu generierten Zusammenfassungen. Querverweise auf Pattern-Dateien werden im Volltext erhalten; die Vorschau beginnt mit der eigentlichen Aussage.
- Kompaktes Vorschaubild mit Galerie für alle referenzierten Bilder; Navigation per Button und Pfeiltasten, Escape und Fokus-Rückkehr.
- Merkliste, „Später lesen“ und persönlicher Lesestatus im Browserspeicher. Leseflags ändern den Wissens-Verarbeitungsstatus nicht. „Später lesen“ enthält gemerkte, noch ungelesene Quellen. Speicherfehler werden als Sitzungsspeicherung angezeigt.
- Lesemodus mit vollständigem Text, Inhaltsverzeichnis und optionalem Originalvergleich. Videos ohne Aufarbeitung bevorzugen das vorhandene Transkript samt Herkunftshinweis. Dialoge unterstützen Tastaturbedienung und behalten den Fokus.
- Verbindungen kompakter mit zwei sichtbaren Quellen und einer weiteren auf Wunsch. Die Begründung beruht auf gemeinsamen Themen; unbewiesene inhaltliche Beziehungen werden nicht behauptet.
- Thema als Seitentitel, kurze Einführung und kompakte Links zu verwandten Themen. Auf Mobilbreite sind textbasierte Originalquellen über den Original-Reiter erreichbar; Videoansichten bleiben direkt zugänglich.
- Fünf bestätigte Autorenidentitäten ergänzt: Boris Cherny, Jarrod Watts, Lauren Tan, Claude Developers und Dario Amodei. Bestehende Autorenlinks werden auf die gemeinsame Identität abgebildet; vorhandene Bild-Caches werden weiterverwendet.

## Dateien

- `70_Scripts/quellen_feed/feed.js`, `feed.css`, `index.html`, `model.mjs`: Darstellung, Navigation und persönliche Leselisten.
- `70_Scripts/quellen_feed/viewer.mjs`: neuer Galerie- und Lesedialog.
- `70_Scripts/build_quellen_feed.py`: vorhandene Kernaussagen als Vorschau und Alias-Metadaten für alte Links.
- `70_Scripts/quellen_feed/avatars.py`, `70_Scripts/quellen_dashboard/autoren.yaml`: bestätigte Autorenvarianten und Wiederverwendung der Profilbilder.
- `tests/test_quellen_feed.py`, `tests/quellen-feed.test.mjs`: Regressionen für Vorschauen, Autoren, Browserspeicher und Lesefilter.
- `feed/README.md`: Bedienung und Grenzen der lokalen Speicherung.

## Prüfung

- 40 Python-Tests für Feed, Quellenstatistik und CLI sowie 65 Node-Tests für Feed-Modell und bestehende X-/TikTok-Erfassung bestanden.
- Syntaxprüfungen und `git diff --check` erfolgreich.
- Im separaten lokalen Testbrowser geprüft: Merken, Neuladen, Leselistenwechsel, Gelesen-Markierung und Rücknahme, gesperrter Browserspeicher, alte Autoren-URLs, Galerie-Pfeiltasten, Escape, Fokus-Rückkehr, Fokus innerhalb des Dialogs, Inhaltsverzeichnis, Originalvergleich und Inline-Aufklappen.
- Desktop und Mobilbreite einschließlich Reduced Motion ohne horizontalen Überlauf; keine Konsolenfehler im letzten Prüflauf.
- Die erste geprüfte SDLC-Karte sank bei gleichem Testviewport von 2.112 auf 889 CSS-Pixel Höhe. Das ist ein Einzelvergleich, keine Messung aller Karten.
- Build: weiterhin 483 Quellen und vier übersetzte X-Quellen; 424 Quellen haben eine Kernaussagen-Vorschau. Persönliche Leseflags werden nicht in die statische Ausgabe übernommen.

Die In-App-Browser-Anbindung war nicht erreichbar; die Browserabnahme erfolgte gegen denselben lokalen Server im separaten Testbrowser.
