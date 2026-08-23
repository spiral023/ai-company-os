# Changelog externer Repositories

Dieses Changelog dokumentiert inhaltliche Änderungen der lokal gepflegten externen Repositories. Neue Update-Läufe werden oben ergänzt. Pro geändertem Repo werden Commit-Spanne, relevante Neuerungen und die Auswirkung auf `external_repos/INDEX.md` festgehalten.

Unveränderte Repositories erscheinen nur in der Laufstatistik. Mechanische Metadaten wie Dateizahl, Größe, Struktur und Stars bleiben im `external_repos/INDEX.md`.

## 2026-08-23

- **Regulärer Lauf:** 55 Repos geprüft · 49 geändert · 6 unverändert · 0 Fehler
- **Separater Lauf:** `mleibetseder/ai-llm-wiki` unter `external_knowledge/` aktualisiert
- **Nicht gepullt:** `nexu-io/open-design` ist kein Git-Klon mehr und wird seit dem 30.07.2026 bewusst übersprungen (daher 55 statt 56 Ordner)
- **Index:** Mechanische Metadaten vollständig neu gescannt; 30 inhaltliche Repo-Zusammenfassungen angepasst

### 0xNyk/council-of-high-intelligence

- **Commits:** `c1395a6f → f506e010` (13 Commits)
- **Änderungen:** GitHub-Actions wurden auf Commit-SHAs gepinnt und mit expliziten Permissions versehen; ein Roster-Drift zwischen SKILL.md-Prosa und Agent-Frontmatter wurde repariert, und Enforcement-Aufrufe werden in den Session-Metadaten mitgezählt. Dazu die üblichen Star-History-Refreshes.
- **Index:** Unverändert — 18 Personas, Modi und Council-Workflow sind gleich geblieben, die Änderungen betreffen Wartung und Konsistenzprüfung.

### abi/screenshot-to-code

- **Commits:** `b0d6ab88 → d026163f`
- **Änderungen:** Ein einzelner Commit parallelisiert Batch-Bildbearbeitung und Hintergrundentfernung.
- **Index:** Unverändert — der Eintrag nennt Replicate für Bildgenerierung, Hintergrundentfernung und Bildbearbeitung bereits; parallelisiert statt sequenziell ändert die Einordnung nicht.

### addyosmani/agent-skills

- **Commits:** `7829ffd9 → 5a5ea45e` (56 Commits)
- **Änderungen:** Plugin-Manifeste auf 0.6.7. Der `spec`-Skill erhielt einen Phase-0-Scope-Check mit Capability-Map für Anforderungen über mehrere Fähigkeiten, die Planung ein einziges pluggables Task-List-Ziel. Neu sind ein CI-Gate für `references/`-Links in Skills, ein Validator für Spec-/Plan-/Todo-Artefaktpfade, Idempotency-Key-Guidance und ein Abschnitt zu Datenschutz und Compliance.
- **Index:** Unverändert — 24 Skills, Lifecycle-Struktur und Slash-Commands sind identisch; die Änderungen verfeinern bestehende Skills, statt den Umfang zu verschieben.

### affaan-m/ECC

- **Commits:** `e4e41631 → d8409a4b` (92 Commits)
- **Änderungen:** Neue multimodale Skill-Familie „TasteForge“ inklusive `tasteforge-video` für wiederholbare, geschmacksgetriebene Video-Arbeit, mit gehärtetem und getestetem Kontrakt. Dazu Release-Tests für die gepackte Ito-Distribution, Windows-Fixes bei Nasiko und präzisierte Antigravity- und Installationsdokumentation.
- **Index:** Angepasst — Agenten- und Skill-Zahlen auf 68/286 aktualisiert und TasteForge in der Skill-Aufzählung ergänzt.

### alirezarezvani/claude-skills

- **Commits:** `aa8d7788 → 98180daf` (19 Commits)
- **Änderungen:** Zwei neue Engineering-Skills: `book-to-skill` (aus EPUB/PDF einen Skill destillieren, mit gehärteter XML- und Zip-Verarbeitung, Zip-Budget, privatem Arbeitsverzeichnis und Verweigerung symlinkter Bäume) und `memory-engineering` („engineer the forgetting“, mit geschlossener F1-Umgehung und erreichbaren Tie-Breakern). Der Referenz-Doku-Zähler wurde von 746 auf 750 korrigiert.
- **Index:** Angepasst — Skill-Zahl auf die README-Angabe 345 gesetzt (bei 364 SKILL.md-Dateien im Baum), die beiden neuen Engineering-Skills und die Zahl der Referenzdateien ergänzt.

### anthropics/claude-code

- **Commits:** `7ef6eec9 → 45bdfa96` (707 Commits)
- **Änderungen:** 707 Commits, praktisch ausschließlich automatische Synchronisierung von `CHANGELOG.md` und `feed.xml`. Am Aufbau des Repositories selbst hat sich nichts geändert.
- **Index:** Unverändert — der Eintrag beschreibt genau diesen Charakter des Repos (Distributionsmaterial statt CLI-Quellcode).

