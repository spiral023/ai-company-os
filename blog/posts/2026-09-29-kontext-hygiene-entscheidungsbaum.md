---
titel: "Nach jedem Arbeitsblock fünf Optionen: Weiter ist der teuerste Default"
datum: 2026-09-29
kategorie: arbeitsweisen
zusammenfassung: "Continue, rewind, compact, clear oder Subagent: Wie man nach jedem Block eines Coding-Agents entscheidet, was jede Option kostet und wie dünn die Belege für konkrete Schwellenwerte sind."
status: entwurf
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

- Nach jedem abgeschlossenen Arbeitsblock stehen fünf Optionen zur Wahl: weiter, zurückspulen (`rewind`), `/compact`, `/clear` oder Subagent. Der Reflex „einfach weiterschreiben“ ist die riskanteste.
- Die Kosten wachsen bei langen Threads näherungsweise quadratisch, die Qualität sinkt durch Altlasten im Kontext. Beides spricht für aktives Aufräumen, doch Prompt-Caching zieht in die Gegenrichtung.
- Die Grundidee ist mehrfach belegt, die konkreten Schwellenwerte („ab X Prozent aufräumen“) sind es nicht. Sie sind Erfahrungswerte einzelner Autoren.

## Das Problem

Ein Agent liest bei jeder Antwort den gesamten bisherigen Verlauf erneut. Dazu gehören Fehlversuche, Tool-Outputs und verworfene Hypothesen. Zwei Effekte folgen daraus: Die Präzision sinkt („Context Rot“), und der Tokenverbrauch wächst schneller als der Arbeitsaufwand.

Die Kostenseite hat eine Primärquelle mit Rechnung. Der X-Autor kaize (März 2026) nimmt 500 Tokens pro Austausch an und kommt mit `S · N(N+1)/2` auf 7.500 Tokens bei 5 Nachrichten und 232.500 bei 30. Nachricht 30 ist damit 31-mal so teuer wie Nachricht 1. Bei langen Chats sollen bis zu 98,5 % der Tokens auf das Wiedereinlesen entfallen. Das ist ein Rechenmodell, keine Messung, und es ignoriert Caching.

## Die fünf Optionen

Die Aufteilung stammt von Thariq (Anthropic), der sie im April 2026 auf X beschrieben hat. `Continue` nennt er ausdrücklich den riskanten Default.

| Option | Wann | Was sie kostet |
|---|---|---|
| Continue | Dieselbe Aufgabe läuft weiter, gelesene Dateien sind noch nützlich | Der Kontext wächst weiter, Fehlversuche bleiben drin |
| `rewind` | Ein falscher Lösungsweg wurde eingeschlagen | Der Fehlversuch verschwindet, aber auch das damit Gelernte. Laut Sankalp setzt Rewind Code und Konversation gemeinsam zurück |
| `/compact` | Gleicher Problemraum, aber der Kontext soll leichter werden | Verlustbehaftet: Das Modell entscheidet, was wichtig war |
| `/clear` | Neue Aufgabe oder Phase mit bewusst formulierter Rahmung | Der gesamte Kontext ist weg. Du musst ihn selbst neu aufbauen (Handoff-Datei, Spec) |
| Subagent | Viel Zwischenoutput, später zählt nur die Schlussfolgerung | Eigener Kontext plus Grundkosten pro Aufruf |

## Woran man entscheidet

Fünf Fragen decken die meisten Fälle ab.

1. **Falscher Weg?** Dann `rewind`, nicht „nein, mach es anders“. Eine Korrekturnachricht lässt den Fehlversuch im Kontext. Boris Tane beschreibt dieselbe Logik als Verwerfen und Neuscopen. Bei Thariq gehört dazu die Formulierung „verwirf das und implementiere die elegante Lösung“.
2. **Braucht die nächste Aufgabe die gelesenen Dateien?** Wenn ja, bleib dabei. Thariqs Beispiel: direkt nach dem Feature die zugehörige Doku schreiben. Sonst gilt die Faustregel „neue Aufgabe, neue Session“.
3. **Fällt viel Zwischenoutput an?** Thariqs Test lautet: Brauche ich den Tool-Output später noch, oder nur die Schlussfolgerung? Bei „nur die Schlussfolgerung“ gehört die Arbeit in einen Subagent.
4. **Will ich verdichten, ohne Phase oder Ziel zu wechseln?** Dann `/compact` mit ausdrücklichem Fokus, was erhalten bleiben muss. Die Anthropic-Doku (Stand 4. August 2026) nennt zwei feinere Werkzeuge: `/rewind` mit „Summarize from/up to this message“ sowie eine Compaction-Anweisung in der `CLAUDE.md`, etwa die Liste geänderter Dateien immer zu behalten.
5. **Ist die Session ohnehin überladen?** Dann `/clear` mit vorherigem Handoff. Sankalp löst einen eigenen `/handoff`-Befehl nach eigener Angabe typischerweise bei rund 60 % Auslastung aus, bewusst vor dem automatischen Compact.

Der Zeitpunkt ist wichtiger, als es klingt. Thariq beobachtet, dass schlechte Compacts oft entstehen, wenn der automatische Trigger erst bei sehr vollem Kontext greift. Das Modell fasst dann nicht im besten Zustand zusammen. Seine Konsequenz: früh und aktiv kompaktieren.

