# Semantischer Factory-Pilot: Aussagen, Synthesen und Fähigkeitskandidaten

**Stand:** 2026-10-26 · **Umfang:** begrenzter kuratierter Pilot auf Basis gezielt geprüfter Originalstellen. Keine semantische Vollanalyse der Bibliothek und kein praktischer Factory-Vergleich.

## Ergebnis

Die erste Aussage-/Beziehungsschicht ist nutzbar: 24 Aussagen, 27 konkrete Belegbereiche aus zwölf Herkunftsfamilien, elf begründete Beziehungen, drei Quersynthesen und fünf Kandidatenkarten. Die Belege sind an Datei-/Bereichshashes und bei externen Repos an lokale Commitstände gebunden. Fremde Skills wurden gelesen und fachlich eingeordnet, nicht installiert oder aktiviert.

Der Abruf liefert relevante Aussagen, Voraussetzungen, Spannungen und Kandidaten gemeinsam. Bei geänderten oder fehlenden Belegen werden betroffene Aussagen und über deklarierte Abhängigkeiten auch Synthesen/Karten als prüfbedürftig erkannt. Ein betroffenes Kontextpaket hält die Aussagen und Kandidaten zurück. Die Karten werden aus der gemeinsamen Registry erzeugt; abweichende oder fehlende Ansichten werden erkannt.

## Bedienung

```powershell
python ai.py wissen pilot-check
python ai.py wissen kontext "Wie unterscheiden sich Grilling und To-spec sowie Tickets und Ausführungspläne?"
python ai.py wissen kontext "Wie bleibt Wissen aktuell?" --thema s-wissenspflege
python ai.py wissen karten --check
```

Die Befehle lesen die führenden Pilot-Dateien direkt. Der große Volltextkatalog wurde in dieser Stufe nicht neu aufgebaut. Neue Pilot-Dokumente erscheinen dort erst nach erneuter Indexierung; der Kontextabruf ist davon unabhängig. Der offene Gesamtprüfplan vom 25.10. bleibt ein historischer Snapshot und wurde nicht als bearbeitet markiert.

## Was der Quellenvergleich konkret ergänzt

**Klärung und Formulierung haben verschiedene Eingänge.** Grilling (`c13`) behandelt offene Entscheidungen. To-spec (`c21`) verdichtet ausreichend bekannten Kontext. Ein Agent soll zuerst den Eingangszustand erkennen, statt beide Anweisungen unterschiedslos zu vermischen. Beziehung `r05` enthält diese Bedingung.

**Tickets und Ausführungspläne haben verschiedene Lebenszyklen.** To-tickets vermeidet veraltende Dateipfade im Ticket (`c22`), pstack verlangt für große Ausführungspläne konkrete Dateien/Symbole (`c23`). Der eigene Entwurf hält Verhalten und Abnahme langfristig stabil und konkretisiert die zeitnahe Ausführung separat. Beziehung `r06` macht die Spannung abrufbar.

**Reviewachsen sind verschiedene Nachweise.** Spec- und Standards-Review (`c08`, `c09`, `c24`) bleiben getrennt. Laufzeitverifikation (`c14`, `c15`) ergänzt sie. Friedmans Argument (`c06`) verhindert die Überinterpretation, dass ein zweiter Agent allein schon eine unabhängige Abnahme garantiere.

**Mehr Belegzeilen sind nicht automatisch mehr unabhängige Quellen.** Rohtext und Source-Notiz von Friedman zählen als eine Familie; ebenso die beiden Darstellungen der ZazenCodes-Veröffentlichung (`c18`). Auch Spec- und Standards-Kandidat stammen aus derselben Originalanweisung von Matt Pocock. Familienzählung beweist weder Unabhängigkeit noch Richtigkeit.

## Sieben Fragen technisch geprüft

Die folgenden Checks prüfen die Ausgabe des echten CLI gegen vorab benannte Eigenschaften. Sie bewerten keine fertig formulierten Modellantworten und sind kein verblindeter Vergleich mit dem bisherigen Vorgehen.

| Eval-Frage | Erwartete Eigenschaft | Beobachtung |
|---|---|---|
| W01: Ablauf von Spec bis Verifikation | Ablauf-Synthese und Kandidatenverträge verfügbar | `s-ablauf`, fünf Kandidaten, 16 verbundene Aussagen |
| W03: Grilling/To-spec und Ticket/Plan unterscheiden | Beide bedingten Spannungen enthalten | `r05` und `r06` im Kontextpaket |
| W04: Rohquelle und Source als unabhängig zählen? | Herkunftsfamilien statt Belegzahl | `c06` und `c18` haben trotz mehrerer Belegstellen jeweils Familienzahl 1 |
| W06: Welche Skills dürfen aktiviert werden? | Kandidaten bleiben Kandidaten | Fünf Kandidaten, keine Aktivierung durch den Abruf |
| W07: Belege und Versionen prüfen | Explizite Themenwahl und aktuelle Belegprüfung | `s-wissenspflege` mit versionierten Fundstellen; Fehlerweitergabe zusätzlich in Fehlerfalltests geprüft |
| W11: Gesamter Wissensbestand bereits analysiert? | Scope darf keine Vollanalyse behaupten | `vollanalyse: false`, `wirksamkeit_gemessen: false` |
| W12: Kontext, Verifikation und Wissenspflege verbinden | Eigene Kombination als Ableitung erkennbar | Drei Synthesen zusammen, `c20` bleibt eigene Architekturhypothese mit Ursprungsaussagen |

