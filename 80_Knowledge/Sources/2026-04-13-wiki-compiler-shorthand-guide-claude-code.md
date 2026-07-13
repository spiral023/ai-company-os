---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-13
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „The Shorthand Guide to Everything Claude Code“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/02-agent-guides-und-templates/wka-shorthand-guide-claude-code-2026-04-13.md`), Zusammenfassung eines praxiserprobten persönlichen Claude-Code-Setups (u.a. X-Post @affaanmustafa).

Kernpunkte (kondensiert):

- Sechs Hook-Typen genannt: `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `PreCompact`, `Notification` — typische Nutzung: Erinnerungen vor riskanten Shell-Befehlen, automatische Formatierung/Typechecks nach Edits, Sicherheitswarnungen, Abschlussprüfungen.
- MCPs und Plugins: viele in der Konfiguration akzeptabel, aber nur wenige gleichzeitig aktiv halten — sonst sinkt das effektive Kontextfenster und das Signal-Rausch-Verhältnis verschlechtert sich.
- Rules/Memory: entweder eine zentrale `CLAUDE.md` oder ein modularer Rules-Ordner mit mehreren Markdown-Dateien für Security, Coding Style, Testing, Git-Workflow, Delegationsregeln, Performance/Modellwahl.
- Subagents sollen eng gescopt sein (Tools/MCP-Zugriff pro Rolle begrenzen), nicht maximal frei.
- Produktivitätstipps: `/fork` für parallele nicht überlappende Gesprächsstränge, Git Worktrees für parallele Arbeitskopien, manuelle Kontrollbefehle wie `/rewind`, `/compact`, `/checkpoints`.
- Zentrale Takeaway: Konfiguration ist eher feines Tuning als komplexe Architektur; Kontextfenster ist knappe Ressource und muss aktiv geschützt werden.

## Kernaussagen

- Hooks für deterministische, ereignisgetriebene Automatisierung (sechs Standard-Trigger-Punkte); MCP/Plugins bewusst klein halten, auch wenn viele konfiguriert sind → [[Erweiterungs-Ebenen-Zuordnung]]
- Subagents eng scopen statt überprivilegiert einzusetzen → [[Erweiterungs-Ebenen-Zuordnung]], [[Kontrollierte-Agent-Parallelisierung]]
