# Projektkarte-als-Status-und-Entscheidungsartefakt

**Konfidenz:** meinung

## Zweck

Nach längeren Arbeitsphasen schnell erkennen, was erledigt ist, was bis zum Meilenstein fehlt und welche Entscheidungen Arbeit blockieren.

## Funktionsweise

Projektteile und Meilensteine aus Code, Historie und Issues ableiten. Teile als erledigt, in Arbeit, nicht begonnen oder blockiert markieren. Wartegründe, verbleibende Aufgaben, Veränderungen seit dem letzten Stand und einen vorgeschlagenen nächsten Schritt anzeigen. Vor längeren Arbeitsphasen und nach Meilensteinen aktualisieren. Entscheidungspunkte mit erlaubten Defaults verbinden; freigabepflichtige Schritte bleiben bis zur Entscheidung blockiert. Eine lokale HTML-Karte ist eine mögliche Darstellung.

## Vorteile

- Verkürzt den Wiedereinstieg und macht Blockaden sichtbar.
- Verbindet Status mit konkretem Handlungsbedarf und nächstem Schritt.

## Nachteile & Grenzen

- Agent-generierte Prozentwerte brauchen überprüfbare Nachweise; eine Karte kann veralten.
- Erstellung, Nachführung und zusätzliche Agent-Aufrufe kosten Zeit und Kontext.
- Eine vorgeschlagene Folgeaktion erweitert keine Ausführungsbefugnis.

## Wann einsetzen, wann nicht

- Einsetzen: mehrere Projektteile, längere Arbeitsphasen und wiederkehrende Meilensteine.
- Nicht einsetzen: als Ersatz für Specs, Testergebnisse oder vollständige Sessionübergaben.

## Belege

- 2026-10-06 · [[2026-10-06-voxyz_ai-2107455844992299272]] · meinung — Vox beschreibt einen dedizierten Projektkarten-Agenten mit Meilensteinen, Blockaden, verbleibenden Aufgaben und Entscheidungsfeldern; das Beispiel belässt Stripe ohne Antwort im Testmodus und belegt keine Produktionswirkung oder Statusaktualität.
- 2026-08-20 · [[2026-08-20-latent-the-wayfinder-skill-navigating-the-fog-of-war-of]] · meinung — Das Interview trennt gemeinsame Karte, einzelne Entscheidungstickets und Sessions; es begrenzt Wayfinder auf Vorhaben mit unklarem Weg.
- 2026-08-12 · [[2026-08-12-shannholmberg-2087539757052285200]] · meinung — Überträgt vier Ticketarten auf eine einzelne Kampagne und dokumentiert Entscheidungen schrittweise im Brief; warnt vor veraltenden Gesamtstrategiekarten.

## Spannungen & offene Fragen

- Der Quellenpost empfiehlt Fortsetzung bei fehlender Antwort; sein Bild begrenzt den Stripe-Default auf Testmodus. Keine Antwort ersetzt keine erforderliche Freigabe.
- Beispielstatus und Fortschrittswerte belegen keine Produktionswirkung.

## Verwandte Patterns

- [[Task-basierte-Steuerung]]
- [[Handoff-Doc]]
- [[Blockierende-Task-Abhaengigkeiten]]
- [[Handlungsbedarf-zuerst-im-Agent-Bericht]]
