# Knowledge-System (80_Knowledge) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Selbstverbesserndes Markdown-Knowledge-System für Arbeitsweisen-Wissen (Tweets, Repos, Artikel über Coding Agents) mit Ingest- und Review-Skill aufbauen und mit zwei Tweets initial befüllen.

**Architecture:** Zweischichtiges Markdown-System unter `80_Knowledge/`: unveränderliche `Sources/` (Quellen-Archiv), lebende `Patterns/` (eine Synthese-Notiz pro Arbeitsweise, datierte Belege, Spannungen statt Überschreiben) und `Vergleiche/` (Empfehlungs-Verdichtung). Zwei lokale Skills (`knowledge-ingest`, `knowledge-review`) steuern Einarbeitung und Pflege. Spec: `docs/superpowers/specs/2026-07-11-knowledge-system-design.md`.

**Tech Stack:** Nur Markdown + YAML (Obsidian-kompatibel, Wiki-Links). Keine Scripts, keine Abhängigkeiten. Verifikation über Datei-Checks in PowerShell.

## Global Constraints

- Sprache: Deutsch mit korrekten Umlauten; englische Fachbegriffe wo üblich (gemäß `AGENTS.md`).
- Obsidian-kompatibel: reine Markdown-Dateien, Wiki-Links wie `[[Spec-Grilling]]`, keine Plugin-Abhängigkeiten.
- Invariante des Systems: In `Patterns/` wird nie gelöscht, nur datiert ergänzt oder als überholt markiert; `Sources/` sind nach Anlage unveränderlich (nur Pattern-Links dürfen ergänzt werden).
- Jede inhaltliche Aussage in einer Pattern-Notiz muss mindestens einem Beleg zuordenbar sein.
- Konfidenz-Modell (aufsteigend): `meinung` < `mehrfach-belegt` < `verifiziert`.
- Commits: kleine, nachvollziehbare Schritte; Co-Authored-By-Zeile gemäß Harness-Vorgabe.
- Das Repo ist ein Windows-Checkout; Pfade in Befehlen mit `/` schreiben (PowerShell akzeptiert beides).

---

### Task 1: Grundgerüst `80_Knowledge/` (README + Index)

**Files:**
- Create: `80_Knowledge/README.md`
- Create: `80_Knowledge/Index.md`

**Interfaces:**
- Produces: `80_Knowledge/README.md` mit den drei Notiz-Templates (Source, Pattern, Vergleich) und dem Konfidenz-Modell — die Skills aus Task 2 und 3 verweisen auf genau diese Datei als Schema-Quelle. `80_Knowledge/Index.md` mit den Abschnitten `## Patterns` und `## Vergleiche`, die der Ingest-Skill pflegt.

- [ ] **Step 1: `80_Knowledge/README.md` anlegen**

Exakter Inhalt:

````markdown
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

Konfidenz eines Patterns = höchster erreichter Beleg-Typ.

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
````

- [ ] **Step 2: `80_Knowledge/Index.md` anlegen**

Exakter Inhalt:

```markdown
# Knowledge-Index

Einstieg ins Knowledge-System. Regeln und Templates: [[README]] (80_Knowledge/README.md).

## Patterns

_(noch keine — werden durch knowledge-ingest angelegt)_

## Vergleiche

_(noch keine)_
```

- [ ] **Step 3: Verifizieren**

Run: `Test-Path 80_Knowledge/README.md, 80_Knowledge/Index.md`
Expected: zweimal `True`

- [ ] **Step 4: Commit**

