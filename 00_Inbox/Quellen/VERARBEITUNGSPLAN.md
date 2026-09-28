# Verarbeitungsplan: vibedeck-Übernahme

**Stand:** 2026-08-09 · **Fortschritt:** 41 von 81 Quellen erledigt (39 verarbeitet, 2 ignoriert)

Hält den Zwischenstand fest, damit ein späterer Lauf nahtlos fortsetzt. Nach vollständiger Abarbeitung kann die Datei gelöscht werden.

## Kennzahlen

| | Anzahl |
|---|---|
| Quellen in der Inbox | 81 |
| davon `status: neu` | **40** |
| davon `status: verarbeitet` | 39 |
| davon `status: ignoriert` | 2 |
| Bilder lokal | 188 |
| Source-Notizen in `80_Knowledge/Sources/` | 83 |
| Patterns | 40 (2 neu in Schritt 1: Freiheitsgrad-nach-Aufgaben-Fragilitaet, Blockierende-Task-Abhaengigkeiten; 2 neu in Schritt 2: Hook-erzwungene-Skill-Aktivierung, MCP-Code-Execution-statt-Tool-Definitionen; 3 neu in Schritt 3: Trainingsdaten-Dichte-als-Stack-Kriterium, Spec-Ordner-pro-Feature, Skill-aus-Demonstration-statt-Beschreibung; 3 neu in Schritt 4: Skill-Schwellenwert-institutionelles-Wissen, Claude-als-Lernwerkzeug, Hook-Entscheidungstyp-nach-Pruefbarkeit; 1 neu im Effizienz-Testlauf: Screenshot-als-Spezifikationsmedium) |
| Verbrauch 2 Subagents (10 Quellen, 1. Lauf) | ~363k Tokens, 121 Tool-Calls, ~18,5 Min. Laufzeit gesamt |
| Verbrauch 5 Subagents (5 Paare, Schritt 1, parallel) | ~757k Tokens, 238 Tool-Calls, ~7,5 Min. Laufzeit (längster Einzellauf; parallel statt sequenziell) |
| Verbrauch 5 Subagents (2 Paare + 3 Einzelquellen, Schritt 2, parallel) | ~610k Tokens, 160 Tool-Calls, ~7 Min. Laufzeit (längster Einzellauf; parallel statt sequenziell) |
| Verbrauch 5 Subagents (5 Einzelquellen, Schritt 3, parallel) | ~608k Tokens, 171 Tool-Calls, ~6,3 Min. Laufzeit (längster Einzellauf; parallel statt sequenziell) |
| Verbrauch 5 Subagents (5 Einzelquellen, Schritt 4, parallel) | ~552k Tokens, 140 Tool-Calls, ~6,2 Min. Laufzeit (längster Einzellauf; parallel statt sequenziell) |
| Verbrauch 1 Subagent mit überarbeitetem Auftrag (Common-Workflows, Einzeltest 2026-08-09) | ~73k Tokens, 9 Tool-Calls, ~3,8 Min. Laufzeit — zum Vergleich: Schritt 1–4 lagen bei ~110-150k Tokens/Quelle |

## Erledigt

