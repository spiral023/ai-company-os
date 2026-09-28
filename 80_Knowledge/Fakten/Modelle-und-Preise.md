# Fakten: Modelle, Preise, Benchmarks

**Stand:** 2026-09-29

Datierte Einzelangaben aus den verarbeiteten Quellen (`80_Knowledge/Sources/`). Anders als ein Pattern beschreibt dieses Register keine Arbeitsweise, sondern hält fest, **wer was wann gemessen oder angekündigt hat**. Jede Zeile führt Datum, Gegenstand, Aussage, Einschränkung und Quelle.

## Lesehinweise

- Zahlen sind **nur innerhalb derselben Messung vergleichbar**. Artificial-Analysis-Indizes tragen Versionsnummern (der Juli-Bericht nennt Opus 5 mit 61 Punkten im Intelligence Index v4.1, die September-Posts nennen 51 Punkte in v4.3). Kosten pro Task im Intelligence Index und im Coding Agent Index sind verschiedene Messungen.
- Herstellerangaben und Drittmessungen stehen in der Spalte „Einschränkung“. Ein Eintrag ohne Vermerk ist keine Bestätigung.
- Preise und Modellnamen verfallen. Neue Angaben werden als neue Zeile ergänzt, alte bleiben mit ihrem Datum stehen.

## Modelle und Releases

| Datum | Gegenstand | Aussage | Einschränkung | Quelle |
|---|---|---|---|---|
| 2026-09-22 | Claude Opus 5.5 | Kontextfenster 1 Mio. Token, Bild und Text als Input, fünf Effort-Stufen (low bis max), unverändert zu Opus 5 | - | [[2026-09-22-artificialanlys-2102438210798514391]] |
| 2026-09-15 | Jev (TypeSafe AI) | Release als „System One“-Modell für typisierte Entscheidungen (Choice, Score, Noul) mit Wahrscheinlichkeiten; kein Text-Output | Herstellerangabe laut Drittartikel; Closed Weights, Early Access, nur Text/JSON | [[2026-09-18-akshay_pachaar-2101037514945597645]] |
| 2026-08-03 | Subagent-Startkosten | ca. 50.000 Token (System-Prompt plus MCP-Connectoren) | Nur im Transkript (Rückübersetzung), nicht in Caption | [[2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso]] |
| 2026-08-03 | Claude-Tokenizer ab 4.7 | ca. 30 % mehr Token aus demselben Text | Creator-Angabe, nicht an Anthropic-Quelle geprüft | [[2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso]] |
| 2026-07-27 | Sprachabhängiger Token-Mehrverbrauch Gemini, Mistral, GPT | ca. +12 % laut Sprecher; Asiatische Modelle fast +50 % | Sprecherwiedergabe; sichtbar: GPT 5.6 Sol Französisch +20 %, Chinesisch +16 %; Opus 4.8 Chinesisch +19 % | [[2026-07-27-techfeed5-1-reason-why-the-cloud-limits-could-hit-directly-that-we-talk-to-opus-in]] |
| 2026-07-27 | Sprachabhängiger Token-Mehrverbrauch Claude Opus | Deutsch ca. +57 % gegenüber Englisch laut Sprecher | Tabelle ohne Quellenangabe, Deutsch-Zeile im Bild verdeckt; Einzelblick | [[2026-07-27-techfeed5-1-reason-why-the-cloud-limits-could-hit-directly-that-we-talk-to-opus-in]] |
| 2026-07-27 | Kimi K3 Serving | ca. 1,4 TB, MXFP4, 64+ Accelerators (ca. 8 Nodes); Inkling ab 600 GB (1 Node), GLM 5.2 ca. 577 GB INT4 | Gewichte K3 am 27.07.2026, API 16.07.2026 | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-04-22 | Qwen3.6-27B lokaler Betrieb | ab ca. 18 GB RAM (Q4-GGUF), ca. 50–70 tok/s auf RTX 4090 | Richtwerte der vibedeck-Aufarbeitung ohne Messquelle; Sekundärquelle | [[2026-04-22-alibaba-qwen-qwen3-6-27b-lokal-betreiben]] |

## Preise

