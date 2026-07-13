# Erweiterungs-Ebenen-Zuordnung

**Konfidenz:** meinung

## Zweck

Verhindert, dass dieselbe Anforderung mehrfach und inkonsistent auf verschiedenen Ebenen eines Coding-Agent-Setups modelliert wird (z.B. gleichzeitig in `CLAUDE.md`, einem Skill und einem Hook). Ohne klare Zuordnung wachsen Setups unnötig komplex, ohne dass klar ist, welche Ebene welche Verantwortung trägt.

## Funktionsweise

Fünf Erweiterungsebenen werden strikt nach Verantwortung getrennt: **`CLAUDE.md`/Agent-Datei** für Regeln, die *immer* gelten (Projektkonventionen, globale Guardrails, knapper Repo-Kontext) — sie muss kurz bleiben, weil sie permanent Kontext kostet. **Skills** für on-demand Wissen und wiederkehrende Workflows, mit Progressive Disclosure (Name/Beschreibung immer sichtbar, Inhalt erst bei Aktivierung geladen). **Subagents** für isolierte Arbeit mit eigenem Kontext und eng gescopten Rechten (Recherche mit vielen Dateilesen, laute Test-/Log-Ausgaben, spezialisierte Reviews) — nicht als „besserer Skill“, sondern als eigene Arbeitskammer. **Hooks** für deterministische, ereignisgetriebene Automatisierung an sechs Standard-Trigger-Punkten (`PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `PreCompact`, `Notification`) — kein freies Reasoning nötig. **MCP** für Verbindungen zu externen Diensten/Daten (GitHub, Datenbanken, Browser) — die Integrationsschicht, nicht die Arbeitslogik selbst. Die praktische Entscheidungsregel: „immer gültige Regel“ → Agent-Datei, „wiederkehrender Ablauf“ → Skill, „isolierte Teilaufgabe“ → Subagent, „immer gleicher Trigger“ → Hook, „externe Quelle/Aktion“ → MCP.

## Vorteile

- Macht sofort erkennbar, auf welcher Ebene eine neue Anforderung modelliert werden sollte, statt sie versehentlich doppelt oder an der falschen Stelle zu implementieren.
- Hält den permanenten Kontext (Agent-Datei) klein, weil alles Wiederkehrende, Isolierte oder Deterministische in die jeweils passende Ebene statt in die Hauptdatei wandert.
- Skaliert gut mit wachsender Setup-Komplexität: neue Bedürfnisse bekommen eine klare Heimat statt in eine bereits überladene Ebene gepresst zu werden.

## Nachteile & Grenzen

- Erfordert Disziplin bei jeder neuen Anforderung, die passende Ebene bewusst zu wählen — bei Zeitdruck landet Neues oft „der Einfachheit halber“ in der Agent-Datei.
- Grenzfälle sind denkbar (z.B. ein Skill, der eigentlich eine isolierte Subagent-Aufgabe wäre); die Zuordnung ist eine Heuristik, kein Algorithmus.
- Viele aktive MCP-Server oder Plugins gleichzeitig kosten Kontext und verschlechtern das Signal-Rausch-Verhältnis, selbst wenn die Zuordnung an sich korrekt ist — die Ebene allein schützt nicht vor Überladung innerhalb der Ebene.

## Wann einsetzen, wann nicht

- Einsetzen: beim Aufbau oder Ausbau eines Coding-Agent-Setups mit mehr als nur einer Handvoll Regeln, insbesondere sobald Skills, Subagents, Hooks oder MCP-Server gleichzeitig im Einsatz sind.
- Nicht einsetzen: bei minimalen Setups mit nur einer kurzen Agent-Datei und keinen weiteren Erweiterungen — dort lohnt sich die explizite Kategorisierung noch nicht.

## Belege

- 2026-04-17 · [[2026-04-17-wiki-compiler-skills-subagents-hooks-mcp-pragmatisch]] · meinung — Wiki-Artikel (synthetisiert aus offizieller Claude-Code-Doku und X-Posts) beschreibt die fünf Ebenen, die Fehlerquelle der Mehrfachmodellierung und die Einführungsreihenfolge.
- 2026-04-13 · [[2026-04-13-wiki-compiler-shorthand-guide-claude-code]] · meinung — Unabhängiger Wiki-Artikel (Quelle: praxiserprobtes persönliches Setup, X-Post @affaanmustafa) bestätigt dieselbe Ebenenaufteilung, insbesondere die sechs Hook-Trigger-Punkte und die Regel „viele MCPs konfigurieren, aber nur wenige aktiv halten“.
- 2026-02-04 · [[2026-02-04-affaanmustafa-shorthand-guide-primaer]] · meinung — Primärquelle desselben Autors konkretisiert die Faustregel (20-30 MCPs konfiguriert, <10 aktiv, <80 Tools aktiv) mit realem Setup-Beispiel (14 installierte, nur 4-5 gleichzeitig aktive Plugins) und Hook-JSON-Beispielen.
- 2026-05-01 · [[2026-05-01-mnilax-claude-code-overhead-9-patterns]] · meinung — 90-Tage-Audit (430h Nutzung) belegt konkret, dass `UserPromptSubmit`-Hooks sich zu „Prompt-Wänden“ summieren und dass MCP-Server unabhängig vom Bedarf Tool-Schemas in jede Anfrage laden — mit Audit-Kommandos, um beides sichtbar zu machen.
- 2026-01-20 · [[2026-01-20-ben-tossell-agent-coding]] · meinung — Praxisbericht bevorzugt CLIs gegenüber MCPs explizit, weil MCPs zu viel Kontext verbrauchen und oft nur wenige Tools tatsächlich gebraucht werden.

## Spannungen & offene Fragen

- Mehrere unabhängige Quellen (Shorthand-Guide-Autor, Overhead-Audit, Ben Tossell) konvergieren unabhängig auf dieselbe Kernregel „MCPs/Hooks kosten immer Kontext, auch wenn ungenutzt“ — das stützt die Aussage über bloße Einzelmeinung hinaus, auch wenn keine kontrollierte Studie vorliegt.
- Offene Frage: Wie verhält sich dieses 5-Ebenen-Modell zur bereits bestehenden [[Skill-Call-Hierarchie]] (user-invoked vs. model-invoked)? Beide Modelle scheinen orthogonal (Ebene der Verantwortung vs. Aufrufberechtigung innerhalb der Skill-Ebene), eine explizite Zusammenführung steht noch aus.

## Verwandte Patterns

- [[Skill-Call-Hierarchie]]
- [[Klein-und-komposierbar]]
- [[Kontrollierte-Agent-Parallelisierung]]
