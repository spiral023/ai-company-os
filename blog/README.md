# Blog (ai-blog.sp23.online)

Statischer Blog aus Markdown, gespeist aus der Wissensbasis (`80_Knowledge/`). Der Generator `build_blog.py` erzeugt Seiten, RSS-Feeds und Sitemap.

## Ablauf

1. **Entwurf schreiben** (Skill `blog-schreiben`): `blog/posts/YYYY-MM-DD-<slug>.md` mit `status: entwurf`.
2. **Vorschau:** `python blog/build_blog.py --drafts`, danach `blog/_preview/` lokal öffnen (`python -m http.server -d blog/_preview 8000`).
3. **Freigabe:** `python blog/build_blog.py --auto-freigeben` gibt jeden Entwurf frei, der alle Prüfungen ohne Fehler und Hinweise besteht. Er erscheint sofort mit dem nächsten Build und Deployment (Beschluss Philipp, 07.10.2026; bis dahin galt der Folgetag). Zurückhalten lässt er sich mit `status: entwurf` oder einem späteren Datum. Einzeln freigeben: `--freigeben <slug>`. Vermerke im Frontmatter: `geprueft_am`, bei Automatik `freigabe: automatisch`. Entwürfe mit Hinweisen bleiben liegen.
4. **Build:** `python blog/build_blog.py` schreibt `blog/_site/`. Nur freigegebene Beiträge landen in Seite und Feed.
5. **Deployment** nach ai-blog.sp23.online: Cloudflare Worker mit Static Assets (`blog/wrangler.jsonc`). Testseite: `cd blog && wrangler deploy --assets ./_probe`, produktiv: `python build_blog.py && wrangler deploy`.

## Frontmatter

```yaml
---
titel: "Konkreter Titel"
datum: 2026-09-29
kategorie: modelle          # modelle | arbeitsweisen | tools | duell | check | digest | prompts | kurz | redaktion (ohne Quellen)
zusammenfassung: "Ein bis zwei Sätze für Liste, Feed und Suchmaschinen."
status: entwurf             # entwurf | freigegeben
aktualisiert: 2026-10-05    # optional; erscheint in Meta-Zeile und Schema.org
pruefen_bis: 2026-11-01     # optional; danach meldet der Build „Zahlen erneut prüfen“
geprueft_am: 2026-09-30     # setzt --freigeben; Pflicht bei status: freigegeben
quellen:                    # Pflicht; Namen von Source-Notizen in 80_Knowledge/Sources/
  - 2026-09-22-artificialanlys-2102438210798514391
---
```

Im Text: `{q:2}` verweist auf die zweite Quelle. Die Prüfung verlangt es, angezeigt wird es nicht (`quellenverweise_im_text: false` in `site.yaml`), die Quellenliste steht am Ende. `[Text](post:<slug>)` verlinkt einen anderen Beitrag. `## Kurz gesagt` wird zur Box, bei mehr als vier Abschnitten und 600 Wörtern entsteht ein Inhaltsverzeichnis. Unter jedem Beitrag stehen „Weiterlesen“ (gemeinsame Quellen, gleiche Kategorie) und ein Abo-Hinweis. Die Seite „Über“ kommt aus `ueber:` in `site.yaml`.

Quellenangaben (Titel, Autor, Datum, Original-URL) erzeugt der Generator aus den Source-Notizen. Wiki-Links in Doppelklammern sind im Text nicht erlaubt.

## Glossar

`blog/glossar.yaml` enthält die Fachbegriffe (Begriff, Aliase, Erklärung, „Siehe auch“). Der Generator erzeugt daraus die Seite `/glossar/` (mit Schema.org `DefinedTermSet`) und verlinkt in jedem Beitrag die **erste Nennung** eines Begriffs mit Tooltip. Überschriften, Links, Code und Fußnotenmarken bleiben unverlinkt, Pluralformen (s, n, en, es) werden erkannt.

