---
url: https://code.claude.com/docs/en/skills
autor: Anthropic Docs
datum: 2026-02-01
erfasst: 2026-08-04
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-extend-claude-with-skills.md
thema: Tools & Releases
zeitkritisch: ja
beleg_art: sekundaerquelle
---

# Skills in Claude Code: Frontmatter, Ort und Ausführung

Deutsche Aufarbeitung (vibedeck) der Anthropic-Doku zu Skills; Feldnamen sind nicht am Original geprüft, Stand Februar 2026.

## Kernaussagen
- Ein Skill ist `SKILL.md` mit YAML-Frontmatter; Commands unter `.claude/commands` und Skills erzeugen denselben `/name`. Orte: Personal, Project, Plugin. → [[Erweiterungs-Ebenen-Zuordnung]]
- `disable-model-invocation`, `user-invocable`, `allowed-tools` steuern, wer auslöst. → [[Skill-Call-Hierarchie]]
- `context: fork` läuft im Subagent; ein `!`-Befehl im Skill fügt Shell-Ausgabe vor dem Start ein.
- Triggert ein Skill nicht, ist meist die `description` schuld.

## Einordnung
Referenzwissen, keine Neuheit; ergänzt Bestandsnotizen um Frontmatter-Details. Lies für Feldnamen die Primärquelle.

## Verbindungen
- [[2026-02-01-anthropic-docs-extend-claude-code]]
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
