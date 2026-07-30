# Changelog externer Repositories

Dieses Changelog dokumentiert inhaltliche Änderungen der lokal gepflegten externen Repositories. Neue Update-Läufe werden oben ergänzt. Pro geändertem Repo werden Commit-Spanne, relevante Neuerungen und die Auswirkung auf `external_repos/INDEX.md` festgehalten.

Unveränderte Repositories erscheinen nur in der Laufstatistik. Mechanische Metadaten wie Dateizahl, Größe, Struktur und Stars bleiben im `external_repos/INDEX.md`.

## 2026-07-30

- **Regulärer Lauf:** 56 Repos geprüft · 43 geändert · 13 unverändert · 0 Fehler
- **Separater Lauf:** `mleibetseder/ai-llm-wiki` unter `external_knowledge/` aktualisiert
- **Index:** Mechanische Metadaten vollständig neu gescannt; 15 inhaltliche Repo-Zusammenfassungen angepasst

### 0xNyk/council-of-high-intelligence

- **Commits:** `482d8e88 → c1395a6f`
- **Änderungen:** Ausschließlich die Star-History-Charts wurden aktualisiert; Rollen, Skills und Council-Workflow blieben unverändert.
- **Index:** Inhaltliche Zusammenfassung unverändert, da keine funktionale Änderung vorliegt.

### abi/screenshot-to-code

- **Commits:** `e68babc6 → b0d6ab88` (33 Commits)
- **Änderungen:** Neue Text-Brief-Eval-Sets, Side-by-Side-Vergleich für Eval-Ausgaben und strengere Fehlerbehandlung für Agent-Runs ohne Output. Modellmixe und Preise wurden unter anderem für Gemini-3.6-Flash-Varianten aktualisiert.
- **Index:** Inhaltliche Zusammenfassung unverändert; der bestehende Eintrag deckt Modellwahl, visuelle Evaluation und Preview-Iteration bereits ab.

### addyosmani/agent-skills

- **Commits:** `2fbfa004 → 7829ffd9` (15 Commits)
- **Änderungen:** Commands und TDD-Anweisungen wurden stärker ecosystem-neutral formuliert. Performance-Optimierung erhielt einen expliziten Keep-or-Revert-Verifikationsschritt; Skill-Referenzen und Security-Dokumentation wurden präzisiert.
- **Index:** Inhaltliche Zusammenfassung unverändert, da Umfang und Lifecycle-Modell gleich blieben.

### affaan-m/ECC

- **Commits:** `5deee34c → e4e41631` (66 Commits)
- **Änderungen:** Release 2.1 mit 67 Agenten, 281 Skills und 94 Legacy-Command-Shims. Hook-Erkennung, OpenCode-Fehlerbehandlung, Installationshinweise und die README-Struktur wurden überarbeitet.
- **Index:** Zusammenfassung auf die aktuellen Agenten-, Skill- und Command-Zahlen sowie die breitere Harness-Unterstützung aktualisiert.

### anthropics/claude-code

- **Commits:** `ac062f33 → 7ef6eec9` (3 Commits)
- **Änderungen:** Offizielles `CHANGELOG.md` und der Release-Feed wurden dreimal synchronisiert; am Aufbau des GitHub-Repositories änderte sich nichts Wesentliches.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### anthropics/skills

- **Commits:** `fa0fa64b → b29e7cf6` (2 Commits)
- **Änderungen:** Der neue bzw. stark erweiterte `claude-api`-Skill dokumentiert Claude Opus 5, Tool Runner und Managed Agents. Mehrsprachige Beispiele behandeln gehostete Session-Workspaces, Skills/MCP, Vault-Credentials und Scheduled Deployments.
- **Index:** Zusammenfassung um den Claude-API-/Managed-Agents-Bereich und den Hinweis auf schnell veränderliche Beta-Oberflächen ergänzt.

### bmad-code-org/BMAD-METHOD

- **Commits:** `8b4da791 → 9b672e1e` (16 Commits)
- **Änderungen:** `Quick Dev`/`Dev Auto` wurden zu `Build`/`Build Auto`; alte Namen bleiben über v6-Shims kompatibel. Market-, Domain- und Technical-Research wurden in `bmad-deep-recon` konsolidiert, Review-Flows und Editor-Handoffs verbessert.
- **Index:** Aktive Skill-Struktur, Kompatibilitäts-Shims, neue Build-Namen und Deep-Recon-Konsolidierung eingearbeitet.

