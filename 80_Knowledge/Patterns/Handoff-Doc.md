# Handoff-Doc

**Konfidenz:** verifiziert

## Zweck

Erhält den Arbeitszustand über das Ende einer Session oder eines Kontextfensters hinaus, damit ein neuer Agent (oder derselbe nach einem Neustart) nahtlos weitermachen kann, statt bei null anzufangen.

## Funktionsweise

Ein Skill komprimiert die laufende Konversation in ein Übergabe-Dokument („Handoff Doc“): die relevanten Entscheidungen, der aktuelle Stand, offene Fragen. Der nächste Agent liest dieses Dokument statt der vollständigen Historie und setzt die Arbeit an derselben Stelle fort. Für Vorhaben, die den Rahmen einer einzelnen Session sprengen, gibt es einen verwandten, aber eigenständigen Mechanismus: eine „Landkarte“ aus Untersuchungs-Tickets auf dem Issue-Tracker, die nacheinander abgearbeitet werden, bis der Weg zum Ziel klar ist — statt eines einzelnen Übergabe-Dokuments wird hier der große Auftrag in kleine, session-große Entscheidungs-Häppchen zerlegt. Verwandte Umsetzungen außerhalb des Referenz-Repos: `planning-with-files` (`task_plan.md`/`findings.md`/`progress.md` als persistente Dateien), GSD Core `STATE.md` (überlebt Session-Grenzen) — siehe `external_repos/INDEX.md`.

Ein Handoff kann außerdem bewusst zwischen unterschiedlichen Arbeitsmodi vermitteln: Taucht während eines Grilling eine Wissenslücke auf, wird sie in ein Handoff-Dokument kompaktiert, in einem separaten `/teach`-Workspace bearbeitet und danach die ursprüngliche Grilling-Session fortgesetzt. Das Handoff soll vorhandene Specs, Pläne, ADRs, Issues, Commits oder Diffs nicht duplizieren, sondern auf sie verweisen.

## Vorteile

- Übersteht Kontextfenster-Limits, `/clear` und Session-Abbrüche.
- Reduziert Einarbeitungskosten für eine neue Session erheblich.
- Macht den Übergabepunkt explizit und nachvollziehbar statt implizit im Gedächtnis des vorherigen Agenten.
- Hält den Ursprungskontext sauber, wenn eine Nebenaufgabe wie Lernen einen eigenen persistenten Workspace benötigt.

## Nachteile & Grenzen

- Verdichtung ist verlustbehaftet: Was ins Handoff-Doc aufgenommen wird, entscheidet, was der nächste Agent weiß — Nuancen können verloren gehen.
- Zusätzlicher Schritt/Overhead, der sich bei kurzen Aufgaben innerhalb einer Session nicht lohnt.
- Für Vorhaben, die viele Sessions brauchen, reicht ein einzelnes Handoff-Doc oft nicht — dafür ist die tickets-basierte Landkarte gedacht (siehe Funktionsweise).

## Wann einsetzen, wann nicht

- Einsetzen: lange Sessions kurz vor dem Kontextlimit, Mehr-Sessions-Vorhaben, geplante Übergaben zwischen Agenten.
- Nicht einsetzen: kurze, in einer Session abschließbare Aufgaben.

## Belege

