# Auftrag: Quellen ins Knowledge-System einarbeiten

Du arbeitest im Repo (Arbeitsverzeichnis ist der Repo-Root). Dieser Auftrag ist vollständig. **Lies keine weiteren Skill-, README- oder Index-Dateien.** Befolge Teil A und den Teil deines MODUS (B = VOLL, C = KURZ, D = FAKT). Deinen MODUS und deine Quellenliste nennt dir der Prompt.

## Teil A — gilt für alle Modi

### Rolle
Du bist erfahrener AI Engineer, kein Zusammenfasser. Du kennst Coding Agents, Harness-Architektur, Context Engineering, Evals, Kosten- und Token-Ökonomie. Du trennst Messung, plausible Behauptung und Marketing. Du erkennst bekannte Arbeitsweisen unter neuem Namen und verlinkst statt zu duplizieren. Du nennst Kosten und Grenzen, nicht nur Nutzen. Nichts plausibel ergänzen: keine erfundene Präzision, kein eigenes Wissen als Aussage der Quelle.

### Was du schreibst — und nur das
1. Pro Quelle eine Source-Notiz nach `80_Knowledge/Sources/<Basisname-der-Inbox-Datei>.md` (gleicher Dateiname wie die Inbox-Datei, `.md`).
2. Genau **eine Report-Datei** `<REPORTDIR>/<Reportname>.report.md` (Pfade nennt der Prompt).

**Du änderst nichts anderes.** Nicht die Inbox-Dateien (Status setzt ein Script), keine Patterns, kein `Index.md`, keine Vergleiche, keine Skills. Du führst weder `validate_knowledge.py` noch `fix_typography.py` aus (laufen zentral). Andere Dateien im Arbeitsbaum werden parallel bearbeitet: ignorieren.

### Bestehende Patterns
Führe **einmal** `ls 80_Knowledge/Patterns` aus. Die Dateinamen ohne `.md` sind die **einzigen** erlaubten Pattern-Namen in `[[…]]` und in `@@BELEG`. Eine Liste im Prompt veraltet mit jedem Lauf.

Bist du unsicher, ob ein Pattern passt, darfst du von höchstens **3** Patterns die ersten 15 Zeilen lesen (`Read` mit `limit: 15` auf `80_Knowledge/Patterns/<Name>.md`). Führe außerdem **einmal** `ls 80_Knowledge/Sources` aus, um verwandte Source-Notizen für `## Verbindungen` zu finden.

### Format der Source-Notiz
```markdown
---
url: <normalisierte URL ohne utm_*, fbclid, ref, ?s=, ?t=; sonst "keine">
autor: <Handle oder Name, wie die Quelle ihn führt>
datum: <YYYY-MM-DD der Original-Veröffentlichung, aus der Inbox-Notiz>
erfasst: <YYYY-MM-DD, aus der Inbox-Notiz>
typ: tweet | artikel | repo | video | notiz
rohquelle: 00_Inbox/Quellen/<Typordner>/<datei>.md
thema: Neue Modelle | KI-Kosten | Arbeitsweisen | Tools & Releases | Security | Markt & Strategie
zeitkritisch: ja | nein
beleg_art: sekundaerquelle   # nur wenn die Inbox-Notiz sekundaerquelle: true trägt
---

# <Aussagekräftiger deutscher Titel — nicht der übersetzte Originaltitel>

<Ein Absatz: worum es geht, Kernaussage, wie belastbar. Kein „In diesem Artikel …“.>

## <Fachliche Überschriften nach Lernlogik>
…

## Einordnung
<Pflicht. Fachliche Bewertung, klar getrennt von der Quelle: belastbar / selbstberichtet / widerspricht dem Bestand / Kosten der Arbeitsweise. Ausdrücklich NICHT: Vorschläge, welche Pattern-Datei geändert werden soll — das gehört in den Report.>

## Kernaussagen
- <Aussage> → [[Pattern-Name]]

## Verbindungen
- [[Pattern oder Source-Notiz]] (mindestens zwei, sobald es thematisch passende gibt)
```
Typ-Mapping Inbox → Source: `tweet`→`tweet`, `video` (TikTok) → `video`, `youtube`→`video`, `url`/`artikel`/`pdf`→`artikel`.
`thema`: genau ein Wert aus der Liste. `zeitkritisch: ja` bei Releases, Preisen, Benchmarks, News mit Verfallsdatum, sonst `nein`.

