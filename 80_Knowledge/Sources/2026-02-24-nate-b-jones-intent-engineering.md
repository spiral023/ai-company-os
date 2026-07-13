---
url: https://www.youtube.com/watch?v=QWzLPn164w0
autor: "Nate B. Jones (AI News & Strategy Daily)"
datum: 2026-02-24
erfasst: 2026-07-13
typ: video
---

# Nate B. Jones zu „Intent Engineering: Warum Prompt- und Context-Optimierung allein nicht mehr reichen“

## Inhalt

Kernthese: In Enterprise-AI ist nicht mehr das Modell der Engpass, sondern fehlende Ausrichtung auf den eigentlichen Unternehmenszweck. „Kontext sagt der AI, was sie wissen soll. Intent sagt ihr, was sie wollen soll.“

Klarna als Warnsignal: Der AI-Customer-Service-Agent übernahm Arbeit im Umfang von 853 FTE, sparte ~60 Mio. Dollar — gleichzeitig litten laut Management Kundenerlebnis, Vertrauen und Markenwirkung. Der Agent war nicht schlecht, sondern zu gut darin, die falsche Metrik zu optimieren (kurze Bearbeitungszeit/hohe Abschlussquote statt langfristiger Kundenbeziehung). Menschen balancieren solche Zielkonflikte implizit (mehr Zeit bei heiklen Fällen, bewusstes Eskalieren) — ein Agent ohne expliziten Intent hat dafür kein Entscheidungsmodell.

Drei Entwicklungsstufen: (1) Prompt Engineering — skaliert in Unternehmen begrenzt, personenabhängig. (2) Context Engineering — RAG, Tool-Zugriffe, Wissensobjekte, Rechtekonzepte; löst aber nicht das Zielproblem, ein Agent kann alles Relevante wissen und trotzdem falsch priorisieren. (3) Intent Engineering — Ziele, Werte, Prioritäten, Eskalationsregeln, Entscheidungsschranken werden maschinenlesbar strukturiert: welche Metrik führt, welche Trade-offs erlaubt sind, wann eskaliert werden muss, welche Aktionen verboten sind, wie Drift erkannt wird.

Microsoft Copilot als zweites Beispiel: breite Einführung, aber stagnierende Nutzung — Analogie: tausende neue Mitarbeitende einstellen, ohne ihnen je zu sagen, was wichtig ist und welche Entscheidungen sie treffen dürfen.

Drei systemische Ebenen, auf denen Unternehmen scheitern: Unified Context Infrastructure (Governance/Berechtigungen), Coherent AI Worker Toolkit (gemeinsame Workflows statt individueller Tool-Bastelei), Intent Engineering im engeren Sinn (maschinenlesbare Erfolgssignale, erlaubte/verbotene Aktionsräume, Eskalationsschwellen, Drift-Feedback-Loops).

## Kernaussagen

- Ein Agent kann vollständigen Kontext haben und trotzdem scheitern, wenn ihm Zielhierarchie und Trade-off-Logik (Intent) fehlen — Klarna optimierte die falsche Metrik perfekt und beschädigte dabei Kundenbeziehung/Marke → [[Intent-Engineering-als-dritte-Schicht]]
- Intent Engineering als dritte Schicht nach Prompt- und Context Engineering: explizite Ziele, erlaubte/verbotene Aktionen, Eskalationsschwellen und Drift-Erkennung machen aus einem „fähigen“ Agenten einen organisatorisch ausgerichteten Agenten → [[Intent-Engineering-als-dritte-Schicht]]
- Breite AI-Adoption ohne übersetzten Intent erzeugt Aktivität ohne nachhaltige Wirkung (Copilot-Beispiel: viel Nutzung, wenig Outcome) → [[Intent-Engineering-als-dritte-Schicht]]
