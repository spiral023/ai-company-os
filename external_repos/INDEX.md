# Index externer Repos

Lokale Referenzbibliothek geklonter GitHub-Repos für AI-gestützte Produkt- und Softwareentwicklung: bewährte Workflows vergleichen, einzelne Skills und Regeln studieren, Agenten-Setups verstehen und konkrete Lösungsansätze extrahieren — ohne erneut klonen zu müssen. Gepflegt gemäß `AGENTS.md` → „Fremde GitHub-Repos herunterladen".

- **Ablage:** `external_repos/<owner>/<repo-name>/` (Owner als Unterordner gegen Namenskollisionen, seit 2026-07-10).
- **Versionierung:** Der Ordner `external_repos/` ist nicht versioniert (siehe `.gitignore`) und nicht im Obsidian-Vault sichtbar (siehe `.obsidian/app.json`); nur dieser Index ist versioniert.
- **Pflege:** Mechanische Felder (Dateien, Größe, Struktur, Übersicht) aktualisiert `70_Scripts/update_external_repos.py`; die Zusammenfassungen sind handgeschrieben.

**So findest du schnell das passende Repo:**

1. Aufgabe unter [Was möchtest du tun?](#was-möchtest-du-tun) nachschlagen — oder direkt in einer Kategorie unter [Repos nach Kategorie](#repos-nach-kategorie) stöbern.
2. Detail-Eintrag des Kandidaten unter [Detail-Einträge](#detail-einträge) lesen: Kontext, Stärken, Risiken, Lizenz.
3. Lokal einsteigen: zuerst `README.md`, danach die im Eintrag genannten Skills, Regeln oder Quellordner.
4. Externe Inhalte erst nach Source-, Lizenz-, Inhalts- und Trust-Prüfung übernehmen — siehe [Sicher und sinnvoll übernehmen](#sicher-und-sinnvoll-übernehmen).

> [!TIP]
> Du musst kein komplettes Framework installieren. Häufig ist es sinnvoller, ein einzelnes Pattern, eine Checkliste oder einen fokussierten Skill zu übernehmen und an das eigene Projekt anzupassen.

## Was möchtest du tun?

| Aufgabe | Gute Startpunkte | Was du dort konkret findest |
|---|---|---|
| Eine vage Idee schärfen | [mattpocock/skills](#mattpocockskills), [garrytan/gstack](#garrytangstack) | Gezielte Produktfragen, Grilling, Office Hours und Design-Reviews vor der Umsetzung |
| Einen belastbaren Umsetzungsplan erstellen | [shadcn/improve](#shadcnimprove), [obra/superpowers](#obrasuperpowers), [open-gsd/gsd-core](#open-gsdgsd-core), [github/spec-kit](#githubspec-kit) | Repo-Audit, kleinteilige Pläne, Spec-driven Development und Review-Gates |
| Strukturiert mit AI entwickeln | [obra/superpowers](#obrasuperpowers), [addyosmani/agent-skills](#addyosmaniagent-skills), [garrytan/gstack](#garrytangstack) | Durchgängige Workflows von Brainstorming und TDD bis Review, QA und Shipping |
| Ein vollständiges Agile-Framework mit Rollen nutzen | [bmad-code-org/BMAD-METHOD](#bmad-code-orgbmad-method) | Scale-adaptive Phasen, benannte Experten-Personas, Party Mode, Web-Bundles und Modul-Ökosystem |
| Kontext über lange Aufgaben erhalten | [OthmanAdi/planning-with-files](#othmanadiplanning-with-files), [open-gsd/gsd-core](#open-gsdgsd-core) | Persistente Plan-, Findings- und Statusdateien sowie frische Kontexte pro Phase |
| Code testen, reviewen und sicher shippen | [addyosmani/agent-skills](#addyosmaniagent-skills), [garrytan/gstack](#garrytangstack), [shadcn/improve](#shadcnimprove) | Test-, Security-, Performance- und Code-Review-Workflows mit Verifikation |
| Agenten-Ergebnisse prüfen und Feedback gebündelt zurückgeben | [petergyang/human-review](#petergyanghuman-review) | Direktes Editieren und punktgenau verankerte Kommentare in HTML, Markdown oder localhost-Seiten, als ein Batch an den Agenten |
| React oder Next.js verbessern | [millionco/react-doctor](#millioncoreact-doctor), [vercel-labs/agent-skills](#vercel-labsagent-skills) | Deterministischer Audit mit CI-Gate sowie Performance-, Composition- und Accessibility-Regeln |
| Mit shadcn/ui-Komponenten bauen | [shadcn-ui/ui](#shadcn-uiui) | Projektbewusster `shadcn`-Skill: liest `components.json`, empfiehlt Komposition und saubere Registry-Nutzung |
| Eine generische AI-Oberfläche aufwerten | [pbakaus/impeccable](#pbakausimpeccable), [Leonxlnx/taste-skill](#leonxlnxtaste-skill), [emilkowalski/skills](#emilkowalskiskills), [jakubkrehel/make-interfaces-feel-better](#jakubkrehelmake-interfaces-feel-better) | Anti-Slop-Regeln, Design-Taste, Animationen, visuelle Reviews und gezielte Polish-Workflows |
| Ein Design-System ableiten | [nextlevelbuilder/ui-ux-pro-max-skill](#nextlevelbuilderui-ux-pro-max-skill), [pbakaus/impeccable](#pbakausimpeccable), [VoltAgent/awesome-design-md](#voltagentawesome-design-md) | Datenbasierte Stil-, Farb- und Typografieauswahl sowie fertige, markenspezifische DESIGN.md-Tokens |
| Vom Brief zu Design-Artefakten arbeiten | [nexu-io/open-design](#nexu-ioopen-design), [abi/screenshot-to-code](#abiscreenshot-to-code) | Agent-native Prototypen, Decks, Bild/Video-Artefakte oder Screenshot-zu-Code-Generierung |
| Frontend-Qualität mit Checklisten und MCP-Tools prüfen | [thedaviddias/Front-End-Checklist](#thedaviddiasfront-end-checklist) | 385 kuratierte Regeln, 390 generierte Skills und ein gehosteter MCP-Server mit Audit-/Fix-Tools |
| Eine fremde Codebasis verstehen | [Egonex-AI/Understand-Anything](#egonex-aiunderstand-anything), [shanraisshan/claude-code-best-practice](#shanraisshanclaude-code-best-practice), [Graphify-Labs/graphify](#graphify-labsgraphify) | Knowledge Graph, Architektur- und Domain-Analyse sowie praxisnahe Agenten-Wissensbasis |
| Einen Obsidian-Vault mit Agenten bearbeiten | [kepano/obsidian-skills](#kepanoobsidian-skills) | Obsidian-Markdown, Bases, JSON Canvas, CLI-Steuerung und Web-Extraktion |
| Begriffe des AI-Codings klären und gemeinsam benennen | [mattpocock/dictionary-of-ai-coding](#mattpocockdictionary-of-ai-coding) | 69 knappe Erklärungen von Harness bis Attention Budget, jeweils mit typischem Symptom und Beispieldialog |
| AI-/LLM-Engineering-Konzepte (Skills, Harness, Kontext, SDD) nachschlagen | [mleibetseder/ai-llm-wiki](#mleibetsederai-llm-wiki) | 334 quellenzitierte Konzept-Seiten, destilliert aus 213 Artikeln und 24 Fach-PDFs |
| Aktuelle Library-Dokumentation in den Agenten holen | [upstash/context7](#upstashcontext7) | Versionsbezogene Primärdokumentation und Codebeispiele per CLI oder MCP |
| NotebookLM programmatisch oder mit Agenten nutzen | [teng-lin/notebooklm-py](#teng-linnotebooklm-py) | Python-API, CLI, MCP-Server und Skill für Quellenrecherche, zitierte Antworten sowie Artefakt-Exporte |
| Automatisch aktuelle Projekt-/Wissens-Dokumentation für Agenten pflegen | [langchain-ai/openwiki](#langchain-aiopenwiki) | CI-aktualisierte Repo-Wiki oder persönliches Wissens-Wiki aus Git, Gmail, Notion, Slack u.a. |
| Dateien (PDF, Office, Bilder, Audio) für LLM-Pipelines vorbereiten | [microsoft/markitdown](#microsoftmarkitdown) | Konvertierung diverser Formate nach Markdown, als CLI, Python-API oder MCP-Server |
| Eigene Skills entwickeln | [anthropics/skills](#anthropicsskills), [mattpocock/skills](#mattpocockskills), [addyosmani/agent-skills](#addyosmaniagent-skills) | Offizielles Format, kleine komponierbare Skills und disziplinierte Skill-Anatomien |
| Fremde Skills vor der Installation prüfen | [NVIDIA/SkillSpector](#nvidiaskillspector) | Statischer Security-Scan, optionales LLM-Review, Risk Score und SARIF-Reports |
| Skills installieren und verteilen | [vercel-labs/skills](#vercel-labsskills), [wshobson/agents](#wshobsonagents) | Multi-Agent-Installer und Beispiele für Multi-Harness-Distribution |
| Skills passend zum Stack auswählen | [midudev/autoskills](#midudevautoskills), [davila7/claude-code-templates](#davila7claude-code-templates) | Stack-Erkennung mit verifizierter Registry beziehungsweise großer Komponenten-Katalog |
| Ein großes Skill- oder Plugin-System aufbauen | [wshobson/agents](#wshobsonagents), [affaan-m/ECC](#affaan-mecc), [alirezarezvani/claude-skills](#alirezarezvaniclaude-skills), [msitarzewski/agency-agents](#msitarzewskiagency-agents) | Plugin-Architektur, Generierung für mehrere Harnesses, Evals, Security und große Skill-Kataloge |
| Overengineering und Code-Bloat vermeiden | [DietrichGebert/ponytail](#dietrichgebertponytail) | Prioritätenleiter (YAGNI, Wiederverwendung, Stdlib, Einzeiler) vor jeder Implementierung |
| Ein persistentes Agenten-Team einsetzen | [bradygaster/squad](#bradygastersquad), [garrytan/gstack](#garrytangstack) | Benannte Spezialisten, Entscheidungsprotokolle, Rollen-Reviews und automatisierte Issue-Bearbeitung |
| Komplexe strategische Entscheidung bewusst konträr prüfen | [0xNyk/council-of-high-intelligence](#0xnykcouncil-of-high-intelligence) | Rollenbasierte Gegenpositionen, Mehranbieter-Routing und dokumentierte offene Fragen |
| AI-Teams, Ziele und Budgets operativ steuern | [paperclipai/paperclip](#paperclipaipaperclip) | Org-Charts, Tickets, Heartbeats, Governance, Kostenlimits und Audit-Trails |
| Langen Agenten-Kontext oder Shell-Ausgaben verdichten | [headroomlabs-ai/headroom](#headroomlabs-aiheadroom), [rtk-ai/rtk](#rtk-airtk) | Lokale reversible Kontextkompression bzw. kompakte Command-Output-Filter |
| Agenten-Antworten und Output-Tokens verdichten | [juliusbrussee/caveman](#juliusbrusseecaveman) | Komprimierter „Caveman"-Antwortstil über 30+ Agenten, Code byte-genau erhalten |
| Persistentes Gedächtnis über Coding-Sessions hinweg aufbauen | [thedotmack/claude-mem](#thedotmackclaude-mem) | Hook-basierte Session-Kompression in SQLite/Chroma mit MCP-Suchtools |
| Mehrere KI-Coding-Tools, Provider und Configs zentral verwalten | [diegosouzapw/OmniRoute](#diegosouzapwomniroute), [farion1231/cc-switch](#farion1231cc-switch) | Multi-Provider-Gateway mit Auto-Fallback bzw. Desktop-GUI für Provider-Presets und MCP/Skill-Verwaltung |
| Autonome ML-Experimente auf einer GPU durchführen | [karpathy/autoresearch](#karpathyautoresearch) | Minimaler, messbarer Trainingsloop mit klarer Agenten- und Menschenrolle |
| Claude Code besser konfigurieren | [shanraisshan/claude-code-best-practice](#shanraisshanclaude-code-best-practice), [affaan-m/ECC](#affaan-mecc) | Best Practices für Agents, Commands, Hooks, Memory, Worktrees und Security |
| Claude Code und Codex als Referenz-Implementierungen studieren | [anthropics/claude-code](#anthropicsclaude-code), [openai/codex](#openaicodex) | Offizielle Plugin-Bundles, Hook-/Settings-Beispiele bzw. Rust-Agent-Loop, Sandboxing und SDKs eines konkurrierenden CLI-Agenten |
| SEO technisch und inhaltlich bearbeiten | [AgriciDaniel/claude-seo](#agricidanielclaude-seo), [coreyhaines31/marketingskills](#coreyhaines31marketingskills) | Tiefgehende SEO-Audits, Schema, GEO/AEO, Content und Marketing-Kontext |
| Marketing-Aufgaben mit AI bearbeiten | [coreyhaines31/marketingskills](#coreyhaines31marketingskills), [alirezarezvani/claude-skills](#alirezarezvaniclaude-skills) | Copywriting, Ads, Analytics, Pricing, Launch, RevOps und Business-Workflows |

## Repos nach Kategorie

**Charakter:** `Skill` = fokussierte Agentenanweisung · `Sammlung` = mehrere unabhängige Skills · `Framework` = zusammenhängender Arbeitsablauf · `Tool` = ausführbare Software · `Wissensbasis` = Referenzmaterial

### Workflow und Methodik

Durchgängige Entwicklungs-Workflows: Anforderungen klären, planen, umsetzen, verifizieren, shippen.

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [addyosmani/agent-skills](#addyosmaniagent-skills) | Produktionsreife Engineering-Abläufe etablieren | Define–Plan–Build–Verify–Review–Ship, Personas und Verification-Gates | Framework / Sammlung | `external_repos/addyosmani/agent-skills/skills/` |
| [bmad-code-org/BMAD-METHOD](#bmad-code-orgbmad-method) | Ein vollständiges Agile-AI-Framework mit Rollen einsetzen | Phasen-Workflows, benannte Personas, Party Mode, Web-Bundles und Modul-Ökosystem | Framework / Sammlung | `external_repos/bmad-code-org/BMAD-METHOD/src/` |
| [DietrichGebert/ponytail](#dietrichgebertponytail) | Overengineering und Code-Bloat vermeiden | Prioritätenleiter (YAGNI, Wiederverwendung, Stdlib) vor jeder Implementierung, ~20 Agent-Hosts | Skill / Sammlung | `external_repos/DietrichGebert/ponytail/skills/` |
| [garrytan/gstack](#garrytangstack) | Einen vollständigen AI-Entwicklungszyklus abbilden | Rollen-Reviews, Browser-QA, Security, Shipping und persistentes Wissen | Framework | `external_repos/garrytan/gstack/` |
| [github/spec-kit](#githubspec-kit) | Spec-Driven Development als ausführbaren Prozess etablieren | Python-CLI, Slash-Commands je Phase, Extensions/Presets/Bundles, 30+ Agenten | Framework / Tool | `external_repos/github/spec-kit/templates/` |
| [mattpocock/skills](#mattpocockskills) | Anforderungen klären, TDD und Debugging | Kleine Engineering-Skills, Grilling, Fachsprache und Architekturpflege | Sammlung | `external_repos/mattpocock/skills/skills/` |
| [multica-ai/andrej-karpathy-skills](#multica-aiandrej-karpathy-skills) | Ein kompaktes Grundverhalten für Agenten vorgeben | Vier Regeln (Think Before Coding, Simplicity First u.a.) als CLAUDE.md/Cursor-Rule/Skill | Skill | `external_repos/multica-ai/andrej-karpathy-skills/skills/` |
| [obra/superpowers](#obrasuperpowers) | Disziplinierte, testgetriebene Entwicklung | Brainstorming, Worktrees, Pläne, TDD, Reviews und Branch-Abschluss | Framework | `external_repos/obra/superpowers/skills/` |
| [open-gsd/gsd-core](#open-gsdgsd-core) | Spec-driven Development mit sauberem Kontext | Discuss–Plan–Execute–Verify–Ship, State-Dateien und Phasen-Workflows | Framework | `external_repos/open-gsd/gsd-core/` |
| [OthmanAdi/planning-with-files](#othmanadiplanning-with-files) | Lange Aufgaben und Context Rot beherrschen | Persistente Plan-, Findings- und Fortschrittsdateien plus Recovery-Hooks | Skill / Framework | `external_repos/OthmanAdi/planning-with-files/skills/` |
| [petergyang/human-review](#petergyanghuman-review) | Menschliches Review als eigenen Schritt in die Agentenschleife legen | Browser-Editor für HTML, Markdown und localhost, verankerte Kommentare, blockierendes `poll` als Wartepunkt | Tool / Skill | `external_repos/petergyang/human-review/src/` |
| [shadcn/improve](#shadcnimprove) | Eine Codebasis auditieren und gute Pläne erzeugen | Mehrdimensionaler Audit, Finding-Verifikation und ausführbare Einzelpläne | Skill | `external_repos/shadcn/improve/skills/` |

### Skills bauen, prüfen und verteilen

Skill-Format, große Skill-Ökosysteme, Auswahl, Installation und Security-Prüfung externer Skills.

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [affaan-m/ECC](#affaan-mecc) | Ein großes, portables Agent-Harness untersuchen | Agents, Skills, Commands, Hooks, Rules, Memory und Security-Audits | Framework / Sammlung | `external_repos/affaan-m/ECC/` |
| [alirezarezvani/claude-skills](#alirezarezvaniclaude-skills) | Breite Business- und Engineering-Skillbibliotheken | Hunderte Skills, Analyse-Scripts, Personas, Orchestrierung und Security-Checks | Sammlung / Marketplace | `external_repos/alirezarezvani/claude-skills/` |
| [anthropics/skills](#anthropicsskills) | Das offizielle Agent-Skills-Format verstehen | Spezifikation, Template und produktionsnahe Dokument- und Beispiel-Skills | Referenz / Sammlung | `external_repos/anthropics/skills/spec/` |
| [davila7/claude-code-templates](#davila7claude-code-templates) | Claude-Code-Komponenten recherchieren | Großer Katalog für Agents, Commands, MCPs, Settings, Hooks und Skills | Sammlung / Marketplace | `external_repos/davila7/claude-code-templates/` |
| [midudev/autoskills](#midudevautoskills) | Passende Skills automatisch zum Tech-Stack wählen | Stack-Scan, kuratierte Registry, SHA-256-Verifikation und Lockfile | Tool / Sammlung | `external_repos/midudev/autoskills/` |
| [msitarzewski/agency-agents](#msitarzewskiagency-agents) | Breite Business-/Domänen-Personas über viele Tools verteilen | ~250 Agenten in 17 Divisions, Konvertierungspipeline für 8+ Tools, Desktop-Installer | Sammlung | `external_repos/msitarzewski/agency-agents/` |
| [NVIDIA/SkillSpector](#nvidiaskillspector) | Agent-Skills und MCPs sicherheitlich prüfen | 68 statische Muster, optionales LLM-Review, Baselines, JSON/Markdown/SARIF | Tool | `external_repos/NVIDIA/SkillSpector/` |
| [vercel-labs/skills](#vercel-labsskills) | Skills über viele Coding-Agenten installieren | Quellcode der `npx skills`-CLI und Agent-Erkennung | Tool | `external_repos/vercel-labs/skills/src/` |
| [wshobson/agents](#wshobsonagents) | Ein Multi-Harness-Plugin-Ökosystem untersuchen | Viele Agents, Skills und Commands, Generatoren sowie mehrstufige Evals | Sammlung / Marketplace | `external_repos/wshobson/agents/plugins/` |

### Design und Frontend

UI-Qualität, Design-Systeme, Animation, React/Next.js-Audits und Design-Artefakte.

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [abi/screenshot-to-code](#abiscreenshot-to-code) | Screenshots und Mockups in Frontend-Code überführen | React/FastAPI-App, Multi-Modell-Generierung, Asset-Extraktion und Video-Modus | Tool | `external_repos/abi/screenshot-to-code/` |
| [emilkowalski/skills](#emilkowalskiskills) | Animation und Design-Details verbessern | Design-Engineering-Regeln, Animation-Reviews und präzises Motion-Vokabular | Sammlung | `external_repos/emilkowalski/skills/skills/` |
| [jakubkrehel/make-interfaces-feel-better](#jakubkrehelmake-interfaces-feel-better) | Finaler Polish-Pass für Web-UIs | Regeln zu Radien, Schatten, Hit Areas, Typografie und Animation mit Before/After-Review | Skill | `external_repos/jakubkrehel/make-interfaces-feel-better/skills/` |
| [Leonxlnx/taste-skill](#leonxlnxtaste-skill) | AI-generierte Frontends weniger generisch machen | Stilvarianten, Layout-, Typografie- und Motion-Regeln, Redesign-Prompts | Sammlung | `external_repos/Leonxlnx/taste-skill/skills/` |
| [millionco/react-doctor](#millioncoreact-doctor) | React-Code systematisch auditieren | Deterministische Rules, Agent-Skill, JSON-Reports und CI-Gate für neue Findings | Tool / Skill | `external_repos/millionco/react-doctor/packages/react-doctor/` |
| [nextlevelbuilder/ui-ux-pro-max-skill](#nextlevelbuilderui-ux-pro-max-skill) | Datenbasiert ein Design-System erzeugen | Stil-, Farb-, Typografie-, Chart- und UX-Datenbanken für viele Tech-Stacks | Tool / Skill | `external_repos/nextlevelbuilder/ui-ux-pro-max-skill/src/ui-ux-pro-max/` |
| [nexu-io/open-design](#nexu-ioopen-design) | Agent-native Design-Artefakte erzeugen | Desktop-Studio, Skills, `DESIGN.md`, Plugins, MCP und HTML/PDF/PPTX/MP4-Export | Tool / Framework | `external_repos/nexu-io/open-design/` |
| [pbakaus/impeccable](#pbakausimpeccable) | Bestehende Frontends systematisch polieren | 23 Design-Befehle, Produktkontext und deterministische Anti-Slop-Detektoren | Tool / Skill | `external_repos/pbakaus/impeccable/skill/` |
| [shadcn-ui/ui](#shadcn-uiui) | Projektbewusst mit shadcn/ui arbeiten | `shadcn`-Skill liest `components.json`, empfiehlt Komposition und saubere Registry-Nutzung | Tool / Skill | `external_repos/shadcn-ui/ui/` |
| [thedaviddias/Front-End-Checklist](#thedaviddiasfront-end-checklist) | Frontend-Qualität systematisch checken | 385 Regeln, 390 generierte Skills, gehosteter MCP-Server mit Audit-/Fix-Tools | Tool / Sammlung | `external_repos/thedaviddias/Front-End-Checklist/skills/` |
| [vercel-labs/agent-skills](#vercel-labsagent-skills) | React, Next.js und Web-UIs optimieren | Performance-, Composition-, Accessibility-, Writing- und Animation-Regeln | Sammlung | `external_repos/vercel-labs/agent-skills/skills/` |
| [VoltAgent/awesome-design-md](#voltagentawesome-design-md) | Marken-Design-Tokens direkt ins Projekt legen | ~70 kuratierte DESIGN.md-Dateien bekannter Marken (Farben, Typografie, Spacing) | Wissensbasis | `external_repos/VoltAgent/awesome-design-md/design-md/` |

### Marketing und SEO

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [AgriciDaniel/claude-seo](#agricidanielclaude-seo) | Umfassende SEO- und GEO-Audits | Technisches SEO, Schema, Content, Local SEO, APIs und prüfbare Empfehlungen | Framework / Sammlung | `external_repos/AgriciDaniel/claude-seo/` |
| [coreyhaines31/marketingskills](#coreyhaines31marketingskills) | Marketing für SaaS und digitale Produkte | SEO, Copy, Ads, Analytics, CRO, Pricing, Launch und zentraler Produktkontext | Sammlung | `external_repos/coreyhaines31/marketingskills/skills/` |

### Codebasis und Wissen verstehen

Onboarding in fremde Codebasen, Nachschlagewerke und aktuelle Dokumentation.

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [Egonex-AI/Understand-Anything](#egonex-aiunderstand-anything) | Große Code- und Wissensbasen verstehen | Tree-sitter-Analyse, Knowledge Graph, Dashboard, Touren und Diff-Analyse | Tool / Framework | `external_repos/Egonex-AI/Understand-Anything/understand-anything-plugin/` |
| [Graphify-Labs/graphify](#graphify-labsgraphify) | Code, Dokumente und Medien als Knowledge Graph abfragen | Deterministisches Tree-Sitter-Parsing (~40 Sprachen), MCP-Server, `/graphify`-Befehl | Tool | `external_repos/Graphify-Labs/graphify/graphify/` |
| [kepano/obsidian-skills](#kepanoobsidian-skills) | Obsidian-Vaults agentenfähig machen | Obsidian-Markdown, Bases, JSON Canvas, CLI-Steuerung und Web-Extraktion | Sammlung | `external_repos/kepano/obsidian-skills/skills/` |
| [langchain-ai/openwiki](#langchain-aiopenwiki) | Projektdoku oder persönliches Wissen automatisch aktuell halten | CI-gepflegtes Repo-Wiki bzw. persönliches Wiki aus Git/Gmail/Notion/Slack/X | Tool | `external_repos/langchain-ai/openwiki/src/` |
| [mattpocock/dictionary-of-ai-coding](#mattpocockdictionary-of-ai-coding) | Eine gemeinsame Sprache für die Arbeit mit Coding-Agenten aufbauen | 69 quervernetzte Begriffe in 7 Sektionen, je mit Mechanik, Symptom und Usage-Dialog | Wissensbasis | `external_repos/mattpocock/dictionary-of-ai-coding/dictionary/` |
| [mleibetseder/ai-llm-wiki](#mleibetsederai-llm-wiki) | Verdichtetes, zitiertes AI-/LLM-Engineering-Wissen nachschlagen | 334 Konzept-Seiten zu Skills, Harness, Context Engineering, SDD; 213 Rohquellen inkl. 24 Fach-PDFs | Wissensbasis | `external_knowledge/ai-llm-wiki/wiki/` |
| [shanraisshan/claude-code-best-practice](#shanraisshanclaude-code-best-practice) | Claude-Code-Methoden vergleichen und nachschlagen | Best Practices, Reports, Community-Tipps und Workflow-Vergleiche | Wissensbasis | `external_repos/shanraisshan/claude-code-best-practice/best-practice/` |
| [teng-lin/notebooklm-py](#teng-linnotebooklm-py) | NotebookLM automatisieren und als quellengebundenen Agenten-Speicher einsetzen | Python-API, CLI, MCP/REST-Server, Codex-Skill sowie Export von Audio, Reports, Quiz, Mindmaps und mehr | Tool / Skill | `external_repos/teng-lin/notebooklm-py/` |
| [upstash/context7](#upstashcontext7) | Aktuelle, versionsgenaue Dokumentation abrufen | `ctx7`-CLI, MCP-Server, Library-ID-Auflösung und Docs-Abfragen | Tool / Dienst | `external_repos/upstash/context7/` |

### Agenten-Teams und Entscheidungen

Persistente Agenten-Organisationen, Governance und bewusst konträre Entscheidungsprozesse.

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [0xNyk/council-of-high-intelligence](#0xnykcouncil-of-high-intelligence) | Schwierige, strategische Entscheidungen prüfen | 18 konträre Rollen, Deliberation-Modi, Dissent-Gates und Multi-Provider-Routing | Framework / Sammlung | `external_repos/0xNyk/council-of-high-intelligence/` |
| [bradygaster/squad](#bradygastersquad) | Persistente AI-Teams und Issue-Automation | CLI/SDK, Teamvorlagen, Entscheidungsprotokoll und Watch Mode | Tool / Framework | `external_repos/bradygaster/squad/packages/` |
| [paperclipai/paperclip](#paperclipaipaperclip) | AI-Agenten als Organisation mit Governance führen | Ziele, Tickets, Heartbeats, Budgets, Workspaces, Audit-Log und UI | Tool / Framework | `external_repos/paperclipai/paperclip/` |

### Kontext-Ökonomie und Infrastruktur

Token-/Kontextreduktion und lokale API-Infrastruktur — durchweg prüfpflichtig, da Datenflüsse, Tokens und Agenten-Konfigurationen betroffen sind.

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [diegosouzapw/OmniRoute](#diegosouzapwomniroute) | ~250 LLM-Provider hinter einem Endpunkt bündeln | Next.js-Gateway, 18 Routing-Strategien, MCP-Server (94 Tools), A2A-Agentenserver | Tool / Infrastruktur | `external_repos/diegosouzapw/OmniRoute/src/` |
| [farion1231/cc-switch](#farion1231cc-switch) | Provider-Configs mehrerer Coding-Tools grafisch verwalten | Tauri-Desktop-App, 50+ Presets, lokaler Proxy mit Failover, MCP-/Skill-Verwaltung | Tool | `external_repos/farion1231/cc-switch/` |
| [headroomlabs-ai/headroom](#headroomlabs-aiheadroom) | LLM- und Agentenkontext lokal komprimieren | Library, lokaler Proxy, MCP, reversible Retrieval-Cache und `headroom learn` | Tool / Framework | `external_repos/headroomlabs-ai/headroom/` |
| [juliusbrussee/caveman](#juliusbrusseecaveman) | Output-Tokens durch komprimierten Antwortstil sparen | „Caveman"-Skill mit Intensitätsstufen, Hooks, `caveman-compress`, cavecrew-Subagenten und MCP-Middleware | Skill / Sammlung | `external_repos/juliusbrussee/caveman/skills/` |
| [router-for-me/CLIProxyAPI](#router-for-mecliproxyapi) | CLI-Modelle hinter kompatiblen APIs bündeln | Go-Proxy, OAuth-Flows, Account-Pools, Load Balancing und SDK | Tool / Infrastruktur | `external_repos/router-for-me/CLIProxyAPI/` |
| [rtk-ai/rtk](#rtk-airtk) | Shell-Ausgaben für Coding-Agenten verkleinern | Rust-CLI, Command-Filter, Hook-basierte Umschreibung und Einspar-Analytics | Tool | `external_repos/rtk-ai/rtk/` |
| [thedotmack/claude-mem](#thedotmackclaude-mem) | Persistentes Gedächtnis über Sessions hinweg aufbauen | Hook-Pipeline, SQLite/Chroma-Speicher, vier MCP-Suchtools, Web-Viewer | Tool / Framework | `external_repos/thedotmack/claude-mem/src/` |

### Konkurrierende Agenten-CLIs vergleichen

Offizielle CLI-Repos zweier führender Coding-Agenten als Architektur- und Feature-Referenz.

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [anthropics/claude-code](#anthropicsclaude-code) | Offizielle Hook-/Settings-/Plugin-Beispiele nachschlagen | CHANGELOG, MDM-/Security-Settings, Plugin-Marketplace-Bundles (kein Engine-Quellcode) | Referenz | `external_repos/anthropics/claude-code/plugins/` |
| [openai/codex](#openaicodex) | Einen konkurrierenden Coding-Agenten technisch verstehen | Rust-Agent-Loop, Sandboxing, MCP-Client/-Server, Python-/TypeScript-SDKs | Tool | `external_repos/openai/codex/codex-rs/` |

### Dateien und Dokumente für Agenten aufbereiten

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [microsoft/markitdown](#microsoftmarkitdown) | Beliebige Dateiformate für LLM-Pipelines konvertieren | CLI, Python-API, MCP-Server, OCR-Plugin für PDF/Office/Bild/Audio → Markdown | Tool | `external_repos/microsoft/markitdown/packages/` |

### Autonome Forschung

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [karpathy/autoresearch](#karpathyautoresearch) | Einen kleinen autonomen LLM-Research-Loop studieren | Feste 5-Minuten-Experimente, eine editierbare Trainingsdatei und `program.md` | Referenz / Tool | `external_repos/karpathy/autoresearch/` |

## Empfohlene Startpunkte

### Für Vibe Coder: schnell bessere Ergebnisse

1. **[mattpocock/skills](#mattpocockskills)** für bessere Rückfragen und klarere Anforderungen.
2. **[pbakaus/impeccable](#pbakausimpeccable)** oder **[Leonxlnx/taste-skill](#leonxlnxtaste-skill)** gegen generische Oberflächen.
3. **[vercel-labs/agent-skills](#vercel-labsagent-skills)** für React-, Performance- und Accessibility-Qualität.
4. **[shadcn/improve](#shadcnimprove)**, wenn das Projekt gewachsen ist und einen belastbaren Verbesserungsplan braucht.
5. **[upstash/context7](#upstashcontext7)**, wenn Libraries oder APIs implementiert werden und veraltetes Modellwissen ein Risiko ist.
6. **[millionco/react-doctor](#millioncoreact-doctor)**, sobald ein React-Prototyp gewachsen ist und konkrete technische Findings statt allgemeiner Designregeln benötigt.

**Praktische Kombination:** Erst Anforderungen mit einem Grilling-Skill klären, dann bauen, anschließend UI-Regeln und einen separaten Audit anwenden.

### Für Entwickler: reproduzierbar und verifizierbar arbeiten

1. **[obra/superpowers](#obrasuperpowers)** oder **[addyosmani/agent-skills](#addyosmaniagent-skills)** als methodisches Grundgerüst.
2. **[OthmanAdi/planning-with-files](#othmanadiplanning-with-files)** für lange Aufgaben und persistente Arbeitsstände.
3. **[garrytan/gstack](#garrytangstack)** als Referenz für Rollen-Reviews, Browser-QA, Security und Shipping.
4. **[Egonex-AI/Understand-Anything](#egonex-aiunderstand-anything)** zum Onboarding in unbekannte Codebasen.
5. **[NVIDIA/SkillSpector](#nvidiaskillspector)** als zusätzlicher Scan, bevor externe Skills oder MCPs übernommen werden.

**Praktische Kombination:** Einen Hauptworkflow wählen und nur gezielte Spezial-Skills ergänzen. Mehrere vollständige Frameworks gleichzeitig erzeugen meist doppelte Regeln und widersprüchliche Gates.

### Für den Aufbau eines eigenen KI-gestützten Arbeits- und Entwicklungssystems

1. **[anthropics/skills](#anthropicsskills)** als Referenz für Format und minimale Skill-Struktur.
2. **[wshobson/agents](#wshobsonagents)** für Multi-Harness-Generierung, Plugin-Grenzen und Evals.
3. **[affaan-m/ECC](#affaan-mecc)** für Hooks, Memory, Security und große Agent-Harnesses.
4. **[coreyhaines31/marketingskills](#coreyhaines31marketingskills)** für gemeinsamen Produktkontext über viele Business-Skills.
5. **[alirezarezvani/claude-skills](#alirezarezvaniclaude-skills)** als Skalierungsreferenz für breite Domänen und Persona-Orchestrierung.
6. **[paperclipai/paperclip](#paperclipaipaperclip)** als Referenz für Ziele, Budget-Grenzen, Governance und dauerhafte Agentenarbeit.

**Praktische Kombination:** Offizielle Konventionen als Basis nehmen, kleine lokale Skills bevorzugen und große externe Systeme nur als Referenz für klar benannte Patterns verwenden.

## Sicher und sinnvoll übernehmen

Die Repositories sind lokal geklonte **Analyse- und Inspirationsquellen**, keine automatisch freigegebenen Abhängigkeiten. Vor einer produktiven Übernahme gilt der Prozess aus `AGENTS.md`:

- Quelle und Maintainer prüfen.
- Lizenz und erlaubte Nutzung prüfen.
- `SKILL.md`, Scripts, Hooks, Commands und Installationslogik vollständig sichten.
- Netzwerkzugriffe, Shell-Befehle, Credentials und Datenflüsse besonders prüfen.
- Trust-Level in `30_Skills/registry.yaml` setzen.
- Philipps Freigabe einholen, bevor ein externer Skill produktiv verwendet wird.

Bevorzuge die kleinste sinnvolle Übernahme: erst Pattern oder Checkliste, dann einzelner Skill, erst zuletzt ein vollständiges Framework oder Plugin-System.

Bei Infrastruktur, die OAuth-Tokens, API-Keys, Agenten-Accounts oder Netzwerkverkehr bündelt (etwa `CLIProxyAPI`, `headroom`, `Paperclip` oder `Context7`), sind zusätzlich Berechtigungsumfang, Datenflüsse, Telemetrie, lokale Ports und Anbieterbedingungen zu prüfen. Nicht mit Produktionsdaten oder echten Accounts einsetzen, bevor diese Punkte bewertet und gegebenenfalls freigegeben sind.

<!-- OVERVIEW:START (automatisch generiert von 70_Scripts/update_external_repos.py — nicht von Hand bearbeiten) -->
## Übersicht

- **Repos gesamt:** 57
- **Gesamtgröße:** ca. 1.568 MB
- **Dateien gesamt:** ca. 90.805 (ohne `.git`)
- **Sterne gesamt:** ca. 4.585.247 (57/57 Repos abgerufen)
- **Stand:** 2026-09-14

| Repo | Dateien | Größe | ⭐ |
|---|---:|---:|---:|
| diegosouzapw/OmniRoute | 12.757 | 213M | 65.848 |
| thedotmack/claude-mem | 1.025 | 119M | 93.817 |
| paperclipai/paperclip | 4.883 | 110M | 80.632 |
| davila7/claude-code-templates | 9.224 | 103M | 30.718 |
| teng-lin/notebooklm-py | 1.446 | 75M | 19.304 |
| shanraisshan/claude-code-best-practice | 454 | 74M | 65.907 |
| intellectronica/ruler | 257 | 71M | 2.926 |
| openai/codex | 6.504 | 64M | 123.956 |
| headroomlabs-ai/headroom | 2.314 | 63M | 71.975 |
| pbakaus/impeccable | 3.267 | 61M | 67.882 |
| affaan-m/ECC | 3.493 | 49M | 257.938 |
| shadcn-ui/ui | 5.762 | 45M | 123.709 |
| open-gsd/gsd-core | 3.057 | 45M | 9.431 |
| farion1231/cc-switch | 1.230 | 44M | 132.740 |
| millionco/react-doctor | 7.085 | 39M | 14.839 |
| Egonex-AI/Understand-Anything | 499 | 31M | 82.613 |
| midudev/autoskills | 4.610 | 30M | 6.871 |
| alirezarezvani/claude-skills | 4.777 | 30M | 25.935 |
| garrytan/gstack | 1.359 | 28M | 132.923 |
| microsoft/markitdown | 165 | 24M | 183.743 |
| bradygaster/squad | 1.891 | 22M | 3.172 |
| upstash/context7 | 410 | 21M | 61.975 |
| nextlevelbuilder/ui-ux-pro-max-skill | 662 | 21M | 127.453 |
| router-for-me/CLIProxyAPI | 1.373 | 16M | 51.695 |
| juliusbrussee/caveman | 1.436 | 16M | 105.440 |
| Graphify-Labs/graphify | 845 | 16M | 116.533 |
| langchain-ai/openwiki | 583 | 15M | 16.455 |
| OthmanAdi/planning-with-files | 610 | 14M | 26.870 |
| anthropics/claude-code | 229 | 12M | 144.960 |
| thedaviddias/Front-End-Checklist | 1.875 | 11M | 74.132 |
| github/spec-kit | 545 | 11M | 136.545 |
| anthropics/skills | 417 | 10M | 176.186 |
| wshobson/agents | 1.157 | 7,7M | 39.636 |
| vercel-labs/agent-skills | 446 | 7,5M | 31.173 |
| bmad-code-org/BMAD-METHOD | 603 | 6,3M | 52.984 |
| 0xNyk/council-of-high-intelligence | 68 | 5,9M | 4.233 |
| NVIDIA/SkillSpector | 323 | 4,5M | 17.128 |
| AgriciDaniel/claude-seo | 403 | 4,5M | 16.877 |
| msitarzewski/agency-agents | 343 | 4,2M | 152.199 |
| rtk-ai/rtk | 412 | 4,2M | 80.246 |
| coreyhaines31/marketingskills | 434 | 3,3M | 50.082 |
| abi/screenshot-to-code | 316 | 2,6M | 78.757 |
| VoltAgent/awesome-design-md | 153 | 2,1M | 115.761 |
| petergyang/human-review | 52 | 1,8M | 1.258 |
| Leonxlnx/taste-skill | 64 | 1,7M | 86.950 |
| obra/superpowers | 195 | 1,6M | 286.363 |
| DietrichGebert/ponytail | 159 | 1,6M | 137.674 |
| vercel-labs/skills | 118 | 1016K | 31.577 |
| addyosmani/agent-skills | 188 | 795K | 94.142 |
| karpathy/autoresearch | 10 | 747K | 95.745 |
| mattpocock/skills | 162 | 655K | 261.546 |
| mattpocock/dictionary-of-ai-coding | 88 | 321K | 4.590 |
| emilkowalski/skills | 23 | 239K | 37.518 |
| shadcn/improve | 9 | 61K | 9.116 |
| kepano/obsidian-skills | 14 | 53K | 48.295 |
| jakubkrehel/make-interfaces-feel-better | 12 | 48K | 3.433 |
| multica-ai/andrej-karpathy-skills | 9 | 38K | 212.841 |

Dateianzahl, Größe, Struktur und Sterne pro Repo (ohne `.git`-Verzeichnis) stehen zusätzlich in jedem Eintrag unten und werden von `70_Scripts/update_external_repos.py` automatisch aufgefrischt.
<!-- OVERVIEW:END -->

---

## Detail-Einträge

Ein Eintrag pro Repo, alphabetisch nach `owner/repo` sortiert — neue Repos entsprechend einsortieren. Mechanische Felder (Dateien, Größe, Struktur, Stars) pflegt `70_Scripts/update_external_repos.py`; die Zusammenfassung ist handgeschrieben.

---

## 0xNyk/council-of-high-intelligence

- **URL:** https://github.com/0xNyk/council-of-high-intelligence
- **Stars:** ⭐ 4.233
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 68 · **Größe:** 5,9M
- **Struktur:** Claude-Plugin mit Rollen in `agents/`, Steuerung in `skills/` und Konfigurationen in `configs/`; Installations- und Demo-Scripts separat <!-- manual -->

„Council of High Intelligence“ ist ein Multi-Agent-Plugin für strategische oder schwer umkehrbare Entscheidungen. Es inszeniert 18 klar gegensätzliche Persona-Rollen – etwa Socrates, Feynman, Torvalds, Kahneman oder Rams – und zwingt sie zu unterschiedlichen Problemrahmungen, unabhängiger Analyse, Kreuzverhören und einer abschließenden Synthese. Drei Modi begrenzen Aufwand und Tiefe: Full mit drei Runden, Quick ohne Cross-Examination und Duo mit einem gezielten Gegenpaar; zusätzlich gibt es fachbezogene Dreiergruppen für Architektur, Produkt, Risiko, Design oder AI. Das Plugin kann verfügbare Provider wie Claude, Codex, Gemini, Ollama und Cursor erkennen und Rollen über sie verteilen, um nicht nur identische Modellantworten zu vervielfachen. Dissent-Quoten, Novelty-Gates und Counterfactual-Prompts sollen Gruppendenken entgegenwirken; der Bericht soll offene Fragen und nächste Schritte vor Konsens stellen. Relevant als anschauliche Referenz für bewusst erzeugte Spannungen in Entscheidungsprozessen. Nicht geeignet für Faktenfragen, triviale oder dringende Entscheidungen – genau das dokumentiert die README selbst. Die Subagenten- und Provider-Aufrufe können erhebliche Tokenkosten, Zugriffe und Laufzeit erzeugen; deshalb nur gezielt und mit Kostenlimit verwenden. MIT-lizenziert.

---

## abi/screenshot-to-code

- **URL:** https://github.com/abi/screenshot-to-code
- **Stars:** ⭐ 78.757
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 316 · **Größe:** 2,6M
- **Struktur:** FastAPI-Backend in `backend/`, React/Vite-Frontend in `frontend/`, Hilfsprogramme und Design-Dokumente in `scripts/` und `design-docs/`; kein Skill-Paket <!-- manual -->

Screenshot to Code ist eine Web-Anwendung, die Screenshots, Mockups, Figma-Designs und Bildschirmaufzeichnungen mit generativen Modellen in funktionsfähigen Frontend-Code überführt. Unterstützt werden HTML mit Tailwind oder CSS, React, Vue, Bootstrap und Ionic; ein React/Vite-Frontend kommuniziert mit einem FastAPI-Backend. Für lokale Ausführung verlangt das Projekt mindestens einen Provider-Key (OpenAI, Anthropic oder Gemini); Gemini wird für Asset-Extraktion und Video-Modus, Replicate für Bildgenerierung, Hintergrundentfernung und Bildbearbeitung empfohlen. Mehrere konfigurierte Anbieter erlauben Modellvarianten und Vergleiche; optional rendert ein Chromium-basierter Preview-Mechanismus erzeugte Seiten, sodass der Agent das Ergebnis visuell prüfen kann. Relevant als Referenz für den Workflow „visuelle Vorlage → Code → Browser-Preview → Iteration“, nicht als Ersatz für ein bewusstes Designsystem oder Accessibility-Review. Die lokale Ausführung kann Bildmaterial und Prompts an externe Modellanbieter übertragen und verursacht API-Kosten; API-Keys gehören ausschließlich in lokale Umgebungsdateien und dürfen nicht eingecheckt werden. Vor Nutzung von Screenshots mit Kunden-, Marken- oder personenbezogenen Inhalten sind Rechte und Datenschutz zu klären. MIT-lizenziert.

---

## addyosmani/agent-skills

- **URL:** https://github.com/addyosmani/agent-skills
- **Stars:** ⭐ 94.142
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 188 · **Größe:** 795K
- **Struktur:** 24× SKILL.md · Ordner: skills, agents, commands, hooks, references · Spiegelordner: .agents, .claude, .gemini (generiert)

"Production-grade engineering skills" von Addy Osmani: 24 Skills (23 Lifecycle-Skills plus ein Meta-Skill `using-agent-skills`), die entlang des Entwicklungszyklus Define → Plan → Build → Verify → Review → Ship organisiert sind, mit acht zugehörigen Slash-Commands (`/spec`, `/plan`, `/build`, `/test`, `/review`, `/webperf`, `/code-simplify`, `/ship`). `/build auto` kann Plan und Umsetzung in einem einzigen freigegebenen Durchgang autonom abarbeiten (weiterhin testgetrieben und mit Einzel-Commits pro Aufgabe). Jeder Skill folgt einer festen Anatomie (Frontmatter, Overview, When to Use, Process, Rationalizations-Tabelle mit Gegenargumenten, Red Flags, Verification) und bettet Praktiken aus Googles Engineering-Kultur ein (Hyrum's Law, Beyonce Rule, Chesterton's Fence, Trunk-based Development, Shift Left). Vier vorkonfigurierte Agenten-Personas (code-reviewer, test-engineer, security-auditor, web-performance-auditor) für gezielte Reviews. Funktioniert über 13+ Agenten/Tools hinweg. Enthält einen expliziten Vergleich zu Superpowers und Matt Pococks Skills (`docs/comparison.md`) inkl. Link zu einem kontrollierten Head-to-Head-Experiment. Sehr relevant als weiteres, sehr diszipliniertes Gegenstück zu Superpowers/Matt-Pocock-Skills mit Fokus auf Verifikations-Pflicht und Anti-Rationalisierungs-Tabellen.

---

## affaan-m/ECC

- **URL:** https://github.com/affaan-m/ECC
- **Stars:** ⭐ 257.938
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 3.493 · **Größe:** 49M
- **Struktur:** 286× SKILL.md · Ordner: skills, agents, commands, hooks, rules, plugins, references · Spiegelordner: .agents, .claude, .codex, .cursor, … (+2) (generiert)

ECC ("Agent Harness Operating System") ist ein sehr umfangreiches Claude-Code-Plugin-System eines Einzelentwicklers, das über 10+ Monate produktiven Einsatzes gewachsen ist und über mehrere Agent-Harnesses (Claude Code, Cursor, Codex, OpenCode, Gemini, Zed, GitHub Copilot u.a.) hinweg funktioniert. Es bündelt 68 spezialisierte Subagenten (Planner, Architect, Code-Reviewer, Security-Reviewer u.v.m.), 286 Skills (Coding-Standards für 12+ Sprachökosysteme, Backend-/Frontend-Patterns, Content-/Marketing-Skills, ML-Workflows, neu die multimodale "TasteForge"-Familie inkl. `tasteforge-video` für wiederholbare, geschmacksgetriebene Video-Arbeit), 94 Legacy-Command-Shims, Hooks für Memory-Persistenz zwischen Sessions, ein instinkt-basiertes kontinuierliches Lernsystem, Verifikations-/Eval-Loops sowie einen eigenen Security-Auditor (AgentShield, OWASP-artige Scans von Claude-Konfigurationen). Installierbar als Plugin, npm-Paket oder manuell; bietet zusätzlich eine kostenpflichtige "ECC Pro"-Stufe für private Repos. Das Repo dokumentiert explizit Fallstricke bei Mehrfachinstallation (Plugin + manueller Installer gleichzeitig führt zu Duplikaten) und pflegt ein detailliertes Änderungsprotokoll. Relevant als Referenz für Skalierung eines Skill-/Agenten-Ökosystems über viele Sprachen und Harnesses hinweg, für Memory-Persistenz-Hooks und für strukturierte Sicherheits-Audits von Agent-Konfigurationen.

---

## AgriciDaniel/claude-seo

- **URL:** https://github.com/AgriciDaniel/claude-seo
- **Stars:** ⭐ 16.877
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-22
- **Dateien:** 403 · **Größe:** 4,5M
- **Struktur:** 33× SKILL.md · Ordner: skills, agents, hooks, references

Claude SEO ist ein Open-Source-SEO-Analyse-Plugin für Claude Code, das 25 Sub-Skills und 18 spezialisierte Subagenten parallel über technische SEO, Content-Qualität (E-E-A-T), Schema.org-Markup, KI-Suchoptimierung (GEO), lokale SEO, E-Commerce und internationale SEO laufen lässt. Jeder Audit erzeugt einen priorisierten, testbaren Maßnahmenplan, der auf Primärquellen (Google-Dokumentation) beruht statt auf Vermutungen – jede Empfehlung trägt explizit die zugrunde liegende Beobachtung, Abhängigkeiten zu anderen Empfehlungen, einen "woran erkennen wir das Scheitern?"-Check und einen Frühindikator. Zentrale Befehle: `/seo audit`, `/seo page`, `/seo schema`, `/seo geo`, `/seo technical`, `/seo local`, `/seo sitemap` u.v.m. Vollständige Site-Audits laufen mit bis zu 15 parallelen Agenten in 10–15 Minuten statt Stunden. Vierstufiges Credential-System erlaubt Start ohne jegliche API-Keys, mit optionalem Ausbau (PageSpeed/CrUX, Search Console, GA4, Keyword Planner). Erweiterbar durch MCP-Extensions (DataForSEO, Firecrawl, Ahrefs, SE Ranking, Profound, Bing Webmaster, Unlighthouse, Bildgenerierung). Sehr relevant als direktes fachliches Gegenstück/Vorbild zum `seo`-Skill-Bereich im eigenen Environment – deutlich tiefer ausgebaut mit konkreten Python-Skripten, Falsifizierbarkeits-Prinzip und Google-API-Integration.

---

## alirezarezvani/claude-skills

- **URL:** https://github.com/alirezarezvani/claude-skills
- **Stars:** ⭐ 25.935
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 4.777 · **Größe:** 30M
- **Struktur:** 364× SKILL.md · Ordner: skills, agents, commands, hooks, rules, references · Spiegelordner: .claude, .codex, .gemini, .hermes, … (+1) (generiert)

Die mit Abstand umfangreichste Skill-Bibliothek im gesamten Index: laut README 345 produktionsreife Skills über 18 Domänen (der Baum enthält inzwischen 364 `SKILL.md`-Dateien) (Engineering Core & POWERFUL-Tier, Product, Marketing inkl. AEO/Answer-Engine-Optimization, Regulatorik/Qualitätsmanagement, Compliance-OS, vollständige C-Level-Beratung als Personas CEO/CTO/CFO/CMO/CRO/CPO/COO/CHRO/CISO/GC/CDO/CAIO/CCO/VPE, Business-Growth, Business-Operations, Commercial, Finance, akademische Forschung sowie unternehmensweite Research Operations), mit 644 stdlib-only Python-Analyse-Tools (keine LLM-Aufrufe in Scripts, bewusst für Portabilität), rund 740 Referenzdateien, 102 Agenten und 116 Slash-Commands, verteilt als 88 Marketplace-Plugins. Neu hinzugekommen ist die Domäne Produktivität (11 Skills: `capture`, `email`-Paar, `reflect`, `handoff`, `andreessen`, `roast`, `fable-goal`, `weekly-review`, `deep-work`, `meetings`) für persönliches Aufgaben- und Zeitmanagement nach GTD-Prinzipien. Funktioniert nativ oder per Konvertierungsskript auf 13 Tools (Claude Code, Codex, Gemini CLI, Cursor, Aider, Windsurf u.a.). Enthält einen eigenen Skill-Security-Auditor (Prompt-Injection-, Command-Injection- und Supply-Chain-Scans vor Installation) sowie ein dokumentiertes Orchestrierungs-Protokoll für Persona-Ketten über Domänengrenzen hinweg (Solo Sprint, Domain Deep-Dive, Multi-Agent Handoff, Skill Chain). Neueste Versionen bauen Product- und Projekt-Management-Skills zu selbstverifizierenden "Agent-Harness"-Loops mit deterministischen Goal-Routern aus. Im Engineering-Bereich kamen zuletzt `book-to-skill` (aus einem EPUB/PDF einen Skill destillieren, mit gehärteter XML-/Zip-Verarbeitung und Symlink-Verweigerung) und `memory-engineering` ("engineer the forgetting" – bewusste Vergessens-Strategien statt unbegrenzter Memory-Akkumulation) hinzu; die Referenz-Dokumentation liegt bei rund 750 Dateien. Sehr relevant als Referenz für Skalierung eines sehr breiten Skill-Ökosystems inkl. Business-/C-Level-Perspektive und jetzt auch persönlicher Produktivität, die in den bisherigen Repos kaum abgedeckt war.

---

## anthropics/claude-code

- **URL:** https://github.com/anthropics/claude-code
- **Stars:** ⭐ 144.960
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 229 · **Größe:** 12M
- **Struktur:** Die Top-Level-Struktur (CHANGELOG, `scripts/` für Issue-Automatisierung, `examples/` für Settings/Hooks/MDM, ein Devcontainer) zeigt, dass hier nicht der CLI-Quellcode liegt, sondern rund um ein npm/Binary-Release organisierte Doku und Tooling; der Ordner `plugins/` enthält zusätzlich mehrere eigenständige Bundles mit jeweils eigenen skills/agents/commands/hooks-Unterordnern, die eine rein mechanische Skills-Repo-Erkennung fälschlich nahelegen würde. <!-- manual -->

Dieses Repository ist das offizielle GitHub-Repo zu Claude Code, enthält jedoch nicht den proprietären CLI-Quellcode selbst, sondern die Distribution begleitende Materialien: ein knappes README mit Installationsanleitung (curl/Homebrew/WinGet, npm-Installation als deprecated markiert), ein sehr umfangreiches CHANGELOG als Versionshistorie, Issue-Templates und GitHub-Actions-Workflows samt Skripten zur automatisierten Issue-Pflege (Duplikate schließen, Lifecycle-Kommentare, gh-CLI-Wrapper), sowie Beispielkonfigurationen für Hooks, MDM-Verteilung (macOS/Windows) und Settings-Sicherheitsstufen. Der Ordner `plugins/` bündelt zusätzlich mehrere offizielle, aber optionale Erweiterungen (u.a. code-review, feature-dev, hookify, pr-review-toolkit, plugin-dev, frontend-design) mit eigenen Agents, Commands, Skills und Hooks – funktional vergleichbar mit dem `anthropics/skills`-Repo, aber als Plugin-Marketplace organisiert (`.claude-plugin/marketplace.json`). Der praktische Wert liegt primär in den Beispiel-Settings, Hook-Patterns und Plugin-Referenzimplementierungen, nicht in eigenem CLI-Code. Einschränkung: Die Kernlogik der Engine ist nicht einsehbar, die Lizenz ist proprietär (© Anthropic PBC, Anthropic Commercial Terms of Service statt Open-Source-Lizenz), und Inhalte sind stark auf Anthropics eigenen Release- und Community-Betrieb zugeschnitten statt auf Wiederverwendung als Bibliothek ausgelegt.

---

## anthropics/skills

- **URL:** https://github.com/anthropics/skills
- **Stars:** ⭐ 176.186
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 417 · **Größe:** 10M
- **Struktur:** 20× SKILL.md · Ordner: skills, agents, references

Das offizielle Anthropic-Repository mit Referenz-Implementierungen für das Claude-Skills-System. Enthält Beispiel-Skills für kreative Anwendungen (Kunst, Musik, Design), technische Aufgaben (Web-App-Testing, MCP-Server-Generierung) sowie Unternehmens-Workflows (Kommunikation, Branding). Besonders relevant: die Dokument-Skills (`skills/docx`, `skills/pdf`, `skills/pptx`, `skills/xlsx`), die tatsächlich Claudes Dokumentenerstellung in Produktion antreiben – "source-available", nicht Open Source, aber als Referenz für komplexe, produktiv genutzte Skills freigegeben. Neu hinzugekommen ist `skills/claude-api`: eine sehr umfangreiche, mehrsprachige Referenz für Claude API, Tool Runner und die beta Managed Agents mit persistenten Agent-Konfigurationen, gehosteten Session-Workspaces, Skills/MCP und Scheduled Deployments. Dieser Teil ist wegen der schnell veränderlichen Modelle und Beta-Oberflächen nur zusammen mit aktueller offizieller Dokumentation zu verwenden. Zuletzt neu hinzugekommen sind `discernment-nudge` (Agenten zu bewusster Urteilsbildung anhalten statt vorschnell zuzustimmen) und `academy-guide` (vormals `claude-academy-guide`); der `claude-api`-Skill enthält jetzt zusätzlich einen Migrationsleitfaden vom Python-SDK 0.x auf 1.x. Das Repo enthält außerdem die Agent-Skills-Spezifikation (`spec/`) und ein minimales Skill-Template (`template/`) mit den zwei Pflichtfeldern im YAML-Frontmatter (`name`, `description`). Installierbar als Claude-Code-Plugin-Marketplace (`document-skills`, `example-skills`), in Claude.ai direkt nutzbar oder über die Claude API hochladbar. Als "Quelle der Wahrheit" für das Skill-Format und als Referenz für gut strukturierte, offizielle Beispiel-Skills die wichtigste Referenz unter den geladenen Repos.

---

## bmad-code-org/BMAD-METHOD

- **URL:** https://github.com/bmad-code-org/BMAD-METHOD
- **Stars:** ⭐ 52.984
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 603 · **Größe:** 6,3M
- **Struktur:** Skills in `src/bmm-skills/` (vier nummerierte Phasen) und `src/core-skills/`; Installer in `tools/installer/`, Web-Bundles in `web-bundles/`, Doku in `docs/`; kein Top-Level-`skills/`-Ordner <!-- manual -->

BMAD-METHOD („Breakthrough Method of Agile AI-driven Development") von Brian „BMad" Madison ist eines der bekanntesten und ausgereiftesten Agile-Frameworks für KI-gestützte Entwicklung (npm `bmad-method`, v6, sehr großes Changelog) und taucht in den Workflow-Vergleichen anderer Repos regelmäßig als Referenzmethodik neben Superpowers, GSD und Spec Kit auf. Der Kern führt Coding-Agenten „scale-adaptiv" durch vier nummerierte Phasen – Analysis, Plan, Solutioning, Implementation (`src/bmm-skills/1-analysis` … `4-implementation`) – und passt die Planungstiefe automatisch an die Projektkomplexität an, vom Bugfix bis zum Enterprise-System. Besonderheit sind 12+ benannte Experten-Personas (PM, Architect, Developer „Amelia", UX-Designer, Analyst, Tech Writer) als eigene Agent-Skills, ergänzt um Core-Skills wie `bmad-brainstorming`, `bmad-advanced-elicitation`, `bmad-party-mode` und `bmad-help`. Der aktive Baum umfasst acht Core- und 25 BMM-Skills; weitere 17 v6-Kompatibilitäts-Shims halten alte Skill-IDs funktionsfähig. Die bisherigen Market-, Domain- und Technical-Research-Workflows wurden in `bmad-deep-recon` mit zusätzlichen Research-Shapes zusammengeführt; `bmad-quick-dev`/`bmad-dev-auto` heißen nun `bmad-build`/`bmad-build-auto`, wobei Shims alte Aufrufe weiterleiten. Neu ist ein mehrschichtiges Code-Review (`bmad-code-review`): Review-Ebenen werden alle vor der Auswertung gestartet, erhalten den Diff als Pfad statt inline, bleiben in ihrem Ausgabevertrag und durchlaufen einen Edge-Case-Hunter mit Falsifikationsdurchgang für die eigenen Behauptungen. Anpassung erfolgt über eine base → team → user TOML-Merge-Kette (`customize.toml`, `_bmad/custom/*.toml`, `resolve_customization.py`). Ein Node-Installer (`npx bmad-method install`, Node ≥20.12, Python ≥3.10, uv) und die `bmad-modules.yaml`-Registry binden offizielle Zusatzmodule an: BMad Builder (BMB), Test Architect (TEA), Game Dev Studio, Creative Intelligence Suite, BMad Loop und WDS. Web-Bundles paketieren Planungs-Skills als Gemini Gems / ChatGPT Custom GPTs. Sehr relevant als schwergewichtige, rollen- und phasenbasierte Alternative zu schlankeren Skill-Sets – mit Alleinstellungsmerkmalen bei benannten Agile-Rollen, scale-adaptiver Tiefe und Modul-Ökosystem. MIT-lizenziert (Marke „BMAD" jedoch geschützt, siehe `TRADEMARK.md`).

---

## bradygaster/squad

- **URL:** https://github.com/bradygaster/squad
- **Stars:** ⭐ 3.172
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 1.891 · **Größe:** 22M
- **Struktur:** kein statischer Skill-Ordner mit Inhalt — die eigentliche Logik ist CLI-Quellcode in `packages/squad-cli/`, `packages/squad-sdk/`; Vorlagen in `templates/skills/`; erzeugt zur Laufzeit `.squad/agents/` + `.squad/skills/` im Zielprojekt <!-- manual -->

Squad baut über GitHub Copilot ein "menschengeführtes" Team benannter KI-Spezialisten (Frontend, Backend, Tester, Lead etc.) auf, die als Dateien im Repo (`.squad/`) persistieren, projektübergreifendes Wissen ansammeln und über Sessions hinweg lernen. Nutzer beschreiben ihr Vorhaben, Squad schlägt ein Team vor, das dann parallel an Aufgaben arbeitet; alle Entscheidungen werden nachvollziehbar in `decisions.md` protokolliert. Besonderheit ist der "Watch Mode" (genannt Ralph): ein Polling-Prozess, der GitHub Issues überwacht, priorisiert, Kontext an einen Copilot-Agenten übergibt und diesem die Auswahl überlässt, mit einer vierstufigen Fehler-Eskalation (Circuit-Breaker-Reset, Auth-Reprobe, Git-Pull, Pause mit Eskalation an Menschen). Alpha-Software, Node.js-Monorepo mit SDK- und CLI-Paket, auch als programmierbares TypeScript-Setup (`squad.config.ts`) nutzbar. Ausdrücklich als Produktivitätswerkzeug positioniert, das Menschen nicht ersetzt, sondern Koordination und Wiederholung abnimmt. Relevant als Vorbild für persistente, benannte Agenten-Teams mit Entscheidungsprotokoll und autonomem Issue-Polling mit Eskalationsstufen.

---

## coreyhaines31/marketingskills

- **URL:** https://github.com/coreyhaines31/marketingskills
- **Stars:** ⭐ 50.082
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 434 · **Größe:** 3,3M
- **Struktur:** 49× SKILL.md · Ordner: skills, references

Sammlung von 49 Marketing-Skills für KI-Coding-Agenten (Claude Code, Codex, Cursor, Windsurf) von Corey Haines (Conversion Factory, Swipe Files). Deckt praktisch das gesamte technische Marketing ab: SEO & Content (seo-audit, ai-seo, programmatic-seo, schema), Conversion-Optimierung (cro, signup, onboarding, popups, paywalls), Content & Copy (copywriting, cold-email, emails, social, video), bezahlte Kanäle (ads, ad-creative), Messung (analytics, ab-testing, attribution), Retention (churn-prevention), Wachstum (co-marketing, free-tools, referrals) sowie Strategie/Sales (pricing, launch, revops, sales-enablement). Der `attribution`-Skill trennt Plattformmeldungen von einer belastbaren Conversion-Quelle, behandelt First-/Last-/Multi-Touch-Modelle, Incrementality und First-Party-Stitching bis ins CRM; der Pricing-Workflow bewertet zusätzlich die AI-Agent-Readiness einer Seite. Zuletzt erhielt `ai-seo` eine eigene Agent-Readiness-Ebene samt Bewertung der Volatilität von Zitationsquellen, `influencer-marketing` ein Programm für UGC-Creator in technischen Nischen, und die auditierenden Skills eine durchgängige Regel zum Umgang mit nicht vertrauenswürdigen Daten. Alle Skills referenzieren ein zentrales `product-marketing`-Kontextdokument, das Produkt, Zielgruppe und Positionierung festhält und von jedem anderen Skill zuerst gelesen wird – ein Muster, um wiederholte Grundinformationen zu vermeiden. Skills sind stark querverweisend (z.B. copywriting ↔ cro ↔ ab-testing). Installierbar über npx skills, Claude-Code-Plugin, Git-Submodule oder einfaches Kopieren. Sehr relevant als direktes Vorbild für die eigenen Marketing-bezogenen Skills unter `30_Skills/`, insbesondere das Muster eines zentralen Produkt-Kontext-Dokuments, das andere Skills referenzieren.

---

## davila7/claude-code-templates

- **URL:** https://github.com/davila7/claude-code-templates
- **Stars:** ⭐ 30.718
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 9.224 · **Größe:** 103M
- **Struktur:** Großer Komponenten-Katalog in `.claude/` und `.claude-plugin/`; Installer, APIs und Dashboard-Code in `cli-tool/`, `api/`, `dashboard/` und `cloudflare-workers/`; zahlreiche generierte Spiegel und Drittquellen <!-- manual -->

Claude Code Templates ist ein großer Katalog für vorkonfigurierte Claude-Code-Komponenten. Über eine npm-CLI oder die Website lassen sich mehr als hundert Agents, Slash-Commands, MCP-Integrationen, Settings, Hooks und Skills auswählen; Beispiele reichen von Security-Audits und React-Performance bis zu Datenbank-, GitHub-, Stripe- oder AWS-Integrationen. Neben der Sammlung liefert das Projekt eigene Bedienoberflächen für Installationsverwaltung, Session-Analytics, Conversation-Monitoring, Health Checks und Plugin-Übersicht. Die README dokumentiert außerdem eine Reihe übernommener Quellen – darunter Anthropic Skills, Superpowers, wshobson/agents und alirezarezvani/claude-skills – und verweist auf deren originale Lizenzen und Attributionen. Das macht das Repo als Landkarte und Vergleichssammlung interessant, aber auch besonders prüfbedürftig: Der sehr große Katalog enthält installierbare Hooks, MCPs und Integrationen aus vielen Domänen, die nicht pauschal als vertrauenswürdig gelten können. Relevant als Referenz für Marketplace-UX, Komponententypen und Attribution bei Aggregationen. Einzelne Komponenten müssen mit ihrer tatsächlichen Quelle, Lizenz, Script- und Berechtigungswirkung geprüft werden; nicht das Gesamtpaket installieren. Das Repository selbst ist MIT-lizenziert, ohne damit die Lizenzen eingebetteter Komponenten zu vereinheitlichen.

---

## diegosouzapw/OmniRoute

- **URL:** https://github.com/diegosouzapw/OmniRoute
- **Stars:** ⭐ 65.848
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 12.757 · **Größe:** 213M
- **Struktur:** Reiner Next.js-16-Anwendungscode in `src/` (app/, domain/, lib/, server/, sse/), plus Workspace `open-sse/` (Streaming-Engine), `electron/` (Desktop-App) und `bin/` (CLI); der vorhandene Ordner `skills/` enthält keine wiederverwendbaren Agenten-Skills, sondern 42 auto-generierte SKILL.md-Referenzdateien (API/CLI-Doku für den eigenen MCP-/A2A-/REST-Zugriff auf OmniRoute selbst). <!-- manual -->

OmniRoute ist ein selbstgehosteter AI-Gateway/Proxy-Server (Next.js 16, TypeScript, npm-Paket „omniroute", zusätzlich Docker/Electron/CLI-Distribution), der einen einheitlichen OpenAI-kompatiblen Endpunkt vor rund 250 LLM-Provider legt und Format-Übersetzung zwischen OpenAI-, Claude- und Gemini-API bietet. Kernproblem: Entwickler, die viele KI-Coding-Tools (Claude Code, Codex, Cursor, Cline, Copilot) parallel nutzen, sollen kostenlose/günstige Kontingente über Provider hinweg ausschöpfen, Rate-Limits per Auto-Fallback (18 Routing-Strategien, Circuit Breaker, Cooldowns) umgehen und Tokenverbrauch durch eigene Kompressionsverfahren (RTK, „Caveman") senken. Technisch bringt es einen MCP-Server (94 Tools, drei Transporte), einen A2A-JSON-RPC-Agentenserver, ein Skill-Framework, Memory-Subsystem und umfangreiche Policy-/Kosten-Engine mit; die Qualitätssicherung ist mit ca. 21.000 Tests, ~48 Quality-Gates und strengen Contribution-Regeln (CLAUDE.md/AGENTS.md) sehr ausgeprägt. Als Referenz-Infrastruktur ist es vor allem für Multi-Provider-Routing, Kostenkontrolle und MCP-/A2A-Integrationsmuster interessant, nicht als Skill- oder Agentenbibliothek zum Einbinden. Risiken: sehr großer, komplexer Monorepo-Codebestand, starke Marketingsprache im README, Node-only-Betrieb, Sicherheitsrelevanz durch eingebettete OAuth-Client-Secrets und lokal gespeicherte Provider-Credentials, sowie hohe Wartungslast durch Providerzahl und Feature-Umfang. MIT-lizenziert.

---

## DietrichGebert/ponytail

- **URL:** https://github.com/DietrichGebert/ponytail
- **Stars:** ⭐ 137.674
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 159 · **Größe:** 1,6M
- **Struktur:** Skill-/Plugin-Paket mit `skills/` (6 SKILL.md-Definitionen), `commands/` (Slash-Commands als .toml), `hooks/` (Lifecycle-Hooks u.a. für Claude Code/Codex) sowie zusätzlichen Adapterordnern (`.cursor/`, `.windsurf/`, `.clinerules/`, `.kiro/`, `.opencode/`, `.qoder/` etc.) für rund 20 Agent-Hosts; kein klassischer Anwendungscode, sondern ein Multi-Host-Plugin-System. <!-- manual -->

Ponytail ist ein Regel- und Skill-Paket, das KI-Coding-Agenten (Claude Code, Codex, Gemini CLI, Copilot CLI, Cursor, Windsurf, OpenCode u.a.) zu minimalistischem Code zwingt: Vor jeder Implementierung durchläuft der Agent eine Prioritätenleiter (YAGNI-Prüfung, Wiederverwendung vorhandenen Codes, Standardbibliothek, native Plattformfeatures, installierte Abhängigkeiten, Einzeiler, erst dann Custom-Code), um Overengineering, unnötige Abstraktionen und Bloat zu vermeiden. Technisch besteht das Projekt aus portablen Regeltexten (AGENTS.md, host-spezifische Rule-Files) plus sechs Skills (ponytail, -review, -audit, -debt, -gain, -help) und Lifecycle-Hooks, die den Modus (lite/full/ultra/off) je Host aktivieren und injizieren; es gibt native Adapter für rund 20 Agent-Umgebungen – neu inklusive Grok Build mit nativer Skills-Anbindung – sowie einen eigenen MCP-Server (ponytail-mcp) und eine Pi-Extension. Relevant für Skill- und Prompt-Engineering in Multi-Agent-Setups, insbesondere als Vorbild für portable Regelverteilung über heterogene Agent-Hosts hinweg und als Gegenmodell zu "mehr Code ist besser". Stärken: sehr gut dokumentierte Portabilität, eigene Benchmarks (Claude-Code-Sessions) zur Wirksamkeit, klare Eskalationsleiter statt vager Prinzipien. Risiken: Benchmark-Zahlen stammen vom Autor selbst und wurden bereits einmal öffentlich korrigiert (Community-Kritik zu Baseline-Fairness); Wirkung stark modellabhängig (bei manchen Reasoning-Modellen kontraproduktiv); Setup je Host uneinheitlich (teils Plugin mit Hooks, teils nur statische Regeldatei ohne Commands); erfordert Node.js für Hooks in Claude Code/Codex. MIT-lizenziert.

---

## Egonex-AI/Understand-Anything

- **URL:** https://github.com/Egonex-AI/Understand-Anything
- **Stars:** ⭐ 82.613
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 499 · **Größe:** 31M
- **Struktur:** `understand-anything-plugin/skills/`, `understand-anything-plugin/agents/` (project-scanner, file-analyzer usw.), Analyse-Engine in `understand-anything-plugin/packages/core`, Dashboard in `understand-anything-plugin/packages/dashboard`, Standalone-Viewer in `understand-anything-plugin/packages/viewer` (committeten Graph ohne Claude Code via `npx` ansehen) <!-- manual -->

Ein Claude-Code-Plugin (ursprünglich von Lum1104, jetzt bei Egonex weitergeführt), das eine beliebige Codebasis mit einer Multi-Agent-Pipeline analysiert und daraus einen interaktiven Knowledge Graph baut – jede Datei, Funktion, Klasse und Abhängigkeit wird zum klickbaren, durchsuchbaren Knoten in einem visuellen Dashboard. Kombiniert deterministische Tree-sitter-Analyse (Imports, Exports, Funktions-/Klassendefinitionen, Aufrufstellen – reproduzierbar) mit LLM-Auswertung (Klartext-Zusammenfassungen, Architektur-Layer, Business-Domain-Mapping, geführte Touren). Sechs bis sieben spezialisierte Agenten (project-scanner, file-analyzer, architecture-analyzer, tour-builder, graph-reviewer, domain-analyzer, article-analyzer) arbeiten parallel; Folge-Läufe sind inkrementell (nur geänderte Dateien). Zentrale Befehle: `/understand` (Analyse), `/understand-dashboard` (Visualisierung), `/understand-chat` (Fragen zur Codebasis stellen), `/understand-diff` (Impact-Analyse von Änderungen), `/understand-onboard` (Onboarding-Guide generieren), `/understand-knowledge` (auch für Wissens-/Dokumentations-Basen nach Karpathy-Wiki-Muster nutzbar). Der Graph ist reines JSON und kann committet werden, damit Teammitglieder die Analyse nicht wiederholen müssen. Funktioniert über viele Agenten hinweg (Claude Code, Codex, Cursor, Copilot, Gemini CLI u.v.m.). Sehr relevant als direktes Vorbild für den eigenen `graphify`-Skill – ähnliches Ziel (Code/Wissen → Graph), aber mit ausgereifter Multi-Agent-Pipeline und Dashboard.

---

## emilkowalski/skills

- **URL:** https://github.com/emilkowalski/skills
- **Stars:** ⭐ 37.518
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 23 · **Größe:** 239K
- **Struktur:** 12× SKILL.md · Ordner: skills

"Skills For Design Engineers" von Emil Kowalski (Design-Engineering-Erfahrung u.a. bei Vercel und Linear, Betreiber von animations.dev). Mittlerweile zwölf fokussierte Skills adressieren gezielt die "fehlende Design-Taste" von KI-Agenten: `emil-design-eng` (Hauptskill, primär Animation plus allgemeine Design-Ratschläge), `review-animations`, `improve-animations`, `find-animation-opportunities`, `animation-vocabulary`, `apple-design`, `pick-ui-library`, `prototype` sowie neu `animate` (Animationen von Null aufbauen statt nur bewerten), `animate-expo` und `write-swift` (React Native/Expo bzw. natives Swift) und `ask-sonner` (Fragen zur Toast-Bibliothek Sonner des Autors). Der Prototyping-Skill erzeugt mehrere unterschiedliche Varianten eines beschriebenen UI-Bausteins und macht sie über einen Switcher direkt vergleichbar – nützlich, um vor dem Polish bewusst zwischen Richtungen zu entscheiden. Mit `animate`, `animate-expo` und `write-swift` verlässt die Sammlung erstmals das reine Web-Frontend und deckt auch Mobile-/Apple-Plattformen ab. Kernthese: Agenten treffen oft die falschen Detailentscheidungen (z.B. `ease-in` statt `ease-out` bei Enter-Animationen, solide statt halbtransparente Schatten) – kleine Fehler, die sich zu insgesamt mittelmäßigen statt herausragenden Interfaces summieren. Die Skills sind laut Autor ein Nebenprodukt echter Domänen-Expertise, nicht deren Ersatz. Installation über `npx skills@latest add emilkowalski/skills`. Sehr relevant als kompakte, hochkarätige Ergänzung zu den vorhandenen Design-/Taste-Skills (`taste-skill`, `ui-ux-pro-max-skill`) – hier mit Fokus auf Animation, Variantenbildung und einen erfahrenen, spezifischen Blickwinkel statt breiter Systematik.

---

## farion1231/cc-switch

- **URL:** https://github.com/farion1231/cc-switch
- **Stars:** ⭐ 132.740
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 1.230 · **Größe:** 44M
- **Struktur:** Reiner Anwendungscode einer Tauri-Desktop-App: React/TypeScript-Frontend in `src/` (u.a. `components/providers`, `components/mcp`, `components/skills`, `components/proxy`) und Rust-Backend in `src-tauri/src/` (`commands/`, `services/`, `database/`, `proxy/`, `mcp/`); trotz Verzeichnisnamen wie `skills/` oder `mcp/` handelt es sich nicht um ein Claude-Code-Skill/Plugin-Paket, sondern um UI-Module zur Verwaltung von Skills/MCP-Konfigurationen anderer Tools. <!-- manual -->

CC Switch ist eine Cross-Platform-Desktop-Anwendung (Tauri 2 mit Rust-Backend und React/TypeScript-Frontend), die zentrale Verwaltung von API-Provider-Konfigurationen für inzwischen acht KI-Coding-Tools bietet: Claude Code, Claude Desktop, Codex, Gemini CLI, OpenCode, OpenClaw, Hermes und seit v3.18.0 neu Grok Build (xAI) als achtes verwaltetes Tool mit eigenem Preset-Set, Proxy-Route und MCP-/Skill-Sync. Statt Konfigurationsdateien (JSON/TOML/.env) manuell zu editieren, bietet die App eine grafische Oberfläche mit über 50 Provider-Presets, Ein-Klick-Wechsel, System-Tray-Schnellzugriff sowie einer lokalen SQLite-Datenbank mit atomaren Schreibvorgängen zum Schutz vor Config-Korruption. Neu hinzugekommen ist außerdem eine direkte xAI-Grok-Kontoanmeldung per OAuth-Device-Flow für Claude Code, Claude Desktop und Codex, bei der ein lokaler Proxy Anfragen ohne eigenen API-Key in die xAI-API übersetzt. Version 3.20 bringt für Codex einen wieder verfügbaren Umschalter für das 1-Mio.-Token-Kontextfenster, mehrere Follow-Login-Provider und konfigurierbare OAuth-Verbrauchsabfragen; die mitgelieferte Preistabelle wird laufend nachgezogen. Zusätzliche Funktionen umfassen einen lokalen Proxy mit Failover/Circuit-Breaker, vereinheitlichte Verwaltung von MCP-Servern, Prompts und Skills über mehrere Tools hinweg, ein Nutzungs-Dashboard für Kosten/Tokens sowie Cloud-Sync via Dropbox/OneDrive/WebDAV. Technisch handelt es sich um eine reine Anwendung (kein Python/Node-Package, keine Bibliothek), mit klarer Schichtenarchitektur (Commands/Services/DAO) im Rust-Teil. Besonders nützlich ist sie als Referenz für Provider-Switching-UX und Multi-Tool-Konfigurationsmanagement, weniger als wiederverwendbarer Code-Baustein. Wesentliches Risiko: Die App speichert API-Keys, OAuth-Refresh-Tokens und Provider-Zugangsdaten lokal (SQLite/JSON) und synchronisiert diese optional über Cloud-Dienste Dritter; das README enthält zudem zahlreiche gesponserte Relay-Anbieter, was Sorgfalt bei Vertrauenswürdigkeit und Datenschutz nahelegt. Die Wartungsqualität wirkt aktiv (häufige Releases laut CHANGELOG), Tests via vitest/cargo test vorhanden. MIT-lizenziert.

---

## garrytan/gstack

- **URL:** https://github.com/garrytan/gstack
- **Stars:** ⭐ 132.923
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 1.359 · **Größe:** 28M
- **Struktur:** 61× SKILL.md · Ordner: skills, agents, hooks, references

gstack ist Garry Tans (Präsident/CEO von Y Combinator) persönliches Open-Source-System, das Claude Code in ein virtuelles Engineering-Team verwandelt: 23 Rollen-Skills und 8 "Power Tools" bilden einen kompletten Sprint-Zyklus ab – Think → Plan → Build → Review → Test → Ship → Reflect. Zentrale Skills: `/office-hours` (Produktinterview mit gezielten Rückfragen, erzeugt Design-Doc), `/plan-ceo-review`/`/plan-eng-review`/`/plan-design-review`/`/plan-devex-review` (mehrstufige Planbewertung aus verschiedenen Rollen-Perspektiven), `/design-shotgun` (KI-generierte Mockup-Varianten mit Geschmacks-Lernen), `/review` und `/qa` (automatisierte Code- und Browser-Tests mit echten Screenshots), `/cso` (OWASP+STRIDE-Sicherheitsaudit), `/ship`/`/land-and-deploy` (Test, PR, Deployment, Monitoring). Ergänzt durch GBrain, eine persistente, projektübergreifende Wissensdatenbank für Agenten, sowie ausgefeilte Sicherheitsmechanismen gegen Prompt-Injection im Browser-Modus. Funktioniert nicht nur mit Claude Code, sondern auch mit Codex, Cursor, OpenCode u.a. MIT-lizenziert, sehr aktiv gepflegt (detailliertes Architektur- und Sicherheitsdokument) – im August 2026 mit auffällig vielen Sicherheits- und Tracker-Wellen: Tunnel-/Pairing-Grants werden beim Neu-Verbinden sofort entzogen, `revoke` löscht auch Setup-Keys, ein Beitragenden-Security-Sweep härtete sechs Funde mit Regressionstests ab, und die Plan-Modus-Auswahl am Review-Gate erfolgt automatisch. Für Codex-Installationen gibt es ein Profil mit bewusst begrenztem Scope. Relevant als Vorbild für einen vollständigen, rollenbasierten Entwicklungs-Workflow mit Review-Gates und Browser-QA.

---

## github/spec-kit

- **URL:** https://github.com/github/spec-kit
- **Stars:** ⭐ 136.545
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 545 · **Größe:** 11M
- **Struktur:** Kern ist eine Python-CLI (`src/specify_cli` mit `integrations/`, `bundler/`, `presets/`, `workflows/`) zur Codegenerierung; `templates/commands`, `extensions/*/commands` und `presets/*/commands` enthalten Slash-Command-/Skill-Vorlagen, die beim `specify init` in Zielprojekte (z.B. `.claude/commands/`) geschrieben werden – kein eigenständiges Skill-Paket, sondern ein Generator/Installer für Skill- und Command-Artefakte anderer Agenten. <!-- manual -->

Spec-Kit ist GitHubs Referenzimplementierung von Spec-Driven Development (SDD), einem Workflow, bei dem Spezifikationen nicht nur Dokumentation, sondern ausführbarer Ausgangspunkt für KI-gestützte Codegenerierung sind. Das Projekt hat am 21.08.2026 – zum ersten Jahrestag – Version 1.0 erreicht und damit den Beta-Status verlassen; parallel kamen ein Adoptionsleitfaden für bestehende Projekte, Workflow-Quickstarts und eine Projekt-Historie in die Dokumentation. Kernstück ist die Python-CLI „specify“ (uv/pipx-Installation), die in Zielprojekten strukturierte Artefakte anlegt und über Slash-Commands bzw. Agent-Skills (`/speckit.constitution`, `.specify`, `.plan`, `.tasks`, `.implement`, `.clarify`, `.analyze`, `.checklist`, `.converge`) einen mehrstufigen Prozess von Projektprinzipien über Spezifikation und Taskaufteilung bis zu Implementierung und verbleibender Arbeit steuert. Über 30 Coding-Agenten (Claude Code, Copilot, Cursor, Codex, Gemini u.a.) werden per Integrationsmodule unterstützt, inklusive Skills-Mode für einige Agenten. Erweiterbar über Extensions, stapelbare Presets und Bundles; hinzu kommt ein katalogisiertes Workflow-System für wiederverwendbare Steps, Gates und Community-Abläufe. Komponenten werden versioniert über priorisierte Kataloge verwaltet und lokal installiert. Als Vergleichsreferenz ist Spec-Kit besonders interessant: Es ist stärker prozess-, artefakt- und distributionsorientiert (Spec/Plan/Tasks plus installierbare Workflows) als reine Skill-Sammlungen wie Superpowers. Stärken: breite Agent-Unterstützung, klare Phasenstruktur, aktive Erweiterbarkeit. Risiken: hohe CLI-/Tooling-Komplexität, starke Abhängigkeit von Python/uv, GitHub-zentrierte Governance, und der generierte Prozess kann für kleine Projekte overhead-lastig wirken. Community-Artefakte müssen vor Installation separat geprüft werden. MIT-lizenziert.

---

## Graphify-Labs/graphify

- **URL:** https://github.com/Graphify-Labs/graphify
- **Stars:** ⭐ 116.533
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 845 · **Größe:** 16M
- **Struktur:** Python-Paket (`pyproject.toml`, CLI-Entry-Point `graphify`) mit Quellcode in `graphify/`; enthält zwar einen Unterordner `graphify/skills/`, dieser ist aber ein Vorlagenverzeichnis für die vom Tool selbst generierten Skill-Dateien verschiedener KI-Assistenten (Claude, Codex, Cursor u.a.), kein direkt kopierbarer Skill-Ordner für Dritte. <!-- manual -->

Graphify ist ein Python-CLI-Tool und PyPI-Paket (`graphifyy`), das Code, Dokumente, PDFs, Bilder und Videos eines Projekts in einen durchsuchbaren Knowledge Graph überführt, den man abfragt statt Dateien zu grep-en. Code wird lokal per Tree-Sitter-AST ohne LLM geparst (deterministisch, rund 40 Sprachen), Dokumente/Medien werden optional über das Modell des jeweiligen KI-Assistenten oder einen konfigurierten API-Key semantisch erschlossen; jede Kante ist als EXTRACTED oder INFERRED markiert. Ausgabe sind drei Artefakte (graph.html, GRAPH_REPORT.md, graph.json), abfragbar per `/graphify`-Befehl, CLI-Kommandos (`query`, `path`, `explain`) oder einem optionalen MCP-Server (stdio/HTTP). Wichtige Erkenntnis für dieses Environment: Dies ist exakt die Quelle des bereits lokal installierten gleichnamigen Skills (`~/.claude/skills/graphify/SKILL.md`, identische Beschreibung „any input to knowledge graph"), der über die Befehle `graphify install` bzw. `graphify claude install` genau aus diesem Repository generiert wird — kein unabhängiges Projekt mit ähnlichem Namen und keine bloße Inspirationsquelle, sondern das Original-Tool selbst. Relevant für Agenten/Workflows, die Codebasen oder Wissenssammlungen explorierbar machen wollen, insbesondere als Ergänzung zu grep/Read-Workflows in Claude Code, Cursor, Codex etc. Stärken: breite Sprachabdeckung, lokale Verarbeitung von Code, Git-Hook-Integration, PR-Triage. Einschränkungen: junges YC-S26-Startup-Projekt mit kommerziellem Ableger (Penpax), Abhängigkeit von externen LLM-Backends für Nicht-Code-Inhalte, hohe CLI-Komplexität mit vielen Flags/Plattformen. MIT-lizenziert.

---

## headroomlabs-ai/headroom

- **URL:** https://github.com/headroomlabs-ai/headroom
- **Stars:** ⭐ 71.975
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 2.314 · **Größe:** 63M
- **Struktur:** Rust-Kern in `crates/`, Python-Paket in `headroom/`, Integrationen in `plugins/`, umfangreiche Evals und Dokumentation; kein klassisches Skill-Paket <!-- manual -->

Headroom ist eine lokale Kontext-Kompressionsschicht für LLM-Anwendungen und Coding-Agenten. Es reduziert nach eigener Darstellung Tool-Ausgaben, Logs, RAG-Chunks, Dateien und Gesprächshistorie, bevor sie ein Modell erreichen, und verbindet das mit einer reversiblem Cache: Originale bleiben lokal verfügbar und können über Retrieval nachgeladen werden. Der Inhalt kann als Python-/TypeScript-Library, lokaler OpenAI-kompatibler Proxy, MCP-Server oder Agent-Wrapper eingesetzt werden; der Wrapper unterstützt unter anderem Claude Code, Codex, Copilot, OpenCode und Cline. Die Architektur routet Inhalte zu JSON-, AST-Code- oder Text-Kompressoren und versucht über CacheAligner zudem Provider-KV-Caches besser nutzbar zu machen. Ergänzend analysiert `headroom learn` vergangene Sitzungen und kann Korrekturen oder Präferenzen in lokale Agenten-Anweisungen schreiben. Die README nennt Benchmarks und Einsparungswerte, die als Herstellerangaben zu verstehen sind. Relevant als Referenz für lokale, wiederherstellbare Kontextreduktion und für die Kombination von Token-Ökonomie, Memory und Agenten-Integration. Wegen Proxy, MCP, Session-Auswertung und möglichen Änderungen an Agenten-Konfigurationen nur nach Datenfluss-, Telemetrie- und Berechtigungsprüfung produktiv einsetzen. Apache-2.0-lizenziert.

---

## intellectronica/ruler

- **URL:** https://github.com/intellectronica/ruler
- **Stars:** ⭐ 2.926
- **Heruntergeladen:** 2026-07-15
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 257 · **Größe:** 71M
- **Struktur:** TypeScript-CLI mit Quellcode in `src/` (Adapter unter `src/agents/`, Rule-/Konfigurations- und Dateisystemlogik in `src/core/`, MCP-Transformationen in `src/mcp/`), umfangreichen Jest-Tests in `tests/` und GitHub-Actions-Workflows in `.github/workflows/` <!-- manual -->

Ruler ist eine MIT-lizenzierte TypeScript-CLI, die Anweisungen für AI-Coding-Agenten aus einem zentralen `.ruler/`-Verzeichnis in die jeweiligen nativen Konfigurationsdateien ausspielt. Markdown-Regeln werden rekursiv gesammelt, mit Herkunftsmarkern zusammengeführt und unter anderem für Codex, Claude Code, Copilot, Cursor, Gemini CLI, OpenCode und Aider erzeugt. Optional synchronisiert das Tool MCP-Server-Konfigurationen, Skills und Subagenten – neu auch nach `.kiro/skills` für Kiro; verschachtelte `.ruler/`-Verzeichnisse erlauben unterschiedliche Regeln für Teilbereiche eines Monorepos. Die Adapterliste umfasst inzwischen über 30 Agenten. Damit ist das Projekt vor allem als Referenz für Multi-Harness-Konfiguration und die Verteilung eines gemeinsamen `AGENTS.md`-/Skill-Kontexts interessant. Die Implementierung enthält Backups, Provenance-Dateien, idempotente Updates sowie Schutz gegen Schreibvorgänge über Symlinks oder außerhalb des Projektroots. Die Testbasis deckt Adapter, MCP-Merges, Revert-Verhalten und Sicherheitsgrenzen breit ab; CI prüft Linting, Tests, Build und npm-Audits mit gepinnten GitHub Actions. Praktische Risiken bleiben: `apply` verändert viele agentenspezifische Dateien und standardmäßig auch `.gitignore`; MCP-Konfigurationen können Umgebungsvariablen oder Zugangsdaten referenzieren; Skills und Subagenten sind laut README experimentell. Wegen der aktiven Beta-Positionierung und der vielen Tool-spezifischen Adapter sollte Ruler zunächst nur in einem Testprojekt mit `--dry-run`, gezielter Agentenauswahl und deaktivierten MCP-/Gitignore-Updates evaluiert werden. Für Teams, die ein solches System aufbauen, empfiehlt sich Ruler als Referenz, nicht als unbesehen zu übernehmendes Tool.

---

## jakubkrehel/make-interfaces-feel-better

- **URL:** https://github.com/jakubkrehel/make-interfaces-feel-better
- **Stars:** ⭐ 3.433
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 12 · **Größe:** 48K
- **Struktur:** 1× SKILL.md · Ordner: skills, agents

Ein einzelner, bewusst kompakter Design-Engineering-Skill für die letzte Qualitätsstufe einer Oberfläche. Er bündelt konkrete Regeln zu konzentrischen Border-Radien, optischer statt rein geometrischer Ausrichtung, transparenten Schatten, ausreichenden Hit Areas, Font Smoothing, ausgeglichenem Textumbruch, tabellarischen Zahlen, subtilen Bild-Outlines und Icons. Die neue Icon-Referenz behandelt u.a. optisches Gewicht passend zur Typografie, `currentColor`-basierte Zustände, Outline-vs.-Fill, kleine Rastergrößen, RTL-Spiegelung und zugängliche Icon-only Controls. Weitere Referenzen decken unterbrechbare Interaktionen, gestaffelte Enter- und sanfte Exit-Animationen sowie eine sparsame, GPU-freundliche Nutzung von CSS-Transitions und `will-change` ab. Besonders nützlich ist das vorgegebene Review-Format: Änderungen werden je Prinzip als Tabelle mit „Before“ und „After“ dokumentiert, nicht als unspezifische Design-Meinung. Das ergänzt breitere UI-/UX- und Frontend-Skills gut als abschließender Polish-Pass. Einige Regeln sind absichtlich sehr konkret und sollten als Heuristik statt als Produktdesign-Gesetz behandelt werden; bei Barrierefreiheit, Performance und Markenvorgaben haben projektspezifische Anforderungen Vorrang. Der Skill enthält keine Scripts, Netzwerkzugriffe oder Credential-Anweisungen. Er verweist relativ auf fünf Dokumente, weshalb bei einer selektiven Übernahme der gesamte Skill-Ordner erhalten bleiben muss. MIT-lizenziert.

---

## juliusbrussee/caveman

- **URL:** https://github.com/juliusbrussee/caveman
- **Stars:** ⭐ 105.440
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 1.436 · **Größe:** 16M
- **Struktur:** Skills als Quelle der Wahrheit in `skills/`, Subagenten in `agents/`, Command-Stubs in `commands/`, interner Code in `src/` (`hooks/`, `rules/`, `tools/`, `mcp-servers/`); Claude-Plugin-Spiegel in `plugins/caveman/` (CI-generiert) <!-- manual -->

Caveman ist ein Skill/Plugin, das KI-Coding-Agenten in komprimiertem „Caveman"-Stil antworten lässt – laut gemessenen Benchmarks rund 65 % weniger Output-Tokens bei voller technischer Genauigkeit, wobei Code, Befehle und Fehlermeldungen byte-genau erhalten bleiben. Es funktioniert über 30+ Agenten (Claude Code, Codex, Gemini, Cursor, Windsurf, Cline, Copilot, OpenClaw u.a.) via `npx skills`, Claude-Plugin, Gemini-Extension oder unified Node-Installer. Sechs Intensitätsstufen (`lite`, `full`, `ultra` sowie `wenyan`-Varianten in klassischem Chinesisch für maximale Dichte) komprimieren den Stil, nicht den Inhalt, und behalten die Sprache des Nutzers. Neben dem Kern-Skill gibt es `/caveman-commit` (Conventional Commits ≤50 Zeichen), `/caveman-review` (einzeilige PR-Kommentare), `/caveman-stats` (echte Token-Ersparnis aus dem Session-Log, Statusline-Badge), `/caveman-compress` (schreibt Memory-Dateien wie `CLAUDE.md` in Caveman-Form um und spart ~46 % Input-Tokens in jeder Folge-Session), die `caveman-shrink` MCP-Middleware und die `cavecrew`-Subagenten (Investigator/Builder/Reviewer, ~60 % kleinere Tool-Ergebnisse im Hauptkontext). Die dritte Generation des Lern-Teils ist der interessanteste Zuwachs: `/caveman-discover`, `/caveman-learn` und `/caveman-evidence-review` messen, wohin Tokens tatsächlich fließen, schlagen jede Optimierung als Diff zur Bestätigung vor, messen danach erneut und verwerfen alles, was Tokens pro Turn nicht gesenkt hat – gegengerechnet gegen die eigenen Kosten des Lernlaufs (Spend-vs-Savings-Ledger, Holdout-Berichte). Die erklärte Grenze: der Agent wird nicht dümmer gemacht, um billiger zu werden. Auf Claude Code steuern drei Hooks (SessionStart schreibt ein Flag und injiziert das Regelset, UserPromptSubmit verfolgt den Modus und verstärkt ihn, Statusline zeigt die Lebenszeit-Ersparnis) das Verhalten; Flag-Schreibvorgänge sind bewusst symlink-sicher. Eine Auto-Clarity-Regel fällt bei Sicherheitswarnungen, irreversiblen Bestätigungen und mehrstufigen Abläufen auf normale Prosa zurück. Das README ist ehrlich zu den Grenzen: Nur Output-Tokens schrumpfen, der Skill selbst kostet ~1–1,5k Input-Tokens pro Turn, auf ohnehin knappen Workloads kann die Gesamtbilanz negativ werden – der eigentliche Gewinn liegt in Lesbarkeit und Geschwindigkeit. Kein Telemetrie- oder Netzwerkzugriff nach der Installation. Relevant als fokussiertes Gegenstück zu [headroomlabs-ai/headroom](#headroomlabs-aiheadroom) und [rtk-ai/rtk](#rtk-airtk): Caveman verdichtet, was der Agent *sagt*, nicht seinen Kontext oder Shell-Ausgaben. MIT-lizenziert. Teil einer größeren Familie (`caveman-code`, `cavemem`, `cavekit`, `cavegemma`); der Installer verändert Agenten-Konfigurationen (Hooks, `settings.json`), was vor Produktivnutzung zu sichten ist.

---

## karpathy/autoresearch

- **URL:** https://github.com/karpathy/autoresearch
- **Stars:** ⭐ 95.745
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-07-13
- **Dateien:** 10 · **Größe:** 747K
- **Struktur:** bewusst minimal: `prepare.py` für feste Daten-/Runtime-Vorbereitung, `train.py` als einzige Agenten-Änderungsfläche und `program.md` als menschlicher Steuervertrag <!-- manual -->

Autoresearch ist Andrej Karpathys bewusst kleines Experiment für autonome LLM-Forschung auf einer einzelnen NVIDIA-GPU. Ein Agent darf ausschließlich `train.py` verändern, startet dann einen festen fünfminütigen Trainingslauf, misst `val_bpb` (niedriger ist besser), behält Verbesserungen und verwirft Verschlechterungen. Die konstant gehaltene Laufzeit macht Experimente auf derselben Hardware vergleichbar; die menschliche Steuerung liegt nicht in einem komplexen Framework, sondern in `program.md`, das Rollen, Grenzen und Ziel der Agentenarbeit beschreibt. `prepare.py` bleibt unverändert und übernimmt einmalige Daten- und Tokenizer-Vorbereitung, während `train.py` Modell, Optimierer und Trainingsloop enthält. Das Projekt ist absichtlich keine allgemeine AutoML-Plattform: Es verlangt laut README Python 3.10+, `uv` und eine einzelne NVIDIA-GPU (getestet auf H100); Daten-Downloads und Trainingsläufe verursachen Rechen- und potenziell Cloudkosten. Relevant als sehr klares Pattern für autonome Iteration: eine enge Änderungsfläche, ein fester Budgetrahmen, eine objektive Metrik und explizite menschliche Regeln. Für dieses Repo ist es primär ein Vorbild für experimentelles Agenten-Design, nicht ein sofort einsetzbarer Produktworkflow. Die README nennt MIT, eine Root-Lizenzdatei fehlt im geklonten Stand jedoch; Lizenz vor Übernahme separat verifizieren.

---

## kepano/obsidian-skills

- **URL:** https://github.com/kepano/obsidian-skills
- **Stars:** ⭐ 48.295
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-07-13
- **Dateien:** 14 · **Größe:** 53K
- **Struktur:** 5× SKILL.md · Ordner: skills, references

Kepanos kompakte Skill-Sammlung ergänzt Agenten um Obsidian-spezifisches Wissen, ohne ein eigenes Framework zu erzwingen. Sie enthält fünf klar getrennte Skills: `obsidian-markdown` für Wikilinks, Embeds, Callouts und Properties; `obsidian-bases` für datenbankartige `.base`-Ansichten mit Filtern und Formeln; `json-canvas` für valide `.canvas`-Dateien; `obsidian-cli` für die Arbeit mit einer laufenden Obsidian-Instanz sowie `defuddle` zum Extrahieren von sauberem Markdown aus Webseiten. Besonders passend ist `obsidian-markdown`: Das Repo ist selbst ein Obsidian-Vault, verwendet Wiki-Links und legt Wert auf portable Markdown-Dateien. JSON Canvas und Bases sind sinnvolle Ergänzungen, falls künftig visuelle Maps oder querybare Arbeitsübersichten explizit gewünscht werden. Der CLI-Skill kann Dateien ändern, JavaScript im Obsidian-Kontext ausführen, Plugins neu laden und Screenshots erstellen; daher nur mit klar benanntem Vault und enger Aufgabe verwenden. `defuddle` fordert bei Bedarf eine globale npm-Installation und ruft externe URLs ab. Das Repository enthält keine eigenen ausführbaren Scripts; die Hauptgefahr liegt in den durch Skills ausgelösten CLI-, Installations- und Netzwerkaktionen. Als Referenz sowie für eine selektive Übernahme einzelner, überprüfter Skills gut geeignet. MIT-lizenziert.

---

## langchain-ai/openwiki

- **URL:** https://github.com/langchain-ai/openwiki
- **Stars:** ⭐ 16.455
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 583 · **Größe:** 15M
- **Struktur:** Reiner Anwendungscode in `src/` (agent, auth, connectors, cli.tsx) plus `test/` und `examples/`; kein Skill-/Agent-Definitionsordner im OS-Sinne — der Ordner `openwiki/` enthält nur die vom Tool selbst generierte Wiki-Doku, und `AGENTS.md`/`CLAUDE.md` sind autogenerierte Verweisdateien auf diese Doku, keine Agentendefinitionen. <!-- manual -->

OpenWiki ist ein von LangChain entwickeltes Node/TypeScript-CLI-Tool, das für Codebasen oder persönliches Wissen automatisch eine lokale "Agent-Wiki" erstellt und pflegt. Es unterstützt zwei Modi: Code-Modus generiert Repository-Dokumentation (Architektur, Workflows, Domänenkonzepte) im Ordner `openwiki/` und aktualisiert diese per CI-Workflow (GitHub Actions, GitLab, Bitbucket) via Pull Request; Personal-Modus baut ein persönliches Wissens-Wiki unter `~/.openwiki/wiki` aus Quellen wie lokalen Git-Repos, Gmail, Notion, Slack, X/Twitter, Websuche und Hacker News. Deterministische Connector-Tools ziehen Rohdaten, ein LLM-Agent (LangChain-basiert, mit better-sqlite3-Checkpointing) synthetisiert daraus Markdown-Seiten. `.openwikiignore` kann private, generierte oder irrelevante Pfade aus Discovery und Shell-Zugriff ausschließen. Zusätzlich schreibt das Tool Blöcke in `AGENTS.md`/`CLAUDE.md`, damit Coding-Agenten die Wiki als Kontextquelle referenzieren; für Claude Code, Codex und weitere Agenten gibt es inzwischen eigene Integrationen. Neu sind "grounded claims" für selbstkorrigierende Code-Wikis: Aussagen tragen eine überprüfbare Herkunft, damit veraltete Seiten auffallen statt unbemerkt weiterzuleben. Beim `init` werden Repository-Wikis vollständig neu generiert, und das Zustandsverzeichnis ist konfigurierbar. Unterstützt werden OpenAI inkl. ChatGPT-Login, Anthropic, OpenRouter, Gemini/Vertex, AWS Bedrock, GitHub Copilot und mehrere weitere bzw. kompatible Provider sowie optionales LangSmith-Tracing. Relevant als Ergänzung zu Doku-Retrieval-Tools wie Context7, insbesondere für automatisch aktuell gehaltene Projektdokumentation als Agentenkontext. Risiken: junges Projekt, lokale Speicherung von API-Keys/OAuth-Tokens in `~/.openwiki/.env`, native Abhängigkeit (better-sqlite3), laufende LLM-Kosten und weitreichende OAuth-Connector-Berechtigungen mit Datenschutzimplikationen. MIT-lizenziert.

---

## Leonxlnx/taste-skill

- **URL:** https://github.com/Leonxlnx/taste-skill
- **Stars:** ⭐ 86.950
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 64 · **Größe:** 1,7M
- **Struktur:** 13× SKILL.md · Ordner: skills

"Anti-Slop Frontend Framework" – eine Sammlung portabler Agent-Skills, die die visuelle Qualität von KI-generierten Frontends verbessern sollen (Layout, Typografie, Bewegung, Abstände), statt generisch wirkender Standard-UIs. Enthält mehrere Implementierungs-Varianten für unterschiedliche Stilrichtungen: das Standard-`taste-skill` (v2, mit einstellbaren Reglern für Layout-Varianz, Bewegungsintensität und visuelle Dichte), eine strengere GPT/Codex-Variante, sowie spezialisierte Stile (minimalistisch, brutalistisch, "soft"/hochwertig), zusätzlich ein Skill zur Überarbeitung bestehender Projekte (`redesign-skill`) und eines gegen abgeschnittene/unvollständige Ausgaben. Ergänzend gibt es reine Bildgenerierungs-Skills (Website-Mockups, Mobile-Screens, Brand-Kits) zur Nutzung mit Bildgeneratoren wie ChatGPT Images, deren Ergebnisse dann an Coding-Agenten übergeben werden. Framework-agnostisch (React, Vue, Svelte). Installierbar über `npx skills add`. Relevant als Referenz für konkrete, anwendbare Stilregeln gegen generisch wirkende KI-UIs sowie für das Muster "Bildgenerierung zur Referenz, dann Code-Umsetzung".

---

## mattpocock/dictionary-of-ai-coding

- **URL:** https://github.com/mattpocock/dictionary-of-ai-coding
- **Stars:** ⭐ 4.590
- **Heruntergeladen:** 2026-09-14
- **Zuletzt aktualisiert:** 2026-09-14
- **Dateien:** 88 · **Größe:** 321K
- **Struktur:** Wissensbasis ohne Skill-Paket: 69 Begriffsdateien in `dictionary/`, Kuration und Generator in `internal/`, generierte `README.md` als Gesamtansicht (`dictionary/Skill.md` ist ein Lexikoneintrag, kein Agent-Skill) <!-- manual -->

Nachschlagewerk von Matt Pocock (AI Hero), das das Vokabular der KI-gestützten Softwareentwicklung in einfachem Englisch erklärt — ausdrücklich gegen den Eindruck, AI-Coding sei Expertensache und der Jargon Teil des Geschäftsmodells. 69 Einträge liegen als einzelne Markdown-Dateien in `dictionary/` und sind über `internal/Curriculum.md` in sieben Sektionen geordnet: Modell (Token, Inference, Effort, Prefix Cache), Sessions und Kontextfenster, Tools und Environment (Tool Call, MCP, Permission Mode, Sandbox), Fehlermodi (Sycophancy, Halluzination, Attention Budget und -Degradation, Smart Zone), Handoffs (Primary/Secondary Source, Spec, Ticket, Compaction), Memory und Steering (AGENTS.md, Progressive Disclosure, Context Pointer, Skill, Subagent) sowie Arbeitsmuster (Vibe Coding, Grilling, Prototyping, AFK, DX/AX). Die Einträge sind dicht quervernetzt, mindestens 200 Wörter lang und folgen einem festen Aufbau: Definition, Mechanik, das typische Symptom, an dem man das Problem erkennt, und ein kurzer Usage-Dialog. Die `README.md` ist daraus generiert (`npm run generate`, tsx-Script in `internal/`), ein CI-Job prüft ihre Aktualität. Nützlich zweifach: als Begriffsreferenz für eine einheitliche Fachsprache in diesem Repo — kompakter und einsteigerfreundlicher als das breitere, zitierte [mleibetseder/ai-llm-wiki](#mleibetsederai-llm-wiki) — und als Muster für agentengepflegte Wissensbasen, denn `CLAUDE.md` und `internal/` legen Schreibregister, Verlinkung, Issue-Tracker-Konventionen und ADR-Ablage explizit fest. Einschränkungen: keine Lizenzdatei, damit rechtlich „alle Rechte vorbehalten“ — nur als Referenz lesen, keine Inhalte übernehmen. Deutlicher Newsletter-Bezug zu aihero.dev, letzter Commit 01.07.2026 (49 Commits seit Mai 2026), Node-Tooling (husky, lint-staged, tsx) wird nicht benötigt und nicht ausgeführt.

---

## mattpocock/skills

- **URL:** https://github.com/mattpocock/skills
- **Stars:** ⭐ 261.546
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 162 · **Größe:** 655K
- **Struktur:** 36× SKILL.md · Ordner: skills, agents

Sammlung von Agent-Skills von Matt Pocock (AI Hero), die er täglich für echte Softwareentwicklung nutzt – bewusst als Gegenentwurf zu "Vibe Coding" und prozess-diktierenden Frameworks wie GSD, BMAD oder Spec-Kit. Die Skills sind klein, modular, modellunabhängig und adressieren vier typische Fehlerquellen bei KI-gestützter Entwicklung: (1) Missverständnis zwischen Nutzer und Agent, gelöst durch "Grilling"-Sessions (`grill-me`, `grill-with-docs`), die den Agenten vor der Umsetzung gezielt nachfragen lassen; (2) zu weitschweifige Agenten, gelöst durch eine geteilte Fachsprache in einem `CONTEXT.md`-Dokument; (3) nicht funktionierender Code, gelöst durch strikte Test-Driven-Development- und Debugging-Skills (`tdd`, `diagnosing-bugs`); (4) architektonischer Verfall ("Ball of Mud"), adressiert durch `improve-codebase-architecture`. Skills sind in zwei Kategorien gegliedert: Engineering (Code-Arbeit) und Productivity (allgemeine Workflows), jeweils unterteilt in user-invoked (nur per Slash-Command aufrufbar, orchestrierend) und model-invoked (auch automatisch vom Agenten genutzt, enthalten die eigentliche Disziplin). Inzwischen deckt der Engineering-Zweig auch die Kette von der Spezifikation zur Umsetzung ab (`to-spec`, `to-tickets`, `implement`, ergänzt um `wayfinder`, `triage` und `code-review`). Zwei jüngere Regeländerungen sind als Pattern interessant: Skills dürfen keine anderen user-invoked Skills aufrufen (das war eine Fehlerquelle), und das Repo hat sämtliche Gedankenstriche entfernt, um Agenten von diesem typischen KI-Schreibmuster wegzusteuern. Relevant als Vorbild für strukturierte, disziplinierte Engineering-Skills mit klarer Trennung von Orchestrierung und wiederverwendbarer Logik.

---

## microsoft/markitdown

- **URL:** https://github.com/microsoft/markitdown
- **Stars:** ⭐ 183.743
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 165 · **Größe:** 24M
- **Struktur:** keine Standard-Skill-/Agent-Ordner (Quellcode/CLI oder reine Doku)

MarkItDown ist ein von Microsoft (AutoGen-Team) entwickeltes Python-Utility, das diverse Dateiformate (PDF, Word, PowerPoint, Excel, Bilder, Audio, HTML, CSV/JSON/XML, ZIP, EPub, YouTube-URLs) in Markdown konvertiert, um sie für LLM-Pipelines und Textanalyse nutzbar zu machen. Der Ansatz: Struktur (Überschriften, Listen, Tabellen, Links) wird erhalten, das Ergebnis ist nicht auf menschliche Lesbarkeit, sondern auf Token-Effizienz und LLM-Verständlichkeit optimiert. Technisch gibt es eine CLI (`markitdown datei.pdf`), eine Python-API, einen Docker-Container sowie einen separaten MCP-Server (`markitdown-mcp`), der die Konvertierung direkt als Tool in MCP-fähige Agenten-Umgebungen einbindet – dadurch unmittelbar relevant für Agenten- und Tool-Workflows in KI-gestützten Arbeitsumgebungen. Ein Plugin-System erlaubt Erweiterungen (z. B. `markitdown-ocr` für LLM-gestützte OCR über Vision-Modelle); optional Azure Document Intelligence/Content Understanding für höherwertige Cloud-Konvertierung. Stärken: breite Formatunterstützung, leichtgewichtig, aktiv von Microsoft gepflegt, klare Sicherheitsdoku. Risiken: explizit dokumentierte Sicherheitswarnung, da I/O mit Prozessrechten erfolgen (SSRF/Path-Traversal-Risiko bei ungeprüften Eingaben), Konvertierungsqualität ist funktional statt hochtreu, viele optionale Abhängigkeiten (`[all]`) erhöhen die Angriffsfläche, und Cloud-Feature (Azure) verursachen laufende Kosten. MIT-lizenziert.

---

## midudev/autoskills

- **URL:** https://github.com/midudev/autoskills
- **Stars:** ⭐ 6.871
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-07-22
- **Dateien:** 4.610 · **Größe:** 30M
- **Struktur:** CLI-Quellcode in `src/` und `packages/`; kuratierte, gehashte Skill-Registry und Metadaten im Repository; keine klassische Quellenstruktur je Skill <!-- manual -->

Autoskills ist eine Node.js-CLI, die ein Projekt analysiert, dessen Tech-Stack aus Manifesten und Konfigurationen ableitet und dazu passende Agent-Skills installiert. Der interessante Teil ist weniger der Ein-Befehl-Installer als das Supply-Chain-Modell: Die Skills werden laut README nicht zur Laufzeit aus beliebigen Upstream-Repos gezogen, sondern von Maintainer:innen in eine repositoryeigene Registry synchronisiert, auf Prompt-Injection- und Supply-Chain-Risiken geprüft und mit SHA-256-Hashes im Manifest festgehalten. Der Installer lädt nur die ausgewählten Registry-Dateien, verifiziert sie gegen das Manifest und schreibt Herkunft und Bundle-Hash in ein `skills-lock.json`. Unterstützt werden breite moderne Stacks von React/Next.js bis zu Flutter, Cloudflare, Datenbanken, Testing und AI-/Media-Tools. Relevant als Referenz für eine kuratierte statt beliebige Skill-Beschaffung und für Lockfile-/Hash-basierte Nachvollziehbarkeit. Die README verspricht eine automatische Auswahl, die konkreten Regeln und die Registry bleiben dennoch unabhängig zu prüfen; der Installer schreibt Dateien in Zielprojekte und benötigt Node.js 22 oder neuer. Besonders wertvoll ist das Muster „vorprüfen → paketieren → verifizieren → locken“, nicht eine unreflektierte Masseninstallation. Die Lizenz CC BY-NC 4.0 schränkt insbesondere kommerzielle Nutzung ein.

---

## millionco/react-doctor

- **URL:** https://github.com/millionco/react-doctor
- **Stars:** ⭐ 14.839
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 7.085 · **Größe:** 39M
- **Struktur:** TypeScript-Monorepo in `packages/`; Kern-CLI in `packages/react-doctor/`, ergänzende ESLint-/Oxlint-/Language-Server-/Editor-Pakete sowie Skills in `skills/`; Provider-Artefakte in `.agents/` <!-- manual -->

React Doctor ist ein deterministischer Auditor für React-Codebasen. Die CLI scannt laut Paket-README Probleme in State und Effects, Performance, Architektur, Security und Accessibility und soll mit unterschiedlichen React-Frameworks und Bibliotheken arbeiten, darunter Next.js, Vite, TanStack, React Native und Expo. Ein schneller Lauf erfolgt über `npx react-doctor`; Konfigurationen lassen sich in `doctor.config.ts` anpassen, und JSON-Ausgaben enthalten stabile Diagnose-IDs sowie projektbezogene Scan-Abdeckung. Nach einem Audit kann die CLI eine passende Skill-Anleitung für Coding-Agenten wie Claude Code, Cursor, Codex oder OpenCode installieren. Für CI erstellt sie GitHub-Workflows, die Pull Requests auf neu eingeführte Findings prüfen, statt den gesamten historischen Backlog als Blocker zu behandeln; GitLab erhält einen Gate-Entwurf. Das Monorepo enthält außerdem Regeln bzw. Integrationen für ESLint, Oxlint, Language Server, VS Code und Zed. Neuere Ausbaustufen ergänzen React-bewusste Laufzeit-Traces in der CLI, Regeln zu UI-Library-Komposition und -Korrektheit hinter Capability-Gates sowie einen `improve-threejs`-Skill; die ESLint-Presets berücksichtigen jetzt den React Compiler. Relevant als ausführbares Gegenstück zu den eher regelbasierten Frontend-Skills im Index: zuerst deterministisch feststellen, was im konkreten Projekt problematisch ist, dann gezielt beheben. Die CLI sendet standardmäßig anonyme Nutzungs- und Laufzeitdaten sowie Regelzähler an Sentry; `--no-telemetry` deaktiviert dies. Die Root-Lizenz ist eine modifizierte MIT-Lizenz und verlangt für ML-Training/-Evaluation sowie bestimmte kommerzielle Hosting-/SaaS-Nutzungen vorherige schriftliche Zustimmung – daher vor Übernahme oder Produktintegration rechtlich prüfen und nur als Referenz nutzen.

---

## mleibetseder/ai-llm-wiki

- **URL:** https://github.com/mleibetseder/ai-llm-wiki
- **Stars:** ⭐ n/a (privates Repo, API nicht abrufbar)
- **Heruntergeladen:** 2026-07-14
- **Zuletzt aktualisiert:** 2026-08-23
- **Ablage (abweichend):** `external_knowledge/ai-llm-wiki/` — bewusst außerhalb von `external_repos/`, daher NICHT vom Update-Script erfasst; Pflege manuell via `git -C external_knowledge/ai-llm-wiki pull` <!-- manual -->
- **Dateien:** 2.121 · **Größe:** 531M <!-- manual -->
- **Struktur:** Obsidian-Vault: Rohquellen in `raw/` (213 Markdown-Artikel + 24 PDFs), synthetisiertes Wiki in `wiki/` (334 `concept-*`, 107 `entity-*`, 15 `paper-*`); Ingestion-Regeln in `agents.md` <!-- manual -->

Persönliche, LLM-gepflegte Wissenssammlung eines Kollegen (Obsidian-Wissensgraph) zu AI-/LLM-Engineering. Ein Agent liest Quellen (Artikel, Papers, Bücher) nach den Regeln in `agents.md` ein und destilliert sie in ein verlinktes Wiki mit strikter Grounding-Regel: Jede Aussage in `wiki/` muss eine Zitation auf eine Datei in `raw/` tragen; Wikilink-Minima (3 ausgehende, 1 eingehende) werden vor jedem Commit erzwungen. Thematische Schwerpunkte: Agent Skills und Harness Engineering, Context Engineering (Context Rot, Compaction, Progressive Disclosure, Memory-Tiers), Spec-Driven Development, Prompt Engineering sowie Agentic AI im Enterprise-Kontext. Der aktuelle Ausbau ist der größte bisher: Der Rohbestand wuchs von 161 auf 213 Artikel, das Wiki von 250 auf 334 Konzeptseiten, und erstmals ist auch das komplette Rohmaterial eingecheckt (Dateizahl von 764 auf 2.121, Größe von 262M auf 531M). Inhaltlich neu sind vor allem die Kataloge "Awesome AI Handbook" und "Awesome Agentic Patterns", Intent-Driven Development samt Outcome-Oriented Design, eine Verification Layer, Agent Security und Red-Teaming, Agent-Native Memory sowie die Unterscheidung von geteiltem und isoliertem Speicher, Agent Engineering Principles, Inference Engineering, Loop Engineering und das SkillsBench-Paper. Der frühere Ausbau hatte Loop Engineering, 30 Memory-Techniken, Agent Usability Testing, Evaluation Loops, AI Trust & Verification, resiliente AI-Stacks und autonome Digital Workers ergänzt. Relevant als bereits verdichtete, zitierte Sekundärquelle mit großer thematischer Überschneidung zu diesem Repo — Einstieg über `wiki/concept-*.md` statt über das Rohmaterial. Achtung: private Sammlung ohne Lizenz; PDFs teils urheberrechtlich geschützt, Inhalte nicht weiterverbreiten.

---

## msitarzewski/agency-agents

- **URL:** https://github.com/msitarzewski/agency-agents
- **Stars:** ⭐ 152.199
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 343 · **Größe:** 4,2M
- **Struktur:** Keine Standard-Ordner skills/agents/commands/hooks; stattdessen 17 thematische "Divisions"-Verzeichnisse (engineering, marketing, sales, design, security, gis, healthcare u.a.) mit insgesamt ca. 250 Markdown-Agentendateien mit YAML-Frontmatter (name, description, color, vibe), ergänzt um `integrations/` (generierte Konvertierungs-Outputs pro Tool), `strategy/` (Playbooks/Runbooks) und `scripts/` (Bash/Python-Installer und Konverter). <!-- manual -->

Agency-agents ist eine umfangreiche Sammlung vorformulierter KI-Agenten-Personas als Markdown-Dateien mit YAML-Frontmatter, organisiert in 17 fachlichen "Divisions" wie Engineering, Marketing, Sales, Design, Security, GIS, Healthcare, Finance und Projektmanagement mit insgesamt rund 250 Agentendefinitionen. Neuere Spezialisten decken u.a. Privacy Engineering, Rust-Refactoring, LLM-Post-Training, Data Visualization, einen Anti-Generic-UI-Finish-Gate-Review, Unterstützung für pflegende Angehörige und neu einen "Economy Designer" für Wirtschafts-/Anreizsysteme ab; Reality Checker und SEO Specialist wurden nachgeschärft. Jede Datei beschreibt Rolle, Persönlichkeit, Kernauftrag, Workflows und Erfolgsmetriken eines Spezialisten und ist als System-Prompt für Claude Code, Cursor, Codex, Gemini CLI, OpenCode, Windsurf, Aider und weitere Tools gedacht. Ein Shell-Skript-Toolkit (`scripts/install.sh`, `convert.sh`) übersetzt die Agenten automatisiert in die jeweiligen Tool-Formate und installiert sie interaktiv nach Tool und Division wählbar; zusätzlich existiert eine Desktop-App. Ergänzend gibt es unter `strategy/` Playbooks und Runbooks für Multi-Agenten-Koordination (NEXUS-Konzept). Relevant für Skill-/Agenten-Bibliotheken und Multi-Tool-Rollout von Subagenten-Prompts. Risiken: reine Prompt-Texte ohne ausführbaren Code oder Tests der Aussagen, Qualität und Tiefe variieren, Aktualität/Richtigkeit der Fachinhalte ist nicht verifizierbar, und die Menge kann Kontextfenster und Wartungsaufwand aufblähen. MIT-lizenziert.

---

## multica-ai/andrej-karpathy-skills

- **URL:** https://github.com/multica-ai/andrej-karpathy-skills
- **Stars:** ⭐ 212.841
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-07-13
- **Dateien:** 9 · **Größe:** 38K
- **Struktur:** Nur ein Ordner `skills/karpathy-guidelines` mit einer einzigen SKILL.md, deren Inhalt zusätzlich als `CLAUDE.md` und als Cursor-Rule (`.cursor/rules/karpathy-guidelines.mdc`) dupliziert vorliegt – kein Skill-Set, sondern ein einzelnes Verhaltens-/Prompt-Dokument in drei Distributionsformaten, verpackt als Claude-Code-Plugin/Marketplace-Eintrag (`.claude-plugin/`). <!-- manual -->

Das Repository ist kein Code- oder Anwendungsprojekt, sondern ein einzelnes Prompt-Dokument mit vier Verhaltensregeln für LLM-Coding-Agenten (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution), das typische Schwächen von Coding-Agenten adressieren soll: falsche Annahmen ohne Rückfrage, Überkomplizierung, ungewollte Nebenänderungen und vage Erfolgskriterien. Der Inhalt ist bewusst schlank gehalten und dreifach ausgeliefert – als CLAUDE.md, als Cursor-Regel und als Claude-Code-Skill/Plugin über einen eigenen Marketplace-Eintrag. Wichtig für die Einordnung: Trotz des Namens "andrej-karpathy-skills" stammt das Projekt nicht von Andrej Karpathy selbst, sondern von einem Drittanbieter (GitHub-Nutzer "forrestchang", Organisation "multica-ai"); es leitet sich lediglich inhaltlich von einem öffentlichen X-Post Karpathys über LLM-Coding-Fehler ab und wirbt zudem im README aktiv für das kommerzielle/eigene Folgeprojekt "Multica" des Autors – ein deutlicher Unterschied zu tatsächlich von Karpathy selbst betriebenen Repos wie [karpathy/autoresearch](#karpathyautoresearch). Relevanz für das eigene Projekt ist gering bis mittel: allenfalls als kompakte, sofort einsetzbare CLAUDE.md-Vorlage für Agenten-Grundverhalten, nicht als eigenständiges Skill- oder Agenten-Framework. Risiko: Namensgebung kann Urheberschaft vortäuschen und ist eher Marketing-Trittbrettfahrerei als Zeichen inhaltlicher Tiefe. MIT-lizenziert (laut README und plugin.json/marketplace.json angegeben, aber keine separate LICENSE-Datei im Repo-Root vorhanden).

---

## nextlevelbuilder/ui-ux-pro-max-skill

- **URL:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- **Stars:** ⭐ 127.453
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 662 · **Größe:** 21M
- **Struktur:** Quelle der Wahrheit in `src/ui-ux-pro-max/` (`data/`, `scripts/`, `templates/`), Installer in `cli/`, Dev-Kopie in `.claude/skills/` <!-- manual -->

"UI UX Pro Max" ist ein KI-Skill, der Design-Intelligenz für professionelles UI/UX über mehrere Plattformen und Frameworks bereitstellt: durchsuchbare Datenbanken mit 79 UI-Stilen (davon 50 aktiv kuratiert: Glassmorphism, Claymorphism, Neumorphism, Brutalism, Bento Grid, AI-Native UI u.v.m.), 192 Farbpaletten (1:1 auf 192 Produkttypen abgestimmt), 74 Schriftpaarungen, 25 Chart-Typen und 119 UX-Richtlinien. Ein Überarbeitungslauf im August 2026 hat Relevanzbewertung und Datenkuration angefasst: Die UX-Richtlinien wuchsen von 98 auf 119, die Stil-Datenbank wurde dagegen von 84 auf 79 Einträge verdichtet und in aktive und passive Stile getrennt – also bewusst kuratiert statt nur vergrößert. Kernstück ist weiterhin der in v2.0 eingeführte Design-System-Generator: eine Reasoning-Engine, die aus einer Produktbeschreibung (z.B. "Beauty-Spa-Landingpage") automatisch ein komplettes, begründetes Design-System ableitet – Seitenstruktur, Stil, Farben, Typografie, Effekte, Anti-Pattern-Warnungen und eine Vorab-Auslieferungs-Checkliste (Kontrast, Fokus-States, Responsive-Breakpoints etc.). Nutzt eine BM25-Suchmaschine über CSV-Datenbanken und unterstützt weiterhin 22 Tech-Stacks (React, Next.js, Vue, SwiftUI, Flutter, Laravel u.v.m.), neu ergänzt um einen eigenen Website-Design-Stack-Starter unter `stack/` sowie CodeWhale als zusätzliches Installationsziel neben Claude Code, Cursor, Windsurf & Co.; die CLI kennt jetzt ein `--global`-Flag und ein universelles `--ai`-Ziel, und für VS-Code-Copilot werden Slash-Commands als `.prompt.md` erzeugt. Die Web-Galerie zeigt Stile zusätzlich in einem Detail-Modal mit Phone-UI-Vorschau. Design-Systeme können projektübergreifend als Master+Override-Dateien persistiert werden. Aktiviert sich automatisch bei UI/UX-Anfragen in unterstützten Agenten oder per Slash-Command in anderen. Es gibt eine kostenlose Basis- und eine kostenpflichtige Premium-Version (Branding, Logo, Assets). Relevant als konkretes, datengetriebenes Gegenstück zu den eher stilistischen `taste-skill`-Ansätzen – hier mit strukturierten Entscheidungsregeln statt reiner Stilbeschreibung.

---

## nexu-io/open-design

- **URL:** https://github.com/nexu-io/open-design
- **Stars:** ⭐ 82.678
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-07-30
- **Dateien:** 11.797 · **Größe:** 310M
- **Struktur:** Monorepo mit Desktop-/Daemon-Code in `apps/`, wiederverwendbaren Skills, Templates und Datenbanken in `skills/`, `design-templates/`, `design-systems/`, `prompt-templates/` und `data/`; Provider-Ausgaben in `.claude/` <!-- manual -->

Open Design positioniert sich als Open-Source-Alternative zu Claude Design und als agent-native, lokale Design-Umgebung für macOS und Windows. Statt eines klassischen Canvas-Editors organisiert es einen Dateibestand aus Skills, `DESIGN.md`-Designsystemen, Templates und Plugins; ein Coding-Agent erzeugt daraus reale Artefakte. Das Studio kann Web-, Desktop- und Mobile-Prototypen, editierbare Live-Dashboards, HTML-basierte Decks, Bilder sowie Video-/HyperFrame-Animationen erzeugen und nach HTML, PDF, PPTX oder MP4 exportieren. Die lokale Desktop-App kann über CLI und MCP mit zahlreichen Agenten wie Claude Code, Codex, Cursor, OpenCode, Copilot und Gemini verbunden werden; alternativ bietet sie eine BYOK-Proxy-Schicht oder den neuen Managed-Dienst „Open Design Cloud" (nutzungsbasiert abgerechneter Zugriff auf 20+ Modelle von GPT, Claude, Gemini und DeepSeek ohne eigene API-Keys). Seit Version 0.13.0 überstehen lange Design-Sessions Unterbrechungen besser: Runs bei Codex, OpenCode, Pi und Open Design Cloud lassen sich über mehrere Turns fortsetzen, ergänzt um einen verbesserten Modellwähler und direkten Screenshot-Export nach PPTX/PDF. Besonders interessant sind die explizite Brand-Contract-Datei `DESIGN.md`, das breite Template-/Prompt-Material und die Plugin-Architektur. Relevant als große Referenz für einen nachvollziehbaren „Brief → Designsystem → Artefakt → Kritik → Export“-Workflow und dafür, wie Skills als Produktoberfläche nutzbar werden. Der Umfang, eingebundene Drittinhalte, Modellprovider und die Proxy-/MCP-Integration machen es jedoch zu einer Referenzquelle, nicht zu einem ungeprüften Standard-Plugin. Apache-2.0-lizenziert.

---

## NVIDIA/SkillSpector

- **URL:** https://github.com/NVIDIA/SkillSpector
- **Stars:** ⭐ 17.128
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 323 · **Größe:** 4,5M
- **Struktur:** Python-Scanner in `src/`, Regeln und Tests in `tests/`, Integrationen und Batch-Tools unter `extensions/` und `contrib/`; kein Skill-Paket <!-- manual -->

SkillSpector ist ein Security-Scanner für Agent-Skills, MCPs und verwandte Konfigurationen. Er akzeptiert lokale Verzeichnisse, einzelne `SKILL.md`-Dateien, Git-Repositories und ZIP-Dateien und prüft sie zunächst statisch, optional danach mit semantischer LLM-Auswertung. Die README nennt 68 Muster in 17 Kategorien, darunter Prompt Injection, Datenexfiltration, Privilege Escalation, Supply-Chain-Risiken, Memory Poisoning, Tool Misuse, MCP Least Privilege und Tool Poisoning. Ergebnisse können im Terminal sowie als JSON, Markdown oder SARIF ausgegeben werden; Baselines erlauben es, bekannte Findings zu akzeptieren und spätere Scans auf neue Befunde zu fokussieren. Version 2.5 ergänzt ein kanonisches Inspection Ledger und weist in JSON/SARIF aus, ob rekursive Child-Scans vollständig ausgeführt wurden; fehlgeschlagene Unter-Scans können damit nicht mehr wie ein sauberer Gesamtlauf erscheinen. Berichte unterscheiden zudem `llm_used`/`scan_mode`, sodass ein statischer Low-Risk-Score nicht mit einer vollständigen LLM-Prüfung verwechselt wird. Die Patches 2.5.1/2.5.2 setzen diese Linie fort: Der Scanner läuft bei nicht erreichbarem LLM-Provider fail-closed statt still degradiert, meldet auch einen nur teilweisen LLM-Ausfall als "degraded", begrenzt die Aufnahme von Remote-URLs, ZIP-Archiven und Git-Repos vor der Verarbeitung, inspiziert verborgene ausführbare Dateien in verschachtelten Artefakten und prüft neu die Posture von MCP-Registries. OSV-Advisories werden über exakte Lockfile-Versionen aufgelöst. Zusätzlich kann der Scanner OSV-Daten für Schwachstellen nachschlagen und als MCP-Server laufen. Für die optionale LLM-Stufe unterstützt er verschiedene Cloud-Provider und lokale CLIs – ein wichtiger Datenabfluss- und Kostenaspekt. Relevant als Prüfwerkzeug vor produktiver Übernahme externer Skills. Ein Scan ist kein Sicherheitsnachweis; Findings, Baselines und übermittelte Inhalte müssen von Menschen bewertet werden. Apache-2.0-lizenziert.

---

## obra/superpowers

- **URL:** https://github.com/obra/superpowers
- **Stars:** ⭐ 286.363
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 195 · **Größe:** 1,6M
- **Struktur:** 14× SKILL.md · Ordner: skills, hooks, references · Spiegelordner: .agents, .opencode (generiert)

Superpowers ist eine vollständige Softwareentwicklungs-Methodik als Satz komponierbarer Skills von Jesse Vincent (Prime Radiant), verfügbar für praktisch alle gängigen Coding-Agenten (Claude Code, Antigravity, Codex, Cursor, Factory Droid, GitHub Copilot CLI, Kimi Code, OpenCode, Pi). Der Kern-Workflow läuft automatisch ab, sobald der Agent erkennt, dass etwas gebaut werden soll: `brainstorming` → `using-git-worktrees` → `writing-plans` → `subagent-driven-development`/`executing-plans` → `test-driven-development` → Code-Review → Branch-Abschluss. Version 6.3 erweitert die Harness-Unterstützung um Devin CLI und Hermes Agent (plus Grok Build in der Installationsdoku) und skaliert die Brainstorming-Zeremonie an der Aufgabe: Anfragen werden als spike, bounded oder architectural klassifiziert, kleine Aufgaben überspringen das Zwei-Dokumente-Ritual, die Freigabe vor der Umsetzung bleibt aber immer bestehen. In der subagentengetriebenen Entwicklung stallen Controller nicht mehr bei Plankonflikten – nicht-katastrophale Konflikte erhalten ein protokolliertes Ruling, nur destruktive oder irreversible Aktionen stoppen weiterhin für Menschen; gleichartige Kleinaufgaben werden zu einem Dispatch gebündelt, Implementer und Reviewer dürfen keine eigenen Subagenten mehr starten, und Pläne tragen einen `Spec:`-Zeiger, gegen den Konflikte aufgelöst werden. Beim Branch-Abschluss zerstört das Worktree-Entfernen keine untracked Dateien mehr, sondern benennt sie und fragt nach. Version 6.2 hatte zuvor den SDD-Arbeitsbereich planbezogen gemacht (`.superpowers/sdd/<plan>/`); die TDD-Referenz ist ein positiver Katalog für belastbare Tests inklusive Mutation-/Falsifizierbarkeitsprüfung. Philosophie: Test-Driven Development, systematisches statt Ad-hoc-Vorgehen, Einfachheit, Belege statt Behauptungen. Das Projekt hat strenge Beitragsregeln (94% PR-Ablehnungsquote, Offenlegung von Modell/Harness, keine Fremd-Abhängigkeiten oder domänenspezifischen Skills im Core). Direkt relevant als Referenz für Skill-Disziplin, reviewbare Subagenten-Abläufe und PR-Qualitätsstandards.

---

## open-gsd/gsd-core

- **URL:** https://github.com/open-gsd/gsd-core
- **Stars:** ⭐ 9.431
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 3.057 · **Größe:** 45M
- **Struktur:** 71× SKILL.md · Ordner: skills, agents, commands, hooks, references · Spiegelordner: .kilo, .opencode (generiert)

GSD Core ("Git. Ship. Done.") ist ein inzwischen umfangreiches Context-Engineering- und Spec-driven-Development-Framework für Claude Code, OpenCode, Antigravity CLI, Kimi, Kilo, Codex, Copilot, Cursor, Windsurf und weitere Hosts. Der Kern bleibt ein disziplinierter Fünf-Schritte-Zyklus: Discuss → Plan → Execute → Verify → Ship. Er adressiert "Context Rot", indem schwere Arbeit in frischen Executor-Kontexten läuft und strukturierte Artefakte wie `STATE.md` und `CONTEXT.md` Session-Grenzen überleben. Über diesen Kern hinaus bietet GSD mittlerweile einen Companion-MCP-Server, Capability-/Predicate-Gates, Host-Integrationen, State-Rebuilds, Knowledge-Graph-Anbindung, einen stark formalisierten Debugger und optional eine default-off Claude-Orchestrierung mit planbezogenen Worktrees und gemeinsamem Budget. Reviewer-Lanes und Trust-Disclosure-Klassen machen unterschiedliche Review-Arten explizit; API-Integrationen können vor dem Verify eine Coverage-Matrix verlangen. Zuletzt kamen ein Konsens-Gate für die `CYCLE_SUMMARY` bei mehreren Reviewern, eine Provenance-Pflicht für UI-SPEC-Komponenten-Inventare, ein erzwungenes Rollen-Register in `docs/INVENTORY.md` und ein Opt-in-Mechanismus für absichtliche Löschungen beim Worktree-Cleanup hinzu. Das ist leistungsfähig, aber deutlich weniger "schlank" als frühere Versionen und erhöht Konfigurations-, Installations- und Governance-Aufwand. Installation über `npx @opengsd/gsd-core@latest`; Einstieg über `/gsd-new-project` oder `/gsd-onboard`. Relevant als Referenz für frischen Kontext pro Executor, persistente Projektzustände und explizite Verification-Gates.

---

## openai/codex

- **URL:** https://github.com/openai/codex
- **Stars:** ⭐ 123.956
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 6.504 · **Größe:** 64M
- **Struktur:** Monorepo mit Rust-Kernimplementierung (`codex-rs`, ~109 Crates: Core-Agent-Loop, Sandboxing, MCP-Server, TUI, App-Server), einem dünnen npm-Wrapper (`codex-cli`) sowie separaten Python- und TypeScript-SDKs (`sdk/`), zusätzlich Bazel- und Nix-Build-Tooling — kein Skill-/Plugin-Paket im Claude-Code-Sinne. <!-- manual -->

Codex CLI ist OpenAIs lokal laufender Coding-Agent, das direkte Gegenstück zu Claude Code. Kern ist in Rust implementiert (`codex-rs`, dutzende Crates für Agent-Loop, Sandbox unter Linux/macOS/Windows, MCP-Client/-Server, App-Server-Protokoll, TUI, Cloud-Tasks-Integration), umgeben von einem npm-Distributionspaket (`codex-cli`) sowie offiziellen Python- und TypeScript-SDKs zur programmatischen Steuerung. Installation erfolgt über Shell-/PowerShell-Installer, npm, Homebrew oder vorgefertigte Release-Binaries; Build-Infrastruktur nutzt zusätzlich Bazel und Nix, was auf hohe interne Komplexität und Multi-Plattform-Anspruch (inkl. nativer Windows-Sandbox) hindeutet. Authentifizierung läuft primär über ChatGPT-Abo (Plus/Pro/Business/Enterprise) oder alternativ API-Key. Anders als reine Skill-Repos handelt es sich um den vollständigen Quellcode eines konkurrierenden Agenten-Produkts, inklusive eigenem Skills-/Hooks-/Plugin-System (`codex-rs/skills`, `codex-rs/hooks`, `codex-rs/plugin`) und Cloud-Anbindung (ChatGPT/Codex Web). Als Vergleichsreferenz zeigt das Repo, wie OpenAI CLI-Agent, Sandboxing, MCP-Interop und SDK-Ökosystem architektonisch löst. Die Entwicklung im August 2026 kreist auffällig um zwei Themen: "Guardian"-Review-Threads, die als eigene Thread-Art von Subagenten unterschieden und über Thread-Quellen-Metadaten klassifiziert werden, sowie durchgängig typisierte Inhaltsarten für Nutzereingaben und Kontextfragmente – die Grundlage dafür, Memory-Konsolidierung als eigene Anfrageart zu erkennen und Annotationen beim Zusammenführen von Nachrichten zu erhalten. Risiken: sehr großer, stark OpenAI-spezifischer Rust-Monorepo-Umfang, Abhängigkeit von ChatGPT-Konto/Cloud-Diensten, hohe Build-Komplexität (Bazel/Nix) erschwert eigenständiges Nachvollziehen oder Wiederverwendung einzelner Komponenten. Apache-2.0-lizenziert.

---

## OthmanAdi/planning-with-files

- **URL:** https://github.com/OthmanAdi/planning-with-files
- **Stars:** ⭐ 26.870
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 610 · **Größe:** 14M
- **Struktur:** 6× SKILL.md · Ordner: skills, commands · Spiegelordner: .agents, .codebuddy, .codex, .continue, … (+9) (generiert)

"Planning with Files" ist ein dateibasierter Planungs-Skill, der dem Muster von Manus (der für 2 Mrd. USD von Meta übernommenen Agentenfirma) folgt: Für jede komplexe Aufgabe legt der Agent drei persistente Markdown-Dateien an – `task_plan.md` (Phasen/Fortschritt), `findings.md` (Rechercheergebnisse) und `progress.md` (Session-Log). Kernprinzip: Das Kontextfenster ist wie flüchtiges RAM, das Dateisystem wie persistente Festplatte – alles Wichtige wird auf Platte geschrieben statt im Kontext zu verbleiben. Hooks (bis zu 8, je nach Agent) lesen den Plan vor wichtigen Entscheidungen erneut ein, erinnern nach Datei-Schreibvorgängen an Status-Updates und verifizieren Vollständigkeit vor dem Stoppen (Stop-Hook, optional gated Modus seit v3.0). Damit übersteht der Agent Kontextverlust, `/clear` und Abstürze und erholt sich automatisch (Session Recovery). Mittlerweile bei v3.11 unterstützt der Skill 60+ Agenten über den Agent-Skills-Standard, davon 18+ mit dokumentiertem, gestuftem Support: volle Hook-Integration bei Claude Code, Cursor, Codex u.a., reine SKILL.md-Erkennung bei Continue, Pi, OpenClaw u.a., und seit v3.7.0 zusätzlich ein in-Tree-Pfad ohne Tool-Setup. Der Self-Check-Befehl `/plan-doctor` (v3.6.0+) prüft Plan-Auflösung, Injection und Installationsoberflächen und deckt damit typische, sonst stille Fehlerquellen auf. Die Sprachvarianten liegen jetzt gebündelt unter `skills/i18n`, damit das Plugin nur einen Skill registriert statt vieler Dubletten, und ein Planning-Opt-out wird auch auf den Cursor- und Copilot-Routen respektiert. Laut eigener Evaluation steigt die Aufgaben-Erfolgsquote von 6,7% ohne auf 96,7% mit Skill. Sehr relevant als konkretes, breit erprobtes Muster für strukturierte Notizen/Planpersistenz gegen Kontext-Rot.

---

## paperclipai/paperclip

- **URL:** https://github.com/paperclipai/paperclip
- **Stars:** ⭐ 80.632
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 4.883 · **Größe:** 110M
- **Struktur:** Node.js-/React-Monorepo in `packages/` mit CLI, Server und UI; Agenten-/Skill-Integrationen in `.agents/`, `.claude/` und `plugins/`; Betriebsartefakte in `docker/`, `evals/` und `docs/` <!-- manual -->

Paperclip ist eine selbst hostbare Control Plane für Teams von AI-Agenten. Es modelliert eine Organisation statt nur einzelner Chats: Ziele, Firmen, Projekte, Org-Charts, Rollen, Tickets und Entscheidungswege bilden den Kontext; Agents verschiedener Runtimes wie Claude Code, Codex, Cursor, OpenClaw, Bash oder HTTP-Bots können Aufgaben über Heartbeats abarbeiten. Die React-Oberfläche und der Node.js-Server kombinieren Task-Tracking mit Budgetlimits, Kostenmessung, Governance-/Approval-Gates, Workspaces und Worktrees, Routinen, Plugin-Workers, Secret-Handling und einem dauerhaften Audit-Log. Bemerkenswert sind die als atomar beschriebenen Task-Checkouts und Budgetgrenzen sowie Mehrfirmen-Isolation und Export/Import mit Secret-Scrubbing. Relevant als umfassendes Referenzsystem für den Schritt vom Agenten-Workflow zur operativen AI-Organisation – besonders für Zielvererbung, Kostenkontrolle und menschliche Eingriffsrechte. Es ist ausdrücklich nicht für einen einzelnen Agenten gedacht und ersetzt keine Code-Review- oder Agenten-Framework-Entscheidung. Wegen Workspaces, Secrets, Schedules, automatischer Ausführung, Kosten und Tenant-Isolation ist jede produktive Einführung ein Security-, Billing- und Governance-Projekt und benötigt vorher eine separate Architektur- und Freigabeentscheidung. MIT-lizenziert.

---

## pbakaus/impeccable

- **URL:** https://github.com/pbakaus/impeccable
- **Stars:** ⭐ 67.882
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 3.267 · **Größe:** 61M
- **Struktur:** Quelle in `skill/` (`SKILL.src.md` + `reference/<command>.md`), generierte Provider-Ausgaben in `plugin/skills/` bzw. `.claude/skills/`, `.cursor/skills/` usw. <!-- manual -->

Design-Guidance für KI-Coding-Agenten von Paul Bakaus, explizit als Weiterentwicklung von Anthropics `frontend-design`-Skill positioniert. Besteht aus einem einzigen Skill `impeccable` mit 23 Unterbefehlen (`/impeccable init`, `craft`, `polish`, `audit`, `critique`, `bolder`, `quieter`, `distill`, `animate`, `live` u.v.m.) plus inzwischen 59 deterministischen Detektor-Regeln, die typische KI-Generik, Accessibility-Probleme und allgemeine Designfehler erkennen (Inter-Schriftart überall, Lila-Blau-Verläufe, verschachtelte Cards, graue Schrift auf farbigem Hintergrund). `/impeccable init` legt einmalig `PRODUCT.md` und optional `DESIGN.md` an, die Zielgruppe, Marken-/Produkt-Register, Stimme, Anti-Referenzen, Farben, Typografie und Komponenten festhalten. Live-Modus erlaubt visuelle Iteration direkt im Browser; Regeln lassen sich projektbezogen konfigurieren oder begründet inline unterdrücken. Installierbar per CLI (`npx impeccable install`), Git-Submodule, Plugin oder manuellem Kopieren für über zehn Tools; ein providernativer Hook prüft Verstöße direkt bei Datei-Edits. Apache-2.0-lizenziert. Sehr relevant als ausgereiftes Anti-Slop-Design-Tool neben `taste-skill` und `emilkowalski/skills` – mit dem Alleinstellungsmerkmal deterministischer Detektor-Regeln und Live-Browser-Iteration.

---

## petergyang/human-review

- **URL:** https://github.com/petergyang/human-review
- **Stars:** ⭐ 1.258
- **Heruntergeladen:** 2026-09-14
- **Zuletzt aktualisiert:** 2026-09-14
- **Dateien:** 52 · **Größe:** 1,8M
- **Struktur:** Node-CLI statt Skill-Paket: `src/` enthält CLI, lokalen Server, Browser-Client, Markdown-Renderer und Setup, dazu `src/SKILL.md` als Agent-Anleitung; 20 Test-Dateien in `test/`; `design-ref/` und `spec.html` als Entwurfsmaterial <!-- manual -->

Lokales Node-Werkzeug mit mitgeliefertem Agent-Skill von Peter Yang, das den Umweg über getippte Änderungswünsche ersetzt: Statt im Chat zu beschreiben, welcher Satz im dritten Absatz anders lauten soll, öffnet der Agent die Datei im Browser. Dort lässt sich Text direkt bearbeiten, Formatierung, Listen und Links setzen, Bilder skalieren und verschieben, ganze Blöcke umsortieren und Elemente löschen; Kommentare hängen punktgenau an der markierten Stelle oder am angeklickten Element. Ein Klick auf Send schickt sämtliche Edits und Kommentare als ein Bündel zurück an den Agenten. Unterstützt werden HTML-Dateien, gerenderte Markdown-Dateien (die Quelldatei bleibt unangetastet, der Agent überträgt die Änderungen selbst) und laufende localhost-Seiten. Das eigentliche Muster steckt im Wartepunkt: `human-review poll` blockiert, bis der Mensch sendet, und weckt den Agenten dann mit dem gesamten Batch — in Claude Code als Hintergrundprozess, der den Zug beendet und später aufgeweckt wird. Damit ist menschliches Review ein benannter Schritt in der Agentenschleife statt einer Unterbrechung. Alles läuft lokal, ohne Account, Cloud oder API-Key; 19 Test-Dateien decken unter anderem Sicherheit, Feedback-Integrität und Frame-Policy ab. Aktiv gepflegt (Version 0.8.1, 52 Commits, zuletzt 04.09.2026), MIT-lizenziert. Vor einer Übernahme zu prüfen: `npx -y human-review setup --global` schreibt den Skill in globale Agenten-Konfigurationen, und HTML-Edits speichern direkt in die Datei.

---

## router-for-me/CLIProxyAPI

- **URL:** https://github.com/router-for-me/CLIProxyAPI
- **Stars:** ⭐ 51.695
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 1.373 · **Größe:** 16M
- **Struktur:** Go-Server in `cmd/` und `internal/`, SDK und Beispiele in `sdk/` und `examples/`, Betriebs-/API-Dokumentation unter `docs/`; kein Skill-Paket <!-- manual -->

CLIProxyAPI ist ein in Go implementierter lokaler Proxy, der OpenAI-, Gemini-, Claude-, Codex- und Grok-kompatible API-Schnittstellen für CLI- und SDK-Clients bereitstellt. Er unterstützt laut README OAuth-Logins für Codex, Claude Code und Grok Build, mehrere Accounts mit Round-Robin-Load-Balancing, Streaming, Tool Calling, multimodale Eingaben sowie konfigurierbare OpenAI-kompatible Upstreams. Zusätzlich gibt es eine Management-API, eine einbettbare Go-SDK und ein großes Umfeld von Dashboards, Tray-Apps und Account-/Quota-Tools. Das kann für lokale Tests, Provider-Abstraktion oder die Analyse von API-Übersetzern technisch interessant sein. Gleichzeitig ist es Infrastruktur mit besonders hohem Risiko: OAuth-Tokens, API-Keys, Requests und Account-Pools werden zentral verarbeitet; die README enthält zahlreiche Sponsor-/Relay-Angebote und verweist auf Drittanbieter-Zugänge. Daher ausschließlich als Analyse- und Referenzquelle behandeln. Eine produktive Nutzung erfordert vorab eine genaue Prüfung der OAuth-Abläufe, Secret-Speicherung, Netzwerk-Exposition, Logging, Providerbedingungen, Rechtslage und Account-Compliance sowie Philipps explizite Freigabe. MIT-lizenziert, wobei die Lizenz keine Freigabe für die Nutzung von Provider-Accounts oder Drittservices ersetzt.

---

## rtk-ai/rtk

- **URL:** https://github.com/rtk-ai/rtk
- **Stars:** ⭐ 80.246
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 412 · **Größe:** 4,2M
- **Struktur:** Rust-CLI in `src/`; Integrationen als `hooks/`, `.claude/` und `openclaw/`; 12× SKILL.md für Agenten-Anleitungen <!-- manual -->

RTK („Rust Token Killer“) ist eine einzelne Rust-CLI, die Shell-Ausgaben vor der Übergabe an einen Coding-Agenten verdichtet. Statt Agenten ihre Arbeitsweise neu lernen zu lassen, können Hooks Bash-Aufrufe wie `git status`, `rg`, Test-Runner, Build-Tools, Cloud-CLIs oder Container-Kommandos transparent auf `rtk` umschreiben; der Agent erhält gefilterte, gruppierte, gekürzte und deduplizierte Ergebnisse. Zusätzlich bietet das Tool direkte Befehle für Dateien, Git, GitHub, Tests, Linting, Paketmanager, AWS, Docker und Analytics über erzielte Einsparungen. Unterstützt werden laut README zahlreiche Agenten, darunter Claude Code, Codex, Gemini CLI, Cursor, OpenCode und Copilot. Wichtig ist die dokumentierte Grenze: eingebaute Read-/Grep-/Glob-Tools eines Agenten passieren den Bash-Hook nicht. RTK enthält außerdem eine optionale, standardmäßig deaktivierte anonyme Telemetrie. Relevant als fokussierter Gegenentwurf zu großen Kontext-Frameworks: es optimiert vor allem die terminalbasierte Datenquelle, ohne den gesamten Prompt- oder Memory-Stack zu ersetzen. Für eine Produktivnutzung sind die globalen Hooks, die lokale Aufzeichnung von Roh-Ausgaben bei Fehlern („tee“) und die Telemetrie-Einstellung bewusst zu prüfen. Apache-2.0-lizenziert.

---

## shadcn-ui/ui

- **URL:** https://github.com/shadcn-ui/ui
- **Stars:** ⭐ 123.709
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 5.762 · **Größe:** 45M
- **Struktur:** 2× SKILL.md · Ordner: skills, agents, commands, hooks, rules · Spiegelordner: .cursor (generiert)

Das offizielle shadcn/ui-Monorepo ist die Quelle für die CLI, Komponenten, Registry- und Template-Logik sowie zwei Agent-Skills: `shadcn` und `migrate-radix-to-base`. Neu im Monorepo ist `@shadcn/helpers`, eine Sammlung von Helfern zum Bauen von AI-Anwendungen (u.a. ein deklarativer `createChat`-Builder, mit dem Konversationen inklusive Reasoning-, Tool-Call- und Streaming-Verläufen für Entwicklung und Tests nachgestellt werden); die Registry-CLI unterstützt jetzt zusätzlich private GitHub-Registries. Der zentrale `shadcn`-Skill arbeitet nicht als allgemeiner Designratgeber, sondern als projektbewusste Arbeitsanweisung für Projekte mit `components.json`: Er liest die tatsächliche Konfiguration (Alias, Framework, Tailwind-Version, Komponenten, Icon-Bibliothek und Primitive-Base), sucht vorhandene Komponenten, ruft versionsnahe Dokumentation ab und empfiehlt Komposition statt selbst gebauter UI-Duplikate. Seine Regeln zu semantischen Farben, `gap` statt `space-*`, Accessibility-Titeln in Overlays, Form-Komposition und vorsichtigen Component-Updates sind als Referenz sehr wertvoll. Das Repo ist jedoch ein großes, aktiv entwickeltes pnpm/Turbo-Monorepo; seine Build-, Release- und Template-Sync-Scripts sind nicht für dieses Mutter-Repo bestimmt. Insbesondere `scripts/sync-templates.sh` löscht Inhalte in temporären Klonen und darf nur nach vollständigem Verständnis ausgeführt werden. Der Skill selbst erlaubt `npx`/`pnpm dlx`/`bunx shadcn@latest` und kann über Registries Quellcode in Zielprojekte einbringen. Vor jeder produktiven Nutzung: Registry explizit wählen, `--dry-run`/`--diff` verwenden, hinzugefügte Dateien prüfen und niemals Überschreiben ohne Freigabe ausführen. Als offizielle Referenz und selektiv aktivierbarer Projekt-Skill geeignet, nicht als pauschaler globaler Standard. MIT-lizenziert.

---

## shadcn/improve

- **URL:** https://github.com/shadcn/improve
- **Stars:** ⭐ 9.116
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-07-10
- **Dateien:** 9 · **Größe:** 61K
- **Struktur:** 1× SKILL.md · Ordner: skills, references

Kleiner, fokussierter Agent-Skill von shadcn: auditiert eine beliebige Codebasis mit einem leistungsstarken (teuren) Modell und schreibt daraus präzise, in sich geschlossene Umsetzungspläne, die anschließend von günstigeren Modellen oder anderen Agenten ausgeführt werden können. Der Skill implementiert selbst nie Code – "der Plan ist das Produkt". Ablauf: Recon (Repo-Struktur, Build/Test/Lint-Befehle, vorhandene ADRs/PRDs erfassen) → Audit (parallele Subagenten über neun Kategorien: Korrektheit, Sicherheit, Performance, Testabdeckung, technische Schulden, Abhängigkeiten, Developer Experience, Doku, Richtung/Feature-Vorschläge) → Vet (Advisor prüft jeden gemeldeten Fund selbst nach, verwirft Fehlalarme) → Priorisierung (Impact/Aufwand) → Plan-Erstellung (eine Datei pro gewähltem Finding, mit exakten Dateipfaden, Code-Ausschnitten, Verifikationsbefehlen und klaren Grenzen). Kann Pläne auch direkt an einen günstigeren Executor-Agenten in einem isolierten Git-Worktree übergeben und dessen Ergebnis wie ein Tech Lead gegenprüfen, oder Pläne als GitHub Issues veröffentlichen. Relevant als schlankes Vorbild für Audit-zu-Plan-Workflows mit klarer Trennung zwischen teurem Planungsmodell und günstigem Ausführungsmodell.

---

## shanraisshan/claude-code-best-practice

- **URL:** https://github.com/shanraisshan/claude-code-best-practice
- **Stars:** ⭐ 65.907
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 454 · **Größe:** 74M
- **Struktur:** kein Skill-Paket, sondern Wissensbasis: `best-practice/`, `reports/`, `tips/` (die eigentlichen Inhalte); Demo-Setup in `.claude/agents/`, `.claude/commands/`, `.claude/skills/` <!-- manual -->

Eine sehr umfangreiche, laufend aktualisierte Sammlung von Claude-Code-Best-Practices ("from vibe coding to agentic engineering"): keine Skill-Sammlung, sondern eine kuratierte Wissensbasis über Subagenten, Commands, Skills, Hooks, MCP-Server, Settings, Memory, Worktrees u.v.m., mit Verweisen auf offizielle Doku und eigenen Implementierungsbeispielen (u.a. ein Wetter-Demo-Workflow nach dem Muster Command → Agent → Skill). Besonders wertvoll: eine vergleichende Tabelle konkurrierender Entwicklungs-Workflow-Methodologien (Superpowers, ECC, Matt-Pocock-Skills, gstack, Spec Kit, GSD, BMAD-METHOD u.a.) mit Stern-Zahlen und Schritt-für-Schritt-Ablauf, sowie separate Tabellen für reine Skill- und Agenten-Sammlungen. Enthält zudem 83 gesammelte "Tips and Tricks" aus der Community (u.a. von Boris Cherny, Mitentwickler von Claude Code) zu Prompting, Planung, Kontextmanagement, Session-Handling, CLAUDE.md-Gestaltung, Hooks, Git/PR-Workflow und Debugging – z.B. "Context Rot setzt bei ~300-400k Tokens ein" oder "PRDs in vertikale Slices statt horizontale Phasen zerlegen". Sehr relevant als Meta-Referenz: liefert sowohl konkrete, sofort anwendbare Tipps als auch eine Landkarte weiterer relevanter Repos, von denen einige bereits im eigenen Index enthalten sind.

---

## teng-lin/notebooklm-py

- **URL:** https://github.com/teng-lin/notebooklm-py
- **Stars:** ⭐ 19.304
- **Heruntergeladen:** 2026-07-14
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 1.446 · **Größe:** 75M
- **Struktur:** 1× SKILL.md

`notebooklm-py` ist ein aktiver, MIT-lizenzierter Python-Client für Google NotebookLM (seit Juli 2026 von Google zu "Gemini Notebook" umbenannt; gleiches Produkt, automatische Weiterleitungen, keine API-Änderung – das Paket behält seinen Namen) mit asynchroner API, CLI, optionalem MCP- und lokalem REST-Server sowie einem mitgelieferten Agent-Skill für Claude Code, Codex und kompatible Hosts. Er automatisiert Notebooks, Quellenimporte aus URLs, Dateien, YouTube und Google Drive, quellengebundene Fragen mit Zitaten, Deep Research sowie die Erstellung und den Download von Audio-/Video-Überblicken, Slides, Infografiken, Reports, Quizzen, Flashcards, Datentabellen und Mindmaps. Damit eignet sich das Projekt als Referenz und optionales Werkzeug, um umfangreiche Dokumentbestände von NotebookLM verdichten und für Agent-Workflows als persistenten, quellengebundenen Wissensspeicher abfragen zu lassen. Die CLI bietet strukturierte JSON-Ausgaben und getrennte Profile, was parallele Agentenläufe erleichtert. Version 0.8.1 ergänzt Notebook-Collections auf Kontoebene, deutlich reichere Quellen-Metadaten (Status-/Typ-Filter, exakte Zählungen, Drive-Health, Wortzahlen, Revisionsstempel), offset-genaue Zitationsdaten für die Ausrichtung von Antwort und Quelle sowie einen eigenständigen Research-Import. Für die Cookie-Übernahme aus dem Browser wurde von `rookiepy` auf `rookie-cookies` migriert. Die praktische Einschränkung ist wesentlich: Das Projekt nutzt nicht dokumentierte Google-APIs, kann deshalb ohne Vorwarnung brechen, Rate Limits oder Kontobeschränkungen auslösen und ist nicht mit Google verbunden. Die Anmeldung verwaltet sensible Google-Session-Cookies lokal; Cookie-Dateien und Browserprofile müssen geschützt und aus Git ausgeschlossen bleiben. Optionale Browser-, Cookie-, MCP- und Server-Abhängigkeiten erweitern die Angriffs- und Wartungsfläche. Daher zunächst nur als lokale Referenz nutzen; eine produktive Integration, insbesondere mit Firmenquellen, Remote-MCP oder geteilten Credentials, erfordert vorherige Sicherheits- und Datenschutzprüfung sowie Philipp-Freigabe.

---

## thedaviddias/Front-End-Checklist

- **URL:** https://github.com/thedaviddias/Front-End-Checklist
- **Stars:** ⭐ 74.132
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 1.875 · **Größe:** 11M
- **Struktur:** Umfangreiches pnpm/Turborepo-Monorepo mit Next.js-Web-App (`apps/web/`), MCP-Server, CLI und Regel-Content in `packages/`, plus separatem `skills/`-Ordner mit 390 generierten SKILL.md-Dateien (je mit `references/rule.md`) — kein reiner Checklisten-Dokumentenordner, sondern ein produktionsreifes Softwareprodukt mit Skill-Paket als Nebenprodukt. <!-- manual -->

Front-End-Checklist begann als reine Markdown-Checkliste für Frontend-Qualitätssicherung und hat sich zu einem vollständigen Monorepo-Produkt entwickelt: eine Next.js-Website (frontendchecklist.io), ein gehosteter MCP-Server mit elf Tools (u. a. search_rules, check_rule, fix_rule, explain_rule, audit_url), eine CLI sowie 385 einzelne Regeln als MDX-Content. Aus diesen Regeln werden automatisiert 390 Claude-Skills generiert (`skills/<name>/SKILL.md` plus `references/rule.md`), die jeweils Quick-Reference, Check-, Fix-, Explain- und Code-Review-Abschnitte enthalten und auf WCAG-, Performance-, SEO- und Security-Quellen verweisen. Technologisch handelt es sich um ein TypeScript-/pnpm-/Turborepo-Setup mit Prisma, Zod, Better-Auth und Content-Collections; AGENTS.md dokumentiert explizit MCP-Nutzungsregeln für Coding-Agenten. Relevant ist das Repo für Skill-Bibliotheken zu Frontend-Review (Accessibility, Performance, SEO, Sicherheit) und als Beispiel dafür, wie eine kuratierte Regel-Quelle automatisiert in Agenten-Skills und MCP-Tools übersetzt wird. Einschränkungen: sehr große, teils redundante Skill-Menge (390 Dateien) ohne eigene Kuration nötig, starke Bindung an den gehosteten MCP-Server und die eigene Content-Pipeline, keine LICENSE-Datei im lokalen Klon trotz MIT-Verweis in der README, sowie hohe Komplexität durch Vollausbau als Produkt statt einfacher Referenzdokumentation.

---

## thedotmack/claude-mem

- **URL:** https://github.com/thedotmack/claude-mem
- **Stars:** ⭐ 93.817
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 1.025 · **Größe:** 119M
- **Struktur:** Quellcode überwiegend in `src/` (CLI, Worker-Service, Server/MCP, SQLite/Chroma-Storage) sowie ein gebauter Claude-Code-Plugin-Artefakt unter `plugin/` mit eigenen `skills/`, `hooks/`, `modes/`-Unterordnern und weiteren Skill-/Hook-Ordnern unter `.claude/` und `openclaw/` — kein reines Skill-Repo, sondern eine vollwertige Anwendung, die sich selbst als Plugin ausliefert. <!-- manual -->

Claude-Mem ist ein persistentes Gedächtnis- und Kompressionssystem für Claude Code (sowie OpenCode, Antigravity CLI, Cursor, OpenClaw-Gateways), das Tool-Nutzungsdaten während Coding-Sessions über Lifecycle-Hooks abgreift, mittels Claude Agent SDK zu semantischen Zusammenfassungen komprimiert und in einer lokalen SQLite-Datenbank plus Chroma-Vektor-DB für hybride Semantik-/Keyword-Suche ablegt. Ein lokaler Worker-Service (verwaltet via Bun) stellt HTTP-API, Web-Viewer und MCP-Suchtools nach einem Progressive-Disclosure-Muster bereit. Neuere Releases ergänzen eine zweispurige, standardmäßig deaktivierte Cloud-Synchronisierung über einen pro Benutzer isolierten Sync-Hub; ohne explizite Hub-Konfiguration verlassen keine Erinnerungen den Rechner. Ein großer Fix-Lauf adressiert Windows-Prozesse, Suchranking, Datenintegrität, Worker-Neustarts und Codex-Kontextinjektion – zugleich zeigen kritische Restart- und Migrationsfehler, wie komplex und beweglich die Architektur bleibt. Seit v13.15 ist das Projekt merklich stärker kommerzialisiert: Der `npx claude-mem install`-Installer führt einen vollständigen Funnel für eine kostenlose CMEM-Pro-Woche durch (Pitch, E-Mail-Eingabe, Magic-Link, Stripe-Checkout, Pairing-Polling), abgesichert über einen im Browser zu bestätigenden Device-Code; Modellpreise werden live vom Backend geladen statt hart kodiert. Zudem warnt die Session jetzt, wenn keine Beobachtungen mehr eintreffen. Relevant für projektübergreifende Kontinuität und als Referenz für Hook-Architektur und MCP-Suche – vergleichbar mit [headroomlabs-ai/headroom](#headroomlabs-aiheadroom), aber auf semantisches Session-Gedächtnis fokussiert. Einschränkungen: hoher Laufzeit-Overhead (Bun, uv/Python für Chroma, SQLite, Dauerprozess-Worker), starke Kopplung an Plugin-Runtimes sowie optionale Cloud-Sync- und Token-Nebenaspekte. Apache-2.0-lizenziert.

---

## upstash/context7

- **URL:** https://github.com/upstash/context7
- **Stars:** ⭐ 61.975
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 410 · **Größe:** 21M
- **Struktur:** TypeScript-Monorepo in `packages/`; Agenten-Installationen, Regeln und Skills unter `plugins/`, `rules/` und `skills/`; Provider-Spiegel in `.agents/` und `.claude-plugin/` <!-- manual -->

Context7 bringt aktuelle, versionsbezogene Library-Dokumentation und Codebeispiele in den Kontext eines Coding-Agenten. Dafür gibt es zwei Modi: Die `ctx7`-CLI installiert eine Skill-Anleitung, über die Agenten Bibliotheken suchen und passende Dokumentauszüge abfragen, oder ein MCP-Server stellt native Tools zur Auflösung einer Library-ID und zur Docs-Abfrage bereit. Prompts können eine konkrete Context7-ID wie `/vercel/next.js` oder eine gewünschte Version nennen, um die Suche zu präzisieren. Das Ziel ist, alte Modellkenntnis, halluzinierte APIs und generische Beispiele durch quellennähere Informationen zu ersetzen. Die README weist zugleich darauf hin, dass die zugrundeliegenden Library-Projekte Community-Beiträge sind und Richtigkeit, Vollständigkeit oder Sicherheit nicht garantiert werden; Backend, Parser und Crawler sind nicht Teil dieses öffentlichen Repositories. Eine API-Key-Anmeldung erhöht Limits, und die automatisierte Installation verändert Agenten-Konfigurationen. Neu gibt es ein Context7-Plugin für OpenCode, OAuth über Clerk als ausgewiesenen Issuer und Integrationsleitfäden für weitere Hosts (u.a. OpenClaw, Gerrit). Relevant als leichtgewichtige Ergänzung für Library-/API-Arbeit und als Muster für CLI- plus MCP-Dualität. Für produktive Nutzung sind API-Key, Telemetrie/Datentransfer, die Vertrauenswürdigkeit einzelner Dokumentquellen und die automatisierten Konfigurationsänderungen zu prüfen. MIT-lizenziert.

---

## vercel-labs/agent-skills

- **URL:** https://github.com/vercel-labs/agent-skills
- **Stars:** ⭐ 31.173
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 446 · **Größe:** 7,5M
- **Struktur:** 9× SKILL.md · Ordner: skills, rules, references

Kompakte, von Vercel Engineering kuratierte Sammlung von neun Skills nach dem Agent-Skills-Standard: `vercel-optimize` (Audit von Vercel-Projekten auf Kosten/Performance/Caching/Function-Nutzung), `react-best-practices` (40+ priorisierte React/Next.js-Performance-Regeln in 8 Kategorien, z.B. Waterfall-Vermeidung, Bundle-Size), `web-design-guidelines` (100+ Regeln zu Accessibility, Fokus-States, Formularen, Animation, Typografie, Dark Mode), `writing-guidelines` (80+ Regeln aus dem Vercel-Schreibhandbuch zu Tonalität, Struktur, Code-Beispielen, Typografie), `react-native-skills` (Performance/Architektur für React Native/Expo), `react-view-transitions` (React View Transition API, Next.js-Integration, inkl. vorab geladener Route-Transitions), `composition-patterns` (React-Komposition statt Boolean-Prop-Wildwuchs), `deploy-to-vercel` (sofortiges Deployment aus der Konversation heraus, mit übertragbarer Ownership) und `vercel-cli-with-tokens` (CLI-Nutzung mit Access-Tokens). Neu veröffentlicht das Repo zusätzlich einen Agent-Skills-Discovery-Index nach dem Well-Known-Entwurf der Spezifikation und liefert je Skill ein ZIP-Artefakt – interessant als Referenz dafür, wie Skill-Auffindbarkeit über Repo-Grenzen hinweg standardisiert werden soll. Installation einheitlich über `npx skills add vercel-labs/agent-skills`. Besonders relevant als unmittelbar einsetzbare, hochwertige Referenz-Skills für Frontend-Qualität (Performance, Accessibility, Schreibstil) – die `web-design-guidelines` und `react-best-practices` sind direkt vergleichbar mit den bereits genutzten Skills `web-design-guidelines` bzw. `vercel-react-best-practices` im eigenen Environment.

---

## vercel-labs/skills

- **URL:** https://github.com/vercel-labs/skills
- **Stars:** ⭐ 31.577
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 118 · **Größe:** 1016K
- **Struktur:** kein Skill-Inhalt — das ist die Installer-CLI selbst, Quellcode in `src/` <!-- manual -->

Das ist keine Skill-Sammlung, sondern die CLI (`npx skills`) für das offene Agent-Skills-Ökosystem – das zugrundeliegende Werkzeug, mit dem Skills aus beliebigen GitHub-/GitLab-Repos oder lokalen Pfaden in über 70 unterstützte Coding-Agenten (Claude Code, Cursor, Codex, OpenCode, Windsurf, Antigravity, Gemini CLI, GitHub Copilot u.v.m.) installiert werden – per Symlink (empfohlen, eine kanonische Kopie) oder Kopie, projekt- oder global-scoped. Zentrale Befehle: `skills add <source>` (installieren, mit Filtern nach Skill-Namen/Agenten), `skills use <source>` (Skill ohne Installation testen, druckt generierten Prompt oder startet Agent direkt), `skills list`, `skills find` (interaktive/keyword-Suche, auch über alle Repos eines Owners), `skills update`, `skills remove`, `skills init` (neues SKILL.md-Template). Erkennt Skills automatisch über verschiedene Ablage-Konventionen (`skills/`, `.claude/skills/`, Root-`SKILL.md` etc.) inkl. Claude-Plugin-Marketplace-Manifesten. Jüngere Versionen ergänzen einen Select-all-Schalter im interaktiven Skill-Picker, Unterstützung für Posit Assistant als weiteren Agenten, gesicherte Authentifizierung für private Repositories und schärfere Grenzen beim Wildcard-Install (interne Well-known-Skills bleiben ausgeschlossen). Über die Website skills.sh können Skills durchsucht werden. Sehr relevant als das faktische Standard-Werkzeug, mit dem praktisch alle anderen in diesem Index gelisteten Skill-Repos installiert werden – guter Kandidat, um das eigene Skill-Handling zu vereinheitlichen.

---

## VoltAgent/awesome-design-md

- **URL:** https://github.com/VoltAgent/awesome-design-md
- **Stars:** ⭐ 115.761
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 153 · **Größe:** 2,1M
- **Struktur:** keine Standard-Skill-/Agent-Ordner (Quellcode/CLI oder reine Doku)

Awesome-design-md ist eine von VoltAgent kuratierte Sammlung von rund 70 DESIGN.md-Dateien, die das von Google Stitch eingeführte Format für maschinenlesbare Design-Systeme nutzen. Jede Datei beschreibt für eine bekannte Marke (u.a. Stripe, Apple, Notion, Tesla, Figma) Farbpalette, Typografie-Hierarchie, Komponentenstile, Spacing/Grid, Schatten/Elevation, Responsive-Regeln sowie Do's/Don'ts als strukturiertes YAML-artiges Markdown mit kurzem Agenten-Prompt-Leitfaden. Das Konzept ist analog zu AGENTS.md gedacht: Während AGENTS.md Coding-Agenten sagt, wie gebaut wird, sagt DESIGN.md Design-/Coding-Agenten, wie es aussehen soll. Nutzer kopieren die Datei ins Projektroot und weisen den KI-Agenten an, UI im jeweiligen Stil zu generieren. Es handelt sich um reine, textuelle Referenzdaten ohne Automatisierungslogik, Parser oder Tooling – kein Skill-/Plugin-System, kein Code. Besonders nützlich ist die Sammlung als Prompt-Kontext-Baustein für UI-generierende Agenten und Workflows: Design-Konsistenz per Drop-in-Datei, nicht als Skill oder Agent selbst. Sie ergänzt damit die eher regelbasierten Design-Skills wie [nextlevelbuilder/ui-ux-pro-max-skill](#nextlevelbuilderui-ux-pro-max-skill) um fertige, markenspezifische Tokens. Einschränkungen: Werte sind aus öffentlich sichtbarem CSS extrahiert (keine Garantie auf Aktualität/Rechtmäßigkeit bei Markenänderungen), es gibt keine Validierung/Tests der Tokens, Qualität hängt von der ursprünglichen Extraktion ab, und das Projekt ist stark durch das kommerzielle Angebot getdesign.md/VoltAgent getrieben (Sponsoring-Banner, Marketingsprache im README). MIT-lizenziert.

---

## wshobson/agents

- **URL:** https://github.com/wshobson/agents
- **Stars:** ⭐ 39.636
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-08-23
- **Dateien:** 1.157 · **Größe:** 7,7M
- **Struktur:** 181× SKILL.md · Ordner: skills, agents, commands, hooks, plugins, references · Spiegelordner: .agents, .cursor, .cursor-plugin (generiert)

Ein sehr umfangreicher "Agentic Plugin Marketplace": 92 Plugins, 202 Agenten, 181 Skills und 105 Commands (u.a. neu: `avoid-ai-writing` gegen typische KI-Schreibmuster, `pptx-deck-creation` für Präsentationserstellung sowie `llm-finetuning` und `dgx-spark-ops` für eine Eval-gesteuerte Fine-Tuning-Pipeline), aus einer einzigen Markdown-Quelle (`plugins/`) generiert und nativ auf fünf Harnesses ausgespielt (Claude Code als Quelle der Wahrheit, plus Codex CLI, Cursor, OpenCode, Gemini CLI, GitHub Copilot) – jeweils mit harness-nativen Artefakten statt kleinstem gemeinsamen Nenner. Jedes Plugin ist isoliert und komponierbar (z.B. `plugins/python-development/` mit eigenen Agenten, Commands, Skills); die Installation eines Plugins lädt nur dessen Komponenten in den Kontext. Nutzt eine gestufte Modellstrategie (Fable 5/Opus für Architektur/Sicherheit, Sonnet für Doku/Tests, Haiku für operative Aufgaben) und ein dreistufiges Qualitäts-Eval-Framework (`plugin-eval`: statische Analyse, LLM-Judge, Monte-Carlo-Zuverlässigkeitstests). Enthält externe Memory-Integration (Pensyve) als Git-Subdir-Einbindung. Build-Tooling (`make generate-all`, `make validate`, `make garden`) hält alle Harness-Ausgaben synchron; die Garden-Prüfungen kontrollieren inzwischen auch Komponenten-Zahlen und Agenten-Divergenz. Ein Breaking Change im August 2026 verlegt das Gemini-CLI-Ziel auf die Google-Antigravity-CLI als Harness. Sehr relevant als Referenz für Multi-Harness-Distribution aus einer Quelle sowie für das eigene Qualitäts-Eval-Konzept für Skills/Plugins.
