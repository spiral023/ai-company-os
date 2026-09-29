---
titel: "Plugin-Evals in Claude Code: mit und ohne Plugin messen, im CI absichern"
datum: 2026-09-30
kategorie: kurz
zusammenfassung: "Mit claude plugin eval laufen Eval-Cases mit und ohne Plugin; das Delta zeigt den Beitrag. Ein CI-Gate begrenzt Schwelle und Kosten."
status: freigegeben
geprueft_am: 2026-09-29
freigabe: automatisch
quellen:
  - 2026-09-14-code-test-plugins-with-evals-claude-code-docs
---

Mit `claude plugin eval` testest du Plugins und Skills in Claude Code gegen echte Aufgaben.{q:1} Jeder Eval-Case besteht aus einer `prompt.md` und Gradern und läuft einmal mit und einmal ohne Plugin. Das Delta (Δ) zeigt, was das Plugin beiträgt. Die Funktion gibt es laut Doku ab Claude Code v2.1.269.{q:1}

Zu den Grader-Typen gehören `llm`, Regex und `tool_used`, der prüft, ob ein Skill gefeuert hat. Die Doku empfiehlt pro Case zwei Grader: einen auf das Ergebnis, einen auf den Weg dorthin. Lange Outputs prüfst du per Regex. `llm`-Grader eignen sich nur für kurze Outputs mit konkreten PASS/FAIL-Regeln. Ist Δ negativ, obwohl `tool_used` besteht, verdächtige zuerst den Judge.

Im CI begrenzen `--threshold` und `--max-cost-usd` Schwelle und Kosten. Die Läufe verbrauchen echte Nutzung oder API-Geld, dazu kommen Judge-Läufe und mehrere Runs pro Case.

Die Doku zeigt, wie das Werkzeug funktioniert, nicht, ob deine Plugins etwas taugen. Wenn du Skills pflegst, starte mit wenigen Cases und setze die Kostenobergrenze von Anfang an.
