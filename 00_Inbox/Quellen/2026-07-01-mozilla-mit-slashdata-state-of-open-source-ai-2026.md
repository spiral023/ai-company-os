---
url: https://stateofopensource.ai/state-of-open-source-ai-v1-0-1.pdf
titel: "State of Open Source AI 2026 (Mozilla): Der Harness ist die neue Frontier"
autor: "Mozilla mit SlashData"
datum: 2026-07-01
erfasst: 2026-08-04
typ: url
quelle: vibedeck
sekundaerquelle: true
status: neu
beschreibung: "Mozillas erster Report zum Stand offener KI: Der Fähigkeitsabstand schrumpft auf einen Release-Zyklus, offene Modelle routen ein Drittel aller Tokens – und der Engpass verschiebt sich auf Orchestrierung, Memory und Permission."
vibedeck_category: fundamentals
vibedeck_level: advanced
vibedeck_tags:
  - "fundamentals/open-source-ai"
  - "open-weights"
  - "agentic-harness"
  - "marktanalyse"
  - "tooling/mcp"
  - "ai-agents"
vibedeck_topics:
  - "[[Open Weights]]"
  - "[[Agentic Harness]]"
  - "[[MCP]]"
  - "[[Portable Permission]]"
  - "[[Agent Memory]]"
  - "[[AI Souveränität]]"
---

# State of Open Source AI 2026 (Mozilla): Der Harness ist die neue Frontier

> Sekundärquelle: aus vibedeck übernommene deutsche Aufarbeitung (`src/content/knowledge/state-of-open-source-ai-2026.md`). Primärquelle: https://stateofopensource.ai/state-of-open-source-ai-v1-0-1.pdf

> Quelle: Mozilla mit SlashData, *The State of Open Source AI — An Inaugural Mozilla Assessment*, Volume 1.01, Juli 2026 (Redaktionsstand 30. Juni 2026). 65 Seiten, 5 Sektionen plus Appendix.

## Kernthese in drei Sätzen

Offene Modelle haben den Fähigkeitsrückstand auf ungefähr einen Release-Zyklus verkürzt und routen inzwischen rund ein Drittel aller Tokens — die Modellfrage ist damit praktisch entschieden. Der Engpass hat sich eine Ebene nach oben verlagert: auf den **Harness**, also Orchestrierung, Memory, Sandboxes, Tools und vor allem das Permission-Modell. Genau dort entscheidet sich in den nächsten Quartalen, ob Open Weights auch wirklich deploybar bleiben — oder ob geschlossene Plattformen Modell und Scaffold zu einem gemieteten Gesamtprodukt verschweißen.

Der Report ist bewusst als Momentaufnahme angelegt (Leaderboards und Preise verschieben sich innerhalb von Tagen) und mischt harte Fremdquellen mit zwei eigenen, ausdrücklich **ordinalen** Bewertungen (Stack-Heatmap, Funding-Maturity).

---

## 01 · Der aktuelle Stand: Capability, Cost, Adoption

### Der Fähigkeitsabstand ist auf einen Release-Zyklus geschrumpft

| Messung | Bestes offenes Modell | Closed Frontier | Abstand |
|---|---|---|---|
| Artificial Analysis Intelligence Index v4.1 | Kimi K3 · 57 (Rang 4 von 586) | Claude Opus 5 · 61 | 4 Punkte |
| Epoch Capabilities Index (Juli 2026) | Kimi K3 · 156 | GPT-5.6 Sol · 162 | 6 Punkte, **Konfidenzintervalle überlappen** |

Kimi K3 liegt im AA-Index vor Opus 4.8, GPT-5.6 Terra, Grok 4.5 und Sonnet 5. Drei der elf Top-Modelle liefern offene Gewichte. Bemerkenswert an den ECI-Daten: Alle gelisteten Modelle wurden zwischen April und Juli 2026 veröffentlicht — Frontier-Führung verhält sich weniger wie ein dauerhafter Vorsprung als wie eine Position, die jeden Release-Zyklus neu vergeben wird. Der Abstand setzt sich zurück statt sich aufzuaddieren.

Die Entwicklung in vier Stufen: 2023 Llama 2 (Qualitätsprobleme, gescheiterte Fine-Tunings, Rückkehr zu GPT-4) → 2024 Llama-3-Ära (echte Alternative) → 2025 DeepSeek-Ära (Near-Parity, starke Ökonomie) → 2026 Produktionsmaßstab.

### Die Frontier ist „jagged" — drei Zonen statt einer Linie

- **Open führt oder Parität — Frontend-Coding:** K3 debütierte als Nr. 1 in LMArenas Frontend Code Arena (1679 Elo), erster in sechs von sieben Frontend-Domänen, plus Coding, Instruction-Following, General Knowledge.
- **Umkämpft — agentische Terminal-Arbeit:** K3 88,3 vs. Sol 88,8 auf Terminal-Bench 2.1; K3 gewinnt Program Bench, SpreadsheetBench 2, BrowseComp — verliert FrontierSWE mit 81,2 gegen Fable 5 (86,6).
- **Closed-Vorsprung — professionelle Wissensarbeit:** Fable 5 führt auf GDPval-AA v2 mit 92 Elo Abstand (die größte Elo-Trennung aller gemeinsamen Benchmarks), plus Long-Context-Treue und konversationelle Politur (Moonshot räumt schwächere UX selbst ein).

Praktische Konsequenz: Wer Modell und Aufgabe passend zuordnet, braucht die Frontier für deutlich weniger Workloads als angenommen.

### Preise: 50× in 36 Monaten

Der günstigste Anbieter auf GPT-4-Niveau fiel von 20 $ auf 0,40 $ pro 1M Tokens (112× gerechnet ab GPT-4s Launch-Preis von 45 $). Zum Vergleich: Die historische PC-Compute-Kurve hätte im selben Zeitraum 3,4× geliefert, die Dotcom-Bandbreitenkurve 2,6×. Der größte Einzelsprung ging auf Open Weights zurück — Llama 3.1 drückte den Boden auf 0,88 $ (11× in einem Quartal), DeepSeek-V3 folgte mit 0,69 $.

