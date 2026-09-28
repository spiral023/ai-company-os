# Metrikband-gestufte-Agent-Autonomie

**Konfidenz:** meinung

## Zweck

Ein Agent reagiert auf Abweichungen einer Produktionsmetrik nur so weit, wie die Schwere der Abweichung es rechtfertigt, und speist seine Erkenntnisse zurück in den Entwicklungsprozess. Das begrenzt den Schaden durch Fehlalarme und verhindert, dass ein Agent bei jeder Schwankung eigenmächtig eingreift.

## Funktionsweise

Ein deterministisches Skript ohne Modell berechnet für eine Metrik mit rollierender Baseline (z. B. 30 Tage) die Abweichung in Sigma. Versionierte Stufen legen fest, was der Agent bei welcher Abweichung darf: bei 1σ wird nur geloggt, bei 2σ arbeitet der Agent read-only zur Diagnose, bei 3σ darf er nur einen Pull Request öffnen oder ein vorab genehmigtes Runbook auslösen. Der Agent schreibt seine Diagnose als `intent.md`, ein Service-Owner triagiert (beheben, planen, verwerfen), und nach dem Fix wird ein Eval als Regressionstest ergänzt. Die Erkennung selbst braucht damit kein Modell und kostet keine Token.

## Vorteile

- Die Rechte des Agents wachsen mit der Schwere der Abweichung, nicht mit seiner Selbsteinschätzung.
- Erkennung und Schwellen sind deterministisch und versioniert, also nachvollziehbar und ohne Modellkosten.
- Jede Störung erzeugt ein Artefakt (Diagnose, Eval) und stärkt so den Entwicklungsprozess.

## Nachteile & Grenzen

- Setzt stabile Baselines und geprüfte Runbooks voraus.
- Die Quelle liefert weder Schwellenwerte aus der Praxis noch Ergebnisse; die Sigma-Stufen sind eine Herstellerempfehlung.
- Fehlalarme kosten Triage-Zeit und Token.

## Wann einsetzen, wann nicht

- Einsetzen: Systeme mit gut messbaren Metriken (Fehlerrate, Latenz, Kosten pro Aufgabe) und vorhandenen, geprüften Runbooks.
- Nicht einsetzen: neue Systeme ohne belastbare Baseline oder Metriken, die stark saisonal schwanken, ohne dass die Baseline das abbildet.

## Belege

- 2026-09-27 · [[2026-09-27-anthropic-academy-sdlc-playbook]] · meinung — Lektion 13 beschreibt das Schema mit `bands.yaml` und Western-Electric-Regeln als Herstellerempfehlung ohne Praxisdaten.

## Spannungen & offene Fragen

- Keine bekannt. Offen ist, ob sich die Stufen aus der Praxis bestätigen lassen; die Quelle ist eine Anleitung, keine Auswertung.

## Verwandte Patterns

- [[CI-Agent-mit-Review-Gate]]
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[Spec-Ordner-pro-Feature]]
