# Vergleich: Workflow-Frameworks

**Stand:** 2026-07-11

## Übersicht

| Framework/Pattern | Kernidee | Stärken | Schwächen | Quelle/Repo |
|---|---|---|---|---|
| mattpocock/skills | Kleine, komposierbare Einzel-Skills gegen vier typische KI-Entwicklungs-Fehlermodi; Kontrolle bleibt beim Menschen | Leichtgewichtig, modellunabhängig, leicht hackbar, klare user-/model-invoked-Trennung | Kein eingebautes Prozess-/State-Management; Gesamtworkflow muss selbst zusammengesetzt werden; `wayfinder` setzt einen externen Issue-Tracker voraus | `external_repos/INDEX.md` → mattpocock/skills |
| Superpowers (obra/superpowers) | Vollständige, weitgehend verpflichtende Entwicklungsmethodik als Skill-Kette: brainstorming → worktrees → writing-plans → TDD → Review → finishing | Sehr diszipliniert, TDD-first, strenge Qualitätskultur (94% PR-Ablehnungsquote), bereits im eigenen Environment aktiv genutzt (`superpowers:*`) | Verpflichtender/automatischer Ablauf lässt weniger Freiraum als der mattpocock-Ansatz; stark von einem einzelnen Autor/einer Philosophie geprägt | `external_repos/INDEX.md` → obra/superpowers |
| GSD Core (open-gsd/gsd-core) | Fünf-Phasen-Zyklus Discuss → Plan → Execute → Verify → Ship gegen „Context Rot“ | Adressiert gezielt Kontext-Verschlechterung über lange Sessions; frischer Kontext pro Executor-Subagent; `STATE.md`/`CONTEXT.md` überleben Session-Grenzen | Mehr Prozess-Overhead und Setup (interaktiver Runtime-Prompt, eigenes Tracking); laut mattpocock-Kritik potenziell weniger Nutzerkontrolle | `external_repos/INDEX.md` → open-gsd/gsd-core |
| gstack (garrytan/gstack) | Virtuelles Engineering-Team: 23 Rollen-Skills + 8 „Power Tools“ über vollen Sprintzyklus Think → Plan → Build → Review → Test → Ship → Reflect | Sehr umfassend (Security-Audits, Browser-QA mit echten Screenshots, projektübergreifendes GBrain-Wissen); rollenbasierte Reviews aus mehreren Perspektiven | Hoher Umfang/Komplexität (59 SKILL.md, 53 MB); vermutlich Overkill für kleine Projekte; viele bewegliche Teile zu warten | `external_repos/INDEX.md` → garrytan/gstack |
| addyosmani/agent-skills | 24 Lifecycle-Skills entlang Define → Plan → Build → Verify → Review → Ship, feste Anatomie mit Rationalizations-Tabelle und Red Flags | Sehr diszipliniert, explizite Anti-Rationalisierungs-Vorkehrungen, Google-Engineering-Praktiken eingebettet (Hyrum's Law, Chesterton's Fence u.a.), expliziter eigener Vergleich zu Superpowers/mattpocock vorhanden | Striktere, vorgegebene Anatomie evtl. weniger flexibel/hackbar als der mattpocock-Ansatz | `external_repos/INDEX.md` → addyosmani/agent-skills |
| Squad (bradygaster/squad) | Menschengeführtes Team benannter KI-Spezialisten als persistente Dateien (`.squad/`); autonomer „Watch Mode“ (Ralph) für GitHub-Issue-Polling | Nachvollziehbares Entscheidungsprotokoll (`decisions.md`); autonomes Issue-Polling mit vierstufiger Fehler-Eskalation; projektübergreifendes Lernen | Alpha-Software; kein statischer Skill-Ordner — Logik liegt in CLI-Quellcode, dadurch schwerer zu inspizieren/anzupassen als reine Markdown-Skills | `external_repos/INDEX.md` → bradygaster/squad |

## Empfehlungen

- Solo-Entwicklung/kleine Teams mit Wunsch nach Kontrolle über den Prozess: mattpocock/skills als Ausgangspunkt, da leichtgewichtig, modellunabhängig und ohne aufgezwungenen Gesamtworkflow.
- Lange Sessions oder große Codebasen mit Risiko von Kontext-Verschlechterung: Die GSD-Core-Ideen (frischer Subagent-Kontext pro Ausführungsschritt, persistente `STATE.md`) prüfen — unabhängig davon, ob das gesamte Framework übernommen wird.
- Teams, die durchgängige Disziplin und Nachvollziehbarkeit über den ganzen Lebenszyklus wollen (Anti-Rationalisierung, Red Flags, verpflichtende Reviews): addyosmani/agent-skills oder Superpowers als Vorbild.
- Umfangreiche, rollenbasierte Workflows mit Sicherheits-/QA-Gates über den vollen Sprintzyklus: gstack als Vorbild — Umfang gegen Wartungsaufwand abwägen.
- Autonomes Issue-Polling und persistente, benannte Agenten-Teams: Squad als Inspirationsquelle, Alpha-Status beachten.

## Offene Fragen

- Ab welcher Projekt-/Teamgröße überwiegt der Vorteil eines „process-owning“ Frameworks (GSD, gstack) gegenüber der Kontrolle bei kleinen, komponierbaren Skills (mattpocock)? Siehe Spannung in [[Klein-und-komposierbar]].
- Lässt sich mattpococks user-/model-invoked-Hierarchie mit GSDs Phasen-Subagenten kombinieren, ohne die Einfachheit des kleinen Ansatzes zu verlieren?
- Keiner der Frameworks wurde bisher im eigenen Environment produktiv getestet — alle Einschätzungen in dieser Tabelle stammen aus Repo-Struktur/README-Analyse (`external_repos/INDEX.md`), nicht aus eigener Nutzung. Konfidenz „verifiziert“ im Sinne von „selbst getestet“ steht für diesen Vergleich insgesamt noch aus.
