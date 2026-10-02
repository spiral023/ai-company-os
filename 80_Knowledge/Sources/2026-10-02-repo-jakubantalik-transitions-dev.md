---
url: https://github.com/Jakubantalik/transitions.dev
autor: Jakubantalik
datum: 2026-10-02
erfasst: 2026-10-02
typ: repo
thema: Tools & Releases
zeitkritisch: ja
---

# transitions.dev: „Transitions Agent“ scannt Motion, bewertet sie und behebt Funde

Im Klon von Jakubantalik/transitions.dev (Stand Commit `d8f2c222`) beschreibt `agent/README.md` den Transitions Agent: Er scannt die Codebasis auf fehlende oder uneinheitliche UI-Transitions, vergibt einen Motion-Score von 0 bis 100 und schlägt Fixes als Diffs vor. Zusätzlich liegt `skills/transitions-polish/SKILL.md` im Repo. Gelesen, nichts ausgeführt.

## Kernaussagen
- Scan: `npx transitions-agent` liefert Score, Funde und passende Rezepte der Bibliothek; Funde sind etwa `off-scale`, `recipe-mismatch`, `recipe-available`.
- Fixes: `npx transitions-agent fix` (Modus `polish`: Werte auf die Motion-Skala; `--mode revamp` installiert Bibliotheks-Rezepte, laut README Business-Plan), `--pr` öffnet einen Pull Request. Nichts wird ohne Bestätigung geändert.
- `npx transitions-agent skill` installiert einen Claude-Code-Skill, damit eine Bitte wie „check this app’s motion“ den ganzen Ablauf auslöst.
- `npx transitions-agent init-ci` richtet eine GitHub Action ein, die jeden Pull Request bewertet; `--min-score <n>` lässt CI unter einem Wert scheitern.
- MCP-Server: `claude mcp add --transport http transitions-agent https://api.transitions.dev/v1/agent/mcp --header "Authorization: Bearer $TRANSITIONS_AGENT_LICENSE"`, damit dein eigenes Claude die Fixes macht.

## Einordnung
Der Scan liefert eine messbare Zahl für ein sonst schwer prüfbares Thema. Gehostete Fixes brauchen ein Konto und eine Lizenz; der Scan allein läuft über `npx`.

## Verbindungen
- [[CI-Agent-mit-Review-Gate]]
