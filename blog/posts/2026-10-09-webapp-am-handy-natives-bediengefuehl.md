---
titel: "Warum sich deine Webapp am Handy noch falsch anfühlt"
datum: 2026-10-09
kategorie: arbeitsweisen
zusammenfassung: "Prüfe deine Webapp am Handy auf klebende Hover-Zustände, Browserleisten, Bildschirmtastatur und verdeckte Buttons. Gezielte CSS-Beispiele und ein Hardware-Prüfablauf helfen dir, die tatsächlichen Bedienprobleme einzugrenzen."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-10-04-emilkowalski-2106752670405099523
  - 2026-10-09-repo-emilkowalski-mobile-native
---

## Kurz gesagt

- Begrenze Hover-Effekte anhand der Eingabefähigkeiten und gib Buttons ein sichtbares Drückfeedback.
- Prüfe die Höhe deiner App mit Browserleisten und geöffneter Bildschirmtastatur getrennt.
- Halte Zoom und Textauswahl für Inhalte verfügbar. Passe Touch-Regeln nur an den betroffenen Steuerelementen an.
- Teste den wichtigsten Ablauf auf einem echten Handy, einschließlich Scrollen, Formular und gegebenenfalls installierter PWA.

## Suche nach dem konkreten Bedienproblem

Ein Button bleibt nach dem Tippen hervorgehoben. Der Speichern-Button verschwindet hinter der Tastatur. Beim Scrollen bewegt sich plötzlich die Seite hinter einem Dialog. Solche Fehler stören schon dann, wenn Farben, Abstände und Animationen gut aussehen.

Emil Kowalskis Skill `/mobile-native` sammelt dafür Prüfungen und Anpassungen rund um Touch, Bildschirmhöhe, sichere Ränder und echte Geräte. Der Name beschreibt ein angestrebtes Bediengefühl. Die Arbeit bleibt eine Prüfung und Anpassung der Webapp; eine Umwandlung in eine Native-App gehört nicht zum beschriebenen Ablauf.{q:1}

Starte mit einem Symptom, das du reproduzieren kannst. Ein pauschaler Auftrag wie „mach es nativer“ lädt zu Änderungen ein, deren Nutzen du anschließend schwer beurteilen kannst. Schreib stattdessen auf, bei welcher Aktion welches Element falsch reagiert.

## Hover braucht einen passenden Eingabemechanismus

Ein schmaler Bildschirm sagt wenig darüber aus, ob jemand mit einem Finger, einer Maus oder einem Trackpad arbeitet. Geräte können mehrere Eingabearten kombinieren.

Mit `(hover: hover)` fragst du ab, ob der primäre Eingabemechanismus bequem über einem Element schweben kann. `(pointer: fine)` ergänzt die Präzision des primären Zeigegeräts. Diese Fähigkeiten passen besser zum Hover-Effekt als eine Abfrage der Bildschirmbreite. Auf Geräten mit mehreren Eingabearten bleibt eine praktische Prüfung sinnvoll. [MDN erklärt die Hover-Abfrage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover).{q:2}

Dieses CSS ist ein Vorschlag für einen Button. `--button-hover` steht für einen bereits vorhandenen Farbwert deines Projekts. Die Fokusmarkierung bleibt für Tastaturbedienung sichtbar.

```css
.action {
  touch-action: manipulation;
}

.action:active {
  transform: translateY(1px); /* sichtbares Drückfeedback */
}

.action:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

@media (hover: hover) and (pointer: fine) {
  .action:hover {
    background: var(--button-hover);
  }
}
```

`touch-action: manipulation` erlaubt Scrollbewegungen und Pinch-Zoom, also Vergrößern mit zwei Fingern. Es schaltet jedoch die zusätzliche Geste zum Vergrößern per Doppeltippen ab. Setze die Regel deshalb gezielt ein und prüfe die Wirkung. [MDN beschreibt die erlaubten Gesten](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/touch-action).{q:2}

Entferne Hover weder pauschal noch als einzige Rückmeldung. Eine Aktion braucht auch beim Antippen erkennbares Feedback. Falls du die Browserhervorhebung eines Links oder Buttons abschwächst, muss die eigene Rückmeldung diesen Zustand zuverlässig zeigen.

## Bildschirmhöhe und Tastatur sind getrennte Fälle

Der Viewport ist der Bereich, den der Browser für die Seite bereitstellt. Am Handy verändert sich dieser Bereich durch ein- und ausfahrende Browserleisten.

`vh` orientiert sich derzeit an der großen Viewporthöhe. Dadurch kann ein bildschirmfüllendes Layout bei sichtbarer Browserleiste mehr Platz beanspruchen als sichtbar ist. `dvh` folgt der dynamischen Höhe; `svh` verwendet die kleine, stabile Variante. Mit `dvh` kann sich die Größe beim Scrollen verändern. [MDN erläutert die Viewport-Einheiten](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length).{q:2}

Für eine App-Hülle könntest du diesen Ausgangspunkt prüfen:

```css
.app {
  min-height: 100vh;  /* Fallback für ältere Zielbrowser */
  min-height: 100dvh;
}
```

