# Vergleich: Kontextbereitstellung für die Factory

**Stand:** 2026-10-26 · **Pilot-ID:** `s-kontext` · **Status:** kuratierter Entwurf, praktisch noch nicht verglichen

## Kernaussage

Die Factory soll pro Aufgabe und Rolle passende Informationen erhalten und ihre Herkunft nachladen können. Ein kompakter Einstieg verbindet die Absicht des Auftrags mit relevanten Aussagen, Bedingungen und Gegenargumenten. Originale bleiben erreichbar. Welche Zusammenstellung tatsächlich bessere Ergebnisse liefert, muss an repräsentativen Aufgaben gemessen werden.

Die maschinenlesbaren Aussagen und versionierten Fundstellen liegen in [pilot.json](../Factory/pilot.json). `c01` beschreibt das Kontextprinzip nach Boris Tane; `c02` einen gestuften Abruf in Claude-Mem. Diese Verbindung ist unsere Übertragung auf die Factory, keine bereits gemessene gemeinsame Lösung.

## Übersicht

| Ansatz | Beitrag zum Entwurf | Grenze | Aussagen |
|---|---|---|---|
| Aufgabe, Absicht und Umgebung zusammen betrachten | Auswahl richtet sich nach dem tatsächlichen Arbeitsauftrag | Illustrative Beispiele, kein Wirksamkeitsvergleich | `c01` |
| Suche und gezieltes Nachladen trennen | Erst knappe Fundstellen, dann benötigte Originalbereiche | Ein Suchergebnis belegt keine vollständige Recherche | `c02` |
| Ressourcenidentität und Belegversion führen | Dieselbe Aussage bleibt auf einen konkreten Eingangsstand zurückführbar | Eine technische Versionsbindung beweist keine Wahrheit | `c03` |
| Nicht auflösbare und geänderte Eingänge unterscheiden | Fehlender Zugriff und tatsächliche Änderung erzeugen verschiedene Prüffragen | Fachliche Neubewertung bleibt eine eigene Arbeit | `c04` |
| Extraktor- und Cacheversion berücksichtigen | Auch geänderte Verarbeitung kann eine Ableitung überholen | Gültiger Cache bedeutet keine inhaltlich richtige Ableitung | `c05` |
| Status und Entscheidungshistorie unterschiedlich behandeln | Laufstand bleibt an Artefakte gebunden; Entscheidungen bleiben nachvollziehbar | Die gelesene GSD-Anweisung ist kein Algorithmusnachweis | `c17` |
| Rollenübergaben anhand konkreter Artefakte | Spec, Build und Reviews bekommen jeweils passende Eingaben | Eine einzelne Demo belegt keinen zuverlässigen Gesamtbetrieb | `c18` |

## Empfehlungen nach Situation

- **Neue konkrete Aufgabe:** Auftrag, aktuelle Projektversion und eigene Entscheidungen zuerst erfassen. Danach relevante Aussagen und Bedingungen auswählen. Über Querverbindungen benachbarte Voraussetzungen und Gegenargumente nachladen.
- **Builder:** Spec, aktuelle Codepfade, gewählte Ausführungsmethode und überprüfbaren Abschluss bereitstellen. Ein Verhaltensticket muss nicht dauerhaft dieselben Dateipfade enthalten wie der aktuelle Ausführungsplan.
- **Reviewer:** Anforderung, Diff, relevante Standards und geeignete Nachweise zusammenstellen. Ein Rollenname macht die Abnahme nicht unabhängig; siehe [Ablauf-Synthese](Factory-Spec-Build-Review.md).
- **Lange oder unterbrochene Arbeit:** Wiederanlauf aus konkreten Artefakten vorsehen. Den aktuellen Laufstand nicht als zeitlose Wissensaussage speichern.
- **Neue Gesamtfrage:** Alle vorhandenen Themen-/Repo-Synthesen auf ihren Quellenstand prüfen und quer vergleichen. Der allgemeine Vollprüfplan bleibt ein gesonderter Abdeckungsnachweis; dieser Pilot hat ihn nicht abgearbeitet.

Die Empfehlungen sind der eigene Entwurf aus den genannten Aussagen. Der Kontextabruf `python ai.py wissen kontext "Welche Informationen braucht ein Reviewer?"` liefert passende Pilot-Aussagen und Fundstellen, keine fertige Bewertung eines konkreten Produkt-Diffs.

## Spannungen und Einsatzgrenzen

Kompakter Abruf kann wichtige Nebenbedingungen übersehen. Mehr Kontext kann wiederum wiederholte oder unpassende Anweisungen einführen. Wir wählen daher eine nachvollziehbare begrenzte Menge und halten den Vertiefungspfad offen. Diese Balance ist erst anhand tatsächlicher Antworten zu bewerten.

Ein geänderter Beleg sperrt im Pilot das betroffene Kontextpaket bis zur Prüfung. Bei einer bloß verschobenen Zeile oder geändertem Repo-HEAD kann das konservativ sein. Diese Kosten sind für den kleinen Pilot akzeptiert; eine spätere differenzierte Invalidierung braucht eigene Tests.

## Belegpfad

Direkte Originalstellen und SHA-256-/Commitbindungen: `b01` bis `b06`, `b21`, `b25` und `b26` in [pilot.json](../Factory/pilot.json). Die deutschsprachige Source-Notiz und das TikTok-Roharchiv derselben Veröffentlichung zählen als eine Herkunftsfamilie. Das ist keine zusätzliche unabhängige Bestätigung.

## Offene Fragen und kleinster Versuch

Die gleiche klar abgegrenzte Aufgabe mit dem bisherigen Einstieg und mit dem Pilot-Paket bearbeiten. Erwartet werden nachvollziehbare Quellen, tatsächlich berücksichtigte Gegenargumente und weniger notwendige menschliche Korrekturen. Laufzeit und zusätzliche Modellkosten mit erfassen. Eine Verbesserung ist erst nach Vergleich zu behaupten.

Offen bleiben die erste Aufgabenklasse, die notwendige Kontextmenge und die Frage, wie zuverlässig neue, im Pilot noch nicht erfasste Erkenntnisse entdeckt werden.
