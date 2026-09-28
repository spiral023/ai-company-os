---
url: https://www.youtube.com/watch?v=YE40EDb1kRk
autor: Alex Sprogis
datum: 2026-09-09
erfasst: 2026-09-14
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-09-09-alex-sprogis-so-erstellst-du-interaktive-architektur-diagramm.md
thema: Tools & Releases
zeitkritisch: nein
---

# Archify: Diagramme aus der Codebase statt von Hand

Das Video zeigt den Open-Source-Skill Archify, der aus Beschreibung oder Codebase interaktive HTML-Diagramme erzeugt. Es ist eine Demo mit Sponsoring und eigener Kursewerbung, ohne Vergleich oder Messung.

## Kernaussagen
- Ergebnis pro Diagramm: eine HTML-Datei plus JSON-Quelle unter `docs/diagrams`; der Agent prüft sich per Screenshot, bis die Darstellung stimmt. → [[Screenshot-als-Spezifikationsmedium]]
- Typen: Architektur, Datenfluss, Sequenz, Workflow, Lifecycle, auch Geschäftsprozesse.
- Sein Entwicklungs-Workflow: Spec, Architektur, Tasks, Build, unabhängige QA gegen die Spec. → [[Plan-first-mit-getrenntem-Review]]

## Einordnung
Nützlich gegen veraltete Handdiagramme, doch die Korrektheit der abgeleiteten Beziehungen wird nicht geprüft.

## Verbindungen
- [[Plan-first-mit-getrenntem-Review]]
- [[Spec-Ordner-pro-Feature]]