### bradygaster/squad

- **Commits:** `667271b5 → e23dd920` (32 Commits)
- **Änderungen:** Work-Item-Bodies werden nun über den Adapter hydratisiert und der Zwei-Pass-Scan läuft durch die Plattformabstraktion. Der übrige Lauf bestand überwiegend aus SDK-, Docs-, Playwright- und CI-Dependency-Updates.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### coreyhaines31/marketingskills

- **Commits:** `67264763 → 7868cb92` (11 Commits)
- **Änderungen:** Neuer `attribution`-Skill für Source-of-Truth, Multi-Touch-Modelle, Incrementality und First-Party-Stitching bis ins CRM. Der Pricing-Teardown bewertet zusätzlich die AI-Agent-Readiness einer Seite.
- **Index:** Skill-Zahl auf 49 erhöht und Attribution sowie Pricing-Erweiterung ergänzt.

### davila7/claude-code-templates

- **Commits:** `b87f5c0c → 67b5a008` (28 Commits)
- **Änderungen:** Drei Ansvar-Skills für EU-Compliance wurden ergänzt. Backend-Developer- und Market-Researcher-Agenten erhielten aktualisierte Runtime-, Security-, Discovery- und Qualitätsvorgaben; Katalog- und Trending-Daten wurden mehrfach synchronisiert.
- **Index:** Inhaltliche Zusammenfassung unverändert, da der Eintrag die Sammlung bewusst auf Katalogebene beschreibt.

### diegosouzapw/OmniRoute

- **Commits:** `698b6eb0 → e6523da2` (5 Commits)
- **Änderungen:** Release 3.8.49, überarbeitete README-/Sprach-Dokumentation und stabilisierter npm-Publish-Workflow. Mehrere Dependabot-Sicherheitsmeldungen wurden über Upgrades bzw. Overrides geschlossen.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### Egonex-AI/Understand-Anything

- **Commits:** `6ae71878 → fe8c5bc5` (13 Commits)
- **Änderungen:** Swift-Ignore-Patterns wurden auf Testverzeichnisse begrenzt. Der `PostToolUse`-Hook liefert wieder zusätzlichen Kontext; Handler und Tests wurden entsprechend refaktoriert und erweitert.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### emilkowalski/skills

- **Commits:** `f6f79ca1 → 70744e38` (2 Commits)
- **Änderungen:** Neuer `prototype`-Skill erzeugt mehrere UI-Varianten und macht sie über einen Switcher vergleichbar.
- **Index:** Skill-Zahl auf acht erhöht und der neue Varianten-/Prototyping-Workflow beschrieben.

### farion1231/cc-switch

- **Commits:** `606e7bbe → c0ff89b9` (41 Commits)
- **Änderungen:** Release 3.19.0 mit Security- und Preset-Aktualisierungen. Der App-Switcher wurde vereinfacht; Codex-Rollout-Timelines werden gecacht und mehrere Provider-Presets aktualisiert.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### github/spec-kit

- **Commits:** `d7699c39 → f36634b5` (171 Commits)
- **Änderungen:** Stark ausgebautes Workflow-, Extension-, Preset- und Bundle-System mit zahlreichen Community-Katalogen und Governance-Presets. Neu bzw. hervorgehoben sind `/speckit.converge`, Intent Reconciliation und zusätzliche Community-Workflows; Parser, Downloads und Katalog-Metadaten wurden umfassend gehärtet.
- **Index:** Zusammenfassung um `.converge`, katalogisierte Workflows, priorisierte Kataloge und den Prüfhinweis für Community-Artefakte ergänzt.

### Graphify-Labs/graphify

- **Commits:** `e32c9f43 → ecfcd160` (94 Commits)
- **Änderungen:** Release 0.9.30 behebt TSX-Grammatik, Edge-Richtung und Bedrock-Timeouts. Multi-Projekt-Kontexte im MCP-Server sind nun begrenzt; weitere Fixes verbessern Graph-Merges, Parser und Provider-Backends.
- **Index:** Inhaltliche Zusammenfassung unverändert, da der Eintrag die Knowledge-Graph-Funktion bereits abdeckt.

