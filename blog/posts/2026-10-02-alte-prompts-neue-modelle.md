---
titel: "Neues Modell, alte Prompts: Was du aus AGENTS.md und Skills streichen solltest"
datum: 2026-10-02
kategorie: arbeitsweisen
zusammenfassung: "Anweisungen veralten mit dem Modell. Welche Regeln du nach einem Modellwechsel aus AGENTS.md und Skills streichst, wie du Skills zu Routern mit engen Triggern umbaust und wie du prüfst, ob eine Regel noch nützt."
status: freigegeben
geprueft_am: 2026-10-02
quellen:
  - 2026-09-14-developers-rethinking-skills-and-prompts-for-gpt-6-astra-op
  - 2026-09-04-pvncher-2095991462416490862
  - 2026-09-07-sairahul1-2096902575035683147
  - 2026-09-19-voxyz_ai-2101355643882065971
  - 2026-02-26-omarsar0-agents-md-evaluation
---

## Kurz gesagt

- Regeln, die ein älteres Modell zum Testen, Prüfen und Weitermachen gedrängt haben, bremsen ein stärkeres. Nach jedem Modellwechsel gehört jede Zeile in AGENTS.md und in deinen Skills auf den Prüfstand.
- Skills beschreibst du über einen engen Auslöser und baust sie als schlanke Router, die Details erst bei Bedarf nachladen.
- Statt Einzelschritten gibst du ein prüfbares Endergebnis, eine Stop-Bedingung und eine Berichtspflicht vor.
- Ob eine Streichung hilft, zeigt nur der Vergleich an echten Aufgaben vorher und nachher.

## Das Problem

Wer ein Jahr mit Coding-Agents arbeitet, sammelt Anweisungen an: „Lies vor jeder Änderung die Architektur-Doku“, „Prüfe deine Arbeit“, „Führe immer alle Tests aus“, „Ändere niemals Dateien außerhalb von src“. Jede Regel hatte einmal einen Grund, meist ein Modell, das zu früh aufhörte oder zu forsch war.

OpenAI beschreibt im Entwicklerblog vom 14.09.2026, was mit solchen Regeln beim Wechsel auf GPT-6 Astra passiert: Das Modell testet und prüft von selbst, alte Testaufforderungen erzeugen zusätzliche, unnötige Testläufe {q:1}. Harte Verbote, die ein eigenmächtiges Vorgängermodell bremsen sollten, nimmt Astra so ernst, dass es stoppt, wo du es weiterarbeiten lassen würdest {q:1}. Eric Provencher hat denselben Text als Artikel auf X verbreitet {q:2}. Beide beschreiben Erfahrungen mit einem Modell, ohne Messwerte. Der Mechanismus gilt allgemein. Eine Anweisung gleicht eine Schwäche des Modells aus, und fällt die Schwäche weg, bleibt nur ihr Preis.

Laut einem Praxisleitfaden von @sairahul1 führen widersprüchliche Regeln zwischen AGENTS.md, Skill und Task-Prompt bei Astra zu Pausen und frühem Abbruch {q:3}. Er empfiehlt, festzulegen, welche Datei bei einem Konflikt gewinnt.

## Was du streichst und was du umbaust

| Regel vorher | Problem mit stärkerem Modell | Nachher |
|---|---|---|
| „Vor jeder Änderung architecture.md, database.md und deployment.md lesen“ | Verbrennt Kontext, auch bei einem Tippfehler | Jede Datei mit Anlass nennen: Architektur bei Service-Grenzen, Datenbank bei Schemaänderungen, Deployment vor einem Release {q:1} |
| „Teste immer alles, prüfe deine Arbeit“ | Das Modell testet ohnehin, die Regel erzeugt Zusatzläufe | Streichen und durch eine Abnahmebedingung ersetzen (siehe unten) |
| „Frag vor jedem Testlauf nach“ | Das ohnehin zögerliche Modell hält bei jedem Schritt an | Sichere Abläufe vorab freigeben: lokale Tests mit Wegwerf-Fixtures, ohne Produktionszugriff, Fehler beheben und erneut testen, ohne zu fragen {q:2} |
| „Nach dem ersten Entwurf zur Review anhalten“ | Zieht das Modell zu früh zum Stopp | Fertigstellung definieren: lauffähig machen, Ergebnis prüfen, Fehler beheben {q:1} |
| „Think step by step“ | Gibt Denkschritte vor, die das Modell selbst wählt | Streichen. Reasoning steuerst du über die Effort-Einstellung der API {q:3} |

