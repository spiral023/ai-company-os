---
titel: "UI mit Agenten bauen: Referenzbild vorab, benannte Design-Operationen, Audit im Browser"
datum: 2026-10-02
kategorie: arbeitsweisen
zusammenfassung: "Ein Workflow in fünf Schritten für Oberflächen mit Coding Agents: Referenzbild als Spezifikation, benannte Design-Operationen statt „mach es schöner“, ein Design-Reference-Skill und ein UX-Audit, bei dem der Agent die Seite im Browser bedient."
status: freigegeben
geprueft_am: 2026-10-02
quellen:
  - 2026-09-19-voxyz_ai-2101295246659182978
  - 2026-09-20-voxyz_ai-2101657631249031507
  - 2026-09-21-voxyz_ai-2102050225443766571
  - 2026-09-09-alex-sprogis-so-erstellst-du-interaktive-architektur-diagramm
  - 2026-02-15-avid-ai-design-workflow-2026
---

## Kurz gesagt

- Lass den Agenten zuerst ein Referenzbild der Seite erzeugen und setze erst danach Code um. Das Bild ist die Spezifikation für das Codemodell.{q:1}
- Ersetze „mach es schöner“ durch benannte Operationen wie bolder, distill oder polish.{q:2}
- Leg Komponentenquelle, Auswahlkriterien und Prüfschritt einmal in einem Skill ab, damit du nicht in jedem Auftrag Links und Regeln wiederholst.{q:3}
- Zum Schluss bedient ein Audit-Skill die Seite im Browser als Erstnutzer und liefert Reproduktionsschritte, Screenshots und konkrete Fixes.{q:3}

## Das Problem

Ein Coding Agent baut eine Seite, die funktioniert und trotzdem beliebig aussieht. Die übliche Reaktion ist ein Nachsatz wie „mach es moderner“. Der Agent rät dann, was gemeint ist, und ändert Farben oder Abstände ohne erkennbare Richtung. Geprüft wird das Ergebnis meist per Blick auf einen Screenshot, und der sagt nichts darüber, ob ein Button reagiert oder ein Formular durchläuft.

Vox (@Voxyz_ai auf X) hat dafür im September 2026 drei Posts mit Prompt-Vorlagen veröffentlicht, gebaut für Codex.{q:1}{q:2}{q:3} Zusammen ergeben sie einen Ablauf, den ein Video von Alex Sprogis um Diagramme aus der Codebase ergänzt.{q:4}

## Der Ablauf

### 1. Referenzbild generieren und als Spezifikation nutzen

Trenne Gestaltung und Umsetzung. Vox lässt Codex zuerst mit dem eingebauten Werkzeug `imagegen` ein Bild der Seite entwerfen, laut Post mit Images 2.5 (Stand 19.09.2026). Danach setzt das Codemodell, bei ihm Sol oder Astra, das Bild in Code um.{q:1} Sein Prompt sinngemäß lautet „Entwirf diese Seite mit imagegen neu und setz das Ergebnis dann um.“

Das Bild ersetzt eine lange Beschreibung von Layout, Farben und Abständen. Wer lieber selbst vorgibt, sammelt Referenz-Screenshots und schreibt dazu, was an jedem funktioniert. So entsteht das Vokabular, mit dem du später präzise promptest.{q:5} Rechne mit einem zusätzlichen Schritt für die Bildgenerierung und erwarte keine pixelgenaue Umsetzung.{q:1}

### 2. Vage Wünsche durch benannte Operationen ersetzen

Wenn die Seite steht und etwas noch nicht passt, gib eine benannte Operation statt eines Adjektivs. Vox nutzt dafür den Skill Impeccable:{q:2}

| Befund | Operation |
|---|---|
| Seite wirkt blass | `bolder` |
| Seite wirkt überladen | `distill` |
| Fast fertig, Details fehlen | `polish` |

Jede Operation übersetzt sich in konkrete Designänderungen, die der Agent ausführen kann.{q:2} Ohne Skill hilft die gleiche Disziplin im Prompt. Avid empfiehlt, im ersten Durchgang vollen Kontext mitzugeben (Ziel, Zielgruppe, Hex-Codes, Komponenten, Referenzcode), dann ein erzwungenes Self-Review der KI und erst zuletzt Feinschliff anhand von Screenshots.{q:5}

Vox nennt als Notlösung einen Zusatzsatz am Ende jedes Auftrags, der UX, DX und AX gegeneinander abwägen lässt, ohne bestehende Funktionen zu brechen.{q:2} Das ist ein Prompt-Trick ohne Nachweis. Die benannten Operationen sind der bessere Weg.

### 3. Referenzquelle, Auswahl und Prüfschritt in einen Skill

Komponenten, die dir gefallen, sollen beim Seitenbau automatisch als Referenz dienen. Vox packt dafür eine Komponentenbibliothek in einen eigenen Skill namens `design-reference`. Er muss drei Dinge festlegen:{q:3}

- **Wo gesucht wird:** ein Web-Katalog, ein Open-Source-Repo oder ein lokales Verzeichnis im Projekt.
- **Was ausgewählt wird:** zuerst vorhandene Komponenten des Projekts wiederverwenden, externe Referenzen nach Funktion, Layout, Interaktion und Passung zum Tech-Stack wählen.
- **Wie es übernommen wird:** Farben, Schriften, Abstände und Inhalte ans Projekt anpassen, danach die Seite im Browser auf Desktop und Mobile prüfen und die wichtigsten Interaktionen ausprobieren.

