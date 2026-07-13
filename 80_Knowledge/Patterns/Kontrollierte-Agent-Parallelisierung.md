# Kontrollierte-Agent-Parallelisierung

**Konfidenz:** meinung

## Zweck

Verhindert, dass parallele Agent-Nutzung (mehrere Subagents, Agent Teams oder mehrere Coding Agents gleichzeitig) mehr Tokenverbrauch, Koordinationsaufwand und Edit-Kollisionen erzeugt, als sie an Durchsatz gewinnt. Adressiert die Versuchung, Parallelisierung als generellen Geschwindigkeitshebel statt als gezielte Eskalation für echte Parallelität einzusetzen.

## Funktionsweise

Parallelisierung lohnt sich nur unter drei Voraussetzungen: (1) **klare Modulgrenzen** — unabhängige Flächen im Projekt, sonst steigen Edit-Kollisionen und Tokenverbrauch; (2) **kurzer gemeinsamer Laufzeitkontext** — alle Teilnehmer laden denselben Grundkontext, ein überladenes `CLAUDE.md` skaliert bei mehreren Agenten besonders schlecht; (3) **klare Verifikationssignale** — Teilnehmer müssen ihre eigenen Ergebnisse selbst validieren können. Das mentale Modell bei Agent Teams: ein Lead zerlegt die Arbeit, mehrere Teammates bearbeiten Teilaufgaben, Koordination läuft über Struktur statt freie Konversation. Praktische Regel für die Aufteilung: nach Modulen oder Dateien parallelisieren, niemals über gemeinsam editierte Kernartefakte. Geeignete Muster: Writer/Reviewer in getrennten Worktrees, unabhängige Modulpakete für größere Refactorings, Recherche/Testvorbereitung/Dokumentation in isolierten Subsessions. Bei zwei parallel arbeitenden Coding Agents (z.B. Codex + Claude Code): ein Hauptagent arbeitet am Code, der andere übernimmt Review, zweite Meinung oder ein klar getrenntes Teilpaket — nicht beide gleichzeitig an denselben Dateien. Sinnvolle Eskalationsreihenfolge: erst normaler Hauptthread, dann spezialisierte Subagents, erst bei echter, sauber abgrenzbarer Parallelität Agent Teams oder mehrere Agenten gleichzeitig.

## Vorteile

- Verhindert den häufigsten Parallelisierungsfehler: mehrere Agenten bearbeiten versehentlich dieselben Dateien oder dieselbe Entscheidungsebene gleichzeitig.
- Die Drei-Voraussetzungen-Prüfung (Modulgrenzen, kurzer Kontext, Verifikationssignale) liefert eine konkrete Vorab-Checkliste, bevor überhaupt parallelisiert wird.
- Klare Rollentrennung (ein Hauptagent, der andere Review/getrenntes Paket) macht Doppelnutzung mehrerer Coding Agents nachvollziehbar statt chaotisch.

## Nachteile & Grenzen

- Höherer Tokenverbrauch, langsamere Gesamtkoordination und mehr Setup-/Kontrollaufwand sind auch bei korrekter Anwendung inhärente Kosten von Parallelisierung.
- Ohne saubere Modulgrenzen im Projekt selbst lässt sich die Voraussetzung gar nicht erfüllen — das Pattern setzt eine bestimmte Codebasis-Struktur voraus.
- Weniger sinnvoll bei kleinen Einzeländerungen, stark gekoppelten Dateien oder Aufgaben, die ohnehin nur sequentiell lösbar sind — dort erzeugt Parallelisierung nur Overhead.

## Wann einsetzen, wann nicht

- Einsetzen: tiefes Debugging mit konkurrierenden Hypothesen, größere Refactorings über getrennte Modulflächen, Architekturuntersuchungen aus mehreren Blickwinkeln, langlaufende Analyseaufgaben mit klar trennbaren Teilfragen.
- Nicht einsetzen: kleine Einzeländerungen, stark gekoppelte Dateien, Aufgaben ohne erfüllbare Modulgrenzen-Voraussetzung.

## Belege

- 2026-04-17 · [[2026-04-17-wiki-compiler-agent-teams-in-claude-code]] · meinung — Wiki-Artikel (Quelle: zwei unabhängige X-Posts, @dani_avila7 und @jasonzhou1993) beschreibt die drei Voraussetzungen und die Eskalationsreihenfolge Hauptthread → Subagents → Agent Teams.
- 2026-04-17 · [[2026-04-17-wiki-compiler-praktische-claude-code-workflows]] · meinung — Unabhängige Zweitquelle bestätigt die Regel „nach Modulen/Dateien parallelisieren, nicht über gemeinsam editierte Kernartefakte“.
- 2026-04-17 · [[2026-04-17-wiki-compiler-codex-claude-code-lovable-workflow]] · meinung — Ergänzt die Praxisregel für zwei parallel eingesetzte Coding Agents (ein Hauptagent, der andere Review/getrenntes Paket).

## Spannungen & offene Fragen

- Die drei Quellen überschneiden sich teilweise in ihren zugrunde liegenden X-Posts (u.a. @dani_avila7 taucht in mehreren vibe-repo-Artikeln auf), sind aber inhaltlich eigenständig und ergänzen sich, statt sich zu widersprechen.
- Offene Frage: Wie lässt sich die Drei-Voraussetzungen-Prüfung praktisch vor jedem Parallelisierungsversuch operationalisieren (z.B. als Checkliste in einem Skill), statt sie nur als Prinzip im Kopf zu behalten?

## Verwandte Patterns

- [[Erweiterungs-Ebenen-Zuordnung]]
- [[Plan-first-mit-getrenntem-Review]]
- [[Klein-und-komposierbar]]
