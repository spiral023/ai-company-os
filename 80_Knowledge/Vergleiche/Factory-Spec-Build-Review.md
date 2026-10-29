# Vergleich: Spec, Build und Review in der Factory

**Stand:** 2026-10-29 · **Pilot-ID:** `s-ablauf` · **Status:** kuratierter Entwurf, kein aktivierter Produktionsworkflow

## Kernaussage

Eine belastbare Factory braucht verschiedene Artefakte für verschiedene Entscheidungen: geklärte Anforderungen, langlebige Verhaltenstickets, aktuelle Ausführungspläne, tatsächliche Änderungen und getrennte Prüfergebnisse. An jeder Übergabe muss erkennbar sein, welche Frage beantwortet ist und welche offen bleibt.

Die [Pilot-Registry](../Factory/pilot.json) bindet die Aussagen an konkrete Textstände. Die fünf [Fähigkeitskarten](../Faehigkeiten/README.md) sind daraus abgeleitete Kandidaten für diesen Ablauf.

## Übersicht

| Aufgabe | Geeigneter Baustein | Prüffähiger Abschluss | Aussagen |
|---|---|---|---|
| Offene Produktentscheidungen klären | Grilling und eigener Entscheidungsbaum | Entscheidungen und Annahmen erkennbar, offene Punkte benannt | `c13` |
| Vorhandenen geklärten Kontext formulieren | To-spec als Synthese | Lokaler Spec-Entwurf mit Grenzen und Testseams | `c21` |
| Arbeit in Verhaltenseinheiten zerlegen | Vertikale Slices, Blocker, begründete Migrationsausnahme | Jede Einheit beobachtbar und verifizierbar | `c12` |
| Ausführung konkretisieren | Begrenzter aktueller Plan mit Dateien, Symbolen und Nachweisen | Auftrag ist ausführbar oder seine Hindernisse sind sichtbar | `c23` |
| Spec-Erfüllung und Standards prüfen | Zwei lesende Reviewachsen | Getrennte Findings mit Regel-/Anforderungsbezug | `c08`, `c09`, `c24` |
| Verhalten nachweisen | Reale Einstiegsschnittstelle und dokumentierter Lauf | Beobachtung samt Umgebung, Ergebnis und Grenzen | `c14`, `c15` |

Die ZazenCodes-Demo (`c18`) illustriert Spec-Writer → Builder → Fachreviews → Approver. Sprogis (`c07`) ergänzt Erfolgskriterien und begrenzte Wiederholungen. Friedmans Argument (`c06`) begrenzt die Interpretation: Eine Reviewer-Rolle allein stellt keine unabhängige Abnahme her. Eigene Regeln (`c19`) bestimmen die erlaubten Aktionen.

## Drei Spannungen fachlich auflösen

### Interview oder direkte Spec-Synthese?

Grilling (`c13`) stellt offene Entscheidungen in den Mittelpunkt. To-spec (`c21`) soll bereits bekannten Kontext ohne neue Interviewrunde verdichten. Für den Pilot gilt: Erst erkennen, ob eine Entscheidung offen ist. Fakten recherchieren; fehlende Nutzerentscheidungen klären; ausreichend geklärten Kontext anschließend formulieren. Die Vorschriften widersprechen sich erst, wenn ihre unterschiedlichen Eingangszustände ignoriert werden.

### Langlebige Tickets oder dateigenaue Pläne?

To-tickets vermeidet grundsätzlich konkrete Dateipfade im Ticket (`c22`), während der große pstack-Plan sie ausdrücklich nennt (`c23`). Unser Entwurf trennt die Lebenszyklen: Das Ticket beschreibt erwartetes Verhalten und Abnahme; der Ausführungsplan bindet sich an die aktuelle Projektversion. Ein später verschobenes Modul muss dadurch nicht die fachliche Anforderung verändern. Prototypische präzise Entscheidungen bleiben eine benannte Ausnahme.

### Kleine Methoden oder ein Framework als Ablaufbesitzer?

Matt Pocock betont frei kombinierbare Methoden (`c10`); pstack verwendet einen übergeordneten Playbook-Router (`c11`). Für einen Factory-Lauf braucht es einen klaren Eigentümer des Ablaufs. Einzelmethoden werden bewusst zugeordnet. Mehrere vollständige Orchestratoren gleichzeitig zu laden ist kein belegter Vorteil.

Diese drei Auflösungen sind unsere Einordnung der Originalanweisungen, keine gemessenen universellen Regeln.

## Abnahmevertrag und Fehlerpfad

