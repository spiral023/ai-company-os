---
titel: "Vier Releases fügen der Kosten-Leistungs-Front elf Punkte hinzu"
datum: 2026-09-29
kategorie: kurz
zusammenfassung: "MiMo-V2.6-Pro, Claude Opus 5.5, GPT-6 Luna und GPT-6 Sol erweitern laut Artificial Analysis die Pareto-Front aus Intelligence Index und Kosten pro Task."
status: entwurf
quellen:
  - 2026-09-23-artificialanlys-2102833926788288704
---

Artificial Analysis (Drittanbieter) meldet am 23.09.2026, dass vier Modelle die Pareto-Front (die Modelle, die bei ihren Kosten nicht übertroffen werden) von Intelligence Index gegen Kosten pro Task innerhalb einer Woche um elf Messpunkte erweitert haben (das sind Kombinationen aus Modell und Effort-Stufe, nicht Indexpunkte). Die Punkte entstehen durch verschiedene Reasoning-Efforts: fünf von GPT-6 Luna, vier von Opus 5.5, je einer von MiMo-V2.6-Pro und GPT-6 Sol.

Die Eckpunkte auf der Front:

| Modell | Intelligence Index | Kosten pro Task |
|---|---|---|
| GPT-6 Luna (max) | 37 | $0,068 |
| MiMo-V2.6-Pro | 46 | $0,13 |
| GPT-6 Sol (max) | 48 | $1,06 |
| Claude Opus 5.5 (max mit Fallback) | 58 | $5,98 |

Opus 5.5 hat damit den höchsten gemessenen Score. MiMo-V2.6-Pro liegt bei 46 Punkten nur zwei unter Sol, kostet pro Task rund ein Achtel (eigene Rechnung aus $0,13 und $1,06).

Zwei Einschränkungen: Die Kosten sind gewichtete Durchschnitte über die Intelligence-Index-Aufgaben, kein Wert für reale Coding-Sitzungen. Dort liegt Opus 5.5 im Coding Agent Index bei etwa $13,04 pro Task. Außerdem ist die Front relativ zum gemessenen Modellset.

Da mehrere Effort-Stufen eines Modells getrennte Punkte auf der Front sind, ist die Effort-Wahl ein Kostenhebel. Vergleiche für deinen Fall Effort-Stufen desselben Modells, bevor du das Modell wechselst.
