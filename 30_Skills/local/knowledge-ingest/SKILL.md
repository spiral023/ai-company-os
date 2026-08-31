---
name: knowledge-ingest
description: Verwende diesen Skill, wenn Philipp eine einzelne neue Quelle über KI-Arbeitsweisen, Skills, Agent-Workflows oder Frameworks teilt — X/Twitter, TikTok, YouTube, Artikel, PDF oder formlosen Text, auch ohne expliziten Auftrag. Archiviert sie lokal, arbeitet sie ins Knowledge-System ein und liefert ein Diff-Resümee.
---

# Knowledge Ingest

## Ziel

Neue Informationen über Arbeitsweisen dauerhaft ins Knowledge-System einarbeiten: Quelle archivieren, Erkenntnisse in Pattern-Notizen synthetisieren, Vergleiche aktualisieren. Neue Infos machen alte nicht irrelevant — es wird ergänzt, nie gelöscht.

## Schema

Templates, Invarianten und Konfidenz-Modell stehen in `80_Knowledge/README.md`. Diese Datei vor der ersten Einarbeitung lesen und exakt befolgen.

## Ablauf

1. **Quelle beschaffen.** Das passende Playbook aus `references/quellen-playbooks.md` (im Skill-Verzeichnis) anwenden.
   - Eingefügter Originaltext hat Vorrang (verlustfrei).
   - **X/Twitter:** immer `npm run ingest:x -- <url> --thread` statt WebFetch. Das Script holt Artikel-Volltext, Thread und Bilder über die API.
   - **TikTok:** immer `npm run ingest:tiktok -- <url>`. Das Script holt Caption, Cover und — sofern verfügbar — das Transkript.
   - **YouTube, Artikel und PDF:** immer `python ai.py ingest <url-oder-pfad>`. YouTube wird mit Beschreibung und lesbarem Transkript ohne Zeitstempel archiviert.
   - Die Scripts legen Quellen automatisch unter `00_Inbox/Quellen/{X,TikTok,YouTube,URL,PDF}/` ab. Liegt dort schon eine Notiz zur normalisierten URL bzw. ID, diese verwenden statt neu abzurufen.
   - Schlägt der vorgesehene Abruf fehl oder wirkt der Inhalt unvollständig, nicht still auf WebFetch ausweichen und die Teilfassung als vollständig behandeln. Fehler benennen und bei fehlendem Originaltext Philipp fragen.
   - Liegt die Quelle als Inbox-Notiz vor: nach dem Einarbeiten `status: neu` → `status: verarbeitet` setzen und `source_notiz:` auf die erzeugte Datei in `80_Knowledge/Sources/` verweisen. Ohne diesen Schritt taucht die Quelle beim nächsten Sammel-Lauf erneut als offen auf.
2. **Duplikat-Check.** URL normalisieren: Tracking-Parameter entfernen (`utm_*`, `fbclid`, `gclid`, `ref`, bei x.com auch `?s=…`/`?t=…`), Canonical-Form behalten. YouTube-Links auf `https://www.youtube.com/watch?v=<ID>` bringen, damit `youtu.be`- und `/shorts/`-Adressen desselben Videos zusammenfallen. Dann `80_Knowledge/Sources/` nach gleicher normalisierter URL oder gleichem Inhalt durchsuchen. Bei Treffer: nicht neu archivieren, sondern nur prüfen, ob neue Aussagen dazugekommen sind.
3. **Source-Notiz anlegen** nach Template, Dateiname `YYYY-MM-DD-<autor>-<slug>.md` (Datum = Original-Veröffentlichung). Als `url:` die normalisierte URL eintragen.
4. **Kernaussagen extrahieren — erst erfassen, dann synthetisieren.** Vor dem Schreiben intern jede tragende Aussage mit Quelle, Datum und Vertrauensgrad verknüpfen und Übereinstimmungen, Ergänzungen und Widersprüche zum Bestand unterscheiden. Keine Lücke plausibel ergänzen; Ergänzungen aus eigenem Wissen nie als Aussage der Quelle ausgeben. Jede benennbare, wiederverwendbare Erkenntnis über eine Arbeitsweise ist ein Kandidat für ein Pattern.
5. **Abgleich mit Bestand.** `80_Knowledge/Index.md` lesen. Pro Kernaussage entscheiden:
   - Passendes Pattern existiert → Notiz ergänzen (neuer Beleg, ggf. neue Vor-/Nachteile, Konfidenz neu ableiten).
   - Kein passendes Pattern → neue Pattern-Notiz nach Template anlegen. Schwelle: Das Konzept ist benennbar und über die konkrete Quelle hinaus wiederverwendbar.
   - Aussage widerspricht Bestandswissen → im betroffenen Pattern unter „Spannungen & offene Fragen“ als Trade-off festhalten, mit beiden Quellen.