Spec-, Standards- und Funktionsprüfung behalten eigene Aussagen. Fehlt eine Spec, lautet der entsprechende Status nicht geprüft (`c09`). Ein Standardsbefund zitiert eine vorhandene Projektregel oder kennzeichnet eine Heuristik (`c24`). Ein Verifikationsentwurf wird erst durch einen tatsächlichen Prüflauf bestätigt (`c15`). Kein einzelnes grünes Ergebnis beweist alle übrigen Eigenschaften.

Abnahmebedingungen und erlaubte Nacharbeit stehen vor der Umsetzung fest. Eine Reparaturschleife bekommt einen konkreten Befund und ein Limit (`c07`). Nicht prüfbare Kriterien und ungelöste Abhängigkeiten bleiben offen. Für Commits und Produktion gelten die vorhandenen Freigaberegeln (`c19`); die Kandidatenkarten erweitern den Auftrag nicht.

## Ergänzung aus dem Quellenlauf vom 28.10.2026

[[Qualitaetsaufwand-nach-Folgen-und-Abhaengigkeiten-staffeln]] begründet die Prüftiefe mit Ausfallfolgen, Neubaukosten, Abhängigkeiten und Wartung. Das aus Sprogis vermittelte Raster ist eine Heuristik, keine neue Freigabepolicy. Die ausgewählten Kriterien brauchen weiterhin tatsächliche Nachweise.

Das [[2019-09-13-pdf-the-pragmatic-programmer-20th-anniversary-edition|Buch]] unterscheidet wegwerfbare Prototypen von weiterverwendetem Tracer Code und warnt vor grünen Tests ohne fachlichen Fortschritt. [[Frontend-Zustandslogik-mit-Reducer-isolieren]] konkretisiert eine mögliche Prüfgrenze: Zustandsübergänge separat testen, anschließend Browser-Anbindung und Effekte abnehmen. Diese Ergänzungen ändern weder Pilot-Registry noch aktivierte Workflows.

## Belegpfad

Ergänzung vom 29.10.2026 außerhalb der unveränderten Pilot-Registry: [[2026-10-29-matt-pocock-software-factories-real-engineers]] verbindet Domain Language, sparsame ADRs, Decision Map, Spec und dreistufige Prüfung in einer ausführlichen HTML-Lehrdemo. Decision Tickets beantworten vor der Delivery offene Fragen; sie sind von späteren Implementierungstickets zu unterscheiden. [[Matt-Pocock-Software-Factories-Kurstransfer]] konkretisiert den Anschluss an die vier Softwarebücher und einen begrenzten Prüfversuch. Die Videos wurden nur archiviert; der Kurs erzeugt keine unabhängige zweite Herkunft für bereits vorhandene Pocock-Skills. Die Pilot-Aussagen und Fähigkeitskarten wurden nicht geändert.

Ergänzung vom 27.10.2026 außerhalb der unveränderten Pilot-Registry: [[2026-10-26-addyosmani-2114604912520921136]] konkretisiert begrenzte Review-Schleifen mit Ansatzprüfung nach drei erfolglosen Runden, späterem Fokus auf den neuen Diff und separater Bestandsprüfung. Das Diagramm nennt 2,08 gegenüber 1,32 Reviews bis zum Abschluss; ohne Messdesign ist das keine übertragbare Erfolgsquote. Die X-Fassung gehört zur selben Herkunft wie [[2026-10-15-claude-how-the-claude-code-team-does-code-review-claude]] und zählt nicht als unabhängiger Beleg. Für den lokalen Entwurf folgt als Prüffrage: Werden neue Fehler erkannt oder erzeugen wiederholte Altbefunde nur weitere Runden? Produktionsregeln und Fähigkeitskarten werden damit nicht geändert.

Die Aussagen `c06` bis `c15`, `c18`, `c19` sowie `c21` bis `c24` verweisen in [pilot.json](../Factory/pilot.json) auf Originalskills, Playbooks und archivierte Quellen. Spec- und Standards-Review stammen aus derselben Matt-Pocock-Quelldatei. Ihre getrennte Modellierung erzeugt keine zweite Herkunftsfamilie.

## Offene Fragen und kleinster Versuch

Eine kleine Feature-Änderung und einen mechanischen Refactor als lokale Planungs-/Reviewfälle verwenden. Absichtlich eine fehlende Anforderung, einen echten Regelverstoß und eine unklare Prüfumgebung einbauen. Erwartet werden passende Artefakte, getrennte belegte Findings und erkennbare offene Punkte. Bisher sind diese Fähigkeitsversuche vorbereitet; die Implementierung der Wissensschicht wurde technisch geprüft, eine Factory-Wirkung wurde nicht gemessen.
