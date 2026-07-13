---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-20
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Superpowers für AI Coding Agents“ (inkl. Sicherheits-/Vertrauensbewertung)

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/03-tool-profile/01-coding-agent-werkzeuge/wka-superpowers-fuer-ai-coding-agents-2026-04-16.md`, aktualisiert 20.04.2026), Einordnung von `obra/superpowers` per README/SKILL.md-Zugriff, mit eigener Sicherheitsbewertung (Datum der Bewertung: 20.04.2026).

Kernpunkte, die über den bereits im eigenen Vergleich erfassten Stand hinausgehen:

- Umfang laut Artikel: ~154k GitHub-Stars, 355.657 Claude-Plugin-Installs (Stand 16.04.2026).
- Explizite Nuance: Skill-Disziplin gilt als zwingend, aber explizite Nutzerinstruktionen haben weiterhin Vorrang — das Framework beansprucht nicht, über Nutzer-/Repo-Regeln zu stehen.
- Codex-Support ist ein bewusst mitgedachter Pfad (Klonen nach `~/.codex/superpowers`, Sichtbarmachen über `~/.agents/skills/superpowers`, Windows-Junction-Anleitung ohne Developer Mode).
- Sicherheits-/Vertrauensbewertung (eigene Recherche des Wiki-Artikels, keine formale Garantie): keine sichtbare `.mcp.json`/Remote-Connector in der öffentlichen Plugin-Struktur; `SessionStart`-Hook liest nach öffentlichem Stand primär lokale Skill-Dateien. Aber: Anthropic weist in den Claude-Code-Power-User-Tips ausdrücklich darauf hin, dass Community-Marketplace-Plugins **nicht von Anthropic geprüft oder sanktioniert** werden; kein sichtbares „Anthropic verified“-Badge gefunden (Stand 20.04.2026); keine öffentliche Zusage gefunden, dass jede Aktualisierung erneut geprüft wird.
- Praktische Konsequenz aus der Bewertung: Superpowers sollte trotz offenem Repo wie „Drittcode mit Hooks“ behandelt werden — Hooks/Agents/Commands vor produktivem Einsatz und nach Updates gezielt prüfen.

## Kernaussagen

- Skill-Disziplin bei Superpowers ist zwingend gemeint, aber explizite Nutzerinstruktionen haben weiterhin Vorrang vor der Skill-Disziplin → [[Workflow-Frameworks]]
- Community-Marketplace-Plugins wie Superpowers sind von Anthropic nicht geprüft/sanktioniert und sollten wie Drittcode mit Hooks behandelt werden (Hooks/Agents/Commands vor Einsatz und nach Updates prüfen), auch wenn keine offensichtliche Datenexfiltration im öffentlichen Repo-Stand erkennbar ist → [[Workflow-Frameworks]]
