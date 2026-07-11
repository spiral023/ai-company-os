# Knowledge-System

Wissensbasis über KI-Arbeitsweisen (Coding Agents, Skills, Agent-Workflows, Frameworks). Gespeist aus Tweets, GitHub-Repos, Artikeln und eigener Erfahrung. Design-Spec: `docs/superpowers/specs/2026-07-11-knowledge-system-design.md`.

## Struktur

- `Sources/` — unveränderliches Quellen-Archiv, eine Datei pro Quelle: `YYYY-MM-DD-<autor>-<slug>.md` (Datum = Original-Veröffentlichung).
- `Patterns/` — lebende Synthese-Notizen, eine pro Arbeitsweise.
- `Vergleiche/` — Verdichtung mehrerer Patterns/Frameworks zu Empfehlungen, eine Datei pro Themenfeld.
- `Index.md` — Einstieg: alle Patterns und Vergleiche mit Einzeilern.

## Invarianten

1. In `Patterns/` wird nie gelöscht. Überholte Aussagen bekommen einen datierten Vermerk („bis YYYY-MM üblich, seitdem …“).
2. `Sources/`-Notizen werden nach Anlage nicht mehr inhaltlich verändert; nur Pattern-Links dürfen ergänzt werden.
3. Widersprüche zwischen Quellen werden nicht aufgelöst, sondern als Spannung (Trade-off) im betroffenen Pattern festgehalten.
4. Jede inhaltliche Aussage in einem Pattern muss mindestens einem Beleg zuordenbar sein.
5. Unklare Zuordnungen kommen als Frage nach `00_Inbox/Fragen_an_Philipp.md`, es wird nicht geraten.

## Konfidenz-Modell

Drei Beleg-Typen, aufsteigend gewichtet:

1. `meinung` — einzelner Tweet/Blogpost, eine Person.
2. `mehrfach-belegt` — mehrere voneinander unabhängige Quellen.
3. `verifiziert` — im geklonten Repo (`external_repos/`) nachgeprüft oder selbst getestet.

Konfidenz eines Patterns = höchster erreichter Beleg-Typ. Ist ein Pattern bereits `verifiziert`, werden weitere Belege trotzdem als Zeilen ergänzt; die Konfidenz-Angabe ändert sich nicht mehr.

## Template: Source-Notiz

```markdown
---
url: <URL oder "keine">
autor: <Handle oder Name>
datum: <YYYY-MM-DD der Original-Veröffentlichung>
erfasst: <YYYY-MM-DD des Ingests>
typ: tweet | artikel | repo | video | notiz
---

# <Titel: Autor zu Thema>

## Inhalt

<Originaltext. Bei URL-Abruf: das Abruf-Ergebnis, gekennzeichnet mit „(per WebFetch abgerufen, ggf. verlustbehaftet)“.>

Medien: <optional — Original-URL relevanter Bilder/Diagramme plus Ein-Satz-Beschreibung des Inhalts; nichts herunterladen>

## Kernaussagen

- <Aussage 1> → [[<Pattern-Name>]]
- <Aussage 2> → [[<Pattern-Name>]]
```

## Template: Pattern-Notiz

```markdown
# <Pattern-Name>

**Konfidenz:** meinung | mehrfach-belegt | verifiziert

## Zweck

<Welches Problem löst die Arbeitsweise?>

## Funktionsweise

<Wie läuft sie konkret ab?>

## Vorteile

- …

## Nachteile & Grenzen

- …

## Wann einsetzen, wann nicht

- Einsetzen: …
- Nicht einsetzen: …

## Belege

- YYYY-MM-DD · [[<Source-Datei>]] · <beleg-typ> — <Ein-Satz-Zusammenfassung des Belegs>
- YYYY-MM-DD · external_repos/<owner>/<repo>/<pfad> · verifiziert — <was dort bestätigt wurde>

## Spannungen & offene Fragen

- <Widerspruch/Trade-off oder "keine bekannt">

## Verwandte Patterns

- [[<Pattern>]]
```

## Template: Vergleichs-Notiz

```markdown
# Vergleich: <Themenfeld>

**Stand:** YYYY-MM-DD

## Übersicht

| Framework/Pattern | Kernidee | Stärken | Schwächen | Quelle/Repo |
|---|---|---|---|---|

## Empfehlungen

- <Situation/Projekttyp>: <Empfehlung mit Begründung>

## Offene Fragen

- …
```
