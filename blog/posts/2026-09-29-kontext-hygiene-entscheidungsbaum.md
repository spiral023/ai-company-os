---
titel: "Nach jedem Arbeitsblock fünf Optionen: Weiter ist der riskanteste Default"
datum: 2026-09-29
kategorie: arbeitsweisen
zusammenfassung: "Continue, rewind, compact, clear oder Subagent: Wie du nach jedem Block eines Coding-Agents entscheidest, was jede Option kostet und warum feste Schwellenwerte nur Erfahrungswerte sind."
status: freigegeben
geprueft_am: 2026-09-29
freigabe: automatisch
quellen:
  - 2026-04-15-trq212-claude-code-session-management-1m-context-primaer
  - 2026-03-29-0x-kaize-claude-usage-limits-primaer
  - 2026-05-01-mnilax-claude-code-overhead-9-patterns
  - 2026-01-25-sankalp-claude-code-experience
  - 2026-07-27-cerebras-gpt-5-6-modellwahl-und-reasoning
  - 2026-02-10-boris-tane-plan-annotation-workflow
  - 2026-08-04-anthropic-docs-claude-code-best-practices
---

## Kurz gesagt

- Nach jedem Arbeitsblock hast du fünf Optionen: weiter, zurückspulen (`rewind`), `/compact`, `/clear` oder Subagent. Der Reflex „einfach weiterschreiben“ ist die riskanteste.{q:1}
- Lange Threads werden teuer und ungenauer. Aktives Aufräumen hilft, Prompt-Caching spricht aber dagegen.
- Feste Schwellenwerte („ab X Prozent aufräumen“) sind Erfahrungswerte einzelner Autoren. Beobachte deine eigenen Sessions und lege die Grenze dort fest.

## Das Problem

Ein Agent liest bei jeder Antwort den gesamten bisherigen Verlauf erneut, samt Fehlversuchen, Tool-Outputs und verworfenen Hypothesen. Die Präzision sinkt („Context Rot“), und der Tokenverbrauch wächst schneller als die Arbeit.

Wie schnell, hat kaize im März 2026 vorgerechnet.{q:2} Bei 500 Tokens pro Austausch braucht ein Chat mit 5 Nachrichten 7.500 Tokens, einer mit 30 Nachrichten 232.500. Das ist das 31-Fache bei sechsfacher Länge. Bei langen Chats sollen bis zu 98,5 % der Tokens auf das Wiedereinlesen entfallen.{q:2} Das ist ein Rechenmodell ohne Caching, keine Messung.

## Die fünf Optionen

Die Aufteilung stammt von Thariq (Anthropic).{q:1} Er nennt `Continue` ausdrücklich den riskanten Default.

| Option | Wann | Was sie kostet |
|---|---|---|
| Continue | Dieselbe Aufgabe läuft weiter, gelesene Dateien sind noch nützlich | Der Kontext wächst, Fehlversuche bleiben drin |
| `rewind` | Ein falscher Lösungsweg wurde eingeschlagen | Der Fehlversuch verschwindet, aber auch das Gelernte. Rewind setzt Code und Konversation gemeinsam zurück{q:4} |
| `/compact` | Gleicher Problemraum, der Kontext soll leichter werden | Verlustbehaftet: Das Modell entscheidet, was wichtig war |
| `/clear` | Neue Aufgabe oder Phase | Der gesamte Kontext ist weg. Handoff-Datei oder Spec baust du selbst |
| Subagent | Viel Zwischenoutput, später zählt nur die Schlussfolgerung | Eigener Kontext plus Grundkosten pro Aufruf |

## Woran du entscheidest

1. **Falscher Weg?** Dann `rewind`, nicht „nein, mach es anders“. Eine Korrekturnachricht lässt den Fehlversuch im Kontext. Boris Tane nennt dieselbe Logik Verwerfen und Neuscopen.{q:6}
2. **Braucht die nächste Aufgabe die gelesenen Dateien?** Wenn ja, bleib dabei. Thariqs Beispiel: direkt nach dem Feature die zugehörige Doku schreiben. Sonst gilt „neue Aufgabe, neue Session“.{q:1}
3. **Fällt viel Zwischenoutput an?** Frag dich, ob du den Tool-Output später noch brauchst oder nur die Schlussfolgerung. Bei Letzterem gehört die Arbeit in einen Subagent.{q:1}
4. **Willst du verdichten, ohne Phase oder Ziel zu wechseln?** Dann `/compact` mit klarem Fokus, was erhalten bleiben muss. Laut Anthropic-Doku (Stand 04.08.2026) gibt es dafür `/rewind` mit „Summarize from/up to this message“ und eine Compaction-Anweisung in der `CLAUDE.md`, etwa die Liste geänderter Dateien immer zu behalten.{q:7}
5. **Ist die Session ohnehin überladen?** Dann `/clear` mit vorherigem Handoff. Sankalp startet seinen `/handoff`-Befehl typischerweise bei rund 60 % Auslastung, bewusst vor dem automatischen Compact.{q:4}

