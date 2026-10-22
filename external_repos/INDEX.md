# Index externer Repos

Lokale Referenzbibliothek geklonter GitHub-Repos für AI-gestützte Produkt- und Softwareentwicklung: bewährte Workflows vergleichen, einzelne Skills und Regeln studieren, Agenten-Setups verstehen und konkrete Lösungsansätze extrahieren — ohne erneut klonen zu müssen. Gepflegt gemäß `AGENTS.md` → „Fremde GitHub-Repos herunterladen".

- **Ablage:** `external_repos/<owner>/<repo-name>/` (Owner als Unterordner gegen Namenskollisionen, seit 2026-07-10).
- **Versionierung:** Die Analysekopien unter `external_repos/` sind nicht versioniert und nicht im Obsidian-Vault sichtbar; Index, erzeugte HTML-Bibliothek und Änderungsprotokolle bleiben versioniert.
- **Pflege:** Mechanische Felder (Dateien, Größe, Struktur, Übersicht) aktualisiert `70_Scripts/update_external_repos.py`; die Zusammenfassungen sind handgeschrieben.
- **HTML-Bibliothek:** [Offline öffnen](INDEX.html). Nach Inhaltsänderungen mit `python ai.py repos build` neu erzeugen; `python ai.py repos check` prüft Aktualität und Vollständigkeit. Der Repo-Update-Lauf erzeugt die HTML automatisch. Modulare Quellen und Anleitung: `70_Scripts/repo_library/`.

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
| Research, Planung und Implementierung getrennt durchführen | [humanlayer/skills](#humanlayerskills) | Dokumentierte RPI-Phasen mit frischen Sessions, visuellen Reviews und Vorlagen für begrenzte Agent-Schleifen |
| Agent-Arbeit nach Aufgabentyp routen und mit Laufzeitevidenz prüfen | [cursor/plugins](#cursorplugins) (`pstack`) | Engineering-Prinzipien, Task-Playbooks, Modellrollen, Verifikations- und Review-Workflows |
| Ein vollständiges Agile-Framework mit Rollen nutzen | [bmad-code-org/BMAD-METHOD](#bmad-code-orgbmad-method) | V7 Preview: Phasen, Expertenrollen, Sofia-Produktplanung und Toolsmith; stabile v6-Linie separat |
| Kontext über lange Aufgaben erhalten | [OthmanAdi/planning-with-files](#othmanadiplanning-with-files), [open-gsd/gsd-core](#open-gsdgsd-core) | Persistente Plan-, Findings- und Statusdateien sowie frische Kontexte pro Phase |
| Code testen, reviewen und sicher shippen | [addyosmani/agent-skills](#addyosmaniagent-skills), [garrytan/gstack](#garrytangstack), [shadcn/improve](#shadcnimprove) | Test-, Security-, Performance- und Code-Review-Workflows mit Verifikation |
| Agenten-Ergebnisse prüfen und Feedback gebündelt zurückgeben | [petergyang/human-review](#petergyanghuman-review) | Direktes Editieren und punktgenau verankerte Kommentare in HTML, Markdown oder localhost-Seiten, als ein Batch an den Agenten |
| React oder Next.js verbessern | [millionco/react-doctor](#millioncoreact-doctor), [vercel-labs/agent-skills](#vercel-labsagent-skills) | Deterministischer Audit mit CI-Gate sowie Performance-, Composition- und Accessibility-Regeln |
| Mit shadcn/ui-Komponenten bauen | [shadcn-ui/ui](#shadcn-uiui) | Projektbewusster `shadcn`-Skill: liest `components.json`, empfiehlt Komposition und saubere Registry-Nutzung |
| Designsystem-Regeln für Coding Agents durchsetzen | [shadcn-ui/lint](#shadcn-uilint) | Tailwind-v4-Regeln für Komponentenverträge, Theme-Tokens und hilfreiche ESLint-/Oxlint-Diagnosen |
| KI-typische Schreibmuster aus Texten entfernen | [petergyang/no-ai-slop](#petergyangno-ai-slop) | Über 20 benannte Slop-Muster, ein Detect-Modus ohne Umschreiben und eine Selbstprüfung nach jeder Bearbeitung |
| Web-Oberflächen mit fertigen CSS-Transitions animieren | [Jakubantalik/transitions.dev](#jakubantaliktransitionsdev) | 32 portable Transitions mit Motion-Tokens, Reduced-Motion-Guard, CLI und Live-Refine-Panel |
| Eine generische AI-Oberfläche aufwerten | [pbakaus/impeccable](#pbakausimpeccable), [Leonxlnx/taste-skill](#leonxlnxtaste-skill), [emilkowalski/skills](#emilkowalskiskills), [jakubkrehel/make-interfaces-feel-better](#jakubkrehelmake-interfaces-feel-better) | Anti-Slop-Regeln, Design-Taste, Animationen, visuelle Reviews und gezielte Polish-Workflows |
| Ein Design-System ableiten | [nextlevelbuilder/ui-ux-pro-max-skill](#nextlevelbuilderui-ux-pro-max-skill), [pbakaus/impeccable](#pbakausimpeccable), [VoltAgent/awesome-design-md](#voltagentawesome-design-md) | Datenbasierte Stil-, Farb- und Typografieauswahl sowie fertige, markenspezifische DESIGN.md-Tokens |
| Vom Brief zu Design-Artefakten arbeiten | [nexu-io/open-design](#nexu-ioopen-design), [abi/screenshot-to-code](#abiscreenshot-to-code) | Agent-native Prototypen, Decks, Bild/Video-Artefakte oder Screenshot-zu-Code-Generierung |
| Videos und Motion Graphics mit HTML erstellen | [heygen-com/hyperframes](#heygen-comhyperframes) | HTML-Kompositionen, Agent-Skills, Browser-Vorschau und lokale MP4-Renderpipeline |
| Frontend-Qualität mit Checklisten und MCP-Tools prüfen | [thedaviddias/Front-End-Checklist](#thedaviddiasfront-end-checklist) | 385 kuratierte Regeln, 390 generierte Skills und ein gehosteter MCP-Server mit Audit-/Fix-Tools |
| Eine fremde Codebasis verstehen | [Egonex-AI/Understand-Anything](#egonex-aiunderstand-anything), [shanraisshan/claude-code-best-practice](#shanraisshanclaude-code-best-practice), [Graphify-Labs/graphify](#graphify-labsgraphify) | Knowledge Graph, Architektur- und Domain-Analyse sowie praxisnahe Agenten-Wissensbasis |
| Eine Codebasis als Architekturkarte dokumentieren | [oh-my-mermaid/oh-my-mermaid](#oh-my-mermaidoh-my-mermaid) | Perspektiven für Struktur, Datenfluss und Request-Lifecycle; Mermaid-Diagramme mit Dateipfaden und rekursiven Detailansichten |
| Diagramme für Dokumentation und Präsentationen gestalten | [cathrynlavery/diagram-design](#cathrynlaverydiagram-design) | 45 Diagrammtypen, Design-Tokens, HTML mit inline SVG und nachvollziehbare Diagrammimporte |
| Anwendungen und Binärdateien anhand von Belegen untersuchen | [morluto/rea](#morlutorea) | CLI, MCP und Skill für statische Analyse, Browser- und Laufzeitbeobachtung |
| Einen Obsidian-Vault mit Agenten bearbeiten | [kepano/obsidian-skills](#kepanoobsidian-skills) | Obsidian-Markdown, Bases, JSON Canvas, CLI-Steuerung und Web-Extraktion |
| Begriffe des AI-Codings klären und gemeinsam benennen | [mattpocock/dictionary-of-ai-coding](#mattpocockdictionary-of-ai-coding) | 71 knappe Erklärungen von Harness bis Attention Budget, jeweils mit typischem Symptom und Beispieldialog |
| AI-/LLM-Engineering-Konzepte (Skills, Harness, Kontext, SDD) nachschlagen | [mleibetseder/ai-llm-wiki](#mleibetsederai-llm-wiki) | 380 quellenzitierte Konzept-Seiten, destilliert aus 234 Artikeln und 25 Fach-PDFs |
| Aktuelle Library-Dokumentation in den Agenten holen | [upstash/context7](#upstashcontext7) | Versionsbezogene Primärdokumentation und Codebeispiele per CLI oder MCP |
| NotebookLM programmatisch oder mit Agenten nutzen | [teng-lin/notebooklm-py](#teng-linnotebooklm-py) | Python-API, CLI, MCP-Server und Skill für Quellenrecherche, zitierte Antworten sowie Artefakt-Exporte |
| Automatisch aktuelle Projekt-/Wissens-Dokumentation für Agenten pflegen | [langchain-ai/openwiki](#langchain-aiopenwiki) | CI-aktualisierte Repo-Wiki oder persönliches Wissens-Wiki aus Git, Gmail, Notion, Slack u.a. |
| Dateien (PDF, Office, Bilder, Audio) für LLM-Pipelines vorbereiten | [microsoft/markitdown](#microsoftmarkitdown) | Konvertierung diverser Formate nach Markdown, als CLI, Python-API oder MCP-Server |
| Eigene Skills entwickeln | [anthropics/skills](#anthropicsskills), [mattpocock/skills](#mattpocockskills), [addyosmani/agent-skills](#addyosmaniagent-skills) | Offizielles Format, kleine komponierbare Skills und disziplinierte Skill-Anatomien |
| Fremde Skills vor der Installation prüfen | [NVIDIA/SkillSpector](#nvidiaskillspector) | Statischer Security-Scan, optionales LLM-Review, Risk Score und SARIF-Reports |
| Qualität und Nutzen eigener Skills messen | [NVIDIA/skillevaluator](#nvidiaskillevaluator) | Qualitätsprüfungen, semantische Duplikaterkennung und Vergleichsläufe mit und ohne Skill |
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
| [bmad-code-org/BMAD-METHOD](#bmad-code-orgbmad-method) | Ein vollständiges Agile-AI-Framework mit Rollen einsetzen | V7 Preview mit Phasen, Sofia-Produktplanung, Toolsmith und Review-Linsen | Framework / Sammlung | `external_repos/bmad-code-org/BMAD-METHOD/skills/` |
| [cursor/plugins](#cursorplugins) (`pstack`) | Rigorous Engineering mit aufgabenspezifischem Routing untersuchen | 23 Playbooks, 24 Prinzipien, Multi-Model-Reviews und evidenzbasierte Verifikation | Framework / Sammlung | `external_repos/cursor/plugins/pstack/skills/poteto-mode/` |
| [DietrichGebert/ponytail](#dietrichgebertponytail) | Overengineering und Code-Bloat vermeiden | Prioritätenleiter (YAGNI, Wiederverwendung, Stdlib) vor jeder Implementierung, ~20 Agent-Hosts | Skill / Sammlung | `external_repos/DietrichGebert/ponytail/skills/` |
| [garrytan/gstack](#garrytangstack) | Einen vollständigen AI-Entwicklungszyklus abbilden | Rollen-Reviews, Browser-QA, Security, Shipping und persistentes Wissen | Framework | `external_repos/garrytan/gstack/` |
| [humanlayer/skills](#humanlayerskills) | Entwicklungsphasen und wiederkehrende Codepflege strukturieren | RPI, visuelle Erklärungen und PRs, begrenzte Agent-Schleifen | Sammlung / Framework | `external_repos/humanlayer/skills/plugins/rpi/skills/rpi/` |
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
| [NVIDIA/skillevaluator](#nvidiaskillevaluator) | Qualität und tatsächlichen Nutzen von Agent-Skills evaluieren | Drei Prüfstufen, synthetische Eval-Datasets, Skill Lift und Harbor-Agentenläufe | Tool | `external_repos/NVIDIA/skillevaluator/src/skillevaluator/` |
| [NVIDIA/SkillSpector](#nvidiaskillspector) | Agent-Skills und MCPs sicherheitlich prüfen | 68 statische Muster, optionales LLM-Review, Baselines, JSON/Markdown/SARIF | Tool | `external_repos/NVIDIA/SkillSpector/` |
| [vercel-labs/skills](#vercel-labsskills) | Skills über viele Coding-Agenten installieren | Quellcode der `npx skills`-CLI und Agent-Erkennung | Tool | `external_repos/vercel-labs/skills/src/` |
| [wshobson/agents](#wshobsonagents) | Ein Multi-Harness-Plugin-Ökosystem untersuchen | Viele Agents, Skills und Commands, Generatoren sowie mehrstufige Evals | Sammlung / Marketplace | `external_repos/wshobson/agents/plugins/` |

### Design und Frontend

UI-Qualität, Design-Systeme, Animation, React/Next.js-Audits und Design-Artefakte.

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [abi/screenshot-to-code](#abiscreenshot-to-code) | Screenshots und Mockups in Frontend-Code überführen | React/FastAPI-App, Multi-Modell-Generierung, Asset-Extraktion und Video-Modus | Tool | `external_repos/abi/screenshot-to-code/` |
| [cathrynlavery/diagram-design](#cathrynlaverydiagram-design) | Diagramme für Dokumentation, Präsentationen und Blogbeiträge gestalten | 45 Diagrammtypen, inline SVG, Designsystem, Import- und Export-Helfer | Skill | `external_repos/cathrynlavery/diagram-design/skills/diagram-design/` |
| [emilkowalski/skills](#emilkowalskiskills) | Animation und Design-Details verbessern | Design-Engineering-Regeln, Animation-Reviews und präzises Motion-Vokabular | Sammlung | `external_repos/emilkowalski/skills/skills/` |
| [heygen-com/hyperframes](#heygen-comhyperframes) | HTML-Kompositionen in Videos und Motion Graphics überführen | CLI, Browser-Vorschau, MP4-Renderer, Studio und sieben veröffentlichte Agent-Skills | Tool / Framework | `external_repos/heygen-com/hyperframes/skills/hyperframes/` |
| [Jakubantalik/transitions.dev](#jakubantaliktransitionsdev) | Konkrete Interaktionen animieren, ohne Motion selbst zu entwerfen | 32 benannte CSS-Transitions als Skill, Motion-Tokens, `prefers-reduced-motion`, CLI und Refine-Panel | Tool / Skill | `external_repos/Jakubantalik/transitions.dev/skills/transitions-dev/` |
| [jakubkrehel/make-interfaces-feel-better](#jakubkrehelmake-interfaces-feel-better) | Finaler Polish-Pass für Web-UIs | Regeln zu Radien, Schatten, Hit Areas, Typografie und Animation mit Before/After-Review | Skill | `external_repos/jakubkrehel/make-interfaces-feel-better/skills/` |
| [Leonxlnx/taste-skill](#leonxlnxtaste-skill) | AI-generierte Frontends weniger generisch machen | Einzel-Skill mit recherchierten Designrichtungen, App-/Dashboard-Regeln und Browserkritik | Skill | `external_repos/Leonxlnx/taste-skill/skills/taste-skill/` |
| [millionco/react-doctor](#millioncoreact-doctor) | React-Code systematisch auditieren | Deterministische Rules, Agent-Skill, JSON-Reports und CI-Gate für neue Findings | Tool / Skill | `external_repos/millionco/react-doctor/packages/react-doctor/` |
| [nextlevelbuilder/ui-ux-pro-max-skill](#nextlevelbuilderui-ux-pro-max-skill) | Datenbasiert ein Design-System erzeugen | Stil-, Farb-, Typografie-, Chart- und UX-Datenbanken für viele Tech-Stacks | Tool / Skill | `external_repos/nextlevelbuilder/ui-ux-pro-max-skill/src/ui-ux-pro-max/` |
| [nexu-io/open-design](#nexu-ioopen-design) | Agent-native Design-Artefakte erzeugen | Desktop-Studio, Skills, `DESIGN.md`, Plugins, MCP und HTML/PDF/PPTX/MP4-Export | Tool / Framework | `external_repos/nexu-io/open-design/` |
| [pbakaus/impeccable](#pbakausimpeccable) | Bestehende Frontends systematisch polieren | 23 Design-Befehle, Produktkontext und deterministische Anti-Slop-Detektoren | Tool / Skill | `external_repos/pbakaus/impeccable/skill/` |
| [shadcn-ui/ui](#shadcn-uiui) | Projektbewusst mit shadcn/ui arbeiten | `shadcn`-Skill liest `components.json`, empfiehlt Komposition und saubere Registry-Nutzung | Tool / Skill | `external_repos/shadcn-ui/ui/` |
| [shadcn-ui/lint](#shadcn-uilint) | Tailwind-v4-Designsysteme konsistent halten | ESLint-/Oxlint-Regeln, Komponentenverträge, Theme- und Klassenprüfungen | Tool | `external_repos/shadcn-ui/lint/packages/lint/src/` |
| [thedaviddias/Front-End-Checklist](#thedaviddiasfront-end-checklist) | Frontend-Qualität systematisch checken | 385 Regeln, 390 generierte Skills, gehosteter MCP-Server mit Audit-/Fix-Tools | Tool / Sammlung | `external_repos/thedaviddias/Front-End-Checklist/skills/` |
| [vercel-labs/agent-skills](#vercel-labsagent-skills) | React, Next.js und Web-UIs optimieren | Performance-, Composition-, Accessibility-, Writing- und Animation-Regeln | Sammlung | `external_repos/vercel-labs/agent-skills/skills/` |
| [VoltAgent/awesome-design-md](#voltagentawesome-design-md) | Marken-Design-Tokens direkt ins Projekt legen | ~70 kuratierte DESIGN.md-Dateien bekannter Marken (Farben, Typografie, Spacing) | Wissensbasis | `external_repos/VoltAgent/awesome-design-md/design-md/` |

### Marketing und SEO

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [AgriciDaniel/claude-seo](#agricidanielclaude-seo) | Umfassende SEO- und GEO-Audits | Technisches SEO, Schema, Content, Local SEO, APIs und prüfbare Empfehlungen | Framework / Sammlung | `external_repos/AgriciDaniel/claude-seo/` |
| [coreyhaines31/marketingskills](#coreyhaines31marketingskills) | Marketing für SaaS und digitale Produkte | SEO, Copy, Ads, Analytics, CRO, Pricing, Launch und zentraler Produktkontext | Sammlung | `external_repos/coreyhaines31/marketingskills/skills/` |

### Text und Schreibqualität

Von KI erzeugte Texte entkitschen, ohne die eigene Stimme zu glätten.

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [petergyang/no-ai-slop](#petergyangno-ai-slop) | Entwürfe schärfen und KI-Sprachmuster loswerden | Benannte Muster statt Detektor-Rätselraten, getrennter Detect-Modus, `eval.md` als Selbstprüfung | Skill | `external_repos/petergyang/no-ai-slop/skills/no-ai-slop/` |

### Codebasis und Wissen verstehen

Onboarding in fremde Codebasen, Nachschlagewerke und aktuelle Dokumentation.

| Repo | Am besten geeignet für | Konkret nutzbar | Charakter | Lokaler Einstieg |
|---|---|---|---|---|
| [Egonex-AI/Understand-Anything](#egonex-aiunderstand-anything) | Große Code- und Wissensbasen verstehen | Tree-sitter-Analyse, Knowledge Graph, Dashboard, Touren und Diff-Analyse | Tool / Framework | `external_repos/Egonex-AI/Understand-Anything/understand-anything-plugin/` |
| [Graphify-Labs/graphify](#graphify-labsgraphify) | Code, Dokumente und Medien als Knowledge Graph abfragen | Deterministisches Tree-Sitter-Parsing (~40 Sprachen), MCP-Server, `/graphify`-Befehl | Tool | `external_repos/Graphify-Labs/graphify/graphify/` |
| [kepano/obsidian-skills](#kepanoobsidian-skills) | Obsidian-Vaults agentenfähig machen | Obsidian-Markdown, Bases, JSON Canvas, CLI-Steuerung und Web-Extraktion | Sammlung | `external_repos/kepano/obsidian-skills/skills/` |
| [langchain-ai/openwiki](#langchain-aiopenwiki) | Projektdoku oder persönliches Wissen automatisch aktuell halten | CI-gepflegtes Repo-Wiki bzw. persönliches Wiki aus Git/Gmail/Notion/Slack/X | Tool | `external_repos/langchain-ai/openwiki/src/` |
| [mattpocock/dictionary-of-ai-coding](#mattpocockdictionary-of-ai-coding) | Eine gemeinsame Sprache für die Arbeit mit Coding-Agenten aufbauen | 71 quervernetzte Begriffe in 7 Sektionen, je mit Mechanik, Symptom und Usage-Dialog | Wissensbasis | `external_repos/mattpocock/dictionary-of-ai-coding/dictionary/` |
| [mleibetseder/ai-llm-wiki](#mleibetsederai-llm-wiki) | Verdichtetes, zitiertes AI-/LLM-Engineering-Wissen nachschlagen | 380 Konzept-Seiten zu Skills, Harness, Context Engineering, SDD; 234 Rohquellen inkl. 25 Fach-PDFs | Wissensbasis | `external_knowledge/ai-llm-wiki/wiki/` |
| [oh-my-mermaid/oh-my-mermaid](#oh-my-mermaidoh-my-mermaid) | Codearchitektur in mehreren Perspektiven nachvollziehen | Rekursive Mermaid-Karten, sieben Dokumentationsfelder und Viewer; Cloud-Abgleich separat prüfpflichtig | Tool / Skill | `external_repos/oh-my-mermaid/oh-my-mermaid/skills/omm-scan/` |
| [morluto/rea](#morlutorea) | Verhalten bestehender Anwendungen beleggestützt untersuchen | Statische Analyse, native Provider, Browser- und Prozessbeobachtung, MCP | Tool / Skill | `external_repos/morluto/rea/.agents/skills/reverse-engineer-anything/` |
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
| [juliusbrussee/caveman](#juliusbrusseecaveman) | Output-Tokens durch komprimierten Antwortstil sparen | Suite für Antwortstil, Input-Kompression, Auto-Routing, Blocks, Waste fixes und Browse; Cloud-Datenflüsse prüfen | Skill / Sammlung | `external_repos/juliusbrussee/caveman/skills/` |
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

- **Repos gesamt:** 71
- **Gesamtgröße:** ca. 3.727 MB
- **Dateien gesamt:** ca. 148.187 (ohne `.git`)
- **Sterne gesamt:** ca. 5.677.515 (71/71 Repos abgerufen)
- **Stand:** 2026-10-22

| Repo | Dateien | Größe | ⭐ |
|---|---:|---:|---:|
| heygen-com/hyperframes | 9.008 | 874M | 69.257 |
| diegosouzapw/OmniRoute | 26.003 | 784M | 79.458 |
| paperclipai/paperclip | 11.343 | 167M | 105.715 |
| thedotmack/claude-mem | 2.570 | 166M | 102.164 |
| teng-lin/notebooklm-py | 2.214 | 118M | 19.841 |
| davila7/claude-code-templates | 9.777 | 118M | 32.813 |
| tt-a1i/archify | 1.174 | 98M | 87.109 |
| openai/codex | 9.437 | 92M | 130.325 |
| pbakaus/impeccable | 4.125 | 78M | 84.473 |
| shanraisshan/claude-code-best-practice | 454 | 75M | 67.886 |
| intellectronica/ruler | 264 | 71M | 2.949 |
| headroomlabs-ai/headroom | 2.662 | 70M | 77.292 |
| garrytan/gstack | 3.939 | 68M | 137.210 |
| open-gsd/gsd-core | 4.162 | 65M | 10.759 |
| morluto/rea | 5.164 | 63M | 358.296 |
| latent-spaces/brag | 369 | 62M | 17.351 |
| affaan-m/ECC | 4.627 | 59M | 285.767 |
| farion1231/cc-switch | 1.685 | 56M | 147.274 |
| shadcn-ui/ui | 6.404 | 50M | 126.156 |
| millionco/react-doctor | 7.416 | 40M | 15.034 |
| alirezarezvani/claude-skills | 5.782 | 37M | 28.502 |
| Jakubantalik/transitions.dev | 456 | 37M | 5.487 |
| router-for-me/CLIProxyAPI | 2.062 | 34M | 55.917 |
| midudev/autoskills | 4.574 | 32M | 6.968 |
| Egonex-AI/Understand-Anything | 521 | 32M | 87.510 |
| OthmanAdi/planning-with-files | 759 | 30M | 27.569 |
| Graphify-Labs/graphify | 1.105 | 28M | 131.715 |
| cathrynlavery/diagram-design | 686 | 28M | 59.572 |
| microsoft/markitdown | 196 | 26M | 191.496 |
| upstash/context7 | 536 | 25M | 63.452 |
| bradygaster/squad | 2.030 | 22M | 3.295 |
| juliusbrussee/caveman | 1.791 | 21M | 114.150 |
| nextlevelbuilder/ui-ux-pro-max-skill | 693 | 21M | 138.520 |
| langchain-ai/openwiki | 585 | 18M | 17.325 |
| github/spec-kit | 985 | 15M | 142.325 |
| anthropics/claude-code | 1.615 | 15M | 152.762 |
| NVIDIA/skillevaluator | 455 | 12M | 587 |
| thedaviddias/Front-End-Checklist | 1.978 | 12M | 74.540 |
| DietrichGebert/ponytail | 214 | 12M | 171.756 |
| anthropics/skills | 445 | 11M | 182.785 |
| rtk-ai/rtk | 814 | 9,3M | 84.211 |
| NVIDIA/SkillSpector | 461 | 9,2M | 20.827 |
| wshobson/agents | 1.170 | 8,1M | 41.485 |
| vercel-labs/agent-skills | 447 | 7,6M | 32.776 |
| 0xNyk/council-of-high-intelligence | 68 | 5,9M | 4.687 |
| coreyhaines31/marketingskills | 770 | 5,8M | 55.845 |
| AgriciDaniel/claude-seo | 494 | 5,4M | 19.603 |
| msitarzewski/agency-agents | 383 | 4,7M | 162.957 |
| bmad-code-org/BMAD-METHOD | 584 | 4,5M | 54.423 |
| cursor/plugins | 175 | 3,4M | 13.409 |
| Leonxlnx/taste-skill | 69 | 3,0M | 100.612 |
| abi/screenshot-to-code | 316 | 2,6M | 80.602 |
| VoltAgent/awesome-design-md | 173 | 2,4M | 122.766 |
| oh-my-mermaid/oh-my-mermaid | 212 | 2,0M | 3.188 |
| petergyang/human-review | 52 | 1,8M | 1.403 |
| shadcn-ui/lint | 403 | 1,7M | 3.245 |
| obra/superpowers | 231 | 1,5M | 303.183 |
| vercel-labs/skills | 143 | 1,2M | 35.995 |
| addyosmani/agent-skills | 217 | 1,0M | 109.346 |
| docker/skills | 184 | 878K | 588 |
| karpathy/autoresearch | 10 | 747K | 98.319 |
| mattpocock/skills | 191 | 730K | 299.931 |
| ayghri/i-have-adhd | 74 | 622K | 58.172 |
| humanlayer/skills | 102 | 351K | 5.401 |
| mattpocock/dictionary-of-ai-coding | 90 | 331K | 5.211 |
| emilkowalski/skills | 29 | 297K | 48.446 |
| petergyang/no-ai-slop | 14 | 257K | 12.660 |
| shadcn/improve | 10 | 61K | 9.240 |
| kepano/obsidian-skills | 15 | 57K | 49.889 |
| jakubkrehel/make-interfaces-feel-better | 12 | 48K | 3.756 |
| multica-ai/andrej-karpathy-skills | 9 | 38K | 221.977 |

Dateianzahl, Größe, Struktur und Sterne pro Repo (ohne `.git`-Verzeichnis) stehen zusätzlich in jedem Eintrag unten und werden von `70_Scripts/update_external_repos.py` automatisch aufgefrischt.
<!-- OVERVIEW:END -->

---

## Detail-Einträge

Ein Eintrag pro Repo, alphabetisch nach `owner/repo` sortiert — neue Repos entsprechend einsortieren. Mechanische Felder (Dateien, Größe, Struktur, Stars) pflegt `70_Scripts/update_external_repos.py`; die Zusammenfassung ist handgeschrieben.

---

## 0xNyk/council-of-high-intelligence

- **URL:** https://github.com/0xNyk/council-of-high-intelligence
- **Stars:** ⭐ 4.687
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 68 · **Größe:** 5,9M
- **Struktur:** Claude-Plugin mit Rollen in `agents/`, Steuerung in `skills/` und Konfigurationen in `configs/`; Installations- und Demo-Scripts separat <!-- manual -->

„Council of High Intelligence“ ist ein Multi-Agent-Plugin für strategische oder schwer umkehrbare Entscheidungen. Es inszeniert 18 klar gegensätzliche Persona-Rollen – etwa Socrates, Feynman, Torvalds, Kahneman oder Rams – und zwingt sie zu unterschiedlichen Problemrahmungen, unabhängiger Analyse, Kreuzverhören und einer abschließenden Synthese. Drei Modi begrenzen Aufwand und Tiefe: Full mit drei Runden, Quick ohne Cross-Examination und Duo mit einem gezielten Gegenpaar; zusätzlich gibt es fachbezogene Dreiergruppen für Architektur, Produkt, Risiko, Design oder AI. Das Plugin kann verfügbare Provider wie Claude, Codex, Gemini, Ollama und Cursor erkennen und Rollen über sie verteilen, um nicht nur identische Modellantworten zu vervielfachen. Dissent-Quoten, Novelty-Gates und Counterfactual-Prompts sollen Gruppendenken entgegenwirken; der Bericht soll offene Fragen und nächste Schritte vor Konsens stellen. Relevant als anschauliche Referenz für bewusst erzeugte Spannungen in Entscheidungsprozessen. Nicht geeignet für Faktenfragen, triviale oder dringende Entscheidungen – genau das dokumentiert die README selbst. Die Subagenten- und Provider-Aufrufe können erhebliche Tokenkosten, Zugriffe und Laufzeit erzeugen; deshalb nur gezielt und mit Kostenlimit verwenden. MIT-lizenziert.

---

## abi/screenshot-to-code

- **URL:** https://github.com/abi/screenshot-to-code
- **Stars:** ⭐ 80.602
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 316 · **Größe:** 2,6M
- **Struktur:** FastAPI-Backend in `backend/`, React/Vite-Frontend in `frontend/`, Hilfsprogramme und Design-Dokumente in `scripts/` und `design-docs/`; kein Skill-Paket <!-- manual -->

Screenshot to Code ist eine Web-Anwendung, die Screenshots, Mockups, Figma-Designs und Bildschirmaufzeichnungen mit generativen Modellen in Frontend-Code überführt. Unterstützt werden HTML mit Tailwind oder CSS, React, Vue, Bootstrap und Ionic; ein React/Vite-Frontend kommuniziert mit einem FastAPI-Backend. Für lokale Ausführung verlangt das Projekt mindestens einen Provider-Key für OpenAI, Anthropic oder Gemini. Gemini übernimmt zusätzlich Asset-Extraktion und Video-Modus; Replicate ergänzt Bildgenerierung, Hintergrundentfernung und Bildbearbeitung. Mehrere konfigurierte Anbieter ermöglichen Modellvarianten und Vergleiche. Im Checkout vom 22.10.2026 verwenden die Bildvorlagen-Defaults bei vollständig konfigurierten Keys Claude Opus 5.5 mit medium/xhigh, Gemini 3 Flash und GPT-6.1 Sol high; Bearbeitungen nutzen Gemini 3 Flash minimal und GPT-6.1 Sol low. Die README-Modellliste hinkt diesen Codevorgaben teilweise hinterher. Der OpenAI-Provider verkleinert übergroße eingebettete Screenshots automatisch auf das unterstützte Patch-Limit, ohne den Event-Loop mit der Bildbearbeitung zu blockieren. Optional rendert ein Chromium-basierter Preview-Mechanismus erzeugte Seiten zur visuellen Kontrolle; eine Eval-Vergleichsansicht unterstützt Modellvergleiche.

Relevant als Referenz für „visuelle Vorlage → Code → Browser-Preview → Iteration“. Erzeugter Code braucht weiterhin Designsystem-, Funktions- und Accessibility-Prüfung. Bilder und Prompts können an externe Anbieter übertragen werden und API-Kosten verursachen; Keys gehören ausschließlich in lokale Umgebungsdateien. Rechte und Datenschutz von Vorlagen sind vor Nutzung zu klären. MIT-lizenziert.

---

## addyosmani/agent-skills

- **URL:** https://github.com/addyosmani/agent-skills
- **Stars:** ⭐ 109.346
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 217 · **Größe:** 1,0M
- **Struktur:** 25× SKILL.md · Ordner: skills, agents, commands, hooks, references · Spiegelordner: .agents, .claude, .gemini (generiert)

„Production-grade engineering skills“ von Addy Osmani bündelt 25 Skills entlang Define → Plan → Build → Verify → Review → Ship: 24 Lifecycle-Skills und den Router `using-agent-skills`. Neun Slash-Commands führen unter anderem zu Spezifikation, Planung, Umsetzung, Tests, Review, Webperformance und Constraints. `/build auto` kann nach einer Planfreigabe Aufgaben testgetrieben und mit Einzel-Commits abarbeiten; Fehler und riskante Schritte bleiben Haltepunkte. Jeder Skill folgt einer festen Anatomie mit Einsatzgrenzen, Prozess, Rationalisierungen, Warnsignalen und Verifikation. Fachliche Grundlagen reichen von Hyrum’s Law, Beyonce Rule und Chesterton’s Fence bis Trunk-based Development, Shift Left, SLOs und Context-Budget-Management. Vier Personas decken Code-, Test-, Security- und Performance-Reviews ab.

Version 0.6.13 ergänzt einen quellentreuen Prosa-Review: Namen, Zahlen, Befehle, Unsicherheiten und Entscheidungskompromisse müssen eine sprachliche Überarbeitung überstehen. TDD adressiert auch inline eingefügten Code; `/review` und `/test` laufen in der Hauptsession. Die Eval-Werkzeuge verlangen nichtleere Belege, erkennen doppelte Fall-IDs und prüfen Persona-Metadaten. Host-Adapter haben unterschiedliche Fähigkeiten: Copilot erhält die Claude-Lifecycle-Commands nicht; einzelne Skill-Installationen können gemeinsame Checklisten unter `references/` auslassen. Das MIT-lizenzierte Pack ist als disziplinierte Referenz für Workflow-Qualität, überprüfbare Abschlusskriterien und Anti-Rationalisierungs-Tabellen relevant. Der Vergleich mit Superpowers und Matt Pococks Skills sowie ein verlinktes Experiment liefern weitere Einordnung, ersetzen aber keine eigene Wirksamkeitsprüfung oder Übernahmefreigabe.

---

## affaan-m/ECC

- **URL:** https://github.com/affaan-m/ECC
- **Stars:** ⭐ 285.767
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 4.627 · **Größe:** 59M
- **Struktur:** 443× SKILL.md · Ordner: skills, agents, commands, hooks, rules, plugins, references · Spiegelordner: .agents, .claude, .codex, .cursor, … (+2) (generiert)

ECC („Agent Harness Operating System“) verbindet Planung, TDD, Review, Verifikation, Memory und kontinuierliches Lernen in einem umfangreichen, MIT-lizenzierten Agenten-Ökosystem. Laut aktueller README umfasst es 71 spezialisierte Agenten, 311 Skills und 97 Legacy-Command-Shims. Claude Code ist die führende Integration; Codex und Qoder besitzen native Plugin-Pfade, weitere Harnesses unterschiedlich weit entwickelte Adapter. Gleiche Funktionsabdeckung wird ausdrücklich nicht zugesichert. Der geführte Installer 2.2.3 inventarisiert Installations-Scopes und verwaltet eigene Dateien über Install-State, Doctor, Repair und Uninstall. Mehrfachinstallation innerhalb eines Harnesses kann Skills und Hooks duplizieren.

Neuere Workflows behandeln MCP-Abhängigkeiten, Agent-Sicherheit, Change Impact, Story-Lifecycle und konventionelle Commit-Reviews. `/astra-review` übergibt Änderungen für ein unabhängiges Review an die separat installierte Codex CLI; daraus können externe Datenübertragung und Nutzungskosten entstehen. GateGuard passt Erstzugriffsfragen an Dateityp und Änderungsprofil an, berücksichtigt bereits erfolgte zielbezogene Suchen und behandelt sensible Ziele, MultiEdit und NotebookEdit strenger. Eine dokumentierte Pilot-Evaluation mit 72 Sessions misst rund 45 Prozent mehr Turns, belegt aber keine Qualitätsverbesserung, weil alle Versuchsarme bestanden. Memory Vault und Instincts liefern dauerhaften Kontext; die Plattformmatrix nennt weiterhin native Windows-Grenzen. Relevant als Referenz für skalierbare Skills, überprüfbare Installations-Lifecycles, Hook-Grenzen und ehrliche Evaluation. AgentShield und optionale Pro-/GitHub-App-Funktionen sind gesondert zu prüfen; ein Versions-Pin allein ist kein Sicherheitsnachweis.

---

## AgriciDaniel/claude-seo

- **URL:** https://github.com/AgriciDaniel/claude-seo
- **Stars:** ⭐ 19.603
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 494 · **Größe:** 5,4M
- **Struktur:** 35× SKILL.md · Ordner: skills, agents, hooks, plugins, references

Claude SEO ist ein MIT-lizenziertes SEO-Analyse-Plugin für Claude Code mit 26 Sub-Skills und 19 spezialisierten Agenten. Es kombiniert technische SEO, Content-Qualität, Schema.org, KI-Suchoptimierung, lokale SEO, E-Commerce und internationale SEO in priorisierten Maßnahmenplänen. Empfehlungen sollen Beobachtung, Abhängigkeiten, einen Widerlegungstest und einen Frühindikator enthalten. `/seo agentic` prüft Agent-Readiness einschließlich Crawler-Zugriff, Markdown-Auslieferung, `ai-catalog.json` und WebMCP. Ein verwalteter Python-/Playwright-Runtime-Pfad unterstützt auch SPAs; verzögerte Hydration und Inhalte nach Interaktion bleiben dokumentierte Grenzen.

Release v2.4.2 ergänzt das optionale Mods-Begleit-Plugin `seo-cockpit` für Claude Code ab 2.1.287 mit Budgetkontrolle kostenpflichtiger SEO-APIs, Audit-Anzeige, Economy-Modus und Dashboard. Google-APIs können die eigene gcloud-Anmeldung verwenden. Der anschließende unveröffentlichte Stand erweitert `seo-technical` um einen rein lesenden Stack-/CVE-Check für eigene oder autorisiert geprüfte Hosts. Er nutzt normale Header, Cookies und HTML-Signale; die gebündelten PHP-Advisory-Daten sind eine datierte Repo-Angabe und vor konkreten Entscheidungen gegen Primärquellen zu prüfen. Externe Signale liefern keinen vollständigen Nachweis des gesamten Serverbestands.

Der Kern funktioniert ohne zusätzliche Datenanbieter; Google-Credentials und optionale MCP-Erweiterungen liefern Feld-, Indexierungs- und Wettbewerbsdaten. Audits kontaktieren Zielwebsites und verwenden Claude; optionale Dienste können zusätzliche Kosten verursachen. Parallelisierungs- und Zeitversprechen stammen vom Projekt und wurden hier nicht gemessen. Relevant als fachlich tiefe Referenz für testbare SEO-Empfehlungen, API-Anreicherung und kontrollierte Audit-Workflows.

---

## alirezarezvani/claude-skills

- **URL:** https://github.com/alirezarezvani/claude-skills
- **Stars:** ⭐ 28.502
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 5.782 · **Größe:** 37M
- **Struktur:** 398× SKILL.md · Ordner: skills, agents, commands, hooks, rules, references · Spiegelordner: .claude, .codex, .gemini, .hermes, … (+1) (generiert)

Breite MIT-lizenzierte Skill- und Plugin-Bibliothek für Engineering, Product, Marketing, Research Operations, Finance, Compliance, C-Level-Beratung und persönliche Produktivität. Version 2.14.0 nennt 398 Skills über 20 Domänen, 766 Python-Werkzeuge, 877 Referenzen, 123 Agents, 157 Commands und 104 Marketplace-Plugins; diese Zähler schließen teilweise gebündelte und eigenständige Varianten desselben Skills ein. Manche README-Abschnitte führen noch ältere Zahlen, daher sind die Release-Zähler die präzisere Momentaufnahme. Native Anbindungen und Konvertierungswege decken laut Projekt 13 Coding-Tools ab; die Python-Werkzeuge sollen überwiegend ohne zusätzliche Pakete laufen.

Neu sind `agent-regression-evals` mit wiederholten Versuchen, Trajectory-Prüfung und statistischen Regressions-Gates, `coding-agent-rollout` für Team-Settings, MCP-/Plugin-Inventar und CLAUDE.md-Schichten sowie `month-end-close` für Abschlusskalender, Abstimmung und Abweichungsanalyse. `interview-mapper`, `red-green-proof` und ein opt-in `hivemind` erweitern Quellenprüfung und Agent-Orchestrierung. Letzteres sendet mit dem Standardmodell Code an einen gehosteten Dienst; lokale Modelle benötigen eine bewusste Konfiguration. `youtube-full` bevorzugt jetzt offene Abrufwege und behandelt einen kommerziellen Anbieter als optionalen Fallback. Die Qualitätsrunde repariert Command-Namen, Codex-Frontmatter, Mirrors und eigenständige Plugin-Installationen. Der Plugin-Name `claude-coach` wird zu `power-user-coach`, bestehende Installationen brauchen einen Wechsel. Relevant als Referenz für die Pflege großer Skill-Ökosysteme, mit eigenem Security-Auditor und Persona-Orchestrierung; die vom Autor behauptete Produktionsreife ersetzt keine eigene Übernahmeprüfung.

---

## anthropics/claude-code

- **URL:** https://github.com/anthropics/claude-code
- **Stars:** ⭐ 152.762
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 1.615 · **Größe:** 15M
- **Struktur:** Die Top-Level-Struktur (CHANGELOG, `scripts/` für Issue-Automatisierung, `examples/` für Settings/Hooks/MDM, ein Devcontainer) zeigt, dass hier nicht der CLI-Quellcode liegt, sondern rund um ein npm/Binary-Release organisierte Doku und Tooling; der Ordner `plugins/` enthält zusätzlich mehrere eigenständige Bundles mit jeweils eigenen skills/agents/commands/hooks-Unterordnern, die eine rein mechanische Skills-Repo-Erkennung fälschlich nahelegen würde. <!-- manual -->

Offizielles GitHub-Repository zu Claude Code mit Distributionsdokumentation, CHANGELOG, Beispielkonfigurationen und Erweiterungsquellen; die proprietäre Kern-Engine ist hier weiterhin nicht enthalten. Der Installationsleitfaden nennt native Installer, Homebrew und WinGet und kennzeichnet npm als veraltet. Das CHANGELOG reicht beim Update vom 22.10.2026 bis Version 2.1.307 und dokumentiert unter anderem Haiku 5.5, Workflow-Wiederaufnahme, neue Mod-APIs und `claude_code.safety_event` für von Sicherheits- oder Freigabemechanismen behandelte Tool-Aufrufe. Hook-Konfigurationen können mit `onFailure: block` beim Ausfall eines Hooks sperren; HTTP-MCP-Aufrufe werden nach Verbindungsabbrüchen nur bei lesenden oder idempotenten Tools erneut gesendet.

Praktisch relevant sind die Settings-/Hook-Beispiele, darunter ein neues HIPAA-orientiertes Konfigurationsbeispiel, sowie die TypeScript-Quellen der Built-in-Mods `sec-default`, `diff`, `telemetry` und `agents-md`. Sie zeigen Policy-Abschirmung, UI-Erweiterung, Telemetrie und das Laden von Projektanweisungen samt Tests und Engine-Typdeklarationen. Die aktuellen Änderungen härten verwaltete Policies, MCP-Toolnamen und sicherheitsrelevante Umgebungsvariablen gegenüber nutzerinstallierten Mods. Weitere Fixes behandeln UNC-Lesezugriffe, Bash-Permission-Checks, Windows-Hooks und Sandbox-Pfade über Symlinks. `plugins/` enthält optionale Referenzimplementierungen etwa für Code-Review, Feature-Entwicklung und Plugin-Bau. Das Repo eignet sich zum Studium konkreter Integrationsmuster, nicht als wiederverwendbare Engine-Bibliothek. Mod-APIs bleiben Early Access; Lizenz und Nutzung richten sich nach Anthropics Bedingungen. Die Konfigurationsbeispiele belegen keine Compliance einer eigenen Installation.

---

## anthropics/skills

- **URL:** https://github.com/anthropics/skills
- **Stars:** ⭐ 182.785
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 445 · **Größe:** 11M
- **Struktur:** 20× SKILL.md · Ordner: skills, agents, references

Offizielles Anthropic-Repository mit Beispiel-Skills für kreative Aufgaben, Web-App-Tests, MCP-Entwicklung, Unternehmenskommunikation und Dokumenterstellung. `spec/` und `template/` zeigen das Agent-Skills-Format mit `name` und `description` als Pflichtfeldern. Viele Beispiele sind Apache-2.0-lizenziert; `skills/docx`, `skills/pdf`, `skills/pptx` und `skills/xlsx` sind ausdrücklich nur source-available und laut Anthropic Referenzen der eigenen Dokumentfunktionen. Diese Lizenzgrenze muss bei Übernahmen pro Verzeichnis geprüft werden.

`skills/claude-api` bündelt mehrsprachige API-/SDK-Referenzen, Tool Runner, Modellmigration, Preserved Thinking, Evals und Managed Agents mit persistenten Konfigurationen, Workspaces und geplanten Ausführungen. Das Update vom 22.10.2026 ergänzt Haiku 5.5 und vertieft dynamische Workflows für große, wiederholte Aufgabenmengen. Neue Quickstarts behandeln Bug-Suche, Erklärvideos, Performance-Tuning und Watchlist-Auswertung. Die Dokumentation unterscheidet einzelne prüfbare Deliverables mit Outcome und Rubrik von fortlaufenden Dialogen und erläutert zusätzliche Workflow-Kosten sowie Abschaltmöglichkeiten. Korrigierte Netzwerkregeln beziehen `allowed_hosts` bei eingeschränkten Managed-Agents-Umgebungen auf die Web-Tools ein. Bestehende Eval-/Hillclimb-Guides unterstützen strukturierte Qualitäts- und Kostenvergleiche.

Die Sammlung ist ein wichtiger Ausgangspunkt für offizielle Skill-Struktur und komplexe Referenzimplementierungen; hinzu kommen `discernment-nudge` und `academy-guide`. Sie wird als Claude-Code-Marketplace angeboten und beschreibt Nutzung über Claude.ai und die API. Die Beispiele sind Demonstrationsmaterial, kein Nachweis gleicher Produktfunktion oder eigener Laufzeitkompatibilität; Modell- und Beta-API-Angaben benötigen beim Einsatz eine erneute Prüfung.

---

## ayghri/i-have-adhd

- **URL:** https://github.com/ayghri/i-have-adhd
- **Stars:** ⭐ 58.172
- **Heruntergeladen:** 2026-09-17
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 74 · **Größe:** 622K
- **Struktur:** 1× SKILL.md · Ordner: skills, agents, hooks · Spiegelordner: .agents, .cursor, .opencode (generiert)

Ein fokussierter Output-Style-Skill, der Antworten für Leser mit ADHS leichter handhabbar machen soll: konkrete Handlung zuerst, nummerierte Schritte, genau eine nächste Aktion, unterdrückte Nebenthemen, sachliche Fehlerhinweise und kurze Listen. Zehn Regeln mit Vorher-/Nachher-Beispielen stehen zentral in `skills/i-have-adhd/SKILL.md`; Ausnahmen berücksichtigen Erklärfragen, destruktive Aktionen, Debug-Spiralen und echte Mehrdeutigkeit. Der Modus bleibt bis zur ausdrücklichen Abschaltung aktiv. Die Methode orientiert sich laut Autor am Adult ADHD Tool Kit und ist als Kommunikationshilfe gedacht, nicht als medizinisches Verfahren.

Das MIT-lizenzierte Projekt enthält Adapter für mehrere Coding-Harnesses, darunter Claude Code, Cursor, Codex, Gemini CLI und OpenCode, sowie ein Eval-Set mit Szenarien und LLM-Judge. Version 0.4.1 unterstützt OpenCode V1 ab 1.18.29 und dessen V2-Plugin-API über getrennte `server()`-/`setup()`-Einstiege. Ein `.js`-Loader macht den Adapter lokal auffindbar; registriert werden der kanonische Skill, ein Slash-Command und auf Wunsch ein Always-on-Kontexthook. Ältere OpenCode-Versionen benötigen ein Upgrade oder den älteren Adapter. Die Installationshilfe unterscheidet nun Marketplace-Aktualisierung und Update des tatsächlich installierten Claude-Code-Plugins; Änderungen werden erst nach Neustart geladen. Mehrsprachige READMEs schließen jetzt Französisch ein. Relevant als kompakte Referenz für einen über mehrere Tools gepflegten Verhaltens-Skill mit eigener Evaluation; Wirkung und Regelkonformität sind vor einer Übernahme im eigenen Harness zu prüfen.

---

## bmad-code-org/BMAD-METHOD

- **URL:** https://github.com/bmad-code-org/BMAD-METHOD
- **Stars:** ⭐ 54.423
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 584 · **Größe:** 4,5M
- **Struktur:** V7-Preview mit kanonischen Skills unter `skills/`, Dokumentation in `docs/` und `docs-site/`, Prüf- und Pflegewerkzeugen unter `tools/`; kein klassischer Anwendungscode. Die stabile npm-Linie bleibt v6.12. <!-- manual -->

BMAD-METHOD ist ein rollen- und workflowbasiertes Framework für KI-gestützte Softwareentwicklung: Anforderungen klären, Planungstiefe an die Aufgabe anpassen, bauen, prüfen und aus Ergebnissen lernen. Der aktuelle Branch ist ausdrücklich V7 Preview Alpha mit möglichen Breaking Changes; v6.12 bleibt die stabile, über den npm-Installer angebotene Linie. Für die Vorschau führen Skills-CLI oder Claude-/Codex-Plugin-Marketplaces in eine flache `skills/`-Struktur mit dem zentralen `bmad`-Hub. Setup, Status, Updates und Migrationen arbeiten über Modul-Metadaten und geschichtete TOML-Konfigurationen; gerenderte Workflows nutzen Python und uv.

Die neue Product-Owner-Agentin Sofia (`bmad-agent-po`) ersetzt `bmad-spec`, `bmad-ticket` und `bmad-correct-course`. Sie pflegt Tickets in `tickets/`, verfeinert Epics und plant übergeordnete Initiativen; Migrationen falten ältere Specs ein und erhalten Customizations und Dokumentverweise. `bmad-deep-recon` untersucht Code und Git-Historie mit nachprüfbaren Quellenstellen. `bmad-build` und `bmad-build-auto` verbinden Umsetzung und Reviews; ein No-Code-Review kann Findings an einen Coding-Agenten übergeben. Review-Linsen sollen ausschließlich lesen, und die Verification-gap-Linse verlangt einen konkreten Regressionstest statt pauschaler Testforderungen.

Toolsmith ersetzt BMad Builder als Modul für Skill-/Agent-Erstellung, Überarbeitung und Evaluation. Das weitere Ökosystem umfasst unter anderem Test Architect, Game Dev Studio, Creative Intelligence und BMad Loop. Relevant als umfangreiche Alternative zu schlanken Skill-Sets, besonders für explizite Rollen, nachvollziehbare Planung und konfigurierbare Review-Schritte. MIT-lizenziert, mit gesondertem Markenschutz; die Vorschau sollte vor Übernahme auf Migrations- und Prozessaufwand geprüft werden.

---

## bradygaster/squad

- **URL:** https://github.com/bradygaster/squad
- **Stars:** ⭐ 3.295
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 2.030 · **Größe:** 22M
- **Struktur:** kein statischer Skill-Ordner mit Inhalt — die eigentliche Logik ist CLI-Quellcode in `packages/squad-cli/`, `packages/squad-sdk/`; Vorlagen in `templates/skills/`; erzeugt zur Laufzeit `.squad/agents/` + `.squad/skills/` im Zielprojekt <!-- manual -->

Squad koordiniert über GitHub Copilot ein menschengesteuertes Team benannter KI-Spezialisten. Rollen, Entscheidungsprotokolle, Wissen und Verlauf bleiben unter `.squad/` als Dateien nachvollziehbar. Ralph überwacht Issues, übergibt Kontext an Agenten und eskaliert Fehler stufenweise; ein paralleler Integrationsweg nutzt GitHub Agentic Workflows für Bootstrap, Planung, Implementierung, Review und Retrospektiven. Das Node.js-Monorepo enthält CLI und TypeScript-SDK, ergänzt durch das unabhängig versionierte .NET-Paket `Squad.Agents.AI`. CLI und SDK haben mit 1.0.0 den Alpha-Status verlassen; das CHANGELOG dokumentiert inzwischen 1.1.0, während dieser Checkout den nächsten Preview-Zyklus vorbereitet.

Eine zentrale Modellauflösung berücksichtigt Nutzerwahl, Konfiguration, Session, Rolle und Aufgabe. Die Profile `quality-first`, `balanced` und `economy` verwenden dokumentierte GA-Modelle; HydraFusion bleibt ein ausdrücklicher Opt-in. Atomisches `createIfAbsent` schützt konkurrierende State-Anlagen über sämtliche Backends. Strukturierte Nutzungsereignisse und Kontextmetriken ergänzen die bisherigen Logs. `cast`/`hire`, `build --watch` und Windows-Prompt-Transport wurden ausgebaut; Upgrades bewahren nutzereigene Copilot-Anweisungen.

Die CI-Schicht pinnt den Compiler auf `gh-aw` 0.91.5 und prüft Paketintegrität, Eigentümerschaft, Freigaben und Planrevisionen. Research wird erst auf ausdrücklichen Befehl veröffentlicht; automatisierte Verbesserungen benötigen dokumentierte Opt-ins beziehungsweise menschliche Freigaben, PR-Merges bleiben menschlich. MIT-lizenzierte Referenz für persistente Agententeams, Modellrouting und nachvollziehbare Issue-Automatisierung. GitHub-Zugang, Workflows und Schreibrechte machen jede tatsächliche Übernahme gesondert prüfpflichtig; die dokumentierten Schutzmechanismen wurden hier nicht live abgenommen.

---

## cathrynlavery/diagram-design

- **URL:** https://github.com/cathrynlavery/diagram-design
- **Stars:** ⭐ 59.572
- **Heruntergeladen:** 2026-10-11
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 686 · **Größe:** 28M
- **Struktur:** Einzelner Skill unter `skills/diagram-design/` mit `SKILL.md`, Referenzen, Python-Helfern und Galerie `assets/index.html`; ergänzende Commands, Prompts und Dokumentation unter `commands/`, `prompts/` und `docs/` <!-- manual -->

Diagram Design ist ein Agent-Skill für gestaltete Diagramme als eigenständige HTML-Datei mit inline SVG. Die README nennt inzwischen 45 Diagrammtypen für Entwickler, Autoren und Produktteams: Architektur, Datenflüsse, Sequenzen, Zustandsmodelle, Charts und neu Service Blueprints für Frontstage-/Backstage-Abläufe. Architekturdiagramme können administrative Bereiche und Netzwerkgrenzen verschachtelt darstellen. Ein reduziertes Designsystem verbindet wenige Akzente, ein 4-Pixel-Raster und klare Typografie mit gezielt nachgeladenen Typreferenzen; semantische Muster, Markenprofile und zugängliche Animationen ergänzen es bei Bedarf.

Einstiege sind `skills/diagram-design/SKILL.md`, die Galerie `assets/index.html` und `docs/cookbook.md`. Vorhandene draw.io-, Mermaid- und Excalidraw-Dateien werden neu gezeichnet; ein Fidelity Ledger dokumentiert Vereinfachungen. Die aktuellen Parserkorrekturen betreffen etwa Mermaid-Fragmente, unsichtbare Links und versteckte draw.io-Zellen. Python-Helfer übernehmen Extraktion, SVG-Export und Ausgabeprüfungen. Ein paketierter PNG-Renderer benötigt Playwright/Chromium; SVG-Export bewahrt zusätzliche CSS-, Referenz- und Transparenzdetails. Neben bestehenden Agent-Hosts gibt es ein natives Qoder-Plugin.

Das Repo ist MIT-lizenziert; `THIRD_PARTY_LICENSES.md` hält weitere Icon-/Font-Lizenzen und Markenhinweise fest. Standardvorlagen laden Google Fonts, Systemfonts ermöglichen netzfreie Ausgaben. Marken-Onboarding kann Websites abrufen; Eingaben verarbeitet der gewählte Agent-Anbieter. Updates können direkte Änderungen am installierten Skill überschreiben. Layoutqualität bleibt modellabhängig. Lokale Referenz für Diagrammgestaltung, progressive Kontextladung und nachvollziehbare Importe; keine automatische Integration oder eigene Laufzeitabnahme.

---

## coreyhaines31/marketingskills

- **URL:** https://github.com/coreyhaines31/marketingskills
- **Stars:** ⭐ 55.845
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 770 · **Größe:** 5,8M
- **Struktur:** 52× SKILL.md · Ordner: skills, references · Spiegelordner: .agents (generiert)

Sammlung von 52 Marketing-Skills für Coding-Agenten von Corey Haines; die Plugin-Manifeste stehen beim aktuellen Checkout auf 2.13.0. Sie deckt SEO, Conversion-Optimierung, Copywriting, bezahlte Kanäle, Analytics, Retention, Wachstum und Sales ab. Neu ergänzen `link-building` für verdiente Backlinks und AI-Zitationen sowie `conversion-tracking` für Formulare, Buchungen, Pixels, GTM und serverseitige Zustellung den Bestand. Der Tracking-Skill unterscheidet Erfolgssignale und Zustellwege; Hilfsprogramme und Rezepte wurden unter anderem bei Consent-Anforderungen, Payload-Formaten und Request-Zeitlimits korrigiert.

Alle Skills beziehen zuerst ein gemeinsames `product-marketing`-Kontextdokument ein. Dieses enthält inzwischen eine aus Belegen entwickelte Brand Voice, optionale Paid-Ads-Daten und ein Learnings Ledger, das Copywriting, E-Mails und Anzeigen vor neuen Entwürfen lesen. Wiederkehrende Marketing-Loops dokumentieren Entscheidungen und schlagen neue Erkenntnisse vor. Ads-Reviews sollen in eine konkrete Betriebsentscheidung münden; `ai-seo` ergänzt Claim Ledger, mehrschichtige Attribution, Prompt-Portfolios, Agent-Defaults und getrennte Crawler-Zwecke. Ein geführtes Tool-Onboarding beginnt mit begrenzten Zugangsdaten und einem read-only Ergebnis.

Die MIT-lizenzierte Bibliothek bietet CLI-/Plugin-Installationen sowie separate Claude-Web-ZIPs; diese richten keine MCPs oder Zugangsdaten ein. Offen ausgewiesene Partnerintegrationen und Verweise auf das Eigenprodukt Magister sind bei Empfehlungen mitzulesen. Referenz für zentrale Produktkontexte, nachvollziehbare Marketing-Evidenz und wiederverwendbare Workflows; externe Dienste, Kosten und Schreibrechte bleiben pro Komponente zu prüfen.

---

## cursor/plugins

- **URL:** https://github.com/cursor/plugins
- **Stars:** ⭐ 13.409
- **Heruntergeladen:** 2026-10-22
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 175 · **Größe:** 3,4M
- **Struktur:** Partieller Checkout: `pstack/` mit Skills, Agents, Playbooks, Guide und Automation-Pack; Root-Dateien des Monorepos bleiben vorhanden. Andere Plugin-Unterordner und `harness/pstack/` sind nicht ausgecheckt. <!-- manual -->

Gezielt als Referenz erfasster Unterordner [pstack](https://github.com/cursor/plugins/tree/main/pstack), Lauren Tans Engineering-Workflows im offiziellen Cursor-Plugin-Monorepo. Der lokale Sparse Checkout unter `external_repos/cursor/plugins/` enthält `pstack/` und die Root-Dateien, nicht den gesamten Plugin-Katalog. Stand der Sichtung: Version `0.15.29`, Checkout-Commit `f2bad5225cb2d4f5e58b45aa36be89d16a558c13`; die letzte Änderung am Teilbaum stammt vom 20.10.2026. Einstieg ist `pstack/README.md`, danach `pstack/skills/poteto-mode/SKILL.md` und `pstack/docs/guide/`. Der Router ordnet Aufgaben 23 Playbooks zu, darunter Investigation, Bugfix, Performance, Refactoring, Prototyping, Verifikation und Shipping. 24 kurze Prinzipien behandeln Datenmodelle, Typen, Idempotenz, Ursachenanalyse, Prüfbarkeit und Kontextdisziplin. Weitere Skills liefern konkurrierende Lösungsversuche, getrennte Reviews sowie projektspezifische Verifikations-Skills. Das ist besonders nützlich, um unsere Skill-Hierarchie und Builder-/Reviewer-Trennung mit einem anderen Ansatz zu vergleichen; Qualitäts- und Parallelisierungsversprechen sind dabei Autorenaussagen, keine eigenen Messungen.

`pstack/LICENSE` und die Plugin-Manifeste nennen MIT; daraus folgt keine Lizenzannahme für sämtliche anderen Monorepo-Inhalte. Claude Code nutzt laut Dokumentation einen generierten Adapter unter `harness/pstack/`, der hier bewusst nicht enthalten ist. Manche Abläufe benötigen zusätzlich `cursor-team-kit`, Cursor-spezifische Funktionen oder das dormant mitgelieferte Benny-Automation-Pack. Shell- und TypeScript-Helfer können GitHub, Worktrees und PR-Abläufe berühren; die TypeScript-Werkzeuge setzen Bun und weitere Pakete voraus. Nur statisch gelesen, keine Installation, Script-Ausführung oder produktive Aktivierung. Übernahmeprüfung: [pstack-Review](../30_Skills/external/reviews/cursor-pstack.md).

---

## davila7/claude-code-templates

- **URL:** https://github.com/davila7/claude-code-templates
- **Stars:** ⭐ 32.813
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 9.777 · **Größe:** 118M
- **Struktur:** Großer Komponenten-Katalog in `.claude/` und `.claude-plugin/`; Installer, APIs und Dashboard-Code in `cli-tool/`, `api/`, `dashboard/` und `cloudflare-workers/`; zahlreiche generierte Spiegel und Drittquellen <!-- manual -->

Claude Code Templates ist ein großer Katalog vorkonfigurierter Agents, Commands, MCP-Integrationen, Settings, Hooks und Skills. Website und npm-CLI erschließen Komponenten für Entwicklung, Security, Datenbanken, Marketing und externe Dienste. Ergänzend liefert das Projekt Session-Analytics, Conversation-Monitoring, Health Checks und Plugin-Verwaltung. CLI 1.30.0 zeigt Mehrkomponenten-Installationen mit Plan, Zielpfaden, Fortschritt und gezieltem Retry an. Dashboard-Erweiterungen umfassen eine OpenAPI-Beschreibung, `llms.txt`, echte 404-Antworten und Hinweise auf NVIDIA-SkillSpector-Scans samt Bericht; ein solcher Hinweis ist kein eigener Vertrauens- oder Sicherheitsnachweis.

Die hauseigenen Mods übernehmen zunehmend Konfiguration und Beobachtung: `stack-viewer` zeigt Komponenten nach Geltungsbereich, `turn-inspector` den Kontextverlauf, `ultra-config` Profile und modellabhängigen Aufwand, `subagent-tuner` die Subagent-Einstellungen. Hinzu kommen Skill-Typeahead, Read-only-Subagent-Settings mit PreToolUse-Guard und eine Stripe-Einstellung zur Bestätigung vor Schreibzugriffen. CLI 1.29.7 schließt laut CHANGELOG eine Command Injection in der Analytics Console Bridge und weitere Shell-Sinks; WebSocket und API-Proxy erhalten lokale Zugriffsgrenzen, Settings dürfen nur unter `.claude/` schreiben.

Die Sammlung übernimmt zahlreiche Drittquellen, darunter Anthropic Skills, Superpowers und wshobson/agents. Deren Lizenzen und Attributionen bleiben neben der MIT-Lizenz des Repositorys erhalten. Relevant als Landkarte für Marketplace-UX, Komponententypen und Installationsfeedback. Hooks, Mods, MCPs, Remotezugänge und integrierte Schreibrechte verlangen eine Prüfung jeder tatsächlich übernommenen Komponente; keine pauschale Vertrauensannahme, Installation oder eigene Sicherheitsabnahme des Gesamtpakets.

---

## diegosouzapw/OmniRoute

- **URL:** https://github.com/diegosouzapw/OmniRoute
- **Stars:** ⭐ 79.458
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 26.003 · **Größe:** 784M
- **Struktur:** Reiner Next.js-16-Anwendungscode in `src/` (app/, domain/, lib/, server/, sse/), plus Workspace `open-sse/` (Streaming-Engine), `electron/` (Desktop-App) und `bin/` (CLI); der vorhandene Ordner `skills/` enthält keine wiederverwendbaren Agenten-Skills, sondern 42 auto-generierte SKILL.md-Referenzdateien (API/CLI-Doku für den eigenen MCP-/A2A-/REST-Zugriff auf OmniRoute selbst). <!-- manual -->

OmniRoute ist ein selbstgehosteter AI-Gateway und Proxy auf Basis von Next.js 16 und TypeScript, verteilt als npm-Paket, Docker-Image, Electron-App und CLI. Ein OpenAI-kompatibler Endpunkt bündelt laut Checkout v3.8.52 inzwischen 375 Provider; Formatübersetzung verbindet OpenAI-, Claude- und Gemini-APIs. Combos, Auto-Fallback, Circuit Breaker, Cooldowns und 20 Routingstrategien einschließlich Quota-Share sollen verfügbare Provider-Kontingente koordinieren. RTK-, Caveman- und weitere Kompressionsverfahren ergänzen Kosten- und Kontextkontrolle. Angegebene Einsparungen und summierte Gratis-Kontingente sind Projektangaben: Sie setzen eigene, jeweils berechtigte Provider-Accounts voraus und sind keine garantierte Tokenzuteilung.

Der aktuelle Stand bietet `serve --headless` beziehungsweise `OMNIROUTE_HEADLESS=1` für den Proxybetrieb ohne Dashboard und dessen Zusatzsysteme sowie eine erweiterte Modell-Discovery. Hinzu kommen MCP mit dokumentierten 110 Tools, A2A, Memory, Policy-/Kostenverwaltung und Anbindungen an zahlreiche Coding-Tools. Der vorliegende Update-Schritt umfasst nur sieben Git-Commits, enthält aber einen sehr großen kumulierten Release-Snapshot; die Commitzahl beschreibt dessen Umfang daher schlecht. Als Referenz ist das MIT-lizenzierte Projekt für Multi-Provider-Routing, Streaming, API-Übersetzung und Gateway-Bedienung interessant. Die enthaltenen Skills dokumentieren vor allem OmniRoutes eigene Schnittstellen und sind kein allgemeines Skill-Pack. Risiken ergeben sich aus großem Code- und Providerumfang, gespeicherten Zugangsdaten, OAuth-/Gateway-Vertrauensgrenzen sowie hoher Wartungslast. Veröffentlichte Testzahlen und Werbeversprechen ersetzen keine eigene Laufzeit- oder Sicherheitsabnahme.

---

## DietrichGebert/ponytail

- **URL:** https://github.com/DietrichGebert/ponytail
- **Stars:** ⭐ 171.756
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 214 · **Größe:** 12M
- **Struktur:** Skill-/Plugin-Paket mit `skills/` (6 SKILL.md-Definitionen), `commands/` (Slash-Commands als .toml), `hooks/` (Lifecycle-Hooks u.a. für Claude Code/Codex) sowie zusätzlichen Adapterordnern (`.cursor/`, `.windsurf/`, `.clinerules/`, `.kiro/`, `.opencode/`, `.qoder/` etc.) für rund 20 Agent-Hosts; kein klassischer Anwendungscode, sondern ein Multi-Host-Plugin-System. <!-- manual -->

Ponytail ist ein MIT-lizenziertes Regel- und Skill-Paket für schlanke Implementierungen in rund 20 Agent-Umgebungen. Vor eigenem Code steht eine Prioritätenleiter: Bedarf prüfen, Vorhandenes wiederverwenden, Standardbibliothek und Plattformfunktionen nutzen, installierte Abhängigkeiten prüfen, dann die kleinste passende Lösung schreiben. Version 5 baut Prompt, Review und Audit neu auf: Erst den tatsächlichen Datenfluss verstehen, dann reduzieren; Validierung, Fehlerbehandlung, Sicherheit und Barrierefreiheit bleiben erhalten. `/ponytail-review` betrachtet auch betroffene Aufrufer außerhalb des Diffs und priorisiert Bugs, Lastverhalten, fehlende Tests und Performance; `/ponytail-audit` überträgt diese Prüfung auf das ganze Repo. Sechs Skills und hostabhängige Lifecycle-Hooks verteilen die Regeln, mit lite/full/ultra/off und persistentem Modus über Kontextkompaktierung hinweg. Der frühere eigene MCP-Server wurde entfernt.

Seit Version 5.3 zeigt Claude Code eine optionale Band mit Kosten, Tokens, Agent-Zeit, Wiederverwendung und Teststatus sowie ein lokales Board über Sessions und Projekte; historische Sessions lassen sich importieren. Voraussetzung ist Claude Code ab 2.1.290 in Terminal oder Desktop, nicht dessen VS-Code-Chat, Cloud oder Headless-Modus. Der Checkout steht bei 5.3.2, mit weiteren Fixes für Windows-Startzeiten, Hook-Ausgabe, große Repository-Maps und benutzerdefinierte Cursor-Konfigurationen. Relevant als Vorbild für portable Regelverteilung und risikoorientierte Vereinfachung. Benchmark-Ergebnisse stammen vom Autor und sind keine eigene Wirksamkeitsmessung; Unterstützung und Commands unterscheiden sich je Host, Hooks benötigen Node.js.

---

## docker/skills

- **URL:** https://github.com/docker/skills
- **Stars:** ⭐ 588
- **Heruntergeladen:** 2026-09-27
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 184 · **Größe:** 878K
- **Struktur:** 12× SKILL.md · Ordner: skills, agents, references · Spiegelordner: .agents (generiert)

Docker-eigenes Repository mit Agent Skills für KI-Coding-Agenten rund um Docker-Produkte: Dockerfile/Build (`docker-project-foundations`, `docker-build-strategies`), Compose (`docker-compose-patterns`), Docker Sandboxes/`sbx`-CLI (Lifecycle, Netzwerk/Credentials, deklarative `sbxenv.yaml`-Umgebungen, Kits — letztere beide als experimentell markiert) und Docker Agent/`cagent` (Config, lokaler Run, Deploy/Distribution), plus Cross-Product-Skills für destruktive-Operationen-Guardrails und Dokumentationsrecherche. Der neue experimentelle `docker-docs` sucht in offizieller Docker-Dokumentation, bevorzugt per Docker-Docs-MCP, mit Fallback auf `llms.txt` und Seiten-Markdown. Plugin-/Extension-Installationen registrieren dafür den Remote-MCP-Server `https://ai-backend-service.docker.com/mcp`; Skills-CLI, Docker Sandboxes und manuelle Kopien liefern dagegen nur die Skill-Dateien. Alle Skills folgen der offenen Agent-Skills-Spezifikation (agentskills.io) und bestehen den upstream `skills-ref`-Validator; `catalog.yaml` ist die Single Source of Truth, aus der README-Tabelle, `skills.sh.json` und Plugin-Manifeste per `task catalog` generiert werden. Installierbar über die `skills`-CLI (skills.sh, herstellerübergreifend für Claude Code, Codex, Cursor, Copilot CLI, Gemini CLI, OpenCode, Windsurf, Cline, Kiro u.a.), native Plugin-Marketplaces (Claude Code, Codex, Copilot CLI), die Gemini-CLI-Extension, `sbx skills add` oder klassisches Git-Clone mit Discovery-Symlinks (`.claude/skills`, `.agents/skills` usw.), sofern das geklonte Repo selbst Projekt-Root ist. Relevant als Referenz für sauberes Skill-Katalog-Management (Versionierung pro Skill, generierte statt handgepflegte Tabellen, CI-Validierung via Taskfile) und für Docker-Sandboxes/-Agent-spezifisches Vorgehen, weniger als inhaltlich übertragbares Wissen für andere Domänen. Apache-2.0-lizenziert, aktiver Maintainer (Docker Inc.), OpenSSF-Scorecard-Badge vorhanden.

---

## Egonex-AI/Understand-Anything

- **URL:** https://github.com/Egonex-AI/Understand-Anything
- **Stars:** ⭐ 87.510
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 521 · **Größe:** 32M
- **Struktur:** `understand-anything-plugin/skills/`, `understand-anything-plugin/agents/` (project-scanner, file-analyzer usw.), Analyse-Engine in `understand-anything-plugin/packages/core`, Dashboard in `understand-anything-plugin/packages/dashboard`, Standalone-Viewer in `understand-anything-plugin/packages/viewer` (committeten Graph ohne Claude Code via `npx` ansehen) <!-- manual -->

Ein Claude-Code-Plugin (ursprünglich von Lum1104, jetzt bei Egonex weitergeführt), das eine beliebige Codebasis mit einer Multi-Agent-Pipeline analysiert und daraus einen interaktiven Knowledge Graph baut – jede Datei, Funktion, Klasse und Abhängigkeit wird zum klickbaren, durchsuchbaren Knoten in einem visuellen Dashboard. Kombiniert deterministische Tree-sitter-Analyse (Imports, Exports, Funktions-/Klassendefinitionen, Aufrufstellen – reproduzierbar) mit LLM-Auswertung (Klartext-Zusammenfassungen, Architektur-Layer, Business-Domain-Mapping, geführte Touren). Sechs bis sieben spezialisierte Agenten (project-scanner, file-analyzer, architecture-analyzer, tour-builder, graph-reviewer, domain-analyzer, article-analyzer) arbeiten parallel; Folge-Läufe sind inkrementell (nur geänderte Dateien). Zentrale Befehle: `/understand` (Analyse), `/understand-dashboard` (Visualisierung), `/understand-chat` (Fragen zur Codebasis stellen), `/understand-diff` (Impact-Analyse von Änderungen), `/understand-onboard` (Onboarding-Guide generieren), `/understand-knowledge` (auch für Wissens-/Dokumentations-Basen nach Karpathy-Wiki-Muster nutzbar). Der Graph ist reines JSON und kann committet werden, damit Teammitglieder die Analyse nicht wiederholen müssen. Funktioniert über viele Agenten hinweg (Claude Code, Codex, Cursor, Copilot, Gemini CLI u.v.m.). Sehr relevant als direktes Vorbild für den eigenen `graphify`-Skill – ähnliches Ziel (Code/Wissen → Graph), aber mit ausgereifter Multi-Agent-Pipeline und Dashboard.

---

## emilkowalski/skills

- **URL:** https://github.com/emilkowalski/skills
- **Stars:** ⭐ 48.446
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 29 · **Größe:** 297K
- **Struktur:** 15× SKILL.md · Ordner: skills

"Skills For Design Engineers" von Emil Kowalski (Design-Engineering-Erfahrung u.a. bei Vercel und Linear, Betreiber von animations.dev). Mittlerweile 15 fokussierte Skills adressieren gezielt die "fehlende Design-Taste" von KI-Agenten: `emil-design-eng` (Hauptskill, primär Animation plus allgemeine Design-Ratschläge), `review-animations`, `improve-animations`, `find-animation-opportunities`, `animation-vocabulary`, `animation-performance` (Ursachen für Frame-Drops und Rendering-Kosten), `break-ui` (UI-Stresstest mit extremen Eingabedaten), `apple-design`, `pick-ui-library`, `prototype` sowie `animate` (Animationen von Null aufbauen statt nur bewerten), `animate-expo` und `write-swift` (React Native/Expo bzw. natives Swift), `ask-sonner` (Fragen zur Toast-Bibliothek Sonner des Autors) und neu `mobile-native` (CSS-/Meta-Tag-Fixes, die eine Web-App auf dem Handy nativ statt "wie im Browser" wirken lassen – Sticky-Hover, Tap-Highlights, 100vh-Bug, Safe-Areas u.a.). Der Prototyping-Skill erzeugt mehrere unterschiedliche Varianten eines beschriebenen UI-Bausteins und macht sie über einen Switcher direkt vergleichbar – nützlich, um vor dem Polish bewusst zwischen Richtungen zu entscheiden. Mit `animate`, `animate-expo`, `write-swift` und `mobile-native` verlässt die Sammlung das reine Desktop-Web-Frontend und deckt auch Mobile-/Apple-Plattformen ab. Kernthese: Agenten treffen oft die falschen Detailentscheidungen (z.B. `ease-in` statt `ease-out` bei Enter-Animationen, solide statt halbtransparente Schatten) – kleine Fehler, die sich zu insgesamt mittelmäßigen statt herausragenden Interfaces summieren. Die Skills sind laut Autor ein Nebenprodukt echter Domänen-Expertise, nicht deren Ersatz. Installation über `npx skills@latest add emilkowalski/skills`. Sehr relevant als kompakte, hochkarätige Ergänzung zu den vorhandenen Design-/Taste-Skills (`taste-skill`, `ui-ux-pro-max-skill`) – hier mit Fokus auf Animation, Variantenbildung und einen erfahrenen, spezifischen Blickwinkel statt breiter Systematik.

---

## farion1231/cc-switch

- **URL:** https://github.com/farion1231/cc-switch
- **Stars:** ⭐ 147.274
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 1.685 · **Größe:** 56M
- **Struktur:** Reiner Anwendungscode einer Tauri-Desktop-App: React/TypeScript-Frontend in `src/` (u.a. `components/providers`, `components/mcp`, `components/skills`, `components/proxy`) und Rust-Backend in `src-tauri/src/` (`commands/`, `services/`, `database/`, `proxy/`, `mcp/`); trotz Verzeichnisnamen wie `skills/` oder `mcp/` handelt es sich nicht um ein Claude-Code-Skill/Plugin-Paket, sondern um UI-Module zur Verwaltung von Skills/MCP-Konfigurationen anderer Tools. <!-- manual -->

CC Switch ist eine plattformübergreifende Desktop-Anwendung mit Tauri 2, Rust und React/TypeScript für Provider-, Konto- und Konfigurationsverwaltung von KI-Coding-Tools. Version 4.0.18 verwaltet elf Anwendungen: Claude Code, Claude Desktop, Codex, Gemini CLI, OpenCode, OpenClaw, Hermes, Grok Build, MiniMax Code, Pi und Antigravity CLI. Provider-Presets, Direct-/Routing-/Aggregation-Modi, lokaler Proxy mit Failover, MCP-/Skill-/Prompt-Sync, Session-Browser und Nutzungsdashboard ersetzen viele manuelle Konfigurationsschritte. Claude Desktop nutzt inzwischen ebenfalls Direct, Routing und Aggregation; Codex erhält konfigurierbare Reviewer- und Subagent-Modelle. Währungen, Logspalten und Diagrammansichten lassen sich lokal anpassen.

Antigravity-Provider gelten nur für Terminals, die von der jeweiligen Karte gestartet wurden. Mehrere offizielle Antigravity-Konten, Quoten und Kontobindungen unterstützt das Auth Center zunächst nur unter macOS. Die Datenbank steigt auf Schema 21; vor der Migration wird ein Backup erzeugt, ältere Versionen verweigern die neue Datenbank. Aktuelle Fixes betreffen Windows-MSI-Neustarts, atomare Einstellungsspeicherung samt beschädigter Originaldatei als Backup, Terminalstarts, konkurrierende MCP-Toggles und Codex-Compaction-/Tool-History-Kompatibilität.

Das MIT-lizenzierte Projekt ist eine Anwendung und keine direkt einbindbare Skill-Bibliothek. Interessant sind Provider-Switching-UX, sichere Konfigurationsprojektionen, Kontenverwaltung und Recovery-Lifecycles. API-Keys, OAuth-Tokens und weitere Credentials liegen lokal; optionaler Cloud-Sync über Drittanbieter erweitert die Vertrauensgrenze. Zahlreiche gesponserte Relay-Presets sind keine unabhängige Vertrauensbewertung. Aktive Releases und vorhandene Tests belegen Pflege, ersetzen aber keine eigene Laufzeit- und Datenabnahme.

---

## garrytan/gstack

- **URL:** https://github.com/garrytan/gstack
- **Stars:** ⭐ 137.210
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 3.939 · **Größe:** 68M
- **Struktur:** 65× SKILL.md · Ordner: skills, agents, hooks, references

gstack ist Garry Tans MIT-lizenziertes System für rollenbasierte KI-Entwicklung von Produktklärung über Planung, Umsetzung, Review und Browser-QA bis Shipping und Retro. Skills wie `/office-hours`, die CEO-/Engineering-/Design-/DevEx-Planreviews, `/review`, `/qa`, `/cso`, `/test-audit` und `/ship` verbinden konkrete Artefakte mit Qualitätsprüfungen. GBrain ergänzt dauerhaftes Projektwissen. Im aktuellen Stand 1.91.176.0 kommen Merge-Trains mit Train-Verifikation und Pattern-Bisect sowie Capy-Funktionen für Freigaben pro Thread, Planbriefings und Vorher-/Nachher-PR-Bilder hinzu. Eine Modellpolicy trennt Frontier-Planreview von Smart-Implementierung; native Einstellungen und Overrides bleiben möglich.

Setup erzeugt nur die Skill-Kopien der tatsächlich aus diesem Checkout installierten Hosts und sichert entfernte generierte Kopien. Antigravity CLI ist ein weiterer experimenteller Host; Fähigkeiten und Durchsetzung unterscheiden sich je Integration. Bun-Startpunkte ignorieren die `.env` und `bunfig.toml` des untersuchten Repos. Fehlgeschlagene Gate-Evals werden einmal wiederholt; ein danach grüner Fall bleibt als flaky erkennbar.

Relevant als umfassende Referenz für Rollen-Workflows, Nachweisführung und Browser-QA. Die Netzwerkgrenzen verdienen Beachtung: Nutzungstelemetrie ist opt-in, Update-Checks und automatische Reviews bei einem zweiten Modell sind laut Dokumentation standardmäßig aktiv. Solche Reviews übertragen relevante Prompts, Pläne oder Code mit dem eigenen Provider-Login. Egress-Receipts dokumentieren Übertragungsversuche, ersetzen aber keine Netzwerk-Firewall. Installation und produktive Verwendung erfordern weiterhin eine gesonderte Übernahmeprüfung; die zahlreichen Workflows können für kleine Aufgaben erheblichen Aufwand erzeugen.

---

## github/spec-kit

- **URL:** https://github.com/github/spec-kit
- **Stars:** ⭐ 142.325
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 985 · **Größe:** 15M
- **Struktur:** Kern ist eine Python-CLI (`src/specify_cli` mit `integrations/`, `bundler/`, `presets/`, `workflows/`) zur Codegenerierung; `templates/commands`, `extensions/*/commands` und `presets/*/commands` enthalten Slash-Command-/Skill-Vorlagen, die beim `specify init` in Zielprojekte (z.B. `.claude/commands/`) geschrieben werden – kein eigenständiges Skill-Paket, sondern ein Generator/Installer für Skill- und Command-Artefakte anderer Agenten. <!-- manual -->

Spec-Kit ist GitHubs MIT-lizenziertes Toolkit für strukturierte Agentenprozesse, wiederverwendbare Templates und dokumentierte Ergebnisse. Spec-Driven Development bleibt der Kern: Constitution, Spezifikation, Plan, Tasks, Implementierung und Converge führen ein Feature durch überprüfbare Artefakte. Bugfix- und Ideenbewertungsprozesse sind unabhängige Erweiterungen, keine verpflichtenden Vorstufen. Die Python-CLI `specify` unterstützt zahlreiche Coding-Agenten und kann über Extensions, Presets, Workflows, eigene Steps und Bundles an Teams angepasst werden. Aktuelles Release ist 1.2.2; der Checkout entwickelt bereits 1.2.3.dev0.

Workflows können verschachtelt zu einem gemeinsamen Ausführungsbaum zusammengesetzt werden. Command-/Prompt-Schritte bieten optionales Output-Capture, ein eingebauter GitHub-Step verbindet externe Arbeit. MCP stellt Version und Artefakte bereit; kataloginstallierte externe Agent-Adapter erweitern die Integrationsgrenze. Bundles und weitere Komponenten unterstützen exakte Katalog-Releases und Konfliktabgleich. `.presetignore` begrenzt Preset-Inhalte, `integration none` erzeugt nur gemeinsames Scaffolding. Korrekturen schützen fremde Hooks, behandeln abgebrochene Gates nicht als Zustimmung und erhalten literale PowerShell-Pfade.

Das Projekt ist ein Generator und Installer für Agent-Artefakte, kein unabhängig kopierbares Skill-Pack. Relevant sind die klare Phasenstruktur, komponierbare Prozesse, versionierte Distribution und dokumentierte Zuständigkeit von Hooks gegenüber Runtime-Events. Risiken bleiben Tooling-Komplexität, Python-/uv-Voraussetzungen und Prozessaufwand bei kleinen Aufgaben. Community-Katalogeinträge sind weder Audit noch Empfehlung; heruntergeladene Erweiterungen können Code ausführen und müssen separat geprüft werden.

---

## Graphify-Labs/graphify

- **URL:** https://github.com/Graphify-Labs/graphify
- **Stars:** ⭐ 131.715
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 1.105 · **Größe:** 28M
- **Struktur:** Python-Paket (`pyproject.toml`, CLI-Entry-Point `graphify`) mit Quellcode in `graphify/`; enthält zwar einen Unterordner `graphify/skills/`, dieser ist aber ein Vorlagenverzeichnis für die vom Tool selbst generierten Skill-Dateien verschiedener KI-Assistenten (Claude, Codex, Cursor u.a.), kein direkt kopierbarer Skill-Ordner für Dritte. <!-- manual -->

Graphify ist ein Python-CLI-Tool und PyPI-Paket (`graphifyy`), das Code, Dokumente, PDFs, Bilder und Videos in einen durchsuchbaren Knowledge Graph überführt. Code wird lokal mit Tree-Sitter ohne LLM geparst; semantische Verarbeitung anderer Inhalte verwendet optional das Modell des Assistenten oder konfigurierte Backends. Beziehungen sind als EXTRACTED oder INFERRED gekennzeichnet. `graph.html`, `GRAPH_REPORT.md` und `graph.json` bilden die Ausgabe; CLI-Abfragen wie `query`, `path`, `explain` und ein optionaler MCP-Server erschließen sie. Die mitgelieferten Skill-Dateien sind generierte Host-Integrationen dieses Tools, keine unabhängige Skill-Sammlung.

Version 0.9.93 verbessert Symbolauflösung über viele Sprachen und Repositories, inkrementelle Updates und parallele Graphkanten. Mehrdeutige exakte Namen verlangen eine eindeutige Auswahl; normale Stichwortsuchen bleiben möglich. Nur teilweise gelesene Dateien werden als unvollständig markiert und beim nächsten Update erneut verarbeitet. Credential-Muster in Rationale-Labels werden redigiert, unlesbare PDFs als Fehler erkennbar, und vaultrelative Obsidian-Wikilinks erreichen die tatsächliche Notiz. Windows-MCP-stdio und Ollama-Kontextübergabe wurden korrigiert. Cache-Schemaänderungen können eine vollständige AST-Neuextraktion auslösen.

Relevant als Ergänzung zu Datei-/Textsuche für Code- und Wissensexploration. Das lokale Tool ist Apache-2.0-lizenziert, nicht MIT. Der separat beworbene Dienst Graphify Cloud und dessen Einsparungs-/Verifikationsversprechen sind vom lokalen Funktionsumfang zu unterscheiden und hier nicht gemessen. Weitere Risiken sind LLM-Datenübertragung für semantische Inhalte, zahlreiche optionale Abhängigkeiten und hohe CLI-/Integrationskomplexität.

---

## headroomlabs-ai/headroom

- **URL:** https://github.com/headroomlabs-ai/headroom
- **Stars:** ⭐ 77.292
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 2.662 · **Größe:** 70M
- **Struktur:** Rust-Kern in `crates/`, Python-Paket in `headroom/`, Integrationen in `plugins/`, umfangreiche Evals und Dokumentation; kein klassisches Skill-Paket <!-- manual -->

Headroom ist eine Apache-2.0-lizenzierte Kontext-Kompressionsschicht für LLM-Anwendungen und Coding-Agenten. Bibliothek, lokaler Proxy, MCP-Server und Agent-Wrapper reduzieren etwa Tool-Ausgaben, Logs, RAG-Chunks und Dateien vor dem Modellaufruf. Inhaltsabhängige JSON-, AST- und Text-Kompressoren arbeiten mit einem lokalen Cache der Originale, die per Retrieval nachgeladen werden können. CacheAligner und Prefix-Tracking sollen Provider-Caches nutzbar halten. Unterstützte Integrationen umfassen unter anderem Claude Code, Codex, Copilot und OpenCode; Drittanbieter-Upstreams benötigen eine passende explizite Ziel-URL.

Das Update ergänzt umschreibende Turn-Hooks für OpenAI Responses über HTTP und WebSocket, Request-bezogene Counterfactual-Savings-Datensätze und genauere Cache-Write-Zähler. Prefix-Zustand bleibt bei geordneten Neustarts erhalten. `headroom learn` wertet Sitzungen aus und kann lokale Agenten-Anweisungen ergänzen; optionale Output-Steuerung beeinflusst Antwortlänge und Reasoning-Aufwand. Die dokumentierten Einsparungen sind projektspezifische Benchmarks beziehungsweise Schätzungen, keine zugesicherte Wirkung im eigenen Betrieb.

Bei Telemetrie sind mehrere Mechanismen zu unterscheiden: Der anonyme, inhaltsfreie Upload-Beacon ist laut aktueller README und Implementierung standardmäßig aktiv. `HEADROOM_BEACON=off`, `DO_NOT_TRACK=1` oder Offline-Modus schalten ihn aus; jetzt wirkt auch `HEADROOM_TELEMETRY=off`, sofern der Beacon nicht ausdrücklich wieder aktiviert wurde. Der getrennte Cloud-Usage-Reporter bleibt opt-in. Proxy-Routing, Modellabrufe, Session-Auswertung und Änderungen an Agenten-Konfigurationen verlangen deshalb eine eigene Datenflussprüfung. Relevant als Referenz für reversible Kontextreduktion und überprüfbare Token-Ökonomie; die kommerzielle Enterprise-Ausgabe hat zusätzlichen Scope.

---

## heygen-com/hyperframes

- **URL:** https://github.com/heygen-com/hyperframes
- **Stars:** ⭐ 69.257
- **Heruntergeladen:** 2026-10-11
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 9.008 · **Größe:** 874M
- **Struktur:** Bun-/TypeScript-Monorepo mit CLI, Renderpipeline und Studio unter `packages/`, sieben veröffentlichten Skills unter `skills/` (vier Core, drei On-demand), Katalog in `registry/`, Beispielen in `examples/` und Dokumentation in `docs/`; Testmedien nutzen Git LFS <!-- manual -->

HyperFrames ist ein Apache-2.0-lizenziertes Framework, das HTML, CSS, Medien und zeitlich steuerbare Animationen über Headless Chrome und FFmpeg in Videos überführt. Kompositionen definieren Timing und Spuren mit HTML-Attributen; Adapter unterstützen unter anderem GSAP, CSS, Lottie, Three.js, Anime.js und WAAPI. Zum Bun-/TypeScript-Monorepo gehören CLI, Renderpipeline, Browser-Studio, Player, Katalog und verteilte Renderwege. Die CLI verlangt Node.js ab 22 und FFmpeg; Einstiegspunkte sind `README.md`, `packages/cli/`, `packages/engine/` und `packages/producer/`.

Stand des Updates ist CLI 0.8.185. Die veröffentlichte Skill-Struktur wurde von 21 auf sieben Skills umgestellt: `hyperframes`, `hyperframes-cli`, `hyperframes-registry` und `media-use` bilden den Kern; `figma`, `slideshow` und `remotion-to-hyperframes` kommen bei Bedarf hinzu. Film-, Motion-, Look- und Caption-Wissen liegt jetzt überwiegend in Referenzen statt separaten Workflow-Skills. Neu ist Capture Motion Blur mit Integration in Studio und Renderpipeline; Prüfberichte erklären, weshalb Blur für bestimmte Routen oder Defekte ausbleibt. Cloud-Rendering unterstützt transparente MOV-/WebM-Ausgaben in 4K und gesonderte Uploads großer Medien. Weitere Arbeiten verbessern Capture-/Encoding-Parallelität, Audio-Muting und Alpha-Proxies.

Relevant für reproduzierbare, agentengestützte Video-Produktion. Cloud-Rendering, Veröffentlichung, Medienprovider und Telemetrie sind gesonderte Datenfluss- und Kostenaspekte. Ausschließlich lokale Analyse-Referenz ohne Installation oder Aktivierung. Die Analysekopie behält ihre zuvor dokumentierten lokalen LFS-Attributausnahmen; diese ändern keine versionierten Quelldateien.

---

## humanlayer/skills

- **URL:** https://github.com/humanlayer/skills
- **Stars:** ⭐ 5.401
- **Heruntergeladen:** 2026-10-11
- **Zuletzt aktualisiert:** 2026-10-11
- **Dateien:** 102 · **Größe:** 351K
- **Struktur:** Sieben Skills/Plugins unter `plugins/`, RPI-Agenten unter `plugins/rpi/agents/`, Marketplace unter `.claude-plugin/marketplace.json`, Workflow-Vorlagen in Skill-Referenzen und TypeScript-Helfer unter `scripts/` <!-- manual -->

HumanLayer Skills ist eine Sammlung von sieben Agent-Skills für Softwareentwicklung, visuelle Erklärungen und wiederkehrende Codepflege. Sie richtet sich vor allem an Entwickler und Teams mit Claude Code; für den RPI-Ablauf beschreibt die README auch Codex-Nutzung. Es handelt sich um Markdown-Prozesse und Plugin-Pakete mit Referenzen, Templates und Hilfscode. `plugins/rpi/skills/rpi/SKILL.md` führt von Recherchefragen über Designentscheidungen, PRDs und technische Entwürfe bis zur Implementierung. Die Phasen arbeiten standardmäßig in frischen Sessions und übergeben lokale Dokumente; TDD bezeichnet hier Technical Design. `show-me` erklärt Zusammenhänge mit Diagrammen, Code-Skizzen und HTML-Artefakten; `visual-pr` erstellt oder aktualisiert Pull Requests mit einer visuellen Änderungsübersicht. Weitere Skills überarbeiten Agent-Anweisungen und verengen React-Prop-Typen anhand tatsächlich genutzter Codepfade. Besonders relevant sind `build-iterated-agentic-loop` und `design-control-loop`: Sie bereiten wiederkehrende Agent-Aufgaben mit GitHub-Actions-Workflows, Feedback-Dateien und begrenzter Zahl offener PRs vor. Das Repo enthält eine MIT-Lizenz. `.claude-plugin/marketplace.json` verzeichnet die Pakete; `scripts/` enthält TypeScript-Helfer zur Synchronisierung und Prüfung von Referenzen. Workflow-Vorlagen setzen je nach Variante Node/Bun, Agenten-CLIs, GitHub CLI, API-Secrets und weitere Werkzeuge voraus. Sie installieren teilweise aktuelle Pakete, nutzen weitreichende Agent-Berechtigungen und können Branches pushen sowie PRs schreiben. Code und Prompts gehen an den Modellanbieter; API- und Actions-Kosten sind einzuplanen. Empfehlung: ausschließlich lokale Referenz für Entwicklungsphasen, visuelle Reviews und begrenzte Agent-Schleifen; keine automatische Installation oder Workflow-Aktivierung.

---

## intellectronica/ruler

- **URL:** https://github.com/intellectronica/ruler
- **Stars:** ⭐ 2.949
- **Heruntergeladen:** 2026-07-15
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 264 · **Größe:** 71M
- **Struktur:** TypeScript-CLI mit Quellcode in `src/` (Adapter unter `src/agents/`, Rule-/Konfigurations- und Dateisystemlogik in `src/core/`, MCP-Transformationen in `src/mcp/`), umfangreichen Jest-Tests in `tests/` und GitHub-Actions-Workflows in `.github/workflows/` <!-- manual -->

Ruler ist eine MIT-lizenzierte TypeScript-CLI, die Regeln aus einem zentralen `.ruler/`-Verzeichnis in native Konfigurationen zahlreicher Coding-Agenten ausspielt. Markdown-Regeln werden rekursiv gesammelt, mit Herkunftsmarkern verbunden und unter anderem für Codex, Claude Code, Copilot, Cursor, Gemini CLI, OpenCode und Aider erzeugt. Optional verteilt das Tool MCP-Konfigurationen, Skills und Subagenten; verschachtelte `.ruler/`-Verzeichnisse erlauben abweichende Regeln für Teilbereiche eines Monorepos. Damit ist es als Referenz für gemeinsamen Projektkontext über mehrere Harnesses hinweg interessant.

Mit Version 0.3.45 werden GitHub-Copilot-Reviews und der native Skill-Pfad `.github/skills/` berücksichtigt. OpenCode-Subagenten liegen unter `.opencode/agents/`; pro Agent lassen sich Provider-/Modell-IDs und Berechtigungen überschreiben. Die Übersetzung behandelt gemeinsame Tool-Listen, konservative Read-only-Regeln und OpenCode-spezifische Pattern-Reihenfolgen. Vor dem Schreiben wird das gesamte OpenCode-Target gerendert: ungültige Modelle, reservierte Namen oder widersprüchliche Permissions lassen dessen vorhandene Dateien unverändert. Skill-Diagnosen prüfen Frontmatter und Konflikte, verändern die kopierten Inhalte aber nicht.

Backups, Provenance-Dateien, idempotente Updates und Schutz gegen Schreibvorgänge über Symlinks oder außerhalb des Projektroots gehören zur Implementierung. Praktische Grenzen bleiben: `apply` verändert viele Konfigurationsdateien und standardmäßig `.gitignore`; MCP-Einträge können Zugangsdaten referenzieren. Skills und Subagenten sind weiterhin experimentell, und Tool-Permissions ersetzen keine Betriebssystem-Sandbox. Vor einer Übernahme gezielte Agentenauswahl und `--dry-run` im Testprojekt nutzen; hier bleibt das Repo Analyse-Referenz.

---

## Jakubantalik/transitions.dev

- **URL:** https://github.com/Jakubantalik/transitions.dev
- **Stars:** ⭐ 5.487
- **Heruntergeladen:** 2026-09-14
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 456 · **Größe:** 37M
- **Struktur:** Skills unter `skills/transitions-dev/`, `skills/transitions-polish/` und `skills/transitions-ui-generation/`; dazu Showcase-Website, Community-/Builder-Oberflächen, CLI in `cli/`, Live-Werkzeug in `refine/` und Generator in `build/`. <!-- manual -->

Transitions.dev verbindet eine Sammlung wiederverwendbarer CSS-Interaktionen mit Showcase, CLI und Agent-Skills. Typische Muster sind Dropdowns, Modals, Panels, Seitenwechsel, Text-/Icon-Tausch, Zahlenanimationen, Skeletons und Fehler-Shakes. Portable Schnipsel nutzen semantische CSS-Custom-Properties, `t-*`-Klassen und Reduced-Motion-Regeln. `build/extract.mjs` erzeugt Referenzmaterial aus der Demoquelle, damit Beispiel und Skill zusammenpassen. Der Index erfasst inzwischen 32 Transition-Referenzen; Teile der README beschreiben noch den älteren Umfang.

Neu ist `skills/transitions-ui-generation/`: Eine dependency-freie Runtime zeichnet aus der vorhandenen Elementstruktur ein gepunktetes Wireframe und enthüllt die echte Oberfläche. Die Modi `skeleton` und `skeleton-texts` unterscheiden sich durch zusätzliche Text-/Agent-Log-Darstellung. Daneben bestehen CLI, Motion-Analyse-/Polish-Agent und das ältere Refine-Werkzeug. Das aktuelle Produkt erweitert Community und Builder/Studio um Komponenten-Remix, Moderationszustände, Credits und mobile Bedienung. Große Agent-Läufe werden in Schritte zerlegt und behalten Teilergebnisse; unterbrochene Drafts lassen sich erneut anstoßen.

Relevant als Motion-Bibliothek und als Referenz für Demo, Generator, CLI und Skills aus gemeinsamen Quellen. Lokale Bibliotheksnutzung und gehostete KI-Funktionen sind getrennt zu betrachten; Pro-Inhalte, MCP-Zugriff und Credits hängen vom Angebot und Konto ab. Transitions und Skills dürfen laut Repository in privaten und kommerziellen Projekten genutzt, verändert und ausgeliefert werden, jedoch nicht als konkurrierende Bibliothek weitervertrieben werden; Tooling ist MIT. Vor Übernahme konkrete Lizenzdateien und Datenflüsse prüfen.

---

## jakubkrehel/make-interfaces-feel-better

- **URL:** https://github.com/jakubkrehel/make-interfaces-feel-better
- **Stars:** ⭐ 3.756
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-09-17
- **Dateien:** 12 · **Größe:** 48K
- **Struktur:** 1× SKILL.md · Ordner: skills, agents

Ein einzelner, bewusst kompakter Design-Engineering-Skill für die letzte Qualitätsstufe einer Oberfläche. Er bündelt konkrete Regeln zu konzentrischen Border-Radien, optischer statt rein geometrischer Ausrichtung, transparenten Schatten, ausreichenden Hit Areas, Font Smoothing, ausgeglichenem Textumbruch, tabellarischen Zahlen, subtilen Bild-Outlines und Icons. Die neue Icon-Referenz behandelt u.a. optisches Gewicht passend zur Typografie, `currentColor`-basierte Zustände, Outline-vs.-Fill, kleine Rastergrößen, RTL-Spiegelung und zugängliche Icon-only Controls. Weitere Referenzen decken unterbrechbare Interaktionen, gestaffelte Enter- und sanfte Exit-Animationen sowie eine sparsame, GPU-freundliche Nutzung von CSS-Transitions und `will-change` ab. Besonders nützlich ist das vorgegebene Review-Format: Änderungen werden je Prinzip als Tabelle mit „Before“ und „After“ dokumentiert, nicht als unspezifische Design-Meinung. Das ergänzt breitere UI-/UX- und Frontend-Skills gut als abschließender Polish-Pass. Einige Regeln sind absichtlich sehr konkret und sollten als Heuristik statt als Produktdesign-Gesetz behandelt werden; bei Barrierefreiheit, Performance und Markenvorgaben haben projektspezifische Anforderungen Vorrang. Der Skill enthält keine Scripts, Netzwerkzugriffe oder Credential-Anweisungen. Er verweist relativ auf fünf Dokumente, weshalb bei einer selektiven Übernahme der gesamte Skill-Ordner erhalten bleiben muss. MIT-lizenziert.

---

## juliusbrussee/caveman

- **URL:** https://github.com/juliusbrussee/caveman
- **Stars:** ⭐ 114.150
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 1.791 · **Größe:** 21M
- **Struktur:** Skills als Quelle der Wahrheit in `skills/`, Subagenten in `agents/`, Command-Stubs in `commands/`, interner Code in `src/` (`hooks/`, `rules/`, `tools/`, `mcp-servers/`); Claude-Plugin-Spiegel in `plugins/caveman/` (CI-generiert) <!-- manual -->

Caveman ist inzwischen eine Apache-2.0-lizenzierte Suite zur Token- und Kostensenkung für Coding-Agenten, nicht mehr nur ein knapper Antwortstil. Version 4.0.1 beschreibt sechs Teile: `Say less` für Ausgabe, `Read less` für komprimierte Eingaben, `Auto` für Modell-/Reasoning-Auswahl, `Blocks` für wiederverwendbare Skripte, `Waste fixes` mit Lernanalyse und Warm Cache sowie `Browse` für reduzierte Webseitenansichten. Die Stil-Skills heißen `/caveman`, `/ultracave` und `/megacave`; Code, Befehle und Fehlermeldungen sollen unverändert bleiben. CLI, Proxy, Middleware und agentenspezifische Adapter erweitern den Einsatz über zahlreiche Harnesses.

`Blocks` bewahrt wiederkehrende Code-Mode-Skripte im Projekt auf; `learn` analysiert lokale Sitzungsverläufe und schlägt Änderungen einzeln zur Bestätigung vor. Die README trennt kleine Fixtures, vollständige Sessions und vorläufige Auto-Routing-Benchmarks und nennt Gegenbeispiele sowie eigenen Prompt-Overhead. Diese Zahlen sind Hersteller-Evidenz, kein allgemeiner Nachweis gleicher Qualität oder eigener Einsparung.

Der Vollinstaller verändert Agenten-Konfigurationen und aktiviert grundsätzlich die verfügbaren Teile. Die CLI sendet standardmäßig Nutzungsstatistiken; Abschaltung über `caveman telemetry off` oder `DO_NOT_TRACK=1`. Auto benötigt Anmeldung und Auswahl und sendet dann unter anderem aktuelle/vorherige Anfrage samt angehängtem Kontext an Caveman Cloud; bei Cloud-Modellrouting können vollständige Requests passieren. Auch `/caveman-compress` übermittelt die betreffende Datei an den konfigurierten Modellprovider. Die reine Stil-Skill-Nutzung ist davon zu unterscheiden. Vor produktiver Übernahme Konfigurationsänderungen, Provider-Routing, Telemetrie und tatsächliche Kosten prüfen; hier ausschließlich Analyse-Referenz.

---

## karpathy/autoresearch

- **URL:** https://github.com/karpathy/autoresearch
- **Stars:** ⭐ 98.319
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-07-13
- **Dateien:** 10 · **Größe:** 747K
- **Struktur:** bewusst minimal: `prepare.py` für feste Daten-/Runtime-Vorbereitung, `train.py` als einzige Agenten-Änderungsfläche und `program.md` als menschlicher Steuervertrag <!-- manual -->

Autoresearch ist Andrej Karpathys bewusst kleines Experiment für autonome LLM-Forschung auf einer einzelnen NVIDIA-GPU. Ein Agent darf ausschließlich `train.py` verändern, startet dann einen festen fünfminütigen Trainingslauf, misst `val_bpb` (niedriger ist besser), behält Verbesserungen und verwirft Verschlechterungen. Die konstant gehaltene Laufzeit macht Experimente auf derselben Hardware vergleichbar; die menschliche Steuerung liegt nicht in einem komplexen Framework, sondern in `program.md`, das Rollen, Grenzen und Ziel der Agentenarbeit beschreibt. `prepare.py` bleibt unverändert und übernimmt einmalige Daten- und Tokenizer-Vorbereitung, während `train.py` Modell, Optimierer und Trainingsloop enthält. Das Projekt ist absichtlich keine allgemeine AutoML-Plattform: Es verlangt laut README Python 3.10+, `uv` und eine einzelne NVIDIA-GPU (getestet auf H100); Daten-Downloads und Trainingsläufe verursachen Rechen- und potenziell Cloudkosten. Relevant als sehr klares Pattern für autonome Iteration: eine enge Änderungsfläche, ein fester Budgetrahmen, eine objektive Metrik und explizite menschliche Regeln. Für dieses Repo ist es primär ein Vorbild für experimentelles Agenten-Design, nicht ein sofort einsetzbarer Produktworkflow. Die README nennt MIT, eine Root-Lizenzdatei fehlt im geklonten Stand jedoch; Lizenz vor Übernahme separat verifizieren.

---

## kepano/obsidian-skills

- **URL:** https://github.com/kepano/obsidian-skills
- **Stars:** ⭐ 49.889
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-09-17
- **Dateien:** 15 · **Größe:** 57K
- **Struktur:** 6× SKILL.md · Ordner: skills, references

Kepanos kompakte Skill-Sammlung ergänzt Agenten um Obsidian-spezifisches Wissen, ohne ein eigenes Framework zu erzwingen. Sie enthält sechs klar getrennte Skills: `obsidian-markdown` für Wikilinks, Embeds, Callouts und Properties; `obsidian-bases` für datenbankartige `.base`-Ansichten mit Filtern und Formeln; `json-canvas` für valide `.canvas`-Dateien; `obsidian-cli` für die Arbeit mit einer laufenden Obsidian-Instanz; `defuddle` zum Extrahieren von sauberem Markdown aus Webseiten; sowie neu `knap` zum Rendern von Markdown aus Templates und strukturierten JSON-/CSV-Daten über die Knap-CLI, u.a. um Defuddle-Output in ein einheitliches Notizformat zu bringen. Besonders passend ist `obsidian-markdown`: Das Repo ist selbst ein Obsidian-Vault, verwendet Wiki-Links und legt Wert auf portable Markdown-Dateien. JSON Canvas und Bases sind sinnvolle Ergänzungen, falls künftig visuelle Maps oder querybare Arbeitsübersichten explizit gewünscht werden. Der CLI-Skill kann Dateien ändern, JavaScript im Obsidian-Kontext ausführen, Plugins neu laden und Screenshots erstellen; daher nur mit klar benanntem Vault und enger Aufgabe verwenden. `defuddle` fordert bei Bedarf eine globale npm-Installation und ruft externe URLs ab. Das Repository enthält keine eigenen ausführbaren Scripts; die Hauptgefahr liegt in den durch Skills ausgelösten CLI-, Installations- und Netzwerkaktionen. Als Referenz sowie für eine selektive Übernahme einzelner, überprüfter Skills gut geeignet. MIT-lizenziert.

---

## langchain-ai/openwiki

- **URL:** https://github.com/langchain-ai/openwiki
- **Stars:** ⭐ 17.325
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 585 · **Größe:** 18M
- **Struktur:** Reiner Anwendungscode in `src/` (agent, auth, connectors, cli.tsx) plus `test/` und `examples/`; kein Skill-/Agent-Definitionsordner im OS-Sinne — der Ordner `openwiki/` enthält nur die vom Tool selbst generierte Wiki-Doku, und `AGENTS.md`/`CLAUDE.md` sind autogenerierte Verweisdateien auf diese Doku, keine Agentendefinitionen. <!-- manual -->

OpenWiki ist LangChains Node-/TypeScript-CLI für verknüpfte Markdown-Wikis aus Code und persönlichen Wissensquellen. Code-Wikis liegen im Repository unter `openwiki/`; persönliche Wikis können lokale Repos und Connectoren etwa für Gmail, Notion, Slack oder X einbeziehen. Coding-Agent-Integrationen verwenden deren vorhandene Sitzung und Repository-Werkzeuge; der native CLI-Weg nutzt konfigurierbare Modellprovider. Such- und Lesewerkzeuge sind lokal, read-only und modellfrei; verknüpfte Workspaces erlauben Retrieval über mehrere Repos. Ein interaktiver Graph ergänzt die Markdown-Seiten.

Die Generierung folgt einer dauerhaften Seitenqueue von `begin` über Planung und Seitenabgabe bis `finish`. Grounded Claims tragen Quellbelege; abgeschlossene Seiten überleben Unterbrechungen auf persistenten Checkouts. Native Worker können mehrere Seiten parallel bearbeiten, Host-Integrationen verwenden den sequenziellen Lifecycle. Version 0.7.2 stärkt die Grenzen: Update-Planung folgt ausdrücklichen Anfragen, Operationen derselben Seite werden serialisiert, erfolglose Worker einmal wiederholt und abgeschnittene Übersetzungen ersetzen keine intakten Seiten. Bedrock-Throttling senkt die Parallelität. Anker-, Link- und Frontmatter-Korrekturen verbessern das Retrieval.

Relevant als Referenz für evidenzgebundene Projektdokumentation, sparsame Kontextsuche und wiederaufnehmbare Agent-Pipelines. MIT-lizenziert, benötigt Node 22.22+ und native `better-sqlite3`-Abhängigkeiten. Provider- und Connector-Zugänge, lokale Credential-Speicherung, LLM-Kosten und CI-Schreibrechte verlangen eine eigene Übernahmeprüfung. Telemetrie ist standardmäßig aktiv und abschaltbar; der Visualizer lädt CDN-Bibliotheken. Ein erneutes `--init` ersetzt das generierte Wiki, während `INSTRUCTIONS.md` erhalten bleibt. Hier ausschließlich statisch als Analysekopie geprüft.

---

## latent-spaces/brag

- **URL:** https://github.com/latent-spaces/brag
- **Stars:** ⭐ 17.351
- **Heruntergeladen:** 2026-10-02
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 369 · **Größe:** 62M
- **Struktur:** 2× SKILL.md · Ordner: skills, references · Spiegelordner: .agents, .claude, .opencode (generiert)

`/brag` ist ein Agent-Skill, der aus einem fertigen Projekt ein kurzes Launch-Video (15–25 s) samt Musik, Soundeffekten und Share-Texten für X oder LinkedIn macht. Statt Screenshots oder einer Live-URL liest der Agent den Projektcode selbst, entwickelt daraus einen projektspezifischen Video-Plan mit Storyboard und übergibt ein fokussiertes Composition-Brief an Hyperframes (HeyGen), das Video rendert. Gesteuert wird über Optionen wie `--tone` (Presets von `polished` bis `yc-parody` oder freie Regie), `--format` (quer, hochkant, quadratisch) und optional `--voice` (Kokoro-Sprecher). Der Ablauf ist in vier Referenzdateien (Inspect, Plan, Compose, Deliver) zerlegt; ein Python-Script analysiert Musik-Cues für den Schnitt. Neu ist `/brag-slim`: eine schlanke Einzeldatei-Variante ohne Hyperframes und gebündelte Assets, bei der Opus 5.5 das ganze Video selbst baut. Deren Inspektion schließt jetzt Build-Ausgaben, Lockfiles, Tests, ignorierte Konfiguration und Geheimnisdateien aus; sensible UI-Daten müssen vor Plan, Video und Share-Text durch als fiktiv ausgewiesene Beispieldaten ersetzt werden. Bemerkenswert als Muster ist der modellabhängige Dispatch am Skill-Anfang: Erkennt sich das Modell als Opus 5.5, wechselt der Skill automatisch zur Slim-Variante und sagt das dem Nutzer in einer Zeile. Das Repo verteilt denselben Skill per Symlinks an die Discovery-Pfade von Claude Code, Codex, opencode und Antigravity sowie als Plugin-Manifeste (`.claude-plugin/`, `.codex-plugin/`, `plugin.json`); fünf erfundene Demo-Sites in `examples/` dienen als Benchmark-Suite. Relevant als Referenz für Skill-Distribution über mehrere Agenten und als Werkzeug für Launch-Content der Wissensfabrik. Voraussetzungen: Node.js 22+, FFmpeg, Hyperframes-CLI. Auf Windows funktionieren die Symlinks nur mit `core.symlinks` und Developer Mode. MIT-lizenziert, gehostete Variante unter letsbrag.app.

---

## Leonxlnx/taste-skill

- **URL:** https://github.com/Leonxlnx/taste-skill
- **Stars:** ⭐ 100.612
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 69 · **Größe:** 3,0M
- **Struktur:** 1× SKILL.md · Ordner: skills, references · Spiegelordner: .agents (generiert)

Taste Skill ist inzwischen ein einzelner Agent-Skill mit Installationsnamen `design-taste-frontend` für Websites und App-Oberflächen. Version 2 ersetzt die frühere Sammlung durch einen Ablauf aus Brief-Inventar, zugeloster Designrichtung, projektspezifischer Idee, Umsetzung, Browserprüfung und Screenshot-Kritik. Laut Autor stammen die Richtungen aus einer Untersuchung von 247 kuratierten Sites; spätere Regeln beziehen weitere Awwwards-Seiten ein. Das ist die dokumentierte Herkunft des Designsystems, kein eigener Qualitätsnachweis.

Version 2.1 unterscheidet Websites von Dashboards, Admin- und Settings-Screens. Für Apps gibt es sieben Stilrichtungen sowie eigene Regeln für Shells, Tabellen, Charts, echte beziehungsweise korrekt ausgewiesene Daten, Leerzustände und mobile Navigation. Node-Scripts wählen Vorlagen, suchen Bilder in offenen Sammlungen und prüfen Source sowie gerenderte Oberflächen bei mehreren Breiten. Gefundene Bilder werden mit Lizenz- und Herkunftsangaben erfasst. Eigene Inhalte und bestehende Stacks sollen bei Redesigns erhalten bleiben; deren Ausgangszustand wird im Browser dokumentiert.

Klassische Stil-Skills liegen jetzt in `Leonxlnx/taste-skill-classics`, Bild-/Brandkit-Skills in `Leonxlnx/imagegen-skills`; Full-Output-Enforcement wurde entfernt. Der Checkout dokumentiert 2.1.4 mit strikt geprüftem Frontmatter und Prozessbesitz für temporäre Browser-Profile. MIT-lizenziert, frameworkunabhängig, benötigt Node 22+ und Chrome, Edge oder Chromium sowie Netzwerk für Bildsuche. Die README nennt erheblichen Zeit- und Tokenaufwand. Relevant als Referenz für konkrete Designregeln und Browserfeedback; externe Scripts, Medienlizenzen und automatische Bereinigungen vor Übernahme gesondert prüfen.

---

## mattpocock/dictionary-of-ai-coding

- **URL:** https://github.com/mattpocock/dictionary-of-ai-coding
- **Stars:** ⭐ 5.211
- **Heruntergeladen:** 2026-09-14
- **Zuletzt aktualisiert:** 2026-09-27
- **Dateien:** 90 · **Größe:** 331K
- **Struktur:** Wissensbasis ohne Skill-Paket: 71 Begriffsdateien in `dictionary/`, Kuration und Generator in `internal/`, generierte `README.md` als Gesamtansicht (`dictionary/Skill.md` ist ein Lexikoneintrag, kein Agent-Skill) <!-- manual -->

Nachschlagewerk von Matt Pocock (AI Hero), das das Vokabular der KI-gestützten Softwareentwicklung in einfachem Englisch erklärt — ausdrücklich gegen den Eindruck, AI-Coding sei Expertensache und der Jargon Teil des Geschäftsmodells. 71 Einträge liegen als einzelne Markdown-Dateien in `dictionary/` und sind über `internal/Curriculum.md` in sieben Sektionen geordnet: Modell (Token, Inference, Effort, Prefix Cache), Sessions und Kontextfenster, Tools und Environment (Tool Call, MCP, Permission Mode, Sandbox), Fehlermodi (Sycophancy, Halluzination, Attention Budget und -Degradation, Smart Zone), Handoffs (Primary/Secondary Source, Spec, Ticket, Compaction), Memory und Steering (AGENTS.md, Progressive Disclosure, Context Pointer, Skill, Subagent) sowie Arbeitsmuster (Vibe Coding, Grilling, Prototyping, AFK, DX/AX, neu Software Factory und Dark Factory — Agenten-Sessions, die durch Trigger statt durch Menschen gestartet werden, und deren Grenzfall ganz ohne menschliches Code-Review). Die Einträge sind dicht quervernetzt, mindestens 200 Wörter lang und folgen einem festen Aufbau: Definition, Mechanik, das typische Symptom, an dem man das Problem erkennt, und ein kurzer Usage-Dialog. Die `README.md` ist daraus generiert (`npm run generate`, tsx-Script in `internal/`), ein CI-Job prüft ihre Aktualität. Nützlich zweifach: als Begriffsreferenz für eine einheitliche Fachsprache in diesem Repo — kompakter und einsteigerfreundlicher als das breitere, zitierte [mleibetseder/ai-llm-wiki](#mleibetsederai-llm-wiki) — und als Muster für agentengepflegte Wissensbasen, denn `CLAUDE.md` und `internal/` legen Schreibregister, Verlinkung, Issue-Tracker-Konventionen und ADR-Ablage explizit fest. Einschränkungen: keine Lizenzdatei, damit rechtlich „alle Rechte vorbehalten“ — nur als Referenz lesen, keine Inhalte übernehmen. Eine lesbare Vault-Kopie mit einem Ordner pro Sektion und umgeschriebenen Querverweisen erzeugt `python 70_Scripts/sync_ai_coding_dictionary.py` unter `00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/` (nach jedem Pull erneut ausführen; wegen der fehlenden Lizenz nur lokal, per `.gitignore` ausgeschlossen). Deutlicher Newsletter-Bezug zu aihero.dev, letzter Commit 24.09.2026 (51 Commits seit Mai 2026), Node-Tooling (husky, lint-staged, tsx) wird nicht benötigt und nicht ausgeführt.

---

## mattpocock/skills

- **URL:** https://github.com/mattpocock/skills
- **Stars:** ⭐ 299.931
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 191 · **Größe:** 730K
- **Struktur:** 38× SKILL.md · Ordner: skills, agents

Matt Pococks Skills bündeln kleine, anpassbare Engineering- und Produktivitätsabläufe statt eines durchgehend vorgeschriebenen Entwicklungsframeworks. Sie adressieren Missverständnisse durch Grilling, gemeinsame Fachsprache durch `GLOSSARY.md` und ADRs, funktionales Feedback durch TDD und Diagnose sowie Architekturpflege durch tiefe Module. Die Engineering-Kette führt von Spezifikation und Tickets über Implementierung bis Code-Review und Retrospektive. User-invoked Skills orchestrieren nur nach ausdrücklichem Aufruf; model-invoked Skills liefern wiederverwendbare Disziplin. Ein User-Skill darf keine anderen User-Skills aufrufen.

Aktuelle Korrekturen machen die Evidenz genauer: `code-review` sucht sämtliche Standardsquellen und führt Standards- und Spec-Achse parallel mit getrennter Bewertung aus. `diagnosing-bugs` verlangt bei einem erzwungenen Red den Nachweis der tatsächlich angewendeten Mutation; TDD nennt Reichweite und Lücken vorgeschlagener Prüfschnittstellen. `implement` lädt referenzierte Tickets, `to-tickets` verknüpft Sub-Issues und Setup pflegt Triage-Labels. Der Bash-Wizard behandelt bestehende `.env`-Werte, Quoting, EOF und Symlinks zuverlässiger; Handoff vermeidet Shell-Interpolation.

Im Bereich `skills/in-progress/` entwickelt `chief-of-staff` langfristige Orchestrierung mit einer verlinkten Markdown-Wiki: Aussagen werden datiert, Codebezug erhält Repo und Commit, überholte Aussagen bleiben als Historie sichtbar. Ingest, Query und Lint sollen Wissen über Kontextwechsel erhalten; dieser Ansatz bleibt experimentell. Relevant als Vorbild für modulare Skills, Review-Trennung und überprüfbare Wissenspflege. Plugin-Updates und manuell editierbare Kopien sind getrennte Installationswege; produktive Übernahme und mögliche Tracker-Schreibwirkungen bleiben einzeln zu prüfen.

---

## microsoft/markitdown

- **URL:** https://github.com/microsoft/markitdown
- **Stars:** ⭐ 191.496
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 196 · **Größe:** 26M
- **Struktur:** keine Standard-Skill-/Agent-Ordner (Quellcode/CLI oder reine Doku)

MarkItDown ist ein von Microsoft (AutoGen-Team) entwickeltes Python-Utility, das diverse Dateiformate (PDF, Word, PowerPoint, Excel, Bilder, Audio, HTML, CSV/JSON/XML, ZIP, EPub, YouTube-URLs) in Markdown konvertiert, um sie für LLM-Pipelines und Textanalyse nutzbar zu machen. Der Ansatz: Struktur (Überschriften, Listen, Tabellen, Links) wird erhalten, das Ergebnis ist nicht auf menschliche Lesbarkeit, sondern auf Token-Effizienz und LLM-Verständlichkeit optimiert. Technisch gibt es eine CLI (`markitdown datei.pdf`), eine Python-API, einen Docker-Container sowie einen separaten MCP-Server (`markitdown-mcp`), der die Konvertierung direkt als Tool in MCP-fähige Agenten-Umgebungen einbindet – dadurch unmittelbar relevant für Agenten- und Tool-Workflows in KI-gestützten Arbeitsumgebungen. Ein Plugin-System erlaubt Erweiterungen (z. B. `markitdown-ocr` für LLM-gestützte OCR über Vision-Modelle); optional Azure Document Intelligence/Content Understanding für höherwertige Cloud-Konvertierung. Stärken: breite Formatunterstützung, leichtgewichtig, aktiv von Microsoft gepflegt, klare Sicherheitsdoku. Risiken: explizit dokumentierte Sicherheitswarnung, da I/O mit Prozessrechten erfolgen (SSRF/Path-Traversal-Risiko bei ungeprüften Eingaben), Konvertierungsqualität ist funktional statt hochtreu, viele optionale Abhängigkeiten (`[all]`) erhöhen die Angriffsfläche, und Cloud-Feature (Azure) verursachen laufende Kosten. MIT-lizenziert.

---

## midudev/autoskills

- **URL:** https://github.com/midudev/autoskills
- **Stars:** ⭐ 6.968
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 4.574 · **Größe:** 32M
- **Struktur:** CLI-Quellcode in `src/` und `packages/`; kuratierte, gehashte Skill-Registry und Metadaten im Repository; keine klassische Quellenstruktur je Skill <!-- manual -->

Autoskills ist eine Node.js-CLI, die ein Projekt analysiert, dessen Tech-Stack aus Manifesten und Konfigurationen ableitet und dazu passende Agent-Skills installiert. Der interessante Teil ist weniger der Ein-Befehl-Installer als das Supply-Chain-Modell: Die Skills werden laut README nicht zur Laufzeit aus beliebigen Upstream-Repos gezogen, sondern von Maintainer:innen in eine repositoryeigene Registry synchronisiert, zweistufig von KI auf Prompt-Injection- und Supply-Chain-Risiken geprüft (schnelle Triage, stärkere Modellentscheidung bei Verdachtsfällen) und mit SHA-256-Hashes im Manifest festgehalten. Der Installer lädt nur die ausgewählten Registry-Dateien, verifiziert sie gegen das Manifest und schreibt Herkunft und Bundle-Hash in ein `skills-lock.json`. Version 0.4.1 ergänzt eine lokale Webübersicht installierter Skills (`autoskills ui`), parallele Downloads und Registry-Synchronisierung mit Entfernung upstream gelöschter Einträge. Als akzeptabel eingestufte Skills können vor Installation dennoch einen Sicherheitshinweis erhalten; die KI-Prüfung ersetzt keine eigene Übernahmeprüfung. Deno wird seit 0.4.0 nicht mehr unterstützt. Unterstützt werden breite moderne Stacks von React/Next.js bis zu Flutter, Cloudflare, Datenbanken, Testing und AI-/Media-Tools. Relevant als Referenz für eine kuratierte statt beliebige Skill-Beschaffung und für Lockfile-/Hash-basierte Nachvollziehbarkeit. Die README verspricht eine automatische Auswahl, die konkreten Regeln und die Registry bleiben dennoch unabhängig zu prüfen; der Installer schreibt Dateien in Zielprojekte und benötigt Node.js ab 22.6. Besonders wertvoll ist das Muster „vorprüfen → paketieren → verifizieren → locken“, nicht eine unreflektierte Masseninstallation. Die Lizenz CC BY-NC 4.0 schränkt insbesondere kommerzielle Nutzung ein.

---

## millionco/react-doctor

- **URL:** https://github.com/millionco/react-doctor
- **Stars:** ⭐ 15.034
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 7.416 · **Größe:** 40M
- **Struktur:** TypeScript-Monorepo in `packages/`; Kern-CLI in `packages/react-doctor/`, ergänzende ESLint-/Oxlint-/Language-Server-/Editor-Pakete sowie Skills in `skills/`; Provider-Artefakte in `.agents/` <!-- manual -->

React Doctor ist ein deterministischer Auditor für React-Codebasen. Die CLI scannt laut Paket-README Probleme in State und Effects, Performance, Architektur, Security und Accessibility und soll mit unterschiedlichen React-Frameworks und Bibliotheken arbeiten, darunter Next.js, Vite, TanStack, React Native und Expo. Ein schneller Lauf erfolgt über `npx react-doctor`; Konfigurationen lassen sich in `doctor.config.ts` anpassen, und JSON-Ausgaben enthalten stabile Diagnose-IDs sowie projektbezogene Scan-Abdeckung. Nach einem Audit kann die CLI eine passende Skill-Anleitung für Coding-Agenten wie Claude Code, Cursor, Codex oder OpenCode installieren. Für CI erstellt sie GitHub-Workflows, die Pull Requests auf neu eingeführte Findings prüfen, statt den gesamten historischen Backlog als Blocker zu behandeln; GitLab erhält einen Gate-Entwurf. Kontextbezogene Diff-Scopes berücksichtigen nun explizite Eigentümer von Findings, und Warnungen bekommen einen separaten Exit-Code. Zahlreiche Regeln verfolgen Cancellation sowie Listener-/Object-URL-Lebenszyklen genauer; GitHub Actions respektieren den Projekt-Paketmanager und schließen Base-Branch-Drift aus dem PR-Dateivergleich aus. Das Monorepo enthält außerdem Regeln bzw. Integrationen für ESLint, Oxlint, Language Server, VS Code und Zed. Neuere Ausbaustufen ergänzen React-bewusste Laufzeit-Traces in der CLI, Regeln zu UI-Library-Komposition und -Korrektheit hinter Capability-Gates sowie einen `improve-threejs`-Skill; die ESLint-Presets berücksichtigen jetzt den React Compiler. Relevant als ausführbares Gegenstück zu den eher regelbasierten Frontend-Skills im Index: zuerst deterministisch feststellen, was im konkreten Projekt problematisch ist, dann gezielt beheben. Die CLI sendet standardmäßig anonyme Nutzungs- und Laufzeitdaten sowie Regelzähler an Sentry; `--no-telemetry` deaktiviert dies. Die Root-Lizenz ist eine modifizierte MIT-Lizenz und verlangt für ML-Training/-Evaluation sowie bestimmte kommerzielle Hosting-/SaaS-Nutzungen vorherige schriftliche Zustimmung – daher vor Übernahme oder Produktintegration rechtlich prüfen und nur als Referenz nutzen.

---

## mleibetseder/ai-llm-wiki

- **URL:** https://github.com/mleibetseder/ai-llm-wiki
- **Stars:** ⭐ n/a (privates Repo, API nicht abrufbar)
- **Heruntergeladen:** 2026-07-14
- **Zuletzt aktualisiert:** 2026-09-17
- **Ablage (abweichend):** `external_knowledge/ai-llm-wiki/` — bewusst außerhalb von `external_repos/`, daher NICHT vom Update-Script erfasst; Pflege manuell via `git -C external_knowledge/ai-llm-wiki pull` <!-- manual -->
- **Dateien:** 2.220 · **Größe:** 546M <!-- manual -->
- **Struktur:** Obsidian-Vault: Rohquellen in `raw/` (234 Markdown-Artikel + 25 PDFs), synthetisiertes Wiki in `wiki/` (380 `concept-*`, 115 `entity-*`, 16 `paper-*`); Ingestion-Regeln in `agents.md` <!-- manual -->

Persönliche, LLM-gepflegte Wissenssammlung eines Kollegen (Obsidian-Wissensgraph) zu AI-/LLM-Engineering. Ein Agent liest Quellen (Artikel, Papers, Bücher) nach den Regeln in `agents.md` ein und destilliert sie in ein verlinktes Wiki mit strikter Grounding-Regel: Jede Aussage in `wiki/` muss eine Zitation auf eine Datei in `raw/` tragen; Wikilink-Minima (3 ausgehende, 1 eingehende) werden vor jedem Commit erzwungen. Thematische Schwerpunkte: Agent Skills und Harness Engineering, Context Engineering (Context Rot, Compaction, Progressive Disclosure, Memory-Tiers), Spec-Driven Development, Prompt Engineering sowie Agentic AI im Enterprise-Kontext. Der aktuelle Ausbau ergänzt vor allem agentische Design-Patterns (Google-Cloud-Referenz plus „Awesome Agentic Patterns"), Loop Engineering nach Addy Osmani, Context Engineering nach Anthropic/Kushal Banda samt dem SKILL.state-Paper, den „Practical Guide to Building Agents" von OpenAI, Manager-/Worker-Agent-Architekturen, den Langfuse/OpenTelemetry-Observability-Stack, Task-Scoped Memory Contracts, ein LLMOps-Playbook für Small Language Models sowie Notizen zur DevCon London 2026. Der Rohbestand wuchs von 213 auf 234 Artikel (plus 25 statt 24 PDFs), das Wiki von 334 auf 380 Konzeptseiten (Entities von 107 auf 115, Paper-Seiten von 15 auf 16). Frühere Ausbauten hatten unter anderem Intent-Driven Development, eine Verification Layer, Agent Security/Red-Teaming und Agent-Native Memory ergänzt. Relevant als bereits verdichtete, zitierte Sekundärquelle mit großer thematischer Überschneidung zu diesem Repo — Einstieg über `wiki/concept-*.md` statt über das Rohmaterial. Achtung: private Sammlung ohne Lizenz; PDFs teils urheberrechtlich geschützt, Inhalte nicht weiterverbreiten.

---

## morluto/rea

- **URL:** https://github.com/morluto/rea
- **Stars:** ⭐ 358.296
- **Heruntergeladen:** 2026-10-11
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 5.164 · **Größe:** 63M
- **Struktur:** CLI, MCP und Analyseadapter in `src/`, Host-Brücken in `bridge/` und `native/`, ergänzender Skill unter `.agents/skills/reverse-engineer-anything/`, Dokumentation in `docs/` und Drittanbieterhinweise in `third_party/` und `licenses/` <!-- manual -->

REA („Reverse Engineer Anything“) ist ein CLI- und MCP-Werkzeug für beleggestützte Analyse von Anwendungen, Binärdateien und Laufzeitverhalten. Ein ergänzender Agent-Skill beschreibt Untersuchungsabläufe; das Repository ist keine reine Skill-Sammlung. Neben JavaScript/Electron, .NET und nativen Programmen umfasst der aktuelle Checkout Android/Flutter und Unity-IL2CPP, SQLite-Snapshots, Godot-/PyInstaller-Archive, GGUF-/safetensors-Metadaten sowie CUDA/HIP-Codeobjekte. Native Analyse verwendet je nach Ziel Hopper, Ghidra, IDA oder Kuna; Format- und Betriebssystemgrenzen bleiben providerspezifisch. Paketversion ist 6.7.0, zusätzliche Funktionen auf main können erst später veröffentlicht werden.

Gespeicherte Netzwerk- und Browser-Scenario-Captures lassen sich in Environment-Manifeste und Replay-Umgebungen überführen. HAR/SAZ, ausgewählte Protobuf-/gRPC-Nutzdaten und retained Evidence unterstützen nachvollziehbare Folgeschritte, selektive Abfragen, Zusammenfassungen und Paging. MCP bietet neben dem lokalen Standard einen optionalen Streamable-HTTP-Transport. Aktuelle Fixes erhalten Abbruchgründe und unbekannte Abdeckung über Cleanup hinweg, prüfen Quellidentitäten und lehnen kollidierende Extraktionspfade ab.

Einstiege sind `README.md`, `docs/installation.md`, `docs/cli.md` und `docs/mcp-contracts.md`; Workflow-Anweisungen liegen unter `.agents/skills/reverse-engineer-anything/`. Unterstützte Node-Versionen beginnen bei 22.19 beziehungsweise 24.11 oder 26; einzelne Werkzeuge verlangen neuere Versionen. Root-Code ist MIT-lizenziert, Drittmaterial behält eigene Bedingungen. Setup verändert Agent-Konfigurationen nach Bestätigung und kann Hopper installieren; Source-Prepare kann Husky einrichten. Laufzeitbeobachtung bedient Programme mit Benutzerrechten, Ergebnisse erreichen den Modellanbieter des Agents. Ausschließlich lokale Referenz; keine Installation, Integration oder eigene Provider-Abnahme.

---

## msitarzewski/agency-agents

- **URL:** https://github.com/msitarzewski/agency-agents
- **Stars:** ⭐ 162.957
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 383 · **Größe:** 4,7M
- **Struktur:** Keine Standard-Ordner skills/agents/commands/hooks; stattdessen 17 thematische "Divisions"-Verzeichnisse (engineering, marketing, sales, design, security, gis, healthcare u.a.) mit insgesamt ca. 250 Markdown-Agentendateien mit YAML-Frontmatter (name, description, color, vibe), ergänzt um `integrations/` (generierte Konvertierungs-Outputs pro Tool), `strategy/` (Playbooks/Runbooks) und `scripts/` (Bash/Python-Installer und Konverter). <!-- manual -->

Agency-agents ist eine umfangreiche Sammlung spezialisierter KI-Personas als Markdown-Dateien mit YAML-Frontmatter. Fachbereiche reichen von Engineering, Design, Marketing und Sales bis Security, Finance, GIS, Healthcare und Research. Jede Definition verbindet Rolle, Arbeitsablauf, Codebeispiele, Kommunikationsstil und Erfolgsmetriken. Die Research Division enthält etwa einen Research Synthesist zur gewichteten Zusammenführung vorhandener Evidenz; andere Spezialisten decken Privacy Engineering, Knowledge Graphs, PDF-Erzeugung und datengetriebene Oberflächen ab.

Shell-Installer und Konverter übertragen die Definitionen in Hostformate für Claude Code, Codex, Cursor, Gemini, OpenCode, Qwen und weitere Werkzeuge; Auswahl nach Division oder Agentenliste begrenzt den Rollout. Qwen benötigt laut aktueller Dokumentation mindestens 0.25.1, damit `${…}` in Codebeispielen keinen Launch-Fehler auslöst. Ein Linter verbietet dessen reservierte Launch-Platzhalter in Agententexten. Playbooks und Runbooks unter `strategy/` unterstützen Multi-Agent-Koordination; ergänzend existiert eine Desktop-App.

Der jüngste Lauf repariert zahlreiche Beispiele und fachliche Berechnungen: Bestell- statt Positionszählung in RFM, getrennte Zahlungswährungen, sichere Roblox-Datenladepfade, servergebundene Godot-RPCs, begrenzte Retries und PDF-Validierung vor Konformitätsbehauptungen. Das verbessert die Vorlage, beweist aber keine erfolgreiche Ausführung aller Rollen. Die MIT-lizenzierte Sammlung eignet sich als Referenz für Persona-Struktur und Multi-Tool-Distribution. Agenten sind Promptdefinitionen; behauptete Produktionserfolge, regulatorische Eignung und Erfolgsmetriken bleiben zu prüfen. Installer, Konverter und enthaltene Befehlsbeispiele vor tatsächlicher Übernahme einzeln sichten.

---

## multica-ai/andrej-karpathy-skills

- **URL:** https://github.com/multica-ai/andrej-karpathy-skills
- **Stars:** ⭐ 221.977
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-07-13
- **Dateien:** 9 · **Größe:** 38K
- **Struktur:** Nur ein Ordner `skills/karpathy-guidelines` mit einer einzigen SKILL.md, deren Inhalt zusätzlich als `CLAUDE.md` und als Cursor-Rule (`.cursor/rules/karpathy-guidelines.mdc`) dupliziert vorliegt – kein Skill-Set, sondern ein einzelnes Verhaltens-/Prompt-Dokument in drei Distributionsformaten, verpackt als Claude-Code-Plugin/Marketplace-Eintrag (`.claude-plugin/`). <!-- manual -->

Das Repository ist kein Code- oder Anwendungsprojekt, sondern ein einzelnes Prompt-Dokument mit vier Verhaltensregeln für LLM-Coding-Agenten (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution), das typische Schwächen von Coding-Agenten adressieren soll: falsche Annahmen ohne Rückfrage, Überkomplizierung, ungewollte Nebenänderungen und vage Erfolgskriterien. Der Inhalt ist bewusst schlank gehalten und dreifach ausgeliefert – als CLAUDE.md, als Cursor-Regel und als Claude-Code-Skill/Plugin über einen eigenen Marketplace-Eintrag. Wichtig für die Einordnung: Trotz des Namens "andrej-karpathy-skills" stammt das Projekt nicht von Andrej Karpathy selbst, sondern von einem Drittanbieter (GitHub-Nutzer "forrestchang", Organisation "multica-ai"); es leitet sich lediglich inhaltlich von einem öffentlichen X-Post Karpathys über LLM-Coding-Fehler ab und wirbt zudem im README aktiv für das kommerzielle/eigene Folgeprojekt "Multica" des Autors – ein deutlicher Unterschied zu tatsächlich von Karpathy selbst betriebenen Repos wie [karpathy/autoresearch](#karpathyautoresearch). Relevanz für das eigene Projekt ist gering bis mittel: allenfalls als kompakte, sofort einsetzbare CLAUDE.md-Vorlage für Agenten-Grundverhalten, nicht als eigenständiges Skill- oder Agenten-Framework. Risiko: Namensgebung kann Urheberschaft vortäuschen und ist eher Marketing-Trittbrettfahrerei als Zeichen inhaltlicher Tiefe. MIT-lizenziert (laut README und plugin.json/marketplace.json angegeben, aber keine separate LICENSE-Datei im Repo-Root vorhanden).

---

## nextlevelbuilder/ui-ux-pro-max-skill

- **URL:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- **Stars:** ⭐ 138.520
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 693 · **Größe:** 21M
- **Struktur:** Quelle der Wahrheit in `src/ui-ux-pro-max/` (`data/`, `scripts/`, `templates/`), Installer in `cli/`, Dev-Kopie in `.claude/skills/` <!-- manual -->

UI UX Pro Max ist ein datenbasierter Agent-Skill für UI-/UX-Entscheidungen über zahlreiche Plattformen. BM25-Suche und Reasoning-Regeln erschließen 79 durchsuchbare Stile, davon 50 aktiv kuratiert, 192 Produkttypen und Farbpaletten, 74 Schriftpaarungen, 25 Chart-Typen und 119 UX-Richtlinien. Ein Design-System-Generator leitet daraus Seitenmuster, Farben, Typografie, Effekte, Anti-Patterns und Prüfpunkte ab. Die Datenbank unterscheidet aktive, ergänzende und veraltete Stile; 22 Tech-Stacks erhalten eigene, teils versionsabhängige Hinweise.

Design-Systeme können als `MASTER.md` mit seitenspezifischen Overrides gespeichert werden. Für bestehende React-Apps dokumentiert das Repo jetzt zuerst die Untersuchung von Stack, Komponenten und Tokens, danach eine schrittweise Migration im vorhandenen Styling-System. Die Suchergebnisse ändern eine App nicht automatisch. Brand-Erkennung berücksichtigt zusätzliche CSS-Dateinamen; aktuelle Generator-Fixes verhindern beschädigte SVGs, falsche Bildendungen und verlorene Fehlerstatus.

Die Quelle liegt unter `src/ui-ux-pro-max/`, der CLI-Installer erzeugt Hostdateien. Amazon Q Developer und OpenClaw sind neue Ziele; GitHub Copilot erhält nun einen Agent Skill unter `.github/skills` statt nur Slash-Command-Prompts. Amazon Q lädt eine Regeldatei, die auf Daten und Scripts verweist. Python-Suchscripts verwenden die Standardbibliothek und arbeiten laut Dokumentation ohne Netzwerk. Die Basis ist MIT-lizenziert, daneben gibt es ein kostenpflichtiges Premium-Angebot für Branding und Assets. Relevant als strukturierte Alternative zu rein stilistischen Prompts; Regeln, Lizenzen und Installationswirkungen vor Übernahme prüfen, konkrete Barrierefreiheit bleibt an der erzeugten Oberfläche zu testen.

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

## NVIDIA/skillevaluator

- **URL:** https://github.com/NVIDIA/SkillEvaluator
- **Stars:** ⭐ 587
- **Heruntergeladen:** 2026-10-11
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 455 · **Größe:** 12M
- **Struktur:** Python-CLI und Evaluationspipeline in `src/skillevaluator/`, Dokumentation in `docs/`, Tests in `tests/` und CI-Prüfwerkzeuge in `scripts/`; Referenz-Skills unter `src/skillevaluator/tier3/reference_skills/`, kein installierbares Skill-Pack <!-- manual -->

NVIDIAs SkillEvaluator ist ein experimentelles Framework zur Bewertung von Agent-Skills mit drei unabhängig ausführbaren Stufen: Tier 1 prüft Format, Qualität, Abhängigkeiten und Sicherheit, Tier 2 semantische Überlappung, Tier 3 den Leistungsbeitrag in paarweisen Agentenläufen mit und ohne Skill. Version 0.6.0 nutzt Python 3.12/3.13, Harbor und standardmäßig Docker; Codex, Claude Code und OpenCode sind unterstützte Agenten. Zusätzliche Scanner wie SkillSpector, Semgrep und Gitleaks erweitern die Sicherheitsabdeckung. Ein optionales Dashboard vergleicht gespeicherte Berichte nach Skill, Modell und Harness sowie nach Score, Tokens, Zeit und vorhandenen Kostenmessungen. Fehlende Messungen bleiben unbekannt.

Neu stehen eigene Execution-Backends sowie GKE, Kata, Runta und Mosaic zur Verfügung, mit begrenzter Weitergabe von Konfiguration und Credentials. Aussagekräftiger Skill Lift erfordert vollständige Versuchspaare, kompatible Metrik-Policies und passende Judge-Modelle; positive Trials ohne Skill-Aktivierung gelten als unentscheidbar. Veröffentlichungsbelege binden Tier-Ausführungen an Source-Digest und Run-ID und verlangen vollständige Entscheidungsevidenz; die bloße Existenz eines Reports genügt nicht. Das ist eine konkrete Referenz für reproduzierbare Skill-Evals und vorsichtige Qualitäts-Gates. Aufgaben und Rubriken bestimmen die Aussagekraft; automatisch erzeugte Starterfälle haben begrenzte Abdeckung. `validate` startet standardmäßig auch Live-Evaluation und kann Modell-/Sandbox-Kosten auslösen. Provider-Aufrufe können Inhalte übertragen; das Projekt bleibt eine lokale Analyse-Referenz ohne Installation oder Ausführung fremder Scripts. Lizenz laut Repository: Apache-2.0, Drittanbieterhinweise separat.

---

## NVIDIA/SkillSpector

- **URL:** https://github.com/NVIDIA/SkillSpector
- **Stars:** ⭐ 20.827
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 461 · **Größe:** 9,2M
- **Struktur:** Python-Scanner in `src/`, Regeln und Tests in `tests/`, Integrationen und Batch-Tools unter `extensions/` und `contrib/`; kein Skill-Paket <!-- manual -->

SkillSpector ist ein Apache-2.0-lizenzierter Security-Scanner für Agent-Skills, MCPs und verwandte Konfigurationen. Er untersucht lokale Dateien/Verzeichnisse, Git-Repos, URLs und ZIPs statisch und optional semantisch mit LLMs. Die README nennt 71 Muster in 17 Kategorien, darunter Prompt Injection, Exfiltration, Supply Chain, Memory Poisoning, Tool Misuse und MCP-Berechtigungen. Ergebnisse erscheinen als Terminaltext, JSON, Markdown oder SARIF; separate Gates können aktive Findings, unvollständige Prüfung und Mindestabdeckung steuern. Exit 0 allein umfasst auch `CAUTION`.

Die als 2.12.0-Unreleased geführte Entwicklung stärkt das Inspection Ledger, verschachtelte Artefakte, lexikalische Python-/Taint-Analyse und ressourcenbegrenzte Verarbeitung. Deterministische Findings bleiben auch bei LLM-Widerspruch erhalten; exakte Baseline-Fingerprints binden an Quellinhalt und Scanner-Version. Explizite Dateiausschlüsse verhindern eine vollständige SAFE-Einstufung. DSSE-/Signaturbundles werden auf Inhalte untersucht, ohne Signatur oder Identität zu verifizieren.

Provider umfassen HTTP-APIs, lokale Endpunkte und begrenzte CLI-Integrationen; Gemini auf Google Cloud kommt hinzu. `codex_cli` ist wegen möglicher Hostdatei-Lesezugriffe deaktiviert, `opencode_cli` akzeptiert exakt 1.18.33. Neuere OpenAI-/Claude-Modelle bleiben ausdrücklich Opt-in. LLM-Prüfung sendet Dateiinhalte an den gewählten Provider; OSV-Abfragen übermitteln Paketkoordinaten auch bei `--no-llm`. Atomische Report-/Baseline-Dateiausgabe benötigt POSIX-No-follow-Operationen und steht unter Windows nicht bereit; stdout bleibt verfügbar. Referenz für vorgeschaltete Skill-Prüfung, kein Sandbox- oder Sicherheitsnachweis. Findings, Abdeckung, Baselines und übertragene Daten müssen vor produktiver Übernahme geprüft werden.

---

## obra/superpowers

- **URL:** https://github.com/obra/superpowers
- **Stars:** ⭐ 303.183
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 231 · **Größe:** 1,5M
- **Struktur:** 15× SKILL.md · Ordner: skills, hooks, references · Spiegelordner: .agents, .opencode (generiert)

Superpowers ist Jesse Vincents vollständige Entwicklungs-Methodik aus komponierbaren Agent-Skills. Der Kernablauf verbindet Brainstorming und Designfreigabe mit isolierter Git-Arbeit, kleinteiliger Planung, TDD, Code-Review und Branch-Abschluss. Umsetzung erfolgt entweder mit frischen Subagents pro Task und Zwischenreviews oder direkt in der Hauptsession mit einem abschließenden unabhängigen Branch-Review. Skills triggern auf passenden Aufgaben und schreiben damit einen deutlich stärkeren Prozess vor als lose Prompt-Sammlungen.

Version 7.0.1 überarbeitet vor allem Brainstorming: zuerst vorhandene Projektunterlagen lesen, bereits beantwortete Fragen vermeiden, verbleibende Entscheidungen konkret abfragen und Ansätze sowie Design vor der Umsetzung abstimmen. Ein frischer Builder-Check prüft, welche Informationen zur Umsetzung noch fehlen. Lange Skills laden Fix-Schleife, Preflight, Wiederaufnahme und Abschlussreview aus Referenzen nach. Ein Größencheck hält `SKILL.md` unter 20.000 Bytes, weil die dokumentierte Claude-Code-Compaction spätere Regeln abschneiden konnte.

Unterstützte Hosts umfassen Claude Code, Codex, Cursor, Antigravity, Gemini, Copilot, OpenCode, Pi und weitere. Aktuelle Fixes betreffen native Antigravity-Pakete, Windows-Git-Bash-Erkennung und Hook-Exitcodes; im Repo platzierte `bash`-/`where`-Dateien sollen nicht ausgeführt werden. `diagnosing-superpowers` untersucht Session-Transkripte mit Zeilenbelegen. Beiträge verlangen eine menschlich verfasste Zusammenfassung; fremde Issues dürfen nicht ungefragt per Agent-PR bearbeitet werden. MIT-lizenzierte Referenz für disziplinierte Agentenabläufe und überprüfbare Reviews. Der optionale Visual Companion lädt standardmäßig ein versionsmarkiertes Herstellerlogo mit abschaltbarer Telemetrie; Installation und produktive Übernahme bleiben getrennt zu prüfen.

---

## oh-my-mermaid/oh-my-mermaid

- **URL:** https://github.com/oh-my-mermaid/oh-my-mermaid
- **Stars:** ⭐ 3.188
- **Heruntergeladen:** 2026-10-10
- **Zuletzt aktualisiert:** 2026-10-10
- **Dateien:** 212 · **Größe:** 2,0M
- **Struktur:** TypeScript-CLI unter `src/`, HTTP-Viewer unter `src/server/`, drei Skills unter `skills/`, Architekturbeispiele unter `.omm/`, Vitest-Dateien unter `src/__tests__/` <!-- manual -->

Oh-my-mermaid erstellt navigierbare Architekturdokumentation für Codebasen, die mit Coding-Agenten analysiert werden. Der Scan-Skill liest Manifeste, Einstiegspunkte, Routen, Services und Integrationen und wählt passende Perspektiven: etwa Gesamtarchitektur, Request-Lifecycle, Datenfluss oder CLI-Befehle. Komplexe Knoten erhalten rekursiv eigene Unteransichten; einfache bleiben Blätter. Knoten-IDs entsprechen Verzeichnisnamen, Beschriftungen nennen konkrete Codepfade und Kanten erklären die Verbindung. Unter `.omm/` liegen Mermaid-Diagramme und Markdown-Dateien für Beschreibung, Kontext, Einschränkungen, Bedenken, Aufgaben und Notizen. Die Ablage bleibt unabhängig vom Viewer lesbar.

Technisch ist Version 0.2.0 eine TypeScript-CLI für Node.js ab 18 mit `yaml` als Laufzeitabhängigkeit, einem HTTP-Viewer und drei Skills für Scan, Anzeige und Cloud-Push. Plattformadapter unterstützen Claude Code, Codex, Cursor, OpenClaw und Antigravity. Acht Vitest-Dateien prüfen unter anderem Ablage, Diagrammregeln und Cloud-Pfade; sie messen keine Genauigkeit der KI-generierten Architektur. Der letzte Commit am 07.04.2026 verbessert die Windows-Befehlserkennung. MIT-Lizenz vorhanden.

Relevant für Onboarding, Architekturkommunikation und gezielte Detailanalysen. Empfehlung: zunächst nur Referenz; [Wissensaufarbeitung](../80_Knowledge/Sources/2026-10-10-repo-oh-my-mermaid-architektur.md) mit verifizierten Dateibelegen vorhanden. Vor einer Installation sind globale Skill-Verknüpfungen zu prüfen. Der Viewer bindet nicht ausdrücklich an Loopback, erlaubt CORS `*` und lädt CDN-Scripts, darunter eine ungepinnte `marked`-Version. Cloud-Push überträgt sämtliche `.omm/`-Dateien. Weder Scan-Skill noch CLI wurden ausgeführt oder installiert; Cloud- und Laufzeitverhalten bleiben ungeprüft.

---

## open-gsd/gsd-core

- **URL:** https://github.com/open-gsd/gsd-core
- **Stars:** ⭐ 10.759
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 4.162 · **Größe:** 65M
- **Struktur:** 144× SKILL.md · Ordner: skills, agents, commands, hooks, references · Spiegelordner: .kilo, .opencode (generiert)

GSD Core („Git. Ship. Done.“) ist ein MIT-lizenziertes Context-Engineering- und Spec-driven-Development-Framework für viele Coding-Harnesses. Sein Ablauf Discuss → Plan → Execute → Verify → Ship verlagert schwere Recherche und Umsetzung in frische Subagent-Kontexte; `STATE.md`, `CONTEXT.md` und weitere Planungsartefakte erhalten Entscheidungen über Sessions hinweg. Capabilities, Predicate-Gates, externe Reviewer-Lanes, Worktrees und optional kompakte Workflow-Spines erweitern diesen Kern. Relevant ist vor allem die Verbindung von persistentem Projektzustand mit expliziten Verifikations- und Abschlussbedingungen.

Release 1.18.0 und die nachfolgenden Änderungen bauen auf der OpenCode-2.x-Unterstützung aus 1.17.0 auf: Plugin-Einstiege, Tool-Guards, JSONC-sichere Konfigurationspflege, vollständige Deinstallation und Statusline wurden angepasst. OpenCode 1.x ist als auslaufende Bugfix-Linie dokumentiert. Pi erhält ein natives Paket, Rollen-Dispatch über `gsd_dispatch` sowie Hook-/Lifecycle-Anbindung. Ein interner `StateWriteIntent`-Executor prüft deklarierte Schreibgrenzen; seine Existenz bedeutet noch keine vollständige Umstellung aller State-Schreibpfade. Mehrdeutige Artifact-Frontmatter-Gates blockieren mit einer Kandidatenliste statt einen Treffer zufällig zu wählen.

Weitere Fixes begrenzen das Lesen fehlerhafter Skill-Dateien, verhindern Shell-Auswertung von Command-Argumenten und schützen Secrets bei Brave-Redirects und command-wertigem `git -c`. Der Umfang bringt weiterhin Installations-, Konfigurations- und Governance-Aufwand mit sich. Cross-Runtime-Kompatibilität hängt vom Installer ab; bloßes Kopieren einzelner Agent-Dateien ist kein gleichwertiger Installationsweg. Hier bleibt GSD Analyse-Referenz ohne Aktivierung.

---

## openai/codex

- **URL:** https://github.com/openai/codex
- **Stars:** ⭐ 130.325
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 9.437 · **Größe:** 92M
- **Struktur:** Monorepo mit Rust-Kernimplementierung (`codex-rs`, ~109 Crates: Core-Agent-Loop, Sandboxing, MCP-Server, TUI, App-Server), einem dünnen npm-Wrapper (`codex-cli`) sowie separaten Python- und TypeScript-SDKs (`sdk/`), zusätzlich Bazel- und Nix-Build-Tooling — kein Skill-/Plugin-Paket im Claude-Code-Sinne. <!-- manual -->

Codex CLI ist OpenAIs lokal laufender Coding-Agent als Apache-2.0-lizenzierter Rust-Monorepo. `codex-rs/` enthält Agent-Loop, TUI, App-Server, MCP-Anbindung, Skills-/Hooks-/Plugin-Systeme sowie Linux-, macOS- und Windows-Sandboxing. npm-Wrapper, Release-Binaries und SDKs ergänzen die Distribution; Bazel-/Nix-Tooling zeigt den erheblichen Build- und Plattformumfang. Anmeldung erfolgt über einen unterstützten ChatGPT-Plan oder entsprechend konfigurierte API-Zugänge. Das Repo ist deshalb eine Architekturquelle für ein vollständiges Agentenprodukt, nicht bloß eine Sammlung wiederverwendbarer Prompts.

Die aktuelle Commit-Spanne erweitert Remote-Ausführung mit Credential-Providern, Request-bezogenen OAuth-Daten, Session-Lifecycle-APIs und erneuerbaren Zugangsdaten. Windows erhält Proxy-Authentifizierungshelfer; der Bedrock-Setup-Wizard ist im Source standardmäßig aktiviert. Guardian-V2-Arbeiten betreffen Vergleich von Review-Entscheidungen, Evidenzerhalt und Laufzeitmessung. Lokale Agent-Message-Boards erhalten getrennte Storage-Namespaces und Nachrichten Lifecycle-Hooks; Cloud-Skills und Plugins nutzen eingefrorene Snapshots beziehungsweise aktualisierte Kataloge nach Auth-Wechseln. Weitere Schutzmaßnahmen begrenzen Credential-Substitution auf vertrauenswürdige Ziele und verweigern unsichere Executable-/Windows-Provisioning-Pfade.

Praktisch interessant sind die Grenzen zwischen Agent-Ausführung, Freigabeprüfung, Sandbox, Remote-Transport und Host-App. Die Commit-Historie enthält auch experimentelle oder gestaffelt aktivierte Funktionen; sie belegt weder Verfügbarkeit im eigenen Konto noch Verhalten jeder ausgelieferten Desktop-Version. Große, OpenAI-spezifische Abhängigkeiten und Cloud-/Kontointegration erschweren isolierte Wiederverwendung. Vor Übernahme einzelner Komponenten deren Schnittstellen, Lizenzhinweise und Laufzeitbedingungen separat prüfen.

---

## OthmanAdi/planning-with-files

- **URL:** https://github.com/OthmanAdi/planning-with-files
- **Stars:** ⭐ 27.569
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 759 · **Größe:** 30M
- **Struktur:** 6× SKILL.md · Ordner: skills, commands, hooks · Spiegelordner: .agents, .codebuddy, .codex, .continue, … (+9) (generiert)

„Planning with Files“ hält Aufgabenwissen in drei Markdown-Dateien fest: `task_plan.md` für Plan und Fortschritt, `findings.md` für Erkenntnisse und `progress.md` für das Session-Log. Hooks laden den ausgewählten Plan erneut, erinnern an Statuspflege und prüfen den Abschluss; das Muster richtet sich gegen Kontextverlust durch Kompaktierung, `/clear` oder Abstürze. Version 3.25.0 unterstützt laut Projekt über 60 Agenten mit je nach Host unterschiedlicher Integration. Native Plugins gibt es für Claude Code, Codex CLI, Qoder CLI, Pi, Hermes, OpenCode und DeepSeek Harness; die reine Skill-Installation liefert nicht überall dieselben Commands und Hooks. `/plan-doctor` prüft Auflösung und Installationsoberflächen.

Neu bindet Hermes benannte Pläne pro Gespräch, persistent über Backend-Neustarts und isoliert zwischen parallelen Sessions. Qoder CLI bekommt sieben Hooks und ein optionales Completion-Gate, benötigt Bash und Python ab 3.10; dessen IDE-Verhalten ist nicht bestätigt. Claude Code und Pi unterdrücken unveränderte Plan-Wiederholungen nach erfolgreicher Kontextinjektion, führen Zulassungs- und Attestierungsprüfungen aber weiterhin aus. Pi attestiert den tatsächlich injizierten Snapshot; selbst Fortschrittsänderungen erfordern eine explizite erneute Attestierung. Automatische Recovery liest nur Projektdateien, Session-Records brauchen einen ausdrücklich gewählten Catchup-Modus. Ein öffentliches File-only-Recovery-Fixture trennt Baseline, Replay und unklare Ergebnisse. Relevant als konkretes Planpersistenz-Muster und als Referenz für sitzungsgebundene Kontextzufuhr; historische Erfolgszahlen des Autors sind keine eigene Wirkungsmessung.

---

## paperclipai/paperclip

- **URL:** https://github.com/paperclipai/paperclip
- **Stars:** ⭐ 105.715
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 11.343 · **Größe:** 167M
- **Struktur:** Node.js-/React-Monorepo in `packages/` mit CLI, Server und UI; Agenten-/Skill-Integrationen in `.agents/`, `.claude/` und `plugins/`; Betriebsartefakte in `docker/`, `evals/` und `docs/` <!-- manual -->

Paperclip ist eine MIT-lizenzierte, selbst hostbare Control Plane für Teams aus Menschen und AI-Agenten. Node.js-Server und React-Oberfläche verbinden Organisationsziele, Rollen, Aufgaben, Freigaben, Projekte und Arbeitsverläufe mit Budgetkontrolle und Audit-Log. Agents unterschiedlicher Harnesses bearbeiten Arbeit über Heartbeats, Nachrichten und geplante Routinen. Skills, persönliche oder gemeinsame App-Verbindungen und projektbezogene Workspaces liefern den jeweiligen Ausführungskontext. Das System adressiert den Betrieb einer Agentenorganisation statt nur einzelne Coding-Sessions.

Die aktuelle Entwicklung rückt Paperclip Runner als gemeinsame Ausführungsschicht in den Mittelpunkt. Neue Pi-/OpenCode-Agenten und qualifizierte Claude-Ziele nutzen ihn standardmäßig; bestehende Claude-/Codex-Agenten bekommen einen Umstieg angeboten. Gemeinsame Verträge regeln Launch-Vorbereitung, Resume, Workspace-Zulassung und sitzungslokalen MCP-Transport. Cases ergänzen persistente Workflows mit Handoffs zwischen Agents innerhalb derselben Aufgabe und wiederverwendbaren Prompt-Abläufen. Neue Connections umfassen Braintrust, Ditto, Google Workspace und einen experimentellen Notebook-MCP-Zugang. Änderungen an Connector-Rechten oder Tooldefinitionen können Runtimes invalidieren; Recovery-Arbeit schützt menschliche Stop-Autorität und Aufgabenfortsetzungen.

Relevant als umfangreiche Referenz für Zielvererbung, Runtime-Orchestrierung, Budgetdurchsetzung und menschliche Eingriffsrechte. Dokumentierte Isolation, atomare Checkouts und Evals sind Architektur-/Implementierungsmerkmale, kein Nachweis eigener sicherer Betriebsfähigkeit. Secrets, externe Verbindungen, automatische Ausführung, Budgets und Mehrfirmenzugriffe verlangen vor einer Einführung eine gesonderte Architektur- und Freigabeentscheidung. Es ersetzt weder Code-Review noch die Auswahl eines passenden Agenten-Harnesses.

---

## pbakaus/impeccable

- **URL:** https://github.com/pbakaus/impeccable
- **Stars:** ⭐ 84.473
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 4.125 · **Größe:** 78M
- **Struktur:** Quelle in `skill/` (`SKILL.src.md` + `reference/<command>.md`), generierte Provider-Ausgaben in `plugin/skills/` bzw. `.claude/skills/`, `.cursor/skills/` usw. <!-- manual -->

Impeccable von Paul Bakaus bündelt Design-Guidance für Coding-Agenten als einen Skill mit 24 Unterbefehlen, Live-Browser-Iteration und laut README 61 deterministischen Detektor-Regeln. `init` hält dauerhafte Produktfakten in `PRODUCT.md`; visuelle Richtung und Oberflächenentscheidungen liegen getrennt in `DESIGN.md` beziehungsweise `.impeccable/`. Commands wie `craft`, `polish`, `audit`, `critique`, `typeset`, `harden` und `live` verbinden gestalterische Planung, Komponentenreview und Umsetzung. Der Detektor prüft typische AI-Generik sowie konkrete Layout-, Text-, Kontrast- und Bedienprobleme ohne LLM.

Version 4.7.0 mit Engine 0.1.16 verbessert insbesondere gerenderte Textgeometrie, verdeckte Inhalte, Kontrastflächen und Bildsyntax verschiedener Frameworks. `detect --github` liefert Actions-Annotationen, `--list-rules` den Regelkatalog und `--cdp` die Prüfung laufender Desktop-Apps mit DevTools-Port. Operate-/Read-Flächen werden code-first gebaut; Landing-/Showcase-Flächen können weiterhin über Comps beginnen. Native Edit-Hooks und Live-/Review-Oberflächen erhalten Windows-, Codex- und Browserkorrekturen.

Der lokale Detektor ist von der Designauswahl zu unterscheiden: Neue Designrunden fragen die Roll-API bei impeccable.style nach visuellen Welten. Standardmäßig werden anonyme Roll-/Choice-Daten erfasst; CLI-, Projekt- und Umgebungs-Opt-outs unterbinden diese Erfassung, nicht den funktionalen API-Aufruf. Git-Artefakte speichern gesalzene Seed-Referenzen statt Roll-Keys. Apache-2.0-lizenziert und als Referenz für überprüfbare Design-Guidance interessant. Ein fehlerfreier Detektor-Lauf ersetzt keine visuelle oder Accessibility-Abnahme, und Hooks/Binary-Downloads benötigen vor Übernahme eine eigene Prüfung.

---

## petergyang/human-review

- **URL:** https://github.com/petergyang/human-review
- **Stars:** ⭐ 1.403
- **Heruntergeladen:** 2026-09-14
- **Zuletzt aktualisiert:** 2026-09-17
- **Dateien:** 52 · **Größe:** 1,8M
- **Struktur:** Node-CLI statt Skill-Paket: `src/` enthält CLI, lokalen Server, Browser-Client, Markdown-Renderer und Setup, dazu `src/SKILL.md` als Agent-Anleitung; 20 Test-Dateien in `test/`; `design-ref/` und `spec.html` als Entwurfsmaterial <!-- manual -->

Lokales Node-Werkzeug mit mitgeliefertem Agent-Skill von Peter Yang, das den Umweg über getippte Änderungswünsche ersetzt: Statt im Chat zu beschreiben, welcher Satz im dritten Absatz anders lauten soll, öffnet der Agent die Datei im Browser. Dort lässt sich Text direkt bearbeiten, Formatierung, Listen und Links setzen, Bilder skalieren und verschieben, ganze Blöcke umsortieren und Elemente löschen; Kommentare hängen punktgenau an der markierten Stelle oder am angeklickten Element. Ein Klick auf Send schickt sämtliche Edits und Kommentare als ein Bündel zurück an den Agenten. Unterstützt werden HTML-Dateien, gerenderte Markdown-Dateien (die Quelldatei bleibt unangetastet, der Agent überträgt die Änderungen selbst) und laufende localhost-Seiten. Das eigentliche Muster steckt im Wartepunkt: `human-review poll` blockiert, bis der Mensch sendet, und weckt den Agenten dann mit dem gesamten Batch — in Claude Code als Hintergrundprozess, der den Zug beendet und später aufgeweckt wird. Damit ist menschliches Review ein benannter Schritt in der Agentenschleife statt einer Unterbrechung. Alles läuft lokal, ohne Account, Cloud oder API-Key; 19 Test-Dateien decken unter anderem Sicherheit, Feedback-Integrität und Frame-Policy ab. Aktiv gepflegt (Version 0.8.1, 52 Commits, zuletzt 04.09.2026), MIT-lizenziert. Vor einer Übernahme zu prüfen: `npx -y human-review setup --global` schreibt den Skill in globale Agenten-Konfigurationen, und HTML-Edits speichern direkt in die Datei.

---

## petergyang/no-ai-slop

- **URL:** https://github.com/petergyang/no-ai-slop
- **Stars:** ⭐ 12.660
- **Heruntergeladen:** 2026-09-14
- **Zuletzt aktualisiert:** 2026-09-14
- **Dateien:** 14 · **Größe:** 257K
- **Struktur:** 1× SKILL.md · Ordner: skills, agents

Ein einzelner, eng gefasster Schreib-Skill von Peter Yang gegen die typischen Sprachmuster von KI-Texten: binäre Kontraste („It’s not X. It’s Y.“), Räusper-Einstiege, Pseudo-Einsichten („What nobody tells you“), Doppelpunkt-Enthüllungen, dramatische Satzfragmente, Bedeutungs-Aufplusterung, vage Belege („experts agree“), Synonym-Rotation und tiefsinnig gemeinte Schlusssätze — über 20 benannte Muster. Die Leitlinie ist dabei ausdrücklich nicht Glättung: Der Skill soll Vokabular, Rhythmus, Härte, Humor, Unsicherheit und Abschweifungen der schreibenden Person erhalten und nur die kleinste wirksame Änderung vornehmen. Zwei getrennte Modi machen ihn brauchbar: Edit schreibt um und listet die Änderungen, Detect benennt lediglich jedes gefundene Muster mit Zitat und kurzem Fix, ohne den Text anzufassen. Die Begründung dafür ist als Haltung interessant — KI-Detektoren raten, benannte Muster dagegen sind nachprüfbare Belege; der Skill urteilt deshalb nie darüber, ob ein Text von einer KI stammt. Eine eigene `eval.md` hält die Selbstprüfung nach jeder Bearbeitung als Pass/Fail-Liste fest und ist unabhängig vom Thema als Muster für überprüfbare Skills lesenswert. MIT-lizenziert, zusätzlich als ChatGPT-/Codex-Plugin paketiert (`.codex-plugin/plugin.json`, gebaut über `scripts/build_plugin.py`). Deutlicher Eigenwerbungsbezug zu Behind the Craft und Newsletter.

---

## router-for-me/CLIProxyAPI

- **URL:** https://github.com/router-for-me/CLIProxyAPI
- **Stars:** ⭐ 55.917
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 2.062 · **Größe:** 34M
- **Struktur:** Go-Server in `cmd/` und `internal/`, SDK und Beispiele in `sdk/` und `examples/`, Betriebs-/API-Dokumentation unter `docs/`; kein Skill-Paket <!-- manual -->

CLIProxyAPI ist ein MIT-lizenzierter Go-Proxy für die Übersetzung zwischen OpenAI-, Responses-, Claude-, Gemini- und weiteren CLI-/SDK-Protokollen. Account-Pools, OAuth-Anmeldungen, API-Keys, Streaming, Tool Calling und konfigurierbare Upstreams ermöglichen heterogene Clients und Provider hinter einer gemeinsamen Schnittstelle. Management-API, Pluginhost und Go-SDK erweitern die Einbettung; die README beschreibt zusätzlich ein großes Umfeld kommerzieller Relays und Community-Werkzeuge. Verfügbarkeit einzelner Modelle bleibt vom Kanal und jeweiligen Account abhängig.

Die aktuelle Commit-Spanne erweitert Credential- und SIWC-Bindungsverträge um einen lesenden Statusendpunkt und Schutz gegen zwischenzeitlich ersetzte Accounts. Guardian-Reviews übernehmen Eltern-Credentials, Codex-Alpha-Search verwendet die ursprünglichen OAuth-Zugangsdaten. Pluginhost-Abfragen ermitteln Modelle pro Credential; Vertex erhält Routing-Optionen je Modell und Account, und Cluster-Rebalance-Handoffs werden vorbereitet. Übersetzer bewahren explizites `parallel_tool_calls=false`, Claude-Effort-/Stop-Gründe, Gemini-Thought-Signatures und Antigravity-Tool-Replay. Request-bezogene Metadaten-Caches vermeiden wiederholte Tool-Scans; einzelne Credential-gebundene Caches verbessern die Trennung von Aufrufern.

Interessant als Analysequelle für Provider-Abstraktion und Protokolladapter. Zugleich verarbeitet der Proxy hochsensible Tokens, Zugangsdaten und Requests zentral; funktionierende Übersetzung oder eine MIT-Lizenz belegen keine zulässige Account-Nutzung oder sichere Installation. Secret-Speicherung, Account-Isolation, Netzwerk-Exposition, Logging, Datenflüsse und Providerbedingungen müssen vor jedem produktiven Einsatz gesondert geprüft werden. Hier ausschließlich Referenzbestand; keine Installation, Anmeldung oder Aktivierung.

---

## rtk-ai/rtk

- **URL:** https://github.com/rtk-ai/rtk
- **Stars:** ⭐ 84.211
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 814 · **Größe:** 9,3M
- **Struktur:** Rust-CLI in `src/`; Integrationen als `hooks/`, `.claude/` und `openclaw/`; 12× SKILL.md für Agenten-Anleitungen <!-- manual -->

RTK („Rust Token Killer“) verdichtet Terminalausgaben für Coding Agents: Hooks können Git-, Such-, Test-, Build-, Cloud- und Containerbefehle auf kompakte RTK-Ausgaben umschreiben. Filterung, Gruppierung, Kürzung und Deduplizierung sollen den gelesenen Kontext reduzieren. Eingebaute Read-/Grep-/Glob-Tools des Hosts passieren den Bash-Hook nicht. Die Integrationen unterscheiden sich deshalb in Reichweite und Durchsetzung. Gemessene Byte-Reduktion ist zudem weder exakte Tokenzählung noch gleich hohe Einsparung der gesamten Modellrechnung.

Der neue Aufbau ergänzt eine über `pipeline.toml` konfigurierbare Engine mit Regeln, Bedingungen, Tasks und Methoden. Ohne eigene Pipeline bleibt der bisherige Standard aktiv. Ein separat installiertes `rtk-proxy` verarbeitet optional Provider-API-Verkehr; `rtk claude` startet den Daemon und leitet Claude darüber. Andere Harnesses werden nicht stillschweigend als nachgewiesen proxied ausgegeben. Dieser Pfad erweitert die Vertrauensgrenze um API-Payloads und Provider-Credentials. Permission-Regeln, Hook-Integrität, unlesbare Settings, JSON-Schlüsselausgabe und Recall-Schlüssel wurden gehärtet.

Die Lizenz ist komponentenspezifisch: CLI-/Hook-Kern und `rtk-oss` nennen Apache-2.0; die im vollständigen `rtk` eingebundene Engine und der separate Proxy BUSL-1.1. Beide Editionen installieren denselben Binärnamen und können nicht gleichzeitig installiert werden. Die jeweiligen Lizenzdateien und Additional Use Grants sind vor Übernahme separat zu prüfen. Relevant als Referenz für gezielte Kontextverdichtung, transparente Messgrenzen und konfigurierbare Agenten-I/O-Pipelines. Globale Hooks, lokal aufbewahrte Roh-Ausgaben und die standardmäßig deaktivierte Telemetrie verdienen bewusste Konfiguration; hier wurde nichts installiert.

---

## shadcn-ui/lint

- **URL:** https://github.com/shadcn-ui/lint
- **Stars:** ⭐ 3.245
- **Heruntergeladen:** 2026-10-11
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 403 · **Größe:** 1,7M
- **Struktur:** Plugin, Regeln und Projektmodell in `packages/lint/src/`, Agent-Evals in `packages/evals/`, Dokumentation in `docs/` und Setup-Anleitung in `SETUP.md` <!-- manual -->

`@shadcn/lint` ist ein programmierbarer Linter für Tailwind-v4-Designsysteme und damit ein ausführbares Entwicklungswerkzeug, kein Skill-Pack. Er richtet sich an Teams, die UI-Code durch Coding Agents erstellen lassen und vorhandene Komponenten, Varianten und Theme-Tokens konsistent halten wollen. Regeln erfassen unter anderem unerlaubtes Restyling, rohe Farben, beliebige Werte, Inline-Styles, unbekannte Klassen und nicht statisch auswertbare Klassen. Konfigurierbare Komponentenverträge und Fehlermeldungen erklären, welche vorhandene Variante oder welcher Theme-Wert stattdessen verwendet werden soll. shadcn/ui ist dafür nicht erforderlich. Gute Einstiegspunkte sind `README.md`, `SETUP.md`, `docs/design-systems.md` und `docs/rules.md`; die Implementierung liegt unter `packages/lint/src/`. Das Paket unterstützt ESLint und Oxlint sowie React, Vue und Svelte. Voraussetzung ist Node.js ab 20.19; bei Vue und Svelte prüft Oxlint nur Script-Blöcke, weshalb die Framework-Unterstützung nicht überall gleich umfassend ist. Die Root-Lizenz ist MIT. Sichtbare Paketabhängigkeiten sind `@eslint/core`, `cn` und optional `oxc-parser`; Build-, Test- und Pack-Scripts erzeugen beziehungsweise verändern lokale Dateien. Die separat enthaltenen Agent-Evals unter `packages/evals/` rufen angemeldete Modell-CLIs auf und verursachen laut Dokumentation Modellkosten. Veröffentlichte Erfolgs- und Kostenwerte ersetzen keine Prüfung im eigenen Projekt. Empfehlung: ausschließlich lokale Referenz für überprüfbare Designsystem-Regeln und hilfreiche Agent-Diagnosen; keine Installation oder Integration wurde vorgenommen.

---

## shadcn-ui/ui

- **URL:** https://github.com/shadcn-ui/ui
- **Stars:** ⭐ 126.156
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 6.404 · **Größe:** 50M
- **Struktur:** 2× SKILL.md · Ordner: skills, agents, commands, hooks, rules

Das offizielle shadcn/ui-Monorepo liefert CLI, Komponenten, Registries, Templates und die Agent-Skills `shadcn` sowie `migrate-radix-to-base`. Komponenten gelangen als veränderbarer Quellcode in Zielprojekte. Der projektbewusste `shadcn`-Skill liest `components.json`, erkennt Framework, Tailwind-Version, Aliase, Icons und Primitive-Base, sucht vorhandene Bausteine und bevorzugt Komposition. Regeln betreffen semantische Farben, Layout mit `gap`, zugängliche Overlay-Titel, Formularstruktur und vorsichtige Updates.

Der neue Designsystem-Workflow überträgt `DESIGN.md` oder eine Brand-Vorgabe auf Theme und Komponenten. Eine Showcase-Seite mit Zustandsmatrix, fixierbaren Vorschauzuständen, Kontrast- und Coverage-Helfern macht die Umsetzung prüfbar. Chat-/AI-Oberflächen erhalten unter anderem Trace- und Codeblock-Bausteine; `@shadcn/helpers` unterstützt deklarative Konversationsfixtures. Die eigenständige Registry-Implementierung entfernt ihre `ts-morph`-Abhängigkeit, berücksichtigt Style-Verfügbarkeit und behebt einen Windows-Absturz bei `pnpm dlx`; Community-Registries und private GitHub-Registries erweitern die Quellenwahl.

Relevant als offizielle Referenz und selektiv einsetzbarer Projekt-Skill für konsistente UI-Systeme. Das MIT-lizenzierte pnpm-/Turbo-Monorepo enthält Build-, Release- und Template-Sync-Scripts mit lokalen Schreibwirkungen; diese gehören nicht automatisch in dieses Mutter-Repo. Registry-Aufrufe können fremden Quellcode und Abhängigkeiten hinzufügen. Vor Integration sind Quelle, Dry-run/Diff und tatsächlich geänderte Dateien zu prüfen. Ein Showcase oder erfolgreicher Build ersetzt keine Funktions-, Accessibility- und Laufzeitabnahme. Der Skill ist kein pauschaler globaler Designstandard; hier wurde keine Installation oder Aktivierung vorgenommen.

---

## shadcn/improve

- **URL:** https://github.com/shadcn/improve
- **Stars:** ⭐ 9.240
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-09-17
- **Dateien:** 10 · **Größe:** 61K
- **Struktur:** 1× SKILL.md · Ordner: skills, references

Kleiner, fokussierter Agent-Skill von shadcn: auditiert eine beliebige Codebasis mit einem leistungsstarken (teuren) Modell und schreibt daraus präzise, in sich geschlossene Umsetzungspläne, die anschließend von günstigeren Modellen oder anderen Agenten ausgeführt werden können. Der Skill implementiert selbst nie Code – "der Plan ist das Produkt". Ablauf: Recon (Repo-Struktur, Build/Test/Lint-Befehle, vorhandene ADRs/PRDs erfassen) → Audit (parallele Subagenten über neun Kategorien: Korrektheit, Sicherheit, Performance, Testabdeckung, technische Schulden, Abhängigkeiten, Developer Experience, Doku, Richtung/Feature-Vorschläge) → Vet (Advisor prüft jeden gemeldeten Fund selbst nach, verwirft Fehlalarme) → Priorisierung (Impact/Aufwand) → Plan-Erstellung (eine Datei pro gewähltem Finding, mit exakten Dateipfaden, Code-Ausschnitten, Verifikationsbefehlen und klaren Grenzen). Kann Pläne auch direkt an einen günstigeren Executor-Agenten in einem isolierten Git-Worktree übergeben und dessen Ergebnis wie ein Tech Lead gegenprüfen, oder Pläne als GitHub Issues veröffentlichen. Relevant als schlankes Vorbild für Audit-zu-Plan-Workflows mit klarer Trennung zwischen teurem Planungsmodell und günstigem Ausführungsmodell.

---

## shanraisshan/claude-code-best-practice

- **URL:** https://github.com/shanraisshan/claude-code-best-practice
- **Stars:** ⭐ 67.886
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 454 · **Größe:** 75M
- **Struktur:** kein Skill-Paket, sondern Wissensbasis: `best-practice/`, `reports/`, `tips/` (die eigentlichen Inhalte); Demo-Setup in `.claude/agents/`, `.claude/commands/`, `.claude/skills/` <!-- manual -->

Eine umfangreiche kuratierte Wissensbasis zu Claude Code und Agentic Engineering: Subagenten, Commands, Skills, Hooks, MCP, Settings, Memory, Worktrees und konkrete Implementierungsbeispiele sind über Themenberichte, Best-Practice-Seiten und Community-Tipps erschlossen. Das mitgelieferte Wetterbeispiel demonstriert Command → Agent → Skill. Vergleichstabellen ordnen Entwicklungs-Workflows wie Superpowers, ECC, Matt-Pocock-Skills, gstack, Spec Kit, GSD und BMAD sowie reine Skill- und Agentensammlungen ein. Damit ist das Repo vor allem eine Landkarte und Lesereferenz, kein einheitliches installierbares Skill-Pack.

Die aktuelle Pflege reicht bis zu den Referenztabellen für Claude Code 2.1.306. Sie ergänzt `plugin-authoring`, präzisiert Command-Verhalten und führt Settings für Modellbeschränkungen, MCP-/Marketplace-Governance, Output-Limits, Plugin-/Skill-Sync und Workflow-Subagenten nach. Datierte Änderungsprotokolle unterscheiden erkannte Änderungen, ruhige Prüfläufe und zurückgestellte Auffälligkeiten. Viele Commits aktualisieren lediglich Sterne oder Zeitstempel; sie stehen nicht für neue Methoden.

Relevant als Meta-Referenz für die Auswahl passender Erweiterungsebenen und für konkrete Arbeitsweisen rund um Prompting, Planung, Kontext, CLAUDE.md und Reviews. Versions-, Provider- und Feature-Flag-Grenzen müssen gegen die aktuell verwendete Laufzeit geprüft werden. Community-Heuristiken, Erfolgsbehauptungen und Sternewerte sind keine eigenen Messungen oder Qualitätsnachweise. Beispiele und Demo-Konfigurationen dürfen nicht automatisch als globale Agentenregeln übernommen werden; die jeweilige Primärquelle und der konkrete Projektbedarf bleiben maßgeblich.

---

## teng-lin/notebooklm-py

- **URL:** https://github.com/teng-lin/notebooklm-py
- **Stars:** ⭐ 19.841
- **Heruntergeladen:** 2026-07-14
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 2.214 · **Größe:** 118M
- **Struktur:** 1× SKILL.md

`notebooklm-py` ist ein aktiver, MIT-lizenzierter Python-Client für Google NotebookLM (seit Juli 2026 von Google zu „Gemini Notebook“ umbenannt; gleiches Produkt, automatische Weiterleitungen, keine API-Änderung – das Paket behält seinen Namen) mit asynchroner API, CLI, optionalem MCP- und lokalem REST-Server sowie einem mitgelieferten Agent-Skill für Claude Code, Codex und kompatible Hosts. Er automatisiert Notebooks, Quellenimporte aus URLs, Dateien, YouTube, Google Drive und Google Play Books, quellengebundene Fragen mit Zitaten, Deep Research sowie die Erstellung und den Download von Audio-/Video-Überblicken, Slides, Infografiken, Reports, Quizzen, Flashcards, Datentabellen und Mindmaps. Release 0.8.5 ergänzt Python 3.15; weitere Commits bringen aufgeschobene Audio-Erstellung auf Web und Android, robustere Windows-Uploads und die Ablehnung abgemeldeter Headless-/CDP-Login-Sessions. Seit v0.8.2 gibt es neben dem Web-Backend einen nativen Android-Backend-Modus, der über kurzlebige OAuth-Bearer-Token direkt mit NotebookLMs mobiler gRPC-API spricht statt über Browser-Cookies – praktischer für CI/Container, aber mit einem dauerhaften Master-Token als deutlich mächtigerem Credential als eine Cookie-Momentaufnahme. Seit v0.8.3 (Android) und v0.8.4 (Web-Backend) bedienen MCP- und REST-Server mehrere Profile gleichzeitig (`--profiles work,personal`); Anfragen werden per Header `X-NotebookLM-Profile` bzw. Tool-Parameter geroutet, Profile mit gemeinsamer Session-Cookie werden abgelehnt. v0.8.4 bringt außerdem eine optionale URL-Wiederherstellung (`source add --fallback-fetch`, importiert fehlgeschlagene Webseiten als statischen Text) und Retry-Metadaten in MCP-Fehlern. Bulk-Operationen sind abgeschlossen: `notes.delete()`/MCP `studio_delete()` löschen mehrere Notizen in einem Request, `share_set_user()` vergibt 1–100 Editor-/Viewer-Rechte im Batch. Die 0.9-Entwicklung baut die öffentliche API um (typisierte `ClientConfig`, ein `outcomes`-Modul mit Commit-/Recovery-Status statt Silent-Retry, aggregierte Operation-Timeouts) und schließt eine Sicherheitslücke: MCP-Stdio-`source_add` mit Host-Pfaden ist standardmäßig verweigert und erfordert explizit konfigurierte erlaubte Wurzelverzeichnisse; die MCP-OAuth-Implementierung bindet Tokens fest an die jeweilige MCP-Resource. Die praktische Einschränkung bleibt wesentlich: Das Projekt nutzt nicht dokumentierte Google-APIs, kann deshalb ohne Vorwarnung brechen, Rate Limits oder Kontobeschränkungen auslösen und ist nicht mit Google verbunden. Sensible Google-Credentials – Session-Cookies wie auch der Master-Token – müssen lokal geschützt und aus Git ausgeschlossen bleiben. Daher zunächst nur als lokale Referenz nutzen; eine produktive Integration, insbesondere mit Firmenquellen, Remote-MCP oder geteilten Credentials, erfordert vorherige Sicherheits- und Datenschutzprüfung sowie Philipp-Freigabe.

---

## thedaviddias/Front-End-Checklist

- **URL:** https://github.com/thedaviddias/Front-End-Checklist
- **Stars:** ⭐ 74.540
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 1.978 · **Größe:** 12M
- **Struktur:** Umfangreiches pnpm/Turborepo-Monorepo mit Next.js-Web-App (`apps/web/`), MCP-Server, CLI und Regel-Content in `packages/`, plus separatem `skills/`-Ordner mit 390 generierten SKILL.md-Dateien (je mit `references/rule.md`) — kein reiner Checklisten-Dokumentenordner, sondern ein produktionsreifes Softwareprodukt mit Skill-Paket als Nebenprodukt. <!-- manual -->

Front-End-Checklist begann als reine Markdown-Checkliste für Frontend-Qualitätssicherung und hat sich zu einem vollständigen Monorepo-Produkt entwickelt: eine Next.js-Website (frontendchecklist.io), ein gehosteter MCP-Server mit elf Tools (u. a. search_rules, check_rule, fix_rule, explain_rule, audit_url), eine neue agentenorientierte CLI (`@frontendchecklist/cli`, arbeitet offline mit den Regeln) sowie 386 einzelne Regeln als MDX-Content (zuletzt ergänzt um eine Video-Optimierungsregel). Aus diesen Regeln werden automatisiert rund 390 Claude-Skills generiert (`skills/<name>/SKILL.md` plus `references/rule.md`), die jeweils Quick-Reference, Check-, Fix-, Explain- und Code-Review-Abschnitte enthalten und auf WCAG-, Performance-, SEO- und Security-Quellen verweisen. Der MCP-Server wurde zuletzt stark ausgebaut: Migration auf MCP SDK v2 (Protokoll 2026-07-28), „Skills over MCP“, eine MCP-Apps-Berichtsansicht, Veröffentlichung in der offiziellen MCP-Registry, ein Schutz gegen DNS-Rebinding in `audit_url`, ein Lint für Tool-Beschreibungen und eine Tool-Choice-Evaluation gegen die Anthropic-API. Technologisch handelt es sich um ein TypeScript-/pnpm-/Turborepo-Setup mit Prisma, Zod, Better-Auth und Content-Collections; AGENTS.md dokumentiert explizit MCP-Nutzungsregeln für Coding-Agenten. Relevant ist das Repo für Skill-Bibliotheken zu Frontend-Review (Accessibility, Performance, SEO, Sicherheit) und als Beispiel dafür, wie eine kuratierte Regel-Quelle automatisiert in Agenten-Skills, CLI und MCP-Tools übersetzt wird. Einschränkungen: sehr große, teils redundante Skill-Menge ohne eigene Kuration nötig, starke Bindung an den gehosteten MCP-Server und die eigene Content-Pipeline, MIT-Lizenz im lokalen LICENSE bestätigt, sowie hohe Komplexität durch Vollausbau als Produkt statt einfacher Referenzdokumentation.

---

## thedotmack/claude-mem

- **URL:** https://github.com/thedotmack/claude-mem
- **Stars:** ⭐ 102.164
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 2.570 · **Größe:** 166M
- **Struktur:** Quellcode überwiegend in `src/` (CLI, Worker-Service, Server/MCP, SQLite/Chroma-Storage) sowie ein gebauter Claude-Code-Plugin-Artefakt unter `plugin/` mit eigenen `skills/`, `hooks/`, `modes/`-Unterordnern und weiteren Skill-/Hook-Ordnern unter `.claude/` und `openclaw/` — kein reines Skill-Repo, sondern eine vollwertige Anwendung, die sich selbst als Plugin ausliefert. <!-- manual -->

Claude-Mem ist ein Apache-2.0-lizenziertes Gedächtnis- und Kompressionssystem für Coding-Agenten. Lifecycle-Hooks und Transkript-Watcher erfassen Arbeit; ein konfiguriertes Observer-Modell verdichtet sie zu Observationen und Zusammenfassungen. Ein lokaler Bun-Worker bietet HTTP-API, Web-Oberfläche und MCP-Suche über SQLite und optionale Chroma-Anbindung. Neben Claude Code gibt es Integrationen für Codex, OpenCode, Antigravity, Cursor und weitere Harnesses; neu hinzugekommen sind unter anderem T3 Code, Pi, DeepSeek Harness und Hermes.

Version 15.0.1 setzt Smart Recall als dreistufigen Ablauf `search` → `timeline` → `get_observations` voraus. Der Agent bewertet die Treffer zwischen den Schritten; `dumb_search` bleibt eine ausdrücklich flache Einmal-Suche. Alte guided/auto-APIs und Continuation-Cursors entfallen, daher müssen bestehende MCP-Clients ihren Tool-Katalog erneuern. Der Patch hält Projektscope und ausgewählte Details auch bei zusammengeführten Projekt-Aliasen konsistent. My Work ergänzt lokale Auftragsübersichten und menschliche Review-Zustände; ein vom Agenten gemeldetes „fertig“ ist von menschlich geprüft getrennt. TeamBrain ist ein optionales, kommerzielles Angebot für bewusst geteilte Projektarbeit.

Shellfreie Hook-Launcher, Windows-PATH-Einrichtung und Fallback zwischen API-Key und Claude-Abo verbessern den Betrieb. Observer-Aufrufe verarbeiten erfasste Inhalte beim gewählten Provider; optionale Cloud-/Team-Funktionen und Work-State-Telemetrie sind zusätzliche Datenflüsse. Private-Tag- und Redaction-Fixes ersetzen keine Prüfung sensibler Sitzungsdaten. Relevant als Referenz für Session-Gedächtnis und abgestufte Suche, mit erheblichem Runtime-, Storage- und Integrationsaufwand.

---

## tt-a1i/archify

- **URL:** https://github.com/tt-a1i/archify
- **Stars:** ⭐ 87.109
- **Heruntergeladen:** 2026-09-27
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 1.174 · **Größe:** 98M
- **Struktur:** Monorepo, kein reiner Skill-Ordner: `archify/` enthält Skill-Paket (`SKILL.md`, `bin/archify.mjs`-CLI, `schemas/`, `examples/`) plus gebündeltes `archify.zip` für Claude.ai/Projekt-Uploads; daneben `viewer/` (HTML-Viewer-Runtime), `website/` (Marketing-/Gallery-Seite), `docs/`, `benchmarks/`, `experiments/`, `integrations/` (u. a. DeepSeek-Harness-Plugin) und `scripts/`, `tools/`, `test/`. <!-- manual -->

Archify ist ein MIT-lizenzierter Agent-Skill mit Node-CLI unter `archify/bin/archify.mjs`, der Beschreibungen oder Repository-Evidenz in eigenständige, interaktive HTML-Artefakte überführt. Version 3.2.0 unterstützt zehn Diagrammtypen: Architecture, Workflow, Sequence, Dataflow, Lifecycle, ERD, Class/interface, Tree, Timeline und Waterfall. Typisierte JSON-Eingaben, Schema-/Layoutprüfungen und Exportdiagnosen machen Probleme für Reparaturen greifbar. Repository-Belege verweisen auf Dateien und Zeilen eines gepinnten Commits, einschließlich GitLab-Unterstützung. Viewer-Funktionen umfassen Fokus, Reach, Routen, Rollenvergleich und Live-/Still-Darstellung.

Neu ist die Explainer-Produktlinie für Antworten, die mehr als ein Diagramm brauchen: Ein Markdown-Entwurf wird zur conclusion-first Seite, in der Panels einzelne Fragen mit Prosa, Tabellen, Schritten, Charts, Code und validierten Diagrammen beantworten. Schritte und Diagrammknoten verweisen aufeinander; Quellenkarten und commit-gepinnte Codeauszüge erleichtern Prüfung. `finalize explainer` validiert und liefert atomar, `patch explainer` ersetzt ein Panel nach ID. Vier Gestaltungsstile mit hellen/dunklen Themen sowie PNG-/WebP-/JPG-Langbildexport und Druck-PDF unterstützen Weitergabe. Leere Chart-Zellen bleiben Fehler statt als Null zu erscheinen; geteilte Seiten legen keine absoluten lokalen Quellpfade offen.

Relevant für kuratierte Architekturkommunikation und nachvollziehbare technische Erklärungen. Input-, Artefakt- und Browser-Gates werden getrennt berichtet; ihr Bestehen beweist weder die fachliche Wahrheit der Autorenannahmen noch visuelle Lesbarkeit jeder komplexen Darstellung. Layout- und Wahrnehmungsgrenzen sowie unabhängig versionierte Integrationen müssen vor Übernahme separat geprüft werden.

---

## upstash/context7

- **URL:** https://github.com/upstash/context7
- **Stars:** ⭐ 63.452
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 536 · **Größe:** 25M
- **Struktur:** TypeScript-Monorepo in `packages/`; Agenten-Installationen, Regeln und Skills unter `plugins/`, `rules/` und `skills/`; Provider-Spiegel in `.agents/` und `.claude-plugin/` <!-- manual -->

Context7 liefert versionsbezogene Library-Dokumentation und Codebeispiele an Coding-Agenten. Im CLI-/Skill-Modus suchen Agents mit `ctx7 library` und fragen mit `ctx7 docs` passende Ausschnitte ab; alternativ bietet der MCP-Server native Library-Auflösung und `query-docs`. Konkrete Library-IDs und Versionsangaben präzisieren die Auswahl. Das TypeScript-Monorepo enthält öffentliche Clients, MCP-Server, SDKs und Integrationen, während API-Backend, Parsing- und Crawling-Engine privat bleiben. Community-Quellen sind deshalb weiterhin auf Qualität und Herkunft zu prüfen; Abruf garantiert keine korrekte API-Nutzung.

Beim Update stehen `ctx7` 0.8.1 und MCP 4.4.4 im Repo. Die CLI verlangt nun Node.js ab 22.13. `query-docs` kann über eine optionale Sprachpräferenz Codebeispiele bevorzugt ranken. Tokenrefresh wird zwischen parallelen Commands verriegelt; ungültige Refresh-Tokens führen zu einer erneuten Anmeldung. OpenCode-Konfigurationen behalten beim Setup Kommentare und nachlaufende Kommas, und beim Umschreiben einer stdio-Konfiguration werden inline übergebene API-Key-Argumente entfernt. Veraltete Skill-Hub-Commands sind gestrichen. Transport-/Portprüfungen, MCP-Cache-Hinweise und geordnetes HTTP-Shutdown ergänzen die Betriebskorrekturen.

Die Dokumentation präzisiert Context7 Ask und Docs7, Crawl-Grenzen, Trust-Filter sowie Query-Speicherung und LLM-Provider im Enterprise-Kontext. API-Key-/OAuth-Nutzung erhöht Zugriff und Limits, verändert bei automatischem Setup aber Agenten-Konfigurationen und erzeugt externe Datenflüsse. Relevant als Ergänzung für Library-Arbeit und als CLI-/MCP-Vergleichsreferenz. MIT-lizenziert; Limits, Kosten, Quellenvertrauen und tatsächliche Datenverarbeitung vor Nutzung separat prüfen.

---

## vercel-labs/agent-skills

- **URL:** https://github.com/vercel-labs/agent-skills
- **Stars:** ⭐ 32.776
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-09-17
- **Dateien:** 447 · **Größe:** 7,6M
- **Struktur:** 9× SKILL.md · Ordner: skills, rules, references

Kompakte, von Vercel Engineering kuratierte Sammlung von neun Skills nach dem Agent-Skills-Standard: `vercel-optimize` (Audit von Vercel-Projekten auf Kosten/Performance/Caching/Function-Nutzung), `react-best-practices` (40+ priorisierte React/Next.js-Performance-Regeln in 8 Kategorien, z.B. Waterfall-Vermeidung, Bundle-Size), `web-design-guidelines` (100+ Regeln zu Accessibility, Fokus-States, Formularen, Animation, Typografie, Dark Mode), `writing-guidelines` (80+ Regeln aus dem Vercel-Schreibhandbuch zu Tonalität, Struktur, Code-Beispielen, Typografie), `react-native-skills` (Performance/Architektur für React Native/Expo), `react-view-transitions` (React View Transition API, Next.js-Integration, inkl. vorab geladener Route-Transitions), `composition-patterns` (React-Komposition statt Boolean-Prop-Wildwuchs), `deploy-to-vercel` (sofortiges Deployment aus der Konversation heraus, mit übertragbarer Ownership) und `vercel-cli-with-tokens` (CLI-Nutzung mit Access-Tokens). Neu veröffentlicht das Repo zusätzlich einen Agent-Skills-Discovery-Index nach dem Well-Known-Entwurf der Spezifikation und liefert je Skill ein ZIP-Artefakt – interessant als Referenz dafür, wie Skill-Auffindbarkeit über Repo-Grenzen hinweg standardisiert werden soll. Installation einheitlich über `npx skills add vercel-labs/agent-skills`. Besonders relevant als unmittelbar einsetzbare, hochwertige Referenz-Skills für Frontend-Qualität (Performance, Accessibility, Schreibstil) – die `web-design-guidelines` und `react-best-practices` sind direkt vergleichbar mit den bereits genutzten Skills `web-design-guidelines` bzw. `vercel-react-best-practices` im eigenen Environment.

---

## vercel-labs/skills

- **URL:** https://github.com/vercel-labs/skills
- **Stars:** ⭐ 35.995
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 143 · **Größe:** 1,2M
- **Struktur:** kein Skill-Inhalt — das ist die Installer-CLI selbst, Quellcode in `src/` <!-- manual -->

`skills` ist die MIT-lizenzierte Installer-CLI des offenen Agent-Skills-Ökosystems, keine Sammlung fachlicher Skills. `add`, `find`, `list`, `use`, `check`, `update`, `remove` und `init` erschließen Remote-Repositories und lokale Quellen für zahlreiche Coding-Agenten. Installation erfolgt projektbezogen oder global, per Symlink beziehungsweise Kopie; `use` kann einen Prompt ausgeben oder einen unterstützten Agenten ohne dauerhafte Installation starten. Skill-Discovery erkennt unterschiedliche Verzeichnislayouts und Plugin-Manifeste. Version 1.7.4 verlangt laut README Node.js ab 22.20.

`experimental_sync` verbindet Skills aus installierten npm-Abhängigkeiten und `package.json`-Deklarationen mit dem Projekt. Es berücksichtigt auch optionale und Peer-Dependencies, rekursive Workspaces, deklarierte Git-Quellen und die zuletzt gewählten Agenten. Die kanonische Ablage ist `.agents/skills/`; weitere Host-Verzeichnisse verweisen darauf. Nach einer kurzzeitigen Promotion in 1.7.3 ist der öffentliche Befehl wieder ausdrücklich experimentell; `sync` bleibt ein Kompatibilitätsalias. Gepinnte Skill-Pfade, gespiegelte Installationen, UTF-8-BOM-Frontmatter und besondere Skill-Namen werden robuster behandelt.

Relevant als möglicher gemeinsamer Installationsweg für geprüfte Skill-Quellen. Die CLI prüft dadurch weder fachliche Qualität noch automatisch die Vertrauenswürdigkeit installierter Anweisungen. Telemetrie ist standardmäßig aktiv; `DISABLE_TELEMETRY=1` oder `DO_NOT_TRACK=1` schaltet sie und Security-Audit-Anfragen ab. Bei bestätigten öffentlichen GitHub-Quellen können Repo-/Skill-Identifier übermittelt werden; andere Quelltypen haben abweichende Sichtbarkeitsgrenzen. Neue automatische Dependency-Syncs und globale Schreibpfade sind vor Übernahme bewusst zu prüfen.

---

## VoltAgent/awesome-design-md

- **URL:** https://github.com/VoltAgent/awesome-design-md
- **Stars:** ⭐ 122.766
- **Heruntergeladen:** 2026-07-13
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 173 · **Größe:** 2,4M
- **Struktur:** keine Standard-Skill-/Agent-Ordner (Quellcode/CLI oder reine Doku)

Awesome-design-md ist eine von VoltAgent kuratierte Sammlung von laut README 84 DESIGN.md-Analysen, die das von Google Stitch eingeführte Format für maschinenlesbare Design-Systeme nutzen. Jede Datei beschreibt für eine bekannte Marke (u.a. Stripe, Apple, Notion, Tesla, Figma; neu auch Enterprise-Marken wie Oracle und SAP) Farbpalette, Typografie-Hierarchie, Komponentenstile, Spacing/Grid, Schatten/Elevation, Responsive-Regeln sowie Do's/Don'ts als strukturiertes YAML-artiges Markdown mit kurzem Agenten-Prompt-Leitfaden. Das Konzept ist analog zu AGENTS.md gedacht: Während AGENTS.md Coding-Agenten sagt, wie gebaut wird, sagt DESIGN.md Design-/Coding-Agenten, wie es aussehen soll. Nutzer kopieren die Datei ins Projektroot und weisen den KI-Agenten an, UI im jeweiligen Stil zu generieren. Es handelt sich um reine, textuelle Referenzdaten ohne Automatisierungslogik, Parser oder Tooling – kein Skill-/Plugin-System, kein Code. Besonders nützlich ist die Sammlung als Prompt-Kontext-Baustein für UI-generierende Agenten und Workflows: Design-Konsistenz per Drop-in-Datei, nicht als Skill oder Agent selbst. Sie ergänzt damit die eher regelbasierten Design-Skills wie [nextlevelbuilder/ui-ux-pro-max-skill](#nextlevelbuilderui-ux-pro-max-skill) um fertige, markenspezifische Tokens. Einschränkungen: Werte sind aus öffentlich sichtbarem CSS extrahiert (keine Garantie auf Aktualität/Rechtmäßigkeit bei Markenänderungen), es gibt keine Validierung/Tests der Tokens, Qualität hängt von der ursprünglichen Extraktion ab, und das Projekt ist stark durch das kommerzielle Angebot getdesign.md/VoltAgent getrieben (Sponsoring-Banner, Marketingsprache im README). MIT-lizenziert.

---

## wshobson/agents

- **URL:** https://github.com/wshobson/agents
- **Stars:** ⭐ 41.485
- **Heruntergeladen:** 2026-07-10
- **Zuletzt aktualisiert:** 2026-10-22
- **Dateien:** 1.170 · **Größe:** 8,1M
- **Struktur:** 185× SKILL.md · Ordner: skills, agents, commands, hooks, plugins, references · Spiegelordner: .agents, .cursor, .cursor-plugin (generiert)

Eine sehr umfangreiche Sammlung von Plugins, Agenten und Skills für KI-Coding-Tools: 94 Plugins (92 lokale plus 2 externe Einträge), 202 Agenten, 185 Skills und 105 Commands (u. a. `avoid-ai-writing` gegen typische KI-Schreibmuster, `pptx-deck-creation` für Präsentationen, `llm-finetuning` und `dgx-spark-ops` für eine Eval-gesteuerte Fine-Tuning-Pipeline sowie `superself`), aus einer einzigen Markdown-Quelle (`plugins/`) generiert und auf sieben Tools ausgespielt: Claude Code als Quelle der Wahrheit plus Codex CLI, Cursor, OpenCode, Antigravity CLI, GitHub Copilot und Pi – jeweils mit harness-nativen Artefakten statt kleinstem gemeinsamen Nenner. Neu ist `social-evidence-research` für beleggestützte Social-Recherche; übergroße Skills lagern Details in Referenzen aus, und Copilot-Adapter bewahren diese samt Assets. Ein Breaking Change im August 2026 hatte das frühere Gemini-CLI-Ziel durch die Google-Antigravity-CLI ersetzt. Claude Code, Codex (`codex plugin marketplace add`) und Cursor installieren nativ aus committeten Marketplace-Registern; der native Codex-Katalog enthält inzwischen nur noch Plugins mit echten Quell-Skills, während generierte TOML-Agenten und aus Commands abgeleitete Skills einen separaten Adapterweg nutzen. OpenCode, Antigravity, Copilot und Pi werden per Clone und `make install-<harness>` eingerichtet, einzelne Skills zusätzlich über `gh skill` oder `npx skills`. Jedes Plugin ist isoliert und komponierbar (z. B. `plugins/python-development/` mit eigenen Agenten, Commands, Skills); die Installation eines Plugins lädt nur dessen Komponenten in den Kontext. Sicherheits- und datenschutzrelevant: Der `file-conversion`-Skill lädt Dateien nicht mehr per Skript zu einem externen Konvertierungsdienst hoch, sondern beschreibt lokale Konvertierung mit FFmpeg, ImageMagick, Pandoc und LibreOffice; mehrere Infrastruktur-Skills erhielten sicherere Setup-Beispiele. Nutzt eine gestufte Modellstrategie (Fable 5/Opus für Architektur/Sicherheit, Sonnet für Doku/Tests, Haiku für operative Aufgaben) und ein dreistufiges Qualitäts-Eval-Framework (`plugin-eval`: statische Analyse, LLM-Judge, Monte-Carlo-Zuverlässigkeitstests). LLM-Judge und Monte-Carlo-Layer sind experimentell und nicht gegen menschliche Labels validiert; deren Scores belegen keine erfolgreiche Projektaufgabe. Enthält externe Memory-Integration (Pensyve) als Git-Subdir-Einbindung. Build-Tooling (`make generate-all`, `make validate`, `make garden`) hält alle Harness-Ausgaben synchron; die Garden-Prüfungen kontrollieren auch Komponenten-Zahlen und Agenten-Divergenz. Sehr relevant als Referenz für Multi-Harness-Distribution aus einer Quelle sowie für das eigene Qualitäts-Eval-Konzept für Skills/Plugins.
