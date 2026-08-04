# Modell-Eskalation-von-guenstig-nach-teuer

**Konfidenz:** mehrfach-belegt

## Zweck

Verhindert, dass für jede Aufgabe reflexhaft das stärkste verfügbare Modell mit maximaler Reasoning-Stufe gewählt wird. Adressiert, dass die Kosten pro Aufgabe annähernd exponentiell mit der Reasoning-Stufe steigen, der Fähigkeitszugewinn aber deutlich langsamer — die teuerste Konfiguration ist damit für die Mehrheit der Aufgaben eine Fehlallokation, nicht die sichere Wahl.

## Funktionsweise

Die Aufgabe startet beim günstigsten Modell, das sie plausibel lösen kann, und wird erst hochgeschaltet, wenn der Fortschritt ausbleibt. Die Abbruchkriterien werden vorab benannt statt nach Gefühl entschieden: der Agent bleibt hängen, Fixes greifen nicht mehr, oder das Modell verliert den Faden über den Aufgabenkontext.

**Vorgeschaltet — der Input.** Bevor eine der beiden Achsen bewegt wird, gehört geprüft, ob überhaupt ein Compute-Problem vorliegt. Unklarer Auftrag, fehlende Dateien, fehlende Tools oder eine widersprüchliche `CLAUDE.md` lassen sich weder mit einem stärkeren Modell noch mit mehr Aufwand reparieren — mehr Rechenleistung arbeitet dann nur länger auf unvollständiger Grundlage. Diese Stufe ergänzt Anthropic (2026-07-08) und sie fehlt in der ursprünglichen Cerebras-Fassung des Patterns.

Es gibt zwei unabhängige Eskalationsachsen, die getrennt gedacht werden müssen. Die erste ist das **Modell** (Beispiel GPT-5.6: Luna → Terra → Sol), die zweite die **Reasoning-Stufe** innerhalb eines Modells (in Codex: Light → Medium → High → Extra High → Ultra). Eine schwierige Aufgabe kann auf einem mittleren Modell mit hoher Reasoning-Stufe günstiger laufen als auf dem Spitzenmodell mit niedriger — beide Achsen zu prüfen ist Teil des Patterns.

Die Zahlengrundlage für die zweite Achse (Artificial Analysis, GPT-5.6 Sol, Messung 17.07.2026): 0,20 $ pro Task bei `low`, 0,31 $ bei `medium`, 0,45 $ bei `high`, 0,68 $ bei `xhigh`, 1,04 $ bei `max`. Das sind Aufschläge von 45 bis 55 % pro Stufe, insgesamt Faktor 5,2 — für einen Zugewinn von etwa 49,5 auf 58,7 Index-Punkte. Nur die Stufen bis `high` liegen im günstigen Kosten-Nutzen-Bereich.

**Diagnose statt pauschaler Richtung.** Welche Achse zu bewegen ist, verrät das Fehlerbild. Hat der Agent Arbeit übersprungen — eine Datei nicht gelesen, Tests nicht ausgeführt, seine Änderung nicht kontrolliert, eine mehrstufige Aufgabe nur halb erledigt oder vorschnell nachgefragt —, fehlt Arbeitstiefe, also die Aufwandsstufe erhöhen. Hat er alles Relevante gelesen, die Tools eingesetzt, das Problem nachvollziehbar untersucht und liegt trotzdem selbstbewusst falsch, fehlt Fähigkeit, also das Modell wechseln. Trifft keines von beidem zu, liegt das Problem beim Input.

Ergänzend gilt die Rollenteilung im Multi-Agent-Fall: das starke Modell entscheidet die Richtung, das günstigere führt als Subagent aus.

## Vorteile

- Macht die Modell- und Reasoning-Wahl zu einer bewussten Entscheidung pro Aufgabe statt zu einer globalen Voreinstellung.
- Der Großteil alltäglicher Aufgaben wird auf der günstigen Stufe erledigt; die teure Konfiguration bleibt für die Fälle übrig, die sie brauchen.
- Eskalation nach klaren Abbruchkriterien liefert nebenbei ein Signal über die tatsächliche Aufgabenschwere — wiederholte Eskalation an derselben Stelle deutet auf ein Struktur- oder Kontextproblem, nicht auf ein Modellproblem.
- Die beiden getrennten Achsen erlauben günstigere Kombinationen als die naive Wahl „stärkstes Modell, höchste Stufe“.

## Nachteile & Grenzen

- Ein Fehlversuch auf der günstigen Stufe ist nicht kostenlos: die verbrauchten Tokens sind weg, und bei Aufgaben, die erkennbar über dem günstigen Modell liegen, ist der Umweg teurer als der Direktstart.
- Erfordert Beobachtung während des Laufs. Wer die Abbruchkriterien nicht aktiv prüft, lässt ein zu schwaches Modell lange erfolglos arbeiten — das ist der teuerste Fall.
- Alle konkreten Zahlen sind zeitgebunden und modellspezifisch. Übertragbar ist die Methode, nicht die Preisstaffel.
- Der Modellwechsel mitten in einer Aufgabe kostet den Prompt-Cache: das neue Modell liest den Kontext zum vollen Preis erneut ein. Das relativiert den Vorteil bei kontextlastigen Aufgaben und steht in Spannung zu [[Kontext-Hygiene-Entscheidungsbaum]].

