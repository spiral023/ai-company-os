# Quellen-Eingang

Roh erfasste externe Quellen, vollständig und unbearbeitet. Eingangsstufe vor `80_Knowledge/`.

## Struktur

```
00_Inbox/Quellen/
  X/
    2026-07-27-cerebras-2081828128952095022.md    ← Notiz mit Volltext
    medien/
      2026-07-27-cerebras-2081828128952095022/    ← Bilder dieser Quelle
  TikTok/
  YouTube/
  URL/
  PDF/
    dateien/                                            ← lokal gespeicherte Remote-PDFs
```

Die Ingest-Scripts wählen den Typordner automatisch. X verwendet den Slug `<Veröffentlichungsdatum>-<Handle>-<ID>`, TikTok dagegen `<Veröffentlichungsdatum>-<Handle>-<gekürzter Titel>`. URL, YouTube und PDF ergänzen ebenfalls einen gekürzten Titel. TikToks bleiben über `video_id` im Frontmatter eindeutig; nur bei einer seltenen Dateinamenskollision ergänzt das Script einen kurzen ID-Suffix. `Sonstige/` ist der kontrollierte Fallback für einen künftig unbekannten technischen Typ.

| Quelle | Zielordner | Abruf |
|---|---|---|
| X/Twitter | `X/` | `npm run ingest:x -- <url> --thread` |
| TikTok | `TikTok/` | `npm run ingest:tiktok -- <url>` |
| YouTube | `YouTube/` | `python ai.py ingest <url>` |
| Website/Artikel | `URL/` | `python ai.py ingest <url>` |
| PDF | `PDF/` | `python ai.py ingest <url-oder-pfad>` |

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
Get-ChildItem "00_Inbox/Quellen" -Filter "*.md" -File -Recurse |
  Select-String -Pattern '^status: neu$' |
  Select-Object Path
