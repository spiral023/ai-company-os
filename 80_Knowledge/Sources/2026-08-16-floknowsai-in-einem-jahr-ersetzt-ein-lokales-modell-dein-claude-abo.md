---
url: https://www.tiktok.com/@floknowsai/video/7674510846168419606
autor: "@floknowsai"
datum: 2026-08-16
erfasst: 2026-08-29
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-08-16-floknowsai-in-einem-jahr-ersetzt-ein-lokales-modell-dein-claude-abo.md
thema: KI-Kosten
zeitkritisch: nein
---

# Rechenregeln für lokale Modelle: Speicherbedarf und Tempo abschätzen

Lehrvideo (Transkript, Caption mit Rechenbeispielen). Die Prognose im Titel, ein lokales Modell ersetze in einem Jahr das Claude-Abo, ist eine unbelegte Behauptung; die Faustregeln sind dagegen nachvollziehbar.

## Kernaussagen
- Speicher: Parameter mal Bits je Gewicht geteilt durch acht; 8B in Q4 sind rund 4,5 GB. Bei Mixture of Experts zählt der Speicher für alle Parameter (Qwen3-30B-A3B braucht Platz für 30,5 Mrd.), „aktiv“ heißt gerechnet, nicht geladen. → [[Lokale-Modell-Umleitung-Muster]]
- Tempo: Speicherbandbreite geteilt durch Modellgröße, dann halbiert; 8B in Q4 bei 400 GB/s ergibt rund 44 Token pro Sekunde. Läuft das Modell nicht komplett im VRAM, wird es deutlich langsamer.
- Für sich ändernde Dokumente ist Fine-Tuning/LoRA falsch, ein RAG-Index bleibt aktuell.

## Einordnung
Grobe Faustformeln (Rechenbeispiel, keine Messung); Kontext-Länge und KV-Cache-Speicher fehlen in der Rechnung. Nützlich zur Vorabprüfung der Hardware.

## Verbindungen
- [[Lokale-Modell-Umleitung-Muster]]
- [[2026-04-22-alibaba-qwen-qwen3-6-27b-lokal-betreiben]]
- [[2026-02-02-unsloth-team-claude-code-local-llm]]
