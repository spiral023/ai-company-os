# Matt Pockocks „Skills for Real Engineers“: Briefing für Podcast und Präsentation

## Zweck und Quellenbasis

Dieses Briefing erklärt Matt Pockocks Open-Source-Sammlung `mattpocock/skills` für Menschen, die AI Coding Agents professionell einsetzen wollen. Es basiert auf dem lokalen Stand des Repositories vom 10. Juli 2026, insbesondere auf der README und den Original-Skills `grill-with-docs`, `grilling`, `domain-modeling`, `wayfinder`, `codebase-design`, `improve-codebase-architecture`, `prototype`, `research`, `to-spec`, `to-tickets`, `implement`, `tdd`, `diagnosing-bugs` und `code-review`. Ergänzend wurden die Architekturtexte `DEEPENING.md` und `DESIGN-IT-TWICE.md` sowie Matt Pockocks eigene Dokumentation auf AI Hero berücksichtigt.

Die Sammlung steht unter der MIT-Lizenz. Sie ist aktiv in Entwicklung. Einzelne Namen, Details und Abläufe können sich deshalb verändern. Entscheidend sind die zugrunde liegenden Engineering-Prinzipien, nicht die exakte Schreibweise eines Commands.

## Die Kernthese

AI Coding Agents machen Programmieren schneller, aber Geschwindigkeit löst die klassischen Probleme der Softwareentwicklung nicht. Sie kann sie sogar verschärfen. Ein Agent kann schneller missverstehen, schneller ungetesteten Code produzieren und schneller eine schwer wartbare Architektur aufbauen. Matt Pockocks Antwort ist kein großes Framework, das den gesamten Entwicklungsprozess übernimmt. Seine Skills sind kleine, anpassbare und kombinierbare Arbeitsanweisungen. Jeder Skill korrigiert einen bestimmten Fehlermodus und erzeugt ein klar definiertes Ergebnis: eine geklärte Entscheidung, ein Glossar, eine Architekturkarte, ein Ticket, einen Testzyklus oder einen Review-Bericht.

Das unterscheidet die Sammlung von umfassenden Methoden wie BMAD, GSD oder Spec Kit. Die Skills wollen dem Entwickler nicht die Kontrolle über den Prozess abnehmen. Sie sollen Engineering-Grundlagen so präzise formulieren, dass ein Agent sie wiederholbar anwenden kann. Der Mensch bleibt Entscheider, insbesondere bei Produktfragen, Architektur-Trade-offs und HITL-Aufgaben – „human in the loop“.

## Vier Fehlermodi, gegen die die Sammlung arbeitet

### 1. Der Agent baut nicht das, was der Mensch wollte

Das Grundproblem ist Misalignment. Menschen kennen ihre Anforderungen oft selbst noch nicht vollständig. Ein kurzer Prompt verdeckt offene Entscheidungen, Randfälle und widersprüchliche Begriffe. Der Agent füllt diese Lücken mit plausiblen Annahmen und liefert möglicherweise technisch sauberen Code für das falsche Produkt.

Die Antwort ist `grill-with-docs`. Der Skill startet eine konsequente Befragung über den wiederverwendbaren `grilling`-Skill. Fragen werden einzeln gestellt, weil mehrere Fragen gleichzeitig zu oberflächlichen Antworten führen. Fakten, die im Repository auffindbar sind, soll der Agent selbst recherchieren. Entscheidungen bleiben beim Menschen. Gleichzeitig aktiviert `grill-with-docs` das `domain-modeling`: Begriffe werden geschärft, konkrete Szenarien und Grenzfälle geprüft, Widersprüche zwischen Gespräch und Code offengelegt und belastbare Erkenntnisse sofort dokumentiert.

### 2. Mensch und Agent sprechen nicht dieselbe Sprache

