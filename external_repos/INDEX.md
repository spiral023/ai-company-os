# Index externer Repos

Dieser Index wird gemäß `AGENTS.md` → „Fremde GitHub-Repos herunterladen" gepflegt. Ordner `external_repos/` ist nicht versioniert (siehe `.gitignore`) und nicht im Obsidian-Vault sichtbar (siehe `.obsidian/app.json`). Ziel: anhand dieser Zusammenfassungen später effizient passende Repos empfehlen und Arbeitsweisen/Infos extrahieren, ohne erneut klonen zu müssen.

Ordnerstruktur seit 2026-07-10: `external_repos/<owner>/<repo-name>/` (Owner als Unterordner, um Namenskollisionen zu vermeiden).

<!-- OVERVIEW:START (automatisch generiert von 70_Scripts/update_external_repos.py — nicht von Hand bearbeiten) -->
## Übersicht

- **Repos gesamt:** 22
- **Gesamtgröße:** ca. 415 MB
- **Dateien gesamt:** ca. 20.664 (ohne `.git`)
- **Stand:** 2026-07-11

| Repo | Dateien | Größe |
|---|---:|---:|
| pbakaus/impeccable | 2.201 | 77M |
| shanraisshan/claude-code-best-practice | 454 | 74M |
| garrytan/gstack | 1.170 | 53M |
| affaan-m/ECC | 3.322 | 44M |
| Egonex-AI/Understand-Anything | 469 | 31M |
| alirezarezvani/claude-skills | 4.606 | 29M |
| open-gsd/gsd-core | 2.477 | 28M |
| bradygaster/squad | 1.747 | 19M |
| nextlevelbuilder/ui-ux-pro-max-skill | 482 | 13M |
| OthmanAdi/planning-with-files | 424 | 12M |
| anthropics/skills | 415 | 10M |
| vercel-labs/agent-skills | 442 | 7,5M |
| wshobson/agents | 1.094 | 7,3M |
| AgriciDaniel/claude-seo | 364 | 3,8M |
| coreyhaines31/marketingskills | 416 | 3,1M |
| Leonxlnx/taste-skill | 56 | 1,6M |
| obra/superpowers | 172 | 1,3M |
| vercel-labs/skills | 96 | 798K |
| addyosmani/agent-skills | 126 | 665K |
| mattpocock/skills | 114 | 450K |
| emilkowalski/skills | 8 | 84K |
| shadcn/improve | 9 | 61K |

Dateianzahl, Größe und Struktur pro Repo (ohne `.git`-Verzeichnis) stehen zusätzlich in jedem Eintrag unten und werden von `70_Scripts/update_external_repos.py` automatisch aufgefrischt.
<!-- OVERVIEW:END -->

---

## mattpocock/skills

- **URL:** https://github.com/mattpocock/skills
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-11
- **Dateien:** 114 · **Größe:** 450K
- **Struktur:** 39× SKILL.md · Ordner: skills

Sammlung von Agent-Skills von Matt Pocock (AI Hero), die er täglich für echte Softwareentwicklung nutzt – bewusst als Gegenentwurf zu "Vibe Coding" und prozess-diktierenden Frameworks wie GSD, BMAD oder Spec-Kit. Die Skills sind klein, modular, modellunabhängig und adressieren vier typische Fehlerquellen bei KI-gestützter Entwicklung: (1) Missverständnis zwischen Nutzer und Agent, gelöst durch "Grilling"-Sessions (`grill-me`, `grill-with-docs`), die den Agenten vor der Umsetzung gezielt nachfragen lassen; (2) zu weitschweifige Agenten, gelöst durch eine geteilte Fachsprache in einem `CONTEXT.md`-Dokument; (3) nicht funktionierender Code, gelöst durch strikte Test-Driven-Development- und Debugging-Skills (`tdd`, `diagnosing-bugs`); (4) architektonischer Verfall ("Ball of Mud"), adressiert durch `improve-codebase-architecture`. Skills sind in zwei Kategorien gegliedert: Engineering (Code-Arbeit) und Productivity (allgemeine Workflows), jeweils unterteilt in user-invoked (nur per Slash-Command aufrufbar, orchestrierend) und model-invoked (auch automatisch vom Agenten genutzt, enthalten die eigentliche Disziplin). Relevant als Vorbild für strukturierte, disziplinierte Engineering-Skills mit klarer Trennung von Orchestrierung und wiederverwendbarer Logik.

---

## affaan-m/ECC

- **URL:** https://github.com/affaan-m/ECC
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-10
- **Dateien:** 3.322 · **Größe:** 44M
- **Struktur:** 278× SKILL.md · Ordner: skills, agents, commands, hooks, rules, plugins, references · Spiegelordner: .agents, .claude, .codex, .cursor, … (+2) (generiert)

