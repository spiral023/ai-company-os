# Helper-Nutzung-durch-Lint-erzwingen

**Konfidenz:** meinung

## Zweck

Wiederkehrende, statisch erkennbare Agentfehler durch einen verständlichen Implementierungsweg und konkrete Check-Meldungen vermeiden.

## Funktionsweise

Korrekturen, Fixes und Reverts auf wiederholte Fehlermuster prüfen. Herkunft und aktuelle Verstöße benennen. Einen Helper oder Typ für das gewünschte Verhalten bereitstellen. Im vorhandenen Linter den alten Pfad beanstanden und in der Fehlermeldung den Ersatz nennen; vorhandene Verbotsregeln bevorzugen. Aufrufer umstellen, Lint und Verhaltenstests ausführen. Für verbindliche Blockierung muss der Check in den Arbeits- oder Integrationsablauf eingebunden sein.

## Vorteile

- Fehlermeldung erklärt unmittelbar, wie der Agent korrigieren soll.
- Gemeinsames Verhalten wie Tokenbehandlung, Retries und Fehlerformate bleibt an einer Stelle.

## Nachteile & Grenzen

- Statische Regeln erfassen nur definierte Muster; semantische Fehler benötigen weitere Tests.
- Ausnahmen und Kompatibilität des Helpers müssen geprüft werden.
- Lint wirkt nur, wenn es ausgeführt und sein Ergebnis beachtet wird; es begrenzt keine Zugriffsrechte.

## Wann einsetzen, wann nicht

- Einsetzen: belegte Wiederholungsfehler mit gut erkennbarer Syntax und stabilem Ersatz.
- Nicht einsetzen: als pauschale Forderung nach mehr Abstraktionen oder für reine Ermessensfragen.

## Belege

- 2026-10-04 · [[2026-10-04-voxyz_ai-2106829206134931539]] · meinung — Vox bietet einen API-Helper und Lint-Meldungen mit benanntem Ersatz an; die illustrierten zentralen Tokens, Retries und Fehlerformate sind kein ausgeführter Fix oder Wirkungsnachweis.
- 2026-09-14 · [[2026-09-14-shadcn-2099534231114314145]] · meinung — `shadcn/no-restyle` beanstandet Vertragsbrüche in Tailwind-Klassen und nennt gültige Größenvarianten sowie die Komponentendatei aus dem vorhandenen Designsystem; ergänzt kontextabhängige Ersatzwege, setzt aber einen verbindlichen Lintlauf voraus und garantiert keine gesamte App-Qualität.
- 2026-10-08 · [[2026-10-08-moritz-brandes-sauberer-code-mit-claude-code-so-geht-s-wirklich]] · meinung — Brandes empfiehlt, wiederkehrende frameworkbezogene Agentfehler in projektspezifische statische Regeln zu übersetzen und Codeerzeugung, Prüfung und Korrektur zu einer Schleife zu verbinden. Die behauptete Wirkung ist Projekterfahrung; vorhandene Regeln müssen tatsächlich ausgeführt und relevante Verstöße im Arbeitsablauf behandelt werden.

## Spannungen & offene Fragen

- 2026-10-10: [[2026-09-14-shadcn-2099534231114314145]] nennt im Thread `{{variants}}`, während ein Screenshot `{{sizes}}` zeigt. Die genaue Platzhalterunterstützung bleibt ohne Prüfung der Implementierung offen; die zwei Namen werden nicht als belegte Aliasse behandelt. Die Hersteller-Evals messen Regelkorrekturen, nicht die Qualität der gesamten Anwendung.

- 50 Commits und höchstens drei Muster sind Budgets des Quellenprompts, keine empirisch optimalen Größen.
- Der Deletion Test kann zeigen, dass ein neuer Wrapper mehr Komplexität erzeugt als er bündelt.

## Verwandte Patterns

- [[Testharness-als-staerkster-Hebel]]
- [[Fachregel-Konsolidierung-vor-Featureaenderung]]
- [[Abstraktionswert-mit-Deletion-Test-pruefen]]
