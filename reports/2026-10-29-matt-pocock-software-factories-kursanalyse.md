# Matt Pococks Software-Factory-Kurs: Analyse und deutscher Lesepfad

**Stand: 29.10.2026.** Der Kurs verbindet präzise Fachsprache, bewahrte Entscheidungsgründe, gezielte Untersuchungen und nachvollziehbare Review-Belege. Sein größter Wert für unsere Factory liegt in den konkreten Übergaben zwischen diesen Arbeitsweisen. Weder ein ausgefülltes Glossar noch eine geschlossene Map oder eine grüne Testsuite beweist für sich die fachliche Richtigkeit des Produkts.

## Umfang und Nachweis

Der Nutzer stellte 38 MP4-Dateien und eine HTML-Leseausgabe bereit. Alle 39 Dateien wurden vollständig kopiert und mit SHA-256 gegen den Eingang verglichen: 1.664.537.099 Bytes. Die Analyse umfasst sämtliche 38 HTML-Kapitel, erklärende Prosa, Beispielprompts, Übungen, Lösungen und Quiztexte. Die Videos wurden ausschließlich archiviert und inventarisiert; sie wurden nicht abgespielt oder transkribiert.

Das ursprüngliche Veröffentlichungsdatum ist nicht ausgewiesen. Der 29.10.2026 ist der Erfassungstag, keine behauptete Kursveröffentlichung. Die Zuordnung zu Matt Pocock stammt vom Nutzer und passt zu den verlinkten Skills und beschriebenen Inhalten; die Herkunft der zusammengestellten Leseausgabe wurde nicht unabhängig festgestellt.

Der reguläre Artikel-Ingest wurde mit der lokalen Datei-URL verwendet. Er wählte zunächst nur den ersten article-Container und erfasste dadurch Kapitel 1. Vor der Verarbeitung wurde die Rohnotiz aus dem unveränderten gelieferten HTML um den Text aller 38 Kapitel ergänzt. Originaldatei, Kapitelinventar und Textknotenlisten machen diesen Umfang prüfbar. Es wurden keine vom Kurs beschriebenen Git-, API-, Zahlungs-, Secret- oder Deploymentaktionen ausgeführt.

156 verlinkte Abbildungen wurden in Originalauflösung lokal gespeichert. Die Diagramme 37 (Fidelity), 51 (Ticketabhängigkeiten), 118 (drei Prüfebenen), 125 (Reversibilität), 139 (Implementierung und Review) und 148 (Reviewgeschwindigkeit und Priorität) wurden groß angesehen. Drei Kontaktbögen ergänzen die visuelle Orientierung. Das ist eine gezielte Sichtung, keine Behauptung, sämtlichen Screenshottext unabhängig abgelesen zu haben. Die Analyse der übrigen Demonstrationen stützt sich auf deren vollständige schriftliche Darstellung.

## Deutsche HTML-Fassung

[Deutsche Leseausgabe – lokal](../00_Inbox/Quellen/URL/lokal/matt-pocock-software-factories-real-engineers/index.de.html) · [unverändertes Original – lokal](../00_Inbox/Quellen/URL/lokal/matt-pocock-software-factories-real-engineers/index.html) · [Inventar und Ablagebeschreibung](../docs/kurse/matt-pocock-software-factories/README.md).

2.932 eindeutige Eingabe-IDs sind berücksichtigt: 2.757 Textknoten sowie 175 Beispielblöcke. Davon wurden 110 Blöcke vollständig oder in ihren klar natürlichsprachlichen Teilen übersetzt; 65 technische beziehungsweise leere Blöcke bleiben unverändert. Ausführbare Syntax, Dateinamen, Skill-Aufrufe und technische Identifier werden erhalten. Fachliche Bezeichnungen bleiben dort Englisch, wo die Benennung selbst Gegenstand der Diskussion ist. Screenshots und Diagramme bleiben bildlich im Original, ihre Bildunterschriften sind Deutsch.

Die Ausgabe behält alle Kapitelanker, 22 Quizfragen mit identischen Antwortschlüsseln und 98 Aufgaben-IDs. Jedes Kapitel verlinkt sein lokales Video. Bilder benötigen keine Remote-Aufrufe; externe Font-Links entfallen zugunsten vorhandener Systemschriften. Browserfortschritt der deutschen Ausgabe verwendet einen eigenen Speicher-Key. Lange Begriffe können mobil umbrechen, feste Bildgrößen stabilisieren die Navigation, und eine Kapitelansicht begrenzt die gleichzeitig gerenderte Dokumentlänge. Beim Drucken bleiben sämtliche Kapitel enthalten.

## Übergreifende Erkenntnisse

1. **Sprache ist Teil des Modells.** Zustände, Akteure und Handlungen an Szenarien unterscheiden, bevor Bezeichner vereinheitlicht werden. Eine Refund Request, ihre Genehmigung und die tatsächliche Auszahlung beantworten verschiedene Fragen.
2. **Dokumenttypen tragen verschiedene Informationen.** Glossar: Bedeutung. ADR: wichtiger Entscheidungsgrund. Map: Klärungsstand und Abhängigkeiten. Spec: gewünschtes Verhalten. Tests und QA: beobachtetes Ergebnis. Eine lange Datei für alle Zwecke verdeckt diese Unterschiede.
3. **Untersuchung und Delivery brauchen getrennte Tickets.** Wayfinder organisiert Fragen, deren Beantwortung eine Entscheidung ermöglicht. Erst ein hinreichend geklärter Weg lässt sich belastbar in Umsetzungsslices überführen.
4. **Prototypen erhöhen die Gesprächsauflösung.** Das setzt klare Lernfragen, bewusst akzeptierte Shortcuts und ein begrenztes Ergebnis voraus. Demonstrierbarer Teilfortschritt ist noch keine allgemeine Integrationszusage.
5. **Prüfer haben verschiedene Grenzen.** Deterministische Checks, Agent-Review und menschliches Urteil ergänzen sich. Frischer Kontext schafft jedoch keine automatisch unabhängige fachliche Wahrheit.
6. **Review muss den nächsten Lauf beeinflussen können.** Aus konkreten Fehlern wenige begründete Verbesserungen ableiten. Mechanische Fehler bevorzugt durch Checks abfangen; echte Ermessensfragen gezielt dokumentieren.

Die folgenden drei Auswertungen enthalten 32 konkrete Erkenntnisse und zwölf abgeleitete Handlungsempfehlungen. Kursdarstellung und eigene Einordnung sind jeweils getrennt. Kapitel-IDs entsprechen den Ankern des lokalen Originals und der deutschen Fassung.

## Fachsprache, Entscheidungen und Planung über mehrere Sitzungen

### Gegenstand und Grenzen

Dieser Analysebaustein wertet den bereitgestellten HTML-Text der Kurskapitel 1–13 aus. Die Eingabe umfasst 967 Textknoten und 64 `pre`-Blöcke; alle 1.031 IDs wurden im Übersetzungsobjekt berücksichtigt. Der zusammenhängende Kontexttext wurde vollständig gelesen. Aussagen über Demonstrationen beruhen auf deren schriftlicher Beschreibung. Die Videos wurden nicht als angesehen behandelt; beschriebene Implementierungen, Tests oder Git-Zustände wurden hier nicht ausgeführt oder unabhängig überprüft.

Der Kurs verbindet Domänensprache mit konkreter Produktgestaltung und anschließend mit einer über mehrere Sitzungen verteilten Planung. Die folgenden zwölf Erkenntnisse unterscheiden die Kursposition von eigener Einordnung und Anwendung. Die Kapitel-IDs sind die Anker des gelieferten Textes.

### Kapitelabdeckung

| Kapitel | Kapitel-ID | Ausgewerteter Schwerpunkt |
|---|---|---|
| 1 | `domain-language` | Kommunikationsprobleme, Glossar, Ubiquitous Language, Quiz |
| 2 | `using-grill-with-docs` | Übung zur Begriffsklärung und einheitlichen Umsetzung |
| 3 | `using-grill-with-docs-solution` | Refund Request, Refund, Zustände und Migration |
| 4 | `adrs` | Zweck, Minimalformat, drei Auswahlkriterien, Tagesfenster |
| 5 | `writing-an-adr` | Übung zu Genehmigung, Enrollment und Fortschritt |
| 6 | `writing-an-adr-solution` | Szenarien, Rollen, Team Licence, vier ADRs |
| 7 | `pruning-the-glossary` | Übung zur begründeten Glossarbereinigung |
| 8 | `pruning-the-glossary-solution` | Fachbegriffe, Zahlen, Umbenennungskosten, Enrollment |
| 9 | `pruning-adrs` | Übung zu Beibehalten, Löschen und Kennzeichnung |
| 10 | `pruning-adrs-solution` | Codeabgleich, entfernte ADRs und neue Kehrtwende |
| 11 | `q-a` | Bounded Contexts, Menschen im Prozess, frühe Umbenennung |
| 12 | `the-limits-of-one-session` | Kontextverwaltung und passende Fidelity |
| 13 | `charting-the-way` | Wayfinder-Map, Tickets, Frontier und Tickettypen |