## Wann einsetzen, wann nicht

- Einsetzen: bei hohem Aufgabenvolumen mit gemischter Schwere, bei Budgetdeckeln pro Nutzer oder Team, und bei Subagent-Architekturen, in denen ohnehin mehrere Modelle koordiniert werden.
- Nicht einsetzen: bei einmaligen, erkennbar schwierigen Aufgaben mit hohem Kontextaufwand — dort frisst der Cache-Verlust beim Wechsel den Ersparnis-Vorteil. Ebenfalls nicht bei Aufgaben, deren Fehlversuch teurer ist als die Modelldifferenz (Produktionsänderungen, irreversible Schritte).

## Belege

- 2026-07-27 · [[2026-07-27-cerebras-gpt-5-6-modellwahl-und-reasoning]] · meinung — Cerebras-Artikel beschreibt die Eskalation „Start with Luna, then escalate“ mit benannten Abbruchkriterien; die mitgelieferten Artificial-Analysis-Charts (Messung 17.07.2026) liefern die Kostenprogression pro Reasoning-Stufe und die zugehörigen Index-Werte, die Preistabelle der OpenAI-Preisseite die Modellverhältnisse 1 : ½ : ⅕.
- 2026-07-08 · [[2026-07-08-claudedevs-modell-vs-effort]] · meinung — Unabhängige Bestätigung der Zwei-Achsen-Struktur durch Anthropic für Claude Code, anderer Anbieter und andere Produktfamilie: das Modell wählt die Qualitätskurve, die Aufwandsstufe die Position darauf. Ergänzt den vorgeschalteten Input-Check und die Diagnose nach Fehlerbild statt pauschaler Eskalationsrichtung; präzisiert, dass die Aufwandsstufe eine Ausgabebereitschaft ist und kein Tokenbudget.
- 2026-01-10 · [[2026-01-10-eyad-khrais-claude-code-tutorial]] · meinung — Erfahrungsbericht empfiehlt eine feste Rollenteilung statt dynamischer Eskalation: Opus für Planung/Architektur, Sonnet für die anschließende, günstigere Ausführung nach Plan.
- 2026-02-14 · [[2026-02-14-minty-mastering-claude-code]] · meinung — Orchestrator-Modell: das teure Modell (Claude) plant und reviewt, günstigere spezialisierte Worker (Codex, Gemini, DeepSeek) übernehmen die Bulk-Implementierung nach jeweiliger Stärke — die konkrete Modell-Rollenzuordnung ist unbelegte persönliche Konfiguration, übertragbar ist nur das Prinzip „teuer plant, günstig implementiert“.

## Spannungen & offene Fragen

- **Startpunkt umstritten.** Cerebras (2026-07-27) empfiehlt, grundsätzlich beim günstigsten Modell zu beginnen und bei Stillstand zu eskalieren. Anthropic (2026-07-08) empfiehlt, beim Default zu starten und dann anhand des Fehlerbildes zu diagnostizieren, statt pauschal eine Richtung zu fahren. Beide teilen die Zwei-Achsen-Analyse, unterscheiden sich aber in der Strategie. Nicht aufgelöst: Cerebras optimiert erkennbar auf Kosten pro Aufgabe bei hohem Volumen, Anthropic auf Ergebnisqualität bei Einzelaufgaben — welche Empfehlung trägt, hängt davon ab, ob Durchsatz oder Trefferquote das knappe Gut ist.
- Die erste Quelle stammt von einem Inferenz-Hardware-Anbieter, der im selben Artikel eigene Produkte empfiehlt; die zweite vom Modellhersteller selbst. Beide haben ein Interesse, argumentieren aber jeweils gegen den eigenen naheliegenden Anreiz (Cerebras nennt günstige Fremdmodelle, Anthropic rät vom Griff zum größten Modell ab). Die Zahlen der ersten Quelle sind unabhängig belegt (OpenAI-Preisseite, Artificial Analysis) und nachgerechnet; die Kurven der zweiten sind ausdrücklich illustrativ und keine Messung.
- Spannung zu [[Kontext-Hygiene-Entscheidungsbaum]]: Eskalation verlangt Modellwechsel, Cache-Ökonomie belohnt das Verharren in einer warmen Session mit einem Modell. Ab welchem Kontextumfang der Cache-Verlust die Modellersparnis übersteigt, ist offen und müsste am eigenen Workload gemessen werden.
- Offene Frage: Lässt sich die Eskalation im eigenen Setup automatisieren (Abbruchkriterium als Hook oder Eval), oder bleibt sie eine manuelle Beobachtungsentscheidung?

## Verwandte Patterns

- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Action-Space-Design-nach-Modellfaehigkeit]]
- [[Lokale-Modell-Umleitung-Muster]]
- [[Advisor-Agent-gegen-Drift]]