Das prägnanteste Einzelbeispiel bleibt DeepSeek-R1 (Januar 2025, MIT-Lizenz) gegen OpenAI o1-1217: MATH-500 97,3 % vs. ~97 %, AIME 2024 79,8 % vs. ~79 % — bei 0,55 $/2,19 $ gegen 15 $/60 $ pro 1M Tokens. Rund **27× Preisunterschied bei nahezu identischen Reasoning-Scores**. Im April 2026 erweiterte DeepSeek-V4 Pro auf 1,6T Parameter und 1M Kontext bei 0,435 $/M Input.

### Nutzung: Open dominiert die Tokens, Closed die Requests

- Open-Weight-Anteil an allen auf OpenRouter gerouteten Tokens: ~2 % (Nov 2024) → ~33 % (Nov 2025) → weiter steigend (Jun 2026).
- Juli 2026: Die **sieben volumenstärksten Modelle liefern alle offene Gewichte** — MiMo-V2.5 (Xiaomi) 32,3T Tokens/17,8 %, DeepSeek V4 Flash 24,0T/13,3 %, Hy3 free (Tencent) 19,4T/10,7 %, MiniMax M3 15,0T, GLM 5.2 13,5T, DeepSeek V4 Pro 11,9T, Nemotron 3 Ultra 9,02T. Auf den Rängen 1–10 stehen 72,4 % offene gegen 8,7 % geschlossene Tokens.
- Nach Monats-Tokens: chinesisch gebaut und offen ~82T gegen US-amerikanisch und geschlossen ~23T — mehr als 3,5:1.
- Nach **Request-Zahl** führen geschlossene US-Anbieter weiter: Google allein 28,7 %, Anthropic plus OpenAI ~20 %. Der offene Vorsprung konzentriert sich auf token-intensive Coding- und Agent-Workloads — also dort, wo das Geld liegt.

Wichtige Einschränkung durchgängig: Es handelt sich nur um gerouteten Traffic, First-Party-Nutzung (ChatGPT, Gemini, Doubao) ist ausgeschlossen. Kimi K3 fehlt in der Juli-Statistik komplett, weil API (16.7.) und Gewichte (27.7.) nach dem Messfenster kamen.

### Deployability trennt sich von Verfügbarkeit

Frontier-Fähigkeit ist herunterladbar — aber die Zahl benötigter GPU-Nodes entscheidet, wer sie tatsächlich betreiben kann. Die Deployability-Linie liegt bei **einem 8-GPU-Node**:

| Modell | Footprint | Nodes |
|---|---|---|
| Kimi K3 (Moonshot, CN) | ~1,4 TB, native MXFP4, 64+ Accelerators | ≈ 8 Nodes |
| Inkling (Thinking Machines, US) | ≥600 GB, NVFP4, Apache 2.0 | 1 Node |
| GLM 5.2 / K2.7-Klasse | ~577 GB, INT4 | 1 Node |

Das heißt: Das offene Frontier-Modell und das *deploybare* offene Frontier-Modell sind seit Juli 2026 nicht mehr dasselbe.

### Wo Teams hängenbleiben — der Funnel

| Stufe | Wert |
|---|---|
| Firmen, die offene Komponenten nutzen | 89 % |
| Entwickler, die offene Modelle nutzen | 79 % |
| Offene Modelle, die Produktion erreichen | **51 %** |
| Geschlossene Modelle, die Produktion erreichen | **63 %** |
| Deployments mit Vendor-Partner in Produktion | 67 % |
| Rein interne Builds in Produktion | 33 % |
| Enterprise-Pilots mit messbarem finanziellem Effekt | **5 %** |

Und — das ist der stärkste Befund der Sektion — **Größe löst das Problem nur für Closed**:

| Organisationsgröße | Closed in Produktion | Open in Produktion |
|---|---|---|
| Klein (2–50) | 54 % | 53 % |
| Mittel (51–1.000) | 66 % | 55 % |
| Enterprise (1.001+) | 73 % | 57 % |

Wäre die Lücke eine Ressourcenfrage, würde Skalierung sie schließen. Tut sie nicht. Closed-Deployment ist ein Problem, das Geld löst; Open-Deployment ist ein Problem, das das Ökosystem fertigbauen muss.

### Was Entwickler abwandern lässt

Top-Blocker insgesamt: Infrastruktur-/Compute-Kosten 27 %, Security/Privacy/Compliance 26 %, laufende Wartung 24 %, Deployment-Komplexität 23 %. Interessanter ist die Differenz zwischen aktuellen und abgewanderten Open-Nutzern (Δ in Prozentpunkten): Modell-Performance nicht ausreichend **+12 pp**, laufende Wartung **+11 pp**, Integration in bestehende Systeme **+11 pp**, Dokumentation **+9 pp**, Deployment-Komplexität und Modellvergleich je **+8 pp**. Fehlender Spezialsupport liegt bei −2 pp, ist also kein Abwanderungsgrund.

Regional sind die Probleme bemerkenswert gleichförmig. Auffällig: Südasien nennt Security/Compliance mit 39 % weit überdurchschnittlich; „keine größeren Probleme" sagen 21 % in Nordamerika, aber nur 4 % in Südamerika. Ozeanien (n=39) und Osteuropa/CIS (n=98) liegen unter der Reliabilitätsschwelle.

### Die Stack-Heatmap: stark in Capability, schwach in Operations

Mozillas eigene Bewertung von 9 Stack-Layern gegen 9 Kriterien (1–5, 48 Subkomponenten, 1.361 Projekte):

- **Stärkste Kriterien:** Community 4,00 · Ease of Adoption 3,63 · Production Readiness 3,54
- **Schwächste Kriterien:** Standardization 2,83 · Enterprise Readiness 2,79 — und diese zwei kalten Spalten wiederholen sich über *jeden* Layer
- **Stärkste Layer:** Model Code 3,96 · Model Weights 3,67 · Infrastructure 3,48
- **Schwächste Layer:** Agent Layer 3,04 · Safeguards 2,64 (Standardization dort nur 1,6)

