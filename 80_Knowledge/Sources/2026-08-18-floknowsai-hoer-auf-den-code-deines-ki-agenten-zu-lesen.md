---
url: https://www.tiktok.com/@floknowsai/video/7675431688024984865
autor: "@floknowsai"
datum: 2026-08-18
erfasst: 2026-08-29
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-08-18-floknowsai-hoer-auf-den-code-deines-ki-agenten-zu-lesen.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Mutation Testing und ein zweiter Agent statt Code-Review

Florian Schünemann gibt in einem kurzen Video wieder, warum Robert C. Martin den Code seiner Agenten nicht mehr liest: Er verlässt sich auf Unit-Tests, Qualitätsmetriken und Mutation Testing. Die Zahl „über die Hälfte der Fehler wird nicht gefunden“ steht nur im Video und ist ohne Beleg. Die Methode ist plausibel, die Zahl selbstberichtet.

## Kernaussagen
- Schreibt derselbe Agent Code und Tests, beweist ein grüner Test nur, dass niemand widersprochen hat. Mutation Testing setzt absichtlich Fehler in den Code und prüft, ob Tests anspringen → [[Testharness-als-staerkster-Hebel]]
- Ein zweiter Agent mit frischem Kontext prüft Implementierung, Codequalität und Testqualität ohne Befangenheit → [[Plan-first-mit-getrenntem-Review]]

## Einordnung
Der Kern ist Trennung von Autor und Prüfer, ergänzt um einen deterministischen Check auf die Tests selbst. Kosten: Mutation Testing verlängert Läufe deutlich, und ein zweiter Agent verdoppelt Tokenverbrauch.

## Verbindungen
- [[2026-08-19-matt-pocock-live-uncle-bob-on-software-fundamentals-in-the-a]]
- [[2026-08-14-floknowsai-ueber-achtzig-prozent-des-codes-von-claude-code-und-codex-sieht-kein]]
- [[TDD-als-Verifikationshebel]]