ECC ("Agent Harness Operating System") ist ein sehr umfangreiches Claude-Code-Plugin-System eines Einzelentwicklers, das über 10+ Monate produktiven Einsatzes gewachsen ist und über sieben Agent-Harnesses (Claude Code, Cursor, Codex, OpenCode, Gemini, Zed, GitHub Copilot) hinweg funktioniert. Es bündelt ~67 spezialisierte Subagenten (Planner, Architect, Code-Reviewer, Security-Reviewer u.v.m.), ~278 Skills (Coding-Standards für 12+ Sprachökosysteme, Backend-/Frontend-Patterns, Content-/Marketing-Skills, ML-Workflows), Hooks für Memory-Persistenz zwischen Sessions, ein instinkt-basiertes kontinuierliches Lernsystem, Verifikations-/Eval-Loops sowie einen eigenen Security-Auditor (AgentShield, OWASP-artige Scans von Claude-Konfigurationen). Installierbar als Plugin, npm-Paket oder manuell; bietet zusätzlich eine kostenpflichtige "ECC Pro"-Stufe für private Repos. Das Repo dokumentiert explizit Fallstricke bei Mehrfachinstallation (Plugin + manueller Installer gleichzeitig führt zu Duplikaten) und pflegt ein detailliertes Änderungsprotokoll. Relevant als Referenz für Skalierung eines Skill-/Agenten-Ökosystems über viele Sprachen und Harnesses hinweg, für Memory-Persistenz-Hooks und für strukturierte Sicherheits-Audits von Agent-Konfigurationen.

---

## garrytan/gstack

- **URL:** https://github.com/garrytan/gstack
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-11
- **Dateien:** 1.170 · **Größe:** 53M
- **Struktur:** 59× SKILL.md · Ordner: skills, agents, hooks, references

gstack ist Garry Tans (Präsident/CEO von Y Combinator) persönliches Open-Source-System, das Claude Code in ein virtuelles Engineering-Team verwandelt: 23 Rollen-Skills und 8 "Power Tools" bilden einen kompletten Sprint-Zyklus ab – Think → Plan → Build → Review → Test → Ship → Reflect. Zentrale Skills: `/office-hours` (Produktinterview mit gezielten Rückfragen, erzeugt Design-Doc), `/plan-ceo-review`/`/plan-eng-review`/`/plan-design-review`/`/plan-devex-review` (mehrstufige Planbewertung aus verschiedenen Rollen-Perspektiven), `/design-shotgun` (KI-generierte Mockup-Varianten mit Geschmacks-Lernen), `/review` und `/qa` (automatisierte Code- und Browser-Tests mit echten Screenshots), `/cso` (OWASP+STRIDE-Sicherheitsaudit), `/ship`/`/land-and-deploy` (Test, PR, Deployment, Monitoring). Ergänzt durch GBrain, eine persistente, projektübergreifende Wissensdatenbank für Agenten, sowie ausgefeilte Sicherheitsmechanismen gegen Prompt-Injection im Browser-Modus. Funktioniert nicht nur mit Claude Code, sondern auch mit Codex, Cursor, OpenCode u.a. MIT-lizenziert, sehr aktiv gepflegt (detailliertes Architektur- und Sicherheitsdokument). Relevant als Vorbild für einen vollständigen, rollenbasierten Entwicklungs-Workflow mit Review-Gates und Browser-QA.

---

## coreyhaines31/marketingskills

- **URL:** https://github.com/coreyhaines31/marketingskills
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-11
- **Dateien:** 416 · **Größe:** 3,1M
- **Struktur:** 47× SKILL.md · Ordner: skills, references

Sammlung von rund 47 Marketing-Skills für KI-Coding-Agenten (Claude Code, Codex, Cursor, Windsurf) von Corey Haines (Conversion Factory, Swipe Files). Deckt praktisch das gesamte technische Marketing ab: SEO & Content (seo-audit, ai-seo, programmatic-seo, schema), Conversion-Optimierung (cro, signup, onboarding, popups, paywalls), Content & Copy (copywriting, cold-email, emails, social, video), bezahlte Kanäle (ads, ad-creative), Messung (analytics, ab-testing), Retention (churn-prevention), Wachstum (co-marketing, free-tools, referrals) sowie Strategie/Sales (pricing, launch, revops, sales-enablement). Alle Skills referenzieren ein zentrales `product-marketing`-Kontextdokument, das Produkt, Zielgruppe und Positionierung festhält und von jedem anderen Skill zuerst gelesen wird – ein Muster, um wiederholte Grundinformationen zu vermeiden. Skills sind stark querverweisend (z.B. copywriting ↔ cro ↔ ab-testing). Installierbar über npx skills, Claude-Code-Plugin, Git-Submodule oder einfaches Kopieren. Sehr relevant als direktes Vorbild für die eigenen Marketing-bezogenen Skills unter `30_Skills/`, insbesondere das Muster eines zentralen Produkt-Kontext-Dokuments, das andere Skills referenzieren.

---

## Leonxlnx/taste-skill

- **URL:** https://github.com/Leonxlnx/taste-skill
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-10
- **Dateien:** 56 · **Größe:** 1,6M
- **Struktur:** 13× SKILL.md · Ordner: skills

"Anti-Slop Frontend Framework" – eine Sammlung portabler Agent-Skills, die die visuelle Qualität von KI-generierten Frontends verbessern sollen (Layout, Typografie, Bewegung, Abstände), statt generisch wirkender Standard-UIs. Enthält mehrere Implementierungs-Varianten für unterschiedliche Stilrichtungen: das Standard-`taste-skill` (v2, mit einstellbaren Reglern für Layout-Varianz, Bewegungsintensität und visuelle Dichte), eine strengere GPT/Codex-Variante, sowie spezialisierte Stile (minimalistisch, brutalistisch, "soft"/hochwertig), zusätzlich ein Skill zur Überarbeitung bestehender Projekte (`redesign-skill`) und eines gegen abgeschnittene/unvollständige Ausgaben. Ergänzend gibt es reine Bildgenerierungs-Skills (Website-Mockups, Mobile-Screens, Brand-Kits) zur Nutzung mit Bildgeneratoren wie ChatGPT Images, deren Ergebnisse dann an Coding-Agenten übergeben werden. Framework-agnostisch (React, Vue, Svelte). Installierbar über `npx skills add`. Relevant als Referenz für konkrete, anwendbare Stilregeln gegen generisch wirkende KI-UIs sowie für das Muster "Bildgenerierung zur Referenz, dann Code-Umsetzung".

