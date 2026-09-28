# Blog (blog.sp23.online)

Statischer Blog aus Markdown, gespeist aus der Wissensbasis (`80_Knowledge/`). Der Generator `build_blog.py` erzeugt Seiten, RSS-Feeds und Sitemap.

## Ablauf

1. **Entwurf schreiben** (Skill `blog-schreiben`): `blog/posts/YYYY-MM-DD-<slug>.md` mit `status: entwurf`.
2. **Vorschau:** `python blog/build_blog.py --drafts`, danach `blog/_preview/` lokal öffnen (`python -m http.server -d blog/_preview 8000`).
3. **Freigabe:** Philipp setzt `status: freigegeben` (das Datum darf in der Zukunft liegen; dann erscheint der Beitrag erst ab diesem Tag).
4. **Build:** `python blog/build_blog.py` schreibt `blog/_site/`. Nur freigegebene Beiträge landen in Seite und Feed.
5. **Deployment** nach blog.sp23.online: noch offen (Hosting-Entscheidung).

## Frontmatter

```yaml
---
titel: "Konkreter Titel"
datum: 2026-09-29
kategorie: modelle          # modelle | arbeitsweisen | tools | duell | check | digest | kurz
zusammenfassung: "Ein bis zwei Sätze für Liste, Feed und Suchmaschinen."
status: entwurf             # entwurf | freigegeben
quellen:                    # Pflicht; Namen von Source-Notizen in 80_Knowledge/Sources/
  - 2026-09-22-artificialanlys-2102438210798514391
---
```

Quellenangaben (Titel, Autor, Datum, Original-URL) erzeugt der Generator aus den Source-Notizen. Wiki-Links in Doppelklammern sind im Text nicht erlaubt.

## Prüfungen

`python blog/build_blog.py --check` bricht ab bei fehlenden Pflichtfeldern, unbekannter Kategorie, fehlender Quelle oder Wiki-Links im Text.

## Abhängigkeiten

`pip install markdown-it-py pyyaml`
