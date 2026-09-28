---
url: https://www.tiktok.com/@agentic.james/video/7666102633823882510
autor: "@agentic.james"
datum: 2026-07-24
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-07-24-agenticjames-the-creator-of-claude-code-released-a-guide-to-the-4-levels-of-ai-coding.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Vier Reifegrade der KI-Coding-Nutzung: vom Pair Programming zur Agentenflotte

Ein TikTok-Creator fasst in 94 Sekunden zusammen, was er als Leitfaden des Claude-Code-Erfinders zu vier Adoptionsstufen darstellt. Der Leitfaden selbst wird weder verlinkt noch zitiert; die Quelle ist eine Zweitdarstellung per automatischem Transkript und dient nebenbei der Werbung für eine Bezahl-Community. Belastbar ist höchstens das Stufenmodell als Denkraster, nicht die Zuschreibung.

## Die vier Stufen

- **Stufe 1:** Pair Programming. Du promptest kleine Änderungen in einer Session und prüfst jede Änderung selbst.
- **Stufe 2:** Auto Mode, sodass die meisten Permissions automatisch akzeptiert werden. Claude verifiziert selbst (End-to-End-Tests, Linting). Mehrere Sessions laufen parallel in getrennten Worktrees, gesteuert durch Skills wie automatisches Security- und Code-Review. Der Sprecher sieht hier den Punkt, den die meisten für das Maximum halten.
- **Stufe 3:** Eine zweite Schleife außerhalb der Coding-Schleife optimiert diese. Leitfrage: Welchen Kontext hätte ich zu Beginn mitgeben müssen, damit der Lauf autonomer und sauberer endet? Diese Iteration am Mechanismus soll das Vertrauen aufbauen, das für die nächste Stufe nötig ist.
- **Stufe 4:** Claude startet selbst automatisierte Coding-Sessions anderer Agenten. Hunderte oder tausende laufen parallel; du prüfst ganze Features statt einzelner Commits.

## Einordnung

Das Modell ist plausibel und deckt sich mit bekannten Bausteinen (Worktrees, Verifikationsschleifen, Kontextpflege), enthält aber keine Belege: keine Zahlen, keine Fehlerraten, keine Kosten. Verschwiegen werden insbesondere Token-Kosten und Rate Limits bei „Hunderten Agenten“, das Review-Risiko beim Wechsel von Commit- zu Feature-Review und die Frage, woran „genug Vertrauen“ gemessen wird. Die Stufen 2 und 3 sind die operativ nützlichen: Verifikation automatisieren, dann Fehlläufe systematisch in besseren Startkontext übersetzen. Stufe 4 bleibt Behauptung.

## Kernaussagen

- Parallele Sessions in getrennten Worktrees setzen automatische Verifikation und Review-Skills voraus → [[Kontrollierte-Agent-Parallelisierung]]
- Ohne Testharness und Linting im Loop trägt Auto Mode nicht → [[Testharness-als-staerkster-Hebel]]
- Eine Meta-Schleife fragt nach jedem Lauf, welcher Startkontext gefehlt hat → [[Kontext-Hygiene-Entscheidungsbaum]]

## Verbindungen

- [[Kontrollierte-Agent-Parallelisierung]]
- [[Testharness-als-staerkster-Hebel]]
- [[2026-04-22-agenticjames-everything-you-need-to-know-about-context-engineering-in-1-minute]]
- [[2026-01-31-bcherny-claude-code-team-tips]]