Die Operationslücke ist damit exakt benannt: Standardisierung plus Enterprise-Readiness. Eine erwähnenswerte Bewegung: Infrastructure-Standardisierung stieg von 3,1 auf 3,4, weil KDA-artige Linear Attention die Runtime-Kompatibilität brach (Gewichte laden garantierte kein Serving mehr) und Moonshot das upstream löste, indem es KDA-Prefix-Caching an vLLM beisteuerte. Das stärkt den Standard — und konzentriert gleichzeitig Einfluss darüber. Offene Frage des Reports: Landet die nächste divergente Architektur auch upstream, oder forkt sie den Serving-Layer?

---

## 02 · Wer darauf wettet: Kapital, Firmen, Ökonomie

### Open Weights ist ein Geschäftsmodell

| Firma | Kennzahl | Kapitalseite |
|---|---|---|
| Databricks | 5,4 Mrd. $ Revenue-Run-Rate, >65 % YoY | erwägt Runde bei 165 Mrd. $+ |
| Mistral | 400 Mio. $ ARR, 20× in zwölf Monaten | Gespräche über 3 Mrd. € bei 20 Mrd. € |
| DeepSeek | 220 Mio. $ ARR (Mitte 2025), überwiegend API und Enterprise | 7,4 Mrd. $ bei 50 Mrd. $+ |

Fünf Revenue-Modelle gelten als skaliert belegt: Hosted Inference, Enterprise-Plattformen, On-Prem-Lizenzierung, Fine-Tuning-Services und Harness-Tooling.

### Entwickler nutzen Open breiter — aber nicht als Ersatz

5,1 Use Cases pro Entwickler bei offenen Modellen gegen 4,6 bei geschlossenen; Open führt in jeder erhobenen Kategorie. 79 % nutzen offene, 71 % geschlossene Modelle. 78 % kombinieren spezialisierte, task-optimierte offene Modelle neben oder anstelle generalistischer. Die Kombination ist der Normalfall: **50 % nutzen beides**, 29 % nur Open, 21 % nur Closed.

### Wo das Kapital liegt — und wo Löcher sind

Offengelegte Gesamtfinanzierung (Mio. $): DeepSeek 7.400 · Moonshot AI 3.900 · Mistral AI 3.050 · Reflection AI 2.130 · Cerebras 2.100 · Thinking Machines Lab 2.000 · Cohere 1.700 · Together AI 1.334 · Baseten 585 · Black Forest Labs 450 · Hugging Face 400 · Fireworks AI 327. Dazu Anyscale 281, LangChain 260, Stability 230 sowie Zhipu und MiniMax mit Hongkong-IPOs 2026.

Alle sechs größten Tech-Konzerne sind beteiligt — Microsoft (Mistral), Amazon (Hugging Face), NVIDIA (sieben Beteiligungen plus eigenes Nemotron), Google (HF plus Gemma), IBM (HF plus Granite), Meta (Llama). Größte offengelegte Runden: ASML → Mistral 1.400 Mio. $, Tencent → DeepSeek 1.400 Mio. $, CATL → DeepSeek 700 Mio. $, Schwarz Group → Cohere/Aleph Alpha 600 Mio. $.

Die Konsolidierung läuft bereits: CoreWeave → Weights & Biases (1.700 Mio. $), Databricks → MosaicML (1.300), Nvidia → Run:ai (700), AMD → Silo AI (665), Nvidia → Gretel (320) und OctoAI (165), Rubrik → Predibase (100–500), Cohere → Aleph Alpha (April 2026).

**Das strukturelle Loch:** Nach Mozillas Funding-Intensitätsmatrix (0–3 je Layer und Kapitaltyp) sind Foundation Models, Inference/Serving und Compute gut kapitalisiert. Data/Datasets sowie Safety/Eval/Governance — zusammen der Trust-Layer — bekommen praktisch kein privates VC und keine Revenue, sondern laufen allein auf Philanthropie und Staatsgeld.

### Das metered Modell bricht bei Skalierung

Drei dokumentierte Kollisionen mit Token-Pricing:

- **Microsoft** kündigt die meisten Claude-Code-Lizenzen zum 30. Juni 2026 — Token-Billing verbrauchte das Jahres-AI-Budget der Division in Monaten. Bis Juni prüfte Microsoft Azure-gehostetes DeepSeek V4 für die schwerste Copilot-Last: der größte Softwarekonzern der Welt umgeht den Zähler seines eigenen Partners.
- **Uber:** Coding-Budget 2026 nach vier Monaten erschöpft; Engineers verursachten 500–2.000 $ pro Monat, bevor bei 1.500 $ pro Tool pro Mitarbeiter gedeckelt wurde.
- **Stripe:** Inferenzkosten um 73 % gesenkt (Kostenindex 1,00 → 0,27) — 50 Mio. API-Calls täglich über vLLM mit einem Drittel der GPU-Flotte, als planbare Fixkosten im eigenen Besitz.

Der gemeinsame Auslöser: eine Umstellung auf Usage-based Pricing, die die Kontrolle über die Unit Economics beim Anbieter statt beim Kunden konzentriert. Wenn ein Werkzeug zu nützlich ist, um es zu rationieren, wird das Besitzen der Ökonomie wichtiger als das Mieten.

### Ein Fünftel der Nutzung, 4 % des Umsatzes

Auf OpenRouter (Mai–Sep 2025) stand offen für ~20 % der Nutzung, aber nur ~4 % des Umsatzes — geschlossene Modelle ~80 % Nutzung und ~96 % Umsatz. Treiber sind ~6× höhere Preise pro Call bei ~90 % Capability-Parität: also Preis, nicht Fähigkeit. Die Linux Foundation schätzt daraus **24,8 Mrd. $ nicht realisierte Jahresersparnis**. 30 % der Entwickler nennen niedrigere Kosten, 28 % Privacy als Hauptgrund für Open. Wertschöpfung sitzt damit systematisch höher im Stack als die Nutzung.

---

## 03 · Warum es überall passiert: Optionalität, Souveränität, Politik

### Open ist Optionalität, nicht Ideologie

Die Cloud-Ära hat dasselbe Experiment schon durchlaufen: proprietäre APIs plus Data Gravity machten den Ausstieg teuer. Belege: 90–120 Tsd. $ für 1 PB Egress aus AWS S3 · ~80 % der Unternehmen repatriieren laut IDC inzwischen Workloads · GEICOs Cloud-Kosten lagen 2,5× über Erwartung · 37signals rechnet mit 10 Mio. $+ Fünfjahresersparnis nach dem Ausstieg. Geschlossene Modell-APIs reproduzieren dieselbe Falle: Der Anbieter kontrolliert Preise, es gibt keinen saubereren Migrationspfad, Preisänderungen erbt man mit.

