---
url: https://x.com/bcherny/status/2017742741636321619
autor: "Boris Cherny (@bcherny)"
datum: 2026-01-31
erfasst: 2026-08-04
typ: tweet
rohquelle: 00_Inbox/Quellen/X/2026-01-31-bcherny-claude-code-team-tips.md
beleg_art: sekundaerquelle
---

# Wie das Claude-Code-Team bei Anthropic tatsächlich arbeitet

Boris Cherny, der Schöpfer von Claude Code, hat zehn Praktiken geteilt, die nicht seine eigenen sind, sondern aus der täglichen Arbeit des gesamten Claude-Code-Teams bei Anthropic stammen. Der Rahmen, den er selbst mitliefert, ist wichtiger als jede Einzelpraxis: Das Team nutzt Claude Code anders als Boris selbst — es gibt nicht den einen richtigen Workflow, sondern mehrere, die nebeneinander funktionieren.

## Parallelisierung als größter Hebel

Der vom Team selbst als wichtigster benannte Tipp: 3-5 `git worktrees` gleichzeitig, jeder mit eigener Claude-Sitzung. Manche im Team binden Shell-Aliase (`za`, `zb`, `zc`) an einen Tastendruck, um zwischen Sitzungen zu springen; andere reservieren einen eigenen Worktree ausschließlich zum Lesen von Logs und für BigQuery-Abfragen. Der Grund: getrennte Arbeitsverzeichnisse bedeuten getrennte Kontexte — keine Kontamination zwischen Aufgaben.

## Planung, Review und Selbstkorrektur

Plan Mode wird von allen im Team genutzt, aber mit unterschiedlicher Disziplin. Ein wiederkehrendes Muster: eine Instanz schreibt den Plan, eine zweite Claude-Instanz prüft ihn — in der Rolle eines Staff Engineers — bevor überhaupt implementiert wird. Geht eine Aufgabe mittendrin schief, wird nicht am fehlerhaften Pfad weitergearbeitet, sondern zurück in den Plan Mode gewechselt und neu geplant.

Nach jeder Korrektur endet ein Prompt im Team häufig mit dem Satz: „Aktualisiere Deine `CLAUDE.md`, damit Du diesen Fehler nicht noch einmal machst.“ Die Datei wird so lange iterativ bearbeitet, bis die Fehlerrate messbar sinkt — laut Cherny ist Claude überraschend gut darin, eigene Regeln für sich selbst zu formulieren.

Drei weitere Prompting-Muster fordern das Modell gezielt heraus statt es nur zu instruieren: „Hinterfrage diese Änderungen kritisch und erstelle keinen PR, bis Du meinen Test bestanden hast“ (Claude als Reviewer, nicht nur als Umsetzer); „Beweise mir, dass das funktioniert“ (Verhalten zwischen `main` und Feature-Branch vergleichen lassen); und nach einem mittelmäßigen Fix: „Mit allem, was Du jetzt weißt — verwirf das und implementiere die elegante Lösung“, statt am bestehenden Pfad zu patchen.

## Skills als institutionelles Wissen

Faustregel des Teams: Alles, was man mehr als einmal am Tag tut, wird ein Skill. Genannte Beispiele: `/techdebt` findet und eliminiert doppelten Code am Ende jeder Sitzung; ein „Context dump“-Slash-Command synchronisiert Slack, Google Drive, Asana und GitHub der letzten sieben Tage in den Kontext; Analytics-Agents schreiben dbt-Modelle, reviewen Code und testen Änderungen in der Dev-Umgebung selbst. Entscheidend: Skills, die in Git eingecheckt sind, werden zu geteiltem Team-Wissen statt persönlichem Werkzeug einer einzelnen Person.

Konkretes Beispiel für diesen Effekt: ein eingecheckter BigQuery-Skill für Analytics-Abfragen. Cherny berichtet, seit über sechs Monaten keine Zeile SQL mehr selbst geschrieben zu haben — der eigentliche Vorteil sei dabei nicht, dass Claude SQL beherrscht, sondern dass man im eigenen Kontext (Produktfrage, nicht Query-Syntax) bleibt, während Claude die Übersetzungsschicht übernimmt.

