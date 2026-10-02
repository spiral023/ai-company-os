---
url: https://www.tiktok.com/@promptgefluester/video/7688428923016826145
autor: "@promptgefluester"
datum: 2026-09-22
erfasst: 2026-10-02
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-09-22-promptgefluester-ich-arbeite-mit-multiorgastation-und-das-hat-was-mit-meinem-tokenlimit.md
thema: KI-Kosten
zeitkritisch: nein
---

# Token sparen in Claude Code: Orchestrierung, Kontext, Planung, Effort

Ein Creator nennt aus Praxiserfahrung Hebel gegen aufgebrauchte Token-Limits. Alles ist Erfahrungsbericht ohne Messung, das Transkript ist automatisch erzeugt und stark verhört; die Empfehlung eines eigenen Tools (vermutlich Code Guardian) ist Eigenwerbung.

## Kernaussagen
- Orchestrator auf dem stärksten Modell, Umsetzung auf dem zweitbesten → [[Modell-Eskalation-von-guenstig-nach-teuer]]
- Nach erledigter Aufgabe `/clear` (oder `/compact`), statt etwa 80 % Kontext bei jeder Eingabe mitzuschleppen → [[Kontext-Hygiene-Entscheidungsbaum]]
- Erst planen, den Plan zusätzlich mit Sonnet reviewen lassen; Planfehler seien später teurer → [[Plan-first-mit-getrenntem-Review]]
- Statische Codeanalyse statt LLM-Fehlersuche, Debug-Logging aktiv, exakte Fehlermeldung und betroffene Datei direkt mitgeben; „kurz und prägnant“ in CLAUDE.md, mit Risiko des Informationsverlusts.
- Effort: `low` reiche oft, `xhigh` zum Programmieren, `max` nur für den Orchestrator.

## Einordnung
Die Hebel sind plausibel, aber unbelegt. Die Effort-Empfehlung (`xhigh` zum Programmieren) steht in Spannung zu den Leitfäden derselben Woche, die eher `medium`/`high` raten.

## Verbindungen
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[2026-09-28-claude-building-with-claude-sonnet-5-5-claude-dev-blog]]
