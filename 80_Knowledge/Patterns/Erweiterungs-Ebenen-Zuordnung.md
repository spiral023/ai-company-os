# Erweiterungs-Ebenen-Zuordnung

**Konfidenz:** meinung

## Zweck

Verhindert, dass dieselbe Anforderung mehrfach und inkonsistent auf verschiedenen Ebenen eines Coding-Agent-Setups modelliert wird (z.B. gleichzeitig in `CLAUDE.md`, einem Skill und einem Hook). Ohne klare Zuordnung wachsen Setups unnötig komplex, ohne dass klar ist, welche Ebene welche Verantwortung trägt.

## Funktionsweise

Fünf Erweiterungsebenen werden strikt nach Verantwortung getrennt: **`CLAUDE.md`/Agent-Datei** für Regeln, die *immer* gelten (Projektkonventionen, globale Guardrails, knapper Repo-Kontext) — sie muss kurz bleiben, weil sie permanent Kontext kostet. **Skills** für on-demand Wissen und wiederkehrende Workflows, mit Progressive Disclosure (Name/Beschreibung immer sichtbar, Inhalt erst bei Aktivierung geladen). **Subagents** für isolierte Arbeit mit eigenem Kontext und eng gescopten Rechten (Recherche mit vielen Dateilesen, laute Test-/Log-Ausgaben, spezialisierte Reviews) — nicht als „besserer Skill“, sondern als eigene Arbeitskammer. **Hooks** für deterministische, ereignisgetriebene Automatisierung an sechs Standard-Trigger-Punkten (`PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `PreCompact`, `Notification`) — kein freies Reasoning nötig. **MCP** für Verbindungen zu externen Diensten/Daten (GitHub, Datenbanken, Browser) — die Integrationsschicht, nicht die Arbeitslogik selbst. Die praktische Entscheidungsregel: „immer gültige Regel“ → Agent-Datei, „wiederkehrender Ablauf“ → Skill, „isolierte Teilaufgabe“ → Subagent, „immer gleicher Trigger“ → Hook, „externe Quelle/Aktion“ → MCP. Für den oft unscharfen Grenzfall Agent-Datei/Skill liefert ein unabhängiger Autor einen griffigen Litmus-Test: „Würdest du wollen, dass diese Instruktion auch gilt, wenn du gerade nicht aktiv daran denkst? Ja → Agent-Datei/Rule, Nein → Skill.“

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
- 2026-01-21 · [[2026-01-21-tempoimmaterial-agent-skills-vs-rules-vs-commands]] · meinung — Ergänzt einen Litmus-Test für den Rule/Skill-Grenzfall („würde ich wollen, dass die Instruktion auch gilt, wenn ich nicht aktiv daran denke?“) sowie konkrete Beispielpaare (`.env` nie committen = Rule; Billing-Tests bei Billing-Changes = Skill).
- 2026-02-09 · [[2026-02-09-pdrmnvd-how-claude-code-skills-work]] · meinung — Präzisiert die Skill-Ebene mit einer konkreten Zahl: rund 100 Wörter Name+Description pro Skill sind permanent im Kontext, bevor überhaupt ein Trigger feuert.
- 2026-01-06 · [[2026-01-06-jarrodwatts-context-engineering-guide]] · meinung — Ergänzt MCP als „Just-in-Time“-Context-Strategie mit drei benannten Beispiel-Servern (`exa.ai`, `context7`, `grep.app`) und die griffige Gegenüberstellung „Skills sind kinda the reverse of subagents“ — Kontextrichtung (hinein vs. hinaus) als zusätzliches Unterscheidungsmerkmal zwischen Skill- und Subagent-Ebene.
- 2026-01-12 · [[2026-01-12-dhruv1103-lessons-learned-500k-lines-claude-code]] · meinung — Zwei konkrete Instanzen der Skill- und MCP-Ebene: ein Skill pro Architektur-Modul, der dessen Implementierung erklärt; Read-only-MCP-Zugriff auf die Datenbank für autonome Fehlerdiagnose, ohne dass Abfragen von Hand geliefert werden müssen — konkretisiert die MCP-Integrationsschicht um ein Rechte-Scoping-Beispiel.
- 2026-01-22 · [[2026-01-22-hooeem-claude-code-7-schritte-plan]] · meinung — MCP-Server (Beispiel Playwright) geben Zugriff auf externe Werkzeuge; Tools lassen sich in den Settings für einen schnelleren Workflow automatisch genehmigen — knappe Bestätigung der MCP-Integrationsebene.
- 2026-02-01 · [[2026-02-01-aiedge-claude-code-starter-pack]] · meinung — Unabhängige Lernpfad-Grafik (Core CLI → Configuration → Extension Systems → Programmatic Usage → Enterprise Deployment) bestätigt die Level 2/3-Kategorisierung dieses Patterns aus der Perspektive einer Lernreihenfolge statt einer Verantwortungs-Heuristik; ergänzt zwei zusätzliche Reifegrad-Achsen, die im Pattern bisher nicht als eigene Ebene auftauchen: SDK/Headless/CI als Kompetenzstufe und Enterprise-Betrieb (IAM, Netzwerk, Monitoring).
- 2026-02-01 · [[2026-02-01-anthropic-docs-automate-workflows-with-hooks]] · meinung — Anthropics eigene Hooks-Doku bestätigt die Hook-Ebene als deterministische, ereignisgetriggerte Automatisierung an festen Lifecycle-Punkten (`PreToolUse`, `PostToolUse`, `SessionStart`, `Stop`); `matcher` grenzt Hooks gezielt auf Tool-Namen oder Event-Typen ein, statt bei jedem Aufruf jedes Tools zu feuern.
- 2026-07-30 · [[2026-07-30-floknowsai-ki-gibt-dir-das-gefuehl-dass-du-so-schnell-wie-noch-nie-arbeitest]] · meinung — Nennt drei Kontext-Orte (Regeln in CLAUDE.md, Skills, Wissenssystem/Connectors) als Einsteiger-Aufteilung. Kein neuer Gehalt gegenüber dem Bestand, nur Laienformulierung.
- 2026-08-21 · [[2026-08-21-promptgefluester-agent-plug-ins-das-ist-der-neue-standard-mit-dem-die-grossen-ai]] · meinung — Beschreibt Agent Plugins (`plugin.json`, `skills/`, `mcp.json`) als anbieterübergreifende Verpackung für Skills und MCP; ergänzt die Zuordnung um die Auslieferungsebene. Einschränkung: nur Kommentarvideo und ChatGPT-Screenshot, keine Primärspezifikation.
- 2026-02-01 · [[2026-02-01-anthropic-docs-connect-claude-code-to-mcp]] · meinung — MCP-Scopes Local/Project/User und `managed-mcp.json` für Enterprise-Policies; Zweitfassung der Herstellerdoku, Stand Februar 2026.
- 2026-02-01 · [[2026-02-01-anthropic-docs-extend-claude-code]] · meinung — Herstellerseitige Entscheidungstabelle CLAUDE.md/Skill/Subagent/MCP/Hook inklusive Kontext-Kosten pro Ebene; bestätigt den Bestand, Sekundärfassung.
- 2026-02-01 · [[2026-02-01-anthropic-docs-extend-claude-with-skills]] · meinung — Skill-Orte Personal, Project, Plugin und Zusammenführung von Commands und Skills; Sekundärquelle (vibedeck).
- 2026-09-21 · [[2026-09-21-voxyz_ai-2102050225443766571]] · meinung — Komponentenbibliothek wird als Skill verpackt (Quelle, Auswahlkriterien, Prüfschritt) statt Links pro Auftrag einzufügen. Selbstberichtet, ohne Ergebnisprüfung.

## Spannungen & offene Fragen

- Mehrere unabhängige Quellen (Shorthand-Guide-Autor, Overhead-Audit, Ben Tossell) konvergieren unabhängig auf dieselbe Kernregel „MCPs/Hooks kosten immer Kontext, auch wenn ungenutzt“ — das stützt die Aussage über bloße Einzelmeinung hinaus, auch wenn keine kontrollierte Studie vorliegt.
- Offene Frage: Wie verhält sich dieses 5-Ebenen-Modell zur bereits bestehenden [[Skill-Call-Hierarchie]] (user-invoked vs. model-invoked)? Beide Modelle scheinen orthogonal (Ebene der Verantwortung vs. Aufrufberechtigung innerhalb der Skill-Ebene), eine explizite Zusammenführung steht noch aus.
- Ergänzung 2026-01-21: Ein Quellenautor bemängelt eine fehlende sechste Ebene „Commands/Slash-Commands“ als expliziter, deterministischer Trigger. Bei näherer Prüfung deckt die bereits bestehende [[Skill-Call-Hierarchie]] (user-invoked vs. model-invoked) genau diese Achse ab — Commands sind die deterministische, user-invoked Seite dieser Unterscheidung. Keine sechste Ebene nötig, aber die Verlinkung zwischen beiden Patterns ist damit expliziter geworden.

## Verwandte Patterns

- [[Skill-Call-Hierarchie]]
- [[Klein-und-komposierbar]]
- [[Kontrollierte-Agent-Parallelisierung]]
