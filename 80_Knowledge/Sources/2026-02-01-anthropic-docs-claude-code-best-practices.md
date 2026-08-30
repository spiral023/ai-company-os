---
url: https://code.claude.com/docs/en/best-practices
autor: Anthropic Docs
datum: 2026-02-01
erfasst: 2026-08-04
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-claude-code-best-practices.md
beleg_art: sekundaerquelle
---

# Claude Code Best Practices: Kontextfenster, Verifikation und CLAUDE.md-Disziplin

Anthropics eigene Best-Practices-Dokumentation für Claude Code, hier in sekundärer deutscher Aufarbeitung. Der Wert liegt weniger in Neuheit als in Autorität: Anthropic bestätigt als Hersteller nahezu jedes bereits im Bestand vorhandene Pattern zu Kontext, Planung und Verifikation aus erster Hand, statt sie nur von Drittautoren übernommen zu sehen.

## Das Kontextfenster als knappste Ressource

Die meisten Best Practices beruhen auf einer einzigen Einschränkung: Das Kontextfenster füllt sich schnell — es enthält die gesamte Konversation, alle gelesenen Dateien und Befehlsausgaben — und die Performance sinkt, wenn es voll ist. Ein voller Kontext führt dazu, dass Claude Anweisungen „vergisst“ oder mehr Fehler macht.

## Verifikation als effektivster Hebel

Claude arbeitet laut Anthropic drastisch besser, wenn es seinen eigenen Erfolg validieren kann. Drei Beispiele aus der Dokumentation zeigen den Unterschied zwischen vager und verifizierbarer Anweisung: Statt „implementiere eine Funktion zur E-Mail-Validierung“ konkrete Testfälle benennen und nach der Implementierung ausführen lassen; statt „mache das Dashboard schöner“ einen Screenshot beilegen und einen Soll-Ist-Vergleich mit Differenzliste einfordern; statt „der Build schlägt fehl“ den konkreten Fehler einfügen und die Ursache statt des Symptoms beheben lassen.

## Erst erkunden, dann planen, dann coden

Der empfohlene Standardablauf: Explore (Dateien lesen, Kontext verstehen, z. B. „verstehe, wie wir Sessions handhaben“), Plan (detaillierten Implementierungsplan anfordern, im Plan Mode über `Ctrl+G` im Editor verfeinerbar), Implement (im Normal Mode gegen den Plan umsetzen) und Commit (aussagekräftige Commit-Nachricht, PR).

## CLAUDE.md gezielt einsetzen

CLAUDE.md wird bei jeder Session geladen und soll Konventionen enthalten, die Claude nicht allein aus dem Code ableiten kann — spezielle Bash-Befehle, Coding-Styles, Test-Setups. Ausgeschlossen bleibt, was Claude selbst lesen kann, Standard-Sprachkonventionen und lange Tutorials. Wird die Datei zu lang, gehen Regeln im Rauschen unter — Pruning ist die empfohlene Gegenmaßnahme.

## Session-Management und häufige Fehlermuster

Anthropic benennt vier wiederkehrende Fehlermuster mit jeweiligem Fix: die **Kitchen-Sink-Session** (mehrere unzusammenhängende Aufgaben in einer Session häufen Kontextmüll an → `/clear` zwischen Aufgaben), **endlose Korrekturen** (derselbe Fehler wiederholt sich → `/clear` und besserer Initial-Prompt), die **überladene CLAUDE.md** (wichtige Regeln gehen unter → radikal kürzen) und **Infinite Exploration** (Claude liest hunderte Dateien ohne Ziel → Scope eng fassen oder Subagents für die Recherche nutzen). Ergänzend empfiehlt die Dokumentation frühes Eingreifen (`Esc`, `/rewind`), aggressives Context-Management (`/clear` zwischen Aufgaben, gezieltes `/compact <Fokus>`) und Subagents explizit für Recherche, damit die Exploration nicht den Hauptkontext flutet.

