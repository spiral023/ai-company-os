# Erster Entwurf: Wie Wissen einen Factory-Lauf steuert

**Stand:** 2026-10-25 · **Status:** Synthesevorschlag aus gezielt untersuchten Quellen und zehn Referenz-Repos; keine vollständige Bestandsanalyse und kein aktivierter Factory-Workflow.

## Leitidee

Ein Factory-Lauf bekommt einen konkreten Auftrag und einen überprüfbaren Vertrag. Der Wissenszugriff liefert pro Phase passende Methoden, Projektkontext, Entscheidungen und Gegenargumente. Übergeben werden versionierte Artefakte mit Herkunft. Die Laufzeit hält den Betriebszustand, die Wissensbasis hält wiederverwendbare Erkenntnisse.

Diese Aufteilung verbindet die [Loop-/Artefakt-Idee von Sprogis](../../80_Knowledge/Sources/2026-08-30-alex-sprogis-loop-graph-engineering-das-letzte-video-was-du-s.md), den [sichtbaren Spec–Build–Review-Ablauf von ZazenCodes](../../80_Knowledge/Sources/2026-10-19-zazencodes-factory-works-in-this-loop-a-feature-comes-through-the-spec-writer-which.md) und die [Randbedingungen begrenzter Autonomie von Friedman](../../80_Knowledge/Sources/2026-10-22-itamar_mar-2113255396299128887.md). Die Beispiele belegen keine allgemeine Leistungssteigerung. Ihre Kombination ist unsere zu prüfende Entwurfshypothese.

## Vertrag eines einzelnen Jobs

| Bestandteil | Inhalt |
|---|---|
| Auftrag | Nutzerziel, erwartetes Ergebnis, Projekt/Revision, enthaltene und ausgeschlossene Arbeit |
| Abnahme | Konkrete Kriterien, passende Prüfverfahren, benötigte Eingaben und benannte verbleibende Unsicherheit |
| Wissensstand | Verwendeter Snapshot, eigene Entscheidungen, relevante Aussagen und ausgewählte Fähigkeitsversionen |
| Ausführung | Zuständige Phase, Laufzeitadapter, verfügbare Tools, Dauer-/Iterations-/Kostenrahmen |
| Ergebnis | Artefakte, tatsächliche Änderungen, Prüfbelege, Restfragen und nötige menschliche Entscheidung |

Die vorhandenen Freigaberegeln bleiben maßgeblich. Dieser Entwurf definiert keine zusätzlichen Produktionsrechte. Eine gefundene externe Empfehlung ist ein Wissenseingang; sie erweitert den autorisierten Auftrag nicht.

## Ablauf und Wissensbedarf

| Phase | Benötigtes Wissen | Prüfbares Ausgangsartefakt |
|---|---|---|
| Auftrag klären | Mission, Produktwissen, Entscheidungen, Spec-Klärungsmethoden und bekannte Risiken | Abgegrenzter Auftrag mit offenen Fragen und Akzeptanzkriterien |
| Vorgehen auswählen | Vergleich geeigneter Methoden, Runtime-Bindungen, Voraussetzungen, Gegenargumente und frühere Ergebnisse | Begründeter Plan mit ausgewählten Fähigkeitsversionen |
| Umsetzung | Projektspezifische Regeln, aktuelle Codepfade, konkrete Teilaufgabe und Schnittstellen | Änderung plus Bericht tatsächlicher Umsetzung und ausgeführter Checks |
| Ergebnis prüfen | Auftrag/Abnahmevertrag, anwendbare Standards, relevante Fehlermodi und geeignete Prüfdaten | Getrennte Aussagen zu Spec-Erfüllung, Standards und beobachtetem Verhalten |
| Entscheidung treffen | Prüfergebnisse, erlaubte Aktionen, verbleibende Risiken und Fehlerpfad | Abschluss, begrenzte Nacharbeit oder konkrete menschliche Eskalation |
| Lernen | Laufartefakte, Korrekturen und Vergleich zur ursprünglichen Erwartung | Belegter Lernkandidat oder bewusste Entscheidung mit Geltungsbereich |

