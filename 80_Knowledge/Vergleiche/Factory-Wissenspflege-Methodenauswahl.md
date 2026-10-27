# Vergleich: Wissenspflege und Methodenauswahl

**Stand:** 2026-10-26 · **Pilot-ID:** `s-wissenspflege` · **Status:** kuratierter semantischer Pilot

## Kernaussage

Ein wachsender Bestand wird nutzbarer, wenn Herkunft, Version, Geltungsbedingungen und Ableitungen erhalten bleiben. Auffindbarkeit, fachliche Bewertung und tatsächliche Nutzung einer Methode sind eigene Entscheidungen. Die Factory erhält dadurch begründete Kandidaten und sichtbare Unsicherheit.

Die konkrete Kombination ist unsere Architekturhypothese `c20` in [pilot.json](../Factory/pilot.json). Der kleine Pilot implementiert Belegprüfung und Kontextbereitstellung. Eine bessere Qualität realer Factory-Läufe ist damit noch nicht nachgewiesen.

## Übersicht

| Referenzmechanismus | Eigene Übertragung | Grenze | Aussagen |
|---|---|---|---|
| Ressourcenidentität plus Belegversion | Datei, Bereich, SHA-256 und bei externen Repos HEAD speichern | Technische Identität ersetzt keine fachliche Bewertung | `c03` |
| Nicht auflösbar versus geändert | Fehlenden Beleg und veralteten Beleg getrennt melden | Die richtige Neubewertung wird nicht automatisch erzeugt | `c04` |
| Verschiedene Cacheversionskriterien | Eingangs- und Verarbeitungsversion berücksichtigen | Wiederverwendung ist keine Qualitätsprüfung | `c05` |
| Kleine Methoden versus Playbook-Router | Geltungsbedingungen und Ablaufverantwortung ausdrücklich wählen | Kein hier gemessener Gesamtsieger | `c10`, `c11` |
| Katalog versus Agent-Zuweisung | Kandidaten erfassen, Nutzung gesondert entscheiden | Kein Ersatz für die bestehende Registry und Import-Prüfung | `c16` |
| Aktueller State versus vollständiger Entscheidungsverlauf | Rekonstruierbare Ansichten von begründeten Entscheidungen unterscheiden | Workflowdokumentation belegt keine driftfreie Implementierung | `c17` |

## Herkunftsfamilien statt Wiederholungszählung

Ein Originalpost, sein Roharchiv, eine Source-Notiz und eine spätere Synthese können dieselbe Aussage wiederholen. Der Pilot ordnet diese Belege einer Herkunftsfamilie zu. Beispielsweise werden Friedmans Originaltext und die Source-Notiz gemeinsam gezählt (`c06`); ebenso die beiden Darstellungen der ZazenCodes-Veröffentlichung (`c18`). Mehrere Stellen desselben Matt-Pocock-Skills erzeugen ebenfalls keine unabhängige Zweitquelle.

Die Zahl unterschiedlicher Familien ist ein Hilfsmittel zur Nachvollziehbarkeit. Sie beweist nicht, dass die Autoren unabhängig voneinander gearbeitet haben oder dass eine Aussage zutrifft. Es gibt daher keine automatische Hochstufung zu verifiziert.

## Änderungen über die Ableitungskette sichtbar machen

Jede Aussage besitzt Belege oder explizite Ursprungsaussagen. Ein geänderter Datei-Hash oder Repo-HEAD markiert die betroffene Aussage und ihre abgeleiteten Synthesen/Fähigkeiten als prüfbedürftig. Ein betroffenes Kontextpaket enthält dann keine freigegebenen Aussagen oder Methodenkandidaten. Die Änderung wird nicht stillschweigend als neue Wahrheit übernommen.

Die Prüfung ist bewusst konservativ: Auch eine inhaltlich harmlose Änderung kann Review auslösen. Unveränderte Dateien können umgekehrt weiterhin fachlich überholt sein, etwa durch eine neue Gegenquelle. Hashprüfung ist deshalb nur eine technische Frischeprüfung; die neue oder geänderte fachliche Einordnung bleibt eine datierte redaktionelle Arbeit.

## Aus einer Methode einen Kandidaten machen

Die [Fähigkeitskarten](../Faehigkeiten/README.md) halten Ziel, Inputs, prüfbare Outputs, Voraussetzungen, Vorgehen, Stop-Grenze, Laufzeitabhängigkeit und kleinsten Versuch fest. Quellenanweisungen werden in einen eigenen fachlichen Vertrag eingeordnet. Die Kandidaten enthalten keine Installation und starten keinen fremden Orchestrator.

Für die erste Auswahl gelten drei Fragen: Passt die Methode zur Aufgabe? Sind Voraussetzungen und erlaubte Aktionen vorhanden? Welcher Nachweis würde ihren Nutzen oder ihr Scheitern zeigen? Bei gleicher Aufgabe können verschiedene Methoden konkurrieren. Ein kleiner Vergleich mit denselben Eingaben ist aussagekräftiger als ein unbegründeter Sieger aus dem Katalog.

## Gesamtbetrachtung und Rückfluss

Neue Querverbindungen entstehen durch das gemeinsame Lesen verschiedener Synthesen. Dieser Pilot verbindet beispielsweise Kontextversionierung, Aufgabenrouting und methodische Aktivierungsbedingungen. Die Quellen belegen die Einzelmechanismen; die daraus gebildete Kombination `c20` ist eine eigene, zu prüfende Ableitung.

Die vollständige Bestandsanalyse bleibt vom Pilot getrennt. Der allgemeine Analyseplan enthält weiterhin offene Arbeit; neue Aussagen müssen erst geprüft und aufgenommen werden. Ergebnisse echter Factory-Läufe können spätere Belege liefern, wenn Auftrag, verwendete Wissensversion, Prüfungen, menschliche Eingriffe und Grenzen erhalten bleiben. Einzelne erfolgreiche oder fehlgeschlagene Läufe werden zunächst Lernkandidaten.

## Belegpfad und offene Fragen

Die Aussagen `c03`, `c04`, `c05`, `c06`, `c10`, `c11`, `c16`, `c17`, `c18` und `c20` sind in [pilot.json](../Factory/pilot.json) auf aktuelle Bereiche und Ableitungen gebunden. Die Registry führt Herkunftsfamilien und Nachweisarten pro Aussage.

Offen sind die erste reale Aufgabenklasse, ein belastbarer Methodenvergleich und der Aufnahmeprozess für neue Gegenargumente außerhalb des Piloten. Der kleinste technische Versuch verändert eine Belegkopie: Erwartet werden Prüfebedarf, sichtbare betroffene Ableitungen und ein gesperrtes Kontextpaket. Der fachliche Versuch vergleicht anschließend tatsächliche Antworten und menschliche Korrekturen.
