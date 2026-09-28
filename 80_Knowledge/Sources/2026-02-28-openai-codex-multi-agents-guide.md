---
url: https://developers.openai.com/codex/multi-agent/
autor: OpenAI
datum: 2026-02-28
erfasst: 2026-08-04
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-28-openai-codex-multi-agents-guide.md
thema: Tools & Releases
zeitkritisch: ja
beleg_art: sekundaerquelle
---

# Codex Multi-Agent: Rollen, Limits und Sandbox-Vererbung

Deutsche Aufarbeitung (vibedeck, Sekundärquelle) der OpenAI-Doku zu experimentellen Multi-Agent-Workflows in der Codex CLI, Stand Februar 2026. Aktivierung per `[features] multi_agent = true` in `~/.codex/config.toml`. Codex orchestriert selbst: Agenten starten, Follow-ups routen, Ergebnisse konsolidieren. Herstellerdoku, Feature war als experimentell markiert.

## Kernaussagen
- Rollen (`default`, `worker`, `explorer`, `monitor`, eigene per `config_file`) sollen eng gefasst sein; `agents.max_threads` und `agents.max_depth` (Standard 1) begrenzen die Parallelität. → [[Kontrollierte-Agent-Parallelisierung]]
- Sub-Agenten erben die Sandbox-Policy, laufen aber mit non-interaktiven Approvals: Aktionen, die eine Freigabe bräuchten, schlagen fehl und werden dem Parent gemeldet. → [[Kontrollierte-Agent-Parallelisierung]]
- Typischer Einsatz: ein Agent pro Review-Punkt (Security, Bugs, Tests …), Ergebnisse zusammengefasst; Explorer read-only. → [[Plan-first-mit-getrenntem-Review]]

## Einordnung
Reine Feature-Beschreibung ohne Messung von Nutzen oder Tokenkosten paralleler Agenten. Nicht am Original geprüft.

## Verbindungen
- [[Kontrollierte-Agent-Parallelisierung]]
- [[2026-02-01-anthropic-docs-create-custom-subagents]]
- [[2026-02-07-jasonzhou-claude-code-agent-teams]]
