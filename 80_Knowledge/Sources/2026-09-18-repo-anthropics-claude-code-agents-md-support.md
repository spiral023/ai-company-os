---
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
autor: "Anthropic (Claude Code Changelog)"
datum: 2026-09-18
erfasst: 2026-10-07
typ: repo
thema: Arbeitsweisen
zeitkritisch: ja
---

# Claude Code liest AGENTS.md: Unterstützung seit Version 2.1.277

Im Klon von anthropics/claude-code (Stand Commit `2bfb629`, Version 2.1.289) steht in `CHANGELOG.md` unter 2.1.277: „Added AGENTS.md support: in a project with no CLAUDE.md, Claude Code reads AGENTS.md instead; change it under "Project instructions" in `/config`". Laut `feed.xml` erschien 2.1.277 am 18.09.2026. Gelesen, nichts ausgeführt.

## Kernaussagen

- Seit 2.1.277 (18.09.2026) liest Claude Code `AGENTS.md`, wenn ein Projekt keine `CLAUDE.md` hat. Gibt es beide Dateien, bleibt `CLAUDE.md` maßgeblich; das Verhalten lässt sich in `/config` unter „Project instructions“ ändern.
- Seit 2.1.281 (23.09.2026) gilt die AGENTS.md-Unterstützung auch über Amazon Bedrock, Google Vertex AI, Microsoft Foundry, LLM-Gateways und in Sessions mit abgeschalteter Telemetrie.
- Werkzeuge gegen zu lange Instruktionsdateien im selben Changelog: Die Warnschwelle „CLAUDE.md is too long“ skaliert seit 2.1.169 mit dem Kontextfenster des Modells. Seit 2.1.206 schlägt `/doctor` vor, eingecheckte `CLAUDE.md`-Dateien um Inhalte zu kürzen, die Claude aus dem Code ableiten kann. Seit 2.1.281 zählt der Startup-Hinweis mehrere mittelgroße Instruktionsdateien und `@`-Imports zusammen. Seit 2.1.283 prüft `/doctor prompt-audit` CLAUDE.md-Dateien, Skills, Agents und Commands auf Prompt-Muster für ältere Modelle.

## Einordnung

Damit kann ein Repository eine einzige Instruktionsdatei für Claude Code und andere Agents wie Codex führen, die `AGENTS.md` lesen. Eine zusätzliche `CLAUDE.md` hat Vorrang und verdrängt die `AGENTS.md`, solange die Einstellung nicht geändert ist. Herstellerangabe aus dem Changelog; wie `@`-Imports oder verschachtelte `AGENTS.md`-Dateien in Unterordnern behandelt werden, sagt der Eintrag nicht.

## Verbindungen

- [[AGENTS-md-Onboarding-Design]]
- [[Erweiterungs-Ebenen-Zuordnung]]
- [[2026-09-14-developers-rethinking-skills-and-prompts-for-gpt-6-astra-op]]
