# Vergleich: Softwaregrundlagen für Agentic Engineering

**Stand:** 2026-10-29

Diese Synthese verbindet vier vollständig ausgewertete Buchdateien mit dem bestehenden AI-Company-OS. Ihr praktischer Nutzen liegt darin, Agentenarbeit fachlich abzugrenzen, verständliche Software zu entwerfen und Ergebnisse an belastbaren Kriterien zu prüfen. Die Bücher liefern dafür unterschiedliche Perspektiven. Sie ergeben kein einheitliches Verfahren, das ohne Abwägung auf jedes Projekt passt.

Ousterhout untersucht die Komplexität von Entwürfen, Evans die Verbindung von Fachwissen und Softwaremodell, Hunt und Thomas die tägliche Entwicklungspraxis und Osmani die Arbeitsteilung zwischen Menschen und generativer KI. Gemeinsam verschieben sie den Maßstab von erzeugtem Code zu verstandenen Problemen, begrenzten Abhängigkeiten und überprüfbarem Verhalten. Die Übertragung der älteren Bücher auf heutige Coding Agents ist unsere redaktionelle Ableitung; sie haben keine aktuellen Modelle evaluiert.

## Lesepfade und Quellen

| Buch | Beitrag zu Agentic Engineering | Ausführliche Analyse | Source-Notiz |
|---|---|---|---|
| John Ousterhout: A Philosophy of Software Design, 2nd Edition | Komplexität, Information Hiding, Deep Modules, Schnittstellen, Kommentare und Entwurfsalternativen | [Ousterhout](../../reports/buecher/2026-10-29-ousterhout.md) | [[2021-07-01-pdf-a-philosophy-of-software-design-2nd-edition]] |
| Eric Evans: Domain-Driven Design | Gemeinsame Modellbildung, fachliche Grenzen, Invarianten und strategische Priorisierung | [Evans](../../reports/buecher/2026-10-29-evans.md) | [[2003-08-01-pdf-domain-driven-design]] |
| Addy Osmani: Beyond Vibe Coding | Bewusster KI-Einsatz, Kontext, Prototypen, Verifikation und menschlicher Reviewdurchsatz | [Osmani](../../reports/buecher/2026-10-29-osmani.md) | [[2025-08-18-pdf-beyond-vibe-coding]] |
| David Thomas und Andrew Hunt: The Pragmatic Programmer, 20th Anniversary Edition | Verantwortung, Änderbarkeit, Tracer Bullets, Verträge, Tests, Ressourcen und Zusammenarbeit | [Hunt und Thomas](../../reports/buecher/2026-10-29-pragmatic.md) | [[2019-09-13-pdf-the-pragmatic-programmer-20th-anniversary-edition]] |

Die Seitenangaben in dieser Synthese beziehen sich auf die bereitgestellten **PDF-Dateien**, nicht auf gedruckte Buchseiten. Das ist bei Evans besonders wichtig: Seine Datei hat 324 PDF-Seiten und beginnt nach dem Cover unmittelbar mit Kapitel 1. Der [Lese- und Prüfnachweis](../../reports/buecher/2026-10-29-lese-und-pruefnachweis.md) dokumentiert Umfang, Dateihashes, Bildprüfungen und Grenzen. Die Rohvolltexte und Originalabbildungen bleiben im lokalen Quellenarchiv.

Die [Gesamtauswertung vom 28.10.2026](../../reports/2026-10-28-gesamtes-wissen-ai-company-os.md) beschreibt den vorherigen Bestand. Diese Buchauswertung ergänzt ihn; sie behauptet keine erneute Prüfung aller externen Repositories und keine Umsetzung der hier entworfenen Verfahren in Produktprojekten.

## 1. Welche Arbeit der Mensch weiterhin verantwortet

Die Bücher teilen eine Grundidee: Das Schreiben einer plausiblen Lösung ist nur ein Teil des Engineering. Zuerst müssen Problem, erwünschtes Ergebnis, Randbedingungen und Folgen verstanden werden. Evans zeigt, dass diese Arbeit nicht durch das einmalige Einsammeln vermeintlich fertiger Anforderungen erledigt ist. Modell und Implementierung verändern sich im Gespräch mit Fachleuten und durch konkrete Beispiele. Hunt und Thomas behandeln Anforderungen ebenfalls als Gegenstand gemeinsamer Entdeckung. Osmani beschreibt die zusätzliche Versuchung, generierten Code wegen seiner überzeugenden Form schon für eine gelöste Aufgabe zu halten.

Für das AI-Company-OS folgt daraus eine klare Unterscheidung. Ein Agent kann einen Vorschlag für eine Fachregel liefern, ihre Konsistenz untersuchen und Tests formulieren. Die fachliche Gültigkeit braucht jedoch einen Ursprung außerhalb derselben Generierung: etwa eine ausdrücklich bestätigte Anforderung, eine vorhandene maßgebliche Regel oder ein fachlich geprüftes Gegenbeispiel. Wenn Implementierung, Test, Dokumentation und Review alle denselben ungeprüften Ausgangssatz übernehmen, erhöht ihre Übereinstimmung die fachliche Sicherheit kaum. Osmani beschreibt dieses Problem als zusammenhängende falsche Stimmigkeit über mehrere Artefakte hinweg (PDF-S. 213–214).

