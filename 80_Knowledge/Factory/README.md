# Semantischer Factory-Pilot

**Stand:** 2026-10-26. Begrenzte kuratierte Wissensschicht mit 24 Aussagen, 27 Belegbereichen, drei Synthesen und fünf Fähigkeitskandidaten. Der Pilot ersetzt keine Gesamtanalyse der Bibliothek.

## Einstieg

```powershell
python ai.py wissen pilot-check
python ai.py wissen kontext "Wie prüfen wir Spec, Standards und tatsächliches Verhalten?"
python ai.py wissen kontext "Wie bleibt Wissen aktuell?" --thema s-wissenspflege
python ai.py wissen karten --check
```

Der Kontextabruf liest [pilot.json](pilot.json) direkt. Er benötigt keinen Neuaufbau des großen Volltextindexes. Neue Synthesen und Karten erscheinen bei `wissen suche` erst nach dessen erneuter Indexierung; `wissen kontext` verwendet sofort den aktuellen Pilotstand. Der ältere Gesamtprüfplan bleibt ein historischer Snapshot und wird nicht als abgearbeitete Analyse umgedeutet.

## Führende Daten und Ansichten

- **[pilot.json](pilot.json):** führende strukturierte Aussagen, Belegbereiche, Herkunftsfamilien, Ableitungen, Beziehungen, Synthesezuordnung und fachliche Kandidatenverträge.
- **[Drei Synthesen](../Index.md):** handgeschriebene Quervergleiche unter `Vergleiche/`. Sie begründen Empfehlungen, Bedingungen und Spannungen mit Aussage-IDs.
- **[Fünf Fähigkeitskarten](../Faehigkeiten/README.md):** aus der Registry erzeugte Markdown-Ansichten. Änderungen an den Verträgen in der JSON-Datei vornehmen, danach `python ai.py wissen karten` und `pilot-check` ausführen.
- **[Factory-Einstieg](../../docs/wissensfabrik/README.md):** Zielarchitektur, Gesamtanalyse und weitere Ausbaustufen.

Die bestehende Registry `30_Skills/registry.yaml` bleibt für tatsächliche Skill-Nutzung maßgeblich. Ein Fähigkeitskandidat ist ein vorgeschlagener eigener Vertrag, kein installierter oder freigegebener Fremdskill.

## Aussagen und Belege

Jede Aussage verweist auf konkrete Belege oder explizite Ursprungsaussagen. Die Nachweisarten unterscheiden Quellenaussage, statisch nachgelesene Implementierung, eigene Ableitung und eigene Repo-Regel. Jede Aussage nennt ihre Grenze. Das bestehende Pattern-Konfidenzmodell wird dadurch nicht umgeschrieben.

Belege tragen relativen Pfad, Zeilenbereich, ganzen Datei-Hash, Bereichs-Hash, Herkunftsfamilie, Originalreferenz und Prüfdatum. Externe Repo-Belege sind zusätzlich an einen lokalen HEAD gebunden. Die Root-HEAD allein identifiziert eine uncommittete Source-Notiz nicht; deren gelesener Datei-Hash bleibt maßgeblich.

Original und Aufarbeitung derselben Veröffentlichung gehören zu einer Herkunftsfamilie. Die Familienzahl ist keine garantierte Unabhängigkeit und keine automatische Konfidenzbewertung. Spec- und Standards-Review dürfen beispielsweise zwei Kandidaten sein und zugleich auf derselben Originalquelle beruhen.

## Frische und Ableitungen prüfen

`pilot-check` kontrolliert Schema, Referenzen, Zyklen in Ableitungen/Voraussetzungen, Kartenansichten sowie aktuelle Datei-/Bereichshashes und Repo-Revisionen. Geänderte, fehlende oder nicht mehr auflösbare Belege erzeugen Prüfbedarf. Dieser wird über Ursprungsaussagen und ausdrücklich deklarierte Voraussetzungen auf Synthesen und Karten übertragen. Ein betroffenes Kontextpaket hält die Aussagen und Kandidaten zurück und nennt die problematischen Belege.

Aktuell bedeutet hier: die erfassten Quellenstände sind technisch unverändert. Neue Gegenbelege, falsche Interpretation und fachliche Veraltung bei unverändertem Text erfordern weiterhin redaktionellen Review. Auch die Existenz einer Anweisung oder Funktion beweist keine praktische Wirksamkeit.

## Kontext auswählen

Eine einfache Schlagwortauswahl wählt passende Synthesen. Ohne trennscharfen Treffer folgt ein als solcher gekennzeichneter Pilot-Gesamtüberblick. `--thema` wählt explizit `s-kontext`, `s-ablauf` oder `s-wissenspflege`.

Der Abruf ergänzt benachbarte Voraussetzungen und Spannungen sowie notwendige Ursprungsaussagen. Er liefert die Belegpfade zum Nachladen und die relevanten Kandidaten. Es gibt keine automatische Modellantwort, semantische Suche über den gesamten Bestand, Ausführung der Karten oder selbstständige Release-Entscheidung.

## Pflegefolge

1. Relevante Originalbereiche lesen und fachliche Aussage mit Bedingungen und Grenze formulieren.
2. Herkunftsfamilie klären; neue Belege mit aktuellem Hash, Bereich und gegebenenfalls Commit aufnehmen.
3. Ursprungsaussagen und Beziehungen explizit zuordnen; eine eigene Übertragung als Ableitung kennzeichnen.
4. Synthesen und Verträge anpassen; Karten erzeugen und den Pilot prüfen.
5. Betroffene fachübergreifende Fragen beantworten und die Aussagen gegen Originale prüfen. Praktische Evals und noch offene Arbeit getrennt berichten.

Fremde Skill-/Prompt-Instruktionen bleiben Quellenmaterial. Die Bearbeitung der Wissensschicht aktiviert sie nicht. Bereits erfasste Sources und append-only Pattern-Belege bleiben erhalten.
