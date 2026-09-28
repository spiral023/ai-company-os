---
url: https://dev.to/wasp/claude-code-for-fullstack-development-the-3-things-you-actually-need-1p6p
autor: vincanger
datum: 2026-02-13
erfasst: 2026-08-04
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-13-vincanger-claude-code-fullstack-essentials.md
thema: Arbeitsweisen
zeitkritisch: nein
beleg_art: sekundaerquelle
---

# Fullstack mit Claude Code: Sichtbarkeit, aktuelle Docs und ein meinungsstarker Stack statt Feature-Sammlung

Der Beitrag argumentiert, dass für Fullstack-Arbeit mit Claude Code drei Grundlagen reichen und Subagents, Skills und MCP-Server für Einsteiger meist verzichtbar sind. Es ist ein Erfahrungsbericht mit Meinungscharakter, keine Messung. Der Autor gehört zum Team hinter dem Wasp-Framework und bewirbt am Ende das eigene Plugin. Vorliegend ist eine deutsche Aufarbeitung aus vibedeck (Sekundärquelle), die Primärquelle ist der dev.to-Artikel; Zahlen wurden nicht am Original geprüft.

## Erste Säule: Claude sieht das Ergebnis seines Codes

Der langsame Standardablauf lautet Prompten, warten, Code prüfen, im Browser testen und Fehlermeldungen von Hand zurückkopieren. Der Beitrag will diese Schleife schließen.

- Dev-Server als Background Task: `npm run dev` läuft im Hintergrund, Claude liest den Output und reagiert auf Fehler, ohne dass die Konversation blockiert. Auslösung per Prompt oder mit `Ctrl + B` während eines Bash-Befehls.
- Browser-Sicht per Chrome DevTools MCP (`claude mcp add chrome-devtools --scope project npx chrome-devtools-mcp@latest`, Stand der Quelle). Damit lädt Claude Seiten, klickt, liest Logs und macht Screenshots, sodass Runtime- und UI-Fehler sichtbar werden.

## Zweite Säule: Docs, die ins Context Window passen

Trainingsdaten veralten, das Modell schreibt Code für frühere Versionen. Die meiste Dokumentation ist für Menschen gebaut. Der Beitrag zitiert Karpathy sinngemäß: Docs sollten 2025 eine `.md`-Datei sein, die direkt ins Context Window geht. Als Lösung nennt er `llms.txt`, eine kuratierte, LLM-freundliche Fassung unter `/llms.txt`. Behauptet werden rund zehnmal weniger Token als bei MCP-Doc-Servern (ohne Messmethode). Gegenposten laut Quelle: Der Agent braucht mehr Führung im Umgang mit den Rohdaten.

## Dritte Säule: Stack mit vielen Vorgaben

Je mehr Entscheidungen ein Framework vorgibt, desto weniger muss die KI raten und desto weniger Code muss sie erzeugen und du prüfen. Als Beispiel nennt der Beitrag Auth in Wasp mit etwa 15 Zeilen Konfiguration statt über 500 Zeilen Handcode (angeblich 97 % weniger). Genannte Kandidaten: Wasp, Next.js, Laravel, Ruby on Rails.

## Feature-Askese

Als Beleg dient ein Zitat von Chris McCord (Phoenix): eine durchgehende Konversation pro Projekt, nie Subagent oder MCP genutzt, trotzdem gute Ergebnisse. Subagents und eigene Skills lohnen sich laut Beitrag erst bei repetitiven Aufgaben mit konstanten Kriterien, etwa Test-Runner, automatisches Review nach jeder Änderung oder Skripte für Bildkonvertierung und Deployment.

## Einordnung

Belastbar ist die Grundidee, dass ein Agent Ergebnisse selbst beobachten muss, damit die Korrekturschleife ohne Mensch läuft; das deckt sich mit dem Verifikationsgedanken im Bestand. Die Stack-Empfehlung ist plausibel, aber durch den Wasp-Bezug interessengeleitet, und die Zahlen (97 %, zehnfach weniger Token) sind unbelegte Selbstauskunft. Ein Widerspruch entsteht nur scheinbar: Die Feature-Askese gilt für Einsteiger; wo Kontext-Hygiene oder Parallelisierung nötig werden, greifen Subagents und Skills weiterhin. Kosten des Ansatzes: Der Browser-MCP verbraucht Kontext durch Snapshots und Screenshots, und `llms.txt` setzt voraus, dass die Bibliothek es anbietet.

## Kernaussagen

- Ein Agent, der Dev-Server-Output und Browser-Zustand selbst liest, korrigiert autonom und ohne Copy-and-paste-Schleife → [[Testharness-als-staerkster-Hebel]]
- Ein meinungsstarkes Framework mit klaren Ablageorten reduziert Raten und Codemenge → [[Trainingsdaten-Dichte-als-Stack-Kriterium]]
- Mit Basisfunktionen anfangen, Subagents und Skills erst bei wiederkehrenden Aufgaben mit festen Kriterien ergänzen → [[Klein-und-komposierbar]]

## Verbindungen

- [[Testharness-als-staerkster-Hebel]]
- [[Trainingsdaten-Dichte-als-Stack-Kriterium]]
- [[Klein-und-komposierbar]]
- [[2026-02-01-anthropic-docs-connect-claude-code-to-mcp]]
- [[2026-02-27-meer-claude-code-best-practices]]
