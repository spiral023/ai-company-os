---
titel: "Claude Code Skills, die zuverlässig auslösen: vorführen, Trigger testen, flach halten"
datum: 2026-10-02
kategorie: arbeitsweisen
zusammenfassung: "Wann sich ein eigener Skill lohnt, warum du ihn aus einer Vorführung statt aus einer Beschreibung baust, wie eine Trigger-Testliste mit Baseline aussieht und welche Aufrufregeln eine Skill-Sammlung beherrschbar halten."
status: freigegeben
geprueft_am: 2026-10-02
quellen:
  - 2026-01-31-bcherny-claude-code-team-tips
  - 2026-09-27-anthropic-academy-sdlc-playbook
  - 2026-07-01-anthropic-skill-creator-skill-md
  - 2026-01-21-aiedge-claude-50-pro-tips
  - 2025-10-31-agenticjames-best-claude-skills-for-agentic-coding
  - 2026-06-04-agenticjames-most-people-have-not-touched-the-best-parts-of-claude-code-skills-forked
  - 2026-07-10-voxyz-mattpocock-skills
  - 2026-02-01-anthropic-docs-extend-claude-with-skills
  - 2026-02-27-thariq-lessons-building-claude-code
---

## Kurz gesagt

- Bau einen Skill erst, wenn du dieselbe Arbeit regelmäßig erklärst und das Wissen über eine Sitzung hinaus gelten soll. Pflichtregeln gehören zusätzlich in einen Hook.
- Spiel die Aufgabe einmal mit dem Agent durch und lass ihn den Skill aus diesem Verlauf schreiben, statt ihn vorher in Prosa zu beschreiben.
- Teste die Beschreibung mit Prompts, die auslösen sollen, und knappen Fehlgriffen, die es nicht sollen. Lass dieselben Aufgaben einmal ohne Skill laufen.
- Halte die Aufrufkette flach. Orchestrator-Skills startest nur du, und sie rufen nie einen anderen Orchestrator auf.

## Wann sich ein Skill lohnt

Das Claude-Code-Team bei Anthropic macht alles, was es mehr als einmal am Tag tut, zu einem Skill.{q:1} Boris Cherny nennt als Beispiel einen eingecheckten BigQuery-Skill, mit dem er seit über sechs Monaten kein SQL mehr selbst geschrieben hat. Weil der Skill im Git-Repo liegt, nutzt ihn das ganze Team, nicht nur sein Autor.{q:1}

Anthropics SDLC-Playbook zieht die Grenze von der anderen Seite. Skills sind für institutionelles Wissen gedacht, das konsistent angewendet werden soll, und sie bleiben beratend.{q:2} Was immer gelten muss, braucht zusätzlich einen Hook oder einen Review-Schritt. Eine Korrektur, die du zweimal geben musstest, landet laut Playbook zuerst in der CLAUDE.md.{q:2}

Einmalige Aufgaben erledigst du also im Chat, eine wiederholte Korrektur wandert in die CLAUDE.md. Ein Skill wird erst der Ablauf mit mehreren Schritten, eigenem Material oder Skripten, den du regelmäßig brauchst. Zu früh gebaute Skills belegen mit ihrer Beschreibung dauerhaft Kontext und überlappen mit Nachbarn.

## Erst vorführen, dann aufschreiben lassen

Wer mit einer leeren SKILL.md startet, schreibt auf, wie die Arbeit gehen sollte, und vergisst die Schritte, die er aus Gewohnheit macht. Erledige die Aufgabe einmal vollständig mit dem Agent, korrigiere ihn unterwegs und sag am Ende „mach daraus einen Skill“. Anthropics offizieller `skill-creator` unterstützt diesen Weg, er liest die Absicht aus dem laufenden Gespräch und fragt danach Randfälle und Formate ab.{q:3} Deine Korrekturen aus der Vorführung zeigen, wo das Modell ohne Anleitung danebenliegt, und gehören deshalb in den Skill.

