---
name: repo-import-review
description: Verwende diesen Skill, wenn ein externes GitHub-Repository, Skill-Pack, Template oder Tool geprüft werden soll, bevor es in das AI-Company-OS oder ein Projekt-Repo übernommen wird. Prüft Zweck, Lizenz, Risiken, Scripts, Vertrauensniveau und Integrationsform.
---

# Repo Import Review

## Ziel

Prüfe externe Repositories, bevor sie übernommen oder als Referenz genutzt werden.

## Prüffelder

- Zweck und Nutzen
- Lizenz
- Wartungszustand
- Umfang
- enthaltene Scripts
- externe Abhängigkeiten
- mögliche Secrets
- Prompt-Injection- oder Supply-Chain-Risiken
- Überschneidung mit bestehenden Skills
- empfohlene Integrationsform

## Integrationsformen

- Nicht übernehmen
- Nur als Referenz nutzen
- Einzelne Dateien kopieren
- Als Git Submodule einbinden
- Fork erstellen und anpassen

## Ausgabeformat

- Kurzfazit
- Nutzen
- Risiken
- Lizenzstatus
- Empfohlene Integrationsform
- Offene Fragen
- Philipp-Freigabe erforderlich: ja / nein