---

## shadcn/improve

- **URL:** https://github.com/shadcn/improve
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-10
- **Dateien:** 9 · **Größe:** 61K
- **Struktur:** 1× SKILL.md · Ordner: skills, references

Kleiner, fokussierter Agent-Skill von shadcn: auditiert eine beliebige Codebasis mit einem leistungsstarken (teuren) Modell und schreibt daraus präzise, in sich geschlossene Umsetzungspläne, die anschließend von günstigeren Modellen oder anderen Agenten ausgeführt werden können. Der Skill implementiert selbst nie Code – "der Plan ist das Produkt". Ablauf: Recon (Repo-Struktur, Build/Test/Lint-Befehle, vorhandene ADRs/PRDs erfassen) → Audit (parallele Subagenten über neun Kategorien: Korrektheit, Sicherheit, Performance, Testabdeckung, technische Schulden, Abhängigkeiten, Developer Experience, Doku, Richtung/Feature-Vorschläge) → Vet (Advisor prüft jeden gemeldeten Fund selbst nach, verwirft Fehlalarme) → Priorisierung (Impact/Aufwand) → Plan-Erstellung (eine Datei pro gewähltem Finding, mit exakten Dateipfaden, Code-Ausschnitten, Verifikationsbefehlen und klaren Grenzen). Kann Pläne auch direkt an einen günstigeren Executor-Agenten in einem isolierten Git-Worktree übergeben und dessen Ergebnis wie ein Tech Lead gegenprüfen, oder Pläne als GitHub Issues veröffentlichen. Relevant als schlankes Vorbild für Audit-zu-Plan-Workflows mit klarer Trennung zwischen teurem Planungsmodell und günstigem Ausführungsmodell.

---

## bradygaster/squad

- **URL:** https://github.com/bradygaster/squad
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-11
- **Dateien:** 1.747 · **Größe:** 19M
- **Struktur:** kein statischer Skill-Ordner mit Inhalt — die eigentliche Logik ist CLI-Quellcode in `packages/squad-cli/`, `packages/squad-sdk/`; Vorlagen in `templates/skills/`; erzeugt zur Laufzeit `.squad/agents/` + `.squad/skills/` im Zielprojekt <!-- manual -->

Squad baut über GitHub Copilot ein "menschengeführtes" Team benannter KI-Spezialisten (Frontend, Backend, Tester, Lead etc.) auf, die als Dateien im Repo (`.squad/`) persistieren, projektübergreifendes Wissen ansammeln und über Sessions hinweg lernen. Nutzer beschreiben ihr Vorhaben, Squad schlägt ein Team vor, das dann parallel an Aufgaben arbeitet; alle Entscheidungen werden nachvollziehbar in `decisions.md` protokolliert. Besonderheit ist der "Watch Mode" (genannt Ralph): ein Polling-Prozess, der GitHub Issues überwacht, priorisiert, Kontext an einen Copilot-Agenten übergibt und diesem die Auswahl überlässt, mit einer vierstufigen Fehler-Eskalation (Circuit-Breaker-Reset, Auth-Reprobe, Git-Pull, Pause mit Eskalation an Menschen). Alpha-Software, Node.js-Monorepo mit SDK- und CLI-Paket, auch als programmierbares TypeScript-Setup (`squad.config.ts`) nutzbar. Ausdrücklich als Produktivitätswerkzeug positioniert, das Menschen nicht ersetzt, sondern Koordination und Wiederholung abnimmt. Relevant als Vorbild für persistente, benannte Agenten-Teams mit Entscheidungsprotokoll und autonomem Issue-Polling mit Eskalationsstufen.

---

## obra/superpowers

- **URL:** https://github.com/obra/superpowers
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-10
- **Dateien:** 172 · **Größe:** 1,3M
- **Struktur:** 14× SKILL.md · Ordner: skills, hooks, references · Spiegelordner: .agents, .opencode (generiert)

Superpowers ist eine vollständige Softwareentwicklungs-Methodik als Satz komponierbarer Skills von Jesse Vincent (Prime Radiant), verfügbar für praktisch alle gängigen Coding-Agenten (Claude Code, Antigravity, Codex, Cursor, Factory Droid, GitHub Copilot CLI, Kimi Code, OpenCode, Pi). Der Kern-Workflow läuft automatisch und verpflichtend ab, sobald der Agent erkennt, dass etwas gebaut werden soll: `brainstorming` (sokratisches Nachfragen statt sofortigem Coden) → `using-git-worktrees` (isolierter Branch) → `writing-plans` (kleinteilige, präzise Aufgaben) → `subagent-driven-development`/`executing-plans` (Ausführung mit zweistufigem Review) → `test-driven-development` (striktes Red-Green-Refactor) → `requesting-code-review`/`receiving-code-review` → `finishing-a-development-branch`. Philosophie: Test-Driven Development, systematisches statt Ad-hoc-Vorgehen, Einfachheit, Belege statt Behauptungen. Das Projekt hat auffällig strenge Beitragsregeln (94% PR-Ablehnungsquote, Pflicht zur Offenlegung von Modell/Harness bei Beiträgen, Verbot von Fremd-Abhängigkeiten und domänenspezifischen Skills im Core). Direkt relevant, da dieses Skill-Set bereits im eigenen Environment als `superpowers:*` aktiv genutzt wird – gutes Referenzmaterial für eigene Skill-Disziplin und PR-Qualitätsstandards.

