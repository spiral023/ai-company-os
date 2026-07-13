---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-16
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Everything Claude Code (ECC) für AI Coding Agents“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/03-tool-profile/01-coding-agent-werkzeuge/wka-everything-claude-code-ecc-fuer-ai-coding-agents-2026-04-16.md`), Einordnung des Repos `affaan-m/everything-claude-code` per README/CLAUDE.md/Quick-Reference-Zugriff.

Kernpunkte (kondensiert):

- ECC (~157k GitHub-Stars, Stand 16.04.2026) ist kein Skill-Paket, sondern ein breites Agent-Betriebssystem: Skills, Agents, Commands, Hooks, Rules, MCP-Konfigurationen, Security-/Verification-Lanes, Memory-/Session-Mechaniken, Continuous-Learning/Skill-Evolution.
- Cross-harness gedacht: nennt Claude Code, Codex, Cursor, OpenCode, Gemini als Zielumgebungen; für Codex gibt es ein eigenes Betriebsmodell (`.codex/config.toml`, `.codex/AGENTS.md`, `.agents/skills/`, `.codex/agents/`).
- Sichtbares Surface laut Working-Context: 47 Agents, 79 Commands, 181 Skills (README-Release-Surface nennt teils andere Zahlen — Marketing-/Release-Oberfläche und operative Arbeitsoberfläche divergieren).
- Skill-Provenance-Modell: trennt kuratierte Skills im Repo von lokal gelernten, importierten und evolvierten Skills (`SKILL-PLACEMENT-POLICY`).
- Kritische Punkte: hoher Einarbeitungsaufwand, unterschiedliche Zählstände zwischen README und Working-Context, Risiko dass große Skill-Portfolios ohne diszipliniertes Kuratieren in Wartungsaufwand kippen.
- Einordnung: „nicht nur Skill-Sammlung, nicht nur Workflow-Engine, sondern umfassendes Harness-Performance-System mit starkem Cross-Harness-Fokus.“

## Kernaussagen

- ECC ist ein umfassendes Agent-Betriebssystem (Skills+Hooks+Memory+Security+Continuous Learning), nicht nur ein Workflow wie GSD oder ein Skill-Regime wie Superpowers → [[Workflow-Frameworks]]
- Cross-Harness-Support (Claude Code, Codex, Cursor, OpenCode, Gemini) mit eigenem Codex-Betriebsmodell ist ungewöhnlich breit im Vergleich zu den anderen Frameworks → [[Workflow-Frameworks]]
- Große Skill-Portfolios ohne diszipliniertes Kuratieren kippen in Wartungsaufwand — abweichende Zählstände zwischen README und Working-Context als Warnsignal → [[Workflow-Frameworks]]
