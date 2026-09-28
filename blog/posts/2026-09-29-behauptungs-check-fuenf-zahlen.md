---
titel: "Fünf Behauptungen aus der KI-Szene im Check: Was die Quellen wirklich tragen"
datum: 2026-09-29
kategorie: check
zusammenfassung: "Fine-Tuning sei tot, 94 Commits an einem Tag, 93 % zu 76 % Kontext-Recall, gefühlt schneller und gemessen langsamer, weniger Halluzinationen bei GPT-6: fünf Zahlen, geprüft gegen das, was die Quellen hergeben."
status: entwurf
quellen:
  - 2025-12-31-natebjones-seriously-not-worth-it-now
  - 2026-02-23-elvis-openclaw-codex-agent-swarm
  - 2026-09-04-julian-ivanov-ki-automat-so-nutzt-du-claude-code-nach-anthropics-neuen-re
  - 2026-07-30-floknowsai-ki-gibt-dir-das-gefuehl-dass-du-so-schnell-wie-noch-nie-arbeitest
  - 2026-09-22-artificialanlys-2102462962758033624
---

## Kurz gesagt

- Von fünf geprüften Behauptungen ist nur eine durch das mitgelieferte Material direkt gestützt, und die ist ein Messwert eines Drittanbieters, der anders gelesen werden muss, als die Überschrift nahelegt.
- Eine Behauptung wird vom mitgelieferten Bild nicht bestätigt: Der Contribution-Graph zeigt an einem Tag im Februar 62 Beiträge. Ob es der Tag mit den 94 Commits ist, bleibt offen.
- Drei Zahlen sind Herstellerangaben, Selbstberichte oder Zweitzitate ohne Primärquelle. Das macht sie nicht falsch, aber nicht belegt.

Grundlage sind Source-Notizen aus der Wissensbasis. Wo eine Primärquelle nicht gelesen wurde, steht das dabei. Alles Weitere zur Sache selbst wäre Modellwissen und bleibt draußen.

## 1. „Fine-Tuning ist tot“

**Behauptet** von Nate B. Jones in einem knapp zweiminütigen TikTok-Clip (Dezember 2025): Wer 2026 feintunt, verliert gegen ein gutes Agentic Harness. Ein Projekt dauere acht bis zwölf Wochen, danach sei das Modell von einer neuen Generation überholt. Unternehmen hätten im letzten Jahr zweistellige bis dreistellige Millionenbeträge verbrannt.

**Belegt:** nichts. Die Quelle ist reine Meinung ohne Messwerte, Fallstudie oder Methode. Die Zeitfalle-Logik (Modellwechsel schneller als Trainingszyklus) ist plausibel, aber nicht gemessen.

**Es fehlt:** die Millionenzahl hat keine Herleitung. Gegenfälle, die in der Einordnung der Notiz stehen (kleine Modelle für Latenz- oder Kostenziele, Datenschutzvorgaben, enge Aufgaben mit hohem Volumen), kommen im Clip nicht vor.

**Urteil: unbelegt.** Als Entscheidungsreihenfolge (erst Instruktionen, Constraints und Evals ausreizen) taugt die Aussage, als Absolutheit nicht.

## 2. „94 Commits an einem Tag mit einem Agent-Schwarm“

**Behauptet** von Elvis (@elvissun) in einem X-Thread: Ein Orchestrator steuert parallele Coding-Agents, im Schnitt 50 Commits pro Tag, Spitze 94. Rund 90 % der Aufgaben übernehme Codex.

**Belegt:** das Architekturprinzip (getrennte Kontexte für Business und Code, Worktree-Isolation, mehrere Gates vor dem Menschen), weil es zu bekannten Mustern passt. Die Zahlen selbst sind selbstberichtet, und unsere Quelle ist eine deutsche Aufarbeitung des Threads, nicht das Original.

**Es fehlt:** Kosten, komplett. Token-Verbrauch dreier Reviewer pro PR, 20+ parallele Agents und Hardware werden nicht beziffert. Commit-Zahlen sagen zudem nichts über Qualität oder Wert. Das mitgelieferte Bild ist ein Contribution-Graph und zeigt an einem Tag im Februar 62 Beiträge. Ob das der Tag mit den 94 Commits ist, geht aus der Quelle nicht hervor.

**Urteil: unbelegt.** Das mitgelieferte Bild bestätigt die 94 nicht (62 Beiträge an einem Tag im Februar; ob derselbe Tag gemeint ist, bleibt offen).

## 3. „93 % Recall bei 256.000 Token, 76 % bei einer Million; siebenfacher Tokenverbrauch bei hoher Effort-Stufe“

**Behauptet** in einem Video von Julian Ivanov, der sich auf Anthropic-Doku und -Blog beruft: Beim MRCR-Benchmark findet das Modell bei rund 256.000 Token 93 % der versteckten Informationen, bei einer Million nur 76 %. Ein Anthropic-Beispiel zeige etwa die siebenfache Tokenmenge von niedriger zu hoher Effort-Stufe.

**Belegt:** dass Ivanov die Zahlen so nennt. Die Notiz vermerkt „Original nicht geprüft“, das Video zitiert ohne Methode. Es sind Herstellerangaben aus zweiter Hand. Beim Tokenfaktor fehlen Aufgabe, Modell und Vergleichsstufen.

