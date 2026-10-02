---
url: https://epoch.ai/publications/the-plunging-price-of-thought
autor: Luke Emberson (Epoch AI)
datum: 2026-09-22
erfasst: 2026-10-02
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-09-22-epoch-the-plunging-price-of-thought.md
zweitquelle: 00_Inbox/Quellen/X/2026-09-22-epochairesearch-2102510281176023529.md
thema: KI-Kosten
zeitkritisch: ja
---

# Epoch AI misst den Preisverfall von KI-Leistung: etwa 47 % pro Quartal seit 2023

Epoch AI hat Kosten je Leistungsniveau auf fünf Benchmarks (FrontierMath Tier 1–3, OTIS Mock AIME, GPQA Diamond, Chess Puzzles, Mystery Game Puzzles) untersucht. Ergebnis: Das günstigste Modell für ein festes Niveau wurde seit 2023 im Schnitt um rund 47 % pro Quartal billiger, rund 13-fach pro Jahr. Die Autoren nennen die Zahlen selbst repräsentativ, aber nicht exakt. Der X-Thread von @EpochAIResearch (22.09.2026) fasst den Bericht zusammen.

## Methode
Gemessen werden die tatsächlichen Kosten je Aufgabe, nicht der Token-Preis. Ein Benchmark-Lauf mit hohem Budget wird nach dem CAISI-Verfahren nachträglich auf kleinere Token-Budgets gekürzt; so entsteht je Modell und Reasoning-Stufe eine Kosten-Leistungs-Kurve. Der Thread nennt 222 Modelle und bis zu 11 Benchmarks. Ein Test mit angekündigtem Budget lieferte ähnliche Kurven wie das stille Kürzen. Open-Weight-Modelle liefen auf gemieteter Hardware (Abweichung zur API unter 30 %). Die Rate stammt aus einem Modellfit der empirischen Kosten-Frontier (Box-Tidwell); modellfrei ergibt sich ebenfalls 47 %. Standardfehler werden bewusst nicht berichtet.

## Ergebnisse
- Je Benchmark 43 % (Chess) bis 53 % (FrontierMath); Spiele-Puzzles 39–43 %, Mathe 50–52 %.
- Direkt nach dem SOTA-Debüt fällt der Preis um 66 % pro Quartal, zwei Jahre später um 32 %.
- Beispiel GPQA Diamond: `o3` (Jan. 2025) rund 0,30 USD je Frage, `GPT-5.6 Luna` 0,0004 USD, 725-fach in unter 18 Monaten. Der Thread nennt FrontierMath: 0,55 USD gegen 0,0015 USD, 377-fach (im Berichtstext nicht zu finden, evtl. nur in einer lokal fehlenden Grafik).
- Vergleich der Rate in Log-Punkten: 4× DNA-Sequenzierung, 6× Compute, 18× Lithium-Batterien, 54× Strom (bis 1973).
- Die härteste Preiskonkurrenz nahe SOTA lief zwischen Closed-Weight-Modellen.

## Einordnung
Belastbar ist die Richtung, nicht die Einzelzahl: Je nach Mittelung liegt der Wert bei 42,9–58,0 % pro Quartal. Epoch nennt selbst Benchmaxxing (der geheime Test Mystery Game Puzzles liegt mit 44 % bzw. 38,7 % unter dem Schnitt), den kurzen Zeitraum von rund drei Jahren und die Annahme eines Nutzers, der ständig das billigste Modell wählt. Der Technologievergleich hinkt, weil der „Preis des Denkens“ ein wechselndes Bündel ist. Der Rückgang gilt für ein festes Niveau, nicht für Frontier-Preise.

## Kernaussagen
- Ein festes Leistungsniveau wird rasch billiger, daher Modellwahl regelmäßig neu bewerten → [[Modell-Eskalation-von-guenstig-nach-teuer]]
- Reale Nutzer wechseln selten Modelle und realisieren die Ersparnis nur teilweise.

## Verbindungen
- [[2026-09-23-kimmonismus-2102748118400004100]]
- [[2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso]]
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