Vage oder überladene Begriffe erzeugen lange Erklärungen und inkonsistente Namen. `domain-modeling` pflegt deshalb eine Ubiquitous Language in `CONTEXT.md`. Das Dokument ist bewusst nur ein Glossar – keine Spezifikation und kein Sammelplatz für Implementierungsdetails. Wenn „Account“ einmal Nutzerkonto, einmal Kunde und einmal Abonnement meint, fordert der Skill eine präzisere kanonische Benennung.

Schwer umkehrbare und überraschende Architekturentscheidungen können als ADR, als Architecture Decision Record, festgehalten werden. Ein ADR ist aber nur sinnvoll, wenn drei Kriterien erfüllt sind: Die Entscheidung ist teuer rückgängig zu machen, ohne Kontext überraschend und das Ergebnis eines echten Trade-offs. Dadurch soll die Dokumentation klein und wertvoll bleiben.

Die Wirkung reicht über schönere Dokumente hinaus. Gemeinsame Begriffe verbessern Datei-, Funktions- und Typnamen. Sie verkürzen Prompts und Antworten. Sie helfen Agenten, die Codebasis zu navigieren, weil Domain-Sprache und Code-Sprache näher zusammenrücken.

### 3. Der Code funktioniert nicht zuverlässig

Schnelle Codegenerierung ohne Feedback Loop ist Blindflug. Der `tdd`-Skill fordert Red vor Green: Zuerst muss ein Test am vereinbarten Seam scheitern, dann wird nur so viel implementiert, dass er besteht. Ein Seam ist die Stelle, an der Verhalten von außen beobachtet wird. Tests prüfen öffentliche Interfaces und Nutzerverhalten, nicht private Implementierungsdetails.

Die Sammlung warnt vor drei verbreiteten Testfehlern. Implementierungsgekoppelte Tests brechen bei internen Refactorings, obwohl das Verhalten unverändert bleibt. Tautologische Tests berechnen den erwarteten Wert mit derselben Logik wie der Produktivcode und können deshalb kaum einen Fehler entdecken. Horizontales TDD schreibt erst alle Tests und danach die gesamte Implementierung. Matt Pockock bevorzugt vertikale Tracer Bullets: ein Verhalten, ein fehlschlagender Test, eine minimale Implementierung – dann der nächste Slice.

Für schwierige Fehler gibt es `diagnosing-bugs`. Dessen wichtigste Phase ist nicht das Formulieren einer Hypothese, sondern der Aufbau eines schnellen, deterministischen und agentenfähigen Feedback Loops, der exakt den gemeldeten Fehler reproduzieren kann. Erst danach folgen Minimierung, drei bis fünf falsifizierbare Hypothesen, gezielte Instrumentierung, Fix und Regressionstest. Kann kein passender Test-Seam gefunden werden, ist das selbst ein Architektur-Finding.

### 4. Der Agent beschleunigt den „Ball of Mud“

Mehr Code pro Stunde bedeutet auch mehr potenzielle Entropie. Die Architektur-Skills übersetzen Ideen aus John Ousterhouts „A Philosophy of Software Design“ in ein präzises Vokabular:

- Ein **Module** ist etwas mit Interface und Implementation – unabhängig davon, ob es eine Funktion, Klasse, ein Package oder ein systemübergreifender Slice ist.
- Das **Interface** umfasst alles, was ein Caller wissen muss: Typen, Invarianten, Reihenfolge, Fehlerfälle, Konfiguration und Performance-Eigenschaften.
- **Depth** beschreibt den Leverage des Interfaces. Ein tiefes Module versteckt viel sinnvolles Verhalten hinter einem kleinen Interface. Ein flaches Module reicht Komplexität fast unverändert weiter.
- Ein **Seam** ist eine Stelle, an der Verhalten verändert werden kann, ohne den aufrufenden Ort zu bearbeiten.
- Ein **Adapter** ist eine konkrete Implementation an einem Seam.
- **Leverage** ist der Nutzen für Caller: viel Verhalten für wenig erlerntes Interface.
- **Locality** ist der Nutzen für Maintainer: Wissen, Änderungen, Fehler und Verifikation konzentrieren sich an einer Stelle.

