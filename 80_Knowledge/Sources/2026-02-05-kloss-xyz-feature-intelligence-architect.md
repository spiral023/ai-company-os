---
url: https://x.com/kloss_xyz/status/2019152438910165393
autor: klöss (@kloss_xyz)
datum: 2026-02-05
erfasst: 2026-08-04
typ: tweet
rohquelle: 00_Inbox/Quellen/X/2026-02-05-kloss-xyz-feature-intelligence-architect.md
thema: Arbeitsweisen
zeitkritisch: nein
beleg_art: sekundaerquelle
---

# Read-only-Prompt für Feature-Planung mit Phasenplan

Deutsche Aufarbeitung (vibedeck, Sekundärquelle) eines Prompts, der einen Agenten als „Feature Intelligence Architect“ Feature-Ideen entwickeln lässt, ohne Code zu schreiben. Der Agent liest zuerst die Projektdokumente (PRD, App-Flow, Tech-Stack, Progress-Datei) und erzeugt genau eine Datei `FEATURE_PLAN_[Datum].md` mit Phasen, Parking Lot, verworfenen Ideen und Abhängigkeiten. Belege für die Wirkung liefert die Quelle nicht.

## Kernaussagen
- Analyse und Umsetzung sind getrennt: Der Planer schreibt nur eine Markdown-Datei, ein Build-Agent führt sie nach ausdrücklicher Freigabe aus. → [[Plan-first-mit-getrenntem-Review]]
- Jedes Feature muss drei Gates bestehen (Nutzer-Journey, Mehrwert für Bestehendes, kein Regress); die Zahl der Features je Phase ist gedeckelt.
- Der freigegebene Plan ist ein Vertrag für den nächsten Agenten. → [[Handoff-Doc]]

## Einordnung
Die Struktur (Read-only-Rolle, Freigabe, Übergabedatei) ist bekannt; die Persona-Rhetorik („180+ IQ“) ist Dekoration ohne Messung. Nützlich sind die Pflicht, Voraussetzungsdokumente zu lesen, und die Rubrik „Rejected Ideas“. Kosten: viele Pflichtdokumente füllen das Context Window, bevor gedacht wird.

## Verbindungen
- [[Plan-first-mit-getrenntem-Review]]
- [[Handoff-Doc]]
- [[2026-01-14-ashpreetbedi-claude-code-spec-first]]