### Zwölf konkrete Erkenntnisse

#### 1. Sprachprobleme können sich bis in die Bedienung fortsetzen

Der Kurs zeigt dieselbe Rückzahlungsanfrage unter Bezeichnungen wie Cancellation, Reversal und Chargeback. Der Nutzer sieht verschiedene Wörter in Button, E-Mail und Einstellungen; Agenten müssen dieselbe Bedeutung unter verschiedenen Bezeichnern suchen. Die vorgeschlagene Antwort ist ein gemeinsam verwendetes Glossar mit Anwendung in Gespräch, Oberfläche und Code. [`domain-language`, `using-grill-with-docs`]

**Eigene Einordnung:** Der Text erklärt erfundene Agentenbegriffe mit Tokeneffizienz. Das ist eine Autorenbehauptung, keine vorgeführte Kausalanalyse aller Modelle. Als Arbeitsschritt ist die beobachtbare Frage hilfreicher: Welche Wörter verwendet der Agent, die weder im Team noch im Produkt definiert sind? Ein passender Name allein beweist außerdem noch kein korrekt implementiertes Feature. [`domain-language`]

#### 2. Szenarien trennen Entscheidung und Geldtransfer

Die Lösung unterscheidet Refund Request als Anfrage und Entscheidung von Refund als tatsächlichem Geldvorgang. Wiederholte Anfragen nach Ablehnung sowie eine genehmigte, aber fehlgeschlagene Zahlung machen die Unterscheidung greifbar. Open, Approved und Declined gehören zur Anfrage; Pending Refund, Issued Refund und Failed Refund betreffen die Geldbewegung. „Approved am Montag, Bestätigung am Donnerstag“ verhindert, dass am Dienstag bereits „erstattet“ behauptet wird. [`using-grill-with-docs-solution`]

**Eigene Ableitung:** Ein Agent sollte Zustandstabellen an konkreten Verläufen prüfen, bevor er Statuswerte zusammenlegt. Entscheidungszustand, Versuch und Ergebnis können verschiedene Fragen beantworten. Das Kursmodell ist eine Produktentscheidung und kein allgemeines Regelwerk für reale Erstattungsprozesse. [`using-grill-with-docs-solution`]

#### 3. Zugang, Kauf und Fortschritt brauchen getrennte Fragen

Die Genehmigungsübung führt zunächst zu einer scheinbar einfachen Frage nach dem Lernfortschritt. Die Lösung entdeckt getrennte Speicherung von Enrollment, Fortschritt und Kauf. Team Licence und Individual Purchase gewähren unterschiedliche Dinge. Ein Refund Request muss den konkret ausgewählten Purchase betreffen, während ein weiterer Claimed Seat den Kursplatz erhalten kann. Kommentare und Bewertungen sollen nach dem beschriebenen Produktentscheid bestehen bleiben. [`writing-an-adr`, `writing-an-adr-solution`]

**Eigene Ableitung:** Vor einem Zustandswechsel lohnt eine Tabelle aus Gegenstand, Herkunft und Wirkung. „Kauf rückabwickeln“ beantwortet weder automatisch „Zugang entziehen“ noch „Lerndaten löschen“. Diese Trennung schützt vor unbemerkten Folgewirkungen; sie ersetzt keine eigenständige Prüfung der Regeln im jeweiligen Produkt. [`writing-an-adr-solution`]

#### 4. Codeerkundung korrigiert die sprachliche Diskussion

Der beschriebene Agent liest bestehende Routen und Schema vor weiteren Szenarien. Dabei fallen die falsche Auswahl des neuesten Kaufs, die uneinheitliche Rollenbezeichnung und die unterschiedliche Durchsetzung einer 50%-Grenze auf. Eine frühere Umbenennung erzeugt zudem eine Migration, die zunächst nur den Default für neue Datensätze ändert; bestehende Werte benötigen einen zusätzlichen Datenübergang. [`using-grill-with-docs-solution`, `writing-an-adr-solution`]

**Eigene Ableitung:** Eine semantische Umbenennung hat mehrere Reichweiten: Begriffe, Aufrufer, gespeicherte Werte und sichtbares Verhalten. Der Text beschreibt 23 neue Tests und eine nicht gezeigte Implementierung; daraus folgt hier kein eigener Ausführungsnachweis. Die Demonstration ist ein Anlass, diese Reichweiten im konkreten Auftrag sichtbar zu machen. [`writing-an-adr-solution`]

#### 5. Ein ADR bewahrt die verworfenen Wege

ADRs erklären im Kurs Gründe, die aus dem Endzustand des Codes schwer erschließbar sind. Das Minimalformat besteht aus kurzem Titel und ein bis drei Sätzen; Optionen und Folgen kommen nur bei Bedarf dazu. Drei Kriterien müssen zusammenpassen: relevante Umkehrkosten, Überraschung ohne Kontext und eine echte Auswahl zwischen Alternativen. Als Beispiel dient das Refund-Fenster nach ganzen Kalendertagen statt exakt verstrichenen Stunden. [`adrs`]

**Eigene Einordnung:** Die Einordnung einzelner Bibliotheken als leicht austauschbar gilt für die Beispielumgebung. Integrationsumfang oder Folgekosten können anderswo größer sein. Ebenso ist die Kalenderregel eine Produktentscheidung. Bei ihrer Umsetzung müssen konkrete Zeitbasis und Grenzfälle geklärt werden, statt allein den Namen eines Helpers zu übernehmen. [`adrs`]

#### 6. Glossarbereinigung braucht einen Zweckfilter

Die Bereinigungsübung entfernt Datenbankfelder und allgemeine Programmierbegriffe aus dem Domänenglossar. Ein slug kann dennoch später fachlich relevant werden, falls Nutzer darüber sprechen und eigene Operationen daran hängen. Ein veralteter Watch-Limit-Wert wird durch eine Definition ohne konkrete Zahl ersetzt. Das Kriterium ist somit Verwendung für das aktuelle Produkt, keine feste Liste verbotener Wörter. [`pruning-the-glossary`, `pruning-the-glossary-solution`]

**Eigene Einordnung:** Eine Geschäftsregel ist nicht schon deshalb unwichtig, weil sie als Konstante implementiert wird. Die konkrete Grenze braucht gegebenenfalls einen anderen maßgeblichen Platz. Außerdem wechselt die Lapsed-Erklärung von einem inaktiven Enrollment zu einem Student mit erhaltenem Fortschritt. Solche Wechsel sollten ausdrücklich auf ihren Bezugstyp geprüft werden. [`pruning-the-glossary-solution`]

#### 7. Bestehende Verwendung beeinflusst die Namenswahl

Bei learner und student hat der Autor zunächst keine starke Präferenz. Die Verteilung im vorhandenen Code führt dann zur Entscheidung für Student. Im Text werden zunächst 112 Vorkommen in 23 Dateien und später 180 student-Vorkommen gegenüber acht learner-Vorkommen genannt; die Übersetzung gleicht diese unterschiedlichen Angaben nicht nachträglich an. ADR-Texte, Dateinamen und Kommentare werden ebenfalls auf die vereinbarte Sprache gebracht. [`pruning-the-glossary-solution`]

**Eigene Ableitung:** Wenn zwei Begriffe fachlich gleich gut sind, können Umstellungskosten entscheiden. Häufigkeit macht aber einen unpassenden Begriff nicht richtig. Die Empfehlung, Umbenennungen vor Spezifikation und Tickets zu übernehmen, vermeidet anschließend veraltete Pfade. Umfang und Verifikation der Änderung bleiben eigenständige Arbeit. [`pruning-the-glossary-solution`, `q-a`]

#### 8. ADR-Pflege muss Geschichte und aktuellen Stand auseinanderhalten

Die Übung bietet Löschen und Kennzeichnung als überholt an. Die Lösung wählt eine strengere Variante: ersetzte Dateien entfernen und wichtige frühere Ansätze unter den erwogenen Optionen eines neuen ADR erklären. Das Beispiel 0012 hält die Aufgabe der ip-api.com-Abfrage zugunsten des Vollpreises bei unbekanntem Land fest. Die Commit-Historie bleibt ein weiterer Zugang zur alten Entscheidung. [`pruning-adrs`, `pruning-adrs-solution`]