Das ergänzt [[Intent-Engineering-als-dritte-Schicht]], [[Fable-Unknowns-vor-Prompt-Qualitaet]] und [[Domaenen-Harness-mit-Daten-Evals-Rechten-und-Review]]. Die neue Konsequenz lautet: Nicht nur das Ziel aufschreiben, sondern auch festhalten, **wer oder was seine Bedeutung bestätigt**. Die gleiche Unterscheidung gilt für Rechte. Eine überzeugende Empfehlung in einem Buch oder ein bestandenes lokales Experiment erteilt keine Freigabe für externe Kommunikation, Produktivänderungen oder die Änderung geschützter Daten.

## 2. Drei verschiedene Grenzen statt einer universellen Architektur

Eine der nützlichsten Verbindungen zwischen den Büchern entsteht durch die Trennung von Informations-, Bedeutungs- und Konsistenzgrenzen.

| Grenze | Leitfrage | Typische Fehlentscheidung | Geeigneter Nachweis |
|---|---|---|---|
| Modulgrenze nach Ousterhout | Welches schwierige Wissen muss ein Aufrufer nicht kennen? | Eine lange Methode wird in viele Durchreichungen zerlegt; alle müssen dieselben Details kennen. | Öffentliche Schnittstelle, notwendiges Aufruferwissen und betroffene Stellen bei einer konkreten Änderung vergleichen. |
| Bounded Context nach Evans | In welchem Bereich hat ein Modellbegriff eine konsistente Bedeutung? | Ein globales Datenmodell zwingt unterschiedliche fachliche Bedeutungen zusammen. | Kontextkarte, Begriffsdefinitionen, Besitzer und konkrete Übersetzungsbeispiele. |
| Aggregate nach Evans | Welche fachlichen Bedingungen müssen bei einer Änderung zusammen konsistent bleiben? | Ein gesamter Objektgraph wird als Transaktionsgrenze geladen oder jeder Datensatz isoliert geändert. | Invarianten, erlaubte Operationen und konkurrierende Änderungsfälle. |

Diese Grenzen können zusammenfallen, müssen es aber nicht. Ein Bounded Context kann viele Module und Aggregate enthalten. Er ist weder automatisch ein Microservice noch ein Mandant. Ein Aggregate ist weder automatisch eine Datenbanktabelle noch eine frei wählbare Baumstruktur. Ein Deep Module ist nicht deshalb gut, weil seine Datei lang ist: Seine Schnittstelle muss im Verhältnis zum verborgenen Verhalten einfach sein.

Für die Delegation an Coding Agents ist diese Unterscheidung unmittelbar hilfreich. Ein Auftrag kann auf ein Modul begrenzt sein, obwohl fachlich ein benachbarter Context betroffen ist. Zwei Agents können verschiedene Dateien bearbeiten und trotzdem dieselbe Invariante verletzen. Ein getrenntes Worktree isoliert lokale Dateiedits; es isoliert nicht automatisch Schemaänderungen, Datenbanken, Ports, Testkonten oder Bedeutung. Deshalb ergänzt eine fachliche Abhängigkeitskarte die Dateiliste, statt durch sie ersetzt zu werden.

Neue Einstiege dafür sind [[Information-Hiding-an-Aenderungsgruenden-ausrichten]], [[Bounded-Contexts-und-Uebersetzungsgrenzen-kartieren]] und [[Aggregate-durch-fachliche-Invarianten-begrenzen]]. Sie vertiefen [[Abstraktionswert-mit-Deletion-Test-pruefen]] und [[Kontrollierte-Agent-Parallelisierung]].

## 3. Gemeinsame Sprache wird erst durch Verhalten belastbar

Ein Glossar ist ein guter Einstieg, aber noch keine Ubiquitous Language im Sinne von Evans. Das gemeinsame Modell muss auch Beziehungen, Zustandswechsel, Operationen und Randbedingungen tragen. Die Sprache soll im fachlichen Gespräch, in Beispielen, im Code und in den Tests verwendbar sein. Wenn Fachleute einen Sachverhalt nur mit langen Ausnahmen und technischen Übersetzungen erklären können, ist das ein Anlass, das Modell selbst zu hinterfragen.

Für einen Agentenauftrag reicht deshalb die Definition „Reservierung = vorübergehende Vormerkung“ nicht. Es muss etwa geklärt werden, ob eine Reservierung Kapazität sofort bindet, wann sie abläuft, was Bestätigung bedeutet und ob ein abgelaufener Vorgang noch bestätigt werden darf. Solche Fragen lassen sich nicht durch konsequentes Umbenennen einer Klasse beantworten. Ein Begriff kann sprachlich vereinheitlicht sein und trotzdem widersprüchliche Regeln verdecken.

