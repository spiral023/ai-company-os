# Skill-Call-Hierarchie

**Konfidenz:** verifiziert

## Zweck

Verhindert unkontrollierte, tief verschachtelte oder zirkuläre Aufrufketten zwischen Skills, sobald eine Skill-Bibliothek eine gewisse Größe erreicht. Ohne klare Hierarchie kann jeder Skill jeden anderen aufrufen — das macht das Gesamtverhalten schwer vorhersagbar.

## Funktionsweise

Skills werden entlang genau einer Achse unterschieden: wer sie aufrufen darf. **User-invoked** Skills sind ausschließlich per explizitem Nutzerbefehl erreichbar (z.B. `/grill-me`) und übernehmen die Orchestrierung. **Model-invoked** Skills sind sowohl vom Menschen als auch automatisch vom Modell erreichbar, sobald die Aufgabe passt, und tragen die eigentliche, wiederverwendbare Disziplin/Logik. Die Regel: ein Orchestrator (user-invoked) darf Disziplin-Skills (model-invoked) aufrufen, aber niemals einen anderen Orchestrator. Technisch wird das über das Frontmatter-Feld `disable-model-invocation: true` erzwungen — ein user-invoked Skill hat dadurch keine modell-lesbare `description`, also kann ihn kein anderer Skill „finden“ und aufrufen.

Version 1.1 macht diese Trennung im Lifecycle sichtbar: `wayfinder`, `to-spec`, `to-tickets` und `implement` sind bewusst vom Menschen gestartete Orchestratoren. `research`, `prototype`, `tdd`, `domain-modeling`, `codebase-design` und `code-review` liefern automatisch erreichbare Disziplin. Die Umbenennung von `to-prd`/`to-issues` zu `to-spec`/`to-tickets` beschreibt Artefakte allgemeiner und sollte in aktuellen Anleitungen verwendet werden.

## Vorteile

- Verhindert tiefe oder zirkuläre Aufrufketten strukturell, nicht nur durch Konvention.
- Klare Trennung von Orchestrierung (was tun) und Disziplin (wie tun) macht einzelne Skills leichter verständlich und austauschbar.
- Vorhersagbare Komposition: aus der Klassifizierung eines Skills folgt sofort, wer ihn aufrufen darf.

## Nachteile & Grenzen

- Erfordert Disziplin bei der Neuklassifizierung jedes neuen Skills; eine falsche Einordnung kann die Invariante unbemerkt brechen.
- Mehr Entwurfsaufwand upfront als eine flache, unstrukturierte Skill-Liste.
- Setzt voraus, dass sich jeder Skill eindeutig einer der beiden Kategorien zuordnen lässt — Grenzfälle sind denkbar.

## Wann einsetzen, wann nicht

- Einsetzen: Skill-Bibliotheken mit mehr als einer Handvoll Skills, insbesondere wenn Skills sich gegenseitig aufrufen können sollen.
- Nicht einsetzen: einzelne, isolierte Skills oder sehr kleine, triviale Setups ohne Aufrufbeziehungen.

## Belege

- 2026-07-10 · [[2026-07-10-voxyz-mattpocock-skills]] · meinung — Tweet beschreibt die Aufruf-Hierarchie: user-invoked orchestrieren, model-invoked halten die Disziplin, Orchestrator ruft nie Orchestrator.
- 2026-07-11 · external_repos/mattpocock/skills/.agents/invocation.md · verifiziert — Datei „Model-invoked vs user-invoked“ definiert exakt diese Unterscheidung inkl. Frontmatter-Flag `disable-model-invocation: true` und der Regel „a user-invoked skill may invoke model-invoked skills, but it can never reach another user-invoked skill.“
- 2026-07-11 · external_repos/mattpocock/skills/README.md · verifiziert — Abschnitt „Reference“ gliedert alle Skills explizit in „User-invoked“ und „Model-invoked“ je Kategorie (Engineering/Productivity) und wiederholt die Aufrufregel wörtlich.
- 2026-07-08 · [[2026-07-08-mattpocock-skills-v1-1]] · meinung — Release-Ankündigung dokumentiert den aktuellen Lifecycle, unterstützende Skills und die neuen Namen `to-spec` und `to-tickets`.
- 2026-07-13 · external_repos/mattpocock/skills/README.md · verifiziert — Die aktuelle Reference-Liste klassifiziert Lifecycle-Orchestratoren als user-invoked und Research, Prototype, TDD, Domain Modeling, Codebase Design und Code Review als model-invoked.
- 2026-01-21 · [[2026-01-21-tempoimmaterial-agent-skills-vs-rules-vs-commands]] · meinung — Unabhängige Bestätigung derselben Aufruf-Achse unter anderen Namen: Commands sind deterministisch und explizit ausgelöst (= user-invoked), Skills ein Vorschlag, den der Agent selbst zieht (= model-invoked).
- 2026-01-22 · [[2026-01-22-hooeem-claude-code-7-schritte-plan]] · meinung — Wiederkehrende, komplexe Prompts werden als Markdown-Datei in `.claude/commands/` hinterlegt und per Slash-Command deterministisch statt neu formuliert ausgelöst — knappe Bestätigung der Commands-als-deterministischer-Trigger-Seite dieses Patterns.
- 2026-02-11 · [[2026-02-11-rohit4verse-guide-building-agent-skills]] · meinung — Dreistufige Offenlegung (Frontmatter, Body, Ressourcen) als Ladehierarchie; Sekundärquelle, deckt sich mit Doku.
- 2026-04-22 · [[2026-04-22-agenticjames-everything-you-need-to-know-about-context-engineering-in-1-minute]] · meinung — Progressive Disclosure als Baum aus Entscheidungen statt Vorabladen; Grenzen des Verweisfolgens nicht behandelt.
- 2026-07-25 · [[2026-07-25-agenticjames-they-cut-claude-code-system-prompt-by-80-and-you-should-be-doing-the]] · meinung — Ausgelagerter Kontext gehört in Skills zur progressiven Offenlegung. Bekannte Aussage, hier nur wiederholt.
- 2026-02-01 · [[2026-02-01-anthropic-docs-extend-claude-with-skills]] · meinung — Frontmatter `disable-model-invocation`, `user-invocable`, `context: fork` steuern Auslösung und Isolation; Sekundärquelle.
- 2026-10-02 · [[2026-10-02-developers-using-gpt-6-openai-api]] · meinung — OpenAI rät, den Vorrang der Nutzeranweisung vor Skill-Anweisungen explizit zu setzen, weil Astra empfindlicher auf Skills und `AGENTS.md` reagiert und bei Widersprüchen früh pausiert. Selbstbericht, verhaltensbasiert, nicht gemessen.

## Spannungen & offene Fragen

- Keine bekannt.

## Verwandte Patterns

- [[Spec-Grilling]]
- [[Handoff-Doc]]
- [[Klein-und-komposierbar]]
