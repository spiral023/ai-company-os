---
titel: "Grüne Tests, der Bug bleibt: Prüft dein Test den echten Code?"
datum: 2026-10-09
kategorie: arbeitsweisen
zusammenfassung: "Erkenne Tests, die nur Mocks prüfen: Ein kleines Python-Beispiel zeigt einen übersehenen Grenzfall, einen aus der Anforderung abgeleiteten Verhaltenstest und eine gezielte Mutation zur Kontrolle."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-02-04-tweag-tdd-agentic-coding
  - 2026-02-14-matt-pocock-skill-tdd-claude-code
---

## Kurz gesagt

- Formuliere das erwartete Verhalten aus der Anforderung, bevor du den Test an der Implementierung ausrichtest.
- Verfolge im Test den Aufruf bis zum echten Code. Prüfe, welche Teile durch Mocks ersetzt werden.
- Kontrolliere einen wichtigen Grenzfall mit einer gezielten falschen Änderung und beobachte, ob der Test reagiert.
- Investiere diese Prüfung in relevante Regeln und Fehlerrisiken. Kleine, reversible Änderungen brauchen keine zusätzliche Testsammlung aus Gewohnheit.

## Warum ein grüner Test den Fehler übersehen kann

Der Agent hat eine Funktion gebaut, Tests ergänzt und alles läuft durch. Trotzdem verhält sich die App am entscheidenden Grenzwert falsch. Beim Blick in den Test siehst du: Die betroffene Funktion wird durch eine vorbereitete Antwort ersetzt. Der Test erreicht ihre Logik gar nicht.

Ein Mock ist ein Testobjekt, das eine Abhängigkeit ersetzt und beispielsweise eine festgelegte Antwort liefert. Das kann sinnvoll sein, wenn du einen externen Dienst isolieren willst. Es hilft dir jedoch wenig beim Prüfen genau der Logik, die dadurch aus dem Ablauf verschwindet.

Matt Pocock beschreibt dieses Problem bei generierten Tests ausdrücklich: Manche Prüfungen bestätigen Aufrufe interner Ersatzobjekte, während tatsächliche Codepfade unberührt bleiben. Sein Vorschlag setzt auf kleine Schritte und beobachtbares Verhalten über eine öffentliche Schnittstelle.{q:2}

Die entscheidende Frage beim Review lautet deshalb: Welche falsche Implementierung könnte diesen Test bestehen? Wenn die Antwort die gerade untersuchte Fehlfunktion einschließt, fehlt dir ein passendes Prüfkriterium.

## Leite den Grenzfall aus der Anforderung ab

Unser synthetisches Beispiel ist ein Formular. Seine vereinfachte Regel lautet: Sobald mindestens die erforderliche Anzahl an Antworten vorhanden ist, trägt der Button die Beschriftung „Senden“. Andernfalls zeigt er „Weiter“. Die Eingaben sind hier nicht negative ganze Zahlen; deren Validierung liegt außerhalb des Beispiels.

Aus „mindestens“ ergibt sich die Entscheidung bei Gleichheit. Diese Erwartung stammt aus der formulierten Anforderung. Du musst die Funktion dafür noch nicht gelesen haben. Tweags TDD-Ablauf empfiehlt ebenfalls, Geschäftsregeln in kleine prüfbare Verhaltensschritte zu zerlegen.{q:1}

Die folgende Funktion enthält absichtlich einen Fehler:

```python
def can_submit(answered, required):
    return answered > required  # absichtlicher Grenzfehler


def button_label(answered, required, ready):
    return "Senden" if ready(answered, required) else "Weiter"
```

`ready` ist eine übergebene Funktion. Diese kleine Schnittstelle erlaubt dem Test, entweder die echte Regel oder eine Ersatzfunktion einzusetzen. Im Produkt könnte eine vergleichbare Entscheidung in einem Service oder einer Komponente liegen.

## Der Mocktest erreicht die falsche Regel nicht

Dieser Test ersetzt die Entscheidung durch eine festgelegte positive Antwort:

```python
from unittest.mock import Mock

fake = Mock(return_value=True)
assert button_label(3, 3, fake) == "Senden"
fake.assert_called_once_with(3, 3)
```

Er bestätigt, dass der Button bei positiver Antwort „Senden“ anzeigt und die Ersatzfunktion mit den angegebenen Werten aufruft. Die Funktion `can_submit` wird dabei nicht ausgeführt. Ihre falsche Grenze bleibt unangetastet.