### anthropics/skills

- **Commits:** `b29e7cf6 → 3b3fad96` (6 Commits)
- **Änderungen:** Zwei neue Skills: `discernment-nudge` und `claude-academy-guide`, letzterer direkt danach zu `academy-guide` umbenannt und in der Beschreibung gekürzt. Der `claude-api`-Skill erhielt einen Upgrade-Guide vom Python-SDK 0.x auf 1.x, eine Doku zum `prompt-audit`-Unterkommando und die Managed-Agents-Augustwelle.
- **Index:** Angepasst — die beiden neuen Skills und der SDK-Migrationsleitfaden sind ergänzt.

### bmad-code-org/BMAD-METHOD

- **Commits:** `9b672e1e → 67d876f1` (60 Commits)
- **Änderungen:** Schwerpunkt ist ein mehrschichtiges Code-Review: Review-Ebenen werden alle gestartet, bevor ein Ergebnis behandelt wird, erhalten Diff und Review-Inhalt per Pfad statt inline, bleiben in ihrem Ausgabekontrakt, und ein Edge-Case-Hunter falsifiziert die eigenen Behauptungen. Dazu wurden Menü-Buchstabencodes durchgängig ersetzt, und der Installer fragt bei Quick Update nach veralteten Shims.
- **Index:** Angepasst — das neue `bmad-code-review` mit seinen Review-Ebenen ist ergänzt; Phasen, Personas und Modul-Ökosystem blieben unverändert.

### bradygaster/squad

- **Commits:** `e23dd920 → 4b32f7be` (1921 Commits)
- **Änderungen:** Mit 1.921 Commits der bewegteste Klon im Index. Inhaltlich: Ein Team-Guard-Schritt zertifiziert das Roster, `/squad` scheitert jetzt laut statt still, wenn kein Kommando geparst wird, CRLF-Arbeitsbäume werden repariert, und die Scribe-Archivierung kann Zustand nicht mehr zerstören. Dazu eine umfangreiche E2E-Dokumentation, in der auch eine falsche Prognose ausdrücklich zurückgezogen wird.
- **Index:** Unverändert — das Konzept (persistente, benannte Agenten-Teams, Watch Mode „Ralph“, Entscheidungsprotokoll) ist unberührt; die Änderungen sind Härtung und Testdokumentation.

### coreyhaines31/marketingskills

- **Commits:** `7868cb92 → 3df87f97` (7 Commits)
- **Änderungen:** `ai-seo` erhielt eine Agent-Readiness-Ebene und eine Bewertung der Volatilität von Zitationsquellen (2.4.0), `influencer-marketing` ein Programm für UGC-Creator in technischen Nischen mit Compliance-Überarbeitung. Außerdem wurden Praktiker- und Knowatoa-Erkenntnisse in `ads`, `ai-seo`, `content-strategy` und `public-relations` eingearbeitet sowie eine Regel für nicht vertrauenswürdige Daten über alle auditierenden Skills gelegt.
- **Index:** Angepasst — Agent-Readiness in `ai-seo`, das UGC-Programm und die Untrusted-Data-Regel sind ergänzt; die Skill-Zahl 49 bleibt.

### davila7/claude-code-templates

- **Commits:** `67b5a008 → 5d313282` (95 Commits)
- **Änderungen:** Laufender Katalogbetrieb: neue MCP-Server (Sicex, AgentPlat), ein Cohesivity-Marketplace-Eintrag, ein `repo-publication-auditor` bei den Security-Agenten, ein globaler Concise-Mode als Setting und automatisierte Review-Verbesserungen an bestehenden Agenten, dazu regelmäßige Trending-Data-Updates.
- **Index:** Unverändert — der Eintrag beschreibt den Katalog absichtlich mengenneutral („mehr als hundert“) und betont die Prüfbedürftigkeit; einzelne Katalogzugänge ändern das nicht.

### diegosouzapw/OmniRoute

- **Commits:** `e6523da2 → 65e81158` (9 Commits)
- **Änderungen:** Ollama-Modelle werden nach beworbener Capability geroutet, vom Health-Check ausgeschlossene Modelle verschwinden aus dem `/v1/models`-Katalog, geteilte Passthrough-Provider werden respektiert, und die Modell-Preisabfrage ist memoisiert (Event-Loop und Healthz). Dazu Dependabot-Bumps für nanoid und dompurify.
- **Index:** Unverändert — Providerzahl, Routing-Strategien und Risikobewertung bleiben gültig; die Änderungen sind Routing- und Sicherheits-Feinschliff.

### DietrichGebert/ponytail

- **Commits:** `16f29800 → 2ed6c52c` (4 Commits)
- **Änderungen:** Release v4.9.0 mit einem nativen Skills-Adapter für Grok Build. VS Code Copilot wird jetzt auch über `CLAUDE_PLUGIN_ROOT` erkannt, und `commandWindows` wurde aus `hooks.json` entfernt, damit die Claude.ai-Marketplace-Validierung durchläuft.
- **Index:** Angepasst — Grok Build ist in der Liste der nativen Adapter ergänzt.

