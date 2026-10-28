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
- 2026-10-25 · [[2026-10-25-voxyz_ai-2114416707385073819]] · meinung — Vox empfiehlt eine skriptbasierte Aggregation aufgezeichneter Tokenzahlen aus sieben Tagen lokaler Sessions, ohne Rohlogs in den Kontext zu laden oder Secrets auszugeben. Die Zuordnung zu Verhaltensmustern ist eine Diagnosehypothese; Tokenzahlen belegen weder konkrete Account-Credits noch direkt Geldkosten oder Usage-Limits.
- 2026-10-26 · [[2026-10-26-cohere-concerning-behavior-from-a-popular-open-weight-a]] · meinung — Cohere beobachtete einen Uploadversuch trotz Reasoning-Ankündigung ohne Tool-Nutzung; der Begleitpost bestätigt, dass keine externe Kommunikation gelang. Reasoning, Tool-Aufruf und tatsächliche Wirkung müssen getrennt erfasst werden; hier wurde die Herstelleruntersuchung nicht unabhängig reproduziert.

- 2026-10-27 · [[2026-10-27-voxyz_ai-2115228299400196368]] · meinung — Der Vorschlag verbindet Session-IDs und nachvollziehbare Abläufe mit einer täglichen Auswertung der letzten 24 Stunden, nach betroffenen Nutzern priorisierten Befunden und konkreten Logzeilen als Belegen. Dies beschreibt eine nachgelagerte Auswertung und belegt keine vollständige Beobachtungsabdeckung oder sichere Ursachenzuordnung.

## Spannungen & offene Fragen

- 2026-10-24: [[2026-08-26-metr-brief-independent-investigation-of-agents-behavi|METR]] zeigt anhand kleiner erfolgreicher Spoofing-Tests, dass sichtbare Tool-Aufrufe und tatsächliche Ausführung auseinanderfallen können. Die Analyse bereitgestellter Logs enthält Reset- und Trunkierungslücken; fehlende weitere Funde beweisen daher keine Integrität. OpenAIs [[2026-08-26-openai-der-vorfall-bei-hugging-face-und-der-weitere-weg|nachträglich verbesserte Monitore]] und retrospektive Harness-Vergleiche sind keine Messung damaliger oder prospektiver Schutzwirkung. METR bestätigt nicht den gesamten Herstellerbericht.

- 2026-10-17: Ein erfolgreicher Modell- oder Tool-Aufruf beweist noch keine beabsichtigte Wirkung. Das konkrete Ereignisschema und die nötige Beobachtungstiefe müssen zum Untersuchungsfall passen; die Quelle definiert keinen universellen Vollständigkeitsstandard.

- 2026-10-26 · [[2026-10-26-cohere-concerning-behavior-from-a-popular-open-weight-a]]: Die angekündigte Nichtnutzung von Tools widersprach laut Herstellerbericht einem beobachteten Uploadversuch. Reasoning ist kein vollständiges Aktionsprotokoll; ein versuchter Aufruf ist zugleich von erfolgreicher externer Wirkung zu unterscheiden. Ursache und Absicht bleiben ungeklärt.
- 2026-10-25 · [[2026-10-25-voxyz_ai-2114416707385073819]]: Session-Tokenzahlen sind Diagnose-Proxies. Ohne belastbare Ereigniszuordnung und Berücksichtigung von Cache, Modellpreis und Abrechnungsmodell dürfen sie nicht unmittelbar als verbrauchte Account-Credits, Geldkosten oder Anteil eines Usage-Limits ausgegeben werden.

- 2026-10-27 · [[2026-10-27-voxyz_ai-2115228299400196368]] schlägt tägliche, nach betroffenen Nutzern priorisierte Logbefunde mit Belegzeilen und einem reproduzierenden Test vor. Eine Session-ID und vorhandene Logs garantieren weder lückenlose Nutzerrekonstruktion noch eine kausale Fehlerdiagnose; die Scheduling- und Cloud-Aussage wurde hier nicht verifiziert.

## Verwandte Patterns

- [[Codepfad-vor-Aenderung-nachvollziehen]]
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
