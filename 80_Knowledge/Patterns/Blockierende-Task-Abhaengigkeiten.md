# Blockierende-Task-Abhaengigkeiten

**Konfidenz:** meinung

## Zweck

Verhindert, dass an einer Aufgabe begonnen wird, deren Voraussetzung noch nicht erfüllt ist (z. B. Auth-Routen bauen, bevor die Datenbank steht), indem Abhängigkeiten zwischen Tasks explizit im System statt implizit im Kopf des Agenten oder Nutzers gehalten werden.

## Funktionsweise

Tasks bekommen über `addBlockedBy`/`addBlocks` explizite, append-only Abhängigkeitslisten zu anderen Task-IDs — wiederholte Aufrufe ergänzen bestehende Listen, statt sie zu ersetzen. Ein Task mit offenen `addBlockedBy`-Einträgen kann nicht auf `in_progress` wechseln; sobald alle blockierenden Tasks `completed` sind, wird die Abhängigkeit automatisch aufgelöst und der Task freigegeben, ohne dass ein Mensch oder Agent den Graphen manuell abläuft. Jeder Task ist eine eigene Datei (z. B. JSON unter `~/.claude/tasks/<list-id>/`), der Status läuft strikt `pending → in_progress → completed`. Tasks ohne gegenseitige Abhängigkeit laufen parallel; ein nachgelagerter Task kann von mehreren parallelen Zweigen gleichzeitig abhängen (Merge-Punkt). Das Feld `owner` klassifiziert Tasks nach zuständigem Agenten, löst aber selbst keine Ausführung aus — Spawnen und Zuweisung bleiben getrennte Schritte.

## Vorteile

- Verhindert strukturell den häufigsten Reihenfolgefehler bei paralleler oder Multi-Session-Arbeit: Beginn vor erfüllter Voraussetzung.
- Der Graph macht parallele und sequentielle Abschnitte eines Vorhabens explizit sichtbar, statt sie nur im Kopf zu tragen.
- Append-only-Semantik verhindert versehentlichen Verlust bereits gesetzter Abhängigkeiten bei wiederholten Updates.

## Nachteile & Grenzen

- Setzt einen vorab modellierten Graphen voraus — bei hoher Unschärfe über den tatsächlichen Ablauf entsteht Modellierungsaufwand, der sich erst später auszahlt (Kontrast zu [[Task-basierte-Steuerung]]).
- Der Mechanismus für parallelen Schreibzugriff mehrerer Agenten auf dieselbe Liste (Konfliktfreiheit bei simultanem Update) ist in der bisherigen Quelle unbelegt — kein Locking- oder Merge-Mechanismus beschrieben.
- Lohnt sich laut Quelle erst ab einer gewissen Komplexität (mindestens drei Schritte oder echte Abhängigkeiten); bei einfachen Einzelaufgaben ist der Graph-Overhead unnötig.

## Wann einsetzen, wann nicht

- Einsetzen: Vorhaben mit mindestens drei Schritten, echten Abhängigkeiten zwischen Teilschritten, Arbeit über mehrere Sessions oder Delegation an mehrere Agenten.
- Nicht einsetzen: schnelle Einzelfragen, einfache Single-File-Edits, oder Vorhaben mit so hoher Unschärfe, dass sich noch kein stabiler Abhängigkeitsgraph modellieren lässt — dort eher [[Task-basierte-Steuerung]].

## Belege

- 2026-01-23 · [[2026-01-23-nummanali-claude-task-system]] · meinung — X-Artikel von @nummanali beschreibt die vier Tools `TaskCreate`/`TaskUpdate`/`TaskGet`/`TaskList`, die Blockierlogik `addBlockedBy`/`addBlocks`, die Datei-pro-Task-Persistenz unter `~/.claude/tasks/<list-id>/` und `owner` als reines Filter-Label, anhand einer siebenteiligen JWT-Migration und einer achtteiligen Hochzeitsplanung als Beispielgraphen.

## Spannungen & offene Fragen

- Der Synchronisationsmechanismus für parallel schreibende Agenten (mehrere Agenten aktualisieren laut Quelle „ohne Konflikte“) bleibt unbelegt; ein Abgleich mit `external_repos/anthropics/claude-code/` lieferte keinen Engine-Quellcode, nur Plugin-/Hook-Beispiele. Bis zu einer Verifikation bleibt das unverifizierte Anwenderbeobachtung.

## Verwandte Patterns

- [[Task-basierte-Steuerung]]
- [[Kontrollierte-Agent-Parallelisierung]]
