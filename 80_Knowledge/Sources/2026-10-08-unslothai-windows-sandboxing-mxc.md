---
url: https://x.com/UnslothAI/status/2108229721159053557
autor: "@UnslothAI"
datum: 2026-10-08
erfasst: 2026-10-09
typ: tweet
rohquelle: 00_Inbox/Quellen/X/2026-10-08-unslothai-2108229721159053557.md
---

# Unsloth ergänzt Windows-Sandboxing mit MXC: Softwarefilter, OS-Isolation und Freigaben

Unsloth kündigt eine Integration von Microsoft eXecution Container (`MXC`) für die Ausführung von Code unter Windows an. Der Post nennt eine Zusammenarbeit mit dem Windows-Team und weniger als `100 ms` zusätzlichen Overhead. Der verlinkte Guide und seine Screenshots zeigen die konkrete Bedienung, aber auch Einschränkungen, die die pauschale Ankündigung nicht nennt.

## Zwei Sandbox-Stufen und eigene Freigabe-Modi

Das Post-Bild unterscheidet `Low` und `High`. Low prüft Tool-Aufrufe durch Strings, AST und reguläre Ausdrücke. High ergänzt eine Isolation auf Betriebssystemebene. Das Menü benennt Python und Terminal als die betroffenen Tools; daraus lässt sich keine überprüfte Isolation beliebiger anderer Tools ableiten.

![Unsloth-Post: Low mit Softwareprüfungen, High mit OS-Isolation und separate Freigabe-Modi](../../00_Inbox/Quellen/X/medien/2026-10-08-unslothai-2108229721159053557/01-photo.jpg)

Daneben stehen die Freigabe-Modi `Ask for approval`, `Approve for me` und `Run automatically`. Das Bild zeigt `Approve for me` zusammen mit `Sandbox High`. Ob eine Aktion vorher bestätigt werden muss und in welcher Umgebung sie anschließend läuft, sind damit getrennte Entscheidungen. `Full access` hebt laut Quelle beide Sandbox-Stufen auf; es ist mehr als eine automatische Freigabe innerhalb einer Sandbox.

## Plattformen, Status und Grenzen

Der ergänzend [lokal archivierte Guide](../../00_Inbox/Quellen/URL/2026-10-08-unsloth-sandboxing-in-unsloth-unsloth-documentation.md) nennt `MXC` unter Windows, `bubblewrap` beziehungsweise `bwrap` unter Linux und `Seatbelt` unter macOS. Linux benötigt laut Guide bwrap; auf dem Mac werde Seatbelt automatisch aktiviert. Für Windows behauptet der Fließtext Verfügbarkeit ab Windows 11 `24H2`.

Der Windows-Screenshot präzisiert: Python und Terminal zeigen jeweils einen eigenen Sandbox-Status. Terminal läuft hier in `cmd.exe`, weil Git Bash in dieser Windows-Sandbox nicht starten könne. Ein eingebauter Container ist im gezeigten System aktiv. Der alternative Fallback benötigt laut Screenshot einen Admin-Schritt, der nach einem Neustart wiederholt werden muss. Ohne funktionierende OS-Sandbox sollen riskante Aufrufe zuerst eine Freigabe verlangen.

![Windows-Sandbox-Einstellungen: Status für Python und Terminal, aktiver Built-in-Container, Fallback und Preview-Hinweis](../../00_Inbox/Quellen/URL/medien/2026-10-08-unsloth-sandboxing-in-unsloth-unsloth-documentation/03-bild.jpg)

Entscheidend ist der Hinweis im selben Screenshot: MXC sei noch eine Preview und keine Sicherheitsgrenze. Das ist eine Einschränkung der Herstellerdarstellung und kein eigener Sicherheitstest. Die Aussage im Post-Bild, Tool-Aufrufe könnten keinen Schaden auf OS-Ebene anrichten, wird deshalb nicht als Garantie übernommen.

