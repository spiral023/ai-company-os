---
url: https://x.com/ashpreetbedi/status/2011220028453241218
autor: "Ashpreet Bedi (@ashpreetbedi)"
datum: 2026-01-14
erfasst: 2026-08-05
typ: tweet
rohquelle: 00_Inbox/Quellen/X/2026-01-14-ashpreetbedi-claude-code-spec-first.md
beleg_art: sekundaerquelle
---

# Spec-First Development: Ein persistenter Spec-Ordner statt Chat-Gedächtnis

Ashpreet Bedi, Maintainer der Open-Source-Multi-Agent-Runtime Agno, beschreibt in einem X-Thread seinen kompletten Umbau der eigenen Arbeitsweise auf Claude Code: Er orchestriert nur noch, Claude übernimmt Design, Implementierung, Tests und Dokumentation. Der Thread liegt hier ausschließlich als vibedeck-Aufarbeitung vor — eine Primärquelle wurde nicht separat erfasst, daher stammt jede Aussage dieser Notiz aus zweiter Hand und ist nicht gegen den Originaltext geprüft. Kernstück ist ein privates, per Symlink eingebundenes `specs/`-Repository mit fünf festen Dateien pro Feature, das als externes, git-unsichtbares Gedächtnis über Sessions und Kontextlimits hinweg fungiert.

## Der Spec-Ordner: fünf Dateien als externes Feature-Gedächtnis

Bedi symlinkt ein privates `specs/`-Repository in sein Agno-Repo; der Symlink steht in `.gitignore` — unsichtbar für Git, aber sichtbar für Claude. Jedes Feature folgt darin derselben Struktur aus fünf Dateien, die laut eigener Angabe fast vollständig von Claude selbst geschrieben werden:

- **`design.md`** ist die Source of Truth. Details werden zwischen Bedi und Claude abgestimmt, bevor überhaupt Code entsteht — seine Regel: „Keine Spec, keine Implementierung.“
- **`implementation.md`** verfolgt den Fortschritt (erledigt/blockiert) und trägt die Session-Kontinuität: Stößt die Konversation an ein Kontextlimit und muss neu gestartet werden, macht Claude anhand dieser Datei dort weiter, wo sie aufgehört hat.
- **`decisions.md`** hält das Warum hinter Entscheidungen fest, damit sowohl der Agent als auch Bedis „zukünftiges Ich“ spätere Weichenstellungen nachvollziehen können.
- **`prompts.md`** speichert wiederverwendbare Prompts für wiederkehrende Aufgaben (Design-Docs mit der Codebase resynchronisieren, verfeinern, reviewen, nach neuer Implementierung testen).
- **`future-work.md`** parkt zurückgestellte Ideen, die später wieder aufgegriffen werden können.

## Geschichtete CLAUDE.md und der Workflow in neun Schritten

Zusätzlich zur Spec-Struktur setzt Bedi zwei Ebenen von `CLAUDE.md` ein: eine auf Repo-Ebene, die beschreibt, wie Claude durch die Codebase navigiert, und bleibt stabil; eine auf Feature-Ebene, die vorgibt, wie an diesem konkreten Feature gearbeitet wird, und sich mit der Arbeit weiterentwickelt. Öffnet er Claude Code im Agno-Repo, um an einem Feature zu arbeiten, sieht Claude beide Anweisungssätze gleichzeitig.

Der eigentliche Ablauf pro Feature, so wie Bedi ihn beschreibt: Er transkribiert eine Idee bewusst „schlecht“ und unstrukturiert per Whisper Flow; Claude prüft Codebase und `specs/`-Repo und schreibt daraus ein Design-Dokument; Bedi überprüft es vollständig — hier fließe der Großteil seiner eigenen Denkarbeit hin; er beauftragt Claude mit einem konkreten Teilstück, dann mit Cookbooks und Tests dazu; er prüft das Ergebnis, lässt testen und verbessern, iteriert bis es passt; Claude aktualisiert `implementation.md`; erst danach geht es zum nächsten Teilstück. Entscheidend sei, dass Claude immer nur an einem kleinen Stück gleichzeitig arbeitet — als Faustregel gilt, dass ein Pull Request unter zehn Minuten Reviewzeit brauchen soll, was Bedi direkt in der `CLAUDE.md` erzwingt.

