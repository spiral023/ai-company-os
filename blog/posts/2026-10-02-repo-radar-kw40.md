---
titel: "Repo-Radar KW 40: Evals per Befehl, Claude Mods und ein Launch-Video aus dem Projekt"
datum: 2026-10-02
kategorie: tools
zusammenfassung: "Acht Repos mit neuen Funktionen in dieser Woche: Eval-Flows im claude-api-Skill, Mods und /diff in Claude Code, /test-audit, ein Stack-Modus für Drittanbieter-Modelle, ein Motion-Scan, eine Frontend-CLI, die Umbenennung von CONTEXT.md und /brag."
status: freigegeben
geprueft_am: 2026-10-02
quellen:
  - 2026-10-02-repo-anthropics-skills
  - 2026-10-02-repo-anthropics-claude-code
  - 2026-10-02-repo-garrytan-gstack
  - 2026-10-02-repo-farion1231-cc-switch
  - 2026-10-02-repo-jakubantalik-transitions-dev
  - 2026-10-02-repo-thedaviddias-front-end-checklist
  - 2026-10-02-repo-mattpocock-skills
  - 2026-10-02-repo-latent-spaces-brag
  - 2026-10-01-julian-ivanov-ki-automat-claude-code-ist-unglaublich-gut-in-motion-graphi
---

## Kurz gesagt

- Du baust eine Claude-App um oder änderst einen Prompt: Lass dir mit `/claude-api build-eval` ein Eval bauen, bevor du etwas anfasst. {q:1}
- Du arbeitest in Claude Code: Probiere `/diff`, den eingebauten Änderungs-Überblick neben dem Transkript. {q:2}
- Du nutzt die Skills von Matt Pocock mit einer `CONTEXT.md`: Die nächste Version sucht nur noch `GLOSSARY.md`. Benenne die Datei um, sobald du aktualisierst. {q:7}
- Die übrigen Werkzeuge testest du an einem Nachmittag; die Reihenfolge steht am Ende.

## Evals und Qualität

**anthropics/skills.** Der `claude-api`-Skill bringt vier Anleitungen unter `shared/evals/` mit: `build-eval`, `eval-hillclimb`, `cost-hillclimb` und `eval-audit`. {q:1} Der erste führt per Interview zu einem Eval samt Runner-Skript, der zweite verbessert die App Runde für Runde gegen dieses Eval, der dritte sucht gezielt nach niedrigeren Kosten bei gleicher Qualität, der vierte ist die Checkliste, ob ein Eval überhaupt taugt. {q:1} Aufrufen kannst du sie mit `/claude-api build-eval` und `/claude-api hillclimb`. {q:1} Warum der Train/Test-Split dabei wichtig ist, steht im Beitrag [Hillclimbing mit Holdout](post:hillclimbing-mit-holdout).

**garrytan/gstack.** Der neue Skill `/test-audit` sucht in deiner Testsuite nach wertarmen, doppelten und an die Implementierung gekoppelten Tests. {q:3} Jeder Fund kommt mit einer Karte, die erklärt, was der Test erkennt, wer sonst davon abhängt und was bei Stilllegung bleibt. {q:3} Geändert wird nichts ohne deine Freigabe; mit `--since <ref>` begrenzt du den Lauf auf neuere Änderungen. {q:3} Der Hintergrund ist die „Test Value Bar“: Ein Test zählt nur, wenn er eine echte Regression fangen würde. {q:3}

## Claude Code

**anthropics/claude-code, Version 2.1.287.** Neu sind Claude Mods, also Plugins mit tieferem Zugriff auf das Verhalten von Claude Code. {q:2} Vier davon sind eingebaut, ihr Quelltext liegt unter `mods/`. {q:2} Am schnellsten nützlich ist `/diff`: Es zeigt die uncommitteten Änderungen Datei für Datei in einem Panel neben dem Gespräch und aktualisiert sich, während Claude editiert. {q:2} „You should know“ schickt einen Seitenagenten los, der auf Übersehenes hinweist; du schaltest ihn mit `/plugin enable cc-plugin-you-should-know@builtin` ein, er läuft laut Changelog nur bei aktiver Telemetrie. {q:2} Außerdem gilt auf Bedrock, Vertex und Foundry jetzt ein 1M-Kontext als Standard für Opus 4.7 und neuer; `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` hält ihn bei 200K. {q:2}