```powershell
git add 80_Knowledge/README.md 80_Knowledge/Index.md
git commit -m @'
Knowledge-System: Grundgeruest 80_Knowledge (README, Index)

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

---

### Task 2: Skill `knowledge-ingest`

**Files:**
- Create: `30_Skills/local/knowledge-ingest/SKILL.md`

**Interfaces:**
- Consumes: Templates und Invarianten aus `80_Knowledge/README.md` (Task 1).
- Produces: Skill mit id `knowledge-ingest`, der von Task 4 (Registry) referenziert und in Task 5/6 ausgeführt wird.

- [ ] **Step 1: `30_Skills/local/knowledge-ingest/SKILL.md` anlegen**

Exakter Inhalt:

```markdown
---
name: knowledge-ingest
description: Verwende diesen Skill, wenn Philipp einen Tweet, einen Link (z.B. x.com), einen Artikel oder formlosen Text über KI-Arbeitsweisen, Skills, Agent-Workflows oder Frameworks teilt — auch ohne expliziten Auftrag. Arbeitet die Information ins Knowledge-System (80_Knowledge/) ein und liefert ein Diff-Resümee.
---

# Knowledge Ingest

## Ziel

Neue Informationen über Arbeitsweisen dauerhaft ins Knowledge-System einarbeiten: Quelle archivieren, Erkenntnisse in Pattern-Notizen synthetisieren, Vergleiche aktualisieren. Neue Infos machen alte nicht irrelevant — es wird ergänzt, nie gelöscht.

## Schema

Templates, Invarianten und Konfidenz-Modell stehen in `80_Knowledge/README.md`. Diese Datei vor der ersten Einarbeitung lesen und exakt befolgen.

## Ablauf

1. **Quelle beschaffen.**
   - Eingefügter Originaltext hat Vorrang (verlustfrei).
   - Bei URL: per WebFetch abrufen. Schlägt der Abruf fehl oder wirkt unvollständig (z.B. fehlender Thread), Philipp um den eingefügten Originaltext bitten und so lange nicht weitermachen.
2. **Duplikat-Check.** `80_Knowledge/Sources/` nach gleicher URL oder gleichem Inhalt durchsuchen. Bei Treffer: nicht neu archivieren, sondern nur prüfen, ob neue Aussagen dazugekommen sind.
3. **Source-Notiz anlegen** nach Template, Dateiname `YYYY-MM-DD-<autor>-<slug>.md` (Datum = Original-Veröffentlichung).
4. **Kernaussagen extrahieren.** Jede benennbare, wiederverwendbare Erkenntnis über eine Arbeitsweise ist ein Kandidat für ein Pattern.
5. **Abgleich mit Bestand.** `80_Knowledge/Index.md` lesen. Pro Kernaussage entscheiden:
   - Passendes Pattern existiert → Notiz ergänzen (neuer Beleg, ggf. neue Vor-/Nachteile, Konfidenz neu ableiten).
   - Kein passendes Pattern → neue Pattern-Notiz nach Template anlegen. Schwelle: Das Konzept ist benennbar und über die konkrete Quelle hinaus wiederverwendbar.
   - Aussage widerspricht Bestandswissen → im betroffenen Pattern unter „Spannungen & offene Fragen“ als Trade-off festhalten, mit beiden Quellen.
6. **Repo-Verifikation.** Erwähnt die Quelle ein Repo, das unter `external_repos/` liegt (siehe `external_repos/INDEX.md`): zentrale Behauptungen dort stichprobenartig nachprüfen (Dateien/Struktur ansehen). Bestätigte Belege auf `verifiziert` heben; Abweichungen als Spannung notieren. Liegt das Repo nicht vor: Download gemäß `AGENTS.md` → „Repo-Import“ vorschlagen, aber nicht eigenmächtig klonen.
7. **Vergleiche & Index aktualisieren.** Betroffene Notizen in `80_Knowledge/Vergleiche/` aktualisieren (Stand-Datum setzen); neue Patterns und Vergleiche in `80_Knowledge/Index.md` mit Einzeiler eintragen.
8. **Diff-Resümee ausgeben** (siehe Ausgabeformat).

## Grenzfälle

