---
name: quellen-verarbeiten
description: "Verwende diesen Skill, wenn offene Quellen aus den Typordnern unter 00_Inbox/Quellen/ (status: neu) ins Knowledge-System eingearbeitet werden sollen — als Sammel-Lauf über alle oder für einzelne Quellen. Auch bei Formulierungen wie „verarbeite die neuen Quellen“, „arbeite die Inbox ab“, „was liegt noch offen“. Schreibt deutsche Zusammenfassungen mit Bildern, leitet Arbeitsweisen ab und vergleicht mit dem Bestand."
---

# Quellen verarbeiten

## Rolle

Du arbeitest als erfahrener AI Engineer, nicht als Zusammenfasser. Du kennst Coding Agents, Harness-Architektur, Context Engineering, Evals, Kosten- und Token-Ökonomie aus der Praxis. Deine Aufgabe ist es, aus Quellenmaterial **belastbare Arbeitsweisen** zu destillieren — und Marketing, Anekdote und Messung auseinanderzuhalten.

Das bedeutet konkret:

- Du fragst bei jeder Behauptung, ob sie gemessen, plausibel oder bloß behauptet ist — und schreibst das Ergebnis dazu.
- Du erkennst, wenn eine Quelle eine bekannte Arbeitsweise unter neuem Namen verkauft, und verlinkst statt zu duplizieren.
- Du erkennst den Unterschied zwischen einer Erkenntnis (übertragbar) und einer Konfiguration (versionsabhängig, verfällt).
- Du nennst Kosten und Grenzen einer Arbeitsweise, nicht nur ihren Nutzen. Eine Technik ohne benannten Preis ist unvollständig beschrieben.

## Abgrenzung

- **Dieser Skill:** Batch über bereits erfasste Quellen in `00_Inbox/Quellen/`. Der Rohtext liegt schon lokal.
- **`knowledge-ingest`:** Einzelne Quelle, die Philipp gerade teilt und die noch nicht erfasst ist. Nutzt für X `npm run ingest:x`, für TikTok `npm run ingest:tiktok`, für Artikel/YouTube/PDF `python ai.py ingest`.

Beide schreiben ins selbe Ziel und folgen denselben Invarianten aus `80_Knowledge/README.md`.

## Schema und Format

Vor dem ersten Schreiben lesen und exakt befolgen:

1. `80_Knowledge/README.md` — Invarianten, Konfidenz-Modell, Templates.
2. `references/artikel-format.md` (in diesem Skill-Verzeichnis) — Aufbau der deutschen Zusammenfassung, Bildregeln, Sprachregeln.

## Ablauf

### 1. Offene Quellen ermitteln

```powershell
Get-ChildItem "00_Inbox/Quellen" -Filter "*.md" -File -Recurse |
  Select-String -Pattern '^status: neu$' |
  Select-Object -ExpandProperty Path
```

`README.md` in diesem Ordner ist keine Quelle. Gibt es keine Treffer: das melden und aufhören, nichts erfinden.

Bei mehr als fünf offenen Quellen: nach thematischer Nähe gruppieren und in einer Reihenfolge arbeiten, die zusammengehörige Quellen benachbart hält — dann werden Quervergleiche und Widersprüche in einem Durchgang sichtbar statt über mehrere Läufe verstreut.

### 2. Quelle vollständig erfassen

Die Notiz komplett lesen, nicht nur den Anfang. **Die Bilder im zugehörigen `medien/<slug>/`-Ordner ebenfalls öffnen und lesen** — Charts, Preistabellen und Benchmark-Grafiken enthalten regelmäßig Zahlen, die im Fließtext fehlen. Eine Verarbeitung, die die Bilder überspringt, verliert genau die belastbaren Werte.

Bei YouTube-Transkripten: Der Rohtext liegt absichtlich ohne Zeitstempel als lesbare Absätze vor. Kapitelmarken aus der Videobeschreibung belegen nur grobe Abschnitte, nicht einzelne Sätze. Bei Auto-Transkripten (`transkript_generiert: ja`) mit Fachbegriff-Fehlern rechnen und offensichtliche Verballhornungen als solche behandeln, statt sie als Zitat zu übernehmen.

### 3. Relevanz-Gate

Prüfen, ob die Quelle eine übertragbare Erkenntnis über Arbeitsweisen enthält (AI Coding, Agents, Skills, Evals, Modell-Ökonomie, angrenzende Themen wie Security oder Tooling).

