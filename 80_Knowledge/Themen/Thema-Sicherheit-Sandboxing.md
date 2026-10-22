# Sicherheit & Sandboxing

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-22. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Technisch erzwungene Grenzen statt Empfehlungen: Deny-Regeln, Sandboxes, Secrets, Permissions, Plugin-Vertrauen, Sicherheit bei Vibe-Coding-Apps. Berichte über Gefahren, Missbrauch und konkrete KI-Vorfälle stehen in ki-risiken.

## Suchbegriffe

- **Hauptkeyword:** Claude Code Sicherheit
- **Long-Tail:** Deny Rules statt CLAUDE.md; .env Secrets Claude Code schützen; Agent Sandbox einrichten; Docker Sandbox Claude Code; Codex Execpolicy; Vibe Coding Sicherheit
- **Fragen:** Wie verhindere ich, dass der Agent meine .env liest? / Reicht eine Regel in CLAUDE.md?
- **Häufig in den Quellen:** row level security (3), security (3), sicherheit (3), sandbox (3), os-level sandboxing (3), mxc (3), security checker (2), docker sandboxes (2), deny-rules (2), command smuggling (2), agent sandbox (2), ki-vertragsprüfung (2), produktedition (2), freigaben (2), playwright (2), sandboxing (2), prompt injection (2), process isolation (2), sandbox permissions (2), vibe coding security (2)

## Verwandte Themen

- [[Thema-Hooks-MCP-Erweiterungs-Ebenen]] — Hooks, MCP & Erweiterungs-Ebenen
- [[Thema-Autonome-Läufe-Loops-CI]] — Autonome Läufe, Loops & CI
- [[Thema-Prototyping-UI-Design]] — Prototyping & UI-Design
- [[Thema-AI-nativer-SDLC]] — AI-nativer SDLC
- [[Thema-KI-Risiken-Sicherheitsvorfälle]] — KI-Risiken & Sicherheitsvorfälle

## Patterns (6)

- [[Adversarialer-Pre-Launch-Check]] · meinung · 8 Belege
- [[Agent-Rechte-umfassen-Kommunikationswege]] · meinung · 5 Belege
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]] · mehrfach-belegt · 13 Belege
- [[Freigaben-und-Isolation-getrennt-steuern]] · meinung · 9 Belege
- [[KI-Dienste-nach-Vertrag-und-Datenfluss-pruefen]] · meinung · 1 Belege
- [[Sandbox-Komposition-aus-OS-Primitiven]] · meinung · 7 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[CI-Agent-mit-Review-Gate]], [[Externe-Evaluatoren-mit-dauerhaftem-Zugang]], [[Hook-Entscheidungstyp-nach-Pruefbarkeit]], [[Metrikband-gestufte-Agent-Autonomie]], [[Quellen-Bookmarks-fuer-Agent-Automationen]], [[Review-Autonomie-mit-Shadow-Mode-und-Stichproben]]

## Quellen (17)