## Cookbooks als Fertigstellungskriterium

Jedes implementierte Pattern muss laut Bedi ein ausführbares Beispiel bekommen — ohne Ausnahme. Läuft das zugehörige Cookbook nicht, gilt die Implementierung als nicht fertig, unabhängig davon, wie sauber der Code aussieht. Für das Feature „Learning Machines“ nennt er 26 Cookbook-Dateien über acht Ordner, von denen laut eigener Aussage jede einzelne läuft. Claude führt die Cookbooks demnach selbst aus und protokolliert die Ergebnisse in einer `TESTING.md`; als Beleg verweist der Thread auf eine `testing.md` im öffentlichen Agno-Repository (`github.com/agno-agi/agno`). Das Repo ist nicht Teil von `external_repos/` in diesem System, die Behauptung lässt sich hier also nicht stichprobenartig nachprüfen.

## Plan Mode, Modellwahl und Kontext-Disziplin

Bedi nutzt konsequent den eingebauten Plan Mode (`Shift+Tab`), weil direkte Implementierungssprünge in der komplexen Agno-Codebase nach eigener Erfahrung durchgehend schlechte Ergebnisse lieferten. Sein Prinzip ist Front-Loading: Architekturentscheidungen, Edge Cases und Constraints vor der Umsetzung einbringen, nicht danach — fünf Minuten Planung hätten ihm nach eigener Einschätzung Stunden gespart. Auch hierfür diktiert er lieber, als zu tippen. Als Modell setzt er Opus 4.5 ein, kommentiert mit „iykyk“ ohne weitere Begründung, und bilanziert im Fazit unbelegt „Opus 4.5 ist AGI“ — reine Zuspitzung, keine Messung. In seiner Zusammenfassung nennt er eine Kontext-Degradationsschwelle von 30 % Fensterauslastung, ab der er auf eine Konversation pro Feature und externes Gedächtnis via Spec-Files statt Chatverlauf setzt, plus `Clear` bei Bedarf. Trotz der Aussage, Claude schreibe „100 % meines Codes“, betont er ausdrücklich, weiterhin jede Zeile zu reviewen — nur das Tippen entfällt, nicht die Prüfung.

## Einordnung

Diese Notiz beruht vollständig auf der vibedeck-Sekundäraufarbeitung eines einzelnen X-Threads; ohne erfasste Primärquelle lässt sich weder die genaue Wortwahl noch die Vollständigkeit der Wiedergabe prüfen. Alle Zahlen — fünf Tage Bauzeit für „Learning Machines“, 26 Cookbook-Dateien über acht Ordner, „100 % des Codes von Claude geschrieben“ — sind unbelegte Selbstangaben einer Einzelperson, keine Messungen, und „Opus 4.5 ist AGI“ sowie „iykyk“ sind Zuspitzung statt Aussage.

Der Kern der Quelle — ein persistenter, dateibasierter Spec-Ordner pro Feature als externes Gedächtnis, das Planung (`design.md`), Fortschritt (`implementation.md`) und Rationale (`decisions.md`) explizit voneinander trennt — deckt sich im Grundprinzip mit dem bereits verifizierten [[Plan-first-mit-getrenntem-Review]] (Plan als persistentes Artefakt vor der Umsetzung) und mit [[Handoff-Doc]] (externer Zustand überlebt Kontextlimits). Boris Tanes ähnlich benannter, aber inhaltlich anderer Workflow ([[2026-02-10-boris-tane-plan-annotation-workflow]]) trennt nur zwei Artefakte (`research.md`/`plan.md`) für die aktuelle Aufgabe; Bedis Struktur ist breiter (fünf Dateien, inklusive Decision-Log und wiederverwendbarer Prompts) und dauerhaft pro Feature statt pro Task angelegt — keine inhaltliche Dublette, sondern eine eigenständige, aufwendigere Umsetzung derselben Grundidee. Weder `decisions.md` als eigenständiges Rationale-Log noch `prompts.md`/`future-work.md` als feste Bestandteile eines solchen Ordners sind durch ein bestehendes Pattern vollständig abgedeckt — neues Pattern vorgeschlagen (siehe Abschlussbericht).

