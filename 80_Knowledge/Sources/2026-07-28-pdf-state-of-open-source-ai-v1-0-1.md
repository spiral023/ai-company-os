---
url: https://stateofopensource.ai/state-of-open-source-ai-v1-0-1.pdf
autor: Mozilla mit SlashData
datum: 2026-07-28
erfasst: 2026-08-05
typ: artikel
rohquelle: 00_Inbox/Quellen/PDF/2026-07-28-pdf-state-of-open-source-ai-v1-0-1.md
zweitquelle: 00_Inbox/Quellen/URL/2026-07-01-mozilla-mit-slashdata-state-of-open-source-ai-2026.md
thema: Markt & Strategie
zeitkritisch: ja
---

# Mozilla-Bericht zu offener KI 2026: kleiner Modellabstand, Engpass im Harness

Der 65-seitige Bericht „State of Open Source AI“ (Volume 1.01, Juli 2026) von Mozilla mit SlashData sammelt Fremdmessungen (Artificial Analysis, Epoch AI, OpenRouter, vals.ai) und eine eigene Entwicklerumfrage (Feld 19.–29. Mai 2026, n=1.494). Die Zweitquelle ist eine deutsche vibedeck-Aufarbeitung desselben Berichts; Zahlen unten stammen aus dem PDF-Text. Belastbar sind die Fremdmessungen. Die fünf „Wetten“ sind eine Förderagenda des selbst beteiligten Herausgebers.

## Fähigkeit und Preis

- Artificial Analysis Intelligence Index v4.1 (Juli 2026): bestes offenes Modell Kimi K3 mit 57 (Rang 4 von 586), bestes geschlossenes Claude Opus 5 mit 61. Fable 5 und Sol sind Deployed-System-Konfigurationen, verglichen wird also System gegen Modell.
- Epoch Capabilities Index: Kimi K3 156, GPT-5.6 Sol 162; die 90-%-Konfidenzintervalle überlappen.
- Herstellerläufe auf verschiedenen Skalen, laut Bericht nur „direktional“ zu lesen.
- Günstigster Anbieter auf GPT-4-Niveau: 20 $ auf 0,40 $ pro 1M Token in 36 Monaten.

## Harness und Kosten

- Terminal-Bench 2.0 (Mai 2026): Fremd-Scaffold mit Anthropic-Gewichten 79,8 % gegen Claude Code mit denselben Gewichten 58,0 %. Auf Terminal-Bench 2.1 nur noch etwa 3 Punkte Spread.
- Neutraler Scaffold (vals.ai Terminus-2): GLM 5.2 67,79 % bei 0,43 $ pro Task, Opus 4.7 68,54 % bei 1,98 $.
- Umfrage: offene Modelle erreichen zu 51 % Produktion, geschlossene zu 63 %; Größe hilft nur Closed.
- Microsoft, Uber und Stripe werden als Beispiele für Bruchpunkte des Token-Abrechnungsmodells genannt (Berichtsangaben, nicht geprüft).

## Einordnung

Belastbar ist die Aussage, dass Benchmark-Scores an Modell und Harness hängen. Offen bleibt die Vergleichbarkeit, weil Hersteller im eigenen Harness messen. Der Bericht nennt selbst die Zahl „3,3 % Gap“ in der Watchlist, die zu den 4 bzw. 6 Indexpunkten nicht erklärt passt. Der OpenRouter-Tokenanteil misst nur gerouteten Traffic. Die Selbsthosting-Schwelle von etwa 8.000 Konversationen pro Tag ist eine Berichtsannahme.

## Kernaussagen

- Offene Modelle liegen bei Reasoning etwa einen Release-Zyklus hinter der Frontier; Zuordnung nach Aufgabe senkt den Bedarf am teuersten Modell → [[Modell-Eskalation-von-guenstig-nach-teuer]]
- Kein veröffentlichter Frontier-Benchmark ist harness-neutral → [[Testharness-als-staerkster-Hebel]]
- Offene Gewichte als Second Source gegen Metered Pricing → [[Lokale-Modell-Umleitung-Muster]]

## Verbindungen

- [[Modell-Eskalation-von-guenstig-nach-teuer]]
- [[Lokale-Modell-Umleitung-Muster]]
- [[2026-07-27-cerebras-gpt-5-6-modellwahl-und-reasoning]]
- [[2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso]]
