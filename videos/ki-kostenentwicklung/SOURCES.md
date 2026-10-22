# Quellen und redaktionelle Entscheidungen

Geprüft am 17.10.2026. Der Film erklärt Inferenzkosten für vergleichbare Leistung, keine Trainingsbudgets oder Abo-Preisliste.

## Hauptbeleg

- Repo: `80_Knowledge/Sources/2026-09-22-epoch-the-plunging-price-of-thought.md`
- Rohquelle: `00_Inbox/Quellen/URL/2026-09-22-epoch-the-plunging-price-of-thought.md`
- Original: [Epoch AI: The plunging price of thought](https://epoch.ai/publications/the-plunging-price-of-thought), Luke Emberson und David Roodman, 22.09.2026; live geprüft.
- Befund: Seit 2023 rund 47 % niedrigere Kosten pro Quartal für ein festes Benchmark-Leistungsniveau. Betrachtet wird die günstigste jeweils verfügbare Möglichkeit, das Niveau zu erreichen. Die Autoren betonen begrenzte Übertragbarkeit von Benchmarks, unvollständige Daten und unterschiedliche Rückgänge je Aufgabenbereich. Keine Prognose.

## Rechenbeispiel

Kostenindex zu Beginn = 100. Viermal Multiplikation mit 0,53: 100 → 53 → 28,09 → 14,8877 → 7,890481. Anzeige gerundet: 100 → 53 → 28 → 15 → 8. Dies ist eine illustrative Rechnung mit der mittleren Studienrate, keine gemessene Quartalsreihe. Keine konkreten Jahre an die Punkte schreiben.

## Praktische Einordnung aus dem Repo

- `80_Knowledge/Patterns/Modell-Eskalation-von-guenstig-nach-teuer.md`: Modell und Effort anhand eigener Aufgaben vergleichen, Kosten pro Aufgabe statt nur Tokenpreise.
- `blog/posts/2026-10-09-kosten-fertiges-feature-erfassen.md`: Kosten für fertige Ergebnisse erfassen.
- `80_Knowledge/Fakten/Modelle-und-Preise.md`: datierte Preise und Benchmarks nicht ungeprüft miteinander vergleichen.

Der praktische Schluss ist redaktionelle Einordnung. Keine garantierte Einsparung oder allgemeine Modellrangfolge.

## Gestaltung und Audio

RAITEC-CI aus `../raitec-ci/hyperframes/FRAME.md`, angewendet mit `apply.mjs`. Keine Avallon-Datei. Original-Logo unverändert, Titillium Web samt OFL lokal. Sprachwahl anhand `../Motion Tests/docs/sprachausgabe-stimmen.md`: George, ElevenLabs `eleven_multilingual_v2`, vorhandenes Free-Kontingent. Nutzer hat den Wechsel nach erschöpftem HeyGen-Kontingent ausdrücklich gewählt. Wortzeiten aus der tatsächlich erzeugten Sprachaufnahme; Ereignisse und Untertitel werden daran ausgerichtet.
