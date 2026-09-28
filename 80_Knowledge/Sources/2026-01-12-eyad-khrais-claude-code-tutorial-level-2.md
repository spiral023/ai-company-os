---
url: https://x.com/eyad_khrais/status/2010810802023141688
autor: Eyad Khrais
datum: 2026-01-12
erfasst: 2026-08-04
typ: tweet
rohquelle: 00_Inbox/Quellen/X/2026-01-12-eyad-khrais-claude-code-tutorial-level-2.md
beleg_art: sekundaerquelle
---

# Claude Code jenseits der Grundlagen: Skills, Subagents und MCP als ein System

Zweiter Teil desselben Autors (Eyad Khrais) zu einem separaten X-Thread, zwei Tage nach dem Grundlagen-Tutorial. Während Teil 1 Einstiegsdisziplin behandelte (Plan Mode, `CLAUDE.md`, Kontextgrenzen, Modellwahl, Headless Mode), geht Teil 2 auf ein anderes Thema über: die drei Erweiterungsebenen **Skills**, **Subagents** und **MCP Connectors**, die Claude Code laut Autor vom Chat-Werkzeug zu einem „autonomen Entwicklungssystem“ machen. Inhaltlich ist das größtenteils Neuland gegenüber Teil 1 — mit einer Ausnahme: Die Kontextdegradierungs-Schwelle wird hier erneut genannt, allerdings mit einer dritten, wieder abweichenden Zahl (siehe Einordnung).

## Context Window als Ausgangspunkt

Der Autor eröffnet mit einem Vergleichsanspruch: Cursor kürze laut „Analysen von Qodo“ den Kontext intern aus Performance-Gründen, während Claude Code konstant und explizit das volle 200K-Token-Fenster liefere. Das sei bei großen, vernetzten Codebasen für komplexe Aufgaben entscheidend.

## Skills: Workflows als abrufbares Wissen

Ein Skill ist eine Markdown-Datei unter `~/.claude/skills/<name>/SKILL.md` mit Frontmatter (`name`, `description`) und Instruktionsteil, die Claude automatisch anwendet, sobald die Anfrage zum Skill passt. Der zentrale Mechanismus ist Progressive Disclosure: Beim Start lädt Claude nur Name und Beschreibung, die vollen Instruktionen erst bei tatsächlicher Aktivierung — das schont das Context Window.

## Subagents: isolierter Kontext für parallele Arbeit

Ein Subagent ist eine separate Claude-Instanz mit eigenem Context Window und eigenen Berechtigungen. Als Begründung nennt der Autor, dass Kontext-Degradierung „oft ab ca. 45% Auslastung“ beginnt — Subagents halten die Hauptkonversation dadurch sauber. Claude Code bringt drei eingebaute Subagents mit: **Explore** (schneller Read-only-Such-Agent), **Plan** (Recherche-Agent für Architektur-Entscheidungen) und **General-purpose** (komplexe, mehrstufige Aufgaben). Eigene Subagents lassen sich unter `~/.claude/agents/` als Markdown mit Frontmatter (`name`, `description`, `tools`) definieren, etwa ein auf Sicherheitsreview eingeschränkter `security-reviewer` mit den Tools `Read, Grep, Glob`. Kommunikation läuft laut Autor nicht über geteilten Kontext, sondern über Delegation und Zusammenfassung: Der Hauptagent erhält nur die gefilterten Ergebnisse des Subagents zurück, nie dessen vollen Arbeitskontext.

## MCP Connectors: die Integrationsschicht zu externen Diensten

MCP (Model Context Protocol) verbindet Claude Code über ein einheitliches Interface mit externen Diensten — Beispielbefehl: `claude mcp add --transport http github https://api.github.com/mcp`. Als Anwendungsfälle nennt der Autor das Implementieren von Features direkt aus JIRA-Issues, PostgreSQL-Abfragen direkt aus Claude, Figma-Design-Import und das Zusammenfassen von Slack-Threads — Workflows, die vorher fünf Tab-Wechsel brauchten, laufen laut Autor jetzt in einer Session.

## Der Compound-Effekt

Der Autor schließt mit der These, dass die eigentliche Wirkung erst entsteht, wenn Skill (kodiert Team-Konventionen), Subagent (übernimmt Testing/Security-Review) und MCP (verbindet mit dem Issue-Tracker) zusammenwirken, und dass sich die Zeit für das Konfigurieren „doppelt“ auszahle.

