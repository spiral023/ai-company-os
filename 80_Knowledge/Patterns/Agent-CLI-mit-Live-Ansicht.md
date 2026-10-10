# Agent-CLI-mit-Live-Ansicht

**Konfidenz:** meinung

## Zweck

Macht agentengestützte Bearbeitung von Inhalten für Menschen laufend anschaulich, ohne die Agent-Bedienung an dieselbe grafische Oberfläche zu binden. Relevant etwa für Kursmaterial oder andere Ergebnisse, deren sinnvolle Prüfung eine gerenderte Ansicht braucht.

## Funktionsweise

Der Agent erhält eine CLI für die Bearbeitung des jeweiligen Inhalts. Eine getrennte, automatisch aktualisierte Oberfläche stellt denselben Inhalt für den Menschen dar. Änderungen können dadurch programmatisch vorgenommen und anschließend in der geeigneten Darstellung betrachtet werden. Die Aktualisierung der Ansicht und die fachliche Freigabe sind dabei unterschiedliche Schritte.

## Vorteile

- Agent und Mensch nutzen jeweils passende Schnittstellen.
- Die Darstellung macht laufende Änderungen sichtbar.
- Das Grundmuster ist auf unterschiedliche Inhaltsarten übertragbar.

## Nachteile & Grenzen

- CLI und Ansicht müssen denselben Zustand abbilden; ein veraltetes Rendering kann eine falsche Rückmeldung geben.
- Die Quelle nennt keine Implementierungskosten, Fehlerquote oder gemessene Beschleunigung.
- Eine Live-Ansicht ersetzt weder inhaltliche Prüfung noch Tests des tatsächlichen Bearbeitungsverhaltens.
- Die nötigen Bearbeitungsrechte folgen der Aufgabe; umfassende Kontrolle ist kein Selbstzweck.

## Wann einsetzen, wann nicht

Geeignet, wenn Inhalte programmatisch bearbeitet werden können und die menschliche Prüfung eine laufend aktualisierte Darstellung braucht, etwa bei Kurserstellung. Der Aufwand für eine eigene Ansicht lohnt sich vor allem bei wiederkehrenden Aufgaben. Bei einzelnen einfachen Textänderungen zuerst prüfen, ob vorhandener Editor und Vorschau bereits ausreichen; der Post enthält keinen Kostenvergleich.

## Belege

- 2026-07-23 · [[2026-07-23-mattpocockuk-2080277204970143986]] · meinung — Matt Pocock beschreibt CLI-Bearbeitung durch einen Agenten und eine eigene Live-Ansicht für den Menschen, eingesetzt bei Kurserstellung. Persönlicher Praxisbericht ohne bereitgestellte Implementierung oder Vergleichsmessung.

## Spannungen & offene Fragen

- Die Trennung der Schnittstellen ist nur hilfreich, wenn Änderungen zuverlässig in der Ansicht ankommen. Wie Aktualität und Vollständigkeit geprüft werden, bleibt in der Quelle offen.
- Sichtbarkeit ist kein Abnahmenachweis: Die menschliche Prüfung muss weiterhin erklären, welche Eigenschaften sie bewertet.

## Verwandte Patterns

- [[Visuelle-Abnahme-mit-Live-Lokal-Vergleich]]
- [[Agent-generierte-Schulung-mit-Curriculum-Gate]]
