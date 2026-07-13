---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-05-04
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Claude Session- und Token-Management für lange Agent-Arbeiten“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/02-agent-guides-und-templates/wka-claude-session-und-token-management-2026-05-04.md`), kombinierte Synthese der beiden Artikel zu Session-Management (1M Context) und Usage-Limits-Token-Strategien.

Kernpunkte (kondensiert, gegenüber den beiden Einzelartikeln neu/verdichtet):

- Zentrale Praxisregel: „Gute Claude-Nutzung optimiert nicht auf möglichst lange Chats, sondern auf klar geschnittene Arbeitsblöcke mit bewusst gewähltem Kontext.“
- Konkretes Arbeitsmuster für lange Agent-Arbeiten: (1) Start mit engem Briefing, (2) Analyse und Umsetzung bewusst trennen, (3) Zwischenstände als kurze Handoff-Summary festhalten (Ziel, Entscheidungen, Dateien, Risiken, Tests), (4) Review möglichst in neuer Session/Subagent, (5) Fehlpfade früh mit `rewind` abschneiden, (6) `/compact` nur mit klaren Erhaltungsanforderungen, (7) Tokenbudget/Modellwahl bewusst nach Aufgabenschwere einsetzen.
- Entscheidungscheckliste vor dem nächsten Prompt: Ist das noch dieselbe Aufgabe? Braucht Claude den bisherigen Detailkontext wirklich? Enthält der Verlauf Fehlversuche/alte Hypothesen? Würde ein Handoff-Prompt die nächste Phase klarer machen? Soll ein Subagent die Zwischenarbeit isolieren?

## Kernaussagen

- Sieben-Schritte-Arbeitsmuster für lange Claude-Code-Sessions (enges Briefing → Analyse/Umsetzung trennen → Handoff-Summary → Review neu rahmen → früh reseten → gezielt kompaktieren → Tokenbudget bewusst einsetzen) → [[Kontext-Hygiene-Entscheidungsbaum]]
- Entscheidungscheckliste vor jedem Prompt als praktisches Werkzeug, um `Continue` als riskanten Default zu vermeiden → [[Kontext-Hygiene-Entscheidungsbaum]]
