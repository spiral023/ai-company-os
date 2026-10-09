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
- 2026-01-21 · [[2026-01-21-aiedge-claude-50-pro-tips]] · meinung — Negatives Anschauungsbeispiel für exakt das Kernproblem dieses Patterns: Die genannten Cowork-Sicherheitshinweise (Ordner-Isolation, Bestätigung vor Löschung, Backup vorher) sind ausschließlich Prompt-Formulierungen — reine Empfehlung, keine technische Durchsetzung. Die Quelle thematisiert diese Lücke selbst nicht.
- 2026-01-22 · [[2026-01-22-hooeem-claude-code-7-schritte-plan]] · meinung — Konkretes Pre-Hook-Beispiel: Ein Skript beendet sich mit Exit-Code 2 und schreibt die Begründung nach `stderr`, sobald ein `read`/`grep`-Aufruf den Pfad `.env` enthält — die `stderr`-Ausgabe ist entscheidend, weil nur so die Blockade an das Modell zurückgefüttert wird.
- 2026-01-31 · [[2026-01-31-bcherny-claude-code-team-tips]] · meinung — Team routet Berechtigungsanfragen an ein stärkeres Modell (Opus 4.5), das sie auf Angriffsmuster scannt und sichere Anfragen automatisch freigibt — deckt sich inhaltlich mit dem bereits belegten „Auto Mode“-Klassifikator, hier als interne Teampraxis vor dessen Produktveröffentlichung.
- 2026-02-01 · [[2026-02-01-anthropic-docs-automate-workflows-with-hooks]] · meinung — Anthropics eigenes `.env`-Schutzbeispiel für `PreToolUse`-Hooks demonstriert ungewollt die Lücke dieses Patterns: Es prüft nur `tool_input.file_path` per Substring-Match und deckt damit ausschließlich den Leckpfad „direkter Write“ ab — nicht Read über andere Tools, nicht Runtime-Output-Capture, nicht Search-Treffer und nicht Command-Smuggling. Ein `PreToolUse`-Hook ist derselbe Enforcement-Punkt wie eine `permissions.deny`-Regel, verschiebt aber Zuverlässigkeit von der Plattform auf selbst zu schreibende Skriptlogik.
- 2026-05-09 · [[2026-05-09-zodchiii-15-claude-code-settings-most-developers]] · meinung — Explizite Allow-/Deny-Liste (.env, .ssh, rm -rf, sudo, git push) als Permissions-Baseline; Sekundärquelle, Autorenmeinung ohne Messung.
- 2026-08-19 · [[2026-08-19-matt-pocock-live-uncle-bob-on-software-fundamentals-in-the-a]] · meinung — Lange Regeldokumente werden laut Martin wie Richtlinien behandelt (lost in the middle); deterministische Tools verschwinden nicht aus der Aufmerksamkeit. Stützt das Prinzip, nicht die konkrete Deny-Mechanik.

- 2026-10-08 · [[2026-10-08-unslothai-windows-sandboxing-mxc]] · meinung — Unsloths Low-Stufe führt String-, AST- und Regex-Prüfungen aus, High ergänzt OS-Isolation für Python und Terminal. Das erweitert die Trennung von Prompt-Empfehlung und technischer Kontrolle um zwei unterschiedliche Kontrollschichten; Robustheit der Filter und OS-Grenzen ist nicht im Code geprüft.

## Spannungen & offene Fragen

- Die ursprüngliche Einzelquelle ist inzwischen durch fünf weitere, organisatorisch unabhängige Quellen (OpenAI-Doku, OpenAI-Engineering-Blog, Anthropic-Doku ×2, Unsloth-Tutorial) auf verschiedenen Plattformen (Claude Code, Codex CLI, GitLab CI) bestätigt — die Konfidenz wurde entsprechend angehoben.
- Offene Frage: Wie lässt sich diese Deny-Liste standardmäßig in neue Projekt-Setups (z.B. unsere `create_project_kit.py`-Vorlagen) integrieren, statt sie bei jedem Projekt neu aufzusetzen?
- Spannung (2026-09-29): [[2026-09-07-sairahul1-2096902575035683147]] und [[2026-09-14-developers-rethinking-skills-and-prompts-for-gpt-6-astra-op]] behaupten, harte Verbotssprache in Prompts lasse GPT-6 Astra zu früh stoppen. Das betrifft Prompt-Formulierungen, nicht technisch erzwungene Deny-Regeln, und ist unbelegt. Offen bleibt, ob die Empfehlung, Verbote im Prompt weicher zu fassen, die Wirksamkeit technischer Grenzen berührt.

- 2026-10-09: Technische Softwarefilter sind mehr als eine Empfehlung, aber weder eine Filterliste noch ein High-Schalter beweist eine belastbare OS-Sicherheitsgrenze. Unsloths eigener Windows-Screenshot nennt eine Preview-Einschränkung. Full access hebt laut Quelle beide Kontrollschichten auf. → [[2026-10-08-unslothai-windows-sandboxing-mxc]]

## Verwandte Patterns

- [[AGENTS-md-Onboarding-Design]]
- [[Erweiterungs-Ebenen-Zuordnung]]
- [[Freigaben-und-Isolation-getrennt-steuern]]
