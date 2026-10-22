---
titel: Entwicklung der LLM-Modelle von April bis Oktober 2026
stand: 2026-10-13
zeitraum: 2026-04-01 bis 2026-10-13
typ: recherchebericht
---

# Entwicklung der LLM-Modelle von April bis Oktober 2026

**Die zentrale Entwicklung ist die Verbindung von stärkerem Reasoning, längeren Arbeitsabläufen und günstigeren Modellstufen.** LLMs werden zunehmend dafür optimiert, Werkzeuge zu verwenden, Ergebnisse zu überprüfen und Aufgaben über mehrere Schritte fortzusetzen. Gleichzeitig sinkt der Preis bestimmter Leistungsniveaus. Beides zusammen erweitert die wirtschaftlich sinnvollen Anwendungen.

Dieser Bericht betrachtet den Zeitraum **1. April bis 13. Oktober 2026**. Er konzentriert sich auf wichtige Modellfamilien und technische Veränderungen; die Zeitlinie ist keine vollständige Liste jedes Releases. Grundlage sind live gelesene Herstellerankündigungen, Model Cards, technische Dokumentation und Forschungsberichte. Veröffentlichungstermine können sich zwischen API, Webapp und Coding-Produkten unterscheiden. Es wurden keine eigenen Modell-Benchmarks ausgeführt.

Herstellerangaben zu Leistungsgewinnen bleiben als solche gekennzeichnet. Eine verfügbare API, ein angekündigtes Modell und herunterladbare Gewichte sind verschiedene Zustände. Einschätzungen und Vorschläge im Bericht sind ausdrücklich als eigene Einordnung formuliert.

**Die ausgewählten Meilensteine zeigen, wie schnell sich die Modelllandschaft verändert hat.**

| Zeitraum / Datum 2026 | Entwicklung | Belegter Zustand bzw. Bedeutung |
|---|---|---|
| 24. April | GPT-5.5; DeepSeek V4 | OpenAI-API-Release; DeepSeek-Preview mit API und offenen Gewichten |
| 19. Mai | Gemini 3.5 Flash | Allgemein veröffentlichte, agentisch ausgerichtete Flash-Generation |
| 9. Juni | Claude Fable 5 / Mythos 5 | Allgemeines Modell und gesondert zugängliche Variante |
| 9. Juli | GPT-5.6 Sol, Terra, Luna | Deutlicher Ausbau der Leistungs- und Kostenstaffelung |
| 24. Juli | Claude Opus 5 | Stärkere Alltagsklasse unterhalb der teuersten Spitzenmodelle |
| August | Qwen3.8; Muse Glimmer-30B | Große offene Modelle und kleinere lokale Alternativen |
| 12. August | Grok 4.6 | Schwerpunkt lange Agent-Aufgaben und interaktive Arbeit |
| 1.–3. September | Fable 5.1; Gemini 3.8 Flash; GPT-6 Astra | Neue Leistungsstufen für anspruchsvolle Arbeit |
| 10. September | DeepSeek V4.1 Flash; OpenAI Agents API | Neue Architektur und zusätzliche Infrastruktur für Agenten |
| 21.–22. September | Grok 4.7; Opus 5.5; GPT-6 Sol/Luna | Fähigkeiten und Preis-Leistung werden gleichzeitig verbessert |
| 28.–29. September | Sonnet 5.5; GPT-6.1 Sol | Leistungsfähige Modelle für häufige professionelle Aufgaben |
| 30. September | Gemini 4 Argon | Angekündigt; Zugang zunächst für ausgewählte Teilnehmer |
| 5.–6. Oktober | Reflection Beam; Mistral Large 4 | Early Access bzw. API-Preview; Gewichte später angekündigt |
| 7. Oktober | Claude Haiku 5.5 | Sehr günstige Modellstufe für begrenzte Aufgaben |
| 12. Oktober | Muse Wonder / Wonder Full | Gehostete Modelle über Metas Produkte und API |

Die Belege und Einschränkungen zu diesen Meilensteinen stehen direkt bei den jeweiligen Anbieterabschnitten.

