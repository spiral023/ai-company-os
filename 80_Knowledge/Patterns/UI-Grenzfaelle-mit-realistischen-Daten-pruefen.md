# UI-Grenzfaelle-mit-realistischen-Daten-pruefen

**Konfidenz:** verifiziert

## Zweck

Oberflächen mit plausiblen Extremwerten prüfen, die gewöhnliche Demo-Daten nicht abdecken.

## Funktionsweise

Gerenderte Werte und ihre Verträge identifizieren. Realistische lange Namen, untrennbare E-Mail-Adressen, fehlende Felder, leere und große Listen, kurze Labels sowie verschiedene Schriftsysteme als Fixture bereitstellen. Demo- und Worst-case-Daten im gleichen Komponentenlayout vergleichbar machen, beispielsweise per Toggle. Jeden Rendering-Defekt mit auslösendem Wert dokumentieren, gezielt korrigieren und erneut rendern.

## Vorteile

- Reproduziert datenabhängige Layoutfehler mit konkreten Eingaben.
- Verbindet Fehlerbefund, Korrektur und erneut überprüfbaren Zustand.

## Nachteile & Grenzen

- Unrealistische Fantasiedaten können die Prüfung entwerten.
- Rendering-Abnahme deckt Datenfluss, Sicherheit und mobile Hardwareeigenschaften nicht vollständig ab.
- Die Verifikation bestätigt den beschriebenen Ablauf im Skill-Repo; ein eigener UI-Testlauf fand hier nicht statt.

## Wann einsetzen, wann nicht

- Einsetzen: Tabellen, Listen, Formulare, Profile und Komponenten mit variablen Inhaltsgrößen.
- Nicht einsetzen: als vollständige Release-Abnahme oder mit ungültigen Eingaben, die der reale Datenvertrag ausschließt.

## Belege

- 2026-10-04 · [[2026-10-04-emilkowalski-2106752670405099523]] · meinung — Kowalski kündigt /break-ui für lange Namen, ungewöhnliche E-Mail-Adressen und lange Listen mit anschließender Korrektur an; der Post liefert keinen Testlauf oder Abdeckungsnachweis.
- 2026-10-09 · external_repos/emilkowalski/skills/skills/break-ui/SKILL.md · verifiziert — Checkout e8a175d dokumentiert realistische Extremdaten-Fixtures, Demo-/Worst-case-Toggle sowie Befund und Fix je Rendering-Defekt; bestätigt den Skill-Ablauf, keine ausgeführte UI-Abnahme oder Wirksamkeit.

## Spannungen & offene Fragen

- Welche Extremwerte realistisch sind, hängt vom Produkt und seinen tatsächlichen Datenverträgen ab.
- Ein Toggle erleichtert die Untersuchung, ersetzt aber keine definierten Assertions für dauerhafte Regressionstests.

## Verwandte Patterns

- [[Adversarialer-Pre-Launch-Check]]
- [[Visuelle-Abnahme-mit-Live-Lokal-Vergleich]]
- [[Testharness-als-staerkster-Hebel]]
