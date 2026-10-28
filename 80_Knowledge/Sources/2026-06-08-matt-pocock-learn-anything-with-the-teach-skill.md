---
url: https://www.youtube.com/watch?v=s5T5oQJcJ6U
autor: Matt Pocock
datum: 2026-06-08
erfasst: 2026-10-28
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-06-08-matt-pocock-learn-anything-with-the-teach-skill.md
thema: Arbeitsweisen
zeitkritisch: ja
---

# Lernen über mehrere Sitzungen: Mission, Lernjournal und passende Übungen

Matt Pocock beschreibt im [Video zum `teach`-Skill](https://www.youtube.com/watch?v=s5T5oQJcJ6U) einen persönlichen Lernarbeitsraum, der Ziele, Ressourcen und Fortschritt außerhalb des Chats festhält. Grundlage dieser Auswertung sind Videobeschreibung und vollständiges, automatisch erzeugtes englisches Transkript; Bild und Ton wurden nicht geprüft. Das Rubik-Beispiel macht die beabsichtigte Arbeitsweise anschaulich, liefert aber keinen kontrollierten Nachweis besserer Lernergebnisse.

## Mit der Lernabsicht beginnen

Pococks Ausgangspunkt ist der Unterschied zwischen einer einzelnen Erklärung und einer fortgesetzten Lernbeziehung. Für eine Einmalfrage kann ein zustandsloser Skill ausreichen. Über mehrere Sitzungen braucht der Agent dagegen verlässliche Informationen darüber, was die Person erreichen will, was sie bereits kann und wo sie Schwierigkeiten meldet. Der gespeicherte Zustand ersetzt dabei die Annahme, dass ein neuer Chat den bisherigen Lernweg noch kennt.

Die Mission begrenzt das Lernziel. Beim Rubik-Beispiel geht es darum, einen verdrehten Würfel einmal ohne Hilfe lösen zu können. Geschwindigkeit und umfassende Theorie gehören zunächst nicht dazu. Diese Eingrenzung gibt der Auswahl von Erklärungen und Übungen einen Maßstab: Relevant ist, was für das konkrete Ziel und den gegenwärtigen Lernstand gebraucht wird.

## Den Lernzustand in getrennten Artefakten halten

Der beschriebene Arbeitsraum verteilt unterschiedliche Aufgaben auf wiederauffindbare Dateien und Verzeichnisse:

- `MISSION.md` hält Lernziel und Motivation fest.
- `RESOURCES.md` sammelt vertrauenswürdige Ressourcen, vorzugsweise Primärquellen, als Grundlage der Lektionen.
- `learning-records` dokumentiert Rückmeldungen zum erreichten Stand und zu offenen Schwierigkeiten.
- `lessons` enthält gezielte HTML-Lektionen, die während des Lernens entstehen.
- `reference` bündelt Nachschlagehilfen wie Glossar und kompakte Ablaufkarten.
- `NOTES.md` bewahrt Präferenzen und Hinweise für spätere Sitzungen.

Die Trennung ist fachlich sinnvoll: Eine subjektive Rückmeldung zum Lernstand hat eine andere Funktion als eine fachliche Quelle oder ein Glossareintrag. Ein dokumentierter Erfolg ist zunächst eine gemeldete Leistung; die Datei allein prüft nicht, ob das Können später ohne Hilfen abrufbar ist. Ebenso muss die Auswahl vertrauenswürdiger Ressourcen tatsächlich gelingen, damit die darauf aufgebauten Lektionen belastbar werden.

## Rückmeldung bestimmt den nächsten Lernschritt

Der Lernende berichtet, was funktioniert und wo er hängen bleibt. Daraufhin soll der Agent den gespeicherten Stand lesen und die nächste Aufgabe eingrenzen. Im Beispiel ist der Ablauf eines Algorithmus verstanden, aber noch nicht sicher eingeübt. Daraus entsteht eine zusätzliche Lektion zum gezielten Üben dieser Bewegung statt einer Wiederholung des gesamten Stoffes.

Pocock verbindet dies mit der Zone der nächsten Entwicklung: Aufgaben sollen herausfordern, ohne zu überfordern. HTML dient als Darstellungsraum für Diagramme, kurze Erklärungen, Quizfragen und interaktive Übungshilfen. Seine Stärke liegt hier in den möglichen Rückmeldungen und Handlungen, nicht schon im Dateiformat. Eine attraktiv gestaltete Lektion belegt noch keine angemessene Schwierigkeit oder nachhaltiges Behalten.

Glossar und Ablaufkarten ergänzen diesen Kreislauf. Bereits eingeführte Begriffe müssen nicht in jeder Lektion erneut erklärt werden; eine kompakte Referenz kann bei praktischen Schritten helfen. Ob solche Hilfen das selbstständige Können fördern oder nur die Aufgabe mit Unterstützung lösbar machen, bleibt eine Frage der konkreten Lernaufgabe.

## Wissen, Fertigkeit und Praxisgemeinschaft unterscheiden

Der Skill soll Wissen aus geeigneten Quellen vermitteln und Fertigkeiten durch passende Aufgaben aufbauen. Pocock unterscheidet davon Erfahrungswissen, das durch den Austausch mit Lernenden und Praktikern entsteht. Bei Fragen, die solche Erfahrung verlangen, soll der Agent auch auf passende Gemeinschaften verweisen. Das begrenzt seinen Anspruch als alleinige Lehrinstanz und eröffnet Rückmeldungen außerhalb des eigenen Lernarbeitsraums.

Als Einsatzfeld nennt Pocock das Onboarding in eine Codebasis: Eine Person benötigt möglicherweise Domänenwissen, eine andere zunächst Grundlagen des verwendeten Stacks. Das Modell legt nahe, Lernziele und Vorkenntnisse vor der Lektion zu klären. Seine Erwartung schnellerer Produktivität ist jedoch eine Anwendungsidee; im Video wird kein Vergleich verschiedener Onboarding-Verfahren ausgewertet.

## Einordnung

Die am 28.10.2026 statisch gesichtete Fassung von `skills/productivity/teach/SKILL.md` im lokalen Referenzrepo `mattpocock/skills` auf Commit `5beb35b` bestätigt die genannten Zustandsartefakte und den Rückmeldungsablauf. Sie nennt zusätzlich wiederverwendete Assets und ein geteiltes Stylesheet; Video und Checkout bilden unterschiedliche Stände ab. Diese Stichprobe bestätigt dokumentierte Anweisungen, keine ausgeführte Unterrichtssitzung und keine Lernwirkung. Pococks berichteter Rubik-Erfolg und seine Begeisterung sind persönliche Erfahrung, keine kontrollierte Studie. Für eine Übernahme bleibt entscheidend, wie Lernstand, Quellenqualität und selbstständige Anwendung überprüft werden.

## Kernaussagen

- [[Claude-als-Lernwerkzeug]] erhält eine konkrete Struktur für fortgesetztes Lernen: Mission, Quellen, Lernjournal und Referenzmaterial tragen den Kontext über Sitzungen hinweg.
- Zu [[Claude-als-Lernwerkzeug]] gehört die Trennung zwischen Erklärungen, tatsächlichem Üben und Rückmeldungen aus einer Praxisgemeinschaft; keine dieser Ebenen ersetzt die anderen.

## Verbindungen

- [[Claude-als-Lernwerkzeug]]: Der bereits vorhandene Lernmodus wird um gespeicherten Lernzustand und eine daraus abgeleitete nächste Aufgabe konkretisiert.
- [[2026-10-09-openai-codebase-onboarding]]: Codebase-Onboarding ist ein Anschlussfeld für die Frage, wie Vorkenntnisse und Domänenwissen den individuellen Lernpfad bestimmen sollen.
