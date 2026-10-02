---
url: https://github.com/anthropics/claude-code
autor: anthropics
datum: 2026-10-02
erfasst: 2026-10-02
typ: repo
thema: Tools & Releases
zeitkritisch: ja
---

# Claude Code 2.1.287: Claude Mods, „You should know“ und der diff-Mod

Laut `CHANGELOG.md` (Eintrag 2.1.287, Repo-Stand Commit `52c76441`) gibt es „Claude Mods“, also Plugins, die tieferes Verhalten ändern dürfen. Der Ordner `mods/` im Repo enthält die vier eingebauten Mods `sec-default`, `diff`, `telemetry` und `agents-md` im Quelltext (`mods/README.md`). Zusätzlich gilt laut CHANGELOG 1M-Kontext für Opus 4.7+ und Fable auf Bedrock, Vertex, Foundry und dem Claude-apps-Gateway ohne `[1m]`-Suffix. Gelesen, nichts ausgeführt.

## Kernaussagen
- Ein Mod ist ein Plugin, dessen Verhalten in einem Hooks-Modul liegt (`register(on, options)`); `mods/README.md` beschreibt Aufbau und Tests (`claude plugin test mods/diff`).
- „You should know“ ist ein eingebauter Mod: ein Seitenagent weist auf Dinge hin, die du oder Claude übersehen könnten. Einschalten mit `/plugin enable cc-plugin-you-should-know@builtin` (laut CHANGELOG nur für First-Party-Sitzungen mit eingeschalteter Telemetrie).
- Der `diff`-Mod liefert `/diff`: die uncommitteten Änderungen in einem Panel neben dem Transkript, Datei für Datei mit Hunks, live aktualisiert (`mods/diff/README.md`).
- `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` hält die Fenster bei 200K (CHANGELOG-Eintrag zum 1M-Standard).
- Einen Mod im Quelltext ausprobieren: `claude --plugin-dir mods/diff`.

## Einordnung
Für Nutzer ist `/diff` sofort nützlich; „You should know“ ist ein Experiment mit Telemetrie-Voraussetzung. Die Mod-Schnittstelle selbst ist für Plugin-Autoren relevant.

## Verbindungen
- [[Erweiterungs-Ebenen-Zuordnung]]
