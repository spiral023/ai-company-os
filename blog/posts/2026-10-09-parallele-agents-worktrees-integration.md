---
titel: "Parallele Coding-Agents mit Git Worktrees: Aufgaben trennen und zentral integrieren"
datum: 2026-10-09
kategorie: arbeitsweisen
zusammenfassung: "Teile parallele Coding-Aufgaben mit Git Worktrees klar auf. Getrennte Dateien, Ports und Testdaten sowie eine zentrale Integration machen Abhängigkeiten früh sichtbar."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-10-09-git-worktree
  - 2026-01-31-bcherny-claude-code-team-tips
---

## Kurz gesagt

- Wähle unabhängige Aufgaben und weise jedem Agent konkrete Dateien und ein prüfbares Ergebnis zu.
- Erstelle getrennte Worktrees auf derselben vereinbarten Ausgangsrevision.
- Trenne auch laufende Anwendungen, Ports und veränderliche Testdaten.
- Führe die Ergebnisse nacheinander zusammen und prüfe anschließend den gemeinsamen Stand.

## Prüfe zuerst, ob die Aufgaben unabhängig sind

Zwei Agents können gleichzeitig an getrennten Bereichen arbeiten. Dafür brauchst du eine Aufteilung, bei der ein Agent ohne laufende Entscheidungen des anderen vorankommt. Wenn beide dieselbe Schnittstelle entwerfen oder dieselbe zentrale Datei verändern müssen, besteht bereits eine Abhängigkeit.

Boris Cherny beschreibt in seinen Teamtipps vom 31. Januar 2026 parallele Claude-Sitzungen mit jeweils eigenen Git Worktrees. Das ist eine geschilderte Teampraxis ohne Benchmark, aus der sich kein bestimmter Geschwindigkeitsvorteil für dein Projekt ableiten lässt.{q:2}

Mein Vorschlag beginnt mit einem synthetischen Beispiel: Eine Kontaktverwaltung soll vorhandene Anmerkungen zusätzlich exportieren und Validierungsfehler im Kontaktformular verständlicher anzeigen. Der Datenvertrag zwischen Browser und API bleibt dabei unverändert. Beide Aufgaben verwenden bereits vorhandene Felder.

| Zuständigkeit | Aufgabe | Eigener Bereich | Gemeinsame Grenze |
|---|---|---|---|
| Export-Agent | Vorhandenes Feld in den CSV-Export aufnehmen | Exportformatierung und zugehörige Tests | Kontaktmodell und API bleiben stabil |
| Formular-Agent | Bestehende Fehler verständlich anzeigen | Formularkomponente und zugehörige Tests | Fehlerformat des Servers bleibt stabil |
| Integration | Änderungen prüfen und zusammenführen | Gemeinsamer Zielstand | Schnittstellen und Gesamtfluss kontrollieren |

Falls der Export doch ein neues Serverfeld braucht, melde diese Abhängigkeit zuerst. Der ursprünglich getrennte Auftrag hat dann seinen Umfang verändert und braucht eine abgestimmte Schnittstelle.

## Was ein Worktree trennt und was er teilt

Ein Git Worktree ist ein zusätzliches Arbeitsverzeichnis desselben Repositorys. Du kannst darin einen anderen Branch auschecken und Dateien unabhängig bearbeiten. Laut Git-Dokumentation teilen Worktrees unter anderem das Repository und seine Objekte. `HEAD`, Index und Arbeitsdateien sind jeweils getrennt; viele Referenzen, darunter die Branch-Referenzen, werden gemeinsam verwendet.{q:1}

`HEAD` bezeichnet hier den ausgecheckten Stand. Der Index hält die Änderungen für den nächsten Commit bereit. Getrennte Verzeichnisse verhindern, dass die normalen Dateiänderungen eines Agents unmittelbar im Verzeichnis des anderen erscheinen. Sie machen die spätere Zusammenführung jedoch nicht automatisch konfliktfrei.

Die folgenden PowerShell-Befehle sind ein Beispiel für ein lokales Demo-Repository. Wähle vorher den gewünschten Ausgangsstand, prüfe vorhandene Worktrees und stelle sicher, dass die neuen Branch-Namen und Zielordner frei sind:

```powershell
git worktree list
$basisCommit = git rev-parse HEAD
git worktree add -b codex/export-spalte ../demo-export $basisCommit
git worktree add -b codex/formular-fehler ../demo-formular $basisCommit
```

`git worktree add -b` erstellt einen neuen Branch und sein Arbeitsverzeichnis am angegebenen Commit. Der explizite Ausgangsstand macht die gemeinsame Basis im Beispiel nachvollziehbar.{q:1} Notiere diese Revision im Auftrag und gib jedem Agent den tatsächlichen Pfad seines Verzeichnisses.

## Trenne auch Anwendungen und Testdaten

Ein eigenes Arbeitsverzeichnis isoliert keine externe Datenbank und keinen gemeinsamen Dienst. Als eigener Vorgehensvorschlag gehört deshalb eine kurze Umgebungsprüfung vor den parallelen Start.

