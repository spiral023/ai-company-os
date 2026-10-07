---
titel: "Vier Prompts für lange Agent-Läufe: Aufgaben finden, durcharbeiten, ehrlich abschließen"
datum: 2026-10-07
kategorie: prompts
zusammenfassung: "Vier Prompts aus vier Quellen für lange Läufe mit Claude Code und Codex, auf Deutsch übertragen: Aufgaben für die Nacht finden, einen Plan durcharbeiten, echte Prüfungen erzwingen und Stopps regeln. Mit Link zum Original."
status: freigegeben
geprueft_am: 2026-10-07
freigabe: automatisch
quellen:
  - 2026-08-12-voxyz_ai-2087579867139264681
  - 2026-02-10-boris-tane-plan-annotation-workflow
  - 2026-09-28-claude-building-with-claude-sonnet-5-5-claude-dev-blog
  - 2026-09-22-claude-getting-the-most-out-of-opus-5-5-in-claude-and-c
---

## Kurz gesagt

- Vier Prompts aus vier Quellen für Läufe, bei denen du nicht danebensitzt: Aufgaben auswählen, einen Plan abarbeiten, Fertigmeldungen absichern, Stopps und Abschluss regeln.
- Zwei davon sind Bausteine für CLAUDE.md oder den System-Prompt. Sie wirken in jedem Lauf, ohne dass du sie jedes Mal eintippst.
- Lies nach einem langen Lauf zuerst, was der Agent von dir braucht, dann Diff und Testergebnisse, und merge erst danach.
- Jeder Prompt ist auf Deutsch übertragen, das englische Original ist verlinkt.

## Die vier Prompts im Überblick

| Prompt | Wann | Ergebnis | Von |
|---|---|---|---|
| Abend-Scan | Eine Stunde vor Feierabend, als geplanter Lauf | Bericht mit Aufgaben, die nachts sicher laufen können | @Voxyz_ai |
| Plan durcharbeiten | Ein freigegebener Plan liegt als Datei vor | Umsetzung bis zur letzten Aufgabe, Fortschritt im Plan | Boris Tane |
| Echte Prüfung vor „fertig“ | Dauerhaft im System-Prompt oder in CLAUDE.md | Fertigmeldung nur mit Test-, Typecheck- oder Build-Lauf | Addy Osmani (Anthropic) |
| Stopps, Checkliste, Abschluss | Dauerhaft in CLAUDE.md oder im Auftrag | Weniger unnötige Pausen, Stand in TASKS.md, klarer Abschluss | Addy Osmani (Anthropic) |

## 1. Abend-Scan: Welche Aufgaben können über Nacht laufen?

@Voxyz_ai plant diesen Prompt als Automatisierung eine Stunde vor dem Schlafengehen ein, damit ungenutztes Kontingent von Claude Code oder Codex nicht verfällt. Der Lauf schreibt nur einen Bericht, er ändert keinen Code und startet keinen Agent.{q:1}

