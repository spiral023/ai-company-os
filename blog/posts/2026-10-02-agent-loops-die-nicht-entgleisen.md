---
titel: "Ralph Loop ohne Drift: Ja/Nein-Kriterium, Iterationslimit, fremder Prüfer"
datum: 2026-10-02
kategorie: arbeitsweisen
zusammenfassung: "Ein Ralph Loop startet jede Iteration mit frischem Kontext und hält den Stand in Dateien und Git. Damit er nicht driftet, braucht er ein binäres Erfolgskriterium, ein Iterationslimit, Tests, die einmal rot waren, und einen Prüfer, der nicht selbst gebaut hat."
status: freigegeben
geprueft_am: 2026-10-02
quellen:
  - 2026-08-30-alex-sprogis-loop-graph-engineering-das-letzte-video-was-du-s
  - 2026-02-23-d4m1n-ralph-loop-setup-primaer
  - 2026-02-05-d4m1n-docker-sandboxes
  - 2026-02-05-carlini-anthropic-c-compiler
  - 2026-08-04-anthropic-docs-claude-code-best-practices
---

## Kurz gesagt

- Formuliere das Ziel jedes Loops so, dass es sich mit Ja oder Nein beantworten lässt, etwa „alle Tests grün“, und gib ihm eine Höchstzahl an Durchläufen mit.
- Lass Umsetzung und Prüfung von verschiedenen Instanzen erledigen. Der Agent, der den Code schreibt, meldet nie selbst „fertig“.
- Jeder Test muss einmal rot gewesen sein, sonst erfüllt ein wirkungsloser Test das Ziel „alle Tests grün“.
- Starte mit zwei Iterationen in einer Sandbox und erhöhe erst, wenn die Commits stimmen.

## Das Problem: Lange Läufe driften

Ein Agent, der viele Aufgaben in einer einzigen Session abarbeitet, schleppt jeden Fehlversuch und jeden Tool-Output mit. Die Präzision sinkt mit wachsendem Kontext (Context Rot), mehr dazu in [Nach jedem Arbeitsblock fünf Optionen](post:kontext-hygiene-entscheidungsbaum). Beim Ralph Loop beginnt deshalb jede Iteration mit leerem Kontext. Der Arbeitsstand liegt in Dateien und Git-Commits, nicht im Modell.

Frischer Kontext allein verhindert aber kein Entgleisen. Alex Sprogis nennt zwei typische Fehler. Ist das Ziel offen formuliert, trifft der Agent eigene Annahmen und dreht unnötige Runden. Ist es zu leicht zu erfüllen, nimmt er die Abkürzung und löscht beim Ziel „alle Tests grün“ Tests oder konfiguriert sie wirkungslos. Ein sauberes Kriterium allein verhindert dieses Reward Hacking nicht. {q:1}

## Die Bausteine

Dan (@d4m1n) installiert seinen Loop mit `npx @pageai/ralph-loop`. Das legt ein Verzeichnis `.agent/` an, in dem jede Datei eine klare Rolle hat. {q:2}

| Datei | Rolle |
|---|---|
| `PROMPT.md` | Die feste Anweisung, die jede Iteration bekommt |
| `SUMMARY.md` | Kurze Projektbeschreibung als Startkontext |
| `STEERING.md` | Kurskorrekturen während des Laufs, wird zu Beginn jeder Iteration gelesen |
| `tasks.json`, `tasks/` | Die Aufgabenliste mit Status |
| `prd/` | Das Anforderungsdokument |
| `logs/LOG.md`, `history/` | Protokoll und voller Output jeder Iteration |

Jede Iteration nimmt die nächste offene Aufgabe, liest die zugehörige Spezifikation, setzt sie um, lässt die Tests laufen und committet. Pro Aufgabe entsteht ein Commit. Geht etwas schief, nimmst du ihn mit `git revert` zurück, die zugehörigen Tests schlagen in der nächsten Iteration fehl, und der Loop korrigiert erneut. {q:2}

Dazu kommen drei Abbruchbedingungen, die du festlegst, bevor der Loop startet.

1. **Ein binäres Erfolgskriterium.** Sprogis schreibt Akzeptanzkriterien im Format „Angenommen X, wenn Y, dann Z“ mit festen IDs in die Spezifikation, bevor Code entsteht. Das Ziel lautet dann „alle Akzeptanzkriterien im Testbericht bestanden“. {q:1}
2. **Ein Iterationslimit.** Bei ihm sind es fünf Durchläufe für die Umsetzung eines Features und drei für einen stündlichen Audit-Loop, der nur auf einer eigenen Branch fixen darf, nie auf `main`. {q:1} Das Limit ist die einzige Kostenbremse, die er nennt.
3. **Ein deterministisches Gate.** Laut Anthropic-Doku (Stand 04.08.2026) kann ein Stop-Hook das Ende einer Session blockieren, bis ein Prüfskript besteht. Nach acht Blockierungen in Folge überschreibt Claude Code den Hook und beendet den Zug. {q:5} Ein Lauf kann also ohne bestandene Prüfung enden. Lies das Log, bevor du ihn abhakst.

## Tests als Fortschrittsmaß

Ohne installierte Tests „halluziniert“ der Agent Fortschritt, sagt d4m1n, deshalb sind Playwright und Vitest bei ihm Pflicht. {q:2} Nicholas Carlini hat bei Anthropic mit 16 parallelen Agents einen C-Compiler mit rund 100.000 Zeilen gebaut und kommt zum selben Schluss: Agents optimieren zuverlässig das, was der Prüfer misst. Ist der Prüfer unpräzise, sind sie zuverlässig falsch erfolgreich. {q:4} Seine Tests nennen deshalb die genaue Fehlerstelle, damit sich auch eine Instanz mit frischem Kontext schnell zurechtfindet.