| Datum | Gegenstand | Aussage | Einschränkung | Quelle |
|---|---|---|---|---|
| 2026-09-24 | Claude Code mit Opus 5.5 (max) | Cost per Task `$13.04` (Opus 5: `$10.79`, +21 %) | Coding Agent Index (nicht Intelligence Index), pay-per-token API | [[2026-09-24-artificialanlys-2102932119995756613]] |
| 2026-09-22 | GPT-6 Sol | `$2`/`$10` pro 1M Input/Output (GPT-5.6 Sol: `$4`/`$20`) | Cache Reads 90 % Rabatt, Cache Writes 25 % Aufschlag; Stand 2026-09-22 | [[2026-09-22-artificialanlys-2102462962758033624]] |
| 2026-09-22 | GPT-6 Luna | `$0.10`/`$0.50` pro 1M Input/Output (GPT-5.6 Luna: `$0.20`/`$1.20`) | Cache Reads 90 % Rabatt, Cache Writes 25 % Aufschlag; Stand 2026-09-22 | [[2026-09-22-artificialanlys-2102462962758033624]] |
| 2026-09-22 | Claude Opus 5.5 | `$4`/`$20` pro 1M Input/Output (Opus 5: `$5`/`$25`, minus 20 %) | Stand 2026-09-22 | [[2026-09-22-artificialanlys-2102438210798514391]] |
| 2026-09-22 | Claude Opus 5.5 | Cache Reads `$0.20` pro 1M (vorher `$0.50`, minus 60 %), Cache Writes `$5` (5 Min TTL, vorher `$6.25`); 95 % Rabatt auf ungecachten Input | Stand 2026-09-22 | [[2026-09-22-artificialanlys-2102438210798514391]] |
| 2026-09-18 | Jev | `$0.042` pro 1M Input-Token, Output kostenlos | Herstellerangabe | [[2026-09-18-akshay_pachaar-2101037514945597645]] |
| 2026-08-03 | GPT-5.6 Luna | 0,20 $/1,20 $ pro 1M Token seit Ende Juli 2026 | Creator-Angabe; Transkript nennt zusätzlich 80 % Senkung, weicht von Caption ab | [[2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso]] |
| 2026-08-03 | GPT-5.2 | 1,75 $/14 $ pro 1M Token, unverändert seit Release | Creator-Angabe | [[2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso]] |
| 2026-08-03 | Anthropic Opus-Stufe | 5 $/25 $ pro 1M Token, unverändert über fünf Generationen | Creator-Angabe mit Verweis auf Anthropic-Modellübersicht | [[2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso]] |
| 2026-07-28 | Stripe, Inferenzkosten | minus 73 % (50 Mio. API-Calls täglich über vLLM mit einem Drittel der GPU-Flotte) | Berichtsangabe, nicht geprüft | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-07-28 | GLM 5.2 (offen), Terminal-Bench 2.1 auf vals.ai Terminus-2 | 67,79 % bei 0,43 $ pro Task | Neutraler Scaffold, Drittanbieter | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-07-28 | Claude Opus 4.8, Terminal-Bench 2.1 auf vals.ai Terminus-2 | 71,91 % bei 2,41 $ pro Task | Neutraler Scaffold, Drittanbieter | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-07-28 | Claude Opus 4.7, Terminal-Bench 2.1 auf vals.ai Terminus-2 | 68,54 % bei 1,98 $ pro Task | Neutraler Scaffold; ca. 5x Preis für ca. 1 Punkt | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-04-30 | DeepSeek-V4 Pro | 0,435 $/M Input, 1,6T Parameter, 1M Kontext | Bericht, April 2026 | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2025-12-31 | Günstigster Anbieter auf GPT-4-Niveau | 0,40 $ pro 1M Token (blended) gegenüber 20 $ im Nov 2023, 45 $ zum GPT-4-Launch (Faktor 50 bzw. 112) | a16z-LLMflation-Methodik, Listenpreise, Dez 2025 | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2025-01-31 | DeepSeek-R1 vs. OpenAI o1-1217 | 0,55 $/2,19 $ gegen 15 $/60 $ pro 1M Token bei MATH-500 97,3 % gegen ca. 97 % (ca. 27x Preisunterschied) | Alt-Angabe Jan 2025, MIT-Lizenz | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |

## Benchmarks und Messungen

