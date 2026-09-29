---
name: blog-schreiben
description: "Verwende diesen Skill, um aus der Wissensbasis (80_Knowledge/) Blogbeiträge für ai-blog.sp23.online zu schreiben: Kurzmeldungen, Modell-Radar, Arbeitsweisen, Duelle, Behauptungs-Checks und Wochen-Digest. Auch bei „schreib einen Blogartikel über …“, „was gibt es Neues diese Woche“, „mach einen Wochen-Digest“. Schreibt nur Entwürfe (status: entwurf) und veröffentlicht nie selbst."
---

# Blog schreiben

Schreibt Entwürfe für den Blog in `blog/posts/`. Leser sind technisch interessierte Menschen, die mit KI arbeiten oder coden: Anwender, Vibe Coder, Programmierer. Sie kennen die Grundbegriffe, aber nicht jeden Fachausdruck. Die erste Nennung eines Begriffs aus `blog/glossar.yaml` wird automatisch mit dem Glossar verlinkt. Sie wollen Einordnung, keine Grundlagen.

## Harte Regeln

- **Nur Entwürfe.** Jeder Beitrag beginnt mit `status: entwurf`. Nie `freigegeben` setzen, nie deployen. Die Freigabe ist Philipps Entscheidung (AGENTS.md: öffentliche Veröffentlichungen).
- **Nur belegte Aussagen.** Jede Zahl und jede Behauptung stammt aus einer Source-Notiz, einem Pattern oder dem Fakten-Register (`80_Knowledge/Fakten/Modelle-und-Preise.md`). Nichts aus eigenem Modellwissen als Tatsache ausgeben.
- **Quellen sind Pflicht.** Im Frontmatter `quellen:` mit den Basisnamen der Source-Notizen. Der Generator erzeugt daraus Titel, Autor, Datum und Original-URL.
- **Eigenes von Fremdem trennen.** Eigene Rechnungen ausdrücklich kennzeichnen („eigene Rechnung“). Herstellerangaben, Selbstberichte und Sekundärquellen als solche benennen. Bei Zahlen nennen, wer sie gemessen hat und welche Einschränkung gilt.
- **Nicht vergleichen, was nicht vergleichbar ist.** Index-Versionen, Harnesses und Kosten pro Token gegen Kosten pro Aufgabe getrennt halten.
- **Keine fremden Texte übernehmen.** Aussagen in eigenen Worten, Zitate höchstens ein Satz. Der Beitrag liefert Einordnung, keine Kopie.
- **Keine internen Begriffe.** Leser kennen das Wissenssystem nicht. Nie „Notiz“, „Pattern“, „Konfidenz“, „Wiki“, „Wissensbasis“ oder „Source-Notiz“ im Text. Stattdessen benennen, woher die Aussage stammt („laut Anthropic-Blog“, „so berichtet der Autor“). Die Belegstärke in einem Satz sagen („mehrfach belegt“, „nur eine Meinung“), nicht die interne Skala erklären. Der Generator lehnt diese Begriffe ab.
- **Aktualität prüfen.** Bei Preisen, Modellen, Benchmarks das Datum der Quelle nennen und im Fakten-Register nachsehen, ob es neuere Angaben gibt.

## Stil

- **Glossar pflegen.** Kommt ein Fachbegriff vor, den ein Vibe Coder nicht kennt (Harness, TTL, Blast Radius), zuerst in `blog/glossar.yaml` prüfen, ob es ihn gibt, sonst mit zwei bis vier Sätzen in eigenen Worten ergänzen. Nie Definitionen aus dem AI Coding Dictionary (Matt Pocock) oder anderen Quellen übernehmen oder übersetzen, dort fehlt eine Lizenz. Erklärungen im Glossar beschreiben Allgemeinverständnis, keine Zahlen.
- Deutsch, sachlich und direkt, Ansprache mit „du“ bei Handlungsempfehlungen (kleingeschrieben: du, dich, dein). Englische Fachbegriffe im Original.
- Hohe Informationsdichte: erst das Ergebnis, dann die Begründung. Kein Einleitungsgeplänkel, keine Floskeln („in der heutigen schnelllebigen Zeit“), keine Werbesprache, keine Emojis.
- Konkrete Titel mit Aussage („Opus 5.5 an der Spitze, aber teurer pro Task“), nicht „Neues von Anthropic“.
- Tabellen für Vergleiche, kurze Absätze, ein Fazit mit einer Handlungsempfehlung.
- Am Anfang `## Kurz gesagt` mit zwei bis vier Stichpunkten (außer Kurzmeldung). Der Generator macht daraus eine Box. Die Stichpunkte beantworten „Was mache ich damit?“, nicht nur „Was ist passiert?“.
- Das Ergebnis steht oben: Bei Checks und Duellen die Urteilstabelle direkt nach „Kurz gesagt“, die Begründung danach. Herkunft und Lücken einer Aussage in ein bis zwei Sätzen, kein eigener Prozessabschnitt.
- Länge deckeln: Analysen etwa 700 Wörter. Wird es mehr, in zwei Beiträge aufteilen und verlinken.
- Belege an der Aussage: `{q:2}` verweist auf die zweite Quelle aus `quellen:` (Reihenfolge zählt) und wird zur Fußnote mit Sprung zur Quellenliste.
- Verweise auf andere Beiträge als `[Text](post:<slug>)`. Der Generator prüft, dass der Beitrag existiert. Kein „dazu ein eigener Beitrag“ ohne Link. Existiert er noch nicht, ihn zuerst schreiben oder den Satz streichen.
- Zahlen deutsch: `$0,068` und `4/20 US-Dollar` mit Komma, Daten als 22.09.2026, nicht im Code-Format. Nach jedem Satzende ein Leerzeichen.
- Jede Quelle aus `quellen:` mindestens einmal mit `{q:n}` zitieren, sonst lehnt der Generator ab. Absätze mit Zahlen ohne `{q:n}` meldet er als Hinweis: beheben, nicht ignorieren.
- Ändern sich Preise oder Zahlen später, `aktualisiert: JJJJ-MM-TT` im Frontmatter setzen.
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