Für Claude Code kommt eine Einschränkung dazu: Zwei `/context`-Screenshots (Jarrod Watts, Sankalp) zeigen denselben Autocompact-Puffer von 45.000 Tokens, also 22,5 % eines 200k-Fensters. Der Puffer scheint ein fester Anteil zu sein. „60 % Auslastung“ bezieht sich also nicht auf das volle Fenster, sondern auf das, was davon nutzbar ist.Das ist eine Lesart aus nur zwei Screenshots.

## Wo es sich nicht lohnt

Bei kurzen Aufgaben ohne Fehlversuche ist die explizite Entscheidung pro Turn reiner Overhead. Auch Mnimiy (@Mnilax) warnt vor Übertreibung. In seinem 90-Tage-Audit über einen HTTP-Proxy (430 Stunden, 6 Mio. Input-Tokens, 1.340 USD) waren nur 27 % der Tokens produktiv. Zu den neun Posten zählen neben langen Chats vor allem Struktur: eine 4.800 Token große `CLAUDE.md`, Hooks, ungenutzte Skills und MCP-Server sowie Cache-Misses nach Pausen. Aggressives `/clear` nach jeder Aufgabe nennt er oft kontraproduktiv. Es ist eine Einzelmessung eines einzelnen Setups, aber sie verschiebt die Priorität: erst den festen Ballast pro Turn kürzen, dann die Session-Disziplin verfeinern.

## Wie belastbar ist das?

Das Pattern führt die Konfidenz „mehrfach-belegt“. Das bedeutet hier:

- **Kernaussage gut gestützt.** „Kontext ist die knappste Ressource, ein größeres Fenster löst das nicht“ kommt von mehreren Autoren, die die Notizen als unabhängig einordnen. Dazu gehören Thariq, kaize, Mnimiy, mrexodia und Jarrod Watts. Für die Empfehlung `rewind` statt Korrektur gibt es zusätzlich die offizielle Doku.
- **Die Beschaffung ist zum Teil sekundär.** Die Notizen weisen selbst darauf hin, dass mehrere dieser Aussagen über Sammlungen und Wiki-Zusammenfassungen kamen und nicht gegen die Original-Posts nachgeprüft wurden. Für Thariq und kaize liegen inzwischen Primärquellen vor.
- **Schwellenwerte streuen.** Die Rot-Schwelle liegt bei Thariq bei etwa 300.000 bis 400.000 Tokens im 1M-Modell („keine harte Grenze“). Andere Autoren nennen 20–40 %, 30 % oder 50–60 % eines 200k-Fensters. Ein Autor widerspricht sich zwischen zwei Threads selbst. Das sind Erfahrungswerte für unterschiedliche Fenster und Modelle, nicht vergleichbar und nicht gemessen.
- **Kaum Messungen.** Die harten Zahlen sind kaizes Rechenmodell und Mnimiys Audit. Wie stark die Antwortqualität bei welcher Füllung wirklich fällt, belegt keine der gelesenen Quellen mit einer Messreihe.

## Spannungen

**Cache gegen Sauberkeit.** Cerebras (Juli 2026) rechnet vor: Cached Input kostet 10 % des Normalpreises, die TTL liegt bei etwa 30 Minuten. Das bestätigt die OpenAI-Preisseite im Artikel für die drei genannten GPT-5.6-Modelle. Daraus folgt: Eine durchgehende warme Session ist billiger als eine neue pro Aufgabe, weil jeder Neustart die Codebasis wieder zum vollen Preis einliest. Mnimiy nennt Cache-Misses nach Pausen als eigenen Kostenfaktor. Das Pattern rät aus Qualitätsgründen zu frühem Aufräumen. Kostenoptimum und Kontextqualität zeigen in verschiedene Richtungen. Die Grenze hängt von deinem Workload ab, und keine Quelle liefert dafür eine Formel. Achtung: Die Preise sind OpenAI-Preise vom 21. Juli 2026. Die Zahlen für deinen Anbieter musst du gegen dessen Preisseite prüfen.

**Compaction: verlustbehaftet oder gut genug?** Cerebras behauptet, die Codex-Kompaktion reiche für Sessions über hunderte Millionen Tokens. Das ist unbelegt und widerspricht der Erfahrung der anderen Quellen. Boris Tane arbeitet Recherche, Planung und Umsetzung bewusst in einer einzigen langen Session und sieht nach eigener Aussage keine Degradation nach 50 % Fensterauslastung. Sein Plandokument überlebt die Auto-Compaction. Das ist eine Selbstauskunft ohne Messung, aber sie zeigt den Punkt, an dem beide Lager sich vermutlich treffen: Was in einer Datei steht, geht beim Kompaktieren nicht verloren.

**Handoff oder Compact?** Offen bleibt, wann `/compact` mit Fokus reicht und wann ein explizites Handoff-Dokument vor `/clear` nötig ist. Sankalp und Tane deuten beide auf Dateien als Gedächtnis hin, aber eine Regel steht in keiner Quelle.

## Empfehlung

Behandle den Baum als Gewohnheit, nicht als Formel. Drei Schritte reichen für den Anfang:

1. Wähle nach jedem Block bewusst, statt zu tippen. Bei einem falschen Weg immer zuerst `rewind`.
2. Schreibe Zwischenstände in Dateien (Plan, Handoff, Spec). Dann kosten `/compact` und `/clear` wenig, und die Cache-Frage verliert Gewicht.
3. Miss vor allem den festen Overhead pro Turn (`CLAUDE.md`, Hooks, MCP, Skills), bevor du an der Session-Länge feilst. Für den eigenen Schwellenwert gibt es keine belastbare fremde Zahl. Beobachte, wann deine Sessions abdriften, und leg die Grenze dort fest.