Ebenso falsch wäre es, alle Unternehmensbereiche auf ein universelles Wortverständnis zu verpflichten. Eine Reservierung im Vertrieb kann ein anderes Modell haben als die technische Sperre im Kapazitätsdienst. Die Kontextkarte macht diese Unterschiede sichtbar. Eine Übersetzung muss Bedeutung vermitteln: Ein fremdes Feld `confirmed` einfach in das eigene `confirmed` umzubenennen hilft nicht, wenn beide Seiten unterschiedliche fachliche Zusagen meinen.

Die bestehende [[CONTEXT-Glossar|Glossar-Arbeitsweise]] erhält damit eine wichtige Ergänzung: Begriffe mit Beispielen und Gegenbeispielen prüfen und bei Modelländerungen ihre Verwendung in Implementierung und Akzeptanzfällen nachführen. Ein neues Glossar ist kein Ersatz für die fachliche Klärung; ein zentraler Begriff darf außerdem innerhalb klar benannter Contexts unterschiedliche Bedeutungen haben.

## 4. Änderbarkeit konkret prüfen

Ousterhouts Komplexitätsbegriff ist an die Arbeit gebunden, die ein Entwickler erledigen muss. Änderungsausbreitung, kognitive Belastung und unbekannte betroffene Stellen sind nützlicher als eine pauschale Obergrenze für Zeilen oder Methoden. Hunt und Thomas fassen die Entwurfsbewertung mit dem Wert zusammen, spätere Änderungen leichter zu machen. Beide Perspektiven helfen, die typische Agentenreflexhandlung zu korrigieren: mehr Dateien, mehr Helfer und mehr Schichten als vermeintlichen Qualitätsnachweis zu erzeugen.

Eine konkrete Entwurfsprüfung beginnt mit einer realistischen Änderung. Beispielsweise soll die Darstellung einer Kapazitätsquelle wechseln, während die Reservierungsregeln gleich bleiben. Müssen Aufrufer dafür neue Speicherformate kennen? Müssen alle dieselbe Fehlerbehandlung nachbauen? Wird eine fachliche Zusage an mehreren Stellen manuell synchronisiert? Solche Antworten zeigen, welches Wissen die Schnittstelle durchlässt.

DRY ergänzt diese Prüfung um die Frage, ob tatsächlich **dieselbe fachliche Aussage** mehrfach repräsentiert wird. Zwei derzeit gleich aussehende Berechnungen müssen nicht dieselbe Regel sein. Die Altersgrenze eines Angebots und die Anzahl zulässiger Wiederholungen können zufällig denselben Vergleich enthalten und unabhängig geändert werden. Umgekehrt kann dieselbe Regel in völlig verschiedenem Code dupliziert sein. Eine zentrale Schemaquelle mit generierten Darstellungen kann Wissensduplikation reduzieren; eine gemeinsam benutzte generische Funktion kann unabhängige Regeln unerwünscht verkoppeln.

Auch die Empfehlung zur Zukunftssicherheit braucht ein Maß. Ousterhout verlangt strategischen Entwurf und passende Generalität; Hunt und Thomas warnen davor, über die Reichweite des verfügbaren Feedbacks hinaus zu planen (Pragmatic PDF-S. 222–225). Diese Positionen lassen sich verbinden, solange man eine aktuelle Variante als Prüfstein nutzt: heutige Fälle einfach unterstützen, teure Kenntnis verbergen, Austausch ermöglichen und spekulative Erweiterungspunkte vermeiden. Ein Framework für fünf unbekannte Produktlinien lässt sich daraus nicht ableiten.

## 5. Den richtigen ersten ausführbaren Schritt wählen

Die Begriffe Prototyp und Tracer Bullet verdienen vor Beginn eine ausdrückliche Entscheidung.

| Vorgehen | Zweck | Erwarteter Qualitätsumfang | Was bleibt? |
|---|---|---|---|
| Lernprototyp nach Hunt und Thomas | Eine begrenzte Unsicherheit untersuchen, beispielsweise Bedienbarkeit oder Machbarkeit. | Nur das für die Lernfrage Nötige; ausgelassene Robustheit und Vollständigkeit sind sichtbar. | Erkenntnis und gegebenenfalls Spezifikationsmaterial; der Versuchscode wird verworfen. |
| Tracer Bullet nach Hunt und Thomas | Einen schmalen Weg durch den tatsächlichen technischen Gesamtpfad zum Laufen bringen. | Angemessene Struktur, Fehlerbehandlung und Prüfungen trotz geringer Funktionsbreite. | Ein weiterentwickelbares Integrationsgerüst. |
| Iterativ gehärteter Prototyp bei Osmani | Einen schnellen Ausgangspunkt ausdrücklich in einen belastbaren Entwicklungsmodus überführen. | Fehlende Qualitätsaspekte werden inventarisiert, geprüft und gezielt nachgezogen. | Je nach Zustand Neubau anhand der Erkenntnisse oder schrittweise überarbeiteter Code. |
| Einfacher regelkonformer Ersatz bei Evans | Eine benötigte Integration ermöglichen, während eine bessere Fachimplementierung entsteht. | Gemeinsame Schnittstelle und fachliche Assertions; Leistungs- und Lösungsgrenzen bleiben sichtbar. | Der Vertrag bleibt; die einfache Implementierung kann gezielt ersetzt werden. |