- Unklare Zuordnung oder mehrdeutige Aussage: als Frage in `00_Inbox/Fragen_an_Philipp.md` eintragen, nicht raten.
- Quelle enthält nichts über Arbeitsweisen (reine Meinung/News ohne wiederverwendbare Erkenntnis): kurz melden, nichts anlegen.
- Meta-Erkenntnisse über das Knowledge-System selbst (z.B. bessere Notiz-Struktur): Philipp vorschlagen, nicht eigenmächtig das Schema ändern.

## Ausgabeformat (Diff-Resümee)

- ✓ Quelle archiviert: `Sources/<datei>`
- ✓ Pattern ergänzt: `<Name>` (+n Belege, Konfidenz: <alt> → <neu>)
- ✓ Pattern NEU: `<Name>`
- ✓ Vergleich aktualisiert: `<Name>`
- ⚠ Spannung: <Ein-Satz-Beschreibung> → notiert in `<Pattern>`
- ? Offene Frage: <Frage> → `00_Inbox/Fragen_an_Philipp.md`
```

- [ ] **Step 2: Verifizieren**

Run: `Test-Path 30_Skills/local/knowledge-ingest/SKILL.md`
Expected: `True`

Zusätzlich prüfen (lesen): Frontmatter enthält `name:` und `description:`, Ablauf hat 8 Schritte.

- [ ] **Step 3: Commit**

```powershell
git add 30_Skills/local/knowledge-ingest/SKILL.md
git commit -m @'
Knowledge-System: Skill knowledge-ingest

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

---

### Task 3: Skill `knowledge-review`

**Files:**
- Create: `30_Skills/local/knowledge-review/SKILL.md`

**Interfaces:**
- Consumes: Templates und Konfidenz-Modell aus `80_Knowledge/README.md` (Task 1).
- Produces: Skill mit id `knowledge-review`, referenziert von Task 4 (Registry, Wochenreview).

- [ ] **Step 1: `30_Skills/local/knowledge-review/SKILL.md` anlegen**

Exakter Inhalt:

```markdown
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
- Konfidenz-Korrekturen: <Liste oder "keine">
- Index-/Link-Korrekturen: <Liste oder "keine">
- Empfehlung: <max. 3 nächste Schritte>
```

- [ ] **Step 2: Verifizieren**

Run: `Test-Path 30_Skills/local/knowledge-review/SKILL.md`
Expected: `True`

- [ ] **Step 3: Commit**

```powershell
git add 30_Skills/local/knowledge-review/SKILL.md
git commit -m @'
Knowledge-System: Skill knowledge-review

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

---

### Task 4: Integration (Registry, AGENTS.md, Wochenreview)

**Files:**
- Modify: `30_Skills/registry.yaml` (skills-Liste, nach dem Eintrag `seo-manager`, vor `project_types:`)
- Modify: `AGENTS.md` (neuer Abschnitt nach „## Scripts“-Vorgänger — konkret: direkt nach dem Abschnitt „## Skill-Nutzung“)
- Modify: `20_Workflows/Wochenreview.md` (Ablauf + Empfohlene Skills)

**Interfaces:**
- Consumes: Skill-Dateien aus Task 2 und 3 (Pfade müssen existieren).
- Produces: Registry-Einträge `knowledge-ingest`, `knowledge-review`; AGENTS.md-Trigger für formlose Tweet-Links.

- [ ] **Step 1: Registry-Einträge ergänzen**

In `30_Skills/registry.yaml` in der `skills:`-Liste direkt nach dem `seo-manager`-Eintrag (endet mit der Zeile `  description: Erstellt SEO-Strategien, Keyword-Cluster, Content-Briefs und Onpage-Checklisten.`) einfügen:

```yaml
- id: knowledge-ingest
  type: local
  path: 30_Skills/local/knowledge-ingest/SKILL.md
  status: active
  trust: owned
  copy_to_project: false
  project_types:
  - all
  default_for_project_types: []
  description: Arbeitet Tweets, Links und Texte über KI-Arbeitsweisen ins Knowledge-System
    (80_Knowledge) ein und liefert ein Diff-Resümee.
