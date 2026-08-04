---
url: https://code.claude.com/docs/en/features-overview
titel: "Extend Claude Code"
autor: "Anthropic Docs"
datum: 2026-02-01
erfasst: 2026-08-04
typ: url
quelle: vibedeck
sekundaerquelle: true
status: neu
beschreibung: "Verstehe, wann du CLAUDE.md, Skills, Subagents, Hooks, MCP und Plugins verwenden solltest."
vibedeck_category: fundamentals
vibedeck_tags:
  - "tooling/claude-code"
  - "fundamentals/extension"
  - "workflows/customization"
vibedeck_topics:
  - "[[Claude Code]]"
  - "[[CLAUDE.md]]"
  - "[[Skills]]"
  - "[[MCP]]"
  - "[[Subagents]]"
  - "[[Hooks]]"
---

# Extend Claude Code

> Sekundärquelle: aus vibedeck übernommene deutsche Aufarbeitung (`src/content/knowledge/extend-claude-code.md`). Primärquelle: https://code.claude.com/docs/en/features-overview

Claude Code kombiniert ein Modell, das über deinen Code nachdenkt, mit eingebauten Tools. Die "Extension Layer" ermöglicht es dir, Claude an deine Bedürfnisse anzupassen.

## Überblick der Erweiterungen

*   **[CLAUDE.md](/knowledge/writing-a-good-claude-md):** Persistenter Kontext, den Claude in jeder Session sieht.
*   **Skills:** Wiederverwendbares Wissen und aufrufbare Workflows.
*   **MCP:** Verbindung zu externen Diensten (Datenbanken, Slack).
*   **Subagents:** Isolierte Worker, die eigene Loops ausführen und Zusammenfassungen zurückgeben.
*   **Hooks:** Deterministische Skripte, die bei Events (z.B. Datei-Edit) laufen.
*   **Plugins:** Bündeln diese Features zur Distribution.

## Wann nutze ich was?

| Feature | Zweck | Wann nutzen? | Beispiel |
| :--- | :--- | :--- | :--- |
| **CLAUDE.md** | Immer aktiver Kontext | Projekt-Konventionen, "Immer X tun" Regeln | "Nutze pnpm statt npm." |
| **Skill** | Wissen & Workflows | Referenzmaterial, wiederholbare Tasks | `/review` führt Checklist aus; API Docs |
| **Subagent** | Isolierter Kontext | Aufgaben mit vielen Datei-Reads, parallele Arbeit | Recherche, die viele Dateien liest |
| **MCP** | Externe Dienste | Externe Daten oder Aktionen | Datenbank abfragen, Browser steuern |
| **Hook** | Skripte bei Events | Deterministische Automatisierung | ESLint nach jedem Edit ausführen |

### Vergleich ähnlicher Features

#### Skill vs. Subagent
*   **Skill:** Wissen, das in jeden Kontext geladen werden kann.
*   **Subagent:** Isolierter Arbeiter.
*   **Kombination:** Ein Subagent kann Skills laden.

#### CLAUDE.md vs. Skill
*   **CLAUDE.md:** Wird **immer** geladen. Gut für Regeln, die immer gelten.
*   **Skill:** Wird **bei Bedarf** geladen. Gut für Referenzen oder spezifische Workflows (`/deploy`).
*   **Regel:** Halte `CLAUDE.md` unter ~500 Zeilen. Lagere den Rest in Skills aus.

#### MCP vs. Skill
*   **MCP:** Stellt die **Verbindung/Tools** bereit.
*   **Skill:** Lehrt Claude, **wie** man die Tools nutzt.

## Kontext-Kosten verstehen

Jedes Feature verbraucht Kontext.

| Feature | Wann geladen? | Was wird geladen? | Kontext-Kosten |
| :--- | :--- | :--- | :--- |
| **CLAUDE.md** | Session Start | Vollständiger Inhalt | Jeder Request |
| **Skills** | Start + Nutzung | Beschreibung (Start), Inhalt (Nutzung) | Gering (außer bei Nutzung) |
| **MCP** | Session Start | Tool-Definitionen & Schemas | Jeder Request (via Tool Search optimiert) |
| **Subagents** | Bei Spawn | Frischer Kontext | Isoliert (belastet Haupt-Session nicht) |
| **Hooks** | Bei Trigger | Nichts (extern) | Null |

> **Tipp:** Nutze `disable-model-invocation: true` für Skills, die nur manuell aufgerufen werden sollen, um Kontext zu sparen.

## Wie Features laden

*   **CLAUDE.md:** Additiv. Dateien vom aktuellen Verzeichnis bis zum Root werden geladen.
*   **Skills & Subagents:** Überschreiben nach Name (Managed > User > Project).
*   **MCP:** Überschreiben nach Name (Local > Project > User).
*   **Hooks:** Mergen (alle Hooks feuern).

## Kombinationen (Patterns)

*   **Skill + MCP:** MCP verbindet zur DB, Skill erklärt das Schema.
*   **Skill + Subagent:** `/review` Skill startet Subagents für Security und Style.
*   **CLAUDE.md + Skills:** `CLAUDE.md` verweist auf API-Konventionen, Skill enthält den Styleguide.
*   **Hook + MCP:** Hook sendet Slack-Nachricht via MCP nach wichtigem Edit.

## Verbindungen
- [[Claude Code]]
- [[CLAUDE.md]]
- [[Skills]]
- [[Model Context Protocol]]
- [[Subagents]]
- [[Hooks]]
- [[Prompt Engineering]]
- [[Workflow Automation]]
