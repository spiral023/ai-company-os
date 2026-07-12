# Design: Praxis-Guide für mattpocock/skills

**Datum:** 2026-07-13

## Ziel

Ein deutschsprachiger, Obsidian-kompatibler Guide unter `80_Knowledge/Guides/` erklärt Entwicklern, wie sie `mattpocock/skills` situationsgerecht kombinieren. Der Schwerpunkt liegt auf Wayfinder und dem Coding-Lifecycle, ohne die Sammlung fälschlich als starren End-to-End-Prozess darzustellen.

## Zielgruppe und Ergebnis

Der Guide richtet sich an Entwickler, die Coding Agents bereits grundsätzlich bedienen können, aber noch nicht wissen, welchen Skill sie wann einsetzen sollen. Nach der Lektüre sollen sie:

- die Philosophie kleiner, komponierbarer Skills verstehen,
- zwischen kleinen Änderungen und großen, unscharfen Vorhaben unterscheiden,
- den empfohlenen Coding-Fluss `wayfinder → to-spec → to-tickets → implement → code-review` anwenden,
- Research, Prototype, Grilling, Handoff, Teach und Architekturpflege passend einschieben,
- häufige Fehlanwendungen erkennen und vermeiden.

## Informationsarchitektur

Der Guide wird handlungsorientiert statt als vollständiger Skill-Katalog aufgebaut:

1. Kurzfassung und mentales Modell
2. Installation und Setup
3. Auswahl nach Arbeitssituation
4. Standardfluss für große Coding-Vorhaben
5. Wayfinder im Detail
6. Abkürzungen für kleine Änderungen und Bugs
7. Unterstützende Schleifen für Research, Prototyping, Lernen und Handoffs
8. Qualitäts- und Architekturpflege
9. Rezepte mit Beispielbefehlen
10. Fehlanwendungen, Grenzen und Quellenlage

Mindestens drei Mermaid-Diagramme zeigen den Lifecycle, einen Skill-Entscheidungsbaum und die Trennung zwischen user-invoked Orchestratoren und model-invoked Disziplin-Skills.

## Quellen- und Evidenzmodell

Die vom Nutzer eingefügten Tweets werden verlustfrei als einzelne Source-Notizen archiviert, soweit sie noch nicht vorhanden sind. Bestehende Sources werden nicht dupliziert. Wiederverwendbare Aussagen ergänzen passende Patterns; neue Patterns entstehen nur für eigenständige, übertragbare Konzepte.

Der Guide unterscheidet sichtbar zwischen:

- im Repository verifizierter Funktionsweise,
- Empfehlungen von Matt Pocock,
- Erfahrungsberichten Dritter,
- daraus abgeleiteten Anwendungsempfehlungen dieses Guides.

Zentrale Aussagen werden gegen `external_repos/mattpocock/skills/README.md`, `.agents/invocation.md`, `CHANGELOG.md` und die jeweils relevanten `SKILL.md`-Dateien geprüft. Abweichungen oder Unsicherheiten werden als Grenzen oder Spannungen dokumentiert.

## Änderungen im Repository

- Neue Guide-Datei unter `80_Knowledge/Guides/`
- Neue Source-Notizen für noch nicht erfasste Tweets
- Ergänzungen bestehender Pattern-Notizen; bei Bedarf wenige neue Patterns
- Aktualisierung von `80_Knowledge/Index.md` und `80_Knowledge/Vergleiche/Workflow-Frameworks.md`

Bestehende, nicht zu dieser Aufgabe gehörende Änderungen im Worktree bleiben unberührt.

## Qualitätsprüfung

- Keine unbelegten Tatsachenbehauptungen über das Skill-Repo
- Alle Mermaid-Blöcke syntaktisch einfach und Obsidian-kompatibel
- Befehle und Skill-Namen stimmen mit dem lokalen Repo überein
- Keine Duplikate in `80_Knowledge/Sources/`
- `python 70_Scripts/validate_knowledge.py` läuft fehlerfrei
- Abschließender Diff- und Konsistenz-Check der eigenen Änderungen

