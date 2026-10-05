---
titel: "Retro-Skill für Claude Code: Fehler einer Session in Checks verwandeln"
datum: 2026-10-06
kategorie: arbeitsweisen
zusammenfassung: "Matt Pococks Retro-Skill wertet eine Coding-Session aus und macht aus Agent-Fehlern Linter-Regeln, Hooks und bessere Navigation. Dazu der Vergleich mit anderen Retros und mit Doctor-Werkzeugen wie /doctor, /skill-doctor und React Doctor."
status: freigegeben
geprueft_am: 2026-10-05
freigabe: automatisch
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
---

## Kurz gesagt

- Lass nach einer holprigen Session `/retro` aus Matt Pococks Skill-Sammlung laufen. Er schlägt Änderungen an der Umgebung vor, damit derselbe Fehler nicht wieder passiert.
- Mechanische Fehler gehören in einen Linter, Pre-Commit-Hook oder CI-Job. Regeln in Prosa bleiben für Ermessensfragen.
- Doctor-Werkzeuge prüfen den aktuellen Zustand von Setup oder Code. Eine Retro fragt, was in einer konkreten Session schiefging, deshalb brauchst du beides.
- Mach aus jedem Retro-Ergebnis ein Ticket oder einen Commit, sonst bleibt es folgenlos.

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

Matt Pocock hat `retro` mit Version 1.3.0 seiner Skill-Sammlung in den Engineering-Bereich übernommen, seitdem steckt der Skill im Claude-Code-Plugin.{q:1} Du rufst ihn selbst auf, Claude startet ihn nie eigenständig. Ohne Angabe wertet er die laufende Session aus, sonst die genannte.{q:1}

Der Skill sucht in sieben Bereichen nach Verbesserungen: Navigation, automatische Checks, Coding Standards für den Review-Agent, eine zu große globale AGENTS.md, teure Tool-Aufrufe, Anweisungen ohne Wirkung und fehlender Zugang zu Informationen wie Logs des Dev-Servers.{q:1} Am Ende stehen Vorschläge, sortiert nach Schwere. Umsetzen musst du sie selbst oder in einem neuen Auftrag.

Ein Beispiel für Navigation: Hat der Agent lange gesucht, bis er die richtige Konfigurationsdatei fand, schlägt die Retro einen Hinweis in der CLAUDE.md vor, der direkt dorthin zeigt. Ein Beispiel für Checks: Hat er einen Import in falscher Form geschrieben und erst der Review hat es bemerkt, wird daraus eine Linter-Regel.

## Checks schlagen Regeln

Der Skill stuft jeden Verstoß gegen Coding Standards zuerst als mechanisch oder als Ermessensfrage ein. Mechanisch heißt: ein festes Syntaxmuster, eine verbotene API, eine Importform, ein falscher Dateiort. Dafür baut die Retro eine deterministische Prüfung, also eine eigene Linter-Regel, einen Pre-Commit-Hook oder einen CI-Job, je nachdem, was im Repo am wenigsten Aufwand macht.{q:1} Nur echte Ermessensfragen landen als Text in `CODING_STANDARDS.md`. Ein Repo ganz ohne Pre-Commit-Hook und ohne CI-Job für Lint, Typecheck und Tests zählt selbst schon als Befund.{q:1}

Die Begründung liefert Pocock in seinem Vortrag zum PR-Engpass. Der Agent, der implementiert, steht unter dem größten Kontextdruck, er muss suchen, schreiben und debuggen. Der Review-Agent bekommt nur den Diff. Standards gehören deshalb in eine eigene Datei für den Review und nicht in die AGENTS.md, die jeder Agent bei jedem Start lädt.{q:2} `/retro` ist in diesem Ablauf der letzte Schritt, der Funde aus dem Review in Checks und Standards überführt.{q:2} Warum eine Prosa-Regel für Pflichtvorgaben zu schwach ist, zeigt auch der Beitrag zu [Deny-Rules statt Bitte](post:deny-rules-statt-bitte).

## Andere Retros: Woche, Epic, Pflichttermin

Garry Tans gstack hat ebenfalls einen `/retro`, der aber eine andere Frage beantwortet. Er wertet die Commits einer Woche aus: wann gearbeitet wurde, welche Ordner Hotspots sind, wie groß die PRs waren und welcher Commit der größte war. Im Team gibt es pro Person Lob und eine Wachstumschance, KI-Co-Autoren zählt er getrennt als eigene Kennzahl.{q:3} Ergebnisse speichert er, damit die nächste Retro Trends vergleichen kann.{q:3} Das ist ein Rückblick auf Produktivität, die Agent-Umgebung bleibt außen vor.

