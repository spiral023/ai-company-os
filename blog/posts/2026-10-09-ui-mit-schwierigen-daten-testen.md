---
titel: "Deine UI mit schwierigen Daten testen: lange Namen, leere Listen, große Zahlen"
datum: 2026-10-09
kategorie: arbeitsweisen
zusammenfassung: "Teste deine UI mit gültigen Extremdaten: Eine kleine Daten-Fixture, leere Listen und ein reproduzierbarer Vergleich zeigen dir, wo Namen, E-Mail-Adressen und große Zahlen das Layout überfordern."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-10-04-emilkowalski-2106752670405099523
---

## Kurz gesagt

- Erfasse die angezeigten Felder und ihre tatsächlichen Grenzen aus Formular, API und Datenmodell.
- Baue eine kleine Fixture mit plausiblen Extremwerten. Eine Fixture ist ein festgelegter Datensatz, den du wiederholt in dieselbe Oberfläche laden kannst.
- Vergleiche normale, schwierige, leere und einzelne Einträge bei identischer Darstellung.
- Halte jeden Fehler mit Eingabe und Reproduktionsschritten fest. Sichere relevante Korrekturen gegen erneutes Auftreten ab.

## Die Demo passt. Deine echten Inhalte vielleicht weniger.

Deine Mitgliederliste sieht ordentlich aus: kurze Namen, vollständig ausgefüllte Profile, kompakte Zahlen. Dann kommt ein Import mit langen Familiennamen, fehlenden Rollen und einer E-Mail-Adresse ohne günstige Umbruchstelle. Plötzlich wandert das Aktionsmenü aus der Zeile.

Genau solche Inhaltsfälle beschreibt Emil Kowalskis Skill `/break-ui`: realistische Extremwerte durch dieselbe Datenschnittstelle wie die Demo laden, zwischen den Zuständen wechseln und auftretende Darstellungsfehler einzeln erfassen. Der veröffentlichte Ablauf liefert einen Prüfauftrag; eine gemessene Verbesserung deiner App folgt daraus noch nicht.{q:1}

Beim [UI-Aufbau mit Referenzbild und Browser-Audit](post:ui-mit-agenten-referenzbild-audit) legst du die Gestaltung und Bedienung fest. Hier prüfst du, wie diese Gestaltung auf variable Inhalte reagiert. Das ist besonders hilfreich für Tabellen, Profile, Karten, Suchergebnisse und Formulare.

## Prüfe zuerst, welche Daten wirklich erlaubt sind

Liste für die betroffene Komponente die sichtbaren Werte auf: Name, Adresse, Rolle, Avatar, Status, Anzahl, Button-Text und die Liste selbst. Auch ein leerer Titel oder ein einzelner Treffer verändert die Darstellung.

Notiere pro Feld, woher es kommt, ob es fehlen darf und welche Grenze tatsächlich gilt. Ein Eingabefeld kann kürzere Texte zulassen als eine API oder ein Import. Deshalb reicht der Blick auf `maxLength` im Formular allein nicht. Kowalskis Ablauf sieht ausdrücklich den Abgleich mit Validierung, Datenbank und API-Vertrag vor.{q:1}

Ein Datenvertrag beschreibt dabei die vereinbarte Form und Bedeutung der Daten. Er beantwortet beispielsweise, ob `null` eine fehlende Rolle darstellt, ob ein leerer String erlaubt ist und ob eine Anzahl negativ werden kann.

Fehlt eine definierte Textgrenze, halte das als offene Produktentscheidung fest. Für den Layouttest wählst du zunächst einen glaubwürdigen langen Wert. Eine frei erfundene Zeichenfolge mit absurdem Umfang hilft wenig, wenn dein Produkt solche Eingaben schon vorher zurückweist.

## Eine kleine Fixture für eine Mitgliederliste

Das folgende JSON ist ein synthetisches Beispiel. Es setzt voraus, dass die Komponente Namen und E-Mail-Adressen als Text, eine optionale Rolle als `null` und nicht negative ganze Projektzahlen annimmt. Passe Feldnamen, Werte und zulässige Grenzen an deinen tatsächlichen Vertrag an.

```json
[
  {
    "name": "Elisabeth von Hohenberg-Schwarzhausen",
    "email": "elisabeth.hohenberg@projektkoordination.example",
    "role": null,
    "projectCount": 24680
  },
  {
    "name": "Q",
    "email": "q@team.example",
    "role": "QA",
    "projectCount": 1
  },
  {
    "name": "佐藤 杏奈",
    "email": "anna@team.example",
    "role": "Internationale Projektkoordination",
    "projectCount": 0
  }
]
```

