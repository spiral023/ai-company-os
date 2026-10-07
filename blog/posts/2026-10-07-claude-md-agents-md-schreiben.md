---
titel: "CLAUDE.md oder AGENTS.md schreiben: kurz, von Hand und nur für die Lücke"
datum: 2026-10-07
kategorie: arbeitsweisen
zusammenfassung: "So schreibst du eine CLAUDE.md oder AGENTS.md, die der Agent befolgt: was hineingehört, wie lang sie sein darf und warum eine generierte Datei schadet. Claude Code liest seit September auch AGENTS.md."
status: freigegeben
geprueft_am: 2026-10-07
freigabe: automatisch
quellen:
  - 2026-09-18-repo-anthropics-claude-code-agents-md-support
  - 2026-02-26-omarsar0-agents-md-evaluation
  - 2026-02-01-humanlayer-writing-a-good-claude-md
  - 2026-02-01-anthropic-docs-claude-code-best-practices
  - 2026-08-04-anthropic-docs-claude-code-best-practices
  - 2026-02-01-anthropic-docs-extend-claude-code
  - 2026-07-06-mattpocockuk-2074060484047712521
  - 2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck
  - 2026-01-31-bcherny-claude-code-team-tips
  - 2026-09-14-developers-rethinking-skills-and-prompts-for-gpt-6-astra-op
---

## Kurz gesagt

- Claude Code liest seit Version 2.1.277 auch AGENTS.md, solange das Projekt keine CLAUDE.md hat. Eine Datei reicht dann für Claude Code und Codex.
- Schreib nur hinein, was der Agent nicht selbst aus Code und README ablesen kann. Eine generierte Datei kostet mehr und hilft weniger als gar keine.
- Halte die Datei kurz und verweise für Details auf eigene Dokumente, die der Agent bei Bedarf liest.
- Stilregeln und Verbote gehören in Linter, Hooks und Berechtigungen, nicht in Prosa.

## CLAUDE.md oder AGENTS.md: welcher Dateiname?

Seit Version 2.1.277 vom 18.09.2026 liest Claude Code die Datei AGENTS.md, wenn ein Projekt keine CLAUDE.md hat. Seit 2.1.281 klappt das auch über Bedrock, Vertex AI, Foundry und LLM-Gateways.{q:1} Codex arbeitet ohnehin mit AGENTS.md.{q:10} Ein Repository kann damit eine einzige Datei für beide Agents führen.

Liegt zusätzlich eine CLAUDE.md im Projekt, liest Claude Code diese und lässt die AGENTS.md liegen. Ändern lässt sich das in `/config` unter „Project instructions“.{q:1} Pflege deshalb nicht beide Dateien nebeneinander, sonst arbeiten Claude Code und Codex nach unterschiedlichen Regeln. Für neue Projekte nimm gleich AGENTS.md. Bei einem bestehenden Projekt verschiebst du den Inhalt der CLAUDE.md in die AGENTS.md und löschst die alte Datei.

Persönliche Regeln bleiben, wo sie sind. Die globale Datei `~/.claude/CLAUDE.md` gilt für alle deine Sessions, `CLAUDE.local.md` für persönliche Regeln im Projekt, die nicht ins Git gehören.{q:5}

Im Rest des Beitrags steht „die Datei“ für beide Namen.

## Was hineingehört: nur die Lücke

Eine Studie der ETH Zürich hat 138 Aufgaben aus 12 Python-Repositories mit Claude Code, Codex und Qwen Code getestet, jeweils ohne Datei, mit generierter und mit von Menschen geschriebener Datei. Generierte Dateien senkten die Erfolgsquote im eigenen Benchmark um 2 Prozent gegenüber gar keiner Datei und erhöhten die Kosten um über 20 Prozent. Von Menschen geschriebene Dateien brachten 4 Prozent mehr Erfolg.{q:2}

Den Unterschied erklären die Autoren mit Wiederholung. Generierte Dateien wiederholen, was ohnehin im README und in der Doku steht. Von Menschen geschriebene enthalten, was nirgends sonst steht: Entscheidungen zum Tooling, Eigenheiten der CI, Konventionen abseits des Standards. Wurde die Doku vorher entfernt, schnitten auch die generierten Dateien besser ab.{q:2} Die Studie nutzt wenig bekannte Python-Projekte, bei anderen Sprachen kann das Ergebnis anders ausfallen.

Anthropic zieht in den Best Practices dieselbe Grenze. In die Datei gehören spezielle Shell-Befehle, abweichende Code-Styles und das Test-Setup. Was Claude im Code lesen kann, Standard-Konventionen der Sprache und lange Anleitungen bleiben draußen.{q:4} HumanLayer rät deshalb von `/init` und anderen automatisch erzeugten Dateien ab: Keine Datei wirkt auf so viele Aufgaben, also sollte jede Zeile bewusst von Hand geschrieben sein.{q:3}

| Gehört hinein | Gehört woanders hin |
|---|---|
| Build-, Test- und Prüfbefehle, die vom Standard abweichen | Was README oder Code schon zeigen: weglassen |
| Eigenheiten von CI, Tooling und Deployment | Stil- und Formatregeln: Formatter und Linter |
| Wo was liegt, mit Verweis auf Detaildokumente | Lange Anleitungen: eigene Dokumente oder Skills |
| Zeiger auf Laufzeit-Informationen wie Logdateien | Coding Standards: eigene Datei für das Review |

