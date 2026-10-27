---
url: keine
autor: Philipp Asanger
datum: 2026-10-27
erfasst: 2026-10-27
typ: notiz
rohquelle: 00_Inbox/Quellen/URL/2026-10-27-philipp-asanger-imagegen-designvergleich.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Designfeinschliff mit einem Bildentwurf vor der Umsetzung prüfen

Philipps eigener Prompt nutzt ein Bildmodell, um kleine Designverbesserungen an einer bestehenden Seite vorab sichtbar zu machen. Ein Screenshot des aktuellen Stands und eine mit Imagegen erzeugte Variante werden in einer lokalen Vergleichsseite gegenübergestellt. Der mitgelieferte Screenshot veranschaulicht die Arbeitsweise; ein gemessener Qualitätsgewinn oder eine Funktionsprüfung ist damit nicht belegt.

## Den Vergleich auf die Gestaltung begrenzen

Ausgangspunkt ist die bestehende Seite. Inhalte, Branding und Bildausschnitt sollen im generierten Entwurf möglichst gleich bleiben, damit die gestalterischen Unterschiede beurteilbar werden. Der Prompt zielt auf Detailverbesserungen am Projekt, ohne die eigentliche Anwendung zunächst zu verändern.

Der vorgesehene Ablauf ist:

1. Den aktuellen Stand per Screenshot festhalten.
2. Mit Imagegen eine verbesserte Designvariante auf dieser Grundlage erzeugen.
3. Beide Bilder auf einer lokalen Vergleichsseite mit Umschalter für Vorher und Entwurf, Schieberegler, Nebeneinander-Ansicht, Zoom und Vollbild anbieten.
4. Den Entwurf ausdrücklich als noch nicht implementiert kennzeichnen und Bilder sowie Prompt im Projekt speichern.
5. Die Vergleichsseite im Browser prüfen und öffnen. Änderungen an der eigentlichen Anwendung sind ein späterer Arbeitsschritt.

## Das Beispiel zeigt die Vergleichsansicht

![EventHorizon-Aktivitätenseite im Schieberegler-Vergleich: links der Entwurf, rechts der vorherige Stand; darüber Ansichtswechsel, Zoom und Vollbild](../../00_Inbox/Quellen/URL/medien/2026-10-27-philipp-asanger-imagegen-designvergleich/01-beispiel-designvergleich.png)

Das Bild zeigt die Aktivitätenseite von EventHorizon mit Navigation, Filtern und Aktivitätskarten. Eine vertikale türkisfarbene Trennlinie mit Griff stellt links den Entwurf und rechts den vorherigen Stand gegenüber. Oben sind die vier Ansichten und ein Zoomwert von 100 % sichtbar. Der Screenshot zeigt diese Bedienelemente, belegt aber nicht deren Funktion. Auch die im Prompt geforderte ausdrückliche Kennzeichnung als noch nicht implementiert ist durch das sichtbare Label „Entwurf“ allein nicht vollständig nachgewiesen.

## Einordnung

Die Methode ergänzt das bekannte Vorgehen, zunächst ein Referenzbild zu generieren und es danach umzusetzen: Hier stehen der direkte Vergleich mit dem bestehenden Produkt und die bewusste Pause vor der Implementierung im Mittelpunkt. Gleiche Inhalte und ein vergleichbarer Bildausschnitt helfen bei der Beurteilung; ob das Bildmodell diese Vorgaben einhält, muss am Ergebnis kontrolliert werden. Als fachliche Grenze gilt: Ein überzeugender Rasterentwurf belegt weder Responsive-Verhalten und Accessibility noch funktionierende Interaktionen oder die technische Umsetzbarkeit einzelner Details. Zusätzlicher Aufwand entsteht durch Bildgenerierung, Aufbau und Prüfung der Vergleichsseite; eine Zeitersparnis wurde nicht gemessen. Der archivierte Prompt bleibt eine vorgeschlagene Arbeitsweise mit Anschauungsbild, kein in diesem Quellenlauf ausgeführter Produkttest.

## Kernaussagen

- Einen bestehenden Screenshot und einen generierten Entwurf mit möglichst gleichen Inhalten als konkrete visuelle Vorgabe nutzen. → [[Screenshot-als-Spezifikationsmedium]]
- Kleine Designänderungen vor der Implementierung lokal vergleichbar machen und den Entwurfsstatus sichtbar halten. → [[Variantenvergleich-vor-Produktionsabnahme]]
- Die Vergleichsseite prüfen und die spätere Abnahme der tatsächlich implementierten Oberfläche als eigenen Schritt behandeln. → [[Variantenvergleich-vor-Produktionsabnahme]]

## Verbindungen

- [[Screenshot-als-Spezifikationsmedium]]
- [[Variantenvergleich-vor-Produktionsabnahme]]
- [[Visuelle-Abnahme-mit-Live-Lokal-Vergleich]]
- [[2026-09-19-voxyz_ai-2101295246659182978]]
