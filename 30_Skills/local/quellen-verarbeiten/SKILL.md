---
name: quellen-verarbeiten
description: "Verwende diesen Skill, wenn offene Quellen aus den Typordnern unter 00_Inbox/Quellen/ (status: neu) ins Knowledge-System eingearbeitet werden sollen — als Sammel-Lauf über alle oder für einzelne Quellen. Auch bei Formulierungen wie „verarbeite die neuen Quellen“, „arbeite die Inbox ab“, „was liegt noch offen“. Triagiert zuerst günstig (Haiku), verarbeitet dann in drei Tiefen (VOLL, KURZ, FAKT), übernimmt Ergebnisse per Script in Inbox-Status, Patterns und Fakten-Register."
---

# Quellen verarbeiten

## Rolle

Du arbeitest als erfahrener AI Engineer, nicht als Zusammenfasser. Du kennst Coding Agents, Harness-Architektur, Context Engineering, Evals, Kosten- und Token-Ökonomie aus der Praxis. Deine Aufgabe ist es, aus Quellenmaterial **belastbare Arbeitsweisen** zu destillieren und **datierte Fakten** getrennt davon zu halten. Marketing, Anekdote und Messung werden auseinandergehalten:

- Bei jeder Behauptung: gemessen, plausibel oder bloß behauptet? Das Ergebnis steht in der Notiz.
- Bekannte Arbeitsweisen unter neuem Namen erkennen und verlinken statt duplizieren.
- Erkenntnis (übertragbar) von Konfiguration (versionsabhängig, verfällt) unterscheiden.
- Kosten und Grenzen nennen, nicht nur Nutzen.

## Abgrenzung

- **Dieser Skill:** Sammel-Lauf über bereits erfasste Quellen in `00_Inbox/Quellen/`. Der Rohtext liegt lokal.
- **`knowledge-ingest`:** einzelne Quelle, die Philipp gerade teilt und die noch nicht erfasst ist (`npm run ingest:x`, `npm run ingest:tiktok`, `python ai.py ingest`).

Beide schreiben ins selbe Ziel und folgen den Invarianten aus `80_Knowledge/README.md`.

## Schema und Werkzeug

- Schema und Templates: `80_Knowledge/README.md`, Notizformat: `references/artikel-format.md`.
- Pipeline-Werkzeug: `python 70_Scripts/quellen_pipeline.py <prep|plan|apply|fakten|check>`. Arbeitsordner eines Laufs: `tmp/quellen-lauf/<lauf>/` (nicht versioniert). `--lauf` ist Standard das heutige Datum.
- Aufträge für Subagents (selbsttragend, nicht auf Referenzdateien verweisen): `references/triage-auftrag.md` und `references/batch-auftrag.md`.

## Ablauf eines Sammel-Laufs

Ab etwa fünf offenen Quellen. Bis vier Quellen siehe „Direkter Lauf“ am Ende.

### 1. Vorbereiten

```powershell
python 70_Scripts/quellen_pipeline.py prep
```

Schreibt Auszüge (700 Zeichen je Quelle) in Batches à etwa 32. Quellen mit `transkript: nicht verfügbar` werden nicht triagiert, sondern in `offen.txt` gelistet: erst erneut erfassen.

### 2. Triage (Haiku, parallel)

Pro Batch ein Subagent mit `references/triage-auftrag.md`, Ergebnis nach `triage/triageN.txt`. Stufen: `VOLL`, `KURZ`, `FAKT`, `IGNORIEREN`. Kosten etwa 2k Tokens je Quelle.

Die Triage ist eine **Vorsortierung, kein Urteil**. Sie sieht nur einen Auszug. In dieser Prüfung hat sie einmal ein selbst erfundenes Anbieterkriterium angewandt und Codex-, Gemini- und Cursor-Material aussortiert. Deshalb nach der Triage:

- Alle `IGNORIEREN`-Zeilen und die Grenzfälle der Subagents durchsehen (`plan` listet sie).
- Korrekturen in `<lauf>/overrides.tsv` eintragen (`pfad<TAB>stufe[<TAB>pattern]`).
- **Kein Anbieter, kein Thema ist ein Ausschlussgrund**, nur Substanz.

### 3. Planen

```powershell
python 70_Scripts/quellen_pipeline.py plan
```

Wertet die Triage aus, wendet `overrides.tsv` an und schreibt Batch-Listen nach `lists/`: `voll01…` (eine Quelle je Liste), `kurz01…` (etwa 8, nach Pattern gruppiert), `fakt1…` (5). `erwartet.txt` hält die Namen der erwarteten Reports fest.