Ein Beispiel für die letzte Zeile links stammt von Matt Pocock. Er lässt den Dev-Server per `tee` zusätzlich in eine Logdatei schreiben und vermerkt in der AGENTS.md, wo sie liegt. Der Agent liest so die Laufzeitausgabe, ohne den Server-Prozess selbst zu steuern.{q:7} Diese Information findet der Agent nirgends sonst, genau dafür ist die Datei da.

## Wie lang: kurz genug, dass jede Zeile zählt

Laut HumanLayer befolgen aktuelle Modelle mit Reasoning etwa 150 bis 200 Anweisungen einigermaßen zuverlässig. Rund 50 davon verbraucht schon der System-Prompt von Claude Code. Mit jeder weiteren Anweisung sinkt die Befolgung, und zwar für alle Anweisungen gleichmäßig, nicht nur für die neuen.{q:3} Claude Code schickt die Datei außerdem mit dem Hinweis an das Modell, den Inhalt nur zu beachten, wenn er für die Aufgabe hochrelevant ist.{q:3} Füllstoff verwässert also auch die wichtigen Zeilen.

Bei der Länge gehen die Richtwerte auseinander. HumanLayer nennt unter 300 Zeilen als verbreiteten Konsens und kommt selbst mit unter 60 aus.{q:3} Die Übersicht von Anthropic setzt die Grenze bei etwa 500 Zeilen und rät, den Rest in Skills auszulagern.{q:6} Claude Code warnt selbst, wenn die Datei zu lang wird, und seit Version 2.1.206 schlägt `/doctor` vor, Inhalte zu streichen, die Claude aus dem Code ableiten kann.{q:1} Peile eher die 60 als die 500 an.

## Grundlagen in die Datei, Details dahinter

Was nicht in jede Aufgabe gehört, lagerst du aus. HumanLayer legt dafür einen Ordner `agent_docs/` an, etwa mit `building_the_project.md`, `running_tests.md` und `database_schema.md`. In der Hauptdatei steht nur eine Zeile pro Dokument, was darin steht, und Claude entscheidet selbst, was es liest. Verweise auf Datei und Zeile sind dabei besser als kopierte Code-Ausschnitte, weil Kopien veralten.{q:3}

Claude Code unterstützt das mit seinem Lademechanismus. Dateien in übergeordneten Ordnern lädt es beim Start mit, eine CLAUDE.md in einem Unterordner erst, wenn Claude dort eine Datei liest.{q:5} In einem Monorepo kann jedes Paket so seine eigenen Regeln mitbringen, ohne den Start zu belasten. Ob Claude Code verschachtelte AGENTS.md-Dateien genauso nachlädt, sagt der Changelog nicht.{q:1}

## Pflichtregeln gehören nicht in Prosa

Eine Zeile in der Datei ist eine Bitte, die das Modell gegen alles andere im Kontext abwägt. Was immer gelten muss, braucht ein Werkzeug, das es erzwingt: Formatter und Linter für Stil, Hooks für feste Abläufe, Deny-Regeln für Verbote. Warum eine Zeile in der Agent-Datei keine geheimen Dateien schützt, steht im Beitrag zu [Deny-Rules statt Bitte](post:deny-rules-statt-bitte), die Zuordnung zu Skill, Hook oder MCP im Beitrag zu den [Erweiterungs-Ebenen](post:welche-ebene-claude-md-skill-hook-mcp).

Matt Pocock nimmt auch die Coding Standards heraus. Sie landen in einer eigenen Datei, die nur ein Review-Agent liest. Der Agent, der umsetzt, steht ohnehin unter dem größten Kontextdruck und soll sie nicht bei jedem Start mitschleppen.{q:8}

## Pflegen: korrigieren ja, sammeln nein

Das Team von Boris Cherny, der Claude Code entwickelt hat, hängt an Korrekturen oft den Satz an, Claude solle seine CLAUDE.md so anpassen, dass der Fehler nicht wieder passiert. Laut Cherny formuliert Claude solche Regeln überraschend gut, und das Team wiederholt das, bis die Fehlerrate sinkt.{q:9} Das widerspricht dem Gebot der Kürze nur scheinbar. Eine Regel, die einen wiederkehrenden Fehler verhindert, füllt eine echte Lücke. Gefährlich wird die Gewohnheit, jede einmalige Korrektur festzuhalten.

Prüf die Datei außerdem bei jedem Modellwechsel. OpenAI rät, Anweisungen für ein stärkeres Modell auszudünnen, weil überholte Regeln aktiv schaden können.{q:10} Claude Code bringt dafür seit Version 2.1.283 `/doctor prompt-audit` mit, der Instruktionsdateien und Skills auf Muster für ältere Modelle prüft.{q:1} Welche Regeln du nach einem Wechsel streichen kannst, steht im Beitrag zu [alten Prompts und neuen Modellen](post:alte-prompts-neue-modelle).

## Empfehlung

Öffne heute deine CLAUDE.md oder AGENTS.md und streich jede Zeile, die der Agent aus Code oder README selbst ablesen kann. Was übrig bleibt, verschiebst du in eine AGENTS.md ohne parallele CLAUDE.md, damit Claude Code und Codex dieselben Regeln lesen. Detailwissen kommt in eigene Dokumente mit einer Zeile Verweis, Pflichtregeln in Linter, Hooks und Deny-Regeln.