- id: knowledge-review
  type: local
  path: 30_Skills/local/knowledge-review/SKILL.md
  status: active
  trust: owned
  copy_to_project: false
  project_types:
  - all
  default_for_project_types: []
  description: Pflege-Lauf für das Knowledge-System — Duplikate, veraltete Patterns,
    Spannungen, Konfidenzen und Index-Konsistenz.
```

- [ ] **Step 2: AGENTS.md-Abschnitt ergänzen**

In `AGENTS.md` direkt nach dem Abschnitt „## Skill-Nutzung“ (nach der Zeile `- Externe Skills müssen geprüft werden, bevor sie in Projekt-Kits übernommen werden.`) einfügen:

```markdown

## Knowledge-System

Wissen über KI-Arbeitsweisen (Skills, Agent-Workflows, Frameworks) lebt unter `80_Knowledge/`. Regeln und Templates: `80_Knowledge/README.md`.

- Teilt Philipp einen Tweet, x.com-Link oder Text über Arbeitsweisen — auch formlos ohne Auftrag — den Skill `knowledge-ingest` anwenden.
- Pflege-Lauf über den Skill `knowledge-review`, u.a. im Wochenreview.
- In `80_Knowledge/Patterns/` wird nie gelöscht, nur datiert ergänzt; Widersprüche werden als Spannungen festgehalten.
```

- [ ] **Step 3: Wochenreview ergänzen**

In `20_Workflows/Wochenreview.md`:

Im Abschnitt `## Ablauf` nach Zeile `5. relevante Memory-Dateien aktualisieren.` ergänzen:

```markdown
6. Knowledge-System pflegen (Skill knowledge-review).
```

Im Abschnitt `## Empfohlene Skills` nach `- skill-autoreview` ergänzen:

```markdown
- knowledge-review
```

- [ ] **Step 4: Verifizieren**

Run: `Select-String -Path 30_Skills/registry.yaml -Pattern 'knowledge-ingest|knowledge-review' | Measure-Object | Select-Object -ExpandProperty Count`
Expected: `4` (je id- und path-Zeile pro Skill)

Run: `Select-String -Path AGENTS.md -Pattern '## Knowledge-System'`
Expected: ein Treffer

Run: `Select-String -Path 20_Workflows/Wochenreview.md -Pattern 'knowledge-review' | Measure-Object | Select-Object -ExpandProperty Count`
Expected: `2`

- [ ] **Step 5: Commit**

