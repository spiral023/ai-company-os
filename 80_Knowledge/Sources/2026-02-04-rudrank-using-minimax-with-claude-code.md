---
url: https://x.com/rudrank/status/2018272804966449209
autor: "@rudrank"
datum: 2026-02-04
erfasst: 2026-07-13
typ: tweet
---

# @rudrank zu „Using MiniMax M2.1 with Claude Code“

## Inhalt

Zeigt dasselbe Umleitungs-Muster wie bei lokalen Modellen, diesmal für einen bezahlten Cloud-Provider (MiniMax M2.1) als günstigere Alternative zu Opus 4.5 bei Rate-Limit-Problemen. Claude Code liest Modell/Endpunkt aus Umgebungsvariablen (oder `~/.claude/settings.json`): `ANTHROPIC_BASE_URL`, `ANTHROPIC_API_KEY`/`ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_MODEL`. Wichtiger Praxishinweis: alle bestehenden Anthropic-Overrides löschen, bevor ein neuer Provider verbunden wird, sonst gehen Anfragen an den falschen Endpunkt. Nach dem Setzen der Variablen empfiehlt der Autor, sofort `/status` auszuführen und zu verifizieren, dass der Banner den neuen Endpunkt zeigt, bevor schwerere Tasks gestartet werden.

Für häufigen Modellwechsel wird **CC-MIRROR** genannt: erstellt isolierte Claude-Code-Instanzen pro Provider, sodass z.B. der Alias `minimax` MiniMax nutzt, während `claude` weiter mit Opus 4.5 läuft — dasselbe Muster funktioniert auch für Kimi K2.5 oder GLM 4.7.

## Kernaussagen

- Dasselbe Drei-Variablen-Umleitungsmuster (`ANTHROPIC_BASE_URL`/`API_KEY`/`MODEL`) funktioniert nicht nur für lokale Modelle, sondern für jeden Anthropic-kompatiblen Cloud-Provider — Claude Code bleibt die UI, das Modell dahinter wird austauschbar → [[Lokale-Modell-Umleitung-Muster]]
- Vor dem Wechsel alle bestehenden Provider-Overrides löschen und das Routing mit `/status` verifizieren, bevor schwerere Tasks laufen — sonst können Anfragen unbemerkt an den falschen Provider gehen → [[Lokale-Modell-Umleitung-Muster]]
- Werkzeuge wie CC-MIRROR erlauben mehrere isolierte Claude-Code-Instanzen mit unterschiedlichen Providern parallel (per Alias), statt ständig manuell umzuschalten → [[Lokale-Modell-Umleitung-Muster]]
