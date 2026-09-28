---
url: https://www.tiktok.com/@nate.b.jones/video/7589872498901077278
autor: "@nate.b.jones"
datum: 2025-12-31
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2025-12-31-natebjones-seriously-not-worth-it-now.md
thema: Markt & Strategie
zeitkritisch: nein
---

# Fine-Tuning ist 2026 die letzte Option: erst Harness, dann Modell anfassen

Ein knapper Standpunkt-Clip (1:51, automatisches Transkript): Wer 2026 ein Modell selbst trainiert oder feintunt, verliert laut Nate B. Jones Zeit gegenüber einem gut gebauten Agentic Harness. Die Quelle ist reine Meinung ohne Messwerte, Fallstudien oder Methode. Belastbar ist höchstens die Entscheidungsreihenfolge, nicht die Absolutheit der Aussage.

## Die Argumentation

- **Zeitfalle:** Ein Fine-Tuning-Projekt dauert laut Sprecher acht bis zwölf Wochen. In dieser Zeit erscheint eine neue Modellgeneration, und das feingetunte Modell bleibt auf dem alten Stand „gestrandet“.
- **Ersatz durch Harness:** Was man mit Fine-Tuning erreichen will, lasse sich mit passenden Instruktionen, Constraints, Guardrails und Evaluations erreichen, also mit einem Harness, das das Modell in die gewünschte Richtung lenkt. Ein anderes Substitut gebe es nicht.
- **Reihenfolge:** Fine-Tuning sei eine „letzte Option“, die durch das steigende Tempo der Modellentwicklung immer später komme.
- **Kostenbehauptung:** Im Unternehmenssektor seien im letzten Jahr zweistellige bis dreistellige Millionenbeträge in Fine-Tuning verbrannt worden. Der Sprecher nennt dafür weder Quelle noch Herleitung („tens of millions, probably hundreds of millions“).

## Einordnung

Die Kernrichtung deckt sich mit dem Bestand: Erst Instruktionen, Testharness und Evals ausreizen, bevor man am Modell selbst schraubt. Die Zeitfalle-Logik (Modellwechsel schneller als Trainingszyklus) ist plausibel, aber nicht belegt. „Fine-Tuning is dead“ ist Zuspitzung: Für enge, hochvolumige Aufgaben, Latenz- oder Kostenziele mit kleinen Modellen oder Datenschutzvorgaben kann Fine-Tuning weiterhin sinnvoll sein; das erwähnt der Clip nicht. Die Millionenzahl ist eine ungeprüfte Schätzung. Die Aussage ist ein Ausgangspunkt für eine eigene Prüfung (Eval-Baseline vor jeder Fine-Tuning-Entscheidung), kein Beweis.

## Kernaussagen

- Zuerst Harness (Instruktionen, Constraints, Evals) ausreizen, Fine-Tuning nur als letzte Option → [[Testharness-als-staerkster-Hebel]]
- Modellgenerationen wechseln schneller als Trainingszyklen, daher wird spezialisiertes Training schnell obsolet → [[Intent-Engineering-als-dritte-Schicht]]

## Verbindungen

- [[Testharness-als-staerkster-Hebel]]
- [[Intent-Engineering-als-dritte-Schicht]]
- [[2026-02-24-nate-b-jones-intent-engineering]]