- [[2026-10-16-voxyz_ai-2111079716832886886]] — Vox schlägt einen Pre-Launch-Test mit normalen Konten A und B sowie einem Admin vor.
- [[2026-10-10-satyanadella-2108931348857827686]] — Satya Nadella argumentiert im X-Artikel für eine Architektur, die leistungsfähige Modelle wie potenzielle Insider-Risiken behandelt.
- [[2026-10-09-openaidevs-2108573188703781190]] — OpenAI Developers meldet am 09.10.2026 einen neuen `Codex`-Sandboxmodus mit `Microsoft Execution Containers` (`MXC`) unter Windows.
- [[2026-10-08-unslothai-windows-sandboxing-mxc]] — Unsloth kündigt eine Integration von Microsoft eXecution Container (`MXC`) für die Ausführung von Code unter Windows an.
- [[2026-09-29-suraj_sharma14-2104790775397830755]] — Suraj Sharma listet 30 knappe Sicherheitsmaßnahmen für KI-generierte Apps.
- [[2026-09-29-openclaw-openclaw-enterprise-the-open-agent-platform-open]] — Herstellerankündigung der OpenClaw Foundation: Open-Source-Control-Plane für persistente Agenten in sensiblen Umgebungen, vor 1.0, nutzbar für interne Piloten.
- [[2026-09-27-voxyz_ai-2104224555040452925]] — Vox beschreibt einen Pre-Launch-Check für Claude Code (Modellname im Tweet: Opus 5.5): Vier Subagents haben nur die Aufgabe, die eigene App zu brechen, und teilen sich 16 feste Prüffragen.
- [[2026-08-19-openai-2090165328290701800]] — OpenAI kündigt am `2026-08-19` Private Safety Processing als Vorschau an.
- [[2026-08-18-docker-2089789519788728379]] — MicroVM-Isolation mit eigenem Kernel pro Sandbox gilt laut Docker inzwischen als empfohlener Standardpfad für Claude Code, ist aber nur als Herstellermeldung belegt.
- [[2026-08-14-claudedevs-2088332927189049738]] — ClaudeDevs meldet am `2026-08-14` den Rollout von Auto mode als Standard für Pro, Max und Team.
- [[2026-08-07-claude-auto-mode-is-now-the-default-in-claude-code-for]] — Anthropic begründet den Auto-Mode mit Messungen gegen tatsächlich beobachtetes Freigabeverhalten.
- [[2026-07-14-vischer-teil-31-ki-tools-wie-es-um-den-schutz-der-daten]] — Die VISCHER-Autoren David Rosenthal, Lucian Hunger und Jonas Baeriswyl beurteilen KI-Angebote am `14.07.2026` anhand konkreter Vertrags- und Konfigurationskombinationen.
- [[2026-05-13-david-wiesen-openai-codex-windows-sandbox]] — Kein einzelnes OS-Feature reichte für eine Agent-Sandbox; sie wurde aus mehreren Primitiven komponiert, und rein advisory Netzwerkschutz genügt nicht.
- [[2026-04-30-zodchiii-claude-code-env-security]] — Nur Deny-Regeln in settings.json erzwingen Zugriffssperren, CLAUDE.md-Hinweise sind Empfehlungen; Secrets lecken auch über Runtime-Output und Grep-Treffer.
- [[2026-02-28-openai-codex-rules-guide]] — Eine Grenze wirkt nur, wenn eine Regel-Engine sie vor der Ausführung erzwingt; Codex Rules zerlegen verpackte Shell-Aufrufe, um Command Smuggling zu verhindern.
- [[2026-02-05-d4m1n-docker-sandboxes]] — Docker Sandboxes isolieren Agent-CLIs per Micro-VM und machen YOLO-Modus und nächtliche Ralph-Loop-Läufe sicher, ohne den Host zu gefährden.
- [[2026-02-04-lovable-docs-lovable-security-guide]] — Secrets und Autorisierung gehören ins Backend, Row Level Security früh setzen; die Verantwortung für Sicherheit bleibt beim Builder, nicht beim Tool.

## Quellen mit diesem Thema als Nebenthema

- [[2026-10-17-voxyz_ai-2111442102756463077]]
- [[2026-10-15-mardehaym-2110763129885835505]]
- [[2026-10-11-developers-codex-as-a-platform-build-on-the-open-agent-harn]]
- [[2026-10-09-voxyz_ai-2108573215224160393]]
- [[2026-10-07-alex-sprogis-t3-code-endlich-eine-steuerzentrale-fuer-alle-de]]
- [[2026-10-02-repo-thedaviddias-front-end-checklist]]
- [[2026-09-27-anthropic-academy-sdlc-playbook]]
- [[2026-09-18-akshay_pachaar-2101037514945597645]]
- [[2026-08-28-the-morpheus-der-huggingface-hack-ist-jetzt-untersucht]]
- [[2026-07-27-anthropic-our-position-on-open-weights-models]]
- [[2026-07-21-claude-how-anthropic-secures-its-ai-native-software-dev]]
- [[2026-07-16-amasad-2077802290304684404]]
- [[2026-04-17-wiki-compiler-lovable-design-debugging-sicherheit]]
- [[2026-04-16-wiki-compiler-superpowers]]
- [[2026-02-28-openai-codex-multi-agents-guide]]
