# Quellen-Playbooks

Kompakte Erfassungsregeln pro Quellentyp. Nur den Abschnitt des tatsächlich vorliegenden Quellentyps anwenden. Grundregel für alle Typen: erst vollständig erfassen, dann synthetisieren — keine Lücke plausibel ergänzen.

## X/Twitter

**Primärweg ist die X API, nicht WebFetch:**

```powershell
npm run ingest:x -- <tweet-url-oder-id> --thread
```

Ergebnis: `00_Inbox/Quellen/X/<slug>.md` mit `status: neu`, Bilder lokal unter `00_Inbox/Quellen/X/medien/<slug>/`. Details: `00_Inbox/Quellen/README.md`.

- Die API liefert, was WebFetch nicht kann: `note_tweet`-Langtexte, den Volltext nativer X-Artikel, aufgelöste Threads und Medien mit Alt-Text. Deshalb immer zuerst das Script.
- Läuft ein API-Call ins Leere, sagt die Fehlermeldung, was zu tun ist: 401 Token ungültig · **402 Guthaben aufgebraucht** · 429 Rate-Limit (kein Auto-Retry, die API ist pay-per-use) · 404 Post gelöscht oder privat. Bei 402/429 nicht auf WebFetch ausweichen, sondern Philipp informieren — sonst entsteht eine unvollständige Source-Notiz, die aussieht wie eine vollständige.
- Threads älter als 7 Tage brauchen Full-Archive-Zugang. Meldet das Script, dass der Thread nicht auflösbar ist: die URL des **letzten** Threadposts übergeben, dann läuft der Rückwärts-Walk über die `replied_to`-Kette. Er kommt ohne Search aus und findet regelmäßig mehr Posts als die Suche. Die Notiz hängt am ältesten eigenen Post des Strangs, deshalb trifft der Nachlauf dieselbe Datei statt eine zweite anzulegen — ohne `--force` meldet das Script nur, dass die neue Fassung mehr Posts hätte.
- Autor-Posts und Replies Dritter strikt trennen: Nur Posts des Thread-Autors bilden den Primärinhalt; fachlich relevante Replies sind Zusatzquellen und werden als solche gekennzeichnet. Der Vorwärts-Weg über die Suche liefert nur Autor-Posts; der Rückwärts-Walk folgt der Antwortkette und nimmt auch Posts Dritter mit — die tragen in der Notiz `· Reply von @handle (nicht vom Autor)` in der Überschrift.
- Nie Vollständigkeit behaupten: Der Frontmatter-Wert `thread_posts` sagt, wie viele Posts erfasst wurden. Deutet der Text auf mehr hin („1/7" bei 2 erfassten Posts), die Lücke in der Source-Notiz vermerken.
- Bilder liegen bereits lokal. Tragen sie Kernaussagen (Charts, Preistabellen, Benchmarks), den Bildinhalt lesen und die Zahlen in die Source-Notiz übernehmen — Diagramme enthalten regelmäßig Werte, die im Text fehlen. Unter `Medien:` auf den lokalen Pfad verweisen.
- WebFetch nur als Fallback, wenn das Script nicht nutzbar ist (kein Token, kein Guthaben) und Philipp zustimmt. Dann in der Source-Notiz als „per WebFetch abgerufen, ggf. verlustbehaftet" kennzeichnen.
- Bei unsicherer Autor-Zuordnung oder wesentlich unvollständigem Inhalt: Philipp um eingefügten Originaltext bitten statt aus Such-Snippets oder einem einzelnen Mirror zu rekonstruieren.

## TikTok

**Primärweg ist das Script, nicht WebFetch:**

```powershell
npm run ingest:tiktok -- <video-url-oder-id>
```

Ergebnis: `00_Inbox/Quellen/TikTok/<slug>.md` mit `status: neu`, Cover lokal unter `00_Inbox/Quellen/TikTok/medien/<slug>/`. Details: `00_Inbox/Quellen/README.md`.

- Der gesprochene Inhalt ist bei TikTok die eigentliche Quelle — die Caption besteht oft nur aus Hashtags. Das Script holt das Transkript über einen kostenpflichtigen Apify-Actor ($0.001 pro Video). Bei `402 Guthaben aufgebraucht` nicht auf WebFetch ausweichen, sondern Philipp informieren.
- Steht `sprache_abweichung: true` im Frontmatter, hat TikTok statt des Originaltons eine maschinell übersetzte Untertitelspur geliefert (typisch: deutsches Video, englischer Text mit deutscher Satzstellung). Diese Fassung ist eine doppelte Verfremdung — Spracherkennung plus Übersetzung — und taugt nicht für Zitate. Inhalt aus der Caption belegen und die Einschränkung in der Source-Notiz vermerken.
- **Das Transkript ist automatische Spracherkennung, keine Autorenschrift.** Eigennamen und Zahlwörter sind regelmäßig falsch (`Grammy` statt `graphify`, `1 KI System` statt `ein KI-System`). Wörtliche Zitate nur nach Prüfung gegen das Video übernehmen; im Zweifel sinngemäß wiedergeben und den Vorbehalt in der Source-Notiz vermerken.
- Meldet das Script „Kein Transkript verfügbar", hat TikTok für das Video keine Untertitel erzeugt. Dann trägt die Notiz nur Metadaten. Bei Accounts, die den Inhalt in die Caption schreiben, kann die Caption trotzdem eine tragfähige Quelle sein — dann in der Source-Notiz vermerken, dass der Beleg aus der Caption stammt und nicht aus dem gesprochenen Wort. Ist auch die Caption leer, ist die Notiz keine ausreichende Quelle.
- Ein `datum_unsicher: true` im Frontmatter heißt: das Veröffentlichungsdatum ließ sich nicht aus der Video-ID ableiten und ist das Erfassungsdatum. Nicht als Publikationsdatum zitieren.

## YouTube

```powershell
python ai.py ingest <youtube-url>
```

Ergebnis: `00_Inbox/Quellen/YouTube/<slug>.md` mit Videobeschreibung und einer vorhandenen deutschen oder englischen Untertitelspur.

- Das Transkript wird ohne Zeitstempel zu lesbaren Absätzen verbunden. Kapitelmarken können weiterhin in der unverändert übernommenen Videobeschreibung vorkommen.
- `transkript_generiert: ja` kennzeichnet automatische Spracherkennung. Eigennamen und Fachbegriffe vor Zitaten gegen das Video prüfen; nicht still korrigieren und anschließend als Originalwortlaut ausgeben.
- Stellt YouTube keine Untertitelspur bereit, bricht der Abruf ab. Keine Transkription aus Such-Snippets erfinden.
- Titel, Kanal, Beschreibung und Veröffentlichungsdatum kommen ohne YouTube-API-Key von der Videoseite; bei unvollständigen Metadaten die Einschränkung sichtbar lassen.

## GitHub-Repository

- Aussagen an konkrete Dateien, Releases oder Commits binden — keine Pauschal-Zusammenfassung und keine Schlüsse aus Dateinamen allein.
- Reihenfolge: README → gezielt `docs/`/Releases → nur die Dateien lesen, die eine konkrete Aussage tragen.
- README, Docs und Code können auseinanderlaufen: bei Konflikt den jeweiligen Stand benennen statt zu glätten.
- Liegt das Repo unter `external_repos/`: dort prüfen (Beleg-Typ `verifiziert`). Liegt es nicht vor: Download gemäß `AGENTS.md` → „Repo-Import“ vorschlagen, nicht eigenmächtig klonen.

## Website/Blog/Docs

- Zuerst mit `python ai.py ingest <url>` nach `00_Inbox/Quellen/URL/` archivieren; WebFetch ist kein Ersatz für die lokale Rohquelle.
- Canonical URL, Autor und Datum festhalten; bei Docs zusätzlich die Version — versionsabhängige Aussagen ohne Versionsbezug sind unvollständig.
- Hauptinhalt erfassen, Boilerplate (Navigation, Newsletter, Werbung) verwerfen. Bei Paywall/Teaser: stoppen und nachfragen, nicht aus Snippets ergänzen.
- Aussagen aus verlinkten Quellen der tatsächlich tragenden Quelle zuordnen, nicht dem verlinkenden Artikel.

## PDF

- Mit `python ai.py ingest <url-oder-pfad>` nach `00_Inbox/Quellen/PDF/` archivieren.
- Seitenstruktur und extrahierte Bilder erhalten. Bei gescannten PDFs ohne Textschicht nicht behaupten, der Inhalt sei vollständig extrahiert; OCR wäre ein eigener, expliziter Verarbeitungsschritt.
