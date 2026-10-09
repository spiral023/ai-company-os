# Visuelle-Abnahme-mit-Live-Lokal-Vergleich

**Konfidenz:** meinung

## Zweck

Visuelle Codeänderungen am tatsächlich gerenderten Ergebnis prüfen, bevor die Arbeit als fertig gemeldet wird. Der Vergleich mit dem bisherigen Live-Zustand hilft, neu verursachte Fehler von bestehenden Auffälligkeiten zu unterscheiden.

## Funktionsweise

Dem Prüfagenten betroffene URLs, Seiten, Änderungen und erwarteten Soll-Zustand übergeben. Live- und lokale Version mit vergleichbaren Daten öffnen; ohne Live-Version nur lokal prüfen. Auf tatsächlichen Seiteninhalt warten und lange Seiten abschnittsweise per Screenshot erfassen. Unterschiede dokumentieren und nach Ursache zuordnen. Nur durch die Änderung verursachte Defekte korrigieren und anschließend erneut prüfen. Die Quelle begrenzt die Schleife auf zwei Runden; offene Befunde werden danach gemeldet.

Die Prüfung findet im freigegebenen Browser statt. Bestehende Tabs bleiben unberührt; neue Tabs werden geschlossen. Passworteingaben, Senden und Bezahlaktionen gehören nicht zur Prüfung. Der Bericht benennt auch unerreichbare Seiten, fehlende Zugänge und abgebrochene Schritte.

## Vorteile

- Erfasst Layout, Überlappungen und leere Bereiche, die ein Code-Review allein übersehen kann.
- Liefert konkrete Befunde vor der Fertigmeldung und begrenzt automatische Korrekturschleifen.

## Nachteile & Grenzen

- Abweichende Daten, Feature-Flags, Browserzustände und Veröffentlichungsstände können den Vergleich verfälschen.
- Beabsichtigte Änderungen brauchen einen Soll-Zustand; Gleichheit mit Live ist kein allgemeines Qualitätsziel.
- Screenshots belegen weder funktionale Korrektheit noch mobile Nutzung oder Barrierefreiheit.
- Wirksamkeit und Kostenersparnis sind in der Quelle nicht gemessen; die genannte Integration wurde hier nicht getestet.

## Wann einsetzen, wann nicht

- Einsetzen: Änderungen an Layout, Darstellung und visuellen Interaktionszuständen mit erreichbaren Testseiten.
- Nicht einsetzen: rein interne Änderungen ohne sichtbare Wirkung; produktive Schreibaktionen bleiben außerhalb dieser Prüfung.

## Belege

- 2026-10-06 · [[2026-10-06-voxyz_ai-2107576635578855461]] · meinung — Vox schlägt gerenderte Live-/Lokal-Prüfung vor der Fertigmeldung vor, mit Zuordnung neuer Defekte, maximal zwei Korrekturrunden und begrenzten Browseraktionen; Wirksamkeit und konkrete Integration sind nicht gemessen.

## Spannungen & offene Fragen

- Zwei Runden sind ein Budget des Quellenprompts, keine empirisch begründete Obergrenze für Fehlerbehebung.
- Ein Screenshot kann einen plausiblen Zustand zeigen, während Datenfluss oder Interaktion weiterhin fehlerhaft sind.

## Verwandte Patterns

- [[Screenshot-als-Spezifikationsmedium]]
- [[Testharness-als-staerkster-Hebel]]
- [[Plan-first-mit-getrenntem-Review]]