Verteile die schwierigen Werte über mehrere Zeilen. So kannst du sehen, ob etwa eine Zeile mit mehrzeiligem Namen die danebenliegenden Avatare und Aktionen verschiebt. Ergänze je nach Zielgruppe Texte mit Akzenten, arabischer Schrift oder Emoji. Falls dein Produkt eine Darstellung von rechts nach links unterstützt, prüfe auch diese Richtung ausdrücklich.

Erzeuge zusätzlich eine leere Liste und eine Liste mit genau einem Mitglied. Für große Listen verwendest du einen Umfang, den das Produkt tatsächlich anzeigen oder laden soll. Eine paginierte Tabelle benötigt andere Fälle als eine Liste, die alle Einträge gleichzeitig rendert.

Auch Labels gehören dazu: „QA“ und „Internationale Projektkoordination“ stellen andere Anforderungen an dasselbe Badge. Bei Zahlen prüfst du Darstellung, Ausrichtung und Bedeutung. Ein fehlender Wert darf nur dann als null Projekte erscheinen, wenn das fachlich stimmt.

## Vergleiche dieselbe Oberfläche mit verschiedenen Inhalten

Lade die Fixture dort ein, wo die Komponente normalerweise ihre Daten erhält: als Props, über einen vorhandenen Mock oder über eine Entwicklungsroute. Props sind die Eingabewerte einer Komponente; ein Mock ersetzt für den Test eine echte Datenantwort.

Ein Umschalter zwischen Demo, schwierigen Daten, leerer Liste und einzelnem Eintrag erleichtert die Untersuchung. Halte ihn auf die Entwicklungsumgebung beschränkt. Ändere beim Wechsel ausschließlich den Datensatz. Handbearbeitetes HTML würde einen anderen Zustand erzeugen als der reguläre Datenfluss.{q:1}

Wähle die tatsächliche Containerbreite. Eine Liste in der Seitenleiste braucht diese schmale Breite auch im Test. Prüfe danach weitere unterstützte Größen und vergrößerten Text.

Der vorgeschlagene Vorher/Nachher-Vergleich läuft so: Lade zuerst die normale Fixture, dann die schwierige. Halte die störende Stelle fest. Nach einer gezielten Korrektur lädst du beide erneut unter denselben Bedingungen. Falls du Screenshots erstellst, gehören Datensatz, Fenstergröße und Zustand dazu. Hier wurden keine solchen Screenshots oder Testläufe durchgeführt.

## Dokumentiere den Fehler, bevor du die Darstellung entscheidest

Für jeden Fund reichen zunächst vier Angaben: auslösender Wert, betroffene Stelle, sichtbare Folge und gewünschtes Verhalten. Beispielsweise wäre „lange E-Mail-Adresse verdrängt das Menü“ ein sinnvoller Befund, wenn du ihn tatsächlich reproduziert hast.

Die Korrektur hängt vom Feld ab. Ein Name kann umbrechen. Eine sekundäre Rollenbeschreibung kann gekürzt werden, wenn der vollständige Inhalt erreichbar bleibt. Bei ähnlichen Dateinamen musst du möglicherweise das unterscheidende Ende erhalten. Zahlen, die verglichen werden sollen, brauchen genügend Platz.

Fehlende Werte brauchen ebenfalls eine bewusste Entscheidung. Eine leere Zeile für die Rolle, ein Platzhalter und das Weglassen der Rolle erzeugen verschiedene Zeilenhöhen. Definiere, was zu deiner Liste passt, und prüfe die übrigen Zustände danach erneut.

Ein Regressionstest schützt eine behobene Fehlfunktion vor späteren Änderungen. Dafür formulierst du ein beobachtbares Kriterium: Das Menü bleibt erreichbar, der vollständige Name ist lesbar oder der Leerzustand enthält die vorgesehene Aktion. Ein vorhandener Browsertest kann solche Kriterien übernehmen. Für reine Darstellungsfragen kann zusätzlich ein visueller Vergleich sinnvoll sein.

## Plane die Grenzen der Prüfung ein

Der Aufwand wächst mit Zuständen, Sprachen und unterstützten Layouts. Beginne deshalb mit der wichtigsten Komponente und Fällen, die ihre Nutzer tatsächlich erreichen können.

Ein Renderingtest untersucht die sichtbare Ausgabe. Er prüft weder vollständig den Weg vom Import bis zur Datenbank noch Sicherheit oder das Verhalten auf einem echten Handy. Für weitere Fehlerfälle kannst du den [Pre-Launch-Check](post:pre-launch-app-angreifen) ergänzen. Prüfe Touch, Tastatur und Browserleisten zusätzlich auf einem Zielgerät.

Nimm als nächsten Schritt eine bestehende Liste, erfasse ihren Datenvertrag und baue daraus eine kleine Fixture. Halte reproduzierte Fehler fest, entscheide das gewünschte Verhalten und korrigiere gezielt. So bleibt jeder Fix an eine konkrete Eingabe und ein überprüfbares Ergebnis gebunden.
