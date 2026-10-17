# Schema-als-Vertrag-mit-generierten-Clients

**Konfidenz:** meinung

## Zweck

Strukturelle API-Verträge für Produzenten, Verbraucher und Coding Agents aus einer gemeinsamen Quelle bereitstellen, statt Payloads aus getrennt gepflegter Prosa zu rekonstruieren.

## Funktionsweise

Requests und Responses in einem versionierten, maschinenlesbaren Schema definieren. Laufzeitvalidatoren, Typen, API-Spezifikation und Clients daraus ableiten oder über typisierte Schnittstellen anbinden. CI regeneriert die Artefakte, prüft ihren Versionsstand und führt Typechecks der betroffenen Verbraucher aus. Bestehende APIs schrittweise an den am häufigsten genutzten Grenzen anbinden. Prosa erläutert Zweck und Einsatzbedingungen; fachliche Semantik und Laufzeitverhalten werden zusätzlich geprüft.

## Vorteile

- Pflichtfelder und erlaubte Werte sind direkt für Menschen und Agents lesbar.
- Generation vermeidet unabhängig gepflegte Kopien desselben strukturellen Vertrags.
- Inkompatible Änderungen können bei angebundenen Verbrauchern vor der Auslieferung sichtbar werden.

## Nachteile & Grenzen

- Generatoren, Schema-Pakete und Clients brauchen Versionspflege und passende CI-Abdeckung.
- Compile-Erfolg prüft keine vollständige Fachsemantik und garantiert keine Kompatibilität unabhängig ausgelieferter Versionen.
- Behauptete Token- und Latenzeinsparungen sind in der ersten Quelle nicht gemessen.

## Wann einsetzen, wann nicht

- Einsetzen: wiederholt falsch verwendete API-Grenzen, mehrere Clients oder Services, Agent-Integrationen mit häufigen Payloadfehlern.
- Nicht einsetzen: ein vollständiger Architekturumbau nur für einen einmaligen Aufruf; zuerst eine begrenzte Schnittstelle prüfen.

## Belege

- 2026-10-11 · [[2026-10-11-shiptypes-ship-types-not-docs]] · meinung — Beschreibt Schema-first, Laufzeitvalidierung, generierte Clients und CI-Typechecks; das Veröffentlichungsdatum ist im Archiv unsicher, Codeschnipsel und behauptete Einsparungen wurden nicht verifiziert.
- 2026-10-12 · [[2026-10-12-sarahfim-2109736893198016898]] · meinung — Die Autorin empfiehlt Ende-zu-Ende-Typisierung mit tRPC und OpenAPI, damit der Compiler bei Schemaänderungen betroffene Aufrufer aufzeigt; der Bericht belegt weder eine automatische fachliche Konsistenzprüfung noch die isolierte Wirksamkeit dieses Mechanismus.

## Spannungen & offene Fragen

- 2026-10-11: Die Quelle setzt erfolgreichen Compile stellenweise mit korrektem API-Verhalten gleich. Ihr eigenes Schema-first-Beispiel enthält zugleich Laufzeitvalidierung; Versionskompatibilität und fachliche Regeln bleiben separate Prüfaufgaben.

## Verwandte Patterns

- [[Fachregel-Konsolidierung-vor-Featureaenderung]]
- [[Refactoring-mit-Verhaltensvergleich]]
- [[Testharness-als-staerkster-Hebel]]