---

## OthmanAdi/planning-with-files

- **URL:** https://github.com/OthmanAdi/planning-with-files
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-10
- **Dateien:** 424 · **Größe:** 12M
- **Struktur:** 6× SKILL.md · Ordner: skills, commands · Spiegelordner: .codebuddy, .codex, .continue, .cursor, … (+8) (generiert)

"Planning with Files" ist ein dateibasierter Planungs-Skill, der dem Muster von Manus (der für 2 Mrd. USD von Meta übernommenen Agentenfirma) folgt: Für jede komplexe Aufgabe legt der Agent drei persistente Markdown-Dateien an – `task_plan.md` (Phasen/Fortschritt), `findings.md` (Rechercheergebnisse) und `progress.md` (Session-Log). Kernprinzip: Das Kontextfenster ist wie flüchtiges RAM, das Dateisystem wie persistente Festplatte – alles Wichtige wird auf Platte geschrieben statt im Kontext zu verbleiben. Hooks lesen den Plan vor wichtigen Entscheidungen erneut ein (PreToolUse), erinnern nach Datei-Schreibvorgängen an Status-Updates (PostToolUse) und verifizieren Vollständigkeit vor dem Stoppen (Stop-Hook). Damit übersteht der Agent Kontextverlust, `/clear` und Abstürze und erholt sich automatisch (Session Recovery). Läuft über 60+ Agenten/IDEs hinweg (Claude Code, Codex, Cursor, Gemini CLI u.v.m.) via SKILL.md-Standard, inkl. mehrsprachiger Varianten. Laut eigener Evaluation (Anthropics skill-creator-Framework) steigt die Aufgaben-Erfolgsquote von 6,7% ohne auf 96,7% mit Skill. Neu in v3.0.0: optionale autonome und "gated" Modi mit einem Completion-Gate, das den Agenten erst stoppen lässt, wenn der Plan tatsächlich fertig ist. Sehr relevant als konkretes, breit erprobtes Muster für strukturierte Notizen/Planpersistenz gegen Kontext-Rot.

---

## anthropics/skills

- **URL:** https://github.com/anthropics/skills
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-10
- **Dateien:** 415 · **Größe:** 10M
- **Struktur:** 18× SKILL.md · Ordner: skills, agents, references

Das offizielle Anthropic-Repository mit Referenz-Implementierungen für das Claude-Skills-System. Enthält Beispiel-Skills für kreative Anwendungen (Kunst, Musik, Design), technische Aufgaben (Web-App-Testing, MCP-Server-Generierung) sowie Unternehmens-Workflows (Kommunikation, Branding). Besonders relevant: die Dokument-Skills (`skills/docx`, `skills/pdf`, `skills/pptx`, `skills/xlsx`), die tatsächlich Claudes Dokumentenerstellung in Produktion antreiben – "source-available", nicht Open Source, aber als Referenz für komplexe, produktiv genutzte Skills freigegeben. Das Repo dient explizit als Inspirationsquelle und Muster-Referenz, nicht als garantiertes Abbild von Claudes tatsächlichem Verhalten. Enthält außerdem die Agent-Skills-Spezifikation (`spec/`) und ein minimales Skill-Template (`template/`) mit den zwei Pflichtfeldern im YAML-Frontmatter (`name`, `description`). Installierbar als Claude-Code-Plugin-Marketplace (`document-skills`, `example-skills`), in Claude.ai direkt nutzbar, oder über die Claude API hochladbar. Als "Quelle der Wahrheit" für das Skill-Format und als Referenz für gut strukturierte, offizielle Beispiel-Skills die mit Abstand wichtigste Referenz unter allen geladenen Repos.

---

## open-gsd/gsd-core

- **URL:** https://github.com/open-gsd/gsd-core
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-11
- **Dateien:** 2.477 · **Größe:** 28M
- **Struktur:** 71× SKILL.md · Ordner: skills, agents, commands, hooks, references · Spiegelordner: .opencode (generiert)

GSD Core ("Git. Ship. Done.") ist ein schlankes Context-Engineering- und Spec-driven-Development-Framework, das KI-Coding-Agenten (Claude Code, OpenCode, Antigravity CLI, Kimi CLI, Kilo, Codex, Copilot, Cursor, Windsurf u.a.) durch einen disziplinierten Fünf-Schritte-Phasenzyklus führt: Discuss (Entscheidungen vor der Planung festhalten) → Plan (Recherche, Zerlegung, Prüfung dass der Plan in ein frisches Kontextfenster passt) → Execute (Pläne in parallelen Wellen ausführen, jeder Executor startet mit sauberem 200k-Token-Kontext) → Verify (Durchgehen was gebaut wurde, Fixes vor "fertig") → Ship (PR erstellen, Phase archivieren, nächste Phase). Löst damit gezielt "Context Rot" – die Qualitätsverschlechterung, die sich aufbaut, während ein Agent sein Kontextfenster füllt – indem schwere Arbeit in frischen Subagenten läuft, während die Hauptsession schlank bleibt. Strukturierte Artefakte wie `STATE.md` und `CONTEXT.md` überleben Session-Grenzen. Installation über `npx @opengsd/gsd-core@latest` mit interaktivem Runtime-Prompt; Einstieg über `/gsd-new-project` (Neuprojekt) oder `/gsd-onboard` (bestehende Codebasis). Relevant als alternatives, sehr fokussiertes Muster zum eigenen mehrstufigen Workflow-Ansatz, insbesondere die "frischer Kontext pro Executor"-Idee.

