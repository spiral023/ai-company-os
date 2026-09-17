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

## Subagents und Token-Ökonomie

Delegation an parallele Subagents ist bei gleichartiger Arbeit über viele Dateien der richtige Hebel — aber sie multipliziert jeden Fehler im Auftrag mit der Anzahl der Subagents. Deshalb gelten für jeden Batch-Auftrag drei Regeln:

1. **Der Auftrag ist selbsttragend.** Alle Regeln stehen im Auftragstext, statt den Subagent auf Referenzdateien zu verweisen. Fünf Subagents, die je drei unveränderliche Regel-Dateien lesen, erzeugen fünfzehn identische Volltext-Reads pro Schritt.
2. **Repo-weite Prüfläufe laufen zentral, nicht pro Subagent.** Validatoren, Linter und Scans über den Gesamtbestand gehören einmal in die Konsolidierung durch den Hauptagenten. Pro Subagent nur, was die eigenen Dateien betrifft. Solche Läufe werden mit wachsendem Bestand teurer — pro Subagent ausgeführt wächst der Verbrauch quadratisch statt linear.
3. **Der Abschlussbericht ist die Konsolidierungs-Grundlage, nicht das Artefakt.** Der Subagent liefert fertig formulierte Ergebnisse, nicht nur Stichworte — dann muss der Hauptagent seine Ausgabe nicht noch einmal im Volltext lesen.

Für den Hauptagenten bei der Konsolidierung: **gezielt lesen statt vollständig.** Um eine Zeile an eine lange, wachsende Datei anzuhängen, per `Grep -n` den Anker suchen und mit `Read`-`offset` nur den relevanten Bereich laden. Vollständig lesen nur, wenn tatsächlich der ganze Inhalt beurteilt werden muss.

Nach jedem Batch-Schritt den Usage-Stand prüfen, bevor der nächste startet. Schrittgröße lieber klein halten (Richtwert: 5 Einheiten pro Schritt) — das macht den Verbrauch vorhersagbar und lässt nach jedem Schritt eine Kurskorrektur zu.

## Commit-Nachrichten

Nur committen, wenn explizit beauftragt (siehe `Autonom erlaubt` / `Freigabe durch Philipp erforderlich`). Ist ein Commit beauftragt, gilt für die Nachricht:

- **Titel:** kurzer Imperativ auf Deutsch, ohne Satzpunkt am Ende, möglichst unter 70 Zeichen (z. B. „Externe Repos aktualisieren und Wissens-Patterns ergänzen“).
- **Body:** immer ausführlich, nie nur eine Dateiliste. Eine Leerzeile nach dem Titel, danach in Fließtext erklären, WAS sich geändert hat und WARUM — so, dass der Commit ohne Rückfrage beim Autor verständlich ist.
- Bei mehreren unabhängigen Änderungsblöcken (z. B. Skript-Lauf + Knowledge-Patterns + neue Datei) jeden Block als eigenen Absatz mit kurzer Einleitung, nicht alles vermischt.
- Auffälligkeiten, Überraschungen oder Abweichungen vom Erwarteten explizit benennen (z. B. „Bemerkenswert: …“), nicht nur den Normalfall beschreiben.
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

- Teilt Philipp eine neue Quelle über Arbeitsweisen — X/Twitter, TikTok, YouTube, Artikel, PDF oder formlosen Text, auch ohne expliziten Auftrag — den Skill `knowledge-ingest` anwenden.
- Neue Quellen immer über den passenden lokalen Abrufweg archivieren: X mit `npm run ingest:x -- <url> --thread`, TikTok mit `npm run ingest:tiktok -- <url>`, YouTube/Artikel/PDF mit `python ai.py ingest <url-oder-pfad>`. Nicht ersatzweise per WebFetch eine unvollständige Quelle als vollständig behandeln.
- Rohquellen liegen automatisch nach Typ unter `00_Inbox/Quellen/{X,TikTok,YouTube,URL,PDF}/`; Medien jeweils im typgleichen Unterordner `medien/<slug>/`.
- TikTok- und YouTube-Untertitel sind automatisch erzeugt und können ähnlich klingende Wörter falsch wiedergeben; kritische Aussagen und Zitate gegen das Video prüfen.
- Bereits erfasste Quellen aus diesen Typordnern (`status: neu`) über den Skill `quellen-verarbeiten` einarbeiten. Bei Batch-Läufen gilt zusätzlich der Abschnitt „Subagents und Token-Ökonomie“; der Auftragstext dafür ist `30_Skills/local/quellen-verarbeiten/references/batch-auftrag.md`.
- Pflege-Lauf über den Skill `knowledge-review`, u.a. im Wochenreview.
- In `80_Knowledge/Patterns/` wird nie gelöscht, nur datiert ergänzt; Widersprüche werden als Spannungen festgehalten.
- Patterns wachsen dadurch append-only. Wer Belege ergänzt, liest deshalb gezielt (Anker `## Spannungen`) statt die ganze Datei.

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

### Fremde GitHub-Repos herunterladen und aktualisieren (Analyse-Repos)

Fremde GitHub-Repos, die nur zur Analyse oder als Inspiration für Arbeitsweisen dienen, werden nach `external_repos/<owner>/<repo-name>/` geklont (einfacher `git clone`, kein Submodule/Subtree). Der Ordnername enthält immer den GitHub-Owner als Unterordner (z.B. `external_repos/mattpocock/skills/`), damit gleichnamige Repos verschiedener Owner nicht kollidieren. Der Ordner `external_repos/` ist in `.gitignore` und in der Obsidian-Konfiguration (`.obsidian/app.json` → `userIgnoreFilters`) ausgeschlossen: die Inhalte werden weder versioniert noch im Obsidian-Vault indiziert oder angezeigt. `external_repos/INDEX.md` selbst ist von dieser `.gitignore`-Ausnahme ausgenommen (`!external_repos/INDEX.md`) und bleibt versioniert.

Den kompletten Ablauf — neues Repo laden und in `external_repos/INDEX.md` dokumentieren, bestehende Repos pullen, INDEX.md-Zusammenfassungen bei inhaltlich relevanten Änderungen nachziehen, jeden Update-Lauf in `external_repos/changelog/<Datum>.md` festhalten — deckt der Skill **`external-repos`** (`30_Skills/local/external-repos/SKILL.md`) ab. Trigger-Phrasen wie „lade das Repo <URL>“, „update die externen Repos“ oder „aktualisiere external_repos“ lösen diesen Skill aus.

Mechanische INDEX.md-Felder (`Dateien`, `Größe`, `Struktur`, `Stars`, Übersichtstabelle) pflegt `python 70_Scripts/update_external_repos.py` automatisch (Ausnahme: `- **Struktur:**`-Zeilen mit `<!-- manual -->`-Marker, für Repos wo die mechanische Erkennung in die Irre führen würde). Die ~200-Wort-Inhaltszusammenfassung pro Repo bleibt bewusst Handarbeit — das braucht Urteilsvermögen.

Ziel: Anhand dieses Index später effizient (ohne erneutes Klonen) passende GitHub-Repos empfehlen, direkt zu den relevanten Skill-/Agent-Ordnern springen und Informationen/Arbeitsweisen daraus extrahieren können.

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
