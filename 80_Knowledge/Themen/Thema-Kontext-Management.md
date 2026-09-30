# Kontext-Management

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-09-30. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Was im Kontextfenster steht und wie man es sauber hält: Context Rot, Compact, Clear, Rewind, Handoff zwischen Sessions, Kontextkosten von Tools. Regeldateien gehören zu agent-dateien, die Kosten des Cachings zu modelle-kosten.

## Suchbegriffe

- **Hauptkeyword:** Context Engineering
- **Long-Tail:** Context Rot vermeiden; Claude Code /compact oder /clear; Claude Code Kontextfenster verwalten; Session Handoff Dokument; Rewind statt Korrektur; Subagents als Kontextgrenze
- **Fragen:** Wann sollte ich /clear statt /compact nutzen? / Warum wird mein Agent in langen Sessions schlechter?
- **Häufig in den Quellen:** context rot (7), context window (6), /clear (6), progressive disclosure (6), /compact (5), claude.md (5), context engineering (4), subagents (4), rewind (4), claude code hooks (4), claude code skills (4), prompt caching (4), context pollution (3), plan mode (3), autocompact-puffer (2), mcp tools (2), ralph loop (2), subagent-kosten (2), userpromptsubmit hook (2), subagents als kontextgrenze (2)

## Verwandte Themen

- [[Thema-Agent-Dateien-Memory]] — Agent-Dateien & Memory
- [[Thema-Modelle-Kosten-Limits]] — Modelle, Kosten & Limits
- [[Thema-Multi-Agent-Parallelisierung]] — Multi-Agent & Parallelisierung
- [[Thema-Spezifikation-Planung]] — Spezifikation & Planung

## Patterns (2)

- [[Handoff-Doc]] · verifiziert · 17 Belege
- [[Kontext-Hygiene-Entscheidungsbaum]] · mehrfach-belegt · 36 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[AGENTS-md-Onboarding-Design]], [[CONTEXT-Glossar]], [[MCP-Code-Execution-statt-Tool-Definitionen]], [[Ralph-Loop-Frischer-Kontext-pro-Iteration]], [[Spec-Ordner-pro-Feature]]

## Quellen (16)

- [[2026-09-04-julian-ivanov-ki-automat-so-nutzt-du-claude-code-nach-anthropics-neuen-re]] — Weniger Anweisungen, mehr Absicht und messbares Abschlusskriterium: Kontext klein halten, Garantien in Hooks legen und das Setup bei jedem Modellwechsel ausdünnen.
- [[2026-08-14-agenticjames-ai-memory-is-trash-heres-some-solutions]] — Agent Memory ist nicht ein Problem, sondern vier: Ablage, Turn-Erinnerung, multimodale Suche und Abrufzeitpunkt, wobei Pull durch den Agenten und Push per Hook Kosten und Nutzen tauschen.
- [[2026-08-03-steffen_hauptmann-die-meisten-lassen-sich-ein-handover-erst-schreiben-wenn-das]] — Eine fortlaufend gepflegte Zustandsdatei macht den Handover schon vor vollem Context Window verfügbar, kostet aber laufend Tokens und kann bei falschem Stand irreführen.
- [[2026-07-30-floknowsai-ki-gibt-dir-das-gefuehl-dass-du-so-schnell-wie-noch-nie-arbeitest]] — Erfahrene Entwickler fühlen sich mit KI schneller, messen aber langsamer, und falscher Kontext schadet mehr als gar keiner, weshalb Pflege wichtiger ist als Sammeln.
- [[2026-07-13-mattpocock-handoff-to-teach]] — Wissenslücken während einer Grilling-Session per Handoff an einen Lern-Workspace auslagern hält die Session fokussiert und bewahrt den Lernfortschritt.
- [[2026-07-12-agenticjames-claude-codes-new-feature-checkup-makes-claude-more-token-efficient-and]] — Ein automatisches Aufräumen von Skills, MCP-Servern und CLAUDE.md senkt den Baseline-Kontext, verschiebt aber Kontrolle und birgt das Risiko, wichtige Regeln oder Fähigkeiten zu entfernen.
- [[2026-06-06-agenticjames-your-agent-is-referencing-documentation-when-it-should-be-reading-the]] — Agenten sollten gegen den lokal abgelegten Quellcode von Dependencies statt nur gegen Doku arbeiten, damit sie nicht raten; Nutzen und Kosten sind ungeprüft.
- [[2026-05-04-wiki-compiler-claude-session-und-token-management]] — Gute Claude-Nutzung optimiert auf klar geschnittene Arbeitsblöcke mit bewusstem Kontext statt lange Chats, gestützt auf Handoff-Summaries und eine Prompt-Checkliste.
- [[2026-04-29-wiki-compiler-claude-code-session-management-1m-context]] — Nach jedem Arbeitsblock bewusst zwischen Continue, Rewind, Compact, Clear und Subagent wählen, weil mehr Kontext ab etwa 300k Tokens Context Rot riskiert.
- [[2026-04-22-agenticjames-everything-you-need-to-know-about-context-engineering-in-1-minute]] — Was nicht im Context Window landet, kennt der Agent nicht; CLAUDE.md oder AGENTS.md ist der immer geladene Stamm, von dem Verweise bei Bedarf abzweigen.
- [[2026-04-15-trq212-claude-code-session-management-1m-context-primaer]] — Ein 1M-Kontext ist kein pauschaler Gewinn: Früh und aktiv kompaktieren, neue Aufgabe meist neue Session, Subagents als Kontextgrenze nutzen.
- [[2026-02-14-gmoney-eth-25-claude-code-lessons]] — Das Context Window wie RAM behandeln: früh löschen, Subagents nutzen, 3 bis 5 parallele Sessions in eigenen Worktrees fahren und bei Misserfolg neu ansetzen.
- [[2026-01-25-sankalp-claude-code-experience]] — Subagents, Checkpoints und frühe Handoffs steuern das 200k-Budget; ein zweites Modell (Codex) reviewt besser als das bauende Claude.
- [[2026-01-21-aiedge-claude-50-pro-tips]] — Bei anhaltender Verwirrung Kontext zurücksetzen, günstig prototypen und autonome Desktop-Agenten wie Cowork per Ordner-Isolation und Backups absichern.
- [[2026-01-15-avasdr34m-its-not-easy-but-it-is-simple-kontext-nutzung-in-claude-code-entscheidet]] — Je länger der Kontext, desto schlechter das Modell: MCP-Overhead vermeiden, Aufgaben in frischen Sessions abarbeiten und Research von Implementierung trennen.
- [[2026-01-06-jarrodwatts-context-engineering-guide]] — Wer den Kontext als einzigen Stellhebel versteht, hält ihn schlank, setzt schlechte Sessions zurück und lagert teure Recherche in Subagents aus.

