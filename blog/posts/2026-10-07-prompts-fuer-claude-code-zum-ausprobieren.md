---
titel: "Fünf Prompts für Claude Code zum Ausprobieren: von der Wissenslücke bis zum Bugfix"
datum: 2026-10-08
kategorie: prompts
zusammenfassung: "Fünf Prompts für Claude Code aus öffentlichen Quellen, auf Deutsch übertragen: was jeder Prompt macht, wann du ihn einsetzt und was dabei herauskommt. Mit Link zum englischen Original."
status: freigegeben
geprueft_am: 2026-10-07
freigabe: automatisch
quellen:
  - 2026-07-03-trq212-2073100352921215386
  - 2026-08-04-anthropic-docs-claude-code-best-practices
  - 2026-02-10-boris-tane-plan-annotation-workflow
  - 2026-09-22-claude-getting-the-most-out-of-opus-5-5-in-claude-and-c
  - 2026-09-19-voxyz_ai-2101355643882065971
---

## Kurz gesagt

- Fünf Prompts aus fünf Quellen, je einer pro Arbeitsschritt: Wissenslücken finden, Anforderungen klären, planen, umsetzen, Fehler beheben.
- Kopiere den Prompt, ersetze die Platzhalter in eckigen Klammern und probier ihn an deiner nächsten echten Aufgabe aus.
- Jeder Prompt ist eine deutsche Übertragung eines Autors, das englische Original ist verlinkt. Varianten anderer Autoren sind nicht eingemischt.
- Die Autoren beschreiben ihre Erfahrung, keine Messungen. Ob ein Prompt dir hilft, zeigt erst der Vergleich mit deinem gewohnten Vorgehen.

## Die fünf Prompts im Überblick

| Prompt | Wann | Ergebnis | Von |
|---|---|---|---|
| Blindspot Pass | Du arbeitest in einem Bereich, den du nicht kennst | Erklärung deiner Wissenslücken, bessere Folgeprompts | Thariq (Anthropic) |
| Interview zur Spec | Vor einem größeren Feature | `SPEC.md` mit geklärten Anforderungen | Claude-Code-Dokumentation |
| Recherche, Plan, Anmerkungen | Vor Änderungen an einem bestehenden System | `research.md` und `plan.md`, die du korrigierst, bevor Code entsteht | Boris Tane |
| Zielzustand vorgeben | Lange Aufgaben mit vielen Teilschritten | Durchlauf bis zu einem prüfbaren Ende | Addy Osmani (Anthropic) |
| Fehler reproduzieren | Ein Bug, den du Schritt für Schritt beschreiben kannst | Behebung mit Bericht zu Ursache, Änderung und Prüfung | @Voxyz_ai |

## 1. Blindspot Pass: Finde heraus, was du nicht weißt

In einem fremden Teil der Codebasis weißt du oft nicht, welche Fragen du stellen müsstest. Thariq von Anthropic lässt Claude deshalb zuerst die Unknown Unknowns sammeln, also die Lücken, die dir gar nicht bewusst sind. Er verwendet dafür bewusst die englischen Begriffe „blindspot pass“ und „unknown unknowns“ und sagt dem Modell, wer er ist und was er schon weiß.{q:1}

```text
Ich soll [Aufgabe, z. B. einen neuen Auth-Provider einbauen], kenne mich aber
mit [Bereich, z. B. den Auth-Modulen dieser Codebasis] nicht aus. Mach einen
Blindspot Pass: Finde meine relevanten Unknown Unknowns, erklär sie mir und
hilf mir, dir bessere Prompts zu geben.
```

**Wann:** zu Beginn einer Aufgabe in unbekanntem Gelände. Thariqs zweites Beispiel dreht sich um Color Grading für ein Video, der Prompt funktioniert also auch ohne Code in jedem Chat.{q:1}

