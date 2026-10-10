---
titel: "Eine Skill-Sammlung aktualisieren: lokale Anpassungen zuerst prüfen"
datum: 2026-10-09
kategorie: arbeitsweisen
zusammenfassung: "Ein Skill-Update prüfen heißt, die neue Version mit eigenen Anpassungen, genutzten Aufrufen und einer kleinen repräsentativen Aufgabe abzugleichen."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-10-04-mattpocockuk-2106730768789602313
  - 2026-10-05-aihero-v1-3-implement-spec-pr-retro-and-glossary-md
---

## Kurz gesagt

- Ermittle die aktive Installation und halte den bisherigen Versionsstand fest.
- Vergleiche Änderungen des Autors mit deinen lokalen Anpassungen und verwendeten Aufrufen.
- Prüfe umbenannte Dateien und abhängige Skills gemeinsam.
- Übernimm das Update nach einer kleinen repräsentativen Aufgabe und einem nachvollziehbaren Vergleich.

## Kläre, welche Installation tatsächlich aktiv ist

Du hast eine externe Skill-Sammlung übernommen und an deinen Arbeitsablauf angepasst. Jetzt gibt es ein Update. Ein Skill enthält Anweisungen und gegebenenfalls Hilfsmittel für eine wiederkehrende Agent-Aufgabe. Entscheidend ist zunächst, welche Fassung dein Agent tatsächlich verwendet.

Matt Pococks Sammlung unterscheidet einen verwalteten Plugin-Weg von bearbeitbaren Dateikopien. Sein Update-Hinweis empfiehlt, eigene Dateien mit dem Autorenstand und der lokalen Nutzung abzugleichen. Das ist der Ausgangspunkt für einen Wartungsablauf, der beide Installationswege berücksichtigt. {q:1}

Bei einem Plugin hältst du installierte Version, Herkunft und vorhandene Update-Einstellungen fest. Bei einer lokalen Kopie brauchst du zusätzlich den übernommenen Ausgangsstand und deine Änderungen. Prüfe auch, ob eine globale Installation und eine Projektkopie denselben Skill anbieten. Die aktive Fassung lässt sich aus dem Dateinamen allein nicht zuverlässig ableiten.

Das folgende synthetische Beispiel verwendet einen Skill, der Pull Requests für das Review vorbereitet. Eine eigene Anpassung verlangt dabei die Auflistung ausgeführter Prüfungen. Hier wurde keine Installation aktualisiert und kein eigener Skill-Test durchgeführt.

## Halte den Ausgangsstand vor Änderungen fest

Erfasse die aktuelle Version oder den zugehörigen Git-Commit. Ein Commit bezeichnet einen gespeicherten Stand im Versionsverlauf. Halte außerdem fest, welche Dateien lokal verändert wurden und welche zusätzlichen Vorlagen oder Hilfsskripte dazugehören.

In einem vorhandenen Checkout der Sammlung helfen diese lesenden Befehle:

```sh
git status --short
git rev-parse HEAD
git diff HEAD -- SKILL-PFAD
```

`SKILL-PFAD` ist ein Platzhalter für den betroffenen Bereich. Der Diff zeigt lokale Änderungen gegenüber dem zuletzt gespeicherten Commit, einschließlich bereits zum Commit vorgemerkter Änderungen. Bereits früher gespeicherte eigene Anpassungen brauchen zusätzlich einen Vergleich mit dem ursprünglichen Autorenstand. Unversionierte lokale Dateien prüfst du separat.

Stelle vor der Übernahme sicher, dass sich der bisherige Zustand wiederherstellen lässt. Eine lokale Dateikopie und ein verwaltetes Plugin benötigen dafür jeweils einen passenden Weg. Dokumentiere diesen zusammen mit dem Zielstand des Updates. So bleibt später erkennbar, welche Fassung welche Ausgabe erzeugt hat.

## Vergleiche Autorenänderungen und eigene Anpassungen

Betrachte die Änderungen des Autors zwischen deinem bisherigen Ausgangsstand und dem gewünschten Release. Ein Release ist eine veröffentlichte Version. Lies dabei gezielt den betroffenen Skill, seine referenzierten Dateien und die Änderungsbeschreibung.

Für das vorgeschlagene PR-Beispiel möchtest du wissen: Ändert sich die erwartete Eingabe? Verlangt die neue Fassung andere Prüfungen? Verweist sie auf neue Hilfsmittel? Überschreibt sie die lokale Anforderung, ausgeführte Checks ausdrücklich zu nennen?

