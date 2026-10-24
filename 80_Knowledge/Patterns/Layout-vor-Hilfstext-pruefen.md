# Layout vor Hilfstext prüfen

**Konfidenz:** meinung

## Zweck

Unnötige Nebenlabels, Slogans und Beschreibungen vermeiden, die eine unklare Oberfläche sprachlich überdecken. Erforderliche Hilfe und zugängliche Beschriftungen bleiben erhalten.

## Funktionsweise

Bei erklärendem Nebentext zuerst benennen, welche Unklarheit er behebt. Prüfen, ob Gruppierung, Reihenfolge, visuelle Hierarchie oder präzisere Hauptlabels diese Unklarheit direkt lösen. Eine Layoutvariante am gerenderten Bildschirm vergleichen, statt nur Text aus dem Code zu entfernen.

Fachlich notwendige Erklärungen, Fehlerhilfen, Auswirkungen wichtiger Aktionen und Informationen für assistive Technologien erhalten. Die Regel als gezielten Reviewcheck oder Agentenhinweis behandeln und ihre Wirksamkeit am konkreten Ergebnis prüfen. Die Quellen sind kein Auftrag, bestehende Agent-Dateien pauschal umzuschreiben.

## Vorteile

- Lenkt die Gestaltung auf nachvollziehbare Struktur statt zusätzliche Erklärungsschichten.
- Liefert einen konkreten Prüfanlass für generische Slogans und redundante Nebenlabels.

## Nachteile & Grenzen

- Die Quellen liefern Erfahrungsberichte und Prompt-Vorschläge, keinen kontrollierten Nutzertest.
- Weniger Text kann Verständlichkeit und Accessibility verschlechtern.
- Tooltips ersetzen nicht automatisch sichtbare Hilfe oder zugängliche Beschriftungen.

## Wann einsetzen, wann nicht

- Einsetzen: bei übererklärten Agent-Oberflächen und redundantem Text mit unklarem Informationswert.
- Nicht einsetzen: als pauschales Textverbot oder zur Verschleierung folgenreicher Entscheidungen.

## Belege

- 2026-10-22 · [[2026-10-22-luinlee-2113085361836744764]] · meinung — Zihua empfiehlt nach UI-Arbeit mit Opus und Astra, unnötige Nebenlabels und Beschreibungen durch verständlicheres Layout zu vermeiden. Die Regel bleibt ein Erfahrungsbericht und benötigt Ausnahmen für notwendige Erklärungen und Accessibility.
- 2026-10-22 · [[2026-10-22-voxyz_ai-2113254050170843418]] · meinung — Vox schlägt eine schärfere Regel gegen Slogans, Hilfstexte und Nebenlabels vor und verbindet sie mit UX, DX und AX; es fehlen Verfahren für Zielkonflikte und eine unabhängige Wirksamkeitsmessung.

## Spannungen & offene Fragen

- 2026-10-24: Die beiden Quellen teilen dieselbe Grundidee und zählen nicht als unabhängige empirische Bestätigung. Weniger Text und bessere Verständlichkeit können auseinanderfallen; das konkrete Layout muss diesen Trade-off entscheiden.

## Verwandte Patterns

- [[Visuelle-Abnahme-mit-Live-Lokal-Vergleich]]
- [[Variantenvergleich-vor-Produktionsabnahme]]
- [[AGENTS-md-Onboarding-Design]]
