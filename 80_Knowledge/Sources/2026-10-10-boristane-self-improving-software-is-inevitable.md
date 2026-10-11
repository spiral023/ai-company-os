---
url: https://boristane.com/blog/self-improving-software-is-inevitable/
autor: Boris Tane
datum: 2026-10-10
erfasst: 2026-10-11
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-10-10-boristane-self-improving-software-is-inevitable.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Produktionssignale als Rückkopplung für Coding Agents

Boris Tane beschreibt einen Entwicklungsprozess, in dem Agents Logs, Traces, Produktmetriken, Session Replays und Supporttickets gemeinsam untersuchen und Verbesserungen vorbereiten. Seine These: Codegenerierung allein schließt den Lernkreislauf nicht. Der Beitrag formuliert eine Architekturvision und bewirbt zugleich sein Produkt Polylane; eine gemessene Umsetzung liefert er nicht.

## Vom Einzelalarm zur gemeinsamen Untersuchung

Nach Tanes Darstellung tragen Menschen heute Informationen zwischen getrennten Analysewerkzeugen und Coding Agents hin und her. Ein Agent mit direktem Lesezugang zu mehreren Signalquellen könnte zusammengehörige Symptome gruppieren, den auslösenden Release suchen und einen Fix mit Belegen als Pull Request vorschlagen.

Vordefinierte Alerts und Webhooks bleiben dabei begrenzt: Sie entdecken vor allem Fehlerklassen, für die bereits ein Signal festgelegt wurde. Der Autor schlägt deshalb zusätzlich regelmäßige Untersuchungen über Werkzeuggrenzen hinweg vor. Dass Agents dadurch unbekannte Probleme zuverlässig entdecken, wird jedoch nicht getestet.

## Zielhierarchie vor Optimierung

Tane verwendet die Analogie von Vorwärtsdurchlauf und Backpropagation: Anforderungen erzeugen Code; Betriebssignale zeigen die Differenz zwischen gewünschtem und tatsächlichem Ergebnis. Die Analogie beschreibt eine Rückkopplung, kein mathematisch hergeleitetes Optimierungsverfahren für Software.

Menschen sollen festlegen, was eine Verbesserung bedeutet: führende Metriken, harte Grenzen, Zielkunden und erlaubte Trade-offs. Schnellerer Checkout, Betrugserkennung, Aktivierung und Marge können sich widersprechen. Ein Agent braucht eine explizite Gewichtung statt der pauschalen Aufgabe, alle Zahlen zu verbessern.

Die Beispielprompts kombinieren stündliche Fehleruntersuchungen mit täglichen Zielvergleichen. Genannte Werte wie Checkout-p99 unter `300 ms` sind illustrative Vorgaben, keine allgemein belegten Qualitätsgrenzen.

## Einordnung

Die gemeinsame Sicht auf Produktionssignale ergänzt vorhandene Ansätze zur begrenzten Agent-Autonomie. Tanes Forderung nach weitgehender Abgabe menschlicher Kontrolle steht jedoch in Spannung zu Review-Gates und abgestuften Rechten. Seine praktischen Beispiele enden bei Pull Requests, während die Vision selbstständiges Ausliefern und Wirkungskontrolle umfasst. Behauptungen über nahezu kostenlose Intelligenz, vollständige Datenanalyse oder unvermeidliche Selbstverbesserung sind nicht durch Messungen gedeckt. Als fachliche Grenze bleiben die Qualität der Signale, kausale Zuordnung, Verarbeitungskosten und Fehloptimierung offen.

## Kernaussagen

- Mehrere Produktionssignale gemeinsam auswerten und Änderungen mit ihrer Evidenz verbinden → [[Metrikband-gestufte-Agent-Autonomie]]
- Führende Ziele, harte Grenzen und Trade-offs vor automatischer Optimierung festlegen → [[Intent-Engineering-als-dritte-Schicht]]
- Einen vorgeschlagenen Fix und seine Freigabe als eigene Schritte beurteilen → [[CI-Agent-mit-Review-Gate]]

## Verbindungen

- [[Metrikband-gestufte-Agent-Autonomie]]
- [[Intent-Engineering-als-dritte-Schicht]]
- [[Review-Autonomie-mit-Shadow-Mode-und-Stichproben]]