Für Visuelles geht das auch ohne Gespräch. Laut einer Tippsammlung von AI Edge lässt sich aus einem Screenshot eines gelungenen Designs ein Skill ableiten, der das Schema wiederholt, und Cowork lernt einen Ablauf aus einer aufgezeichneten Browser-Sitzung.{q:4} Erfolgszahlen nennt die Sammlung nicht. Wie ein solcher Design-Skill im Alltag aussieht, zeigt der Beitrag zu [UI mit Agenten und Referenzbild](post:ui-mit-agenten-referenzbild-audit).

Aus einer einzigen Vorführung übernimmt der Agent auch Zufälle dieses einen Falls. Streich beim Lesen des Entwurfs, was nur dort galt. Einen Skill-Generator, der wiederkehrende Muster selbstständig zu Skills macht, empfiehlt @agentic.james.{q:5} Ohne Review entstehen so viele kleine Skills mit überlappenden Beschreibungen.

## Trigger testen, bevor du dem Skill traust

Ob ein Skill lädt, entscheidet seine `description`. Warum sie nur den Auslöser nennen soll, steht in [Alte Prompts, neue Modelle](post:alte-prompts-neue-modelle). Ob deine Formulierung trifft, zeigt erst ein Test.

Der `skill-creator` arbeitet dafür mit etwa 20 realistischen Anfragen, gemischt aus solchen, die auslösen sollen, und solchen, die es nicht sollen.{q:3} Die Negativfälle sind bewusst knappe Fehlgriffe, keine offensichtlich fremden Themen. Einfache Ein-Schritt-Anfragen gehören nicht hinein, denn Claude greift bei Aufgaben, die es trivial selbst löst, auch mit perfekter Beschreibung nicht zum Skill.{q:3}

Eine Testliste für einen Release-Notes-Skill könnte so aussehen (eigenes Beispiel):

```text
Soll auslösen:
  „Schreib die Release Notes für v2.4 aus allen PRs seit dem letzten Tag.“
  „Was haben wir seit Montag ausgeliefert? Fass es für den Kunden-Newsletter zusammen.“
  „Mach aus diesen fünf PR-Titeln einen Changelog-Abschnitt für Endnutzer.“

Soll nicht auslösen:
  „Schreib die Beschreibung für diesen Pull Request.“
  „Welche API-Endpunkte haben sich zwischen v2.3 und v2.4 geändert? Ich suche einen Bug.“
  „Erklär mir, wie unser Release-Prozess in der CI funktioniert.“
```

Der zweite Test ist der Baseline-Vergleich. Der `skill-creator` lässt zwei bis drei echte Aufgaben je einmal mit Skill und ohne ihn laufen, bei einer Überarbeitung gegen die alte Version, und misst Erfolgsquote, Zeit und Tokens.{q:3} Liefert der Skill kein besseres Ergebnis, kostet er nur Kontext. Die Beschreibung optimiert der `skill-creator` in einer Schleife mit einem Split von 60 zu 40 zwischen Trainings- und Testfragen, drei Läufen pro Frage und bis zu fünf Durchgängen.{q:3} Warum der Split nötig ist, steht im Beitrag zu [Hillclimbing mit Holdout](post:hillclimbing-mit-holdout).

Der `skill-creator` hält zu seltenes Auslösen für den Normalfall und rät zu einer drängenden Beschreibung.{q:3} @agentic.james empfiehlt sogar die Befehlsform „You must use this skill when …“, ohne Trigger-Rate zu messen.{q:6} Je drängender die Beschreibung, desto eher löst sie auch bei den Fehlgriffen aus. Welche Fassung gewinnt, entscheidet die Testliste.

Im Ordner sieht das so aus:

```text
.claude/skills/release-notes/
├── SKILL.md            # Frontmatter mit description, kurzer Ablauf
├── references/stil.md  # Tonalität und zwei gute Beispiele
├── scripts/prs.sh      # sammelt gemergte PRs, immer gleich
└── evals/
    ├── evals.json      # zwei bis drei Aufgaben mit Prüfkriterien
    └── trigger.txt     # die Testliste von oben
```

