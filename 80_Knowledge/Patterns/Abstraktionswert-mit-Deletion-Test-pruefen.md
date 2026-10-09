# Abstraktionswert-mit-Deletion-Test-pruefen

**Konfidenz:** verifiziert

## Zweck

Den Nutzen eines Moduls anhand der gebündelten Komplexität und der Anforderungen seiner Aufrufer beurteilen.

## Funktionsweise

Das Entfernen eines Moduls gedanklich durchspielen: Verschwindet Komplexität, ist es möglicherweise eine entbehrliche Durchreichung. Taucht dieselbe Komplexität bei vielen Aufrufern wieder auf, bündelt das Modul wertvolles Verhalten. Deep Modules sollen viel Verhalten hinter einer kleinen, klaren Schnittstelle anbieten. Entfernungskandidaten anschließend auf Verträge, Seiteneffekte, Abhängigkeiten und Tests prüfen, bevor tatsächlich geändert wird.

## Vorteile

- Unterscheidet nützliche Bündelung von zusätzlichem Verwaltungsaufwand.
- Lenkt die Bewertung auf Schnittstellenwissen, Wartung und Testbarkeit.

## Nachteile & Grenzen

- Der Test verlangt Kenntnisse der Aufrufer und fachlichen Verträge.
- Tokenersparnis und Produktivität sind im Post nicht gemessen.
- Die Verifikation bestätigt die dokumentierte Methode im Autorenrepo; es wurde kein Modul entfernt oder Benchmark ausgeführt.

## Wann einsetzen, wann nicht

- Einsetzen: Durchreichungen, Wrapper und geplante gemeinsame Abstraktionen.
- Nicht einsetzen: als automatische Löschregel oder als bloße Zählung von Dateien und Codezeilen.

## Belege

- 2026-10-01 · [[2026-10-01-mattpocockuk-2105563604384915639]] · meinung — Pocock schlägt /codebase-design für Shallow Modules und Deletion-Test-Kandidaten vor; sein späteres Plädoyer für tokeneffiziente Abstraktionen beschreibt keine Messung, und der Test autorisiert keine Löschung.
- 2026-10-09 · external_repos/mattpocock/skills/skills/engineering/codebase-design/SKILL.md · verifiziert — Checkout 4588b32 beschreibt Deep Modules über Verhalten hinter kleiner Schnittstelle und den Deletion Test über verschwindende oder bei Aufrufern wiederkehrende Komplexität; bestätigt die dokumentierte Methode, keine ausgeführte Entfernung oder Tokenersparnis.

## Spannungen & offene Fragen

- Der Autorenpost kritisiert unnötige Abstraktionen und verteidigt sie später als tokeneffizient. Entscheidend bleibt, welche Komplexität eine konkrete Schnittstelle bündelt.

## Verwandte Patterns

- [[Helper-Nutzung-durch-Lint-erzwingen]]
- [[Fachregel-Konsolidierung-vor-Featureaenderung]]
- [[Klein-und-komposierbar]]