```powershell
git add 30_Skills/registry.yaml AGENTS.md 20_Workflows/Wochenreview.md
git commit -m @'
Knowledge-System: Integration in Registry, AGENTS.md und Wochenreview

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

---

### Task 5: Initialbefüllung Tweet 1 (Vox zu mattpocock/skills) — Abnahmetest „Neuanlage“

**Files:**
- Create: `80_Knowledge/Sources/2026-07-10-voxyz-mattpocock-skills.md`
- Create: mehrere Dateien unter `80_Knowledge/Patterns/` (erwartet: `Spec-Grilling.md`, `CONTEXT-Glossar.md`, `Handoff-Doc.md`, `Skill-Call-Hierarchie.md`, `Klein-und-komposierbar.md`, `One-File-per-Failure-Mode.md`)
- Create: `80_Knowledge/Vergleiche/Workflow-Frameworks.md`
- Modify: `80_Knowledge/Index.md`

**Interfaces:**
- Consumes: Skill `30_Skills/local/knowledge-ingest/SKILL.md` (Task 2) — diesen Skill lesen und Schritt für Schritt befolgen; Templates aus `80_Knowledge/README.md` (Task 1).
- Produces: Patterns mit exakt diesen Dateinamen (Task 6 ergänzt sie): `Spec-Grilling.md`, `CONTEXT-Glossar.md`, `Handoff-Doc.md`, `Skill-Call-Hierarchie.md`, `Klein-und-komposierbar.md`, `One-File-per-Failure-Mode.md`; außerdem `Vergleiche/Workflow-Frameworks.md`.

**Quelltext (Originaltext des Tweets, vom Nutzer eingefügt — als Inhalt der Source-Notiz verwenden):**

> Vox (@Voxyz_ai), 2026-07-10:
>
> the most irreplaceable layer of the agent stack is now a folder of markdown files.
>
> best reference is mattpocock's skills repo: one md folder straight from his .claude directory, 164k stars. [Anm.: WebFetch-Abruf vom 2026-07-11 nennt 16.400 Stars — Zahl als unsicher kennzeichnen]
>
> 1. /grill-me interrogates you until the spec is clear. /tdd locks in red-green-refactor. /improve-codebase-architecture treats codebase rot, he recommends running it every few days. one file per failure mode.
> 2. CONTEXT.md holds the project's shared vocabulary. once the glossary exists, a bug that took a full sentence to describe (a course lesson getting materialized into the file system) shrinks to one term: materialization cascade. the agent spends fewer thinking tokens.
> 3. /handoff compacts the current conversation into a handoff doc, the next agent continues in place. /wayfinder turns work too big for one session into a map of tickets to chew through.
> 4. the md files have a call hierarchy. user-invoked skills orchestrate, model-invoked skills hold the discipline. an orchestrator may call the discipline files, never another orchestrator. a dependency architecture growing out of plain text files.
> 5. npx skills@latest add mattpocock/skills. pick the skills, pick which agents to install them on, 30 seconds in. installs like an npm package.
> 6. the readme sets the boundary up front: skills stay small, composable, easy to hack. control of the process stays with you.

- [ ] **Step 1: Skill und Schema lesen**

`30_Skills/local/knowledge-ingest/SKILL.md` und `80_Knowledge/README.md` vollständig lesen. Der Skill ist die Prozessvorschrift für die folgenden Schritte; bei Konflikt zwischen diesem Task und dem Skill gilt der Skill (das IST der Abnahmetest).

- [ ] **Step 2: Source-Notiz anlegen**

`80_Knowledge/Sources/2026-07-10-voxyz-mattpocock-skills.md` nach Template anlegen. Frontmatter: `url: https://x.com/Voxyz_ai/status/2075603005143924959`, `autor: "@Voxyz_ai (Vox)"`, `datum: 2026-07-10`, `erfasst:` heutiges Datum, `typ: tweet`. Inhalt: obiger Originaltext. Kernaussagen-Liste mit Wiki-Links auf die in Step 3 anzulegenden Patterns.

- [ ] **Step 3: Pattern-Notizen anlegen**

Nach Template, je mit Zweck/Funktionsweise/Vor-/Nachteilen/Wann-einsetzen, einem Beleg-Eintrag auf `[[2026-07-10-voxyz-mattpocock-skills]]` (Beleg-Typ zunächst `meinung`) und Konfidenz `meinung`:

1. `Spec-Grilling.md` — Agent verhört Nutzer vor Umsetzung bis Spec klar ist (/grill-me; verwandt: gstack /office-hours, superpowers brainstorming — siehe `external_repos/INDEX.md`).
2. `CONTEXT-Glossar.md` — geteiltes Projekt-Vokabular in CONTEXT.md; komprimiert Kommunikation (Beispiel „materialization cascade“), spart Thinking-Tokens.
3. `Handoff-Doc.md` — Konversation wird in Übergabe-Dokument kompaktiert, nächster Agent macht nahtlos weiter (/handoff; verwandt: planning-with-files, GSD STATE.md).
4. `Skill-Call-Hierarchie.md` — user-invoked Skills orchestrieren, model-invoked Skills tragen die Disziplin; Orchestrator ruft nie Orchestrator.
5. `Klein-und-komposierbar.md` — Skills klein, komponierbar, leicht hackbar halten; Prozesskontrolle bleibt beim Menschen; Gegenposition zu schweren Frameworks (GSD, BMAD) als Spannung eintragen.
6. `One-File-per-Failure-Mode.md` — pro typischem Fehlermodus des Agenten genau eine Skill-Datei (tdd, grill-me, improve-codebase-architecture als Beispiele).

