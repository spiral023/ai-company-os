# Deny-Rules-statt-CLAUDE-md-Empfehlung

**Konfidenz:** mehrfach-belegt

## Zweck

Verhindert, dass Secret-Schutz nur auf dem Papier existiert. Adressiert die verbreitete Scheinsicherheit, ein Hinweis wie „lies niemals .env“ in der Agent-Datei sei bereits ein Sicherheitsmechanismus.

## Funktionsweise

Ein Hinweis in `CLAUDE.md`/`AGENTS.md` ist Teil des Kontextes und damit reine Empfehlung (Advisory) — bei komplexen oder mehrdeutigen Aufgaben kann der Agent trotzdem darauf zugreifen. Echte Sicherheit beginnt erst dort, wo ein Zugriff *vor* dem Modell technisch blockiert wird, über eine globale Deny-Liste in `~/.claude/settings.json` (z.B. `Read(**/.env*)`, `Read(**/*.pem)`, `Read(**/secrets/**)`, `Read(**/.ssh/**)` plus entsprechende `Write`-Deny-Regeln). Vier Leckpfade müssen dabei separat bedacht werden: (1) direkter File-Read — durch Deny-Regeln zuverlässig abfangbar; (2) Runtime-Output-Capture — Tests/App/Scripts geben Secrets im Output aus, der in den Conversation-Kontext gezogen wird, Deny-Regeln greifen hier nicht; (3) Search-/Grep-Treffer, die Secrets in Suchergebnissen sichtbar machen; (4) **Command Smuggling über Shell-Wrapper** — ein naiver Präfix-Filter lässt sich umgehen, wenn mehrere Befehle in einem einzigen `bash -c "cmd1 && cmd2"`-Aufruf verpackt werden. Gegenmaßnahme ist ein Parser (z. B. Tree-sitter), der die Kette in Einzelbefehle zerlegt und jeden separat prüft, sofern sie nur aus einfachen Wörtern und sicheren Operatoren besteht — bei Variablen, Wildcards oder Control-Flow bleibt der gesamte Aufruf ein einziger, konservativ eingestufter Block. Für Pfad 2 hilft eine separate `.env.test` mit garantiert falschen Dummy-Werten, damit Runtime-Output nie etwas Reales enthalten kann. Ergänzend: ein Pre-Commit-Hook, der nach Secret-Mustern sucht (`sk-ant-`, `sk-live-`, `ghp_`, `AKIA`, `BEGIN.*PRIVATE KEY`), und für besonders sensible Projekte Container-Isolation, bei der produktive `.env`-Dateien im Container gar nicht existieren.

## Vorteile

- Verschiebt Sicherheit von „sollte nicht“ zu „kann technisch nicht“ — robust auch gegenüber Fehlinterpretation oder Drift des Modells bei komplexen Aufgaben.
- Adressiert alle drei Leckpfade statt nur des offensichtlichsten (Direct Read), der allein meist schon als „gelöst“ wahrgenommen wird.
- Kombinierbar mit normalem Arbeits-Workflow (Deny-Regeln blockieren nur Secrets, nicht normale Read/Edit/Test-Workflows).

## Nachteile & Grenzen

- Deny-Regeln lösen nur direkte Dateioperationen — sie verhindern nicht, dass Runtime-Output oder Suchergebnisse Secrets zeigen, wenn keine Dummy-Werte und Pre-Commit-Scans ergänzt werden.
- Pflegeaufwand: Deny-Liste muss bei neuen Secret-Pfaden/-Formaten aktiv erweitert werden.
- Container-Isolation ist für viele Projekte zu aufwendig, um sie durchgängig einzusetzen.

## Wann einsetzen, wann nicht

- Einsetzen: sobald Claude Code oder ein anderer Coding Agent Zugriff auf ein Projekt mit echten Credentials, Datenbank-Zugängen oder Client-Daten hat.
- Nicht einsetzen: reine Spielwiesen-/Lernprojekte ohne jegliche echte Secrets — dort ist der Aufwand nicht nötig, sollte aber vor dem ersten echten Secret nachgezogen werden.

## Belege

- 2026-04-30 · [[2026-04-30-zodchiii-claude-code-env-security]] · meinung — X-Post beschreibt die drei Leckpfade, die konkrete Deny-Liste, `.env.test`-Muster und Pre-Commit-Hook-Signaturen.
- 2026-02-28 · [[2026-02-28-openai-codex-rules-guide]] · meinung — OpenAI Codex Rules generalisieren das Prinzip produktseitig auf beliebige Shell-Befehle (`forbidden` > `prompt` > `allow`) und liefern den vierten Leckpfad: Command Smuggling über verpackte Shell-Aufrufe, mit Tree-sitter-Splitting als Gegenmaßnahme und einer klar benannten Fallback-Grenze.
- 2026-05-13 · [[2026-05-13-david-wiesen-openai-codex-windows-sandbox]] · meinung — Bestätigt „Empfehlung ≠ Durchsetzung“ auf Netzwerkebene: ein rein advisory Proxy-Variablen-Schutz ließ sich von nicht kooperativem Code umgehen, erst eine durchsetzende, an einen eigenen Windows-Principal gebundene Firewall-Regel schloss die Lücke.
- 2026-02-01 · [[2026-02-01-anthropic-docs-claude-code-gitlab-ci]] · meinung — Dieselbe Grundregel für CI-Umgebungen: API-Keys niemals committen, sondern über maskierte CI/CD-Variablen oder OIDC/Workload-Identity-Federation statt statischer Keys im Repo beziehen.
- 2026-02-02 · [[2026-02-02-unsloth-team-claude-code-local-llm]] · meinung — `--dangerously-bypass-approvals-and-sandbox` in Codex CLI hebt Bestätigungen und Sandbox vollständig auf — Gegenbeispiel für den Preis, wenn die Advisory-vs-Enforcement-Grenze selbst abgeschaltet wird.
- 2026-08-04 · [[2026-08-04-anthropic-docs-claude-code-best-practices]] · meinung — Anthropics „Auto Mode“ (dynamischer Klassifikator pro Befehl) ist ein zur statischen Deny-Liste komplementärer, nicht ersetzender Mechanismus — ein Klassifikator-Fehlurteil bleibt möglich, eine technisch verdrahtete Deny-Regel nicht umgehbar.

## Spannungen & offene Fragen

- Die ursprüngliche Einzelquelle ist inzwischen durch fünf weitere, organisatorisch unabhängige Quellen (OpenAI-Doku, OpenAI-Engineering-Blog, Anthropic-Doku ×2, Unsloth-Tutorial) auf verschiedenen Plattformen (Claude Code, Codex CLI, GitLab CI) bestätigt — die Konfidenz wurde entsprechend angehoben.
- Offene Frage: Wie lässt sich diese Deny-Liste standardmäßig in neue Projekt-Setups (z.B. unsere `create_project_kit.py`-Vorlagen) integrieren, statt sie bei jedem Projekt neu aufzusetzen?

## Verwandte Patterns

- [[AGENTS-md-Onboarding-Design]]
- [[Erweiterungs-Ebenen-Zuordnung]]
