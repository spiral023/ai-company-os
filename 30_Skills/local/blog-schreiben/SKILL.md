---
name: blog-schreiben
description: "Verwende diesen Skill, um aus der Wissensbasis (80_Knowledge/) Blogbeiträge für ai-blog.sp23.online zu schreiben: Kurzmeldungen, Modell-Radar, Arbeitsweisen, Duelle, Behauptungs-Checks und Wochen-Digest. Auch bei „schreib einen Blogartikel über …“, „was gibt es Neues diese Woche“, „mach einen Wochen-Digest“. Schreibt Entwürfe (status: entwurf); die Freigabe läuft ausschließlich über das Skript `build_blog.py --auto-freigeben`."
---

# Blog schreiben

Schreibt Entwürfe für den Blog in `blog/posts/`. Leser sind technisch interessierte Menschen, die mit KI arbeiten oder coden: Anwender, Vibe Coder, Programmierer. Sie kennen die Grundbegriffe, aber nicht jeden Fachausdruck. Die erste Nennung eines Begriffs aus `blog/glossar.yaml` wird automatisch mit dem Glossar verlinkt. Sie wollen Einordnung, keine Grundlagen.

## Harte Regeln

- **Entwürfe schreiben, nie selbst freigeben.** Jeder Beitrag beginnt mit `status: entwurf`. Den Status nie von Hand auf `freigegeben` setzen und nie deployen. Philipp hat am 29.09.2026 beschlossen, dass die Freigabe automatisch läuft: `python blog/build_blog.py --auto-freigeben` gibt jeden Entwurf frei, der alle Prüfungen ohne Fehler und Hinweise besteht, und veröffentlicht ihn sofort (seit 07.10.2026, vorher frühestens am Folgetag). Wer Hinweise nicht beheben kann, lässt den Entwurf liegen und meldet das.
- **Nur belegte Aussagen.** Jede Zahl und jede Behauptung stammt aus einer Source-Notiz, einem Pattern oder dem Fakten-Register (`80_Knowledge/Fakten/Modelle-und-Preise.md`). Nichts aus eigenem Modellwissen als Tatsache ausgeben.
- **Quellen sind Pflicht.** Im Frontmatter `quellen:` mit den Basisnamen der Source-Notizen. Der Generator erzeugt daraus Titel, Autor, Datum und Original-URL.
- **Eigenes von Fremdem trennen.** Eigene Rechnungen kennzeichnen („eigene Rechnung“). Bei Zahlen einmal nennen, wer sie gemessen hat („laut Artificial Analysis“), und eine Einschränkung nur, wenn sie die Entscheidung ändert (Herstellerangabe bei Preisen, anderer Index).
- **Nicht vergleichen, was nicht vergleichbar ist.** Index-Versionen, Harnesses und Kosten pro Token gegen Kosten pro Aufgabe getrennt halten.
- **Keine fremden Texte übernehmen.** Aussagen in eigenen Worten, Zitate höchstens ein Satz. Der Beitrag liefert Einordnung, keine Kopie.
- **Keine internen Begriffe.** Leser kennen das Wissenssystem nicht. Nie „Notiz“, „Pattern“, „Konfidenz“, „Wiki“, „Wissensbasis“ oder „Source-Notiz“ im Text. Stattdessen benennen, woher die Aussage stammt („laut Anthropic-Blog“). Der Generator lehnt diese Begriffe ab.
- **Keine Beleg-Diskussion im Text.** Nicht „belegt“, „unbelegt“, „Belegstärke“, „Primärquelle“, „Quellenlage“. Der Text sagt, was gilt und was du tun sollst. Ist eine Aussage unsicher, reicht ein Halbsatz („bisher nur eine Einzelmessung“) oder sie fällt weg. Der Generator meldet solche Wörter als Hinweis, und ein Beitrag mit Hinweisen wird nicht automatisch freigegeben.
- **Aktualität prüfen.** Bei Preisen, Modellen, Benchmarks das Datum der Quelle nennen und im Fakten-Register nachsehen, ob es neuere Angaben gibt.