## Kontext-Ökonomie und Vertrauen in den Agenten

Bugfixing läuft im Team oft ohne Kontextwechsel: Ein Bug-Thread wird per Slack-MCP direkt in Claude kopiert, dazu das Wort „fix“. Ebenso: „Geh und behebe die fehlschlagenden CI-Tests.“ Mikromanagement wird dabei explizit als kontraproduktiv benannt — dem Modell wird zugetraut, den Lösungsweg selbst zu finden.

„Nutze Subagents“ wird im Team an Anfragen angehängt, bei denen mehr Rechenleistung auf ein Problem geworfen werden soll; einzelne Teilaufgaben werden ausgelagert, um den Hauptkontext sauber zu halten. Ein drittes Subagent-Muster betrifft Sicherheit statt Kontext: Berechtigungsanfragen werden an ein stärkeres Modell (genannt: Opus 4.5) weitergeleitet, das sie auf Angriffsmuster scannt und sichere Anfragen automatisch freigibt.

Terminal-Setup: Das Team bevorzugt Ghostty wegen synchronisiertem Rendering, 24-Bit-Farben und korrekter Unicode-Unterstützung, nutzt `/statusline` zur laufenden Sicht auf Kontext-Auslastung und Git-Branch, und setzt auf Sprachdiktat (z. B. Doppel-Fn auf macOS) für komplexe Prompts — man spricht laut Quelle etwa dreimal schneller als man tippt, was zu detaillierteren, nuancierteren Prompts führt.

## Lernen mit Claude

Ein zehnter Punkt weicht vom reinen Produktivitätsfokus ab: Claude Code als Lernwerkzeug für unbekannten Code. Der „Explanatory“- bzw. „Learning“-Stil in `/config`, HTML-Präsentationen oder ASCII-Diagramme zur Erklärung komplexer Protokolle oder Code-Strukturen, sowie ein selbstgebauter „Spaced-Repetition“-Skill, der das eigene Verständnis abfragt und Wissenslücken schließt.

## Einordnung

Die Quelle ist durchgängig Erfahrungsbericht, keine Messung — jede Aussage stammt aus Selbstbeschreibung des Teams, ohne Vergleichszahlen gegen eine Baseline ohne die jeweilige Praxis. Das gilt besonders für den SQL-Punkt („seit über 6 Monaten keine Zeile SQL geschrieben“): plausibel, aber unüberprüfbar und stark abhängig davon, wie eng die Analytics-Aufgaben tatsächlich gefasst sind.

Zwei der zehn Punkte — die Plan-Review durch eine zweite Instanz „als Senior/Staff Engineer“ und Voice Dictation für komplexe Prompts — decken sich nahezu wortgleich mit den beiden Zusatzpunkten aus [[2026-02-27-meer-claude-code-best-practices]], die ebenfalls Boris Cherny zugeschrieben werden. Beide Sekundärquellen (vibedeck hier, @Meer_AIIT dort) gehen aller Wahrscheinlichkeit nach auf dieselbe Primäraussage Chernys zurück, nur über unterschiedliche Aggregatoren erfasst. Das ist kein unabhängiger Zweitbeleg, sondern dieselbe Quelle zweimal durchs Sieb — die Konfidenz der betroffenen Patterns darf dadurch nicht steigen.

Bemerkenswert ist die Konvergenz beim Permission-Routing-Punkt: Ein stärkeres Modell prüft Berechtigungsanfragen auf Angriffsmuster und gibt sichere Anfragen automatisch frei — das ist inhaltlich derselbe Mechanismus, den Anthropics „Auto Mode“ (dynamischer Klassifikator pro Befehl, bereits belegt in [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]) als Produktfeature umsetzt. Eine interne Teampraxis und ein später ausgeliefertes Feature zeigen hier in dieselbe Richtung, was die Grundidee stützt, auch wenn beide letztlich auf denselben Anthropic-Kontext zurückgehen und keine externe Bestätigung liefern.

