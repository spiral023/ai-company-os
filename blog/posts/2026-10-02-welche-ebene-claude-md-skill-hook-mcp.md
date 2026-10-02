---
titel: "Hook, Skill oder CLAUDE.md? Fünf Fragen, wohin eine Anforderung gehört"
datum: 2026-10-02
kategorie: arbeitsweisen
zusammenfassung: "Wann eine Regel in die CLAUDE.md gehört, wann in einen Skill, einen Slash-Command, einen Subagent, einen Claude Code Hook oder einen MCP-Server: ein Entscheidungsbaum mit Beispielen, typischen Fehlzuordnungen und dem Code-Mode-Ansatz für MCP."
status: freigegeben
geprueft_am: 2026-10-02
quellen:
  - 2026-02-01-anthropic-docs-extend-claude-code
  - 2026-01-21-tempoimmaterial-agent-skills-vs-rules-vs-commands
  - 2026-01-06-jarrodwatts-context-engineering-guide
  - 2026-02-01-anthropic-docs-automate-workflows-with-hooks
  - 2026-09-17-agenticjames-i-think-code-mode-mcps-are-probably-the-best-way-to-give-agents-access
  - 2026-09-27-anthropic-academy-sdlc-playbook
---

## Kurz gesagt

- Jede Anforderung bekommt genau eine Heimat. Was garantiert passieren muss, gehört in einen Hook, was immer gilt, in die CLAUDE.md, was nur bei bestimmten Aufgaben zählt, in einen Skill oder Slash-Command.
- Externe Daten und Aktionen laufen über MCP, laute oder anders berechtigte Teilarbeit über einen Subagent.
- Den Hook-Typ wählst du danach, wie sich die Bedingung prüfen lässt: Skript, Modellurteil oder Prüflauf mit Tools.
- Viele MCP-Server kosten Kontext in jedem Turn. Ein einzelnes Skript-Tool vor den Servern hält Definitionen und große Ausgaben klein.

## Das Problem

Eine Regel landet in der CLAUDE.md, später entsteht ein Skill zum selben Thema, und nach dem ersten Unfall kommt ein Hook dazu. Die drei Fassungen driften auseinander, und niemand weiß mehr, welche gilt. So wird ein Setup schnell unübersichtlich.

Die Ebenen unterscheiden sich in Verantwortung und Preis. Laut Anthropics Übersicht (Stand Februar 2026) liegt die CLAUDE.md bei jedem Request im Kontext, ebenso die Definitionen aller MCP-Tools. Von Skills sieht das Modell nur die Beschreibung, bis es einen Skill lädt. Hooks kosten keinen Kontext {q:1}. Eine Regel an der falschen Stelle kostet also dauerhaft Tokens oder wird nicht durchgesetzt.

## Die Entscheidungsfragen

Geh die Fragen in dieser Reihenfolge durch und hör beim ersten Ja auf.

