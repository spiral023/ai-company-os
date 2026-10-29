# Vergleich: Kurstransfer auf eine Agentic Software Factory

**Stand:** 2026-10-29

## Übersicht

Die lokale HTML-Leseausgabe zu Matt Pococks Kurs verbindet die bisher einzeln erfassten Methoden zu einem nachvollziehbaren Lernablauf. Sie liefert zusätzliche konkrete Beispiele, aber keine neue unabhängige Herkunftsfamilie für bereits bekannte Pocock-Skills. Die Analyse umfasst HTML, Übungen, Lösungen und ausgewählte Abbildungen; die Videos sind ausschließlich archiviert und inventarisiert.

| Entscheidung | Beitrag des Kurses | Anschluss an den Bestand | Grenze |
|---|---|---|---|
| Welche Begriffe meinen dasselbe? | Szenarien prüfen, Glossar schärfen, UI und Code abgleichen | [[CONTEXT-Glossar]], Evans | Gleich klingende Begriffe können in verschiedenen Bounded Contexts etwas anderes bedeuten |
| Welche Gründe müssen bleiben? | ADR nur für schwer umkehrbare, überraschende Trade-offs | [[ADRs-auf-tragende-Entscheidungen-begrenzen]], Ousterhout | Knappe Dokumentation darf notwendige Randbedingungen nicht verschweigen |
| Welches Wissen fehlt vor der Umsetzung? | Decision Map mit Frontier und passenden Untersuchungen | [[Wayfinder-als-Karte-offener-Entscheidungen]] | Kein Ersatz für spätere Verhaltenstickets und Ausführungspläne |
| Was muss ein Prototyp beantworten? | Konkrete Bedienung und Integration vor Festlegung untersuchen | [[Tracer-Bullet-und-Lernprototyp-bewusst-waehlen]], Pragmatic Programmer | Lerncode ist noch kein freigegebener Produktionspfad |
| Was bedeutet abgeschlossen? | Spec, überprüfbares Verhalten, Standards und sichtbare QA verbinden | [[Plan-first-mit-getrenntem-Review]], Osmani | Implementierung, Test und Erklärung können dieselbe falsche Annahme teilen |
| Wo wird menschliche Aufmerksamkeit gebraucht? | Reversibilität, Blast Radius und fehlende Belege offenlegen | [[Qualitaetsaufwand-nach-Folgen-und-Abhaengigkeiten-staffeln]] | Ein kompaktes Risikoetikett ersetzt die Begründung nicht |
| Wie wird der nächste Lauf besser? | Reviewkommentare mit Sessions verbinden und gezielt Verbesserungen auswählen | [[Review-Findings-in-Agent-Verbesserungen-ueberfuehren]] | Jede Präferenz als globale Regel zu speichern würde den Kontext weiter aufblähen |

Quelle: [[2026-10-29-matt-pocock-software-factories-real-engineers]]. Die Buchaussagen und ihre Grenzen sind in [[Softwaregrundlagen-fuer-Agentic-Engineering]] ausführlich belegt.

## Empfehlungen

### Die Arbeitsweise nach der offenen Frage wählen

Ein kleiner, gut überschaubarer Diff kann mit einer kurzen Aufgabenbeschreibung und passender Verifikation auskommen. Wenn Anforderungen oder Fachbegriffe unscharf sind, mit Grilling beginnen. Erst wenn dessen Ergebnis nicht mehr sinnvoll in einer Session entsteht oder weitere Untersuchungen voraussetzt, die Klärung als Wayfinder-Map fortführen. Das entspricht dem Kursentscheidungsbaum und begrenzt Prozessaufwand anhand der tatsächlichen Schwierigkeit.

Der Nutzen einer Map liegt nicht in ihrer Ticketzahl. Entscheidend ist, ob ein Ticket eine präzise Frage beantwortet, auf deren Ergebnis andere Entscheidungen warten. Research beschafft fehlendes Wissen. Ein Prototype macht Verhalten oder Integration beurteilbar. Grilling klärt Präferenzen und Regeln mit einem fachkundigen Menschen. Eine vorbereitende Task ermöglicht die Untersuchung, etwa durch einen bereitgestellten Testzugang. Diese Ergebnisse gehören mit ihrer Belegart zurück in die Map.

