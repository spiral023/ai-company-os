# KI-Quellen

Lokale HTML-Liste zum Weitergeben an Kollegen. Gestaltung nach der ausgewählten ersten Vorschau: Dark Mode, blaue Akzente, Profilkarten und Themenlabels; optionaler Light Mode.

## Öffnen und weitergeben

`index.html` im Browser öffnen. Die Datei enthält CSS, JavaScript und alle Profilbilder. Es genügt, **diese eine Datei** weiterzugeben; ein Server, Installation oder zusätzliche Dateien sind für die Nutzung nicht nötig. Kanallinks brauchen eine Internetverbindung. Merkliste und Theme werden im jeweiligen Browser gespeichert; wenn dessen Speicher gesperrt ist, gelten sie für die aktuelle Sitzung.

## Aktualisieren

Im Repo-Root:

```powershell
python ai.py social
python ai.py social --check
```

Das erzeugt nur die HTML-Liste. Es lädt keine neuen Beiträge, schreibt keine Knowledge-Dateien und führt keine Neuindizierung aus. Der Build braucht weder Netzwerkzugriff noch zusätzliche Python-Pakete.

## Inhalte und Dateien

- Beschreibungen und bestehende Kanallinks: `80_Knowledge/Guides/AI-Coding-Agents-Social-Media-Uebersicht.md`.
- `profiles.json`: Reihenfolge, Namen, Sprache, Themen und Labels. Nate B. Jones ist als eine Person mit zwei Plattformen zusammengefasst; sein gemeinsamer Beschreibungstext steht hier und basiert auf beiden Guide-Einträgen.
- `image-research.json`: Herkunft der recherchierten Bilder, Abrufdatum und ergänzte YouTube-Kanallinks.
- `images/`: verkleinerte Originalbilder und Kanalavatare. Für TechSnack konnte kein Avatar abgerufen werden; die Karte zeigt Initialen.
- `template.html`: HTML-, CSS- und JavaScript-Vorlage.
- `index.html`: erzeugte, eigenständig nutzbare Datei. Änderungen hier werden beim nächsten Build ersetzt.
- `70_Scripts/build_social_directory.py`: kleiner Generator mit Python-Standardbibliothek.

Neue Kanäle zuerst im Guide beschreiben und in `profiles.json` ergänzen. Für YouTube-Kanäle ohne Link im Guide den verifizierten `channelUrl` in `image-research.json` angeben. Danach bauen. Der Generator prüft, dass alle Guide-Einträge genau einmal abgedeckt sind und die Texte 300–500 Zeichen lang bleiben.

## Bilder und Reichweite

Die eingebundenen Bilder stammen aus den jeweils dokumentierten eigenen Websites oder Profilen. Die Herkunft ist auch auf der Seite unter „Über diese Liste & Bildquellen“ erreichbar.

Followerzahlen werden nur bei tatsächlich geprüften Plattformangaben ergänzt, nicht geschätzt oder über Plattformen summiert. Der aktuelle Stand enthält keine Zahlen. Optionaler Metadateneintrag je Profil in `image-research.json`:

```json
"followers": {
  "platform": "YouTube",
  "label": "auf dem Profil angezeigte Abonnentenzahl",
  "source": "https://www.youtube.com/@verifizierter-kanal",
  "checkedAt": "2026-10-10"
}
```

## Lokale Vorschau

Optional im Repo-Root:

```powershell
python -m http.server 8766 --bind 127.0.0.1 --directory docs/ki-quellen
```

Dann `http://127.0.0.1:8766/` öffnen. Es erfolgt kein Deployment.

## Mobile Prüfung

Am 10.10.2026 lokal in Chrome mit Touch-Emulation geprüft: 320, 360, 375, 390 und 430 Pixel Breite, Tablet mit 768 Pixeln sowie Querformat mit 844 × 390 Pixeln, jeweils im Dark und Light Mode. Suche, Plattform-/Themen-/Sprachfilter, Merkliste und Infodialog funktionieren ohne seitliche Seitenüberläufe. Touch-Bedienelemente sind mindestens 44 × 44 Pixel groß; Eingabefelder verwenden mindestens 16 Pixel Schriftgröße.

Bei 320 und 390 Pixeln wurde zusätzlich 200 % Schriftgröße geprüft. Lange Wörter umbrechen, schmale Filter und Karten ordnen sich neu an; eine hohe Kopfzeile scrollt mit dem Inhalt. Die Prüfung ersetzt keinen Test auf einem echten Gerät mit iOS/Safari.
