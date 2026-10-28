# Frontend-Zustandslogik mit Reducer isolieren

**Konfidenz:** meinung

## Zweck

Frontend-Verhalten über explizite Zustände und Ereignisse getrennt vom Rendering prüfen können.

## Funktionsweise

Die Ausarbeitung vom 28.10.2026 überträgt Pococks Kamera-Beispiel in eine Prüfgrenze: Benenne die relevanten Zustände sowie Benutzer- und Fehlerereignisse. Eine gemeinsame Übergangslogik verarbeitet den bisherigen Zustand und ein Ereignis und liefert den Folgezustand. Die Oberfläche löst Ereignisse aus und stellt den Zustand dar.

Prüfe die erwarteten Übergänge außerhalb des Browsers, einschließlich unerwarteter Ereignisreihenfolgen und fachlich unzulässiger Zustände. Danach bleiben die Anbindung der UI und tatsächlich ausgeführte Effekte als eigene Prüfschicht. Der Vorschlag legt keine bestimmte State-Library fest.

## Vorteile

- Bündelt zusammengehöriges Zustandsverhalten an einer überschaubaren Schnittstelle.
- Macht erwartete Ereignisfolgen ohne vollständigen Browserlauf prüfbar.
- Gibt dem Agenten konkrete Eingaben und beobachtbare Folgezustände.

## Nachteile & Grenzen

- Die Auswahl der Zustände und Ereignisse kann unvollständig oder fachlich falsch sein.
- Ein Reducer deckt asynchrone Effekte, Browser-Anbindung und sichtbares Verhalten nicht automatisch ab.
- Zu große Zustandsmodelle können neue Kopplung und schwer verständliche Übergänge erzeugen.
- Die Quelle beschreibt wahrgenommene Robustheit und schnelle Tests ohne Vergleichsmessung.

## Wann einsetzen, wann nicht

- Einsetzen: mehrere zusammenhängende UI-Zustände, Ereignisse und Fehlerfälle erschweren die lokale Prüfung.
- Nicht einsetzen: als pauschale Pflicht für jeden einfachen UI-Wert oder als Ersatz für Browser- und Effekttests.

## Belege

- 2026-10-16 · [[2026-10-16-matt-pocock-the-secret-to-building-robust-frontend-apps-with]] · meinung — Kamera-Ereignisse werden in einer separat prüfbaren Zustandsfunktion verarbeitet; das UI löst nur die passende Aktion aus. Testgeschwindigkeit und Robustheit sind subjektiv beschrieben, nicht hier gemessen.

## Spannungen & offene Fragen

- 2026-10-28: Browserunabhängige Übergangstests prüfen die ausgewählte Logik. Sie ersetzen weder die fachliche Vollständigkeitsprüfung noch die sichtbare Abnahme; mehr Reducer sind für sich kein Qualitätsnachweis.

## Verwandte Patterns

- [[Testharness-als-staerkster-Hebel]]
- [[Refactoring-mit-Verhaltensvergleich]]
- [[Visuelle-Abnahme-mit-Live-Lokal-Vergleich]]
