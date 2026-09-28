---
url: https://code.claude.com/docs/en/hooks-guide
autor: Anthropic Docs
datum: 2026-02-01
erfasst: 2026-08-05
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-automate-workflows-with-hooks.md
beleg_art: sekundaerquelle
---

# Hooks in Claude Code: Blockieren per Exit-Code, und eine dritte Stufe zwischen Skript und Modellurteil

Anthropics eigene Einführung in Hooks, hier als sekundäre deutsche Aufarbeitung (vibedeck) ohne im Bestand vorhandene Primärquelle. Hooks sind benutzerdefinierte Shell-Befehle, die an festen Punkten im Claude-Code-Lebenszyklus feuern — der Kernpunkt der Dokumentation ist, dass sie **deterministische Kontrolle** liefern, nicht bloß eine weitere Form von Kontext, dem das Modell folgen kann oder auch nicht.

## Blockieren vor der Tool-Ausführung

`PreToolUse`-Hooks laufen, bevor ein Tool ausgeführt wird, und können den Aufruf technisch verhindern. Der Mechanismus dahinter: Der Hook erhält den Tool-Aufruf als JSON über `stdin` (u. a. `tool_name`, `tool_input`), Exit-Code `0` lässt die Ausführung weiterlaufen, Exit-Code `2` blockiert sie (Begründung nach `stderr`), und strukturiertere Entscheidungen lassen sich per JSON auf `stdout` treffen (z. B. `permissionDecision: "deny"`). Das im Artikel gezeigte Beispiel nutzt das, um Schreibzugriffe auf `.env`-Dateien zu verhindern: Ein Skript prüft `tool_input.file_path` auf das Substring `.env` und beendet sich mit Exit `2`, falls es einen Treffer gibt.

Andere Events aus derselben Tabelle: `SessionStart` (Session-Beginn), `PostToolUse` (nach der Tool-Ausführung) und `Stop` (wenn Claude fertig ist). Auffällig ist, dass diese Liste kürzer ist als das, was im Bestand bereits zu Hooks bekannt ist — `UserPromptSubmit` etwa taucht in [[Hook-erzwungene-Skill-Aktivierung]] bereits als eigenes Event auf, hier aber nicht. Es handelt sich damit erkennbar um einen eingekürzten Einstiegs-Auszug, nicht um die vollständige Event-Referenz.

Zusätzlich lassen sich Hooks per `matcher` gezielt auf einzelne Tools oder Event-Typen eingrenzen (`"Bash"`, `"Edit|Write"`), statt bei jedem Aufruf jedes Tools zu feuern.

## Zwei weitere Entscheidungsformen neben dem Shell-Skript

Neben dem klassischen, deterministischen Shell-Hook nennt die Dokumentation zwei weitere Hook-Typen, die im Bestand bisher nicht erfasst waren:

- **Prompt-based (`type: "prompt"`):** Ein LLM trifft die Ja/Nein-Entscheidung, statt dass ein Skript sie mit Pattern-Matching berechnet.
- **Agent-based (`type: "agent"`):** Ein Subagent mit eigenem Tool-Zugriff prüft eine Bedingung, die sich nicht ohne Ausführung feststellen lässt — genanntes Beispiel: „Laufen alle Tests?“

Das ist eine dritte, abgestufte Ebene zwischen starrem Skript (schnell, aber nur für vorher bekannte, klar formulierbare Bedingungen geeignet) und freiem Modellurteil ohne jede Struktur. Die Dokumentation selbst führt das nicht weiter aus — keine Beispiele, keine Kostenangabe, keine Aussage dazu, wie zuverlässig ein Prompt-Hook im Vergleich zum Skript-Hook tatsächlich ist.

## Troubleshooting als Hinweis auf Fehlerquellen

Genannte Fehlerquellen: ein Hook feuert nicht, weil Matcher oder Event-Typ nicht passen; JSON-Parsing schlägt fehl, wenn Shell-Profile (`.bashrc`) unbedingte `echo`-Ausgaben vor dem eigentlichen JSON ausgeben; `Ctrl+O` schaltet einen Verbose-Modus zum Debuggen frei. Das sind Konfigurationsdetails ohne übertragbaren Erkenntniswert über die konkrete Version hinaus.

