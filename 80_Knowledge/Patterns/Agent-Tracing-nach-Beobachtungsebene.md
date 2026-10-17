# Agent-Tracing nach Beobachtungsebene

**Konfidenz:** meinung

## Zweck

Agentenläufe untersuchen, ohne Modellaufruf-Logs mit einer vollständigen Aufzeichnung von Ausführung und Wirkung zu verwechseln.

## Funktionsweise

Vor der Instrumentierung festlegen, welche Fragen beantwortet werden sollen. Modellaufrufe, Harness-Operationen, native Sitzungshistorien, verteilte Prozesse und Umgebungsartefakte als unterschiedliche Beobachtungsebenen behandeln. Tool-Anforderung, tatsächliche Ausführung und resultierende Änderung getrennt erfassen und soweit möglich über Sitzungs- und Delegationsgrenzen verbinden.

Strukturierte Rohereignisse und Verweise auf Diffs, Tests oder andere Ergebnisartefakte erhalten. Mehrfach erfasste Ereignisse und nicht instrumentierte Bereiche sichtbar machen. Semantische Bewertungen und aus Traces gewonnene Regressionstestfälle sind nachgelagerte Auswertungen; sie erweitern nicht rückwirkend die beobachtete Abdeckung.

## Vorteile

- Die Instrumentierung folgt einer konkreten Diagnosefrage.
- Fehlende Beobachtungen bleiben von negativen Ergebnissen unterscheidbar.
- Rohdaten lassen sich später mit anderen Fragen erneut auswerten.

## Nachteile & Grenzen

- Logs, Korrelation und Aufbewahrung verursachen Betriebs- und Auswertungsaufwand.
- Gemeinsame Konventionen wie OpenTelemetry garantieren keine einheitliche Beobachtungstiefe.
- Veränderte Umgebungen und nichtdeterministische Antworten verhindern garantierte exakte Wiederholung.

## Wann einsetzen, wann nicht

- Einsetzen: Fehlersuche und Evaluation über mehrere Tools, Prozesse oder Sitzungen.
- Nicht einsetzen: Eine einfache Frage wird bereits von einem begrenzten Tool-Ergebnis beantwortet; zusätzliche Vollerfassung hätte keinen erkennbaren Nutzen.

## Belege

- 2026-10-12 · [[2026-10-12-josharosen-2109649928276341191]] · meinung — Die Architekturübersicht trennt Modell-, Harness-, Sitzungs-, verteilte und Umgebungssicht sowie semantische Anreicherung; sie liefert keine quantitative Abdeckungs- oder Genauigkeitsprüfung.

## Spannungen & offene Fragen

- 2026-10-17: Ein erfolgreicher Modell- oder Tool-Aufruf beweist noch keine beabsichtigte Wirkung. Das konkrete Ereignisschema und die nötige Beobachtungstiefe müssen zum Untersuchungsfall passen; die Quelle definiert keinen universellen Vollständigkeitsstandard.

## Verwandte Patterns

- [[Codepfad-vor-Aenderung-nachvollziehen]]
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
