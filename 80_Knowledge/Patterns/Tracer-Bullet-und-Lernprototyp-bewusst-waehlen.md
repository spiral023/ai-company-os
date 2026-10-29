# Tracer-Bullet-und-Lernprototyp-bewusst-waehlen

**Konfidenz:** meinung

## Zweck

Verhindern, dass ein begrenzter Lernversuch wegen seiner überzeugenden Darstellung stillschweigend als weiterverwendbare Produktbasis behandelt wird.

## Funktionsweise

Vor Beginn Lernfrage, Qualitätsumfang und spätere Codeverwendung benennen. Ein Lernprototyp nach Hunt und Thomas beantwortet eine konkrete Unsicherheit und darf dafür Vollständigkeit, Robustheit oder Stil auslassen. Sein Ergebnis ist die Erkenntnis; der Versuchscode wird verworfen. Ein Tracer Bullet führt dagegen einen schmalen realen Weg durch den technischen Gesamtpfad aus und enthält bereits angemessene Struktur, Fehlerbehandlung und Prüfungen. Er bleibt als erweiterbares Gerüst bestehen.

Osmani lässt beim Wechsel aus dem schnellen Prototypmodus sowohl Neubau anhand der Erkenntnisse als auch schrittweises Refactoring zu. Deshalb muss das Team festlegen, welchen Begriff es benutzt und welche Qualitätslücken vor einer Übernahme geschlossen sein müssen. Mockdaten, Stubs und simulierte Wirkungen gehören ausdrücklich in den Übergabestand.

**Übertragung auf Agents:** Den ersten Auftrag auf eine überprüfbare Unsicherheit begrenzen. Sichtbare Funktionsbreite ist kein Reifegrad; die Abnahme prüft den vereinbarten Lern- oder Integrationszweck. Aus dem Prototypbegriff entsteht keine Freigabe für reale externe Wirkungen.

## Vorteile

- Macht Erwartungen vor dem ersten Demo sichtbar.
- Prüft riskante Integration früh mit einem kleinen realen Ablauf.
- Erlaubt schnelle Lernversuche ohne falsche Produktreifezusagen.

## Nachteile & Grenzen

- Wiederverwendung von Versuchscode kann im Einzelfall sinnvoll sein, braucht aber eine bewusste Qualitätsentscheidung.
- Ein Tracer Bullet ist trotz geringer Funktionsbreite kein vollständig fertiges Produkt.
- Ein vorführbarer Versuch kann fachliche und betriebliche Lücken verdecken.

## Wann einsetzen, wann nicht

- Einsetzen: neue Produkte, UI-Demos, unklare Integrationen und Übergaben von schnellen Buildern an lokale Entwicklung.
- Nicht einsetzen: um jede kleine reversible Änderung mit einer zusätzlichen Prozessphase zu belasten.

## Belege

- 2019-09-13 · [[2019-09-13-pdf-the-pragmatic-programmer-20th-anniversary-edition]] · meinung — PDF-S. 109–123 unterscheiden weiterverwendbare Tracer Bullets mit Qualitätsstruktur von bewusst verworfenen Lernprototypen.
- 2025-08-18 · [[2025-08-18-pdf-beyond-vibe-coding]] · meinung — PDF-S. 129–133 erlauben Neubau oder schrittweise Härtung und verlangen, Attrappen sowie fehlende Produktteile beim Übergang sichtbar zu machen; die Begriffsgrenze unterscheidet sich von Pragmatic.

## Spannungen & offene Fragen

- 2026-10-29: Die Bücher stimmen in der notwendigen Reifeentscheidung überein, behandeln den weiterverwendbaren Prototypcode aber verschieden. Die Abweichung bleibt erhalten; es wird keine einheitliche Wegwerfpflicht aus beiden Quellen behauptet.
- Ein allgemeiner Prozentwert für den Abstand zwischen Demo und Produkt lässt sich daraus nicht ableiten.

## Verwandte Patterns

- [[Lovable-Prototyp-dann-lokaler-Handoff]]
- [[Produktreife-durch-echte-Testnutzer]]
- [[TDD-als-Verifikationshebel]]
- [[Qualitaetsaufwand-nach-Folgen-und-Abhaengigkeiten-staffeln]]
