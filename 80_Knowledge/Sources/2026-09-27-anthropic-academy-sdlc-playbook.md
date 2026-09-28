---
url: https://academy.claude.com/de/courses/ai-native-sdlc-playbook
autor: Anthropic
datum: 2026-09-27
erfasst: 2026-09-27
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-09-27-anthropic-academy-sdlc-playbook.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Der SDLC als Schleife aus committeten Artefakten: Anthropics Playbook für große, regulierte Organisationen

Anthropic beschreibt in einem 14-lektionigen Academy-Kurs, wie ein Software Development Lifecycle aussieht, wenn Agenten den Großteil des Codes schreiben. Kernthese: Der Engpass wandert von der Build-Phase in Planung, Review/Test und Deployment; die alten Kontrollziele bleiben, aber die Durchsetzung wird automatisiert. Es ist ein Vorgehensleitfaden des Herstellers ohne eigene Messdaten, die Kennzahlen sind Vorschläge, keine Ergebnisse.

## Das committete Artefakt als Übergabe

Jede der sechs Phasen (Plan, Design, Build, Test, Deploy, Maintain) endet mit einem Artefakt in Git, das die nächste Phase liest: `intent.md` (Problem, gewünschtes Ergebnis, Einschränkungen, offene Fragen), `spec.md`, `plan.md`, Diff mit Tests, PR mit Review-Befunden, Vorfallsbericht. Die Commit-Kette ist zugleich der Audit-Trail. Die `intent.md` entsteht im Brainstorming mit Claude und wird vom Product Owner korrigiert; die `spec.md` erzeugt Claude mit den als Skills kodierten Marken-, Security- und Compliance-Regeln, der Product Owner prüft sie nur. Plan-Modus liefert danach die `plan.md`; Auto-Modus ist erst nach ausgereiften Leitplanken (CLAUDE.md, Skills, Hooks, Testsuite) Standard für Routinearbeit. Für Legacy-Artefakte (Jira, Figma) soll pro Artefakt ein System als Source of Truth benannt werden.

## Welche Ebene was durchsetzt

- CLAUDE.md: unter einer Seite, im Root eingecheckt; dieselbe Korrektur zweimal nötig heißt Eintrag in die Datei.
- Skills: nur für konsistent anzuwendendes institutionelles Wissen; sie sind beratend. Was immer gelten muss, braucht zusätzlich einen Hook oder Review-Durchgang.
- Hooks: deterministisch, in Build-Phase schnell und dateibezogen (Formatter, Schutz von Pfaden, Testdatei-Sperre bei Bugfixes), in Deploy-Phase als Genehmigungsgate (Exit-Code 2 mit Begründung). Nicht verhandelbare Hooks gehören in verwaltete Einstellungen, ergänzt um Sandbox, Deny-Regeln, Managed-MCP-Allowlist und Mindestversion.
- Feedback-Schleife: Verifikation in ein Ziel mit Exit-Code (`make test`) verpacken; bei Bugs erst fehlschlagenden Test committen, dann Claude ohne Teständerung lösen lassen. Der Verifizierer-Subagent prüft am Ende mit frischem Kontext.

## Skalierung und Betrieb

Parallel: zwei bis drei Sessions als Start, je eigener Worktree, Obergrenze ist die Review-Kapazität der Person. Evals: 20 bis 50 reale Aufgaben mit Abnahmeprüfung, in CI bei Änderung von CLAUDE.md, Skills oder Hooks und nach Zeitplan, als Merge-Check; jeder Produktionsvorfall wird ein neues Eval. Review: `REVIEW.md` definiert Durchläufe und was „Wichtig“ heißt, Nits sind gedeckelt; der schreibende Agent darf nicht selbst genehmigen, Code-Owner-Freigabe bleibt. CI/CD: erst read-only (Build-Triage, Changelog), dann Schreibschritte nur als PR; Autonomie nach Umgebung gestaffelt, Produktion bereitet der Agent vor, ein Mensch autorisiert per Hook; Rollback wird regelmäßig geprobt.

Den Kreis schließt Lektion 13: ein deterministisches Erkennungsskript ohne Modell überwacht eine Metrik mit rollierender Baseline. Bei 1σ wird nur geloggt, bei 2σ diagnostiziert Claude read-only, bei 3σ darf er einen PR oder ein vorab genehmigtes Runbook auslösen; das Ergebnis wird wieder eine `intent.md`.

## Einordnung

Belastbar ist die Struktur: Sie bündelt bekannte Muster (Spec, Plan-Modus, Hooks, Skills, Evals, getrenntes Review) zu einem durchgängigen Ablauf mit klarer Trennung zwischen beratender und erzwingender Ebene. Zahlen zur Wirkung fehlen vollständig; die Früh- und Spätindikatoren sind ungeprüfte Vorschläge. Neu gegenüber dem Bestand sind die Rückkopplung aus der Produktion in die nächste `intent.md` und die σ-gestufte Agent-Autonomie. Kosten sind kaum benannt: Pflege von Skills, Evals und Hooks, Review-Last bei mehr Output und Token-Verbrauch der Eval-Läufe. Zugeschnitten auf große Unternehmen; für kleine Teams ist das Gesamtpaket überdimensioniert, einzelne Bausteine übertragen sich. Teile (Claude Design, verwalteter Code-Review, Claude Tag) sind laut Quelle Beta oder Research Preview.

## Kernaussagen
- Jede Phase endet mit einem committeten Artefakt, das die nächste auslöst; die Commit-Kette ist der Audit-Trail → [[Intent-Engineering-als-dritte-Schicht]]
- Ein Skill ist nur für konsistent anzuwendendes Wissen sinnvoll und bleibt beratend; Pflichtregeln brauchen einen Hook → [[Skill-Schwellenwert-institutionelles-Wissen]]
- Hooks für deterministische Prüfungen und Freigabe-Gates, nicht verhandelbare zentral verwaltet → [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]
- Der Autor-Agent genehmigt nicht selbst; Befunde blockieren nicht, Code-Owner-Freigabe bleibt → [[CI-Agent-mit-Review-Gate]]
- Bugfix per Test zuerst, Verifikation als Exit-Code-Ziel → [[Testharness-als-staerkster-Hebel]]
- Plan im Plan-Modus als eigener Schritt vor der Umsetzung → [[Plan-first-mit-getrenntem-Review]]

## Verbindungen
- [[Intent-Engineering-als-dritte-Schicht]]
- [[Spec-Ordner-pro-Feature]]
- [[Kontrollierte-Agent-Parallelisierung]]
- [[2026-02-01-anthropic-docs-claude-code-gitlab-ci]]
- [[2026-09-17-anthropic-how-claude-code-is-used-in-practice]]
