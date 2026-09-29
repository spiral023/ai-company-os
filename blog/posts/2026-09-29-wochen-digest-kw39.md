---
titel: "KW 39: Opus 5.5 führt, GPT-6 halbiert die Preise, Effort kauft Verifikation"
datum: 2026-09-29
kategorie: digest
zusammenfassung: "Wochenrückblick KW 39: Opus 5.5 an der Spitze beider Indizes, GPT-6 Sol und Luna deutlich günstiger, dazu Effort-Daten, ein Opus-Leitfaden und drei Arbeitsweisen gegen den Review-Engpass."
status: entwurf
quellen:
  - 2026-09-22-artificialanlys-2102438210798514391
  - 2026-09-22-artificialanlys-2102462962758033624
  - 2026-09-23-artificialanlys-2102833926788288704
  - 2026-09-24-artificialanlys-2102932119995756613
  - 2026-09-22-claude-getting-the-most-out-of-opus-5-5-in-claude-and-c
  - 2026-09-25-trq212-2103576349499855160
  - 2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck
  - 2026-09-27-anthropic-academy-sdlc-playbook
---

## Kurz gesagt

- Claude Opus 5.5 führt Intelligence Index (58) und Coding Agent Index (66), kostet aber in Claude Code pro Task rund 21 Prozent mehr als Opus 5.
- GPT-6 Sol und Luna kosten pro Token nur noch die Hälfte der Vorgänger, Luna ist der günstigste Punkt auf der Kostenfront.
- Effort kauft Verifikationstiefe, keinen besseren Ansatz. Das ist die wichtigste Arbeitsregel der Woche.

## 1. Opus 5.5: Spitze bei Intelligenz und Coding

Artificial Analysis (unabhängiger Dritter) misst für Opus 5.5 (max, mit Fallback) 58 Punkte im Intelligence Index, vor Fable 5.1 und GPT-6 Astra mit je 53. Im Coding Agent Index in Claude Code sind es 66 Punkte (Opus 5: 60, Fable 5.1: 62). Beide Indizes sind getrennte Skalen, Werte lassen sich nicht mischen. Wenn du Coding-Agenten einsetzt, ist Opus 5.5 der Kandidat zum Testen; mehr dazu im [Beitrag zu Opus 5.5](post:opus-5-5-hoechster-score-teurer-pro-task).{q:1}

## 2. Opus 5.5 im Preis: Token billiger, Tasks teurer

Der Listenpreis sinkt auf 4/20 US-Dollar pro 1M Input/Output (Opus 5: 5/25), Cache Reads kosten 0,20 US-Dollar statt 0,50. Gleichzeitig verbraucht Opus 5.5 im Coding Agent Index rund 15,6 Mio. Token pro Task statt 11,4 Mio., die Kosten liegen bei 13,04 statt 10,79 US-Dollar. Preis pro Token und Kosten pro Aufgabe sind verschiedene Größen: Rechne mit deinen eigenen Läufen, nicht mit der Preisliste.{q:4}

## 3. GPT-6: halber Preis, gemischte Qualität

GPT-6 Sol kostet 2/10 US-Dollar (GPT-5.6 Sol: 4/20), Luna 0,10/0,50 (vorher 0,20/1,20), Stand 22.09.2026. Im Coding Agent Index legt Sol um zwei Punkte zu (57) bei etwa halben Kosten, Luna verliert zwei Punkte (41) bei etwa 60 Prozent niedrigeren Kosten. Bei GDPval-AA fällt Sol um rund 100 Elo, laut Quelle wegen schwächerer Präsentationsqualität.{q:2} Für Coding-Routine lohnt der Wechsel zu Sol wahrscheinlich, bei Büro- und Präsentationsaufgaben solltest du vorher testen.

## 4. Die Kostenfront verschiebt sich

Elf neue Punkte auf der Pareto-Front von Intelligence Index gegen Kosten pro Task: fünf von Luna, vier von Opus 5.5, je einer von MiMo-V2.6-Pro und Sol. Eckpunkte: Luna 37 Punkte für 0,068 US-Dollar, MiMo-V2.6-Pro 46 für 0,13, Sol 48 für 1,06, Opus 5.5 58 für 5,98. Dass mehrere Effort-Stufen eines Modells getrennte Punkte bilden, macht Effort zum Kostenhebel. Die Werte gelten für den Intelligence Index, nicht für echte Coding-Sitzungen.{q:3}

## 5. Effort kauft Verifikation, keinen besseren Ansatz

Thariq (Anthropic) wertet eigene Terminal-Bench-3.0-Läufe aus, also Herstellerangaben mit ungefähr aus dem Chart abgelesenen Werten. Bei Fable 5.1 sinken übersehene Randfälle von 59 auf 24, falsche Grundentscheidungen aber nur von 133 auf 107. Opus 5.5 auf High erreicht laut Chart etwa den Score von Fable 5.1 auf Max mit rund der halben Token-Menge. Sein Ablauf: Claude dich interviewen lassen, auf Low oder Medium bauen, Ergebnis lesen, auf High verifizieren lassen. Umschalten geht mit `/effort` mitten im Gespräch.{q:6}

## 6. Opus 5.5 führen: Zielzustand, Stopp-Regeln, Task-Datei

Der Herstellerleitfaden{q:5} (ohne Messwerte) rät, „done“ in einer Nachricht zu definieren, „think carefully“-Zeilen zu streichen und Stopp-Regeln in die `CLAUDE.md` zu schreiben: nur vor Destruktivem fragen. Am belastbarsten ist die Task-Liste in einer Datei, weil sie die Kontext-Zusammenfassung überlebt. Weniger Stopps erhöhen das Risiko, Permission Prompts bleiben deshalb an. Wie sich das mit einem Kontext-Aufräumplan verträgt, steht im [Beitrag zur Kontext-Hygiene](post:kontext-hygiene-entscheidungsbaum).

## 7. Review als Engpass

Matt Pocock (Praxisbericht, ohne Messdaten){q:7} setzt auf drei Bremsen: deterministische Checks, ein Review-Subagent mit eigener Standards-Datei, der Fixes committet, und Human Review nach Risiko. Grüne Tests können lügen, etwa tautologische oder wegmockende Tests. Anthropics SDLC-Playbook (Hersteller, keine Wirkungszahlen){q:8} ergänzt: Der schreibende Agent genehmigt nicht selbst, Pflichtregeln gehören in Hooks statt in Skills. Kosten sind zusätzliche Review-Token pro PR. Die beiden Positionen dazu stehen im [Duell: Adversarial Agent oder menschlicher Review](post:duell-adversarial-agent-oder-review).

## Was ich diese Woche nicht einordnen konnte

Zur Aussage, Effort zerstöre bei Fable 5.1 und Opus 5.5 den Prompt Cache nicht, gibt es nur die Behauptung der Quelle. Die Bugfund-Aussage im Opus-Leitfaden (niedrigster Effort schlägt Opus 5 bei hohem) stammt von einem einzelnen Tester. Die Terminal-Bench-Werte für Opus 5.5 weichen je nach Setup ab (59,6 Prozent im Intelligence Index, 63,1 Prozent im Coding Agent Index), die Ursache ist nur mit „anderes Harness“ beschrieben. Die Kennzahlen im SDLC-Playbook sind ungeprüfte Vorschläge. Zu GPT-6 lag mir nur die Auswertung von Artificial Analysis vor, keine Herstellerseite mit den Preisen.

## Fazit

Teste diese Woche Opus 5.5 auf High statt Max an einer echten Aufgabe und miss Kosten pro Task statt Preis pro Token.
