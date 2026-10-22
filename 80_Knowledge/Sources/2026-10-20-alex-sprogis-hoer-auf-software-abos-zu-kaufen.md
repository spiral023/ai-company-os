---
url: https://www.youtube.com/watch?v=DN7bHOVmE88
autor: "Alex Sprogis"
datum: 2026-10-20
erfasst: 2026-10-22
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-10-20-alex-sprogis-hoer-auf-software-abos-zu-kaufen.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Produktbrief, Design-Prototyp und Feature-Spezifikationen bilden getrennte Entscheidungsstufen

Alex Sprogis erläutert am `20.10.2026` die Entwicklung einer persönlichen `macOS`-Menüleisten-App für Systemübersicht, Speicherbereinigung und Shortcuts. Grundlage dieser Notiz sind die vollständig erfassten, automatisch erzeugten deutschen Untertitel und die Videobeschreibung; eine vollständige Hör- oder Bildprüfung liegt nicht vor. Die Quelle beschreibt einen Demoablauf, keinen gemessenen allgemeinen Kosten- oder Qualitätsvorteil gegenüber gekaufter Software.

## Der Produktbrief grenzt das Vorhaben ein

Vor der Implementierung entsteht ein eigenständiges Briefing mit Zielgruppe, Plattform, Funktionen und ausdrücklich ausgeschlossenen Aufgaben. Die Nicht-Ziele sollen verhindern, dass der Agent mehr baut als für den konkreten Bedarf nötig ist. Das Dokument hält damit Produktentscheidungen außerhalb des flüchtigen Chatverlaufs fest.

Sprogis nutzt nach eigener Darstellung den „Grill me“-Skill von Matt Pocock, um fehlende Antworten gemeinsam zu erarbeiten. Das Interview soll ein geteiltes Verständnis herstellen, bevor aus vagen Vorstellungen technische Entscheidungen werden. Ein Briefing ist dabei noch keine vollständige Spezifikation: Es benennt den Rahmen, nicht jede Interaktion und jeden Sonderfall.

## Der Design-Prototyp klärt Aussehen vor Produktionscode

Auf Inspiration und Briefing folgt ein Prototyp in dem im Beitrag genannten `Claude Design`. Sein Zweck ist die Erprobung des Aussehens und grober Funktionen. Der dabei erzeugte Code ist laut Quelle zunächst nachrangig; er wird nicht als bereits geeignete Grundlage der nativen Anwendung ausgewiesen.

Die Reihenfolge soll vermeiden, eine weit entwickelte App später wegen ungeklärter Gestaltung vollständig umzustrukturieren. Der Prototyp trägt somit eine andere Entscheidung als das Briefing: Er konkretisiert die Oberfläche, ohne bereits alle Anforderungen an tatsächliches Systemverhalten abzudecken. Ob diese Vorarbeit im Beispiel Nacharbeit eingespart hat, wird nicht vergleichend gemessen.

## Feature-Spezifikationen machen Annahmen und Prüfungen sichtbar

Briefing und Prototyp werden anschließend in einzelne Features heruntergebrochen. Für jedes Feature sollen schriftliche Anforderungen festhalten, welche Funktion vorhanden sein muss, wie Details zusammenwirken und wie sich das Ergebnis prüfen lässt. Auch seltene Sonderfälle gehören hinein. Diese Dokumente bilden eine zentrale, nachvollziehbare Referenz für die Zusammenarbeit, statt Entscheidungen immer wieder aus Code oder Chat rekonstruieren zu müssen.

Sprogis bezeichnet die Spezifikation als „Vertrag“ mit dem Agenten. Gemeint ist ein abgestimmter Arbeitsmaßstab: Der Mensch prüft die inhaltlichen Anforderungen, bevor der Agent die Umsetzung übernimmt. Eine konkrete Ordnerstruktur oder ein vollständiges Spezifikationstemplate ist im archivierten Text nicht enthalten; der verkürzt angezeigte externe Link wird hier nicht ergänzt.

Die Quelle unterscheidet persönliche Experimente von Software für weitere Nutzer. Zugleich begründet Sprogis auch bei seiner privaten App einen höheren Detailgrad mit den Folgen von Dateilöschung, Cachebereinigung und automatischen Empfehlungen. Damit folgt der Prüfbedarf nicht nur der Nutzerzahl, sondern auch der Tragweite der Funktionen.

## Architektur, Umsetzung und unabhängige Prüfung anschließen

Nach der Anforderungsklärung plant Sprogis zusätzlich Architektur und Aufgabenreihenfolge. Ein separater Prüfagent soll die Ergebnisse untersuchen und einen Testbericht mit Bugs liefern; der Beitrag stellt diese zusätzliche Qualitätssicherung als optionalen Ausbau vor. Am Ende bleibt der Abgleich zwischen geplanter und tatsächlich umgesetzter Funktion.

Für das native Beispiel nennt er `Xcode` und `Swift`, außerdem Coding Agents und seine Nutzung von `T3 Code`. Das sind datierte Werkzeugangaben des Beispiels. Der pauschale Beschreibungstext mit `Next.js`, `Tailwind`, `Supabase` und Hosting-Werbung belegt nicht, dass diese Komponenten den Stack der nativen App bilden.

## Einordnung

Übertragbar ist die Trennung von Produktumfang, gestalteter Oberfläche, prüfbaren Feature-Anforderungen und Implementierung. Dokumente erleichtern den Abgleich, erzwingen aber weder ihre eigene Aktualität noch korrekte Ausführung. Gerade Löschfunktionen benötigen belastbare Verhaltensnachweise; ein Prototyp oder Agentbericht allein belegt deren sichere Umsetzung nicht. Die Demo zeigt keine unabhängige Abnahme der App und keinen kontrollierten Vergleich des Vorgehens. Der Titel zur Abobefreiung sowie Werbung für Blueprint, Kurs und Hosting tragen keine allgemeine Wirtschaftlichkeitsaussage. Aussagen über das weitgehend selbstständige Erledigen des Rests werden deshalb nicht als Qualitätsgarantie übernommen.

## Kernaussagen

- [[Spec-Grilling]]: Das Produktinterview klärt Zielgruppe, Plattform, Funktionen und Nicht-Ziele vor der Umsetzung.
- [[Spec-Ordner-pro-Feature]]: Detaillierte Anforderungen einschließlich Sonderfällen und Prüfungen schaffen eine dauerhafte Referenz; die Quelle verlangt nicht das konkrete Dateiset des Patterns.
- [[Plan-first-mit-getrenntem-Review]]: Briefing, Design-Prototyp, Feature-Planung, Umsetzung und unabhängige Ergebnisprüfung tragen unterschiedliche Entscheidungen.

## Verbindungen

- [[2026-07-06-alex-sprogis-claude-design-2-0-ist-der-wahnsinn-kompletter-gu]] – frühere Quelle zur Design-Erprobung.
- [[2026-10-07-alex-sprogis-t3-code-endlich-eine-steuerzentrale-fuer-alle-de]] – Werkzeugkontext zur später genannten Arbeitsoberfläche.
