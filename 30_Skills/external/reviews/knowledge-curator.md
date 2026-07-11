# Review: knowledge-curator

Geprüft: 2026-07-12 (Skill `repo-import-review`-Schema)

## Kurzfazit

Ausgereifter Knowledge-Ingest-Skill (Herkunft: von Philipp bereitgestellt, ursprüngliche Quelle/Autor unbekannt) für ein anderes Zielsystem — eine Publishing-App mit typisiertem Frontmatter-Schema (`src/content/knowledge/`, `src/types/knowledge.ts`). Nicht direkt einsetzbar, aber methodisch wertvoll; die übertragbaren Lektionen wurden am 2026-07-12 in das eigene Knowledge-System übernommen.

## Nutzen

- Quellen-Playbooks pro Quellentyp (X/Twitter-Thread-Vollständigkeit, GitHub-Belege an Dateien/Releases binden, Abbruchbedingungen) → übernommen nach `30_Skills/local/knowledge-ingest/references/quellen-playbooks.md`.
- Prinzip „erst vollständig erfassen, dann synthetisieren; keine Lücke plausibel ergänzen" → übernommen in `knowledge-ingest` Schritt 4.
- URL-Normalisierung (Tracking-Parameter) für Dubletten-Checks → übernommen in Schritt 2.
- Maschineller Validator als Gate vor Erfolgsmeldung → als eigene, kleinere Python-Implementierung übernommen (`70_Scripts/validate_knowledge.py`, eigener Code, kein kopierter).
- „Häufige Fehler"-Abschnitte und Fehler-Gates → übernommen in beide Knowledge-Skills.

## Risiken

- Enthält ein Node-Script (`scripts/validate-knowledge-article.mjs`, 878 Zeilen, plus Tests). Gemäß AGENTS.md nicht automatisch ausführen; für unseren Zweck nicht benötigt (eigene Python-Implementierung existiert).
- Keine erkennbaren Secrets, keine Netzwerk-Zugriffe im Script (nur fs/path), keine Prompt-Injection-Muster in den Markdown-Dateien gefunden.

## Lizenzstatus

Unbekannt — keine LICENSE-Datei, kein Autor-/Quellhinweis enthalten. Deshalb: kein Code kopieren, nur als Konzept-Referenz nutzen. Der übernommene Python-Validator ist eine Eigenentwicklung.

## Empfohlene Integrationsform

Nur als Referenz nutzen (bereits geschehen). Keine Datei-Übernahme, kein Submodule, keine Script-Ausführung.

## Offene Fragen

- Ursprüngliche Quelle/Autor des Skills? (Für Lizenzklärung und spätere Updates interessant.)

## Philipp-Freigabe erforderlich

Nein — reine Referenznutzung, keine produktive Einbindung.
