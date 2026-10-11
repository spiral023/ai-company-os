---
url: https://developer.nvidia.com/blog/evaluating-ai-agent-skill-performance-with-nvidia-skillevaluator/
autor: NVIDIA Technical Blog
datum: 2026-08-19
erfasst: 2026-10-11
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-08-19-developer-evaluating-ai-agent-skill-performance-with-nvidi.md
zweitquelle: 00_Inbox/Quellen/X/2026-08-19-nvidiaai-2090113635683340622.md
thema: Arbeitsweisen
zeitkritisch: ja
---

# NVIDIA: Skill-Nutzen mit kontrollierten Vergleichsläufen messen

NVIDIA berichtet bessere Ergebnisse mit Skills in eigenen Produktaufgaben. Primärartikel und begleitender Tweet beschreiben dieselbe Evaluation und werden gemeinsam geführt.

## Einordnung

Herstellerbenchmark über mehr als 300 Skills für mehr als 30 Produkte, geprüft mit zwei Harnesses. Zahlen beziehen sich auf `benchmarks.json`, Snapshot 12. August 2026, Commit `738d79e`; sie sind kein allgemeiner Wirksamkeitsnachweis für beliebige Skills.

## Kernaussagen

- Zuerst Struktur, Sicherheit und Lizenz prüfen; danach überlappende Inhalte; zuletzt Aufgaben mit und ohne Skill unter gleichen Bedingungen ausführen.
- `Harbor` isoliert die Läufe. Prompt, Modell, Eingaben und Bewertung bleiben innerhalb eines Harness-Vergleichs gleich.
- Makromittel gewichten jedes Skill-Harness-Paar gleich. Correctness steigt von 46 auf 87 Punkte, Effectiveness von 39 auf 78; Efficiency-Lift beträgt 35 Punkte.
- Testfälle müssen relevante Aufgaben und Nicht-Anwendungsfälle abdecken. Ein Skill sollte bei unpassenden Anfragen nicht geladen werden.

## Messgrenzen

85 % der Skills wurden einmal je Aufgabe getestet, 15 % zweimal; Konfidenzintervalle fehlen. Discoverability und Efficiency bewerten teilweise das Laden und Benutzen des Skills selbst. Deshalb messen ihre Gewinne nicht nur bessere Aufgabenergebnisse. Scores sind keine Erfolgswahrscheinlichkeiten.

Tokens und Laufzeit werden separat erfasst: `jetson-optimize-memory` spart in einem Einzelversuch 76,9 % Tokens, `cuopt-install` benötigt 120,3 % mehr. Das beweist weder generelle Kostensenkung noch stabile Zeitgewinne.

## Verbindungen

- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]] — Vergleich mit Baseline und Nicht-Anwendungsfällen.
- [[Testharness-als-staerkster-Hebel]] — die Definition des Scores begrenzt seine Bedeutung.

## Medien

Beide Bilder geprüft: Der Tweet zeigt die drei Prüfstufen, der Artikel ein dekoratives Motiv. Keine zusätzlichen Benchmarkzahlen in den Bildern.

![Drei Prüfstufen des SkillEvaluator](../../00_Inbox/Quellen/X/medien/2026-08-19-nvidiaai-2090113635683340622/01-photo.jpg)

![Dekoratives Artikelmotiv](../../00_Inbox/Quellen/URL/medien/2026-08-19-developer-evaluating-ai-agent-skill-performance-with-nvidi/01-bild.png)
