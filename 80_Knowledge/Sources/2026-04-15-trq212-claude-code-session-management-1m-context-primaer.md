---
url: https://x.com/trq212/status/2044548257058328723
autor: "Thariq (@trq212, Anthropic)"
datum: 2026-04-15
erfasst: 2026-07-13
typ: tweet
---

# Thariq zu „Using Claude Code: Session Management & 1M Context“ (Primärquelle)

## Inhalt

Primärquelle zum Thema, das bereits über eine Sekundärsynthese (vibe-repo-Wiki) im Knowledge-System erfasst war ([[2026-04-29-wiki-compiler-claude-code-session-management-1m-context]]). Diese Notiz ergänzt die dort fehlenden Details aus dem vibedeck-Original (Autor Thariq direkt, nicht nur „X-Artikel von @trq212“ ohne Zuordnung).

Kernaussage: Ein 1M-Token-Context-Window ist kein pauschaler Qualitätsgewinn — es erlaubt längere autonome Arbeitsphasen, erhöht aber das Risiko von Context Pollution und Context Rot. Heuristik: ab ca. 300k-400k Tokens wird der Effekt beim 1M-Modell oft spürbar (keine harte Grenze). Fünf Anschlussoptionen nach jedem Turn: `Continue`, `rewind`, `/clear`, `/compact`, Subagents — `Continue` ist der riskante Default. Klare Regel: neue Aufgabe = meist neue Session, außer bei eng verwandten Folgeaufgaben (Beispiel: direkt nach Feature-Implementierung die zugehörige Doku schreiben — derselbe Kontext bleibt dann nützlich). `rewind` schlägt „try again“, weil man vor der Fehlabbiegung neu ansetzt statt Fehlversuche im aktiven Kontext zu behalten. `/compact` verdichtet verlustbehaftet (Claude entscheidet was wichtig war), `/clear` gibt volle Kontrolle über die neue Rahmung — schlechte Compacts entstehen oft gerade dann, wenn Claude die künftige Richtung nicht vorhersehen kann UND der Kontext beim automatischen Trigger bereits sehr voll ist (das Modell fasst also nicht in seinem besten Zustand zusammen); Konsequenz: aktiv und früh kompaktieren statt auf das automatische Compact zu warten. Subagents als Kontextgrenze: mentaler Test „Werde ich diesen Tool-Output später noch brauchen oder nur die Schlussfolgerung?“

## Kernaussagen

- Schlechte Compacts entstehen oft gerade dann, wenn der automatische Trigger erst bei bereits sehr vollem Kontext greift — das Modell fasst also nicht in seinem besten Zustand zusammen; Konsequenz: früh und aktiv kompaktieren statt automatisches Compact abzuwarten → [[Kontext-Hygiene-Entscheidungsbaum]]
- Konkretes Beispiel für eine sinnvolle Ausnahme von „neue Aufgabe = neue Session“: direkt nach einer Feature-Implementierung die zugehörige Dokumentation im selben Kontext schreiben, weil die gelesenen Dateien noch relevant sind → [[Kontext-Hygiene-Entscheidungsbaum]]
