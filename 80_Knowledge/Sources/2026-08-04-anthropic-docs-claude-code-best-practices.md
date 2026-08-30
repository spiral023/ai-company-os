---
url: https://www.anthropic.com/engineering/claude-code-best-practices
autor: "Anthropic (Claude Code Docs)"
datum: 2026-08-04
erfasst: 2026-08-05
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-08-04-anthropic-best-practices-for-claude-code-claude-code-docs.md
---

# Anthropics aktuelle Best-Practices-Seite: Verifikation als vierstufige Eskalation

Anthropic pflegt unter `/engineering/claude-code-best-practices` die offizielle, laufend aktualisierte Best-Practices-Seite für Claude Code. Der Stand vom 2026-08-04 ist gegenüber einer älteren, bereits im Bestand liegenden Fassung (datiert 2026-02-01, separat in der Inbox als Sekundärquelle) an mehreren Stellen erkennbar weiterentwickelt: Es kommen konkrete Mechanismen hinzu, die im Februar-Stand noch fehlten (`/goal`-Bedingungen, Stop-Hooks mit Override-Zähler, Auto-Mode-Klassifikator, `/btw`, Agent Teams, Fan-out-Schleifen). Als Primärquelle direkt von Anthropic ist dieser Stand maßgeblich; ältere Sekundärfassungen sollten als zeitgebunden markiert werden, sobald sie verarbeitet werden.

## Verifikation als vierstufige Eskalation, nicht nur „Tests mitliefern“

Die Seite beschreibt vier Ebenen, wie Claude die eigene Arbeit prüfen kann, mit steigender struktureller Robustheit:

1. **Im selben Prompt**: Prüfbefehl und Iteration in einer Nachricht anfordern.
2. **Über die Session**: Ein `/goal`-Zustand wird von einem separaten Evaluator nach jedem Zug erneut geprüft; Claude arbeitet weiter, bis die Bedingung hält.
3. **Als deterministisches Gate**: Ein Stop-Hook führt die Prüfung als Skript aus und blockiert das Sessionende, bis sie besteht — mit einem konkreten Sicherheitsventil: Claude Code überschreibt den Hook und beendet den Zug nach acht aufeinanderfolgenden Blockierungen.
4. **Durch eine zweite Meinung**: Ein Verifikations-Subagent oder ein dynamischer Workflow mit einem frischen Modell versucht aktiv, den eigenen Befund zu widerlegen — die Arbeit wird nicht von derselben Instanz benotet, die sie erledigt hat.

Diese vier Stufen konkretisieren [[Testharness-als-staerkster-Hebel]] deutlich über den bisherigen Beleg (Anthropics C-Compiler-Bericht mit Oracle-Ansatz) hinaus: Dort ging es um Testqualität für autonome Agenten allgemein, hier liefert Anthropic den strukturellen Baukasten (Prompt → Goal → Hook → zweite Meinung) für den Verifikationsschritt selbst. Neu und bislang nicht im Bestand: der explizite Override-Mechanismus nach acht Blockierungen als eingebautes Sicherheitsventil gegen Endlosschleifen, sowie das Prinzip, dass die zweite Meinung aus einem *anderen* Modell/Kontext kommen sollte als der Ersteller der Lösung.

## Explore, Plan, Implement, Commit als vierteiliger Standardfluss

Die Doku gibt den Ablauf mit konkreten Beispielprompts vor: zuerst lesend erkunden („read /src/auth and understand how we handle sessions“), dann einen Plan einfordern („What files need to change? Create a plan.“), erst danach implementieren (inklusive Tests für den neuen Pfad) und abschließend committen und einen PR öffnen. Ergänzt wird ein konkretes Beispiel für den adversarialen Review-Schritt: ein Subagent prüft den Diff gegen `PLAN.md`, kontrolliert, ob alle gelisteten Edge-Cases Tests haben und ob nichts außerhalb des Scopes geändert wurde — mit der expliziten Anweisung „Report gaps, not style preferences“. Das bestätigt und konkretisiert [[Plan-first-mit-getrenntem-Review]] um einen direkt einsetzbaren Prompt-Baustein für die Review-Stufe.

## CLAUDE.md: Ort bestimmt Reichweite

Die Doku unterscheidet fünf Ablageorte mit unterschiedlicher Reichweite: `~/.claude/CLAUDE.md` (alle Sessions), Projekt-Root `./CLAUDE.md` (eingecheckt, Team), `./CLAUDE.local.md` (persönlich, gitignored), Parent-Verzeichnisse (Monorepos laden Root- und Unterordner-Dateien automatisch) und Child-Verzeichnisse (werden erst bei Bedarf nachgeladen, wenn Claude eine Datei dort liest — Progressive Disclosure in der Praxis). Das ergänzt [[AGENTS-md-Onboarding-Design]] um die konkrete Lademechanik hinter dem dort bereits belegten Progressive-Disclosure-Prinzip.

## Rechtekonfiguration: Auto Mode als dritter Mechanismus neben Allowlist und Sandbox

