---
url: https://x.com/ClaudeDevs/status/2074900291062034618
titel: "Modell und Effort in Claude Code: Wissen oder gründlicher arbeiten?"
autor: "Claude Developers (@ClaudeDevs)"
datum: 2026-07-08
erfasst: 2026-08-04
typ: tweet
quelle: vibedeck
sekundaerquelle: true
status: verarbeitet
verarbeitet_am: 2026-08-04
source_notiz: 80_Knowledge/Sources/2026-07-08-claudedevs-modell-vs-effort.md
medien: "10 lokal"
beschreibung: "Anthropic erklärt, warum Modellwahl und Effort Level unterschiedliche Probleme lösen. Der Guide zeigt, wann Du ein stärkeres Modell brauchst, wann mehr Effort hilft und warum zuerst der Kontext stimmen muss."
vibedeck_category: tooling
vibedeck_level: intermediate
vibedeck_tags:
  - "tooling/claude-code"
  - "tooling/ai-models"
  - "configuration/effort-level"
  - "workflows/context-engineering"
  - "optimization/token-costs"
vibedeck_topics:
  - "[[Claude Code]]"
  - "[[Effort Level]]"
  - "[[AI Models]]"
  - "[[Context Engineering]]"
---

# Modell und Effort in Claude Code: Wissen oder gründlicher arbeiten?

> Sekundärquelle: aus vibedeck übernommene deutsche Aufarbeitung (`src/content/knowledge/claude-code-model-und-effort.md`). Primärquelle: https://x.com/ClaudeDevs/status/2074900291062034618

Wenn Claude Code eine Aufgabe nicht sauber löst, liegt der Reflex nahe: ein größeres Modell auswählen und es noch einmal versuchen. Der von Claude Developers geteilte Artikel zeigt, warum das oft die falsche Stellschraube ist. **Modellwahl** und **Effort Level** verbessern Ergebnisse auf unterschiedliche Weise: Das Modell bestimmt den verfügbaren Fähigkeitsraum, Effort bestimmt, wie gründlich Claude diesen Raum für eine konkrete Aufgabe nutzt.

Die praktische Leitfrage lautet deshalb nicht einfach „Wie bekomme ich eine bessere Antwort?“, sondern:

> **Wusste Claude nicht genug – oder hat Claude nicht gründlich genug gearbeitet?**

Bevor Du eine der beiden Einstellungen änderst, solltest Du allerdings noch einen Schritt zurückgehen. Ein unklarer Prompt, fehlende Tools, ungeeignete Skills oder unvollständiger Projektkontext lassen sich weder mit einem teureren Modell noch mit mehr Effort zuverlässig reparieren.

## Was Claude Code an das Modell sendet

Claude Code verarbeitet nicht nur Deine letzte Nachricht. Vor einem API-Aufruf stellt es ein Paket aus System Prompt, Tool-Definitionen, `CLAUDE.md`, Gesprächsverlauf und den aktuell verfügbaren Dateien zusammen. Der konkrete Kontext steuert die Antwort stark, verändert aber nicht das zugrunde liegende Modell.

![Claude Code bündelt Prompt, Tools, CLAUDE.md, Verlauf und Dateien in einer API-Anfrage](medien/2026-07-08-claudedevs-claude-code-model-und-effort/context-api-request.png)

Auf dem Server wird dieser Text tokenisiert. Ein Tokenizer zerlegt den Inhalt in Einheiten und ordnet ihnen numerische IDs aus einem festen Vokabular zu.

![Der Tokenizer zerlegt Text in Einheiten und ordnet ihnen Token-IDs zu](medien/2026-07-08-claudedevs-claude-code-model-und-effort/tokenization.png)

Das Modell erhält diese Tokenfolge und berechnet Wahrscheinlichkeiten für das nächste Token. Nach jedem erzeugten Token beginnt dieser Vorgang erneut. Eine Antwort mit 200 Tokens entsteht also nicht in einem einzigen Schritt, sondern aus einer Folge von Vorhersagen.

![Das Modell bewertet mögliche nächste Tokens mit unterschiedlichen Wahrscheinlichkeiten](medien/2026-07-08-claudedevs-claude-code-model-und-effort/next-token-probabilities.png)

## Modellwahl: Welche Fähigkeiten stehen zur Verfügung?

Die Gewichte eines Modells enthalten die während des Trainings erworbenen Muster, Kenntnisse und Fähigkeiten. Sie sind zur Inference-Zeit fest. Dein Prompt, eine ausführliche `CLAUDE.md` oder beigefügte Dokumentation können die nächste Vorhersage lenken, aber die Modellgewichte nicht dauerhaft erweitern.

![Der Prompt läuft durch feste Modellgewichte und erzeugt eine Wahrscheinlichkeitsverteilung](medien/2026-07-08-claudedevs-claude-code-model-und-effort/fixed-model-weights.png)

