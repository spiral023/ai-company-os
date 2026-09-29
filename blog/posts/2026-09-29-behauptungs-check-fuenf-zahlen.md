---
titel: "Stimmt das? Fünf Aussagen aus der KI-Szene im Faktencheck"
datum: 2026-09-30
kategorie: check
zusammenfassung: "Fine-Tuning sei tot, 94 Commits an einem Tag, 93 % zu 76 % Kontext-Recall, gefühlt schneller und gemessen langsamer, weniger Halluzinationen bei GPT-6: fünf Aussagen und was an ihnen dran ist."
status: freigegeben
geprueft_am: 2026-09-29
freigabe: automatisch
quellen:
  - 2025-12-31-natebjones-seriously-not-worth-it-now
  - 2026-02-23-elvis-openclaw-codex-agent-swarm
  - 2026-09-04-julian-ivanov-ki-automat-so-nutzt-du-claude-code-nach-anthropics-neuen-re
  - 2026-07-30-floknowsai-ki-gibt-dir-das-gefuehl-dass-du-so-schnell-wie-noch-nie-arbeitest
  - 2026-09-22-artificialanlys-2102462962758033624
---

## Kurz gesagt

- Von fünf Aussagen stimmt eine, aber anders, als die Schlagzeile klingt: Bei GPT-6 sinken die Halluzinationen vor allem, weil das Modell öfter nicht antwortet.{q:5}
- Bei vier Aussagen lässt sich die Zahl nicht prüfen. Das macht sie nicht falsch, aber du solltest sie nicht als Fakt weitergeben.
- Frag bei jeder Zahl aus der Szene: Wer hat gemessen, was genau, und was fehlt daneben?

| Aussage | Wer sagt es | Urteil |
|---|---|---|
| Fine-Tuning ist tot{q:1} | Nate B. Jones | nicht prüfbar |
| 94 Commits an einem Tag{q:2} | Elvis | nicht prüfbar |
| 93 % zu 76 % Recall, siebenfacher Tokenverbrauch{q:3} | Julian Ivanov, zitiert Anthropic | nicht prüfbar, als Richtung plausibel |
| Gefühlt schneller, gemessen langsamer{q:4} | @floknowsai, zitiert zwei Studien | nicht prüfbar, plausibel |
| Weniger Halluzinationen bei GPT-6{q:5} | Artificial Analysis | stimmt, aber anders gemeint |

## 1. „Wer 2026 feintunt, verliert gegen ein gutes Harness“

Nate B. Jones sagt in einem knapp zweiminütigen TikTok-Clip vom Dezember 2025:{q:1} Ein Fine-Tuning-Projekt dauere acht bis zwölf Wochen, danach sei das Modell von einer neuen Generation überholt. Unternehmen hätten im letzten Jahr zweistellige bis dreistellige Millionenbeträge verbrannt.

Der Clip zeigt weder Messwerte noch eine Fallstudie. Die Logik, dass Modellwechsel schneller kommen als Trainingszyklen, leuchtet ein. Woher die Millionenzahl stammt, sagt er nicht. Gegenfälle wie kleine Modelle für Latenz- oder Kostenziele, Datenschutzvorgaben und enge Aufgaben mit hohem Volumen kommen nicht vor.

**Nicht prüfbar.** Als Reihenfolge taugt die Aussage: erst Instruktionen, Constraints und Evals ausreizen. Als Absolutheit nicht.

## 2. „50 Commits pro Tag, Spitze 94“

Elvis (@elvissun) beschreibt in einem X-Thread einen Orchestrator, der parallele Coding-Agents steuert. Im Schnitt seien es 50 Commits pro Tag, an der Spitze 94. Rund 90 % der Aufgaben übernehme Codex.{q:2} Die Architektur (getrennte Kontexte für Business und Code, Worktree-Isolation, mehrere Gates vor dem Menschen) passt zu bekannten Mustern. Die Zahlen sind Eigenangaben.

Das Bild aus dem Thread ist ein Contribution-Graph und zeigt an einem Tag im Februar 62 Beiträge. Ob es der Tag mit den 94 Commits ist, geht daraus nicht hervor.{q:2} Kosten nennt Elvis nicht: keinen Token-Verbrauch für drei Reviewer pro PR, keine Hardware für 20 und mehr parallele Agents. Commit-Zahlen sagen zudem nichts über Qualität oder Wert.