Die Sprache ist absichtlich streng. Begriffe wie „Component“, „Service“, „API“ oder „Boundary“ sollen nicht als unscharfe Synonyme dienen. Der zentrale Test ist der Deletion Test: Wenn ein Module gelöscht wird, verschwindet dann echte Komplexität – oder verteilt sie sich nur auf viele Caller? Ein sinnvolles tiefes Module konzentriert Komplexität; ein flacher Middle Man verschiebt sie lediglich.

## `improve-codebase-architecture`: Architektur als regelmäßige Wartung

Dieser Skill scannt eine bestehende Codebasis nach „Deepening Opportunities“. Vorher liest er das Domain-Glossar und relevante ADRs. Die Erkundung sucht nicht mechanisch nach möglichst vielen Dateien oder Funktionen, sondern nach Reibung:

- Muss man zwischen vielen kleinen Modulen springen, um ein Konzept zu verstehen?
- Ist ein Interface fast so kompliziert wie seine Implementation?
- Wurden pure Funktionen nur deshalb extrahiert, damit man sie isoliert testen kann, während die echten Fehler in ihrer Orchestrierung stecken?
- Lecken eng gekoppelte Module Wissen über ihre Seams?
- Ist wichtiges Verhalten schwer über ein öffentliches Interface testbar?

Die Kandidaten werden nicht sofort umgesetzt. Der Skill erstellt einen visuellen HTML-Report mit Dateien, Problem, Lösung, Nutzen, Vorher-/Nachher-Diagramm und einer Empfehlungsstärke. Erst nachdem der Mensch einen Kandidaten ausgewählt hat, beginnt ein Grilling über Constraints, Abhängigkeiten, Interface, Seam und Teststrategie. Das verhindert den typischen „Refactoring Enthusiasm“-Fehler: eine breite Umbauaktion ohne priorisiertes Problem und ohne Zustimmung.

### Abhängigkeiten richtig einordnen

Der zugehörige Deepening-Leitfaden unterscheidet vier Abhängigkeitsarten:

1. **In-process:** reine Berechnung oder In-Memory-State. Solche Cluster können direkt vertieft und über das neue Interface getestet werden.
2. **Local-substitutable:** lokale Test-Stand-ins wie PGLite oder ein In-Memory-Dateisystem. Der Seam bleibt intern.
3. **Remote but owned:** eigene Services hinter Netzwerkgrenzen. Ein Port definiert das Interface; HTTP, gRPC oder Queue sind produktive Adapter, ein In-Memory-Adapter dient Tests.
4. **True external:** fremde Dienste wie Stripe oder Twilio. Die Abhängigkeit wird als Port injiziert und in Tests durch einen Mock-Adapter ersetzt.

Eine wichtige YAGNI-Regel lautet: Ein Adapter macht einen Seam nur hypothetisch, zwei Adapter machen ihn real. Abstraktionen sollen nicht vorsorglich entstehen. Wenn ein tiefes Module über sein neues Interface getestet wird, werden alte, an flache Interna gekoppelte Tests nicht zusätzlich behalten. Der Ansatz lautet „replace, don’t layer“.

### Design It Twice

Ist der richtige Kandidat gewählt, aber das Interface noch offen, empfiehlt die Sammlung mehrere radikal unterschiedliche Entwürfe. Ein Entwurf minimiert das Interface auf wenige Einstiegspunkte, einer maximiert Flexibilität, einer optimiert den häufigsten Caller und gegebenenfalls einer Ports & Adapters. Verglichen wird nicht nach Geschmack, sondern nach Depth, Locality und Seam Placement. Die erste plausible Idee wird dadurch nicht automatisch zur Architektur.

## `wayfinder`: Planung unter „Fog of War“

`wayfinder` ist für Vorhaben gedacht, die größer als eine Agenten-Session sind und deren Weg zum Ziel noch nicht sichtbar ist. Er ist nicht für jede Aufgabe sinnvoll. Wenn Ziel, Entscheidungen und Umsetzung bereits klar in eine Session passen, braucht man keine Map.