**Eigene Einordnung:** Das ist eine mögliche Pflegepolitik, keine universelle Pflicht. Eine andere Organisation kann historische ADRs ausdrücklich unverändert erhalten und deren Status verknüpfen. Wichtig ist ein eindeutiger Weg zur aktuellen Entscheidung. Auch „Code ist maßgeblich“ beantwortet nur das implementierte Verhalten; ein unbeabsichtigter Bug wird dadurch nicht zum richtigen Sollverhalten. [`adrs`, `pruning-adrs-solution`]

#### 9. Ubiquitous Language benötigt einen Geltungsbereich

Kapitel 11 präzisiert die anfängliche Forderung nach einheitlicher Sprache. Quiz question und Discussion question lassen sich mit Präfixen unterscheiden. Wenn Produkt und Finanzen dagegen berechtigt verschiedene Modelle verwenden, sieht der Kurs eigene Glossare vor, verbunden durch GLOSSARY-MAP.md. ADRs können entsprechend global oder auf einen Bounded Context begrenzt sein. [`q-a`]

**Eigene Ableitung:** Ein Agent braucht die betroffene Modellgrenze mit seinem Auftrag. Sonst könnte er fachlich richtige Unterschiede als sprachlichen Fehler vereinheitlichen. Eine Glossaraufteilung macht die Grenze sichtbar, löst aber noch keine Datenübersetzung oder Integrationsverantwortung zwischen den Modellen. [`q-a`]

#### 10. Menschen behalten die Verantwortung für gemeinsame Sprache

Der Autor lehnt eine vollständig autonome Glossarpflege ab. Agenten gehören zum Team, sollen aber keine Sprache erfinden, die die Menschen nicht verwenden. Nutzerinterviews liefern geeignete Wörter; Glossare entstehen langsam, bedarfsgerecht und bleiben veränderbar. Auch die Lösung zeigt, wie der Mensch zusätzliche Begriffe wie Void Seat verwirft und eine erneute ADR-Prüfung verlangt. [`q-a`, `writing-an-adr-solution`]

**Eigene Ableitung:** Agenten können Sucharbeit, Varianten und Szenarien vorbereiten. Die Annahme des Begriffs braucht die betroffenen Menschen. Reines Sprachgefühl ist dabei ein Signal, kein vollständiger Nachweis: Ein zunächst ungewohntes, aber notwendiges Konzept darf nicht allein deshalb verschwinden, weil es sich unbequem anhört. [`writing-an-adr-solution`, `q-a`]

#### 11. Fidelity richtet sich nach der offenen Frage

Der Planungseinstieg beschreibt lange Einzelsitzungen, Verdichtungsverluste und mühsame Übergaben als Anlass für Wayfinder. Die Fidelity-Leiter reicht von Diskussion über Breadboarding, Wireframes und Prototyp bis zum produktiven Code. Ein höherer Ausarbeitungsgrad schafft mehr Anschauung, kostet aber mehr und bindet stärker. [`the-limits-of-one-session`]

**Eigene Einordnung:** Die genannten 200.000 oder 300.000 Tokens sind Szenarien des Kursautors und keine allgemeingültige Qualitätsgrenze. Ebenso ist der verschobene Engpass zur Planung eine Erfahrung, kein gemessener Satz für jedes Team. Sinnvoll übertragbar ist die Frage, welche Unsicherheit noch ein Gespräch klärt und für welche ein ausführbares Anschauungsobjekt erforderlich ist. [`the-limits-of-one-session`]

#### 12. Wayfinder trennt Übersicht, Detail und ausführbare Entscheidungsarbeit

Die Map ist ein Issue mit Ziel und knapper Übersicht; untergeordnete Entscheidungstickets enthalten Diskussion und Begründung. Abhängigkeiten bilden einen gerichteten azyklischen Graphen. Zur Frontier gehören genau die offenen, nicht blockierten und noch nicht übernommenen Kindtickets. Bereits übernommene Tickets bleiben auch ohne Blockade außerhalb der Frontier. Neue Erkenntnisse können zusätzliche Tickets erzeugen. [`charting-the-way`]

Grilling klärt Fragen im Gespräch, Prototype liefert Anschauung, Research beschafft fehlende Tatsachen, Task beschreibt nötige manuelle Vorarbeit. Der Kurs sieht Research als unmittelbar delegierte Arbeit vor. **Eigene Ableitung:** Zuweisung ist noch keine geprüfte Antwort; Herkunft, Erfüllung und Abschluss bleiben zu beurteilen. Geschlossene Tickets sind außerdem nur ein technisches Signal. Das festgelegte Ziel muss inhaltlich erreicht sein, bevor die Map als fertig gilt. [`charting-the-way`]

### Vier Handlungsempfehlungen für Agentic Engineering

1. **Einen unscharfen Vorgang durch Szenarien klären.** Sammle die aktuellen Namen, prüfe Antrag, Ablehnung, Wiederholung und zeitversetzte Ausführung. Führe danach eine kleine Tabelle aus Begriff, Zustand und zugesicherter Wirkung. Der Refund-Lebenszyklus zeigt, welche Unterschiede sonst verschwinden. Umsetzung und Persistenz werden anschließend gezielt kontrolliert. [`domain-language`, `using-grill-with-docs-solution`]

2. **Jede neue Dokumentdatei mit einer Frage rechtfertigen.** Ein Glossar erklärt Fachbedeutung; ein ADR erklärt eine wichtige Entscheidung samt Gründen. Halte Datenfelder und bloße Konventionen aus diesen Rollen heraus, wenn sie keinen zusätzlichen Nutzen liefern. Bestimme zugleich, wo konkrete Geschäftsparameter maßgeblich gepflegt werden. [`adrs`, `pruning-the-glossary-solution`, `pruning-adrs-solution`]

3. **Umbenennung als begrenzte Änderung abschließen.** Entscheide menschlich über den Begriff, ermittle seine Verwendung und ziehe UI, Code, Kommentare und relevante ADRs nach. Prüfe gespeicherte Werte zusätzlich zu Defaults. Erst danach sollten Spezifikation und Tickets die neuen Namen als aktuellen Stand verwenden. Die Aussage des Autors, solche Refactorings seien günstig, ersetzt die Prüfung ihrer tatsächlichen Folgen nicht. [`using-grill-with-docs-solution`, `pruning-the-glossary-solution`, `q-a`]

4. **Große Planung nach Entscheidungen und Unsicherheit aufteilen.** Bestimme zuerst das Ziel, dann eine kleine Map und ausführliche Tickets. Wähle Grilling, Prototype, Research oder Task nach der benötigten Erkenntnis. Prüfe vor Parallelisierung Abhängigkeiten und Übernahmezustand; führe abgeschlossene Erkenntnisse in der Übersicht zusammen. Zusätzliche Sitzungen sind damit an einen nachvollziehbaren Gegenstand gebunden. [`the-limits-of-one-session`, `charting-the-way`]

### Ergebnis und noch erforderliche Prüfung

Der eigenständige Beitrag dieser Kapitel besteht in der Verbindung von Sprachklärung, kleinen Entscheidungsdokumenten und dauerhafter Planungsstruktur. Der Kurs zeigt Korrekturen am eigenen Vorschlag: ein zu einfaches Refund-Modell wird erweitert, unpassende Glossarbegriffe werden entfernt, eine zunächst übersehene ADR-Würdigkeit wird erneut geprüft. Der nützliche Mechanismus ist wiederholtes Gegenprüfen an Szenarien und vorhandenem Verhalten. [`using-grill-with-docs-solution`, `writing-an-adr-solution`, `pruning-the-glossary-solution`]

Für die Anwendung bleibt zu prüfen, ob diese Dokumente im konkreten Team tatsächlich gelesen werden, die fachliche Entscheidung tragen und mit implementiertem Verhalten zusammenpassen. Die bereitgestellten HTML-Texte enthalten Erfahrungsurteile und Demonstrationen, keinen kontrollierten Produktivitätsvergleich. Die Übersetzung erhält diese Urteile; die Analyse macht daraus keine verifizierten Eigenschaften aktueller Modelle oder Dienste. [`domain-language`, `q-a`, `the-limits-of-one-session`, `charting-the-way`]


---

## Von offenen Fragen zu einer implementierbaren Entscheidung

### Gegenstand und Lesart

