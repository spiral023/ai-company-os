---
url: https://developers.openai.com/codex/rules
autor: OpenAI
datum: 2026-02-28
erfasst: 2026-08-04
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-28-openai-codex-rules-guide.md
beleg_art: sekundaerquelle
---

# Codex Rules: technisch erzwungene Grenzen für Befehle außerhalb der Sandbox

Codex führt mit **Rules** einen deklarativen Mechanismus ein, der festlegt, welche Befehle das Tool außerhalb seiner Sandbox ausführen darf, ohne dass diese Entscheidung dem Modell selbst überlassen wird. Das ist der gleiche Grundgedanke wie bei technisch erzwungenen Deny-Regeln: Eine Grenze wirkt nur, wenn sie vor dem Modell greift, nicht als Hinweis im Prompt.

## Wie eine Rule aufgebaut ist

Rules liegen als `.rules`-Dateien unter `~/.codex/rules/` und werden mit `prefix_rule()` definiert. Jede Regel prüft ein Befehls-Präfix (`pattern`) und ordnet ihm eine `decision` zu: `allow` (Standard, ohne Rückfrage), `prompt` (Rückfrage vor jeder Ausführung) oder `forbidden` (Blockade ohne Rückfrage). Codex startet immer nach dem restriktivsten Treffer — `forbidden` schlägt `prompt`, `prompt` schlägt `allow`. `match`/`not_match`-Listen dienen als Unit-Tests für die Regel selbst und werden beim Laden validiert, sodass Fehler in der Regellogik früh auffallen. Nach dem Anlegen einer Regeldatei muss Codex neu gestartet werden, damit alle `rules/`-Verzeichnisse neu gescannt werden.

## Command Smuggling über Shell-Wrapper

Der praktisch wichtigste Teil des Artikels beschreibt, wie Codex verhindert, dass ein Präfix-Filter durch verpackte Shell-Aufrufe umgangen wird — etwa `["bash", "-lc", "git add . && rm -rf /"]`. Codex nutzt **Tree-sitter**, um solche Skripte zu parsen. Eine Kette wird nur dann in Einzelbefehle zerlegt und separat gegen die Rules geprüft, wenn sie ausschließlich aus einfachen Wörtern (keine Variablen-Expansion, keine Wildcards) und sicheren Operatoren (`&&`, `||`, `;`, `|`) besteht. Das Beispiel oben würde in `["git", "add", "."]` und `["rm", "-rf", "/"]` aufgeteilt — erlaubt man `git add`, aber verbietet `rm -rf`, stoppt der gesamte Aufruf.

Sobald Redirections (`>`, `>>`, `<`), Variablen-Substitutionen, Wildcards oder Control-Flow (`if`, `for`) im Skript vorkommen, verzichtet Codex auf das Splitting und behandelt den gesamten `bash -lc <script>`-Aufruf als einen einzigen, konservativ eingestuften Block. Das ist eine bewusste Fail-safe-Entscheidung, hat aber eine Kehrseite: Wer `bash` allgemein erlaubt, erlaubt implizit auch jeden nicht aufteilbaren Block, solange keine explizite `forbidden`-Regel für das gesamte Muster existiert.

## Testen ohne scharf zu schalten

Mit `codex execpolicy check --pretty --rules <pfad> -- <befehl>` lässt sich die Entscheidung für einen konkreten Befehl im JSON-Format prüfen, inklusive der greifenden Regel und ihrer `justification`. Das erlaubt, neue Regeln vor dem produktiven Einsatz gegen reale Befehle zu verifizieren, statt live zu testen.

## Starlark als Rules-Sprache

Das `.rules`-Format basiert auf **Starlark**, einer python-ähnlichen Sprache, die absichtlich keine Seiteneffekte zulässt (kein Dateisystem-, kein Netzwerkzugriff aus dem Regel-Code selbst). Die Rules-Engine kann Nutzer-Code damit sicher ausführen, ohne dass dieser Code selbst zu einem Angriffsvektor wird.

## Einordnung

Das ist offizielle OpenAI-Dokumentation, hier in sekundärer, deutscher Aufarbeitung aus vibedeck vorliegend — die Feature-Beschreibung selbst ist als Herstellerangabe zu lesen, nicht als unabhängig verifiziertes Verhalten. Fachlich ist der Kern deckungsgleich mit einem bereits im Bestand vorhandenen Pattern: Eine Grenze, die nur als Text im Modellkontext existiert, ist eine Empfehlung; eine Grenze, die eine Regel-Engine vor der Ausführung prüft, ist eine Durchsetzung. Codex Rules ist eine generalisierte, produktseitige Umsetzung genau dieses Prinzips — nicht auf Secret-Dateien beschränkt wie im bisher einzigen Beleg des Patterns, sondern auf beliebige Shell-Befehle.

Neu und über den Bestand hinausgehend ist die explizite Behandlung von **Command Smuggling durch Shell-Wrapper**: Ein naiver Präfix-Filter lässt sich durch Verkettung in einem einzigen `bash -c`-Aufruf umgehen, wenn die Engine nicht in die Kette hineinschaut. Codex' Tree-sitter-Splitting ist eine konkrete Gegenmaßnahme, mit einer sauber benannten Grenze (kein Splitting bei Variablen/Wildcards/Control-Flow — dann gilt der ganze Block als ein Objekt). Das ist ein vierter Leckpfad neben den drei bereits im Bestand dokumentierten (Direct Read, Runtime-Output-Capture, Search-Treffer) und sollte dort ergänzt werden.

Nicht geprüft werden konnte, wie robust das Splitting in der Praxis gegen kreative Umgehungsversuche ist (z. B. verschachtelte Quotings, Base64-dekodierte Befehle) — der Artikel beschreibt nur den dokumentierten Regelfall.

## Kernaussagen

- Rules erzwingen technisch, welche Befehle Codex außerhalb der Sandbox ausführen darf, mit restriktivstem Vorrang (`forbidden` > `prompt` > `allow`) statt einer bloßen Empfehlung an das Modell → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- Verpackte Shell-Aufrufe (`bash -c "cmd1 && cmd2"`) werden per Tree-sitter in Einzelbefehle zerlegt und separat geprüft, sofern die Kette nur aus einfachen Wörtern und sicheren Operatoren besteht — bei Variablen, Wildcards oder Control-Flow bleibt der gesamte Aufruf ein einziger, konservativ behandelter Block → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]] (vierter Leckpfad: Command Smuggling über Shell-Wrapper)
- Regeln lassen sich vor dem produktiven Einsatz per `codex execpolicy check` gegen konkrete Befehle validieren, inklusive Begründung der greifenden Regel
- Starlark als seiteneffektfreie Sprache erlaubt es, Nutzer-definierte Regellogik sicher auszuführen, ohne dass der Regel-Code selbst Dateisystem oder Netzwerk berühren kann

## Verbindungen

- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[2026-05-13-david-wiesen-openai-codex-windows-sandbox]]