- **Nein** — reine News, Ankündigung ohne Methode, Werbung: in der Inbox-Notiz `status: ignoriert` setzen und `notiz:` mit einem Satz Begründung ergänzen. Keine Source-Notiz anlegen. Im Diff-Resümee ausweisen.
- **Ja** — weiter. Marktdaten und Zahlen ohne Arbeitsweise können relevant sein, wenn sie eine Entscheidung stützen (Kosten, Modellwahl, Build-vs-Buy); dann als Source-Notiz ohne Pattern.

### 4. Bestand abgleichen — vor dem Schreiben

Nie mit dem Schreiben beginnen, ohne den Bestand zu kennen:

1. `80_Knowledge/Index.md` lesen — welche Patterns existieren?
2. Dubletten-Check: normalisierte URL (ohne `utm_*`, `fbclid`, `ref`, `?s=`, `?t=`) gegen `80_Knowledge/Sources/`.
3. Themennähe: nach Schlüsselbegriffen der Quelle in `Sources/`, `Patterns/` und `Vergleiche/` suchen. Zwei Quellen zum gleichen Thema sind der wertvollste Fall — dort entstehen Konfidenz-Sprünge und Spannungen.
4. Nennt die Quelle ein Repo aus `external_repos/INDEX.md`: dort stichprobenartig nachprüfen. Bestätigte Aussagen bekommen eine Beleg-Zeile mit Repo-Pfad und Typ `verifiziert`.

### 5. Evidenz inventarisieren

Vor dem Formulieren intern jede tragende Aussage zuordnen: Wer behauptet sie, wann, auf welcher Grundlage (Messung, Erfahrungsbericht, Meinung)? Stimmt sie mit dem Bestand überein, ergänzt sie ihn, oder widerspricht sie?

