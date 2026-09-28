---
url: https://code.claude.com/docs/en/plugin-evals
autor: Claude Code Docs
datum: 2026-09-14
erfasst: 2026-09-14
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-09-14-code-test-plugins-with-evals-claude-code-docs.md
thema: Tools & Releases
zeitkritisch: ja
---

# Plugin-Evals mit `claude plugin eval` und No-Plugin-Baseline

Die offizielle Doku (Stand 2026-09-14, Datum unsicher, ab Claude Code v2.1.269) beschreibt, wie Plugins und Skills per Eval-Cases getestet werden. Jeder Case läuft mit und ohne Plugin; das Delta (Δ) zeigt den Beitrag des Plugins. Herstellerdokumentation, also belastbar für das Verhalten, nicht für den Nutzen.

## Kernaussagen

- Case = `prompt.md` plus Grader; Grader-Typen u. a. `llm`, regex und `tool_used` (prüft z. B. ob der Skill gefeuert hat).
- Pro Case ein Grader auf das Ergebnis und einer auf den Weg dorthin; lange Outputs per Regex, `llm`-Grader nur für kurze Outputs mit konkreten PASS/FAIL-Regeln.
- Ist Δ negativ trotz bestandenem `tool_used`, zuerst den Judge verdächtigen.
- CI-Gate mit `--threshold` und `--max-cost-usd`; Läufe kosten echte Nutzung bzw. API-Geld.

## Einordnung

Operationalisiert Baseline-Evals für Skills konkret. Kosten: Judge-Läufe und mehrere Runs pro Case.

## Verbindungen

- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- [[2026-07-01-anthropic-skill-creator-skill-md]]
- [[CI-Agent-mit-Review-Gate]]
