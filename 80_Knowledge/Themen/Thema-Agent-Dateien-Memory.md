# Agent-Dateien & Memory

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-28. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

CLAUDE.md, AGENTS.md und ähnliche Onboarding-Dateien: Länge, Ort, Progressive Disclosure, Regelbudget, Memory-Systeme und LLM-Wikis. Skills und Hooks gehören zu skills und erweiterungen. Inhaltliche Aufnahme, Aufbereitung, Retrieval und regelmäßige Pflege von Quellen stehen in wissensarbeit.

## Suchbegriffe

- **Hauptkeyword:** CLAUDE.md
- **Long-Tail:** CLAUDE.md schreiben; AGENTS.md Best Practices; CLAUDE.md zu lang; Progressive Disclosure Agent; Claude Code Memory; LLM Wiki aufbauen
- **Fragen:** Wie lang darf eine CLAUDE.md sein? / Was gehört in AGENTS.md und was in einen Skill?
- **Häufig in den Quellen:** agents.md (14), claude.md (9), progressive disclosure (7), context engineering (5), agent-datei (4), coding_standards.md (3), agent_docs (2), instruktionsbudget (2), instruction following (2), mcp-server (2), agentbench (2), llm-generierte context files (2), claude code hooks (2), obsidian (2), llm wiki (2), /doctor (2), retro (2), test (2), regeln (2), handlungsbedarf (2)

## Verwandte Themen

- [[Thema-Kontext-Management]] — Kontext-Management
- [[Thema-Skill-Design]] — Skill-Design
- [[Thema-Hooks-MCP-Erweiterungs-Ebenen]] — Hooks, MCP & Erweiterungs-Ebenen
- [[Thema-Prompting-Klärung]] — Prompting & Klärung

## Patterns (2)

- [[AGENTS-md-Onboarding-Design]] · mehrfach-belegt · 45 Belege
- [[Handlungsbedarf-zuerst-im-Agent-Bericht]] · meinung · 3 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Helper-Nutzung-durch-Lint-erzwingen]], [[Wissenspflege-mit-Inbox-und-Review]]

## Quellen (22)