- **70 vibedeck-Artikel importiert** als Sekundärquellen (`sekundaerquelle: true`, `quelle: vibedeck`) samt **131 Bildern**. Die Bildpositionen im Text stammen aus vibedeck und wurden nicht neu gesetzt — dort standen sie bereits an der inhaltlich passenden Stelle; das Skript schreibt nur die Pfade um. Skript: `70_Scripts/import_vibedeck_knowledge.py`.
- **19 Artikel übersprungen**, deren `sourceURL` bereits als Source-Notiz existiert. Die Liste erzeugt das Skript erneut, wenn man `--skip-vorhandene-urls` weglässt.
- **10 Primärquellen nachgeholt**: 7 über die X-API, 1 Blogartikel (Boris Tane) per URL-Ingest, 2 waren bereits vollständig durch die vibedeck-Fassung abgedeckt.
- **3 Quellen verarbeitet**: Cerebras (GPT-5.6-Modellwahl) sowie das Paar ClaudeDevs Modell/Effort (Primär + Sekundär zu einer Notiz verschmolzen). Sie dienen als Qualitätsmuster für die übrigen.
- **2 neue Patterns** aus diesen Quellen: `Modell-Eskalation-von-guenstig-nach-teuer` (inzwischen `mehrfach-belegt`) und `Advisor-Agent-gegen-Drift`.
- **Schritt 1 (5×1 Sonnet-Subagents, parallel, 2026-08-05):** die 5 kuratierten Primär/Sekundär-Paare (tempoimmaterial, jarrodwatts, nummanali, jason-zhou, pdrmnvd) zu je einer Source-Notiz verschmolzen, alle 10 zugehörigen Inbox-Dateien auf `verarbeitet` gesetzt. Zentrale Konsolidierung durch den Hauptagenten: 2 neue Patterns angelegt (`Freiheitsgrad-nach-Aufgaben-Fragilitaet`, `Blockierende-Task-Abhaengigkeiten`), 2 weitere Pattern-Vorschläge der Subagents (`Rule-oder-Skill-Litmustest`, `Task-Registry-als-Shared-State`) bewusst **nicht** als eigene Patterns angelegt, sondern als Beleg-Zeilen in `Erweiterungs-Ebenen-Zuordnung` bzw. `Kontrollierte-Agent-Parallelisierung` verschmolzen, weil sie dieselbe Entscheidungsachse bzw. denselben Koordinationsmechanismus nur präzisierten. Insgesamt 11 Bestandspatterns um Beleg-Zeilen ergänzt (`Erweiterungs-Ebenen-Zuordnung`, `Skill-Qualitaet-durch-Trigger-und-Baseline-Evals`, `AGENTS-md-Onboarding-Design`, `Klein-und-komposierbar`, `Skill-Call-Hierarchie`, `Kontrollierte-Agent-Parallelisierung`, `Modell-Eskalation-von-guenstig-nach-teuer`, `Ralph-Loop-Frischer-Kontext-pro-Iteration`, `Kontext-Hygiene-Entscheidungsbaum`, `Spec-Grilling`, `Plan-first-mit-getrenntem-Review`). Validator danach: 44 Fehler, ausschließlich vorbestehend in unangetasteten Altdateien — keine neuen Fehler durch diesen Schritt.
- **Schritt 2 (5×1 Sonnet-Subagents, parallel, 2026-08-05):** die 2 restlichen Primär/Sekundär-Paare (daniel-san, boris-tane) sowie 3 Einzelquellen (eyad-khrais Level 2, meta-alchemist, sankalp) verarbeitet — alle 4 zugehörigen Paar-Inbox-Dateien und 3 Einzeldateien auf `verarbeitet` gesetzt. Beide Paare bestätigten erneut die Schritt-1-Korrektur: die Primärquellen waren vollständige X-Artikel, keine „nur Einzelpost“-Fälle. Zentrale Konsolidierung: 2 neue Patterns angelegt (`Hook-erzwungene-Skill-Aktivierung`, `MCP-Code-Execution-statt-Tool-Definitionen`), 1 weiterer Pattern-Vorschlag (`Plan-Mode-Granularitaet-in-Agent-Teams`) **nicht** als eigenes Pattern angelegt, sondern als Beleg-Zeile in `Kontrollierte-Agent-Parallelisierung` verschmolzen (spezifisches Verhaltensdetail eines dort bereits umfassend belegten Features, kein eigenständig benennbares Konzept). 2 Quellen (eyad-khrais Level 2, meta-alchemist) schlugen bewusst **keine** neuen Patterns vor, weil ihre Kernthemen im Bestand bereits präziser abgedeckt waren — als negative Vergleichsbeispiele bzw. Spannungshinweise trotzdem als Beleg-Zeilen eingearbeitet. `Action-Space-Design-nach-Modellfaehigkeit` per zweiter unabhängiger Quelle (sankalp) von `meinung` auf `mehrfach-belegt` hochgestuft. Insgesamt 9 Bestandspatterns um Beleg-Zeilen ergänzt (`Kontrollierte-Agent-Parallelisierung`, `Kontext-Hygiene-Entscheidungsbaum`, `Task-basierte-Steuerung`, `Plan-first-mit-getrenntem-Review`, `Great-Decoupling-Rollenverstaendnis`, `Handoff-Doc`, `AGENTS-md-Onboarding-Design`, `Action-Space-Design-nach-Modellfaehigkeit`, `Skill-Qualitaet-durch-Trigger-und-Baseline-Evals`). Validator danach: 45 Fehler — 44 vorbestehend unverändert, **+1 neu**, aber kein Inhaltsfehler: der bereits unter Offener Punkt 2 dokumentierte Validator-Bug greift jetzt zusätzlich bei der `Action-Space-Design-nach-Modellfaehigkeit`-Hochstufung auf `mehrfach-belegt`.
- **Schritt 3 (5×1 Sonnet-Subagents, parallel, 2026-08-05):** erster Schritt ohne kuratierte Paare — 5 Quellen frisch per `Select-String` ermittelt (dhruv1103, ashpreetbedi, elenakvcs, ai-edge, damien), alle eigenständige vibedeck-Sekundärquellen ohne erfasste Primärquelle im Bestand. Zentrale Konsolidierung: 3 neue Patterns angelegt (`Trainingsdaten-Dichte-als-Stack-Kriterium`, `Spec-Ordner-pro-Feature`, `Skill-aus-Demonstration-statt-Beschreibung`), alle drei bewusst mit Konfidenz `meinung` trotz Einzelquelle — Pattern-Neuanlage ab einer Quelle ist in diesem System etabliert, Konfidenz folgt der Beleglage, nicht die Existenz des Patterns. 2 Quellen (elenakvcs, damien) schlugen bewusst **keine** neuen Patterns vor, weil ihre Kernaussagen bereits mehrfach/verifiziert belegt bzw. generisches Webdesign-Wissen ohne KI-spezifische Mechanik waren. 12 Bestandspatterns um Beleg-Zeilen ergänzt (`Erweiterungs-Ebenen-Zuordnung`, `AGENTS-md-Onboarding-Design`, `TDD-als-Verifikationshebel`, `Testharness-als-staerkster-Hebel`, `Kontrollierte-Agent-Parallelisierung`, `Great-Decoupling-Rollenverstaendnis`, `Kontext-Hygiene-Entscheidungsbaum`, `Plan-first-mit-getrenntem-Review`, `Voice-Prompting-fuer-Kontextreichtum`, `Lovable-Prototyp-dann-lokaler-Handoff`, `Modell-Eskalation-von-guenstig-nach-teuer`, `Deny-Rules-statt-CLAUDE-md-Empfehlung`, `Klein-und-komposierbar`). Validator danach: 43 Fehler — netto **-2** gegenüber Schritt 2, weil `fix_typography.py` beim Bearbeiten von `TDD-als-Verifikationshebel.md` zwei vorbestehende gemischte Anführungszeichen in einer Alt-Beleg-Zeile mitkorrigiert hat (kein Inhaltsfehler, reiner Bonus-Fund); keine neuen Fehler durch diesen Schritt.

