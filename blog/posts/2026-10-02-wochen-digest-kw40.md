---
titel: "KW 40: GPT-6.1 Sol fast auf Astra-Niveau, Sonnet 5.5 schluckt Tokens, Gemini ist zurück"
datum: 2026-10-03
kategorie: digest
zusammenfassung: "Wochen-Digest KW 40 (28.09. bis 04.10.2026): GPT-6.1 Sol kommt für ein Viertel der Kosten an GPT-6 Astra heran, Sonnet 5.5 senkt die Kosten laut Anthropic und steigert sie laut Artificial Analysis, Gemini 4 Argon zieht gleich."
status: freigegeben
geprueft_am: 2026-10-02
freigabe: automatisch
quellen:
  - 2026-09-29-artificialanlys-2105025585332605357
  - 2026-10-01-artificialanlys-2105491868608004578
  - 2026-09-22-kimmonismus-2102462091299098640
  - 2026-09-29-openai-rueckblick-auf-den-devday-2026
  - 2026-09-29-thsottiaux-2104823812042940713
  - 2026-09-28-artificialanlys-2104640155843989864
  - 2026-09-28-claude-building-with-claude-sonnet-5-5-claude-dev-blog
  - 2026-09-30-artificialanlys-2105392625788637299
  - 2026-09-22-epoch-the-plunging-price-of-thought
  - 2026-09-29-openclaw-openclaw-enterprise-the-open-agent-platform-open
  - 2026-10-01-julian-ivanov-ki-automat-claude-code-ist-unglaublich-gut-in-motion-graphi
---

## Kurz gesagt

- Vergleiche Modelle nach Kosten pro Aufgabe, nicht nach Preis pro Million Token: Diese Woche gehen beide Zahlen bei Sonnet 5.5 auseinander.
- GPT-6.1 Sol ist für viele Coding-Aufgaben die günstigste Wahl im oberen Leistungsbereich, Gemini 4 Argon ist noch nicht öffentlich.
- Prüfe nach jedem Modellwechsel Effort-Stufe und Eval-Ergebnisse neu, statt alte Einstellungen zu übernehmen.

## 1. GPT-6.1 Sol: vier Punkte mehr in sieben Tagen

Eine Woche nach GPT-6 Sol, das laut OpenAI-Ankündigung bei Preis pro Task weit unter Fable 5.1 lag {q:3}, löst GPT-6.1 Sol den Vorgänger ab. Artificial Analysis misst 52 Punkte im Intelligence Index bei `max`, GPT-6 Astra kommt auf 53, GPT-6 Sol auf 48. Die Kosten pro Task liegen bei 0,72 US-Dollar gegen 3,26 für Astra {q:1}. Der Token-Preis bleibt bei 2/10 US-Dollar je Million Token, der Verbrauch steigt um 10 bis 30 Prozent {q:1}. Ein Nachtrag vom 01.10. bestätigt: Für kein Intelligenzniveau gibt es ein günstigeres OpenAI-Modell, auf allen Effort-Stufen. Ein behobener Fehler im Bildencoding hob außerdem GPT-6 Luna um einen Punkt {q:2}. Für den Effort-Hebel selbst lohnt der [Effort-Check](post:check-effort-stufen).

## 2. DevDay: Agenten, Entscheidungen, Geschwindigkeit

OpenAI nennt über 20 Neuerungen, alles Herstellerangaben {q:4}. Die wichtigsten: `dots` als dauerhaft laufende Agenten mit eigenem Cloud-Computer, die Agents API mit verwaltetem Codex-Harness, ein Pro-Tarif für 500 US-Dollar und Ultrafast mit bis zu 8-facher Token-Geschwindigkeit in Codex. Die Decisions API wählt aus vorgegebenen Antworten statt Text zu erzeugen, mehr dazu in [Routing per Scoring statt Text](post:routing-per-scoring-statt-text).

## 3. Codex Pro: halbes Volumen, kein Fünf-Stunden-Limit

Das Pro-Abo für 200 US-Dollar öffnet wieder für Neukunden, rechnet die Nutzung aber auf rund den halben API-Gegenwert um. Ein Fünf-Stunden-Limit soll nicht zurückkehren {q:5}. Das ist eine Ankündigung aus dem Codex-Umfeld; wie viel Arbeit pro Dollar tatsächlich herauskommt, ist nicht gemessen.

## 4. Sonnet 5.5: billiger oder teurer, je nach Messung

Der Token-Preis bleibt bei 2/10 US-Dollar. Anthropic verspricht bis zu 30 Prozent geringere Kosten durch weniger Tokens pro Aufgabe {q:7}. Artificial Analysis misst bei `max` 7,60 US-Dollar pro Task, rund 50 Prozent mehr als Sonnet 5, bei etwa 193.000 Output-Token und 56 Indexpunkten {q:6}. Beide Aussagen stehen nebeneinander: Anthropic spricht von den meisten Aufgaben, die Messung betrifft die höchste Stufe, und gemessen wurde ein Vorab-Deployment. Der Leitfaden rät, den Effort-Sweep neu zu fahren und `medium` als Start zu wählen {q:7}.

## 5. Gemini 4 Argon: Gleichstand, aber nicht für alle

Argon erreicht 53 Punkte, gleichauf mit Astra, bei 1,99 US-Dollar pro Task. Das gilt für einen befristeten Rabatt, regulär sind es 3,98 US-Dollar. Das Modell ist nur für ausgewählte Nutzer freigeschaltet {q:8}. Die Halluzinationsrate liegt bei 15 Prozent, die Genauigkeit aber nur bei 50 Prozent. Plane damit noch nicht.

## 6. Preise fallen, Kosten pro Task nicht automatisch

Epoch AI beziffert den Rückgang der Kosten für ein festes Leistungsniveau auf rund 47 Prozent pro Quartal, je nach Methode zwischen 43 und 58 Prozent {q:9}. Für die Preise der jeweils stärksten Modelle gilt der Rückgang nicht. Steigt zudem der Tokenverbrauch pro Aufgabe, kann er ihn aufzehren, wie Sonnet 5.5 bei `max` zeigt {q:6}. Wie du solche Änderungen absicherst, steht in [Hillclimbing mit Holdout](post:hillclimbing-mit-holdout).

## 7. OpenClaw Enterprise: Governance für Dauer-Agenten

Die OpenClaw Foundation kündigt eine offene Control Plane für dauerhaft laufende Agenten an, entwickelt mit Red Hat und NVIDIA {q:10}. Zusammen mit `dots` und der Agents API zeigt sich ein Trend zu Agenten, die ohne Sitzung weiterlaufen. Es ist eine Ankündigung vor Version 1.0, eine Referenzarchitektur fehlt noch.

## 8. Videos aus Code

Ein Creator baut in drei Selbsttests mit Claude Code, Opus 5.5 und HyperFrames Motion Graphics {q:11}. Die Ergebnisse sind nur im Video zu sehen, prüfen kannst du sie nicht, als Anregung taugt es.

## Was du jetzt tust

Rechne Kosten pro Task mit deinen eigenen Aufgaben nach, bevor du wechselst, und lies im [Repo-Radar](post:repo-radar-kw40) nach, was sich bei den Werkzeugen getan hat. Den Rückblick auf die Vorwoche findest du im [Wochen-Digest KW 39](post:wochen-digest-kw39).
