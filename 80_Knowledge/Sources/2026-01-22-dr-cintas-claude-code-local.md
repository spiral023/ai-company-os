---
url: https://x.com/dr_cintas/status/2014380662300533180
autor: "Alvaro Cintas (@dr_cintas)"
datum: 2026-01-22
erfasst: 2026-07-13
typ: tweet
---

# Alvaro Cintas zu „Claude Code lokal ausführen (Kostenlos & Privat)“

## Inhalt

Tutorial, wie Claude Code komplett lokal mit Ollama betrieben wird, ohne Cloud/Kosten. Kernschritt (Schritt 3, „der wichtigste Schritt“): Claude Code über Umgebungsvariablen umleiten, statt mit Anthropic direkt mit einem lokalen Ollama-Server zu sprechen:

```bash
export ANTHROPIC_BASE_URL="http://localhost:11434"
export ANTHROPIC_AUTH_TOKEN="ollama"
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
```

Danach Start mit `claude --model qwen2.5-coder:7b`. Claude Code selbst bleibt unverändert (liest Dateien, editiert Code, führt Terminalbefehle aus) — nur das Ziel der Anfragen wechselt. Empfohlene Modelle: `qwen3-coder:30b` (High Performance) oder `gemma:2b`/`qwen2.5-coder:7b` (weniger RAM).

## Kernaussagen

- Claude Code lässt sich über drei Umgebungsvariablen (`ANTHROPIC_BASE_URL`, Auth-Token, Modellname) komplett von Anthropic weg auf einen lokalen Ollama-Server umleiten — die CLI selbst bleibt identisch, nur das Backend-Modell wechselt → [[Lokale-Modell-Umleitung-Muster]]
