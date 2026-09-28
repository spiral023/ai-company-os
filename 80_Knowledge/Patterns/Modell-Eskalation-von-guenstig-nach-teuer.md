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
- 2026-01-23 · [[2026-01-23-nummanali-claude-task-system]] · meinung — Dritte unabhängige Nennung derselben festen Rollenzuteilung neben Eyad Khrais und Minty: Haiku für Befehle/einfache Suche, Sonnet für die meiste Implementierungsarbeit, Opus für Architekturentscheidungen und mehrstufiges Schließen — Modell lässt sich pro Agent-Aufruf explizit festlegen.
- 2026-01-06 · [[2026-01-06-jarrodwatts-context-engineering-guide]] · meinung — Konkretes Beispiel der bereits belegten „teuer entscheidet/günstig recherchiert“-Aufteilung: ein Sonnet-„Librarian“-Subagent recherchiert für einen Opus-Hauptagenten.
- 2026-01-21 · [[2026-01-21-aiedge-claude-50-pro-tips]] · meinung — Wegen des hohen Credit-Verbrauchs von Cowork wird im günstigeren normalen Chat mit Sonnet 4.5 geplant und erst zur Ausführung zu Cowork gewechselt — dieselbe Zwei-Stufen-Logik (günstig planen/vorbereiten, teurer ausführen), hier nach Werkzeug statt nach Modell gestaffelt.
- 2026-02-01 · [[2026-02-01-aiedge-claude-code-starter-pack]] · meinung — Spannung: Boris Cherny nutzt laut Cheatsheet Opus 4.5 mit Thinking für praktisch alles, mit der unbelegten Begründung, weniger Steering-Aufwand mache das größere Modell am Ende schneller — widerspricht der Startpunkt-Empfehlung dieses Patterns direkt, deckt sich aber mit der hier bereits dokumentierten Anthropic-Gegenposition „beim Default starten, nach Fehlerbild diagnostizieren“.
- 2026-07-28 · [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] · meinung — Bericht argumentiert, dass die Frontier für weniger Workloads nötig ist als angenommen (jagged Frontier); neutraler Scaffold zeigt etwa 5x Kosten pro Task für etwa einen Punkt mehr. Einschränkung: eine Benchmark, Berichtsquelle.
- 2026-08-03 · [[2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso]] · meinung — Sparen entsteht nur, wenn man beim nächsten Modell das kleinere wählt; Luna erreicht im Codex-Harness mehr als GPT-5.2 zu einem Bruchteil des Preises. Einschränkung: Creator-Aufbereitung, Zahlen nicht am Original geprüft.
- 2026-09-24 · [[2026-09-24-artificialanlys-2102932119995756613]] · meinung — Zeigt im Coding Agent Index, dass der Spitzenscore (Opus 5.5, 66) mit `$13.04` pro Task am teuersten ist und Codex GPT-6 Sol (57, `$2.99`) auf der Pareto-Front liegt. Einschränkung: Score gilt für Harness plus Modell, Drittanbieter-Benchmark.
- 2026-09-22 · [[2026-09-22-artificialanlys-2102462962758033624]] · meinung — Belegt, dass eine Preissenkung von rund 50 % die Kosten pro Task halbiert, obwohl der Tokenverbrauch leicht steigt (Sol 31k statt 29k). Einschränkung: Qualitätsrückgänge bei Knowledge-Work-Evals (GDPval-AA, AA-Briefcase).
- 2026-09-18 · [[2026-09-18-akshay_pachaar-2101037514945597645]] · meinung — Beschreibt ein spezialisiertes Router-Modell, das Konfidenz liefert und Eskalation an ein stärkeres Modell oder einen Menschen über Schwellen im Code steuert. Einschränkung: Herstellerzahlen, keine unabhängige Kalibrierungsmessung.
- 2026-06-04 · [[2026-06-04-agenticjames-most-people-have-not-touched-the-best-parts-of-claude-code-skills-forked]] · meinung — Zeigt Eskalation auf Skill-Ebene: Session auf günstigem Modell, ein Architektur-Review-Skill mit `context: fork` und `model: opus`, sodass das teure Modell nur dort läuft. Reine Praxisempfehlung ohne Kostenmessung.
- 2026-09-25 · [[2026-09-25-trq212-2103576349499855160]] · meinung — Liefert Herstellerzahlen zur Effort-Achse (Terminal-Bench 3.0, Fable 5.1: 140 auf 214 von 370 Versuchen bei 73k auf 222k Median-Tokens) und den Befund, dass Opus 5.5 High etwa den Score von Fable 5.1 Max bei halben Tokens erreicht. Selbstmessung eines Anthropic-Mitarbeiters, Werte aus Charts abgelesen.
- 2026-06-02 · [[2026-06-02-trq212-2061907337154367865]] · meinung — Classifier-Agent wählt Sonnet oder Opus nach erwarteter Komplexität; Token-Budget im Prompt setzbar. Nur beschrieben, keine Kostenzahlen.
- 2026-08-14 · [[2026-08-14-claude-maximizing-the-value-of-your-claude-code-session]] · meinung — Wiederkehrende laute Jobs in Subagent mit model: haiku oder sonnet; Modell- und Effort-Wechsel mitten in der Sitzung entwertet den Prompt Cache. Preisfaktoren (0.1x Lesen, bis 2x Schreiben, Output etwa 5x) Stand 2026-08-14.
- 2026-05-09 · [[2026-05-09-zodchiii-15-claude-code-settings-most-developers]] · meinung — Modell-Routing per Task (Haiku/Sonnet/Opus) plus fixer hoher Effort; steht teils quer zur Eskalation von günstig nach teuer, da Effort dauerhaft hoch empfohlen wird.
- 2026-02-01 · [[2026-02-01-anthropic-docs-create-custom-subagents]] · meinung — Subagents haben pro Agent ein eigenes model-Feld; Explore läuft read-only auf Haiku, leichte Tasks sollen an Haiku gehen. Sekundärquelle, Stand Februar 2026.
- 2026-09-09 · [[2026-09-09-voxyz_ai-2097814698204832116]] · meinung — Codex-Agent-Tree: Luna (max) erkundet, Sol (high) implementiert, Astra (medium) orchestriert und verifiziert, Astra (xhigh) nur bei Bedarf als Review. Effort-Wahl angeblich nach DeepSWE, Zahlen nicht mitgeliefert.

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
