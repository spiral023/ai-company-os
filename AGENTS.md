# AGENTS.md

## Zweck

Dieses Repository ist Philipps AI-Company-OS. Es dient als Mutter-Repo für Firmenwissen, Workflows, Skills, Projekt-Kits und wiederverwendbare Arbeitsweisen für KI-gestützte Softwareentwicklung und digitale Produkte.

Einzelne Softwareprojekte liegen in eigenen Repositories. Dieses Repo liefert dafür Vorlagen, Skills und Entscheidungswissen.

## Grundprinzipien

- Arbeite schlank, konkret und nachvollziehbar.
- Nutze nur die Informationen, die für die aktuelle Aufgabe relevant sind.
- Stelle konkrete Rückfragen, wenn wichtige Informationen fehlen.
- Erstelle keine unnötig komplexen Frameworks.
- Pflege Wissen in Markdown-Dateien, die auch in Obsidian gut funktionieren.
- Schreibe auf Deutsch mit korrekten Umlauten.
- Verwende englische Fachbegriffe dort, wo sie in Entwicklung, AI, SaaS oder Marketing üblich sind.

## Führende Dateien

- `AGENTS.md` ist die führende Datei für Agenten.
- `CLAUDE.md` verweist nur auf `AGENTS.md`.
- Projekt-Repos können eigene `AGENTS.md` Dateien erhalten.
- Bereichsspezifische Regeln gehören in Skills oder Workflows, nicht in diese Root-Datei.

## Arbeitsweise

1. Aufgabe verstehen.
2. Relevante Memory-, Workflow- oder Skill-Dateien prüfen.
3. Falls wichtige Informationen fehlen, den Skill `ask-user-question` verwenden.
4. Einen kurzen Plan erstellen.
5. Änderungen in kleinen, nachvollziehbaren Schritten durchführen.
6. Relevante Checks, Tests oder Reviews ausführen.
7. Ergebnis zusammenfassen:
   - Was wurde erstellt oder geändert?
   - Welche Dateien wurden geändert?
   - Welche Checks wurden ausgeführt?
   - Welche offenen Fragen oder Risiken bleiben?

## Freigabe durch Philipp erforderlich

Immer nach Freigabe fragen vor:

- Produktion-Deployments
- echten Kunden-E-Mails oder öffentlichen Veröffentlichungen
- Preisänderungen
- rechtlichen, steuerlichen oder datenschutzrelevanten Aussagen
- Änderungen an Authentifizierung, Billing, Security oder Tenant-Isolation
- Löschen von Daten
- neuen kostenpflichtigen Tools, APIs oder Diensten
- Aussagen über Zertifizierungen, Kunden, Compliance oder garantierte AI-Ergebnisse

## Autonom erlaubt

Ohne vorherige Freigabe erlaubt:

- Entwürfe erstellen
- lokale Dateien anlegen oder bearbeiten
- Projektideen strukturieren
- PRDs, Prompts, Checklisten und Testfälle erstellen
- Beispielcode und Prototypen vorbereiten
- lokale Reviews durchführen
- Verbesserungsvorschläge machen

## Skill-Nutzung

Skills liegen unter `30_Skills/`.

- Eigene Skills liegen unter `30_Skills/local/`.
- Externe Skill-Packs liegen unter `30_Skills/external/`.
- Die zentrale Übersicht ist `30_Skills/registry.yaml`.
- Nicht alle Skills sind automatisch aktiv.
- Externe Skills müssen geprüft werden, bevor sie in Projekt-Kits übernommen werden.

## Scripts

Wiederkehrende Aufgaben sollen bevorzugt über Scripts unter `70_Scripts/` gelöst werden, wenn sie mehr als zweimal vorkommen.

Vor Änderungen an Scripts:
- bestehende Nutzung prüfen
- einfache CLI beibehalten
- keine unnötigen Abhängigkeiten hinzufügen
- Syntax-Check ausführen

## Benutzerfreundliche Bedienung

Für normale Bedienung bevorzugt `python ai.py` im Repo-Root nutzen. Die Scripts unter `70_Scripts/` bleiben die darunterliegenden Werkzeuge für Automatisierung, Debugging und direkte Agent-Nutzung.

## Externe Skills

Externe Skills dürfen nicht automatisch als vertrauenswürdig gelten.

Vor Nutzung in Projekten:
1. Quelle prüfen
2. Lizenz prüfen
3. Inhalt sichten
4. Trust-Level in `30_Skills/registry.yaml` setzen
5. Philipp-Freigabe einholen, wenn der Skill produktiv genutzt werden soll

## Repo-Import

Externe Repositories, Templates und Skill-Packs müssen vor Integration mit dem Skill `repo-import-review` geprüft werden. Externe Scripts dürfen nicht automatisch ausgeführt werden.

## Projektarten in Phase 1

Dieses Repo unterstützt zuerst diese Projektarten:

- SaaS Webapp
- Shopify App
- Website-Redesign

## Obsidian-Kompatibilität

Nutze:

- Markdown-Dateien
- klare Ordnernamen
- kurze Index-Dateien
- Wiki-Links wie `[[Mission]]`, `[[Idee_zu_Produkt]]`
- keine proprietären Obsidian-Plugins als Voraussetzung

## Stil

- Direkt und praktisch schreiben.
- Keine unnötigen Floskeln.
- Keine langen theoretischen Erklärungen, wenn eine Checkliste reicht.
- Bei Entscheidungen Optionen mit Empfehlung liefern.
