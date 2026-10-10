---
titel: "KI-Code verstehen lernen: Erst vorhersagen, dann ändern und prüfen"
datum: 2026-10-09
kategorie: arbeitsweisen
zusammenfassung: "Verstehe KI-generierten Code mit einem kleinen Lernablauf: Erklärung lesen, Ausgabe selbst vorhersagen, gezielt ändern und Verständnisfragen beantworten. Die abschließende Codekontrolle bleibt eine eigene Aufgabe."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-01-31-bcherny-claude-code-team-tips
  - 2026-07-03-trq212-2073100352921215386
---

## Kurz gesagt

- Lass dir einen kleinen Codepfad anhand seiner Eingaben, Entscheidungen und Ausgabe erklären.
- Sage das Verhalten selbst voraus, bevor du die Ausgabe ausführst oder die Musterantwort ansiehst.
- Ändere eine klar abgegrenzte Anforderung und prüfe, ob du die notwendige Codeänderung begründen kannst.
- Nutze Verständnisfragen zum Aufdecken eigener Lücken. Kontrolliere anschließend den tatsächlichen Code und relevante Tests gesondert.

## Eine verständliche Erklärung ist erst der Einstieg

Der Agent hat eine Funktion gebaut und erklärt sie flüssig. Beim Lesen klingt alles nachvollziehbar. Kurz darauf willst du einen Sonderfall ändern und weißt nicht, welche Bedingung dafür zuständig ist.

Du brauchst eine Gelegenheit, das Verhalten selbst herzuleiten. Dafür eignet sich ein kleiner Ausschnitt, bei dem du Eingabe, Entscheidung und Ergebnis überblicken kannst. Ein kompletter Service mit Datenbankzugriff und Hintergrundjobs ist für den Einstieg meist zu viel auf einmal.

Boris Cherny berichtet von Teampraktiken, die Claude zum Erklären von Code, für Diagramme und für wiederkehrende Verständnisfragen einsetzen. Thariq beschreibt nach längeren Änderungen einen erklärenden Bericht mit Quiz. Beide Quellen schildern Arbeitsweisen; sie liefern keine kontrollierte Messung eines Lernerfolgs.{q:1}{q:2}

Der folgende Ablauf ist ein Vorschlag für deine Arbeit. Er verbindet Erklärung, Vorhersage, kleine Änderung und anschließende Kontrolle. Wie hilfreich er für dich ist, musst du an deinen Aufgaben beurteilen.

## Lass dir den Code an einer konkreten Eingabe erklären

Unser synthetisches Beispiel zeigt eine Aufgabenliste. Die Funktion soll die Titel offener Aufgaben zurückgeben. Die Eingabe besteht aus Einträgen mit einem Titel und einem booleschen Feld `done`; ein boolescher Wert kann wahr oder falsch sein.

```python
def visible_tasks(tasks):
    return [
        task["title"]
        for task in tasks
        if not task["done"]
    ]


tasks = [
    {"title": "Entwurf", "done": False},
    {"title": "Review", "done": True},
]
```

Bitte den Agenten zunächst um eine Erklärung dieses konkreten Ablaufs: Welcher Eintrag wird betrachtet? Welche Bedingung wird ausgewertet? Welcher Wert gelangt in die Rückgabe? Ein passender Auftrag wäre:

> Erkläre den Ablauf mit dieser Eingabe. Zeige bei jedem Eintrag die ausgewertete Bedingung. Benenne die Annahmen über die Daten und ändere den Code noch nicht.

Die Schreibweise in eckigen Klammern ist eine List Comprehension: Sie baut eine neue Liste aus ausgewählten Werten einer vorhandenen Sammlung. Die Erklärung sollte dieses Sprachmittel mit dem tatsächlichen Verhalten verbinden.

Prüfe außerdem die Grenzen der Erklärung. Die Funktion setzt passende Schlüssel voraus. Sie entscheidet nicht selbst, ob die gelieferten Daten vollständig oder fachlich gültig sind. Wenn der Agent zusätzliche Validierung beschreibt, suche die entsprechende Stelle im Code.

## Sage die Ausgabe voraus, bevor du sie ansiehst

Schließe die Erklärung und formuliere die erwartete Ausgabe selbst. Begründe, warum der offene Eintrag aufgenommen wird und der erledigte Eintrag entfällt. Erst danach führst du das Beispiel aus.

Für die gezeigte Eingabe wurde die Funktion lokal ausgeführt. Die Ausgabe war:

```text
['Entwurf']
```

Vergleiche deine Vorhersage mit dieser Ausgabe. Wenn sie abweicht, gehe zur entscheidenden Bedingung zurück. Vielleicht hast du `not` überlesen oder Titel mit vollständigen Aufgabenobjekten verwechselt.

Nimm danach eine leere Liste und eine Liste aus ausschließlich erledigten Aufgaben. Formuliere wieder zuerst deine Erwartung. Solche Varianten verändern die Eingabe bei gleichbleibendem Code und zeigen dir, ob du die Auswahlregel erklären kannst.

