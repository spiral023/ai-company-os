---
url: https://x.com/omarsar0/status/2027025098578727353
autor: "elvis (@omarsar0)"
datum: 2026-02-26
erfasst: 2026-07-13
typ: artikel
---

# Elvis (@omarsar0) zu „Hilft AGENTS.md wirklich?“

## Inhalt

(per Datei-Zugriff auf vibedeck-Knowledge-Artikel abgerufen, der wiederum einen X-Thread zusammenfasst; Original-Paper: „Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?“, ETH Zürich SRI Labs, arxiv.org/abs/2602.11988)

Eine Studie der ETH Zürich (SRI Labs) führt **AGENTbench** ein: 138 Instanzen aus 12 weniger populären Python-Repos mit bereits vorhandenen, von Menschen geschriebenen Context Files (durchschnittlich 641 Wörter, ~10 Abschnitte). Getestet wurden Claude Code (Sonnet-4.5), Codex (GPT-5.2/GPT-5.1 mini) und Qwen Code (Qwen3-30b-coder) unter drei Bedingungen: ohne Context File, mit LLM-generiertem Context File, mit menschlich geschriebenem Context File.

Kernergebnisse:
- **LLM-generierte Context Files senken die Erfolgsquote** gegenüber gar keinem Kontext (SWE-bench Lite: -0,5%, AGENTbench: -2%) und erhöhen die Inference-Kosten um über 20%.
- Context Files (egal ob menschlich oder LLM-generiert) führen zu 14-22% mehr Reasoning-Tokens und 2-4 zusätzlichen Schritten — Instruction-Following kostet immer Rechenleistung, unabhängig davon ob es hilft.
- **Menschlich geschriebene Dateien** erzielen dagegen **+4% Erfolgsquote**.
- Explorations-Paradoxon: Agenten folgen Instruktionen in Context Files sehr genau (z.B. Tool-Nutzung steigt drastisch, wenn vorgeschrieben), explorieren dadurch gründlicher, aber nicht korrekter — mehr Files/Tests durchsuchen hilft nicht automatisch, die richtige Stelle zu finden.
- Der entscheidende Unterschied ist **Redundanz vs. Additivität**: LLM-generierte Dateien reproduzieren oft, was bereits in README/Doku steht. In einem Kontroll-Experiment (Doku vorher entfernt) verbesserten sich LLM-generierte Dateien um 2,7% und übertrafen sogar die menschlichen — reiner Redundanz-Effekt macht sie sonst kontraproduktiv. Menschliche Dateien enthalten dagegen oft Informationen, die nirgendwo sonst stehen (Tooling-Entscheidungen, CI-Eigenheiten, nicht-standardisierte Konventionen).
- Praktische Konsequenz aus dem Artikel: „Schreibe für die Lücke, nicht für den Überblick“ — Context Files sollten kodieren, was das Repo *nicht* bereits erklärt.

## Kernaussagen

- LLM-generierte Context Files (AGENTS.md/CLAUDE.md) senken empirisch die Erfolgsquote und erhöhen die Kosten um >20%, während menschlich geschriebene +4% Erfolgsquote bringen — der Unterschied liegt in Redundanz (Doppelung von README/Doku) vs. additivem Kontext → [[AGENTS-md-Onboarding-Design]]
- Instruction-Following in Context Files funktioniert zuverlässig, aber mehr befolgte Instruktionen bedeuten nicht automatisch mehr Erfolg — Agenten explorieren gründlicher, nicht unbedingt korrekter → [[AGENTS-md-Onboarding-Design]]