Der erste Schritt ist die Formulierung einer **Destination**: Woran erkennt man, dass die Erkundung fertig ist? Das kann eine freigabefähige Spezifikation, eine entschiedene Architektur oder eine ausreichend geklärte Migration sein. Danach wird die erste sichtbare **Frontier** aus präzise formulierbaren Untersuchungen und Entscheidungen kartiert. Unklare, aber in Richtung Destination liegende Bereiche bleiben als **Fog of War** unter „Not yet specified“. Ausdrücklich außerhalb der Destination liegende Arbeit kommt unter „Out of scope“.

Die Map ist ein Issue im Projekt-Tracker. Ihre Child Issues sind vier Typen:

- **Research (AFK):** Der Agent untersucht Primärquellen und liefert eine zitierte Notiz.
- **Prototype (HITL):** Ein billiges, bewusst wegwerfbares Artefakt macht eine abstrakte Frage konkret.
- **Grilling (HITL):** Mensch und Agent lösen eine Entscheidung im Gespräch.
- **Task (AFK oder HITL):** Eine notwendige Handlung schafft erst die Fakten, auf deren Grundlage später entschieden werden kann.

Tickets besitzen Blocking-Beziehungen. Die Frontier besteht aus offenen, nicht blockierten und nicht beanspruchten Tickets. Jede Session bearbeitet höchstens ein Ticket. Nach der Auflösung wird das Ergebnis am Ticket dokumentiert, die Map erhält nur einen kompakten Verweis, und neu sichtbar gewordene Fragen werden aus dem Fog in konkrete Tickets überführt. Das ist Progressive Disclosure für Projektplanung: Nur das kartieren, was aktuell scharf genug ist.

Der wichtigste Unterschied zu einem klassischen Projektplan: Wayfinder plant Entscheidungen, nicht automatisch Deliverables. Wenn der Weg klar ist, endet Wayfinding und die Umsetzung wird an Spec, Tickets und Implementierung übergeben.

## Der komponierte Idea-to-Ship-Workflow

Die Skills lassen sich als Kette mit klaren Übergaben verstehen:

1. **Setup:** `setup-matt-pocock-skills` konfiguriert Issue Tracker, Triage-Labels und den Ort von Domain-Dokumenten.
2. **Große Unklarheit:** `wayfinder` kartiert Destination, Frontier, Blocker und Fog. Bei kleinen Vorhaben entfällt dieser Schritt.
3. **Produkt- und Designklärung:** `grill-with-docs` interviewt den Menschen, pflegt `CONTEXT.md` und bietet bei wirklich tragenden Entscheidungen ADRs an.
4. **Konkretheit durch Experiment:** `prototype` erzeugt bewusst wegwerfbare Logik- oder UI-Prototypen, wenn Diskussion allein eine Frage nicht klären kann.
5. **Externe Fakten:** `research` untersucht Primärquellen und schreibt zitierte Findings in eine Markdown-Datei.
6. **Spezifikation:** `to-spec` synthetisiert den bereits geklärten Gesprächs- und Codebase-Kontext zu Problem, Lösung, User Stories, Implementierungs- und Testentscheidungen. Es beginnt bewusst kein neues Interview.
7. **Umsetzbare Arbeit:** `to-tickets` zerlegt die Spec in vertikale Tracer-Bullet-Tickets, die jeweils einen vollständigen, demonstrierbaren Pfad liefern und ihre Blocker angeben. Breite Refactorings verwenden Expand–Migrate–Contract.
8. **Implementierung:** `implement` arbeitet ein Ticket ab, verwendet TDD an vorher vereinbarten Seams, führt Typprüfung und Tests aus und übergibt anschließend an den Review.
9. **Qualitätssicherung:** `code-review` trennt zwei Achsen, die sich nicht gegenseitig verdecken dürfen: Standards-Review gegen Repo-Regeln und Code Smells sowie Spec-Review gegen das gewünschte Verhalten.

