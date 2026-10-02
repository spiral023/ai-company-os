# Adversarialer-Pre-Launch-Check

**Konfidenz:** meinung

## Zweck

Findet Sicherheits-, Daten-, Ablauf- und Umgebungsfehler vor dem Release, indem du gezielt versuchst, die eigene App zu brechen, bevor es Nutzer oder Angreifer tun. Besonders relevant für schnell mit Coding Agents gebaute Apps, bei denen solche Prüfungen sonst ausfallen.

## Funktionsweise

Mehrere read-only Prüfagenten bekommen je einen Themenbereich und einen festen Fragenkatalog, etwa:

- **Security:** Schlüssel im Frontend-Bundle oder in der Git-History, API-Aufrufe ohne Login oder mit fremder ID, manipulierte Preise und Rollen, Rate Limits, XSS über Markdown oder SVG.
- **Daten:** große Datenmengen, lange Namen mit Emoji, doppelte Konten durch Groß- und Kleinschreibung, leere Formulare.
- **Abläufe:** doppelte Bestellungen und Webhooks, Neuladen mitten im Formular, Speichern ohne Verbindung, große Uploads.
- **Umgebung:** kleine Displays mit Zoom, Safari, Zeitzonen.

Gearbeitet wird in einer abgesicherten Testumgebung: Testkonten, Payment-Testmodus, Test-Datenbank mit Aufräumen, gemockte KI-APIs oder Keys mit Ausgabenlimit, sofortiger Stopp bei Produktionsschlüsseln. Jeder Befund kommt mit Repro-Schritten, Screenshot und Fix-Vorschlag; Unprüfbares wird mit Grund als „untested“ markiert. Der Hauptagent bekommt eine nach Schwere sortierte Liste und behebt erst nach Freigabe. Riskante Bereiche wie Login und Zahlung laufen auf höherem Effort.

Der Katalog lässt sich mit Security-Checklisten erweitern: Row Level Security, CORS, sichere Cookies, CSRF, Session-Ablauf, Backups mit Restore-Test, von der KI erfundene Paketnamen, Prompt Injection, Grenzen für Tool- und SQL-Ausführung durch das Modell, harte Ausgabenlimits bei KI-Anbietern.

## Vorteile

- Macht die oft übersprungene Sicherheits- und Robustheitsprüfung zu einem wiederholbaren Schritt vor jedem Launch.
- Read-only Prüfer und ein einziger behebender Agent vermeiden Schreibkonflikte.
- Der Katalog ist austauschbar und wächst mit jedem gefundenen Fehlertyp.

## Nachteile & Grenzen

- Die Abdeckung reicht nur so weit wie der Katalog.
- Wirkung und Kosten sind nicht gemessen.
- Die Schutzregeln für die Testumgebung sind Anweisungen an den Agenten, keine technische Sperre.

## Wann einsetzen, wann nicht

- Einsetzen: vor dem ersten öffentlichen Release und vor größeren Änderungen an Login, Zahlung, Uploads oder Datenmodell.
- Nicht einsetzen: als Ersatz für ein Security-Review durch Fachleute bei sensiblen Daten oder regulierten Bereichen.

## Belege

- 2026-09-26 · [[2026-09-26-voxyz_ai-2103977414711767244]] · meinung — Frühere Fassung mit fünf Subagents und 20 Prüfpunkten (Design, Mobile, UI-Zustände, Nutzerverhalten, Launch-Basics); Fixes erst nach Freigabe.
- 2026-09-27 · [[2026-09-27-voxyz_ai-2104224555040452925]] · meinung — Vier Breaker-Subagents (Security, Daten, Abläufe, Umgebung) mit 16 Fragen, Effort `high` bzw. `xhigh` für Security und Sicherheitsrahmen für die Testumgebung; Praxistipp ohne Messung.
- 2026-09-29 · [[2026-09-29-suraj_sharma14-2104790775397830755]] · meinung — Security-Checkliste mit 30 Punkten, die dem Katalog fehlende Punkte liefert (RLS, CORS, CSRF, Backups, Prompt Injection, Ausgabenlimits); letzter Punkt empfiehlt, die KI die App angreifen zu lassen.

## Spannungen & offene Fragen

- Die beiden Vox-Fassungen prüfen unterschiedliche Bereiche (26.09.: Design, Mobile, UI-Zustände; 27.09.: Security, Daten, Abläufe, Umgebung). Offen ist, ob beide Kataloge zusammen gehören oder je nach App-Typ gewählt werden.
- Zwei der drei Belege stammen vom selben Autor; unabhängig ist bisher nur die Checkliste.

## Verwandte Patterns

- [[Kontrollierte-Agent-Parallelisierung]]
- [[Plan-first-mit-getrenntem-Review]]
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