Die BMAD-Methode prüft mit `bmad-retrospective` ein abgeschlossenes Epic gegen die Spuren, die es hinterlassen hat: Tickets, Pläne, Diffs, Commits, Session-Logs. Jeder Befund braucht eine Fundstelle, sonst fliegt er raus. Zu jedem Befund gibt es zwei Antworten, was mit diesem Fall passiert und was den nächsten verhindert.{q:4} Außerdem kontrolliert der Skill, ob die Aktionspunkte der vorigen Retro umgesetzt wurden.{q:4}

Squad geht die Nachverfolgung noch härter an. Es blockiert jede andere Arbeit, wenn in den letzten sieben Tagen keine Retro gelaufen ist, und lässt Aktionspunkte nur als GitHub Issue zu. Als Grund nennt der Skill Zahlen aus einem einzelnen Projekt: Sechs Retros mit Markdown-Checklisten erledigten 0 von 23 Punkten, nach der Umstellung auf Issues waren es 4 von 4.{q:5} Das ist keine kontrollierte Messung. Die Erklärung im Skill überzeugt trotzdem: Eine Markdown-Checkliste hat keinen Verantwortlichen, schickt keine Benachrichtigung und lässt sich nicht abfragen.{q:5}

## Doctor-Werkzeuge: Zustand statt Verlauf

Claude Code bringt drei eingebaute Diagnosebefehle mit. `/doctor` ist seit Version 2.1.205 ein vollständiger Setup-Check, der Fehler in Plugins, Hooks und MCP-Konfiguration findet und behebt. Er schlägt vor, CLAUDE.md-Dateien um Inhalte zu kürzen, die Claude aus dem Code ableiten kann, und prüft mit `/doctor prompt-audit` seit 2.1.283, ob Skills und Anweisungen noch für ältere Modelle geschrieben sind.{q:6} `/skill-doctor` zeigt seit 2.1.261, welche geladenen Skills ungenutzt bleiben und wie viel Kontext sie kosten.{q:6} `/insights` wertet deine Nutzung aus. Tom Crawshaw ließ damit 318 Sessions analysieren. Als eine Reibung meldete der Bericht über 7.700 Bash-Befehle, weil der Agent ohne Startkontext im Projekt suchen musste.{q:9}

Der gleichnamige `skill-doctor` aus der Sammlung von Alireza Rezvani geht weiter. Er sammelt lokale Sessions von Claude Code und Codex, schwärzt Secrets und bewertet jede Session nach Effizienz und Code-Qualität. Das Modell vergibt nur Labels, die Gesamtnote rechnet ein Skript aus (0,5 × Effizienz + 0,35 × Code-Qualität + 0,15 × Skill-Abdeckung).{q:7} Jeder vorgeschlagene Skill-Diff muss auf eine bewertete Session verweisen, und deine echten Skills ändert er nur nach ausdrücklichem Ja.{q:7}

React Doctor ist ein Doctor im engsten Sinn. Nach jeder Änderung führt der Agent `npx react-doctor@latest --scope changed` aus und behebt Regressionen, bevor er committet; das Ergebnis ist ein Health-Score von 0 bis 100.{q:8} Das passt zu `/retro`: Wenn eine Retro ergibt, dass der Agent wiederholt React-Fehler übersieht, ist ein solcher Scan der Check, den sie vorschlagen würde.

## Grenzen

Jede Retro ist eine Interpretation des Modells und sieht nur, was in den Logs steht. Den Wert liefert erst die Umsetzung: Eine neue Linter-Regel wirkt bei jedem Lauf, ein Absatz in der CLAUDE.md nur, solange der Agent ihn beachtet. Und jeder zusätzliche Check kostet Laufzeit in Hook und CI. Prüf deshalb bei jedem Vorschlag, ob der Fehler oft genug vorkommt, damit sich der Check lohnt.

## Empfehlung

Starte `/retro` nach jeder Session, in der du den Agent mehr als einmal korrigieren musstest. Setz den wichtigsten mechanischen Vorschlag sofort als Linter-Regel oder Hook um und leg den Rest als Issue an. Lass `/doctor` und `/skill-doctor` einmal im Monat laufen, um Setup und Skill-Liste schlank zu halten. Wie du entscheidest, ob ein Vorschlag in CLAUDE.md, Skill, Hook oder MCP gehört, steht im Beitrag zu den [Erweiterungs-Ebenen](post:welche-ebene-claude-md-skill-hook-mcp).