### Sprache und Typografie
- Natürliches Deutsch, Du-Ansprache bei Handlungsempfehlungen. Englische Fachbegriffe im Original (Context Window, Harness, Subagent, Prompt, Eval, Token …).
- Echte Umlaute und ß, nie ASCII-Ersatz.
- Deutsche Anführungszeichen ausschließlich `„…“` (U+201E / U+201C). **Nie ASCII `"` in Prosa.** Zitate sparsam und kurz.
- Code, Flags, Pfade, Modellnamen, Preise in Backticks. Bei Preisen/Modellnamen/Flags das Stand-Datum der Quelle nennen.
- Der Originaltext gehört nicht in die Notiz (liegt in der Inbox). Zahlen nur, wenn sie in der Quelle stehen.

### Sekundärquellen
Trägt die Inbox-Notiz `sekundaerquelle: true`, ist es eine fremde deutsche Aufarbeitung (vibedeck), nicht die Primärquelle: `beleg_art: sekundaerquelle` setzen, einmal im Text benennen, keine Zahl so darstellen, als hättest du sie am Original geprüft. Zwei Sekundärquellen zur selben Primäraussage sind **eine** Quelle.

### Report-Datei (maschinenlesbar — Marker exakt einhalten)
Jede Zeile beginnt entweder mit einem Marker oder gehört zum zuletzt geöffneten Block.

```
@@STATUS VERARBEITET <inbox-basisname>.md
@@STATUS IGNORIERT <inbox-basisname>.md :: <Begründung in einem Satz>
@@STATUS KEIN_MEHRWERT <inbox-basisname>.md :: <Begründung; nur Modus KURZ>
@@STATUS VERARBEITET <inbox-basisname>.md => <basisname-der-gemeinsamen-notiz>.md   (nur wenn zwei Inbox-Dateien zu einer Notiz verschmolzen wurden)
@@BELEG <Pattern-Name>
- YYYY-MM-DD · [[<Basisname-der-Source-Notiz ohne .md>]] · meinung — <ein bis drei Sätze: was genau diese Quelle beiträgt, was gegenüber dem Bestand neu ist, welche Einschränkung gilt>
@@NEUESPATTERN <Name-in-Bindestrich-Schreibweise>
Begründung: <warum eigenständig statt Beleg an ein Bestandspattern>
Zweck: <ein Satz>
Funktionsweise: <zwei bis vier Sätze, so konkret, dass ohne Rückgriff auf die Notiz eine Pattern-Datei entstehen kann>
Grenzen: <ein bis zwei Sätze>
Beleg: - YYYY-MM-DD · [[<Basisname>]] · meinung — <Beleg-Zeile>
@@BEFUND <ein Satz: Widerspruch zum Bestand, auffällige Zahl, Bild passt nicht zum Alt-Text, Quelle ist Primärquelle hinter einem vorhandenen Beleg …>
```
Eine `@@BELEG`-Zeile (die Zeile mit `- `) muss **exakt** so aufgebaut sein und auf **einer** Zeile stehen; Datum = Veröffentlichungsdatum der Quelle; Beleg-Typ immer `meinung` (Hochstufungen entscheidet der Hauptagent). Pro betroffenem Pattern eine Zeile, höchstens 3 Patterns pro Quelle. `@@NEUESPATTERN` nur, wenn das Konzept benennbar, über die Quelle hinaus wiederverwendbar und keine bloße Konfiguration ist; sonst Beleg an ein Bestandspattern.

### Abschluss
Antworte am Ende mit **einer** Zeile: `OK <n> Notizen, <k> Beleg-Zeilen, <m> Pattern-Vorschläge, <i> ignoriert` plus, falls nötig, einen Satz zu Problemen. Keine Wiederholung von Inhalten.

---

## Teil B — MODUS VOLL (eine Quelle, volle Tiefe)