**Nicht prüfbar.** Das Bild bestätigt die 94 jedenfalls nicht.

## 3. „93 % bei 256.000 Token, 76 % bei einer Million“

Julian Ivanov beruft sich in einem Video auf Anthropic-Doku und -Blog:{q:3} Beim MRCR-Benchmark finde das Modell bei rund 256.000 Token 93 % der versteckten Informationen, bei einer Million nur 76 %. Ein Anthropic-Beispiel zeige etwa die siebenfache Tokenmenge von niedriger zu hoher Effort-Stufe.

Ivanov nennt die Zahlen ohne Methode, und das Original ist nicht geprüft. Unklar bleiben das Testsetup, das Modell und beim Faktor sieben die Aufgabe und die Vergleichsstufen. Der Faktor ist ein einzelnes Beispiel, kein Durchschnitt.

**Nicht prüfbar, als Richtung plausibel.** Die Konsequenz (Kontext klein halten, Effort nach Aufgabe wählen) hängt nicht an der exakten Zahl. Zitiere die Zahlen nicht als Fakt, bevor du die Anthropic-Seite selbst gelesen hast.

## 4. „Gefühlt 20 % schneller, gemessen 19 % langsamer“

@floknowsai fasst in einem 96-Sekunden-TikTok zwei arXiv-Studien zusammen.{q:4} In der ersten arbeiteten 16 erfahrene Entwickler im eigenen Projekt, zwölf wurden langsamer. Vorher erwarteten sie 24 % Beschleunigung, hinterher fühlten sie 20 %, gemessen waren es 19 % mehr Zeit.

Die Zahlen stammen aus Caption und Transkript des Videos, die Studien selbst sind nicht geprüft. Die Stichprobe ist klein und betrifft erfahrene Entwickler in vertrauten Projekten mit einem früheren Modellstand. Für Neulinge oder neuere Tools sagt sie wenig. Die Erklärung, fünf Jahre Projektwissen kämen beim Agent nicht an, ist Florians eigene Deutung, keine Aussage der Zahlen.

**Nicht prüfbar, plausibel.** Die Wahrnehmungslücke ist der belastbare Kern, sofern die Studie so ist, wie das Video sie wiedergibt. Verlass dich bei deiner eigenen Produktivität nicht aufs Gefühl, sondern miss.

## 5. „GPT-6 halluziniert deutlich weniger“

Im Benchmark AA-Omniscience fällt die Halluzinationsrate bei Sol von 92 % auf 60 %, bei Luna von 93 % auf 77 %. Gemessen hat Artificial Analysis, Stand 22.09.2026 im Intelligence Index v4.3.{q:5}

Die Zahl bedeutet nicht, was sie klingt. Sol beantwortet nur noch 83 % der Fragen statt 99 %, die Accuracy sinkt von 59 % auf 54 %. Artificial Analysis liest das selbst überwiegend als Verweigerung, nicht als mehr Wissen. Der zusammengefasste Omniscience Index steigt trotzdem (Sol 27 statt 22, Luna 1 statt minus 10). Wie er gewichtet, steht nicht in der Quelle.{q:5}

**Stimmt, aber anders gemeint.** Weniger Halluzinationen heißt hier weniger geantwortet, nicht mehr gewusst. Ob dir das nützt, hängt davon ab, ob in deinem Einsatz eine falsche Antwort teurer ist als keine.

## Drei Fragen für jede Zahl

1. **Wer hat gemessen, und woher kennst du die Zahl?** Hersteller, Drittanbieter oder der Urheber selbst? Liest du das Original oder ein Video, das es zusammenfasst? Jede Zwischenstufe fügt Fehler hinzu.
2. **Was genau wurde gemessen?** Welcher Index, welches Harness, welche Stichprobe, welcher Modellstand? Dieselbe Kennzahl weicht je nach Setup ab, und ein Rückgang kann aus etwas anderem stammen, als die Überschrift vermuten lässt.
3. **Was fehlt neben der Zahl?** Kosten, Gegenfälle, Qualität statt Menge. Eine Zahl ohne den Preis, den sie verursacht, ist nur die halbe Aussage.

## Empfehlung

Behandle Zahlen aus der Szene als Hypothese, bis du das Original gelesen oder selbst gemessen hast. Für Entscheidungen über Modell, Effort oder Setup: Miss auf deinen eigenen Aufgaben, mit Kosten pro Aufgabe statt Preis pro Token.
