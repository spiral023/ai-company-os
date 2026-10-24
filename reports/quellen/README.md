# Quellenstatistik

[Interaktive Auswertung öffnen](index.html) · [Markdown-Übersicht](Uebersicht.md) · [Aktuelle Daten](aktuell.json)

## Aktualisieren

Im Repo-Root ausführen:

```powershell
python ai.py quellen statistik
python ai.py quellen statistik --snapshot
```

Der erste Befehl aktualisiert HTML, JSON und Markdown. `--snapshot` speichert zusätzlich eine unveränderliche Messung unter `snapshots/`. Bestehende Messungen werden nicht überschrieben. Die HTML-Datei enthält alle Daten, Styles und Diagramme und funktioniert direkt per Doppelklick ohne Server, Internet oder externe Bibliotheken. Dateilinks funktionieren, solange die Auswertung an ihrem Ort im Repo liegt; beim alleinigen Weitergeben der HTML bleiben Diagramme und Filter nutzbar.

Empfohlener Rhythmus: einmal pro Woche und nach größeren Quellenläufen `--snapshot` verwenden. Es wurde kein automatischer Zeitplan eingerichtet. Ein Scheduler kann denselben Befehl mit dem Repo als Arbeitsverzeichnis starten. Dafür ist kein LLM nötig. Quellen, Patterns und Themenzuordnungen werden nur gelesen; es erfolgen keine API-Aufrufe.

## Filtern und exportieren

```powershell
python ai.py quellen statistik --autor matt-pocock
python ai.py quellen statistik --thema verifikation --keyword TDD
python ai.py quellen statistik --bestand sources
python ai.py quellen statistik --ausgabe tmp/meine-quellen-auswertung
```

CLI-Filter zeigen passende Quellen im Terminal und setzen die Anfangsansicht im HTML. JSON, Markdown und Snapshots enthalten weiterhin den Gesamtbestand. Im HTML lassen sich Bestand, Plattform, Autor, Thema, Keyword, Status und Freitext kombinieren. Balken und Keyword-Schaltflächen setzen Filter. Die aktuelle Auswahl kann als CSV exportiert werden. Kennzahlen oben und gespeicherte Bestandsmessungen bleiben global; die Trendverteilungen folgen nur der Auswahl des Bestands (Roharchiv oder Sources).

## Zählregeln

- **Rohdateien:** direkte Markdown-Dateien unter `00_Inbox/Quellen/<Typ>/`. Keine Medien, Wörterbuch-Unterarchive oder Root-README.
- **Eindeutige Rohquellen:** X-Posts und Videos anhand ihrer ID, sonst normalisierte URL ohne Fragment und Trackingparameter. Relevante Query-Parameter bleiben erhalten. Ein archivierter Thread zählt als eine Quelle, nicht als Zahl seiner Posts. Notizen ohne URL bleiben getrennt. Nicht jede inhaltliche Dublette ist damit automatisch erkannt.
- **Source-Notizen:** eigene Zählmenge aus `80_Knowledge/Sources/`; nicht mit Rohquellen addieren. Explizite Verknüpfungen über `source_notiz`, `rohquelle` und `zweitquelle`, jeweils auch als YAML-Liste.
- **Autoren:** bekannte Identitäten werden über `70_Scripts/quellen_dashboard/autoren.yaml` verbunden. Ohne expliziten Alias bleiben Namen nach Plattform getrennt. Fehlende Roh-Autoren werden aus verknüpften Sources übernommen, sonst als „Unbekannt“ gezählt. Hersteller, Kanäle und Personen sind unterschiedliche Autorenidentitäten; keine Aussage über die Anzahl natürlicher Personen.
- **Themen und Keywords:** aus `zuordnung.yaml`, Haupt- und Nebencluster zusammen. Pro Quelle und Begriff nur eine Zählung. Ein Rohquellen-Duplikat übernimmt die Vereinigung seiner Zuordnungen. Quellen ohne Aufarbeitung können ohne Thema bleiben. Source- und Pattern-Keywords werden hier nicht vermischt.
- **Qualität:** Metadatenhinweise sind keine vollständige Knowledge-Validierung. Dafür separat `python 70_Scripts/validate_knowledge.py` ausführen. Die 53 dort am 24.10.2026 beobachteten bestehenden Befunde wurden durch diese Funktion nicht bearbeitet.
- **Geltungsbereich:** `external_knowledge/`, `external_repos/`, Blogposts und Faktenzeilen sind nicht in diesen Quellensummen enthalten.

## Verlauf und Trends

Die Ansicht unterscheidet zwei Zeitmodelle:

1. **Erfassungsverlauf:** standardmäßig der gesamte Zeitraum seit der frühesten Erfassung des gewählten Bestands bis heute. Wahlweise letzte 365, 90, 28 oder 7 Tage. Umschaltbar zwischen kumulierten Erfassungen und neu erfassten Quellen, mit automatischen Tages-, Wochen- oder Monatsintervallen und einer vollständigen Wertetabelle. Bei einem begrenzten Zeitraum enthält die kumulierte Kurve den bekannten Vorbestand. Autoren-/Themenfilter behalten die gemeinsame Zeitachse des gewählten Bestands. Fehlende, ungültige und zukünftige Datumsangaben werden ausgeschlossen und ausgewiesen. Separat darunter: kurzfristiger Vergleich von 7, 28 oder 90 vollständigen Tagen bis gestern mit dem vorherigen Zeitraum. Alles wird aus dem `erfasst`-Datum des heutigen Bestands rekonstruiert, bei Duplikaten frühester Termin. Später gelöschte Quellen fehlen in dieser Rückschau; das ist keine historische Bestandsmessung. Das Veröffentlichungsdatum wird dafür nicht verwendet.
2. **Bestandsmessungen:** ausschließlich gespeicherte Snapshots, mit echten Zeitabständen im Diagramm. Autoren-, Themen- und Keyword-Trends zeigen die Nettoänderung der letzten zwei vergleichbaren Messungen. Ein einzelner Snapshot ist nur ein Ausgangspunkt. Rückdatierte Snapshots werden nicht erzeugt.

Snapshots verwenden UTC-Zeitstempel; die HTML zeigt Zeiten in Europe/Vienna. Ändern sich Zählregel-Version oder Autoren-Aliase, werden alte Messungen aufbewahrt, aber aus der vergleichbaren Reihe ausgeschlossen. Unlesbare oder inkompatible Messungen werden sichtbar gemeldet. Ein anderer Ausgabeordner hat eine eigene Snapshot-Reihe. Die Metadaten werden bei jedem Lauf neu eingelesen; Caches und eine Datenbank sind nicht nötig.

## Prüfen

```powershell
python -m unittest discover -s tests -p test_quellen_statistik.py
python -m unittest discover -s tests -p test_ai_cli.py
python -m py_compile 70_Scripts/quellen_statistik.py ai.py
node --test tests/quellen-activity.test.cjs
```
