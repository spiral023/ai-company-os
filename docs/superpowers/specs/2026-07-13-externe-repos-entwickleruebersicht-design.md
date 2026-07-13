# Design: Entwicklerübersicht für externe Repositories

**Stand:** 2026-07-13  
**Zieldatei:** `external_repos/INDEX.md`

## Ziel

Der bestehende Index erhält einen handgepflegten, aufgabenorientierten Einstieg für Entwickler und Vibe Coder. Leser sollen ohne Kenntnis der Repo-Namen erkennen, welches externe Repository ihnen bei einer konkreten Aufgabe hilft und welche Bestandteile sie dort untersuchen oder übernehmen können.

## Struktur

Die neue Übersicht steht vor der automatisch generierten Bestandsstatistik und besteht aus vier Teilen:

1. **Schnelleinstieg:** erklärt in wenigen Sätzen, wie die Übersicht zu verwenden ist.
2. **Was möchtest du tun?:** ordnet typische Entwicklungsaufgaben passenden Repositories und einem konkreten Nutzen zu.
3. **Repos im direkten Vergleich:** führt alle 22 Repositories mit Einsatzzweck, nutzbaren Bestandteilen, Charakter und lokalem Einstiegspfad auf.
4. **Empfohlene Startpunkte:** bietet kuratierte Kombinationen für Vibe Coding, disziplinierte Softwareentwicklung und den Ausbau eines eigenen Skill-/Agenten-Systems.

Ein Sicherheitshinweis macht deutlich, dass die Repositories Analysequellen sind und externe Skills vor produktiver Nutzung weiterhin auf Quelle, Lizenz, Inhalt und Trust-Level geprüft werden müssen.

## Abgrenzung

- Die automatisch generierten Inhalte zwischen den `OVERVIEW`-Markern werden nicht manuell verändert.
- Die bestehenden ausführlichen Repo-Beschreibungen bleiben unverändert die Detailansicht.
- Es werden keine externen Skills installiert oder ausgeführt.
- Es entsteht keine zweite Datei und keine redundante Kurzbeschreibung in jedem Detail-Eintrag.

## Qualitätskriterien

- Alle 22 aktuell indexierten Repositories erscheinen im Vergleich.
- Die Übersicht startet bei Aufgaben und Ergebnissen, nicht bei Repo-Namen.
- Tabellen bleiben auf üblichen Markdown- und Obsidian-Ansichten verständlich.
- Repo-Namen verlinken auf die vorhandenen Detailanker; lokale Pfade sind direkt nutzbar.
- Aussagen basieren auf den bereits geprüften Beschreibungen im Index.
- Das Update-Script kann weiterhin ausgeführt werden, ohne die handgepflegte Übersicht zu überschreiben.

## Prüfung

- Vollständigkeit gegen alle `## <owner>/<repo>`-Überschriften prüfen.
- Links und lokale Pfade stichprobenartig kontrollieren.
- `python 70_Scripts/update_external_repos.py --index-only` ausführen und sicherstellen, dass nur automatisch verwaltete Inhalte angepasst werden.
- Markdown-Struktur auf konsistente Überschriften und Tabellen prüfen.
