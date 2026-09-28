---
url: https://x.com/Alibaba_Qwen/status/2046939764428009914
autor: Alibaba Qwen
datum: 2026-04-22
erfasst: 2026-08-04
typ: tweet
rohquelle: 00_Inbox/Quellen/X/2026-04-22-alibaba-qwen-qwen3-6-27b-lokal-betreiben.md
thema: Neue Modelle
zeitkritisch: ja
beleg_art: sekundaerquelle
---

# Qwen3.6-27B: kleines offenes Coding-Modell auf Augenhöhe mit Claude 4.5 Opus (Herstellerangabe)

Alibaba veröffentlichte am 22. April 2026 das Dense-Modell Qwen3.6-27B unter Apache 2.0. Die Benchmarks stammen vom Hersteller selbst; diese Notiz beruht auf einer deutschen vibedeck-Aufarbeitung, die Zahlen wurden am Header-Chart des Tweets gegengeprüft, nicht an der Primärquelle. Verglichen wird mit Claude 4.5 Opus, das zum Veröffentlichungszeitpunkt bereits ein älteres Modell war.

## Zahlen (Hersteller-Chart, Qwen3.6-27B gegen Claude 4.5 Opus)

- Terminal-Bench 2.0: 59,3 gegen 59,3.
- SWE-bench Verified: 77,2 gegen 80,9; SWE-bench Pro: 53,5 gegen 57,1; NL2Repo: 36,2 gegen 43,2.
- SkillsBench: 48,2 gegen 45,3; Claw-Eval Pass³: 60,6 gegen 59,6; GPQA Diamond: 87,8 gegen 87,0.
- Gegen Qwen3.5-397B-A17B: in allen Coding-Benchmarks vorn, SkillsBench +18 Punkte.

## Lokaler Betrieb

Laut Aufarbeitung ab etwa 18 GB RAM (Q4-GGUF von Unsloth). Die genannten Tokens pro Sekunde (RTX 4090 50–70, Apple M3/M4 Max 30–50) sind „Richtwerte“ ohne Messquelle.

## Einordnung

Herstellerangaben, kein Drittvergleich, Harness und Sampling-Einstellungen nicht genannt. Claude 4.5 Opus ist kein aktueller Maßstab mehr. Der Befund „kleines offenes Modell nahe an einem Frontier-Modell von vor einem Release-Zyklus“ passt zur Richtung anderer Quellen, ist aber hier nicht unabhängig belegt.

## Kernaussagen

- Ein 27B-Modell erreicht im Herstellerchart bei Agentic-Coding etwa den Stand eines geschlossenen Vorjahresmodells → [[Lokale-Modell-Umleitung-Muster]]
- Lokaler Betrieb ist eine Speicher- und Bandbreitenfrage → [[Lokale-Modell-Umleitung-Muster]]

## Verbindungen

- [[Lokale-Modell-Umleitung-Muster]]
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
- [[2026-02-02-unsloth-team-claude-code-local-llm]]
- [[2026-01-22-dr-cintas-claude-code-local]]
