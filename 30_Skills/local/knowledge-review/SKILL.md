---
name: knowledge-review
description: Verwende diesen Skill für den Pflege-Lauf des Knowledge-Systems (80_Knowledge/) — manuell auf Zuruf oder als Teil des Wochenreviews. Findet Duplikate, veraltete Patterns und prüfbare Spannungen, hält Index und Vergleiche konsistent.
---

# Knowledge Review

## Ziel

Das Knowledge-System wird mit der Zeit besser statt nur größer: Redundanz zusammenführen, Veraltetes markieren, offene Spannungen auflösen, Konfidenzen aktuell halten.

## Schema

Templates, Invarianten und Konfidenz-Modell stehen in `80_Knowledge/README.md`.

## Ablauf

1. **Duplikate/Merge-Kandidaten.** Alle Dateien in `80_Knowledge/Patterns/` sichten. Patterns, die dasselbe Konzept unter anderem Namen beschreiben, als Merge-Kandidat melden. Merge nur nach Philipp-OK; beim Merge alle Belege übernehmen und im aufgehenden Pattern einen Verweis „aufgegangen in [[Ziel]]“ hinterlassen (nicht löschen).
2. **Frische.** Patterns, deren jüngster Beleg älter als ~90 Tage ist, im Konfidenz-Block mit „zu prüfen (kein frischer Beleg seit YYYY-MM-DD)“ markieren.
3. **Spannungen prüfen.** Für jede offene Spannung prüfen, ob sie inzwischen entscheidbar ist — z.B. weil das betreffende Repo jetzt unter `external_repos/` liegt oder neue Quellen existieren. Entscheidbare Spannungen mit datiertem Vermerk auflösen (alte Sicht bleibt dokumentiert).
4. **Konfidenzen neu ableiten.** Pro Pattern: höchster Beleg-Typ = Konfidenz. Abweichungen korrigieren.
5. **Konsistenz.** `80_Knowledge/Index.md` gegen die tatsächlichen Dateien in `Patterns/` und `Vergleiche/` abgleichen (fehlende Einträge ergänzen, verwaiste entfernen); Wiki-Links stichprobenartig prüfen; Stand-Daten der Vergleichs-Notizen prüfen.
6. **Bericht ausgeben** (siehe Ausgabeformat).

## Ausgabeformat

- Merge-Kandidaten: <Liste oder "keine">
- Zu prüfen (veraltet): <Liste oder "keine">
- Aufgelöste Spannungen: <Liste oder "keine">
- Konfidenz-Korrektionen: <Liste oder "keine">
- Index-/Link-Korrekturen: <Liste oder "keine">
- Empfehlung: <max. 3 nächste Schritte>
