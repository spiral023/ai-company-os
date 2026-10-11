---
url: https://www.youtube.com/watch?v=MN9dGgmLyso
autor: "Matt Pocock"
datum: 2026-10-02
erfasst: 2026-10-11
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-10-02-matt-pocock-live-poteto-creator-of-pstack-on-shipping-1-000.md
thema: Arbeitsweisen
zeitkritisch: ja
---

# Poteto: Verifikation und gebündelte Befunde vor mehr Agentenautonomie

Lauren Tan beschreibt im Gespräch vom 2. Oktober 2026 ihre pstack-Arbeitsweise. Vertrauen entsteht durch prüfbare Ausführung und verbesserte Arbeitsumgebungen; PR-Mengen bleiben Selbstauskunft.

## Kernaussagen

- Agents Anwendungen ausführen, Traces und Screenshots erfassen lassen; deterministische Prüfabläufe in wiederverwendbare CLIs verlagern: [[Testharness-als-staerkster-Hebel]].
- Nutzerberichte und wiederkehrende Codeprobleme zunächst sammeln und zusammen betrachten, bevor einzelne Reparaturen gestartet werden: [[Task-basierte-Steuerung]].
- Automatisch zusammengeführte Änderungen nachträglich stichprobenartig prüfen und wiederkehrende Fehler in Skills, Lint-Regeln oder Codekonventionen zurückführen: [[Review-Autonomie-mit-Shadow-Mode-und-Stichproben]].

## Einordnung

Der beschriebene Ablauf berichtet automatische Merges, aber keinen vorausgehenden Shadow-Mode oder unabhängigen Qualitätsnachweis. Viele PRs betreffen Codepflege; ihr Umfang belegt keine entsprechende Menge ausgelieferter Features. Für irreversible oder schwer überprüfbare Änderungen bleibt die Autonomiefrage im Gespräch offen.

## Verbindungen

- [[Testharness-als-staerkster-Hebel]] liefert Rückmeldung statt bloßer Erfolgsmeldungen.
- [[Review-Autonomie-mit-Shadow-Mode-und-Stichproben]] ergänzt die im Gespräch unvollständig beschriebene Freigabelogik.