1. **Muss es garantiert passieren, auch wenn das Modell es vergisst?** Dann ein Hook. Die CLAUDE.md ist Kontext, dem das Modell folgen kann oder nicht. Ein `PreToolUse`-Hook bekommt den geplanten Tool-Aufruf als JSON und blockiert ihn mit Exit-Code 2 {q:4}. Anthropics Academy-Kurs zum Entwicklungsprozess nennt Skills ausdrücklich beratend und verlangt für alles, was immer gelten muss, zusätzlich einen Hook oder einen Review-Schritt {q:6}.
2. **Braucht es Daten oder Aktionen außerhalb des Repos?** Dann MCP, etwa für Datenbank, Browser oder Ticketsystem. Der Server liefert den Zugang, wie die Tools zu nutzen sind, beschreibt ein Skill {q:1}.
3. **Soll es gelten, auch wenn du gerade nicht daran denkst?** Diesen Test schlägt Alice Moore vor {q:2}. Bei Ja gehört es in die CLAUDE.md, etwa „Das Design-System nutzt diese Token-Namen“. Bei Nein ist es ein Skill, etwa „Bei Änderungen am Billing-Code diese Integrationstests ausführen“.
4. **Startest du es selbst, oder soll das Modell es erkennen?** Den bewussten Start übernimmt ein Slash-Command, das Erkennen ein Skill. Moore empfiehlt beides zusammen: Die Logik bleibt im Skill, `/release` lädt ihn nur und arbeitet die Checkliste ab {q:2}. Wie du Skill-Beschreibungen auf einen engen Auslöser zuschneidest, steht im Beitrag zu [alten Prompts und neuen Modellen](post:alte-prompts-neue-modelle).
5. **Braucht die Arbeit einen eigenen Kontext, andere Rechte oder ein anderes Modell?** Dann ein Subagent. Ein Skill ändert, was der aktuelle Agent weiß, ein Subagent ändert, wer arbeitet. Moore rät, erst bei getrennten Rechten, einem anderen Modell oder verschmutztem Hauptkontext zu wechseln {q:2}. Wann sich die Auslagerung für den Kontext lohnt, zeigt der [Entscheidungsbaum zur Kontext-Hygiene](post:kontext-hygiene-entscheidungsbaum).

Ein Plugin bündelt Skills, Hooks und MCP-Konfiguration zu einem installierbaren Paket und kommt ins Spiel, sobald du ein Setup weitergibst. Ob ein Plugin etwas bringt, misst du mit [Plugin-Evals](post:plugin-evals-in-claude-code).

## Zuordnungstabelle mit Beispielen

| Anforderung | Ebene | Warum |
|---|---|---|
| Testbefehl, Paketmanager, Ordnerkonventionen | CLAUDE.md | Gilt in jeder Session, kurz genug {q:1} |
| Keine Schreibzugriffe auf `.env`-Dateien | Hook (`PreToolUse`) | Muss technisch blockieren {q:4} |
| Formatter nach jedem Speichern | Hook (`PostToolUse`) | Immer gleicher Auslöser, kein Urteil nötig {q:6} |
| Release Notes nach Format und Checkliste | Skill, dazu `/release` | Nur bei dieser Aufgabe, explizit gestartet {q:2} |
| Codebasis durchsuchen, Logs auswerten | Subagent | Viel Zwischenoutput, zurück kommt nur das Ergebnis {q:1} |
| Fehler in der Produktionsdatenbank nachsehen | MCP-Server, Skill erklärt die Abfragen | Externe Quelle {q:1} |
| Deployment nur nach Freigabe | Hook als Gate (Exit-Code 2) | Nicht verhandelbar, zentral verwaltet {q:6} |

Für die Länge der CLAUDE.md nennt Anthropics Übersicht etwa 500 Zeilen als Obergrenze {q:1}, der Academy-Kurs weniger als eine Seite. Laut Kurs gehört eine Korrektur in die Datei, sobald du sie zum zweiten Mal geben musst {q:6}.

## Hook-Typ nach Prüfbarkeit wählen

Ein Hook muss kein Shell-Skript sein. Die Hooks-Doku nennt zwei weitere Typen {q:4}:

| Bedingung | Hook-Typ | Beispiel |
|---|---|---|
| Lässt sich vorab in Code fassen | Skript | Enthält der Pfad `.env`? |
| Braucht sprachliches Urteil | `type: "prompt"`, ein Modell entscheidet Ja oder Nein | Verändert der Commit die öffentliche API? |
| Lässt sich nur durch Ausführen prüfen | `type: "agent"`, ein Subagent mit Tools | Laufen alle Tests? |

Nimm die erste Zeile, die passt. Prompt- und Agent-Hooks opfern einen Teil der Vorhersagbarkeit, derentwegen du einen Hook einsetzt, und der Agent-Hook startet für eine einzige Bedingung einen ganzen Subagent-Lauf. Wie zuverlässig beide entscheiden, beschreibt die Doku nicht. Mit dem `matcher` grenzt du jeden Hook auf bestimmte Tools ein, etwa `Edit|Write`, damit er nicht bei jedem Aufruf feuert {q:4}. Ein Stop-Hook als Abschluss-Gate für lange Läufe steht im Beitrag zu [Agent-Loops, die nicht entgleisen](post:agent-loops-die-nicht-entgleisen).

