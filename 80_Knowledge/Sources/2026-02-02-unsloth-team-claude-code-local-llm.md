---
url: https://unsloth.ai/docs/basics/claude-codex
autor: "Unsloth Team"
datum: 2026-02-02
erfasst: 2026-08-05
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-02-unsloth-team-claude-code-local-llm.md
beleg_art: sekundaerquelle
---

# Claude Code und OpenAI Codex vollständig lokal: Unsloth-Anleitung mit llama.cpp

Unsloth zeigt Schritt für Schritt, wie sich Claude Code und OpenAI Codex CLI komplett ohne Cloud-Anbindung betreiben lassen: ein lokal gebautes `llama.cpp` serviert ein quantisiertes Open-Modell, beide CLIs werden per Umgebungsvariable bzw. Konfigurationsdatei auf den lokalen Server statt auf die Anbieter-API umgeleitet. Als Beispielmodell dient GLM-4.7-Flash, ein 30B-MoE-Modell, das Unsloth als „stark für Agentic Coding“ einordnet, in der Quantisierung `UD-Q4_K_XL` (Unsloth Dynamic GGUF) als „beste Balance aus Größe und Genauigkeit“ für eine 24-GB-GPU wie eine RTX 4090.

## Aufbau: llama.cpp, Modell, Server

`llama.cpp` wird aus dem Quellcode mit CUDA-Unterstützung gebaut (`cmake -DGGML_CUDA=ON`, `-DGGML_CUDA=OFF` ohne NVIDIA-GPU). Das Modell wird über `huggingface_hub.snapshot_download` mit dem Filter `UD-Q4_K_XL` geladen. Der Server startet mit einer für Agentic Workflows abgestimmten Parameterkombination: `--ctx-size 131072` (128k-Kontextfenster), `--flash-attn on`, `--kv-unified`, `--cache-type-k q8_0 --cache-type-v q8_0`, `--temp 1.0 --top-p 0.95 --min-p 0.01`, `--jinja` für Chat-Templates.

## Umleitung: dieselbe Anthropic-Variable, ein anderer Serving-Stack

Claude Code wird identisch zum bereits belegten Muster umgeleitet: `ANTHROPIC_BASE_URL="http://localhost:8001"` und ein Dummy-`ANTHROPIC_API_KEY="sk-no-key-required"`, danach `claude --model unsloth/GLM-4.7-Flash`. Das ist eine dritte, unabhängige Bestätigung von [[Lokale-Modell-Umleitung-Muster]] — nach Ollama und einem bezahlten Cloud-Provider (MiniMax) nun mit einem selbst gehosteten `llama.cpp`-Server als drittem Serving-Backend hinter derselben Drei-Variablen-Schnittstelle.

Codex CLI folgt einem anderen Mechanismus: Statt Umgebungsvariablen liegt die Provider-Definition in `~/.codex/config.toml` unter `[model_providers.llama_cpp]` mit `base_url`, `wire_api = "responses"` und einem `stream_idle_timeout_ms`. Gestartet wird mit `codex --model ... -c model_provider=llama_cpp`. Das ist funktional dasselbe Ziel (lokales Modell statt Cloud-API), aber ein strukturell anderer Konfigurationsweg (Datei statt Env-Vars) — die Quelle bestätigt damit nicht direkt das für Claude Code beschriebene Muster, sondern zeigt eine Codex-spezifische Parallele dazu. Die Anleitung warnt zusätzlich explizit vor `--dangerously-bypass-approvals-and-sandbox`: Codex führt Code damit ohne jede Bestätigung aus, nur in vertrauenswürdigen Umgebungen zu verwenden.

## Einordnung

Die konkreten Werte (Modellname, Quant-Stufe, Serverflags, Portnummern) sind Konfigurationsstand zum Erfassungsdatum und plattform-/hardwareabhängig (24-GB-GPU-Annahme) — sie sollten nicht als zeitlose Empfehlung zitiert werden, sondern als ein funktionierendes Beispiel-Setup. Die Einordnung „stark für Agentic Coding“ für GLM-4.7-Flash ist eine unbelegte Herstellerangabe (Unsloth vertreibt selbst die GGUF-Quantisierung), keine unabhängige Benchmark-Messung. Der eigentliche Wert dieser Quelle liegt in der dritten unabhängigen Bestätigung des Umleitungsmusters und in der Beobachtung, dass Codex CLI denselben Zweck über einen strukturell anderen Konfigurationsweg löst als Claude Code.

## Kernaussagen

- `ANTHROPIC_BASE_URL`/`ANTHROPIC_API_KEY` funktioniert unverändert gegen einen selbst gehosteten `llama.cpp`-Server als drittes, unabhängiges Serving-Backend → [[Lokale-Modell-Umleitung-Muster]]
- OpenAI Codex CLI löst dieselbe Umleitung strukturell anders: Provider-Definition in `~/.codex/config.toml` statt Umgebungsvariablen — kein Beleg für das Claude-Code-Pattern, sondern eine eigenständige Parallele
- `--dangerously-bypass-approvals-and-sandbox` in Codex hebt Bestätigungen und Sandbox vollständig auf — nur in vertrauenswürdigen Umgebungen vertretbar → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]

## Verbindungen

- [[Lokale-Modell-Umleitung-Muster]]
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
