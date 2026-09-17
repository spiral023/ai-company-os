---
name: external-repos
description: Verwende diesen Skill, um die lokale Referenzbibliothek fremder GitHub-Repos unter external_repos/ zu pflegen — neues Repo laden und in external_repos/INDEX.md dokumentieren, oder alle geklonten Repos aktualisieren (git pull, INDEX.md-Metadaten, Changelog unter external_repos/changelog/). Trigger-Phrasen: "lade das Repo <URL> herunter", "downloade <owner/repo> als Referenz", "update die externen Repos", "aktualisiere external_repos".
---

# External Repos

## Ziel

Pflegt `external_repos/` — eine lokale, nicht versionierte Referenzbibliothek geklonter GitHub-Repos für AI-gestützte Produkt- und Softwareentwicklung (siehe `external_repos/INDEX.md`). Zwei Abläufe: ein neues Repo laden, oder alle bestehenden Repos aktualisieren. Siehe auch `AGENTS.md` → „Fremde GitHub-Repos herunterladen und aktualisieren“ und `AGENTS.md` → „Repo-Import“.

Diese Repos sind **Analyse- und Inspirationsquellen**, keine automatisch freigegebenen Abhängigkeiten. Vor produktiver Übernahme (nicht nur Referenz-Lektüre) gilt der Skill `repo-import-review` und Philipps Freigabe.

## Ablauf A: Neues Repo laden

1. **Klonen:** `git clone <url> external_repos/<owner>/<repo-name>` (Owner als Unterordner gegen Namenskollisionen, kein Submodule/Subtree).
2. **Lesen:** README.md vollständig, dazu bei Bedarf LICENSE, package.json/pyproject.toml, und falls vorhanden das zentrale `SKILL.md`/`AGENTS.md` des Repos für Kontext.
3. **Sterne abrufen (optional, für den Eintrag):** `gh api repos/<owner>/<repo> --jq ".stargazers_count"` (Fallback: anonyme REST-API `https://api.github.com/repos/<owner>/<repo>`).
4. **INDEX.md-Eintrag von Hand anlegen**, alphabetisch nach Owner einsortiert (case-insensitiv, an den Nachbareinträgen orientieren):
   ```
   ## <owner>/<repo>

   - **URL:** https://github.com/<owner>/<repo>
   - **Stars:** ⭐ <Zahl>
   - **Heruntergeladen:** <heutiges Datum, YYYY-MM-DD>
   - **Zuletzt aktualisiert:** <= Download-Datum>

   <eigene Zusammenfassung, ca. 200 Wörter>
   ```
   Die Zusammenfassung beschreibt in eigenen Worten: was das Projekt macht, welches Problem es löst, Technologie/Ansatz, für wen es relevant ist, und was am Repo (Lizenz, Ökosystem-Reichweite, Eval-Infrastruktur, Risiken) bemerkenswert ist. Nicht aus SKILL.md/README abschreiben — eigenständig zusammenfassen.
5. **Mechanische Felder ergänzen:** `python 70_Scripts/update_external_repos.py --index-only` ausführen. Das trägt `Dateien`, `Größe`, `Struktur` und die Übersichtstabelle automatisch nach (Stars nur falls noch nicht gesetzt oder Abruf gewünscht — mit `--no-stars` weglassen, wenn du den Wert schon manuell eingetragen hast).
6. **Struktur-Nuance:** Führt eine `packages/`/`src/`-Quellcode-Struktur, eine reine CLI oder eine Wissensbasis ohne Skill-Paket die mechanische Erkennung in die Irre, die `- **Struktur:**`-Zeile von Hand schreiben und mit ` <!-- manual -->` am Zeilenende markieren — das Script überschreibt solche Zeilen nie.
7. **Kein eigener Changelog-Eintrag nötig** — ein Neuzugang ist kein „Update-Lauf“. Fällt das Laden zeitlich mit einem Update-Lauf zusammen, im Changelog dieses Laufs (`external_repos/changelog/<Datum>.md`) nur kurz als Randnotiz erwähnen (siehe Ablauf B, Kopfzeile).
8. Vor jeder produktiven Übernahme (Code kopieren, Skill installieren, Script ausführen) zusätzlich `repo-import-review` durchlaufen.

## Ablauf B: Repos aktualisieren

