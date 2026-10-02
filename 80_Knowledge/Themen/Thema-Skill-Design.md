# Skill-Design

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-02. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Aufbau, Trigger und Qualität von Skills (SKILL.md), Aufrufhierarchie, Evals und Baselines, Skills als Teamwissen. Wayfinder und Frameworks aus Skill-Sammlungen stehen in frameworks.

## Suchbegriffe

- **Hauptkeyword:** Claude Code Skills
- **Long-Tail:** Skill Description schreiben; Skill Evals Baseline; SKILL.md Aufbau; Skills vs. Slash Commands; Skill Trigger optimieren; Skills als Teamwissen
- **Fragen:** Wann lohnt sich ein eigener Skill? / Warum löst mein Skill nicht aus?
- **Häufig in den Quellen:** progressive disclosure (10), claude code skills (7), skill description (6), skill.md (5), slash commands (4), skill evals (4), mattpocock/skills (4), grill-me (4), claude code hooks (4), wayfinder (4), claude skills (3), skill-creator (3), undertriggering (3), to-tickets (3), to-spec (3), agents.md (3), skill-trigger (2), baseline-vergleich (2), subagents (2), agent skills (2)

## Verwandte Themen

- [[Thema-Hooks-MCP-Erweiterungs-Ebenen]] — Hooks, MCP & Erweiterungs-Ebenen
- [[Thema-Workflow-Frameworks-Tools]] — Workflow-Frameworks & Tools
- [[Thema-Agent-Dateien-Memory]] — Agent-Dateien & Memory
- [[Thema-Verifikation-Tests-Review]] — Verifikation, Tests & Review

## Patterns (9)

- [[Anti-Rationalization-Tables]] · verifiziert · 3 Belege
- [[Freiheitsgrad-nach-Aufgaben-Fragilitaet]] · meinung · 8 Belege
- [[Hook-erzwungene-Skill-Aktivierung]] · meinung · 4 Belege
- [[Klein-und-komposierbar]] · verifiziert · 16 Belege
- [[One-File-per-Failure-Mode]] · verifiziert · 3 Belege
- [[Skill-Call-Hierarchie]] · verifiziert · 11 Belege
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]] · verifiziert · 18 Belege
- [[Skill-Schwellenwert-institutionelles-Wissen]] · meinung · 3 Belege
- [[Skill-aus-Demonstration-statt-Beschreibung]] · meinung · 3 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Erweiterungs-Ebenen-Zuordnung]], [[Hillclimbing-mit-Holdout-Split]]

## Quellen (18)

