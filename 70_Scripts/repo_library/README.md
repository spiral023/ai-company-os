# Repo-Bibliothek

Erzeugt aus `external_repos/INDEX.md` genau eine offline nutzbare Datei: `external_repos/INDEX.html`. Es werden keine Dependencies installiert und keine Analyse-Repos oder externen Dienste angesprochen.

## Inhalte aktualisieren

1. Aufgaben, Kategorien, Empfehlungen oder Repo-Profile in `external_repos/INDEX.md` bearbeiten.
2. Im Repo-Root `python ai.py repos build` ausführen.
3. `external_repos/INDEX.html` per Doppelklick öffnen beziehungsweise im Browser neu laden.

`python ai.py repos check` prüft, ob die HTML zum aktuellen Markdown, zur Konfiguration und zu den Vorlagen passt. Der Check schreibt nichts und meldet einen Fehler, wenn die Datei fehlt oder veraltet ist. Auch `70_Scripts/update_external_repos.py` erzeugt die HTML nach der Index-Pflege neu; `--dry-run` und `--no-index` erzeugen keine HTML.

Direkter Aufruf, beispielsweise für eine separate Ausgabedatei:

```powershell
python 70_Scripts/build_repo_library.py --input external_repos/INDEX.md --output external_repos/INDEX.html
python 70_Scripts/build_repo_library.py --check
```

## Module

| Datei | Aufgabe |
|---|---|
| `parser.py` | Detailprofile, Aufgaben, Kategorien, Empfehlungen und allgemeine Abschnitte lesen; Verweise und eindeutige IDs prüfen |
| `markdown.py` | Markdown aus dem Index sicher und ohne nachgeladene Ressourcen darstellen |
| `builder.py` | Daten, Vorlagen und Module deterministisch in eine HTML einbetten; Aktualität prüfen |
| `discovery.json` | Suchsynonyme, Stoppwörter, Ziele für den Wegfinder und schnelle Sucheinstiege |
| `templates/index.html` | Grundstruktur, Dialoge und zugängliche Bedienelemente |
| `templates/library.css` | Gestaltung, helle/dunkle und schmale Ansichten, Druck und Reduced Motion |
| `templates/search.js` | Gewichtete, lokale Suche und Ähnlichkeit über gemeinsame Aufgaben/Themen |
| `templates/state.js` | Merkliste, letzte Profile, Filter, Deep Links und Clipboard-Fallback |
| `templates/views.js` | Bibliothek, Aufgaben, Arbeitsrouten, Vergleich und vollständiger Originalindex |
| `templates/app.js` | Ereignisse, Tastaturbedienung und mobile Detailansicht |

Die Quellen sind modular; die Ausgabedatei bleibt vollständig eigenständig. Nach Änderungen an einem Modul ebenfalls `python ai.py repos build` ausführen. Generierte HTML nicht von Hand bearbeiten.

## Datenvertrag und Vollständigkeit

- Ein Repo erhält eine Überschrift `## owner/repo` und eine GitHub-URL als Metadatenfeld. Neue Felder werden ohne Schema-Erweiterung übernommen.
- Aufgaben verwenden die vorhandene Tabelle mit drei Spalten; Kategorien die vorhandenen Tabellen mit fünf Spalten. Ihre Repo-Verweise müssen auf Detailprofile zeigen.
- Mehrfachzuordnungen bleiben erhalten. Unkategorisierte Detailprofile erscheinen weiterhin in der Bibliothek.
- `n/a` oder fehlende Sterne werden als unbekannt gespeichert und angezeigt. Sterne sind kein Qualitätsscore.
- Abweichende lokale Ablagen werden aus `Ablage (abweichend)` übernommen. Lokale README-Links funktionieren, wenn die HTML Zugriff auf die zugehörige Bibliothek hat; sämtliche Profilinhalte bleiben auch ohne diese Ordner verfügbar.
- Alle allgemeinen Abschnitte, der vollständige gerenderte Index und der unveränderte Original-Markdown sind eingebettet. Auch ohne JavaScript bleibt der Index lesbar.
- Die Suche ordnet vorhandene Inhalte über Begriffe, Synonyme und kuratierte Aufgaben zu. Sie verwendet kein externes Modell. Neue Arbeitsrouten werden nicht automatisch erfunden; ihre Quelle ist „Empfohlene Startpunkte“.
- Der Build enthält keinen variablen Zeitstempel. Gleiche Eingaben erzeugen dieselbe Ausgabe; `check` erkennt auch geänderte Vorlagen.

## Bedienung

- **Entdecken:** Problemsuche, kombinierbare Themen- und Typfilter, Sortierung und vollständiges Detailprofil.
- **Aufgaben:** Zwei Schritte über Ziel und konkrete Aufgabe; „Alle Aufgaben“ zeigt den gesamten Bestand.
- **Arbeitsrouten:** Empfehlungen und praktische Kombinationen mit kopierbaren lokalen Einstiegspunkten.
- **Merkliste:** Favoriten und zuletzt explizit geöffnete Profile; gespeichert im jeweiligen Browser. Bei blockiertem Browser-Speicher funktioniert die Sitzung weiter.
- **Vergleich:** Zwei oder drei Profile mit gleichen Informationsfeldern nebeneinander.
- **Originalindex:** Alle Inhalte plus Original-Markdown und eine Druckansicht.
- **Strg+K:** Suche fokussieren. Pfeiltasten navigieren in der Ergebnisliste, Enter öffnet das Profil. Escape schließt Dialoge.

## Checks

```powershell
python -m pytest tests/test_repo_library.py tests/test_update_external_repos.py tests/test_ai_cli.py -q
node --test tests/test_repo_library_search.cjs
python ai.py repos check
```
