# Matt Pocock Skills Guide Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Einen belegbaren, deutschsprachigen Praxis-Guide erstellen, der Entwicklern die situationsgerechte Nutzung von `mattpocock/skills` mit Schwerpunkt Wayfinder erklärt.

**Architecture:** Tweet-Texte werden zuerst als unveränderliche Source-Notizen erfasst und anschließend in bestehende Pattern-Notizen synthetisiert. Der Guide bildet darauf eine handlungsorientierte Nutzungsschicht; Index und Framework-Vergleich sorgen für Auffindbarkeit, der bestehende Knowledge-Validator sichert Schema und Links.

**Tech Stack:** Markdown, Obsidian-Wikilinks, Mermaid, Python-Knowledge-Validator, lokales Referenz-Repo `external_repos/mattpocock/skills`

---

## Dateistruktur

- `80_Knowledge/Sources/2026-07-13-mattpocock-handoff-to-teach.md`: Lern-Handoff aus einer Grilling-Session.
- `80_Knowledge/Sources/2026-07-11-mattpocock-wayfinder-to-implementation.md`: empfohlener Coding-Lifecycle nach Wayfinder.
- `80_Knowledge/Sources/2026-07-08-mattpocock-custom-issue-tracker.md`: Anpassung an beliebige programmatisch erreichbare Issue-Tracker.
- `80_Knowledge/Sources/2026-07-08-mattpocock-skills-v1-1.md`: Release-Ankündigung und Lifecycle-Skills.
- `80_Knowledge/Sources/2026-07-06-mattpocock-writing-great-skills-beyond-skills.md`: Skill-Writing-Prinzipien für agentenlesbare Dokumente.
- `80_Knowledge/Sources/2026-07-06-nightmoon-wayfinder.md`: unabhängiger Wayfinder-Erfahrungsbericht.
- `80_Knowledge/Patterns/Handoff-Doc.md`: Lern-Handoff ergänzen.
- `80_Knowledge/Patterns/Task-basierte-Steuerung.md`: Wayfinder-Grenze und Übergang zur Delivery ergänzen.
- `80_Knowledge/Patterns/Klein-und-komposierbar.md`: konfigurierbares Tracker-Backend und nicht-codierende Nutzung ergänzen.
- `80_Knowledge/Patterns/One-File-per-Failure-Mode.md`: Architekturpflege als wiederkehrende Routine ergänzen.
- `80_Knowledge/Patterns/Skill-Call-Hierarchie.md`: Release-Stand und unterstützende Skills ergänzen.
- `80_Knowledge/Guides/Matt-Pocock-Skills-Praxisguide.md`: zentraler, handlungsorientierter Guide.
- `80_Knowledge/Vergleiche/Workflow-Frameworks.md`: Wayfinder-Empfehlung und Grenzen aktualisieren.
- `80_Knowledge/Index.md`: Guide und neue beziehungsweise ergänzte Wissenseinstiege verlinken.
- `00_Inbox/Fragen_an_Philipp.md`: nicht belegbare anonyme Aussage zu `/improve-codebase-architecture` als Rückfrage erfassen, falls dort noch kein entsprechender Eintrag existiert.

### Task 1: Quelleninventar und Source-Notizen

- [ ] **Step 1: Duplikate und bestehende Evidenz prüfen**

Run:

```powershell
rg -n -i "handoff.*teach|wayfinder.*to-spec|custom issue tracker|v1.1|writing-great-skills|nightmoon" 80_Knowledge/Sources 80_Knowledge/Patterns
```

Expected: Bereits vorhandene Quellen werden sichtbar; die sechs oben genannten Source-Dateien fehlen oder werden aus der Dateiliste entfernt, falls ein inhaltliches Duplikat existiert.

- [ ] **Step 2: Sechs Source-Notizen nach dem Template anlegen**

Jede Datei enthält Frontmatter mit `url: keine`, Autor, Originaldatum, `erfasst: 2026-07-13`, `typ: tweet`, den vom Nutzer eingefügten Originaltext und Kernaussagen mit Wikilinks. Der relative Zeitbezug „4 Std.“ wird als am Ingest-Tag veröffentlicht dokumentiert; diese Datumsableitung wird in der Notiz transparent vermerkt.