---

## vercel-labs/skills

- **URL:** https://github.com/vercel-labs/skills
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-11
- **Dateien:** 96 · **Größe:** 798K
- **Struktur:** kein Skill-Inhalt — das ist die Installer-CLI selbst, Quellcode in `src/` <!-- manual -->

Das ist keine Skill-Sammlung, sondern die CLI (`npx skills`) für das offene Agent-Skills-Ökosystem – das zugrundeliegende Werkzeug, mit dem Skills aus beliebigen GitHub-/GitLab-Repos oder lokalen Pfaden in über 70 unterstützte Coding-Agenten (Claude Code, Cursor, Codex, OpenCode, Windsurf, Antigravity, Gemini CLI, GitHub Copilot u.v.m.) installiert werden – per Symlink (empfohlen, eine kanonische Kopie) oder Kopie, projekt- oder global-scoped. Zentrale Befehle: `skills add <source>` (installieren, mit Filtern nach Skill-Namen/Agenten), `skills use <source>` (Skill ohne Installation testen, druckt generierten Prompt oder startet Agent direkt), `skills list`, `skills find` (interaktive/keyword-Suche, auch über alle Repos eines Owners), `skills update`, `skills remove`, `skills init` (neues SKILL.md-Template). Erkennt Skills automatisch über verschiedene Ablage-Konventionen (`skills/`, `.claude/skills/`, Root-`SKILL.md` etc.) inkl. Claude-Plugin-Marketplace-Manifesten. Über die Website skills.sh können Skills durchsucht werden. Sehr relevant als das faktische Standard-Werkzeug, mit dem praktisch alle anderen in diesem Index gelisteten Skill-Repos installiert werden – guter Kandidat, um das eigene Skill-Handling zu vereinheitlichen.

---

## AgriciDaniel/claude-seo

- **URL:** https://github.com/AgriciDaniel/claude-seo
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-10
- **Dateien:** 364 · **Größe:** 3,8M
- **Struktur:** 33× SKILL.md · Ordner: skills, agents, hooks, references

Claude SEO ist ein Open-Source-SEO-Analyse-Plugin für Claude Code, das 25 Sub-Skills und 18 spezialisierte Subagenten parallel über technische SEO, Content-Qualität (E-E-A-T), Schema.org-Markup, KI-Suchoptimierung (GEO), lokale SEO, E-Commerce und internationale SEO laufen lässt. Jeder Audit erzeugt einen priorisierten, testbaren Maßnahmenplan, der auf Primärquellen (Google-Dokumentation) beruht statt auf Vermutungen – jede Empfehlung trägt explizit die zugrunde liegende Beobachtung, Abhängigkeiten zu anderen Empfehlungen, einen "woran erkennen wir das Scheitern?"-Check und einen Frühindikator. Zentrale Befehle: `/seo audit`, `/seo page`, `/seo schema`, `/seo geo`, `/seo technical`, `/seo local`, `/seo sitemap` u.v.m. Vollständige Site-Audits laufen mit bis zu 15 parallelen Agenten in 10–15 Minuten statt Stunden. Vierstufiges Credential-System erlaubt Start ohne jegliche API-Keys, mit optionalem Ausbau (PageSpeed/CrUX, Search Console, GA4, Keyword Planner). Erweiterbar durch MCP-Extensions (DataForSEO, Firecrawl, Ahrefs, SE Ranking, Profound, Bing Webmaster, Unlighthouse, Bildgenerierung). Sehr relevant als direktes fachliches Gegenstück/Vorbild zum `seo`-Skill-Bereich im eigenen Environment – deutlich tiefer ausgebaut mit konkreten Python-Skripten, Falsifizierbarkeits-Prinzip und Google-API-Integration.

---

## nextlevelbuilder/ui-ux-pro-max-skill

- **URL:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-11
- **Dateien:** 482 · **Größe:** 13M
- **Struktur:** Quelle der Wahrheit in `src/ui-ux-pro-max/` (`data/`, `scripts/`, `templates/`), Installer in `cli/`, Dev-Kopie in `.claude/skills/` <!-- manual -->

"UI UX Pro Max" ist ein KI-Skill, der Design-Intelligenz für professionelles UI/UX über mehrere Plattformen und Frameworks bereitstellt: durchsuchbare Datenbanken mit 67 UI-Stilen (Glassmorphism, Neumorphism, Brutalism, Bento Grid, AI-Native UI u.v.m.), 161 Farbpaletten (1:1 auf 161 Produkttypen abgestimmt), 57 Schriftpaarungen, 25 Chart-Typen und 99 UX-Richtlinien. Kernstück von v2.0 ist der Design-System-Generator: eine Reasoning-Engine, die aus einer Produktbeschreibung (z.B. "Beauty-Spa-Landingpage") automatisch ein komplettes, begründetes Design-System ableitet – Seitenstruktur, Stil, Farben, Typografie, Effekte, Anti-Pattern-Warnungen und eine Vorab-Auslieferungs-Checkliste (Kontrast, Fokus-States, Responsive-Breakpoints etc.). Nutzt eine BM25-Suchmaschine über CSV-Datenbanken und unterstützt 22 Tech-Stacks (React, Next.js, Vue, SwiftUI, Flutter, Laravel u.v.m.). Design-Systeme können projektübergreifend als Master+Override-Dateien persistiert werden. Aktiviert sich automatisch bei UI/UX-Anfragen in unterstützten Agenten oder per Slash-Command in anderen. Es gibt eine kostenlose Basis- und eine kostenpflichtige Premium-Version (Branding, Logo, Assets). Relevant als konkretes, datengetriebenes Gegenstück zu den eher stilistischen `taste-skill`-Ansätzen – hier mit strukturierten Entscheidungsregeln statt reiner Stilbeschreibung.

