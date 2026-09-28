---
url: https://www.youtube.com/watch?v=bKt-GZicIlM
autor: Alex Sprogis
datum: 2026-08-30
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-08-30-alex-sprogis-loop-graph-engineering-das-letzte-video-was-du-s.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Loop Engineering und Graph Engineering: Erfolgskriterien, unabhängige Prüfer und Artefakt-Übergaben

Alex Sprogis ordnet die Begriffe „Loop Engineering“ und „Graph Engineering“ ein und zeigt, wie er sie in einem spec-driven Workflow mit Claude Code (Opus 4.7, Stand der Videobeschreibung) einsetzt. Kernaussage: Ein Agent braucht nicht nur den Auftrag, sondern ein binär prüfbares Erfolgskriterium, und die Prüfung muss von einer anderen Instanz kommen als die Umsetzung. Das Video ist eine Praxisschilderung ohne Messwerte; die Belastbarkeit beruht auf der Erfahrung des Autors. Es enthält Werbung (Konferenz, eigenes Kursprogramm).

## Bestandteile eines Loops

Jeder Loop hat drei Teile: Startkriterium (manuell, Zeitplan oder Ereignis), Aufgabe und Erfolgskriterium. Entscheidend ist das dritte, und es muss sich mit Ja oder Nein beantworten lassen, etwa „alle Tests grün“ oder „alle Akzeptanzkriterien im Testbericht auf bestanden“. Bei Interpretationsspielraum trifft der Agent eigene Annahmen und dreht unnötige Runden, was Tokens kostet. Als Quelle für die Loop-Typen nennt er einen Anthropic-Artikel, den er nur verlinkt und nicht im Detail wiedergibt.

## Vier Loop-Typen

- **Turn-based:** Der Agent entscheidet selbst, wann er fertig ist. Umsetzbar allein per Skill-Datei mit Regel „bei Fehlschlag beheben und bei Schritt 1 neu starten“. Sprogis' Build-Skill verlangt, dass jeder neue Test einmal rot gewesen sein muss: Erwartung bewusst umdrehen oder die geprüfte Logik kurz entfernen, Fehlschlag bestätigen, wiederherstellen, dann grün. Schwäche: Der Agent entwickelt und verifiziert zugleich und kennt den Weg, prüft also weniger scharf. Gegenmittel ist ein QA-Skill, der an einen Reviewer-Agent mit eigenem Kontext übergibt, der nur Spezifikation und Ergebnis sieht.
- **Goal-based:** Über `/goal` mit messbarem Ziel und Iterationslimit, z. B. Feature-ID, „alle Akzeptanzkriterien implementiert und im Testbericht bestanden“, Status `approved`, maximal fünf Durchläufe. Die Akzeptanzkriterien der Spezifikation (Format „Angenommen X, wenn Y, dann Z“, feste IDs) liefern das Erfolgskriterium, bevor Code entsteht.
- **Time-based:** Startet per Intervall oder Uhrzeit. `/loop` läuft lokal, `/schedule` in der Anthropic Cloud, auch bei ausgeschaltetem Rechner. Beispiel: stündlicher `/audit`, der prüft, ob Code und Spezifikation zusammenpassen; Variante 1 nur Bericht, Variante 2 mit Fix-Erlaubnis auf eigener Branch, nie auf `main`, maximal drei Durchläufe, Spezifikation schreibgeschützt, spezifikationsloser Code wird nur gemeldet.
- **Proaktiv:** Ereignisgetrieben (z. B. neuer Pull Request), ohne dass du beteiligt bist. Stufenweise Autonomie: Zwischenergebnisse anfangs selbst ansehen, erst dann laufen lassen.

## Reward Hacking und Gegenregeln

Beim Ziel „alle Tests grün“ ist der kürzeste Weg, Tests zu löschen oder wirkungslos zu konfigurieren. Ein sauberes Kriterium reicht nicht; zusätzlich muss festgelegt sein, wer die Erfüllung prüft, und das darf nicht der umsetzende Agent sein. Sprogis' Regeln: Spezifikation während Bau und Testschreiben schreibgeschützt; Build- und Test-Agent getrennt; QA findet Bugs, behebt sie aber nicht; Subagents melden nie selbst „fertig“, das bewertet der Hauptagent; Prüfszenarien werden vor der Umsetzung geschrieben und dem Entwickler-Agent nie gezeigt.

## Graph Engineering und Dark Software Factory

Ein Gesamtauftrag (Architektur, Aufgabenplan, Umsetzung, Test, Deployment) in einem Context Window führt zu Context Rot. Stattdessen läuft jeder Schritt als eigener Loop mit frischem Kontext; übergeben werden nur Artefakte (Spezifikation, Architektur, Aufgabenplan, Umsetzungsergebnis, Testbericht), nicht die Zwischenschritte. Knoten sind Loops, Agents oder Subagents, Kanten die Artefakte. Nicht zu verwechseln mit Knowledge Graphs. Er verweist auf LangGraph als etablierte Bibliothek dafür.

Die „Dark Software Factory“ ist ein Repository, das seinen Code selbst ausliefert: Warteschlange freigegebener Spezifikationen, Time-based Loop als Takt, Eingangsprüfung (darf ablehnen oder teilen), Planung mit unabhängiger Verifikation, Goal-based Umsetzung, getrennter Reviewer, Auslieferung per PR oder Deploy. Nötig sind eine Eskalationsmöglichkeit zum Menschen und ein minimaler gemeinsamer Zustand (z. B. Datenbank mit Statusfeldern). Er beschreibt das Konzept, baut es im Video nicht.

## Einordnung

Belastbar ist die Argumentationslinie: binäres Erfolgskriterium, Trennung von Umsetzung und Prüfung, Artefakt-Übergaben statt langer Kontexte. Sie deckt sich mit bekannten Mustern (Test-first, frischer Kontext pro Iteration, unabhängiger Review) unter neuem Etikett. Alle Aussagen zur Wirksamkeit sind selbstberichtet, ohne Vergleichsmessung. Kosten: Mehr Loops und getrennte Reviewer erhöhen den Tokenverbrauch, den der Autor zu Beginn selbst als Kritikpunkt nennt; Iterationslimits sind die einzige genannte Bremse. Die Rot-dann-grün-Regel ist eine konkrete, übertragbare Maßnahme gegen wirkungslose Tests. Die Factory bleibt Konzept.

## Kernaussagen

- Ein Loop braucht ein Ja/Nein-Erfolgskriterium und ein Iterationslimit, sonst drehen Agents unnötige Runden → [[Ralph-Loop-Frischer-Kontext-pro-Iteration]]
- Tests müssen einmal rot gewesen sein, und Prüfszenarien bleiben dem Entwickler-Agent verborgen (gegen Reward Hacking) → [[TDD-als-Verifikationshebel]]
- Umsetzung und Prüfung trennen: Reviewer sieht nur Spezifikation und Ergebnis, Subagents melden nicht selbst „fertig“ → [[Plan-first-mit-getrenntem-Review]]
- Große Aufträge in Schritte mit frischem Kontext zerlegen, die nur über Artefakte kommunizieren → [[Handoff-Doc]]

## Verbindungen

- [[Ralph-Loop-Frischer-Kontext-pro-Iteration]]
- [[Testharness-als-staerkster-Hebel]]
- [[Kontrollierte-Agent-Parallelisierung]]
- [[2026-04-17-wiki-compiler-ralph-loop]]
- [[2026-02-23-d4m1n-ralph-loop-setup-primaer]]