- [ ] **Step 3: Anonyme Aussage als offene Frage erfassen**

In `00_Inbox/Fragen_an_Philipp.md` ergänzen: Autor, Datum und Originaltext beziehungsweise URL des Nutzers, der `/improve-codebase-architecture` liebt, fehlen; ohne diese Angaben wird keine Source-Notiz angelegt.

- [ ] **Step 4: Source-Dateien gezielt prüfen**

Run:

```powershell
rg -n "^url:|^autor:|^datum:|^erfasst:|^typ:|^## Inhalt|^## Kernaussagen" 80_Knowledge/Sources/2026-07-{06,08,11,13}-*.md
```

Expected: Jede neue Source enthält vollständiges Frontmatter sowie Inhalt und Kernaussagen.

### Task 2: Aussagen gegen das Repository verifizieren

- [ ] **Step 1: Lifecycle- und Wayfinder-Regeln lesen**

Read:

```text
external_repos/mattpocock/skills/README.md
external_repos/mattpocock/skills/CHANGELOG.md
external_repos/mattpocock/skills/skills/engineering/wayfinder/SKILL.md
external_repos/mattpocock/skills/skills/engineering/to-spec/SKILL.md
external_repos/mattpocock/skills/skills/engineering/to-tickets/SKILL.md
external_repos/mattpocock/skills/skills/engineering/implement/SKILL.md
external_repos/mattpocock/skills/skills/engineering/code-review/SKILL.md
```

- [ ] **Step 2: Unterstützende und konfigurierende Skills lesen**

Read:

```text
external_repos/mattpocock/skills/skills/engineering/setup-matt-pocock-skills/SKILL.md
external_repos/mattpocock/skills/skills/engineering/improve-codebase-architecture/SKILL.md
external_repos/mattpocock/skills/skills/engineering/research/SKILL.md
external_repos/mattpocock/skills/skills/engineering/prototype/SKILL.md
external_repos/mattpocock/skills/skills/productivity/handoff/SKILL.md
external_repos/mattpocock/skills/skills/productivity/teach/SKILL.md
external_repos/mattpocock/skills/skills/productivity/writing-great-skills/SKILL.md
```

- [ ] **Step 3: Evidenz-Inventar erstellen**

Vor dem Schreiben intern jede tragende Guide-Aussage einem Tweet und/oder konkreten Repo-Pfad zuordnen. Nicht bestätigte Aussagen werden als Erfahrungsbericht oder Ableitung formuliert, nicht als Repo-Funktion.

### Task 3: Bestehende Patterns ergänzen

- [ ] **Step 1: Fachlich passende Abschnitte ergänzen**

Neue Erkenntnisse werden datiert ergänzt; bestehender Text und bestehende Beleg-Zeilen bleiben unverändert. Je Pattern kommen nur Aussagen hinzu, die dessen bestehenden Zweck direkt erweitern.

- [ ] **Step 2: Repo-Belege ergänzen**

Für bestätigte Lifecycle-, Tracker-, Handoff-, Teach- und Architekturpflege-Aussagen jeweils eine neue Beleg-Zeile im Format aus `80_Knowledge/README.md` ergänzen.

- [ ] **Step 3: Spannungen sichtbar machen**

In `Task-basierte-Steuerung.md` festhalten: Wayfinder kann zwar einen gesamten nicht-codierenden Prozess tragen, für Coding empfiehlt Matt Pocock jedoch die Übergabe an Spec, Tickets und eine separate Implementierungsphase. Erfahrungsberichte über höhere Autonomie werden nicht als garantierte Skill-Eigenschaft formuliert.

### Task 4: Praxis-Guide schreiben

- [ ] **Step 1: Guide mit klarer Kurzfassung beginnen**

Die Datei `80_Knowledge/Guides/Matt-Pocock-Skills-Praxisguide.md` beginnt mit Zweck, Zielgruppe, einer Fünf-Zeilen-Kurzfassung und einer Evidenzlegende.

