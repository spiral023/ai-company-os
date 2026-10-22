---
url: https://github.com/cursor/plugins/tree/main/pstack
autor: "Lauren Tan (@poteto)"
datum: 2026-10-22
datum_unsicher: true
erfasst: 2026-10-22
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-10-22-cursor-pstack-engineering-skills.md
thema: Arbeitsweisen
zeitkritisch: ja
---

# Engineering-Prinzipien über Playbooks und Verifikation ausführbar machen

`pstack` verbindet Lauren Tans Engineering-Prinzipien mit aufgabenspezifischen Playbooks und getrennten Agent-Rollen. Die archivierte README beschreibt Version `0.15.29`; Struktur und ausgewählte Dateien wurden im lokalen Teil-Checkout geprüft, Qualitäts- und Effizienzversprechen nicht gemessen. Die README nennt kein eigenes Publikationsdatum: Der 22.10.2026 ist der Erfassungsstand, der letzte Teilbaum-Commit stammt vom 20.10.2026.

## Routing vor beliebiger Skill-Auswahl

`poteto-mode` ordnet Aufgaben einem von 23 Playbooks zu und lädt passende Skills entlang der Arbeitsschritte. Investigation, Bugfix, Performance, Prototyping und Refactoring haben unterschiedliche Nachweise. Beispielsweise soll ein Bug reproduziert und an der Laufzeit geprüft werden; eine Verhaltensänderung ist kein erhaltender Refactor. Der Hauptchat führt den Ablauf, während spezialisierte Delegates begrenzte Aufgaben erhalten.

24 kurze Prinzipien ergänzen diese Abläufe. Sie behandeln unter anderem Datenmodelle, Typen, Idempotenz, kleine verifizierbare Einheiten, Kontextgrenzen und Ursachenanalyse. Entscheidend ist der konkrete Auslöser eines Prinzips, nicht dessen bloße Erwähnung. Kommentare, Regeln und Automatisierung sollen eine erkannte Fehlerklasse an einer passenden Stelle absichern.

## Verifikation und Modellrollen

Separate Skills erzeugen projektspezifische Verifikationswege oder überprüfen komplexe Eigenschaften. Reviews, konkurrierende Lösungsansätze und Vorher-/Nachher-Messungen sollen Behauptungen über Qualität begrenzen. Die Modellkonfiguration unterscheidet Codearbeit und Urteil; eine Rollenwahl ist dabei eine Einstellung, kein eigener Nachweis besserer Ergebnisse.

## Abhängigkeiten bewusst abgrenzen

Nicht alles steckt im Teilbaum: Einige Kontroll- und Bereinigungsskills kommen aus `cursor-team-kit`. Die dokumentierte Claude-Code-Installation verwendet einen generierten Adapter unter `harness/pstack/`, der außerhalb des lokalen Sparse Checkouts liegt. Benny enthält vorbereitete Cursor-Automationen. Shell- und TypeScript-Helfer können GitHub- und Worktree-Zustand berühren; sie wurden nicht ausgeführt. Die mitgelieferte Lizenzdatei nennt MIT für den pstack-Teil.

## Einordnung

Die Primärquelle konkretisiert eine Skill-Hierarchie, beweist aber weder sichere Autonomie noch einen Gewinn durch zusätzliche Agents oder Modelle. Ein statischer Dateibefund bestätigt Aufbau und Referenzen, keine Harness-Kompatibilität oder Laufzeitwirkung. Bestehende menschliche Freigaben gelten auch gegenüber Shipping-Playbooks. Vor einer Übernahme sind der einzelne Engpass, notwendige Abhängigkeiten und ein geeigneter Verifikationsweg zu bestimmen.

## Kernaussagen

- Aufgaben-Router, fachliche Skills und Delegates getrennt verantworten → [[Skill-Call-Hierarchie]].
- Eine Korrektur auf der Ebene verankern, die sie zuverlässig trägt → [[Erweiterungs-Ebenen-Zuordnung]].
- Die konkrete Wirkung am Artefakt nachweisen → [[Testharness-als-staerkster-Hebel]].

## Verbindungen

- [[Kontrollierte-Agent-Parallelisierung]]
- [[2026-10-16-poteto-2111133080526495985]]
- [[Plan-first-mit-getrenntem-Review]]
