# Corporate Baseline für AI Coding Agents

**Stand:** 2026-08-29
**Zweck:** Besprechungsgrundlage für ein unternehmensweites Baseline-Setup (Workspace Settings, Repo Settings, Rules) für Claude Code und OpenAI Codex.
**Status:** Entwurf zur Diskussion — die Vorschläge in Abschnitt 9 sind noch nicht beschlossen.

---

## 0. Wie dieses Dokument in der Besprechung genutzt wird

- **Abschnitte 1–3** sind der gemeinsame Rahmen — kurz durchgehen, damit alle dieselbe Landkarte haben.
- **Abschnitte 4–7** sind Nachschlagewerk (Herstellerdoku, verdichtet). In der Besprechung nur bei Bedarf öffnen.
- **Abschnitt 8** ist der Vergleich Claude Code ↔ Codex.
- **Abschnitt 9** enthält die konkreten Baseline-Vorschläge in drei Ausbaustufen.
- **Abschnitt 10** ist die eigentliche Agenda: neun Entscheidungen, die wir treffen müssen.
- **Abschnitt 11** listet offene Fragen und Risiken, die wir bewusst nicht entscheiden können.

---

## 1. Das Kernprinzip: Empfehlung ist keine Durchsetzung

Der wichtigste Satz für die Besprechung:

> Ein Hinweis in `CLAUDE.md` oder `AGENTS.md` ist Kontext für das Modell — also eine **Empfehlung**. Eine Regel in `managed-settings.json` oder `requirements.toml` greift **vor** dem Modell — das ist **Durchsetzung**.

Ein Satz wie „lies niemals `.env`" in der Agent-Datei ist Scheinsicherheit: Bei komplexen oder mehrdeutigen Aufgaben kann der Agent trotzdem zugreifen. Beide Hersteller haben dieses Prinzip inzwischen produktseitig verankert — Anthropic mit der Managed-Settings-Ebene, OpenAI mit `requirements.toml` und den Codex Rules.

**Konsequenz für unser Baseline:** Alles, was wirklich gelten muss, gehört in die durchgesetzte Ebene. Die Agent-Datei ist für Arbeitsweise und Kontext da, nicht für Sicherheit.

**Vier Leckpfade, die man dabei getrennt betrachten muss** (aus unserem Pattern [Deny-Rules-statt-CLAUDE-md-Empfehlung](../Patterns/Deny-Rules-statt-CLAUDE-md-Empfehlung.md)):

1. **Direkter File-Read** — durch Deny-Regeln zuverlässig abfangbar.
2. **Runtime-Output-Capture** — Tests oder die App geben Secrets im Output aus, der in den Kontext wandert. Deny-Regeln greifen hier **nicht**. Gegenmaßnahme: separate `.env.test` mit garantiert falschen Dummy-Werten.
3. **Search-/Grep-Treffer** — Suchergebnisse machen Secrets sichtbar.
4. **Command Smuggling** — mehrere Befehle in einem `bash -c "cmd1 && cmd2"` umgehen naive Präfix-Filter. Beide Tools zerlegen Ketten inzwischen (Claude Code kennt die Shell-Operatoren `&&`, `||`, `;`, `|`, `|&`, `&` und Newline; Codex nutzt Tree-sitter) — aber nur bei einfachen Befehlen ohne Variablen, Wildcards oder Control-Flow.

**Wichtige Einschränkung, die Anthropic selbst dokumentiert:** Read- und Edit-Deny-Regeln gelten für die eingebauten Datei-Tools und für Datei-Befehle, die Claude Code in Bash erkennt (`cat`, `head`, `tail`, `sed`). Sie gelten **nicht** für beliebige Subprozesse — ein Python- oder Node-Skript, das die Datei selbst öffnet, wird nicht erfasst. Dafür braucht es die Sandbox (OS-Ebene).

---

## 2. Die fünf Erweiterungsebenen — was gehört wohin?

Damit ein Setup nicht dieselbe Anforderung dreifach modelliert (Agent-Datei + Skill + Hook), brauchen wir eine klare Zuordnung. Aus unserem Pattern [Erweiterungs-Ebenen-Zuordnung](../Patterns/Erweiterungs-Ebenen-Zuordnung.md):

| Anforderung | Ebene | Begründung |
|---|---|---|
| „Gilt immer" (Projektkonventionen, Guardrails) | Agent-Datei (`AGENTS.md` / `CLAUDE.md`) | Permanent im Kontext — muss deshalb kurz bleiben |
| „Wiederkehrender Ablauf" | Skill | Progressive Disclosure: Inhalt lädt erst bei Aktivierung |
| „Isolierte Teilaufgabe" | Subagent | Eigener Kontext, eng gescopte Rechte |
| „Immer derselbe Trigger" | Hook | Deterministisch, kein Reasoning nötig |
| „Externe Quelle/Aktion" | MCP | Integrationsschicht, nicht Arbeitslogik |

**Litmus-Test für den häufigsten Grenzfall (Agent-Datei vs. Skill):** „Möchte ich, dass diese Instruktion auch gilt, wenn ich gerade nicht aktiv daran denke?" → Ja: Agent-Datei. Nein: Skill.

**Kostenhinweis:** Jeder Skill kostet rund 100 Wörter (Name + Beschreibung) permanent im Kontext, bevor überhaupt ein Trigger feuert. MCP-Server laden ihre Tool-Schemas in **jede** Anfrage, unabhängig davon, ob sie gebraucht werden. Praxis-Faustregel aus den Quellen: viele MCPs konfiguriert, aber unter 10 aktiv und unter 80 Tools aktiv.

---

## 3. Die vier Ebenen eines Corporate Setups

