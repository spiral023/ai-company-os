---
url: https://www.humanlayer.dev/blog/writing-a-good-claude-md
autor: "Kyle (HumanLayer)"
datum: 2026-02-01
erfasst: 2026-07-13
typ: artikel
---

# Kyle (HumanLayer) zu „Writing a good CLAUDE.md“

## Inhalt

Primärquelle, deren Kerninhalte bereits über eine RAITEC-Sekundärsynthese ([[2026-04-13-wiki-compiler-gute-agents-md-schreiben]]) erfasst waren. Diese Notiz ergänzt konkrete, in der Sekundärquelle fehlende Details.

Claude Code injiziert einen expliziten System-Reminder, der besagt, dass CLAUDE.md-Kontext möglicherweise nicht relevant ist und ignoriert werden soll, wenn nicht „hochgradig relevant“ — wörtlich zitiert: „IMPORTANT: this context may or may not be relevant to your tasks. You should not respond to this context unless it is highly relevant to your task.“ Das erklärt konkret, WARUM zu viel Inhalt in CLAUDE.md kontraproduktiv ist: das Modell selbst wird angewiesen, irrelevant wirkenden Kontext zu verwerfen.

Konkrete Forschungsangaben zum Instruction-Following: Frontier-Thinking-LLMs befolgen ~150-200 Instruktionen mit vernünftiger Konsistenz; kleinere Modelle degradieren bei steigender Instruktionszahl exponentiell schneller; LLMs bevorzugen Instruktionen am Anfang und Ende des Prompts; mit steigender Instruktionszahl sinkt die Befolgungsqualität gleichmäßig für ALLE Instruktionen, nicht nur die neuen. Da der Claude-Code-System-Prompt bereits ~50 Instruktionen enthält, bleibt wenig Spielraum. Konkrete Längenempfehlung: genereller Konsens < 300 Zeilen, HumanLayer selbst nutzt < 60 Zeilen.

Progressive Disclosure konkret: separates `agent_docs/`-Verzeichnis (`building_the_project.md`, `running_tests.md`, `code_conventions.md`, `database_schema.md`), in CLAUDE.md nur mit kurzer Beschreibung gelistet, Claude entscheidet selbst welche relevant sind. Referenzen (`file:line`) statt Code-Snippet-Kopien, damit nichts veraltet. Explizite Warnung: kein `/init` oder auto-generierte CLAUDE.md nutzen, da die Datei den höchsten Hebel im gesamten Harness hat — jede Zeile sollte bewusst von Hand geschrieben werden.

## Kernaussagen

- Claude Code injiziert einen expliziten System-Reminder, der das Modell anweist, CLAUDE.md-Inhalt zu ignorieren, wenn er nicht hochgradig relevant wirkt — das ist der technische Grund, warum überladene Agent-Dateien nicht nur nutzlos, sondern aktiv kontraproduktiv werden → [[AGENTS-md-Onboarding-Design]]
- Konkrete Zahl: Claude-Code-System-Prompt selbst verbraucht bereits ~50 der ~150-200 zuverlässig befolgbaren Instruktionen, bevor die Agent-Datei überhaupt geladen wird → [[AGENTS-md-Onboarding-Design]]
- Explizite Empfehlung gegen `/init`/auto-generierte CLAUDE.md-Dateien: die Datei hat den höchsten Hebel im ganzen Harness, jede Zeile sollte bewusst von Hand geschrieben werden → [[AGENTS-md-Onboarding-Design]]
