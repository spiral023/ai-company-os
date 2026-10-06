---
titel: "Retro-Skill für Claude Code: Fehler einer Session in Checks verwandeln"
datum: 2026-10-06
kategorie: arbeitsweisen
zusammenfassung: "Matt Pococks Retro-Skill verbessert nach deiner Auswahl Checks, Navigation und Standards. Was Version 1.3 mit /implement-spec und /pr ergänzt und wie sich Retro und Doctor unterscheiden."
status: freigegeben
geprueft_am: 2026-10-05
freigabe: automatisch
aktualisiert: 2026-10-07
quellen:
  - 2026-10-05-repo-mattpocock-skills-retro
  - 2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck
  - 2026-10-05-repo-garrytan-gstack-retro
  - 2026-10-05-repo-bmad-method-retrospective
  - 2026-10-05-repo-squad-retro-enforcement
  - 2026-10-05-repo-claude-code-doctor-insights
  - 2026-10-05-repo-alirezarezvani-skill-doctor
  - 2026-10-05-repo-millionco-react-doctor-skill
  - 2026-02-09-tom-crawshaw-claude-code-insights-guide
  - 2026-10-05-aihero-v1-3-implement-spec-pr-retro-and-glossary-md
---

## Kurz gesagt

- Lass nach einer holprigen Session `/retro` aus Matt Pococks Skill-Sammlung laufen. Er schlägt Änderungen an der Umgebung vor, damit derselbe Fehler nicht wieder passiert.
- Mechanische Fehler gehören in einen Linter, Pre-Commit-Hook oder CI-Job. Regeln in Prosa bleiben für Ermessensfragen.
- Doctor-Werkzeuge prüfen den aktuellen Zustand von Setup oder Code. Eine Retro fragt, was in einer konkreten Session schiefging, deshalb brauchst du beides.
- Wähle die sinnvollen Retro-Vorschläge selbst aus und setze sie um. Pocock rät von automatischen Retro-Schleifen ab, weil falsche Funde unnötige Umbauten auslösen können.

## Retro oder Doctor: welches Werkzeug wofür

| Werkzeug | Schaut auf | Liefert | Passt, wenn |
|---|---|---|---|
| `/retro` (mattpocock/skills) | eine Coding-Session | Vorschläge für Checks, Navigation, Standards | ein Agent-Fehler nicht wiederkommen soll |
| `/retro` (gstack) | Git-Historie einer Woche | Kennzahlen, Lob, Trends | ein Team auf seinen Output schauen will |
| `bmad-retrospective` | ein abgeschlossenes Epic | Befunde mit Fundstelle, Abnahmeentscheidung | du im BMad-Ticketsystem arbeitest |
| `/doctor` (Claude Code) | die Einrichtung | Fehler in Plugins, Hooks, MCP, CLAUDE.md | Claude Code sich seltsam verhält |
| `/skill-doctor` (Claude Code) | geladene Skills | ungenutzte Skills und ihre Kontextkosten | die Skill-Liste gewachsen ist |
| `skill-doctor` (alirezarezvani) | viele vergangene Sessions | Note und Skill-Diffs | du Skills anhand echter Läufe verbessern willst |
| React Doctor | React-Code | Health-Score 0 bis 100 | nach jeder Änderung an einer React-App |

## Was `/retro` macht

Matt Pocock hat `retro` mit Version 1.3.0 seiner Skill-Sammlung in den Engineering-Bereich übernommen, seitdem steckt der Skill im Claude-Code-Plugin. Sein Beitrag zum Update 1.3 beschreibt den Ablauf und verweist auf das vollständige Release 1.3.1.{q:1}{q:10} Du rufst `/retro` selbst auf. Ohne Angabe wertet er die laufende Session aus, sonst die genannte.{q:1}

Der Skill sucht in sieben Bereichen nach Verbesserungen: Navigation, automatische Checks, Coding Standards für den Review-Agent, eine zu große globale AGENTS.md, teure Tool-Aufrufe, Anweisungen ohne Wirkung und fehlender Zugang zu Informationen wie Logs des Dev-Servers.{q:1} Am Ende stehen Vorschläge, sortiert nach Schwere. Er ändert nichts, bis du auswählst, welche davon umgesetzt werden sollen.{q:10}

