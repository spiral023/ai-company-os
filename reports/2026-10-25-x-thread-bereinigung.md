# X-Threads: Gesprächsantworten aus Quellen entfernen

Stand: 25.10.2026. Lokale Bereinigung und Feed-Build, ohne neue X-API-Aufrufe.

## Ursache

Die Suche nach `conversation_id` und Autor liefert auch Antworten des Autors an andere Nutzer. Der Rückwärtslauf kann fremde Vorgänger mitbringen. Diese Treffer wurden bislang zusammen als Thread archiviert; ein gemeinsamer Autor beweist jedoch keine zusammenhängende Fortsetzung.

## Ergebnis

- 259 X-Notizen und 311 vorhandene API-Caches geprüft; keine unzuordenbaren Mehrpost-Notizen verbleiben.
- 228 Beiträge aus 52 Quellen entfernt: 4 Fremdposts, 222 Gesprächsantworten außerhalb der belegten Autorenkette und 2 reine Werbebeiträge. Darunter sind auch Folgeantworten entfernter Gesprächszweige.
- Insgesamt 56 Rohnotizen aktualisiert; bei vier weiteren Quellen wurden sachliche Ergänzungen ausdrücklich gekennzeichnet. 54 Cache-Dateien bereinigt.
- Hauptpost, echte Selbst-Antwortketten und einzeln geprüfte fachliche Ergänzungen bleiben mit unverändertem Originaltext erhalten. Die konkrete Auswahl der Ergänzungen steht in `scripts/config/x-thread-content.json`; weitere Antworten werden dadurch nicht freigegeben.
- Das Beispiel von Franz Bruckhoff enthält jetzt 2 statt 18 Posts: Hauptprompt und gekennzeichnete Einschränkung zu False Positives. Die angeführten Posts 3–18 sind entfernt.
- Betroffene Aufarbeitungen um Aussagen aus entfernten Antworten und veraltete Umfangsangaben bereinigt. Beim append-only Pattern „Adversarialer Pre-Launch-Check“ ergänzt eine datierte Korrektur die bisherige Belegzeile.
- Verarbeitungsstatus, Source-Verweise, ursprüngliche Quell-URLs und Tweet-IDs unverändert; lokal gesicherte Medien bleiben erhalten.

## Künftige Erfassung

`scripts/lib/x-thread-source.mjs` prüft Autor und konkrete `replied_to`-Kette vor Speicherung sowie beim Lesen älterer Caches. Der Markdown-Formatter wendet dieselbe Auswahl an. Reine Werbe-/Smalltalk-Fortsetzungen und ihre Folgeantworten werden ausgeschlossen. Ein ausdrücklich angefragter Post bleibt eine eigenständige Quelle, auch wenn er selbst eine Antwort ist.

Fachlich notwendige Autor-Ergänzungen werden einzeln geprüft und als solche gekennzeichnet. Automatisch werden keine neuen Gesprächszweige aufgenommen. Die Erfassungsregeln sind im X-Playbook dokumentiert.

`node scripts/clean-x-threads.mjs` erstellt eine Vorschau; `--apply` schreibt mit lokaler Sicherung. Der Lauf vom 25.10. liegt unter `tmp/quellen-lauf/x-thread-bereinigung-2026-10-25/`: `applied.json` dokumentiert die Auswahl einschließlich entfernter Texte, `backups/` enthält die ursprünglichen Dateien. Diese Sicherungen gehören nicht zum Feed.

## Prüfung

- 61 Node-Tests für X-Import, Thread-Auswahl, sichere Archivbereinigung, TikTok und Feed-Modell bestanden; zusätzlich 28 Python-Tests für Feed und CLI bestanden.
- Erneute Bereinigung: keine weiteren Änderungen, keine unzuordenbaren Notizen.
- Quellen-Pipeline konsistent; Themenprüfung erfolgreich.
- Knowledge-Validator: unverändert 53 bereits vor dem Lauf vorhandene Fehler, keine neuen Fehler.
- Syntaxprüfung der geänderten Scripts und `git diff --check` erfolgreich.
- Feed neu gebaut: 483 Quellen. Über `http://127.0.0.1:8766/` ausgelieferte Index- und Detaildaten bestätigen die bereinigte Beispielquelle mit zwei Posts und ohne die beanstandete Antwort an `@Serocu`.