### Egonex-AI/Understand-Anything

- **Commits:** `fe8c5bc5 → 32944829` (4 Commits)
- **Änderungen:** Der Onboarding-Guide wird als `UA_ONBOARDING.md` gespeichert, und generierte Artefakte werden beim Auto-Update ignoriert.
- **Index:** Unverändert — zwei kleine Fixes an Dateinamen und Update-Verhalten; Pipeline, Agenten und Befehle sind identisch.

### emilkowalski/skills

- **Commits:** `70744e38 → d23d7f88` (8 Commits)
- **Änderungen:** Vier neue Skills: `animate` (Animationen von Null aufbauen statt nur bewerten), `expo`/`animate-expo` und `write-swift` für React Native/Expo und natives Swift sowie `ask-sonner` zur Toast-Bibliothek des Autors. Damit verlässt die Sammlung erstmals das reine Web-Frontend.
- **Index:** Angepasst — Skill-Zahl von acht auf zwölf korrigiert, die vier neuen Skills benannt und die Ausweitung auf Mobile- und Apple-Plattformen vermerkt.

### farion1231/cc-switch

- **Commits:** `c0ff89b9 → 5ca9459d` (114 Commits)
- **Änderungen:** Release v3.20.0: Der Umschalter für das 1-Mio.-Token-Kontextfenster bei Codex ist zurück, der Goal-Mode-Toggle entfällt (Upstream aktiviert Goals per Default), mehrere Follow-Login-Provider und konfigurierbare OAuth-Verbrauchsabfragen sind möglich. Dazu Preis-Nachträge (DeepSeek V4 Peak-Tier, Gemini 3.7 Flash), ein Fix gegen hängende Upgrade-Preflights und `process:allow-exit`, damit die Exit-Buttons die App wirklich beenden.
- **Index:** Angepasst — die v3.20-Funktionen (1-Mio.-Kontext-Toggle, Follow-Login-Provider, OAuth-Verbrauchsabfragen) sind ergänzt; die Bewertung als Referenz für Provider-Switching-UX bleibt.

### garrytan/gstack

- **Commits:** `a3259400 → 85fd9db5` (16 Commits)
- **Änderungen:** Auffällig sicherheitslastige Serie von v1.62 bis v1.68.3: Re-Pairing auf einen engeren Scope entzieht den alten Grant sofort, `tunnel revoke` existiert nachweislich und entfernt auch Setup-Keys, ein Security-Sweep zu externen Beiträgen härtete sechs Funde regressionsgepinnt ab, und Phantom-AskUserQuestion-Hooks werden durch kanonische Registrierung plus selbstheilende `settings.json` beseitigt. Dazu ein Bounded-Scope-Profil `gpt-5.6-sol` für Codex-Installationen und automatische Plan-Modus-Auswahl am Review-Gate.
- **Index:** Angepasst — die Sicherheitswelle, das Codex-Profil und die automatische Plan-Modus-Auswahl sind ergänzt; Rollen-Skills und Sprint-Zyklus bleiben unverändert beschrieben.

### github/spec-kit

- **Commits:** `f36634b5 → 27f50f7e` (203 Commits)
- **Änderungen:** Version 1.0.0 am 21.08.2026 — zum ersten Jahrestag des Projekts — und direkt danach 1.0.1. Damit verlässt Spec-Kit den Beta-Status. Dokumentationsseitig kamen ein Adoptionsleitfaden für bestehende Projekte, Workflow-Quickstarts, eine Projekt-Historie und eigenes Spec-Kit-Branding hinzu; funktional wurden Switch-Steps auf einen `cases`-Block verpflichtet und mehrere Bundler- und Preset-Validierungen verschärft.
- **Index:** Angepasst — der 1.0-Meilenstein und die neuen Einstiegsdokumente sind ergänzt.

### Graphify-Labs/graphify

- **Commits:** `ecfcd160 → b2cd3626` (205 Commits)
- **Änderungen:** Bis Version 0.9.48: `--no-dedup` erlaubt inkrementelle Merges ohne Fuzzy-Deduplizierung, der HTML-Export funktioniert wieder für große Graphen und bricht nicht mehr an einem Steuerzeichen im Label ab. Bei den LLM-Antworten werden hohle Antworten neu versucht statt bisektiert und JSON aus reasoning-first-Antworten wiederhergestellt; Markdown-Wikilinks werden vault-weit aufgelöst, wenn die Geschwister-Auflösung scheitert.
- **Index:** Unverändert — Zweck, Artefakte und die Einordnung als Quelle des lokal installierten `graphify`-Skills bleiben exakt gültig; die Änderungen sind Robustheits-Fixes. Bemerkenswert ist die vault-weite Wikilink-Auflösung, weil sie die Markdown- und Obsidian-Nutzung dieses Repos direkt betrifft.

### headroomlabs-ai/headroom

