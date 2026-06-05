# Erster Arbeitsauftrag für Coding Agents

## Zweck

Aus dem Mutter-Repo heraus einen klaren Startprompt für Claude Code oder Codex im Zielprojekt erstellen.

## Wann verwenden

Nach dem Kopieren eines Projekt-Kits oder wenn ein neues Projekt-Repo erstmals mit einem Coding Agent bearbeitet wird.

## Input

- Projektbeschreibung
- Projektart
- wichtigste Dokumente
- gewünschtes erstes Ziel
- bekannte Grenzen und Freigaben

## Ablauf

1. Relevante Projektdateien nennen.
2. Ziel und Nicht-Ziele beschreiben.
3. offene Fragen markieren.
4. erwartete Checks nennen.
5. Freigabegrenzen wiederholen.

## Output

```md
# Arbeitsauftrag für Coding Agent

## Kontext

[Projektbeschreibung]

## Ziel

[Was soll umgesetzt oder geprüft werden?]

## Relevante Dateien

- `AGENTS.md`
- `docs/PRD.md`
- `docs/DESIGN.md`
- `docs/BACKEND.md`
- `docs/QA.md`

## Aufgabe

1. Lies die relevanten Dateien.
2. Erstelle einen kurzen Plan.
3. Prüfe offene Fragen.
4. Implementiere oder verbessere nur den beschriebenen Bereich.
5. Führe Checks aus.
6. Fasse Änderungen zusammen.

## Nicht tun

- keine Secrets erzeugen
- keine Produktion deployen
- keine externen kostenpflichtigen APIs einbauen
- keine Architektur komplett neu schreiben ohne Freigabe
```

## Beispiel für SaaS-Webapp

Erstelle aus `PRD.md`, `DESIGN.md`, `BACKEND.md` und `QA.md` einen MVP-Umsetzungsplan für die erste nutzbare Webapp-Version.

## Beispiel für Shopify App

Prüfe Merchant Use Case, Shopify-Flows, Admin UX und Webhook-Anforderungen. Erstelle danach den kleinsten umsetzbaren MVP-Plan.

## Beispiel für Website-Redesign

Prüfe Briefing, SEO, Content und Technik. Erstelle danach eine priorisierte Seiten- und Umsetzungsplanung.

## Empfohlene Skills

- project-bootstrap
- produktentwicklung
- qa-engineer
