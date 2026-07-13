---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-29
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Claude Code Session-Management mit 1M Context“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/02-agent-guides-und-templates/wka-claude-code-session-management-1m-context-2026-04-29.md`), Zusammenfassung eines X-Artikels von Thariq (@trq212, 15.04.2026) über vibedeck.sp23.online.

Kernpunkte (kondensiert):

- Ein sehr großes Context Window ist kein automatischer Qualitätsgewinn: Es erlaubt längere Arbeitsphasen, erhöht aber das Risiko für Context Pollution und Context Rot. Die Quelle nennt für das 1M-Modell grob 300k-400k Tokens als Heuristik, ab der Context Rot spürbar wird (keine harte Grenze).
- Nach jedem abgeschlossenen Arbeitsblock gibt es fünf sinnvolle Anschlussoptionen: `Continue` (gleiche Aufgabe, Detailkontext noch nützlich), `rewind` (falscher Lösungsweg, zu einem früheren Punkt zurück), `/compact` (gleicher Problemraum, Verlauf verdichten), `/clear` (neue Phase, bewusstes neues Briefing), Subagent (viel Zwischenoutput, nur Schlussfolgerung später gebraucht).
- Riskante Default-Reaktion ist `Continue`; die eigentliche Frage vor jedem Turn: „Welcher Kontext soll die nächste Antwort beeinflussen?“
- Neue Aufgabe → meistens neue Session, außer der Detailkontext ist noch relevant (z.B. direkt anschließende Doku zum gerade gebauten Feature).
- `rewind` ist oft besser als eine nachgeschobene Korrektur, weil eine Korrektur-Nachricht den Fehlversuch im Kontext belässt und der nächste Anlauf gegen alte Annahmen arbeitet.
- Schlechte Compacts entstehen oft, wenn Claude die künftige Richtung nicht vorhersehen kann (bes. in langen Debugging-Sessions) und automatische Compaction erst spät greift, wenn der Kontext schon unsauber ist — deshalb früh aktiv kompaktieren und vor `/compact` sagen, was erhalten bleiben muss.
- Subagents als Kontextgrenze: mentaler Test „Brauche ich später den Tool-Output oder nur die Schlussfolgerung?“

## Kernaussagen

- Fünfteilige Entscheidung nach jedem Arbeitsblock (Continue/rewind/compact/clear/Subagent) statt reflexhaftem Weiterreden im selben Thread → [[Kontext-Hygiene-Entscheidungsbaum]]
- Context Rot als Heuristik (300k-400k Tokens beim 1M-Modell) — mehr Kontext ist nicht automatisch besser → [[Kontext-Hygiene-Entscheidungsbaum]]
- `rewind` früh statt Korrektur nachschieben, weil Korrekturen den Fehlversuch im Kontext belassen → [[Kontext-Hygiene-Entscheidungsbaum]]
