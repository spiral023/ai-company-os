Erstelle einen langen, gehaltvollen deutschsprachigen Deep-Dive-Podcast als natürliches Gespräch zweier fachkundiger Hosts. Zielgruppe sind Softwareentwickler, Tech Leads, Gründer und Produktverantwortliche, die AI Coding Agents bereits ausprobiert haben und von „Vibe Coding“ zu belastbaren Engineering-Workflows kommen wollen.

Der Podcast soll nicht bloß Skills aufzählen. Entwickelt eine klare Argumentation: AI beschleunigt Codeproduktion, aber auch Misalignment, Bugs und Architektur-Entropie. Matt Pockocks Antwort ist ein komponierbarer Werkzeugkasten kleiner Skills mit begrenzten Mandaten, kein monolithischer Autopilot.

Erklärt ausführlich und mit anschaulichen Beispielen:

1. Die vier Fehlermodi aus der README: Der Agent baut das Falsche, Mensch und Agent sprechen unterschiedliche Sprache, Feedback Loops fehlen und die Codebasis wird zum Ball of Mud.
2. `grill-with-docs`, `grilling` und `domain-modeling`: eine Frage nach der anderen; Fakten im Repo selbst prüfen; Entscheidungen beim Menschen lassen; konkrete Grenzfälle durchspielen; kanonische Begriffe in CONTEXT.md erfassen; ADRs nur für schwer umkehrbare, überraschende echte Trade-offs anbieten. Betont, dass CONTEXT.md ein Glossar und keine Spec ist.
3. `codebase-design`: Definiert Module, Interface, Implementation, Depth, Seam, Adapter, Leverage und Locality exakt. Erklärt den Unterschied zwischen tiefen und flachen Modulen sowie den Deletion Test. Depth bedeutet Leverage am Interface, nicht möglichst viele interne Codezeilen.
4. `improve-codebase-architecture`: Domain-Glossar und ADRs lesen, Codebasis nach Reibung und Shallow Modules erkunden, Kandidaten als visuellen HTML-Report präsentieren, erst nach Auswahl grillen und Interfaces entwerfen. Erläutert Deepening, die vier Abhängigkeitskategorien und „replace, don't layer“ bei Tests. Bezieht „Design It Twice“ ein.
5. `wayfinder`: Für Vorhaben, die größer als eine Session sind und noch im Fog liegen. Erklärt Destination, Map, Child Tickets, Blocking-Beziehungen, Frontier, Fog of War und Out of Scope. Unterscheidet Research, Prototype, Grilling und Task sowie AFK und HITL. Betont: Wayfinder plant Entscheidungen, nicht automatisch Deliverables, und bearbeitet höchstens ein Ticket pro Session.
6. Den gesamten Idea-to-Ship-Flow: Setup → optional Wayfinder → Grill with Docs → bei Bedarf Prototype/Research → To Spec → To Tickets → Implement/TDD → Code Review. Zeigt, welches Artefakt jeder Skill erzeugt und was der nächste Skill davon übernimmt.
7. `to-tickets` und vertikale Tracer Bullets: ein schmaler, vollständiger und demonstrierbarer Pfad durch alle nötigen Layer statt horizontaler Silos. Erklärt Expand–Migrate–Contract als Ausnahme für breite Refactorings.
8. `tdd`, `diagnosing-bugs` und `code-review`: Tests an vereinbarten Seams, Verhalten statt Interna, Red vor Green, enger reproduzierbarer Feedback Loop vor Hypothesen sowie getrennte Review-Achsen Standards und Spec.

Nutzt mindestens zwei durchgehende Beispiele: ein vages SaaS-Feature für flexible Abonnements und eine große, noch unklare Authentifizierungs-Migration. Zeigt konkret, welcher Skill wann übernimmt und wann er ausdrücklich nicht geeignet ist.

Diskutiert kritisch die Grenzen: Prozess-Overhead bei kleinen Änderungen, veraltete Glossare, schlechte Seams, Speculative Generality, Ticket-Bürokratie und die Gefahr, Skills als Garantie statt als Arbeitsdisziplin zu behandeln. Keine erfundenen Erfolgszahlen, keine Garantieversprechen und keine unkritische Heldenverehrung. Matt Pockocks Position darf klar benannt, aber nicht imitiert werden.

Beginnt mit einem starken, konkreten Hook und endet mit einer pragmatischen Einstiegsempfehlung für ein Team: klein anfangen, ein echtes Feature mit Grill with Docs klären, Test-Seams vereinbaren, einen vertikalen Slice umsetzen und anschließend getrennt gegen Standards und Spec reviewen. Wayfinder und Architektur-Review nur einsetzen, wenn das Problem ihre zusätzliche Struktur rechtfertigt.