Die Kurskapitel 14–27 führen die Planung von In-App-Benachrichtigungen für Cadence durch: Wayfinder-Map, Entscheidungstickets, Anbieterrecherche, menschliche Einrichtung, funktionale und visuelle Prototypen, Spec und Implementierung. Ausgewertet wurden sämtliche vorliegenden HTML-Textknoten und pre-Blöcke dieser Kapitel sowie der zusammenhängende Planungstext. Videos wurden nicht angesehen. Bildunterschriften und Beschreibungen erzählen den Kursablauf; sie ersetzen keine eigene Sichtung der dargestellten Oberfläche. (Kap. 14–27)

**Autorenaussage** bezeichnet im Folgenden die Darstellung des Kurses. **Eigene Einordnung/Transfer** bezeichnet daraus abgeleitete Anwendungsvorschläge und Grenzen. Kein Schritt wurde im Cadence-Repo reproduziert, kein Dienst eingerichtet und keine Anbieterfunktion aktuell recherchiert. Die genannten Preise, Produkteigenschaften und Dashboard-Pfade sind Kursinhalt, keine heutige Empfehlung. (Kap. 15, 19, 21, 23, 27)

### Zehn konkrete Erkenntnisse

#### 1. Das Ziel eines Planungsvorgangs muss einen eindeutigen Artefakttyp haben

**Autorenaussage:** Bereits die erste Grilling-Runde fragt, ob die Map mit einer Spec, einer funktionierenden Implementierung oder Entscheidungen enden soll. Der Autor wählt ausdrücklich die Spec. Die Übung betont, dass das Ziel der aktuellen Session nicht das fertige Feature ist. Erst später folgen Umwandlung, Implementierung und QA. (Kap. 14 `chart-the-map`; Kap. 15 `chart-the-map-solution`; Kap. 26 `spec-implement`)

**Eigene Einordnung/Transfer:** Ein Auftrag „Plane und baue Benachrichtigungen“ vermischt unterschiedliche Abschlussbedingungen. Eine engere Session kann mit einem nachvollziehbaren Entscheidungsartefakt enden, obwohl noch kein produktiver Code entsteht. Das erleichtert einen späteren Kontextneustart. Die Grenze verhindert außerdem, dass ein erfolgreicher Planungsdialog unbeabsichtigt eine Freigabe für externe Einrichtung oder Veröffentlichung ersetzt. Ein geeignetes Ergebnis benennt Zielartefakt, betrachtete Version und ausgeschlossene Arbeit. (Ableitung aus Kap. 14–15, 26)

#### 2. Vier Ticket-Typen ordnen unterschiedliche Arten von Ungewissheit

**Autorenaussage:** Die erste Map enthält Research-, Grilling-, Task- und Prototype-Tickets. Recherche untersucht etwa Anbieter und Web-Push-Reichweite. Grilling klärt Entscheidungen wie den Ereigniskatalog. Eine Task verlangt ausgeführte Arbeit, beispielsweise die Registrierung. Ein Prototyp beantwortet eine Frage durch ein konkretes Experiment. Abhängigkeiten bestimmen, welches Ticket bearbeitbar ist. (Kap. 15; Kap. 16 `grilling-ticket`; Kap. 20 `task-ticket`; Kap. 22 `prototype-ticket`)

**Eigene Einordnung/Transfer:** Der Ticket-Typ sollte zum fehlenden Wissen passen. Eine Dokumentationsfrage braucht zunächst belastbare Informationen, eine fachliche Auswahl den zuständigen Entscheider und eine Integrationsfrage gegebenenfalls einen Versuch. Bei einem Task genügt eine getroffene Entscheidung ausdrücklich nicht. Zusätzliche Tickets kosten Verwaltung; ihre Rechtfertigung ist eine unterscheidbare Frage und ein erkennbarer Abschlussnachweis. (Ableitung aus Kap. 15–16, 20, 22)

#### 3. Eine Anbieterempfehlung bleibt bis zum passenden Versuch vorläufig

**Autorenaussage:** Die Recherche entscheidet zunächst für Knock. In der nächsten Entscheidungssession widerspricht der Autor einer sofortigen endgültigen Festlegung: Erst Registrierung, praktische Nutzung und Prototyp sollen zeigen, ob Knock passt. Ein zweites Prototype-Ticket prüft deshalb die Integration getrennt vom UI-Entwurf; Courier bleibt als Alternative. Zusätzliche Anmeldungen werden verschoben, bis ihr Bedarf feststeht. (Kap. 15; Kap. 18 `grilling-ticket-2`; Kap. 19 `grilling-ticket-2-solution`)

**Eigene Einordnung/Transfer:** Das ist eine nützliche Unterscheidung zwischen Auswahlhypothese und bestätigtem Projektentscheid. Der Kurs zeigt damit auch eine Korrektur seiner eigenen Map. Anbieterlisten allein beantworten keine Frage nach realer Bedienbarkeit oder Arbeitsaufwand. Aktuelle Preise, Sicherheitsmerkmale und kostenlose Tarife müssten vor einer heutigen Auswahl separat geprüft werden; diese Auswertung führt bewusst keine solche Recherche durch. (Ableitung und Grenze zu Kap. 15, 19, 23)

#### 4. Das Glossar beeinflusst Fachentscheidungen und spätere Reviews

**Autorenaussage:** Der Autor wählt Notification und Notification Feed. Question und Reply erhalten das Präfix Discussion, weil auch Quizfragen existieren. Refund-Auszahlungen stehen zwar im Glossar, fehlen aber im laufenden Code und bleiben deshalb vorerst unspezifiziert. Später beanstandet der Standards-Review Begriffe, die das Glossar ausdrücklich vermeiden will. (Kap. 15; Kap. 17 `grilling-ticket-solution`; Kap. 27 `spec-implement-solution`)

**Eigene Einordnung/Transfer:** Ein Glossar kann Begriffsverwechslungen und unerlaubte neue Benennungen sichtbar machen. Es beweist weder, dass eine Funktion existiert, noch dass ihre Semantik im Code korrekt umgesetzt ist. Ein Implementierungsauftrag sollte Begriff, vorhandenen Codepfad und noch geplantes Verhalten unterscheiden. Die konkrete Negation bleibt wichtig: Im beschriebenen Katalog erhalten eingeschriebene Students keine Benachrichtigung über eine neu hinzugefügte Lektion. Eine verkürzte Zusammenfassung könnte diese Entscheidung versehentlich umkehren. (Ableitung aus Kap. 17, 27)

#### 5. Ein Wizard erleichtert menschliche Schritte, braucht aber Gegenprüfungen

**Autorenaussage:** Der wizard-Skill erzeugt ein interaktives Bash-Skript für die Einrichtung. Der Mensch führt es in einem separaten Terminal aus und bedient das Dashboard. Dokumentation liefert konkrete Wege; eine unbekannte Schalterposition wird als Wissenslücke benannt. Nach erfolgreichem Durchlauf findet eine lokale Prüfung einen abgeschnittenen Signierschlüssel. Nach manueller Korrektur berichtet der Kurs einen echten API-Aufruf mit signiertem Token. (Kap. 20; Kap. 21 `task-ticket-solution`)

**Eigene Einordnung/Transfer:** „Wizard beendet“ und „Einrichtung funktioniert“ sind verschiedene Nachweise. Ebenso ist die Aussage, Secrets verließen das System nie, zu weit gefasst: Ein lokales Skript kann Werte entsprechend seinem Code an einen Dienst senden. Der enger begründbare Vorteil ist, dass die Eingabe nicht automatisch durch den Modellchat läuft. Ob das tatsächlich gilt, hängt von Skript, Terminal, Logging und beteiligten Werkzeugen ab. Die Kursbehauptung, Agenten kennten den richtigen Umgang mit Schlüsseln, ist keine technische Garantie. (Kritische Einordnung von Kap. 21; weiterer Dienstzugriff in Kap. 27)

#### 6. Ein funktionaler Prototyp braucht eine konkrete Prüfmatrix

**Autorenaussage:** Das Knock-Experiment untersucht vier vorab benannte Punkte. Prüfungen zwei bis vier benötigen zunächst Dashboard-Konfiguration. Es treten ein unklarer Wizard-Schritt, ein nicht funktionierender Antwortablauf und die Verwechslung von gesehen und gelesen auf. Cadence übernimmt den standardmäßig ausgeschalteten Enrollment-Wert. Die Abschlussentscheidung und Stolperfallen landen im Ticket; der Prototyp bleibt als Referenz auf einem separaten Branch. (Kap. 22–23 `prototype-ticket`, `prototype-ticket-solution`)