---

## shanraisshan/claude-code-best-practice

- **URL:** https://github.com/shanraisshan/claude-code-best-practice
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-11
- **Dateien:** 454 · **Größe:** 74M
- **Struktur:** kein Skill-Paket, sondern Wissensbasis: `best-practice/`, `reports/`, `tips/` (die eigentlichen Inhalte); Demo-Setup in `.claude/agents/`, `.claude/commands/`, `.claude/skills/` <!-- manual -->

Eine sehr umfangreiche, laufend aktualisierte Sammlung von Claude-Code-Best-Practices ("from vibe coding to agentic engineering"): keine Skill-Sammlung, sondern eine kuratierte Wissensbasis über Subagenten, Commands, Skills, Hooks, MCP-Server, Settings, Memory, Worktrees u.v.m., mit Verweisen auf offizielle Doku und eigenen Implementierungsbeispielen (u.a. ein Wetter-Demo-Workflow nach dem Muster Command → Agent → Skill). Besonders wertvoll: eine vergleichende Tabelle konkurrierender Entwicklungs-Workflow-Methodologien (Superpowers, ECC, Matt-Pocock-Skills, gstack, Spec Kit, GSD, BMAD-METHOD u.a.) mit Stern-Zahlen und Schritt-für-Schritt-Ablauf, sowie separate Tabellen für reine Skill- und Agenten-Sammlungen. Enthält zudem 83 gesammelte "Tips and Tricks" aus der Community (u.a. von Boris Cherny, Mitentwickler von Claude Code) zu Prompting, Planung, Kontextmanagement, Session-Handling, CLAUDE.md-Gestaltung, Hooks, Git/PR-Workflow und Debugging – z.B. "Context Rot setzt bei ~300-400k Tokens ein" oder "PRDs in vertikale Slices statt horizontale Phasen zerlegen". Sehr relevant als Meta-Referenz: liefert sowohl konkrete, sofort anwendbare Tipps als auch eine Landkarte weiterer relevanter Repos, von denen einige bereits im eigenen Index enthalten sind.

---

## vercel-labs/agent-skills

- **URL:** https://github.com/vercel-labs/agent-skills
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-10
- **Dateien:** 442 · **Größe:** 7,5M
- **Struktur:** 9× SKILL.md · Ordner: skills, rules, references

Kompakte, von Vercel Engineering kuratierte Sammlung von acht Skills nach dem Agent-Skills-Standard: `vercel-optimize` (Audit von Vercel-Projekten auf Kosten/Performance/Caching/Function-Nutzung), `react-best-practices` (40+ priorisierte React/Next.js-Performance-Regeln in 8 Kategorien, z.B. Waterfall-Vermeidung, Bundle-Size), `web-design-guidelines` (100+ Regeln zu Accessibility, Fokus-States, Formularen, Animation, Typografie, Dark Mode), `writing-guidelines` (80+ Regeln aus dem Vercel-Schreibhandbuch zu Tonalität, Struktur, Code-Beispielen, Typografie), `react-native-guidelines` (16 Regeln zu Performance/Architektur für React Native/Expo), `react-view-transitions` (React View Transition API, Next.js-Integration), `composition-patterns` (React-Komposition statt Boolean-Prop-Wildwuchs) und `vercel-deploy-claimable` (sofortiges Deployment aus der Konversation heraus, mit übertragbarer Ownership). Installation einheitlich über `npx skills add vercel-labs/agent-skills`. Besonders relevant als unmittelbar einsetzbare, hochwertige Referenz-Skills für Frontend-Qualität (Performance, Accessibility, Schreibstil) – die `web-design-guidelines` und `react-best-practices` sind direkt vergleichbar mit den bereits genutzten Skills `web-design-guidelines` bzw. `vercel-react-best-practices` im eigenen Environment.

---

## emilkowalski/skills

- **URL:** https://github.com/emilkowalski/skills
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-11
- **Dateien:** 8 · **Größe:** 84K
- **Struktur:** 4× SKILL.md · Ordner: skills

"Skills For Design Engineers" von Emil Kowalski (Design-Engineering-Erfahrung u.a. bei Vercel und Linear, Betreiber von animations.dev). Vier fokussierte Skills, die gezielt die "fehlende Design-Taste" von KI-Agenten adressieren: `emil-design-eng` (Hauptskill, primär Animation plus allgemeine Design-Ratschläge), `review-animations` (strenge Animations-Reviews nach Kowalskis eigenen Regeln), `animation-vocabulary` (präzises Vokabular, um Agenten exakt die gewünschte Animation zu entlocken) und `apple-design` (Apples Interface- und Bewegungsprinzipien, aus WWDC-Design-Talks destilliert und fürs Web übersetzt). Kernthese: Agenten treffen oft die falschen Detailentscheidungen (z.B. `ease-in` statt `ease-out` bei Enter-Animationen, solide statt halbtransparente Schatten) – kleine Fehler, die sich zu insgesamt mittelmäßigen statt herausragenden Interfaces summieren. Die Skills sind laut Autor ein Nebenprodukt echter Domänen-Expertise, nicht deren Ersatz. Installation über `npx skills@latest add emilkowalski/skills`. Sehr relevant als kompakte, hochkarätige Ergänzung zu den bereits vorhandenen Design-/Taste-Skills (`taste-skill`, `ui-ux-pro-max-skill`) – hier mit Fokus auf Animation und einem sehr erfahrenen, spezifischen Blickwinkel statt breiter Systematik.