- **Schritt 4 (5×1 Sonnet-Subagents, parallel, 2026-08-05/09):** 5 Quellen frisch per `Select-String` ermittelt (hooeem, bcherny, unsloth/Kimi K2.5, aiedge Starter Pack, Anthropic Hooks-Guide), alle eigenständige vibedeck-Sekundärquellen ohne Primärquelle im Bestand — Paar-Prüfung explizit vorab durchgeführt, keine Treffer. **Erste Quelle, die als `ignoriert` eingestuft wurde, seit der Umstellung auf 5er-Schritte:** der Kimi-K2.5-Guide ist reiner Modell-Deployment-Stoff (GGUF-Quants, RAM-Anforderungen, llama.cpp-Flags) ohne Coding-Agent-Workflow-Bezug; der Subagent hat ihn sauber gegen die naheliegenden Kandidaten `Lokale-Modell-Umleitung-Muster` und `Trainingsdaten-Dichte-als-Stack-Kriterium` geprüft und beide begründet ausgeschlossen. Zentrale Konsolidierung: 3 neue Patterns angelegt (`Skill-Schwellenwert-institutionelles-Wissen`, `Claude-als-Lernwerkzeug`, `Hook-Entscheidungstyp-nach-Pruefbarkeit`), 17 Bestandspatterns um Beleg-Zeilen ergänzt. `CI-Agent-mit-Review-Gate` von `meinung` auf `mehrfach-belegt` hochgestuft — bislang nur durch eine einzige GitLab-Herstellerdoku belegt, jetzt zusätzlich durch einen Betriebsbericht zu GitHub Actions (Boris Chernys `@claude`-Tag-Action) und drei weitere Anthropic-Werkzeuge aus der hooeem-Quelle. Validator danach: 44 Fehler, **+1 gegenüber Schritt 3** — kein Inhaltsfehler, sondern erneut der unter Offener Punkt 2 dokumentierte Validator-Bug, diesmal ausgelöst durch die `CI-Agent-mit-Review-Gate`-Hochstufung. Gezielt per `grep` geprüft: keine der drei neuen Pattern-Dateien und keine der vier neuen Source-Notizen erscheint im Validator-Output.
- **Effizienz-Überarbeitung (2026-08-09):** Nach einer Analyse des Tokenverbrauchs über alle vier Schritte (~110–150k Tokens pro Quelle allein im Subagent, Tendenz strukturell steigend) wurden `references/batch-auftrag.md`, `SKILL.md` und `AGENTS.md` überarbeitet. Details und Messgrundlage: `TODO.md` im Repo-Root. Kern: der Subagent-Auftrag ist jetzt **selbsttragend** (keine Referenz-Reads mehr), repo-weite Validator-Läufe sind Subagents **verboten** (nur noch zentral), der Abschlussbericht liefert **fertig formulierte Beleg-Zeilen** statt Stichworte, und die Konsolidierung liest Bestandspatterns gezielt per `Grep`-Anker statt vollständig. Wirkung wird nach Schritt 5 gegen die ~552k aus Schritt 4 gemessen.

## Primär- und Sekundärquellen-Paare

Beim Verarbeiten zu **einer** Source-Notiz verschmelzen und beide Inbox-Notizen auf `verarbeitet` setzen.

| Sekundärquelle (vibedeck) | Primärquelle | Thread/Volltext | Status |
|---|---|---|---|
| `2026-07-08-claudedevs-claude-code-model-und-effort` | `2026-07-08-claudedevs-2074900291062034618` | vollständig | **erledigt** |
| `2026-01-21-tempoimmaterial-agent-skills-vs-rules` | `2026-01-21-tempoimmaterial-2014054104658526645` | **vollständig** (Korrektur, s. u.) | **erledigt** |
| `2026-01-23-jarrodwatts-context-engineering-guide` | `2026-01-06-jarrodwatts-2008495347115630701` | **vollständig** (Korrektur, s. u.) | **erledigt** |
| `2026-01-23-nummanali-claude-task-system` | `2026-01-23-nummanali-2014684862985175205` | **vollständig** (Korrektur, s. u.) | **erledigt** |
| `2026-02-07-daniel-san-advanced-agent-teams-patterns` | `2026-02-07-dani_avila7-2020170608290549906` | **vollständig** (Schritt 2 geprüft) | **erledigt** |
| `2026-02-07-jason-zhou-claude-code-agent-teams` | `2026-02-07-jasonzhou1993-2020086991740891526` | **vollständig** (Korrektur, s. u.) | **erledigt** |
| `2026-02-09-pdrmnvd-how-claude-code-skills-work` | `2026-02-09-pdrmnvd-2020967757706297797` | **vollständig** (Korrektur, s. u.) | **erledigt** |
| `2026-02-10-boris-tane-boris-tane-claude-code-workflow` | `2026-08-05-boristane-how-i-use-claude-code` | englischer Volltext | **erledigt** |

