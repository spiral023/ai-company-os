# Action-Space-Design-nach-Modellfaehigkeit

**Konfidenz:** meinung

## Zweck

Verhindert, dass Agent-Tooling nach Feature-Vollständigkeit statt nach tatsächlicher Modellfähigkeit gestaltet wird. Adressiert, dass gute Agent-Systeme nicht durch mehr Tools entstehen, sondern durch Tools, die zur tatsächlichen Denk- und Arbeitsweise des jeweiligen Modells passen.

## Funktionsweise

Der „Action Space“ ist die Menge an Dingen, die ein Agent praktisch tun kann. Zu viele Tool-Optionen erhöhen Entscheidungs- und Fehlerlast, zu wenige limitieren Handlungsspielraum und Effizienz — das richtige Maß hängt vom Fähigkeitsprofil des konkreten Modells ab, nicht von einer abstrakten Idealliste. Interfaces müssen robust gemacht werden, nicht nur geprompted: Wenn Formattreue kritisch ist (z.B. strukturierte Rückfragen), gehört sie in ein eigenes Tool mit erzwungenem Output-Format statt in Freitext-Prompting, das bei Format-Anforderungen unzuverlässig bleibt. Tool-Entscheidungen müssen bei jedem Modell-Upgrade aktiv hinterfragt werden: ein Hilfskonstrukt, das ein schwächeres Modell brauchte (z.B. explizite Todo-Listen, periodische Reminders), kann bei einem stärkeren Modell zum Bottleneck werden (z.B. Wechsel zu einem Task-Tool mit Abhängigkeiten und Subagent-Koordination). Progressive Disclosure gilt auch für den Kontextaufbau selbst: der Agent liest zuerst eine relevante Datei, die auf weitere verweist, und traversiert schrittweise tiefer statt alles upfront in den Prompt zu laden — das reduziert Context Rot. Spezialisierte Subagents (z.B. ein „Guide-Subagent“ für Selbstfragen über das eigene System) erweitern den Action Space funktional, ohne den globalen Tool-Space für alle Aufgaben aufzublähen. Tool-Design bleibt dabei grundsätzlich „an Art, not a Science“ — modell-, ziel- und umgebungsabhängig, ohne statische Regelbibliothek.

## Vorteile

- Verhindert Tool-Wildwuchs: neue Tools werden nur bei diagnostizierter Verhaltenslücke hinzugefügt, nicht nach Gefühl oder Feature-Parität zu anderen Systemen.
- Macht sichtbar, dass „Tool-Nutzung messen“ (nutzt das Modell ein Tool tatsächlich korrekt und freiwillig?) wichtiger ist als „Tool-Verfügbarkeit messen“.
- Capability-Reviews als Routine verhindern, dass veraltete Hilfskonstrukte unbemerkt zum Bottleneck werden, wenn sich die Modellfähigkeit verbessert.

## Nachteile & Grenzen

- Erfordert laufende Beobachtung realer Modell-Outputs statt einmaliger Tool-Entscheidung — das ist Beobachtungsaufwand, kein Einmalaufwand.
- Ohne Instrumentierung (wird ein Tool tatsächlich genutzt?) bleibt die Einschätzung subjektiv.
- Die explizite Aussage „an Art, not a Science“ bedeutet, dass sich das Pattern nicht in eine feste Checkliste übersetzen lässt — es bleibt Erfahrungswissen.

## Wann einsetzen, wann nicht

- Einsetzen: beim Design eigener Agent-Tools/Subagents/Skills, und regelmäßig erneut bei jedem größeren Modell-Upgrade des eingesetzten Coding Agents.
- Nicht einsetzen: bei reiner Nutzung bereits fertiger Standard-Tools ohne eigenen Tool-Bau — dort betrifft das Pattern höchstens die Auswahl, welche vorhandenen Tools/MCPs aktiviert werden.

## Belege

- 2026-02-27 · [[2026-02-27-thariq-lessons-building-claude-code]] · meinung — X-Thread von Thariq (Anthropic, Claude-Code-Team) beschreibt drei konkrete Fallstudien aus der Claude-Code-Entwicklung: AskUserQuestion-Tool (drei gescheiterte Anläufe bis zur robusten Lösung), Todos→Task-Tool-Wechsel bei Modell-Upgrade, Progressive Disclosure beim Kontextaufbau via Guide-Subagent.

## Spannungen & offene Fragen

- Einzige bisherige Quelle ist ein einzelner Erfahrungsbericht aus der Claude-Code-Entwicklung selbst — hohe Glaubwürdigkeit durch Insider-Perspektive, aber keine unabhängige Zweitquelle.
- Offene Frage: Wie lässt sich „Tool-Nutzung messen, nicht nur Verfügbarkeit“ in unserem eigenen Skill-System (30_Skills/) praktisch umsetzen, ohne ein aufwendiges Instrumentierungssystem zu bauen?

## Verwandte Patterns

- [[Erweiterungs-Ebenen-Zuordnung]]
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