## Automatisieren und Skalieren

Headless Mode (`claude -p "prompt"`) für CI-Pipelines und Skripte, parallele Sessions für Writer/Reviewer-Aufteilungen und Fan-out über viele Dateien per Schleife (`for file in $(cat files.txt); do claude -p "..." ...; done`) sind die drei genannten Skalierungsmuster.

## Einordnung

Die inhaltliche Übereinstimmung mit dem bereits im Bestand vorhandenen Patternset ist groß, weil viele dieser Patterns ursprünglich selbst aus Anthropic-nahen oder von Anthropic-Doku inspirierten Quellen synthetisiert wurden — diese Quelle bestätigt sie nun aus erster Hand statt aus abgeleiteten Wiki-Artikeln. Alle vier Fehlermuster (Kitchen Sink, endlose Korrekturen, überladene CLAUDE.md, Infinite Exploration) sind bereits einzeln in [[Kontext-Hygiene-Entscheidungsbaum]] und [[AGENTS-md-Onboarding-Design]] abgedeckt; neu ist hier nur ihre kompakte, offizielle Benennung als vier Fehlermuster in einer Liste.

**Wichtiger Befund zur Dublettenvermeidung:** In `00_Inbox/Quellen/` liegt zusätzlich die noch unverarbeitete Notiz `2026-08-04-anthropic-best-practices-for-claude-code-claude-code-docs.md` (Frontmatter-URL: `https://www.anthropic.com/engineering/claude-code-best-practices`, Status: `neu`). Sie erfasst offenkundig dasselbe Anthropic-Dokument über eine andere URL (Engineering-Blog-Post statt aktueller Docs-Seite) und primärnäher (automatisch per Ingest-Skript erfasst, nicht über vibedeck), mit zusätzlichen Abschnitten, die diese sekundäre Fassung nicht enthält (Stop-Hook mit 8-Block-Override, `/goal`, `/btw`, Agent Teams, Worktrees, Claude Code auf dem Web, adversarialer Review-Subagent). Zum Zeitpunkt dieses Laufs existiert noch keine Source-Notiz für diese URL — dieser Lauf legt keine Dublette an, aber wer die andere Inbox-Notiz später verarbeitet (vermutlich Batch „skills-3-und-basis“), sollte sie mit dieser Source-Notiz verschmelzen statt eine zweite eigenständige Notiz für dasselbe Dokument anzulegen.

## Kernaussagen

- Das Kontextfenster ist die knappste Ressource; ein voller Kontext lässt Claude Anweisungen „vergessen“ und mehr Fehler machen → [[Kontext-Hygiene-Entscheidungsbaum]]
- Verifikationsmöglichkeiten (Tests, Screenshots, konkrete Fehlermeldungen) sind laut Anthropic der effektivste Hebel für gute Ergebnisse → [[Testharness-als-staerkster-Hebel]]
- Explore → Plan (Plan Mode) → Implement → Commit als Standardablauf für nicht-triviale Änderungen → [[Plan-first-mit-getrenntem-Review]]
- CLAUDE.md soll nur enthalten, was Claude nicht selbst ableiten kann, und radikal gekürzt werden, sobald Regeln im Rauschen untergehen → [[AGENTS-md-Onboarding-Design]]
- Vier benannte Fehlermuster (Kitchen Sink, endlose Korrekturen, überladene CLAUDE.md, Infinite Exploration) mit je einem Fix (`/clear`, besserer Prompt, Kürzen, Scope/Subagents) → [[Kontext-Hygiene-Entscheidungsbaum]]
- Subagents explizit für Recherche nutzen, damit Exploration den Hauptkontext nicht flutet → [[Kontrollierte-Agent-Parallelisierung]]

## Verbindungen

- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Testharness-als-staerkster-Hebel]]
- [[Plan-first-mit-getrenntem-Review]]
- [[AGENTS-md-Onboarding-Design]]
