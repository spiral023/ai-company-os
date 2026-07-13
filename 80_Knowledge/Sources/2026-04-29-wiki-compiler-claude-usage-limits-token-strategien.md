---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-29
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Claude Usage Limits mit Token-Strategien steuern“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/02-agent-guides-und-templates/wka-claude-usage-limits-token-strategien-2026-04-29.md`), Zusammenfassung eines Threads von @0x_kaize (29.03.2026) über vibedeck.sp23.online.

Kernpunkte (kondensiert):

- Claude zählt Tokens, nicht Nachrichten. Gesamttokenverbrauch einer Konversation näherungsweise `S * N(N+1) / 2` (S = Tokens/Austausch, N = Anzahl Nachrichten) — der Verlauf wird bei jeder neuen Antwort komplett mitverarbeitet, daher wächst der Verbrauch quadratisch, nicht linear.
- Zehn Strategien u.a.: Prompt editieren statt Korrektur nachsenden; Chat nach 15-20 Nachrichten kritisch prüfen/neu starten mit Zusammenfassung; Fragen bündeln statt aufteilen; wiederkehrende Dateien in Claude Projects statt erneut hochladen; stabile Präferenzen in Memory/User Preferences statt in jeder Session wiederholen; nicht genutzte Features (Search, Connectors, Advanced Thinking) deaktivieren; Haiku für einfache Aufgaben, Sonnet für Standardarbeit, Opus für tiefes Reasoning; Arbeit über den Tag verteilen (rollendes 5-Stunden-Fenster statt Mitternachts-Reset); Peak-Hours beachten; Extra Usage nur als Sicherheitsnetz, nicht als Kapazitätsersatz.
- Für Claude Code: Fokus verschiebt sich von „mehr Prompts“ zu „bessere Arbeitsblöcke“ — kleine klar geschnittene Sessions, kompakte Status-Summaries bei Übergabe, gezielte Modellwahl je Task-Schwere.

## Kernaussagen

- Tokenverbrauch wächst quadratisch mit der Nachrichtenzahl einer Session — lange, unscharfe Chats werden unverhältnismäßig teuer → [[Kontext-Hygiene-Entscheidungsbaum]]
- Modellwahl nach Aufgabenschwere (Haiku für Routine, Opus für schwierige Entscheidungen) als eigenständiger Kostenhebel → [[Kontext-Hygiene-Entscheidungsbaum]]
