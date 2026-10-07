---
titel: "Fünf Rollen-Prompts für Claude Code und Codex: von der Anforderung bis zum Backend"
datum: 2026-10-08
kategorie: prompts
zusammenfassung: "Fünf Rollen-Prompts von @Voxyz_ai für Claude Code und Codex, auf Deutsch übertragen: Requirements Lead, Tech Lead, Performance, Frontend und Backend. Was jeder Prompt verlangt, wann du ihn einsetzt und was herauskommt."
status: freigegeben
geprueft_am: 2026-10-07
freigabe: automatisch
quellen:
  - 2026-09-19-voxyz_ai-2101355643882065971
---

## Kurz gesagt

- Fünf Prompts aus einem Thread von @Voxyz_ai, jeder für eine Rolle: Anforderungen klären, Aufgabe komplett liefern, Performance messen, UI prüfen, Backend durchtesten.
- Alle fünf übergeben dem Agent ein Ergebnis statt einzelner Schritte und verlangen am Ende einen Nachweis, was geprüft wurde.
- Ersetze die Platzhalter in eckigen Klammern und probier einen Prompt an deiner nächsten Aufgabe aus.
- Der Thread enthält Erfahrungswerte des Autors, keine Vergleichsmessung.

## Was die Prompts gemeinsam haben

Vox schreibt, man behandle Claude Code und Codex zu oft wie einen Praktikanten, dem man jeden Schritt vorgibt. Seine Prompts übergeben stattdessen eine Rolle mit klarem Endergebnis.{q:1} Fast jeder endet mit einer Prüfung und einer Berichtspflicht, und jeder verbietet eine typische Abkürzung: Annahmen als Anforderung ausgeben, eine Verbesserung ohne Messung behaupten, eine Seite für fertig halten, weil der Code läuft.{q:1}

Zwei weitere Prompts aus demselben Thread stehen in anderen Beiträgen dieser Reihe, der [Debugging-Prompt](post:prompts-fuer-claude-code-zum-ausprobieren) und der [Reviewer](post:prompts-fuer-review-und-abnahme).

## 1. Requirements Lead: klären, was gebaut werden soll

```text
Ich möchte [IDEE] bauen. Das habe ich bisher: [STICHPUNKTE, SCREENSHOTS,
REFERENZEN ODER PROJEKT].

Hilf mir zuerst zu klären, wer es nutzt, welches Problem es löst, wo der
Nutzer startet und was er am Ende bekommen soll.

Finde, woran ich nicht gedacht habe und was das Ergebnis beeinflussen könnte.
Was du selbst aus den Unterlagen beantworten kannst, schlag nach. Bei
Entscheidungen, die ich treffen muss, stell die wichtigste Frage zuerst. Kipp
keinen Fragebogen über mir aus.

Wenn wir das durchgearbeitet haben, schreib einen Auftrag, den ich direkt an
einen anderen Engineer geben kann. Er soll verstehen, was zu tun ist, was
nicht dazugehört, welche Einschränkungen gelten und wann es fertig ist, ohne
unser Gespräch zu lesen.

Markiere alles, was wir nicht entschieden haben. Mach aus deinen Annahmen
keine bestätigten Anforderungen.

Überlass Umsetzungsentscheidungen dem Engineer. Zeig mir den Auftrag zuerst
zur Freigabe.
```

**Wann:** bei einer Idee, die noch nicht ausformuliert ist, bevor irgendjemand baut.

**Ergebnis:** ein Auftrag mit Ziel, Abgrenzung, Einschränkungen und Kriterium für „fertig“, den ein anderer Engineer oder Agent ohne den Chatverlauf versteht. Offene Punkte sind markiert.{q:1}

## 2. Tech Lead: eine Aufgabe von Anfang bis Ende liefern

```text
Ich möchte das hier abschließen: [AUFGABE ODER VEREINBARTER PLAN].

Mach beim aktuellen Stand weiter, bis [DAS ENDERGEBNIS, DAS ICH SEHEN,
NUTZEN ODER PRÜFEN KANN] erreicht ist.

Lies die relevanten Dateien, um das Projekt zu verstehen. Schlag nach, was du
brauchst. Nutze die Werkzeuge, die du hast.

Übernimm die Arbeit von Anfang bis Ende: Aufgabe verstehen, umsetzen,
ausführen, prüfen und beheben, was fehlschlägt. Frag nicht nach jedem
Schritt, ob du weitermachen sollst.

Wenn eine Seite beteiligt ist, öffne sie mit den verfügbaren Browser-Werkzeugen
und benutze sie wirklich. Klick die Buttons, füll die Formulare aus und geh die
Abläufe durch, die ein Nutzer gehen würde. Behebe gefundene Probleme und prüf
danach noch einmal.

Bei größeren Aufgaben darfst du unabhängige Teile an andere verfügbare Agents
abgeben. Du bist dafür verantwortlich, die Ergebnisse zusammenzuführen und
sicherzustellen, dass das Ganze funktioniert.

Bleib im vereinbarten Umfang. Frag mich, wenn du eine Entscheidung, weiteren
Zugriff oder eine Änderung des Umfangs brauchst.

Zeig mir am Ende das fertige Ergebnis. Sag mir, wie ich es benutze, was du
geprüft hast und was noch offen ist.
```

