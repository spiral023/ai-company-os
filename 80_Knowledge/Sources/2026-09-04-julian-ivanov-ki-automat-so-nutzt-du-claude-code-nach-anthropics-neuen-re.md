---
url: https://www.youtube.com/watch?v=4v_XNgWTLiM
autor: Julian Ivanov | KI-Automatisierung
datum: 2026-09-04
erfasst: 2026-09-14
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-09-04-julian-ivanov-ki-automat-so-nutzt-du-claude-code-nach-anthropics-neuen-re.md
thema: Arbeitsweisen
zeitkritisch: ja
---

# Zwölf Claude-Code-Gewohnheiten, die mit Opus 5 und Fable 5 bremsen

Ivanov geht zwölf verbreitete Fehler im Umgang mit Claude Code durch und stützt sich dabei auf Anthropics Doku und Blogbeiträge (Stand Sommer 2026). Der rote Faden: weniger Anweisungen, mehr Absicht, Referenzen und Verifikation; Context Window klein halten; Setup regelmäßig ausdünnen. Die Belege sind Anthropic-Aussagen aus zweiter Hand (Video), nicht selbst geprüft. Die letzten Minuten enthalten Eigenwerbung für eine Community und wurden ignoriert.

## Prompting: Absicht, Referenz, Abschlusskriterium
- Rollenfloskeln („Du bist ein exzellenter Autor“) bringen laut Video nichts außer Stil; Druckfloskeln („extrem wichtig“) ebenso wenig.
- Nenne Grund und Ziel, nicht nur die Anweisung; die Fable-5-Doku nennt als Vorlage sinngemäß Aufgabe, Zielgruppe, benötigter Output.
- Zeige statt zu beschreiben: Referenzdateien per `@` einbinden (im Beispiel frühere Newsletter statt Stilbeschreibung).
- Definiere „fertig“ messbar („500 Wörter, drei bis vier Absätze, ein Tipp“) und sage, wogegen Claude prüfen soll. Das ist laut Video der wichtigste Tipp der Best-Practices-Doku, weil Claude dann in der agentischen Schleife bleibt.
- Nenne auch, was du nicht willst: Opus 5 und Fable 5 übernehmen gern ungefragt Zusatzaufgaben.
- Wiederkehrende Aufgaben nach einem gelungenen Durchlauf als Skill festhalten.
- Positiv formulieren: „antworte in höchstens fünf Sätzen“ statt „fass dich nicht zu lang“; viele Verbote müssen gegeneinander abgewogen werden. Anthropic habe genau solche Negativregeln aus dem Claude-Code-Systemprompt gestrichen (rund 80 Prozent gekürzt, Modell laut Anthropic dadurch besser).

## Context Window und Kosten
- Modellwechsel mitten in der Session entwertet den Prompt Cache; der gesamte Verlauf wird neu verarbeitet. Empfehlung: ein Modell pro Aufgabe, für neue Aufgaben neue Session.
- Bei einer Million Token Kontext findet das Modell laut MRCR-Benchmark nur 76 Prozent versteckter Informationen wieder, bei rund 256 000 Token 93 Prozent (Angabe im Video, Original nicht geprüft). Also `/clear`, `/compact` oder ein Handoff in eine Datei (Skill von Matt Pocock); `/context` zeigt die Füllung.
- Schon vor der ersten Nachricht liegen Systemprompt, Auto Memory, Umgebungsinfo, MCP-Tools, Skills und CLAUDE.md im Kontext.
- Ort der Information angeben (`@`-Referenz), sonst „Infinite Exploration“: Claude liest Dateien auf Verdacht, alles landet im Kontext.
- Effort: Standard ist `high`. Ein Anthropic-Beispiel zeigt rund siebenfache Tokenmenge von niedriger zu hoher Stufe. Faustregel: `high` im Alltag, `medium`/`low` für Routine, `xhigh` für Aufgaben über etwa eine halbe Stunde; `max` überdenkt gern, Ultracode (`xhigh` plus Subagent-Teams) nur für die komplexesten Fälle.

## Setup: CLAUDE.md, Hooks, Skills, Memory
- CLAUDE.md ist nur zusätzlicher Kontext und wird bei vollem Kontext auch mal ignoriert. Was garantiert passieren muss (Umlaute prüfen, Credential-Dateien sperren), gehört in Hooks, die deterministisch laufen.
- CLAUDE.md wird nur beim Sessionstart geladen; Änderungen wirken erst in einer neuen Session.
- Richtwert unter 200 Zeilen; wie Code behandeln, bei Fehlern prüfen, regelmäßig kürzen und Wirkung beobachten. `/doctor` dient als Diagnose.
- Für ältere Modelle geschriebene Skills sind laut Fable-5-Doku oft zu vorschreibend und verschlechtern das Ergebnis. Boris Cherny: alle sechs Monate CLAUDE.md, Skills und Hooks löschen und testen, was das Modell allein kann.
- Auto Memory (`~/.claude/projects/…/memory`) wird jede Session geladen und kann CLAUDE.md widersprechen; regelmäßig auf Widersprüche und Veraltetes prüfen.
- Skills in Cowork und Claude Code sind getrennte Ablagen; Hooks laufen nur in Claude Code, CLAUDE.md in beiden.

## Einordnung
Inhaltlich meist Bestätigung bekannter Anthropic-Empfehlungen, gut für Einsteiger gebündelt; neu gegenüber älteren Quellen sind vor allem der Rückbau (Setup regelmäßig ausdünnen, Negativregeln vermeiden) und die Effort-Faustregel. Zahlen (MRCR 93/76 Prozent, siebenfache Tokens) sind Anthropic-Angaben, im Video ohne Methode zitiert. Die Kostenseite des Rückbaus (Test, ob ein Skill noch nötig ist) bleibt unerwähnt; „löschen und schauen“ setzt eine Möglichkeit zur Verifikation voraus. Die Session-Kosten durch Modellwechsel sind plausibel, aber hier nicht gemessen.

## Kernaussagen
- Was garantiert gelten muss, in Hooks statt CLAUDE.md legen. → [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]
- Grund, Ziel und messbares Abschlusskriterium statt Rollenfloskeln und Verbotslisten. → [[Fable-Unknowns-vor-Prompt-Qualitaet]]
- Neue Aufgabe, neue Session; `/compact`, `/clear` oder Handoff bei langem Kontext. → [[Kontext-Hygiene-Entscheidungsbaum]]
- Handoff als Skill für den Sessionwechsel. → [[Handoff-Doc]]

## Verbindungen
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]
- [[2026-07-25-agenticjames-they-cut-claude-code-system-prompt-by-80-and-you-should-be-doing-the]]
- [[2026-07-08-claudedevs-modell-vs-effort]]
- [[2026-04-15-trq212-claude-code-session-management-1m-context-primaer]]
