---
url: https://academy.claude.com/de/courses/ai-native-sdlc-playbook
titel: "Das KI-native SDLC-Playbook"
autor: "Anthropic"
datum: 2026-09-27
erfasst: 2026-09-27
typ: artikel
quelle: url
status: verarbeitet
verarbeitet_am: 2026-09-29
source_notiz: 80_Knowledge/Sources/2026-09-27-anthropic-academy-sdlc-playbook.md
lektionen: 14
---

# Das KI-native SDLC-Playbook

> Automatisch per Playwright erfasst (die Academy-Seiten sind eine JS-App ohne serverseitig gerenderten Inhalt, `python ai.py ingest` findet dort keinen Text). Quelle: [https://academy.claude.com/de/courses/ai-native-sdlc-playbook](https://academy.claude.com/de/courses/ai-native-sdlc-playbook) — 14 Lektionen, hier zu einem Artikel zusammengeführt statt als 14 Einzeldateien.

## Kursbeschreibung

Ein technischer Leitfaden dazu, wie du deinen Softwareentwicklungslebenszyklus (SDLC) mit KI transformierst. Organisationen haben begonnen, KI zu nutzen, um Code in einer Geschwindigkeit zu schreiben, die vor einem Jahr noch unvorstellbar war, doch die Prozesse rund um den Code haben sich nicht im gleichen Tempo verändert.

**Für wen dieser Kurs gedacht ist:** Engineering-, Platform- und Security-Leads, deren Organisation bereits Claude Code nutzt und deren Genehmigungsgates, Reviews und Übergaben noch in menschlichem Tempo ablaufen. Geschrieben für große, insbesondere regulierte Unternehmen, bei denen sich die Review-Warteschlange nicht aufstauen darf und Code nicht unzureichend geprüft ausgeliefert werden darf.

**Voraussetzungen:** Vertrautheit mit Claude Code im Alltag, ein Git-Repository und eine CI-Pipeline, die veränderbar sind.

## Lektion 1 — Einführung

Organisationen haben begonnen, KI zu nutzen, um Code in einer Geschwindigkeit zu schreiben, die vor einem Jahr noch undenkbar war, doch die Prozesse rund um den Code haben sich nicht im gleichen Tempo verändert.

Viele Engineering-Teams haben noch immer dieselben Freigabe-Gates, Reviews, Übergaben und Richtlinien, die die Produktivitätsgewinne durch den Einsatz agentischer Coding-Lösungen wie Claude Code ausbremsen.

**Der traditionelle SDLC**

Der Software Development Lifecycle (SDLC) ist der Prozess, der Software von der Idee bis zur Produktion führt. Die meisten Organisationen durchlaufen eine Version derselben sechs Phasen, die Planung, Design, Entwicklung, Testen, Bereitstellung und Wartung von Software umfassen. Traditionell ist jede Phase ein eigenständiger Abschnitt, der von einer anderen Rolle verantwortet wird. Produktmanager schreiben Anforderungen, technische Architekten setzen sie in Designs um, Ingenieure bauen die Designs, QA-Teams in regulierten Unternehmen verifizieren die Software, Release-Teams liefern sie aus, und der Betrieb überwacht, was läuft. Arbeit bewegt sich zwischen den Phasen durch Dokumente, Tickets und Freigaben.

Der traditionelle SDLC ist prozessintensiv, um Verantwortlichkeit und Kontrolle bei jedem Schritt sicherzustellen. Er wurde jedoch entwickelt, um die Effizienz in einer Ära zu maximieren, in der die zeitaufwändigste und teuerste Phase das Schreiben und Implementieren von Code war – was heute nicht mehr der Fall ist. Product Requirements Documents (PRDs), Schätzungsrituale und Produktsicherheitsüberprüfungen existierten alle, um Abstimmung während dessen zu erzwingen, was Wochen, Monate oder Quartale an Entwicklungsarbeit sein konnte.

Der traditionelle SDLC verfügt außerdem über Kontrollen, die davon ausgehen, dass jeder Schritt von Menschen ausgeführt wird. Die Organisationen, die den größten Wert generieren, haben ihren Prozess um das umgebaut, was agentische KI heute leisten kann, während sie sicherstellen, dass Menschen im Loop bleiben.

**Wenn Code nicht mehr der Engpass ist**

Wenn Code nicht mehr der Engpass ist und die Build-Phase schneller läuft, als der traditionelle SDLC es zulässt, werden drei Dinge wahr:

- Der Engpass verschiebt sich auf die Phasen auf beiden Seiten der Build-Phase: hauptsächlich Planung, Review/Test und Deployment, die weiterhin im menschlichen Tempo laufen.
- Die Kontrollen passen nicht mehr zur Realität und werden unhandhabbar. Jede Zeile manuell zu überprüfen, ergab Sinn, als ein Mensch sie geschrieben hatte, aber das kann nicht mithalten, sobald Agenten den Großteil des Diffs schreiben.
- Die Governance-Kosten steigen, weil Ausnahmen weiterhin über Meetings und Ausschüsse laufen, die wöchentlich oder monatlich zusammenkommen.

Nehmen wir einen Sicherheits-Engpass als Beispiel. Sicherheitsteams sind auf menschliche Leistung ausgelegt, sodass sich, wenn Agenten die Code-Ausgabe vervielfachen, entweder die Review-Warteschlange aufbaut oder Code unzureichend überprüft ausgeliefert wird. Eine regulierte Organisation kann keines der beiden Ergebnisse akzeptieren, daher müssen ihre Sicherheits- und Richtlinienprüfungen mit den Agenten Schritt halten.

**Was ist ein KI-nativer SDLC?**

Der KI-native SDLC ist ein neu gedachter Prozess, der die alten Kontrollziele mit neuer Durchsetzung kombiniert. Statt eines linearen Ablaufs wird der Prozess zu einer Schleife, und KI ist an jedem Punkt eingebettet.

Die folgende Tabelle hebt die Extreme des Spektrums zwischen traditionellem SDLC und KI-nativem SDLC hervor:

| Phase | Traditioneller SDLC | KI-nativer SDLC |
|---|---|---|
| Plan | Anforderungen werden vom Ausschuss gesammelt, durch Workshops und Freigaben destilliert, von Hand aufgeschrieben | Claude synthetisiert Schmerzpunkte direkt aus den Quellen und erfasst sie in intent.md, die menschenlesbar und maschinenverarbeitbar ist |
| Design | Spezifikation von Analysten geschrieben, von Designern interpretiert | Anforderungen und Design werden in einer Arbeitssitzung mit einem Agenten komprimiert, geleitet von Standards, die als Skills kodiert und in Git versioniert sind |
| Build | Tests und Code werden handgeschrieben, Dokumentation danach | Tests und Code werden von KI generiert, institutionelles Wissen als CLAUDE.md-Dateien und Skills gepflegt |
| Test | QA-Gates an Phasengrenzen | Kontinuierliche Evals, durch die Implementierung gewoben |
| Deploy | Menschen überprüfen jede Codezeile, Governance oft inkonsistent | Schichten agentischer Reviews, menschliches Review für regulierten/kritischen Code, Hooks als Freigabe-Gates |
| Maintain | Menschen beobachten die Produktion auf Fehler | Agenten überwachen Live-Deployments, verletzte Kontrollgrenzen werden als neue intent.md zurückgeschrieben |

Was die KI-native Spalte zusammenhält, ist das committete Artefakt. Jede Phase endet damit, eines in die Versionskontrolle zu schreiben (intent.md, spec.md, plan.md, der Diff und seine Tests, der PR mit seinen Review-Ergebnissen, der Vorfallsbericht), und die nächste Phase beginnt damit, es zu lesen. Die Kette der Commits ist zugleich der Audit-Trail.

**Wie die Plays funktionieren**

Die Plays sind in sechs nicht-lineare Phasen gruppiert (Plan, Design, Build, Test, Deploy, Maintain). Jedes Play behandelt: was sich ändert, erste Schritte, konkrete Umsetzungsschritte, Governance-Überlegungen und wie du misst, ob es funktioniert hat. Eine Phase endet mit dem Committen eines Artefakts, wobei der Commit die nächste Phase einleitet — eine akzeptierte intent.md löst Requirements/Design aus, eine genehmigte spec.md löst Plan-Mode aus, ein gemergter PR löst die Pipeline aus, eine verletzte Kontrollgrenze in Produktion schreibt die nächste intent.md.

## Lektion 2 — Als intent.md erfassen (Phase 1: Planung)

Die intent.md, die den Softwareentwicklungsprozess einleitet, kann über verschiedene Wege entstehen: eine Person hat eine Idee, ein Ticket wird eingereicht, oder ein Vorfall wird über eine Warnmeldung sichtbar (siehe Lektion 13).

Wenn eine Person eine Idee hat, brainstormt sie mit Claude und erstellt eine Markdown-Proto-Spezifikation, die menschenlesbar, versionskontrolliert und sofort von der nächsten Stage nutzbar ist. Der Product Owner überprüft und korrigiert die vom Agenten geschriebene intent.md, bevor sie committet wird.

**Was sich ändert:** Traditionell durchläuft eine Idee Backlog-Einträge, User Stories, Story Points und Refinement-Meetings, bevor jemand darauf reagieren kann. KI-nativ brainstormt der Urheber mit Claude und schreibt das Ergebnis als intent.md — was gewünscht wird, warum, unter welchen Einschränkungen.

**Erste Schritte:** Keine Voraussetzungen. Infrastruktur: Claude-Zugang für Nicht-Engineers, eine intent.md-Vorlage, ein gemeinsam genutztes, versionskontrolliertes Zuhause für Intents (z. B. ein `intent/`-Ordner im Produkt-Repo).

**So wird es umgesetzt:** Der Urheber beschreibt Claude das Problem in eigenen Worten. Claude brainstormt bis die Idee konkret ist (Umfang, Nutzer, Einschränkungen, Erfolgskriterien). Claude schreibt das Ergebnis als intent.md nach Organisations-Vorlage. Der Urheber korrigiert Missverständnisse und committet.

Beispiel:

```markdown
# Intent: claims status self-service
Author: J. Ortiz (claims operations). Status: draft.
## Problem
Customers phone the contact center to ask where their claim is.
## Proposed outcome
Customers see claim status, next step and expected date in the portal.
## Affected users and systems
Claims handlers, portal team, claims-core API.
## Constraints
No new PII in the portal session. Existing authentication only.
## Open questions
Do third-party loss adjusters need access too?
```

**Governance:** Der Nachweis ist die committete intent.md mit Autor, Zeitstempel und Revisionshistorie in Git. Der Product Owner genehmigt.

**Messung:** Frühindikator ist die Zeit vom ersten Gespräch bis zur committeten intent.md. Spätindikator ist die Überlebensrate — der Anteil der intent.md-Dateien, die in Lektion 3 übernommen statt geschlossen werden.

## Lektion 3 — Anforderungen und Design (Phase 2: Design)

Sobald der Product Owner die intent.md genehmigt, übernimmt Claude sie und erstellt eine Anforderungs- und Design-Spezifikation, geleitet durch die Skills der Organisation für Marke, Sicherheit, Compliance und UX. Der Product Owner prüft diese Spezifikation, schreibt sie aber nicht.

Front-End-Arbeit ist das klarste Beispiel: Der Product Owner entwirft das Design in Claude Design (Beta) auf Basis der intent.md, iteriert, exportiert dann zu Claude Code zum Bauen.

**Was sich ändert:** Traditionell sind Anforderungen und Design separate Phasen mit separaten Teams. KI-nativ finden beide Phasen in einer einzigen geprompteten Sitzung statt.

**Erste Schritte:** Voraussetzung ist eine intent.md sowie Marken-, Sicherheits-, Compliance- und UX-Richtlinien als Skills. Infrastruktur: ein Product Owner mit Claude-Zugang, keine Engineering-Kenntnis nötig.

**So führst du es aus:** Der Product Owner öffnet eine Sitzung mit den verfügbaren Skills, hängt die intent.md an und lässt eine spec.md erstellen. Später wird die Annahme der intent.md zum automatischen Auslöser (nicht-interaktiver Job, der spec.md als PR committet). Der Product Owner prüft die Spezifikation gegen die Idee, klärt gekennzeichnete Bedenken mit den jeweiligen Policy-Ownern, committet spec.md zusammen mit intent.md und entscheidet über die Weitergabe an Build (bei höherem Risiko mit einem Technical Lead).

Prompt-Beispiel: „Lies die angehängte intent.md und erstelle eine Anforderungs- und Design-Spezifikation für ihre Integration in unsere bestehende Codebasis. Wende die dir verfügbaren Skills an … Dokumentiere die Spezifikation vollständig als spec.md … Beschreibe klar alle Problembereiche."

**Governance:** Richtlinienkonflikte werden beim Schreiben der Spezifikation erkannt statt Wochen später. Spezifikation, Prompt und geltende Skill-Versionen werden versioniert.

**Messung:** Frühindikator: Zeit zwischen intent.md- und spec.md-Commit. Spätindikator: Anforderungs-Nacharbeit nach Baubeginn (spec.md-Commits nach dem ersten plan.md-Commit).

## Lektion 4 — Claude Code Plan-Modus als Standard-Ausgangspunkt (Phase 3: Build)

Ingenieure starten Claude-Code-Sitzungen im Plan-Modus, geben Claude die genehmigte spec.md und lassen sich interviewen, wobei der Plan iterativ verfeinert wird.

**Was sich ändert:** Traditionell liest ein Ingenieur das Design und beginnt zu programmieren; wie umgesetzt wird, bleibt im Kopf des Ingenieurs. KI-nativ beginnt die Arbeit mit einem schriftlichen Plan, den Claude im Plan-Modus erstellt (liest die Codebasis, ohne etwas zu ändern); die genehmigte Version wird als plan.md committet.

**So wird es umgesetzt:** Sitzung im Plan-Modus starten, intent.md und spec.md geben, einen Implementierungsplan mit zu ändernden Dateien, Reihenfolge und Tests anfordern. Den Plan hinterfragen (was könnte kaputtgehen, welcher Schritt ist am riskantesten). Iterieren, bis ein fremder Ingenieur die Änderung allein umsetzen könnte. Genehmigten Plan als plan.md committen, dann implementieren lassen. Bei Abweichung plan.md im selben Commit aktualisieren.

Beispiel `plan.md`:

```markdown
# Plan: claims status self-service (from intent.md 2026-06-02)
## Files that change
portal/src/claims/StatusPanel.tsx (new), claims-api/routes/status.py, claims-api/tests/test_status.py
## Order of work
1. Add the status endpoint behind existing auth.
2. Panel against the endpoint.
3. Wire into the portal nav.
## Risks
The claims-core API rate-limits at 50 rps; the panel must cache.
## Proof
test_status.py covers the four claim states; screenshot matches the approved mock.
```

**Governance:** Das Design-Review erfolgt, bevor Code generiert wird. Der Plan-Modus erzwingt das selbst, da Claude vor Akzeptanz nicht bearbeiten kann.

**Messung:** Frühindikator: Anteil aus erstem Durchgang gemergter Änderungen. Spätindikator: Nacharbeitszyklen pro Änderung.

**Claude Code im Auto-Modus:** Der Ingenieur genehmigt den Plan, Claude wendet danach jede Änderung ohne Rückfrage pro Bearbeitung an. Mit ausgereiften Leitplanken (CLAUDE.md, Skills, Hooks, Testsuite) wird der Auto-Modus Standard für Routinearbeit und ermöglicht Parallelität über Worktrees hinweg — Grundlage für den autonomen Kreislauf in Lektion 13.

**Legacy-Systeme und Source of Truth:** Bestehende Prozesse verfolgen Artefakte oft schon, nur nicht in Markdown (Jira, Figma, Change Board). Für jedes Artefakt sollte ein System als Source of Truth benannt werden: das Repo als Wahrheit, das Legacy-System als Wahrheit (Claude liest/schreibt per MCP), oder Verlinkung als Mindestanforderung (Datensatz-ID im Artefakt, Commit-SHA im Legacy-Datensatz).

## Lektion 5 — Die CLAUDE.md (Phase 3: Build)

CLAUDE.md gibt Claude den Kontext, den ein neues Teammitglied benötigen würde: Konventionen, Befehle, Architektur, häufige Fehler. Wissen, das früher in Köpfen und Wikis steckte, wird zu einer Datei, die der Agent zu Beginn jeder Sitzung liest und die das ganze Team pflegt.

**Wie man es umsetzt:** `/init` im Repository ausführen. Die generierte Datei auf das kürzen, was ein neues Teammitglied am ersten Tag braucht (Build-/Test-/Lint-Befehle, wichtige Konventionen, wiederkehrende Fehler). CLAUDE.md im Root einchecken, damit Änderungen wie Code reviewt werden. Faustregel: Macht Claude zweimal denselben Fehler, kommt die Korrektur in CLAUDE.md. Datei unter einer Seite halten.

Beispiel:

```markdown
# Payments service
## Commands
- Build: make build
- Test: make test (unit), make itest (integration, needs docker)
- Lint: make lint (runs in CI; fix before pushing)
## Conventions
- Java 21, Spring Boot 3. No new Lombok.
- Money is always BigDecimal, never double.
## Architecture
- api/ holds REST controllers, core/ holds domain logic, adapters/ talks to external systems.
## Things Claude gets wrong
- Do not bump dependency versions; the platform team owns them.
```

**Governance:** CLAUDE.md wird versioniert, Änderungen werden im PR-Review von Code-Ownern genehmigt.

**Messung:** Frühindikator: wie oft Claude einen Fehler wiederholt, den CLAUDE.md hätte abfangen sollen. Spätindikator: Zeit bis zum ersten gemergten PR eines neuen Teammitglieds.

## Lektion 6 — Skills als institutionelles Wissen (Phase 3: Build)

Skills operationalisieren institutionelles Wissen: explizit, versionskontrolliert, breit angewendet, zentral aktualisiert. Faustregel: Ein Skill für institutionelles Wissen, das konsistent angewendet werden muss; kein Skill für Komponenten, die in CLAUDE.md oder einen Prompt gehören.

**So setzt du es um:** Ein inkonsistent durchgesetztes Wissenselement wählen (Sicherheitsstandard, API-Konvention, Markenregel). Als Skill schreiben — ein Ordner mit SKILL.md, deren Frontmatter den Auslöser definiert. Unter `.claude/skills/<name>/` ablegen oder per Plugin verteilen. Testen, dass der Skill zuverlässig auslöst. Bei Richtlinienänderung den Skill ändern und vom Verantwortlichen abzeichnen lassen.

Beispiel `.claude/skills/secure-api-review/SKILL.md`:

```markdown
---
name: secure-api-review
description: Apply the API security standard. Use whenever creating or
  modifying an external-facing endpoint, reviewing API code, or
  generating an OpenAPI spec.
---
# Secure API review
When you create or change an API endpoint:
1. Authentication: every endpoint requires the gateway JWT.
2. Input validation: validate request bodies against the OpenAPI schema.
3. Audit: every state-changing endpoint emits an audit event.
4. Data classification: pii-tagged fields must never appear in logs.
```

**Governance:** Ein Skill ist eine beratende Kontrolle, kein Zwang. Eine Richtlinie, die immer gelten muss, braucht zusätzlich einen Hook oder einen Review-Durchgang dahinter.

**Messung:** Frühindikator: Zeit von Richtlinien-Genehmigung bis Skill-Merge. Spätindikator: PR-Review-Befunde zur Richtlinie, die gegen null gehen sollten.

**Hooks als Guardrails zur Build-Zeit:** Ein Hook ist die deterministische Ebene hinter dem Skill. Build-Phase-Hooks können Bearbeitungen an geschützten Pfaden blockieren, Formatter/Linter nach Bearbeitungen laufen lassen, Zugangsdaten aus dem Diff heraushalten. Sie sollten schnell und auf die geänderte Datei beschränkt sein — ein Hook, der um Genehmigung bittet, gehört zu Lektion 11 (Deploy-Gates).

## Lektion 7 — Parallele Sessions und Subagents (Phase 3: Build)

Eine parallele Session ist eine weitere vollständige Claude-Code-Instanz in ihrem eigenen Git-Worktree; unabhängige Sessions wissen nichts voneinander. Ein Subagent läuft innerhalb einer Session als abgegrenzter Helfer mit eigenem Kontextfenster für wiederkehrende Aufgaben.

**Was sich ändert:** Traditionell bearbeitet ein Entwickler eine Aufgabe nach der anderen. KI-nativ laufen mehrere Sessions gleichzeitig, je in eigenem Worktree; die Entwickler-Rolle verschiebt sich zu Orchestrierung und Überwachung.

**So setzt du es um:** Arbeit in Aufgaben mit unterschiedlichen Dateien aufteilen (Aufgaben mit geteilten Dateien laufen sequenziell in einer Session). Jede parallele Aufgabe bekommt einen eigenen Worktree (`claude --worktree feature-auth`). Zwei bis drei Sessions als sinnvoller Ausgangspunkt — die Obergrenze ist, wie viele Streams eine Person überprüfen kann. Wiederkehrende Jobs als Subagents unter `.claude/agents/` definieren (Name, Beschreibung, erlaubte Tools), in Git committen.

Beispiel `.claude/agents/verifier.md`:

```markdown
---
name: verifier
description: Runs the app and checks the change works before the session reports done
tools: Bash, Read
---
Start the app with make run. Exercise the changed behavior and the two
nearest neighboring flows. Report what you ran, what you saw, and any
behavior that does not match plan.md. Do not fix anything; report only.
```

**Governance:** Mehr Sessions bedeuten mehr Output — Kontrollen müssen aus der Repo-Konfiguration kommen (Hooks, Berechtigungen gelten für alle Sessions, protokolliert und zugeordnet).

**Messung:** Frühindikator: gleichzeitige Sessions pro Entwickler bei stabiler Review-Qualität. Spätindikator: gemergte Änderungen pro Woche/Entwickler zusammen mit der Nacharbeitsrate.

## Lektion 8 — Gib Claude eine Feedback-Schleife (Phase 4: Test)

Gib Claude immer eine Möglichkeit, die eigene Arbeit zu überprüfen (Tests, Build, Screenshot-Vergleich), bevor ein Engineer sie sieht. Die Feedback-Schleife unterscheidet sich vom Verifizierer-Subagenten (Lektion 7): Sie durchläuft die ganze Aufgabe so oft wie nötig, während der Verifizierer die abschließende Prüfung mit frischem Kontext verpackt.

**Was sich ändert:** Traditionell kommt das Signal, dass Code funktioniert, spät (CI Minuten, Tester Tage, Produktion Wochen später). KI-nativ bekommt die Sitzung die Möglichkeit zur Selbstprüfung, bevor eine Person sie sieht.

**So setzt du es um:** Überprüfung in ein einziges Ziel verpacken (`make test`, `npm test`), das bei Fehler ungleich null endet. Befehle im „Commands"-Abschnitt der CLAUDE.md mit Beispielausgabe auflisten. Ziele quantifizierbar formulieren. Bei Fehlerkorrekturen zuerst den fehlschlagenden Test schreiben, committen, dann Claude bitten, ihn zum Bestehen zu bringen, ohne den Test zu bearbeiten (per Hook erzwungen). Bei UI-Arbeit mit visueller Prüfung schließen (Browser-/Screenshot-Tool, Mock, iterieren). Verifizierung zum Teil von „erledigt" machen. Die Schleife selbst schützen — ein Hook blockiert Bearbeitungen an Testdateien während einer Korrekturaufgabe.

Beispiel CLAUDE.md-Verifizierungsblock:

```markdown
## Verifying your work
- Build: make build (must finish with "Build succeeded")
- Test: make test (all green; never skip or delete a failing test)
- Lint: make lint (zero warnings)
Run all three before reporting any task complete, and paste the output.
If a test fails, fix the code, not the test.
```

**Governance:** Erzwungen wird die Verifizierung vor „erledigt" sowie die Testdatei-Sperre während Korrekturen, beides als Hooks. Nachweis ist die tatsächliche Toolchain-Ausgabe, protokolliert im Sitzungstranskript und im Check-Run des PRs.

**Messung:** Frühindikator: CI-Erfolgsrate beim ersten Durchlauf. Spätindikator: Überprüfungszeit pro PR und Änderungsfehlerrate.

## Lektion 9 — Kontinuierliche Evals in CI (Phase 4: Test)

Evals sind das KI-native Äquivalent zu Stage-Gate-QA: eine Suite, die läuft, wenn sich die Agentenkonfiguration ändert, und sagt, ob der Agent die Arbeit weiterhin in gleicher Qualität erledigt. Evals sind eine lebende Suite — verbessern sich Modelle, verlieren alte Fälle ihre Unterscheidungskraft, neue Fälle aus dem Monitoring müssen ergänzt werden.

**So setzt du es um:** 20–50 reale Aufgaben aus jüngster Arbeit sammeln, je mit erwartetem/akzeptiertem Ergebnis. Jede Aufgabe als Eval schreiben (Prompt plus Abnahmeprüfungen). Suite nicht-interaktiv in CI nach Zeitplan und bei jeder Änderung an CLAUDE.md/Skills/Hooks laufen lassen. Konfigurationsänderungen von den Ergebnissen abhängig machen. Jeder Produktionsvorfall bekommt ein Eval als dauerhaften Regressionstest.

Beispiel `.github/workflows/agent-evals.yml`:

```yaml
name: Agent evals
on:
  pull_request:
    paths: ['CLAUDE.md', '.claude/**']
  schedule:
    - cron: '0 2 * * *'
jobs:
  evals:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install -g @anthropic-ai/claude-code
      - name: Run eval suite
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          for eval in evals/*.json; do
            claude -p "$(jq -r '.prompt' $eval)" \
              --allowedTools "Read,Edit,Bash(make test)" \
              --output-format json > result.json
            ./evals/check.sh "$eval" result.json
          done
```

**Governance:** Der Erfolgsquoten-Schwellenwert wird als Merge-Check durchgesetzt; Durchläufe werden protokolliert.

**Messung:** Frühindikator: Eval-Erfolgsquote im Zeitverlauf. Spätindikator: in CI erkannte Regressionen im Vergleich zu in Produktion gefundenen.

## Lektion 10 — KI in der PR-Review-Schleife (Phase 5: Deployment)

Claude gibt Reviews ab und empfängt sie: prüft eingehende PRs anhand der Organisationsrichtlinien und bearbeitet Review-Kommentare zu eigenen PRs. Menschliche Aufmerksamkeit konzentriert sich auf Absicht und Risiko.

**Erste Schritte:** Voraussetzung ist eine aktuelle CLAUDE.md, ggf. Skills und definierte Subagenten. Infrastruktur: der verwaltete Code-Review-Dienst (Research Preview) oder die `claude-code-action` in eigener CI, plus Branch-Protection mit Code-Owner-Genehmigung.

**Wie man es umsetzt:** Verwalteten Dienst aktivieren oder `claude-code-action` in eigener CI einrichten. Der Tech Lead schreibt `REVIEW.md` im Repo-Root mit den Durchläufen (Bugs/logische Fehler, Sicherheit, Konformität mit spec.md/plan.md/Designprinzipien) sowie was „Wichtig" gegenüber „Nit" bedeutet. Befunde genehmigen/blockieren einen PR nicht von sich aus — Branch-Schutz verlangt weiter Code-Owner-Genehmigung. `@claude` in einem Kommentar löst eine Korrektur aus; bei eigenen PRs kann Claude bis zum Merge betreuen. Review-Befunde fließen in CLAUDE.md zurück, wenn ein Fehler zum zweiten Mal markiert wird.

Beispiel `REVIEW.md`:

```markdown
# Review instructions
## Passes
Run three passes and tag each finding with its pass:
- Bugs: logic errors, broken edge cases, subtle regressions
- Security: injection risks, authentication gaps, PII in logs
- Compliance: the change matches spec.md, plan.md and our design principles
## What Important means here
Reserve Important for findings that would break behavior, leak data or breach a policy.
## Cap the nits
Report at most five nits per review; summarize the rest as a count.
```

**Governance:** Der Agent, der den Code schrieb, kann ihn nicht genehmigen. Befunde, Korrekturen, Bewertungen und Genehmigungen werden in der PR-Historie protokolliert.

**Messung:** Frühindikator: Zeit bis zum ersten Review. Spätindikator: vor dem Merge erkannte Defekte im Verhältnis zu in Produktion durchgesickerten.

## Lektion 11 — Hooks als Genehmigungsgates (Phase 5: Deployment)

Ein Hook kann auch nachfragen und eine Aktion pausieren, bis eine bestimmte Person zustimmt — Release-Gating. Hooks sind nicht deploy-spezifisch: Sie laufen überall dort, wo Claude handelt.

**So setzt du es um:** Engineering-Führung listet zusammen mit Change Management/Compliance die zu erhaltenden Genehmigungsgates. Jedes Gate wird als Hook ausgedrückt (Skript, das erlaubt/nachfragt/blockiert). Team-Hooks in `.claude/settings.json` in Git, nicht verhandelbare Hooks in verwalteten Einstellungen des Plattform-/IT-Admins. Eine Blockierung sollte Grund und Genehmigungsweg in Claudes Ausgabe erklären.

Beispiel `.claude/settings.json` + Gate-Skript:

```json
{
  "hooks": {
    "PreToolUse": [
      { "matcher": "Bash",
        "hooks": [{ "type": "command",
          "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/production-gate.sh" }] }
    ]
  }
}
```

```bash
#!/bin/bash
cmd=$(jq -r '.tool_input.command' < /dev/stdin)
if [[ "$cmd" == *"deploy"* && "$cmd" == *"production"* ]]; then
  if [ -z "$RELEASE_APPROVAL" ]; then
    echo "Production deploys need a release authorization." >&2
    exit 2
  fi
fi
exit 0
```

**Verwaltete Einstellungen für ein reguliertes Unternehmen** (per MDM/Admin-Konsole, von Engineers nicht überschreibbar) kombinieren mehrere Kontrollebenen: `permissions.deny/allow` für Datei-Tools, `disableBypassPermissionsMode`/`allowManagedPermissionRulesOnly` gegen lokale Erweiterung, `sandbox` (Dateisystem-/Netzwerk-Isolation auf OS-Ebene, unabhängig von Tool-Permissions), `credentials`-Denylist gegen `~/.ssh`/`~/.aws/credentials` in sandboxed Shell-Befehlen, `allowManagedHooksOnly` gegen nicht-verwaltete Hooks, `disableSideloadFlags`/`strictKnownMarketplaces` gegen Plugins außerhalb des genehmigten Marktplatzes, `allowManagedMcpServersOnly` als Tool-Allowlist, `requiredMinimumVersion` gegen veraltete Clients.

**Messung:** Frühindikator: Wartezeit je Genehmigungsgate (aus dem OpenTelemetry-Export). Spätindikator: Gate-Verstöße, die vor/nach Hook-Einführung in Produktion gelangen.

## Lektion 12 — CI/CD-Integration und Deployment (Phase 5: Deployment)

Claude Code läuft nicht-interaktiv innerhalb der CI/CD-Pipeline, sandboxed mit eingegrenzten Zugangsdaten; Deployment-Tools kommen über MCP; Rollback-Pfade werden geprobt, bevor der Agent sie braucht.

**So setzt du es um:** Mit schreibgeschützten Urteilsschritten beginnen (`claude -p` zur Build-Triage, Flaky-Test-Zusammenfassung, Changelog-Entwurf). Schreibschritte hinter bestehenden Gates ergänzen (Lint-Fixes, generierte Doku, `@claude`-Review-Antworten) — alles kommt als PR, kein direkter Push nach `main`. Ausführung sandboxed in Containern mit kurzlebigen, eingegrenzten Tokens. Deployment über MCP-Tools pro Umgebung eingrenzen. Autonomie nach Umgebung abstufen (Dev frei, Staging dazwischen, Produktion bereitet der Agent vor, ein Release-Manager autorisiert per Hook). Rollback als am häufigsten geprobter Pfad — ein einzelner Befehl, regelmäßig in Staging geübt.

Beispiel Pipeline-Schritt:

```yaml
- name: Triage failed build
  if: failure()
  run: >
    claude -p "Read the build log at out/build.log. Identify the most
    likely cause, say whether the failure looks flaky or real, and write a
    three-line summary for the PR thread." >> triage.md
```

**Governance:** Der Agent darf bis zum Produktions-Gate handeln, es aber nicht passieren — durchgesetzt durch Branch-Schutz, den Produktions-Deploy-Hook und umgebungsabhängige Berechtigungsstufen.

**Messung:** Frühindikator: Anteil ohne Menschen triagierter Pipeline-Fehler. Spätindikator: DORA-Kennzahlen.

## Lektion 13 — Den Kreislauf bei Metriken schließen (Phase 6: Betrieb)

Anders als jede vorherige Stufe läuft Stufe 6 headless: Ein Trigger (Kontrollband-Verletzung, Ticket, Kanalnachricht, Zeitplan) ruft Claude ohne Person im Ablauf auf. Claude diagnostiziert, handelt nur über abgesicherte Routen und schreibt seine Erkenntnisse als intent.md, die dann alle vorherigen Stufen durchläuft.

**So wird es umgesetzt:** Eine Metrik mit stabiler rollierender Baseline wählen (CI-Testfehlerrate, Post-Deploy-5xx-Rate, PR-Zykluszeit). Ein deterministisches Erkennungsskript schreiben (Mittelwert/Standardabweichung über rollierendes Fenster, Western-Electric-Regeln o. Ä.), vollständig ohne Modellbeteiligung. Reaktionsstufen versioniert konfigurieren: bei 1σ nur protokollieren, bei 2σ Claude read-only zur Diagnose aufrufen, bei 3σ darf Claude nur einen PR öffnen oder ein vorab genehmigtes Runbook auslösen. Der Agent schreibt seine Diagnose als intent.md; der Service-Owner triagiert (beheben/planen/verwerfen). Nach einem Fix wird ein Eval ergänzt (Lektion 9).

Beispiel `bands.yaml`:

```yaml
metric: ci_test_failure_rate
baseline: rolling_30d
rules: western_electric
tiers:
  1sigma: { action: log }
  2sigma: { action: diagnose, tools: "Read,Grep,Bash(gh run view *)" }
  3sigma: { action: propose, routes: [pull_request, runbook:rollback-deploy] }
```

Beispiele: Bei 3σ CI-Testfehlerrate isoliert der Agent den instabilen Test oder öffnet einen Revert-PR. Bei 3σ Post-Deploy-5xx während eines Deployment-Zeitfensters löst der Agent die bestehende Rollback-Pipeline aus. Bei einer PR-Zykluszeit-Drift schreibt der Agent einen Bericht für die Engineering-Leitung.

**Claude im Bereitschaftsdienst mit Claude Tag:** Claude Tag (Public Beta, Slack) macht Claude zum Kanalmitglied unter eigener Identität — jeder Incident bekommt einen First Responder, das Post-Mortem geht in eine versionierte Lessons-Datei. Wird Claude auf einem Ticket getaggt, triagiert es genauso: kleine Fixes als PR, Größeres als neue intent.md für Lektion 2 — der Kreislauf beginnt, sich selbst zu speisen.

**Messung:** Frühindikator: Zeit von Bandverletzung bis intent.md in der Triage-Warteschlange. Spätindikator: Anteil der Befunde, die zu gemergten Fixes werden, sowie rückläufige wiederkehrende Incidents derselben Klasse.

## Lektion 14 — Abschließende Gedanken und Ressourcen

Modelle und Harnesses sind fortschrittlicher geworden und ermöglichen es Organisationen, nicht nur die Art und Weise zu transformieren, wie sie Code produzieren, sondern den gesamten Lebenszyklus der Softwareentwicklung — bei weiterhin zentralem menschlichem Urteilsvermögen und unter Berücksichtigung von Governance- und Regulierungsanforderungen.

**Ressourcen** (ungefähr in Einführungsreihenfolge): Claude Code für die Organisation einrichten (Admin-Entscheidungskarte), Einstellungsreferenz und Priorität, serververwaltete Einstellungen aus der Claude-Admin-Konsole, Berechtigungen, Sandboxing, Hooks-Leitfaden und -Referenz, Skills, Plugins und private Marketplaces, verwaltetes MCP, Übersicht zur Unternehmensbereitstellung (Bedrock, Vertex AI, Microsoft Foundry), Netzwerkkonfiguration für Unternehmen, Monitoring (OpenTelemetry) und Analytics-Dashboard, Compliance-API, Sicherheitsmodell.