Ein Modellwechsel ersetzt diesen Satz fester Gewichte. Ein größeres Modell ist damit nicht bloß dieselbe Engine mit mehr Bedenkzeit, sondern bringt einen anderen Fähigkeitsraum mit. Das hilft besonders bei:

- subtilen Bugs und ungewöhnlichen Fehlerbildern,
- unbekannten oder spezialisierten Fachgebieten,
- mehrdeutigen Anforderungen,
- Architekturentscheidungen und
- Aufgaben, bei denen ein kleineres Modell trotz vollständigem Kontext und ernsthaftem Versuch selbstbewusst falsch bleibt.

Für präzise beschriebene Routineänderungen ist dieser zusätzliche Fähigkeitsraum häufig unnötig. Ein kleineres Modell kann solche Aufgaben schneller und günstiger erledigen, wenn der relevante Code bereits im Kontext liegt.

![Mit jedem erzeugten Token wächst die Sequenz und wird für die nächste Vorhersage erneut verarbeitet](medien/2026-07-08-claudedevs-claude-code-model-und-effort/token-generation-loop.png)

Die Modellwahl beeinflusst außerdem den Preis pro Output-Token. Sie legt jedoch nicht fest, wie viele Tokens Claude für die Aufgabe tatsächlich erzeugt. Genau hier kommt Effort ins Spiel.

## Effort: Wie gründlich arbeitet Claude?

Effort ist mehr als „länger nachdenken“. Während einer Claude-Code-Aufgabe entstehen verschiedene Arten von Output-Tokens:

- **Thinking** für die interne Bearbeitung und Planung,
- **Tool Calls** zum Lesen, Suchen, Bearbeiten oder Testen und
- **Text** für Rückfragen, Fortschrittsmeldungen und das Endergebnis.

![Thinking, Tool Calls und Text sind unterschiedliche Arten desselben Token-basierten Outputs](medien/2026-07-08-claudedevs-claude-code-model-und-effort/output-token-types.png)

Ein höherer Effort Level macht Claude eher bereit, mehr Arbeitsschritte auszuführen, bevor es die Aufgabe als erledigt betrachtet. Das kann bedeuten, dass es zusätzliche Dateien liest, mehrere Hypothesen prüft, Tests ausführt, Änderungen erneut kontrolliert oder eine längere Aufgabe weiterführt, statt früh nachzufragen.

![Illustrativer Vergleich: High Effort liest mehr Kontext, testet und verifiziert vor dem Abschluss](medien/2026-07-08-claudedevs-claude-code-model-und-effort/effort-confidence-paths.png)

Die im Bild genannten Tokenzahlen sind ausdrücklich illustrativ. Effort ist kein festes Tokenbudget und zwingt Claude nicht dazu, bei einer einfachen Aufgabe künstlich Arbeit zu erzeugen. Findet der erste Schritt eines Plans bereits eindeutig den Fehler, darf Claude nicht mehr notwendige Hypothesen verwerfen. Höherer Effort erhöht vor allem die Bereitschaft, bis zu einer belastbareren Lösung weiterzuarbeiten.

## Erst den Input prüfen

Anthropics wichtigste Einschränkung kommt vor der Modell-Effort-Entscheidung: Wenn eine Aufgabe eigentlich einfach sein sollte, ist mehr Rechenaufwand häufig nur eine teure Behandlung des falschen Problems.

Prüfe zuerst:

1. Ist die Aufgabe konkret und sinnvoll abgegrenzt?
2. Hat Claude alle relevanten Dateien und aktuellen Dokumentationen?
3. Sind die nötigen Tools verfügbar?
4. Sind passende Skills oder Projektregeln eingebunden?
5. Enthält die `CLAUDE.md` hilfreiche Vorgaben – oder erzeugt sie Widersprüche?

Fehlt hier etwas, verbessere zunächst den Input. Context Engineering entscheidet darüber, welche Informationen und Handlungsmöglichkeiten Claude überhaupt nutzen kann. Ein stärkeres Modell kann fehlenden Projektkontext nicht erraten; mehr Effort kann lediglich länger auf einer unvollständigen Grundlage arbeiten.

## Die Diagnose: Modell oder Effort erhöhen?

Wenn der Kontext stimmt und das Ergebnis trotzdem falsch ist, hilft eine einfache Fehleranalyse.

### Effort erhöhen, wenn Claude zu früh aufgehört hat

Ein höherer Effort Level passt, wenn Claude:

- eine relevante Datei übersprungen hat,
- Tests nicht ausgeführt hat,
- seine Änderung nicht kontrolliert hat,
- eine mehrstufige Aufgabe nur teilweise erledigt hat oder
- vorschnell um weitere Informationen bittet, die es selbst ermitteln könnte.

Diese Symptome zeigen kein fehlendes Wissen, sondern unzureichende Arbeitstiefe. Mehr Effort verwendet dieselben Modellgewichte, gibt Claude aber eine stärkere Disposition zu weiteren Schritten und zusätzlicher Verifikation.

