# Formale Verifikation mit unabhängigem Proof-Checker

**Konfidenz:** meinung

## Zweck

Eine ausdrücklich festgelegte Eigenschaft eines abgegrenzten Programms für den modellierten Eingaberaum nachweisen. Generative Beweissuche und die Prüfung des fertigen Beweises werden getrennt, damit ein Agent sein Ergebnis nicht allein selbst beurteilt.

## Funktionsweise

Aus vorhandenen Tests, Anforderungen oder Normen eine formale Aussage ableiten. Eingabegrenzen, Speicherbudget, Threading, Bibliotheksbindung und Ausführungsmodell ausdrücklich dokumentieren. Ein Agent erzeugt Beweisartefakte und gegebenenfalls minimale Programmänderungen; ein formaler Checker prüft, ob das Artefakt die festgelegte Aussage unter diesen Annahmen beweist.

Die Soll-Eigenschaft und notwendige Patches werden zusätzlich fachlich kontrolliert. Eine Änderung darf den Nachweis nicht dadurch trivialisieren, dass sie erwünschtes Verhalten entfernt. Bereits geprüfte Hilfsbeweise können kopiert und angepasst werden; auch angepasste Artefakte müssen erneut durch den Checker. Anthropics und Theorems Versuch nutzt dafür Rocq und eine modellierte RISC-V-/Linux-Ausführung.

## Vorteile

- Geprüft wird eine Aussage über den festgelegten Eingaberaum, nicht nur eine Sammlung tatsächlich ausgeführter Testfälle.
- Beweisartefakte bleiben überprüfbar, auch wenn die generative Suche lange und teuer war.
- Wiederverwendbare Hilfsbeweise können parallele Beweissuche entlasten.

## Nachteile & Grenzen

- Eine falsche oder unvollständige Spezifikation kann korrekt bewiesen werden und trotzdem das falsche Produkt beschreiben.
- Vertrauen bleibt in Checker, Semantik und Modellannahmen erforderlich; unmodellierte Umgebungswirkungen werden nicht mitbewiesen.
- Im berichteten Versuch gelten unter anderem eine 64-MB-Eingabegrenze und Single-Thread-Annahmen; ungeprüfte Einstiegspunkte und Aufrufer bleiben außerhalb des Nachweises.
- Beweissuche kann Hunderte Millionen Tokens beanspruchen. Ein nicht gefundener Beweis ist kein automatischer Nachweis eines Programmfehlers.

## Wann einsetzen, wann nicht

- Einsetzen: klar formulierbare Eigenschaften in begrenzten, wichtigen Codepfaden mit geeignetem formalen Modell und prüfbarem Artefakt.
- Nicht einsetzen: als pauschalen Ersatz für Spezifikationsreview, Integrationstests, Betriebsprüfung oder eine vollständige Security-Abnahme.

## Belege

- 2026-10-22 · [[2026-10-22-anthropic-llms-are-making-formal-software-verification-fea]] · meinung — Anthropic und Theorem berichten über geprüfte Rocq-Beweise für 239 Fuzz-Einstiege in 123 Bibliotheken unter begrenzten Eingabe- und Ausführungsannahmen. Der Hersteller-/Partnerbericht belegt weder vollständige Bibliotheksabdeckung noch reale Gesamtsicherheit; die Ergebnisse wurden hier nicht reproduziert.
- 2026-10-21 · [[2026-10-21-githubnext-2112936525457740139]] · meinung — Die PDD-Kit-Ankündigung trennt menschlich bestätigte Verus-Spezifikation, formale Beweisprüfung und empirische Fallbacks; die Korrektheit der Spezifikation und der nicht formal geprüften Teile bleibt eine gesonderte Grenze, die Videodemo wurde nicht gesichtet.

## Spannungen & offene Fragen

- 2026-10-24 · [[2026-10-22-anthropic-llms-are-making-formal-software-verification-fea]]: Der Checker kann einen gültigen Beweis akzeptieren, obwohl ein Agent durch Patches unerwünschtes Verhalten eingeführt oder die Soll-Eigenschaft ausgehöhlt hat. Beweisprüfung und fachliche Verhaltensabnahme sind deshalb getrennte Kontrollpunkte.

## Verwandte Patterns

- [[Testharness-als-staerkster-Hebel]]
- [[TDD-als-Verifikationshebel]]
- [[Kontrollierte-Agent-Parallelisierung]]
