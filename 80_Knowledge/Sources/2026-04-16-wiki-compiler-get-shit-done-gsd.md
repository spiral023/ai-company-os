---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-16
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Get Shit Done (GSD) für AI Coding Agents“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/03-tool-profile/01-coding-agent-werkzeuge/wka-get-shit-done-gsd-fuer-ai-coding-agents-2026-04-16.md`), Einordnung von `gsd-build/get-shit-done` (~53,5k Stars, Paketversion 1.36.0, Stand 16.04.2026) per README/USER-GUIDE-Zugriff.

Kernpunkte, die über den bereits im eigenen Vergleich erfassten Stand hinausgehen (dort primär aus Repo-Struktur, hier zusätzlich aus README/Changelog/Docs):

- GSD positioniert sich explizit gegen „Context Rot“ über vier Bausteine: Context Engineering (persistente Dateien statt alles im Chat), Spec-driven Development (Requirements/Roadmap/atomare Pläne statt Zuruf), Subagent-Orchestrierung, Verifikation+atomare Commits.
- Explizit unterstützte Runtimes über Claude Code hinaus: Codex, Copilot, Gemini CLI, Cursor, Windsurf, Cline; Codex-Installation über `npx get-shit-done-cc --codex --global/--local`, Skills unter `~/.codex/skills/` bzw. `./.codex/skills/`, Verifikation über `$gsd-help`.
- `gsd-map-codebase` für Brownfield-Analyse bestehender Codebasen wird als besondere Stärke hervorgehoben (siehe auch Vergleichs-Artikel zu „persönlichen Learnings“).
- Wellenbasierte Ausführung: unabhängige Pläne parallel, abhängige Pläne sequentiell.
- Kritischer Punkt: die im Repo dokumentierte empfohlene Nutzung von `claude --dangerously-skip-permissions` passt nicht automatisch zu strengeren Governance-/Sicherheitsmodellen.

## Kernaussagen

- GSD ist explizit Multi-Runtime gedacht (Claude Code, Codex, Copilot, Gemini CLI, Cursor, Windsurf, Cline), nicht auf ein Harness beschränkt → [[Workflow-Frameworks]]
- Empfohlene Nutzung von `--dangerously-skip-permissions` im GSD-Standardpfad kollidiert mit strengeren Sicherheits-/Governance-Modellen und muss vor Übernahme geprüft werden → [[Workflow-Frameworks]]