Pocock empfiehlt auffällige Sessions oder gelegentliche Stichproben. Eine automatisch wiederholte Retro lehnt er ab: Falsch positive Funde können immer weitere Umbauten anstoßen. Du entscheidest, welche Vorschläge für dein Projekt sinnvoll sind.{q:10}

Ein Beispiel für Navigation: Hat der Agent lange gesucht, bis er die richtige Konfigurationsdatei fand, schlägt die Retro einen Hinweis in der CLAUDE.md vor, der direkt dorthin zeigt. Ein Beispiel für Checks: Hat er einen Import in falscher Form geschrieben und erst der Review hat es bemerkt, wird daraus eine Linter-Regel.

## Checks schlagen Regeln

Der Skill stuft jeden Verstoß gegen Coding Standards zuerst als mechanisch oder als Ermessensfrage ein. Mechanisch heißt: ein festes Syntaxmuster, eine verbotene API, eine Importform, ein falscher Dateiort. Dafür schlägt die Retro eine deterministische Prüfung vor: eine Linter-Regel, einen Pre-Commit-Hook oder einen CI-Job. Zuerst prüft sie die vorhandenen Prüfkommandos und ihre Einbindung; ein bestehender, aber ungenutzter Check braucht keine zweite Implementierung.{q:1} Nur echte Ermessensfragen landen als Text in `CODING_STANDARDS.md`. Ein Repo ganz ohne Pre-Commit-Hook und ohne CI-Job für Lint, Typecheck und Tests zählt selbst schon als Befund.{q:1}

Die Begründung liefert Pocock in seinem Vortrag zum PR-Engpass. Der Agent, der implementiert, steht unter dem größten Kontextdruck, er muss suchen, schreiben und debuggen. Der Review-Agent bekommt nur den Diff. Standards gehören deshalb in eine eigene Datei für den Review und nicht in die AGENTS.md, die jeder Agent bei jedem Start lädt.{q:2} `/retro` ist in diesem Ablauf der letzte Schritt, der Funde aus dem Review in Checks und Standards überführt.{q:2} Warum eine Prosa-Regel für Pflichtvorgaben zu schwach ist, zeigt auch der Beitrag zu [Deny-Rules statt Bitte](post:deny-rules-statt-bitte).

## Was Version 1.3 um die Retro herum ergänzt

Nach `/grill-with-docs` → `/to-spec` → `/to-tickets` übernimmt `/implement-spec` auf deinen Aufruf die ganze Spec. Ausführbare Tickets starten parallel in eigenen Worktrees; ihre Ergebnisse landen auf einer Integrationsbranch. Am Ende folgen `/code-review` und die Behebung der Funde. Für die meisten Nutzer empfiehlt Pocock weiterhin eine deterministische Script-Schleife mit `/implement` pro Ticket; die Agent-Steuerung beschreibt er als Einstieg, bevor diese eingerichtet ist.{q:10}

`/pr` liefert die Beschreibung für den menschlichen Review: **Summary** als kleine hilfreiche Darstellung, **Evidence** als ausgeführtes Vorher/Nachher und **Merge Danger** mit Rücknehmbarkeit und Blast Radius. Ein grüner Test nach einem zuvor roten Test hilft beim Prüfen; eine versendete E-Mail lässt sich durch einen Revert nicht zurückholen.{q:10}

Diese Aufbereitung verkleinert den Diff nicht. Pocock nennt die große Integrationsbranch ausdrücklich als ungelöstes Problem. Auch Worktrees verhindern keine inhaltlichen Kollisionen: Zwei Tickets können dasselbe Feld unter verschiedenen Namen hinzufügen.{q:10} Plane bei einer großen Spec deshalb früh, welche Teile du getrennt prüfen kannst. Nach dem Review folgt die von dir ausgewählte Retro; nach einem Bugfix verweist `/ask-matt` ebenfalls darauf, um nach einer möglichen Vorbeugung zu fragen.{q:10}

Beim Update brauchst du außerdem eine gemeinsame Umbenennung: `CONTEXT.md` wird zu `GLOSSARY.md`, `CONTEXT-MAP.md` zu `GLOSSARY-MAP.md`. Die Skills suchen nur die neuen Namen; ohne Migration kann neben dem alten ein leeres neues Glossar entstehen. Der frühere Skill `resolving-merge-conflicts` entfällt. Prüfe nach dem Update, ob eine alte Kopie zurückgeblieben ist.{q:10}

