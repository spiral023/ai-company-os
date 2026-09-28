---
url: https://x.com/elenakvcs/status/2008228601980985550
autor: elenakvcs
datum: 2026-01-15
erfasst: 2026-08-04
typ: tweet
rohquelle: 00_Inbox/Quellen/X/2026-01-15-unbekannt-vibe-coding-beginner-guide.md
beleg_art: sekundaerquelle
---

# Vibe Coding als Kommunikationsfähigkeit: Ein Anfänger-Erfahrungsbericht

Elena Kovacs, laut eigener Aussage KI-Forscherin ohne Engineering-Hintergrund, beschreibt ihre ersten sechs Monate mit Claude Code als Werkzeug für Alltagsautomatisierung. Der Bericht liegt nur als vibedeck-Aufarbeitung eines X-Threads vor, nicht als Primärquelle — entsprechend sind alle folgenden Zahlen und Einschätzungen ihre eigenen, unabhängig unbelegten Angaben, nicht extern geprüfte Messwerte.

## Klarheit statt Programmierkenntnis

Ihre zentrale These: Der eigentliche Lernschritt beim Vibe Coding sei nicht Syntax, sondern **Präzision in der Beschreibung des gewünschten Ergebnisses**. Ein vager Auftrag wie „Bau mir ein E-Mail-Tool“ erzeuge laut ihrer Erfahrung „Garbage“; ein präziser Auftrag dagegen führe direkt zum Ziel — ihr Beispiel: „Schreibe ein Python-Skript, das eine CSV-Datei einliest, jede Zeile mittels Regex auf ein gültiges E-Mail-Format prüft, Duplikate entfernt, eine neue CSV mit den sauberen Daten ausgibt und eine Zusammenfassung druckt (verarbeitete Zeilen, ungültige Zeilen, Duplikate).“ Konkreter Beleg aus ihrem Alltag: Eine Datenbereinigung an 4.000 Tabellenzeilen, die sie auf 6 Stunden Handarbeit schätzte, war laut ihrer Angabe nach 45 Sekunden als lauffähiges Python-Skript erledigt.

## Kleinschrittiges Vorgehen nach einem gescheiterten Erstversuch

Ihr erster Versuch, einen Twitter-Bookmark-Analyzer in einem Prompt („Bau mir einen Twitter Bookmark Analyzer“) zu erzeugen, scheiterte laut ihrer Darstellung an einem für sie zu komplexen System mit APIs und Abhängigkeiten, die sie nicht einordnen konnte. Eine Woche später zerlegte sie dieselbe Aufgabe in vier einzeln geprüfte Schritte (API-Verbindung und Abruf der letzten 100 Bookmarks, Textextraktion, Kategorisierung nach Keywords, Speicherung als JSON) und hatte das Ergebnis nach eigener Angabe in einer Stunde statt nach vier gescheiterten Stunden. Ihre Schlussfolgerung: Nicht das Modell war das Problem, sondern der Umfang des einzelnen Arbeitspakets.

## Modellwahl als Nebenaussage

Sie berichtet, nach Tests mit ChatGPT, Cursor, Copilot und Gemini bei Claude geblieben zu sein — nicht wegen besserer Codequalität, sondern weil Claude in ihrer Erfahrung öfter präzisierend nachfragt statt bei Unklarheit einfach eine Annahme zu treffen und loszulegen. Das habe ihr wiederholt Debugging-Zeit gespart. Diese Einschätzung ist ein Einzelvergleich einer Anfängerin ohne kontrollierte Bedingungen, keine Benchmark-Aussage.

## Einordnung

Der Bericht ist ein einzelner, sekundär aufbereiteter Erfahrungsbericht ohne Messmethodik: „10 von 10“-artige Formulierungen fehlen hier zwar, aber alle Zeitangaben (45 Sekunden, 6 Stunden, eine Woche, eine Stunde) sind Elenas eigene, nicht nachprüfbare Schätzungen aus einem einzigen Anwendungsfall. Die beiden tragenden Aussagen — Präzision statt Syntax als Kernfähigkeit, und kleine geprüfte Schritte statt große Sprünge — sind im Bestand bereits über mehrere unabhängige, teils verifizierte Quellen belegt (siehe [[Spec-Grilling]] und [[TDD-als-Verifikationshebel]]); dieser Bericht liefert dazu keine neue Mechanik, sondern eine zusätzliche, unabhängige Bestätigung aus einer bislang unterrepräsentierten Perspektive: einer Nutzerin ganz ohne Engineering-Hintergrund. Die Aussage zu Claudes Rückfrageverhalten gegenüber ChatGPT ist plausibel und deckt sich mit der in [[Spec-Grilling]] beschriebenen Dynamik, bleibt aber ein unkontrollierter Einzelvergleich ohne Modellversion oder Prompt-Wortlaut. Die vier Bilder der Rohquelle (Kaffee-Tastatur-Illustration, ein Flugzeug-Foto, ein VS-Code-Screenshot zu einem BullMQ/Redis-Bug, ein Claude-Code-Login-Bildschirm) enthalten keine der im Text beschriebenen Inhalte (kein Chart, keine Prompt-Beispiele, kein sichtbarer Rückfrage-Dialog) und wurden deshalb nicht übernommen — reine Dekoration bzw. thematisch nicht zuordenbar, siehe Bildregeln in `artikel-format.md`.

## Kernaussagen

- Die übertragbare Fähigkeit beim Vibe Coding ist Präzision in der Auftragsbeschreibung, nicht Programmierkenntnis; vage Prompts erzeugen unbrauchbare Ergebnisse → [[Spec-Grilling]]
- Claude fragt nach eigener Erfahrung häufiger klärend nach statt bei Unklarheit direkt loszulegen, was Debugging-Zeit spart (Einzelvergleich ohne Kontrollbedingungen) → [[Spec-Grilling]]
- Ein gescheiterter Ein-Prompt-Versuch wurde durch Zerlegung in vier einzeln geprüfte Schritte (API-Abruf, Extraktion, Kategorisierung, Speicherung) zum Erfolg — der Scope des Arbeitspakets, nicht das Modell, war der Fehlerfaktor → [[TDD-als-Verifikationshebel]]

## Verbindungen

- [[Spec-Grilling]]
- [[TDD-als-Verifikationshebel]]
- [[2026-01-20-mrexodia-vibe-engineering]]
