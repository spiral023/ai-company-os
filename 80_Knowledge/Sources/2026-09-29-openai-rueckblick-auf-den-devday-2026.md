---
url: https://openai.com/de-DE/index/devday-2026-recap/
autor: OpenAI
datum: 2026-09-29
erfasst: 2026-10-02
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-09-29-openai-rueckblick-auf-den-devday-2026.md
thema: Markt & Strategie
zeitkritisch: ja
---

# OpenAI DevDay 2026: Modelle, Preisstufen und Agent-Infrastruktur im Überblick

OpenAI fasst am 29.09.2026 mehr als 20 Ankündigungen zusammen. Es ist eine reine Herstellerdarstellung: Alle Leistungs- und Preisangaben sind Selbstaussagen ohne Methodenangabe. Für Coding-Agent-Praxis relevant sind vor allem Modellstufen, Geschwindigkeit, die Agents API und die Decisions API.

## Modelle und Preise (Stand 29.09.2026)

- `GPT-6.1 Sol` ersetzt `GPT-6 Sol`. OpenAI behauptet „nahezu die Intelligenz“ von `GPT-6 Astra` zu einem Fünftel der regulären Astra-Token-Preise für Ein- und Ausgabe. Eine Messgröße nennt der Text nicht; eine Drittmessung liefert [[2026-09-29-artificialanlys-2105025585332605357]].
- `Ultrafast`: bis zu 8-mal schnellere Token-Generierung in Codex (300 Token pro Sekunde), bis zu 6-mal in der API. `GPT-6 Astra Ultrafast` ist verfügbar, `GPT-6.1 Sol Ultrafast` „bald“.
- Neuer Pro-Tarif für 500 USD pro Monat mit höchsten Nutzungslimits und exklusivem Astra-Ultrafast-Zugang.
- `dots`: dauerhaft laufende Agenten auf `GPT-6 Astra` mit eigenem Cloud-Computer (Pro, Business Premium, Enterprise).

## Agent-Infrastruktur

- Die Agents API gibt verwalteten Zugriff auf den Codex-Harness (Multi-Agent, Toolsuche, Kontextverdichtung, neu: Computerbedienung); OpenAI betreibt das System. Gleiches als Bedrock Managed Agents auf AWS.
- Die Decisions API richtet die Intelligenz von `Luna` auf einen selbst definierten Fragenkatalog mit begrenzten Antwortoptionen aus: Klassifizieren, Routen, nächste Agent-Aktion wählen. Begrenzte Vorschau.
- Codex CLI mit Sprachchat und `/agents`-Ansicht; Code Review mit automatischer Cloud-Prüfung; Codex Security Cloud.
- ChatGPT als Plattform: 1,2 Milliarden Nutzer genannt, Plugin-Erweiterungen, MCP-Events, Marketplace mit 32 Partnern.

## Einordnung

Selbstberichtet und werblich formuliert. Die Zahl „ein Fünftel des Preises“ bezieht sich auf Token-Preise, nicht auf Kosten pro Task; Letzteres hängt vom Token-Verbrauch ab. Für Entscheidungen taugen die Preise und Verfügbarkeiten als Stand-Angabe, die Leistungsaussagen erst mit Drittmessung. Die Decisions API ist die Produktform eines Entscheidens per Auswahl statt Freitext.

## Kernaussagen

- Mittlere Modellstufe nahe an der Spitze zu einem Bruchteil des Preises → [[Modell-Eskalation-von-guenstig-nach-teuer]]
- Verwaltete Harness-Infrastruktur statt Eigenbau.

## Verbindungen

- [[Entscheidung-per-Scoring-statt-Generierung]]
- [[2026-09-29-artificialanlys-2105025585332605357]]
- [[2026-09-22-kimmonismus-2102462091299098640]]
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
