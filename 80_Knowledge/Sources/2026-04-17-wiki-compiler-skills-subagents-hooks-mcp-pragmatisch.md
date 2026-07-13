---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-17
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Skills, Subagents, Hooks und MCP pragmatisch einsetzen“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/02-agent-guides-und-templates/wka-skills-subagents-hooks-und-mcp-pragmatisch-einsetzen-2026-04-17.md`), synthetisiert aus offizieller Claude-Code-Doku und mehreren X-Posts.

Kernpunkte (kondensiert):

- Fünf Erweiterungsebenen mit klar unterschiedlicher Verantwortung: `CLAUDE.md` (immer gültige Regeln), Skills (on-demand Wissen/Workflows, Progressive Disclosure), Subagents (isolierte Arbeit mit eigenem Kontext/Rechten), Hooks (deterministische Automatisierung an Trigger-Punkten), MCP (Verbindung zu externen Daten/Diensten).
- Zentrale Fehlerquelle: dieselbe Anforderung wird gleichzeitig in mehreren Ebenen modelliert (`CLAUDE.md`, Skill, Hook) — das ist meist ein Designfehler.
- Mapping-Regel: immer gültige Regel → `CLAUDE.md`; wiederkehrender Ablauf → Skill; isolierte Teilaufgabe → Subagent; immer gleicher Trigger → Hook; externe Quelle/Aktion → MCP.
- Gute Skills: klare Trigger-Beschreibung, eine sauber gelöste Verantwortung statt zehn lose verwandter Probleme, Begründung für Grenzfälle.
- Gute Subagents: eng gescopte Tools/Permissions, kleinstmögliches passendes Modell, knappe Ergebnisrückmeldung; häufigster Fehler ist ein überprivilegierter General-Subagent.
- Hooks nur für deterministische Checks; MCP: lieber wenige passende Server aktiv als viele gleichzeitig (kostet Kontext, verschlechtert Signal-Rausch-Verhältnis).
- Sinnvolle Einführungsreihenfolge für Teams: kurze `CLAUDE.md` → 2-5 Skills → 1-2 Subagents → wenige Hooks → ausgewählte MCP-Server für echte Engpässe.

## Kernaussagen

- Die fünf Ebenen (`CLAUDE.md`, Skill, Subagent, Hook, MCP) tragen unterschiedliche Verantwortung; dieselbe Anforderung mehrfach zu modellieren ist ein Designfehler → [[Erweiterungs-Ebenen-Zuordnung]]
- Sinnvolle Einführungsreihenfolge: knapper Kern zuerst, dann schrittweise wenige Skills, Subagents, Hooks, MCP-Server → [[Erweiterungs-Ebenen-Zuordnung]]
