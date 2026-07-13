---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-17
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Kontextsteuerung, Verifikation und TDD mit Claude Code“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/02-agent-guides-und-templates/wka-kontextsteuerung-verifikation-und-tdd-mit-claude-code-2026-04-17.md`), synthetisiert aus mehreren X-Posts, aihero.dev, tweag.github.io Agentic Coding Handbook und offizieller Claude-Code-Doku.

Kernpunkte (kondensiert):

- Drei Faktoren bestimmen die Qualität: Kontextmenge, Prüfbarkeit, Arbeitspaketgröße. Kippt einer, kippt der Workflow (zu viel Kontext → Drift; fehlende Prüfschritte → Scheinfortschritt; zu große Pakete → spekulativer Code).
- Verifikation ist der stärkste Hebel: explizite Testfälle, reproduzierbare Shell-Befehle, erwartete Ausgaben, Screenshots bei UI-Arbeit sind starke Prüfformen; „mach das sauberer“ oder „fix den Bug“ ohne Fehlerbild sind schwache Prüfformen.
- Robustes TDD-Muster für Agenten: genau einen fehlschlagenden Test schreiben → nur minimalen Code ergänzen, damit er grün wird → erst danach aufräumen/abstrahieren. Diese vertikalen Slices werden als Tracer-Bullets bezeichnet; sie verhindern, dass der Agent zuerst eine breite Implementierung fantasiert und Tests danach passend umformt.
- Gute Tests prüfen Verhalten über öffentliche Schnittstellen, überleben Refactorings, minimieren Mocks; schlechte Tests binden sich an interne Aufrufe oder bestätigen nur Mock-Interaktionen.
- Eskalationsstufen für Review: (1) normale Selbstverifikation durch Tests/Builds, (2) zweite Session mit Review-Auftrag, (3) separater Reviewer-Subagent, (4) modellübergreifende Review-Schleife bei hoher Tragweite.
- Häufige Fehlmuster: Kitchen-Sink-Session, Horizontal Slicing (erst ganzes Feature, dann Tests), Symptom-statt-Ursache, Mock-Illusion, Patchen-statt-Neustart.

## Kernaussagen

- Kontext, Prüfbarkeit und Arbeitspaketgröße bestimmen gemeinsam die Qualität agentischer Arbeit; ein einzelner Fehlfaktor kippt den ganzen Workflow → [[Plan-first-mit-getrenntem-Review]]
- TDD in vertikalen Slices (ein fehlschlagender Test → minimaler Code → Refactor) als Tracer-Bullet gegen spekulativen Code → [[TDD-als-Verifikationshebel]]
- Vierstufige Review-Eskalation je nach Tragweite (Selbstverifikation → zweite Session → Subagent-Reviewer → modellübergreifend) → [[TDD-als-Verifikationshebel]], [[Plan-first-mit-getrenntem-Review]]
