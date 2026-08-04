# Verarbeitungsplan: vibedeck-Übernahme

**Stand:** 2026-08-05 · **Fortschritt:** 12 von 81 Quellen verarbeitet

Hält den Zwischenstand fest, damit ein späterer Lauf nahtlos fortsetzt. Nach vollständiger Abarbeitung kann die Datei gelöscht werden.

## Kennzahlen

| | Anzahl |
|---|---|
| Quellen in der Inbox | 81 |
| davon `status: neu` | **68** |
| davon `status: verarbeitet` | 12 |
| davon `status: ignoriert` | 0 |
| Bilder lokal | 188 |
| Source-Notizen in `80_Knowledge/Sources/` | 63 |
| Patterns | 29 (3 neu in diesem Lauf: Voice-Prompting-fuer-Kontextreichtum, CI-Agent-mit-Review-Gate, Sandbox-Komposition-aus-OS-Primitiven) |
| Verbrauch 2 Subagents (10 Quellen) | ~363k Tokens, 121 Tool-Calls, ~18,5 Min. Laufzeit gesamt |

## Erledigt

- **70 vibedeck-Artikel importiert** als Sekundärquellen (`sekundaerquelle: true`, `quelle: vibedeck`) samt **131 Bildern**. Die Bildpositionen im Text stammen aus vibedeck und wurden nicht neu gesetzt — dort standen sie bereits an der inhaltlich passenden Stelle; das Skript schreibt nur die Pfade um. Skript: `70_Scripts/import_vibedeck_knowledge.py`.
- **19 Artikel übersprungen**, deren `sourceURL` bereits als Source-Notiz existiert. Die Liste erzeugt das Skript erneut, wenn man `--skip-vorhandene-urls` weglässt.
- **10 Primärquellen nachgeholt**: 7 über die X-API, 1 Blogartikel (Boris Tane) per URL-Ingest, 2 waren bereits vollständig durch die vibedeck-Fassung abgedeckt.
- **3 Quellen verarbeitet**: Cerebras (GPT-5.6-Modellwahl) sowie das Paar ClaudeDevs Modell/Effort (Primär + Sekundär zu einer Notiz verschmolzen). Sie dienen als Qualitätsmuster für die übrigen.
- **2 neue Patterns** aus diesen Quellen: `Modell-Eskalation-von-guenstig-nach-teuer` (inzwischen `mehrfach-belegt`) und `Advisor-Agent-gegen-Drift`.

## Primär- und Sekundärquellen-Paare

Beim Verarbeiten zu **einer** Source-Notiz verschmelzen und beide Inbox-Notizen auf `verarbeitet` setzen.

| Sekundärquelle (vibedeck) | Primärquelle | Thread/Volltext | Status |
|---|---|---|---|
| `2026-07-08-claudedevs-claude-code-model-und-effort` | `2026-07-08-claudedevs-2074900291062034618` | vollständig | **erledigt** |
| `2026-01-21-tempoimmaterial-agent-skills-vs-rules` | `2026-01-21-tempoimmaterial-2014054104658526645` | nur Einzelpost | offen |
| `2026-01-23-jarrodwatts-context-engineering-guide` | `2026-01-06-jarrodwatts-2008495347115630701` | nur Einzelpost | offen |
| `2026-01-23-nummanali-claude-task-system` | `2026-01-23-nummanali-2014684862985175205` | nur Einzelpost | offen |
| `2026-02-07-daniel-san-advanced-agent-teams-patterns` | `2026-02-07-dani_avila7-2020170608290549906` | nur Einzelpost | offen |
| `2026-02-07-jason-zhou-claude-code-agent-teams` | `2026-02-07-jasonzhou1993-2020086991740891526` | nur Einzelpost | offen |
| `2026-02-09-pdrmnvd-how-claude-code-skills-work` | `2026-02-09-pdrmnvd-2020967757706297797` | nur Einzelpost | offen |
| `2026-02-10-boris-tane-boris-tane-claude-code-workflow` | `2026-08-05-boristane-how-i-use-claude-code` | englischer Volltext | offen |

**Wichtige Korrektur:** Full-Archive-Search funktioniert nicht generell — bei der 8 Tage alten Cerebras-Quelle gelang die Thread-Auflösung, bei diesen sechs Monate alten Tweets nicht (`⚠ Thread über Search nicht auflösbar`). Für alle sechs liegt nur der Einzelpost vor.

**Wichtig bei „nur Einzelpost":** Die Thread-Auflösung schlug fehl (älter als sieben Tage, Full-Archive-Suche lieferte nichts). Der vollständige Inhalt steckt jeweils in der Sekundärfassung. Die Source-Notiz muss unterscheiden, was primär belegt ist und was nur die Sekundärfassung behauptet.