- [[2026-10-25-voxyz_ai-2114446907355648062]] — Vox empfiehlt, bei Widersprüchen vorhandene Codekonventionen zu berücksichtigen und Abweichungen zur Dokumentation ausdrücklich zu melden.
- [[2026-10-24-voxyz_ai-2114069417902403786]] — Vox schlägt eine überprüfbare Pflege von Agent-Dateien vor: Der Agent sammelt konkrete Konflikte, während der Mensch auswählt, welche Regeln geändert werden.
- [[2026-10-07-voxyz_ai-2107939019091005836]] — Vox empfiehlt unter **200 Zeilen** je Agent-Datei und nennt **32 KiB insgesamt** als Codex-Standardlimit.
- [[2026-10-05-voxyz_ai-2107123654219743712]] — Vox beschreibt lange Abschlussberichte, in denen notwendige Nutzeraktionen zwischen anderen Ergebnissen verschwinden.
- [[2026-10-04-voxyz_ai-2106783910055006342]] — Vox empfiehlt eine kompakte `AGENTS.md` gegen vorschnelle Kompatibilitätsschichten, ungenutzte Altdateien und Tests für belanglose Details.
- [[2026-09-26-mattpocockuk-2103748049906397613]] — Matt Pocock empfiehlt, wiederkehrende Agentenfehler in `CODING_STANDARDS.md` festzuhalten. Die Regeln entstehen aus tatsächlichen Fehlversuchen statt aus einer vorab möglichst vollständigen Standardsammlung.
- [[2026-09-18-repo-anthropics-claude-code-agents-md-support]] — Claude Code liest seit 2.1.277 AGENTS.md, wenn keine CLAUDE.md existiert, sodass eine Instruktionsdatei mehrere Agents bedienen kann; eine zusätzliche CLAUDE.md hat Vorrang.
- [[2026-08-21-openknowledge-open-knowledge-format-plugin-for-llm-wikis-openk]] — Lint-Warnungen direkt im Tool-Ergebnis steuern Agents kostengünstig ohne Blockade; harte Durchsetzung braucht weiterhin ein separates CI-Gate.
- [[2026-07-25-agenticjames-they-cut-claude-code-system-prompt-by-80-and-you-should-be-doing-the]] — Neuere Modelle arbeiten mit weniger vorgegebenem Kontext besser; lange CLAUDE.md-Dateien sollten gekürzt und Wissen in bei Bedarf ladbare Skills ausgelagert werden.
- [[2026-07-17-matt-pocock-kill-your-memory-md]] — Matt Pocock bevorzugt im Beitrag vom 17.
- [[2026-07-06-mattpocockuk-2074060484047712521]] — Matt Pocock empfiehlt einen Zwei-Schritt-Trick fürs Debugging: den Dev-Server per `tee` in eine lokale Datei schreiben lassen und in `AGENTS.md` auf diese Datei verweisen.
- [[2026-04-21-natebjones-this-is-so-important-if-you-use-ai-as-a-solo-business-or-ic-theres-a]] — Ein LLM-Wiki passt zu Verbindungsarbeit einzelner Personen, für zitierbare Fakten im Großen braucht es eine Datenbank und für parallele Agenten ein anderes Modell.
- [[2026-04-13-wiki-compiler-shorthand-guide-claude-code]] — Hooks automatisieren deterministisch, MCPs und Subagents bewusst klein und eng gescopt halten; das Kontextfenster ist die knappe Ressource.
- [[2026-04-13-wiki-compiler-gute-agents-md-schreiben]] — Agent-Dateien kurz, universell relevant und gestaffelt halten; Stilregeln gehören in Formatter und Linter, nicht in AGENTS.md.
- [[2026-03-21-sourfraser-claude-obsidian-ai-employee]] — Eine Memory-Datei als Onboarding-Dokument plus Schreibzugriff auf einen Obsidian-Vault gibt Claude persistentes Gedächtnis; Rechte, Qualität und Datenschutz bleiben offen.
- [[2026-02-26-omarsar0-agents-md-evaluation]] — Menschlich geschriebene Context Files bringen etwa 4 Prozent mehr Erfolg, LLM-generierte senken ihn und kosten über 20 Prozent mehr; schreibe für die Lücke, nicht den Überblick.
- [[2026-02-25-heynavtoor-claude-cowork-setup-guide]] — Für Büroarbeit mit Claude Cowork genügen ein Ordner mit Kontextdateien und die Anweisung, vor der Arbeit klärende Fragen zu stellen.
- [[2026-02-14-minty-mastering-claude-code]] — Ein schlanker Memory-Index gegen den Fresh-Context-Neustart und ein Orchestrator, bei dem das teure Modell plant und günstigere Worker implementieren, senken Aufwand und Kosten.
- [[2026-02-09-tom-crawshaw-claude-code-insights-guide]] — Die Auswertung der eigenen Sessions per /insights zeigt Reibung durch fehlenden Startkontext und unklares Done; kurzer CLAUDE.md-Kontext und Slash Commands helfen.
- [[2026-02-03-svpino-claude-code-md-tips]] — Fünf kurze CLAUDE.md-Regeln erzwingen Plan, kleine Schritte und Test zuerst; die Selbstverbesserungsregel lässt die Datei jedoch unkontrolliert wachsen.
- [[2026-02-03-god-of-prompt-karpathy-ai-coding-system-prompt]] — Ein CLAUDE.md-Prompt gegen typische Agent-Fehler bündelt bekannte Prinzipien, konkurriert aber als langer Text im Kontext und wird nur weich befolgt.
- [[2026-02-01-humanlayer-writing-a-good-claude-md]] — Eine CLAUDE.md sollte kurz, handgeschrieben und per Progressive Disclosure strukturiert sein, weil das Modell irrelevant wirkenden Inhalt bewusst ignoriert.

## Quellen mit diesem Thema als Nebenthema

- [[2026-10-27-voxyz_ai-2115198100465697038]]
- [[2026-10-26-voxyz_ai-2114839487574315517]]
- [[2026-10-26-voxyz_ai-2114746374059381186]]
- [[2026-10-22-voxyz_ai-2113254050170843418]]
- [[2026-10-22-luinlee-2113085361836744764]]
- [[2026-10-22-cu30rry-2113242716473602270]]
- [[2026-10-16-poteto-2111133080526495985]]
- [[2026-10-16-niklas-steenfatt-vibe-coding-hat-sich-veraendert]]
- [[2026-10-13-mattpocockuk-2109973273924579720]]
- [[2026-10-05-repo-mattpocock-skills-retro]]
- [[2026-10-05-repo-claude-code-doctor-insights]]
- [[2026-10-04-voxyz_ai-2106829206134931539]]
- [[2026-10-04-mattpocockuk-2106729173511188654]]
- [[2026-08-14-mattpocockuk-2088256432265167185]]
- [[2026-08-04-anthropic-docs-claude-code-best-practices]]
- [[2026-07-30-floknowsai-ki-gibt-dir-das-gefuehl-dass-du-so-schnell-wie-noch-nie-arbeitest]]
- [[2026-07-24-claude-the-new-rules-of-context-engineering-for-claude]]
- [[2026-07-15-xudong07452910-2077246527756775933]]
- [[2026-07-12-agenticjames-claude-codes-new-feature-checkup-makes-claude-more-token-efficient-and]]
- [[2026-07-08-bcherny-2074997570317779038]]
- [[2026-06-06-agenticjames-your-agent-is-referencing-documentation-when-it-should-be-reading-the]]
- [[2026-03-29-julian-ivanov-ki-automat-obsidian-claude-code-so-baust-du-dein-zweites-ge]]
- [[2026-02-24-nate-b-jones-intent-engineering]]
- [[2026-02-05-kloss-xyz-feature-intelligence-architect]]
- [[2026-02-04-rudrank-using-minimax-with-claude-code]]
