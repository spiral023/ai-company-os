# Framework-Quellcode als idiomatische Referenz

**Konfidenz:** meinung

## Zweck

Einem Coding Agent passende Implementierungsbeispiele einer Abhängigkeit zusätzlich zur Dokumentation bereitstellen, damit er APIs und Muster nicht allein aus möglicherweise unpassendem Vorwissen zusammensetzt.

## Funktionsweise

Stand der Ausarbeitung: 2026-10-11. Brandes beschreibt am 2026-10-08 einen lokalen Ordner mit flachen Framework-Checkouts und eine klare Anweisung, diese bei passenden Fragen lesend als Referenz zu nutzen. Idiomatische Konstrukte und ihre Zusammenstellung werden direkt am Quellcode erschlossen.

Eine bereits vorhandene TikTok-Quelle vom 2026-06-06 empfiehlt dieselbe Grundidee für Dependencies über `opensrc` und optional `graphify`. Das neue Pattern bündelt damit einen bekannten Ansatz mit der neu ausgewerteten Framework-Erfahrung; eine zusätzliche Graph-Erzeugung ist keine Voraussetzung.

Als abgeleitete Übernahmebedingungen werden Version beziehungsweise Revision mit der Projektabhängigkeit abgeglichen und nur die für die Frage nötigen Beispiele oder Implementierungsstellen gelesen. Öffentliche APIs, fremde Interna und eigene Projektkonventionen bleiben getrennt. Die Quelle zeigt keinen vollständigen Wartungsprozess für diese Versionspassung.

Bestehende Lint-, Typ- und Verhaltenstests prüfen anschließend die eigene Änderung. Referenzen und statische Regeln können unterschiedliche Aspekte abdecken; weder ein idiomatisches Beispiel noch ein erfolgreicher Lint-Lauf weist korrektes Fachverhalten nach. Der lesbare Checkout erteilt keine Freigabe, fremde Scripts auszuführen.

## Vorteile

- Konkrete Beispiele ergänzen abstrakte API-Beschreibungen.
- Relevante lokale Implementierungen können dem Agenten gezielt zugänglich gemacht werden.
- Projekterfahrung lässt sich mit prüfbaren Regeln verbinden, statt ausschließlich über Stilprompts zu arbeiten.

## Nachteile & Grenzen

- Veraltete Referenzen oder übernommene Interna können unpassende Änderungen begünstigen.
- Zu breite Lektüre erhöht Kontext- und Pflegeaufwand.
- Die Quelle berichtet persönliche Projekterfahrung, keine vergleichenden Fehlerraten.
- Versionsabgleich und gezielte Lesegrenzen sind hier abgeleitete Ergänzungen, keine im Video vollständig geprüfte Routine.

## Wann einsetzen, wann nicht

- Einsetzen: bei Fragen zu idiomatischen Mustern einer konkreten Framework-Version.
- Nicht einsetzen: als Ersatz für öffentliche Dokumentation, eigene Konventionen und Verhaltensprüfung oder als ungeprüfte Einführung fremden Codes.

## Belege

- 2026-06-06 · [[2026-06-06-agenticjames-your-agent-is-referencing-documentation-when-it-should-be-reading-the]] · meinung — Die Bestandsquelle empfiehlt lokal bereitgestellten Dependency-Quellcode statt alleiniger Dokumentation und optional einen Knowledge Graph. Sie enthält weder eine gemessene Qualitätsverbesserung noch eine ausgeführte Versionsprüfung.
- 2026-10-08 · [[2026-10-08-moritz-brandes-sauberer-code-mit-claude-code-so-geht-s-wirklich]] · meinung — Brandes beschreibt lokal lesbare Framework-Checkouts und schreibt ihnen idiomatischere Ergebnisse zu. Ein kontrollierter Qualitätsvergleich und eine ausgeführte Versionspflege fehlen.

## Spannungen & offene Fragen

- 2026-10-11: Explizite, für Agents gedachte Konstrukte und gezielte Referenzen könnten helfen, während ein Bestandspattern dichte Trainingsdaten verbreiteter Stacks bevorzugt. Die Quelle belegt keine allgemeine Rangfolge; ein vergleichbarer eigener Aufgabenversuch bleibt offen.
- 2026-10-11: Wie werden Referenzrevision und tatsächlich genutzte Abhängigkeit gemeinsam aktuell gehalten?

## Verwandte Patterns

- [[Trainingsdaten-Dichte-als-Stack-Kriterium]]
- [[Codepfad-vor-Aenderung-nachvollziehen]]
- [[Helper-Nutzung-durch-Lint-erzwingen]]
- [[Refactoring-mit-Verhaltensvergleich]]
