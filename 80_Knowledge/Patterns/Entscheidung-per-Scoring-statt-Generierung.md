# Entscheidung-per-Scoring-statt-Generierung

**Konfidenz:** meinung

## Zweck

Löst Klassifikation, Routing und Gating, bei denen die erlaubten Antworten vorher feststehen, ohne das Modell Text oder JSON schreiben zu lassen. Ergebnis ist eine Wahrscheinlichkeitsverteilung über die Antworten statt eines geparsten Satzes, schneller und mit sichtbarer Entscheidungssicherheit.

## Funktionsweise

Jede erlaubte Antwort bekommt ein Label, das genau ein Token ist (A, B, C); die Bedeutung steht im Prompt. Der Prompt endet an der Stelle, an der das Label folgen würde. Ein einziger Durchlauf (Prefill) liefert die Logits für die nächste Position; gelesen werden nur die Logits der Label-Tokens, ein Softmax über genau diese ergibt die Verteilung. Lokal geht das z. B. mit SGLang `/v1/score`.

Praxisregeln aus den Belegen:

- Single-Token-Eigenschaft jedes Labels mit dem echten Chat-Template prüfen (`/tokenize`); `"A"` und `" A"` können verschiedene Tokens sein.
- Immer eine Ausweichoption wie OTHER oder ESCALATE anbieten, weil der eingeschränkte Softmax sonst alle Masse auf falsche Antworten verteilt.
- Schwellen im Code statt im Prompt, z. B. beste Antwort über 0,80 und mindestens 0,20 Abstand zur zweiten; knappe Fälle gehen ins Review.
- Die Verteilung ist keine Trefferquote: 0,91 heißt nur, dass 91 % der Masse innerhalb der Kandidaten auf dieser Antwort liegen. Kalibrierung braucht gelabelte Beispiele.
- Die Wahrscheinlichkeiten hängen von der Kandidatenmenge ab. Ausgerollt wird daher immer das Bündel aus Modell, Prompt, Tokenizer, Label-Set und Schwellen.

**Ergänzung 2026-10-09:** [[2026-10-07-unslothai-decision-model-finetuning]] beschreibt mit [[Decision-Head-Finetuning]] einen trainierten Decision-Head plus LoRA als zweite Umsetzung des festen Antwortraums. Das unterscheidet sich vom oben beschriebenen eingeschränkten Softmax über Label-Tokens. Eigene Trainingsdaten und Kalibrierung werden damit zu zusätzlichen Arbeitsschritten.

## Vorteile

- Kein autoregressiver Decoding-Loop, kein Parsen von Freitext oder JSON.
- Die Sicherheit der Entscheidung ist sichtbar und in Code testbar.
- Läuft mit kleinen lokalen Modellen; Daten bleiben auf dem Gerät.

## Nachteile & Grenzen

- Nur bei vorab bekanntem, endlichem Antwortraum; für Extraktion und freie Felder bleibt Structured Output das Mittel.
- Geschwindigkeits- und Kostenvorteile sind bisher behauptet, nicht im Text gemessen.
- Der lokale Nachbau reproduziert nur den Inferenzweg, nicht Training und Kalibrierung spezialisierter Decision-Modelle.

## Wann einsetzen, wann nicht

- Einsetzen: Ticket-Routing, E-Mail-Filter, Tagging, Ja/Nein-Gates, Auswahl der nächsten Agent-Aktion.
- Nicht einsetzen: wenn der Inhalt der Antwort erst erzeugt werden muss oder die Antwortmenge offen ist.

## Belege

- 2026-09-20 · [[2026-09-20-avichawla-2101563610644496464]] · meinung — Erklärt die Mechanik (Prefill, eingeschränkter Softmax, SGLang `/v1/score`) und die Praxisregeln samt Kalibrierungsgrenze; „200x faster, 400x cheaper“ auf dem Cover ohne Messwerte im Text.
- 2026-09-28 · [[2026-09-28-unslothai-2104592692072304916]] · meinung — Produktisiert als lokales Decision-Modell Laya über Unsloth Desktop ab 4 GB RAM mit Fragetypen Ja/Nein, `choice` und `score`.
- 2026-09-29 · [[2026-09-29-openai-rueckblick-auf-den-devday-2026]] · meinung — OpenAI kündigt eine Decisions API an: Luna auf einen festen Fragenkatalog mit begrenzten Antworten, zum Klassifizieren, Weiterleiten und zur Wahl der nächsten Agent-Aktion; Herstellerankündigung, begrenzte Vorschau.

- 2026-10-07 · [[2026-10-07-unslothai-decision-model-finetuning]] · meinung — Unsloth berichtet für einen Clef-Head plus LoRA bei Qwen3.5-0.8B aggregierte Accuracy von 20,7 % auf 74,3 % über drei Decision-Benchmarks und 78 % auf Holdout. Herstellerbericht ohne eigene Reproduktion oder Kalibrierungsmessung; Training und Inferenz sind getrennte Ressourcenangaben.

## Spannungen & offene Fragen

- Drei unabhängige Anbieter zeigen das Muster, gemessen ist bisher nichts davon. Die Konfidenz bleibt deshalb `meinung`, bis Messwerte zu Latenz, Kosten und Trefferquote vorliegen.
- Laya beschreibt seinen Ja/Nein-Fragetyp im Bild als `noul`, vermutlich ein Tippfehler für `bool` (2026-10-02 nicht verifiziert).
- **Korrektur 2026-10-02:** `Noul` ist kein Tippfehler, sondern TypeSafes eigener Name für den Ja/Nein-Typ von Jev (neben `Choice` und `Score`), siehe [[2026-09-18-akshay_pachaar-2101037514945597645]]. Laya übernimmt damit Jevs Benennung, was zur Jev-kompatiblen API passt. Die Vermutung oben ist damit überholt.

- **Ergänzung 2026-10-09:** Die frühere Aussage, es gebe keine Messwerte, ist durch Unsloths Accuracy-Tabelle zeitlich überholt. Unabhängige Qualitäts-, Latenz-, Kosten- und Kalibrierungsmessungen fehlen weiterhin; Post und Guide stammen vom selben Anbieter und erhöhen die Konfidenz deshalb nicht. → [[2026-10-07-unslothai-decision-model-finetuning]]

## Verwandte Patterns

- [[Lokale-Modell-Umleitung-Muster]]
- [[Decision-Head-Finetuning]]
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
