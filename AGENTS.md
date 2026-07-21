# AGENTS.md

## Zweck

Dieses Repository ist Philipps AI-Company-OS. Es dient als Mutter-Repo für Firmenwissen, Workflows, Skills, Projekt-Kits und wiederverwendbare Arbeitsweisen für KI-gestützte Softwareentwicklung und digitale Produkte.

Einzelne Softwareprojekte liegen in eigenen Repositories. Dieses Repo liefert dafür Vorlagen, Skills und Entscheidungswissen.

## Grundprinzipien

- Arbeite schlank, konkret und nachvollziehbar.
- Nutze nur die Informationen, die für die aktuelle Aufgabe relevant sind.
- Stelle konkrete Rückfragen, wenn wichtige Informationen fehlen.
- Erstelle keine unnötig komplexen Frameworks.
- Pflege Wissen in Markdown-Dateien, die auch in Obsidian gut funktionieren.
- Schreibe auf Deutsch mit korrekten Umlauten.
- Verwende englische Fachbegriffe dort, wo sie in Entwicklung, AI, SaaS oder Marketing üblich sind.

## Führende Dateien

- `AGENTS.md` ist die führende Datei für Agenten.
- `CLAUDE.md` verweist nur auf `AGENTS.md`.
- Projekt-Repos können eigene `AGENTS.md` Dateien erhalten.
- Bereichsspezifische Regeln gehören in Skills oder Workflows, nicht in diese Root-Datei.

## Arbeitsweise

1. Aufgabe verstehen.
2. Relevante Memory-, Workflow- oder Skill-Dateien prüfen.
3. Falls wichtige Informationen fehlen, den Skill `ask-user-question` verwenden.
4. Einen kurzen Plan erstellen.
5. Änderungen in kleinen, nachvollziehbaren Schritten durchführen.
6. Relevante Checks, Tests oder Reviews ausführen.
7. Ergebnis zusammenfassen:
   - Was wurde erstellt oder geändert?
   - Welche Dateien wurden geändert?
   - Welche Checks wurden ausgeführt?
   - Welche offenen Fragen oder Risiken bleiben?

## Commit-Nachrichten

Nur committen, wenn explizit beauftragt (siehe `Autonom erlaubt` / `Freigabe durch Philipp erforderlich`). Ist ein Commit beauftragt, gilt für die Nachricht:

