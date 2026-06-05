# AI-Company-OS

Dieses Repository ist das schlanke Mutter-Repo für Philipps KI-Agent-Firma. Es enthält Firmenregeln, Workflows, lokale Skills, Projekt-Kits, Evals und wiederverwendbares Wissen für neue Softwareprojekte.

Einzelne Produkte liegen später in eigenen GitHub-Repositories. Aus diesem Repo werden passende Vorlagen, Skills und Arbeitsweisen in diese Projekt-Repos kopiert.

## Phase-1-Umfang

- Firmenwissen und Arbeitsprinzipien
- wiederverwendbare Workflows
- lokale Markdown-Skills nach dem `SKILL.md`-Prinzip
- Projekt-Kits für die ersten Projektarten
- einfache Eval-Dateien
- kleine Hilfsscripts

## Projektarten

- SaaS Webapp
- Shopify App
- Website-Redesign

## Ordner

- `00_Inbox/`: Ideen, Rohnotizen und Fragen.
- `10_Company/`: Mission, Prinzipien, Freigaben und Glossar.
- `20_Workflows/`: wiederholbare Arbeitsabläufe.
- `30_Skills/`: lokale Skills und Registry für externe Skills.
- `40_Project_Kits/`: Startvorlagen für neue Projekt-Repos.
- `50_Memory/`: Produkte, Entscheidungen, Märkte, Kunden und Lessons Learned.
- `60_Evals/`: Qualitätskriterien für Skills, Produktarbeit und QA.
- `70_Scripts/`: kleine lokale Hilfsscripts.
- `90_Archive/`: Ablage für veraltete Inhalte.

Externe Skills werden über `30_Skills/registry.yaml` verwaltet und vor produktiver Nutzung geprüft.

## Beispielablauf

1. Idee in `00_Inbox/Ideen.md` notieren.
2. Workflow `20_Workflows/Idee_zu_Produkt.md` nutzen.
3. passenden Projekt-Kit auswählen.
4. Skills ins Projekt-Repo kopieren.
5. Projekt mit Claude Code oder Codex weiterentwickeln.

Falls ein `npx skills` Tool verfügbar ist, kann es später zur Verwaltung externer Skill-Packs dokumentiert und getestet werden. In Phase 1 ist es keine Voraussetzung.

## Schnellstart

```bash
python 70_Scripts/skill_registry_check.py
python 70_Scripts/skill_autoreview.py
python 70_Scripts/company_os_healthcheck.py
python 70_Scripts/create_project_kit.py --list
python 70_Scripts/create_project_kit.py --kit saas-webapp --name mein-produkt --target ../mein-produkt --copy-skills
```

## Health Check

Der zentrale Repo-Check läuft über:

```bash
python 70_Scripts/company_os_healthcheck.py
```

## Ideen verarbeiten

Neue Ideen zuerst in `00_Inbox/Ideen.md` sammeln. Danach mit `20_Workflows/Idee_zu_Produkt.md` schärfen und bei Bedarf in `50_Memory/Produkte/` oder ein neues Projekt-Repo überführen.

## Projekt-Repos erstellen

Projekt-Kits werden mit `70_Scripts/create_project_kit.py` kopiert. Beispiel:

```bash
python 70_Scripts/create_project_kit.py --kit shopify-app --name shopify-review-tool --target ../shopify-review-tool --copy-skills
```

Danach wird das Zielprojekt separat als eigenes Git-Repository initialisiert und mit Claude Code oder Codex weiterentwickelt.

## Skills kopieren

Skills werden über `30_Skills/registry.yaml` gesteuert. Defaults pro Projektart kopierst du so:

```bash
python 70_Scripts/install_project_skills.py --project-type website-redesign --target ../mein-redesign
```

Einzelne Skills:

```bash
python 70_Scripts/install_project_skills.py --skills produktentwicklung qa-engineer --target ../mein-projekt
```

## Externe Skills prüfen

Externe Quellen werden dokumentiert, aber nicht automatisch vertraut:

```bash
python 70_Scripts/external_skill_review.py
python 70_Scripts/external_skill_intake.py --id example --name "Example" --source https://github.com/example/repo
```

Vor produktiver Nutzung sind Quelle, Lizenz, Inhalt und Trust-Level zu prüfen.

## Externe Skills

Externe Skill-Packs liegen konzeptionell unter `30_Skills/external/`:

- `sources/`: Submodule, Fork-Kopien oder manuelle Kopien
- `reviews/`: Review-Berichte pro Quelle
- `intake/`: Entwürfe und noch ungeprüfte Quellen

Sichere Nutzung:

1. Quelle mit `external_skill_intake.py` erfassen.
2. Lizenz und Inhalt prüfen.
3. Review-Datei ausfüllen.
4. `external_skill_review.py` ausführen.
5. Trust-Level erst nach Philipp-Freigabe erhöhen.

Externe Skills werden nicht automatisch in Projekt-Kits kopiert.

## Obsidian

Das Repo ist als Obsidian Vault nutzbar: Markdown-Dateien, kurze Index-Dateien und Wiki-Links wie `[[Projekt_Bootstrap]]` funktionieren ohne proprietäre Plugins.

Lokale Obsidian-Workspace-Dateien wie `.obsidian/workspace.json` und `.obsidian/graph.json` sollten normalerweise nicht versioniert werden. Wenn sie bereits tracked sind, nicht automatisch entfernen.

## Bewusst nicht automatisiert

- externe Skills werden nicht automatisch aktiviert
- echte Deployments brauchen Freigabe
- Secrets werden nicht erzeugt
- neue kostenpflichtige Dienste werden nicht automatisch eingerichtet
