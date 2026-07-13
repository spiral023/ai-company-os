---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-16
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zum „Skill Creator Skill für AI Coding Agents“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/02-agent-guides-und-templates/wka-skill-creator-skill-fuer-ai-coding-agents-2026-04-16.md`), Einordnung des offiziellen `skill-creator`-Skills aus `anthropics/skills` (README/SKILL.md per Repo-Zugriff).

Kernpunkte (kondensiert):

- Der Skill Creator behandelt Skills als messbare Produkte, nicht nur als Dateien mit Frontmatter: Lebenszyklus Ziel/Scope klären → Entwurf → Testprompts definieren → mit/ohne Skill vergleichen → auswerten → iterativ verbessern → optional Trigger-Description optimieren.
- Adressierte Fehler: Skills zu früh geschrieben, vage Trigger-Beschreibungen (zu selten/falsch aktiviert), nur gefühlsbasierte Bewertung, keine Baseline-Vergleiche, Iteration endet nach erstem Draft.
- Progressive Disclosure innerhalb eines Skills: (1) Metadaten immer sichtbar, (2) `SKILL.md` bei Aktivierung, (3) weitere Ressourcen (`scripts/`, `references/`, `assets/`) nur bei Bedarf geladen.
- Trigger-Beschreibung als Kernhebel: Claude untertriggert Skills eher als dass es übertriggert, deshalb bewusst „pushigere“ `description`, die klar sagt was der Skill tut, wann er relevant ist, und ähnliche Formulierungen/Kontexte abdeckt.
- Testfälle: 2-3 realistische Testprompts, gefahren mit UND ohne Skill als Baseline-Vergleich, um zu prüfen ob der Skill wirklich etwas verbessert oder nur Tokens kostet.
- Bundled Scripts: wenn dieselbe Hilfslogik in mehreren Testläufen wiederholt neu geschrieben wird, gehört sie in `scripts/` statt jedes Mal neu erfunden zu werden.
- Should-trigger/should-not-trigger-Evals als eigene Qualitätsdimension neben dem eigentlichen Skill-Inhalt.

## Kernaussagen

- Skills sollten als messbare Produkte mit Baseline-Vergleich (mit/ohne Skill) statt nach Gefühl bewertet werden → [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- Die Trigger-Description ist der primäre Aktivierungsmechanismus; Untertriggern ist das häufigere Problem als Übertriggern → [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- Progressive Disclosure innerhalb eines Skills (Metadaten immer sichtbar, Body bei Aktivierung, Zusatzressourcen nur bei Bedarf) hält das Kontextbudget klein → [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
