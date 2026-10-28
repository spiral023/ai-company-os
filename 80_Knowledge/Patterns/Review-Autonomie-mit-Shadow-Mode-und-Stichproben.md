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
- 2026-10-02 · [[2026-10-02-matt-pocock-live-poteto-creator-of-pstack-on-shipping-1-000]] · meinung — Tan berichtet nachträgliche Stichproben bei automatischen Merges und überführt wiederkehrende Fehler in Skills, Lint-Regeln und Codekonventionen. Ein vorausgehender Shadow-Mode wird nicht beschrieben; für irreversible oder schwer überprüfbare Änderungen bleibt die Freigabefrage offen.
- 2026-08-07 · [[2026-08-07-claude-auto-mode-is-now-the-default-in-claude-code-for]] · meinung — Anthropic meldet in einer kontrollierten Studie mit 1.053 Testpersonen 13,6 % menschlich blockierte gefährliche Prompts gegenüber 89 % im Auto-Mode; menschliche Erkennung nahm mit der Prompt-Anzahl ab. Das unterstützt eine Prüfung von Freigabemüdigkeit, belegt aber weder allgemeine Sicherheit noch Gleichwertigkeit zu aufmerksamem risikogewichtetem Review.
- 2026-10-10 · [[2026-10-10-satyanadella-2108931348857827686]] · meinung — Kein Modell soll zugleich seine Arbeit und sämtliche Belege zur eigenen Prüfung kontrollieren; auch Angriffe, Fehler und Randfälle gehören in laufende Systemtests. Mehrere Modelle liefern laut Autor erst mit unabhängiger Beweisführung und Kontrollzuständigkeit mehr als verschachtelte Blackboxes.
- 2026-10-15 · [[2026-10-15-claude-how-the-claude-code-team-does-code-review-claude]] · meinung — Claude-Code-Team beschreibt Risikostufen je Änderung, sensible Pflichtpfade, vertrauenswürdige Autoren und commitgebundene Freigaben; Hersteller-Selbstbericht, interne Freigabeautomatisierung übersteigt das öffentliche Befundprodukt und automatische Circuit Breaker fehlen noch.
- 2026-10-16 · [[2026-10-16-math_rachel-2111238648188584306]] · meinung — Thomas diskutiert Voraburteile, begrenzte autonome Einheiten, gebündelte Reviews und Aufgaben mit bekannten Antworten als Unterstützung menschlicher Aufsicht. Die sichtbaren Papierauszüge sind kein hier replizierter Nachweis; Zustimmung und Widerspruch sind ohne Kontext keine Qualitätsmetriken.
- 2026-07-20 · [[2026-07-20-matt-pocock-do-you-even-need-human-review]] · meinung — Kontrollpunkte variieren nach Umfang und Art der Änderung; der Beitrag nennt Fälle ohne spätes menschliches Review, liefert aber keine Validierung einer sicheren Produktionsfreigabe.
- 2026-10-22 · [[2026-10-22-voxyz_ai-2113314439294570515]] · meinung — Vox trennt fünf gewichtete PR-Risikokriterien von menschlichen Freigaberegeln und schlägt eine lesende Kalibrierung an zehn PRs vor; sensible Pfade und CI-Konfiguration bleiben menschlich zu prüfen, die berichtete Revert-Verbesserung ist kein kausaler Wirksamkeitsnachweis.
- 2026-10-22 · [[2026-10-22-itamar_mar-2113255396299128887]] · meinung — Der Einstieg erfolgt mit einer begrenzten Arbeitsklasse unter menschlicher Aufsicht; Interventionen zeigen fehlenden Kontext, unzureichende Checks oder zu weite Grenzen. Verantwortung wächst mit beobachtetem Verhalten; der Artikel nennt jedoch keine gemessenen Erfolgsquoten oder Freigabeschwellen.
- 2026-10-25 · [[2026-10-25-mattpocockuk-2114311664069718370]] · meinung — Pocock erwägt deterministischen Automerge ausschließlich für Codeumordnung bei unverändertem Modulgraphen und nicht verschlechterter Testabdeckung; Features sind ausgeschlossen. Im zweiten Threadpost nennt er zusätzliche Grenzen und hält die Idee schließlich selbst für wahrscheinlich nicht umsetzbar; es handelt sich um keine verfügbare oder validierte Freigabetechnik.
- 2026-10-26 · [[2026-10-26-addyosmani-2114604912520921136]] · meinung — Zweitfassung derselben Herkunft zeigt null, eine oder zwei menschliche Pflichtfreigaben nach Risiko; Trusted-Author-Grenzen, sensible Pfade und commitgebundene Freigaben bleiben eigene Bedingungen, keine universelle Freigabeschwelle.

## Spannungen & offene Fragen

- Ergänzung 2026-10-17: [[2026-10-15-claude-how-the-claude-code-team-does-code-review-claude]] unterscheidet das öffentliche Produkt mit Reviewbefunden von internen risikogestützten Freigaben. Die dort beschriebene Praxis enthält laut Bericht keine automatischen Circuit Breaker; sie ist deshalb kein Beleg, dass unbeaufsichtigte Freigaben generell abgesichert wären. Mehr Änderungen bei geringerer Revertquote sind Hersteller-Selbstbericht ohne Kausalnachweis. Die offenen Prüf- und Rollbackgrenzen bleiben neben dem Shadow-Mode-Vorschlag erhalten.
- 2026-10-11: [[2026-08-07-claude-auto-mode-is-now-the-default-in-claude-code-for]] meldet höhere Erkennung gefährlicher Aktionen durch Auto-Mode als bei manuellen Bestätigungen. Die Vergleichsbedingungen betreffen auch Freigabemüdigkeit; sie widerlegen weder risikogewichtete menschliche Prüfung noch belegen sie allgemeine Sicherheit durch null beobachtete Angriffe.

- Spannung (2026-10-05): [[CI-Agent-mit-Review-Gate]] und [[2026-09-27-anthropic-academy-sdlc-playbook]] halten menschliche Freigaben im bestehenden Review-Prozess fest; diese Quelle erlaubt automatische Freigaben in ausgewählten Bereichen. Die Unterschiede nach Zeitpunkt und Codebereich sind nicht abschließend erklärt.
- Offen: Welche Fehlentscheidungsrate, Nachweise und Stichprobenquote reichen für einen konkret abgegrenzten Automatisierungsbereich?

- 2026-10-22: [[2026-07-20-matt-pocock-do-you-even-need-human-review]] hält für bestimmte interne Arbeiten nur frühe menschliche Abstimmung für ausreichend. Das ist eine Prozessheuristik ohne validierte Freigabeschwelle; tatsächliche Tragweite und bestehende Produktionsfreigaben bleiben eigenständige Bedingungen.

- 2026-10-25 · [[2026-10-25-mattpocockuk-2114311664069718370]]: Pocock bezweifelt seinen eigenen Vorschlag im zweiten Threadpost bis zur Vermutung, dass er wahrscheinlich nicht möglich sei. Eine Ideenskizze zu unverändertem Modulgraphen, Coverage oder Bundle-Output ist weder ein vorhandenes Automerge-Tool noch eine validierte Freigabegrenze.

## Verwandte Patterns

- [[CI-Agent-mit-Review-Gate]]
- [[Plan-first-mit-getrenntem-Review]]
- [[Testharness-als-staerkster-Hebel]]
- [[Metrikband-gestufte-Agent-Autonomie]]
