---
titel: "DRY: Welche Fachregel ist wirklich doppelt?"
datum: 2026-10-29
kategorie: arbeitsweisen
zusammenfassung: "DRY richtet sich gegen mehrfach gepflegtes Wissen. Prüfe gemeinsame Änderungsgründe, bevor ein Coding Agent ähnliche Codezeilen zu einer allgemeinen Funktion zusammenzieht."
status: freigegeben
geprueft_am: 2026-10-29
freigabe: automatisch
quellen:
  - 2019-09-13-pdf-the-pragmatic-programmer-20th-anniversary-edition
---

## Kurz gesagt

- Prüfe vor einer Zusammenführung, ob die betroffenen Stellen dieselbe fachliche Entscheidung ausdrücken.
- Trenne Regeln, die nur heute gleich aussehen und unabhängig voneinander geändert werden dürfen.
- Wähle für gemeinsam gepflegtes Wissen einen maßgeblichen Ursprung und prüfe seine abgeleiteten Darstellungen.

## Ähnliche Zeilen können verschiedene Regeln meinen

Ein Coding Agent findet mehrfach denselben Vergleich und schlägt einen gemeinsamen Helfer vor. Der Diff wird kleiner, die Funktion erhält einen allgemeinen Namen, alle Tests bleiben grün. Ob damit eine gute Abstraktion entstanden ist, hängt jedoch von der Bedeutung der ursprünglichen Stellen ab.

David Thomas und Andrew Hunt richten DRY in [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) auf Wissen und Absicht. Ihre Kritik betrifft dieselbe Entscheidung, die mehrfach dargestellt und unabhängig gepflegt wird. Gleicher Code ist dafür ein Hinweis, aber keine ausreichende Begründung. Der entsprechende Abschnitt steht auf den PDF-Seiten 79 bis 91.{q:1}

Für Agentenarbeit lässt sich daraus eine einfache Vorbereitung ableiten: Vor dem Extrahieren erklären lassen, welche fachliche Aussage zusammengeführt werden soll. Eine Antwort wie „Diese Zeilen kommen mehrfach vor“ reicht für die Entscheidung noch nicht.

## Suche den gemeinsamen Änderungsgrund

Stell dir ein Ticketsystem vor. Ein Formular prüft, ob ein Betreff lang genug ist. Ein anderer Ablauf entscheidet, ob eine interne Beschreibung ausführlich genug für eine Übergabe ist. Beide Prüfungen können gegenwärtig dieselbe Mindestlänge verwenden. Trotzdem beantworten sie unterschiedliche Fragen.

Die Produktverantwortlichen könnten die Anforderung an den Betreff ändern und die Übergaberegel unverändert lassen. Dann war die Übereinstimmung zufällig. Ein allgemeiner Helfer mit einem gemeinsamen Grenzwert würde beide Entscheidungen miteinander verbinden.

Anders liegt der Fall, wenn Webformular, Import und API dieselbe Betreffregel durchsetzen sollen. Ändert sich die zulässige Länge, müssen alle Zugänge dieselbe fachliche Entscheidung anwenden. Hier ist eine unabhängige Pflege der Regel ein Problem. Dieser Vergleich über mögliche Änderungen entspricht dem Wissensbegriff der Autoren.{q:1}

Frage beim Review deshalb, wer eine Änderung beschließt, welche Nutzerhandlung betroffen ist und welche weiteren Stellen gleichzeitig angepasst werden müssen. Je konkreter die Antworten, desto leichter lässt sich zufällige Ähnlichkeit von gemeinsamer Verantwortung unterscheiden.

## Dieselbe Regel kann unterschiedlich aussehen

Wissensduplikation muss keine identischen Codezeilen erzeugen. Eine Grenze kann als Bedingung im Backend, als Eingabeeinschränkung im Formular und als Satz in der Dokumentation auftauchen. Eine neue fachliche Entscheidung erfordert dann mehrere abgestimmte Anpassungen.

Thomas und Hunt behandeln auch solche Darstellungen als möglichen DRY-Konflikt. Sie diskutieren gemeinsame Beschreibungen und erzeugte Gegenstücke, beispielsweise bei Schnittstellen. Der Zweck ist, dass eine Änderung nicht an vielen unabhängigen Stellen erneut interpretiert werden muss.{q:1}

