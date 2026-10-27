<!-- Generiert aus 80_Knowledge/Factory/pilot.json mit wissen karten. -->
# Fähigkeitskandidat: Implementierungsplanung

**Stand:** 2026-10-26 · **ID:** `f-implementierungsplanung` · **Status:** Kandidat, nicht aktiviert

Eine geklärte Spec in überprüfbare Arbeitseinheiten und tatsächliche Abhängigkeiten übersetzen.

## Eingaben

- Spec, Architekturgrenzen, aktuelle Codeversion und erkennbare Testmöglichkeiten.

## Prüfbare Ausgaben

- Lokaler Aufgabenplan mit Verhalten, Abnahmekriterien und Blockern.
- Für größere Aufgaben ein getrennter Ausführungsplan mit aktuellen Dateien, Symbolen und Prüfnachweisen.

## Einsatzbedingungen

- Ziel und Scope sind hinreichend geklärt.
- Mechanische Migrationen brauchen eine begründete Integrationsgrenze statt künstlicher isolierter Slices.

## Vorgehen als Entwurf

- Demonstrierbare Arbeitseinheiten schneiden und echte Blocker benennen.
- Das Ticket beschreibt Verhalten; ein zeitnaher Ausführungsplan konkretisiert bei Bedarf Dateien und Symbole.
- Für jede Einheit einen prüfbaren Abschluss und benötigte Eingaben angeben.
- Planumfang proportional zur Aufgabe halten und unklare Abhängigkeiten sichtbar lassen.

## Abnahme

- Jede Einheit besitzt ein beobachtbares Ergebnis und einen benannten Nachweis.
- Blocker sind begründet; eine Reihenfolge ohne Abhängigkeit wird nicht als harte Blockade dargestellt.

## Stop und Eskalation

- Fehlende Spec oder Prüfmöglichkeit klären, bevor der Plan als ausführbar gilt.
- Keine Tracker-Publikation oder Umsetzung allein durch die Erstellung dieses Kandidaten.

## Laufzeit und Wirkungen

- Lesender Projektzugriff genügt für den lokalen Entwurf.
- pstack-Checker, Spezialagenten und Tracker bleiben optionale, gesondert zu prüfende Adapter.

## Grenzen und Gegenargumente

- Der Plan beweist weder eine richtige Aufwandsschätzung noch funktionierende Umsetzung.

## Aussagen und Belege

Die IDs verweisen auf die versionierten Belegbereiche in [pilot.json](../Factory/pilot.json). Mehrere Stellen derselben Herkunftsfamilie sind keine unabhängigen Bestätigungen.

- `c12` — Verhaltenstickets sollen schmale verifizierbare Slices und explizite Blocker enthalten; mechanische Migrationen sind eine benannte Ausnahme.
- `c22` — To-tickets vermeidet im langlebigen Ticket grundsätzlich konkrete Dateipfade und Codefragmente; präzise prototypische Entscheidungen sind eine Ausnahme.
- `c23` — Der große pstack-Plan benennt konkrete Dateien, Symbole und beobachtbare Resultate; im Planmodus wird noch nicht implementiert.
- `c19` — In diesem Repo benötigen Commits einen ausdrücklichen Auftrag; Produktions-Deployments benötigen Freigabe. Lokale Entwürfe sind autonom erlaubt.

## Kleinster Versuch

Eine kleine Feature-Erweiterung und einen mechanischen Refactor planen lassen. Prüfen, ob unterschiedliche Zuschnitte und Integrationsgrenzen begründet werden und jedes Ergebnis überprüfbar ist.

Der Versuch ist vorbereitet. Eine praktische Wirksamkeitsmessung und produktive Übernahme stehen aus. Die bestehende Skill-Registry und die Repo-Freigaberegeln bleiben maßgeblich.
