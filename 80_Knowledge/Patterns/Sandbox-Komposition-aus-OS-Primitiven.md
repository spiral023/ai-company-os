# Sandbox-Komposition-aus-OS-Primitiven

**Konfidenz:** meinung

## Zweck

Adressiert, dass kein einzelnes natives Betriebssystem-Feature den Bedarf eines Coding Agents an einer Sandbox typischerweise vollständig abdeckt. Ein Agent braucht offenen, nicht vorab bekannten Zugriff auf Shells, Git, Build-Tools und beliebige weitere Binaries — genau das widerspricht der Grundannahme vieler nativer Sandbox-Mechanismen, dass eine Anwendung ihren Zugriffsbedarf vorab kennt.

## Funktionsweise

Statt sich auf ein einzelnes OS-Feature zu verlassen, wird die Sandbox-Grenze aus mehreren Primitiven zusammengesetzt, die jeweils eine Teilfrage lösen. Am Beispiel Windows: Eine synthetische SID kombiniert mit write-restricted Process Tokens regelt Filesystem-Zugriff (Write/Execute/Delete auf definierte Pfade, explizit ausgeschlossen sensible Unterpfade wie `.git`). Rein *advisory* Schutzmaßnahmen (z. B. Proxy-Umgebungsvariablen für Netzwerkzugriff) reichen nicht — sie lassen sich von Programmen umgehen, die sie ignorieren oder einen eigenen Socket-Stack nutzen. Durchsetzende Kontrolle (z. B. Firewall-Regeln) braucht einen eigenen Principal, an den sich die Regel binden lässt — eine restricted SID allein reicht dafür nicht, weil Firewall-Regeln nicht an Non-Principal-Identitäten binden. Die praktische Konsequenz ist oft ein dedizierter, eigens angelegter lokaler Nutzer als Principal für den gesamten Sandbox-Prozessbaum, mit eigenen ACLs, eigenen Firewall-Regeln und verschlüsselt gespeicherten Credentials. Die Setup-Logik (Anlegen von Usern, SIDs, ACLs, Firewall-Regeln) wird dabei in ein separates, einmalig mit Admin-Rechten laufendes Hilfsbinary ausgelagert, damit die Hauptanwendung selbst unelevated und plattformunabhängig bleiben kann.

Die zentrale Designspannung dabei ist nicht Security als Selbstzweck, sondern **harte Durchsetzung vs. realistischer Entwickler-Workflow**: Eine zu strikte Isolation (z. B. eine vollständige VM-Sandbox) trennt den Agenten vom realen Checkout und Tooling des Nutzers ab; eine zu offene Lösung lässt sich umgehen. Jede Architekturentscheidung im Komponieren der Primitive bewegt sich zwischen diesen beiden Polen.

**Ergänzung 2026-10-09:** [[2026-10-08-unslothai-windows-sandboxing-mxc]] beschreibt für Python und Terminal eine zusätzliche OS-Isolation über MXC unter Windows, bubblewrap unter Linux und Seatbelt unter macOS. Softwareprüfungen bleiben davor bestehen. Der Windows-Screenshot zeigt einen aktiven Built-in-Container und einen alternativen Fallback mit Admin-Vorbereitung; er kennzeichnet MXC zugleich als Preview und ausdrücklich nicht als Sicherheitsgrenze. Das ist ein Herstellerbericht über eine weitere Umsetzung, keine verifizierte Schutzgarantie.

## Vorteile

- Deckt einen offenen, nicht vorab spezifizierbaren Zugriffsbedarf ab, den kein einzelnes natives Feature allein abdeckt.
- Jedes Primitiv löst eine klar abgegrenzte Teilfrage (Filesystem, Netzwerk, Prozessstart) — Fehler in einer Schicht kompromittieren nicht automatisch die anderen.
- Auslagerung der Setup-Logik in ein separates Hilfsbinary trennt einmaligen Admin-Bedarf von der täglichen, unelevated Nutzung.

## Nachteile & Grenzen

- Deutlich komplexer als ein einzelnes Sandbox-Feature — mehr bewegliche Teile, mehr potenzielle Fehlerquellen in der Komposition selbst.
- Plattformspezifisch bis auf die API-Ebene; das Prinzip ist übertragbar, die konkrete Umsetzung nicht.
- Erfordert einmalig erhöhte Rechte fürs Setup, auch wenn die tägliche Nutzung unelevated bleibt — ein zusätzlicher Vertrauens- und Wartungsaufwand.
- Die zentrale Spannung (Durchsetzung vs. Workflow-Realismus) ist nicht auflösbar, nur verhandelbar — es gibt keine Konfiguration, die beide Pole gleichzeitig maximiert.

## Wann einsetzen, wann nicht

