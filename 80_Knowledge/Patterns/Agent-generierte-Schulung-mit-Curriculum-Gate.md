# Agent-generierte Schulung mit Curriculum-Gate

**Konfidenz:** meinung

## Zweck

Erzeugt wiederholbar interaktive Lernangebote mit einem Coding Agent, ohne teure Medienproduktion zu starten, bevor Zielgruppe, Lernziele und Aufbau geprüft sind.

## Funktionsweise

Ein user-invoked Skill orchestriert fünf Phasen: (1) Briefing zu Zielgruppe, Vorwissen, Sprache, Dauer und Gestaltung; (2) Curriculum mit Lernzielen, Leveln, Lehrtexten und Voiceover-Skripten; (3) menschliches Review mit explizitem Freigabe-Gate; (4) Generierung ausgewählter Bild-, Audio- und Video-Assets über externe Tools; (5) Montage als interaktive HTML-Anwendung. Quizfragen, Slider, Zuordnungsaufgaben, Feedback und Fortschrittslogik entstehen überwiegend direkt in HTML; aufwendigere Medien ergänzen nur ausgewählte Lektionen.

## Vorteile

- Verlegt inhaltliche Korrekturen vor die kostenpflichtige Asset-Generierung.
- Macht den Ablauf durch einen Skill für neue Themen wiederholbar.
- Eine einzelne HTML-Datei lässt sich lokal öffnen, weiterbearbeiten und an ein Designsystem anpassen.
- Aufgaben und direktes Feedback ermöglichen aktive Anwendung statt rein passivem Videokonsum.

## Nachteile & Grenzen

- Bisher nur durch eine Creator-Demo belegt; keine unabhängige Messung von Lernwirkung oder Produktionsqualität.
- Fachliche Inhalte brauchen ein separates Expertenreview, besonders bei Recht, Compliance, Sicherheit oder Medizin.
- Single-File-HTML ersetzt nicht automatisch LMS-Funktionen wie Nutzerverwaltung, Lernstands-Synchronisierung, Reporting und standardisierte Kursformate.
- Externe Medienmodelle verursachen variable Kosten und können inkonsistente oder unbrauchbare Assets liefern.
- Accessibility, Browser-Kompatibilität, Datenschutz und Wartbarkeit müssen zusätzlich geprüft werden.

## Wann einsetzen, wann nicht

- Einsetzen: Prototypen, interne Schulungen, Onboarding oder Kursmodule, wenn schnelle Anpassbarkeit und lokale Auslieferung wichtiger als ein vollständiges LMS sind.
- Nicht einsetzen: rechtlich oder fachlich kritische Pflichtschulungen ohne Expertenfreigabe; Kurse mit verbindlichem Tracking, Zertifizierung oder komplexer Mehrbenutzerverwaltung.

## Belege

- 2026-07-30 · [[2026-07-30-julian-ivanov-interaktive-schulungen-mit-claude-code]] · meinung — Creator-Demo zeigt den vollständigen Ablauf vom Agenten-Briefing über Curriculum-Review und Mediengenerierung bis zu einer interaktiven Single-File-HTML-Schulung.

## Spannungen & offene Fragen

- Die Single-File-Auslieferung vereinfacht Prototyping und lokale Nutzung, steht aber im Spannungsverhältnis zu LMS-Anforderungen wie Tracking, Rollen, Updates und Nachweisen.
- Offen ist, wie gut fachliche Richtigkeit, Lernwirkung und Barrierefreiheit über viele Themen und Kurslängen hinweg erhalten bleiben.

## Verwandte Patterns

- [[Spec-Grilling]]
- [[Plan-first-mit-getrenntem-Review]]
- [[Skill-Call-Hierarchie]]
- [[Claude-als-Lernwerkzeug]]