**Eigene Einordnung/Transfer:** Das Ergebnis ist hilfreicher als ein bloßer Screenshot: Frage, Ablauf, erwartetes Ergebnis und entdeckte Einschränkung können gemeinsam übergeben werden. Allerdings erlaubt der Prototype-Skill im Kurs Fehlerbehandlung wie `.catch(() => null)`, die Fehler vollständig ausblendet. Ein solcher Shortcut kann auch eine Machbarkeitsprüfung verfälschen, wenn gerade Fehlerverhalten oder Berechtigungen untersucht werden. Dass Benutzer 2 seinen Feed lesen kann, prüft für sich außerdem keine unzulässigen Zugriffe auf fremde Feeds. Der benötigte Nachweis richtet sich nach der konkreten Frage. (Ableitung und Grenze aus Kap. 23)

#### 7. Fidelity wird pro Frage gewählt und darf während des Versuchs sinken

**Autorenaussage:** Der Feed-Prototyp zeigt Glocken-Popover, Drawer sowie Inbox mit Toasts. Danach vergleichen weitere Varianten „Load more“, Infinite Scroll und „See all“, mit acht oder hundert Einträgen. Der Autor wählt A2 und verfeinert Details. Die Frage nach dauerhaft sichtbarer Historie wird anschließend in einer einfachen Liste besprochen. Er entscheidet sich für die gesamte Historie. (Kap. 24 `finish-the-map`; Kap. 25 `finish-the-map-solution`)

**Eigene Einordnung/Transfer:** Sichtbare Alternativen helfen bei Interaktion und Layout; eine textliche Auswahl kann für eine Verhaltensregel genügen. Das ist keine Pflicht, jede Entscheidung maximal auszuarbeiten. Die Auswahl dokumentiert hier vor allem die Vorlieben des Autors, keine Nutzerstudie. Aussagen über große Zeitersparnis, hohe Tokeneffizienz oder eine Klärung „ohne Tokens“ werden im Kurs gemacht, aber nicht als vergleichende Messung hergeleitet. Aus den genannten Sessionständen von 44K, 107K beziehungsweise 72,9k folgt kein allgemeines Budget. (Einordnung von Kap. 21, 23, 25)

#### 8. Geschlossene Tickets garantieren keine vollständige Map

**Autorenaussage:** Nach Abschluss aller neun Sub-Issues stehen noch Punkte unter Not yet specified. Der Autor startet eine letzte Grilling-Session auf der Map, fasst die Klärungen in einem weiteren Ticket zusammen und beseitigt die Restunklarheiten. Die Quizfrage bewertet genau dieses Vorgehen als richtig. Vorzeitiges Schließen, Löschen des Abschnitts oder ein Prototyp je Restpunkt sind die falschen Antworten. (Kap. 24–25)

**Eigene Einordnung/Transfer:** Vollständigkeit muss zusätzlich zum Status jedes erzeugten Tickets betrachtet werden. Sonst können Anforderungen außerhalb des Ticketgraphen verschwinden. Umgekehrt ist eine bewusst ausgeschlossene Funktion kein ungelöster Rest: E-Mail und Web Push werden für v1 ausgeschlossen, obwohl frühere Recherche sie untersucht hat. Eine spätere Map kann diesen Umfang wieder aufnehmen. Ein Abschluss sollte deshalb geklärt, ausgeschlossen und weiter offen eindeutig auseinanderhalten. (Ableitung aus Kap. 25)

#### 9. Map, Spec und Implementierungstickets haben verschiedene Leseraufgaben

**Autorenaussage:** `/to-spec` liest die Entscheidungstickets und verdichtet sie zu einer Spec mit 61 User Stories, Implementierungsentscheidungen und Prototype-Verweisen. `/to-tickets` schlägt zunächst zwölf Tickets vor; der Autor reduziert nach eigener Aussage eher nach Gefühl auf acht. Der Graph beginnt mit Prefactoring und einem End-to-End-Tracer-Bullet. Danach können fünf Tickets parallel bearbeitet werden. (Kap. 26–27)

**Eigene Einordnung/Transfer:** Die Spec macht verstreute Entscheidungen zugänglich, während Verweise ihre Herkunft erhalten. Dabei muss jede wichtige Negation und spätere Korrektur mitwandern. Eine reine Kürzung könnte etwa „später E-Mail“ in „E-Mail jetzt implementieren“ verwandeln. Acht ist keine ermittelte optimale Ticketzahl. Entscheidend sind kohärente Änderungsaufgaben, echte Abhängigkeiten und Integrationsaufwand. Ein erster durchgängiger Ablauf kann spätere Arbeit stabilisieren; parallele Branches ersetzen keinen gemeinsamen Verhaltensnachweis. (Ableitung aus Kap. 25–27)

#### 10. Automatische Implementierung endet im beschriebenen Beispiel mit weiteren Lernschleifen

**Autorenaussage:** Der Implementierungslauf liest Prototypen, führt Branches zusammen und startet Spec- und Standards-Review. Tests aus `.claude/worktrees/` zählen zunächst doppelt; ein Ausschluss in der Vitest-Konfiguration korrigiert das. Der Fix-Agent bearbeitet 15 Review-Funde und lässt fünf ausdrücklich beibehaltene Punkte stehen. Anschließend folgen Dienstkonfiguration, ein fehlgeschlagener Workflow-Push mit HTTP 422, Korrektur und Browser-QA für Frage, Antwort und Einstellungen. (Kap. 27)

**Eigene Einordnung/Transfer:** Die Erwartung „sollte auf Anhieb funktionieren“ aus der Aufgabe wird im beschriebenen Lösungsweg durch konkrete Nacharbeit begrenzt. Ein gesteigerter Testzähler kann aus Duplikaten stammen. Erfolgreicher Merge ist keine vollständige Abnahme. Das nachträglich entdeckte Management API verbessert die Automatisierung und wird als kurzer Skill festgehalten, benötigt aber einen passenden Service-Token. Die im Skill enthaltene Produktionsoption bleibt Quelltext des Kurses und erteilt keine Ausführungsfreigabe. Auch „zwangsläufig“ erfolgreiche Fehlerschleifen sind eine zugespitzte Autorenaussage: Messbarer Fortschritt braucht richtige Rückmeldung, sichere Wiederholbarkeit und sinnvolle Abbruchkriterien. (Einordnung von Kap. 26–27)

### Vier Handlungsempfehlungen für eigene Agentenarbeit

1. **Einen Auftragsrahmen festhalten.** Benenne Zielartefakt, Scope der aktuellen Version, Ticket-Typ und Abschlussnachweis. Lege externe Handlungen und menschliche Entscheidungspunkte gesondert fest. So werden Spec-Ziel, Anmeldeaufgabe und Implementierung nicht ineinander verschoben. (Eigener Transfer aus Kap. 14–15, 20, 26)
2. **Entscheidungen mit ihrem Versuch verbinden.** Halte beim Prototype-Ticket Fragestellung, konkrete Prüfungen, Shortcut-Grenzen und Ergebnis zusammen. Referenziere den isolierten Versuchscode ausdrücklich als Versuch und übernehme ihn nicht stillschweigend in die produktive Implementierung. (Eigener Transfer aus Kap. 19, 22–25)
3. **Übergaben auf Bedeutungsverlust prüfen.** Vergleiche nach Map→Spec→Tickets die Ausschlüsse, Negationen und nachträglichen Änderungen. Räume Restunklarheiten vor dem Abschluss auf. Anzahl geschlossener Tickets und Länge der Spec sind keine Ersatzmaße für diese Prüfung. (Eigener Transfer aus Kap. 17, 25–27)
4. **Integration und reale Bedienung separat abnehmen.** Prüfe Testsammlung und gemeinsame Umgebung, führe relevante positive und negative Szenarien aus und protokolliere verbleibende menschliche Schritte. Automatisiere wiederholte Einrichtung erst mit geklärten Rechten, benötigten Zugangsdaten und verständlichem Fehlerweg. (Eigener Transfer aus Kap. 21, 23, 27)

### Kapitelabdeckung

