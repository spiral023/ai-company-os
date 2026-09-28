---
url: https://x.com/hooeem/status/2007914329748668472
autor: hoeem (@hooeem)
datum: 2026-01-22
erfasst: 2026-08-04
typ: tweet
rohquelle: 00_Inbox/Quellen/X/2026-01-22-hooeem-claude-code-guide.md
---

# Claude Code lernen: Ein 7-Schritte-Plan aus einem Anthropic-Kurs

hoeem fasst zusammen, was er aus dem zweistündigen Anthropic-Academy-Kurs „Claude Code in Action“ mitgenommen hat, und ordnet es zu sieben Stationen: Kernmechanik, Context Engineering, zwei Arbeitsmodi, Fehlerkorrektur, Hooks, Erweiterungen und CI/CD-Skalierung. Der Wert der Quelle liegt weniger in neuen Erkenntnissen als in der kompakten, gut sortierten Übersicht über Claude-Code-Grundfunktionen — praktisch jede Einzelaussage findet sich bereits ausführlicher in bestehenden Quellen und Patterns dieser Wissensbasis.

## Kernmechanik und Rollenteilung

Claude arbeitet laut der Quelle in einer festen Vier-Schritte-Schleife: Aufgabe erhalten, Kontext sammeln (Dateien lesen), Plan formulieren, Maßnahmen ergreifen (Dateien ändern, Tests ausführen). Die zentrale Lektion daraus: Claudes eigentliche Fähigkeit ist nicht reines Modell-„IQ“, sondern das Verketten von Tool-Aufrufen — das Modell „sieht“ den Rechner nicht selbst, sondern ist darauf angewiesen, dass der Assistent Anweisungen anhängt und formatierte Antworten ausführt. Wer die Tools nicht kontrolliert, steuert blind.

## Context Engineering

`/init` erzeugt einmalig eine `CLAUDE.md` als Architektur-Karte des Projekts — wichtig dabei: Ihr Inhalt wird in **jede einzelne Anfrage** aufgenommen, weshalb sie schlank bleiben muss. Darüber hinaus beschreibt die Quelle ein Drei-Schichten-Gedächtnis: Project Level (ins Repo committet, geteilt), Local Level (von Git ignoriert, persönlich) und Machine Level (global über alle Projekte hinweg). Ergänzend rät sie, mit `@dateiname` gezielt genau die Datei zu referenzieren, die gebraucht wird, statt das Modell raten zu lassen — das spart Tokens und erhöht die Treffergenauigkeit.

## Zwei Arbeitsmodi

Die Quelle unterscheidet „Planung“ (Shift+Tab zweimal, für Breite — z. B. ein Refactoring über zehn Dateien) von „Ultrathink“/Extended Thinking (für Tiefe — z. B. das Debuggen einer Race Condition mit erweitertem Reasoning-Budget). Beide Modi verbrauchen laut Quelle zusätzliche Tokens und sollten deshalb gezielt statt reflexhaft eingesetzt werden. Ergänzend empfiehlt sie, Screenshots per Copy-Paste (Control-V, auch auf macOS) für visuellen Kontext bei UI-Bugs einzufügen.

## Fehlerkorrektur statt Diskussion

Bei beginnender Halluzination soll man nicht mit dem Modell diskutieren, sondern die Timeline kontrollieren: `Escape` stoppt sofort; `Escape` + eine mit `#` eingefügte Erinnerung korrigiert und lehrt gleichzeitig, damit derselbe Fehler nicht wiederkehrt; doppeltes `Escape` (Rewind) springt vor den Fehler zurück und entfernt den schlechten Kontext vollständig; `/compact` fasst eine zu lang gewordene Konversation zusammen, ohne die bereits gelernten Lektionen zu verlieren.

## Hooks als Guardrails

Drei Beispiele aus `.claude/settings.local.json`: Ein Pre-Hook überwacht `read`/`grep`-Aufrufe und beendet sich mit Exit-Code 2, sobald der Pfad `.env` enthält — entscheidend ist, die Fehlermeldung nach `stderr` zu schreiben, denn nur so wird sie an Claude zurückgefüttert und zwingt es, den Block zu erkennen und die Strategie zu ändern. Ein Post-Hook führt nach jedem Edit `tsc --no-emit` aus und spielt gefundene Typfehler sofort zurück, damit sich Claude selbst korrigiert. Ein drittes „Anti-Bloat“-Beispiel lässt einen Hook eine zweite Claude-Instanz starten, die vor jedem Commit gezielt auf doppelten Code prüft.

## Erweiterungen und Skalierung

Wiederkehrende, komplexe Prompts werden als Markdown-Datei in `.claude/commands/` (z. B. `audit.md`) hinterlegt und per `/audit` sofort ausgeführt. Über MCP (`claude mcp add [name]`) lassen sich externe Tools wie Playwright anbinden, sodass Claude einen echten Browser steuert; Tools können in den Settings für einen schnelleren Workflow automatisch genehmigt werden. Für die Skalierung über den Einzel-Chat hinaus nennt die Quelle die GitHub-App (automatische PR-Prüfung auf Bugs/Sicherheitsrisiken), Custom Instructions in `.github/workflows` für teamspezifische Coding-Standards und das Claude Code SDK, um dieselbe Intelligenz direkt in Python-/TypeScript-CI/CD-Pipelines einzubetten.

## Einordnung

