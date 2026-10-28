# Prompting & Klärung

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-28. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Wie man dem Modell Absicht und Wissen gibt: Prompt-Technik, Pre-Mortem, Unknowns, Voice-Prompting, Anweisungen bei Modellwechsel ausdünnen, Anti-Sycophancy.

## Suchbegriffe

- **Hauptkeyword:** Prompt Engineering
- **Long-Tail:** Pre-Mortem Prompt; Unknowns aufdecken Prompt; Voice Prompting Coding; Anweisungen bei Modellwechsel ausdünnen; Agent Sycophancy vermeiden; Prompt für Coding Agents
- **Fragen:** Warum sind lange Prompts oft schlechter? / Wie decke ich unbekannte Annahmen auf?
- **Häufig in den Quellen:** prompt engineering (3), agents.md (3), spec-grilling (2), known unknowns (2), change quiz (2), voice prompting (2), codex skill-creator (2), progressive disclosure (2), gpt-6 astra (2), überregulierung (2), modellwechsel (2), skill descriptions (2), intent engineering (2), ambitionscheck (2), context engineering (2), pre-mortem prompt, prompt-tricks, risikoanalyse, frühwarnsignale, projektplanung mit ai

## Verwandte Themen

- [[Thema-Spezifikation-Planung]] — Spezifikation & Planung
- [[Thema-Agent-Dateien-Memory]] — Agent-Dateien & Memory
- [[Thema-Rolle-Lernen-Markt]] — Rolle, Lernen & Markt
- [[Thema-Prompts-zum-Ausprobieren]] — Prompts zum Ausprobieren

## Patterns (4)

- [[Ambitionscheck-mit-Zielhoehe-Tiefe-und-Reichweite]] · meinung · 2 Belege
- [[Fable-Unknowns-vor-Prompt-Qualitaet]] · meinung · 3 Belege
- [[Intent-Engineering-als-dritte-Schicht]] · meinung · 12 Belege
- [[Voice-Prompting-fuer-Kontextreichtum]] · meinung · 4 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Entscheidung-per-Scoring-statt-Generierung]], [[Handlungsbedarf-zuerst-im-Agent-Bericht]]

## Quellen (13)

- [[2026-10-23-voxyz_ai-2113632785759973649]] — Vox schlägt eine Agent-Regel gegen ungefragte Absicherung unwahrscheinlicher Race Conditions und Security-Sonderfälle vor: Der Agent soll Schaden, Wahrscheinlichkeit und zusätzliche Komplexität verstä
- [[2026-10-19-promptgefluester-wir-neigen-dazu-dass-wir-beim-aehm-prompting-der-ki-sagen-aehm-8]] — Der Autor warnt, dass wenige genannte Beispiele eine Recherche unbeabsichtigt verengen können.
- [[2026-10-13-felixrieseberg-how-to-be-more-ambitious-a-tutorial-for-humans-w]] — Felix Rieseberg schlägt vor, KI nicht nur für schnellere Ausführung einzusetzen, sondern Aufgaben auf drei weitere Arten anspruchsvoller zu gestalten: am übergeordneten Ergebnis ausrichten, mit besser
- [[2026-09-28-vincentmumme-prompt-engineering-ist-schon-lange-tot-und-ich-weiss-nicht-ob-ihr-euch]] — Vincent Mumme erläutert am 28.09.2026 ein Agenten-Promptschema.
- [[2026-09-22-claude-getting-the-most-out-of-opus-5-5-in-claude-and-c]] — Bei Opus 5.5 helfen ein klares Ziel, eine einzige Stopp-Bedingung und eine Task-Datei, die Kontext-Zusammenfassungen überlebt; weniger Stopps brauchen Gates.
- [[2026-09-14-developers-rethinking-skills-and-prompts-for-gpt-6-astra-op]] — Anweisungen veralten modellabhängig und schaden bei stärkeren Modellen aktiv; Skills als Router mit engen Triggern und schlanke AGENTS.md sind der Ausweg.
- [[2026-09-07-sairahul1-2096902575035683147]] — Alte Prompts, die Testen und Selbstprüfen erzwingen, schaden stärkeren Modellen; gesteuert werden sollten Autonomie, Prioritäten, Verifikationsumfang und prüfbare Stop-Bedingungen.
- [[2026-09-05-waynesutton-2096296858343846261]] — Wayne Sutton empfiehlt einen Prompt, der Entscheidungen zugleich an User Experience, Developer Experience und Agent Experience ausrichtet.
- [[2026-09-04-pvncher-2095991462416490862]] — Bei stärkeren Modellen werden angesammelte Skills und AGENTS.md-Regeln zum Ballast: Descriptions kurz und triggerbasiert halten, Pflichtlektüre und Rezepte streichen.
- [[2026-09-04-guinnesschen-2095920936172335278]] — Guinness Chen kündigt am 04.09.2026 an, dass Voice in bestehenden `Codex`-Chats verfügbar ist.
- [[2026-07-14-fredrikharkort-5-prompts-die-weh-tun]] — Prompts, die Rückfragen und unbequemes Feedback erzwingen, verbessern Entscheidungen, hängen aber davon ab, wie viel Kontext die KI über Person und Geschäft hat.
- [[2026-07-03-trq212-2073100352921215386]] — Die Qualität langer Fable-Aufgaben hängt laut Thariq daran, die Unknowns zwischen Prompt und Codebasis zu klären; Techniken vor, während und nach der Umsetzung, vom Blind Spot Pass bis zum Quiz vor dem Merge.
- [[2026-05-02-vincentmumme-das-muesst-ihr-unbedingt-testen]] — Wer den Agenten aus der Rückschau auf ein gescheitertes Projekt argumentieren lässt, umgeht seine Zustimmungsneigung und deckt Risiken vor der Entwicklung auf.

## Quellen mit diesem Thema als Nebenthema

- [[2026-10-05-voxyz_ai-2107123654219743712]]
- [[2026-09-19-voxyz_ai-2101355643882065971]]
- [[2026-09-04-julian-ivanov-ki-automat-so-nutzt-du-claude-code-nach-anthropics-neuen-re]]
- [[2026-08-19-matt-pocock-live-uncle-bob-on-software-fundamentals-in-the-a]]
- [[2026-07-31-alex-sprogis-dieser-claude-code-skill-ist-genial]]
- [[2026-01-22-damien-lovable-website-guide]]
- [[2026-01-17-damien-ghader-prompting-lovable-design]]
- [[2025-06-23-boristane-context-engineering-is-what-makes-ai-magical]]