Nichts plausibel ergänzen. Eigenes Fachwissen darf einordnen und kontextualisieren, aber nie als Aussage der Quelle erscheinen — solche Ergänzungen sprachlich klar trennen („die Quelle zeigt X; einzuordnen ist das im Kontext von Y").

### 6. Source-Notiz schreiben

Nach Template aus `80_Knowledge/README.md`, Dateiname `YYYY-MM-DD-<autor>-<slug>.md` mit dem **Veröffentlichungsdatum** der Quelle. Aufbau, Sprache und Bildregeln nach `references/artikel-format.md`.

Der Rohtext bleibt in `00_Inbox/Quellen/<Quelltyp>/` und wird **nicht** in die Source-Notiz kopiert. Die Source-Notiz enthält die redaktionelle deutsche Zusammenfassung und verweist im Feld `rohquelle:` auf die Inbox-Datei.

### 7. Arbeitsweisen ableiten

Pro Kernaussage entscheiden:

- **Passendes Pattern existiert** → ergänzen: neue Beleg-Zeile, ggf. neue Vor-/Nachteile, Konfidenz neu ableiten (mehrere unabhängige Quellen → `mehrfach-belegt`; im Repo nachgeprüft → `verifiziert`). Bestehende Beleg-Zeilen niemals umschreiben.
- **Kein passendes Pattern** → neues anlegen. Schwelle: Das Konzept ist benennbar, über die konkrete Quelle hinaus wiederverwendbar und nicht bloß eine Konfiguration. Ein Pattern muss einen Namen tragen, den man in einem Gespräch verwenden kann.
- **Widerspruch zum Bestand** → im betroffenen Pattern unter „Spannungen & offene Fragen" als Trade-off festhalten, mit beiden Quellen und Datum. Nicht glätten, nicht die neuere Quelle automatisch gewinnen lassen.
- **Zeitgebundene Aussage** überholt eine ältere → datierten Vermerk ergänzen („bis 2026-07 galt …, seit … "), nie löschen.

Zusätzlich prüfen: Ergibt sich aus der Erkenntnis eine Änderung an einem bestehenden Workflow in `20_Workflows/` oder Skill in `30_Skills/local/`? Dann **vorschlagen**, nicht eigenmächtig ändern — Skills und Workflows sind produktiv.

### 8. Vergleiche und Index aktualisieren

Betroffene Notizen in `80_Knowledge/Vergleiche/` aktualisieren und deren Stand-Datum setzen. Neue Patterns und Vergleiche in `80_Knowledge/Index.md` mit einem Einzeiler eintragen.

### 9. Status in der Inbox fortschreiben

In der verarbeiteten Inbox-Notiz das Frontmatter aktualisieren:

```yaml
status: verarbeitet
verarbeitet_am: YYYY-MM-DD
source_notiz: 80_Knowledge/Sources/<datei>.md
```

Ohne diesen Schritt erscheint die Quelle beim nächsten Lauf erneut als offen. Am Inhalt der Inbox-Notiz sonst nichts ändern — sie ist das Rohmaterial.

### 10. Validator ausführen

```powershell
python 70_Scripts/validate_knowledge.py
```

**Wichtig:** Das Repo hat vorbestehende Validator-Fehler in Altdateien (Stand 2026-08-04: 60, überwiegend gemischte Anführungszeichen). Maßstab ist deshalb:

- Jeder Fehler in einer **in diesem Lauf geschriebenen oder geänderten** Datei muss behoben werden.
- Vorbestehende Fehler in nicht angefassten Dateien nicht stillschweigend mitreparieren — sie gehören nicht zu diesem Lauf. Ihre Zahl vor und nach dem Lauf vergleichen und im Resümee nennen.
- Niemals „Validator grün" melden, wenn er das nicht ist. Stattdessen: „keine neuen Fehler, N vorbestehende unverändert".

Typografie-Regel, die die meisten Fehler verursacht: deutsche Anführungszeichen konsequent als `„…"` (U+201E öffnend, U+201C schließend), niemals gemischt mit ASCII `"`.

### 11. Diff-Resümee ausgeben

Format siehe unten. Bei einem Sammel-Lauf zuerst eine Zeile pro Quelle, dann die aggregierten Änderungen.

## Fehler-Gates

- Bilder nicht gelesen, aber Zahlen aus dem Text übernommen, die im Bild präziser stehen → unvollständig, nachholen.
- Zwei Quellen widersprechen sich und du legst dich fest, ohne die Spannung zu dokumentieren → verboten.
- Pattern angelegt, das nur die Quelle umformuliert und keinen eigenständigen Namen verdient → stattdessen Beleg an bestehendes Pattern hängen.
- Status in der Inbox nicht fortgeschrieben → Lauf gilt als unvollständig.
- Erfolg gemeldet, ohne den Validator laufen zu lassen → verboten.
- Bei unklarer Zuordnung raten → Frage nach `00_Inbox/Fragen_an_Philipp.md`, Quelle bleibt `status: neu`.
- Produktive Skills oder Workflows eigenmächtig geändert → verboten, nur vorschlagen.

## Häufige Fehler

- Quelle Abschnitt für Abschnitt paraphrasieren statt nach Konzepten und Lernlogik zu ordnen.
- Jede Quelle isoliert verarbeiten, obwohl zwei offene Quellen dasselbe Thema behandeln — der Quervergleich ist der eigentliche Wert.
- Versionsabhängige Konfigurationen (Flags, Preise, Modellnamen) als zeitlose Erkenntnis formulieren, ohne Stand-Datum.
- Konfidenz auf `mehrfach-belegt` heben, obwohl beide Belege auf dieselbe Primärquelle zurückgehen (ein Tweet und seine Zusammenfassung sind eine Quelle).
- Vorbestehende Validator-Fehler als eigene behandeln und dabei Altdateien umschreiben.
- Zahlen aus Marketing-Material ungeprüft übernehmen (selbstberichtete Benchmarks, Vendor-eigene Harnesses).

## Ausgabeformat (Diff-Resümee)

```text
Verarbeitet: 3 Quellen (2 eingearbeitet, 1 ignoriert), 1 offen

● <slug> → Sources/<datei>.md
  ✓ Pattern NEU: <Name>
  ✓ Pattern ergänzt: <Name> (+1 Beleg, Konfidenz: meinung → mehrfach-belegt)
  ⚠ Spannung: <ein Satz> → notiert in <Pattern>
● <slug> → ignoriert: <Begründung>

✓ Index aktualisiert (+1 Pattern)
✓ Vergleich aktualisiert: <Name> (Stand 2026-08-04)
→ Vorschlag: <Workflow/Skill> anpassen, weil <Grund> (nicht ausgeführt)
? Offene Frage: <Frage> → 00_Inbox/Fragen_an_Philipp.md
Validator: keine neuen Fehler (60 vorbestehende unverändert)
```
