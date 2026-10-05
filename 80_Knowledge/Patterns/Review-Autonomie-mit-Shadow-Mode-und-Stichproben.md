# Review-Autonomie mit Shadow Mode und Stichproben

**Konfidenz:** meinung

## Zweck

Menschliche Review-Kapazität gezielt einsetzen, wenn Agent-Output schneller wächst als die Prüfmöglichkeiten. Automatische Freigaben bleiben an Risikobereiche, Beobachtung und menschliche Verantwortung gebunden.

## Funktionsweise

Codebereiche nach Risiko einstufen und festlegen, wo menschliche Freigabe verpflichtend bleibt. Neue Review-Agents zunächst im Shadow Mode einsetzen: Sie liefern Befunde zur menschlichen Prüfung und werden mit absichtlich problematischen Änderungen geprüft. Erst nach Bewertung ihrer Ergebnisse automatische Entscheidungen für ausgewählte Bereiche zulassen; jeder Entscheid protokolliert die verwendeten Signale und Begründungen.

Risikogewichtete menschliche Stichproben prüfen automatische Freigaben weiter. Spezialisierte Agents mit getrennten Kontexten, deterministische Scans und Tests wichtiger Invarianten ergänzen einander. Menschen überwachen Befunde, Fehlentscheidungen und die Review-Schleife selbst. Die Quelle nennt keine feste Stichprobenquote oder messbare Freigabeschwelle.

## Vorteile

- Prüfarbeit lässt sich auf kritische Änderungen und die Qualität der Automatik konzentrieren.
- Shadow Mode erlaubt eine Bewertung, bevor ein neuer Reviewer autonom freigibt.
- Protokolle und Stichproben machen automatische Entscheidungen nachträglich prüfbar.

## Nachteile & Grenzen

- Risikoklassifikation und Stichprobenauswahl können Fehler übersehen.
- Getrennte Kontexte verhindern keine gemeinsamen Modellschwächen.
- Scan-Kosten, menschliche Stichproben und Regelpflege wachsen mit dem Durchsatz.
- Der Herstellerbericht misst die Wirkung dieses Gesamtmodells nicht unabhängig.

## Wann einsetzen, wann nicht

- Einsetzen: bei wachsendem Review-Volumen mit klar abgrenzbaren Risikobereichen und verfügbarer menschlicher Kontrollkapazität.
- Nicht einsetzen: automatische Freigaben ohne nachvollziehbare Befunde, Risikoeinstufung und laufende Kontrolle; die Quelle rechtfertigt keinen pauschalen Ersatz menschlicher Freigaben.

## Belege

- 2026-07-21 · [[2026-07-21-claude-how-anthropic-secures-its-ai-native-software-dev]] · meinung — Anthropic beschreibt Shadow Mode für neue Reviewer, risikobasierte Automatisierung, menschliche Stichproben und protokollierte Freigaben. Herstellerbericht ohne veröffentlichte Stichprobenquoten oder Freigabeschwellen.

## Spannungen & offene Fragen

- Spannung (2026-10-05): [[CI-Agent-mit-Review-Gate]] und [[2026-09-27-anthropic-academy-sdlc-playbook]] halten menschliche Freigaben im bestehenden Review-Prozess fest; diese Quelle erlaubt automatische Freigaben in ausgewählten Bereichen. Die Unterschiede nach Zeitpunkt und Codebereich sind nicht abschließend erklärt.
- Offen: Welche Fehlentscheidungsrate, Nachweise und Stichprobenquote reichen für einen konkret abgegrenzten Automatisierungsbereich?

## Verwandte Patterns

- [[CI-Agent-mit-Review-Gate]]
- [[Plan-first-mit-getrenntem-Review]]
- [[Testharness-als-staerkster-Hebel]]
- [[Metrikband-gestufte-Agent-Autonomie]]
