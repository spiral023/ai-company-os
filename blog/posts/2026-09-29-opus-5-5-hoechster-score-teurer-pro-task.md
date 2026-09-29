---
titel: "Opus 5.5: Höchster Score, niedrigerer Preis, teurere Aufgabe"
datum: 2026-09-29
kategorie: modelle
zusammenfassung: "Der Listenpreis sinkt um 20 %, die Kosten pro Coding-Aufgabe steigen um 21 %. Warum beides stimmt und welche Effort-Stufe sich für die eigene Arbeit lohnt."
status: entwurf
quellen:
  - 2026-09-22-artificialanlys-2102438210798514391
  - 2026-09-24-artificialanlys-2102932119995756613
  - 2026-09-23-artificialanlys-2102833926788288704
  - 2026-09-22-claude-getting-the-most-out-of-opus-5-5-in-claude-and-c
---

## Kurz gesagt

- Claude Opus 5.5 führt beide relevanten Indizes von Artificial Analysis an: Intelligence Index 58 (der höchste bisher gemessene Wert) und Coding Agent Index 66 (Opus 5: 60, Fable 5.1: 62).
- Der Preis pro Token sinkt um 20 %, der Verbrauch pro Aufgabe steigt stärker. Im Coding Agent Index kostet eine Aufgabe $13,04 statt $10,79.
- Vier der fünf Effort-Stufen liegen auf der Kosten-Leistungs-Kurve. Interessant ist deshalb weniger `max` als die Stufen darunter.

## Die Zahlen

Alle Werte stammen von Artificial Analysis, einer unabhängigen Messung. Die Kosten pro Aufgabe beziehen sich auf jeweils denselben Index.

| | Opus 5 | Opus 5.5 |
|---|---|---|
| Preis Input/Output pro 1 Mio. Tokens | $5 / $25 | $4 / $20 |
| Cache-Lesezugriff pro 1 Mio. Tokens | $0,50 | $0,20 |
| Coding Agent Index (Claude Code, `max`) | 60 | 66 |
| Terminal-Bench 4.0 im Coding Agent Index | 54,5 % | 63,1 % |
| DeepSWE v1.1 | 62,5 % | 68,4 % |
| Kosten pro Aufgabe, Coding Agent Index | $10,79 | $13,04 |
| Tokens pro Aufgabe, Coding Agent Index | 11,4 Mio. | 15,6 Mio. |

Der Cache-Rabatt liegt jetzt bei 95 % gegenüber unverändertem Input (vorher 90 %). Das Kontextfenster bleibt bei 1 Million Tokens.

## Warum ein billigeres Modell mehr kostet

Der Preis pro Token sinkt, aber die Anzahl der Tokens pro Aufgabe steigt stärker. Im Coding Agent Index erzeugt Opus 5.5 etwa das 2,4-Fache an Output-Tokens von Opus 5. Im Intelligence Index sind es rund 119.000 Output-Tokens pro Aufgabe, gegenüber 73.000 bei Opus 5 und 27.000 bei GPT-6 Astra. Dort gleicht der Preisnachlass den Mehrverbrauch aus, die Kosten pro Aufgabe bleiben auf dem Niveau von Opus 5. Im Coding Agent Index reicht er nicht: Die Kosten steigen um 21 %.

Wer sein Budget nach Listenpreisen plant, unterschätzt Opus 5.5 also. Maßgeblich sind die Kosten pro erledigter Aufgabe, und die zeigen erst eine Messung am eigenen Workload.

## Die Effort-Stufen sind der eigentliche Hebel

Opus 5.5 hat fünf Stufen: `low`, `medium`, `high`, `xhigh` und `max`. Laut Artificial Analysis liegen `max`, `xhigh`, `high` und `medium` auf der Kurve aus Intelligence Index und Kosten pro Aufgabe. Gegenüber den anderen Modellen mit mindestens 50 Punkten in dieser Messung (GPT-6 Astra, Fable 5.1, Opus 5) sind diese Stufen jeweils billiger oder besser.

Im Vergleich mit der Konkurrenz (Intelligence Index, jeweils `max`):{q:3}

| Modell | Score | Kosten pro Aufgabe |
|---|---|---|
| GPT-6 Luna | 37 | $0,068 |
| MiMo-V2.6-Pro | 46 | $0,13 |
| GPT-6 Sol | 48 | $1,06 |
| Claude Opus 5.5 | 58 | $5,98 |

Opus 5.5 liefert zehn Punkte mehr als Sol und kostet das 5,6-Fache (eigene Rechnung). Ob sich das lohnt, hängt davon ab, was ein Fehlversuch bei dir kostet. Für Routinearbeit mit klarer Verifikation ist Sol oder MiMo die rationalere Wahl. Für lange, mehrstufige Aufgaben ohne engmaschige Aufsicht rechtfertigt sich der Aufpreis eher.

## Was sich beim Prompting ändert

Der Herstellerguide zu Opus 5.5 nennt vier Verschiebungen, die direkt in die `CLAUDE.md` gehören. Das sind Empfehlungen des Herstellers, keine unabhängigen Messungen:{q:4}

1. **Fertig-Kriterium statt Anleitung.** Die Aufgabe in einer Nachricht geben, dazu was „done“ heißt („Tests laufen, alter Client gelöscht“) und wann das Modell nachfragen soll.
2. **„Denk sorgfältig“ streichen.** Das Modell denkt vor jeder Antwort ohnehin. Laut Guide starten Antworten ohne diese Zeile früher, ohne erkennbaren Qualitätsverlust.
3. **Stopps benennen.** Auf langen Läufen bricht das Modell manchmal mit einem Statusbericht ab. Abhilfe ist eine Regel: bei Schritten ohne Rückfrage weitermachen, nur bei Blockaden oder Destruktivem fragen (Daten löschen, Force-Push, Änderungen außerhalb des Repos).
4. **Aufgabenliste in eine Datei.** Eine `TASKS.md` überlebt die Kontext-Zusammenfassung und zeigt, was fertig ist.

## Einordnung

- **Belegt** ist der Sprung in den Indizes: Er kommt von einem unabhängigen Anbieter mit veröffentlichten Benchmarks. **Nicht belegt** ist, dass sich die Werte auf deinen Workload übertragen lassen.
- Zwei Terminal-Bench-Werte kursieren: 59,6 % (Harness des Intelligence Index, gleichauf mit GPT-6 Astra auf `xhigh`) und 63,1 % (Claude Code). Sie stammen aus verschiedenen Harnesses und lassen sich nicht direkt vergleichen.
- Artificial Analysis nennt auch Schwächen: Bei CritPt, AA-LCR und GDP.pdf liegt Opus 5.5 leicht hinten.
- Die Preisangaben gelten zum Stand 22.09.2026 und können sich ändern.

## Empfehlung

Setze Opus 5.5 zunächst auf `medium` oder `high` und miss die Kosten pro Aufgabe an einer eigenen Stichprobe, etwa zehn typischen Tickets. `max` lohnt sich nur dort, wo ein Fehlschlag teurer ist als ein Vielfaches an Tokens. Für einfache, gut verifizierbare Aufgaben lohnt der Blick auf GPT-6 Sol oder MiMo-V2.6-Pro.