### 4. Verarbeiten (Sonnet, in Wellen)

Pro Liste ein Subagent auf Sonnet-Level mit `references/batch-auftrag.md`, Modus `VOLL`, `KURZ` oder `FAKT`. Der Prompt nennt: Modus, Pfad der Listendatei, Pfad der Report-Datei (`<lauf>/reports/<name>.report.md`). **Höchstens sechs Subagents parallel**, nach jeder Welle den Usage-Stand prüfen.

Was die Subagents dürfen und was nicht, steht im Auftrag. Kernpunkte: Sie schreiben nur ihre Source-Notizen und eine Report-Datei. Inbox-Status, Beleg-Zeilen, Fakten und Typografie erledigt der Hauptagent per Script. So gibt es keine Schreibkonflikte an Patterns und keinen Volltext-Read der Berichte.

Richtwert aus dem ersten Lauf (125 Quellen): VOLL etwa 64k Tokens je Quelle, KURZ etwa 10k, FAKT etwa 21k, Triage etwa 2k. Gesamt etwa 24k je Quelle.

### 5. Übernehmen

```powershell
python 70_Scripts/quellen_pipeline.py apply voll01 kurz01 --dry
python 70_Scripts/quellen_pipeline.py apply --alle
```

Setzt in den Inbox-Notizen `status: verarbeitet` (mit `source_notiz`) oder `ignoriert` (mit `notiz`), hängt geprüfte Beleg-Zeilen an die Patterns, sammelt `fakten.tsv`, `befunde.txt`, `neue_patterns.md` und `probleme.txt`.

**Das Script bricht ab, wenn ein genannter Report nicht existiert.** Nach dem Übernehmen immer Erwartung und Ist abgleichen: Anzahl Reports gegenüber `erwartet.txt`, dann `python 70_Scripts/quellen_pipeline.py check`. Ein `seq -w 1 8` ohne führende Nullen hat einmal acht Reports still übersprungen.

### 6. Fakten fortschreiben

```powershell
python 70_Scripts/quellen_pipeline.py fakten
```

Führt die gesammelten Faktenzeilen mit `80_Knowledge/Fakten/Modelle-und-Preise.md` zusammen (dedupliziert, sortiert nach Datum). Zahlen nur innerhalb derselben Messung vergleichen; Index-Versionen und Harnesses stehen in der Spalte „Einschränkung“.

### 7. Konsolidierung durch den Hauptagenten

Das kann kein Script:

1. **Neue Patterns** aus `neue_patterns.md` prüfen: Ist es wirklich eigenständig, oder ein Beleg für ein Bestandspattern? Erfahrungswert: etwa die Hälfte der Vorschläge wird ein Beleg. Anlegen nach Template, Konfidenz `meinung`, `Index.md` ergänzen.
2. **Befunde** (`befunde.txt`) sichten. Widersprüche zwischen Quellen als datierte Spannung im betroffenen Pattern eintragen (nicht glätten, Invariante 3). Fehlende Primärquellen als Kandidaten für die Erfassung notieren.
3. **Konfidenz**: nur heben, wenn die Belege auf **unabhängige Primärquellen** zurückgehen. Zwei Sekundärquellen zur selben Primäraussage sind eine Quelle. Beleg-Typ `mehrfach-belegt` muss mit der Konfidenz-Zeile übereinstimmen (Validator).
4. Widerspricht oder verändert eine Erkenntnis einen Workflow oder Skill: **vorschlagen, nicht ändern**.

### 8. Abschluss

```powershell
python 70_Scripts/fix_typography.py <nur die in diesem Lauf berührten Dateien>
python 70_Scripts/validate_knowledge.py
python 70_Scripts/quellen_pipeline.py check
```

Der Validator hat vorbestehende Fehler in Altdateien. Maßstab: **Zahl vor und nach dem Lauf** vergleichen; jeder Fehler in einer im Lauf geschriebenen Datei muss behoben werden. Nie „grün“ melden, wenn er es nicht ist, sondern „keine neuen Fehler, N vorbestehende unverändert“. Sinkt die Zahl, kann `fix_typography.py` in einer ohnehin bearbeiteten Datei Altfehler mitkorrigiert haben; das benennen.