Zur richtigen Effort-Stufe gibt es einen eigenen [Check mit fünf Aussagen](post:check-effort-stufen).

## Skills als Router mit engem Trigger

Name und Beschreibung jedes Skills liegen dauerhaft im Kontext. Hast du zu viele Skills, kürzt Codex die Beschreibungen selbst, das Modell sieht pro Skill weniger und wählt schlechter {q:1}. Werbende oder überlappende Beschreibungen laden Skills, die nicht helfen.

Die Beschreibung nennt deshalb nur den Auslöser. OpenAI zeigt den Unterschied an einem Migrations-Skill {q:1}:

```text
Vorher:  Use when working with databases, queries, models, or persistence.
Nachher: Use when adding or changing a migration, or reviewing its rollout.
```

Die erste Fassung lädt den Skill bei jeder Berührung mit der Datenbank, die zweite nur bei einer Migration.

Der Inhalt eines Skills mit mehreren Workflows wird zum Router: eine kurze Hauptdatei, die auf Unterdokumente und Skripte zeigt {q:2}. Jeder gelesene Skill kostet Kontext und bringt die Compaction näher, mehr dazu im [Entscheidungsbaum zur Kontext-Hygiene](post:kontext-hygiene-entscheidungsbaum). Detaillierte Schritt-für-Schritt-Rezepte nennt OpenAI ausdrücklich als Fehler, weil sie ein Modell, das mit Mehrdeutigkeit umgehen kann, eher einschränken als leiten {q:1}.

## Ergebnis vorgeben statt Schritte

Ohne Testregeln fehlt dem Agenten die Antwort darauf, wann er fertig ist. Die gibst du als prüfbares Endergebnis vor. @Voxyz_ai hat sieben Rollen-Prompts veröffentlicht, die genau das tun: Der Agent führt die Aufgabe bis zu einem sichtbaren oder prüfbaren Ergebnis, fragt nur bei Entscheidungen, Zugriffen oder Scope-Änderungen nach und meldet am Ende Ergebnis, Nutzung, geprüfte und offene Punkte {q:4}. Belege für bessere Ergebnisse liefert der Thread nicht, die Struktur ist aber übertragbar.

Ein Beispiel:

```text
Vorher:  Fix the login bug. Run all tests. Check your work. Keep going until done.

Nachher: Ziel: Login funktioniert wieder nach Session-Ablauf.
         Fertig, wenn: alle betroffenen Routen liefern 200, keine TypeScript-Fehler.
         Frag nur bei Änderungen am Datenmodell.
         Bericht: Ursache, Änderung, was du geprüft hast, was offen ist.
```

Die Stop-Bedingung stammt sinngemäß aus dem Leitfaden von @sairahul1, der „keep going until done“ durch ein prüfbares Kriterium ersetzt {q:3}. Er empfiehlt außerdem, den Prüfaufwand am Risiko auszurichten: Für einen CSS-Abstand reicht der kleinste relevante Test, eine Änderung an der Session-Wiederherstellung braucht Unit- und Integrationstests und den Durchlauf von Login bis Ablauf {q:3}.

„Prüfe dich selbst“ als Pauschalregel kostet bei einem starken Modell Tokens, eine konkrete Abnahmebedingung mit Berichtspflicht bleibt nützlich. Du schreibst vor, was am Ende stimmen muss, das Modell wählt den Weg.

## Wie du prüfst, ob eine Regel noch nützt