1. **Script ausführen:** `python 70_Scripts/update_external_repos.py` (optional `--repo <owner>/<repo>` für nur ein Repo). Das Script pullt jedes geklonte Repo (`git pull --ff-only`), meldet pro Repo NEU/unverändert/Fehler mit altem und neuem Commit-Hash, und scannt danach alle Repos neu für `Dateien`/`Größe`/`Struktur`/`Stars`/Übersichtstabelle in `external_repos/INDEX.md`. Flags: `--index-only` (nur Neu-Scan ohne Pull), `--no-index` (nur Pull), `--no-stars`, `--dry-run`.
   - **Windows-Longpath-Falle:** Ein Repo mit tief verschachtelten Testpfaden (z. B. `openai/codex`) kann mit `Filename too long` scheitern, weil Windows Pfade über 260 Zeichen ablehnt. Der Pull bricht dann mitten im Checkout ab — HEAD bleibt alt, der Working-Tree ist aber teilweise neu. Fix: im betroffenen Repo `git checkout -- .` + `git clean -fd` (verwirft nur den unvollständigen Zwischenstand fremden Codes, unbedenklich für eine reine Analysekopie — bei eigenen Änderungen im Zweifel vorher fragen), dann `git config core.longpaths true`, dann `git pull --ff-only` erneut.
   - **Separat gepflegte Repos außerhalb `external_repos/`** (aktuell `external_knowledge/ai-llm-wiki/`) hat das Script nicht im Blick — dort zusätzlich manuell `git -C external_knowledge/ai-llm-wiki pull` ausführen und im selben Changelog-Lauf dokumentieren.
2. **Inhaltliche Zusammenfassungen prüfen** — nur für die vom Script als „NEU“ gemeldeten Repos:
   - README.md erneut lesen; falls vorhanden CHANGELOG.md/Release-Notes sichten.
   - Die ~200-Wort-Zusammenfassung in `external_repos/INDEX.md` nur bei inhaltlich relevanten Änderungen umschreiben (neue Skills/Features, geänderter Scope, veraltete Zahlen, Sicherheits- oder Breaking Changes). Reine Maintenance/CI/Dependency-Bumps/Sterne-Refreshs rechtfertigen keine Änderung. Neue Fakten einweben, nicht nur anhängen.
   - **Bei vielen geänderten Repos (Richtwert: mehr als ~10):** die Analyse auf mehrere parallele Subagenten aufteilen (Agent-Tool, general-purpose, Batches von 6–10 Repos). Jeder Agent bekommt: die Liste seiner Repos im Format `owner/repo: alter_hash -> neuer_hash` (aus der Script-Ausgabe), die Anweisung pro Repo Commit-Anzahl zu ermitteln (`git -C external_repos/<owner>/<repo> rev-list --count <alt>..<neu>`), CHANGELOG.md-Diff/README-Diff/Commit-Log zu lesen, 1–3 konkrete Stichpunkte zu formulieren, den betroffenen INDEX.md-Absatz bei Bedarf selbst per Edit zu korrigieren (NUR den Fließtext, nie die Script-gepflegten Feldzeilen Dateien/Größe/Struktur/Stars/Zuletzt aktualisiert), und am Ende NUR die fertigen Changelog-Textblöcke im Format aus Schritt 3 zurückzugeben — keine Meta-Kommentare.
3. **Changelog-Datei schreiben:** `external_repos/changelog/<Datum>.md` (Format `YYYY-MM-DD.md`; bei mehreren Läufen am selben Tag Uhrzeit anhängen, z. B. `2026-09-17-1430.md`). Alte Lauf-Dateien nie umschreiben oder löschen — jeder Lauf ist eine eigene, abgeschlossene Datei.
   - Kopf: `# Update-Lauf <Datum>`, Link `[← Übersicht](README.md)`, dann Laufstatistik (geprüft/geändert/unverändert/Fehler), Hinweis auf separate Läufe (z. B. `ai-llm-wiki`), Hinweis auf Neuzugänge (Ablauf A) und Besonderheiten (z. B. Longpath-Fix).
   - **Rauschfilter — Abschnitt „Nur Wartung, ohne inhaltliche Substanz“:** Repos, deren EINZIGE Änderungen automatisierte Bot-Commits (Star-History-/Badge-Refresh), reine Sponsoren-/Dependabot-Änderungen oder ein einzelner kosmetischer Ein-Zeiler ohne Funktionsbezug sind, bekommen KEINEN eigenen Unterabschnitt. Sie erscheinen gesammelt als Liste direkt unter der Kopfzeile: `` `owner/repo` (`alt → neu`, N Commits) — Ein-Satz-Grund. `` Jeder reale Bugfix, jede Sicherheits- oder Feature-/Skill-Änderung bekommt dagegen einen vollen Unterabschnitt, auch bei nur einem Commit — die Filterung richtet sich nach inhaltlicher Substanz, nicht nach Commit-Zahl.
   - Für jedes verbleibende Repo ein Unterabschnitt:
     ```
     ### owner/repo

     - **Commits:** `alt → neu` (N Commits)
     - **Änderungen:** 1–3 konkrete Sätze, mit echten Feature-/Fix-Namen, Versionsnummern, betroffenen Komponenten — keine generischen Phrasen wie „diverse Verbesserungen“.
     - **Index:** Angepasst/Unverändert — kurze Begründung.
     ```
   - `external_repos/changelog/README.md` (Läufe-Übersichtstabelle) um die neue Zeile ergänzen.
4. Unveränderte Repos brauchen keine Nacharbeit und keine Erwähnung außerhalb der Laufstatistik.
5. Am Ende kurz zusammenfassen, was sich geändert hat, und auf die neue Changelog-Datei verweisen.
