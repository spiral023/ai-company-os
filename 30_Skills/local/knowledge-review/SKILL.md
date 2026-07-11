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
5. **Validator ausführen.** `python 70_Scripts/validate_knowledge.py` — prüft deterministisch Frontmatter, Belege-Format, Konfidenz-Konsistenz, Wiki-Link-Ziele, Index-Vollständigkeit und Typografie. Gemeldete Fehler beheben und erneut ausführen.
6. **Konsistenz (inhaltlich).** Was der Validator nicht sieht: `80_Knowledge/Index.md`-Einzeiler noch treffend? Stand-Daten der Vergleichs-Notizen plausibel? Verwandte-Patterns-Links fachlich sinnvoll?
7. **Bericht ausgeben** (siehe Ausgabeformat). Erfolg nie melden, bevor der Validator fehlerfrei durchläuft; beim Merge erst nach erfolgreichem Validator-Lauf bereinigen.

## Ausgabeformat

- Merge-Kandidaten: <Liste oder "keine">
- Zu prüfen (veraltet): <Liste oder "keine">
- Aufgelöste Spannungen: <Liste oder "keine">
- Konfidenz-Korrekturen: <Liste oder "keine">
- Validator: <fehlerfrei | behobene Fehler>
- Index-/Link-Korrekturen: <Liste oder "keine">
- Empfehlung: <max. 3 nächste Schritte>
