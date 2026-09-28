---
url: https://www.tiktok.com/@floknowsai/video/7669871035340033313
autor: "@floknowsai"
datum: 2026-08-03
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso.md
thema: KI-Kosten
zeitkritisch: ja
---

# Warum das Usage-Limit trotz fallender KI-Preise gleich schnell leer ist

Florian Schünemann argumentiert: Preise fallen nur für festgehaltenes Können; das jeweils stärkste Modell bleibt gleich teuer, und der Verbrauch pro Aufgabe steigt aus fünf Richtungen. Die Zahlen stehen in der Caption (Stand 3. August 2026) und nennen als Quellen Claude-Code-Kostendoku, Anthropic-Supportartikel, Modellübersicht und tbench.ai. Das Video ist eine Sekundäraufbereitung; nicht alle Angaben sind hier an den Quellen geprüft. Das Transkript ist eine maschinelle Rückübersetzung und weicht in Details von der Caption ab (etwa „80 Prozent Preissenkung“ nur im Transkript).

## Zahlen laut Caption

- Anthropic Opus-Stufe: über fünf Generationen unverändert `5 $` / `25 $` je Million Token (Input/Output).
- GPT-5.2: weiter `1,75 $` / `14 $`, Preis vom Releasetag.
- GPT-5.6 Luna: seit Ende Juli `0,20 $` / `1,20 $`; im Codex-Harness 75,7 % Terminal-Bench, GPT-5.2 62,9 %.
- Sonnet Output `15 $` statt Input `3 $`; Chain of Thought wird als Output abgerechnet.
- Tokenizer ab Claude 4.7: rund 30 % mehr Token aus demselben Text.
- Subagent startet laut Transkript mit etwa 50.000 Token (System-Prompt plus MCP-Connectoren).
- Anthropic nennt für Pro und Max keine Einheit des Limits.

## Fünf Verbrauchstreiber und vier Fragen

1M-Kontext verlängert Sitzungen, Denkstufe, Tokenizer, Subagents, ein- bis zweitägige Agentenläufe. Die vier Fragen vor dem Start: Denkstufe nötig? Connector dauerhaft im Kontext? Reicht der Hauptagent? Sitzung fortführen oder neu?

## Einordnung

Selbstgemessen ist nichts, die Zahlen sind aus Hersteller- und Benchmarkseiten zitiert. Die Gegenüberstellung Luna gegen GPT-5.2 beruht auf einem Harness und einem Benchmark. Die Aussage „Preis des Top-Modells bleibt stehen“ ist eine Generalisierung aus zwei Anbietern.

## Kernaussagen

- Kleineres Modell für gleiches Können ist der eigentliche Sparhebel → [[Modell-Eskalation-von-guenstig-nach-teuer]]
- Sitzungslänge, Connectoren und Subagent-Startkosten treiben den Verbrauch → [[Kontext-Hygiene-Entscheidungsbaum]]
- Jeder Subagent zahlt Grundkosten neu → [[Kontrollierte-Agent-Parallelisierung]]

## Verbindungen

- [[2026-07-27-cerebras-gpt-5-6-modellwahl-und-reasoning]]
- [[2026-04-15-trq212-claude-code-session-management-1m-context-primaer]]
- [[2026-07-08-claudedevs-modell-vs-effort]]