```
┌─ Ebene 1: ORGANISATION (durchgesetzt, Admin)
│  Claude Code: managed-settings.json / MDM / claude.ai-Konsole
│  Codex:       requirements.toml (hart) + managed_config.toml (Defaults)
│  → Secrets-Sperren, Login-Bindung, Modell-Allowlist, MCP-Allowlist, Telemetrie
│
├─ Ebene 2: REPOSITORY (geteilt, eingecheckt)
│  Claude Code: .claude/settings.json
│  Codex:       .codex/config.toml (nur in trusted Projekten)
│  → Projekt-Permissions, Hooks, Sandbox-Domains, Plugin-Marketplace
│
├─ Ebene 3: AGENT-DATEI (Kontext, eingecheckt)
│  AGENTS.md (führend) + CLAUDE.md (Zeiger darauf)
│  → Was/Warum/Wie: Stack, Struktur, Test- und Verifikationspfade
│
└─ Ebene 4: ENTWICKLER (persönlich, nicht eingecheckt)
   ~/.claude/settings.json, .claude/settings.local.json, ~/.codex/config.toml
   → Modellwahl, Effort, Terminal, persönliche Allow-Regeln
```

Die entscheidende Eigenschaft: **Ebene 1 kann von unten nicht überschrieben werden.** Ebene 2–4 können nur zusätzlich einschränken, nicht lockern.

---

## 4. Claude Code — was der Hersteller vorgibt

*Quelle: offizielle Anthropic-Dokumentation, abgerufen 2026-08-29.*

### 4.1 Settings-Präzedenz (höchste zuerst)

1. **Managed Settings** — `managed-settings.json`, MDM oder claude.ai-Konsole (Organisation)
2. **Kommandozeile** — `claude --settings` (Session)
3. **Projekt lokal** — `.claude/settings.local.json` (persönlich, pro Projekt)
4. **Projekt geteilt** — `.claude/settings.json` (eingecheckt, alle im Projekt)
5. **User** — `~/.claude/settings.json` (persönlich, alle Projekte)

**Wichtig:** Deny-Regeln aus *jeder* Ebene schlagen Allow-Regeln aus *jeder* Ebene. Ein User-Deny blockiert ein Projekt-Allow. Ein Managed-Deny lässt sich auch mit `--allowedTools` nicht aufheben. Arrays wie `permissions.allow`/`deny` mergen über alle Quellen — Entwickler können also erweitern, aber nichts wegnehmen. Ausnahmen: `fallbackModel`, `availableModels` und `modelPicker` ersetzen statt zu mergen.

### 4.2 Ausrollmechanismen und exakte Pfade

| Mechanismus | Wo | Priorität | Plattform |
|---|---|---|---|
| Server-managed | claude.ai Admin-Konsole (Teams/Enterprise) oder self-hosted Gateway | Höchste | Alle |
| plist / Registry-Policy | macOS: `com.anthropic.claudecode` · Windows: `HKLM\SOFTWARE\Policies\ClaudeCode` (Wert `Settings`, `REG_SZ`) | Hoch | macOS, Windows |
| Datei-basiert | macOS: `/Library/Application Support/ClaudeCode/managed-settings.json` · Linux/WSL: `/etc/claude-code/managed-settings.json` · Windows: `C:\Program Files\ClaudeCode\managed-settings.json` | Mittel | Alle |
| User-Registry | `HKCU\SOFTWARE\Policies\ClaudeCode` | Niedrigste | nur Windows |

**Für uns relevante Details:**

- Der alte Windows-Pfad `C:\ProgramData\ClaudeCode\managed-settings.json` wird **nicht mehr gelesen**. Viele Blog-Anleitungen im Netz sind hier veraltet.
- `HKCU` ist ohne Adminrechte beschreibbar → **kein Durchsetzungskanal**, nur ein Komfort-Default.
- **WSL liest standardmäßig nur `/etc/claude-code`.** Damit Windows-Policies auch in WSL greifen, muss `wslInheritsWindowsSettings: true` in einer der Windows-Admin-Quellen gesetzt sein. Für uns wichtig, wenn Entwickler unter Windows in WSL arbeiten.
- Server-managed Settings werden beim Start geholt und **stündlich** aktualisiert; MDM/Registry alle 30 Minuten; Datei-basiert bei Änderung.
- Standardmäßig gilt **`first-wins`**: Claude Code nimmt die höchstrangige Quelle, die mindestens einen Policy-Key liefert, und **ignoriert die anderen** — kein Merge. Wer mehrere Quellen kombinieren will, muss `managedSourcesBehavior: "merge"` in der höchstrangigen Quelle setzen (ab v2.1.242).
- Mehrere Teams können sich eine Policy teilen: `managed-settings.d/10-telemetry.json`, `20-security.json` usw. werden alphabetisch nach `managed-settings.json` gemerged.
- Verifikation: `/status` zeigt die Zeile `Setting sources` mit `Enterprise managed settings (file|HKLM|remote)`.
- Starter-Templates für Jamf, Intune und Group Policy liegen unter `anthropics/claude-code/tree/main/examples/mdm`.

### 4.3 Was sich durchsetzen lässt (Auszug aus „Decide what to enforce")

| Kontrolle | Keys |
|---|---|
| Permission-Regeln | `permissions.allow`, `permissions.deny`, `permissions.ask` |
| Permission-Lockdown | `allowManagedPermissionRulesOnly`, `permissions.disableBypassPermissionsMode` |
| Start-Permission-Modus | `permissions.defaultMode`, `permissions.disableAutoMode` |
| Sandboxing | `sandbox.enabled`, `sandbox.network.allowedDomains`, `sandbox.network.allowManagedDomainsOnly` |
| Org-weite CLAUDE.md | Datei am Managed-Policy-Pfad — kann nicht ausgeschlossen werden |
| MCP-Kontrolle | `allowedMcpServers`, `deniedMcpServers`, `allowManagedMcpServersOnly`, `managed-mcp.json` |
| Plugin-Marketplaces | `strictKnownMarketplaces`, `blockedMarketplaces`, `disableSideloadFlags`, `disableCommandPluginSources` |
| Customization-Lockdown | `strictPluginOnlyCustomization` (Skills/Agents/Hooks/MCP nur aus Plugins oder Managed Settings) |
| Hook-Restriktionen | `allowManagedHooksOnly`, `allowedHttpHookUrls` |
| Login-Bindung | `forceLoginMethod`, `forceLoginOrgUUID` |
| Modell-Restriktionen | `availableModels`, `enforceAvailableModels` |
| Versions-Untergrenze | `minimumVersion` (blockt Downgrade), `requiredMinimumVersion` (verweigert Start) |
| Telemetrie-Opt-out | `env` mit `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` |
| Aufbewahrung | `cleanupPeriodDays` |