## Andere Retros: Woche, Epic, Pflichttermin

Garry Tans gstack wertet mit `/retro` die Commits einer Woche aus: Arbeitszeiten, Ordner-Hotspots, PR-Größen und den größten Commit. Pro Person gibt es Lob und eine Wachstumschance; KI-Co-Autoren zählt er getrennt. Gespeicherte Ergebnisse machen Trends zwischen Retros vergleichbar.{q:3}

Die BMAD-Methode prüft mit `bmad-retrospective` ein abgeschlossenes Epic anhand von Tickets, Plänen, Diffs, Commits und Session-Logs. Jeder Befund braucht eine Fundstelle, eine Antwort auf den aktuellen Fall und eine Vorbeugung. Der Skill kontrolliert auch die Aktionspunkte der vorigen Retro.{q:4}

Squad blockiert andere Arbeit, wenn in den letzten sieben Tagen keine Retro gelaufen ist, und verlangt Aktionspunkte als GitHub Issues. Als Grund nennt der Skill ein einzelnes Projekt: Sechs Retros mit Markdown-Checklisten erledigten 0 von 23 Punkten, nach der Umstellung auf Issues waren es 4 von 4.{q:5} Das ist keine kontrollierte Messung. Issues helfen durch Zuständigkeit, Benachrichtigungen und Abfragen bei der Nachverfolgung.{q:5}

## Doctor-Werkzeuge: Zustand statt Verlauf

Claude Codes `/doctor` prüft seit Version 2.1.205 Plugins, Hooks, MCP-Konfiguration und kürzbare CLAUDE.md-Inhalte. `/doctor prompt-audit` prüft seit 2.1.283 Anweisungen für ältere Modelle; `/skill-doctor` zeigt seit 2.1.261 ungenutzte Skills und ihre Kontextkosten.{q:6} `/insights` wertet die Nutzung aus. Bei Tom Crawshaws 318 Sessions meldete der Bericht über 7.700 Bash-Befehle als Reibung: Ohne Startkontext musste der Agent im Projekt suchen.{q:9}

Alireza Rezvanis `skill-doctor` sammelt lokale Claude-Code- und Codex-Sessions, schwärzt Secrets und bewertet Effizienz und Code-Qualität. Das Modell vergibt Labels; ein Skript berechnet die Note (0,5 × Effizienz + 0,35 × Code-Qualität + 0,15 × Skill-Abdeckung). Jeder Skill-Diff braucht eine bewertete Session als Grundlage. Echte Skills ändert er erst nach deinem ausdrücklichen Ja.{q:7}

Der React-Doctor-Skill verlangt nach Änderungen `npx react-doctor@latest --scope changed` und die Behebung von Regressionen vor dem Commit. Er liefert einen Health-Score von 0 bis 100.{q:8} Ein solcher Scan passt als Retro-Vorschlag, wenn der Agent wiederholt React-Fehler übersieht.

## Grenzen

Jede Retro ist eine Interpretation des Modells und sieht nur, was in den Logs steht. Den Wert liefert erst die Umsetzung: Eine neue Linter-Regel wirkt bei jedem Lauf, ein Absatz in der CLAUDE.md nur, solange der Agent ihn beachtet. Und jeder zusätzliche Check kostet Laufzeit in Hook und CI. Prüf deshalb bei jedem Vorschlag, ob der Fehler oft genug vorkommt, damit sich der Check lohnt.

## Empfehlung

Starte `/retro` nach einer Session mit auffälligen Fehlern oder nimm gelegentlich eine vergangene Session als Stichprobe. Das entspricht Pococks Empfehlung, die Auswahl beim Menschen zu lassen.{q:10} Wähle den wichtigsten sinnvollen Vorschlag, setze ihn um und lege weitere notwendige Arbeiten als Issues an. Prüfe Setup und Skill-Liste ergänzend mit `/doctor` und `/skill-doctor`. Wie du entscheidest, ob ein Vorschlag in CLAUDE.md, Skill, Hook oder MCP gehört, steht im Beitrag zu den [Erweiterungs-Ebenen](post:welche-ebene-claude-md-skill-hook-mcp).