Neu gegenüber dem Februar-Stand ist **Auto Mode**: ein separates Klassifikator-Modell prüft jeden Befehl und blockiert nur, was riskant wirkt (Scope-Eskalation, unbekannte Infrastruktur, durch feindlichen Inhalt ausgelöste Aktionen) — geeignet, wenn man der Grundrichtung einer Aufgabe vertraut, aber nicht jeden Schritt bestätigen will. Das ist ein anderer Mechanismus als die statische Deny-Liste aus [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]: Dort wird der Zugriff vor dem Modell technisch fest verdrahtet blockiert, hier entscheidet ein Modell dynamisch pro Befehl. Beide sind komplementär, nicht austauschbar — eine dynamische Klassifikation ersetzt keine harte Deny-Regel für Secrets, weil ein Klassifikator-Fehlurteil möglich bleibt, während eine Deny-Regel technisch nicht umgangen werden kann.

## Session-Hygiene: neue Werkzeuge seit Februar

Zu den bereits bekannten Mitteln (`/clear`, `/compact <Fokus>`, Esc zum Stoppen, `/rewind`) kommen zwei differenziertere Werkzeuge hinzu: `/rewind` erlaubt jetzt gezieltes „Summarize from/up to this message“ statt nur Zurückspringen, und `/btw` beantwortet Zwischenfragen in einem verwerfbaren Overlay, ohne dass die Antwort in den Conversation-Verlauf eingeht und weiter Kontext bindet. Compaction lässt sich zudem über eine CLAUDE.md-Anweisung customizen („bewahre immer die vollständige Liste geänderter Dateien“). Diese Details erweitern [[Kontext-Hygiene-Entscheidungsbaum]] um feinere Instrumente für dieselbe Grundentscheidung (Continue/rewind/compact/clear).

## Mehrere Sessions: Agent Teams bestätigen ein bereits vermutetes Muster

Neben Worktrees, Desktop-App und Cloud-Sessions führt die Doku „Agent Teams“ ein: automatisierte Koordination mehrerer Sessions mit geteilten Aufgaben, Messaging und einem Team-Lead. Das deckt sich exakt mit dem in [[Kontrollierte-Agent-Parallelisierung]] bereits beschriebenen mentalen Modell („ein Lead zerlegt die Arbeit, mehrere Teammates bearbeiten Teilaufgaben, Koordination über Struktur statt freie Konversation“) — hier nun als offiziell benanntes Anthropic-Feature, nicht nur als community-beobachtetes Muster. Ergänzt wird die Fan-out-Technik: eine Dateiliste generieren, per Skript iterieren, `claude -p "<prompt>" --allowedTools ...` je Datei aufrufen, zuerst an wenigen Dateien testen, dann skalieren.

## Einordnung

Die Seite ist die Primärquelle von Anthropic selbst und damit die verlässlichste verfügbare Referenz zu aktuellem Claude-Code-Verhalten — allerdings mit dem üblichen Vorbehalt für Doku-Inhalte: Flags, Slash-Commands und Zahlenwerte (wie das Acht-Blockierungen-Limit) sind Konfiguration zum Stand 2026-08-04 und keine zeitlose Erkenntnis; sie sollten bei künftiger Verarbeitung mit Versionsangabe zitiert werden. Inhaltlich deckt die Seite sich stark mit der bereits mehrfach belegten Praxis in [[Plan-first-mit-getrenntem-Review]], [[Kontext-Hygiene-Entscheidungsbaum]] und [[Kontrollierte-Agent-Parallelisierung]] — der Mehrwert dieser Quelle liegt weniger in neuen Grundideen als in der offiziellen Bestätigung und Präzisierung bestehender Annahmen (Agent Teams, Stop-Hook-Override, Auto-Mode-Klassifikator). Die „Common failure patterns“ am Seitenende (Kitchen-Sink-Session, wiederholtes Korrigieren, überladene CLAUDE.md, Trust-then-verify-Lücke, uferlose Exploration) sind wörtlich dieselben vier Fehlermodi, die bereits in der älteren Sekundärfassung vom 2026-02-01 stehen — unverändert seit mindestens Februar, was für deren Stabilität als Kernaussage spricht.

## Kernaussagen

- Vierstufige Verifikations-Eskalation (Prompt → `/goal`-Evaluator → Stop-Hook mit Acht-Blockierungen-Override → zweite Meinung durch frisches Modell) → [[Testharness-als-staerkster-Hebel]]
- Explore-Plan-Implement-Commit mit konkretem Adversarial-Review-Prompt („Report gaps, not style preferences“) → [[Plan-first-mit-getrenntem-Review]]
- CLAUDE.md-Reichweite hängt vom Ablageort ab (Home/Projekt/`.local.md`/Parent/Child), Child-Dateien laden erst bei Bedarf → [[AGENTS-md-Onboarding-Design]]
- Auto Mode (Klassifikator-Modell prüft Befehle dynamisch) ist ein zu statischen Deny-Regeln komplementärer, nicht ersetzender Mechanismus → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- „Agent Teams“ mit Team-Lead und geteilten Aufgaben ist nun ein offiziell benanntes Feature, das exakt dem bereits belegten Lead/Teammate-Modell entspricht → [[Kontrollierte-Agent-Parallelisierung]]
- Die vier „Common failure patterns“ sind gegenüber der Fassung von 2026-02-01 inhaltlich unverändert — stabile Kernaussage, keine Zeitgebundenheit erkennbar

## Verbindungen

- [[Testharness-als-staerkster-Hebel]]
- [[Plan-first-mit-getrenntem-Review]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Kontrollierte-Agent-Parallelisierung]]
- [[AGENTS-md-Onboarding-Design]]
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[2026-02-27-meer-claude-code-best-practices]]
