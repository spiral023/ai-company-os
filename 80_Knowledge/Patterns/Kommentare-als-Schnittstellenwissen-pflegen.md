# Kommentare-als-Schnittstellenwissen-pflegen

**Konfidenz:** meinung

## Zweck

Das für korrekte Nutzung nötige Wissen dort festhalten, wo Namen, Typen und sichtbarer Code es nicht ausreichend vermitteln.

## Funktionsweise

Schnittstellenkommentare erklären Zweck, erlaubte Argumente, Ergebnis, Einheiten, Grenzen, Besitz, relevante Seiteneffekte und Fehler. Sie bleiben auf der öffentlichen Bedeutungsebene. Implementierungskommentare erklären dagegen einen nicht offensichtlichen Grund, eine interne Invariante oder einen Trade-off. Die folgende Anweisung in Prosa zu wiederholen schafft kein zusätzliches Wissen.

Bei einem wichtigen Entwurf den Vertrag früh formulieren. Wenn er nur mit vielen Ausnahmen verständlich wird, die Schnittstelle selbst prüfen. Dauerhafte Entscheidungen an einem passenden auffindbaren Ort beschreiben und von weiteren betroffenen Stellen verlinken. Kommentare im gleichen Diff wie die Verhaltensänderung prüfen; allein im Commitverlauf abgelegte Gründe sind später leicht unsichtbar.

**Übertragung auf Agents:** Für geänderte APIs nach dem notwendigen Aufruferwissen fragen. Neue Kommentare müssen eine tatsächliche Informationslücke schließen und mit Code und Tests übereinstimmen. Automatisch erzeugte Absatzmenge ist kein Qualitätsmaß.

## Vorteile

- Reduziert das notwendige Lesen privater Implementierungen.
- Macht versteckte Nebenwirkungen und Aufrufpflichten auffindbar.
- Verwendet Dokumentation als frühe Prüfung der Abstraktion.

## Nachteile & Grenzen

- Falsche oder veraltete Kommentare können gefährlicher als fehlende sein.
- Zu viele Implementierungsdetails in einer API-Dokumentation schaffen unbeabsichtigte öffentliche Verpflichtungen.
- Es gibt keine aus diesen Quellen abgeleitete Pflicht, jede triviale Funktion mechanisch zu kommentieren.

## Wann einsetzen, wann nicht

- Einsetzen: nicht offensichtliche API-Verträge, Einheiten, Ownership, Nebenläufigkeitsannahmen und Entwurfsgründe.
- Nicht einsetzen: selbsterklärende Zuweisungen nacherzählen oder schwer verständlichen Code lediglich mit mehr Prosa überdecken.

## Belege

- 2021-07-01 · [[2021-07-01-pdf-a-philosophy-of-software-design-2nd-edition]] · meinung — PDF-S. 104–129 und 139–150 begründen fehlendes Schnittstellenwissen, frühe Kommentare und Dokumentationspflege; der bibliografische Tageswert 01 ist ein Sortierwert.
- 2019-09-13 · [[2019-09-13-pdf-the-pragmatic-programmer-20th-anniversary-edition]] · meinung — PDF-S. 68–69 empfehlen API-Wissen, Gründe und Trade-offs und lehnen mechanische Kommentierung jeder Funktion ab. Die Quelle von 2019 untersucht keine aktuellen Agents.

## Spannungen & offene Fragen

- 2026-10-29: Beide Bücher lehnen redundante Kommentare ab. Ousterhout betont vollständiges informelles API-Wissen stärker; Pragmatic setzt den Akzent auf sinnvolle Leserinformation statt Kommentarrituale. Die passende Dichte hängt von der tatsächlichen Informationslücke ab.
- Ob Kommentare Agentenkontext oder Reviewkosten im konkreten Projekt verbessern, wurde hier nicht gemessen.

## Verwandte Patterns

- [[Information-Hiding-an-Aenderungsgruenden-ausrichten]]
- [[Vertraege-mit-Vorbedingungen-Nachbedingungen-und-Invarianten]]
- [[Architektur-in-Perspektiven-dokumentieren]]
- [[CONTEXT-Glossar]]
