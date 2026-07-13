---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-13
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Eine gute AGENTS.md schreiben“

## Inhalt

Interner Wiki-Artikel aus einem fremden Repo (`vibe-repo`, Pfad `docs/70_generated/wiki/03-methoden-und-tooling/02-agent-guides-und-templates/wka-gute-agents-md-schreiben-2026-04-13.md`, per WebFetch/Dateizugriff abgerufen). Behandelt Best Practices für `AGENTS.md`/`CLAUDE.md`/`GEMINI.md`.

Kernpunkte (kondensiert, Volltext im Originalpfad einsehbar):

- LLMs sind zustandslos: Alles, was der Agent über eine Codebasis weiß, muss ihm bei jeder neuen Session erneut über Kontext gegeben werden.
- Eine gute Agent-Datei beantwortet auf hoher Ebene **Was** (Stack, Struktur), **Warum** (Ziel, Zweck der Teile) und **Wie** (Arbeitsweise, Tools, Test-/Build-Pfade).
- Zu viele Spezialregeln in der Agent-Datei sind kontraproduktiv: Das Instruktionsbudget ist begrenzt, und Harnesses können dem Modell erlauben, als irrelevant wirkenden Kontext zu ignorieren.
- Best Practice: „So viel wie nötig, so wenig wie möglich“ — nur universell auf fast jede Aufgabe anwendbare Instruktionen gehören in die Hauptdatei.
- Progressive Disclosure als Lösung für mehr Kontextbedarf: Startdatei beschreibt nur Grundlagen und verweist auf spezialisierte Zusatzdokumente (z.B. `agent_docs/building_the_project.md`), die nur bei Bedarf geladen werden.
- Verweise auf Primärquellen/konkrete Dateien und Zeilen sind robuster als kopierte Code-Snippets oder duplizierte Regeln.
- `AGENTS.md` ist kein Linter: Stil-/Formatregeln gehören in deterministische Tools (Formatter, Linter, Typechecker), nicht in die Agent-Datei.
- Auto-generierte Agent-Dateien sind riskant, weil sie hohe Hebelwirkung auf praktisch jede Arbeitsphase haben — jede Zeile sollte bewusst gewählt sein.

## Kernaussagen

- Agent-Dateien sollen kurz, universell relevant und nach Progressive Disclosure gestaffelt sein statt eine Sammelstelle für Spezialregeln zu werden → [[AGENTS-md-Onboarding-Design]]
- Stil- und Formatregeln gehören in deterministische Tools, nicht in die Agent-Datei → [[AGENTS-md-Onboarding-Design]]
