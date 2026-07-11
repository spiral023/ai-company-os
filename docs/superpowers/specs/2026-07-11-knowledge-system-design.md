# Design: Selbstverbesserndes Knowledge-System für Arbeitsweisen-Wissen

**Datum:** 2026-07-11
**Status:** Freigegeben von Philipp (Brainstorming-Session)
**Ziel-Repo:** ai-company-os

## Problem

Philipp sammelt laufend Informationen über KI-Arbeitsweisen, hauptsächlich zum Thema Coding Agents — Tweets, GitHub-Repos, Artikel über Skills, Agent-Workflows und Frameworks (z.B. mattpocock/skills, Wayfinder, Superpowers, GSD). Bisher gibt es dafür keinen Ort, an dem dieses Wissen strukturiert wächst. `external_repos/INDEX.md` beschreibt Repos, `50_Memory/` hält eigene Entscheidungen — aber Erkenntnisse über **Arbeitsweisen selbst** (Sinn, Zweck, Vor- und Nachteile, Trade-offs) haben keine Heimat und verbessern sich nicht mit neuen Eingaben.

## Kernanforderungen

1. Eingabe per Tweet-Text, x.com-URL (WebFetch funktioniert für einzelne Tweets, verifiziert am 2026-07-11) oder formlosem Text.
2. Neue Infos machen alte nicht irrelevant: nichts wird gelöscht, Wissen wird ergänzt; Widersprüche werden als Spannungen festgehalten, nicht wegaufgelöst.
3. Auto-Synthese: Der Agent arbeitet Eingaben selbstständig ein und zeigt am Ende ein Diff-Resümee.
4. Selbstverbesserung über die Eingabe hinaus: Vergleichsseiten, Pflege-Lauf, Verifikation gegen geklonte Repos.
5. Obsidian-kompatibel: reine Markdown-Dateien, Wiki-Links, keine Plugin-Abhängigkeiten (gemäß AGENTS.md).

## Entschiedener Ansatz

Schlankes eigenes Markdown-System (Option A). Verworfen: arscontexta-Framework (fremde Struktur über durchdachtes Repo-Schema) und Graph-first (JSON statt handpflegbarem Markdown; graphify bleibt als spätere Zusatz-Visualisierung möglich).

## Architektur

### Ordnerstruktur `80_Knowledge/`

```
80_Knowledge/
├── Index.md          ← Einstieg: Liste aller Patterns und Vergleiche mit Einzeilern
├── README.md         ← Regeln des Systems: Schema, Konfidenz-Modell, Invarianten
├── Sources/          ← unveränderliches Quellen-Archiv
│   └── YYYY-MM-DD-<autor>-<slug>.md
├── Patterns/         ← lebende Synthese-Notizen, eine pro Arbeitsweise
│   └── <Pattern-Name>.md
└── Vergleiche/       ← Verdichtung mehrerer Patterns/Frameworks zu Empfehlungen
    └── <Themenfeld>.md
```

### Source-Notiz (unveränderlich)

Frontmatter: `url`, `autor`, `datum` (Original-Veröffentlichung), `erfasst` (Ingest-Datum), `typ` (tweet | artikel | repo | video | notiz).
Body: Originaltext (bei URL-Abruf: das Abruf-Ergebnis, gekennzeichnet als solches), danach extrahierte Kernaussagen als Liste, jede mit Wiki-Link auf das Pattern, in das sie eingeflossen ist.
Invariante: Nach dem Anlegen wird eine Source-Notiz nicht mehr inhaltlich verändert (nur Pattern-Links dürfen ergänzt werden, wenn spätere Läufe weitere Aussagen zuordnen).

### Pattern-Notiz (lebend)

Feste Abschnitte:

- **Zweck** — welches Problem löst die Arbeitsweise
- **Funktionsweise** — wie sie konkret abläuft
- **Vorteile** / **Nachteile & Grenzen**
- **Wann einsetzen, wann nicht**
- **Belege** — datierte Liste, je Eintrag: Datum, Quelle als `[[Source-Link]]`, Beleg-Typ
- **Spannungen & offene Fragen** — Widersprüche zwischen Quellen, explizit als Trade-off formuliert
- **Verwandte Patterns** — `[[Wiki-Links]]`
- **Konfidenz** — abgeleitet aus den Belegen (siehe Modell)

