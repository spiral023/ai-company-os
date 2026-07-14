---
url: https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
autor: Anthropic (Repo anthropics/skills)
datum: 2026-07-01
erfasst: 2026-07-14
typ: repo
---

# Anthropic: offizieller `skill-creator`-Skill (SKILL.md, direkt gelesen)

## Inhalt

Direkte Lektüre der `SKILL.md` aus dem geklonten Repo (`external_repos/anthropics/skills/skills/skill-creator/SKILL.md`, Stand des letzten Commits auf die Datei: 2026-07-01). Damit ist die bisher nur über Sekundärsynthese ([[2026-04-16-wiki-compiler-skill-creator-skill]]) belegte Beschreibung nun am Original verifiziert.

Der Skill kann deutlich mehr als nur neue Skills erstellen. Fähigkeiten laut SKILL.md:

1. **Skills erstellen** — Intent klären (auch aus laufender Konversation extrahieren: „turn this into a skill"), Interview zu Edge Cases/Formaten, SKILL.md-Entwurf nach Anatomie-Vorgabe (`scripts/`, `references/`, `assets/`, Progressive Disclosure, <500 Zeilen Body).
2. **Bestehende Skills verbessern** — feedback-getriebene Iterationsschleife; Leitprinzipien: aus Feedback generalisieren statt overfitten, Prompt schlank halten, das „Warum" erklären statt ALL-CAPS-MUSTs, wiederholte Hilfslogik in Testläufen als Signal für Bundled Scripts erkennen.
3. **Evals fahren** — 2-3 realistische Testprompts in `evals/evals.json`; pro Testfall zwei parallele Subagent-Läufe: mit Skill UND Baseline (ohne Skill bzw. Snapshot der alten Version); Assertions werden während der Läufe entworfen; Grading über `agents/grader.md`.
4. **Benchmarking mit Varianzanalyse** — `scripts/aggregate_benchmark` erzeugt `benchmark.json`/`benchmark.md` mit Pass-Rate, Zeit, Tokens (Mittelwert ± Stddev, Delta zur Baseline); Analyst-Pass sucht Muster, die Aggregatwerte verstecken (nicht-diskriminierende Assertions, flaky Evals, Zeit/Token-Trade-offs); HTML-Viewer über `eval-viewer/generate_review.py` (Outputs-Tab mit Feedback-Textboxen, Benchmark-Tab; Feedback landet in `feedback.json`).
5. **Trigger-/Description-Optimierung** — die frontmatter-`description` ist der primäre Aktivierungsmechanismus; ~20 realistische Should-trigger-/Should-not-trigger-Queries (Negativfälle bewusst als Near-Misses, nicht offensichtlich irrelevant), User-Review über HTML-Template, dann automatische Optimierungsschleife `scripts/run_loop.py`: 60/40 Train/Test-Split, jede Query 3× ausgeführt, bis 5 Iterationen, Auswahl der `best_description` nach Test-Score gegen Overfitting.
6. **Blind-Vergleich zweier Skill-Versionen** — unabhängiger Agent bewertet zwei Outputs ohne zu wissen, welcher von welcher Version stammt (`agents/comparator.md`, `agents/analyzer.md`); optional, für „ist die neue Version wirklich besser?".
7. **Packaging** — `scripts/package_skill.py` erzeugt eine installierbare `.skill`-Datei.

Weitere Kernpunkte:

- **Triggering-Mechanik:** Claude konsultiert Skills nur bei Aufgaben, die es nicht trivial selbst kann — simple Ein-Schritt-Queries („read this PDF") triggern auch bei perfekter Description nicht. Eval-Queries müssen daher substanziell genug sein.
- **Undertriggering als Default-Problem:** Descriptions bewusst „pushy" formulieren (was der Skill tut + konkrete Auslöse-Kontexte, auch ohne explizite Nennung des Skill-Namens).
- **Plattform-Anpassungen:** Claude.ai (keine Subagents → Testfälle seriell selbst ausführen, kein Benchmarking, keine Description-Optimierung da `claude -p` fehlt), Cowork (Subagents ja, aber `--static`-HTML statt Server), Claude Code (voller Funktionsumfang).
- **Kommunikations-Hinweis:** Zielgruppe reicht bis zu Nicht-Programmierern; Jargon („JSON", „assertion") nur mit Kontext-Hinweisen verwenden.
- **„Principle of Lack of Surprise":** Skill-Inhalte dürfen den User bei Beschreibung nicht überraschen; keine irreführenden oder schädlichen Skills.

## Kernaussagen

- Der skill-creator deckt den vollen Lebenszyklus ab: Erstellen, Verbessern, Evals, Benchmarking mit Varianzanalyse, Trigger-Optimierung, Blind-Vergleich, Packaging → [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- Baseline-Vergleich (mit/ohne Skill bzw. alte Version) ist fest in den Eval-Ablauf eingebaut, inkl. Zeit- und Token-Messung → [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- Trigger-Optimierung ist ein eigener automatisierter Loop (Train/Test-Split, 3 Läufe pro Query, Auswahl nach Test-Score) statt Handarbeit → [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- Simple Ein-Schritt-Queries triggern Skills grundsätzlich nicht — relevant für die Gestaltung von Trigger-Evals → [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