- **Titel:** kurzer Imperativ auf Deutsch, ohne Satzpunkt am Ende, möglichst unter 70 Zeichen (z. B. „Externe Repos aktualisieren und Wissens-Patterns ergänzen").
- **Body:** immer ausführlich, nie nur eine Dateiliste. Eine Leerzeile nach dem Titel, danach in Fließtext erklären, WAS sich geändert hat und WARUM — so, dass der Commit ohne Rückfrage beim Autor verständlich ist.
- Bei mehreren unabhängigen Änderungsblöcken (z. B. Skript-Lauf + Knowledge-Patterns + neue Datei) jeden Block als eigenen Absatz mit kurzer Einleitung, nicht alles vermischt.
- Auffälligkeiten, Überraschungen oder Abweichungen vom Erwarteten explizit benennen (z. B. „Bemerkenswert: …"), nicht nur den Normalfall beschreiben.
- Bei automatisiert gepflegten Feldern (z. B. `external_repos/INDEX.md` per `update_external_repos.py`) kurz erwähnen, was automatisch vs. von Hand geprüft/geschrieben wurde.
- Sprache durchgängig Deutsch, außer Code-Identifier, Dateipfade und Eigennamen.
- Am Ende `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>` ergänzen, wenn Claude die Änderung erstellt hat.
- Commit-Message immer per Heredoc übergeben, nie mit `--amend` ohne ausdrücklichen Auftrag.

## Freigabe durch Philipp erforderlich

Immer nach Freigabe fragen vor:

- Produktion-Deployments
- echten Kunden-E-Mails oder öffentlichen Veröffentlichungen
- Preisänderungen
- rechtlichen, steuerlichen oder datenschutzrelevanten Aussagen
- Änderungen an Authentifizierung, Billing, Security oder Tenant-Isolation
- Löschen von Daten
- neuen kostenpflichtigen Tools, APIs oder Diensten
- Aussagen über Zertifizierungen, Kunden, Compliance oder garantierte AI-Ergebnisse

## Autonom erlaubt

Ohne vorherige Freigabe erlaubt:

- Entwürfe erstellen
- lokale Dateien anlegen oder bearbeiten
- Projektideen strukturieren
- PRDs, Prompts, Checklisten und Testfälle erstellen
- Beispielcode und Prototypen vorbereiten
- lokale Reviews durchführen
- Verbesserungsvorschläge machen

## Skill-Nutzung

Skills liegen unter `30_Skills/`.

- Eigene Skills liegen unter `30_Skills/local/`.
- Externe Skill-Packs liegen unter `30_Skills/external/`.
- Die zentrale Übersicht ist `30_Skills/registry.yaml`.
- Nicht alle Skills sind automatisch aktiv.
- Externe Skills müssen geprüft werden, bevor sie in Projekt-Kits übernommen werden.

## Knowledge-System

Wissen über KI-Arbeitsweisen (Skills, Agent-Workflows, Frameworks) lebt unter `80_Knowledge/`. Regeln und Templates: `80_Knowledge/README.md`.

- Teilt Philipp einen Tweet, x.com-Link oder Text über Arbeitsweisen — auch formlos ohne Auftrag — den Skill `knowledge-ingest` anwenden.
- Pflege-Lauf über den Skill `knowledge-review`, u.a. im Wochenreview.
- In `80_Knowledge/Patterns/` wird nie gelöscht, nur datiert ergänzt; Widersprüche werden als Spannungen festgehalten.

## Scripts

Wiederkehrende Aufgaben sollen bevorzugt über Scripts unter `70_Scripts/` gelöst werden, wenn sie mehr als zweimal vorkommen.

Vor Änderungen an Scripts:
- bestehende Nutzung prüfen
- einfache CLI beibehalten
- keine unnötigen Abhängigkeiten hinzufügen
- Syntax-Check ausführen

## Benutzerfreundliche Bedienung

Für normale Bedienung bevorzugt `python ai.py` im Repo-Root nutzen. Die Scripts unter `70_Scripts/` bleiben die darunterliegenden Werkzeuge für Automatisierung, Debugging und direkte Agent-Nutzung.

## Externe Skills

Externe Skills dürfen nicht automatisch als vertrauenswürdig gelten.

Vor Nutzung in Projekten:
1. Quelle prüfen
2. Lizenz prüfen
3. Inhalt sichten
4. Trust-Level in `30_Skills/registry.yaml` setzen
5. Philipp-Freigabe einholen, wenn der Skill produktiv genutzt werden soll

## Repo-Import

Externe Repositories, Templates und Skill-Packs müssen vor Integration mit dem Skill `repo-import-review` geprüft werden. Externe Scripts dürfen nicht automatisch ausgeführt werden.

### Fremde GitHub-Repos herunterladen (Analyse-Repos)

Fremde GitHub-Repos, die nur zur Analyse oder als Inspiration für Arbeitsweisen dienen, werden nach `external_repos/<owner>/<repo-name>/` geklont (einfacher `git clone`, kein Submodule/Subtree). Der Ordnername enthält immer den GitHub-Owner als Unterordner (z.B. `external_repos/mattpocock/skills/`), damit gleichnamige Repos verschiedener Owner nicht kollidieren. Der Ordner `external_repos/` ist in `.gitignore` und in der Obsidian-Konfiguration (`.obsidian/app.json` → `userIgnoreFilters`) ausgeschlossen: die Inhalte werden weder versioniert noch im Obsidian-Vault indiziert oder angezeigt.

Update eines bereits geklonten Repos: `git -C external_repos/<owner>/<repo-name> pull`.

`external_repos/INDEX.md` selbst ist von der `.gitignore`-Ausnahme für `external_repos/` ausgenommen (`!external_repos/INDEX.md`) und bleibt somit versioniert — nur die geklonten Repo-Inhalte selbst sind lokal/ignoriert.

Beim Herunterladen eines neuen Repos immer einen Eintrag in `external_repos/INDEX.md` pflegen. Aufteilung: **die mechanischen Felder erledigt das Script automatisch, die inhaltlichen Felder schreibst du.**

Von Hand pro Repo anzulegen sind nur:

- Überschrift `## <owner>/<repo>` sowie die Zeilen `- **URL:**`, `- **Heruntergeladen:**`, `- **Zuletzt aktualisiert:**` (initial gleich dem Download-Datum).
- Eine Zusammenfassung von ca. 200 Wörtern auf Basis der README.md: Was macht das Projekt, welches Problem löst es, welche Technologie/welcher Ansatz, für wen relevant.

Automatisch durch `python 70_Scripts/update_external_repos.py` gepflegt (nicht von Hand berechnen):

- `- **Dateien:** … · **Größe:** …` — Dateizahl (ohne `.git`) und Größe.
- `- **Struktur:** …` — erkannte Skill-/Agent-/Command-/Hook-/Rules-/Plugin-Ordner, `SKILL.md`-Anzahl (ohne `docs/`- und `.`-Spiegelbäume) und generierte Spiegelordner.
- `- **Stars:** ⭐ …` — aktueller GitHub-Sterne-Stand, abgerufen per `gh api` (Fallback: anonyme REST-API). Bei fehlgeschlagenem Abruf bleibt der zuletzt bekannte Wert unverändert stehen statt überschrieben zu werden.
- Die Übersichtstabelle am Kopf (zwischen den `OVERVIEW`-Markern): Repos gesamt, Gesamtgröße, Dateien gesamt, Sterne gesamt, Stand-Datum, Tabelle je Repo (inkl. Sterne-Spalte).

Damit ein neues Repo alle Felder bekommt: nach dem Anlegen von Überschrift + URL + Datum + Zusammenfassung einmal `python 70_Scripts/update_external_repos.py --index-only` laufen lassen — das ergänzt/aktualisiert `Dateien`, `Größe`, `Struktur`, `Stars` und die Übersicht.

**Struktur-Nuance (`<!-- manual -->`):** Bei Repos, wo die eigentliche Logik NICHT in Standard-Ordnern liegt (Quellcode in `packages/`/`src/`, reine CLI, Wissensbasis ohne Skill-Paket, viele generierte Spiegel), würde die mechanische Erkennung in die Irre führen. Dort die `- **Struktur:**`-Zeile von Hand schreiben und mit ` <!-- manual -->` am Zeilenende markieren — das Script überschreibt solche Zeilen nie.

Ziel: Anhand dieses Index später effizient (ohne erneutes Klonen) passende GitHub-Repos empfehlen, direkt zu den relevanten Skill-/Agent-Ordnern springen und Informationen/Arbeitsweisen daraus extrahieren können.

### Externe Repos aktualisieren

Trigger-Phrasen wie „update die externen Repos“ oder „aktualisiere external_repos“ lösen folgenden Ablauf aus:

1. `python 70_Scripts/update_external_repos.py` ausführen (optional mit `--repo <owner>/<repo>` für nur ein Repo beim Pull). Das Script:
   - führt in jedem geklonten Repo `git pull --ff-only` aus und meldet pro Repo, ob es unverändert war oder neue Commits erhalten hat;
   - scannt danach **alle** Repos neu und aktualisiert in `external_repos/INDEX.md` automatisch `Dateien`, `Größe`, `Struktur` (außer `<!-- manual -->`-Zeilen), `Stars` und die Übersichtstabelle;
   - setzt `Zuletzt aktualisiert` nur bei Repos mit neuen Commits auf das heutige Datum.
   - Flags: `--index-only` (nur Neu-Scan ohne Pull), `--no-index` (nur Pull), `--no-stars` (Sterne-Abruf überspringen), `--dry-run` (Index-Änderungen nur anzeigen).
2. Nur für die vom Script als „NEU" gemeldeten Repos die inhaltliche Zusammenfassung prüfen:
   - README.md erneut lesen; falls vorhanden `CHANGELOG.md` bzw. Release-Notes sichten (viele READMEs enthalten die Highlights bereits inline).
   - Die ~200-Wort-Zusammenfassung in `external_repos/INDEX.md` nur bei inhaltlich relevanten Änderungen neu schreiben (dieser Teil ist bewusst NICHT automatisiert — er braucht Urteilsvermögen).
3. Unveränderte Repos brauchen keine manuelle Nacharbeit — ihre Metadaten hat das Script bereits aufgefrischt.
4. Am Ende kurz zusammenfassen, welche Repos sich geändert haben und was daran neu ist.

## Projektarten in Phase 1

Dieses Repo unterstützt zuerst diese Projektarten:

- SaaS Webapp
- Shopify App
- Website-Redesign

## Obsidian-Kompatibilität

Nutze:

- Markdown-Dateien
- klare Ordnernamen
- kurze Index-Dateien
- Wiki-Links wie `[[Mission]]`, `[[Idee_zu_Produkt]]`
- keine proprietären Obsidian-Plugins als Voraussetzung

## Stil

- Direkt und praktisch schreiben.
- Keine unnötigen Floskeln.
- Keine langen theoretischen Erklärungen, wenn eine Checkliste reicht.
- Bei Entscheidungen Optionen mit Empfehlung liefern.
