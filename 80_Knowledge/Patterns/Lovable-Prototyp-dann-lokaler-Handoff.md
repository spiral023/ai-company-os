# Lovable-Prototyp-dann-lokaler-Handoff

**Konfidenz:** meinung

## Zweck

Nutzt Lovable (oder vergleichbare Cloud-UI-Builder) für das, worin es wirklich stark ist — schnelle visuelle Prototypen —, ohne dort hängenzubleiben, sobald Backend, Auth, Tests, Deployment oder Security wichtig werden. Verhindert sowohl verfrühtes manuelles Coding vor UI-Klärung als auch das Gegenteil: langes Weiterarbeiten in Lovable, obwohl echtes Engineering ansteht.

## Funktionsweise

Der Ablauf ist bewusst zweigeteilt: (1) Idee, Scope und erste UX in Lovable verdichten, einen klickbaren Prototyp im Zielstack (typischerweise React, Vite, TypeScript, shadcn/ui, Tailwind CSS) erzeugen; (2) früh in ein lokales Repository wechseln und dort mit einem Coding Agent (Codex, Claude Code o.ä.) Architektur, Tests, APIs, Deployment und Produktreife weiterentwickeln. Der erste Prompt für Lovable ist kein Kurzbefehl, sondern ein vollständiges Produktbriefing: Ziel/Nutzen, Zielnutzer/Rollen, Hauptabläufe, Informationsarchitektur (Screens, Tabs, Dialoge), Datenmodell mit Beispielobjekten, UI-/Design-Richtung, technische Leitplanken und explizite Nicht-Ziele. Mock-first statt Backend-first: ausschließlich synthetische Beispieldaten, keine echten Secrets/sensiblen Daten im Prototyp — echte Backend-APIs ersetzen die Mocks erst nach dem Export. Design arbeitet component-first statt seitenzentriert: Komponenten zuerst definieren, gute vorhandene Komponenten referenzieren, klare Layout-Logik statt vager Adjektive, projektweite Design-Knowledge-Datei für Design-System/Rollen/User-Journeys. Bei Fehlern: Plan-Modus für Root-Cause-Suche statt wiederholtem blindem „try to fix“; bei verstricktem Zustand ist ein sauberer Neustart/Remix oft günstiger als weitere Korrekturschleifen. Sicherheitsdisziplin vor Veröffentlichung: Frontend ist nie vertrauenswürdig (keine Secrets/Validierung im Client), sensible Logik serverseitig (z.B. Supabase Edge Functions, Row Level Security), Security Checker als fester Release-Schritt (laufen lassen → Funde prüfen → Fixes → erneut prüfen), nicht als Alibi-Häkchen.

## Vorteile

- Nutzt die jeweilige Stärke beider Werkzeuge: Lovable für schnelle visuelle Iteration und Mock-Daten, lokaler Coding Agent für Backend/Tests/Deployment/Security — statt eines Werkzeugs für alles.
- Ein vollständiges Produktbriefing als erster Prompt reduziert teure Korrekturschleifen gegenüber einem vagen Kurzprompt erheblich.
- Frühe, klare Handoff-Checkliste (Hauptscreen vorhanden, Kernflows klickbar, keine sensiblen Daten im Projekt) macht den Übergangspunkt explizit statt beliebig.

## Nachteile & Grenzen

- Setzt voraus, dass vor dem ersten Prompt tatsächlich Zeit in Problemverständnis, Nutzerflüsse und Datenmodell investiert wird — bei Zeitdruck wird dieser Schritt oft übersprungen, was die Korrekturschleifen zurückbringt, die das Pattern vermeiden soll.
- Lovable-spezifische Details (Zielstack, Security-Checker, Credit-Modell) sind produktspezifisch und veralten schneller als die zugrunde liegende Reihenfolge (früh sichtbar machen → früh exportieren → lokal professionalisieren).
- Kein Ersatz für echte Sicherheitsprüfung: Ein Security-Checker findet mechanische Schwachstellen zuverlässig, ersetzt aber kein fachliches Security-Review bei sensiblen Anwendungen.

## Wann einsetzen, wann nicht

- Einsetzen: neue Webapp-Ideen, bei denen zuerst UI/Navigation/Mock-Daten geklärt werden müssen, bevor sich Backend-Aufwand lohnt.
- Nicht einsetzen: Erweiterungen an bereits bestehenden, produktiven Codebasen ohne neuen UI-Explorationsbedarf — dort ist der direkte Weg über den lokalen Coding Agent angemessener.

## Belege

- 2026-04-17 · [[2026-04-17-wiki-compiler-lovable-frontend-rapid-prototyping]] · meinung — Wiki-Artikel beschreibt den Zielstack, das Produktbriefing-Prompt-Muster und die Handoff-Checkliste.
- 2026-04-17 · [[2026-04-17-wiki-compiler-lovable-design-debugging-sicherheit]] · meinung — Unabhängige Quelle (X-Posts @damienghader, offizielle Lovable-Doku) ergänzt component-first Design, Plan-Modus-Debugging und den Security-Checker-Ablauf.
- 2026-04-17 · [[2026-04-17-wiki-compiler-codex-claude-code-lovable-workflow]] · meinung — Bestätigt den Handoff „Lovable → Export → lokales Repo → Coding Agent“ aus Entwickler-Workflow-Perspektive, unabhängig von den beiden anderen Quellen.
- 2026-02-04 · [[2026-02-04-lovable-docs-best-practices]] · meinung — Primärquelle (Lovable Docs) konkretisiert die Knowledge-Datei als PRD-Ersatz, den 60-70%-Plan-Modus-Richtwert, „In Bricks bauen“ und die Frontend-First-Build-Strategie mit Supabase-Revert-Fallstrick.
- 2026-01-17 · [[2026-01-17-damien-ghader-prompting-lovable-design]] · meinung — Primärquelle liefert das Drei-Ebenen-Modell (Foundations/Komponenten/Komposition) im Original mit konkreten Tailwind-Prompt-Beispielen und der Regel, existierende Komponenten namentlich zu referenzieren statt Design erneut zu beschreiben.

## Spannungen & offene Fragen

- Die fünf Quellen stammen aus unterschiedlichen Primärquellen (Lovable-Doku direkt, unabhängige X-Posts, Tool-Vergleichsartikel) und widersprechen sich nicht, ergänzen sich aber in unterschiedlichen Facetten (Prompt-Design, Debugging/Security, Werkzeugwahl, Design-System-Aufbau).
- Bei uns bereits als Workflow-Datei vorhanden: `20_Workflows/Lovable_Prototyping.md` — offene Frage, ob und wie dieses Pattern dort eingearbeitet werden soll (bewusst nicht eigenmächtig entschieden, siehe Skill-Grenzfälle für Meta-Änderungen an bestehenden Workflows).

## Verwandte Patterns

- [[Plan-first-mit-getrenntem-Review]]
- [[Spec-Grilling]]
