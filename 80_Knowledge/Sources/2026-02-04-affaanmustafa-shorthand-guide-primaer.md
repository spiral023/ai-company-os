---
url: https://x.com/affaanmustafa/status/2012378465664745795
autor: "@affaanmustafa"
datum: 2026-02-04
erfasst: 2026-07-13
typ: tweet
---

# @affaanmustafa zu „The Shorthand Guide to Everything Claude Code“ (Primärquelle)

## Inhalt

Primärquelle, die bereits über zwei Sekundärsynthesen (vibe-repo-Wiki) erfasst war ([[2026-04-13-wiki-compiler-shorthand-guide-claude-code]] als eigene Notiz, außerdem als Beleg in mehreren Patterns). Diese Notiz ergänzt konkrete operative Details aus dem Original nach 10 Monaten täglicher Nutzung, die in den Zusammenfassungen fehlten.

Konkrete Faustregel für MCPs/Plugins: 20-30 MCPs in der Config, aber unter 10 aktiviert / unter 80 Tools aktiv — ein 200k-Kontextfenster kann mit zu vielen aktiven Tools vor der Kompaktierung effektiv nur noch 70k groß sein. Konkretes Hook-Beispiel mit Matcher-Syntax (`tool == "Bash" && tool_input.command matches "(npm|pnpm|yarn|cargo|pytest)"`) für eine tmux-Erinnerung. `hookify`-Plugin erlaubt, Hooks im Gespräch zu erstellen statt JSON manuell zu schreiben. Konkretes eigenes Setup: 14 aktive Plugins (u.a. `ralph-wiggum` für Loop-Automation, `frontend-design`, `commit-commands`, `security-guidance`, `pr-review-toolkit`, `typescript-lsp`, `hookify`, `context7`), aber „meist nur 4-5 gleichzeitig aktiv“. Vollständige MCP-Server-Liste (GitHub, Firecrawl, Supabase, Memory, Sequential-Thinking, Vercel, Railway, mehrere Cloudflare-Endpunkte, ClickHouse, AbletonMCP, Magic) mit projektspezifischer Deaktivierung in `~/.claude.json` unter `disabledMcpServers`. Konkrete Key-Hooks: PreToolUse blockiert `.md`-Writes außer README/CLAUDE, öffnet Editor vor `git push`; PostToolUse führt `prettier --write` und `tsc --noEmit` nach TS-Edits aus, warnt vor `console.log`. Tastaturkürzel: `Ctrl+U` (Zeile löschen), `!` (Bash-Präfix), `@` (Dateisuche), `Tab` (Thinking-Display umschalten), `Esc Esc` (unterbrechen/wiederherstellen). Editor-Präferenz Zed mit `Ctrl+G` (springt zur gerade bearbeiteten Datei) und Split-Screen-Workflow.

## Kernaussagen

- Konkrete MCP/Tool-Faustregel: 20-30 MCPs konfigurieren, aber unter 10 gleichzeitig aktivieren / unter 80 Tools aktiv halten — sonst schrumpft das effektive Kontextfenster drastisch vor der Kompaktierung → [[Erweiterungs-Ebenen-Zuordnung]]
- Reale Plugin-Nutzung bleibt trotz vieler installierter Plugins klein (4-5 gleichzeitig aktiv von 14 installierten) — Konfiguration bewusst schmal halten, auch wenn viel verfügbar ist → [[Erweiterungs-Ebenen-Zuordnung]]
- Konkrete Hook-Beispiele mit Matcher-Syntax zeigen den Unterschied zwischen PreToolUse (Validierung/Blockieren vor Aktionen) und PostToolUse (automatische Nachbearbeitung wie Formatierung/Typecheck) in der Praxis → [[Erweiterungs-Ebenen-Zuordnung]]