Der geprüfte Referenzstand von `mattpocock/skills` unterscheidet außerdem offene, unblockierte, unbeanspruchte Tickets als Frontier. Damit sind drei Bedingungen sichtbar: Eine Frage kann inhaltlich offen, durch ein Ergebnis blockiert oder bereits einer anderen Session zugeordnet sein. Eine reine Liste offener Issues drückt diese Unterschiede nicht aus.

### Fachsprache und Architekturwissen gemeinsam pflegen

Evans begründet, warum Begriffe innerhalb eines Modells präzise sein müssen und über Modellgrenzen ihre Bedeutung ändern können. Der Kurs zeigt den alltäglichen Agentenfehler: UI, E-Mail, Datenbank und Funktionsnamen verwenden uneinheitliche Wörter. Der Transfer ist eine begrenzte semantische Prüfung vor einer Umbenennung. Zuerst zeigen, welche Zustände und Regeln gemeint sind; danach entscheiden, welche Namen gemeinsam geändert werden dürfen.

Der Refund-Fall ist dafür besonders brauchbar: Anfrage, Genehmigung und Auszahlung sind verschiedene Vorgänge. Ein bloßes Search-and-replace würde eine fachliche Unterscheidung verdecken. Entsprechend darf ein Datenbankdefault nicht als Migration vorhandener Werte ausgegeben werden. Terminologiekonsistenz und Datenzustand sind getrennt zu prüfen.

Ousterhout ergänzt den Informationsaspekt: Ein nützliches Modul reduziert das Wissen, das Aufrufer mitbringen müssen. Ein Glossar kann fehlendes Fachwissen erklären, aber keine unnötig komplizierte Schnittstelle heilen. Wenn eine einfache Operation ständig lange Erläuterungen verlangt, sind sowohl Sprache als auch Modulgrenze zu untersuchen. ADRs bewahren dann nur die wichtigen Gründe hinter einer bewussten Entscheidung; sie ersetzen weder API-Vertrag noch Domänenmodell.

### Prototypergebnisse vor dem Handoff qualifizieren

Der Pragmatic Programmer unterscheidet Lernprototyp und Tracer Bullet. Der Kurs macht diese Grenze an der Notification-Integration anschaulich: Ein funktionierender Versuch kann wichtige Erkenntnisse über Preferences und Workflows liefern, obwohl er mit Abkürzungen und manuellen Schritten arbeitet. Die belastbare Übergabe benennt deshalb, was tatsächlich gezeigt wurde, welche Daten oder Berechtigungen gebraucht wurden und was am späteren Produktpfad noch fehlt.

Für eine Spec darf aus einem erfolgreichen Einzelversuch keine umfassende Integrationszusage werden. Eine vorbereitete UI beweist keine Zustellung. Ein gespeicherter Preference-Wert beweist noch nicht, dass sämtliche Versandwege ihn beachten. Ein gebauter Client beweist keine korrekte externe Konfiguration. Diese Gegenfragen sind aus dem Material abgeleitete Empfehlungen für unseren Versuch, keine zusätzlich beobachteten Kursfehler.

### Prüfungen mit unterschiedlichen Erkenntnisgrenzen kombinieren

Deterministische Checks finden nur Eigenschaften, die sie ausdrücken. Ein Review-Agent kann Spec und Standards vergleichen, bleibt aber ein fehlbarer Beurteiler. Ein Mensch kann fachliche Plausibilität und Produktwirkung bewerten, benötigt dafür gut abgegrenzte Belege. Die drei Ebenen ergänzen sich; eine weitere Rolle schafft nicht automatisch eine unabhängige Annahmebasis.

Osmanis Warnung vor zusammenpassenden, aber falschen Artefakten verschärft die PR-Frage: Stammen erwartetes Verhalten, Test und Implementierung aus derselben ungeprüften Interpretation? Ein Reviewer soll deshalb die ursprüngliche Anforderung gegen die demonstrierte Wirkung halten. Vorher-Nachher-Belege helfen nur, wenn sie den relevanten Fall und die behauptete Korrektur tatsächlich zeigen.

