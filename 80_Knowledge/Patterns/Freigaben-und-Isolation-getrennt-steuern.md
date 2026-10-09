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

## Spannungen & offene Fragen

- 2026-10-09: Das Post-Bild spricht pauschal von OS-Schutz für alle Tool-Aufrufe; Menü und Guide-Screenshot benennen Python und Terminal. Abdeckung weiterer Tools und das Verhalten bei Backend-Ausfall sind nicht im Code geprüft.
- 2026-10-09: Der Preview-Hinweis im Screenshot begrenzt die starke Schutzdarstellung des Posts. Unabhängige Prüfung von Isolation, Netzwerkkontrolle und Freigabe-Fehlentscheidungen fehlt.

## Verwandte Patterns

- [[Sandbox-Komposition-aus-OS-Primitiven]]
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[Metrikband-gestufte-Agent-Autonomie]]
