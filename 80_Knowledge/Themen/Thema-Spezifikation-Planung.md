# Spezifikation & Planung

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-10. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Alles, was vor dem Code passiert: Plan Mode, Spec-First, Grilling, Task-Steuerung, Spec-Ordner, persistente Pläne. Prompt-Methoden für Klärung (Pre-Mortem, Unknowns) stehen in prompting.

## Suchbegriffe

- **Hauptkeyword:** Spec-Driven Development
- **Long-Tail:** Plan Mode Claude Code; Spec-First Development; Grill Me Skill; Plan vor Code; Spec Ordner pro Feature; Plan Annotation Workflow
- **Fragen:** Lohnt sich Plan Mode? / Wie schreibe ich eine Spec für einen Coding Agent?
- **Häufig in den Quellen:** spec-driven development (6), grilling (5), plan mode (4), spec (4), spec-grilling (4), wayfinder (4), design.md (3), plan.md (3), vibe coding (3), handoff-dokument (2), session-kontinuität (2), claude code workflow (2), self-verification (2), single-model-blindheit (2), plan (2), planung (2), plan-first (2), skill (2), skill.md (2), to-spec (2)

## Verwandte Themen

- [[Thema-Prompting-Klärung]] — Prompting & Klärung
- [[Thema-Verifikation-Tests-Review]] — Verifikation, Tests & Review
- [[Thema-Workflow-Frameworks-Tools]] — Workflow-Frameworks & Tools
- [[Thema-Kontext-Management]] — Kontext-Management
- [[Thema-AI-nativer-SDLC]] — AI-nativer SDLC

## Patterns (8)

- [[Architektur-in-Perspektiven-dokumentieren]] · verifiziert · 4 Belege
- [[CONTEXT-Glossar]] · verifiziert · 8 Belege
- [[Codepfad-vor-Aenderung-nachvollziehen]] · meinung · 1 Belege
- [[Plan-first-mit-getrenntem-Review]] · verifiziert · 44 Belege
- [[Projektkarte-als-Status-und-Entscheidungsartefakt]] · meinung · 1 Belege
- [[Spec-Grilling]] · verifiziert · 18 Belege
- [[Spec-Ordner-pro-Feature]] · meinung · 2 Belege
- [[Task-basierte-Steuerung]] · verifiziert · 16 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Abstraktionswert-mit-Deletion-Test-pruefen]], [[Agent-generierte-Schulung-mit-Curriculum-Gate]], [[Blockierende-Task-Abhaengigkeiten]], [[Fable-Unknowns-vor-Prompt-Qualitaet]], [[Fachregel-Konsolidierung-vor-Featureaenderung]], [[Handoff-Doc]], [[Intent-Engineering-als-dritte-Schicht]], [[Lovable-Prototyp-dann-lokaler-Handoff]], [[Screenshot-als-Spezifikationsmedium]], [[Variantenvergleich-vor-Produktionsabnahme]], [[Voice-Prompting-fuer-Kontextreichtum]]

## Quellen (19)

- [[2026-10-09-openai-codebase-onboarding]] — Ein begrenzter Codepfad wird durch Dateien, Zustandswechsel und offene Fragen nachvollzogen.
- [[2026-10-08-mattpocockuk-2108216899439894574]] — Matt Pocock empfiehlt bei winzigen Änderungen direktes Umsetzen: Ist der Diff schnell prüfbar und ein neuer Versuch fast kostenlos, lohnt ausführliches „Grilling“ weniger.
- [[2026-10-06-voxyz_ai-2107455844992299272]] — Vox schlägt für längere autonome Arbeit mit `Opus 5.5` einen `project-map`-Subagent vor: `medium` für die Karte, während die Hauptsession mit `high` weiterarbeitet.
- [[2026-10-05-voxyz_ai-2107214251408433365]] — Vox nimmt ein bald zurückgesetztes Wochenlimit mit **mehr als der Hälfte** Restkapazität zum Anlass, sinnvolle Aufgaben für `Opus 5.5` vorzuschlagen; das Verfahren sei auch auf `Sol` in Codex anwendba
- [[2026-10-05-repo-squad-retro-enforcement]] — Im Klon von bradygaster/squad (Branch `dev`, Stand Commit `d2364dfe`) liegt die Skill-Vorlage `templates/skills/retro-enforcement/SKILL.md`.
- [[2026-10-05-repo-bmad-method-retrospective]] — Im Klon von bmad-code-org/BMAD-METHOD (Stand Commit `8f2c13d`) liegt `skills/bmad-retrospective/` mit `workflow.md` und fünf Referenzdateien.
- [[2026-10-02-repo-mattpocock-skills]] — Im Klon von mattpocock/skills (Stand Commit `d81f3a18`) liegen `implement-spec`, `pr` und `retro` unter `skills/engineering/`.
- [[2026-08-05-floknowsai-dein-vibe-coding-projekt-bricht-nicht-am-coding-agent-zusammen-sondern]] — Vibe-Coding-Projekte scheitern am fehlenden Fundament aus Architektur, Datenfluss und Fehlerfällen, nicht am Agenten, und Rules allein setzen Qualität nicht durch.
- [[2026-07-31-alexfinn-2082982462012227648]] — Alex Finn nennt seine Vorgehensweise Reverse Prompting: Nach einer Beschreibung von Zielen und Umständen soll der Agent fehlende Informationen erfragen und mögliche Aufgaben vorschlagen.
- [[2026-07-23-ccarlosai-2080339591014261034]] — Carlos beschreibt eine Planungssitzung, die vorhandenen Projektkontext durch Rückfragen ergänzt und anschließend in Dateien für Claude Code überführt.
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

- [[2026-10-10-repo-oh-my-mermaid-architektur]]
- [[2026-10-09-voxyz_ai-2108543002830360775]]
- [[2026-10-09-shadcn-2108574564586332615]]
- [[2026-10-08-voxyz_ai-2108324058739745228]]
- [[2026-10-05-aihero-v1-3-implement-spec-pr-retro-and-glossary-md]]
- [[2026-10-01-mattpocockuk-2105563604384915639]]
- [[2026-09-24-mattpocock-ai-coding-dictionary]]
- [[2026-09-20-eric-tech-claude-code-the-complete-ai-native-sdlc-guide]]
- [[2026-09-15-emilkowalski-2099948779864793303]]
- [[2026-09-05-waynesutton-2096296858343846261]]
- [[2026-07-30-julian-ivanov-interaktive-schulungen-mit-claude-code]]
- [[2026-07-26-promptgefluester-ich-hab-ne-unbequeme-wahrheit-und-zwar-ich-wurde-gefragt-wieso]]
- [[2026-07-21-claudedevs-2079654423828304282]]
- [[2026-07-14-fredrikharkort-5-prompts-die-weh-tun]]
- [[2026-07-13-mattpocock-handoff-to-teach]]
- [[2026-07-11-mattpocock-wayfinder-to-implementation]]
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
