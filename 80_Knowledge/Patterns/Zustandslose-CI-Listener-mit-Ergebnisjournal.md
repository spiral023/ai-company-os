# Zustandslose CI-Listener mit Ergebnisjournal

**Konfidenz:** meinung

## Zweck

CI-Ergebnisse auch bei wachsender Last zeitnah aufnehmen, damit eine deterministische Testauswahl auf einer ausreichend aktuellen Ergebnisgeschichte beruht.

## Funktionsweise

Ergebnisannahme und Historienbildung trennen. Zustandslose Listener hängen CI-Ergebnisse an ein externes In-Memory-Journal an, statt die gesamte Testhistorie selbst im Prozess zu halten. Ein separater Consumer verdichtet das Journal regelmäßig zu Historien je Test; ein Selector liest diese Grundlage für die Testauswahl.

Anzahl eingehender und verarbeiteter Ergebnisse, Lag, Backlog und Speicherbedarf instrumentieren. Weitere Listener können die Ergebnisannahme skalieren; die Reihenfolge und Korrektheit der Historienbildung bleiben ein eigener Prüfpunkt. Das Journal beseitigt diese Anforderungen nicht.

Anthropics vorheriges Package-Sharding lockerte die Single-Writer-Grenze pro Package, hielt den Zustand aber im Listener-Prozess. Der Journal-Umbau entkoppelte den nächsten Schritt. Das ist ein historischer Architekturbericht, kein universeller Wechselzwang für kleinere CI-Systeme.

## Vorteile

- Ergebnisannahme und Historienbildung lassen sich getrennt betreiben und beobachten.
- Zusätzliche Listener müssen nicht jeweils die vollständige Historie halten.
- Veraltete Selektionsdaten werden als eigener Fehlerzustand sichtbar.

## Nachteile & Grenzen

- Mehr Komponenten und ein externes System erhöhen Betriebsaufwand; der Autor berichtet höhere Infrastrukturkosten.
- Persistenz, Replay, Retry, Duplikate und Atomizität werden im Artikel nicht vollständig spezifiziert.
- Ein In-Memory-Journal garantiert allein weder verlustfreie Verarbeitung noch Exactly-once.
- Historische Wachstumszahlen sind keine allgemeine 25-fache Lastprognose. Der Umbau wurde hier nicht selbst ausgeführt oder anhand von Rohmessdaten überprüft.

## Wann einsetzen, wann nicht

- Einsetzen: wenn ein zustandsbehafteter Ergebnis-Listener unter CI-Last zurückfällt und die Auswahl neuer, reparierter oder störender Tests dadurch veraltet.
- Nicht einsetzen: als pauschale Architektur für kleine Projekte oder als Ersatz für fachlich richtige Tests und überprüfte Selektionsregeln.

## Belege

- 2026-09-14 · [[2026-09-14-claude-agentic-coding-is-straining-ci-here-s-how-we-sca]] · meinung — Sachin Malhotra beschreibt zustandslose Listener, externes In-Memory-Journal und separate Historienverdichtung; anschließende Stabilität und höhere Kosten sind selbstberichtet, Zustell- und Korrektheitsgarantien ungeprüft.

## Spannungen & offene Fragen

- 2026-10-10: Ein leistungsfähiger [[Testharness-als-staerkster-Hebel]] reicht nicht, wenn die tatsächlich ausgewählten Tests auf veralteter Historie beruhen. Aktualität ergänzt die Qualität des Verifiers.
- 2026-10-10: Welche Reihenfolge gilt bei parallelen, verspäteten oder wiederholten Ergebnissen? Die Quelle legt keine vollständige Konsistenz- und Wiederherstellungsregel vor.
- 2026-10-10: Wie viel Lastwachstum rechtfertigt die höheren Kosten? Die Quelle berichtet einen großen Unternehmenskontext, keinen übertragbaren Schwellenwert.

## Verwandte Patterns

- [[Testharness-als-staerkster-Hebel]]
- [[Quellen-Bookmarks-fuer-Agent-Automationen]]
- [[Abstraktionswert-mit-Deletion-Test-pruefen]]
