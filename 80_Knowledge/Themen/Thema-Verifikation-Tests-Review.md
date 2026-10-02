# Verifikation, Tests & Review

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-02. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Wie man prüft, ob der Agent liefert: TDD, Testharness, Mutation Testing, statische Analyse, Quality Gates, getrenntes Review, Review als Engpass.

## Suchbegriffe

- **Hauptkeyword:** AI Code Review
- **Long-Tail:** TDD mit Coding Agents; Testharness für Agents; Mutation Testing KI; Reward Hacking Tests; Adversarial Review Agent; Review als Engpass
- **Fragen:** Wie prüfe ich KI-generierten Code? / Warum schreibt der Agent Tests passend zum Bug?
- **Häufig in den Quellen:** test (4), testharness (4), verifier (3), /goal (3), auto mode (3), llm-as-judge (3), git worktrees (2), red green refactor (2), review (2), reviewer (2), qualität (2), verifikation (2), loop engineering (2), tests (2), ai slop (2), statische code-analyse (2), tdd (2), coding agents (2), mutation testing (2), hillclimbing (2)

## Verwandte Themen

- [[Thema-Spezifikation-Planung]] — Spezifikation & Planung
- [[Thema-Autonome-Läufe-Loops-CI]] — Autonome Läufe, Loops & CI
- [[Thema-Multi-Agent-Parallelisierung]] — Multi-Agent & Parallelisierung
- [[Thema-Skill-Design]] — Skill-Design

## Patterns (3)

- [[Hillclimbing-mit-Holdout-Split]] · meinung · 3 Belege
- [[TDD-als-Verifikationshebel]] · mehrfach-belegt · 11 Belege
- [[Testharness-als-staerkster-Hebel]] · meinung · 26 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Adversarialer-Pre-Launch-Check]], [[Anti-Rationalization-Tables]], [[Great-Decoupling-Rollenverstaendnis]], [[Plan-first-mit-getrenntem-Review]], [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]

## Quellen (17)