**Ergebnis:** eine Erklärung der Stellen, an denen du etwas übersehen könntest, und Hinweise, was in deinen nächsten Prompt gehört. Eine Lücke, die du vor dem ersten Code kennst, musst du später nicht als falsche Annahme im fertigen Code suchen.

Original: [A Field Guide to Fable von Thariq auf X (englisch)](https://x.com/trq212/status/2073100352921215386)

## 2. Interview zur Spec: Claude fragt, du antwortest

Bei einem neuen Feature fehlen meist Details, die erst beim Bauen auffallen. In den Best Practices für Claude Code stellt deshalb Claude die Fragen und schreibt am Ende die Spezifikation.{q:2}

```text
Ich möchte [kurze Beschreibung] bauen. Interviewe mich ausführlich mit dem
AskUserQuestion-Tool.

Frag nach technischer Umsetzung, UI/UX, Randfällen, Bedenken und Trade-offs.
Lass offensichtliche Fragen weg und bohr bei den schwierigen Stellen nach, an
die ich vielleicht nicht gedacht habe.

Interviewe mich weiter, bis alles abgedeckt ist, und schreib dann eine
vollständige Spezifikation in SPEC.md.
```

**Wann:** bevor du ein größeres Feature baust. AskUserQuestion ist das eingebaute Werkzeug von Claude Code für Rückfragen. In anderen Agents oder im Chat streichst du diesen Teil, der Rest funktioniert genauso.

**Ergebnis:** eine `SPEC.md`, die du lesen und korrigieren kannst, bevor Code entsteht. Die Fragen konzentrieren sich auf die schwierigen Stellen, weil der Prompt offensichtliche Fragen ausschließt.{q:2}

Original: [Best Practices for Claude Code (englisch)](https://www.anthropic.com/engineering/claude-code-best-practices)

## 3. Recherche, Plan, Anmerkungen: kein Code vor der Freigabe

Boris Tane trennt Verstehen, Planen und Umsetzen strikt. Claude schreibt zuerst Markdown-Dateien, die er liest und korrigiert, bevor eine Zeile Code entsteht.{q:3} Die Prompt-Kette hat drei Schritte.

```text
1. Lies diesen Ordner gründlich. Versteh im Detail, wie er funktioniert, was er
   tut und welche Besonderheiten er hat. Schreib danach einen ausführlichen
   Bericht deiner Erkenntnisse in research.md.

2. Ich möchte das Feature [Name und Beschreibung] bauen, das das System um
   [geschäftliches Ziel] erweitert. Schreib einen ausführlichen plan.md, wie
   das umgesetzt wird, mit Code-Snippets.

3. Ich habe Anmerkungen in das Dokument geschrieben. Arbeite alle Anmerkungen ein und
   aktualisiere das Dokument. Noch nicht implementieren.
```

Zwischen Schritt 2 und 3 schreibst du deine Korrekturen direkt in den Plan, etwa „Abschnitt streichen, Caching brauchen wir hier nicht“. Tane wiederholt Schritt 3 ein- bis sechsmal. Die Wörter „gründlich“ und „im Detail“ sind Absicht, ohne sie überfliegt Claude laut Tane den Code nur. Den Zusatz „Noch nicht implementieren“ hält er für unverzichtbar, weil Claude sonst losschreibt, sobald ihm der Plan gut genug erscheint.{q:3}

**Wann:** bei Änderungen, die ein bestehendes System berühren. Als teuersten Fehler nennt Tane Code, der für sich funktioniert, aber das umgebende System bricht, etwa durch doppelte Logik oder einen übergangenen Cache.{q:3}

**Ergebnis:** eine `research.md`, an der du Missverständnisse erkennst, bevor sie im Plan landen, und ein `plan.md`, der zu deinem System passt. Erst danach folgt die Umsetzung, bei Tane mit einem eigenen Prompt, der den Plan Punkt für Punkt abhakt.{q:3}

Original: [How I Use Claude Code von Boris Tane (englisch)](https://boristane.com/blog/how-i-use-claude-code/)

## 4. Zielzustand vorgeben: Sag dem Agent, wann er fertig ist

Addy Osmani empfiehlt im Leitfaden zu Opus 5.5, die ganze Aufgabe in einer Nachricht zu geben und das Ziel prüfbar zu benennen. Mit einem klaren Ende weiß das Modell, wann es fertig ist.{q:4}

```text
Migriere die Payment-Endpunkte vom alten auf den neuen Client.
Fertig heißt: Jeder Endpunkt nutzt den neuen Client, der alte Client ist
gelöscht und die Testsuite läuft durch.
Halt nur an und frag mich, wenn ein Test aus einem Grund fehlschlägt, den du
nicht erklären kannst.
```

Für eigene Aufgaben übernimmst du das Gerüst: `[Aufgabe]. Fertig heißt: [prüfbare Bedingungen]. Halt nur an, wenn [Ausnahme].`

**Wann:** bei langen Aufgaben mit vielen Teilschritten, etwa einer Migration durch ein großes Repository. Laut Anthropic hält Opus 5.5 solche Arbeit länger durch als Opus 5.{q:4} Welche älteren Anweisungen einem klaren Ende im Weg stehen, steht im Beitrag zu [alten Prompts und neuen Modellen](post:alte-prompts-neue-modelle).

**Ergebnis:** ein Durchlauf bis zum vereinbarten Ende ohne Rückfrage nach jedem Schritt. Die Stopp-Regel legt fest, wann eine Rückfrage trotzdem nötig ist.

Original: [Getting the most out of Opus 5.5 von Addy Osmani (englisch)](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/)

## 5. Fehler reproduzieren statt verstecken

Der Debugging-Prompt von @Voxyz_ai verlangt, den Fehler vor und nach der Änderung mit denselben Schritten nachzustellen, und schließt ausdrücklich aus, ihn nur zu verstecken.{q:5}

```text
Das Problem: [PROBLEM].
Meine Schritte: [SCHRITTE].
Erwartetes Ergebnis: [ERGEBNIS].
Screenshots oder Fehlermeldungen: [MATERIAL].

Reproduziere das Problem zuerst mit meinen Schritten. Finde die Ursache und
behebe sie. Wiederhole danach dieselben Schritte und prüf, ob das Problem weg
ist und angrenzende Funktionen weiter laufen.

Sag mir, was die Ursache war, was du geändert hast und wie du die Behebung
geprüft hast.

Wenn du die Ursache noch nicht gefunden hast, such weiter. Wenn du das Problem
mit meinen Schritten nicht reproduzieren kannst, sag mir, was du noch
brauchst. Versteck den Fehler nicht einfach.
```

**Wann:** bei jedem Bug, den du Schritt für Schritt beschreiben kannst, in Claude Code oder Codex.{q:5}

**Ergebnis:** eine Behebung, die mit deinen eigenen Schritten geprüft ist, und ein kurzer Bericht über Ursache, Änderung und Prüfung. Die Anweisung „such weiter“ kann teuer werden. Brich ab, wenn der Agent lange ohne Fortschritt sucht, und gib ihm mehr Material.

Original: [Thread von @Voxyz_ai auf X (englisch)](https://x.com/Voxyz_ai/status/2101355643882065971). Dort stehen sechs weitere Rollen-Prompts, unter anderem für Review und Anforderungen.

## Empfehlung

Nimm für deine nächste Aufgabe den Prompt aus der Tabelle, der zum Arbeitsschritt passt, und ändere nur die Platzhalter. Hilft er dir, speichere ihn als Snippet oder als eigenen Befehl, damit du ihn nicht jedes Mal neu tippst. Wie du entscheidest, ob ein wiederkehrender Prompt in CLAUDE.md, einen Skill oder einen Hook gehört, steht im Beitrag zu den [Erweiterungs-Ebenen](post:welche-ebene-claude-md-skill-hook-mcp).