Die Unterschiede sind materiell: Hunt und Thomas reservieren den Prototypbegriff für das Wegwerfen, Osmani erlaubt daneben die schrittweise Überarbeitung (Pragmatic PDF-S. 109–123; Osmani PDF-S. 129–132). Ein Team muss deshalb seine Erwartung benennen. Ein Screenshot, der fertige Bedienbarkeit suggeriert, sagt nichts darüber, ob Fachregeln, Datenhaltung, Fehlerpfade oder Berechtigungen vorhanden sind.

Evans' Warehouse Packer ergänzt einen anderen Fall: Ein einfacher Algorithmus erfüllt bereits denselben fachlichen Vertrag und ermöglicht die Zusammenarbeit, findet aber nicht jede mögliche Packlösung und ist kein vollständiger Optimierer. Ein fehlgeschlagener Versuch beweist dort keine Unlösbarkeit; bereits erfolgte Zustandsänderungen und Rollback werden gesondert behandelt (PDF-S. 142–146). Diese Art Ersatz ist weder ein bloßer UI-Mock noch schon wegen des Wortes Prototyp pauschal zum Wegwerfen bestimmt.

Unser Anwendungsvorschlag ist [[Tracer-Bullet-und-Lernprototyp-bewusst-waehlen]]: Lernfrage, spätere Verwendung und ausgelassene Qualitätsmerkmale in den Auftrag schreiben. Wenn die Funktion weiterleben soll, einen schmalen realen Durchstich mit Abnahme wählen. Wenn nur eine UX-Hypothese geprüft wird, den Versuchsstatus sichtbar halten. Die bestehende [[Lovable-Prototyp-dann-lokaler-Handoff|Prototyp-Handoff-Arbeitsweise]] bekommt damit ein konkreteres Übergabekriterium.

## 6. Ein eigener Beispielfall: Kapazität reservieren

Das folgende Beispiel ist unser Entwurf zur Anwendung der Bücher, kein nachgebautes Buchbeispiel und keine vorhandene Produktfunktion. Ein Team möchte per Agent die Reservierung begrenzter Plätze ergänzen.

Zunächst werden Regeln mit dem fachlich Verantwortlichen geklärt. Eine mögliche bestätigte Fassung lautet: Eine aktive Reservierung bindet Plätze bis zu ihrem Ablauf. Die Summe aktiver Reservierungen und bestätigter Buchungen darf die verfügbare Kapazität nicht überschreiten. Eine bereits bestätigte Reservierung darf bei wiederholtem identischem Auftrag nicht ein zweites Mal Kapazität verbrauchen. Welche Vorgänge als aktiv gelten und welche Uhr maßgeblich ist, gehört ausdrücklich zur Definition.

Nun werden die drei Grenzen separat entworfen. Das Buchungsmodell definiert die fachliche Bedeutung der Reservierung. Ein fremdes Verkaufssystem bekommt eine Übersetzungsgrenze, wenn seine Statuswerte anders gemeint sind. Die Konsistenzgrenze umfasst diejenigen Änderungen, die gemeinsam die Kapazitätsinvariante schützen müssen. Die technische Umsetzung kann später etwa mit einer geeigneten Transaktion, Versionsprüfung oder atomaren Bedingung arbeiten; die Bücher entscheiden diese konkrete Datenbankfrage nicht für uns.

Die öffentliche Operation soll die Fachabsicht ausdrücken. Ein Aufrufer sollte weder interne Sperren noch Tabellenfolgen kennen müssen. Der Vertrag beschreibt die zulässige Menge, mögliche Ergebnisse und das Verhalten bei einem wiederholten Auftrag. Eine normale Ablehnung wegen fehlender Kapazität ist ein erwartetes fachliches Ergebnis. Ein intern unmöglicher Zustand ist etwas anderes und darf nicht als vermeintlicher Erfolg verborgen werden.

Die erste ausführbare Lieferung ist ein Tracer Bullet: ein kleiner realer Ablauf durch Eingang, Regelentscheidung und Persistenz. Eine tatsächliche E-Mail oder Zahlung gehört nur dazu, wenn sie ausdrücklich Teil des autorisierten Tests ist. Für die lokale Integrationsprüfung kann ihre beabsichtigte Auslösung beobachtbar ersetzt werden. Die Wahl einer späteren Technik wie Outbox oder Idempotenzspeicher wäre eine zusätzliche Entwurfsentscheidung aus dem heutigen Projektkontext; sie steht nicht schon deshalb in Evans' Buch, weil dessen Regeln dazu passen.

