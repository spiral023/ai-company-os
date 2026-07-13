# Intent-Engineering-als-dritte-Schicht

**Konfidenz:** meinung

## Zweck

Verhindert, dass ein technisch fähiger, gut informierter Agent trotzdem das Falsche optimiert, weil ihm die organisatorische Zielhierarchie fehlt. Adressiert, warum hohe Investition in AI und sichtbare Aktivität nicht automatisch zu Unternehmenswert führen.

## Funktionsweise

Drei Entwicklungsstufen werden unterschieden: **Prompt Engineering** (Anweisung im Chatfenster, skaliert in Unternehmen begrenzt, personenabhängig), **Context Engineering** (Informationsgrundlage: RAG, Tool-Zugriffe, Wissensobjekte, Rechtekonzepte — löst aber nicht das Zielproblem, ein Agent kann alles Relevante wissen und trotzdem falsch priorisieren) und **Intent Engineering** als dritte, meist fehlende Schicht: Ziele, Werte, Prioritäten, Eskalationsregeln und Entscheidungsschranken werden so strukturiert, dass ein Agent danach handeln kann. Konkret heißt das: welche Metrik führt, welche nur sekundär ist; welche Trade-offs erlaubt sind (z.B. Speed vs. Qualität); wann eskaliert werden muss; welche Aktionen erlaubt/verboten sind; wie Drift erkannt und korrigiert wird. Menschen balancieren solche Zielkonflikte implizit (mehr Zeit bei heiklen Fällen, bewusstes Eskalieren, kontrolliertes Regelbiegen) — ein Agent ohne expliziten Intent hat dafür kein Entscheidungsmodell und optimiert stattdessen zuverlässig die lokal messbare Metrik, selbst wenn das dem eigentlichen Zweck schadet.

## Vorteile

- Erklärt einen sonst schwer greifbaren Effekt: ein Agent kann technisch sehr gut sein und trotzdem strategisch schaden, weil ihm die Zielhierarchie fehlt — nicht nur mehr Kontext, sondern mehr Zielklarheit ist der Hebel.
- Macht sichtbar, warum breite AI-Adoption ohne übersetzten Intent Aktivität ohne nachhaltige Wirkung erzeugt.
- Liefert konkrete Ansatzpunkte (Metrik-Priorität, Trade-off-Regeln, Eskalationsschwellen, Drift-Erkennung), die sich in Governance/Prompt-Design operationalisieren lassen.

## Nachteile & Grenzen

- Intent explizit zu formalisieren ist aufwendig, weil entscheidendes Wissen oft „tacit knowledge“ ist — implizit, historisch gewachsen, selten aufgeschrieben.
- Erfordert Zusammenarbeit zwischen Strategie/Business und Engineering, die in vielen Organisationen kulturell getrennt arbeiten.
- Das Konzept ist noch jung (Autor beschreibt es selbst als neu) — es gibt bislang keine etablierten Standard-Frameworks zur Umsetzung.

## Wann einsetzen, wann nicht

- Einsetzen: geschäftskritische Agenten-Workflows mit echten Zielkonflikten (Kundenkontakt, Automatisierung mit KPI-Druck, Enterprise-Rollouts).
- Nicht einsetzen: einzelne, klar abgegrenzte technische Coding-Aufgaben ohne Zielkonflikt — dort reichen Prompt- und Context Engineering meist aus.

## Belege

- 2026-02-24 · [[2026-02-24-nate-b-jones-intent-engineering]] · meinung — Video-Analyse beschreibt die drei Entwicklungsstufen, das Klarna-Fallbeispiel (853 FTE ersetzt, ~60 Mio. USD gespart, aber Kundenerlebnis/Marke beschädigt) und das Microsoft-Copilot-Gegenbeispiel (breite Adoption, stagnierende Nutzung).

## Spannungen & offene Fragen

- Einzige bisherige Quelle ist eine Video-Analyse eines einzelnen Autors, keine unabhängige Zweitquelle.
- Offene Frage: Wie lässt sich Intent Engineering konkret in unser eigenes AGENTS.md-System übertragen — reicht die bestehende „Freigabe durch Philipp erforderlich“-Liste als Intent-Schicht, oder fehlt die explizite Trade-off-/Eskalationslogik dahinter?

## Verwandte Patterns

- [[Fable-Unknowns-vor-Prompt-Qualitaet]]
- [[AGENTS-md-Onboarding-Design]]