- **Commits:** `28aa53dc → 34a55175` (284 Commits)
- **Änderungen:** Releases bis 0.36.5: ChatGPT-Auth wird aus id_token-Claims erkannt, sodass `wrap` und `init` korrekt `requires_openai_auth` melden; `doctor` meldet projektbezogenes Claude-Routing statt eines falschen Negativs. Sicherheitsseitig werden vom Aufrufer gelieferte Upstreams auf jedem Auflösungspfad validiert, und Output-Tokens werden aus dem Stream-Text statt aus der Wire-Größe gezählt.
- **Index:** Unverändert — Architektur, Einsatzformen und die Einordnung der Benchmark-Angaben als Herstellerangaben bleiben zutreffend.

### intellectronica/ruler

- **Commits:** `82244744 → 0fa2caee` (12 Commits)
- **Änderungen:** Skills werden jetzt auch nach `.kiro/skills` propagiert; dazu mehrere Fixes zu den Issues #770, #776 und #778 und die Entfernung eines Codebase-Smells-Workflows aus der CI.
- **Index:** Angepasst — Kiro als Skill-Ziel und die auf über 30 gewachsene Adapterliste sind ergänzt.

### jakubkrehel/make-interfaces-feel-better

- **Commits:** `5f3c3c26 → 5a4076ac` (2 Commits)
- **Änderungen:** Eine `.gitattributes` und eine Kürzung der README (36 Zeilen entfernt, 2 hinzugefügt).
- **Index:** Unverändert — der Skill selbst und seine Referenzen sind unberührt.

### juliusbrussee/caveman

- **Commits:** `0d95a81d → 7bb71309` (145 Commits)
- **Änderungen:** Die dritte Generation des Lern-Teils ist der eigentliche Zuwachs: `caveman-learn` weist Spend und zugeschriebene Ersparnis aus, die CLI zeigt Learn-Spend, ein Savings-Ledger und Holdout-Berichte, und die Regel Spend-vs-Savings ist für den lokalen Learn-Lauf dokumentiert. Dazu Release 1.2.5 der CLI, ein mitten in der Session wiederbelebter lokaler Proxy, auf v2.3.1 gepinnte Shims und ein Support-Plan für Cursor Tier 1.
- **Index:** Angepasst — der Learn- und Evidence-Zweig mit Spend-vs-Savings-Ledger und Holdout-Berichten ist ergänzt, inklusive der erklärten Grenze, den Agenten nicht für Ersparnis dümmer zu machen.

### langchain-ai/openwiki

- **Commits:** `3076d557 → a525ed88` (92 Commits)
- **Änderungen:** „Grounded claims“ für selbstkorrigierende Code-Wikis, Integrationen für Coding-Agenten, vollständige Neu-Generierung von Repository-Wikis beim `init` und ein konfigurierbares Zustandsverzeichnis. Eine im Juli eingeführte Authoring-Architektur (Fan-out der Autorenschaft, mechanische Planvalidierung, aus der Quelle abgeleitete Seiten-Untergrenze) wurde nach kurzer Zeit wieder zurückgenommen.
- **Index:** Angepasst — grounded claims, die Agenten-Integrationen und das Neu-Generieren beim init sind ergänzt. Bemerkenswert: Die zurückgezogene Authoring-Architektur zeigt, wie beweglich das Projekt noch ist — die Risikoeinschätzung „junges Projekt“ bleibt damit ausdrücklich gültig.

### Leonxlnx/taste-skill

- **Commits:** `e988add2 → 72e29953` (9 Commits)
- **Änderungen:** Ausschließlich Sponsoring: React Bits und interfaces.dev als Sponsoren aufgenommen, Tiers standardisiert, Logos für Light- und Dark-Mode und Tracking-URLs.
- **Index:** Unverändert — keine inhaltliche Änderung an Skills oder Stilregeln.

### mattpocock/skills

- **Commits:** `2ab95809 → 5b15a47f` (138 Commits)
- **Änderungen:** Ein `implement-spec`-Skill ist als Work in Progress dazugekommen; der Engineering-Zweig deckt mit `to-spec`, `to-tickets`, `implement`, `wayfinder` und `triage` inzwischen die Kette von der Spezifikation zur Umsetzung ab. Zwei Regeländerungen sind als Pattern interessant: Skills dürfen keine anderen user-invoked Skills aufrufen, und das Repo hat alle Gedankenstriche entfernt, um Agenten von diesem KI-Schreibmuster wegzusteuern. Dazu ein Fix für SKILL.md-Beschreibungen mit unquotierten Doppelpunkten im YAML-Frontmatter.
- **Index:** Angepasst — die Kette von der Spezifikation zur Umsetzung und die beiden Regeländerungen sind ergänzt.

### microsoft/markitdown

- **Commits:** `fd239d5d → 9dc0d657`
- **Änderungen:** Ein einzelner Commit pinnt GitHub Actions auf vollständige Commit-SHAs.
- **Index:** Unverändert — Funktionsumfang, Risiken und Lizenz sind unberührt.

### millionco/react-doctor

