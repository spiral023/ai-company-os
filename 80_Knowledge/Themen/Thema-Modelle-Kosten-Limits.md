# Modelle, Kosten & Limits

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-22. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Modellwahl, Reasoning-Effort, Preise, Kosten pro Task, Usage Limits, Prompt Caching, Benchmarks und Provider-Umleitung. Verfügbarkeit offener Gewichte, lokale Inferenz, Hardware und Fine-Tuning gehören vorrangig zu open-source-llms; Kostenvergleiche bleiben hier.

## Suchbegriffe

- **Hauptkeyword:** Claude Code Kosten
- **Long-Tail:** Claude Code Usage Limits; Kosten pro Task statt pro Token; Prompt Caching Claude Code; Claude Code mit lokalem Modell; Reasoning Effort wählen; Modell-Eskalation günstig nach teuer
- **Fragen:** Welches Modell für welche Aufgabe? / Warum sind meine Limits so schnell leer?
- **Häufig in den Quellen:** modell-eskalation (31), modell (29), kosten (21), effort (21), benchmark (19), preis (17), kosten pro task (14), terminal-bench (13), gpt-6 (13), token (12), modellwahl (8), coding agent index (8), preise (8), intelligence index (7), pareto (7), sonnet (7), opus 5.5 (7), anthropic_base_url (4), cost per task (4), /compact (4)

## Verwandte Themen

- [[Thema-Kontext-Management]] — Kontext-Management
- [[Thema-Multi-Agent-Parallelisierung]] — Multi-Agent & Parallelisierung
- [[Thema-Autonome-Läufe-Loops-CI]] — Autonome Läufe, Loops & CI
- [[Thema-Rolle-Lernen-Markt]] — Rolle, Lernen & Markt
- [[Thema-Open-Source-LLMs-lokale-Modelle]] — Open-Source-LLMs & lokale Modelle

## Patterns (5)

- [[Entscheidung-per-Scoring-statt-Generierung]] · meinung · 4 Belege
- [[Lokale-Modell-Umleitung-Muster]] · mehrfach-belegt · 10 Belege
- [[Modell-Eskalation-von-guenstig-nach-teuer]] · mehrfach-belegt · 53 Belege
- [[Prompt-Cache-TTL-nach-Agent-Pausen-waehlen]] · meinung · 1 Belege
- [[Trainingsdaten-Dichte-als-Stack-Kriterium]] · meinung · 3 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Action-Space-Design-nach-Modellfaehigkeit]], [[Decision-Head-Finetuning]], [[Kontext-Hygiene-Entscheidungsbaum]], [[Kontrollierte-Agent-Parallelisierung]], [[Lokale-Inferenz-nach-Arbeitslast-dimensionieren]]

## Quellen (65)