## Einordnung

Die Quelle ist Anthropic-eigene Produktdokumentation, entsprechend autoritativ für die technische Funktionsweise, aber ohne jede Bewertung von Kosten oder Grenzen — reine Beschreibung „so geht es“, keine Aussage „das kostet X“ oder „das versagt bei Y“. Zwei Punkte sind eigenständig einzuordnen:

Erstens demonstriert das eigene `.env`-Schutzbeispiel der Dokumentation ungewollt genau das Problem, das [[Deny-Rules-statt-CLAUDE-md-Empfehlung]] bereits mit vier Leckpfaden beschreibt: Der gezeigte Hook prüft nur `tool_input.file_path` per Substring-Match und wird offenbar an `PreToolUse` ohne einschränkenden Matcher registriert. Er deckt damit ausschließlich den Leckpfad „direkter Write“ ab — nicht Read-Zugriffe über andere Tools, nicht Runtime-Output-Capture, nicht Search-Treffer und nicht Command-Smuggling über verpackte Bash-Aufrufe. Ein `PreToolUse`-Hook ist funktional derselbe Enforcement-Punkt wie eine `permissions.deny`-Regel (beides blockiert technisch vor der Ausführung, nicht nur per Empfehlung), aber mit selbst zu schreibender und zu wartender Skriptlogik statt einer deklarativen Liste — das verschiebt Zuverlässigkeit von der Plattform auf die Sorgfalt des Autors.

Zweitens ist die Event-Tabelle erkennbar unvollständig gegenüber dem, was im Bestand bereits zu Hooks dokumentiert ist (`UserPromptSubmit` fehlt komplett, ebenso weitere von Claude Code tatsächlich unterstützte Events). Das schwächt den Wert dieser Quelle als Referenz für die Hooks-Mechanik als Ganzes — sie taugt als Einstieg, nicht als vollständige Spezifikation.

Der eigentliche neue Fund ist die Unterscheidung deterministisches Skript / Prompt-Hook / Agent-Hook als drei Stufen wachsender Flexibilität und sinkender Vorhersagbarkeit. Das ist mehr als eine Konfigurationsdetail und über die konkrete Anthropic-Doku hinaus wiederverwendbar, aber in dieser Quelle nur als Zwei-Punkt-Erwähnung ohne Vertiefung belegt — eine zweite, unabhängige Quelle würde die Aussage deutlich stärken.

## Kernaussagen

- Hooks liefern deterministische Automatisierung an festen Lifecycle-Punkten (Shell-Kommandos) — eine der Erweiterungsebenen neben CLAUDE.md, Skill, Subagent und MCP → [[Erweiterungs-Ebenen-Zuordnung]]
- `PreToolUse`-Hooks können per Exit-Code 2 vor der Tool-Ausführung technisch blockieren; das im Artikel gezeigte `.env`-Schutzbeispiel deckt aber nur den Leckpfad „direkter Write“ ab, nicht die drei anderen bereits dokumentierten Leckpfade → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- Neben deterministischen Shell-Hooks gibt es Prompt-based Hooks (LLM trifft Ja/Nein-Entscheidung) und Agent-based Hooks (Subagent mit Tool-Zugriff prüft nicht-triviale Bedingungen wie „laufen alle Tests“) als dritte, abgestufte Ebene zwischen starrem Skript und freiem Modellurteil → neues Pattern vorgeschlagen (siehe Abschlussbericht)
- Matcher grenzen Hooks gezielt auf Tool-Namen oder Event-Typen ein, statt bei jedem Aufruf jedes Tools zu feuern — dieselbe Zielgerichtetheit, die die Keyword-/Intent-Prüfung in [[Hook-erzwungene-Skill-Aktivierung]] technisch voraussetzt → [[Hook-erzwungene-Skill-Aktivierung]]

## Verbindungen

- [[Hook-erzwungene-Skill-Aktivierung]]
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[Erweiterungs-Ebenen-Zuordnung]]
- [[2026-04-17-wiki-compiler-skills-subagents-hooks-mcp-pragmatisch]]