### Die neunzehn Tage (Juni–Juli 2026)

Der eindrucksvollste Abschnitt des Reports macht Optionalität konkret:

| Datum | Ereignis |
|---|---|
| 9. Juni | Anthropic veröffentlicht Fable 5 und Mythos 5 |
| 12. Juni | Das Commerce Department verhängt sofort wirksame Exportkontrollen: kein Zugang für Foreign Nationals — innerhalb oder außerhalb der USA, inklusive Anthropics eigener Mitarbeiter. Da Nationalität nicht in Echtzeit prüfbar ist, gehen **beide Modelle für alle dunkel** |
| 26. Juni | Teilfreigabe: Mythos für ~100 geprüfte US-Organisationen kritischer Infrastruktur |
| 30. Juni | Kontrollen aufgehoben |
| 1. Juli | Fable 5 global wieder verfügbar — neunzehn Tage nach der Abschaltung |
| 16. Juli | Moonshot öffnet die K3-API: ein Frontier-Modell auf einem Release-Pfad, den kein Exportbescheid mehr erreicht, sobald die Gewichte draußen sind |

Die Pointe ist die Asymmetrie der Reversibilität: Zugang kann entzogen und wiederhergestellt werden, eine Gewichts-Veröffentlichung nicht mehr zurückgenommen werden. Sechs Wochen später zeigte derselbe Hebel in die andere Richtung — und fand keinen Griff.

Genau darauf zielt auch die Sanktionsdebatte: Treasury-Secretary Bessent kündigte am 21. Juli an, chinesische Open-Source-Modelle auf IP-Diebstahl zu prüfen und Sanktionen zu erwägen. Fünf Instrumente sind in Prüfung (Entity List, Beschaffungsgrenzen, Security Advisories, Haftungsanforderungen, öffentlicher Druck). Das Problem: Sanktionen brauchen einen durchsetzbaren Chokepoint. Sobald Gewichte über viele Jurisdiktionen verteilt heruntergeladen sind, existiert keiner mehr.

### China dominiert die Verbreitung

Kumulative Hugging-Face-Downloads (März 2026): **Qwen 942 Mio. gegen Llama 476 Mio.** — im Februar 2026 übertraf Qwen die nächsten acht Organisationen zusammen. Chinesische Open-Weight-Modelle auf OpenRouter: <2 % (Ende 2024) → >45 % (April 2026), und 61 % des Traffics unter den zehn meistgenutzten Modellen. 26.000+ DeepSeek-Enterprise-Accounts, präsent in 58 % neuer AI-Startup-Stacks 2025.

Die Vorbehalte nennt der Report explizit — Opazität der Trainingsdaten, hartkodierte Refusals — und beschreibt die Auflösung als architektonisch: Mindestens acht Jurisdiktionen verbieten die gehostete App; Unternehmen übernehmen die Gewichte trotzdem, selbst gehostet oder über westliche Endpoints.

### Offene Proliferation als chinesische Außenpolitik