- 2026-07-10 · [[2026-07-10-voxyz-mattpocock-skills]] · meinung — Tweet beschreibt `/handoff` (Konversation → Übergabe-Dokument) und `/wayfinder` (zu große Arbeit → Ticket-Landkarte).
- 2026-07-11 · external_repos/mattpocock/skills/skills/productivity/handoff/SKILL.md · verifiziert — Skill `handoff` existiert im Repo unter `skills/productivity/`.
- 2026-07-11 · external_repos/mattpocock/skills/skills/engineering/wayfinder/SKILL.md · verifiziert — Skill `wayfinder` existiert unter `skills/engineering/`; Beschreibung bestätigt exakt das Tweet-Motiv „Plan a huge chunk of work — more than one agent session can hold — as a shared map of investigation tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear.“
- 2026-07-13 · [[2026-07-13-mattpocock-handoff-to-teach]] · meinung — Matt empfiehlt, Wissenslücken aus einem Grilling per Handoff in einen Teach-Workspace auszulagern und danach zum Grilling zurückzukehren.
- 2026-07-13 · external_repos/mattpocock/skills/skills/productivity/handoff/SKILL.md · verifiziert — Das Handoff wird im temporären OS-Verzeichnis gespeichert, schlägt Skills für die nächste Session vor und verweist auf bestehende Artefakte, statt sie zu duplizieren.
- 2026-07-13 · external_repos/mattpocock/skills/skills/productivity/teach/SKILL.md · verifiziert — `/teach` definiert einen persistenten Teaching-Workspace mit Mission, Ressourcen, Lessons und Learning Records.
- o. D. (gesichtet 2026-07-14) · external_knowledge/ai-llm-wiki/raw/coding-agents-continuity.md · meinung — Liefert die konzeptionelle Begründung des Patterns in einem Satz: „Context is what the agent has available now. Continuity is what lets the next execution continue from what actually happened before.“ Größere Kontextfenster lösen das Session-Grenzen-Problem explizit nicht — „Continuity is the bridge between sessions.“
- 2026-05-27 · external_knowledge/ai-llm-wiki/raw/drowning-in-context.md (G. Vetukuri) · meinung — Ergänzt das Architektur-Pendant: „Structured Handoff Packets“ — zusammengefasste Checkpoints statt Roh-History an den nächsten Bearbeitungsschritt übergeben, als eine von drei Mitigationen gegen Context Rot.
- 2026-02-14 · [[2026-02-14-minty-mastering-claude-code]] · meinung — `sessions.md` als rollierendes Log der letzten fünf Sessions mit Handoff-Kontext ist eine unabhängige, funktional passende Umsetzung desselben Prinzips außerhalb des Referenz-Repos.
- 2026-02-10 · [[2026-02-10-boris-tane-plan-annotation-workflow]] · meinung — Ein persistentes `plan.md`-Dokument fungiert selbst als Handoff-Artefakt: Es überlebt Auto-Compaction in voller Genauigkeit, worauf der Autor Claude jederzeit erneut verweisen kann, statt ein separates Übergabe-Dokument zu erzeugen.
- 2026-01-25 · [[2026-01-25-sankalp-claude-code-experience]] · meinung — Ein eigener `/handoff`-Custom-Command wird bewusst vor dem automatischen `/compact` ausgelöst (typischerweise bei ca. 60 % Kontextauslastung), bevor die Session beendet und neu gestartet wird — aktive statt reaktive Nutzung des Handoff-Mechanismus.
- 2026-02-01 · [[2026-02-01-aiedge-claude-code-starter-pack]] · meinung — Ein Power-User meidet Plan Mode dauerhaft (fehlende Tool-Rechte-Vererbung, Stand Dez. 2025) und ersetzt sie durch eine eigenständige, funktional passende Umsetzung dieses Patterns: Der Agent stellt Klärungsfragen, die in eine Markdown-Datei übertragen und dort beantwortet werden, statt eines Session-Übergabe-Dokuments als bewusste Alternative zu Plan Mode selbst.
- 2026-08-03 · [[2026-08-03-steffen_hauptmann-die-meisten-lassen-sich-ein-handover-erst-schreiben-wenn-das]] · meinung — Laufend gepflegte STATE.md statt Handover erst bei vollem Context Window; nur für Solo-Arbeit, selbstberichtet, im Team nicht eingecheckt.
- 2026-02-05 · [[2026-02-05-kloss-xyz-feature-intelligence-architect]] · meinung — Freigegebener FEATURE_PLAN als Ausführungsvertrag für den Build-Agenten; nur Prompt-Design, kein Nachweis.
- 2026-03-21 · [[2026-03-21-sourfraser-claude-obsidian-ai-employee]] · meinung — Call-Transkripte werden täglich in Entscheidungen, Actions und Kundendateien im Vault überführt (Memory Loop); Qualität der Extraktion ungeprüft.
- 2026-08-12 · [[2026-08-12-voxyz_ai-2087579867139264681]] · meinung — Nutzt Handoff-Notizen anderer Agenten als Eingabe und fordert Rückgabe von Änderungen, Tests und Blockern; keine Belege zur Wirkung.
- 2026-02-02 · [[2026-02-02-anthony-riera-planning-with-files-skill]] · meinung — Dateibasierter Plan als externer Speicher über lange Sessions; bekannte Arbeitsweise unter neuem Skill-Namen.
- 2026-10-06 · [[2026-10-06-voxyz_ai-2107455844992299272]] · meinung — Vox verdichtet Projektteile, Meilensteine und ausstehende Entscheidungen in einer visuell lesbaren HTML-Karte für den späteren Wiedereinstieg; ein Sessionwechsel oder vollständiger Übergabekontext wird nicht beschrieben, weshalb die Karte ein Handoff ergänzt und nicht ersetzt.

## Spannungen & offene Fragen

- Keine Spannung zu `planning-with-files` oder GSD `STATE.md` bekannt — beide verfolgen dasselbe Grundprinzip (Zustand auf Platte statt im flüchtigen Kontext), mit unterschiedlicher Formatwahl.

## Verwandte Patterns

- [[Skill-Call-Hierarchie]]
- [[Task-basierte-Steuerung]]
