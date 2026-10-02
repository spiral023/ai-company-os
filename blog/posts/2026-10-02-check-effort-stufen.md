---
titel: "Welche Effort-Stufe stimmt? Fünf Aussagen im Check"
datum: 2026-10-03
kategorie: check
zusammenfassung: "Vier Stimmen derselben Woche empfehlen vier verschiedene Effort-Stufen. Fünf Aussagen zur richtigen Reasoning-Einstellung im Check: Zwei stimmen, drei lassen sich nicht prüfen."
status: freigegeben
geprueft_am: 2026-10-02
freigabe: automatisch
quellen:
  - 2026-09-29-voxyz_ai-2105012597796057438
  - 2026-09-29-artificialanlys-2105025585332605357
  - 2026-09-22-promptgefluester-ich-arbeite-mit-multiorgastation-und-das-hat-was-mit-meinem-tokenlimit
  - 2026-09-28-claude-building-with-claude-sonnet-5-5-claude-dev-blog
  - 2026-09-28-artificialanlys-2104640155843989864
  - 2026-09-25-voxyz_ai-2103586663393853636
  - 2026-09-25-trq212-2103576349499855160
  - 2026-09-27-voxyz_ai-2104254744722383210
  - 2026-09-29-voxyz_ai-2104919123918479521
---

## Kurz gesagt

- Eine allgemein richtige Effort-Stufe gibt es nicht. Wer `max` als Standard setzt, zahlt oft für nichts.
- Fang bei `medium` an, miss deine eigene Aufgabe und gib die teuerste Stufe nur dem Schritt mit wenig Output und hoher Tragweite.
- Nach jedem Modellwechsel die Stufe neu ausmessen, alte Einstellungen tragen nicht.

## Das Ergebnis

| Nr. | Aussage | Urteil |
|---|---|---|
| 1 | Bei GPT-6.1 Sol schneidet `high` am besten ab, `xhigh` und `max` schlechter | nicht prüfbar |
| 2 | `medium` liegt etwa 2 Punkte unter `high` bei über 30 % weniger Kosten pro Task {q:1} | nicht prüfbar |
| 3 | `xhigh` zum Programmieren, `max` nur für den Orchestrator | nicht prüfbar |
| 4 | Sonnet 5.5: Stufen neu kalibriert, Start bei `medium` | stimmt |
| 5 | Mehr Effort kauft vor allem Verifikation und Randfalltests | stimmt |

## 1. „Bei GPT-6.1 Sol ist `high` am besten“

Vox empfiehlt für Codex `high` für den Orchestrator und beruft sich auf ein DeepSWE-Chart von OpenAI: `high` vorn, `xhigh` und `max` dahinter {q:1}. Das Chart liegt uns nicht vor, die Aussage kommt aus zweiter Hand und vom Hersteller selbst.

Artificial Analysis misst im Coding Agent Index etwas anderes: `xhigh` liegt 3 Punkte über `max` und 1 Punkt über `GPT-6 Astra`, bei unter 15 % von dessen Kosten {q:2}. Das ist ein anderer Benchmark, also kein direkter Widerspruch. Beide Messungen sagen aber dasselbe: `max` gewinnt nicht automatisch. Welche der beiden Stufen unter `max` vorn liegt, hängt vom Benchmark ab. Urteil: nicht prüfbar. Für deine Aufgabe sagt keine der Zahlen etwas.

## 2. „`medium` kostet 2 Punkte, spart aber über 30 %“

Dieselbe Quelle nennt für `medium` etwa 2 Punkte Rückstand auf `high` bei über 30 % geringeren Kosten pro Task {q:1}. Die Zahl stammt aus dem Herstellerchart und steht in keiner unabhängigen Messung. Artificial Analysis stützt nur die Richtung: Bei GPT-6.1 Sol sind `low` und `medium` auch token-effizient auf der Pareto-Front {q:2}. Die konkreten 2 Punkte und 30 % bleiben unbestätigt. Urteil: nicht prüfbar, die Richtung ist plausibel.

## 3. „`xhigh` zum Programmieren, `max` nur für den Orchestrator“