Die Quelle ist eine deutsche Sekundäraufarbeitung (vibedeck) eines Tweets, der selbst nur eine Mitschrift eines bezahlten Anthropic-Kurses ist — der Kurs selbst ist nicht verlinkt oder überprüfbar, es handelt sich also um Wiedergabe aus dritter Hand ohne eigene Messung. Nichts an den Aussagen ist quantifiziert („spart Tokens“, „erhöht Genauigkeit“ — keine Zahl); das deckt sich mit dem Charakter einer Lern-Zusammenfassung, nicht einer Fallstudie. Inhaltlich deckt sich praktisch jede Einzelaussage mit bereits ausführlicher belegten Patterns dieser Wissensbasis — die Drei-Schichten-Gedächtnis-Beschreibung ist eine vereinfachte Variante der in [[AGENTS-md-Onboarding-Design]] bereits per offizieller Anthropic-Doku belegten fünf Ablageorte, die Panic-Buttons sind eine kompakte Neuauflage der in [[Kontext-Hygiene-Entscheidungsbaum]] bereits mehrfach belegten `/rewind`/`/compact`-Mechanik. Als eigenständigen, bisher so nicht vermerkten Belegwert liefert sie vor allem drei Details: den `Escape`+`#`-Kombigriff als benannten „Panic Button“ (statt nur als generelle `#`-Regel wie bisher), das konkrete `tsc --no-emit`-Post-Hook-Beispiel als Typsicherheits-Feedback-Loop, und den Hinweis, dass ein Hook selbst eine zweite Claude-Instanz für einen Anti-Bloat-Check vor dem Commit anstoßen kann. Weil die Quelle drei Weiterverarbeitungsstufen (Kurs → Tweet → vibedeck-Übersetzung) von der Primärquelle entfernt ist, hebt sie die Konfidenz keines betroffenen Patterns an — sie bleibt Beleg vom Typ `meinung`, wie die bisherigen Tweet-Quellen zum Thema.

## Kernaussagen

- Claudes Kernfähigkeit ist Tool-Verkettung, nicht reine Modell-Intelligenz — das Modell „sieht“ den Rechner nur über die vom Harness angehängten Anweisungen. → [[Great-Decoupling-Rollenverstaendnis]]
- `CLAUDE.md` wird in jede Anfrage aufgenommen und muss deshalb schlank bleiben; ein Drei-Schichten-Gedächtnis (Project/Local/Machine) trennt geteilte, persönliche und globale Anweisungen. → [[AGENTS-md-Onboarding-Design]]
- Gezielte Dateireferenzen per `@dateiname` statt Modell-Raten sparen Tokens und erhöhen die Treffergenauigkeit. → [[Kontext-Hygiene-Entscheidungsbaum]]
- Plan Mode (Shift+Tab x2) für Breite und Extended Thinking („Ultrathink“) für Tiefe sind zwei unterschiedliche, jeweils zusätzlich Tokens kostende Arbeitsmodi. → [[Plan-first-mit-getrenntem-Review]]
- Bei Fehlentwicklung wird die Timeline kontrolliert statt diskutiert: Escape zum Stoppen, Escape+`#`-Erinnerung zum Korrigieren-und-Lehren, doppeltes Escape zum Rewind, `/compact` zum verlustarmen Verdichten. → [[Kontext-Hygiene-Entscheidungsbaum]]
- Der Escape+`#`-Kombigriff, um einen erkannten Fehler dauerhaft als Erinnerung zu vermerken, deckt sich mit der bereits belegten Praxis, Regeln erst nach einer zweimal nötigen Korrektur in die Agent-Datei aufzunehmen. → [[AGENTS-md-Onboarding-Design]]
- Ein Pre-Hook mit Exit-Code 2 und `stderr`-Ausgabe blockiert `.env`-Zugriffe technisch und füttert die Blockade als Feedback an das Modell zurück. → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- Ein Post-Hook, der nach jedem Edit `tsc --no-emit` ausführt und Typfehler zurückspielt, macht Verifikation zum automatisierten Feedback-Loop statt zur manuellen Nachkontrolle. → [[Testharness-als-staerkster-Hebel]]
- Ein Hook kann vor dem Commit eine zweite Claude-Instanz anstoßen, die gezielt auf doppelten Code prüft — Review getrennt von der Erstellung, aber automatisch statt manuell ausgelöst. → [[Plan-first-mit-getrenntem-Review]]
- Wiederkehrende Prompts werden als Markdown-Datei in `.claude/commands/` hinterlegt und per Slash-Command deterministisch statt neu formuliert ausgelöst. → [[Skill-Call-Hierarchie]]
- MCP-Server (z. B. Playwright) geben Claude Zugriff auf externe Werkzeuge; Tools lassen sich für einen schnelleren Workflow automatisch genehmigen. → [[Erweiterungs-Ebenen-Zuordnung]]
- Die GitHub-App prüft Pull Requests automatisch, Custom Instructions in `.github/workflows` tragen Team-Standards in CI, und das Claude Code SDK bettet dieselbe Intelligenz in eigene CI/CD-Pipelines ein. → [[CI-Agent-mit-Review-Gate]]

## Verbindungen

- [[AGENTS-md-Onboarding-Design]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Erweiterungs-Ebenen-Zuordnung]]
- [[2026-08-04-anthropic-docs-claude-code-best-practices]]
- [[2026-01-25-sankalp-claude-code-experience]]