**Es fehlt:** die Primärquelle, das Testsetup des Benchmarks und die Frage, für welches Modell die Werte gelten. Der Faktor sieben ist ein einzelnes Beispiel, kein Durchschnitt.

**Urteil: unbelegt, aber als Richtung plausibel.** Die Konsequenz (Kontext klein halten, Effort nach Aufgabe wählen) hängt nicht an der exakten Zahl. Zitiere sie nicht als Fakt, bevor du die Anthropic-Seite selbst gelesen hast.

## 4. „Gefühlt 20 % schneller, gemessen 19 % langsamer“

**Behauptet** in einem 96-Sekunden-TikTok von @floknowsai, der zwei arXiv-Studien zusammenfasst: In der ersten arbeiteten 16 erfahrene Entwickler im eigenen Projekt. Zwölf wurden langsamer. Erwartet hatten sie vorher 24 % Beschleunigung, gefühlt waren es hinterher 20 %, gemessen 19 % mehr Zeit.

**Belegt:** in der Notiz nur als Wiedergabe. Die Zahlen stammen aus Caption und Transkript, die Studien wurden nicht geprüft. Das Transkript ist eine maschinelle Rückübersetzung, die Studien-Kennung steht nur als Link. Die Deutung, fünf Jahre Projektwissen kämen beim Agent nicht an, ist Florians eigene Erklärung, keine Aussage der Zahlen.

**Es fehlt:** die Primärquelle. Die Stichprobe ist klein, bezieht sich auf erfahrene Entwickler in vertrauten Projekten und auf einen früheren Modellstand. Für Neulinge oder neuere Tools sagt sie wenig.

**Urteil: plausibel.** Die Wahrnehmungslücke ist der belastbare Kern, sofern die Studie so berichtet, wie das Video sie wiedergibt. Was du daraus mitnimmst: Verlass dich bei deiner eigenen Produktivität nicht aufs Gefühl, sondern miss.

## 5. „Weniger Halluzinationen bei GPT-6 Sol und Luna“

**Behauptet** wird der Rückgang der Halluzinationsrate im Benchmark AA-Omniscience: Sol von 92 % auf 60 %, Luna von 93 % auf 77 %.

**Belegt:** als Messung von Artificial Analysis (Drittanbieter, Intelligence Index v4.3, Stand 2026-09-22) durch die Notiz selbst. Aber die Zahl bedeutet nicht, was sie klingt. Sol beantwortet nur noch 83 % der Fragen statt 99 %, die Accuracy sinkt von 59 % auf 54 %. Die Notiz ordnet ausdrücklich ein: überwiegend Verweigerung, nicht mehr Wissen. Der zusammengefasste Omniscience Index steigt dennoch (Sol 27 statt 22, Luna 1 statt minus 10); wie er gewichtet, steht nicht in der Notiz.

**Es fehlt:** die Antwort auf die Frage, ob dir die Verweigerung nützt. Das hängt davon ab, ob in deinem Einsatz eine falsche Antwort teurer ist als keine.

**Urteil: belegt als Messwert, irreführend als Schlagzeile.** Weniger Halluzinationen heißt hier weniger geantwortet, nicht mehr gewusst.

## Übersicht

| Behauptung | Wer sagt es | Art der Quelle | Urteil |
|---|---|---|---|
| Fine-Tuning ist tot | Nate B. Jones | Meinung ohne Daten | unbelegt |
| 94 Commits am Tag | Elvis, via Zweitquelle | Selbstbericht, Bild bestätigt es nicht | unbelegt |
| 93 % / 76 % MRCR, 7x Token | Ivanov, zitiert Anthropic | Hersteller aus zweiter Hand | unbelegt, plausibel |
| Gefühlt schneller, gemessen langsamer | @floknowsai, zitiert arXiv | Studie aus zweiter Hand | plausibel |
| Weniger Halluzinationen | Artificial Analysis | Drittmessung | belegt, aber Verweigerung |

## Drei Prüffragen für jede Zahl

1. **Wer hat gemessen, und woher kennst du die Zahl?** Hersteller, Drittanbieter oder Selbstbericht? Und liest du die Primärquelle oder ein Video, das sie zusammenfasst? Jede Zwischenstufe fügt Fehler hinzu, wie die Transkriptions- und Übersetzungsfehler in den Notizen zeigen.
2. **Was genau wurde gemessen, und unter welchen Bedingungen?** Welcher Index, welches Harness, welche Stichprobe, welcher Modellstand? Die gleiche Kennzahl kann je nach Setup abweichen, und ein Rückgang kann aus etwas anderem stammen, als die Überschrift vermuten lässt.
3. **Was fehlt neben der Zahl?** Kosten, Gegenfälle, Qualität statt Menge. Wenn eine Zahl ohne den Preis daherkommt, den sie verursacht, ist sie nur die halbe Aussage.

## Empfehlung

Behandle Zahlen aus der Szene als Hypothese, bis du die Primärquelle gelesen oder selbst gemessen hast. Für Entscheidungen über Modell, Effort oder Setup: miss auf deinen eigenen Aufgaben, mit Kosten pro Aufgabe statt Preis pro Token.