**Der wichtigste Satz aus dieser Doku-Seite:** *„Denying WebFetch blocks Claude's fetch tool, but if Bash is allowed, `curl` and `wget` can still reach any URL. Sandboxing closes that gap with a network domain allowlist enforced at the OS level."*

Permission-Regeln und Sandbox decken also **verschiedene Schichten** ab. Wer nur Permissions setzt, hat kein Netzwerk-Gate.

### 4.4 Permission-Regelsyntax — inklusive Fallstricke

Format: `Tool` oder `Tool(specifier)`.

```json
{
  "permissions": {
    "allow": ["Bash(npm run *)", "Bash(git commit *)"],
    "ask":   ["Bash(git push *)"],
    "deny":  ["Read(./.env)", "Read(./secrets/**)", "Bash(curl *)"]
  }
}
```

**Wildcard-Regeln, die man kennen muss:**

- Der `*` steht für beliebigen Text **inklusive Leerzeichen**. `Bash(git * main)` matcht auch `git push origin main` — der Stern muss **nach** dem Subkommando stehen.
- `Bash(ls *)` matcht auch das nackte `ls` (nur bei einzelnem Trailing-Wildcard). `Bash(ls*)` ohne Leerzeichen matcht auch `lsof`.
- `Bash(*)` ist äquivalent zu `Bash`.

**Pfadmuster (gitignore-Syntax) — häufige Fehlerquelle:**

| Muster | Bedeutung |
|---|---|
| `//pfad` | Absolut ab Dateisystem-Wurzel |
| `~/pfad` | Ab Home-Verzeichnis |
| `/pfad` | Relativ zur **Settings-Quelle** — *nicht* absolut! |
| `pfad` oder `./pfad` | Relativ zum aktuellen Verzeichnis |

`/Users/alice/file` ist also **kein** absoluter Pfad. Für absolut braucht es `//Users/alice/file`.

**Weitere dokumentierte Fallstricke:**

- Zusammengesetzte Befehle: Jedes Teilkommando muss unabhängig matchen. `Bash(safe-cmd *)` erlaubt **nicht** `safe-cmd && other-cmd`.
- Wrapper werden gestrippt (`timeout`, `time`, `nice`, `nohup`, `stdbuf`, `command`, `builtin`, `noglob`, flagloses `xargs`) — Environment-Runner wie `npx`, `docker exec`, `devbox run`, `mise exec` **nicht**. `Bash(devbox run *)` erlaubt damit auch `devbox run rm -rf .`.
- Argument-basierte Filter sind fragil. Anthropic warnt explizit: `Bash(curl http://github.com/ *)` umgeht man mit Optionen davor, anderem Protokoll, Redirects oder Variablen. Empfehlung des Herstellers: `curl`/`wget` per Deny blocken und stattdessen `WebFetch(domain:...)` nutzen.
- Für `Write`, `NotebookEdit`, `Glob` oder `MultiEdit` geschriebene Pfadregeln werden **akzeptiert, aber nie ausgewertet**. Immer `Edit(...)` und `Read(...)` verwenden.
- Ein eingebauter Satz Read-only-Befehle (`ls`, `cat`, `grep`, `find`, `git status` …) läuft in jedem Modus ohne Prompt und ist **nicht konfigurierbar**. Wer davon einen blocken will, braucht eine explizite `ask`- oder `deny`-Regel.
- Output-Redirections (`>`, `>>`, `2>`) werden als Datei-Write gegen die `Edit`-Regeln geprüft.

**Workspace Trust:** `permissions.allow` und `additionalDirectories` aus einer eingecheckten `.claude/settings.json` greifen erst, **nachdem** der Entwickler den Trust-Dialog für den Ordner akzeptiert hat. `deny` und `ask` greifen sofort. In `claude -p`- und SDK-Sessions erscheint der Dialog nie — dort werden Projekt-Allow-Regeln gar nicht angewandt, `.mcp.json`-Server dagegen ohne Rückfrage verbunden. **Das ist für unsere CI-Nutzung relevant.**

### 4.5 Sandboxing

OS-Ebene, greift für Bash-Befehle und deren Kindprozesse (macOS, Linux, WSL2). Die wichtigsten Keys:

- `sandbox.enabled`, `sandbox.failIfUnavailable` (Start verweigern, wenn Sandbox nicht verfügbar)
- `sandbox.allowUnsandboxedCommands: false` (kein Retry außerhalb der Sandbox)
- `sandbox.filesystem.allowWrite` / `denyRead` / `denyWrite` / `allowManagedReadPathsOnly`
- `sandbox.network.allowedDomains` / `deniedDomains` / `strictAllowlist` / `allowManagedDomainsOnly`
- `sandbox.credentials.files` und `.envVars` — Credential-Dateien und Umgebungsvariablen in der Sandbox blocken oder maskieren

`sandbox.credentials` adressiert direkt unseren Leckpfad 2 (Runtime-Output-Capture) — das ist neu gegenüber unserem bisherigen Wissensstand und sollte im Baseline berücksichtigt werden.

