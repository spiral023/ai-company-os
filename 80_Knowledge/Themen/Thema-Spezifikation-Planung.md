# Spezifikation & Planung

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-02. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Alles, was vor dem Code passiert: Plan Mode, Spec-First, Grilling, Task-Steuerung, Spec-Ordner, persistente Pläne. Prompt-Methoden für Klärung (Pre-Mortem, Unknowns) stehen in prompting.

## Suchbegriffe

- **Hauptkeyword:** Spec-Driven Development
- **Long-Tail:** Plan Mode Claude Code; Spec-First Development; Grill Me Skill; Plan vor Code; Spec Ordner pro Feature; Plan Annotation Workflow
- **Fragen:** Lohnt sich Plan Mode? / Wie schreibe ich eine Spec für einen Coding Agent?
- **Häufig in den Quellen:** spec-driven development (6), plan mode (4), vibe coding (3), handoff-dokument (2), design.md (2), session-kontinuität (2), claude code workflow (2), self-verification (2), plan.md (2), single-model-blindheit (2), to-tickets (2), to-spec (2), grilling (2), wayfinder (2), known unknowns (2), matt pocock skills (2), decision log, layered claude.md, spec-first development, cookbooks als tests

## Verwandte Themen

- [[Thema-Prompting-Klärung]] — Prompting & Klärung
- [[Thema-Verifikation-Tests-Review]] — Verifikation, Tests & Review
- [[Thema-Workflow-Frameworks-Tools]] — Workflow-Frameworks & Tools
- [[Thema-Kontext-Management]] — Kontext-Management

## Patterns (5)

- [[CONTEXT-Glossar]] · verifiziert · 4 Belege
- [[Plan-first-mit-getrenntem-Review]] · verifiziert · 37 Belege
- [[Spec-Grilling]] · verifiziert · 15 Belege
- [[Spec-Ordner-pro-Feature]] · meinung · 2 Belege
- [[Task-basierte-Steuerung]] · verifiziert · 14 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Agent-generierte-Schulung-mit-Curriculum-Gate]], [[Blockierende-Task-Abhaengigkeiten]], [[Fable-Unknowns-vor-Prompt-Qualitaet]], [[Handoff-Doc]], [[Intent-Engineering-als-dritte-Schicht]], [[Lovable-Prototyp-dann-lokaler-Handoff]], [[Screenshot-als-Spezifikationsmedium]], [[Voice-Prompting-fuer-Kontextreichtum]]

## Quellen (11)

- [[2026-10-02-repo-mattpocock-skills]] — Im Klon von mattpocock/skills (Stand Commit `d81f3a18`) liegen `implement-spec`, `pr` und `retro` unter `skills/engineering/`.
- [[2026-08-05-floknowsai-dein-vibe-coding-projekt-bricht-nicht-am-coding-agent-zusammen-sondern]] — Vibe-Coding-Projekte scheitern am fehlenden Fundament aus Architektur, Datenfluss und Fehlerfällen, nicht am Agenten, und Rules allein setzen Qualität nicht durch.
- [[2026-07-17-promptgefluester-ich-werd-gerade-extrem-dafuer-kritisiert-dass-ich-an-meine-videos-gesagt]] — Eine ausführliche Spezifikation mit verweisenden Task-Listen und mehrfacher Agent-Prüfung des Plans ist billiger als spätes Nachbessern, verursacht aber eigene Pflegekosten.
- [[2026-04-17-wiki-compiler-praktische-claude-code-workflows]] — Ein Fünf-Schritte-Workflow mit Plan als Datei und getrenntem Review trennt Erstellung von Prüfung und schützt vor Blindheit des einzelnen Modells.
- [[2026-04-17-wiki-compiler-kontextsteuerung-verifikation-tdd]] — Kontextmenge, Prüfbarkeit und Paketgröße bestimmen die Qualität; TDD in vertikalen Slices und gestufte Review-Eskalation verhindern spekulativen Code und Scheinfortschritt.
- [[2026-02-20-aseem-shrey-claude-codex-plan-review]] — Ein zweites Modell als Reviewer für Pläne, mit VERDICT-Protokoll und Rundenlimit, deckt blinde Flecken auf, die das planende Modell allein übersieht.
- [[2026-02-15-avid-ai-design-workflow-2026]] — KI-Design gelingt in drei Durchgängen mit Referenzen, erzwungenem Self-Review und Feinschliff; Geschmack ist der Engpass, nicht die Ausführung.
- [[2026-02-10-boris-tane-plan-annotation-workflow]] — Claude schreibt keinen Code vor einem geprüften Plan; Recherche und Plan sind persistente Markdown-Artefakte, die der Mensch per Inline-Annotation iterativ schärft.
- [[2026-02-05-kloss-xyz-feature-intelligence-architect]] — Analyse und Umsetzung trennen: Ein Read-only-Planer erzeugt eine Plan-Datei, die als Vertrag für den Build-Agenten nach Freigabe dient.
- [[2026-02-02-anthony-riera-planning-with-files-skill]] — Plan, Erkenntnisse und Fortschritt als drei Dateien halten den Agenten in langen Sessions am Ziel, kosten aber zusätzliche Token beim Wiederlesen.
- [[2026-01-14-ashpreetbedi-claude-code-spec-first]] — Ein persistenter Spec-Ordner pro Feature mit Design, Fortschritt und Entscheidungen ersetzt Chat-Gedächtnis und trägt Arbeit über Kontextlimits hinweg.

## Quellen mit diesem Thema als Nebenthema

- [[2026-07-30-julian-ivanov-interaktive-schulungen-mit-claude-code]]
- [[2026-07-26-promptgefluester-ich-hab-ne-unbequeme-wahrheit-und-zwar-ich-wurde-gefragt-wieso]]
- [[2026-07-14-fredrikharkort-5-prompts-die-weh-tun]]
- [[2026-07-13-mattpocock-handoff-to-teach]]
- [[2026-07-11-mattpocock-wayfinder-to-implementation]]
- [[2026-07-03-trq212-fable-field-guide-unknowns]]
- [[2026-07-03-trq212-2073100352921215386]]
- [[2026-05-02-vincentmumme-das-muesst-ihr-unbedingt-testen]]
- [[2026-04-16-wiki-compiler-get-shit-done-gsd]]
- [[2026-02-27-meer-claude-code-best-practices]]
- [[2026-02-04-tweag-tdd-agentic-coding]]
- [[2026-02-04-lovable-docs-prompting-debugging]]
- [[2026-02-04-lovable-docs-best-practices]]
- [[2026-02-03-god-of-prompt-karpathy-ai-coding-system-prompt]]
- [[2026-01-31-bcherny-claude-code-team-tips]]
- [[2026-01-23-nummanali-claude-task-system]]
- [[2026-01-15-elenakvcs-vibe-coding-beginner-guide]]