Gegen wirkungslose Tests hilft Sprogis' Regel aus dem Test-first-Vorgehen (TDD). Jeder neue Test muss einmal rot gewesen sein. Der Agent dreht die Erwartung bewusst um oder entfernt die geprüfte Logik kurz, bestätigt den Fehlschlag, stellt alles wieder her und macht den Test dann grün. {q:1}

## Ein unabhängiger Prüfer

Wer baut und zugleich prüft, kennt den eigenen Weg und prüft weniger scharf. Sprogis trennt deshalb die Rollen: Die Spezifikation ist während Bau und Testschreiben schreibgeschützt, Build- und Test-Agent sind getrennt, die QA findet Bugs, behebt sie aber nicht. Subagents melden nie selbst „fertig“, das entscheidet der Hauptagent. Die Prüfszenarien entstehen vor der Umsetzung und bleiben dem bauenden Agent verborgen. {q:1}

Bei Anthropic ist das die höchste Stufe der Verifikation: Ein Subagent oder ein frisches Modell versucht, den Befund zu widerlegen. Ein Beispiel-Prompt lässt den Diff gegen `PLAN.md` prüfen, mit der Anweisung „Report gaps, not style preferences“. {q:5} Wie sich ein solcher Gegenprüfer vom klassischen Review unterscheidet, steht im [Duell zu Adversarial Agent und Review](post:duell-adversarial-agent-oder-review).

## Große Aufträge in Schritte zerlegen

Architektur, Aufgabenplan, Umsetzung, Test und Deployment in einem Kontext führen laut Sprogis zu Context Rot. Er lässt jeden Schritt als eigenen Loop mit frischem Kontext laufen. Weitergereicht werden nur die Ergebnisse als Dateien (Spezifikation, Architektur, Aufgabenplan, Testbericht), nicht die Zwischenschritte. {q:1} Im Ralph Loop heißt das, jede Aufgabe in `tasks.json` muss in eine Iteration mit einem Commit passen.

## Minimal-Setup in fünf Schritten

1. **Spezifikation schreiben und prüfen.** Lass dich vom Agent zur unklaren Stelle interviewen und lies jede erzeugte Aufgabenspezifikation selbst. Eine korrigierte Spec ist laut d4m1n viel billiger als zehn schlechte Commits zurückzunehmen. {q:2}
2. **Tests installieren,** bevor der Loop startet, und das Erfolgskriterium als Ja/Nein-Satz in `PROMPT.md` schreiben.
3. **In der Sandbox starten.** `docker sandbox run claude .` isoliert den Agent in einer Micro-VM mit eigenem Docker-Daemon. Der Loop selbst ist ein Bash-Skript, das `docker sandbox run claude . -- -p "$PROMPT_CONTENT"` bis `MAX_ITERATIONS` wiederholt. {q:3}
4. **Klein anfangen.** d4m1n startet mit `./ralph.sh -n 2`, geht auf 10 und erst bei Vertrauen auf 30 Iterationen über Nacht. {q:2}
5. **Commits lesen.** Nach jedem Lauf `git log` und `LOG.md` durchgehen, falsche Commits zurücknehmen und Korrekturen in `STEERING.md` schreiben.

## Wann es sich lohnt und wann nicht

Der Ralph Loop trägt bei vielen kleinen, klar prüfbaren Aufgaben: MVPs aus einem klaren Anforderungsdokument, Migrationen, repetitive Refactorings. Sein bekanntester Lauf dauerte 37 Stunden und erledigte 250 Aufgaben aus einem Anforderungsdokument mit 2.000 Zeilen, ohne dass d4m1n am Rechner saß. {q:2} Schwach ist er bei pixelgenauem Design, neuartiger Architektur ohne Vorbild und sicherheitskritischem Code. {q:2}

## Kosten und Grenzen

Mehr Loops und getrennte Prüfer kosten mehr Tokens, das nennt Sprogis selbst als Einwand. Messwerte zu seinem Aufbau gibt es nicht. {q:1} Die einzige Kostenzahl in diesem Umfeld kommt aus Carlinis Compiler-Projekt: rund 20.000 US-Dollar und knapp 2.000 Sessions in etwa zwei Wochen. {q:4} Für einen einzelnen Nachtlauf taugt das nicht als Maßstab.

Der Aufwand verschiebt sich vom Prompt zum Testaufbau, er verschwindet nicht. Und „alles grün“ heißt nicht „alles sicher“. Carlini warnt ausdrücklich, dass Tests nie alle Angriffsflächen abdecken, sobald kein Mensch mehr eng dabei ist. {q:4} Regressionen blieben auch bei ihm ein wiederkehrendes Problem.

Offen bleibt, ab welcher Aufgabengröße sich der volle Loop gegenüber einer gut geführten Session mit Handoff-Datei lohnt. Für eine kurze Liste ist der Aufbau aus Spezifikation, Tests und Sandbox oft mehr Arbeit als die Aufgaben selbst.

Bau den ersten Ralph Loop für eine Aufgabenliste, die du ohnehin abarbeiten musst und für die schon Tests existieren. Schreib das Ja/Nein-Kriterium, das Iterationslimit und die Rot-dann-grün-Regel in `PROMPT.md`, lass einen zweiten Agent gegen die Spezifikation prüfen und starte mit zwei Iterationen.