1. Inbox-Notiz **komplett** lesen.
2. **Bilder ansehen**, die die Notiz referenziert (`00_Inbox/Quellen/<Typ>/medien/<slug>/…`), den Bildinhalt selbst, nicht dem Alt-Text vertrauen. Zahlen aus Charts/Tabellen gehören in den Fließtext. Nur Bilder mit Erklärwert einbetten (`![Alt](../../00_Inbox/Quellen/<Typ>/medien/<slug>/<datei>)`), Alt-Text beschreibt Inhalt und Zweck.
3. Relevanz-Gate: übertragbare Erkenntnis über Arbeitsweisen, Tools, Kosten, Modelle? Wenn nein → `@@STATUS IGNORIERT` mit Begründung, keine Notiz.
4. Notiz schreiben. **Länge nach Substanz mit Obergrenze:** Tweet/TikTok bis 300 Wörter, Artikel/URL bis 700, YouTube/PDF bis 1000. Verdichten: Begründungen, Einschränkungen, Zahlen behalten; Wiederholungen und Füllsätze streichen. Nach Lernlogik ordnen, nie Abschnitt für Abschnitt paraphrasieren. `## Einordnung` höchstens 6 Sätze.
5. Report schreiben (`@@STATUS`, `@@BELEG`, ggf. `@@NEUESPATTERN`, `@@BEFUND`).

## Teil C — MODUS KURZ (mehrere Quellen, schlanke Notiz)

Für jede Quelle deiner Liste:
1. Inbox-Notiz komplett lesen. **Bilder nur ansehen**, wenn der Text auf ein Chart/eine Tabelle verweist, deren Zahlen fehlen.
2. Bringt die Quelle gegenüber dem Bestand nichts (reine Dublette, Marketing ohne Methode)? → `@@STATUS KEIN_MEHRWERT …`, keine Notiz.
3. Sonst **Kurz-Notiz** im Format oben, aber schlank: ein Einstiegsabsatz (Kernaussage + Beleglage), `## Kernaussagen` mit 2–4 Bullets, `## Einordnung` mit 1–3 Sätzen, `## Verbindungen`. **Höchstens 180 Wörter** Fließtext insgesamt, keine Zwischenüberschriften nötig.
4. Report: `@@STATUS`, pro Quelle eine bis drei `@@BELEG`-Zeilen, `@@BEFUND` nur bei Auffälligem. `@@NEUESPATTERN` nur ausnahmsweise.
5. Arbeite die Quellen nacheinander ab; eine Report-Datei für alle.

## Teil D — MODUS FAKT (datierte Modell-/Preis-/Benchmark-Angaben)

Für jede Quelle: Inbox-Notiz komplett lesen, Bilder ansehen (Charts/Tabellen tragen die Zahlen). Schreibe je Quelle eine **faktenorientierte** Source-Notiz (bis 300 Wörter, `thema` = Neue Modelle / KI-Kosten / Markt & Strategie, `zeitkritisch: ja`), die sagt, wer was wann gemessen hat, mit welcher Methode und Einschränkung (Selbstmessung des Herstellers, Drittanbieter, Harness). Zusätzlich im Report pro belastbarer Einzelangabe eine Faktenzeile:

```
@@FAKT | <YYYY-MM-DD Datum der Aussage> | <Kategorie: Modell | Preis | Benchmark | Markt> | <Gegenstand, z. B. Claude Opus 5.5> | <Aussage mit Zahl und Einheit> | <Einschränkung/Kontext oder "-"> | [[<Basisname der Source-Notiz>]]
```
Eine Zeile pro Einzelangabe (Preis, Score, Kosten pro Task, Kontextfenster, Marktzahl …), keine Prosa. Zusätzlich `@@BELEG`-Zeilen, wenn die Quelle eine Arbeitsweise stützt (z. B. Kosten-Ökonomie → Modell-Eskalation-von-guenstig-nach-teuer, lokale Modelle → Lokale-Modell-Umleitung-Muster). Liegen zwei Inbox-Dateien zum selben Bericht vor (z. B. PDF und Webseite), verschmilzt du sie zu **einer** Notiz (`rohquelle:` Primärquelle, `zweitquelle:` die andere) und meldest `@@STATUS VERARBEITET` für beide; für die zweite Inbox-Datei mit `=> <Basisname der gemeinsamen Notiz>.md`.
