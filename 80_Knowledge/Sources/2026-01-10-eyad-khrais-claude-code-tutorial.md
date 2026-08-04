---
url: https://x.com/eyad_khrais/status/2010076957938188661
autor: Eyad Khrais
datum: 2026-01-10
erfasst: 2026-08-04
typ: tweet
rohquelle: 00_Inbox/Quellen/2026-01-10-eyad-khrais-claude-code-tutorial.md
beleg_art: sekundaerquelle
---

# Claude Code Grundlagen: Denken vor Tippen, CLAUDE.md und Kontextgrenzen

Ein Praktiker-Playbook (Eyad Khrais, 7 Jahre Software Engineer bei Amazon, Disney, Capital One, heute CTO) für den Einstieg in Claude Code. Der Wert liegt nicht in neuen Techniken, sondern in der Verdichtung bekannter Grundregeln zu einem einprägsamen Anfänger-Leitfaden — mit einer eigenen, unbelegten Zahlenangabe zur Kontextdegradierung, die von der im Bestand dokumentierten Heuristik abweicht (siehe Einordnung).

## Erst denken, dann tippen

Der größte Anfängerfehler ist laut Autor, sofort loszutippen statt zu planen. Der Plan Mode (`Shift+Tab` zweimal) liefere „10 von 10 Mal“ signifikant bessere Ergebnisse als direktes Losschreiben. Der Unterschied zwischen einer schlechten Anweisung („Build me an auth system“) und einer guten („Build email/password authentication using the existing User model, store sessions in Redis with 24-hour expiry, and add middleware that protects all routes under /api/protected“) ist laut Autor der Unterschied zwischen Stunden Debugging und fünf Minuten zusätzlicher Planung.

## CLAUDE.md als Notizen an das eigene Amnesie-Ich

Die Datei wird vor jeder Konversation neu eingelesen, soll aber laut Autor kurz bleiben: Ein Frontier-Modell befolgt zuverlässig nur etwa 150-200 Anweisungen, wovon das System selbst schon rund 50 verbraucht. Projektspezifisches gehört hinein (ungewöhnliche Bash-Befehle, Testsetup), Standard-Konventionen der Sprache nicht. Wichtiger als die reine Regel ist laut Autor die Begründung: „Use TypeScript strict mode because we've had production bugs from implicit any types“ gibt dem Modell Entscheidungskontext, den die bloße Regel nicht liefert. Praktischer Pflegehinweis: Mit `#` während der Arbeit lässt sich eine Anweisung direkt in die Datei einfügen; wird eine Korrektur zweimal nötig, gehört sie dort hinein.

## Kontextgrenzen und Gegenmaßnahmen

Auch bei einem 200k-Token-Fenster degradiert die Qualität laut Autor schon ab etwa **20-40% Context-Usage**, lange vor 100%. Als Gegenmaßnahmen nennt er: eine Konversation pro Feature statt Themen zu vermischen, externen Speicher in Dateien (`SCRATCHPAD.md`, `plan.md`), die Sessions überdauern, sowie einen bewussten Copy-Paste-Reset (Wichtiges sichern, `/compact`, `/clear`, Wichtiges wieder einfügen) statt gegen einen entgleisten Kontext anzukämpfen. Sein Mentalmodell: Claude ist zustandslos, jede Konversation startet bei null außer dem, was explizit mitgegeben wird.

## Modellwahl: Opus zum Planen, Sonnet zum Ausführen

Schlechte Ergebnisse mit einem starken Modell führt der Autor primär auf schlechten Input zurück, nicht auf Modellgrenzen — Fix ist ein spezifischerer Prompt, keine Modellumschaltung. Für die Modellwahl selbst empfiehlt er eine feste Arbeitsteilung: Opus für komplexes Reasoning und Architektur-Planung, Sonnet für die anschließende, günstigere Ausführung nach Plan.

## Vom Chat zum System

Profis nutzen Claude Code laut Autor nicht nur interaktiv, sondern im Headless Mode (`-p`-Flag) scriptbar, in andere Tools gepiped und in automatisierte Workflows (Auto-PR-Reviews, Support-Tickets) integriert — ein Flywheel aus Fehler → Log-Prüfung → CLAUDE.md/Tooling-Verbesserung → besseres Ergebnis.

## Einordnung

Der Text ist ein einzelner, unabhängig unbelegter Erfahrungsbericht (sekundäre deutsche Aufarbeitung eines X-Threads) — „10 von 10 Mal“ und die 20-40%-Marke sind subjektive Einschätzungen des Autors, keine Messung. Auffällig: Die hier genannte Degradierungsschwelle (20-40% eines 200k-Fensters, also grob 40.000-80.000 Tokens) liegt deutlich niedriger als die im Bestand dokumentierte Heuristik von 300.000-400.000 Tokens in [[Kontext-Hygiene-Entscheidungsbaum]] — auch wenn Letztere sich eher auf sehr große (1M-Token-)Fenster bezieht und beide Zahlen aus unabhängigen, ebenfalls unbelegten Sekundärquellen stammen, ist die Diskrepanz in der Größenordnung nicht glattzuziehen und sollte als eigene Spannungszeile im Pattern festgehalten werden. Die Opus-für-Planung/Sonnet-für-Ausführung-Regel deckt sich exakt mit einer bereits im Bestand als Ergänzung notierten Rollenteilung im Multi-Agent-Fall.

## Kernaussagen

- Plan Mode vor Implementierung liefert laut Autor „10 von 10 Mal“ bessere Ergebnisse als direktes Losschreiben → [[Plan-first-mit-getrenntem-Review]]
- CLAUDE.md soll kurz und projektspezifisch bleiben, das „Warum“ statt nur die Regel nennen und laufend per `#`-Shortcut aktualisiert werden, sobald eine Korrektur zweimal nötig war → [[AGENTS-md-Onboarding-Design]]
- Modellqualität degradiert laut Autor bereits ab ca. 20-40% Context-Usage eines 200k-Fensters, lange vor 100% — externer Speicher (`SCRATCHPAD.md`) und bewusster Copy-Paste-Reset als Gegenmaßnahme → [[Kontext-Hygiene-Entscheidungsbaum]] (Spannung: abweichende Größenordnung zur bestehenden Heuristik, siehe Einordnung)
- Feste Rollenteilung Opus (Planung/Architektur) und Sonnet (Ausführung nach Plan) als Kostenoptimierung → [[Modell-Eskalation-von-guenstig-nach-teuer]]
- Headless Mode (`-p`) macht Claude Code scriptbar und pipebar; professionelle Nutzung baut Systeme statt Einzel-Interaktionen

## Verbindungen

- [[Plan-first-mit-getrenntem-Review]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[AGENTS-md-Onboarding-Design]]
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
