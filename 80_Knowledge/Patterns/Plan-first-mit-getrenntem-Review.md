# Plan-first-mit-getrenntem-Review

**Konfidenz:** verifiziert

## Zweck

Reduziert das Risiko, dass ein Agent zu früh implementiert, bevor Scope und Vorgehen geklärt sind, und dass derselbe Agent seine eigene Planung/Umsetzung unkritisch für gut hält (Single-Model-Blindheit). Adressiert damit einen anderen Fehlermodus als reines Nachfragen vor dem Start ([[Spec-Grilling]]): hier geht es um die Struktur der Ausführung selbst, nicht nur um die Klärung der Anforderung.

## Funktionsweise

Für mittelgroße bis große Änderungen gilt ein Fünf-Schritte-Ablauf: (1) **Discovery nur lesend** — relevante Dateien, Schnittstellen, Tests, Abhängigkeiten verstehen, ohne zu schreiben; (2) **Plan als persistentes Artefakt** (z.B. `plan.md`) statt nur im Chat formuliert — mit betroffenen Dateien, Risiken, offenen Fragen, Prüfschritten; (3) **Plan iterativ schärfen** — der Nutzer ergänzt Inline-Notizen, korrigiert Annahmen, grenzt Nicht-Ziele ein; (4) **Umsetzung gegen die Checkliste** im Plan, der zugleich als Fortschrittsprotokoll dient; (5) **Review getrennt von der Erstellung** — zweite Session, Subagent oder expliziter Review-Schritt mit anderem Fokus. Rollentrennung dagegen, dass derselbe Agent plant und implizit die eigene Planung für gut hält: **Builder** schreibt Plan/Code, **Reviewer** prüft Architektur/Edge-Cases/Sicherheit/Testlücken, **Verifier** validiert nur Nachweise und Regressionen. Bei hoher Tragweite eskaliert die Prüfung stufenweise: normale Selbstverifikation → zweite Session mit Review-Auftrag → separater Reviewer-Subagent → modellübergreifende Review-Schleife, bei der ein zweiter Agent den Plan so lange zurückweist, bis offene Punkte weg sind.

## Vorteile

- Ein explizites Plan-Dokument macht Annahmen sichtbar und annotierbar, statt sie implizit im Chatverlauf zu vergraben — neue Sessions oder Reviewer können an einem stabilen Zwischenstand ansetzen.
- Rollentrennung (Builder/Reviewer/Verifier) deckt blinde Flecken auf, die ein einzelner Agent in seiner eigenen Planung typischerweise nicht sieht.
- Die gestufte Eskalation passt den Prüfaufwand an die tatsächliche Tragweite an, statt für jede Änderung denselben (zu hohen oder zu niedrigen) Reviewaufwand zu betreiben.

## Nachteile & Grenzen

- Langsamer als sofortiges Tippen — lohnt sich laut Quelle aber, weil es schneller ist als eine Korrekturschleife nach einem schlechten Erstansatz.
- Erfordert Disziplin, den Plan tatsächlich als Artefakt zu pflegen statt doch wieder direkt in den Chat zu planen.
- Bei sehr kleinen, eindeutigen Änderungen ist der volle Fünf-Schritte-Ablauf unverhältnismäßiger Overhead.

## Wann einsetzen, wann nicht

- Einsetzen: mittelgroße bis große Änderungen, Architektur- oder sicherheitsrelevante Entscheidungen, alles mit spürbarer Tragweite bei Fehlern.
- Nicht einsetzen: triviale, eindeutig spezifizierte Einzeländerungen ohne nennenswertes Risiko.

## Belege

- 2026-04-17 · [[2026-04-17-wiki-compiler-praktische-claude-code-workflows]] · meinung — Wiki-Artikel (synthetisiert aus mehreren X-Posts u.a. @Meer_AIIT sowie offizieller Claude-Code-Doku) beschreibt den Fünf-Schritte-Ablauf und die Builder/Reviewer/Verifier-Rollentrennung.
- 2026-04-17 · [[2026-04-17-wiki-compiler-kontextsteuerung-verifikation-tdd]] · meinung — Teilweise überlappende, aber zusätzlich eigenständige Quelle (u.a. aihero.dev, tweag.github.io Agentic Coding Handbook) bestätigt die vierstufige Review-Eskalation und ergänzt, dass Kontextmenge/Prüfbarkeit/Arbeitspaketgröße gemeinsam über Qualität entscheiden.
- 2026-07-11 · [[2026-07-11-mattpocock-wayfinder-to-implementation]] · meinung — Für große Coding-Vorhaben empfiehlt Matt Pocock eine explizite Übergabe von Wayfinder über Spec und Tickets an einen AFK-Implementierungsagenten.
- 2026-07-13 · external_repos/mattpocock/skills/skills/engineering/implement/SKILL.md · verifiziert — `/implement` arbeitet gegen Spec oder Tickets und schließt mit `/code-review` ab.
- 2026-07-13 · external_repos/mattpocock/skills/skills/engineering/code-review/SKILL.md · verifiziert — Code Review trennt Standards- und Spec-Prüfung in zwei unabhängige Review-Achsen.
- 2026-02-20 · [[2026-02-20-aseem-shrey-claude-codex-plan-review]] · meinung — Unabhängige Primärquelle liefert ein konkretes technisches Muster für getrenntes Review: Cross-Model-Review (Codex prüft read-only Claudes Pläne) mit VERDICT-Protokoll und Rundenlimit, plus Vorher-Nachher-Beispiel (14 Probleme in 3 Runden behoben).
- 2026-07-03 · [[2026-07-03-trq212-fable-field-guide-unknowns]] · meinung — Ergänzt eine konkrete Priorisierungsregel für den Plan-Schritt: Implementierungspläne nach Änderungswahrscheinlichkeit sortieren (Datenmodelle/Interfaces zuerst), damit Review-Aufwand dort konzentriert wird, wo Fehlannahmen am teuersten sind.

## Spannungen & offene Fragen

- Beide ursprünglichen Quellen teilen sich mindestens eine Primärquelle (@Meer_AIIT), sind also nicht vollständig unabhängig; die neu ergänzten Quellen (Aseem Shrey, Thariq, Matt Pocock) sind davon unabhängig und beschreiben eigenständige, sich ergänzende Facetten derselben Grundidee.
- Offene Frage: Wie genau lässt sich die hier beschriebene Rollentrennung (Builder/Reviewer/Verifier) mit [[Kontrollierte-Agent-Parallelisierung]] kombinieren, wenn Builder und Reviewer parallel statt sequentiell arbeiten sollen?

## Verwandte Patterns

- [[Spec-Grilling]]
- [[TDD-als-Verifikationshebel]]
- [[Kontrollierte-Agent-Parallelisierung]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
