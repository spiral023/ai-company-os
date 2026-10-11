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

- 2026-10-05 · [[2026-10-05-aihero-v1-3-implement-spec-pr-retro-and-glossary-md]] · meinung — `/implement-spec` startet Implementierer für nicht mehr blockierte Tickets in eigenen Worktrees, führt Ergebnisse auf einer Integrationsbranch zusammen und überprüft den Gesamtstand anschließend mit `/code-review`; der Autor benennt große Branches und semantische Merge-Kollisionen ausdrücklich als ungelöste Grenzen.
- 2026-07-13 · [[2026-07-13-matt-pocock-live-the-wayfinder-demo]] · meinung — Pocock bearbeitet unabhängige Klärungen parallel, wartet bei abhängigen Punkten und erklärt manuelles Nachführen neu entdeckter Wechselwirkungen. Der Ablauf zeigt fachliche Sperren, aber keinen Nachweis automatischer Konfliktfreiheit zwischen Sessions.
- 2026-07-30 · [[2026-07-30-matt-pocock-wayfinder-nothing-is-too-big-to-plan-anymore]] · meinung — Offene Entscheidungen werden hinter noch ausstehender Recherche, Prototypen oder anderen Entscheidungen gesperrt; nach Auflösung verschiebt sich die nächste bearbeitbare Grenze. Das erklärt fachliche Abhängigkeiten vor Implementierung, ohne unabhängige Wirkungsmessung.
- 2026-08-12 · [[2026-08-12-shannholmberg-2087539757052285200]] · meinung — Beschreibt abhängige Kampagnenentscheidungen und die Auswahl aktuell unblockierter Tickets; ein konkretes Tracker-System wurde nicht geprüft.

## Spannungen & offene Fragen

- Der Synchronisationsmechanismus für parallel schreibende Agenten (mehrere Agenten aktualisieren laut Quelle „ohne Konflikte“) bleibt unbelegt; ein Abgleich mit `external_repos/anthropics/claude-code/` lieferte keinen Engine-Quellcode, nur Plugin-/Hook-Beispiele. Bis zu einer Verifikation bleibt das unverifizierte Anwenderbeobachtung.
- 2026-10-05: Pocock hält die deterministische Ticket-Schleife für verlässlicher als eine durch Agents gesteuerte Schleife. Worktree-Isolation verlagert Kollisionen auf den Merge; ein abgearbeiteter Task-Graph garantiert daher keine konfliktfreie Gesamtänderung. → [[2026-10-05-aihero-v1-3-implement-spec-pr-retro-and-glossary-md]]

## Verwandte Patterns

- [[Task-basierte-Steuerung]]
- [[Kontrollierte-Agent-Parallelisierung]]