Die Erklärungen sind eigene Texte. Die Begriffsauswahl orientiert sich am AI Coding Dictionary von Matt Pocock, das keine Lizenzangabe hat: Es werden keine Definitionen übernommen oder übersetzt. Unter `beobachten:` stehen Fachbegriffe, die ohne Glossareintrag nicht im Fließtext vorkommen dürfen. `--check` schlägt dann an.

## Prüfungen

`python blog/build_blog.py --check` bricht ab bei fehlenden Pflichtfeldern, unbekannter Kategorie, fehlender Quelle, Wiki-Links, ungültigen `{q:n}`- oder `post:`-Verweisen, fehlendem Abschnitt „Kurz gesagt“ (außer Kurzmeldung) sowie bei Fehlern im Glossar (doppelte Schreibweise, unbekannter „Siehe auch“-Verweis, interne Begriffe) und Fachbegriffen aus `beobachten:` ohne Eintrag sowie bei Stilfehlern: interne Begriffe (Notiz, Pattern, Konfidenz, Wiki), ISO-Daten im Fließtext, Dollar-Beträge mit Dezimalpunkt, fehlendes Leerzeichen nach Satzende.

Zusätzlich gilt:

- **Jede Quelle muss zitiert werden.** Eine Quelle in `quellen:` ohne `{q:n}` im Text ist ein Fehler.
- **Quellen werden für alle Beiträge aufgelöst**, auch für Entwürfe. Ein Tippfehler im Namen fällt sofort auf.
- **Slug eindeutig, keine toten Links.** Ein freigegebener Beitrag darf nur auf Beiträge verlinken, die ebenfalls sichtbar sind.
- **Hinweise (kein Abbruch):** Absätze mit Zahlen, aber ohne `{q:n}`, erscheinen unter „HINWEISE“. Die Box „Kurz gesagt“ ist ausgenommen.
- **Platzhalter blockieren den öffentlichen Build.** `[hier ergänzen …]`, `TODO` und die Platzhalter „sp23“ in `site.yaml` lassen `python blog/build_blog.py` scheitern. `--check` und `--drafts` melden sie nur.
- **Blogstil:** Wörter wie „belegt“, „unbelegt“, „Belegstärke“, „Primärquelle“ im Text erscheinen als Hinweis.
- **Weitere Hinweise:** unbekannte Frontmatter-Felder (Tippfehler), überschrittenes `pruefen_bis`, „Kurz gesagt“ mit weniger als 2 oder mehr als 4 Stichpunkten.
- Die Navigation zeigt nur Kategorien mit sichtbaren Beiträgen.
- **CI:** `.github/workflows/blog.yml` führt Tests und `--check` bei Änderungen aus und baut täglich als Artefakt. Deployment gibt es noch nicht.

## Lebende Seite „Modelle und Preise“

`/modelle-und-preise/` entsteht bei jedem Build aus dem Fakten-Register (`80_Knowledge/Fakten/Modelle-und-Preise.md`, Konfiguration in `site.yaml` unter `modelle_preise`). Neue Angaben kommen als Zeile ins Register, danach `python blog/build_blog.py` und Deployment. Die Seite zeigt Stand-Datum (Zeile `**Stand:**` im Register), Filter und Quellenliste.

- Der Build bricht ab bei fehlender Quelle, ungültigem Datum, fehlendem Stand oder internen Begriffen (Notiz, Pattern, Wiki …) in den Zellen.
- `--check` meldet einen Hinweis, wenn der Stand älter als 14 Tage ist.
- Für Leser wird die Schreibweise angepasst: kein Code-Format, Datum als TT.MM.JJJJ, Dollarbeträge mit Komma.
- Code: `blog/fakten_seite.py`. Weitere lebende Seiten (Arbeitsweisen A bis Z, Behauptungs-Register) folgen demselben Muster.

Tests: `python -m pytest tests/test_build_blog.py`

## Abhängigkeiten

`pip install markdown-it-py pyyaml`
