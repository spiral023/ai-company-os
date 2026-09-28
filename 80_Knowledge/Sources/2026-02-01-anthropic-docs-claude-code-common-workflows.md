---
url: https://code.claude.com/docs/en/common-workflows
autor: Anthropic Docs
datum: 2026-02-01
erfasst: 2026-08-04
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-claude-code-common-workflows.md
beleg_art: sekundaerquelle
---

# Claude Code Common Workflows: Offizielles Rezeptbuch mit wenigen neuen Konkretisierungen

Anthropics „Common Workflows“-Dokumentation listet praktische Rezepte für den Alltag mit Claude Code: Codebase-Exploration, Debugging, Refactoring, Subagents, Plan Mode, Tests, PRs, Dokumentation, Bilder, `@`-Referenzen, Extended Thinking, Sessions, Git Worktrees und Claude als Unix-Utility. Die Quelle ist rein präskriptiv — sie beschreibt empfohlene Nutzung, liefert aber keine Messwerte, Vergleiche oder Fallzahlen. Der Wert liegt fast ausschließlich in wenigen konkreten Mechanik-Details, nicht in neuen Prinzipien: Der Großteil der Abschnitte wiederholt in knapperer, aufzählungsartiger Form, was die thematisch fast identische Schwesterquelle [[2026-02-01-anthropic-docs-claude-code-best-practices]] (selbes Datum, selber Autor, selbe Docs-Familie) bereits ausführlicher und mit Fehlermuster-Systematik belegt hat.

## Was tatsächlich neu konkretisiert

Vier Abschnitte enthalten Mechanik, die in der Best-Practices-Schwesterquelle so nicht stand:

**Git Worktrees als Isolationsmechanismus für Parallelität.** Die Best-Practices-Quelle erwähnte „parallele Sessions für Writer/Reviewer-Aufteilungen“ nur als Prinzip. Hier steht der konkrete Mechanismus: `git worktree add ../project-feature-a -b feature-a`, eigene Claude-Instanz je Worktree, `git worktree remove` nach Abschluss. Das ist Dateisystem-Isolation auf Betriebssystemebene, nicht nur eine zweite Terminal-Session im selben Checkout — ein relevanter Unterschied, weil parallele Sessions im selben Arbeitsverzeichnis sich beim Dateizugriff in die Quere kommen können.

**`@`-Referenzen als expliziter Kontext-Injektionsmechanismus.** `@datei`, `@verzeichnis/**` und `@mcp:resource` binden Inhalte direkt ein, ohne dass Claude sie per eigenem Tool-Call erst suchen muss. Das ist eine konkrete Technik gegen unnötige Explorationsrunden, die die Best-Practices-Quelle nur abstrakt über `/clear`, `/compact` und Subagent-Auslagerung behandelt hatte.

**Claude als Unix-Filter mit strukturiertem Output.** Über die schon bekannte Headless-Nutzung (`claude -p`) hinaus nennt diese Quelle das Verketten via Pipe (`cat build-error.txt | claude -p '...' > output.txt`) und maschinenlesbare Ausgabeformate (`--output-format json` bzw. `stream-json`) für die Weiterverarbeitung in Skripten. Das macht aus der Headless-Nutzung erst eine wirklich komponierbare Unix-Utility statt eines reinen CLI-Aufrufs.

**Plan Mode headless.** `claude --permission-mode plan -p "Analyze authentication..."` kombiniert Plan Mode (rein lesende Analyse) mit Headless-Aufruf — ein risikoarmer, automatisierbarer Analyseschritt ohne Seiteneffekte, der so in der Schwesterquelle nicht explizit stand (dort nur `Ctrl+G` im interaktiven Editor).

## Was reine Feature-Beschreibung ohne Erkenntniswert ist

Codebase-Exploration („breite Fragen zuerst, dann spezifisch“), Debugging-Workflow (Fehler mitteilen, Fix-Empfehlung, anwenden), Refactoring-Workflow und Test-Workflow sind generische Prompt-Rezepte ohne neue Aussage — sie bestätigen nur, was in [[Testharness-als-staerkster-Hebel]] und [[Plan-first-mit-getrenntem-Review]] bereits mit mehr Substanz steht. Extended Thinking (`MAX_THINKING_TOKENS`, `Ctrl+O`, `Alt+T`/`Option+T`), Session-Verwaltung (`--continue`, `--resume`, `/rename`, Picker mit `P`/`B`) und Bild-Handling (Drag & Drop, Copy & Paste, Pfad) sind reine, versionsabhängige UI- und CLI-Konfiguration ohne begleitende Handlungsempfehlung, wann und warum man sie einsetzen sollte — dafür fehlt hier jede Tiefe. Die Selbstauskunft-Sektion („can Claude Code create pull requests?“) ist eine Trivialität ohne Arbeitsweisen-Bezug.

## Einordnung

Alle Aussagen dieser Quelle sind Herstellerempfehlungen zur intendierten Nutzung — **behauptet**, nicht **gemessen**: Es gibt keine Benchmark, keine Vorher-Nachher-Zahl, keinen Nutzerbericht. Als Sekundärquelle (vibedeck-Übernahme der Anthropic-Doku, keine Prüfung am Original) ist zusätzlich Vorsicht bei Detailgenauigkeit geboten — insbesondere bei Tastenkombinationen und Flag-Namen, die sich mit Versionswechseln ändern können. Der eigentliche Erkenntnisgewinn gegenüber dem Bestand ist gering: Der Bestand ist zu Claude Code bereits sehr dicht belegt (Plan Mode, Kontext-Hygiene, Subagent-Parallelisierung, Headless-Automatisierung), und diese Quelle bestätigt das im Wesentlichen nur redundant. Der Beitrag beschränkt sich auf vier Mechanik-Konkretisierungen (Worktree-Befehle, `@`-Syntax, Pipe/JSON-Output, Plan-Mode-Headless-Kombination), die bestehende Patterns um ein Stück CLI-Realität ergänzen, ohne deren Kernaussage zu verändern. Keine der vier Konkretisierungen widerspricht dem Bestand.

## Kernaussagen

- Git Worktrees sind der konkrete Dateisystem-Isolationsmechanismus für parallele Claude-Code-Sessions (`git worktree add ../pfad -b branch`, eigene Session pro Worktree) → [[Kontrollierte-Agent-Parallelisierung]]
- `@datei`, `@verzeichnis/**` und `@mcp:resource` injizieren Kontext explizit und ersparen Claude eigene Such-Tool-Calls → [[Kontext-Hygiene-Entscheidungsbaum]]
- Claude lässt sich als Unix-Filter verketten (`cat fehler.txt | claude -p "..." > out.txt`) und liefert mit `--output-format json`/`stream-json` maschinenlesbaren Output für Pipelines → [[Klein-und-komposierbar]]
- `claude --permission-mode plan -p "..."` kombiniert rein lesende Planungsanalyse mit Headless-Aufruf für risikoarme, automatisierbare Vorab-Analysen → [[Plan-first-mit-getrenntem-Review]]
- Screenshots/Mockups lassen sich per Drag & Drop, Copy & Paste oder Pfad als visueller Kontext für Fehlerdiagnose und Design-zu-Code-Generierung einbinden → [[Screenshot-als-Spezifikationsmedium]] (neu vorgeschlagen, Beleglage hier dünn)

## Verbindungen

- [[2026-02-01-anthropic-docs-claude-code-best-practices]]
- [[Kontrollierte-Agent-Parallelisierung]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Klein-und-komposierbar]]
- [[Plan-first-mit-getrenntem-Review]]
