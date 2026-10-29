# Wayfinder als Karte offener Entscheidungen

**Konfidenz:** verifiziert

## Zweck

Ein Vorhaben über mehrere Agent-Sessions untersuchen, wenn dessen Umsetzung noch von ungeklärten Entscheidungen abhängt.

## Funktionsweise

Eine persistente Map hält Destination, bereits geklärte Entscheidungen, offene Decision Tickets, Abhängigkeiten und noch nicht ausreichend bestimmte Unklarheit fest. Die Destination setzt den Scope. Unscharfe Fragen innerhalb des Scopes bleiben als Fog of War sichtbar; bewusst ausgeschlossene Arbeit erhält einen eigenen Bereich.

Ein Decision Ticket stellt eine beantwortbare Frage. Je nach Erkenntnisbedarf folgt Grilling, Research, Prototype oder eine vorbereitende Task. Eine Task verdient hier ihren Platz, weil sie eine Entscheidung ermöglicht, etwa Zugang für einen Integrationsversuch bereitstellt. Ein Ticket ist kein gewöhnlicher Implementierungsslice.

Die Frontier besteht aus offenen, nicht blockierten und nicht übernommenen Tickets. Vor der Arbeit ein Ticket übernehmen. Nach der Klärung Ergebnis und Folgen in der Map festhalten, Blockaden auflösen und neue, nun präziser formulierbare Fragen ergänzen. Eine Session orientiert sich an der Destination und bearbeitet eine begrenzte Klärungsfrage. Bei geklärtem Weg folgen Spec und Implementierungstickets als andere Artefakte.

## Vorteile

- Verbindet neue Sessions über explizite Ergebnisse statt über einen wachsenden Chat.
- Macht Abhängigkeiten und noch fehlendes Wissen sichtbar.
- Erlaubt höhere Prototypauflösung genau dort, wo eine Entscheidung davon abhängt.

## Nachteile & Grenzen

- Map, Claims und Abhängigkeiten müssen konsistent gepflegt werden.
- Zu früh detaillierte Tickets erzeugen Scheingenauigkeit und überholte Planung.
- Eine geschlossene Map beweist weder die Richtigkeit einer Entscheidung noch Produktreife.

## Wann einsetzen, wann nicht

- Einsetzen: mehrere Sessions, unsichere Integration, konkurrierende Produktentscheidungen oder Prüfbedarf durch Prototypen.
- Nicht einsetzen: ein winziger, unmittelbar prüfbarer Diff oder ein bereits klarer Ablauf, den ein kurzes Grilling ausreichend klärt.

## Belege

- 2026-10-29 · [[2026-10-29-matt-pocock-software-factories-real-engineers]] · meinung — Die Kapitel zu Wayfinder untersuchen Benachrichtigungen mit Grilling, Vendor Research, manueller Einrichtung und Prototypen. Datum ist der Erfassungstag; die HTML-Demo ist kein Benchmark und die Videos wurden nicht ausgewertet.
- 2026-10-29 · external_repos/mattpocock/skills/skills/engineering/wayfinder/SKILL.md · verifiziert — Decision Tickets, die vier Typen, Claims, Frontier und Trennung von Fog und Out of scope im lokalen Checkout 59db609eb1e18aaf59b63284d0e52255aff0c63c statisch geprüft; kein Lauf gegen einen Issue-Tracker ausgeführt.

## Spannungen & offene Fragen

- 2026-10-29: Die Kursfassung zeigt ältere konkrete Kommandos und Trackerabläufe. Der lokale Referenzstand verwendet trackerabhängige Operationen und kann auf einen lokalen Markdown-Tracker zurückfallen. Die Methode ist übertragbar, ein eingefrorenes Kommando-Rezept braucht Versionsprüfung.
- 2026-10-29: [[Blockierende-Task-Abhaengigkeiten]] steuert ausführbare Arbeit. Wayfinder verwendet ähnliche Beziehungen für entscheidungsbezogene Untersuchungen; beide dürfen nicht zu einer einzigen unklaren Ticketklasse verschmelzen.

## Verwandte Patterns

- [[Spec-Grilling]]
- [[Projektkarte-als-Status-und-Entscheidungsartefakt]]
- [[Blockierende-Task-Abhaengigkeiten]]
- [[Tracer-Bullet-und-Lernprototyp-bewusst-waehlen]]
