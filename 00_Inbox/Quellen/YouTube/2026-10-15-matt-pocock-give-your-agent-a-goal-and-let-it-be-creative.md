---
url: https://www.youtube.com/watch?v=fn3iRGgRuWU
titel: "Give your agent a goal, and let it be creative"
autor: "Matt Pocock"
datum: 2026-10-15
erfasst: 2026-10-28
typ: youtube
quelle: youtube
status: verarbeitet
verarbeitet_am: 2026-10-28
source_notiz: 80_Knowledge/Sources/2026-10-15-matt-pocock-give-your-agent-a-goal-and-let-it-be-creative.md
video_id: "fn3iRGgRuWU"
transkript_sprache: "de"
transkript_generiert: "ja"
transkript_segmente: "35"
transkript_zusatzsprache: "en"
transkript_zusatz_generiert: "ja"
transkript_zusatz_segmente: "33"
transkript_zusatz_datei: "medien/2026-10-15-matt-pocock-give-your-agent-a-goal-and-let-it-be-creative/transkript-youtube-en.json"
---

# Give your agent a goal, and let it be creative

> Automatisch per `python ai.py ingest` erfasst. Quelle: [https://www.youtube.com/watch?v=fn3iRGgRuWU](https://www.youtube.com/watch?v=fn3iRGgRuWU)

## Videobeschreibung

Learn how to use verification and continuous improvement to make your AI agents better over time. In this video, I walk through building a custom video editor and using a scorecard system to track performance metrics, then having agents autonomously work to improve them day after day.

Keep up to date with my skills here:

https://aihero.dev/s/l2LvvX

Follow Matt on Twitter

https://twitter.com/mattpocockuk

Join the Discord:

https://aihero.dev/s/9uhQZL

## Transkript

Die Arbeit von Agenten zu überprüfen ist unglaublich wichtig, und ich lege bei meinen Agenten mittlerweile mehr Wert darauf. Zum Beispiel verwende ich gerade einen benutzerdefinierten Video-Editor für diese Aufnahme und wollte meine Abhängigkeit von OBS beenden. Also musste ich einen Ersatz für OBS bauen. Natürlich musste er nicht alle Funktionen von OBS haben, nur die, die ich brauchte, aber die Leistung sollte exakt dieselbe sein. Deshalb habe ich den Agenten eine Scorecard für den Rekorder erstellen lassen, die OBS anhand verschiedener Metriken bewertet und uns misst, wie gut wir im Vergleich dazu abschneiden.

Dieses Skript läuft etwa 20 Minuten und liefert mir alle möglichen Metriken. Mein Plan ist, dass der Agent das Ganze einmal täglich neu ausführt , um die Ergebnisse immer weiter zu verbessern und jedes Mal nach Optimierungen zu suchen. Da er nun eine klare Reihe von Metriken hat, die er über die Zeit verfolgen muss, kann er immer kreativere Wege finden, um diese Werte zu verbessern. Dies ist eine massiv unterschätzte Art, Agenten einzusetzen. Man gibt ihnen einfach ein Ziel vor, und mit der Zeit kommen sie diesem Ziel immer näher. Das ist großartig für leistungskritische Software, von der ehrlich gesagt die meisten Programme betroffen sind.

## Zusätzliches Transkript (Englisch)

> Zusätzlich direkt von YouTube erfasste englische Untertitelspur; automatisch erzeugt. Die oben archivierte deutsche Spur bleibt unverändert. [Unveränderter Segmentexport mit Zeitmarken](medien/2026-10-15-matt-pocock-give-your-agent-a-goal-and-let-it-be-creative/transkript-youtube-en.json).

Verifying agent's work is unbelievably important, and I've started putting more emphasis on this with my agents. For instance, I'm using a custom video editor to record this right now, and I wanted to drop my dependency on OBS. And so, I needed to build a replacement OBS. Now, of course, it didn't need to have all the features of OBS, it just had the features that I needed, but I wanted it to have exactly the same performance. And so, what I did, I got the agent to build a recorder scorecard, which would score OBS on a bunch of metrics and score us based on how well it performs against it. This script takes about 20 minutes to run, and it gives me all sorts of metrics. And the way I'm going to get this working is the agent is going to, once a day, try to rerun this and get the results better and better, looking for improvements every single time. Now, it's got a very clear set of metrics that it needs to track over time, it can just look for more and more creative ways to try to make those metrics better. This is a massively underused way of using agents. You just give it a goal, and over time it will get closer to that goal. This is a really amazing for performance-sensitive software, of which, honestly, most software is
