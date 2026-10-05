---
url: https://github.com/garrytan/gstack/tree/main/retro
autor: garrytan
datum: 2026-10-05
erfasst: 2026-10-05
typ: repo
thema: Arbeitsweisen
zeitkritisch: nein
---

# gstack `/retro`: wöchentliche Engineering-Retrospektive aus der Git-Historie

Im Klon von garrytan/gstack (Stand Commit `857466f`) liegt `retro/SKILL.md` (Skill-Version 2.0.0, rund 1.200 Zeilen, aus einer Vorlage generiert). Gelesen, nichts ausgeführt.

## Kernaussagen
- Auslöser sind „weekly retro“, „what did we ship“ oder „engineering retrospective“; der Skill soll sich am Ende einer Arbeitswoche oder eines Sprints selbst anbieten.
- Ausgewertet wird die Commit-Historie: Zeitverteilung der Commits, Arbeitssessions, Commit-Typen, Hotspots, PR-Größen (Small unter 100 Zeilen bis XL über 1.500), ein „Focus Score“ (Anteil der Änderungen im meistgeänderten Top-Level-Ordner) und das größte Commit als „Ship of the Week“.
- Teamfähig: pro Person zwei bis drei Sätze, ein bis zwei konkrete Lobpunkte und eine Wachstumschance. KI-Co-Autoren zählen als eigene Kennzahl „AI-assisted commits“, nicht als Teammitglied.
- Ab einem Zeitfenster von 14 Tagen Wochenvergleich; ein „Shortcut Debt Ledger“ sammelt bewusst gesetzte Abkürzungs-Marker im Code.
- Ergebnisse werden als JSON unter `.context/retros/` gespeichert und bei der nächsten Retro geladen, um Trends zu vergleichen.

## Einordnung
Diese Retro schaut auf Output und Arbeitsmuster eines Teams über Tage oder Wochen, nicht auf die Agent-Umgebung einer einzelnen Session. Sie setzt das gstack-Setup voraus (Preamble-Skript, Telemetrie-Schritt).

## Verbindungen
- [[Metrikband-gestufte-Agent-Autonomie]]
- [[2026-10-02-repo-garrytan-gstack]]