```

## Erfassen

**Artikel, YouTube und PDF:**

```powershell
python ai.py ingest <url-oder-pdf-pfad> [--force] [--no-media]
```

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

### Woher das Veröffentlichungsdatum kommt

Für Artikel sucht `ingest_source.py` das Datum in dieser Reihenfolge: erklärtes Veröffentlichungsdatum in den Meta-Tags (`article:published_time`, `datePublished`), dann JSON-LD (`<script type="application/ld+json">`, wo Substack und viele CMS es ausschließlich führen), dann ein `<time datetime>`, zuletzt `og:updated_time`. Das Änderungsdatum steht bewusst am Ende — laufend gepflegte Doku-Seiten datieren damit auf heute statt auf ihr Erscheinen.

Findet keine dieser Quellen etwas, steht im Feld `datum:` der Abruftag, damit Slug und Sortierung funktionieren, und die Notiz trägt zusätzlich `datum_unsicher: true`. Dieses Feld ist das Signal, das Datum vor einem Zitat oder einer Aktualitätsaussage gegen die Quelle zu prüfen. Ohne die Markierung liest sich der Abruftag wie ein belegtes Veröffentlichungsdatum — genau das war vorher der Fall. Reine Dokumentationsseiten (`docs.anthropic.com`, `unsloth.ai/docs`) führen typischerweise kein Datum und bekommen die Markierung deshalb regelmäßig.

### Was YouTube-Notizen ausmacht

Das Script übernimmt die Videobeschreibung und eine vorhandene deutsche oder englische Untertitelspur. Das Transkript wird ohne Zeitstempel zu lesbaren Absätzen verbunden; die ursprünglichen Untertitel-Segmente werden nur als Anzahl im Frontmatter dokumentiert. Titel, Kanal und Veröffentlichungsdatum kommen ohne API-Key von YouTube.

Bei `transkript_generiert: ja` handelt es sich um automatische Spracherkennung. Eigennamen, Produktnamen und Fachbegriffe können falsch sein und werden im Roharchiv nicht stillschweigend korrigiert. Vor Zitaten oder der Übernahme kritischer Aussagen ins Knowledge-System den Inhalt gegen das Video prüfen. Stellt YouTube keine Untertitelspur bereit, bricht der Abruf mit einer klaren Meldung ab.

### Was TikTok-Notizen ausmacht

Das Transkript kommt vom Apify-Actor `scrape-creators/best-tiktok-transcripts-scraper` ($0.001 pro Video, `APIFY_TOKEN` in `.env.local`). Der Actor liefert trotz seiner Beschreibung **nur** das Transkript, keine Metadaten. Deshalb kommen die übrigen Felder aus zwei kostenlosen Quellen:

- **Veröffentlichungsdatum** aus der Video-ID — TikTok-IDs sind Snowflake-artig, die oberen 32 Bit sind der Unix-Timestamp. Lässt sich das Datum nicht ableiten, trägt die Notiz `datum_unsicher: true`.
- **Caption, Autorname, Cover** über TikTok oEmbed (ohne Key). Scheitert der Abruf, entsteht die Notiz trotzdem — nur ohne diese Felder.

Der gesprochene Text steht als Fließtext in der Notiz, getrennt in Absätze an Sprechpausen ab `--gap` (Default 0,4s). `transkript: automatisch` im Frontmatter kennzeichnet die automatische Spracherkennung; der immer gleiche Warnblock wird nicht in jede Notiz kopiert. Eigennamen und Zahlwörter können trotzdem falsch sein und müssen vor Zitaten gegen das Video geprüft werden.

Nicht jedes Video hat ein Transkript: TikTok erzeugt nicht überall Untertitel. Dann trägt die Notiz `transkript: nicht verfügbar`; ein leerer Transkript-Abschnitt wird nicht angelegt. Der Actor berechnet den Credit trotzdem.

Die Notizen vermeiden abruftechnischen Boilerplate: URL, Video-ID, Hashtags und Transkriptstatus stehen einmal im Frontmatter; Hashtags werden nicht zusätzlich im Fließtext wiederholt. Eine Caption erscheint nur, wenn sie über den bereits verwendeten Titel hinausgeht. Spezifische Qualitätswarnungen wie eine erkannte Rückübersetzung bleiben direkt an der betroffenen Quelle stehen.

**Übersetzte Untertitelspuren:** TikTok liefert zu manchen Videos statt des Originaltons eine maschinell ins Englische übersetzte Fassung — ein deutsches Video kommt dann als englischer Text zurück, mit deutscher Satzstellung („Anthropic hat die Claude Academy veröffentlicht" wird zu „1 Tropic has the cloud Academy published"). Der Actor kennt keinen Sprachparameter. Das Script misst deshalb die Sprache von Transkript und Caption und trägt `sprache:` ins Frontmatter; weichen beide ab, kommen `sprache_abweichung: true`, ein Warnblock in der Notiz und eine Warnung im Terminal dazu. Ein `--refetch` liefert manchmal die Originalspur (bei einem Video half es, bei einem anderen blieb es über drei Versuche englisch) — hilft es nicht, ist die Caption die verlässlichere Quelle.

### Mehrteilige Sammlungen: AI Coding Dictionary

Das [AI Coding Dictionary](https://www.aihero.dev/ai-coding-dictionary) von Matt Pocock liegt als eigener Ordner unter `URL/aihero-ai-coding-dictionary/`: `00-index.md` mit allen Begriffen und Kurzdefinitionen, darunter ein Unterordner pro Sektion (`01-the-model/`, `03-tools-environment/` …), wie auf der Website. Quelle ist nicht die Website, sondern der Klon `external_repos/mattpocock/dictionary-of-ai-coding/`. Dort liegen die Einträge als Original-Markdown vor, dazu die Sektionsreihenfolge in `internal/Curriculum.md`.

```powershell
git -C external_repos/mattpocock/dictionary-of-ai-coding pull --ff-only
python 70_Scripts/sync_ai_coding_dictionary.py [--dry-run]
```

- Nur `00-index.md` trägt `status`. Die Sammlung wird als *eine* Quelle verarbeitet, nicht als 71.
- Die Querverweise zwischen Begriffen schreibt das Script auf relative Pfade zwischen den Sektionsordnern um. Wiki-Links werden bewusst nicht verwendet, weil Dateinamen wie `Agent.md` oder `Skill.md` im Vault kollidieren könnten.
- Begriffsdateien sind reine Spiegel: Ändert sich ein Eintrag im Repo, schreibt der nächste Lauf ihn neu. Im Index bleiben `status`, `source_notiz`, `notiz` und `erfasst` erhalten. Entfernte Begriffe meldet das Script nur, es löscht sie nicht.
- **Nur lokal, nicht versioniert:** Das Dictionary-Repo hat keine Lizenzdatei (alle Rechte vorbehalten), dieses Repo ist öffentlich. Der Ordner steht deshalb in `.gitignore`. In Obsidian bleibt er sichtbar. Auf einem neuen Rechner erst das Repo klonen, dann das Script ausführen. Inhalte nicht wörtlich in eigene, versionierte Artefakte übernehmen.

## Regeln

- Notizen hier werden inhaltlich nicht redigiert — sie sind das Rohmaterial. Kürzungen und Interpretation gehören in `80_Knowledge/`.
- Nichts löschen, solange `status: neu` steht.
- Enthält eine Quelle nichts Wiederverwendbares: `status: ignoriert` setzen statt löschen, damit dieselbe URL nicht erneut erfasst wird.