**Korrektur 2026-08-05 (Schritt 1):** Die ursprüngliche Annahme unten („Full-Archive-Search funktioniert bei sechs Monate alten Tweets nicht, nur Einzelpost verfügbar“) war für **alle fünf in Schritt 1 geprüften Paare falsch**. Jede der fünf Primärquellen war ein vollständiger X-„Artikel“ (Langform mit eigenem `Artikel-Volltext`-Abschnitt und allen Originalbildern), kein abgeschnittener Tweet-Thread — die „⚠ Thread über Search nicht auflösbar“-Markierung bezog sich offenbar auf eine andere Eigenschaft als Vollständigkeit, oder war für X-Artikel (im Unterschied zu echten Tweet-Threads) nie zutreffend. Alle fünf Subagents haben das unabhängig selbst festgestellt und jede Aussage der Notiz direkt gegen den vollständigen Primärtext geprüft; nur ganz vereinzelte Details (z. B. der genaue Feature-Flag-Name bei jasonzhou) standen ausschließlich in der Sekundärfassung. **Konsequenz für die beiden verbleibenden Paare in Schritt 2** (daniel-san, boris-tane): die „nur Einzelpost“-Einschätzung nicht ungeprüft übernehmen, sondern wie in Schritt 1 am tatsächlichen Inhalt der Primärquelle verifizieren.

**Ursprüngliche (jetzt widerlegte) Annahme, zur Nachvollziehbarkeit belassen:** „Full-Archive-Search funktioniert nicht generell — bei der 8 Tage alten Cerebras-Quelle gelang die Thread-Auflösung, bei diesen sechs Monate alten Tweets nicht (`⚠ Thread über Search nicht auflösbar`). Für alle sechs liegt nur der Einzelpost vor.“ Die Thread-Auflösung schlug demnach fehl (älter als sieben Tage, Full-Archive-Suche lieferte nichts), der vollständige Inhalt stecke nur in der Sekundärfassung. Siehe Korrektur oben.

**Zum Boris-Tane-Paar:** Das Ingest-Datum der Primärquelle (2026-08-05) ist nicht das Veröffentlichungsdatum — der Blog gibt keines aus. Für die Source-Notiz gilt das Datum der vibedeck-Fassung, 2026-02-10.

## Schrittgröße: 5 Quellen pro Schritt (ab 2026-08-05)

**Grund:** Der erste Lauf (2 Subagents × 5 Quellen) hat das 5h-Nutzungsfenster von 23 % auf 58 % gehoben — für 10 von 81 Quellen. Bei dieser Rate sprengt ein durchgehender Lauf über alle 68 offenen Quellen das Fenster um ein Vielfaches. Kleinere, bewusst getaktete Schritte machen den Verbrauch vorhersagbar und lassen nach jedem Schritt eine Kurskorrektur zu.

**Regel:** Pro Schritt werden **genau 5 Quellen** verarbeitet — als **5 parallele Subagents auf Sonnet-Level**, **je 1 Quelle pro Subagent** (nicht mehr 2 Subagents mit je 5 Quellen wie im ersten Lauf). Ausnahme: ein Primär/Sekundär-Paar (siehe Tabelle oben) zählt als **eine** Quelle/ein Subagent, weil beide Dateien zu einer Source-Notiz verschmolzen werden. Nach jedem Schritt: Konsolidierung (Beleg-Zeilen, neue Patterns, Index) durch den Hauptagenten, danach Usage-Stand prüfen, bevor der nächste Schritt startet.

Modellwahl explizit: Sonnet statt Opus für die Subagents, um den Tokenverbrauch pro Schritt zu senken — Qualität der ersten 9 Sonnet-Ergebnisse war bereits hoch genug für produktive Übernahme ohne Nacharbeit.

### Schritt 1 — erledigt (2026-08-05)

Alle fünf kuratierten Primär/Sekundär-Paare aus der Tabelle oben abgearbeitet (je 1 Subagent auf Sonnet-Level, parallel, verschmolz beide Dateien zu einer Source-Notiz):

1. ~~`2026-01-21-tempoimmaterial-agent-skills-vs-rules.md` + `2026-01-21-tempoimmaterial-2014054104658526645.md`~~
2. ~~`2026-01-23-jarrodwatts-context-engineering-guide.md` + `2026-01-06-jarrodwatts-2008495347115630701.md`~~
3. ~~`2026-01-23-nummanali-claude-task-system.md` + `2026-01-23-nummanali-2014684862985175205.md`~~
4. ~~`2026-02-07-jason-zhou-claude-code-agent-teams.md` + `2026-02-07-jasonzhou1993-2020086991740891526.md`~~
5. ~~`2026-02-09-pdrmnvd-how-claude-code-skills-work.md` + `2026-02-09-pdrmnvd-2020967757706297797.md`~~

### Schritt 2 — erledigt (2026-08-05)

Restliche 2 Paare + 3 Einzelquellen abgearbeitet. Beide Paare bestätigten die Schritt-1-Korrektur: Primärquellen waren vollständig, nicht „nur Einzelpost“:

1. ~~`2026-02-07-daniel-san-advanced-agent-teams-patterns.md` + `2026-02-07-dani_avila7-2020170608290549906.md`~~
2. ~~`2026-02-10-boris-tane-boris-tane-claude-code-workflow.md` + `2026-08-05-boristane-how-i-use-claude-code.md`~~
3. ~~`2026-01-12-eyad-khrais-claude-code-tutorial-level-2.md`~~
4. ~~`2026-01-21-meta-alchemist-claude-skills-deep-dive.md`~~
5. ~~`2026-01-25-sankalp-claude-code-experience.md`~~

### Schritt 3 — erledigt (2026-08-05)

Erster Schritt ohne kuratierte Paare, 5 Quellen frisch per `Select-String` ermittelt und abgearbeitet:

1. ~~`2026-01-12-dhruv1103-lessons-learned-500k-lines-claude-code.md`~~
2. ~~`2026-01-14-ashpreetbedi-claude-code-spec-first.md`~~
3. ~~`2026-01-15-unbekannt-vibe-coding-beginner-guide.md`~~
4. ~~`2026-01-21-ai-edge-claude-50-pro-tips.md`~~
5. ~~`2026-01-22-damien-lovable-website-guide.md`~~

### Schritt 4 — erledigt (2026-08-05/09)

5 Quellen frisch per `Select-String` ermittelt, Paar-Prüfung vorab ergab keine Treffer:

1. ~~`2026-01-22-hooeem-claude-code-guide.md`~~
2. ~~`2026-01-31-bcherny-claude-code-team-tips.md`~~
3. ~~`2026-01-31-unsloth-team-kimi-k2-5-local-guide.md`~~ — **ignoriert** (reiner Modell-Deployment-Guide ohne Workflow-Bezug)
4. ~~`2026-02-01-aiedge-claude-starter-pack.md`~~
5. ~~`2026-02-01-anthropic-docs-automate-workflows-with-hooks.md`~~

### Nächster Schritt (Schritt 5 von ca. 10)

**Vorher lesen:** `TODO.md` (Repo-Root), Abschnitt 4 — die Effizienzmaßnahmen sind seit 2026-08-09 in `batch-auftrag.md` und `SKILL.md` umgesetzt und müssen beim Dispatch tatsächlich angewendet werden, sonst verpufft die Überarbeitung. Insbesondere: Auftragstext aus `batch-auftrag.md` **kopieren** statt den Subagent auf Referenzdateien zu verweisen.

Nächste 5 Quellen frisch ermitteln statt einem starren Vorausplan zu folgen (der Bestand verschiebt sich mit jedem Schritt):

```powershell
Select-String -Path "00_Inbox/Quellen/*.md" -Pattern '^status: neu$' | Select-Object -First 5 -ExpandProperty Path
```

Grobe thematische Reihenfolge zur Orientierung (Details in `batch-zuordnung.json`, überholt seit der Umstellung auf 5er-Schritte, aber als Themenfolge weiter brauchbar): Agent Skills/Subagents/Context Engineering → MCP/Hooks/IDE/Agent Teams → Task-System/Vibe Coding/lokale Modelle → SDLC/Cowork/Multi-Agent → Spec-first/TDD/Testing/CLAUDE.md → Lovable/Design-Workflows/NotebookLM → Qwen3.6 und der **Mozilla-Komplex** (`2026-07-01-mozilla-mit-slashdata-…` + `2026-07-28-pdf-state-of-open-source-ai-…`, dazu die vorhandene Langzusammenfassung `00_Inbox/state-of-open-source-ai-2026-Zusammenfassung.md` — alle drei gehören in denselben Schritt).

## Lektionen aus dem ersten Subagent-Lauf (2026-08-05, 2 Batches à 5 Quellen)

- **Schrittgröße 2×5 war zu groß für das Nutzungsfenster.** 23 % → 58 % für 10 Quellen plus Konsolidierung. Ab jetzt 5×1 statt 2×5 (siehe oben).
- **Konsolidierung ist zentrale Arbeit, kein Nebenschritt.** Subagents liefern exzellente Source-Notizen, dürfen aber keine Pattern-Dateien anfassen — dadurch entstehen pro Schritt mehrere Dutzend nachzutragende Beleg-Zeilen in Bestandspatterns. Diese Konsolidierung hat mehr Zeit gekostet als die Subagent-Läufe selbst. Realistisch einplanen, nicht nur die Subagent-Laufzeit.
- **Cross-Batch-Dubletten sind möglich, aber selbstauflösend.** Zwei parallele Subagents haben unabhängig zwei Source-Notizen zur „gleichen“ Anthropic-Best-Practices-Doku angelegt — bei näherer Prüfung stellte sich heraus, dass es zwei echte, verschieden datierte Dokumente unter verschiedenen URLs sind (nicht dieselbe Quelle). Beide Agenten haben das jeweils selbst erkannt und im Text vermerkt. Trotzdem: kurzer Dublettencheck vor der Pattern-Konsolidierung lohnt sich.
- **`fix_typography.py` in den Auftrag aufgenommen, funktioniert.** Beide Batches lieferten 0 neue Anführungszeichen-Fehler.
- **Pattern-Zuordnung ist nicht immer 1:1.** Ein Quellenpunkt kann mehrere Pattern-Kandidaten haben, die bei näherer Prüfung nicht beide passen (z. B. „Skills kodieren einen Prozess“ passt zu `Klein-und-komposierbar`, aber nicht zu `Skill-Call-Hierarchie`, das ausschließlich die Aufruf-Berechtigung regelt). Bei der Konsolidierung entscheidet der Pattern-*Zweck*, nicht die vom Subagent vorgeschlagene Liste.

## Lektionen aus Schritt 1 (2026-08-05, 5×1 Sonnet-Subagents, parallel)

