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
- 2026-07-03 · [[2026-07-03-trq212-2073100352921215386]] · meinung — Ergänzt eine konkrete Priorisierungsregel für den Plan-Schritt: Implementierungspläne nach Änderungswahrscheinlichkeit sortieren (Datenmodelle/Interfaces zuerst), damit Review-Aufwand dort konzentriert wird, wo Fehlannahmen am teuersten sind.
- 2026-08-04 · [[2026-08-04-anthropic-docs-claude-code-best-practices]] · meinung — Ergänzt einen konkreten Adversarial-Review-Prompt gegen `PLAN.md`: Diff gegen Plan, Edge-Case-Test-Abdeckung und Scope-Grenzen prüfen, mit der expliziten Anweisung „Report gaps, not style preferences“.
- 2026-02-27 · [[2026-02-27-meer-claude-code-best-practices]] · meinung — Boris Cherny (laut Tweet-Sekundärquelle) lässt eine zweite Claude-Instanz bereits den Plan selbst als Senior Engineer prüfen, bevor implementiert wird — Review vor der Umsetzung statt erst am fertigen Diff.
- 2026-01-10 · [[2026-01-10-eyad-khrais-claude-code-tutorial]] · meinung — Erfahrungsbericht: Plan Mode vor Implementierung liefert laut Autor „10 von 10 Mal“ signifikant bessere Ergebnisse als direktes Losschreiben (unbelegte Einschätzung).
- 2026-02-01 · [[2026-02-01-anthropic-docs-claude-code-best-practices]] · meinung — Offizielle Anthropic-Doku bestätigt Explore→Plan→Implement→Commit als empfohlenen Standardablauf für nicht-triviale Änderungen.
- 2026-01-06 · [[2026-01-06-jarrodwatts-context-engineering-guide]] · meinung — Ergänzt die Empfehlung, den Plan vor der Umsetzung mehrfach gegen Architektur, Best Practices, Sicherheitsrisiken und Teststrategie zu reviewen, statt nur einmal gegenzulesen.
- 2026-02-10 · [[2026-02-10-boris-tane-plan-annotation-workflow]] · meinung — Trennt Recherche (`research.md`, geprüftes Artefakt vor jeder Planung) und Planung (`plan.md`) explizit in zwei aufeinanderfolgende, persistente Dokumente statt eines einzigen Plans. Der wertschöpfende Schritt ist der Annotations-Zyklus: 1–6 Runden inline-Notizen direkt im Plandokument (Plan als „Shared Mutable State“), mit explizitem „don't implement yet“-Guard gegen vorschnelle Umsetzung — ohne den Guard springt das Modell zur Implementierung, sobald der Plan aus seiner Sicht gut genug wirkt. Nach Freigabe folgt ein fester, wortidentischer Implementierungs-Prompt („implement it all … do not stop until all tasks and phases are completed … continuously run typecheck“).
- 2026-01-14 · [[2026-01-14-ashpreetbedi-claude-code-spec-first]] · meinung — `design.md` als „Source of Truth“ mit der Regel „Keine Spec, keine Implementierung“ bestätigt unabhängig das Prinzip Plan-als-persistentes-Artefakt-vor-der-Umsetzung; ausführlichere Umsetzung als eigenständiges Pattern siehe [[Spec-Ordner-pro-Feature]]. Ergänzt Plan Mode und bewusstes Front-Loading von Architektur, Edge Cases und Constraints vor der Implementierung.
- 2026-01-22 · [[2026-01-22-hooeem-claude-code-7-schritte-plan]] · meinung — Unterscheidet Plan Mode (Shift+Tab×2, für Breite) explizit von Extended Thinking/„Ultrathink“ (für Tiefe) als zwei unterschiedliche, je zusätzlich Tokens kostende Arbeitsmodi; ergänzt ein Hook-Beispiel, das vor jedem Commit eine zweite Claude-Instanz gezielt auf doppelten Code prüfen lässt — Review automatisch statt manuell ausgelöst.
- 2026-01-31 · [[2026-01-31-bcherny-claude-code-team-tips]] · meinung — Team-Praxis bestätigt beide Kernideen: Bei schiefgehender Aufgabe wird zurück in Plan Mode gewechselt statt am fehlerhaften Pfad weiterzuarbeiten; eine zweite Claude-Instanz prüft den Plan explizit in der Rolle eines Staff Engineers, bevor implementiert wird.
- 2026-02-01 · [[2026-02-01-aiedge-claude-code-starter-pack]] · meinung — Spannung: Ein Praktiker meidet Plan Mode dauerhaft, weil frühe Versionen keine Tool-Rechte vom YOLO-Modus erbten und deshalb ständig neue Freigaben anfragten (Stand Dezember 2025) — ersetzt Plan Mode durch vom Agenten gestellte Klärungsfragen, die in einer Markdown-Datei beantwortet werden (siehe [[Handoff-Doc]]). Zeigt einen Fall, in dem eine technische Einschränkung einen erfahrenen Nutzer vom Konzept weggetrieben hat, ohne das Grundbedürfnis (klären vor Ausführen) zu widerlegen.
- 2026-02-01 · [[2026-02-01-anthropic-docs-claude-code-common-workflows]] · meinung — Nennt `claude --permission-mode plan -p "..."` als headless, rein lesenden Analyseschritt ohne Seiteneffekte — ein automatisierbares Vorab-Planungsmuster, das die Schwesterquelle nur interaktiv (`Ctrl+G` im Editor) beschrieb. Reine CLI-Flag-Konkretisierung, keine neue Aussage zum Wert von Plan Mode selbst.
- 2026-07-30 · [[2026-07-30-julian-ivanov-interaktive-schulungen-mit-claude-code]] · meinung — Überträgt Plan-first auf Content-Produktion: Ein Curriculum mit Lernzielen, Leveln und Voiceover wird vor der kostenpflichtigen Mediengenerierung geprüft und explizit freigegeben.
- 2026-08-30 · [[2026-08-30-alex-sprogis-loop-graph-engineering-das-letzte-video-was-du-s]] · meinung — Unabhängiger Reviewer-Agent sieht nur Spezifikation und Ergebnis, QA behebt keine Bugs, Subagents melden nie selbst „fertig“; gilt auch für Architektur und Aufgabenplan. Erfahrungsbericht ohne Vergleich.
- 2026-06-16 · [[2026-09-17-anthropic-how-claude-code-is-used-in-practice]] · meinung — Sessions, in denen Claude die Planung übernimmt, lösen ca. 16 statt ca. 8 Aktionen pro Turn aus; Expert-Sessions haben 11,7 statt 4,9 Aktionen pro Prompt. Korrelation, keine Kausalität.
- 2026-09-19 · [[2026-09-19-voxyz_ai-2101355643882065971]] · meinung — Der Reviewer-Prompt verlangt eine getrennte Konversation oder einen Review-Agent, der die Umsetzung unabhängig prüft und zuerst berichtet, dann ändert; nichts erfinden. Bestätigt die Trennung von Umsetzung und Review, liefert aber keine Messung.
- 2026-07-26 · [[2026-07-26-promptgefluester-ich-hab-ne-unbequeme-wahrheit-und-zwar-ich-wurde-gefragt-wieso]] · meinung — Plant mit Fable Five, setzt mit Opus 5 um und ergänzt Vorab-Validierung der Business-Logik sowie nachgelagerte Impact-Analysen gegen Logik-Drift. Nur als Arbeitsbericht, keine Vergleichsmessung.
- 2026-06-02 · [[2026-06-02-trq212-2061907337154367865]] · meinung — Adversariale Verifikation durch getrennte Verifier-Agents (je Ergebnis oder je Regel) gegen Self-preferential Bias. Herstellerpraxis, nicht gemessen.
- 2026-09-24 · [[2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck]] · meinung — Review-Subagent mit eigenem Context Window liest coding-standards.md und committet Fixes statt zu kommentieren; Implement-Agent bleibt frei von Standards. Kosten: zusätzliche Review-Tokens pro PR.
- 2026-08-14 · [[2026-08-14-floknowsai-ueber-achtzig-prozent-des-codes-von-claude-code-und-codex-sieht-kein]] · meinung — Frische Review-Session mit Originalaufgabe hebt laut zitierter Studie die Endkorrektheit von 71,6 auf 89,7 Prozent; Zahlen nur aus TikTok-Caption, Studie nicht verlinkt.
- 2026-02-05 · [[2026-02-05-kloss-xyz-feature-intelligence-architect]] · meinung — Read-only-Planer erzeugt eine Plan-Datei, Build-Agent führt nach Freigabe aus; Sekundärquelle, keine Wirkungsmessung.
- 2026-09-26 · [[2026-09-26-voxyz_ai-2103977414711767244]] · meinung — Befundliste wird vor jeder Änderung gezeigt, Änderungen erst nach Freigabe, danach Vorher/Nachher-Screenshots.
- 2026-02-15 · [[2026-02-15-avid-ai-design-workflow-2026]] · meinung — Dreistufiger Design-Ablauf mit erzwungenem Self-Review-Durchgang; die Angabe, die KI finde dabei 70 % ihrer Fehler, ist selbstberichtet. Sekundärquelle.
- 2026-02-03 · [[2026-02-03-svpino-claude-code-md-tips]] · meinung — Regelzeile „Ansatz beschreiben, Freigabe abwarten“ für die CLAUDE.md. Sekundärquelle, kein Review-Trennung.
- 2026-02-04 · [[2026-02-04-lovable-docs-prompting-debugging]] · meinung — Plan-Modus für Audits ohne Codeänderung; Lovable-spezifisch, Sekundärquelle.
- 2026-08-25 · [[2026-08-25-vikingmute-2092059170812108811]] · meinung — Strenger Review-Skill (Cursor zugeschrieben) erzwingt Strukturvereinfachung, 1000-Zeilen-Grenze; nur Selbstversuch, Regeln vom Autor übersetzt.
- 2026-09-09 · [[2026-09-09-alex-sprogis-so-erstellst-du-interaktive-architektur-diagramm]] · meinung — Beschreibt Workflow Spec, Architektur, Tasks, Build, unabhängige QA gegen die Spec; nur Beschreibung, gesponserte Demo.
- 2026-08-05 · [[2026-08-05-creatoreconomy-use-my-human-review-skill-to-edit-html-and-markd]] · meinung — Menschliches Review von Planungsdokumenten per Inline-Kommentar in einem lokalen Visual Editor statt im Chat. Neu ist nur das Werkzeug; keine Wirksamkeitsmessung.
- 2026-08-18 · [[2026-08-18-floknowsai-hoer-auf-den-code-deines-ki-agenten-zu-lesen]] · meinung — Zweiter Agent mit frischem Kontext prüft Code und Tests, weil der Autor-Agent befangen ist; Kosten: doppelter Tokenverbrauch.
- 2026-09-27 · [[2026-09-27-voxyz_ai-2104224555040452925]] · meinung — Die Agent-Dateien werden erst nach Freigabe geschrieben, Befunde kommen priorisiert mit Repro, Screenshot und Fix an die Hauptsession, Unprüfbares als „untested“. Wirkung nicht belegt.
- 2026-09-22 · [[2026-09-22-promptgefluester-ich-arbeite-mit-multiorgastation-und-das-hat-was-mit-meinem-tokenlimit]] · meinung — Plan mit Opus erstellen, mit Sonnet gegenreviewen; Planfehler seien später teurer. Behauptet, das Review finde noch weitere Fehler (ohne Zahl).

