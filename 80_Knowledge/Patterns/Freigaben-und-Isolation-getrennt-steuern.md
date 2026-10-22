# Freigaben-und-Isolation-getrennt-steuern

**Konfidenz:** meinung

## Zweck

Trennt die Entscheidung, ob eine Tool-Aktion vorher bestätigt werden muss, von den technischen Zugriffsgrenzen ihrer Ausführung. Verhindert, dass automatische Freigabe mit unbeschränktem Zugriff oder eine sichtbare Sandbox-Einstellung mit einer nachgewiesenen Sicherheitsgrenze gleichgesetzt wird. Grundlage: [[2026-10-08-unslothai-windows-sandboxing-mxc]].

## Funktionsweise

Unsloths Post-Bild zeigt Freigabe-Modi (`Ask for approval`, `Approve for me`, `Run automatically`) neben der Sandbox-Stufe (`Low`, `High`). `Approve for me` ist dort zusammen mit High ausgewählt. Die Freigabe-Ebene entscheidet über vorherige Rückfragen; die Isolationsebene steuert die Ausführungsumgebung. Low nutzt Softwareprüfungen, High ergänzt OS-Isolation für Python und Terminal.

Der archivierte Guide-Screenshot zeigt den Backend-Status pro Tool. Ohne funktionierende OS-Sandbox sollen riskante Aufrufe zuerst fragen. Der Modus `Full access` hebt laut Quelle sowohl die Software- als auch die OS-Sandbox auf. Er ist eine gesonderte Ausnahme, keine andere Bezeichnung für automatische Freigabe innerhalb derselben Grenzen.

Als Einordnung für die eigene Bewertung: Freigabe-Regeln, aktive Backends und erlaubte Zugriffe getrennt erfassen. Erst anschließend anhand konkreter Dateien, Netzwerke und Prozesse beurteilen, welche Isolation tatsächlich durchgesetzt wird. Die Quelle liefert dafür ein Bedienbeispiel, keine validierte Konfiguration für andere Tools.

## Vorteile

- Macht die Kombination aus Automatik und begrenzter Ausführungsumgebung sichtbar.
- Ein Status pro Tool zeigt genauer als ein globaler Schalter, welche Ausführung eine OS-Sandbox verwendet.
- Kennzeichnet Full access als Änderung der technischen Grenzen und nicht nur der Rückfragehäufigkeit.

## Nachteile & Grenzen

- Ein Freigabe-Klassifikator kann sich irren; eine Freigabe bestätigt nicht die Wirksamkeit der Isolation.
- Der Windows-Screenshot bezeichnet MXC ausdrücklich als Preview und nicht als Sicherheitsgrenze. High ist in diesem Beispiel daher kein pauschaler Sicherheitsnachweis.
- Die benannten Tool-Grenzen gelten für Python und Terminal; andere Tools wurden nicht geprüft.
- Schutzumfang und Rückfallverhalten sind produkt- und versionsabhängig. Die Unsloth-Implementierung ist lokal nicht im Code verifiziert.

## Wann einsetzen, wann nicht

- Einsetzen: beim Beschreiben oder Prüfen agentischer Tool-Ausführung, wenn automatische Freigabe und eine Sandbox gemeinsam angeboten werden.
- Nicht einsetzen: als Begründung für uneingeschränktes Vertrauen in eine Sandbox oder als Übernahme ungeprüfter Produkt-Einstellungen in einen anderen Agenten.

## Belege

