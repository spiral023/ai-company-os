# Open-Source-LLMs & lokale Modelle

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-09. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Offene LLMs und Open-Weight-Modelle: verfügbare oder angekündigte Gewichte, lokale Inferenz und Serving, Hardwarebedarf, Quantisierung und Fine-Tuning. Eine Gewichtsankündigung ist kein Release; die Bezeichnung Open Source setzt eine gesonderte Prüfung der Lizenz und Offenheit voraus. Allgemeine Modellpreise und Benchmark-Kostenvergleiche stehen in modelle-kosten.

## Suchbegriffe

- **Hauptkeyword:** Open Source LLM
- **Long-Tail:** Open-Weight vs. Open Source; LLM lokal betreiben; Claude Code mit lokalem Modell; Ollama vs. llama.cpp; LLM Hardware und VRAM; GGUF Quantisierung; Offene LLMs fine-tunen; Mistral offene Gewichte
- **Fragen:** Welche LLM-Gewichte sind tatsächlich verfügbar? / Was unterscheidet Open Weight von Open Source? / Welche Hardware brauche ich für lokale Modelle? / Wann lohnt sich lokales Serving oder Fine-Tuning?
- **Häufig in den Quellen:** unsloth (3), claude code lokal (2), anthropic_base_url (2), lokale llms (2), terminal-bench (2), modell (2), modell-eskalation (2), token (2), clef head (2), lora fine-tuning (2), holdout accuracy (2), probability calibration (2), decision models (2), qwen3-coder, lokales llm, ollama, claude code kostenlos, qwen2.5-coder, config.toml provider, glm-4.7-flash

## Verwandte Themen

- [[Thema-Modelle-Kosten-Limits]] — Modelle, Kosten & Limits
- [[Thema-Kontext-Management]] — Kontext-Management
- [[Thema-Autonome-Läufe-Loops-CI]] — Autonome Läufe, Loops & CI
- [[Thema-Rolle-Lernen-Markt]] — Rolle, Lernen & Markt
- [[Thema-Verifikation-Tests-Review]] — Verifikation, Tests & Review

## Patterns (1)

- [[Decision-Head-Finetuning]] · meinung · 1 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Lokale-Modell-Umleitung-Muster]]

## Quellen (7)

- [[2026-10-07-unslothai-decision-model-finetuning]] — Unsloth erweitert den lokalen Betrieb von Decision-Modellen um eigenes Training: Ein LLM soll vorgegebene Optionen bewerten und Wahrscheinlichkeiten liefern, statt eine Antwort auszuformulieren.
- [[2026-09-28-unslothai-2104592692072304916]] — Unsloth kündigt am 28.09.2026 an, dass sich das Decision-Modell „Laya“ (laut Guide eine offene Jev-Alternative) lokal über Unsloth Desktop betreiben lässt, auf CPU, Mac, Windows, Linux und GPU.
- [[2026-08-16-floknowsai-in-einem-jahr-ersetzt-ein-lokales-modell-dein-claude-abo]] — Speicherbedarf und Tempo lokaler Modelle lassen sich mit einfachen Faustformeln aus Parametern, Quantisierung und Speicherbandbreite vorab abschätzen; Kontext und KV-Cache fehlen dabei.
- [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] — Offene Modelle liegen nur etwa einen Release-Zyklus hinter der Frontier, und Benchmark-Ergebnisse hängen stark vom Harness, nicht nur vom Modell ab.
- [[2026-04-22-alibaba-qwen-qwen3-6-27b-lokal-betreiben]] — Ein offenes 27B-Modell erreicht laut Herstellerchart im Agentic Coding etwa den Stand eines Vorjahres-Frontiermodells; lokaler Betrieb ist eine Speicher- und Bandbreitenfrage.
- [[2026-02-02-unsloth-team-claude-code-local-llm]] — Claude Code und Codex CLI laufen komplett lokal gegen einen llama.cpp-Server, wenn die Basis-URL oder der Provider auf den lokalen Endpunkt zeigt.
- [[2026-01-22-dr-cintas-claude-code-local]] — Über drei Umgebungsvariablen lässt sich Claude Code auf einen lokalen Ollama-Server umleiten, ohne die CLI selbst zu ändern.

## Quellen mit diesem Thema als Nebenthema

- [[2026-10-06-artificialanlys-2107467221421420919]]