## Stil

- **Glossar pflegen.** Kommt ein Fachbegriff vor, den ein Vibe Coder nicht kennt (Harness, TTL, Blast Radius), zuerst in `blog/glossar.yaml` prüfen, ob es ihn gibt, sonst mit zwei bis vier Sätzen in eigenen Worten ergänzen. Nie Definitionen aus dem AI Coding Dictionary (Matt Pocock) oder anderen Quellen übernehmen oder übersetzen, dort fehlt eine Lizenz. Erklärungen im Glossar beschreiben Allgemeinverständnis, keine Zahlen.
- **Klingt wie ein Blog, nicht wie ein Gutachten.** Ein Mensch erklärt einem Kollegen, was passiert ist und was er tun soll: konkrete Aussagen, kurze Sätze, eine Haltung („Für Routinearbeit lohnt sich das nicht“). Kein Prozess-, Quellen- oder Methodengerede im Text. Die Quellen stehen ohnehin unter dem Beitrag.
- Deutsch, sachlich und direkt, Ansprache mit „du“ bei Handlungsempfehlungen (kleingeschrieben: du, dich, dein). Englische Fachbegriffe im Original.
- Hohe Informationsdichte: erst das Ergebnis, dann die Begründung. Kein Einleitungsgeplänkel, keine Floskeln („in der heutigen schnelllebigen Zeit“), keine Werbesprache, keine Emojis.
- Konkrete Titel mit Aussage („Opus 5.5 an der Spitze, aber teurer pro Task“), nicht „Neues von Anthropic“.
- Tabellen für Vergleiche, kurze Absätze, ein Fazit mit einer Handlungsempfehlung.
- Am Anfang `## Kurz gesagt` mit zwei bis vier Stichpunkten (außer Kurzmeldung). Der Generator macht daraus eine Box. Die Stichpunkte beantworten „Was mache ich damit?“, nicht nur „Was ist passiert?“.
- Das Ergebnis steht oben: Bei Checks und Duellen die Urteilstabelle direkt nach „Kurz gesagt“, die Begründung danach. Herkunft und Lücken einer Aussage in ein bis zwei Sätzen, kein eigener Prozessabschnitt.
- Länge deckeln: Analysen höchstens etwa 1300 Wörter (Philipp, 29.09.2026). Die Längen in der Formate-Tabelle sind Richtwerte darunter. Wird es mehr, in zwei Beiträge aufteilen und verlinken.
- Belege im Markdown: `{q:2}` verweist auf die zweite Quelle aus `quellen:` (Reihenfolge zählt). Die Prüfung verlangt sie an jeder Aussage mit Zahl, die Seite zeigt sie nicht im Text (`quellenverweise_im_text: false`), sondern nur die Quellenliste am Ende.
- Verweise auf andere Beiträge als `[Text](post:<slug>)`. Der Generator prüft, dass der Beitrag existiert. Kein „dazu ein eigener Beitrag“ ohne Link. Existiert er noch nicht, ihn zuerst schreiben oder den Satz streichen.
- Zahlen deutsch: `$0,068` und `4/20 US-Dollar` mit Komma, Daten als 22.09.2026, nicht im Code-Format. Nach jedem Satzende ein Leerzeichen.
- Jede Quelle aus `quellen:` mindestens einmal mit `{q:n}` zitieren, sonst lehnt der Generator ab. Absätze mit Zahlen ohne `{q:n}` meldet er als Hinweis: beheben, nicht ignorieren.
- Ändern sich Preise oder Zahlen später, `aktualisiert: JJJJ-MM-TT` im Frontmatter setzen.
- Echte Umlaute, deutsche Anführungszeichen „…“, keine ASCII-Ersatzzeichen.

## Slop-Muster (nach no-ai-slop, Peter Yang, MIT)

Beim Schreiben vermeiden, beim Prüfen als Detect-Durchgang suchen. Quelle: `external_repos/petergyang/no-ai-slop`, hier auf Deutsch und für den Blog verdichtet.

