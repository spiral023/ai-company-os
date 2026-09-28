# Auftrag: Triage offener Quellen

**Vorlage für den Prompt an einen Haiku-Subagent.** Vor dem Dispatch `BATCHFILE` und `ERGEBNISDATEI` einsetzen (Pfade liefert `quellen_pipeline.py prep`). Pro Batch ein Subagent, alle Batches parallel. Kosten: etwa 2k Tokens je Quelle.

---

## --- AUFTRAG ---

Triage-Auftrag (nur lesen, keine Repo-Dateien ändern). Lies die Datei `BATCHFILE`. Sie enthält pro Quelle einen Block: Pfad, Dateigröße, Metadaten und einen Auszug (die ersten 700 Zeichen). Beurteile **jede** Quelle anhand dieses Auszugs. Öffne die Originaldatei nur, wenn der Auszug für die Entscheidung nicht reicht (Ausnahme, nicht Regel).

**Kontext:** Wissensbasis für Leute, die mit KI arbeiten oder coden. Behandelt werden alle Anbieter und Werkzeuge gleichwertig (Anthropic, OpenAI, Google, Open-Source-Modelle, Cursor, Codex, Claude Code …). **Ein Anbieter ist nie ein Grund zum Aussortieren.** Führe einmal `ls 80_Knowledge/Patterns` aus; die Dateinamen ohne `.md` sind die bestehenden Patterns.

**Vergib pro Quelle:**

- **STUFE**
  - `VOLL`: neue, belegte oder primäre Erkenntnis, die kein bestehendes Pattern abdeckt, oder eine Quelle mit vielen Details, Zahlen oder Bildern (lange Artikel, YouTube, PDF).
  - `KURZ`: bestätigt oder ergänzt ein bestehendes Pattern; eine Beleg-Zeile genügt. Auch Primärdokumentation zu einem bekannten Feature gehört hierher, weil sie ein Pattern belegt.
  - `FAKT`: enthält datierte Modell-, Preis-, Benchmark- oder Marktangaben, die veralten (Release, Preis, Score, Kosten pro Task, Marktanteil).
  - `IGNORIEREN`: Dublette (gleiche Aussage wie eine andere Quelle im Batch oder erkennbar dasselbe Video), reines Marketing ohne Methode, Kurswerbung, Clickbait ohne Substanz. **Nicht** aus Anbieter- oder Themengründen.
- **PATTERN**: bei `KURZ` der passende bestehende Pattern-Name; bei `VOLL` ein Name für ein mögliches neues Pattern oder `keins`; sonst `-`.
- **THEMA** (genau eins): Neue Modelle | KI-Kosten | Arbeitsweisen | Tools & Releases | Security | Markt & Strategie | Sonstiges
- **AKTUELL**: `ja`, wenn der Inhalt zeitkritisch ist (Release, Preis, Benchmark, News), sonst `nein`.
- **WARUM**: ein deutscher Satz, höchstens 20 Wörter, mit der konkreten Begründung.

Reicht der Auszug nicht für ein Urteil (nur Tags, nur Titel), entscheide nicht `IGNORIEREN`, sondern öffne die Originaldatei oder schreibe `KURZ` mit dem Vermerk „Auszug zu dünn“ im WARUM.

**Ergebnis:** Schreibe die Datei `ERGEBNISDATEI` (UTF-8, mit dem Write-Tool), **eine Zeile pro Quelle**, Felder getrennt durch ` | ` in dieser Reihenfolge:

`PFAD | STUFE | PATTERN | THEMA | AKTUELL | WARUM`

Keine Kopfzeile, keine Leerzeilen. Der Pfad ist exakt der Pfad aus dem Batch.

**Abschlussantwort:** Nur: Anzahl Zeilen, Verteilung der Stufen und die drei Fälle, bei denen du dir am unsichersten warst (Pfad, kurzer Grund).
