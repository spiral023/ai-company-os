---
url: https://www.youtube.com/watch?v=djSbndoByr8
autor: Matt Pocock
datum: 2026-10-14
erfasst: 2026-10-22
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-10-14-matt-pocock-mutation-testing-is-awesome.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Mit absichtlichen Codefehlern die Aussagekraft von Tests untersuchen

Matt Pocock stellt am 14. Oktober 2026 Mutation Testing als Feedback für agentengeschriebene Tests vor. Statt nur erfolgreiche Testläufe zu betrachten, wird kontrolliert veränderter Quellcode erneut getestet. Die kurze Demonstration nennt Stryker.js für TypeScript, liefert aber keine gemessene Qualitätssteigerung.

## Kernaussagen

- Ein Mutationstool verändert den Quellcode gezielt, etwa durch Ersetzen eines Strings mit einem leeren String. Danach müssen die Tests einen verhaltensrelevanten Fehler erkennen. → [[Testharness-als-staerkster-Hebel]]
- Überlebende Mutanten liefern dem Agent konkrete Kandidaten für unzureichende Tests. Pocock erwartet daraus strengere Tests; das ist seine qualitative Einschätzung. → [[Mutationstests-fuer-Agent-geschriebene-Tests]]

## Einordnung

Als eigene Bewertung ist ein überlebender Mutant ein Untersuchungsauftrag: erst seine Verhaltensrelevanz prüfen, dann einen fachlichen Test ergänzen. Ein höherer Score allein ersetzt keine realistischen Anforderungen oder unabhängige Abnahme. Die deutsche automatisch erzeugte Spur kann Übersetzungs- und ASR-Fehler enthalten; Beschreibung und Transkript nennen übereinstimmend Stryker.js, ohne vollständige Hör- oder Bildprüfung.

## Verbindungen

- [[Hillclimbing-mit-Holdout-Split]]
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