**Zum Boris-Tane-Paar:** Das Ingest-Datum der Primärquelle (2026-08-05) ist nicht das Veröffentlichungsdatum — der Blog gibt keines aus. Für die Source-Notiz gilt das Datum der vibedeck-Fassung, 2026-02-10.

## Schrittgröße: 5 Quellen pro Schritt (ab 2026-08-05)

**Grund:** Der erste Lauf (2 Subagents × 5 Quellen) hat das 5h-Nutzungsfenster von 23 % auf 58 % gehoben — für 10 von 81 Quellen. Bei dieser Rate sprengt ein durchgehender Lauf über alle 68 offenen Quellen das Fenster um ein Vielfaches. Kleinere, bewusst getaktete Schritte machen den Verbrauch vorhersagbar und lassen nach jedem Schritt eine Kurskorrektur zu.

**Regel:** Pro Schritt werden **genau 5 Quellen** verarbeitet — als **5 parallele Subagents auf Sonnet-Level**, **je 1 Quelle pro Subagent** (nicht mehr 2 Subagents mit je 5 Quellen wie im ersten Lauf). Ausnahme: ein Primär/Sekundär-Paar (siehe Tabelle oben) zählt als **eine** Quelle/ein Subagent, weil beide Dateien zu einer Source-Notiz verschmolzen werden. Nach jedem Schritt: Konsolidierung (Beleg-Zeilen, neue Patterns, Index) durch den Hauptagenten, danach Usage-Stand prüfen, bevor der nächste Schritt startet.

Modellwahl explizit: Sonnet statt Opus für die Subagents, um den Tokenverbrauch pro Schritt zu senken — Qualität der ersten 9 Sonnet-Ergebnisse war bereits hoch genug für produktive Übernahme ohne Nacharbeit.

### Nächster Schritt (Schritt 1 von ca. 13)

Kuratiert, damit alle fünf verbleibenden Primär/Sekundär-Paare aus der Tabelle oben zuerst und gebündelt abgearbeitet werden (je 1 Subagent verschmilzt beide Dateien zu einer Source-Notiz):

1. `2026-01-21-tempoimmaterial-agent-skills-vs-rules.md` + `2026-01-21-tempoimmaterial-2014054104658526645.md`
2. `2026-01-23-jarrodwatts-context-engineering-guide.md` + `2026-01-06-jarrodwatts-2008495347115630701.md`
3. `2026-01-23-nummanali-claude-task-system.md` + `2026-01-23-nummanali-2014684862985175205.md`
4. `2026-02-07-jason-zhou-claude-code-agent-teams.md` + `2026-02-07-jasonzhou1993-2020086991740891526.md`
5. `2026-02-09-pdrmnvd-how-claude-code-skills-work.md` + `2026-02-09-pdrmnvd-2020967757706297797.md`

### Schritt 2 (danach)

Restliche 2 Paare + 3 Einzelquellen:

1. `2026-02-07-daniel-san-advanced-agent-teams-patterns.md` + `2026-02-07-dani_avila7-2020170608290549906.md`
2. `2026-02-10-boris-tane-boris-tane-claude-code-workflow.md` + `2026-08-05-boristane-how-i-use-claude-code.md`
3. `2026-01-12-eyad-khrais-claude-code-tutorial-level-2.md`
4. `2026-01-21-meta-alchemist-claude-skills-deep-dive.md`
5. `2026-01-25-sankalp-claude-code-experience.md`

### Schritt 3 und weiter

Ab Schritt 3 gibt es keine Paare mehr. Nächste 5 Quellen jeweils frisch ermitteln statt einem starren Vorausplan zu folgen (der Bestand verschiebt sich mit jedem Schritt):

```powershell
Select-String -Path "00_Inbox/Quellen/*.md" -Pattern '^status: neu$' | Select-Object -First 5 -ExpandProperty Path
```

Grobe thematische Reihenfolge zur Orientierung (Details in `batch-zuordnung.json`, überholt seit der Umstellung auf 5er-Schritte, aber als Themenfolge weiter brauchbar): Agent Skills/Subagents/Context Engineering → MCP/Hooks/IDE/Agent Teams → Task-System/Vibe Coding/lokale Modelle → SDLC/Cowork/Multi-Agent → Spec-first/TDD/Testing/CLAUDE.md → Lovable/Design-Workflows/NotebookLM → Qwen3.6 und der **Mozilla-Komplex** (`2026-07-01-mozilla-mit-slashdata-…` + `2026-07-28-pdf-state-of-open-source-ai-…`, dazu die vorhandene Langzusammenfassung `00_Inbox/state-of-open-source-ai-2026-Zusammenfassung.md` — alle drei gehören in denselben Schritt).

## Lektionen aus dem ersten Subagent-Lauf (2026-08-05, 2 Batches à 5 Quellen)

