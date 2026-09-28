---
url: https://www.tiktok.com/@avasdr34m/video/7595680584995704086
autor: "@avasdr34m"
datum: 2026-01-15
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-01-15-avasdr34m-its-not-easy-but-it-is-simple-kontext-nutzung-in-claude-code-entscheidet.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Kontext klein halten: MCP-Overhead, Loop-Sessions, Phasentrennung

TikTok-Kurzvideo (automatisches Transkript, Selbstbehauptung ohne eigene Messung; gezeigt wird nur ein Graph zur Leistungsabnahme bei langem Context). Kernthese: Je länger der Context, desto schlechter die Modellleistung.

## Kernaussagen
- Zu viele MCP-Server belasten den Context dauerhaft; Tool-Beschreibungen (genannt: etwa 500 Token je Tool) liegen ständig am Anfang. → [[MCP-Code-Execution-statt-Tool-Definitionen]]
- Für Aufgabenlisten ein Bash-Skript mit Schleife und abgehakter Liste, jede Aufgabe in frischer Session. → [[Ralph-Loop-Frischer-Kontext-pro-Iteration]]
- Research und Implementierung in getrennten Contexts. → [[Kontext-Hygiene-Entscheidungsbaum]]

## Einordnung
Deckt sich mit dem Bestand; die 500-Token-Zahl ist eine grobe Faustregel. Die Grafik wurde nicht ausgewertet, die Quelle nennt keine Werte.

## Verbindungen
- [[Ralph-Loop-Frischer-Kontext-pro-Iteration]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[2026-05-01-mnilax-claude-code-overhead-9-patterns]]