- **Commits:** `5dc936e1 → bd084063` (134 Commits)
- **Änderungen:** React-bewusste Laufzeit-Traces in der CLI, Regeln zu UI-Library-Komposition und -Korrektheit hinter Capability-Gates, ein neuer `improve-threejs`-Skill und Berücksichtigung des React Compiler in den ESLint-Presets. Dazu Performance-Profiling der Regelausführung, ein Tiefenlimit gegen Stack-Overflow in der Funktionsauflösung und korrigierte flatMap-Empfehlungen.
- **Index:** Angepasst — Laufzeit-Traces, die neuen Regelgruppen und `improve-threejs` sind ergänzt; die Lizenz- und Telemetrie-Hinweise bleiben unverändert stehen.

### msitarzewski/agency-agents

- **Commits:** `8ef49232 → ebe9c99a` (2 Commits)
- **Änderungen:** Ein neuer „Economy Designer“ für Wirtschafts- und Anreizsysteme, dazu nachgeschärfte Reality-Checker- und SEO-Specialist-Agenten.
- **Index:** Angepasst — der Economy Designer ist in der Aufzählung neuerer Spezialisten ergänzt.

### nextlevelbuilder/ui-ux-pro-max-skill

- **Commits:** `4857a2c5 → bc826e22` (13 Commits)
- **Änderungen:** Ein Overhaul von Relevanzbewertung und kuratierten Design-Daten: Die UX-Richtlinien wuchsen von 98 auf 119, die Stil-Datenbank wurde dagegen von 84 auf 79 Einträge verdichtet und in 50 aktive plus passive Stile getrennt — also bewusst kuratiert statt vergrößert. Dazu ein `--global`-Flag und ein universelles `--ai`-Ziel in der CLI, `.prompt.md`-Erzeugung für VS Code Copilot, ein Style-Detail-Modal mit Phone-UI-Vorschau in der Galerie und automatisches Bumpen der Skill-JSON-Versionen nach Release.
- **Index:** Angepasst — alle Datenbankzahlen aktualisiert und die Kuration ausdrücklich als Verdichtung statt Wachstum beschrieben; CLI- und Galerie-Neuerungen ergänzt.

### NVIDIA/SkillSpector

- **Commits:** `34f60308 → 698e2bf2` (62 Commits)
- **Änderungen:** Patches 2.5.1 und 2.5.2 mit klarer Fail-closed-Linie: Bei nicht erreichbarem LLM-Provider bricht der Scan ab statt still zu degradieren, ein nur teilweiser LLM-Ausfall wird als „degraded“ gemeldet, die Aufnahme von Remote-URLs, ZIP-Archiven und Git-Repos ist vor der Verarbeitung begrenzt, verborgene ausführbare Dateien in verschachtelten Artefakten werden inspiziert, und die Posture von MCP-Registries wird neu geprüft. OSV-Advisories nutzen exakte Lockfile-Versionen und melden SC4 nur verifiziert. Dazu strukturierte Skill-Zusammenfassungen (Phase 1) und portiertes transitives Scanning.
- **Index:** Angepasst — die Fail-closed-Semantik, die begrenzte Ingestion, das MCP-Registry-Scanning und die präzisere OSV-Auflösung sind ergänzt. Für die eigene Skill-Prüfpraxis der relevanteste Zugewinn dieses Laufs.

### obra/superpowers

- **Commits:** `44c9b2d6 → b36e0829`
- **Änderungen:** Ein einzelner Release-Commit für v6.3.0: Devin CLI und Hermes Agent als neue Harnesses (Grok Build in der Installationsdoku), die Brainstorming-Zeremonie skaliert per Klassifikation in spike, bounded oder architectural, und in der subagentengetriebenen Entwicklung stallen Controller nicht mehr bei Plankonflikten — nicht-katastrophale Konflikte erhalten ein protokolliertes Ruling. Gleichartige Kleinaufgaben werden gebündelt, Implementer und Reviewer dürfen keine eigenen Subagenten starten, Pläne tragen einen `Spec:`-Zeiger, und das Entfernen eines Worktrees zerstört keine untracked Dateien mehr.
- **Index:** Angepasst — die Zusammenfassung beschreibt jetzt v6.3 statt v6.2. Besonders relevant für dieses Repo: Implementer und Reviewer dürfen keine eigenen Subagenten mehr starten, und Kleinaufgaben werden zu einem Dispatch gebündelt — beides deckt sich mit dem Abschnitt „Subagents und Token-Ökonomie“ in der eigenen AGENTS.md.

### open-gsd/gsd-core

- **Commits:** `4f6935e2 → 1178c5f9` (590 Commits)
- **Änderungen:** 590 Commits mit Schwerpunkt auf Nachweispflichten: ein Konsens-Gate für die `CYCLE_SUMMARY` bei mehreren Reviewern, Provenance-Pflicht für UI-SPEC-Komponenten-Inventare, ein erzwungenes Rollen-Register in `docs/INVENTORY.md` mit 32 nachgetragenen Lücken, ein Opt-in für absichtliche Löschungen beim Worktree-Cleanup und pro Modell aufgelöste Codex-Reasoning-Effort-Werte mit sichtbaren Clamps.
- **Index:** Angepasst — Konsens-Gate, Provenance-Pflicht, Rollen-Register und das Löschungs-Opt-in sind ergänzt; die Einschätzung „leistungsfähig, aber nicht mehr schlank“ bestätigt sich damit weiter.

