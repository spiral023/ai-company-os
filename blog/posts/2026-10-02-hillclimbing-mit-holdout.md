---
titel: "Evals verbessern, ohne sich selbst zu täuschen: Hillclimbing mit Holdout"
datum: 2026-10-02
kategorie: arbeitsweisen
zusammenfassung: "Wer einen Prompt gegen ein Eval optimiert, optimiert irgendwann das Eval selbst. Ein zufälliger Train/Test-Split mit Revert-Regel macht das sichtbar; Claude Code bringt dafür zwei Befehle mit."
status: freigegeben
geprueft_am: 2026-10-02
quellen:
  - 2026-09-28-claude-automating-eval-design-and-hillclimbing-with-cla
---

## Kurz gesagt

- Teile deine Eval-Fälle zufällig in Train und Test. Der Optimierer sieht nur Train, und eine Änderung bleibt nur, wenn beide Werte steigen.
- In Claude Code übernehmen `/claude-api build-eval` und `/claude-api hillclimb` diesen Ablauf. Vorher `claude update`, sonst fehlen die Befehle möglicherweise.
- Ein Eval mit 14 Test-Fällen liefert Richtungen, keine Beweise. Prüfe die angegebene Schwankungsbreite, bevor du etwas übernimmst.

## Das Problem: Der Score steigt, die Produktion nicht

Du baust ein Eval, siehst einen Score von 70 %, besserst den Prompt nach, und der Score steigt. Das fühlt sich nach Fortschritt an. Es kann aber auch heißen, dass du dem Prompt beigebracht hast, genau diese Fälle zu lösen. Anthropic beschreibt das als Overfitting auf das Eval: Das System schneidet auf der Eval besser ab als auf echtem Traffic. {q:1}

Das Risiko ist größer, als es klingt, weil der Weg dorthin unauffällig ist. Ein Eval mit Aufgaben, die OCR brauchen, belohnt einen OCR-Baustein, der im Produktivbetrieb nie gebraucht wird. Kopierst du Fehlerinhalte in den Prompt, löst er bald genau diese Fehler. Im Extremfall findet das Modell die Antworten direkt, etwa in einem öffentlichen Repository. {q:1}

## Erst ein Eval, das etwas taugt

Hillclimbing hilft nur, wenn das Eval selbst stimmt. Anthropic nennt vier Eigenschaften: Die Aufgaben spiegeln die Produktion, stärkere Modelle und mehr Effort schneiden besser ab, das beste Modell liegt deutlich unter 100 %, und die Läufe schwanken wenig. {q:1}

Die Fälle wählst du nicht danach aus, woran das heutige Modell scheitert. Sonst misst du den Fehler-Fingerabdruck dieses einen Modells. Besser sind Fälle aus Tickets, Bug Reports und Produktionsfehlern, bei denen du begründen kannst, warum sie schwer sind. Reiner Nutzertraffic fällt oft zu leicht aus, weil Nutzer das versuchen, was voraussichtlich klappt. {q:1}

Beim Grader nimmst du die billigste Prüfung, die passt: einen Code-Check bei festem Ausgaberaum, sonst ein zweites Modell als Richter mit einer Rubrik aus prüfbaren Aussagen statt einer Skala von 1 bis 5. Der Richter sollte nicht das getestete Modell sein. Lies danach selbst eine Stichprobe bewerteter Antworten, und lass den Grader zweimal über dieselbe Ausgabe laufen. Ändert sich das Urteil, hast du ein Varianzproblem im Eval. {q:1}

## Der Ablauf mit Holdout

1. **Zufällig teilen.** Ein Teil der Fälle ist Train, den der Optimierer lesen darf. Der Rest ist Test und bleibt unsichtbar.
2. **Rauschen messen.** Der Score darf zufällig nicht stärker schwanken als die kleinste Verbesserung, auf die du reagieren würdest. Sonst brauchst du mehr Fälle oder Wiederholungen.
3. **Eine Änderung pro Runde,** an der Ursache statt als Umformulierung.
4. **Behalten oder zurücknehmen.** Steigen Train und Test, bleibt die Änderung. Steigt nur Train, ist das ein Verdacht auf Overfitting, und die Änderung fliegt raus. Dasselbe gilt für jede Regression.
5. **Bei Stillstand nicht weiter ändern.** Nach zwei bis drei flachen Runden sortierst du alle Restfehler nach Ursache: fehlender Inhalt, veraltetes Vorwissen des Modells, fehlerhafte Aufgabe oder fehlerhafter Grader, reine Varianz. Nur echte Fehler gehen in weitere Runden. {q:1}