Die vollständigen Kontextausgaben umfassen im technischen Smoke-Test ungefähr 40–55 KB JSON. Das ist eine gemessene Ausgabegröße, kein Nachweis geringerer Tokenkosten oder besserer Antworten. Die Mengen erklären, warum eine spätere Factory Inhalte passend zur Rolle auswählen und bei Bedarf vertiefen sollte.

## Beispiel einer daraus abgeleiteten Factory-Verbesserung

Ein späterer Job könnte vor dem Start seine verwendete Wissensversion, Anforderung und Prüfmethode festhalten. Ändert sich ein benötigter Beleg, wird zunächst seine Ableitung geprüft, bevor der Job auf dieser Grundlage weiterarbeitet. Das verbindet Kontextbereitstellung (`c01`/`c02`), versionierte Evidenz (`c03`/`c04`) und geschützte Abnahme (`c06`).

Das ist ein eigener Versuchsvorschlag. Der kleinste technische Test verändert eine Belegkopie und erwartet eine gesperrte betroffene Ableitung; dieser Mechanismus ist in den Tests abgedeckt. Der praktische Versuch muss anschließend zeigen, ob bei echten Aufgaben weniger falsche Entscheidungen oder menschliche Korrekturen entstehen und welche Kosten dafür anfallen.

## Checks und Grenzen

- Pilot-Check: alle 27 Belegbereiche im erfassten lokalen Stand auflösbar, Hashes und Repo-Revisionen passend, Ansichten konsistent.
- Fehlerfalltests: geänderte/fehlende Belege, Repo-Revision, Herkunftsfamilien, Ableitungs- und Voraussetzungsketten, Zyklen, Gegenargumente, Ansichtendrift, unbekannte Referenzen und Kandidatenstatus.
- Zentrale Abschlussprüfung: 36 gezielte Tests bestanden (elf Pilot-, acht Katalog- und 17 CLI-Tests), dazu erfolgreiche Syntax-, Markdown-Link- und Formatprüfungen.
- Knowledge-Validator: Baseline 53 Altfehler; nach Ergänzung unverändert. Bestehende Sources und Pattern-Belege wurden in dieser Stufe nicht verändert.

Die technische Frischeprüfung entdeckt weder jede neue Gegenquelle noch fachliche Veraltung bei unveränderten Eingängen. Uncommittete Änderungen außerhalb der benannten Belegdateien sind ebenfalls kein automatisch erkannter neuer Beleg. Erforderliche Abhängigkeiten müssen ausdrücklich aufgenommen werden. Die vollständige Bestandsanalyse und ein unabhängiger Vergleich tatsächlicher Antworten stehen weiterhin aus.

## Führende Dateien

- [Pilot-Registry und Bedienung](../80_Knowledge/Factory/README.md), [strukturierte Daten](../80_Knowledge/Factory/pilot.json)
- [Kontextbereitstellung](../80_Knowledge/Vergleiche/Factory-Kontextbereitstellung.md), [Spec–Build–Review](../80_Knowledge/Vergleiche/Factory-Spec-Build-Review.md), [Wissenspflege/Methodenauswahl](../80_Knowledge/Vergleiche/Factory-Wissenspflege-Methodenauswahl.md)
- [Fünf generierte Kandidatenkarten](../80_Knowledge/Faehigkeiten/README.md)
- [Pilot-Werkzeug](../70_Scripts/wissens_pilot.py), CLI-Anbindung in [ai.py](../ai.py), [Fehlerfalltests](../tests/test_wissens_pilot.py)
- [Originalstellen für die Methoden](2026-10-26-factory-pilot-methodenbelege.md), [Originalstellen für die Wissensmechanismen](2026-10-26-factory-pilot-wissensbelege.md)

Einstiege und Index wurden in `README.md`, `docs/wissensfabrik/`, `80_Knowledge/README.md`, `80_Knowledge/Index.md` und `70_Scripts/README.md` aktualisiert. Es gab keine Commits, Pushes, Deployments, externen Nachrichten oder Änderungen an der bestehenden Skill-Registry.