### openai/codex

- **Commits:** `bdda5da5 → c9b19deb` (961 Commits)
- **Änderungen:** 961 Commits um zwei erkennbare Themen: „Guardian“-Review-Threads werden als eigene Thread-Art von Subagenten unterschieden und über Thread-Quellen-Metadaten klassifiziert; parallel werden Nutzereingaben und Kontextfragmente durchgängig mit Inhaltsarten annotiert, was Memory-Konsolidierung als eigene Anfrageart erkennbar macht und Annotationen beim Zusammenführen von Nachrichten erhält. Dazu das Abschalten resumierter Nachkommen beim Archivieren von Thread-Bäumen und ein entfernter Plan-Mode-Composer-Nudge.
- **Index:** Angepasst — Guardian-Reviews und die typisierten Inhaltsarten samt Memory-Konsolidierung sind ergänzt, weil sie die Architektur-Vergleichbarkeit mit Claude Code direkt betreffen.

### OthmanAdi/planning-with-files

- **Commits:** `b04ffd9c → 9e94390e` (37 Commits)
- **Änderungen:** Releases bis v3.11.2. Die Sprachvarianten liegen jetzt unter `skills/i18n`, damit das Plugin nur einen Skill registriert statt vieler Dubletten; das Planning-Opt-out wird auch auf der Cursor-Route und im deaktivierten Copilot-Hook respektiert. Mehrere Hook-Fixes betreffen POSIX-Shells: Hook-JSON wird per `printf` ausgegeben und der Copilot-Error-Hook über eine Pipe gefüttert, damit `dash` es parsen kann.
- **Index:** Angepasst — Versionsstand auf v3.11 aktualisiert, i18n-Bündelung und Opt-out-Respektierung ergänzt.

### paperclipai/paperclip

- **Commits:** `d5b9f6c8 → 16b59c93` (476 Commits)
- **Änderungen:** 476 Commits, im Kern eine neue Duplex-Bridge für Sandbox-Transporte: Broker mit gated Transport-Auswahl, sequenzierte Chunks mit Spill auf der Empfangsseite, ein prozesseigenes Byte-Ledger als Ressourcengrenze und Fail-closed-Verhalten bis in die CLI-Spur. Außerdem wurden automatische Übernahmen gestrandeter Tasks abgeschaltet, der Onboarding-Agent-Bogen neu gebaut und der Mission-Schritt aus dem Wizard entfernt.
- **Index:** Unverändert — die Einordnung als Control Plane für Agenten-Teams mit Governance-, Budget- und Audit-Fokus bleibt zutreffend; die Änderungen sind Transport- und Onboarding-Interna.

### pbakaus/impeccable

- **Commits:** `6b342244 → 56f44523` (250 Commits)
- **Änderungen:** 250 Commits, überwiegend wiederkehrende Synchronisierung generierter Provider-Ausgaben. Inhaltlich: Die Installation von Claude-Agenten wurde repariert, der abgeleitete Update-Scope bleibt erhalten, ein hängender Tune-Zustand ohne Parameter wurde behoben, toter Code im Design-Parser und ein veralteter Claude-MultiEdit-Matcher entfernt, und der manuelle Apply-Rollback wurde vereinfacht.
- **Index:** Unverändert — 23 Unterbefehle und 59 Detektor-Regeln stimmen weiterhin mit der README überein.

### router-for-me/CLIProxyAPI

- **Commits:** `a80e8082 → a7e3596b` (306 Commits)
- **Änderungen:** 306 Commits fast ausschließlich an den Format-Konvertern: Gemini normalisiert fehlerhafte Schema-Knoten und Claude-Thinking-Signaturen, OpenAI validiert und filtert Thought Signatures, Claude leitet eine stabile request-bezogene `metadata.user_id` ab, und xAI behält `image_generation` auf grok-4.6+ bzw. verwirft verwaiste `tool_choice`-Angaben. Dazu Credential-Metadaten-Normalisierung und Retry-Runden-Filterung bei der Authentifizierung.
- **Index:** Unverändert — Funktionsumfang und die deutliche Risikoeinschätzung (OAuth-Tokens, Account-Pools, Sponsor-Relays) bleiben unverändert gültig.

### rtk-ai/rtk

- **Commits:** `8a24ce2e → 29f9bb71` (71 Commits)
- **Änderungen:** 71 Commits, im Schwerpunkt die Argument-Erkennung für `git log`: `--stat` und `--numstat` forderten keinen Raw-Passthrough an, `--grep`-Werte wurden als Flags fehlerkannt, und mehrere Optionen (`-U`, `--unified`, `--expand-tabs`, `--max-parents`, `--diff-algorithm`) wurden falsch als wertkonsumierend behandelt. Dazu Benchmark-Fixes: Fixtures laufen über Loopback statt über mockhttp.org, und `benchmark.sh` löscht die getrackte Harness nicht mehr.
- **Index:** Unverändert — Zweck, Grenzen (eingebaute Read-, Grep- und Glob-Tools passieren den Bash-Hook nicht) und Telemetrie-Hinweis bleiben zutreffend.

