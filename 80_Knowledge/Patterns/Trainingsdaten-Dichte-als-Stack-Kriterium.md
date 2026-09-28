# Trainingsdaten-Dichte-als-Stack-Kriterium

**Konfidenz:** meinung

## Zweck

Verhindert, dass Technologie-/Versionswahl allein nach technischer Eignung oder Aktualität getroffen wird, ohne zu berücksichtigen, wie zuverlässig ein Coding Agent mit der jeweiligen Bibliothek tatsächlich umgehen kann. Adressiert eine stille Fehlerquelle: Bleeding-Edge-Stacks liefern nicht per se schlechteren Code, aber das Modell kennt sie schlechter.

## Funktionsweise

Bei der Wahl von Framework, Bibliothek oder Version wird neben technischer Eignung eine zusätzliche Achse berücksichtigt: Wie dicht ist diese Technologie in den Trainingsdaten des eingesetzten Modells vertreten? Populäre, etwas ältere und stabile Stacks (z. B. React, FastAPI, Python) erzeugen laut dieser Heuristik zuverlässigere Agent-Ausgaben als Bleeding-Edge-Versionen oder Nischen-Frameworks, weil das Modell auf massenhaft vorhandenem, gut repräsentiertem Code trainiert wurde und dort weniger halluziniert oder veraltete/falsche APIs mischt. Die Begründung ist eine Trainingsdaten-Erklärung, keine Messung: Es gibt (noch) keine Zahl dazu, wie stark die Fehlerrate mit sinkender Trainingsdaten-Dichte tatsächlich steigt.

## Vorteile

- Macht eine bisher meist implizite Intuition explizit und damit bei Technologieentscheidungen bewusst gegen Aktualität abwägbar.
- Reduziert einen stillen Fehlermodus: Ein Agent, der mit einer schlecht repräsentierten Bibliothek arbeitet, produziert oft plausibel aussehenden, aber subtil falschen Code (veraltete API-Nutzung, Vermischung von Versionen), ohne dass das sofort auffällt.
- Einfach anzuwenden, ohne zusätzliche Tooling- oder Prozessänderung — wirkt bereits bei der Stack-Entscheidung selbst.

## Nachteile & Grenzen

- Unbelegte Einzelmeinung ohne Messung; „Trainingsdaten-Dichte“ lässt sich von außen nicht direkt prüfen, nur indirekt an Popularität/Alter einer Technologie schätzen.
- Steht in Grundspannung zur eigentlich gewünschten technischen Eignung — die zuverlässigste Wahl für den Agenten ist nicht automatisch die fachlich beste Wahl für das Projekt.
- Veraltet mit jedem neuen Modell-Trainingslauf: Was heute schlecht repräsentiert ist, kann in einem späteren Modell bereits gut abgedeckt sein.

## Wann einsetzen, wann nicht

- Einsetzen: bei echter Wahlfreiheit zwischen mehreren technisch gleichwertigen Optionen, insbesondere bei stark agentisch getriebener Entwicklung mit wenig menschlichem Gegenlesen.
- Nicht einsetzen: wenn eine Bleeding-Edge-Technologie fachlich klar erforderlich ist (z. B. eine neue Sprachfunktion, ein Pflicht-Compliance-Framework) — dort überwiegt die technische Notwendigkeit, und die Mehrarbeit durch geringere Modellzuverlässigkeit muss anders kompensiert werden (mehr Tests, mehr Review).

## Belege

- 2026-01-12 · [[2026-01-12-dhruv1103-lessons-learned-500k-lines-claude-code]] · meinung — Reddit-Erfahrungsbericht (über vibedeck-Sekundärfassung) empfiehlt populäre, etwas ältere Stacks statt Bleeding-Edge-Versionen mit der Begründung, Modelle machten bei trainingsdaten-dichtem Code deutlich weniger Fehler — unbelegt, einzelquellig.
- 2026-02-13 · [[2026-02-13-vincanger-claude-code-fullstack-essentials]] · meinung — Argumentiert für meinungsstarke Frameworks (Wasp, Next.js, Laravel, Rails), weil klare Ablageorte und weniger Boilerplate das Raten reduzieren; Zahl 97 % weniger Code ist Herstellerbeispiel (Wasp-Team) und ungeprüft.

## Spannungen & offene Fragen

- Einzige bisherige Quelle, selbst unbelegt und aus zweiter Hand (vibedeck-Aufarbeitung, keine geprüfte Primärquelle) — keine unabhängige Zweitbestätigung, keine Zahl zur tatsächlichen Fehlerratendifferenz.

## Verwandte Patterns

- [[Action-Space-Design-nach-Modellfaehigkeit]]
- [[Erweiterungs-Ebenen-Zuordnung]]