Die zweistufige `CLAUDE.md` (Repo-Ebene stabil, Feature-Ebene entwickelt sich mit) ist eine unabhängige, praktische Bestätigung der bei [[AGENTS-md-Onboarding-Design]] bereits als Anthropic-Beleg vermerkten Parent/Child-Lademechanik von `CLAUDE.md`-Dateien — hier aus der Perspektive eines Drittautors, nicht der offiziellen Doku.

Die genannte 30-%-Kontext-Degradationsschwelle ist ein weiterer, unbelegter Einzelwert im bereits bei [[Kontext-Hygiene-Entscheidungsbaum]] dokumentierten Streit unterschiedlicher Schwellenangaben (dort 20-40 %, „ca. 45 %“ und eine 300k-400k-Token-Heuristik) — sie löst die Spannung nicht auf, sondern fügt eine weitere, ebenfalls unbelegte Stimme hinzu.

Das „Cookbooks or it didn't happen“-Prinzip — Fertigstellung wird an ein lauffähiges, selbst ausgeführtes Beispiel gekoppelt, nicht an den optischen Eindruck des Codes — passt genau in die bereits belegte Logik von [[Testharness-als-staerkster-Hebel]] und die vertikalen Slices aus [[TDD-als-Verifikationshebel]]: Ein Cookbook ist hier faktisch der Verifier. Der Rollenwechsel „Ich orchestriere nur noch“ bei gleichzeitig festgehaltenem Zeile-für-Zeile-Review bestätigt unabhängig die in [[Great-Decoupling-Rollenverstaendnis]] beschriebene Trennung von Programming und Engineering.

## Kernaussagen

- Ein privates, git-unsichtbares `specs/`-Repo mit fünf festen Dateien (`design.md`, `implementation.md`, `decisions.md`, `prompts.md`, `future-work.md`) dient als externes Gedächtnis pro Feature; `design.md` ist Source of Truth vor jeder Implementierung, `implementation.md` trägt die Session-Kontinuität über Kontextlimits hinweg → [[Plan-first-mit-getrenntem-Review]] · [[Handoff-Doc]] · neues Pattern vorgeschlagen (siehe Abschlussbericht)
- Zwei `CLAUDE.md`-Ebenen (Repo-Ebene stabil/navigierend, Feature-Ebene entwickelt sich mit der Arbeit) werden beim Öffnen des Feature-Ordners gemeinsam geladen → [[AGENTS-md-Onboarding-Design]]
- „Cookbooks or it didn't happen“: Jedes implementierte Pattern braucht ein ausführbares Beispiel; ein nicht lauffähiges Cookbook bedeutet „nicht fertig“, unabhängig von der Codequalität; Claude führt die Cookbooks selbst aus und protokolliert Ergebnisse → [[Testharness-als-staerkster-Hebel]] · [[TDD-als-Verifikationshebel]]
- Kleine Arbeitspakete werden über eine in der `CLAUDE.md` erzwungene Faustregel (PR-Review unter zehn Minuten) statt nur durch Empfehlung diszipliniert → [[TDD-als-Verifikationshebel]]
- Plan Mode und Front-Loading von Architektur, Edge Cases und Constraints vor der Implementierung, Ideenerfassung per Diktat statt Tippen → [[Plan-first-mit-getrenntem-Review]] · [[Voice-Prompting-fuer-Kontextreichtum]]
- Rollenwechsel zum reinen Orchestrator bei gleichzeitig festgehaltenem vollständigem Zeile-für-Zeile-Review („ich reviewe immer noch jede Zeile“) → [[Great-Decoupling-Rollenverstaendnis]]
- Selbstberichtete Kontext-Degradationsschwelle von 30 % Fensterauslastung als Grund für eine Konversation pro Feature und externes Gedächtnis statt Chatverlauf → [[Kontext-Hygiene-Entscheidungsbaum]]

## Verbindungen

- [[Plan-first-mit-getrenntem-Review]]
- [[Handoff-Doc]]
- [[AGENTS-md-Onboarding-Design]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Testharness-als-staerkster-Hebel]]
- [[TDD-als-Verifikationshebel]]
- [[Great-Decoupling-Rollenverstaendnis]]
- [[Voice-Prompting-fuer-Kontextreichtum]]
- [[2026-02-10-boris-tane-plan-annotation-workflow]]