- **Portabilitätstest.** Ließe sich ein Satz unverändert in einen anderen Beitrag oder zu einem anderen Produkt schieben, ist er Füllstoff. Streichen oder durch Zahl, Mechanismus, Folge oder Urteil ersetzen.
- **Binärkontrast.** „Nicht X, sondern Y“, „Die Frage ist nicht …, sondern …“. Direkt Y sagen.
- **Aufmerksamkeitsheischer.** „Hier ist der Punkt“, „Was die meisten übersehen“, „Das wird oft unterschätzt“, „Ehrlich gesagt“. Behauptung stehen lassen, Ankündigung streichen.
- **Zeigefinger-Sätze.** „Das ist wichtig“, „Der entscheidende Punkt“, „Das ändert alles“. Die Fakten tragen die Betonung.
- **Doppelpunkt-Enthüllung.** „Der Trick dahinter: …“. Als normalen Satz schreiben. Doppelpunkt nur für Listen und Labels.
- **Bedeutungs-Anhängsel.** „…, was zeigt, wie ernst das Team es meint“. Wirkung als konkrete Folge nennen oder streichen.
- **Wichtigtuerei.** „markiert einen Wendepunkt“, „spielt eine zentrale Rolle“. Fakt nennen, Leser urteilen lassen.
- **Vage Zuschreibung.** „Experten sagen“, „Studien zeigen“, „viele meinen“. Quelle nennen oder Aussage streichen.
- **Wortkarussell.** Nicht Agent, Assistent, Tool abwechseln. Das richtige Wort wiederholen.
- **Fragmente und Staccato.** „Das war’s. Ganz einfach.“ Vollständige Sätze, wechselnde Satzlänge.
- **Rhetorische Vorlagen.** „Was, wenn ich dir sage …“, Frage mit selbst gegebener Antwort.
- **Kicker und Recap.** Kein „Am Ende gilt“, kein Schlusssatz mit Metapher, keine Wiederholung des Beitrags. Enden mit der Handlungsempfehlung.
- **Formatierungs-Slop.** Fettdruck mitten im Satz, Listen statt zwei Sätzen, Überschrift über zwei Sätzen, Gedankenstriche als Rhythmus.
- **Leere Wörter.** tatsächlich, einfach, wirklich, im Grunde, letztlich, grundlegend, „es lohnt sich zu erwähnen“, „im Kern“, „in der Welt von“. Nur behalten, wenn sie Unsicherheit oder Kontrast tragen.

## Formate

| Format (`kategorie`) | Länge | Rohstoff | Aufbau |
|---|---|---|---|
| **Kurzmeldung** (`kurz`) | 120–250 Wörter | eine Neuigkeit aus Fakten oder Release-Source | Was ist neu, was bedeutet es für dich |
| **Modell-Radar** (`modelle`) | 500–900 | Fakten-Register, Modell- und Kosten-Sources | Kurz gesagt, Zahlen als Tabelle, Warum (Mechanik), Einordnung, Empfehlung |
| **Arbeitsweise** (`arbeitsweisen`) | 700–1200 | ein Pattern mit seinen Belegen | Problem, Ablauf, wann es trägt, Kosten und Grenzen, Spannungen |
| **Werkzeug-Notiz** (`tools`) | 300–600 | Release-Sources | Was es tut, wie man es nutzt, was fehlt, Trade-offs |
| **Duell** (`duell`) | 700–1100 | zwei Sources mit Gegenpositionen oder ein Pattern mit Spannung | Position A, Position B, wo sie sich wirklich unterscheiden, wann welche gilt |
| **Behauptungs-Check** (`check`) | 700–1100 | Befunde und Source-Einordnungen | fünf Behauptungen: Was wird behauptet, was stimmt, was fehlt, Urteil in einem Wort („stimmt“, „stimmt nicht“, „nicht prüfbar“) |
| **Wochen-Digest** (`digest`) | 400–700 | alles Neue seit dem letzten Digest | fünf bis acht Punkte mit je zwei bis drei Sätzen und Verweis auf die Einzelbeiträge |
| **Prompts zum Ausprobieren** (`prompts`) | 700–1200 ohne Prompt-Text | Quellen im Cluster `prompt-vorlagen` mit vollständigem Prompt in der Rohquelle | Übersichtstabelle (Prompt, wann, Ergebnis, von wem), dann je Prompt: was er macht und warum, Prompt auf Deutsch als Codeblock mit Platzhaltern in eckigen Klammern, **Wann:**, **Ergebnis:**, Link zum englischen Original. Ein Prompt stammt aus genau einer Quelle; Varianten anderer Autoren nicht einmischen oder zusammenführen. Übertragen, nicht wörtlich übersetzen; Fachbegriffe, die der Autor bewusst wählt, im Original lassen. |

