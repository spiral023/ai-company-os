---
url: https://x.com/trq212/status/2027463795355095314
autor: "Thariq (@trq212, Anthropic)"
datum: 2026-02-27
erfasst: 2026-07-13
typ: tweet
---

# Thariq zu „Lessons from Building Claude Code: So lernst du, wie ein Agent zu sehen“

## Inhalt

Kernbegriff: der **Action Space** — die Menge an Dingen, die ein Agent praktisch tun kann. These: Gute Agent-Systeme entstehen nicht durch mehr Tools, sondern durch Tools, die zur tatsächlichen Denk-/Arbeitsweise des Modells passen. Analogie: ein schweres Matheproblem — Papier hilft begrenzt, ein Taschenrechner mehr (braucht Bedienkompetenz), ein Computer am meisten (verlangt operative Fähigkeiten). Zu viele Tool-Optionen erhöhen Entscheidungs-/Fehlerlast, zu wenige limitieren den Handlungsspielraum.

Drei Fallstudien aus der Claude-Code-Entwicklung:
1. **AskUserQuestion-Tool**: Erst wurde versucht, Rückfragen als Parameter in ein bestehendes ExitPlanTool zu packen (Plan/Fragen vermischten sich, Ablauf unklar) — scheiterte. Dann wurde versucht, per Prompting ein parsbares Markdown-Frageformat zu erzwingen — scheiterte an Formatinstabilität. Erst ein explizites, eigenes Tool (mit Modal, das den Loop blockiert bis zur Antwort) funktionierte, weil es strukturierten Output erzwingt und das Modell es „gern und zuverlässig“ nutzt. „Das beste Tool ist wertlos, wenn das Modell nicht versteht, wann und wie es es aufrufen soll.“
2. **Capability-Drift, Todos → Tasks**: Frühe Modelle brauchten explizite Todo-Listen (TodoWrite) plus periodische System-Reminders, um auf Kurs zu bleiben. Mit stärkeren Modellen wurden Reminders störend und starre Todo-Listen limitierend, während Subagents stärker wurden aber bessere Koordination brauchten — Ergebnis: Wechsel zum Task-Tool (Abhängigkeiten, Updates über Subagents hinweg, editier-/löschbar). Ein Tool, das 2025 nötig war, kann 2026 ein Bottleneck sein.
3. **Kontextaufbau-Evolution**: von RAG-Vector-DB (fragil, Setup-lastig) über Agent-Self-Search mit Grep zu Progressive Disclosure (Agent liest eine relevante Datei, die auf weitere verweist, traversiert schrittweise tiefer statt alles upfront zu laden) — reduziert Context Rot. Zusätzliches Pattern: ein spezialisierter **Guide-Subagent** für Selbstfragen über Claude Code selbst (statt alles in den System Prompt zu kippen) erweitert den Action Space funktional, ohne den globalen Tool-Space aufzublähen.

Fazit des Autors: Tool-Design ist „an Art, not a Science“ — modell-, ziel- und umgebungsabhängig, es gibt keine statische Regelbibliothek. Fünf ableitbare Regeln: Tools nur bei diagnostizierter Verhaltenslücke hinzufügen; Interfaces robust machen (Tool-Verträge statt freies Markdown-Prompting); Tool-Nutzung messen, nicht nur Verfügbarkeit; Capability-Reviews als Routine (alte Hilfskonstrukte können bei stärkeren Modellen regressiv wirken); Progressive Disclosure als Standard für Kontext.

## Kernaussagen

- Action-Space-Design bedeutet, Tools an das tatsächliche Fähigkeitsprofil des Modells anzupassen statt Feature-Parität anzustreben — zu viele Optionen erhöhen Fehlerlast, zu wenige limitieren Handlungsspielraum → [[Action-Space-Design-nach-Modellfaehigkeit]]
- Tool-Entscheidungen müssen bei jedem Modell-Upgrade aktiv hinterfragt werden: ein 2025 nötiges Hilfskonstrukt (starre Todo-Liste, Reminder) kann 2026 ein Bottleneck sein (Beispiel Todos → Task-Tool) → [[Action-Space-Design-nach-Modellfaehigkeit]]
- Wenn Formattreue kritisch ist, gehört sie in ein robustes Tool/Interface, nicht in Freitext-Prompting — drei gescheiterte Anläufe beim AskUserQuestion-Tool zeigen das konkret → [[Action-Space-Design-nach-Modellfaehigkeit]]
- Progressive Disclosure beim Kontextaufbau (Datei liest zu Datei, statt alles upfront zu laden) reduziert Context Rot; spezialisierte Guide-Subagents erweitern den Action Space, ohne den globalen Tool-Space aufzublähen → [[Action-Space-Design-nach-Modellfaehigkeit]], [[Kontext-Hygiene-Entscheidungsbaum]]
