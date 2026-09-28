---
url: https://www.tiktok.com/@agentic.james/video/7674000398218284302
autor: "@agentic.james"
datum: 2026-08-14
erfasst: 2026-08-29
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-08-14-agenticjames-ai-memory-is-trash-heres-some-solutions.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Vier Speicher-Ansätze für Agent Memory nach Anwendungsfall

Ein 2:28-Minuten-TikTok, das Agent Memory nicht als ein Problem, sondern als vier getrennte Probleme mit jeweils eigener Lösung sortiert. Die Quelle ist eine Übersicht aus dem Gedächtnis des Autors, ohne Messwerte, Kosten oder Vergleiche; belastbar ist höchstens die Einteilung, nicht die Empfehlung einzelner Tools. Das Cover zeigt nur Titel und Untertitel, keine zusätzlichen Inhalte.

## Vier Probleme, vier Mechanismen

- **Wissen und Ergebnisse ablegen:** Dateien und Ordner plus ein Knowledge-Graph-Werkzeug (genannt: Obsidian-Wiki, das Open-Source-Repo Graphify). Nach Aussage des Autors deckt das die meisten einfachen Fälle ab, vor allem bei interaktiver Arbeit, in der das Warten auf die Suche im Graphen akzeptabel ist.
- **Einzelne Gesprächsturns wiedererkennen:** Für Chat-Historie reichen Dateien und Graph laut Autor nicht, weil zu viel Text anfällt. Der Hermes Agent indexiert alle vollständigen Chat-Transkripte in eine Vektordatenbank, und der Agent sucht per semantischer Suche darin.
- **Audio und Video durchsuchbar machen:** Ein multimodales Embedding-Modell (genannt: Google „Gemini Embeddings 2“) legt Video, Bild, Audio und Text im selben Vektorspeicher ab, sodass nach Bedeutung gesucht werden kann. Der Autor bewirbt dafür ein eigenes Plug-in in seiner Community.
- **Latenz umgehen:** Wer nicht auf das Abrufen warten will, setzt programmatische Hooks im Harness. Beim Start und vor jeder Antwort-Runde wird eine Zusammenfassung relevanter Erinnerungen aus der Wissensbasis in das Context Window injiziert.

Die Auswahl hängt laut Autor vom Einsatzzweck des Agenten ab; oft kombiniert man mehrere Mechanismen.

## Einordnung

Nützlich ist die Achse „Abrufzeitpunkt“: Pull (Agent sucht selbst) gegenüber Push (Hook injiziert vorab). Push spart Suchschritte, kostet aber bei jedem Turn Token und kann irrelevanten Kontext einschleusen; die Quelle nennt diese Kosten nicht. Die Aussagen zu Hermes und Gemini Embeddings 2 sind unbelegt, und die Eigenwerbung für das Plug-in färbt die Darstellung. Der Wiki-plus-Graph-Ansatz entspricht dem, was dieses Repo ohnehin nutzt, und ist damit keine neue Arbeitsweise.

## Kernaussagen

- Agent Memory zerfällt in Ablage, Turn-Erinnerung, multimodale Suche und Timing; ein einzelner Mechanismus deckt nicht alle ab. → [[Kontext-Hygiene-Entscheidungsbaum]]
- Hooks, die beim Sessionstart und pro Turn relevanten Kontext injizieren, ersetzen die Suche durch den Agenten. → [[Hook-erzwungene-Skill-Aktivierung]]
- Dateien plus Wiki/Graph genügen für interaktive Arbeit, bei der Suchlatenz tolerierbar ist. → [[Klein-und-komposierbar]]

## Verbindungen

- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Hook-erzwungene-Skill-Aktivierung]]
- [[2026-04-22-agenticjames-everything-you-need-to-know-about-context-engineering-in-1-minute]]
- [[2026-01-06-jarrodwatts-context-engineering-guide]]
