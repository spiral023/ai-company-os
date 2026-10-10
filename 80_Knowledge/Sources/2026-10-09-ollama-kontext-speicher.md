---
url: https://docs.ollama.com/context-length
autor: Ollama
datum: 2026-10-09
erfasst: 2026-10-09
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-10-09-docs-ollama-kontextlaenge-und-speicherbedarf.md
zeitkritisch: ja
---

# Ollama: Kontextlänge braucht zusätzlichen Speicher

Undatierte Dokumentation, gesichtet am 09.10.2026. Der HTML-Ingest ließ Fließtext aus; das Archiv enthält zusätzlich den Originaltext der offiziellen Markdown-Fassung unter `https://docs.ollama.com/context-length.md`. Keine konkrete Ollama-Version wird auf der Seite genannt; die Angaben sind ein datierter Dokumentationsstand.

## Speicher und Konfiguration

Die Dokumentation beschreibt Kontext als die vom Modell nutzbare Tokenmenge. Eine größere konfigurierte Kontextlänge erhöht den Speicherbedarf. Die Seite nennt VRAM-abhängige Voreinstellungen von 4k, 32k und 256k und empfiehlt für Coding- und Agent-Aufgaben mindestens 64000 Tokens. Diese Empfehlung ist kein allgemein tragfähiger Hardware-Mindestwert.

`OLLAMA_CONTEXT_LENGTH` setzt die Kontextlänge beim Start des Servers. `ollama ps` zeigt unter anderem die aktuelle Zuordnung zu CPU/GPU und die konfigurierte Kontextgröße. Ollama empfiehlt für Leistung, CPU-Offloading zu vermeiden. Die Dokumentation enthält keine Messung des Speicherverbrauchs einer konkreten Coding-Aufgabe.

## Einordnung

Modellgewichte allein sind kein vollständiges Speicherbudget. Die grobe Gewichtsrechnung aus der älteren Videoquelle dient nur einer Vorabschätzung; Laufzeitreserven und Kontext müssen praktisch geprüft werden. Kein universelles Tempo- oder Abo-Ersatzversprechen.

## Kernaussagen

- Speicherplanung für lokale Modelle um Kontext und tatsächliche CPU/GPU-Zuordnung ergänzen → [[Lokale-Modell-Umleitung-Muster]].

## Verbindungen

- [[2026-08-16-floknowsai-in-einem-jahr-ersetzt-ein-lokales-modell-dein-claude-abo]]
