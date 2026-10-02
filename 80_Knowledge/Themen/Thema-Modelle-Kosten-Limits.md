# Modelle, Kosten & Limits

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-02. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Modellwahl, Reasoning-Effort, Preise, Kosten pro Task, Usage Limits, Prompt Caching, Benchmarks, offene und lokale Modelle, Provider-Umleitung.

## Suchbegriffe

- **Hauptkeyword:** Claude Code Kosten
- **Long-Tail:** Claude Code Usage Limits; Kosten pro Task statt pro Token; Prompt Caching Claude Code; Claude Code mit lokalem Modell; Reasoning Effort wählen; Modell-Eskalation günstig nach teuer
- **Fragen:** Welches Modell für welche Aufgabe? / Warum sind meine Limits so schnell leer?
- **Häufig in den Quellen:** modell-eskalation (14), modell (11), kosten pro task (10), effort (10), gpt-6 (8), kosten (7), preis (6), opus 5.5 (6), token (5), anthropic_base_url (4), preise (4), /compact (4), sonnet (4), terminal-bench (4), prompt caching (3), modellwahl (3), artificial analysis intelligence index (3), limit (3), modellpreise (3), pareto-front (3)

## Verwandte Themen

- [[Thema-Kontext-Management]] — Kontext-Management
- [[Thema-Multi-Agent-Parallelisierung]] — Multi-Agent & Parallelisierung
- [[Thema-Autonome-Läufe-Loops-CI]] — Autonome Läufe, Loops & CI
- [[Thema-Rolle-Lernen-Markt]] — Rolle, Lernen & Markt

## Patterns (4)

- [[Entscheidung-per-Scoring-statt-Generierung]] · meinung · 3 Belege
- [[Lokale-Modell-Umleitung-Muster]] · mehrfach-belegt · 8 Belege
- [[Modell-Eskalation-von-guenstig-nach-teuer]] · mehrfach-belegt · 36 Belege
- [[Trainingsdaten-Dichte-als-Stack-Kriterium]] · meinung · 2 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Action-Space-Design-nach-Modellfaehigkeit]], [[Kontext-Hygiene-Entscheidungsbaum]], [[Kontrollierte-Agent-Parallelisierung]]

## Quellen (37)

