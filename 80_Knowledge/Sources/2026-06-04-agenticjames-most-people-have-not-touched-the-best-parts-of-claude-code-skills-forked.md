---
url: https://www.tiktok.com/@agentic.james/video/7647517398890794253
autor: "@agentic.james"
datum: 2026-06-04
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-06-04-agenticjames-most-people-have-not-touched-the-best-parts-of-claude-code-skills-forked.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Drei ungenutzte Skill-Features in Claude Code: Fork-Kontext, Argumente, imperative Descriptions

Ein knapp zweiminütiges Erklärvideo, das drei Frontmatter- und Prompting-Techniken für Claude-Code-Skills nennt: einen Skill in einem geforkten Context Window mit eigenem Modell laufen lassen, Parameter per `$ARGUMENTS` durchreichen und die `description` imperativ formulieren. Es sind Praxishinweise ohne Messung; die Belastbarkeit beruht auf dem Verhalten von Claude Code selbst, nicht auf Belegen im Video. Das Transkript ist automatisch erzeugt (etwa „Sonic“ statt Sonnet, „fork parameter“ statt eines Feldes `context: fork`). Am Ende steht Werbung für einen Kurs und einen Lead-Magnet („Comment SKILLS“).

## Fork-Kontext mit eigenem Modell

Im YAML-Frontmatter eines Skills lässt sich `context: fork` setzen. Der Skill läuft dann in einem separaten Context Window als Subagent, und zusätzlich kann per `model` ein anderes Modell gewählt werden. Das Beispiel des Autors: Die Hauptsession läuft auf einem günstigeren Modell (Sonnet), ein Architektur-Review-Skill bekommt `model: opus`, sodass das teure Modell nur für diese Aufgabe Tokens verbraucht. Der Nutzen ist doppelt: Kostensteuerung pro Aufgabentyp und ein Review-Ergebnis, das den Hauptkontext nicht mit dem gelesenen Code füllt. Ob der Fork nur das Ergebnis zurückgibt und welche Teile des Hauptkontexts der Fork sieht, sagt das Video nicht.

## Parametrisierte Skills mit `$ARGUMENTS`

Steht die Variable `$ARGUMENTS` im Skill-Text, wird sie beim Aufruf durch das ersetzt, was hinter dem Slash-Command steht, etwa `/docx <Datei>`. Damit werden Skills zu wiederverwendbaren, parametrisierten Kommandos statt starrer Prompts.

## Description als Anweisung

Die `description` steht oben im Frontmatter und entscheidet, ob Claude den Skill von sich aus aufruft. Empfohlen wird ein imperativer Ton („You must use this skill when …“) plus explizite Trigger-Wörter. Das ist eine Erfahrungsregel; eine Trigger-Rate wird nicht gemessen.

## Einordnung

Die drei Techniken sind Claude-Code-Funktionen, die sich in der Dokumentation prüfen lassen; das Video liefert keine eigenen Zahlen. Neu gegenüber dem Bestand ist vor allem die Kombination Fork plus Modellwahl als Kostenhebel auf Skill-Ebene, während Eskalation sonst meist über die Session-Modellwahl gedacht wird. Kosten: Ein Fork bekommt keinen Zugriff auf den Gesprächsverlauf im Hauptkontext, du musst also alles Nötige in den Skill oder die Argumente packen. Die imperative Description erhöht die Auslösewahrscheinlichkeit, kann aber auch zu Fehlauslösungen führen; ohne Eval bleibt offen, ob sie wirklich besser triggert. Der Kurs- und Lead-Magnet-Kontext färbt die Aussage „die meisten nutzen das nicht“ als Marketing.

## Kernaussagen

- `context: fork` plus `model:` im Skill-Frontmatter beschränkt ein teures Modell auf genau eine Aufgabe → [[Modell-Eskalation-von-guenstig-nach-teuer]]
- Ein Fork hält den Hauptkontext frei von umfangreichem Lese-Material → [[Kontext-Hygiene-Entscheidungsbaum]]
- Imperative Descriptions mit expliziten Triggern sollen Skills zuverlässiger auslösen; ungemessen → [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]

## Verbindungen

- [[Modell-Eskalation-von-guenstig-nach-teuer]]
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- [[2026-02-09-pdrmnvd-how-claude-code-skills-work]]
- [[2026-07-01-anthropic-skill-creator-skill-md]]
