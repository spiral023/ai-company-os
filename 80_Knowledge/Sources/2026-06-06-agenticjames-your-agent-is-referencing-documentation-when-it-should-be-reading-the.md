---
url: https://www.tiktok.com/@agentic.james/video/7648227434789195022
autor: "@agentic.james"
datum: 2026-06-06
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-06-06-agenticjames-your-agent-is-referencing-documentation-when-it-should-be-reading-the.md
thema: Tools & Releases
zeitkritisch: nein
---

# Dependency-Quellcode lokal ablegen statt Agent nur Doku lesen lassen

Ein einminütiges Erfahrungsvideo empfiehlt `opensrc` von Vercel Labs: Das Tool holt den vollständigen Quellcode von Open-Source-Dependencies in das Projekt, sodass ein Coding Agent gegen echten Code statt gegen Dokumentation entwickelt. Zusätzlich schlägt der Autor vor, `graphify` über diese Sourcen laufen zu lassen. Es handelt sich um eine selbstberichtete Tool-Empfehlung ohne Messung, ohne Beispiel und ohne Zahlen; das Cover zeigt nur den Sprecher mit einer Texteinblendung.

## Die Argumentation

- Agents ziehen bei Open-Source-Bibliotheken meist nur die Dokumentation. Code gilt dem Autor als die bessere Referenz, weil Doku unvollständig oder veraltet sein kann und der Agent sonst rät.
- Fast jedes Projekt hängt an Open-Source-Dependencies, der Effekt betrifft also den Normalfall.
- `opensrc` legt die Dependency-Repos lokal im Projekt ab, der Agent kann sie beim Schreiben von Code durchsuchen.
- Kombination mit `graphify`: Aus dem Code der Dependencies entsteht ein Knowledge Graph, der als durchsuchbare Wissensbasis dient, während der Agent arbeitet.

## Einordnung

Die Grundidee (Primärquelle Code vor Sekundärquelle Doku) ist plausibel, der Nutzen im Video aber nur behauptet. Offen bleiben Kosten: Vollständige Dependency-Repos vergrößern Suchraum und Repository, erzeugen Rauschen in Grep-Treffern und können Token verbrauchen, wenn der Agent breit liest. Die Graph-Erzeugung über viele Dependencies kostet zusätzlich Zeit und Tokens, und ob sie gegenüber gezieltem Lesen der relevanten Dateien besser abschneidet, zeigt das Video nicht. Versionsgleichheit zwischen lokal abgelegtem Code und tatsächlich installierter Version ist eine Voraussetzung, die die Quelle nicht anspricht. Das Video endet mit einem Comment-Trigger („Comment OPEN SOURCE“), also Reichweitenmarketing.

## Kernaussagen

- Bei Dependencies den Quellcode statt nur die Doku als Referenz bereitstellen, damit der Agent nicht rät → [[Kontext-Hygiene-Entscheidungsbaum]]
- Lokal abgelegter Fremdcode plus Knowledge Graph als durchsuchbare Wissensbasis (unbelegt, Kosten ungeklärt) → [[Kontext-Hygiene-Entscheidungsbaum]]

## Verbindungen

- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[MCP-Code-Execution-statt-Tool-Definitionen]]
- [[2026-04-22-agenticjames-everything-you-need-to-know-about-context-engineering-in-1-minute]]
- [[2026-08-14-agenticjames-ai-memory-is-trash-heres-some-solutions]]
