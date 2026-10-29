---
titel: "Gute Kommentare machen API-Verträge sichtbar"
datum: 2026-10-29
kategorie: arbeitsweisen
zusammenfassung: "Mit frühen Schnittstellenkommentaren prüfst du einen Entwurf vor der Umsetzung. Ein hypothetischer Bildzuschnitt zeigt, welche Regeln ein Coding Agent ausdrücklich kennen muss."
status: freigegeben
geprueft_am: 2026-10-29
freigabe: automatisch
quellen:
  - 2021-07-01-pdf-a-philosophy-of-software-design-2nd-edition
---

## Kurz gesagt

- Beschreibe vor der Umsetzung, welche Bedingungen und Ergebnisse deine Schnittstelle verspricht.
- Ergänze in Kommentaren das Wissen, das Namen, Typen und sichtbarer Code offenlassen.
- Prüfe bei einer Verhaltensänderung auch den dazugehörigen Vertrag.

Ein Coding Agent, ein KI-System für Entwicklungsaufgaben, kann aus einer Methodensignatur viele plausible Absichten ableiten. Einige davon können falsch sein. John Ousterhout macht in [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php) deshalb die informellen Regeln einer API, also einer Programmierschnittstelle, ausdrücklich zum Gegenstand des Entwurfs. Kommentare können diese Regeln sichtbar machen. Die folgende Anwendung auf Agenten ist eine eigene Ableitung aus seiner Entwurfsphilosophie. {q:1}

## Welches Wissen der Code offenlässt

Eine Funktion namens `cropImage` klingt verständlich. Trotzdem bleiben Fragen. Verwenden ihre Koordinaten Pixel oder normierte Werte? Gehört die rechte Grenze noch zum ausgewählten Bereich? Wird das Original verändert? Was passiert bei einem Ausschnitt außerhalb des Bildes?

Ein sprechender Name hilft beim Einstieg. Für die korrekte Verwendung brauchst du zusätzlich die vereinbarte Bedeutung. Wenn jeder Aufrufer dafür die Implementierung untersuchen muss, trägt die Schnittstelle ihre Funktion nur teilweise.

Ousterhout unterscheidet zwischen präziser Information und erklärender Intuition. Einheiten und Grenzen können entscheidende Details sein. Eine Beschreibung des übergeordneten Ziels kann dagegen erklären, warum ein Verfahren ungewöhnlich aufgebaut ist. Beide Arten ergänzen das Verständnis. Auf den PDF-Seiten 110–124 arbeitet er diese Aufgaben von Kommentaren aus. {q:1}

## Ein früher Kommentar prüft den Entwurf

Ousterhout empfiehlt, wesentliche Schnittstellenkommentare vor den Methodenrümpfen zu schreiben. Dabei formulierst du Zweck, Benutzungsbedingungen und Ergebnisse, bevor dich die technischen Einzelheiten beanspruchen. Wenn eine vollständige Beschreibung kaum verständlich gelingt, kann das auf eine schwierige Abstraktion hinweisen. {q:1}

Das Verfahren braucht Ehrlichkeit. Ein kurzer Text wirkt nur dann einfach, wenn er die relevanten Regeln tatsächlich enthält. „Schneidet das Bild passend zu“ lässt fast alle wichtigen Entscheidungen offen. Die Kürze dieser Formulierung sagt daher wenig über die Qualität des Entwurfs aus.

Beim Schreiben entdeckst du möglicherweise, dass eine Methode zwei unterschiedliche Aufgaben verbindet oder mehrere Zustände widersprüchlich behandelt. Die PDF-Seiten 139–143 beschreiben Kommentare gerade als Werkzeug für solche frühen Entscheidungen. Für einen Agentenauftrag lässt sich daraus eine kleine Vorarbeit ableiten: den Vertrag formulieren und an konkreten Aufrufen prüfen, bevor die Implementierung entsteht.

## Ein Bildzuschnitt als Gedankenexperiment

Stell dir hypothetisch vor, dein Produkt erzeugt Vorschaubilder für hochgeladene Fotos. Ein Agent soll einen neuen Zuschnittmodus ergänzen. Du legst zunächst fest, dass die Koordinaten in Pixeln des bereits ausgerichteten Bildes angegeben werden. Ein Ausschnitt außerhalb der Bildfläche wird abgelehnt. Das Original bleibt erhalten; das Ergebnis ist ein neues Bild.

