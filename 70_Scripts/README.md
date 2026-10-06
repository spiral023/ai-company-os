# Scripts

Für die normale Bedienung bevorzugt `python ai.py` im Repo-Root verwenden. Die Scripts in diesem Ordner sind die darunterliegenden Werkzeuge für Automatisierung, Debugging und direkte Agent-Nutzung.

Kleine lokale Hilfsscripts für Phase 1.

- `skill_registry_check.py`: prüft Registry und lokale Skill-Pfade.
- `skill_autoreview.py`: zeigt Zeilenanzahl lokaler Skills und warnt bei langen Skills.
- `create_project_kit.py`: kopiert Projekt-Kits in Zielordner.
- `install_project_skills.py`: kopiert lokale Skills in Projekt-Repos.
- `external_skill_review.py`: prüft externe Skill-Quellen ohne Aktivierung.
- `external_skill_intake.py`: legt neue externe Quellen als Registry- und Review-Entwurf an.
- `quellen_pipeline.py`: Werkzeug für den Skill `quellen-verarbeiten` (`prep`, `plan`, `apply`, `fakten`, `check`); Arbeitsordner `tmp/quellen-lauf/<lauf>/`, Beschreibung im Skill.
- `feeds.py`: RSS-/Atom-Feeds registrieren (`add`), auflisten (`list`) und thematisch passende Artikel mit Begründung vorschlagen (`check`, optional `--thema`, `--alle`, `--ausgabe`); Bedienung über `python ai.py feeds`, Register unter `00_Inbox/Feeds/feeds.yaml`.
- `themen.py`: Themencluster für `80_Knowledge/` (`check`, `zuordnen`, `verwandt`, `luecken`, `index`, `blog`); Taxonomie und Zuordnung liegen in `80_Knowledge/Themen/`.
- `company_os_healthcheck.py`: führt die zentralen Repo-Checks gesammelt aus.
- `sync_ai_coding_dictionary.py`: spiegelt das AI Coding Dictionary aus `external_repos/mattpocock/dictionary-of-ai-coding/` mit Sektionsordnern nach `00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/`.