Die Abnahme benötigt mehrere voneinander verschiedene Fragen. Wird eine normale Reservierung angenommen? Bleibt bei Ablehnung der Zustand unverändert? Können zwei konkurrierende Vorgänge dieselbe letzte Kapazität verbrauchen? Erzeugt eine Wiederholung einen zweiten Effekt? Was geschieht, wenn ein fachlich erforderlicher Zielzustand oder Datensatz fehlt? Der letzte Punkt ist entscheidend: Dass ein Codeblock eine Transaktion benutzt und keine Exception meldet, beweist noch keine korrekte Fachoperation. Ein Null-Update kann technisch erfolgreich durchlaufen und fachlich scheitern.

Die Implementierung darf die Erwartungswerte dieser Tests nicht aus ihrer eigenen Berechnung ableiten. Fachbeispiele werden vorab bestätigt, der Test überprüft Zustand und sichtbare Wirkung. Zusätzlich kann eine Property prüfen, dass kein erlaubter Operationsablauf die bestätigte Kapazitätsgrenze überschreitet. Auch diese Property ist nur so sinnvoll wie das zugrunde gelegte Modell. Damit verbinden sich Evans' Invarianten, Verträge aus Pragmatic, Ousterhouts Informationsgrenzen und Osmanis Verifikationsproblem.

## 7. Verträge ergänzen Beispiele und Tests

Ein Vertrag beantwortet drei verschiedene Fragen: Was schuldet der Aufrufer vor der Operation? Was garantiert die Operation bei ihrem beschriebenen Ergebnis? Welche Eigenschaft muss an den vereinbarten Beobachtungsgrenzen erhalten bleiben? Eine Invariante muss nicht nach jeder internen Zuweisung gelten. Sie darf während einer gekapselten Änderung vorübergehend verletzt sein, solange kein unzulässiger Zustand sichtbar wird und die festgelegte Grenze wieder konsistent verlassen wird.

Das ist keine Aufforderung, Benutzereingaben mit Laufzeit-assert-Anweisungen zu validieren. Erwartbare ungültige Eingaben brauchen einen fachlichen oder technischen Fehlerpfad. Technische assert-Anweisungen prüfen intern als wahr angenommene Bedingungen; sie können abhängig von Sprache und Laufzeit deaktiviert sein und beweisen weder Vollständigkeit noch Terminierung. Evans' Assertions sind zunächst fachliche Zustandszusagen und Verträge, unabhängig von einer bestimmten Laufzeitanweisung. Externe Wirkungen und Wiederholungen brauchen zusätzliche Regeln. [[Vertraege-mit-Vorbedingungen-Nachbedingungen-und-Invarianten]] dokumentiert diese Unterschiede.

Beispieltests, Property-Based Tests, Integrationstests und Laufzeitbeobachtung haben unterschiedliche Aufgaben. Ein Beispiel zeigt eine konkrete fachliche Entscheidung. Eine Property untersucht eine allgemein formulierte Eigenschaft für viele Eingaben. Eine Integrationsprüfung kann sichtbar machen, dass Treiber, Schema und Fehlerbehandlung wirklich zusammenpassen. Ein Laufzeitcheck kann eine falsche Annahme über tatsächliche Daten oder Umgebung aufdecken. Kein grüner Einzeltest ersetzt die anderen Nachweise unabhängig von Risiko und Aufgabe.

Hunt und Thomas empfehlen zudem, gefundene Fehler in reproduzierbare Tests zu überführen und die Aussagekraft einer Testsuite mit kontrollierten Fehlern zu prüfen. Das ergänzt [[Mutationstests-fuer-Agent-geschriebene-Tests]] und [[Testharness-als-staerkster-Hebel]]. Ob dafür ein neues Werkzeug nötig ist, muss im Projekt entschieden werden; aus dem Buch folgt keine Installationspflicht.

## 8. Widersprüche als Entscheidungen nutzbar machen

