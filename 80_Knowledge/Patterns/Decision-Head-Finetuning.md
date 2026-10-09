# Decision-Head-Finetuning

**Konfidenz:** meinung

## Zweck

Spezialisiert ein kleines LLM auf Entscheidungen mit vorgegebenen Antwortoptionen, wenn allgemeines Prompting oder ein unverändertes Decision-Modell nicht ausreicht. Der Anwendungsfall ist Klassifikation und Routing mit gelabelten Beispielen, nicht die Generierung offener Antworten. Grundlage: [[2026-10-07-unslothai-decision-model-finetuning]].

## Funktionsweise

Unsloth beschreibt einen LLM-Backbone mit einem Clef-Head, der Optionen bewertet, und LoRA für die Anpassung. Die Inferenz gibt eine Auswahl mit Wahrscheinlichkeiten aus. Das ist eine trainierte Variante von [[Entscheidung-per-Scoring-statt-Generierung]]; sie reproduziert nicht dessen konkreten Label-Logit-Mechanismus.

Die Quelle nennt das Dataset-Format von Laya und Clef. Der ergänzend archivierte Guide beschreibt Holdout-Kalibrierung und eine separate Testauswertung. Als Einordnung für die eigene Anwendung: Eingabe, Fragen, Optionen und Goldantworten vorab definieren, Baseline und Fine-Tuning auf denselben zurückgehaltenen Testfällen vergleichen und Kalibrierung getrennt von Accuracy bewerten. Die Kontrolle gegen Overfitting ergänzt [[Hillclimbing-mit-Holdout-Split]].

Die berichtete Benchmark-Konfiguration lautet `r=64`, eine Epoche. Die Setup-Anleitung im Guide verwendet `r=16`, zwei Epochen. Das sind verschiedene Stände oder Versuchsbedingungen; eine exakte Reproduktion ist daraus nicht gesichert.

## Vorteile

- Liefert einen benannten Trainingsweg für lokale Decision-Modelle statt nur einer Inferenz-Umleitung.
- Unsloth berichtet Training für `Qwen3.5-0.8B` mit `4 GB VRAM` und für kleine Modelle wie Laya mit `2,5 GB VRAM`; kein eigener Hardwaretest.
- Der Herstellervergleich zeigt Accuracy-Gewinne je Datensatz, wodurch die Wirkung genauer beurteilt werden kann als anhand einer einzelnen aggregierten Zahl.

## Nachteile & Grenzen

- Die Ergebnisse sind Herstellermessungen; unabhängige Reproduktion und Kalibrierungswerte für den eigenen Einsatz fehlen.
- Gelabelte Daten, Training und Kalibrierung kommen als Aufwand zum lokalen Serving hinzu.
- Aggregate, einzelne Benchmark-Scores und Holdout-Accuracy messen unterschiedliche Ausschnitte. Für `0.8B` nennt der Post `20,7 % → 74,3 %` aggregiert, das Bild `78 %` auf Holdout; für `2B` stehen dort `81 %`.
- Die Modelle bewerten vorgegebene Optionen. Ihre Wahrscheinlichkeiten sind ohne eigenes Eval kein Beleg für Nutzerzufriedenheit oder absolute Präferenzen.
- Der verlinkte Unsloth-Code ist lokal nicht vorhanden und wurde nicht verifiziert.

## Wann einsetzen, wann nicht

- Einsetzen: als Offline-Versuch für Klassifikation oder Routing mit festem Antwortraum und eigenen gelabelten Fällen, wenn die Baseline messbare Fehler zeigt.
- Nicht einsetzen: für offene Textgenerierung, ohne getrennte Testfälle oder wenn die Benchmark-Werte als Qualitätsgarantie für eine andere Domäne dienen sollen.

## Belege

- 2026-10-07 · [[2026-10-07-unslothai-decision-model-finetuning]] · meinung — Herstellerbericht mit zwei Autor-Posts und Benchmark-Bild: Clef-Head plus LoRA, Accuracy-Gewinne für Qwen3.5-0.8B und 2B, Training ab 2,5 beziehungsweise 4 GB VRAM; ergänzender Guide beschreibt Kalibrierung, nennt aber abweichende Setup-Parameter.

## Spannungen & offene Fragen

- 2026-10-09: Benchmark-Konfiguration (`r=64`, eine Epoche) und Guide-Setup (`r=16`, zwei Epochen) stimmen nicht überein. Welche Konfiguration die einzelnen Tabellenwerte erzeugt hat, bleibt offen.
- 2026-10-09: Unsloth nennt Dekontamination und Kalibrierung, liefert im X-Beitrag aber weder das Prüfverfahren noch Kalibrierungsfehler. Accuracy allein beantwortet die Frage nach belastbaren Entscheidungsschwellen nicht.
- 2026-10-09: Offen bleibt, ob der Gewinn auf eigene Fälle übertragbar ist. Ein Repo-Import und eine getrennte lokale Evaluation wären weitere Arbeitsschritte.

## Verwandte Patterns

- [[Entscheidung-per-Scoring-statt-Generierung]]
- [[Hillclimbing-mit-Holdout-Split]]
- [[Lokale-Modell-Umleitung-Muster]]