Diese Entscheidungen gehören zur Verwendung. Der Agent muss sie kennen, um Vorschau, Speicherzugriff und Fehleranzeige konsistent zu gestalten. Daraus lassen sich konkrete Prüffälle ableiten: ein gültiger Ausschnitt, eine überschrittene Grenze und der Zustand des Originals nach dem Aufruf.

Während der Umsetzung könnte ein anderer Vorschlag entstehen: Überstehende Bereiche werden automatisch auf die Bildkante begrenzt. Auch das wäre eine mögliche Semantik. Sie verändert jedoch den zugesicherten Umgang mit Eingaben. Du müsstest sie fachlich auswählen und die betroffenen Aufrufer darauf abstimmen. Ein nachträglich angepasstes Testergebnis erledigt diese Entscheidung nicht.

## Schnittstelle und Implementierung haben verschiedene Leserfragen

Zur Schnittstelle gehören die Regeln, die Benutzer für den Aufruf benötigen. Der interne Mechanismus kann andere Erklärungen brauchen: etwa warum die Bibliothek ein Zwischenformat erhält oder weshalb zwei Verarbeitungsschritte in einer bestimmten Reihenfolge stehen.

Ousterhout warnt davor, Schnittstellenkommentare mit privaten Implementierungsdetails zu überladen. Solche Details können Benutzer an eine Entscheidung gewöhnen, die sie gar nicht kennen müssen. Gleichzeitig dürfen relevante Nebenwirkungen, Fehler oder Einschränkungen der gleichzeitigen Benutzung sichtbar bleiben. Diese Trennung erläutert er auf den PDF-Seiten 119–129. {q:1}

Im Bildbeispiel muss ein Aufrufer die Koordinaten verstehen. Die genaue interne Bibliotheksfunktion könnte austauschbar bleiben. Würde ein Wechsel dieser Funktion das Ergebnisformat oder die Fehlermeldungen verändern, müsste dagegen geprüft werden, welche Zusicherung nach außen besteht. Das Verhältnis von verborgenem Wissen und Benutzung vertieft der [Beitrag zu Deep Modules](post:deep-modules-weniger-wissen-fuer-coding-agents).

## So bleiben Gründe bei Änderungen auffindbar

Hilfreiche Kommentare verlieren ihren Nutzen, wenn sie dem Code widersprechen. Ousterhout empfiehlt deshalb, sie nahe an den beschriebenen Stellen zu halten, Entwurfsentscheidungen möglichst einmal zu erklären und andere Stellen dorthin verweisen zu lassen. Dauerhafte Gründe sollen auch dort stehen, wo spätere Bearbeiter sie suchen. Eine alleinige Erklärung im Änderungsverlauf ist leicht zu übersehen. {q:1}

Für die Zusammenarbeit mit einem Agenten leite ich daraus eine konkrete Reviewaufgabe ab. Lass ihn für jede geänderte Zusicherung den betroffenen Kommentar nennen. Kontrolliere anschließend Code, Vertrag und Prüffall gemeinsam. Die PDF-Seiten 147–150 begründen diese Nähe und die gemeinsame Prüfung beim Durchsehen einer Änderung.

Vermeide dabei eine Flut automatisch erzeugter Beschreibungen. Ein Kommentar zu einer sichtbaren Zuweisung trägt wenig bei, wenn er nur dieselbe Zuweisung in Worte fasst. Interessant wird er, sobald er eine sonst fehlende Einheit, Einschränkung oder Entwurfsentscheidung verständlich macht. Seine Pflege muss zu dem Wissen passen, das du erhalten möchtest.

## Beginne mit einer häufig benutzten Schnittstelle

Wähle für den nächsten Auftrag eine Funktion, deren Benutzung regelmäßig Rückfragen auslöst. Formuliere ihren Zweck, die erlaubten Eingaben, das zugesicherte Ergebnis und die wichtigen Nebenwirkungen. Ergänze einen normalen Aufruf und einen Fehlerfall.

Gib diese Beschreibung dem Agenten zur kritischen Prüfung: Welche Entscheidung bleibt mehrdeutig? Welche Regel müsste ein neuer Aufrufer zusätzlich erraten? Kläre die offenen Punkte, bevor du Code ergänzen lässt.
