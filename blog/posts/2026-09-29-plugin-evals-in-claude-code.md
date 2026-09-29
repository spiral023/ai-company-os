---
titel: "Plugin-Evals in Claude Code: mit und ohne Plugin messen, im CI absichern"
datum: 2026-09-29
kategorie: kurz
zusammenfassung: "Mit claude plugin eval laufen Eval-Cases mit und ohne Plugin; das Delta zeigt den Beitrag. Ein CI-Gate begrenzt Schwelle und Kosten."
status: entwurf
quellen:
  - 2026-09-14-code-test-plugins-with-evals-claude-code-docs
---

Die offizielle Claude-Code-Doku beschreibt{q:1}, wie sich Plugins und Skills mit `claude plugin eval` testen lassen (laut Quelle ab Claude Code v2.1.269, Datum der Doku unsicher). Jeder Eval-Case besteht aus einer `prompt.md` und Gradern und läuft mit und ohne Plugin. Das Delta (Δ) zeigt, was das Plugin tatsächlich beiträgt.

Zu den Grader-Typen gehören `llm`, regex und `tool_used`, der prüft, ob ein Skill gefeuert hat. Die Doku empfiehlt pro Case zwei Grader: einen auf das Ergebnis, einen auf den Weg dorthin. Lange Outputs prüfst du per Regex, `llm`-Grader eignen sich nur für kurze Outputs mit konkreten PASS/FAIL-Regeln. Ist Δ negativ, obwohl `tool_used` besteht, solltest du zuerst den Judge verdächtigen.

Fürs CI gibt es ein Gate mit `--threshold` und `--max-cost-usd`. Die Läufe kosten echte Nutzung bzw. API-Geld, dazu kommen Judge-Läufe und mehrere Runs pro Case.

Das ist Herstellerdokumentation: belastbar für das Verhalten des Werkzeugs, nicht für den Nutzen deiner Plugins. Wenn du Skills pflegst, starte mit wenigen Cases und setze die Kostenobergrenze von Anfang an.
