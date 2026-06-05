# Externe Skills Integrieren

## Zweck

Externe Skills sauber prüfen und verwalten, ohne ihnen automatisch zu vertrauen.

## Wann verwenden

Wenn ein externer Skill-Pack, ein GitHub-Repo oder eine kopierte Skill-Sammlung in das AI-Company-OS aufgenommen werden soll.

## Inputs

- Quelle
- Zweck
- Lizenz
- gewünschter Einsatzbereich

## Ablauf

1. Quelle erfassen:

```bash
python 70_Scripts/external_skill_intake.py --id example --name "Example" --source https://github.com/example/repo
```

2. Quelle manuell prüfen.
3. Lizenz prüfen.
4. Optional als Submodule, Fork oder Kopie unter `30_Skills/external/sources/` ablegen.
5. Review-Datei in `30_Skills/external/reviews/` ausfüllen.
6. Prüfung ausführen:

```bash
python 70_Scripts/external_skill_review.py --source example
```

7. Trust-Level erst nach Philipp-Freigabe erhöhen.
8. Einzelne Skills nur in Projekt-Repos kopieren, wenn:
   - Lizenz geklärt ist
   - Inhalt geprüft ist
   - keine riskanten Scripts enthalten sind
   - keine Konflikte mit `AGENTS.md` bestehen
   - Philipp zugestimmt hat

## Freigabe

Philipp muss freigeben, bevor externe Skills als `reviewed` oder `trusted` markiert oder produktiv verwendet werden.

## Output

- Registry-Eintrag
- Trust-Level
- offene Risiken
- Empfehlung zur Nutzung

## Empfohlene Skills

- skill-autoreview
- security-reviewer
- repo-import-review