| Kapitel | ID | Ausgewerteter Schwerpunkt |
|---:|---|---|
| 14 | `chart-the-map` | Ziel Spec, eigene Map oder reproduzierbarer Checkpoint |
| 15 | `chart-the-map-solution` | Fragen, vier Ticket-Typen, Recherche und Herkunft |
| 16 | `grilling-ticket` | Frischer Kontext, Frage entscheiden, Abschluss prüfen |
| 17 | `grilling-ticket-solution` | Ereigniskatalog, Rollen, Glossar und Negationen |
| 18 | `grilling-ticket-2` | Rechercheabhängige Anbieterentscheidung |
| 19 | `grilling-ticket-2-solution` | Vorläufige Wahl, weiteres Experiment, Fallback |
| 20 | `task-ticket` | Menschliche Einrichtung mit interaktivem Wizard |
| 21 | `task-ticket-solution` | Zugangsdaten, abgeschnittener Schlüssel, Gegenprüfung |
| 22 | `prototype-ticket` | Vier Prüfungen, Isolation, Seed ist keine Einrichtung |
| 23 | `prototype-ticket-solution` | Integrationsversuch, Shortcuts, gesehen/gelesen |
| 24 | `finish-the-map` | Resttickets, Prototyp entfernen, Unklarheiten prüfen |
| 25 | `finish-the-map-solution` | Versionsumfang, UI-Varianten, Fidelity und Schlussprüfung |
| 26 | `spec-implement` | Map→Spec→Tickets→Implementierung |
| 27 | `spec-implement-solution` | Ticketgraph, Integration, Reviews, CLI-Fehler und QA |

Die Erkenntnisse beruhen vollständig auf dem bereitgestellten Text. Recherchen, Registrierungen, Prüfaufrufe und Browserhandlungen sind als vom Kurs beschriebene Vorgänge eingeordnet. Ihre Ergebnisse wurden hier weder unabhängig reproduziert noch als aktuelle Eigenschaften der genannten Dienste verifiziert. (Kap. 14–27)


---

## Vom passenden Workflow zum lernenden Reviewprozess

Dieser Analysebaustein behandelt die Kurskapitel 28–38 anhand der bereitgestellten HTML-Textauszüge. Er unterscheidet Aussagen und Beispiele des Autors von eigenen Ableitungen für Agentic Engineering. Videos wurden nicht angesehen. Beschriebene Agentenläufe, Screenshots und Testergebnisse sind Inhalte der Kursdarstellung; sie wurden hier nicht selbst ausgeführt oder unabhängig reproduziert.

Die Kapitel bilden einen zusammenhängenden Regelkreis: angemessenen Planungsaufwand wählen, Änderungen verständlich darstellen, automatisiert gegen Standards und Auftrag prüfen, menschliche Aufmerksamkeit nach Folgen verteilen und wiederkehrendes Feedback in das Arbeitssystem zurückführen. Das ist eine nachvollziehbare Methodik, aber kein gemessener allgemeiner Produktivitätsnachweis. Die Aussagekraft einzelner Demonstrationen bleibt auf das dargestellte Kursprojekt begrenzt. (Kapitel-IDs: `grill-vs-wayfinder-vs-ship-first`, `the-three-kinds-of-review`, `trying-out-retro-solution`.)

### Zehn konkrete Erkenntnisse

#### 1. Der Planungsaufwand richtet sich nach den Kosten eines Missverständnisses

**Autorenposition:** Winzige, schnell prüfbare und billig wiederholbare Änderungen eignen sich für One-shot: Der Agent arbeitet zuerst, danach wird abgeglichen. Bei größeren Änderungen empfiehlt der Autor zunächst `/grill-with-docs`. Wenn mehr Unklarheit auftaucht oder der Kontext in die „Dumb Zone“ gerät, lässt sich daraus eine Wayfinder-Karte entwickeln. Der volle Ablauf mit Prototypen, Recherche, Aufgaben und Spec ist für kleine Änderungen unnötig aufwendig. (Kapitel 28, `grill-vs-wayfinder-vs-ship-first`.)

**Eigener Transfer:** Die wirklich hilfreiche Größe ist der erwartete Schaden einer Fehlinterpretation. Eine kleine Farbkorrektur kann billig wiederholt werden. Eine ebenso kurze Änderung an einer Berechtigungsbedingung kann erhebliche Folgen haben. Diffgröße ist ein praktischer Hinweis, aber kein Ersatz für die Betrachtung von Wirkung und Rücknehmbarkeit. Die Eskalation sollte deshalb über tatsächlich neu entdeckte Fragen erfolgen, nicht über eine Pflicht zu immer umfangreicheren Planungsdokumenten.

#### 2. Drei Prüfarten beantworten unterschiedliche Fragen

**Autorenposition:** Automatisierte Checks sind deterministische Verfahren wie Unit-Tests, Typecheck und Linter. Automatisiertes Review lässt Agents beurteilen. Menschliches Review bringt die eigene Beurteilung hinzu. Die letzten beiden Stufen werden in diesem Kursabschnitt vertieft; die Ausarbeitung automatisierter Checks folgt später. (Kapitel 29, `the-three-kinds-of-review`.)

**Eigener Transfer:** Ein erfolgreicher Typecheck ist keine fachliche Zustimmung. Ein Reviewkommentar ist kein ausgeführter Test. Eine menschliche Freigabe ersetzt keine fehlende Laufzeitprüfung. Die drei Ergebnisse sollten getrennt sichtbar sein. Die Formulierung des Autors, Checks kosteten nur CPU-Zyklen und keine Tokens, beschreibt den direkten Checklauf: Einrichtung, Laufzeit, Wartung und die Verarbeitung seiner Ausgabe bleiben Aufwand. Viele Checks sind deshalb nicht automatisch besser; relevant ist, welche Fehlerklasse sie tatsächlich erkennen.

#### 3. Ein guter PR-Text verkürzt die Zeit bis zum richtigen Verständnis

**Autorenposition:** Das menschliche Review soll schneller und sinnvoll priorisiert werden. Aus dem `show-me`-Skill entwickelt der Autor eine `pr`-Vorlage mit kurzer visueller Zusammenfassung, Nachweisen und Merge-Gefahr. Diff-Skizzen, Dateibäume und Mermaid-Diagramme können Absicht, Zuständigkeiten oder zeitliche Abläufe erklären. Der Skill berücksichtigt auch die Domänensprache des Glossars. (Kapitel 30, `the-pr-skill`; Kapitel 31, `running-the-pr-skill`.)

**Eigener Transfer:** Ein Diagramm ist eine Behauptung über die Änderung. Es muss zum tatsächlichen Diff passen. Für eine neue Note-Funktion wäre eine kleine Darstellung des Weges von Eingabe über Validierung zur Speicherung hilfreicher als eine Liste aller bearbeiteten Dateien. Der Text sollte zuerst die Verhaltensänderung erklären. Zusätzliche Visualisierung lohnt sich, wenn sie eine konkrete Verständnisfrage beantwortet; rein dekorative Skizzen erhöhen die Reviewlast.

#### 4. Vorher und Nachher schützen vor einem irreführenden grünen Ergebnis

**Autorenposition:** Die Evidence-Sektion soll einen fehlerhaften Ausgangszustand und das erfolgreiche Ergebnis zeigen. Der Agent soll Code tatsächlich ausführen und konkrete Tests oder Konsolenausgaben vorlegen. In der PR-Übung bestehen Typecheck und vorhandene Tests, obwohl Bookmarks und Notes von keinem Test abgedeckt sind. Der Autor benennt diese Nachweise ausdrücklich als schwach. (Kapitel 30, `the-pr-skill`; Kapitel 32, `running-the-pr-skill-solution`.)

**Eigener Transfer:** Für einen Bugfix sollte derselbe relevante Fall vor der Korrektur scheitern und danach bestehen. Bei einem neuen Feature muss deutlich sein, welche vorher fehlende Fähigkeit geprüft wird. Ein Screenshot kann eine sichtbare Änderung zeigen, aber weder Persistenz noch Rechte oder Nebenläufigkeit vollständig nachweisen. Gute Evidence enthält deshalb die Frage, den ausgeführten Fall und die Grenzen des Ergebnisses. Die qualitative Screenshot-Rangfolge des Kurses ist eine Heuristik für geeignete Situationen, kein allgemeiner Maßstab für jede Änderung.

#### 5. Rücknehmbarkeit und Schadensausmaß sind zwei verschiedene Achsen

**Autorenposition:** Eine „Two-way Door“ lässt sich zurücknehmen; eine „One-way Door“ erzeugt schwer rückholbare Folgen wie Datenverlust, Kosten oder versandte E-Mails. Der Blast Radius beschreibt das mögliche Ausmaß eines Fehlers. Die Quizbeispiele priorisieren eine spaltenlöschende Migration gegenüber einer breiten Farbänderung. Wenig menschliches Vorabreview kommt laut Autor nur bei leicht rücknehmbaren Änderungen mit kleinem Blast Radius und zuvor solider Automatisierung infrage. (Kapitel 30, `the-pr-skill`.)

