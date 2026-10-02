---
url: https://github.com/thedaviddias/Front-End-Checklist
autor: thedaviddias
datum: 2026-10-02
erfasst: 2026-10-02
typ: repo
thema: Tools & Releases
zeitkritisch: ja
---

# Front-End-Checklist: CLI `@frontendchecklist/cli` mit Offline-Regeln und MCP-Server

Im Klon von thedaviddias/Front-End-Checklist (Stand Commit `7bfd8680`) beschreibt `packages/cli/README.md` die CLI `@frontendchecklist/cli`; die Regeln liegen im Paket, sie läuft offline. Die Haupt-`README.md` nennt 386 englische Regeln in 11 Kategorien und einen MCP-Server (`packages/mcp/`, öffentlich unter mcp.frontendchecklist.io). Gelesen, nichts ausgeführt.

## Kernaussagen
- Code prüfen: `npx -y @frontendchecklist/cli review src/`; auch per Pipe (`git diff --cached | frontendchecklist review -`).
- Öffentliche Seiten prüfen: `frontendchecklist audit https://example.com`; Regeln suchen mit `search`, einzelne mit `rule <id>`.
- Für Agenten und CI gebaut: JSON bei Pipe, Exit-Code 1 bei Funden ab `--fail-on`, `frontendchecklist skill` erzeugt eine `SKILL.md` für Coding-Agenten.
- MCP-Tools laut README unter anderem `review_code`, `search_rules`, `get_workflow`, `audit_url`; lokal als stdio-Server in `packages/mcp/src/cli.ts`.

## Einordnung
Ein schneller Frontend-Check vor dem Release ohne Konto und ohne Netz. Die Regeln sind allgemein; Treffer ersetzen kein Review des konkreten Produkts.

## Verbindungen
- [[Adversarialer-Pre-Launch-Check]]