Schreib in jeden solchen Skill außerdem, dass der Agent fehlenden Zugriff auf eine Quelle oder ein Werkzeug meldet, statt einen Abruf vorzutäuschen.{q:3}

Setze die Bibliothek nur für die ein bis zwei Sektionen ein, die die Seite tragen, etwa Hero und Pricing.{q:2} Ein Auftrag lautet dann zum Beispiel „Bau mit design-reference eine Preisseite, Referenzen für Pricing-Karten und einen Umschalter monatlich/jährlich, Stil wie die bestehende Seite.“{q:3} Die Bibliothek, die Vox verwendet, hat beim Kopieren und Installieren von Komponenten ein kostenloses Nutzungslimit. Ein Open-Source-Repo oder ein lokales Verzeichnis umgeht das.{q:3}

### 4. Der Agent bedient die Seite im Browser

Ein gut aussehender Screenshot beweist nichts über das Verhalten. Im letzten Schritt öffnet der Agent den Browser, klickt Buttons, füllt Formulare aus und wechselt in einen mobilen Viewport.{q:2} Er sucht Buttons ohne Funktion, unverständliche Fehlermeldungen und Stellen, an denen der nächste Schritt unklar ist.

Vox nutzt dafür einen UX-Audit-Skill, den er für Codex angepasst hat. Das Original ist für Claude Code gebaut, die Browser-Anbindung musst du also für dein Werkzeug umstellen und den Umfang auf die gewünschten Seiten begrenzen.{q:3} Wirksam wird der Audit mit einer konkreten Nutzeraufgabe, zum Beispiel „Geh als Erstnutzer auf der Testseite von der Planauswahl bis zur abgeschlossenen Registrierung, klick und füll alles aus, prüf die Ergebnisse. Liefere Reproduktionsschritte, Screenshots und konkrete Fixes.“{q:3}

Der Audit prüft Verhalten statt Optik, deshalb ist er der belastbarste Schritt des Ablaufs.{q:2} Wie du daraus vor dem Release einen vollständigen Prüflauf mit mehreren Agenten machst, steht in [Vor dem Launch: Lass Agenten deine App angreifen](post:pre-launch-app-angreifen).

### 5. Optional: Architektur-Diagramme aus der Codebase

Dasselbe Prinzip, erzeugen und per Bild selbst prüfen, funktioniert auch für Dokumentation. Sprogis zeigt den Open-Source-Skill Archify, der aus einer Beschreibung oder direkt aus der Codebase interaktive Diagramme baut: Architektur, Datenfluss, Sequenz, Workflow, Lifecycle und auch Geschäftsprozesse.{q:4} Pro Diagramm entstehen eine HTML-Datei und eine JSON-Quelle unter `docs/diagrams`. Der Agent macht Screenshots der eigenen Darstellung und arbeitet nach, bis sie stimmt.{q:4}

Damit ersetzt du Handdiagramme, die nach jeder Codeänderung veralten. Die Screenshot-Schleife prüft allerdings nur, ob das Diagramm sauber dargestellt wird. Ob die abgeleiteten Beziehungen zwischen den Komponenten stimmen, prüft niemand.{q:4}

## Wann du was einsetzt

| Situation | Schritt |
|---|---|
| Neue Seite, keine klare Vorstellung | Referenzbild generieren |
| Seite steht, wirkt aber falsch | benannte Operation |
| Mehrere Seiten im selben Stil | Design-Reference-Skill |
| Vor jeder Übergabe an Nutzer | UX-Audit im Browser |
| Architektur erklären oder onboarden | Diagramm-Skill |

## Kosten und Grenzen

- **Kein Nachweis der Wirkung.** Alle Quellen sind Praxisberichte ohne Vorher-Nachher-Vergleich, die drei Posts zum Kern stammen vom selben Autor.{q:2}
- **Bilder kosten Kontext.** Jedes Referenzbild und jeder Screenshot nimmt Platz im Context Window ein. Für rein strukturelle Aufgaben lohnt das nicht.
- **Der Agent schließt aus Code.** Ein Modell leitet CSS-Fixes aus dem Quelltext ab und sieht das gerenderte Ergebnis nicht. Ohne Prüfung im Browser sieht niemand nach, ob die Änderung so aussieht wie gewollt.
- **Browser-Läufe sind teuer.** Der Audit kostet Tokens und Zeit, begrenze ihn deshalb auf die Flows, die zählen.{q:2}
- **Diagramme können falsch sein.** Die Selbstkorrektur per Screenshot sichert die Darstellung, nicht den Inhalt.{q:4}

## Empfehlung

Fang mit dem UX-Audit an, weil er echte Fehler mit Reproduktionsschritten findet, und schreib für jeden Kern-Flow eine konkrete Nutzeraufgabe. Benannte Operationen kosten nichts und sparen dir die „mach es schöner“-Runden. Den Design-Reference-Skill lohnt es sich zu bauen, sobald du mehr als eine Seite im selben Stil brauchst. Referenzbilder setzt du bei neuen Seiten ein, Diagramme aus der Codebase nur mit einem Menschen, der die Beziehungen gegenliest.