6. **Repo-Verifikation.** Erwähnt die Quelle ein Repo, das unter `external_repos/` liegt (siehe `external_repos/INDEX.md`): zentrale Behauptungen dort stichprobenartig nachprüfen (Dateien/Struktur ansehen). Für bestätigte Aussagen eine neue Beleg-Zeile mit Repo-Pfad ergänzen (`YYYY-MM-DD · external_repos/<owner>/<repo>/<pfad> · verifiziert — …`); bestehende Beleg-Zeilen nie ändern. Abweichungen als Spannung notieren. Liegt das Repo nicht vor: Download gemäß `AGENTS.md` → „Repo-Import“ vorschlagen, aber nicht eigenmächtig klonen.
7. **Vergleiche & Index aktualisieren.** Betroffene Notizen in `80_Knowledge/Vergleiche/` aktualisieren (Stand-Datum setzen); neue Patterns und Vergleiche in `80_Knowledge/Index.md` mit Einzeiler eintragen.
8. **Validator ausführen.** `python 70_Scripts/validate_knowledge.py` — jeden gemeldeten Fehler beheben und erneut ausführen. Erfolg nie melden, bevor der Validator fehlerfrei durchläuft.
9. **Diff-Resümee ausgeben** (siehe Ausgabeformat).

## Grenzfälle

- Unklare Zuordnung oder mehrdeutige Aussage: als Frage in `00_Inbox/Fragen_an_Philipp.md` eintragen, nicht raten.
- Quelle enthält nichts über Arbeitsweisen (reine Meinung/News ohne wiederverwendbare Erkenntnis): kurz melden, nichts anlegen.
- Meta-Erkenntnisse über das Knowledge-System selbst (z.B. bessere Notiz-Struktur): Philipp vorschlagen, nicht eigenmächtig das Schema ändern.

## Häufige Fehler

- Eine unterstützte Quelle per WebFetch verarbeiten, obwohl der typgerechte Ingest-Pfad sie vollständig und lokal archiviert.
- Quelle einarbeiten, aber `status: neu` in ihrem Typordner stehen lassen — sie gilt dann weiter als offen.
- Zahlen aus mitgelieferten Charts und Tabellen übergehen, weil nur der Text gelesen wurde.
- Unvollständigen Thread-Abruf als vollständig behandeln, statt die Lücke zu vermerken oder nach dem Originaltext zu fragen.
- Dieselbe Quelle wegen Tracking-Parametern in der URL doppelt archivieren.
- Aussagen mehrerer Quellen entlang der Quellenreihenfolge einarbeiten, statt sie dem fachlich passenden Pattern zuzuordnen.
- Widersprüche glätten, statt sie als Spannung sichtbar zu machen.
- Bestehende Beleg-Zeilen umschreiben, statt neue Zeilen zu ergänzen.
- Erfolg melden, bevor der Validator fehlerfrei durchgelaufen ist.

## Ausgabeformat (Diff-Resümee)

- ✓ Quelle archiviert: `Sources/<datei>`
- ✓ Pattern ergänzt: `<Name>` (+n Belege, Konfidenz: <alt> → <neu>)
- ✓ Pattern NEU: `<Name>`
- ✓ Vergleich aktualisiert: `<Name>`
- ⚠ Spannung: <Ein-Satz-Beschreibung> → notiert in `<Pattern>`
- ? Offene Frage: <Frage> → `00_Inbox/Fragen_an_Philipp.md`
