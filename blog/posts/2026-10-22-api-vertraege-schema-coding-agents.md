---
titel: "API-Verträge für Coding Agents: Schema und Clients gemeinsam prüfen"
datum: 2026-10-22
kategorie: arbeitsweisen
zusammenfassung: "API-Verträge machen Pflichtfelder und erlaubte Werte für Coding Agents sichtbar. Leite Typen und Clients aus einem Schema ab und prüfe Fachregeln sowie ausgelieferte Versionen zusätzlich."
status: freigegeben
geprueft_am: 2026-10-22
freigabe: automatisch
quellen:
  - 2026-10-11-shiptypes-ship-types-not-docs
  - 2026-10-12-sarahfim-2109736893198016898
---

## Kurz gesagt

- Pflege die Struktur einer Schnittstelle an einer maßgeblichen Stelle und leite benötigte Typen und Clients daraus ab.
- Prüfe in CI, ob die erzeugten Dateien aktuell sind und die angebundenen Verbraucher weiterhin zum Vertrag passen.
- Ergänze Laufzeitvalidierung und Tests für Fachregeln, die ein Feldtyp allein nicht ausdrückt.
- Beginne an einer Schnittstelle mit wiederkehrenden Fehlern; ein vollständiger Architekturumbau ist dafür kein sinnvoller Startpunkt.

## Wenn der Agent das falsche Feld verwendet

Dein Backend erwartet `projectId`, der Agent sendet `project_id`. Die Dokumentation enthält noch ein älteres Beispiel. Du korrigierst den Aufruf, beim nächsten Feature taucht dieselbe Abweichung in einem anderen Client auf.

API-Verträge sollen solche Strukturentscheidungen für Produzenten und Verbraucher gemeinsam sichtbar machen. Ein API-Schema beschreibt Pflichtfelder, Datentypen und erlaubte Werte maschinenlesbar. Ein Coding Agent kann diese Beschreibung beim Schreiben des Aufrufs verwenden.

Boris Tane schlägt in „Ship types, not docs“ vor, Typen, Validatoren und Clients aus einer gemeinsamen Schemaquelle abzuleiten. Sarah beschreibt in ihrem Composio-Praxisbericht ebenfalls typisierte Verträge, damit Änderungen bis zu betroffenen Aufrufern sichtbar werden. Beide Texte beschreiben Arbeitsweisen; daraus folgt keine Garantie für fehlerfreie Integrationen.{q:1}{q:2}

## Ein Schema hat eine konkrete Zuständigkeit

Wähle für eine Schnittstelle eine maßgebliche Vertragsbeschreibung. Welche Technik dazu passt, hängt von deinem vorhandenen Stack ab. Der Zweck ist, dass Feldnamen und erlaubte Formen nicht unabhängig in Backend, Frontend und Beispieldokumentation gepflegt werden müssen.

Ein synthetischer Auftrag zum Anlegen einer Aufgabe könnte so aussehen:

```json
{
  "projectId": "projekt-demo",
  "title": "Import prüfen",
  "priority": "normal"
}
```

Das ist ein illustratives Datenbeispiel, kein Aufruf gegen eine bestehende API. Der zugehörige Vertrag müsste festlegen, ob `title` leer sein darf, welche Werte `priority` akzeptiert und ob weitere Felder zulässig sind. Eine JSON-Beispielantwort allein klärt diese Fragen nicht.

Beschreibe außerdem Fehler und Responses. Ein Client braucht auch für einen abgelehnten Auftrag eine verlässliche Form. Die Bedeutung des Vorgangs bleibt als Prosa erhalten: Wann soll eine Aufgabe angelegt werden, was bewirkt sie und welche Voraussetzungen gelten?

Tanes Vorschlag verbindet dafür ein Schema mit abgeleiteten Typen, Laufzeitprüfung und generierten Darstellungen wie OpenAPI oder Clients. Die Verbindung muss im jeweiligen Projekt eingerichtet und gepflegt werden; eine Schemadatei erzeugt diese Rückmeldung nicht von selbst.{q:1}

## Generierte Clients müssen am geprüften Stand hängen

Ein Typecheck kann einen falschen Feldnamen dort erkennen, wo ein Aufrufer an den passenden Typ angebunden ist. Ein frei zusammengesetzter Request oder eine umgangene Typprüfung kann außerhalb dieser Verbindung liegen.