Schreibt der Agent in mehreren Testläufen dieselbe Hilfslogik neu, gehört sie als Skript in `scripts/`.{q:3}

## Wer wen aufrufen darf

Rufen sich Skills gegenseitig auf, wird das Verhalten schnell unvorhersagbar. Matt Pocock trennt in seiner Sammlung deshalb zwei Arten. Skills, die nur du startest, orchestrieren den Ablauf. Skills, die auch das Modell von selbst laden darf, tragen die Disziplin, etwa TDD oder Code Review. Ein Orchestrator darf Disziplin-Skills aufrufen, nie einen anderen Orchestrator.{q:7}

In Claude Code setzt du das mit `disable-model-invocation: true` im Frontmatter um.{q:8} Ein so markierter Skill ist für das Modell nicht auffindbar und kann deshalb von keinem anderen Skill aufgerufen werden. Damit hat die Kette höchstens zwei Ebenen, und Zyklen zwischen Orchestratoren sind ausgeschlossen. Noch flacher wird die Kette, wenn Disziplin-Skills selbst keine Skills aufrufen (eigene Ergänzung). Was zwei davon brauchen, legst du in ein gemeinsames Referenzdokument.

Braucht ein Disziplin-Skill viel Lesestoff, etwa für ein Architektur-Review, kann `context: fork` ihn als Subagent in einem eigenen Kontext laufen lassen.{q:8} Der Fork sieht den Gesprächsverlauf nicht, alles Nötige muss also im Skill oder in den Argumenten stehen.{q:6}

## Pflege nach dem Modellwechsel

Thariq vom Claude-Code-Team beschreibt, wie Hilfskonstrukte, die ein älteres Modell brauchte, bei einem stärkeren zum Engpass werden, und rät zu einer Überprüfung bei jedem Modell-Upgrade.{q:9} Für Skills heißt das, dass Trigger-Testliste und Baseline-Vergleich nach jedem Wechsel erneut laufen. Ein Skill, der mit dem neuen Modell keinen Vorsprung mehr gegenüber der Baseline hat, fliegt raus. Welche Anweisungen du dabei typischerweise streichst, steht in [Alte Prompts, neue Modelle](post:alte-prompts-neue-modelle).

Anthropic schlägt im Playbook 20 bis 50 echte Aufgaben als Eval vor, die in der CI laufen, sobald sich CLAUDE.md, Skills oder Hooks ändern, und zusätzlich nach Zeitplan.{q:2} Jeder Fehler im Betrieb wird ein neuer Testfall.

## Kosten und Grenzen

- Testliste, Baseline und Beschreibungs-Schleife kosten Läufe und Tokens. Für einen kleinen Skill, den nur du nutzt, reichen Vorführung und eine Handvoll Prüfprompts.
- Die Tagesschwelle des Claude-Code-Teams ist eine Erfahrungsregel ohne Vorher-nachher-Vergleich.{q:1} Prüfe sie an deinem eigenen Wiederholungsmuster.
- Schlecht gewählte Testfälle täuschen Sicherheit vor. Fehlen die knappen Fehlgriffe, misst du nur, ob der Skill bei Offensichtlichem lädt.
- Ein veralteter, eingecheckter Skill verteilt falsches Wissen im ganzen Team. Er braucht eine zuständige Person.
- Skills sind beratend.{q:2} Was nie passieren darf, sicherst du mit einem Hook ab.

## Was du jetzt tust

Nimm die Aufgabe, die du diese Woche am häufigsten erklärt hast. Spiel sie einmal mit dem Agent durch und lass ihn daraus den Skill schreiben. Schreib sechs Prompts auf, drei sollen auslösen, drei knapp danebenliegen, und vergleiche zwei echte Aufgaben mit und ohne Skill. Behalte ihn nur, wenn er dort messbar besser abschneidet.