| Spannung | Positionen | Entscheidungsvorschlag für unsere Arbeit |
|---|---|---|
| TDD als Entwurfsmotor | Ousterhout kritisiert featuregetriebenes Test-First als übergeordnetes Designverfahren, unterstützt Unit-Tests und Regressionstests. Hunt und Thomas sehen Tests als Entwurfsfeedback und warnen vor grünen Tests ohne gelöstes Problem. Osmani betont Tests für generierten Code. | Für einen reproduzierbaren Bug erst den Fehler belegen; bei neuen Features Fachvertrag und Schnittstelle prüfen. Kurze Testschritte dürfen die Gesamtstruktur nicht zufällig festlegen. Kein allgemeiner TDD-Wirksamkeitsnachweis für Agents. |
| Kommentare | Ousterhout verlangt fehlendes Schnittstellen- und Entwurfswissen ausdrücklich. Pragmatic rät zu API-Wissen, Gründen und Trade-offs und gegen mechanische Kommentierung jeder Funktion. | [[Kommentare-als-Schnittstellenwissen-pflegen]]: Einheiten, Besitz, erlaubte Zustände, Seiteneffekte und Gründe ergänzen, die Namen und Typen nicht tragen. Offensichtlichen Code nicht nacherzählen. |
| Prototyp weiterverwenden | Pragmatic verlangt bei seinem Prototypbegriff Wegwerfen. Osmani erlaubt Neubau oder bewusste schrittweise Härtung. | Vor dem ersten Demo entscheiden, welche Verwendung erlaubt ist und welche Qualitätslücken die Übernahme blockieren. Keine stillschweigende Beförderung zur Produktion. |
| Planung vor Umsetzung | Getrennte Planung hilft Agents, aber Evans fordert gemeinsame Weiterentwicklung von Modell und Code; neue Erkenntnisse können den ursprünglichen Plan verändern. | Plan als überprüfbare Hypothese behandeln. Modelländerungen offen begründen, fachlich bestätigen und Tests nachführen; Änderungen nicht als bloßes Abhaken des Plans tarnen. |
| Generalität und Zukunft | Ousterhout fordert strategische Investition und passende Allgemeinheit, Pragmatic begrenzt Spekulation durch die Reichweite des Feedbacks. | Zwei konkrete Entwürfe am heutigen Bedarf und einem realistischen Änderungsfall vergleichen. Unbekannte Zukunft nicht durch optionale Parameter und Schichten simulieren. |
| Einheitliche Sprache | Evans will konsistente Sprache innerhalb eines Contexts und erlaubt mehrere Modelle über Contextgrenzen. Ein globales Agentenglossar kann zu viel vereinheitlichen. | Context zum Begriff mitführen; Übersetzung und Eigentümer dokumentieren. Gemeinsame Wörter sind kein Beweis gemeinsamer Bedeutung. |

Diese Spannungen werden in den betroffenen Patterns datiert ergänzt. Frühere Aussagen werden dadurch nicht gelöscht. Die Konfidenz unterscheidet Buchmeinung, unabhängige Belege und tatsächlich durchgeführte Prüfung. Ein Buch mit renommiertem Autor ist keine eigene Ausführung eines Verfahrens in unseren Repositories.

## 9. Ein schlanker Auftragsvertrag für Coding Agents

Die folgende Vorlage ist ein Anwendungsvorschlag in diesem Wissensdokument. Sie ändert keinen aktiven Skill und keine bestehende Freigaberegel. Für kleine Aufgaben reichen wenige Sätze; ein Formular ist kein Selbstzweck.

```markdown
## Ziel und fachliche Bestätigung
Welches beobachtbare Problem wird gelöst?
Welche bestätigte Quelle bestimmt die Bedeutung des gewünschten Verhaltens?

## Modell und Grenzen
Welche Begriffe, Zustände und Invarianten gelten?
Welche Module und Contexts sind betroffen, welche Schnittstellen bleiben stabil?
Welche Ressourcen oder externen Wirkungen brauchen einen benannten Besitzer?

## Erster Schritt
Lernprototyp, Tracer Bullet, Verhaltensänderung oder erhaltender Refactor?
Welche konkrete Unsicherheit oder welches Risiko prüft dieser Schritt?

## Nachweis und Gegenprobe
Welche bestätigten Beispiele, Randfälle und Fehlerpfade entscheiden die Abnahme?
Wie wird eine gemeinsame falsche Annahme in Code und Tests erkennbar?
Welche Prüfungen sind für diese Änderung angemessen und tatsächlich ausführbar?

## Rückmeldung und Ende
Welche neue Erkenntnis erfordert eine Plan- oder Modellkorrektur?
Wann stoppen wir einen ungeeigneten Ansatz?
Welche Ergebnisse, offenen Punkte und nicht ausgeführten Checks werden berichtet?
```

Der Vertrag verbindet [[Plan-first-mit-getrenntem-Review]], [[Codepfad-vor-Aenderung-nachvollziehen]], [[Refactoring-mit-Verhaltensvergleich]] und die neuen Architekturpatterns. Er sollte bestehende Belege verlinken, statt alle Informationen in jeden Auftrag zu kopieren. Eine unabhängige Prüfung braucht jedoch genug Kontext, um die gewünschte Bedeutung beurteilen zu können.

## 10. Reviewfragen nach Art der Änderung

