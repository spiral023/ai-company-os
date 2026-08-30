---
url: https://www.youtube.com/watch?v=gz0PBC2P9eg
autor: "Julian Ivanov | KI-Automatisierung"
datum: 2026-07-30
erfasst: 2026-08-30
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-07-30-julian-ivanov-ki-automat-so-erstellst-du-interaktive-schulungen-mit-claud.md
---

# Vom Briefing zur interaktiven Schulung in einer HTML-Datei

Ein wiederverwendbarer Skill steuert Claude Code vom ersten Briefing bis zu einer interaktiven Schulung: Der Agent klärt Zielgruppe und Rahmen, legt ein Curriculum zur Freigabe vor, erzeugt nach dem menschlichen Go Medien und montiert alles zu einer einzelnen HTML-Datei. Der entscheidende Workflow-Gedanke ist die Trennung zwischen günstig prüfbarer Konzeption und der anschließenden, teilweise kostenpflichtigen Produktion.

## Briefing und Curriculum vor Produktion

Der im Video gezeigte `/schulung`-Skill startet nicht direkt mit der Generierung. Er fragt zunächst unter anderem nach Zielgruppe, Vorwissen, Sprache, Dauer, Anzahl der Level und visuellem Stil. Für unklare Vorhaben empfiehlt Ivanov zusätzlich einen ausführlicheren Interview-Skill. Aus den Antworten erstellt Claude ein Curriculum mit Lernzielen, Level-Struktur, Lehrtext und Voiceover-Inhalten.

Dieses Curriculum ist ein explizites Review-Gate: Der Mensch soll Inhalt und Aufbau prüfen, Feedback geben und erst danach mit einem „Go“ die eigentliche Produktion auslösen. Das ist besonders relevant, weil fehlgeleitete Bild-, Audio- und Videogenerierungen Geld und Zeit kosten. Die Quelle überträgt damit [[Spec-Grilling]] und [[Plan-first-mit-getrenntem-Review]] auf Content-Produktion.

## Skill- und Tool-Pipeline

Der Skill beschreibt den gesamten Ablauf und die benötigten Werkzeuge. Laut Demo erzeugt Claude nach der Freigabe Referenzbilder für konsistente Figuren und Umgebungen, Stimmen sowie einzelne Videosequenzen. Ein in der Videobeschreibung verlinkter Higgsfield-MCP-Zugang stellt die externen Medienmodelle bereit; HyperFrames dient laut Video dazu, HTML-basierte Animationen als Video zu rendern. Claude koordiniert die Prompts und Assets innerhalb derselben Arbeitssession.

Der Großteil der Lernanwendung bleibt HTML: Navigation, Slider, Quizfragen, Drag-and-drop-Aufgaben, direktes Feedback, XP und Fortschritts-Gates werden als Code erzeugt. Aufwendige generative Videos kommen nur punktuell zum Einsatz. Das Ergebnis ist eine einzelne HTML-Datei, deren Umfang, Inhalte und Branding anschließend weiter angepasst werden können.

## Lernen durch aktive Anwendung

Die Demo kombiniert kurze Erklärsequenzen mit Selbsteinschätzung, Zuordnungsaufgaben und unmittelbarem Feedback. Teilnehmende können bestimmte Abschnitte erst nach einer gelösten Aufgabe abschließen. Gegenüber einem linearen Erklärvideo entsteht so ein ausführbares Lernartefakt, das Wissen nicht nur präsentiert, sondern direkt abfragt und anwenden lässt.

## Einordnung

Die Quelle ist eine Creator-Demo mit zwei sichtbaren Beispielkursen, aber kein unabhängiger Qualitäts- oder Wirksamkeitsnachweis. Weder fachliche Richtigkeit noch Lernwirkung, Accessibility, Browser-Kompatibilität, Datenschutz oder Wartbarkeit werden systematisch getestet. Aussagen zu Produktionskosten und Modellqualität sind zeitabhängige Selbstauskünfte. Die im Beispielkurs vorkommenden Aussagen zur EU-KI-Verordnung wurden für diese Workflow-Aufarbeitung nicht rechtlich geprüft.

Die Produktnamen sind im automatisch erzeugten YouTube-Transkript mehrfach entstellt; ihre Schreibweise wurde nur dort normalisiert, wo die Videobeschreibung oder der sichtbare Kontext sie eindeutig macht. HyperFrames ist nicht unter `external_repos/` vorhanden und wurde daher nicht lokal verifiziert.

## Kernaussagen

- Ein Agenten-Interview klärt Zielgruppe, Dauer, Lernziele und Gestaltung vor der Kurserstellung → [[Spec-Grilling]]
- Ein prüfbares Curriculum bildet das Freigabe-Gate vor kostenpflichtiger Mediengenerierung → [[Plan-first-mit-getrenntem-Review]]
- Ein Skill kann Briefing, Medien-Tools und HTML-Generierung zu einem wiederholbaren Kurs-Workflow orchestrieren → [[Agent-generierte-Schulung-mit-Curriculum-Gate]]
- Interaktive HTML-Elemente tragen den Großteil der Lernerfahrung; generative Videos bleiben optionale, punktuelle Assets → [[Agent-generierte-Schulung-mit-Curriculum-Gate]]

## Verbindungen

- [[Skill-Call-Hierarchie]]
- [[Claude-als-Lernwerkzeug]]
- [[Klein-und-komposierbar]]