- 2026-09-20 · [[2026-09-20-eric-tech-claude-code-the-complete-ai-native-sdlc-guide]] · meinung — Intent erklärt das Warum, Spec das erwartete Verhalten, Plan Dateien, Reihenfolge, Risiken und Nachweise; bestehende Plan-Workflows weiterverwenden. Sekundärdarstellung des Anthropic-Playbooks, keine unabhängige Wirkungsmessung.
- 2026-10-05 · external_repos/obra/superpowers/skills/writing-plans/SKILL.md · verifiziert — Der im Video genannte Plan-Skill fordert einen Plan aus Spec oder Anforderungen vor Codeänderungen, mit konkreten Dateien, Schnittstellen und Tests pro Aufgabe; bestätigt die beschriebene Plan-Variante, keine Produktivitätswirkung.
- 2026-10-08 · [[2026-10-08-mattpocockuk-2108216899439894574]] · meinung — Pocock empfiehlt /wayfinder erst nach begonnener Klärung bei wachsender Komplexität, weil ein vorschneller Plan unnötige Karten und Tickets erzeugen kann; menschliches Review behandelt er separat von der Entscheidung über Grilling vor dem Coden.

## Spannungen & offene Fragen

- 2026-10-09 · [[2026-10-08-mattpocockuk-2108216899439894574]]: Wayfinder erst bei wachsender Komplexität der begonnenen Klärung einsetzen; zu frühe Planung kann unnötige Karten und Tickets erzeugen. Menschliches Review bleibt eine getrennte Entscheidung, auch wenn kleine Diffs ohne vorgelagerten Plan entstehen.

- Beide ursprünglichen Quellen teilen sich mindestens eine Primärquelle (@Meer_AIIT), sind also nicht vollständig unabhängig; die neu ergänzten Quellen (Aseem Shrey, Thariq, Matt Pocock) sind davon unabhängig und beschreiben eigenständige, sich ergänzende Facetten derselben Grundidee.
- Offene Frage: Wie genau lässt sich die hier beschriebene Rollentrennung (Builder/Reviewer/Verifier) mit [[Kontrollierte-Agent-Parallelisierung]] kombinieren, wenn Builder und Reviewer parallel statt sequentiell arbeiten sollen?

## Verwandte Patterns

- [[Spec-Grilling]]
- [[TDD-als-Verifikationshebel]]
- [[Kontrollierte-Agent-Parallelisierung]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
