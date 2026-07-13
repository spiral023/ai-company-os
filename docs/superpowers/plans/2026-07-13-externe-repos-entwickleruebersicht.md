# Entwicklerübersicht für externe Repositories – Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Die `external_repos/INDEX.md` um einen vollständigen, aufgabenorientierten Einstieg für Entwickler und Vibe Coder erweitern.

**Architecture:** Die handgepflegte Orientierung wird vor dem automatisch generierten `OVERVIEW`-Block eingefügt. Sie verlinkt auf die bestehenden Detailabschnitte und verändert weder die generierten Statistiken noch die ausführlichen Repo-Beschreibungen.

**Tech Stack:** Markdown, Obsidian-kompatible Anker, PowerShell, bestehendes Python-Index-Script

---

### Task 1: Aufgabenorientierte Entwicklerübersicht ergänzen

**Files:**
- Modify: `external_repos/INDEX.md`

- [x] **Step 1: Bestand vor der Änderung erfassen**

Run: `rg '^## ' external_repos/INDEX.md`

Expected: Eine automatisch generierte Übersicht und 22 Repo-Detailüberschriften werden ausgegeben.

- [x] **Step 2: Handgepflegte Orientierung einfügen**

Direkt vor `<!-- OVERVIEW:START` diese Abschnitte einfügen:

- `## Schnelleinstieg für Entwickler und Vibe Coder`
- `## Was möchtest du tun?`
- `## Repos im direkten Vergleich`
- `## Empfohlene Startpunkte`
- `## Sicher und sinnvoll übernehmen`

Die Aufgabentabelle muss typische Arbeiten von Ideenklärung bis Shipping, UI/UX, Codeverständnis, Skills, Agententeams, SEO und Marketing abdecken. Der direkte Vergleich muss alle 22 Repositories jeweils mit Einsatzzweck, konkret nutzbaren Bestandteilen, Charakter und lokalem Pfad enthalten.

- [x] **Step 3: Markdown-Struktur statisch prüfen**

Run: `rg '^## ' external_repos/INDEX.md`

Expected: Die fünf neuen handgepflegten Abschnitte stehen vor `## Übersicht`; alle 22 Repo-Detailüberschriften bleiben erhalten.

- [x] **Step 4: Vollständigkeit des Repo-Katalogs prüfen**

Run: PowerShell-Vergleich der Repo-Namen aus den Detailüberschriften mit den Repo-Links im Abschnitt `Repos im direkten Vergleich`.

Expected: Keine fehlenden oder zusätzlichen Repo-Namen.

### Task 2: Update-Sicherheit und Diff prüfen

**Files:**
- Verify: `external_repos/INDEX.md`

- [x] **Step 1: Index-Script ausführen**

Run: `python 70_Scripts/update_external_repos.py --index-only`

Expected: Erfolgreicher Scan aller lokalen Repositories; die handgepflegte Entwicklerübersicht bleibt erhalten.

- [x] **Step 2: Formatfehler prüfen**

Run: `git diff --check -- external_repos/INDEX.md`

Expected: Keine Ausgabe und Exit-Code 0.

- [x] **Step 3: Änderung gegen das Design prüfen**

Run: `git diff -- external_repos/INDEX.md`

Expected: Ausschließlich die neue handgepflegte Orientierung sowie gegebenenfalls legitime, vom Index-Script aktualisierte Werte im automatisch verwalteten Block.

- [x] **Step 4: Ergebnis dokumentieren**

In der Abschlussmeldung aufführen: geänderte Dateien, ausgeführte Checks, etwaige automatische Metadatenänderungen und verbleibende Risiken.
