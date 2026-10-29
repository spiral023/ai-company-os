# Review-Findings in Agent-Verbesserungen überführen

**Konfidenz:** verifiziert

## Zweck

Wiederholte menschliche Korrekturen als konkrete Hinweise auf fehlende Checks, Standards, Navigation oder Informationen verwenden.

## Funktionsweise

Nach einem Review nicht allein den letzten Diff betrachten: ursprüngliche Aufgabe, Agent-Sessions, Reviewkommentare und anschließende Korrekturen zusammenführen. Für jeden Fehler unterscheiden, ob der Agent die Information nicht fand, eine mechanisch prüfbare Regel verletzte oder eine echte Ermessensentscheidung falsch traf. Vorschläge nach Wirkung und Beleg priorisieren; ein Mensch beurteilt, was tatsächlich in die Arbeitsumgebung übernommen wird.

Die dauerhafte Verbesserung an der passenden Stelle verankern. Mechanische Verstöße gehören bevorzugt in vorhandene deterministische Checks. Ermessensregeln können in gezielt gelesene Coding Standards, fehlendes Fachwissen in referenzierte Dokumentation und Navigationsprobleme in knappe Wegweiser. Große globale Agent-Dateien sind kein universeller Sammelplatz. Nach einem Korrekturcommit erneut prüfen, ob die Korrektur selbst den vereinbarten Reviewpfad durchlaufen hat.

## Vorteile

- Verbindet konkrete Fehlbeobachtungen mit einer begründeten Änderung der Arbeitsumgebung.
- Kann menschliches Review von wiederkehrenden mechanischen Beanstandungen entlasten.
- Trennt Produktkorrektur und Verbesserung des künftigen Agentenablaufs.

## Nachteile & Grenzen

- Sessionlogs und Kommentare sind unvollständig; fehlender Kontext kann falsche Ursachen nahelegen.
- Ein einzelner Reviewwunsch ist nicht automatisch eine allgemeine Teamregel.
- Neue Regeln brauchen eine Gegenprobe, sonst wachsen Kontext und Fehlalarme weiter.

## Wann einsetzen, wann nicht

- Einsetzen: wiederholte Reviewfehler, aufwendige Navigation, fehlende Ausführungsbelege oder unreviewte Korrekturcommits.
- Nicht einsetzen: als automatische Übernahme sämtlicher Reviewerpräferenzen oder als Ersatz für Produktabnahme.

## Belege

- 2026-10-29 · [[2026-10-29-matt-pocock-software-factories-real-engineers]] · meinung — Die Retro-Kapitel zeigen die Auswertung von PR-Sessions und Kommentaren, eine nicht geprüfte Korrektur sowie die bewusste Auswahl von Verbesserungen. Datum ist der Erfassungstag; die Demonstration liefert keine gemessene Fehlerreduktionsquote.
- 2026-10-29 · external_repos/mattpocock/skills/skills/engineering/retro/SKILL.md · verifiziert — Die Kategorien Navigation, Automated checks, Coding standards, Global AGENTS.md, Tool economy, No-ops und Information access im Checkout 59db609eb1e18aaf59b63284d0e52255aff0c63c statisch geprüft. Der aktuelle Skill bevorzugt für mechanische Verstöße explizit deterministische Checks.

## Spannungen & offene Fragen

- 2026-10-29: Die Kursdemo ergänzt teilweise textuelle Coding Standards. Der geprüfte Referenzstand verlangt für mechanische Verstöße einen deterministischen Check. Bei der Übertragung daher erst die Fehlerklasse beurteilen und vorhandene Checks prüfen.
- 2026-10-29: Automatische Pflege kann dieselbe falsche Präferenz verbreiten. Kandidaten werden hier als Wissensgrundlage festgehalten; produktive Regeln und Skills werden dadurch nicht geändert.

## Verwandte Patterns

- [[Wissenspflege-mit-Inbox-und-Review]]
- [[Helper-Nutzung-durch-Lint-erzwingen]]
- [[Pruefungen-nach-Feedbackzeitpunkt-staffeln]]
- [[Plan-first-mit-getrenntem-Review]]