## Quellen mit diesem Thema als Nebenthema

- [[2026-09-17-agenticjames-i-think-code-mode-mcps-are-probably-the-best-way-to-give-agents-access]]
- [[2026-08-14-claude-maximizing-the-value-of-your-claude-code-session]]
- [[2026-08-12-voxyz_ai-2087579867139264681]]
- [[2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso]]
- [[2026-07-27-cerebras-gpt-5-6-modellwahl-und-reasoning]]
- [[2026-07-25-agenticjames-they-cut-claude-code-system-prompt-by-80-and-you-should-be-doing-the]]
- [[2026-07-21-promptgefluester-prompt-engineering-ist-tot-und-keiner-hats-gemerkt-was-meine-ich-damit]]
- [[2026-07-17-promptgefluester-ich-werd-gerade-extrem-dafuer-kritisiert-dass-ich-an-meine-videos-gesagt]]
- [[2026-07-10-voxyz-mattpocock-skills]]
- [[2026-07-08-claudedevs-modell-vs-effort]]
- [[2026-07-06-mattpocock-writing-great-skills-beyond-skills]]
- [[2026-07-03-calebwritescode-loop-engineering-explained-in-7-min-and-simplified]]
- [[2026-05-01-mnilax-claude-code-overhead-9-patterns]]
- [[2026-04-29-wiki-compiler-claude-usage-limits-token-strategien]]
- [[2026-04-17-wiki-compiler-ralph-loop]]
- [[2026-04-17-wiki-compiler-kontextsteuerung-verifikation-tdd]]
- [[2026-04-17-wiki-compiler-agent-teams-in-claude-code]]
- [[2026-04-16-wiki-compiler-context7]]
- [[2026-04-13-wiki-compiler-gute-agents-md-schreiben]]
- [[2026-03-29-0x-kaize-claude-usage-limits-primaer]]
- [[2026-03-21-sourfraser-claude-obsidian-ai-employee]]
- [[2026-02-27-thariq-lessons-building-claude-code]]
- [[2026-02-23-elvis-openclaw-codex-agent-swarm]]
- [[2026-02-10-boris-tane-plan-annotation-workflow]]
- [[2026-02-09-pdrmnvd-how-claude-code-skills-work]]
- [[2026-02-07-daniel-san-agent-teams-praxismuster]]
- [[2026-02-02-anthony-riera-planning-with-files-skill]]
- [[2026-02-01-anthropic-docs-how-claude-code-works]]
- [[2026-02-01-anthropic-docs-connect-claude-code-to-mcp]]
- [[2026-02-01-anthropic-docs-claude-code-best-practices]]
- [[2026-01-14-ashpreetbedi-claude-code-spec-first]]
- [[2026-01-12-eyad-khrais-claude-code-tutorial-level-2]]
- [[2026-01-10-eyad-khrais-claude-code-tutorial]]
