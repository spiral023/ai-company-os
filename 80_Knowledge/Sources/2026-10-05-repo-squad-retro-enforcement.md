---
url: https://github.com/bradygaster/squad/tree/dev/templates/skills/retro-enforcement
autor: bradygaster
datum: 2026-10-05
erfasst: 2026-10-05
typ: repo
thema: Arbeitsweisen
zeitkritisch: nein
---

# Squad `retro-enforcement`: Retro erzwingen, Aktionspunkte nur als GitHub Issues

Im Klon von bradygaster/squad (Branch `dev`, Stand Commit `d2364dfe`) liegt die Skill-Vorlage `templates/skills/retro-enforcement/SKILL.md`. Gelesen, nichts ausgeführt.

## Kernaussagen
- Der Koordinator prüft zu Beginn jeder Runde, ob in `.squad/log/` innerhalb von sieben Tagen ein Retro-Log liegt. Fehlt es, blockiert er andere Arbeit, bis eine Retro gelaufen ist.
- Jeder Aktionspunkt muss als GitHub Issue angelegt werden. Eine Prüffunktion lehnt Retro-Logs mit offenen Markdown-Checkboxen ab.
- Begründung mit Projektdaten aus einem einzelnen Repo (tamirdresher/tamresearch1): sechs Retros mit Markdown-Checklisten zwischen 05.12.2025 und 21.02.2026 erledigten 0 von 23 Aktionspunkten; nach der Umstellung auf Issues am 24.03.2026 waren es 4 von 4.
- Als Ursache nennt der Skill, dass Markdown-Checklisten keinen Verantwortlichen, keine Benachrichtigung, kein Schließ-Ereignis und keine Abfrage haben.

## Einordnung
Selbstberichtete Zahlen aus einem Projekt, keine kontrollierte Messung. Die Aussage passt aber zur BMAD-Retro, die ebenfalls die Umsetzung der vorigen Aktionspunkte nachhält: Eine Retro ist nur so gut wie die Nachverfolgung ihrer Ergebnisse.

## Verbindungen
- [[Blockierende-Task-Abhaengigkeiten]]
- [[Task-basierte-Steuerung]]
