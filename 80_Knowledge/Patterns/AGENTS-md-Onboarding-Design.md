# AGENTS-md-Onboarding-Design

**Konfidenz:** mehrfach-belegt

## Zweck

Verhindert, dass die zentrale Agent-Onboarding-Datei (`AGENTS.md`/`CLAUDE.md`/`GEMINI.md`) mit der Zeit zu einer Sammelstelle für Spezialregeln wird und dadurch an Wirksamkeit verliert. Löst das Problem, dass LLMs zustandslos sind: Was ein Agent über eine Codebasis weiß, hängt vollständig vom Kontext ab, der ihm in der jeweiligen Session gegeben wird.

## Funktionsweise

Die Agent-Datei beantwortet auf hoher Ebene nur drei Fragen: **Was** (Stack, Struktur, Einstiegspunkte), **Warum** (Ziel und Zweck der zentralen Teile) und **Wie** (Arbeitsweise, Tools, Test-/Build-/Verifikationspfade). Sie enthält bevorzugt nur Instruktionen, die universell auf fast jede Aufgabe im Repository anwendbar sind. Für tieferen, aufgabenspezifischen Kontext wird Progressive Disclosure genutzt: Die Startdatei beschreibt nur die wichtigsten Grundlagen und verweist auf spezialisierte Zusatzdokumente (z.B. `agent_docs/building_the_project.md`, `agent_docs/service_architecture.md`), die der Agent nur bei Bedarf lädt. Verweise auf konkrete Dateien/Zeilen sind dabei robuster als kopierte Snippets. Stil- und Formatregeln gehören nicht in die Agent-Datei, sondern in deterministische Tools (Formatter, Linter, Typechecker, Tests) — ein LLM ist dafür langsamer, teurer und unzuverlässiger als ein Tool.

Empirisch bestätigt (ETH-Zürich-Studie, AGENTbench): LLM-generierte Context Files senken die Erfolgsquote gegenüber gar keinem Kontext und erhöhen die Kosten um über 20%, während menschlich geschriebene Dateien +4% Erfolgsquote bringen. Der entscheidende Unterschied ist Redundanz vs. Additivität — LLM-generierte Dateien wiederholen oft, was bereits in README/Doku steht, menschliche enthalten dagegen Informationen, die nirgendwo sonst stehen. Praxisregel daraus: „Schreibe für die Lücke, nicht für den Überblick.“ Technisch bestätigt: Claude Code injiziert einen expliziten System-Reminder, der das Modell anweist, Kontext zu ignorieren, wenn er nicht „hochgradig relevant“ wirkt — das erklärt, warum überladene Agent-Dateien nicht nur nutzlos, sondern aktiv kontraproduktiv werden. Konkrete Zahl: der Claude-Code-System-Prompt selbst verbraucht bereits ~50 der ~150-200 zuverlässig befolgbaren Instruktionen eines Frontier-Modells, bevor die Agent-Datei überhaupt geladen wird.

## Vorteile

- Kurze, fokussierte Agent-Dateien werden vom Modell zuverlässiger befolgt als lange Regelsammlungen (begrenztes Instruktionsbudget konkurriert sonst mit der eigentlichen Aufgabe).
- Progressive Disclosure hält den Startkontext klein, ohne dass Projektwissen verloren geht — es wird nur bei Bedarf nachgeladen.
- Klare Arbeitsteilung zwischen Agent-Kontext (Was/Warum/Wie) und deterministischen Tools (Stil/Format) reduziert unnötigen Modelleinsatz für mechanisch prüfbare Dinge.

## Nachteile & Grenzen

- Erfordert laufende Disziplin: Jede neue Zeile in der Hauptdatei muss bewusst gewählt werden, sonst wächst sie doch wieder zur Sammelstelle.
- Progressive-Disclosure-Struktur (mehrere Zusatzdokumente) erzeugt Navigationsaufwand, der sich für sehr kleine Projekte nicht lohnt.
- Automatisch generierte Agent-Dateien sind riskant, weil eine schlechte Zeile auf praktisch jede Arbeitsphase wirkt — Auto-Generierung ersetzt keine bewusste Kuratierung.

## Wann einsetzen, wann nicht

- Einsetzen: Projekte mit wiederkehrender Coding-Agent-Nutzung, insbesondere Monorepos oder Projekte mit wachsendem Spezialwissen.
- Nicht einsetzen: Einmal-Skripte oder sehr kleine Projekte ohne wiederkehrenden Bedarf an Onboarding-Kontext.

## Belege

- 2026-04-13 · [[2026-04-13-wiki-compiler-gute-agents-md-schreiben]] · meinung — Wiki-Artikel (Sekundärquelle, Ursprungsquelle laut dessen Frontmatter ein eingefügter Originalartikel) beschreibt Progressive Disclosure, das Was/Warum/Wie-Prinzip und die Trennung von Agent-Kontext und deterministischen Tools.
- 2026-02-01 · [[2026-02-01-humanlayer-writing-a-good-claude-md]] · meinung — Primärquelle (HumanLayer) bestätigt und konkretisiert dieselben Prinzipien: exaktes Instruction-Following-Budget (~150-200 Instruktionen, ~50 bereits vom System-Prompt verbraucht), Längenempfehlung (<300 Zeilen, HumanLayer selbst <60), wörtliches Zitat des Claude-Code-System-Reminders, explizite Warnung vor `/init`/Auto-Generierung.
- 2026-02-26 · [[2026-02-26-omarsar0-agents-md-evaluation]] · meinung — ETH-Zürich-Studie (AGENTbench, 138 Instanzen/12 Repos) liefert empirischen Beleg: LLM-generierte Context Files senken die Erfolgsquote und erhöhen Kosten um >20%, menschlich geschriebene bringen +4% — Redundanz vs. Additivität als Ursache.
- 2026-01-20 · [[2026-01-20-ben-tossell-agent-coding]] · meinung — Praxisbeispiel: eigene `agents.md` pro Projektordner mit explizitem Setup (Git-Workflow, Account-Wahl, E2E-Tests), aktiv von fremden `agents.md`-Dateien inspiriert.
- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/agents-md-official-spec.md (agents.md, Linux Foundation) · meinung — Offizielle Spezifikations-Website bestätigt die Design-Begründung auf Standard-Ebene: `AGENTS.md` als „README for agents", bewusst getrennt vom menschlichen README (Build-Steps, Tests, Konventionen, die ein README überladen würden); Verbreitung: über 60.000 Open-Source-Projekte auf GitHub nutzen das Format.

## Spannungen & offene Fragen

- Die ETH-Studie ist die bislang stärkste Einzelquelle (kontrollierter Benchmark statt Erfahrungsbericht), bleibt aber eine einzelne Studie mit einem spezifischen Benchmark-Design (AGENTbench, wenig populäre Python-Repos) — Übertragbarkeit auf andere Sprachen/Repo-Typen ungeprüft.
- Offene Frage: Ab welcher Projektgröße lohnt sich die zusätzliche Navigationsebene der Progressive-Disclosure-Struktur gegenüber einer einzigen, etwas längeren Datei? Aus den Quellen nicht abschließend beantwortbar.

## Verwandte Patterns

- [[CONTEXT-Glossar]]
- [[Erweiterungs-Ebenen-Zuordnung]]
