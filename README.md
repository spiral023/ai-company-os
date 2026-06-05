# AI-Company-OS

Schlankes Mutter-Repo für Philipps KI-Agent-Firma. Es bündelt Firmenregeln, Workflows, lokale Skills, Projekt-Kits, Evals und wiederverwendbares Wissen für KI-gestützte Softwareentwicklung und digitale Produkte.

Einzelne Softwareprojekte liegen später in eigenen GitHub-Repositories. Dieses Repo liefert dafür Vorlagen, Skills, Checklisten und Entscheidungswissen.

## Status

| Bereich | Stand |
|---|---|
| Agent-Regeln | `AGENTS.md` ist führend, `CLAUDE.md` verweist nur darauf |
| Projekt-Kits | SaaS Webapp, Shopify App, Website-Redesign |
| Skills | lokale Skills unter `30_Skills/local/`, Registry unter `30_Skills/registry.yaml` |
| Externe Skills | dokumentiert, aber nicht automatisch vertrauenswürdig |
| Health Check | `python 70_Scripts/company_os_healthcheck.py` |
| Obsidian | Markdown, Wiki-Links und kurze Index-Dateien |

## Was dieses Repo ist

- Firmen- und Arbeitswissen für KI-gestützte Produktentwicklung.
- Startpunkt für neue Projekt-Repos.
- Sammlung lokaler Markdown-Skills nach dem `SKILL.md`-Prinzip.
- Obsidian-kompatible Wissensbasis.
- Kontrollierter Prozess für externe Skill-Quellen.

## Was dieses Repo nicht ist

- kein Produkt-Code-Repo
- kein Ort für Secrets, Tokens, Passwörter oder Kundendaten
- kein automatischer Installer für externe Skills
- kein Deployment- oder Produktionssystem

## Schnellstart

```bash
python 70_Scripts/company_os_healthcheck.py
python 70_Scripts/create_project_kit.py --list
python 70_Scripts/install_project_skills.py --list
```

Neues SaaS-Projekt vorbereiten:

```bash
python 70_Scripts/create_project_kit.py --kit saas-webapp --name mein-produkt --target ../mein-produkt --copy-skills
```

Danach im Zielprojekt mit Claude Code oder Codex weiterarbeiten.

## Typischer Ablauf

1. Idee in `00_Inbox/Ideen.md` notieren.
2. Idee mit `20_Workflows/Idee_zu_Produkt.md` schärfen.
3. Projektart auswählen.
4. Projekt-Kit mit `create_project_kit.py` kopieren.
5. passende lokale Skills ins Projekt kopieren.
6. Zielprojekt separat als Git-Repository initialisieren.
7. ersten Arbeitsauftrag mit `20_Workflows/Erster_Arbeitsauftrag_für_Coding_Agents.md` formulieren.

## Projekt-Kits

| Kit | Zweck | Pfad |
|---|---|---|
| SaaS Webapp | B2B/SaaS-Produkte mit Auth, Rollen, QA, Security und Deployment | `40_Project_Kits/saas-webapp/` |
| Shopify App | Merchant Use Case, Admin UX, Shopify-Flows und Deployment | `40_Project_Kits/shopify-app/` |
| Website-Redesign | Briefing, SEO, Content, Design, Technik und QA | `40_Project_Kits/website-redesign/` |

Beispiel:

```bash
python 70_Scripts/create_project_kit.py --kit shopify-app --name shopify-review-tool --target ../shopify-review-tool --copy-skills
```

## Skills

Lokale Skills liegen unter `30_Skills/local/` und werden über `30_Skills/registry.yaml` gesteuert.

| Script | Aufgabe |
|---|---|
| `skill_registry_check.py` | prüft Registry, lokale Skill-Pfade und externe Quellen |
| `skill_autoreview.py` | prüft lokale Skills auf Länge, Frontmatter, Output und Risiken |
| `install_project_skills.py` | kopiert lokale Skills in Projekt-Repos |
| `external_skill_review.py` | prüft externe Skill-Quellen ohne Aktivierung |
| `external_skill_intake.py` | legt neue externe Skill-Quellen als Entwurf an |
| `company_os_healthcheck.py` | führt die zentralen Checks gesammelt aus |

Default-Skills für ein Projekt kopieren:

```bash
python 70_Scripts/install_project_skills.py --project-type website-redesign --target ../mein-redesign
```

Einzelne Skills kopieren:

```bash
python 70_Scripts/install_project_skills.py --skills produktentwicklung qa-engineer --target ../mein-projekt
```

## Externe Skills

Externe Skill-Packs werden dokumentiert, aber nicht automatisch vertraut.

| Ordner | Bedeutung |
|---|---|
| `30_Skills/external/sources/` | mögliche Submodule, Fork-Kopien oder manuelle Kopien |
| `30_Skills/external/reviews/` | Review-Berichte pro externer Quelle |
| `30_Skills/external/intake/` | Entwürfe und ungeprüfte Quellen |

Neue externe Quelle erfassen:

```bash
python 70_Scripts/external_skill_intake.py --id example --name "Example" --source https://github.com/example/repo
```

Externe Quellen prüfen:

```bash
python 70_Scripts/external_skill_review.py
python 70_Scripts/external_skill_review.py --source marketingskills
```

Vor produktiver Nutzung immer:

1. Quelle prüfen.
2. Lizenz prüfen.
3. Inhalt sichten.
4. Review-Datei ausfüllen.
5. Philipp-Freigabe einholen.

Externe Scripts werden nicht automatisch ausgeführt. Externe Skills werden nicht automatisch in Projekt-Kits kopiert.

## Workflows

| Workflow | Einsatz |
|---|---|
| `Idee_zu_Produkt.md` | aus rohen Ideen Produktkonzepte machen |
| `Projekt_Bootstrap.md` | neues Projekt-Repo vorbereiten |
| `Lovable_Prototyping.md` | Lovable-Prompts und Übergabe an Coding Agents |
| `Open_Source_zu_SaaS.md` | Open-Source-Ideen in SaaS-Chancen übersetzen |
| `Erster_Arbeitsauftrag_für_Coding_Agents.md` | Startprompt für Claude Code oder Codex erstellen |
| `Externe_Skills_Integrieren.md` | externe Skill-Quellen sicher aufnehmen |

Alle Workflows liegen unter `20_Workflows/`.

## Memory

`50_Memory/` enthält wiederverwendbares Wissen:

- `Produkte/`: Produktideen und Produktnotizen, z. B. `TeamBridge`
- `Entscheidungen/`: Entscheidungsdokumentation
- `Märkte/`: Märkte, Wettbewerber und Zielgruppen
- `Kunden/`: Kundensegmente und Bedarfsmuster
- `Lessons_Learned/`: wiederverwendbare Erkenntnisse

## Obsidian

Das Repo ist als Obsidian Vault nutzbar:

- Markdown-Dateien
- klare Ordnernamen
- kurze Index-Dateien
- Wiki-Links wie `[[Projekt_Bootstrap]]`
- keine proprietären Obsidian-Plugins als Voraussetzung

Lokale Obsidian-UI-Dateien werden nicht versioniert:

- `.obsidian/workspace.json`
- `.obsidian/workspace-mobile.json`
- `.obsidian/graph.json`

## Sicherheit und Freigaben

Nicht in dieses Repo schreiben:

- Secrets
- Tokens
- Passwörter
- private Kundendaten
- produktive API-Keys

Philipp muss freigeben vor:

- Produktion-Deployments
- echten Kunden-E-Mails oder öffentlichen Veröffentlichungen
- Preisänderungen
- rechtlichen, steuerlichen oder datenschutzrelevanten Aussagen
- Änderungen an Authentifizierung, Billing, Security oder Tenant-Isolation
- neuen kostenpflichtigen Tools, APIs oder Diensten

## Health Check

Vor größeren Änderungen oder vor Commits:

```bash
python 70_Scripts/company_os_healthcheck.py
```

Der Check umfasst:

- Registry Check
- Skill Autoreview
- External Skill Review
- Projekt-Kit-Liste
- Skill-Install-Liste
- Python Compile für Scripts

## Nächste sinnvolle Schritte

- Erste echte Projektidee über `00_Inbox/Ideen.md` und `20_Workflows/Idee_zu_Produkt.md` ausarbeiten.
- Für TeamBridge ein eigenes Projekt-Repo aus dem SaaS-Kit erzeugen.
- Externe Skill-Quellen nur nach Review und Freigabe weiter integrieren.