@promptgefluester empfiehlt das aus der Praxis. Der Orchestrator erzeuge wenig Output, deshalb sei `max` dort billig, `low` reiche oft für den Rest {q:3}. Es gibt keine Messung dazu, und im selben Video wirbt der Creator für ein eigenes Tool. Die Empfehlung widerspricht den Startwerten von Anthropic (siehe Punkt 4), und Vox staffelt ähnlich vorsichtig: `low` für Recherche, `medium` für Schreiben, `high` für Review, `xhigh` nur für die Entscheidung {q:8}.

Der Gedanke dahinter trägt: Die teuerste Stufe gehört dorthin, wo wenig Text entsteht und viel an der Entscheidung hängt. Dass sie zum Programmieren die richtige ist, zeigt keine der Quellen. Urteil: nicht prüfbar.

## 4. „Stufen neu kalibriert, Start bei `medium`“

Anthropics Leitfaden zu Sonnet 5.5 sagt genau das: Die Stufen sind neu kalibriert, ein alter Wert trägt nicht. Start bei `medium` für gut spezifizierte agentische Aufgaben, `high` für schwerere oder längere, `xhigh` und `max` nur, wenn deine Evals einen Gewinn zeigen {q:4}. Vox verpackt das als Audit-Prompt, der hart codierte Stufen im eigenen Setup sucht {q:9}.

Der Rat passt zur Drittmessung. Artificial Analysis sieht Sonnet 5.5 bei `max` mit rund 193.000 Output-Tokens pro Task und 7,60 US-Dollar Kosten, etwa 50 % mehr als bei Sonnet 5, bei gleichem Token-Preis. `high` ist dort die konkurrenzfähigste Stufe {q:5}. Das Kostenversprechen „bis zu 30 % weniger“ aus dem Leitfaden gilt also nicht für `max`. Urteil: stimmt.

## 5. „Mehr Effort kauft Verifikation“

Thariq von Anthropic hat bei Fable 5.1 je 370 Läufe auf `low` und `max` verglichen. Übersehene Randfälle sanken von 59 auf 24. Falsche Grundentscheidungen sanken nur von 133 auf 107, und „falsch gelesene Aufgabe“ stieg sogar von 25 auf 47 {q:7}. Mehr Effort bringt also gründlichere Prüfung, aber keinen besseren Ansatz. Die Zahlen sind eine Selbstmessung des Herstellers, die Richtung ist aber klar und konsistent. Der Preis: rund dreifache Tokens bei etwa 20 Prozentpunkten mehr bestandenen Aufgaben.

Daraus folgt „Build on low, verify on high“: ein Builder auf `low`, ein Verifier auf `high`, der das Feature ausführt, Randfälle testet und selbst keinen Code ändert {q:6}. Urteil: stimmt.

## Was daraus folgt

Die Widersprüche lösen sich auf, wenn man sie nach Rolle sortiert. Aufgabe, Modell und Benchmark unterscheiden sich, deshalb passen die Empfehlungen nicht zusammen. Es gibt zwei Gruppen:

- Wer günstig baut und teuer prüft, landet bei `low` oder `medium` für die Umsetzung und `high` für die Verifikation.
- Wer einen Entscheider einsetzt, gibt ihm die höchste Stufe, weil dort wenig Text entsteht.

Beides ist dieselbe Regel: Die Kosten der hohen Stufe sind dort gut angelegt, wo wenig Output auf viel Tragweite trifft. Für den Rest zählen die Kosten pro Aufgabe, nicht der Preis pro Token. Das zeigt auch der [Beitrag zu Opus 5.5](post:opus-5-5-hoechster-score-teurer-pro-task).

## Was du tun solltest

1. Starte mit `medium` und miss an zehn echten Aufgaben aus deinem Alltag, wie oft du nacharbeiten musst. Erst dann gehst du hoch oder runter.
2. Suche in deinem Setup nach hart codierten Stufen und nach Subagents ohne eigene Modellangabe. Beides erbt sonst, was die Hauptsitzung hat.
3. Gib `high` oder `xhigh` dem Reviewer vor größeren Änderungen und dem Entscheider im Workflow, nicht dem Builder.
4. Setze `max` nicht als Standard. Nutze es nur, wenn deine eigene Messung einen Gewinn zeigt.
5. Wiederhole die Messung nach jedem Modellwechsel.
