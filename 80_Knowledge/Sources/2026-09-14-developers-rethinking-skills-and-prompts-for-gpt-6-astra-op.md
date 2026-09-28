---
url: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
autor: OpenAI Developers
datum: 2026-09-14
erfasst: 2026-09-14
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-09-14-developers-rethinking-skills-and-prompts-for-gpt-6-astra-op.md
thema: Arbeitsweisen
zeitkritisch: ja
---

# Skills, AGENTS.md und Prompts für ein stärkeres Modell entschlacken

OpenAI empfiehlt, angesammelte Anweisungen (Skills, `AGENTS.md`, Task-Prompts) bei jedem Modellwechsel zu überprüfen, weil ein fähigeres Modell weniger Scaffolding braucht und zu viel davon aktiv schadet. Der Beitrag ist ein Herstellerblog mit Erfahrungswerten zu GPT-6 Astra (Stand 2026-09-14), ohne Messdaten oder Evals. Die Aussagen sind plausibel und selbstberichtet, nicht belegt. Das Datum ist in der Inbox-Notiz als unsicher markiert.

## Skills: kurz, geroutet, nicht überspezifiziert

- **Beschreibungen kurz halten.** Skill-Name und -Beschreibung liegen dauerhaft im Kontext. Bei zu vielen Skills kürzt Codex die Beschreibungen selbst, das Modell sieht dann weniger je Skill und wählt schlechter. Widersprüchliche oder überbetonte Beschreibungen laden Skills, die der Aufgabe nicht helfen.
- **Auslöser eng fassen.** Das Beispiel: „Use when working with databases, queries, models, or persistence“ zieht den Migrations-Skill bei jeder Datenbankberührung. „Use when adding or changing a migration, or reviewing its rollout“ trifft nur den eigentlichen Fall.
- **Progressive Disclosure.** Ein Skill mit mehreren Workflows bekommt ein minimales Root-Dokument als Router, das auf Zusatzdokumente und Skripte verweist. Jeder gelesene Skill kostet Kontext und bringt die Compaction näher.
- **Keine Itinerare.** Sehr detaillierte Rezepte helfen bei stärkeren Modellen nicht mehr und können das Ergebnis verschlechtern. Repository-Skills steuern außerdem die Agents anderer Contributor, die evtl. andere Modelle nutzen; Anleitungen für schwächere Modelle können Astra überconstrainen. OpenAI hat dazu die Guidance des `$skill-creator` aktualisiert.

## AGENTS.md und Grenzen

- **Kein Pflichtlesen vor jeder Änderung.** „Vor jedem Edit architecture.md, database.md, deployment.md lesen“ verbrennt Kontext und bremst, etwa bei einem Typo-Fix. Besser ist ein kontextueller Verweis: welches Dokument für welchen Anlass.
- **Testaufforderungen prüfen.** Astra testet von selbst; alte Anweisungen dazu erzeugen unnötige Testläufe.
- **Freigaben für sichere Workflows.** Astra sei eher zögerlich. Ein Satz in `AGENTS.md` kann gezielt erlauben, etwa eine lokale Suite mit Wegwerf-Fixtures ohne Produktionszugriff auszuführen, Fehler zu beheben und ohne Rückfrage erneut zu testen.
- **Harte Verbots-Formulierungen entschärfen.** Was früher gegen eigenmächtige Modelle geschrieben wurde, kann Astra zu ernst nehmen und stoppen lassen, wo Weiterarbeit erwünscht wäre.

## Persistenz und Completion

Im Vergleich zu GPT-5.6 Sol liefert Astra eher eine erste Implementierung und wartet auf Review. Gegenmittel: Fertigstellung vorab definieren (starten, Ergebnis prüfen, Fehler beheben) und keine Pflichtpause nach dem ersten Wurf einbauen. Explorationen über den ersten Durchgang hinaus brauchen ein Ziel und ein Stoppkriterium. Zum Schluss der Hinweis, Astra selbst ein Audit der eigenen Anweisungen nach diesen Punkten durchführen zu lassen.

## Einordnung

Der Kern deckt sich mit bereits belegten Prinzipien: kurze, trennscharfe Trigger, Router statt Monolith, lean `AGENTS.md`. Neu ist die explizite Aussage, dass Anweisungen modellabhängig veralten und aktiv Schaden anrichten können, sowie der Punkt, dass Verbotssprache bei einem „aligneren“ Modell überkorrigiert. Belegt ist davon nichts: keine Eval, keine Zahlen, keine Vergleichsläufe. Kosten: Wer Anweisungen pro Modell pflegt, braucht Evals, sonst wird aus dem Entschlacken Bauchgefühl, und geteilte Repos mit gemischten Modellen haben keine einheitlich richtige Fassung. Das Audit durch das Modell selbst ist bequem, aber ungeprüft.

## Kernaussagen

- Skill-Beschreibungen kurz und auf konkrete Auslöser beschränken, sonst Fehlaktivierung und automatische Kürzung → [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- Root-Skill als Router mit Verweisen statt Volltext, um Kontext zu sparen → [[Kontext-Hygiene-Entscheidungsbaum]]
- Pflichtlektüre in `AGENTS.md` durch kontextuelle Verweise ersetzen und veraltete Anweisungen regelmäßig streichen → [[AGENTS-md-Onboarding-Design]]
- Bei stärkeren Modellen Rezepte durch Ziele ersetzen; Vorgaben nach Fragilität dosieren → [[Freiheitsgrad-nach-Aufgaben-Fragilitaet]]

## Verbindungen

- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- [[AGENTS-md-Onboarding-Design]]
- [[Freiheitsgrad-nach-Aufgaben-Fragilitaet]]
- [[2026-07-01-anthropic-skill-creator-skill-md]]
- [[2026-07-06-mattpocock-writing-great-skills-beyond-skills]]
- [[2026-02-26-omarsar0-agents-md-evaluation]]
- [[2026-07-27-cerebras-gpt-5-6-modellwahl-und-reasoning]]
