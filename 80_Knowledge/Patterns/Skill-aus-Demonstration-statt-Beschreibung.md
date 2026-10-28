# Skill-aus-Demonstration-statt-Beschreibung

**Konfidenz:** meinung

## Zweck

Löst das Problem, dass manche Arbeitsweisen sich leichter zeigen als beschreiben lassen — ein Design-Schema, ein Klickpfad in einer Oberfläche oder ein visuelles Muster ist oft schwer präzise in Prosa zu fassen, aber sofort erkennbar, wenn man es sieht. Ergänzt die verbale Skill-Erstellung um einen zweiten, bildbasierten Eingabekanal.

## Funktionsweise

Statt einen Skill ausschließlich aus einer verbalen Spezifikation zu bauen, entsteht er aus einem gezeigten Beispiel: ein Screenshot eines gefallenden Designs wird dem Agenten gegeben, der daraus einen Skill ableitet, der dieses Design-Schema repliziert; oder ein aufgezeichneter Bedienungsablauf (Browser-Interaktionen) dient als Vorlage, aus der ein neuer Workflow-Skill entsteht, ohne dass der Ablauf schriftlich spezifiziert werden muss. In beiden Fällen liefert das gezeigte Beispiel — Bild oder aufgezeichnete Interaktion — die Spezifikation, aus der der Agent den Skill selbst extrahiert.

Datierte Ergänzung vom 2026-10-27: [[2026-10-27-alexgoughcooper-2115076988327076296|Cooper]] konkretisiert die Demonstration für Videoschnitt: je Stil vier bis fünf Referenzedits sammeln, erfahrene Editoren ihre Entscheidungen in kommentierten Screenrecordings erklären lassen und den abgeleiteten Skill auf 25 vorhandene Anzeigen anwenden. Senior-Feedback wird in weiteren Runden eingearbeitet; die fachliche Trainingszeit ist Teil des Aufwands. Das ist die beschriebene Lernschleife, kein gemessener Produktivitätsgewinn.

## Vorteile

- Erfasst Arbeitsweisen, die sich nur schwer in Prosa präzise beschreiben lassen (visuelle Muster, feinmotorische Bedienabläufe), ohne dass der Mensch sie erst verbalisieren muss.
- Senkt die Einstiegshürde zur Skill-Erstellung für Personen, die eine Arbeitsweise zwar ausführen, aber nicht ohne Weiteres in eine klare Beschreibung übersetzen können.
- Ergänzt statt ersetzt die verbale Skill-Erstellung — beide Eingabekanäle lassen sich je nach Aufgabe wählen.

## Nachteile & Grenzen

- Der aus einer Demonstration abgeleitete Skill kann implizite Annahmen der einen gezeigten Instanz überverallgemeinern, wenn nur ein einziges Beispiel vorliegt.
- Keine der beiden bisherigen Erwähnungen liefert einen Erfolgsnachweis oder eine Einschränkung — unbelegte Werkzeug-Erwähnung ohne Zahl, Beispielqualität oder Fehlerquote.
- Setzt ein Werkzeug voraus, das Bild- oder Interaktionsaufzeichnung überhaupt verarbeiten kann — nicht jede Agent-Umgebung bietet das.

## Wann einsetzen, wann nicht

- Einsetzen: wenn die zu erfassende Arbeitsweise primär visuell oder interaktions-basiert ist und sich schwerer verbal als bildlich spezifizieren lässt.
- Nicht einsetzen: bei Arbeitsweisen mit klaren, leicht in Prosa fassbaren Regeln — dort ist eine verbale Skill-Spezifikation präziser und einfacher zu pflegen als eine aus einem Einzelbeispiel abgeleitete.

## Belege