Nimm bei einer Vertragsänderung deshalb die verwendeten Verbraucher in den Prüfauftrag auf. Wo wird der Client erzeugt? Welche Anwendung importiert ihn? Welche Version liegt ihrem Build zugrunde? Diese Fragen sind konkreter als die Aussage, das Projekt sei durchgehend typisiert.

Tane empfiehlt, die abgeleiteten Dateien in CI neu zu erzeugen, Abweichungen zum eingecheckten Stand zu erkennen und die Verbraucher zu prüfen. Sarah setzt Compilerfeedback ebenfalls als Rückmeldung für Agenten ein. Das erreicht jeweils die angebundenen und ausgeführten Prüfungen.{q:1}{q:2}

Für deinen Einstieg bietet sich dieser begrenzte Ablauf an:

- Ändere den Vertrag an seiner maßgeblichen Stelle.
- Erzeuge die betroffenen Typen und Clients erneut.
- Kontrolliere den Diff auf erwartete und unerwartete Änderungen.
- Führe den Typecheck der angebundenen Anwendungen aus.
- Prüfe einen erfolgreichen Aufruf und einen passenden Fehlerfall am laufenden Backend.

Ein lokaler Typecheck und ein Integrationstest beantworten dabei verschiedene Fragen. Halte fest, welche Prüfung welche Verbindung erreicht hat.

## Fachlich falsch kann weiterhin typkorrekt sein

Im Aufgabenbeispiel kann `projectId` eine gültige Zeichenkette sein und trotzdem das falsche Projekt bezeichnen. Ein Titel kann die erlaubte Form erfüllen und inhaltlich unbrauchbar sein. Auch die richtige Antwortstruktur sagt noch nicht, ob der Auftrag den erwarteten Zustand erzeugt hat.

Laufzeitvalidierung prüft die tatsächlich eingehenden Daten gegen die implementierten Regeln. Fachliche Prüfungen brauchen zusätzlich die Bedeutung des Vorgangs und gegebenenfalls vorhandenen Zustand. Welche dieser Bedingungen bereits im Schema ausdrückbar sind, hängt vom Schema und seiner Ausführung ab.

Leite relevante Verhaltenstests deshalb aus der Anforderung ab. Im Beispiel könntest du kontrollieren, dass die neue Aufgabe zum ausgewählten Projekt gehört und ein unbekanntes Projekt zum vereinbarten Fehler führt. Der [Beitrag über grüne Tests und übersehene Fehler](post:gruene-tests-bug-bleibt) zeigt, weshalb der echte Entscheidungspfad dafür erreichbar sein muss.

Prüfe außerdem die Kombination ausgelieferter Versionen. Ein neuer Server kann neben einem noch geöffneten älteren Webclient laufen. Ein gemeinsam erfolgreicher Build des neuesten Codes untersucht diese Kombination nicht automatisch. Tanes weitreichende Gleichsetzung von Compile-Erfolg und korrektem Verhalten reicht dafür nicht aus.{q:1}

## Beginne an der wiederholt falsch benutzten Schnittstelle

Suche eine API-Grenze, an der Feldnamen, fehlende Werte oder veraltete Clients bereits Nacharbeit verursachen. Verfolge dort den Weg vom Vertrag über die Erzeugung bis zum verwendeten Client. Tane empfiehlt für bestehende Systeme ebenfalls einen schrittweisen Einstieg an häufig genutzten Grenzen.{q:1}

Gib deinem Coding Agent einen Auftrag mit genau diesem Umfang: maßgebliches Schema finden, angebundene Verbraucher benennen, eine begrenzte Änderung durchführen und ausgeführte Prüfungen zuordnen. Offene Verbraucher und ältere Versionen gehören ausdrücklich ins Ergebnis.

Beurteile den nächsten Schritt anhand der verbleibenden Fehler. Werden weiterhin Payloads frei nachgebaut, fehlt eine Anbindung. Werden typkorrekte Aufträge fachlich falsch verarbeitet, brauchst du eine passende Regel und ihre Prüfung. Erweitere den Vertrag dort, wo du die konkrete Lücke gefunden hast.