| Vergleich | Zweck |
|---|---|
| Bisheriger Autorenstand gegen neues Release | Änderungen aus dem Update verstehen |
| Bisheriger Autorenstand gegen eigene Fassung | Lokale Ergänzungen erkennen |
| Geplante neue Fassung gegen eigene Fassung | Übernahme und Konflikte beurteilen |

Ordne jede lokale Ergänzung ein: weiterhin benötigt, durch das Update bereits abgedeckt oder mit neuem Verhalten unvereinbar. Bei einem Konflikt formulierst du die gewünschte Regel ausdrücklich. Ein mechanisch erfolgreiches Zusammenführen der Dateien beantwortet die fachliche Frage noch nicht.

## Prüfe verwendete Aufrufe und Migrationen

Pococks Update-Prompt schlägt vor, die letzten **25 Sessions** nach Skill-Aufrufen auszuwerten. Das beschreibt seinen empfohlenen Suchbereich; für diesen Beitrag wurde keine eigene Session-Historie analysiert. Die Häufigkeit eines Aufrufs zeigt Nutzung und beantwortet allein noch nicht, ob der Skill hilfreich gearbeitet hat. {q:1}

Für deinen Wartungscheck wählst du einen überschaubaren vorhandenen Verlauf. Sammle verwendete Aufrufe und dazugehörige Aufgaben. Ein selten verwendeter Skill kann für einen kritischen Schritt wichtig sein; ein häufig verwendeter kann weiterhin viel Korrektur brauchen.

Der AIHero-Beitrag nennt konkrete Migrationen: `CONTEXT.md` und `CONTEXT-MAP.md` werden zu `GLOSSARY.md` und `GLOSSARY-MAP.md`. Aktualisierte Skills suchen die neuen Namen. Die Referenzen und zusammengehörigen Dateien müssen deshalb bei einer Übernahme gemeinsam geprüft werden. {q:2}

Suche gezielt nach Verweisen auf die alten Dateinamen in deinen betroffenen Vorlagen und Aufrufen. Prüfe ebenso, welche Skills andere Skills aufrufen. Der Beitrag beschreibt Änderungen an diesen Aufrufen und an installierbaren Skill-Dateien. Eine vorhandene Datei bedeutet daher noch nicht, dass sie korrekt geladen wird. {q:2}

## Nutze eine kleine repräsentative Aufgabe

Bereite für den lokalen Vergleich eine begrenzte Aufgabe vor, die deinen tatsächlich genutzten Ablauf trifft. Im synthetischen Beispiel erhält der PR-Skill denselben kleinen Diff, dieselbe Liste ausgeführter Prüfungen und dieselben bekannten Einschränkungen.

Lass bisherige und geplante Fassung daraus jeweils einen Entwurf der PR-Beschreibung erstellen. Der Versuch endet bei den Entwürfen; er benötigt keine Veröffentlichung. Halte Modell, Eingabe und relevante Einstellungen fest, damit Unterschiede leichter einzuordnen sind.

Prüfe vorher benannte Kriterien: Findet der Skill die richtigen Referenzdateien? Bleibt deine lokale Anforderung erhalten? Nennt die Ausgabe ausschließlich tatsächlich übergebene Prüfungen? Werden bekannte Einschränkungen sichtbar? Ein ausgedachtes Testergebnis im Entwurf wäre ein konkreter Grund, die geplante Fassung zu korrigieren.

Ein kleiner Versuch deckt einen begrenzten Teil des Verhaltens ab. Ergänze bei Bedarf einen Fall mit fehlenden Eingaben oder eine seltene wichtige Aufgabe. Jede zusätzliche Aufgabe sollte eine offene Frage beantworten, die für deine Übernahmeentscheidung relevant ist.

## Übernimm das Update mit einem kurzen Wartungsprotokoll

Halte zum Abschluss Ausgangsstand, Zielstand, übernommene Änderungen, erhaltene lokale Anpassungen und die Ergebnisse deiner Prüfaufgaben fest. Wenn du nur einen Teil geprüft hast, nenne den übrigen Bereich ausdrücklich.

Ein Plugin kann den Transport neuer Versionen übernehmen; der Vergleich mit deinem Arbeitsablauf bleibt eine eigene Aufgabe. Bei einer lokalen Kopie pflegst du die übernommenen Änderungen selbst. Neue Skripte, Abhängigkeiten oder verlangte Rechte benötigen eine gesonderte inhaltliche Prüfung vor ihrer Nutzung.

Beginne mit dem Skill, den du aktuell für eine konkrete Aufgabe brauchst. Vergleiche seinen Versionsstand, seine lokalen Änderungen und seine Referenzen. Anschließend entscheidet eine kleine passende Prüfaufgabe, ob du die geplante Fassung übernimmst oder zunächst nacharbeitest.
