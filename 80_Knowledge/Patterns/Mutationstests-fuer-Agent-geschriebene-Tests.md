# Mutationstests für agentengeschriebene Tests

**Konfidenz:** meinung

## Zweck

Untersuchen, ob eine Testsuite verhaltensrelevante Fehler erkennt, statt einen erfolgreichen Testlauf bereits als ausreichenden Qualitätsnachweis zu behandeln.

## Funktionsweise

Stand der Ausarbeitung: 2026-10-22. Ein Mutationstool verändert Quellcode kontrolliert und führt die Tests erneut aus. Pococks Beispiel ersetzt einen String durch einen leeren String; ein geeigneter Test sollte eine dadurch verletzte Anforderung erkennen. Überleben Mutanten die Tests, erhält der Agent konkrete Stellen zur Untersuchung.

Als fachliche Einordnung gilt: Erst prüfen, ob der Mutant tatsächlich relevantes Verhalten verändert und im vereinbarten Testumfang liegt. Dann einen an der Anforderung ausgerichteten Test ergänzen und gegen unveränderten sowie mutierten Code kontrollieren. Ein höherer Mutationswert ist ein Prüfsignal, keine unabhängige Bestätigung der Produktqualität. Die Quelle nennt Stryker.js für TypeScript als Beispiel; sie weist keinen allgemeinen Qualitätsgewinn nach.

## Vorteile

- Zeigt konkrete Kandidaten für schwache Assertions oder fehlende Testfälle.
- Gibt dem Agent eine nachvollziehbare Fehlerprobe statt ausschließlich eines grünen Testlaufs.

## Nachteile & Grenzen

- Zusätzliche Testausführungen kosten Laufzeit.
- Nicht jede Quellcodeänderung erzeugt einen fachlich relevanten Unterschied; überlebende Mutanten müssen beurteilt werden.
- Die untersuchten Mutationen ersetzen weder realistische Anforderungen noch die Prüfung anderer Fehlerklassen.
- Die bisherige Evidenz ist eine kurze Empfehlung mit Beispiel, kein kontrollierter Wirksamkeitsnachweis.

## Wann einsetzen, wann nicht

- Einsetzen: wenn eine bestehende Testsuite wichtige Agent-Änderungen absichern soll und ihre Aussagekraft unklar ist.
- Nicht einsetzen: als alleinige Freigabemetrik oder als Ersatz für das Klären des erwarteten Verhaltens.

## Belege

- 2026-10-14 · [[2026-10-14-matt-pocock-mutation-testing-is-awesome]] · meinung — Pocock demonstriert kontrollierte Codeänderungen mit Stryker.js als Feedback für Tests; qualitative Empfehlung ohne unabhängigen Wirksamkeitsnachweis.

## Spannungen & offene Fragen

- 2026-10-22: Pocock fordert das Eliminieren überlebender Mutanten. Als fachliche Grenze muss zuvor ihre Verhaltensrelevanz geprüft werden; den Score allein zu optimieren kann die eigentliche Anforderung aus dem Blick verlieren.

## Verwandte Patterns

- [[Testharness-als-staerkster-Hebel]]
- [[TDD-als-Verifikationshebel]]
- [[Hillclimbing-mit-Holdout-Split]]
