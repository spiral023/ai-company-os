# Variantenvergleich vor Produktionsabnahme

**Konfidenz:** verifiziert

## Zweck

Eine gestalterische Richtung anhand bedienbarer Alternativen wählen, bevor sie in die Anwendung integriert und für den Einsatz geprüft wird.

## Funktionsweise

Den vorhandenen Produktkontext und seine Design-Tokens aufnehmen. Unterschiede auf benannten Achsen entwerfen, etwa Layout, Dichte, Interaktionsmodell oder Motion. Oberflächliche Farbvarianten erfüllen diesen Vergleich nicht.

Die Varianten auf einer isolierten Vorschau mit plausiblen Inhalten und funktionierenden Interaktionen anbieten. Im geprüften Prototype-Skill sind standardmäßig drei Varianten vorgesehen, bis zu fünf bei begründetem Bedarf. Jede Variante im Browser prüfen und Kosten sowie geeigneten Einsatz erklären.

Der Mensch wählt eine Richtung und iteriert deren Details. Erst die gewählte Variante integrieren. Emils historischer Workflow ergänzt anschließend Performance-, Accessibility- und Mobile-Prüfungen. Der Name des damaligen Produktions-Skills ist keine Voraussetzung für diese getrennte Abnahme.

## Vorteile

- Alternativen machen konkrete Gestaltungsentscheidungen und ihre Kosten vergleichbar.
- Isolierte Exploration begrenzt vorzeitige Eingriffe in die Anwendung.
- Funktionierende Varianten zeigen Verhalten, das ein statisches Mockup nicht vermittelt.

## Nachteile & Grenzen

- Mehr Varianten kosten Implementierungs- und Prüfzeit; ohne klare Unterschiede entsteht zusätzliche Auswahl ohne Erkenntnisgewinn.
- Menschliches Urteil und eine anschließende Abnahme bleiben erforderlich.
- Die Verifikation betrifft lokale Skill-Vorgaben, keinen gemessenen Qualitäts- oder Produktivitätsgewinn.
- `/prep-for-prod` aus dem Tweet vom 15.09.2026 fehlt im am 10.10.2026 geprüften Skillverzeichnis. Daraus folgt keine Widerlegung seiner damaligen Existenz.

## Wann einsetzen, wann nicht

- Einsetzen: wenn mehrere plausible Antworten auf eine konkrete UI- oder Motion-Frage bestehen und Verhalten für die Auswahl wichtig ist.
- Nicht einsetzen: für einen bekannten kleinen Defekt oder eine bereits verbindlich festgelegte Gestaltung.

## Belege

- 2026-09-15 · [[2026-09-15-emilkowalski-2099948779864793303]] · meinung — Emil beschreibt Variantenwahl, Iteration und anschließende Produktionsprüfung als persönlichen Workflow; kein eigener Erfolgstest oder gemessener Produktivitätsgewinn.
- 2026-10-10 · external_repos/emilkowalski/skills/skills/prototype/SKILL.md · verifiziert — Checkout `e8a175de22ae1e49370fc144c1f3bb9aeedf988d` verlangt unterschiedliche Gestaltungsachsen, echte Interaktionen, isolierte Vorschau, Browserprüfung und Integration erst nach Auswahl.
- 2026-10-10 · external_repos/emilkowalski/skills/skills/animate/SKILL.md · verifiziert — derselbe Checkout beschreibt Easing-/Timing-Entscheidungen und Reduced Motion; keine Animation wurde für diese Prüfung ausgeführt.

## Spannungen & offene Fragen

- 2026-10-10: Variantenexploration ergänzt [[Plan-first-mit-getrenntem-Review]], ersetzt aber keinen unabhängigen fachlichen Review.
- 2026-10-10: Wie viele Varianten sind im konkreten Fall sinnvoll? Drei ist die Vorgabe des geprüften Skills, keine universelle optimale Zahl.
- 2026-10-10: Eine überzeugende Vorschau belegt noch keine Persistenz, Regressionstauglichkeit oder Performance der integrierten Anwendung.

## Verwandte Patterns

- [[Plan-first-mit-getrenntem-Review]]
- [[Visuelle-Abnahme-mit-Live-Lokal-Vergleich]]
- [[UI-Grenzfaelle-mit-realistischen-Daten-pruefen]]