`min-height` erlaubt dem Inhalt, darüber hinaus zu wachsen. Eine fest vorgegebene Höhe kann bei langen Inhalten zusätzliche Scrollcontainer erforderlich machen. Welche Variante passt, entscheidet die Struktur deiner App.

Die Bildschirmtastatur behandelt der Browser gesondert. Sie kann den sichtbaren Ausschnitt verkleinern, während die Layoutgröße bestehen bleibt. `dvh` allein garantiert deshalb keinen erreichbaren Button über der Tastatur. Der Viewport-Parameter `interactive-widget` kann dieses Verhalten in unterstützenden Browsern beeinflussen. Prüfe die Unterstützung und den tatsächlichen Ablauf deiner Zielgeräte. [MDN beschreibt die Tastaturwirkung auf den Viewport](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport).{q:2}

Teste ein Formular mit dem letzten Eingabefeld: Fokus setzen, Text schreiben, zur nächsten Eingabe wechseln und speichern. Bleiben Feld, Fehlermeldung und Aktion erreichbar? Prüfe auch, ob der Browser beim Fokussieren hineinzoomt. Gut lesbare Eingabeschrift ist ein sinnvoller erster Ansatz. Begrenze den Zoom dafür nicht mit `user-scalable=no` oder `maximum-scale=1`.

## Sichere Ränder brauchen zusätzlich normale Abstände

Bei einer randfüllenden Darstellung können Aussparungen und der Bereich der Systemgesten wichtige Inhalte verdecken. Mit `viewport-fit=cover` nutzt die Seite den Bildschirm bis zum Rand. Anschließend berücksichtigt gezieltes Padding die Safe Areas: die vom System vorgesehenen Randbereiche. [WebKit zeigt das Zusammenspiel](https://webkit.org/blog/7929/designing-websites-for-iphone-x/).{q:2}

Dieses Beispiel ist für eine untere Aktionsleiste gedacht. Prüfe auch seitliche Abstände im Querformat.

```html
<meta name="viewport"
      content="width=device-width, initial-scale=1, viewport-fit=cover">
```

```css
.bottom-actions {
  padding: 1rem;
  padding-bottom: calc(1rem + env(safe-area-inset-bottom, 0px));
  padding-left: max(1rem, env(safe-area-inset-left, 0px));
  padding-right: max(1rem, env(safe-area-inset-right, 0px));
}
```

Das zusätzliche Padding betrifft die Leiste. Verteile dieselbe Randkorrektur nicht ungeprüft auf verschachtelte Container, sonst summieren sich die Abstände. Sichere Ränder ersetzen außerdem keine Prüfung bei geöffneter Tastatur.

## Scrollen und langes Drücken gezielt untersuchen

Scrolle einen Dialog bis zum oberen und unteren Ende. Bewegt sich dabei die Seite dahinter? Eine lokale Regel wie `overscroll-behavior: contain` kann verhindern, dass Scrollbewegungen an einen übergeordneten Bereich weitergereicht werden. Prüfe dabei, welche Gesten dein Produkt weiterhin anbieten soll.

Globale Scrollsperren oder `touch-action: none` können Bedienmöglichkeiten nehmen. Für einen horizontalen, regulär scrollbaren Bereich ist die eingebaute Browserbewegung häufig ein sinnvoller Ausgangspunkt. Eigene Drag-Gesten benötigen zusätzliche Entscheidungen zu Richtung, Abbruch und Zoom.

Halte auch länger auf einen Button und auf kopierbare Inhalte gedrückt. Du kannst die Auswahl des Button-Labels gezielt unterbinden. Adressen, Fehlermeldungen und Bestellnummern sollten weiterhin auswählbar bleiben. Eine globale `user-select: none`-Regel auf dem gesamten Dokument ist dafür ungeeignet.

## Prüfe einen vollständigen Ablauf auf echter Hardware

Wähle einen wichtigen Ablauf: suchen, Ergebnis öffnen, Formular bearbeiten, speichern und zurückkehren. Führe ihn zuerst mit sichtbaren Browserleisten aus, dann nach dem Scrollen und mit geöffneter Tastatur. Wiederhole die relevanten Schritte im Querformat.

Wenn deine mobile Webapp als PWA installiert werden soll, prüfe auch diesen Modus. Eine PWA ist eine Webapp, die der Browser je nach Plattform mit App-Funktionen wie Installation ergänzt. Darstellung und verfügbare Browseroberflächen können sich dabei unterscheiden.

Die Geräteansicht am Desktop hilft beim Layout. Für Tastatur, tatsächliche Touch-Reaktion und die Bedienung mit dem Daumen brauchst du ein echtes Gerät. Halte Browser, Gerät, Zustand und Reproduktionsschritte fest. Der beschriebene Ablauf ist ein Vorschlag; hier wurde keine Handy-Abnahme durchgeführt.

Beginne mit dem störendsten Symptom und prüfe jede Änderung im selben Ablauf erneut. Plane dafür Zugriff auf deine Zielgeräte ein. Wie vertraut die Bedienung wirkt, musst du auf diesen Geräten beurteilen. Eine mobile Bedienprüfung ersetzt außerdem keine vollständige Prüfung der Barrierefreiheit. Schwierige Inhalte brauchen zusätzlich den [UI-Test mit langen Namen, leeren Listen und großen Zahlen](post:ui-mit-schwierigen-daten-testen).
