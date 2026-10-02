---
titel: "Entscheiden statt schreiben: Routing per Scoring"
datum: 2026-10-03
kategorie: arbeitsweisen
zusammenfassung: "Wenn die erlaubten Antworten feststehen, muss ein Modell keinen Text erzeugen. Fixed-Answer Scoring liest nach einem Durchlauf nur die Wahrscheinlichkeiten der Antwort-Labels. Was das für Klassifikation und Routing bringt, welche Regeln gelten und was bisher nicht gemessen ist."
status: freigegeben
geprueft_am: 2026-10-02
freigabe: automatisch
quellen:
  - 2026-09-20-avichawla-2101563610644496464
  - 2026-09-28-unslothai-2104592692072304916
  - 2026-09-29-openai-rueckblick-auf-den-devday-2026
---

## Kurz gesagt

- Steht der Antwortraum fest (Ticket-Routing, Filter, Ja/Nein-Gates), lies Wahrscheinlichkeiten für die Antworten aus, statt Text oder JSON generieren zu lassen.
- Baue immer eine Ausweichoption (OTHER, ESCALATE) ein und lege Schwellen im Code fest, nicht im Prompt.
- Eine Wahrscheinlichkeit ist keine Trefferquote. Prüfe sie an gelabelten Beispielen aus deinem eigenen Betrieb.
- Die Geschwindigkeits- und Kostenversprechen sind bisher nicht gemessen. Teste mit deinen Daten, bevor du umbaust.

Der Beitrag baut auf [Jev: ein Modell für typisierte Entscheidungen statt Text](post:jev-entscheidungsmodell-statt-textmodell) auf. Dort geht es um das Produkt, hier um die Technik dahinter und darum, wie du sie selbst einsetzt.

## Das Problem mit Text als Antwort

Ein Support-Ticket („doppelt abgebucht“) soll an Billing, Technical Support oder Account Access gehen. Ein normaler Modellaufruf lässt das Modell einen Satz oder ein JSON-Objekt schreiben, das deine Anwendung danach wieder parsen muss.{q:1} Auch Structured Output ändert daran wenig: Es garantiert ein schemagültiges Objekt, aber das Modell erzeugt Klammern, Feldnamen und Werte weiterhin Token für Token.{q:1} Für eine Entscheidung zwischen drei bekannten Zielen ist das mehr Arbeit als nötig.

## So funktioniert Scoring

Jede erlaubte Antwort bekommt ein Label, das genau ein Token ist: A, B, C. Was A, B und C bedeuten, steht im Prompt, der Prompt endet dort, wo das Label folgen würde. Das Modell rechnet den Prompt einmal durch (Prefill) und liefert für die nächste Position einen Wert pro Token des Vokabulars, die Logits. Du liest nur die Logits der drei Labels und wendest Softmax ausschließlich darauf an.{q:1} Im Beispiel der Quelle ergeben die Werte 8,2, 5,5 und 4,8 etwa 0,91, 0,06 und 0,03.{q:1}

Lokal geht das mit SGLang über den Endpunkt `/v1/score`. Avi Chawla zeigt es mit einem kleinen Qwen-Modell mit 0,5 Milliarden Parametern; die Anwendung sieht nur die semantischen Antworten, die Labels bleiben im Scoring-Client.{q:1} Du sparst die Generierungsschleife und das Parsen, und du bekommst eine Verteilung statt einer Behauptung. Im Beispiellauf gewinnt Billing mit nur 0,678; bei einer Schwelle von 0,70 ginge dieses Ticket in die manuelle Prüfung.{q:1}

## Wann das passt, wann nicht

Einsetzen bei bekanntem, endlichem Antwortraum: Ticket-Routing, E-Mail-Filter, Tagging, Ja/Nein-Gates, die Wahl der nächsten Agent-Aktion.{q:3} Nicht einsetzen, wenn der Inhalt der Antwort erst entstehen muss oder die Antwortmenge offen ist. Für Extraktion und freie Felder (Rechnungsnummer, Betrag, Zusammenfassung) bleibt Structured Output das richtige Mittel. Die Faustregel der Quelle: Generieren, wenn der Inhalt vorher unbekannt ist; scoren, wenn Auswahl genügt.{q:1}

Auch die Eingabe zählt. Das kleinste Laya-Modell hat 678 MB und 1024 Token Kontext, die Variante für Englisch nur 512.{q:2} Lange Tickets oder Agent-Traces musst du kürzen, bevor du sie scorst.

## Fünf Praxisregeln