Invarianten: Nichts löschen. Überholte Aussagen bekommen einen datierten Vermerk („bis YYYY-MM üblich, seitdem …"). Jede inhaltliche Aussage muss mindestens einem Beleg zuordenbar sein.

### Konfidenz-Modell

Drei Beleg-Typen, aufsteigend gewichtet:

1. `meinung` — einzelner Tweet/Blogpost, eine Person
2. `mehrfach-belegt` — mehrere voneinander unabhängige Quellen
3. `verifiziert` — im geklonten Repo (`external_repos/`) nachgeprüft oder selbst getestet

Konfidenz der Pattern-Notiz = höchster erreichter Beleg-Typ, ausgewiesen im Konfidenz-Abschnitt.

### Vergleichs-Notiz

Pro Themenfeld (z.B. `Workflow-Frameworks.md`): Vergleichstabelle der relevanten Frameworks/Patterns, danach Empfehlungsteil („wann was, für welchen Projekttyp"). Wird bei jeder Eingabe aktualisiert, die eines der verglichenen Themen berührt. Speist sich auch aus `external_repos/INDEX.md`.

## Skills

### `30_Skills/local/knowledge-ingest/SKILL.md`

Trigger: `/knowledge-ingest <url|text>` oder formlos geposteter Tweet-Link/-Text.

Ablauf:

1. Quelle beschaffen: bei URL WebFetch; schlägt der Abruf fehl oder wirkt unvollständig, Philipp um eingefügten Originaltext bitten. Eingefügter Text hat Vorrang vor Abruf (verlustfrei).
2. Source-Notiz anlegen (Duplikat-Check über URL/Inhalt gegen `Sources/`).
3. Kernaussagen extrahieren.
4. Abgleich gegen `80_Knowledge/Index.md`: bestehende Patterns ergänzen, neue anlegen (Schwelle: ein Konzept bekommt eine eigene Notiz, sobald es benennbar und wiederverwendbar ist).
5. Widersprüche zu Bestandswissen als Spannung im betroffenen Pattern notieren.
6. Repo-Verifikation: Liegt das erwähnte Repo in `external_repos/`, Behauptungen dort stichprobenartig nachprüfen und Beleg-Typ ggf. auf `verifiziert` heben. Liegt es nicht vor, optional Download gemäß AGENTS.md-Prozess vorschlagen.
7. Betroffene Vergleichs-Notizen aktualisieren, `Index.md` aktualisieren.
8. Diff-Resümee ausgeben: archiviert / ergänzt (+n Belege) / neu angelegt / Spannungen / offene Fragen.

Unklare Zuordnungen: als Frage in `00_Inbox/Fragen_an_Philipp.md` eintragen, nicht raten.

### `30_Skills/local/knowledge-review/SKILL.md`

Trigger: `/knowledge-review`, zusätzlich als Punkt im `20_Workflows/Wochenreview.md`.

Ablauf: Duplikat-/Merge-Kandidaten unter Patterns finden (Merge nur mit Philipp-OK) → Patterns ohne Belege der letzten ~90 Tage als „zu prüfen" markieren → offene Spannungen gegen inzwischen verfügbare Repos/Quellen prüfen → Konfidenzen neu ableiten → `Index.md` und Vergleichs-Notizen auf Konsistenz prüfen → kurzer Bericht.

## Integration

- Beide Skills in `30_Skills/registry.yaml` eintragen (lokal, Trust: eigen).
- `AGENTS.md`: kurzer Abschnitt „Knowledge-System" (Zweck, Trigger, Verweis auf `80_Knowledge/README.md` für Details — Root-Datei bleibt schlank).
- `external_repos/INDEX.md` bleibt unverändert zuständig für Repo-Metadaten; Patterns verlinken dorthin.

## Initialbefüllung (zugleich Abnahmetest)

Die zwei vorliegenden Tweets durch den fertigen Skill verarbeiten:

1. Vox (@Voxyz_ai, 2026-07-10) zu mattpocock/skills
2. Will Ness (@N3sOnline, 2026-07-09) zu Wayfinder

Erwartetes Ergebnis: 2 Sources, ca. 6 Patterns (Spec-Grilling, CONTEXT.md-Glossar, Handoff-Doc, Task-basierte-Steuerung, Skill-Call-Hierarchie, Klein-und-komposierbar), 1 Vergleichs-Notiz `Workflow-Frameworks.md`, aktualisierter Index, Diff-Resümee. Repo-Verifikation greift, da `external_repos/mattpocock/skills/` bereits geklont ist.

## Bewusst weggelassen (YAGNI)

- Kein Graph/Dashboard im ersten Wurf (graphify kann Markdown später jederzeit visualisieren).
- Keine Python-Scripts/Validatoren (erst wenn Pflege von Hand mehr als zweimal nervt, gemäß AGENTS.md-Script-Regel).
- Kein eigenes Tag-System über Wiki-Links hinaus.
- Beleg-Typ „selbst getestet" als eigener Workflow (Anbindung an `50_Memory/Lessons_Learned`) — späterer Ausbau, im Konfidenz-Modell aber bereits vorgesehen (`verifiziert`).
