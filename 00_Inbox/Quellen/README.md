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

**X (Twitter):**

```powershell
npm run ingest:x -- <tweet-url-oder-id> [--thread] [--force] [--no-media]
```

**TikTok:**

```powershell
npm run ingest:tiktok -- <video-url-oder-id> [--force] [--refetch] [--no-media] [--gap <sek>]
```

Eine bestehende Notiz wird **nicht** überschrieben — so gehen manuelle Ergänzungen und ein bereits gesetzter Status nicht verloren. `--force` überschreibt bewusst; `--refetch` holt zusätzlich die API-Antwort neu (kostet einen Request bzw. $0.001).

Der JSON-Cache unter `scripts/.ingest/` verhindert doppelte API-Calls und ist gitignored.

### Was TikTok-Notizen ausmacht

Das Transkript kommt vom Apify-Actor `scrape-creators/best-tiktok-transcripts-scraper` ($0.001 pro Video, `APIFY_TOKEN` in `.env.local`). Der Actor liefert trotz seiner Beschreibung **nur** das Transkript, keine Metadaten. Deshalb kommen die übrigen Felder aus zwei kostenlosen Quellen:

- **Veröffentlichungsdatum** aus der Video-ID — TikTok-IDs sind Snowflake-artig, die oberen 32 Bit sind der Unix-Timestamp. Lässt sich das Datum nicht ableiten, trägt die Notiz `datum_unsicher: true`.
- **Caption, Autorname, Cover** über TikTok oEmbed (ohne Key). Scheitert der Abruf, entsteht die Notiz trotzdem — nur ohne diese Felder.

Der gesprochene Text steht als Fließtext in der Notiz, getrennt in Absätze an Sprechpausen ab `--gap` (Default 0,4s). Die Spracherkennung von TikTok setzt keine Satzzeichen und verhaut regelmäßig Eigennamen und Zahlwörter — die Notiz trägt dazu einen Warnhinweis. Vor der Übernahme ins Knowledge-System gegen das Video prüfen.

Nicht jedes Video hat ein Transkript: TikTok erzeugt nicht überall Untertitel. Dann trägt die Notiz `transkript: "keins verfügbar"` und nur die Metadaten. Der Actor berechnet den Credit trotzdem.

**Übersetzte Untertitelspuren:** TikTok liefert zu manchen Videos statt des Originaltons eine maschinell ins Englische übersetzte Fassung — ein deutsches Video kommt dann als englischer Text zurück, mit deutscher Satzstellung („Anthropic hat die Claude Academy veröffentlicht" wird zu „1 Tropic has the cloud Academy published"). Der Actor kennt keinen Sprachparameter. Das Script misst deshalb die Sprache von Transkript und Caption und trägt `sprache:` ins Frontmatter; weichen beide ab, kommen `sprache_abweichung: true`, ein Warnblock in der Notiz und eine Warnung im Terminal dazu. Ein `--refetch` liefert manchmal die Originalspur (bei einem Video half es, bei einem anderen blieb es über drei Versuche englisch) — hilft es nicht, ist die Caption die verlässlichere Quelle.

## Regeln

- Notizen hier werden inhaltlich nicht redigiert — sie sind das Rohmaterial. Kürzungen und Interpretation gehören in `80_Knowledge/`.
- Nichts löschen, solange `status: neu` steht.
- Enthält eine Quelle nichts Wiederverwendbares: `status: ignoriert` setzen statt löschen, damit dieselbe URL nicht erneut erfasst wird.