Reversibilität und Blast Radius separat beschreiben. Ein Textwechsel lässt sich häufig leicht zurücknehmen; eine Datenänderung kann trotz kleinem Diff bleibende Folgen haben. Der Kurs berichtet dazu aus seiner Praxis. Wir übernehmen das Entscheidungsraster, keine persönliche Prozentangabe als allgemeine Risikoverteilung.

### Retro als begrenzte Verbesserungsschleife behandeln

Eine Retro soll einen beobachteten Fehler auf eine passende Änderung zurückführen. Bei einem mechanisch erkennbaren Muster zuerst vorhandene Checks prüfen: Fehlt der Check, wird er nicht ausgeführt oder wurde sein Ergebnis ignoriert? Bei einer Ermessensentscheidung prüfen, welche Fachinformation oder Präferenz fehlte. Bei Navigationsproblemen nach einem gezielten Wegweiser suchen.

Die Kursdemo und der lokale Skill-Checkout unterscheiden sich hier in der Schärfe: Der aktuelle Retro-Text verlangt bei mechanischen Verstößen ausdrücklich deterministische Checks. Diese Abweichung bleibt sichtbar. Die historische Demo wird nicht nachträglich so dargestellt, als hätte sie bereits jede aktuelle Regel enthalten.

## Kleiner Versuch für dieses Repo

Ein vorhandenes, überschaubares Feature in einem separaten Projekt-Repo auswählen. Keine neue Factory-Laufzeit und kein umfassendes Regelpaket einführen. Als Entwurf gelten folgende Prüffragen:

1. Kann ein fachkundiger Mensch am konkreten Beispiel entscheiden, ob zwei Begriffe dasselbe meinen? Das Ergebnis mit zwei oder drei Gegenbeispielen festhalten.
2. Lässt sich eine offene Integrationsfrage durch eine begrenzte Research- oder Prototype-Aufgabe beantworten? Vor dem Versuch das erwartete Entscheidungssignal und die Abbruchbedingung nennen.
3. Kann eine neue Session anhand der persistenten Map zwischen geklärten Fakten, Entscheidungen, Blockaden und ungesicherten Annahmen unterscheiden?
4. Zeigt die spätere Spec beobachtbares Verhalten und Ausschlüsse, ohne Implementierungsdetails des Lernprototyps unbemerkt festzuschreiben?
5. Findet das getrennte Spec-/Standards-Review eine absichtlich eingebaute fehlende Anforderung und einen tatsächlichen Regelverstoß? Finding, Dateibeleg und Unklarheiten erfassen.
6. Wird ein Korrekturcommit erneut angemessen geprüft? Die Retro soll den tatsächlichen Ablauf rekonstruieren und höchstens wenige belegte Verbesserungen vorschlagen.

Zu dokumentieren wären Untersuchungszeit, Zahl ungeklärter Annahmen am Handoff, falsche Reviewalarme, gefundene absichtliche Defekte und benötigte menschliche Eingriffe. Das sind vorgeschlagene Beobachtungen, keine bereits erhobenen Messwerte. Produktive Skills, Rechte, Authentifizierung und Release-Gates werden durch diesen Wissenseintrag nicht geändert.

## Offene Fragen

- Welche Fehler entstehen durch unklare Fachsprache und welche durch eine ungeeignete Modulgrenze?
- Wie viel Map-Pflege ist bei unserem Projektumfang tatsächlich hilfreich?
- Welche Aussagen der Notification-Demo brauchen vor heutiger Nutzung eine erneute Anbieterprüfung?
- Welche mechanischen Reviewwünsche decken bestehende Checks bereits ab?
- Wie lässt sich eine Verbesserung der Reviewqualität messen, ohne nur die Zahl gefundener Kleinigkeiten zu erhöhen?

Die [ausführliche Analyse](../../reports/2026-10-29-matt-pocock-software-factories-kursanalyse.md) enthält Kapitelbelege und Abdeckungsgrenzen. Der [Archivnachweis](../../docs/kurse/matt-pocock-software-factories/README.md) führt zur lokalen Leseausgabe und zum Dateiinventar.