Diese Übergaben sind ein wesentlicher Designpunkt. `grill-with-docs` soll nicht heimlich implementieren. `wayfinder` soll nicht die Destination liefern, sondern den Weg klären. `to-spec` soll nicht erneut interviewen. `tdd` soll nicht spekulativ refactoren. Jeder Skill bleibt klein, weil er ein begrenztes Mandat besitzt.

## Drei anschauliche Anwendungsszenarien

### Szenario A: Ein neues SaaS-Feature

Ein Team möchte „flexible Abonnements“ bauen. Der Begriff ist unklar: Darf ein Kunde mehrere Abonnements haben? Was ist ein Planwechsel? Was passiert mit offenen Rechnungen? `grill-with-docs` klärt die Fälle und unterscheidet Customer, Subscription, Plan und Billing Cycle im Glossar. Eine schwer umkehrbare Entscheidung zur Prorating-Strategie wird als ADR dokumentiert. `to-spec` fasst die geklärten Anforderungen zusammen. `to-tickets` erzeugt vertikale Slices wie „bestehender Kunde wechselt zum Monatsende den Plan“ statt horizontale Tickets „Datenbank“, „Backend“, „Frontend“. `tdd` prüft das Verhalten über das Subscription-Interface. `code-review` kontrolliert getrennt, ob der Code sauber und ob das richtige Feature gebaut wurde.

### Szenario B: Eine alte Codebasis ist schwer änderbar

Bei jeder Preisänderung müssen fünf Dateien und mehrere Tests angepasst werden. `improve-codebase-architecture` identifiziert Shotgun Surgery und ein flaches Cluster. Der HTML-Report vergleicht den Ist-Zustand mit einem tieferen Pricing Module. Im Grilling wird entschieden, welches Verhalten hinter dem Seam liegt. „Design It Twice“ liefert alternative Interfaces. Der gewählte Entwurf konzentriert Rundung, Rabatte, Währung und Steuerregeln hinter einem kleinen Interface. Neue Tests laufen an diesem Interface, alte Tests an internen Hilfsfunktionen werden ersetzt. Das Ergebnis ist nicht zwangsläufig weniger Code, aber mehr Locality und Leverage.

### Szenario C: Eine große Migration ist noch zu unklar

Ein Unternehmen will von einer monolithischen Authentifizierung zu einem externen Identity Provider wechseln. Eine sofortige Spec wäre voller Annahmen. `wayfinder` definiert als Destination eine genehmigte Migrationsstrategie mit Rollback, Tenant-Isolation und Testkonzept. Die erste Frontier enthält Research zu Provider-Fähigkeiten, ein Prototype für Token-Claims und ein HITL-Grilling zu Migrationsrisiken. Fragen zur endgültigen Datenmigration bleiben zunächst im Fog, weil sie von den Claim- und Session-Entscheidungen abhängen. Nach jeder Auflösung wird die Karte präziser, bis eine Spec möglich ist.

## Kritische Einordnung und Grenzen

Die Sammlung ist bewusst meinungsstark. Das ist ihre Stärke und ihre Grenze.

- Grilling verbessert Alignment, kann aber bei kleinen oder reversiblen Änderungen unverhältnismäßig wirken. Die Kunst liegt darin, offene Entscheidungen zu erkennen und nicht jede Kleinigkeit zu interviewen.
- Ein Glossar hilft nur, wenn es aktuell bleibt und Domain-Sprache statt Implementierungsdetails enthält.
- Tiefe Module sind kein Aufruf zu großen Klassen oder monolithischem Code. Depth ist Leverage am Interface, nicht die Anzahl interner Codezeilen.
- „Ein Adapter hypothetisch, zwei real“ schützt vor Speculative Generality, darf aber nicht ignorieren, dass manche externe Systeme aus Sicherheits- oder Testgründen schon früh einen Port benötigen.
- TDD garantiert keine korrekten Anforderungen. Es verstärkt nur den Feedback Loop an den ausgewählten Seams. Schlechte Seams erzeugen fragile oder blinde Tests.
- Wayfinder kann in Ticket-Bürokratie kippen, wenn die Destination klein oder der Weg bereits klar ist. Der Skill enthält deshalb einen ausdrücklichen Abbruchtest.
- Die Skills hängen von der Fähigkeit des verwendeten Agents ab, Repository-Kontext wirklich zu lesen, Fragen ehrlich offenzulassen und Mandatsgrenzen einzuhalten.
- Da das Repository aktiv weiterentwickelt wird, sollten produktiv übernommene Skills versioniert, lokal geprüft und an die eigenen Repo-Regeln angepasst werden.

