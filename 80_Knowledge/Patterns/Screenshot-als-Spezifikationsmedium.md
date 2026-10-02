# Screenshot-als-Spezifikationsmedium

**Konfidenz:** meinung

## Zweck

Ersetzt eine mehrstufige verbale Beschreibung eines visuellen Ist- oder Soll-Zustands durch das Bild selbst. Adressiert, dass UI-Fehler, Design-Mockups oder Rendering-Probleme sich oft schlechter in Prosa fassen lassen als sie sich zeigen lassen.

## Funktionsweise

Ein Bild (Screenshot, Mockup, Fehlerdarstellung) wird per Drag & Drop, Copy & Paste oder Dateipfad direkt in den Kontext eingebunden, statt seinen Inhalt verbal zu beschreiben. Das Modell nutzt das Bild auf drei Arten: **Analyse** (UI-Elemente eines Screenshots beschreiben), **Fehlerdiagnose** (aus einem Fehler-Screenshot die wahrscheinliche Ursache ableiten) und **Code-Generierung** (aus einem Design-Mockup passendes CSS/Markup ableiten). Der Kanal selbst trägt Informationen, die in Textform aufwendig zu reproduzieren wären — Layout, Abstände, Farben, exakte Fehlermeldungen im Screenshot.

## Vorteile

- Erspart die verlustbehaftete Übersetzung eines visuellen Zustands in Prosa.
- Design-zu-Code-Generierung wird direkt möglich, ohne dass jemand das Mockup erst in Maße und Werte übersetzt.
- Fehlerdiagnose aus einem Screenshot kann Kontext liefern, der im reinen Fehlertext fehlt (z. B. Layout-Kontext eines visuellen Bugs).

## Nachteile & Grenzen

- Ein Bild belegt sofort erhebliches Kontext-Budget, anders als ein kurzer Textsatz.
- Nur so präzise wie Bildqualität und Auflösung — unscharfe oder zu klein zugeschnittene Screenshots verschenken den Vorteil.
- Ersetzt keine Verifikation: Ein Screenshot zeigt den Ist-Zustand, aber nicht, ob eine daraus abgeleitete Änderung tatsächlich korrekt ist. Bereits als Grenze bekannt: Ein Modell schließt CSS-/Rendering-Fixes rein logisch aus dem Code, nicht aus dem tatsächlich gerenderten Ergebnis — visuelle Änderungen müssen von einem Menschen (oder einem Screenshot-Diff) gegengeprüft werden.

## Wann einsetzen, wann nicht

- Einsetzen: UI-Bugs, Design-zu-Code-Übersetzung, jede Aufgabe, bei der der Ist- oder Soll-Zustand primär visuell ist.
- Nicht einsetzen: Aufgaben mit rein textuellem oder strukturellem Kontext, bei denen ein Bild nur zusätzliches Kontext-Budget ohne Mehrwert kosten würde.

## Belege

- 2026-02-01 · [[2026-02-01-anthropic-docs-claude-code-common-workflows]] · meinung — Anthropics Common-Workflows-Doku beschreibt Screenshot-Einbindung (Drag & Drop, Paste, Pfad) für UI-Analyse, Fehlerdiagnose und Design-zu-Code-Generierung als eigenständige Technik. Beleglage dünn: reine Feature-Aufzählung ohne Tiefe, kein Vorher-Nachher-Vergleich.
- 2026-02-15 · [[2026-02-15-avid-ai-design-workflow-2026]] · meinung — Referenz-Screenshots und Video-zu-Code (Kimi K2.5) als Spezifikation für Design; Design-Vokabular macht Prompts präzise. Sekundärquelle.
- 2026-09-19 · [[2026-09-19-voxyz_ai-2101295246659182978]] · meinung — Variante, bei der der Agent das Referenzbild per Bildmodell selbst erzeugt und dann umsetzt; keine Vergleichsmessung, Modellaussage nur Behauptung.
- 2026-10-01 · [[2026-10-01-julian-ivanov-ki-automat-claude-code-ist-unglaublich-gut-in-motion-graphi]] · meinung — Claude prüft die selbst gerenderten Frames per Screenshot. Nur beiläufig erwähnt, schwacher Beleg.

## Spannungen & offene Fragen

- Einzige bisherige Quelle, dort nur als knappe Feature-Liste ohne Vertiefung — eine zweite, unabhängige Quelle würde die Aussage stärken.
- Verwandte, bereits belegte Grenze: [[Testharness-als-staerkster-Hebel]] hält fest, dass ein Modell CSS-/Rendering-Fixes rein aus dem Code ableitet, ohne das tatsächliche Rendering zu sehen — dieses Pattern sollte deshalb nie ohne begleitende visuelle Verifikation (Vorher-Nachher-Screenshot) eingesetzt werden, sonst wird die Eingabe visuell, die Prüfung aber nicht.

## Verwandte Patterns

- [[Testharness-als-staerkster-Hebel]]
- [[Freiheitsgrad-nach-Aufgaben-Fragilitaet]]