**Wann:** wenn Aufgabe oder Plan feststehen und du den Agent ohne Zwischenfragen arbeiten lassen willst.

**Ergebnis:** ein fertiges, im Browser durchgeklicktes Ergebnis mit Anleitung, Prüfliste und offenen Punkten.{q:1} Der Preis ist das Risiko, dass der Agent lange in die falsche Richtung läuft und viele Tokens verbraucht. Kläre deshalb vorher die Anforderungen, etwa mit dem Prompt aus Abschnitt 1.

## 3. Performance Engineer: erst messen, dann ändern

```text
[SEITE ODER FEATURE] ist langsam, wenn [NUTZUNGSSZENARIO].

Finde heraus, wo die Zeit verloren geht, bevor du etwas änderst. Verwechsle
einfacheren Code nicht mit schnellerem Code.

Vergleiche vorher und nachher mit denselben Aktionen und Daten und prüf, ob
die Ergebnisse noch stimmen. Sag mir, was sich geändert hat und ob die
Änderungen andere Probleme verursacht haben.

Behaupte keine Verbesserung, die du nicht gemessen hast.
```

**Wann:** wenn etwas spürbar langsam ist und du wissen willst, warum, bevor jemand umbaut.

**Ergebnis:** eine Messung vor und nach der Änderung mit denselben Aktionen und Daten, dazu die Bestätigung, dass die Ergebnisse noch stimmen.{q:1} Eine Verbesserung ohne Messung darf der Agent nicht melden.

## 4. Frontend Engineer: UI und UX wirklich prüfen

```text
Bau [SEITE] nach [REFERENZBILD ODER DESIGNVORGABEN] und halte sie konsistent
mit dem Rest des Projekts.

Prüf mehr als den Normalzustand. Was passiert ohne Daten, während des Ladens,
bei einem Fehler oder bei ungewöhnlich langem Text? Funktioniert es auch auf
dem Handy?

Öffne die fertige Seite und prüf zuerst die UI: Passen Layout, Schriften,
Farben und Abstände zur Referenz?

Prüf danach die UX: Finden Nutzer die Buttons, können sie Formulare leicht
ausfüllen, erkennen sie, ob eine Aktion geklappt hat, und wissen sie, was zu
tun ist, wenn etwas schiefgeht?

Behebe die Probleme, die du tatsächlich findest, und zeig mir Screenshots vom
Ergebnis.

Halt die Seite nicht für fertig, nur weil der Code läuft.
```

**Wann:** beim Bau einer Seite nach Vorlage, besonders wenn du Leer-, Lade- und Fehlerzustände sonst erst im Betrieb entdeckst.

**Ergebnis:** eine Seite, die gegen die Referenz und auf typische UX-Probleme geprüft ist, mit Screenshots als Nachweis.{q:1} Wie du den Abgleich mit einem Referenzbild weiter schärfst, steht im Beitrag zu [UI mit Agenten](post:ui-mit-agenten-referenzbild-audit).

## 5. Backend Engineer: den Ablauf hinter dem Button durchtesten

```text
Bring [FEATURE] vollständig zum Laufen.

Wenn der Nutzer [AKTION] ausführt, soll er [ERGEBNIS] bekommen. Folge dem
bestehenden Ansatz des Projekts und binde die Daten an, die gelesen,
gespeichert oder aktualisiert werden müssen.

Probier es wirklich aus. Klappt der normale Ablauf? Was passiert bei
ungültiger Eingabe, fehlenden Rechten, einem Fehler mittendrin oder einem
zweiten Klick?

Prüf, ob die Anzeige auf der Seite mit den tatsächlich gespeicherten Daten
übereinstimmt und ob bestehende Features weiter funktionieren.

Sag mir, wie ich es ausprobiere und welche Szenarien du getestet hast.

Denk auch an die Developer Experience: wie man die API aufruft, welche
Parameter man schickt und wie man Fehler untersucht. Gib dem Nächsten ein
Beispiel, das er direkt ausführen kann.
```

**Wann:** wenn ein Feature Daten liest oder schreibt und du sicher sein willst, dass Anzeige und Datenbank übereinstimmen.

**Ergebnis:** ein durchgetesteter Ablauf mit Anleitung zum Ausprobieren, Liste der geprüften Szenarien und einem direkt ausführbaren Beispiel für die API.{q:1}

## Empfehlung

Fang mit dem Requirements Lead an, wenn deine Aufgabe noch vage ist, und gib den fertigen Auftrag dann dem Tech Lead. So weiß der Agent genau, wohin er ohne Zwischenfragen läuft. Den Performance-Prompt kannst du jederzeit einzeln nutzen, er ändert nichts, bevor er gemessen hat.

Original: [Thread von @Voxyz_ai auf X (englisch)](https://x.com/Voxyz_ai/status/2101355643882065971)
