# Quellen-Playbooks

Kompakte Erfassungsregeln pro Quellentyp. Nur den Abschnitt des tatsächlich vorliegenden Quellentyps anwenden. Grundregel für alle Typen: erst vollständig erfassen, dann synthetisieren — keine Lücke plausibel ergänzen.

## X/Twitter

- Autor-Posts und Replies Dritter strikt trennen: Nur Posts des Thread-Autors bilden den Primärinhalt; fachlich relevante Replies sind Zusatzquellen und werden als solche gekennzeichnet.
- WebFetch liefert bei Threads oft nur den Ausgangspost. Nie Vollständigkeit behaupten; erkennbare Lücken („1/7“ ohne Folgeposts, abgeschnittene Aufzählungen) in der Source-Notiz explizit vermerken.
- Bei wesentlich unvollständigem Thread oder unsicherer Autor-Zuordnung: Philipp um eingefügten Originaltext bitten statt aus Such-Snippets oder einem einzelnen Mirror zu rekonstruieren.
- Enthält der Tweet Bilder/Diagramme mit Kernaussagen: unter `Medien:` in der Source-Notiz die Original-URL verlinken und den Inhalt in einem Satz beschreiben (nichts herunterladen).

## GitHub-Repository

- Aussagen an konkrete Dateien, Releases oder Commits binden — keine Pauschal-Zusammenfassung und keine Schlüsse aus Dateinamen allein.
- Reihenfolge: README → gezielt `docs/`/Releases → nur die Dateien lesen, die eine konkrete Aussage tragen.
- README, Docs und Code können auseinanderlaufen: bei Konflikt den jeweiligen Stand benennen statt zu glätten.
- Liegt das Repo unter `external_repos/`: dort prüfen (Beleg-Typ `verifiziert`). Liegt es nicht vor: Download gemäß `AGENTS.md` → „Repo-Import“ vorschlagen, nicht eigenmächtig klonen.

## Website/Blog/Docs

- Canonical URL, Autor und Datum festhalten; bei Docs zusätzlich die Version — versionsabhängige Aussagen ohne Versionsbezug sind unvollständig.
- Hauptinhalt erfassen, Boilerplate (Navigation, Newsletter, Werbung) verwerfen. Bei Paywall/Teaser: stoppen und nachfragen, nicht aus Snippets ergänzen.
- Aussagen aus verlinkten Quellen der tatsächlich tragenden Quelle zuordnen, nicht dem verlinkenden Artikel.