### headroomlabs-ai/headroom

- **Commits:** `961866ba → 28aa53dc` (57 Commits)
- **Änderungen:** MCP-Abhängigkeit gegen einen Startup-Crash gepinnt, Cache-Control-TTLs und Sliding-Window-TTLs korrigiert. Code-Kompression berücksichtigt CJK besser; Gemini-Thinking-Tokens fließen korrekt in die Kostenmessung ein.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### intellectronica/ruler

- **Commits:** `9da4410e → 82244744` (10 Commits)
- **Änderungen:** Generierte MCP-Provenienz bleibt über Reverts erhalten; verschachtelte Agent-Auswahl, leere Verzeichnisbereinigung und OpenCode-Markierungen wurden korrigiert. MCP-Transportfelder und Release-Workflow wurden gehärtet.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### jakubkrehel/make-interfaces-feel-better

- **Commits:** `366f0f86 → 5f3c3c26` (2 Commits)
- **Änderungen:** Neue Icon-Referenz zu Stroke Weight, `currentColor`-Zuständen, Outline/Fill, kleinen Rastergrößen, RTL und Accessibility. Skill- und Referenzstruktur wurden entsprechend angepasst.
- **Index:** Zusammenfassung um Icon-Polish ergänzt und die Zahl der relativen Referenzdokumente von vier auf fünf korrigiert.

### langchain-ai/openwiki

- **Commits:** `08514449 → 3076d557` (49 Commits)
- **Änderungen:** `.openwikiignore` schließt private, generierte oder irrelevante Pfade aus Discovery und Shell-Zugriff aus. Neu sind ein DeepSWE-Eval-Harness, GitHub-Copilot-/Requesty-Dokumentation, idempotenter Skill-Sync und Changeset-basiertes Release-Tooling.
- **Index:** Zusammenfassung um `.openwikiignore` und GitHub Copilot als Inference-Provider ergänzt.

### Leonxlnx/taste-skill

- **Commits:** `98565e65 → e988add2` (4 Commits)
- **Änderungen:** Ausschließlich Sponsoren und deren Darstellung im README wurden angepasst.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### mattpocock/skills

- **Commits:** `ed37663c → 2ab95809` (2 Commits)
- **Änderungen:** Installationsanweisungen wurden nach Zielgruppe getrennt und klarer strukturiert; die Skills selbst änderten sich nicht.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### microsoft/markitdown

- **Commits:** `24c14c6b → fd239d5d` (3 Commits)
- **Änderungen:** Release 0.1.7 behebt OMML-Template-Probleme und unterstützt PPTX-SVG-Bilder ohne vorhandenes Raster-Fallback zuverlässiger.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### millionco/react-doctor

- **Commits:** `84b99900 → 5dc936e1` (51 Commits)
- **Änderungen:** Zahlreiche Präzisionskorrekturen reduzieren False Positives bei lokalem State, Promise-Recovery, Ref-Initialisierung, Next.js-Props und kleinen Iterationsketten. Mehrere Pakete und Changelogs wurden gemeinsam veröffentlicht.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### msitarzewski/agency-agents

- **Commits:** `459dce83 → 8ef49232` (2 Commits)
- **Änderungen:** Neue Agenten für Privacy Engineering, Rust-Refactoring, LLM-Post-Training, Data Visualization, UI Finish-Gate und die Unterstützung pflegender Angehöriger.
- **Index:** Zusammenfassung um die neuen Spezialgebiete ergänzt.

### nextlevelbuilder/ui-ux-pro-max-skill

- **Commits:** `1307d97a → 4857a2c5` (7 Commits)
- **Änderungen:** Codex installiert Skills nun korrekt unter `.agents`; Shared Targets und Uninstall-Hinweise wurden korrigiert. Der TypeScript-Fallback läuft über Node und das shadcn-Test-Asset ist gepinnt.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### nexu-io/open-design

- **Commits:** `447b18b9 → 7d7c56a7` (79 Commits)
- **Änderungen:** Zahlreiche Daemon- und Session-Fixes für lokale Codex-/Kiro-Läufe, Tool-Fortsetzungen und Auth-Recovery. Browser-Preview-Viewport, Pack-Artefakte und Release-Workflows wurden stabilisiert.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### NVIDIA/SkillSpector