Der fünfte Schritt findet Fehler im Eval selbst. In Anthropics Skill-Beispiel verlangte eine Aufgabe Code, der einen Fehlertyp fängt, während der Grader eine Kette von mindestens drei Fehlern wollte. Ein anderer Grader widersprach der Dokumentation, und ein Test gegen die echte API zeigte, dass die Dokumentation recht hatte. {q:1}

## Was dabei herauskam

Anthropic hat den Ablauf an einem internen Support-Benchmark mit 44 Tickets gemessen: 30 zum Suchen, 14 als Holdout. Ziel war weniger Kosten bei besserer Genauigkeit. Der Start war Opus 4.8 auf `high` mit 74,4 % bei 4,6 Cent pro Ticket. Der Hillclimb räumte zuerst den Prompt auf, dann kam Opus 5.5 auf `low` mit 87,8 % bei 1,9 Cent. Sonnet 5 auf `low` erreichte 88,9 % bei einem Cent. Mit verbessertem Prompt (Routing-Regeln, ein Querverweis auf die Erstattungsgrenze) stieg Sonnet 5 auf 98,9 % bei gleichem Preis. {q:1}

Auf den 14 Tickets, die die Suche nie gesehen hatte, lag die Endkonfiguration bei 90,5 % gegen 78,6 % für das Original, bei etwa einem Fünftel der Kosten. {q:1} Die 98,9 % gelten also nur für die Such-Tickets. Der Holdout-Wert ist die Zahl, auf die du dich verlassen solltest.

Das zweite Beispiel ist das Eval für den `claude-api`-Skill. Es stieg in 24 Runden von 66,1 % auf 87,9 %. Den größten Teil brachten fehlende Abschnitte, eine Tabelle von älteren auf aktuelle API-Formen und korrigierte Aufgaben und Grader. {q:1}

## Selbst ausprobieren

In Claude Code aktualisierst du zuerst mit `claude update`, weil der `claude-api`-Skill mit dem Programm ausgeliefert wird. Danach:

```
/claude-api build-eval
/claude-api hillclimb
```

`build-eval` interviewt dich, sammelt Fälle aus Produktions-Transkripten, Tickets und eigenen Beispielen, schlägt einen Grader vor und wartet auf deine Freigabe. Danach läuft die Baseline, der Score kommt mit Schwankungsbreite. Liegt sie schon bei etwa 95 % oder höher, warnt der Skill, und du solltest eher Kosten als Qualität optimieren. `hillclimb` fragt nach deinem Ziel, teilt die Fälle, geht Runde für Runde vor und lässt deinen Code am Ende auf dem Stand, der auf dem Test-Split am besten war. Liegt der Gewinn im Rauschen, rät er vom Mergen ab. {q:1}

Geeignet sind billig änderbare, klar zuordenbare Stellen wie Prompts, Skill-Beschreibungen oder die Wahl von Modell und Effort. Offene Umbauten am Harness stocken eher, weil sich ein Score-Sprung nicht mehr einer Änderung zuordnen lässt. {q:1} Wie du mit Evals ein Plugin gegen den Fall ohne Plugin misst, steht in [Plugin-Evals in Claude Code](post:plugin-evals-in-claude-code).

## Grenzen und Kosten

Die Zahlen stammen von Anthropic selbst, ohne Rohdaten, und beschreiben einen internen Benchmark. Bei 14 Holdout-Tickets {q:1} verschiebt ein einzelner Fall den Wert um rund 7 Prozentpunkte (eigene Rechnung). Der Abstand von 90,5 % zu 78,6 % {q:1} ist deshalb ein Hinweis, keine sichere Aussage. Unabhängige Erfahrungsberichte zum Train/Test-Split bei kleinen Eval-Mengen fehlen bisher.

Dazu kommen die Kosten. Jede Runde führt das Eval erneut aus, und Wiederholungen gegen das Rauschen vervielfachen die Läufe. Bei einem LLM-Richter zahlst du außerdem für jede Bewertung. `build-eval` nennt dir vor dem Start Umfang und ungefähre Dauer. Lies diese Angabe, bevor du bestätigst.

Mein Rat: Fang mit einem Prompt oder einer Skill-Beschreibung an, für die du schon 30 bis 50 echte Fälle hast. Gib dem Ablauf ein klares Ziel, entweder gleiche Qualität bei weniger Kosten oder mehr Qualität auf einem Eval mit Luft nach oben. Übernimm das Ergebnis erst, wenn der Test-Split es trägt.
