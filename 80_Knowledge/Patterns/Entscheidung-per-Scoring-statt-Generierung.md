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

## Spannungen & offene Fragen

- Drei unabhängige Anbieter zeigen das Muster, gemessen ist bisher nichts davon. Die Konfidenz bleibt deshalb `meinung`, bis Messwerte zu Latenz, Kosten und Trefferquote vorliegen.
- Laya beschreibt seinen Ja/Nein-Fragetyp im Bild als `noul`, vermutlich ein Tippfehler für `bool` (2026-10-02 nicht verifiziert).

## Verwandte Patterns

- [[Lokale-Modell-Umleitung-Muster]]
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
