# Videoanalyse mit Frames und Transkript

**Konfidenz:** meinung

## Zweck

Visuelle Quelleninformationen zeitlich prüfen: Diagramme, UI-Wechsel und stumme Handlungen können im Transkript fehlen oder ohne passenden Bildbeleg falsch zugeordnet werden.

## Funktionsweise

Stand der Ausarbeitung: 2026-10-11. Das Tutorial vom 2026-06-07 kombiniert ein zeitmarkiertes Transkript mit verteilten Bildframes. Aus der Frage und dem relevanten Zeitbereich ergeben sich Kandidatenstellen; unabhängige Frame-Stichproben können auch visuelle Ereignisse ohne gesprochenen Hinweis entdecken.

An Kandidatenstellen wird der tatsächliche Bildinhalt geprüft. Passt ein Ausschnitt nicht zum vermuteten Diagramm oder UI-Zustand, werden benachbarte Frames nachgezogen. Ergebnisse erhalten Quelle, Zeitmarke und passenden Bildbezug; beobachtete Inhalte und Schlussfolgerungen bleiben unterscheidbar.

Die Methode ist eine Quellenanalyse vor einer möglichen Skill-Ableitung. Gegenüber einem einzelnen Screenshot ergänzt sie die zeitliche Folge. Die dargestellte Technik ist zugleich eine Stichprobe: Eine spätere technische Beschreibung begrenzter Frames trägt kein Versprechen vollständiger Videosichtung.

## Vorteile

- Erschließt visuelle und stumme Abläufe zusätzlich zur gesprochenen Erklärung.
- Bildbezüge und Zeitmarken machen Aussagen nachprüfbar.
- Nachziehen benachbarter Frames kann eine unpassende Einzelzuordnung korrigieren.

## Nachteile & Grenzen

- Grobe oder budgetbegrenzte Stichproben können kurze Ereignisse vollständig verpassen.
- ASR, Zeitmarken und visuelle Detailerkennung können falsch sein.
- Ohne passende Vergleichsdaten erklären sichtbare Hooks oder Schnitte keine hohen Abrufzahlen.
- Die hier ausgewertete Rohquelle enthält keine auswertbaren Demo-Frames; die dargestellte Erkennung wurde nicht unabhängig nachgemessen.

## Wann einsetzen, wann nicht

- Einsetzen: für bebilderte Wissensnotizen, stumme Bedienabläufe und zeitlich begrenzte Bug-Aufnahmen.
- Nicht einsetzen: als Vollständigkeitsnachweis oder für kritische Detailaussagen ohne Prüfung der betreffenden Szene.

## Belege

- 2026-06-07 · [[2026-06-07-julian-ivanov-ki-automat-so-laesst-du-claude-jedes-video-fuer-dich-anscha]] · meinung — Beschreibt Transkript, unabhängige Frame-Stichproben und Nachprüfung benachbarter Zeitpunkte für Wissensnotizen und Bug-Aufnahmen. Die Erkennung wurde hier nicht gegen sämtliche Videoereignisse geprüft.

## Spannungen & offene Fragen

- 2026-10-11: Die einleitende Vollständigkeitsbehauptung steht in Spannung zur später beschriebenen begrenzten Frame-Stichprobe. Lokales Nachziehen verbessert die Zuordnung, garantiert aber keine vollständige Ereignismenge.
- 2026-10-11: Welche Stichprobe genügt für den konkreten Zweck, und welche Aussagen erfordern anschließend die direkte Sichtung einer Szene?

## Verwandte Patterns

- [[Screenshot-als-Spezifikationsmedium]]
- [[Skill-aus-Demonstration-statt-Beschreibung]]
- [[Wissenspflege-mit-Inbox-und-Review]]