- [[2026-10-02-repo-thedaviddias-front-end-checklist]] — Im Klon von thedaviddias/Front-End-Checklist (Stand Commit `7bfd8680`) beschreibt `packages/cli/README.md` die CLI `@frontendchecklist/cli`; die Regeln liegen im Paket, sie läuft offline.
- [[2026-10-02-repo-garrytan-gstack]] — Laut `CHANGELOG.md` von garrytan/gstack (Repo-Stand Commit `7fca42ad`, Einträge um v1.91.9.0) wenden alle Workflows, die Tests vorschlagen, schreiben, prüfen oder ausliefern, eine gemeinsame „Test Val
- [[2026-09-28-claude-automating-eval-design-and-hillclimbing-with-cla]] — Anthropic beschreibt Prinzipien für Eval-Design und für das schrittweise Verbessern gegen ein Eval (Hillclimbing) und zeigt, wie die Befehle `/claude-api build-eval` und `/claude-api hillclimb` im `cl
- [[2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck]] — Mehr Agent-Output verschärft den Review-Flaschenhals: deterministische Checks, ein separater Review-Agent mit Commits und risikobasiertes Human Review bremsen ihn in drei Stufen.
- [[2026-08-25-vikingmute-2092059170812108811]] — Ein strenger Review-Skill sucht zuerst Vereinfachungen der Struktur statt Detailkritik, erzeugt aber bei Bestandscode schnell mehr Befunde, als sich abarbeiten lassen.
- [[2026-08-19-matt-pocock-live-uncle-bob-on-software-fundamentals-in-the-a]] — Statt langer Regeltexte gehören deterministische Tools wie Mutation Testing und Komplexitätsmetriken in eine Agent-Schleife, weil Modelle lange Regeldokumente nur als Richtlinie behandeln.
- [[2026-08-18-floknowsai-hoer-auf-den-code-deines-ki-agenten-zu-lesen]] — Autor und Prüfer müssen getrennt sein: Mutation Testing prüft die Tests selbst, ein zweiter Agent mit frischem Kontext bewertet Code und Testqualität.
- [[2026-08-14-floknowsai-ueber-achtzig-prozent-des-codes-von-claude-code-und-codex-sieht-kein]] — Ein Agent findet eigene Fehler seltener im selben Verlauf, weshalb eine frische Prüf-Session mit gleich starkem Modell und erzwungenen Status-Checks besser verifiziert.
- [[2026-08-05-creatoreconomy-use-my-human-review-skill-to-edit-html-and-markd]] — Feedback direkt an der Stelle in der Datei ist präziser als Chat-Anweisungen und verhindert, dass ungeprüfte Agent-Edits Slop ins Projekt tragen.
- [[2026-08-04-anthropic-docs-claude-code-best-practices]] — Anthropic empfiehlt Verifikation als vierstufige Eskalation vom Prompt über Goal-Evaluator und Stop-Hook bis zur zweiten Meinung durch ein frisches Modell, ergänzt um Plan-first und Session-Hygiene.
- [[2026-08-02-promptgefluester-wenn-ihr-versucht-euer-software-projekt-mit-fable-five-oder-o-plus-5]] — Vor einem KI-Refactoring deterministische statische Analyse laufen lassen, toten Code entfernen und Architekturregeln festlegen, statt das Modell Abhängigkeiten selbst abgleichen zu lassen.
- [[2026-07-26-promptgefluester-ich-hab-ne-unbequeme-wahrheit-und-zwar-ich-wurde-gefragt-wieso]] — Bei größeren Codebasen liefern dichte deterministische Prüfungen die Qualität, nicht das Modell allein, und kosten bewusst Zeit und Pflege.
- [[2026-07-16-amasad-2077802290304684404]] — Replit-CEO Amjad Masad beschreibt, wie Replit zwischen Januar und Juni 2026 interne Agents in Engineering, Data, Sales, Marketing und Support eingeführt hat.
- [[2026-07-01-0xcodila-2072329149520232639]] — Der X-Artikel erklärt Loops als Ziel, auf das ein Agent ohne Prompt pro Schritt hinarbeitet, und stützt sich auf Karpathys `autoresearch` und eine Bilevel-Arbeit.
- [[2026-02-14-matt-pocock-skill-tdd-claude-code]] — Ein Test, eine Implementierung, wiederholen: Vertikale Tracer-Bullet-Zyklen verhindern, dass das Modell Tests umschreibt oder nur Mocks verifiziert.
- [[2026-02-04-tweag-tdd-agentic-coding]] — Ein Test ist ein präziser Prompt: Der Agent baut Logik Test für Test, wobei die Testqualität beim Menschen liegt.
- [[2026-01-12-dhruv1103-lessons-learned-500k-lines-claude-code]] — Modulare Architektur, TDD gegen echte Container, Read-only-MCP-Diagnose und gründliches Review machen große KI-Codebasen beherrschbar.

## Quellen mit diesem Thema als Nebenthema

- [[2026-09-27-voxyz_ai-2104224555040452925]]
- [[2026-09-25-voxyz_ai-2103586663393853636]]
- [[2026-09-25-trq212-2103576349499855160]]
- [[2026-09-14-code-test-plugins-with-evals-claude-code-docs]]
- [[2026-08-30-alex-sprogis-loop-graph-engineering-das-letzte-video-was-du-s]]
- [[2026-08-05-floknowsai-dein-vibe-coding-projekt-bricht-nicht-am-coding-agent-zusammen-sondern]]
- [[2026-07-24-agenticjames-the-creator-of-claude-code-released-a-guide-to-the-4-levels-of-ai-coding]]
- [[2026-07-06-claudedevs-2074208949205881033]]
- [[2026-04-16-wiki-compiler-gstack]]
- [[2026-04-10-paulsolt-2042716870512353294]]
- [[2026-02-23-d4m1n-ralph-loop-setup-primaer]]
- [[2026-02-13-vincanger-claude-code-fullstack-essentials]]
- [[2026-02-05-carlini-anthropic-c-compiler]]
- [[2026-02-03-svpino-claude-code-md-tips]]
- [[2026-01-26-karpathy-coding-workflow-2026]]
- [[2026-01-20-mrexodia-vibe-engineering]]
