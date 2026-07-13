---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-17
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Lovable für Design, Debugging und Sicherheit“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/03-tool-profile/02-design-und-ui-tools/wka-lovable-design-debugging-und-sicherheit-2026-04-17.md`), Synthese aus X-Posts (@damienghader) und offizieller Lovable-Doku.

Kernpunkte (kondensiert):

- Design: component-first statt seitenzentriert — Komponenten zuerst definieren, vorhandene gute Komponenten referenzieren, klare Layout-Logik statt vager Design-Adjektive, Screenshots/Vorher-Nachher gezielt einsetzen. Design-Konsistenz über eine projektweite Knowledge-Datei mit Design-System, Rollen, User Journeys.
- Debugging: bei komplexen Fehlern erst Plan-Modus für Root-Cause-Suche nutzen, statt zehnmal stumpf „try to fix“ auszulösen. Logs/Konsolenfehler direkt einfüttern, nach bereits Probiertem fragen, alternative Lösungswege anfordern. Für verstrickte Zustände: sauberer Neustart/Remix oft günstiger als weitere Korrekturschleifen.
- Sicherheit: Frontend ist nie vertrauenswürdig — keine Secrets im Frontend, keine reine Client-Validierung, sensible Logik in Supabase Edge Functions, Auth/Autorisierung serverseitig prüfen, früh mit Row Level Security arbeiten.
- Security Checker als fester Release-Schritt (nicht Alibi): Checker laufen lassen → Funde prüfen → Fixes einbauen → erneut prüfen. Gerade bei Supabase-Apps ist frühe Sicherheitsdisziplin billiger als spätes Nachhärten.

## Kernaussagen

- Plan-Modus für Root-Cause-Debugging statt wiederholter blinder „try to fix“-Versuche; bei verstrickten Zuständen sauberer Neustart günstiger als weitere Korrekturschleifen → [[Lovable-Prototyp-dann-lokaler-Handoff]]
- Frontend ist nie vertrauenswürdig: Secrets/Validierung/Autorisierung gehören serverseitig, Security Checker als fester Release-Schritt vor Veröffentlichung → [[Lovable-Prototyp-dann-lokaler-Handoff]]
- Component-first-Design mit projektweiter Design-Knowledge-Datei statt Seite-für-Seite-Beschreibung → [[Lovable-Prototyp-dann-lokaler-Handoff]]