## Zentrale Botschaften für den Podcast

1. AI beschleunigt nicht nur Output, sondern auch Missverständnisse und Entropie.
2. Der Mensch ist nicht aus dem Prozess entfernt; er wird an den richtigen Entscheidungen gezielt eingebunden.
3. Kleine, komponierbare Skills funktionieren wie Engineering-Disziplinen mit klaren Übergaben.
4. Gemeinsame Sprache ist Infrastruktur für Menschen und Agenten.
5. Gute Architektur bedeutet viel Verhalten hinter einem kleinen Interface: Depth, Leverage und Locality.
6. Tests gehören an bewusst gewählte Seams und prüfen Verhalten statt Interna.
7. Große Vorhaben brauchen unter Unsicherheit eine Frontier und Fog of War, keine erfundene Vollplanung.
8. Der End-to-End-Flow verbindet Klärung, Wissen, Spec, vertikale Tickets, TDD und zweiachsigen Review.
9. Die Sammlung ist kein Autopilot. Sie ist ein Werkzeugkasten, der Engineering-Urteil präziser und wiederholbarer macht.

## Redaktionelle Vorgaben für den langen Audio-Überblick

Der Podcast soll auf Deutsch als lebendiges Gespräch zweier fachkundiger Hosts entstehen. Zielgruppe sind Softwareentwickler, Tech Leads, Produktverantwortliche und Gründer mit ersten Erfahrungen mit Coding Agents. Er soll ungefähr 20 bis 30 Minuten wirken, verständlich beginnen und anschließend technisch in die Tiefe gehen.

Empfohlene Dramaturgie:

1. Einstieg mit dem scheinbaren Paradox: Warum kann zehnmal schnelleres Coding zu einer schlechteren Codebasis führen?
2. Matt Pockocks Gegenentwurf zu monolithischen Agenten-Frameworks: kleine Skills und klare Mandate.
3. Die vier Fehlermodi Misalignment, fehlende gemeinsame Sprache, schwache Feedback Loops und Architektur-Entropie.
4. Ausführlicher Walkthrough durch `grill-with-docs`, `domain-modeling`, `improve-codebase-architecture` und `wayfinder`.
5. Erklärung des kompletten Idea-to-Ship-Flows anhand des SaaS-Szenarios.
6. Kritische Diskussion: Wann sind die Skills hilfreich, wann entsteht Prozess-Theater?
7. Konkrete Einstiegsempfehlung: Setup, ein kleines Feature mit `grill-with-docs`, vereinbarte Test-Seams, anschließend Review; `wayfinder` und Architektur-Review nur bei passendem Problem.

Die Hosts sollen Begriffe wie Module, Interface, Seam, Adapter, Depth, Leverage, Locality, Frontier und Fog of War präzise erklären. Sie sollen keine unbelegten Erfolgszahlen erfinden, Matt Pockock nicht wörtlich imitieren und die Skills nicht als Garantie für fehlerfreie Software darstellen.

## Storyboard für die Präsentation

Die Präsentation soll detailliert, visuell klar und für einen 15- bis 20-minütigen Vortrag geeignet sein:

1. **Titel:** Skills for Real Engineers – AI Coding ohne Kontrollverlust
2. **Das Geschwindigkeitsparadox:** Mehr Output kann Misalignment, Bugs und Entropie beschleunigen
3. **Der Gegenentwurf:** kleine, komponierbare Skills statt eines allumfassenden Prozesses
4. **Die vier Fehlermodi:** falsches Ziel, falsche Sprache, fehlendes Feedback, Ball of Mud
5. **Grill with Docs:** Fragen → Szenarien → Glossar → ausgewählte ADRs
6. **Gemeinsame Sprache:** `CONTEXT.md` als Domain-Glossar, ausdrücklich keine Spec
7. **Architekturvokabular:** Module, Interface, Depth, Seam, Adapter, Leverage, Locality
8. **Deep vs. Shallow:** visuelle Gegenüberstellung mit Deletion Test
9. **Improve Codebase Architecture:** Explore → HTML-Kandidatenreport → Auswahl → Grilling → Interface-Design
10. **Abhängigkeiten und Tests:** in-process, local-substitutable, remote-owned, true external
11. **Wayfinder:** Destination, Map, Frontier, Blocker und Fog of War
12. **Tickettypen:** Research, Prototype, Grilling und Task; AFK gegenüber HITL
13. **Idea-to-Ship:** Setup → Wayfinder optional → Grill → Prototype/Research → Spec → Tickets → TDD → Review
14. **Vertikale Tracer Bullets:** ein demonstrierbares Verhalten pro Ticket statt Layer-Silos
15. **TDD an Seams:** Red → minimale Green-Implementation; Verhalten statt Interna
16. **Zweiachsiger Review:** Standards und Spec getrennt bewerten
17. **Praxisbeispiel:** Flexible SaaS-Abonnements vom vagen Wunsch bis zum geprüften Slice
18. **Grenzen:** Overhead, veraltete Docs, falsche Seams und Prozess-Theater
19. **Empfohlener Einstieg:** mit einem kleinen Feature beginnen, Artefakte klein halten, regelmäßig reflektieren
20. **Schlussgedanke:** AI ersetzt Engineering-Urteil nicht – gute Skills machen es wiederholbar

Die Slides sollen wenig Fließtext, klare Diagramme und konkrete Begriffe verwenden. Besonders geeignet sind ein Pipeline-Diagramm für den Idea-to-Ship-Flow, ein Deep-vs.-Shallow-Querschnitt, eine Wayfinder-Karte mit Frontier/Fog und eine Matrix für die vier Abhängigkeitskategorien.

## Lokale Primärquellen

- `external_repos/mattpocock/skills/README.md`
- `external_repos/mattpocock/skills/skills/engineering/grill-with-docs/SKILL.md`
- `external_repos/mattpocock/skills/skills/productivity/grilling/SKILL.md`
- `external_repos/mattpocock/skills/skills/engineering/domain-modeling/SKILL.md`
- `external_repos/mattpocock/skills/skills/engineering/wayfinder/SKILL.md`
- `external_repos/mattpocock/skills/skills/engineering/codebase-design/SKILL.md`
- `external_repos/mattpocock/skills/skills/engineering/codebase-design/DEEPENING.md`
- `external_repos/mattpocock/skills/skills/engineering/codebase-design/DESIGN-IT-TWICE.md`
- `external_repos/mattpocock/skills/skills/engineering/improve-codebase-architecture/SKILL.md`
- `external_repos/mattpocock/skills/skills/engineering/prototype/SKILL.md`
- `external_repos/mattpocock/skills/skills/engineering/research/SKILL.md`
- `external_repos/mattpocock/skills/skills/engineering/to-spec/SKILL.md`
- `external_repos/mattpocock/skills/skills/engineering/to-tickets/SKILL.md`
- `external_repos/mattpocock/skills/skills/engineering/implement/SKILL.md`
- `external_repos/mattpocock/skills/skills/engineering/tdd/SKILL.md`
- `external_repos/mattpocock/skills/skills/engineering/diagnosing-bugs/SKILL.md`
- `external_repos/mattpocock/skills/skills/engineering/code-review/SKILL.md`