```text
Führ diese Prüfung jeden Tag eine Stunde vor dem Schlafengehen aus.

Untersuche nur Quellen, auf die du schon Zugriff hast:
- Repositories, die heute geändert wurden, einschließlich git status
- offene Issues, TODOs und Pläne
- kürzlich fehlgeschlagene Tests oder Builds
- Übergabe-Dokumente, die Agents hinterlassen haben

Finde 3 bis 5 Aufgaben, die Claude Code oder Codex über Nacht sicher
erledigen können.

Jeder Kandidat muss:
- ein klares Ziel und eine Definition von „fertig“ haben
- während des Laufs keine Entscheidung von mir brauchen
- in einen isolierten Branch oder Worktree passen
- einen exakten Test-, Build- oder Prüfbefehl haben
- vollständig umkehrbar sein

Schließ alles aus, was Mergen, Deployen, Nachrichten verschicken, Geld
ausgeben, Zugangsdaten ändern oder Produktionsdaten anfassen erfordert.

Gib zu jedem Kandidaten zurück:
1. Aufgabe
2. Wo du sie gefunden hast
3. Was sie bis morgen früh liefern kann
4. Wie man sie prüft
5. Was sie nicht anfassen darf
6. Einen vollständigen Prompt, den ich in Claude Code oder Codex einfügen kann

Dieser Prompt muss Arbeitsverzeichnis, Branch oder Worktree, die Definition
von „fertig“ und die Prüfbefehle enthalten, außerdem, welche Änderungen,
Testergebnisse und Blocker er morgens zurückmelden muss.

Sortiere die Kandidaten nach Nutzen und danach, wie wahrscheinlich sie bis
zum Morgen fertig werden.

Wenn nichts passt, schreib: „Heute Nacht kann keine Aufgabe sicher laufen.“
Erfinde keine Aufgaben, um den Bericht zu füllen.

Hör nach dem Bericht auf. Bearbeite keine Dateien, starte keinen Agent und
führ keine der Aufgaben aus.
```

**Wann:** als geplanter Lauf am Abend. Vox rät, mit einem einzigen Repository zu beginnen und Issue-Tracker und Übergabe-Dokumente erst dazuzunehmen, wenn der Bericht brauchbare Aufgaben liefert.{q:1}

**Ergebnis:** ein Bericht mit 3 bis 5 sortierten Kandidaten, jeder mit fertigem Ausführungs-Prompt. Welche davon nachts laufen, entscheidest du. Am Morgen liest du Diff und Prüfergebnisse, bevor du etwas mergst.{q:1}

