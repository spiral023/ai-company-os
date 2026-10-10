---
titel: "Session-Handoff: Morgen weiterarbeiten, ohne den Projektstand zu erraten"
datum: 2026-10-09
kategorie: arbeitsweisen
zusammenfassung: "Ein kurzes Session-Handoff hält Ziel, Revision, Entscheidungen, ausgeführte Checks und offene Fragen fest. Nutze die Markdown-Vorlage und prüfe beim Wiedereinstieg zuerst den aktuellen Arbeitsstand."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-07-10-voxyz-mattpocock-skills
  - 2026-02-10-boris-tane-plan-annotation-workflow
---

## Kurz gesagt

- Schreibe vor dem Sessionende das Ziel, den tatsächlich erreichten Stand und den nächsten konkreten Schritt auf.
- Ordne ausgeführte Checks einer Revision und dem uncommitteten Zustand zu. Fehlende Prüfungen bleiben ausdrücklich offen.
- Halte Entscheidungen mit ihrer Begründung fest und verweise auf vorhandene Dateien.
- Lass die Fortsetzung zuerst den gegenwärtigen Repository-Zustand prüfen, bevor sie alte Aussagen übernimmt oder Code verändert.

## Der nächste Morgen braucht einen klaren Einstieg

Gestern hast du eine Suche untersucht, eine Filterregel geändert und noch einen offenen Fall entdeckt. Heute startet ein neuer Chat. Im Verlauf stehen verworfene Ideen, frühere Testergebnisse und der letzte Satz „morgen weitermachen“. Welcher Stand ist jetzt gültig?

Ein Handoff ist eine kompakte Übergabe des Arbeitsstands. Es hält die Informationen bereit, die du für die Fortsetzung brauchst: Was war das Ziel, was ist entschieden, was wurde tatsächlich überprüft und wo beginnt die nächste Handlung?

Vox beschreibt `/handoff` aus Matt Pococks Skills als Verdichtung der laufenden Unterhaltung in ein Übergabedokument. Das ist ein beschriebenes Verfahren; eine automatische, fehlerfreie Fortsetzung ergibt sich daraus noch nicht.{q:1}

Du kannst denselben Zweck mit einer schlichten Markdown-Datei erfüllen. Ihr Nutzen liegt in prüfbaren Angaben und einem klaren Einstieg. Eine Abschrift der ganzen Session macht diesen Einstieg wieder schwer auffindbar.

## Trenne Arbeitsstand, Entscheidung und Prüfergebnis

Beginne mit dem Ziel in einem Satz. „Suche fertigstellen“ lässt offen, welche Funktion du erwartest. „Die Mitgliederliste soll nach Namen filtern und einen Leerzustand anzeigen“ gibt der Fortsetzung ein konkretes Verhalten.

Danach beschreibst du den erreichten Stand: betroffene Dateien, fertig bearbeitete Teile und noch fehlende Schritte. Verweise auf vorhandene Anforderungen oder Pläne. Boris Tane arbeitet mit einer persistenten Plandatei, auf die er nach einer Kontextverdichtung erneut verweisen kann. Diese Form des vorhandenen Projektartefakts passt als Bezugspunkt für eine Übergabe.{q:2}

Eine Entscheidung braucht einen Grund. Etwa: „Der Filter bleibt lokal, weil die vollständige Liste bereits geladen wird.“ Ohne diesen Zusammenhang könnte ein späterer Agent dieselbe Frage neu öffnen und einen zusätzlichen API-Weg bauen.

Prüfergebnisse bilden einen eigenen Teil. „Tests grün“ ist zu ungenau. Nenne den ausgeführten Befehl, den Umfang, das Ergebnis und den geprüften Arbeitsstand. Ein Build und ein Browserablauf beantworten unterschiedliche Fragen. Ein geplanter Check gehört in die offenen Schritte.

## Eine kurze Vorlage mit ehrlichen Platzhaltern

Die folgende Vorlage ist synthetisch. Sie beschreibt keinen echten Projektstand und enthält weder Zugangsdaten noch persönliche Informationen. Die Platzhalter werden erst durch beobachtete Angaben aus deiner Session ersetzt.

```markdown
# Session-Handoff

## Ziel
<Gewünschtes Verhalten und Grenze des Auftrags>

## Geprüfter Arbeitsstand
- Repository und Branch: <ermittelte Angaben>
- Revision: <ermittelte Commit-ID>
- Uncommittete Änderungen: <Dateien und aktueller Diff>
- Betroffene Dateien: <Pfade>

## Erreichter Stand und Entscheidungen
- Stand: <fertige und noch offene Teile>
- Entscheidung: <gewählte Lösung und Grund>
- Vorhandener Plan: <Dateipfad, falls vorhanden>

## Tatsächlich ausgeführte Checks
- <Befehl oder manueller Ablauf> — <Ergebnis und Umfang>
- Geprüfter Stand: <Revision plus uncommittete Änderungen>
- Noch ungeprüft: <klar benannte Bereiche>

## Offene Fragen
- <Frage, Auswirkung und benötigte Information>

## Nächster Schritt
<Eine konkrete Handlung mit Prüfkriterium>

## Einstieg für die Fortsetzung
Aktuellen Branch, Revision, Status und relevante Dateien prüfen.
Abweichungen zum Handoff klären, bevor Änderungen beginnen.
```

