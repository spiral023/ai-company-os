---
url: https://github.com/alirezarezvani/claude-skills/tree/main/engineering/skill-doctor
autor: alirezarezvani
datum: 2026-10-05
erfasst: 2026-10-05
typ: repo
thema: Arbeitsweisen
zeitkritisch: nein
---

# `skill-doctor` (alirezarezvani/claude-skills): Agent-Setup aus echten Sessions benoten

Im Klon von alirezarezvani/claude-skills (Stand Commit `19392f7a`) liegt `engineering/skill-doctor/` mit SKILL.md (Version 1.0.0, MIT), drei Python-Skripten und zwei Bewertungsrubriken. Laut Metadaten ein Nachbau von `skill-doctor` aus warpdotdev/common-skills (MIT). Gelesen, nichts ausgeführt.

## Kernaussagen
- Fünf Schritte: lokale Claude-Code- und Codex-Sessions einsammeln und Secrets schwärzen, jede Session nach Effizienz- und Code-Qualitäts-Rubrik bewerten, belegte Skill-Änderungen als Diff entwerfen, alles durch einen deterministischen Aggregator prüfen, einen HTML-Bericht erzeugen.
- Das Modell vergibt nur Labels aus den Rubrik-Tabellen; Zahlen rechnet der Aggregator aus (Gesamtnote 0,5 × Effizienz + 0,35 × Code-Qualität + 0,15 × Skill-Abdeckung). Exit-Code 4 stoppt den Lauf.
- Jeder Änderungsvorschlag muss auf eine bewertete Session verweisen, sonst fällt er weg. Null Vorschläge gilt als Erfolg.
- Echte Skill-Dateien werden nur nach ausdrücklichem Ja pro Skill geändert; Transkripte verlassen den Rechner nie.

## Einordnung
Schaut wie eine Retro auf vergangene Sessions, aber über ein Zeitfenster vieler Sessions und mit Benotung. Der Fokus liegt auf den Skills selbst, nicht auf Checks oder Repo-Struktur.

## Verbindungen
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- [[Hillclimbing-mit-Holdout-Split]]
