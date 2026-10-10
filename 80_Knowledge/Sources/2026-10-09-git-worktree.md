---
url: https://git-scm.com/docs/git-worktree
autor: Git-Projekt
datum: 2026-10-09
erfasst: 2026-10-09
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-10-09-git-scm-git-worktree-getrennte-arbeitsverzeichnisse.md
zeitkritisch: nein
---

# Git Worktrees isolieren Arbeitsverzeichnisse innerhalb eines Repositories

Referenzdokumentation, gesichtet am 09.10.2026; Sichtungsdatum, keine Veröffentlichung. Die Seite bezeichnet Git 2.56.0 als aktuellen Dokumentationsstand. Der vollständige manuelle Text wurde lokal archiviert.

## Geteilte und getrennte Zustände

Ein Repository kann mehrere Arbeitsverzeichnisse mit unterschiedlichen ausgecheckten Branches besitzen. Worktrees teilen zentrale Repository-Daten und Referenzen, während HEAD, Index und Arbeitsdateien jeweils getrennt sind. `git worktree add` erzeugt einen weiteren Checkout, `list` zeigt vorhandene Worktrees, `remove` entfernt einen sauberen Checkout. Die Dokumentation beschreibt Einschränkungen bei bereits ausgecheckten Branches und veränderten Arbeitsverzeichnissen.

## Einordnung

Dokumentierte Git-Mechanik. Getrennte Dateien verhindern keine fachlichen Konflikte gemeinsamer Schnittstellen und isolieren keine externen Datenbanken oder belegten Ports. Die Anwendung auf Coding Agents braucht zusätzliche Zuständigkeiten und Integrationstests. Keine eigene Parallelitätsmessung.

## Kernaussagen

- Eigene Arbeitsverzeichnisse für parallele Änderungen, gemeinsame Zusammenführung → [[Kontrollierte-Agent-Parallelisierung]].

## Verbindungen

- [[2026-01-31-bcherny-claude-code-team-tips]]
