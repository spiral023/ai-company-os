# Quellen-Eingang

Roh erfasste externe Quellen, vollständig und unbearbeitet. Eingangsstufe vor `80_Knowledge/`.

## Struktur

```
00_Inbox/Quellen/
  2026-07-27-cerebras-2081828128952095022.md      ← Notiz mit Volltext
  medien/
    2026-07-27-cerebras-2081828128952095022/      ← Bilder dieser Quelle
      01-cover.jpg
      02-photo.jpg
```

Slug = `<Veröffentlichungsdatum>-<Handle>-<ID>`. Die ID hält den Slug eindeutig, auch bei mehreren Posts eines Autors am selben Tag.

## Warum Bilder lokal liegen

Bei X-Artikeln tragen Charts und Preistabellen regelmäßig Zahlen, die im Text nicht vorkommen. `pbs.twimg.com`-URLs sind nicht dauerhaft — sie verfallen mit gelöschten Posts. Die Bilder werden deshalb in Originalauflösung (`?name=orig`) heruntergeladen und liegen neben der Notiz.

Bilder sind in `.gitignore` **nicht** ausgeschlossen, werden also mit dem Repo versioniert. Die Notiz verweist relativ auf sie, damit die Darstellung in Obsidian und auf GitHub funktioniert.

## Verarbeitungsstatus

Jede Notiz trägt im Frontmatter ein `status`-Feld:

| Status | Bedeutung |
|---|---|
| `neu` | Erfasst, noch nicht ins Knowledge-System eingearbeitet. |
| `verarbeitet` | Über `knowledge-ingest` eingearbeitet; `source_notiz:` verweist auf das Ergebnis in `80_Knowledge/Sources/`. |
| `ignoriert` | Geprüft, enthält keine wiederverwendbare Erkenntnis. Kurze Begründung im Feld `notiz:`. |

Alle offenen Quellen finden:

```powershell
Select-String -Path "00_Inbox/Quellen/*.md" -Pattern '^status: neu$' | Select-Object Path
```

## Erfassen

```powershell
npm run ingest:x -- <tweet-url-oder-id> [--thread] [--force] [--no-media]
```

Eine bestehende Notiz wird **nicht** überschrieben — so gehen manuelle Ergänzungen und ein bereits gesetzter Status nicht verloren. `--force` überschreibt bewusst und lädt auch die API-Antwort neu (kostet einen Request).

Der JSON-Cache unter `scripts/.ingest/` verhindert doppelte API-Calls und ist gitignored.

## Regeln

- Notizen hier werden inhaltlich nicht redigiert — sie sind das Rohmaterial. Kürzungen und Interpretation gehören in `80_Knowledge/`.
- Nichts löschen, solange `status: neu` steht.
- Enthält eine Quelle nichts Wiederverwendbares: `status: ignoriert` setzen statt löschen, damit dieselbe URL nicht erneut erfasst wird.
