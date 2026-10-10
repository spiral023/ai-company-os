---
url: https://www.aihero.dev/ai-coding-dictionary
autor: Matt Pocock
datum: 2026-09-24
erfasst: 2026-09-27
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/00-index.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Agent-Coding präziser steuern: Kontext, Übergaben und Prüfung unterscheiden

Matt Pococks AI Coding Dictionary ordnet 71 Begriffe in sieben Bereiche. Sein praktischer Nutzen liegt für uns darin, unpräzise Fehlerbeschreibungen in überprüfbare Fragen zu übersetzen: Fehlt dem Agenten Wissen, funktioniert ein Werkzeug nicht, ist der Auftrag ungeklärt oder wurde das Ergebnis unzureichend geprüft? Diese Notiz bündelt die Unterscheidungen zu einer eigenen Arbeitslogik; sie bildet keine Definitionensammlung nach.

## Fehler auf der passenden Ebene untersuchen

Pocock trennt Model, Harness, Provider und Environment. Für eine Diagnose bedeutet das: Zuerst feststellen, welche Eingaben, Werkzeuge und Ergebnisse tatsächlich vorlagen. Ein Modellwechsel kann weder einen fehlenden Dateizugriff noch einen veralteten Tool result zuverlässig ausgleichen. Ein angekündigter Testlauf belegt außerdem keine ausgeführte Prüfung; entscheidend sind Tool call, Ergebnis und geprüfter Stand.

Die Trennung zwischen gespeichertem Modellwissen und aktuell geladenem Kontext macht API-Fehler untersuchbar. Ist die benötigte Signatur nie gelesen worden, helfen die installierten Typdefinitionen oder aktuelle Dokumentation. War die richtige Information bereits vorhanden, muss zusätzlich geprüft werden, ob der Agent sie übergangen hat oder inzwischen auf einem veralteten Snapshot arbeitet. Mehr Text ist dann keine automatische Verbesserung.

## Relevanten Kontext auswählen und Arbeitszustand erhalten

Die Quelle unterscheidet aufgabenrelevante Informationen von der gesamten Session-Historie und der technischen Kapazität des Context window. Daraus folgt für uns: Kontextqualität anhand benötigter Entscheidungen beurteilen, nicht anhand gefüllter Tokens. Lange Logs und fremde Teilaufgaben können Platz belegen, ohne die nächste Entscheidung zu unterstützen. Progressive disclosure verbindet kurze Orientierung mit gezielten Verweisen auf Details.

Memory, Compaction und Handoff verschieben Informationen zwischen Arbeitsphasen; sie ersetzen keine Verifikation. Ein Handoff ist eine verdichtete Darstellung des bisherigen Wissensstands. Er sollte Entscheidungen samt Begründung, konkrete Dateipfade, offenen Arbeitsumfang und Prüfbelege enthalten. Bei wichtigen Aussagen muss die nächste Session zum Code oder zum tatsächlichen Prüfergebnis zurückfinden können. Eine Zusammenfassung, die „fertig“ meldet, ist selbst kein Fertigstellungsnachweis.

## Planung vor unbeaufsichtigter Ausführung konkretisieren

Pocock verbindet Design concept, Grilling, Prototyping, Spec und Ticket. Die relevante Reihenfolge ist für uns: Ungeklärte Produktentscheidungen erkennen, durch Fragen oder einen kleinen Prototyp klären und erst danach in ausführbare Aufgaben übersetzen. Ein ausführlicher Plan kann verdeckte Annahmen ebenso dauerhaft festhalten wie gute Entscheidungen.

Ein Ticket braucht einen begrenzten Auftrag, Abnahmekriterien und Verweise auf erforderlichen Kontext. Ob es für eine Session passend zugeschnitten ist, zeigt sich am Arbeitsverlauf. Unabhängige Aufgaben können getrennt bearbeitet werden; Abhängigkeiten brauchen eine erkennbare Reihenfolge. Unbeaufsichtigte Ausführung setzt außerdem voraus, dass wesentliche Mehrdeutigkeiten vorher geklärt und Ergebnisse anschließend prüfbar sind.

## Unterschiedliche Nachweise kombinieren

Automated check, Automated review und Human review beantworten verschiedene Fragen. Tests und Typprüfung prüfen formulierte Eigenschaften. Ein anderer Agent kann zusätzliche Probleme vermuten, sein Urteil bleibt aber fehlbar. Menschliche Prüfung untersucht den tatsächlichen Diff und die Angemessenheit der Änderung. Ein positiver Agentenbericht übernimmt keine dieser Aufgaben vollständig.

Der AX-Begriff verbindet diese Ebenen: Ein navigierbares Repository, verständliche Fehlermeldungen, kurze Regeln und erreichbare Prüfwerkzeuge unterstützen Agenten stärker als immer längere Arbeitsanweisungen.

## Einordnung

Das Dictionary liefert einen begrifflichen Orientierungsrahmen, keine Evaluation von Effizienz oder Korrektheit. Seine Attention-Erklärung und genannten Kontextschwellen sind vereinfachte beziehungsweise umstrittene Orientierung; daraus folgt keine allgemeine Token-Grenze. Aussagen über Subagent-Tiefe, Berechtigungsmodi, Cache-Laufzeiten und Abrechnung müssen am konkreten Harness beziehungsweise Provider geprüft werden. Die lokale Sammlung ist ein archivierter Stand und eine Quelle. Diese eigenständige Analyse übernimmt keine Originaldefinitionen oder Zitate.

## Kernaussagen

- Bei falschem Output fehlende Fakten, übergangene Vorgaben und veraltete Snapshots getrennt untersuchen: [[Kontext-Hygiene-Entscheidungsbaum]].
- Handoffs erhalten Entscheidungen, müssen aber Rückwege zu Primärbelegen enthalten: [[Handoff-Doc]].
- Grüne Checks, Agentenurteile und menschliche Diff-Prüfung als unterschiedliche Nachweise behandeln: [[Testharness-als-staerkster-Hebel]].

## Verbindungen

- [[Kontext-Hygiene-Entscheidungsbaum]]: Ergänzt die Entscheidung über Nachladen oder Verdichten um eine Diagnose der tatsächlich vorhandenen Informationen.
- [[Handoff-Doc]]: Verbindet dauerhaftes Arbeitswissen mit überprüfbaren Verweisen auf Code und Prüfstände.
- [[Testharness-als-staerkster-Hebel]]: Präzisiert, welche Aussagen ein automatischer Check belegen kann und welche eine zusätzliche Beurteilung brauchen.