- **Schrittgröße 2×5 war zu groß für das Nutzungsfenster.** 23 % → 58 % für 10 Quellen plus Konsolidierung. Ab jetzt 5×1 statt 2×5 (siehe oben).
- **Konsolidierung ist zentrale Arbeit, kein Nebenschritt.** Subagents liefern exzellente Source-Notizen, dürfen aber keine Pattern-Dateien anfassen — dadurch entstehen pro Schritt mehrere Dutzend nachzutragende Beleg-Zeilen in Bestandspatterns. Diese Konsolidierung hat mehr Zeit gekostet als die Subagent-Läufe selbst. Realistisch einplanen, nicht nur die Subagent-Laufzeit.
- **Cross-Batch-Dubletten sind möglich, aber selbstauflösend.** Zwei parallele Subagents haben unabhängig zwei Source-Notizen zur „gleichen" Anthropic-Best-Practices-Doku angelegt — bei näherer Prüfung stellte sich heraus, dass es zwei echte, verschieden datierte Dokumente unter verschiedenen URLs sind (nicht dieselbe Quelle). Beide Agenten haben das jeweils selbst erkannt und im Text vermerkt. Trotzdem: kurzer Dublettencheck vor der Pattern-Konsolidierung lohnt sich.
- **`fix_typography.py` in den Auftrag aufgenommen, funktioniert.** Beide Batches lieferten 0 neue Anführungszeichen-Fehler.
- **Pattern-Zuordnung ist nicht immer 1:1.** Ein Quellenpunkt kann mehrere Pattern-Kandidaten haben, die bei näherer Prüfung nicht beide passen (z. B. „Skills kodieren einen Prozess" passt zu `Klein-und-komposierbar`, aber nicht zu `Skill-Call-Hierarchie`, das ausschließlich die Aufruf-Berechtigung regelt). Bei der Konsolidierung entscheidet der Pattern-*Zweck*, nicht die vom Subagent vorgeschlagene Liste.

## Regeln für die Fortsetzung

1. Patterns werden **zentral** angelegt, nicht von parallel laufenden Bearbeitern — sonst entstehen Duplikate unter verschiedenen Namen. Bearbeiter liefern nur Vorschläge.
2. Offene Quellen finden: `Select-String -Path "00_Inbox/Quellen/*.md" -Pattern '^status: neu$'`.
3. Nach jeder Quelle den Status fortschreiben, sonst erscheint sie erneut als offen.
4. Nach dem Schreiben `python 70_Scripts/fix_typography.py <eigene-datei>` laufen lassen — gemischte Anführungszeichen sind der häufigste Validator-Fehler und passieren trotz Regel.
5. `README.md` und diese Datei sind keine Quellen (im Code über `KEINE_QUELLEN` ausgeschlossen).

## Offene Punkte

| # | Punkt | Entscheidung nötig |
|---|---|---|
| 1 | **78 Quellen verarbeiten** in 13 Batches. Blockiert war das durch das Session-Limit; die Vorarbeit liegt vollständig bereit. | nein — kann laufen |
| 2 | **Validator-Regel zur Konfidenz** ist falsch implementiert: `mehrfach-belegt` mit ausschließlich `meinung`-Belegen gilt als Fehler, obwohl sechs Patterns genau das nutzen und `80_Knowledge/README.md` es so definiert. Fix: bei mindestens zwei unabhängigen `meinung`-Belegen `mehrfach-belegt` zulassen. | **ja** — Eingriff ins Knowledge-Schema |
| 3 | **Validator kennt `external_knowledge/`-Pfade nicht** und meldet zwei korrekte Beleg-Zeilen in `Kontext-Hygiene-Entscheidungsbaum` als Formatfehler. | **ja** — Eingriff ins Knowledge-Schema |
| 4 | **58 gemischte Anführungszeichen in 12 Altdateien** könnten mit `fix_typography.py` bereinigt werden. Nicht getan, weil Source-Notizen nach Anlage unverändert bleiben (Invariante 2). | **ja** — Ausnahme von der Invariante |
| 5 | **Export nach vibedeck** fehlt: Source-Notiz → vibedeck-Frontmatter, damit die Darstellung dort die Synthese von hier zeigt. | ja — eigenes Vorhaben |
| 6 | **19 übersprungene Dubletten** wurden nicht geprüft: enthält die vibedeck-Fassung Inhalte, die in der vorhandenen Source-Notiz fehlen? | ja — eigener Durchgang |
| 7 | **PDF-Bildextraktion** liefert bei vektorbasierten PDFs fast nichts (Mozilla-Report: 1 Bild aus 65 Seiten). Seiten-Rendering wäre die Alternative, produziert aber viel Ausschuss. | ja — nur bei Bedarf |
