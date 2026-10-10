# Quellen-Bookmarks für Agent-Automationen

**Konfidenz:** meinung

## Zweck

Wiederkehrende Quellenabfragen am bisherigen Verarbeitungsfortschritt anschließen, auch wenn ein Agent-Lauf früher oder später als geplant startet.

## Funktionsweise

Pro Quelle einen persistenten Fortschrittsmarker verwenden, statt jeden Lauf pauschal auf die vergangenen 24 Stunden zu beschränken. Bei verschobenen Startzeiten können relative Fenster Lücken oder Überlappungen erzeugen. Ein Quellen-Bookmark macht den vorgesehenen Anschluss unabhängig vom tatsächlichen Laufbeginn nachvollziehbar.

Quellenabruf, Verarbeitung und Versand getrennt prüfen: Lesefehler sichtbar melden, Duplikate erkennen und einen Versand erst nach Bestätigung als abgeschlossen markieren. Kosten pro Lauf begrenzen und Tokens nur die erforderlichen Rechte geben. Bei einer Bestandsprüfung Fundstelle, konkretes Fehlerszenario und kleinsten Änderungsvorschlag nennen.

Die Quelle beschreibt keine vollständige Zustandsmaschine. Bookmark-Schema, Aktualisierungszeitpunkt und Wiederholungsregeln müssen für die jeweilige Quelle festgelegt werden; sie folgen nicht automatisch aus dem Begriff Bookmark.

## Vorteile

- Der Quellenfortschritt lässt sich getrennt vom Ausführungsplan nachvollziehen.
- Fehler beim Lesen werden von tatsächlich fehlenden Neuigkeiten unterscheidbar.
- Getrennte Versandzustände ermöglichen eine gezielte Prüfung offener Zustellungen.

## Nachteile & Grenzen

- Persistierter Zustand, Fehlerbehandlung und Versandabgleich verursachen zusätzlichen Aufwand.
- Bookmarks allein garantieren keine lückenlose oder Exactly-once-Verarbeitung.
- Nachgelieferte, geänderte oder gelöschte Einträge, Pagination und parallele Läufe brauchen eigene Regeln.
- Kostenersparnis und Zuverlässigkeitsgewinn sind in der Quelle nicht gemessen.
- Der verlinkte Anthropic-Guide wurde nicht archiviert oder geprüft; Beleg sind Vox' Darstellung und sein eigener Audit-Prompt.

## Wann einsetzen, wann nicht

- Einsetzen: regelmäßige Quellenabfragen, Feeds, Monitoring oder Benachrichtigungen mit nachvollziehbarem Fortschritt und möglichen Laufverschiebungen.
- Nicht einsetzen: einmaliger Abruf oder als Ersatz für eine bereits verbindlich spezifizierte Zustell- und Wiederholungslogik.

## Belege

- 2026-10-09 · [[2026-10-09-voxyz_ai-2108573215224160393]] · meinung — Vox schlägt Quellen-Bookmarks plus Fehler-, Zustell-, Kosten- und Rechteprüfung für wiederkehrende Agent-Aufgaben vor; konkrete Zustands- und Wiederholungslogik sowie gemessene Ergebnisse fehlen.

## Spannungen & offene Fragen

- 2026-10-10: Wann darf der Bookmark fortgeschrieben werden: nach Abruf, Verarbeitung oder bestätigter Zustellung? Die Quelle legt dies nicht fest; eine falsche Grenze kann trotz Bookmark Daten verlieren oder doppelt verarbeiten.
- 2026-10-10: Wie werden Retry, parallele Läufe und später eintreffende Einträge behandelt? Eine reine Zeitmarke beantwortet diese Fragen nicht.
- 2026-10-10: Ein bestätigter Versand belegt nicht automatisch Anzeige oder Lesen beim Empfänger.

## Verwandte Patterns

- [[Handlungsbedarf-zuerst-im-Agent-Bericht]]
- [[Freigaben-und-Isolation-getrennt-steuern]]
- [[Sandbox-Komposition-aus-OS-Primitiven]]
