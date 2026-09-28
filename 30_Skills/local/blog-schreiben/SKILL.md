---
name: blog-schreiben
description: "Verwende diesen Skill, um aus der Wissensbasis (80_Knowledge/) Blogbeiträge für blog.sp23.online zu schreiben: Kurzmeldungen, Modell-Radar, Arbeitsweisen, Duelle, Behauptungs-Checks und Wochen-Digest. Auch bei „schreib einen Blogartikel über …“, „was gibt es Neues diese Woche“, „mach einen Wochen-Digest“. Schreibt nur Entwürfe (status: entwurf) und veröffentlicht nie selbst."
---

# Blog schreiben

Schreibt Entwürfe für den Blog in `blog/posts/`. Leser sind technisch interessierte Menschen, die mit KI arbeiten oder coden: Anwender, Vibe Coder, Programmierer. Sie kennen Begriffe wie Context Window, Effort-Stufe oder Prompt Cache und wollen Einordnung, keine Grundlagen.

## Harte Regeln

- **Nur Entwürfe.** Jeder Beitrag beginnt mit `status: entwurf`. Nie `freigegeben` setzen, nie deployen. Die Freigabe ist Philipps Entscheidung (AGENTS.md: öffentliche Veröffentlichungen).
- **Nur belegte Aussagen.** Jede Zahl und jede Behauptung stammt aus einer Source-Notiz, einem Pattern oder dem Fakten-Register (`80_Knowledge/Fakten/Modelle-und-Preise.md`). Nichts aus eigenem Modellwissen als Tatsache ausgeben.
- **Quellen sind Pflicht.** Im Frontmatter `quellen:` mit den Basisnamen der Source-Notizen. Der Generator erzeugt daraus Titel, Autor, Datum und Original-URL.
- **Eigenes von Fremdem trennen.** Eigene Rechnungen ausdrücklich kennzeichnen („eigene Rechnung“). Herstellerangaben, Selbstberichte und Sekundärquellen als solche benennen. Bei Zahlen nennen, wer sie gemessen hat und welche Einschränkung gilt.
- **Nicht vergleichen, was nicht vergleichbar ist.** Index-Versionen, Harnesses und Kosten pro Token gegen Kosten pro Aufgabe getrennt halten.
- **Keine fremden Texte übernehmen.** Aussagen in eigenen Worten, Zitate höchstens ein Satz. Der Beitrag liefert Einordnung, keine Kopie.
- **Aktualität prüfen.** Bei Preisen, Modellen, Benchmarks das Datum der Quelle nennen und im Fakten-Register nachsehen, ob es neuere Angaben gibt.

## Stil

- Deutsch, sachlich und direkt, Ansprache mit „du“ bei Handlungsempfehlungen (kleingeschrieben: du, dich, dein). Englische Fachbegriffe im Original.
- Hohe Informationsdichte: erst das Ergebnis, dann die Begründung. Kein Einleitungsgeplänkel, keine Floskeln („in der heutigen schnelllebigen Zeit“), keine Werbesprache, keine Emojis.
- Konkrete Titel mit Aussage („Opus 5.5 an der Spitze, aber teurer pro Task“), nicht „Neues von Anthropic“.
- Tabellen für Vergleiche, kurze Absätze, ein Fazit mit einer Handlungsempfehlung.
- Am Anfang „Kurz gesagt“ mit zwei bis vier Stichpunkten (außer Kurzmeldung).
- Echte Umlaute, deutsche Anführungszeichen „…“, keine ASCII-Ersatzzeichen.

## Formate

| Format (`kategorie`) | Länge | Rohstoff | Aufbau |
|---|---|---|---|
| **Kurzmeldung** (`kurz`) | 120–250 Wörter | eine Neuigkeit aus Fakten oder Release-Source | Was ist neu, was bedeutet es, was ist unbelegt |
| **Modell-Radar** (`modelle`) | 500–900 | Fakten-Register, Modell- und Kosten-Sources | Kurz gesagt, Zahlen als Tabelle, Warum (Mechanik), Einordnung, Empfehlung |
| **Arbeitsweise** (`arbeitsweisen`) | 700–1200 | ein Pattern mit seinen Belegen | Problem, Ablauf, wann es trägt, Kosten und Grenzen, Belegstärke (Konfidenz, Autorenvielfalt), Spannungen |
| **Werkzeug-Notiz** (`tools`) | 300–600 | Release-Sources | Was es tut, wie man es nutzt, was fehlt, Trade-offs |
| **Duell** (`duell`) | 700–1100 | zwei Sources mit Gegenpositionen oder ein Pattern mit Spannung | Position A, Position B, wo sie sich wirklich unterscheiden, wann welche gilt |
| **Behauptungs-Check** (`check`) | 700–1100 | Befunde und Source-Einordnungen | fünf Behauptungen: Was wird behauptet, was ist belegt, was fehlt, Urteil |
| **Wochen-Digest** (`digest`) | 400–700 | alles Neue seit dem letzten Digest | fünf bis acht Punkte mit je zwei bis drei Sätzen und Verweis auf die Einzelbeiträge |

## Ablauf

1. Auftrag klären: Format, Thema oder Zeitraum. Bei „was gibt es Neues“: Sources mit `datum:` im Zeitraum und `zeitkritisch: ja` sowie neue Zeilen im Fakten-Register sichten.
2. Rohstoff lesen: `80_Knowledge/Index.md` für Patterns, dann gezielt die passenden Notizen. Bei Patterns die **Belege** und **Spannungen** lesen, nicht nur den Zweck.
3. Zahlen gegen die Source-Notiz prüfen (nicht aus dem Gedächtnis). Widersprüche zwischen Quellen im Text nennen.
4. Beitrag schreiben nach `blog/posts/YYYY-MM-DD-<slug>.md` mit dem Frontmatter aus `blog/README.md`. Das Datum ist das Tagesdatum (oder das gewünschte Veröffentlichungsdatum).
5. Prüfen: `python blog/build_blog.py --check`, dann `python blog/build_blog.py --drafts` und die Vorschau ansehen.
6. Bericht an Philipp: Titel, Format, Länge, verwendete Quellen, alles, was Philipp vor der Freigabe prüfen sollte (unsichere Zahlen, Herstellerangaben, fehlende Primärquellen).

## Häufige Fehler

- Preis pro Token mit Kosten pro Aufgabe gleichsetzen.
- Zahlen aus verschiedenen Index-Versionen nebeneinanderstellen.
- Selbstberichtete Herstellerzahlen ohne Vermerk übernehmen.
- Aus einer einzelnen Meinung ein Fazit ableiten. Die Belegstärke gehört in den Text.
- Ein Pattern erklären, ohne seine Grenzen und Kosten zu nennen.
- Den Beitrag ohne Handlungsempfehlung enden lassen.