---

## Egonex-AI/Understand-Anything

- **URL:** https://github.com/Egonex-AI/Understand-Anything
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-11
- **Dateien:** 469 · **Größe:** 31M
- **Struktur:** `understand-anything-plugin/skills/`, `understand-anything-plugin/agents/` (project-scanner, file-analyzer usw.), Analyse-Engine in `understand-anything-plugin/packages/core`, Dashboard in `understand-anything-plugin/packages/dashboard`, Standalone-Viewer in `understand-anything-plugin/packages/viewer` (committeten Graph ohne Claude Code via `npx` ansehen) <!-- manual -->

Ein Claude-Code-Plugin (ursprünglich von Lum1104, jetzt bei Egonex weitergeführt), das eine beliebige Codebasis mit einer Multi-Agent-Pipeline analysiert und daraus einen interaktiven Knowledge Graph baut – jede Datei, Funktion, Klasse und Abhängigkeit wird zum klickbaren, durchsuchbaren Knoten in einem visuellen Dashboard. Kombiniert deterministische Tree-sitter-Analyse (Imports, Exports, Funktions-/Klassendefinitionen, Aufrufstellen – reproduzierbar) mit LLM-Auswertung (Klartext-Zusammenfassungen, Architektur-Layer, Business-Domain-Mapping, geführte Touren). Sechs bis sieben spezialisierte Agenten (project-scanner, file-analyzer, architecture-analyzer, tour-builder, graph-reviewer, domain-analyzer, article-analyzer) arbeiten parallel; Folge-Läufe sind inkrementell (nur geänderte Dateien). Zentrale Befehle: `/understand` (Analyse), `/understand-dashboard` (Visualisierung), `/understand-chat` (Fragen zur Codebasis stellen), `/understand-diff` (Impact-Analyse von Änderungen), `/understand-onboard` (Onboarding-Guide generieren), `/understand-knowledge` (auch für Wissens-/Dokumentations-Basen nach Karpathy-Wiki-Muster nutzbar). Der Graph ist reines JSON und kann committet werden, damit Teammitglieder die Analyse nicht wiederholen müssen. Funktioniert über viele Agenten hinweg (Claude Code, Codex, Cursor, Copilot, Gemini CLI u.v.m.). Sehr relevant als direktes Vorbild für den eigenen `graphify`-Skill – ähnliches Ziel (Code/Wissen → Graph), aber mit ausgereifter Multi-Agent-Pipeline und Dashboard.

---

## wshobson/agents

- **URL:** https://github.com/wshobson/agents
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-10
- **Dateien:** 1.094 · **Größe:** 7,3M
- **Struktur:** 162× SKILL.md · Ordner: skills, agents, commands, hooks, plugins, references · Spiegelordner: .agents, .cursor, .cursor-plugin (generiert)

Ein sehr umfangreicher "Agentic Plugin Marketplace": 92 Plugins, 199 Agenten, 162 Skills und 106 Commands, aus einer einzigen Markdown-Quelle (`plugins/`) generiert und nativ auf fünf Harnesses ausgespielt (Claude Code als Quelle der Wahrheit, plus Codex CLI, Cursor, OpenCode, Gemini CLI, GitHub Copilot) – jeweils mit harness-nativen Artefakten statt kleinstem gemeinsamen Nenner. Jedes Plugin ist isoliert und komponierbar (z.B. `plugins/python-development/` mit eigenen Agenten, Commands, Skills); die Installation eines Plugins lädt nur dessen Komponenten in den Kontext. Nutzt eine gestufte Modellstrategie (Fable 5/Opus für Architektur/Sicherheit, Sonnet für Doku/Tests, Haiku für operative Aufgaben) und ein dreistufiges Qualitäts-Eval-Framework (`plugin-eval`: statische Analyse, LLM-Judge, Monte-Carlo-Zuverlässigkeitstests). Enthält externe Memory-Integration (Pensyve) als Git-Subdir-Einbindung. Build-Tooling (`make generate-all`, `make validate`, `make garden`) hält alle Harness-Ausgaben synchron. Sehr relevant als Referenz für Multi-Harness-Distribution aus einer Quelle sowie für das eigene Qualitäts-Eval-Konzept für Skills/Plugins.

---

## addyosmani/agent-skills

- **URL:** https://github.com/addyosmani/agent-skills
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-11
- **Dateien:** 126 · **Größe:** 665K
- **Struktur:** 24× SKILL.md · Ordner: skills, agents, commands, hooks, references · Spiegelordner: .agents, .claude, .gemini (generiert)

