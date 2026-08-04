# Artikel-Format für Source-Notizen

Gilt für Notizen in `80_Knowledge/Sources/`. Maßgeblich für Pflichtfelder und Invarianten bleibt `80_Knowledge/README.md`; diese Referenz beschreibt Aufbau, Sprache und Bildbehandlung der redaktionellen Zusammenfassung.

## Grundidee

Seit die Rohquellen in `00_Inbox/Quellen/` vollständig archiviert werden, ist die Source-Notiz **nicht mehr das Rohtext-Archiv**, sondern die redaktionelle deutsche Aufarbeitung. Der Originaltext wird nicht kopiert — das Feld `rohquelle:` verweist darauf.

Das trennt die Aufgaben sauber: Die Inbox hält das Unveränderliche, die Source-Notiz das Verständliche, die Patterns das Übertragbare.

## Frontmatter

```yaml
---
url: <normalisierte Canonical-URL>
autor: <Handle oder Name, wie die Quelle ihn führt>
datum: <YYYY-MM-DD der Original-Veröffentlichung>
erfasst: <YYYY-MM-DD des Ingests>
typ: tweet | artikel | repo | video | notiz
rohquelle: 00_Inbox/Quellen/<slug>.md
---
```

`url`, `autor`, `datum`, `erfasst` und `typ` sind Pflicht — der Validator bricht sonst ab. `rohquelle` ist neu und verweist auf das Archiv.

**Typ-Mapping** von der Inbox in die Source-Notiz (die Inbox nutzt technische Typen, der Validator akzeptiert nur diese fünf):

| Inbox `typ` | Source `typ` |
|---|---|
| `tweet` | `tweet` |
| `artikel` (X-Artikel) | `artikel` |
| `url` | `artikel` |
| `youtube` | `video` |
| `pdf` | `artikel`, bei internen Dokumenten `notiz` |
| GitHub-Repo | `repo` |

## Aufbau

Reihenfolge nach Lernlogik, nicht nach Quellenreihenfolge:

```markdown
# <Aussagekräftiger deutscher Titel — nicht der Originaltitel übersetzt>

<Ein Absatz Einstieg: Worum geht es, warum ist es relevant, was ist die Kernaussage.
Kein „In diesem Artikel wird …" — direkt in die Sache.>

## <Fachliche Überschrift>

<Erklärung mit Belegen. Zahlen konkret nennen. Bilder an der Stelle einfügen,
wo der Text sie braucht.>

![Beschreibender Alt-Text](../../00_Inbox/Quellen/medien/<slug>/02-photo.jpg)

## Einordnung

<Deine fachliche Bewertung als AI Engineer, klar getrennt von den Aussagen der
Quelle: Was ist belastbar, was ist selbstberichtet, was widerspricht dem Bestand,
was kostet die Arbeitsweise. Dieser Abschnitt ist Pflicht.>

## Kernaussagen

- <Aussage 1> → [[Pattern-Name]]
- <Aussage 2> → [[Pattern-Name]]

## Verbindungen

- [[Verwandtes Pattern]]
- [[Andere Source-Notiz zum gleichen Thema]]
```

`## Kernaussagen` ist Pflicht (Invariante 4: jede Aussage muss einem Beleg zuordenbar sein). `## Einordnung` ist Pflicht, weil sie die Fachbewertung von der Wiedergabe trennt. `## Verbindungen` mit mindestens zwei Wiki-Links, sobald thematisch benachbarte Notizen existieren.

## Länge

Nach Substanz, nicht nach Schema. Ein Tweet mit einer Erkenntnis braucht 200 Wörter, ein 7.000-Zeichen-Artikel mit sechs Charts braucht 800 bis 1.200. Verdichten heißt: Begründungen, Einschränkungen und Zahlen behalten, Wiederholungen und Füllsätze streichen.

Nie mechanisch Abschnitt für Abschnitt paraphrasieren. Wenn die Quelle schlecht strukturiert ist, strukturiert die Notiz um.

## Sprache

- Professionelles, natürliches Deutsch. Du-Ansprache, wenn die Notiz Handlungsempfehlungen gibt.
- Englische Fachtermini im Original: Context Window, Tool Calling, Harness, Prompt, Eval, Token, Rate-Limit, Subagent. Keine erzwungenen Eindeutschungen.
- Echte Umlaute und `ß`. Niemals ASCII-Ersatz.
- Deutsche Anführungszeichen ausschließlich als `„…"` (U+201E öffnend, U+201C schließend). **Nie gemischt mit ASCII `"`** — das ist der häufigste Validator-Fehler im Repo.
- Code, Flags, Pfade, Modellnamen und Preise in Backticks.
- Zitate sparsam und kurz; sonst paraphrasieren.

## Bilder

Die Bilder liegen bereits lokal unter `00_Inbox/Quellen/medien/<slug>/`. Sie werden **nicht kopiert**, sondern relativ referenziert:

```markdown
![Chart: Intelligence-Index gegen Kosten pro Task](../../00_Inbox/Quellen/medien/2026-07-27-cerebras-2081828128952095022/02-photo.jpg)
```

Regeln:

- **Bilder vor dem Referenzieren lesen.** Charts und Tabellen enthalten regelmäßig Werte, die im Text fehlen. Diese Zahlen gehören in den Fließtext, nicht nur ins Bild — ein Leser der Notiz soll die Aussage ohne Bildbetrachtung verstehen.
- Nur Bilder mit Erklärwert übernehmen: Diagramme, Benchmarks, Screenshots mit Aussage. Header-Grafiken, Logos und Deko weglassen.
- Alt-Text beschreibt Inhalt und Zweck, nicht die Datei. Statt „Bild 2" also „Chart: Kosten pro Task gegen Intelligence-Index".
- Bild dort platzieren, wo der zugehörige Text steht — nicht alle am Anfang sammeln.
- Nur auf Dateien verweisen, die tatsächlich existieren. Zeigt die Inbox-Notiz `⚠️ nicht lokal gespeichert`, stattdessen die Remote-URL verlinken oder den Inhalt beschreiben.

## Was nicht hineingehört

- Der Originaltext der Quelle (liegt in der Inbox).
- Erfundene Präzision: Wenn die Quelle „deutlich schneller" sagt, wird daraus keine Prozentzahl.
- Eigenes Fachwissen als Aussage der Quelle. Einordnung gehört in `## Einordnung` und wird sprachlich als Bewertung markiert.
- Selbstberichtete Benchmarks ohne Kennzeichnung. Wer im eigenen Harness gemessen hat, hat nicht neutral gemessen — das gehört dazugeschrieben.
