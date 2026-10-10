# Mobile-Webapp-nach-Eingabefaehigkeit-pruefen

**Konfidenz:** verifiziert

## Zweck

Beim mobilen UI-Design Bedienprobleme einer Webapp anhand von Eingabefähigkeit, Viewportverhalten und Zielhardware untersuchen. Responsive Layouts und tatsächliches Touch-Verhalten werden dabei gemeinsam geprüft.

## Funktionsweise

Ein reproduzierbares Symptom auswählen: festhängendes Hover, verdeckter Button, Eingabezoom oder blockiertes Scrollen. Hover-Stile nach Eingabefähigkeit begrenzen, Viewporteinheiten nach Layoutzweck wählen und sichere Ränder an betroffenen Bedienelementen berücksichtigen. Zoom, Auswahl von Textinhalten und normale Scrollgesten erhalten. Änderungen einzeln vergleichen und die vollständige betroffene Interaktion auf einem Zielgerät wiederholen.

## Vorteile

- Konkrete Symptome führen zu eng begrenzten Korrekturen.
- Geräte mit verschiedenen Eingabemechanismen werden berücksichtigt.
- Eine Hardwareprüfung erfasst zusätzlich Browserleisten, Tastatur und echte Touch-Interaktionen.

## Nachteile & Grenzen

- Viewporteinheiten lösen nicht jedes Tastaturproblem; Browserunterstützung und App-Layout bestimmen das Verhalten.
- Globale Änderungen an Gesten oder Textauswahl können die Bedienung verschlechtern.
- Die Repo-Verifikation bestätigt den dokumentierten Ablauf, keine gemessene Wirkung und keinen eigenen Hardwaretest.

## Wann einsetzen, wann nicht

- Einsetzen: Webapps mit mobilen Formularen, festen Bedienelementen oder Gestenflächen.
- Nicht einsetzen: als pauschale Umwandlung zur Native-App oder Ersatz für Funktions- und Barrierefreiheitsprüfungen.

## Belege

- 2026-10-09 · [[2026-10-09-repo-emilkowalski-mobile-native]] · verifiziert — Read-only-Abgleich des mobile-native-Skills an Checkout e8a175de mit dokumentierten Eingabe-, Viewport- und Hardwareprüfungen; ergänzende MDN-/WebKit-Prüfung begrenzt pauschale Browseraussagen.
- 2026-09-14 · [[2026-09-14-voxyz_ai-2099528601557496220]] · meinung — Relevante Desktop- und Mobile-Zustände einschließlich verdeckter Buttons, Formularbedienung, Laden, Fehlern und Speicherfeedback prüfen; konkrete Zielgeräte und Touch-/Viewportmessungen fehlen.

## Spannungen & offene Fragen

- Der Skill enthält eine globale Baseline; welche Regeln sinnvoll sind, hängt von den konkreten Symptomen und den Zielbrowsern ab.
- Ein kleiner Desktop-Viewport ist eine Layoutprüfung, aber kein vollständiger Nachweis des mobilen Bedienverhaltens.

## Verwandte Patterns

- [[UI-Grenzfaelle-mit-realistischen-Daten-pruefen]]
- [[Visuelle-Abnahme-mit-Live-Lokal-Vergleich]]
