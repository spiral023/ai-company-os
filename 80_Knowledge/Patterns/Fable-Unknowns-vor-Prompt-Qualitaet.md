# Fable-Unknowns-vor-Prompt-Qualitaet

**Konfidenz:** meinung

## Zweck

Verschiebt den Engpass agentischer Arbeit von „Wie schreibe ich einen besseren Prompt?“ zu „Was weiß ich, das ich nicht aufgeschrieben habe — und was weiß ich nicht, das ich wissen müsste?“. Adressiert, dass stärkere Modelle das Unknowns-Problem verschärfen statt lösen: sie lösen Ambiguität selbstbewusst auf und tragen eine falsche Annahme konsistent durch eine ganze Multi-File-Session, statt (wie schwächere Modelle) laut und lokal zu scheitern.

## Funktionsweise

Prompts/Skills/Kontext sind nur eine Karte der Arbeit; die echte Codebasis mit ihrer Geschichte und den undokumentierten Constraints im Kopf des Entwicklers ist das Territorium — die Differenz sind die Unknowns. Vier-Quadranten-Modell: Known Knowns (explizit im Prompt), Known Unknowns (bekannte Lücken), Unknown Knowns (so offensichtlich, dass man es nie aufschreiben würde), Unknown Unknowns (woran man nicht mal gedacht hat) — die gefährlichsten sind die unteren beiden. Konkrete Techniken entlang der Zeitachse: **vor der Arbeit** — Blind Spot Pass (offen sagen, was man selbst nicht versteht, das Modell kartiert Standards/Risiken/Fragen), Brainstorms/Prototypen (bei Design-Entscheidungen mehrere bewusst unterschiedliche Wegwerf-Prototypen statt einer Prosa-Beschreibung — Reagieren ist leichter als Spezifizieren), Interviews (das Modell befragt den Nutzer eine Frage nach der anderen, priorisiert nach architektonischer Tragweite, mit dokumentiertem Decision Record — dreht die übliche Prompt-Richtung um), References statt Beschreibungen (Quellcode/Referenz-Library benennen statt schwer beschreibbares Verhalten in Prosa zu spezifizieren), Implementation Plans nach Änderungswahrscheinlichkeit sortiert (Datenmodelle/Interfaces zuerst, mechanisches Refactoring ans Ende — konzentriert Review dort, wo Unknowns am teuersten sind); **während der Arbeit** — Implementation Notes (laufendes Protokoll über Entscheidungen, Abweichungen, unerwartete Funde); **nach der Arbeit** — Pitches/Explainer (Spezifikation+Prototyp+Notes zu einem Dokument mit Demo statt rohem Diff) und der **Change Quiz**: vor dem Merge lässt man sich vom Modell ein Quiz über die eigenen Änderungen stellen — wer es nicht besteht, hat die Änderung nicht verstanden und sollte nicht mergen (Verifikation für den Menschen, nicht für das Modell).

## Vorteile

- Macht implizites Wissen und blinde Flecken systematisch adressierbar statt dem Zufall überlassen zu bleiben.
- Der Change Quiz ist eine konkrete, einfach einsetzbare Verifikationsschranke gegen unreflektiertes Mergen von KI-generierten Änderungen.
- Implementierungspläne nach Änderungswahrscheinlichkeit zu sortieren, konzentriert begrenzten Review-Aufwand genau dort, wo Fehlannahmen am teuersten sind.

## Nachteile & Grenzen

- Der volle Technik-Katalog (Blind Spot Pass, Interview, Prototypen, Notes, Pitch, Quiz) ist aufwendig und lohnt sich nicht für triviale Änderungen.
- Die Methodik hängt an der Bereitschaft, vor dem eigentlichen Coden Zeit in Klärung zu investieren — bei Zeitdruck wird genau dieser Schritt oft übersprungen.
- Für Domänen, in denen der Nutzer selbst Laie ist (wie im Praxisbeispiel des Autors demonstriert), funktioniert die Methodik gut; bei sehr technischen Spezialaufgaben ist unklar, wie gut das Modell die richtigen Interview-Fragen stellt.

## Wann einsetzen, wann nicht

- Einsetzen: nichttriviale Vorhaben mit unklarer oder unvollständiger Spezifikation, besonders wenn der Nutzer selbst Wissenslücken in der Zieldomäne hat oder das Modell über mehrere Dateien hinweg konsistent falsch abbiegen könnte.
- Nicht einsetzen: triviale, eindeutig spezifizierte Änderungen ohne nennenswertes Risiko einer Fehlannahme.

## Belege

- 2026-07-03 · [[2026-07-03-trq212-fable-field-guide-unknowns]] · meinung — X-Artikel von Thariq Shihipar (Anthropic) beschreibt das Vier-Quadranten-Modell, alle acht Techniken und ein konkretes Praxisbeispiel (Videoschnitt als Laiendomäne).
- 2026-02-01 · [[2026-02-01-aiedge-claude-code-starter-pack]] · meinung — Gegenbeispiel: Ein beworbener „bester Claude Code Prompt“ ist ein reiner Persona-/Vision-Priming-Prompt („Craftsman“, „Reality Distortion Field“, `ultrathink`), der nichts fragt, keine Erfolgskriterien benennt und keine Unknowns adressiert — steht in direktem Gegensatz zur Kernthese dieses Patterns und stachelt das Modell eher zu mehr Selbstüberzeugung an, statt Ambiguität offenzulegen. Die Quelle liefert keinen Vorher-Nachher-Vergleich für die Superlativ-Behauptung.
- 2026-09-04 · [[2026-09-04-julian-ivanov-ki-automat-so-nutzt-du-claude-code-nach-anthropics-neuen-re]] · meinung — Prompt mit Grund, Ziel, Referenzdateien und messbarem Abschlusskriterium statt Rollenfloskeln und Verbotslisten; gibt die Fable-5-Doku nur sinngemäß wieder. Einschränkung: Ergebnisse nur an einem Newsletter-Beispiel gezeigt.
- 2026-07-03 · [[2026-07-03-trq212-2073100352921215386]] · meinung — Volltext-Fassung des Artikels mit allen Techniken (Blind Spot Pass, Brainstorm/Prototyp, Interview, References, Plan, Implementation Notes, Pitch, Quiz) und Rückkopplungs-Zeitleiste. Selbstberichtet, ohne Messwerte.

## Spannungen & offene Fragen

- Einzige bisherige Quelle ist ein einzelner Artikel, wenn auch von einem Anthropic-Mitarbeiter mit hoher Reichweite (laut Quelle >3,6 Mio. Views).
- Ergänzung 2026-02-01: Ein unabhängiges Gegenbeispiel (aiedge Starter Pack) zeigt einen verbreiteten Prompt-Stil, der der Kernthese dieses Patterns direkt widerspricht — stützt indirekt die Kernthese, weil genau die Art Prompt, vor der das Pattern warnt, in der Praxis unbelegt als „bester Prompt“ beworben wird.
- Offene Frage: Wie genau lässt sich der „Change Quiz“ praktisch operationalisieren (automatisiert vom Modell generiert, oder manuell vom Reviewer gestellt)?

## Verwandte Patterns

- [[Plan-first-mit-getrenntem-Review]]
- [[Spec-Grilling]]
- [[Ralph-Loop-Frischer-Kontext-pro-Iteration]]