| Datum | Gegenstand | Aussage | Einschränkung | Quelle |
|---|---|---|---|---|
| 2026-09-24 | Claude Code mit Opus 5.5 (max) | Coding Agent Index v1.5: 66 Punkte, höchster gemessener Wert (Opus 5: 60, Fable 5.1: 62) | Coding Agent Index, Claude Code Harness; DeepSWE v1.1, Terminal-Bench 4.0, SWE-Atlas-QnA gleich gewichtet | [[2026-09-24-artificialanlys-2102932119995756613]] |
| 2026-09-24 | Claude Code mit Opus 5.5 (max) | Terminal-Bench 4.0 63,1 % (Opus 5: 54,5 %), DeepSWE v1.1 68,4 % (62,5 %), SWE-Atlas-QnA 66,4 % (62,1 %) | Coding Agent Index; Terminal-Bench-Wert weicht vom Intelligence-Index-Wert (59,6 %) ab | [[2026-09-24-artificialanlys-2102932119995756613]] |
| 2026-09-24 | Claude Code mit Opus 5.5 (max) | Ca. 15,6 Mio. Token pro Task (Opus 5: 11,4 Mio.), ca. 2,4-mal so viele Output-Token | Coding Agent Index | [[2026-09-24-artificialanlys-2102932119995756613]] |
| 2026-09-23 | MiMo-V2.6-Pro | Intelligence Index 46 bei `$0.13` pro Task | Intelligence Index, Cost per Intelligence-Index-Task | [[2026-09-23-artificialanlys-2102833926788288704]] |
| 2026-09-23 | GPT-6 Luna (max) | Intelligence Index 37 bei `$0.068` pro Task | Intelligence Index; im Quelltext von 2102462962758033624 gerundet `$0.07` | [[2026-09-23-artificialanlys-2102833926788288704]] |
| 2026-09-23 | Claude Opus 5.5 (max mit Fallback) | Intelligence Index 58 bei `$5.98` pro Task | Intelligence Index, nicht Coding Agent Index | [[2026-09-23-artificialanlys-2102833926788288704]] |
| 2026-09-22 | GPT-6 Sol / Luna | GDPval-AA v2.1: Sol ca. -100 Elo, Luna ca. -75 Elo; AA-Briefcase v1.1: Luna ca. -45 Elo, Sol unverändert; jeweils gegenüber GPT-5.6 | Ursache laut Quelle: schwächere Präsentationsqualität, fehlende Rubrik-Elemente | [[2026-09-22-artificialanlys-2102462962758033624]] |
| 2026-09-22 | GPT-6 Sol / Luna | Terminal-Bench 4.0: Sol 44 % (vorher 40 %), Luna 13 % (vorher 12 %); AutomationBench-AA: Sol 62 % (60 %), Luna 53 % (50 %) | Intelligence-Index-Setup; weicht vom Wert im Coding Agent Index (43 % vs. 37 %) ab, anderes Harness | [[2026-09-22-artificialanlys-2102462962758033624]] |
| 2026-09-22 | GPT-6 Sol (max) | Intelligence Index 48; Cost per Intelligence-Index-Task `$1.06` (GPT-5.6 Sol max `$1.99`) | Intelligence Index; 31k Output-Token pro Task (GPT-5.6 Sol 29k) | [[2026-09-22-artificialanlys-2102462962758033624]] |
| 2026-09-22 | GPT-6 Sol (max) | Coding Agent Index 57 (+2 gegenüber GPT-5.6 Sol), `$2.99` pro Task, ca. 50 % weniger | Coding Agent Index, Codex-Harness; Terminal-Bench 4.0 43 % vs. 37 %, SWE-Atlas-QnA 58 % vs. 54 % | [[2026-09-22-artificialanlys-2102462962758033624]] |
| 2026-09-22 | GPT-6 Sol (max) | AA-Omniscience Halluzinationsrate 60 % (vorher 92 %), Accuracy 54 % (vorher 59 %), Omniscience Index 27 (vorher 22) | Sol beantwortet nur 83 % der Fragen (vorher 99 %), Verbesserung durch Verweigern | [[2026-09-22-artificialanlys-2102462962758033624]] |
| 2026-09-22 | GPT-6 Luna (max) | Intelligence Index 37; Cost per Intelligence-Index-Task `$0.07` (GPT-5.6 Luna max `$0.18`) | Intelligence Index; 51k Output-Token pro Task (GPT-5.6 Luna 41k) | [[2026-09-22-artificialanlys-2102462962758033624]] |
| 2026-09-22 | GPT-6 Luna (max) | Coding Agent Index 41 (-2 gegenüber GPT-5.6 Luna), ca. 60 % niedrigere Kosten pro Task | Coding Agent Index, Codex-Harness; SWE-Atlas-QnA 44 % vs. 49 %, DeepSWE v1.1 64 % vs. 66 % | [[2026-09-22-artificialanlys-2102462962758033624]] |
| 2026-09-22 | GPT-6 Luna (max) | AA-Omniscience Halluzinationsrate 77 % (vorher 93 %), Accuracy 44 % (vorher 43 %), Omniscience Index 1 (vorher -10) | Luna beantwortet weniger Fragen | [[2026-09-22-artificialanlys-2102462962758033624]] |
| 2026-09-22 | Claude Opus 5.5 (max, mit Fallback) | Intelligence Index v4.3: 58 Punkte, höchster gemessener Wert (Fable 5.1: 53, GPT-6 Astra: 53, Opus 5: 51) | Artificial Analysis, Intelligence Index, Fallback aktiv | [[2026-09-22-artificialanlys-2102438210798514391]] |
| 2026-09-22 | Claude Opus 5.5 (max) | ca. 119k Output-Token pro Intelligence-Index-Task (Opus 5 ca. 73k, Fable 5.1 ca. 78k, GPT-6 Astra ca. 27k); Kosten pro Task auf Niveau von Opus 5 | Intelligence Index, nicht Coding Agent Index | [[2026-09-22-artificialanlys-2102438210798514391]] |
| 2026-09-22 | Claude Opus 5.5 | Humanity's Last Exam 61,4 % (bisher bester Wert 59,1 %, Fable 5.1) | Intelligence Index, Artificial Analysis | [[2026-09-22-artificialanlys-2102438210798514391]] |
| 2026-09-22 | Claude Opus 5.5 | SciCode 66,9 % (bisher 63,1 %, Fable 5.1) | Intelligence Index, Artificial Analysis | [[2026-09-22-artificialanlys-2102438210798514391]] |
| 2026-09-22 | Claude Opus 5.5 | Terminal-Bench 4.0 59,6 %, gleichauf mit GPT-6 Astra (xhigh), +11 Punkte gegenüber Opus 5 | Intelligence-Index-Setup (nicht Coding Agent Index) | [[2026-09-22-artificialanlys-2102438210798514391]] |
| 2026-09-22 | Claude Opus 5.5 | AA-Briefcase v1.1 Elo 1822, +143 gegenüber Fable 5.1 | Privater Benchmark, Harness Stirrup | [[2026-09-22-artificialanlys-2102438210798514391]] |
| 2026-09-18 | Jev | Ende-zu-Ende-Latenz 70 bis 500 ms | Herstellerangabe, keine unabhängige Messung | [[2026-09-18-akshay_pachaar-2101037514945597645]] |
| 2026-09-18 | Jev | ca. 200-mal schneller und 400-mal günstiger als vergleichbare LLM-Workflows | Herstellerangabe aus eigenen Workflow-Evals, laut Artikel Obergrenze | [[2026-09-18-akshay_pachaar-2101037514945597645]] |
| 2026-08-03 | GPT-5.6 Luna vs. GPT-5.2, Terminal-Bench im Codex-Harness | 75,7 % gegen 62,9 % | Creator-Angabe mit Verweis auf tbench.ai, nicht geprüft | [[2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso]] |
| 2026-07-28 | Terminal-Bench 2.1, Harness-Effekt | Codex CLI/GPT-5.5 83,4 %, Claude Code/Fable 5 83,1 %, bester unabhängiger Harness mit Fable-Gewichten 80,4 % (Spread ca. 3 Punkte) | acht Wochen nach 2.0; Lab-Harness gewinnt jeweils auf eigenem Modell | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-07-28 | Kimi K3 vs. GPT-5.6 Sol, Terminal-Bench 2.1 | 88,3 gegen 88,8 | Herstellerlauf laut Bericht, direktional; Harness unterschiedlich | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-07-28 | Kimi K3 vs. Fable 5, FrontierSWE | 81,2 gegen 86,6 | Herstellerangabe (Moonshot) | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-07-28 | Fable 5 vs. Kimi K3, GDPval-AA v2 | Fable 5 führt mit 92 Elo | Größte Elo-Trennung unter gemeinsamen Benchmarks laut Bericht | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-07-28 | Epoch Capabilities Index | GPT-5.6 Sol 162 (CI 159–166), Kimi K3 156 (CI 154–159), Abstand 6 Punkte | Konfidenzintervalle (90 %) überlappen; alle gelisteten Modelle von April bis Juli 2026 | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-07-28 | Artificial Analysis Intelligence Index v4.1 | Claude Opus 5 = 61 (geschlossen, Spitze), Kimi K3 = 57 (bestes offenes Modell, Rang 4 von 586) | Fable 5 und Sol sind Deployed-System-Konfigurationen (System gegen Modell); Drittanbieter-Index, Juli 2026 | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-05-31 | Terminal-Bench 2.0, Harness-Effekt | Fremd-Scaffold mit Anthropic-Gewichten 79,8 % gegen Claude Code mit denselben Gewichten 58,0 % (21,8 Punkte) | Mai 2026 (Tag ungenau); Bericht zitiert Fremdmessung | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-04-22 | Qwen3.6-27B vs. Claude 4.5 Opus, Terminal-Bench 2.0 | 59,3 gegen 59,3 | Selbstmessung Alibaba, Apache-2.0-Modell, Harness nicht genannt | [[2026-04-22-alibaba-qwen-qwen3-6-27b-lokal-betreiben]] |
| 2026-04-22 | Qwen3.6-27B vs. Claude 4.5 Opus, SkillsBench | 48,2 gegen 45,3 | Selbstmessung Alibaba | [[2026-04-22-alibaba-qwen-qwen3-6-27b-lokal-betreiben]] |
| 2026-04-22 | Qwen3.6-27B vs. Claude 4.5 Opus, SWE-bench Verified | 77,2 gegen 80,9 | Selbstmessung Alibaba | [[2026-04-22-alibaba-qwen-qwen3-6-27b-lokal-betreiben]] |
| 2026-04-22 | Qwen3.6-27B vs. Claude 4.5 Opus, GPQA Diamond | 87,8 gegen 87,0 | Selbstmessung Alibaba | [[2026-04-22-alibaba-qwen-qwen3-6-27b-lokal-betreiben]] |