- [[2026-10-20-artificialanlys-2112582116651466965]] — Artificial Analysis vergleicht am 20.10.2026 sinkende Kosten fester Intelligence-Index-Schwellen mit steigenden Spitzenkosten.
- [[2026-10-19-artificialanlys-2112218661432000694]] — Artificial Analysis meldet am 19.10.2026 Fortschritte für `DeepSeek V4.1 Flash 1017`.
- [[2026-10-17-kimmonismus-2111385805449048181]] — Chubby berichtet am 17.10.2026 über `DeepSeek V4.1 Flash-1017`.
- [[2026-10-16-artificialanlys-2111052531166249039]] — Artificial Analysis meldet am 16.10.2026 `Liquid AI d1-ultra` auf Rang 1 seines Decision Index `v1.0`.
- [[2026-10-16-0xkense1-2111105138290987198]] — Kenseis Eigenbenchmark legt nahe: Wiederholt mitgesendeter Kontext bietet mehr Einsparpotenzial als kurze Antworten.
- [[2026-10-14-andrewcurran-2110444907966181544]] — Andrew Curran begegnet dem Einwand, lange Agentenläufe könnten vor allem kapitalkräftigen Entwicklern helfen, mit einer Behauptung über rapide sinkende KI-Kosten.
- [[2026-10-13-artificialanlys-2110081938140582085]] — Artificial Analysis berichtet am 13.10.2026 über `Fish Audio Drama 3 Preview`.
- [[2026-10-10-voxyz_ai-2109056129884123370]] — Vox empfiehlt längere Prompt-Caches für Subagents, die auf Builds oder Tests warten.
- [[2026-10-10-developers-using-gpt-6-openai-api]] — Der am 10.10.2026 archivierte OpenAI-Guide ergänzt die regionalen Verfügbarkeitsangaben gegenüber dem erfassten Stand vom 02.10.2026.
- [[2026-10-09-satyanadella-2108627923888754862]] — Satya Nadella stellt `Microsoft-Decision-1` für schnelle strukturierte Entscheidungen vor und nennt interne Tests sowie Vertriebskanäle.
- [[2026-10-09-openrouter-2108689756372775370]] — OpenRouter meldet `Microsoft-Decision-1` als verfügbar und nennt Preis, Kontextumfang und Microsoft-Benchmarkzahlen.
- [[2026-10-09-natebjones-thats-model-vs-effort-in-plain-english]] — Nate Jones erklärt Modellwahl und Effort als zwei getrennte Entscheidungen: Welches Fähigkeitsniveau braucht die Aufgabe, und wie viel Denkaufwand soll das gewählte Modell investieren?
- [[2026-10-08-voxyz_ai-haiku-subagents-und-opus-worker]] — Vox empfiehlt für Claude Code eine feste Rollenteilung: `Opus 5.5` plant und prüft, `Haiku 5.5` liest Code und recherchiert Dokumentation.
- [[2026-10-07-kimmonismus-2107894978332557756]] — Chubby meldet `Claude Haiku 5.5`: Nach Herstellerangaben liegen durchschnittliche Betriebskosten rund **75 % unter** `Haiku 4.5`.
- [[2026-10-07-artificialanlys-2107911905822351609]] — Artificial Analysis (AA) berichtet Modellmerkmale von `Claude Haiku 5.5`: adaptive thinking, Effort-Einstellungen, 1 Million Kontexttokens, Text-/Bildinput, Textoutput.
- [[2026-10-06-artificialanlys-2107467221421420919]] — Artificial Analysis (AA) berichtet `Mistral Large 4 Preview`: „Research Public Preview“ über Mistrals API, 1 Billion Parameter, 49 Milliarden aktiv, 512k Kontexttokens, Text-/Bildinput, Textoutput.
- [[2026-10-02-repo-farion1231-cc-switch]] — Im Klon von farion1231/cc-switch (Stand Commit `b9e96202`) beschreibt `src/i18n/locales/en.json` einen „Stack“-Modus: Du legst mehrere Anbieter an, und alle ihre Modelle erscheinen im Modellmenü von C
- [[2026-10-02-developers-using-gpt-6-openai-api]] — Die Entwicklerseite „Using GPT-6“ beschreibt die drei GPT-6-Modelle, neue API-Funktionen und Prompt-Bausteine für Astra.
- [[2026-10-01-artificialanlys-2105491868608004578]] — Artificial Analysis (Drittanbieter) misst am 01.10.2026 Kosten pro Intelligence-Index-Task für OpenAI-Modelle nach.
- [[2026-09-30-artificialanlys-2105392625788637299]] — Artificial Analysis (Drittanbieter-Messung, Intelligence Index v4.3.2 mit 10 Evaluations) bewertet am 30.09.2026 Googles Gemini 4 Argon mit `high` Reasoning, der höchsten verfügbaren Stufe.
- [[2026-09-29-voxyz_ai-2104919123918479521]] — Vox liefert einen Prompt, mit dem Claude Code das eigene Setup gegen Anthropics Leitfaden zu Sonnet 5.5 prüft ([[2026-09-28-claude-building-with-claude-sonnet-5-5-claude-dev-blog]]).
- [[2026-09-29-thsottiaux-2104823812042940713]] — Tibo (@thsottiaux, signiert „Codexingly“, also aus dem Codex-Umfeld bei OpenAI) kündigt am 29.09.2026 an, dass das Pro-$200-Abo am Folgetag wieder für Neukunden öffnet.
- [[2026-09-29-openai-rueckblick-auf-den-devday-2026]] — OpenAI fasst am 29.09.2026 mehr als 20 Ankündigungen zusammen.
- [[2026-09-29-artificialanlys-2105025585332605357]] — Artificial Analysis (Drittanbieter, Intelligence Index v4.3.2) misst `GPT-6.1 Sol`, das `GPT-6 Sol` nach sieben Tagen ablöst.
- [[2026-09-28-claude-building-with-claude-sonnet-5-5-claude-dev-blog]] — Der Herstellerleitfaden zu `claude-sonnet-5-5` (Stand 2026-09-28) behauptet: gleicher Token-Preis wie Sonnet 5, aber deutlich weniger Tokens pro Aufgabe, daher „bis zu 30 % weniger“ Kosten.
- [[2026-09-28-artificialanlys-2104640155843989864]] — Artificial Analysis (Drittanbieter) misst `Claude Sonnet 5.5` mit dem Intelligence Index v4.3.2 (zehn Evals, u.
- [[2026-09-25-voxyz_ai-2103586663393853636]] — Vox übersetzt Thariqs Tests (mehr Effort kaufe vor allem mehr Verifikation und Edge-Case-Tests) in zwei Subagents: ein builder auf `low`, ein verifier auf `high`.
- [[2026-09-25-trq212-2103576349499855160]] — Effort kauft Verifikationstiefe und übersehene Randfälle, keinen besseren Ansatz; ein stärkeres Modell auf High kann ein schwächeres auf Max bei halben Tokens einholen.
- [[2026-09-24-artificialanlys-2102932119995756613]] — Opus 5.5 in Claude Code führt den Coding Agent Index, kostet aber pro Task 21 Prozent mehr, weil der Tokenverbrauch die Preissenkung überkompensiert.
- [[2026-09-23-kimmonismus-2102748118400004100]] — Kimmonismus fasst eine Analyse von Epoch AI zusammen.
- [[2026-09-23-artificialanlys-2102833926788288704]] — Mehrere Effort-Stufen desselben Modells liegen als getrennte Punkte auf der Pareto-Front; die Effort-Wahl ist damit ein eigener Kostenhebel.
- [[2026-09-22-promptgefluester-ich-arbeite-mit-multiorgastation-und-das-hat-was-mit-meinem-tokenlimit]] — Ein Creator nennt aus Praxiserfahrung Hebel gegen aufgebrauchte Token-Limits.
- [[2026-09-22-kimmonismus-2102462091299098640]] — Kimmonismus gibt die Benchmarkvergleiche aus der OpenAI-Ankündigung zu `GPT-6 Sol` und `Luna` wieder.
- [[2026-09-22-epoch-the-plunging-price-of-thought]] — Epoch AI hat Kosten je Leistungsniveau auf fünf Benchmarks (FrontierMath Tier 1–3, OTIS Mock AIME, GPQA Diamond, Chess Puzzles, Mystery Game Puzzles) untersucht.
- [[2026-09-22-artificialanlys-2102462962758033624]] — GPT-6 Sol und Luna halbieren die Kosten bei etwa gleichem Score wie GPT-5.6; die bessere Halluzinationsrate stammt überwiegend aus mehr Verweigerung.
- [[2026-09-22-artificialanlys-2102438210798514391]] — Opus 5.5 führt den Intelligence Index bei niedrigerem Listenpreis, verbraucht aber mehr Tokens; maßgeblich sind Kosten pro Task, nicht der Preis pro Million Token.
- [[2026-09-20-avichawla-2101563610644496464]] — Avi Chawla zeigt, wie sich ein offenes LLM ohne Training als schnelle lokale Entscheidungsmaschine nutzen lässt, wenn die erlaubten Antworten vorab feststehen: Statt Text zu erzeugen, liest der Server
- [[2026-09-18-akshay_pachaar-2101037514945597645]] — Kleine Urteile in Agent-Schleifen brauchen kein generatives LLM: ein typisiertes, kalibriertes Entscheidungsmodell liefert Wahrscheinlichkeiten, Schwellen und Verzweigung bleiben im Code.
- [[2026-09-14-arena-2099606881845321841]] — Arena berichtet für `DeepSeek-V4.1-Flash (Max)` eine günstige Position auf der eigenen Pareto-Grenze.
- [[2026-08-14-claude-maximizing-the-value-of-your-claude-code-session]] — Tool-Outputs bleiben in jedem Folgeturn im Kontext, und Modell- oder Effort-Wechsel sowie Compact entwerten den Prompt Cache, daher Sitzungen aufgabenweise mit /clear führen.
- [[2026-08-07-theaicareercoach-vor-einem-jahr-noch-teuer-heute-fast-geschenkt-die-preise-fuer-ki]] — Ein Creator (Norman, Daten- und KI-Leiter einer Beratung) meldet Anfang August 2026 eine Preissenkung von OpenAI und nennt drei Treiber für sinkende Modellpreise.
- [[2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso]] — Trotz fallender Preise für festes Können bleibt das Limit gleich schnell leer, weil Kontextlänge, Denkstufe, Tokenizer, Subagents und Langläufer den Verbrauch pro Aufgabe erhöhen.
- [[2026-08-01-arena-2083348755559207047]] — Arena berichtet am 1.
- [[2026-07-31-kimmonismus-2083144340176609556]] — Der Post vom 31.
- [[2026-07-27-techfeed5-1-reason-why-the-cloud-limits-could-hit-directly-that-we-talk-to-opus-in]] — Der Token-Verbrauch hängt von der Sprache ab und Deutsch verbraucht bei Claude Opus laut Clip deutlich mehr als Englisch, allerdings ohne belegte Quelle und Methode.
- [[2026-07-27-cerebras-gpt-5-6-modellwahl-und-reasoning]] — Mit dem günstigsten tragfähigen Modell starten und bei Stillstand eskalieren, denn jede Reasoning-Stufe kostet rund 50 Prozent mehr bei sinkendem Grenznutzen; warme Sessions sparen Cache-Kosten.
- [[2026-07-25-valsai-2080817011157094511]] — Vals AI veröffentlicht am 25.
- [[2026-07-24-kimmonismus-2080751641393836085]] — Der Post vom 24.
- [[2026-07-24-artificialanlys-2080734447717298483]] — Artificial Analysis veröffentlicht am 24.
- [[2026-07-24-andrew_n_carr-2080727000004878593]] — Andrew Carr kommentiert am 24.
- [[2026-07-17-hedgeye-2078165516657549710]] — Hedgeye behauptet am 17.
- [[2026-07-16-kimmonismus-2077828228282982886]] — Chubby kommentiert am 16.
- [[2026-07-16-artificialanlys-2077832874183860404]] — Artificial Analysis beschreibt `Kimi K3` als leistungsfähiges Modell mit höheren Tokenpreisen als sein Vorgänger.
- [[2026-07-15-xudong07452910-2077246527756775933]] — Der Tweet fasst auf Chinesisch den Prompt-Guide von OpenAI zu GPT-5.6 Sol zusammen (Stand 2026-07-15) und zieht daraus eine Folgerung für `AGENTS.md`.
- [[2026-07-10-rasbt-2075573860796436626]] — Sebastian Raschka liest aus einem Chart des Artificial Analysis Coding Agent Index v1.1 Faustregeln für agentisches Coding ab: Statt auf die nächsthöhere Modellstufe zu wechseln, lohnt sich häufig das
- [[2026-07-10-matthewberman-2075597710435266674]] — @MatthewBerman gibt eine DeepSWE-Auswertung weiter und stimmt ihr zu, dass GPT-5.6 Sol in der Stufe `high` das beste Preis-Leistungs-Modell sei.
- [[2026-07-09-voxyz_ai-2075278546570801574]] — @Voxyz_ai argumentiert, dass bei niedrigen Preisen die Frage entfällt, ob eine Aufgabe das gute Modell wert ist.
- [[2026-07-09-kimmonismus-2075271465964798147]] — Der Post fasst den GPT-5.6-Launch zusammen und gibt Benchmark-Zahlen wieder.
- [[2026-07-09-artificialanlys-2075268970492657905]] — Artificial Analysis (AA) misst die drei GPT-5.6-Modelle im eigenen Intelligence Index v4.1 und im neuen Coding Agent Index.
- [[2026-07-08-claudedevs-modell-vs-effort]] — Bei schlechten Ergebnissen zuerst Input und Kontext prüfen, dann nach Fehlerbild entscheiden: übersprungene Arbeit braucht mehr Effort, gründlich erarbeitete Fehler ein anderes Modell.
- [[2026-05-01-mnilax-claude-code-overhead-9-patterns]] — Ein 90-Tage-Audit zeigt: 73 Prozent der Claude-Code-Tokens gehen in strukturellen Overhead wie große CLAUDE.md, Hooks, MCPs und Cache-Misses, nicht in Modellwahl.
- [[2026-04-29-wiki-compiler-claude-usage-limits-token-strategien]] — Tokenverbrauch wächst quadratisch mit der Nachrichtenzahl; kurze klar geschnittene Sessions und Modellwahl nach Aufgabenschwere senken Verbrauch und Limit-Druck.
- [[2026-03-29-0x-kaize-claude-usage-limits-primaer]] — Der Tokenverbrauch wächst in langen Chats quadratisch, weil der Verlauf neu eingelesen wird; kurze Chats, Haiku für Routine und Nutzung außerhalb der Peak Hours sparen Limit.
- [[2026-02-04-rudrank-using-minimax-with-claude-code]] — Claude Code lässt sich per drei Umgebungsvariablen auf jeden Anthropic-kompatiblen Provider umleiten; vorher alte Overrides löschen und Routing mit /status prüfen.
- [[2025-12-31-natebjones-seriously-not-worth-it-now]] — Vor jedem Fine-Tuning zuerst Instruktionen, Constraints und Evals als Harness ausreizen, da neue Modellgenerationen Trainingsprojekte schnell überholen.

## Quellen mit diesem Thema als Nebenthema

- [[2026-10-19-unslothai-2112212605930778830]]
- [[2026-10-17-developers-maintaining-software-with-the-gpt-6-family-opena]]
- [[2026-10-10-julian-ivanov-ki-automat-diese-10-claude-code-mods-solltest-du-unbedingt]]
- [[2026-10-07-unslothai-decision-model-finetuning]]
- [[2026-10-06-promptgefluester-vielleicht-mal-zur-begruendung-warum-ich-euch-zeig-wie-ich-280-website]]
- [[2026-10-02-repo-anthropics-skills]]
- [[2026-10-01-julian-ivanov-ki-automat-claude-code-ist-unglaublich-gut-in-motion-graphi]]
- [[2026-09-29-voxyz_ai-2105012597796057438]]
- [[2026-09-28-unslothai-2104592692072304916]]
- [[2026-09-28-claude-automating-eval-design-and-hillclimbing-with-cla]]
- [[2026-09-27-voxyz_ai-2104254744722383210]]
- [[2026-09-14-shadcn-2099534231114314145]]
- [[2026-09-09-voxyz_ai-2097814698204832116]]
- [[2026-09-01-ai-mit-arnie-lokale-ki-kauf-nicht-die-falsche-hardware]]
- [[2026-08-19-developer-evaluating-ai-agent-skill-performance-with-nvidi]]
- [[2026-08-16-floknowsai-in-einem-jahr-ersetzt-ein-lokales-modell-dein-claude-abo]]
- [[2026-07-31-unslothai-2083231049434435596]]
- [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]]
- [[2026-07-06-claudedevs-2074208949205881033]]
- [[2026-07-01-0xcodila-2072329149520232639]]
- [[2026-06-10-ai-news-strategy-daily-n-codex-vs-claude-code-stop-picking-one-here-s-wha]]
- [[2026-06-04-agenticjames-most-people-have-not-touched-the-best-parts-of-claude-code-skills-forked]]
- [[2026-05-09-zodchiii-15-claude-code-settings-most-developers]]
- [[2026-05-04-wiki-compiler-claude-session-und-token-management]]
- [[2026-04-22-alibaba-qwen-qwen3-6-27b-lokal-betreiben]]
- [[2026-02-14-minty-mastering-claude-code]]
- [[2026-02-02-unsloth-team-claude-code-local-llm]]
- [[2026-01-22-dr-cintas-claude-code-local]]
- [[2026-01-21-meta-alchemist-claude-skills-deep-dive]]
- [[2026-01-21-aiedge-claude-50-pro-tips]]