### 4.6 Monitoring und Kosten

OpenTelemetry-Export per `env`-Block, damit unternehmensweit ausrollbar:

```json
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_LOGS_EXPORTER": "otlp",
    "OTEL_EXPORTER_OTLP_PROTOCOL": "grpc",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "http://collector.example.com:4317"
  }
}
```

Metriken u. a.: `claude_code.session.count`, `claude_code.cost.usage` (USD), `claude_code.token.usage`, `claude_code.lines_of_code.count`, `claude_code.commit.count`, `claude_code.code_edit_tool.decision`, `claude_code.active_time.total`.
Events u. a.: `user_prompt`, `api_request`, `tool_decision`, `tool_result`, `auth`, `mcp_server_connection`.
Attribute auf allen Daten: `session.id`, `user.id`/`user.email`, `organization.id`, `prompt.id`.

`OTEL_LOG_USER_PROMPTS=1` und `OTEL_LOG_TOOL_DETAILS=1` sind **standardmäßig aus** — bewusste Datenschutzentscheidung, die wir treffen müssen (siehe Entscheidung E7).

Zusätzlich ohne eigene Infrastruktur: Analytics-Dashboard unter `claude.ai/analytics/claude-code` (Teams/Enterprise) bzw. `platform.claude.com/claude-code` (Console), plus Spend-Limits in den Admin-Settings.

---

## 5. OpenAI Codex — was der Hersteller vorgibt

*Quelle: offizielle OpenAI-/ChatGPT-Learn-Dokumentation, abgerufen 2026-08-29.*

### 5.1 Konfigurationshierarchie (höchste zuerst)

1. Cloud-managed Requirements (Policy-Bundle beim ChatGPT-Login)
2. macOS MDM Requirements (`com.openai.codex`, Key `requirements_toml_base64`)
3. System-`requirements.toml`
4. Managed Defaults (`managed_config.toml`)
5. CLI-Flags und `--config`-Overrides
6. Profile (`~/.codex/<name>.config.toml`, per `--profile`)
7. Projekt-`.codex/config.toml` (Repo-Wurzel abwärts, nächstes gewinnt — **nur in trusted Projekten**)
8. User-`~/.codex/config.toml`
9. Eingebaute Defaults

**Wichtig:** Untrusted Projekte überspringen **alle** projektbezogenen Ebenen. Vertrauen wird in `config.toml` gesetzt:

```toml
[projects."/absolute/path/to/project"]
trust_level = "trusted"
```

### 5.2 Zwei Admin-Dateien — harte Grenzen vs. weiche Defaults

| Datei | Zweck | Pfad Unix | Pfad Windows |
|---|---|---|---|
| `requirements.toml` | **Harte Constraints**, nicht überschreibbar | `/etc/codex/requirements.toml` | `%ProgramData%\OpenAI\Codex\requirements.toml` |
| `managed_config.toml` | **Weiche Defaults**, überschreibbar | `/etc/codex/managed_config.toml` | `~/.codex/managed_config.toml` |

> ⚠️ Der Windows-Pfad für `managed_config.toml` steht laut Doku im User-Profil, was für eine Admin-Datei inkonsistent wirkt. **Vor einem Rollout auf einer Testmaschine verifizieren.**

Auslieferung: Dateisystem, Cloud-Policy-Bundle (beim ChatGPT-Login auf unterstützten Plänen) oder macOS-MDM über die Domain `com.openai.codex` mit `config_toml_base64` und `requirements_toml_base64`.

### 5.3 Was `requirements.toml` erzwingen kann

- `allowed_approval_policies` — schränkt die wählbaren Approval-Policies ein
- `allowed_sandbox_modes` — schränkt die wählbaren Sandbox-Modi ein
- `allowed_approvals_reviewers` — legt fest, welche Reviewer verfügbar sind (eine unerlaubte Entwicklerwahl wird **still** überschrieben)
- `allowed_permission_profiles` — kontrolliert Zugriff auf Permission-Profile
- `allowed_web_search_modes`
- `[mcp_servers]` — MCP-Allowlist per Name **und Identität** (Command oder URL)
- `[rules]` — Befehlsregeln; die `decision` darf hier nur `prompt` oder `forbidden` sein (ein Admin kann also nur einschränken, nie lockern)
- `[permissions.filesystem]` — Deny-Read-Pfade und Globs
- `[features]` — Feature-Flags pinnen (`browser_use`, `computer_use`, `plugins` …)
- `[experimental_network]`, `[computer_use]`, `[hooks]`, `[marketplaces]`
- `allow_appshots`, `allow_remote_control`

Beispiele aus der Doku:

```toml
allowed_approval_policies = ["untrusted", "on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

[mcp_servers.docs]
identity = { command = "codex-mcp" }

[mcp_servers.remote]
identity = { url = "https://example.com/mcp" }

[features]
browser_use = false
computer_use = false
plugins = false
```

Eigene Permission-Profile lassen sich definieren und erzwingen:

```toml
default_permissions = "acme_review_only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
acme_review_only = true

[permissions.acme_review_only]
description = "Review code without modifying the workspace."
extends = ":read-only"
```

### 5.4 Sandbox- und Approval-Modi

**Sandbox-Modi** (`sandbox_mode`):

- `read-only` — nur Lesen; Änderungen und Ausführung brauchen Freigabe
- `workspace-write` — Lesen/Schreiben und Befehle im Arbeitsverzeichnis; **kein Netzwerk standardmäßig**
- `danger-full-access` — keine Beschränkungen (nicht empfohlen)

Geschützte Pfade innerhalb der Writable Roots bleiben read-only: `.git`, `.agents`, `.codex`.

**Approval-Policies** (`approval_policy`):

- `untrusted` — sichere Leseoperationen laufen automatisch, zustandsändernde brauchen Freigabe
- `on-request` — Freigabe bei Sandbox-Eskalation, Netzwerkzugriff und destruktiven Aktionen
- `never` — keine Rückfragen (mit Vorsicht)
- granular:

