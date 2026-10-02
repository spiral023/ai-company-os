# Hillclimbing-mit-Holdout-Split

**Konfidenz:** meinung

## Zweck

Verbessert einen Prompt, Skill, eine Tool-Beschreibung oder Modell- und Effort-Wahl schrittweise gegen ein Eval, ohne sich dabei selbst zu täuschen. Adressiert das Kernrisiko jeder Eval-gestützten Optimierung: Overfitting auf die Eval-Fälle, das den Score hebt, im echten Betrieb aber nichts bringt.

## Funktionsweise

1. **Eval taugt erst etwas, wenn es Produktion spiegelt.** Aufgaben aus echtem Traffic, Bug-Reports und Tickets, ergänzt um Fälle, deren Schwierigkeit ein Mensch begründen kann. Nicht danach auswählen, woran das heutige Modell scheitert, sonst misst das Eval nur dessen Schwächen. Das stärkste Modell auf höchstem Effort muss klar unter 100 % liegen, ohne dass unlösbare oder mehrdeutige Aufgaben das erklären.
2. **Grader validieren.** Billigste passende Prüfung (Code-Check bei festem Ausgaberaum, sonst LLM-as-Judge mit prüfbaren Aussagen statt 1-bis-5-Skala, Judge ≠ getestetes Modell). Ein Mensch liest eine Stichprobe bewerteter Transkripte gegen; der Grader läuft zweimal auf derselben Ausgabe, um Varianz zu sehen.
3. **Fälle zufällig in Train und Test teilen.** Der Optimierer liest nur Train-Transkripte, den Test-Split sieht er nie.
4. **Noise-Check vor Runde 1.** Das Rauschen des Scores muss kleiner sein als die kleinste Verbesserung, auf die du reagieren würdest; sonst mehr Fälle oder Wiederholungen.
5. **Eine Änderung pro Runde**, an der Ursache statt als Umformulierung. Behalten nur, wenn Train und Test steigen; zurücknehmen, wenn nur Train steigt oder irgendwo eine Regression auftritt. Fehlerinhalte nie in den Prompt kopieren, Antworten strukturell außer Reichweite halten.
6. **Bei Stillstand nach zwei bis drei Runden** keine Änderung, sondern alle Restfehler nach Ursache sortieren: Inhaltslücke, veralteter Modell-Prior, fehlerhafte Aufgabe oder Grader, Varianz. Nur echte Fehler gehen in weitere Runden.
7. **Abschluss** mit dem besten Stand auf dem Test-Split und Konfidenzintervall gegenüber der Baseline; liegt der Gewinn im Rauschen, nicht mergen.

Gut geeignete Oberflächen sind billig änderbar und eindeutig zurechenbar, etwa Skill-Beschreibungen für die Trigger-Rate. Ist das Eval nahezu gesättigt (Baseline ab etwa 95 %), ist Kosten bei gleicher Qualität das sinnvollere Ziel.

## Vorteile

- Overfitting wird sichtbar und automatisch zurückgedreht, statt im Score zu verschwinden.
- Die Stillstandsanalyse findet Fehler im Eval selbst (falscher Grader, mehrdeutige Aufgabe), nicht nur im optimierten Artefakt.
- Funktioniert auch als Kostenoptimierung: Modell- und Effort-Stufe absenken, solange der Test-Score hält.

## Nachteile & Grenzen

- Braucht genug Fälle für einen aussagekräftigen Test-Split; im Beispiel der Quelle sind es nur 14 Holdout-Tickets.
- Wiederholungen pro Runde kosten Tokens und Zeit.
- Offene Änderungen am Harness lassen sich schlecht zurechnen und stocken eher.
- Die Belege sind bisher Selbstmessungen des Herstellers.

## Wann einsetzen, wann nicht

- Einsetzen: Prompts, Skills, Tool-Beschreibungen, Modell- oder Effort-Wahl, wenn ein Eval mit Headroom existiert oder sich bauen lässt.
- Nicht einsetzen: ohne validierten Grader, bei gesättigtem Eval mit Qualitätsziel, bei offenen Harness-Umbauten ohne klare Zurechnung.

## Belege

- 2026-09-28 · [[2026-09-28-claude-automating-eval-design-and-hillclimbing-with-cla]] · meinung — Anthropic beschreibt Eval-Design-Regeln und den Hillclimb-Loop samt Revert-Regeln (`/claude-api build-eval`, `/claude-api hillclimb`); Support-Benchmark auf Holdout 90,5 % gegen 78,6 % bei etwa einem Fünftel der Kosten und `claude-api`-Skill von 66 % auf etwa 88 % als Selbstmessung.
- 2026-07-01 · [[2026-07-01-0xcodila-2072329149520232639]] · meinung — Karpathys `autoresearch`: nur `train.py` änderbar, Evaluator gesperrt, Commit bei Verbesserung, sonst Rollback; Bilevel-Variante mit äußerem Loop soll laut Paper -0,045 statt -0,009 `val_bpb` erreichen. Kein Holdout erwähnt, Zahlen ungeprüft aus zweiter Hand.
- 2026-07-16 · [[2026-07-16-amasad-2077802290304684404]] · meinung — Replit Agent verbessert sich per Schleife aus Benchmarks vor dem Release und A/B-Tests mit geclusterten Traces danach. Nur als Skizze beschrieben, kein Holdout oder Rausch-Check erwähnt.

## Spannungen & offene Fragen

- Bisher nur eine Quelle, und die stammt vom Anbieter des Werkzeugs. Unabhängige Erfahrungsberichte zum Train/Test-Split bei kleinen Eval-Mengen fehlen.

## Verwandte Patterns

- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- [[Testharness-als-staerkster-Hebel]]
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
