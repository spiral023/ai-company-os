# Hook-erzwungene-Skill-Aktivierung

**Konfidenz:** meinung

## Zweck

Verhindert, dass ein inhaltlich guter Skill folgenlos bleibt, weil die `description`-basierte Trigger-Heuristik ihn nicht zuverlässig auslöst. Adressiert den in [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]] bereits benannten Fehlermodus „inhaltlich guter Skill wird zu selten aktiviert“ mit einem strukturellen statt einem sprachlichen Mittel.

## Funktionsweise

Statt sich ausschließlich auf die Beschreibungsqualität zu verlassen, prüft ein `UserPromptSubmit`-Hook den eingehenden Prompt technisch auf Keywords und Intent, **bevor** das Modell die Nachricht überhaupt sieht, und injiziert bei Treffer eine formatierte Erinnerung in den Kontext (Beispiel: eine Frage nach dem Layout-System löst „SKILL ACTIVATION CHECK — Use project-catalog-developer skill“ aus). Ergänzend prüft ein nach der Antwort laufender `Stop`-Hook die geänderten Dateien auf riskante Muster (try-catch-Blöcke, Datenbank-Operationen, async-Funktionen) und zeigt eine nicht-blockierende Selbstprüfungs-Erinnerung („Did you add error handling?“). Eine verwandte Variante nutzt einen „Do more“-Hook nach jedem `Stop`, der automatisch eine Fortsetzungsaufforderung nachschiebt, um stundenlange autonome Läufe ohne menschliches Eingreifen zu erzwingen.

## Vorteile

- Macht Skill-Aktivierung deterministisch statt probabilistisch — der Hook feuert bei einem Keyword-/Intent-Treffer zuverlässig, unabhängig davon, wie gut das Modell die `description` gerade interpretiert.
- Der nachgeschaltete `Stop`-Hook fängt einen anderen Fehlermodus als der `UserPromptSubmit`-Hook ab: nicht ausbleibende Aktivierung, sondern übersehene Sorgfaltspflichten nach der Änderung.
- Ergänzt statt ersetzt die Trigger-Qualitätsarbeit aus [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]] — beide Mittel greifen an unterschiedlichen Stellen derselben Ursache.

## Nachteile & Grenzen

- Erfordert Hook-Infrastruktur und Keyword-/Intent-Pflege außerhalb der Skill-Datei selbst — ein zweiter Ort, an dem Trigger-Logik gepflegt werden muss.
- Nur eine einzelne Quelle (zitiertes Beispiel aus einem Blogpost, nicht selbst verifiziert) belegt den Mechanismus; keine Zahl dazu, wie viel zuverlässiger die Aktivierung dadurch tatsächlich wird.
- Ein zu aggressiver „Do more“-Hook kann autonome Läufe über den eigentlich sinnvollen Punkt hinaus fortsetzen, wenn kein Abbruchkriterium definiert ist.

## Wann einsetzen, wann nicht

- Einsetzen: bei Skills, deren ausbleibende Aktivierung teuer wäre (Sicherheits-/Compliance-relevante Checks, immer wieder vergessene Konventionen), und wenn Beschreibungs-Tuning allein nicht ausreicht.
- Nicht einsetzen: bei Skills mit bereits verlässlichem Trigger-Verhalten oder geringem Schaden bei Nichtauslösung — dort ist der Infrastrukturaufwand unverhältnismäßig.

## Belege

- 2026-01-25 · [[2026-01-25-sankalp-claude-code-experience]] · meinung — Zitiert ein Beispiel aus einem anderen Blogpost (`UserPromptSubmit`-Hook mit Keyword-/Intent-Prüfung plus injizierter Erinnerung, `Stop`-Hook für riskante Code-Muster) und ergänzt eine eigene Praxis: `CLAUDE.md` in kleine Skills aufteilen und Hooks nutzen, um Claude an bestimmte Skills zu erinnern, sobald bestimmte Dateien angefasst werden.
- 2026-02-01 · [[2026-02-01-anthropic-docs-automate-workflows-with-hooks]] · meinung — Anthropics eigene Hooks-Doku bestätigt technisch die Voraussetzung dieses Patterns: `matcher` grenzt Hooks gezielt auf einzelne Tools oder Event-Typen ein (`"Bash"`, `"Edit|Write"`), statt bei jedem Aufruf jedes Tools zu feuern — dieselbe Zielgerichtetheit, die die Keyword-/Intent-Prüfung im `UserPromptSubmit`-Hook technisch voraussetzt. Bestätigt damit den zugrunde liegenden Mechanismus, nicht aber die spezifische Skill-Aktivierungs-Anwendung selbst — `UserPromptSubmit` fehlt sogar in Anthropics eigener, erkennbar unvollständiger Event-Tabelle in dieser Quelle.
- 2026-07-21 · [[2026-07-21-promptgefluester-prompt-engineering-ist-tot-und-keiner-hats-gemerkt-was-meine-ich-damit]] · meinung — Creator begründet hook-basierte Skills damit, dass Initial-Regeln im wachsenden Context nicht mehr eingehalten werden und Regeln im Prozess nachgeladen werden sollten. Nur Behauptung ohne Messung.
- 2026-08-14 · [[2026-08-14-agenticjames-ai-memory-is-trash-heres-some-solutions]] · meinung — Nennt Hooks, die beim Start und pro Chat-Turn eine Zusammenfassung relevanter Erinnerungen in das Context Window injizieren. Übertragung des Hook-Prinzips von Skills auf Memory; Token-Kosten pro Turn werden nicht genannt.

## Spannungen & offene Fragen

- Die spezifische Skill-Aktivierungs-Anwendung bleibt einzelquellig (Sankalp zitiert einen fremden Blogpost) — der zugrunde liegende Hook-Mechanismus (`matcher`, `UserPromptSubmit`) ist seit 2026-02-01 durch Anthropics eigene Doku technisch bestätigt, aber ohne den konkreten Skill-Aktivierungs-Anwendungsfall zu erwähnen.

## Verwandte Patterns

- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- [[Erweiterungs-Ebenen-Zuordnung]]