- **5×1 parallel war deutlich besser handhabbar als 2×5.** ~757k Tokens/238 Tool-Calls über 5 Subagents, längster Einzellauf ~7,5 Min. statt ~18,5 Min. — Parallelität statt Sequenz spart Wanduhrzeit, ohne den Gesamttokenverbrauch pro Quelle zu erhöhen.
- **Die „nur Einzelpost“-Annahme aus dem ersten Lauf war für alle fünf geprüften Paare falsch.** Jede Primärquelle war ein vollständiger X-Artikel, keine gescheiterte Thread-Auflösung. Lektion: pauschale Vorab-Einschätzungen zur Quellqualität in diesem Plan sind Hypothesen, keine Fakten — jeder Subagent muss sie am tatsächlichen Inhalt selbst prüfen, wie es der Auftrag bereits verlangte. Die Tabelle wird dadurch teils overcautious geschrieben (z. B. „Wichtige Korrektur“ oben), was sich aber als harmlos erwiesen hat, weil die Prüfpflicht im Auftrag stand.
- **Pattern-Vorschläge von Subagents sind ein guter Ausgangspunkt, aber kein Automatismus.** Von 4 vorgeschlagenen neuen Patterns wurden nur 2 tatsächlich als eigene Dateien angelegt; die anderen 2 (`Rule-oder-Skill-Litmustest`, `Task-Registry-als-Shared-State`) deckten bei näherer Prüfung dieselbe Entscheidungsachse bzw. denselben Mechanismus ab, den ein Bestandspattern (`Erweiterungs-Ebenen-Zuordnung`, `Kontrollierte-Agent-Parallelisierung`) bereits abdeckte — nur präziser benannt oder mit mehr Mechanik belegt. Jeder Subagent kennt nur seine eigene Quelle, nicht die anderen vier parallel bearbeiteten; erst die zentrale Konsolidierung sieht Überlappungen zwischen den fünf Vorschlägen selbst (hier: keine direkte Überlappung zwischen den 4 Vorschlägen, aber je eine Überlappung mit dem Bestand).
- **Dangling Wiki-Links durch Vorwärtsverweise auf noch nicht angelegte Patterns sind normal und einkalkuliert.** Zwei Subagents verlinkten korrekt auf ihren eigenen Pattern-Vorschlag, der zum Zeitpunkt ihres Laufs noch nicht existierte; die zentrale Konsolidierung löst das auf, indem sie den Link entweder auf die neu angelegte Datei zeigen lässt oder auf das Pattern umbiegt, das den Inhalt tatsächlich aufgenommen hat.
- **`fix_typography.py` weiterhin zuverlässig, auch bei Bestandspattern-Edits.** 14 gemischte Anführungszeichen in 4 Dateien korrigiert — ausschließlich in während dieses Laufs frisch hinzugefügten Zeilen, keine Regression in unangetastetem Altbestand.

## Lektionen aus Schritt 2 (2026-08-05, 5×1 Sonnet-Subagents, parallel)

- **Der explizite Hinweis auf die Schritt-1-Korrektur im Auftrag hat funktioniert.** Beide Paar-Subagents (daniel-san, boris-tane) haben die Primärquelle selbst geprüft statt die „nur Einzelpost“-Einschätzung zu übernehmen, und beide bestätigten erneut: vollständig. Eine pauschale Annahme im Plan lässt sich also durch eine explizite Prüfpflicht im Subagent-Auftrag zuverlässig neutralisieren, ohne den Plantext selbst vorab korrigieren zu müssen.
- **Nicht jede Quelle liefert einen neuen Pattern-Vorschlag — und das ist ein gutes Zeichen für die Bestandsreife.** 2 von 5 Subagents (eyad-khrais Level 2, meta-alchemist) kamen explizit zum Schluss „keine neuen Patterns nötig“, weil ihre Kernthemen im mittlerweile 31 Patterns umfassenden Bestand bereits präziser abgedeckt waren. Beide lieferten trotzdem verwertbare Befunde (Autor-Inkonsistenz bei Schwellenwerten, methodische Schwäche eines Vendor-Benchmarks) als Beleg-Zeilen statt als Pattern.
- **Ein Subagent kann eine eigene Quelle korrekt als „Primärquelle hinter einem bereits vorhandenen Beleg“ einordnen, statt sie fälschlich als unabhängige Zweitbestätigung zu zählen.** Der daniel-san-Subagent erkannte, dass seine Quelle die Primärquelle hinter einem bereits über ein Wiki-Kompilat referenzierten Beleg in `Kontrollierte-Agent-Parallelisierung` ist, und hat das explizit vermerkt statt die Konfidenz fälschlich zu stützen. Wichtig für die Konsolidierung: solche Vermerke im Subagent-Bericht aktiv suchen, nicht nur die vorgeschlagenen Beleg-Zeilen selbst übernehmen.
- **Eine Konfidenz-Hochstufung (`meinung` → `mehrfach-belegt`) durch eine neue, unabhängige Zweitquelle löst denselben vorbekannten Validator-Bug aus wie bei den sechs bereits betroffenen Patterns.** Bei `Action-Space-Design-nach-Modellfaehigkeit` erwartungsgemäß eingetreten (Offener Punkt 2) — kein Grund, die Hochstufung zu unterlassen, nur weil der Validator sie fälschlich meldet.

## Lektionen aus Schritt 3 (2026-08-05, 5×1 Sonnet-Subagents, parallel, erster Schritt ohne kuratierte Paare)