**Eigener Transfer:** Rücknehmbarkeit umfasst den entstandenen Zustand, nicht nur den Git-Merge. Im Kurs fügt eine Migration lediglich Tabellen hinzu; sobald Students Notes schreiben, kann ein Rückbau dennoch Daten bewahren oder löschen müssen. Diese Unterscheidung ist treffender als „Add-only ist harmlos“. Die geschätzten 95 Prozent reversibler Änderungen bei persönlicher Software bleiben eine Autorenschätzung. Wenige Nutzer allein beweisen keinen kleinen Schaden. (Kapitel 32, `running-the-pr-skill-solution`.)

#### 6. Ein frischer Reviewer hat einen anderen Auftrag als der Implementer

**Autorenposition:** Der Implementer muss erkunden, implementieren und debuggen. Ein separater Reviewer erhält einen frischen Kontext und einen bereits eingegrenzten Diff. Dadurch kann er gezielt mit Standards ausgestattet werden. Der Autor hält `CODING_STANDARDS.md` als Reviewquelle teilweise vom Implementer fern, damit dieser einen groben Entwurf produzieren kann. Das ist keine Aussage, Reviewer seien grundsätzlich intelligentere Modelle. (Kapitel 33, `the-code-review-skill`.)

**Eigener Transfer:** Diese Aufteilung kann Aufmerksamkeit bündeln, erzeugt aber Übergabeaufwand. Ein Reviewer benötigt ausreichend Umgebung, um Auswirkungen jenseits der geänderten Zeilen zu verstehen. Frischer Kontext garantiert keine unabhängige Fachbeurteilung. Kritische Domänen-, Daten- und Rechtevorgaben sollten schon im Implementierungsauftrag verfügbar sein; eine spätere kosmetische oder projektbezogene Nachprüfung kann separat geladen werden. Die Verteilung von Regeln ist eine Entwurfsentscheidung, kein allgemeines Argument dafür, wesentliche Anforderungen erst nachträglich offenzulegen.

#### 7. Standards und Spec liefern zwei eigenständige Reviewachsen

**Autorenposition:** Die Übung prüft sowohl dokumentierte Regeln als auch eine schriftliche Spec. Im Lösungsdurchlauf wird zunächst der Bezugspunkt des PRs bestimmt; dann laufen Standards- und Spec-Review getrennt. Gefunden werden unter anderem eine zurückgegebene statt geworfene Response, falsche Domänenbegriffe und widersprüchliche Kommentare. Die Spec-Prüfung findet fehlende Änderungszeit, falsche Position des Notizfelds, ein zusätzliches Instructor-Feature, die Grenze 5000 statt 2000 und fehlende Inhaltszugriffsprüfungen. (Kapitel 34, `testing-out-the-code-review-skill`; Kapitel 35, `testing-out-the-code-review-skill-solution`.)

**Eigener Transfer:** Die beiden Achsen verhindern unterschiedliche Fehler. Sauberer Code kann den Auftrag verfehlen; auftragsgetreuer Code kann Projektregeln verletzen. Einen Reviewauftrag würde ich an einen eindeutigen Ausgangsstand und eine konkrete Spec-Version binden. Ein beweglicher Branchname allein kann bei paralleler Arbeit den Vergleich verändern. Automatische Befunde bleiben zu prüfen: Ein Standard ist kontextgebunden, und eine widersprüchliche Spec wird durch genaue Einhaltung nicht sinnvoll.

#### 8. Automatisiertes Review soll eindeutige Arbeit erledigen und Entscheidungen sichtbar lassen

**Autorenposition:** Die zusätzliche Aufforderung „fix what you find“ soll verhindern, dass automatisiertes Review lediglich Kommentararbeit auf Menschen ablädt. Im Lösungsdurchlauf werden Module und Tests ergänzt, die PR-Beschreibung nachgezogen und Ermessensfragen besprochen. Bei den Foreign Keys bleibt nach dem Gespräch der vorhandene Zustand bestehen. (Kapitel 34, `testing-out-the-code-review-skill`; Kapitel 35, `testing-out-the-code-review-skill-solution`.)

**Eigener Transfer:** Ein Reviewbericht und die anschließende Änderung sind zwei verschiedene Arbeitsstände. Eindeutige, beauftragte Korrekturen können automatisiert werden; offene Fachentscheidungen brauchen eine Klärung. Nach relevanten Fixes sind passende Checks für den neuen Stand nötig. In Kapitel 38 lehnt der Autor den Retro-Vorschlag eines zusätzlichen Standards-Reviews als für ihn zu aufwendig ab. Das ist seine Abwägung, keine allgemeine Befreiung von erneuter Verifikation. Ebenso ergibt sich aus seiner filmischen Abkürzung, kein Folge-Issue anzulegen, keine Empfehlung, offene Arbeit dauerhaft unregistriert zu lassen. (`trying-out-retro-solution`, `testing-out-the-code-review-skill-solution`.)

#### 9. Wiederkehrendes Feedback gehört in Regeln und in die vorgelebten Beispiele

**Autorenposition:** Menschliches Review soll das System verbessern, das den Code erzeugt. Derselbe sinnvolle Kommentar sollte nicht ständig wiederholt werden müssen. Retro betrachtet Sitzungen und später auch ausdrücklich angeforderte PR-Kommentare. Die Übung sucht verallgemeinerbare Regeln. In der Lösung fehlen dokumentierte Vorlieben, während bestehende Module die unerwünschten Bannerkommentare vorleben. Deshalb werden Standards und Beispiele gemeinsam geändert. (Kapitel 36, `why-retro`; Kapitel 37, `trying-out-retro`; Kapitel 38, `trying-out-retro-solution`.)

**Eigener Transfer:** Eine nützliche Regel benennt Situation, erwartetes Verhalten und prüfbares Gegenbeispiel. Nicht jeder Einzelfehler verdient eine dauerhafte Regel. Die Übungsanweisung, stark implementierungsbezogene Kommentare zu löschen, gilt dem Lernziel dieser Übung; in einem echten Review darf eine konkrete Fehlerbeschreibung nötig bleiben. „Nie denselben Kommentar zweimal“ ist eine Zielrichtung für Prozesslernen, keine Garantie des Agentenverhaltens.

#### 10. Retro-Vorschläge brauchen Auswahl und einen überprüfbaren Effekt

**Autorenposition:** Retro kann viele Tokens verbrauchen und Befunde überzeichnen. Der Autor warnt vor selbstverstärkenden Verbesserungsschleifen und lässt nicht alle Änderungen automatisch anwenden. Er wählt dokumentierte Kommentar- und Testsetup-Regeln, gemeinsame Testdatenbanktypen und Branded Types aus. Letztere unterscheiden Markdown und PlainText. Die Testvorbereitung soll über Modulfunktionen laufen. (Kapitel 38, `trying-out-retro-solution`.)

**Eigener Transfer:** Diese Entscheidungen benötigen Gegenbedingungen. Modulfunktionen reduzieren Kopplung an die Datenbank, können aber zusätzliche öffentliche Funktionen oder gemeinsame Fehler in Vorbereitung und Test erzeugen. Ein Branded Type markiert eine technische Bedeutung; die dargestellten Type Assertions prüfen oder bereinigen keinen Inhalt zur Laufzeit. Die Kommentar- und ADR-Präferenz ist eine Autorenposition, keine allgemeine Regel gegen hilfreiches Schnittstellenwissen. Für Retro lohnt sich eine begrenzte Auswahl wiederkehrender Probleme. Nach einer Änderung muss ein späterer Lauf zeigen, ob der konkrete Fehler seltener entsteht, ohne einen größeren neuen Aufwand einzuführen.

### Vier Handlungsempfehlungen als eigener Transfer

1. **Eine kurze Aufgabenweiche verwenden:** Prüfbarkeit, Wiederholungskosten und Folgen erfassen. Kleine, günstige Änderungen direkt ausprobieren; bei größeren offenen Fragen erst klären und bei Bedarf zu Wayfinder eskalieren. Den Umfang nicht allein an der Zeilenzahl festmachen. (Kapitel 28, `grill-vs-wayfinder-vs-ship-first`.)
2. **PRs mit einer nachvollziehbaren Prüffrage abnehmen:** Verhaltensänderung, konkrete Ausführung, Vorher/Nachher und offene Grenzen getrennt nennen. Rücknehmbarkeit und Blast Radius zusätzlich beurteilen. Bei ungetesteten Features den grünen Gesamtlauf nicht als Feature-Nachweis zählen. (Kapitel 30–32, `the-pr-skill`, `running-the-pr-skill`, `running-the-pr-skill-solution`.)
3. **Review und Fix in begrenzte Schritte gliedern:** Ausgangsstand, Standards und Spec benennen. Eindeutige Korrekturen beauftragen, fachliche Fragen eskalieren und den geänderten Stand angemessen prüfen. Prüftiefe nach Folgen statt nach einem festen Zeremoniell wählen. (Kapitel 33–35, `the-code-review-skill`, `testing-out-the-code-review-skill`, `testing-out-the-code-review-skill-solution`.)
4. **Eine Retro-Änderung am Wiederholungsfall überprüfen:** Wenige tatsächlich wiederkehrende Befunde auswählen, Regel und kopierte Beispiele gemeinsam verbessern und später denselben Fehlertyp erneut untersuchen. Große Transkriptmengen bei Bedarf aufteilen, den Nutzen aber gegen Token- und Konsolidierungsaufwand rechnen. (Kapitel 36–38, `why-retro`, `trying-out-retro`, `trying-out-retro-solution`.)

