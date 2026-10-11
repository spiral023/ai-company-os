---
url: https://claude.com/de/resources/articles/auto-mode-default-in-claude-code
autor: "Conner Phillippi (Anthropic)"
datum: 2026-08-07
erfasst: 2026-10-11
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-08-07-claude-auto-mode-is-now-the-default-in-claude-code-for.md
thema: Security
zeitkritisch: ja
---

# Automatische Aktionsprüfung muss gegen müde menschliche Freigaben bewertet werden

Anthropic begründet den Auto-Mode mit Messungen gegen tatsächlich beobachtetes Freigabeverhalten. Die Herstellerstudien sprechen für weniger Unterbrechungen und bessere Erkennung gefährlicher Aktionen in den untersuchten Umgebungen; sie belegen keine allgemeine Sicherheitsgarantie.

## Ausführung und Einführung

Der Artikel kündigt den Standard für neue Pro-, Max- und Team-Sessions ab `14.08.2026` an; selbst gesetzte oder administrativ fixierte Standards bleiben bestehen. Classifier-Overhead wird für diese Pläne laut Ankündigung ab dem Artikeltermin nicht mehr berechnet. Enterprise, API und Cloud-Partner bleiben zunächst opt-in; deren Umstellung wird erst angekündigt. Das ist der damalige Release-Stand.

Ein Classifier prüft Tool-Aktionen auf irreversible, destruktive oder nach außen gerichtete Folgen. Nach `3` aufeinanderfolgenden beziehungsweise `20` gesamten Blockierungen erfolgt die Rückkehr zu manuellen Freigaben. Bestehende Permission-Regeln greifen vorher; beliebige Codeausführung erlaubende Allow-Regeln wie `python:*` werden im Auto-Mode vorübergehend ausgesetzt, ohne die Settings-Datei zu ändern. Admins steuern `defaultMode` und `disableAutoMode`; Nutzer wechseln über `Shift+Tab` oder die Desktop-Auswahl.

## Freigabemüdigkeit und Vergleichsstudien

Anthropic meldet `97 %` bestätigte Permission-Prompts, gegenüber `39 %` abgelehnten Plänen. Im Juni hätten `49,5 %` aktiver CLI-Nutzer Bash-Allow-Regeln eingerichtet; rund `5 %` erlaubten alle Shellbefehle, weitere `43 %` breite Interpreter-Aufrufe. Der Anteil wachse etwa `5` Prozentpunkte je `5` Wochen. `62 %` hätten Berechtigungen bereits umgangen, `25 %` interaktiver Sessions starteten im Bypass-Modus.

In einer kontrollierten Studie mit `1.053` bezahlten Testpersonen wurde jeweils ein Prompt durch einen gefährlichen Befehl ersetzt, ohne diesen auszuführen: Menschen blockierten `13,6 %` (`143`), Auto-Mode `89 %` (`937`). Menschliche Erkennung sank von etwa `17 %` zu Beginn auf `5 %` nach mindestens `50` Prompts. In bereits sicherheitsauffälligen, zur Datennutzung freigegebenen Sessions aus Mai/Juni wurden nicht explizit angeforderte Schäden mit modellbewerteter Schwere mindestens `7/10` bei manueller Freigabe in `6,3 %`, mit Auto-Mode in `2,4 %` gefunden. Diese vorselektierten Sessions bilden keine Grundrate aller Nutzer ab.

Apollo Research prüfte synthetische Angriffe in einem Find-fix-verify-Verfahren. Nach zusätzlichem Repository-, Git- und Datenkontext sank die Missrate über geteilte und zurückgehaltene Angriffe von `12 %` auf `7 %`; etwa die Hälfte früher verpasster Angriffe wurde erkannt, etwa `2 %` zuvor erkannter Angriffe anschließend verpasst.

## Prompt-Injection: Harness und Stichprobe begrenzen den Vergleich

Trajectory Labs testete zum Stand `17.07.2026` insgesamt `72` zurückgehaltene Szenarien mit je `10` Versuchen. Die vier geprüften Diagramme zeigen:

| Angriffserfolg | Claude Auto-Mode | Claude Bypass | `GPT-5.6 Sol` Full Access / Auto-review |
|---|---|---|---|
| Gesamt, `720` je Balken | alle drei Modelle `0 %` | Sonnet/Opus `0 %`, Fable `0,28 %` | `19,03 %` / `5,83 %` |
| Tool-Calling, `250` | alle `0 %` | alle `0 %` | `6,80 %` / `2,00 %` |
| Browser, `470` | alle `0 %` | Sonnet/Opus `0 %`, Fable `0,43 %` | `25,53 %` / `7,87 %` |

Die Angriffe waren gegen `Opus 4.7` optimiert. Beide Produkte verwendeten dieselbe fremde Browser-MCP-Integration; eigene Browser-Schutzmechanismen wurden ausgeschlossen. Geprüft wurden `Claude Code v2.1.205` und `Codex v0.144.5`; die Fußnote nennt bereits eine neuere Auto-review-Version. Null beobachtete Erfolge bedeutet keine Unverwundbarkeit.

## Zusätzliche Kontrollen und Praxiserfahrungen

Anthropic beschreibt konfigurierbare Hard Denies, Geheimnis-/Zielklassifikation vor Push/PR, Git-Status vor destruktiven Befehlen und API-seitige Injection-Probes. Intern seien Veröffentlichung eines privaten Reports, massenhafte Pod-/Trainingsjob-Zerstörung und administrative statt angeforderter Leserechte verhindert worden. Adobe, Nuro, Gusto und Garner Health liefern Einsatzbeispiele; `25 %` mehr PRs bei adoptierten Teams ist eine Herstellerbeobachtung ohne ausgewiesenen Kausalnachweis. Produktionskritische Änderungen sollen weiterhin persönlich geprüft werden.

## Einordnung

Der stärkste übertragbare Befund ist die Vergleichsbasis: Ein Approval-Dialog wirkt nur, wenn er aufmerksam geprüft wird. Auswahl, Modellbewertung und herstellereigene Darstellung begrenzen die Studien. Automatische Freigabe ersetzt weder technische Isolation noch eine unabhängige lokale Evaluation. Für unser Wissen ist dies ein Beleg für risikogewichtete Review-Steuerung, keine Freigabe produktiver Security-Änderungen.

## Kernaussagen

- [[Review-Autonomie-mit-Shadow-Mode-und-Stichproben]]: Review-Müdigkeit und Fehlentscheidungen empirisch beobachten.
- [[Freigaben-und-Isolation-getrennt-steuern]]: Aktionsprüfung und technische Zugriffsgrenzen getrennt bewerten.
- [[Agent-Rechte-umfassen-Kommunikationswege]]: Das Ziel einer Übertragung entscheidet über ihren zulässigen Umfang.

## Verbindungen

- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[Hillclimbing-mit-Holdout-Split]]
