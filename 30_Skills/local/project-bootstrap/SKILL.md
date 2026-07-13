---
name: project-bootstrap
description: Verwende diesen Skill, wenn aus dem Mutter-Repo ein neues Softwareprojekt vorbereitet werden soll. Unterstützt SaaS-Webapps, Shopify Apps und Website-Redesigns mit passenden Projekt-Kits, Dokumenten, Skills und Agent-Anweisungen.
---

# Project Bootstrap

## Ziel

Erstelle aus einem Projekt-Kit ein startbares Projekt-Setup.

## Unterstützte Projektarten

- SaaS Webapp
- Shopify App
- Website-Redesign

## Standardablauf

1. Projektart bestimmen.
2. Passendes Projekt-Kit aus `40_Project_Kits/` auswählen.
3. Relevante Skills aus `30_Skills/registry.yaml` identifizieren.
4. Projektname, Zielgruppe und Zweck eintragen.
5. Projekt-Dokumente vorbereiten (Inhalte ggf. über den Skill `produktentwicklung` erheben):
   - PRD oder Briefing
   - DESIGN
   - BACKEND oder TECHNIK
   - QA
   - DEPLOYMENT
6. Optional: PRD/Briefing zusätzlich als Master-Prompt bündeln, wenn die Umsetzung direkt an Claude Code oder Codex übergeben wird.
7. Hinweise für Claude Code und Codex ergänzen.

## Ausgabeformat

- Projektart
- Erstellte Dateien
- Empfohlene Skills
- Offene Fragen
- Nächster Schritt