### Kapitelabdeckung und Interpretationsgrenzen

| Kapitel | Kapitel-ID | Verarbeiteter Schwerpunkt |
|---|---|---|
| 28 | `grill-vs-wayfinder-vs-ship-first` | One-shot, Grill with Docs und Eskalation zu Wayfinder |
| 29 | `the-three-kinds-of-review` | Deterministische Checks, Agentenreview und menschliches Review |
| 30 | `the-pr-skill` | Geschwindigkeit, Evidence, Türmodell, Blast Radius und Quiz |
| 31 | `running-the-pr-skill` | Draft-PR, Beschreibung erzeugen, kritisch lesen und anpassen |
| 32 | `running-the-pr-skill-solution` | Schwache Feature-Nachweise, Privacy-Widerspruch und Rücknahme neuer Daten |
| 33 | `the-code-review-skill` | Frischer Reviewkontext, Standardquellen und Rollenverteilung |
| 34 | `testing-out-the-code-review-skill` | Zwei Reviewachsen und beauftragte Korrekturen |
| 35 | `testing-out-the-code-review-skill-solution` | Konkrete Standard-/Spec-Verstöße, Fixes, Entscheidungen und aktualisierter PR |
| 36 | `why-retro` | Wiederkehrendes Feedback in das Arbeitssystem zurückführen |
| 37 | `trying-out-retro` | Prozessorientierte Kommentare und Retro über zugehörige Sitzungen |
| 38 | `trying-out-retro-solution` | Vorschläge auswählen, widersprüchliche Beispiele bereinigen, Regeln und Typen verbessern |

Die Übersetzung bewahrt auch überzogene Originalformulierungen und alle Quizalternativen. Die Analyse macht daraus keine Autorisierung, PRs zu erstellen, Daten zu verändern, Kommentare zu löschen, Skills anzuwenden oder Regeln ungeprüft zu übernehmen. Der HTML-Text beschreibt Demonstrationen. Weder die in Alttexten genannten Bilder noch die Videos wurden hier als eigene visuelle Beobachtung gewertet.


## Abgleich mit dem lokalen Skill-Checkout

Referenz ist ausschließlich der vorhandene Checkout von mattpocock/skills bei Commit 59db609eb1e18aaf59b63284d0e52255aff0c63c; er wurde für diese Analyse nicht aktualisiert. Statisch geprüft wurden ADR-FORMAT.md unter domain-modeling sowie die SKILL.md-Dateien von wayfinder, code-review und retro. Die drei ADR-Kriterien, Decision Tickets mit Frontier, zwei Reviewachsen und die Retro-Kategorien sind dort dokumentiert. Diese Sichtung bestätigt die beschriebenen Regeln, keine ausgeführte Factory und keine gemessene Produktivitätswirkung.

Der Checkout ist weiterentwickelt: Wayfinder beschreibt trackerabhängige Operationen und einen lokalen Markdown-Fallback. Retro verlangt für mechanische Verstöße deterministische Checks, während die historische Demo teilweise Coding Standards ergänzt. Konkrete Kurskommandos, Providerfunktionen und Preise sind daher Momentaufnahmen. Vor tatsächlicher heutiger Nutzung sind passende Versionen und aktuelle Primärdokumentation gesondert zu prüfen.

## Einarbeitung ins Knowledge-System

Eine kompakte [Source-Notiz](../80_Knowledge/Sources/2026-10-29-matt-pocock-software-factories-real-engineers.md) verweist auf die vollständige lokale Rohquelle. Nach deren Vervollständigung hat die Quellen-Pipeline den Status verarbeitet und drei neue Belege in CONTEXT-Glossar, Plan-first-mit-getrenntem-Review und Qualitaetsaufwand-nach-Folgen-und-Abhaengigkeiten-staffeln übernommen.

Drei neue Patterns halten eigenständige Methoden fest: [sparsame ADRs](../80_Knowledge/Patterns/ADRs-auf-tragende-Entscheidungen-begrenzen.md), [Wayfinder als Entscheidungskarte](../80_Knowledge/Patterns/Wayfinder-als-Karte-offener-Entscheidungen.md) und [Review-Findings als Verbesserungsinput](../80_Knowledge/Patterns/Review-Findings-in-Agent-Verbesserungen-ueberfuehren.md). Verifiziert bezeichnet hier die statische Prüfung der Methode im vorhandenen Referenz-Repo; die Wirksamkeit wurde nicht experimentell gemessen. Die Kursdemo und Pococks Skills zählen als eine Herkunftsfamilie.

Der [Kurstransfer](../80_Knowledge/Vergleiche/Matt-Pocock-Software-Factories-Kurstransfer.md) verbindet die Erkenntnisse mit Ousterhout, Evans, Osmani und Thomas/Hunt. Der bestehende Vergleich Factory-Spec-Build-Review erhält einen datierten Zusatz außerhalb der unveränderten Pilot-Registry. Produktive Skills und Workflows wurden nicht geändert.

Source und neue Patterns sind bestehenden Themenclustern zugeordnet; Keywords und Pattern-Synonyme wurden nachgeschärft. Für das ADR-Pattern bleibt das automatische Scoring unter der Schwelle. Die eindeutige inhaltliche Zuordnung erfolgt manuell unter planung mit agent-dateien; die mögliche Keyword-Lücke ist in Fragen_an_Philipp für spätere Taxonomiepflege festgehalten. Die Taxonomie wurde nicht erweitert.

## Prüfstand und Grenzen

- Alle 39 Eingangskopien stimmen in Größe und SHA-256 mit den Originalen überein. Alle 156 referenzierten Bilder sind lokal vorhanden; jedes Kapitel hat den korrekt nummerierten lokalen Videolink.
- Sämtliche 2.932 Übersetzungs-IDs sind abgedeckt. Ankerreihenfolge, Quizantwortschlüssel und Task-IDs entsprechen dem Original. Inline-Code bleibt unverändert; natürliche Prosa in Beispielblöcken ist übersetzt. Die deutschen JavaScript-Anpassungen bestehen die Syntaxprüfung.
- Desktop- und Mobilansicht wurden mit Playwright geprüft. Suche, Bilddialog, richtige Quizantwort einschließlich Erklärung, Aufgabenhaken und Wiederherstellung nach Navigation funktionieren. Auf schmaler Ansicht tritt nach den gezielten Layoutkorrekturen kein horizontaler Seitenüberlauf auf. Der In-App-Browser ließ sich nicht verbinden; die Prüfung erfolgte mit dem verfügbaren Browser-Fallback.
- Quellen-Pipeline und Themenprüfung sind konsistent. Der Knowledge-Validator meldet dieselben 53 vorbestehenden Fehler mit exakt unverändertem Fehlertext; es gibt keine neuen Fehler. Dieser Bestand ist damit ausdrücklich nicht insgesamt fehlerfrei.
- 67 Blogtests und die Blogprüfung bestehen; die gemeinsame Git-Sicherung umfasst auch die vorangegangene Buchauswertung und zwölf freigegebene Artikel. Fremde vorbestehende Änderungen bleiben getrennt. Die Themenansichten für den Commit werden ohne die uncommittete fremde Source erzeugt.

Das öffentliche Repository enthält die eigene Analyse, Quellenaufbereitung, Belege, Themenzuordnung und das Inventar. Originalkurs, vollständige Übersetzung, Rohtext und Videos bleiben gemäß bestehender Volltext-Ablageregel lokal ignoriert. Die Videos wurden nicht hochgeladen. Quellen-Pipeline und Prüfprotokolle sowie die manuellen Übersetzungsobjekte liegen zusätzlich unter .wissen/analysen/matt-pocock-kurs-2026-10-29.