- [ ] **Step 2: Setup und Auswahlbaum dokumentieren**

Installation über `npx skills@latest add mattpocock/skills`, projektspezifisches Setup und einen Mermaid-Entscheidungsbaum aufnehmen. Der Guide erklärt ausdrücklich, dass user-invoked Skills orchestrieren und model-invoked Skills Disziplin bereitstellen.

- [ ] **Step 3: Coding-Lifecycle und Wayfinder erklären**

Den Fluss `wayfinder → to-spec → to-tickets → implement → code-review` als Mermaid-Flowchart darstellen. Wayfinder als Fog-of-War-Schleife mit Investigation Tickets, Session-Sizing, Research- und Prototype-Abzweigungen erklären; die Übergabe zur Delivery klar markieren.

- [ ] **Step 4: Kleine Aufgaben und Sonderfälle ergänzen**

Direkte Wege für kleine Änderungen, Bugs, reine Recherche, Prototyping, nicht-codierende Vorhaben, Lern-Handoffs und Session-Wechsel dokumentieren.

- [ ] **Step 5: Qualitätsroutine und Rezepte ergänzen**

`grill-with-docs`, `CONTEXT.md`, TDD, Debugging, Code Review und `/improve-codebase-architecture` in eine Wartungsroutine einordnen. Konkrete Befehlsrezepte und erwartete Artefakte pro Schritt aufnehmen.

- [ ] **Step 6: Fehlanwendungen und Grenzen dokumentieren**

Mindestens diese Fehler behandeln: Wayfinder als Standard für jede Kleinigkeit; Exploration und Delivery vermischen; große Tickets statt Session-großer Investigation Tickets; Handoff-Dokumente als Duplikat vorhandener Artefakte; blindes Vertrauen in Erfahrungsberichte; Tracker-Anbindung ohne Setup.

### Task 5: Auffindbarkeit und Vergleich aktualisieren

- [ ] **Step 1: Guide im Knowledge-Index verlinken**

Unter einer neuen Überschrift `## Guides` einen Einzeiler zu `[[Matt-Pocock-Skills-Praxisguide]]` ergänzen, ohne bestehende Index-Einträge umzuschreiben.

- [ ] **Step 2: Workflow-Vergleich aktualisieren**

Stand auf `2026-07-13` setzen und Wayfinder um den empfohlenen Übergang zu Spec/Tickets/Implementierung sowie die konfigurierbare Tracker-Anbindung ergänzen.

### Task 6: Validierung und Abschlussprüfung

- [ ] **Step 1: Knowledge-Validator ausführen**

Run:

```powershell
python 70_Scripts/validate_knowledge.py
```

Expected: Exit-Code 0 und keine Validierungsfehler.

- [ ] **Step 2: Mermaid- und Link-Sanity-Check ausführen**

Run:

```powershell
rg -n '^```mermaid|^```$|\[\[' 80_Knowledge/Guides/Matt-Pocock-Skills-Praxisguide.md
```

Expected: Jeder Mermaid-Block besitzt einen schließenden Fence; Wikilinks zeigen auf vorhandene oder durch diese Aufgabe neu angelegte Knowledge-Dateien.

- [ ] **Step 3: Eigene Änderungen isoliert prüfen**

Run:

```powershell
git diff -- 00_Inbox/Fragen_an_Philipp.md 80_Knowledge/Sources 80_Knowledge/Patterns 80_Knowledge/Guides 80_Knowledge/Index.md 80_Knowledge/Vergleiche/Workflow-Frameworks.md
```

Expected: Nur aufgabenbezogene Ergänzungen; keine Löschungen bestehender Pattern-Aussagen und keine unbeabsichtigten Änderungen an fremden Worktree-Inhalten.

- [ ] **Step 4: Planfortschritt markieren und aufgabenbezogen committen**

Nur sicher der Aufgabe zuordenbare Dateien stagen. Bereits vor der Aufgabe vorhandene, nicht zugehörige Änderungen in `80_Knowledge/Index.md` oder `Workflow-Frameworks.md` dürfen nicht versehentlich als eigene Arbeit committed werden.

