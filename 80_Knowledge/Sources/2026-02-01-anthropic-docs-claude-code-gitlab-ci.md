---
url: https://code.claude.com/docs/en/gitlab-ci-cd
autor: "Anthropic Docs"
datum: 2026-02-01
erfasst: 2026-08-05
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-claude-code-gitlab-ci.md
beleg_art: sekundaerquelle
---

# Claude Code in GitLab CI/CD: Event-getriggerter Agent mit Merge-Request als Gate

Claude Code lässt sich als eigener Job in GitLab CI/CD betreiben, der auf Trigger wie einen `@claude`-Kommentar in einem Issue oder einer Merge Request reagiert, in einem isolierten Runner arbeitet und Ergebnisse ausschließlich als Merge Request zurückspielt. Das Muster ist damit strukturell dasselbe wie bei lokaler Nutzung — Discovery, Umsetzung, Verifikation — nur dass der Auslöser ein Kommentar statt ein Prompt ist und der Reviewer-Schritt durch den normalen MR-Prozess des Teams ersetzt wird, statt einen eigenen Review-Agenten zu benötigen.

## Funktionsweise und Setup

Drei Bausteine tragen das Muster: **Event-driven** (GitLab-Trigger wie Kommentare mit `@claude`), **Provider-Abstraktion** (Claude API, AWS Bedrock oder Google Vertex AI hinter derselben Job-Definition) und **Sandboxed Execution** (jeder Lauf isoliert im Runner, Änderungen erreichen den Hauptbranch nur über einen MR). Der schnellste Einstieg nutzt die Claude API direkt: `ANTHROPIC_API_KEY` als maskierte CI/CD-Variable hinterlegen und einen Job mit `curl -fsSL https://claude.ai/install.sh | bash` sowie `claude -p "..." --permission-mode acceptEdits --allowedTools "Bash Read Edit Write mcp__gitlab"` definieren. Für Enterprise-Umgebungen ohne statische Keys im Repo stehen AWS Bedrock über OIDC-Token-Exchange und Google Vertex AI über Workload Identity Federation bereit — beide vermeiden dauerhaft gespeicherte Zugangsdaten in der CI-Konfiguration.

Drei Use Cases werden konkret genannt: „Issue zu MR“ (Kommentar beschreibt das Feature, Claude öffnet einen MR), Implementierungshilfe in einer laufenden MR-Diskussion, und Bugfix aus einer kurzen Fehlerbeschreibung heraus. In allen drei Fällen bleibt `CLAUDE.md` im Projekt-Root die Quelle für Coding-Standards, die der CI-Agent genauso liest wie eine lokale Session.

## Sicherheits- und Kostenhinweise

Die Doku nennt explizit: API-Keys niemals committen, sondern über CI/CD-Variablen oder OIDC beziehen; `CLAUDE.md` prägnant halten, weil sie auch im CI-Job vollständig geladen wird; NPM-Pakete cachen für Performance; Runner-Minuten und API-Token-Kosten im Blick behalten. Troubleshooting-Hinweise sind konkret genug, um typische erste Fehler zu vermeiden: keine Reaktion meist wegen `@claude` statt `/claude` oder falscher Pipeline-Trigger, fehlende MRs meist wegen unzureichender `CI_JOB_TOKEN`-Berechtigungen (Project Access Token als Alternative).

## Einordnung

Der Inhalt ist eine deutsche Sekundäraufarbeitung der offiziellen Anthropic-Dokumentation, nicht selbst gegen die Live-Seite oder ein eigenes GitLab-Setup verifiziert — Konkretes wie Image-Tags (`node:24-alpine3.21`), das Install-Skript oder einzelne CLI-Flags sind Konfigurationsstand zum Erfassungszeitpunkt und können sich ändern, ohne dass das Muster selbst veraltet. Das eigentlich Übertragbare ist unabhängig vom GitLab-Detail: ein Coding Agent wird als sandboxed CI-Job event-getriggert betrieben und sein Output läuft ausschließlich durch das bestehende Review-Gate (hier: Merge Request) des Teams, statt eigene Freigabemechanismen zu erfinden. Das ist im Bestand noch nicht als eigenständiges Pattern erfasst; die drei genannten Provider-Optionen (Claude API/Bedrock/Vertex) hinter derselben Job-Definition sind zusätzlich ein konkretes Beispiel für Provider-Abstraktion, wie sie im Kern auch [[Lokale-Modell-Umleitung-Muster]] beschreibt — dort für die lokale CLI-Session, hier für einen automatisierten CI-Kontext.

## Kernaussagen

- Ein Coding Agent kann als event-getriggerter, sandboxed CI-Job betrieben werden, dessen Output ausschließlich über das bestehende Merge-Request-Gate des Teams läuft → [[CI-Agent-mit-Review-Gate]]
- Für Enterprise-Umgebungen ersetzt Provider-Abstraktion (Claude API/AWS Bedrock/Google Vertex AI über OIDC bzw. Workload Identity Federation) statische API-Keys im Repo → [[Lokale-Modell-Umleitung-Muster]]
- API-Keys niemals committen, sondern über maskierte CI/CD-Variablen oder OIDC beziehen — dieselbe Grundregel wie bei lokalen Secret-Leckpfaden, nur für die CI-Umgebung → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]

## Verbindungen

- [[Lokale-Modell-Umleitung-Muster]]
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[CI-Agent-mit-Review-Gate]]
