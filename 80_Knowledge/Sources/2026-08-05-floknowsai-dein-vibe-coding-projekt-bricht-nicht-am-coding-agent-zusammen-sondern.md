---
url: https://www.tiktok.com/@floknowsai/video/7670597972576537888
autor: "@floknowsai"
datum: 2026-08-05
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-08-05-floknowsai-dein-vibe-coding-projekt-bricht-nicht-am-coding-agent-zusammen-sondern.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Vibe-Coding scheitert am fehlenden Fundament, nicht am Agenten

Kurzes Erfahrungsvideo: Ein Wochenende reicht für Prototyp oder MVP, nicht aber für Login mit Passwort-Reset, Zahlungsanbindung und DSGVO-konforme Datenhaltung. Für ein System mit echten Kundendaten rechnet der Autor mit mindestens drei Monaten, auch mit Agent. Die Behauptung „99 % scheitern“ ist unbelegt.

Das Fundament (Technologie, Datenfluss, Schnittstellenformate, Verhalten bei jedem Fehlerfall, etwa fehlgeschlagene Abo-Zahlung) muss vor der ersten Codezeile feststehen. Stabilisieren lässt es sich auf zwei Wegen: Rules für Architektur und Qualität, die aber in langen Sessions im Kontext untergehen können, und statische Code-Analyse per Script.

## Einordnung
Erfahrungsbericht, keine Messung. Belastbar ist der Hinweis, dass Rules kein Durchsetzungsmechanismus sind; das deckt sich mit dem Bestand.

## Kernaussagen
- Rules können in langen Sessions untergehen, deterministische Prüfung ist nötig → [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]
- Architektur und Fehlerfälle vor dem Code festlegen → [[Spec-Grilling]]

## Verbindungen
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[2026-08-14-floknowsai-ueber-achtzig-prozent-des-codes-von-claude-code-und-codex-sieht-kein]]