- **Commits:** `5fb8399d → 34f60308` (11 Commits)
- **Änderungen:** Release 2.5 führt ein kanonisches Inspection Ledger und Execution-Completeness in JSON/SARIF ein. Rekursive Child-Scan-Fehler schlagen nun auf den Gesamtlauf durch; Anthropic-Endpoint-Overrides und Provider-Isolation wurden korrigiert.
- **Index:** Zusammenfassung um Inspection Ledger, vollständige Ausführungsnachweise und die Unterscheidung statischer gegenüber LLM-Scans ergänzt.

### obra/superpowers

- **Commits:** `d884ae04 → 44c9b2d6` (52 Commits)
- **Änderungen:** Release 6.2 macht SDD-Workspaces planbezogen und lässt Review-Fixes denselben Implementer fortsetzen. Fokussierte Re-Reviews, ein Fünf-Runden-Circuit-Breaker und ein positiver Katalog für belastbare Tests stärken die Verifikation; Windows-SessionStart wurde repariert.
- **Index:** Zusammenfassung auf den neuen SDD-Lifecycle und die verschärften Test-/Review-Gates aktualisiert.

### open-gsd/gsd-core

- **Commits:** `34352180 → 4f6935e2` (135 Commits)
- **Änderungen:** Breiter Ausbau von Reviewer-Lanes, Trust-Disclosure, Capability-Gates, Host-Integrationen, MCP-Server, State-Rebuild und Debugger-Methodik. Optionale Claude-Orchestrierung, API-Coverage-Gates und mehrere Runtime-/Windows-Fixes kamen hinzu.
- **Index:** Charakterisierung von „schlank" zu „umfangreich" korrigiert und die neuen Orchestrierungs-, MCP-, Debugging- und Governance-Funktionen ergänzt.

### openai/codex

- **Commits:** `5bfd74d3 → bdda5da5` (292 Commits)
- **Änderungen:** Executor-Workspace-Rechte werden bei `apply_patch` gewahrt; normalisierte Toolnamen kollidieren nicht mehr. Delegierte Tasks überleben Remote-Compaction, Tool-Runtime-Assembly und Capability Discovery wurden sicherer und stärker zentralisiert.
- **Index:** Inhaltliche Zusammenfassung unverändert, da sie bewusst Architektur und Referenzwert des Repositories beschreibt.

### OthmanAdi/planning-with-files

- **Commits:** `117dfae8 → b04ffd9c` (3 Commits)
- **Änderungen:** Release 3.8.2 macht Session-Recovery robust für Projektpfade mit Punkten, Leerzeichen und Emojis. Transcript-Catchup wird zusätzlich über das aufgezeichnete Arbeitsverzeichnis gegen projektübergreifende Kollisionen abgesichert.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### paperclipai/paperclip

- **Commits:** `cac3c0fa → d5b9f6c8` (133 Commits)
- **Änderungen:** Referenzierte Projekte werden als mehrere Workspaces durch Run-Vorbereitung und Sandbox-Synchronisierung geführt. UI-Listen erhielten Recency-Trenner und Loader; Plugin-RPC-Timeouts sowie Sandbox-Sync-Performance wurden verbessert.
- **Index:** Inhaltliche Zusammenfassung unverändert, da Workspaces, Plugins und Governance bereits beschrieben sind.

### pbakaus/impeccable

- **Commits:** `4d849eb7 → 6b342244` (415 Commits)
- **Änderungen:** Releases für Skill 4.0.4, CLI 3.5.0 und Extension 1.3.1. Der Detektor umfasst nun 59 Regeln; `craft`, Finish-Reviewer-Autorität, Ignore-Konfiguration und mehrere Framework-/Provider-Pfade wurden ausgebaut.
- **Index:** Detektorzahl von 46 auf 59 erhöht und `craft`, Accessibility-/Qualitätschecks sowie konfigurierbare Ausnahmen ergänzt.

### router-for-me/CLIProxyAPI