"Production-grade engineering skills" von Addy Osmani: 24 Skills (23 Lifecycle-Skills plus ein Meta-Skill `using-agent-skills`), die entlang des Entwicklungszyklus Define → Plan → Build → Verify → Review → Ship organisiert sind, mit acht zugehörigen Slash-Commands (`/spec`, `/plan`, `/build`, `/test`, `/review`, `/webperf`, `/code-simplify`, `/ship`). `/build auto` kann Plan und Umsetzung in einem einzigen freigegebenen Durchgang autonom abarbeiten (weiterhin testgetrieben und mit Einzel-Commits pro Aufgabe). Jeder Skill folgt einer festen Anatomie (Frontmatter, Overview, When to Use, Process, Rationalizations-Tabelle mit Gegenargumenten, Red Flags, Verification) und bettet Praktiken aus Googles Engineering-Kultur ein (Hyrum's Law, Beyonce Rule, Chesterton's Fence, Trunk-based Development, Shift Left). Vier vorkonfigurierte Agenten-Personas (code-reviewer, test-engineer, security-auditor, web-performance-auditor) für gezielte Reviews. Funktioniert über 13+ Agenten/Tools hinweg. Enthält einen expliziten Vergleich zu Superpowers und Matt Pococks Skills (`docs/comparison.md`) inkl. Link zu einem kontrollierten Head-to-Head-Experiment. Sehr relevant als weiteres, sehr diszipliniertes Gegenstück zu Superpowers/Matt-Pocock-Skills mit Fokus auf Verifikations-Pflicht und Anti-Rationalisierungs-Tabellen.

---

## pbakaus/impeccable

- **URL:** https://github.com/pbakaus/impeccable
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-11
- **Dateien:** 2.201 · **Größe:** 77M
- **Struktur:** Quelle in `skill/` (`SKILL.src.md` + `reference/<command>.md`), generierte Provider-Ausgaben in `plugin/skills/` bzw. `.claude/skills/`, `.cursor/skills/` usw. <!-- manual -->

Design-Guidance für KI-Coding-Agenten von Paul Bakaus, explizit als Weiterentwicklung von Anthropics `frontend-design`-Skill positioniert. Besteht aus einem einzigen Skill `impeccable` mit 23 Unterbefehlen (`/impeccable init`, `polish`, `audit`, `critique`, `bolder`, `quieter`, `distill`, `animate`, `live` u.v.m.) plus 46 deterministischen Detektor-Regeln, die typische KI-Generik erkennen (Inter-Schriftart überall, Lila-Blau-Verläufe, verschachtelte Cards, graue Schrift auf farbigem Hintergrund). `/impeccable init` legt einmalig `PRODUCT.md` (und optional `DESIGN.md`) an, die Zielgruppe, Marken-/Produkt-Register, Stimme, Anti-Referenzen, Farben, Typografie und Komponenten festhalten, auf die alle weiteren Befehle zugreifen. Live-Modus erlaubt visuelle Iteration direkt im Browser. Installierbar per CLI (`npx impeccable install`), Git-Submodule, Plugin oder manuellem Kopieren, für über zehn Tools (Cursor, Claude Code, Copilot, Gemini CLI, Codex, Grok Build u.a.); ein providernativer Hook prüft Design-Verstöße direkt bei Datei-Edits. Apache-2.0-lizenziert. Sehr relevant als weiteres, sehr ausgereiftes Anti-Slop-Design-Tool neben `taste-skill` und `emilkowalski/skills` – mit dem Alleinstellungsmerkmal der deterministischen (nicht nur LLM-basierten) Detektor-Regeln und Live-Browser-Iteration.

---

## alirezarezvani/claude-skills

- **URL:** https://github.com/alirezarezvani/claude-skills
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-10
- **Dateien:** 4.606 · **Größe:** 29M
- **Struktur:** 357× SKILL.md · Ordner: skills, agents, commands, hooks, rules, references · Spiegelordner: .claude, .codex, .gemini, .hermes, … (+1) (generiert)

Die mit Abstand umfangreichste Skill-Bibliothek im gesamten Index: 355 produktionsreife Skills über 18 Domänen (Engineering Core & POWERFUL-Tier, Product, Marketing inkl. AEO/Answer-Engine-Optimization, Regulatorik/Qualitätsmanagement, Compliance-OS, vollständige C-Level-Beratung als Personas CEO/CTO/CFO/CMO/CRO/CPO/COO/CHRO/CISO/GC/CDO/CAIO/CCO/VPE, Business-Growth, Business-Operations, Commercial, Finance, akademische Forschung sowie unternehmensweite Research Operations), mit 602 stdlib-only Python-Analyse-Tools (keine LLM-Aufrufe in Scripts, bewusst für Portabilität), 731 Referenzdateien, 99 Agenten und 109 Slash-Commands, verteilt als 83 Marketplace-Plugins. Funktioniert nativ oder per Konvertierungsskript auf 13 Tools (Claude Code, Codex, Gemini CLI, Cursor, Aider, Windsurf u.a.). Enthält einen eigenen Skill-Security-Auditor (Prompt-Injection-, Command-Injection- und Supply-Chain-Scans vor Installation) sowie ein dokumentiertes Orchestrierungs-Protokoll für Persona-Ketten über Domänengrenzen hinweg (Solo Sprint, Domain Deep-Dive, Multi-Agent Handoff, Skill Chain). Neueste Versionen bauen Product- und Projekt-Management-Skills zu selbstverifizierenden "Agent-Harness"-Loops mit deterministischen Goal-Routern aus. Sehr relevant als Referenz für Skalierung eines sehr breiten Skill-Ökosystems inkl. Business-/C-Level-Perspektive, die in den bisherigen Repos kaum abgedeckt war.
