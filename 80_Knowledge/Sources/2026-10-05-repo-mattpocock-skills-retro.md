---
url: https://github.com/mattpocock/skills/tree/main/skills/engineering/retro
autor: mattpocock
datum: 2026-10-05
erfasst: 2026-10-05
typ: repo
thema: Arbeitsweisen
zeitkritisch: nein
---

# mattpocock/skills `retro`: Retrospektive einer Coding-Session verbessert die Umgebung, nicht den Code

Im Klon von mattpocock/skills (Stand Commit `4588b32`, Version 1.3.1) liegt `retro` unter `skills/engineering/retro/SKILL.md`. Laut `CHANGELOG.md` kam der Skill mit 1.3.0 (#1120) in den Engineering-Bereich und damit ins Claude-Code-Plugin; seit 1.3.1 (#1121) verweist `ask-matt` nach einem behobenen Bug auf `/retro`. Gelesen, nichts ausgeführt.

## Kernaussagen
- `retro` ist nur manuell aufrufbar (`disable-model-invocation: true`). Er liest die Logs der angegebenen Session, standardmäßig der aktuellen, und schlägt Änderungen an der Agent-Umgebung vor, sortiert nach Schwere.
- Sieben Prüfkategorien: Navigation (Hinweise auf schwer auffindbare Dateien), automatische Checks, Coding Standards für den Review-Agent, eine zu große globale `AGENTS.md`, Tool-Ökonomie (teure Tool-Aufrufe), No-ops (Anweisungen ohne Wirkung) und Zugang zu Informationen (z. B. Dev-Server-Logs).
- Mechanische Verstöße (fester Syntaxfehler, verbotene API, Importform, Dateiort) bekommen immer eine deterministische Prüfung: Linter-Regel, Pre-Commit-Hook oder CI-Job. `CODING_STANDARDS.md` bleibt für echte Ermessensfragen.
- Ein Repo ohne Pre-Commit-Hook und ohne CI-Job für Lint, Typecheck und Tests gilt selbst als Befund.
- Begründung im Skill: Der Implementierungs-Agent trägt den größten Kontextdruck, der Review-Agent sieht nur den Diff. Deshalb gehören Standards in den Review, und `CLAUDE.md`/`AGENTS.md` sollen fast nur Navigationshinweise enthalten.
- Abhängigkeit: Der Skill lädt zuerst `writing-for-agents` als Stilvorgabe.

## Einordnung
`retro` schließt den Kreis aus Implementieren und Review: Fehler einer Session werden zu Checks und Regeln, damit sie in der nächsten nicht wieder passieren. Er liefert nur Vorschläge; umsetzen muss der Mensch oder ein weiterer Auftrag.

## Verbindungen
- [[Plan-first-mit-getrenntem-Review]]
- [[AGENTS-md-Onboarding-Design]]
- [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]
- [[2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck]]
- [[2026-10-02-repo-mattpocock-skills]]
