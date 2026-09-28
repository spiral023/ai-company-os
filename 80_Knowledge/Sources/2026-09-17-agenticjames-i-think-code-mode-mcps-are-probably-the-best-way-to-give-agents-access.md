---
url: https://www.tiktok.com/@agentic.james/video/7686584043177135373
autor: "@agentic.james"
datum: 2026-09-17
erfasst: 2026-09-17
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-09-17-agenticjames-i-think-code-mode-mcps-are-probably-the-best-way-to-give-agents-access.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Code-Mode-MCP: ein Skript-Tool statt vieler vordefinierter MCP-Tools

Ein 97-Sekunden-Pitch dafür, MCP-Server nicht mehr einzeln, sondern hinter einem „Code Mode“-Gateway anzubinden. Die Kernaussage ist plausibel und deckt sich mit bekannten Ansätzen zur Tool-Token-Reduktion, wird im Video aber nur behauptet: Es gibt keine Messwerte, keine Demo und keine Vergleichszahlen. Der Autor bewirbt zudem einen eigenen kostenpflichtigen Kurs in seiner Community.

## Das Prinzip

Ein Code-Mode-Gateway stellt dem Agenten nur ein einziges MCP-Tool bereit, das ein Skript ausführt. Dieses Skript ruft dahinter die eigentlichen MCP-Tools auf. Der Ablauf laut Video: Der Agent sucht zuerst die benötigten Tools, generiert dann ein maßgeschneidertes Skript und führt damit mehrere Tool-Aufrufe in einem einzigen MCP-Call aus.

## Die zwei genannten Vorteile

- **Komposierbarkeit:** Der Agent baut sich den Aufruf passend zur Aufgabe, statt auf feste Tool-Signaturen beschränkt zu sein. Mehrere Tools lassen sich in einem Schritt verketten.
- **Weniger Context-Verbrauch:** Das Skript kann die Ausgabe filtern, bevor sie ins Context Window gelangt. Ein großer JSON-Body landet so nicht ungefiltert im Kontext. Bei klassischen MCP-Servern mit festen Tools hat der Agent darauf keinen Einfluss.

Als Abgrenzung zu CLI-Tools nennt der Autor: Auch CLIs sind komposierbar, aber ein Code-Mode-MCP bleibt ein MCP-Tool, dessen Beschreibung automatisch in den Kontext geladen wird. Der Agent weiß also ohne weiteres Zutun, dass es existiert („MCP und CLI hatten ein Baby“).

## Genannte Umsetzung

Der Autor nutzt das Gateway `executor` (laut seiner Aussage kostenlos und selbst hostbar), hinter dem er sich bei allen seinen MCP-Servern anmeldet. Er erwähnt außerdem, dass Docker ein eigenes Code-Mode-Gateway hat. Beides ist unverifiziert; Stand der Angaben: 2026-09-17.

## Einordnung

Das Muster ist nicht neu, sondern dasselbe Prinzip wie Code Execution mit MCP: Tools als aufrufbare Schnittstelle statt als vorgeladene Definitionen, Filterung im Code statt im Kontext. Belastbar ist der Mechanismus (Ausgabefilterung, Tool-Verkettung), nicht die implizite Behauptung, es sei „the best way“. Nicht genannte Kosten: Das Skript muss in einer Sandbox laufen, der Agent muss Tools zuerst per Suche entdecken (zusätzlicher Schritt), generierter Code kann fehlerhaft sein, und ein weiteres Gateway ist eine zusätzliche Vertrauens- und Wartungsstelle, die Zugangsdaten zu allen angeschlossenen Servern bündelt.

## Kernaussagen

- Ein Skript-Tool vor vielen MCP-Tools macht Aufrufe komposierbar und erlaubt Ausgabefilterung vor dem Context Window → [[MCP-Code-Execution-statt-Tool-Definitionen]]
- Ausgaben im Code zu filtern hält große Antworten aus dem Kontext fern → [[Kontext-Hygiene-Entscheidungsbaum]]

## Verbindungen

- [[MCP-Code-Execution-statt-Tool-Definitionen]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[2026-02-01-anthropic-docs-connect-claude-code-to-mcp]]
- [[2026-04-22-agenticjames-everything-you-need-to-know-about-context-engineering-in-1-minute]]