- **Frisch per `Select-String` ermittelte Quellen liefen genauso reibungslos wie die kuratierten Paare.** Kein qualitativer Unterschied zu den ersten beiden Schritten — die Umstellung von „vorbereitete Liste“ auf „jeweils frisch ermitteln“ (siehe Regeln oben) hat den Ablauf nicht verkompliziert.
- **Neue Pattern-Anlage aus einer Einzelquelle ist in diesem System etabliert, nicht die Ausnahme.** Alle 3 in diesem Schritt neu angelegten Patterns hatten zum Zeitpunkt der Anlage nur einen einzigen, unbelegten Beleg — genau wie die meisten der bereits in Schritt 1 und 2 angelegten. Konfidenz `meinung` ist ein legitimer Startzustand; ein Subagent, der aus Vorsicht die Anlage selbst zurückstellt (wie bei `Trainingsdaten-Dichte-als-Stack-Kriterium` empfohlen), liegt konservativer als die etablierte Praxis dieses Systems — die zentrale Konsolidierung legt das Pattern trotzdem an, wenn es benennbar und eigenständig ist.
- **Ein Subagent kann einen eigenen kleinen Fehler noch im selben Lauf selbst korrigieren.** Beim Damien-Lovable-Subagent entstand durch das Edit-Tool kurzzeitig ein doppeltes `status:`-Feld in der Inbox-Datei; der Subagent hat das selbst erkannt und bereinigt, bevor der Bericht ging. Trotzdem: Frontmatter frisch bearbeiteter Inbox-Dateien bei der Konsolidierung stichprobenartig gegenlesen.
- **Nicht jedes Bild mit passendem Alt-Text im Rohmaterial zeigt tatsächlich das, was der Alt-Text behauptet.** Beim elenakvcs-Subagent zeigten alle vier Bilder der Rohquelle andere Inhalte als ihre eigenen Alt-Texte (mutmaßlich ein vibedeck-Scrape-Zuordnungsfehler) — der Subagent hat das erkannt und konsequent keines übernommen, statt sich auf den Alt-Text zu verlassen. Bildregel-Prüfung heißt: den Bildinhalt selbst ansehen, nicht nur den mitgelieferten Text dazu.
- **`fix_typography.py` kann als Nebeneffekt vorbestehende Fehler in einer bearbeiteten Datei mitkorrigieren.** Beim Lauf über `TDD-als-Verifikationshebel.md` wurden zwei alte, nicht von diesem Schritt verursachte gemischte Anführungszeichen in einer bestehenden Beleg-Zeile automatisch mitbereinigt — Validator-Fehlerzahl sank dadurch sogar unter den Vorschritt-Wert. Kein Nachteil, aber beim Berichten der Fehlerzahl-Differenz benennen, damit „weniger Fehler als vorher“ nicht als Messfehler missverstanden wird.

## Effizienz-Testlauf (2026-08-09, 1 Subagent, überarbeiteter Auftrag)

Nach der Überarbeitung von `batch-auftrag.md`/`SKILL.md`/`AGENTS.md` (siehe `TODO.md`) wurde die Wirkung an einer einzelnen Quelle geprüft, bevor ein voller 5er-Schritt gefahren wird: `2026-02-01-anthropic-docs-claude-code-common-workflows.md` (Anthropic-Doku, keine Bilder, keine Primärquelle).

**Ergebnis: ~73k Tokens, 9 Tool-Calls — gegenüber ~110-150k Tokens im Schnitt der Schritte 1-4.** Der Subagent hat keine Referenzdatei gelesen, `validate_knowledge.py` nicht ausgeführt und im Bericht bereits fertig formulierte Beleg-Zeilen für vier Bestandspatterns geliefert (`Kontrollierte-Agent-Parallelisierung`, `Kontext-Hygiene-Entscheidungsbaum`, `Klein-und-komposierbar`, `Plan-first-mit-getrenntem-Review`) sowie einen vollständig ausgearbeiteten Pattern-Vorschlag (`Screenshot-als-Spezifikationsmedium`, angelegt). Die Konsolidierung selbst hat testweise die `Grep`-Anker-Technik statt Volltext-Reads genutzt (vier `Grep -n "## Spannungen"` + gezielte `Read`-`offset`-Aufrufe von je 4-5 Zeilen statt vier Dateien mit 45-65 Zeilen vollständig zu laden) — spürbar weniger Kontext für dieselbe Konsolidierungsarbeit. Validator danach: 44 Fehler, unverändert gegenüber Schritt 4, keiner davon im Testlauf verursacht.

**Bemerkenswert:** Die Quelle überlappte inhaltlich stark mit der bereits verarbeiteten Schwesterquelle `2026-02-01-anthropic-docs-claude-code-best-practices.md` (selbes Datum, selber Autor, selbe Docs-Familie) — der Subagent hat das selbst erkannt, generische Workflow-Rezepte (Debugging, Refactoring, Tests) bewusst nicht als eigene Kernaussagen aufgenommen und nur die tatsächlich neuen Mechanik-Details (Worktree-Befehle, `@`-Referenzsyntax, Headless-Pipe-Komposition, `--permission-mode plan`) als Beleg-Zeilen formuliert.

**Einordnung des Ergebnisses:** Ein einzelner Datenpunkt ohne Bilder ist kein Beweis, aber ein starkes Signal — die Größenordnung der Einsparung (grob Faktor 1,5-2) deckt sich mit der Erwartung aus der Ursachenanalyse. Verlässliche Bestätigung erst nach einem vollen 5er-Schritt mit den überarbeiteten Regeln (Schritt 5).

## Lektionen aus Schritt 4 (2026-08-05/09, 5×1 Sonnet-Subagents, parallel)

