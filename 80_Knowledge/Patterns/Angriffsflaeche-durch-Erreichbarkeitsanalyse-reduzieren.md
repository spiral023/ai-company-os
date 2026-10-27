# Angriffsflaeche-durch-Erreichbarkeitsanalyse-reduzieren

**Konfidenz:** meinung

## Zweck

Unnötig exponierte Funktionalität hinter geeignete Authentifizierungs-, Konfigurations- oder Protokollgrenzen verschieben. Das begrenzt die Erreichbarkeit möglicherweise verwundbaren Codes, ohne zuerst jede einzelne Schwachstelle finden zu müssen.

## Funktionsweise

Zuerst die beabsichtigte Exposition und die tatsächlichen Einstiegspunkte inventarisieren: Welche Funktionen sollen öffentlich, erst nach Authentifizierung oder ausschließlich intern erreichbar sein? Anthropics Herstellerbericht vom 20.10.2026 beschreibt anschließend drei getrennte Analysen mit jeweils frischem Kontext und einer kurzen Übergabe:

1. Code suchen, den die Default-Konfiguration erreichbar macht, obwohl keine beabsichtigte Funktion ihn benötigt.
2. Verarbeitung vor Authentifizierung, Konfigurationsprüfungen oder geeigneten Eintrittspunkten der Protokoll-Zustandsmaschine untersuchen.
3. Konfigurationskombinationen ermitteln, die Sicherheitskontrollen unbemerkt abschalten oder schwächen.

Positive Befunde mit dynamischen Traces nachvollziehen. Ein Gate muss am tatsächlich verarbeiteten Payload greifen; die Prüfung eines angekündigten Algorithmus allein kann verschachtelte Parser- oder CA-Signaturpfade übersehen. Änderungen an unnötiger Default-Erreichbarkeit gegen eine unveränderte Baseline prüfen: Projekt-Tests und Black-Box-Regressionen sollen identische Ergebnisse liefern. Ändert sich das Verhalten anderer Konfigurationen, gehört diese Abweichung in eine gesonderte menschliche Entscheidung. Andere Befundklassen können eine frühere Prüfung, ein Zustands-Gate oder das Ablehnen einer Konfigurationskombination erfordern.

## Vorteile

- Richtet die Analyse auf unnötige Exposition auch bei unbekannten Schwachstellen.
- Verbindet statische Kandidatensuche mit beobachtbaren Ausführungspfaden und einem konkreten Prüfvertrag für die Änderung.
- Trennt Verhaltenserhalt im geprüften Default-Fall von bewusst veränderten Konfigurationen.

## Nachteile & Grenzen

- Instrumentierung, repräsentative Eingaben und Black-Box-Regressionen brauchen Aufwand und Fachkenntnis.
- Der Herstellerbericht zählt 493 Befunde in 25 Projekten; das sind keine 493 nachgewiesenen Exploits und keine eigene Reproduktion.
- Fehlende Traces beweisen keine Unerreichbarkeit. Identische Testergebnisse belegen nur den geprüften Verhaltensumfang.

## Wann einsetzen, wann nicht

- Einsetzen: bei Netzwerkdiensten, Parsern und anderen Programmen, deren erreichbare Funktionen von Authentifizierung, Zuständen oder Konfiguration abhängen.
- Nicht einsetzen: als Ersatz für Isolation, eine vollständige Sicherheitsprüfung oder eine Freigabe von Security-Änderungen. Die Analyse bereitet solche Entscheidungen vor.

## Belege

- 2026-10-20 · [[2026-10-20-anthropic-using-claude-to-reduce-the-attack-surface-of-cod]] · meinung — Anthropic berichtet drei getrennte Analysen zur Default-Erreichbarkeit, Verarbeitung vor Sicherheitsgrenzen und problematischen Konfigurationskombinationen mit dynamischen Befund-Traces und Baseline-Regressionstests; OpenSSH dient als konkreter Hersteller-Fallbericht ohne eigene Reproduktion.

## Spannungen & offene Fragen

- 2026-10-20 · [[2026-10-20-anthropic-using-claude-to-reduce-the-attack-surface-of-cod]]: Weniger beobachtete Erreichbarkeit ist kein Beweis vollständiger Unerreichbarkeit; die Reichweite einer Aussage hängt von Instrumentierung, Eingaben und Konfigurationen ab. Ein Gate kann legitimes Verhalten beschneiden, das die vorhandenen Tests nicht abdecken.
- Die OpenSSH-Zahlen betreffen verschiedene Stände: rund 4.500 Zeilen beziehungsweise 16 Prozent bei Version 10.4 und ungefähr ein Fünftel weniger erreichbarer Code nach der Korrektur in 10.6 sind keine identischen Messungen.

## Verwandte Patterns

- [[Codepfad-vor-Aenderung-nachvollziehen]]
- [[Refactoring-mit-Verhaltensvergleich]]
- [[Sandbox-Komposition-aus-OS-Primitiven]]