Der Zeitpunkt zählt. Schlechte Compacts entstehen laut Thariq oft, wenn der automatische Trigger erst bei sehr vollem Kontext greift. Das Modell fasst dann nicht im besten Zustand zusammen. Kompaktiere lieber früh und aktiv.{q:1}

In Claude Code kommt hinzu, dass der Autocompact-Puffer mit 45.000 Tokens reserviert ist, bei einem 200k-Fenster also 22,5 %.{q:4} „60 % Auslastung“ bezieht sich daher auf das nutzbare Fenster, nicht auf das ganze. Das lesen wir aus nur zwei `/context`-Screenshots.

## Wo es sich nicht lohnt

Bei kurzen Aufgaben ohne Fehlversuche ist die Entscheidung pro Turn reiner Overhead. Mnimiy hat 90 Tage lang über einen HTTP-Proxy mitgeschnitten (430 Stunden, 6 Mio. Input-Tokens, 1.340 USD). Nur 27 % der Tokens waren produktiv.{q:3} Den Rest fraßen vor allem feste Posten: eine 4.800 Token große `CLAUDE.md`, Hooks, ungenutzte Skills und MCP-Server, Cache-Misses nach Pausen. Aggressives `/clear` nach jeder Aufgabe hält er oft für kontraproduktiv.{q:3} Das ist eine Einzelmessung, aber sie legt die Reihenfolge nahe: erst den festen Ballast pro Turn kürzen, dann die Session-Disziplin verfeinern.

## Cache gegen Sauberkeit

Cerebras rechnet vor, dass Cached Input nur 10 % des Normalpreises kostet und die TTL bei etwa 30 Minuten liegt (OpenAI-Preise vom 21.07.2026, drei GPT-5.6-Modelle).{q:5} Eine durchgehende warme Session ist damit billiger als eine neue pro Aufgabe, weil jeder Neustart die Codebasis wieder zum vollen Preis einliest. Auch Mnimiy nennt Cache-Misses nach Pausen als Kostenfaktor.{q:3} Für die Qualität spricht dagegen alles für frühes Aufräumen. Wo die Grenze liegt, hängt von deinem Workload ab. Prüfe die Preise deines Anbieters, bevor du rechnest.

## Compaction: gut genug?

Cerebras behauptet, die Codex-Kompaktion trage Sessions über hunderte Millionen Tokens.{q:5} Das passt nicht zu den Erfahrungen der anderen Autoren. Boris Tane arbeitet Recherche, Planung und Umsetzung bewusst in einer einzigen langen Session und sieht nach eigener Aussage keinen Abfall nach 50 % Fensterauslastung. Sein Plandokument überlebt die Auto-Compaction.{q:6} Beide Lager treffen sich vermutlich hier: Was in einer Datei steht, geht beim Kompaktieren nicht verloren. Ob `/compact` mit Fokus reicht oder ein Handoff-Dokument vor `/clear` nötig ist, hat bisher niemand geklärt.

## Empfehlung

Nimm den Baum als Gewohnheit, nicht als Formel:

1. Wähle nach jedem Block bewusst, statt zu tippen. Bei einem falschen Weg zuerst `rewind`.
2. Schreibe Zwischenstände in Dateien (Plan, Handoff, Spec). Dann kosten `/compact` und `/clear` wenig, und die Cache-Frage verliert Gewicht.
3. Miss zuerst den festen Overhead pro Turn (`CLAUDE.md`, Hooks, MCP, Skills), dann die Session-Länge. Die Schwellenwerte der Autoren streuen von 20 bis 60 % eines 200k-Fensters, bei Thariq liegt die Rot-Schwelle im 1M-Modell bei etwa 300.000 bis 400.000 Tokens.{q:1}{q:4} Beobachte, wann deine Sessions abdriften, und lege die Grenze dort fest.