```toml
approval_policy = { granular = {
  sandbox_approval = true,
  rules = true,
  mcp_elicitations = true,
  request_permissions = false,
  skill_approval = false
} }
```

**Auto-Review als zusätzliche Schicht:** `approvals_reviewer = "auto_review"` leitet freigabepflichtige Anfragen an einen automatischen Reviewer-Agenten, der auf Daten-Exfiltration, Credential-Probing, Schwächung von Sicherheitsmechanismen und destruktive Aktionen prüft. Er lehnt kritische Risiken ab. Die Policy ist per `guardian_policy_config` in den Managed Requirements durch eine eigene ersetzbar.

Das ist konzeptionell dasselbe wie Anthropics Auto Mode (Klassifikator pro Befehl) — und in beiden Fällen gilt: **komplementär zur statischen Deny-Liste, kein Ersatz**. Ein Klassifikator kann fehlurteilen, eine verdrahtete Deny-Regel nicht.

**Codex Rules** (`~/.codex/rules/*.rules`, Starlark): deklarative Präfix-Regeln mit `allow` / `prompt` / `forbidden`; der restriktivste Treffer gewinnt. `match`/`not_match`-Listen dienen als Unit-Tests der Regel selbst. Vor dem Scharfschalten testbar mit:

```bash
codex execpolicy check --pretty --rules <pfad> -- <befehl>
```

Nach dem Anlegen einer Regeldatei muss Codex neu gestartet werden.

### 5.5 Managed Defaults — Beispiel aus der Doku

```toml
approval_policy = "on-request"
sandbox_mode = "workspace-write"

[sandbox_workspace_write]
network_access = false

[otel]
environment = "prod"
exporter = "otlp-http"
log_user_prompt = false
```

Weitere relevante Keys für ein Baseline: `model`, `model_reasoning_effort`, `web_search`, `project_doc_max_bytes`, `[shell_environment_policy.filters]` (dort sind `AWS_*` und `AZURE_*` bereits per Default ausgeschlossen), `[history] persistence`, `forced_chatgpt_workspace_id`, `forced_login_method`, `[windows] sandbox = "unelevated"`.

---

## 6. Die Repo-Ebene: AGENTS.md und CLAUDE.md

### 6.1 Wie beide Tools laden

**Codex** baut eine Instruktionskette:
1. Global: `~/.codex/AGENTS.override.md`, dann `~/.codex/AGENTS.md`
2. Projekt: von der Git-Wurzel bis zum aktuellen Verzeichnis, pro Ebene erst Override-, dann Standarddatei
3. Reihenfolge pro Verzeichnis: `AGENTS.override.md`, `AGENTS.md`, `TEAM_GUIDE.md`, `.agents.md`
4. Näher am aktuellen Verzeichnis = später im Prompt = **gewinnt bei Konflikten**
5. Größenlimit `project_doc_max_bytes`, Default **32 KiB** — danach wird abgeschnitten

**Claude Code** kennt fünf Ablageorte (Home, Projekt, `.local.md`, Parent, Child); Child-Dateien laden bei Bedarf nach. Zusätzlich kann eine org-weite `CLAUDE.md` am Managed-Policy-Pfad ausgerollt werden, die sich **nicht** ausschließen lässt.

### 6.2 Was hineingehört — und was nicht

Aus unserem Pattern [AGENTS-md-Onboarding-Design](../Patterns/AGENTS-md-Onboarding-Design.md), belegt durch mehrere unabhängige Quellen:

**Die Datei beantwortet drei Fragen:** Was (Stack, Struktur, Einstiegspunkte) — Warum (Zweck der zentralen Teile) — Wie (Arbeitsweise, Test-/Build-/Verifikationspfade).

**Harte Regeln:**