| Änderung | Zentrale Fragen | Häufig übersehene Grenze |
|---|---|---|
| Neue Fachfunktion | Ist die Regel bestätigt? Stimmen Sprache, Zustände und Fehlerergebnisse? Wo wird die Invariante geschützt? | Ein technischer Erfolg kann fachlich wirkungslos oder falsch sein. |
| Strukturänderung | Bleiben öffentliche Ergebnisse und erlaubte Seiteneffekte erhalten? Welches Wissen wird tatsächlich verborgen? | Weniger Zeilen oder Methoden sind allein kein Qualitätsnachweis. |
| Integration | Welche Bedeutung wird übersetzt? Wie behandeln beide Seiten Wiederholung, Teilfehler und Versionswechsel? | Ein passendes JSON-Schema beweist keine fachliche Übereinstimmung. |
| Parallelisierung | Welche Aufgaben sind fachlich unabhängig? Wer integriert und prüft gemeinsam? Wie groß ist die Reviewwarteschlange? | Getrennte Dateien und Worktrees garantieren weder getrennte Ressourcen noch genügend menschliche Prüfrate. |
| Lernprototyp | Welche Frage entscheidet der Versuch? Welche Teile sind Attrappen? Was wird verworfen? | Ein überzeugendes Demo kann nicht vorhandene Produktreife suggerieren. |
| Bugfix | Ist der ursprüngliche Fehler reproduziert? Prüft der Test den Nutzerfall? Welche benachbarte Annahme war falsch? | Eine lokale Symptomkorrektur kann denselben Fehlerpfad an anderer Stelle erhalten. |

Nicht jede Zeile dieser Tabelle braucht einen neuen Test. Ein kurzer lokaler Dokumentationsfix verlangt eine andere Prüfung als eine Änderung mit konkurrierenden Schreibzugriffen. [[Qualitaetsaufwand-nach-Folgen-und-Abhaengigkeiten-staffeln]] bleibt der Maßstab für die Prüftiefe.

## 11. Parallelität endet am Integrations- und Reviewdurchsatz

Osmani beschreibt die Reviewwarteschlange als Begrenzung des Nutzens paralleler Agents (PDF-S. 214–215). Hunt und Thomas behandeln im älteren Buch gemeinsame Zustände, zeitliche Kopplung und klare Ressourcenverantwortung. Daraus folgt unser Transfer: Erst Aufgabenabhängigkeiten und gemeinsam genutzte Ressourcen sichtbar machen, dann parallelisieren, anschließend die Zusammenführung als eigene Arbeit prüfen.

Ein schneller Builder kann den Gesamtdurchsatz verschlechtern, wenn er mehr ungeprüfte Änderungen produziert, als fachlich abgenommen werden können. Die Zahl aktiver Agents ist deshalb keine geeignete Zielmetrik. Sinnvoller sind etwa die Zeit bis zur bestätigten Fertigstellung, Fehler nach der Integration, notwendige Nacharbeit und Wartedauer vor Review. Diese Messgrößen sind Vorschläge für einen lokalen Pilot; für unsere Projekte wurden hier keine entsprechenden Vorher-Nachher-Werte erhoben.

Auch ein fast fertiger Agenten-PR kann falsch priorisiert sein. Osmani nennt ausdrücklich den Einfluss bereits investierter Arbeit auf die Entscheidung, einen ursprünglich wenig wichtigen Vorschlag weiterzuverfolgen (PDF-S. 205). Eine Stop-Regel sollte sich am verbleibenden Nutzen und Aufwand orientieren. Sie soll keinen sinnvollen Ansatz nach einer starren Zahl Fehlversuche verwerfen, aber das Fortsetzen allein wegen schon verbrauchter Tokens verhindern.

## 12. Grenzen der Buchaussagen und offene Versuche

### Den ersten Aufwand auf den fachlichen Kern richten

Evans' Distillation ergänzt die technische Prüflogik um Priorität. Der Core Domain trägt den besonderen fachlichen Nutzen des konkreten Produkts. Er ergibt sich weder aus dem Ordnernamen `core` noch aus der technisch anspruchsvollsten Infrastruktur. Qualifizierte Lern- und Entwurfsarbeit soll dort ansetzen, wo ein falsches Modell den Produktwert gefährdet. Unterstützende generische Fähigkeiten dürfen im tatsächlich benötigten Umfang übernommen oder gebaut werden; ihre allgemeine Wiederverwendbarkeit ist kein eigenes Produktziel (PDF-S. 247–271).

Für einen Agentenauftrag bedeutet das als eigene Ableitung: Der erste Durchstich soll eine echte Kernunsicherheit treffen. Bei einem Planungsprodukt könnte das eine fachlich zulässige Zuordnung unter konkurrierenden Einschränkungen sein. Ein perfektes Login-Demo würde diese Frage offenlassen. Ein knappes Kerndokument benennt den besonderen Wert, wesentliche Begriffe und zuständige Codebereiche. Es dient als Wegweiser und ersetzt weder den Code noch die Fachabnahme. Das verbindet Evans mit [[Produktwert-jenseits-des-reproduzierbaren-Codes]] und der Abwägung, welchen Agenten-PR man überhaupt weiterverfolgt.

### Eine Regel darf mehrere technische Darstellungen haben

Evans' Specifications beschreiben Kriterien, die einen Gegenstand prüfen, passende Gegenstände auswählen oder die Erzeugung eines Gegenstands begrenzen können (PDF-S. 135–146). Die gemeinsame Semantik ist der Bezugspunkt. Sie verlangt keinen einzelnen Codepfad, der gleichermaßen effizient als Datenbankfilter, In-Memory-Prüfung und Optimierungsproblem arbeitet. Ebenso wenig rechtfertigt sie eine vollständige Rule Engine auf Vorrat.