## Ablauf

1. Auftrag klären: Format, Thema oder Zeitraum. Bei „was gibt es Neues“: Sources mit `datum:` im Zeitraum und `zeitkritisch: ja` sowie neue Zeilen im Fakten-Register sichten.
2. Thema und Keywords klären: `python 70_Scripts/themen.py blog "<Cluster-ID oder Hauptkeyword>"` liefert Patterns mit Belegzahl und Spannungen (Duell-Stoff), alle Quellen des Themas mit Kernaussage, welche davon schon in einem Beitrag stehen, bestehende Beiträge zum Thema (interne Verweise per `post:`) und die Suchbegriffe. Das Hauptkeyword gehört in Titel und `zusammenfassung`, ein bis zwei Long-Tail-Begriffe in Zwischenüberschriften und den Einstieg; Keywords nie in den Text stopfen, das ist Slop. Bei Quellen mit „· offen“ zuerst schauen, ob sie den Beitrag schärfen. Passt das Thema in keinen Cluster: `python 70_Scripts/themen.py blog "<Suchbegriff>"` zeigt Notizen mit passendem Keyword.
3. Rohstoff lesen: `80_Knowledge/Index.md` für Patterns, dann gezielt die passenden Notizen. Bei Patterns die **Belege** und **Spannungen** lesen, nicht nur den Zweck.
4. Zahlen gegen die Source-Notiz prüfen (nicht aus dem Gedächtnis). Widersprüche zwischen Quellen im Text nennen.
5. Beitrag schreiben nach `blog/posts/YYYY-MM-DD-<slug>.md` mit dem Frontmatter aus `blog/README.md`. Das Datum ist das Tagesdatum (oder das gewünschte Veröffentlichungsdatum).
6. Prüfen: `python blog/build_blog.py --check`. Hinweise (Zahl ohne Beleg, Beleg-Meta) beheben, sonst wird der Entwurf nicht automatisch freigegeben. Dann `--drafts` und die Vorschau ansehen.
7. Slop-Durchgang (Detect): den Entwurf einmal komplett gegen „Slop-Muster“ lesen. Jeden Fund mit zitierter Zeile notieren und selbst beheben, ohne Zahlen, `{q:n}`-Marker oder Aussagen zu ändern. Danach Schritt 6 wiederholen.
8. Freigabe: `python blog/build_blog.py --auto-freigeben`. Der Beitrag erscheint sofort mit dem nächsten Build und Deployment.
9. Bericht an Philipp: Titel, Format, Länge, verwendete Quellen, freigegebene und liegen gebliebene Entwürfe mit Grund.

## Häufige Fehler

- Preis pro Token mit Kosten pro Aufgabe gleichsetzen.
- Zahlen aus verschiedenen Index-Versionen nebeneinanderstellen.
- Selbstberichtete Herstellerzahlen ohne Vermerk übernehmen.
- Aus einer einzelnen Meinung ein Fazit ableiten. Ein Halbsatz („bisher nur eine Einzelmessung“) reicht, oder die Aussage fällt weg.
- Ein Pattern erklären, ohne seine Grenzen und Kosten zu nennen.
- Den Beitrag ohne Handlungsempfehlung enden lassen.
