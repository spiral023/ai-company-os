---
url: https://x.com/0x_kaize/status/2038286026284667239
autor: "kaize (@0x_kaize)"
datum: 2026-03-29
erfasst: 2026-07-13
typ: tweet
---

# kaize (@0x_kaize) zu „Claude Usage Limits meistern: 10 Token-Strategien“ (Primärquelle)

## Inhalt

Primärquelle zum Thema, das bereits über eine Sekundärsynthese (vibe-repo-Wiki) im Knowledge-System erfasst war ([[2026-04-29-wiki-compiler-claude-usage-limits-token-strategien]]). Diese Notiz ergänzt konkrete Zahlen, die in der Sekundärzusammenfassung verlorengingen.

„Claude doesn't count messages. It counts tokens.“ Formel: `Gesamt = S × N(N+1) / 2` (S = Ø Tokens/Austausch, N = Nachrichtenzahl). Bei ~500 Tokens/Austausch: 5 Nachrichten = 7.500 Tokens (1×), 10 = 27.500 (3,7×), 20 = 105.000 (14×), 30 = 232.500 (**31×**). Ein Entwickler fand: bei langen Chats entfielen 98,5% aller Tokens auf das Wiedereinlesen des Verlaufs, nur 1,5% auf tatsächlichen Output.

Zehn Strategien (Kernpunkte, die über die Sekundärzusammenfassung hinausgehen): Prompt per Edit-Funktion korrigieren statt Korrektur-Nachricht zu senden (ersetzt statt stapelt den Austausch); Chat alle 15-20 Nachrichten per Zusammenfassung neu starten; Fragen bündeln statt aufteilen (auch Qualitätsgewinn, weil Claude den Gesamtzusammenhang sofort sieht); wiederkehrende Dateien in Claude Projects hochladen (Caching, keine erneute Tokenisierung); Memory/User Preferences für Setup-Wiederholungen nutzen; ungenutzte Features (Search, Connectors, Advanced Thinking) deaktivieren; Haiku für einfache Aufgaben spart laut Artikel 50-70% des Budgets gegenüber Sonnet/Opus für Routineaufgaben; rollendes 5-Stunden-Fenster statt Mitternachts-Reset (Arbeit über den Tag verteilen: Morgen/Mittag/Abend statt alles auf einmal); Peak-Hours seit 26.03.2026 (Mo-Fr 5-11 Uhr Pacific/8-14 Uhr Eastern) verbrauchen das Limit schneller bei gleicher Query; Extra-Usage/Overage als Sicherheitsnetz mit Ausgabenlimit.

## Kernaussagen

- Konkrete Zahlen zum quadratischen Tokenwachstum: Nachricht 30 kostet 31× mehr als Nachricht 1, bis zu 98,5% des Verbrauchs in langen Chats ist reines Wiedereinlesen des Verlaufs → [[Kontext-Hygiene-Entscheidungsbaum]]
- Haiku für Routineaufgaben (Grammatik, Formatierung, Entwürfe) spart 50-70% des Budgets gegenüber durchgängiger Nutzung von Sonnet/Opus → [[Kontext-Hygiene-Entscheidungsbaum]]
- Claude nutzt ein rollendes 5-Stunden-Fenster statt Mitternachts-Reset — wer das Limit in einer Morgensession verbraucht, verschenkt den Rest des Tages; zusätzlich verbrauchen Peak-Hours (Mo-Fr 5-11 Pacific) das Limit schneller bei gleicher Nutzung → [[Kontext-Hygiene-Entscheidungsbaum]]