- **Commits:** `36b45d57 → a80e8082` (117 Commits)
- **Änderungen:** Codex-Modellauflösung und Header-Management wurden präzisiert, inklusive `disable-codex-cloaking`. Auth-Dateien unterstützen Credential-Gewichte; JSON-Schema-/Response-Format-Übersetzung und Repository-Recovery wurden stabilisiert.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### rtk-ai/rtk

- **Commits:** `4f865233 → 8a24ce2e` (67 Commits)
- **Änderungen:** Grep-Ausgabe wurde transparenter und mit/ohne Zeilennummern getestet; Escaped-Space-Pfade bei `tee` wurden repariert. Regex-Initialisierung und mehrere Search-/Recovery-Pfade wurden vereinfacht bzw. korrigiert.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### shadcn-ui/ui

- **Commits:** `fa4872c8 → efafb091` (36 Commits)
- **Änderungen:** Mehrere neue Registry-Anbieter (`atelier`, `kinetic`, `usva`, `wa-ui`) und Umbenennungen wurden aufgenommen. shadcn-Paket-Changelog, Templates und Next.js-Canary-Tests wurden aktualisiert.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### shanraisshan/claude-code-best-practice

- **Commits:** `154e7247 → e30c04a1` (113 Commits)
- **Änderungen:** Umfangreiche automatisierte Drift-Checks und Changelog-Aktualisierungen für Commands, Skills, Subagents, Settings und Konzepte. Veraltete Claude-Dokumentationslinks wurden korrigiert; die Kernstruktur blieb gleich.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### teng-lin/notebooklm-py

- **Commits:** `45fd4258 → 7d0aa42c` (2 Commits)
- **Änderungen:** Playwright-Start für die Authentifizierung wurde zentralisiert und Windows-sicher gemacht. Der Gemini-Notebook-Login-Host wird nun korrekt erkannt.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### thedotmack/claude-mem

- **Commits:** `f5633c1f → 132b4634` (2.319 Commits)
- **Änderungen:** Releases bis 13.12.4 mit zweispuriger, standardmäßig deaktivierter Cloud-Synchronisierung. Große Fix-Welle für Windows-Prozesse, Suchranking, Datenintegrität, Worker-Neustarts, Migrationen und Codex-Kontextinjektion; kritische Restart-Loops wurden strukturell behoben.
- **Index:** Zusammenfassung um Opt-in-Sync, aktuelle Reliability-Fixes und das daraus sichtbare Komplexitätsrisiko ergänzt.

### upstash/context7

- **Commits:** `23843e9c → 594a7313` (13 Commits)
- **Änderungen:** API-Methodentabelle und Beispiel-URLs wurden korrigiert; Enterprise-Dokumentation deckt externe Postgres-Datenbanken und Library Access Control ab. Die CLI schreibt API-Keys nun korrekt als Authorization-Header; mehrere Pakete wurden veröffentlicht.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### vercel-labs/agent-skills

- **Commits:** `4559f18a → 7c180d90` (11 Commits)
- **Änderungen:** React-View-Transition-Skill um Layout-Stabilisierung, Enter-only Reveals, Live-Root-Rezept, Wrapper-Trick, Z-Index-Tiering und präzisere Router-Back-Guidance ergänzt. Installationsbefehl korrigiert.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### vercel-labs/skills

- **Commits:** `1be66ad0 → 7cb7db64` (14 Commits)
- **Änderungen:** Release 1.5.21. Direkte URL-Installationen und Well-known-Archive wurden gehärtet; ZIP-Extraktion wurde vereinheitlicht und von `yauzl` entkoppelt.
- **Index:** Inhaltliche Zusammenfassung unverändert.

### mleibetseder/ai-llm-wiki

- **Commits:** `7c0748a → bd8f3d9`
- **Änderungen:** 111 Dateien mit 1.907 neuen Zeilen: Loop Engineering, 30 Memory-Techniken, Agent Usability Testing, Evaluation Loops, AI Trust & Verification, resiliente AI-Stacks, autonome Digital Workers und Open Multi-Agent Kit. Drei neue Fach-PDFs wurden aufgenommen.
- **Index:** Manuellen Eintrag auf 764 Dateien, 262 MB, 250 Konzepte, 96 Entities und 14 Paper-Seiten aktualisiert; Zusammenfassung um die neuen Wissenscluster ergänzt.
