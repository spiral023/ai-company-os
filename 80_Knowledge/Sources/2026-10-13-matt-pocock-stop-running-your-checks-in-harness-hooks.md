---
url: https://www.youtube.com/watch?v=zgy8_ApYNDk
autor: Matt Pocock
datum: 2026-10-13
erfasst: 2026-10-22
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-10-13-matt-pocock-stop-running-your-checks-in-harness-hooks.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Prüffeedback an abgeschlossenen Arbeitseinheiten bündeln

Matt Pocock empfiehlt am 13. Oktober 2026, Prüfungen zeitlich zu staffeln. Er kritisiert umfangreiche Checks nach jeder Dateiänderung, weil Refactorings zwischenzeitlich absichtlich inkonsistent sein können. Die Empfehlung beruht auf Praxiserfahrung, nicht auf einem kontrollierten Geschwindigkeitsvergleich.

## Kernaussagen

- Checks nach jedem Speichern können wiederholt bekannte Zwischenfehler melden, Arbeit unterbrechen und viele Feedback-Tokens erzeugen. Das ist keine generelle Ablehnung automatisierter Prüfungen oder sämtlicher Harness-Hooks. → [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]
- Kurze Pre-Commit-Checks bündeln Rückmeldungen vor dem Eintragen in die Historie; umfangreiche Prüfungen laufen in CI vor dem Merge. Weniger als drei Sekunden für Pre-Commit ist seine Zielheuristik, kein allgemeines Limit. → [[Pruefungen-nach-Feedbackzeitpunkt-staffeln]]

## Einordnung

Zeitpunkt und Implementierung einer Prüfung sind unterschiedliche Entscheidungen. Als eigene Bewertung bleibt offen, welche schnellen Prüfungen pro Änderung trotzdem nützlich sind und wie ein umgangener Commit-Hook abgesichert wird. Die deutsche Untertitelspur ist automatisch erzeugt und möglicherweise übersetzt; keine vollständige Hör- oder Bildprüfung.

## Verbindungen

- [[CI-Agent-mit-Review-Gate]]
- [[Helper-Nutzung-durch-Lint-erzwingen]]
