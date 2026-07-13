# Import von zwölf externen Repositories – Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Zwölf vom Nutzer benannte GitHub-Repositories als lokale Analysequellen unter `external_repos/<owner>/<repo>/` klonen und nachvollziehbar in `external_repos/INDEX.md` dokumentieren.

**Architecture:** Die Clones bleiben durch `.gitignore` lokal. Der Index erhält für jedes Repo einen manuellen Eintrag mit URL, Datum, rund 200 Wörtern README-basierter Einordnung und gegebenenfalls einer handgepflegten Strukturzeile; `update_external_repos.py --index-only` ergänzt alle mechanischen Metadaten.

**Tech Stack:** Git, PowerShell, Markdown, Python-Index-Script

---

### Task 1: Repositories sicher als Analysequellen klonen

**Files:**
- Create locally (ignoriert): `external_repos/<owner>/<repo>/` für alle zwölf Quellen
- Modify: `external_repos/INDEX.md`

- [x] **Step 1: Zielpfade und Ignorierung prüfen**

Run: `git check-ignore external_repos/headroomlabs-ai/headroom external_repos/rtk-ai/rtk external_repos/nexu-io/open-design`

Expected: Alle Beispielpfade werden als ignoriert ausgegeben.

- [x] **Step 2: Jeden angegebenen GitHub-Clone ohne Script-Ausführung erstellen**

Run für jede Quelle: `git clone https://github.com/<owner>/<repo>.git external_repos/<owner>/<repo>`

Expected: Zwölf Git-Repositories mit `.git`-Verzeichnis; keine Installations-, Build- oder Fremd-Scripts werden ausgeführt.

- [x] **Step 3: Vorhandene Lizenz-, README- und Script-Signale erfassen**

Run: Dateinamen, Lizenzdateien, Paketmanifeste, Setup-Dateien und `SKILL.md`-Vorkommen je Clone ausgeben.

Expected: Eine Grundlage für die Einschätzung „nur als Referenz“ und für die manuelle Strukturzeile.

### Task 2: README-basierte Analyse und Indexeinträge erstellen

**Files:**
- Modify: `external_repos/INDEX.md`

- [x] **Step 1: README-Dateien und relevante Metadaten vollständig lesen**

Run: `Get-Content -Raw` für jede primäre README sowie gezielt für Lizenz- und Sicherheitsdokumente, sofern vorhanden.

Expected: Pro Repo belegte Aussagen zu Zweck, Zielgruppe, Ablauf, wichtigen Komponenten und Integrationsrisiken.

- [x] **Step 2: Zwölf Indexeinträge nach vorhandener Konvention ergänzen**

Für jeden Eintrag ergänzen: `## <owner>/<repo>`, URL, Download- und Aktualisierungsdatum `2026-07-13`, eine präzise deutsche Zusammenfassung und bei nicht standardmäßiger Struktur eine mit `<!-- manual -->` markierte Strukturzeile.

- [x] **Step 3: Entwicklerübersicht aktualisieren**

Die Abschnitte „Was möchtest du tun?“, „Repos im direkten Vergleich“ und „Empfohlene Startpunkte“ gezielt um die neuen Repos erweitern, wenn sie neue klar abgegrenzte Aufgaben abdecken.

### Task 3: Mechanische Metadaten und Vollständigkeit verifizieren

**Files:**
- Modify: `external_repos/INDEX.md`

- [x] **Step 1: Index-Metadaten erzeugen**

Run: `python 70_Scripts/update_external_repos.py --index-only`

Expected: Übersicht, Dateizahlen und Größen für 34 Repositories; manuelle Strukturzeilen bleiben erhalten.

- [x] **Step 2: Einträge gegen Clone-Verzeichnisse prüfen**

Run: PowerShell-Vergleich der 12 `<owner>/<repo>`-Namen im Index mit den zwölf angelegten Clone-Verzeichnissen.

Expected: Keine fehlenden oder zusätzlichen Namen.

- [x] **Step 3: Formatprüfung ausführen**

Run: `git diff --check -- external_repos/INDEX.md`

Expected: Keine Ausgabe und Exit-Code 0.

- [x] **Step 4: Änderungen dokumentieren**

In der Abschlussmeldung die importierten Repos, die Indexdatei, ausgeführte Checks sowie den Hinweis nennen, dass keine fremden Scripts installiert oder ausgeführt wurden.
