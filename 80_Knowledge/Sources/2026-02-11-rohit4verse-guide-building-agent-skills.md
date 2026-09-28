---
url: https://x.com/rohit4verse/status/2021622526112358663
autor: Rohit (@rohit4verse)
datum: 2026-02-11
erfasst: 2026-08-04
typ: tweet
rohquelle: 00_Inbox/Quellen/X/2026-02-11-rohit4verse-guide-building-agent-skills.md
thema: Arbeitsweisen
zeitkritisch: nein
beleg_art: sekundaerquelle
---

# Agent Skills bauen: dreistufige Offenlegung und Erfolgskriterien

Deutsche Aufarbeitung (vibedeck, Sekundärquelle) eines Guides zum Skills-Standard. Die Beschreibung der Mechanik entspricht der Anthropic-Dokumentation; eigene Zahlen oder Messungen liefert die Quelle nicht.

## Kernaussagen
- Drei Ladestufen: Frontmatter immer im Context, `SKILL.md`-Body bei Relevanz, `scripts/` und `references/` nur bei Bedarf. → [[Skill-Call-Hierarchie]]
- Vor dem Bau werden Erfolgskriterien gesetzt: Trigger-Trefferquote (Ziel über 90 %, ohne Herleitung), weniger Tool-Calls, konsistente Ergebnisse. Die `description` gilt als Trigger und folgt „was + wann“. → [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- `allowed-tools` im Frontmatter begrenzt die Rechte eines Skills; Skills fremder Herkunft sind ein Vertrauensthema.

## Einordnung
Kein neues Konzept, aber eine kompakte Bestätigung des Bestands. Die 90-%-Marke ist ein Richtwert ohne Messgrundlage; Aussagen wie „1 % der Nutzer baut Skills“ sind Rhetorik.

## Verbindungen
- [[Skill-Call-Hierarchie]]
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- [[2026-02-09-pdrmnvd-how-claude-code-skills-work]]
- [[2026-07-01-anthropic-skill-creator-skill-md]]
