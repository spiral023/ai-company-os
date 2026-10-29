# Bounded-Contexts-und-Uebersetzungsgrenzen-kartieren

**Konfidenz:** meinung

## Zweck

Verhindern, dass unterschiedliche fachliche Bedeutungen still in ein gemeinsames Modell gepresst werden oder Integrationen nur strukturell passende Daten austauschen.

## Funktionsweise

Einen Bounded Context als Geltungsbereich eines konsistenten Modells beschreiben: Fachsprache, Modell, beteiligte Software und Verantwortliche benennen. Eine Context Map hält die tatsächlich vorhandenen Beziehungen einschließlich Brüchen und widersprüchlicher Bedeutungen fest. Sie beginnt beim Istzustand und darf keine Wunscharchitektur vortäuschen.

Pro Integration klären, wer Bedeutung und Änderungen bestimmt. Ein Shared Kernel braucht gemeinsame Änderungsregeln; Customer/Supplier setzt echte Kooperation bei Prioritäten und Abnahme voraus. Ein Conformist übernimmt bewusst ein fremdes Modell. Eine Anti-Corruption Layer übersetzt fremde Begriffe und Operationen in die eigene Fachbedeutung. Separate Ways kann günstiger sein, wenn Integration wenig Nutzen stiftet. Diese Optionen sind kontextabhängige Entscheidungen.

**Übertragung auf Agents:** Bei einem Auftrag den fachlichen Context und die Übersetzungsfälle mitgeben. Gleichnamige Felder werden an Beispielen verglichen, statt ihre Gleichbedeutung vorauszusetzen. Contextgrenzen entscheiden keine automatische Aufteilung in Microservices oder Agentenrollen.

## Vorteile

- Erlaubt mehrere passende Modelle statt eines schwer pflegbaren Universalmodells.
- Macht Integrationsverantwortung und fachliche Übersetzung sichtbar.
- Verbindet gemeinsames Vokabular mit seinem tatsächlichen Geltungsbereich.

## Nachteile & Grenzen

- Übersetzung, Synchronisation und gemeinsame Modellpflege kosten Arbeit.
- Eine Karte kann veralten; technische Datenverträge reichen für Bedeutungsfragen nicht aus.
- Ein Bounded Context ist weder automatisch Deployment-, Mandanten- noch Berechtigungsgrenze.

## Wann einsetzen, wann nicht

- Einsetzen: komplexe Fachmodelle, mehrere Teams, Legacy-Anbindung und widersprüchliche Begriffe.
- Nicht einsetzen: als Pflichtzerlegung einer einfachen CRUD-Anwendung oder als Etikett für bestehende Ordner.

## Belege

- 2003-08-01 · [[2003-08-01-pdf-domain-driven-design]] · meinung — Kapitel 14, PDF-S. 205–246, behandelt Bounded Contexts, Context Map und Integrationsbeziehungen einschließlich kooperativer und bewusst getrennter Modelle; August 2003 ist monatsgenau. Die Agentenanwendung ist unsere Übertragung, keine Studie aus dem Buch.

## Spannungen & offene Fragen

- 2026-10-29: Einheitliche Sprache gilt innerhalb einer geklärten Modellgrenze. Ein globales Glossar kann Unterschiede verdecken, wenn es kontextabhängige Bedeutungen zu einer einzigen Definition vereinheitlicht.
- Gemeinsame Teams, Code-Repositories und Deployments können die Contextwahl beeinflussen, ersetzen aber keine Prüfung der Modellkonsistenz.

## Verwandte Patterns

- [[CONTEXT-Glossar]]
- [[Aggregate-durch-fachliche-Invarianten-begrenzen]]
- [[Schema-als-Vertrag-mit-generierten-Clients]]
- [[Kontrollierte-Agent-Parallelisierung]]
