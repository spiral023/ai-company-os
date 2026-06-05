# Projekt Bootstrap

## Zweck

Aus einem Projekt-Kit ein startbares Projekt-Setup vorbereiten.

## Wann verwenden

Wenn ein neues Projekt-Repo für SaaS, Shopify App oder Website-Redesign entstehen soll.

## Inputs

- Projektart
- Projektname
- Zielgruppe
- Zweck

## Ablauf

1. Projektart bestimmen.
2. passenden Projekt-Kit auswählen.
3. Optional temporären Dry-Run in `tmp/` durchführen.
4. Projekt-Kit kopieren:

```bash
python 70_Scripts/create_project_kit.py --kit saas-webapp --name mein-produkt --target ../mein-produkt --copy-skills
```

5. Falls Skills separat kopiert werden sollen:

```bash
python 70_Scripts/install_project_skills.py --project-type saas-webapp --target ../mein-produkt
```

6. Zielprojekt später separat als eigenes Git-Repository initialisieren.
7. ersten Arbeitsauftrag an Claude Code oder Codex im Zielprojekt formulieren.
8. offene Fragen notieren.

## Output

- Projektstruktur
- Startdokumente
- empfohlene Skills
- offene Fragen
- erster Agent-Auftrag

## Empfohlene Skills

- project-bootstrap
- ask-user-question
