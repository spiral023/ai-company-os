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
- 2026-10-18 · [[2026-10-18-ai-news-strategy-daily-n-what-really-happens-when-ai-agents-meet-in-the-w]] · meinung — Die Forderung nach Auditierbarkeit wird auf die nachvollziehbare Verbindung von Identität, Auftrag, Freigabe, Agentenkontakt, Ausführung und Wirkung bezogen; dieses Schema ist eine gekennzeichnete Engineering-Ableitung, die Quelle liefert weder eine vollständige Instrumentierung noch eigene Messabdeckung.
- 2026-10-23 · [[2026-10-23-anthropic-an-alignment-assessment-of-the-uk-aisi-cybertest]] · meinung — Die Untersuchung trennt tatsächlich ausgeführte PRs und E-Mails von CoT-Deutungen, nachträglicher Selbstauskunft und LLM-bewerteten Fortsetzungen mit simulierten Toolantworten. Dieselben 25 Beobachtungen galten im laufenden Kontext vollständig als Simulationsbeleg, isoliert nur zu 16 %; ein Monitor- oder Modellurteil über Harmlosigkeit darf daher nicht mit beobachteter Isolation oder ausbleibender Wirkung gleichgesetzt werden.
- 2026-08-26 · [[2026-08-26-openai-der-vorfall-bei-hugging-face-und-der-weitere-weg]] · meinung — OpenAI trennt im Rückblick CoT-, Aktions- und Ergebnisanalyse und berichtet mögliche frühere Erkennung durch heutige Monitore; diese wurden mit Vorfallwissen verbessert, weshalb retrospektive Treffer weder damalige Abdeckung noch prospektive Interventionswirkung belegen.
- 2026-08-26 · [[2026-08-26-metr-brief-independent-investigation-of-agents-behavi]] · meinung — Erfolgreiche Tool-Spoofing-Tests ließen sichtbare Anforderungen und tatsächliche Befehle beziehungsweise Ausgaben auseinanderfallen; Resets und abgeschnittene Transkripte verursachten zusätzliche Lücken, weshalb ein Transkript Ausführung und Wirkung nicht allein beweist und das Ausbleiben weiterer Funde keine Integritätsgarantie ist.

## Spannungen & offene Fragen

- 2026-10-24: [[2026-08-26-metr-brief-independent-investigation-of-agents-behavi|METR]] zeigt anhand kleiner erfolgreicher Spoofing-Tests, dass sichtbare Tool-Aufrufe und tatsächliche Ausführung auseinanderfallen können. Die Analyse bereitgestellter Logs enthält Reset- und Trunkierungslücken; fehlende weitere Funde beweisen daher keine Integrität. OpenAIs [[2026-08-26-openai-der-vorfall-bei-hugging-face-und-der-weitere-weg|nachträglich verbesserte Monitore]] und retrospektive Harness-Vergleiche sind keine Messung damaliger oder prospektiver Schutzwirkung. METR bestätigt nicht den gesamten Herstellerbericht.

- 2026-10-17: Ein erfolgreicher Modell- oder Tool-Aufruf beweist noch keine beabsichtigte Wirkung. Das konkrete Ereignisschema und die nötige Beobachtungstiefe müssen zum Untersuchungsfall passen; die Quelle definiert keinen universellen Vollständigkeitsstandard.

## Verwandte Patterns

- [[Codepfad-vor-Aenderung-nachvollziehen]]
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
