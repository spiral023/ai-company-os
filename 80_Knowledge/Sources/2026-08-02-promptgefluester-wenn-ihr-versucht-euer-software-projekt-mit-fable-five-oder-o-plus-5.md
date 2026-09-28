---
url: https://www.tiktok.com/@promptgefluester/video/7669564638576594208
autor: "@promptgefluester"
datum: 2026-08-02
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-08-02-promptgefluester-wenn-ihr-versucht-euer-software-projekt-mit-fable-five-oder-o-plus-5.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Vor dem KI-Refactoring: statische Analyse als deterministischer Prüfer

Der Creator warnt, ein KI-generiertes Altprojekt per einfachem „refactor“-Prompt umzubauen, zerstöre es. Erst statische Code-Analyse laufen lassen, toten Code entfernen und Regeln festlegen. Erfahrungsbericht ohne Zahlen; die „10 Prozent“ toter Code sind eine Beispielnennung.

## Kernaussagen
- Deterministische Tools (statische Analyse) finden kaputte Referenzen, unvollständige Queries, ungenutzte Variablen, statt dass die KI selbst abgleicht → [[Testharness-als-staerkster-Hebel]]
- Erst aufräumen, dann kann das Modell Abhängigkeiten sauber erkennen
- Architekturprinzipien (z. B. MVC) vorher als Plan festlegen

## Einordnung
Solide, nicht neu: deterministische Prüfer vor generativer Änderung. Fehlt: Tool-Namen und Belege.

## Verbindungen
- [[Testharness-als-staerkster-Hebel]]
- [[Freiheitsgrad-nach-Aufgaben-Fragilitaet]]
- [[2026-08-21-promptgefluester-wie-macht-man-refactering-bei-einer-richtig-grossen-code-base-mit-aeh]]