Eine Reparaturschleife erhält konkrete Befunde und endet nach ihrem vereinbarten Limit. Eine unerfüllbare Voraussetzung oder unklare Abnahme wird als Hindernis dokumentiert. „Der Reviewer sagt bestanden“ ersetzt weder die Belege noch den vereinbarten Prüfvertrag.

## Kontext je Rolle zusammenstellen

Der Spec-Writer braucht Produktabsicht, bestehende Entscheidungen und passende Klärungsmethoden. Der Builder braucht konkrete Eingaben und aktuelle Projektimplementierung. Der Reviewer braucht die Anforderung, die relevanten Standards und unabhängige Prüfmöglichkeiten. Alle drei laden Wissen aus demselben Bestand, aber für verschiedene Fragen.

Übergreifende Synthesen halten mögliche Gegenargumente sichtbar. Einzelne Prompts liefern begrenzte Verfahren. Das entspricht dem [Kontext-zur-Laufzeit-Prinzip](../../80_Knowledge/Sources/2025-06-23-boristane-context-engineering-is-what-makes-ai-magical.md), ohne daraus ein Versprechen über die Ergebnisqualität abzuleiten. Fremde Prompts werden nicht zu einem wachsenden gemeinsamen Systemprompt zusammenkopiert.

## Entscheidungen aus konkurrierenden Referenzen

| Spannung | Vorschlag für den Pilot | Grundlage |
|---|---|---|
| Umfassendes Framework oder kleine Methoden? | Ein expliziter eigener Ablauf mit wenigen ausgewählten Methoden; Frameworks als Alternativen vergleichen | pstack-Routing versus Matt-Pocock-Komposition, [Methodenrecherche](../../reports/2026-10-25-factory-methoden-recherche.md) |
| Wer besitzt den Jobstatus? | Genau eine Laufzeit als Eigentümer; Dateien sind Artefakte/Checkpoints oder rekonstruierbare Ansichten | Paperclip-Organisation, GSD-State und gstack-Checkpoints, [Methodenrecherche](../../reports/2026-10-25-factory-methoden-recherche.md) |
| Alle Methoden auffindbar oder nur freigegebene installieren? | Breiter Wissenskatalog, engere bewusste Aktivierung über vorhandene Regeln | Paperclip „Catalog install ≠ agent attach“, [Methodenrecherche](../../reports/2026-10-25-factory-methoden-recherche.md) |
| Langzeitwissen oder Sitzungsmemory? | Kuratierte Aussagen und Entscheidungen plus referenzierte Laufbeobachtungen | OpenWiki-Evidence und Claude-Mem-Abruf, [Referenzanalyse](../../reports/2026-10-25-factory-referenzsysteme.md) |
| Vollständige Neuanalyse oder schnelle Aktualisierung? | Erste vollständige Textbaseline; danach Abhängigkeiten erneuern und regelmäßig erneut querdenken | GraphRAG-Globalprinzip, Hash-Invalidierung und eigene Scope-Nachweise, [Architekturrecherche](../../reports/2026-10-25-factory-wissensarchitektur-recherche.md) |

## Kleinster aussagekräftiger Versuch

Eine klar begrenzte, wertvolle Aufgabenklasse in einem repräsentativen eigenen Projekt auswählen. Die Auswahl ist noch offen. Mehrere vergleichbare Aufgaben mit dem bisherigen Vorgehen und mit diesem Entwurf bearbeiten. Für beide dieselben Eingaben, Projektstände, Berechtigungen und Abnahmekriterien verwenden.

Vorab festhalten: Was gilt als korrekter Abschluss? Welche Fehler dürfen nicht entkommen? Wie viel menschliche Nacharbeit, Zeit und Modellkosten entstehen? Anschließend die Ergebnisse mit anonymisierter Reihenfolge beurteilen und die entscheidenden Prüfnachweise nachlesen. Der Pilot misst damit Nutzen und zusätzliche Prozesskosten gemeinsam.

Die [Wissensbasis-Evalfragen](../../60_Evals/Wissensbasis_Factory_Eval.md) prüfen zunächst, ob Wissen überhaupt besser verbunden und angewendet wird. Ein guter Wissensabruf ist eine Voraussetzung für den Factory-Pilot, kein Beweis für autonomen Betrieb.