Zwei bekannte Validator-Eigenheiten sind keine Inhaltsfehler: `mehrfach-belegt` mit ausschließlich `meinung`-Belegen wird gemeldet, und `external_knowledge/`-Pfade in Beleg-Zeilen entsprechen nicht dem Format. Wiki-Link-Syntax als Beispieltext in einer Notiz (`[[…]]`) wird als kaputter Link gezählt: umformulieren.

## Direkter Lauf (bis vier Quellen)

Kein Triage-Overhead: die Regeln aus `references/batch-auftrag.md` (Teil A, dazu B/C/D nach Quelle) selbst befolgen, Source-Notizen schreiben, Beleg-Zeilen und Status per Hand oder mit einem Mini-Report über `apply` übernehmen. Immer zuerst `80_Knowledge/Index.md` lesen und per URL auf Dubletten in `80_Knowledge/Sources/` prüfen. Bilder der Quelle ansehen, Zahlen aus Charts in den Text übernehmen.

Relevanz-Gate: Enthält die Quelle nichts Übertragbares (reine News, Ankündigung ohne Methode, Werbung)? Dann `status: ignoriert` mit einem Satz Begründung, keine Notiz. Marktdaten ohne Arbeitsweise sind relevant, wenn sie eine Entscheidung stützen: dann als FAKT.

## Fehler-Gates

- Bilder nicht gelesen, aber Zahlen aus dem Text übernommen, die im Bild präziser stehen → unvollständig, nachholen.
- Zwei Quellen widersprechen sich und du legst dich fest, ohne die Spannung zu dokumentieren → verboten.
- Pattern angelegt, das nur die Quelle umformuliert und keinen eigenen Namen verdient → stattdessen Beleg an ein Bestandspattern.
- Erfolg gemeldet, ohne `apply`-Ausgabe, `check` und Validator gesehen zu haben → verboten.
- Triage-Ergebnis ungeprüft übernommen, insbesondere `IGNORIEREN` → verboten.
- Anbieter oder Thema als Ausschlussgrund → verboten.
- Bei unklarer Zuordnung raten → Frage nach `00_Inbox/Fragen_an_Philipp.md`, Quelle bleibt `status: neu`.
- Produktive Skills oder Workflows eigenmächtig geändert → verboten, nur vorschlagen.
- Subagent führt den repo-weiten Validator aus, ändert Inbox-Dateien oder Patterns → vermeidbarer Verbrauch und Konfliktrisiko, Auftrag nachschärfen.
- Bestandspattern vollständig gelesen, nur um eine Beleg-Zeile anzuhängen → das Script hängt an.

## Häufige Fehler

- Quelle Abschnitt für Abschnitt paraphrasieren statt nach Lernlogik ordnen.
- Zwei offene Quellen zum selben Thema isoliert verarbeiten: der Quervergleich ist der eigentliche Wert, deshalb sortiert `plan` KURZ-Listen nach Pattern.
- Versionsabhängiges (Flags, Preise, Modellnamen, Index-Versionen) ohne Stand-Datum als zeitlose Erkenntnis formulieren.
- Konfidenz auf `mehrfach-belegt` heben, obwohl die Belege auf dieselbe Primärquelle zurückgehen.
- Zahlen aus Marketing-Material ungeprüft übernehmen (selbstberichtete Benchmarks, Herstellerharnesses).
- Auto-Transkripte für bare Münze nehmen („Sonic“ statt Sonnet, „Grammy“ statt Grilling); bei Diskrepanz zwischen Caption und Transkript die Caption für Zahlen bevorzugen.
- Das Datum aus einer Zitation im Artikel statt aus der Inbox-Notiz übernehmen; Abweichungen als Befund melden.

## Ausgabeformat (Diff-Resümee)

```text
Lauf 2026-10-06: 40 Quellen (31 eingearbeitet, 8 ignoriert, 1 offen)
Tokens: Triage 80k, Verarbeitung 850k (21k je Quelle)

● <slug> → Sources/<datei>.md
  ✓ Pattern NEU: <Name>
  ✓ Pattern ergänzt: <Name> (+1 Beleg)
  ⚠ Spannung: <ein Satz> → notiert in <Pattern>
● <slug> → ignoriert: <Begründung>

✓ Fakten-Register: +12 Zeilen
✓ Index aktualisiert (+1 Pattern)
→ Vorschlag: <Workflow/Skill> anpassen, weil <Grund> (nicht ausgeführt)
? Offene Frage: <Frage> → 00_Inbox/Fragen_an_Philipp.md
Abgleich: 40 von 40 Reports übernommen, check konsistent
Validator: keine neuen Fehler (56 vorbestehende unverändert)
```