- [[2026-10-02-repo-anthropics-skills]] — Im Klon von anthropics/skills (Stand Commit `8a1541c4`) enthält der Skill `skills/claude-api/` unter `shared/evals/` die Anleitungen `build-eval.md`, `eval-hillclimb.md`, `cost-hillclimb.md` und `eval
- [[2026-09-14-code-test-plugins-with-evals-claude-code-docs]] — Plugins und Skills lassen sich per Eval mit und ohne Plugin vergleichen; das Delta zeigt den Beitrag, ein negatives Delta verdächtigt zuerst den Judge.
- [[2026-07-30-julian-ivanov-interaktive-schulungen-mit-claude-code]] — Ein Skill kann Briefing, Curriculum-Freigabe und Medienproduktion zu einem wiederholbaren Kurs-Workflow verbinden, wobei ein menschliches Review-Gate teure Fehlproduktion verhindert.
- [[2026-07-21-promptgefluester-prompt-engineering-ist-tot-und-keiner-hats-gemerkt-was-meine-ich-damit]] — Statt eines langen Initial-Prompts erzeugen Rückfrage-Skills sauberen Basis-Kontext und Hook-Skills laden Regeln im Prozess nach, weil frühe Regeln im wachsenden Kontext verblassen.
- [[2026-07-10-voxyz-mattpocock-skills]] — Eine kleine Sammlung Markdown-Skills mit Aufrufhierarchie, gemeinsamem Projekt-Glossar und Handoff ist ein leichtgewichtiger, komponierbarer Agent-Stack unter menschlicher Prozesskontrolle.
- [[2026-07-08-mattpocock-custom-issue-tracker]] — Workflow-Skills lassen sich per Setup-Befehl an jeden programmierbar erreichbaren Issue-Tracker anbinden, weil Arbeitslogik und Tracker-Anbindung getrennt sind.
- [[2026-07-06-mattpocock-writing-great-skills-beyond-skills]] — Struktur, Leading Words und Pruning, entwickelt für Skills, verbessern jeden Text, den Agenten lesen, von AGENTS.md über Specs bis zu AFK-Prompts.
- [[2026-07-01-anthropic-skill-creator-skill-md]] — Der offizielle skill-creator deckt Erstellen, Evals mit Baseline, Varianz-Benchmarks, automatisierte Trigger-Optimierung und Blind-Vergleich ab; simple Ein-Schritt-Queries triggern Skills nie.
- [[2026-06-04-agenticjames-most-people-have-not-touched-the-best-parts-of-claude-code-skills-forked]] — Mit context: fork und model im Skill-Frontmatter läuft ein teures Modell nur für eine Aufgabe, ohne den Hauptkontext zu füllen; imperative Descriptions sollen besser triggern.
- [[2026-04-16-wiki-compiler-skill-creator-skill]] — Skills sind messbare Produkte: Wer sie mit und ohne Skill vergleicht und die Trigger-Description schärft, statt nach Gefühl zu bewerten, verbessert sie belegbar.
- [[2026-02-27-thariq-lessons-building-claude-code]] — Tools müssen zum Fähigkeitsprofil des Modells passen und bei jedem Modell-Upgrade neu geprüft werden; Formattreue gehört in Tool-Verträge statt in Freitext-Prompts.
- [[2026-02-11-rohit4verse-guide-building-agent-skills]] — Vor dem Bau eines Skills Erfolgskriterien wie Trigger-Trefferquote festlegen; die description folgt dem Muster was plus wann, allowed-tools begrenzt Rechte.
- [[2026-02-09-pdrmnvd-how-claude-code-skills-work]] — Skills laden Fachwissen in drei Stufen erst bei Bedarf; die description ist der Trigger, und Anweisungs-Spezifität richtet sich nach der Fragilität der Aufgabe.
- [[2026-02-04-meer-aiit-claude-skills-complete-guide]] — Die description steuert das Triggern eines Skills; SKILL.md kurz halten, Details in references auslagern und Skripte für Deterministisches nutzen.
- [[2026-02-01-anthropic-docs-extend-claude-with-skills]] — Ein Skill ist SKILL.md mit Frontmatter, das Auslösung, Rechte und Ausführung steuert; triggert er nicht, liegt es meist an der description.
- [[2026-01-21-tempoimmaterial-agent-skills-vs-rules-vs-commands]] — Rules gelten immer, Commands sind explizit, Skills optional und selbst geladen; gute Skills haben eine Routing-Description und eine Prozedur statt Enzyklopädie.
- [[2026-01-21-meta-alchemist-claude-skills-deep-dive]] — Ein Vendor-Benchmark für Skills überzeugt erst mit Stichprobengröße, Varianz und unabhängiger Prüfung; das Prinzip mit/ohne Skill zu testen bleibt richtig.
- [[2025-10-31-agenticjames-best-claude-skills-for-agentic-coding]] — Skills lassen sich für Marke, Debugging und Selbstgenerierung nutzen, doch automatisch erzeugte Skills ohne Review riskieren Wildwuchs und schlechte Trigger.

## Quellen mit diesem Thema als Nebenthema

- [[2026-10-02-repo-mattpocock-skills]]
- [[2026-10-02-repo-latent-spaces-brag]]
- [[2026-09-28-claude-automating-eval-design-and-hillclimbing-with-cla]]
- [[2026-09-21-voxyz_ai-2102050225443766571]]
- [[2026-09-20-voxyz_ai-2101657631249031507]]
- [[2026-09-14-developers-rethinking-skills-and-prompts-for-gpt-6-astra-op]]
- [[2026-09-04-pvncher-2095991462416490862]]
- [[2026-08-25-vikingmute-2092059170812108811]]
- [[2026-08-21-promptgefluester-wie-macht-man-refactering-bei-einer-richtig-grossen-code-base-mit-aeh]]
- [[2026-08-21-promptgefluester-agent-plug-ins-das-ist-der-neue-standard-mit-dem-die-grossen-ai]]
- [[2026-08-14-agenticjames-ai-memory-is-trash-heres-some-solutions]]
- [[2026-08-05-creatoreconomy-use-my-human-review-skill-to-edit-html-and-markd]]
- [[2026-07-08-mattpocock-skills-v1-1]]
- [[2026-07-06-nightmoon-wayfinder]]
- [[2026-04-22-agenticjames-everything-you-need-to-know-about-context-engineering-in-1-minute]]
- [[2026-04-17-wiki-compiler-skills-subagents-hooks-mcp-pragmatisch]]
- [[2026-04-16-wiki-compiler-everything-claude-code-ecc]]
- [[2026-02-14-matt-pocock-skill-tdd-claude-code]]
- [[2026-02-09-tom-crawshaw-claude-code-insights-guide]]
