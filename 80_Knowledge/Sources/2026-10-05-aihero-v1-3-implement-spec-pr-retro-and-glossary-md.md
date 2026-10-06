---
url: https://www.aihero.dev/skills/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md
autor: Matt Pocock
datum: 2026-10-05
erfasst: 2026-10-05
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-10-05-aihero-v1-3-implement-spec-pr-retro-and-glossary-md.md
---

# Matt Pococks Skills 1.3: Umsetzung, menschlicher Review und Retro als zusammenhängender Ablauf

Matt Pocock erweitert seine Skill-Sammlung um den hinteren Teil des Entwicklungsablaufs: Eine Spec mit Tickets wird umgesetzt, ein PR für den menschlichen Review aufbereitet und die Agent-Umgebung anhand einer Session verbessert. Der Beitrag beschreibt Version 1.3 und verweist auf das vollständige Release 1.3.1. Im lokalen Repo bestätigt das Changelog die Einführung der Skills mit 1.3.0 und einen korrigierten Verweis auf `/retro` nach Bugfixes mit 1.3.1.

## Eine große Spec wird zum Task-Graphen

Die Vorbereitung bleibt `/grill-with-docs` → `/to-spec` → `/to-tickets`. `/implement` bearbeitet weiterhin ein einzelnes Ticket. Das vom Nutzer aufgerufene `/implement-spec` übernimmt dagegen die ganze Spec: Es liest blockierende Ticket-Abhängigkeiten, startet Implementierungs-Subagents für ausführbare Tickets in eigenen Worktrees und führt fertige Arbeit auf einer gemeinsamen Integrationsbranch zusammen. Neue Tickets werden ausführbar, sobald ihre Voraussetzungen erledigt sind. Am Schluss folgen `/code-review` und die Behebung der Review-Funde.

Ziel ist die fertig umgesetzte Integrationsbranch. Ein Draft-PR entsteht nur auf Wunsch oder wenn der Issue-Tracker Arbeit über PRs schließt. Pocock empfiehlt für die meisten Nutzer weiterhin eine deterministische Schleife, in der ein Script Tickets mit `/implement` abarbeitet. Die Agent-Schleife ist für ihn ein Einstieg in unbeaufsichtigte Umsetzung, bevor eine solche Steuerung eingerichtet ist; sein Zuverlässigkeits- und Kostenurteil ist keine vergleichende Messung.

Die große gemeinsame Branch bleibt ausdrücklich ein ungelöstes Problem. Worktrees verschieben Kollisionen auf den Merge: Zwei Tickets können beispielsweise dasselbe Feld unter unterschiedlichen Namen einführen. Parallele Umsetzung garantiert daher weder konfliktfreie Integration noch einen kleinen Review-Umfang.

## Ein PR braucht Orientierung, Ausführungsnachweise und Risikoeinordnung

Der automatisch durch das Modell aufrufbare `/pr` gibt eine Vorlage mit drei Teilen vor:

- **Summary:** die kleinste hilfreiche Darstellung, etwa Pseudocode, ein Aufrufbaum, eine Dateistruktur oder Mermaid.
- **Evidence:** ein konkretes Vorher/Nachher, beispielsweise ein zuvor fehlgeschlagener und danach erfolgreicher Test oder Screenshots.
- **Merge Danger:** Rücknehmbarkeit der Änderung und Blast Radius. Ein Revert macht externe Folgen wie bereits versendete E-Mails nicht rückgängig.

Pocock will damit menschliche Review-Zeit auf die riskanten Stellen lenken. Seine Aussage, dass der Skill bei seinem verwendeten Modell zuverlässig geladen werde, ist eine persönliche Beobachtung. Die Vorlage ersetzt keine Prüfung und verkleinert den Diff nicht.

## Retro: Der Mensch wählt, mechanische Fehler werden Checks

`/retro` wird ausdrücklich vom Nutzer gestartet. Es liest die aktuelle oder eine benannte vergangene Session und liefert nach Schwere sortierte Verbesserungen für Navigation, automatische Checks, Coding Standards, globale `AGENTS.md`, Tool-Ökonomie, wirkungslose Anweisungen und Informationszugang.

Vor einer Änderung wählt der Nutzer aus diesen Vorschlägen. Pocock rät von einer automatisch wiederholten Retro ab: Falsch positive Funde könnten fortlaufend unnötige Umbauten auslösen. Er empfiehlt Stichproben oder Sessions mit auffälligem Agent-Verhalten. Das lokale `retro/SKILL.md` endet bei der Präsentation der Vorschläge; es enthält keinen selbstständigen Umsetzungsschritt.

Mechanische Verstöße gehören in deterministische Linter-Regeln, Pre-Commit-Hooks oder CI-Jobs. `CODING_STANDARDS.md` ist für Ermessensfragen vorgesehen. Vor neuen Checks sind vorhandene Prüfkommandos und deren tatsächliche Einbindung zu prüfen. Eine fehlende Absicherung ist selbst ein Befund. `/ask-matt` verweist nach `/code-review` und nach behobenen Bugs auf die Retro.

## Migration und verlässliche Skill-Aufrufe

`CONTEXT.md` und `CONTEXT-MAP.md` heißen jetzt `GLOSSARY.md` und `GLOSSARY-MAP.md`. Die Skills suchen nur die neuen Namen. Bestehende Dateien sollen gemeinsam in einem Commit umbenannt werden; sonst kann ein bereits aktualisierter Agent ein leeres Glossar neben dem alten anlegen. Die Arbeitsweise bleibt unverändert.

Skills rufen andere Skills nun ausdrücklich über das Skill-Tool auf. Die bloße Erwähnung eines Skill-Namens hatte laut Pocock nicht zuverlässig geladen. Nur vom Nutzer aufrufbare Skills bleiben beim Nutzer. `resolving-merge-conflicts` entfällt; vorhandene Installationen können eine veraltete Kopie behalten. Außerdem behebt das Release ungültiges YAML, durch das sechs Skills bei der Installation übersprungen wurden.

## Einordnung

Der Beitrag ist eine Primärdarstellung des Autors. Die Beschreibungen von `/retro`, `/pr`, `/implement-spec` und der Glossar-Migration wurden am vorhandenen lokalen Repo gegengeprüft; die Skills wurden nicht ausgeführt. Belastbar sind damit die vorgesehenen Abläufe, nicht deren Wirksamkeit in eigenen Projekten. Die Retro ergänzt die bestehende Trennung zwischen deterministischer Prüfung und Modellurteil. Für das Review-Problem liefert Pocock eine bessere PR-Aufbereitung, nennt die große Integrationsbranch aber weiterhin als Grenze.

## Kernaussagen

- Blockierende Ticket-Abhängigkeiten steuern, welche Arbeit parallel starten kann; die gemeinsame Integration bleibt ein eigener Aufwand. → [[Blockierende-Task-Abhaengigkeiten]]
- Mechanische Fehler werden deterministische Checks; die menschliche Auswahl schützt vor unnötigen Retro-Umbauten. → [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]
- Die Glossar-Konvention ist mit 1.3 veröffentlicht; eine gemeinsame Umbenennung verhindert parallele alte und neue Dateien. → [[CONTEXT-Glossar]]

## Verbindungen

- [[2026-10-05-repo-mattpocock-skills-retro]]
- [[2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck]]
- [[Plan-first-mit-getrenntem-Review]]
- [[Skill-Call-Hierarchie]]