**Single-Token-Labels prüfen.** Ganze Wörter können mehrere Tokens belegen, dann wäre Sequenz-Scoring samt Längeneffekt nötig. Buchstaben vermeiden das. Aber „A“ und „A“ mit führendem Leerzeichen sind verschiedene Tokens (im Bild der Quelle die IDs 32 und 362). Rendere den vollständigen Prompt mit dem echten Chat-Template, schicke die exakte Fortsetzung an `/tokenize` und lehne Labels mit mehr als einem Token ab. Das gilt für jeden Tokenizer neu.{q:1}

**Eine Ausweichoption einbauen.** Ohne OTHER oder ESCALATE verteilt Softmax die ganze Wahrscheinlichkeit auf falsche Optionen. Im Beispiel der Quelle ist das ein Security-Incident, der in einem Support-Router landet und irgendeinem der drei Ziele zugeschlagen wird.{q:1}

**Schwellen im Code festlegen.** Ein Beispiel aus der Quelle: Die beste Antwort liegt über 0,80 und mindestens 0,20 vor der zweiten. Knappe Fälle gehen ins Review.{q:1} Solche Regeln kannst du testen und ändern, ohne den Prompt anzufassen.

**Wahrscheinlichkeit nicht mit Trefferquote verwechseln.** 0,91 heißt, dass 91 Prozent der Wahrscheinlichkeit innerhalb der Kandidaten auf dieser Antwort liegen, nicht dass die Antwort in 91 Prozent der Fälle stimmt. Dafür brauchst du gelabelte Beispiele und eine Kalibrierung.{q:1} Laut Autor ist sie pro Modell, Quantisierung und Label-Set nötig; über verschiedene Backends hinweg hat er sie nicht getestet.{q:1}

**Das ganze Bündel versionieren.** Die Wahrscheinlichkeiten hängen von der Kandidatenmenge ab, ein zusätzliches Label verschiebt alle anderen. Ausgeliefert wird deshalb immer Modell, Prompt, Tokenizer, Label-Set und Schwellen zusammen.{q:1}

## Was fehlt

Die Mechanik ist gut erklärt, Messwerte fehlen. Auf dem Cover von Chawlas Artikel steht „200x faster and 400x cheaper than LLMs“, im Text wird die Zahl nicht hergeleitet, Ergebnisse zeigen nur Videos.{q:1} Der Vergleichsaufbau ist zudem günstig für Scoring gewählt: Die Generierungsseite erzeugt bis zu 32 Token Erklärtext und wird per Textsuche geparst.{q:1} Zu Latenz und Kosten hast du also keine belastbare Zahl, auch Unsloth nennt für Laya keine Messwerte zu Qualität oder Latenz.{q:2}

Zwei weitere Grenzen. Der lokale Nachbau reproduziert nur den Inferenzweg, nicht das Training und die Kalibrierung spezialisierter Decision-Modelle.{q:1} Und es kostet Aufwand: Labeling, Kalibrierung, Versionierung und eigene Inferenz-Infrastruktur (GPU, SGLang).{q:1}

## Drei Wege zum Ausprobieren

| Weg | Was du brauchst | Stand |
|---|---|---|
| Lokal mit SGLang `/v1/score` | Eigener Server, offenes Modell, Label-Prompt | Funktioniert ohne Training; Kalibrierung musst du selbst bauen{q:1} |
| Lokal mit Unsloth Desktop und Laya | Mindestens 4 GB RAM, CPU genügt | Herstellerangabe vom 28.09.2026; Fragetypen Ja/Nein, `choice` und `score`; Daten bleiben auf dem Gerät{q:2} |
| Gehostet mit OpenAIs Decisions API | Zugang zur Vorschau | Angekündigt am 29.09.2026; richtet Luna auf einen eigenen Fragenkatalog mit begrenzten Antworten aus; begrenzte Vorschau{q:3} |

Bei Laya kannst du bestehende Jev-Integrationen auf den lokalen Server umlenken.{q:2} Zur Decisions API gibt es bisher nur die Ankündigung von OpenAI, Preise und Messwerte nennt sie nicht.{q:3}

## Empfehlung

Such dir einen Router oder ein Gate, das du heute mit einem Textmodell betreibst und dessen Antworten du kennst. Sammle 100 bis 200 echte Fälle mit richtigem Label und lass Scoring im Schattenbetrieb mitlaufen. Miss Latenz und Kosten selbst, lege die Schwellen anhand der Fehler fest und automatisiere zuerst die Fälle, in denen die Verteilung eindeutig ist. Alles Knappe geht weiter an ein Review oder ein stärkeres Modell.