- [ ] **Step 4: Repo-Verifikation durchführen**

`external_repos/mattpocock/skills/` liegt lokal vor (siehe `external_repos/INDEX.md`). Stichproben: Existiert eine Skill-Struktur mit den genannten Skills (grill-me, tdd, handoff, wayfinder)? Bestätigt das README „small, composable“? Prüfbefehl-Beispiel:

Run: `Get-ChildItem external_repos/mattpocock/skills -Recurse -Filter SKILL.md | Select-Object -ExpandProperty FullName`

Bestätigte Aussagen in den betroffenen Patterns auf Beleg-Typ `verifiziert` heben (Beleg-Zeile ergänzen: `YYYY-MM-DD · external_repos/mattpocock/skills/<pfad> · verifiziert — …`), Konfidenz entsprechend. Nicht Bestätigbares (z.B. Star-Zahl) als offene Frage/Unsicherheit in der Source-Notiz belassen.

- [ ] **Step 5: Vergleichs-Notiz anlegen**

`80_Knowledge/Vergleiche/Workflow-Frameworks.md` nach Template. Zeilen der Tabelle aus dem Wissen in `external_repos/INDEX.md` speisen (mindestens: mattpocock/skills, Superpowers, GSD Core, gstack, addyosmani/agent-skills, Squad; Spalte Quelle/Repo verweist auf `external_repos/INDEX.md`-Einträge). Empfehlungsteil: erste vorsichtige Empfehlungen mit Begründung, offene Fragen explizit.

- [ ] **Step 6: Index aktualisieren**

`80_Knowledge/Index.md`: die sechs Patterns und den Vergleich mit je einem Einzeiler eintragen, Platzhalterzeilen `_(noch keine …)_` entfernen.

- [ ] **Step 7: Verifizieren**

Run: `(Get-ChildItem 80_Knowledge/Patterns -Filter *.md | Measure-Object).Count`
Expected: `6`

Run: `Select-String -Path 80_Knowledge/Patterns/*.md -Pattern '## Belege' | Measure-Object | Select-Object -ExpandProperty Count`
Expected: `6`

Zusätzlich lesen: Jedes Pattern hat mindestens einen Beleg mit Wiki-Link auf die Source; `Skill-Call-Hierarchie.md` oder andere verifizierte Patterns tragen Konfidenz `verifiziert`; das Diff-Resümee wurde ausgegeben.

- [ ] **Step 8: Commit**

```powershell
git add 80_Knowledge
git commit -m @'
Knowledge-System: Initialbefuellung aus Vox-Tweet zu mattpocock/skills

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

---

### Task 6: Initialbefüllung Tweet 2 (Will Ness zu Wayfinder) — Abnahmetest „Ergänzung“

**Files:**
- Create: `80_Knowledge/Sources/2026-07-09-n3sonline-wayfinder.md`
- Create: `80_Knowledge/Patterns/Task-basierte-Steuerung.md`
- Modify: `80_Knowledge/Patterns/Handoff-Doc.md` (oder verwandte, je nach Zuordnung), `80_Knowledge/Patterns/Klein-und-komposierbar.md`
- Modify: `80_Knowledge/Vergleiche/Workflow-Frameworks.md`, `80_Knowledge/Index.md`

**Interfaces:**
- Consumes: Skill `knowledge-ingest` (Task 2); vorhandene Patterns aus Task 5 (exakte Dateinamen siehe dort).
- Produces: abgeschlossene Initialbefüllung gemäß Spec-Abschnitt „Initialbefüllung (zugleich Abnahmetest)“.

**Quelltext (Originaltext des Tweets, vom Nutzer eingefügt):**

> WILL NESS (@N3sOnline), 2026-07-09:
>
> Day 1 of using @mattpocockuk's Wayfinder. I have a lot to say, but I think this sums it up:
>
> 1. Your agent can now be both a PM and a developer.
> 2. For the last year or so, every paradigm has been some form of Research -> Plan -> Implement. This is different, it's more like:
>    Set Goal -> Task -> Adjust -> Task -> Adjust -> Task -> Adjust -> ...
>    Where "Task" can be to research, to plan/grill, to implement, or to prototype.
>    In hindsight, this flexibility is obviously needed for real work.
> 3. The best solution I have used for 'sizing' tasks for a single agent session.
> 4. A lot of other frameworks are HUGE. This one is small.

- [ ] **Step 1: Skill befolgen, Source anlegen**

`30_Skills/local/knowledge-ingest/SKILL.md` befolgen. Source: `80_Knowledge/Sources/2026-07-09-n3sonline-wayfinder.md`, Frontmatter: `url: https://x.com/N3sOnline/status/2075260831500312947`, `autor: "@N3sOnline (WILL NESS)"`, `datum: 2026-07-09`, `erfasst:` heutiges Datum, `typ: tweet`.