Im gedachten Ticketsystem könntest du zunächst klären, welche Darstellung maßgeblich ist. Danach untersuchst du, was daraus ableitbar ist und wo zusätzlicher fachlicher Text benötigt wird. Eine Frontendgrenze allein ersetzt beispielsweise keine tatsächlich ausgeführte Prüfung am vorgesehenen Eingang.

Eine [gemeinsame Schemabeschreibung mit angebundenen Clients](post:api-vertraege-schema-coding-agents) kann strukturelle Abweichungen reduzieren. Ob ein Ticket fachlich zulässig ist, verlangt weiterhin passende Regeln und Verhaltenstests. Gemeinsame Typen und gemeinsame Bedeutung sind getrennt zu prüfen.

## Berechnete Werte brauchen einen eindeutigen Zusammenhang

Auch gespeicherte Ableitungen können Wissen doppelt halten. Wird derselbe Zustand als Einzelwerte und zusätzlich als Gesamtergebnis geführt, muss klar sein, wie beide zusammenpassen. Die Autoren nennen Berechnung oder gekapselte Ableitung einschließlich Aktualisierung als mögliche Wege.{q:1}

Ein eigener Beispielsfall wäre die Anzahl offener Tickets neben der eigentlichen Ticketliste. Du kannst sie beim Abruf berechnen. Falls ein gespeicherter Wert nötig ist, muss dessen Aktualisierung zu den erlaubten Änderungen passen. Ihn unabhängig an verschiedenen Stellen hoch- und herunterzuzählen schafft zusätzliche Pflichten für die Aufrufer.

DRY verlangt daraus keine pauschale Abschaffung jedes Cache. Ein Cache hält bewusst eine weitere Darstellung vor, um einen anderen Aufwand zu verändern. Seine Gültigkeit und Aktualisierung gehören aber zum Entwurf. Ob sich die zusätzliche Komplexität lohnt, muss am konkreten Ablauf entschieden werden.

## Eine gemeinsame Funktion kann neue Kopplung erzeugen

Wenn ein Helfer verschiedene Fachregeln bedienen soll, wachsen oft Parameter und Schalter. Aufrufer müssen wissen, welche Kombination zu ihrem Fall gehört. Die ursprünglich sichtbaren Unterschiede verschwinden dann hinter einer allgemeinen Signatur, bleiben für die richtige Benutzung aber erforderlich.

Die Autoren verbinden DRY mit Orthogonalität: unabhängig veränderliche Entscheidungen sollen möglichst unabhängig bleiben. Eine Zusammenführung, die ihre Änderungen erst miteinander verkoppelt, verbessert diesen Entwurf nicht automatisch.{q:1}

Prüfe den Vorschlag des Agenten an einer konkreten Variante. Was passiert, wenn nur die Betreffregel geändert wird? Muss die Übergabefunktion nun eine Sonderoption bekommen? Bleiben ihre Tests verständlich? Solche Fragen zeigen mehr als eine reine Zählung eingesparter Zeilen.

Ebenso wenig ist jede Duplikation sofort ein großer Umbauauftrag. Wenn die gemeinsame Bedeutung noch unklar ist, kannst du zunächst die betroffenen Stellen und ihre Unterschiede festhalten. Eine spätere belastbare Entscheidung ist günstiger als eine vorschnelle Universalabstraktion.

## Lass den Agenten Regel und Struktur getrennt bearbeiten

Ein sinnvoller Auftrag beginnt mit der Bestandsaufnahme: Aufrufer suchen, die vermutete gemeinsame Regel beschreiben und Unterschiede benennen. Erst danach folgt der Vorschlag für eine gemeinsame Zuständigkeit.

Falls die bisherigen Stellen widersprüchliche Ergebnisse liefern, braucht es eine fachliche Entscheidung. Ein erhaltender Strukturumbau und eine Korrektur des gewünschten Verhaltens sind verschiedene Änderungen. Thomas und Hunt grenzen Refactoring ausdrücklich auf Strukturänderungen bei erhaltenem äußerem Verhalten ein.{q:1}

Wähle als nächsten Schritt eine verdächtige Doppelung. Lass den Agenten den gemeinsamen Änderungsgrund formulieren und eine mögliche unabhängige Änderung durchspielen. Führe die Stellen zusammen, wenn die Verantwortung übereinstimmt. Wo fachliche Unterschiede bestehen, erhalten sie eigene Namen und eigene erlaubte Änderungen.