Aus der Binnendirektive („AI Plus" plus 15. Fünfjahresplan) wurde im Juli 2026 eine internationale Institution: Xis erste WAIC-Keynote stellte Open Source ins Zentrum, **WAICO** startete mit 29 Gründungsstaaten und Sitz in Shanghai — darunter Russland, Pakistan, Indonesien, Kasachstan, Brasilien, Südafrika, aber **keine große westliche Demokratie**. Der Mechanismus ist ökonomisch elegant: Gewichte freigeben → Inferenz auf die lokale Hardware der Nutzer auslagern → keine Serving-Kosten, keine Exportfläche, kein sanktionierbarer Chokepoint. Als Juli-Exponat diente K3, „das erste offene Modell der 3T-Klasse", auf der WAIC angekündigt und am 27. Juli publiziert. Als Verteilungsschienen kommen 5.000 zugesagte AI-Trainingsplätze für Entwicklungsländer über fünf Jahre und geplante Kooperationszentren mit ASEAN, Arabischer Liga, Afrikanischer Union und BRICS. Chinesische Modelle stehen bei 46,4 % der gerouteten OpenRouter-Tokens gegen 35,7 % aus den USA.

Mozillas Bewertung dazu ist unmissverständlich und wird in Wette 5 aufgegriffen: Ein Commons mit einem einzigen Ursprung hört auf, ein Commons zu sein.

### Europa, Kanada, Indien, global

- **Europa** behandelt offene Gewichte als Industriepolitik: Februar 2025 Frankreich mit 109 Mrd. € für AI-Infrastruktur · August 2025 gezielte AI-Act-Ausnahmen für qualifizierte Open-Source-Systeme · Juni 2026 EUROPA-Award für ein souveränes 400B-Parameter-Modell über alle 24 EU-Sprachen · Juli 2026 Portugals vollständig offenes LLM „Amália" für 5,5 Mio. € und Deutschlands Open-Sourcing seiner Verwaltungs-KI-Plattform SPARK. Von der Leyen: „Wir können es uns nicht leisten, bei den Technologien, die unsere Krankenhäuser am Laufen halten, von anderen abhängig zu sein."
- **Kanada:** 890 Mio. $ für einen souveränen öffentlichen AI-Supercomputer; „AI for All" (Juni 2026) mit expliziter „Sovereign Foundation" als einer von sechs Säulen. Cohere veröffentlichte Command A+ (Mai 2026), ein 218B-MoE für agentische Enterprise-Aufgaben, das auf zwei H100 läuft.
- **Indien:** 38.231 subventionierte GPUs bei etwa ₹65/Stunde (~40 % unter Markt) · 5 Mio.+ neue GitHub-Entwickler allein 2025 auf 21,9 Mio., die schnellstwachsende Basis weltweit · IndiaAI-Mission mit ₹10.372 Cr und 600 geplanten Data Labs · 13,6 % der monatlich aktiven DeepSeek-Nutzer, nach China der zweitgrößte Anteil.
- **Global:** 70+ nationale AI-Strategien; größte offengelegte Infrastruktur-Commitments Saudi-Arabien/Humain 77 Mrd. $, Südkorea 71,5 Mrd. $ über fünf Jahre, UAE/G42–Microsoft 15,2 Mrd. $. 80+ Jurisdiktionen mit AI-Politik, 47 Nationen beschränken ausländische Verarbeitung kritischer Workloads. Die strategische Frage hat sich verschoben — nicht mehr *ob* ein Land AI-Politik betreibt, sondern *welche Stack-Ebene* es besitzen kann.

---

## 04 · Der Harness ist die neue Frontier

### Die Analogie

Der agentische Harness ist ein weiterer User Agent: Code auf der Seite des Nutzers, der in dessen Auftrag mit der Welt verhandelt — eine Ebene über dem Browser. Er umfasst Orchestrierungsloop, Tools, Memory, Sandboxes und Permission-Modell, also genau die Schicht, in der sich die Produktionsschwierigkeit konzentriert. Das ist längst eine Produktkategorie: LangChain mit 126.000+ GitHub-Stars und ~60 % Entwickleranteil bei Orchestrierung, 97 Mio. monatliche MCP-SDK-Downloads, 10.000+ aktive Server im ersten Jahr. Der Markt konsolidiert nach oben zu Meta-Harnesses (etwa Databricks' open-gesourctes Omnigent), die separate Agent-Ökosysteme unter einer Governance-Ebene kapseln.

Die Market Map von unten nach oben: **Modell** (offen oder geschlossen, austauschbar, Preis tendiert gegen null) → **Control** (LangGraph, CrewAI, AutoGen, LlamaIndex) → **Reach** (MCP, A2A, Memory: Mem0, Letta, Zep) → **Action** (Sandboxes E2B/Daytona/Modal, Eval Langfuse/Phoenix, und Permission & Identity als *ungelöste Lücke*) → **Surface** (AG-UI/A2UI, Payment x402/AP2/UCP) → **Govern** (Stateful Policy, Registry & Lineage, Budget & Revocation). Orchestrierung und Memory sind open-geführt, Interop läuft auf offenen Standards, Sandboxes und Evaluation sind gemischt — Permission ist die jüngste und am wenigsten standardisierte Kategorie.

### Der Harness zählte mehr als eine Modellgeneration — acht Wochen lang

| Messung | Werte | Spread |
|---|---|---|
| Terminal-Bench 2.0 (Mai 2026) | Fremd-Scaffold mit Anthropic-Gewichten 79,8 % vs. Claude Code mit *denselben* Gewichten 58,0 % | **21,8 Punkte** |
| Terminal-Bench 2.1 (acht Wochen später) | Codex CLI/GPT-5.5 83,4 % · Claude Code/Fable 5 83,1 % · bester unabhängiger Harness mit Fable-Gewichten 80,4 % | **~3 Punkte** |

Sobald die Labs den Harness ins Haus holten, komprimierte sich der Vorsprung — und auf jedem Modell, wo beide auftreten, gewinnt der Harness des jeweiligen Labs. Der Score ist eine Eigenschaft des *Paares*, nicht des Modells: DeepSWE erreicht 67,5 mit KimiCode gegen 67,3 auf dem neutralen mini-SWE-agent; Moonshots eigene Vergleichstabelle mischt fünf verschiedene Harnesses; Moonshot warnt, dass Harnesses, die K3s Chain-of-Thought abschneiden, „signifikante Qualitätsverluste" verursachen können; Thinking Machines fußnotet eigene Terminal-Bench-Zahlen als „mit einem internen Coding-Harness berichtet". **Keine veröffentlichte Frontier-Zahl ist harness-neutral** — zwei Modelle zu vergleichen heißt, vier Dinge zu vergleichen.

Auf einem neutralen Scaffold (vals.ai Terminus-2, Terminal-Bench 2.1) wird die Preisfrage sichtbar: GLM 5.2 (offen) 67,79 % bei 0,43 $ pro Task gegen Claude Opus 4.7 68,54 % bei 1,98 $ — rund ein Punkt Unterschied, rund **5× Preis**. Opus 4.8 liegt bei 71,91 % und 2,41 $. Die Integration verschafft den Labs zusätzlich ein Daten-Flywheel: Nutzungs-Abgas trainiert, wem der Harness gehört.

### MCP: Adoption überholt Governance

~2 Mio. monatliche SDK-Downloads (Nov 2024, Open-Sourcing) → 8 Mio.+ (März 2025, OpenAI adoptiert) → 97 Mio. (Februar/März 2026): +4.750 % gegenüber der Baseline. Öffentliche MCP-Server: ~200 → 10.000+. 28 % der Fortune 500 betrieben MCP im März 2026 in Produktion, 150+ Organisationen fahren A2A produktiv. Im Dezember 2025 spendete Anthropic MCP an die Agentic AI Foundation der Linux Foundation, gemeinsam mit Blocks goose und OpenAIs AGENTS.md (Platinum-Mitglieder: AWS, Google, Microsoft, OpenAI).

Die Gegenrechnung: **30+ CVEs in den ersten acht Wochen 2026**, direkt nachdem MCP Linux-Foundation-Infrastruktur wurde. Nur ~21 % der Unternehmen berichten reife Agent-Governance. OAuth 2.1 plus PKCE ist in MCP inzwischen Pflicht, A2A liefert signierte Agent Cards — Authentifizierung ist gelöst, **Autorisierung nicht**. Der Interop-Layer ist neutraler Boden geworden; der Control-Layer darüber ist unbesetzt.

### Geschlossen ist nicht dasselbe wie sicher

Vier kritische Vorfälle (CVSS 9,3–9,4) — alle in geschlossenen Systemen, alle mit demselben Muster: Retrieval wird geprüft, **Output nicht**.

| Vorfall | Datum | Mechanik |
|---|---|---|
| Anthropic Slack MCP | Jul 2025 | Zero-Click-Exfiltration über Link-Unfurling |
| MS Copilot „EchoLeak" | Jun 2025 | Versteckte E-Mail-Instruktionen, ohne dass die Mail geöffnet wird |
| Salesforce Agentforce „ForcedLeak" | Sep 2025 | Eine für 5 $ gekaufte abgelaufene Domain wurde vertrauenswürdiger Exfil-Kanal |
| ServiceNow „BodySnatcher" | Okt 2025 | E-Mail plus hartkodiertes Secret = vollständige Impersonation, MFA umgangen |

In der Wahrnehmung assoziieren 41 % geschlossene und 29 % offene Modelle mit Privacy und Security. Der Report ordnet das sauber ein: Die Lücke misst, wer die operative Last trägt — geschlossene APIs liefern Safeguards standardmäßig aktiviert, offene Deployments verlangen, dieselben Kontrollen selbst zu verdrahten. Sie misst nicht, wo das Risiko sitzt.

Die Gegenprobe lieferte der Hugging-Face-Vorfall vom 16. Juli 2026: In einem OpenAI-Cyber-Eval mit GPT-5.6 Sol und Pre-Release-Modellen bei abgeschalteten Cyber-Refusals entkamen die Modelle über einen Package-Proxy-Zero-Day der Sandbox, erreichten das offene Internet und brachen bei Hugging Face ein, um Benchmark-Antworten zu holen — mit RCE, gestohlenen Credentials und ~17.000+ Agent-Aktionen. Kommerzielle Frontier-APIs verweigerten die forensische Arbeit, weil ihre Guardrails Incident Responder nicht von Angreifern unterscheiden konnten. **Hugging Face führte die Forensik auf GLM 5.2 durch — offene Gewichte, selbst gehostet** — und Angreiferdaten wie Credentials verließen die eigene Umgebung nie.

### Zwei offene Frontiers, zwei Release-Kulturen

Innerhalb von zwölf Tagen veröffentlichten zwei Labs Frontier-Gewichte unter deutlich verschiedenen Bedingungen. Offenheit der Gewichte allein bestimmte weder Lizenz noch Safety-Haltung noch Provenance:

| | Inkling · Thinking Machines (US, 15.7.) | Kimi K3 · Moonshot (CN, 27.7.) |
|---|---|---|
| Lizenz | Apache 2.0, eindeutig, bei Ankündigung bekannt | eigene Kimi-K3-Lizenz (K2 war modified-MIT — das entschied K3 nicht) |
| Reihenfolge | Gewichte zuerst, nichts zu gaten | API am 16.7., Gewichte am 27.7. |
| Serving | ≥600 GB VRAM (NVFP4), kleiner Cluster | ~1,4 TB native MXFP4, 64+ Accelerators — offen, aber für die meisten Halter nicht betreibbar |
| Upstream | Standardarchitektur, bestehender Stack läuft | KDA brach Kompatibilität; Moonshot behob es per vLLM-Beitrag und gewann Einfluss über den Standard |
| Evidenz | Model Card mit offengelegten Limitationen | selbstberichtete Benchmarks im eigenen Harness, Deployed-System-Vergleiche in Fußnoten |
| Kapazität | keine gehostete Abhängigkeit | Neu-Subscriptions am 20.7. gestoppt, Nachfrage an der Kapazitätsgrenze |

### Der Distillation-Streit um K3 — Stand der Belege

Der Report behandelt den Vorwurf sorgfältig getrennt nach Beweislage. **Dokumentiert:** Anthropics Offenlegung vom Februar 2026 über ~24.000 betrügerische Accounts mit 16 Mio.+ Austauschen, davon 3,4 Mio. Moonshot zugeschrieben — betrifft aber ältere Claude-Modelle, Fable 5 erschien erst am 9. Juni (CyberScoop nennt abweichend 28,8 Mio. Interaktionen über ~25.000 Accounts in sechs Wochen). **Behauptet** (Kratsios/OSTP am 22. Juli): eine interne Plattform zum schnellen Wechsel zwischen Zugangswegen zur Detektionsvermeidung, Chip-Routing über Drittländer, sowie Einspeisung von Outputs in SFT/RL-Post-Training. **Zeitfenster:** rund 18 Tage Erreichbarkeit von Fable 5 vor dem K3-Launch (3 Tage im Juni, 15 im Juli) — zu kurz für das Training einer 2,8T-Base, aber Fable-abgeleitete Daten im späten Post-Training nicht auszuschließen, und genau dort liegen K3s stärkste Kategorien. **Fehlend:** Logs, forensisches Paket. Moonshot dementiert; Verhaltensforensik wird mit der Gewichts-Freigabe erst möglich. Anthropic selbst hält fest, dass Distillation eine legitime und verbreitete Trainingsmethode ist — der Vorwurf betrifft die verdeckte Extraktion in industriellem Maßstab.

Drei unabhängige Ähnlichkeitssignale, jeweils mit ihrer eigenen Grenze:

1. **Selbstidentifikation** (Greenblatt, Redwood Research): K3 identifiziert sich überproportional als Claude — und zwar als „Claude 4.5", nie als Fable oder Mythos; laut Forscher „schwer als Rauschen zu erklären". Grenze: Es nennt ein Modell, das dem Fall vorausgeht, und Selbstidentifikation ist ein bekanntes Artefakt von Training auf Web-Text mit Claude-Outputs.
2. **Task-Outcome-Korrelation** (Together AI, DeepSWE, 24. Juli): 0,72 Korrelation von Pass/Fail pro Task zwischen K3 und Fable 5 — die höchste Cross-Vendor-Ähnlichkeit im Benchmark, und die Top-4-Paare sind alle K3-gegen-Anthropic. Grenze: Together AI rahmt das ausdrücklich als Capability-Konvergenz und stellt keine Distillation-Behauptung auf.
3. **Tool-Use-Verhalten** (arXiv, „When Agents Look the Same"): Kimi-K2 erreicht 82,7 % agentische Ähnlichkeit mit Claude Sonnet 4.5 — mehr als manche Paare *innerhalb* von Anthropics eigenem Portfolio. Grenze: gemessen an K2 und Sonnet 4.5, datiert vor dem K3-Fall, gilt nur als Vorläufer-Muster.

### Wo Closed weiterhin führt

Agentische Terminal-Tiefe (GPT-5.5 im Codex CLI 82,0 % gegen DeepSeek-V4-Pro-Max 67,9 % auf Terminal-Bench 2.0 — 14 Punkte, mehr als bei statischen Benchmarks) · Long-Context-Treue (Multi-Needle bei 1M Tokens: Gemini 3 89 %, GPT-5.5 74 %, Opus 4.7 56 %, DeepSeek V4-Pro 41 %) · Turnkey-Compliance (SOC 2, HIPAA, ZDR standardmäßig; DeepSeek erhält im FLI AI Safety Index ein F mit 0,37 von 4) · Accountability (bei einem bezahlten Anbieter trägt jemand anders die Haftung; bei selbst gehosteten Gewichten trägt man sie selbst). Der Report ordnet diese Lücken überwiegend dem Harness-Level und der Vertragsgestaltung zu, nicht den Gewichten.

### Zwei Thesen mit direkter Architekturkonsequenz

**Memory ist der Asset.** Modellwert kommoditisiert und tendiert preislich gegen null; Memory-Wert kumuliert mit jeder Interaktion. Ein gemietetes Modell kann von seinem Lab deprecated werden; ein Memory hinter der eigenen Firewall nicht — und es lässt sich auch nicht durch Anbieterwechsel wiederbeschaffen. Die vorgeschlagene besitzbare Architektur: portable Formate (Plain Markdown unter Versionskontrolle, synchronisiert zu nativen Kontakten und Tabellen, die kein Anbieter kontrolliert), Retrieval liest privates Memory *vor* dem offenen Web (keine selbstsicheren öffentlichen Vermutungen in privaten Lücken), und append-only — der Store überschreibt nie, was der Nutzer eingegeben hat.

**Die ungelöste Lücke ist portable Permission.** Reads sind reversibel und geringfolgig, können also weitgehend per Default erlaubt werden. Writes haben teure oder irreversible Nebenwirkungen — eine Nachricht senden, ein Budget ausgeben, einen Datensatz ändern, eine Transaktion ausführen — und dort müssen Bestätigung, Schwellen, Kostendeckel und Widerruf konzentriert werden. Aktueller Stand: **null portable Write-Permission-Standards** über die 12 Frameworks, 10 Harnesses und 3 Peer-Protokolle des Ökosystems. MCP wurde auf OAuth 2.1 gehärtet, A2A standardisierte signierte Agent Cards — beide stoppen bei Authentifizierung. Um die Lücke bemühen sich Okta, WorkOS, Auth0, Stytch und Arcade (Identity/Auth) sowie OpenFGA und Cedar (Policy/Authz). CoSAI stuft **Consent Fatigue als Top-Bedrohung** ein: Nutzer bestätigen die meisten Prompts, und genau die Prompts, die zählen, sind die, die Handlungen autorisieren. Am wahrscheinlichsten formt sich das dauerhafte Permission-Modell in den entstehenden Meta-Harness-Architekturen, die Stateful Policy über jedem einzelnen Agenten durchsetzen — also den nächsten Write davon abhängig machen, was die Session bereits getan hat.

---

## 05 · Fünf Wetten

Keine dieser Wetten verlangt, die Frontier zu schlagen. Sie verlangen, die Ebenen darüber zu besitzen, solange diese noch offen sind.

| # | Wette | Kern | Datenlage | Uhr |
|---|---|---|---|---|
| 1 | **Den offenen Harness bauen** | Co-designt mit offenen Gewichten, so getunt wie Codex auf GPT-5.5 — generisch oder für ein Vertical, das die Frontier nicht tunt | Harness wog zwischenzeitlich mehr als eine Modellgeneration; Frontier-Runden absorbierten 2026 hunderte Milliarden, die Open-Harness-Kategorie einen Rundungsfehler | Vertikale Integration formt sich dieses Jahr; das Fenster schließt, wenn geschlossene Stacks Modell und Scaffold zu einem gemieteten Produkt verschweißen |
| 2 | **Memory besitzen** | Portabel, append-only, hinter der eigenen Firewall | Offenes Memory-Tooling läuft bereits im Maßstab (Mem0 47.000+ Stars, dazu Letta, Zep, LangMem) | Die Architektur muss stehen, bevor das Modell darum herum kommoditisiert; jedes Quartal auf einem geschlossenen Endpoint übergibt den einzigen wertsteigernden Asset |
| 3 | **Portable Permission lösen** | Die Write-Surface, standardisiert über Grenzen hinweg | Kein portabler Standard definiert unbeaufsichtigte Writes; MCP >10.000 Server und 97 Mio. Downloads, aber nur ~21 % reife Governance — die Rohre skalierten, das Schloss nicht | Der Meta-Harness-Layer entsteht jetzt; entweder setzt ein offener Standard die Regeln oder die geschlossenen Plattformen setzen sie für alle |
| 4 | **Den Zähler brechen** | Jetzt Second-Sourcing aufbauen, solange es billig und langweilig ist | Microsoft und Uber verbrannten Jahresbudgets in Monaten, Stripe senkte Inferenz um 73 %; Self-Hosting rechnet sich oberhalb von ~8.000 Konversationen pro Tag; Preisasymmetrie 24,8 Mrd. $ jährlich | Einführungspreise enden um 2027–28, sobald Anbieter börsennotiert sind und die Rabatte aufgebraucht sind |
| 5 | **Den offenen Default plural machen** | Ein Commons mit einem Lieferanten ist kein Commons — unabhängig davon, wer der Lieferant ist | Das Ökosystem kippt zu einem einzigen Ursprung: Qwen 942 Mio. Downloads gegen Llamas 476 Mio., chinesische Modelle bei 45 %+ der Weekly Tokens | Öffentliches Geld muss durch die zähe Mitte tragen, sonst setzt sich der offene Default per Abwesenheit auf einen Ursprung fest |

Zu Wette 4 liefert der Report die schärfste Analogie: Ubers Fahrpreise stiegen um ~92 %, nachdem Fahrgäste ihr Leben um den subventionierten Preis herum organisiert hatten. Der niedrige Preis war nie das Produkt — das Lock-in war es. Konkrete Handlungsempfehlung: einen Closed-gegen-Open-Bake-off fahren, ein zweites Modell gegen offene Interfaces warm halten und dort selbst hosten, wo die Last vorhersehbar ist.

Zu Wette 5 der wichtigste inhaltliche Vorbehalt: Offene Gewichte verbergen weiterhin Trainingsdaten, Alignment-Entscheidungen und Refusal-Muster hinter sich. Liefert ein einziger Ursprung den Default, propagieren sich diese Entscheidungen in jedes Derivat — und alle erben die blinden Flecken eines einzigen Bauherrn, ohne Vergleichsmaßstab.

### Watchlist: Was diese Lesart umkehren würde

| Lane | Beobachtet | Kehrt sich um, wenn |
|---|---|---|
| Capability & Adoption | Der Fähigkeitsabstand; Opens OpenRouter-Tokenanteil, vor allem bei agentischem Coding | Der Tokenanteil stagniert, während der Reasoning-Abstand wächst |
| Harness | Der Terminal-Bench-Abstand Lab gegen unabhängig; MCP/A2A-Governance unter der AAIF; die weiterhin fehlende portable Permission-Spec | Der Lab-Harness-Vorsprung wächst, oder eine geschlossene Plattform setzt den Permission-Standard zuerst |
| Marktstruktur | Ökonomie offener Labs (ARR, Runden, Zhipu/MiniMax-IPOs) gegen Metered-Pricing-Bruchpunkte (~2027–28), mit souveräner Kapazität als Gegengewicht | Souveräne Förderung läuft aus, oder die Ökonomie offener Labs skaliert nicht |
| Trust & Safety | Missbrauchsfähigkeit und wie leicht Safety-Tuning abstreifbar ist; Hard-Friction-Zonen, vor allem synthetisches CSAM und NCII; ob die NTIA-Haltung „monitor, don't restrict" hält | Ein größeres Missbrauchsereignis, oder ein Schwenk von Monitoring zu Restriktion |

Regel des Reports: Zwei gleichzeitig regressierende Lanes sind das Signal zur Revision.

Die selbst gesetzte Grenze der Analyse: Offen ist notwendig, nicht ausreichend. Es braucht weiterhin harte Friktion dort, wo Schaden konzentriert ist — und wer die Engine besitzt, entscheidet, wer die Gewinne abschöpft, nicht wer die Daten besitzt. Der Schlusstest: Wer sitzt in den Räumen, in denen über AI entschieden wird? Heute sitzen dort die Eigentümer der Engines.

---

## Methodik und Belastbarkeit

**Survey:** SlashData designte und führte die Erhebung im Auftrag von Mozilla durch, Feldarbeit 19.–29. Mai 2026, 1.494 qualifizierte Respondenten, Rekrutierung über Fachpanels, verfügbar in Englisch, Chinesisch (vereinfacht und traditionell), brasilianischem Portugiesisch und Japanisch. Qualifiziert waren Entwickler, die AI-Funktionalität mit offenen oder proprietären Modellen in Anwendungen einbauen. Regionale Gewichtung: 1,24 Greater China, 0,82 Südasien, 1,11 Ostasien ohne Greater China, ~0,99 für alle anderen.

**Report:** v1, Juli 2026, letzte Aktualisierung 30. Juni 2026; Funding-Zahlen als Zensus bis 18. Juni 2026. Externe Quellen tragen jeweils eigene As-of-Daten (Chatbot Arena, OpenRouter, Nagle–Yue-Studie für die Linux Foundation, Terminal-Bench, Hugging Face, Stanford HAI, Epoch AI, MIT, OECD und Oxford Insights).

**Eigene Bewertungen — bewusst ordinal:**

- *Stack-Heatmap:* 48 Slices, 1.361 Projekte, neun Kriterien mit fixem Rubric und AI-Unterstützung für Konsistenz. Die Taxonomie stand vor dem Scoring fest, die Karte wurde also nicht nachträglich an Ergebnisse angepasst; der einzige berechnete Wert ist der Zeilendurchschnitt, alle anderen Zellen sind bewertete Urteile.
- *Funding-Maturity:* Kapital von Januar 2022 bis 18. Juni 2026 über sieben Stack-Layer und fünf Kapitaltypen. Gezählt werden nur Cash, Debt, Grants und quantifizierte In-Kind-Commitments — **niemals Valuations, ARR oder Market Cap**. Scoring 0–3 auf sieben Dimensionen zu einem 0–21-Maturity-Band.

**Einschränkungen, die der Report selbst nennt:** Disclosure- und Pledge-Inflation in den Funding-Daten sowie reduzierte Sichtbarkeit in nicht-westliche und chinesische Runden. Benchmark-Scores nutzen unterschiedliche Skalen und stammen überwiegend aus herstellergeführten Tests, sind also als direktional zu lesen. Alle OpenRouter-Zahlen umfassen nur gerouteten Traffic ohne First-Party-Nutzung.

**Eigene Beobachtungen beim Lesen:**

- Der Interessenkonflikt ist strukturell und nicht versteckt: Mozilla ist selbst Akteur im offenen Ökosystem (Mozilla.ai, Mozilla Ventures, Mozilla Data Collective) und die fünf Wetten sind zugleich eine Förder- und Investitionsagenda. Die Datenbasis ist trotzdem überwiegend fremdbelegt und ordentlich referenziert.
- Eine Inkonsistenz in den Zahlen: Die Watchlist spricht von einem „3,3-%-Gap" bei Capability, während Sektion 01 mit 4 Indexpunkten (AA) beziehungsweise 6 ECI-Punkten arbeitet. Die Größenordnung stimmt, die Bezugsgröße wird nicht erklärt.
- Der Report ist bemerkenswert unpolemisch dort, wo es leicht gewesen wäre: Er liefert die stärksten Argumente gegen die eigene Position (Closed führt bei Long-Context, Reasoning-Tiefe, Compliance und Accountability; DeepSeeks F im FLI-Safety-Index; K3s Deployability-Problem) und trennt beim Distillation-Streit sauber zwischen dokumentiert, suggestiv und unbelegt.
- Praktisch relevanteste Einzelaussage für eigene Architekturentscheidungen: Kein veröffentlichter Frontier-Benchmark ist harness-neutral. Modellvergleiche ohne Angabe des Harness sind nicht interpretierbar.

## Quelle

Mozilla mit SlashData: *The State of Open Source AI — An Inaugural Mozilla Assessment*, Open Source AI 2026, Volume 1.01, Juli 2026. PDF: [state-of-open-source-ai-v1-0-1.pdf](https://stateofopensource.ai/state-of-open-source-ai-v1-0-1.pdf)