Eine richtige Vorhersage für dieses Beispiel reicht noch nicht, um einen großen Codepfad zu verstehen. Sie gibt dir einen begrenzten Prüfpunkt für das gerade behandelte Sprachmittel und Verhalten.

## Ändere eine kleine Anforderung

Die neue synthetische Anforderung lautet: Optional sollen auch erledigte Aufgaben sichtbar sein. Ohne diese Option soll das bisherige Verhalten erhalten bleiben.

Überlege zuerst selbst, wo die Entscheidung stattfinden muss. Der Aufbau der Ergebnisliste bleibt gleich; die Auswahlbedingung bekommt eine zusätzliche Möglichkeit. Schreibe deine Idee auf, bevor du den Agenten um eine Implementierung bittest.

Eine mögliche Lösung sieht so aus:

```python
def visible_tasks(tasks, include_done=False):
    return [
        task["title"]
        for task in tasks
        if include_done or not task["done"]
    ]
```

`include_done` ist ein optionaler Parameter mit dem Standardwert `False`. Ist er wahr, erfüllt jeder Eintrag die Auswahlbedingung. Andernfalls entscheidet weiterhin sein Erledigt-Status.

Auch diese Variante wurde mit der synthetischen Eingabe lokal geprüft. Der Standardaufruf gab weiterhin `['Entwurf']` zurück. Mit `include_done=True` erschien `['Entwurf', 'Review']`. Geprüft wurden außerdem die leere Liste und der unveränderte Erledigt-Status der ursprünglichen Eingabe.

Betrachte den Unterschied zwischen den Varianten. Welche Zeile trägt die neue Anforderung? Welche Eigenschaft ist bewusst gleich geblieben? Wenn du die Änderung nur als fertige Antwort übernehmen kannst, lohnt sich eine weitere Erklärung dieses kleinen Abschnitts.

## Nutze Verständnisfragen mit Bezug zum echten Code

Lass den Agenten Fragen stellen, deren Antworten eine konkrete Entscheidung im Code benötigen. Thariqs vorgeschlagenes Quiz soll das Verständnis einer Änderung einschließlich vorhandener Codepfade prüfen.{q:2}

Für unser Beispiel wären diese Fragen passend:

- Warum bleibt das bisherige Verhalten beim Standardaufruf erhalten?
- Was würde sich ändern, wenn `or` durch `and` ersetzt würde?
- Warum enthält die Ausgabe Titel statt vollständiger Aufgabenobjekte?
- Welche Annahme macht die Funktion über einen fehlenden `done`-Schlüssel?
- Wird die Eingabeliste verändert, und woran erkennst du das?

Beantworte die Fragen ohne direkt sichtbare Musterantwort. Fordere anschließend die konkrete Codezeile und ein Gegenbeispiel zu einer falschen Antwort an. Eine allgemeine Bestätigung wie „gut erklärt“ hilft wenig beim Erkennen der verbleibenden Lücke.

Der Agent kann Fragen und Antworten ebenfalls falsch formulieren. Gleiche deshalb strittige Aussagen mit dem Code und bei Sprachdetails mit der passenden Dokumentation ab. Eine später wiederholte Frage kannst du nutzen, um festzustellen, welche Teile du erneut herleiten musst.

## Kontrolliere die Implementierung anschließend gesondert

Ein Code-Quiz prüft Antworten auf ausgewählte Fragen. Es kann eine gemeinsame Fehlannahme von dir und dem Agenten übersehen. Selbst richtige Antworten zeigen nicht, dass die gesamte Implementierung korrekt ist.

Lies deshalb den tatsächlichen Diff und verfolge den betroffenen Aufrufweg. Prüfe passende Testfälle aus der Anforderung. Bei einem UI-Ablauf gehört gegebenenfalls die Bedienung im Browser dazu. Welche Prüfungen nötig sind, hängt vom Umfang und Risiko der Änderung ab.

Die lokalen Läufe hier betreffen ausschließlich die gezeigten synthetischen Funktionen. Sie prüfen weder eine echte App noch Datenbankzugriffe, Nebenwirkungen anderer Komponenten oder die Bedienung einer Aufgabenoberfläche.

Plane den Lernschritt klein genug, dass du ihn selbst nachvollziehen kannst. Erklärung, Änderung und Rückfragen kosten zusätzliche Zeit. Für eine unbekannte Bedingung kann dieser Aufwand passend sein; für eine bereits verstandene Textkorrektur brauchst du keinen eigenen Lernablauf.

Nimm beim nächsten KI-generierten Code einen kleinen Ausschnitt. Lass ihn erklären, sage seine Ausgabe voraus und ändere eine Anforderung. Beantworte danach Verständnisfragen und kontrolliere die Umsetzung. Halte fest, welche Teile du selbst erklären kannst und wo Fragen offenbleiben.