Die am 09.10.2026 gelesene [Microsoft-Dokumentation zur Windows-Unterstützung](https://github.com/microsoft/mxc/blob/main/docs/backends/process-container/os-version-support.md) nennt für Process Isolation auf 24H2 konkret Build `26100.9278`. Die Versionsbezeichnung `24H2` allein beschreibt die Voraussetzung somit nicht vollständig. Microsoft beschreibt [MXC im README](https://github.com/microsoft/mxc) als eingebettetes SDK mit mehreren Backends und Policies für Dateisystem, Netzwerk und UI; das Framework ist plattformübergreifend. Das ist eine ergänzende Dokumentationsprüfung, keine Code-Verifikation der Unsloth-Integration.

## Latenzangaben auseinanderhalten

| Plattform | Backend laut Guide | Low Sandbox | High Sandbox |
|---|---|---|---|
| Windows | `MXC` | 8 ms | 164 ms |
| Linux | `bubblewrap` | 3 ms | 50 ms |
| macOS | `Seatbelt` | 10 ms | 110 ms |

Die Guide-Tabelle widerspricht für Windows High der pauschalen Post-Angabe von weniger als `100 ms`. Zusätzlich nennt der Guide für die reinen Softwareprüfungen `1–2 ms` je Aufruf; deren Messumfang ist offenbar anders als in der Low-Tabelle, wird aber nicht erklärt. Hardware, Stichprobe und genaue Messbedingungen fehlen. Alle Werte bleiben Herstellerangaben und werden nicht zu einem gemeinsamen Leistungsversprechen verdichtet.

Der Guide nennt außerdem Limits von `100 MB` Dateigröße, `8 GB` Speicher und `600 Sekunden` CPU-Zeit sowie Prozesslimits, das Entfernen geheimer Umgebungsvariablen und Sperren eigener Credential-Dateien. Diese beschriebenen Kontrollen sind hier nicht getestet.

## Einordnung

Der Beitrag erweitert das bestehende Thema Sicherheit & Sandboxing um eine konkrete lokale Tool-Integration. Softwarefilter sind technisch ausgeführte Prüfungen und damit mehr als eine Prompt-Empfehlung; sie sind aber nicht gleichbedeutend mit einer geprüften OS-Sicherheitsgrenze. Ein High-Schalter, ein Backend-Name und ein Screenshot ersetzen keinen Test der tatsächlichen Datei-, Netzwerk- und Prozessgrenzen.

[[2026-05-13-david-wiesen-openai-codex-windows-sandbox]] beschreibt bereits eine andere Windows-Sandbox-Architektur. Die neue Quelle belegt daher eine Unsloth-Integration, nicht den erstmaligen Beginn von Sandboxing unter Windows. `microsoft/mxc` und `unslothai/unsloth` sind lokal nicht unter `external_repos/` vorhanden; ein gezielter Repo-Import wäre ein weiterer Schritt für eine Code-Prüfung. Erfasst wurde ein Autor-Post, ohne behauptete Thread-Vollständigkeit.

## Kernaussagen

- Low kombiniert Softwareprüfungen, High ergänzt plattformspezifische OS-Isolation; Status und Preview-Grenzen bleiben zu prüfen → [[Sandbox-Komposition-aus-OS-Primitiven]]
- Freigabe-Modus und Isolation getrennt beurteilen; automatische Freigabe innerhalb einer Sandbox unterscheidet sich von Full access → [[Freigaben-und-Isolation-getrennt-steuern]]
- Technisch ausgeführte Filter, OS-Isolation und Prompt-Empfehlungen bieten unterschiedliche Arten von Kontrolle → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]

## Verbindungen

- [[Sandbox-Komposition-aus-OS-Primitiven]]
- [[Freigaben-und-Isolation-getrennt-steuern]]
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[2026-05-13-david-wiesen-openai-codex-windows-sandbox]]
- [[Thema-Sicherheit-Sandboxing]]