- **Kurz halten.** Ein Frontier-Modell befolgt zuverlässig ~150–200 Instruktionen; der Claude-Code-System-Prompt verbraucht davon bereits ~50. Empfehlung aus der Praxis: unter 300 Zeilen.
- **Nicht auto-generieren.** Eine ETH-Zürich-Studie (AGENTbench, 138 Instanzen über 12 Repos) zeigt: LLM-generierte Context-Files **senken** die Erfolgsquote gegenüber gar keinem Kontext und erhöhen die Kosten um über 20 %. Menschlich geschriebene bringen +4 %. Ursache: Redundanz vs. Additivität.
- **„Schreibe für die Lücke, nicht für den Überblick."** Nur was der Agent nicht selbst aus dem Code ableiten kann.
- **Stil- und Formatregeln gehören nicht hinein**, sondern in Formatter, Linter, Typechecker und Tests. Ein LLM ist dafür langsamer, teurer und unzuverlässiger als ein Tool.
- **Begründung mitliefern** („Use TypeScript strict mode because …") statt bloßer Anweisung.
- **Verweise auf Dateien/Zeilen** sind robuster als kopierte Snippets.

**Multi-Agent-Kostenfaktor:** In einem Agent-Team lädt jeder Teammate die Datei unabhängig. Bleibt sie vage, exploriert jeder Teammate die Codebase eigenständig — N Teammates erzeugen den N-fachen Tokenverbrauch für dieselbe Kontext-Erschließung.

### 6.3 Ein Regelwerk für mehrere Tools

Wenn im Haus Claude Code, Codex und ggf. Copilot/Cursor parallel laufen, ist die Frage: eine Quelle oder mehrere Dateien?

**Option A — `AGENTS.md` als führende Datei**, `CLAUDE.md` enthält nur einen Zeiger darauf. Genau so macht es dieses Repo bereits. Kein Tooling nötig, funktioniert sofort. `AGENTS.md` ist inzwischen ein Standard unter dem Dach der Linux Foundation, laut deren Angaben in über 60.000 Open-Source-Projekten im Einsatz.

**Option B — [Ruler](https://github.com/intellectronica/ruler)** (`@intellectronica/ruler`, MIT, aktuell Beta): zentrale Regelbasis in `.ruler/`, die automatisch in die tool-spezifischen Konfigurationsdateien verteilt wird. Unterstützt verschachtelte `.ruler/`-Verzeichnisse für kontextspezifische Instruktionen. Liegt bereits unter [external_repos/intellectronica/ruler](../../external_repos/intellectronica/ruler/README.md).

**Empfehlung:** Mit Option A starten. Ruler erst einführen, wenn wirklich mehr als zwei Tools produktiv genutzt werden — der Beta-Status ist für eine Corporate-Baseline sonst ein unnötiges Risiko.

---

## 7. Bestehendes internes Material

Was wir im Repo schon haben und in der Besprechung referenzieren können:

| Thema | Dokument |
|---|---|
| Ebenen-Zuordnung | [Erweiterungs-Ebenen-Zuordnung](../Patterns/Erweiterungs-Ebenen-Zuordnung.md) |
| Secrets & Durchsetzung | [Deny-Rules-statt-CLAUDE-md-Empfehlung](../Patterns/Deny-Rules-statt-CLAUDE-md-Empfehlung.md) |
| Agent-Datei-Design | [AGENTS-md-Onboarding-Design](../Patterns/AGENTS-md-Onboarding-Design.md) |
| Hooks | [Hook-Entscheidungstyp-nach-Pruefbarkeit](../Patterns/Hook-Entscheidungstyp-nach-Pruefbarkeit.md), [Hook-erzwungene-Skill-Aktivierung](../Patterns/Hook-erzwungene-Skill-Aktivierung.md) |
| Sandbox | [Sandbox-Komposition-aus-OS-Primitiven](../Patterns/Sandbox-Komposition-aus-OS-Primitiven.md) |
| Autonomiegrenzen | [Freiheitsgrad-nach-Aufgaben-Fragilitaet](../Patterns/Freiheitsgrad-nach-Aufgaben-Fragilitaet.md) |
| Review-Gates in CI | [CI-Agent-mit-Review-Gate](../Patterns/CI-Agent-mit-Review-Gate.md), [Plan-first-mit-getrenntem-Review](../Patterns/Plan-first-mit-getrenntem-Review.md) |
| Freigabegrenzen (Ist-Stand) | [10_Company/Freigabe_Policy.md](../../10_Company/Freigabe_Policy.md), [Entscheidungsrechte.md](../../10_Company/Entscheidungsrechte.md) |
| Projekt-Vorlagen | [40_Project_Kits/](../../40_Project_Kits/) — drei Kits mit `AGENTS.md`, `CLAUDE.md`, `docs/SECURITY.md` |

**Erkannte Lücke:** In keinem der Projekt-Kits gibt es bisher eine `settings.json`- oder `config.toml`-Vorlage. Die Deny-Listen existieren nur als Prosa im Pattern. Das ist der konkreteste umsetzbare Punkt aus dieser Besprechung.

---

## 8. Vergleich Claude Code ↔ Codex

| Aspekt | Claude Code | OpenAI Codex |
|---|---|---|
| Admin-Datei | `managed-settings.json` (JSON) | `requirements.toml` (hart) + `managed_config.toml` (weich) |
| Ausrollwege | Datei, MDM/Registry, claude.ai-Konsole, Gateway | Datei, macOS-MDM, Cloud-Policy-Bundle |
| Zentrale Fernverwaltung | Ja (claude.ai-Konsole, stündlicher Refresh) | Ja (Cloud-Policy beim Login) |
| Gruppen-Targeting | Konsole noch nicht; per Datei/Profil oder Gateway (per IdP-Gruppe) | über MDM-Profile |
| Permission-Modell | allow/ask/deny-Regeln pro Tool + Modi | Approval-Policy + Sandbox-Modus + Rules + Permission-Profile |
| Netzwerk-Gate | Sandbox-Domain-Allowlist (OS-Ebene) | `sandbox_workspace_write.network_access`, `[experimental_network]` |
| Automatische Risikoprüfung | Auto Mode (Klassifikator) | Auto-Review / Guardian-Policy |
| Regel-Testbarkeit vor Rollout | `/status`, `claude doctor` | `codex execpolicy check`, `match`/`not_match` in `.rules` |
| Agent-Datei | `CLAUDE.md` (+ org-weite Managed-Variante) | `AGENTS.md`-Kette, 32 KiB Limit |
| Telemetrie | OpenTelemetry (Metriken + Events), Analytics-Dashboard | `[otel]`-Block, `log_user_prompt` default aus |
| Versionskontrolle | `minimumVersion`, `requiredMinimumVersion/Maximum` | nicht dokumentiert gefunden |

**Beobachtung für die Diskussion:** Die Architekturen sind bemerkenswert konvergent — beide Hersteller sind unabhängig auf dasselbe Muster gekommen: eine unüberschreibbare Admin-Ebene, eine Sandbox auf OS-Ebene, ein Klassifikator für Grauzonen. Ein einheitliches internes Rahmenwerk ist deshalb realistisch; nur die Syntax unterscheidet sich.

---

## 9. Vorschlag: Baseline in drei Stufen

Der Gedanke: nicht alles auf einmal durchsetzen, sondern gestaffelt nach Sensibilität des Repos. **Stufe 1 gilt überall, Stufe 2 ist der Regelfall, Stufe 3 für regulierte oder kundendatenhaltige Projekte.**

### Stufe 1 — Minimum (gilt ausnahmslos für jedes Repo)

Ziel: Secrets können technisch nicht abfließen, und wir wissen, was läuft.

**Claude Code, `managed-settings.json`:**

```json
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(**/.env*)",
      "Read(**/*.pem)",
      "Read(**/*.key)",
      "Read(**/secrets/**)",
      "Read(**/.ssh/**)",
      "Edit(**/.env*)",
      "Edit(**/secrets/**)",
      "Bash(curl *)",
      "Bash(wget *)"
    ],
    "disableBypassPermissionsMode": "disable"
  },
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_LOGS_EXPORTER": "otlp",
    "OTEL_EXPORTER_OTLP_PROTOCOL": "grpc",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "http://<unser-collector>:4317"
  },
  "requiredMinimumVersion": "<aktuell freigegebene Version>",
  "cleanupPeriodDays": 30
}
```

**Codex, `/etc/codex/requirements.toml`:**

```toml
allowed_approval_policies = ["untrusted", "on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

[permissions.filesystem]
deny_read = ["**/.env*", "**/*.pem", "**/*.key", "**/secrets/**", "**/.ssh/**"]
```

**Codex, `/etc/codex/managed_config.toml`:**

```toml
approval_policy = "on-request"
sandbox_mode = "workspace-write"

[sandbox_workspace_write]
network_access = false

[otel]
environment = "prod"
exporter = "otlp-http"
log_user_prompt = false
```

**Flankierend (nicht Settings, aber Teil der Stufe):**
- `.env.test` mit garantiert falschen Dummy-Werten in jedem Projekt (schließt Leckpfad 2)
- Pre-Commit-Hook mit Secret-Signaturen: `sk-ant-`, `sk-live-`, `ghp_`, `AKIA`, `BEGIN.*PRIVATE KEY`
- `.env` in `.gitignore`

> Hinweis zur Genauigkeit: Der exakte Key-Name in `[permissions.filesystem]` ist aus der Doku-Zusammenfassung als „deny-read paths/glob patterns" beschrieben; die genaue Schreibweise ist vor dem Rollout an der Konfigurationsreferenz zu prüfen.

### Stufe 2 — Standard (Regelfall für interne Produktentwicklung)

Zusätzlich zu Stufe 1:

```json
{
  "allowManagedPermissionRulesOnly": false,
  "allowedMcpServers": [ { "serverUrl": "https://<freigegebener-server>/*" } ],
  "allowManagedMcpServersOnly": true,
  "strictKnownMarketplaces": [
    { "source": "github", "repo": "<unsere-org>/approved-plugins" }
  ],
  "disableSideloadFlags": true,
  "sandbox": {
    "enabled": true,
    "network": {
      "allowedDomains": ["registry.npmjs.org", "github.com", "pypi.org"]
    }
  },
  "availableModels": ["opus", "sonnet"],
  "forceLoginMethod": "claudeai",
  "forceLoginOrgUUID": ["<unsere-org-uuid>"]
}
```

Plus auf Repo-Ebene eine eingecheckte `.claude/settings.json` pro Projekt mit den projektspezifischen Allow-Regeln (`Bash(npm run *)` etc.), einem `PreToolUse`-Hook und den Sandbox-Domains, die dieses Projekt wirklich braucht.

### Stufe 3 — Reguliert (Kundendaten, Auth, Billing, Tenant-Isolation)

Zusätzlich zu Stufe 2:

```json
{
  "allowManagedPermissionRulesOnly": true,
  "allowManagedHooksOnly": true,
  "strictPluginOnlyCustomization": true,
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "allowUnsandboxedCommands": false,
    "network": { "allowManagedDomainsOnly": true, "strictAllowlist": true },
    "filesystem": { "allowManagedReadPathsOnly": true }
  },
  "cleanupPeriodDays": 7,
  "permissions": { "defaultMode": "plan" }
}
```

Codex-Äquivalent: eigenes Permission-Profil per `requirements.toml`, `allowed_sandbox_modes = ["read-only"]` für Review-Repos, `[features]` mit `plugins = false`, `guardian_policy_config` mit unserer eigenen Review-Policy.

Flankierend: Container-Isolation (Dev Container), in der produktive `.env`-Dateien gar nicht existieren; Review-Gate in der CI vor jedem Merge.

---

## 10. Entscheidungen für die Besprechung

| # | Entscheidung | Optionen | Vorschlag |
|---|---|---|---|
| **E1** | Welche Tools unterstützen wir offiziell? | nur Claude Code · nur Codex · beide · beide + Copilot | **Beide** — die Architekturen konvergieren, ein gemeinsames Rahmenwerk ist machbar |
| **E2** | Über welchen Kanal rollen wir aus? | claude.ai-Konsole · MDM/Intune · Datei im Image · Kombination | **Intune/GPO für Windows** (adminrechtgeschützt, providerunabhängig), Konsole zusätzlich für claude.ai-Nutzer |
| **E3** | Welche Ausbaustufe ist der Default? | Stufe 1 · Stufe 2 | **Stufe 2**, Stufe 3 nur für definierte Repo-Klassen |
| **E4** | Wer pflegt die Baseline? | Security · Platform/DevOps · verteiltes Ownership | Ein benannter Owner + `managed-settings.d/`-Split pro Team |
| **E5** | Wie klassifizieren wir Repos in Stufe 2 vs. 3? | Manuell per Liste · Label im Repo · nach Datenklassifizierung | An bestehende Datenklassifizierung koppeln, falls vorhanden |
| **E6** | MCP-Server: Allowlist ab wann? | sofort · nach Pilot · vorerst nicht | **Nach Pilot** — vorher wissen wir nicht, welche wirklich gebraucht werden |
| **E7** | Loggen wir Prompts (`OTEL_LOG_USER_PROMPTS`)? | ja · nein · nur in Stufe 3 | **Nein** — Betriebsrat/Datenschutz vorher klären, Default ist bewusst aus |
| **E8** | Ein Regelwerk oder mehrere? | `AGENTS.md` führend · Ruler · pro Tool getrennt | **`AGENTS.md` führend**, `CLAUDE.md` als Zeiger — Ruler zurückstellen |
| **E9** | Wie verhindern wir CLAUDE.md-Wildwuchs? | Review-Pflicht · Längenlimit · Auto-Generierung verbieten | Alle drei; Auto-Generierung (`/init`) explizit untersagen |

**Zusätzlich zu klären, aber keine Baseline-Entscheidung:** Wer trägt die Kosten (zentral vs. Kostenstelle), und welche Spend-Limits setzen wir initial?

---

## 11. Offene Fragen und Risiken

1. **Windows-Pfad für Codex `managed_config.toml`** steht laut Doku im User-Profil (`~/.codex/`). Das ist als Admin-Kanal untauglich. Vor Rollout auf einer Testmaschine verifizieren; ggf. ausschließlich über `requirements.toml` und MDM arbeiten.
2. **WSL-Abdeckung.** Wenn Entwickler unter Windows in WSL arbeiten, greift ohne `wslInheritsWindowsSettings: true` keine Windows-Policy. Außerdem sind Prozesse in der WSL-2-Utility-VM für Windows-seitige EDR-Sensoren nicht sichtbar — das ist ein Punkt für die IT-Security, nicht für uns allein.
3. **`claude -p` und SDK-Sessions.** Dort erscheint kein Trust-Dialog: Projekt-Allow-Regeln greifen nicht, `.mcp.json`-Server werden aber ohne Rückfrage verbunden. Für CI-Pipelines brauchen wir eine eigene Vorgabe (`--setting-sources user` oder `--bare`).
4. **`first-wins` überrascht.** Wer parallel Konsole *und* MDM ausrollt, bekommt standardmäßig nur eine Quelle angewandt — nicht das Merge, das man intuitiv erwartet. Entweder bewusst nur einen Kanal nutzen oder `managedSourcesBehavior: "merge"` setzen (setzt Mindestversion voraus).
5. **Versionsdrift.** Viele der genannten Keys haben Mindestversionen (v2.1.208 bis v2.1.242). Ohne `requiredMinimumVersion` ist nicht garantiert, dass eine Policy auf jeder Maschine überhaupt greift.
6. **Argument-basierte Bash-Filter sind fragil** — der Hersteller sagt das selbst. Unsere Deny-Liste sollte auf Programmnamen und Pfade setzen, nicht auf Argumentmuster.
7. **Kein Ersatz für Code-Review.** Alle hier beschriebenen Mechanismen begrenzen, was der Agent *tun* kann — nicht, ob das Ergebnis richtig ist.
8. **Blog-Quellen im Netz sind teils veraltet** (z. B. der alte Windows-Pfad `C:\ProgramData\ClaudeCode\`). Für den Rollout ausschließlich die Herstellerdoku als Referenz nehmen.

---

## 12. Vorgeschlagene nächste Schritte

1. Entscheidungen E1–E9 in der Besprechung treffen und hier festhalten.
2. Baseline Stufe 1 als konkrete Dateien schreiben und auf **einer** Testmaschine je Betriebssystem verifizieren (`/status` bzw. `codex execpolicy check`).
3. Pilot mit 3–5 Entwicklern über zwei Wochen; Telemetrie auswerten, welche Deny-Regeln real stören.
4. Baseline in die Projekt-Kits übernehmen (`40_Project_Kits/*/.claude/settings.json` und `.codex/config.toml`), damit `create_project_kit.py` sie automatisch ausrollt — das schließt die offene Frage aus dem Deny-Rules-Pattern.
5. `10_Company/Freigabe_Policy.md` um eine Team-Perspektive erweitern (Rollen, Onboarding, Audit).
6. Nach dem Pilot über Stufe 2 und die MCP-Allowlist entscheiden.

---

## 13. Quellen

**Anthropic (offizielle Dokumentation, abgerufen 2026-08-29)**
- [Claude Code Settings](https://code.claude.com/docs/en/settings)
- [Settings Reference](https://code.claude.com/docs/en/settings-reference)
- [Deploy managed settings](https://code.claude.com/docs/en/managed-settings)
- [Set up Claude Code for your organization](https://code.claude.com/docs/en/admin-setup)
- [Configure permissions](https://code.claude.com/docs/en/permissions)
- [Example settings files](https://code.claude.com/docs/en/settings-example)
- [Security](https://code.claude.com/docs/en/security)
- [Authentication](https://code.claude.com/docs/en/iam)
- [Monitoring usage](https://code.claude.com/docs/en/monitoring-usage)
- [MDM-Beispiele (Jamf, Intune, GPO)](https://github.com/anthropics/claude-code/tree/main/examples/mdm)
- [Beispiel-Settings](https://github.com/anthropics/claude-code/tree/main/examples/settings)

**OpenAI (offizielle Dokumentation, abgerufen 2026-08-29)**
- [Config basics](https://learn.chatgpt.com/docs/config-file/config-basic)
- [Sample configuration](https://learn.chatgpt.com/docs/config-file/config-sample)
- [Agent approvals & security](https://learn.chatgpt.com/docs/agent-approvals-security)
- [Managed configuration](https://learn.chatgpt.com/docs/enterprise/managed-configuration)
- [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md)
- [Codex Rules](https://developers.openai.com/codex/rules)

**Standards und Werkzeuge**
- [agents.md — offizielle Spezifikation (Linux Foundation)](https://agents.md)
- [Ruler — zentrale Regelverwaltung über mehrere Agenten](https://github.com/intellectronica/ruler)

**Intern**
- Pattern-Sammlung unter [80_Knowledge/Patterns/](../Patterns/) — siehe Abschnitt 7
- ETH-Zürich-Studie zu AGENTS.md-Wirksamkeit: erfasst in [AGENTS-md-Onboarding-Design](../Patterns/AGENTS-md-Onboarding-Design.md)