- Einsetzen: Coding Agents oder vergleichbare Werkzeuge mit offenem, nicht vorab bekanntem Zugriffsbedarf (Shells, beliebige Build-Tools), auf Plattformen ohne ein einzelnes ausreichendes natives Sandbox-Feature.
- Nicht einsetzen: Anwendungen mit von vornherein bekanntem, engem Zugriffsbedarf — dort ist ein einzelnes passendes natives Feature (z. B. AppContainer) einfacher und ausreichend.

## Belege

- 2026-05-13 · [[2026-05-13-david-wiesen-openai-codex-windows-sandbox]] · meinung — OpenAI-Engineering-Bericht beschreibt, warum AppContainer, Windows Sandbox und Mandatory Integrity Control einzeln nicht ausreichten, und wie die finale Architektur aus SIDs, restricted Tokens, dedizierten lokalen Usern, Firewall-Regeln und separaten Hilfsbinaries komponiert wurde.
- 2026-08-18 · [[2026-08-18-docker-2089789519788728379]] · meinung — Docker Sandboxes laut Herstellerangabe in Claude-Code-Docs als MicroVM-Option (eigener Kernel und Daemon); Docs-Aufnahme nicht geprüft.
- 2026-09-29 · [[2026-09-29-openclaw-openclaw-enterprise-the-open-agent-platform-open]] · meinung — Herstellerankündigung: harte Grenzen trusted/untrusted, Sandboxing und feine Berechtigungen, Sandbox austauschbar. Referenzarchitektur steht aus, nicht prüfbar.

- 2026-07-21 · [[2026-07-21-claude-how-anthropic-secures-its-ai-native-software-dev]] · meinung — Anthropic beschreibt Remote-VMs mit beschränkten Netzwerkzielen und zweckgebundene Agent-Identitäten zur Begrenzung möglicher Schäden; Instruktionen werden um technische Grenzen ergänzt. Herstellerbericht, Implementierung nicht im Code geprüft.

- 2026-10-08 · [[2026-10-08-unslothai-windows-sandboxing-mxc]] · meinung — Unsloth kombiniert Softwarefilter mit OS-Backends für Python und Terminal und zeigt den Status pro Tool; der ergänzende Guide nennt einen Windows-Fallback und enthält eine Preview-Einschränkung. Implementierung und Schutzumfang sind lokal nicht im Code geprüft.

## Spannungen & offene Fragen

- Ergänzung (2026-10-05): [[2026-07-21-claude-how-anthropic-secures-its-ai-native-software-dev]] liefert einen weiteren Herstellerbericht über technische Grenzen, hier Remote-VMs, beschränkte Netzwerkziele und Agent-Identitäten. Das ergänzt die bisherige Perspektive, verifiziert aber weder die OS-Komposition noch die Implementierung.

- Einzige bisherige Quelle ist ein einzelner Herstellerbericht (OpenAI über die eigene Architektur), nicht unabhängig gegen den Quellcode oder eine zweite Plattform (macOS/Linux-Sandbox-Komposition) verifiziert.
- Verhältnis zu [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]: Dort wird Container-Isolation als „für viele Projekte zu aufwendig“ eingeordnet — dieser Bericht liefert die technische Begründung, warum die schwächere Alternative (rein advisory Schutz) tatsächlich nicht ausreicht, ohne den Aufwandseinwand selbst zu widerlegen.
- Offene Frage: Wie sieht die äquivalente Komposition auf macOS oder Linux aus, und teilen sich dort dieselben Grundprinzipien (kein Einzel-Primitiv reicht, Durchsetzung braucht einen eigenen Principal)?

- 2026-10-09: Die pauschale Darstellung im Post-Bild, OS-Schäden seien ausgeschlossen, steht gegen den Guide-Screenshot, der MXC als Preview und nicht als Sicherheitsgrenze bezeichnet. Die Frage nach belastbaren Datei-, Netzwerk- und Prozessgrenzen bleibt damit offen. → [[2026-10-08-unslothai-windows-sandboxing-mxc]]
- 2026-10-09: Der Post nennt weniger als 100 ms Overhead, der Guide 164 ms für Windows High. Low/High-Werte und 1–2 ms für reine Softwarechecks haben unklare Messbedingungen. Der behauptete geringe Overhead ist nicht reproduziert. → [[2026-10-08-unslothai-windows-sandboxing-mxc]]
- 2026-10-09: Die frühere Aussage einer einzigen Herstellerquelle ist inzwischen überholt; Unsloth ergänzt einen weiteren Bericht. Das verifiziert die konkrete OS-Komposition jedoch nicht. Freigabe-Automatik und aktive Isolation sind zudem verschiedene Ebenen. → [[Freigaben-und-Isolation-getrennt-steuern]]

## Verwandte Patterns

- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[CI-Agent-mit-Review-Gate]]
- [[Freigaben-und-Isolation-getrennt-steuern]]
