# Externe Skill-Quelle als Git Submodule einbinden

Beispiel:

```bash
git submodule add <REPO_URL> 30_Skills/external/sources/<source-id>
git submodule update --init --recursive
```

Vorher prüfen:

- Quelle vertrauenswürdig?
- Lizenz geeignet?
- Enthält das Repo Scripts?
- Enthält das Repo Secrets oder riskante Anweisungen?
- Soll der Inhalt wirklich als Submodule statt als Kopie/Fork geführt werden?

Nachher ausführen:

```bash
python 70_Scripts/external_skill_review.py --source <source-id>
```