- 2026-01-21 · [[2026-01-21-aiedge-claude-50-pro-tips]] · meinung — X-Thread-Aufarbeitung (über vibedeck-Sekundärfassung) nennt zwei Varianten derselben Grundidee: Skill aus Design-Screenshot ableiten, sowie Cowork per aufgezeichnetem Browser-Ablauf einen neuen Workflow beibringen — beide ohne Erfolgsnachweis oder Einschränkung.
- 2025-10-31 · [[2025-10-31-agenticjames-best-claude-skills-for-agentic-coding]] · meinung — Skill-Generator, der wiederkehrende Chat-Muster zu Skills abstrahiert; nicht demonstriert, Wildwuchs-Risiko.
- 2026-09-20 · [[2026-09-20-voxyz_ai-2101657631249031507]] · meinung — Eigene Komponentenbibliothek und benannte Design-Operationen als Skill statt vager Prompts; Erfahrungsbericht ohne Messung.
- 2026-07-21 · [[2026-07-21-claudeai-2079595988998554047]] · meinung — Claude kündigt Skill-Erstellung durch Bildschirmaufnahme und gesprochene Erläuterung in Cowork an; das UI zeigt erfasste Klicks, Eingaben und Stimme sowie einen gespeicherten Skill. Dies ist ein Herstellerbeispiel zum Demonstrationsprinzip, kein unabhängig getesteter Wiederholungsnachweis.
- 2026-06-18 · [[2026-06-18-julian-ivanov-ki-automat-bau-dir-dein-ki-betriebssystem-mit-claude-code-k]] · meinung — Empfiehlt, eine wiederkehrende Aufgabe zuerst mit dem Agenten gemeinsam erfolgreich durchzuführen und anschließend den Ablauf als Skill festzuhalten. Der Bericht enthält keine kontrollierte Evaluation des abgeleiteten Skills.
- 2026-06-07 · [[2026-06-07-julian-ivanov-ki-automat-so-laesst-du-claude-jedes-video-fuer-dich-anscha]] · meinung — Zeitmarkierte Frames erschließen auch stumme oder nur visuell erklärte Abläufe als Eingabe für spätere Skill-Ableitung. Die Videoanalyse selbst ist ein vorgelagerter Evidenzprozess; ungeprüfte Stichproben dürfen nicht als vollständige Arbeitsanleitung gelten.

- 2026-10-27 · [[2026-10-27-mho_23-2115187475802890348]] · meinung — Miko betont, dass erfahrene Editoren ihr Prozesswissen in einen spezialisierten Schnitt-Harness und dessen Feedbackschleife einbringen sollen. Der Post verlinkt Cooper, liefert keine unabhängige Qualitätsmessung und belegt weder vollständig automatisierten Videoschnitt noch den behaupteten hundertfachen Nutzen.
- 2026-10-27 · [[2026-10-27-alexgoughcooper-2115076988327076296]] · meinung — Cooper konkretisiert die Skill-Gewinnung aus vier bis fünf Referenzedits und Screenrecordings, in denen erfahrene Editoren Schnitt-, Tempo- und B-Roll-Entscheidungen erklären. Die Verfeinerung beruht auf Expertenfeedback; gemessene Übertragbarkeit oder unabhängige Qualitätswerte fehlen.

## Spannungen & offene Fragen

- Einzige bisherige Quelle, selbst nur als Sekundärfassung ohne geprüfte Primärquelle vorliegend, und dort bereits als unbelegte Werkzeug-Erwähnung gekennzeichnet — keine unabhängige Zweitbestätigung, keine Messung.

- 2026-10-27 · [[2026-10-27-mho_23-2115187475802890348]] verlinkt [[2026-10-27-alexgoughcooper-2115076988327076296|Cooper]]. Die beiden Posts sind für dieselbe Produktivitäts- und Workflowbehauptung keine unabhängigen Bestätigungen. Ein erklärter Stil und Expertenfeedback belegen weder vollständige Automatisierung noch Übertragbarkeit auf jede Videoform.

## Verwandte Patterns

- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- [[Freiheitsgrad-nach-Aufgaben-Fragilitaet]]