- [ ] **Step 2: Neues Pattern anlegen**

`80_Knowledge/Patterns/Task-basierte-Steuerung.md`: iterative Steuerung „Set Goal → Task → Adjust → …“ statt linearem „Research → Plan → Implement“; Task kann Recherche, Planung/Grilling, Implementierung oder Prototyp sein; Agent als PM+Developer; Stärke: Task-Sizing für einzelne Agent-Sessions. Beleg: `[[2026-07-09-n3sonline-wayfinder]]`, Typ `meinung`, Konfidenz `meinung`. Verwandte Patterns: `[[Spec-Grilling]]`, `[[Handoff-Doc]]`, `[[Klein-und-komposierbar]]`. Spannung eintragen: linearer Phasen-Ansatz (GSD, Superpowers-Kette) vs. iteratives Task-Modell — Trade-off Planbarkeit/Disziplin vs. Flexibilität.

- [ ] **Step 3: Bestehende Patterns ergänzen (der eigentliche Test)**

- `Klein-und-komposierbar.md`: neuer Beleg (Will Ness: „A lot of other frameworks are HUGE. This one is small.“) → damit zwei unabhängige Quellen: Konfidenz auf `mehrfach-belegt` heben (sofern nicht schon `verifiziert`; Belege-Liste in jedem Fall ergänzen).
- Prüfen, ob weitere Aussagen bestehende Patterns berühren (z.B. Task-Sizing ↔ `Handoff-Doc.md`/Session-Grenzen) und dort datiert ergänzen. Nichts löschen oder umschreiben.

- [ ] **Step 4: Vergleich + Index aktualisieren**

`Workflow-Frameworks.md`: Wayfinder-Zeile ergänzen/anreichern (iteratives Task-Modell, klein), Stand-Datum aktualisieren, Empfehlungsteil ggf. anpassen. `Index.md`: `Task-basierte-Steuerung` eintragen.

- [ ] **Step 5: Verifizieren**

Run: `(Get-ChildItem 80_Knowledge/Patterns -Filter *.md | Measure-Object).Count`
Expected: `7`

Run: `Select-String -Path 80_Knowledge/Patterns/Klein-und-komposierbar.md -Pattern 'n3sonline'`
Expected: mindestens ein Treffer (neuer Beleg eingetragen)

Zusätzlich lesen: Diff-Resümee ausgegeben; Spannung „linear vs. iterativ“ steht in `Task-basierte-Steuerung.md`; keine bestehende Beleg-Zeile wurde entfernt (`git diff HEAD~1 -- 80_Knowledge/Patterns` zeigt nur Ergänzungen in bestehenden Dateien).

- [ ] **Step 6: Commit**

```powershell
git add 80_Knowledge
git commit -m @'
Knowledge-System: Zweiter Ingest (Wayfinder-Tweet), Ergaenzungs-Pfad getestet

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```
