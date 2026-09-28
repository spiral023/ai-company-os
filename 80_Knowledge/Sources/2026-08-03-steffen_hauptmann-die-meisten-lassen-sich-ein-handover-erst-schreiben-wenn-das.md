---
url: https://www.tiktok.com/@steffen_hauptmann/video/7669828414232136982
autor: "@steffen_hauptmann"
datum: 2026-08-03
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-08-03-steffen_hauptmann-die-meisten-lassen-sich-ein-handover-erst-schreiben-wenn-das.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Laufendes STATE.md statt Handover erst bei vollem Context Window

Ein Solo-Entwickler lässt Claude den aktuellen Zustand fortlaufend in eine `STATE.md` schreiben (Fortschritt, offene Punkte, Learnings, aus denen später Regeln werden), statt erst bei vollem Context Window ein Handover-Prompt zu erzeugen. Selbstberichtete Praxis, keine Messung.

## Kernaussagen
- Die Zustandsdatei wird in jeder Session automatisch aktuell gehalten; der Handover existiert, bevor man ihn braucht. → [[Handoff-Doc]]
- Neue Session: `/clear`, Datei per Drag and Drop einbinden, weiterarbeiten. → [[Kontext-Hygiene-Entscheidungsbaum]]
- Learnings in der Datei dienen als Rohmaterial für spätere Regeln.

## Einordnung
Nur für Einzelarbeit gedacht; der Autor würde die Datei im Team nicht einchecken (Merge-Konflikte, veraltete Zustände). Kosten: Claude verbraucht laufend Tokens fürs Nachpflegen, und die Datei kann bei falschem Zustand irreführen.

## Verbindungen
- [[Handoff-Doc]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
