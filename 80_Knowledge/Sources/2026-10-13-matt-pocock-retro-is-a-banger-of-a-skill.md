---
url: https://www.youtube.com/watch?v=Q8XzzKUbp0Y
autor: Matt Pocock
datum: 2026-10-13
erfasst: 2026-10-28
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-10-13-matt-pocock-retro-is-a-banger-of-a-skill.md
thema: Arbeitsweisen
zeitkritisch: ja
---

# Sitzungsfehler in überprüfbare Verbesserungen überführen

Matt Pocock stellt im [kurzen Video zu `retro`](https://www.youtube.com/watch?v=Q8XzzKUbp0Y) eine Retrospektive für Fehler und Reibung in vorangegangenen Agent-Sitzungen vor. Ausgewertet wurden die vollständigen, automatisch erzeugten deutschen und englischen Transkriptspuren; die englische Spur diente dem Wortlautabgleich. Bild und Ton wurden nicht geprüft. Die Quelle erklärt eine Arbeitsweise und Pococks persönliche Einschätzung ihres Nutzens, enthält aber keine gemessene Fehlerreduktion.

## Vom Vorfall zur passenden Absicherung

Die Leitfrage lautet sinngemäß, wodurch derselbe Fehler künftig schwerer zu begehen wäre. Ausgangspunkt sind tatsächlich aufgetretene Fehler und ineffiziente Abläufe. Daraus sollen zwei Arten von Verbesserungen entstehen: deterministische Checks für mechanisch entscheidbare Bedingungen und fachliche Regeln für Code-Reviews, wenn die Beurteilung echtes Ermessen verlangt.

Für [[Helper-Nutzung-durch-Lint-erzwingen]] liefert das den vorgelagerten Anlass: Eine konkrete Sitzung zeigt, welche Fehlhandlung ein bestehender Check künftig erkennen sollte. Das Auswahlkriterium entspricht dem Grundgedanken von [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]: Die Prüfbarkeit der Bedingung bestimmt die Art der Absicherung. Daraus folgt keine pauschale Empfehlung für Harness-Hooks. Eine allgemeine Ermahnung im Regeltext ersetzt keinen mechanischen Check; umgekehrt lässt sich eine fachliche Abwägung nicht allein durch ihr Aufschreiben deterministisch machen.

## Einordnung

Das Video ordnet den Skill der Version `v1.3` zu. Die am 28.10.2026 statisch gesichtete Referenz `skills/engineering/retro/SKILL.md` im lokalen Repo `mattpocock/skills` auf Commit `5beb35b` verlangt Sitzungsevidenz sowie die Prüfung vorhandener Checkcommands und CI. Sie trennt mechanische Fehler von echten Ermessensfragen für `CODING_STANDARDS` und präsentiert Kandidaten nach Schwere. Das konkretisiert dokumentierte Anweisungen eines später gesichteten Stands, belegt aber weder eine Ausführung noch, dass ein Aufruf automatisch alle Änderungen umsetzt. Pococks Begeisterung und seine Kritik an der eigenen Codebasis bleiben persönliche Erfahrung; eine allgemeine Wirksamkeit lässt sich daraus nicht ableiten.

## Kernaussagen

- [[Helper-Nutzung-durch-Lint-erzwingen]]: Konkrete Fehlerevidenz kann den Bedarf für einen deterministischen Check begründen; seine tatsächliche Ausführung und Wirkung müssen getrennt geprüft werden.
- [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]: Die Entscheidung zwischen mechanischer Prüfung und fachlicher Reviewregel folgt der Art des Fehlers, nicht der Vorliebe für ein bestimmtes Werkzeug.

## Verbindungen

- [[2026-10-05-repo-mattpocock-skills-retro]]: Ergänzender Bezug zur dokumentierten Skill-Struktur; Videoaussage und Repository-Stand müssen zeitlich unterschieden werden.
- [[Helper-Nutzung-durch-Lint-erzwingen]]: Konkreter Anschluss für statisch erkennbare Fehler, die nach einer Retrospektive im bestehenden Prüfablauf abgesichert werden können.
- [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]: Verwandtes Entscheidungskriterium für die Grenze zwischen deterministischer Prüfung und erforderlichem Urteil.
