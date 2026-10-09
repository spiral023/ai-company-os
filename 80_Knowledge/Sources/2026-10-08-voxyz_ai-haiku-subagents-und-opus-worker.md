---
url: https://x.com/Voxyz_ai/status/2108301411188408794
autor: "@Voxyz_ai"
datum: 2026-10-08
erfasst: 2026-10-09
typ: tweet
rohquelle: 00_Inbox/Quellen/X/2026-10-08-voxyz_ai-2108301411188408794.md
---

# Haiku für Recherche, Opus für Umsetzung: Modellwahl pro Subagent

Vox empfiehlt für Claude Code eine feste Rollenteilung: `Opus 5.5` plant und prüft, `Haiku 5.5` liest Code und recherchiert Dokumentation. Der Worker für Änderungen und Tests bleibt auf Opus. Übertragbar ist die explizite Modellwahl pro Rolle; die konkrete Konfiguration und der angeführte Kostenvorteil sind an den Stand vom 08.10.2026 gebunden.

## Rollen und Effort getrennt konfigurieren

| Rolle | Modell laut Quelle | Effort | Aufgabe |
|---|---|---|---|
| Hauptsession | `Opus 5.5` | `high` | Planen, Ergebnisse zusammenführen, Review und Verifikation |
| `Explore` | `Haiku 5.5` | `medium` | Code lesen und durchsuchen; nur `Read`, `Grep`, `Glob` |
| Researcher | `Haiku 5.5` | `medium` | Dokumentation recherchieren; zusätzlich `WebFetch`, `WebSearch` |
| Worker | `Opus 5.5` | `medium` | Code ändern und Tests ausführen |

![Agent-Baum: Opus auf high führt, Haiku auf medium recherchiert, ein Opus-Worker auf medium implementiert](../../00_Inbox/Quellen/X/medien/2026-10-08-voxyz_ai-2108301411188408794/01-photo.png)

Der eingebaute Explore-Agent folgt laut Vox dem Modell der Hauptsession und läuft damit bei einer Opus-Session ebenfalls auf Opus. Ein Custom Agent mit dem Namen `Explore` und `model: haiku` ersetzt diesen Standard. Eine passende Rollenbeschreibung soll dafür sorgen, dass Claude tatsächlich die gewünschte Aufgabe delegiert.

Der beigefügte Setup-Prompt fordert zunächst einen Änderungsvorschlag. Vorhandene Agents unter `~/.claude/agents/` und `.claude/agents/` sollen wiederverwendet und Namens- oder Modellkonflikte vor Änderungen geklärt werden. Als Mindestversion nennt Vox `2.1.293`; bei Bedrock oder Vertex seien vollständige Modell-IDs nötig. Außerdem soll `CLAUDE_CODE_EFFORT_LEVEL` geprüft werden, weil die Variable die Effort-Wahl der Subagents übersteuert. Der Originalprompt liegt unverändert in der Rohquelle.

## Demo-Zahlen mit begrenzter Übertragbarkeit

Vox führt eine Anthropic-Egg-Drop-Demo auf Claude Managed Agents an. Für das 32-Meter-Ziel nennt er mit Opus und zehn Haiku-Subagents `58 Sekunden` bei `$0.14`; Opus allein habe `3:37 Minuten` und `$0.47` benötigt. Das Bild wiederholt diese Werte.

Diese Demo nutzt zehn Subagents; der vorgeschlagene Claude-Code-Baum enthält drei Rollen. Es ist kein kontrollierter Vergleich dieses Coding-Setups, und der Thread enthält keinen Verweis auf die ursprüngliche Messung. Erfasst wurde ein Autor-Post; die Thread-Suche ist kein Vollständigkeitsnachweis.

## Einordnung

Die [aktuelle Claude-Code-Dokumentation](https://code.claude.com/docs/en/sub-agents), geprüft am 09.10.2026, bestätigt Modellvererbung für Explore bei einer Opus-Hauptsession, den gleichnamigen Custom-Agent-Override und den Vorrang von `CLAUDE_CODE_EFFORT_LEVEL`. Projekt-Agents haben Vorrang vor User-Agents. Damit erklärt sich, warum die tatsächlich aktive Konfiguration geprüft werden muss.

Im Bestand beschreibt [[2026-02-01-anthropic-docs-create-custom-subagents]] Explore noch als Haiku-Agent. Das ist ein datierter Unterschied; die alte Source bleibt erhalten. Der lokale Claude-Code-Checkout steht auf Commit `2bfb629` vom 03.10.2026 und sein Changelog endet bei `2.1.289`. Er reicht zur Prüfung der behaupteten Mindestversion `2.1.293` nicht aus. Kosten- und Qualitätsgewinne dieses Baums wurden hier nicht gemessen.

## Kernaussagen

- Modell und Effort pro Rolle festlegen; günstige Recherche kann mit einem starken Implementierungsmodell kombiniert werden → [[Modell-Eskalation-von-guenstig-nach-teuer]]
- Delegation braucht getrennte Aufgaben, passende Tool-Grenzen und eine geprüfte aktive Konfiguration → [[Kontrollierte-Agent-Parallelisierung]]
- Demo-Zahlen aus Managed Agents belegen keinen identischen Gewinn im eigenen Coding-Workflow → [[Kontrollierte-Agent-Parallelisierung]]

## Verbindungen

- [[2026-09-09-voxyz_ai-2097814698204832116]]
- [[2026-02-01-anthropic-docs-create-custom-subagents]]
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
- [[Kontrollierte-Agent-Parallelisierung]]
