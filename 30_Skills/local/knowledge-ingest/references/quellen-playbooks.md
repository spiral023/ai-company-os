# Quellen-Playbooks

Kompakte Erfassungsregeln pro Quellentyp. Nur den Abschnitt des tatsächlich vorliegenden Quellentyps anwenden. Grundregel für alle Typen: erst vollständig erfassen, dann synthetisieren — keine Lücke plausibel ergänzen.

## X/Twitter

**Primärweg ist die X API, nicht WebFetch:**

```powershell
npm run ingest:x -- <tweet-url-oder-id> --thread
```

Ergebnis: `00_Inbox/Quellen/<slug>.md` mit `status: neu`, Bilder lokal unter `00_Inbox/Quellen/medien/<slug>/`. Details: `00_Inbox/Quellen/README.md`.

- Die API liefert, was WebFetch nicht kann: `note_tweet`-Langtexte, den Volltext nativer X-Artikel, aufgelöste Threads und Medien mit Alt-Text. Deshalb immer zuerst das Script.
- Läuft ein API-Call ins Leere, sagt die Fehlermeldung, was zu tun ist: 401 Token ungültig · **402 Guthaben aufgebraucht** · 429 Rate-Limit (kein Auto-Retry, die API ist pay-per-use) · 404 Post gelöscht oder privat. Bei 402/429 nicht auf WebFetch ausweichen, sondern Philipp informieren — sonst entsteht eine unvollständige Source-Notiz, die aussieht wie eine vollständige.
- Threads älter als 7 Tage brauchen Full-Archive-Zugang. Meldet das Script, dass der Thread nicht auflösbar ist: die URL des **letzten** Threadposts übergeben, dann läuft der Rückwärts-Walk über die `replied_to`-Kette.
- Autor-Posts und Replies Dritter strikt trennen: Nur Posts des Thread-Autors bilden den Primärinhalt; fachlich relevante Replies sind Zusatzquellen und werden als solche gekennzeichnet. Das Script liefert nur Autor-Posts.
- Nie Vollständigkeit behaupten: Der Frontmatter-Wert `thread_posts` sagt, wie viele Posts erfasst wurden. Deutet der Text auf mehr hin („1/7" bei 2 erfassten Posts), die Lücke in der Source-Notiz vermerken.
- Bilder liegen bereits lokal. Tragen sie Kernaussagen (Charts, Preistabellen, Benchmarks), den Bildinhalt lesen und die Zahlen in die Source-Notiz übernehmen — Diagramme enthalten regelmäßig Werte, die im Text fehlen. Unter `Medien:` auf den lokalen Pfad verweisen.
- WebFetch nur als Fallback, wenn das Script nicht nutzbar ist (kein Token, kein Guthaben) und Philipp zustimmt. Dann in der Source-Notiz als „per WebFetch abgerufen, ggf. verlustbehaftet" kennzeichnen.
- Bei unsicherer Autor-Zuordnung oder wesentlich unvollständigem Inhalt: Philipp um eingefügten Originaltext bitten statt aus Such-Snippets oder einem einzelnen Mirror zu rekonstruieren.

## GitHub-Repository

- Aussagen an konkrete Dateien, Releases oder Commits binden — keine Pauschal-Zusammenfassung und keine Schlüsse aus Dateinamen allein.
- Reihenfolge: README → gezielt `docs/`/Releases → nur die Dateien lesen, die eine konkrete Aussage tragen.
- README, Docs und Code können auseinanderlaufen: bei Konflikt den jeweiligen Stand benennen statt zu glätten.
- Liegt das Repo unter `external_repos/`: dort prüfen (Beleg-Typ `verifiziert`). Liegt es nicht vor: Download gemäß `AGENTS.md` → „Repo-Import“ vorschlagen, nicht eigenmächtig klonen.

## Website/Blog/Docs

- Canonical URL, Autor und Datum festhalten; bei Docs zusätzlich die Version — versionsabhängige Aussagen ohne Versionsbezug sind unvollständig.
- Hauptinhalt erfassen, Boilerplate (Navigation, Newsletter, Werbung) verwerfen. Bei Paywall/Teaser: stoppen und nachfragen, nicht aus Snippets ergänzen.
- Aussagen aus verlinkten Quellen der tatsächlich tragenden Quelle zuordnen, nicht dem verlinkenden Artikel.
