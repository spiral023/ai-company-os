---
url: https://x.com/mrexodia/status/2010157660885176767
autor: "Duncan Ogilvie (@mrexodia)"
datum: 2026-01-20
erfasst: 2026-07-13
typ: tweet
---

# Duncan Ogilvie (mrexodia) zu „Vibe Engineering“

## Inhalt

Umfassender Erfahrungsbericht nach Monaten reiner Arbeit mit AI Coding Agents. Kernpunkte:

- Agenten sind im Kern nur eine Schleife (Simon Willisons Definition: „Ein Agent führt Tools in einer Schleife aus, um ein Ziel zu erreichen“) — keine Magie, aber State-of-the-Art-Modelle sind nötig, Open-Source-Modelle noch spürbar dahinter.
- Das Context Window ist die knappste Ressource: Ideal unter 50-75% Kapazität bleiben, darüber steigen Halluzinationen und Fehler. Mentalmodell nach Geoffrey Huntley: wie ein Commodore 64 mit 200-500 KB — bei vollem Kontext kommt „Compaction“, was Qualität degradiert.
- **„The Great Decoupling“** (Begriff von Gemini übernommen): Programming (physisches Code-Tippen) entkoppelt sich von Engineering (Architektur, Ziele, das Warum). LLMs werden im Tippen für praktisch jede Sprache/Domain besser als der Mensch; was bleibt, ist die Frage „Wie passen Komponenten zusammen, welchen Mehrwert bietet das?“
- „Du wurdest gerade befördert“: neuer Titel Tech Lead + QA Lead. Aufgabe: klare Spezifikationen/Pläne/Beispiele schreiben, „done“ definieren, **Ergebnisse statt Zeilen** reviewen. Das Modell ist „ein genialer Praktikant mit Amnesie“ — 100x Geschwindigkeit, aber kein Langzeitgedächtnis, braucht strikte Leitplanken ("Model CI").
- „Trust the Harness, not your Eyes“: Mikromanagement (Variablennamen korrigieren, jede Zeile reviewen) ist Kämpfen gegen das Modell und kontraproduktiv. Stattdessen einen besseren Harness bauen — bei Testfehlern: revert, besseren Test schreiben, erneut versuchen lassen; bei Stil: Linter-Regel statt manueller Korrektur. Bei falschem Ansatz: Plan war schlecht, Code löschen, zurück zur Planung.
- Projekt-Setup als wichtigste menschliche Zeitinvestition: Hard Requirement, dass das Projekt mit einem einzigen Befehl baut/testet/lintet; minimale, actionable Fehlermeldungen (nicht „Test bestanden“ ×1000, sondern die fehlgeschlagene Assertion + Call Stack).
- TDD ist für Agenten (anders als laut Autor für Menschen) kein Scam, sondern Goldstandard, weil es eine Feedback-Schleife per Design ist (fehlschlagenden Test schreiben → Feature implementieren → Test besteht).
- „Golden Master Testing“ für Portierungen/große Refactorings: bestehendes System mit Debug-Prints instrumentieren, Output als „Golden Master“ einfangen, nach dem Port müssen die Prints byte-für-byte übereinstimmen.
- „DevDocs“ gegen Context-Reset-Verlust: Unterordner mit `plan.md` (Ziele, Phasen, Ansatz) und `progress.md` (Status, Checkboxen) — „Dein Plan ist permanent, Code ist vergänglich.“
- CLI wird der IDE vorgezogen: IDEs ermutigen zu Mikromanagement (Diff-Anzeige verleitet zu Zeile-für-Zeile-Review), CLI ist eine „Forcing Function“, da Modelle auf Unix-Shells trainiert sind (Windows-Nutzern wird WSL/Devcontainer empfohlen).
- Sub-Agents als nächster Schritt gegen Context Rot: Hauptmodell spawnt einen Sub-Agent für den eigentlichen Fix, der nur zurückmeldet.

## Kernaussagen

- „The Great Decoupling“: Programming (Tippen) und Engineering (Architektur/Ziele) trennen sich; die Rolle wird zu Tech Lead + QA Lead, der Ergebnisse statt Code-Zeilen reviewt → [[Great-Decoupling-Rollenverstaendnis]]
- „Trust the Harness, not your Eyes“: Mikromanagement des Modells (Variablennamen, Zeile-für-Zeile-Review) ist kontraproduktiv — stattdessen bessere Tests/Linter-Regeln als Feedback-Schleife bauen → [[Great-Decoupling-Rollenverstaendnis]]
- Projekt-Setup mit Single-Command-Build und actionable, minimalen Fehlermeldungen ist die wichtigste menschliche Zeitinvestition, bevor überhaupt agentisch gearbeitet wird → [[Great-Decoupling-Rollenverstaendnis]]
- TDD ist für Agenten der Goldstandard, weil es Verifikation strukturell erzwingt, nicht optional macht → [[TDD-als-Verifikationshebel]]
- Context Window als knappste Ressource: unter 50-75% Kapazität bleiben, „Commodore-64“-Mentalmodell statt naiv auf großes Fenster zu vertrauen → [[Kontext-Hygiene-Entscheidungsbaum]]
