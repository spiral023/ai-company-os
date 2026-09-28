---
url: https://www.tiktok.com/@agentic.james/video/7661714775629499662
autor: "@agentic.james"
datum: 2026-07-12
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-07-12-agenticjames-claude-codes-new-feature-checkup-makes-claude-more-token-efficient-and.md
thema: Tools & Releases
zeitkritisch: ja
---

# Claude Code `/checkup`: sieben Aufräum- und Konfigurationsschritte für weniger Baseline-Kontext

Das Video stellt den neuen Claude-Code-Befehl `/checkup` (Stand der Quelle: 2026-07-12) vor. Laut Sprecher senkt er den Token-Verbrauch, indem er Setup und Memory-Dateien eines Projekts aufräumt. Es ist eine reine Feature-Beschreibung aus dem Transkript eines Creators, der nebenbei seine Kurs-Community bewirbt: keine Messung, keine Zahlen, kein Vorher-Nachher. Was `/checkup` tatsächlich tut, ist hier nicht gegen die Anthropic-Doku geprüft.

## Die sieben Schritte laut Sprecher

**Kontext verschlanken (Schritte 1 bis 3):**
1. Die Session-Historie wird ausgewertet: Welche Skills, MCP-Server und Plugins werden nie genutzt? Ungenutzte werden entfernt, um Context-Verbrauch zu senken.
2. `CLAUDE.md` auf User-, Projekt- und lokaler Ebene werden gegeneinander dedupliziert.
3. Zu lange `CLAUDE.md`-Dateien werden in mehrere spezifischere, verschachtelte `CLAUDE.md`-Dateien aufgeteilt. Das ermöglicht Progressive Disclosure: Der Agent lädt Wissen erst, wenn er im passenden Verzeichnis arbeitet. Der Sprecher behauptet, diese drei Schritte senkten den Baseline-Kontext beim Start „schockierend“ stark, nennt aber keine Zahl.

**Betrieb und Komfort (Schritte 4 bis 7):**
4. Hooks werden getestet; zu langsame sollen effizienter gemacht werden.
5. Claude Code wird automatisch aktualisiert.
6. Auto Mode wird als Standard eingestellt.
7. Aus der Historie werden häufig bestätigte Read-only-Befehle als vorab genehmigt in die Permissions übernommen.

## Einordnung

Die Schritte 1 bis 3 entsprechen manuellen Kontext-Hygiene-Regeln, die im Bestand schon stehen (schlanke Root-Datei, Details auslagern, ungenutzte Tools entfernen); neu ist allenfalls die Automatisierung auf Basis der tatsächlichen Nutzungshistorie. Ob die automatische Aufteilung inhaltlich sauber ist, bleibt offen: Ein Split kann Regeln in Unterordner verschieben, in denen sie nie geladen werden, und ein Löschen „ungenutzter“ MCP-Server oder Skills kann selten, aber wichtige Fähigkeiten entfernen. Schritt 7 lockert Permissions anhand von Gewohnheit statt Prüfung; Auto Mode als Default verschiebt Kontrolle zum Modell. Beides ist ein Sicherheits- und Bequemlichkeits-Trade-off, den die Quelle nicht erwähnt. Belastbarkeit: selbstberichtet, ungeprüft, zeitkritisch (Feature-Stand Juli 2026).

## Kernaussagen
- `/checkup` räumt anhand der Nutzungshistorie ungenutzte Skills, MCP-Server und Plugins auf und reduziert so den Baseline-Kontext → [[Kontext-Hygiene-Entscheidungsbaum]]
- Lange `CLAUDE.md`-Dateien werden dedupliziert und in verschachtelte, spezifische Dateien gesplittet (Progressive Disclosure) → [[AGENTS-md-Onboarding-Design]]
- Hooks werden auf Geschwindigkeit getestet; Permissions und Auto Mode werden aus dem Nutzungsverhalten vorkonfiguriert → [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]

## Verbindungen
- [[2026-05-01-mnilax-claude-code-overhead-9-patterns]]
- [[2026-07-25-agenticjames-they-cut-claude-code-system-prompt-by-80-and-you-should-be-doing-the]]
- [[2026-04-13-wiki-compiler-gute-agents-md-schreiben]]
- [[2026-05-09-zodchiii-15-claude-code-settings-most-developers]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
