---
url: https://www.youtube.com/watch?v=zcLPGC-tvgk
autor: Matt Pocock
datum: 2026-08-19
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-08-19-matt-pocock-live-uncle-bob-on-software-fundamentals-in-the-a.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Uncle Bob: Deterministische Checks statt Regeltexte für Agenten

Im Gespräch mit Matt Pocock beschreibt Robert C. Martin seine Arbeitsweise mit Coding Agents. Er lässt sie Code-Coverage mit Komplexität verrechnen (sein „CRAP“-Score) und Mutation Testing laufen, bis der Code sauber ist, und will den Code selbst kaum noch lesen. Alles Erfahrungsbericht, keine Messung.

## Kernaussagen
- Lange Regeldokumente (TDD, Clean Code) behandeln Modelle laut Martin wie Richtlinien; Mittelteile des Contexts gehen verloren („lost in the middle“). Deshalb Prompt minimal halten, danach deterministische Tools → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- Tools setzen den Agenten in eine Schleife: Code ändern, bis das Tool zufrieden ist. Grenze ist, dass der Agent nicht langsamer als ein Mensch werden darf → [[Testharness-als-staerkster-Hebel]]
- Unordentlicher Code bremst auch Agenten; sie drehen sich im Kreis, wenn Änderungen anderes brechen.

## Einordnung
Deckt sich mit dem Bestand (Checks vor Steering). Neu ist Mutation Testing und CRAP als Agent-Schleife. Kosten: Laufzeit der Checks, Pflege der Toolchain.

## Verbindungen
- [[2026-08-18-floknowsai-hoer-auf-den-code-deines-ki-agenten-zu-lesen]]
- [[2026-02-14-matt-pocock-skill-tdd-claude-code]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