Für die Darstellung des Buttons kann diese isolierte Prüfung passend sein. Für die Anforderung „mindestens genügend Antworten“ fehlt der reale Entscheidungspfad. Prüfe deshalb pro Test, welche Verantwortung du ihm tatsächlich zuschreibst.

Ein rotes Ergebnis nach dem Umbenennen einer internen Methode sagt ebenfalls wenig über die fachliche Regel aus. Überlege beim Testreview, ob sich die Prüfung an Namen und Aufrufstruktur bindet oder an einem Ergebnis, das deine Nutzer benötigen. Pococks Beispiele unterscheiden diese beiden Ebenen.{q:2}

## Der Verhaltenstest verwendet die echte Funktion

Jetzt speisen wir die echte Entscheidung in denselben Aufruf ein. Die erwarteten Beschriftungen haben wir bereits aus der Anforderung abgeleitet:

```python
assert button_label(2, 3, can_submit) == "Weiter"
assert button_label(3, 3, can_submit) == "Senden"
assert button_label(4, 3, can_submit) == "Senden"
```

Diese synthetischen Werte liegen unter, auf und über der Schwelle. Beim lokalen Lauf bestand der Mocktest mit der fehlerhaften Funktion. Die Verhaltenstests bestanden unterhalb und oberhalb der Grenze; bei Gleichheit schlug die Prüfung fehl. Nach der Korrektur auf `answered >= required` bestanden die gezeigten Verhaltensfälle.

Das Ergebnis betrifft ausschließlich dieses kleine Beispiel. Es zeigt, welcher Test den eingebauten Fehler erkennt. Daraus folgt keine Aussage über die Testqualität einer kompletten App.

Beim Arbeiten mit einem Agenten kannst du denselben Ablauf gezielt anfordern: Anforderung nennen, erwartetes Ergebnis begründen lassen, den relevanten Test ausführen und erst danach die Implementierung korrigieren. Ein fehlgeschlagener Test muss dabei am untersuchten Verhalten scheitern. Ein Importfehler oder ein nicht erreichbarer Testserver prüft diese Regel noch nicht.

## Eine gezielte Mutation kontrolliert das Prüfkriterium

Eine Mutation ist eine absichtliche kleine Änderung am Code. Hier lässt sich der korrigierte Vergleich probeweise wieder von `>=` auf `>` ändern. Wenn der Grenztest danach besteht, solltest du untersuchen, weshalb er die Änderung nicht bemerkt.

Auch diese gezielte Mutation wurde im synthetischen Beispiel lokal ausgeführt. Der Test bei Gleichheit schlug erneut fehl. Die falsche Änderung blieb auf die lokale Versuchsfunktion beschränkt.

Bei einer echten Änderung wählst du einen isolierten Arbeitsstand und stellst den ursprünglichen Code anschließend wieder her. Kontrolliere danach den Diff und führe die betroffenen Prüfungen erneut aus. Ein Diff zeigt die Änderungen zwischen zwei Arbeitsständen.

Der Wechsel aus fehlschlagendem Test, minimaler Korrektur und anschließendem Aufräumen wird oft RED–GREEN–REFACTOR genannt. Tweag und Pocock beschreiben diesen kleinteiligen Ablauf. Er strukturiert die Arbeit; gegen angepasste Tests, umgangene Ausführung oder eine falsch verstandene Anforderung liefert er keine technische Garantie.{q:1}{q:2}

## Wähle die Prüfung nach dem Risiko der Änderung

Ein Verhaltenstest trägt nur so weit, wie seine Eingaben und Erwartungen reichen. Datenbankeffekte, Browserbedienung und externe Antworten können weitere Prüfungen erfordern. Umgekehrt brauchst du für eine kleine Textkorrektur nicht automatisch neue Tests.

Mocks bleiben ein brauchbares Werkzeug für gezielte Isolation. Halte fest, welche Abhängigkeit sie ersetzen und welches Verhalten damit außerhalb der Prüfung liegt. Für weitergehende Abläufe kannst du den [Pre-Launch-Check deiner App](post:pre-launch-app-angreifen) ergänzen.

Nimm als nächsten Schritt einen wichtigen grünen Test und zeichne seinen echten Aufrufweg nach. Formuliere eine plausible falsche Implementierung. Prüfe dann gezielt, ob das bestehende Kriterium diese Abweichung erkennen würde. Ergänze einen Test dort, wo dir tatsächlich ein relevantes Verhalten fehlt.