Das präzisiert DRY: Mehrere technische Darstellungen sind nicht automatisch verbotene Duplikation, brauchen aber einen verantwortlichen Ursprung und Vergleichsfälle, wenn sie dieselbe Fachregel ausdrücken. Ein Agent darf die Regeln bei der Übersetzung in SQL oder eine Suchfunktion nicht unabhängig neu erfinden. Rein berechnende Operationen und ausdrückliche Zustandsänderungen bleiben getrennt beurteilt; daraus wird hier kein nachträglich Evans zugeschriebenes vollständiges CQRS-Verfahren.

### Was aus den Büchern keine allgemeine Regel wird

Die Auswertung übernimmt weder Produktivitätsfaktoren noch eine universelle Prozentzahl für den Abstand zwischen Demo und Produkt. Osmanis Fallgeschichten sind teilweise ausdrücklich zusammengesetzt; seine Promptgegenüberstellung ist simuliert. Aussagen über damalige Modelle und Produkte beschreiben den Buchstand von 2025. Sie dienen hier nicht als aktuelle Kauf- oder Modellwahlempfehlung.

Einige Beispiele sind fachlich problematisch. Die Osmani-Analyse erläutert unter anderem ein Transaktionsbeispiel ohne ausreichende Prüfung des Ziel-Updates und einen fehlerhaften Big-O-Vergleich. Die verkürzte Passwort-Hashing-Liste auf PDF-S. 159 und pauschale Rechtsdarstellungen werden nicht als Anleitungen übernommen; das gesonderte bcrypt-Beispiel auf PDF-S. 162 ist von dieser Kritik zu unterscheiden. Rechts-, Lizenz- und Datenschutzfragen bleiben außerhalb einer aktuellen fachlichen Freigabe dieser Buchauswertung. Die alten Bücher enthalten ebenfalls Zuspitzungen: Automatisiertes Deployment ist etwa nicht allein durch Versionsverwaltung in jeder Wirkung rückgängig zu machen.

Die geeigneten nächsten Versuche sind begrenzt und brauchen einen konkreten Projektfall:

- Ein bestehendes Modul an zwei echten Änderungsfällen vergleichen: notwendiges Aufruferwissen, Änderungsausbreitung und verbliebene Abhängigkeiten dokumentieren.
- Für eine komplexe Fachfunktion eine Context Map und wenige bestätigte Invarianten ergänzen; prüfen, ob dadurch bisher unklare Tests entscheidbar werden.
- Einen kleinen Tracer Bullet bewusst mit einem reinen Lernprototyp vergleichen: Welche Unsicherheit wurde jeweils tatsächlich beseitigt und welcher Code durfte weiterleben?
- Einen Agentenauftrag gegen unabhängige Fachbeispiele abnehmen und untersuchen, welche Fehler die bisherigen, eng an der Implementierung entstandenen Tests übersehen hätten.
- Die Parallelität erst erhöhen, wenn Integration und Review im bisherigen Umfang nachvollziehbar funktionieren; zusätzlich Kosten und Nacharbeit erfassen.

Diese Vorschläge sind vorbereitetes Entscheidungswissen. Es wurden damit keine Produktprojekte umgebaut, keine neuen Dienste aktiviert und keine Wirksamkeitskennzahlen gemessen.

## Verbindungen zum Wissensbestand

- [[Information-Hiding-an-Aenderungsgruenden-ausrichten]] und [[Abstraktionswert-mit-Deletion-Test-pruefen]] verbinden die Entwurfsfrage mit dem vorhandenen Deep-Module-Wissen.
- [[Bounded-Contexts-und-Uebersetzungsgrenzen-kartieren]], [[Aggregate-durch-fachliche-Invarianten-begrenzen]] und [[CONTEXT-Glossar]] machen fachliche Bedeutung und Konsistenzgrenzen explizit.
- [[Vertraege-mit-Vorbedingungen-Nachbedingungen-und-Invarianten]], [[TDD-als-Verifikationshebel]] und [[Testharness-als-staerkster-Hebel]] verbinden spezifizierte Erwartungen mit tatsächlich aussagekräftiger Prüfung.
- [[Tracer-Bullet-und-Lernprototyp-bewusst-waehlen]], [[Kommentare-als-Schnittstellenwissen-pflegen]] und [[Designalternativen-vor-Festlegung-vergleichen]] ergänzen bisher wenig ausgearbeitete Designentscheidungen.
- [[Kontrollierte-Agent-Parallelisierung]], [[Domaenen-Harness-mit-Daten-Evals-Rechten-und-Review]] und [[Qualitaetsaufwand-nach-Folgen-und-Abhaengigkeiten-staffeln]] bleiben die Anknüpfung für Durchführung und spätere Bewertung.
