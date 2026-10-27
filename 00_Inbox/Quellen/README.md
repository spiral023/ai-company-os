# Quellen-Eingang

Roh erfasste externe Quellen mit unverändertem Originaltext der ausgewählten Inhalte. Eingangsstufe vor `80_Knowledge/`. Bei X bilden Hauptpost und belegte Fortsetzungen die Quelle; die Gesprächsauswahl ist im [X-Playbook](../../30_Skills/local/knowledge-ingest/references/quellen-playbooks.md#xtwitter) beschrieben.

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

RSS-/Atom-Feeds werden unter `00_Inbox/Feeds/feeds.yaml` registriert. `python ai.py feeds check` zeigt noch nicht archivierte Einträge; ausgewählte Artikel werden über den folgenden Artikel-Ingest erfasst. Details: [Feed-Verwaltung](../Feeds/README.md).

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
npm run ingest:tiktok -- <video-url-oder-id> [--force] [--refetch] [--no-media] [--no-video] [--gap <sek>]
```

Eine bestehende Notiz wird **nicht** überschrieben — so gehen manuelle Ergänzungen und ein bereits gesetzter Status nicht verloren. `--force` überschreibt bewusst; `--refetch` holt zusätzlich die API-Antwort neu (kostet einen Request bzw. $0.001).

Der JSON-Cache unter `scripts/.ingest/` verhindert doppelte API-Calls und ist gitignored.

X-Threads werden vor Speicherung und beim Lesen älterer Caches nach Autor und Antwortkette gefiltert. `thread_posts` zählt die übernommenen Posts, nicht alle Antworten und nicht die Vollständigkeit eines Threads. Bestehende Notizen können mit `node scripts/clean-x-threads.mjs` ohne Netzwerk geprüft werden; `--apply` übernimmt die Vorschau mit Sicherungen und Prüfbericht unter `tmp/quellen-lauf/` und erhält Verarbeitungsstatus sowie manuelle Ergänzungen.

### Woher das Veröffentlichungsdatum kommt

Für Artikel sucht `ingest_source.py` das Datum in dieser Reihenfolge: erklärtes Veröffentlichungsdatum in den Meta-Tags (`article:published_time`, `datePublished`), dann JSON-LD (`<script type="application/ld+json">`, wo Substack und viele CMS es ausschließlich führen), dann ein `<time datetime>`, zuletzt `og:updated_time`. Das Änderungsdatum steht bewusst am Ende — laufend gepflegte Doku-Seiten datieren damit auf heute statt auf ihr Erscheinen.

Findet keine dieser Quellen etwas, steht im Feld `datum:` der Abruftag, damit Slug und Sortierung funktionieren, und die Notiz trägt zusätzlich `datum_unsicher: true`. Dieses Feld ist das Signal, das Datum vor einem Zitat oder einer Aktualitätsaussage gegen die Quelle zu prüfen. Ohne die Markierung liest sich der Abruftag wie ein belegtes Veröffentlichungsdatum — genau das war vorher der Fall. Reine Dokumentationsseiten (`docs.anthropic.com`, `unsloth.ai/docs`) führen typischerweise kein Datum und bekommen die Markierung deshalb regelmäßig.

### Was YouTube-Notizen ausmacht

Das Script übernimmt die Videobeschreibung und eine vorhandene deutsche oder englische Untertitelspur. Das Transkript wird ohne Zeitstempel zu lesbaren Absätzen verbunden; die ursprünglichen Untertitel-Segmente werden nur als Anzahl im Frontmatter dokumentiert. Titel, Kanal und Veröffentlichungsdatum kommen ohne API-Key von YouTube.

Bei `transkript_generiert: ja` handelt es sich um automatische Spracherkennung. Eigennamen, Produktnamen und Fachbegriffe können falsch sein und werden im Roharchiv nicht stillschweigend korrigiert. Vor Zitaten oder der Übernahme kritischer Aussagen ins Knowledge-System den Inhalt gegen das Video prüfen. Sind Untertitel deaktiviert oder fehlt eine nutzbare Spur, versucht der Import automatisch die lokale Audio-Transkription. `python ai.py ingest <URL> --no-whisper` schaltet diesen Fallback ab.

`RequestBlocked` und `IpBlocked` bedeuten dagegen einen blockierten Abruf, nicht nachgewiesen fehlende Untertitel. Bei einer solchen Meldung weitere automatische Batch-Aufrufe anhalten. Eine Bot-Abfrage kann auch mit HTTP 200 und dem Playerstatus `LOGIN_REQUIRED` erscheinen; ein erfolgreicher Seitenabruf allein bestätigt keinen Zugriff auf Untertitel oder Audio.

### YouTube-Untertitel über den verbundenen Browser erfassen

Wenn der direkte Abruf blockiert ist, kann die Originalseite im bereits verbundenen normalen Chrome-Browser weiterhin funktionieren. Im Quellenlauf vom 22.10.2026 gelang so der integrierte Transkript-Export für acht Videos, während Python- und Audio-Abruf blockiert blieben. Das ist ein geprüfter alternativer Erfassungsweg, keine Zusage dauerhafter Verfügbarkeit.

1. Originalvideo öffnen und die Video-ID mit dem Auftrag abgleichen.
2. Beschreibung aufklappen und das konkrete Veröffentlichungsdatum, Titel und Kanal erfassen; relative Altersangaben nicht als Datum umrechnen.
3. Den integrierten YouTube-Transkript-Export des Browserwerkzeugs verwenden. Sitzungscookies müssen dafür nicht exportiert oder an CLI-Werkzeuge übertragen werden.
4. Den unveränderten UTF-8-Export mit Video-ID, Sprache, Kennzeichnung der Erzeugung und Zeitmarken unter `YouTube/medien/<slug>/transkript-browser.txt` aufbewahren. Die Rohnotiz enthält wie üblich lesbare Absätze ohne Zeitmarken und verlinkt den Export.
5. Sprache und Herkunft ausdrücklich markieren: Der Export kann eine deutsche automatisch erzeugte Spur eines ursprünglich englischen, automatisch synchronisierten Videos wählen. Dann `originalsprache: en`, `sprache_abweichung: true` und einen erklärenden Hinweis setzen. Diese Fassung ist kein wortgetreues englisches Original und taugt ohne Originalabgleich nicht für Zitate.
6. Erst nach Erfassung des Untertitelinhalts verarbeiten. Bei fehlendem Inhalt `status: neu` und `transkript: nicht verfügbar` erhalten; keine Aussagen aus Titel oder Suchtreffern rekonstruieren.

Diagnose und aktuelle Primärdokumentation: [Quellenlauf und Abrufdiagnose vom 22.10.2026](../../reports/2026-10-22-youtube-quellenimport.md).

### Fehlende YouTube- und TikTok-Transkripte lokal nachholen

`python ai.py transkribieren <Video-ID-oder-URL>` ergänzt fehlende Transkripte mit `faster-whisper` auf der lokalen NVIDIA-GPU. Für YouTube lädt der Befehl die Tonspur mit `yt-dlp`; für TikTok verwendet er das bereits archivierte `medien/<slug>/02-video.mp4`. Der Standard ist `large-v3` mit Float16. Sprache und Zeitstempel werden automatisch erkannt. Das Modell wird einmal heruntergeladen; die lokale Transkription benötigt keinen API-Key oder kostenpflichtigen Dienst.

Beim regulären Import startet der Fallback für tatsächlich fehlende YouTube-Untertitel beziehungsweise fehlende TikTok-Untertitel mit verfügbarem lokalen Video. Eine YouTube-Abrufsperre wie `RequestBlocked` löst ihn **nicht** automatisch aus: Sie belegt keine fehlenden Untertitel. In diesem Fall den Zugriff klären und gegebenenfalls den expliziten Befehl mit einer verfügbaren Tonspur verwenden. Fehlen GPU, Umgebung oder Audio oder scheitert die Erkennung, wird der Fehler gemeldet und kein erfolgreiches Transkript eingetragen.

Die optionale Python-Umgebung getrennt einrichten (Windows mit CUDA 12):

```powershell
uv venv --python 3.12 .venv/youtube-transcription
uv pip install --python .venv/youtube-transcription/Scripts/python.exe "faster-whisper==1.2.1" "av==18.0.0" "nvidia-cublas-cu12==12.9.2.10" "nvidia-cudnn-cu12==9.27.0.42" "yt-dlp[default]==2026.10.21" pyyaml
python ai.py transkribieren 2EoNRuFJfBo
python ai.py transkribieren https://www.tiktok.com/@autor/video/1234567890123456789
```

Für den YouTube-Abruf wird zusätzlich Node.js ab Version 22 oder Deno ab Version 2.3 im `PATH` benötigt. Die Routine aktiviert beide unterstützten Laufzeiten; die passende EJS-Komponente wird mit `yt-dlp[default]` installiert ([yt-dlp-Anleitung](https://github.com/yt-dlp/yt-dlp/wiki/EJS)).

Liefert der direkte Audio-Download HTTP 403, kann `python ai.py transkribieren <ID> --hls` eine alternative HLS-Tonspur verwenden. Die Dauer wird aus den decodierten Audio-Frames bestimmt, damit fehlende Container-Zeitstempel den Abruf nicht verhindern. Vor dem Schreiben wird sie mit der YouTube-Videodauer verglichen; eine Abweichung über drei Sekunden stoppt die Ergänzung.

Mehrere YouTube-/TikTok-IDs oder URLs sind zulässig; zwischen Videos liegt eine Pause von zehn Sekunden. Bei einem Fehler stoppt der Lauf. Erneutes Ausführen nutzt den Cache unter `tmp/youtube-transcription/` und überspringt vorhandene Transkripte, auch kurze Untertitel. `--audio <Datei>` verwendet für genau ein Video eine vorhandene Audio- oder Videodatei. Für TikTok muss die Rohnotiz bereits existieren; fehlt die MP4, zuerst den Video-Ingest ohne `--no-video` ausführen.

Umgebung, Audio, Modell und Laufzeitcache bleiben lokal und gitignored; für `large-v3` mehrere GB freien Speicher vorhalten. TikTok erhält zusätzlich `medien/<slug>/transkript-whisper.json` mit Zeitstempeln, Sprache, Modellversion und Hash der verwendeten Datei. `transkript_datei:` verlinkt dieses überprüfbare Textartefakt. Damit lässt sich der Whisper-Text von einer Plattform-Untertitelspur unterscheiden.

Der Befehl ergänzt fehlende Transkripte erst nach erfolgreicher Verarbeitung. Beschreibung, Veröffentlichungsdatum, Bearbeitungsstatus, Source-Verweise und manuelle Hinweise bleiben erhalten. `transkript_quelle: lokale Audio-Transkription`, Modell, Werkzeugversion und Erfassungsdatum kennzeichnen die Herkunft. Besteht schon eine Knowledge-Source ohne Rohnotiz, wird die neue Rohnotiz mit ihr verknüpft. Das Nachholen erzeugt keine neuen Knowledge-Artikel oder Patterns. Die Regeln zur Prüfung automatischer Spracherkennung gelten weiterhin.

### Was TikTok-Notizen ausmacht

Videos werden beim Ingest zusätzlich als `medien/<slug>/02-video.mp4` lokal gespeichert und in der Rohquelle verlinkt. Der Download nutzt `yt-dlp` ohne zusätzliche API-Gebühren. Einmal installieren: `python -m pip install --user "yt-dlp[default,curl-cffi]"`. Bei abweichendem Python-Pfad kann `TIKTOK_PYTHON` auf den Interpreter zeigen. `--no-video` überspringt nur die MP4, `--no-media` überspringt Cover und Video.

Ein erneuter Ingest derselben URL lädt ein fehlendes Video nach und ergänzt den Medien-Link oder ein noch fehlendes Transkript; Verarbeitungsstatus, Source-Verweis, vorhandene Untertitel und manuelle Ergänzungen bleiben erhalten. Vorhandene MP4s werden wiederverwendet. Download-Fehler werden gemeldet, während Metadaten und Transkript weiter archiviert werden können. MP4s und unvollständige Downloads sind gitignored und damit nur auf dem jeweiligen Rechner verfügbar. Auf einem neuen Rechner die betreffende URL erneut ingestieren. TikTok kann den Abruf einzelner Videos blockieren oder das Video entfernen.

Das Transkript kommt vom Apify-Actor `scrape-creators/best-tiktok-transcripts-scraper` ($0.001 pro Video, `APIFY_TOKEN` in `.env.local`). Der Actor liefert trotz seiner Beschreibung **nur** das Transkript, keine Metadaten. Deshalb kommen die übrigen Felder aus zwei kostenlosen Quellen:

- **Veröffentlichungsdatum** aus der Video-ID — TikTok-IDs sind Snowflake-artig, die oberen 32 Bit sind der Unix-Timestamp. Lässt sich das Datum nicht ableiten, trägt die Notiz `datum_unsicher: true`.
- **Caption, Autorname, Cover** über TikTok oEmbed (ohne Key). Scheitert der Abruf, entsteht die Notiz trotzdem — nur ohne diese Felder.

Der gesprochene Text steht als Fließtext in der Notiz, getrennt in Absätze an Sprechpausen ab `--gap` (Default 0,4s). `transkript: automatisch` im Frontmatter kennzeichnet die automatische Spracherkennung; der immer gleiche Warnblock wird nicht in jede Notiz kopiert. Eigennamen und Zahlwörter können trotzdem falsch sein und müssen vor Zitaten gegen das Video geprüft werden.

Liefert der Actor keine nutzbaren Untertitel, versucht der Ingest die lokale MP4 mit Whisper zu transkribieren. `npm run ingest:tiktok -- <URL> --no-whisper` deaktiviert diesen Schritt. Ohne lokale Tonspur oder bei einem fehlgeschlagenen Whisper-Lauf bleibt `transkript: nicht verfügbar` erhalten; ein leerer Transkript-Abschnitt wird nicht angelegt. Der Actor kann seinen Credit auch ohne Untertitel berechnen. Ein lokaler Fallback lädt keine Apify-Credits nach und startet keinen zweiten Actor-Run.

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
