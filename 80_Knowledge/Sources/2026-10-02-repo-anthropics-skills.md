---
url: https://github.com/anthropics/skills
autor: anthropics
datum: 2026-10-02
erfasst: 2026-10-02
typ: repo
thema: Tools & Releases
zeitkritisch: ja
---

# claude-api-Skill: Eval-Flows für Aufbau, Hillclimbing, Kostensuche und Eval-Prüfung

Im Klon von anthropics/skills (Stand Commit `8a1541c4`) enthält der Skill `skills/claude-api/` unter `shared/evals/` die Anleitungen `build-eval.md`, `eval-hillclimb.md`, `cost-hillclimb.md` und `eval-audit.md` sowie einen Ordner `report/`. In `skills/claude-api/SKILL.md` sind `build-eval` und `hillclimb` als Subcommands eingetragen, `eval-audit` und der Report-Aufruf stehen im Routing-Abschnitt. Alles gelesen, nichts ausgeführt.

## Kernaussagen
- `build-eval.md` führt per Interview zu einem Eval für eine Claude-Anwendung: Eingaben beschaffen, Grading-Methode festlegen, zwei Freigabepunkte, am Ende ein Runner-Skript. Vorher wird `eval-audit.md` als Checkliste geladen.
- `eval-hillclimb.md` iteriert gegen ein bestehendes Eval mit Train/Test-Split. Ohne lauffähiges Eval verweist die Anleitung zurück auf `build-eval`.
- `cost-hillclimb.md` ordnet die Kostensuche in fester Reihenfolge (zuerst Caching-Gesundheit, dann Modell × Effort und weitere Hebel) und misst Qualität gegen das Eval.
- `eval-audit.md` ist eine Gesundheits-Checkliste (Aufgabendesign, Harness, Metriken, Grader, Messbarkeit) und prüft auch große Fallmengen in drei Stufen.
- Aufruf: `/claude-api build-eval` und `/claude-api hillclimb`; ein HTML-Bericht entsteht mit `shared/evals/report/build-report.mjs`.

## Einordnung
Wer eine Claude-App auf ein neues Modell umstellt oder den Prompt ändert, bekommt eine geführte Eval-Pipeline statt eines selbstgebauten Skripts. Die Flows sind Anweisungen an den Agenten, kein eigenes Tool; sie brauchen API-Zugang und kosten Tokens je Durchlauf.

## Verbindungen
- [[Hillclimbing-mit-Holdout-Split]]
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
