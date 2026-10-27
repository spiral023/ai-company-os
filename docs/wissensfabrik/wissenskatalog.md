# Wissenskatalog bedienen

**Stand:** 2026-10-25. Lokale Grundlage für Recherche und wiederholbare Gesamtanalysen; ohne neue Python-Abhängigkeiten, Modelle oder Netzwerkzugriff.

**Ergänzung 2026-10-26:** `wissen kontext`, `pilot-check` und `karten` bedienen den [semantischen Pilot](../../80_Knowledge/Factory/README.md) direkt aus seinen führenden Dateien. Diese Befehle benötigen keinen Neuaufbau des Volltextindexes; dessen gespeicherter Snapshot bleibt eine gesonderte Sicht.

## Befehle

Im Repo-Root:

```powershell
python ai.py wissen index
python ai.py wissen status
python ai.py wissen suche "software factory"
python ai.py wissen suche "review" --repo cursor/plugins --limit 5
python ai.py wissen suche "spec" --art skill --limit 5
python ai.py wissen lesen "80_Knowledge/Patterns/Handoff-Doc.md" --von 1 --bis 30
python ai.py wissen analyse-plan --ausgabe .wissen/analysen/baseline-01.json
```

Die Ausgabe ist JSON. `index` erstellt `.wissen/index.sqlite` zunächst als temporäre Datei und ersetzt den bisherigen Katalog erst nach erfolgreichem Schreiben. `.wissen/` ist lokal und von Git ausgeschlossen. Ein schreibender Indexlauf sollte jeweils einzeln laufen.

`status` beschreibt den **gespeicherten Snapshot**. Es führt keinen erneuten Scan aus. Nach Änderungen oder Repo-Updates erneut `index` starten. `--max-bytes` steuert das Dateigrößenlimit beim Indexieren, Standard ist 1.000.000 Bytes; übergroße Texte werden ausdrücklich ausgeschlossen und nicht abgeschnitten.

## Eingänge und Umfang

- Eigene Wissensbereiche `00_Inbox` bis `90_Archive`, `docs`, `reports`, Root-Einstiegsdateien sowie externer Index und Changelog. Die genaue Pfadliste steht in `70_Scripts/wissen.py` (`OWN_ROOTS`).
- Alle erkannten Git-Checkouts unter `external_repos/<owner>/<repo>/`.
- Die vorhandene separate Kopie `external_knowledge/ai-llm-wiki/`.
- In den eigenen definierten Wissensordnern auch von Git ignorierte Archive, etwa das gespiegelte AI-Coding-Lexikon. Die Versionierungsentscheidung bestimmt nicht die Auffindbarkeit von Wissen.
- In externen Git-Repos die erfassten Dateien und nicht ignorierten unversionierten Dateien. Bereits versionierte, inzwischen fehlende Dateien bleiben als Lücke sichtbar. Der Cursor-Checkout enthält bewusst nur `pstack`; andere dort verzeichnete Dateien werden dadurch nicht automatisch nachgeladen.

Markdown und weitere dokumentartige UTF-8-Formate werden vollständig nach Überschriften und begrenzten Passagen aufgeteilt. Prompt-/Skill-/Agent-/Playbook-Verzeichnisse sowie als Prompt benannte Codedateien werden ebenfalls textuell erschlossen. Code außerhalb dieser Bereiche und nicht unterstützte Formate bleiben im Inventar mit Ausschlussgrund. Der Katalog führt keine AST-Analyse aus.

Wissens- und Codeverzeichnisse werden nicht beliebig außerhalb dieser Liste gesucht. Ignorierte Downloads oder ein zusätzlicher separat gepflegter Klon müssen vor einer behaupteten Gesamtanalyse ausdrücklich in den Scope aufgenommen werden. Unterrepos/Submodule, die nicht selbst als Eingang entdeckt wurden, sind kein automatisch erschlossener eigener Checkout.

## Herkunft eines Treffers

