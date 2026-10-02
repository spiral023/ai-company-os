---
url: https://claude.dev/blog/building-with-claude-sonnet-5-5/
autor: Addy Osmani
datum: 2026-09-28
erfasst: 2026-10-02
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-09-28-claude-building-with-claude-sonnet-5-5-claude-dev-blog.md
thema: Neue Modelle
zeitkritisch: ja
---

# Sonnet 5.5 einsetzen: Effort neu kalibrieren, Workarounds streichen, echten Check verlangen

Der Herstellerleitfaden zu `claude-sonnet-5-5` (Stand 2026-09-28) behauptet: gleicher Token-Preis wie Sonnet 5, aber deutlich weniger Tokens pro Aufgabe, daher „bis zu 30 % weniger“ Kosten. Das ist eine Herstellerangabe ohne eigene Messreihe im Text. Für Dich übertragbar ist vor allem die Arbeitsweise beim Modellwechsel, weniger die Migrationsliste.

## Arbeitsweisen beim Modellwechsel
- **Effort-Sweep neu fahren:** Die Stufen sind neu kalibriert, ein alter Wert trägt nicht. Startwerte laut Leitfaden: `medium` für gut spezifizierte agentische Aufgaben und Chat mit Latenzdruck (dort auch `low`), `high` für schwerere oder längere Aufgaben, `xhigh`/`max` nur, wenn Deine Evals einen Qualitätsgewinn zeigen. Die API startet bei `high`, Claude Code bei `medium`.
- **Weniger Thinking über Effort steuern:** Eine Bitte im System-Prompt, weniger zu denken, wirkt laut Quelle nicht zuverlässig.
- **Workarounds entfernen:** Refusal-Steering, Retry-Shims für Tool-Calls und „do not be lazy“ raus, dann Evals neu fahren, bevor Du anderes tunst.
- **Echter Check vor „fertig“:** Bei `low` überspringt das Modell gelegentlich einen Check, der die Änderung wirklich ausführt. Der Leitfaden empfiehlt einen System-Prompt-Absatz: Tests, Type-Checker, Build oder der geänderte Befehl müssen laufen. Ein reiner Syntax-Check zählt nicht, fehlende Abhängigkeiten werden mit dem projekteigenen Paketmanager installiert, und nur wenn kein echter Check möglich ist, muss das Modell sagen, welcher fehlt.
- **Reasoning nicht in die Antwort schreiben lassen:** Das löst `reasoning_extraction`-Ablehnungen aus. Stattdessen `thinking.display` (`summarized` oder `updates`, beta) lesen.
- **Modellwahl:** Sonnet bei klarer Spezifikation und prüfbarem Ergebnis, Opus für lange, urteilsintensive Arbeit.

## Zuordnung Workload und Startmodell
Die Tabelle fehlt im archivierten Text. Sie stammt aus einem Bild, das Vox am 29.09. aus diesem Leitfaden zeigt (Herkunft: Vox-Bild, nicht der archivierte Text). Mit Sonnet 5.5 starten: gut abgegrenztes Alltags-Coding (Bugs, schnelles Iterieren, Prüfen gegen Anforderungen), High-Volume-Entwicklung, polierte Dokumente, Folien und Tabellen, wiederholt laufende, klar definierte Agent-Aufgaben (Untersuchung, Review, Entwurf). Mit Opus 5.5 starten: komplexe Arbeit mit sorgfältigem Urteil, darunter lange agentische Coding- und Wissensarbeit, sowie die schwersten Probleme.

## Preise und Parameter (Herstellerangabe, Stand 2026-09-28)
Alle Preise inkl. Batch und Prompt Caching entsprechen Sonnet 5. US-only-Inference (`inference_geo: "us"`) kostet das 1,1-Fache. Das Bild-Tier (bis 2576 px lange Kante) macht ein 2000×1500-Bild etwa 2,5-mal so teuer wie bei Sonnet 4.6/4.5 oder Haiku 4.5, also vorher herunterskalieren. Die Mindestgröße fürs Caching sinkt auf 512 Tokens, ein Cache-Read kostet ein Zehntel des Input-Preises; ein Wechsel des Top-Level-Effort invalidiert den Cache, per-message Effort (beta) nicht. Für agentisches Coding `max_tokens` 128.000 mit Streaming, weil Thinking mitzählt.

## Migrationsbrüche (Kurzfassung)
`thinking: disabled` und erzwungenes `tool_choice` (`any`/`tool`) liefern 400; Ersatz sind `between_tools` (nur `low` bis `high`) bzw. `auto` plus `strict`-Tools. Computer Use läuft nur über `computer_toolset_20260801`. Als Advisor akzeptiert ein Sonnet-5.5-Executor Opus 5.5, Opus 5 und Sonnet 5.5, die Antwort kommt verschlüsselt zurück. Text zwischen Tool-Calls steckt in Thinking-Blöcken, lies Blöcke nach Typ. In Claude Code löst der Alias `sonnet` ab v2.1.284 auf Sonnet 5.5 auf (`medium`, 1M Kontext, kein Fast Mode, Thinking nicht abschaltbar); Standardmodell bleibt Opus 5.5.

![Letztes Bild der Animation: Foto einer Skyline im Sonnenuntergang neben drei Gemälden, die Sonnet 5, Sonnet 5.5 und Opus 5.5 per selbst geschriebenem Python-Code gemalt haben](../../00_Inbox/Quellen/URL/medien/2026-09-28-claude-building-with-claude-sonnet-5-5-claude-dev-blog/01-bild.jpg)

## Einordnung
Die Kosten-Aussage ist Marketing mit plausiblem Mechanismus: Preis pro Token gleich, Verbrauch angeblich geringer. Artificial Analysis misst am selben Tag bei `max` deutlich mehr Output-Tokens und Kosten pro Task als bei Sonnet 5 (siehe [[2026-09-28-artificialanlys-2104640155843989864]]); andere Effort-Stufe und Methode, daher Spannung, kein Widerspruch. Die Mal-Demo ist ein Einzelvergleich ohne Metrik. Die Arbeitsweisen (Sweep, Workarounds streichen, Check-Pflicht) sind bekannt und modellunabhängig. Kosten: Jeder Wechsel erfordert Evals, sonst ist der Sweep nur Bauchgefühl.

## Kernaussagen
- Nach jedem Modellwechsel den Effort-Sweep neu fahren; `xhigh`/`max` nur mit gemessenem Gewinn → [[Modell-Eskalation-von-guenstig-nach-teuer]]
- Ein System-Prompt-Absatz erzwingt einen echten Check vor „fertig“ → [[Testharness-als-staerkster-Hebel]]
- Advisor-Paarungen sind modellabhängig und liefern verschlüsselte Antworten → [[Advisor-Agent-gegen-Drift]]

## Verbindungen
- [[2026-09-22-claude-getting-the-most-out-of-opus-5-5-in-claude-and-c]]
- [[2026-07-08-claudedevs-modell-vs-effort]]
- [[2026-09-28-artificialanlys-2104640155843989864]]
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