### Modell wechseln, wenn die Fähigkeit nicht reicht

Ein größeres Modell passt, wenn Claude:

- alle relevanten Informationen gelesen hat,
- die nötigen Tools und Tests tatsächlich eingesetzt hat,
- das Problem ernsthaft und nachvollziehbar untersucht hat und
- trotzdem zu einer fachlich falschen oder zu oberflächlichen Schlussfolgerung kommt.

Dann fehlt nicht Einsatz, sondern Fähigkeit oder passendes Vorwissen. Ein Modellwechsel stellt andere Gewichte und damit einen anderen Fähigkeitsraum bereit.

![Entscheidungsbaum: übersprungene Arbeit spricht für mehr Effort, ein gründlich erarbeitetes falsches Ergebnis für ein stärkeres Modell](medien/2026-07-08-claudedevs-claude-code-model-und-effort/model-or-effort-decision.png)

Die Grafik ist eine Heuristik, keine starre Regel. Treffen beide Muster nicht zu, solltest Du zum Input zurückkehren und Kontext, `CLAUDE.md` oder Task Scope verbessern.

## Modell, Effort und Kosten zusammendenken

Bei Routineaufgaben erreichen kleinere und größere Modelle oft beide das gewünschte Ergebnis. Das größere Modell kann dabei zusätzliche Verifikationsschritte mit einem höheren Preis pro Token ausführen. Für mechanische Änderungen lohnt es sich daher, nicht mehr Fähigkeit einzukaufen, als die Aufgabe verlangt.

![Illustrative Kostenkurven für eine Routineaufgabe, die beide Modellgrößen schnell lösen können](medien/2026-07-08-claudedevs-claude-code-model-und-effort/routine-task-cost-curves.png)

Bei schwierigen, mehrstufigen Aufgaben kann sich das Verhältnis umkehren. Ein kleines Modell benötigt möglicherweise zahlreiche Iterationen und nähert sich dabei seiner Fähigkeitsgrenze. Ein größeres Modell ist pro Token teurer, kann dasselbe Qualitätsniveau aber mit weniger Umwegen erreichen – oder überhaupt erst erreichbar machen.

![Illustrative Kostenkurven: Bei einer schwierigen Aufgabe kann das größere Modell dieselbe Qualität mit weniger Tokens erreichen](medien/2026-07-08-claudedevs-claude-code-model-und-effort/hard-task-cost-curves.png)

Auch diese Kurven sind keine Benchmarkdaten. Sie erklären das mentale Modell: **Das Modell wählt die Fähigkeitskurve, Effort bestimmt, wie weit Claude entlang dieser Kurve zu arbeiten bereit ist.** Mehr Effort formt den Tokenverbrauch, setzt aber kein hartes Limit. Ein festes `max_tokens` kann eine Ausgabe dagegen mitten in der Bearbeitung abschneiden.

## Ein pragmatischer Workflow

Für den Alltag ergibt sich daraus eine robuste Reihenfolge:

1. **Mit dem Default starten.** Die Standardwerte sollen für die meisten Aufgaben ein vernünftiges Verhältnis aus Qualität, Zeit und Kosten liefern.
2. **Kontext prüfen.** Wenn das Ergebnis nicht passt, zuerst Prompt, Dateien, Tools, Skills und Scope untersuchen.
3. **Das Fehlermuster benennen.** Hat Claude Arbeit übersprungen oder trotz gründlicher Arbeit falsch entschieden?
4. **Nur die passende Stellschraube ändern.** Mehr Effort für Gründlichkeit, ein größeres Modell für zusätzliche Fähigkeit.
5. **Nach Aufgabenklasse optimieren.** Routinearbeit eher klein und schnell ausführen; schwierige oder mehrdeutige Arbeit gezielt mit stärkerem Modell bearbeiten.

Anthropic empfiehlt, Effort eher als allgemeine Präferenz für die eigene Arbeitsweise zu behandeln und nicht bei jedem einzelnen Prompt nervös nachzuregeln. Der Default ist der Ausgangspunkt. Die Regler werden dann wichtig, wenn Du aus einem konkreten Fehlerbild ableiten kannst, welche Ressource tatsächlich gefehlt hat.

## Quellen

- [Claude Developers: „Model and effort in Claude Code“](https://x.com/ClaudeDevs/status/2074900291062034618) — offizieller Ausgangspost und Primärquelle dieser Source Note.
- [Lydia Hallie: „Choosing a Claude model and effort level in Claude Code“](https://claude.com/blog/claude-model-and-effort-level-in-claude-code) — ausführlicher Originalartikel, fachliche Grundlage und Quelle aller eingebundenen Grafiken. Bilder: Anthropic, unverändert übernommen; lokale Wiederverwendung laut Nutzerbestätigung vom 13. Juli 2026 erlaubt.

## Verbindungen

- [[Claude Code]]
- [[Effort Level]]
- [[AI Models]]
- [[Context Engineering]]
- [[Token Economics]]
