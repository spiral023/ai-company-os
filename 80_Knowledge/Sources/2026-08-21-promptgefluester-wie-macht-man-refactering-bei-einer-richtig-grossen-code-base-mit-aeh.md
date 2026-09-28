---
url: https://www.tiktok.com/@promptgefluester/video/7676584233586003232
autor: "@promptgefluester"
datum: 2026-08-21
erfasst: 2026-08-29
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-08-21-promptgefluester-wie-macht-man-refactering-bei-einer-richtig-grossen-code-base-mit-aeh.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Großes Refactoring stufenweise: Analyse, leicht vor schwer, Business-Logik-Doku

Vorgehen für Refactoring großer Codebases mit Claude Code, als Empfehlung ohne Messung. Nicht direkt loslegen, sondern in Stufen.

## Kernaussagen
- Zuerst einen Refactoring-Skill aus Best-Practice-Recherche erzeugen, mit mehreren Testszenarien und Analyseläufen prüfen → [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- Dann nur analysieren, Funde nach Kritikalität sortieren und von einfach (UTF-8, doppelte Funktionen) nach schwer abarbeiten → [[Modell-Eskalation-von-guenstig-nach-teuer]]
- Während der einfachen Fixes wird in Markdown die Business-Logik dokumentiert, die später als Kontext für schwere Umbauten dient

## Einordnung
Die Reihenfolge einfach vor schwer als Kontextaufbau ist ein brauchbarer Gedanke; Modell-Eskalation ist hier nur eine Analogie. Selbst erzeugte Business-Logik-Doku kann Fehler festschreiben und braucht menschliche Prüfung.

## Verbindungen
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- [[Task-basierte-Steuerung]]
- [[2026-08-02-promptgefluester-wenn-ihr-versucht-euer-software-projekt-mit-fable-five-oder-o-plus-5]]