## Modelle

**farion1231/cc-switch.** Der neue Stack-Modus hängt Modelle mehrerer Anbieter an Claude Code und Codex. {q:4} Du trägst pro Anbieter die Modelle ein, wählst sie danach im `/model`-Menü, und die Anfrage geht direkt an diesen Anbieter. {q:4} Aktivieren musst du den Schalter in den Einstellungen von cc-switch, und nach jeder Änderung braucht der Client einen Neustart. {q:4} Ein Failover gibt es im Stack-Modus nicht. {q:4} Sinnvoll, wenn du ein günstiges Zweitmodell neben dem Hauptmodell im selben Client greifbar haben willst.

## UI und Frontend

**Jakubantalik/transitions.dev.** Der „Transitions Agent“ bewertet die Animationen deines Projekts mit einem Score von 0 bis 100. {q:5} `npx transitions-agent` scannt, `npx transitions-agent fix` schlägt Korrekturen als Diff vor, und `init-ci` richtet eine GitHub Action ein, die jeden Pull Request prüft. {q:5} Der Scan läuft lokal; gehostete Fixes brauchen Konto und Lizenz. {q:5} Wer lieber sein eigenes Claude arbeiten lässt, bindet den MCP-Server des Agenten ein. {q:5}

**thedaviddias/Front-End-Checklist.** Die neue CLI `@frontendchecklist/cli` bringt die Regeln offline mit. {q:6} `npx -y @frontendchecklist/cli review src/` prüft deinen Code, `audit <url>` eine öffentliche Seite, und ein Exit-Code ab `--fail-on` macht daraus ein CI-Gate. {q:6} Der MCP-Server liefert dieselben Regeln an Agenten, zum Beispiel über `review_code` und `audit_url`. {q:6} Wie du damit eine App vor dem Start gezielt angreifst, steht in [App vor dem Launch angreifen](post:pre-launch-app-angreifen).

## Workflow-Skills

**mattpocock/skills.** `implement-spec`, `pr` und `retro` liegen jetzt im stabilen Ordner `skills/engineering/`. {q:7} `implement-spec` setzt eine Spec samt Tickets auf einem Integrationsbranch um, `pr` liefert die Vorlage für den PR-Text, `retro` wertet eine Sitzung aus und schlägt Verbesserungen an deiner Agent-Umgebung vor. {q:7} Wichtiger für bestehende Projekte: Im Hauptzweig wird aus `CONTEXT.md` die Datei `GLOSSARY.md` und aus `CONTEXT-MAP.md` die Datei `GLOSSARY-MAP.md`; veröffentlicht ist das noch nicht, die aktuelle Version bleibt beim alten Namen. {q:7} Ab der nächsten Version suchen die Skills nur noch den neuen Namen. Führe `git mv CONTEXT.md GLOSSARY.md` deshalb erst aus, wenn du auf diese Version aktualisierst. {q:7}

## Neuzugang

**latent-spaces/brag.** `/brag` erzeugt aus deinem Projekt ein kurzes Launch-Video mit Musik, Motion und Texten zum Teilen, gebaut auf Hyperframes. {q:8} Installation in Claude Code: `/plugin marketplace add latent-spaces/brag`, dann `/plugin install brag@brag`. {q:8} Unter Opus 5.5 schaltet `/brag` selbst auf `/brag-slim` um, eine schlankere Fassung ohne Hyperframes; `/brag --full` erzwingt den klassischen Ablauf. {q:8} Unabhängige Ergebnisse gibt es noch nicht. Ein Creator zeigt in einem Video, dass Claude Code mit Opus 5.5 und Hyperframes Motion Graphics als Code baut und seine Frames per Screenshot selbst prüft; die Ergebnisse sieht man nur dort, Laufzeiten von 15 Minuten bis etwa einer Stunde nennt er selbst. {q:9}

## Womit anfangen

Starte mit dem, was nichts kostet und sofort etwas zeigt: `/diff` in Claude Code und `npx -y @frontendchecklist/cli review src/` an einem echten Projekt. Wenn du ohnehin ein Modell oder einen Prompt wechselst, lohnt sich danach `/claude-api build-eval`. Die Umbenennung von `CONTEXT.md` gehört auf deine Liste für das nächste Skill-Update.