Original: [Post von @Voxyz_ai auf X (englisch)](https://x.com/Voxyz_ai/status/2087579867139264681)

## 2. Plan durcharbeiten: alles umsetzen, Fortschritt im Plan abhaken

Boris Tane lässt Claude erst bauen, wenn er den Plan in `plan.md` freigegeben hat. Wie dieser Plan entsteht, steht im [ersten Teil dieser Reihe](post:prompts-fuer-claude-code-zum-ausprobieren). Danach folgen zwei Prompts, die er in jeder Session wiederverwendet.{q:2}

```text
1. Ergänz den Plan um eine detaillierte To-do-Liste mit allen Phasen und
   einzelnen Aufgaben, die für den Plan nötig sind. Noch nicht implementieren.

2. Setz alles um. Wenn eine Aufgabe oder Phase fertig ist, markier sie im
   Plan-Dokument als erledigt. Hör nicht auf, bevor alle Aufgaben und Phasen
   erledigt sind. Füg keine unnötigen Kommentare oder JSDocs hinzu und
   verwende keine any- oder unknown-Typen. Führ laufend den Typecheck aus,
   damit du keine neuen Fehler einbaust.
```

**Wann:** wenn der Plan steht und du keine Einwände mehr hast. Die Vorgaben zu JSDoc, `any` und Typecheck gelten für TypeScript. Für andere Sprachen ersetzt du sie durch eure Regeln und euren Prüfbefehl.

**Ergebnis:** eine Umsetzung, die bis zur letzten Aufgabe durchläuft. Weil Claude jede erledigte Aufgabe im Plan abhakt, siehst du dort jederzeit den Stand. Tane nennt das besonders nützlich bei Sessions, die Stunden laufen.{q:2}

Original: [How I Use Claude Code von Boris Tane (englisch)](https://boristane.com/blog/how-i-use-claude-code/)

## 3. Echte Prüfung vor „fertig“

Im Leitfaden zu Sonnet 5.5 schreibt Addy Osmani, dass das Modell seine Arbeit meist prüft, bevor es sie als erledigt meldet. Bei niedriger Effort-Stufe überspringt es aber manchmal eine Prüfung, die die Änderung wirklich ausführt. Für diesen Fall empfiehlt der Leitfaden einen Absatz für den System-Prompt.{q:3}

```text
Wenn du Code änderst, der sich ausführen, bauen oder per Typecheck prüfen
lässt, führ eine echte Prüfung aus, die die Änderung abdeckt, bevor du sie als
erledigt meldest: die Tests des Projekts, den Typechecker, den Build oder den
geänderten Befehl selbst. Eine reine Syntaxprüfung oder ein Prüfbefehl, der
gar nicht erst startet, zählt nicht. Fehlen nur die deklarierten
Abhängigkeiten des Projekts, installiere sie mit dem Paketmanager und dem
Lockfile des Projekts (z. B. npm install, pip install -r requirements.txt),
nie mit sudo oder dem Paketmanager des Systems, außer ich sage etwas anderes.
Nur wenn hier keine echte Prüfung laufen kann, nenne die Prüfung, die du nicht
ausgeführt hast, und den Grund, statt die Änderung als erledigt zu melden.
```

**Wann:** sobald du Fertigmeldungen ohne Test- oder Build-Ausgabe siehst.{q:3} Der Absatz ist an kein bestimmtes Modell gebunden, du kannst ihn in CLAUDE.md, AGENTS.md oder einen eigenen System-Prompt setzen.

**Ergebnis:** Eine Fertigmeldung kommt nur noch mit echtem Prüflauf. Kann keiner laufen, sagt der Agent, welche Prüfung fehlt und warum.

Original: [Building with Claude Sonnet 5.5 von Addy Osmani (englisch)](https://claude.dev/blog/building-with-claude-sonnet-5-5/)

## 4. Stopps, Checkliste und Abschluss regeln

Opus 5.5 hält dich laut Osmani während der Arbeit auf dem Laufenden. Bei langen Aufgaben hält es manchmal an, um zu berichten, statt weiterzumachen. Es fasst dann zum Beispiel den nächsten Schritt zusammen, ohne ihn auszuführen, oder bietet an, weiterzumachen. Anweisungen, die solche Stopps benennen, befolgt es.{q:4} Osmani gibt dafür drei kurze Anweisungen, hier zu einem Block zusammengefasst.

```text
Wenn ein Schritt meine Eingabe nicht braucht, mach weiter. Schreib
Statusmeldungen in dieselbe Nachricht wie deine nächste Aktion.
Halt nur an und frag, wenn du ohne mich nicht weiterkommst, oder vor allem,
was etwas zerstört: Daten löschen, Force-Push oder Änderungen außerhalb
dieses Repositorys.

Führ eine Checkliste in TASKS.md. Hak jeden Punkt ab, sobald er erledigt ist,
und ergänze alles Neue, das du findest.

Beende jeden Lauf mit drei Überschriften: Blockiert durch mich, Geändert,
Gefunden.
```

**Wann:** Die Stopp-Regel und die Überschriften gehören in CLAUDE.md, die Checkliste in den Auftrag für einen längeren Lauf. Passe die Liste der zerstörerischen Aktionen an dein Projekt an, das empfiehlt auch Osmani.{q:4}

**Ergebnis:** Der Agent pausiert seltener ohne Grund. Die Checkliste in TASKS.md bleibt erhalten, wenn Claude Code bei vollem Kontextfenster ältere Teile der Unterhaltung zusammenfasst. Du liest den Stand in der Datei statt im Verlauf.{q:4} Am Ende steht zuerst, worauf der Agent bei dir wartet.

Original: [Getting the most out of Opus 5.5 von Addy Osmani (englisch)](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/)

## Empfehlung

Setz den Absatz zur echten Prüfung heute in deine CLAUDE.md oder AGENTS.md. Er kostet kaum Kontext und greift genau dann, wenn der Agent eine Prüfung auslässt. Den Abend-Scan kannst du gefahrlos ausprobieren, weil er nur einen Bericht schreibt. Wie du einen Lauf mit binärem Ziel und getrennter Prüfung absicherst, steht im Beitrag zu [Agent-Loops, die nicht entgleisen](post:agent-loops-die-nicht-entgleisen).
