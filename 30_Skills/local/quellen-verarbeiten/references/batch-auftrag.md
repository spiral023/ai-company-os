# Auftrag: Quellen aus der Inbox ins Knowledge-System einarbeiten

Du arbeitest als erfahrener AI Engineer im Repo `c:\Users\asi\Documents\GitHub\ai-company-os`.

## Zuerst lesen (Pflicht, in dieser Reihenfolge)

1. `30_Skills/local/quellen-verarbeiten/SKILL.md` — dein Ablauf und deine Rolle.
2. `30_Skills/local/quellen-verarbeiten/references/artikel-format.md` — Aufbau, Sprache, Bildregeln.
3. `80_Knowledge/README.md` — Invarianten und Konfidenz-Modell.

## Was du tust

Für **jede** dir zugewiesene Quelle in einem Typordner unter `00_Inbox/Quellen/`:

1. **Vollständig lesen.** Nicht nur den Anfang.
2. **Alle Bilder lesen**, die die Notiz referenziert (`medien/<slug>/...`). Das ist Pflicht, keine Option. Charts, Preistabellen und Diagramme enthalten regelmäßig Zahlen und Abläufe, die im Text fehlen — genau diese Werte sind der Mehrwert. Ein Bild ohne Erklärwert (Header-Grafik, Logo, Deko) wird nicht in die Source-Notiz übernommen.
3. **Relevanz prüfen.** Enthält die Quelle eine übertragbare Erkenntnis über Arbeitsweisen (AI Coding, Agents, Skills, Context, Evals, Kosten, Tooling, Security)? Falls nein: in der Inbox-Notiz `status: ignoriert` setzen, `notiz:` mit einem Satz Begründung ergänzen, keine Source-Notiz anlegen.
4. **Source-Notiz schreiben** nach `80_Knowledge/Sources/YYYY-MM-DD-<autor>-<slug>.md` (Datum = Veröffentlichungsdatum der Quelle, aus dem Frontmatter-Feld `datum`).
5. **Inbox-Status fortschreiben**: `status: verarbeitet`, `verarbeitet_am: 2026-08-04`, `source_notiz: 80_Knowledge/Sources/<datei>.md`. Am Inhalt der Inbox-Notiz sonst nichts ändern.

## Bilder in der Source-Notiz

Bilder werden **nicht kopiert**, sondern relativ referenziert:

```markdown
![Beschreibender Alt-Text, der Inhalt und Zweck nennt](../../00_Inbox/Quellen/<Quelltyp>/medien/<slug>/<datei>.jpg)
```

- Platziere jedes Bild **an der Stelle, wo der zugehörige Text steht** — nicht alle am Anfang. Die Inbox-Notiz zeigt dir bei importierten vibedeck-Artikeln die ursprüngliche Position; übernimm sie, wenn sie inhaltlich passt.
- Schreibe die **Werte aus dem Bild in den Fließtext**. Ein Leser soll die Aussage ohne Bildbetrachtung verstehen.
- Prüfe, dass die Datei existiert, bevor du sie referenzierst.

## Sekundärquellen: besondere Vorsicht

Trägt die Inbox-Notiz `sekundaerquelle: true`, ist der Inhalt eine **fremde deutsche Aufarbeitung** aus dem vibedeck-Projekt, nicht die Primärquelle. Dann gilt:

- In der Source-Notiz das Feld `beleg_art: sekundaerquelle` ergänzen und im Text einmal klar benennen, dass die Aufarbeitung aus zweiter Hand stammt.
- Keine Zahl oder Behauptung so darstellen, als hättest du sie in der Primärquelle geprüft.
- Liegt zusätzlich eine **Primärquelle** zur selben URL in der Inbox (ich nenne sie dir explizit, falls vorhanden): beide zu **einer** Source-Notiz verschmelzen, `rohquelle:` auf beide Dateien verweisen lassen, und im Text unterscheiden, was aus der Primärquelle belegt ist und was nur die Sekundärfassung behauptet. Beide Inbox-Notizen auf `verarbeitet` setzen.

## Strikte Grenzen — nicht verletzen

- **Lege KEINE Pattern-Dateien an und ändere KEINE bestehenden Patterns.** Mehrere Subagents arbeiten parallel; Patterns werden zentral konsolidiert. Du lieferst nur Vorschläge in deinem Abschlussbericht.
- **Ändere nicht** `80_Knowledge/Index.md`, `80_Knowledge/Vergleiche/`, Skills oder Workflows.
- Verweise in `## Kernaussagen` und `## Verbindungen` bevorzugt auf **bestehende** Patterns (Liste unten). Brauchst du ein neues, verwende einen sprechenden Namen in `[[Doppelklammern]]` und melde ihn als Vorschlag — ich lege ihn an oder mappe ihn auf ein bestehendes.
- Erfinde keine Präzision. „Deutlich schneller" wird nicht zu einer Prozentzahl.
- Deutsche Anführungszeichen ausschließlich `„…"` (U+201E öffnend, U+201C schließend), **niemals** gemischt mit ASCII `"`. Das ist der häufigste Validator-Fehler und passiert erfahrungsgemäß trotz dieser Regel. Deshalb **nach dem Schreiben verpflichtend** über die eigenen neuen Dateien laufen lassen:

  ```powershell
  python 70_Scripts/fix_typography.py 80_Knowledge/Sources/<deine-datei>.md
  ```

  Nur die eigenen Dateien angeben, niemals ganze Ordner — Altdateien gehören nicht zu deinem Lauf.
- Dateien mit LF-Zeilenenden und ohne BOM schreiben.

## Bestehende Patterns (26) — bevorzugt darauf verweisen

Action-Space-Design-nach-Modellfaehigkeit · Advisor-Agent-gegen-Drift · AGENTS-md-Onboarding-Design · Anti-Rationalization-Tables · CONTEXT-Glossar · Deny-Rules-statt-CLAUDE-md-Empfehlung · Erweiterungs-Ebenen-Zuordnung · Fable-Unknowns-vor-Prompt-Qualitaet · Great-Decoupling-Rollenverstaendnis · Handoff-Doc · Intent-Engineering-als-dritte-Schicht · Klein-und-komposierbar · Kontext-Hygiene-Entscheidungsbaum · Kontrollierte-Agent-Parallelisierung · Lokale-Modell-Umleitung-Muster · Lovable-Prototyp-dann-lokaler-Handoff · Modell-Eskalation-von-guenstig-nach-teuer · One-File-per-Failure-Mode · Plan-first-mit-getrenntem-Review · Ralph-Loop-Frischer-Kontext-pro-Iteration · Skill-Call-Hierarchie · Skill-Qualitaet-durch-Trigger-und-Baseline-Evals · Spec-Grilling · Task-basierte-Steuerung · TDD-als-Verifikationshebel · Testharness-als-staerkster-Hebel

## Dein Abschlussbericht (knapp, strukturiert)

```
VERARBEITET
- <inbox-datei> → Sources/<datei>.md · <n> Bilder eingebettet
  Kernaussagen: <Stichworte>
  Patterns bestehend: <Namen, auf die du verwiesen hast>
  Patterns NEU vorgeschlagen: <Name> — <ein Satz Begründung, warum eigenständig>
  Beleg-Art: primaerquelle | sekundaerquelle
IGNORIERT
- <inbox-datei> — <Begründung>
BEFUNDE
- <Widersprüche zwischen zwei deiner Quellen, auffällige Zahlen, fehlende Bilder>
```

Halte den Bericht kompakt — er wird von mir gelesen, nicht vom Nutzer. Wichtig sind die Pattern-Vorschläge und Widersprüche.