- **Das Relevanz-Gate greift und darf greifen.** Erstmals seit der Umstellung auf 5er-Schritte hat ein Subagent eine Quelle begründet als `ignoriert` eingestuft, statt eine dünne Source-Notiz zu erzwingen. Entscheidend war, dass der Auftrag den Zweifel ausdrücklich benannte („diese Quelle ist tendenziell randständig, prüfe kritisch“) — ein neutral formulierter Auftrag hätte vermutlich zu einer Notiz geführt. Lektion: Bei erkennbar randständigen Quellen den Zweifel in den Auftrag schreiben, statt ihn dem Subagenten allein zu überlassen.
- **Dieselbe Aussage über zwei verschiedene Aggregatoren ist kein Zweitbeleg.** Zwei der zehn bcherny-Tipps decken sich nahezu wortgleich mit einer bereits verarbeiteten Quelle, die ebenfalls Boris Cherny zuschreibt — verschiedene Sekundärquellen (vibedeck vs. @Meer_AIIT), aber dieselbe Primäraussage. Der Subagent hat das selbst erkannt und die Konfidenz nicht angehoben. Bei prominenten Autoren, die vielfach zitiert werden, ist das der Normalfall, nicht die Ausnahme.
- **Eine echte Konfidenz-Hochstufung sieht anders aus.** `CI-Agent-mit-Review-Gate` stand auf `meinung` mit einer einzigen Herstellerdoku zu einer Plattform (GitLab). Der Betriebsbericht zu GitHub Actions ist eine andere Plattform, ein anderer Organisationskontext und ein Praxisbericht statt einer Doku — das trägt `mehrfach-belegt`, anders als der bcherny/Meer-Fall oben.
- **Die Effizienz-Analyse hat mehr gebracht als eine weitere Quelle.** Der Tokenverbrauch lag bei ~110–150k pro Quelle allein im Subagent, mit strukturell steigender Tendenz (append-only Patterns). Die Ursachenanalyse (redundante Referenz-Reads, Validator-Läufe pro Subagent statt zentral, Volltext-Reads für Anhänge-Edits) führte zur Überarbeitung von `batch-auftrag.md`, `SKILL.md` und `AGENTS.md`. Lektion für künftige Batch-Vorhaben: den Verbrauch nicht erst am Limit analysieren — die Treiber waren aus den Subagent-Berichten von Anfang an ablesbar (mehrere meldeten „Validator: 43 vorbestehende“, obwohl der Auftrag das nie verlangt hatte).
- **Ein Auftrag, der etwas nicht verbietet, erlaubt es faktisch.** Mehrere Subagents führten den repo-weiten Validator aus, weil `SKILL.md` — das sie laut Auftrag lesen sollten — ihn als Pflichtschritt führt. Die Regeln für den delegierten und den direkten Lauf müssen getrennt formuliert sein, sonst zieht der Subagent Pflichten aus einem Kontext, der für ihn gar nicht gilt.

## Regeln für die Fortsetzung

1. Patterns werden **zentral** angelegt, nicht von parallel laufenden Bearbeitern — sonst entstehen Duplikate unter verschiedenen Namen. Bearbeiter liefern nur Vorschläge.
2. Offene Quellen finden: `Select-String -Path "00_Inbox/Quellen/*.md" -Pattern '^status: neu$'`.
3. Nach jeder Quelle den Status fortschreiben, sonst erscheint sie erneut als offen.
4. Nach dem Schreiben `python 70_Scripts/fix_typography.py <eigene-datei>` laufen lassen — gemischte Anführungszeichen sind der häufigste Validator-Fehler und passieren trotz Regel.
5. `README.md` und diese Datei sind keine Quellen (im Code über `KEINE_QUELLEN` ausgeschlossen).

## Offene Punkte

| # | Punkt | Entscheidung nötig |
|---|---|---|
| 1 | **41 Quellen verarbeiten**, weiter in Schritten à 5. Schritt 1–4 sind erledigt — Schritt 5 per `Select-String` frisch ermitteln, dabei die seit 2026-08-09 überarbeiteten Effizienzregeln anwenden (siehe `TODO.md` Abschnitt 4). | nein — kann laufen |
| 1a | **80+ Dateien sind seit Schritt 1 ungecommittet.** Bisher kein einziger Zwischen-Commit über die gesamte Verarbeitung. | **ja** — Commit-Rhythmus festlegen |
| 2 | **Validator-Regel zur Konfidenz** ist falsch implementiert: `mehrfach-belegt` mit ausschließlich `meinung`-Belegen gilt als Fehler, obwohl sechs Patterns genau das nutzen und `80_Knowledge/README.md` es so definiert. Fix: bei mindestens zwei unabhängigen `meinung`-Belegen `mehrfach-belegt` zulassen. | **ja** — Eingriff ins Knowledge-Schema |
| 3 | **Validator kennt `external_knowledge/`-Pfade nicht** und meldet zwei korrekte Beleg-Zeilen in `Kontext-Hygiene-Entscheidungsbaum` als Formatfehler. | **ja** — Eingriff ins Knowledge-Schema |
| 4 | **58 gemischte Anführungszeichen in 12 Altdateien** könnten mit `fix_typography.py` bereinigt werden. Nicht getan, weil Source-Notizen nach Anlage unverändert bleiben (Invariante 2). | **ja** — Ausnahme von der Invariante |
| 5 | **Export nach vibedeck** fehlt: Source-Notiz → vibedeck-Frontmatter, damit die Darstellung dort die Synthese von hier zeigt. | ja — eigenes Vorhaben |
| 6 | **19 übersprungene Dubletten** wurden nicht geprüft: enthält die vibedeck-Fassung Inhalte, die in der vorhandenen Source-Notiz fehlen? | ja — eigener Durchgang |
| 7 | **PDF-Bildextraktion** liefert bei vektorbasierten PDFs fast nichts (Mozilla-Report: 1 Bild aus 65 Seiten). Seiten-Rendering wäre die Alternative, produziert aber viel Ausschuss. | ja — nur bei Bedarf |
