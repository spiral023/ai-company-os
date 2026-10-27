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
- 2026-10-04 · [[2026-10-04-emilkowalski-2106752670405099523]] · meinung — `/break-ui` benennt lange Namen, ungewöhnliche E-Mail-Adressen und lange Listen als Belastungsfälle; der zentrale Repo-Check bestätigt realistische Extremdaten, Daten-Fixture, Worst-case-Toggle und eine Befundliste mit Fix je Defekt. Das konkretisiert adversariale UI-Prüfungen als dokumentierten Mechanismus, belegt aber keinen durchgeführten Volltest oder eine Reparaturwirkung.
- 2026-08-09 · [[2026-08-09-julian-ivanov-ki-automat-5-claude-code-skills-die-dir-wirklich-arbeit-abn]] · meinung — Die Skill-Übersicht beschreibt eine Kartierung von Eingabeflächen, spezialisierte Fehlersuche und Widerlegungsversuche durch andere Agenten als die Finder. Der Ablauf kann Befunde nachvollziehbarer machen, beweist aber weder vollständige Sicherheitsabdeckung noch einen wirtschaftlichen Vorteil der zusätzlichen Parallelisierung.
- 2026-10-16 · [[2026-10-16-voxyz_ai-2111079716832886886]] · meinung — Drei Testkonten und getrennte Prüfgruppen machen Kontengrenzen, direkte API-Aufrufe und nicht nachgewiesene Fälle explizit; der Post beschreibt einen Auftrag, keine hier ausgeführten Angriffe.
- 2026-10-17 · [[2026-10-17-voxyz_ai-2111442102756463077]] · meinung — Die Checkliste verbindet Idempotenz, Zahlungszustände, Zugriffsende und isolierte Restore-Tests mit getrennten Code- und Dashboardbelegen; Anbieter- und Rechtsaussagen sind ungeprüfter Prüfbedarf.
- 2026-10-19 · [[2026-10-19-voxyz_ai-2112302775547679169]] · meinung — Vox präzisiert den Prüfumfang bis zum ersten Produkterfolg durch vier Personas, sequenzielle Browsernutzung, Screenshotbelege, deduplizierte Befunde und einen erneuten Durchlauf mit vier frischen Agents ohne Befundliste. Die Zahl betroffener Personas ist keine empirische Nutzerhäufigkeit und ersetzt keine reale Testgruppe.
- 2026-10-22 · [[2026-10-22-franzbruckhoff-2113401002355298410]] · meinung — Der Prompt fordert reproduzierte Befunde mit Schweregrad, Dateizeile, Ursache, Angriffsweg und Patchvorschlag; der Thread warnt zugleich vor False Positives durch erzwungenes Weitersuchen und empfiehlt repospezifische Prüfdurchgänge.
- 2026-10-23 · [[2026-10-23-openai-securing-our-frontier-model-training-environment]] · meinung — Konkrete Grenzverletzungsziele, Versuche unter angenommenem Kontrollversagen und wiederholte Infrastrukturtests ergänzen den einmaligen Pre-Launch-Check; hoher Compute-Einsatz und menschliche Fundreproduktion begrenzen die direkte Übertragbarkeit.
- 2026-10-21 · [[2026-10-21-promptgefluester-jeder-der-ne-website-mit-p]] · meinung — Die sekundäre Warnung verbindet Patchmanagement mit öffentlich erreichbaren Vibe-Coding-Servern. Ohne CVE, Advisory und verlässliche Versionsangaben bleibt der Fall ungeprüft; er belegt vor allem die Notwendigkeit eines nachvollziehbaren Betroffenheitschecks, keine konkrete Patch-Anweisung.
- 2026-10-22 · [[2026-10-22-promptgefluester-im-kanal-leo-tech-coding-und-it-beschreibt-sie-ganz-gut-ist-ne]] · meinung — Ein dokumentiertes Inventar von Anwendung und Server samt Versionen ermöglicht erst den wiederkehrenden Abgleich mit Herstellerhinweisen. Die TikTok-Praxisaussage ergänzt den einmaligen Launch-Check um laufende Wartung; automatisch erzeugte Update-Befehle und Angriffsbehauptungen sind nicht validiert.
- 2026-10-11 · [[2026-10-11-voxyz_ai-2109328172273606771]] · meinung — Vox ergänzt den UI-Vorgänger um 25 Backend-/Betriebsprüfpunkte: serverseitige Rechte und Datenzugriffe, begrenzte Kosten, signierte/idempotente Zahlungs-Webhooks und tatsächlich erprobten Restore. Die Prüfliste ist ein konkreter Scope mit Fundstellen, keine Sicherheitsgarantie; echte Zahlungen und Produktionsdaten bleiben außerhalb des Tests.

## Spannungen & offene Fragen

- Korrektur 2026-10-25: Bei [[2026-10-22-franzbruckhoff-2113401002355298410]] wurden Gesprächsantworten aus der Rohquelle entfernt. Der Beleg vom 22.10. stützt sich weiterhin auf den Hauptprompt und die gekennzeichnete Ergänzung zu False Positives. Die damalige Aussage zu repospezifischen mehreren Prüfdurchgängen stammt aus einer entfernten Gesprächsantwort und gehört nicht mehr zum übernommenen Quelleninhalt.

- 2026-10-22: [[2026-10-19-voxyz_ai-2112302775547679169]] erweitert den ursprünglich lesenden Prüfauftrag um lokale oder Preview-Testinteraktionen und einen begrenzten Korrekturlauf. Testdaten, erlaubte Änderungen und menschlich zu prüfende Preis-, Rechts- und Datenschutzbefunde brauchen einen expliziten Scope. Vier simulierte Personas und ihre Rückkehrabsicht sind keine reale Nutzerstichprobe; [[Produktreife-durch-echte-Testnutzer]] liefert eine andere Art von Evidenz.

- 2026-10-09 · [[2026-10-04-emilkowalski-2106752670405099523]] beschreibt mit `/break-ui` eine Variante mit Daten-Fixture und anschließenden Korrekturen. Das erweitert den ursprünglich lesenden Prüfauftrag; Prüfen, Erzeugen von Testdaten und Codeänderungen brauchen jeweils klaren Scope. Rendering mit Extremdaten belegt keine vollständige Release- oder Hardware-Abnahme.

- Die beiden Vox-Fassungen prüfen unterschiedliche Bereiche (26.09.: Design, Mobile, UI-Zustände; 27.09.: Security, Daten, Abläufe, Umgebung). Offen ist, ob beide Kataloge zusammen gehören oder je nach App-Typ gewählt werden.
- Zwei der drei Belege stammen vom selben Autor; unabhängig ist bisher nur die Checkliste.

- 2026-10-24: [[2026-10-22-franzbruckhoff-2113401002355298410]] warnt, dass erzwungenes Weitersuchen False Positives erzeugen kann; reproduzierbare Befunde sind wichtiger als eine behauptete Vollständigkeit. [[2026-10-23-openai-securing-our-frontier-model-training-environment]] ergänzt kontinuierliche, isolierte Infrastrukturtests unter angenommenem Versagen innerer Kontrollen. Das ist nicht derselbe Scope wie ein lesender App-Audit; belastende Versuche benötigen eine dafür freigegebene Testumgebung.

## Verwandte Patterns

- [[Kontrollierte-Agent-Parallelisierung]]
- [[Plan-first-mit-getrenntem-Review]]
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
