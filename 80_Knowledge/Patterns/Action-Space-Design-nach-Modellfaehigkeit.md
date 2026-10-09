# Action-Space-Design-nach-Modellfaehigkeit

**Konfidenz:** mehrfach-belegt

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
- 2026-01-25 · [[2026-01-25-sankalp-claude-code-experience]] · meinung — Unabhängige Bestätigung anhand konkreter, reverse-engineerter Zahlen: Die vier Claude-Code-Subagent-Typen unterscheiden sich messbar in Tool-Zugriff, Kontext-Overhead und Kontext-Vererbung (Explore: 516 Token, read-only, kein Kontext-Erbe; Plan: 633 Token, alle Tools, volles Kontext-Erbe) — das Action-Space-Design ist je Subagent-Typ bewusst unterschiedlich zugeschnitten, nicht einheitlich.
- 2026-10-07 · [[2026-10-07-artificialanlys-2107911905822351609]] · meinung — Haikus 1578 Elo in AA-Briefcase, 33 % in Terminal-Bench und durch Verweigerungen beeinträchtigte 35 % in AutomationBench zeigen ein aufgabenspezifisches Fähigkeitsprofil; Tooling sollte mit eigenen Einsatz-Evals geprüft werden, da der Gesamtindex keine zuverlässige Automation garantiert.
- 2026-10-06 · [[2026-10-06-artificialanlys-2107467221421420919]] · meinung — Mistrals Ergebnisse unterscheiden sich stark zwischen AutomationBench (60 %), Terminal-Bench (27 %) und den drei Cyber-Teiltests (51 %, 16 %, 82 %); Agent-Tools und Einsatzbereiche benötigen passende Evals, denn weder der Gesamtindex noch der Cyber-Index belegen allgemeine Zuverlässigkeit oder Sicherheit.
- 2026-10-04 · [[2026-10-04-voxyz_ai-2106829206134931539]] · meinung — Ein zentraler API-Helper für Token, Retries und Fehlerformat bietet dem Agenten einen passenden Handlungspfad; Lint soll alternative Rohaufrufe beanstanden, doch die Quelle liefert weder einen Wirkungsnachweis noch eine allgemeine Begründung für zusätzliche Abstraktionen.

## Spannungen & offene Fragen

- Zwei unabhängige Erfahrungsberichte (Thariq aus der Claude-Code-Entwicklung selbst, Sankalp als externer Anwender mit eigener Reverse-Engineering-Messung) stützen die Kernaussage jetzt über bloße Einzelmeinung hinaus, auch ohne kontrollierte Studie.
- Offene Frage: Wie lässt sich „Tool-Nutzung messen, nicht nur Verfügbarkeit“ in unserem eigenen Skill-System (30_Skills/) praktisch umsetzen, ohne ein aufwendiges Instrumentierungssystem zu bauen?

## Verwandte Patterns

- [[Erweiterungs-Ebenen-Zuordnung]]
- [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
