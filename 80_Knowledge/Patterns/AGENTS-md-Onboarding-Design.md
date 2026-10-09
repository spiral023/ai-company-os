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
- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/agents-md-official-spec.md (agents.md, Linux Foundation) · meinung — Offizielle Spezifikations-Website bestätigt die Design-Begründung auf Standard-Ebene: `AGENTS.md` als „README for agents“, bewusst getrennt vom menschlichen README (Build-Steps, Tests, Konventionen, die ein README überladen würden); Verbreitung: über 60.000 Open-Source-Projekte auf GitHub nutzen das Format.
- 2026-08-04 · [[2026-08-04-anthropic-docs-claude-code-best-practices]] · meinung — Offizielle Doku unterscheidet fünf Ablageorte mit unterschiedlicher Reichweite (Home/Projekt/`.local.md`/Parent/Child); Child-Dateien laden erst bei Bedarf nach — konkrete Lademechanik hinter dem hier bereits belegten Progressive-Disclosure-Prinzip.
- 2026-01-10 · [[2026-01-10-eyad-khrais-claude-code-tutorial]] · meinung — Erfahrungsbericht ergänzt die Begründungspflicht: eine Regel soll das „Warum“ mitliefern („Use TypeScript strict mode because …“), nicht nur die Anweisung, und wird per `#`-Shortcut laufend gepflegt, sobald eine Korrektur zweimal nötig war.
- 2026-02-01 · [[2026-02-01-anthropic-docs-claude-code-best-practices]] · meinung — Offizielle Doku bestätigt: nur was Claude nicht selbst aus dem Code ableiten kann, gehört in die Datei; bei Rauschen radikal kürzen (Pruning).
- 2026-02-14 · [[2026-02-14-minty-mastering-claude-code]] · meinung — Memory-System (schlanker `MEMORY.md`-Index mit Verweisen auf Detaildateien) ist eine unabhängige Bestätigung des Progressive-Disclosure-Prinzips außerhalb der Agent-Datei selbst.
- 2026-01-21 · [[2026-01-21-tempoimmaterial-agent-skills-vs-rules-vs-commands]] · meinung — Empfiehlt, Rules als Routing-Logik zu formulieren, die auf passende Skills verweist („Wenn du UI-Komponenten änderst, lade den `ui-change`-Skill“), statt die volle Logik direkt in der Agent-Datei zu halten — hält den permanent geladenen Prompt klein und den Agenten trotzdem anpassungsfähig.
- 2026-02-07 · [[2026-02-07-daniel-san-agent-teams-praxismuster]] · meinung — Konkreter Multi-Agent-Kostenfaktor für vage `CLAUDE.md`-Inhalte: Jeder Teammate in einem Agent-Team lädt die Datei unabhängig; bleibt sie vage, exploriert jeder Teammate die Codebase eigenständig, wodurch N Teammates den N-fachen Tokenverbrauch für dieselbe Kontext-Erschließung erzeugen.
- 2026-01-12 · [[2026-01-12-dhruv1103-lessons-learned-500k-lines-claude-code]] · meinung — `CLAUDE.md` instruiert Claude, an den Anfang jeder neuen Datei einen kurzen Zweck-Kommentar zu setzen, damit sich frische Sitzungen in der Codebase schneller zurechtfinden — konkrete Umsetzung der Navigations-Unterstützung durch die Agent-Datei.
- 2026-01-14 · [[2026-01-14-ashpreetbedi-claude-code-spec-first]] · meinung — Unabhängige Drittautor-Bestätigung der Parent/Child-Lademechanik: zwei `CLAUDE.md`-Ebenen (Repo-Ebene stabil und navigierend, Feature-Ebene entwickelt sich mit der Arbeit) werden beim Öffnen eines Feature-Ordners gemeinsam geladen — deckt sich mit der bereits über die offizielle Anthropic-Doku belegten Mehr-Orte-Lademechanik.
- 2026-01-22 · [[2026-01-22-hooeem-claude-code-7-schritte-plan]] · meinung — Sekundärquelle beschreibt ein vereinfachtes Drei-Schichten-Gedächtnis (Project/Local/Machine), das den bereits per offizieller Doku belegten fünf Ablageorten entspricht; ergänzt den Escape+`#`-Kombigriff als benannten Kurzbefehl für die bereits belegte Praxis, eine Regel erst nach zweimal nötiger Korrektur in die Datei aufzunehmen.
- 2026-01-31 · [[2026-01-31-bcherny-claude-code-team-tips]] · meinung — Boris Chernys Team hängt an Korrektur-Prompts routinemäßig „Aktualisiere Deine CLAUDE.md, damit Du diesen Fehler nicht noch einmal machst“ an und wiederholt das, bis die Fehlerrate messbar sinkt — konkrete Team-Praxis der bereits belegten Selbstkorrektur-Schleife.
- 2026-02-01 · [[2026-02-01-aiedge-claude-code-starter-pack]] · meinung — Boris Chernys Team pflegt eine einzige, ins Repo eingecheckte CLAUDE.md, an der mehrere Personen wöchentlich mitschreiben („add incorrect actions so Claude can learn“) — konkretes Beispiel für kontinuierliche statt einmaliger Pflege der Agent-Datei.
- 2026-07-30 · [[2026-07-30-floknowsai-ki-gibt-dir-das-gefuehl-dass-du-so-schnell-wie-noch-nie-arbeitest]] · meinung — Zitiert (nur aus der Caption) eine Studie, nach der richtiger Kontext die Erfolgsrate von 26 auf 34 Prozent hebt, falscher sie auf 22 Prozent senkt, also unter den Wert ohne Kontext. Stützt „schlank und korrekt statt viel“; Studie nicht geprüft, Bezugsgröße unbekannt.
- 2026-09-04 · [[2026-09-04-pvncher-2095991462416490862]] · meinung — Pflichtlektüre von Doc-Stapeln vor jeder Änderung ersetzen durch kontextuelle Verweise mit Anlass; Test-Aufforderungen und harte Verbote bei stärkerem Modell neu prüfen. Modellspezifisch (GPT-6 Astra), nicht gemessen.
- 2026-09-07 · [[2026-09-07-sairahul1-2096902575035683147]] · meinung — Empfiehlt nach dem Wechsel auf GPT-6 Astra ein Audit aller Instruktionsdateien und eine deklarierte Prioritätsreihenfolge, weil überholte oder widersprüchliche Regeln in AGENTS.md das Modell verschlechtern könnten. Selbstberichtet, ohne Messung, modellspezifisch.
- 2026-07-12 · [[2026-07-12-agenticjames-claude-codes-new-feature-checkup-makes-claude-more-token-efficient-and]] · meinung — `/checkup` dedupliziert `CLAUDE.md` über User-, Projekt- und lokale Ebene und splittet lange Dateien in verschachtelte, spezifische Dateien (Progressive Disclosure). Einschränkung: Qualität des automatischen Splits ist nicht belegt.
- 2026-09-24 · [[2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck]] · meinung — Coding Standards gehören nicht in AGENTS.md, sondern in eine Datei, die nur der Review-Agent liest. Nuanciert den Bestand; nur Praxisbericht.
- 2026-09-14 · [[2026-09-14-developers-rethinking-skills-and-prompts-for-gpt-6-astra-op]] · meinung — Pflichtlektüre vor jedem Edit ersetzen durch kontextuelle Verweise, veraltete Anweisungen (Tests, Verbote) regelmäßig streichen; selbstberichtet für GPT-6 Astra, nicht gemessen.
- 2026-02-01 · [[2026-02-01-anthropic-docs-extend-claude-code]] · meinung — Richtwert CLAUDE.md unter ca. 500 Zeilen, Rest in Skills auslagern; weicht vom HumanLayer-Richtwert unter 300 Zeilen ab.
- 2026-04-22 · [[2026-04-22-agenticjames-everything-you-need-to-know-about-context-engineering-in-1-minute]] · meinung — AGENTS.md/CLAUDE.md als immer geladener Stamm mit Verweisen auf Skills, Dokumente, MCP; Metapher ohne Messung.
- 2026-07-25 · [[2026-07-25-agenticjames-they-cut-claude-code-system-prompt-by-80-and-you-should-be-doing-the]] · meinung — Fordert, CLAUDE.md-Dateien für neuere Modelle zu kürzen und präskriptive Regeln zu vermeiden. Keine eigene Messung, Papers und Benchmarks nicht benannt.
- 2026-03-21 · [[2026-03-21-sourfraser-claude-obsidian-ai-employee]] · meinung — Memory-Datei als Onboarding-Dokument mit Routing-Regeln, zu Sessionbeginn per Custom Instruction geladen; selbstberichtet, Sekundärquelle.
- 2026-02-09 · [[2026-02-09-tom-crawshaw-claude-code-insights-guide]] · meinung — Sekundärquelle: `/insights` führt hohen Exploration-Overhead (Bash 4x Dateiedits) auf fehlenden Startkontext zurück und empfiehlt wenige Zeilen in `CLAUDE.md`. Selbstberichtete Einzelzahlen.
- 2026-02-25 · [[2026-02-25-heynavtoor-claude-cowork-setup-guide]] · meinung — Ordner `Claude Context` mit drei Kontextdateien (about-me, brand-voice, working-style) als dauerhafter Hintergrund; Sekundärquelle.
- 2026-08-22 · [[2026-08-22-promptgefluester-wenn-euch-jemand-verspricht-token-zu-sparen-bei-cloud-code-dann-vorsicht]] · meinung — Quellcode als einzige Quelle der Wahrheit halten; ausgelagerte Notizen, Logs und Kommentare am Session-Ende auf Aktualität prüfen, weil der Agent sie später wieder als wahr einliest.
- 2026-07-06 · [[2026-07-06-mattpocockuk-2074060484047712521]] · meinung — Dev-Server per `tee` in Logdatei, Zeiger in `AGENTS.md`: Agent sieht Laufzeitausgabe ohne Prozessbesitz; ungemessener Praxistipp, Logwachstum nicht adressiert.
- 2026-07-15 · [[2026-07-15-xudong07452910-2077246527756775933]] · meinung — Empfiehlt, in `AGENTS.md` Akzeptanzkriterien, Berechtigungsgrenzen und Verifikationsablauf zu betonen statt enger Prozesssteuerung. Reine Autorenmeinung zu einem Herstellerdokument, ohne Beispiel.
- 2026-09-18 · [[2026-09-18-repo-anthropics-claude-code-agents-md-support]] · verifiziert — Claude Code liest seit 2.1.277 `AGENTS.md`, wenn keine `CLAUDE.md` existiert (umstellbar in `/config` unter „Project instructions“), seit 2.1.281 auch über Bedrock, Vertex, Foundry und Gateways. Eine Datei kann damit Claude Code und andere Agents bedienen; eine zusätzliche `CLAUDE.md` hat Vorrang.
- 2026-10-07 · [[2026-10-07-voxyz_ai-2107939019091005836]] · meinung — Vox empfiehlt dauerhaft nur universelle Regeln und konkrete Leseanlässe für Deployment-, Schema- und Ordnerwissen; sein Diagramm verallgemeinert bedarfsabhängiges Laden, während der Post Codex-Sessionstart und Claude-Dateizugriff unterscheidet, deren Produktdetails hier unverifiziert bleiben.
- 2026-10-05 · [[2026-10-05-voxyz_ai-2107123654219743712]] · meinung — Vox formuliert für lange Abschlüsse oder Blockaden eine konkrete Berichtsregel mit nummeriertem Handlungsbedarf, Ort und erwarteter Rückgabe am Anfang; der Nutzen liegt in der Output-Gestaltung, nicht in zusätzlichen Root-Regeln als Selbstzweck, und die bessere Lesbarkeit bleibt persönliche Erfahrung.
- 2026-10-04 · [[2026-10-04-voxyz_ai-2106783910055006342]] · meinung — Vox grenzt eine kompakte Regeldatei auf Projekte ohne reale Nutzer ein, koppelt minimale Lösungen an gemeinsame Aufruferänderungen und Lessons-Pflege; dieser Status allein belegt nicht, dass Migrationen oder bestehende Daten entbehrlich sind.
- 2026-10-02 · [[2026-10-02-voxyz_ai-2106006290954592332]] · meinung — Die Wartung trennt Quellcode, Konfiguration und sitzungsbezogene Lernsignale; der zentral geprüfte Retro-Skill bevorzugt deterministische Checks für mechanische Fehler, während die beschriebenen Doctor-Freigabegrenzen nicht getestet wurden.
- 2026-10-09 · external_repos/mattpocock/skills/skills/engineering/retro/SKILL.md · verifiziert — Checkout 4588b32 ordnet mechanische Verstöße deterministischen Linter-, Hook- oder CI-Checks zu und reserviert Coding-Standards-Prosa für Ermessensfragen; bestätigt die dokumentierte Empfehlung, keine Fehlerreduktion.