- [[2026-10-02-repo-farion1231-cc-switch]] — Im Klon von farion1231/cc-switch (Stand Commit `b9e96202`) beschreibt `src/i18n/locales/en.json` einen „Stack“-Modus: Du legst mehrere Anbieter an, und alle ihre Modelle erscheinen im Modellmenü von C
- [[2026-10-01-artificialanlys-2105491868608004578]] — Artificial Analysis (Drittanbieter) misst am 01.10.2026 Kosten pro Intelligence-Index-Task für OpenAI-Modelle nach.
- [[2026-09-30-artificialanlys-2105392625788637299]] — Artificial Analysis (Drittanbieter-Messung, Intelligence Index v4.3.2 mit 10 Evaluations) bewertet am 30.09.2026 Googles Gemini 4 Argon mit `high` Reasoning, der höchsten verfügbaren Stufe.
- [[2026-09-29-voxyz_ai-2104919123918479521]] — Vox liefert einen Prompt, mit dem Claude Code das eigene Setup gegen Anthropics Leitfaden zu Sonnet 5.5 prüft ([[2026-09-28-claude-building-with-claude-sonnet-5-5-claude-dev-blog]]).
- [[2026-09-29-thsottiaux-2104823812042940713]] — Tibo (@thsottiaux, signiert „Codexingly“, also aus dem Codex-Umfeld bei OpenAI) kündigt am 29.09.2026 an, dass das Pro-$200-Abo am Folgetag wieder für Neukunden öffnet.
- [[2026-09-29-openai-rueckblick-auf-den-devday-2026]] — OpenAI fasst am 29.09.2026 mehr als 20 Ankündigungen zusammen.
- [[2026-09-29-artificialanlys-2105025585332605357]] — Artificial Analysis (Drittanbieter, Intelligence Index v4.3.2) misst `GPT-6.1 Sol`, das `GPT-6 Sol` nach sieben Tagen ablöst.
- [[2026-09-28-unslothai-2104592692072304916]] — Unsloth kündigt am 28.09.2026 an, dass sich das Decision-Modell „Laya“ (laut Guide eine offene Jev-Alternative) lokal über Unsloth Desktop betreiben lässt, auf CPU, Mac, Windows, Linux und GPU.
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
- [[2026-08-16-floknowsai-in-einem-jahr-ersetzt-ein-lokales-modell-dein-claude-abo]] — Speicherbedarf und Tempo lokaler Modelle lassen sich mit einfachen Faustformeln aus Parametern, Quantisierung und Speicherbandbreite vorab abschätzen; Kontext und KV-Cache fehlen dabei.
- [[2026-08-14-claude-maximizing-the-value-of-your-claude-code-session]] — Tool-Outputs bleiben in jedem Folgeturn im Kontext, und Modell- oder Effort-Wechsel sowie Compact entwerten den Prompt Cache, daher Sitzungen aufgabenweise mit /clear führen.
- [[2026-08-07-theaicareercoach-vor-einem-jahr-noch-teuer-heute-fast-geschenkt-die-preise-fuer-ki]] — Ein Creator (Norman, Daten- und KI-Leiter einer Beratung) meldet Anfang August 2026 eine Preissenkung von OpenAI und nennt drei Treiber für sinkende Modellpreise.
- [[2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso]] — Trotz fallender Preise für festes Können bleibt das Limit gleich schnell leer, weil Kontextlänge, Denkstufe, Tokenizer, Subagents und Langläufer den Verbrauch pro Aufgabe erhöhen.
- [[2026-07-27-techfeed5-1-reason-why-the-cloud-limits-could-hit-directly-that-we-talk-to-opus-in]] — Der Token-Verbrauch hängt von der Sprache ab und Deutsch verbraucht bei Claude Opus laut Clip deutlich mehr als Englisch, allerdings ohne belegte Quelle und Methode.
- [[2026-07-27-cerebras-gpt-5-6-modellwahl-und-reasoning]] — Mit dem günstigsten tragfähigen Modell starten und bei Stillstand eskalieren, denn jede Reasoning-Stufe kostet rund 50 Prozent mehr bei sinkendem Grenznutzen; warme Sessions sparen Cache-Kosten.
- [[2026-07-08-claudedevs-modell-vs-effort]] — Bei schlechten Ergebnissen zuerst Input und Kontext prüfen, dann nach Fehlerbild entscheiden: übersprungene Arbeit braucht mehr Effort, gründlich erarbeitete Fehler ein anderes Modell.
- [[2026-05-01-mnilax-claude-code-overhead-9-patterns]] — Ein 90-Tage-Audit zeigt: 73 Prozent der Claude-Code-Tokens gehen in strukturellen Overhead wie große CLAUDE.md, Hooks, MCPs und Cache-Misses, nicht in Modellwahl.
- [[2026-04-29-wiki-compiler-claude-usage-limits-token-strategien]] — Tokenverbrauch wächst quadratisch mit der Nachrichtenzahl; kurze klar geschnittene Sessions und Modellwahl nach Aufgabenschwere senken Verbrauch und Limit-Druck.
- [[2026-04-22-alibaba-qwen-qwen3-6-27b-lokal-betreiben]] — Ein offenes 27B-Modell erreicht laut Herstellerchart im Agentic Coding etwa den Stand eines Vorjahres-Frontiermodells; lokaler Betrieb ist eine Speicher- und Bandbreitenfrage.
- [[2026-03-29-0x-kaize-claude-usage-limits-primaer]] — Der Tokenverbrauch wächst in langen Chats quadratisch, weil der Verlauf neu eingelesen wird; kurze Chats, Haiku für Routine und Nutzung außerhalb der Peak Hours sparen Limit.
- [[2026-02-04-rudrank-using-minimax-with-claude-code]] — Claude Code lässt sich per drei Umgebungsvariablen auf jeden Anthropic-kompatiblen Provider umleiten; vorher alte Overrides löschen und Routing mit /status prüfen.
- [[2026-02-02-unsloth-team-claude-code-local-llm]] — Claude Code und Codex CLI laufen komplett lokal gegen einen llama.cpp-Server, wenn die Basis-URL oder der Provider auf den lokalen Endpunkt zeigt.
- [[2026-01-22-dr-cintas-claude-code-local]] — Über drei Umgebungsvariablen lässt sich Claude Code auf einen lokalen Ollama-Server umleiten, ohne die CLI selbst zu ändern.
- [[2025-12-31-natebjones-seriously-not-worth-it-now]] — Vor jedem Fine-Tuning zuerst Instruktionen, Constraints und Evals als Harness ausreizen, da neue Modellgenerationen Trainingsprojekte schnell überholen.

## Quellen mit diesem Thema als Nebenthema

- [[2026-10-02-repo-anthropics-skills]]
- [[2026-10-01-julian-ivanov-ki-automat-claude-code-ist-unglaublich-gut-in-motion-graphi]]
- [[2026-09-29-voxyz_ai-2105012597796057438]]
- [[2026-09-28-claude-automating-eval-design-and-hillclimbing-with-cla]]
- [[2026-09-27-voxyz_ai-2104254744722383210]]
- [[2026-09-09-voxyz_ai-2097814698204832116]]
- [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]]
- [[2026-06-04-agenticjames-most-people-have-not-touched-the-best-parts-of-claude-code-skills-forked]]
- [[2026-05-09-zodchiii-15-claude-code-settings-most-developers]]
- [[2026-05-04-wiki-compiler-claude-session-und-token-management]]
- [[2026-02-14-minty-mastering-claude-code]]
- [[2026-01-21-meta-alchemist-claude-skills-deep-dive]]
- [[2026-01-21-aiedge-claude-50-pro-tips]]