Ein Suchtreffer liefert Pfad, Zeilenbereich, Überschrift, Textauszug, Repo, Git-HEAD, Dirty-Markierung und SHA-256 des gelesenen Dateiinhalts. Einfache Frontmatter-Felder `url` und `rohquelle` verbinden aufbereitete Notizen mit ihren Originalen. Das ist eine Herkunftsreferenz; Quelle und Ableitung werden dadurch noch nicht automatisch fachlich zusammengeführt oder dedupliziert.

Der Indexsnapshot bezieht Dateipfade, Status, Ausschlussgründe, Größen, gelesene Inhaltshashes und Repo-Zustände ein. Ein Commit allein reicht wegen lokaler Änderungen nicht. Exkludierte Inhalte werden nicht vollständig gehasht; ihr Eintrag ist ein Bestandsnachweis, kein Inhaltsnachweis. Der Zeitpunkt liegt separat in `created`.

Für reine Inventareinträge steht die Größe auf `-1` (nicht erhoben). Das spart bei großen Codebeständen unnötige Dateizugriffe. Der Scan ist kein atomarer Dateisystem-Snapshot; während paralleler Änderungen die Eingänge erneut prüfen beziehungsweise neu indexieren.

## Suche und Grenzen

`suche` verwendet SQLite FTS5 mit BM25 auf Überschriften und Text. Die Wörter der Frage werden als wörtliche Alternativen gesucht; damit ist auch ein ungenauer Einstieg möglich. Es gibt noch keine semantischen Embeddings, Themenexpansion oder inhaltliche Bewertung. `--repo` und `--art` beschränken die Treffer.

`lesen` lädt einen gewählten Originalbereich nach und prüft dabei den Inhaltshash gegen den Snapshot. Geänderte Quellen ergeben einen Fehler mit Aufforderung zur erneuten Indexierung. Pro Abruf sind höchstens 30.000 Zeichen erlaubt; längere Dokumente in expliziten Zeilenbereichen lesen.

Bei einer konkreten Aufgabe den Treffer im Original nachlesen und seine Voraussetzungen prüfen. Für einen Zusammenhang über mehrere Themen mehrere Quellen vergleichen. Für eine Gesamtanalyse den gesonderten Analyseplan verwenden. Eine kleine Trefferliste kann die Abdeckung des Gesamtbestands nicht belegen.

## Auslassungen und Vertraulichkeit

Der Katalog liest keine `.env*`-, Schlüsseldateien oder `secrets/`-Inhalte. Symlinks/Junctions, bekannte Build-/Abhängigkeitsordner, ungültiges UTF-8 und Binärinhalte erhalten Ausschlussgründe. Das ist eine Pfad-/Formatbegrenzung und keine allgemeine Secrets-Erkennung in beliebigen normalen Textdateien.

Archivierte Videos und Bilder werden als vorhandene Dateien erfasst, soweit Git sie kennt. Ihr visueller Inhalt wird nicht analysiert. Vorhandene Transkripte sind Text, behalten aber die Unsicherheit automatischer Spracherkennung. Bildbelege, OCR und Codeanalyse brauchen passende zusätzliche Extraktoren.

Externe Prompts und Agent-Dateien sind untersuchte Inhalte. Ihre Auffindbarkeit aktiviert sie nicht. Eigene Entscheidungen und die vorhandene Skill-Registry bestimmen die spätere Nutzung.

## Fehler und Prüfung

Repo-Fehler und nicht lesbare Dokumente werden in der JSON-Ausgabe sichtbar und ergeben Exitcode 1. Ein partieller Katalog kann zur Fehlersuche erhalten bleiben; seine Lücken stehen in `repository_errors` und `documents.error`. Ein fehlender Index fordert zuerst zur Indexierung auf. Bestehende Analysepläne werden nicht überschrieben.

Ein formal vollständiger Bearbeitungsnachweis lässt sich später mit folgendem Befehl prüfen:

```powershell
python ai.py wissen analyse-check --plan .wissen/analysen/baseline-01.json --ergebnisse .wissen/analysen/baseline-01-ergebnisse.jsonl
```

Das Ergebnisformat und die inhaltliche Abnahme stehen im [Gesamtanalyse-Ablauf](gesamtanalyse.md). Tests liegen unter `tests/test_wissen.py` und die CLI-Integration unter `tests/test_ai_cli.py`.
