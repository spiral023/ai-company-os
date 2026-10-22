# Open-Source-LLMs & lokale Modelle

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-22. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Offene LLMs und Open-Weight-Modelle: verfügbare oder angekündigte Gewichte, lokale Inferenz und Serving, Hardwarebedarf, Quantisierung und Fine-Tuning. Eine Gewichtsankündigung ist kein Release; die Bezeichnung Open Source setzt eine gesonderte Prüfung der Lizenz und Offenheit voraus. Allgemeine Modellpreise und Benchmark-Kostenvergleiche stehen in modelle-kosten.

## Suchbegriffe

- **Hauptkeyword:** Open Source LLM
- **Long-Tail:** Open-Weight vs. Open Source; LLM lokal betreiben; Claude Code mit lokalem Modell; Ollama vs. llama.cpp; LLM Hardware und VRAM; GGUF Quantisierung; Offene LLMs fine-tunen; Mistral offene Gewichte
- **Fragen:** Welche LLM-Gewichte sind tatsächlich verfügbar? / Was unterscheidet Open Weight von Open Source? / Welche Hardware brauche ich für lokale Modelle? / Wann lohnt sich lokales Serving oder Fine-Tuning?
- **Häufig in den Quellen:** unsloth (3), terminal-bench (3), benchmark (3), quantisierung (3), vram (3), lokale inferenz (3), anthropic_base_url (2), claude code lokal (2), ollama (2), lokale llms (2), open weights (2), kimi k3 (2), deepseek (2), hardware-pilot (2), arbeitslast (2), speicherbedarf (2), token (2), modell-eskalation (2), modell (2), holdout accuracy (2)

## Verwandte Themen

- [[Thema-Modelle-Kosten-Limits]] — Modelle, Kosten & Limits
- [[Thema-Kontext-Management]] — Kontext-Management
- [[Thema-Autonome-Läufe-Loops-CI]] — Autonome Läufe, Loops & CI
- [[Thema-Rolle-Lernen-Markt]] — Rolle, Lernen & Markt
- [[Thema-Verifikation-Tests-Review]] — Verifikation, Tests & Review

## Patterns (2)

- [[Decision-Head-Finetuning]] · meinung · 1 Belege
- [[Lokale-Inferenz-nach-Arbeitslast-dimensionieren]] · meinung · 1 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Lokale-Modell-Umleitung-Muster]]

## Quellen (12)

- [[2026-10-19-unslothai-2112212605930778830]] — Unsloth beschreibt am 19.10.2026 die lokale Ausführung von `DeepSeek V4.1-Flash-1017` mit Dynamic GGUFs.
- [[2026-10-09-ollama-kontext-speicher]] — Größerer Kontext erhöht den Speicherbedarf; die CPU/GPU-Zuordnung muss am tatsächlichen Lauf geprüft werden.
- [[2026-10-07-unslothai-decision-model-finetuning]] — Unsloth erweitert den lokalen Betrieb von Decision-Modellen um eigenes Training: Ein LLM soll vorgegebene Optionen bewerten und Wahrscheinlichkeiten liefern, statt eine Antwort auszuformulieren.
- [[2026-09-28-unslothai-2104592692072304916]] — Unsloth kündigt am 28.09.2026 an, dass sich das Decision-Modell „Laya“ (laut Guide eine offene Jev-Alternative) lokal über Unsloth Desktop betreiben lässt, auf CPU, Mac, Windows, Linux und GPU.
- [[2026-09-01-ai-mit-arnie-lokale-ki-kauf-nicht-die-falsche-hardware]] — Lokale Inferenz wird nach Qualitätsziel, Modell, Kontext und Parallelität dimensioniert; historische Preise und unklare Formeln sind keine aktuelle Kaufgrundlage.
- [[2026-08-16-floknowsai-in-einem-jahr-ersetzt-ein-lokales-modell-dein-claude-abo]] — Speicherbedarf und Tempo lokaler Modelle lassen sich mit einfachen Faustformeln aus Parametern, Quantisierung und Speicherbandbreite vorab abschätzen; Kontext und KV-Cache fehlen dabei.
- [[2026-07-31-unslothai-2083231049434435596]] — Unsloth kündigt am 31.
- [[2026-07-28-pdf-state-of-open-source-ai-v1-0-1]] — Offene Modelle liegen nur etwa einen Release-Zyklus hinter der Frontier, und Benchmark-Ergebnisse hängen stark vom Harness, nicht nur vom Modell ab.
- [[2026-07-27-anthropic-our-position-on-open-weights-models]] — Dario Amodei erläutert am 27.
- [[2026-04-22-alibaba-qwen-qwen3-6-27b-lokal-betreiben]] — Ein offenes 27B-Modell erreicht laut Herstellerchart im Agentic Coding etwa den Stand eines Vorjahres-Frontiermodells; lokaler Betrieb ist eine Speicher- und Bandbreitenfrage.
- [[2026-02-02-unsloth-team-claude-code-local-llm]] — Claude Code und Codex CLI laufen komplett lokal gegen einen llama.cpp-Server, wenn die Basis-URL oder der Provider auf den lokalen Endpunkt zeigt.
- [[2026-01-22-dr-cintas-claude-code-local]] — Über drei Umgebungsvariablen lässt sich Claude Code auf einen lokalen Ollama-Server umleiten, ohne die CLI selbst zu ändern.

## Quellen mit diesem Thema als Nebenthema

- [[2026-10-19-artificialanlys-2112218661432000694]]
- [[2026-10-17-kimmonismus-2111385805449048181]]
- [[2026-10-13-artificialanlys-2110081938140582085]]
- [[2026-10-06-artificialanlys-2107467221421420919]]
- [[2026-07-16-kimmonismus-2077828228282982886]]
