---
url: https://claude.dev/blog/solving-code-review-at-anthropic/
autor: "Addy Osmani"
datum: 2026-10-15
erfasst: 2026-10-17
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-10-15-claude-how-the-claude-code-team-does-code-review-claude.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Review nach Risiko, Belegen und menschlichem Aufwand steuern

Addy Osmani beschreibt den internen Review-Prozess des Claude-Code-Teams: Maschinen übernehmen wiederholbare Fehlersuche, Menschen beurteilen Absicht, Architektur, Risiko und verbleibende Prüflücken. Freigaben, Rückrollbarkeit und Kontextaufbau bilden eigene Aufgaben. Es handelt sich um einen Hersteller-Selbstbericht ohne unabhängige Messung oder hier durchgeführte Prüfung.

## Menschliche Aufmerksamkeit als Zielgröße

Das Team will den gesamten menschlichen Aufwand senken: Review-Zeit plus spätere Fehlerbehebung. Genannt werden menschliche Freigaben je PR mit Median und 95. Perzentil, Kommentare und Wartezeit; Reverts und Incidents dienen als Gegenkontrolle. Eine schnellere Freigabe wäre kein Gewinn, wenn Arbeit anschließend in Reparaturen wandert.

Laut Artikel haben sich gemergte Claude-Code-PRs von Juni bis September mehr als verdoppelt, während der Anteil zurückgenommener PRs um mehr als 40 Prozent sank. Absolute PR-/Revert-Zahlen und kontrollierte Vergleichsbedingungen fehlen. Das belegt weder eine bestimmte absolute Fehlerzahl noch eine kausale Wirkung einzelner Review-Maßnahmen. Die zusätzlich erwähnten Monorepo-Zahlen betreffen ausdrücklich einen anderen Repository-Kontext.

## Prüfbarkeit vor der Freigabe herstellen

Vor dem PR sollen ausführbare Tests, Builds oder Screenshots sichtbare Ergebnisse liefern. Ein Agent mit frischem Kontext prüft anschließend den Diff. Die PR-Vorlage fragt nach Tests, Risiko und Rücknahmeweg; der auftraggebende Mensch verantwortet diese Angaben.

Die allgemeine `CLAUDE.md` bleibt kurz. Bereichseigene `REVIEW.md`-Dateien beschreiben konkrete Fehlermodi, ignorierbare Pfade und Beleganforderungen mit Datei und Zeile. Laut Bericht wird gesondert geprüft, ob der Reviewer diese Anweisungen tatsächlich befolgt. Wiederkehrende Befunde wandern in Regeln, Skills oder deterministische Checks.

Der erste PR-Review betrachtet Diff, Repository und beabsichtigte Wirkung. Weitere Agents verifizieren Befunde; offene Bug- und Security-Threads blockieren den Merge, können aber mit begründeter Auflösung geschlossen werden. Das ist eine Befundbehandlung, kein Beweis für Fehlerfreiheit.

## Freigaberechte und Rücknahme getrennt absichern

Die Änderung bestimmt ihre Risikostufe; ein zweiter Klassifikator kann zusätzliche menschliche Prüfung verlangen. Sensible Pfade und CI-Workflows brauchen immer Menschen. Erleichterte Wege gelten nur für vertrauenswürdige Autoren; Agent-Freigaben ersetzen keinen vorgeschriebenen Menschen. Die Person hinter einem Agent-PR zählt als verantwortliche Beteiligte.

Freigaben gelten für einen konkreten Commit und müssen bei nicht verbürgten Folgeänderungen erneuert werden. Eine Merge Queue prüft das Zusammenspiel mit dem aktuellen Hauptzweig. Feature Flags, interne Nutzung, gestufte Releases und schnelle Reverts sollen Fehlerfolgen begrenzen; eine On-Call-Rotation trägt die Reaktion. Automatische Circuit Breaker, die bei schlechteren Revert-/Incident-Metriken die Freigaben verschärfen, fehlen nach eigener Aussage noch.

## Review-Schleifen müssen konvergieren

Incidents mit bestätigter Fehlerstelle werden tägliche Evals. Zusätzlich misst das Team Fehlalarme anhand menschlicher Reaktionen und bekanntermaßen sauberer PRs. Noise kostet bei Agent-Autoren zusätzliche Fixes, Commits und Review-Runden.

Nach einem berichteten Lauf mit über fünfzig Runden führte das Team einen Stopp nach drei Runden zum Überdenken des Ansatzes ein. Spätere Reviews betrachten nur neue Änderungen, melden Fehlerklassen gesammelt und wiederholen bestehende Befunde nicht. Runden bis zur Freigabe werden neben Erkennungsleistung verfolgt; nächtliche Bestandsprüfung bleibt eine separate Routine.

## Einordnung

Übertragbar sind die getrennten Verträge für Belege, Befunde, Freigaben und Rücknahme. Der interne Prozess geht laut Artikel weiter als das öffentliche Review-Produkt, das Befunde statt Freigaben liefert. Weniger menschliche Freigaben sind nur mit beobachteter Fehlerentwicklung sinnvoll zu bewerten. Kontextaufbau bleibt ausdrücklich eine zweite Review-Aufgabe ohne formalisierten Teamprozess. Dafür nutzt das Team aktuelle Modulerklärungen und kleine Visualisierungen vor anstehenden Änderungen; daraus folgt keine geprüfte vollständige Wissensabdeckung.

![Das lokal geprüfte Diagramm zeigt eine konkrete Modulfrage als Einstieg in Erklärung und Visualisierung; es enthält keine Wirksamkeitsmessung.](../../00_Inbox/Quellen/URL/medien/2026-10-15-claude-how-the-claude-code-team-does-code-review-claude/01-bild.png)

## Kernaussagen

- [[Review-Autonomie-mit-Shadow-Mode-und-Stichproben]]: Risiko, vertrauenswürdige Autoren, menschliche Pflichtprüfung und commitgebundene Freigaben begrenzen Autonomie; automatische Gegensteuerung fehlt noch.
- [[Testharness-als-staerkster-Hebel]]: Ausführbare Belege, Incident-Evals und saubere Kontroll-PRs prüfen sowohl übersehene Bugs als auch schädliche Fehlalarme.
- [[Codepfad-vor-Aenderung-nachvollziehen]]: Vor der eigenen Änderung den betroffenen Bereich gezielt erklären lassen; triviale Difflektüre ersetzt diesen Kontext nicht.

## Verbindungen

- [[AGENTS-md-Onboarding-Design]] passt zur kurzen allgemeinen Projektdatei und ausgelagerten bereichsspezifischen Review-Regeln.
- [[CI-Agent-mit-Review-Gate]] verbindet automatische Prüfung mit verpflichtenden menschlichen Entscheidungen und expliziten Merge-Grenzen.
