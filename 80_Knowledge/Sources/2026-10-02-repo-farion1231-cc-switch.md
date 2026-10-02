---
url: https://github.com/farion1231/cc-switch
autor: farion1231
datum: 2026-10-02
erfasst: 2026-10-02
typ: repo
thema: Tools & Releases
zeitkritisch: ja
---

# cc-switch: Stack-Modus hängt Drittanbieter-Modelle an Claude Code und Codex

Im Klon von farion1231/cc-switch (Stand Commit `b9e96202`) beschreibt `src/i18n/locales/en.json` einen „Stack“-Modus: Du legst mehrere Anbieter an, und alle ihre Modelle erscheinen im Modellmenü von Claude Code (`/model`) und Codex. Die Einstellung heißt dort „Show the Stack mode switch on the main page“. Nur anhand der UI-Texte im Repo geprüft, nichts gestartet.

## Kernaussagen
- Pro Anbieter trägst du Modelle ein (Beispiel im Platzhalter: `deepseek-v4-pro`); das erste ist das Standardmodell des Anbieters und läuft beim Start und für Hintergrundaufgaben.
- Wählst du ein Modell im Menü, gehen Anfragen direkt an diesen Anbieter. Es gibt kein Failover; Stack-Modus und lokales Routing schließen sich aus.
- Nach Änderungen muss der Client neu gestartet werden; bei Codex (CLI-Daemon oder Desktop-App) braucht es einen vollständigen Neustart.
- Der Schalter muss in den Einstellungen von cc-switch aktiviert werden.

## Einordnung
Praktisch, wenn du günstigere oder lokale Modelle neben dem Hauptmodell im selben Client wählen willst. Die Hinweise zu Neustart und erneuter Modellauswahl zeigen, dass der Ablauf noch Reibung hat.

## Verbindungen
- [[Lokale-Modell-Umleitung-Muster]]
