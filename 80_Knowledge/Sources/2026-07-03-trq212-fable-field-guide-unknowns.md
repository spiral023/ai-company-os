---
url: https://x.com/trq212/status/2073100352921215386
autor: "Thariq Shihipar (@trq212, Anthropic)"
datum: 2026-07-03
erfasst: 2026-07-13
typ: tweet
---

# Thariq Shihipar zu „A Field Guide to Fable: Finding Your Unknowns“

## Inhalt

Zentrale These: „The map is not the territory.“ Prompts/Skills/Kontext sind nur eine Karte der Arbeit; die echte Codebasis mit ihrer Geschichte und den undokumentierten Constraints im Kopf des Entwicklers ist das Territorium. Die Differenz sind die Unknowns — trifft das Modell auf eines, muss es raten. Bei stärkeren Modellen (Fable 5) wird das Problem schlimmer statt besser, weil ein starkes Modell Ambiguität selbstbewusst aufzulöst und eine falsche Annahme konsistent durch eine ganze Multi-File-Session trägt (schwächere Modelle scheitern dagegen laut und lokal). Der Engpass verschiebt sich von „Kann das Modell die Aufgabe?“ zu „Habe ich die Aufgabe richtig spezifiziert?“

Vier-Quadranten-Modell (Rumsfeld-Schema): Known Knowns (explizit im Prompt), Known Unknowns (bekannte Lücken), Unknown Knowns (so offensichtlich, dass man es nie aufschreiben würde), Unknown Unknowns (woran man nicht mal gedacht hat). Die gefährlichsten sind die unteren beiden.

Konkrete Techniken entlang der Zeitachse:
- **Blind Spot Pass** (vor der Arbeit): dem Modell offen sagen, was man selbst nicht versteht — es kartiert dann Standards, historische Probleme, unbekannte Fragen.
- **Brainstorms/Prototypen**: bei Design-Entscheidungen mehrere bewusst unterschiedliche Wegwerf-Prototypen bauen lassen statt eine Entscheidung in Prosa zu beschreiben — Reagieren ist leichter als Spezifizieren.
- **Interviews**: das Modell befragt den Nutzer eine Frage nach der anderen, priorisiert nach architektonischer Tragweite, mit dokumentiertem Decision Record am Ende — dreht die übliche Prompt-Richtung um.
- **References statt Beschreibungen**: bei schwer beschreibbarem Verhalten Quellcode/eine Referenz-Library benennen statt es in Prosa zu spezifizieren.
- **Implementation Plans nach Änderungswahrscheinlichkeit sortiert**: Datenmodelle/Interfaces (die am ehesten kippen) nach vorne, mechanisches Refactoring ans Ende — konzentriert Review dort, wo Unknowns am teuersten sind.
- **Implementation Notes** (während der Arbeit): laufendes Protokoll über Entscheidungen, Abweichungen vom Plan, unerwartete Funde.
- **Pitches/Explainer** (nach der Arbeit): Spezifikation+Prototyp+Notes zu einem Dokument mit Demo konsolidieren statt rohem Diff.
- **Change Quiz**: vor dem Merge lässt man sich vom Modell ein Quiz über die eigenen Änderungen stellen — wer es nicht besteht, hat die Änderung nicht verstanden und sollte nicht mergen. Verifikation für den Menschen, nicht für das Modell.

## Kernaussagen

- Stärkere Modelle verschärfen das Unknowns-Problem, statt es zu lösen: sie lösen Ambiguität selbstbewusst auf und tragen falsche Annahmen konsistent durch die ganze Session, statt laut zu scheitern → [[Fable-Unknowns-vor-Prompt-Qualitaet]]
- Vier-Quadranten-Modell (Known/Unknown × Knowns/Unknowns) macht implizites Wissen und blinde Flecken systematisch adressierbar statt zufällig zu bleiben → [[Fable-Unknowns-vor-Prompt-Qualitaet]]
- Implementierungspläne nach Änderungswahrscheinlichkeit sortieren (Datenmodelle/Interfaces zuerst) konzentriert Review-Aufwand dort, wo Fehlannahmen am teuersten sind → [[Fable-Unknowns-vor-Prompt-Qualitaet]], [[Plan-first-mit-getrenntem-Review]]
- Der „Change Quiz“ vor dem Merge ist Verifikation für den Menschen (nicht das Modell): Wer die eigene Änderung nicht im Quiz erklären kann, hat sie nicht verstanden und sollte nicht mergen → [[Fable-Unknowns-vor-Prompt-Qualitaet]]