Verwende für jede gestartete Anwendung einen freien eigenen Port. Prüfe außerdem, ob beide Frontends auf denselben Backend-Prozess zugreifen würden. Falls du getrennte Backend-Instanzen brauchst, müssen auch deren Ports und die jeweils verwendete Clientkonfiguration zusammenpassen.

Testdaten sollten aus demselben Ausgangsbestand stammen, aber unabhängig veränderbar sein. Dafür eignen sich beispielsweise separate lokale Testdatenbanken oder getrennte temporäre Datendateien, sofern das Projekt diese Betriebsweise unterstützt. Ein Test, der Kontakte löscht oder neu anlegt, kann sonst den anderen Lauf verändern.

Prüfe die tatsächlichen Konfigurationsnamen im Projekt. Eigene lokale Umgebungsdateien können Ports und Datenpfade je Worktree festhalten. Ergänze bei Bedarf getrennte Cache- und Ausgabeordner. Die erforderlichen Schritte hängen davon ab, welche Ressourcen deine Anwendung außerhalb ihres Verzeichnisses verwendet.

## Gib jedem Agent einen vollständigen Auftrag

Im synthetischen Beispiel könnte der Auftrag für den Export so lauten:

> Arbeite ausschließlich im zugewiesenen Export-Worktree auf der genannten Ausgangsrevision. Ergänze das bereits vorhandene Anmerkungsfeld im CSV-Export. Bearbeite die Exportdateien und ihre Tests. Bewahre Kontaktmodell und API-Vertrag. Prüfe vorhandene, leere und fehlende Anmerkungen sowie Sonderzeichen. Melde zusätzliche Abhängigkeiten vor deren Änderung. Fasse Änderung, tatsächliche Prüfergebnisse und offene Punkte zusammen.

Der Formular-Agent erhält analog den Auftrag, ausschließlich die Anzeige vorhandener Validierungsfehler in seinen Formular-Dateien anzupassen. Gib ihm dieselben Grenzen für Kontaktmodell und API sowie die für seine Ansicht passenden Prüffälle.

Lege zusätzlich fest, wer gemeinsame Konfigurationen, Paketdefinitionen oder Lockdateien bearbeiten darf. Falls ein Agent eine neue Abhängigkeit benötigt, gehört diese Entscheidung in die Koordination. Ein unvermuteter gemeinsamer Dateiwechsel kann die Aufteilung sonst nachträglich auflösen.

Die [Rollen-Prompts für Claude Code und Codex](post:rollen-prompts-fuer-claude-code-und-codex) können bei der Formulierung helfen. Ergänze für parallele Arbeit immer den Arbeitsort, die Zuständigkeit und das verlangte Ergebnis.

## Integriere die Ergebnisse an einer Stelle

Mein Vorschlag für die Integration: Prüfe zuerst die Berichte und Diffs beider Agents. Achte auf unerwartete Änderungen an gemeinsamen Schnittstellen und darauf, welche Prüfungen tatsächlich gelaufen sind. Ein Bericht über vorhandene Tests ersetzt keinen Testlauf.

Führe anschließend ein Ergebnis in den vereinbarten Zielbranch ein. Prüfe diesen Zwischenstand und übernimm danach das zweite Ergebnis. Bei Konflikten vergleiche die beabsichtigten Verhaltensänderungen; eine rein mechanische Konfliktauflösung kann die Aufgabe eines Agents versehentlich entfernen.

Prüfe zum Schluss den kombinierten Ablauf mit denselben vereinbarten Erwartungen. Im Beispiel sollte das Formular weiterhin passende Fehler anzeigen, und gespeicherte Anmerkungen sollten im Export korrekt erscheinen. Diese gemeinsame Prüfung kann Probleme aufdecken, die in isolierten Komponentenprüfungen verborgen bleiben.

Breite Projektprüfungen laufen zentral am integrierten Stand. Die Agents konzentrieren ihre eigenen Prüfungen auf die bearbeiteten Bereiche. Halte fest, welche zusätzlichen Prüfungen aus der Kombination der Änderungen entstehen.

## Beende den Versuch mit einem nachvollziehbaren Stand

Parallelisierung bringt zusätzliche Aufträge, Kontext und Integrationsarbeit mit sich. Wenn Agents ständig Rückfragen zur Arbeit des anderen stellen oder dieselben Entscheidungen wiederholen, verkleinere die Aufgaben oder bearbeite die abhängigen Teile nacheinander.

Vor dem Aufräumen der Worktrees prüfst du, wo Änderungen und gegebenenfalls lokale Ergebnisse erhalten sind. Die Git-Dokumentation beschreibt `git worktree remove` zum Entfernen eines abgeschlossenen Worktrees.{q:1} Verwende die normale Prüfung des Befehls und untersuche verbleibende Änderungen, bevor du einen Arbeitsstand aufgibst.

Beginne mit dem hier beschriebenen kleinen Versuch. Entscheidend für die nächste Aufteilung sind klare Zuständigkeiten, nachvollziehbare Prüfergebnisse und ein kontrollierter gemeinsamer Stand. Ob sich der zusätzliche Aufwand lohnt, zeigt erst die Arbeit an deinen eigenen Aufgaben.
