# One-File-per-Failure-Mode

**Konfidenz:** verifiziert

## Zweck

Strukturiert eine Skill-Bibliothek entlang konkret benannter, wiederkehrender Fehlermodi der Agentenarbeit, statt einen einzigen großen Allzweck-Skill zu bauen. Jeder Fehlermodus bekommt eine eigene, fokussierte Lösung.

## Funktionsweise

Statt eines monolithischen Prompts wird für jeden typischen Fehlermodus des Agenten — z.B. „Agent hat das Falsche gebaut“, „Agent ist zu weitschweifig“, „Code funktioniert nicht“, „Codebasis verkommt“ — genau ein passender, schmal geschnittener Skill (oder eine kleine Gruppe verwandter Skills) angelegt. Beispiele aus dem Referenz-Repo: `tdd` (Fehlermodus „Code funktioniert nicht“), `grill-me`/`grill-with-docs` (Fehlermodus „Agent hat das Falsche gebaut“), `improve-codebase-architecture` (Fehlermodus „Ball of Mud“; empfohlene Ausführung alle paar Tage).

## Vorteile

- Jeder Skill bleibt klein und fokussiert — leichter zu lesen, zu debuggen, einzeln zu ersetzen oder wiederzuverwenden.
- Klare Zuordnung von benanntem Problem zu Lösung erleichtert das Auffinden des richtigen Skills.
- Neue Fehlermodi lassen sich inkrementell durch neue, einzelne Dateien abdecken, ohne bestehende Skills aufzublähen.

## Nachteile & Grenzen

- Risiko von Überlappung/Duplikation, wenn sich Fehlermodi nicht sauber trennen lassen.
- Erfordert laufende Kuratierung, damit die Sammlung nicht unübersichtlich wächst, je mehr Fehlermodi identifiziert werden.
- Die Formulierung „one file per failure mode“ ist eine Zuspitzung/Synthese des Tweet-Autors, keine wörtliche Aussage aus dem Repo (siehe Spannungen).

## Wann einsetzen, wann nicht

- Einsetzen: Skill-/Prompt-Bibliotheken, die über Zeit gepflegt und erweitert werden sollen.
- Nicht einsetzen: Wegwerf-Prompts für einmalige Aufgaben.

## Belege

- 2026-07-10 · [[2026-07-10-voxyz-mattpocock-skills]] · meinung — Tweet: „/grill-me ... /tdd ... /improve-codebase-architecture treats codebase rot ... one file per failure mode.“
- 2026-07-11 · external_repos/mattpocock/skills/README.md · verifiziert — Abschnitt „Why These Skills Exist“ öffnet wörtlich mit „I built these skills as a way to fix common failure modes I see with Claude Code, Codex, and other coding agents“ und listet vier nummerierte Fehlermodi (#1 Agent tut nicht, was gewünscht; #2 Agent zu weitschweifig; #3 Code funktioniert nicht; #4 Ball of Mud), jeweils einem oder wenigen konkret benannten Skills zugeordnet (`grill-me`/`grill-with-docs`, `CONTEXT.md`, `tdd`/`diagnosing-bugs`, `improve-codebase-architecture`). Die Formulierung „every few days“ für `improve-codebase-architecture` ist ebenfalls wörtlich bestätigt.

## Spannungen & offene Fragen

- Die exakte Formulierung „one file per failure mode“ ist keine wörtliche Repo-Aussage, sondern eine Zuspitzung des Tweet-Autors der im README dokumentierten Struktur (nummerierte Fehlermodi → benannte Skills). Die inhaltliche Struktur ist verifiziert, der genaue Wortlaut nicht.

## Verwandte Patterns

- [[Spec-Grilling]]
- [[Klein-und-komposierbar]]