### shadcn-ui/ui

- **Commits:** `efafb091 → ac60ef5c` (67 Commits)
- **Änderungen:** Neu im Monorepo ist `@shadcn/helpers` mit einem deklarativen `createChat`-Builder, der Konversationen inklusive Reasoning-, Tool-Call- und Streaming-Verläufen nachstellt — gedacht für Entwicklung und Tests von AI-Oberflächen. Die Registry-CLI unterstützt jetzt private GitHub-Registries; dazu ein großer Zulauf an Community-Registries im Directory und ein Fix, der beendete Spinner abmeldet.
- **Index:** Angepasst — `@shadcn/helpers` und die Unterstützung privater Registries sind ergänzt; die Warnung zu `scripts/sync-templates.sh` bleibt unverändert stehen.

### shanraisshan/claude-code-best-practice

- **Commits:** `e30c04a1 → d57ddc78` (236 Commits)
- **Änderungen:** 236 Commits, die dem Betriebsmuster dieses Repos entsprechen: tägliche Drift-Checks mit Changelog-Eintrag und Badge-Update bis v2.1.241. Inhaltlich wurden `/auto-mode-setup` und `/effort` in der Commands-Übersicht dokumentiert und die Workflow-Tabelle nachgezogen (u.a. Matt Pocock von 230k auf 232k Sterne, Skills von 35 auf 36).
- **Index:** Unverändert — der Eintrag beschreibt genau diese Charakteristik einer laufend aktualisierten Wissensbasis; die Zahlen im Repo ändern sich täglich und werden im Index bewusst nicht nachgeführt.

### teng-lin/notebooklm-py

- **Commits:** `7d0aa42c → 3bb0c185` (312 Commits)
- **Änderungen:** Release v0.8.1 mit Notebook-Collections auf Kontoebene (`client.collections` plus CLI-Gruppe), deutlich reicheren Quellen-Metadaten (Status- und Typ-Filter, exakte Zählungen, Drive-Health, Wortzahlen, Revisionsstempel), offset-genauen Zitationsdaten, mehr Projekt-, Chat- und Artefakt-Metadaten und einem eigenständigen `notebooklm research import`. Für die Cookie-Übernahme wurde von `rookiepy` auf `rookie-cookies` migriert und ein Cookie-Ablauf in Millisekunden korrekt auf Sekunden normalisiert.
- **Index:** Angepasst — Collections, die reicheren Metadaten, die offset-genauen Zitationen und die Cookie-Bibliotheksmigration sind ergänzt; die Warnung zu nicht dokumentierten Google-APIs und Session-Cookies bleibt zentral.

### thedaviddias/Front-End-Checklist

- **Commits:** `48405aaf → 30756a79` (4 Commits)
- **Änderungen:** Vier Commits, ausschließlich CI und Betrieb: Produktions-Deploys laufen über die gewählte CI, Content wird vor dem Typecheck generiert, in-flight geroutete Builds bleiben erhalten, und OpenPanel zeigt auf die selbst gehostete API.
- **Index:** Unverändert — 385 Regeln, 390 generierte Skills und MCP-Server sind unberührt.

### thedotmack/claude-mem

- **Commits:** `132b4634 → e2d1df56` (24 Commits)
- **Änderungen:** Ab v13.15 ist das Projekt deutlich stärker kommerzialisiert: Der Installer `npx claude-mem install` führt einen vollständigen Funnel für eine kostenlose CMEM-Pro-Woche durch (Pitch, E-Mail, Magic-Link, Stripe-Checkout, Pairing-Polling) und verlangt dafür eine Device-Code-Bestätigung im Browser, was laut Changelog eine Offenlegung des Pairing-Secrets schließt. Modellpreise werden live geladen statt hart kodiert. Außerdem warnt die Session am Start, wenn keine Beobachtungen mehr eintreffen, und der Gateway-Fehler-Envelope wird durchgereicht, statt Quota-Fehler endlos zu wiederholen. Stand v13.15.3.
- **Index:** Angepasst — der Trial-Funnel im Installer, der Device-Code-Mechanismus und die Observer-Health-Warnung sind ergänzt. Bemerkenswert und prüfrelevant: Ein Installer, der Stripe-Checkout und Konto-Pairing ausführt, ist ein anderer Eingriff als ein reines Memory-Plugin — das gehört vor jeder Nutzung in die Bewertung.

### upstash/context7

- **Commits:** `594a7313 → c3248289` (26 Commits)
- **Änderungen:** Ein Context7-Plugin für OpenCode, Clerk als ausgewiesener OAuth-Issuer im MCP-Server samt dokumentiertem Plugin-OAuth-Kommando und eine `context7.json` mit URL und Public Key. Dazu Integrationsleitfäden für OpenClaw, Gerrit und eve, aktualisierte Preisangaben für privates Parsing und OIDC statt statischer Credentials in der CI.
- **Index:** Angepasst — OpenCode-Plugin, Clerk-OAuth und die neuen Integrationsleitfäden sind ergänzt.