Terminal-Wahl (Ghostty) und `/statusline` sind reine Konfigurationsentscheidungen ohne übertragbare Erkenntnis darüber hinaus, dass Terminal-Eigenschaften (Unicode, Farbtiefe, Rendering) für Coding-Agent-Workflows relevant sind — das verfällt mit dem nächsten Terminal-Release und wird hier bewusst nicht zu einem Pattern erhoben.

Für „Skills als institutionelles Wissen“ (Schwelle: mehr als einmal täglich → Skill; git-eingecheckt → Teamwissen statt Einzelwerkzeug) und für „Claude als Lernwerkzeug“ (Explanatory-Modus, Diagramme, Spaced-Repetition-Skill) gibt es im Bestand kein Pattern, das die Kernidee trägt, ohne sie zu verbiegen — siehe Vorschläge im Abschlussbericht.

Der eingangs von Cherny selbst benannte Rahmen — das Team arbeitet anders als er selbst — verdient es, wörtlich ernst genommen zu werden: Keiner der zehn Punkte ist als universelle Empfehlung formuliert, sondern als Beobachtung dessen, was in einer bestimmten Gruppe funktioniert. Das rechtfertigt Sekundärquellen-Status, aber keine Abwertung der inhaltlichen Relevanz — der Urheber von Claude Code, der beschreibt, wie sein eigenes Team das Produkt nutzt, ist eine ungewöhnlich direkte Quelle für Betriebspraxis.

## Kernaussagen

- 3-5 parallele `git worktrees` mit Shell-Aliasen zum Wechseln, teils ein dedizierter Analyse-Worktree für Logs/BigQuery → [[Kontrollierte-Agent-Parallelisierung]]
- Bei schiefgehender Aufgabe zurück in Plan Mode statt den fehlerhaften Pfad zu erzwingen; zweite Instanz prüft den Plan als Staff Engineer vor der Umsetzung → [[Plan-first-mit-getrenntem-Review]]
- Nach jeder Korrektur wird `CLAUDE.md` per Prompt aktualisiert, bis die Fehlerrate messbar sinkt → [[AGENTS-md-Onboarding-Design]]
- Drei Herausfordern-statt-Instruieren-Prompts: kritisch hinterfragen vor PR, Verhalten zwischen `main` und Feature-Branch als Beweis vergleichen, nach mittelmäßigem Fix bewusst verwerfen und neu (elegant) implementieren → [[TDD-als-Verifikationshebel]], [[Kontext-Hygiene-Entscheidungsbaum]]
- Bugfixing per Slack-MCP-Copy-Paste und „geh, behebe die CI-Tests“ ohne Mikromanagement — dem Modell wird die Pfadfindung überlassen → [[Freiheitsgrad-nach-Aufgaben-Fragilitaet]]
- Auslagern einzelner Teilaufgaben an Subagents, um den Hauptkontext sauber zu halten → [[Kontext-Hygiene-Entscheidungsbaum]]
- Berechtigungsanfragen werden an ein stärkeres Modell (Opus 4.5) geroutet, das auf Angriffsmuster scannt und sichere Anfragen automatisch freigibt → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- Eingecheckter BigQuery-Skill ersetzt selbstgeschriebenes SQL; Skills, die in Git eingecheckt sind, werden zu Team- statt Einzelwissen → kein passendes Pattern, siehe Vorschlag im Abschlussbericht
- Sprachdiktat für komplexe Prompts, weil Sprechen beiläufig mehr Kontext liefert als Tippen → [[Voice-Prompting-fuer-Kontextreichtum]]
- Explanatory-/Learning-Stil, HTML-/ASCII-Diagramme und ein Spaced-Repetition-Skill zum Verstehen unbekannten Codes → kein passendes Pattern, siehe Vorschlag im Abschlussbericht

## Verbindungen

- [[2026-02-27-meer-claude-code-best-practices]]
- [[Kontrollierte-Agent-Parallelisierung]]
- [[Plan-first-mit-getrenntem-Review]]
- [[Voice-Prompting-fuer-Kontextreichtum]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
