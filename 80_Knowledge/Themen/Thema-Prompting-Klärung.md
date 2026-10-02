# Prompting & Klärung

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-02. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Wie man dem Modell Absicht und Wissen gibt: Prompt-Technik, Pre-Mortem, Unknowns, Voice-Prompting, Anweisungen bei Modellwechsel ausdünnen, Anti-Sycophancy.

## Suchbegriffe

- **Hauptkeyword:** Prompt Engineering
- **Long-Tail:** Pre-Mortem Prompt; Unknowns aufdecken Prompt; Voice Prompting Coding; Anweisungen bei Modellwechsel ausdünnen; Agent Sycophancy vermeiden; Prompt für Coding Agents
- **Fragen:** Warum sind lange Prompts oft schlechter? / Wie decke ich unbekannte Annahmen auf?
- **Häufig in den Quellen:** prompt engineering (3), known unknowns (2), change quiz (2), skill descriptions (2), codex skill-creator (2), modellwechsel (2), gpt-6 astra (2), agents.md (2), progressive disclosure (2), überregulierung (2), risikoanalyse, spec grilling, sycophancy, prompt-tricks, ai agent zustimmungsneigung, projektplanung mit ai, pre-mortem prompt, frühwarnsignale, blind spot pass, spec-driven development

## Verwandte Themen

- [[Thema-Spezifikation-Planung]] — Spezifikation & Planung
- [[Thema-Agent-Dateien-Memory]] — Agent-Dateien & Memory
- [[Thema-Rolle-Lernen-Markt]] — Rolle, Lernen & Markt

## Patterns (3)

- [[Fable-Unknowns-vor-Prompt-Qualitaet]] · meinung · 3 Belege
- [[Intent-Engineering-als-dritte-Schicht]] · meinung · 4 Belege
- [[Voice-Prompting-fuer-Kontextreichtum]] · meinung · 3 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Entscheidung-per-Scoring-statt-Generierung]]

## Quellen (8)

- [[2026-09-22-claude-getting-the-most-out-of-opus-5-5-in-claude-and-c]] — Bei Opus 5.5 helfen ein klares Ziel, eine einzige Stopp-Bedingung und eine Task-Datei, die Kontext-Zusammenfassungen überlebt; weniger Stopps brauchen Gates.
- [[2026-09-19-voxyz_ai-2101355643882065971]] — Coding Agents führt man besser über Ergebnisverantwortung mit prüfbarem Endergebnis und Berichtspflicht als über Einzelschritte; der Reviewer läuft getrennt vom Implementierer.
- [[2026-09-14-developers-rethinking-skills-and-prompts-for-gpt-6-astra-op]] — Anweisungen veralten modellabhängig und schaden bei stärkeren Modellen aktiv; Skills als Router mit engen Triggern und schlanke AGENTS.md sind der Ausweg.
- [[2026-09-07-sairahul1-2096902575035683147]] — Alte Prompts, die Testen und Selbstprüfen erzwingen, schaden stärkeren Modellen; gesteuert werden sollten Autonomie, Prioritäten, Verifikationsumfang und prüfbare Stop-Bedingungen.
- [[2026-09-04-pvncher-2095991462416490862]] — Bei stärkeren Modellen werden angesammelte Skills und AGENTS.md-Regeln zum Ballast: Descriptions kurz und triggerbasiert halten, Pflichtlektüre und Rezepte streichen.
- [[2026-07-14-fredrikharkort-5-prompts-die-weh-tun]] — Prompts, die Rückfragen und unbequemes Feedback erzwingen, verbessern Entscheidungen, hängen aber davon ab, wie viel Kontext die KI über Person und Geschäft hat.
- [[2026-07-03-trq212-fable-field-guide-unknowns]] — Stärkere Modelle tragen falsche Annahmen selbstbewusst durch die Session; der Engpass ist die Spezifikation, daher Unknowns per Interview, Prototyp und Change Quiz heben.
- [[2026-05-02-vincentmumme-das-muesst-ihr-unbedingt-testen]] — Wer den Agenten aus der Rückschau auf ein gescheitertes Projekt argumentieren lässt, umgeht seine Zustimmungsneigung und deckt Risiken vor der Entwicklung auf.

## Quellen mit diesem Thema als Nebenthema

- [[2026-09-04-julian-ivanov-ki-automat-so-nutzt-du-claude-code-nach-anthropics-neuen-re]]
- [[2026-08-19-matt-pocock-live-uncle-bob-on-software-fundamentals-in-the-a]]
- [[2026-01-22-damien-lovable-website-guide]]
- [[2026-01-17-damien-ghader-prompting-lovable-design]]