**Reasoning ist inzwischen eine wesentliche Stellschraube für Leistung und Kosten.** Modelle verfügen häufiger über einstellbare Denktiefe. Der Nutzer oder die Anwendung bestimmt damit, wie viel Rechenaufwand eine Aufgabe erhalten soll. Für knappe Klassifikationen ist das eine andere Entscheidung als für die Untersuchung eines widersprüchlichen Softwarefehlers.

Eine Epoch-Analyse vom 16. April findet in drei von vier untersuchten Fähigkeitsmaßen Anzeichen beschleunigten Fortschritts. Die Veränderung fällt mit Reasoning-Modellen, mehr Inferenzrechenaufwand und stärkerem Reinforcement Learning zusammen. Die untersuchten Fortschritte betreffen allerdings überwiegend Mathematik und Programmierung. Die Studie belegt keine gleichartige Beschleunigung in sämtlichen Formen menschlicher Arbeit. [Epoch: Beschleunigung von KI-Fähigkeiten](https://epoch.ai/publications/have-ai-capabilities-accelerated)

Meine Einordnung: Fortschritt entsteht sowohl durch bessere Modelle als auch durch eine bessere Nutzung des verfügbaren Rechenbudgets. Eine längere Antwort ist dabei kein Qualitätsbeweis. Mehr Reasoning muss sich durch weniger Fehler, bessere Entscheidungen oder geringere Nacharbeit rechtfertigen.

**OpenAI hat seine Modellpalette und die Infrastruktur für längere Aufgaben ausgebaut.** Auf GPT-5.5 im April folgte GPT-5.6 mit Sol, Terra und Luna im Juli. GPT-6 Astra erschien laut API-Changelog am 3. September, GPT-6 Sol/Luna am 22. September und GPT-6.1 Sol am 29. September. Die Agents API startete am 10. September als öffentliche Beta; Computer Use kam am 29. September hinzu. Eine Korrektur der Bildverarbeitung in Sol/Luna am 25. September zeigt außerdem, dass auch Änderungen innerhalb einer Modellgeneration Ergebnisse verändern können. [OpenAI API-Changelog](https://developers.openai.com/api/docs/changelog)

GPT-5.5 bietet bereits 1,05 Millionen Kontexttokens und bis zu 128.000 Outputtokens. Das Modell verarbeitet Text und Bilder und gibt direkt Text aus. Der dokumentierte Wissensstand reicht bis Dezember 2025. Ein späteres Veröffentlichungsdatum bedeutet also keinen entsprechend aktuellen Wissensstand. [GPT-5.5-Modellkarte](https://developers.openai.com/api/docs/models/gpt-5.5)

GPT-6 Astra richtet sich laut OpenAI an anspruchsvolles Reasoning, Coding, Computer Use und Recherche. GPT-6.1 Sol wird als nahe an Astra bei niedrigerem Preis positioniert; diese Nähe ist eine Herstellerbewertung. Beide besitzen 1,05 Millionen Kontexttokens und einen Wissensstand bis 30. April 2026. Luna bietet dieselbe nominelle Kontextkapazität bei wesentlich niedrigerem Tokenpreis, wird aber für fokussierte Volumenaufgaben positioniert. Gleiche Kontextgröße bedeutet keine gleiche Problemlösefähigkeit. [Astra](https://developers.openai.com/api/docs/models/gpt-6-astra), [6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna)

Die GPT-6-Dokumentation beschreibt unter anderem wiederverwendbare Reasoning-Zustände, asynchrone Werkzeugaufrufe und Steuerung während laufender Arbeit. Programmatic Tool Calling kann mehrere Abfragen in einem Programm zusammenführen und Ergebnisse vor der Rückgabe filtern. Meine Einordnung: Damit lässt sich auch der Ablauf zwischen Modell und Werkzeugen effizienter gestalten. Ein Teil des Fortschritts betrifft die Arbeitsumgebung. [GPT-6-Leitfaden](https://developers.openai.com/api/docs/guides/latest-model), [Programmatic Tool Calling](https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling)

**Anthropic hat neue Spitzenfähigkeiten auf günstigere Modellklassen übertragen.** Fable 5 und Mythos 5 erschienen im Juni. Anthropic beschreibt längere autonome Arbeit, verbessertes Bildverständnis und die Verwendung dauerhafter Notizen. Beide Varianten basieren laut Anbieter auf demselben zugrunde liegenden Modell, unterscheiden sich aber in Zugang und Schutzmaßnahmen. Der zeitweise unterbrochene und anschließend wiederhergestellte Zugang unterstreicht, dass eine Veröffentlichung keine unveränderte dauerhafte Verfügbarkeit garantiert. [Fable 5 / Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)

Opus 5 folgte im Juli mit einem niedrigeren Preis als Fable und einem Schwerpunkt auf Coding, Computer Use und Wissensarbeit. Bei der Interpretation der veröffentlichten Evaluationen ist wichtig, dass zum Teil mehrere Versuche und Fallback-Modelle verwendet wurden. Die gemessene Leistung betrifft somit ein konkretes Gesamtsystem. [Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)

Fable 5.1 erschien am 1. September. Anthropic beschreibt Fortschritte bei langen Aufgaben und niedrigeren Effort-Stufen. Die regulären Input-/Outputpreise blieben bei 10/50 Dollar je Million Tokens, während günstigere Cache-Reads die Kosten wiederholter Arbeit reduzieren sollen. [Fable 5.1 / Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1), [datiertes Fable-Produktregister](https://www.anthropic.com/claude/fable)

Opus 5.5 erschien am 22. September mit Preisen von 4/20 Dollar. Anthropic berichtet schnellere Ausgabe und niedrigere Kosten typischer Aufgaben. Sonnet 5.5 folgte am 28. September für häufige, klar begrenzte Aufgaben. Besonders aufschlussreich: Anthropics Sonnet-Evaluierung zeigt Fälle, in denen die höchste Effort-Stufe schlechter abschneidet, weil zusätzliche Subagents und Änderungen außerhalb des Auftrags Nachteile verursachen. Mehr Rechenaufwand verbessert das Ergebnis nicht automatisch. [Opus 5.5](https://www.anthropic.com/claude-opus-5-5), [Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)

Haiku 5.5 erschien am 7. Oktober. Für Prompts bis 100.000 Tokens gelten 0,10 Dollar Input und 0,50 Dollar Output pro Million Tokens; darüber 0,50/2,50 Dollar. Das Modell bietet einstellbaren Effort und wird für Zusammenfassungen, Klassifikation und begrenzte Hilfsaufgaben positioniert. Meine Einordnung: Die wirtschaftlich wichtige Entwicklung ist die Kombination leistungsfähiger Hauptmodelle mit sehr günstigen Hilfsmodellen. [Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5)

**Google verbindet häufige Flash-Updates mit einer neuen, zunächst eingeschränkt zugänglichen Spitzenklasse.** Gemini 3.5 Flash erschien im Mai allgemein. Die Ankündigung betont Coding, multimodale Verarbeitung, Tool-Nutzung und den Antigravity-Harness. [Gemini 3.5](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)

Gemini 3.8 Flash folgte am 2. September. Google beschreibt zusätzliche Denkschritte und iterative Werkzeugnutzung, weist aber auf möglichen höheren Tokenverbrauch hin. Die Einführungspreise von 0,75/3,75 Dollar gelten laut Veröffentlichung bis Ende 2026; ab Januar 2027 sind 1,50/7,50 Dollar vorgesehen. Flash Cyber ist eine gesondert zugängliche Variante. Ein besseres Modell zum gleichen Tokenpreis kann also trotzdem höhere Kosten je Aufgabe verursachen. [Gemini 3.8 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)

Gemini 4 Argon wurde am 30. September angekündigt. Hervorzuheben ist das Output-Limit von einer Million Tokens. Das ist eine Angabe zur Ausgabe, kein Beleg für ein gleich großes Eingabekontextfenster. Zugang erhalten zunächst ausgewählte Teilnehmer; die breite Freigabe ist angekündigt. Die Veröffentlichung nennt 2/10 Dollar als Einführungspreis und anschließend 4/20 Dollar. Diese Angaben machen Argon noch nicht zu einem für jeden verfügbaren Dienst. [Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

**Grok hat sich stärker auf lange Coding- und Wissensaufgaben ausgerichtet.** Grok 4.6 erschien am 12. August, Grok 4.7 am 21. September. Der Anbieter beschreibt für 4.7 ein größeres Basismodell und längeres Reinforcement Learning mit schwierigeren Aufgaben. Die behaupteten Verbesserungen betreffen unter anderem Verifikation und Kontextverwaltung. [Grok 4.6](https://x.ai/news/grok-4-6), [Grok 4.7](https://x.ai/news/grok-4-7)

Die aktuelle Entwicklerdokumentation nennt für Grok 4.7 500.000 Kontexttokens, Text-/Bildinput sowie 2/6 Dollar je Million Input-/Outputtokens. Wiederverwendeter Reasoning-Zustand und Kontextverdichtung gehören zur Unterstützung langer Arbeitsverläufe. Meine Einordnung: Der Wettbewerb betrifft auch hier das Paket aus Modell, Werkzeugen und fortgesetzter Arbeit. [Grok-4.7-Dokumentation](https://docs.x.ai/developers/grok-4-7)

**Bei offenen Gewichten wachsen sowohl die Spitzenmodelle als auch die kleineren Alternativen.** DeepSeek veröffentlichte V4 am 24. April als Preview mit API und offenen Gewichten. V4 Pro besitzt laut Hersteller 1,6 Billionen Parameter, davon 49 Milliarden aktiv; Flash 284 Milliarden insgesamt und 13 Milliarden aktiv. Beide unterstützen eine Million Kontexttokens. V4 Pro erreichte im August die allgemeine API-Verfügbarkeit, V4.1 Flash folgte im September. [DeepSeek V4](https://deepseek.com/en/news/v4-preview/), [API-Changelog](https://api-docs.deepseek.com/updates/?release=deepseek-coder)

V4.1 Flash trennt die aktive Modellgröße für Inputverarbeitung und Outputgenerierung: acht beziehungsweise 16 Milliarden Parameter. Die Model Card unterscheidet Backbone und zusätzliche Engram-Memory-Parameter. Meine Einordnung: Solche Architekturen machen einfache Vergleiche anhand einer einzigen Parameterzahl immer weniger aussagekräftig. [V4.1-Flash Model Card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)

Alibaba veröffentlichte im August Qwen3.8 sowohl als 2,4T-A95B-Modell als auch als dichtes 27B-Modell. Das offizielle Repository dokumentiert unterschiedliche Serving-Wege. Die Familie verbindet damit eine große MoE-Spitzenklasse mit einer wesentlich kleineren Alternative. [Qwen3.8-Repository](https://github.com/QwenLM/Qwen3.8)

Kimi K3 besitzt laut Moonshot 2,8 Billionen Parameter, Bildverständnis und eine Million Kontexttokens. Die veröffentlichten Gewichte und das dokumentierte MXFP4-Training sind für Betreiber relevant. Diese Größenordnung bleibt allerdings anspruchsvoll für das Serving. Moonshot räumt selbst einen Abstand zu den stärksten getesteten proprietären Modellen ein. [Kimi-K3-Ankündigung](https://www.kimi.ai/blog/kimi-k3), [Repository](https://github.com/MoonshotAI/Kimi-K3)

Z.ai beschreibt GLM-5.3 als Fortschritt durch Post-Training auf dem Basismodell von GLM-5.2. Das Repository führt GLM-5.3 als 744B-A40B und Flash als 320B-A18B und verlinkt veröffentlichte Gewichte. Die größere Leistungsfähigkeit entsteht somit nicht in jedem Fall durch ein neues, größeres Basismodell. Ein genaues GLM-5.3-Erstveröffentlichungsdatum wurde in dieser Recherche nicht belastbar bestätigt. [GLM-Repository](https://github.com/zai-org/GLM-5)

Reflection Beam wurde am 5. Oktober vorgestellt, mit 501 Milliarden Gesamtparametern und 23 Milliarden aktiven Parametern. Zum Stichtag sind Early Access und eine spätere Gewichtsveröffentlichung angekündigt. Mistral Large 4 folgte am 6. Oktober als öffentliche API-Preview eines multimodalen Modells mit einer Billion Parametern; die Gewichte sind für Ende Oktober vorgesehen. Beide sollten noch nicht als bereits herunterladbare Oktober-Releases gezählt werden. [Beam](https://reflection.ai/blog/introducing-beam), [Mistral Large 4](https://mistral.ai/news/mistral-large-4/)

Meta veröffentlichte Muse Wonder und Wonder Full am 12. Oktober über API bzw. Muse Code. Die Ankündigung belegt keine offenen Wonder-Gewichte. Davon getrennt ist Muse Glimmer-30B: Die Model Card nennt August 2026 als Veröffentlichungsmonat und dokumentiert quantisierte Varianten für 24-/32-GB-Hardware. Das sind Angaben unter bestimmten Hersteller-Testbedingungen, keine Zusage für jede Kontextlänge und jedes System. [Muse Wonder](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/), [Glimmer Model Card](https://huggingface.co/meta-models/Muse-Glimmer-30B)

**Aktive Parameter, Speicherbedarf und lokale Nutzbarkeit sind verschiedene Fragen.** Bei Mixture of Experts werden pro Verarbeitungsschritt nur Teile eines größeren Modells aktiviert. Das senkt Rechenaufwand, bedeutet aber nicht, dass ausschließlich diese aktiven Teile gespeichert werden müssen. Zu den Gewichten kommen Speicher für Kontextzustand und Laufzeit. Quantisierung reduziert den Speicherbedarf, während Kontextlänge, Parallelität und Hardware weiterhin die nutzbare Geschwindigkeit bestimmen.

Meine praktische Einordnung: Für einen lokalen Pilot sind die kleineren Qwen- und Glimmer-Varianten besonders interessante Ausgangspunkte. Sehr große MoE-Modelle sind ein anderes Infrastrukturprojekt. Die Entscheidung sollte an Qualität, Latenz und tatsächlichem Speicherverbrauch der eigenen Aufgaben hängen. Die bloße Verfügbarkeit von Gewichten beantwortet diese Fragen nicht.

**Multimodalität wird stärker in Arbeitsabläufe eingebunden.** Text- und Bildinput unterstützen etwa das Lesen von Screenshots, Dokumentlayouts und Benutzeroberflächen. Fortschritt ist dann praktisch wertvoll, wenn das Modell eine Beobachtung in eine passende Aktion übersetzt und anschließend das Ergebnis prüft. Ein schöner UI-Entwurf und die zuverlässige Bedienung einer fremden Oberfläche sind unterschiedliche Fähigkeiten.

Auch eine multimodale Produktoberfläche sagt wenig darüber aus, welche Modalitäten ein einzelnes API-Modell nativ verarbeitet oder erzeugt. GPT-6 Astra beispielsweise verarbeitet Text und Bilder und gibt direkt Text aus. Audio-, Video- oder Bildgenerierung können im Produkt über zusätzliche Modelle und Werkzeuge hinzukommen. Deshalb lohnt die Unterscheidung zwischen Basismodell, API-Funktionen und gesamtem Produkt.

**Die Kostenentwicklung erweitert den nutzbaren Einsatzbereich erheblich.** Epoch schätzt im September, dass die Kosten eines gegebenen benchmarkbasierten Leistungsniveaus seit 2023 im Mittel um etwa 47 Prozent pro Quartal gefallen sind. Die Studie berücksichtigt Leistungs-/Kostenkurven, warnt aber vor Benchmarkoptimierung, unvollständigen Daten und einer idealisierten Auswahl des jeweils günstigsten Modells. Diese historische Schätzung ist keine Zusage entsprechender Einsparungen für jede Anwendung. [Epoch: The plunging price of thought](https://epoch.ai/publications/the-plunging-price-of-thought)

Die folgenden Preise sind ein **API-Snapshot vom 13. Oktober 2026**, in US-Dollar je Million Tokens. Es handelt sich um regulären Input ohne Cache und Output im Standardmodus; besondere Verarbeitungstarife, Werkzeuge und Nacharbeit sind nicht eingerechnet.

| Modell | Input | Output | Einschränkung / Quelle |
|---|---:|---:|---|
| GPT-6 Astra | 10,00 | 50,00 | Bis 272K Input; [Modellkarte](https://developers.openai.com/api/docs/models/gpt-6-astra) |
| GPT-6.1 Sol | 2,00 | 10,00 | Bis 272K Input; [Modellkarte](https://developers.openai.com/api/docs/models/gpt-6.1-sol) |
| GPT-6 Luna | 0,10 | 0,50 | Bis 272K Input; [Modellkarte](https://developers.openai.com/api/docs/models/gpt-6-luna) |
| Claude Fable 5.1 | 10,00 | 50,00 | Reguläre Tokenpreise; [Release](https://www.anthropic.com/claude-fable-and-mythos-5-1) |
| Claude Opus 5.5 | 4,00 | 20,00 | Reguläre Tokenpreise; [Release](https://www.anthropic.com/claude-opus-5-5) |
| Claude Sonnet 5.5 | 2,00 | 10,00 | Reguläre Tokenpreise; [Release](https://www.anthropic.com/claude-sonnet-5-5) |
| Claude Haiku 5.5 | 0,10 | 0,50 | Bis 100K Prompt; darüber 0,50/2,50; [Release](https://www.anthropic.com/claude-haiku-5-5) |
| Gemini 3.8 Flash | 0,75 | 3,75 | Einführungspreis bis Ende 2026; [Release](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) |
| Grok 4.7 | 2,00 | 6,00 | Kurzer Kontext; separate höhere Preise über 200K laut Modellseite; [Dokumentation](https://docs.x.ai/developers/models/grok-4.7) |

Eine reine Rechenillustration mit 100.000 Input- und 10.000 berechneten Outputtokens ergibt 1,50 Dollar für Astra, 0,30 Dollar für 6.1 Sol und 0,015 Dollar für Luna. Gleich viele Tokens bedeuten dabei weder gleiche Qualität noch gleiche tatsächliche Aufgabenlänge. Bei Reasoning können zusätzliche berechnete Tokens anfallen.

Bei GPT-6 steigen über 272.000 Inputtokens die Input- und Cachepreise auf das Doppelte und der Outputpreis auf das 1,5-Fache, für die gesamte Anfrage. Cache, schnellere Verarbeitung und Werkzeugkosten verändern die Rechnung zusätzlich. [OpenAI-Preise](https://developers.openai.com/api/docs/pricing)

Meine Empfehlung ist deshalb, **Kosten je akzeptiertem Ergebnis** zu messen. Dazu gehören Modellaufrufe, Reasoning, Tools, Wiederholungen und menschliche Nacharbeit. Ein teureres Modell kann bei schwierigen Aufgaben günstiger sein, wenn es weniger Fehlversuche verursacht. Ein günstiges Modell kann bei einfacher Verarbeitung die richtige Wahl sein.

**Die Benchmarks müssen stärker als Systemevaluation gelesen werden.** ARC Prize dokumentiert für GPT-6 Astra auf ARC-AGI-3 rund 62,7 Prozent mit dem Standard-Harness und rund 99,9 Prozent mit einem Provider-Adapter. Die besten genannten Ergebnisse verwenden unterschiedliche Reasoning-Einstellungen. Der Adapter bewahrt Reasoning-Zustand und verdichtet Kontext. Es ist also kein reiner Vergleich zweier Modellenamen und kein kontrollierter Vergleich nur einer veränderten Variable. [ARC-Prize-Ergebnisse](https://arcprize.org/results/openai-gpt-6-astra)

Epochs Automation Reports vom 8. Oktober testen elf Aufgaben aus der eigenen Arbeit mit sechs Modellen. Fable 5.1 und Astra führen insgesamt, aber offene Forschungsaufgaben und die Bewertung eigener Experimente bleiben problematisch. Die Grenzen des Tests sind ausdrücklich relevant: wenige Aufgaben, nur ein Lauf je Modell und Aufgabe, teilweise subjektive Bewertung und unterschiedliche Agent-Harnesses. Der Bericht zeigt konkrete Lücken; er quantifiziert nicht die Automatisierbarkeit aller Berufe. [Epoch Automation Reports](https://epoch.ai/publications/can-ai-automate-epoch)

METR definiert einen Aufgabenhorizont über die menschliche Bearbeitungsdauer und eine bestimmte Erfolgswahrscheinlichkeit. Ein 50-Prozent-Horizont bedeutet Erfolg bei ungefähr der Hälfte vergleichbarer Aufgaben, keine zuverlässige Arbeitszeit eines Agenten. Die veröffentlichte Seite wird seit September nicht mehr aktiv aktualisiert; außerdem bezeichnet METR Messungen über 16 Stunden mit der bestehenden Aufgabensuite als unzuverlässig. Sie eignet sich damit nicht als aktuelle Oktober-Bestenliste. [METR Time Horizons](https://metr.org/time-horizons/)

Aus diesen Beispielen leite ich vier Prüffragen ab: Welche Aufgaben wurden getestet? Welche Werkzeuge und welches Reasoning-Budget waren erlaubt? Wie wurden Fehler und Wiederholungen bewertet? Wie stark ähnelt der Test meinem tatsächlichen Arbeitsablauf? Ein kleiner Abstand zwischen Zahlen aus unterschiedlichen Benchmarkversionen beantwortet diese Fragen nicht.

**Für Softwareentwicklung und digitale Produkte ergibt sich eine differenzierte Strategie.** Ich würde ein leistungsfähiges Hauptmodell anhand repräsentativer eigener Aufgaben auswählen, etwa einer schwierigen Fehlerdiagnose, einer Änderung über mehrere Dateien und einer Dokumentanalyse mit widersprüchlichen Angaben. Billigere Modelle würde ich für klar begrenzte Arbeit prüfen: Klassifikation, strukturierte Extraktion, kurze Zusammenfassungen und Routing.

Bei jedem Vergleich sollten Ergebnisqualität, zusätzliche Rückfragen, Fehlversuche, Dauer, berechnete Tokens und menschliche Nacharbeit protokolliert werden. Ein Modellwechsel lohnt sich, wenn er im eigenen Aufgabensatz einen klaren Vorteil liefert. Höhere Modellversionen und größere Kontextfenster sind allein keine ausreichenden Gründe.

Für Coding bleibt ausführbares Feedback besonders wertvoll: Tests, Builds, tatsächliche UI-Prüfung und klare Abnahmekriterien. Bei langen Aufgaben sollten Anforderungen, Zwischenentscheidungen und offene Punkte explizit erhalten bleiben. Die Entwicklung hin zu besseren Agenten verringert diese Notwendigkeit bislang nicht; sie macht einen gut gestalteten Arbeitsablauf wertvoller.

**Der weitere Verlauf bleibt offen.** Aus den beobachteten Veröffentlichungen erwarte ich mehr Fähigkeiten in günstigen Modellstufen, bessere Verifikation und engere Integration von Modellen mit Werkzeugen. Das ist eine eigene Prognose. Die angekündigten Gewichts-Releases von Beam und Mistral Large 4 sowie eine breitere Argon-Freigabe müssen nach tatsächlicher Veröffentlichung neu bewertet werden.

Die belastbare Veränderung dieses Halbjahres ist ein größeres Spektrum wirtschaftlich nutzbarer KI-Arbeit. Ob ein bestimmter Agent einen vollständigen Arbeitsablauf zuverlässig übernehmen kann, bleibt eine Frage der Aufgabe, Umgebung und überprüften Erfolgsquote.