## Einordnung

Der Text bleibt ein einzelner, unabhängig unbelegter Erfahrungsbericht desselben Autors wie Teil 1 (sekundäre deutsche Aufarbeitung eines weiteren X-Threads, keine kontrollierte Messung). Die drei Kernthemen (Skills, Subagents, MCP) sind im Bestand bereits ausführlicher und mit konkreteren Zahlen dokumentiert — etwa die ~100-Wörter-Kontextkosten pro Skill-Name+Description oder die 20-30-konfiguriert/<10-aktiv-Faustregel für MCP in [[Erweiterungs-Ebenen-Zuordnung]]. Diese Quelle liefert dazu keine neue Präzisierung, sondern bestätigt die grobe Struktur ein weiteres Mal auf Meinungsebene, ohne dass erkennbar ist, ob der Autor unabhängig vom bereits erfassten Wiki-/Doku-Material zu denselben Schlüssen kam. Das zählt daher nicht als unabhängige Zweitbestätigung im engeren Sinn.

Auffällig und eigenständig festzuhalten: Die hier genannte Kontext-Degradierungsschwelle („ca. 45% Auslastung“) unterscheidet sich von der Zahl, die derselbe Autor zwei Tage zuvor im Grundlagen-Thread genannt hat („20-40% eines 200k-Fensters“, siehe [[2026-01-10-eyad-khrais-claude-code-tutorial]]). Beide Zahlen sind unbelegte Erfahrungswerte desselben Autors aus zwei verschiedenen Threads — das ist kein neuer, unabhängiger Datenpunkt, sondern eine Inkonsistenz innerhalb der eigenen Aussagen des Autors, die die Verlässlichkeit seiner konkreten Prozentangaben zusätzlich schwächt (zumal beide Werte auch von der im Bestand dokumentierten 300k-400k-Token-Heuristik in [[Kontext-Hygiene-Entscheidungsbaum]] abweichen).

Der Eingangsclaim zu Cursor („kürzt Kontext laut Analysen von Qodo“) ist eine Dritthand-Behauptung (Autor zitiert eine nicht näher benannte Qodo-Analyse) in einem Text, der explizit für Claude Code wirbt — ein klassischer Fall von unbelegter, potenziell selektiver Konkurrenzaussage. Ohne die Primärquelle zu prüfen, gehört das nicht als Tatsache, sondern nur als zitierte Behauptung in den Bestand. Ebenso ist der „Compound-Effekt“ am Ende reine Plausibilitätsbehauptung ohne Zahl oder Fallbeispiel („zahlt sich doppelt aus“ ist keine Messung).

## Kernaussagen

- Claude Code liefert laut Autor konstant das volle 200K-Token-Fenster, während Cursor laut einer zitierten (nicht selbst geprüften) Qodo-Analyse intern kürze → [[Kontext-Hygiene-Entscheidungsbaum]] (unbelegte Dritthand-Behauptung, siehe Einordnung)
- Skills sind Markdown-Dateien mit Progressive Disclosure (Name/Beschreibung permanent geladen, volle Instruktionen erst bei Aktivierung) → [[Erweiterungs-Ebenen-Zuordnung]]
- Subagents laufen mit eigenem Context Window und eigenen Rechten; Kommunikation mit dem Hauptagenten läuft über Delegation und gefilterte Zusammenfassung, nicht über geteilten Kontext → [[Erweiterungs-Ebenen-Zuordnung]], [[Kontrollierte-Agent-Parallelisierung]]
- Kontext-Degradierung setzt laut Autor „oft ab ca. 45% Auslastung“ ein — abweichend von seiner eigenen 20-40%-Angabe zwei Tage zuvor und von der 300k-400k-Token-Heuristik im Bestand → [[Kontext-Hygiene-Entscheidungsbaum]] (Spannung, siehe Einordnung)
- MCP verbindet Claude Code über ein einheitliches Interface mit externen Diensten (JIRA, PostgreSQL, Figma, Slack) → [[Erweiterungs-Ebenen-Zuordnung]]

## Verbindungen

- [[Erweiterungs-Ebenen-Zuordnung]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Kontrollierte-Agent-Parallelisierung]]
- [[2026-01-10-eyad-khrais-claude-code-tutorial]]