## Typische Fehlzuordnungen

- **Dieselbe Regel in CLAUDE.md, Skill und Hook.** Lege das Wissen an einer Stelle ab und die Durchsetzung im Hook. In der CLAUDE.md bleibt höchstens ein Verweis. Skill und Hook zum selben Thema sind in Ordnung, solange der Skill erklärt und der Hook erzwingt {q:6}.
- **Pflichtregel nur als Text.** „Committe nie `.env`“ in der CLAUDE.md ist eine Bitte. Auch ein Hook deckt nur ab, was er prüft. Das `.env`-Beispiel der Doku fängt direkte Schreibzugriffe ab, Lesezugriffe über andere Tools nicht {q:4}.
- **Der Skill für alles.** Ein Skill, der auf jede Aufgabe passt, ist eine Regel und gehört in die CLAUDE.md {q:2}.
- **Der allmächtige Subagent.** Ein Subagent bekommt ein eigenes Context Window und kann ein günstigeres Modell nutzen. Jarrod Watts lässt etwa einen Recherche-Subagent auf Sonnet laufen, der dem Hauptagent auf Opus nur eine Zusammenfassung liefert {q:3}. Gib ihm nur die Tools, die er für diese Aufgabe braucht.
- **Arbeitslogik im MCP-Server.** Abläufe, Prüfschritte und Formate gehören in einen Skill, der Server liefert nur Zugriff {q:1}.

## Code Mode: ein Skript-Tool statt vieler MCP-Tools

Jeder zusätzliche MCP-Server legt seine Tool-Definitionen in jeden Request {q:1}. Claude Code lädt Definitionen inzwischen über Tool Search bei Bedarf nach {q:2}. Große Ausgaben bleiben trotzdem ein Problem, weil ein klassisches MCP-Tool seinen JSON-Body ungefiltert in den Kontext schreibt.

Der Code-Mode-Ansatz setzt ein Gateway vor alle Server. Laut @agentic.james sieht der Agent nur ein Tool, sucht darüber die passenden MCP-Tools, schreibt ein Skript und führt damit mehrere Aufrufe in einem Call aus {q:5}. Das Skript filtert die Ausgabe, bevor sie im Context Window landet, und verkettet Tools passend zur Aufgabe. Als Umsetzungen nennt er das selbst hostbare Gateway `executor` und ein Code-Mode-Gateway von Docker {q:5}. Messwerte zeigt er nicht, und er bewirbt einen eigenen Kurs.

Die Kosten nennt er nicht. Das Skript braucht eine Sandbox, die Tool-Suche ist ein zusätzlicher Schritt, und generierter Code kann Parameter falsch setzen. Das Gateway bündelt zudem die Zugangsdaten aller angeschlossenen Server an einer Stelle. Bei zwei oder drei Servern mit kleinen Antworten lohnt sich das nicht. Interessant wird es bei vielen Servern oder Tools, die große Datenmengen zurückgeben.

## Empfehlung

Die Zuordnung ist eine Heuristik, Grenzfälle bleiben Ermessenssache, und jede Ebene will gepflegt werden, denn Hooks sind Code und Skills veralten mit dem Modell. Nimm dir deine CLAUDE.md vor und frag bei jeder Zeile, ob sie garantiert gelten muss, nur bei bestimmten Aufgaben zählt oder externe Daten braucht. Pflichtregeln wandern in einen Hook mit dem einfachsten passenden Typ, Aufgabenwissen in einen Skill, und jede doppelte Fassung fliegt raus. Erst wenn die Datei kurz ist und mehrere MCP-Server Kontext fressen, lohnt sich ein Code-Mode-Gateway.