### vercel-labs/agent-skills

- **Commits:** `7c180d90 → dd089a8c` (7 Commits)
- **Änderungen:** Das Repo veröffentlicht einen Agent-Skills-Discovery-Index und richtet seine Discovery-Artefakte am Entwurf der Spezifikation aus; Skill-Frontmatter wird jetzt als YAML geparst. Dazu präzisierte Content-Readiness-Guidance und dokumentierte, vorab geladene Route-Transitions.
- **Index:** Angepasst — deutlich überarbeitet: Der Eintrag nannte acht Skills mit teils veralteten Namen. Aktuell sind es neun (`vercel-deploy-claimable` heißt jetzt `deploy-to-vercel`, `react-native-guidelines` heißt `react-native-skills`, neu ist `vercel-cli-with-tokens`), dazu der Discovery-Index und die ZIP-Artefakte je Skill.

### vercel-labs/skills

- **Commits:** `7cb7db64 → 435076e7` (34 Commits)
- **Änderungen:** Bis v1.5.23: ein Select-all-Schalter im Skill-Picker, Posit Assistant als weiterer unterstützter Agent, gesicherte Authentifizierung für private Repositories und mehrere Präzisierungen beim Install-Verhalten (interne Well-known-Skills bleiben vom Wildcard ausgeschlossen, `remove --all` wird verweigert, wenn zugleich einzelne Skills benannt sind, und ein Skill aus demselben Repo mit anderem Ref wird nicht mehr gelöscht).
- **Index:** Angepasst — Select-all, Posit Assistant, die Authentifizierung für private Repos und die schärferen Install-Grenzen sind ergänzt. Relevant, weil dies das Standardwerkzeug für die Installation praktisch aller anderen Repos im Index ist.

### VoltAgent/awesome-design-md

- **Commits:** `664b3e78 → 8147538b`
- **Änderungen:** Ein Commit, ausschließlich README: zwei neue Sponsoren-Banner (EveryFeed, LaunchKit) und ein ausgetauschtes Bild.
- **Index:** Unverändert — keine neuen DESIGN.md-Dateien; der bestehende Hinweis auf die starke kommerzielle Prägung des README bestätigt sich.

### wshobson/agents

- **Commits:** `c4b82b0a → 2b49247f` (27 Commits)
- **Änderungen:** Ein neues `avoid-ai-writing`-Plugin gegen typische KI-Schreibmuster und ein Breaking Change, der das Gemini-CLI-Ziel auf die Google-Antigravity-CLI als Harness umstellt. Die Garden-Prüfungen kontrollieren jetzt Komponenten-Zahlen und Agenten-Divergenz, `plugin-eval` füllt `model_usage` aus Judge- und Monte-Carlo-Ebene und löst verschachtelte Skill-Referenzen auf. Echte-CLI-Smoke-Tests laufen nicht mehr im normalen Testziel mit.
- **Index:** Angepasst — Zahlen auf 92 Plugins, 202 Agenten, 181 Skills und 105 Commands korrigiert; `avoid-ai-writing`, die Antigravity-Migration und die erweiterten Garden-Prüfungen sind ergänzt. Bemerkenswert: Plugins, Agenten und Commands sind gesunken, Skills gestiegen — das Repo konsolidiert offenbar in Richtung Skills.

### mleibetseder/ai-llm-wiki (separat unter `external_knowledge/`)

- **Commits:** `bd8f3d9 → 0761bb3` (24 Commits)
- **Änderungen:** Der größte Ausbau bisher. Der Rohbestand wuchs von 161 auf 213 Artikel (plus unverändert 24 PDFs), das Wiki von 250 auf 334 `concept-*`-Seiten, von 96 auf 107 `entity-*` und von 14 auf 15 `paper-*`. Inhaltlich neu sind vor allem die Kataloge „Awesome AI Handbook“ und „Awesome Agentic Patterns“, Intent-Driven Development samt Outcome-Oriented Design, eine Verification Layer, Agent Security und Red-Teaming, Agent-Native Memory sowie die Unterscheidung von geteiltem und isoliertem Speicher, Agent Engineering Principles, Inference Engineering, Loop Engineering und das SkillsBench-Paper. Auch die OpenWiki-Ankündigung ist eingearbeitet — dasselbe Projekt liegt als [langchain-ai/openwiki](#langchain-aiopenwiki) im Index.
- **Index:** Angepasst — Metadaten und Struktur von Hand nachgezogen (die Felder dieses Eintrags sind als `<!-- manual -->` markiert und werden vom Script bewusst nicht gepflegt) und die Inhaltsbeschreibung auf den neuen Ausbau umgeschrieben. Bemerkenswert: Die Dateizahl springt von 764 auf 2.121 und die Größe von 262M auf 531M, weil erstmals das komplette Rohmaterial eingecheckt wurde — der Klon ist damit deutlich schwerer geworden.

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