Wenn keine Checks ausgeführt wurden, schreibe das direkt hinein. Wenn eine Browserprüfung nur einen Ablauf abdeckte, benenne genau diesen Ablauf. Formulierungen wie „scheint fertig“ lassen den Nachfolger wieder raten.

Die Commit-ID allein beschreibt einen uncommitteten Arbeitsstand nur teilweise. Ergänze deshalb die betroffenen Änderungen. Für eine wichtige Abnahme kannst du einen erhaltenen Diff oder einen anderen im Projekt üblichen Vergleichspunkt referenzieren.

## Halte nur Entscheidungen fest, die die Fortsetzung brauchen wird

Eine Übergabe wächst schnell zu einem zweiten Projektplan. Begrenze sie auf Informationen, deren Verlust eine falsche Entscheidung oder wiederholte Untersuchung wahrscheinlich macht.

Eine verworfene Idee gehört hinein, wenn ihr Grund weiterhin relevant ist. Ein möglicher zusätzlicher Cache könnte beispielsweise wegen bereits vorhandener Aktualisierungslogik entfallen sein. Dann reicht eine kurze Begründung mit dem passenden Dateipfad.

Referenziere längere Spezifikationen, vorhandene Tests und bestehende Tickets. Übernimm ihren gesamten Inhalt nicht erneut. Mehrere Kopien derselben Anforderung können später unterschiedliche Zustände zeigen.

Der nächste Schritt sollte ausführbar sein. „Weiter testen“ ist vage. „Leerzustand mit bestehendem Suchfilter reproduzieren und erwartete Aktion prüfen“ benennt Handlung und Ergebnis. Bei einer offenen Produktentscheidung lautet der nächste Schritt entsprechend, die fehlende Information einzuholen.

## Prüfe beim Wiedereinstieg den gegenwärtigen Zustand

Eine Fortsetzung beginnt mit Lesen und Abgleichen. Diese Git-Befehle sind ein Vorschlag für den Einstieg; sie wurden hier nicht gegen ein Beispielprojekt ausgeführt:

```sh
git branch --show-current
git rev-parse HEAD
git status --short
git diff --stat
```

Der Status zeigt, ob inzwischen weitere Änderungen vorliegen. Die Übersicht des Diffs hilft bei der Auswahl der relevanten Dateien; ihre Inhalte musst du anschließend gezielt prüfen. Unversionierte Dateien können ebenfalls zum Arbeitsstand gehören.

Vergleiche die aktuelle Revision und die betroffenen Stellen mit der Übergabe. Wurde eine Entscheidung inzwischen verändert? Ist eine erwähnte Datei verschoben? Passt der beschriebene Test noch zur vorhandenen Implementierung?

Alte Ergebnisse gelten für ihren damaligen Stand. Wiederhole relevante Checks, wenn die geprüften Bereiche verändert wurden oder die aktuelle Aufgabe eine neue Prüfung braucht. Ein Handoff führt zu den richtigen Informationen; die gegenwärtige Beobachtung entscheidet über die nächsten Schritte.

## Halte Aufwand und Gültigkeit im Blick

Eine kurze Aufgabe, die du unmittelbar abschließt, braucht oft keine eigene Übergabedatei. Bei einer Unterbrechung oder einem Wechsel zwischen Chats lohnt sich dagegen ein klarer Abschluss. Der [Entscheidungsbaum für Agent-Kontext](post:kontext-hygiene-entscheidungsbaum) hilft beim Einordnen solcher Wechsel.

Auch eine gute Verdichtung verliert Details. Der Agent kann eine Vermutung als Entscheidung zusammenfassen oder einen geplanten Test als ausgeführt darstellen. Lies deshalb besonders Ziel, Entscheidungen und Checks selbst gegen, bevor du die Session beendest.

Aktualisiere die Übergabe nach einer relevanten Änderung oder kennzeichne ihren alten Stand deutlich. Vermeide parallele Übergabedateien ohne erkennbar gültige Fassung.

Beende deine nächste längere Session mit dieser Vorlage. Fülle nur beobachtete Fakten ein, lasse offene Punkte offen und formuliere eine nächste Handlung. Beim Wiedereinstieg prüfst du zuerst den aktuellen Arbeitsstand und setzt dann an diesem konkreten Punkt fort.