## Spannungen & offene Fragen

- 2026-10-09 · [[2026-10-04-voxyz_ai-2106783910055006342]] begrenzt seine Vorlage auf Projekte ohne reale Nutzer und empfiehlt dort Verzicht auf Kompatibilität und Migrationen. Gespeicherte Zustände und externe Aufrufer können trotzdem bestehen; der Projektstatus allein rechtfertigt keine Datenlöschung. Die dortige Lessons-Bereinigung gilt nicht für unsere append-only Patterns.

- 2026-10-09 · [[2026-10-07-voxyz_ai-2107939019091005836]]: Die Strukturidee bedarfsabhängiger Regeln ist vom Ladeverhalten des Werkzeugs abhängig; der Post unterscheidet Codex-Sessionstart und Claude-Dateizugriff, während das Diagramm Ordnerladen verallgemeinert. Der lokale Codex-Repo-Check bestätigt nur das gemeinsame 32-KiB-Standardbudget, keinen Kontextgewinn der vorgeschlagenen Umstrukturierung.

- Die ETH-Studie ist die bislang stärkste Einzelquelle (kontrollierter Benchmark statt Erfahrungsbericht), bleibt aber eine einzelne Studie mit einem spezifischen Benchmark-Design (AGENTbench, wenig populäre Python-Repos) — Übertragbarkeit auf andere Sprachen/Repo-Typen ungeprüft.
- Offene Frage: Ab welcher Projektgröße lohnt sich die zusätzliche Navigationsebene der Progressive-Disclosure-Struktur gegenüber einer einzigen, etwas längeren Datei? Aus den Quellen nicht abschließend beantwortbar.

## Verwandte Patterns

- [[CONTEXT-Glossar]]
- [[Erweiterungs-Ebenen-Zuordnung]]
