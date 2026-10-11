# Prompt-Cache-TTL-nach-Agent-Pausen-waehlen

**Konfidenz:** meinung

## Zweck

Cache-Laufzeiten so wählen, dass erwartete Wiederverwendung nach Agent-Pausen den zusätzlichen Schreibaufwand rechtfertigt.

## Funktionsweise

Aufgaben danach unterscheiden, ob sie durchgehend laufen oder mitten im Ablauf länger pausieren. Vor einer TTL-Änderung den Abrechnungsweg, verfügbare Optionen, Version und wirksame Overrides prüfen. Eine längere Laufzeit nur für Aufgaben wählen, deren Kontext danach tatsächlich wiederverwendet wird. Anschließend Cache-Lese- und Schreibanteile sowie die akzeptierten Aufgabenergebnisse vergleichen. Kontextkompaktierung bleibt eine eigene Entscheidung.

## Vorteile

- Kann die erneute Verarbeitung desselben Kontextes nach einer Pause vermeiden.
- Behandelt wartende Test-Runner und kurze, durchgehende Aufgaben unterschiedlich.
- Macht wirksame Einstellung und behauptete Einsparung getrennt prüfbar.

## Nachteile & Grenzen

- Längere Cache-Laufzeit kann höhere Schreibkosten verursachen.
- Ein geänderter Prefix, Modellwechsel oder übersteuernde Einstellungen können den Vorteil verhindern.
- Die erste Quelle misst keine Einsparung; die beste TTL hängt von der eigenen Arbeitslast ab.

## Wann einsetzen, wann nicht

- Einsetzen: wiederaufgenommene Aufgaben mit längeren Test-, Build- oder menschlichen Pausen und belegbarer Kontextwiederverwendung.
- Nicht einsetzen: pauschal für jeden Agent; durchgehende kurze Aufgaben können nur zusätzliche Schreibkosten erzeugen.

## Belege

- 2026-10-10 · [[2026-10-10-voxyz_ai-2109056129884123370]] · meinung — Unterscheidet pausierende Subagents von durchgehenden Jobs und fordert Prüfung der TTL-Overrides; Konfiguration im Bild geprüft, konkrete Einsparung nicht gemessen.

## Spannungen & offene Fragen

- 2026-10-11: Längere Cache-Wärme kann Wiederverarbeitung reduzieren, ersetzt aber keine Kontexthygiene. Die verlinkte Herstellerdokumentation begrenzt zudem die Per-Agent-Option bei Usage Credits; der Post nennt diese Grenze nicht.

## Verwandte Patterns

- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Kontrollierte-Agent-Parallelisierung]]
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