- 2026-10-08 · [[2026-10-08-unslothai-windows-sandboxing-mxc]] · meinung — Unsloth zeigt getrennte Freigabe-Modi und Low-/High-Isolation, Status pro Python-/Terminal-Tool und Full access als Abschaltung beider Sandbox-Stufen; der ergänzende Windows-Screenshot enthält eine ausdrückliche Preview-Einschränkung.
- 2026-10-01 · [[2026-10-01-floknowsai-diese-faehigkeiten-helfen-dir-2026-bei-deiner-arbeit-mit-ki-damit-du]] · meinung — Bei Connectoren wie MCP sollen Anwender erlaubte Tool-Zugriffe und sinnvolle Freigaben bewusst einschätzen; Harness, Tools und Regeln sind Teil der Agent-Kompetenz. Stützt die menschliche Zugriffsentscheidung, liefert aber keinen technischen Isolationsnachweis oder konkreten Freigabeplan.
- 2026-10-07 · [[2026-10-07-alex-sprogis-t3-code-endlich-eine-steuerzentrale-fuer-alle-de]] · meinung — Die Demo zeigt getrennte Einstellungen für Freigabemodus und neue Worktrees, zugleich aber weitreichenden Zugriff als Voreinstellung. Ein Moduswechsel ist kein Beleg dafür, dass destruktive Aktionen zuverlässig verhindert werden.
- 2026-01-04 · [[2026-01-04-ai-news-strategy-daily-n-why-andrej-karpathy-feels-behind-and-what-it-mea]] · meinung — Ergebnisentscheidung, Herkunftsnachweise und begrenzte Werkzeugrechte bleiben im umgebenden Workflow verankert, während das Modell Vorschläge erzeugt. Die allgemeine Empfehlung liefert kein konkret geprüftes Berechtigungsmodell.
- 2026-08-14 · [[2026-08-14-claudedevs-2088332927189049738]] · meinung — Die Rolloutmeldung vom 14.08. ergänzt die Ankündigung vom 07.08.: vorhandene Default-Einstellungen sollen nur nach Rückfrage geändert werden; keine unabhängige Sicherheitsprüfung.
- 2026-08-07 · [[2026-08-07-claude-auto-mode-is-now-the-default-in-claude-code-for]] · meinung — Der beschriebene Auto-Mode klassifiziert Tool-Aktionen und setzt breite Interpreter-Allow-Regeln vorübergehend aus; er ist damit eine Freigabeschicht. Die veröffentlichten Injection-Werte gelten für bestimmte Modelle, Versionen und eine fremde Browser-MCP-Integration ohne native Browser-Schutzmechanismen und weisen keine eigene technische Isolation nach.
- 2026-10-10 · [[2026-10-10-satyanadella-2108931348857827686]] · meinung — Nadella fordert außerhalb des Modells liegende Berechtigungen und Containment-Grenzen sowie einen menschlichen Stopp laufender Aufgaben. Die Forderung trennt leistungsfähige Intelligenz von Handlungsautorität, liefert aber keinen Nachweis einer konkreten implementierten Sicherheitsgrenze.
- 2026-10-11 · [[2026-10-11-developers-codex-as-a-platform-build-on-the-open-agent-harn]] · meinung — Die Anwendung bestimmt im beschriebenen `app-server`-Ansatz zugängliche Tools und Daten sowie fachliche Zustimmung, während Codex konfigurierte Sandbox- und Approval-Policies ausführt. Die Existenz dieser Integrationsflächen beweist weder die Sicherheit einer konkreten Konfiguration noch eine vollständige Übertragung der Produktverantwortung.
- 2026-10-02 · [[2026-10-02-zdfheute-nachrichten-videopodcast-droht-die-ki-apokalypse-lanz-precht]] · meinung — Das Gespräch macht behauptete Sandboxgrenzen und die Möglichkeit ihres Überschreitens zur Risikofrage; die konkrete Prüfung aktiver technischer Grenzen ist eine fachliche Ableitung aus dieser Diskussion, kein durch die Sendung validiertes Sicherheitsverfahren.
- 2026-10-18 · [[2026-10-18-ai-news-strategy-daily-n-what-really-happens-when-ai-agents-meet-in-the-w]] · meinung — Jones trennt dauerhafte Harnesskontrolle von der Kompensation gegenwärtiger Modellschwächen und nennt Geld-/Dateirechte, VM-Lebenszyklus und Abschaltbarkeit; die daraus abgeleiteten getrennten Prüfungen von Freigabe, Handlungsgrenze und Isolation sind keine im Video validierte Sicherheitskonfiguration.

## Spannungen & offene Fragen

- 2026-10-11: [[2026-10-10-satyanadella-2108931348857827686]] verlangt CoT-Transparenz, räumt zugleich deren unzuverlässige Treue ein. Plausible Modellbegründungen ersetzen daher keine extern prüfbaren Belege für wirksame Zugriffskontrolle oder Eindämmung.

- 2026-10-09: Das Post-Bild spricht pauschal von OS-Schutz für alle Tool-Aufrufe; Menü und Guide-Screenshot benennen Python und Terminal. Abdeckung weiterer Tools und das Verhalten bei Backend-Ausfall sind nicht im Code geprüft.
- 2026-10-09: Der Preview-Hinweis im Screenshot begrenzt die starke Schutzdarstellung des Posts. Unabhängige Prüfung von Isolation, Netzwerkkontrolle und Freigabe-Fehlentscheidungen fehlt.

## Verwandte Patterns

- [[Sandbox-Komposition-aus-OS-Primitiven]]
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[Metrikband-gestufte-Agent-Autonomie]]