## Markt und Adoption

| Datum | Gegenstand | Aussage | Einschränkung | Quelle |
|---|---|---|---|---|
| 2026-09-23 | Intelligence Index vs. Cost per Task Pareto-Front | Elf neue Punkte auf der Front in einer Woche: fünf GPT-6 Luna, vier Claude Opus 5.5, je einer MiMo-V2.6-Pro und GPT-6 Sol | Verschiedene Reasoning-Efforts; Artificial Analysis | [[2026-09-23-artificialanlys-2102833926788288704]] |
| 2026-07-28 | Self-Hosting-Breakeven | ab ca. 8.000 Konversationen pro Tag | Annahme des Berichts | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-07-28 | Request-Anteile nach Anbieter (OpenRouter) | Google allein 28,7 %, Anthropic plus OpenAI ca. 20 % | FT-Analyse mid-2026, nur gerouteter Traffic | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-07-28 | Nutzung vs. Umsatz auf OpenRouter (Mai–Sep 2025) | Offen ca. 20 % der Nutzung, ca. 4 % des Umsatzes; Linux Foundation schätzt 24,8 Mrd. $ jährliche nicht realisierte Ersparnis | Studie zitiert, Schätzung | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-07-27 | OpenRouter, Top-20-Tokens Juli 2026 | Ränge 1–10: 72,4 % offene gegen 8,7 % geschlossene Tokens; sieben volumenstärkste Modelle offen (MiMo-V2.5 32,3T Tokens/17,8 %) | Nur gerouteter Traffic, First-Party ausgeschlossen; Kimi K3 fehlt (nach Messfenster) | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-06-30 | Open-Weight-Anteil an OpenRouter-Tokens | ca. 2 % (Nov 2024), ca. 33 % (Nov 2025), weiter steigend (Jun 2026) | Kurve zwischen Messpunkten indikativ | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
| 2026-05-29 | Produktionsquote nach Modelltyp (Umfrage) | Offene Modelle 51 %, geschlossene 63 %; Enterprise 57 % gegen 73 % | SlashData-Umfrage, n=1.494, Feld 19.–29. Mai 2026 | [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] |