@sairahul1 schlägt ein Raster mit acht Blöcken vor: Goal, Context, Priority, Autonomy, Tools, Output, Verify, Stop {q:3}. Jeder Block soll einen bestimmten Fehler verhindern. Kannst du den Fehler nicht benennen, fliegt der Block raus. Dieselbe Frage stellst du jeder Zeile deiner AGENTS.md: Welches Fehlverhalten des aktuellen Modells verhindert sie, und hast du es zuletzt beobachtet?

Eine Studie der ETH Zürich spricht für diese Strenge. Auf AGENTbench mit 138 Aufgaben aus 12 Python-Repos senkten automatisch erzeugte Kontextdateien die Erfolgsquote gegenüber gar keiner Datei und erhöhten die Kosten um über 20 % {q:5}. Von Menschen geschriebene Dateien brachten 4 % mehr Erfolg. Jede Kontextdatei kostete 14 bis 22 % mehr Reasoning-Tokens, egal ob sie half {q:5}. Die Agenten befolgten die Anweisungen genau und suchten gründlicher, fanden die richtige Stelle aber nicht öfter. Geholfen hat nur, was nirgendwo sonst im Repo steht. Getestet wurden ältere Modelle wie Sonnet 4.5 und GPT-5.2, die Richtung passt aber zu den Erfahrungen mit Astra.

Prüfe deine Streichungen deshalb an echten Aufgaben. Nimm zehn aus deinem Alltag, lass sie mit alter und neuer Fassung laufen und zähle Nacharbeit und Tokens. Umbauten nicht so zu vergleichen, führt @sairahul1 ausdrücklich als Fehler {q:3}. Wie du so eine Messung gegen Selbsttäuschung absicherst, steht im Beitrag zu [Hillclimbing mit Holdout](post:hillclimbing-mit-holdout).

## Kosten und Grenzen

- Jeder Modellwechsel kostet ein Audit, und ohne Vergleichslauf verwechselst du „kürzer“ mit „besser“.
- Repository-Skills steuern auch die Agents anderer Mitwirkender, die vielleicht ein schwächeres Modell nutzen {q:1}. Eine Leitplanke, die du für Astra streichst, kann dort fehlen. Bei gemischten Teams gibt es keine Fassung, die für alle stimmt.
- OpenAI und @sairahul1 empfehlen, das Modell selbst ein Audit der eigenen Anweisungen machen zu lassen {q:1}{q:3}. Das ist bequem, aber ungeprüft. Automatisch erzeugte Kontextdateien schnitten in der ETH-Studie am schlechtesten ab {q:5}. Lass das Modell Kandidaten vorschlagen und entscheide selbst.
- „Nicht nach jedem Schritt fragen“ erhöht das Risiko, dass ein Agent lange in die falsche Richtung läuft {q:4}. Eine Freigabe gilt deshalb nur für Abläufe, die du als sicher kennst.

## Checkliste nach dem Modellwechsel

1. Lege fest, welche Datei bei Konflikten gewinnt: AGENTS.md, Skill oder Task-Prompt.
2. Streiche pauschale Test- und Selbstprüfungsregeln. Ersetze sie pro Aufgabentyp durch eine Abnahmebedingung.
3. Ersetze Pflichtlektüre durch Verweise mit Anlass.
4. Lies jedes „niemals“ und „immer“ neu. Behalte es nur, wenn es einen echten Schaden verhindert, und gib sichere Abläufe ausdrücklich frei.
5. Kürze jede Skill-Beschreibung auf den Auslöser und entferne Skills, die sich überschneiden.
6. Baue lange Skills zu einer kurzen Hauptdatei mit Verweisen um.
7. Ersetze „mach weiter, bis es fertig ist“ durch ein prüfbares Kriterium und eine Berichtspflicht.
8. Lass zehn echte Aufgaben mit alter und neuer Fassung laufen und behalte nur die Änderungen, die Nacharbeit oder Tokens senken.
