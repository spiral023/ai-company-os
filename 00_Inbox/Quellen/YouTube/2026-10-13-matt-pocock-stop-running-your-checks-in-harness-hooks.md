---
url: https://www.youtube.com/watch?v=zgy8_ApYNDk
titel: "STOP running your checks in harness hooks"
autor: "Matt Pocock"
datum: 2026-10-13
erfasst: 2026-10-22
typ: youtube
quelle: youtube
status: verarbeitet
verarbeitet_am: 2026-10-22
source_notiz: 80_Knowledge/Sources/2026-10-13-matt-pocock-stop-running-your-checks-in-harness-hooks.md
video_id: "zgy8_ApYNDk"
transkript_quelle: "Chrome-Export der YouTube-Untertitel"
transkript_sprache: "de"
transkript_generiert: "ja"
transkript_segmente: "49"
videobeschreibung_erfassung: "Sichtbarer Beschreibungstext, Abstände normalisiert; einzelne Links von YouTube verkürzt dargestellt"
metadaten_quelle: "YouTube-Originalseite in Chrome; Datum aus aufgeklappter Beschreibung"
sprache_abweichung: true
originalsprache: "en"
transkript_spur_hinweis: "Deutsche automatisch erzeugte Spur eines englischsprachigen Videos mit automatischer Synchronisation; Übersetzungs- und ASR-Fehler möglich. Keine wörtlichen Originalzitate daraus ableiten."
---

# STOP running your checks in harness hooks

> Nach blockiertem Standardabruf über die YouTube-Originalseite in Chrome erfasst; automatisch erzeugte Untertitel. Quelle: [https://www.youtube.com/watch?v=zgy8_ApYNDk](https://www.youtube.com/watch?v=zgy8_ApYNDk)

## Videobeschreibung

Learn the right way to set up automated checks for AI coding agents. This video covers the key difference between running checks on every file edit versus using pre-commit hooks, and how to optimize your CI/CD pipeline for agent workflows.

Keep up to date with my skills here:
https://aihero.dev/s/qfwVgl

Follow Matt on Twitter
/mattpocockuk

Join the Discord:
https://aihero.dev/s/RXm2vT

## Transkript

Viele Leute empfehlen: „Okay, du hast diese Hooks für dein Agent-Harness. Du solltest automatisierte Prüfungen in diesen Hooks laufen lassen, um sicherzugehen, dass der Agent tut, was du willst.“ Generell halte ich automatisierte Prüfungen für den Agenten für wirklich sehr nützlich, weil er so versteht, was er falsch macht, und er bekommt Feedback genau im richtigen Moment. Viele empfehlen, dies bei jeder einzelnen Dateiänderung auszuführen, aber das kann extrem störend sein, da man in einer Sitzung 100 Dateiänderungen haben kann–etwa bei einem großen Refactoring–und diese automatisierten Prüfungen verlangsamen alles, wenn man jede einzelne Datei beim Speichern prüft.

Es ist auch für den Agenten unglaublich verwirrend. Der Agent erhält bei jeder Datei eine Menge Tokens und weiß oft selbst, dass er die Datei in einen fehlerhaften Zustand versetzt. Man sagt dem Agenten also nur etwas, das er bereits weiß. Wenn man diese Prüfungen stattdessen in einen Pre-Commit-Hook legt, erzielt man ein besseres Ergebnis. Du ermutigst deinen Agenten also zu einem Commit, und sobald er committet, wird die Information an ihn zurückgegeben: „ Oh, das ist eigentlich falsch.“ Das bedeutet, du bündelst all diese Informationen für den richtigen Moment , nämlich wenn der Agent sie tatsächlich in die Historie schreibt.

Du solltest dort nicht unbedingt alle Prüfungen laufen lassen, denn diese Pre-Commit-Checks sollen nicht etwa zwei Minuten dauern. Idealerweise sollten sie unter drei Sekunden bleiben . Alles, was sehr umfangreich ist und mehr Zeit benötigt, kannst du an die CI delegieren, die vor dem Mergen des PR läuft. Das ist also die Art und Weise, wie ich die Einrichtung automatisierter Prüfungen für deinen Agenten empfehle.

## Erfassungsbeleg

Unveränderter Browser-Export mit Zeitmarken: [transkript-browser.txt](medien/2026-10-13-matt-pocock-stop-running-your-checks-in-harness-hooks/transkript-browser.txt).
