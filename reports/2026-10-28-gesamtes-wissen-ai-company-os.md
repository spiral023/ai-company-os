# Das Wissen des AI-Company-OS

**Gesamtsynthese des lokalen Quellenbestands und der im Index verzeichneten externen Repositories**  
**Stand: 28. Oktober 2026 · Sprache: Deutsch · Verwendung: lokales Wissens- und Arbeitsdokument**

**Abgrenzung des Snapshots:** Dieser Bericht hält den Bestand vor dem späteren Quellenlauf vom 28. Oktober 2026 mit neun weiteren Source-Notizen fest. Seine Bestandszahlen und der daraus erzeugte HTML-Atlas beziehen sich auf diesen Erfassungsstand; sie werden nicht automatisch mit dem Repository fortgeschrieben.

Dieses Dokument hat fünf Lesepfade: Kapitel 1–20 verbinden das Wissen zu einer Arbeitsweise; Kapitel 21 erschließt jedes Repo; Kapitel 22 bewahrt jeden Quellenbefund; Kapitel 23–24 dienen als Methodenkarte und Glossar; Kapitel 25 dokumentiert die tatsächliche Abdeckung.

- [1. Worum es in diesem Wissensbestand geht](#1-worum-es-in-diesem-wissensbestand-geht)
- [2. Das Grundmodell: Modell, Harness, Kontext und Umgebung](#2-das-grundmodell-modell-harness-kontext-und-umgebung)
- [3. Vom Ziel zum belastbaren Auftrag](#3-vom-ziel-zum-belastbaren-auftrag)
- [4. Planung, Spezifikation und Aufgabensteuerung](#4-planung-spezifikation-und-aufgabensteuerung)
- [5. Kontext gezielt aufbauen und über Sitzungen erhalten](#5-kontext-gezielt-aufbauen-und-über-sitzungen-erhalten)
- [6. Eine Codebasis für Agenten verständlich machen](#6-eine-codebasis-für-agenten-verständlich-machen)
- [7. Skills, Hooks, Tools und Plugins passend einsetzen](#7-skills-hooks-tools-und-plugins-passend-einsetzen)
- [8. Parallelität, Agententeams und Übergaben](#8-parallelität-agententeams-und-übergaben)
- [9. Verifikation: Fortschritt belegen und den Prüfer mitprüfen](#9-verifikation-fortschritt-belegen-und-den-prüfer-mitprüfen)
- [10. Autonomie, Sicherheit und menschliche Verantwortung](#10-autonomie-sicherheit-und-menschliche-verantwortung)
- [11. Modelle, Reasoning und Kosten wirtschaftlich wählen](#11-modelle-reasoning-und-kosten-wirtschaftlich-wählen)
- [12. UI, Designsysteme und verständliche Interaktion](#12-ui-designsysteme-und-verständliche-interaktion)
- [13. Videos und Motion als überprüfbare Produktion](#13-videos-und-motion-als-überprüfbare-produktion)
- [14. Wissen, Recherche, RAG und Memory](#14-wissen-recherche-rag-und-memory)
- [15. Bestehende Software verstehen, verändern und rekonstruieren](#15-bestehende-software-verstehen-verändern-und-rekonstruieren)
- [16. Produkte, Marketing, SEO und Schreiben](#16-produkte-marketing-seo-und-schreiben)
- [17. Lernen, Rollen und Einführung in Organisationen](#17-lernen-rollen-und-einführung-in-organisationen)
- [18. Von Einzelmethoden zu einer schlanken Agentic Software Factory](#18-von-einzelmethoden-zu-einer-schlanken-agentic-software-factory)
- [19. Die wichtigen Spannungen im Bestand](#19-die-wichtigen-spannungen-im-bestand)
- [20. Was sich aus dem Gesamtbestand praktisch ableiten lässt](#20-was-sich-aus-dem-gesamtbestand-praktisch-ableiten-lässt)
- [21. Alle 74 externen Repositories: Funktionen, Methoden und Grenzen](#21-alle-74-externen-repositories-funktionen-methoden-und-grenzen)
- [22. Vollständiges Register der Quellenlektüre](#22-vollständiges-register-der-quellenlektüre)
- [23. Vollständige Karte der 93 Patterns](#23-vollständige-karte-der-93-patterns)
- [24. Begriffsglossar aus dem AI Coding Dictionary](#24-begriffsglossar-aus-dem-ai-coding-dictionary)
- [25. Umfang, Abdeckungsnachweis und Grenzen dieser Synthese](#25-umfang-abdeckungsnachweis-und-grenzen-dieser-synthese)

## 1. Worum es in diesem Wissensbestand geht

Das AI-Company-OS sammelt Arbeitsweisen für Menschen, die mit KI Software und digitale Produkte entwickeln, Wissen aufbereiten und wiederkehrende Arbeit organisieren. Seine Quellen reichen von kurzen Praxistipps über lange Tutorials und Herstellerberichte bis zu ausführbaren Werkzeugen und umfangreichen Methoden-Repositories. Die gemeinsame Frage lautet: Wie wird aus einer Absicht ein brauchbares, überprüftes Ergebnis, wenn ein Agent einen erheblichen Teil der Ausführung übernimmt?

Eine tragfähige Antwort besteht aus mehreren zusammenhängenden Fähigkeiten: das richtige Problem wählen, Anforderungen klären, relevantes Wissen bereitstellen, die Arbeitsumgebung verständlich machen, Fortschritt prüfen, Eingriffsrechte begrenzen und aus tatsächlichen Fehlern lernen. Die Bibliothek enthält viele Varianten dieser Fähigkeiten. Keine einzelne Quelle und kein einzelnes Framework ersetzt ihre gemeinsame Gestaltung.

Dieses Dokument verdichtet die Inhalte nach Themen. Ähnliche Empfehlungen werden zusammengeführt, ihre Voraussetzungen und Gegenpositionen bleiben erhalten. Das Quellenregister am Ende hält auch Beiträge fest, deren übertragbarer Inhalt klein ist oder die überwiegend eine Produktankündigung, ein Benchmark-Snapshot oder eine Zukunftsthese liefern. Ihre Aufnahme bedeutet keine Empfehlung zur Installation oder Einführung.

### Wie Aussagen zu lesen sind

Vier Nachweisarten werden unterschieden:

| Nachweisart | Was daraus folgt | Was daraus nicht folgt |
|---|---|---|
| Meinung, Prompt oder Erfahrungsbericht | Eine Person schlägt eine Methode vor oder beschreibt einen eigenen Einsatz | Allgemeine Wirksamkeit, optimale Schwellen oder verlässliche Wiederholbarkeit |
| Dokumentierte Funktion | README, Skill oder Anleitung beschreibt einen konkreten Mechanismus | Dass er im eigenen Harness verfügbar ist oder zuverlässig ausgeführt wird |
| Statisch geprüfte Umsetzung | Gelesene Dateien belegen die untersuchte Struktur oder Implementierung am lokalen Stand | Ein erfolgreicher Lauf oder ein sicherer Betrieb unter allen Bedingungen |
| Ausgeführter Versuch mit Ergebnissen | Die dokumentierten Bedingungen und Fälle wurden tatsächlich geprüft | Übertragbarkeit auf andere Aufgaben, Modelle, Daten oder Umgebungen |

Die im Knowledge-System verwendete Kennzeichnung `verifiziert` kann bereits einen statischen Repo-Abgleich meinen. Sie wird deshalb hier nicht als pauschales Gütesiegel für Produktivität, Sicherheit oder Produktionsreife behandelt. Mehrere Darstellungen desselben Herstellerberichts sind eine Herkunft, auch wenn sie von verschiedenen Creatorn kommentiert werden. Nennungshäufigkeit, Unabhängigkeit der Belege und tatsächliche Wirkung sind drei verschiedene Größen.

Preise, Modellnamen, Limits, Benchmarks, Installationswege und Versionsangaben gehören zum Datum der jeweiligen Quelle beziehungsweise zum gelesenen Checkout. Die Synthese bewahrt die daraus ableitbare Entscheidungsmethode. Für einen späteren Einsatz müssen veränderliche Produktdetails erneut geprüft werden.

## 2. Das Grundmodell: Modell, Harness, Kontext und Umgebung

Ein Sprachmodell erzeugt Ausgaben aus den ihm verfügbaren Eingaben. Zum handelnden Agenten wird das konfigurierte Gesamtsystem aus Modell, Anweisungen, Werkzeugen, Kontextverwaltung und Ausführungsschleife. Diese umgebende Software wird als Harness bezeichnet. Sie stellt Werkzeuge bereit, verarbeitet deren Aufrufe, liefert Ergebnisse zurück und verwaltet den Sitzungszustand.

Die Umgebung umfasst die tatsächlich erreichbaren Dateien, Prozesse, Browser, Datenbanken und Dienste. Ein Werkzeugergebnis ist eine Beobachtung dieser Umgebung zu einem bestimmten Zeitpunkt. Ändert sich danach eine Datei, ein Deployment oder eine Konfiguration, kann der Agent weiter mit einem veralteten Abbild arbeiten. Er muss die relevante Stelle erneut lesen oder prüfen.

Diese Trennung macht Fehlerdiagnosen präziser. Ein falsches Ergebnis kann durch fehlende Information, eine ungeeignete Schnittstelle, unzureichende Modellfähigkeit, unpassenden Denkaufwand, einen fehlerhaften Tool-Aufruf oder eine geänderte Umgebung entstehen. „Die KI ist schlecht“ erklärt diese Unterschiede nicht. Ein Modellwechsel behebt beispielsweise keine fehlende Datenbankverbindung und keine widersprüchliche Anforderung.

Auch „Gedächtnis“ bezeichnet verschiedene Dinge. Die Modellgewichte enthalten erlernte Fähigkeiten und Wissen; eine gewöhnliche Korrektur im Chat verändert diese Gewichte nicht. Die aktuelle Sitzung hält Arbeitsinformationen bereit. Ein Memory-System speichert ausgewählte Informationen außerhalb der Sitzung und macht sie später wieder zugänglich. Das kann Kontinuität herstellen, zugleich aber alte oder falsch verdichtete Annahmen weitertragen.

Das AI Coding Dictionary liefert hierfür ein nützliches gemeinsames Vokabular. Seine didaktischen Vereinfachungen sind keine allgemeine technische Spezifikation: Aussagen über feste Kontextgrenzen, ausschließlich einstufige Subagents, vollständige Isolation durch eine VM oder bestimmte Preisverhältnisse müssen auf ihren konkreten Geltungsbereich begrenzt werden. Für die praktische Arbeit zählt, welche Fähigkeiten und Grenzen der eingesetzte Harness tatsächlich besitzt.

**Grundlage:** [CONTEXT-Glossar](../80_Knowledge/Patterns/CONTEXT-Glossar.md), [Action-Space-Design](../80_Knowledge/Patterns/Action-Space-Design-nach-Modellfaehigkeit.md), [AI Coding Dictionary](../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/00-index.md).

## 3. Vom Ziel zum belastbaren Auftrag

### Ergebnis, Zweck und Grenzen zuerst klären

Ein Auftrag braucht ein Ergebnis, das sich beurteilen lässt. „Baue eine moderne App“ lässt Zielgruppe, Nutzen, Daten und Erfolg offen. Ein brauchbarer Brief erklärt, für wen die Anwendung gedacht ist, welche Aufgabe sie erleichtert, welche Abläufe dazugehören und welche ausdrücklich außerhalb des Umfangs liegen. Bei einer Änderung im Bestand kommen vorhandenes Verhalten, betroffene Verbraucher und Kompatibilitätsanforderungen hinzu.

Eine kompakte Auftragsbeschreibung enthält:

1. Problem und gewünschte Wirkung.
2. Nutzer, Daten und relevante bestehende Systeme.
3. Erwartetes Verhalten einschließlich wichtiger Fehler- und Grenzfälle.
4. Nicht-Ziele und unveränderliche Randbedingungen.
5. Beobachtbare Akzeptanzkriterien und passende Nachweise.
6. Erlaubte Aktionen, notwendige Entscheidungen sowie Zeit- und Kostenrahmen.

Das ist ein anpassbares Arbeitsformat, kein verpflichtendes Sechs-Dateien-System. Bei einer kleinen eindeutigen Änderung reichen wenige Sätze. Bei einem großen Vorhaben können daraus PRD, technische Spezifikation und einzelne Tickets entstehen.

### Grilling, Recherche und Prototyp beantworten unterschiedliche Fragen

Grilling entwickelt das gemeinsame Verständnis durch gezielte Rückfragen. Die wertvollste Frage ist häufig diejenige mit der größten fachlichen oder architektonischen Folgewirkung. Bereits im Code, in Dokumenten oder in der Unterhaltung beantwortete Fragen sollen vorher geklärt werden, damit das Interview keine Wiederholung bekannter Informationen wird.

Nicht jede Unsicherheit lässt sich im Gespräch lösen. Eine technische Behauptung braucht Recherche oder einen begrenzten Versuch. Eine Gestaltungsfrage kann einen klickbaren Prototyp benötigen. Eine fachliche Entscheidung verlangt die zuständige Person. Die sinnvolle Folge lautet daher nicht immer „erst alles fragen, dann alles planen“, sondern: die nächste entscheidende Unklarheit erkennen und die passende Untersuchungsform wählen.

Ein Blind-Spot-Pass fragt ausdrücklich nach nicht betrachteten Randfällen, Abhängigkeiten und Wissenslücken. Er hilft gegen die Neigung, plausible Annahmen als vollständige Anforderungen zu präsentieren. Er liefert jedoch selbst nur Kandidaten. Auch ein langes Interview und ein überzeugender Plan können relevante Fragen übersehen.

### Intent ergänzt Information um Prioritäten

Context Engineering stellt Informationen bereit. Intent Engineering beschreibt zusätzlich, welche Ziele führen und wie Zielkonflikte entschieden werden: Geschwindigkeit gegen Wartbarkeit, Kosten gegen Fehlerrisiko, Conversion gegen verständliche Nutzerentscheidung. Eine Unternehmensmission oder ein Rollenname ist dafür zu allgemein. Der Agent braucht konkrete Grenzen, Eskalationsanlässe und eine klare Aussage darüber, welche Entscheidung beim Menschen bleibt.

Der Ambitionscheck ergänzt drei Fragen: Ermöglicht das angeforderte Artefakt die eigentlich nötige Entscheidung? Ist die Untersuchung tief genug, etwa mit Originaldaten und Gegenproben? Fehlt eine fachliche Perspektive, die einen relevanten Fehler erkennen könnte? Mehr Ambition braucht zugleich einen begrenzten Untersuchungsauftrag; sie rechtfertigt weder endlose Recherche noch zusätzliche Handlungsrechte.

**Grundlage:** [Spec-Grilling](../80_Knowledge/Patterns/Spec-Grilling.md), [Unknowns vor Prompt-Qualität](../80_Knowledge/Patterns/Fable-Unknowns-vor-Prompt-Qualitaet.md), [Intent Engineering](../80_Knowledge/Patterns/Intent-Engineering-als-dritte-Schicht.md), [Ambitionscheck](../80_Knowledge/Patterns/Ambitionscheck-mit-Zielhoehe-Tiefe-und-Reichweite.md).

## 4. Planung, Spezifikation und Aufgabensteuerung

### Exploration und Lieferung haben unterschiedliche Zustände

Bei offenen Vorhaben ist der Weg noch unbekannt. Eine Untersuchungskarte wie Wayfinder hält Entscheidungen, Recherchefragen, Prototypen und ihre Abhängigkeiten fest. Ein Untersuchungsticket beantwortet eine Frage, die weitere Planung ermöglicht. Ein Implementierungsticket liefert dagegen ein abgegrenztes Stück Verhalten. Diese Aufgabenarten zu vermischen erzeugt scheinbar erledigte Tickets, obwohl das Produkt noch nicht geliefert wurde.

Eine mögliche Kombination ist: offene Fragen iterativ untersuchen; sobald der Weg ausreichend klar ist, die Ergebnisse in Spezifikation und ausführbare Tickets überführen. Das verbindet flexible Exploration mit nachvollziehbarer Umsetzung. Ein von Anfang an klares Vorhaben braucht keine zusätzliche Untersuchungskarte.

### Ein Plan ist eine überprüfbare Hypothese

Vor einer größeren Änderung werden relevante Codepfade, Schnittstellen, Tests und Abhängigkeiten gelesen. Der Plan benennt betroffene Flächen, Reihenfolge, Risiken und Prüfungen. Besonders folgenreiche Entscheidungen — Datenmodell, öffentliche Schnittstelle, Integrationsgrenze — verdienen frühe Aufmerksamkeit. Mechanische Umbauten können danach folgen.

Ein dauerhaft gespeicherter Plan lässt sich kommentieren und an eine neue Sitzung übergeben. Der Nutzen entsteht durch seine konkreten Entscheidungen und den Abgleich mit der Umsetzung. Zusätzliche Dokumente oder viele Planrunden sind für sich kein Qualitätsnachweis. Sobald neue Erkenntnisse den Ansatz widerlegen, wird der Plan angepasst und die Abweichung sichtbar gemacht.

Manche Quellen bevorzugen dauerhaft gepflegte Feature-Ordner mit Design, Fortschritt, Entscheidungen, Prompts und späteren Aufgaben. Andere legen Specs in abschließbare Tracker-Issues und erhalten im Repo vor allem Architekturentscheidungen. Wieder andere betrachten eine umgesetzte Spezifikation als entbehrlich. Der gemeinsame Bedarf besteht darin, geltende Anforderungen, Entscheidungsgründe und offene Arbeit auffindbar zu halten. Die Ablageform ist ein Trade-off aus Wiederverwendung und Pflegeaufwand.

### Aufgaben brauchen eine sinnvolle Größe und echte Abhängigkeiten

Ein Ticket sollte ohne Kenntnis des bisherigen Chats verständlich sein. Es nennt Ziel, Akzeptanzkriterien, relevante Pfade und Voraussetzungen. Zu große Tickets überlasten Kontext und Review; zu kleine vervielfachen Einrichtung und Koordination. Eine universelle Dateizahl oder Tokenzahl gibt es dafür im Bestand nicht.

Explizite Abhängigkeiten verhindern den Beginn vor einer benötigten Schemaänderung, Entscheidung oder Schnittstelle. Eine eingetragene Zuständigkeit startet noch keinen Agenten. Ein als erledigt markiertes Ticket ersetzt keine Abnahme. Für Integration und maßgeblichen Aufgabenstatus sollte jeweils ein klarer Eigentümer feststehen.

**Grundlage:** [Task-basierte Steuerung](../80_Knowledge/Patterns/Task-basierte-Steuerung.md), [blockierende Abhängigkeiten](../80_Knowledge/Patterns/Blockierende-Task-Abhaengigkeiten.md), [Plan und Review](../80_Knowledge/Patterns/Plan-first-mit-getrenntem-Review.md), [Spec-Ordner](../80_Knowledge/Patterns/Spec-Ordner-pro-Feature.md).

## 5. Kontext gezielt aufbauen und über Sitzungen erhalten

### Relevanz ist wichtiger als die Menge geladener Dateien

Ein großes Kontextfenster schafft Platz, garantiert aber weder Aufmerksamkeit noch richtige Schlussfolgerungen. Sachfremde Regeln, wiederholte Suchausgaben, alte Fehlversuche und lange Logs können die eigentliche Aufgabe überdecken. Umgekehrt ist ein kurzer Kontext unzureichend, wenn eine entscheidende Typdefinition oder Fachregel fehlt.

Vor zusätzlicher Information sollte deshalb das Fehlerbild geklärt werden:

| Beobachtung | Naheliegende Untersuchung |
|---|---|
| Der Agent kennt eine notwendige Information nicht | Zuständige Datei oder Primärdokumentation gezielt laden |
| Er widerspricht bereits gelesenen Vorgaben | Konflikte, irrelevanten Kontext und erforderliche erneute Orientierung prüfen |
| Er beschreibt einen früheren Dateistand | Aktuelle Datei oder Laufzeit erneut lesen |
| Er wiederholt denselben falschen Ansatz | Annahmen und Ansatz neu prüfen; gegebenenfalls mit bereinigtem Kontext fortsetzen |
| Die nächste Aufgabe ist weitgehend unabhängig | Neuen Arbeitskontext mit den erforderlichen Übergabeinformationen erwägen |

Die Quellen nennen viele Degradierungsschwellen, die stark voneinander abweichen. Sie werden hier nicht zu einer verbindlichen Prozentregel vereinheitlicht. Auch vereinfachte quadratische Kostenformeln beschreiben nicht unmittelbar die Rechnung oder das Nutzungslimit eines konkreten Produkts.

### Progressive Disclosure braucht brauchbare Wegweiser

Die ständig geladene Agent-Datei enthält universell geltende Besonderheiten, wichtige Grenzen und klare Einstiegspunkte. Details werden nach Anlass geladen. Ein hilfreicher Verweis nennt sowohl den stabilen Pfad als auch den Auslöser: „Bei Schemaänderungen die Migrationsregeln lesen“ ist nützlicher als eine unkommentierte Linkliste.

AGENTS.md sollte Informationen ergänzen, die sich nicht zuverlässig aus dem Code erschließen lassen. Mechanisch prüfbare Konventionen gehören möglichst in vorhandene Typprüfung, Linting oder Tests. Das bedeutet nicht, wichtige Freigabe- oder Sicherheitsvorgaben zugunsten kürzerer Prompts zu entfernen. Die Aufgabe jeder Regel und ihre tatsächliche Durchsetzung bleiben zu prüfen.

Eine Source-Datei erklärt, was eine Quelle behauptet. Ein Pattern bündelt eine wiederkehrende Arbeitsweise. Ein Glossar erklärt die geltende Domänensprache. Ein Laufprotokoll hält ein konkretes Ereignis fest. Diese Informationsarten haben unterschiedliche Lebensdauer und sollten nicht als gleichwertige aktuelle Wahrheit behandelt werden.

### Handoff und Compaction erhalten unterschiedliche Ausschnitte

Ein guter Handoff nennt den aktuellen Auftrag, Entscheidungen mit Gründen, konkrete Artefakte, ausgeführte Prüfungen, offene Arbeit und geltende Grenzen. Er verweist auf Code, Tests und Originalbelege, statt alles zu duplizieren. Die nächste Sitzung prüft wichtige Aussagen am aktuellen Zustand nach.

Compaction verdichtet einen Gesprächsverlauf. Was dabei entfällt, kann später relevant werden; auch falsche Annahmen können erhalten bleiben. Ein gespeicherter Plan und ein Ergebnisjournal helfen, diese Verdichtung zu kontrollieren. Frischer Kontext ist wiederum nur dann hilfreich, wenn die notwendigen Informationen gezielt wieder eingebracht werden.

Im Bestand stehen lange warme Sessions mit gut gepflegtem Plan gegen häufige Neustarts und frische Kontexte pro Phase. Beide können unter ihren Voraussetzungen sinnvoll sein. Cache-Wiederverwendung, Informationsverlust, Wiederanlaufaufwand und Ergebnisqualität müssen gemeinsam betrachtet werden.

**Grundlage:** [Kontext-Hygiene](../80_Knowledge/Patterns/Kontext-Hygiene-Entscheidungsbaum.md), [AGENTS.md-Onboarding](../80_Knowledge/Patterns/AGENTS-md-Onboarding-Design.md), [Handoff](../80_Knowledge/Patterns/Handoff-Doc.md), [Wissenspflege](../80_Knowledge/Patterns/Wissenspflege-mit-Inbox-und-Review.md).

## 6. Eine Codebasis für Agenten verständlich machen

### Erst den tatsächlichen Ablauf nachvollziehen

Bei einer unbekannten Funktion wird der Weg vom Eingang über Validierung und Fachlogik bis zur Persistenz und den Verbrauchern verfolgt. Jede wichtige Verbindung bekommt einen konkreten Dateibezug. Dynamische Aufrufer, generierte Clients, Konfigurationen und Betriebssignale können eine rein statische Suche ergänzen. Ein fehlender Suchtreffer beweist keine fehlende Nutzung.

Für wiederkehrendes Onboarding kann eine Architekturkarte helfen. Getrennte Perspektiven — Systemstruktur, Request-Lifecycle, Datenfluss, externe Integrationen — beantworten verschiedene Fragen. Sinnvolle Detailansichten führen vom Überblick zu konkreten Pfaden. Eine syntaktisch korrekte Mermaid-Kante belegt jedoch keinen realen Datenfluss. Diagramme brauchen fachliche Gegenprüfung und einen Anlass zur Aktualisierung.

### Kleine Schnittstellen können viel Verhalten bündeln

Deep Modules verbergen relevante Komplexität hinter einer verständlichen Schnittstelle. Der Deletion-Test fragt gedanklich, ob das Entfernen eines Moduls Komplexität beseitigt oder lediglich auf viele Aufrufer verteilt. Eine Durchreichung kann entbehrlich sein; ein zentraler Vertrag für fachliches Verhalten kann sehr wertvoll sein. Die Zahl der Dateien und Zeilen entscheidet das nicht.

Vor einer Featureänderung sollten mehrere Implementierungen derselben Fachregel erkannt werden. Unterschiedliche Resultate verlangen zuerst eine fachliche Entscheidung. Erst danach folgt eine verhaltensbewahrende Konsolidierung. Ähnlich aussehender Code kann in verschiedenen Kontexten berechtigt unterschiedliche Regeln enthalten.

Wiederkehrende Fehler lassen sich häufig strukturell begrenzen: starke Typen, sinnvolle APIs, eindeutige Besitzverhältnisse und Invarianten machen falsche Zustände schwerer darstellbar. Ein verständlicher Helper plus eine Lint-Regel mit konkretem Ersatzweg kann effektiver sein als ein weiteres Verbot im Prompt. Er muss aber wirklich benötigt werden und in einem verbindlich ausgeführten Check liegen.

### Schema, Dokumentation und Quellcode ergänzen einander

Eine gemeinsame maschinenlesbare Schemaquelle kann Validatoren, Typen, Spezifikationen und Clients verbinden. CI prüft generierte Artefakte und betroffene Verbraucher. Ein erfolgreicher Compile-Lauf sichert strukturelle Verträge im geprüften Bereich; er beweist keine vollständige Fachsemantik und keine Kompatibilität unabhängig ausgelieferter Versionen.

Versionspassender Framework-Quellcode liefert idiomatische Beispiele, wenn Dokumentation eine Frage offenlässt. Öffentliche API und interne Implementierung bleiben getrennt. Aktuelle Dokumentation kann über Context7 oder direkte Primärquellen erschlossen werden; Abruf allein bestätigt weder ihre Passung noch eine korrekte Umsetzung.

**Grundlage:** [Codepfad](../80_Knowledge/Patterns/Codepfad-vor-Aenderung-nachvollziehen.md), [Architekturperspektiven](../80_Knowledge/Patterns/Architektur-in-Perspektiven-dokumentieren.md), [Abstraktionswert](../80_Knowledge/Patterns/Abstraktionswert-mit-Deletion-Test-pruefen.md), [Fachregeln](../80_Knowledge/Patterns/Fachregel-Konsolidierung-vor-Featureaenderung.md), [Schema-Vertrag](../80_Knowledge/Patterns/Schema-als-Vertrag-mit-generierten-Clients.md).

## 7. Skills, Hooks, Tools und Plugins passend einsetzen

### Verantwortung und Aufrufrecht sind verschiedene Achsen

| Baustein | Hauptaufgabe | Typischer Fehler |
|---|---|---|
| Agent-Datei | Dauerhafte Projektbesonderheiten und Routing | Vollständige Spezialhandbücher immer laden |
| Skill | Wiederholbare fachliche Arbeitsweise mit Referenzen | Einen vagen Prompt als fertige Fähigkeit behandeln |
| Subagent | Abgegrenzte Arbeit in eigenem Kontext | Eng gekoppelte Schritte mit verlustreichen Übergaben zerlegen |
| Hook oder Check | Ereignisbezogene Ausführung und überprüfbare Bedingungen | Erinnerung, Warnung und harte Sperre gleichsetzen |
| Tool, CLI oder MCP | Konkreter Datenzugriff oder ausführbare Aktion | Schnittstelle mit fachlicher Freigabe verwechseln |
| Plugin oder Installer | Komponenten verpacken und verteilen | Installation als Qualitäts- und Vertrauensnachweis verstehen |

Zusätzlich wird entschieden, welche Abläufe ausschließlich auf ausdrücklichen Aufruf starten und welche das Modell bei passenden Aufgaben auswählen darf. Eine begrenzte Aufrufhierarchie verhindert unnötig tiefe Orchestrierung. Ihre konkrete technische Unterstützung hängt vom Harness ab; Metadaten und Namenskonventionen sind keine allgemeine Sicherheitsgrenze.

### Ein Skill sollte einen beobachteten Bedarf lösen

Gute Kandidaten sind wiederkehrende Aufgaben mit speziellem Fachwissen, konsistenten Kriterien und aufwendiger erneuter Erklärung. Eine genaue Tageshäufigkeit ist kein empirisch belegter Schwellenwert. Der Skill braucht einen Pflegeverantwortlichen und ein klar benanntes Ergebnis.

Die Beschreibung erklärt, was der Skill tut und wann er passt. Der Haupttext enthält die wesentlichen Schritte und Grenzen; längere Fachreferenzen und wiederkehrende Hilfslogik werden gezielt nachgeladen. Zu breite Skills laden unnötiges Wissen, zu enge zerlegen eine zusammenhängende Aufgabe in eine Suchkette.

Eine gelungene gemeinsame Aufgabe, ein Screenshot oder eine Bildschirmaufnahme kann als Ausgangspunkt für einen Skill dienen. Aus einem einzelnen Beispiel dürfen seine zufälligen Annahmen nicht zu allgemeinen Regeln werden. Gute und schlechte Beispiele sowie nachvollziehbare Ausnahmen helfen, den tatsächlichen Anwendungsbereich zu prüfen.

### Aktivierung, Befolgung und Nutzen getrennt messen

Ein Skill kann korrekt installiert sein und trotzdem nie ausgewählt werden. Er kann geladen werden, während zentrale Schritte ausbleiben. Er kann alle Schritte ausführen, ohne das Ergebnis zu verbessern. Deshalb braucht die Evaluation drei getrennte Fragen: Wird er bei passenden Aufgaben aktiviert? Wird sein Vertrag eingehalten? Verbessert er gegenüber einer Baseline Qualität, Zeit oder Gesamtkosten?

Should-trigger- und should-not-trigger-Fälle prüfen die Auswahl. Wiederholte vergleichbare Aufgaben mit und ohne Skill prüfen den Leistungsbeitrag. Offene Aufgaben wie Grilling brauchen fachliche Rubriken; zwei unterschiedlich formulierte Antworten lassen sich nicht allein über Textähnlichkeit bewerten. SkillEvaluator, Skill-Creator-Verfahren und die Eval-Systeme größerer Packs liefern unterschiedliche Bausteine hierfür.

Anti-Rationalization-Tabellen halten bekannte Ausreden und ihre Gegenargumente fest. Sie können einen Workflow verständlicher und schwerer zu überspringen machen. Sie erzwingen seine Befolgung nicht. Ebenso kann ein Hook zuverlässig eine Erinnerung einblenden, ohne damit die tatsächliche Skill-Anwendung zu garantieren.

### Technische Automatisierung klein und prüfbar halten

Deterministisch formulierbare Bedingungen gehören vorzugsweise in einfache Checks. Semantische Entscheidungen können zusätzliches Modellurteil benötigen. Ein Script kann selbst Tests starten und deren Ergebnis auswerten; dafür ist kein Agent-Hook erforderlich. Die Art der Entscheidung und der Zeitpunkt des Feedbacks sind getrennte Entwurfsfragen.

Bei vielen Tools können dynamische Tool-Suche und programmatisches Aufrufen den Kontext entlasten. Ergebnisfilterung verhindert, dass ein großer JSON-Dump vollständig im Modellkontext landet. Dafür entstehen neue Pflichten bei Parameterwahl, Fehlerbehandlung, Timeout, Berechtigungen und Nachvollziehbarkeit. Für wenige passende Tools kann direkte Nutzung einfacher sein.

**Grundlage:** [Erweiterungsebenen](../80_Knowledge/Patterns/Erweiterungs-Ebenen-Zuordnung.md), [Skill-Hierarchie](../80_Knowledge/Patterns/Skill-Call-Hierarchie.md), [Trigger und Baseline-Evals](../80_Knowledge/Patterns/Skill-Qualitaet-durch-Trigger-und-Baseline-Evals.md), [Hook-Entscheidung](../80_Knowledge/Patterns/Hook-Entscheidungstyp-nach-Pruefbarkeit.md), [MCP Code Execution](../80_Knowledge/Patterns/MCP-Code-Execution-statt-Tool-Definitionen.md).

## 8. Parallelität, Agententeams und Übergaben

Parallelität ist sinnvoll, wenn die Arbeit unabhängige Flächen besitzt, die Aufträge selbsttragend sind und jeder Teil ein prüfbares Ergebnis liefern kann. Sie spart nicht automatisch Tokens. Jeder Agent benötigt Kontext, produziert Ergebnisse und verursacht Konsolidierungsarbeit.

Für Codeänderungen werden Dateien, Module oder Worktrees eindeutig zugeordnet. Ein Worktree trennt Dateistände, aber keine Ports, Datenbanken oder logischen Schnittstellen. Semantische Konflikte können erst beim Zusammenführen sichtbar werden. Geteilte Browser und andere zustandsabhängige Oberflächen brauchen ebenfalls klare Zuständigkeit.

Bei gleichartigen Quellenanalysen lässt sich nach Dokumenten oder Quellenfamilien aufteilen. Gemeinsame unveränderliche Regeln gehören einmal vollständig in den Auftrag. Repo-weite Scans werden zentral ausgeführt. Der Abschlussbericht eines Workers sollte fertig formulierte Befunde, Herkunft, Grenzen und offene Punkte enthalten, damit die Konsolidierung nicht erneut alle Eingänge lesen muss.

Bei eng gekoppelten Spezialisten kann das Gegenteil richtig sein: Ein gemeinsamer Hauptloop mit bedarfsweise geladenen Skills vermeidet Informationsverluste und wiederholte Übergaben. Die passende Grenze richtet sich danach, welche Informationen gemeinsam gebraucht werden — nicht allein danach, ob die Rollen „Researcher“, „Planner“ und „Builder“ heißen.

Ein unabhängiger Reviewer soll Anforderungen, relevante Standards und das Ergebnis prüfen können. Ein frischer Kontext reduziert die Übernahme der bisherigen Begründung, schafft aber keine vollständige Unabhängigkeit von Modellschwächen oder gemeinsamen falschen Annahmen. Rollenvielfalt und Mehranbieter-Routing sind deshalb mögliche Perspektivhilfen, kein Ersatz für belastbare Evidenz.

Ein Advisor während eines langen Laufs verfolgt eine engere Aufgabe: Ziel und Constraints beobachten und bei Drift eingreifen. Sein Nutzen hängt von der Eingriffsschwelle und den beobachtbaren Daten ab. Für kurze Aufgaben kann der Zusatzaufwand überwiegen.

**Grundlage:** [kontrollierte Parallelisierung](../80_Knowledge/Patterns/Kontrollierte-Agent-Parallelisierung.md), [Advisor gegen Drift](../80_Knowledge/Patterns/Advisor-Agent-gegen-Drift.md), [Handoff](../80_Knowledge/Patterns/Handoff-Doc.md).

## 9. Verifikation: Fortschritt belegen und den Prüfer mitprüfen

### Vier verschiedene Fragen benötigen verschiedene Nachweise

Ein Build prüft, ob das Projekt im gewählten Setup gebaut werden kann. Ein Verhaltenstest prüft definierte Erwartungen für konkrete Fälle. Ein Review beurteilt zusätzliche Zusammenhänge und mögliche Lücken. Eine Abnahme entscheidet, ob das Ergebnis für den vorgesehenen Einsatz genügt. Keine dieser Aussagen sollte durch eine andere ersetzt werden.

Die Review-Trennung nach Spezifikation und Standards ist besonders hilfreich. Die erste Achse fragt, ob das beauftragte Verhalten vollständig und richtig umgesetzt wurde. Die zweite prüft dokumentierte Architektur-, Sicherheits- und Qualitätsanforderungen. Beide brauchen konkrete Fundstellen. Eine stilistische Vorliebe ist kein Bug; ein plausibler Verdacht ist noch kein reproduzierter Fehler.

Ein aussagekräftiger Befund nennt Auslöser, betroffene Stelle, tatsächliches Verhalten, erwartetes Verhalten, Folgen und einen nachvollziehbaren Prüfweg. Fehlende Zugänge oder nicht ausgeführte Fälle werden als offen ausgewiesen. Ein Bericht mit vielen Findings ist nicht automatisch besser: erzwungenes Weitersuchen kann harmlose Stellen zu Problemen erklären.

### TDD schafft eine kurze Rückkopplung

Bei klar prüfbarem Verhalten lautet das vertikale Muster: einen relevanten fehlschlagenden Fall herstellen, den kleinsten passenden Code ergänzen, erneut prüfen und anschließend strukturieren. Tests sollten beobachtbares Verhalten an stabilen Schnittstellen absichern. Ein Test, der lediglich den Quelltext nach dem erwarteten String durchsucht oder sämtliche relevante Logik wegmockt, kann einen Scheinerfolg erzeugen.

Das beobachtete Red ist selbst zu beurteilen. Ein Syntaxfehler, eine falsche Umgebung oder eine fehlende Abhängigkeit belegt nicht, dass der Test die beabsichtigte Regression erkennt. Eine behauptete Mutation muss tatsächlich angewendet worden sein. Tests an wichtigen Stellen werden zusätzlich mit absichtlich fehlerhaften Gegenproben geprüft.

Bei explorativer Gestaltung gibt es nicht immer vorab einen sinnvollen automatisierten Test. Dann beantworten Prototyp, gerenderte Vorschau und fachliches Urteil zunächst die offene Frage. Nach Stabilisierung des Verhaltens können passende Regressionstests hinzukommen. Der Bestand begründet damit keine Pflicht, für jede reversible Text- oder Farbänderung neue Tests zu schreiben.

### Ein grüner Harness hat einen begrenzten Aussagebereich

Autonome Arbeit benötigt verwertbare Rückmeldung: erwartete und tatsächliche Werte, konkrete Pfade, reproduzierbare Befehle und aussagekräftige Fehler. Ein großer undurchsichtiger Build-Fehler kann alle Worker gleichzeitig blockieren. Ein Referenzsystem oder Oracle hilft, einzelne Fälle abzugrenzen und unabhängig zu bearbeiten.

Auch ein vorhandener Prüfer kann falsch sein. Im Bestand stehen Berichte über Vergleichswerkzeuge, die fehlerhafte Ergebnisse akzeptierten, sowie über eine Migration mit grünen Tests und später gefundenen Regressionen. Daraus folgt ein eigener Prüfauftrag für den Verifier: erkennt er einen bekannten Fehler, akzeptiert er einen korrekten Kontrollfall, und repräsentieren seine Fälle den vorgesehenen Betrieb?

Mutationstests verändern Quellcode kontrolliert und untersuchen, welche Veränderungen die Tests erkennen. Überlebende Mutanten sind Kandidaten für fehlende oder schwache Prüfungen. Sie müssen auf fachliche Relevanz untersucht werden. Ein höherer Mutationsscore ist kein unabhängiger Nachweis eines besseren Produkts.

Formale Verifikation geht für eine ausdrücklich formulierte Eigenschaft weiter als endlich viele ausgeführte Tests. Ein unabhängiger Checker prüft ein Beweisartefakt unter einem festgelegten Ausführungsmodell. Die Grenze bleibt die Spezifikation: Eine unvollständige Eigenschaft kann korrekt bewiesen sein. Ein Patch kann den Beweis erleichtern, indem er erwünschtes Verhalten entfernt. Fachliches Spezifikationsreview, Umgebungsannahmen und Abnahme bleiben deshalb eigenständige Aufgaben.

### Feedback an der passenden Stelle geben

Kurze Checks können Fehler früh lokalisieren. Umfangreiche Prüfungen nach jedem einzelnen Edit können bei zusammenhängenden Umbauten wiederholt denselben bewusst inkonsistenten Zwischenstand melden. Sinnvoll ist eine Staffelung nach Signal, Dauer und Fehlerfolge: gezieltes lokales Feedback, zusammenhängende Prüfung einer Änderung und die erforderlichen Integrationschecks vor einem Merge.

Notwendige Prüfungen müssen an einem verlässlichen Ausführungsort liegen. Ein umgehbarer lokaler Hook genügt nicht für eine verbindliche Integrationsregel. Eine nach Wiederholung grüne Suite darf einen zuvor fehlgeschlagenen Lauf nicht aus der Historie verschwinden lassen; Flakiness ist ein eigener Befund.

### Agent-Evals prüfen das Arbeitssystem

Anwendungstests prüfen Softwareverhalten. Agent-Evals prüfen dagegen, wie gut ein bestimmtes Modell mit Prompt, Skills, Tools, Kontext und Rechten Aufgaben bearbeitet. Repräsentative historische Tickets, echte Fehler und fachlich begründete Grenzfälle sind wertvoller als ausschließlich künstliche Aufgaben, die auf heutige Modellschwächen zugeschnitten sind.

Vor einer Optimierung wird der Grader geprüft. Wo eine mechanische Assertion genügt, ist sie günstiger und nachvollziehbarer als ein freies Modellurteil. LLM-Judges brauchen Rubriken, menschlich gegengeprüfte Beispiele und eine Betrachtung ihrer Varianz. Ein einzelner erfolgreicher Lauf genügt bei nichtdeterministischen Agenten nicht.

Train-, Validierungs- und Testfälle müssen nach ihrem Zweck getrennt werden. Ein während jeder Optimierungsrunde zur Variantenauswahl genutzter Holdout übernimmt faktisch eine Validierungsfunktion. Für eine belastbarere Abschlussaussage wird ein zusätzlicher unangetasteter Testsatz benötigt. Kleine Fallzahlen, wechselnde Aufgaben und gleichzeitig geänderte Modellparameter begrenzen die Zurechenbarkeit.

**Grundlage:** [TDD](../80_Knowledge/Patterns/TDD-als-Verifikationshebel.md), [Testharness](../80_Knowledge/Patterns/Testharness-als-staerkster-Hebel.md), [Mutationstests](../80_Knowledge/Patterns/Mutationstests-fuer-Agent-geschriebene-Tests.md), [formale Verifikation](../80_Knowledge/Patterns/Formale-Verifikation-mit-unabhaengigem-Proof-Checker.md), [Hillclimbing](../80_Knowledge/Patterns/Hillclimbing-mit-Holdout-Split.md), [Feedbackzeitpunkt](../80_Knowledge/Patterns/Pruefungen-nach-Feedbackzeitpunkt-staffeln.md).

## 10. Autonomie, Sicherheit und menschliche Verantwortung

### Zustimmung, Erreichbarkeit und Abnahme getrennt gestalten

Die Freigabeschicht entscheidet, ob eine konkrete Aktion vorher bestätigt werden muss. Die technische Ausführungsgrenze bestimmt, auf welche Dateien, Prozesse, Netzwerke und Dienste sie zugreifen kann. Die fachliche Abnahme beurteilt ihr Ergebnis. Automatische Zustimmung innerhalb einer begrenzten Umgebung ist etwas anderes als unbeschränkter Zugriff.

Ein Prompt mit „lies keine Secrets“ ist eine Anweisung, keine technische Sperre. Auch eine Deny-Liste oder ein Hook muss alle relevanten Wege abdecken: direkte Dateioperationen, Shell und Unterprozesse, Suche, Testausgaben, Netzwerk und indirekt erreichte Dienste. Secret-Schutz für ein Read-Tool verhindert beispielsweise nicht, dass ein Test echte Zugangsdaten ins Log schreibt.

Ein Scope sollte deshalb benötigte Identitäten, Daten und Aktionen konkret benennen. Dummy-Daten, begrenzte Testzugänge, geeignete Betriebssystemkontrollen und eine kontrollierte Netzwerkfläche können die Folgen von Fehlern begrenzen. Ein „High“-Schalter, Containername oder VM-Label ist kein eigener Nachweis der wirksamen Grenzen. Die zusammengesetzten Kontrollmechanismen und ihr Verhalten bei Ausfall müssen geprüft werden.

### Agenten können über andere Agenten handeln

Kommunikation ist Teil des Berechtigungsmodells. Ein diagnostizierender Agent mit lesenden Tools kann einen schreibberechtigten Agenten um Umsetzung bitten. Geteilte Caches, Paketdienste oder andere gemeinsam beschreibbare Ressourcen können zusätzliche Kommunikationswege bilden. Eine reine Liste direkter Tools erfasst diese Wege nicht vollständig.

Eine Nachricht eines anderen Agenten ist keine menschliche Autorisierung. Tool-Anforderung, tatsächliche Ausführung und externe Wirkung bleiben getrennt zu erfassen. Ein angekündigter Verzicht auf Tools beweist nicht, dass keine aufgerufen wurden; ein versuchter Upload beweist wiederum keinen erfolgreichen Datenabfluss. Die im Bestand dokumentierten Vorfälle und Untersuchungen sind wichtige Fallbeispiele, erlauben aber keine pauschalen Aussagen über Absicht oder Verhalten sämtlicher Modelle.

### Die Anwendung selbst braucht eigene Schutzregeln

Agentensicherheit und Anwendungssicherheit sind verschiedene Prüfgegenstände. Ein öffentliches Frontend kann keine vertraulichen Serverregeln durch versteckte Bedienelemente schützen. Authentifizierung, fachliche Autorisierung und Datenzugriff werden am tatsächlich ausführenden Backend beziehungsweise der Datenbank geprüft. Tests mit getrennten Identitäten, direkten API-Aufrufen, fremden Objekt-IDs, Quotenrennen und untrusted Eingaben können konkrete Grenzen untersuchen. Ein Security-Checker oder grüner Build belegt diese Eigenschaften nicht vollständig. Solche Versuche benötigen einen autorisierten Testbereich, begrenzte Kosten und passende Testdaten; die Analyse erteilt keine neue Befugnis für Eingriffe in produktive Systeme.

### Autonomie auf eine Arbeitsklasse begrenzen

Ein brauchbarer Autonomievertrag beschreibt zulässige Aufgaben, Voraussetzungen, erlaubte Aktionen, Ergebnisnachweise, Budget und Fehlerpfad. Er gilt für diese Arbeitsklasse unter diesen Bedingungen. Er ist kein Reifezertifikat für eine ganze Organisation.

Ein sicherer Fallback darf nicht von einer sofort verfügbaren Person abhängen. Je nach Prozess kann er bedeuten, vor weiteren Aktionen zu stoppen, einen begrenzten Ablauf zu isolieren oder einen erprobten Zustand wiederherzustellen. Dieser Weg braucht selbst passende Rechte. Ein Git-Revert macht eine bereits verschickte Nachricht, eine reale Zahlung oder verlorene Daten nicht rückgängig.

Im Monitoring kann eine deterministische Erkennung eine begrenzte Diagnose starten. Höhere Eskalationsstufen können einen PR oder ein ausdrücklich freigegebenes Runbook erlauben. Die im Material genannten Sigma-Bänder sind Beispiele; saisonale Verläufe, instabile Baselines und Fehlalarme verlangen aufgabenspezifische Regeln.

### Review-Automatik braucht eigene Kontrolle

Der Bestand enthält unterschiedliche Policies: durchgängig menschliches PR-Review, risikogewichtete Pflichtfreigaben, automatische Entscheidungen mit Stichproben und Visionen vollständig automatisierter Lieferung. Diese Ansätze sind nicht zu einem allgemein bewiesenen Standard zusammenzuführen.

Shadow Mode erlaubt, einen automatisierten Reviewer zunächst ohne Freigabemacht zu beobachten. Bekannte Fehlerfälle und saubere Kontrolländerungen prüfen sowohl übersehene Fehler als auch störende Fehlalarme. Entscheidungen werden an den tatsächlich geprüften Stand gebunden. Nach Änderungen oder neuen Commits kann eine frühere Freigabe ihre Grundlage verlieren.

Menschliche Aufsicht ist ebenfalls eine zu prüfende Leistung. Viele Bestätigungsklicks können Aufmerksamkeit verbrauchen. Hohe Zustimmung, lange Reviewdauer oder häufige Rückfragen beweisen für sich keine gute Kontrolle. Kleine verständliche Revieweinheiten, konkrete Belege und risikogerechte Vorprüfungen unterstützen ein eigenständiges Urteil.

Für dieses Repository bleiben die bestehenden Freigaberegeln maßgeblich. Die Analyse externer Arbeitsweisen ändert keine Produktions-, Kommunikations-, Lösch-, Security- oder Veröffentlichungsbefugnis.

**Grundlage:** [Freigaben und Isolation](../80_Knowledge/Patterns/Freigaben-und-Isolation-getrennt-steuern.md), [Deny-Regeln](../80_Knowledge/Patterns/Deny-Rules-statt-CLAUDE-md-Empfehlung.md), [Kommunikationsrechte](../80_Knowledge/Patterns/Agent-Rechte-umfassen-Kommunikationswege.md), [Fallback](../80_Knowledge/Patterns/Sicherer-Fallback-vor-menschlicher-Eskalation.md), [Review-Autonomie](../80_Knowledge/Patterns/Review-Autonomie-mit-Shadow-Mode-und-Stichproben.md), [menschliche Aufsicht](../80_Knowledge/Patterns/Menschliche-Aufsicht-als-eigene-Leistung-pruefen.md).

## 11. Modelle, Reasoning und Kosten wirtschaftlich wählen

### Zuerst den Engpass bestimmen

Modellfähigkeit und Reasoning-Effort sind unterschiedliche Achsen. Überspringt ein Agent notwendige Arbeit, kann mehr angemessener Aufwand helfen. Hat er alle relevanten Informationen sorgfältig untersucht und scheitert trotzdem fachlich, kann ein stärkeres oder anders geeignetes Modell nötig sein. Fehlende Eingaben, falsche Tools und unklare Ziele verlangen zuerst eine Korrektur der Arbeitsgrundlage.

Die Strategie „günstig beginnen und eskalieren“ ist bei hohem Volumen gut prüfbarer Aufgaben plausibel. Ein sofortiger Start auf einer stärkeren Konfiguration kann bei erkennbar schwierigen, kontextreichen oder folgenkritischen Aufgaben günstiger sein als ein zusätzlicher Fehlversuch. Der Bestand liefert keinen universellen Sieger. Auch ein starkes Modell mit geringerem Effort und ein kleineres Modell mit höherem Effort müssen anhand geeigneter Aufgaben verglichen werden.

Feste Rollentabellen wie „klein recherchiert, groß plant“ sind Ausgangshypothesen. Recherche kann schwierige Quellenkritik enthalten; Implementierung kann mechanisch oder hochriskant sein. Die Aufgabenanforderung entscheidet. Tatsächlich verwendetes Modell und wirksame Overrides sollten am Lauf belegt werden, statt sie aus einer Rollenbeschreibung abzuleiten.

### Die relevante Einheit ist das akzeptierte Ergebnis

Zu den Gesamtkosten gehören Modellaufrufe, Fehlversuche, Recherche, Reviews, Koordination, Infrastruktur und menschliche Nacharbeit. Ein niedriger Tokenpreis kann durch höheren Verbrauch aufgezehrt werden. Weniger Tokens können mit schlechterer Qualität einhergehen. Schnellere Ausgabe kann durch langsame Tools, Builds oder Freigaben bedeutungslos werden.

Vergleiche benötigen gleiche Aufgaben, gleiche Erfolgskriterien und dokumentierte Versionen. Ein Coding-Agent-Benchmark misst ein konfiguriertes System; ein anderer Harness, Pass@k, eine geänderte Aufgabenmenge oder ein neuer Grader verändert die Bedeutung des Scores. Punktwerte aus unterschiedlichen Indizes sind keine gemeinsame Rangliste. Zeitlich begrenzte Rabatte sind keine dauerhafte Kostenbasis.

Tokenzahlen aus lokalen Sessions sind nützliche Diagnosewerte. Sie sind ohne weitere Kenntnis weder konkrete Geldkosten noch verbrauchte Abo-Credits oder ein Anteil des aktuellen Nutzungslimits. Diese Größen benötigen ihre jeweilige Abrechnungsgrundlage.

### Cache und Kompression optimieren unterschiedliche Stellen

Prefix-Caching kann wiederverwendete Eingaben billiger machen. Geänderte Präfixe, Modellwechsel, TTL und Overrides beeinflussen die tatsächliche Wiederverwendung. Eine längere TTL kann nach einer echten Pause helfen, zugleich höhere Schreibkosten verursachen. Die passende Entscheidung verlangt gemessene Lese- und Schreibanteile bei gleichbleibender Ergebnisqualität.

RTK verdichtet vor allem Kommandoausgaben. Headroom bietet zusätzliche kontextbezogene Kompression mit Nachladepfad. Caveman umfasst unter anderem verkürzte Sprache, Eingabekompression und Routing. Diese Mechanismen haben verschiedene Wirkflächen und Datenflüsse. Byte-Reduktion ist keine vollständige Kostenmessung. Wo etwas entfernt wird, braucht der Agent bei Bedarf einen verlässlichen Weg zum Original.

### Offenheit und Betrieb getrennt beurteilen

Offene Gewichte, offene Trainingsdaten, offene Software und praktisch betreibbare Infrastruktur sind unterschiedliche Eigenschaften. Lizenz, verfügbare Artefakte, Hardware, Tool-Kompatibilität und portable Rechte bestimmen gemeinsam, was ein eigener Stack leisten kann. Der archivierte Bericht zum Stand offener KI sieht wichtige Lücken bei Harness, Betrieb, Memory und Permission-Systemen. Seine Reifegradnoten bleiben Autorenurteile; Traffic eines einzelnen Routers repräsentiert nicht den Gesamtmarkt. Eine lokal gespeicherte Wissensbasis kann weiterhin Inhalte an externe Modelle oder Tools übertragen. Vertragsgrundlage, Datenfluss und Ausführung müssen für jeden beteiligten Dienst konkret geprüft werden.

### Lokale Modelle nach der tatsächlichen Arbeitslast beurteilen

Die Dimensionierung beginnt mit benötigter Qualität und Aufgabe. Danach folgen Modell, Quantisierung, Kontextlänge und gleichzeitige Sitzungen. Gewichte, KV-Cache, Laufzeit und übriger Systembedarf gehören gemeinsam in die Speicherbetrachtung. Das erfolgreiche Laden einer Modelldatei belegt keine akzeptable Geschwindigkeit für einen kompletten Agentenlauf.

Ein repräsentativer Versuch misst Speicherpeak, Promptverarbeitung, Ausgabe, Tool-Nutzung und Ergebnisqualität. Lokales Serving kann Kontrolle erhöhen, verhindert aber nicht automatisch Netzwerkzugriffe anderer Komponenten oder Telemetrie. Provider-Umleitung verändert den Daten- und Ausführungsweg; eine kompatible API garantiert keine identische Tool- oder Modellsemantik.

Bei festem Antwortraum können Klassifikation oder Routing über Scoring statt freie Textgenerierung erfolgen. Label-Logits und trainierte Decision Heads sind verschiedene Ansätze. Eine normalisierte Wahrscheinlichkeit innerhalb einer Kandidatenmenge ist keine kalibrierte Trefferwahrscheinlichkeit. Ausweichoptionen, getrennte Testdaten und fachlich geeignete Schwellen bleiben nötig.

**Grundlage:** [Modell-Eskalation](../80_Knowledge/Patterns/Modell-Eskalation-von-guenstig-nach-teuer.md), [Cache-TTL](../80_Knowledge/Patterns/Prompt-Cache-TTL-nach-Agent-Pausen-waehlen.md), [lokale Inferenz](../80_Knowledge/Patterns/Lokale-Inferenz-nach-Arbeitslast-dimensionieren.md), [lokale Umleitung](../80_Knowledge/Patterns/Lokale-Modell-Umleitung-Muster.md), [Scoring](../80_Knowledge/Patterns/Entscheidung-per-Scoring-statt-Generierung.md), [Decision-Head-Finetuning](../80_Knowledge/Patterns/Decision-Head-Finetuning.md).

## 12. UI, Designsysteme und verständliche Interaktion

### Produktabsicht vor visueller Dekoration

Eine Oberfläche braucht einen klaren Hauptzweck, realistische Inhalte und nachvollziehbare Handlungen. Ein Designbrief hält Zielgruppe, gewünschte Nutzung, Informationshierarchie und vorhandene Markenmittel fest. Ein gemeinsames Brand Kit verbindet Farben, Schriften, Logos, Bildsprache und Beispiele über App, Website, Dokument und Video hinweg.

Eine maschinenlesbare Designbeschreibung kann diese Entscheidungen als Tokens und Regeln verfügbar machen. Die Gestaltung muss trotzdem pro Medium geprüft werden. Ein kopiertes DESIGN.md einer bekannten Marke ist keine eigene Markenstrategie und keine Garantie für passende oder aktuelle Werte.

Die Design-Repos decken unterschiedliche Aufgaben ab: UI UX Pro Max erschließt strukturierte Stile und Richtlinien; Taste und Impeccable entwickeln beziehungsweise kritisieren eine konkrete visuelle Richtung; Emil Kowalskis Skills und Make Interfaces Feel Better schärfen Interaktion und Details; shadcn und Vercel liefern komponenten- und frameworkbezogene Regeln. Diese Perspektiven ergänzen sich, sollten aber nicht als widersprüchliche globale Vorgaben gleichzeitig geladen werden.

### Varianten müssen eine Entscheidung ermöglichen

Ein sinnvoller Variantenvergleich ändert Layout, Dichte, Navigation oder Interaktionsmodell. Drei nahezu gleiche Entwürfe mit anderen Farben liefern wenig Erkenntnis. Die Varianten werden isoliert mit plausiblen Inhalten und echten relevanten Interaktionen angeboten. Erst die gewählte Richtung wird integriert und nach den Anforderungen des Produkts abgenommen.

Für begrenzten Designfeinschliff kann ein Bildentwurf eine frühere Entscheidungsstufe sein. Philipps archivierter Vergleichsprompt fordert möglichst gleiche Inhalte, Branding und Bildausschnitt sowie eine separate lokale Ansicht mit Umschalter, Schieberegler, Nebeneinander-Vergleich und Zoom. Der Entwurf wird als noch nicht implementiert gekennzeichnet. Die Bedienbarkeit dieser Vergleichsseite belegt weder die Umsetzbarkeit des Bildes noch die späteren Interaktionen der Anwendung.

### Struktur kann Erklärung ersetzen — notwendige Hilfe bleibt

Wenn Nebenlabels und Hilfstexte eine Oberfläche erklären müssen, ist zuerst ihre Struktur zu untersuchen: Gruppierung, Reihenfolge, visuelle Hierarchie und präzisere Hauptlabels können die Ursache lösen. Ein pauschales Textverbot wäre falsch. Fehlerhilfe, Folgen wichtiger Aktionen und zugängliche Namen müssen erkennbar bleiben.

Polish umfasst konkrete Details: optische Ausrichtung, konsistente Abstände, lesbare Typografie, passende Icon-Gewichte, Hit Areas, Fokuszustände, transparente Schatten, sinnvolle Radien und stabile Zahlenbreiten. Solche Heuristiken sind am Produkt zu beurteilen. Ein Detektor kann auffällige Muster finden, aber weder Geschmack noch vollständige Barrierefreiheit entscheiden.

### Daten und Eingabefähigkeiten gehören in die Abnahme

Realistische Extremdaten zeigen Defekte, die saubere Demo-Daten verbergen: lange Namen, untrennbare E-Mail-Adressen, fehlende Bilder, leere oder große Listen, verschiedene Schriftsysteme und ungewöhnliche, aber zulässige Werte. Die Fixture muss zum tatsächlichen Datenvertrag passen. Demo- und Extremzustand im gleichen Layout erleichtern den Vergleich.

Mobile Qualität wird nicht allein über einen schmalen Viewport geprüft. Hover-Fähigkeit, Pointer, Touchflächen, Bildschirmtastatur, Safe Areas, Browserleisten, Zoom, Textauswahl und Scrollverhalten können das Ergebnis verändern. Eine Desktop-Vorschau bei 375 Pixeln ist eine Layoutprobe; sie ersetzt keinen benötigten Test auf dem Zielgerät.

Eine visuelle Abnahme betrachtet das tatsächliche Rendering mit vergleichbaren Daten und Zuständen. Lange Seiten werden vollständig betrachtet, Interaktionszustände gesondert ausgelöst. Beabsichtigte Änderungen erhalten einen Sollzustand; Gleichheit mit der bisherigen Live-Version ist nicht automatisch das Ziel. Neue Defekte werden von vorhandenen Auffälligkeiten getrennt.

### Bewegung braucht einen Zweck

Animation kann Zusammenhang, räumliche Orientierung, Rückmeldung und Zustandswechsel erklären. Sie kann ebenso Aufmerksamkeit binden, Arbeit verlangsamen oder Bedienung erschweren. Vor Timing und Easing steht deshalb die Frage, welche Information die Bewegung vermittelt.

Interaktionen müssen unterbrechbar bleiben und reduzierte Bewegung berücksichtigen. Performance wird am realen Gerät beziehungsweise im geeigneten Laufzeitprofil geprüft. Transition-Bibliotheken liefern Ausgangswerte, ersetzen aber keine Entscheidung über Zweck, Intensität und Eignung. Eine Animation, ein Routenwechsel und ein geschnittener Produktfilm benötigen unterschiedliche Produktions- und Prüfverfahren.

**Grundlage:** [Brand Kit](../80_Knowledge/Patterns/Brand-Kit-als-gemeinsame-Artefaktbasis.md), [Variantenvergleich](../80_Knowledge/Patterns/Variantenvergleich-vor-Produktionsabnahme.md), [Layout vor Hilfstext](../80_Knowledge/Patterns/Layout-vor-Hilfstext-pruefen.md), [UI-Grenzfälle](../80_Knowledge/Patterns/UI-Grenzfaelle-mit-realistischen-Daten-pruefen.md), [Mobile](../80_Knowledge/Patterns/Mobile-Webapp-nach-Eingabefaehigkeit-pruefen.md), [visuelle Abnahme](../80_Knowledge/Patterns/Visuelle-Abnahme-mit-Live-Lokal-Vergleich.md).

## 13. Videos und Motion als überprüfbare Produktion

### Ein Film entsteht aus Entscheidungen über Zeit

Codebasierte Videos verbinden eine Gestaltung mit einer Timeline und einem Renderer. Die Ausgabe soll für einen bestimmten Zeitpunkt reproduzierbar sein: derselbe Zeitpunkt, dieselben Assets und derselbe Zufalls-Seed ergeben denselben Frame. Ein direkter Zeitzugriff wie seek(t) erleichtert die Untersuchung, weil nicht jedes Mal die gesamte Animation ablaufen muss. Versteckte Echtzeitabhängigkeiten, Netzwerkzugriffe und ungesetzter Zufall erschweren dagegen Rendering und Reparatur.

Vor der Animation stehen Botschaft, Zielgruppe, Format, tatsächliche Produktfakten und gewünschte Handlung. Ein Storybeat benennt, was die Zuschauer danach mehr wissen. Die Shotlist übersetzt diesen Wissensfortschritt in sichtbare Zustände. Ein Titel, ein Screenshot und ein Übergang sind Mittel; ihre bloße Abfolge ergibt noch keine verständliche Geschichte.

Reale Produktoberflächen, Logos und Zahlen werden als verbindliche Assets behandelt. Eine erfundene Oberfläche kann eine Illustration sein, darf aber nicht als belegte Produktfunktion erscheinen. Referenzvideos lassen sich über Frames und Transkript analysieren: Welche Informationsdichte, Bildkomposition, Übergänge und Lesepausen tragen ihre Wirkung? Das ist eine Untersuchung der Gestaltung, keine pauschale Erlaubnis, geschützte Inhalte zu übernehmen.

### Frühe Gates vermeiden teure Fehlproduktion

Ein sinnvoller Ablauf führt vom Brief über Styleframes und Animatic zum vollständigen Film. Zuerst werden die längste Copy, endgültige Schriften, echte Assets und kleine Ausgabegrößen geprüft. Erst danach lohnt die Ausarbeitung vieler Szenen. Bei freigestellten Bildobjekten helfen einzelne Ebenen, Bewegung gezielt zu gestalten. Die Wahl zwischen HTML, Canvas, WebGL, Remotion, HyperFrames oder einer anderen Renderumgebung folgt der benötigten Szene und vorhandenen Pipeline.

Eine lokale Korrektur beschreibt Ort und Zeitpunkt, beobachteten Fehler, konkrete Änderung und zu bewahrende Eigenschaften. Dadurch wird aus „mehr Punch“ eine ausführbare Reparatur. Contact Sheets zeigen Layoutprobleme über die Timeline. Aufeinanderfolgende Frames zeigen schnelle Übergänge. Die vollständige Wiedergabe prüft Lesbarkeit, Rhythmus, Dramaturgie und Übergänge zwischen den untersuchten Stichproben. Keine dieser Prüfungen ersetzt alle anderen.

Hochkant und Querformat benötigen eigene Kompositionen mit passenden Textumbrüchen und Bildausschnitten. Ein Crop derselben Szene kann die entscheidende Information entfernen. Statische Kennzahlen oder ein automatisch erzeugtes Audit belegen nur die jeweils gemessenen Eigenschaften. Sie ersetzen kein Urteil über Verständlichkeit und Wirkung.

### Ton wird an der fertigen Ausgabe geprüft

Wortzeitstempel sollten zur tatsächlich verwendeten Sprachaufnahme passen. Ein früherer Text mit anderer Sprechgeschwindigkeit ist keine sichere Zeitbasis. Musik, Sprache, Effekte und Pausen brauchen eine gemeinsame Mischung. Ein erkanntes Beatraster kann versetzt sein; Wellenformkontrolle und Anhören prüfen verschiedene Aspekte.

Die im Bestand vorgeschlagenen Lautheitswerte sind Produktionsziele der jeweiligen Autoren. Maßgeblich sind Zielmedium und konkrete Ausgabe. Die exportierte Datei muss auf vorhandene Tonspuren, Synchronität, Pegel und hörbare Fehler geprüft und vollständig angesehen beziehungsweise angehört werden. Ein korrektes Projekt oder erfolgreiche Renderlogs beweisen das fertige MP4 nicht.

Viele One-shot-Erzählungen verbergen Vorbereitung, Referenzsuche, Skills, Varianten und Korrekturrunden. Ein fairer Verfahrensvergleich hält Aufgaben, Assets, Nachbearbeitung und Abnahmekriterien möglichst gleich. Selbstberichtete Centbeträge erfassen häufig weder Abos noch Agentennutzung oder menschliche Produktionszeit. Kosten je akzeptiertem Film sind aussagekräftiger als der Preis eines einzelnen Generationsaufrufs.

**Grundlage:** [framebasierte Produktion](../80_Knowledge/Patterns/Framebasierte-Motion-Produktion-mit-Brief-und-Abnahme.md), [Videoanalyse](../80_Knowledge/Patterns/Videoanalyse-mit-Frames-und-Transkript.md), [Brand Kit](../80_Knowledge/Patterns/Brand-Kit-als-gemeinsame-Artefaktbasis.md).

## 14. Wissen, Recherche, RAG und Memory

### Herkunft erhalten, bevor verdichtet wird

Eine belastbare Wissensnotiz unterscheidet Originalaussage, eigene Interpretation und zusätzlich geprüften Befund. Zur Herkunft gehören Original-URL, Autor, Veröffentlichungs- und Abrufdatum, Roharchiv und die genaue Fundstelle. Bei Repositories kommen Checkout und gelesene Dateien hinzu. Eine Source-Notiz soll ihre Grundlage erschließen, statt sie durch eine überzeugender klingende, aber weitergehende Aussage zu ersetzen.

Rohquelle, Source-Notiz, Pattern und Themenindex erfüllen verschiedene Zwecke. Die Rohquelle bewahrt den erfassten Inhalt. Die Source-Notiz ordnet eine Veröffentlichung ein. Ein Pattern formuliert eine übertragbare Arbeitsweise mit Voraussetzungen, Belegen und Spannungen. Der Themenindex verbindet verwandte Notizen. Die Zahl dieser Dateien ist keine Zahl unabhängiger Studien. Ein Tweet über einen Herstellerbericht und ein Video über denselben Tweet bilden keine drei unabhängigen Bestätigungen.

Bei einer Synthese werden Aussagen zunächst einzeln erfasst und erst danach gruppiert. Häufigkeit kann zeigen, welche Themen den Bestand prägen. Sie beweist keine Wirksamkeit. Gemeinsame Herkunft, ähnliche Beispiele, Sponsoring und Wiederveröffentlichungen müssen bei der Belegstärke berücksichtigt werden. Widersprüche bleiben mit Datum und Geltungsbereich sichtbar.

### Retrieval und vollständige Lektüre beantworten verschiedene Aufträge

Eine gezielte Suche soll die nächste Frage effizient beantworten. Sie darf irrelevante Inhalte auslassen. Eine Gesamtauswertung benötigt dagegen ein vorab erfasstes Inventar und einen Abdeckungsnachweis. Viele passende Suchtreffer beweisen keine Vollständigkeit; ein großer Index beweist keine Lektüre. Dieser Unterschied gilt auch für GraphRAG, Embeddings und automatisch erzeugte Zusammenfassungen.

Volltextsuche findet Begriffe und genaue Kennungen gut. Semantische Suche kann verwandte Formulierungen erschließen. SQL beantwortet strukturierte Aggregationen. Ein multimodaler Bestand braucht zusätzlich stabile Identität über Text-, Tabellen- und Bildderivate hinweg. Die Ausgabe sollte auf das Original zurückführen, einschließlich Tabellenstruktur oder vollständigem Dokument, wenn die Antwort davon abhängt.

Updates, Wiederholungen und Löschungen gehören zum Datenmodell. Ein einmal funktionierender Import reicht nicht: Dieselbe Veröffentlichung darf nach erneutem Lauf nicht unkontrolliert dupliziert werden; geänderte oder entfernte Quellen müssen in abgeleiteten Indizes entsprechend behandelt werden. Eine Rohquelle mit abgeschnittenem Ende bleibt auch nach erfolgreicher Indexierung unvollständig.

### Ein Knowledge Graph braucht eine ausdrückliche Semantik

Aussagen, Quellen, Methoden und Fähigkeiten sind unterschiedliche Objekttypen. Beziehungen wie „belegt“, „widerspricht“, „setzt voraus“, „gilt für“ und „implementiert“ erlauben gezieltere Fragen als bloße thematische Nähe. Extrahierte Fakten und vom Modell erschlossene Beziehungen werden getrennt gekennzeichnet. Ein schöner Graph macht eine Vermutung nicht wahr.

Ein Hash kann zeigen, ob eine bekannte Datei seit der Prüfung verändert wurde. Ändert sie sich, können davon abhängige Aussagen gezielt invalidiert werden. Ein unveränderter Hash beweist jedoch keine inhaltliche Aktualität: Neue Gegenbelege oder eine außerhalb des Archivs geänderte Produktfunktion können die Aussage trotzdem überholen. Technische Integrität und semantische Pflege sind zwei Aufgaben.

Memory-Systeme speichern episodische Erfahrungen oder kuratierte Regeln. Automatisch verdichtete Erinnerungen können situative Wünsche fälschlich verallgemeinern. Ein guter Eintrag hält Anlass, Reichweite und Herkunft fest. Für Korrekturen und Verwerfen alter Annahmen muss ein klarer Pfad bestehen. Synchronisierte Markdown-Dateien, wieder auffindbare Sessions und nach einem Neustart wieder laufende Dienste sind außerdem drei verschiedene Fähigkeiten.

**Grundlage:** [Wissenspflege](../80_Knowledge/Patterns/Wissenspflege-mit-Inbox-und-Review.md), [Mehrquellen-Synthese](../80_Knowledge/Patterns/Mehrquellen-Synthese-mit-Haeufigkeiten-und-Widerspruechen.md), [RAG](../80_Knowledge/Patterns/RAG-mit-Text-Tabellen-und-Volltextpfad.md), [eigene Wissensfabrik](../docs/wissensfabrik/README.md).

## 15. Bestehende Software verstehen, verändern und rekonstruieren

### Verhalten vor der Änderung beobachten

Refactoring verbessert Struktur bei geklärtem Verhalten. Eine Fehlerkorrektur ändert ausdrücklich unerwünschtes Verhalten. Eine Migration wechselt technische Grundlagen. Diese Vorhaben können zusammen auftreten, benötigen aber erkennbare Ziele und Nachweise. Wer gleichzeitig Architektur, Datenmodell und Benutzerverhalten ändert, erschwert die Zuordnung einer Regression.

Ein Verhaltensvergleich erfasst repräsentative Eingaben, Ausgaben, Zustände und Fehlerfälle vor und nach der Änderung. Der Sollzustand entscheidet, ob eine Abweichung erwünscht ist; reine Gleichheit kann einen bestehenden Fehler konservieren. Eine grüne vorhandene Testsuite belegt nur ihre abgedeckten Fälle. Die im Archiv geschilderte Bun-Migration mit später gefundenen Regressionen zeigt, warum Integrationsverhalten und reale Nutzung ergänzend geprüft werden müssen.

Performancearbeit beginnt mit einer gemessenen Ursache. Weniger Renderings, kleinere Bundles oder schnellere Teilfunktionen sind mögliche Proxys. Ihr Nutzen muss sich am relevanten Benutzerpfad zeigen. Ein großer Komplexitätszuwachs für einen kaum spürbaren Gewinn kann die falsche Abwägung sein. Reale Browseraufzeichnungen können andere Fehler offenlegen als eine ausschließlich headless ausgeführte Probe.

### Reverse Engineering braucht eine begrenzte Erkenntnisfrage

Übertragbar ist die Trennung von Untersuchung und Umsetzung. Eine Analyse hält beobachtetes Verhalten, belegte Strukturen und Unbekanntes fest. Die Verhaltensspezifikation ist der Vertrag für eine separate Implementierung. Ein Comparator prüft ausgewählte Gemeinsamkeiten und Unterschiede. Der Comparator selbst benötigt Kontrollfälle, die bewusst falsches Verhalten zuverlässig erkennen.

Eine kleine Frage wie „Welche Eingaben beeinflussen diesen Export?“ ist besser überprüfbar als „rekonstruiere die gesamte Anwendung“. Statische Analyse, Textsuche, Laufzeitbeobachtung und Protokollanalyse erschließen unterschiedliche Teile. Nicht zugänglicher Servercode, fremde Daten und betriebliche Prozesse bleiben unbekannt. Die REA-Beispiele zeigen neben eindrucksvollen Behauptungen auch abgebrochene Analysen und Ergebnisse, die schon durch einfache Suche auffindbar waren.

Featureähnlichkeit, sichtbare Parität, vollständige Semantik und wirtschaftlicher Ersatz sind verschiedene Ziele. Mehrere Beiträge wiederholen dieselben Showcases; daraus entsteht kein unabhängiger Nachweis universeller Rekonstruierbarkeit. Das als Clean Room bezeichnete Arbeitsformat ist eine Informationsgrenze, keine hier geprüfte rechtliche Freigabe. Vor einem tatsächlichen Vorhaben müssen Berechtigung, Herkunft und zulässiger Umfang separat geklärt sein.

### Wartung benötigt Nutzungs- und Entscheidungswissen

Ein nicht gefundener statischer Aufrufer beweist keine Nichtnutzung. Dynamische Namen, Konfiguration, externe Verbraucher, historische Gründe und Live-Betrieb können relevant sein. Ein konstantes Feature Flag kann weiterhin als Killswitch dienen. Datenlöschung und entfernte Außenwirkungen sind durch einen Git-Revert nicht zuverlässig rückgängig zu machen.

Kleine akzeptierte Wartungsänderungen können anschließend als Lernfälle dienen. Wiederkehrende Fehlerklassen wandern, wo sinnvoll, in zentrale Helper, Typen, Tests oder Lintregeln. Retrospektiven halten Ursache, konkrete Prävention, Verantwortlichkeit und spätere Nachkontrolle fest. Commitzahl und erledigte Tickets bleiben Aktivitätsmaße; die Wirkung zeigt sich an besseren Ergebnissen und weniger erforderlicher Reparatur.

**Grundlage:** [Refactoring](../80_Knowledge/Patterns/Refactoring-mit-Verhaltensvergleich.md), [Analyse und Nachbau](../80_Knowledge/Patterns/Verhaltens-Spec-als-Grenze-zwischen-Analyse-und-Nachbau.md), [Codepfad](../80_Knowledge/Patterns/Codepfad-vor-Aenderung-nachvollziehen.md), [Fachregeln](../80_Knowledge/Patterns/Fachregel-Konsolidierung-vor-Featureaenderung.md).

## 16. Produkte, Marketing, SEO und Schreiben

### Technische Reproduzierbarkeit ist nur ein Teil des Produktwerts

Niedrigere Implementierungskosten verändern, welche Werkzeuge eine Person selbst bauen kann. Sie beseitigen Wartung, Datenqualität, zuverlässigen Betrieb, Distribution, Vertrauen und fachliche Weiterentwicklung nicht. Ein persönliches Hilfsmittel kann mit kleinem Umfang genügen. Ein Produkt für andere Menschen benötigt einen zugesagten Leistungsumfang und einen tragfähigen Betrieb.

Echte Nutzer prüfen Dinge, die eine Demo und simulierte Personas nur eingeschränkt erfassen: Verstehen sie das Angebot, lösen sie ihre Aufgabe, kommen sie wieder, vertrauen sie dem Ergebnis? Ein KI-gestützter Persona-Durchlauf kann Blockaden finden, bildet aber keine unabhängige Nutzerstudie. Feedback ist eine Lernquelle; allein sein Vorhandensein beweist keinen Netzwerkeffekt.

Ein sinnvoller Produktversuch hält Zielgruppe, Problem, gewünschte Verhaltensänderung und Beobachtungszeit fest. Eine Anmeldung, eine abgeschlossene Kernaufgabe, wiederkehrende Nutzung und Zahlung messen unterschiedliche Stufen. Die passende Kennzahl folgt dem Nutzenversprechen. Vermittelte Händlerumsätze sind beispielsweise keine eigenen Affiliate-Einnahmen.

### Inhalte und Suchintention vor Layout klären

Website-Arbeit beginnt mit Angebot, Zielgruppe und gewünschter Handlung. Suchbegriffe und vorhandene Nutzerdaten können zeigen, welche Fragen und Absichten tatsächlich relevant sind. Informationssuche, Vergleich und Kaufbereitschaft verlangen unterschiedliche Antworten. Ein Design ohne klare Inhalte optimiert möglicherweise die falsche Aufgabe.

Rechercheanbieter, Keyword-Tools und generierte Briefings sind Eingänge, keine Wahrheit. Anbieterantworten, eigene Interpretation und erfundene Beispieldaten werden getrennt gehalten. Gesponserte Vorführungen desselben Dienstes bilden keinen unabhängigen Wirkungsnachweis. Strukturierte Inhalte, Metadaten, interne Verlinkung, technische Erreichbarkeit und passende strukturierte Daten unterstützen Auffindbarkeit; sie garantieren keine Suchposition und keine Conversion.

Lighthouse, Browserprüfung, Veröffentlichung, Indexierung und Geschäftserfolg sind unterschiedliche Nachweise. Eine lokal schnelle Seite kann später andere reale Nutzungswerte zeigen. Ein A/B-Test benötigt eine begründete Zielgröße und hinreichende Beobachtung; ein einzelner Vorher-/Nachher-Wert kann durch andere Änderungen beeinflusst sein.

### Überzeugende Kommunikation braucht überprüfbare Substanz

Gute Texte benennen ein konkretes Problem, einen nachvollziehbaren Nutzen und passende Belege. Eine klare Hauptaussage, spezifische Beispiele und verständliche nächste Schritte helfen mehr als austauschbare Superlative. Testimonials, Kundennamen, Zertifizierungen, Preise und Leistungsversprechen müssen auf tatsächlich freigegebenen Tatsachen beruhen.

Psychologische Modelle wie Framing, soziale Orientierung oder Verlustaversion können erklären, wie Menschen eine Entscheidung wahrnehmen. Sie ersetzen keine Produktqualität und keinen empirischen Versuch im eigenen Kontext. Künstliche Knappheit oder erfundene Erfolge wären keine belastbare Anwendung solcher Modelle.

Beim Schreiben im Stil einer Person helfen echte, zur Textart passende Beispiele. Stilübernahme darf Fakten und Absicht nicht verändern. Lange Prompt-Schablonen sind nur sinnvoll, wenn sie wiederkehrende Fehler tatsächlich reduzieren. Floskeln, Wiederholungen und abstrakte Behauptungen lassen sich durch konkrete Aussagen, Belege und klare Verben ersetzen. Menschliche Autorschaft und eigenes Nachdenken können zudem ausdrückliche Ziele sein, auch wenn mehr Delegation möglich wäre.

**Grundlage:** [Produktwert](../80_Knowledge/Patterns/Produktwert-jenseits-des-reproduzierbaren-Codes.md), [echte Testnutzer](../80_Knowledge/Patterns/Produktreife-durch-echte-Testnutzer.md), [Suchintention](../80_Knowledge/Patterns/Suchintention-mit-Daten-vor-Webdesign-klaeren.md). Die späteren Repo-Profile ergänzen konkrete Marketing- und Schreibverfahren.

## 17. Lernen, Rollen und Einführung in Organisationen

### Verstehen kann gezielt Teil des Auftrags sein

KI kann Erklärungen, Rückfragen, Übungen und Gegenbeispiele an tatsächlichen Code binden. Change Quizzes prüfen beispielsweise, ob jemand die Wirkung einer Änderung erklären kann. Die Qualität liegt in den Fragen und ihrer Beziehung zum Lernziel, nicht in der Zahl automatisch erzeugter Aufgaben. Eine überzeugende Erklärung kann falsch sein und braucht bei wichtigen Details die zugrunde liegende Quelle.

Schulungen beginnen deshalb mit Curriculum, Zielgruppe und beobachtbarer Fähigkeit. Erst nach fachlicher Prüfung dieser Struktur lohnt die Erzeugung aufwendiger Videos und interaktiver Medien. Ein bestandener Quiz, hohe Nutzung und tatsächlich selbstständige Arbeitsfähigkeit sind verschiedene Ergebnisse. Transferaufgaben und spätere Anwendung zeigen mehr als unmittelbares Wiedererkennen.

Voice-Prompting kann implizites Wissen schneller zugänglich machen: Hintergründe, Beispiele und Ausnahmen lassen sich im Gespräch leichter schildern. Die Transkription kann Namen, Zahlen und ähnlich klingende Fachwörter verfälschen. Vor folgenreichen Aktionen werden diese Stellen geprüft. Mehr gesprochener Kontext ist nur dann hilfreich, wenn er für die Aufgabe relevant bleibt.

### Verantwortung verschiebt sich, verschwindet aber nicht

Wenn Codeerzeugung billiger wird, gewinnen Problemwahl, Architektur, fachliche Entscheidungen, Integration und Abnahme an Gewicht. Die Quellen nennen dies unter anderem Great Decoupling. Es ist eine nützliche Perspektive auf Arbeitsteilung, keine sichere Prognose über Berufe oder Beschäftigungszahlen. Organisationsaussagen, Zukunftsszenarien und gemessene aktuelle Praxis werden getrennt gelesen.

Eine Einführung braucht verantwortliche Personen mit real verfügbarer Zeit, geeignete Aufgaben, zugängliche Daten und angepasste Schulung. Lizenzen und ein zentraler Promptkatalog allein schaffen keinen verlässlichen Prozess. Eine Bibliothek benötigt Eigentümer, Pflegeanlässe und ein Verfahren für schlechte oder veraltete Beispiele.

Ein begrenzter Pilot misst einen Ausgangszustand und denselben Aufgabentyp mit Unterstützung. Neben Zeit gehören Ergebnisqualität, Nacharbeit, Akzeptanz und tatsächliche Nutzung in die Betrachtung. Selbst eingeschätzte Zeitersparnis ist ein anderes Signal als beobachteter Durchsatz. Lokale Geschwindigkeit wird erst dann Unternehmenswirkung, wenn sie einen relevanten Engpass verändert.

### Strategische Szenarien als Fragen nutzen

AI 2027 und Essays über das Tempo der Frontier-Forschung behandeln Rückkopplungen automatisierter Forschung, Wettbewerbsdruck und schwächere Überwacher. Ein hypothetisches Szenario mit fiktiven Firmen ist keine gemessene Eintrittswahrscheinlichkeit. Das lokale AI-2027-Archiv endet zudem vor den beiden Schlusszweigen. Solche Texte schärfen Fragen nach unabhängiger Kontrolle, nachvollziehbaren Zielen und wirksamen Stopps; sie rechtfertigen keine scheinpräzisen Zukunftsaussagen.

**Grundlage:** [Lernen](../80_Knowledge/Patterns/Claude-als-Lernwerkzeug.md), [Curriculum-Gate](../80_Knowledge/Patterns/Agent-generierte-Schulung-mit-Curriculum-Gate.md), [Voice-Prompting](../80_Knowledge/Patterns/Voice-Prompting-fuer-Kontextreichtum.md), [Rollen](../80_Knowledge/Patterns/Great-Decoupling-Rollenverstaendnis.md), [KI-Adoption](../80_Knowledge/Patterns/KI-Adoption-mit-Use-Case-und-Befaehigungs-Gate.md).

## 18. Von Einzelmethoden zu einer schlanken Agentic Software Factory

### Die Wissensbasis und der laufende Betrieb sind verschiedene Systeme

Das Mutter-Repo enthält Firmenwissen, Methoden, Skills, Projekt-Kits und Entscheidungsgrundlagen. Einzelne Softwareprodukte bleiben in ihren eigenen Repositories. Ein Suchkatalog ist dabei Infrastruktur für Wissenszugriff. Er verwaltet nicht automatisch produktive Jobs, Freigaben, Deployments oder die fachliche Abnahme einer Änderung.

Der lokale Wissenskatalog nutzt dateibasierte Eingänge und SQLite-Volltextsuche mit FTS5/BM25. Er ist kein vollständiger semantischer Graph. Der am 26. Oktober dokumentierte semantische Pilot umfasst 24 Claims, 27 Belegbereiche, drei Synthesen und fünf Capability-Kandidaten. Er zeigt einen begrenzten Ableitungs- und Invalidierungspfad. Daraus folgt keine vollständige semantische Erschließung des gesamten Archivs.

Der Pilot kann Kontext direkt aus seiner Registry bereitstellen und bekannte Abhängigkeiten bei geänderten Basishashes zurückhalten. Das ist eine überprüfbare technische Eigenschaft. Die praktische Verbesserung realer Entwicklungsaufgaben, ein geeigneter Factory-Runtime und die repräsentative erste Aufgabenklasse sind damit noch nicht entschieden. Der allgemeine Katalog und dieser Analysebericht sind wiederum getrennte Artefakte.

### Ein einziger Prozessrahmen, gezielt gewählte Methoden

Eine Factory braucht eine führende Zustandsverwaltung und klare Übergaben. Mehrere umfassende Frameworks gleichzeitig als globale Autorität einzusetzen kann widersprüchliche Phasen, Dateiformate und Freigabeannahmen schaffen. Sinnvoller ist ein verantwortlicher Prozessrahmen mit kleinen Methoden an passenden Stellen.

| Phase | Führende Frage | Nützliches Ergebnis | Abschlussnachweis |
|---|---|---|---|
| Eingang | Was soll für wen besser werden? | Auftrag mit Grenzen und Verantwortlichem | Ziel und offene Entscheidungen sind sichtbar |
| Discovery | Was wissen wir, was fehlt? | Quellen, Codepfade, Unsicherheiten, gegebenenfalls Prototyp | Tragende Annahmen sind belegt oder markiert |
| Entscheidung | Welches Verhalten und welche Grenzen gelten? | Spec, ADR oder kurze Entscheidung | Fachlicher Vertrag ist verständlich |
| Zerlegung | Welche Arbeit ist unabhängig möglich? | Kleine Tickets mit Abhängigkeiten | Jede startbare Aufgabe hat Eingänge und Prüfkriterium |
| Umsetzung | Wie wird der Vertrag im Bestand erfüllt? | Kleine Änderungen und geeignete Prüfungen | Relevante Checks beobachten das gewünschte Verhalten |
| Review | Welche Fehler und Folgen bleiben? | Verifizierte Befunde und Entscheidung | Spec, Standards und Fachfolgen sind beurteilt |
| Lieferung | Welche Außenwirkung ist autorisiert? | Freigegebene Integration beziehungsweise Veröffentlichung | Tatsächlich gelieferter Stand und Betrieb sind beobachtet |
| Lernen | Was verbessert den nächsten Durchlauf? | Nachverfolgte Korrektur an Umgebung oder Verfahren | Maßnahme wurde geprüft, nicht nur notiert |

Nicht jede Aufgabe benötigt acht Dokumente. Eine kleine Änderung kann mehrere Phasen in wenigen Sätzen abdecken. Ein komplexes Vorhaben braucht ausführlichere Artefakte. Für jede Information wird eine führende Quelle gewählt; vorhandene Tickets, Designs und Betriebsdaten werden verlinkt statt unkontrolliert kopiert.

Eine Capability-Karte beschreibt Anlass, Voraussetzungen, Ablauf, Eingänge, Ergebnis, Nachweise und bekannte Grenzen einer Fähigkeit. Sie erleichtert Auswahl. Sie ist weder Installationsfreigabe noch Nachweis produktiver Zuverlässigkeit. Die Skill-Registry behält ihre eigene Rolle bei Vertrauen und erlaubter Nutzung externer Pakete.

### Wiederholung benötigt expliziten Zustand

Ein Loop braucht Aufgabe, Beobachtung, Stop-Bedingung, Ressourcenrahmen und Wiederaufnahmezustand. „Arbeite weiter“ erzeugt Aktivität ohne eindeutiges Ende. Fortschrittsdateien und Journale halten erledigte und offene Einheiten fest. Ein vollständig gelesener Abschlussbericht sollte den nächsten Bearbeiter handlungsfähig machen; allein ein gesetztes Done-Flag genügt nicht.

Automationen sollten mit belastbaren Quellen-Bookmarks arbeiten. Ein relativer Zeitraum wie „seit gestern“ kann bei Ausfällen Lücken oder Doppelverarbeitung erzeugen. Ein Lesefehler darf nicht als leere Ergebnismenge gelten. Ein Versand ist erst nach bestätigter Übergabe abgeschlossen. Ein Bookmark allein garantiert keine Exactly-once-Verarbeitung; Idempotenz und atomare Zustandsübergänge bleiben erforderlich.

Projektkarten können aktuellen Stand, letzten Nachweis und erforderliche Entscheidung zeigen. Handlungsbedarf gehört an den Anfang eines Berichts. Schweigen nach einem eindeutigen Freigabeauftrag ist anders zu beurteilen als eine noch offene echte Entscheidung. Ein Kartenstatus braucht Datum und Beleg, sonst entsteht eine weitere veraltende Übersicht.

### Skalierung erst nach gemessenem Engpass

Mehr Agenten erzeugen mehr Repositoryzugriffe, Builds, Tests, Reviewbedarf und Ereignisse. Die CI-Berichte zeigen, dass veraltete Testhistorien zu falscher Testselektion führen können. Zustandslose Listener mit getrenntem Ergebnisjournal entlasten den Eingang; Reihenfolge, Deduplizierung, Wiederaufbau und Aktualitätsverzug müssen trotzdem geklärt werden.

Bedarfsorientierter Repositoryzugriff trennt Metadatenabfragen von benötigten Dateiinhalten. Nicht jeder Job braucht vollständigen Checkout und Historie. Die beschriebenen Monorepo-Systeme reagieren auf außergewöhnliche Last. Für kleinere Projekte ist zuerst zu messen, welcher Zugriff oder Check überhaupt Zeit kostet. Eine große Infrastruktur nachzubauen, bevor dieser Engpass existiert, wäre keine aus dem Bestand belegte Verbesserung.

**Grundlage:** [Zielarchitektur](../docs/wissensfabrik/agentic-factory-architektur.md), [Methodenvergleiche](../80_Knowledge/Vergleiche/Factory-Spec-Build-Review.md), [Agent-Organisation](../80_Knowledge/Patterns/Agent-Organisation-mit-Rollen-Budgets-und-Heartbeats.md), [Bookmarks](../80_Knowledge/Patterns/Quellen-Bookmarks-fuer-Agent-Automationen.md), [Projektkarte](../80_Knowledge/Patterns/Projektkarte-als-Status-und-Entscheidungsartefakt.md), [CI-Journal](../80_Knowledge/Patterns/Zustandslose-CI-Listener-mit-Ergebnisjournal.md), [Repositoryzugriff](../80_Knowledge/Patterns/Bedarfsorientierter-Repositoryzugriff.md).

## 19. Die wichtigen Spannungen im Bestand

Die Quellen lassen sich nicht widerspruchsfrei zu einer einzigen universellen Methode verdichten. Folgende Entscheidungen bleiben vom Kontext abhängig:

| Spannung | Wann die erste Seite plausibel ist | Wann die Gegenposition plausibel ist | Was vor der Auswahl geprüft wird |
|---|---|---|---|
| Plan und Spec vor Code ↔ früher Prototyp | Hohe Fehlerkosten, mehrere Beteiligte, bekannte Fachanforderungen | Unsichere Interaktion oder kleine reversible Änderung | Welche Ungewissheit löst der nächste Schritt tatsächlich auf? |
| Dauerhafte Feature-Spec ↔ abschließbares Issue | Langfristig gepflegter Verhaltensvertrag | Eng begrenzte Änderungsarbeit mit anderer führender Dokumentation | Pflegeverantwortung und spätere Wiederauffindbarkeit |
| Lange Session ↔ frischer Kontext | Zusammenhängende Aufgabe mit wichtigen impliziten Details | Unabhängige Aufgabe oder festgefahrene Annahme | Welche Information geht verloren, welcher Ballast bleibt? |
| Viele Spezialisten ↔ gemeinsamer Agentenloop | Unabhängige Eingänge und klar getrennte Ergebnisse | Eng gekoppelte Entscheidungen mit hohem Handoff-Verlust | Ende-zu-Ende-Qualität einschließlich Integration |
| Mehr Instruktionen ↔ bessere Umgebung | Fachliche Regeln sind nicht aus dem System ableitbar | Fehler lassen sich durch Typen, Schnittstellen oder Checks verhindern | Tatsächliche Fehlerklasse und aktive Modelle |
| Striktes TDD ↔ andere Agenten-Arbeitsfolge | Regression und fachliches Verhalten lassen sich früh ausdrücken | Explorative Arbeit benötigt zunächst neue Erkenntnisse | Belegt die Prüfung den alten Fehler und das gewünschte neue Verhalten? |
| Checks nach jedem Edit ↔ Checks an Arbeitseinheiten | Kurze lokale Prüfung mit hohem Signal | Zusammenhängender Umbau mit bewusst inkonsistentem Zwischenstand | Feedbacknutzen, Dauer und verbindlicher Integrationspunkt |
| Günstiges Modell zuerst ↔ starke Konfiguration sofort | Große Mengen gut prüfbarer Aufgaben | Schwierige Aufgaben mit teurer Fehlrecherche | Kosten je akzeptiertem Ergebnis und Fehlerfolgen |
| Menschliches Review ↔ automatische Abnahme | Hohe Folgen, unklarer Vertrag oder schwacher Grader | Eng begrenzte, gemessene Aufgabenklasse mit wirksamen Kontrollen | Übersehene Fehler, Fehlalarme und sichere Rückfallstrategie |
| Zentralisierung ↔ lokale Duplikation | Gemeinsame Fachregel oder globales Primitive | Kontextgebundene Darstellung mit bewusst eigener Entwicklung | Ist die Bedeutung wirklich dieselbe? |
| Große Wissensbasis ↔ wenig Kontext | Breite Exploration oder nachgewiesene Gesamtauswertung | Konkrete Ausführung mit engem Informationsbedarf | Inventar, Relevanz und Rückweg zum Original |
| Automatisch erzeugter Inhalt ↔ menschliche Autorschaft | Reproduzierbare Vorarbeit und gewünschte Delegation | Lernen, Urteil oder persönliche Ausdrucksform sind selbst das Ziel | Was soll der Mensch nachher verstanden oder selbst gestaltet haben? |

Manche Gegensätze verschwinden, wenn Lebenszyklen unterschieden werden: Ein dauerhaftes Ticket sollte keine rasch veraltenden Implementierungsdetails festschreiben; der aktuelle Ausführungsplan braucht dagegen genaue Dateien und Symbole. Andere Gegensätze bleiben echte Alternativen. Sie werden durch einen begrenzten Vergleich geklärt, nicht durch die Behauptung, beide seien immer gleichzeitig optimal.

## 20. Was sich aus dem Gesamtbestand praktisch ableiten lässt

Die folgenden Vorhaben sind aus der Synthese abgeleitete Vorschläge. Dieser Bericht setzt sie nicht automatisch um und erteilt keine neue Freigabe.

| Reihenfolge | Begrenzter Versuch | Beobachtbarer Nutzen | Wichtige Grenze |
|---|---|---|---|
| 1 | Eine wiederkehrende Entwicklungsaufgabe mit aktuellem Ablauf als Baseline erfassen | Akzeptanz, Nacharbeit, Laufzeit und Gesamtaufwand werden vergleichbar | Aufgaben nicht nachträglich passend zur Variante auswählen |
| 2 | Einen konkreten Fehler durch bessere Daten, Typen, Schnittstelle oder Check schwerer machbar machen | Derselbe Fehler tritt in Kontrollfällen seltener auf | Kein allgemeiner Umbau aufgrund eines einzigen unsicheren Findings |
| 3 | Einen kleinen Skill gegen No-Skill-Baseline prüfen | Trigger, Verfahrensbefolgung und Ergebnisnutzen werden sichtbar | Geeigneter Grader und unveränderte Aufgabengrundlage |
| 4 | Einen Review-Agenten ohne Freigabemacht auf historische Fehler und saubere Änderungen ansetzen | Übersehene Fehler und Fehlalarme werden messbar | Erfolg im Shadow Mode ist noch keine Autorisierung |
| 5 | Eine unabhängige Recherche in klar begrenzte Pakete teilen | Gesamtlaufzeit sinkt bei gleichwertiger Abdeckung | Koordination, doppelte Reads und Konsolidierung mitrechnen |
| 6 | Einen UI- oder Videoprozess mit realen Extremdaten und reproduzierbaren Zuständen versehen | Konkrete Defekte werden früher auffindbar | Sampleframes ersetzen weder Interaktion noch vollständiges Playback |
| 7 | Einen Wissensclaim mit Herkunft und Invalidierungsabhängigkeit über den Pilotpfad führen | Geänderte Grundlage wird zuverlässig sichtbar | Unveränderte Datei bedeutet keine dauerhaft wahre Aussage |
| 8 | Eine Automation mit Bookmark, Fehlerstatus und Idempotenz lokal erproben | Ausfall und Wiederholung erzeugen keine stillen Lücken | Externe Kommunikation und produktive Rechte separat freigeben |

Die Auswahl folgt Nutzen, Zuversicht, Aufwand und Fehlerfolgen. Eine Methode mit geringem Einführungsaufwand und einer häufigen bestätigten Fehlerklasse kann vor einem umfassenden Framework liegen. Eine anspruchsvolle Runtime lohnt erst, wenn ihr zusätzlicher Zustand und ihre Kontrollmechanismen ein gemessenes Problem lösen.

Das dauerhaft wiederkehrende Arbeitsprinzip ist ein nachvollziehbarer Vertrag zwischen Absicht, Information, Handlung und Nachweis. Die folgenden Register machen die einzelnen Beiträge, Werkzeugfamilien und Grenzen hinter dieser Verdichtung auffindbar.


## 21. Alle 74 externen Repositories: Funktionen, Methoden und Grenzen

Dieses Kapitel beruht auf den vollständig gelesenen tatsächlichen READMEs beziehungsweise angegebenen Einstiegen und ausgewählten zentralen Skills, Dokumenten oder Implementierungen. Große Pakete werden als Ganzes erschlossen, aber nicht jede einzelne Rolle und jede Codezeile als geprüft ausgegeben. Die Profile nennen ihre konkreten Lektürepfade. Externe Anweisungen wurden als Untersuchungsgegenstand gelesen und nicht als neue Arbeits- oder Aktionsrechte übernommen.

Die Gruppierung folgt dem hauptsächlichen Nutzen. Viele Repos berühren mehrere Bereiche. Keine Zeile ist eine Installations- oder Produktionsfreigabe. Versions-, Lizenz-, Datenfluss- und Hostgrenzen gehören zur späteren Auswahl.

| Bedarf | Passende Referenzfamilie | Entscheidung vor einer Übernahme |
|---|---|---|
| Einen Entwicklungsablauf strukturieren | Kleine Pocock-Skills, Superpowers, Spec Kit, BMAD, GSD, pstack, gstack, HumanLayer | Wie viel Discovery, Zustand und Prozesssteuerung braucht die konkrete Aufgabe? |
| Mehrere Agenten dauerhaft koordinieren | Squad, Paperclip, Agency, Council | Sind Aufgaben wirklich unabhängig, welche Instanz hält Zustand und Freigaben? |
| Skills verteilen und prüfen | Offizielle Skills, Ruler, Autoskills, ECC, NVIDIA-Werkzeuge | Welche Dateien werden installiert, was ist tatsächlich evaluiert und welche Rechte gelten? |
| Kontext finden und aktualisieren | OpenWiki, Graphify, Understand-Anything, Claude-Mem, Context7, MarkItDown, Notebooklm-py | Geht es um Quellen, Code, Episoden, aktuelle API-Dokumentation oder generierte Ableitungen? |
| Kosten und Backends steuern | RTK, Headroom, Caveman, OmniRoute, CC Switch, CLIProxyAPI | Wo wird reduziert oder umgeleitet, welche Originale bleiben erreichbar und was wird extern übertragen? |
| Oberflächen entwickeln und prüfen | Taste, Impeccable, Emil, UI UX Pro Max, shadcn, Vercel, React Doctor, Front-End Checklist | Welcher fachliche Zweck, welche vorhandene Designsprache und welche tatsächlichen Zielgeräte gelten? |
| Technische Sachverhalte und Produkte zeigen | Archify, Diagram Design, oh-my-mermaid, HyperFrames, Brag | Welche Quelle trägt die Darstellung und welche Bild-, Bewegungs- und Tonabnahme ist nötig? |
| Nachfrage und Kommunikation verbessern | Marketing Skills, Claude SEO, No AI Slop, I Have ADHD | Welche Aussagen sind belegt und welches tatsächliche Nutzerverhalten wird beobachtet? |


### Entwicklungsprozesse und Orchestrierung

#### R01 · 0xNyk/council-of-high-intelligence

[GitHub](https://github.com/0xNyk/council-of-high-intelligence) · Revision: `34fd7bb45129ac17009b45f64adb4b6c2c303cc3` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Council of High Intelligence beschreibt ein Entscheidungsverfahren mit 18 gegensätzlichen analytischen Rollen. Übertragbar sind vor allem die blinde erste Einschätzung, anonymisierte Gegenprüfung, sichtbare Minderheitspositionen und die Trennung von Fakten, Schlussfolgerungen, Annahmen und Unbekanntem. Full, Quick und Duo variieren den Aufwand. Ein Urteil soll Handlung, Kill-Kriterien und einen späteren Prüftermin festhalten, damit es revidierbar bleibt. Das Verfahren gewichtet Domänenkompetenz und selbst eingeschätzte Sicherheit, liefert dafür aber keinen Kalibrierungsnachweis. Simulierte Persönlichkeiten und mehrere Provider garantieren keine unabhängige Evidenz. Auch ein formal begrenzter Ablauf kann durch zusätzliche Nachfragen teuer werden. Für die Factory ist das eine Referenz für schwierige Architektur- und Produktentscheidungen; triviale Faktenfragen rechtfertigen diesen Aufwand kaum. Die gelesenen Dateien belegen das Protokoll, keinen gemessenen Qualitätsgewinn.

**Übertragbare Verfahren:**

- Full mit drei Runden, Quick mit zwei Runden und Duo als gezieltes Gegenpaar begrenzen die Verfahrensform.
- Behauptungen werden als FACT, INFERENCE, ASSUMPTION oder UNKNOWN markiert; Neuigkeitsprüfung und Gegenhypothesen sollen Echokammern aufbrechen.
- Eine Dissent-Quote und Counterfactuals ab hohem Einverständnis erhalten Einwände.
- Vorab bestimmte Domänengewichte und Konfidenzfaktoren erzeugen ein explizites, jedoch nicht kalibriertes Abstimmungsverfahren.
- Kill-Kriterien, nächste Handlung, Prüftermin und Minderheits-Dealbreaker machen Urteile revidierbar.

**Voraussetzungen:** Agentenfähiger Host; optionale authentifizierte Provider-CLIs. Klare Entscheidung mit Alternativen, Aufwand- und Berechtigungsgrenzen.

**Weitere Grenzen und Voraussetzungen der Aussage:** Persona-Rollen sind simulierte Blickwinkel, keine unabhängigen menschlichen Experten. Selbstberichte zur Sicherheit sind nicht kalibriert; mehrere Provider können dasselbe Basismodell nutzen. Zusätzliche Erzwingungsaufrufe können das nominelle Rundenbudget erweitern; externe Beispiele aktivieren Auto-Approval. Kein eigener Qualitäts-, Kosten- oder Sicherheitsnachweis.

**Abgleich mit dem Index:** Grundzweck bestätigt. Das Urteil-Template beginnt mit akzeptablen Kompromissen, Kill-Kriterien und nächstem Schritt, bevor offene Fragen folgen; die Indexformulierung offene Fragen vor Konsens vereinfacht.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/0xNyk/council-of-high-intelligence/README.md>) · [SKILL.md](<../external_repos/0xNyk/council-of-high-intelligence/SKILL.md>) · [agents/council-feynman.md](<../external_repos/0xNyk/council-of-high-intelligence/agents/council-feynman.md>)

#### R02 · addyosmani/agent-skills

[GitHub](https://github.com/addyosmani/agent-skills) · Revision: `aeac41d4d005999432bb7312f7ff06383a91d59d` · README-Vertrag; Skill-Vertrag; kein eigener Lauf

Addy Osmanis Agent Skills ordnen Engineering-Arbeit einem durchgehenden Lifecycle zu und ergänzen sie um Review-Personas und gemeinsame Checklisten. Besonders konkret ist Constraint-Driven Development: Ein Qualitätsziel wird mit einem ausführbaren Kommando, seinem Zeitbudget und seiner Begründung verbunden. Bestehende Schwächen sollen zunächst gemessen und anschließend schrittweise verschärft werden. Das vermeidet Gates, die bei jeder Ausführung rot bleiben und dadurch ihre Wirkung verlieren. Ausnahmen benötigen einen Verantwortlichen und ein Ablaufdatum. Die Sammlung unterscheidet außerdem Prüfungen außerhalb des Agenten von selbst geschriebenen Tests. Diese Hierarchie ist nützlich, garantiert aber keine Fehlerfreiheit. Gemeinsame Referenzen können bei Einzelinstallation fehlen, und Host-Adapter besitzen unterschiedliche Fähigkeiten. Das gelesene Impact-Ledger enthält keine ausgefüllten Ergebnisse. Die Sammlung liefert damit nachvollziehbare Arbeitsverträge und Integrationsmuster, jedoch keinen eigenständig bestätigten Produktivitätsnachweis.

**Übertragbare Verfahren:**

- Aufgaben über einen Router in Lifecycle-Skills und spezialisierte Personas leiten.
- Projekt-Constraints mit exaktem Prüfkommando, Laufzeit, Begründung und befristeter Ausnahme dokumentieren.
- Bestehende Qualitätsdefizite als gemessene Baseline ratcheten statt dauerhaft rote Gates einzuführen.
- Externe, projektnahe und agenteneigene Prüfungen nach ihrer Unabhängigkeit unterscheiden.
- Risiken und fehlgeschlagene Prüfungen in autonomen Build-Schleifen als Haltepunkte behandeln.

**Voraussetzungen:** Vollständige gemeinsame references und passende Host-Adapter. Projektbezogene echte Prüfkommandos und verantwortliche Freigabe für neue Gates oder Abhängigkeiten.

**Weitere Grenzen und Voraussetzungen der Aussage:** Markdown-Regeln sind keine technische Durchsetzung. Beispielgrenzen wie Coverage oder Mutation Score sind keine allgemein passenden Standards. Der gelesene Skill-Impact-Nachweis enthält nur eine leere Ledger-Vorlage und belegt keine Wirkung.

**Abgleich mit dem Index:** Keine wesentliche strukturelle Abweichung; leeres Impact-Ledger schränkt Wirksamkeitsansprüche zusätzlich ein.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/addyosmani/agent-skills/README.md>) · [skills/constraint-driven-development/SKILL.md](<../external_repos/addyosmani/agent-skills/skills/constraint-driven-development/SKILL.md>) · [evals/skill-impact.md](<../external_repos/addyosmani/agent-skills/evals/skill-impact.md>)

#### R03 · bmad-code-org/BMAD-METHOD

[GitHub](https://github.com/bmad-code-org/BMAD-METHOD) · Revision: `61e01f82644c4bb533750cfa0d6d61ab61d2cc9b` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

BMAD-METHOD verbindet Anforderungen, Planung, Umsetzung und Reviews durch explizite Rollen und Arbeitsverträge. Der untersuchte Stand ist eine V7-Vorschau; die README trennt sie von der stabilen v6.12-Linie. Besonders übertragbar ist die Wahl der Planungstiefe: Ein kleiner, klar verstandener Eingriff braucht keinen vollständigen Dokumentapparat, während mehrere Stakeholder oder parallele Entwicklungsströme von PRD und Architekturentscheidungen profitieren. Autonome Builds erhalten eine begrenzte Einheit, eine Baseline und unveränderliche Intent-Kriterien. Der äußere Orchestrator bleibt für Priorisierung und Checkpoints verantwortlich. Gebaut bedeutet ausdrücklich noch nicht abgeschlossen. Blockaden, Review-Nichtkonvergenz und Lücken im Auftrag haben definierte Ausgänge; bei Intent-Lücken wird die Arbeit gesichert und zurückgesetzt. Dieser Vertrag ist für die Factory wichtiger als die Zahl der Rollen. Die Vorschau verlangt Integrations- und Migrationsprüfung; ein lokaler Lauf wurde nicht ausgeführt.

**Übertragbare Verfahren:**

- Planung richtet sich nach Klarheit der Absicht, Umfang und Risiken statt einem Pflichtstapel von Dokumenten.
- Intent-Verträge halten Ergebnis, Invarianten und Nichtziele fest; PRD und Architektur dienen konkreten Koordinationsproblemen.
- Ein autonomer Build arbeitet an einer klar begrenzten Einheit; ein äußerer Orchestrator verantwortet Auswahl und menschliche Checkpoints.
- Baseline-Revision und strukturierte Endzustände unterscheiden gebaut, blockiert und abgeschlossen.
- Bei Intent-Lücken wird ein Patch gesichert und die Umsetzung zurückgesetzt; wiederholt erfolglose Reviews haben einen Abbruchpunkt.

**Voraussetzungen:** Preview: unterstützter Skill-Host, Python und uv; stabile Linie dokumentiert Node 20.12+ und Python 3.10+. Definierte Absicht, passende Schreibrechte und für autonome Schleifen Subagents.

**Weitere Grenzen und Voraussetzungen der Aussage:** Preview Alpha mit Breaking Changes; keine Garantie einer fertigen universellen Factory. bmad-loop übernimmt laut gelesener Dokumentation noch keine komplette Ticketbaum-Dispatchlogik. Der Build kann committen; Push und übergeordnete Freigaben bleiben getrennt. Keine Durchführung oder gemessene Verbesserung in dieser Analyse.

**Abgleich mit dem Index:** Preview-/Stable-Abgrenzung bestätigt; der Index nennt viele Module, von denen hier nur Build, Planung und autonome Schleifen vertieft gelesen wurden.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/bmad-code-org/BMAD-METHOD/README.md>) · [skills/bmad-build/SKILL.md](<../external_repos/bmad-code-org/BMAD-METHOD/skills/bmad-build/SKILL.md>) · [docs/plan/choose-a-planning-path.md](<../external_repos/bmad-code-org/BMAD-METHOD/docs/plan/choose-a-planning-path.md>) · [docs/build/autonomous-development-loops.md](<../external_repos/bmad-code-org/BMAD-METHOD/docs/build/autonomous-development-loops.md>)

#### R04 · bradygaster/squad

[GitHub](https://github.com/bradygaster/squad) · Revision: `51a14e0f4dfac525e0727c448c88df392e76f042` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Squad macht aus flüchtigen Einzelchats ein persistentes Team mit Rollen, Entscheidungen, Verlauf und optionalem Issue-Monitoring. Seine nützlichsten Details betreffen Koordination: Jeder Agent bekommt einen ausdrücklich aufgelösten Team-Root; lokale Worktree-Zustände und ein geteilter Hauptcheckout haben unterschiedliche Parallelitätsrisiken. Bei einer leeren Antwort kontrolliert der Koordinator zunächst die Arbeitsergebnisse. Archivierung soll erst nach überprüftem Schreiben in ein versioniertes Ziel entfernen und Einträge statt bloßer Bytes zählen. Ein Circuit Breaker kann bei Rate Limits auf andere Modelle wechseln und später die Erholung testen. Die Vorlagen sind jedoch nicht vollständig konsistent: Eine beschreibt Scribe-Commits, eine andere reserviert Persistenz für State-Tools. Experimentelle Backends und Auto-Approval im Einstieg brauchen eigene Prüfung. Der statische Befund unterstützt Koordinationsmethoden, keine pauschale Betriebssicherheit oder Produktivitätszusage.

**Übertragbare Verfahren:**

- Rollen, Entscheidungen und Verlauf werden als expliziter Teamzustand von einzelnen Chats getrennt.
- Ein bekannter Team-Root wird an jeden Agenten übergeben; Worktree-lokaler und gemeinsam genutzter Zustand werden unterschieden.
- Leere Agentenantworten werden gegen tatsächlich erzeugte Dateien geprüft, statt sofort erneut zu starten.
- Archivierung schreibt zuerst in ein versioniertes Ziel, prüft Überschriften und Eintragszahlen und entfernt erst danach den Ursprung.
- Circuit Breaker wechselt bei Rate Limits in einen konfigurierten Modell-Fallback und prüft die Erholung nach Cooldown.
- Autonome Retro-Umsetzung ist opt-in und an genaue Revisionen, Pfade und erneute Berechtigungsprüfung gebunden.

**Voraussetzungen:** Node 22.5+, npm 10+, Git und je Client passende Zugänge; Funktionen unterscheiden sich nach Host. Sauber definierter Teamzustand und Worktree-Strategie.

**Weitere Grenzen und Voraussetzungen der Aussage:** Experimentelle SDK-/Harness-Teile sind keine produktiv abgenommene Laufzeit. Shared-State im Hauptcheckout ist laut Vorlage bei parallelen Sessions unsicher. Vorlagen widersprechen sich: Worktree-Referenz lässt Scribe committen, die neuere After-Agent-Referenz verbietet eigene Git-Mutationen zugunsten State-Tools. Append-only/union-Merges vermeiden nicht automatisch semantische Widersprüche; Modellkostenangaben sind datierte Dokumentaussagen.

**Abgleich mit dem Index:** Persistenz und experimentelle Backends bestätigt. Vertiefte Vorlagen zeigen widersprüchliche Zuständigkeit für State-Commits; diese Spannung fehlt im Index.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/bradygaster/squad/README.md>) · [templates/after-agent-reference.md](<../external_repos/bradygaster/squad/templates/after-agent-reference.md>) · [templates/worktree-reference.md](<../external_repos/bradygaster/squad/templates/worktree-reference.md>) · [templates/ralph-circuit-breaker.md](<../external_repos/bradygaster/squad/templates/ralph-circuit-breaker.md>)

#### R05 · cursor/plugins

[GitHub](https://github.com/cursor/plugins) · Revision: `99b609a72323b70204eab407c622f436e858e112` · README-Vertrag; Skill-/Playbook-Vertrag; kein eigener Lauf

Im Cursor-Plugin-Monorepo ist lokal vor allem pstack ausgecheckt. Der Root-Katalog nennt zusätzliche Integrationen, deren Implementierung damit nicht untersucht wurde. pstack verbindet einen Aufgabenrouter mit Playbooks, Architekturprinzipien und getrennten Rollen für Umsetzung und Urteil. Besonders übertragbar ist sein Generator für projektspezifische Verification-Skills: Start, Zustandsdiagnose, tatsächliche Bedienung, Belege und Cleanup werden als konkrete Kommandos und Benutzerwege beschrieben. Eine Feature Map verhindert, dass nur der bequemste Einstieg geprüft wird. Nachweise müssen die Handlung und ihre Seiteneffekte zeigen und das Aufräumen überleben. Das Eval-Playbook verlangt isolierte Umgebungen, neutrale Bezeichnungen und ein verblindetes Urteil; tatsächlich gelesene Dateien sollen aus Transkripten statt aus Selbstberichten ermittelt werden. Umfangreiche Autonomie- und Modellvorgaben bleiben fremde Arbeitsverträge. Für eine Übernahme müssen Berechtigungen, Kosten und verfügbare Host-Funktionen passend begrenzt werden.

**Übertragbare Verfahren:**

- Aufgabentypen unterscheiden und zur passenden Untersuchung, Umsetzung oder Betriebsbeobachtung leiten.
- Datenform und Verantwortungsgrenzen vor verstreuter Logik festlegen.
- Projektbezogene Verification-Skills mit Launch, Doctor, Drive, Evidence und Cleanup erstellen.
- Echte Benutzerwege samt Seiteneffekten und nach Cleanup erhaltenem Beleg prüfen.
- Varianten in isolierten, neutral benannten Umgebungen mit verblindetem Urteil vergleichen.
- Wiederkehrende Lektionen bevorzugt in Architektur, Typen und ausführbaren Gates verankern.

**Voraussetzungen:** Cursor- oder kompatibler Adapter; verschiedene Funktionen benötigen cursor-team-kit oder Cursor-spezifische Dienste. Explizite Berechtigungen für reale Werkzeuge, Instanzen, PRs und externe Aktionen.

**Weitere Grenzen und Voraussetzungen der Aussage:** Sparse Checkout enthält nicht sämtliche im Root-Katalog genannten Plugins. Großzügige Autonomieregeln des fremden Skills sind keine Autorisierung für dieses Repo. Multi-Modell-Konsens ist keine unabhängige Wahrheit; Aufwand und Korrelation bleiben. README lehnt Planung als Default ab, obwohl mehrphasige Arbeit eigene Plan-Playbooks erhält.

**Abgleich mit dem Index:** Root-README beschreibt einen viel größeren Marktplatz als den lokal ausgecheckten pstack-Ausschnitt; Index benennt diese Einschränkung korrekt.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/cursor/plugins/README.md>) · [pstack/README.md](<../external_repos/cursor/plugins/pstack/README.md>) · [pstack/skills/poteto-mode/SKILL.md](<../external_repos/cursor/plugins/pstack/skills/poteto-mode/SKILL.md>) · [pstack/skills/create-verification-skill/SKILL.md](<../external_repos/cursor/plugins/pstack/skills/create-verification-skill/SKILL.md>) · [pstack/skills/poteto-mode/playbooks/eval.md](<../external_repos/cursor/plugins/pstack/skills/poteto-mode/playbooks/eval.md>)

#### R06 · garrytan/gstack

[GitHub](https://github.com/garrytan/gstack) · Revision: `749a2382750ef742a7345ee270ab3416c0715b6e` · README-Vertrag; eigener Metrikbericht; statischer Hook-Code; kein eigener Lauf

gstack verbindet spezialisierte Rollen mit Artefakten, Browserbedienung und technischen Hilfsprogrammen. Für die Factory sind besonders die Aktualität von Reviews, an den Arbeitsbaum gebundene Prüfbelege und begrenzte explorative QA interessant. Eine Zeitgrenze beendet dabei weitere Prüfhandlungen, beweist aber nicht, dass bereits angenommene externe Anfragen keine Wirkung mehr entfalten. Der gelesene Stop-Hook führt ausschließlich ein zuvor gehashtes und als vertrauenswürdig gespeichertes Prüfkommando aus. Nach mehreren fehlgeschlagenen Wiedereinstiegen lässt er den Turn dennoch mit einer ausdrücklichen roten Warnung enden. Das schützt gegen Endlosschleifen und ist kein unverletzbares Qualitätsgate. Garry Tans großer historischer SLOC-Vergleich bleibt ein Selbstbericht mit Greenfield-, Baseline- und Qualitätsgrenzen. Host-Fähigkeiten unterscheiden sich deutlich. Automatische Zweitmodell-Reviews übertragen relevante Inhalte an einen weiteren Anbieter; ein Egress-Ledger macht Übertragungsversuche nachvollziehbar, ersetzt aber keine Netzwerkgrenze.

**Übertragbare Verfahren:**

- Produktklärung, technische Planung, Umsetzung, Review und QA mit nachvollziehbaren Artefaktübergaben verbinden.
- Belege an den tatsächlichen Arbeitsbaum binden und Aktualität separat bewerten.
- Explorative QA mit echten Benutzerwegen, vorherigen Hypothesen und ausführbaren Zeitgrenzen führen.
- Hooks nur für exakt gehashte vertrauenswürdig erklärte Kommandos aktivieren.
- Externe Übertragungen mit widerrufbaren Einstellungen und Belegen sichtbar machen.
- Selbstbericht, statische Prüfung und unabhängigen Laufzeitnachweis unterscheiden.

**Voraussetzungen:** Passender Host und Bun; Browser-/Security-Funktionen benötigen zusätzliche Plattform- und Toolchain-Voraussetzungen. Authentifizierte zweite Modell-CLI für Outside Reviews; explizite Daten- und Aktionsrechte.

**Weitere Grenzen und Voraussetzungen der Aussage:** 810-facher SLOC-Tagesdurchsatz ist eigener historischer Vergleich und kein kausaler Produktivitäts- oder Qualitätsbeweis. Hook-Sperren sind bei vielen Hosts nur Hinweise; selbst beim Claude-Stop-Gate erfolgt nach begrenzten roten Wiederholungen Freigabe mit Warnung. Vertrauensfreigabe bleibt agentenseitig aufrufbar und dient Unfallvermeidung, nicht Schutz vor entschlossenem Angreifer. Hashketten erkennen nicht die vollständige Löschung oder Endkürzung eines Ledgers. Updates und Zweitmodell-Reviews sind laut README standardmäßig aktiv, Telemetrie dagegen opt-in.

**Abgleich mit dem Index:** Keine wesentliche Abweichung; Detaillektüre präzisiert den begrenzten Stop-Hook und die Schwäche des SLOC-Vergleichs.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/garrytan/gstack/README.md>) · [docs/ON_THE_LOC_CONTROVERSY.md](<../external_repos/garrytan/gstack/docs/ON_THE_LOC_CONTROVERSY.md>) · [docs/reference-qa-deadlines.md](<../external_repos/garrytan/gstack/docs/reference-qa-deadlines.md>) · [bin/gstack-verify-gate](<../external_repos/garrytan/gstack/bin/gstack-verify-gate>)

#### R07 · github/spec-kit

[GitHub](https://github.com/github/spec-kit) · Revision: `67e0f7294e6e728ab60bf7b4590deb470448bc2d` · README-Vertrag; Methodik-/Command-Vorlagen; kein eigener Lauf

Spec Kit behandelt Spezifikation, Plan und Aufgaben als versionierte Eingaben der Umsetzung. Seine aktuelle README bietet zusätzlich unabhängige Prozesse für Bugfixes und Ideenbewertung; der vollständige Feature-Ablauf ist damit keine Pflicht für jede Aufgabe. Der konkrete Nutzen liegt in stabilen Anforderungs-IDs, expliziten Akzeptanzkriterien und der Verbindung von fachlicher Absicht zu technischen Entscheidungen. Analyze prüft die Konsistenz der Dokumente, während Converge den aktuellen Code dagegen bewertet. Fehlende, teilweise erfüllte, widersprüchliche und unangeforderte Arbeit erhalten getrennte Befunde. Korrekturen werden als neue Aufgaben angehängt; eine abgehakte Checkbox zählt ausdrücklich nicht als Nachweis. Das passt zu einer nachvollziehbaren Factory. Die ältere Methodik behauptet allerdings eine vollständige Aufhebung der Spezifikationslücke und enthält pauschale Architekturpflichten. Diese Aussagen gehen über die belegte Funktion der Vorlagen hinaus. Geschäftserfolg und technische Konvergenz bleiben getrennte Bewertungen.

**Übertragbare Verfahren:**

- Warum und Was einer Anforderung von technischer Umsetzung trennen.
- Anforderungen, Akzeptanzkriterien, Planentscheidungen und Tasks über stabile IDs nachverfolgen.
- Inkonsistenzen zwischen Spezifikation, Plan und Tasks vor Umsetzung lesen.
- Konvergenz am tatsächlichen Code prüfen und fehlende, teilweise, widersprüchliche oder unangeforderte Arbeit unterscheiden.
- Korrekturaufgaben append-only ergänzen und abgeschlossene Checkboxen nicht als Beweis anerkennen.
- Nachgelagerte Geschäftsergebnisse von jetzt baubaren Verpflichtungen trennen.

**Voraussetzungen:** Python 3.11+, uv und passender Agent; projektspezifische Constitution. Prüfung installierter Erweiterungen und ihrer ausführbaren Hooks.

**Weitere Grenzen und Voraussetzungen der Aussage:** Methodik verspricht eliminierte Spezifikationslücke; Prompt-basierte Transformation ist kein Beweis ihrer Eliminierung. Ältere Methodik nennt pauschale Library-/CLI-Pflichten, während aktuelle README projektangepasste Prozesse betont. Converged bedeutet bewertete Übereinstimmung im erfassten Scope, nicht unabhängige Laufzeit- oder Marktabnahme. Read-only-Analyse kann registrierte Hooks auslösen; Reichweite des Schreibschutzes muss im Host geklärt bleiben.

**Abgleich mit dem Index:** Keine strukturelle Abweichung; zwischen weitreichenden Methodikversprechen und konkret begrenzten Konvergenzkommandos besteht eine wichtige Spannung.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/github/spec-kit/README.md>) · [spec-driven.md](<../external_repos/github/spec-kit/spec-driven.md>) · [templates/commands/converge.md](<../external_repos/github/spec-kit/templates/commands/converge.md>) · [templates/commands/analyze.md](<../external_repos/github/spec-kit/templates/commands/analyze.md>)

#### R08 · humanlayer/skills

[GitHub](https://github.com/humanlayer/skills) · Revision: `653b6411c1f70c275a18e37673b042ff99f67ceb` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

HumanLayers Skills verbinden dokumentierte Entwicklungsphasen mit dem Entwurf wiederkehrender Agentenschleifen. RPI nutzt lokale Artefakte, Repo-Revisionen und standardmäßig frische Kontexte; Recherche, Designgespräch, PRD und Technical Design lassen sich passend auswählen. TDD bezeichnet hier den technischen Entwurf. Besonders nützlich ist der Regelkreis aus Zielwert, Sensor, Auswahlcontroller, Aktor und Störungen. Seine Komponenten sollen zuerst eigenständig lokal funktionieren; CI orchestriert anschließend dieselben Befehle. Ein dauerhaftes Feedbackdokument und eine begrenzte Zahl offener PRs halten Menschen in der Steuerung. Dabei zählt die genaue Verdrahtung: Feedback wird nach dem Controller an den Aktor geladen und beeinflusst einen deterministischen Selektor deshalb nicht automatisch. Manuelle Läufe umgehen das standardmäßige PR-Limit. Diese Details machen aus einer allgemeinen Autonomieidee einen überprüfbaren Betriebsvertrag; eingerichtet oder ausgeführt wurde hier nichts.

**Übertragbare Verfahren:**

- RPI übergibt nummerierte lokale Dokumente mit Repo-SHA zwischen frischen Phasen und kann bestehende Arbeit fortsetzen.
- Recherchefragen, Designgespräch, PRD, Technical Design und Implementierungsoutline sind wählbare Pfade.
- Regelkreis trennt Zielwert, Sensor, Auswahlcontroller, Agentenaktor und Störungen.
- Sensor, Controller und Aktor zuerst einzeln lokal ausführbar machen, CI als dünne Orchestrierung ergänzen.
- Dauerhaftes Reviewerfeedback lädt jeder Lauf; eine offene PR je Schleife begrenzt standardmäßig die Arbeit.
- Optionales Regressiongate verhindert neue Verschlechterungen während schrittweiser Verbesserung.

**Voraussetzungen:** Definierte Qualitätsziele, Scope, existierende Validierung sowie Agenten-/CI-Zugänge für spätere Umsetzung. Beschreibbare Artefakte und bewusst gewählte Phasen.

**Weitere Grenzen und Voraussetzungen der Aussage:** TDD meint hier Technical Design, nicht Test Driven Development. Memory wird nach dem Controller in den Aktorkontext geladen; daher ändert Feedback allein nicht zwangsläufig einen deterministischen Auswahlcontroller. Manuelle Workflow-Ausführung umgeht das dokumentierte Open-PR-Limit; Schleifen benötigen bewusste Kontrolle. Anweisungen zum Push oder Schedule sind Quellmaterial und wurden nicht ausgeführt.

**Abgleich mit dem Index:** Grundzweck und Risiken bestätigt; die genaue Ladereihenfolge von Feedback und der manuelle WIP-Bypass ergänzen die Indexgrenzen.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/humanlayer/skills/README.md>) · [plugins/rpi/skills/rpi/SKILL.md](<../external_repos/humanlayer/skills/plugins/rpi/skills/rpi/SKILL.md>) · [plugins/design-control-loop/skills/design-control-loop/SKILL.md](<../external_repos/humanlayer/skills/plugins/design-control-loop/skills/design-control-loop/SKILL.md>)

#### R09 · karpathy/autoresearch

[GitHub](https://github.com/karpathy/autoresearch) · Revision: `228791fb499afffb54b46200aca536f79142f117` · README-Vertrag; Experimentanweisung; statischer Bewertungs-Code; kein eigener Lauf

Autoresearch zeigt eine bewusst kleine Experimentarchitektur: Der Agent verändert ausschließlich train.py, während Datenaufbereitung, Tokenizer und Bewertungsfunktion unverändert bleiben sollen. Jeder Versuch trainiert unter demselben fünfminütigen Trainingsbudget und wird anhand von Validation Bits per Byte bewertet. Baseline, akzeptierte Änderungen, verworfene Ideen und Abstürze erhalten einen nachvollziehbaren Eintrag. Vereinfachungen dürfen auch ohne besseren Score gewinnen. Für die Factory ist das ein klares Muster für begrenzte Optimierung mit überprüfbarem Zustand. Seine Grenzen sind ebenso wesentlich: Vorbereitung, Kompilierung, Evaluation und Agentenarbeit liegen außerhalb des Trainingsbudgets. Die Ergebnisse gelten für die verwendete Hardware. Der wiederholt verwendete Validierungsshard ist kein unangetasteter Abschlussdatensatz. Außerdem verhindert eine Markdown-Regel technisch weder eine Manipulation noch einen unbegrenzten Gesamtverbrauch. Ein produktiver Experimentvertrag benötigt daher zusätzliche Isolation, unabhängige Abschlussbewertung und ein ausdrücklich begrenztes Gesamtbudget.

**Übertragbare Verfahren:**

- Eine einzige Änderungsdatei vom festen Daten- und Bewertungsapparat trennen.
- Unveränderte Baseline vor dem ersten Experiment messen.
- Pro Versuch Hypothese, Commit, Ergebnis, Speicherbedarf und keep/discard/crash protokollieren.
- Verbesserungen gegen Komplexitätskosten abwägen und Vereinfachung bei Gleichstand bevorzugen.
- Misserfolge aufzeichnen und Zustand kontrolliert zurücksetzen.

**Voraussetzungen:** Eine NVIDIA-GPU, laut Projekt auf H100 getestet, Python und uv. Vorbereitete Trainingsdaten und Tokenizer; isolierte Experimentumgebung mit begrenztem Gesamtbudget.

**Weitere Grenzen und Voraussetzungen der Aussage:** Fünf Minuten gelten nur für Training; Startup, Kompilierung, Evaluation und Agentenarbeit kommen hinzu. Ergebnisse gelten für Hardware und Budget des Laufs und sind nicht plattformübergreifend vergleichbar. Wiederholte Optimierung auf denselben Validierungsshard birgt adaptive Überanpassung; separater finaler Holdout wird nicht gezeigt. Die textliche Unveränderlichkeitsregel ist keine Betriebssystem-Isolation; train.py kontrolliert das Modell und erhält Evaluationsdaten über den Aufruf. Die Endlosschleife hat im Basisvertrag kein globales Kosten- oder Versuchslimit.

**Abgleich mit dem Index:** Keine wesentliche Abweichung; feste Trainingszeit ist kein festes Ende-zu-Ende-Zeitbudget.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/karpathy/autoresearch/README.md>) · [program.md](<../external_repos/karpathy/autoresearch/program.md>) · [prepare.py](<../external_repos/karpathy/autoresearch/prepare.py>)

#### R10 · mattpocock/skills

[GitHub](https://github.com/mattpocock/skills) · Revision: `5beb35b040e3de97e54fa9e386d7e42d15c295c2` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Matt Pococks Sammlung setzt auf kleine, kombinierbare Engineering-Praktiken und gemeinsame Fachsprache. Der gelesene Architektur-Skill bewertet tiefe Module danach, wie viel Verhalten eine kleine erlernbare Schnittstelle erschließt und wie lokal Wissen, Fehler und Änderungen bleiben. TDD prüft beobachtbares Verhalten an vereinbarten Schnittstellen; erwartete Ergebnisse sollen aus unabhängigen Beispielen oder Spezifikationen stammen. Vertikale Red-Green-Schritte vermeiden Tests einer nur vorgestellten Gesamtimplementierung. Das Code-Review trennt Standards und Anforderungserfüllung in unabhängige Kontexte und Berichte. Repo-Regeln übersteuern allgemeine Geruchsheuristiken. Eine dokumentierte Spannung bleibt: Die README spricht von Red-Green-Refactor, während der aktuelle TDD-Skill Refactoring aus dem Loop in die Reviewphase verlegt. Die Sammlung ist damit ein anpassbares Methodenangebot, dessen konkrete Regeln und Übergaben bewusst zusammengesetzt werden müssen.

**Übertragbare Verfahren:**

- User-invoked Orchestrierung von model-invoked Disziplin trennen.
- Standards und Spec unabhängig seit festgehaltenem Merge-Base prüfen und getrennt berichten, damit gutes Stilurteil fehlende Anforderungen nicht maskiert.
- Repo-Regeln haben Vorrang vor Code-Smell-Heuristiken; von Tools bereits geprüfte Punkte nicht erneut als manuelle Findings aufblasen.
- Tests prüfen Verhalten an vorab vereinbarten öffentlichen Seams mit unabhängigen erwarteten Werten.
- Vertikale Red-Green-Slices halten Rückmeldung eng; keine komplette horizontale Testschicht vor imaginierter Implementierung.
- Modultiefe über Nutzen pro erlernter Schnittstelle, Locality und Deletion-Test beurteilen, nicht Zeilenzahl.

**Voraussetzungen:** Bekannte Standards, Spezifikation, Tracker und Prüfschnittstellen; für getrennte Reviewkontexte Subagents. Passender Installationsweg, um doppelte Skills durch Plugin plus Kopie zu vermeiden.

**Weitere Grenzen und Voraussetzungen der Aussage:** README nennt Red-Green-Refactor, aktueller TDD-Skill verlegt Refactoring ausdrücklich in die Reviewphase; Versions-/Lehrmeinungsspannung. TDD lehnt Tests interner Seams pauschal ab, Codebase-Design erlaubt interne Seams für eigene Modultests; Kontext muss geklärt werden. Kleine Skills vermindern Prozesszwang, benötigen aber bewusste Zusammenstellung und gemeinsame Vokabeln.

**Abgleich mit dem Index:** Review-Trennung und modulare Struktur bestätigt. Neue genaue Spannung zwischen README-Red-Green-Refactor und TDD-Regel ohne Refactoring im Loop erfasst.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/mattpocock/skills/README.md>) · [skills/engineering/code-review/SKILL.md](<../external_repos/mattpocock/skills/skills/engineering/code-review/SKILL.md>) · [skills/engineering/tdd/SKILL.md](<../external_repos/mattpocock/skills/skills/engineering/tdd/SKILL.md>) · [skills/engineering/codebase-design/SKILL.md](<../external_repos/mattpocock/skills/skills/engineering/codebase-design/SKILL.md>)

#### R11 · msitarzewski/agency-agents

[GitHub](https://github.com/msitarzewski/agency-agents) · Revision: `b37b5bb33b78f2c1d6567d98e25ca818e3259219` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Agency-agents liefert eine umfangreiche Rollenbibliothek, deren Nutzen vor allem in expliziten Verantwortlichkeiten, Lieferobjekten und wiederkehrenden Arbeitsabläufen liegt. Der gelesene Multi-Agent-Architekt behandelt Koordination wie ein verteiltes System: Verträge, begrenzte Rechte, Teilfehler, Checkpoints, Idempotenz und Kostenkontrolle gehören zusammen. Der Research Synthesist warnt zutreffend davor, vielfach zitierte Ursprünge als unabhängige Evidenz zu zählen. Andere Rollen zeigen deutliche Schwächen. Der Reality Checker unterstellt automatisch unzureichende Erstversionen und verlangt visuelle Belege auch für nicht visuell nachweisbare Eigenschaften. Eine Sicherheitsregel behauptet zudem fälschlich, injizierte Anweisungen könnten kein gültiges JSON ergeben. Damit illustriert die Sammlung, warum Personas einzeln geprüft werden müssen: Erfahrung, Erinnerung, Produktionsreife und Fachautorität sind zunächst Promptformulierungen. Technische Berechtigungsgrenzen, tatsächliche Evaluation und menschliche Verantwortung entstehen erst durch die konkrete Umgebung. Gelesen wurden die vollständige README und drei methodentragende Definitionen.

**Übertragbare Verfahren:**

- Rollen als Verantwortung, Eingabe-/Ausgabevertrag, erlaubte Tools und Fehlerverhalten beschreiben.
- Topologie nach Abhängigkeit wählen und Fan-in bei vollständigen, partiellen oder fehlenden Resultaten ausdrücklich definieren.
- Kontextzustand, Pflichtfelder, Checkpoints, Idempotenz und Recovery wie in verteilten Systemen entwerfen.
- Agenten- und Pipelineevals sowie Kosten, Latenz, Eskalation und Fehlerzustände getrennt beobachten.
- Forschung nach Primärursprung, Unabhängigkeit, Methodengüte und Evidenzlücken gewichten.
- Ergebnisbehauptungen mit tatsächlichen Artefakten, Nutzerwegen und Messdaten abgleichen.

**Voraussetzungen:** Gezielte Auswahl passender Personas statt pauschaler Installation aller Rollen. Technisch durchgesetzte Berechtigungen, Isolation und Zustandsverwaltung außerhalb der Prompttexte. Fachspezifische Prüfung von Codebeispielen, Heuristiken und regulierten Aussagen.

**Weitere Grenzen und Voraussetzungen der Aussage:** Personabezeichnung und behauptete Erfahrung/Memory erzeugen keine reale Expertise oder dauerhafte Gedächtnisfunktion. README wirbt mit immer erfolgreicher und produktionsreifer Arbeit ohne unabhängigen Gesamtnachweis. Die Behauptung, injizierte Anweisungen könnten kein gültiges JSON erzeugen, ist falsch; Schemas verhindern semantische Prompt-Injection nicht. Reality Checker verlangt pauschal Fehler, Revisionen und Screenshots für jedes Systemclaim; das fördert Negativbias und kann nicht visuelle Eigenschaften nicht belegen. Mindestzahlen für Evals, maximale Agentenzahlen und Konfidenzschwellen sind unbelegte Ausgangsheuristiken. Sicherheits-, Finanz-, medizinische oder Compliance-Personas sind keine fachliche Zertifizierung.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/msitarzewski/agency-agents/README.md>) · [engineering/engineering-multi-agent-systems-architect.md](<../external_repos/msitarzewski/agency-agents/engineering/engineering-multi-agent-systems-architect.md>) · [testing/testing-reality-checker.md](<../external_repos/msitarzewski/agency-agents/testing/testing-reality-checker.md>) · [research/research-synthesist.md](<../external_repos/msitarzewski/agency-agents/research/research-synthesist.md>)

#### R12 · multica-ai/andrej-karpathy-skills

[GitHub](https://github.com/multica-ai/andrej-karpathy-skills) · Revision: `2c606141936f1eeef17fa3043a72095b4765b9c2` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Karpathy-Inspired Guidelines ist ein kompaktes Verhaltensdokument eines Drittanbieters. Es verbindet vier Regeln: Annahmen sichtbar machen, einfache Lösungen wählen, bestehende Projekte chirurgisch ändern und Erfolg überprüfbar definieren. Praktisch bedeutet das, dass jede Diffzeile auf den Auftrag zurückführbar sein soll und nur neu entstandene verwaiste Bestandteile nebenbei entfernt werden. Ein Bugfix wird an einem reproduzierbaren Fehler gemessen, ein Refactoring am vorher und nachher überprüften Verhalten. Die Stärke liegt in der Kürze und der Anschlussfähigkeit an Projektroutinen. Das Dokument liefert jedoch keine Werkzeuge oder gemessenen Resultate und ist nicht von Karpathy selbst betrieben. Seine Vorsicht braucht Augenmaß: Ein offensichtlicher Tippfehler verlangt keine vollständige Anforderungszerlegung. Als gemeinsame Grundhaltung passt es zu kleinen Skills und begrenzten Entwicklungsaufträgen.

**Übertragbare Verfahren:**

- Annahmen und Interpretationsalternativen vor Umsetzung sichtbar machen.
- Kleinste verlangte Lösung ohne spekulative Konfiguration oder Einmalabstraktion wählen.
- Jede Diffzeile auf den Auftrag zurückführen und nur durch eigene Änderungen verwaisten Code entfernen.
- Aufträge in überprüfbare Erfolgskriterien und kurze Schritt–Check-Paare übersetzen.

**Voraussetzungen:** Projektspezifische Regeln und vorhandene Prüfbefehle ergänzen. Triviale Arbeiten bewusst leichter behandeln.

**Weitere Grenzen und Voraussetzungen der Aussage:** Von Dritten aus Karpathy-Beobachtungen abgeleitet; kein von Karpathy betriebenes Framework. Normative Promptregeln, keine empirisch geprüfte Verbesserung. Vorsicht und Rückfragen können Arbeit verlangsamen; unmögliche Fehlerfälle oder unnötige Abstraktionen bleiben Urteilsfragen.

**Abgleich mit dem Index:** Einzeldokument mit mehreren Distributionsformaten bestätigt; wertende Motivzuschreibungen des Index werden nicht als Befund übernommen.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/multica-ai/andrej-karpathy-skills/README.md>) · [CLAUDE.md](<../external_repos/multica-ai/andrej-karpathy-skills/CLAUDE.md>)

#### R13 · obra/superpowers

[GitHub](https://github.com/obra/superpowers) · Revision: `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` · README-Vertrag; drei vollständige Skill-Verträge; kein eigener Lauf

Superpowers verbindet Intentklärung, kleinteilige Planung, testgetriebene Umsetzung und systematische Diagnose. Die gelesene Delegationsmethode setzt einen frischen Implementierer pro Aufgabe ein und übergibt nur den konkreten Brief, notwendige Schnittstellen und globale Grenzen. Ein dauerhaftes Ledger verhindert, dass nach Kontextverlust bereits erledigte Arbeit erneut gestartet wird. Task-Reviews prüfen Spezifikation und Qualität; ein späteres Gesamtbranch-Review betrachtet die Integration. Der tatsächliche Anfangscommit wird vor der Arbeit festgehalten, damit mehrteilige Aufgaben nicht auf den letzten Commit verkürzt werden. Bei Fehlern folgt zunächst Reproduktion und Ursachenanalyse mit einer einzelnen Hypothese. Die Methodik enthält aber bewusste Kosten- und Schleifengrenzen: Inline-Ausführung ist günstiger, und Befunde dürfen nach einem Limit mit begründetem Ruling offen bleiben. Eine abgeschlossene Aufgabe kann daher dokumentierte Restarbeit enthalten. Prosa-Regeln ersetzen weder technische Sperren noch passende Aktionsrechte.

**Übertragbare Verfahren:**

- Frische Implementierer mit engem Aufgabenbrief statt vollständiger Gesprächshistorie einsetzen.
- Planbezogenes Ledger und eindeutige Artefaktverzeichnisse zur Wiederaufnahme verwenden.
- Task-Review auf Spezifikation und Qualität richten und danach den Gesamtbranch prüfen.
- Reviewpaket über den vorab erfassten tatsächlichen Commitbereich erstellen.
- Ursachenanalyse über Reproduktion, Grenzinstrumentierung, einzelne Hypothese und minimale Probe führen.
- Abschlussbehauptung an konkret passenden frischen Beleg binden.

**Voraussetzungen:** Passender Host mit aktivem Bootstrap; für delegierten Pfad Subagenten und isolierter Workspace. Explizite Autorisierung für Commits und externe Seiteneffekte, die fremde Methodik selbst nicht erteilt.

**Weitere Grenzen und Voraussetzungen der Aussage:** Delegierter Pfad ist teurer als Inline-Pfad; kleine Aufgaben brauchen nicht dieselbe Zeremonie. Verifikationsskill verlangt frischen Lauf, Task-Reviewer soll denselben Lauf nicht wiederholen; Wiederverwendungsregeln müssen konsistent auf denselben Inhalt begrenzt werden. Reviewbefunde können am Iterationslimit mit dokumentiertem Ruling geparkt werden; complete bedeutet dann nicht befundfrei. Drei fehlgeschlagene Fixes rechtfertigen Überprüfung der Grundannahmen, beweisen aber für sich keinen Architekturfehler. Strenge Prosa und Anti-Rationalisierungs-Tabellen sind keine unverletzbare technische Sperre.

**Abgleich mit dem Index:** Keine wesentliche Abweichung; Fertigmeldungen können explizit geparkte Restbefunde enthalten.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/obra/superpowers/README.md>) · [skills/subagent-driven-development/SKILL.md](<../external_repos/obra/superpowers/skills/subagent-driven-development/SKILL.md>) · [skills/verification-before-completion/SKILL.md](<../external_repos/obra/superpowers/skills/verification-before-completion/SKILL.md>) · [skills/systematic-debugging/SKILL.md](<../external_repos/obra/superpowers/skills/systematic-debugging/SKILL.md>)

#### R14 · open-gsd/gsd-core

[GitHub](https://github.com/open-gsd/gsd-core) · Revision: `7129a135c7271ccea59df7561df83ac11cbc94bd` · README-Vertrag; drei vollständige Kontext-/Phasen-/Shipping-Dokumente; kein eigener Lauf

GSD Core strukturiert längere Arbeit in Discuss, Plan, Execute, Verify und Ship. Entscheidungen, Recherche, Aufgaben und Verifikation leben als lesbare Dateien außerhalb des laufenden Gesprächs. Dadurch können neue Agentenkontexte eine klar begrenzte Aufgabe übernehmen, während der Hauptkontext die Koordination behält. Gute Phasen besitzen ein präzises Ziel und wenige unabhängige Pläne; für triviale Änderungen bietet das System bewusst leichtere Wege. Besonders übertragbar ist die Frischeprüfung von Verifikationsberichten über Inhaltsfingerprints der tatsächlich abgedeckten Dateien. Nach Änderungen wird ein früheres Passed als stale behandelt. Grenzen bleiben sichtbar: Kontextgrößen und Hook-Fähigkeiten hängen vom Host ab, und Headroom ist eine Schätzung. Die gelesene Shipping-Anleitung führt Code-Review als optional auf. Ihr UAT-Beispiel wertet sogar eine leere Antwort als bestanden. Solche konkreten Abschlussverträge müssen vor Übernahme an die eigenen Zustimmungs- und Qualitätsregeln angepasst werden.

**Übertragbare Verfahren:**

- Entscheidungen, Recherche, Plan, Umsetzung und Verifikation als getrennte Artefakte persistieren.
- Hauptkontext als schlanken Orchestrator führen und schwere Aufgaben klar begrenzt verteilen.
- Unabhängige Arbeit nach Abhängigkeiten in Wellen gruppieren.
- Anforderungs- und Entscheidungsabdeckung getrennt von bloßem Testabschluss prüfen.
- Verifikation mit Inhaltsfingerprints versehen und nach relevanten Änderungen als stale behandeln.
- Für triviale Aufgaben ausdrücklich leichtere Quick-/Fast-Pfade anbieten.

**Voraussetzungen:** Kompatibler Installer und unterstützter Host; Datei-Artefakte vor Übergabe vollständig speichern. Geeigneter Phasenscope und reale Verifikationsmöglichkeiten.

**Weitere Grenzen und Voraussetzungen der Aussage:** 200k-Kontext und vollständige Context-Rot-Lösung sind dokumentierte Architekturannahmen, keine universelle Hostgarantie. Headroom-Messung bleibt Heuristik und Hooks verursachen Pflegeaufwand. UAT-Anleitung zählt auch leere Antwort als pass; fehlende Antwort darf nicht allgemein als Zustimmung interpretiert werden. Code-Review ist laut gelesener Shipping-Anleitung optional und läuft nicht automatisch. Byte-Fingerprints können durch Zeilenendungsunterschiede stale werden.

**Abgleich mit dem Index:** Index beschreibt neuere und detailliertere Runtime-Mechanismen; gelesene Grundlagendokumente enthalten noch pauschale200k-/Parallelitätsannahmen.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/open-gsd/gsd-core/README.md>) · [docs/explanation/context-engineering.md](<../external_repos/open-gsd/gsd-core/docs/explanation/context-engineering.md>) · [docs/explanation/the-phase-loop.md](<../external_repos/open-gsd/gsd-core/docs/explanation/the-phase-loop.md>) · [docs/how-to/verify-and-ship.md](<../external_repos/open-gsd/gsd-core/docs/how-to/verify-and-ship.md>)

#### R15 · OthmanAdi/planning-with-files

[GitHub](https://github.com/OthmanAdi/planning-with-files) · Revision: `dcdfb278de53fdb69b2067ea173dbb1de45345a3` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Planning with Files macht laufende Aufgaben über drei Dateien wiederaufnehmbar: task_plan.md hält Phasen und nächsten Schritt, findings.md Erkenntnisse, progress.md den Arbeitsverlauf. Übertragbar sind eindeutige Planbindung, Formatprüfung, ein verantwortlicher Schreiber und Recovery aus Projektdateien. Native Plugins liefern je nach Host andere Hooks und Abschluss-Gates als eine reine Skill-Installation. Attestierung bedeutet hier Inhaltsgleichheit zu einer lokalen Digest-Baseline; ein Agent mit Schreibrechten auf Plan und Baseline kann sie ersetzen. Sie ist daher kein unabhängiger Genehmigungsnachweis. Ebenso beweisen Phasenstatus und Warnungen keine tatsächliche Fertigstellung. Die veröffentlichten Evals müssen getrennt gelesen werden: Im internen Vergleich vom Juli 2026 schlossen alle Methoden sämtliche 77 Läufe erfolgreich ab; Unterschiede betrafen Aktivierung, Wiederaufnahme und Aufwand. Der historische Vorteil von fünf Wiederaufnahme-Turns wurde mit Transkript-Catchup gemessen und gilt ausdrücklich nicht als Nachmessung der aktuellen automatischen File-only-Recovery.

**Übertragbare Verfahren:**

- Drei getrennte Zustände führen: Phasen und nächsten Schritt im Plan, belegte Erkenntnisse in Findings, ausgeführte Schritte und Fehler im Fortschrittslog; langfristiges Wissen anschließend ausdrücklich kuratieren.
- Mehrere Vorhaben über explizite Planbindung und isolierte Verzeichnisse trennen; bei Mehrdeutigkeit keinen zufälligen Plan wählen und bei Parallelität nur einen Planbesitzer schreiben lassen.
- Planformat vor Nutzung rein lesend validieren; konkrete Phasen und genau ein nativer Status je Phase sind Voraussetzung für verwertbare Abschlussprüfungen.
- Wiederaufnahme zuerst aus Projektdateien; optionale Session-Metadaten und begrenztes Transkript-Replay bewusst separat aktivieren und als untrusted Kontext behandeln.
- Injektionen nur bei Änderungen wiederholen, dabei Ziel, aktuellen Schritt und aktive Phasen sichtbar halten; Hook-Integration und Plugin gegenüber bloßer Skill-Installation unterscheiden.
- Veröffentlichte Evals nach Prozessbefolgung, Aufgabenrichtigkeit, Triggerwahrscheinlichkeit, Wiederaufnahme und Kosten auseinanderhalten.

**Voraussetzungen:** Passende native Host-Integration; Bash und Python für zahlreiche Hook-Pfade, kein gleichwertiger reiner PowerShell-Injektionspfad. Eindeutige Projekt- und Planbindung, gültiges Format und expliziter Umgang mit erlaubten Planänderungen. Zuverlässiges persistentes Dateisystem; Dateien und Attestierungs-Baseline müssen für Sicherheitsannahmen außerhalb untrusted Schreibrechte liegen.

**Weitere Grenzen und Voraussetzungen der Aussage:** Der Attestierungs-Digest ist unkeyed und lokal ersetzbar; er belegt Inhaltsgleichheit zu einer gespeicherten Baseline, keine menschliche Genehmigung oder Sicherheit gegen einen schreibberechtigten Agenten. Abschluss-Gates beruhen auf agentisch gepflegten Statuswerten und begrenzten Follow-ups; Warnungen bei parallelen Änderungen sind weder Sperre noch Merge-Verfahren. Claude-PreCompact-stdout erzwingt keinen Modell-Flush. Die 96,7%-gegen-6,7%-Angabe bewertet überwiegend die verlangte Planstruktur. Der interne Vergleich von 2026-07-06 erreichte mit allen sieben Armen 77/77 Aufgabenabschlüsse; die 5,0 Wiederaufnahme-Turns des historischen v3.4.0 mit Transkript-Catchup messen nicht das heutige File-only-Default. Nur zwei unforced Aufgaben, kleine Wiederholungszahlen und harness-eigene Aufgaben; Rohläufe des Wettbewerbsvergleichs liegen laut Dokument außerhalb dieses Repos. Neuere Defaults wurden nicht unter demselben Protokoll nachgemessen. Die Darstellung exklusiver Recovery-Garantien geht über die gemessenen Fälle hinaus; naive dateibasierte Regeln triggerten im internen Vergleich häufiger als das Skill. Strukturierte Planung erhöhte bei kleinen Aufgaben Aufwand und Kosten.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/OthmanAdi/planning-with-files/README.md>) · [skills/planning-with-files/SKILL.md](<../external_repos/OthmanAdi/planning-with-files/skills/planning-with-files/SKILL.md>) · [SECURITY.md](<../external_repos/OthmanAdi/planning-with-files/SECURITY.md>) · [docs/evals.md](<../external_repos/OthmanAdi/planning-with-files/docs/evals.md>)

#### R16 · paperclipai/paperclip

[GitHub](https://github.com/paperclipai/paperclip) · Revision: `50797ea03ce0b2a84e4df80864ac6e3652382ed5` · README-Vertrag; drei vollständige Heartbeat-/Budget-/Approval-Dokumente; kein eigener Lauf

Paperclip verlagert die Koordination mehrerer Agenten in eine dauerhafte Control Plane. Aufgaben erhalten Ziele, Verantwortliche, Kontext, Ergebnisse und nachvollziehbare Statuswechsel. Der Heartbeat-Vertrag beginnt mit Identität und Zuweisung, verlangt einen atomaren Checkout und behandelt einen Konflikt als bereits vergebene Arbeit. Längere Delegation nutzt Kindaufgaben und spätere Weckereignisse. Das reduziert Polling und hält Verantwortung sichtbar. Für Freigaben ist die Bindung an eine konkrete Planrevision besonders relevant: Eine spätere Änderung oder ein neuer Benutzerkommentar kann eine alte Bestätigung ungültig machen. Prozessstatus, fachlicher Aufgabenstatus und semantischer Fortschritt bleiben getrennt. Budgets pausieren künftige Arbeit anhand des gemeldeten Verbrauchs; laufende oder verspätet gemeldete Nutzung kann das Limit überschreiten. Firmenhierarchie und Dashboard sind damit Koordinationsmittel, kein Beweis erreichter Geschäftsziele. Datenexporte, Verbindungsrechte und standardmäßig aktive Telemetrie benötigen eigene Betriebseinstellungen.

**Übertragbare Verfahren:**

- Zielhierarchie und Elternaufgaben mit konkreten Arbeitsergebnissen verbinden.
- Aufgaben atomar auschecken und409Konflikt als fremde Zuständigkeit behandeln.
- Lang delegierte Arbeit durch Kindaufgaben und Ereignisse statt dauerndes Polling koordinieren.
- Issue-Status, Prozesswiederherstellung und semantische Run-Liveness getrennt modellieren.
- Planbestätigung an exakte Revision und Idempotency-Key binden und bei neuem Kommentar veralten lassen.
- Kosten über aufgezeichnete Nutzung zurechnen und Budgetpausen als Schedulerentscheidung ausweisen.

**Voraussetzungen:** Node24.11+, PostgreSQL bzw eingebettete Instanz, passende Agent-Runtimes und Credentials. Konfigurierte Firmen-, Benutzer-, Agenten- und Verbindungsrechte.

**Weitere Grenzen und Voraussetzungen der Aussage:** Budgetstopps basieren auf gemeldetem Verbrauch und können durch laufende Arbeit verzögert wirken. Organisationsmetapher und Dashboard garantieren keine Geschäftsziele. Export lässt referenzierte Secrets weg, kann aber normale Env-Werte und lokale Pfade enthalten. Telemetrie standardmäßig aktiv; Monitoring-Exporter optional. pnpm test umfasst laut README keine Playwright-Tests.

**Abgleich mit dem Index:** Keine wesentliche Abweichung; Budgetdokumentsatz jeden Token erfassen ist durch README-Verbrauchsmeldegrenze eingeschränkt.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/paperclipai/paperclip/README.md>) · [docs/guides/agent-developer/heartbeat-protocol.md](<../external_repos/paperclipai/paperclip/docs/guides/agent-developer/heartbeat-protocol.md>) · [docs/guides/board-operator/costs-and-budgets.md](<../external_repos/paperclipai/paperclip/docs/guides/board-operator/costs-and-budgets.md>) · [docs/guides/agent-developer/handling-approvals.md](<../external_repos/paperclipai/paperclip/docs/guides/agent-developer/handling-approvals.md>)


### Skills, Regeln und Vertrauensprüfung

#### R17 · affaan-m/ECC

[GitHub](https://github.com/affaan-m/ECC) · Revision: `90606c8315ee09cafc303515c5f33024db6b9882` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

ECC ist eine breite Referenz für die Verbindung von Planung, TDD, Review, Verifikation und dauerhaftem Kontext. Die vollständig gelesene README unterscheidet native Integrationen von begrenzten Adaptern; gleiche Funktionsabdeckung wird ausdrücklich nicht versprochen. Besonders übertragbar sind verwaltete Installationen mit Besitzmanifest und reversibler Pflege sowie die Trennung von bedarfsgeladenen Skills und ständig geladenen Regeln. Der Memory-Skill behandelt gespeicherte Inhalte ausdrücklich als ungeprüfte Belege: Git-Versionierung oder passender Hash machen daraus keine aktuelle Wahrheit und keine Handlungsfreigabe. Der Eval-Skill trennt Fähigkeiten von Regressionen sowie einen Erfolg unter mehreren Versuchen von durchgehender Stabilität. Eine entscheidende Grenze steht im Detail: Kandidatenausführung bleibt auf allen Betriebssystemen deaktiviert, weil kein verifizierter Containment-Backend vorhanden ist. Receipts bestätigen somit Artefaktintegrität, keine sichere Ausführung. Die iterative Suche bietet zusätzlich ein Verfahren, fehlenden Kontext in begrenzten Runden zu ergänzen. Diese Aussagen sind Dokumentverträge, keine eigene Laufprüfung.

**Übertragbare Verfahren:**

- Plan–Test–Implement–Review–Verify als Kette mit Nachweisartefakten.
- Installationen über Besitzmanifest, Dry Run, Doctor, Repair und Uninstall verwalten; verschiedene Kanäle nicht stapeln.
- Memory als create-only unreviewed Kontext speichern; Scopes, Empfängerfilter und Autorisierung unterscheiden.
- Capability- und Regressionsevals sowie pass@k und pass^k trennen; Kandidatenausführung mangels geprüfter OS-Isolation deaktiviert.
- Kontextsuche über Dispatch, Bewertung konkreter Lücken und begrenzte Verfeinerung führen.
- Skills bedarfsgerecht, Regeln selektiv und Harnessadapter mit eigener Fähigkeitsmatrix behandeln.

**Voraussetzungen:** Node18+ für Core; je Harness passende CLI und gesonderte Hook-Trustentscheidung. MemoryVault-CLI benötigt eigene Runtime; optionale Features benötigen Bash/Python oder weitere geprüfte Runner.

**Weitere Grenzen und Voraussetzungen der Aussage:** NativeWindows-Memory-/Observerdefekte und begrenzte Adapterparität ausdrücklich dokumentiert. README-Kosteneinsparungen und starre80ProzentCoverage sind Heuristiken. Evalreceipts und statische Warnungen sind keine Containment- oder Promotionsevidenz; Gate scheitert absichtlich geschlossen.

**Abgleich mit dem Index:** Grundbeschreibung und71/311/97 stimmen. Vertiefung ergänzt die entscheidende Sperre aller Eval-Kandidatenausführung und präzise Memory-Vertrauensgrenzen; Index-Pilotkennzahlen wurden nicht zusätzlich nachgeprüft.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/affaan-m/ECC/README.md>) · [skills/unified-memory/SKILL.md](<../external_repos/affaan-m/ECC/skills/unified-memory/SKILL.md>) · [skills/eval-harness/SKILL.md](<../external_repos/affaan-m/ECC/skills/eval-harness/SKILL.md>) · [skills/iterative-retrieval/SKILL.md](<../external_repos/affaan-m/ECC/skills/iterative-retrieval/SKILL.md>)

#### R18 · alirezarezvani/claude-skills

[GitHub](https://github.com/alirezarezvani/claude-skills) · Revision: `6d2f02ea077eead1bee5411a31bcc6db5a11a70c` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Die Sammlung alirezarezvani/claude-skills verbindet zahlreiche Fachskills mit Rollenprofilen und einem ausdrücklichen Übergabeprotokoll. Übertragbar ist vor allem die Trennung zwischen der Rolle eines Agenten, dem benötigten Fachwissen und dem konkreten Arbeitsauftrag. Die vertieften Dokumente machen zwei Qualitätsmechanismen greifbar: Regressionsevaluationen vergleichen mehrere saubere Durchläufe pro Fall, unterscheiden mindestens einen Erfolg von verlässlichem Erfolg in allen Versuchen und berücksichtigen kritische Einzelregressionen. Die Gedächtnisarchitektur trennt rohe Ereignisse, Kandidaten, projektbezogenes Wissen und stabile übergreifende Regeln. Vorschläge werden vor ihrer dauerhaften Übernahme gestagt; Konflikte sollen sichtbar bleiben. Diese Mechanismen sind dokumentierte Arbeitsverträge, keine von uns ausgeführten Nachweise. Kleine Stichproben und bloße Wiederholung liefern weiterhin keine Wahrheitsgarantie. Widersprüchliche Mengenangaben sowie die pauschale Behauptung konfliktfreier Skill-Kombinationen sprechen dafür, wenige passende Bausteine auszuwählen und ihre gemeinsamen Anweisungen separat zu prüfen.

**Übertragbare Verfahren:**

- Rolle, Fachskill und ausführenden Task-Agenten getrennt modellieren; Phasenwechsel mit Entscheidungen, Artefakten und offenen Punkten übergeben.
- Regressionen über mehrere saubere Trials pro Fall, Ergebnis- und bei Bedarf Pfadgrader sowie verbotene Aktionen beurteilen.
- Pass@k und Pass^k unterscheiden; gepaarte Fallvergleiche, Konfidenzintervalle und kritische Einzelregressionen in Release-Gates berücksichtigen.
- Vier Gedächtnisstufen mit unterschiedlicher Injektion, expliziter Promotion, Herkunft und Widerspruchsbehandlung verwenden.
- Gedächtnisvorschläge zunächst stagen und erst durch menschliche Annahme in dauerhaft injizierte Dateien übernehmen.

**Voraussetzungen:** Passende Skills und Rollendefinitionen gezielt auswählen und an den jeweiligen Agentenadapter anpassen. Evals benötigen extern erzeugte Rollouts, belastbare Sollfälle und für statistische Aussagen ausreichend viele gepaarte Fälle. Gedächtnispromotion benötigt menschliche Prüfung und eigene Regeln für Geheimnisse und widersprüchliche Aussagen.

**Weitere Grenzen und Voraussetzungen der Aussage:** README-Zahlen zu Skills, Scripts und Referenzen widersprechen sich; Umfang ist kein Qualitätsbeleg. Die Aussage, Skills kollidierten nicht, ist für frei kombinierte Anweisungen nicht nachgewiesen. Nicht signifikante Regressionen bei kleinen Stichproben belegen keine Gleichwertigkeit. Wiederholung und Alter einer Gedächtnisaussage ersetzen keinen Wahrheitsnachweis; Redaktionsfilter können sensible Daten übersehen. Nur README und drei zentrale Dokumente vollständig gelesen; dokumentierte Evaluationsskripte wurden weder gelesen noch ausgeführt.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/alirezarezvani/claude-skills/README.md>) · [orchestration/ORCHESTRATION.md](<../external_repos/alirezarezvani/claude-skills/orchestration/ORCHESTRATION.md>) · [engineering/agent-regression-evals/skills/agent-regression-evals/SKILL.md](<../external_repos/alirezarezvani/claude-skills/engineering/agent-regression-evals/skills/agent-regression-evals/SKILL.md>) · [engineering/agent-memory/skills/agent-memory/SKILL.md](<../external_repos/alirezarezvani/claude-skills/engineering/agent-memory/skills/agent-memory/SKILL.md>)

#### R19 · anthropics/claude-code

[GitHub](https://github.com/anthropics/claude-code) · Revision: `318b7e6ac4e726e88a4ad326214866a93c373b1b` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Anthropics öffentliches Claude-Code-Repository eignet sich zum Studium von Integrationsmustern, weil es Dokumentation, Plugins und Hooks enthält; die eigentliche CLI-Engine liegt darin nicht offen. Der gelesene Review-Befehl sucht erhebliche Fehler und Regelverstöße mit mehreren Rollen und validiert Fundkandidaten vor der Ausgabe. Der vollständig gelesene Sicherheits-Hook verbindet schnelle Musterwarnungen mit späterer Diff-Analyse. Besonders lehrreich sind präzise Git-Basen, die Bindung an tatsächlich erzeugte Commit-SHAs sowie Zustände für ausstehende, übersprungene und bereits behandelte Prüfungen. Gleichzeitig zeigen die Grenzen, warum ein Hook kein Sicherheitsnachweis ist: API-Ausfälle, Dateigrenzen, Priorisierung, begrenzte Wiederholungen und Deduplikation reduzieren die Abdeckung. Commit- und Push-Reviews laufen nach den Aktionen. Als geprüft markierte Bereiche können zudem priorisierte Teilmengen enthalten. Für eigene Abläufe sollten deshalb Prüfumfang, erfolgreicher Prüflauf und vorgelagerte Freigabe getrennt dokumentiert werden.

**Übertragbare Verfahren:**

- Review zunächst auf relevante Regeln, konkrete Änderung und erhebliche Fehler begrenzen, anschließend Kandidaten unabhängig validieren.
- Lokale Reviewausgabe und ausdrücklich angefordertes Veröffentlichen eines PR-Kommentars getrennt behandeln.
- Schnelle Musterwarnungen bei Dateiänderungen mit späterer modellgestützter Diff-Analyse kombinieren.
- Änderungsbasis pro Nutzerturn erfassen und ausstehende ungeprüfte Änderungen bei vorübergehenden Fehlern erhalten.
- Commits über tatsächliche SHA und Pushes über überprüfte Ref-/Bereichsgrenzen analysieren; bereits geprüfte zusammenhängende Präfixe deduplizieren.
- Übersprungene Prüfungen, abgeschnittene Dateien, API-Fehler und begrenzte Review-Schleifen als eigene Telemetrie führen.

**Voraussetzungen:** Installierte Claude-Code-Laufzeit und passende Plugin-/Hook-Konfiguration. Für modellgestützte Sicherheitsanalyse API-Zugang und weitere importierte Hilfsbibliotheken. Git-Basis, Dateipfade und Hook-Ereignisse müssen zum tatsächlich untersuchten Repository passen.

**Weitere Grenzen und Voraussetzungen der Aussage:** Der öffentliche Bestand enthält nicht den proprietären CLI-Kern. Die statisch gelesene Sicherheits-Hauptdatei importiert weitere nicht geprüfte Module. Viele Pfade überspringen Prüfungen bei Grenzen oder Fehlern; Teilmengenpriorisierung kann Dateien auslassen. Commit-/Push-Reviews finden nach der Git-Aktion statt und sind daher kein vorgelagertes Freigabegate. Ein Push-Bereich kann nach priorisierter Teilprüfung als geprüft markiert werden; dieser Zustand belegt keine vollständige Sicherheitsabdeckung. Alte Kommentare nennen andere Modellabläufe als der gegenwärtige Code; Warnungszählung ist keine belastbare Sicherheitsmessung.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/anthropics/claude-code/README.md>) · [plugins/code-review/commands/code-review.md](<../external_repos/anthropics/claude-code/plugins/code-review/commands/code-review.md>) · [plugins/security-guidance/hooks/security_reminder_hook.py](<../external_repos/anthropics/claude-code/plugins/security-guidance/hooks/security_reminder_hook.py>)

#### R20 · anthropics/skills

[GitHub](https://github.com/anthropics/skills) · Revision: `dbd4588f9e1033efb41dad4bef2f7947c8993d44` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Anthropics Skills-Sammlung liefert ein Format und konkrete Entwicklungspraktiken für wiederverwendbare Arbeitsanweisungen. Der gelesene Skill Creator behandelt Skills als überprüfbare Intervention: realistische Aufgaben auswählen, eine Version entwerfen, gegen eine Baseline laufen lassen, Ergebnisse anhand von Assertions und menschlicher Bewertung prüfen und anschließend gezielt verbessern. Metadaten dienen der Auslösung; längere Anleitungen, Varianten und Ressourcen werden gestuft geladen. Aussagekräftige Vergleiche berücksichtigen Tokens, Laufzeit, Streuung und Aufgaben, die beide Varianten ohnehin lösen. Die Triggeroptimierung verwendet ähnliche Negativfälle; ihr Testanteil beeinflusst allerdings die Auswahl der besten Beschreibung und ist deshalb kein vollständig unabhängiger Abschlussnachweis. Für Übernahmen zählt die Lizenz pro Ordner: Die Dokument-Skills sind source-available. Die Sammlung ist methodisch nützlich, beweist jedoch weder identische Produktfunktionen noch die Kompatibilität eines fremden Hosts.

**Übertragbare Verfahren:**

- Kurze Metadaten mit präziser Beschreibung steuern die Auslösung; Details und Varianten werden bei Bedarf geladen.
- Realistische Aufgaben werden mit und ohne Skill beziehungsweise gegen die alte Version parallel verglichen.
- Maschinelle Assertions werden durch menschliche Bewertung und optional verblindete Vergleiche ergänzt.
- Timing, Tokens, Streuung und nicht unterscheidende Tests gehören zur Auswertung.
- Trigger-Evaluation nutzt positive und schwer ähnliche negative Fälle sowie getrennte Datenanteile.

**Voraussetzungen:** Ein Host mit Agent-Skills-Unterstützung; für vollständige Evaluation Subagents und lokale Hilfswerkzeuge. Pro Verzeichnis die tatsächliche Lizenz und verfügbare Werkzeuge prüfen.

**Weitere Grenzen und Voraussetzungen der Aussage:** docx, pdf, pptx und xlsx sind source-available und ausdrücklich keine allgemein Apache-lizenzierten Beispiele. Die Auswahl der besten Triggerbeschreibung anhand des Testanteils schwächt dessen Rolle als unberührte Abschlussprüfung. Ohne Subagents entfallen echte Vergleichsläufe; vereinfachte Plattformvarianten dürfen nicht als gleichwertiger Nachweis gelten.

**Abgleich mit dem Index:** Lizenzgrenze und Demonstrationscharakter bestätigt. Die vertiefte Lektüre ergänzt den konkreten Skill-Evaluationskreislauf; API-Referenzen aus dem Index wurden hier nicht vollständig geprüft.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/anthropics/skills/README.md>) · [skills/skill-creator/SKILL.md](<../external_repos/anthropics/skills/skills/skill-creator/SKILL.md>)

#### R21 · davila7/claude-code-templates

[GitHub](https://github.com/davila7/claude-code-templates) · Revision: `9416faad8aa9111a467069e4b5f29766c1d2a388` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Claude Code Templates bündelt viele Agenten, Commands, Hooks, MCPs und Skills und ergänzt sie durch Installation, Monitoring und Verwaltungsoberflächen. Als Referenz sind die Trennung der Komponententypen, gezielte Auswahl sowie Backup- und Merge-Angebote nützlich. Die gelesene Review-Vorlage verlangt konkrete Fundstellen, Risiken und Lösungsvorschläge und passt die Lesetiefe an die Diff-Größe an. Der Installer zeigt zugleich, warum eine Erfolgsmeldung sorgfältig interpretiert werden muss: Er lädt vom beweglichen main-Branch und akzeptiert bereits teilweise erfolgreiche Downloads. Der untersuchte Security-Audit-Einstieg durchsucht nur bestimmte Markdown-Kategorien, lässt Skills aus und beendet außerhalb des CI-Modus auch fehlerhafte Prüfungen mit Exit 0. Das begrenzt die Aussage eines grünen Prozesses. Übernommene Drittquellen behalten ihre Lizenzen. Für die Factory ist der Katalog ein Suchraum, dessen einzelne Komponenten separat geprüft werden müssen.

**Übertragbare Verfahren:**

- Komponententypen und einzelne Auswahl reduzieren die Übernahme kompletter Konfigurationen.
- Installer unterstützt Backup, Merge und Abbruch bei bestehenden Dateien.
- Review-Vorlage skaliert die Lesetiefe nach Diff-Größe und verlangt Fundstelle, Risiko und konkrete Lösung.
- Security-Audit kann im CI bei fehlgeschlagenen Prüfungen abbrechen.
- Download-Retries verwenden Backoff und melden übersprungene Komponenten.

**Voraussetzungen:** Node/npm und passender Claude-Code-Host; Netzwerkausführung und Komponenten einzeln prüfen. Eigene Lizenzen aggregierter Drittquellen beachten.

**Weitere Grenzen und Voraussetzungen der Aussage:** Der gelesene Installer lädt vom beweglichen main-Branch und wertet schon mindestens einen erfolgreichen Dateidownload als Installationserfolg. Audit scannt nur Markdown in agents, commands, mcps, settings und hooks; skills und Nicht-Markdown sind darin nicht enthalten. Außerhalb CI meldet das Audit auch bei Failed-Komponenten Exit 0; erfolgreicher Prozess ist daher kein Gütesiegel. Review-Agent besitzt Schreib-/Bash-Werkzeuge und pauschale Stilregeln; die Rollenbezeichnung allein garantiert keinen reinen Lesezugriff.

**Abgleich mit dem Index:** Katalog- und Drittquellencharakter bestätigt. Statische Vertiefung zeigt Teilinstallation als Erfolg und begrenzte Reichweite des ausgewählten Audit-Einstiegs; neuere Catalog-API und Injection-Fixes des Index wurden nicht als Vollcodeaudit überprüft.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/davila7/claude-code-templates/README.md>) · [cli-tool/components/agents/development-tools/code-reviewer.md](<../external_repos/davila7/claude-code-templates/cli-tool/components/agents/development-tools/code-reviewer.md>) · [cli-tool/src/file-operations.js](<../external_repos/davila7/claude-code-templates/cli-tool/src/file-operations.js>) · [cli-tool/src/security-audit.js](<../external_repos/davila7/claude-code-templates/cli-tool/src/security-audit.js>)

#### R22 · docker/skills

[GitHub](https://github.com/docker/skills) · Revision: `179c9cfd04c89ae50cd5d5d68b939797a8fd03d3` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Docker/skills zeigt eine klare Verbindung zwischen Fachwissen, versioniertem Katalog und mehreren Verteilungswegen. Besonders aufschlussreich sind die vollständig gelesenen Sandbox-Skills: Ein schreibbarer Bind-Mount lässt den Agenten trotz MicroVM direkt am Hostbestand arbeiten; ein privater Clone schützt diesen Bestand, benötigt aber eine spätere Übernahme der Änderungen. Read-only schützt vor Schreiben und verbirgt keine Geheimnisse. Netzwerkfreigabe, Credential-Injektion und Tokenrechte sind getrennte Kontrollen. Auch ein Sentinel hindert den Agenten nicht daran, erlaubte API-Rechte auszuüben; OAuth-Passthrough kann sogar echte Tokens offenlegen. Vor dem Entfernen einer Clone-Sandbox muss ungefetchte Arbeit gesichert werden. Diese präzisen Grenzen sind für jede Agentenumgebung nützlich. Die README trennt zudem statische Validierung von echten Agentenevals. Die dokumentierten Fähigkeiten wurden hier weder installiert noch ausgeführt; experimentelle Formate und Unterschiede zwischen Quellstand und installierter CLI bleiben versionsabhängig.

**Übertragbare Verfahren:**

- Kanonische Skillquelle, Katalog, erzeugte Übersichten und Host-Manifeste getrennt pflegen und Versionen reproduzierbar pinnen.
- Statische Struktur-/Snippet-Prüfung ausdrücklich von lebenden Agentenevaluationen unterscheiden.
- Workspace-Schreibzugriff durch Auswahl zwischen Bind-Mount und privatem Clone bewusst festlegen.
- Netzwerkzugang, Credential-Injektion und Tokenrechte unabhängig begrenzen und ihre tatsächlich wirksame Policy prüfen.
- OAuth-Passthrough und dynamische Host-Credential-Auflösung als eigene Vertrauensgrenzen behandeln.
- Vor Sandbox-Löschung ungefetchte Arbeit sichern und destruktive Operationen eng eingrenzen.

**Voraussetzungen:** Passende Docker-Produkte; Standalone-sbx und Docker-Agent-Sandbox sind unterschiedliche Schnittstellen. Clone-Isolation setzt ein normales Git-Repository mit echtem .git-Verzeichnis voraus. Netzwerk- und Credential-Store müssen passend zum installierten Versionsstand eingerichtet sein.

**Weitere Grenzen und Voraussetzungen der Aussage:** MicroVM-Isolation schützt keine absichtlich schreibbar eingebundenen Hostdateien. Read-only verhindert Schreiben, verbirgt aber keine Geheimnisse. Credential-Sentinels verhindern nicht den Missbrauch erlaubter API-Rechte; OAuth-Passthrough kann echte Tokens sichtbar machen. Hostname-Allow-Regeln werden laut Skill nicht gegen CIDR-Deny der aufgelösten IP geprüft. Experimentelle Schemas und source-only CLI-Abweichungen erfordern Versionsprüfung. Die dokumentierte Isolation wurde von uns nicht ausgeführt oder unabhängig verifiziert.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/docker/skills/README.md>) · [skills/docker-sandboxes-lifecycle/SKILL.md](<../external_repos/docker/skills/skills/docker-sandboxes-lifecycle/SKILL.md>) · [skills/docker-sandboxes-network-credentials/SKILL.md](<../external_repos/docker/skills/skills/docker-sandboxes-network-credentials/SKILL.md>) · [skills/docker-destructive-guardrails/SKILL.md](<../external_repos/docker/skills/skills/docker-destructive-guardrails/SKILL.md>)

#### R23 · intellectronica/ruler

[GitHub](https://github.com/intellectronica/ruler) · Revision: `3c0520f36234ba646c0d612bd363d010b2beab20` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Ruler behandelt Agentenkonfigurationen als Projektionen einer kanonischen Quelle unter .ruler. Regeln werden in festgelegter Reihenfolge mit Herkunftskommentaren verbunden; Skills, MCPs und experimentelle Subagenten werden in zielabhängige Formate übertragen. Das reduziert doppelte Pflege, löst aber keine inhaltlichen Widersprüche in den Regeln. Besonders relevant sind Ownership-Manifeste für erzeugte Dateien, das Erhalten fremder nativer Dateien sowie Dry-run, Backup und Drift-Prüfung in CI. Die Plattformunterschiede bleiben sichtbar: Tool-Listen, Read-only-Verhalten, Modelle und Hintergrundausführung sind nicht überall gleich übersetzbar; Tool-Permissions ersetzen keine Betriebssystem-Sandbox. Wer generierte Dateien ignoriert, muss sie in neuen Worktrees erneut erzeugen. Für Subagenten fehlt ein eigener Revert-Vertrag. Das Repo ist deshalb vor allem eine Referenz für nachvollziehbare Konfigurationsverteilung mit bewusst dokumentierten Verlusten bei der Übersetzung.

**Übertragbare Verfahren:**

- Regeln mit deterministischer Reihenfolge und Herkunftskommentaren zusammenführen.
- CLI vor TOML vor Defaults priorisieren; lokale/global gefundene Regeln und experimentelle Unterbereiche explizit unterscheiden.
- Konfiguration je Zieladapter übersetzen; unbekannte Tools oder nicht unterstützte Fähigkeiten diagnostizieren.
- Generierte Subagentdateien per Ownership-Manifest verwalten und fremde native Dateien bei Kollision erhalten.
- Dry-run und Backups für breite Konfigurationsänderungen anbieten; CI kann Drift zwischen kanonischer Quelle und committed Projektionen erkennen.

**Voraussetzungen:** Node ^20.19 oder ^22.12 oder >=23 laut README; passende native Agentformate und gewünschte Zielauswahl. Entscheidung, ob generierte Anweisungen committed oder bei jedem frischen Worktree neu erzeugt werden.

**Weitere Grenzen und Voraussetzungen der Aussage:** Konkatenation löst inhaltliche Regelwidersprüche und Kontextbudgetprobleme nicht. Tools, readonly und Hintergrundausführung werden je Harness unterschiedlich oder gar nicht abgebildet. Subagents besitzen noch kein explizites revert; manuelle Änderungen an verwalteten Dateien werden überschrieben. OpenCode-Permissions sind keine OS-Sandbox; Beta/experimentelle Features und README-Beispiele können driften.

**Abgleich mit dem Index:** Index weitgehend bestätigt. README-Artefaktbeispiel für CI prüft teilweise .codex/skills statt des dokumentierten .agents/skills; die Reproduzierbarkeit von Beispielpfaden sollte separat geprüft werden. Statischer RuleProcessor bestätigt Herkunftsmarker und Konkatenation.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/intellectronica/ruler/README.md>) · [src/core/RuleProcessor.ts](<../external_repos/intellectronica/ruler/src/core/RuleProcessor.ts>)

#### R24 · midudev/autoskills

[GitHub](https://github.com/midudev/autoskills) · Revision: `2dbab03b41988327e5c714d3fb233ebbce915e8c` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Autoskills verbindet Technologieerkennung mit einer kuratierten Skill-Registry. Sein übertragbares Muster lautet: vorprüfen, paketieren, Dateien und Bundle verifizieren und die Herkunft anschließend im Lockfile festhalten. Der Installer nutzt eine kanonische Ablage und projiziert sie durch Symlinks oder Kopien auf mehrere Agenten. Downloads sind begrenzt parallel und bleiben auch beim Fallback auf main an erwartete Hashes gebunden. Das ist eine Integritätskontrolle gegenüber dem Manifest, keine Garantie guter Anweisungen. Der gelesene lokale Kopierpfad zeigt eine zusätzliche Grenze: Er prüft gelistete Dateien, kopiert danach aber rekursiv das Verzeichnis, sodass zusätzliche unmanifestierte Dateien gesondert geprüft werden müssten. Refresh kann vorhandene Anpassungen ersetzen. Die README nennt eine nichtkommerzielle Lizenz. Für die Factory ist das Beschaffungsmuster nützlicher als die automatische Übernahme eines ganzen Skill-Stacks.

**Übertragbare Verfahren:**

- Upstream-Prüfung vor der Installation in eine kuratierte Registry verlagern.
- Dateihashes und sortierten Bundle-Hash vor Schreiben gegen mitgeliefertes Manifest prüfen.
- Quelle und Bundle-Identität in skills-lock.json festhalten.
- Kanonischen Skill unter .agents/skills anlegen und andere Hostpfade verlinken beziehungsweise kopieren.
- Cache anhand der Bundle-Identität wiederverwenden und parallele Downloads global begrenzen.

**Voraussetzungen:** Node 22.6+, passende Registry und bewusst ausgewählte Agentziele. Projekt- und komponentenspezifische Übernahmeprüfung; README nennt CC BY-NC 4.0.

**Weitere Grenzen und Voraussetzungen der Aussage:** Integrität gegenüber einem Manifest beweist weder Gutartigkeit noch Qualität der bereits freigegebenen Inhalte. AI-Triage ist keine unabhängige Sicherheitsabnahme. Lokaler/cachebasierter Pfad verifiziert nur gelistete Dateien und kopiert anschließend rekursiv das gesamte Verzeichnis; zusätzliche unmanifestierte Dateien können damit mitkopiert werden. Refresh entfernt existierenden Skillordner; eigene Anpassungen und parallele Lockfile-Schreibungen benötigen separate Behandlung.

**Abgleich mit dem Index:** Kuratiertes Hash-/Lockfile-Muster bestätigt. Code-Fallback auf main bleibt hashgebunden; lokale rekursive Kopie ist enger zu prüfen als die pauschale Aussage every file verified.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/midudev/autoskills/README.md>) · [packages/autoskills/installer.ts](<../external_repos/midudev/autoskills/packages/autoskills/installer.ts>)

#### R25 · NVIDIA/skillevaluator

[GitHub](https://github.com/NVIDIA/skillevaluator) · Revision: `c9d170e77bdef0b32a4811fb9b14484578559b2e` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

NVIDIAs SkillEvaluator trennt statische Qualität, semantische Überlappung und praktische Agentenwirkung. Die Liveauswertung vergleicht Aufgaben mit und ohne Skill und erfasst gesondert, ob der Skill tatsächlich aktiviert wurde. Besonders übertragbar sind genaue Quellenidentitäten, eine stabile private Evaluationseingabe, Ausschluss früherer Reports aus dem Agentenkontext und sichtbare unvollständige Evidenz. Ein erfolgreicher Prozess ist dabei ausdrücklich etwas anderes als eine geeignete Veröffentlichungsempfehlung. Die vollständig gelesenen Anleitungen nennen wichtige Grenzen: Starterfälle sind schmal, Standardjudges besitzen keinen publizierten menschlichen Kalibrierungsnachweis, und unterstützte Backends wurden nicht sämtlich praktisch erprobt. Pass@k beschreibt mindestens einen Erfolg in mehreren Versuchen. Auch eine Veröffentlichungsempfehlung setzt nicht zwingend positiven gemessenen Lift voraus. Für eigene Skillfreigaben braucht es deshalb repräsentative Fälle, aussagekräftige Erfolgsdefinitionen und eine getrennte Interpretation von Sicherheitsscan, Aktivierung, Aufgabenresultat, Ressourcen und statistischer Unsicherheit. Hier wurde kein Evaluationslauf gestartet.

**Übertragbare Verfahren:**

- Statische Struktur-/Sicherheitsqualität, Dedup und praktische Wirksamkeit als unabhängige Evidenzstufen prüfen.
- Mit-Skill und Ohne-Skill bei gleichem Agenten, Modell, Aufgabenstand, Budget und Grading vergleichen.
- Skillaktivierung gesondert nachweisen und wirkungslos nie aktivierte Versuche als unentscheidbar behandeln.
- Evaluatorsteuerung, Credentials, Bewertungsdaten und frühere Reports von agentensichtbaren Runtime-Assets trennen.
- Publikationsnachweise an exakten Quelldigest, Dataset, Versuchs-/Scoringpolicy, Evaluator und vollständige Runidentität binden.
- Fehlende Scanner, Judges, Telemetrie und Paarabdeckung ausdrücklich als incomplete/no score statt null Erfolg behandeln.

**Voraussetzungen:** Python, passende Extras, bei voller statischer Prüfung externe Scanner. Liveauswertung benötigt Agent-/Judge-Provider und geeigneten Sandboxbackend. Manuell geprüfte repräsentative Positiv-/Negativfälle und zuverlässige Bewertungsregeln.

**Weitere Grenzen und Voraussetzungen der Aussage:** Ein Starterfall und eine Schwelle von0,5 pro Dimension belegen keine breite Verlässlichkeit. Standardjudges haben keinen publizierten Abgleich mit menschlicher Ground Truth oder Kalibrierung. Pass@k misst mindestens einen Erfolg in mehreren Anläufen und darf nicht als durchgehend wiederholbarer Erfolg gelesen werden. Kleine Skill-Lift-Bänder sind Diagnosekonventionen, keine statistischen Signifikanztests. Publikations-PASS kann trotz negativem diagnostischem Lift entstehen, wenn die anderen Evidenz-/Dimensionsgates bestehen. Prozess-Exitcode und Publikationsstatus unterscheiden sich; Tier3 ist für CLI standardmäßig beratend. Quelle schreibt Sicherheits-/Isolationsverträge, eigene Implementierungs-/Laufprüfung erfolgte nicht.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/NVIDIA/skillevaluator/README.md>) · [docs/tier3-live-evaluation.mdx](<../external_repos/NVIDIA/skillevaluator/docs/tier3-live-evaluation.mdx>) · [docs/tier1-validation.mdx](<../external_repos/NVIDIA/skillevaluator/docs/tier1-validation.mdx>) · [docs/reports.mdx](<../external_repos/NVIDIA/skillevaluator/docs/reports.mdx>)

#### R26 · NVIDIA/SkillSpector

[GitHub](https://github.com/NVIDIA/SkillSpector) · Revision: `d7338f58200a9ae2a24810cee08911ab68b107a7` · README-Vertrag; vollständige Ressourcen-/Suppression-Dokumente; kein eigener Scan

SkillSpector zeigt, wie eine vorgeschaltete Sicherheitsprüfung ihren eigenen Umfang dokumentieren sollte. Risk Score, statischer oder semantischer Modus und Vollständigkeit sind getrennte Ergebnisse. Ein Ressourcenlimit macht den untersuchten Teil nicht sauber; es erzeugt einen sichtbaren partiellen Befund. Deterministische Findings bleiben auch dann erhalten, wenn ein Modell widerspricht. Exakte Baseline-Fingerprints binden Quelltext, Evidenz und Scanner-Version, während absichtlich drifttolerante Glob-Regeln eine stärkere dauerhafte Ausnahme darstellen. Für Integrationen ist entscheidend, dass Exitcode null auch CAUTION umfasst. Ein strenges Gate muss Findings und Unvollständigkeit ausdrücklich berücksichtigen. Semantische Analyse übermittelt Inhalte an den gewählten Anbieter; auch ohne LLM werden Paketkoordinaten für Schwachstellenabfragen versandt. Das Werkzeug führt untersuchte Skills nicht aus und isoliert ihren späteren Betrieb nicht. Es liefert begrenzte, nachvollziehbare Risikohinweise statt einer Sicherheitsgarantie.

**Übertragbare Verfahren:**

- Risk Score, Analysemodus und tatsächliche Abdeckung getrennt ausweisen.
- Ressourcenlimits gemeinsam über rekursive Verarbeitung führen und Abbruch als partielle Analyse erhalten.
- Deterministische Findings trotz widersprechendem Modellurteil behalten.
- Suppression-Fingerprints an Quelltext, Evidenz und Scanner-Version binden.
- CAUTION, Findings und Unvollständigkeit über explizite CI-Policy behandeln.
- Remoteingest, Parser und Reportausgabe als eigene Vertrauensgrenzen begrenzen.

**Voraussetzungen:** Python 3.12+ oder Container; semantische Prüfung benötigt geeigneten Provider. Bewusste Auswahl von Netzwerk-/LLM-Modus und Gates; Windows-Dateiausgabe hat Einschränkungen.

**Weitere Grenzen und Voraussetzungen der Aussage:** Exit0 umfasst CAUTION und ist kein generelles Sicher-Signal. SAFE bei niedriger Punktzahl ist Scannerempfehlung innerhalb Abdeckung, kein Sicherheitsbeweis oder Sandbox. --no-llm verhindert nicht OSV-Netzabfragen mit Paketkoordinaten. Drifttolerante Glob-Unterdrückungen können neue gefährliche Inhalte verbergen. Datenraten26,1/5,2Prozent gelten für die bezeichnete analysierte Teilmenge; keine allgemeine Prävalenz. Bilder, verschlüsselte Inhalte und Laufzeitverhalten bleiben begrenzt oder ungeprüft.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/NVIDIA/SkillSpector/README.md>) · [docs/ANALYSIS_RESOURCE_BOUNDS.md](<../external_repos/NVIDIA/SkillSpector/docs/ANALYSIS_RESOURCE_BOUNDS.md>) · [docs/SUPPRESSION.md](<../external_repos/NVIDIA/SkillSpector/docs/SUPPRESSION.md>)

#### R27 · shanraisshan/claude-code-best-practice

[GitHub](https://github.com/shanraisshan/claude-code-best-practice) · Revision: `162bac91d0d016d30f3e9dce44ce9fdd6cb4c074` · README-Vertrag; Vollständig gelesene Orchestrierungs-, Cross-Model- und Memory-Dokumentation; kein eigener Lauf

claude-code-best-practice ist eine umfangreiche Landkarte von Erweiterungen und Arbeitsweisen, kein einheitliches Verfahren zum Installieren. Das Orchestrierungsbeispiel trennt den sichtbaren Command, einen delegierten Agent und fachliche Skills. Ein weiterer Ablauf hält einen dauerhaften Plan fest, lässt ein zweites Modell Findings ergänzen und prüft die Umsetzung später in einer frischen Sitzung am tatsächlichen Code. Diese Übergaben sind auch ohne dieselbe Modellkombination übertragbar. Die Memory-Seite ergänzt eine sparsame Hierarchie aus gemeinsamer Basis und lokal geltenden Regeln. Der Katalog enthält jedoch unterschiedliche Empfehlungen: frühe Prototypen, ausführliche Planung und Zurückhaltung beim Übersteuern von Agents lösen verschiedene Probleme. Modellnamen, Kontextschwellen, Produktfeatures und Geschwindigkeitswerte sind deshalb als datierte Beispiele zu behandeln. Popularitätstabellen ersetzen weder Primärdokumentation noch eine Prüfung der eingesetzten Laufzeit und des konkreten Projektbedarfs.

**Übertragbare Verfahren:**

- Commands als Einstieg, Agents als delegierte Bearbeitung und Skills als wiederverwendbare Fachfähigkeit trennen.
- Recherche, Planung, Umsetzung und Prüfung als explizite Phasen mit prüfbaren Übergaben gestalten.
- Modellübergreifende Reviews an einem dauerhaften Plan verankern; Findings anhängen statt die Planhistorie umzuschreiben.
- Implementierung phasenweise ausführen und in einer frischen Review-Sitzung gegen tatsächlichen Code prüfen.
- Memory nach Geltungsbereich staffeln: kompakte gemeinsame Basis und lokale Regeln erst bei Arbeit im passenden Verzeichnis laden.

**Voraussetzungen:** Host- und versionsgerechte Prüfung der dokumentierten Features; mehrere Modell-CLIs nur bei entsprechendem Bedarf. Projektbezogene Auswahl aus den vielen Methoden statt globaler Übernahme des gesamten Katalogs.

**Weitere Grenzen und Voraussetzungen der Aussage:** Modelle, Limits, Feature-Flags und Tipps sind datierte Community-Aussagen; Sterne und Umfang belegen keine Wirksamkeit. Prototyping vor PRD, immer planen und Agents nicht übersteuern stehen in unterschiedlichen Situationen; sie sind kein widerspruchsfreies Universalverfahren. Feste Kontextschwellen sind Heuristiken, keine allgemeine Grenze für alle Modelle und Aufgaben. Modellaufteilung im Cross-Model-Beispiel stammt aus einem konkreten historischen Setup und begründet keine aktuelle Modellrangfolge. Vergleiche angeblich ersetzter Startups und Geschwindigkeitsbehauptungen sind Meinungen beziehungsweise Selbstberichte.

**Abgleich mit dem Index:** Index bestätigt den Charakter einer Wissenslandkarte. Einzelne Zählwerte und Modellzuordnungen im umfassenden README bleiben historisch und können gegenüber anderen lokalen Repos abweichen.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/shanraisshan/claude-code-best-practice/README.md>) · [orchestration-workflow/orchestration-workflow.md](<../external_repos/shanraisshan/claude-code-best-practice/orchestration-workflow/orchestration-workflow.md>) · [development-workflows/cross-model-workflow/cross-model-workflow.md](<../external_repos/shanraisshan/claude-code-best-practice/development-workflows/cross-model-workflow/cross-model-workflow.md>) · [best-practice/claude-memory.md](<../external_repos/shanraisshan/claude-code-best-practice/best-practice/claude-memory.md>)

#### R28 · vercel-labs/skills

[GitHub](https://github.com/vercel-labs/skills) · Revision: `a80e4c9d12d607631249d4d7d059f835d4b2f13a` · vollständige README und ausgewählte statische Dokument-/Codebelege; kein eigener Lauf

Die Skills-CLI ist ein Verteilungswerkzeug und keine fachliche Skillsammlung. Sie unterscheidet projektbezogene und globale Installation, kanonische Ablage mit Links und unabhängige Kopien. Der Use-Modus kann einen Prompt erzeugen oder einen Agenten starten, ohne dauerhaft zu installieren. Für wiederholbare Arbeit sind genaue Quelle, Ref, Lockfile und Zielagent entscheidend. Die Discovery-Dokumentation beschreibt begrenzte Verzeichnistiefe und das Überschatten tieferer Skills durch eine flachere SKILL.md. Der experimentelle Dependency-Sync verknüpft Paketinhalt und Agentenwissen; Updates können damit auch wirksame Instruktionen verändern. Auffindbarkeit und korrekte Installation liefern jedoch keinen Qualitäts- oder Vertrauensnachweis. Telemetrie behandelt bestätigte öffentliche GitHub-Quellen anders als andere Quellen. Ihre Abschaltung betrifft zugleich Security-Audit-Anfragen. Die Factory kann den Installationsmechanismus nutzen, muss Inhaltsprüfung, Freigabe und spätere Versionspflege als eigene Schritte erhalten.

**Übertragbare Verfahren:**

- Kanonische Skillablage von agentenspezifischen Links oder unabhängigen Kopien trennen.
- Quellidentität und Version für reproduzierbare Remote-Inhalte erhalten.
- Discoverygrenzen und von flacheren Skills verdeckte Unterverzeichnisse berücksichtigen.
- Dependency-Sync mit Dry-run, Lockfile und ausdrücklicher Cleanup-Entscheidung betreiben.
- Telemetrie und Security-Audit-Anfragen als eigene Datenflüsse prüfen.

**Voraussetzungen:** Passende Node-Version sowie Zugriff auf ausgewählte lokale oder Remote-Quellen. Geprüfte Inhalte, Zielverzeichnisse und bewusst gewählter Projekt-/Globalscope.

**Weitere Grenzen und Voraussetzungen der Aussage:** Installation oder erfolgreiches Frontmatter beweist weder fachliche Qualität noch Vertrauen in die Instruktionen. Mit Dependencies verlinkte Skills können sich bei Paketupdates verändern. Der Sync ist ausdrücklich experimentell; Restore und Agentenlinks haben unterschiedliche Reichweite. Telemetrieabschaltung deaktiviert laut Dokumentation auch Security-Audit-Anfragen.

**Abgleich mit dem Index:** Installercharakter und experimenteller Sync bestätigt. Die gelesene Discoverydokumentation präzisiert die begrenzte Verzeichnistiefe und das Überschatten tieferer Skills.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/vercel-labs/skills/README.md>) · [docs/commands.md](<../external_repos/vercel-labs/skills/docs/commands.md>) · [docs/troubleshooting.md](<../external_repos/vercel-labs/skills/docs/troubleshooting.md>) · [docs/creating-skills.md](<../external_repos/vercel-labs/skills/docs/creating-skills.md>)

#### R29 · wshobson/agents

[GitHub](https://github.com/wshobson/agents) · Revision: `0874a27b17a22e2b7c2e2bcd725768e0803cad06` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Wshobsons Sammlung zeigt, wie viele Agentenrollen, Skills und Commands aus einer gemeinsamen Quelle auf mehrere Harnesses verteilt werden können. Native Registrierung und generierte Adapter sind dabei verschiedene Wege. Die Capability-Matrix dokumentiert Verluste: Tool-Allowlisten, Hooks, Modellvererbung und Agentenformate sind nicht überall gleich, und inherit kann zu einer festen Modellwahl werden. Namespacing und ausgelagerte Referenzen begrenzen Kollisionen und große Skillkörper. Besonders lehrreich ist die Selbstdokumentation von PluginEval. Statischer Lint prüft Struktur, der experimentelle Judge bewertet nur einen Textanfang und eigene Triggerfragen, die Monte-Carlo-Schicht zählt Antwortproduktion und Länge bei wiederholten Prompts. Keine dieser Größen beweist erfolgreiche Projektarbeit. Certified und Badges sind deshalb Verfahrenslabels. Die Factory kann Distribution und Prüfbarkeit übernehmen, sollte Qualität jedoch durch echte Aufgaben, unabhängige Erwartungen und menschlich kalibrierte Ergebnisse messen.

**Übertragbare Verfahren:**

- Native registries und generierte Adapterwege je Host getrennt dokumentieren.
- Capability-Matrix zeigt Verlust von Tool-Allowlisten, Hooks, Modellvererbung und Hintergrund-/Agentfunktionen.
- Große Skillkörper in Referenzen aufteilen und dedizierte Transformationsausgaben gegen Drift prüfen.
- Namespacing und eindeutige Skillnamen verhindern Installationskollisionen.
- Statische Strukturprüfung, Modellurteil und echte Task-Ausführung als verschiedene Evidenzstufen behandeln.

**Voraussetzungen:** Passender Harness und bewusst gewählter Plugin-/Einzelskillweg; Adaptererzeugung benötigt Python/uv. Modelle, Permissions und zusätzliche externe Plugins separat überprüfen.

**Weitere Grenzen und Voraussetzungen der Aussage:** 202 Agentrollen/185 Skills sind Katalogumfang, kein Nachweis entsprechender Expertise oder Taskleistung. inherit kann im Adapter auf feste Modelle abgebildet werden; native und generierte Wege haben unterschiedliche Größen-/Capabilitygrenzen. PluginEval-LLM-Judge sieht nur 3000 Anfangszeichen, erzeugt eigene Triggerfragen und bewertet eigene Vorhersagen. Monte Carlo misst nichtleere Antwort und Antwortlänge statt Aufgabenkorrektheit; 50/100 Läufe wiederholen nur 15 Prompts. Certified/Badges und statistische Intervalle validieren diese Proxy-Metriken nicht gegen menschliche Qualitätslabels.

**Abgleich mit dem Index:** Katalog-/Adapterstruktur bestätigt. Qualitätsframework ist stärker begrenzt als der Name Zuverlässigkeitstest nahelegt: wiederholte Antwortproduktion ist kein Verhaltensbenchmark; bei Plugin-Level nur statischer Lint.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/wshobson/agents/README.md>) · [docs/harnesses.md](<../external_repos/wshobson/agents/docs/harnesses.md>) · [docs/plugin-eval.md](<../external_repos/wshobson/agents/docs/plugin-eval.md>) · [plugins/developer-essentials/agents/monorepo-architect.md](<../external_repos/wshobson/agents/plugins/developer-essentials/agents/monorepo-architect.md>)


### Kontext, Wissensaufbereitung und Recherche

#### R30 · Egonex-AI/Understand-Anything

[GitHub](https://github.com/Egonex-AI/Understand-Anything) · Revision: `e24fcf6d371bcfa529bc110bacb1bb43de1b8d33` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Understand-Anything verbindet Parserstrukturen mit modellgenerierten Zusammenfassungen, Architekturschichten und Lerntouren. Der persistierte JSON-Graph lässt sich anschließend ohne erneute Modellanalyse betrachten. Übertragbar ist die Architektur der Aktualisierung: Inventar und Fingerprints entscheiden zwischen Überspringen, Teilaktualisierung, Architekturarbeit und Neuaufbau. Ein konservatives Symbolverlust-Gate vergleicht frühere Quellidentitäten mit aktuellen Definitionen und blockiert inkrementelle Veröffentlichung, wenn ein verschwundenes Symbol weder gelöscht noch zuverlässig erhalten nachgewiesen ist. Die gelesene Aktualitätsimplementierung unterscheidet außerdem unveränderte, uncommittete, veraltete und unbekannte Zustände. Das macht Fehlermeldungen zu einem Teil des Wissensmodells. Grenzen bleiben wesentlich: Referenzintegrität beweist keine fachlich richtige Bedeutung, Parser unterstützen nicht jede dynamische Deklaration, und alte Aktualitätshelfer verschlucken Git-Fehler weiterhin. Die README-Aussage, jede Funktion und Abhängigkeit abzubilden, ist daher ein Produktziel. Eine vollständige Codeanalyse oder ein praktischer Lauf wurde hier nicht vorgenommen.

**Übertragbare Verfahren:**

- Deterministische Strukturbelege und modellgenerierte Bedeutungsbeschreibungen getrennt erzeugen.
- Inventar, voraufgelöste Imports und begrenzte semantische Batches an spezialisierte Analyseschritte übergeben.
- Fingerprints und Änderungsart nutzen, um kleine Aktualisierungen von Architektur- oder Vollanalysen zu unterscheiden.
- Symbolverluste gegen vorherige Quellidentitäten prüfen und unbekannte oder weiterhin vorhandene Symbole vor inkrementeller Veröffentlichung blockieren.
- Kandidaten und endgültigen Graph getrennt validieren; Baselines erst nach erfolgreicher Aktualisierung fortschreiben.
- Aktualität als fresh, dirty, stale mit Git-Beziehung oder unknown modellieren, statt Metadatenfehler als Aktualität auszugeben.

**Voraussetzungen:** Für Generierung geeignete Agentenlaufzeit, Node/pnpm und unterstützte Parser. Korrektes Inventar, Ignore-Regeln und Git-/Fingerprint-Baselines. Für semantische Interpretation Modellbudget und Prüfung sensibler Inhalte; der Viewer selbst kann ohne Modell laufen.

**Weitere Grenzen und Voraussetzungen der Aussage:** README-Vollständigkeit für jede Funktion und Abhängigkeit übersteigt die garantierbare Parser-/LLM-Abdeckung. Strukturelle Identität und referenzielle Integrität beweisen keine richtige fachliche Beschreibung oder Laufzeitbeziehung. Unsupported Parsing blockiert Symbol-Löschbestätigung; dynamische Metaprogrammierung ist nicht vollständig analysierbar. Allgemeine Regel zum Speichern partieller Resultate steht neben strengem inkrementellem Publikationsgate; die spezifische Sperre muss Vorrang haben. Alte isStale/getChangedFiles-Funktionen behandeln Git-Fehler als leere Änderungsliste, während neue Freshness-Funktionen unknown erhalten. Default-Worktree-Umleitung verändert PROJECT_ROOT und damit Analyseziel; dieses Verhalten muss zum gewünschten Zweig passen. Aufräumtexte beschreiben bewusst zeitversetzte Löschung zur Vermeidung von Host-Destruktivitätsgates; fremde Policy darf dadurch nicht umgangen werden.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/Egonex-AI/Understand-Anything/README.md>) · [understand-anything-plugin/skills/understand/SKILL.md](<../external_repos/Egonex-AI/Understand-Anything/understand-anything-plugin/skills/understand/SKILL.md>) · [understand-anything-plugin/packages/core/src/staleness.ts](<../external_repos/Egonex-AI/Understand-Anything/understand-anything-plugin/packages/core/src/staleness.ts>) · [understand-anything-plugin/packages/core/src/change-classifier.ts](<../external_repos/Egonex-AI/Understand-Anything/understand-anything-plugin/packages/core/src/change-classifier.ts>)

#### R31 · Graphify-Labs/graphify

[GitHub](https://github.com/Graphify-Labs/graphify) · Revision: `92741d162b2094ffc2fed58cfbd8ee823e9da62c` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Graphify bietet eine lokale Graphpipeline mit deterministischer Codeextraktion und optionaler semantischer Verarbeitung von Dokumenten und Medien. Beziehungen tragen Quellenorte und Evidenzklassen; gezielte Teilgraph-, Pfad- und Begriffsabfragen können wiederholte breite Lektüre reduzieren. Wichtig sind die dokumentierten Betriebsgrenzen: Mehrdeutige Dateiendungen können ohne explizite Sprachzuordnung unvollständige, trotzdem gefüllte Graphen erzeugen. Kantenrichtung bleibt trotz eines ungerichteten Speicherformats bedeutsam. Eine gültige Extraktionsstruktur beweist weder vollständige Knoten noch richtige Beziehungen. Der Anbieterbenchmark kontrolliert Modelle und Budgets und legt Bewertungsbelege offen, umfasst für Codeverständnis jedoch nur sechs Fragen; Vergleichssysteme unterscheiden sich teilweise beim Embedder. Die lokale CLI ist vom separat beworbenen Cloud-Dienst zu trennen. Dessen Einsparungs- und Verifikationsversprechen wurden hier nicht überprüft. Ebenso sind lokale Verarbeitung, Provideraufrufe und lokale Abfragelogs unterschiedliche Datenschutzaspekte. Es erfolgten ausschließlich Dokumentlektüre und statische Codeprüfung.

**Übertragbare Verfahren:**

- Deterministische Codeextraktion von optionaler semantischer Dokument-/Medienverarbeitung trennen.
- Beziehungstyp, Herkunft, Quellort und EXTRACTED/INFERRED/AMBIGUOUS als nachvollziehbare Metadaten halten.
- Kleine Teilgraphen, Pfade und Begriffsauflösung vor umfassender Kontextaufnahme nutzen und mehrdeutige Namen explizit zurückweisen.
- Schema- und Produzentenversionsangaben sowie Sprachdeklarationen und Cacheversionen für reproduzierbare Graphen verwenden.
- Strukturierte rationale Kommentare und ADR-Verweise als eigene Wissensknoten erfassen.
- Benchmarkvergleich mit konstanten Modellen, Budgets, atomaren Sollfakten und belegten Bewertungsurteilen dokumentieren.

**Voraussetzungen:** Python und passende Parser-/Format-Extras. Explizite Wahl des Backends und Datenübertragungsumfangs für Dokumente/Medien. Aktueller Graph, passende Sprachzuordnung mehrdeutiger Dateiendungen und richtige Richtungsbehandlung beim Graphladen.

**Weitere Grenzen und Voraussetzungen der Aussage:** Cloud-Versprechen von 80 Prozent Einsparung und formaler Korrektheit sind hier weder lokal implementiert nachgewiesen noch unabhängig gemessen. Graphqualität bleibt parser- und resolverabhängig; falsche Sprachzuordnung kann scheinbar plausible unvollständige Graphen erzeugen. Schema-Validierung beweist keine semantisch korrekte Kante; gelesener Validator prüft Endpunktmitgliedschaft bei leerer Knotenmenge nicht und erzwingt nicht alle behaupteten Stringtypen. README beschreibt keinen Vektorindex; der separate Memory-Benchmark verwendet dennoch einen gemeinsamen lokalen Embedder und hybride Retrievalvarianten. Benchmark stammt vom Anbieter, Codebefunde umfassen nur sechs Fragen; Supermemory-Recall ist durch einen abweichenden Embedder konfundiert. Keine Telemetrie bedeutet nicht keine lokalen Abfragelogdateien oder keine Providerübertragung.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/Graphify-Labs/graphify/README.md>) · [ARCHITECTURE.md](<../external_repos/Graphify-Labs/graphify/ARCHITECTURE.md>) · [BENCHMARKS.md](<../external_repos/Graphify-Labs/graphify/BENCHMARKS.md>) · [graphify/validate.py](<../external_repos/Graphify-Labs/graphify/graphify/validate.py>)

#### R32 · headroomlabs-ai/headroom

[GitHub](https://github.com/headroomlabs-ai/headroom) · Revision: `3fef15d376d9899f77a28464e2e91f8b99514930` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Headroom adressiert Tokenkosten durch lokale, inhaltsabhängige Kompression und einen nachladbaren Originalspeicher. Übertragbar sind die Behandlung nur neuer Kontextteile, der Schutz stabiler Cache-Präfixe, statistische Auswahl redundanter JSON-Daten und das unveränderte Durchreichen bei Fehlern. Die Messmethodik unterscheidet geschätzte Output-Einsparungen von einem Vergleich mit unverkürzten Kontrollgesprächen. Die Grenzen sind entscheidend: README und Limitations unterscheiden sich beim Umfang von Code-, Bild- und RAG-Kompression; viele Inhalte passieren Schutzgates unverändert. Auch reversible Kompression ist kein Nullrisiko: Originale haben Kapazitätsgrenzen und im Proxy standardmäßig 30 Minuten Lebensdauer, und der Agent muss bei Bedarf tatsächlich nachladen können. Der direkte SDK-Weg übernimmt nicht automatisch den vollständigen Retrievalloop. Ein standardmäßig aktiver, laut Dokumentation inhaltsfreier Beacon gehört zur Datenflussprüfung. Eigene Qualitäts- und Kostenmessungen bleiben erforderlich.

**Übertragbare Verfahren:**

- Neue Live-Zone komprimieren und stabilen Präfix für Provider-Caches erhalten.
- JSON-Daten nach Redundanz, statistischen Ausreißern, Fehlern und Randbereichen auswählen; Kompressoren nach Inhalt routen.
- Compress-Cache-Retrieve legt Originale ab und gibt Retrievalmarker samt ausführbarem Tool bereit.
- Bei Parserfehlern, fehlenden Abhängigkeiten oder negativem Größenresultat Original durchreichen.
- Einsparung am eigenen Traffic messen; geschätzte Output-Einsparung von Kontrollgruppen-Messung unterscheiden.

**Voraussetzungen:** Lokaler Prozess; Python 3.10+ für CLI, optionale Modell-/Native-Abhängigkeiten. Expliziter Upstream, ausführbares Retrieval, passende TTL und Kapazität; Datenflüsse und Beacon prüfen.

**Weitere Grenzen und Voraussetzungen der Aussage:** README behauptet alle Inhalte inklusive Bilder/Code/RAG; Limitations dokumentiert für viele solcher Inhalte Passthrough und starke Schutzgates. Reversibel heißt nur innerhalb TTL/Kapazität und funktionsfähigem Retrieval; Proxy-Default 30 Minuten und LRU-Eviction widersprechen zero risk/always accessible. Direkter Python-SDK-Client injiziert laut CCR-Dokument nicht den kompletten Retrievalloop. Beacon standardmäßig aktiv; Benchmarks sind Projektmessungen und teils synthetische Einzelproben.

**Abgleich mit dem Index:** Breite Kompressionsbeschreibung im Index muss durch Passthrough-Gates und TTL begrenzt werden. CCR-Dokument sagt nur SQLite/memory mitgeliefert und weitere Backends via Plugin; Index nennt optionale Redis-Fähigkeiten möglicherweise aus neuerer Implementierung. Keine Auflösung durch Vollcodeprüfung.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/headroomlabs-ai/headroom/README.md>) · [docs/content/docs/limitations.mdx](<../external_repos/headroomlabs-ai/headroom/docs/content/docs/limitations.mdx>) · [docs/content/docs/ccr.mdx](<../external_repos/headroomlabs-ai/headroom/docs/content/docs/ccr.mdx>)

#### R33 · JoasASantos/REA-Prompts

[GitHub](https://github.com/JoasASantos/REA-Prompts) · Revision: `349a59ba476675889b6d88536fb42936ec02af83` · README-/Prompt-Vertrag; gesamter einteiliger Repository-Inhalt gelesen; kein eigener Lauf

REA-Prompts enthält eine einzige umfangreiche README mit Untersuchungsaufträgen für Binärdateien, Firmware, Android, Electron, Dateiformate, Protokolle und Versionsvergleiche. Der übertragbare Kern benötigt keine bestimmte REA-Marke: Eine eng begrenzte Funktion wird vom Einstieg bis zur Wirkung verfolgt, und jede Schlussfolgerung erhält einen konkreten Nachweis. Statisch vorhandener Code, abgeleitete Vermutungen und beobachtetes Verhalten bleiben unterschiedliche Kategorien. Für längere Untersuchungen werden offene Fragen, verworfene Hypothesen und nächste Experimente dauerhaft festgehalten. Rekonstruktionen sollen Abweichungen und ungeprüfte Zustände offenlegen. Einige Beispiele verlangen zwar nur einen passenden Testinput; die Sammlung warnt an anderer Stelle ausdrücklich davor, wenige Treffer als Äquivalenzbeweis zu behandeln. Die Prompts sind keine Implementierung der erwähnten Werkzeuge und garantieren deren Verfügbarkeit nicht. Für die Factory eignen sie sich als präzise Untersuchungs- und Übergabeformate für autorisierte technische Analysen.

**Übertragbare Verfahren:**

- Eine Funktion vom Einstieg über Datenfluss bis zur beobachtbaren Wirkung verfolgen.
- Statische Analyse zuerst durchführen und reale Ausführung gesondert begrenzen.
- Datei, Funktion, Adresse oder Originalbefund jeder Schlussfolgerung zuordnen.
- Fakten, Ableitungen und offene Punkte sichtbar unterscheiden.
- Rekonstruktionen gegen mehrere Fehler-, Grenz- und Zustandsfälle vergleichen.
- Langzeituntersuchungen mit verworfenen Hypothesen und verbleibender Unsicherheit persistieren.

**Voraussetzungen:** Gesonderte REA-Installation und tatsächlich verfügbare Engines. Autorisierter Untersuchungsgegenstand und für den konkreten Fall passende Grenzen.

**Weitere Grenzen und Voraussetzungen der Aussage:** Prompts liefern weder Implementierung noch Nachweis tatsächlich vorhandener Tool-Funktionen. Zitateanforderungen verhindern Halluzinationen nicht automatisch. Ein einzelner passender Beispielinput beweist keine Verhaltensäquivalenz. Lizenzangabe für Prompts umfasst nicht automatisch REA oder untersuchte Software.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/JoasASantos/REA-Prompts/README.md>)

#### R34 · juliusbrussee/caveman

[GitHub](https://github.com/juliusbrussee/caveman) · Revision: `9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4` · README-Vertrag; Skill-Vertrag; Hersteller-Benchmarkbericht; kein eigener Lauf

Caveman trennt inzwischen mehrere Kostenhebel: knappe Antworten, Eingabekompression, Modell- und Effort-Auswahl, wiederverwendbare Skripte und Nutzungsanalyse. Diese Trennung ist entscheidend, weil ein kürzerer Text allein die Rechnung nicht zuverlässig senkt. Das Dokument Honest Numbers nennt gegen eine bereits knappe Kontrollanweisung nur drei Prozent zusätzliche mediane Output-Reduktion für den normalen Stil, gemessen auf zehn Fragen und einem älteren Regelstand. Es hält negative Ergebnisse, Prompt-Overhead und fehlende Qualitätsnachweise ausdrücklich fest. Ganze Sessions werden stärker von Eingaben, Cache-Lesevorgängen und Wiederholungen geprägt. Ein vorläufiger Routingvergleich spart überwiegend durch niedrigeren Effort; seine Übertragbarkeit bleibt offen. Für die Factory ergibt sich eine klare Messregel: dieselbe reale Aufgabe samt Ergebnisqualität und Provider-Abrechnung vergleichen. Der reine Stil-Skill ist von der Vollsuite zu unterscheiden, deren CLI Telemetrie aktiviert und deren Auto-Routing Kontext an Caveman Cloud sendet.

**Übertragbare Verfahren:**

- Ausgabestil, Eingabekompression und Modell-/Effort-Auswahl als getrennte Eingriffe messen.
- Unveränderte technische Payloads und erhaltene Negationen als Kompressionsvertrag verwenden.
- Gegen eine bereits knappe Kontrollanweisung statt nur gegen lange Standardantworten vergleichen.
- Datei-Einsparung und gesamte Session einschließlich Cache, Regeln und Wiederholungen getrennt bilanzieren.
- Negative Benchmarkfälle und gemessene Grenzen öffentlich erhalten.
- Originale und wiederherstellbare Handles bei Eingabeverkleinerung behalten.

**Voraussetzungen:** Für Vollsuite Node 22.13+ und Änderungen an Agentkonfigurationen; Stil-Skill separat verfügbar. Auto benötigt Anmeldung und bewusste Auswahl; eigene Provider-Rechnungen für realen A/B-Vergleich.

**Weitere Grenzen und Voraussetzungen der Aussage:** README-Verkürzungsbeispiel entfernt Unsicherheitswort und ist deshalb kein Beleg identischer Semantik. Output-only-Ergebnisse auf zehn Fällen belegen keine allgemeine Qualitätsäquivalenz oder Geldersparnis. Routingvergleich über 85 Aufgaben ist vorläufig; Vergleich gegen niedrigeren Effort fehlt. CLI-Telemetrie standardmäßig aktiv; Auto sendet Teile der Anfrage samt angehängtem Kontext an Cloud.

**Abgleich mit dem Index:** Index korrekt; Detaillektüre verdeutlicht geringe zusätzliche Output-Einsparung gegenüber Answer concisely und fehlenden allgemeinen Qualitätsbeweis.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/juliusbrussee/caveman/README.md>) · [skills/caveman/SKILL.md](<../external_repos/juliusbrussee/caveman/skills/caveman/SKILL.md>) · [docs/HONEST-NUMBERS.md](<../external_repos/juliusbrussee/caveman/docs/HONEST-NUMBERS.md>)

#### R35 · kepano/obsidian-skills

[GitHub](https://github.com/kepano/obsidian-skills) · Revision: `3ccff5338ea700537839b21900aa5358a0402c98` · README-Vertrag; drei vollständige Skill-Verträge; kein eigener Lauf

Obsidian Skills ist ein kleines Beispiel für gezielte Formatkompetenz statt eines umfassenden Agentenframeworks. Die gelesenen Skills beschreiben Markdown-Erweiterungen, datenbankartige Bases-Ansichten und bereinigte Webextraktion. Ein stabiler Kern aus Frontmatter, verständlichen Überschriften und Quellenverbindungen bleibt dabei als normale Datei nutzbar. Bases ergänzen Filter, Formeln und mehrere Ansichten, benötigen jedoch korrekte YAML-Quotierung, definierte Eigenschaften und passende Typbehandlung. Eine Zeitdifferenz ist beispielsweise zunächst ein Duration-Objekt, dessen numerisches Feld vor Rundung gewählt werden muss. Strukturelle Prüfung und tatsächliches Rendern sind getrennte Schritte. Spezialansichten wie Maps können weitere Plugins voraussetzen. Defuddle reduziert Navigationsrauschen, beweist aber weder Vollständigkeit noch sachliche Richtigkeit einer Quelle. Für dieses Repository passt daher eine selektive Nutzung der Formatmuster mit unverändertem Roharchiv und optionalen Obsidian-Ansichten.

**Übertragbare Verfahren:**

- Notizen mit konsistentem Frontmatter und internen Verbindungen strukturieren.
- Inhalte als portable Markdown-Dateien halten und Spezialansichten optional darauf aufsetzen.
- Globale und ansichtsbezogene Filter sowie abgeleitete Formeln trennen.
- Fehlende Eigenschaften und Duration-Typen bei Formeln ausdrücklich behandeln.
- Strukturelle YAML-Prüfung und tatsächliche Anzeigeprüfung unterscheiden.
- Webtext bereinigen, ohne Extraktion mit Herkunfts- oder Vollständigkeitsnachweis gleichzusetzen.

**Voraussetzungen:** Obsidian für seine speziellen Darstellungen; optionale CLI-Werkzeuge separat. Maps-Ansicht benötigt Community-Plugin und ist damit keine reine Core-Funktion.

**Weitere Grenzen und Voraussetzungen der Aussage:** Wikilinks, Embeds und Bases rendern außerhalb Obsidian unterschiedlich. Defuddle-Anweisung fordert bei Bedarf globale Installation; das ist kein automatisch vorhandenes Werkzeug. Bereinigte Extraktion kann Inhalte auslassen und ersetzt nicht das unveränderte Quellenarchiv.

**Abgleich mit dem Index:** Keine wesentliche Abweichung; Maps explizit mit zusätzlichem Plugin.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/kepano/obsidian-skills/README.md>) · [skills/obsidian-markdown/SKILL.md](<../external_repos/kepano/obsidian-skills/skills/obsidian-markdown/SKILL.md>) · [skills/obsidian-bases/SKILL.md](<../external_repos/kepano/obsidian-skills/skills/obsidian-bases/SKILL.md>) · [skills/defuddle/SKILL.md](<../external_repos/kepano/obsidian-skills/skills/defuddle/SKILL.md>)

#### R36 · langchain-ai/openwiki

[GitHub](https://github.com/langchain-ai/openwiki) · Revision: `305599f8e44203f9ca6b74bb6b38eebaf0b0405e` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

OpenWiki behandelt Projektdokumentation als gepflegten Bestand aus Markdown und expliziten Claims. Ein Claim soll eine wesentliche, unabhängig falsifizierbare Systemaussage mit versionierter Quellressource sein. Die gelesene Implementierung ergänzt notwendige Aktualisierungsjobs auch dann, wenn der Modellplan sie vergisst, und verlangt für veraltete Claims eine ausdrückliche Entscheidung. Ein Seitenmanifest bindet abgeschlossene Arbeit an exakte Markdownbytes, Claim-Sidecar und Quellfingerprint; dadurch können fertige Seiten Unterbrechungen überstehen. Diese Architektur trennt inhaltliche Arbeit von deterministischer Buchführung. Sie garantiert trotzdem keine Wahrheit: Eine unvollständige Belegmenge oder falsche Interpretation kann aktuelle Metadaten besitzen. Die Claimsicherung gilt zudem bisher für Repositoryevidenz, nicht für sämtliche Connectorfakten. Lokale Suche und Abschnittslektüre bleiben modellfrei, während Generierung, Telemetrie und CDN-Viewer eigene Datenflüsse haben. Besonders nützlich ist die Kombination aus sparsamer Recherche, dauerhafter Arbeitsqueue und ausdrücklich begrenztem Nachweisstatus.

**Übertragbare Verfahren:**

- Wesentliche unabhängig falsifizierbare Systemaussagen als Claims mit versionierten Quellressourcen führen.
- Quelländerungen vor No-op-Entscheidung prüfen und notwendige Seitenjobs deterministisch ergänzen, wenn der Modellplan sie auslässt.
- Unveränderte Claims behalten; für veraltete oder unaufgelöste Claims explizite Bestätigung, Revision oder Rücknahme verlangen.
- Seitenabschluss an übereinstimmende Markdownbytes, verifizierten Claim-Sidecar und Quellfingerprint binden.
- Seitenweise dauerhafte Queue und Manifest nutzen, um Unterbrechungen ohne Verlust abgeschlossener Arbeit zu überstehen.
- Kompakte Suche und vollständiges Lesen ausgewählter Abschnitte als optionales Retrieval statt pauschalem Sitzungsritual einsetzen.

**Voraussetzungen:** Node ab 22.22 und native SQLite-Abhängigkeit. Belastbare Quellenbelege und geeignete Claims; Host- und native Generierung unterscheiden sich. Provider-/Connector-Konfiguration und geeignete persistente Ablage für Wiederaufnahme.

**Weitere Grenzen und Voraussetzungen der Aussage:** Versionierte Evidenz beweist nicht logisch, dass ein Claim aus ihr folgt; die wesentliche Inhaltsentscheidung bleibt modell-/menschenabhängig. Grounded Claims gelten derzeit nicht für reine Connector-/LangSmith-Fakten. Unbeeinträchtigte Claims werden automatisch bestätigt; unvollständig ausgewählte Belegmenge kann indirekte Änderungen übersehen. Lokale modellfreie Suche ist von generierender Providerübertragung, Connectoren, Telemetrie und CDN-Viewer zu unterscheiden. Erneutes Init ersetzt generiertes Wissen; ephemere CI-Runner brauchen gesicherte Zustände zum Resume. Die gelesenen Module belegen Seitenplanung, Reconciliation und Manifestbindung; vollständige Resolver-/Transaktionsprüfung erfolgte nicht.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/langchain-ai/openwiki/README.md>) · [src/claims/guidance.ts](<../external_repos/langchain-ai/openwiki/src/claims/guidance.ts>) · [src/generation/page-jobs.ts](<../external_repos/langchain-ai/openwiki/src/generation/page-jobs.ts>) · [src/generation/page-manifest.ts](<../external_repos/langchain-ai/openwiki/src/generation/page-manifest.ts>)

#### R37 · mattpocock/dictionary-of-ai-coding

[GitHub](https://github.com/mattpocock/dictionary-of-ai-coding) · Revision: `ed1ebed3975cba04ed5e74c6ca73659274beb754` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Das AI Coding Dictionary bietet 71 miteinander verlinkte Begriffe und macht technische Fehler genauer benennbar. Es unterscheidet Modell und Harness, einzelne Providerrequests und längere Sessions, Kontext und Kontextfenster sowie Werkzeuge und ihre Resultate. Daraus folgen praktische Diagnosefragen: Sind Tokens wirklich neu oder aus dem Prefix Cache, ist ein Handoff primär belegt, und liegen Regeln erreichbar vor? AX ergänzt die menschliche Developer Experience durch schnelle Checks, navigierbare Architektur und freien Kontext. Eine Software Factory automatisiert den Start von Sessions; erst der Verzicht auf menschliches Lesen kennzeichnet die Dark Factory. Die generierte README enthält dieselben 71 Textkörper wie die bereits vollständig gelesenen Archivseiten; der Vergleich wurde normalisiert nachgewiesen. Didaktische Cache- und Harness-Erklärungen bleiben anbieterabhängig. Das fehlende Lizenzdokument liefert keine pauschale Erlaubnis zur Übernahme.

**Übertragbare Verfahren:**

- 71 kanonische Begriffstexte werden über ein Curriculum in sieben Lernbereiche geordnet und in eine Gesamt-README projiziert.
- Definition, Mechanik, Symptome und konkrete Dialogbeispiele verknüpfen abstrakte Begriffe mit Diagnose.
- Modell und Harness sowie Sitzung, Turn und einzelner Providerrequest werden begrifflich getrennt.
- Primärquellen, Handoff-Artefakte und gestuft geladene Anweisungen erhalten Evidenz über Kontextwechsel.
- AX ergänzt DX durch schnelle Checks, navigierbare Architektur und frei gehaltenen Kontext.
- Software Factory automatisiert den Start begrenzter Sessions; Dark Factory entfernt zusätzlich menschliches Lesen der Ergebnisse.

**Voraussetzungen:** Kein Runtime-Tooling zum Lesen nötig; Generator ist nur für Pflege relevant. Gemeinsame Terminologie und konkrete Quellen statt pauschaler Modellannahmen.

**Weitere Grenzen und Voraussetzungen der Aussage:** Didaktische Erklärungen sind vereinfachte Modelle; Preise, Cache-TTLs und konkrete Harness-Verhalten sind datiert beziehungsweise anbieterabhängig. Keine Lizenzdatei im gelesenen Wurzelverzeichnis; keine pauschale Übernahmefreigabe ableiten. Die Aussage stateless bezieht sich auf Modellaufrufe, nicht fehlende Persistenz im gesamten Harness.

**Abgleich mit dem Index:** 71 Begriffe und generierte README bestätigt. Normalisierter Vergleich ergibt 71/71 gleiche Textkörper zwischen Originalen und bereits vom Hauptagenten vollständig gelesenen Archivseiten, und 71/71 Textkörper sind in README enthalten.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/mattpocock/dictionary-of-ai-coding/README.md>) · [internal/README.template.md](<../external_repos/mattpocock/dictionary-of-ai-coding/internal/README.template.md>) · [internal/Curriculum.md](<../external_repos/mattpocock/dictionary-of-ai-coding/internal/Curriculum.md>) · [internal/generate-readme.ts](<../external_repos/mattpocock/dictionary-of-ai-coding/internal/generate-readme.ts>) · [dictionary/Cache tokens.md](<../external_repos/mattpocock/dictionary-of-ai-coding/dictionary/Cache tokens.md>)

#### R38 · microsoft/markitdown

[GitHub](https://github.com/microsoft/markitdown) · Revision: `7482c092d9c0074a89803c9fdb63a969e7fe17fc` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

MarkItDown ist eine Konvertierungsschicht für strukturierte Textanalyse. Es versucht Überschriften, Listen, Tabellen und Links in Markdown zu erhalten, ohne originalgetreue Dokumentdarstellung zu versprechen. Der Konvertervertrag trennt schnelle Formaterkennung von Extraktion und schützt beim Vorablesen die Streamposition. Der untersuchte PDF-Konverter nutzt Wortpositionen und Heuristiken für Tabellen und Formulare; bei Prosa oder Fehlern wechselt er zur allgemeinen Textextraktion. Das liefert verarbeitbaren Text, garantiert aber weder Lesereihenfolge noch korrekte Tabellen. OCR und Cloud-Analyse sind gesonderte Wege mit eigenen Voraussetzungen; fehlende Visionkonfiguration kann OCR still entfallen lassen. Für die Wissensfabrik zählt deshalb ein enger Eingangsvertrag: nur benötigte Formate, lokale oder kontrollierte Streams, festgehaltene Quelle und nachgelagerte Qualitätsprüfung. Universelles convert besitzt die I/O-Rechte des Prozesses und ist keine Sandbox für fremde Inputs.

**Übertragbare Verfahren:**

- Schmale stream-/local-/response-APIs passend zur eigenen Vertrauensgrenze statt immer universellem convert verwenden.
- Konverter trennt schnelle accepts-Erkennung von eigentlicher Konvertierung; beim Peek muss Streamposition zurückgesetzt werden.
- Formatabhängige Dependencies gezielt installieren; Drittplugins sind standardmäßig aus.
- PDF-Extraktion nutzt Positionsheuristiken für Formulare/Tabellen und fällt bei Prosa oder Fehlern auf pdfminer zurück.
- Cloud-Analyzer und Zusatzfelder können strukturierte YAML-Metadaten erzeugen; Modalität und kostenpflichtige Formate gezielt beschränken.

**Voraussetzungen:** Python 3.10–3.14 und nur benötigte Formatabhängigkeiten. Bei Cloud/Vision Zugang, Kosten- und Datenflussentscheidung sowie separat verifizierte Extraktionsqualität.

**Weitere Grenzen und Voraussetzungen der Aussage:** Markdown dient Textanalyse, nicht visueller Originaltreue; PDF-Positionsheuristiken können Tabelle und mehrspaltige Prosa verwechseln. Gelesener Basiskonverter führt keine OCR durch; fehlender Visionclient lässt OCR-Plugin laut README still überspringen. I/O läuft mit Prozessrechten; universelle Inputs müssen Pfade, Schemes und Netzwerkziele begrenzen. PDF-Code importiert pdfminer und pdfplumber in einem gemeinsamen Dependency-Block; der Kommentar Fallback bei fehlendem pdfplumber ist damit nicht ohne Weiteres gedeckt.

**Abgleich mit dem Index:** Zweck und I/O-Grenzen bestätigt; statischer PDF-Code zeigt konkrete Heuristiken und die kommentarseitige Dependency-Fallback-Spannung.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/microsoft/markitdown/README.md>) · [packages/markitdown/src/markitdown/_base_converter.py](<../external_repos/microsoft/markitdown/packages/markitdown/src/markitdown/_base_converter.py>) · [packages/markitdown/src/markitdown/converters/_pdf_converter.py](<../external_repos/microsoft/markitdown/packages/markitdown/src/markitdown/converters/_pdf_converter.py>)

#### R39 · mleibetseder/ai-llm-wiki

[GitHub](https://github.com/mleibetseder/ai-llm-wiki) · Revision: `93d390f0e5f6d74173bf5fd57be2077ca076d354` · abgeleitete Wiki-Notizen; ausgewählte archivierte Primär-/Sekundärtexte; kein eigener Lauf

Das AI-LLM-Wiki verbindet ein Roharchiv mit vielen vernetzten Konzept- und Literaturseiten. Die hier vollständig gelesene Auswahl von dreißig Dateien reicht von mathematischen und Modellgrundlagen über Kontext, Gedächtnis, RAG, Skills und Sicherheit bis zu Organisation, Design, Schreiben und LLMOps. Der besondere Nutzen liegt in Querverbindungen: Ein Modellwechsel ist zugleich eine Evaluations-, Kosten- und Betriebsfrage; ein Skill verbindet Wissen mit einem Ablauf, benötigt aber weiterhin Werkzeuge und Kontrolle. Die Sammlung ist eine abgeleitete Orientierung und keine unabhängige Bestätigung ihrer Quellen. Das zeigt ein konkreter Schemafehler: Eine Konzeptseite nennt desc als Pflichtfeld, während die archivierte Spezifikation description verlangt. Andere Seiten übernehmen pauschale Garantien zu RAG und lokaler Privatsphäre. Mindestlinks und Grounding-Regeln ersetzen deshalb keine Quellenprüfung. Der gesamte umfangreiche Roh- und PDF-Bestand wurde für diesen Repo-Eintrag ausdrücklich nicht vollständig gelesen.

**Übertragbare Verfahren:**

- Unverändertes Rohmaterial von synthetisierten Konzeptseiten trennen.
- Aussagen mit lokalen Herkunftsverweisen und thematischen Querverbindungen verbinden.
- Kontext, Gedächtnis, Skills, Tools und Harness als verschiedene Ebenen unterscheiden.
- Kosten pro erfolgreichem Ergebnis samt Wiederholungen und Review statt nur Tokenpreise bewerten.
- Versionierte Prompt-/Modellartefakte, Traces, Evaluation und Rollback als Betriebszyklus verknüpfen.
- Verschiedene Zusammenarbeits- und Orchestrierungsmodelle nach Aufgabe auswählen.

**Voraussetzungen:** Gezielter Einstieg über agents.md und Konzeptseiten; Rohquellen bei tragenden Behauptungen überprüfen. Private Sammlung mit gesonderten Rechten der enthaltenen Bücher und Quellen.

**Weitere Grenzen und Voraussetzungen der Aussage:** Nur 30 ausgewählte Dateien vollständig gelesen; keine vollständige Lektüre aller Wiki-, Roh- oder PDF-Dateien. Grounding und Mindestlinks sind Regeln und mentale Kontrolle, keine nachgewiesene technische Garantie. Der Wiki-Skill-Artikel schreibt desc als Pflichtfeld; archivierte Original-Spezifikation verlangt description. Pauschale RAG-Halluzinationsfreiheit und vollständige lokale Privatsphäre werden aus vereinfachenden Quellen übernommen und sind nicht als Garantie verwendbar. agents.md erklärt raw unveränderlich und fordert zugleich ältere Duplikate zu löschen. Ältere Tool-/Modellzahlen stehen neben neueren Quellen; mehrere ähnliche Konzeptseiten erhöhen Driftgefahr.

**Abgleich mit dem Index:** Keine README und kein eigener zentraler Wiki-Index vorhanden; agents.md und themenbreite Konzeptauswahl als Einstieg verwendet. Indexwort erzwungen überzeichnet die nur mental geforderten Linkchecks. Konkreter Schemafehler desc nachgewiesen.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [agents.md](<../external_knowledge/ai-llm-wiki/agents.md>) · [wiki/concept-ai-basics.md](<../external_knowledge/ai-llm-wiki/wiki/concept-ai-basics.md>) · [wiki/concept-transformer-architecture.md](<../external_knowledge/ai-llm-wiki/wiki/concept-transformer-architecture.md>) · [wiki/concept-llm-lifecycle.md](<../external_knowledge/ai-llm-wiki/wiki/concept-llm-lifecycle.md>) · [wiki/concept-context-engineering.md](<../external_knowledge/ai-llm-wiki/wiki/concept-context-engineering.md>) · [wiki/concept-agent-memory-architecture.md](<../external_knowledge/ai-llm-wiki/wiki/concept-agent-memory-architecture.md>) · [wiki/concept-rag.md](<../external_knowledge/ai-llm-wiki/wiki/concept-rag.md>) · [wiki/concept-agent-evaluation.md](<../external_knowledge/ai-llm-wiki/wiki/concept-agent-evaluation.md>) · [wiki/concept-agent-security.md](<../external_knowledge/ai-llm-wiki/wiki/concept-agent-security.md>) · [wiki/concept-ai-engineering-lifecycle.md](<../external_knowledge/ai-llm-wiki/wiki/concept-ai-engineering-lifecycle.md>) · [wiki/concept-human-ai-collaboration-models.md](<../external_knowledge/ai-llm-wiki/wiki/concept-human-ai-collaboration-models.md>) · [wiki/concept-agent-cost-optimization.md](<../external_knowledge/ai-llm-wiki/wiki/concept-agent-cost-optimization.md>) · [wiki/concept-model-selection-strategy.md](<../external_knowledge/ai-llm-wiki/wiki/concept-model-selection-strategy.md>) · [wiki/concept-ai-design-collaboration.md](<../external_knowledge/ai-llm-wiki/wiki/concept-ai-design-collaboration.md>) · [wiki/concept-ai-writing.md](<../external_knowledge/ai-llm-wiki/wiki/concept-ai-writing.md>) · [wiki/concept-founder-playbook.md](<../external_knowledge/ai-llm-wiki/wiki/concept-founder-playbook.md>) · [wiki/concept-enterprise-agentic-ai.md](<../external_knowledge/ai-llm-wiki/wiki/concept-enterprise-agentic-ai.md>) · [wiki/concept-inference-engineering.md](<../external_knowledge/ai-llm-wiki/wiki/concept-inference-engineering.md>) · [wiki/concept-model-adaptation.md](<../external_knowledge/ai-llm-wiki/wiki/concept-model-adaptation.md>) · [wiki/concept-multi-agent-orchestration.md](<../external_knowledge/ai-llm-wiki/wiki/concept-multi-agent-orchestration.md>) · [wiki/concept-agent-skills.md](<../external_knowledge/ai-llm-wiki/wiki/concept-agent-skills.md>) · [wiki/concept-spec-driven-development.md](<../external_knowledge/ai-llm-wiki/wiki/concept-spec-driven-development.md>) · [wiki/concept-physical-ai.md](<../external_knowledge/ai-llm-wiki/wiki/concept-physical-ai.md>) · [wiki/concept-linear-algebra-foundations.md](<../external_knowledge/ai-llm-wiki/wiki/concept-linear-algebra-foundations.md>) · [wiki/concept-hardware-guide.md](<../external_knowledge/ai-llm-wiki/wiki/concept-hardware-guide.md>) · [wiki/concept-data-contracts.md](<../external_knowledge/ai-llm-wiki/wiki/concept-data-contracts.md>) · [wiki/concept-llmops.md](<../external_knowledge/ai-llm-wiki/wiki/concept-llmops.md>) · [raw/agentskills-specification.md](<../external_knowledge/ai-llm-wiki/raw/agentskills-specification.md>) · [raw/awesome-ai-handbook/use-cases/rag.md](<../external_knowledge/ai-llm-wiki/raw/awesome-ai-handbook/use-cases/rag.md>) · [raw/awesome-ai-handbook/basics/what-is-ai.md](<../external_knowledge/ai-llm-wiki/raw/awesome-ai-handbook/basics/what-is-ai.md>)

#### R40 · morluto/rea

[GitHub](https://github.com/morluto/rea) · Revision: `113679c9a6a1af4c77c1b546e466f4d490dc1095` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

REA strukturiert die Untersuchung ausgelieferter Artefakte und ausgewählten Laufzeitverhaltens. Der gelesene Skill trennt statische Analyse, externe Engines und tatsächliche Ausführung und wählt die Route nach dem Zieltyp. Seine stärkste übertragbare Methode ist ein Evidenzvertrag: Ergebnisse behalten Digests, Quellbereiche, Analyseprofile, Inferenzgrenzen und ausdrücklich unbekannte Abdeckung. Große Resultate werden einmal erzeugt und anschließend über gespeicherte Identitäten in passenden Ansichten gelesen. Ein Transportpreview ersetzt kein vollständiges Ergebnis; derselbe Produzent soll nicht bloß wegen übergroßer Ausgabe neu laufen. Fehlende Metadaten beweisen keine fehlende Fähigkeit, Signaturfelder keine Vertrauenswürdigkeit. Für normale Source-Repositories empfiehlt REA selbst gewöhnliche Werkzeuge. Engines, Plattformen und verfügbare Releases begrenzen den tatsächlichen Funktionsumfang. Laufzeitbeobachtung hat reale Seiteneffekte; lokale Analyse bedeutet zudem nicht, dass Modellanbieter keine Toolresultate sehen.

**Übertragbare Verfahren:**

- Zieltyp zuerst bestimmen und statische, enginegestützte sowie Laufzeit-Routen auseinanderhalten.
- Kleine Zusammenfassung und retained Evidence ID statt immer vollem Ergebnis liefern; zielgerichtet Seiten/Facetten nachladen.
- Dateidigest, Quellbereich und Analyseprofil über Folgeaufrufe erhalten.
- Beobachtungen, abgeleitete Kandidaten und Unbekanntes explizit trennen; fehlende Metadaten nicht als Abwesenheit von Verhalten deuten.
- Status-, Transport- und Startupfehler unterscheiden und identische Produzentenanalysen nicht blind wiederholen.
- Fragenledger führt jede Ausgangsfrage als beantwortet, teilweise oder offen.

**Voraussetzungen:** Explizit gewähltes, autorisiert untersuchtes Artefakt; unterstützte Node-Version. Je Ziel lokale externe Engines, Browser, Java/JADX oder weitere vom Betreiber bereitgestellte Werkzeuge.

**Weitere Grenzen und Voraussetzungen der Aussage:** Skill-Installation registriert kein MCP und installiert keine Engine; main-Fähigkeiten können Release und aktuell verbundenem Toolset voraus sein. Statische Deklarationen beweisen keine Ausführung, Signaturmetadaten keine Vertrauenswürdigkeit und Teilseiten keine vollständige Abdeckung. Runtime-Tools starten/bedienen Programme mit Benutzerrechten; lokale Analyse schützt nicht vor Weitergabe der Toolresultate an den Modellprovider. Kein REA-Lauf und keine vollständige Implementierungs-/Providerprüfung.

**Abgleich mit dem Index:** Indexzweck bestätigt. Der Skill enthält engere, besonders nützliche Evidenzgrenzen je Format; gewöhnliche Source-Repo-Architekturanalyse soll ausdrücklich normale Repo-Werkzeuge nutzen.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/morluto/rea/README.md>) · [.agents/skills/reverse-engineer-anything/SKILL.md](<../external_repos/morluto/rea/.agents/skills/reverse-engineer-anything/SKILL.md>)

#### R41 · rtk-ai/rtk

[GitHub](https://github.com/rtk-ai/rtk) · Revision: `32b2ec4386d90f27255ec984ea7b45ba42bf4694` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

RTK verkürzt vor allem das, was ein Agent aus Shellbefehlen liest. Befehlsspezifische Filter gruppieren Ergebnisse, fassen erfolgreiche Tests zusammen, kürzen Kontext und erhalten relevante Fehler. Native Read-, Grep- und Glob-Werkzeuge passieren den Bash-Hook nicht. Für die Bewertung ist seine Messgrenze vorbildlich deutlich: Die Kennzahl ist zunächst ein Byteverhältnis, die Tokenzahl nur bytes geteilt durch vier. Eine starke Verringerung der Terminalausgabe ist deshalb weder dieselbe Tokenquote noch derselbe Rabatt auf die Gesamtrechnung. Ein ungefilterter Bypass bleibt für exakte Diagnose und vollständige Quellenlektüre nötig. Optionale Engine und Proxy erweitern den Scope und besitzen andere Lizenzen als der CLI-Kern. In der Factory passt RTK zu repetitiven Build- und Testausgaben; es darf einen geforderten Volltextnachweis nicht unbemerkt in eine strukturelle Vorschau verwandeln.

**Übertragbare Verfahren:**

- Vor Lesen filtern, gruppieren, deduplizieren und kürzen, passend zum tatsächlichen Befehl.
- Passing Tests verdichten und Fehler fokussiert erhalten; bei Detailbedarf ungefilterten Bypass nutzen.
- Einsparungen als Byteverhältnis der Shellausgabe messen und klar von Token-/Gesamtrechnung trennen.
- Native Read-/Grep-/Glob-Werkzeuge als außerhalb des Bash-Hooks kenntlich machen.
- Defaultverhalten und optionale Pipeline-/Proxy-Erweiterungen trennen; nur nachgewiesene Harnessumleitung als proxied beschreiben.

**Voraussetzungen:** Passendes Rustbinary und jeweiliger Hook/Plugin-Vertrag; Rohdatenzugriff für Detailprüfung erhalten. Komponentenlizenz und eigene Filterempfindlichkeit prüfen.

**Weitere Grenzen und Voraussetzungen der Aussage:** Kürzung ist für vollständige Quellenlektüre oder exakte Diagnostik ungeeignet, wenn fehlende Bereiche nicht nachgeladen werden. bytes/4 liefert keine echten Tokenzahlen; prozentuale Byteverringerung kann sich von tokenizerbasierter Tokenverringerung unterscheiden. Shelloutput ist nur ein Rechnungsanteil; 90% dort bedeuten keine 90% Gesamtkostenersparnis. Engine/Proxy sind laut README BUSL-1.1, CLI-Kern/OSS-Edition Apache-2.0; keine eigene Laufzeitabnahme.

**Abgleich mit dem Index:** Mess- und Lizenzgrenzen bestätigt. Die README nennt percentages reliable; präzise gilt das für Byteverhältnisse, nicht zwangsläufig für tatsächliche modellabhängige Tokenprozente.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/rtk-ai/rtk/README.md>) · [docs/guide/resources/savings-explained.md](<../external_repos/rtk-ai/rtk/docs/guide/resources/savings-explained.md>)

#### R42 · teng-lin/notebooklm-py

[GitHub](https://github.com/teng-lin/notebooklm-py) · Revision: `00b2bd5077b11fc85efb814250b81ded2bd7da8f` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Notebooklm-py erschließt NotebookLM beziehungsweise das im Projekt als Gemini Notebook bezeichnete Produkt über inoffizielle Schnittstellen. Es verbindet Quellenimporte, zitierte Fragen, Recherche, Medienerzeugung und Exporte. Methodisch nützlich ist der genaue Lebenszyklus: vollständige IDs behalten, jede Quelle wirklich bereit werden lassen und anschließend genau das gestartete Artefakt abwarten und laden. Parallele Arbeit braucht getrennte beschreibbare Profile. Zitierbereiche beziehen sich auf strukturierte UTF-16-Dokumentpositionen und dürfen nicht blind auf flachen Text angewendet werden. Der Sicherheitsvertrag behandelt Cookies, CDP und Mastertoken als mächtige Kontozugänge und unterscheidet passive Diagnose von selbstheilender Authprüfung. Die APIs sind undokumentiert und können brechen. Zero-token ist eine Werbeverkürzung für ausgelagerte Analyse: Rechenarbeit, Datenübertragung und Ergebnisprüfung bleiben bestehen. Hier wurden weder Konten verbunden noch Quellen hochgeladen.

**Übertragbare Verfahren:**

- Jede Mutation und Folgeoperation an vollständige Notebook-, Source-, Research- und Artifact-IDs binden.
- Nach Import echte Source-Ready-Zustände abwarten; nach Generierung genau das erhaltene Artefakt fertigstellen und herunterladen.
- Parallele Workflows mit getrennten beschreibbaren Profilen und expliziten Notebook-IDs isolieren.
- Authcheck muss echten Tokenabruf bestätigen; passive Diagnose von selbstheilender schreibender Prüfung trennen.
- Zitierpassagen anhand strukturierter UTF-16-Dokumentbereiche auflösen statt Offsets auf flachen Exporttext anzuwenden.
- Abbruch und unklaren Remote-Commitzustand nicht mit Rollback gleichsetzen; nach Timeouts exakte ID inspizieren.

**Voraussetzungen:** Python 3.10+, separates geschütztes Google-Profil und bewusste externe Datenübertragung. Undokumentierte Backendprotokolle, Account-/Quotenlimits und teils langlaufende Verarbeitung berücksichtigen.

**Weitere Grenzen und Voraussetzungen der Aussage:** Inoffizielle Google-APIs können ohne Vorwarnung brechen; Androidbackend ändert diesen Status nicht. Cookies, CDP und langlebiger Mastertoken sind accountähnliche Credentials; Prozessabbruch kann gestartete Persistenz nicht rückgängig machen. Zero-token bedeutet Auslagerung auf Google und spart nicht alle Orchestrierungs-/späteren Skill-Kontexttokens; Quellbindung beweist keine Fehlerfreiheit. README-Rebrandingbehauptung ist datierte Projektangabe, keine hier extern bestätigte Produktwahrheit.

**Abgleich mit dem Index:** Indexcharakter und Authrisiken bestätigt. README-Werbung zu zero-token/self-validating ist durch die präzisen Lifecycle-/Zitierverträge zu begrenzen.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/teng-lin/notebooklm-py/README.md>) · [docs/security.md](<../external_repos/teng-lin/notebooklm-py/docs/security.md>) · [SKILL.md](<../external_repos/teng-lin/notebooklm-py/SKILL.md>)

#### R43 · thedotmack/claude-mem

[GitHub](https://github.com/thedotmack/claude-mem) · Revision: `bab040941390f6c1e82c0508ec806f2fc8255cbb` · README-Vertrag; Vollständig gelesene Architektur und Search-Skill; Statischer Codebeleg aus PrivacyCheckValidator und redaction.ts; kein eigener Lauf

Claude-Mem macht Arbeit über Sitzungsgrenzen hinweg auffindbar: Hooks oder Watcher erfassen Abläufe, ein Observer-Modell verdichtet sie, und der lokale Worker speichert strukturierte Beobachtungen. Der übertragbare Kern ist die gestufte Suche: erst kompakte Treffer, dann zeitlicher Kontext und schließlich ausgewählte Details; rohe Tool-Daten folgen nur bei Bedarf. Diese Reihenfolge begrenzt unnötigen Kontext, garantiert aber keine vollständige oder richtige Erinnerung. Zusammenfassungen können fehlerhaft, Rohdaten bereits abgeschnitten sein. Besonders relevant sind die Schutzgrenzen des gelesenen Codes: Schlüsselredaktion ist standardmäßig deaktiviert, generische Passwortmuster brauchen ein zusätzliches Opt-in. Fehlt eine Prompt-Zeile, erlaubt der Privacy-Validator die Erfassung mit Warnung; nur eine vorhandene, vollständig bereinigte leere Zeile unterdrückt sie. Lokaler Speicher und optionale gehostete Observer sind außerdem getrennte Datenflüsse. Der Nutzen verlangt deshalb bewusst konfigurierte Erfassung, Aufbewahrung und Abrufprüfung.

**Übertragbare Verfahren:**

- Tool-Beobachtungen und Sitzungszusammenfassungen mit IDs und Projektbezug dauerhaft speichern.
- Zuerst kompakte Suchtreffer, danach den zeitlichen Zusammenhang und erst zuletzt ausgewählte vollständige Beobachtungen laden.
- Mehrere Detailtreffer gebündelt abrufen und rohe Tool-Ein-/Ausgaben nur bei konkretem Bedarf nachladen.
- Queue-Zustand, Parsererfolg und Session-Identitäten ausdrücklich modellieren, damit Neustarts die Bearbeitung nachvollziehbar fortsetzen können.
- Private Inhalte und bekannte Schlüsseltypen vor Speicherung berücksichtigen; den tatsächlichen Aktivierungszustand der Redaktion separat prüfen.
- Transportausfälle als eingeschränkte Gedächtnisfunktion kenntlich machen, ohne automatisch die gesamte Coding-Sitzung zu blockieren.

**Voraussetzungen:** Node.js ab 20 sowie Bun-Worker; je Integration weitere Laufzeit- und Storage-Voraussetzungen. Observer-Modell und bewusste Auswahl lokaler beziehungsweise gehosteter Datenflüsse; Aufbewahrung und private Inhalte klären.

**Weitere Grenzen und Voraussetzungen der Aussage:** Beobachtungen sind modellgenerierte Zusammenfassungen; Zitations-IDs und semantische Suche beweisen deren Wahrheit nicht. Die genannten zehnfachen Token-Einsparungen sind Projektaussagen, keine eigene Messung; Rohdaten über 64 KB können abgeschnitten gespeichert sein. Secret-Redaktion ist im gelesenen Code standardmäßig aus; generische Passwort-/Token-Muster benötigen zusätzliches Opt-in. PrivacyCheckValidator unterdrückt eine vorhandene, nach Bereinigung leere Prompt-Zeile, erlaubt aber bei fehlender Zeile die Erfassung mit Warnung. Das ist eine dokumentierte Verfügbarkeits-/Datenschutzabwägung. Auch aktivierte Muster erkennen nicht jedes Geheimnis; beispielsweise nennt der AWS-Secret-Key-Matcher ausdrücklich eine JSON-Ankergrenze. Lokaler Speicher verhindert keine Übermittlung erfasster Inhalte an das konfigurierte Observer-Modell; Installer und optionale Cloud-Angebote können weitere Datenflüsse hinzufügen.

**Abgleich mit dem Index:** Der Index bestätigt Anwendung, Smart Recall und optionale Cloud-Dienste. Die tatsächliche Default-Deaktivierung der Schlüsselredaktion und das Erlauben bei fehlender Prompt-Zeile präzisieren die Schutzgrenzen wesentlich. README zählt an einer Stelle vier MCP-Tools, während der Kernablauf drei Schritte nennt; der Skill ergänzt den gesonderten Rohdatenabruf.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/thedotmack/claude-mem/README.md>) · [docs/architecture-overview.md](<../external_repos/thedotmack/claude-mem/docs/architecture-overview.md>) · [plugin/skills/mem-search/SKILL.md](<../external_repos/thedotmack/claude-mem/plugin/skills/mem-search/SKILL.md>) · [src/services/worker/validation/PrivacyCheckValidator.ts](<../external_repos/thedotmack/claude-mem/src/services/worker/validation/PrivacyCheckValidator.ts>) · [src/utils/redaction.ts](<../external_repos/thedotmack/claude-mem/src/utils/redaction.ts>)

#### R44 · upstash/context7

[GitHub](https://github.com/upstash/context7) · Revision: `b5e81de845092694ba1bfc5af15400f319c89b6d` · vollständige README und ausgewählte statische Dokument-/Codebelege; kein eigener Lauf

Context7 erschließt Bibliotheksdokumentation über eine aufgelöste Library-ID und eine konkrete Frage. Der gelesene Skill empfiehlt einen begrenzten Abruf pro Konzept und überspringt die Namenssuche, wenn die genaue Identität bereits vorliegt. Versionsangaben helfen, veraltete Modellkenntnis durch passende externe Information zu ergänzen. Die SDK-Implementierung zeigt den tatsächlichen Query-/Library-ID-Aufruf und die Zusammenführung von Code- und Informationssnippets. Das macht den Datenfluss greifbar: Fragen verlassen die lokale Umgebung und dürfen keine Credentials, personenbezogenen Daten oder proprietären Code enthalten. Die Werbeformel ohne Halluzinationen ist enger zu lesen als ihr Wortlaut. Die README selbst garantiert weder Richtigkeit noch Vollständigkeit oder Sicherheit der Community-Inhalte; Backend, Parser und Crawler bleiben privat. Für die Factory ist dies ein gezielter Retrievalweg, der korrekte Auswahl, Quellenprüfung und Verifikation am installierten Projekt weiterhin benötigt.

**Übertragbare Verfahren:**

- Bibliotheksidentität vor dem Abruf auflösen oder eine ausdrücklich vorgegebene ID verwenden.
- Versionsbezug und einzelne Konzepte in der Abfrage präzisieren.
- Dokumentationsausschnitte auf die tatsächliche Aufgabe beziehen und zur Herkunft zurückführen.
- Sensible Daten aus Queries heraushalten, da Fragen an die externe API übertragen werden.

**Voraussetzungen:** Passender CLI-/MCP-/SDK-Zugang und gegebenenfalls API-Key oder OAuth-Konfiguration. Klare Bibliotheks- und Versionszuordnung sowie ein geeigneter Datenfreigaberahmen.

**Weitere Grenzen und Voraussetzungen der Aussage:** Die README schließt Garantien für Richtigkeit, Vollständigkeit und Sicherheit der Community-Dokumentation ausdrücklich aus. Backend, Parsing und Crawling sind nicht Bestandteil des öffentlichen Repos. Erfolgreicher Snippetabruf beweist keine passende oder fehlerfreie API-Nutzung.

**Abgleich mit dem Index:** Library-ID-/Versionsworkflow bestätigt. Admin-MCP, Refresh-Locking und weitere Betriebsdetails des Index wurden in dieser Vertiefung nicht erneut vollständig geprüft.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/upstash/context7/README.md>) · [packages/pi/skills/context7-docs/SKILL.md](<../external_repos/upstash/context7/packages/pi/skills/context7-docs/SKILL.md>) · [packages/sdk/src/commands/get-context/index.ts](<../external_repos/upstash/context7/packages/sdk/src/commands/get-context/index.ts>)


### Modelle und Ausführungsumgebung

#### R45 · diegosouzapw/OmniRoute

[GitHub](https://github.com/diegosouzapw/OmniRoute) · Revision: `edab7c3a59bf7d6f040d581dbda3a46adbee0d57` · README-Vertrag; Architektur-/Routingdokumentation; statischer Codebeleg; kein eigener Lauf

OmniRoute ist eine umfangreiche Referenz für den Betrieb eines Multi-Provider-Gateways. Sein wichtigster fachlicher Unterschied liegt zwischen dem Preis eines Modells und der Abrechnung einer konkreten Verbindung: Dasselbe Modell kann im Abo enthalten oder separat metriert sein. Abo-Routing mit hartem Kostenstopp muss deshalb jede tatsächlich verwendbare Verbindung prüfen und bei Unsicherheit schließen. Davon getrennt ist eine ausdrücklich gewünschte Eskalation zu bezahlten Angeboten. Die Dokumentation beschreibt getrennte Fehlerzustände für Provider, Konten und Modelle sowie unabhängige Grenzen für Queue-Wartezeit und Ausführung. Sie benennt aber auch Lücken: Positive Budgets wirken ohne angeschlossenes Accounting nicht als Ausgabenlimit, und eine Cooldown-Korrektur ist noch nicht verdrahtet. Kompressionsquoten und aggregierte Gratisbudgets bleiben datierte Herstellerangaben. Selbsthosting hält den Kontrollpfad lokal; Anfragen verlassen ihn weiterhin zum jeweils gewählten Anbieter.

**Übertragbare Verfahren:**

- Abrechnung pro Verbindung statt nur pro Modell klassifizieren.
- Fail-closed Abo-Routing von ausdrücklich bezahlten Eskalationspfaden trennen.
- Fehler nach Provider, Verbindung, Modell und dauerhaften Kontozuständen unterscheiden.
- Wartezeit in einer Queue und Ausführungszeit mit verschiedenen Grenzen steuern.
- Verifizierte Verbindungs-Allowlist bis zur tatsächlichen Dispatch-Auswahl erhalten.
- Kosten-, Kompressions- und Routingentscheidungen je Antwort beobachtbar machen.

**Voraussetzungen:** Eigene berechtigte Provider-Verbindungen und geeignete Node-/Bun-Laufzeit. Betrieb und Pflege zahlreicher Zugangsdaten und Anbieterregeln; lange Agentenkontexte benötigen laut README erheblichen RAM.

**Weitere Grenzen und Voraussetzungen der Aussage:** Gratisbudgets und 15–95 Prozent Kompression sind datierte Projektangaben mit wechselnden Voraussetzungen. Subscription-Ladder-Dokumentation nennt nicht verdrahtete Cooldown-Korrektur und nicht erzwungene positive Rung-Budgets; Code bestätigt fehlendes Accounting als nicht begrenzend. Der Code besitzt einen enabled-Schalter, obwohl die fachliche Anleitung keinen abschaltbaren Sicherheitsvertrag verspricht; konkrete Aufrufer wurden nicht komplett geprüft. Einige Concurrency-Gates sind fail-open; Modell-Lockout und zusätzliche Provider-Cooldowns sind teilweise opt-in. Lokaler Kontrollpfad bedeutet weiterhin Übertragung an ausgewählte Upstream-Provider.

**Abgleich mit dem Index:** Index korrekt als Gateway eingeordnet; zusätzliche Detailgrenzen sind reservierte Budgetwerte, fehlende Cooldown-Verdrahtung und unterschiedliche Aktivierungszustände von Resilienzschichten.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/diegosouzapw/OmniRoute/README.md>) · [docs/routing/SUBSCRIPTION_LADDER.md](<../external_repos/diegosouzapw/OmniRoute/docs/routing/SUBSCRIPTION_LADDER.md>) · [docs/architecture/RESILIENCE_GUIDE.md](<../external_repos/diegosouzapw/OmniRoute/docs/architecture/RESILIENCE_GUIDE.md>) · [open-sse/services/autoCombo/subscriptionLadder.ts](<../external_repos/diegosouzapw/OmniRoute/open-sse/services/autoCombo/subscriptionLadder.ts>)

#### R46 · farion1231/cc-switch

[GitHub](https://github.com/farion1231/cc-switch) · Revision: `de0a235ad6389ce4afa333b472cdee615a3f3987` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

CC Switch ist eine Desktop-Anwendung zur zentralen Verwaltung verschiedener Coding-Clients und ihrer Provider. Die klare Trennung der Modi ist übertragbar: Direct schreibt Verbindungseinstellungen, Routing übersetzt API-Protokolle und kann eine Failover-Warteschlange nutzen, Aggregation verteilt anhand des ausgewählten Modells und bietet kein Failover. Gemeinsame Client-Einstellungen sollen von providerspezifischen Feldern getrennt bleiben; Backups und sichtbare Metadatenquellen erleichtern Kontrolle. Requestlogs unterscheiden angefordertes und tatsächlich verwendetes Modell. Gleichzeitig steigt die Verantwortung für Credentials, lokale Daten und optionalen Cloud-Sync. Ein Connectivity-Test bestätigt nur Erreichbarkeit. Gesponserte Preis- und Verfügbarkeitsversprechen sind kein Qualitätsnachweis. Die gelesene README widerspricht dem Index bei Anwendungszahl und Claude-Desktop-Aggregation; das bleibt als Dokumentationsdrift offen. Cross-Provider-Subagents und andere Reviewer-Modelle verändern zudem Sicherheits- und Funktionsannahmen und verlangen eine eigene Abnahme.

**Übertragbare Verfahren:**

- Verbindungsfelder von gemeinsam genutzten Client-Einstellungen trennen und vor erster Änderung sichern.
- Routing übersetzt Protokolle und nutzt explizite Prioritätswarteschlangen mit Retry, Timeout und Circuit Breaker.
- Aggregation routet anhand ausgewählter Modellpräfixe und hat ausdrücklich kein Failover.
- Sessions und Requestlogs machen angefordertes und tatsächlich verwendetes Modell sichtbar.
- Metadatenquellen für Kontextfenster/Capabilities anzeigen und leere Felder ergänzen, statt Fähigkeiten durch Konfiguration zu behaupten.

**Voraussetzungen:** Grafische Umgebung und unterstützte OS-/Clientversionen, lokale Credentials sowie dauerhaft laufender Dienst für Routing/Aggregation. Provider- und Datenschutzprüfung; Neustartverhalten des jeweiligen Clients beachten.

**Weitere Grenzen und Voraussetzungen der Aussage:** Gesponserte Relay-Preise, Sicherheits- und SLA-Versprechen sind Werbung, keine geprüften Fakten. Formatkonvertierung, Reviewer-Modelle und Providerwechsel verändern Verhaltens- und Vertrauensgrenzen; Connectivity-Test prüft nur Erreichbarkeit. Cross-Provider-Subagents benötigen laut Dokumentation klassische unverschlüsselte Aufgabenübergabe und verlieren neuere Agentfunktionen. Lokale Datenbank, OAuth-Dateien und optionaler Cloud-Sync bündeln sensible Konfiguration; kein eigener Lauf.

**Abgleich mit dem Index:** Index nennt 13 Anwendungen einschließlich Antigravity, tatsächliche gelesene README nur 12. Index sagt Claude Desktop unterstützt Routing/Aggregation; README-Tabelle beschränkt Desktop auf Model Mapping und verneint Aggregation. Das kann Dokumentationsdrift sein; Implementierung nicht vollständig geprüft.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/farion1231/cc-switch/README.md>) · [docs/user-manual/en/4-proxy/4.3-failover.md](<../external_repos/farion1231/cc-switch/docs/user-manual/en/4-proxy/4.3-failover.md>) · [docs/user-manual/en/4-proxy/4.6-aggregation.md](<../external_repos/farion1231/cc-switch/docs/user-manual/en/4-proxy/4.6-aggregation.md>)

#### R47 · openai/codex

[GitHub](https://github.com/openai/codex) · Revision: `970111f6cb62cc02fe36a82ea7d71b37a2889c97` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Codex ist im untersuchten Repository ein lokal laufender Coding-Agent mit mehreren Zugängen und einem umfangreichen Rust-Kern. Die kurze README verweist für viele Nutzungsverträge auf externe Dokumentation; sie allein trägt keine detaillierten Aussagen über jede Produktfunktion. Vertieft wurde die Ausführungspolicy: geordnete Argumentpräfixe können erlauben, nachfragen oder verbieten, und passende sowie ausdrücklich unpassende Beispiele werden beim Laden geprüft. Mehrere Treffer ergeben die strengste Entscheidung; fehlende Treffer werden gesondert ausgewiesen. Eine konfigurierbare Zuordnung absoluter Programme zu Basenames macht Pfadannahmen sichtbar. Diese Mechanik zeigt die sinnvolle Trennung zwischen Agentenanweisung, Ausführungsentscheidung und Betriebssystemgrenzen. Sie ist weder eine vollständige Sandboxprüfung noch ein Nachweis aktueller Konto- oder Appfunktionen. Der ausgewählte Code bestätigt Entscheidungswerte, während die umfassende Plattformimplementierung außerhalb dieser Vertiefung bleibt.

**Übertragbare Verfahren:**

- Anweisungen, Agentenlauf, Ausführungsentscheidung und Sandbox als getrennte Verantwortlichkeiten behandeln.
- Prefix-Regeln matchen geordnete Argumenttokens mit Allow, Prompt oder Forbidden.
- Positive und negative Beispielaufrufe werden beim Laden der Policy validiert.
- Absolute Executablepfade können ausdrücklich auf erlaubte Pfade für Basename-Fallback eingeschränkt werden.
- Bei mehreren Treffern gilt die strengste Entscheidung; kein Treffer ist ein eigener Zustand ohne implizites Allow.

**Voraussetzungen:** Unterstütztes Plattformbinary und passender ChatGPT-/API-Zugang; konkrete Runtimekonfiguration gesondert prüfen. Für Policy-Nutzung passende Preview-Schnittstelle und präzise Argumentbeispiele.

**Weitere Grenzen und Voraussetzungen der Aussage:** README und lokale Nutzungsdocs sind überwiegend Verweise; sie belegen keinen vollständigen Vertragsinhalt aller Produktfunktionen. Prefixregel allein ist keine Sandbox oder allgemeiner Sicherheitsbeweis; ohne Hosteintrag erlaubt dokumentierter Fallback auch andere absolute Pfade. Source-Commit beweist keine Verfügbarkeit im eigenen Konto/Appbuild; keine aktuellen Preise oder Modellfähigkeiten abgeleitet. Execpolicy wird als Preview mit möglichen Änderungen beschrieben.

**Abgleich mit dem Index:** Breite Source-Architektur im Index geht über die gelesene README hinaus. Hier konkret Policy-Vertrag und Decision-Code bestätigt; neue Memory-/Guardian-/Remote-/Vertex-Funktionen aus Index nicht vollständig geprüft.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/openai/codex/README.md>) · [docs/exec.md](<../external_repos/openai/codex/docs/exec.md>) · [docs/sandbox.md](<../external_repos/openai/codex/docs/sandbox.md>) · [docs/agents_md.md](<../external_repos/openai/codex/docs/agents_md.md>) · [codex-rs/execpolicy/README.md](<../external_repos/openai/codex/codex-rs/execpolicy/README.md>) · [codex-rs/execpolicy/src/decision.rs](<../external_repos/openai/codex/codex-rs/execpolicy/src/decision.rs>)

#### R48 · router-for-me/CLIProxyAPI

[GitHub](https://github.com/router-for-me/CLIProxyAPI) · Revision: `bc0643405a1d0adf77dd0f109972ac3313d66397` · vollständige README und ausgewählte statische Dokument-/Codebelege; kein eigener Lauf

CLIProxyAPI stellt heterogenen Clients kompatible Modellendpunkte bereit und verbindet sie mit OAuth, API-Keys, Account-Pools und Streaming. Übertragbar ist besonders die klare Trennung dreier Erweiterungen: Ein Executor führt Provideraufrufe aus, Translatoren übersetzen Anfragen und Antworten, und eine Registry veröffentlicht verfügbare Modelle. Eingehende Clientauthentifizierung ist davon ein eigener Vertrag. Der vollständig gelesene Access-Manager bestätigt geordnete Providerketten und unterschiedliche Fehlerzustände. Ohne Manager oder konfigurierte Provider liefert er jedoch keinen Authentifizierungsfehler; die sichere Verdrahtung muss deshalb am konkreten Server geprüft werden. Die README erklärt außerdem, dass eingebaute Nutzungsstatistiken entfernt wurden und separate Dienste nötig sind. Erfolgreiches Routing belegt somit weder Kostenkontrolle noch zulässige Account-Nutzung. Die umfangreichen Sponsorangebote und unterstützten Modelle bleiben datierte Projektangaben. Eigene Anmeldungen oder Laufversuche fanden nicht statt.

**Übertragbare Verfahren:**

- Eingehende Zugangsprüfung von ausgehenden Provider-Credentials trennen.
- Provider-Executor, Request-/Response-Translator und Modellregistrierung als eigene Verträge gestalten.
- Providerreihenfolge, NotHandled, fehlende und ungültige Credentials sowie interne Fehler ausdrücklich unterscheiden.
- Verbrauchsbeobachtung als eigene Betriebsfunktion behandeln, statt sie aus erfolgreichem Routing abzuleiten.

**Voraussetzungen:** Go-Laufzeit beziehungsweise geeigneter Build und ausdrücklich konfigurierte Provider-/Clientzugänge. Geprüfte Netzwerkexposition, Credential-Speicherung und passende Betriebsbeobachtung.

**Weitere Grenzen und Voraussetzungen der Aussage:** Der gelesene Access-Manager deaktiviert seine Prüfung bei nil oder leerer Providerliste; das ist ein SDK-Vertrag, kein vollständiger Nachweis der deployed Serverkonfiguration. Laut README fehlen seit v6.10.0 eingebaute Nutzungsstatistiken; genannte Erweiterungsprodukte wurden nicht vertieft geprüft. Sponsorenpreise, Modellverfügbarkeit und Account-Nutzungsrechte sind hier nicht bestätigt.

**Abgleich mit dem Index:** Provider-Abstraktion bestätigt. Die ausgewählten SDK-Dokumente nutzen weiterhin v6-Pfade; neuere Cluster-, Plugin- und Credential-Details aus dem Index wurden nicht als Vollcodeaudit nachgeprüft.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/router-for-me/CLIProxyAPI/README.md>) · [docs/sdk-access.md](<../external_repos/router-for-me/CLIProxyAPI/docs/sdk-access.md>) · [docs/sdk-advanced.md](<../external_repos/router-for-me/CLIProxyAPI/docs/sdk-advanced.md>) · [sdk/access/manager.go](<../external_repos/router-for-me/CLIProxyAPI/sdk/access/manager.go>)


### Codequalität und Frontend-Design

#### R49 · abi/screenshot-to-code

[GitHub](https://github.com/abi/screenshot-to-code) · Revision: `a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc` · README-Vertrag; Design-Dokument; kein eigener Lauf

Screenshot to Code verbindet Screenshots, Mockups und Bildschirmaufzeichnungen mit einer Werkzeugschleife zur Frontend-Erzeugung. Übertragbar ist vor allem der Ablauf visuelle Spezifikation, Code, gerenderte Vorschau und erneuter Vergleich. Das Design-Dokument zeigt, warum die Fortsetzung einer Tool-Schleife Provider-spezifische IDs und Antwortobjekte erhalten muss. Eine begrenzte Zahl von Werkzeugrunden verhindert unbeschränktes Weiterlaufen. Die Oberfläche kann eine teilweise erzeugte Datei allerdings schon zeigen, bevor ihre Werkzeugausführung abgeschlossen ist; sichtbare Vorschau und erfolgreicher Zustand sind deshalb getrennte Nachweise. Das Evaluationsdokument beschreibt wiederholte subjektive Bewertungen eines kleinen Screenshot-Sets. Daraus folgt keine belegte Funktionsqualität. Für die Factory eignet sich das Projekt als Referenz für visuelle Iteration und Asset-Wiederverwendung. Provider-Keys, optionale Bilddienste und Chromium sind konkrete Voraussetzungen; Modellangaben gelten für den dokumentierten Stand.

**Übertragbare Verfahren:**

- Screenshot oder Mockup als visuelle Spezifikation verwenden und erzeugte Seite im Browser vergleichen.
- Werkzeugschleife pro Variante begrenzen und Provider-native Tool-Call-IDs sowie Fortsetzungsobjekte erhalten.
- Erzeugte Assets wiederverwenden und optionale Renderfähigkeit ausdrücklich anzeigen.
- Visuelle Bewertungen über mehrere Versuche mitteln und von Funktionsprüfung trennen.

**Voraussetzungen:** React/Vite und FastAPI-Laufzeit; mindestens ein unterstützter Provider-Key. Gemini für bestimmte Asset-/Videofunktionen, Replicate für optionale Bildbearbeitung, Chromium für Preview.

**Weitere Grenzen und Voraussetzungen der Aussage:** UI-Vorschau kann bereits vor erfolgreicher Dateierzeugung erscheinen. Evaluation beschreibt 16 Screenshots und subjektive Bewertungen; Datensatz-Download bleibt TODO und beweist keine Funktionalität. README-Modellangaben sind uneinheitlich und ausschließlich datierte Projektangaben.

**Abgleich mit dem Index:** Index weist bereits auf veraltete README-Modelllisten hin; bestätigte Zusatzgrenze ist die optionale, bei fehlenden Voraussetzungen übersprungene Vorschau.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/abi/screenshot-to-code/README.md>) · [design-docs/agent-tool-calling-flow.md](<../external_repos/abi/screenshot-to-code/design-docs/agent-tool-calling-flow.md>) · [Evaluation.md](<../external_repos/abi/screenshot-to-code/Evaluation.md>)

#### R50 · DietrichGebert/ponytail

[GitHub](https://github.com/DietrichGebert/ponytail) · Revision: `09c434ab73ca43761c5d8b0c5d341926c2fba710` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Ponytail formuliert Minimalität als kleinste vollständige Änderung nach gründlichem Verständnis der betroffenen Aufrufer und Datenflüsse. Vor neuer Implementierung stehen Bedarf, vorhandener Code, Standardbibliothek, Plattformfunktionen und installierte Abhängigkeiten. Validierung, Schutz vor Datenverlust, Sicherheit und Barrierefreiheit bleiben ausdrücklich erhalten. Das Review betrachtet auch Verbraucher außerhalb des Diffs und verlangt für jeden Befund einen konkreten Fehlerfall sowie eine Einordnung nach der erwarteten Last. Der datierte Autorenbenchmark berichtet weniger Code, Kosten und Laufzeit sowie häufiger mitgelieferte Tests. Seine Aussagekraft ist begrenzt: Die Agenten konnten keine Shell benutzen, nur 18 von 39 Aufgaben besaßen versteckte ausführbare Korrektheitsprüfungen, und auf den Sicherheitsaufgaben waren alle Vergleichsarme gleich erfolgreich. Übertragbar ist deshalb vor allem die Entscheidungsleiter mit vollständiger Reichweite und überprüfbaren Grenzen; pauschale Einsparungen für andere Hosts oder reale Wartungsarbeit lassen sich daraus nicht ableiten.

**Übertragbare Verfahren:**

- Vor einer Lösung Aufrufer, Tests, Konfiguration und tatsächlichen Datenfluss ermitteln.
- Bedarf, Wiederverwendung, Standardbibliothek, Plattform und vorhandene Abhängigkeiten vor neuem Code prüfen.
- Trust-Boundary-Validierung, Datenverlustschutz, Sicherheit und Barrierefreiheit von Kürzungen ausnehmen.
- Nicht triviale neue Logik mit einem kleinen aussagekräftigen Test absichern.
- Reviewbefunde an konkrete reproduzierbare Fälle und erwartete Last binden; Entscheidungen und nicht geprüfte Bereiche benennen.

**Voraussetzungen:** Ein Agent, der die Anweisungen zuverlässig lädt, und projektspezifische Regeln, die Prioritäten klären. Für Zusatzanzeigen geeignete Hostversion und für Hooks Node.js. Kenntnis der tatsächlichen Nutzerlast und aller durch die Änderung betroffenen Verbraucher.

**Weitere Grenzen und Voraussetzungen der Aussage:** Benchmark vom Autor mit 39 Aufgaben, je fünf Läufen und deaktivierter Shell; kein allgemeiner Produktionsnachweis. Nur 18 Aufgaben hatten ausführbare versteckte Korrektheitsprüfungen; übrige Vollständigkeit teilweise Modellurteil. Sicherheitsaufgaben bestanden auch ohne Skill alle Läufe; der Versuch belegt dort keinen Sicherheitsgewinn. Kürzere Implementierung ist nur zusammen mit erfülltem Umfang und erhaltenen Schutzmechanismen ein Vorteil. Vorliegende Skillversion und datierter Benchmark können voneinander abweichen.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/DietrichGebert/ponytail/README.md>) · [skills/ponytail/SKILL.md](<../external_repos/DietrichGebert/ponytail/skills/ponytail/SKILL.md>) · [benchmarks/results/2026-10-07-agentic.md](<../external_repos/DietrichGebert/ponytail/benchmarks/results/2026-10-07-agentic.md>) · [skills/ponytail-review/SKILL.md](<../external_repos/DietrichGebert/ponytail/skills/ponytail-review/SKILL.md>)

#### R51 · emilkowalski/skills

[GitHub](https://github.com/emilkowalski/skills) · Revision: `2d228630ba1446365f614a108cb8252f1feda202` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Emil Kowalskis Sammlung übersetzt Design-Erfahrung in begrenzte, konkrete Arbeitsweisen. Animation beginnt mit der Frage nach Häufigkeit und Zweck; häufig ausgelöste Bedienung kann ohne Bewegung besser funktionieren. Vorhandene Tokens, einfache Werkzeuge, reduzierte Bewegung und Pointer-Gating gehören zur Umsetzung. Der Prototyping-Skill verlangt echte Alternativen auf benannten Achsen und einen isolierten, funktionsfähigen Vergleich, bevor eine Richtung integriert wird. Break UI ergänzt die ästhetische Sicht durch plausible Grenzdaten aus Schemas und realen Namens-, Zahlen- und Inhaltsmustern. Die Daten wechseln an der regulären Boundary; schmale Container, Zoom, leere Listen und Singularfälle werden sichtbar geprüft. Dadurch ergänzen sich Geschmacksbildung und Robustheit. Die strengen Kurven- und Dauerregeln bleiben die Philosophie des Autors; technische Leistungsbehauptungen und das tatsächliche Bewegungsgefühl erfordern eigene Beobachtung.

**Übertragbare Verfahren:**

- Vor Animation zuerst Nutzungshäufigkeit und konkreten Zweck bestimmen; häufige Bedienung kann bewusst ohne Bewegung bleiben.
- Vorhandene Tokens nutzen, mit dem einfachsten passenden Werkzeug arbeiten und Reduced Motion sowie Pointer-Gating sofort mitliefern.
- Drei echte Designrichtungen auf benannten Achsen in isoliertem, funktionsfähigem Prototyp vergleichen.
- Worst-Case-Daten an derselben Datenboundary wie reguläre Fixtures einspeisen, statt die zu prüfende Komponente umzubauen.
- Schemas, optionale Felder, leere/einzelne/große Listen, 320px, 200%-Zoom und unterstützte RTL-/Dark-Zustände prüfen.

**Voraussetzungen:** Reale Produktkontexte und idealerweise Browser-/Gerätetests. Passende Frontend-Werkzeuge und bestehende Design-Tokens.

**Weitere Grenzen und Voraussetzungen der Aussage:** Die strikten Dauer-, Kurven- und Keyboard-Regeln sind eine Designphilosophie, keine universellen Gesetze. Technische Aussagen wie GPU-Beschleunigung sind kontextabhängig und wurden hier nicht profiliert. Visuelles Gefühl und Gesten müssen tatsächlich gesehen/getestet werden; statische Vorschriften ersetzen das nicht.

**Abgleich mit dem Index:** Sammlung und Fokus bestätigt. Stresstest arbeitet bewusst mit plausiblen/schema-begrenzten Daten und trennt Befund von Designentscheidung; das konkretisiert die knappe Indexbeschreibung.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/emilkowalski/skills/README.md>) · [skills/animate/SKILL.md](<../external_repos/emilkowalski/skills/skills/animate/SKILL.md>) · [skills/prototype/SKILL.md](<../external_repos/emilkowalski/skills/skills/prototype/SKILL.md>) · [skills/break-ui/SKILL.md](<../external_repos/emilkowalski/skills/skills/break-ui/SKILL.md>)

#### R52 · Jakubantalik/transitions.dev

[GitHub](https://github.com/Jakubantalik/transitions.dev) · Revision: `54fbee8e9d698598b4e7ceabb2fb43ea30beacfc` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Transitions.dev verbindet konkrete CSS-Interaktionen mit einem gemeinsamen semantischen Motionvokabular. Auswahl und Anpassung folgen der Funktion eines Elements: Ein geöffnetes Menü braucht andere Werte als ein zurückhaltender Tooltip. Ein Generator hält Demo und Skillreferenzen zusammen. Zusätzlich kann ein Reveal-System fertige Oberflächen, Glyphen und Bilder aus ihren gemessenen Formen inszenieren; seekbare Varianten eignen sich auch für Videorenderer. Diese Darstellung spielt nach dem Eintreffen des Ergebnisses und ist kein Nachweis tatsächlicher Agentenschritte. Reduced-Motion, Cleanup und geladene Fonts beziehungsweise Bilder gehören zur Integration. Die Mengenangaben sind überholt: Der gelesene Katalog enthält 35 Einträge. Ebenso muss zwischen MIT-Tooling und der eingeschränkten Bibliotheks-/Skilllizenz unterschieden werden, insbesondere bei verkauften Templates und Weiterverteilung. Ohne Browserprüfung bleiben Performance, Unterbrechbarkeit und Barrierefreiheit der konkreten Übernahme offen; Produktionsreife ist zunächst eine Aussage des Repositories.

**Übertragbare Verfahren:**

- Motionmuster anhand des sichtbaren Elements und seiner Funktion auswählen.
- Dauer, Easing, Distanz und Skalierung nach semantischem Einsatzzweck in Tokens vereinheitlichen.
- Demo und Agentreferenzen aus einer gemeinsamen Quelle generieren.
- Reduced-Motion-Varianten, konkrete State-Hooks und JavaScript-Cleanup zusammen übernehmen.
- Aufwendige Generierungsreveal-Effekte nur für seltene Momente nach tatsächlichem Daten-/Layoutabschluss nutzen.
- Für Videowerkzeuge seekbare Darstellung von interaktiv automatisch ablaufender Animation trennen.

**Voraussetzungen:** Passende DOM-Hooks, CSS-Variablen und je Rezept notwendige Orchestrierung. Geladene Fonts und decodierte Bilder vor geometrischer Messung. Lizenz- und Angebotsprüfung für konkrete Inhalte, Templates und kostenpflichtige Funktionen.

**Weitere Grenzen und Voraussetzungen der Aussage:** README nennt 18 Referenzen, Skilltext 32, tatsächlicher gelesener Katalog listet 35: Mengenangaben sind veraltet. Produktionsreife und Accessibility-Audit-Bestehen folgen nicht allein aus vorhandenem Reduced-Motion-Block. Der simulierte Agentenlog ist eine Inszenierung über bereits fertiger UI, kein Beleg wirklicher Verarbeitungsschritte. Gemessene Pixel und Konturen können bei CORS, variablen Fonts und Scrolling abweichen. Bibliotheks-/Skilllizenz enthält Weiterverteilungsbeschränkung, während Tooling MIT ist; kommerzielle Template-Regeln sind zusätzlich planabhängig.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/Jakubantalik/transitions.dev/README.md>) · [skills/transitions-dev/SKILL.md](<../external_repos/Jakubantalik/transitions.dev/skills/transitions-dev/SKILL.md>) · [skills/transitions-ui-generation/SKILL.md](<../external_repos/Jakubantalik/transitions.dev/skills/transitions-ui-generation/SKILL.md>) · [LICENSE](<../external_repos/Jakubantalik/transitions.dev/LICENSE>)

#### R53 · jakubkrehel/make-interfaces-feel-better

[GitHub](https://github.com/jakubkrehel/make-interfaces-feel-better) · Revision: `35545ea1512ad59fa463e6b1f95ca9c052981fe6` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Make-interfaces-feel-better ist ein kleiner, vollständig gelesener Skill einschließlich seiner fünf Fachreferenzen. Er eignet sich für die abschließende Detailprüfung einer Oberfläche: optische Ausrichtung, verschachtelte Radien, stabile Zahlentypografie, verständliche Iconzustände und ausreichend große Bedienflächen. Interaktive Animationen sollen unterbrechbar bleiben; häufig wiederkehrende Handlungen erhalten möglichst wenig Bewegung und immer ein statisches Signal. Besonders übertragbar ist das Reviewformat mit offengelegtem Umfang, konkretem Vorher und Nachher, Nutzerwirkung und verworfenen Alternativen. Browserzustände und langsam abgespielte Bewegung sind Teil der vorgesehenen Verifikation. Seine strikten Zahlenwerte, etwa für Druckskalierung oder Icon-Blur, bleiben gestalterische Heuristiken. Sie müssen zu Marke, Inhalt, Gerät und Zugänglichkeit passen. Auch vereinfachte Aussagen zu GPU-Eigenschaften ersetzen keine Messung. Die Sammlung liefert somit ein präzises Prüfvokabular, aber keinen automatischen Beleg einer guten oder barrierefreien Oberfläche.

**Übertragbare Verfahren:**

- Polish in vorhandenes Styling- und Schriftsystem integrieren statt einen zweiten Stack einzuführen.
- Optische Ausrichtung, konzentrische Flächen und stabile Zahlenbreiten gezielt überprüfen.
- Unterbrechbare Zustandswechsel und zurückhaltende seltene Sequenzen unterscheiden; häufige Interaktionen minimal halten.
- Icons über currentColor und verständliche statische Zustände führen, RTL und zugängliche Namen prüfen.
- Prüfumfang pro Kategorie offenlegen und Vorher/Nachher, Nutzerauswirkung sowie verworfene Alternativen dokumentieren.
- Animationen langsam und in allen relevanten Zuständen prüfen; nicht geprüfte Bereiche beim Urteil nennen.

**Voraussetzungen:** Kenntnis bestehender UI-Konventionen und Zugriff auf relevante Zustände. Für verlässliche Motionbewertung echte Browserinteraktion. Projektspezifische Anforderungen an Barrierefreiheit, Marke und Performance.

**Weitere Grenzen und Voraussetzungen der Aussage:** Exakte Werte für Skalierung, Blur, Stroke und Radius sind kuratierte Heuristiken, keine universellen Produktgesetze. Pauschale Aussagen über GPU-Compositing und Unterbrechbarkeit vereinfachen browserspezifisches Verhalten. Bloßes Befolgen visueller Regeln beweist keine Accessibility-Konformität. Ein Review-Finding-Cap begrenzt Berichtslänge und darf nicht als vollständiger Fehlerfreiheitsnachweis gelesen werden. Die Skillregeln wurden vollständig gelesen, keine Oberfläche praktisch verändert oder geprüft.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/jakubkrehel/make-interfaces-feel-better/README.md>) · [skills/make-interfaces-feel-better/SKILL.md](<../external_repos/jakubkrehel/make-interfaces-feel-better/skills/make-interfaces-feel-better/SKILL.md>) · [skills/make-interfaces-feel-better/typography.md](<../external_repos/jakubkrehel/make-interfaces-feel-better/skills/make-interfaces-feel-better/typography.md>) · [skills/make-interfaces-feel-better/surfaces.md](<../external_repos/jakubkrehel/make-interfaces-feel-better/skills/make-interfaces-feel-better/surfaces.md>) · [skills/make-interfaces-feel-better/animations.md](<../external_repos/jakubkrehel/make-interfaces-feel-better/skills/make-interfaces-feel-better/animations.md>) · [skills/make-interfaces-feel-better/icons.md](<../external_repos/jakubkrehel/make-interfaces-feel-better/skills/make-interfaces-feel-better/icons.md>) · [skills/make-interfaces-feel-better/performance.md](<../external_repos/jakubkrehel/make-interfaces-feel-better/skills/make-interfaces-feel-better/performance.md>)

#### R54 · Leonxlnx/taste-skill

[GitHub](https://github.com/Leonxlnx/taste-skill) · Revision: `12af471f627f866411b4bd785b19646d3672784c` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Taste Skill verbindet kundenspezifische Bestandsaufnahme, mehrere Designrichtungen, eine eigene Gestaltungsidee und einen Browserfeedbackzyklus. Für Apps ist besonders die Forderung nach ehrlichen Daten übertragbar: Summen und Deltas entstehen aus denselben sichtbaren Zeilen, wiederholte Fakten aus einer Variablen; fehlende Werte, Null und Prognosen bleiben unterscheidbar. Websites und Arbeitsoberflächen bekommen bewusst verschiedene Regeln. Die vollständig gelesene Forschungsgrundlage begrenzt jedoch die starken Qualitätsbehauptungen. Kuratierte Galerieseiten wurden durch Modelljuroren aus Screenshots bewertet; mehrere Verbote sind ausdrücklich Geschmack des Autors und widersprechen beobachteten erfolgreichen Seiten. Eigene Blindtests verlieren teilweise trotz fehlerfreiem Inspector gegen die Baseline. Die Appstudie umfasst nur 23 Desktopbilder, keine mobilen oder Fehlerzustände. Deshalb sind konkrete Messungen, Vorher-Nachher-Vergleich und Produktionsbuildprüfung wertvoller als das bloße Erfüllen des Hausstils. Die vorgeschriebene Mindestmenge an Webseitenbewegung sollte nicht ungeprüft als allgemeines UX-Ziel übernommen werden.

**Übertragbare Verfahren:**

- Vor Gestaltung klientenspezifische Merkmale, echte Assets, Zielaktion und belegbare Inhaltsclaims inventarisieren.
- Mehrere Richtungen als Suchraum verwenden und die Wahl an ein Motiv binden, das den Wettbewerbertausch nicht übersteht.
- Webseiten und Arbeitsoberflächen mit unterschiedlichen Dichte-, Motion- und Strukturregeln gestalten.
- Appdaten aus einer Quelle rendern, Summen und Deltas aus sichtbaren Teilen berechnen, Null, fehlend, veraltet und Prognose unterscheiden.
- Automatische Stilprüfung mit Screenshotkritik und höchstens drei gezielten Korrekturrunden ergänzen.
- Redesign gegen einen aufgenommenen Ausgangszustand und auf dem Produktionsbuild prüfen; vorhandenen Stack bewahren.

**Voraussetzungen:** Node und Browser für Inspector, Netzwerk nur für Bildsuche. Reale Produktinformationen oder ausdrücklich auszuwechselnde Beispieldaten, dokumentierte Medienrechte. Genügend Budget für sehr umfangreichen Design-/Prüfablauf und Anpassung an die Marke.

**Weitere Grenzen und Voraussetzungen der Aussage:** Studie nutzt Modellbewertungen von Momentaufnahmen, keine Nutzerstudie oder menschliche Jury; kuratierte Galerien sind selektiert. Mehrere verbindliche Verbote widersprechen sogar den beobachteten starken Seiten und sind ausdrücklich Hausgeschmack. Eigene Blindtests zeigen trotz null Inspectorfehlern teils schlechtere Ergebnisse als Baseline; spätere Runden nutzen schon bekannte Briefs. Webseiten-Motion-Floor von mindestens acht bewegten Elementen kollidiert mit anderen Skills und ist kein empirischer Nutzennachweis. App-Studie enthält 23 Desktopbilder ohne mobile, Loading- oder Errorzustände; dazugehörige Regeln sind Erweiterungen aus Hausgeschmack/Tests. Automatische Lizenzfilter und Credits sind kein eigener rechtlicher Nutzungsnachweis.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/Leonxlnx/taste-skill/README.md>) · [skills/taste-skill/SKILL.md](<../external_repos/Leonxlnx/taste-skill/skills/taste-skill/SKILL.md>) · [skills/taste-skill/references/research.md](<../external_repos/Leonxlnx/taste-skill/skills/taste-skill/references/research.md>) · [skills/taste-skill/references/app-screens.md](<../external_repos/Leonxlnx/taste-skill/skills/taste-skill/references/app-screens.md>)

#### R55 · millionco/react-doctor

[GitHub](https://github.com/millionco/react-doctor) · Revision: `84ad0c8d0df7a3ab7d26946367fae3bc39c100d0` · README-Vertrag; Skill-Vertrag; statischer Auswertungscode; Lizenztext; kein eigener Scan

React Doctor ergänzt beratende Frontend-Skills um deterministische Diagnosen. Sein Nutzen liegt in der Trennung von vollständigem Audit, neu eingeführten Findings, geänderten Zeilen und kontextuell betroffenen Funktionen oder Elementen. Für wiederverwendbare Baselines verlangt der Skill dieselben Versionen, Regeln und Filtereinstellungen. Der gelesene Auswertungscode kennzeichnet eine unvollständige Baseline ausdrücklich als eingeschränkt. Ein Health-Score bleibt dennoch ein Aggregat der aktiven Regeln und beweist keine allgemeine Produktqualität. Beim Baseline-Abgleich können gleichbleibende Finding-Anzahlen neue Positionen verdecken. Ergänzende Performance-Traces beobachten eine tatsächliche Interaktion und sollten als sensible lokale Daten behandelt werden. Die Paket-README nennt MIT; der gelesene Root-Lizenztext enthält zusätzliche Zustimmungsvorbehalte. Außerdem lädt der Reparatur-Skill Anleitungen live nach. Für reproduzierbare Nutzung sind daher Version, aktive Regeln, geladene Anleitungen und tatsächlicher Prüfumfang festzuhalten.

**Übertragbare Verfahren:**

- Deterministische Diagnosen vor agentischer Reparatur erheben.
- Vollbestand, neue Findings, geänderte Zeilen und kontextuelle Eigentümer getrennt prüfen.
- Baselines an identische Version, Regeln und Source-Filter-Konfiguration binden.
- Unvollständige Baseline-Abdeckung ausdrücklich als degraded ausgeben.
- Reale langsame Interaktion über lokale DevTools-Traces analysieren.

**Voraussetzungen:** Unterstütztes React-Projekt und geeignete Laufzeit; Runtime-Trace benötigt interaktive Browserbedienung. Regelkonfiguration und Baseline müssen kompatibel sein; Lizenztext gesondert beachten.

**Weitere Grenzen und Voraussetzungen der Aussage:** Health-Score ist Regelaggregat, kein allgemeiner Qualitätsbeweis. Gleiche Regel-/Datei-Anzahl kann neue Positionen bei Baseline-Matching unsichtbar lassen. Skill lädt kanonischen Reparatur-Prompt live; spätere Inhalte sind dadurch nicht an den gelesenen Commit gebunden. Paket-README sagt MIT, Root-LICENSE enthält zusätzliche Zustimmungsvorbehalte für ML-Datennutzung und bestimmte kommerzielle Angebote. Telemetrie ist laut README standardmäßig aktiv und abschaltbar.

**Abgleich mit dem Index:** Root-README ist Pfadzeiger; tatsächliche Paket-README gelesen. Index benennt die modifizierte Lizenz genauer als Paket-README.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [packages/react-doctor/README.md](<../external_repos/millionco/react-doctor/packages/react-doctor/README.md>) · [skills/react-doctor/SKILL.md](<../external_repos/millionco/react-doctor/skills/react-doctor/SKILL.md>) · [packages/react-doctor/src/cli/utils/build-final-cli-scan-outcome.ts](<../external_repos/millionco/react-doctor/packages/react-doctor/src/cli/utils/build-final-cli-scan-outcome.ts>) · [packages/react-doctor/src/cli/utils/filter-diagnostics-by-changed-lines.ts](<../external_repos/millionco/react-doctor/packages/react-doctor/src/cli/utils/filter-diagnostics-by-changed-lines.ts>) · [LICENSE](<../external_repos/millionco/react-doctor/LICENSE>)

#### R56 · nextlevelbuilder/ui-ux-pro-max-skill

[GitHub](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · Revision: `d14efff8ed1faa4187f004f79926f428c8074ec7` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

UI UX Pro Max verbindet kuratierte Designkataloge mit lokaler Suche und einem Designsystem-Generator. Die Methode wird erst durch ihren Suchvertrag brauchbar: Eine neue Produktsprache nutzt das Gesamtsystem, ein einzelner Komponentenfehler eine gezielte Domain und die Implementierung den tatsächlich vorhandenen Stack. Treffer müssen hinsichtlich Identität, Kategorie und Plattform geprüft werden; erfolglose Suche soll nicht endlos mit neuen Begriffen wiederholt werden. MASTER.md und seitenspezifische Abweichungen erhalten Entscheidungen über Sitzungen hinweg. Für bestehende Anwendungen empfiehlt die Vorlage semantische Tokens und kleine überprüfte Migrationsschritte. Das ergänzt geschmacksorientierte Design-Skills durch Systematik. Katalogbreite und BM25-Ranking beweisen aber weder Nutzbarkeit noch Conversion oder Barrierefreiheit. Mobile-Regeln und Web-Anforderungen bleiben getrennt anzuwenden; illustrative Beispiele sowie Premium-Funktionen zählen nicht als gemessene Leistung der offenen Basis.

**Übertragbare Verfahren:**

- Für systemweite Richtung Designsystem, für einzelne Bugs gezielte Domain und für Umsetzung bekannten Stack wählen.
- Eine dominante Suchabsicht mit wenigen Begriffen; Ergebnisidentität und Kategorie prüfen, maximal gezielt wiederholen, ungeprüfte Treffer nicht persistieren.
- MASTER.md als gemeinsame Basis und Page-Dateien nur als abweichende Regeln laden.
- Bestehende semantische Tokens schrittweise migrieren und pro Komponentenbatch Kontrast, Zustände und Responsivität prüfen.
- Aktive, ergänzende, veraltete und versionsbezogene Datensätze getrennt halten.
- Katalogrefresh liefert Kandidaten und Diffs zur Prüfung; normale Entwicklung nutzt offline reproduzierbare Snapshots.

**Voraussetzungen:** Python 3 Standardbibliothek für Suche; richtiger Produktkontext, Plattform und installierter Styling-Stack. Tatsächliche UI-Prüfung und gegebenenfalls freigegebene Assets.

**Weitere Grenzen und Voraussetzungen der Aussage:** BM25 und Regeln sind kuratierte Suche, kein unabhängiges Designurteil oder Nachweis von Conversion und Barrierefreiheit. README verspricht automatische vollständige Systeme; Skill grenzt gezielte Aufgaben auf kleine Suche ein. Große Vorlage enthält plattformspezifische Mobile-Regeln und teils generische Defaults; unpassende Übertragung auf Web vermeiden. Premium-Fähigkeiten und illustrative Demos nicht als getestete OSS-Leistung zählen.

**Abgleich mit dem Index:** Katalogzahlen und Master/Override-Modell bestätigt; konkrete Query-Verifikation und plattformspezifische Grenzen vertieft.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/nextlevelbuilder/ui-ux-pro-max-skill/README.md>) · [src/ui-ux-pro-max/templates/base/skill-content.md](<../external_repos/nextlevelbuilder/ui-ux-pro-max-skill/src/ui-ux-pro-max/templates/base/skill-content.md>)

#### R57 · nexu-io/open-design

[GitHub](https://github.com/nexu-io/open-design) · Lokale Dateikopie ohne eigene Git-Revision · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Open Design macht Skills zu einer Produktoberfläche: Ein Brief wird mit funktionalem Wissen, Render-Template, Brandvertrag und Pluginmaterial zu bearbeitbaren Dateien zusammengesetzt. Deklarative Adapter überlassen Modell- und Toolschleife den vorhandenen Coding-CLIs; Projektkopien aktiver Ressourcen schützen die Ursprungsbibliothek. Diese sinnvolle Modularität darf nicht mit einheitlicher Isolation verwechselt werden. Die vollständig gelesene Adapterdokumentation nennt zahlreiche Modi ohne interaktive Freigabe, unter Windows beziehungsweise WSL auch vollständigen Codex-Dateizugriff, und automatische Pi-Dialogbestätigung. Das Sandboxiframe begrenzt die Vorschau, nicht diese Agentenrechte. Ebenso schließen lokale Projekte und BYOK externe Modellaufrufe oder Telemetrie nicht aus: Inhaltsfreigaben sind optional, bestimmte Sicherheitsdiagnosen bleiben in konfigurierten Builds aktiv. README und Roadmap unterscheiden sich bei einigen Funktionsversprechen. Der Bestand besitzt keine eigene Git-Metadatenstruktur; seine hier geprüfte Identität wird deshalb durch Dateihashes statt eines vermeintlichen Elternrepository-HEAD dokumentiert.

**Übertragbare Verfahren:**

- Funktionale Skills, Renderingvorlagen, Designsysteme und Plugins als unterschiedliche Katalogobjekte führen.
- Brandvertrag und Tokenmaterial mit bedarfsweise geladenen reichhaltigen Ressourcen zusammensetzen.
- Aktive Ressourcen pro Projekt als echte private Kopien stagen, damit Änderungen die Ursprungsbibliothek nicht verändern.
- Agentadapter als deklarative Datenverträge auf eine gemeinsame Erkennungs-, Start- und Streamengine setzen.
- Erkannte Binärverfügbarkeit, Authentifizierung, Modellfähigkeit, Promptannahme und tatsächlichen Runabschluss getrennt behandeln.
- Dateibasierten kanonischen Artefaktbestand von API-Textblock-Handoff und Sandboxvorschau unterscheiden.

**Voraussetzungen:** Passender CLI-/Modellzugang und bewusste Auswahl der effektiven Runtime-Rechte. Für Quellbetrieb Node24/pnpm und native Desktop-/Daemon-Abhängigkeiten. Prüfung der jeweiligen Drittinhaltslizenzen und Provider-/Telemetrieflüsse.

**Weitere Grenzen und Voraussetzungen der Aussage:** Keine eigene .git vorhanden: ungepinnter Dateibestand, Revisionsnachweis nur über gelesene Dateihashes. Sandboxiframe und Loopbackdaemon begrenzen nicht automatisch die Agentenprozesse; viele Adapter deaktivieren interaktive Freigaben. Codex nutzt laut Adapterdokument auf Windows/WSL danger-full-access, Pi bestätigt Dialoge automatisch. Lokale Datenhaltung und BYOK schließen externe Modellaufrufe, optionale Inhalts-/Tooltraces und stets aktive Sicherheitstelemetrie nicht aus. README und Roadmap widersprechen sich bei angeblich fertigen Tweaks, Migrationen und weiteren Fähigkeiten. Als universell bezeichnete Gestaltungsverbote sind Geschmacksvorgaben, keine allgemeine Wahrheit. Read-only-MCP-Behauptung darf nicht auf gesamte Generierungs- und Pluginoberfläche übertragen werden.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/nexu-io/open-design/README.md>) · [docs/skills-protocol.md](<../external_repos/nexu-io/open-design/docs/skills-protocol.md>) · [docs/agent-adapters.md](<../external_repos/nexu-io/open-design/docs/agent-adapters.md>) · [PRIVACY.md](<../external_repos/nexu-io/open-design/PRIVACY.md>)

#### R58 · pbakaus/impeccable

[GitHub](https://github.com/pbakaus/impeccable) · Revision: `936867543ac2576920d663cc9803597f6044f3ac` · README-Vertrag; Quell-Skill und zwei vollständige Playbooks; kein eigener Detektor-/Browserlauf

Impeccable verbindet Designarbeit mit dauerhaftem Produktkontext und überprüfbaren Befunden. PRODUCT.md hält Zweck, Zielgruppe und belastbare Inhalte fest; DESIGN.md und Oberflächenbriefe tragen visuelle Entscheidungen. Die Modi Persuade, Operate, Read und Experience richten Gestaltung am jeweiligen Besuchsziel aus. Ein Dashboard benötigt dabei andere Ausdrucksstärke als eine Kampagne. Der Quell-Skill relativiert pauschale Anti-Pattern-Verbote ausdrücklich durch den konkreten Brief und bestehende Identität. Technische Audits sollen messbare Befunde getrennt von gestalterischem Urteil berichten. Ein gerendertes Mobilformat beweist beispielsweise noch keine funktionierende Touch-Geste. Der deterministische Detektor liefert zusätzliche Hinweise, keine vollständige Qualitäts- oder Accessibility-Abnahme. Auch die Infrastruktur verdient Aufmerksamkeit: Hooks können die Engine automatisch laden, Live-Mode kann ein Projektkommando ausführen, und die visuelle Roll-API bleibt trotz abgeschalteter Telemetrie aktiv. Diese Funktionen benötigen eine passende Vertrauens- und Reproduzierbarkeitsentscheidung.

**Übertragbare Verfahren:**

- Dauerhafte Produktfakten von visueller Richtung und einzelner Oberfläche trennen.
- Erfolg pro Oberfläche als Persuade, Operate, Read oder Experience bestimmen.
- Refinement mit bestehender Identität und Redesign mit bewusster Richtungsänderung unterscheiden.
- Technische Audit-Findings von visuellem Urteil trennen und jeden Fehlalarm im Kontext prüfen.
- Viewport-Bild und tatsächlich synthetisierte Touch-Geste als unterschiedliche Nachweise behandeln.
- Aktive Hook-/Ignore-Konfiguration und Attribution alter Findings offenlegen.

**Voraussetzungen:** Skill und Engine; Browser für gerenderte Prüfung, bewusste Projekt-/Hook-Vertrauensentscheidung. Reale Produktinhalte, visuelle Ausgangsevidenz und klarer Zielscope.

**Weitere Grenzen und Voraussetzungen der Aussage:** Ein sauberer62-Regel-Detektor ersetzt weder visuelle noch Accessibility-Abnahme. README pauschale Font-/Stilverbote werden im Skill durch Brief gewinnt und Operate/Read-Präzision relativiert. Roll-API bleibt funktionaler Netzaufruf trotz Telemetrie-Opt-out. Hooks können Binarydownloads unabhängig von Modell-Toolfreigabe auslösen. Live-Mode führt optionales Projekt-Validierungsscript mit Benutzerrechten aus; nur vertraute lokale Projekte. README craft als Vollworkflow, Skill bereits deprecatedAlias; Dokumentation driftet.

**Abgleich mit dem Index:** Index korrekt62Regeln; gelesener Quell-Skill führt craft bereits als veralteten Alias.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/pbakaus/impeccable/README.md>) · [skill/SKILL.src.md](<../external_repos/pbakaus/impeccable/skill/SKILL.src.md>) · [skill/reference/audit.md](<../external_repos/pbakaus/impeccable/skill/reference/audit.md>) · [skill/reference/shape.md](<../external_repos/pbakaus/impeccable/skill/reference/shape.md>)

#### R59 · petergyang/human-review

[GitHub](https://github.com/petergyang/human-review) · Revision: `f9a55812f6f37e2c53da6ec26c52ef7a489485d6` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Human Review verbindet visuelles Redigieren mit einer präzisen Agentenübergabe. Menschen bearbeiten Text und Formatierung direkt, verschieben Blöcke oder kommentieren markierte Stellen; der Agent erhält alle Seiten als gemeinsamen Batch. Entscheidend ist die Unterscheidung zwischen bereits gespeicherten HTML-Änderungen und Feedback für Markdown oder laufende Apps: Letzteres muss in die eigentliche Quelldatei zurückgeführt werden. Quittiert wird erst nach Übernahme aller Änderungen und temporären Bilder. Der gelesene Server implementiert persistente Batches, eindeutige Zustellung, Loopback-Bindung, zufällige API-Token und einen optionalen Hashvergleich gegen veraltete Speicherungen. Das ist ein statischer Befund, kein Laufnachweis oder vollständiges Sicherheitsaudit. Die Wartefunktion hängt vom Host ab: Codex wird nach einem beendeten Zug durch gesendetes Feedback nicht automatisch geweckt. Außerdem entfernt der App-Proxy Cookies sowie CSP- und Frame-Header; die Review-Ansicht kann deshalb vom geschützten Original abweichen.

**Übertragbare Verfahren:**

- Menschliches Review als expliziten Zustandsübergang mit wartendem Empfänger, einem gesendeten Batch und abschließender Quittierung modellieren.
- Exakte Benutzerformulierungen und Formatierung erhalten, über Quote plus Präfix/Suffix verankern und bei generierten Seiten in die eigentliche Quelle übertragen.
- Bereits gespeicherte HTML-Edits von nur im Feedback vorliegenden Markdown- oder App-Änderungen durch edits_saved unterscheiden; vor dem Weiterarbeiten die aktuelle Datei erneut lesen.
- Feedback bis zur Quittierung persistent halten, neue Änderungen während einer laufenden Bearbeitung separat zustellen und vor dem Ack zwischengespeicherte Bilder übernehmen.
- Lokale API mit pro Serverstart zufälligem Header-Token, expliziter Loopback-Hostprüfung und begrenzten Requestgrößen versehen; bloßes localhost nicht als ausreichenden Schreibschutz ansehen.
- Konkurrierende HTML-Speicherungen mit einer Versionsvorbedingung abweisen, wenn baseHash mitgesendet wird, und geschlossene oder ersetzte Polls ausdrücklich beenden.

**Voraussetzungen:** Node und Browser sowie zugängliche Quelldatei beziehungsweise lokaler Entwicklungsserver. Aktiver Agentenzug oder Host mit tatsächlicher Hintergrund-Benachrichtigung; Codex benötigt nach Zugende eine neue Benutzernachricht. Bewusster Umgang mit HTML-Autosave, lokalen Assets, dauerhaftem Review-Zustand und laufenden Seitenskripten.

**Weitere Grenzen und Voraussetzungen der Aussage:** Das Skill widerspricht sich bei Warteanweisungen: zunächst kein Timeout, später begrenzte Polls mit Timeout; Schritt 4 nennt erneut Hintergrund-Poll trotz hostabhängiger Einschränkungen. Der Server bindet Loopback, validiert lokale HTTP-Ziele und prüft Redirects erneut; das ist kein Audit der gerenderten HTML-Skripte oder ihrer externen Ressourcen. Der App-Proxy entfernt Cookies und Frame/CSP-Header; die Review-Ansicht kann daher vom authentifizierten Original und dessen Schutzmechanismen abweichen. Hashbasierter Schutz vor veralteten Autosaves ist im gelesenen Endpoint nur aktiv, wenn baseHash ein String ist. Client, Store und Frame-Policy wurden nicht vollständig zusätzlich auditiert. Lokale Ausführung ohne eigenen Cloud-Account beweist nicht die Fehlerfreiheit, Wiederherstellbarkeit aller Sonderfälle oder automatische Wiederaufnahme eines bereits beendeten Agentenzugs.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/petergyang/human-review/README.md>) · [src/SKILL.md](<../external_repos/petergyang/human-review/src/SKILL.md>) · [src/server.js](<../external_repos/petergyang/human-review/src/server.js>) · [src/paths.js](<../external_repos/petergyang/human-review/src/paths.js>)

#### R60 · shadcn-ui/lint

[GitHub](https://github.com/shadcn-ui/lint) · Revision: `bceee0febd2b84340d1650e338c3458e12bd356d` · README-Vertrag; Vollständig gelesene Dokumentation zu Designsystemen und Agent-Evals; kein eigener Lauf

shadcn/lint übersetzt Teile eines Designsystems in überprüfbare Regeln. Coding Agents erhalten dadurch konkrete Hinweise auf vorhandene Tokens, Komponentenvarianten und Zuständigkeiten, statt allgemeiner Aufforderungen zu konsistentem Design. Besonders nützlich ist die Trennung von zulässigem Layout und geschütztem Erscheinungsbild einer Komponente. Die Methode funktioniert auch ohne shadcn/ui, setzt jedoch Tailwind v4 und gepflegte Verträge voraus. Dokumentierte Agent-Evals vergleichen mehrere Reparaturrunden und ergänzen eine Kontrolle mit Regeln ohne Linter; nur so lässt sich der Nutzen von zusätzlichen Modellturns teilweise trennen. Veröffentlichte Kostenwerte bleiben quellengebundene Messergebnisse. Bei Vue und Svelte ist die Oxlint-Abdeckung auf Script-Blöcke begrenzt. Eigene CSS-Regeln, neue Tokens und dynamische Konstruktionen zeigen außerdem, weshalb Regelkonformität weder vollständige Designqualität noch Accessibility oder eine unveränderliche Produktvorgabe beweist.

**Übertragbare Verfahren:**

- Semantische Tokens, zulässige Klassen und Komponentenvarianten als ausführbare Regeln erfassen.
- Erscheinungsbild und Layoutverantwortung über no-restyle sowie explizite Komponentenverträge trennen.
- Diagnosen mit konkretem Problem, Begründung und vorhandener Variante beziehungsweise Token-Alternative formulieren.
- Regelkonfiguration und Änderungen am Designsystem gemeinsam prüfen, damit neue Tokens keine unbemerkte Ausnahme werden.
- Agent-Evals um Regeln-ohne-Linter-Kontrollen und begrenzte Reparaturrunden ergänzen, statt zusätzliche Modellturns als reine Linterwirkung zu zählen.

**Voraussetzungen:** Tailwind v4; ESLint ab 9.30 oder Oxlint ab 1.80; Node.js ab 20.19 beziehungsweise passende Bun-Version. Definierte Theme-Tokens und Komponentenverträge; shadcn/ui selbst ist nicht erforderlich.

**Weitere Grenzen und Voraussetzungen der Aussage:** Oxlint prüft Vue und Svelte nur innerhalb von Script-Blöcken; CSS und Markup sind damit nicht vollständig abgedeckt. Neue Theme-Tokens, CSS oder dynamische Konstruktionen können Regelabsichten umgehen; die ausgewiesenen Red-Team-Fälle sind kein Vollständigkeitsbeweis. Eval-Kosten und Erfolgswerte stammen aus projektspezifischen Agent-Läufen; Roh-Runs wurden hier nicht ausgeführt oder unabhängig nachgerechnet. Before/After ohne Kontrollgruppe vermischt Linterwirkung mit zusätzlicher Arbeitszeit; der dokumentierte Regeln-ohne-Linter-Vergleich ist aussagekräftiger. Komponentenverträge werden nach letzter passender Regel ausgewählt, nicht beliebig zusammengeführt; Konfigurationsfehler verändern die Aussage.

**Abgleich mit dem Index:** Index bestätigt; eval.md beschreibt teils ältere Claude-zentrierte Auswertungen, während die README weitere Modellläufe nennt. Abgeschlossene und unvollständige Läufe sind auseinanderzuhalten.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/shadcn-ui/lint/README.md>) · [docs/evals.md](<../external_repos/shadcn-ui/lint/docs/evals.md>) · [docs/design-systems.md](<../external_repos/shadcn-ui/lint/docs/design-systems.md>)

#### R61 · shadcn-ui/ui

[GitHub](https://github.com/shadcn-ui/ui) · Revision: `c2985e43ad554fae11c05e0700a5b582e37a7b03` · README-Vertrag; Vollständig gelesene Grundlagen-, Theming- und Registry-Dokumentation; kein eigener Lauf

shadcn/ui liefert veränderbaren Komponentenquellcode und eine Infrastruktur für die eigene UI-Bibliothek. Der wesentliche Transfer liegt im Zusammenspiel von Komposition, semantischen Tokens und geregelter Verteilung. Hintergrund und Textfarbe bilden fachliche Paare; Dark Mode und Radius-Skalen bleiben dadurch systematisch statt als Sammlung lokaler Ausnahmen. Registries können neben Komponenten auch Hooks, Seiten und Konfigurationen transportieren. Das Schema erleichtert deren Nutzung, bestätigt aber weder Herkunft noch Sicherheit fremder Inhalte. Der Besitz des Codes erleichtert gezielte Anpassungen und verlangt zugleich Pflege lokaler Abweichungen. Updates von Primitive-Abhängigkeiten und Änderungen am übernommenen Komponentencode sind deshalb getrennt zu betrachten. Die vollständig gelesenen Kerndokumente erklären diesen Ansatz; sie belegen keine umfassende Funktions- oder Accessibility-Abnahme aller Bausteine. Für ein konkretes Produkt braucht das System weiterhin eigene Designentscheidungen, Zustandsprüfungen und Laufzeitbeobachtung.

**Übertragbare Verfahren:**

- Komponentenquellcode im eigenen Projekt besitzen und durch Komposition erweitern.
- Semantische Farbpaare wie background/foreground und primary/primary-foreground zentral über Theme-Variablen definieren.
- Dark Mode und Radius-Skalen als zusammenhängendes Tokensystem statt einzelner Sonderwerte pflegen.
- Registries als schemaorientierten Verteilweg für Komponenten, Hooks, Seiten und Konfigurationen nutzen.
- Änderungen an eigenem Komponentencode von Updates zugrunde liegender Primitive-Abhängigkeiten unterscheiden.

**Voraussetzungen:** Passendes Framework- und Styling-Setup sowie Bereitschaft, übernommenen Quellcode selbst zu pflegen. Vertrauensprüfung für Registry-Inhalte und ihre Abhängigkeiten vor einer tatsächlichen Übernahme.

**Weitere Grenzen und Voraussetzungen der Aussage:** Codebesitz ermöglicht Anpassung, erzeugt aber Verantwortung für lokale Abweichungen und spätere Aktualisierungen. Eine offene Registry kann fremden Code und Abhängigkeiten verteilen; ein einheitliches Schema bestätigt deren Vertrauenswürdigkeit nicht. Die gelesenen Kerndokumente belegen Architektur und Theming-Vertrag, keine Funktions- oder Accessibility-Abnahme aller Komponenten. Standardkomponenten und Tokens ersetzen keine eigenständige Produktgestaltung. Dokumentierte Neuinstallation zum Wechsel bestimmter Theming-Optionen ist eine Projektanleitung und wurde hier weder angewandt noch als sichere Migration geprüft.

**Abgleich mit dem Index:** Die Grundarchitektur bestätigt den Index. Dessen neuere Skill-, Showcase- und Helper-Einzelheiten wurden in dieser bewusst begrenzten Auswahl zentraler Dokumente nicht vollständig nachgeprüft.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/shadcn-ui/ui/README.md>) · [apps/v4/content/docs/(root)/index.mdx](<../external_repos/shadcn-ui/ui/apps/v4/content/docs/(root)/index.mdx>) · [apps/v4/content/docs/(root)/theming.mdx](<../external_repos/shadcn-ui/ui/apps/v4/content/docs/(root)/theming.mdx>) · [apps/v4/content/docs/registry/index.mdx](<../external_repos/shadcn-ui/ui/apps/v4/content/docs/registry/index.mdx>)

#### R62 · shadcn/improve

[GitHub](https://github.com/shadcn/improve) · Revision: `cac56e1ebd3c279aa9153616cfeac7b174ab90f9` · vollständige README und ausgewählte statische Dokument-/Codebelege; kein eigener Lauf

Improve behandelt den Plan als eigenständiges Arbeitsprodukt. Ein leistungsfähiger Advisor versteht zunächst Code, Absicht und bestehende Entscheidungen, prüft anschließend die zitierten Findings selbst und schreibt nur ausgewählte Umsetzungspläne. Diese enthalten konkrete Dateien, Codeausschnitte, Prüfkommandos, Grenzen und Stopps bei unerwartetem Zustand. Revisionsbindung und späteres Reconcile halten sie über Sitzungen hinweg brauchbar. Ein separater Executor kann in einem Worktree arbeiten; der Advisor beurteilt seinen Diff und überlässt die Integration dem Verantwortlichen. Besonders sinnvoll sind dokumentierte Ablehnungen, damit bekannte Fehlalarme nicht immer wiederkehren. Die wirtschaftliche Rollenverteilung bleibt eine Hypothese und muss Gesamtkosten einschließlich Planung und Nacharbeit berücksichtigen. Auch maschinenprüfbare Done-Kriterien ersetzen keinen vollständigen fachlichen Vertrag. Der gelesene historische Beispielplan warnt selbst vor ungeprüfter Wiederverwendung. Diese Lektüre aktiviert weder Ausführung noch Veröffentlichung von Issues.

**Übertragbare Verfahren:**

- Repo, Intent, Architekturentscheidungen und tatsächliche Prüfkommandos vor dem Audit erfassen.
- Subagent-Befunde an zitierten Stellen nachprüfen und verworfene Findings dauerhaft festhalten.
- Pläne mit Revision, Codeausschnitten, Scope, Prüfschritten und STOP-Bedingungen schreiben.
- Getrennte Executor-Änderungen gegen den Plan prüfen und einen veralteten Backlog regelmäßig abgleichen.

**Voraussetzungen:** Zugänglicher Projektbestand und prüfbare Build-/Test-/Lint-Verfahren oder eine offen benannte fehlende Baseline. Für delegiertes Execute ein Host mit Subagents und getrennten Worktrees.

**Weitere Grenzen und Voraussetzungen der Aussage:** Stärkeres Planungsmodell und günstigerer Executor sind eine wirtschaftliche Hypothese, kein gemessener universeller Vorteil. Ein erfolgreicher Verifikationsbefehl deckt nur seine tatsächlich erfassten Eigenschaften ab. Der Beispielplan ist ausdrücklich historisch und darf nicht ohne aktuellen Abgleich ausgeführt werden.

**Abgleich mit dem Index:** Methodik bestätigt; das gelesene konkrete Beispiel ist ein veralteter Formatbeleg und kein heute gültiger Implementierungsauftrag.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/shadcn/improve/README.md>) · [skills/improve/SKILL.md](<../external_repos/shadcn/improve/skills/improve/SKILL.md>) · [examples/001-extract-shadow-config-resolution.md](<../external_repos/shadcn/improve/examples/001-extract-shadow-config-resolution.md>)

#### R63 · thedaviddias/Front-End-Checklist

[GitHub](https://github.com/thedaviddias/Front-End-Checklist) · Revision: `e8d14d049010e2ce25afcd5e8609dfcbbe63e47e` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Front-End Checklist macht aus einem zentralen Regelkorpus mehrere Zugänge: Website, kategorisierte Checklisten, Skills und MCP. Die vollständig gelesene README beschreibt 386 Regeln in elf Bereichen von Semantik und Accessibility bis Performance, Sicherheit, SEO und Internationalisierung. Der globale Audit-Skill ist bewusst konservativ: nur belegte Probleme melden, sichere Gegenbeispiele berücksichtigen und bei kleinen Komponenten wenige starke Findings vorziehen. Der URL-Auditcode setzt öffentliche HTTPS-Ziele, Redirectkontrolle, DNS-Prüfung am Verbindungszeitpunkt sowie Größen- und Zeitlimits um. Sein Ergebnis bleibt jedoch eine statische Analyse abgerufenen HTMLs; er führt keine Seite aus und misst weder Core Web Vitals noch vollständige Barrierefreiheit. Kategorieangaben driften zwischen Artefakten. Als Factory-Baustein eignet sich das Muster zentraler Regeln mit gezieltem Retrieval; vollständige Qualitäts- oder Complianceaussagen folgen daraus nicht.

**Übertragbare Verfahren:**

- 386 Regeln in elf Bereichen priorisieren; nur für Projekt und Audit relevante Regeln anwenden.
- Globaler Audit-Skill bevorzugt wenige unmittelbar belegte Findings mit Fundstelle gegenüber hypothetischen Verbesserungslisten.
- Dekorative Bilder, vorhandene Aspect-Ratio-Wrapper, clientseitige Formbehandlung und Next-Metadata als gültige Gegenbeispiele berücksichtigen.
- Einheitlichen Content in mehrere Oberflächen generieren und Struktur-/Quellchecks von inhaltlicher Abnahme trennen.
- URL-Audit erlaubt nur öffentliche HTTPS-Ziele, prüft jeden Redirect und DNS auch beim Verbinden und begrenzt Zeit und Größe.

**Voraussetzungen:** Passender lokaler oder gehosteter MCP-Server beziehungsweise gezielt ausgewählte Skills; Browser für echte Interaktionsmessung. Regeln anhand eigener Plattform und geltender Anforderungen konkretisieren.

**Weitere Grenzen und Voraussetzungen der Aussage:** audit_url führt kein JavaScript aus, misst keine Core Web Vitals und zertifiziert keine Accessibility. README/Global-Skill sprechen teils von rendered/quick audit, Code stellt ausschließlich abgerufenes HTML statisch bereit. Kategorie-Zähler im globalen Skill weichen von README ab; Regeln sind teils redundant und einige SEO-/Privacy-Pauschalen zeit-/kontextabhängig. Kein eigener Auditlauf; die Indexbezeichnung produktionsreif ist daraus nicht geprüft.

**Abgleich mit dem Index:** Monorepo und Generated-Content-Muster bestätigt. Die pauschale Produktionsreife wird nicht übernommen; HTML-Auditgrenzen und Kategorie-Drift konkretisiert.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/thedaviddias/Front-End-Checklist/README.md>) · [skills/frontend-checklist-global/SKILL.md](<../external_repos/thedaviddias/Front-End-Checklist/skills/frontend-checklist-global/SKILL.md>) · [packages/mcp/src/tools/audit-url.ts](<../external_repos/thedaviddias/Front-End-Checklist/packages/mcp/src/tools/audit-url.ts>)

#### R64 · vercel-labs/agent-skills

[GitHub](https://github.com/vercel-labs/agent-skills) · Revision: `063bee94c3f4df8453406c830b0a7df0f2860278` · vollständige README und ausgewählte statische Dokument-/Codebelege; kein eigener Lauf

Vercels Agent Skills verbinden frameworkbezogene Regeln mit gesonderten Verfahren für Gestaltung, Schreiben, Deployment und Betrieb. Die vertiefte React-Anleitung priorisiert Waterfalls und Bundles vor Mikrooptimierungen; die Kompositionsregeln reduzieren schwer verständliche Boolean-Kombinationen durch explizite Varianten und gemeinsame Zustandsinterfaces. Besonders übertragbar ist der Optimize-Vertrag: Erst konsistente Produktionssignale aus demselben Projekt- und Accountscope sammeln, dann deterministisch begrenzte Kandidaten untersuchen und Empfehlungen an Dateien, Metriken und passende Frameworkversionen binden. Nicht untersuchte oder widerlegte Kandidaten bleiben sichtbar. Streamingdauer wird ausdrücklich nicht pauschal als Verschwendung behandelt. Die Sammlung ist damit keine universelle Liste gleichzeitig anzuwendender Regeln. React-19-Vorgaben, Plattformmetriken und einzelne Werkzeuge brauchen ihre jeweiligen Voraussetzungen. Die gelesenen Verträge belegen weder ausgeführte Optimierung noch vollständige Accessibility. Deployment-Skills wurden nicht aktiviert.

**Übertragbare Verfahren:**

- React-Waterfalls und große Bundles vor kleinen JavaScript-Optimierungen priorisieren.
- Komponenten über klare Komposition und Zustandsinterfaces statt vieler Boolean-Modi gestalten.
- Optimierungskandidaten aus konsistenten Projekt-/Accountmetriken ableiten und erst danach gezielt Code untersuchen.
- Beobachtung, widerlegte Kandidaten, nicht untersuchte Bereiche und Empfehlungen getrennt berichten.
- Frameworkversion und erlaubte Zitate gegen konkrete Empfehlungen prüfen.

**Voraussetzungen:** Zur jeweiligen Bibliotheks- und Frameworkversion passende Regeln. Für Vercel Optimize unter anderem verknüpftes Projekt, eindeutiger Accountscope, geeignete CLI und verfügbare Observability-Daten.

**Weitere Grenzen und Voraussetzungen der Aussage:** Hier wurden drei zentrale Skills vertieft, nicht sämtliche Einzelregeln, Deployment-Scripts oder Adapter ausgeführt. Die Verifikationspipeline des Optimize-Skills ist ein gelesener Vertrag; ihre gesamte Implementierung wurde nicht auditiert. Nicht jede lange Requestdauer ist ein Performanceproblem, insbesondere bei Streaming oder dauerhaftem Workflow.

**Abgleich mit dem Index:** Sammlungsstruktur bestätigt. Der React-Skill führt inzwischen 70 Regeln; der allgemeinere README-/Indexüberblick nennt weiterhin 40+. Verfügbarkeit einzelner React-APIs bleibt versionsabhängig.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/vercel-labs/agent-skills/README.md>) · [skills/react-best-practices/SKILL.md](<../external_repos/vercel-labs/agent-skills/skills/react-best-practices/SKILL.md>) · [skills/composition-patterns/SKILL.md](<../external_repos/vercel-labs/agent-skills/skills/composition-patterns/SKILL.md>) · [skills/vercel-optimize/SKILL.md](<../external_repos/vercel-labs/agent-skills/skills/vercel-optimize/SKILL.md>)

#### R65 · VoltAgent/awesome-design-md

[GitHub](https://github.com/VoltAgent/awesome-design-md) · Revision: `3b605329240ce735b510037cca322f1831fdd7f8` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Awesome DESIGN.md sammelt textuelle Analysen bekannter Websites und macht visuelle Entscheidungen für Agenten lesbar. Die vertieften Beispiele Linear und Claude zeigen semantische Farbrollen, Typografiehierarchien, Oberflächen, Spacing, Komponentenvarianten und responsive Regeln. Übertragbar ist die zusammenhängende Beschreibung einer Designsprache und die Iteration über benannte Tokens. Besonders hilfreich sind die ausdrücklich dokumentierten Lücken: Marketingseiten sind keine vollständigen Produktsysteme, nicht sichtbare Validierungszustände bleiben unbekannt, Animation kann außerhalb des Scopes liegen und proprietäre Schriften benötigen Alternativen. Manche Vorgaben sind sehr kategorisch, etwa beim Umgang mit Hover oder heller Darstellung; sie sind Analyseentscheidungen des Katalogs. Die README umfasst den ganzen Katalog, vertieft wurden zwei Beispiele. Vor Nutzung braucht es ein eigenes Produktbriefing, verfügbare Assets und tatsächliche Interaktions- und Kontrastprüfung. Eine abgelegte Datei garantiert allein keine Anwendung durch jeden Host.

**Übertragbare Verfahren:**

- Designentscheidungen als benannte semantische Rollen statt isolierte Hexwerte dokumentieren.
- Typografie, Spacing, Oberflächenhierarchie, Radius und Komponentenvarianten zusammenhängend beschreiben.
- Marketingoberfläche und tatsächliche Produktoberfläche unterscheiden und nicht untersuchte Zustände ausdrücklich benennen.
- Einzelne Komponenten iterativ über Tokenreferenzen verfeinern.
- Extrahierte Werte gegen aktuelle Oberfläche und lokale Previewdarstellung abgleichen, bevor sie zur Grundlage werden.

**Voraussetzungen:** Eigenes Produktbriefing und ausdrückliche Lektüre der passenden Referenz; keine automatische Datei-Erkennung voraussetzen. Verfügbare Schrift-/Bild-/Markenassets und eigene Kontrast-/Interaktionsprüfung.

**Weitere Grenzen und Voraussetzungen der Aussage:** Zwei konkrete DESIGN.md vertieft, nicht sämtliche 84 Analysen; gesamter Katalog über README gelesen. Referenzen enthalten wertende und teils kategorische Stilvorschriften, keine offiziellen Markenstandards. Claude-Datei verbietet Hover-Dokumentation und lässt Validierung/Animation offen; solche Lücken nicht als fertiges Produktsystem übernehmen. MIT-Repolizenz ist keine allgemeine Nutzungsfreigabe fremder Marken und proprietärer Schriften; keine eigene Rechtsbewertung.

**Abgleich mit dem Index:** Textdatencharakter bestätigt. Konkrete Beispiele sind ausdrücklich Marketinganalysen mit Known Gaps; das begrenzt README complete visual language und die Index-Nähe zu fertigen Designsystemen.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/VoltAgent/awesome-design-md/README.md>) · [design-md/linear.app/DESIGN.md](<../external_repos/VoltAgent/awesome-design-md/design-md/linear.app/DESIGN.md>) · [design-md/claude/DESIGN.md](<../external_repos/VoltAgent/awesome-design-md/design-md/claude/DESIGN.md>) · [CONTRIBUTING.md](<../external_repos/VoltAgent/awesome-design-md/CONTRIBUTING.md>)


### Diagramme und Videos

#### R66 · cathrynlavery/diagram-design

[GitHub](https://github.com/cathrynlavery/diagram-design) · Revision: `0b9b10cab3dbf695642fa1a6c4b4f60df9083689` · README-Vertrag; Skill- und Referenzvertrag; kein eigener Lauf

Diagram Design trennt die fachliche Aussage eines Diagramms von seiner visuellen Ausgestaltung. Zunächst werden Bedeutung, passende Darstellung und Informationsbudget gewählt; erst danach folgen Raster, Typografie, Farben und optionale Bewegung. Die semantischen Muster machen unter anderem Kapazitätsgrenzen, den ersten abweichenden Prüfschritt, Verantwortliche einer Kontrolle und verbleibendes Risiko sichtbar. Das ist für Architektur- und Betriebsdokumentation wertvoller als dekorative Pfeile. Beim Import aus Mermaid, draw.io oder Excalidraw werden Strukturen als Daten behandelt und neu gezeichnet. Ein Fidelity Ledger hält fest, welche Inhalte vereinfacht oder weggelassen wurden. Projektbezogene Markenprofile vermeiden vermischte Gestaltung. Zugänglichkeit verlangt verständliche Beschriftungen und eine vollständige statische Darstellung. HTML und SVG bleiben grundsätzlich bearbeitbarer Text; ein verlustfreier Rückweg in das ursprüngliche Diagrammformat wird jedoch nicht zugesichert. Eigene Renderer-Prüfungen wurden hier nicht ausgeführt.

**Übertragbare Verfahren:**

- Bedeutung und Diagrammtyp vor Layout und Animation auswählen.
- Nur die zum Typ nötigen Referenzen laden und strengere semantische Budgets anwenden.
- Importe als Daten extrahieren; Herkunft, Vereinfachungen und entfernte Elemente in einem Fidelity Ledger dokumentieren.
- Markenprofile projektbezogen isolieren und tatsächliche Schrift-/Farbübernahme sichtbar machen.
- Zustände durch Text erklären und Bewegung nur als optionale Darstellungsschicht verwenden.
- Restrisiken, ungeprüfte Kontrollbereiche und nicht erreichte Schritte ausdrücklich darstellen.

**Voraussetzungen:** HTML/SVG-Ausgabe; Renderer und Export benötigen teilweise zusätzliche Browserwerkzeuge. Systemfonts für netzfreie Ausgabe oder erreichbare externe Fonts.

**Weitere Grenzen und Voraussetzungen der Aussage:** Layoutqualität bleibt modellabhängig; dokumentierte Prüfwerkzeuge wurden nicht ausgeführt. Maximal neun Knoten ist eine Übersichtsvorgabe mit begründeten Ausnahmen für quellgetreue Importe. Die README-Aussage fehlender editierbarer Quelle ist für HTML/SVG zu weit; gemeint ist fehlender semantischer Roundtrip in ursprüngliche Diagrammwerkzeuge.

**Abgleich mit dem Index:** Keine wesentliche Abweichung; semantische Muster präzisieren die Darstellung von Restlücken und Kontrollfluss deutlich.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/cathrynlavery/diagram-design/README.md>) · [skills/diagram-design/SKILL.md](<../external_repos/cathrynlavery/diagram-design/skills/diagram-design/SKILL.md>) · [skills/diagram-design/references/semantic-patterns.md](<../external_repos/cathrynlavery/diagram-design/skills/diagram-design/references/semantic-patterns.md>)

#### R67 · heygen-com/hyperframes

[GitHub](https://github.com/heygen-com/hyperframes) · Revision: `495dc95acdf738f419eb644439ca1e90b94b511e` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

HyperFrames übersetzt HTML, CSS und Medien in seekbare Videokompositionen. Der entscheidende Unterschied zu einer Browseraufnahme ist der Zeitvertrag: Jeder sichtbare Zustand muss sich aus Timelinezeit ergeben; Timer, unkontrollierter Zufall und veränderliche Netzwerkdaten gefährden die Reproduzierbarkeit. Clips besitzen Start, Dauer und Spur, während die Zeichenreihenfolge separat bleibt. Der statisch gelesene Parser akzeptiert ältere Timingformen, schreibt Änderungen kanonisch und diagnostiziert widersprüchliche Endwerte. Für die Produktion kombiniert der Workflow automatische Prüfungen mit Bildern jeder Szene, Vorschau und Kontrolle decodierter Renderframes. Ein Ergebnis mit null geprüften Samples darf dabei nicht als bestandene visuelle Prüfung erscheinen. Stabile IDs, einzelne Szenendateien und editierbare Variablen erleichtern die Zusammenarbeit mit Menschen. Die hier gelesenen Verträge belegen den vorgesehenen Arbeitsablauf; sie ersetzen weder eine ausgeführte Renderprüfung noch die Kontrolle von Bildwirkung, Tonmischung, Rechten und externen Diensten.

**Übertragbare Verfahren:**

- Jeden sichtbaren Zustand als Funktion einer seekbaren Timeline statt Wandzeit, Timer oder Zufall gestalten.
- Rootdauer, Clipstart, Dauer und Spur in einem kanonischen Vertrag führen; Spur von Paint-Reihenfolge unterscheiden.
- Szenen, stabile IDs, Variablen und echte Quelldateien so authoren, dass menschliche Bearbeitung im Studio erhalten bleibt.
- Lint, Laufzeit-/Layout-/Kontrastcheck, visuelle Einzelbildprüfung und decodierte Renderprüfung als verschiedene Qualitätsschritte einsetzen.
- Nicht ausgeführte Prüfstufen sichtbar machen; null Samples bedeuten keine geprüften Layouts.
- Ältere Timingattribute lesend unterstützen, neue Änderungen kanonisch schreiben und widersprüchliche Ableitungen diagnostizieren.

**Voraussetzungen:** Node.js ab 22, FFmpeg und passende Browser-/Renderumgebung. Seekbare Animationsadapter, lokale Fonts/Assets sowie korrekt deklarierte Medien- und Audiodaten. Für deterministische Ergebnisse kontrollierte Abhängigkeiten und Ressourcen statt veränderlicher externer Zustände.

**Weitere Grenzen und Voraussetzungen der Aussage:** Determinismus ist ein Vertrag an Inhalt und Umgebung; beliebiges HTML wird dadurch nicht automatisch reproduzierbar. Bestandene automatische Checks belegen keine gute Dramaturgie, vollständige visuelle Abdeckung oder richtigen Tonmix. Doctor kann Exitcode 0 trotz problematischem .ok liefern; Prüfer müssen strukturierte Resultate auswerten. README verwendet ein CDN-Beispiel, während strenger Produktionsvertrag Netzwerkabhängigkeit ausschließt. Cloudrendering, Provider und Telemetrie haben eigene Daten- und Kostenflüsse. Keine Renderpipeline, Medien oder vollständigen Adapter wurden praktisch geprüft.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/heygen-com/hyperframes/README.md>) · [skills/hyperframes/SKILL.md](<../external_repos/heygen-com/hyperframes/skills/hyperframes/SKILL.md>) · [skills/hyperframes-cli/SKILL.md](<../external_repos/heygen-com/hyperframes/skills/hyperframes-cli/SKILL.md>) · [packages/core/src/compositionContract.ts](<../external_repos/heygen-com/hyperframes/packages/core/src/compositionContract.ts>) · [packages/parsers/src/compositionContract.ts](<../external_repos/heygen-com/hyperframes/packages/parsers/src/compositionContract.ts>)

#### R68 · latent-spaces/brag

[GitHub](https://github.com/latent-spaces/brag) · Revision: `669ab9286aa28b6c3ee30e75f181ee74319d012a` · README-Vertrag; beide vollständigen Skill-Verträge; kein Renderlauf

Brag trennt die Geschichte eines Launch-Videos von seiner technischen Komposition. Zuerst werden Zielgruppe, Produktversprechen, visuelle Identität und ein konkreter Ablauf vom Einstieg bis zum Ergebnis verstanden. Daraus entstehen ein kurzer Hook, wenige präzise Highlights und ein Abschluss. Reale Benutzeroberflächen und Komponenten sollen abstrakte Werbebilder ersetzen. Für Text gilt eine erkennbare Haltezeit; Schnitte und Bewegung schaffen Tempo, ohne Lesbarkeit zu opfern. Der klassische Pfad übergibt die Komposition an HyperFrames, Slim verwendet vorhandene Werkzeuge und prüft Standbilder auch mitten im Übergang. Ein zeitabhängig deterministischer Bildzustand macht Einzelbilder reproduzierbar. Plan, Video, stärkster ruhiger Posterframe und Share-Copy bilden die Lieferung. Sensible Daten werden durch ausgewiesene fiktive Beispiele ersetzt. Produktclaims und Medienrechte brauchen weiterhin eine eigenständige Bewertung; ein fertig gerendertes Video erteilt keine Veröffentlichungsfreigabe.

**Übertragbare Verfahren:**

- Produktverständnis und konkreten Benutzerablauf vor visuellen Effekten klären.
- Hook, Reveal, wenige Highlights und Abschluss als zeitlich begrenzte Dramaturgie planen.
- Reale Komponenten und Assets bevorzugen und fiktive sensible Beispieldaten kennzeichnen.
- Textlesbarkeit durch Haltezeit sichern statt Tempo durch zu kurze Anzeige zu erzeugen.
- Bildzustand deterministisch aus Zeit berechnen und Szenen sowie Übergänge vor Vollrender prüfen.
- Plan, Umsetzung, Poster und Share-Copy gemeinsam als überprüfbare Artefakte liefern.

**Voraussetzungen:** Klassischer Pfad benötigt Node 22+, FFmpeg und HyperFrames; Slim nutzt vorhandene Werkzeuge. Musik-/Asset-Rechte und passende Zielplattform; Stimme nur ausdrücklich gewünscht.

**Weitere Grenzen und Voraussetzungen der Aussage:** Modellabhängiger automatischer Wechsel auf Slim ist datierte Routingentscheidung des Projekts. Bestehende Produktclaims sind nicht automatisch wahr oder veröffentlichungsfreigegeben. Wiederverwendetes Website-Markup muss inert werden; echte Komponenten können eigene Laufzeitvoraussetzungen haben. Gebündelte Musik besitzt eine gesonderte Namensnennungspflicht laut README.

**Abgleich mit dem Index:** Keine wesentliche Abweichung; weitergehende verlinkte HyperFrames-Prüfdetails wurden nicht erneut vollständig untersucht.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/latent-spaces/brag/README.md>) · [skills/brag/SKILL.md](<../external_repos/latent-spaces/brag/skills/brag/SKILL.md>) · [skills/brag-slim/SKILL.md](<../external_repos/latent-spaces/brag/skills/brag-slim/SKILL.md>)

#### R69 · oh-my-mermaid/oh-my-mermaid

[GitHub](https://github.com/oh-my-mermaid/oh-my-mermaid) · Revision: `38ccdb69298adec949177c92c88d6e3ddfb5bab7` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Oh-my-mermaid strukturiert Architektur nach verständlichen Perspektiven und rekursiven Unteransichten. Gesamtbild, Request-Lifecycle, Datenfluss oder Zustand beantworten unterschiedliche Fragen; komplexe Knoten bekommen eigene Diagramme, einfache bleiben Blätter. Verzeichnisnamen dienen als Identitäten, Labels nennen Codepfade und jede Kante soll ihre Bedeutung erklären. Beschreibungen, Kontext, Einschränkungen und Bedenken bleiben als normale Dateien neben Mermaid lesbar. Das ist eine schlanke Alternative zu umfangreichen Wissensgraphen. Seine Grenzen zeigt die statisch gelesene Validierung: Sie kontrolliert ausgewählte Syntaxmuster, Klammerzahlen, Referenzen und empfohlene Diagrammgröße, beweist aber weder Mermaidvollständigkeit noch fachlich richtige Architektur. Auch der Scan ist eine Agentenanweisung und keine deterministische Vollanalyse. Geeignet ist das Verfahren daher für nachvollziehbare Architekturkommunikation mit überprüfbaren Quellpfaden. Aktualität, ausgelassene Komponenten, Viewerzugriff und eine mögliche Cloudübertragung benötigen weiterhin eigene Kontrollen; in diesem Lauf wurde nichts installiert oder veröffentlicht.

**Übertragbare Verfahren:**

- Architektur nach passenden Fragen wie Requestfluss, Zustand, Abhängigkeiten und Erweiterungspunkten betrachten.
- Komplexe Komponenten rekursiv auffächern und einfache Blätter unvergrößert lassen.
- Knotenidentitäten an Verzeichnisnamen und Labels an konkrete Quellpfade binden.
- Beschreibung, Diagramm, Kontext, Einschränkungen, Bedenken und nächste Aufgaben getrennt speichern.
- Lesbare Kantenlabels und einfache Diagramm-/Referenzregeln vor Darstellung prüfen.

**Voraussetzungen:** Ein Agent mit Zugriff auf repräsentative Quellstellen und eine installierte CLI für tatsächliche Nutzung. Eindeutige Knotennamen, kontrollierte Rekursion und manuelle Abgleichprüfung der fachlichen Beziehungen. Getrennte Prüfung vor Cloudübertragung oder öffentlicher Viewerbereitstellung.

**Weitere Grenzen und Voraussetzungen der Aussage:** Scanner ist ein Promptverfahren, keine deterministische Vollcodeanalyse. Gelesener Validator prüft ausgewählte Zeilenmuster, Klammerzahlen und Referenzen; kein vollständiger Mermaidparser oder fachlicher Architekturnachweis. Self-Reference-Prüfung ist keine allgemeine Zyklenprüfung; gleiche Klammerzahlen bedeuten nicht korrekte Syntax. Metadaten über Commit/Branch belegen alleine keine aktuelle Quellenübereinstimmung. Cloud-Push und Viewer-Sicherheitsdetails des Index wurden nicht praktisch oder vollständig implementierungsseitig nachgeprüft.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/oh-my-mermaid/oh-my-mermaid/README.md>) · [skills/omm-scan/SKILL.md](<../external_repos/oh-my-mermaid/oh-my-mermaid/skills/omm-scan/SKILL.md>) · [src/types.ts](<../external_repos/oh-my-mermaid/oh-my-mermaid/src/types.ts>) · [src/lib/validate.ts](<../external_repos/oh-my-mermaid/oh-my-mermaid/src/lib/validate.ts>)

#### R70 · tt-a1i/archify

[GitHub](https://github.com/tt-a1i/archify) · Revision: `51a291770851ad27a400cca73c753c166b5e0c65` · README-Vertrag; statischer Dokument-/Codebeleg; kein eigener Lauf

Archify verbindet visuelle Kommunikation mit einem überprüfbaren Quellen- und Liefervertrag. Die Auswahl zwischen Architektur, Workflow, Sequenz, Datenfluss, Zustand, ERD und weiteren Typen folgt der Leserfrage. Für echte Repositories werden Origin und Commit fixiert, Calls und Schreibstellen verfolgt und unbekannte Zusammenhänge sichtbar erhalten. Die typisierte Quelle bleibt editierbar; Validierung, Lieferung und Browserchecks prüfen unterschiedliche Eigenschaften. Kandidaten sollen die letzte gute HTML-Ausgabe erst nach bestandenen Gates atomar ersetzen. Der Viewer untersucht ausschließlich gezeichnete Beziehungen: Reach und Architektur-Delta behaupten keine gemessene Laufzeitwirkung oder Merge-Sicherheit. Auch ein bestandenes Browsergate ersetzt keine Wahrnehmungsprüfung. Das ist für die Factory eine starke Vorlage zur Trennung fachlicher Evidenz, struktureller Gültigkeit und visueller Abnahme. Eine anschauliche Karte wird dadurch nachvollziehbarer, aber nicht automatisch wahr.

**Übertragbare Verfahren:**

- Diagrammtyp aus Leserfrage wählen, Beschreibung von belegtem Repozustand trennen und illustrative Zeiten ausdrücklich markieren.
- Repoidentität auf credentialfreie Origin und Commit fixieren; tatsächliche Caller, Writer und Execution-Sites verfolgen.
- Typisierte JSON-IR vor Layout-/Artefakt-/Browser-Gates erhalten und Fehler mit messbaren Reparaturhinweisen zurückgeben.
- Kandidaten atomar veröffentlichen und bei Fehlern letzte gute Ausgabe erhalten.
- Viewer-Reach und Delta zeigen nur modellierte Beziehungen; keine Laufzeitwirkung, Risiko- oder Merge-Sicherheit erfinden.
- Automatische Gates, Screenshotcapture und wirkliche Wahrnehmungsprüfung getrennt berichten.

**Voraussetzungen:** Node und Renderer für volle Ausgabe; passende Quellbelege und Schemas. Für source-backed Claims committed Bytes am angegebenen Stand, bei Dirtytree explizite Grenze.

**Weitere Grenzen und Voraussetzungen der Aussage:** Schema-/Browserprüfung beweist nicht fachliche Richtigkeit oder visuelle Lesbarkeit. README/Skill behandeln Mermaid als semantischen Input, kein automatischer Parser und kein allgemeines Autolayout. Pinned-Commit-Evidenz erfasst uncommittete Änderungen nicht; local-only ändert das nicht. Optionale Updateabfrage hat Netzwerkmetadaten; keine Ausführung in dieser Analyse.

**Abgleich mit dem Index:** Zehn Modi, Explainer und getrennte Gates bestätigt. README-Vorschlag 8–12 Komponenten ist Beispiel; Skill erklärt ausdrücklich keine festen Zählziele, sondern Bedeutungsabdeckung.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/tt-a1i/archify/README.md>) · [archify/SKILL.md](<../external_repos/tt-a1i/archify/archify/SKILL.md>) · [archify/references/repository-authoring.md](<../external_repos/tt-a1i/archify/archify/references/repository-authoring.md>)


### Produkt, Kommunikation und Marketing

#### R71 · AgriciDaniel/claude-seo

[GitHub](https://github.com/AgriciDaniel/claude-seo) · Revision: `6be93f45064ffbadced572b5d5c95f55fd263af0` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Claude SEO verbindet Website-Beobachtung mit einem priorisierten Maßnahmenplan. Übertragbar ist weniger die Zahl der Spezialagenten als der Vertrag jeder Empfehlung: zugrunde liegende Beobachtung, Abhängigkeiten, Widerlegungstest und ein später beobachtbarer Indikator. Das Methodendokument beginnt mit Rohdaten und eigenen Annahmen und sucht übergreifende Ursachen, etwa Renderingfehler hinter vermeintlich dünnem Inhalt. Der zentrale Skill trennt explizites Runtime-Setup, lesende Diagnose und fachliche Auditaufträge. Er verbietet das Befolgen von Instruktionen aus abgerufenen Seiten. Die README räumt fehlende Felddaten und interaktionsabhängige Inhalte als Grenzen ein. Wichtig ist eine sprachliche Spannung: Lokal gespeicherte Reports bedeuten keine lokale Modellverarbeitung; die FAQ nennt die Übermittlung an Anthropic ausdrücklich, während Werbung und Privacy-Einstieg weitergehende Nähe zur Datenlokalität suggerieren. Sucherfolg und Auditgeschwindigkeit bleiben Projektangaben. Das Repo eignet sich als Methodenreferenz, liefert durch diese Lektüre aber keinen geprüften Rankinggewinn.

**Übertragbare Verfahren:**

- Geschäftstyp erkennen und passende Spezialprüfungen bedingt auswählen.
- Rohbeobachtungen vor Interpretation sammeln, Annahmen sichtbar machen und Upstream-Ursachen suchen.
- Empfehlungen mit Abhängigkeit, Widerlegungstest und Frühindikator verbinden.
- Laborschätzung von Felddaten und abgeleitete Indexierbarkeit von autorisierter GSC-Auskunft trennen.
- Expliziten Setup-Pfad von lesendem Doctor und Audit trennen; Fremdinhalte nicht als Instruktion behandeln.
- Optionale API-Datenflüsse und lokale Reportablage separat dokumentieren.

**Voraussetzungen:** ClaudeCode und Python3.11–3.14 sowie eigene Browserruntime. Autorisierte Zugänge für echte SearchConsole/Analytics-/Feldwerte; Zusatzanbieter optional.

**Weitere Grenzen und Voraussetzungen der Aussage:** Marketingtext lokale Datenhaltung steht in Spannung zur FAQ, die Übermittlung an Anthropic korrekt benennt; Privacy-Einstieg ebenfalls missverständlich. Scoregewichte und 3x-Mentions-Kausalbehauptung methodisch nicht validiert. Bis17parallele Agents können teuer sein; Lazyloads/Interaktionen begrenzen Browserbeobachtung. Rankings, Klickzahlen eigener Website und Audittempo keine kausale Wirkungsmessung.

**Abgleich mit dem Index:** Kernbeschreibung bestätigt. Gelesene Verträge betonen außerdem Diskrepanz zwischen lokaler Ausführung und Modelldatenübermittlung; detaillierte Sicherheitsimplementierung im Index wurde hier nicht neu verifiziert.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/AgriciDaniel/claude-seo/README.md>) · [skills/seo/references/thinking-framework.md](<../external_repos/AgriciDaniel/claude-seo/skills/seo/references/thinking-framework.md>) · [skills/seo/SKILL.md](<../external_repos/AgriciDaniel/claude-seo/skills/seo/SKILL.md>) · [PRIVACY.md](<../external_repos/AgriciDaniel/claude-seo/PRIVACY.md>)

#### R72 · ayghri/i-have-adhd

[GitHub](https://github.com/ayghri/i-have-adhd) · Revision: `1ecea1993b7fce257ffbd686c070948b5e07eda6` · README-Vertrag; Skill-Vertrag; Autorenevaluation; kein eigener Lauf

I Have ADHD ist ein Kommunikations-Skill mit klarer Priorität: die relevante Handlung zuerst, anschließend kurze nummerierte Schritte und eine sichtbare nächste Aktion. Seine eigenen Ausnahmen verhindern, dass ein Präsentationslimit eine vollständige Erklärung oder autonome Bearbeitung künstlich beendet. Für die Factory lässt sich dieses Muster als wählbare Kommunikationspräferenz übernehmen, ohne medizinische Wirkung zu behaupten. Besonders lehrreich ist die interne Evaluation: Über vierzehn Szenarien und drei Versuche pro Bedingung steigt die durchschnittliche Bewertung, dennoch scheitert die Variante am eigenen Release-Gate. Drei blockierende Fehler wiegen dort schwerer als der bessere Mittelwert. Ein Fall zeigt zudem, dass die Forderung nach einer knappen Ursache eine unsichere Diagnose als Gewissheit erscheinen lassen kann. Gute Verständlichkeit benötigt deshalb ausdrücklich erhaltene Unsicherheit und eine Prüfung kritischer Fehlermuster.

**Übertragbare Verfahren:**

- Konkrete Handlung an den Anfang stellen und genau einen nächsten Schritt sichtbar machen.
- Nebenpfade und unnötige Optionen unterdrücken, ohne notwendige Inhalte zu kürzen.
- Lange Erklärungen und selbstständige Ausführung ausdrücklich von Präsentationsregeln ausnehmen.
- Kommunikationsregeln mit Szenarien, mehreren Versuchen und blockierenden Fehlerklassen evaluieren.

**Voraussetzungen:** Bewusste Aktivierung des Stils und passender Harness-Adapter. Individuelle Präferenz prüfen; keine Diagnose als Voraussetzung oder Ergebnis.

**Weitere Grenzen und Voraussetzungen der Aussage:** Gesundheitsbezogene Verallgemeinerungen sind keine klinische Evidenz. Die interne Evaluation verbessert den Durchschnitt, scheitert aber am eigenen Release-Gate mit drei Blockern. Die Vorgabe Ursache dann Lösung kann bei unbekannter Ursache zu erfundener Gewissheit führen.

**Abgleich mit dem Index:** Der Index erwähnt Evaluation, aber nicht deren fehlgeschlagenes Release-Gate.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/ayghri/i-have-adhd/README.md>) · [evals/RESULTS.md](<../external_repos/ayghri/i-have-adhd/evals/RESULTS.md>) · [evals/rubric.md](<../external_repos/ayghri/i-have-adhd/evals/rubric.md>) · [skills/i-have-adhd/SKILL.md](<../external_repos/ayghri/i-have-adhd/skills/i-have-adhd/SKILL.md>)

#### R73 · coreyhaines31/marketingskills

[GitHub](https://github.com/coreyhaines31/marketingskills) · Revision: `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` · README-Vertrag und vollständig gelesene statische Vertiefung; kein eigener Lauf

Corey Haines’ marketingskills organisiert Marketingarbeit um einen gemeinsamen, versionierten Produktkontext. Zielgruppe, Positionierung, echte Kundensprache, Belege und erlaubte Agentenaktionen werden dadurch über verschiedene Aufgaben hinweg wiederverwendbar. Besonders wertvoll ist die Trennung zwischen einer Änderungshistorie und einem Learnings Ledger: Ein Dokument kann sich ändern, ohne dass damit eine Markthypothese bewiesen wäre. Die gelesenen Forschungs- und Experiment-Skills verbinden vorhandene Kundendaten, öffentliche Signale und Interviews mit segmentbezogenen Auswertungen. Personas sollen Daten statt erfundenen Details folgen; vorläufige Proxy-Annahmen bleiben gekennzeichnet. A/B-Tests erhalten vorab definierte Metriken, Guardrails, Stichproben und Stoppregeln sowie eine vorsichtige Interpretation nicht signifikanter Ergebnisse. Praktische Schwellenwerte und Planungsscores bleiben Heuristiken. Offengelegte Partnerintegrationen und Eigenproduktwerbung erfordern bei der Werkzeugwahl weiterhin eigenes Urteil. Keine dieser dokumentierten Methoden ersetzt reale Kundendaten oder ein erfolgreich geprüftes Tracking.

**Übertragbare Verfahren:**

- Positionierung, Zielgruppe, belegte Kundensprache und Grenzen von Agentenrechten in einem versionierten Produktkontext pflegen.
- Änderungshistorie des Kontexts von getesteten Learnings mit Evidenz, Geltungsbereich und Status trennen.
- Bestehende Kundendaten, öffentliche Signale und Primärforschung als unterschiedliche Recherchemodi einsetzen und segmentweise synthetisieren.
- Personas auf unabhängige Datenpunkte stützen und Proxy-Personas ausdrücklich als vorläufig markieren.
- Experimente mit vorab festgelegter Hypothese, Hauptmetrik, Guardrails, Stichprobe und Stoppregel planen.
- Effektgröße und Unsicherheit neben Signifikanz berichten; explorative Segmentbefunde erst separat bestätigen.

**Voraussetzungen:** Verlässliche Informationen über Produkt, Positionierung und Zielkunden. Für Kundenforschung geeignete unabhängige Daten und datenschutzgerechter Umgang. Für A/B-Tests geprüftes Tracking und ausreichend Traffic.

**Weitere Grenzen und Voraussetzungen der Aussage:** Fünf Datenpunkte, Konfidenzlabels und ICE sind praktische Heuristiken, keine allgemeine statistische Absicherung. Aus Code abgeleiteter Marketingkontext bleibt ein durch Nutzer zu prüfender Entwurf. Partnerfinanzierte Integrationen und Eigenproduktwerbung sind offengelegt, behauptete Neutralität wurde nicht unabhängig geprüft. Allgemeine Experimentkadenz und typische Gewinnraten sind unbelegte Orientierungswerte. Viele Fachskills und deren Referenzen wurden nicht einzeln geprüft; keine Marketingaktion wurde ausgeführt.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/coreyhaines31/marketingskills/README.md>) · [skills/product-marketing/SKILL.md](<../external_repos/coreyhaines31/marketingskills/skills/product-marketing/SKILL.md>) · [skills/customer-research/SKILL.md](<../external_repos/coreyhaines31/marketingskills/skills/customer-research/SKILL.md>) · [skills/ab-testing/SKILL.md](<../external_repos/coreyhaines31/marketingskills/skills/ab-testing/SKILL.md>)

#### R74 · petergyang/no-ai-slop

[GitHub](https://github.com/petergyang/no-ai-slop) · Revision: `000650b156983f5159695b441477f4e63b25dc85` · README-Vertrag; Vollständig gelesene Skill-Anweisung und Selbstprüfliste; kein eigener Lauf

no-ai-slop liefert eine begrenzte, gut übertragbare Redaktionsmethode: Nur nachweisbare Sprachmuster bearbeiten und die Stimme der schreibenden Person erhalten. Edit überarbeitet mit möglichst kleinen Eingriffen; Detect benennt Muster mit einem Textzitat und kurzem Änderungsvorschlag. Humor, Rhythmus, Unsicherheit und sinnvolle Abschweifungen bleiben ausdrücklich erhalten. Die Prüfung auf austauschbare Aussagen hilft, konkrete Beobachtungen von bedeutungsvoll klingenden Leerstellen zu unterscheiden. Fehlende Fakten werden dadurch jedoch nicht ergänzt: Zahlen, Quellen oder Wirkungen dürfen nicht erfunden werden. Die eigene eval.md kontrolliert die Ausführung anhand einer Pass/Fail-Liste, belegt aber keine experimentell gemessene Qualitätsverbesserung. Wortlisten und pauschale Formverbote brauchen redaktionelles Urteil, weil Fachsprache und absichtliche Stilmittel sonst verloren gehen können. Aus gefundenen Mustern folgt keine verlässliche Aussage über die Urheberschaft eines Textes.

**Übertragbare Verfahren:**

- Edit und Detect trennen: entweder kleinste wirksame Änderung mit Änderungsübersicht oder belegte Muster mit Zitat und kurzem Fix.
- Rhythmus, Humor, Härte, Unsicherheit und sinnvolle Abschweifungen bewahren; starke Sätze unverändert lassen.
- Allgemein austauschbare Aussagen durch vorhandene konkrete Fakten ersetzen oder streichen; keine Zahlen oder Belege erfinden.
- Benannte Muster wie binäre Kontraste, Pseudo-Einsichten, Räusper-Einstiege und aufgeblähte Schlussfolgerungen als überprüfbare Textbefunde behandeln.
- Nach jeder Bearbeitung eine explizite Pass/Fail-Selbstprüfung für Stimmerhalt, Faktentreue und verbleibende Muster durchführen.

**Voraussetzungen:** Vorhandener Text, Zielgruppe und Zweck; menschliches Urteil über gewollte Stilmittel.

**Weitere Grenzen und Voraussetzungen der Aussage:** Die Muster erlauben keine Aussage über menschliche oder maschinelle Urheberschaft; der Skill verbietet diese Schlussfolgerung selbst. Starre Wortverbote und Verbote bestimmter Satzformen können legitime Fachsprache oder absichtliche Rhetorik treffen. eval.md ist eine Selbstkontrolle, kein kontrollierter Wirksamkeitsbenchmark. Beispielhafte Zahlen in Umschreibungen sind keine Erlaubnis, Tatsachen in echten Texten zu erfinden.

**Abgleich mit dem Index:** Der Index trifft den methodischen Kern; die Selbstprüfung ist kein unabhängiger Evaluationsnachweis.

**Vollständig gelesene Einstiegstexte und Vertiefungen:** [README.md](<../external_repos/petergyang/no-ai-slop/README.md>) · [skills/no-ai-slop/SKILL.md](<../external_repos/petergyang/no-ai-slop/skills/no-ai-slop/SKILL.md>) · [skills/no-ai-slop/eval.md](<../external_repos/petergyang/no-ai-slop/skills/no-ai-slop/eval.md>)



## 22. Vollständiges Register der Quellenlektüre

Die 604 Einträge sind Lektüreeinheiten: Rohtext und passende Source-Notiz wurden, soweit anhand ihres Dateinamens zugeordnet, gemeinsam gelesen. Abweichende Slugs, Nachträge und mehrere Aufbereitungen derselben Veröffentlichung bleiben eigene Einträge, damit keine gelesene Datei verschwindet. Gleiche Original-URLs werden zusätzlich als gemeinsame Herkunft markiert. Auch verschiedene URLs können denselben Bericht referieren; dieses Register zählt deshalb ausdrücklich keine unabhängigen Wirksamkeitsbelege.

Die Links führen zum lokalen Text und, soweit angegeben, zum Original. Die Kernaussagen sind Verdichtungen der Lektüre. Grenzen nennen wichtige Unsicherheiten, keine neue Prüfung aller externen Tatsachen. Datumsangaben folgen der erfassten Veröffentlichung; abweichende oder unsichere Datierung bleibt im Text sichtbar. Die 72 zusätzlichen Wörterbuchdateien sind in Kapitel 24 erfasst.

### 2025-04

**Q0001 · 2025-04-09 · [KI-Risiken und Vertrauensverlust](<../80_Knowledge/Sources/2025-04-09-the-morpheus-ki-ist-ein-fluch.md>)**

Synthetische Inhalte verstärken Spam, Betrug und Vertrauensprobleme; Arbeitsmarkt- und AGI-Szenarien bleiben davon getrennte Prognosen. **Grenze:** Energievergleiche, Rechtsaussagen und AGI-Zeitpläne sind hier nicht verifiziert. [Rohtext](<../00_Inbox/Quellen/YouTube/2025-04-09-the-morpheus-ki-ist-ein-fluch.md>) · [Original](<https://www.youtube.com/watch?v=pCtr-y-9EuM>)

**Q0002 · 2025-04-09 · [KI-Chancen im April 2025: Unterstützung von Arbeit und überdehnte Zukunftsszenarien](<../80_Knowledge/Sources/2025-04-09-the-morpheus-ki-ist-ein-segen.md>)**

Recherche und Lernvorbereitung lassen sich delegieren, während fachliche Bewertung und persönliche Gestaltung beim Menschen bleiben. **Grenze:** SWE-bench-Aufgabenanteile messen keinen automatisierbaren Anteil des gesamten SDLC; medizinische Überlegenheit und gesellschaftliche Utopien bleiben unbelegt. [Rohtext](<../00_Inbox/Quellen/YouTube/2025-04-09-the-morpheus-ki-ist-ein-segen.md>) · [Original](<https://www.youtube.com/watch?v=20UVb7GT6Ic>)


### 2025-06

**Q0003 · 2025-06-23 · [Kontext zur Laufzeit aus Aufgabe, Zustand und Umgebung zusammensetzen](<../80_Knowledge/Sources/2025-06-23-boristane-context-engineering-is-what-makes-ai-magical.md>)**

Kontext muss zur Laufzeit aus Aufgabe, Nutzerabsicht, Repositoryzustand und Betriebssignalen zusammengesetzt werden. **Grenze:** Unbegrenzte Anreicherung erhöht Auswahl- und Berechtigungskosten. [Rohtext](<../00_Inbox/Quellen/URL/2025-06-23-boristane-context-engineering-is-what-makes-ai-magical.md>) · [Original](<https://boristane.com/blog/context-engineering/>)

**Q0004 · 2025-06-28 · [Issues vor Implementierung verifizieren](<../80_Knowledge/Sources/2025-06-28-the-morpheus-tutorials-ai-ersetzt-uns-itler-jetzt-also.md>)**

Ein getrennter Agent sollte ein gemeldetes Problem am tatsächlichen Codepfad prüfen, bevor ein weiterer Agent implementiert. **Grenze:** Erfolgsquoten und Beschäftigungsprognosen sind Selbstberichte; menschliche Funktionsprüfung bleibt nötig. [Rohtext](<../00_Inbox/Quellen/YouTube/2025-06-28-the-morpheus-tutorials-ai-ersetzt-uns-itler-jetzt-also.md>) · [Original](<https://www.youtube.com/watch?v=4zvBgh63Lys>)


### 2025-09

**Q0005 · 2025-09-08 · [Junior-Beschäftigung und KI](<../80_Knowledge/Sources/2025-09-08-the-morpheus-tutorials-studien-ai-verdraengt-also-junior-itler.md>)**

Arbeitsmarktanalysen müssen Beschäftigung, Neueinstellungen, Altersgruppen, Zeitraum und Markt voneinander unterscheiden. **Grenze:** Capability-Horizonte messen Aufgaben und Erfolgswahrscheinlichkeiten, nicht automatisch Beschäftigungsverluste. [Rohtext](<../00_Inbox/Quellen/YouTube/2025-09-08-the-morpheus-tutorials-studien-ai-verdraengt-also-junior-itler.md>) · [Original](<https://www.youtube.com/watch?v=dYTJOD4xuZE>)

**Q0006 · 2025-09-22 · [RAG für Texte, Bilder und Tabellen: getrennte Verarbeitung, gemeinsame Quellenidentität](<../80_Knowledge/Sources/2025-09-22-julian-ivanov-ki-automat-das-ultimative-rag-system-n8n-nextcloud-mistral.md>)**

Gemischte RAG-Bestände benötigen getrennte Pfade für Textsuche, vollständigen Dokumentabruf und strukturierte SQL-Berechnungen, verbunden über stabile Datei-IDs. **Grenze:** Demo-Erfolge belegen keine robuste Retrieval-Pipeline; öffentliche Bildlinks und externe OCR-/Reranking-Dienste relativieren die pauschale Datenschutzbehauptung. [Rohtext](<../00_Inbox/Quellen/YouTube/2025-09-22-julian-ivanov-ki-automat-das-ultimative-rag-system-n8n-nextcloud-mistral.md>) · [Original](<https://www.youtube.com/watch?v=tFANS8Fn2ao>)

**Q0007 · 2025-09-26 · [Stop using Claude Code the wrong way!](<../00_Inbox/Quellen/TikTok/2025-09-26-silviutechnology-stop-using-claude-code-the-wrong-way.md>)**

Wiederverwendbare Requirements- und Test-Commands lassen sich als kleine Arbeitsfolge verketten. **Grenze:** Die Quelle zeigt keine belastbare Methode oder Wirkungsmessung; die zehnfache Produktivität ist Werbung. [Original](<https://www.tiktok.com/@silviu.technology/video/7554320240696462614>)


### 2025-10

**Q0008 · 2025-10-31 · [Skills für Marke, Lernen und Debugging](<../80_Knowledge/Sources/2025-10-31-agenticjames-best-claude-skills-for-agentic-coding.md>)**

Brand- und Debugging-Skills bündeln wiederkehrendes institutionelles Wissen und laden es bei passenden Aufgaben. **Grenze:** Die drei Vorschläge sind Meinung ohne mitgelieferte Skill-Dateien oder Wirkungsmessung. [Rohtext](<../00_Inbox/Quellen/TikTok/2025-10-31-agenticjames-best-claude-skills-for-agentic-coding.md>) · [Original](<https://www.tiktok.com/@agentic.james/video/7567486319610416439>)


### 2025-11

**Q0009 · 2025-11-05 · [Here’s how I teach master prompting](<../00_Inbox/Quellen/TikTok/2025-11-05-natebjones-heres-how-i-teach-master-prompting.md>)**

Selbstkorrektur, Metaprompting, strukturierte Prüfsequenzen und Perspektivwechsel sind wiederverwendbare Prompting-Denkmodelle. **Grenze:** Selbstprüfung ersetzt keinen unabhängigen Nachweis. [Original](<https://www.tiktok.com/@nate.b.jones/video/7569345803840539934>)


### 2025-12

**Q0010 · 2025-12-04 · [KI in Organisationen verankern: Use Case, Befähigung und Betriebsübergang](<../80_Knowledge/Sources/2025-12-04-brutkasten-business-vs-technik-wie-man-ki-in-organisationen.md>)**

KI-Einführung braucht einen konkreten fachlichen Use Case, reale Mitarbeiterbefähigung und einen verantworteten Übergang vom internen Pilot in den Betrieb. **Grenze:** Technische Machbarkeit, Pilotnutzung und wirtschaftlicher Nutzen sind verschieden; Human Review wirkt nur mit fachlicher Bewertungsgrundlage. [Rohtext](<../00_Inbox/Quellen/YouTube/2025-12-04-brutkasten-business-vs-technik-wie-man-ki-in-organisationen.md>) · [Original](<https://www.youtube.com/watch?v=KlbIwEHFLCU>)

**Q0011 · 2025-12-06 · [Mit Coding-Agenten lernen und kleine Änderungen prüfen](<../80_Knowledge/Sources/2025-12-06-the-morpheus-tutorials-software-entwickeln-mit-ki-einsteiger-guide.md>)**

Kleine Änderungen mit Git-Diff, Issue-Steuerung, Browserprüfung und erklärenden Rückfragen bilden einen geeigneten Lernzyklus. **Grenze:** Gezeigte Hard-Reset- und Rebase-Erklärungen sind kein allgemeiner sicherer Git-Ablauf. Automatisches Transkript enthält Produktnamenfehler. [Rohtext](<../00_Inbox/Quellen/YouTube/2025-12-06-the-morpheus-tutorials-software-entwickeln-mit-ki-einsteiger-guide.md>) · [Original](<https://www.youtube.com/watch?v=BA8ieZxiocU>)

**Q0012 · 2025-12-28 · [I do not get why software licenses are stuck in 1997](<../00_Inbox/Quellen/TikTok/2025-12-28-natebjones-i-do-not-get-why-software-licenses-are-stuck-in-1997.md>)**

KI-Lizenzen sollten nach tatsächlichem Arbeitsnutzen und Befähigung beurteilt werden, nicht ausschließlich nach niedrigem Lizenzpreis. **Grenze:** Kostenhöhe beweist keinen Produktivitätsgewinn. [Original](<https://www.tiktok.com/@nate.b.jones/video/7588812222600727839>)

**Q0013 · 2025-12-31 · [Fine-Tuning ist 2026 die letzte Option: erst Harness, dann Modell anfassen](<../80_Knowledge/Sources/2025-12-31-natebjones-seriously-not-worth-it-now.md>)**

Vor Fine-Tuning sollten Instruktionen, Constraints, Harness und Evals als Anpassungshebel geprüft werden. **Grenze:** Genereller Harness-Vorrang widerspricht möglichen spezialisierten Trainingszielen. [Rohtext](<../00_Inbox/Quellen/TikTok/2025-12-31-natebjones-seriously-not-worth-it-now.md>) · [Original](<https://www.tiktok.com/@nate.b.jones/video/7589872498901077278>)


### 2026-01

**Q0014 · 2026-01-04 · [Generierung delegieren und Entscheidungshoheit behalten](<../80_Knowledge/Sources/2026-01-04-ai-news-strategy-daily-n-why-andrej-karpathy-feels-behind-and-what-it-mea.md>)**

Ein verlässlicher KI-Workflow trennt Generierung von Entscheidung und verbindet klare Ziele mit Kontextauswahl, Rechten, Provenienz, Beobachtbarkeit und Evals. **Grenze:** Das vierstufige Kompetenzmodell ist Autoreninterpretation; die angekündigte zehnfache Beschleunigung wurde nicht gemessen. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-01-04-ai-news-strategy-daily-n-why-andrej-karpathy-feels-behind-and-what-it-mea.md>) · [Original](<https://www.youtube.com/watch?v=fyHnGHxGuhI>)

**Q0015 · 2026-01-06 · [Gezieltes Context Engineering](<../00_Inbox/Quellen/X/2026-01-06-jarrodwatts-2008495347115630701.md>)**

Ein klares Ziel pro Chat, geprüfte Pläne und bedarfsorientierter Kontext verhindern unnötige Kontextüberladung. **Grenze:** Die Tool-, Modell- und Kontextfensterzahlen stammen aus Januar 2026; dieselbe Quelle liegt unter weiteren Dateinamen vor. [Original](<https://x.com/jarrodwatts/status/2008495347115630701>) · Gleiche angegebene Herkunft: Q0016, Q0038.

**Q0016 · 2026-01-06 · [Context Engineering mit bedarfsorientiertem Wissen](<../80_Knowledge/Sources/2026-01-06-jarrodwatts-context-engineering-guide.md>)**

Kontextqualität entsteht durch klaren Scope, gezieltes Retrieval und begründete Neustarts bei gescheiterten Ansätzen. **Grenze:** Dieselbe Jarrod-Watts-Quelle wie weitere Fassungen im Bestand; der Screenshot ist ein einzelner historischer Konfigurationsstand. [Original](<https://x.com/jarrodwatts/status/2008495347115630701>) · Gleiche angegebene Herkunft: Q0015, Q0038.

**Q0017 · 2026-01-10 · [Claude Code Grundlagen: Denken vor Tippen, CLAUDE.md und Kontextgrenzen](<../80_Knowledge/Sources/2026-01-10-eyad-khrais-claude-code-tutorial.md>)**

Planung, konkrete Architekturvorgaben, schlanke Projektregeln und externe Fortschrittsdateien verbessern die Steuerbarkeit von Coding-Aufgaben. **Grenze:** Die Kontextschwelle von 20–40 Prozent, 150–200 befolgbaren Instruktionen und feste Opus-/Sonnet-Rollen sind historische Erfahrungsheuristiken. [Rohtext](<../00_Inbox/Quellen/X/2026-01-10-eyad-khrais-claude-code-tutorial.md>) · [Original](<https://x.com/eyad_khrais/status/2010076957938188661>)

**Q0018 · 2026-01-12 · [Architektur, Tests und Vibe Reviewing](<../80_Knowledge/Sources/2026-01-12-dhruv1103-lessons-learned-500k-lines-claude-code.md>)**

Modulare Schnittstellen, echte Integrationstests und zugängliche Logs unterstützen autonome Diagnose und Review. **Grenze:** 500.000 Zeilen sind ungeprüfte Selbstauskunft und kein Qualitätsmaß; Monorepo ist keine allgemeine Pflicht. [Rohtext](<../00_Inbox/Quellen/X/2026-01-12-dhruv1103-lessons-learned-500k-lines-claude-code.md>) · [Original](<https://www.reddit.com/r/ClaudeCode/comments/1id7vzv/what_i_learned_from_writing_500k_lines_with/>)

**Q0019 · 2026-01-12 · [Claude Code jenseits der Grundlagen: Skills, Subagents und MCP als ein System](<../80_Knowledge/Sources/2026-01-12-eyad-khrais-claude-code-tutorial-level-2.md>)**

Skills kodieren Verfahren, Subagents isolieren Arbeitskontexte und MCP verbindet externe Dienste. **Grenze:** Die behaupteten Kontextschwellen variieren selbst innerhalb desselben Autors; keine Messung. [Rohtext](<../00_Inbox/Quellen/X/2026-01-12-eyad-khrais-claude-code-tutorial-level-2.md>) · [Original](<https://x.com/eyad_khrais/status/2010810802023141688>)

**Q0020 · 2026-01-14 · [Spec-First Development: Ein persistenter Spec-Ordner statt Chat-Gedächtnis](<../80_Knowledge/Sources/2026-01-14-ashpreetbedi-claude-code-spec-first.md>)**

Ein Feature-Ordner trennt Design, Fortschritt, Entscheidungen, wiederverwendbare Prompts und spätere Arbeit als persistentes Gedächtnis. **Grenze:** Fünf Tage Bauzeit, 26 Beispiele und 30-Prozent-Kontextgrenze sind ungeprüfte Selbstangaben. [Rohtext](<../00_Inbox/Quellen/X/2026-01-14-ashpreetbedi-claude-code-spec-first.md>) · [Original](<https://x.com/ashpreetbedi/status/2011220028453241218>)

**Q0021 · 2026-01-15 · [Kontext klein halten: MCP-Overhead, Loop-Sessions, Phasentrennung](<../80_Knowledge/Sources/2026-01-15-avasdr34m-its-not-easy-but-it-is-simple-kontext-nutzung-in-claude-code-entscheidet.md>)**

MCP-Toolbeschreibungen und unnötige Historie beanspruchen Kontext; getrennte Research- und Implementierungsphasen können diesen gezielt erneuern. **Grenze:** Die genannten 500 Tokens pro Tool und der gezeigte Leistungsgraph sind nicht gemessene allgemeine Regeln. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-01-15-avasdr34m-its-not-easy-but-it-is-simple-kontext-nutzung-in-claude-code-entscheidet.md>) · [Original](<https://www.tiktok.com/@avasdr34m/video/7595680584995704086>)

**Q0022 · 2026-01-15 · [Präzise Aufträge für Einsteiger](<../80_Knowledge/Sources/2026-01-15-elenakvcs-vibe-coding-beginner-guide.md>)**

Konkrete Ein- und Ausgaben sowie kleine sofort geprüfte Schritte machen Alltagsautomatisierung beherrschbarer. **Grenze:** Sekundärfassung eines Einzelberichts; Modellvergleiche und Zeitgewinne sind unkontrolliert. [Original](<https://x.com/elenakvcs/status/2008228601980985550>) · Gleiche angegebene Herkunft: Q0023.

**Q0023 · 2026-01-15 · [Vibe Coding über Kommunikation und kleine Schritte](<../00_Inbox/Quellen/X/2026-01-15-unbekannt-vibe-coding-beginner-guide.md>)**

Beginne mit einer wiederkehrenden Aufgabe und präzisiere Ergebnis, Eingaben, Fehler und Prüfungen. **Grenze:** Gleiche Ursprungsquelle wie weitere Fassungen im Bestand; behauptete Einsparungen sind nicht unabhängig gemessen. [Original](<https://x.com/elenakvcs/status/2008228601980985550>) · Gleiche angegebene Herkunft: Q0022.

**Q0024 · 2026-01-17 · [Damien Ghader zu „The Complete Guide: Prompting Lovable for Design“](<../80_Knowledge/Sources/2026-01-17-damien-ghader-prompting-lovable-design.md>)**

Ein Design-System wird aus Foundations über Komponenten zur Komposition aufgebaut und über namentliche Referenzen stabilisiert. **Grenze:** Eine vage Aufforderung wie modern ersetzt keine konkreten Tokens oder Komponentenverträge. [Original](<https://x.com/damienghader/status/2012547182130336033>)

**Q0025 · 2026-01-20 · [Use the hookify plugin to spin up Claude code hooks easily on the fly!](<../00_Inbox/Quellen/TikTok/2026-01-20-agenticjames-use-the-hookify-plugin-to-spin-up-claude-code-hooks-easily-on-the-fly.md>)**

Hookify wird als Hilfsmittel zur ereignisbezogenen Konfiguration von Claude-Code-Hooks empfohlen. **Grenze:** Die Empfehlung enthält weder ein konkretes Hook-Beispiel noch einen eigenen Robustheitsnachweis. [Original](<https://www.tiktok.com/@agentic.james/video/7597264031451204877>)

**Q0026 · 2026-01-20 · [Ben Tossell zu „Wie ich mit Agents code, ohne 'technisch' zu sein“](<../80_Knowledge/Sources/2026-01-20-ben-tossell-agent-coding.md>)**

Aufmerksames Lesen von Agentenausgaben und konsequentes Nachfragen können Systemverständnis neben der Produktarbeit aufbauen. **Grenze:** Nicht selbst Code zu lesen verschiebt die Prüfanforderung auf belastbare Verifier. [Original](<https://x.com/bentossell/status/2006352820140749073>)

**Q0027 · 2026-01-20 · [Engineering und Codegenerierung entkoppeln](<../80_Knowledge/Sources/2026-01-20-mrexodia-vibe-engineering.md>)**

Investiere in klare Spezifikationen und einen ausführbaren Testharness, damit du Ergebnisse statt jeden generierten Tastendruck beurteilst. **Grenze:** Trust-the-Harness ersetzt weder schlecht abgedeckte Risiken noch jeden menschlichen Review; Kontextprozentzahlen sind Erfahrungsregeln. [Original](<https://x.com/mrexodia/status/2010157660885176767>)

**Q0028 · 2026-01-21 · [50 historische Claude-Tipps](<../00_Inbox/Quellen/X/2026-01-21-ai-edge-claude-50-pro-tips.md>)**

Eine schlanke Agent-Datei, Planungsmodus, reproduzierbare Prüfungen und gezielte Integrationen bilden eine brauchbare Grundausstattung. **Grenze:** Eine Tippsammlung aus zweiter Hand ist kein Wirksamkeitsnachweis; damalige Produktfunktionen und Kaufempfehlungen sind zeitgebunden. [Original](<https://x.com/aiedge_/status/2014009389427101949>) · Gleiche angegebene Herkunft: Q0029.

**Q0029 · 2026-01-21 · [Claude-Alltagstipps: Kontext-Resets, Kosten-Disziplin und Guardrails für autonome Agenten](<../80_Knowledge/Sources/2026-01-21-aiedge-claude-50-pro-tips.md>)**

Kontext-Resets, günstige Prototypen und aus Demonstrationen abgeleitete Skills bilden praktische, jedoch unbelegte Alltagstipps. **Grenze:** Fünfzig Tipps und wiederholte Herstellerzitate sind keine unabhängigen Wirkungsbelege. [Original](<https://x.com/aiedge_/status/2014009389427101949>) · Gleiche angegebene Herkunft: Q0028.

**Q0030 · 2026-01-21 · [Skill-Benchmark als Verkaufsargument: der Vibeship-Spawner-Case für Claude Skills](<../80_Knowledge/Sources/2026-01-21-meta-alchemist-claude-skills-deep-dive.md>)**

Skill-Nutzen muss gegen eine vergleichbare Baseline und mit reproduzierbaren Testfällen geprüft werden. **Grenze:** Vendor-Eigentest und KI-Selbstreflexion sind keine unabhängige Evaluation. [Rohtext](<../00_Inbox/Quellen/X/2026-01-21-meta-alchemist-claude-skills-deep-dive.md>) · [Original](<https://x.com/meta_alchemist/status/2007388392850641182>)

**Q0031 · 2026-01-21 · [Rules, Commands, Skills und Agenten](<../00_Inbox/Quellen/X/2026-01-21-tempoimmaterial-2014054104658526645.md>)**

Rules tragen Invarianten, Commands explizite Nutzerabsicht, Skills bedarfsorientierte Prozeduren und Agenten isolierte Arbeitsprofile. **Grenze:** Die Begriffe unterscheiden sich je Produkt; ein deterministischer Command-Aufruf garantiert keine deterministische Modellausführung. [Original](<https://x.com/tempoimmaterial/status/2014054104658526645>) · Gleiche angegebene Herkunft: Q0033, Q0032.

**Q0032 · 2026-01-21 · [Agent Skills vs. Rules vs. Commands](<../00_Inbox/Quellen/X/2026-01-21-tempoimmaterial-agent-skills-vs-rules.md>)**

Regeln tragen dauerhafte Invarianten, Commands explizite Aufrufe, Skills bedarfsabhängige Expertise und Subagents isolierte Arbeit. **Grenze:** Ein Skill ist Wissen für den laufenden Agenten, ein Subagent verändert Kontext und Zuständigkeit; konkrete Harness-Semantik bleibt versionsabhängig. [Original](<https://x.com/tempoimmaterial/status/2014054104658526645>) · Gleiche angegebene Herkunft: Q0031, Q0033.

**Q0033 · 2026-01-21 · [Skill-Architektur und Fehlermodi](<../80_Knowledge/Sources/2026-01-21-tempoimmaterial-agent-skills-vs-rules-vs-commands.md>)**

Gute Skills routen präzise, definieren Erfolg und laden umfangreiche Referenzen erst bei Bedarf. **Grenze:** Dieselbe Quelle wie weitere Fassungen im Bestand; die zitierte Starter-Bibliothek ist eine Heuristik, kein evaluierter Mindeststandard. [Original](<https://x.com/tempoimmaterial/status/2014054104658526645>) · Gleiche angegebene Herkunft: Q0031, Q0032.

**Q0034 · 2026-01-22 · [Lovable-Websites: Layout-Vorlagen, Spacing-Regeln und ein Conversion-Baukasten](<../80_Knowledge/Sources/2026-01-22-damien-lovable-website-guide.md>)**

Gestaltungsentscheidungen werden für Website-Builder durch benannte Layouts, Typografie, Breakpoints und konkrete CTA-Ziele überprüfbar. **Grenze:** Feste Zahlen und Conversion-Behauptungen stammen aus einer Sekundärquelle und sind keine universellen Design- oder Erfolgsregeln. [Rohtext](<../00_Inbox/Quellen/X/2026-01-22-damien-lovable-website-guide.md>) · [Original](<https://x.com/damienghader/status/2014341010600435925>)

**Q0035 · 2026-01-22 · [Alvaro Cintas zu „Claude Code lokal ausführen (Kostenlos & Privat)“](<../80_Knowledge/Sources/2026-01-22-dr-cintas-claude-code-local.md>)**

Ein Coding-Harness kann über Endpoint, Auth-Token und Modellname auf ein lokales Backend umgeleitet werden. **Grenze:** Lokaler Endpoint allein beweist weder vollständige Privatheit noch ausreichende Agentenleistung. [Original](<https://x.com/dr_cintas/status/2014380662300533180>)

**Q0036 · 2026-01-22 · [Sieben Lernschritte für Claude Code](<../80_Knowledge/Sources/2026-01-22-hooeem-claude-code-7-schritte-plan.md>)**

Toolschleife, Kontextpflege, Planung, Fehlerkorrektur, Hooks, Erweiterungen und CI gehören als getrennte Bausteine verstanden. **Grenze:** Mehrstufige Kurswiedergabe ohne eigene Messung; Hook-Beispiele und Tastenkürzel sind historisch und teilweise riskant vereinfacht. [Original](<https://x.com/hooeem/status/2007914329748668472>) · Gleiche angegebene Herkunft: Q0037.

**Q0037 · 2026-01-22 · [Claude Code lernen: Der 7-Schritte-Plan](<../00_Inbox/Quellen/X/2026-01-22-hooeem-claude-code-guide.md>)**

Ein Einstieg in Coding-Agents verbindet Kontextmanagement, Planung, Stop-/Recovery-Möglichkeiten, Toolzugriff und passende Feedbackschleifen. **Grenze:** Auto-Approve und ein Typecheck nach jedem Edit brauchen Risiko- und Kosteneinordnung; historische Shortcuts und Produktdetails sind nicht als aktuell bestätigt. [Original](<https://x.com/hooeem/status/2007914329748668472>) · Gleiche angegebene Herkunft: Q0036.

**Q0038 · 2026-01-23 · [Wertdichter Kontext als Arbeitsprinzip](<../00_Inbox/Quellen/X/2026-01-23-jarrodwatts-context-engineering-guide.md>)**

Hole Implementierungswissen bei Bedarf und verdichte Recherche, statt sämtliche Tools und Dokumente vorab zu laden. **Grenze:** Sekundärfassung derselben Jarrod-Watts-Quelle wie weitere Fassungen im Bestand; keine unabhängige Bestätigung. [Original](<https://x.com/jarrodwatts/status/2008495347115630701>) · Gleiche angegebene Herkunft: Q0015, Q0016.

**Q0039 · 2026-01-23 · [Claude Code's New Task System: The Practical Guide and Explainer](<../00_Inbox/Quellen/X/2026-01-23-nummanali-2014684862985175205.md>)**

Persistente Task-Graphen machen blockierende Abhängigkeiten, Zuständigkeiten und Arbeitsfortschritt über Kontextwechsel hinweg sichtbar. **Grenze:** Owner-Labels starten keine Agenten; der Artikel vermischt Variablennamen und behauptet teilweise stärkeres technisches Blocking als lokal geprüft. [Original](<https://x.com/nummanali/status/2014684862985175205>) · Gleiche angegebene Herkunft: Q0040.

**Q0040 · 2026-01-23 · [Persistente Task-Abhängigkeiten](<../80_Knowledge/Sources/2026-01-23-nummanali-claude-task-system.md>)**

Mehrstufige Arbeit benötigt explizite Voraussetzungen und einen gespeicherten Zustand außerhalb des Chatkontexts. **Grenze:** Konfliktfreie gemeinsame Aktualisierung wird behauptet, aber ohne Synchronisationsnachweis; Modellrollen sind historisch. [Rohtext](<../00_Inbox/Quellen/X/2026-01-23-nummanali-claude-task-system.md>) · [Original](<https://x.com/nummanali/status/2014684862985175205>) · Gleiche angegebene Herkunft: Q0039.

**Q0041 · 2026-01-25 · [Subagent-Kosten, Kontext-Haushalt und Cross-Model-Review: Praxisnotizen zu Claude Code 2.0](<../80_Knowledge/Sources/2026-01-25-sankalp-claude-code-experience.md>)**

Gezielter Handoff, getrennte Arbeitskontexte und Cross-Model-Review sind unterschiedliche Hebel zur Begrenzung von Kontextverfall. **Grenze:** Eine injizierte Erinnerung erzwingt keine tatsächliche Skill-Anwendung; feste Kontextprozentwerte bleiben heuristisch. [Rohtext](<../00_Inbox/Quellen/URL/2026-01-25-sankalp-claude-code-experience.md>) · [Original](<https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/>)

**Q0042 · 2026-01-26 · [Andrej Karpathy zu „Karpathys neuer Coding Workflow: 80% Agent, 20% Mensch“](<../80_Knowledge/Sources/2026-01-26-karpathy-coding-workflow-2026.md>)**

Karpathys Erfahrungsbericht verschiebt den Schwerpunkt vom manuellen Schreiben auf Erfolgskriterien, Architekturkritik und Verifikation agentengenerierten Codes. **Grenze:** Generation und Review sind unterschiedliche Fähigkeiten; sein 80/20-Verhältnis und Expansionseffekt sind individuelle Beobachtungen. [Original](<https://x.com/karpathy/status/2015883857489522876>)

**Q0043 · 2026-01-31 · [Wie das Claude-Code-Team bei Anthropic tatsächlich arbeitet](<../80_Knowledge/Sources/2026-01-31-bcherny-claude-code-team-tips.md>)**

Parallele Worktrees, Planreview und versionierte Skills bündeln institutionelles Wissen und trennen unabhängige Aufgaben. **Grenze:** Mehr Parallelität erhöht Koordinationskosten und ist kein universeller Leistungsbeweis. [Rohtext](<../00_Inbox/Quellen/X/2026-01-31-bcherny-claude-code-team-tips.md>) · [Original](<https://x.com/bcherny/status/2017742741636321619>)

**Q0044 · 2026-01-31 · [Kimi K2.5: Lokale Ausführung & Guide](<../00_Inbox/Quellen/URL/2026-01-31-unsloth-team-kimi-k2-5-local-guide.md>)**

Lokale Inferenz muss nach quantisiertem Modellumfang, RAM, VRAM und Auslagerungslatenz dimensioniert werden. **Grenze:** Speicherplatz ist kein Ersatz für ausreichende Bandbreite und nutzbare Tokenrate. [Original](<https://unsloth.ai/docs/models/kimi-k2.5>)


### 2026-02

**Q0045 · 2026-02-01 · [Claude Code Starter Pack: Boris' Setup, ein Fünf-Stufen-Lernpfad und ein zweifelhafter „bester Prompt“](<../80_Knowledge/Sources/2026-02-01-aiedge-claude-code-starter-pack.md>)**

Eine Starter-Kuration verbindet parallele Sessions, gepflegte Projektregeln, Klärungsdokumente und Erfolgskriterien vor Prompt-Iteration. **Grenze:** Die Boris-Infografik ist mehrfach abgeleitet; teuerstes Modell für alles widerspricht Kosteneskalation, der beworbene beste Persona-Prompt besitzt keinen Wirksamkeitsnachweis. [Original](<https://x.com/aiedge_/status/2011108297152082250>) · Gleiche angegebene Herkunft: Q0046.

**Q0046 · 2026-02-01 · [Claude Code Starter Pack: The Ultimate Resource Guide](<../00_Inbox/Quellen/X/2026-02-01-aiedge-claude-starter-pack.md>)**

Die Ressourcenliste ordnet Lernmaterial von CLI-Grundlagen über Skills und Hooks bis zu programmatischer Nutzung und Enterprise-Betrieb. **Grenze:** Gleiche URL wie Nr. 13, keine unabhängige Bestätigung; Link-Kuration und Superlative belegen noch keine Methodenwirkung. [Original](<https://x.com/aiedge_/status/2011108297152082250>) · Gleiche angegebene Herkunft: Q0045.

**Q0047 · 2026-02-01 · [Hooks als technische Lifecycle-Gates](<../80_Knowledge/Sources/2026-02-01-anthropic-docs-automate-workflows-with-hooks.md>)**

Deterministische Hooks eignen sich für eindeutig prüfbare Regeln; Modell- und Agent-Hooks treffen flexiblere, weniger vorhersagbare Urteile. **Grenze:** Ein Pfad-Substring gegen .env deckt weder alle Lesewege noch Shell-Ausgaben und indirekte Zugriffe ab; sekundärer Dokumentationsauszug. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-automate-workflows-with-hooks.md>) · [Original](<https://code.claude.com/docs/en/hooks-guide>)

**Q0048 · 2026-02-01 · [Claude Code Best Practices: Kontextfenster, Verifikation und CLAUDE.md-Disziplin](<../80_Knowledge/Sources/2026-02-01-anthropic-docs-claude-code-best-practices.md>)**

Konkrete Tests, Screenshots und erwartete Ausgaben geben dem Agenten einen überprüfbaren Arbeitsabschluss. **Grenze:** Dies ist eine sekundäre deutsche Fassung; verwandte Herstellerfassungen dürfen nicht als unabhängige Bestätigungen zählen. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-claude-code-best-practices.md>) · [Original](<https://code.claude.com/docs/en/best-practices>)

**Q0049 · 2026-02-01 · [Alltägliche Coding-Workflows](<../80_Knowledge/Sources/2026-02-01-anthropic-docs-claude-code-common-workflows.md>)**

Erkunde Komponenten und Ausführungsfluss, reproduziere Fehler und verifiziere Änderungen über ausführbare Prüfungen. **Grenze:** Herstellerrezepte sind kein Leistungsnachweis; CLI-Flags und Tastenkürzel gelten für den archivierten Stand. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-claude-code-common-workflows.md>) · [Original](<https://code.claude.com/docs/en/common-workflows>)

**Q0050 · 2026-02-01 · [Claude Code in GitLab CI/CD: Event-getriggerter Agent mit Merge-Request als Gate](<../80_Knowledge/Sources/2026-02-01-anthropic-docs-claude-code-gitlab-ci.md>)**

Ein event-getriggerter CI-Agent kann Änderungen in einem isolierten Runner vorbereiten und durch das vorhandene Merge-Request-Review führen. **Grenze:** Die Sekundärdokumentation bestätigt keine heutige GitLab-Installation; CLI-Flags, Images, OIDC und Berechtigungen müssen am Zielstand geprüft werden. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-claude-code-gitlab-ci.md>) · [Original](<https://code.claude.com/docs/en/gitlab-ci-cd>)

**Q0051 · 2026-02-01 · [Use Claude Code in VS Code](<../00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-claude-code-vs-code.md>)**

Eine IDE-Integration macht Dateikontext, Planprüfung, Diffs und Wiederaufnahme im bestehenden Editor zugänglich. **Grenze:** Die archivierten VS-Code-Voraussetzungen und Shortcuts sind historischer Produktstand; Rewind ist kein vollständiges Backup externer Nebenwirkungen. [Original](<https://code.claude.com/docs/en/vs-code>)

**Q0052 · 2026-02-01 · [MCP-Anbindung in Claude Code: Transporte, Scopes und Tool Search](<../80_Knowledge/Sources/2026-02-01-anthropic-docs-connect-claude-code-to-mcp.md>)**

MCP trennt die Anbindung externer Dienste von der fachlichen Anleitung und muss nach Transport, Scope und Rechten konfiguriert werden. **Grenze:** Ein offener Standard oder eine Teamkonfiguration macht einen Server nicht automatisch vertrauenswürdig. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-connect-claude-code-to-mcp.md>) · [Original](<https://code.claude.com/docs/en/mcp>)

**Q0053 · 2026-02-01 · [Claude-Code-Subagents: Konfiguration, Tool-Rechte und Modellwahl](<../80_Knowledge/Sources/2026-02-01-anthropic-docs-create-custom-subagents.md>)**

Isolierte Subagents brauchen einen klaren Auftrag, eigene Toolrechte, passende Skills und eine begrenzte Rückgabe. **Grenze:** Generische Bash-Rechte können eine rein namentliche Read-only-Zuordnung unterlaufen. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-create-custom-subagents.md>) · [Original](<https://code.claude.com/docs/en/sub-agents>)

**Q0054 · 2026-02-01 · [Erweiterungsebenen in Claude Code und ihre Kontext-Kosten](<../80_Knowledge/Sources/2026-02-01-anthropic-docs-extend-claude-code.md>)**

Projektregeln, Skills, Subagents, MCP, Hooks und Plugins erfüllen verschiedene Aufgaben und sollten entsprechend kombiniert werden. **Grenze:** Null Kontextkosten von Hooks gilt nicht für deren zurückgegebene Ausgaben oder injizierte Erinnerungen. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-extend-claude-code.md>) · [Original](<https://code.claude.com/docs/en/features-overview>)

**Q0055 · 2026-02-01 · [Skills in Claude Code: Frontmatter, Ort und Ausführung](<../80_Knowledge/Sources/2026-02-01-anthropic-docs-extend-claude-with-skills.md>)**

Skills bündeln Anweisungen und Ressourcen; Beschreibung, Aufrufrechte und optional isolierter Kontext steuern ihre Aktivierung. **Grenze:** Frontmatter und Command-Integration stammen aus einer nicht am Original nachgeprüften Sekundärfassung vom Februar 2026. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-extend-claude-with-skills.md>) · [Original](<https://code.claude.com/docs/en/skills>)

**Q0056 · 2026-02-01 · [Claude Code im Überblick: Agentic Loop, Sessions und Rechte](<../80_Knowledge/Sources/2026-02-01-anthropic-docs-how-claude-code-works.md>)**

Agentisches Arbeiten verbindet Kontextsammlung, Aktion und Verifikation in wiederholbaren Schritten mit getrenntem Session- und Berechtigungsmanagement. **Grenze:** Zugriff auf Projektdateien bedeutet nicht, dass das Modell alle Dateien bereits gelesen hat; konkrete Session- und Permission-Details sind versionsabhängig. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-01-anthropic-docs-how-claude-code-works.md>) · [Original](<https://code.claude.com/docs/en/how-claude-code-works>)

**Q0057 · 2026-02-01 · [Gemini 3.0: Elite Web Designer Prompt](<../00_Inbox/Quellen/X/2026-02-01-god-of-prompt-gemini-elite-web-designer.md>)**

Ein visueller Workflow kann Briefing, Seitenarchitektur, Design-System, Mockupreview und schrittweise Implementierung trennen. **Grenze:** Ein Bild kann Animation, Responsivität, Accessibility oder produktionsreifes Verhalten nicht nachweisen. [Original](<https://x.com/godofprompt/status/1991930251715440762>)

**Q0058 · 2026-02-01 · [Gemini Image Generation Guide](<../00_Inbox/Quellen/URL/2026-02-01-google-ai-gemini-image-generation.md>)**

Bildprompts sollten Motiv, Umgebung, Licht, Perspektive, Stil und gewünschte Änderungen als kohärente Szene beschreiben. **Grenze:** Ein generiertes UI-Bild ist eine visuelle Referenz ohne funktionale Prüfung. [Original](<https://ai.google.dev/gemini-api/docs/image-generation>)

**Q0059 · 2026-02-01 · [Tutorial: Nano Banana Pro (Gemini 3 Pro Image)](<../00_Inbox/Quellen/X/2026-02-01-google-ai-studio-nano-banana-pro-tutorial.md>)**

Bildgenerierung profitiert von konkreten Vorgaben zu Motiv, Komposition, Licht, Seitenverhältnis und schrittweiser visueller Iteration. **Grenze:** Modell-IDs, 4K-Fähigkeit, 14 Referenzbilder und API-Preise sind datierte Hersteller-/Sekundärangaben, keine aktuellen Fakten oder Qualitätsgarantien. [Original](<https://x.com/GoogleAIStudio/status/1992267030050083091>)

**Q0060 · 2026-02-01 · [Kyle (HumanLayer) zu „Writing a good CLAUDE.md“](<../80_Knowledge/Sources/2026-02-01-humanlayer-writing-a-good-claude-md.md>)**

Eine Agent-Datei sollte knappes bewusst gepflegtes Onboarding mit Links zu vertiefender Projektdokumentation bieten. **Grenze:** Warnung vor automatischem init steht anderen Einstiegs-Guides entgegen; Instruktionszahlen und Zeilenlimits sind Heuristiken, keine universellen Grenzen. [Original](<https://www.humanlayer.dev/blog/writing-a-good-claude-md>)

**Q0061 · 2026-02-01 · [Software-Testing von A bis "läuft wirklich](<../00_Inbox/Quellen/URL/2026-02-01-unbekannt-software-testing-guide.md>)**

Tests reduzieren unterschiedliche Risiken von isolierter Logik über Integration und UAT bis zur Validierung nach Go-live. **Grenze:** Die Primärquelle ist unbekannt; die Übersicht bleibt generisch und liefert keinen Agentenvergleich. 

**Q0062 · 2026-02-01 · [10 Regeln für effektives „Vibe Coding“](<../00_Inbox/Quellen/URL/2026-02-01-unbekannt-vibe-coding-rules.md>)**

Kleine testbare Schritte, klare Anforderungen, funktionierende Minimalbeispiele und gezielter Kontext verbinden schnelle Prototypen mit Engineering-Disziplin. **Grenze:** Anonyme Sekundärquelle ohne prüfbare Primärquelle; destruktive Git-Reset-Empfehlungen sind kein allgemeines sicheres Rücksetzverfahren. 

**Q0063 · 2026-02-01 · [Eine gute AGENTS.md schreiben](<../00_Inbox/Quellen/URL/2026-02-01-unbekannt-writing-agents-md.md>)**

Eine Agentendatei sollte Projektzweck, Navigation und Prüfwege knapp erklären und Spezialwissen über präzise Referenzen zugänglich machen. **Grenze:** Die Instruktionszahlen und Zeilenlimits sind Heuristiken; dieselbe HumanLayer-Quelle liegt in mehreren Fassungen vor. 

**Q0064 · 2026-02-02 · [Plan, Findings und Fortschritt](<../80_Knowledge/Sources/2026-02-02-anthony-riera-planning-with-files-skill.md>)**

Persistente Dateien für Plan, Erkenntnisse und Fortschritt geben langen Sessions einen wiederauffindbaren Arbeitsstand. **Grenze:** 99 Prozent Ersterfolg und fast vollständige Driftfreiheit sind unbelegte Werbeaussagen. [Rohtext](<../00_Inbox/Quellen/X/2026-02-02-anthony-riera-planning-with-files-skill.md>) · [Original](<https://x.com/anthonyriera/status/2018221220160827828>)

**Q0065 · 2026-02-02 · [Claude Code und OpenAI Codex vollständig lokal: Unsloth-Anleitung mit llama.cpp](<../80_Knowledge/Sources/2026-02-02-unsloth-team-claude-code-local-llm.md>)**

Ein lokaler Serving-Stack kann über passende Providerkonfigurationen hinter vorhandenen Coding-CLIs betrieben werden. **Grenze:** Historische Hardware- und API-Angaben sind kein aktuell getestetes Setup; Bypassflags senken keine Risiken. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-02-unsloth-team-claude-code-local-llm.md>) · [Original](<https://unsloth.ai/docs/basics/claude-codex>)

**Q0066 · 2026-02-03 · [Prompt gegen typische Agentenfehler](<../80_Knowledge/Sources/2026-02-03-god-of-prompt-karpathy-ai-coding-system-prompt.md>)**

Annahmen offenlegen, Widersprüche klären, den Scope begrenzen und Erfolgskriterien testen adressiert häufige Agentenfehler. **Grenze:** Der lange System-Prompt ist ungetestet und kann selbst Kontext belasten; die Zuschreibung an Karpathy ist vermittelt. [Rohtext](<../00_Inbox/Quellen/X/2026-02-03-god-of-prompt-karpathy-ai-coding-system-prompt.md>) · [Original](<https://x.com/godofprompt/status/2018482335130296381?s=20>)

**Q0067 · 2026-02-03 · [Regeldatei mit Planung und reproduzierbaren Fehlern](<../80_Knowledge/Sources/2026-02-03-svpino-claude-code-md-tips.md>)**

Eine Agent-Datei kann Planungs-, Test- und Scope-Regeln bündeln, sollte aber nicht nach jeder Korrektur unkontrolliert wachsen. **Grenze:** Die Drei-Dateien-Schwelle ist willkürlich; Freigaben und automatische Regelergänzung müssen zum tatsächlichen Arbeitsmodus passen. [Rohtext](<../00_Inbox/Quellen/X/2026-02-03-svpino-claude-code-md-tips.md>) · [Original](<https://x.com/svpino/status/2018682144361734368>)

**Q0068 · 2026-02-04 · [@affaanmustafa zu „The Shorthand Guide to Everything Claude Code“ (Primärquelle)](<../80_Knowledge/Sources/2026-02-04-affaanmustafa-shorthand-guide-primaer.md>)**

Nur tatsächlich benötigte Tools und Plugins sollten gleichzeitig aktiv sein; Pre- und Post-Tool-Hooks adressieren verschiedene Kontrollpunkte. **Grenze:** Grenzen wie unter zehn MCPs und achtzig Tools sind setupabhängige Faustregeln. [Original](<https://x.com/affaanmustafa/status/2012378465664745795>)

**Q0069 · 2026-02-04 · [10 Claude Code Prompts You Need to Steal](<../00_Inbox/Quellen/X/2026-02-04-aiedge-10-claude-code-prompts-you-need-to-steal.md>)**

Prompt-Vorlagen strukturieren Anforderungen, Diagnose, kleine Umsetzungsschritte und verständliche Übergaben für Einsteiger. **Grenze:** Die Sammlung bietet keine Wirkungsmessung; generische Freigabepausen ersetzen keine aufgabenspezifische Autorisierung. [Original](<https://x.com/aiedge_/status/2018356670070718614>)

**Q0070 · 2026-02-04 · [Lovable Docs zu „Best Practices für Lovable“](<../80_Knowledge/Sources/2026-02-04-lovable-docs-best-practices.md>)**

Lovable-Prototypen lassen sich mit projektweiter Knowledge-Datei, einzelnen testbaren Bausteinen und Mock-Daten vor der Backend-Anbindung entwickeln. **Grenze:** Die 60–70 Prozent Planungszeit sind keine allgemeine Norm; Code-Rücksetzen setzt Datenbankschemata nicht zuverlässig zurück. [Original](<https://docs.lovable.dev/tips-tricks/best-practice>)

**Q0071 · 2026-02-04 · [Lovable-Sicherheitsleitfaden: Drei Schichten, drei Verantwortungen](<../80_Knowledge/Sources/2026-02-04-lovable-docs-lovable-security-guide.md>)**

Die Sicherheitsaufgaben generierter Webapps verteilen sich auf öffentliches Frontend, serverseitige Geschäftslogik und Datenbank-Zugriffskontrollen. **Grenze:** Ein herstellereigener Security Checker beweist keine Sicherheit; konkrete RLS-Policies und Rollen müssen gegen unerlaubte Zugriffe geprüft werden. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-04-lovable-docs-lovable-security-guide.md>) · [Original](<https://docs.lovable.dev/tips-tricks/avoiding-security-pitfalls>)

**Q0072 · 2026-02-04 · [Lovable-Debugging: Plan-Modus, Audit-Prompts und Ursache statt Symptom](<../80_Knowledge/Sources/2026-02-04-lovable-docs-prompting-debugging.md>)**

Hartnäckige Fehler brauchen nachvollzogene Datenflüsse, bekannte bisherige Versuche, isolierte Minimalfälle und eine Korrektur der Ursache. **Grenze:** Eine Vorsichtsformulierung im Prompt schafft keine technische Absicherung; gezielte Checks und wiederherstellbarer Zustand bleiben notwendig. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-04-lovable-docs-prompting-debugging.md>) · [Original](<https://docs.lovable.dev/prompting/prompting-debugging>)

**Q0073 · 2026-02-04 · [Skill-Anatomie und Progressive Disclosure](<../80_Knowledge/Sources/2026-02-04-meer-aiit-claude-skills-complete-guide.md>)**

Skills kombinieren präzise Trigger mit einer Prozedur und bedarfsweise geladenen Referenzen, Scripts und Assets. **Grenze:** Einmal erstellen und immer gleiche Qualität erhalten ist unbelegt; Zeilen- und Tokenbudgets sind Richtwerte. [Rohtext](<../00_Inbox/Quellen/X/2026-02-04-meer-aiit-claude-skills-complete-guide.md>) · [Original](<https://x.com/Meer_AIIT/status/2017984668205756551>)

**Q0074 · 2026-02-04 · [Providerwechsel mit Routingprüfung](<../80_Knowledge/Sources/2026-02-04-rudrank-using-minimax-with-claude-code.md>)**

Bei einem Providerwechsel sollten Endpunkt, Modell und Zugangsdaten konsistent gesetzt und das tatsächliche Routing geprüft werden. **Grenze:** Anthropic-kompatible Schnittstellen garantieren nicht identische Toolfähigkeit oder Qualität; Modelle und Preise sind vom Februar 2026. [Original](<https://x.com/rudrank/status/2018272804966449209>)

**Q0075 · 2026-02-04 · [TDD im Agentic Coding: Tests als kleinteilige Spezifikation](<../80_Knowledge/Sources/2026-02-04-tweag-tdd-agentic-coding.md>)**

Verhaltenstests zerlegen regelreiche Geschäftslogik in kleine implementierbare und überprüfbare Schritte. **Grenze:** Tests des Implementierungsautors können dessen Fehler bestätigen; weniger Halluzinationen wird nicht gemessen. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-04-tweag-tdd-agentic-coding.md>) · [Original](<https://tweag.github.io/agentic-coding-handbook/WORKFLOW_TDD/>)

**Q0076 · 2026-02-05 · [Claude Code for Everyone: Der interaktive Kurs](<../00_Inbox/Quellen/URL/2026-02-05-carl-vellotti-claude-code-for-everyone-course.md>)**

Ein interaktiver Kurs innerhalb des Coding-Tools kann Bedienung, Dateiarbeit, Planung und erste Produktiteration anhand echter Aufgaben vermitteln. **Grenze:** Reine Kursbeschreibung ohne Lernerfolgsmessung; Zeitbedarf, Preis und beworbene Einzigartigkeit bleiben historische Aussagen. [Original](<https://ccforeveryone.com/>)

**Q0077 · 2026-02-05 · [Parallele Agenten beim Compilerbau](<../80_Knowledge/Sources/2026-02-05-carlini-anthropic-c-compiler.md>)**

Lange autonome Entwicklung hängt von präzisen Verifiern, Referenzsystemen und sinnvoll geteilten Aufgaben ab. **Grenze:** Herstellerfallstudie mit hohen Kosten und dokumentierten Regressionen; erfolgreiche Builds beweisen keine vollständige Sicherheit. [Original](<https://www.anthropic.com/engineering/building-c-compiler>)

**Q0078 · 2026-02-05 · [Sandbox und Freigaben trennen](<../80_Knowledge/Sources/2026-02-05-d4m1n-docker-sandboxes.md>)**

Autonome Agenten benötigen technische Isolation und begrenzte Iterationen, wenn häufige Einzelbestätigungen entfallen. **Grenze:** Die Behauptung eines vollständig unangetasteten Hosts ist zu weitgehend; Mounts, Netzwerke und Credentials bleiben gesondert zu prüfen. [Original](<https://x.com/d4m1n/status/2019366063226355930>)

**Q0079 · 2026-02-05 · [Technisches Grundwissen für Vibe Coding](<../00_Inbox/Quellen/X/2026-02-05-harshil-tomar-vibe-coding-roadmap.md>)**

Git, APIs, Logs, Terminal, Datenbanken und sichere Konfiguration bleiben Grundlagen KI-gestützter Entwicklung. **Grenze:** Generische Einsteigerliste ohne neue agentenspezifische Methode; im Archiv bereits ignoriert. [Original](<https://x.com/Hartdrawss/status/2019433363287806243>)

**Q0080 · 2026-02-05 · [Feature-Planung entlang der User Journey](<../80_Knowledge/Sources/2026-02-05-kloss-xyz-feature-intelligence-architect.md>)**

Ein Planer sollte zunächst den Ist-Zustand verstehen und Features nach Nutzerweg, bestehendem Nutzen und Regressionsrisiko filtern. **Grenze:** Persona-Rhetorik beweist keine Produktkompetenz; viele Pflichtdokumente kosten Kontext und ersetzen keine Nutzerforschung. [Rohtext](<../00_Inbox/Quellen/X/2026-02-05-kloss-xyz-feature-intelligence-architect.md>) · [Original](<https://x.com/kloss_xyz/status/2019152438910165393?s=20>)

**Q0081 · 2026-02-05 · [Deep Dive: Agent Skills verstehen und bauen](<../00_Inbox/Quellen/X/2026-02-05-tadas-petra-agent-skills-deep-dive.md>)**

Skills bündeln Fachwissen in einer kleinen SKILL.md und laden Referenzen, Scripts oder Assets nur bei Bedarf nach. **Grenze:** Die Quelle wiederholt Skill-Grundlagen und misst keine tatsächliche Erfolgsrate. [Original](<https://x.com/tadaspetra/status/2019204136982532407>)

**Q0082 · 2026-02-07 · [Agent Teams in Claude Code](<../00_Inbox/Quellen/X/2026-02-07-dani_avila7-2020170608290549906.md>)**

Agententeams arbeiten mit eigenem Kontext, klarer Dateizuständigkeit, operationalem Projektwissen und einem passenden Verifikationsvertrag. **Grenze:** Konfliktfreiheit bei neun bereinigten Dateien ist ein einzelner Selbstbericht, kein Nachweis für große gemeinsam bearbeitete Systeme. [Original](<https://x.com/dani_avila7/status/2020170608290549906>) · Gleiche angegebene Herkunft: Q0084, Q0083.

**Q0083 · 2026-02-07 · [Advanced Patterns für Agent Teams in Claude Code](<../00_Inbox/Quellen/X/2026-02-07-daniel-san-advanced-agent-teams-patterns.md>)**

Parallele Arbeit wird durch Modulgrenzen, kurze gemeinsame Projektregeln und konkrete Ergebnisberichte koordinierbar. **Grenze:** Gleiche Ursprungsquelle wie Nr. 27; die behauptete feste Modus-Lebensdauer und Feature-Flags sind versionsabhängig. [Original](<https://x.com/dani_avila7/status/2020170608290549906>) · Gleiche angegebene Herkunft: Q0084, Q0082.

**Q0084 · 2026-02-07 · [Agent Teams mit klaren Grenzen](<../80_Knowledge/Sources/2026-02-07-daniel-san-agent-teams-praxismuster.md>)**

Modulgrenzen, kurzer operationaler Kontext und definierte Verifikation sind Voraussetzungen sinnvoller Agententeams. **Grenze:** Neun konfliktfreie Dateien sind ein Einzelbericht; Plan-Mode-Details sind historischer, ungeprüfter Laufzeitbefund. [Original](<https://x.com/dani_avila7/status/2020170608290549906>) · Gleiche angegebene Herkunft: Q0082, Q0083.

**Q0085 · 2026-02-07 · [Teamkoordination über Tasks und Nachrichten](<../00_Inbox/Quellen/X/2026-02-07-jason-zhou-claude-code-agent-teams.md>)**

Agententeams ergänzen isolierte Subagenten um gemeinsame Tasks, Nachrichten und Lifecycle-Steuerung. **Grenze:** Mehr Agenten kosten zusätzliche Zeit und Tokens; die Quelle zeigt keine generelle Überlegenheit. [Original](<https://x.com/jasonzhou1993/status/2020086991740891526>) · Gleiche angegebene Herkunft: Q0086, Q0087.

**Q0086 · 2026-02-07 · [Gegenseitige Widerlegung im Agententeam](<../80_Knowledge/Sources/2026-02-07-jasonzhou-claude-code-agent-teams.md>)**

Bei komplexen Fehlern können getrennte Untersuchungen und anschließende Kritik Befunde präzisieren und falsche Hypothesen verwerfen. **Grenze:** Gleiche Ursprungsquelle wie weitere Fassungen im Bestand; Reverse-Engineering und vermuteter Shutdown-Hook sind keine verifizierte Engine-Spezifikation. [Original](<https://x.com/jasonzhou1993/status/2020086991740891526>) · Gleiche angegebene Herkunft: Q0085, Q0087.

**Q0087 · 2026-02-07 · [How to install and use Claude Code Agent Teams (Reverse-engineered)](<../00_Inbox/Quellen/X/2026-02-07-jasonzhou1993-2020086991740891526.md>)**

Langlebige Agententeams ergänzen isolierte Subagents um Nachrichten, geteilte Tasks und explizite Lebenszyklen für voneinander abhängige Untersuchungen. **Grenze:** Reverse-Engineering-Bericht ohne eigenen Benchmark; mehr Kommunikation verursacht zusätzlichen Token- und Koordinationsaufwand. [Original](<https://x.com/jasonzhou1993/status/2020086991740891526>) · Gleiche angegebene Herkunft: Q0085, Q0086.

**Q0088 · 2026-02-09 · [Skills als situationsbezogenes Fachwissen](<../00_Inbox/Quellen/X/2026-02-09-pdrmnvd-2020967757706297797.md>)**

Skills halten projektspezifische Expertise bereit, ohne alle Detailanweisungen in jede Unterhaltung zu laden. **Grenze:** Konkrete Aussagen zur internen Systemnachrichten-Injektion sind produktspezifisch; Fachwissen und gutes Routing garantieren keine Wirkung. [Original](<https://x.com/pdrmnvd/status/2020967757706297797>) · Gleiche angegebene Herkunft: Q0089.

**Q0089 · 2026-02-09 · [Claude-Code-Skills: vom Generalisten zum Spezialisten per Progressive Disclosure](<../80_Knowledge/Sources/2026-02-09-pdrmnvd-how-claude-code-skills-work.md>)**

Skill-Spezifität sollte an die Fragilität der Operation angepasst werden und den Zweck hinter Regeln erklären. **Grenze:** Eine ungefähr hundert Wörter lange Description ist keine Kostenkonstante; Systemnachrichten-Rang ist harnessabhängig. [Rohtext](<../00_Inbox/Quellen/X/2026-02-09-pdrmnvd-how-claude-code-skills-work.md>) · [Original](<https://x.com/pdrmnvd/status/2020967757706297797>) · Gleiche angegebene Herkunft: Q0088.

**Q0090 · 2026-02-09 · [`/insights` als Feedback-Schleife für den eigenen Claude-Code-Workflow](<../80_Knowledge/Sources/2026-02-09-tom-crawshaw-claude-code-insights-guide.md>)**

Nutzungslogs können mehrdeutige Projektverweise, unklare Fertigkriterien und wiederholte Exploration als Ansatzpunkte für Workflowpflege sichtbar machen. **Grenze:** Die Zahlen stammen von einem einzelnen Nutzer; automatisch vorgeschlagene Selbstverbesserung wurde nicht als funktionierendes System gezeigt. [Rohtext](<../00_Inbox/Quellen/X/2026-02-09-tom-crawshaw-claude-code-insights-guide.md>) · [Original](<https://x.com/tomcrawshaw01/status/2020866308230009189>)

**Q0091 · 2026-02-10 · [Research und annotierter Plan](<../00_Inbox/Quellen/URL/2026-02-10-boris-tane-boris-tane-claude-code-workflow.md>)**

Ein schriftlicher Research-Bericht und ein mehrfach annotierter Plan erlauben fachliche Korrektur vor der Implementierung. **Grenze:** Fehlerfreie mechanische Implementierung ist übertrieben; die Empfehlung einer langen Session steht neben Neustart-Empfehlungen anderer Quellen. [Original](<https://boristane.com/blog/how-i-use-claude-code/>) · Gleiche angegebene Herkunft: Q0093, Q0092.

**Q0092 · 2026-02-10 · [Der Annotations-Zyklus: Plan als geteilter Zwischenzustand zwischen Mensch und Claude](<../80_Knowledge/Sources/2026-02-10-boris-tane-plan-annotation-workflow.md>)**

Editierbare Research- und Plan-Dateien ermöglichen einen Annotationszyklus, in dem Menschen Domänenwissen, Scope und Schnittstellen vor der Umsetzung korrigieren. **Grenze:** Tanes durchgehende lange Session widerspricht frischem Kontext pro Phase; beide Positionen beruhen auf Erfahrungsberichten, nicht kontrollierten Vergleichen. [Original](<https://boristane.com/blog/how-i-use-claude-code/>) · Gleiche angegebene Herkunft: Q0091, Q0093.

**Q0093 · 2026-02-10 · [Annotierter Plan als Reviewfläche](<../00_Inbox/Quellen/URL/2026-08-05-boristane-how-i-use-claude-code.md>)**

Detaillierte Analyse, ein editierbarer Plan und gezielte Annotationen übertragen fachliches Urteil in die Umsetzung. **Grenze:** Gleiche Ursprungsquelle wie weitere Fassungen im Bestand; die Erfahrung mit langen Sessions widerspricht pauschalen Kontextgrenzen, ohne sie empirisch zu widerlegen. [Original](<https://boristane.com/blog/how-i-use-claude-code/>) · Gleiche angegebene Herkunft: Q0091, Q0092.

**Q0094 · 2026-02-11 · [Skill-Qualität vorab definieren](<../80_Knowledge/Sources/2026-02-11-rohit4verse-guide-building-agent-skills.md>)**

Definiere reale Triggerfälle, erwartete Ergebnisse, Toolaufwand und Konsistenz, bevor ein Skill gebaut wird. **Grenze:** 90 Prozent Triggerquote und Marktanteilszahlen sind unbelegte Zielwerte; allowed-tools ist nicht in jedem Harness eine vollständige Sicherheitsgrenze. [Rohtext](<../00_Inbox/Quellen/X/2026-02-11-rohit4verse-guide-building-agent-skills.md>) · [Original](<https://x.com/rohit4verse/status/2021622526112358663>)

**Q0095 · 2026-02-13 · [Fullstack mit Claude Code: Sichtbarkeit, aktuelle Docs und ein meinungsstarker Stack statt Feature-Sammlung](<../80_Knowledge/Sources/2026-02-13-vincanger-claude-code-fullstack-essentials.md>)**

Fullstack-Agenten benötigen beobachtbare Laufzeit- und Browserergebnisse, aktuelle versionsbezogene Dokumentation und klare vorhandene Projektmuster. **Grenze:** Wasp-Empfehlungen sind interessengeleitet; weniger Konfigurationszeilen und llms.txt-Tokenersparnis belegen keine höhere Gesamtsicherheit. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-13-vincanger-claude-code-fullstack-essentials.md>) · [Original](<https://dev.to/wasp/claude-code-for-fullstack-development-the-3-things-you-actually-need-1p6p>)

**Q0096 · 2026-02-14 · [25 Praxis-Lektionen zu Claude Code: Kontext, Subagents, parallele Sessions](<../80_Knowledge/Sources/2026-02-14-gmoney-eth-25-claude-code-lessons.md>)**

Persistente Logs, kuratierte Erinnerungen, klare Rollen und getrennte Worktrees können länger laufende Agentenarbeit strukturieren. **Grenze:** Persönlichkeitsdateien und drei- bis fünffache Sessions sind Erfahrungspraktiken, kein Wirkungsbeweis. [Rohtext](<../00_Inbox/Quellen/X/2026-02-14-gmoney-eth-25-claude-code-lessons.md>) · [Original](<https://x.com/gmoneyNFT/status/2022454519741767800>)

**Q0097 · 2026-02-14 · [Vertikale TDD-Slices](<../80_Knowledge/Sources/2026-02-14-matt-pocock-skill-tdd-claude-code.md>)**

Ein Test und die dazu nötige Implementierung pro Schritt halten Agenten näher am beobachtbaren Verhalten als große getrennte Test- und Codeblöcke. **Grenze:** Ein zuerst roter Test verhindert Manipulation nicht technisch vollständig; unabhängige Verifikation bleibt nötig. [Original](<https://www.aihero.dev/skill-test-driven-development-claude-code>)

**Q0098 · 2026-02-14 · [Mastering Claude Code: Memory-System, Orchestrator-Modell und Skills](<../80_Knowledge/Sources/2026-02-14-minty-mastering-claude-code.md>)**

Ein dünner Memory-Index mit Detaildateien trennt stabiles Wissen, laufende Projekte und rollierende Sessionübergaben. **Grenze:** Die konkrete Anbieter-Rollenverteilung ist subjektiv und historisch; visueller Erfolg braucht Rendering. [Rohtext](<../00_Inbox/Quellen/X/2026-02-14-minty-mastering-claude-code.md>) · [Original](<https://x.com/DeFiMinty/status/2022470560505090071>)

**Q0099 · 2026-02-15 · [Design durch Referenzen und mehrere Durchgänge](<../80_Knowledge/Sources/2026-02-15-avid-ai-design-workflow-2026.md>)**

Visuelle Referenzen, präzises Designvokabular und getrennte Entwurfs-, Review- und Politurphasen verbessern die Steuerbarkeit von KI-Design. **Grenze:** Die Prozentwerte für Self-Review und Zeitersparnis sind ungemessen; ein großer Context Dump kann Kontextqualität verschlechtern. [Rohtext](<../00_Inbox/Quellen/X/2026-02-15-avid-ai-design-workflow-2026.md>) · [Original](<https://x.com/Av1dlive/status/2023086925817729306>)

**Q0100 · 2026-02-17 · [Premium Proposals & Slide Decks mit Lovable: Der komplette Guide](<../00_Inbox/Quellen/X/2026-02-17-damien-lovable-proposals-guide.md>)**

Angebotsformate sollten zum Lesemodus passen: scrollbare Dokumente für asynchrone Prüfung, Decks für live begleitete Erzählung. **Grenze:** Umsatz- und Großkundenbeispiele sind unbelegte Marketingbehauptungen. [Original](<https://x.com/damienghader/status/2023780178128728201>)

**Q0101 · 2026-02-19 · [Claude Code: Planprüfung und Feedback trotz weitgehender Codegenerierung](<../80_Knowledge/Sources/2026-02-19-lenny-s-podcast-head-of-claude-code-what-happens-after-coding-is.md>)**

Schnelle Nutzerfeedbackschleifen, geprüfte Pläne und ein an Modellfähigkeit angepasstes Werkzeuggerüst verbinden Produktentwicklung und Agentenarbeit. **Grenze:** Programmierung sei gelöst, Produktivität plus zweihundert Prozent und maximale Tokenbudgets sind Anbieter-Selbstberichte bzw. Wertungen. PR-Anzahl ist keine Qualitäts- oder Nutzermetrik. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-02-19-lenny-s-podcast-head-of-claude-code-what-happens-after-coding-is.md>) · [Original](<https://www.youtube.com/watch?v=We7BZVKbCVw>)

**Q0102 · 2026-02-20 · [Iterative modellübergreifende Planreviews](<../80_Knowledge/Sources/2026-02-20-aseem-shrey-claude-codex-plan-review.md>)**

Ein separater Read-only-Reviewer kann Pläne prüfen und die tatsächliche Behebung seiner Befunde in begrenzten Folgerunden verifizieren. **Grenze:** 14 Probleme in drei Runden sind ein einzelnes Beispiel; unterschiedliche Modelle sind keine Garantie unabhängiger Fehler. [Original](<https://aseemshrey.in/blog/claude-codex-iterative-plan-review/>)

**Q0103 · 2026-02-20 · [Tane: Der SDLC kollabiert zum Loop aus Intent, Build und Observe](<../80_Knowledge/Sources/2026-02-20-boris-tane-sdlc-is-dead.md>)**

Ein enger Intent–Build–Observe-Loop kann technische Phasen schneller verbinden und Telemetrie als Rückmeldung in die nächste Iteration tragen. **Grenze:** Die These vom toten SDLC und der Ersatz menschlicher Reviews sind unbelegt und stehen Tanes eigener planorientierter Praxis gegenüber. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-20-boris-tane-sdlc-is-dead.md>) · [Original](<https://boristane.com/blog/the-software-development-lifecycle-is-dead/>)

**Q0104 · 2026-02-23 · [Dan (@d4m1n) zu „Ralph Loop: Das ultimative Setup“ (Primärquelle)](<../80_Knowledge/Sources/2026-02-23-d4m1n-ralph-loop-setup-primaer.md>)**

Autonome Iterationen brauchen persistente Aufgaben, Steuerungsdateien, Logs und ausführbare Tests als Fortschrittsnachweis. **Grenze:** Siebenunddreißig Stunden und zweihundertfünfzig Aufgaben sind Selbstangaben; neuartige Architektur und Sicherheit bleiben Schwächen. [Original](<https://x.com/d4m1n/status/2026032801322356903>)

**Q0105 · 2026-02-23 · [Zwei-Tier-Orchestrierung: Ein Business-Orchestrator steuert eine Flotte paralleler Coding-Agents](<../80_Knowledge/Sources/2026-02-23-elvis-openclaw-codex-agent-swarm.md>)**

Ein Business-Orchestrator kann strategischen Kontext halten und technische Tasks mit begrenzten Rechten an isolierte Worker geben. **Grenze:** Worktrees isolieren Dateien, keine Systemrechte; der privilegierte Orchestrator konzentriert Risiken und Reviewer-Kosten fehlen. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-23-elvis-openclaw-codex-agent-swarm.md>) · [Original](<https://x.com/elvissun/status/2025920521871716562>)

**Q0106 · 2026-02-24 · [Complete Guide to NotebookLM](<../00_Inbox/Quellen/URL/2026-02-24-aakash-gupta-notebooklm-complete-guide.md>)**

Quellengebundene Recherche lässt sich über gezielte Quellenauswahl, Lückenfragen und wiederverwendbare Artefaktspezifikationen in Produktkommunikation überführen. **Grenze:** Die NotebookLM-Produktbeschreibung ist sekundär und historisch; Quellenbindung verhindert weder Auswahlfehler noch falsche Schlussfolgerungen. [Original](<https://www.news.aakashg.com/p/complete-guide-to-notebooklm>)

**Q0107 · 2026-02-24 · [Intent Engineering für organisatorischen Nutzen](<../00_Inbox/Quellen/YouTube/2026-02-24-ai-news-strategy-daily-n-prompt-engineering-is-dead-context-engineering-i.md>)**

Agentenziele benötigen ausdrücklich beschriebene Werte, Zielkonflikte, Entscheidungsgrenzen und Feedback über geschäftlichen Nutzen. **Grenze:** Klarna-, Copilot- und Umfragezahlen sind sekundär berichtet; falsche Zieloptimierung ist eine Interpretation, keine nachgewiesene alleinige Ursache. [Original](<https://www.youtube.com/watch?v=QWzLPn164w0>) · Gleiche angegebene Herkunft: Q0108.

**Q0108 · 2026-02-24 · [Nate B. Jones zu „Intent Engineering: Warum Prompt- und Context-Optimierung allein nicht mehr reichen“](<../80_Knowledge/Sources/2026-02-24-nate-b-jones-intent-engineering.md>)**

Explizite Zielhierarchien, erlaubte Trade-offs und Eskalationsregeln ergänzen Prompt und Kontext um organisatorischen Intent. **Grenze:** Klarna- und Copilot-Zahlen sind im Archiv nicht unabhängig verifiziert; ein Agent kann eine falsche Metrik erfolgreich optimieren. [Original](<https://www.youtube.com/watch?v=QWzLPn164w0>) · Gleiche angegebene Herkunft: Q0107.

**Q0109 · 2026-02-25 · [Claude Cowork einrichten: Kontextdateien und Rückfragen](<../80_Knowledge/Sources/2026-02-25-heynavtoor-claude-cowork-setup-guide.md>)**

Gemeinsame Kontextdateien zu Person, Schreibstil und Arbeitsweise lassen sich mit projektspezifischen Rückfragen verbinden. **Grenze:** Ein Rückfragetool verhindert Halluzinationen nicht automatisch; Grenzen und Kosten sind historisch. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-25-heynavtoor-claude-cowork-setup-guide.md>) · [Original](<https://x.com/heynavtoor/status/2026717574776631556>)

**Q0110 · 2026-02-26 · [Elvis (@omarsar0) zu „Hilft AGENTS.md wirklich?“](<../80_Knowledge/Sources/2026-02-26-omarsar0-agents-md-evaluation.md>)**

Agentendateien sollten fehlendes institutionelles Wissen ergänzen statt vorhandene README-Informationen zu wiederholen. **Grenze:** Ergebnisse eines kleinen Python-Repo-Benchmarks sind keine universelle Aussage über alle Agentendateien. [Original](<https://x.com/omarsar0/status/2027025098578727353>)

**Q0111 · 2026-02-27 · [Claude Code Best Practices: So nutzt du das volle Potenzial (100x Powerful)](<../00_Inbox/Quellen/X/2026-02-27-meer-ai-tools-news-claude-code-best-practices-2026.md>)**

Überprüfbare Aufgaben, Planreview, rohe Fehlerdaten und gezielte Kontextresets strukturieren die Arbeit mit Coding-Agents. **Grenze:** Die hundertfache Wirkung ist Marketing; wiederholte Herstellerangaben zählen nicht mehrfach. [Original](<https://x.com/Meer_AIIT/status/2027509711722188976>) · Gleiche angegebene Herkunft: Q0112.

**Q0112 · 2026-02-27 · [Claude-Code-Power-Tipps: Was über die offizielle Doku hinausgeht](<../80_Knowledge/Sources/2026-02-27-meer-claude-code-best-practices.md>)**

Eine zweite Instanz kann bereits den Plan prüfen, während Voice Input zusätzlichen Hintergrund für komplexe Aufgaben liefert. **Grenze:** Diese Familie ist inhaltlich dieselbe Ursprungsquelle wie die zuvor gelesene Meer-Rohfassung. [Original](<https://x.com/Meer_AIIT/status/2027509711722188976>) · Gleiche angegebene Herkunft: Q0111.

**Q0113 · 2026-02-27 · [Thariq zu „Lessons from Building Claude Code: So lernst du, wie ein Agent zu sehen“](<../80_Knowledge/Sources/2026-02-27-thariq-lessons-building-claude-code.md>)**

Der Action Space eines Agenten muss zu Modellfähigkeiten passen; kritische Formate gehören in robuste Interfaces und veraltete Hilfskonstrukte in regelmäßige Reviews. **Grenze:** Mehr Tools sind nicht automatisch besser; Todos, Tasks, Retrieval und Fragen-Interfaces sind vom tatsächlichen Modellverhalten abhängig. [Original](<https://x.com/trq212/status/2027463795355095314>)

**Q0114 · 2026-02-28 · [Codex Multi-Agent: Rollen, Limits und Sandbox-Vererbung](<../80_Knowledge/Sources/2026-02-28-openai-codex-multi-agents-guide.md>)**

Spezialisierte Multi-Agent-Rollen erlauben unabhängige Exploration und Reviews, während der Hauptagent Ergebnisse mit klaren Parallelitätsgrenzen konsolidiert. **Grenze:** Archivierte Codex-Rollen und Konfigurationswerte sind historischer Sekundärstand; Kontextentlastung des Hauptagenten ist keine automatische Senkung des Gesamtverbrauchs. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-28-openai-codex-multi-agents-guide.md>) · [Original](<https://developers.openai.com/codex/multi-agent/>)

**Q0115 · 2026-02-28 · [Codex Rules: technisch erzwungene Grenzen für Befehle außerhalb der Sandbox](<../80_Knowledge/Sources/2026-02-28-openai-codex-rules-guide.md>)**

Sicherheitsregeln müssen Befehle vor der Ausführung technisch prüfen und verpackte Shellketten berücksichtigen. **Grenze:** Allgemein erlaubte Shell-Wrapper und nicht zerlegbare Skripte bleiben ein Umgehungsrisiko; kein praktischer Robustheitstest. [Rohtext](<../00_Inbox/Quellen/URL/2026-02-28-openai-codex-rules-guide.md>) · [Original](<https://developers.openai.com/codex/rules>)


### 2026-03

**Q0116 · 2026-03-15 · [Kontextwechsel durch gespeicherten Arbeitsstand absichern](<../80_Knowledge/Sources/2026-03-15-julian-ivanov-ki-automat-claude-code-8-best-practices-fuer-bessere-ergebn.md>)**

Vor einem Kontextwechsel sollten Plan, Änderungen, Entscheidungen und nächster Schritt in Dateien gesichert und anschließend gezielt neu geladen werden. **Grenze:** Die 70-Prozent-Kompaktierung und pauschale CLI-Überlegenheit sind ungeprüfte Heuristiken; delegierte Aufgaben erhöhen oft den Gesamtaufwand. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-03-15-julian-ivanov-ki-automat-claude-code-8-best-practices-fuer-bessere-ergebn.md>) · [Original](<https://www.youtube.com/watch?v=9PFTLjuELs8>)

**Q0117 · 2026-03-17 · [cmux als Terminal-Oberfläche für mehrere parallele Coding Agents](<../80_Knowledge/Sources/2026-03-17-zerotopete-never-use-terminal-again.md>)**

Eine Workspace-Übersicht mit Branch, Pfad, Ports und Eingabebenachrichtigungen reduziert das Aufmerksamkeitsproblem bei mehreren laufenden Agenten. **Grenze:** Die cmux-Empfehlung betrifft macOS und einen Selbstbericht; Benachrichtigungen lösen weder Dateikonflikte noch Qualitätsprüfung. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-03-17-zerotopete-never-use-terminal-again.md>) · [Original](<https://www.tiktok.com/@zerotopete/video/7618333102263274766>)

**Q0118 · 2026-03-19 · [Erweiterungen nach Aufgabe auswählen und Ergebnisse kontrollieren](<../80_Knowledge/Sources/2026-03-19-julian-ivanov-ki-automat-die-10-besten-claude-code-skills-plugins.md>)**

Erweiterungen sollten nach konkretem Arbeitsschritt gewählt und ihre erzeugten Artefakte, Fehler sowie tatsächlicher Ergebnisumfang kontrolliert werden. **Grenze:** Der gezeigte Firecrawl-Lauf blieb durch Kontingentmangel unvollständig; Context7 und NotebookLM garantieren keine korrekten Antworten oder Ranglisten. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-03-19-julian-ivanov-ki-automat-die-10-besten-claude-code-skills-plugins.md>) · [Original](<https://www.youtube.com/watch?v=Vx6QlEhyybQ>)

**Q0119 · 2026-03-21 · [Obsidian-Vault plus MCP als persistentes Gedächtnis für Claude](<../80_Knowledge/Sources/2026-03-21-sourfraser-claude-obsidian-ai-employee.md>)**

Ein vernetzter Markdown-Vault kann Entscheidungen, Aufgaben und Gesprächszusammenfassungen als wiederauffindbaren Projektkontext erhalten. **Grenze:** Automatisches Lernen und der Nutzen über Wochen sind unbelegt; Schreibrechte, fehlerhafte Transkript-Extraktion und Datenflüsse bleiben eigene Risiken. [Rohtext](<../00_Inbox/Quellen/X/2026-03-21-sourfraser-claude-obsidian-ai-employee.md>) · [Original](<https://x.com/sourfraser/status/2035454870204100810>)

**Q0120 · 2026-03-26 · [GSD-Vergleich: Planungsartefakte und Übergaben bewusst auswählen](<../80_Knowledge/Sources/2026-03-26-alex-sprogis-gsd-framework-fuer-claude-code-version-1-2-im-pr.md>)**

GSD illustriert kleine kontextbegrenzte Aufgaben, persistente Planung und Boundary Maps, die Lieferungen und Abhängigkeiten zwischen Bauabschnitten festhalten. **Grenze:** Ein Incident-Prototyp und Dokumentanzahlen beweisen keine Produktionsreife; V1/V2-Kostenvergleich und Vertragsaussagen sind historisch und nicht kontrolliert. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-03-26-alex-sprogis-gsd-framework-fuer-claude-code-version-1-2-im-pr.md>) · [Original](<https://www.youtube.com/watch?v=dWXX0_gQujI>)

**Q0121 · 2026-03-29 · [Tokenverbrauch und Nutzungslimits](<../80_Knowledge/Sources/2026-03-29-0x-kaize-claude-usage-limits-primaer.md>)**

Lange Verläufe verursachen wiederholte Verarbeitung; gezielte Zusammenfassungen und gebündelte Fragen können unnötige Kontextkosten senken. **Grenze:** Die quadratische Formel setzt gleichmäßige Exchanges ohne Cacheeffekte voraus; Prozentwerte und Limitregeln sind historische Quellenaussagen. [Original](<https://x.com/0x_kaize/status/2038286026284667239>)

**Q0122 · 2026-03-29 · [Ein Wissensvault für Claude: von der Inbox zur wiederverwendbaren Entscheidung](<../80_Knowledge/Sources/2026-03-29-julian-ivanov-ki-automat-obsidian-claude-code-so-baust-du-dein-zweites-ge.md>)**

Eine Inbox mit regelmäßiger Zuordnung, Tageslogs und Weekly Review macht Wissen über Chats hinweg wiederverwendbar. **Grenze:** Lokale Markdown-Dateien garantieren keine lokale Datenverarbeitung; mehr Dateien oder Graphverbindungen beweisen keine Qualität. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-03-29-julian-ivanov-ki-automat-obsidian-claude-code-so-baust-du-dein-zweites-ge.md>) · [Original](<https://www.youtube.com/watch?v=NVUCQ-pzBn4>)


### 2026-04

**Q0123 · 2026-04-01 · [Paperclip: proaktive Agent-Arbeit braucht Grenzen und Ergebnisprüfung](<../80_Knowledge/Sources/2026-04-01-ai-mit-arnie-claude-code-und-paperclip-aendern-alles.md>)**

Eine Agentenorganisation braucht begrenzte Aufgaben und fachliche Ergebnisprüfung zusätzlich zu Mission, Rollen und Heartbeats. **Grenze:** Org-Chart, Status und Serverbetrieb beweisen weder funktionierende Firma noch sichere Rechte. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-04-01-ai-mit-arnie-claude-code-und-paperclip-aendern-alles.md>) · [Original](<https://www.youtube.com/watch?v=QFnxhbs-qv0>)

**Q0124 · 2026-04-03 · [Paperclip: Ziele, Rollen, Aufgaben und Budgets gemeinsam führen](<../80_Knowledge/Sources/2026-04-03-julian-ivanov-ki-automat-ich-habe-eine-firma-ohne-menschen-gebaut-papercl.md>)**

Eine dauerhafte Agentenorganisation verbindet Mission, Rollen, Issues, wiederkehrende Aufträge und Budgets über einzelne Coding-Sessions hinaus. **Grenze:** Paperclip-Demo belegt keine Firma ohne Menschen; Null API-Kosten im Dashboard verschweigen Abo und Betrieb, Heartbeat-Intervall allein definiert keine sinnvolle Arbeit. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-04-03-julian-ivanov-ki-automat-ich-habe-eine-firma-ohne-menschen-gebaut-papercl.md>) · [Original](<https://www.youtube.com/watch?v=Ebki7qT0QUw>)

**Q0125 · 2026-04-07 · [Subagents gezielt für Isolation, Parallelität und unabhängige Prüfung einsetzen](<../80_Knowledge/Sources/2026-04-07-claude-how-and-when-to-use-subagents-in-claude-code.md>)**

Subagents lohnen sich für isolierbare Recherche, unabhängige Teilaufgaben und frische Reviews mit explizitem Rückgabeformat. **Grenze:** Kleine oder stark gekoppelte Aufgaben und gemeinsame Dateiedits rechtfertigen Delegation oft nicht; angekündigte Codebeispiele fehlen im archivierten Text. [Rohtext](<../00_Inbox/Quellen/URL/2026-04-07-claude-how-and-when-to-use-subagents-in-claude-code.md>) · [Original](<https://claude.com/de/resources/articles/subagents-in-claude-code>)

**Q0126 · 2026-04-10 · [Agentenfreundliche Xcode-Projekte](<../80_Knowledge/Sources/2026-04-10-paulsolt-2042716870512353294.md>)**

Ein zuverlässiger gemeinsamer Build-, Run- und Test-Einstieg mit knappen parsebaren Fehlern hilft mehr als unstrukturierte Skill-Mengen. **Grenze:** Kuratierte Empfehlungen und Eigenwerbung, kein gemessener Nutzen; Produktfunktionen und Versionsangaben sind datiert. [Rohtext](<../00_Inbox/Quellen/X/2026-04-10-paulsolt-2042716870512353294.md>) · [Original](<https://x.com/PaulSolt/status/2042716870512353294>)

**Q0127 · 2026-04-12 · [Paperclip-Demo: Agentenrollen, Aufgaben, Budgets und Auslöser verbinden](<../80_Knowledge/Sources/2026-04-12-digitale-profis-so-ersetzt-du-dein-unternehmen-mit-ki-agenten-pa.md>)**

Rollen, Issues, Laufprotokolle, Budgets und bewusste Startgründe machen Mehragentenarbeit kontrollierbar. **Grenze:** Budgetanzeige und Vorwarnung beweisen keine harte Kostensperre; kostenlose Modelle sind zeitweilige Angebote. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-04-12-digitale-profis-so-ersetzt-du-dein-unternehmen-mit-ki-agenten-pa.md>) · [Original](<https://www.youtube.com/watch?v=lH228LTSlkI>)

**Q0128 · 2026-04-13 · [Superpowers: Tests aus Akzeptanzkriterien und getrennte Prüfrollen](<../80_Knowledge/Sources/2026-04-13-alex-sprogis-superkraefte-fuer-claude-code.md>)**

Superpowers verbindet Spezifikation und Akzeptanzkriterien mit Red–Green–Refactor sowie sequenziellen Spec- und Qualitätsreviews. **Grenze:** Die Demo überspringt Worktrees, hängt bei der Planung und erzeugt erfundene API-Endpunkte; eiserne Promptregeln sind keine technische Erzwingung. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-04-13-alex-sprogis-superkraefte-fuer-claude-code.md>) · [Original](<https://www.youtube.com/watch?v=91hD4U4e-Jc>)

**Q0129 · 2026-04-13 · [Wiki-Compiler zu „Eine gute AGENTS.md schreiben“](<../80_Knowledge/Sources/2026-04-13-wiki-compiler-gute-agents-md-schreiben.md>)**

Eine knappe Startdatei sollte Zweck, Navigation und Prüfwege liefern und Spezialwissen bei Bedarf referenzieren. **Grenze:** Der Wiki-Artikel ist eine abgeleitete Fassung bekannter HumanLayer-Inhalte. 

**Q0130 · 2026-04-13 · [Wiki-Compiler zu „The Shorthand Guide to Everything Claude Code“](<../80_Knowledge/Sources/2026-04-13-wiki-compiler-shorthand-guide-claude-code.md>)**

Erweiterungen sollten sparsam aktiviert und Subagentrechte eng begrenzt werden. **Grenze:** Eine umfangreiche Konfiguration ist kein Beleg für bessere Ergebnisse; abgeleiteter Wiki-Text. 

**Q0131 · 2026-04-15 · [Thariq zu „Using Claude Code: Session Management & 1M Context“ (Primärquelle)](<../80_Knowledge/Sources/2026-04-15-trq212-claude-code-session-management-1m-context-primaer.md>)**

Context Management wählt bewusst zwischen Fortsetzung, Rewind, Clear, Compact und Delegation, je nachdem welche Details die nächste Aufgabe benötigt. **Grenze:** Die 300–400k-Tokens-Heuristik für 1M-Fenster ist keine harte Grenze; kompakte Übergaben bleiben verlustbehaftet. [Original](<https://x.com/trq212/status/2044548257058328723>)

**Q0132 · 2026-04-16 · [Wiki-Compiler zu „Context7 für AI Coding Agents“](<../80_Knowledge/Sources/2026-04-16-wiki-compiler-context7.md>)**

Context7 ist ein versionsbezogener Dokumentations- und Retrieval-Layer neben Entwicklungsworkflows und sollte eindeutige Library-IDs verwenden. **Grenze:** Die interne Wiki-Synthese ersetzt weder Primärdokumentation noch Implementierungsprüfung; aktuelle Docs beseitigen Architektur- und Integrationsfehler nicht. 

**Q0133 · 2026-04-16 · [Wiki-Compiler zu „Everything Claude Code (ECC) für AI Coding Agents“](<../80_Knowledge/Sources/2026-04-16-wiki-compiler-everything-claude-code-ecc.md>)**

Breite Harness-Sammlungen benötigen Provenienz und Kuratierung, damit Vielfalt nicht zu Wartungsballast wird. **Grenze:** Historische README- und Arbeitsoberflächen zählen teilweise unterschiedlich; Zahlen sind kein Qualitätsmaß. 

**Q0134 · 2026-04-16 · [Wiki-Compiler zu „Get Shit Done (GSD) für AI Coding Agents“](<../80_Knowledge/Sources/2026-04-16-wiki-compiler-get-shit-done-gsd.md>)**

GSD kombiniert persistente Projektartefakte, Spezifikation, abhängigkeitssensitive Ausführungswellen und Verifikation über verschiedene Harnesses. **Grenze:** Die empfohlene Abschaltung von Permission-Rückfragen passt nicht automatisch zu den eigenen Freigabe- und Isolationsregeln. 

**Q0135 · 2026-04-16 · [gstack als Rollen- und QA-System](<../80_Knowledge/Sources/2026-04-16-wiki-compiler-gstack.md>)**

gstack verbindet Rollen-Workflows mit einem persistenten Browser zur praktischen UI-Verifikation. **Grenze:** Interne Sekundärsynthese mit Stand April 2026; Rollenmenge und Version sind kein aktueller Nachweis. 

**Q0136 · 2026-04-16 · [Wiki-Compiler zum „Skill Creator Skill für AI Coding Agents“](<../80_Knowledge/Sources/2026-04-16-wiki-compiler-skill-creator-skill.md>)**

Skills sollten über realistische Aufgaben mit und ohne Skill sowie über positive und negative Triggerfälle evaluiert werden. **Grenze:** Eine funktionsreiche Skill-Datei ist noch kein Nutzenbeleg; Metadaten, Body und Zusatzressourcen sollten bedarfsgerecht geladen werden. 

**Q0137 · 2026-04-16 · [Wiki-Compiler zu „UI UX Pro Max Skill für AI Coding Agents“](<../80_Knowledge/Sources/2026-04-16-wiki-compiler-ui-ux-pro-max-skill.md>)**

Ein Design-Intelligence-Layer kann Anforderungen in Stil, Tokens, Typografie und Anti-Patterns übersetzen. **Grenze:** Regelkonformität ersetzt weder Nutzerforschung noch spezifische Accessibility-Prüfung. 

**Q0138 · 2026-04-16 · [Wiki-Compiler zu „Vergleich von GSD, Superpowers, gstack und ECC – persönliche Learnings“](<../80_Knowledge/Sources/2026-04-16-wiki-compiler-vergleich-gsd-superpowers-gstack-ecc-learnings.md>)**

Frameworks sollten nach dem dominanten Problem gewählt werden: Artefakte, TDD-Disziplin, rollenbasierte QA oder Harness-Infrastruktur. **Grenze:** Die Aussagen sind persönliche Erfahrungen eines historischen Wiki-Artikels. 

**Q0139 · 2026-04-17 · [Wiki-Compiler zu „Agent Teams in Claude Code“](<../80_Knowledge/Sources/2026-04-17-wiki-compiler-agent-teams-in-claude-code.md>)**

Agent Teams lohnen sich bei echten unabhängigen Arbeitsflächen, kurzem gemeinsamen Kontext und klaren Verifikationssignalen. **Grenze:** Gemeinsam editierte Kernartefakte und überladene Startregeln multiplizieren Kosten. 

**Q0140 · 2026-04-17 · [Visueller Prototyp und lokaler Handoff](<../80_Knowledge/Sources/2026-04-17-wiki-compiler-codex-claude-code-lovable-workflow.md>)**

Ein visueller Prototyp kann Richtung und Kernabläufe klären, bevor ein lokaler Coding-Agent Backend, Tests und Betrieb ausarbeitet. **Grenze:** Interne Sekundärsynthese und produktspezifische Arbeitsteilung; kein universeller Toolvergleich. 

**Q0141 · 2026-04-17 · [Wiki-Compiler zu „Kontextsteuerung, Verifikation und TDD mit Claude Code“](<../80_Knowledge/Sources/2026-04-17-wiki-compiler-kontextsteuerung-verifikation-tdd.md>)**

Kontextmenge, Paketgröße und Prüfbarkeit wirken gemeinsam; vertikale TDD-Slices und öffentliche Verhaltensprüfungen begrenzen Scheinfortschritt. **Grenze:** Viele Mocks und interne Aufrufassertionen können Implementierungsdetails statt nützlichen Verhaltens bestätigen; Reviewtiefe soll zur Tragweite passen. 

**Q0142 · 2026-04-17 · [Wiki-Compiler zu „Lovable für Design, Debugging und Sicherheit“](<../80_Knowledge/Sources/2026-04-17-wiki-compiler-lovable-design-debugging-sicherheit.md>)**

Component-first-Design, projektweite Gestaltungsvorgaben und Root-Cause-Debugging ergänzen die serverseitige Absicherung generierter Webapps. **Grenze:** Die interne Synthese fügt keine unabhängigen Wirksamkeitsdaten hinzu; Security-Checker-Befunde müssen fachlich geprüft und erneut getestet werden. 

**Q0143 · 2026-04-17 · [Mock-first-Prototyping](<../80_Knowledge/Sources/2026-04-17-wiki-compiler-lovable-frontend-rapid-prototyping.md>)**

Ein Produktbrief mit Nutzern, wenigen Kernabläufen, Nichtzielen und synthetischen Beispieldaten schafft einen brauchbaren Prototyp-Scope. **Grenze:** Ein sehr langes Erstbriefing ist kein allgemeines Optimum; echte Authentifizierung und Datenhaltung benötigen eine eigene Umsetzung und Prüfung. 

**Q0144 · 2026-04-17 · [Wiki-Compiler zu „Praktische Claude-Code-Workflows für Planung, Ausführung und Review“](<../80_Knowledge/Sources/2026-04-17-wiki-compiler-praktische-claude-code-workflows.md>)**

Discovery, persistenter Plan, Annotation, Umsetzung und getrennter Review bilden einen nachvollziehbaren Entwicklungsablauf. **Grenze:** Die Wiki-Synthese fasst vorhandene Hersteller- und X-Quellen zusammen und ist keine neue unabhängige Messung. 

**Q0145 · 2026-04-17 · [Ralph Loop mit externem Zustand](<../80_Knowledge/Sources/2026-04-17-wiki-compiler-ralph-loop.md>)**

Frische Kontexte pro Iteration funktionieren nur, wenn Tasks, Spezifikation, Fortschritt und Prüfergebnisse dauerhaft außerhalb des Modells liegen. **Grenze:** Autonome Commits sind nur im jeweiligen Auftrag erlaubt; ungeklärtes Fachurteil und sicherheitskritische Architektur eignen sich schlecht für mechanische Loops. 

**Q0146 · 2026-04-17 · [Wiki-Compiler zu „Skills, Subagents, Hooks und MCP pragmatisch einsetzen“](<../80_Knowledge/Sources/2026-04-17-wiki-compiler-skills-subagents-hooks-mcp-pragmatisch.md>)**

Jede Anforderung sollte eine klare verantwortliche Erweiterungsebene erhalten. **Grenze:** Eine Anforderung auf mehreren Ebenen zu duplizieren erzeugt Konflikte; absichtliche technische Durchsetzung bleibt davon unterscheidbar. 

**Q0147 · 2026-04-20 · [Wiki-Compiler zu „Superpowers für AI Coding Agents“ (inkl. Sicherheits-/Vertrauensbewertung)](<../80_Knowledge/Sources/2026-04-16-wiki-compiler-superpowers.md>)**

Auch offen einsehbare Community-Plugins sind Drittcode, dessen Hooks, Commands und Agenten vor Einsatz und nach Updates geprüft werden müssen. **Grenze:** Die historische Sicherheitsbewertung ist keine Garantie für aktuelle Versionen; Popularität und Marketplace-Verfügbarkeit belegen keine Freigabe. 

**Q0148 · 2026-04-21 · [Karpathys Wiki als Memory: für Einzelne gut, für Teams begrenzt](<../80_Knowledge/Sources/2026-04-21-natebjones-this-is-so-important-if-you-use-ai-as-a-solo-business-or-ic-theres-a.md>)**

Wiki-Synthese für Verbindungsarbeit und Datenbanken für skalierbare, zitierbare Fakten lösen unterschiedliche Aufgaben. **Grenze:** Die zehntausend Dokumente als Grenze sind ungeprüft und der Autor bewirbt ein eigenes System. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-04-21-natebjones-this-is-so-important-if-you-use-ai-as-a-solo-business-or-ic-theres-a.md>) · [Original](<https://www.tiktok.com/@nate.b.jones/video/7631050279584009502>)

**Q0149 · 2026-04-22 · [Context Engineering als Baum: CLAUDE.md als Stamm](<../80_Knowledge/Sources/2026-04-22-agenticjames-everything-you-need-to-know-about-context-engineering-in-1-minute.md>)**

Eine Agentendatei kann als kurzer Einstieg über beschriebene Verweise zum passenden Fachkontext führen. **Grenze:** Verweise garantieren keinen korrekten Abruf; immer geladene Einstiegspunkte hängen vom Harness ab. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-04-22-agenticjames-everything-you-need-to-know-about-context-engineering-in-1-minute.md>) · [Original](<https://www.tiktok.com/@agentic.james/video/7631615421434596621>)

**Q0150 · 2026-04-22 · [Kleine offene Modelle und lokale Inferenz](<../80_Knowledge/Sources/2026-04-22-alibaba-qwen-qwen3-6-27b-lokal-betreiben.md>)**

Benchmarknähe eines kleineren offenen Modells sollte pro Aufgabe und unter gleichen Harness-Bedingungen beurteilt werden. **Grenze:** Herstellerchart und unbelegte Hardware-Richtwerte; der Titel verallgemeinert einzelne Siege zu stark und ist kein aktueller Kaufnachweis. [Rohtext](<../00_Inbox/Quellen/X/2026-04-22-alibaba-qwen-qwen3-6-27b-lokal-betreiben.md>) · [Original](<https://x.com/Alibaba_Qwen/status/2046939764428009914>)

**Q0151 · 2026-04-25 · [Validierung als Iterationsbedingung](<../00_Inbox/Quellen/TikTok/2026-04-25-agenticjames-if-youre-using-coding-agents-you-need-to-be-using-validation-and-testing.md>)**

Quantifizierbare Erfolgskriterien erlauben Agenten, Ergebnisse selbst zu prüfen und gezielt weiterzuarbeiten. **Grenze:** Allgemeiner Werbebeitrag ohne Messung; nicht jede Wissens- oder Designaufgabe lässt sich vollständig deterministisch abnehmen. [Original](<https://www.tiktok.com/@agentic.james/video/7632622837878115597>)

**Q0152 · 2026-04-29 · [Wiki-Compiler zu „Claude Code Session-Management mit 1M Context“](<../80_Knowledge/Sources/2026-04-29-wiki-compiler-claude-code-session-management-1m-context.md>)**

Nach jedem Arbeitsblock sollte bewusst zwischen Fortsetzen, Zurückspulen, Verdichten, Neustart und Delegation gewählt werden. **Grenze:** Dreihundert- bis vierhunderttausend Tokens sind eine historische Heuristik für ein bestimmtes Modell. 

**Q0153 · 2026-04-29 · [Wiki-Compiler zu „Claude Usage Limits mit Token-Strategien steuern“](<../80_Knowledge/Sources/2026-04-29-wiki-compiler-claude-usage-limits-token-strategien.md>)**

Lange unscharfe Gespräche können wiederholte Kontextverarbeitung verteuern und sollten in passende Arbeitsblöcke zerlegt werden. **Grenze:** Quadratisches Wachstum ist eine Näherung ohne Cache, Kompaktierung und variierende Nachrichtenlängen. 

**Q0154 · 2026-04-30 · [Secrets entlang aller Leckpfade schützen](<../80_Knowledge/Sources/2026-04-30-zodchiii-claude-code-env-security.md>)**

Anweisungen im Prompt ersetzen keine technischen Zugriffsbeschränkungen und keine Trennung produktiver Secrets von Tests. **Grenze:** Deny-Regeln schützen nur die tatsächlich erfassten Tools und Pfade; Shell- und indirekte Zugriffe benötigen eigene Grenzen. [Original](<https://x.com/zodchiii/status/2049779422291460576>)


### 2026-05

**Q0155 · 2026-05-01 · [Mnimiy (@Mnilax) zu „73% Overhead in Claude Code: 9 Patterns, die Tokens verbrennen“](<../80_Knowledge/Sources/2026-05-01-mnilax-claude-code-overhead-9-patterns.md>)**

Kontextgrundkosten aus Projektregeln, Hooks, MCP-Schemas und Sitzungshistorie sollten vor isolierter Modelloptimierung untersucht werden. **Grenze:** Dreiundsiebzig Prozent Overhead und Zielwerte sind ein einzelner ungeprüfter Audit; Cache-Warmhalten kann selbst Kosten verursachen. [Original](<https://x.com/Mnilax/status/2050261839653556522>)

**Q0156 · 2026-05-02 · [Pre-Mortem gegen Zustimmungsneigung](<../80_Knowledge/Sources/2026-05-02-vincentmumme-das-muesst-ihr-unbedingt-testen.md>)**

Ein Pre-Mortem fragt nach plausiblem Scheitern und Frühwarnsignalen, um eine Idee vor der Umsetzung kritisch zu prüfen. **Grenze:** Auch negative Szenarien kann ein Modell erfinden; der Prompt ist kein Nachweis tatsächlicher Eintrittswahrscheinlichkeiten. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-05-02-vincentmumme-das-muesst-ihr-unbedingt-testen.md>) · [Original](<https://www.tiktok.com/@vincentmumme/video/7635303149112266016>)

**Q0157 · 2026-05-04 · [Wiki-Compiler zu „Claude Session- und Token-Management für lange Agent-Arbeiten“](<../80_Knowledge/Sources/2026-05-04-wiki-compiler-claude-session-und-token-management.md>)**

Lange Agentenarbeit braucht klare Arbeitsblöcke mit gesichertem Handoff aus Ziel, Entscheidungen, Dateien, Tests und Risiken. **Grenze:** Continue als Default kann alte Fehlpfade fortschreiben; ein Reset hilft nur, wenn erforderliches Wissen vorher erhalten wurde. 

**Q0158 · 2026-05-09 · [Reasoning, Rechte und Budget bewusst konfigurieren](<../80_Knowledge/Sources/2026-05-09-zodchiii-15-claude-code-settings-most-developers.md>)**

Agentenqualität hängt auch von Reasoning-Budget, Zugriffsregeln, Kontextpflege, Arbeitskopien und begrenztem Fan-Out ab. **Grenze:** Historische Settings und teils vereinfachte Hook-Snippets dürfen nicht ungeprüft kopiert werden; stets hoher Effort ist keine allgemeine Kostenoptimierung. [Rohtext](<../00_Inbox/Quellen/X/2026-05-09-zodchiii-15-claude-code-settings-most-developers.md>) · [Original](<https://x.com/zodchiii/status/2053042131111927976>)

**Q0159 · 2026-05-13 · [Wie OpenAI Codex' Windows-Sandbox aus mehreren OS-Primitiven zusammensetzte](<../80_Knowledge/Sources/2026-05-13-david-wiesen-openai-codex-windows-sandbox.md>)**

Eine Sandbox für offene Entwicklerarbeit muss Dateirechte, Prozessidentität und Netzgrenzen aus mehreren tatsächlich durchsetzenden OS-Primitiven zusammensetzen. **Grenze:** Proxy-Variablen sind nur advisory; die beschriebene Windows-API-Sequenz ist historische sekundäre Herstellerdarstellung, hier kein Quellcode-Nachweis. [Rohtext](<../00_Inbox/Quellen/URL/2026-05-13-david-wiesen-openai-codex-windows-sandbox.md>) · [Original](<https://openai.com/index/building-codex-windows-sandbox/>)

**Q0160 · 2026-05-18 · [Goals mit prüfbaren Tasks verbinden](<../80_Knowledge/Sources/2026-05-18-agenticjames-using-goal-with-a-task-management-system-is-the-most-overpowered-way-to.md>)**

Ein langfristiges Ziel benötigt kleine persistente Tasks und eine explizite Abarbeitungs- und Prüfprozedur. **Grenze:** Tagelanger erfolgreicher Lauf wird nur behauptet; Taskzahl allein begrenzt weder Kosten noch Fehlerwiederholungen. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-05-18-agenticjames-using-goal-with-a-task-management-system-is-the-most-overpowered-way-to.md>) · [Original](<https://www.tiktok.com/@agentic.james/video/7641240809131609358>)

**Q0161 · 2026-05-21 · [Drift beobachten und verhindern](<../80_Knowledge/Sources/2026-05-21-christophmagnussen-ki-agenten-weichen-ab.md>)**

Agentenhierarchien brauchen vorab geklärte Entscheidungs- und Eskalationsregeln, weil Sichtbarkeit allein Zielabweichung nicht verhindert. **Grenze:** Die Quelle beschreibt das Problem, liefert aber keinen verifizierten Präventionsmechanismus; Reasoning-Spuren sind kein zuverlässiger Beweis. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-05-21-christophmagnussen-ki-agenten-weichen-ab.md>) · [Original](<https://www.tiktok.com/@christophmagnussen/video/7642335774192569632>)


### 2026-06

**Q0162 · 2026-06-02 · [Dynamic Workflows: Claude schreibt sich pro Aufgabe ein eigenes Harness](<../80_Knowledge/Sources/2026-06-02-trq212-2061907337154367865.md>)**

Dynamische Workflows kombinieren Routing, Fan-out, getrennte Verifikation, Turniere und begrenzte Loops passend zur Aufgabe. **Grenze:** Zusätzliche Agenten verbrauchen mehr Tokens; explizite Budgets, Abbruchkriterien und Quarantäne untrusted Inputs bleiben erforderlich. [Rohtext](<../00_Inbox/Quellen/X/2026-06-02-trq212-2061907337154367865.md>) · [Original](<https://x.com/trq212/status/2061907337154367865>)

**Q0163 · 2026-06-04 · [Drei ungenutzte Skill-Features in Claude Code: Fork-Kontext, Argumente, imperative Descriptions](<../80_Knowledge/Sources/2026-06-04-agenticjames-most-people-have-not-touched-the-best-parts-of-claude-code-skills-forked.md>)**

Ein isoliert laufender Skill mit passendem Modell und Parametern erlaubt eine aufgabenbezogene Ressourcenzuordnung. **Grenze:** Imperative Descriptions können auch Fehltrigger erzeugen; der Clip misst keine Triggerquote. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-06-04-agenticjames-most-people-have-not-touched-the-best-parts-of-claude-code-skills-forked.md>) · [Original](<https://www.tiktok.com/@agentic.james/video/7647517398890794253>)

**Q0164 · 2026-06-06 · [Dependency-Code gezielt als Referenz](<../80_Knowledge/Sources/2026-06-06-agenticjames-your-agent-is-referencing-documentation-when-it-should-be-reading-the.md>)**

Der tatsächlich eingesetzte Dependency-Quellcode kann Dokumentationslücken klären, wenn Version und relevanter Codepfad feststehen. **Grenze:** Vollimports vergrößern Suchraum und Pflegeaufwand; Code ist nicht automatisch die dokumentierte öffentliche API und ein Graph ist nicht nachweislich besser. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-06-06-agenticjames-your-agent-is-referencing-documentation-when-it-should-be-reading-the.md>) · [Original](<https://www.tiktok.com/@agentic.james/video/7648227434789195022>)

**Q0165 · 2026-06-07 · [Videoanalyse mit Transkript und Frames](<../80_Knowledge/Sources/2026-06-07-julian-ivanov-ki-automat-so-laesst-du-claude-jedes-video-fuer-dich-anscha.md>)**

Zeitmarkierte Transkripte und gezielt geprüfte Frames ergänzen sich bei Erklärvideos, stummen Abläufen und Bugaufnahmen. **Grenze:** Frame-Stichproben sind keine lückenlose Videosichtung; virale Erfolgsursachen, Servicepreise und Werbeaussagen bleiben unbewiesen. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-06-07-julian-ivanov-ki-automat-so-laesst-du-claude-jedes-video-fuer-dich-anscha.md>) · [Original](<https://www.youtube.com/watch?v=R403PGBArDY>)

**Q0166 · 2026-06-08 · [Loops mit Feedback und Stopps](<../80_Knowledge/Sources/2026-06-08-mvanhorn-2063865685558903149.md>)**

Agentenloops benötigen Verifikation, dauerhaften Zustand, eine Iterationsgrenze, Stillstandserkennung und ein Kostenlimit. **Grenze:** Die historische Stufenleiter ist eine Autorensynthese; zirkulierende Zahlen, Zitate und Produktfeatures sind nicht unabhängig geprüft. [Rohtext](<../00_Inbox/Quellen/X/2026-06-08-mvanhorn-2063865685558903149.md>) · [Original](<https://x.com/mvanhorn/status/2063865685558903149>)

**Q0167 · 2026-06-10 · [Aufgabenreife bestimmt Steuerung und Delegation](<../80_Knowledge/Sources/2026-06-10-ai-news-strategy-daily-n-codex-vs-claude-code-stop-picking-one-here-s-wha.md>)**

Unklare Arbeit wird zunächst gemeinsam geschärft; klar beschreibbare Aufgaben werden mit erlaubten Eingriffen und überprüfbaren Ergebnissen delegiert. **Grenze:** Die Zuordnung zu Claude und Codex ist subjektiv und historisch; Sandbox- und Produktvergleiche sind keine aktuelle technische Referenz. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-06-10-ai-news-strategy-daily-n-codex-vs-claude-code-stop-picking-one-here-s-wha.md>) · [Original](<https://www.youtube.com/watch?v=R2-Y1Hjwx2U>)

**Q0168 · 2026-06-16 · [Expertise und Arbeitsteilung in interaktiven Sessions](<../80_Knowledge/Sources/2026-09-17-anthropic-how-claude-code-is-used-in-practice.md>)**

Anthropics Untersuchung von rund 400.000 interaktiven Sessions verbindet aufgabenspezifische Expertise mit mehr Agentenaktionen pro Anweisung und höherer transkriptbasierter Erfolgsrate. **Grenze:** Herstellerstudie mit Modellklassifikatoren und selektierter Nutzung; Kurzvideo-Zahlen 30/29 stimmen nicht mit allen Primärbericht-Definitionen überein. [Rohtext](<../00_Inbox/Quellen/URL/2026-09-17-anthropic-how-claude-code-is-used-in-practice.md>) · [Original](<https://www.anthropic.com/research/claude-code-expertise>)

**Q0169 · 2026-06-18 · [Persönliches KI-Betriebssystem: Wissen, Tools, Skills und Routinen getrennt aufbauen](<../80_Knowledge/Sources/2026-06-18-julian-ivanov-ki-automat-bau-dir-dein-ki-betriebssystem-mit-claude-code-k.md>)**

Wissen, Vorgehensweisen, Toolverbindungen und Auslöser sollten als getrennte Bausteine eines persönlichen Agentensystems gepflegt werden. **Grenze:** Git ist keine konfliktfreie Synchronisation, tmux kein Wiederanlauf nach Serverneustart und private Ablage kein Beweis lokaler Verarbeitung. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-06-18-julian-ivanov-ki-automat-bau-dir-dein-ki-betriebssystem-mit-claude-code-k.md>) · [Original](<https://www.youtube.com/watch?v=k2p6WprtzFI>)

**Q0170 · 2026-06-23 · [Google liefert mit dem Open Knowledge Format eine (neue) Antwort, wie wir …](<../00_Inbox/Quellen/TikTok/2026-06-23-levanty_ch-google-liefert-mit-dem-open-knowledge-format-eine-neue-antwort-wie-wir.md>)**

Verlinkte Markdown-Dateien mit knappen Metadaten können menschlich bearbeitbares und agentisch auffindbares Firmenwissen strukturieren. **Grenze:** Die Google-Zuschreibung eines Open Knowledge Format ist hier ohne Spezifikation oder Primärbeleg und wird nicht als gesicherter Standard übernommen. [Original](<https://www.tiktok.com/@levanty_ch/video/7654489369960566038>)

**Q0171 · 2026-06-28 · [what loop would help you?](<../00_Inbox/Quellen/TikTok/2026-06-28-natebjones-what-loop-would-help-you.md>)**

Wiederkehrende kleine Informationsaufgaben lassen sich als begrenzte Loops bündeln, sofern Datenzugriff und erlaubte Aktionen geklärt sind. **Grenze:** Alltagsbeispiele sind Illustrationen; der Autor schließt Bankzugriff und selbstständige E-Mails ausdrücklich aus, ohne eine technische Lösung zu zeigen. [Original](<https://www.tiktok.com/@nate.b.jones/video/7656235405821480222>)

**Q0172 · 2026-06-29 · [KI-Einführung an konkretem Nutzen ausrichten](<../00_Inbox/Quellen/TikTok/2026-06-29-jousefmurad-wenn-ich-heute-ki-verantwortlicher-waere.md>)**

Wiederkehrende manuelle Datenarbeit, fachliche Verantwortliche und messbare Ergebnisse bilden einen pragmatischen Einstieg in KI-Nutzung. **Grenze:** Die behauptete Erfahrung aus 200 Projekten wird nicht belegt; generische Beratung ohne konkrete agentische Methode. [Original](<https://www.tiktok.com/@jousefmurad/video/7656735482495225110>)


### 2026-07

**Q0173 · 2026-07-01 · [Loop Engineering: Verifier, State und Stop-Bedingung als Mindestausstattung eines Agent-Loops](<../80_Knowledge/Sources/2026-07-01-0xcodila-2072329149520232639.md>)**

Ein nützlicher Agent-Loop benötigt unabhängigen Verifier, persistenten State und harte Stop-Bedingungen sowie eine geeignete reproduzierbare Aufgabe. **Grenze:** Autoresearch- und Bilevel-Zahlen sind unbestätigte Weitergaben; ein fünfmal größerer Metrikgewinn ist keine fünffache allgemeine Produktivität. [Rohtext](<../00_Inbox/Quellen/X/2026-07-01-0xcodila-2072329149520232639.md>) · [Original](<https://x.com/0xCodila/status/2072329149520232639>)

**Q0174 · 2026-07-01 · [Skills gegen Baseline evaluieren](<../80_Knowledge/Sources/2026-07-01-anthropic-skill-creator-skill-md.md>)**

Skill-Qualität wird über reale Aufgaben, Läufe mit und ohne Skill, quantitative Kosten und unabhängiges Feedback überprüfbar. **Grenze:** Die Source berichtet direkte Repo-Lektüre eines historischen Stands; das ist nicht automatisch ein aktueller Laufnachweis für jedes Script. [Original](<https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md>)

**Q0175 · 2026-07-01 · [State of Open Source AI 2026 (Mozilla): Der Harness ist die neue Frontier](<../00_Inbox/Quellen/URL/2026-07-01-mozilla-mit-slashdata-state-of-open-source-ai-2026.md>)**

Modellfähigkeit, betreibbare Infrastruktur, Memory und Rechte sind getrennte Voraussetzungen eines tragfähigen offenen Agentenstacks. **Grenze:** Die Fassung nennt Redaktionsstand Juni/Juli 1, behandelt aber spätere Juliereignisse; Chronologie und zahlreiche Zahlen müssen am Primär-PDF getrennt geprüft werden. Offene Gewichte beweisen weder Offenheit der Trainingsdaten noch sichere Autonomie. [Original](<https://stateofopensource.ai/state-of-open-source-ai-v1-0-1.pdf>)

**Q0176 · 2026-07-03 · [Loop Engineering als vierte Schicht über dem Harness](<../80_Knowledge/Sources/2026-07-03-calebwritescode-loop-engineering-explained-in-7-min-and-simplified.md>)**

Prompt, Kontext, Task-Harness und wiederkehrende Auslösung beschreiben verschiedene ineinanderliegende Schleifen mit jeweils eigenem Zustand. **Grenze:** Die Begriffsleiter ist keine Messung; der Creator bezeichnet praktischen Nutzen selbst als unbewiesen und verweist auf einen nicht selbst gelesenen Blog. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-07-03-calebwritescode-loop-engineering-explained-in-7-min-and-simplified.md>) · [Original](<https://www.tiktok.com/@calebwritescode/video/7658324465037675789>)

**Q0177 · 2026-07-03 · [Nachtläufe in isolierten Worktrees](<../80_Knowledge/Sources/2026-07-03-emanueledpt-2073013891752251574.md>)**

Parallele Nachtarbeit braucht getrennte Arbeitskopien, klare Aufträge und ein nachgelagertes Review-Gate. **Grenze:** Merge-ready wird nur behauptet; Kosten, Fehlerquote und morgendlicher Reviewaufwand fehlen. [Rohtext](<../00_Inbox/Quellen/X/2026-07-03-emanueledpt-2073013891752251574.md>) · [Original](<https://x.com/emanueledpt/status/2073013891752251574>)

**Q0178 · 2026-07-03 · [Nach jeder Aufgabe wiederverwendbares Wissen in die Knowledge Base überführen](<../80_Knowledge/Sources/2026-07-03-neilzegh-2072977540193378428.md>)**

Nach einer Aufgabe sollte geprüft werden, ob ein wiederverwendbares Werkzeug, Problemwissen oder Muster dauerhaft erhalten werden soll. **Grenze:** Ohne Qualitätsfilter wächst nur die Menge an Notizen. [Rohtext](<../00_Inbox/Quellen/X/2026-07-03-neilzegh-2072977540193378428.md>) · [Original](<https://x.com/neilzegh/status/2072977540193378428>)

**Q0179 · 2026-07-03 · [Unknowns finden: Thariqs Werkzeugkasten für Fable-Sessions, vor, während und nach der Implementierung](<../80_Knowledge/Sources/2026-07-03-trq212-2073100352921215386.md>)**

Blind-Spot-Pass, sichtbare Prototypen, Interviews und Referenzcode helfen, unausgesprochene Anforderungen vor und während der Umsetzung sichtbar zu machen. **Grenze:** Deviations-Logs erhalten konservative Planabweichungen; ein Quiz prüft menschliches Verständnis, nicht die Korrektheit der Implementierung. [Rohtext](<../00_Inbox/Quellen/X/2026-07-03-trq212-2073100352921215386.md>) · [Original](<https://x.com/trq212/status/2073100352921215386>)

**Q0180 · 2026-07-06 · [Ein Designsystem für Prototyp, Pitch, Landingpage und Animation](<../80_Knowledge/Sources/2026-07-06-alex-sprogis-claude-design-2-0-ist-der-wahnsinn-kompletter-gu.md>)**

Ein freigegebenes Designsystem kann Prototyp, Pitch, Landingpage und Animation gestalterisch verbinden und gezieltes Feedback an einzelnen Elementen ermöglichen. **Grenze:** Prototypdaten, Testimonials, simulierte Analysen und fiktive Pitch-Zahlen sind keine echten Unternehmensbelege; Handoff bleibt vor produktiver Implementierung. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-07-06-alex-sprogis-claude-design-2-0-ist-der-wahnsinn-kompletter-gu.md>) · [Original](<https://www.youtube.com/watch?v=KtK4cywgNUA>)

**Q0181 · 2026-07-06 · [Loop nach Trigger und Stoppbedingung wählen](<../80_Knowledge/Sources/2026-07-06-claudedevs-2074208949205881033.md>)**

Turn-, Goal-, zeit- und ereignisbasierte Loops lösen unterschiedliche Aufgaben und sollten nur bei tatsächlichem Bedarf eskaliert werden. **Grenze:** Herstellerleitfaden ohne Wirkungsmessung; ein Evaluatormodell kostet zusätzlich und kann selbst falsch urteilen. [Rohtext](<../00_Inbox/Quellen/X/2026-07-06-claudedevs-2074208949205881033.md>) · [Original](<https://x.com/ClaudeDevs/status/2074208949205881033>)

**Q0182 · 2026-07-06 · [Matt Pocock zu Skill-Writing-Prinzipien außerhalb von Skills](<../80_Knowledge/Sources/2026-07-06-mattpocock-writing-great-skills-beyond-skills.md>)**

Struktur, klare einleitende Signalwörter und Kürzung verbessern agentenlesbare Dokumente auch außerhalb eigentlicher Skills. **Grenze:** Kurze Autorenbeobachtung ohne Vergleichsmessung; die Prinzipien brauchen anwendungsbezogene Verifikation. 

**Q0183 · 2026-07-06 · [Dev-Server-Log in Datei spiegeln, damit Agents Laufzeitfehler sehen](<../80_Knowledge/Sources/2026-07-06-mattpocockuk-2074060484047712521.md>)**

Ein in eine Datei gespiegeltes Dev-Server-Log mit Zeiger in AGENTS.md erlaubt Laufzeitdiagnose ohne Übernahme des Serverprozesses. **Grenze:** Unbegrenzte Log-Lektüre kann Kontext verschwenden; gezielte Ausschnitte und Rotation sind sinnvolle ergänzende Maßnahmen. [Rohtext](<../00_Inbox/Quellen/X/2026-07-06-mattpocockuk-2074060484047712521.md>) · [Original](<https://x.com/mattpocockuk/status/2074060484047712521>)

**Q0184 · 2026-07-06 · [Nightmoon zu Wayfinder](<../80_Knowledge/Sources/2026-07-06-nightmoon-wayfinder.md>)**

Ein Nutzer erlebt Wayfinder als weniger koordinationsintensiv als eine manuell verkettete Skill-Pipeline. **Grenze:** Übersetzter Einzelbericht ohne Methode oder Messwerte. 

**Q0185 · 2026-07-08 · [Claude Code `/checkup` räumt Konfiguration und Kontext auf](<../80_Knowledge/Sources/2026-07-08-bcherny-2074997570317779038.md>)**

Konfigurationspflege kann ungenutzte Erweiterungen, doppelte Regeln und langsame Hooks als eigene Wartungsaufgabe behandeln. **Grenze:** Produktankündigung vom Juli, kein Einsparnachweis; Auto Mode bleibt eine gesonderte Rechteentscheidung. [Rohtext](<../00_Inbox/Quellen/X/2026-07-08-bcherny-2074997570317779038.md>) · [Original](<https://x.com/bcherny/status/2074997570317779038>)

**Q0186 · 2026-07-08 · [Model and effort in Claude Code: knowing more vs. trying harder](<../00_Inbox/Quellen/X/2026-07-08-claudedevs-2074900291062034618.md>)**

Modellwahl bestimmt Fähigkeit und Tokenpreis, Effort beeinflusst Gründlichkeit einschließlich Dateilektüre, Toolnutzung und Verifikation. **Grenze:** Zuerst Kontext und Fehlerbild prüfen; Effort ist kein harter Kostendeckel, Herstellervergleiche und konkrete Modellstufen sind datiert. [Original](<https://x.com/ClaudeDevs/status/2074900291062034618>) · Gleiche angegebene Herkunft: Q0188, Q0187.

**Q0187 · 2026-07-08 · [Modell und Effort in Claude Code: Wissen oder gründlicher arbeiten?](<../00_Inbox/Quellen/X/2026-07-08-claudedevs-claude-code-model-und-effort.md>)**

Fehlender Kontext, ausgelassene Arbeit und fachliche Fähigkeitsgrenzen erfordern unterschiedliche Korrekturen. **Grenze:** Effort ist kein festes Tokenbudget; die Kostenkurven im Text sind ausdrücklich illustrativ. [Original](<https://x.com/ClaudeDevs/status/2074900291062034618>) · Gleiche angegebene Herkunft: Q0188, Q0186.

**Q0188 · 2026-07-08 · [Input, Effort und Modell getrennt diagnostizieren](<../80_Knowledge/Sources/2026-07-08-claudedevs-modell-vs-effort.md>)**

Prüfe zuerst Scope und Kontext, erhöhe Effort bei übersprungener Arbeit und erwäge ein anderes Modell bei gründlich erarbeiteten Fehlschlüssen. **Grenze:** Die Kostenkurven sind illustrativ; Start-mit-Default unterscheidet sich von pauschalem Start-mit-dem-billigsten-Modell. [Original](<https://x.com/ClaudeDevs/status/2074900291062034618>) · Gleiche angegebene Herkunft: Q0186, Q0187.

**Q0189 · 2026-07-08 · [Matt Pocock zur Anbindung eigener Issue-Tracker](<../80_Knowledge/Sources/2026-07-08-mattpocock-custom-issue-tracker.md>)**

Workflowlogik und konkrete Issue-Tracker-Anbindung können getrennt werden. **Grenze:** Kompatibilität mit allem ist eine Autorenbehauptung ohne Testmatrix. 

**Q0190 · 2026-07-08 · [Matt Pocock zur Version 1.1 seiner Skills](<../80_Knowledge/Sources/2026-07-08-mattpocock-skills-v1-1.md>)**

Kleine komponierbare Skills können Exploration, Spec, Tickets, Implementierung und Review zu einem vollständigen Arbeitsablauf verbinden. **Grenze:** Versionsankündigung ohne Wirkungsvergleich; Commandnamen beschreiben den damaligen Stand. 

**Q0191 · 2026-07-09 · [Modelle nach Kosten pro erledigter Aufgabe vergleichen](<../80_Knowledge/Sources/2026-07-09-artificialanlys-2075268970492657905.md>)**

Modellvergleiche sollten Qualität, Reasoning-Stufe, Harness und tatsächliche Kosten pro Task gemeinsam betrachten. **Grenze:** Historische AA-Messung mit Vorabzugang durch OpenAI; Preisangaben und Rankings vom Juli 2026 sind kein aktueller Vergleich. [Rohtext](<../00_Inbox/Quellen/X/2026-07-09-artificialanlys-2075268970492657905.md>) · [Original](<https://x.com/ArtificialAnlys/status/2075268970492657905>)

**Q0192 · 2026-07-09 · [Claude (@claudeai)](<../00_Inbox/Quellen/X/2026-07-09-claudeai-2075225957711929667.md>)**

Ein monatlicher Nutzungsrückblick kann Arbeitszeiten und Themen sichtbar machen und Pausenhinweise anbieten. **Grenze:** Nutzungsintensität ist keine Produktivitätsmetrik. [Original](<https://x.com/claudeai/status/2075225957711929667>)

**Q0193 · 2026-07-09 · [GPT-5.6-Launch: Herstellerzahlen aus OpenAI-Charts, zusammengefasst von @kimmonismus](<../80_Knowledge/Sources/2026-07-09-kimmonismus-2075271465964798147.md>)**

Modellrankings benötigen die genaue Benchmarkauswahl, Konfiguration und Kostenbasis. **Grenze:** Herstellerauswahl und nicht nachgemessene Konkurrenzwerte erlauben keine allgemeine Überlegenheit. [Rohtext](<../00_Inbox/Quellen/X/2026-07-09-kimmonismus-2075271465964798147.md>) · [Original](<https://x.com/kimmonismus/status/2075271465964798147>)

**Q0194 · 2026-07-09 · [Will Ness zu Wayfinder](<../80_Knowledge/Sources/2026-07-09-n3sonline-wayfinder.md>)**

Goal–Task–Adjust erlaubt es, Recherche, Planung, Prototyp und Umsetzung nach dem jeweils nächsten Erkenntnisbedarf zu wählen. **Grenze:** Der Wayfinder-Erfahrungsbericht ist subjektiv; flexible Tasksteuerung widerspricht starren linearen Phasen nur bei ungeklärten Aufgaben. [Original](<https://x.com/N3sOnline/status/2075260831500312947>)

**Q0195 · 2026-07-09 · [Preisvergleich zum GPT-5.6-Start: Luna bei einem Dollar Input](<../80_Knowledge/Sources/2026-07-09-voxyz_ai-2075278546570801574.md>)**

Sinkende Tokenpreise können leistungsfähige Modelle für Routinearbeit zugänglicher machen, doch relevant bleiben Kosten pro erfolgreicher Aufgabe. **Grenze:** Unbestätigte Preise und ein Juli-Snapshot sind keine aktuelle Kaufentscheidung. [Rohtext](<../00_Inbox/Quellen/X/2026-07-09-voxyz_ai-2075278546570801574.md>) · [Original](<https://x.com/Voxyz_ai/status/2075278546570801574>)

**Q0196 · 2026-07-10 · [Preis-Leistungs-Charts begrenzen](<../80_Knowledge/Sources/2026-07-10-matthewberman-2075597710435266674.md>)**

Ein einzelner Benchmark mit unbekannter Methodik reicht nicht für die Aussage, ein Modell sei weltweit das beste Preis-Leistungs-Angebot. **Grenze:** Historisch abgelesene Chartwerte; keine unabhängige Bestätigung der Betreiber- oder Auswertungsmethodik. [Rohtext](<../00_Inbox/Quellen/X/2026-07-10-matthewberman-2075597710435266674.md>) · [Original](<https://x.com/MatthewBerman/status/2075597710435266674>)

**Q0197 · 2026-07-10 · [Coding Agent Index v1.1: Kleineres Modell mit mehr Effort schlägt oft die größere Stufe](<../80_Knowledge/Sources/2026-07-10-rasbt-2075573860796436626.md>)**

Der Vergleich von Modellgröße und Effort sollte Kosten je ausreichend gut gelöster Aufgabe statt allein den stärksten Benchmarkscore betrachten. **Grenze:** Raschkas Pareto-Faustregeln stammen aus einem konkreten Coding-Harness und abgelesener Grafik vom Juli 2026, nicht aus dem eigenen Workload. [Rohtext](<../00_Inbox/Quellen/X/2026-07-10-rasbt-2075573860796436626.md>) · [Original](<https://x.com/rasbt/status/2075573860796436626>)

**Q0198 · 2026-07-10 · [Kleine Skills und gemeinsame Fachsprache](<../80_Knowledge/Sources/2026-07-10-voxyz-mattpocock-skills.md>)**

Kleine komponierbare Skills adressieren konkrete Fehlermodi; ein Projektglossar und Handoffs verdichten wiederkehrenden Kontext. **Grenze:** Tweet über ein Repo statt Repo-Nachweis; genannte Starzahl war im Bestand bereits um Faktor zehn strittig. [Original](<https://x.com/Voxyz_ai/status/2075603005143924959>)

**Q0199 · 2026-07-11 · [Matt Pocock zum Übergang von Wayfinder zur Implementierung](<../80_Knowledge/Sources/2026-07-11-mattpocock-wayfinder-to-implementation.md>)**

Nach explorativer Wayfinder-Arbeit können Spec und Tickets den Übergang in eine getrennte autonome Implementierungsphase konkretisieren. **Grenze:** Für Nicht-Coding-Arbeit kann die flexible Exploration weitertragen; kein universeller Zwang zu allen Commands. 

**Q0200 · 2026-07-12 · [Setup-Pflege mit Sicherheitsfolgen](<../80_Knowledge/Sources/2026-07-12-agenticjames-claude-codes-new-feature-checkup-makes-claude-more-token-efficient-and.md>)**

Ungenutzte Erweiterungen, redundante Agent-Dateien und langsame Hooks sollten anhand tatsächlicher Nutzung geprüft werden. **Grenze:** Der checkup-Befehl und seine sieben Wirkungen sind ungeprüft; automatische Permission-Lockerung und Löschung selten genutzter Tools benötigen eigene Bewertung. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-07-12-agenticjames-claude-codes-new-feature-checkup-makes-claude-more-token-efficient-and.md>) · [Original](<https://www.tiktok.com/@agentic.james/video/7661714775629499662>)

**Q0201 · 2026-07-12 · [Matt Pocock (@mattpocockuk)](<../00_Inbox/Quellen/X/2026-07-12-mattpocockuk-2076373232295587865.md>)**

Bei fachlichen Verständnislücken kann ein gezielter Handoff an einen Lehragenten die Hauptplanung sauber halten und Lernen ermöglichen. **Grenze:** Die Quelle ist eine bereits anderweitig erfasste wortgleiche Dublette, keine unabhängige zweite Bestätigung. [Original](<https://x.com/mattpocockuk/status/2076373232295587865>)

**Q0202 · 2026-07-12 · [Mehrplattform-Recherche als Toolversprechen](<../00_Inbox/Quellen/X/2026-07-12-saboo_shubham-2076380344631398606.md>)**

Ein Recherche-Skill kann mehrere Plattformen bündeln, muss aber Ergebnisse und Quellen weiterhin nachvollziehbar liefern. **Grenze:** Werbepost ohne eigene Methode oder Messung; keine zusätzliche unabhängige Evidenz. [Original](<https://x.com/Saboo_Shubham_/status/2076380344631398606>)

**Q0203 · 2026-07-13 · [Wayfinder trennt Entscheidungen und Implementierung](<../80_Knowledge/Sources/2026-07-13-matt-pocock-live-the-wayfinder-demo.md>)**

Entscheidungstickets klären offene Fragen, bevor eine Spec in separat ausführbare Implementierungstickets übersetzt wird. **Grenze:** Die Live-Demo endet mit offener Entscheidung und zeigt Worktree-/Umgebungsprobleme; Prototypknöpfe belegen keine fertige Funktion. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-07-13-matt-pocock-live-the-wayfinder-demo.md>) · [Original](<https://www.youtube.com/watch?v=251hsWgoTPM>)

**Q0204 · 2026-07-13 · [Komponierbarer Coding-Lifecycle](<../00_Inbox/Quellen/URL/2026-07-13-matt-pocock-matt-pocock-skills-praxisguide.md>)**

Wähle den kleinsten passenden Ablauf: kurze Klärung für kleine Änderungen, Entscheidungskarte und Spec/Tickets für große unscharfe Vorhaben. **Grenze:** Sekundärguide und im Bestand bereits wortgleich vorhanden; Skill-Aufrufregeln und konkreter Funktionsstand sind paketabhängig. [Original](<https://github.com/mattpocock/skills>) · Gleiche angegebene Herkunft: Q0402.

**Q0205 · 2026-07-13 · [Matt Pocock zu Handoff und Teach bei Wissenslücken](<../80_Knowledge/Sources/2026-07-13-mattpocock-handoff-to-teach.md>)**

Eine Wissenslücke im Anforderungsinterview kann über ein Handoff in einen separaten Lernkontext ausgelagert werden. **Grenze:** Der Ablauf braucht eine belastbare Übergabe; ein separater Lernkontext garantiert kein Verständnis. 

**Q0206 · 2026-07-14 · [Fünf konfrontative Prompts für Entscheidungen: Interview, Pre-Mortem, Board Member](<../80_Knowledge/Sources/2026-07-14-fredrikharkort-5-prompts-die-weh-tun.md>)**

Interview, Pre-Mortem, Gegenfragen und radikale Verdichtung können Annahmen und Widersprüche einer Entscheidung sichtbar machen. **Grenze:** Konfrontativer Ton liefert ohne ausreichenden Geschäftskontext nur generische Kritik. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-07-14-fredrikharkort-5-prompts-die-weh-tun.md>) · [Original](<https://www.tiktok.com/@fredrikharkort/video/7662423861232717089>)

**Q0207 · 2026-07-14 · [KI-Dienste nach Edition, Vertrag und Datenfluss](<../80_Knowledge/Sources/2026-07-14-vischer-teil-31-ki-tools-wie-es-um-den-schutz-der-daten.md>)**

Die fachliche Prüfung eines KI-Dienstes muss konkrete Edition, Vertragsfamilie, Konfiguration, Zusatzfunktionen und Datenempfänger auseinanderhalten. **Grenze:** Datierte Autorenbewertung vom Juli 2026 mit Schweizer Rechtsbezug, teils ungeprüften Wettbewerberangaben und Eigenproduktwerbung; keine heutige Anbieter- oder Compliancefreigabe. [Rohtext](<../00_Inbox/Quellen/URL/2026-07-14-vischer-teil-31-ki-tools-wie-es-um-den-schutz-der-daten.md>) · [Original](<https://www.vischer.com/de/insights/teil-31-ki-tools-wie-es-um-den-schutz-der-daten-steht-2026>)

**Q0208 · 2026-07-15 · [Task-Vertrag statt langer Prompt: Lesart der GPT-5.6-Prompt-Guidance](<../80_Knowledge/Sources/2026-07-15-xudong07452910-2077246527756775933.md>)**

Ein klarer Task-Vertrag benennt Ziel, Erfolgskriterium, Pflichtbelege, Stoppregel und Aktionen mit Freigabebedarf. **Grenze:** Der chinesische Tweet interpretiert einen Hersteller-Guide; exakte Schritte bleiben bei fragilen Operationen unter Umständen sinnvoll. [Rohtext](<../00_Inbox/Quellen/X/2026-07-15-xudong07452910-2077246527756775933.md>) · [Original](<https://x.com/Xudong07452910/status/2077246527756775933>)

**Q0209 · 2026-07-16 · [Replit betreibt sich selbst mit Agents: Kennzahlen und Grenzen der „Self-Driving Company“](<../80_Knowledge/Sources/2026-07-16-amasad-2077802290304684404.md>)**

Unternehmensweite Agentennutzung verbindet gesicherte Infrastruktur, semantische Datenmodelle, risikobasierten Review und überprüfbare Arbeitsschleifen. **Grenze:** Alle Wirkungszahlen sind Anbieter-Selbstberichte; Codezeilen messen Volumen, nicht Kundennutzen, und Charts widersprechen teils der Zusammenfassung. [Rohtext](<../00_Inbox/Quellen/X/2026-07-16-amasad-2077802290304684404.md>) · [Original](<https://x.com/amasad/status/2077802290304684404>)

**Q0210 · 2026-07-16 · [Open-Weights-Ankündigungen von Verfügbarkeit trennen](<../80_Knowledge/Sources/2026-07-16-artificialanlys-2077832874183860404.md>)**

Ein angekündigter Gewichtsrelease ist noch kein verfügbares Open-Weights-Modell, und Parameterzahl sagt wenig über eigene Betriebskosten. **Grenze:** AA-Snapshot Juli 2026; Architektur- und Veröffentlichungspläne sind weitergegebene Anbieterangaben. [Rohtext](<../00_Inbox/Quellen/X/2026-07-16-artificialanlys-2077832874183860404.md>) · [Original](<https://x.com/ArtificialAnlys/status/2077832874183860404>)

**Q0211 · 2026-07-16 · [KI-Use-Cases brauchen Daten, Bedarf und Befähigung](<../80_Knowledge/Sources/2026-07-16-jousefmurad-es-gibt-eine-simple-regel-die-erklaert-warum-95-prozent-aller-ki.md>)**

KI-Use-Cases sollten verfügbaren Datenzugang, einen konkreten Bedarf und ausreichendes Umsetzungsverständnis gemeinsam prüfen. **Grenze:** Weder die 95-Prozent-Scheiterquote noch ein zwingender Data Lake oder synthetische Ersatzdaten sind belegt. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-07-16-jousefmurad-es-gibt-eine-simple-regel-die-erklaert-warum-95-prozent-aller-ki.md>) · [Original](<https://www.tiktok.com/@jousefmurad/video/7663144929610173718>)

**Q0212 · 2026-07-16 · [Kimi K3 auf Rang 1 der Frontend Code Arena](<../80_Knowledge/Sources/2026-07-16-kimmonismus-2077828228282982886.md>)**

Eine archivierte Arena-Rangfolge beschreibt Präferenzen unter einem bestimmten Bewertungsverfahren und Zeitpunkt. **Grenze:** Stichprobengröße und Konfidenzintervalle fehlen; nicht mit anderen Benchmarkskalen mischen. [Rohtext](<../00_Inbox/Quellen/X/2026-07-16-kimmonismus-2077828228282982886.md>) · [Original](<https://x.com/kimmonismus/status/2077828228282982886>)

**Q0213 · 2026-07-16 · [Codequalität als Agentenumgebung](<../80_Knowledge/Sources/2026-07-16-matt-pocock-do-software-fundamentals-still-matter.md>)**

Verständliche Module, kleine Schnittstellen und Tests an passenden Grenzen verbessern jede neue Agentensession. **Grenze:** Begründete Praxiseinschätzung ohne Vergleichstest; Gedächtnisgrenzen sind keine allgemeine technische Unmöglichkeit. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-07-16-matt-pocock-do-software-fundamentals-still-matter.md>) · [Original](<https://www.youtube.com/watch?v=eEjBhVI9Qok>)

**Q0214 · 2026-07-16 · [Interview, Spec, Tickets und Abschlussreview](<../80_Knowledge/Sources/2026-07-16-matt-pocock-mattpocock-skills-a-complete-ai-coding-workflow.md>)**

Ein gemeinsames Verständnis wird nur bei Bedarf in Spec und kleine Sitzungstickets überführt; Umsetzung und Abschlussprüfung nutzen frischen Kontext. **Grenze:** Das Tutorial zeigt auch eine unnötige Ticketaufteilung; konkrete Kontextschwellen und automatische Commits sind keine allgemeinen Regeln. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-07-16-matt-pocock-mattpocock-skills-a-complete-ai-coding-workflow.md>) · [Original](<https://www.youtube.com/watch?v=M6mYodf0dJM>)

**Q0215 · 2026-07-17 · [Organisationsadoption als offene Quelle](<../00_Inbox/Quellen/X/2026-07-17-bcherny-2077929379661844559.md>)**

Einzelne intensive KI-Nutzung im Unternehmen bedeutet noch keine breite organisatorische Adoption. **Grenze:** Die vier Schritte stehen nicht im lokalen Archiv; das verlinkte Artefakt darf nicht aus der Ankündigung rekonstruiert werden. [Original](<https://x.com/bcherny/status/2077929379661844559>)

**Q0216 · 2026-07-17 · [Preisindizes korrekt vergleichen](<../80_Knowledge/Sources/2026-07-17-hedgeye-2078165516657549710.md>)**

Preisverfall lässt sich nur mit geklärter Indexbasis, Warenkorb, Zeitraum und Qualitätsbereinigung sinnvoll vergleichen. **Grenze:** Die Faktor-fünf-Behauptung stammt aus einer weitergereichten Grafik; Rohdaten und Gewichtungen fehlen. [Rohtext](<../00_Inbox/Quellen/X/2026-07-17-hedgeye-2078165516657549710.md>) · [Original](<https://x.com/Hedgeye/status/2078165516657549710>)

**Q0217 · 2026-07-17 · [„Skill Hell“ durch ungezielte Prozesssammlung](<../80_Knowledge/Sources/2026-07-17-matt-pocock-framework-hell-tutorial-hell-now-skill-hell.md>)**

Skills sollten bewusst gewählte Arbeitsabläufe unterstützen statt mehrere ungeprüfte Frameworks gleichzeitig in den Kontext zu laden. **Grenze:** Keine sichere Skillanzahl oder gemessene Grenze wird genannt. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-07-17-matt-pocock-framework-hell-tutorial-hell-now-skill-hell.md>) · [Original](<https://www.youtube.com/watch?v=32LyZyFQhCQ>)

**Q0218 · 2026-07-17 · [Automatische Erinnerung kann lokale Präferenzen ungewollt verallgemeinern](<../80_Knowledge/Sources/2026-07-17-matt-pocock-kill-your-memory-md.md>)**

Bewusst gepflegte Projektvorgaben verhindern, dass automatisch gespeicherte situative Präferenzen unkontrolliert auf spätere Aufgaben wirken. **Grenze:** Pococks persönliche Präferenz gegen Auto-Memory ist kein Beleg gegen kuratiertes Quellenwissen und kein Auftrag zum Löschen bestehender Erinnerungen. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-07-17-matt-pocock-kill-your-memory-md.md>) · [Original](<https://www.youtube.com/watch?v=A0scuiiGBC4>)

**Q0219 · 2026-07-17 · [126-Seiten-Spezifikation plus Task-Markdown mit tausenden Einträgen](<../80_Knowledge/Sources/2026-07-17-promptgefluester-ich-werd-gerade-extrem-dafuer-kritisiert-dass-ich-an-meine-videos-gesagt.md>)**

Große Spezifikationen brauchen navigierbare Task-Referenzen, gesicherte Übergaben und überprüfbare Teilergebnisse, um ausführbar zu bleiben. **Grenze:** 126 Seiten, tausende To-dos und mehrstufige Audits sind Selbstberichte; Dokumentumfang beweist keine Vollständigkeit oder bessere Software. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-07-17-promptgefluester-ich-werd-gerade-extrem-dafuer-kritisiert-dass-ich-an-meine-videos-gesagt.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7663472940259888417>)

**Q0220 · 2026-07-17 · [Skills an tatsächlichen Sitzungsverläufen prüfen](<../80_Knowledge/Sources/2026-07-17-reach_vb-2078108681678299194.md>)**

Tatsächliche Sitzungsverläufe liefern realistische Fälle zur Überarbeitung eigener Workflow-Skills. **Grenze:** Historisches Verhalten ist kein Erfolgskriterium; Screenshot zeigt keinen abgeschlossenen Nutzenvergleich. [Rohtext](<../00_Inbox/Quellen/X/2026-07-17-reach_vb-2078108681678299194.md>) · [Original](<https://x.com/reach_vb/status/2078108681678299194>)

**Q0221 · 2026-07-20 · [Menschliche Kontrollpunkte nach Korrekturkosten](<../80_Knowledge/Sources/2026-07-20-matt-pocock-do-you-even-need-human-review.md>)**

Große unscharfe Aufgaben profitieren von früher Abstimmung; kleine leicht korrigierbare Aufgaben können mit späterer Prüfung auskommen. **Grenze:** Diff-Größe ist kein Risikomaß; auch wenige Zeilen können hohe Tragweite haben und keine bestehende Freigaberegel entfällt. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-07-20-matt-pocock-do-you-even-need-human-review.md>) · [Original](<https://www.youtube.com/watch?v=Yn8h5Ip-L9c>)

**Q0222 · 2026-07-21 · [Review-Autonomie braucht Risikostufen, Stichproben und Grenzen zwischen Agents](<../80_Knowledge/Sources/2026-07-21-claude-how-anthropic-secures-its-ai-native-software-dev.md>)**

Review-Autonomie braucht Risikostufen, Shadow Mode, überprüfbare Befunde, menschliche Stichproben und technisch begrenzte Agentenidentitäten. **Grenze:** Ein Incident-Agent versuchte über Slack einen stärkeren Agenten zum Push zu bewegen; Kommunikationswege gehören zur Berechtigungsgrenze, Herstellerkennzahlen sind nicht unabhängig validiert. [Rohtext](<../00_Inbox/Quellen/URL/2026-07-21-claude-how-anthropic-secures-its-ai-native-software-dev.md>) · [Original](<https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle>)

**Q0223 · 2026-07-21 · [Bedienungsabläufe als demonstrierte Skill-Vorlage erfassen](<../80_Knowledge/Sources/2026-07-21-claudeai-2079595988998554047.md>)**

Eine Bildschirmaufnahme mit begleitender Erklärung kann als Vorlage für einen wiederholbaren Skill dienen. **Grenze:** Aufnahmequalität und erzeugte Anweisungen brauchen unabhängige Prüfung. [Rohtext](<../00_Inbox/Quellen/X/2026-07-21-claudeai-2079595988998554047.md>) · [Original](<https://x.com/claudeai/status/2079595988998554047>)

**Q0224 · 2026-07-21 · [Große Sprachmigrationen mit überprüfbaren Agent-Schleifen](<../80_Knowledge/Sources/2026-07-21-claudedevs-2079654423828304282.md>)**

Große Sprachmigrationen benötigen validierte Verhaltensprüfer, Regel-Stresstests, Abhängigkeitskarten und zentrale teure Builds vor breiter Parallelisierung. **Grenze:** Trotz grüner vorhandener Bun-Tests traten laut Bericht 19 Regressionen nach Merge auf; Originalverhalten kann bekannte Fehler enthalten. [Rohtext](<../00_Inbox/Quellen/X/2026-07-21-claudedevs-2079654423828304282.md>) · [Original](<https://x.com/ClaudeDevs/status/2079654423828304282>)

**Q0225 · 2026-07-21 · [Prompt Engineering wird durch Frage-Skills und Hook-Skills ersetzt](<../80_Knowledge/Sources/2026-07-21-promptgefluester-prompt-engineering-ist-tot-und-keiner-hats-gemerkt-was-meine-ich-damit.md>)**

Rückfrage-Skills und bedarfsweise Regeln können fehlenden Kontext im Arbeitsprozess ergänzen. **Grenze:** Skills sind selbst Prompts; wiederholte Hooks kosten Kontext und ungezielte Sammlung erzeugt Konflikte. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-07-21-promptgefluester-prompt-engineering-ist-tot-und-keiner-hats-gemerkt-was-meine-ich-damit.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7664997418081062177>)

**Q0226 · 2026-07-22 · [Kontextwechsel bewusst auswählen](<../80_Knowledge/Sources/2026-07-22-mattpocockuk-2079879414297330146.md>)**

Weiterarbeit, Neustart, Handoff, Delegation und Verdichtung hängen davon ab, welcher Kontext noch gebraucht wird und wer weiterarbeitet. **Grenze:** Die Grafik ist ein diskutierter Praxisentwurf ohne universelle Token- oder Qualitätsgrenzen. [Rohtext](<../00_Inbox/Quellen/X/2026-07-22-mattpocockuk-2079879414297330146.md>) · [Original](<https://x.com/mattpocockuk/status/2079879414297330146>)

**Q0227 · 2026-07-22 · [OpenAI (@OpenAI)](<../00_Inbox/Quellen/X/2026-07-22-openai-2079916436232036614.md>)**

Presence wird als Unternehmensprodukt für Sprach- und Chatagenten mit erlaubten Aktionen und menschlicher Eskalation angekündigt. **Grenze:** Reine Produktankündigung ohne überprüfbaren Methodenbeitrag oder Nachweis aktueller Verfügbarkeit. [Original](<https://x.com/OpenAI/status/2079916436232036614>)

**Q0228 · 2026-07-23 · [Using/goal with a task management system is the most overpowered way to use …](<../00_Inbox/Quellen/TikTok/2026-07-23-agenticjames-using-goal-with-a-task-management-system-is-the-most-overpowered-way-to.md>)**

Ein länger laufendes Ziel lässt sich über persistente granulare Tasks und ein definiertes Iterationsverfahren steuern. **Grenze:** Tageweise Ausführung und erzwungene Zielerreichung sind Werbeversprechen; Aufgabenanzahl ersetzt keine Qualitäts-, Budget- oder Abbruchkontrolle. [Original](<https://www.tiktok.com/@agentic.james/video/7665513807250345229>)

**Q0229 · 2026-07-23 · [Rückfragen vor dem Projekt-Handoff](<../80_Knowledge/Sources/2026-07-23-ccarlosai-2080339591014261034.md>)**

Projektkontext sollte durch gezielte Rückfragen geschärft und danach in umsetzbare Plan- und Kontextdateien übersetzt werden. **Grenze:** Fünf Fragen sind kein Vollständigkeitsnachweis; zehnfache Beschleunigung ist unbelegt. [Rohtext](<../00_Inbox/Quellen/X/2026-07-23-ccarlosai-2080339591014261034.md>) · [Original](<https://x.com/ccarlosai/status/2080339591014261034>)

**Q0230 · 2026-07-23 · [Sichtbare Änderungen mit annotierten PR-Screenshots erklären](<../80_Knowledge/Sources/2026-07-23-colebemis-2080392348836790395.md>)**

Annotierte Screenshots können sichtbare Änderungen und betroffene Bereiche eines Pull Requests für Reviewer nachvollziehbar machen. **Grenze:** Das Bild ist ein Review-Artefakt und beweist weder vollständige Interaktionstests noch Produktionsabnahme. [Rohtext](<../00_Inbox/Quellen/X/2026-07-23-colebemis-2080392348836790395.md>) · [Original](<https://x.com/colebemis/status/2080392348836790395>)

**Q0231 · 2026-07-23 · [Agent-Änderungen per CLI mit einer menschlichen Live-Ansicht verbinden](<../80_Knowledge/Sources/2026-07-23-mattpocockuk-2080277204970143986.md>)**

Agentenbearbeitung per CLI und automatisch aktualisierte menschliche Ansicht können getrennt gestaltet werden. **Grenze:** Live-Ansicht beweist keine korrekte Interaktion und begründet keine uneingeschränkten Rechte. [Rohtext](<../00_Inbox/Quellen/X/2026-07-23-mattpocockuk-2080277204970143986.md>) · [Original](<https://x.com/mattpocockuk/status/2080277204970143986>)

**Q0232 · 2026-07-23 · [Mehrschichtiger Harness statt bloßer Sichtkontrolle](<../80_Knowledge/Sources/2026-07-23-unclebobmartin-2080257779395154409.md>)**

Unit-, Akzeptanz-, QA-, Coverage- und Mutationstests können gemeinsam Vertrauen in generierten Code aufbauen. **Grenze:** Der persönliche Verzicht auf Codelektüre ist ungemessen und steht in Spannung zu notwendigem Codepfadverständnis; grüne Tests beweisen nur abgedeckte Eigenschaften. [Rohtext](<../00_Inbox/Quellen/X/2026-07-23-unclebobmartin-2080257779395154409.md>) · [Original](<https://x.com/unclebobmartin/status/2080257779395154409>)

**Q0233 · 2026-07-24 · [Vier Reifegrade der KI-Coding-Nutzung: vom Pair Programming zur Agentenflotte](<../80_Knowledge/Sources/2026-07-24-agenticjames-the-creator-of-claude-code-released-a-guide-to-the-4-levels-of-ai-coding.md>)**

Ein Reifegradmodell kann Pair Programming, verifizierte Parallelität und bewusste Verbesserung der eigenen Agentenschleifen unterscheiden. **Grenze:** Die Zuschreibung an den Claude-Code-Erfinder ist unbelegt; Hunderte Agenten und Feature-Reviews sind kein nachgewiesener sicherer Endzustand. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-07-24-agenticjames-the-creator-of-claude-code-released-a-guide-to-the-4-levels-of-ai-coding.md>) · [Original](<https://www.tiktok.com/@agentic.james/video/7666102633823882510>)

**Q0234 · 2026-07-24 · [Effort nicht monoton mit Qualität gleichsetzen](<../80_Knowledge/Sources/2026-07-24-andrew_n_carr-2080727000004878593.md>)**

Höherer Reasoning-Effort kann in einer konkreten Evaluation schlechtere Ergebnisse bei höherem Aufwand liefern. **Grenze:** Weitergereichte FrontierCode-Grafik ohne Fallzahlen und Fehlerbalken; kein allgemeines Argument gegen Reasoning. [Rohtext](<../00_Inbox/Quellen/X/2026-07-24-andrew_n_carr-2080727000004878593.md>) · [Original](<https://x.com/andrew_n_carr/status/2080727000004878593>)

**Q0235 · 2026-07-24 · [Claude Opus 5: AA-Scores, Kosten und Halluzinationsgrenze](<../80_Knowledge/Sources/2026-07-24-artificialanlys-2080734447717298483.md>)**

Ein stärkerer Benchmarkscore kann zugleich mit höherer Halluzinationsneigung auftreten. **Grenze:** Historische Preise und unterschiedliche Skalen erlauben keine pauschale Modellrangliste. [Rohtext](<../00_Inbox/Quellen/X/2026-07-24-artificialanlys-2080734447717298483.md>) · [Original](<https://x.com/ArtificialAnlys/status/2080734447717298483>)

**Q0236 · 2026-07-24 · [Kontext nach Modellwechsel neu kalibrieren](<../80_Knowledge/Sources/2026-07-24-claude-the-new-rules-of-context-engineering-for-claude.md>)**

Neue Modellfähigkeiten können alte redundante oder widersprüchliche Anweisungen überflüssig machen; die Wirkung einer Vereinfachung muss geprüft werden. **Grenze:** 80 Prozent Kürzung ist Herstellerbericht für eigene Evals, keine universelle Kürzungsvorgabe; Sicherheitsgrenzen werden damit nicht aufgehoben. [Rohtext](<../00_Inbox/Quellen/URL/2026-07-24-claude-the-new-rules-of-context-engineering-for-claude.md>) · [Original](<https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/>)

**Q0237 · 2026-07-24 · [Opus 5 im Juli 2026: Modellleistung und Agent-Harness getrennt lesen](<../80_Knowledge/Sources/2026-07-24-kimmonismus-2080751641393836085.md>)**

Benchmark-Vergleiche benötigen denselben Indexstand, Effort, Fallback und Harness, bevor daraus eine Modellwahl abgeleitet wird. **Grenze:** Die 26 Prozent niedrigeren Aufgabenkosten stehen nur im Post; unterschiedliche Indexpunkte und ARC-Prozentwerte erlauben keine Gesamtrangfolge. [Rohtext](<../00_Inbox/Quellen/X/2026-07-24-kimmonismus-2080751641393836085.md>) · [Original](<https://x.com/kimmonismus/status/2080751641393836085>)

**Q0238 · 2026-07-24 · [Rollenprognosen als Hypothesen behandeln](<../00_Inbox/Quellen/TikTok/2026-07-24-niklas_volland-link-zur-kompletten-uebersicht-https-niklas-how-48-der-erfinder-von.md>)**

Prototyping, Umsetzung, Vereinfachung, Wachstum und Wartung sind unterschiedliche Tätigkeiten in einem Produktteam. **Grenze:** Zweithand-Prognose mit maschineller Rückübersetzung ohne Primärbeleg; keine belastbare Arbeitsmarktvorhersage. [Original](<https://www.tiktok.com/@niklas_volland/video/7666143066742459680>)

**Q0239 · 2026-07-24 · [The new rules of context engineering for Claude 5 models ](<../00_Inbox/Quellen/X/2026-07-24-trq212-2080710971228918066.md>)**

Stärkere Modelle können mit weniger redundanten Prozessregeln arbeiten, wenn Interfaces, lokale Gotchas und bedarfsgeladene Referenzen klar bleiben. **Grenze:** Die 80-Prozent-Kürzung ist eine herstellerinterne Coding-Eval-Aussage; Auto-Memory steht in Spannung zu bewusst zustandsloser Arbeit und harte Sicherheitsgrenzen bleiben nötig. [Original](<https://x.com/trq212/status/2080710971228918066>)

**Q0240 · 2026-07-24 · [Vox (@Voxyz_ai)](<../00_Inbox/Quellen/X/2026-07-24-voxyz_ai-2080760935455576540.md>)**

Kurze Projektregeln und aufgeteilte Skills sollen nur das Wissen tragen, das nicht bereits im Repository auffindbar ist. **Grenze:** Zusammenfassung desselben Thariq-Artikels wie Nr. 81, keine unabhängige Bestätigung der 80-Prozent-Behauptung. [Original](<https://x.com/Voxyz_ai/status/2080760935455576540>)

**Q0241 · 2026-07-25 · [Regeldateien gezielt verschlanken](<../80_Knowledge/Sources/2026-07-25-agenticjames-they-cut-claude-code-system-prompt-by-80-and-you-should-be-doing-the.md>)**

Bedarfsorientiert geladene Skills können dauerhaft vorgehaltene allgemeine Regeln reduzieren. **Grenze:** Keine eigenständige Messung; nicht benannte Papers und Sonnet-Opus-Gleichheit bleiben unbelegt und dieselbe Herstellerankündigung wird erneut verbreitet. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-07-25-agenticjames-they-cut-claude-code-system-prompt-by-80-and-you-should-be-doing-the.md>) · [Original](<https://www.tiktok.com/@agentic.james/video/7666509323413064974>)

**Q0242 · 2026-07-25 · [Mehr Reasoning bringt im Vals-Snapshot nicht automatisch mehr Treffer](<../80_Knowledge/Sources/2026-07-25-valsai-2080817011157094511.md>)**

Mehr Reasoning sollte anhand von Aufgabenqualität und Kosten gemessen werden, weil höchste Stufen keinen gesicherten zusätzlichen Nutzen zeigen müssen. **Grenze:** Vals meldet Unterschiede innerhalb der Fehlerbalken, die Grafik zeigt aber keine Intervalle oder Stichprobengröße; keine belastbare Rangfolge der Topstufen. [Rohtext](<../00_Inbox/Quellen/X/2026-07-25-valsai-2080817011157094511.md>) · [Original](<https://x.com/ValsAI/status/2080817011157094511>)

**Q0243 · 2026-07-26 · [Warum professionelles AI-Coding langsam ist: Quality Gates statt Vibe-Coding-Illusion](<../80_Knowledge/Sources/2026-07-26-promptgefluester-ich-hab-ne-unbequeme-wahrheit-und-zwar-ich-wurde-gefragt-wieso.md>)**

Bei komplexer Geschäftslogik brauchen Agentenänderungen deterministische Prüfungen, Impact-Betrachtung und gepflegte Verhaltenstests. **Grenze:** Halbstündige Gates und Fehler bei fast jeder Ausgabe sind Einzelberichte; die Unterstellung absichtlich fehlender Anbieter-Gates ist unbelegt. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-07-26-promptgefluester-ich-hab-ne-unbequeme-wahrheit-und-zwar-ich-wurde-gefragt-wieso.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7666715032855661857>)

**Q0244 · 2026-07-27 · [Open Weights: Risikothesen getrennt von Herstellerpositionen beurteilen](<../80_Knowledge/Sources/2026-07-27-anthropic-our-position-on-open-weights-models.md>)**

Offene Gewichte, Chipzugang, Distillation und Sicherheitstests sind unterschiedliche politische und technische Fragen. **Grenze:** Herstellerposition mit wirtschaftlichen Interessen, keine unabhängige Risikoanalyse oder Beschreibung geltenden Rechts. [Rohtext](<../00_Inbox/Quellen/URL/2026-07-27-anthropic-our-position-on-open-weights-models.md>) · [Original](<https://www.anthropic.com/news/position-open-weights-models>)

**Q0245 · 2026-07-27 · [Getting the most out of GPT-5.6: Sol, Terra, and Luna](<../00_Inbox/Quellen/X/2026-07-27-cerebras-2081828128952095022.md>)**

Modellstärke, Reasoning, Cacheverhalten und begrenzte Workerrollen sollten nach der Aufgabenklasse gewählt werden. **Grenze:** Hundertmillionen-Tokens-Sessions und Cache-Warmhalte-Automationen sind unbelegte Anbieterempfehlungen mit eigenen Kosten. [Original](<https://x.com/cerebras/status/2081828128952095022>) · Gleiche angegebene Herkunft: Q0246.

**Q0246 · 2026-07-27 · [Modellwahl und Reasoning-Stufen als Kostenhebel im Codex-Workflow](<../80_Knowledge/Sources/2026-07-27-cerebras-gpt-5-6-modellwahl-und-reasoning.md>)**

Modell- und Effort-Eskalation, gezielter Advisor gegen Drift und bewusste Cache-Nutzung sind getrennte Kostenhebel. **Grenze:** Warme Sessions können Cachekosten senken, aber Kontextqualität verschlechtern; historische TTL, Preisstaffeln und Millionen-Token-Kompaktierung sind keine aktuelle Zusage. [Original](<https://x.com/cerebras/status/2081828128952095022>) · Gleiche angegebene Herkunft: Q0245.

**Q0247 · 2026-07-27 · [Sprachabhängiger Token-Mehrverbrauch: Deutsch kostet bei Opus mehr als Englisch](<../80_Knowledge/Sources/2026-07-27-techfeed5-1-reason-why-the-cloud-limits-could-hit-directly-that-we-talk-to-opus-in.md>)**

Sprachabhängige Tokenisierung kann Kosten verändern und sollte am eigenen Text und Qualitätsziel gemessen werden. **Grenze:** Die Tabelle misst übersetzten literarischen Text und verdeckt deutsche Werte; daraus folgt weder eine konkrete deutsche Mehrkostenquote noch eine pauschale Englischpflicht. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-07-27-techfeed5-1-reason-why-the-cloud-limits-could-hit-directly-that-we-talk-to-opus-in.md>) · [Original](<https://www.tiktok.com/@techfeed5/video/7667084904622017825>)

**Q0248 · 2026-07-28 · [Mozilla-Bericht zu offener KI 2026: kleiner Modellabstand, Engpass im Harness](<../80_Knowledge/Sources/2026-07-28-pdf-state-of-open-source-ai-v1-0-1.md>)**

Der Bericht verortet wichtige Engpässe offener KI bei Betrieb, Harness, portablen Rechten und eigener Wissenshoheit statt allein bei Modellfähigkeit. **Grenze:** OpenRouter-Traffic repräsentiert nicht den Gesamtmarkt, Reifegradnoten sind Autorenurteile und offene Gewichte weder automatisch selbst betreibbar noch vollständig Open Source; Zahlen und politische Behauptungen sind datiert. [Rohtext](<../00_Inbox/Quellen/PDF/2026-07-28-pdf-state-of-open-source-ai-v1-0-1.md>)

**Q0249 · 2026-07-30 · [Browser- und Desktopintegration als Ankündigung](<../00_Inbox/Quellen/X/2026-07-30-chatgpt-2082970812584432115.md>)**

Kontext aus offenen Tabs, markiertem Text und Browserverlauf kann Assistenz näher an die aktuelle Arbeit bringen. **Grenze:** Keine Methode, Messung oder heutige Funktionsbestätigung; im Archiv als Ankündigung ignoriert. [Original](<https://x.com/ChatGPT/status/2082970812584432115>)

**Q0250 · 2026-07-30 · [Gefühlte Geschwindigkeit mit KI: Warum Kontext über Treffsicherheit entscheidet](<../80_Knowledge/Sources/2026-07-30-floknowsai-ki-gibt-dir-das-gefuehl-dass-du-so-schnell-wie-noch-nie-arbeitest.md>)**

Gefühlte Geschwindigkeit muss von gemessener Aufgabenzeit und Ergebnisqualität getrennt werden. **Grenze:** Studien werden nur sekundär zitiert; das Transkript ist eine maschinelle Rückübersetzung und keine zitierfähige Originaltonspur. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-07-30-floknowsai-ki-gibt-dir-das-gefuehl-dass-du-so-schnell-wie-noch-nie-arbeitest.md>) · [Original](<https://www.tiktok.com/@floknowsai/video/7668380261251419424>)

**Q0251 · 2026-07-30 · [Vom Briefing zur interaktiven Schulung in einer HTML-Datei](<../80_Knowledge/Sources/2026-07-30-julian-ivanov-interaktive-schulungen-mit-claude-code.md>)**

Eine interaktive Schulung sollte Zielgruppe und Lernziele klären, ein Curriculum prüfen lassen und erst danach aufwendige Medien produzieren. **Grenze:** Die Demo belegt keine Lernwirkung, Barrierefreiheit oder fachliche Richtigkeit; ein einzelnes HTML-Artefakt ersetzt keine Inhaltsabnahme. [Original](<https://www.youtube.com/watch?v=gz0PBC2P9eg>) · Gleiche angegebene Herkunft: Q0252.

**Q0252 · 2026-07-30 · [So erstellst du interaktive Schulungen mit Claude Code auf Knopfdruck](<../00_Inbox/Quellen/YouTube/2026-07-30-julian-ivanov-ki-automat-so-erstellst-du-interaktive-schulungen-mit-claud.md>)**

Interaktive Schulungen sollten erst nach Zielgruppenbriefing und Curriculumprüfung in Medien und Übungen umgesetzt werden. **Grenze:** Die Demo belegt keine Lernerfolgs- oder Compliance-Wirkung; Rechtsaussagen und Kostenangaben sind ungeprüfte historische Inhalte. [Original](<https://www.youtube.com/watch?v=gz0PBC2P9eg>) · Gleiche angegebene Herkunft: Q0251.

**Q0253 · 2026-07-30 · [Entscheidungskarten für mehrsitzige Planung](<../80_Knowledge/Sources/2026-07-30-matt-pocock-wayfinder-nothing-is-too-big-to-plan-anymore.md>)**

Eine Map aus Recherche-, Prototyp-, Interview- und Vorarbeitstickets erhält offene Entscheidungen samt ihren Abhängigkeiten über Sessions hinweg. **Grenze:** Der Autor hält Specs nach Umsetzung für entbehrlich; das steht in Spannung zu dauerhaft gepflegter Spezifikation und Governance. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-07-30-matt-pocock-wayfinder-nothing-is-too-big-to-plan-anymore.md>) · [Original](<https://www.youtube.com/watch?v=F3lL98Pj90o>)

**Q0254 · 2026-07-31 · [Discovery-Interview in eine prüfbare Spezifikation überführen](<../80_Knowledge/Sources/2026-07-31-alex-sprogis-dieser-claude-code-skill-ist-genial.md>)**

Ein fokussiertes Discovery-Interview liest vorhandene Projektinformationen, klärt eine Entscheidung nach der anderen und übersetzt Antworten in Akzeptanzkriterien. **Grenze:** Weniger Feedbackschleifen und Tokenersparnis sind nicht gemessen; Auswahloptionen benötigen teils zusätzliches Freitextfeedback. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-07-31-alex-sprogis-dieser-claude-code-skill-ist-genial.md>) · [Original](<https://www.youtube.com/watch?v=LYvSIAB4xxI>)

**Q0255 · 2026-07-31 · [Fehlende Zielinformationen durch Agent-Rückfragen aufdecken](<../80_Knowledge/Sources/2026-07-31-alexfinn-2082982462012227648.md>)**

Agentenrückfragen können fehlende Zielinformationen aufdecken und mögliche nächste Aufgaben sichtbar machen. **Grenze:** Hundertfache Wirkung und generelle Überlegenheit gegenüber Menschen sind unbelegte Zuspitzungen. [Rohtext](<../00_Inbox/Quellen/X/2026-07-31-alexfinn-2082982462012227648.md>) · [Original](<https://x.com/AlexFinn/status/2082982462012227648>)

**Q0256 · 2026-07-31 · [Tokenpreise und Aufgabenleistung getrennt halten](<../80_Knowledge/Sources/2026-07-31-kimmonismus-2083144340176609556.md>)**

Sehr niedrige Tokenpreise belegen noch keine niedrigen Gesamtkosten je korrekt erledigter Aufgabe. **Grenze:** Weitergereichter historischer Chart ohne Harness und Unsicherheiten; too cheap to meter ist Rhetorik. [Rohtext](<../00_Inbox/Quellen/X/2026-07-31-kimmonismus-2083144340176609556.md>) · [Original](<https://x.com/kimmonismus/status/2083144340176609556>)

**Q0257 · 2026-07-31 · [Lokales DeepSeek V4 Flash: Quantisierungsangaben widersprechen sich](<../80_Knowledge/Sources/2026-07-31-unslothai-2083231049434435596.md>)**

Quantisierungsformat, Dateigröße und tatsächlich benötigter Gesamtspeicher müssen getrennt bewertet werden. **Grenze:** Herstellerzahlen sind kein Hardwaretest und garantieren keine Anwendungsgleichheit. [Rohtext](<../00_Inbox/Quellen/X/2026-07-31-unslothai-2083231049434435596.md>) · [Original](<https://x.com/UnslothAI/status/2083231049434435596>)


### 2026-08

**Q0258 · 2026-08-01 · [Arena-Snapshot: starke Frontend-Wertung mit widersprüchlicher Preisachse](<../80_Knowledge/Sources/2026-08-01-arena-2083348755559207047.md>)**

Leistung pro Dollar braucht eine nachvollziehbare Kostenbasis und die genaue Frontend-Harness-Konfiguration. **Grenze:** Die Arena-Grafik nennt 0,25 USD gemischten Preis, die angegebenen Input-/Output-Preise ergeben bei 3:1 aber 0,175 USD; der Widerspruch bleibt offen. [Rohtext](<../00_Inbox/Quellen/X/2026-08-01-arena-2083348755559207047.md>) · [Original](<https://x.com/arena/status/2083348755559207047>)

**Q0259 · 2026-08-02 · [Statische Analyse vor breitem Refactoring](<../80_Knowledge/Sources/2026-08-02-promptgefluester-wenn-ihr-versucht-euer-software-projekt-mit-fable-five-oder-o-plus-5.md>)**

Deterministische Analyse und geklärte Architekturregeln können ein Refactoring vorbereiten, bevor große generative Änderungen beginnen. **Grenze:** Keine konkreten Tools oder Messdaten; statische Analyse findet nicht automatisch jede falsche Datenbanklogik und zehn Prozent sind nur ein Beispiel. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-08-02-promptgefluester-wenn-ihr-versucht-euer-software-projekt-mit-fable-five-oder-o-plus-5.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7669564638576594208>)

**Q0260 · 2026-08-03 · [Warum das Usage-Limit trotz fallender KI-Preise gleich schnell leer ist](<../80_Knowledge/Sources/2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso.md>)**

Fallende Preise für festgehaltene Fähigkeiten senken den Gesamtverbrauch nicht automatisch, wenn Sitzungen, Reasoning und parallele Agenten größer werden. **Grenze:** Caption und maschinelle Rückübersetzung weichen ab; genaue Preise, Tokenizer-Aufschläge und Subagent-Grundkosten sind historisch und nur teilweise belegt. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-08-03-floknowsai-die-preise-fuer-ki-fallen-wirklich-und-trotzdem-ist-dein-limit-genauso.md>) · [Original](<https://www.tiktok.com/@floknowsai/video/7669871035340033313>)

**Q0261 · 2026-08-03 · [Laufendes STATE.md statt Handover erst bei vollem Context Window](<../80_Knowledge/Sources/2026-08-03-steffen_hauptmann-die-meisten-lassen-sich-ein-handover-erst-schreiben-wenn-das.md>)**

Eine laufend gepflegte Zustandsdatei hält Fortschritt, offene Punkte und Learnings schon vor einer Kontextgrenze fest. **Grenze:** Veralteter Zustand kann irreführen; gleichzeitige Teamänderungen benötigen eigene Koordination. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-08-03-steffen_hauptmann-die-meisten-lassen-sich-ein-handover-erst-schreiben-wenn-das.md>) · [Original](<https://www.tiktok.com/@steffen_hauptmann/video/7669828414232136982>)

**Q0262 · 2026-08-04 · [Verifizierbare Agentenarbeit als Grundablauf](<../00_Inbox/Quellen/URL/2026-08-04-anthropic-best-practices-for-claude-code-claude-code-docs.md>)**

Erkunden, planen, umsetzen und prüfen bilden einen klaren Ablauf mit spezifischem Kontext und passenden Werkzeugen. **Grenze:** Archivierter Herstellerleitfaden ohne Leistungsmessung; Beispiel-Commits oder Auto-Mode ersetzen keine lokale Autorisierung. [Original](<https://www.anthropic.com/engineering/claude-code-best-practices>) · Gleiche angegebene Herkunft: Q0263.

**Q0263 · 2026-08-04 · [Anthropics aktuelle Best-Practices-Seite: Verifikation als vierstufige Eskalation](<../80_Knowledge/Sources/2026-08-04-anthropic-docs-claude-code-best-practices.md>)**

Promptprüfungen, Goal-Evaluator, deterministische Gates und frischer Gegenreview bieten unterschiedliche Stufen der Verifikation. **Grenze:** Ein Stop-Hook mit Override ist keine absolute Endesperre; auch technische Deny-Regeln wirken nur innerhalb ihres erfassten Kontrollpfads. [Original](<https://www.anthropic.com/engineering/claude-code-best-practices>) · Gleiche angegebene Herkunft: Q0262.

**Q0264 · 2026-08-05 · [Feedback direkt am Artefakt verankern](<../80_Knowledge/Sources/2026-08-05-creatoreconomy-use-my-human-review-skill-to-edit-html-and-markd.md>)**

Direkte Textänderungen und punktgenaue Kommentare im gerenderten Artefakt können Missverständnisse gegenüber reinem Chatfeedback reduzieren. **Grenze:** Werkzeugvorstellung des Autors ohne Wirksamkeitsmessung; Speichern und Anwenden unterscheiden sich je Dateityp. [Rohtext](<../00_Inbox/Quellen/URL/2026-08-05-creatoreconomy-use-my-human-review-skill-to-edit-html-and-markd.md>) · [Original](<https://creatoreconomy.so/p/use-my-human-review-skill-to-edit-html-markdown-visually>)

**Q0265 · 2026-08-05 · [Vibe-Coding scheitert am fehlenden Fundament, nicht am Agenten](<../80_Knowledge/Sources/2026-08-05-floknowsai-dein-vibe-coding-projekt-bricht-nicht-am-coding-agent-zusammen-sondern.md>)**

Vor produktiver Nutzung müssen Datenflüsse, Schnittstellen und Fehlerzustände explizit festgelegt und geprüft werden. **Grenze:** Neunundneunzig Prozent Scheitern und mindestens drei Monate Bauzeit sind unbelegte Fausturteile, keine Schätzung für dieses Projekt. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-08-05-floknowsai-dein-vibe-coding-projekt-bricht-nicht-am-coding-agent-zusammen-sondern.md>) · [Original](<https://www.tiktok.com/@floknowsai/video/7670597972576537888>)

**Q0266 · 2026-08-07 · [Agent-Datei als Navigationswurzel](<../00_Inbox/Quellen/TikTok/2026-08-07-agenticjames-most-people-think-context-engineering-is-some-complex-art.md>)**

Eine kurze Einstiegdatei kann zu Skills, Referenzen, Scripts und Werkzeugen führen, die erst für die konkrete Aufgabe geladen werden. **Grenze:** Inhaltliche Dublette eines älteren Videos; Auffindbarkeit garantiert keine korrekte Auswahl oder vollständige Kenntnis. [Original](<https://www.tiktok.com/@agentic.james/video/7671088367332838670>)

**Q0267 · 2026-08-07 · [Automatische Aktionsprüfung realistisch evaluieren](<../80_Knowledge/Sources/2026-08-07-claude-auto-mode-is-now-the-default-in-claude-code-for.md>)**

Aktionsclassifier sollten gegen tatsächlich ermüdete menschliche Freigaben und gegen unabhängige Angriffssätze geprüft werden. **Grenze:** Herstellerstudien und vorselektierte Sessions begrenzen die Aussage; null beobachtete Erfolge ist keine Sicherheitsgarantie, und Aktionsprüfung ersetzt keine Isolation. [Rohtext](<../00_Inbox/Quellen/URL/2026-08-07-claude-auto-mode-is-now-the-default-in-claude-code-for.md>) · [Original](<https://claude.com/de/resources/articles/auto-mode-default-in-claude-code>)

**Q0268 · 2026-08-07 · [Preisverfall benötigt belegte Ursachen](<../80_Knowledge/Sources/2026-08-07-theaicareercoach-vor-einem-jahr-noch-teuer-heute-fast-geschenkt-die-preise-fuer-ki.md>)**

Wettbewerb, Architektur- und Hardwareeffizienz sind plausible Treiber sinkender Modellpreise. **Grenze:** Creator-Erklärung ohne kausale Messung; Modellname im ASR teilweise unklar und Zahlen sind kein heutiges Preisangebot. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-08-07-theaicareercoach-vor-einem-jahr-noch-teuer-heute-fast-geschenkt-die-preise-fuer-ki.md>) · [Original](<https://www.tiktok.com/@the.ai.career.coach/video/7671162234608864544>)

**Q0269 · 2026-08-09 · [Skills nach Lernziel, Stil und Prüfaufgabe auswählen](<../80_Knowledge/Sources/2026-08-09-julian-ivanov-ki-automat-5-claude-code-skills-die-dir-wirklich-arbeit-abn.md>)**

Skill-Auswahl sollte konkrete Lern-, Schreib-, Gestaltungs- oder Prüfaufgaben mit nachvollziehbaren Rückmeldungen unterstützen. **Grenze:** Installationszahlen und Hersteller-Nutzung belegen weder Lernerfolg noch Security-Abdeckung; Stilbereinigung schafft keinen Faktennachweis und ersetzt keinen eigenen Schreibstil. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-08-09-julian-ivanov-ki-automat-5-claude-code-skills-die-dir-wirklich-arbeit-abn.md>) · [Original](<https://www.youtube.com/watch?v=dX0a9L4f_Lc>)

**Q0270 · 2026-08-09 · [Menschliche Entscheidungskapazität mitplanen](<../80_Knowledge/Sources/2026-08-09-natebjones-decision-exhaustion-is-real-discuss.md>)**

Viele parallele Agenten können menschliche Review- und Entscheidungslast verdichten, obwohl sie Ausführungsarbeit reduzieren. **Grenze:** Persönliche Beobachtung ohne Studie; pauschal nur noch schwere Entscheidungen ist überzeichnet. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-08-09-natebjones-decision-exhaustion-is-real-discuss.md>) · [Original](<https://www.tiktok.com/@nate.b.jones/video/7672185095662390558>)

**Q0271 · 2026-08-11 · [Du wirst gerade von KI abgehängt, weil jedes neue Modell die nächste Entwicklung beschleunigt.](<../00_Inbox/Quellen/TikTok/2026-08-11-floknowsai-du-wirst-gerade-von-ki-abgehaengt-weil-jedes-neue-modell-die-naechste.md>)**

Cloud-/Lokalmodelle, Kontext, RAG, Skills, Rechte und Loops bilden ein nützliches Orientierungsfeld für KI-Kompetenz. **Grenze:** Der Kurzclip zählt Begriffe auf, zeigt aber keine neue Methode oder belastbare Anwendung. [Original](<https://www.tiktok.com/@floknowsai/video/7672793569773505824>)

**Q0272 · 2026-08-12 · [Prognosen vorab operationalisieren](<../80_Knowledge/Sources/2026-08-12-kimmonismus-2087452378299564147.md>)**

Vorhersagen brauchen eine festgehaltene Aussage, Frist, messbares Erfolgskriterium und zulässige Datenquelle. **Grenze:** 19 von 24 AI-2027-Treffern ist eine ungeprüfte Trackerbewertung ohne vollständige Fallliste und Maßstab. [Rohtext](<../00_Inbox/Quellen/X/2026-08-12-kimmonismus-2087452378299564147.md>) · [Original](<https://x.com/kimmonismus/status/2087452378299564147>)

**Q0273 · 2026-08-12 · [Eine Kampagne als begrenzte Karte offener Entscheidungen führen](<../80_Knowledge/Sources/2026-08-12-shannholmberg-2087539757052285200.md>)**

Eine Kampagne lässt sich als begrenzte Karte offener Entscheidungen mit abhängigen Tickets, Recherche und günstigen Prototypen führen. **Grenze:** Eine ganze Strategie als Karte kann durch geänderte frühe Annahmen veralten; der Nutzen ist anekdotisch, kein Wirkungsnachweis. [Rohtext](<../00_Inbox/Quellen/X/2026-08-12-shannholmberg-2087539757052285200.md>) · [Original](<https://x.com/shannholmberg/status/2087539757052285200>)

**Q0274 · 2026-08-12 · [Nachtarbeit zunächst nur triagieren](<../80_Knowledge/Sources/2026-08-12-voxyz_ai-2087579867139264681.md>)**

Geeignete Nachtaufgaben müssen klar, isolierbar, reversibel und ohne laufende menschliche Entscheidungen ausführbar sein. **Grenze:** Reiner Prompt ohne Ergebnismessung; ungenutztes Kontingent ist kein Grund, Aufgaben zu erfinden. [Rohtext](<../00_Inbox/Quellen/X/2026-08-12-voxyz_ai-2087579867139264681.md>) · [Original](<https://x.com/Voxyz_ai/status/2087579867139264681>)

**Q0275 · 2026-08-13 · [OpenAI: höhere Plugin- und Skill-Nutzeranteile bei führenden Firmen](<../80_Knowledge/Sources/2026-08-13-openai-2087912623883051300.md>)**

Nutzeranteile für Plugins und Skills können Adoption sichtbar machen, müssen aber von tatsächlicher Workflowwirkung getrennt werden. **Grenze:** OpenAI vergleicht obere und mittlere zehn Prozent der Firmen, nicht Aufrufe pro Person; Korrelation belegt keine kausale Produktivität. [Rohtext](<../00_Inbox/Quellen/X/2026-08-13-openai-2087912623883051300.md>) · [Original](<https://x.com/OpenAI/status/2087912623883051300>)

**Q0276 · 2026-08-14 · [Memory nach Problem und Abrufzeitpunkt gestalten](<../80_Knowledge/Sources/2026-08-14-agenticjames-ai-memory-is-trash-heres-some-solutions.md>)**

Ablage von Wissen, Suche nach Gesprächsturns, multimodale Suche und Kontextinjektion lösen unterschiedliche Memory-Probleme. **Grenze:** Toolfähigkeiten sind unüberprüfte Empfehlungen mit Eigenwerbung; automatische Injektion kann irrelevanten oder veralteten Kontext einschleusen. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-08-14-agenticjames-ai-memory-is-trash-heres-some-solutions.md>) · [Original](<https://www.tiktok.com/@agentic.james/video/7674000398218284302>)

**Q0277 · 2026-08-14 · [Tokenkosten über Kontextlebensdauer verstehen](<../80_Knowledge/Sources/2026-08-14-claude-maximizing-the-value-of-your-claude-code-session.md>)**

Kosten hängen davon ab, wie viel Kontext entsteht, wie lange er mitgeführt wird und wie viele getrennte Kontexte laufen. **Grenze:** Konkrete Cachepreise, TTLs und Invalidierungsdetails sind Herstellerstand August 2026; Subagenten sparen nicht automatisch Gesamttokens. [Rohtext](<../00_Inbox/Quellen/URL/2026-08-14-claude-maximizing-the-value-of-your-claude-code-session.md>) · [Original](<https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions>)

**Q0278 · 2026-08-14 · [Auto mode startet als Default mit Rückfrage bei bestehender Einstellung](<../80_Knowledge/Sources/2026-08-14-claudedevs-2088332927189049738.md>)**

Permission-Defaults und bestehende Nutzereinstellungen sind explizite Konfigurationsentscheidungen neben technischen Zugriffsgrenzen. **Grenze:** Die Auto-Mode-Rolloutmeldung vom August 2026 bestätigt weder heutigen Umfang noch Sicherheitsleistung. [Rohtext](<../00_Inbox/Quellen/X/2026-08-14-claudedevs-2088332927189049738.md>) · [Original](<https://x.com/ClaudeDevs/status/2088332927189049738>)

**Q0279 · 2026-08-14 · [Frisches Review mit ursprünglichem Auftrag](<../80_Knowledge/Sources/2026-08-14-floknowsai-ueber-achtzig-prozent-des-codes-von-claude-code-und-codex-sieht-kein.md>)**

Ein getrennter Reviewkontext sollte Änderungen gegen ursprüngliche Anforderungen und ausführbare Qualitätsgates prüfen. **Grenze:** Zitierte PR-Studie und Prozentgewinne sind im Beitrag nicht primär belegt; die Source-Notiz behauptet noch fehlendes Transkript, obwohl der Rohstand inzwischen eines enthält. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-08-14-floknowsai-ueber-achtzig-prozent-des-codes-von-claude-code-und-codex-sieht-kein.md>) · [Original](<https://www.tiktok.com/@floknowsai/video/7673935893886979360>)

**Q0280 · 2026-08-14 · [Beobachtete Fehler in Reviewstandards überführen](<../80_Knowledge/Sources/2026-08-14-mattpocockuk-2088256432265167185.md>)**

Konkrete wiederkehrende Agentenfehler können in gepflegten Coding-Standards für spätere Reviews festgehalten werden. **Grenze:** Ein Agentenreview erzwingt Regeln nicht deterministisch; hunderte Standardzeilen benötigen Auswahl, Priorisierung und Pflege. [Rohtext](<../00_Inbox/Quellen/X/2026-08-14-mattpocockuk-2088256432265167185.md>) · [Original](<https://x.com/mattpocockuk/status/2088256432265167185>)

**Q0281 · 2026-08-15 · [Sechs Entscheidungen für einen belastbaren Agent-Harness](<../80_Knowledge/Sources/2026-08-15-undefinedki-2088611136027361368.md>)**

Ein Harness braucht bewusste Entscheidungen zu Loopende, Toolmenü, Kontext, Wiederaufnahme, Rechten und unabhängigem Abschlussnachweis. **Grenze:** Vier Zustandsdateien und wiederholte Evals sind konkrete Vorschläge; Primärbelege der Firmen-/Studienzahlen fehlen und mögliche Thread-Folgeposts bleiben offen. [Rohtext](<../00_Inbox/Quellen/X/2026-08-15-undefinedki-2088611136027361368.md>) · [Original](<https://x.com/undefinedKi/status/2088611136027361368>)

**Q0282 · 2026-08-16 · [Lokale Inferenz nach Speicher und Arbeitslast prüfen](<../80_Knowledge/Sources/2026-08-16-floknowsai-in-einem-jahr-ersetzt-ein-lokales-modell-dein-claude-abo.md>)**

Gewichte, Quantisierung, KV-Cache, Kontext und Speicherbandbreite bestimmen gemeinsam, ob ein lokales Modell praktisch nutzbar ist. **Grenze:** Parameter-mal-Bit und Bandbreitenformeln sind grobe Abschätzungen; Aboersatz in einem Jahr ist unbelegt und ein Index bleibt nur durch Aktualisierung frisch. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-08-16-floknowsai-in-einem-jahr-ersetzt-ein-lokales-modell-dein-claude-abo.md>) · [Original](<https://www.tiktok.com/@floknowsai/video/7674510846168419606>)

**Q0283 · 2026-08-18 · [MicroVM-Isolation als Betriebsmittel](<../80_Knowledge/Sources/2026-08-18-docker-2089789519788728379.md>)**

Ein eigener Kernel und Docker-Daemon können die Agentenlaufzeit stärker vom Host trennen. **Grenze:** Herstellerankündigung ohne eigene Prüfung der Dokumentation oder Konfiguration; harte Trennung ist keine pauschale Datenflussfreigabe. [Rohtext](<../00_Inbox/Quellen/X/2026-08-18-docker-2089789519788728379.md>) · [Original](<https://x.com/Docker/status/2089789519788728379>)

**Q0284 · 2026-08-18 · [Mutation Testing und ein zweiter Agent statt Code-Review](<../80_Knowledge/Sources/2026-08-18-floknowsai-hoer-auf-den-code-deines-ki-agenten-zu-lesen.md>)**

Mutationstests und ein frischer Prüfer können aufdecken, ob Tests tatsächliche Fehler erkennen, auch wenn Agent und Autor ihren Code nicht mehr vollständig lesen. **Grenze:** Die Aufforderung, keinen Code mehr zu lesen, ist eine zugespitzte Meinung; Fehlerquoten bleiben unbelegt und Mutationstests verursachen Laufzeit und prüfen nicht die fachliche Spezifikation. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-08-18-floknowsai-hoer-auf-den-code-deines-ki-agenten-zu-lesen.md>) · [Original](<https://www.tiktok.com/@floknowsai/video/7675431688024984865>)

**Q0285 · 2026-08-18 · [Agentischer SDLC als ungemessenes Organisationsversprechen](<../00_Inbox/Quellen/X/2026-08-18-limestonehq-2089711978914725979.md>)**

Ein agentischer Entwicklungsablauf verschiebt menschliche Arbeit zu Zielen und wichtigen Entscheidungen. **Grenze:** 98 Prozent und Wochen-zu-Tagen sind Marketing ohne Methodik; zwei menschliche Gates sind keine allgemeine sichere Vorgabe. [Original](<https://x.com/LimestoneHQ/status/2089711978914725979>)

**Q0286 · 2026-08-19 · [NVIDIA: Skill-Nutzen mit kontrollierten Vergleichsläufen messen](<../80_Knowledge/Sources/2026-08-19-developer-evaluating-ai-agent-skill-performance-with-nvidi.md>)**

Skillbewertung sollte Sicherheits- und Strukturchecks, Überschneidungssuche und kontrollierte Aufgabenläufe mit und ohne Skill verbinden. **Grenze:** Ein bis zwei Versuche pro Aufgabe und fehlende Konfidenzintervalle begrenzen Einzelwerte; aktivierungsbezogene Scores sind keine Passraten. [Rohtext](<../00_Inbox/Quellen/URL/2026-08-19-developer-evaluating-ai-agent-skill-performance-with-nvidi.md>) · [Original](<https://developer.nvidia.com/blog/evaluating-ai-agent-skill-performance-with-nvidia-skillevaluator/>)

**Q0287 · 2026-08-19 · [Expo-Animationen als Praxisangebot](<../00_Inbox/Quellen/X/2026-08-19-emilkowalski-2090031918523842766.md>)**

Die Ankündigung eines Expo-Kurses nennt Gesten, Sheets, Haptik und Übergänge als zusammenhängende Interaktionsarbeit. **Grenze:** Der kurze Werbepost enthält keine nachvollziehbare Methode oder Evaluation. [Original](<https://x.com/emilkowalski/status/2090031918523842766>)

**Q0288 · 2026-08-19 · [Personalisierte mRNA-Therapie: Phase-3-Meldung und Phase-2b-Zahlen trennen](<../80_Knowledge/Sources/2026-08-19-kimmonismus-2090082088087150979.md>)**

Studienphase, untersuchte Endpunkte und konkrete Effektgrößen müssen bei medizinischen KI-Meldungen getrennt bleiben. **Grenze:** Keine allgemeine Krebsheilung oder konkreter kausaler KI-Beitrag ist aus dem Tweet belegt; hier keine medizinische Empfehlung. [Rohtext](<../00_Inbox/Quellen/X/2026-08-19-kimmonismus-2090082088087150979.md>) · [Original](<https://x.com/kimmonismus/status/2090082088087150979>)

**Q0289 · 2026-08-19 · [Uncle Bob: Deterministische Checks statt Regeltexte für Agenten](<../80_Knowledge/Sources/2026-08-19-matt-pocock-live-uncle-bob-on-software-fundamentals-in-the-a.md>)**

Im Interview trennt Robert C. Martin unverzichtbare Entwurfs- und Qualitätsprinzipien von menschlichen Arbeitsritualen und beschreibt kleine Stories, modulare Architektur sowie getrennte Prüfrollen als seine aktuelle Agentenpraxis. **Grenze:** Der Erfahrungsbericht ist kein kontrollierter Vergleich: Martin lehnt starre Vorab-Spezifikation und strikt menschliches Zeilen-TDD ab, benötigt weiter menschliche Architekturentscheidungen und berichtet zusätzliche Laufzeit der Prüfkette. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-08-19-matt-pocock-live-uncle-bob-on-software-fundamentals-in-the-a.md>) · [Original](<https://www.youtube.com/watch?v=zcLPGC-tvgk>)

**Q0290 · 2026-08-19 · [Skills mit kontrollierter Baseline messen](<../00_Inbox/Quellen/X/2026-08-19-nvidiaai-2090113635683340622.md>)**

NVIDIA beschreibt einen Vergleich von mehr als 300 Skills bei gleichbleibender Aufgabe, Modell und Umgebung als Ansatz zur isolierten Wirkungsmessung. **Grenze:** Aggregierte Prozentpunkte dürfen nicht auf beliebige Skills und Aufgaben übertragen werden. [Original](<https://x.com/NVIDIAAI/status/2090113635683340622>)

**Q0291 · 2026-08-19 · [Private Safety Processing als Ankündigung](<../80_Knowledge/Sources/2026-08-19-openai-2090165328290701800.md>)**

OpenAI kündigt im August 2026 Private Safety Processing an, das sicherheitsrelevante Muster über zusammenhängende Interaktionen erkennen soll. **Grenze:** Der Post liefert keine ausreichenden Architektur- und Vertragsdetails für eine Datenschutzgarantie. [Rohtext](<../00_Inbox/Quellen/X/2026-08-19-openai-2090165328290701800.md>) · [Original](<https://x.com/OpenAI/status/2090165328290701800>)

**Q0292 · 2026-08-20 · [Netzwerkisolation als Antwort auf eine erwartete Schwachstellenwelle](<../80_Knowledge/Sources/2026-08-20-jasondclinton-2090543566682718542.md>)**

Netzwerkisolation kann als zusätzliche Schadensgrenze neben rechtzeitigem Patchen betrachtet werden. **Grenze:** Datierte Prognose ohne gemessene Angriffszahlen; verlinkte NSA-Quelle hier nicht eigenständig gelesen. [Rohtext](<../00_Inbox/Quellen/X/2026-08-20-jasondclinton-2090543566682718542.md>) · [Original](<https://x.com/JasonDClinton/status/2090543566682718542>)

**Q0293 · 2026-08-20 · [Große Vorhaben über Projektkarte und Entscheidungstickets planen](<../80_Knowledge/Sources/2026-08-20-latent-the-wayfinder-skill-navigating-the-fog-of-war-of.md>)**

Unklare Vorhaben lassen sich über eine gemeinsame Projektkarte und begrenzte Grilling-, Recherche-, Prototyp- oder Menschentickets entwickeln. **Grenze:** Das Interview erklärt das Design der Methode, misst aber keinen Vorteil gegenüber einfacher Planung. [Rohtext](<../00_Inbox/Quellen/URL/2026-08-20-latent-the-wayfinder-skill-navigating-the-fog-of-war-of.md>) · [Original](<https://www.latent.space/p/wayfinder-skill>)

**Q0294 · 2026-08-21 · [Brand Kit als lokale Referenz für Website, PDF und Thumbnail](<../80_Knowledge/Sources/2026-08-21-ai-mit-arnie-diese-skills-machen-claude-design-unfair.md>)**

Ein benannter Brand-Kit-Ordner kann gemeinsame Gestaltungsregeln für Website, PDF und Thumbnail bereitstellen. **Grenze:** Visuelle Konsistenz beweist weder richtige Inhalte, SEO noch Performance; pauschale Rechtsaussagen zur Kennzeichnung bleiben ungeprüft. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-08-21-ai-mit-arnie-diese-skills-machen-claude-design-unfair.md>) · [Original](<https://www.youtube.com/watch?v=2EoNRuFJfBo>)

**Q0295 · 2026-08-21 · [Hermes: Rollen, getrennte Kontexte und sichtbare Agentenaufgaben](<../80_Knowledge/Sources/2026-08-21-julian-ivanov-ki-automat-hermes-agent-kann-jetzt-viel-mehr-als-du-denkst.md>)**

Spezialisierte Agenten mit begrenztem Gedächtnis und sichtbaren Übergaben können Aufgaben aufteilen und menschliche Korrektur erleichtern. **Grenze:** Eigene Erinnerungen sind keine technische Isolation; Kanban und Botmodus waren laut Demo noch nicht direkt verknüpft. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-08-21-julian-ivanov-ki-automat-hermes-agent-kann-jetzt-viel-mehr-als-du-denkst.md>) · [Original](<https://www.youtube.com/watch?v=ScoibCUIpjk>)

**Q0296 · 2026-08-21 · [Wissensbasis als Markdown-Spezifikation: Der OKF-Linter als Steuerung für Agents](<../80_Knowledge/Sources/2026-08-21-openknowledge-open-knowledge-format-plugin-for-llm-wikis-openk.md>)**

Das Open Knowledge Format verbindet Markdown und Metadaten mit nachvollziehbarer Herkunft, Verifikationszustand und maschinenlesbaren Validierungsbefunden für ein gepflegtes Agenten-Wiki. **Grenze:** Herstellerankündigung zu Version 0.2: optionale Regeln und nicht blockierende MCP-Warnungen sind von CLI-Fehlschlägen zu unterscheiden; Standard-Markdown statt Wikilinks passt nicht unmittelbar zu jedem Obsidian-Bestand. [Rohtext](<../00_Inbox/Quellen/URL/2026-08-21-openknowledge-open-knowledge-format-plugin-for-llm-wikis-openk.md>) · [Original](<https://openknowledge.ai/blog/open-knowledge-format-okf-plugin-linter>)

**Q0297 · 2026-08-21 · [Agent Plugins: ein gemeinsames Paketformat für Skills und MCP-Server](<../80_Knowledge/Sources/2026-08-21-promptgefluester-agent-plug-ins-das-ist-der-neue-standard-mit-dem-die-grossen-ai.md>)**

Plugin-Manifeste können Skills und MCP-Anbindungen als Paket bündeln, ohne die darin beschriebenen Fähigkeiten oder ihre Qualität automatisch zu verbessern. **Grenze:** Der behauptete universelle Standard wird weder durch eine Spezifikation noch durch mehrere Implementierungen belegt; gezeigt wird vor allem eine ChatGPT-Oberfläche. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-08-21-promptgefluester-agent-plug-ins-das-ist-der-neue-standard-mit-dem-die-grossen-ai.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7676607306452176160>)

**Q0298 · 2026-08-21 · [Großes Refactoring stufenweise: Analyse, leicht vor schwer, Business-Logik-Doku](<../80_Knowledge/Sources/2026-08-21-promptgefluester-wie-macht-man-refactering-bei-einer-richtig-grossen-code-base-mit-aeh.md>)**

Ein großes Refactoring wird besser steuerbar, wenn zunächst Architektur und Tests analysiert und dann kleine Änderungen mit geringem Risiko vor schwierigeren Umbauten durchgeführt werden. **Grenze:** Der Rat enthält keinen gemessenen Projektvergleich; mitgeschriebene Geschäftslogik muss geprüft werden, damit Dokumentation keine falschen Annahmen festschreibt. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-08-21-promptgefluester-wie-macht-man-refactering-bei-einer-richtig-grossen-code-base-mit-aeh.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7676584233586003232>)

**Q0299 · 2026-08-22 · [Anthropic hat die Claude Academy veröffentlicht.](<../00_Inbox/Quellen/TikTok/2026-08-22-floknowsai-anthropic-hat-die-claude-academy-veroeffentlicht.md>)**

Rollen- und produktbezogene Lernangebote können Grundlagenwissen zugänglich machen. **Grenze:** Funktions- und Mengenangaben sind historisch; der Clip liefert keine eigene Lernwirksamkeitsstudie. [Original](<https://www.tiktok.com/@floknowsai/video/7676841192276888864>)

**Q0300 · 2026-08-22 · [Vorsicht bei Token-Spar-Tools: Kontext-Graphen schaffen eine zweite Wahrheit](<../80_Knowledge/Sources/2026-08-22-promptgefluester-wenn-euch-jemand-verspricht-token-zu-sparen-bei-cloud-code-dann-vorsicht.md>)**

Dauerhaft hilfreiche Kontextkompression setzt eine überprüfbare Aktualisierung des Index voraus, weil veraltete Graphen oder Dokumentation neben dem Code eine irreführende zweite Wahrheit bilden können. **Grenze:** Die pauschale Skepsis gegenüber Token-Sparwerkzeugen ist Meinung ohne Vergleichsmessung und widerlegt weder gepflegte Graphen noch aufgabenbezogene Retrieval-Systeme. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-08-22-promptgefluester-wenn-euch-jemand-verspricht-token-zu-sparen-bei-cloud-code-dann-vorsicht.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7676818527080271136>)

**Q0301 · 2026-08-25 · [Strenger Code-Review-Skill erzwingt Strukturvereinfachung](<../80_Knowledge/Sources/2026-08-25-vikingmute-2092059170812108811.md>)**

Strukturreview kann nach Vereinfachungen suchen, die ganze Verzweigungen, Helper und Sondermodi beseitigen. **Grenze:** Harte Zeilenlimits sind Heuristiken; überstrenger Review kann neue Schulden erzeugen. [Rohtext](<../00_Inbox/Quellen/X/2026-08-25-vikingmute-2092059170812108811.md>) · [Original](<https://x.com/vikingmute/status/2092059170812108811>)

**Q0302 · 2026-08-26 · [METR: Agentenverhalten unter benchmarkbedingten Fehlanreizen](<../80_Knowledge/Sources/2026-08-26-metr-brief-independent-investigation-of-agents-behavi.md>)**

Die METR-Untersuchung zeigt, wie Agenten in einer gemeinsamen Infrastruktur Ersatzwege, gegenseitige Bestätigung und teilweise Umgehungsversuche entwickeln, obwohl der eigentliche Auftrag unlösbar oder blockiert ist. **Grenze:** Der primäre Untersuchungsbericht beruht auf bereitgestellten, teils unvollständigen Daten, begrenztem Zugang und umfangreicher KI-Auswertung; gegenseitige Agentenzustimmung ist keine Nutzerautorisierung. [Rohtext](<../00_Inbox/Quellen/URL/2026-08-26-metr-brief-independent-investigation-of-agents-behavi.md>) · [Original](<https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/>)

**Q0303 · 2026-08-26 · [Hugging-Face-Vorfall: Kommunikationswege, Zielübernahme und Grenzen retrospektiver Sicherheitstests](<../80_Knowledge/Sources/2026-08-26-openai-der-vorfall-bei-hugging-face-und-der-weitere-weg.md>)**

Kommunikationswege und gemeinsam beschreibbare Artefakte gehören zu den Berechtigungsgrenzen eines Agentensystems. **Grenze:** Retrospektive Monitore mit Vorfallwissen sind kein prospektiver Schutzbeweis; Herstellerchronologie und vermutete Trainingsursachen bleiben unterscheidbar. [Rohtext](<../00_Inbox/Quellen/URL/2026-08-26-openai-der-vorfall-bei-hugging-face-und-der-weitere-weg.md>) · [Original](<https://openai.com/de-DE/index/hugging-face-incident-and-the-road-ahead/>)

**Q0304 · 2026-08-28 · [HuggingFace-Vorfall: Geteilte Dienste und manipulierbare Bewertung](<../80_Knowledge/Sources/2026-08-28-the-morpheus-der-huggingface-hack-ist-jetzt-untersucht.md>)**

Der kommentierte Hugging-Face-Vorfall zeigt, wie geteilte Infrastruktur, persistenter Agentenzustand, Rechteketten und manipulierbare Bewertung zusammen technische und organisatorische Schutzgrenzen unterlaufen können. **Grenze:** Automatisches Transkript und sekundäre Erklärung eines datierten Forschungsfalls: reduzierte Schutzmaßnahmen und ein internes Modell begrenzen die Übertragbarkeit; METR bestätigte nur einen abgegrenzten Untersuchungszeitraum unabhängig. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-08-28-the-morpheus-der-huggingface-hack-ist-jetzt-untersucht.md>) · [Original](<https://www.youtube.com/watch?v=T5H9nTE34CI>)

**Q0305 · 2026-08-30 · [Loop Engineering und Graph Engineering: Erfolgskriterien, unabhängige Prüfer und Artefakt-Übergaben](<../80_Knowledge/Sources/2026-08-30-alex-sprogis-loop-graph-engineering-das-letzte-video-was-du-s.md>)**

Zielgerichtete Agenten-Loops brauchen prüfbare Abschlusskriterien, begrenzte Wiederholungen, getrennte Verifikation und explizite Artefakte für Übergaben zwischen frischen Kontexten. **Grenze:** Die Dark Factory bleibt ein beworbenes Konzept ohne Implementierungsnachweis; frischer Kontext beseitigt Informationsverluste nicht vollständig, und eine umgedrehte Testerwartung beweist weniger als eine echte Mutation der geprüften Funktion. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-08-30-alex-sprogis-loop-graph-engineering-das-letzte-video-was-du-s.md>) · [Original](<https://www.youtube.com/watch?v=bKt-GZicIlM>)


### 2026-09

**Q0306 · 2026-09-01 · [Lokale Inferenz nach Arbeitslast dimensionieren](<../80_Knowledge/Sources/2026-09-01-ai-mit-arnie-lokale-ki-kauf-nicht-die-falsche-hardware.md>)**

Für lokale Inferenz sollten Aufgabe, Modell, Quantisierung, Kontext und Parallelität vor der Hardwareauswahl feststehen und mit repräsentativen Versuchen geprüft werden. **Grenze:** Automatische Untertitel, vermischte Flash-Attention- und Cache-Begriffe sowie unbelegte Preis-, Durchsatz- und Qualitätszahlen begrenzen die Hardwareempfehlungen. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-09-01-ai-mit-arnie-lokale-ki-kauf-nicht-die-falsche-hardware.md>) · [Original](<https://www.youtube.com/watch?v=DJhiTpQshX4>)

**Q0307 · 2026-09-04 · [Sprachdialog in bestehenden Codex-Chats](<../80_Knowledge/Sources/2026-09-04-guinnesschen-2095920936172335278.md>)**

Sprachdialog kann Architektur- und PR-Klärung im bestehenden Arbeitskontext unterstützen und anschließend in Agentenarbeit übergehen. **Grenze:** Interaktiver Dialog ist etwas anderes als Diktat; Produktivitätsgewinn wurde nicht gemessen. [Rohtext](<../00_Inbox/Quellen/X/2026-09-04-guinnesschen-2095920936172335278.md>) · [Original](<https://x.com/guinnesschen/status/2095920936172335278>)

**Q0308 · 2026-09-04 · [Audit-Aufruf ohne neue Methode](<../00_Inbox/Quellen/X/2026-09-04-joedevon-2095996826596024745.md>)**

Der Post empfiehlt ein Audit bestehender Skills und AGENTS.md anhand des Provencher-Artikels. **Grenze:** Weiterverbreitung ist kein unabhängiger Beleg. [Original](<https://x.com/joedevon/status/2095996826596024745>)

**Q0309 · 2026-09-04 · [Claude-Code-Setup regelmäßig prüfen](<../80_Knowledge/Sources/2026-09-04-julian-ivanov-ki-automat-so-nutzt-du-claude-code-nach-anthropics-neuen-re.md>)**

Absicht, Referenzen und überprüfbare Fertigstellung geben Agenten brauchbarere Orientierung als Rollenfloskeln und wachsende Anweisungslisten. **Grenze:** Video als Zweitquelle; Hooks garantieren nur die abgedeckte Ausführung und keine allgemeine Korrektheit oder vollständige Geheimnissperre. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-09-04-julian-ivanov-ki-automat-so-nutzt-du-claude-code-nach-anthropics-neuen-re.md>) · [Original](<https://www.youtube.com/watch?v=4v_XNgWTLiM>)

**Q0310 · 2026-09-04 · [Anweisungen modellabhängig ausdünnen](<../80_Knowledge/Sources/2026-09-04-pvncher-2095991462416490862.md>)**

Skills sollten knappe Auslöser und einen kleinen Router besitzen; projektspezifische Dokumente werden anlassbezogen statt vor jeder Änderung gelesen. **Grenze:** Selbstbericht ohne Evals; Lockerung kann andere Modelle im selben Repository verschlechtern. [Rohtext](<../00_Inbox/Quellen/X/2026-09-04-pvncher-2095991462416490862.md>) · [Original](<https://x.com/pvncher/status/2095991462416490862>)

**Q0311 · 2026-09-05 · [UX, DX und Agent Experience gemeinsam als Ziele benennen](<../80_Knowledge/Sources/2026-09-05-waynesutton-2096296858343846261.md>)**

UX, DX und Agent Experience gemeinsam zu nennen macht zusätzliche Entscheidungsziele sichtbar, ersetzt aber keine Priorisierung bei Zielkonflikten. **Grenze:** Der kurze Prompt liefert weder eine Gewichtung noch einen Regressionsnachweis; der Thread verweist auf bestehende Gedanken statt unabhängige Wirksamkeitsmessungen. [Rohtext](<../00_Inbox/Quellen/X/2026-09-05-waynesutton-2096296858343846261.md>) · [Original](<https://x.com/waynesutton/status/2096296858343846261>)

**Q0312 · 2026-09-06 · [KI-bezogene US-Beschäftigung relativ zum Einstellungstrend](<../80_Knowledge/Sources/2026-09-06-karl_lauterbach-2096616768974327822.md>)**

Beschäftigungsdifferenzen gegenüber einem erwarteten Branchenverlauf sind keine reine Zahl neu geschaffener KI-Jobs. **Grenze:** Keine Kausalität durch KI belegt und der zugrunde liegende Economist-Artikel wurde nicht vollständig geprüft. [Rohtext](<../00_Inbox/Quellen/X/2026-09-06-karl_lauterbach-2096616768974327822.md>) · [Original](<https://x.com/Karl_Lauterbach/status/2096616768974327822>)

**Q0313 · 2026-09-07 · [Prompting für GPT-6 Astra: Verhalten steuern statt Denkschritte vorgeben](<../80_Knowledge/Sources/2026-09-07-sairahul1-2096902575035683147.md>)**

Autonomie, Instruktionspriorität, Stil, Prüfmaß und Abschlussbedingungen sollten ausdrücklich und aufgabenbezogen definiert werden. **Grenze:** Modellspezifische Verhaltensbehauptungen sind ungemessen; viele angekündigte Copy-Paste-Prompts fehlen im Archivvolltext. [Rohtext](<../00_Inbox/Quellen/X/2026-09-07-sairahul1-2096902575035683147.md>) · [Original](<https://x.com/sairahul1/status/2096902575035683147>)

**Q0314 · 2026-09-09 · [Archify: Diagramme aus der Codebase statt von Hand](<../80_Knowledge/Sources/2026-09-09-alex-sprogis-so-erstellst-du-interaktive-architektur-diagramm.md>)**

Architektur, Datenfluss, Prozesse und Arbeitsabläufe benötigen unterschiedliche Diagrammperspektiven mit nachvollziehbaren Codebezügen. **Grenze:** Ein gut gerendertes Diagramm beweist keine korrekt aus dem Code abgeleiteten Beziehungen; Sponsor-Rechtsaussagen nicht übernehmen. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-09-09-alex-sprogis-so-erstellst-du-interaktive-architektur-diagramm.md>) · [Original](<https://www.youtube.com/watch?v=YE40EDb1kRk>)

**Q0315 · 2026-09-09 · [Kontrollverlust durch KI: Forscherwarnungen und das Gegenargument defensiver KI](<../80_Knowledge/Sources/2026-09-09-orf-anthropic-forscher-ki-risiko-fuer-menschen.md>)**

Persönliche Risikoeinschätzungen und die Forderung nach defensiver KI-Forschung müssen von gemessenen Wahrscheinlichkeiten getrennt werden. **Grenze:** Keine konkrete Schutzarchitektur, kein eingetretener Angriff und keine empirische Herleitung der genannten Wahrscheinlichkeit. [Rohtext](<../00_Inbox/Quellen/URL/2026-09-09-orf-anthropic-forscher-ki-risiko-fuer-menschen.md>) · [Original](<https://orf.at/stories/3441651/>)

**Q0316 · 2026-09-09 · [Kostengünstiger Codex-Agent-Tree mit Effort-Stufen pro Rolle](<../80_Knowledge/Sources/2026-09-09-voxyz_ai-2097814698204832116.md>)**

Rollenbezogene Modell- und Effort-Konfiguration lässt sich erst anhand tatsächlich gestarteter Subagent-Sitzungen verifizieren; eine Rollenanweisung im Chat schaltet kein Modell um. **Grenze:** Der Kostenvorteil des Astra-Luna-Sol-Baums ist selbstberichtet und die genannten DeepSWE-Zahlen fehlen; kleine Aufgaben können ohne Delegationsaufwand wirtschaftlicher sein. [Rohtext](<../00_Inbox/Quellen/X/2026-09-09-voxyz_ai-2097814698204832116.md>) · [Original](<https://x.com/Voxyz_ai/status/2097814698204832116>)

**Q0317 · 2026-09-10 · [Arbeitsumgebung und Prüfmittel vor dem Programmieren klären](<../80_Knowledge/Sources/2026-09-10-promptgefluester-einer-der-groessten-fehler-den-ich-bei-vielen-vibe-codern-mit-ki.md>)**

Entwicklungsumgebung, Wiederverwendung, Designvorgaben und Prüfmittel sollten vor der Umsetzung bewusst gewählt werden. **Grenze:** Vorbereitung rechtfertigt keinen unbegrenzten Hilfswerkzeugbau; Scheiterquoten sind unbelegte Verallgemeinerungen. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-09-10-promptgefluester-einer-der-groessten-fehler-den-ich-bei-vielen-vibe-codern-mit-ki.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7683800524918918432>)

**Q0318 · 2026-09-12 · [Externe Evaluatoren sollen Sicherheitszusagen überprüfbar machen](<../80_Knowledge/Sources/2026-09-12-darioamodei-2098773920774074715.md>)**

Externe Evaluation wird erst durch dauerhaften Einblick und unabhängig veröffentlichbare Befunde nachvollziehbar. **Grenze:** Ankündigung ist keine nachgewiesene Umsetzung oder Wirksamkeit; Herstellerinteressen bleiben sichtbar. [Rohtext](<../00_Inbox/Quellen/X/2026-09-12-darioamodei-2098773920774074715.md>) · [Original](<https://x.com/DarioAmodei/status/2098773920774074715>)

**Q0319 · 2026-09-13 · [Domänenwissen als Agentenhebel](<../80_Knowledge/Sources/2026-09-13-stefanantonelli-du-brauchst-keinen-entwickler-um-mit-ki-etwas-zu-bauen.md>)**

Die Quelle betont Domänenwissen als Grundlage brauchbarer Ziele und Qualitätskriterien auch außerhalb der Softwareentwicklung. **Grenze:** Werbevideo und automatische Transkription; Source-Notiz beschreibt einen älteren Stand ohne mittlerweile vorhandenes Transkript. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-09-13-stefanantonelli-du-brauchst-keinen-entwickler-um-mit-ki-etwas-zu-bauen.md>) · [Original](<https://www.tiktok.com/@stefan.antonelli/video/7685007734546107670>)

**Q0320 · 2026-09-14 · [Agent Arena: Aufgabenleistung und Aufgabenpreis gemeinsam vergleichen](<../80_Knowledge/Sources/2026-09-14-arena-2099606881845321841.md>)**

Eine Pareto-Grenze beschreibt die Kosten-Leistungs-Alternativen innerhalb eines konkreten Aufgabenmixes. **Grenze:** Rundungen von 0,06, 0,065 und 0,07 Dollar bleiben im Archiv uneinheitlich; Stichprobe und Unsicherheit fehlen. [Rohtext](<../00_Inbox/Quellen/X/2026-09-14-arena-2099606881845321841.md>) · [Original](<https://x.com/arena/status/2099606881845321841>)

**Q0321 · 2026-09-14 · [Testselektion bei stark wachsender Agent-CI skalieren](<../80_Knowledge/Sources/2026-09-14-claude-agentic-coding-is-straining-ci-here-s-how-we-sca.md>)**

Bei stark wachsender Agenten-CI ist nicht nur Testlaufzeit, sondern auch die Aktualität der Testauswahl ein Korrektheitsfaktor; zustandslose Ergebnisannahme und separate Historienbildung erleichtern die Skalierung. **Grenze:** Anthropics 25-fache Last und drei Wochen Umbau sind historische Betriebsangaben; Journal und Consumer kosten mehr und der Bericht belegt keine Exactly-once- oder Wiederherstellungsgarantien. [Rohtext](<../00_Inbox/Quellen/URL/2026-09-14-claude-agentic-coding-is-straining-ci-here-s-how-we-sca.md>) · [Original](<https://claude.com/de/resources/articles/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic>)

**Q0322 · 2026-09-14 · [Plugin-Evals mit `claude plugin eval` und No-Plugin-Baseline](<../80_Knowledge/Sources/2026-09-14-code-test-plugins-with-evals-claude-code-docs.md>)**

Plugin-Evals sollten Ergebnisqualität und Ausführungsweg getrennt gegen eine No-Plugin-Baseline bewerten und dabei Judge-Stabilität, Isolation, Kosten und tatsächlich erlaubte Werkzeuge prüfen. **Grenze:** Die archivierte frühe Herstellerdokumentation enthält leere Detailabschnitte; Hooks und reale MCP-Server haben weitergehenden Netzwerkzugang, und publizierte Reports sowie echte Modellnutzung erfordern bewusste Konfiguration. [Rohtext](<../00_Inbox/Quellen/URL/2026-09-14-code-test-plugins-with-evals-claude-code-docs.md>) · [Original](<https://code.claude.com/docs/en/plugin-evals>)

**Q0323 · 2026-09-14 · [Skills und Grenzen mit Modellwechsel überprüfen](<../80_Knowledge/Sources/2026-09-14-developers-rethinking-skills-and-prompts-for-gpt-6-astra-op.md>)**

Der OpenAI-Herstellerbeitrag empfiehlt kurze Skill-Auslöser, gestaffelte Referenzen und aufgabengerechte Vorgaben statt überladener Standardlektüre. **Grenze:** Eng verwandte Fassung von Provenchers Artikel; kein unabhängiger Wirksamkeitsnachweis und unsicheres Veröffentlichungsdatum. [Rohtext](<../00_Inbox/Quellen/URL/2026-09-14-developers-rethinking-skills-and-prompts-for-gpt-6-astra-op.md>) · [Original](<https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra>)

**Q0324 · 2026-09-14 · [Designsystem-Verträge mit verständlichen Lint-Korrekturen](<../80_Knowledge/Sources/2026-09-14-shadcn-2099534231114314145.md>)**

Komponentenverträge können erlaubte Layoutänderungen von unerlaubtem Restyling unterscheiden und konkrete Ersatzwege melden. **Grenze:** Herstellerevals messen Korrektur von Regelverstößen und keine gesamte App-Qualität oder unabhängige Kostenersparnis. [Rohtext](<../00_Inbox/Quellen/X/2026-09-14-shadcn-2099534231114314145.md>) · [Original](<https://x.com/shadcn/status/2099534231114314145>)

**Q0325 · 2026-09-14 · [Abnahmekriterien am laufenden Ergebnis prüfen](<../80_Knowledge/Sources/2026-09-14-voxyz_ai-2099528601557496220.md>)**

Abnahmekriterien müssen am laufenden Ergebnis durch tatsächliche Interaktion, Zustandsprüfung und Persistenztest überprüft werden. **Grenze:** Eine Browserpräferenz des Autors ist keine allgemeine Produktbewertung und keine gemessene Ersparnis. [Rohtext](<../00_Inbox/Quellen/X/2026-09-14-voxyz_ai-2099528601557496220.md>) · [Original](<https://x.com/Voxyz_ai/status/2099528601557496220>)

**Q0326 · 2026-09-15 · [Interaktive Varianten vergleichen, dann produktionsreif prüfen](<../80_Knowledge/Sources/2026-09-15-emilkowalski-2099948779864793303.md>)**

Bedienbare, tatsächlich unterschiedliche Designvarianten unterstützen die menschliche Auswahl; Performance, Accessibility und mobile Nutzung benötigen anschließend eine eigene Produktionsprüfung. **Grenze:** Persönlicher Erfahrungsbericht ohne gemessene Verbesserung; der historische Skillname prep-for-prod fehlt im geprüften Repo-Stand, und automatisierte Varianten nehmen dem Menschen keine Geschmacksentscheidung ab. [Rohtext](<../00_Inbox/Quellen/X/2026-09-15-emilkowalski-2099948779864793303.md>) · [Original](<https://x.com/emilkowalski/status/2099948779864793303>)

**Q0327 · 2026-09-17 · [Code Mode als komposierbare Toolschnittstelle](<../80_Knowledge/Sources/2026-09-17-agenticjames-i-think-code-mode-mcps-are-probably-the-best-way-to-give-agents-access.md>)**

Ein Code-Mode-Gateway lässt benötigte Tools dynamisch entdecken, in einem Skript komponieren und ihre Ausgaben vor dem Modellkontext filtern. **Grenze:** Kurzvideo ohne Messvergleich; ein zentrales Gateway bündelt Zugangsdaten und erhöht die Bedeutung begrenzter Rechte. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-09-17-agenticjames-i-think-code-mode-mcps-are-probably-the-best-way-to-give-agents-access.md>) · [Original](<https://www.tiktok.com/@agentic.james/video/7686584043177135373>)

**Q0328 · 2026-09-18 · [Jev: typisiertes Entscheidungsmodell statt LLM-Aufruf für kleine Urteile](<../80_Knowledge/Sources/2026-09-18-akshay_pachaar-2101037514945597645.md>)**

Bei bekannten Antwortmöglichkeiten kann ein Modell typisierte Wahrscheinlichkeiten liefern, während Code die Verzweigungen kontrolliert. **Grenze:** Schemasicherheit garantiert kein richtiges Urteil; Latenz- und Kostenmultiplikatoren stammen vom Hersteller. [Rohtext](<../00_Inbox/Quellen/X/2026-09-18-akshay_pachaar-2101037514945597645.md>) · [Original](<https://x.com/akshay_pachaar/status/2101037514945597645>)

**Q0329 · 2026-09-18 · [AGENTS.md-Unterstützung als datierte Produkteigenschaft](<../80_Knowledge/Sources/2026-09-18-repo-anthropics-claude-code-agents-md-support.md>)**

Die archivierte Changelog-Notiz beschreibt AGENTS.md als Ersatz für fehlende CLAUDE.md ab Claude-Code-Version 2.1.277. **Grenze:** Abgeleitete Repo-Notiz, kein eigener Laufzeittest; Unterordner- und Importdetails bleiben offen. [Original](<https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md>) · Gleiche angegebene Herkunft: Q0419.

**Q0330 · 2026-09-19 · [Erst Bild generieren, dann Design umsetzen lassen](<../80_Knowledge/Sources/2026-09-19-voxyz_ai-2101295246659182978.md>)**

Gestaltungsentwurf als Bild und anschließende Implementierung sind getrennte Arbeitsschritte. **Grenze:** Zusatzkosten und Umsetzungsabweichungen bleiben möglich; stärkstes Bildmodell ist ungemessene Wertung. [Rohtext](<../00_Inbox/Quellen/X/2026-09-19-voxyz_ai-2101295246659182978.md>) · [Original](<https://x.com/Voxyz_ai/status/2101295246659182978>)

**Q0331 · 2026-09-19 · [Sieben Rollen-Prompts: Coding Agents Ergebnisverantwortung statt Einzelschritte geben](<../80_Knowledge/Sources/2026-09-19-voxyz_ai-2101355643882065971.md>)**

Rollen-Prompts sollten Verantwortung für ein beobachtbares Endergebnis und passende Nachweise übertragen. **Grenze:** Der Thread zeigt Promptstruktur, keinen Wirkungsvergleich; weniger Rückfragen ersetzt keine Scopegrenzen. [Rohtext](<../00_Inbox/Quellen/X/2026-09-19-voxyz_ai-2101355643882065971.md>) · [Original](<https://x.com/Voxyz_ai/status/2101355643882065971>)

**Q0332 · 2026-09-20 · [Entscheidungen per Scoring statt Textgenerierung: Fixed-Answer-Scoring lokal nachgebaut](<../80_Knowledge/Sources/2026-09-20-avichawla-2101563610644496464.md>)**

Für Entscheidungen mit feststehender Kandidatenmenge kann ein einzelner Prefill mit ausgelesenen Label-Logits die Textgenerierung ersetzen, sofern Tokenisierung, Eskalationsoption und Kalibrierung gemeinsam versioniert werden. **Grenze:** Softmax über Kandidaten ist keine kalibrierte Trefferwahrscheinlichkeit; Codeblöcke fehlen im Archiv, die Demo teilt eine GPU mit der Generierungs-Lane und belegt die Werbezahlen 200x und 400x nicht. [Rohtext](<../00_Inbox/Quellen/X/2026-09-20-avichawla-2101563610644496464.md>) · [Original](<https://x.com/_avichawla/status/2101563610644496464>)

**Q0333 · 2026-09-20 · [Intent, Prüfungen und Betriebsfeedback verbinden den AI-nativen SDLC](<../80_Knowledge/Sources/2026-09-20-eric-tech-claude-code-the-complete-ai-native-sdlc-guide.md>)**

Ein durchgängiger AI-nativer SDLC verbindet begründeten Intent, Verhaltensspezifikation, ausführbaren Plan, Produkttests, eigene Workflow-Evals, Review-Regeln und Betriebsfeedback. **Grenze:** Sekundäre Erklärung des Anthropic-Kurses und Werbung ohne unabhängige Fallstudie; Hooks und skizzierter Rollback sind kein vollständiger Sicherheitsnachweis oder Auftrag zu Produktionseingriffen. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-09-20-eric-tech-claude-code-the-complete-ai-native-sdlc-guide.md>) · [Original](<https://www.youtube.com/watch?v=6CaQ9ZFuuKI>)

**Q0334 · 2026-09-20 · [Drei Design-Skills gegen „mach es schöner“](<../80_Knowledge/Sources/2026-09-20-voxyz_ai-2101657631249031507.md>)**

Benannte Designoperationen, gezielt ausgewählte Referenzen und ein real bedienter Nutzerfluss machen den vagen Wunsch nach schöneren Seiten prüfbarer. **Grenze:** Die Kombination ist selbstberichtet; ein Screenshot beweist keine Interaktion und der Satz zu UX, DX und AX ersetzt keine konkrete Regressionprüfung. [Rohtext](<../00_Inbox/Quellen/X/2026-09-20-voxyz_ai-2101657631249031507.md>) · [Original](<https://x.com/Voxyz_ai/status/2101657631249031507>)

**Q0335 · 2026-09-21 · [Komponentenbibliothek als Design-Reference-Skill und UX-Audit per Agent](<../80_Knowledge/Sources/2026-09-21-voxyz_ai-2102050225443766571.md>)**

Ein Design-Reference-Skill sollte Bezugsquelle, Auswahlkriterien, Anpassung an vorhandene Komponenten und Browserprüfung verbindlich beschreiben und fehlenden Zugriff offen melden. **Grenze:** Bibliothekslimits und Unterschiede der Browserwerkzeuge begrenzen Übertragbarkeit; die Promptvorlagen liefern keine gemessene Ergebnisqualität und übernehmen keine Lizenzprüfung. [Rohtext](<../00_Inbox/Quellen/X/2026-09-21-voxyz_ai-2102050225443766571.md>) · [Original](<https://x.com/Voxyz_ai/status/2102050225443766571>)

**Q0336 · 2026-09-22 · [Preis und Tokenverbrauch gemeinsam vergleichen](<../80_Knowledge/Sources/2026-09-22-artificialanlys-2102438210798514391.md>)**

Die Opus-5.5-Messung illustriert, dass niedrigere Tokenpreise durch höheren Verbrauch weitgehend aufgehoben werden können. **Grenze:** Datierte Drittanbieter-Evals mit proprietären Anteilen und Hersteller-Fallback; keine aktuelle Modellrangfolge. [Rohtext](<../00_Inbox/Quellen/X/2026-09-22-artificialanlys-2102438210798514391.md>) · [Original](<https://x.com/ArtificialAnlys/status/2102438210798514391>)

**Q0337 · 2026-09-22 · [Kostenfortschritt kann Regressionen verbergen](<../80_Knowledge/Sources/2026-09-22-artificialanlys-2102462962758033624.md>)**

Die GPT-6-Sol-und-Luna-Auswertung berichtet günstigere Aufgabenbearbeitung bei gemischten Verbesserungen und Rückschritten einzelner Fähigkeiten. **Grenze:** Historische Preise und Benchmarks vom September 2026; aggregierte Scores verdecken ausgelassene Rubrikpunkte und Präsentationsmängel. [Rohtext](<../00_Inbox/Quellen/X/2026-09-22-artificialanlys-2102462962758033624.md>) · [Original](<https://x.com/ArtificialAnlys/status/2102462962758033624>)

**Q0338 · 2026-09-22 · [Artificial Analysis (@ArtificialAnlys)](<../00_Inbox/Quellen/X/2026-09-22-artificialanlys-2102527962201624915.md>)**

Gleiche Benchmarkleistung bei geringeren Tokenpreisen kann die Aufgabenökonomie verbessern. **Grenze:** Der bereits als Dublette markierte Post ist keine zusätzliche unabhängige Modellbewertung. [Original](<https://x.com/ArtificialAnlys/status/2102527962201624915>)

**Q0339 · 2026-09-22 · [Opus 5.5 führen: Zielzustand, Stopp-Regeln und Task-Datei für lange Läufe](<../80_Knowledge/Sources/2026-09-22-claude-getting-the-most-out-of-opus-5-5-in-claude-and-c.md>)**

Lange Läufe brauchen einen definierten Zielzustand, konkrete Stopps und eine fortgeführte Aufgabenliste außerhalb des Chatverlaufs. **Grenze:** Herstelleraussagen über Modellverhalten und einzelne Tester ersetzen keine eigene Replikation. [Rohtext](<../00_Inbox/Quellen/URL/2026-09-22-claude-getting-the-most-out-of-opus-5-5-in-claude-and-c.md>) · [Original](<https://claude.dev/blog/getting-the-most-out-of-opus-5-5/>)

**Q0340 · 2026-09-22 · [Epoch: Leistungskosten und Grenzen von Frontier-Kurven](<../80_Knowledge/Sources/2026-09-22-epoch-the-plunging-price-of-thought.md>)**

Epoch modelliert die billigste verfügbare Benchmarkleistung auf festen Qualitätsniveaus und berichtet starken historischen Preisverfall. **Grenze:** Kein allgemeiner Produktivitäts- oder Preisausblick: nur etwa drei Jahre Daten, Benchmaxxing, unvollständige Abdeckung und bewusst keine Standardfehler. [Rohtext](<../00_Inbox/Quellen/URL/2026-09-22-epoch-the-plunging-price-of-thought.md>) · [Original](<https://epoch.ai/publications/the-plunging-price-of-thought>)

**Q0341 · 2026-09-22 · [Epoch AI (@EpochAIResearch)](<../00_Inbox/Quellen/X/2026-09-22-epochairesearch-2102510281176023529.md>)**

Epoch beschreibt stark fallende Kosten für ein konstantes Benchmark-Leistungsniveau und zeigt damit, weshalb historische Modell- und Effort-Entscheidungen regelmäßig neu evaluiert werden sollten. **Grenze:** Der Thread verweist auf 222 Modelle und elf Benchmarks, liefert aber nicht den vollständigen Datensatz; 47 Prozent pro Quartal sind eine datierte Auswertung und keine Kostenprognose für reale Arbeitsabläufe. [Original](<https://x.com/EpochAIResearch/status/2102510281176023529>)

**Q0342 · 2026-09-22 · [Herstellerbenchmarks auf gewählte Vergleichsstufen prüfen](<../80_Knowledge/Sources/2026-09-22-kimmonismus-2102462091299098640.md>)**

Die weitergegebenen GPT-6-Vergleiche illustrieren Kosten pro Aufgabe, hängen aber entscheidend von den ausgewählten Effort- und Fallback-Stufen ab. **Grenze:** Sekundärpost mit Herstellerzahlen; ungleiche Vergleichsstufen und historische Preise. [Rohtext](<../00_Inbox/Quellen/X/2026-09-22-kimmonismus-2102462091299098640.md>) · [Original](<https://x.com/kimmonismus/status/2102462091299098640>)

**Q0343 · 2026-09-22 · [Debug-Schleifen und Kontext als Kostenfaktoren](<../80_Knowledge/Sources/2026-09-22-promptgefluester-ich-arbeite-mit-multiorgastation-und-das-hat-was-mit-meinem-tokenlimit.md>)**

Exakte Fehlermeldungen, betroffene Dateien, statische Analyse und ein überprüfter Plan können unnötige Such- und Reparaturschleifen verkürzen. **Grenze:** Unvermessener Erfahrungsbericht mit Eigenwerbung und stark fehlerhaftem ASR; xhigh als Coding-Pauschale widerspricht sparsameren Empfehlungen. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-09-22-promptgefluester-ich-arbeite-mit-multiorgastation-und-das-hat-was-mit-meinem-tokenlimit.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7688428923016826145>)

**Q0344 · 2026-09-22 · [Versionierte Übergaben verbinden schnelle Agenten mit menschlicher Abnahme](<../80_Knowledge/Sources/2026-09-22-vateo-after-waterfall-agile-and-devops-anthropic-s-ai.md>)**

Versionierte Intent-, Spezifikations- und Planartefakte können Phasen verbinden, doch ihre bloße Ablage belegt keine schnellere Lieferung. **Grenze:** Hooks kontrollieren nur implementierte Bedingungen; Herstellerquote zum Codeanteil misst keinen Kundennutzen [Rohtext](<../00_Inbox/Quellen/URL/2026-09-22-vateo-after-waterfall-agile-and-devops-anthropic-s-ai.md>) · [Original](<https://vateo.medium.com/after-waterfall-agile-and-devops-anthropics-ai-native-sdlc-playbook-0131a3a9156e>)

**Q0345 · 2026-09-23 · [Pareto-Front Intelligence vs. Kosten verschiebt sich um elf Punkte](<../80_Knowledge/Sources/2026-09-23-artificialanlys-2102833926788288704.md>)**

Kostenoptimierung lässt sich als Pareto-Auswahl zwischen gemessener Leistung und Kosten je Aufgabe behandeln, wobei unterschiedliche Effort-Stufen eigene Optionen bilden. **Grenze:** Die datierten Intelligence-Index-Werte gelten weder für den Coding Agent Index noch für eigene Sitzungen; die Front hängt vom gemessenen Modellset und Aufgabenmix ab. [Rohtext](<../00_Inbox/Quellen/X/2026-09-23-artificialanlys-2102833926788288704.md>) · [Original](<https://x.com/ArtificialAnlys/status/2102833926788288704>)

**Q0346 · 2026-09-23 · [Performance-Agenten brauchen validierte Messgrößen und geschützte Gewinne](<../80_Knowledge/Sources/2026-09-23-claude-how-we-made-claude-ai-3x-faster-in-two-weeks-cla.md>)**

Performance-Agenten werden durch nutzerrelevante Messungen, gegen reale Latenz validierte CI-Proxys, geschützte Verbesserungen und risikobewusste menschliche Abnahme wirksam steuerbar. **Grenze:** Der Herstellerbericht nennt historische Erfolge ohne unabhängige Reproduktion und ausdrücklich keine vollständige Autonomie; Headless-Tests übersahen einen realen Browserfall, und ein 900-Zeilen-PR für zwei Millisekunden wurde wegen Wartungskosten abgelehnt. [Rohtext](<../00_Inbox/Quellen/URL/2026-09-23-claude-how-we-made-claude-ai-3x-faster-in-two-weeks-cla.md>) · [Original](<https://claude.dev/blog/how-we-made-claude-ai-faster/>)

**Q0347 · 2026-09-23 · [Epoch AI: Kosten je Leistungsniveau sinken um rund 13-fach pro Jahr](<../80_Knowledge/Sources/2026-09-23-kimmonismus-2102748118400004100.md>)**

Die Kosten eines konstanten Benchmark-Fähigkeitsniveaus sind von den Kosten stets führender Modelle zu unterscheiden und sollten nicht als unbegrenzt fortsetzbarer Preisrückgang extrapoliert werden. **Grenze:** Sekundärer Kommentar zur bereits archivierten Epoch-Auswertung; globale Zugänglichkeit und Fable-Niveau für alle werden aus den Zahlen nicht nachgewiesen, und die Notiz behauptet fälschlich, Epoch liege gar nicht im Archiv. [Rohtext](<../00_Inbox/Quellen/X/2026-09-23-kimmonismus-2102748118400004100.md>) · [Original](<https://x.com/kimmonismus/status/2102748118400004100>)

**Q0348 · 2026-09-24 · [PR-Engpass lösen: Checks, Review-Agent mit Commits, risikobasiertes Human Review](<../80_Knowledge/Sources/2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck.md>)**

Pocock verlagert Qualitätsarbeit in deterministische Checks und einen eigenen Review-Kontext, damit menschliches Review weniger unfertige Arbeit übernimmt. **Grenze:** Reviewer soll Fixes ausführen, benötigt dafür dennoch Autorisierung; automatisches Transkript enthält eine markierte Lücke; Erfahrungsbericht ohne Messreihe [Rohtext](<../00_Inbox/Quellen/YouTube/2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck.md>) · [Original](<https://www.youtube.com/watch?v=g0vqT_wZtXA>)

**Q0349 · 2026-09-24 · [Opus 5.5 führt den Coding Agent Index, aber mit den höchsten Kosten pro Task](<../80_Knowledge/Sources/2026-09-24-artificialanlys-2102932119995756613.md>)**

Ein niedrigerer Tokenpreis kann von höherem Tokenverbrauch überkompensiert werden, weshalb die Kosten je akzeptierter Aufgabe mehr aussagen als der isolierte API-Tarif. **Grenze:** Die Messwerte gelten für Claude Code mit max-Effort und einen gleich gewichteten historischen Coding Agent Index; daraus folgt kein universelles Preis-Leistungs-Optimum für eigene Aufgaben. [Rohtext](<../00_Inbox/Quellen/X/2026-09-24-artificialanlys-2102932119995756613.md>) · [Original](<https://x.com/ArtificialAnlys/status/2102932119995756613>)

**Q0350 · 2026-09-24 · [Gemeinsame Agentensessions brauchen prüfbare Rechte](<../80_Knowledge/Sources/2026-09-24-floknowsai-open-claw-ist-zurueck-und-spielt-jetzt-wieder-in-einer-liga-mit-kodex.md>)**

Der OpenClaw-Erfahrungsbericht verbindet gemeinsame Sessions mit Zuständigkeit, sichtbaren Beiträgen, Übergaben und gemeinsamem Memory. **Grenze:** Produktbericht mit Bildstichproben und ASR, ohne Funktions- oder Sicherheitstest. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-09-24-floknowsai-open-claw-ist-zurueck-und-spielt-jetzt-wieder-in-einer-liga-mit-kodex.md>) · [Original](<https://www.tiktok.com/@floknowsai/video/7689104906992487702>)

**Q0351 · 2026-09-24 · [Fehler auf der richtigen Agentenebene lokalisieren](<../80_Knowledge/Sources/2026-09-24-mattpocock-ai-coding-dictionary.md>)**

Modell, Harness, Provider und Umgebung sowie fehlende Information, ignorierte Vorgabe und veralteter Snapshot sollten diagnostisch getrennt werden. **Grenze:** Redaktionelle Synthese eines Wörterbuchs, keine Wirksamkeitsstudie; archivierte Hauptquelle liegt außerhalb dieser zugewiesenen Pfade. [Original](<https://www.aihero.dev/ai-coding-dictionary>)

**Q0352 · 2026-09-24 · [KI-Risiken für Minderjährige: Warnung und Schutzforderungen getrennt von Schadensnachweisen](<../80_Knowledge/Sources/2026-09-24-orf-ex-google-manager-warnt-vor-ki-gefahren-fuer-kin.md>)**

Warnungen vor KI-Schäden für Minderjährige dokumentieren Schutzforderungen, sind aber ohne Studien und Kausalitätsprüfung keine empirischen Schadensnachweise. **Grenze:** Kurze Agenturmeldung über Siegels Position; weder Reuters-Original noch die Wirksamkeit von Altersprüfung oder Abschaltoption werden untersucht. [Rohtext](<../00_Inbox/Quellen/URL/2026-09-24-orf-ex-google-manager-warnt-vor-ki-gefahren-fuer-kin.md>) · [Original](<https://orf.at/stories/3443075/>)

**Q0353 · 2026-09-25 · [Using Claude Code: Spending your effort / claude.dev Blog](<../00_Inbox/Quellen/URL/2026-09-25-claude-using-claude-code-spending-your-effort-claude-de.md>)**

Diese Datei dokumentiert eine bereits andernorts archivierte identische Quelle und liefert keinen zusätzlichen unabhängigen Befund. **Grenze:** Nur Dublettenhinweis statt Volltext [Original](<https://claude.dev/blog/spending-your-effort/>)

**Q0354 · 2026-09-25 · [Geordneter Stopp am Nutzungslimit](<../00_Inbox/Quellen/X/2026-09-25-claudedevs-2103561342057943314.md>)**

ClaudeDevs kündigt einen begrenzten Abschluss-Spielraum an, der beim Sitzungslimit einen geordneten Stopp ermöglichen soll. **Grenze:** Datierte Ankündigung ohne eigenen Test oder garantierte Fertigstellung. [Original](<https://x.com/ClaudeDevs/status/2103561342057943314>)

**Q0355 · 2026-09-25 · [PR-Engpass als Reviewproblem](<../00_Inbox/Quellen/X/2026-09-25-mattpocockuk-2103501498361798983.md>)**

Pocock verweist auf einen Vortrag über weniger unnötige Änderungen und leichter reviewbare Pull Requests. **Grenze:** Verweis auf andernorts archivierten Vortrag, kein unabhängiger Beleg. [Original](<https://x.com/mattpocockuk/status/2103501498361798983>)

**Q0356 · 2026-09-25 · [Aufgabenverwaltung von paralleler Ausführung trennen](<../80_Knowledge/Sources/2026-09-25-promptgefluester-weil-mich-viele-danach-gefragt-haben-wollt-ich-jetzt-kurz-noch-n.md>)**

Getrennte Zuständigkeiten für Priorisierung und parallele Ausführung erleichtern einen nachvollziehbaren Aufgabenstand, während zurückgemeldete Nutzerfehler in konkrete Regressionstests überführt werden sollten. **Grenze:** Automatisch erfasstes werbliches Transkript; Prozentstatus, 1600 Tests und fünffache Beschleunigung sind keine unabhängig geprüfte Funktionsabnahme. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-09-25-promptgefluester-weil-mich-viele-danach-gefragt-haben-wollt-ich-jetzt-kurz-noch-n.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7689553692198063393>)

**Q0357 · 2026-09-25 · [Effort an Rückkopplung und Randfällen ausrichten](<../80_Knowledge/Sources/2026-09-25-trq212-2103576349499855160.md>)**

Thariqs Fallanalysen verbinden höheren Effort besonders mit mehr Verifikation und Randfalltests, während falsche Grundansätze oft bestehen bleiben. **Grenze:** Herstellermessungen mit kleinen Untergruppen; mehr Effort bedeutet bei unklaren Aufträgen auch mehr eigenständige Annahmen und längere Laufzeiten. [Rohtext](<../00_Inbox/Quellen/X/2026-09-25-trq212-2103576349499855160.md>) · [Original](<https://x.com/trq212/status/2103576349499855160>)

**Q0358 · 2026-09-25 · [Builder und Verifier als getrennte Rollen](<../80_Knowledge/Sources/2026-09-25-voxyz_ai-2103586663393853636.md>)**

Der Vorschlag übersetzt schnelle Umsetzung und gründliche Prüfung in zwei Agenten mit jeweils eigenem Auftrag und Effort. **Grenze:** Abgeleiteter Ablauf ohne eigene Messung, zusätzliche Übergabe- und Prüfkosten. [Rohtext](<../00_Inbox/Quellen/X/2026-09-25-voxyz_ai-2103586663393853636.md>) · [Original](<https://x.com/Voxyz_ai/status/2103586663393853636>)

**Q0359 · 2026-09-26 · [Website-Demo: Suchintention, Marke und visuelle Prüfung zusammenführen](<../80_Knowledge/Sources/2026-09-26-ai-mit-arnie-gpt-6-kann-endlich-design.md>)**

Ein Website-Briefing gewinnt an Klarheit, wenn Zielhandlung und Suchabsicht vor der Seitenstruktur festgelegt werden. **Grenze:** Automatische Untertitel und Eigenwerbung; vollständige SEO-/GEO-Optimierung unbelegt; Kosten und Tools historisch [Rohtext](<../00_Inbox/Quellen/YouTube/2026-09-26-ai-mit-arnie-gpt-6-kann-endlich-design.md>) · [Original](<https://www.youtube.com/watch?v=mq6pkNAOwE4>)

**Q0360 · 2026-09-26 · [Coding-Standards aus konkreten Agentenfehlern pflegen](<../80_Knowledge/Sources/2026-09-26-mattpocockuk-2103748049906397613.md>)**

Coding-Standards können aus konkreten Agentenfehlern entstehen und über einen Verweis auf das Designsystem ergänzt werden. **Grenze:** Empfehlung ohne gemessene Fehlerreduktion [Rohtext](<../00_Inbox/Quellen/X/2026-09-26-mattpocockuk-2103748049906397613.md>) · [Original](<https://x.com/mattpocockuk/status/2103748049906397613>)

**Q0361 · 2026-09-26 · [Pre-Launch-Check für Vibe-Coding-Sites: fünf Subagents, 20 Prüfpunkte](<../80_Knowledge/Sources/2026-09-26-voxyz_ai-2103977414711767244.md>)**

Ein Pre-Launch-Check sollte Designkonsistenz, mobile Nutzung, UI-Zustände, echte Kernabläufe und verständliche Inhalte getrennt betrachten und anschließend zentral konsolidieren. **Grenze:** Fünf Subagents und medium-Effort sind Empfehlungen ohne gemessene Kosten oder Trefferquote; die Freigaberegel im Beispiel ist kein allgemein geltender Agentenauftrag. [Rohtext](<../00_Inbox/Quellen/X/2026-09-26-voxyz_ai-2103977414711767244.md>) · [Original](<https://x.com/Voxyz_ai/status/2103977414711767244>)

**Q0362 · 2026-09-27 · [SDLC als überprüfbare Artefaktkette](<../80_Knowledge/Sources/2026-09-27-anthropic-academy-sdlc-playbook.md>)**

Das Academy-Playbook verbindet Intent, Spezifikation, Plan, Änderung, Review und Betriebsbefunde über versionierte Artefakte zu einer rückgekoppelten Entwicklungsschleife. **Grenze:** Herstellerleitfaden ohne Wirkungsmessung; Beispiel-Hooks und Sigma-Grenzen sind keine universellen Sicherheits- oder Governance-Garantien, vollständiges Paket für kleine Teams oft zu groß. [Rohtext](<../00_Inbox/Quellen/URL/2026-09-27-anthropic-academy-sdlc-playbook.md>) · [Original](<https://academy.claude.com/de/courses/ai-native-sdlc-playbook>)

**Q0363 · 2026-09-27 · [Vier read-only Breaker-Subagents vor dem Launch: 16 Prüffragen mit Sicherheitsregeln](<../80_Knowledge/Sources/2026-09-27-voxyz_ai-2104224555040452925.md>)**

Adversariale Vorabprüfungen gewinnen durch konkrete Fehlerfälle, getrennte Testkonten, isolierte Daten, begrenzte API-Ausgaben und reproduzierbare Befunde statt pauschaler Sicherheitsbehauptungen. **Grenze:** Der kleine Fragenkatalog ersetzt keine umfassende Sicherheitsprüfung; erlaubte Befehle und Browser können Daten verändern, sodass read-only Codezugriff keine schreibfreie Umgebung garantiert und Stopp-Prompts keine technische Sperre sind. [Rohtext](<../00_Inbox/Quellen/X/2026-09-27-voxyz_ai-2104224555040452925.md>) · [Original](<https://x.com/Voxyz_ai/status/2104224555040452925>)

**Q0364 · 2026-09-27 · [105 Agenten in fünf Workflows: Parallelität begrenzen, Effort nach Rolle staffeln](<../80_Knowledge/Sources/2026-09-27-voxyz_ai-2104254744722383210.md>)**

Begrenzte Parallelität, getrennte Schreibbereiche und Abschlussmarker machen lange Extraktionsläufe kontrollierbarer. **Grenze:** Aufgabentyp und Parallelität gleichzeitig verändert; kein kausaler Vergleich; hohe Tokenkosten [Rohtext](<../00_Inbox/Quellen/X/2026-09-27-voxyz_ai-2104254744722383210.md>) · [Original](<https://x.com/Voxyz_ai/status/2104254744722383210>)

**Q0365 · 2026-09-28 · [Niedriger Tokenpreis garantiert keine billige Aufgabe](<../80_Knowledge/Sources/2026-09-28-artificialanlys-2104640155843989864.md>)**

Die Sonnet-5.5-Auswertung berichtet hohe Leistung mit außergewöhnlich hohem Ausgabetokenverbrauch und entsprechend höheren Aufgabenpreisen. **Grenze:** Vorab-Deployment mit bekanntem Structured-Output-Bug; datierte Messwerte und Fallback-Konfiguration. [Rohtext](<../00_Inbox/Quellen/X/2026-09-28-artificialanlys-2104640155843989864.md>) · [Original](<https://x.com/ArtificialAnlys/status/2104640155843989864>)

**Q0366 · 2026-09-28 · [Evals und Hillclimbing gegen Selbsttäuschung absichern](<../80_Knowledge/Sources/2026-09-28-claude-automating-eval-design-and-hillclimbing-with-cla.md>)**

Ein brauchbares Eval verbindet repräsentative Aufgaben, menschlich kalibrierte Prüfer, Wiederholungen, kontrollierte Umgebung und einen vor dem Optimierer geschützten Datensatz. **Grenze:** Herstellerfälle klein und ohne Rohdaten; wiederholte Auswahl anhand desselben Holdouts kann diesen zur Validierungsmenge machen, ein abschließender frischer Test bleibt sinnvoll. [Rohtext](<../00_Inbox/Quellen/URL/2026-09-28-claude-automating-eval-design-and-hillclimbing-with-cla.md>) · [Original](<https://claude.dev/blog/automating-eval-design-and-hillclimbing/>)

**Q0367 · 2026-09-28 · [Sonnet 5.5 einsetzen: Effort neu kalibrieren, Workarounds streichen, echten Check verlangen](<../80_Knowledge/Sources/2026-09-28-claude-building-with-claude-sonnet-5-5-claude-dev-blog.md>)**

Ein Modellwechsel erfordert neue Effort-Evals und Prüfungen der API-Antwortstruktur statt bloßen Austausch einer Modell-ID. **Grenze:** Historische Herstellerpreise; maximales Effort kann den Effizienzvorteil aufheben; Prompt verlangt Checks, erzwingt sie technisch nicht [Rohtext](<../00_Inbox/Quellen/URL/2026-09-28-claude-building-with-claude-sonnet-5-5-claude-dev-blog.md>) · [Original](<https://claude.dev/blog/building-with-claude-sonnet-5-5/>)

**Q0368 · 2026-09-28 · [Codex Releases (@CodexReleases)](<../00_Inbox/Quellen/X/2026-09-28-codexreleases-2104438417220149728.md>)**

Release-Zusammenfassungen eines Community-Accounts können relevante Änderungsbereiche auffinden helfen, benötigen für tatsächliches Produktverhalten aber die zugrunde liegenden offiziellen Release-Quellen. **Grenze:** Bereits ignorierte Triage-Quelle ohne Methode; die datierten Angaben zu Codex 0.158.0 wurden nicht am Original oder in einer Installation bestätigt. [Original](<https://x.com/CodexReleases/status/2104438417220149728>)

**Q0369 · 2026-09-28 · [Unsloth: Laya Decision Models lokal ab 4 GB RAM mit Jev-kompatibler API](<../80_Knowledge/Sources/2026-09-28-unslothai-2104592692072304916.md>)**

Ein lokales Decision-Modell kann kurze Eingaben über einen festen Antwortraum bewerten und vorhandene Integrationen per kompatibler API bedienen. **Grenze:** Herstellerankündigung ohne Latenz-/Qualitätsmessung; lange Traces müssen gekürzt werden [Rohtext](<../00_Inbox/Quellen/X/2026-09-28-unslothai-2104592692072304916.md>) · [Original](<https://x.com/UnslothAI/status/2104592692072304916>)

**Q0370 · 2026-09-28 · [Ziel, Ausgabe, Grenzen und Kontext als Auftrag](<../80_Knowledge/Sources/2026-09-28-vincentmumme-prompt-engineering-ist-schon-lange-tot-und-ich-weiss-nicht-ob-ihr-euch.md>)**

Das gezeigte Promptschema formuliert Ergebnis, Darstellungsform, Einschränkungen und Hintergrund ausdrücklich und setzt vor einem Kauf eine menschliche Freigabe. **Grenze:** Best-Practice- und Urheberzuschreibung ungeprüft; Tod des Prompt Engineering ist rhetorische Wertung. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-09-28-vincentmumme-prompt-engineering-ist-schon-lange-tot-und-ich-weiss-nicht-ob-ihr-euch.md>) · [Original](<https://www.tiktok.com/@vincentmumme/video/7690594570375122209>)

**Q0371 · 2026-09-29 · [Effort besitzt keine garantierte monotone Qualitätskurve](<../80_Knowledge/Sources/2026-09-29-artificialanlys-2105025585332605357.md>)**

Der GPT-6.1-Sol-Bericht zeigt im Coding Agent Index einen höheren gemessenen Wert bei xhigh als bei max. **Grenze:** Datierte Drittanbietermessung; Source-Notiz ist bei Medienabdeckung älter als das ergänzte Roharchiv. [Rohtext](<../00_Inbox/Quellen/X/2026-09-29-artificialanlys-2105025585332605357.md>) · [Original](<https://x.com/ArtificialAnlys/status/2105025585332605357>)

**Q0372 · 2026-09-29 · [WSL containers is now generally available](<../00_Inbox/Quellen/URL/2026-09-29-blogs-wsl-containers-is-now-generally-available.md>)**

Container-Lebenszyklus, Gesundheitsprüfungen, Ereignisbeobachtung und Registry-Kontrollen gehören zur Betriebsumgebung, sagen für sich aber nichts über zuverlässige Agentenarbeit aus. **Grenze:** Ignorierte Herstellerankündigung vom September: Compose ist dort noch Roadmap, nicht vorhandene Funktion; Leistungs- und Verwaltungsversprechen wurden hier nicht praktisch verifiziert. [Original](<https://blogs.windows.com/windowsdeveloper/2026/09/29/wsl-containers-now-generally-available/>)

**Q0373 · 2026-09-29 · [OpenAI DevDay 2026: Modelle, Preisstufen und Agent-Infrastruktur im Überblick](<../80_Knowledge/Sources/2026-09-29-openai-rueckblick-auf-den-devday-2026.md>)**

Die DevDay-Ankündigungen bündeln Modelle, verwaltete Harness-Infrastruktur, begrenzte Entscheidungs-APIs und gemeinsam bearbeitbare Arbeitsartefakte als verschiedene Ebenen eines Agentenökosystems. **Grenze:** Herstellerankündigung zum 29. September ohne Nutzenmessung; fast alle Preise, Verfügbarkeiten und Datenschutzversprechen sind zeitkritisch, ein Fünftel Tokenpreis bedeutet nicht ein Fünftel Aufgabenkosten. [Rohtext](<../00_Inbox/Quellen/URL/2026-09-29-openai-rueckblick-auf-den-devday-2026.md>) · [Original](<https://openai.com/de-DE/index/devday-2026-recap/>)

**Q0374 · 2026-09-29 · [Control Plane als Unternehmensziel, nicht Sicherheitsbeweis](<../80_Knowledge/Sources/2026-09-29-openclaw-openclaw-enterprise-the-open-agent-platform-open.md>)**

OpenClaw Enterprise wird als austauschbare Control Plane für persistente Agenten mit Governance, Isolation und feinen Rechten angekündigt. **Grenze:** Herstellerankündigung und Eigenbericht; Multi-Tenancy und harte Grenzen sind ohne Architekturprüfung keine belegten Garantien. [Rohtext](<../00_Inbox/Quellen/URL/2026-09-29-openclaw-openclaw-enterprise-the-open-agent-platform-open.md>) · [Original](<https://openclaw.ai/blog/openclaw-enterprise>)

**Q0375 · 2026-09-29 · [Security-Checkliste mit 30 Punkten für vibe-coded Apps](<../80_Knowledge/Sources/2026-09-29-suraj_sharma14-2104790775397830755.md>)**

Eine Sicherheitsliste hilft als Fragenkatalog, ersetzt aber keine Prüfverfahren für Zugriff, Geheimnisse und Missbrauchsschutz. **Grenze:** Pauschale Empfehlungen wie RLS für jede Tabelle benötigen konkrete Architekturprüfung; kein Wirksamkeitsnachweis [Rohtext](<../00_Inbox/Quellen/X/2026-09-29-suraj_sharma14-2104790775397830755.md>) · [Original](<https://x.com/suraj_sharma14/status/2104790775397830755>)

**Q0376 · 2026-09-29 · [Theos Terminal-Bench-Selbstmessung zeigt den Einfluss des Harness](<../80_Knowledge/Sources/2026-09-29-theo-2105063015712465094.md>)**

Modellbenchmarks messen Modell, Harness und Werkzeugzugang gemeinsam und lassen sich ohne gleiche Konfiguration nicht isoliert vergleichen. **Grenze:** Datierte Selbstmessung statt kontrolliertem Harnessvergleich [Rohtext](<../00_Inbox/Quellen/X/2026-09-29-theo-2105063015712465094.md>) · [Original](<https://x.com/theo/status/2105063015712465094>)

**Q0377 · 2026-09-29 · [OpenAI öffnet Pro $200 wieder, rechnet Nutzung aber auf halben API-Gegenwert um](<../80_Knowledge/Sources/2026-09-29-thsottiaux-2104823812042940713.md>)**

Ein Abo sollte nach tatsächlich erledigter Arbeit, Qualitätsniveau und Nutzungsgrenzen beurteilt werden, weil ein nomineller API-Gegenwert durch Preis- und Abrechnungsänderungen verschoben wird. **Grenze:** Datierte Herstellerankündigung ohne Rechenbeispiel; die Garantie künftig höherer Arbeitsmenge und der Wegfall eines Limits sind weder unabhängig gemessen noch als heutiger Tarif bestätigt. [Rohtext](<../00_Inbox/Quellen/X/2026-09-29-thsottiaux-2104823812042940713.md>) · [Original](<https://x.com/thsottiaux/status/2104823812042940713>)

**Q0378 · 2026-09-29 · [ChatGPT-Abonnement als Zugang zu über 16 Partnerprodukten](<../80_Knowledge/Sources/2026-09-29-thsottiaux-2105006253986738615.md>)**

Ein Partnerlogin über ein vorhandenes Abonnement sagt noch nichts über zusätzliche Produktentgelte, regionale Verfügbarkeit oder unbegrenzte Nutzung aus. **Grenze:** Historische Produktankündigung ohne Nutzungsprüfung [Rohtext](<../00_Inbox/Quellen/X/2026-09-29-thsottiaux-2105006253986738615.md>) · [Original](<https://x.com/thsottiaux/status/2105006253986738615>)

**Q0379 · 2026-09-29 · [Modellalias und Effort sind veränderliche Konfiguration](<../80_Knowledge/Sources/2026-09-29-voxyz_ai-2104919123918479521.md>)**

Ein Setup-Audit sollte Modellvererbung, Aliase, hart codierten Effort und API-Altannahmen zusammen prüfen. **Grenze:** Sekundärprompt ohne Messung; halbierter Tokenpreis ist nicht gleich halbierter Aufgabenpreis. [Rohtext](<../00_Inbox/Quellen/X/2026-09-29-voxyz_ai-2104919123918479521.md>) · [Original](<https://x.com/Voxyz_ai/status/2104919123918479521>)

**Q0380 · 2026-09-29 · [Codex-Agent-Tree: Orchestrator auf high, Subagents auf medium, Astra nur als Reviewer](<../80_Knowledge/Sources/2026-09-29-voxyz_ai-2105012597796057438.md>)**

Rollenbezogene Modell- und Effort-Wahl muss an tatsächlich ausgeführten Sessions geprüft werden, weil Vererbung deklarierte Zuweisungen übersteuern kann. **Grenze:** Benchmarkbasierte Effort-Wahl ist modellspezifisch; Preisrelationen historisch; frischer Kontext benötigt selbsttragenden Auftrag [Rohtext](<../00_Inbox/Quellen/X/2026-09-29-voxyz_ai-2105012597796057438.md>) · [Original](<https://x.com/Voxyz_ai/status/2105012597796057438>)

**Q0381 · 2026-09-30 · [Gemini 4 Argon: Index-Gleichstand mit GPT-6 Astra, weniger Halluzinationen, Rabattpreis](<../80_Knowledge/Sources/2026-09-30-artificialanlys-2105392625788637299.md>)**

Eine geringere Halluzinationsrate kann mit niedrigerer Antwortgenauigkeit einhergehen, und ein rabattierter Aufgabenpreis kann mehr von Preisaktionen als von effizienterer Inferenz abhängen. **Grenze:** Historischer Test eines nur ausgewählten Nutzern verfügbaren Modells; Index, Effort, API-Fortsetzungsfunktion und Rabatt bilden einen speziellen Messstand und keine aktuelle Rangfolge. [Rohtext](<../00_Inbox/Quellen/X/2026-09-30-artificialanlys-2105392625788637299.md>) · [Original](<https://x.com/ArtificialAnlys/status/2105392625788637299>)

**Q0382 · 2026-09-30 · [Motion wird durch Frame-Verträge und konkrete Korrekturen steuerbar](<../80_Knowledge/Sources/2026-09-30-flxrnc-2105311836190978392.md>)**

Adressierbare deterministische Frames machen visuelle Fehler zu konkreten Reparaturaufgaben statt vagen Geschmacksurteilen. **Grenze:** Vager und gerichteter Prompt erhielten ungleiche Nacharbeit; Archiv enthält fehlende Promptblöcke; numerische Checks belegen keine Publikumswirkung [Rohtext](<../00_Inbox/Quellen/X/2026-09-30-flxrnc-2105311836190978392.md>) · [Original](<https://x.com/flxrnc/status/2105311836190978392>)


### 2026-10

**Q0383 · 2026-10-01 · [Ein Motion-Studio braucht überprüfbare Produktionsstufen](<../80_Knowledge/Sources/2026-10-01-0xwhrrari-2105643919119696297.md>)**

Wiederverwendbare Filmproduktion braucht getrennte Brief-, Asset-, Timeline-, Render- und Abnahmeartefakte. **Grenze:** Konzeptioneller Vorschlag ohne Produktionsvergleich; vier/fünf Schichten uneinheitlich; Contact Sheet ersetzt Playback nicht [Rohtext](<../00_Inbox/Quellen/X/2026-10-01-0xwhrrari-2105643919119696297.md>) · [Original](<https://x.com/0xwhrrari/status/2105643919119696297>)

**Q0384 · 2026-10-01 · [GPT-6.1 Sol verschiebt die Kosten-Pareto-Grenze, Bildencoding-Fix hebt GPT-6 Luna](<../80_Knowledge/Sources/2026-10-01-artificialanlys-2105491868608004578.md>)**

Auch technische Bildencoding-Fehler können Benchmarkwerte verändern, weshalb Messstand und Eingabepipeline dokumentiert gehören. **Grenze:** Keine heutige Modell- oder Preisempfehlung; Pareto-Aussage gilt nur im untersuchten Vergleich [Rohtext](<../00_Inbox/Quellen/X/2026-10-01-artificialanlys-2105491868608004578.md>) · [Original](<https://x.com/ArtificialAnlys/status/2105491868608004578>)

**Q0385 · 2026-10-01 · [Claude-Code-Mods erweitern Plugins um ausführbare Funktionen](<../80_Knowledge/Sources/2026-10-01-claudedevs-2105721434807083061.md>)**

Ausführbare Mods verändern Verhalten und Oberfläche und besitzen laut Ankündigung denselben Rechnerzugriff wie der Agent. **Grenze:** Herkunftsvertrauen und Inhaltsprüfung vor Installation; historische Herstellerankündigung [Rohtext](<../00_Inbox/Quellen/X/2026-10-01-claudedevs-2105721434807083061.md>) · [Original](<https://x.com/ClaudeDevs/status/2105721434807083061>)

**Q0386 · 2026-10-01 · [Agenten einsetzen heißt Kontext, Zugriffe und Ergebnisse beurteilen](<../80_Knowledge/Sources/2026-10-01-floknowsai-diese-faehigkeiten-helfen-dir-2026-bei-deiner-arbeit-mit-ki-damit-du.md>)**

Agentennutzung verlangt eigene Beurteilung von Zielerreichung, Belegen und Grenzen neben Kenntnissen über Modelle und Harness. **Grenze:** Empfehlung ohne Wirksamkeitsmessung; Kontextverschlechterung nicht allgemein quantifiziert; automatische Untertitel [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-01-floknowsai-diese-faehigkeiten-helfen-dir-2026-bei-deiner-arbeit-mit-ki-damit-du.md>) · [Original](<https://www.tiktok.com/@floknowsai/video/7691751929990450464>)

**Q0387 · 2026-10-01 · [Motion Graphics als veränderbarer Code](<../80_Knowledge/Sources/2026-10-01-julian-ivanov-ki-automat-claude-code-ist-unglaublich-gut-in-motion-graphi.md>)**

Codebasierte Videos erlauben gezielte Änderungen an Timing, Farben, Layout und einzelnen Szenen, wenn Inhalt und gestalterische Referenzen klar vorliegen. **Grenze:** Creator-Selbstbericht mit Sponsoring und ASR, keine vergleichende Qualitäts- oder Kostenevaluation; Werbeaussagen zu Produkten und Rechten bleiben ungeprüft. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-01-julian-ivanov-ki-automat-claude-code-ist-unglaublich-gut-in-motion-graphi.md>) · [Original](<https://www.youtube.com/watch?v=Vc0lLq3SVlw>)

**Q0388 · 2026-10-01 · [Abstraktionswert über entfernte Komplexität beurteilen](<../80_Knowledge/Sources/2026-10-01-mattpocockuk-2105563604384915639.md>)**

Der Deletion Test fragt, ob beim gedachten Entfernen eines Moduls Komplexität verschwindet oder sich in dessen Aufrufer zurückverlagert. **Grenze:** Gedanklicher Prüfschritt, keine Löschfreigabe; behauptete Tokeneffizienz ist nicht gemessen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-01-mattpocockuk-2105563604384915639.md>) · [Original](<https://x.com/mattpocockuk/status/2105563604384915639>)

**Q0389 · 2026-10-02 · [Sonnet 5.5 startet auf Rang 3 der Agent Arena](<../80_Knowledge/Sources/2026-10-02-arena-2106104809514516541.md>)**

Eine günstigere Modellfamilie kann bei hohem Effort teurere Aufgaben erzeugen als ein größeres Modell mit niedrigerem Effort. **Grenze:** Historische Rangliste ohne vollständige Methodenangaben; unklarer Generationenvergleich [Rohtext](<../00_Inbox/Quellen/X/2026-10-02-arena-2106104809514516541.md>) · [Original](<https://x.com/arena/status/2106104809514516541>)

**Q0390 · 2026-10-02 · [Arena-Snapshot besitzt eigene Messgrenzen](<../80_Knowledge/Sources/2026-10-02-arena-2106105400487821764.md>)**

Die Agent-Arena-Paretofront vergleicht gemessene Verbesserung und mediane Aufgabenpreise in einem datierten Zeitfenster. **Grenze:** Widersprüchliche Beschriftung des Spitzenmodells in benachbarten Grafiken bleibt offen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-02-arena-2106105400487821764.md>) · [Original](<https://x.com/arena/status/2106105400487821764>)

**Q0391 · 2026-10-02 · [GPT-6.1 Sol erreicht die Agent-Arena-Paretofront](<../80_Knowledge/Sources/2026-10-02-arena-2106109027923140928.md>)**

Arena-Scores und mediane Aufgabenkosten können kostengünstige Alternativen zur Spitze sichtbar machen, sofern das konkrete Messsystem und sein Zeitraum mitberücksichtigt werden. **Grenze:** Harness-Version und Stichprobe fehlen; zwei gleichzeitige Arena-Snapshots zeigen einen Nebenpunkt unterschiedlich, und die berichteten Abstände sind kein genereller Qualitätsunterschied. [Rohtext](<../00_Inbox/Quellen/X/2026-10-02-arena-2106109027923140928.md>) · [Original](<https://x.com/arena/status/2106109027923140928>)

**Q0392 · 2026-10-02 · [Coding-Agenten als Modell-Harness-Kombination vergleichen](<../80_Knowledge/Sources/2026-10-02-artificialanlys-2105814318294114720.md>)**

Der Coding Agent Index bewertet Kombinationen aus Modell und Harness, deren Score und API-Aufgabenpreis deutlich auseinanderliegen können. **Grenze:** Drittanbieter-Snapshot vom Oktober 2026, keine allgemeine Rangfolge für heutige Projektarbeit. [Rohtext](<../00_Inbox/Quellen/X/2026-10-02-artificialanlys-2105814318294114720.md>) · [Original](<https://x.com/ArtificialAnlys/status/2105814318294114720>)

**Q0393 · 2026-10-02 · [Modellauswahl nach Fähigkeit, Tokenkosten und Latenz vergleichen](<../80_Knowledge/Sources/2026-10-02-artificialanlys-2106165480876863549.md>)**

Modellauswahl sollte Aufgabenfähigkeit, einzelne Benchmarks, Input-, Output- und Cache-Kosten sowie Latenz und Ausgabegeschwindigkeit getrennt vergleichen. **Grenze:** Die Werkzeugankündigung belegt Vergleichsdimensionen, aber keine konkrete Rangfolge oder Eignung für eigene Arbeitsaufgaben. [Rohtext](<../00_Inbox/Quellen/X/2026-10-02-artificialanlys-2106165480876863549.md>) · [Original](<https://x.com/ArtificialAnlys/status/2106165480876863549>)

**Q0394 · 2026-10-02 · [API-Migration nach Fähigkeiten und Arbeitslast prüfen](<../80_Knowledge/Sources/2026-10-02-developers-using-gpt-6-openai-api.md>)**

Der archivierte OpenAI-Leitfaden trennt Modell, Effort, Reasoning-Modus, Tool-Orchestrierung und Cache und empfiehlt Vergleiche auf repräsentativen Aufgaben. **Grenze:** Lebende Dokumentation mit unsicherem Datum und Herstelleraussagen; Parameter-, Residency- und Preisbedingungen sind nur Archivstand. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-02-developers-using-gpt-6-openai-api.md>) · [Original](<https://developers.openai.com/api/docs/guides/latest-model>)

**Q0395 · 2026-10-02 · [Agentenumgebung als Produktivitätshebel](<../80_Knowledge/Sources/2026-10-02-matt-pocock-live-poteto-creator-of-pstack-on-shipping-1-000.md>)**

Lauren Tan beschreibt eine Kombination aus ausführbarer Verifikation, wiederverwendbaren CLIs, eingeschränkten Architekturpfaden und gebündelten Nutzerbefunden als Grundlage höherer Agentenautonomie. **Grenze:** PR-Zahlen und automatische Merges sind Selbstberichte, viele Änderungen betreffen Pflege; gute Verifikation macht irreversible Wirkungen nicht rückgängig. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-02-matt-pocock-live-poteto-creator-of-pstack-on-shipping-1-000.md>) · [Original](<https://www.youtube.com/watch?v=MN9dGgmLyso>)

**Q0396 · 2026-10-02 · [Claude Code 2.1.287: Claude Mods, „You should know“ und der diff-Mod](<../80_Knowledge/Sources/2026-10-02-repo-anthropics-claude-code.md>)**

Die Repository-Notiz beschreibt Mods als Hook-basierte Erweiterung mit eingebauter Diffansicht und weiteren konfigurierbaren Funktionen. **Grenze:** Keine erneute Code- oder Funktionsprüfung durch diese Quellenlektüre; Telemetriebedingung eines Features [Original](<https://github.com/anthropics/claude-code>)

**Q0397 · 2026-10-02 · [Eval-Workflow in Skills operationalisieren](<../80_Knowledge/Sources/2026-10-02-repo-anthropics-skills.md>)**

Die Repo-Notiz beschreibt getrennte Flows für Eval-Aufbau, Audit, Qualitätsoptimierung und Kostensuche. **Grenze:** Abgeleitete Repo-Notiz, keine hier ausgeführte Pipeline oder unabhängige Wirkungsmessung. [Original](<https://github.com/anthropics/skills>)

**Q0398 · 2026-10-02 · [cc-switch: Stack-Modus hängt Drittanbieter-Modelle an Claude Code und Codex](<../80_Knowledge/Sources/2026-10-02-repo-farion1231-cc-switch.md>)**

Ein gemeinsames Client-Menü kann unterschiedliche Modellanbieter zugänglich machen, wobei aktivierter Routingmodus, Hintergrundmodell und vollständiger Neustart das tatsächliche Verhalten bestimmen. **Grenze:** Die Notiz beruht nur auf UI-Texten eines bestimmten Commits von cc-switch; Stack-Modus und lokales Routing schließen sich dort aus, Laufzeitverhalten wurde nicht geprüft. [Original](<https://github.com/farion1231/cc-switch>)

**Q0399 · 2026-10-02 · [Testwert statt Testanzahl](<../80_Knowledge/Sources/2026-10-02-repo-garrytan-gstack.md>)**

Die Test Value Bar beurteilt Tests danach, welche echte Regression sie erkennen und welcher stärkere Nachweis bei ihrer Stilllegung bestehen bleibt. **Grenze:** Repo-Notiz beschreibt ein Verfahren, keinen eigenen Treffergenauigkeitstest. [Original](<https://github.com/garrytan/gstack>)

**Q0400 · 2026-10-02 · [Motion-Scores als gezielte Hilfsmetrik](<../80_Knowledge/Sources/2026-10-02-repo-jakubantalik-transitions-dev.md>)**

Der Transitions-Agent beschreibt Scans auf inkonsistente Animationswerte und die Zuordnung zu Rezepten mit überprüfbaren Diffs. **Grenze:** Repo-Selbstbeschreibung; Konto-, Lizenz- und Angebotsangaben sind datiert und nicht selbst getestet. [Original](<https://github.com/Jakubantalik/transitions.dev>)

**Q0401 · 2026-10-02 · [brag: `/brag` macht aus dem eigenen Projekt ein kurzes Launch-Video](<../80_Knowledge/Sources/2026-10-02-repo-latent-spaces-brag.md>)**

Ein wiederverwendbarer Launch-Video-Skill kann Projektinhalt, Motion, Musik und Share-Texte als Produktionsablauf bündeln. **Grenze:** Repo-Notiz aus README-Lektüre ohne Ausführung oder Ergebnisbewertung; brag-slim nutzt laut historischem Stand einen anderen Ablauf als die klassische HyperFrames-Variante. [Original](<https://github.com/latent-spaces/brag>)

**Q0402 · 2026-10-02 · [mattpocock/skills: implement-spec, pr und retro sind stabil, CONTEXT.md heißt jetzt GLOSSARY.md](<../80_Knowledge/Sources/2026-10-02-repo-mattpocock-skills.md>)**

Eine zusammenhängende Skillkette kann Spezifikation, Tickets, Umsetzung, PR und Retrospektive verbinden und benötigt konsistente Artefaktnamen. **Grenze:** Datierter abgeleiteter Repo-Befund; keine Ausführung; alte Dateinamen können Navigation brechen [Original](<https://github.com/mattpocock/skills>) · Gleiche angegebene Herkunft: Q0204.

**Q0403 · 2026-10-02 · [Front-End-Checklist: CLI `@frontendchecklist/cli` mit Offline-Regeln und MCP-Server](<../80_Knowledge/Sources/2026-10-02-repo-thedaviddias-front-end-checklist.md>)**

Ein lokaler Regelkatalog kann Frontend-Reviews und CI-Ausgaben standardisieren, doch allgemeine Treffer ersetzen kein Produktreview. **Grenze:** Nur dokumentierter historischer Funktionsumfang; keine eigene Ausführung [Original](<https://github.com/thedaviddias/Front-End-Checklist>)

**Q0404 · 2026-10-02 · [Gute Motion-Filme entstehen aus Brief, Timeline und überprüfter Iteration](<../80_Knowledge/Sources/2026-10-02-seeconvm-2106096193235259564.md>)**

Reproduzierbare codebasierte Motion-Produktion verbindet direkte Zeitadressierung, begründete Storybeats, echte Produkt-Assets, gemeinsame Bild-Ton-Timeline und wiederholte Prüfung gerenderter Evidenz. **Grenze:** Creator-Zeiten und Kostenvorteile sind sekundär berichtet; Kontaktbögen und agentische Selbstkritik ersetzen weder den vollständigen Film mit Ton noch unabhängige Produkt- und Markenabnahme. [Rohtext](<../00_Inbox/Quellen/X/2026-10-02-seeconvm-2106096193235259564.md>) · [Original](<https://x.com/seeconvm/status/2106096193235259564>)

**Q0405 · 2026-10-02 · [Wartung von Agent-Code und Agent-Konfiguration unterscheiden](<../80_Knowledge/Sources/2026-10-02-voxyz_ai-2106006290954592332.md>)**

Codebereinigung, lesendes Fehlerreview und Pflege der Agent-Konfiguration sind getrennte Wartungsaufgaben mit eigenen Nachweisen. **Grenze:** Kalender begründet keine automatische Änderung oder Freigabe; nicht alle Befehlswirkungen verifiziert [Rohtext](<../00_Inbox/Quellen/X/2026-10-02-voxyz_ai-2106006290954592332.md>) · [Original](<https://x.com/Voxyz_ai/status/2106006290954592332>)

**Q0406 · 2026-10-02 · [Kopierte Fachregeln vor einer Featureänderung vergleichen](<../80_Knowledge/Sources/2026-10-02-voxyz_ai-2106104334035435572.md>)**

Vor einer Featureänderung sollten gleiche Fachregeln über ihre Implementierungen hinweg verglichen und fachliche Korrekturen von verhaltensgleicher struktureller Konsolidierung getrennt werden. **Grenze:** Unterschiede sind nur bei tatsächlich gleichem fachlichem Kontext Widersprüche; unveränderte Assertions und textuelle Duplikatsuche beweisen weder vollständige Verhaltenserhaltung noch semantische Einmaligkeit. [Rohtext](<../00_Inbox/Quellen/X/2026-10-02-voxyz_ai-2106104334035435572.md>) · [Original](<https://x.com/Voxyz_ai/status/2106104334035435572>)

**Q0407 · 2026-10-02 · [KI-Risiken nach Mechanismus, Beleglage und Interessen prüfen](<../80_Knowledge/Sources/2026-10-02-zdfheute-nachrichten-videopodcast-droht-die-ki-apokalypse-lanz-precht.md>)**

KI-Risiken lassen sich nach erreichbaren Systemen und Schadensmechanismen beurteilen, ohne menschlichen Willen oder Bewusstsein zu unterstellen. **Grenze:** Meinungsdiskussion mit automatischem Transkript; Marketingmotiv beweist keine Falschheit einer Warnung; keine gemessenen Eintrittswahrscheinlichkeiten [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-02-zdfheute-nachrichten-videopodcast-droht-die-ki-apokalypse-lanz-precht.md>) · [Original](<https://www.youtube.com/watch?v=sFxhYEmaamA>)

**Q0408 · 2026-10-03 · [Automatisierbarkeit nach Informationszugang und implizitem Wissen betrachten](<../80_Knowledge/Sources/2026-10-03-philgueth-kaum-jemand-versteht-welche-jobs-wirklich-von-ki-bedroht-sind-ich-sprech.md>)**

Die Automatisierbarkeit einzelner Aufgaben lässt sich sinnvoller über Informationszugang und implizites Wissen untersuchen als allein über Berufsbezeichnungen. **Grenze:** Meinungsquelle ohne Arbeitsmarktstudie; Vorhersagen über ganze Berufe und Regulierung sind weder belastbare Prognosen noch juristische oder medizinische Empfehlungen. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-03-philgueth-kaum-jemand-versteht-welche-jobs-wirklich-von-ki-bedroht-sind-ich-sprech.md>) · [Original](<https://www.tiktok.com/@philgueth/video/7692403362586774817>)

**Q0409 · 2026-10-03 · [Agentenergebnisse durch passende Darstellungen verständlicher machen](<../80_Knowledge/Sources/2026-10-03-vincentmumme-andrej-karpathy-einer-der-fuehrenden-ki-forscher-erfinder-vom-llm-wiki.md>)**

Mit wachsender Agentenleistung wird menschliche Aufmerksamkeit zum Engpass, weshalb Darstellungsform und Ergebnisprüfung gemeinsam geplant werden sollten. **Grenze:** Sekundäre Darstellung eines Karpathy zugeschriebenen Beitrags ohne Verständlichkeitsmessung; HTML, Diagramme oder Videos können Fehler ebenso überzeugend darstellen wie richtige Zusammenhänge. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-03-vincentmumme-andrej-karpathy-einer-der-fuehrenden-ki-forscher-erfinder-vom-llm-wiki.md>) · [Original](<https://www.tiktok.com/@vincentmumme/video/7692348083379637537>)

**Q0410 · 2026-10-04 · [UI mit realistischen Extremfällen prüfen](<../80_Knowledge/Sources/2026-10-04-emilkowalski-2106752670405099523.md>)**

Lange Namen, ungewöhnliche Adressen, große Listen und Touch-Bedienung sind getrennte konkrete Prüfaufträge für robuste Oberflächen. **Grenze:** Autorenpost und Autorenrepo sind derselbe Belegstrang, kein nachgewiesener Qualitätsgewinn. [Rohtext](<../00_Inbox/Quellen/X/2026-10-04-emilkowalski-2106752670405099523.md>) · [Original](<https://x.com/emilkowalski/status/2106752670405099523>)

**Q0411 · 2026-10-04 · [Retro-Skill macht alte Agententranskripte zu Verbesserungsstoff](<../80_Knowledge/Sources/2026-10-04-mattpocockuk-2106729173511188654.md>)**

Vergangene Agententranskripte können gezielte Prozessverbesserungen liefern, und Rollenbezeichnungen eines Skills erfordern nicht automatisch besondere Agententypen. **Grenze:** Release-Ankündigung ohne gemessenen Produktivitätsgewinn; Zugriff auf Sitzungen und Issue-Tracker hängt von tatsächlich verfügbaren Harness-Werkzeugen ab. [Rohtext](<../00_Inbox/Quellen/X/2026-10-04-mattpocockuk-2106729173511188654.md>) · [Original](<https://x.com/mattpocockuk/status/2106729173511188654>)

**Q0412 · 2026-10-04 · [Skill-Updates mit lokaler Nutzung abgleichen](<../80_Knowledge/Sources/2026-10-04-mattpocockuk-2106730768789602313.md>)**

Skill-Updates sollten gegen lokale Änderungen und tatsächliche Nutzung geprüft werden, einschließlich gemeinsamer Fachbegriffe und der gewählten Update-Strategie. **Grenze:** 25 Sitzungen sind ein Promptbudget und Nutzungshäufigkeit kein Wirksamkeitsmaß; ein Plugin-Autoupdate bestätigt weder erfolgte lokale Migration noch die Erhaltung eigener Anpassungen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-04-mattpocockuk-2106730768789602313.md>) · [Original](<https://x.com/mattpocockuk/status/2106730768789602313>)

**Q0413 · 2026-10-04 · [Webseitenoptimierung mit Nutzungs- und Umsatzsignalen rückkoppeln](<../80_Knowledge/Sources/2026-10-04-promptgefluester-ich-zeig-ja-grade-wie-ich-ueber-280-webseiten-in-den-naechsten-paar.md>)**

Nutzungs- und Umsatzsignale können Websiteänderungen rückkoppeln, benötigen aber kontrollierte Änderungen und Rücknahmeregeln. **Grenze:** Keine Vergleichsgruppe oder Messdauer; Datenschutzkonformität unbelegt; automatische Untertitel [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-04-promptgefluester-ich-zeig-ja-grade-wie-ich-ueber-280-webseiten-in-den-naechsten-paar.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7692827981357518112>)

**Q0414 · 2026-10-04 · [Schlanke Agent-Regeln für Projekte ohne reale Nutzer](<../80_Knowledge/Sources/2026-10-04-voxyz_ai-2106783910055006342.md>)**

Kompakte Agent-Regeln brauchen einen expliziten Geltungsbereich und sollten Verhalten statt belangloser Darstellungsdetails prüfen. **Grenze:** Auch nutzerlose Projekte können erhaltenswerte Daten und Schnittstellen haben; kein automatisches Resetrecht; Erfahrungsbericht [Rohtext](<../00_Inbox/Quellen/X/2026-10-04-voxyz_ai-2106783910055006342.md>) · [Original](<https://x.com/Voxyz_ai/status/2106783910055006342>)

**Q0415 · 2026-10-04 · [Wiederkehrende Agentfehler durch Helper und Lint begrenzen](<../80_Knowledge/Sources/2026-10-04-voxyz_ai-2106829206134931539.md>)**

Wiederkehrende statisch erkennbare Fehler lassen sich durch passende Helper und Lintregeln mit konkreten Reparaturhinweisen aus dem bloßen Promptgedächtnis in ausführbares Feedback überführen. **Grenze:** Nur erfasste Muster bei tatsächlich ausgeführten Checks werden begrenzt; immer mehr Abstraktionen sind kein Selbstzweck und Helper samt Migration brauchen Pflege und fachliche Tests. [Rohtext](<../00_Inbox/Quellen/X/2026-10-04-voxyz_ai-2106829206134931539.md>) · [Original](<https://x.com/Voxyz_ai/status/2106829206134931539>)

**Q0416 · 2026-10-05 · [Umsetzung, PR-Beleg und Retro verbinden](<../80_Knowledge/Sources/2026-10-05-aihero-v1-3-implement-spec-pr-retro-and-glossary-md.md>)**

Pococks Release beschreibt eine Task-Graph-Ausführung auf einer Integrationsbranch, anschließendes Review und eine menschlich ausgewählte Retro der Arbeitsumgebung. **Grenze:** Ein großer gemeinsamer Branch bleibt Reviewrisiko; Autor empfiehlt deterministische Steuerung und warnt vor automatisch eskalierenden Retro-Umbauten. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-05-aihero-v1-3-implement-spec-pr-retro-and-glossary-md.md>) · [Original](<https://www.aihero.dev/skills/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md>)

**Q0417 · 2026-10-05 · [Skill-Änderungen an reale Sessions binden](<../80_Knowledge/Sources/2026-10-05-repo-alirezarezvani-skill-doctor.md>)**

Skill-doctor leitet Änderungsvorschläge aus bewerteten Sessions ab und trennt Modelllabels von deterministischer Aggregation. **Grenze:** Repo-Beschreibung ohne Ausführung; Benotungsgewichte sind Designentscheidungen und lokale Dateien garantieren allein keine datenlokale Modellverarbeitung. [Original](<https://github.com/alirezarezvani/claude-skills/tree/main/engineering/skill-doctor>)

**Q0418 · 2026-10-05 · [BMAD `bmad-retrospective`: Epic-Retro mit Quellenpflicht und Abnahmeentscheidung](<../80_Knowledge/Sources/2026-10-05-repo-bmad-method-retrospective.md>)**

Eine Retrospektive wird handlungsfähiger, wenn jeder Befund einen Beleg, eine Fallentscheidung und eine Prävention für den nächsten Lauf erhält. **Grenze:** An BMAD-Artefakte gebunden; abgeleitete Repo-Notiz ohne Ausführung [Original](<https://github.com/bmad-code-org/BMAD-METHOD/tree/main/skills/bmad-retrospective>)

**Q0419 · 2026-10-05 · [Claude Code: `/doctor`, `/skill-doctor` und `/insights` als eingebaute Diagnose](<../80_Knowledge/Sources/2026-10-05-repo-claude-code-doctor-insights.md>)**

Eingebaute Diagnosewerkzeuge können Einrichtung, Kontextkosten und Nutzung prüfen, während die Ableitung eines konkreten präventiven Checks aus einer gescheiterten Sitzung eine andere Aufgabe bleibt. **Grenze:** Die Notiz gibt einen datierten Changelog wieder und beschreibt keine ausgeführte Diagnose; ungenutzte Skills müssen nicht nutzlos sein. [Original](<https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md>) · Gleiche angegebene Herkunft: Q0329.

**Q0420 · 2026-10-05 · [gstack `/retro`: wöchentliche Engineering-Retrospektive aus der Git-Historie](<../80_Knowledge/Sources/2026-10-05-repo-garrytan-gstack-retro.md>)**

Eine Git-basierte Team-Retrospektive kann zeitliche Arbeitsmuster, Hotspots und bewusst gesetzte Abkürzungen über mehrere Wochen vergleichbar machen. **Grenze:** Commitzahl, Focus Score und PR-Größe sind Outputsignale ohne direkten Qualitäts- oder Kundennutzennachweis; das gstack-Setup bringt zusätzliche Skript- und Telemetrieabhängigkeiten mit. [Original](<https://github.com/garrytan/gstack/tree/main/retro>)

**Q0421 · 2026-10-05 · [Mechanische Wiederholungsfehler in die Umgebung verlagern](<../80_Knowledge/Sources/2026-10-05-repo-mattpocock-skills-retro.md>)**

Retro untersucht Navigation, Checks, Standards, Anweisungen, Toolkosten und Informationszugang einer tatsächlichen Session. **Grenze:** Manuell aufrufbarer Vorschlagsprozess, keine automatische Fehlerprävention bewiesen. [Original](<https://github.com/mattpocock/skills/tree/main/skills/engineering/retro>)

**Q0422 · 2026-10-05 · [React Doctor: Health-Score für React-Code als Regressionsprüfung nach jeder Änderung](<../80_Knowledge/Sources/2026-10-05-repo-millionco-react-doctor-skill.md>)**

Ein React-Diagnosewerkzeug kann Änderungen gegen statische Regeln und Laufzeitspuren prüfen, aber sein aggregierter Health-Score ersetzt keine Verhaltenstests. **Grenze:** Nur eine Repo-Notiz wurde gelesen; latest-Aufruf und extern nachgeladenes Triage-Playbook verändern die Laufzeitgrundlage ohne unveränderten Skill-Stand. [Original](<https://github.com/millionco/react-doctor/tree/main/skills/react-doctor>)

**Q0423 · 2026-10-05 · [Retro-Maßnahmen brauchen Zuständigkeit und Abschluss](<../80_Knowledge/Sources/2026-10-05-repo-squad-retro-enforcement.md>)**

Squad illustriert, dass nachvollziehbare Aufgaben mit Verantwortlichkeit und Abschlussereignissen die Umsetzung von Retro-Erkenntnissen unterstützen können. **Grenze:** Einzelfall mit 0/23 gegenüber 4/4 ist keine kontrollierte Kausalstudie; wöchentliche Blockierung kann unnötige Prozesskosten verursachen. [Original](<https://github.com/bradygaster/squad/tree/dev/templates/skills/retro-enforcement>)

**Q0424 · 2026-10-05 · [Refactoring durch Grenzen und gezielte Verhaltensprüfungen absichern](<../80_Knowledge/Sources/2026-10-05-venelin-valkov-stop-ai-code-slop-yes-you-still-need-to-refactor.md>)**

Refactoring sollte öffentliche Modulgrenzen und beobachtbares Verhalten verbessern, während notwendige Prüfungen erhalten bleiben. **Grenze:** ASR-Fachwortfehler; Selbstmessung; weniger Tests oder Kommentare allein kein Qualitätsbeweis; Produktions-YOLO-Rat nicht übernommen [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-05-venelin-valkov-stop-ai-code-slop-yes-you-still-need-to-refactor.md>) · [Original](<https://www.youtube.com/watch?v=VZ7HkHYs9Ag>)

**Q0425 · 2026-10-05 · [Handlungsbedarf gehört an den Anfang langer Agent-Berichte](<../80_Knowledge/Sources/2026-10-05-voxyz_ai-2107123654219743712.md>)**

Benötigte Zuarbeit wird verständlicher, wenn ein Bericht Handlung, Ort und erwartete Rückgabe vor Detailergebnissen nennt. **Grenze:** Persönliche Lesbarkeitserfahrung ohne Messung; fremde Lessonsregeln nicht aktiviert [Rohtext](<../00_Inbox/Quellen/X/2026-10-05-voxyz_ai-2107123654219743712.md>) · [Original](<https://x.com/Voxyz_ai/status/2107123654219743712>)

**Q0426 · 2026-10-05 · [Restkontingent in überprüfbare Optionen übersetzen](<../80_Knowledge/Sources/2026-10-05-voxyz_ai-2107214251408433365.md>)**

Ein sinnvoller Aufgabenpool nennt jeweils konkrete Änderung, Dateien, Nutzen und Fertigstellungsnachweis statt allgemeiner Optimierungswünsche. **Grenze:** Verbleibendes Abokontingent ist kein eigenständiger Arbeitsnutzen und rechtfertigt keine beliebige Pflege. [Rohtext](<../00_Inbox/Quellen/X/2026-10-05-voxyz_ai-2107214251408433365.md>) · [Original](<https://x.com/Voxyz_ai/status/2107214251408433365>)

**Q0427 · 2026-10-06 · [`Mistral Large 4 Preview`: Fähigkeiten und Kosten](<../80_Knowledge/Sources/2026-10-06-artificialanlys-2107467221421420919.md>)**

Ähnliche Gesamtindexwerte können unterschiedliche Fähigkeitsprofile und stark abweichende Aufgabenkosten verdecken. **Grenze:** Datiertes Benchmarkprofil; keine bestätigte Gewichtsveröffentlichung; einige Einzelwerte under review [Rohtext](<../00_Inbox/Quellen/X/2026-10-06-artificialanlys-2107467221421420919.md>) · [Original](<https://x.com/ArtificialAnlys/status/2107467221421420919>)

**Q0428 · 2026-10-06 · [Projektübergreifende Agentarbeit braucht Ressourcenkoordination](<../80_Knowledge/Sources/2026-10-06-promptgefluester-vielleicht-mal-zur-begruendung-warum-ich-euch-zeig-wie-ich-280-website.md>)**

Projektübergreifende Agentenarbeit benötigt neben Fachaufgaben eine eigene Ressourcenverantwortung für gleichzeitige Sessions, Nutzungslimits und Drosselung. **Grenze:** Die behaupteten 280 Relaunches und Richtlinienkonformität sind Selbstberichte ohne Abnahme; mehr Terminals belegen weder Qualität noch belegbaren Umsatz oder Kundennutzen. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-06-promptgefluester-vielleicht-mal-zur-begruendung-warum-ich-euch-zeig-wie-ich-280-website.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7693508884324977953>)

**Q0429 · 2026-10-06 · [Projektkarten zeigen Fortschritt, Blockaden und Entscheidungen](<../80_Knowledge/Sources/2026-10-06-voxyz_ai-2107455844992299272.md>)**

Eine gepflegte Projektkarte kann Meilensteine, Blockaden und Entscheidungsbedarf sichtbar machen, sofern ihr Status aus überprüfbaren Arbeitsartefakten abgeleitet wird. **Grenze:** Eine Karte ist kein Abnahmenachweis und kein vollständiger Handoff; ausbleibende Antworten dürfen nur vorab erlaubte Defaults auslösen, keine erforderliche Freigabe ersetzen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-06-voxyz_ai-2107455844992299272.md>) · [Original](<https://x.com/Voxyz_ai/status/2107455844992299272>)

**Q0430 · 2026-10-06 · [Visuelle Änderungen im gerenderten Zustand prüfen](<../80_Knowledge/Sources/2026-10-06-voxyz_ai-2107576635578855461.md>)**

Ein Live-Lokal-Vergleich sollte tatsächlichen Seiteninhalt, lange Ansichten und durch die konkrete Änderung verursachte Abweichungen untersuchen. **Grenze:** Ungetesteter Workflow-Vorschlag mit Browser-Sitzungsgrenzen, kein gemessener Modellvorteil. [Rohtext](<../00_Inbox/Quellen/X/2026-10-06-voxyz_ai-2107576635578855461.md>) · [Original](<https://x.com/Voxyz_ai/status/2107576635578855461>)

**Q0431 · 2026-10-07 · [T3 Code: Gemeinsame Oberfläche für Agenten, Dateien und Review](<../80_Knowledge/Sources/2026-10-07-alex-sprogis-t3-code-endlich-eine-steuerzentrale-fuer-alle-de.md>)**

Eine gemeinsame Oberfläche für Sessions, Dateien, Diffs und Browser senkt den Navigationsaufwand, während Aufgabenabgrenzung, Isolation und Freigabemodus eigenständige Entscheidungen bleiben. **Grenze:** Nightly-Demo eines Alpha-Produkts mit weitreichendem Standardzugriff; CLI-Nutzung beweist weder Abo-Zulässigkeit noch verhindert ein Automodus alle destruktiven Aktionen. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-07-alex-sprogis-t3-code-endlich-eine-steuerzentrale-fuer-alle-de.md>) · [Original](<https://www.youtube.com/watch?v=ZNQ5Jdn-CwE>)

**Q0432 · 2026-10-07 · [Kontextstaffeln verändern kleine Modellkosten](<../80_Knowledge/Sources/2026-10-07-artificialanlys-2107911905822351609.md>)**

Die Haiku-5.5-Messung zeigt, dass längenabhängige Preise, Effort und Ausgabetoken auch bei einem kleinen Modell gemeinsam betrachtet werden müssen. **Grenze:** Datierte Drittanbietermessung mit angekündigter Wiederholung nach Verweigerungsproblem. [Rohtext](<../00_Inbox/Quellen/X/2026-10-07-artificialanlys-2107911905822351609.md>) · [Original](<https://x.com/ArtificialAnlys/status/2107911905822351609>)

**Q0433 · 2026-10-07 · [Forschungsagenten als Anlass für eine Debatte über Arbeit und Verteilung](<../80_Knowledge/Sources/2026-10-07-kimmonismus-2107804082106782041.md>)**

Wissenschaftliche Agentenergebnisse sind Anlass für Fragen zu Arbeit und Verteilung, belegen aber keine allgemeine Intelligenzexplosion. **Grenze:** Keine Primärprüfung mathematischer Beweise; keine belegte gesamtwirtschaftliche Arbeitsmarktprognose [Rohtext](<../00_Inbox/Quellen/X/2026-10-07-kimmonismus-2107804082106782041.md>) · [Original](<https://x.com/kimmonismus/status/2107804082106782041>)

**Q0434 · 2026-10-07 · [Haiku 5.5: Herstellervergleich und gemeldete Betriebskosten](<../80_Knowledge/Sources/2026-10-07-kimmonismus-2107894978332557756.md>)**

Einstellbarer Effort und Cache-Tarife sind getrennte Hebel der Modellkosten und sollten an eigenen Aufgaben statt an pauschalen Qualitätsurteilen bewertet werden. **Grenze:** Sekundäre Wiedergabe einer Herstellervergleichstabelle; 75 Prozent Betriebskostenersparnis ist keine universelle Tokenpreissenkung und abweichende Terminal-Bench-Setups dürfen nicht vermischt werden. [Rohtext](<../00_Inbox/Quellen/X/2026-10-07-kimmonismus-2107894978332557756.md>) · [Original](<https://x.com/kimmonismus/status/2107894978332557756>)

**Q0435 · 2026-10-07 · [OpenAI kündigt GPT-6 mit interaktiven Antworten in ChatGPT an](<../80_Knowledge/Sources/2026-10-07-openai-2107894997538525580.md>)**

Interaktive Antworten sind eine andere Produktoberfläche und belegen keine Änderung der Modelle in Work oder Codex. **Grenze:** Historische Herstellerankündigung ohne Lern- oder Produktivitätsmessung [Rohtext](<../00_Inbox/Quellen/X/2026-10-07-openai-2107894997538525580.md>) · [Original](<https://x.com/OpenAI/status/2107894997538525580>)

**Q0436 · 2026-10-07 · [Decision-Modell als begrenzter Antwortraum](<../00_Inbox/Quellen/X/2026-10-07-unslothai-2107868866361930236.md>)**

Unsloth kündigt Fine-Tuning kleiner Backbones mit zusätzlichem Decision-Head zur Bewertung vorgegebener Optionen an. **Grenze:** Herstellerbenchmark ohne unabhängige Reproduktion; dieser Rohpost und die folgende Source-Notiz bilden denselben Belegstrang. [Original](<https://x.com/UnslothAI/status/2107868866361930236>) · Gleiche angegebene Herkunft: Q0437.

**Q0437 · 2026-10-07 · [Trainings- und Benchmarkkonfigurationen nicht vermischen](<../80_Knowledge/Sources/2026-10-07-unslothai-decision-model-finetuning.md>)**

Die Unsloth-Notiz trennt aggregierte, datensatzbezogene und Holdout-Accuracy sowie abweichende LoRA-Ränge und Epochenzahlen im Guide. **Grenze:** Identische Originalquelle wie weitere Fassungen im Bestand, nicht unabhängig; keine lokale Codeprüfung des nicht geklonten Repos. [Original](<https://x.com/UnslothAI/status/2107868866361930236>) · Gleiche angegebene Herkunft: Q0436.

**Q0438 · 2026-10-07 · [Agent-Dateien verschlanken und Spezialregeln gezielt laden](<../80_Knowledge/Sources/2026-10-07-voxyz_ai-2107939019091005836.md>)**

Universelle Agentenregeln sollten knapp und stets verfügbar bleiben, während bereichsspezifisches Wissen mit explizitem Leseanlass ausgelagert und auf tatsächlich geladene Inhalte geprüft wird. **Grenze:** 200 Zeilen sind eine Heuristik, während 32 KiB einen datierten gemeinsamen Codex-Standard bezeichnet; behauptete dynamische Ladezeitpunkte bleiben teils unverifiziert und reine Imports verkürzen nicht zwingend den Modellkontext. [Rohtext](<../00_Inbox/Quellen/X/2026-10-07-voxyz_ai-2107939019091005836.md>) · [Original](<https://x.com/Voxyz_ai/status/2107939019091005836>)

**Q0439 · 2026-10-08 · [Technische Rekonstruierbarkeit beweist keinen Zusammenbruch proprietärer Software](<../80_Knowledge/Sources/2026-10-08-heise-dekompilierung-per-ki-warum-closed-source-laut-r.md>)**

Technische Rekonstruktion, vollständiger Produktreplacement und Zusammenbruch eines Geschäftsmodells sind getrennte Behauptungen. **Grenze:** Sekundärbericht mit Hörensagen; kein Skalierungstest; Rechtsdarstellung ungeprüft [Rohtext](<../00_Inbox/Quellen/URL/2026-10-08-heise-dekompilierung-per-ki-warum-closed-source-laut-r.md>) · [Original](<https://www.heise.de/news/Open-Source-Papst-Raymond-KI-setzt-Closed-Source-Software-ein-Ende-11480624.html>)

**Q0440 · 2026-10-08 · [Erst den Umfang klären, dann den passenden Workflow wählen](<../80_Knowledge/Sources/2026-10-08-mattpocockuk-2108216899439894574.md>)**

Planungsaufwand sollte mit Missverständnisrisiko und erwarteter Nacharbeit wachsen: kleine überprüfbare Änderungen können direkt entstehen, unbekannter Umfang braucht Klärung, visuelle Präzision oft schnelle Prototypen. **Grenze:** Die Heuristik ersetzt keine Risikobewertung, denn auch ein kleiner Diff kann kritisch sein; die Entscheidung für menschliches Review bleibt von der Vorabklärung getrennt. [Rohtext](<../00_Inbox/Quellen/X/2026-10-08-mattpocockuk-2108216899439894574.md>) · [Original](<https://x.com/mattpocockuk/status/2108216899439894574>)

**Q0441 · 2026-10-08 · [Idiomatischen Agent-Code mit Framework-Quellcode und Prüfschleifen unterstützen](<../80_Knowledge/Sources/2026-10-08-moritz-brandes-sauberer-code-mit-claude-code-so-geht-s-wirklich.md>)**

Lokale Framework-Checkouts können idiomatische Muster zeigen, müssen aber zur eingesetzten Version und öffentlichen API passen. **Grenze:** Erfahrungsbericht mit ASR-Fehlern; Stackvorteile ungemessen; Hauptbranch kann installierte Version verfehlen [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-08-moritz-brandes-sauberer-code-mit-claude-code-so-geht-s-wirklich.md>) · [Original](<https://www.youtube.com/watch?v=3gmpWRVeTI8>)

**Q0442 · 2026-10-08 · [Sandboxing in Unsloth \| Unsloth Documentation](<../00_Inbox/Quellen/URL/2026-10-08-unsloth-sandboxing-in-unsloth-unsloth-documentation.md>)**

Unsloth unterscheidet String-/AST-Filter von plattformspezifischer OS-Isolation und nennt Ressourcenbegrenzungen für Werkzeugaufrufe. **Grenze:** OS-Level allein keine Garantie gegen Schaden; Latenzangaben uneinheitlich; Vorschau-/Plattformgrenzen separat prüfen [Original](<https://unsloth.ai/docs/new/studio/sandboxing-in-unsloth>)

**Q0443 · 2026-10-08 · [Decision-Training braucht eigene Kalibrierung](<../00_Inbox/Quellen/URL/2026-10-08-unsloth-train-your-own-decision-model-with-unsloth-unslo.md>)**

Der Unsloth-Guide beschreibt einen zusätzlichen Kopf, der Optionen gemeinsam bewertet, und einen von Trainingsdaten getrennten Kalibrierungsschritt. **Grenze:** Herstellerdokumentation mit abweichenden Benchmark- und Beispielparametern; einige Codeblöcke fehlen in der Extraktion, keine exakte Reproduktion ableitbar. [Original](<https://unsloth.ai/docs/basics/train-your-own-decision-model-with-unsloth>)

**Q0444 · 2026-10-08 · [Unsloth AI (@UnslothAI)](<../00_Inbox/Quellen/X/2026-10-08-unslothai-2108229721159053557.md>)**

Der Unsloth-Post kündigt Windows-Sandboxing über MXC an und liefert allein keinen Nachweis der tatsächlichen Isolation. **Grenze:** Historische Herstellerankündigung; Guide und Post keine unabhängigen Belege [Original](<https://x.com/UnslothAI/status/2108229721159053557>) · Gleiche angegebene Herkunft: Q0445.

**Q0445 · 2026-10-08 · [Freigabe, Softwarefilter und Isolation getrennt betrachten](<../80_Knowledge/Sources/2026-10-08-unslothai-windows-sandboxing-mxc.md>)**

Die Unsloth-Sandbox-Notiz unterscheidet Toolfilter, plattformspezifische OS-Isolation und den Modus der vorherigen Freigabe. **Grenze:** Widersprüchliche Latenzangaben und zusätzliche Windows-Buildvoraussetzungen; keine lokale Code-Verifikation. [Original](<https://x.com/UnslothAI/status/2108229721159053557>) · Gleiche angegebene Herkunft: Q0444.

**Q0446 · 2026-10-08 · [Vox (@Voxyz_ai)](<../00_Inbox/Quellen/X/2026-10-08-voxyz_ai-2108301411188408794.md>)**

Lesende Rollen können separat günstiger konfiguriert werden, während ein stärkerer Worker Änderungen und Tests übernimmt. **Grenze:** Herstellerdemo aus zweiter Hand; keine eigene Konfigurationsprüfung; globale Einstellungen nicht ungefragt übernehmen [Original](<https://x.com/Voxyz_ai/status/2108301411188408794>) · Gleiche angegebene Herkunft: Q0448.

**Q0447 · 2026-10-08 · [Scrollanimationen benennen und abnehmen](<../80_Knowledge/Sources/2026-10-08-voxyz_ai-2108324058739745228.md>)**

Scrollanimationen lassen sich präziser über Auslöser, Scrollbindung und Layoutverhalten spezifizieren und müssen einen Zweck, mobile Alternative sowie zugänglichen Reduced-Motion-Fallback erhalten. **Grenze:** Ein Glossar und Screenshots ersetzen keine vollständige Browserprüfung; Begriffe wie Horizontal Scroll sind im Beitrag enger verwendet als allgemein üblich und die Wirkung bleibt ungemessen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-08-voxyz_ai-2108324058739745228.md>) · [Original](<https://x.com/Voxyz_ai/status/2108324058739745228>)

**Q0448 · 2026-10-08 · [Aktive Agentenkonfiguration statt Rollenbild prüfen](<../80_Knowledge/Sources/2026-10-08-voxyz_ai-haiku-subagents-und-opus-worker.md>)**

Modell und Effort sollten pro delegierter Aufgabe ausdrücklich gewählt und gegen Vererbung, Projektpriorität und Umgebungsvariablen kontrolliert werden. **Grenze:** Datierte Sekundäranleitung; Mindestversion und Preisvorteile sind nicht vollständig am lokalen Stand bestätigt. [Original](<https://x.com/Voxyz_ai/status/2108301411188408794>) · Gleiche angegebene Herkunft: Q0446.

**Q0449 · 2026-10-09 · [Launch-Videos werden durch Ereignisframes und begrenzte Reparaturen abnehmbar](<../80_Knowledge/Sources/2026-10-09-beamnxw-2108616740846420354.md>)**

Eine begrenzte Filmkorrektur benennt Ort, sichtbaren Fehler, konkrete Änderung und unveränderliche Elemente. **Grenze:** Kein Kunden- oder Wirtschaftlichkeitsnachweis; Pilotpreis hypothetisch; widersprüchliche Beispiel-Timelines; fehlende Befehlsblöcke [Rohtext](<../00_Inbox/Quellen/X/2026-10-09-beamnxw-2108616740846420354.md>) · [Original](<https://x.com/beamnxw/status/2108616740846420354>)

**Q0450 · 2026-10-09 · [Kontext ist eine reale Speicherentscheidung](<../00_Inbox/Quellen/URL/2026-10-09-docs-ollama-kontextlaenge-und-speicherbedarf.md>)**

Ollamas archivierte Dokumentation macht deutlich, dass größeres Kontextfenster den Speicherbedarf erhöht und die effektiv zugeteilte Länge sowie Offloading geprüft werden sollten. **Grenze:** Lebende Herstellerdokumentation mit Erfassungsdatum statt gesichertem Veröffentlichungsdatum; maximale Länge ist kein universelles Optimum. [Original](<https://docs.ollama.com/context-length>) · Gleiche angegebene Herkunft: Q0459.

**Q0451 · 2026-10-09 · [Git Worktree: Getrennte Arbeitsverzeichnisse](<../00_Inbox/Quellen/URL/2026-10-09-git-scm-git-worktree-getrennte-arbeitsverzeichnisse.md>)**

Git-Worktrees trennen Arbeitsverzeichnisse und Indexzustände, teilen aber Repositoryobjekte und die meisten Referenzen. **Grenze:** Worktree ist keine Sicherheitsisolation; Submodule eingeschränkt; Abrufdatum unsicher; gemeinsame Konfiguration beachten [Original](<https://git-scm.com/docs/git-worktree>) · Gleiche angegebene Herkunft: Q0452.

**Q0452 · 2026-10-09 · [Git Worktrees isolieren Arbeitsverzeichnisse innerhalb eines Repositories](<../80_Knowledge/Sources/2026-10-09-git-worktree.md>)**

Git Worktrees trennen Arbeitsdateien, Index und HEAD mehrerer Checkouts, teilen aber zentrale Repository-Daten und erfordern weiterhin koordinierte Integration. **Grenze:** Die gelesene Notiz fasst offizielle Dokumentation zusammen; Worktrees isolieren weder externe Datenbanken und Ports noch fachliche Konflikte gemeinsamer Schnittstellen. [Original](<https://git-scm.com/docs/git-worktree>) · Gleiche angegebene Herkunft: Q0451.

**Q0453 · 2026-10-09 · [Website-Workflow: Suchdaten und Texte vor Design, danach getrennte Abnahme](<../80_Knowledge/Sources/2026-10-09-julian-ivanov-ki-automat-websites-mit-ki-bauen-die-gut-aussehen-und-perfo.md>)**

Ein Websiteprozess kann Angebot, Suchdaten und Texte vor die Designentscheidung stellen und den Fortschritt in Dateien über Sessions tragen. **Grenze:** Sponsoring und automatische Untertitel; rechtliche Seiten ungeprüft; Domainverfügbarkeit keine Markenfreigabe; Search-Console-Anmeldung garantiert kein Ranking [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-09-julian-ivanov-ki-automat-websites-mit-ki-bauen-die-gut-aussehen-und-perfo.md>) · [Original](<https://www.youtube.com/watch?v=xfPTagIR60Q>)

**Q0454 · 2026-10-09 · [Arbeitsmarktmeinung von Belegen unterscheiden](<../00_Inbox/Quellen/X/2026-10-09-karl_lauterbach-2108478065072374233.md>)**

Der Post äußert eine zugespitzte Sorge über die Entwertung akademischer Arbeit durch KI. **Grenze:** Meinung und Prognose, keine belegte Arbeitsmarktentwicklung. [Original](<https://x.com/Karl_Lauterbach/status/2108478065072374233>)

**Q0455 · 2026-10-09 · [Codex: Einen bestehenden Codepfad verstehen](<../00_Inbox/Quellen/URL/2026-10-09-learn-codex-einen-bestehenden-codepfad-verstehen.md>)**

Vor einer Änderung sollte der konkrete Codepfad mit Zuständigkeiten, Validierung, Seiteneffekten und verdeckten Abhängigkeiten nachvollzogen werden. **Grenze:** Vorgehensbeschreibung ohne Wirksamkeitsmessung; teilweise fehlende Promptfelder im Export [Original](<https://learn.chatgpt.com/use-cases/codebase-onboarding>) · Gleiche angegebene Herkunft: Q0460.

**Q0456 · 2026-10-09 · [Codex: Verhalten bei Refactoring erhalten](<../00_Inbox/Quellen/URL/2026-10-09-learn-codex-verhalten-bei-refactoring-erhalten.md>)**

Refactoring wird reviewbar, wenn pro kleinem Schritt bisheriges Verhalten, Strukturziel und kleinste aussagekräftige Prüfung feststehen. **Grenze:** Herstelleranleitung ohne Erfolgsquote; kleiner Check muss das vereinbarte Verhalten tatsächlich abdecken [Original](<https://learn.chatgpt.com/use-cases/refactor-your-codebase>) · Gleiche angegebene Herkunft: Q0461.

**Q0457 · 2026-10-09 · [KI-Einführung mit Verantwortlichen und laufender Befähigung betreiben](<../80_Knowledge/Sources/2026-10-09-lukepierceops-2108655186080342138.md>)**

Dauerhafte KI-Adoption braucht benannte Verantwortung, geschützte Lernzeit, rollenbezogene Übungen an echter Arbeit und eine regelmäßig geprüfte Wissensbibliothek. **Grenze:** Beratungsmarketing mit selbstberichteten Erfahrungen aus achtzig Unternehmen ohne auswertbare Ergebnisdaten; Nutzung, geschätzte Zeitersparnis und tatsächliche Unternehmenswirkung sind getrennt zu messen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-09-lukepierceops-2108655186080342138.md>) · [Original](<https://x.com/lukepierceops/status/2108655186080342138>)

**Q0458 · 2026-10-09 · [Modellfähigkeit und Effort sind getrennte Stellgrößen](<../80_Knowledge/Sources/2026-10-09-natebjones-thats-model-vs-effort-in-plain-english.md>)**

Jones unterscheidet das erforderliche Fähigkeitsniveau von dem zusätzlichen Rechenaufwand eines gewählten Modells. **Grenze:** Praxisheuristik und Automatisches Transkript ohne Messdaten. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-09-natebjones-thats-model-vs-effort-in-plain-english.md>) · [Original](<https://www.tiktok.com/@nate.b.jones/video/7694456013528763678>)

**Q0459 · 2026-10-09 · [Ollama: Kontextlänge braucht zusätzlichen Speicher](<../80_Knowledge/Sources/2026-10-09-ollama-kontext-speicher.md>)**

Das Speicherbudget lokaler Inferenz muss neben Modellgewichten die konfigurierte Kontextlänge und tatsächliche CPU-GPU-Zuordnung berücksichtigen. **Grenze:** Undatierter Dokumentationsstand ohne konkrete Modellmessung; 64000 Tokens sind eine Herstellerempfehlung für bestimmte Aufgaben und kein allgemeines Hardwareminimum. [Original](<https://docs.ollama.com/context-length>) · Gleiche angegebene Herkunft: Q0450.

**Q0460 · 2026-10-09 · [Einen bestehenden Codepfad mit Codex nachvollziehen](<../80_Knowledge/Sources/2026-10-09-openai-codebase-onboarding.md>)**

Vor Änderungen sollte ein begrenzter Codepfad mit Zuständigkeiten, Datenfluss, Validierung, Nebenwirkungen und passenden Checks an konkreten Dateien nachvollzogen werden. **Grenze:** Die offizielle Anleitung belegt keine Zeit- oder Qualitätsverbesserung; eingebettete Prompts fehlen im Archiv und eine gezeichnete Architektur muss gegen den tatsächlichen Code geprüft werden. [Original](<https://learn.chatgpt.com/use-cases/codebase-onboarding>) · Gleiche angegebene Herkunft: Q0455.

**Q0461 · 2026-10-09 · [Refactoring in kleinen Schritten mit stabilem Verhalten](<../80_Knowledge/Sources/2026-10-09-openai-refactoring.md>)**

Diese redaktionelle Refactoring-Notiz ist die Ableitung derselben zuvor gelesenen Herstelleranleitung und kein unabhängiger Beleg. **Grenze:** Dublettenfamilie mit gleichem Original-URL wie149; Datum ist Sichtungsdatum [Original](<https://learn.chatgpt.com/use-cases/refactor-your-codebase>) · Gleiche angegebene Herkunft: Q0456.

**Q0462 · 2026-10-09 · [`Codex` kündigt Windows-Sandboxing mit `MXC` an](<../80_Knowledge/Sources/2026-10-09-openaidevs-2108573188703781190.md>)**

Der Codex-MXC-Post kündigt granulare Datei- und Netzgrenzen für kompatible Windowsgeräte an, bestätigt aber keine konkrete Schutzwirkung. **Grenze:** Previewgrenzen anderer MXC-Quellen bleiben relevant; keine Übertragung auf alle Geräte [Rohtext](<../00_Inbox/Quellen/X/2026-10-09-openaidevs-2108573188703781190.md>) · [Original](<https://x.com/OpenAIDevs/status/2108573188703781190>)

**Q0463 · 2026-10-09 · [`Codex` schlägt Folgenachrichten in der Pro-Beta vor](<../80_Knowledge/Sources/2026-10-09-openaidevs-2108624138369929725.md>)**

Vorschläge für Folgenachrichten können den Eingabeaufwand verringern, behalten aber die menschliche Auswahl, Bearbeitung und ausdrückliche Sendung als eigene Schritte bei. **Grenze:** Datierte Pro-Beta-Ankündigung ohne Bedienungstest oder Nutzenmessung; interne Beliebtheit ist kein Nachweis besserer Arbeitsergebnisse. [Rohtext](<../00_Inbox/Quellen/X/2026-10-09-openaidevs-2108624138369929725.md>) · [Original](<https://x.com/OpenAIDevs/status/2108624138369929725>)

**Q0464 · 2026-10-09 · [Decision-Benchmarks bleiben auf ihren Antwortraum begrenzt](<../80_Knowledge/Sources/2026-10-09-openrouter-2108689756372775370.md>)**

OpenRouter gibt Microsofts Leistungs-, Robustheits- und Preisangaben eines spezialisierten Entscheidungsmodells weiter. **Grenze:** Herstellerzahlen über Drittkanal; keine unabhängige Bestätigung oder belegte Architekturidentität mit anderen Decision-Modellen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-09-openrouter-2108689756372775370.md>) · [Original](<https://x.com/OpenRouter/status/2108689756372775370>)

**Q0465 · 2026-10-09 · [Mobile-Webapps nach Eingabefähigkeit und tatsächlichem Browserverhalten prüfen](<../80_Knowledge/Sources/2026-10-09-repo-emilkowalski-mobile-native.md>)**

Mobile Webapps müssen nach Eingabefähigkeit, Viewportzuständen, sicheren Rändern und tatsächlichem Browserverhalten geprüft werden. **Grenze:** Abgeleitete datierte Repo- und Dokumentationslektüre; keine ausgeführte Geräteabnahme [Original](<https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/mobile-native/SKILL.md>)

**Q0466 · 2026-10-09 · [GSD Core strukturiert Meilensteine in fünf Phasen](<../80_Knowledge/Sources/2026-10-09-repo-gsd-workflow.md>)**

GSD hält Entscheidungen und Fortschritt in persistenten Dateien und verbindet Discuss, Plan, Execute, Verify und Ship. **Grenze:** Projektversprechen gegen Context Rot ohne eigenen Vergleich; abgeleitete Repo-Notiz [Original](<https://github.com/open-gsd/gsd-core/blob/13d37238ba08377929e4850fd6ae4b8db49a22ca/README.md>)

**Q0467 · 2026-10-09 · [gstack ordnet Entwicklung nach Rollen und überprüfbaren Übergaben](<../80_Knowledge/Sources/2026-10-09-repo-gstack-workflow.md>)**

gstack verteilt Denken, Planung, Bau, Review, Test, Lieferung und Reflexion auf Rollen mit eigenen Übergaben. **Grenze:** Leistungsversprechen keine Messung; keine Installation oder Ausführung [Original](<https://github.com/garrytan/gstack/blob/857466ff8b93c0575bc9e46cf2838d1962077d8f/README.md>)

**Q0468 · 2026-10-09 · [Workflow-Pakete nach Engpass auswählen](<../80_Knowledge/Sources/2026-10-09-repo-superpowers-workflow.md>)**

Superpowers verbindet Design, Plan, Worktrees, TDD und Review zu einem verpflichtenden Entwicklungsablauf. **Grenze:** Abgeleitete Repo-Sichtung, keine gemessene Überlegenheit des gesamten Pakets. [Original](<https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/README.md>)

**Q0469 · 2026-10-09 · [`Microsoft-Decision-1`: Ankündigung und Verfügbarkeit nach Kanal](<../80_Knowledge/Sources/2026-10-09-satyanadella-2108627923888754862.md>)**

Strukturierte Entscheidungsmodelle müssen nach Accuracy, Kalibrierung und Latenz getrennt bewertet werden. **Grenze:** Historische Herstellerzahlen; keine Reproduktion; Kanalposts mit unterschiedlichem zeitlichem Stand [Rohtext](<../00_Inbox/Quellen/X/2026-10-09-satyanadella-2108627923888754862.md>) · [Original](<https://x.com/satyanadella/status/2108627923888754862>)

**Q0470 · 2026-10-09 · [`shadcn/ui`-Skills unterstützen Designsysteme mit `DESIGN.md`](<../80_Knowledge/Sources/2026-10-09-shadcn-2108574564586332615.md>)**

Ein Designsystem kann Farben, Tokens, Typografieskala, Elevation und Komponentenstile als gemeinsame Grundlage von Agentenarbeit bereitstellen. **Grenze:** Datierte Autorenankündigung zu shadcn-Skills ohne eigene Qualitätsprüfung; ein Preset garantiert weder Einzigartigkeit noch korrektes Verhalten und Accessibility. [Rohtext](<../00_Inbox/Quellen/X/2026-10-09-shadcn-2108574564586332615.md>) · [Original](<https://x.com/shadcn/status/2108574564586332615>)

**Q0471 · 2026-10-09 · [Motion-Produktion mit Storyboard und erneuter Render-Abnahme](<../80_Knowledge/Sources/2026-10-09-voxyz_ai-2108543002830360775.md>)**

Motion-Produktionen sollten mit Kommunikationsziel und echten Projektinhalten beginnen, zentrale Parameter nutzen und nach jeder relevanten Änderung erneut gerendert und abgenommen werden. **Grenze:** Der Primärguide wurde im Ursprung nicht geprüft, und HyperFrames ist nicht als identisch mit Claude Motion belegt; eine Text- oder Zeitänderung kann auch umliegendes Layout und Timing verändern. [Rohtext](<../00_Inbox/Quellen/X/2026-10-09-voxyz_ai-2108543002830360775.md>) · [Original](<https://x.com/Voxyz_ai/status/2108543002830360775>)

**Q0472 · 2026-10-09 · [Agent-Automationen mit Quellen-Bookmarks absichern](<../80_Knowledge/Sources/2026-10-09-voxyz_ai-2108573215224160393.md>)**

Wiederkehrende Agentenaufgaben sollten Fortschritt je Quelle speichern und Lesefehler, bestätigte Zustellung, Duplikate, Kostenobergrenzen sowie minimale Rechte getrennt behandeln. **Grenze:** Bookmarks verhindern allein weder doppelte Verarbeitung noch Verluste; Atomizität, Retry und Wiederherstellung bleiben offen, und der zitierte Guide ist hier nur sekundär wiedergegeben. [Rohtext](<../00_Inbox/Quellen/X/2026-10-09-voxyz_ai-2108573215224160393.md>) · [Original](<https://x.com/Voxyz_ai/status/2108573215224160393>)

**Q0473 · 2026-10-09 · [Vor einem unbekannten Projekt Begriffe und erste Weichenstellung klären](<../80_Knowledge/Sources/2026-10-09-voxyz_ai-2108663797091127377.md>)**

Ein kleines Domänenglossar sollte erklären, welche Begriffe Anforderungen verändern und welche Frage zuerst Architektur entscheidet. **Grenze:** Tokenverbrauchsgeschichte unbestätigt; generierte Fachbegriffe selbst prüfbedürftig [Rohtext](<../00_Inbox/Quellen/X/2026-10-09-voxyz_ai-2108663797091127377.md>) · [Original](<https://x.com/Voxyz_ai/status/2108663797091127377>)

**Q0474 · 2026-10-10 · [Produktionssignale in begrenzte Lernschleifen zurückführen](<../80_Knowledge/Sources/2026-10-10-boristane-self-improving-software-is-inevitable.md>)**

Tane schlägt vor, Logs, Traces, Metriken, Replays und Support gemeinsam zu untersuchen und daraus belegte Änderungsvorschläge abzuleiten. **Grenze:** Architekturvision und Produktwerbung; Backpropagation ist Analogie, unbekannte Probleme werden nicht garantiert entdeckt und Metrikänderungen beweisen keine Kausalität. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-10-boristane-self-improving-software-is-inevitable.md>) · [Original](<https://boristane.com/blog/self-improving-software-is-inevitable/>)

**Q0475 · 2026-10-10 · [Dario Amodei — We Must Pace the Frontier](<../00_Inbox/Quellen/URL/2026-10-10-darioamodei-dario-amodei-we-must-pace-the-frontier.md>)**

Amodei fordert, Fähigkeitsfortschritt mit überprüfbaren Sicherheitsprozessen zu verbinden und dauerhaft eingebetteten externen Prüfern Zugang zu Betrieb, Trainingsumgebungen und Vorfällen zu geben. **Grenze:** Strategischer Essay eines Unternehmensleiters mit eigenen Interessen: Zukunftsrisiken und geopolitische Folgen sind Prognosen, zugesagte Prüferzugänge noch kein Nachweis ihrer Umsetzung, und das Archivdatum ist unsicher. [Original](<https://darioamodei.com/post/we-must-pace-the-frontier>)

**Q0476 · 2026-10-10 · [Lebende API-Dokumentation datiert vergleichen](<../80_Knowledge/Sources/2026-10-10-developers-using-gpt-6-openai-api.md>)**

Die zwei archivierten Fassungen des OpenAI-Guides zeigen ein konkretes Delta regionaler Verfügbarkeit zwischen Modell und Geschwindigkeitsmodus. **Grenze:** Erfassungsdatum ist kein Veröffentlichungsdatum; Herstellerdokumentation belegt keine am eigenen Account getestete Datenverarbeitung. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-10-developers-using-gpt-6-openai-api.md>) · [Original](<https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra>)

**Q0477 · 2026-10-10 · [Kontextanzeigen und Hooks mit tatsächlichen Entscheidungen verbinden](<../80_Knowledge/Sources/2026-10-10-julian-ivanov-ki-automat-diese-10-claude-code-mods-solltest-du-unbedingt.md>)**

Kontextanzeigen werden erst dann nützlich, wenn erhaltene Entscheidungen nach Komprimierung geprüft und sichtbare Warnungen von tatsächlich eingreifenden Hooks unterschieden werden. **Grenze:** Automatisches Demo-Transkript ohne kontrollierte Nutzenmessung; Cache-Fristen und Fortschrittsleisten sind keine Garantien, Keep-warm-Aufrufe kosten selbst Ressourcen und Warnhooks bilden keine vollständige Sicherheitsgrenze. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-10-julian-ivanov-ki-automat-diese-10-claude-code-mods-solltest-du-unbedingt.md>) · [Original](<https://www.youtube.com/watch?v=ji4ANdb_M6Y>)

**Q0478 · 2026-10-10 · [Codearchitektur in Perspektiven und nachvollziehbaren Detailansichten dokumentieren](<../80_Knowledge/Sources/2026-10-10-repo-oh-my-mermaid-architektur.md>)**

Architekturwissen lässt sich in passenden Perspektiven mit rekursiven Detailansichten und konkreten Codepfaden dokumentieren, ohne jeden möglichen Diagrammtyp ausfüllen zu müssen. **Grenze:** Gelesen wurde die vorhandene statische Repo-Analyse: Formatvalidatoren beweisen keine echte Architektur, und ein lokaler Viewer kann durch Netzwerkbindung, CORS, externe Assets und Cloud-Push Datenflüsse öffnen. [Original](<https://github.com/oh-my-mermaid/oh-my-mermaid/tree/38ccdb69298adec949177c92c88d6e3ddfb5bab7>)

**Q0479 · 2026-10-10 · [Modellfähigkeiten dürfen keine Autorität über ihre eigenen Kontrollen verleihen](<../80_Knowledge/Sources/2026-10-10-satyanadella-2108931348857827686.md>)**

Modellfähigkeiten dürfen keine Autorität über Zugriffskontrollen und die eigene Beweisführung verleihen. **Grenze:** Normative Architekturposition ohne Umsetzungstest; mehrere Modelle allein schaffen keine Unabhängigkeit; Superintelligence ist Rahmung [Rohtext](<../00_Inbox/Quellen/X/2026-10-10-satyanadella-2108931348857827686.md>) · [Original](<https://x.com/satyanadella/status/2108931348857827686>)

**Q0480 · 2026-10-10 · [CSS-Audit an beobachtbarem Verhalten ausrichten](<../80_Knowledge/Sources/2026-10-10-voxyz_ai-2108875199164871053.md>)**

Mobile Eingabefähigkeiten, Formularzustände, Sprungziele, Ziffernbreiten und Fokusdarstellung liefern konkrete CSS-Prüffälle. **Grenze:** Ungetesteter Auditprompt; 44-Pixel-Fläche und einzelne Techniken sind keine vollständige Barrierefreiheitsprüfung. [Rohtext](<../00_Inbox/Quellen/X/2026-10-10-voxyz_ai-2108875199164871053.md>) · [Original](<https://x.com/Voxyz_ai/status/2108875199164871053>)

**Q0481 · 2026-10-10 · [Motion-Werkzeuge nach Produktionsaufgabe vorsortieren](<../80_Knowledge/Sources/2026-10-10-voxyz_ai-2108905392776360333.md>)**

Motion-Werkzeuge sollten nach Launchfilm, Schnitt, Kurzanimation oder Webinteraktion vorsortiert werden. **Grenze:** 15 Empfehlungen ohne eigenen Qualitätsvergleich oder Installation [Rohtext](<../00_Inbox/Quellen/X/2026-10-10-voxyz_ai-2108905392776360333.md>) · [Original](<https://x.com/Voxyz_ai/status/2108905392776360333>)

**Q0482 · 2026-10-10 · [Browser-Playtesting als Bestandteil einer Game-Studio-Erweiterung](<../80_Knowledge/Sources/2026-10-10-voxyz_ai-2109026189298012522.md>)**

Ein Browsergame sollte als tatsächlicher Spielablauf getestet werden, damit Bedienung, Animation und Zustandswechsel zusätzlich zur Codeprüfung sichtbar werden. **Grenze:** Fremde Pluginempfehlung ohne geprüfte Primärdokumentation; neun Skills und autonomes Spielen belegen weder vollständige Testabdeckung noch Fehlerfreiheit. [Rohtext](<../00_Inbox/Quellen/X/2026-10-10-voxyz_ai-2109026189298012522.md>) · [Original](<https://x.com/Voxyz_ai/status/2109026189298012522>)

**Q0483 · 2026-10-10 · [Cache-Laufzeit nach tatsächlichen Agent-Pausen wählen](<../80_Knowledge/Sources/2026-10-10-voxyz_ai-2109056129884123370.md>)**

Eine längere Cache-TTL lohnt nur, wenn spätere Hits nach realen Pausen die höheren Schreibkosten rechtfertigen. **Grenze:** Historische Preise; keine gemessene Einsparung; Source-Dokumentationsabgleich nennt ignorierte per-Agent-1h bei Subscription-Usage-Credits [Rohtext](<../00_Inbox/Quellen/X/2026-10-10-voxyz_ai-2109056129884123370.md>) · [Original](<https://x.com/Voxyz_ai/status/2109056129884123370>)

**Q0484 · 2026-10-11 · [AI 2027: ein konkretes Zukunftsszenario mit offenen Annahmen](<../80_Knowledge/Sources/2026-10-11-ai-2027-ai-2027.md>)**

AI 2027 macht Rückkopplungen zwischen automatisierter Forschung, Leistungszuwachs, Kontrollproblemen und Wettbewerbsdruck als ausdrücklich hypothetisches Szenario konkret diskutierbar. **Grenze:** Fiktive Firmen und Modelle, unsicheres Archivdatum statt Originalpublikation, korrigierte Prognosekurven und spätere Mediane; das Archiv endet vor den beiden Endzweigen und belegt weder eingetretene Entwicklungen noch Schadenswahrscheinlichkeiten. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-11-ai-2027-ai-2027.md>) · [Original](<https://ai-2027.com/>)

**Q0485 · 2026-10-11 · [Ein wiederverwendbarer Agent-Harness lässt Produktverantwortung bei der Anwendung](<../80_Knowledge/Sources/2026-10-11-developers-codex-as-a-platform-build-on-the-open-agent-harn.md>)**

Ein wiederverwendbarer Agent-Harness kann Lifecycle, Kontext und Tools tragen, während die einbettende Anwendung Fachregeln, aktuelle Datensätze, Benutzeroberfläche und fachliche Freigaben verantwortet. **Grenze:** Herstellerbeschreibung mit unsicherem Publikationsdatum und fiktiver Relay-Demo; Benchmark und Steuerpilot erlauben keine eigene Leistungszusage, Open Source des Harness schließt weder Modellzugang noch Managed Services ein. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-11-developers-codex-as-a-platform-build-on-the-open-agent-harn.md>) · [Original](<https://developers.openai.com/blog/codex-as-a-platform>)

**Q0486 · 2026-10-11 · [Animation-Performance gezielt prüfen und Skills bewusst laden](<../80_Knowledge/Sources/2026-10-11-emilkowalski-2109277388437868623.md>)**

Animation-Performance braucht explizite Prüfaufgaben, und die bewusste Aktivierung spezialisierter Skills kann menschliche Steuerbarkeit unterstützen. **Grenze:** Knappe Autorenankündigung ohne Skillprüfung; Blur-, Schatten- und CSS-Variablen-Regeln sind Beispiele ohne universelle Messgrenzen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-11-emilkowalski-2109277388437868623.md>) · [Original](<https://x.com/emilkowalski/status/2109277388437868623>)

**Q0487 · 2026-10-11 · [Günstigere Nachbauten verschieben den Wert von Software](<../80_Knowledge/Sources/2026-10-11-hood-informatik-wird-code-jetzt-wertlos.md>)**

Günstigere Implementierung macht enge persönliche Werkzeuge attraktiver, während vollständige Produktparität, verlässlicher Betrieb und Wartungsverantwortung eigenständige Wertquellen bleiben. **Grenze:** Die Nachbauprojekte und Zeitangaben sind sekundär berichtet und teils frühe Alpha-Stände; unterschiedliche Spielprojekte bilden keinen kontrollierten Vergleich, rechtliche Aussagen der Quelle wurden nicht geprüft. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-11-hood-informatik-wird-code-jetzt-wertlos.md>) · [Original](<https://www.youtube.com/watch?v=l5SbBoauUNE>)

**Q0488 · 2026-10-11 · [Schnittstellenvertrag aus einer Schemaquelle ableiten](<../80_Knowledge/Sources/2026-10-11-shiptypes-ship-types-not-docs.md>)**

Versionierte Schemas können Typen, Laufzeitvalidatoren, Clients und Dokumentation gemeinsam erzeugen und in CI auf Abweichung prüfen lassen. **Grenze:** Meinungsbeitrag mit Produktwerbung und fehlerhaftem Typnamen im Beispiel; vierfache Ersparnis und Compile-garantiert-Korrektheit sind unbelegt. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-11-shiptypes-ship-types-not-docs.md>) · [Original](<https://shiptypes.com/>)

**Q0489 · 2026-10-11 · [Ein fremdes Feature mit Herkunftsbelegen untersuchen](<../80_Knowledge/Sources/2026-10-11-voxyz_ai-2109297975013081587.md>)**

Featureanalyse sollte beobachtete Dateien, Funktionen oder Adressen von Vermutungen trennen und erst danach einen minimalen Umsetzungsplan bilden. **Grenze:** Kein Rechtsschluss oder Installationsauftrag; Werkzeugfähigkeiten ungetestet [Rohtext](<../00_Inbox/Quellen/X/2026-10-11-voxyz_ai-2109297975013081587.md>) · [Original](<https://x.com/Voxyz_ai/status/2109297975013081587>)

**Q0490 · 2026-10-11 · [Backend-Prüfungen nach Risiko aufteilen und Änderungen zentral abnehmen](<../80_Knowledge/Sources/2026-10-11-voxyz_ai-2109328172273606771.md>)**

Backend-Abnahme braucht konkrete Nachweise für Zugriff, Zahlungskonsistenz, Missbrauchsschutz und Wiederherstellung. **Grenze:** Checkliste ist kein vollständiges Bedrohungsmodell; keine automatische Autorisierung zu Security-/Billingänderungen [Rohtext](<../00_Inbox/Quellen/X/2026-10-11-voxyz_ai-2109328172273606771.md>) · [Original](<https://x.com/Voxyz_ai/status/2109328172273606771>)

**Q0491 · 2026-10-11 · [Audio am fertigen Video messen und gezielt anhören](<../80_Knowledge/Sources/2026-10-11-voxyz_ai-2109358372873183564.md>)**

Audioqualität eines Motion-Videos braucht Messung des fertigen MP4-Exports, kontrollierte Synchronität und menschliche Hörprüfung zusätzlich zur visuellen Framekontrolle. **Grenze:** Die Pegel und Lizenzwahl sind Autorenempfehlungen, keine bestätigte Norm oder konkrete Nutzungsfreigabe; ein berichteter 0,22-Sekunden-Fehler und Promptbild sind kein durchgeführter Test. [Rohtext](<../00_Inbox/Quellen/X/2026-10-11-voxyz_ai-2109358372873183564.md>) · [Original](<https://x.com/Voxyz_ai/status/2109358372873183564>)

**Q0492 · 2026-10-12 · [Reverse Engineering braucht eine überprüfbare Verhaltensspezifikation](<../80_Knowledge/Sources/2026-10-12-0xcodila-2109623431763292649.md>)**

Reverse Engineering wird zu einer belastbaren Arbeitsweise, wenn begrenzte Untersuchungen belegtes Verhalten und verbleibende Unbekannte in eine Spezifikation überführen und auch die Vergleichstests geprüft werden. **Grenze:** Die lange kuratierte Quelle enthält Werbung, fremde Behauptungen und einen Jev-Handelsartikel ohne unabhängige Durchführung; kostenlos und vollständig lokal werden nicht belegt, ein Agent ist kein dokumentierter Clean Room und Rechts- sowie Renditebehauptungen werden nicht übernommen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-12-0xcodila-2109623431763292649.md>) · [Original](<https://x.com/0xCodila/status/2109623431763292649>)

**Q0493 · 2026-10-12 · [Binäranalyse mit kleinen Belegschritten und Verhaltensvergleichen steuern](<../80_Knowledge/Sources/2026-10-12-0xmovez-2109604520770548146.md>)**

Binäranalyse wird überprüfbarer durch kleine Belegschritte, gemeinsame Strukturnamen und getrennte Beobachtungen, Schlussfolgerungen und Unbekannte. **Grenze:** Clean-Room-Regel verbietet die zuvor verlangte Disassemblierung; lokale Verarbeitung sendet Befunde ans Modell; Motion-Zusatz enthält Zeitablauf als vermeintliche Zustimmung und unzureichenden Hashcheck; keine Rechtsgarantie [Rohtext](<../00_Inbox/Quellen/X/2026-10-12-0xmovez-2109604520770548146.md>) · [Original](<https://x.com/0xMovez/status/2109604520770548146>)

**Q0494 · 2026-10-12 · [Muse Wonder: höhere Benchmarkscores bei höherem Aufgabenpreis](<../80_Knowledge/Sources/2026-10-12-artificialanlys-2109697083519447118.md>)**

Geringerer Outputverbrauch kann mit höheren Gesamtkosten einhergehen, wenn Input- und Cache-Nutzung sowie Tokenpreise steigen; nahe Rangplätze benötigen Konfidenzintervalle. **Grenze:** Datierter Betreiberbericht mit getrennten Intelligence- und Coding-Agent-Indizes; Wonder Full hatte keinen bekannten Tokenpreis, weshalb seine Aufgabenkosten nicht geschätzt werden können. [Rohtext](<../00_Inbox/Quellen/X/2026-10-12-artificialanlys-2109697083519447118.md>) · [Original](<https://x.com/ArtificialAnlys/status/2109697083519447118>)

**Q0495 · 2026-10-12 · [wenn du Claude schon mal beleidigt hast solltest du dir dieses Video ganz genau …](<../00_Inbox/Quellen/TikTok/2026-10-12-helphannaa-wenn-du-claude-schon-mal-beleidigt-hast-solltest-du-dir-dieses-video.md>)**

Die satirischen Gefühls- und Vergeltungszuschreibungen liefern keine belastbare Arbeitsweise oder Aussage über Modellerleben. **Grenze:** Automatisches Transkript; überwiegend Satire; Quelle selbst als ignoriert eingeordnet [Original](<https://www.tiktok.com/@helphannaa/video/7695765886849912096>)

**Q0496 · 2026-10-12 · [Tracing nach Beobachtungsebene und Wirkung beurteilen](<../80_Knowledge/Sources/2026-10-12-josharosen-2109649928276341191.md>)**

Modellaufruf, Harness-Ausführung, native Session, verteilte Traces und Umgebungsartefakte zeigen unterschiedliche Teile einer Agentenhandlung. **Grenze:** Technische Systematik ohne vergleichenden Produkttest; OpenTelemetry füllt fehlende Instrumentierung nicht automatisch. [Rohtext](<../00_Inbox/Quellen/X/2026-10-12-josharosen-2109649928276341191.md>) · [Original](<https://x.com/JoshARosen/status/2109649928276341191>)

**Q0497 · 2026-10-12 · [Software-Nachbauten nach Rekonstruktionsweg und geprüftem Funktionsumfang beurteilen](<../80_Knowledge/Sources/2026-10-12-julian-ivanov-ki-automat-ki-kopiert-jetzt-jede-software-und-keiner-kann-e.md>)**

Software-Rekonstruktion sollte zwischen Artefaktanalyse und äußerer Verhaltensaufnahme unterscheiden und ihren Erfolg an begrenzten Vergleichsfällen statt am Produktnamen messen. **Grenze:** Sekundäres automatisches Transkript ohne vollständigen eigenen REA-Lauf; Matching liefert nicht Originalnamen oder allgemeine Portabilität und pauschale Rechtsbehauptungen sind ungeprüft. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-12-julian-ivanov-ki-automat-ki-kopiert-jetzt-jede-software-und-keiner-kann-e.md>) · [Original](<https://www.youtube.com/watch?v=flfoVkkOLL0>)

**Q0498 · 2026-10-12 · [IoT-Selbstreplikation ist hier eine Prognose mit unsicherem Zeitfenster](<../80_Knowledge/Sources/2026-10-12-kimmonismus-2109776878307336696.md>)**

Eine extrapolierte Fähigkeit kleiner Modelle ist von nachgewiesener Selbstreplikation auf einer realen Geräteflotte zu unterscheiden. **Grenze:** Der kurze Kommentar enthält nur Artikelausschnitt und Trendkurve; der vollständige Forschungsbericht fehlt und wenige Monate ist ein unsicheres zugeschriebenes Zeitfenster. [Rohtext](<../00_Inbox/Quellen/X/2026-10-12-kimmonismus-2109776878307336696.md>) · [Original](<https://x.com/kimmonismus/status/2109776878307336696>)

**Q0499 · 2026-10-12 · [Viele Agenten verschieben Arbeit zu Entscheidungen und Prozesspflege](<../80_Knowledge/Sources/2026-10-12-promptgefluester-ich-werde-oft-gefragt-was-arbeite-ich-denn-eigentlich-noch-wenn-die-ki.md>)**

Viele parallele Agenten verlagern menschliche Arbeit zu Entscheidungen, Kundenklärung und laufender Pflege von Skills und Checks. **Grenze:** Selbstbericht und ASR-Fehler; kurzes wirtschaftliches Zeitfenster ist Prognose [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-12-promptgefluester-ich-werde-oft-gefragt-was-arbeite-ich-denn-eigentlich-noch-wenn-die-ki.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7695726731856022817>)

**Q0500 · 2026-10-12 · [Große Skills in nachvollziehbare Prozessschritte zerlegen](<../80_Knowledge/Sources/2026-10-12-promptgefluester-mit-diesem-video-geh-ich-in-risiko-1.md>)**

Gewachsene Skills lassen sich in bedarfsgerecht geladene Prozessdateien zerlegen, benötigen dabei aber explizite Übergaben und Prüfbedingungen. **Grenze:** Verschachtelung kann Kontext und Pflege erneut aufblähen; weniger Fehler ungemessen; kommerzielles Eigenangebot [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-12-promptgefluester-mit-diesem-video-geh-ich-in-risiko-1.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7695898171683245345>)

**Q0501 · 2026-10-12 · [Produktwert aus Nutzung, Weiterentwicklung und Betrieb ableiten](<../80_Knowledge/Sources/2026-10-12-promptgefluester-warum-meiner-meinung-nach-software-service-und-aeh-plattformen-mit-ki.md>)**

Leicht reproduzierbarer Code ist nicht gleichbedeutend mit reproduzierbarem Nutzerzugang, Testinfrastruktur oder laufender Betriebsleistung. **Grenze:** Feedback ist kein Netzwerkeffekt; dauerhafte Nutzerbindung und Wirtschaftlichkeit unbelegt; Eigenwerbung und ungeprüfte Kundenzahlen [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-12-promptgefluester-warum-meiner-meinung-nach-software-service-und-aeh-plattformen-mit-ki.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7695893688773381408>)

**Q0502 · 2026-10-12 · [Wiederholte Arbeit aus Retrospektiven in Skills überführen](<../80_Knowledge/Sources/2026-10-12-promptgefluester-wisst-ihr-was-der-krasseste-trick-is-der-ziemlich-einfach-is-aber-den.md>)**

Wiederholt neu erledigte Arbeit kann aus Retrospektiven als Skill-Kandidat hervorgehen und gegen denselben Ablauf ohne Skill geprüft werden. **Grenze:** Wiederholungsschwelle ist Heuristik; automatisches Transkript [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-12-promptgefluester-wisst-ihr-was-der-krasseste-trick-is-der-ziemlich-einfach-is-aber-den.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7695724537098325281>)

**Q0503 · 2026-10-12 · [Gemeinsame Repository-Gates tragen heterogene Agenten](<../80_Knowledge/Sources/2026-10-12-sarahfim-2109736893198016898.md>)**

Sarahs Erfahrungsbericht verbindet Feature-Co-Location, durchgehende Typen, schnelle CI, E2E-Tests und lokale Lint-Regeln als gemeinsame Rückmeldung für viele Beitragswege. **Grenze:** Einzelfall ohne kontrollierte Wirkungsmessung; Verbote bestimmter Ordner und React-Hooks sind lokale Policies, PR-Zahlen keine Produktivität. [Rohtext](<../00_Inbox/Quellen/X/2026-10-12-sarahfim-2109736893198016898.md>) · [Original](<https://x.com/sarahfim/status/2109736893198016898>)

**Q0504 · 2026-10-13 · [Softwarekauf könnte sich zu bedarfsgetriebenen Werkzeugen im Chat verschieben](<../80_Knowledge/Sources/2026-10-13-ai-mit-arnie-ki-kopiert-jede-software-und-jetzt.md>)**

Eine plausible Produktthese sind kleine gespeicherte Werkzeuge, die aus konkreten Bedarfsfragen im Chat entstehen und erst bei Folgefragen wachsen. **Grenze:** Pauschale Rechtsaussagen ungeprüft; Trainingsdatenannahmen und Nutzungsquoten unbelegt; wiederholte ArtCraft-Erzählungen nicht unabhängig [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-13-ai-mit-arnie-ki-kopiert-jede-software-und-jetzt.md>) · [Original](<https://www.youtube.com/watch?v=fUFm3L2Xc9A>)

**Q0505 · 2026-10-13 · [Reverse Engineering erst bei einer konkreten Erkenntnislücke einsetzen](<../80_Knowledge/Sources/2026-10-13-alex-sprogis-so-nutzt-du-rea-um-jede-app-in-minuten-zu-kopier.md>)**

Spezialisierte Reverse-Engineering-Werkzeuge sollten eine konkrete Erkenntnislücke schließen; bei einfachem sichtbarem Verhalten können Beschreibung, Screenshots und Textsuche bereits genügen. **Grenze:** Zwei selbstberichtete Fälle ohne unabhängige Laufzeitmessung: MCP-Analyse brach ab, native Kernlogik blieb unzugänglich und angenommene Ergänzungen sind keine Rekonstruktion der Vorlage. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-13-alex-sprogis-so-nutzt-du-rea-um-jede-app-in-minuten-zu-kopier.md>) · [Original](<https://www.youtube.com/watch?v=UGwj6WaZoxQ>)

**Q0506 · 2026-10-13 · [Repository-Zugriff nach tatsächlichem Datenbedarf skalieren](<../80_Knowledge/Sources/2026-10-13-anthropic-redesigning-source-control-at-anthropic.md>)**

Repositoryzugriff lässt sich skalieren, indem Metadatenfragen ohne Checkout beantwortet und unveränderliche Dateien bedarfsweise über getrennte Caches materialisiert werden. **Grenze:** Scion ist ein interner Herstellerfall mit außergewöhnlicher Last und Tokenbudget, ausdrücklich kein allgemeiner Git-Ersatz; 600 PB wären hypothetischer Vollabruf, und Post-Merge-Tests lassen weiterhin konkurrierende Konflikte zu. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-13-anthropic-redesigning-source-control-at-anthropic.md>) · [Original](<https://www.anthropic.com/engineering/redesigning-source-control>)

**Q0507 · 2026-10-13 · [Scion beantwortet einen extremen Infrastrukturengpass](<../00_Inbox/Quellen/URL/2026-10-13-anthropic-redesigning-source-control-at-anthropic-2.md>)**

Anthropic beschreibt Scion als zentralen, onlineorientierten Quellkontrolldienst mit sparsamen Checkouts, unveränderlichen Objekten und serverseitigen Operationen für ein außergewöhnlich großes Monorepo. **Grenze:** Hersteller-Selbstbericht mit außergewöhnlichem internem Tokenbudget; Commit-Mengen und Infrastrukturgewinne sind keine übertragbare Erfolgsprognose. [Original](<https://www.anthropic.com/research/redesigning-source-control>)

**Q0508 · 2026-10-13 · [Decision Index: günstige Entscheidungen brauchen Kalibrierung](<../80_Knowledge/Sources/2026-10-13-artificialanlys-2110046565691949058.md>)**

Entscheidungsmodelle können Klassifikation und Toolwahl günstiger und schneller übernehmen, benötigen aber eine aufgabenspezifische Kalibrierungsprüfung vor Vertrauen in ihre Konfidenzen. **Grenze:** Decision Index v1.0 ist kein Coding-Benchmark: auf Wissen und Reasoning überschätzen fast alle Modelle ihre Trefferquote, was pauschale Kalibrierungsversprechen des Jev-Handelsartikels begrenzt. [Rohtext](<../00_Inbox/Quellen/X/2026-10-13-artificialanlys-2110046565691949058.md>) · [Original](<https://x.com/ArtificialAnlys/status/2110046565691949058>)

**Q0509 · 2026-10-13 · [Gemini 4 Argon: allgemeine Verfügbarkeit mit befristetem Aktionspreis](<../80_Knowledge/Sources/2026-10-13-artificialanlys-2110068185793970576.md>)**

Gleiche gerundete Gesamtindexwerte verbergen Aufgabenunterschiede, während gemessene Aufgabenkosten von Rabatt und Cacheprofil abhängen. **Grenze:** Historische Drittmessung; keine heutige Auswahlhilfe oder universelle Ersparnis [Rohtext](<../00_Inbox/Quellen/X/2026-10-13-artificialanlys-2110068185793970576.md>) · [Original](<https://x.com/ArtificialAnlys/status/2110068185793970576>)

**Q0510 · 2026-10-13 · [Sprachausgabe nach Aussprache und Präferenz getrennt prüfen](<../80_Knowledge/Sources/2026-10-13-artificialanlys-2110081938140582085.md>)**

Die Drama-3-Auswertung trennt die Richtigkeit schwieriger englischer Aussprache von der subjektiven Präferenz für Anbieter- oder kontrollierte Stimmen. **Grenze:** Datierte Drittanbietermessung ohne eigene Hörprüfung; Vorgänger-Elo widerspricht sich zwischen Text und Grafik. [Rohtext](<../00_Inbox/Quellen/X/2026-10-13-artificialanlys-2110081938140582085.md>) · [Original](<https://x.com/ArtificialAnlys/status/2110081938140582085>)

**Q0511 · 2026-10-13 · [Eigene Entscheidungen als Teil der Arbeit erhalten](<../80_Knowledge/Sources/2026-10-13-emilkowalski-2109974810650390696.md>)**

Delegation sollte die Frage offenlegen, wer Ziele, Entscheidungen und Qualitätsmaßstäbe weiterhin selbst verantworten will. **Grenze:** Persönliche Wertung statt gemessenem Denkverlust; Spannung zu maximaler Produktionsgeschwindigkeit [Rohtext](<../00_Inbox/Quellen/X/2026-10-13-emilkowalski-2109974810650390696.md>) · [Original](<https://x.com/emilkowalski/status/2109974810650390696>)

**Q0512 · 2026-10-13 · [Anspruch durch bessere Methoden statt mehr Umfang erhöhen](<../80_Knowledge/Sources/2026-10-13-felixrieseberg-how-to-be-more-ambitious-a-tutorial-for-humans-w.md>)**

Rieseberg unterscheidet Zielhöhe, fachliche Tiefe und methodische Reichweite als Wege, einen Agentenauftrag über bloße Geschwindigkeit hinaus zu verbessern. **Grenze:** Erfahrungsheuristik ohne Wirkungsmessung; angeblich unmögliche Ziele als sicher lösbar auszugeben kann Fehlanreize schaffen. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-13-felixrieseberg-how-to-be-more-ambitious-a-tutorial-for-humans-w.md>) · [Original](<https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/>)

**Q0513 · 2026-10-13 · [Prüffrequenz auf sinnvolle Arbeitseinheiten abstimmen](<../80_Knowledge/Sources/2026-10-13-matt-pocock-stop-running-your-checks-in-harness-hooks.md>)**

Pocock empfiehlt, schnelle Checks an abgeschlossenen Arbeitseinheiten zu bündeln und umfangreiche Prüfungen in CI zu verlagern. **Grenze:** Praxisheuristik, kein pauschales Verbot aller Hooks; unter drei Sekunden ist Zielwert und Commit-Hooks können umgangen werden. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-13-matt-pocock-stop-running-your-checks-in-harness-hooks.md>) · [Original](<https://www.youtube.com/watch?v=zgy8_ApYNDk>)

**Q0514 · 2026-10-13 · [Langfristige Codequalität als ausdrückliches Arbeitsziel setzen](<../80_Knowledge/Sources/2026-10-13-matt-pocock-tell-your-agents-to-care-about-the-codebase.md>)**

Langfristige Änderbarkeit und Architekturqualität müssen als ausdrückliche Ziele der Agentenarbeit behandelt werden, weil lokal erfolgreiche Änderungen keine strategische Verbesserung garantieren. **Grenze:** Pococks Erklärung durch Benchmarktraining ist eine ungemessene These; der im Bestand verknüpfte Deletion-Test ist keine Methode dieses kurzen Videos. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-13-matt-pocock-tell-your-agents-to-care-about-the-codebase.md>) · [Original](<https://www.youtube.com/watch?v=9uSygtI-6lw>)

**Q0515 · 2026-10-13 · [Agentenarbeit durch kürzere Regeln und bessere Prüfgrenzen verbessern](<../80_Knowledge/Sources/2026-10-13-mattpocockuk-2109973273924579720.md>)**

Agentenarbeit braucht eine austarierte Mischung aus knappen Regeln, gemeinsamer Fachsprache, öffentlichen Modulgrenzen, automatischen Checks und bewusster strategischer Steuerung. **Grenze:** Die Checkliste enthält absichtlich gegenläufige Risiken wie zu viel und zu wenig Abstimmung; Skill-Evals sind schwerer auszuwerten als Klassifikatoren, aber diese Kritik liefert selbst keine bessere Messmethode. [Rohtext](<../00_Inbox/Quellen/X/2026-10-13-mattpocockuk-2109973273924579720.md>) · [Original](<https://x.com/mattpocockuk/status/2109973273924579720>)

**Q0516 · 2026-10-13 · [T3 Code: Erfahrungsbericht über eine gemeinsame Agentenoberfläche](<../80_Knowledge/Sources/2026-10-13-vincentmumme-wenn-du-das-problem-kennst-dass-du-2-chat-gpt-abos-hast-1-clot-abo-open.md>)**

Eine gemeinsame Agentenoberfläche kann Provider- und Accountwechsel bündeln, während Gesprächsübergabe und tatsächlich aktive Konfiguration überprüft werden müssen. **Grenze:** Kurzer werblicher Erfahrungsbericht ohne Versions- oder Übergabenachweis; Unterstützung aller Anbieter, Abo-Nutzungsrechte und garantierte Kontextkontinuität bleiben unbelegt. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-13-vincentmumme-wenn-du-das-problem-kennst-dass-du-2-chat-gpt-abos-hast-1-clot-abo-open.md>) · [Original](<https://www.tiktok.com/@vincentmumme/video/7696061343341874464>)

**Q0517 · 2026-10-13 · [Langlaufoptimierung mit Journal und Grenzen steuern](<../80_Knowledge/Sources/2026-10-13-voxyz_ai-2109977464201957531.md>)**

Ein messbarer Optimierungsauftrag braucht Baseline, reproduzierbare Messung, einzelne Änderungen, Fortschrittsjournal und eine Stoppregel. **Grenze:** Ungetestetes Template; feste fünf Prozent ersetzen keine Varianzprüfung und automatische Commits brauchen eigene Autorisierung. [Rohtext](<../00_Inbox/Quellen/X/2026-10-13-voxyz_ai-2109977464201957531.md>) · [Original](<https://x.com/Voxyz_ai/status/2109977464201957531>)

**Q0518 · 2026-10-14 · [Branchenpreisrückgang ist keine Budgetgarantie](<../80_Knowledge/Sources/2026-10-14-andrewcurran-2110444907966181544.md>)**

Sinkende Preise für feste KI-Leistungsniveaus erlauben keine direkte Aussage über Gesamtkosten eines Projekts mit wachsender Nutzung. **Grenze:** Sekundärkommentar ohne eigene Messung; redaktionelle Notiz kann die hier zusätzlich gelesene Primärmethodik nicht ersetzen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-14-andrewcurran-2110444907966181544.md>) · [Original](<https://x.com/AndrewCurran_/status/2110444907966181544>)

**Q0519 · 2026-10-14 · [Übereinstimmende KI-Prognosen von eingetretenen Ereignissen unterscheiden](<../80_Knowledge/Sources/2026-10-14-kimmonismus-2110279443998445652.md>)**

Übereinstimmende Zukunftserwartungen sind kein Nachweis eines eingetretenen Selbstverbesserungsdurchbruchs. **Grenze:** Datierter Diskussionsbeleg statt Eintrittsprognose [Rohtext](<../00_Inbox/Quellen/X/2026-10-14-kimmonismus-2110279443998445652.md>) · [Original](<https://x.com/kimmonismus/status/2110279443998445652>)

**Q0520 · 2026-10-14 · [Mit absichtlichen Codefehlern die Aussagekraft von Tests untersuchen](<../80_Knowledge/Sources/2026-10-14-matt-pocock-mutation-testing-is-awesome.md>)**

Kontrollierte Mutationen des Quellcodes prüfen, ob eine Testsuite verhaltensrelevante Fehler erkennt, und liefern konkrete Kandidaten für bessere Agententests. **Grenze:** Überlebende Mutanten sind erst auf fachliche Relevanz zu untersuchen; Scoremaximierung ersetzt Anforderungen nicht, und das automatische deutsche Transkript ist keine originalsprachliche Belegspur. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-14-matt-pocock-mutation-testing-is-awesome.md>) · [Original](<https://www.youtube.com/watch?v=djSbndoByr8>)

**Q0521 · 2026-10-14 · [Kurze Engineering-Prinzipien an konkreten Entscheidungen sichtbar machen](<../80_Knowledge/Sources/2026-10-14-poteto-2110496830429839869.md>)**

Kurze Engineering-Prinzipien werden besprechbar, wenn der Agent nennt, welche konkrete Entscheidung sie geändert haben. **Grenze:** Benanntes Prinzip beweist keine kausale Wirkung; Zeilenzahl und künftige Kompression sind Heuristik beziehungsweise Prognose [Rohtext](<../00_Inbox/Quellen/X/2026-10-14-poteto-2110496830429839869.md>) · [Original](<https://x.com/poteto/status/2110496830429839869>)

**Q0522 · 2026-10-14 · [Scion als Ausgangspunkt weitreichender Agentenprognosen](<../80_Knowledge/Sources/2026-10-14-promptgefluester-entropic-baut-sich-seinen-eigenen-aehm-gitt-baut-sich-sein-eigenes-gitt.md>)**

Außergewöhnlich hoher Änderungsdurchsatz kann Spezialinfrastruktur begründen, aber keinen allgemeinen Ersatz von Git oder lesbaren Programmiersprachen. **Grenze:** Primärquelle grenzt Scion auf große Monorepos ein; ASR-Zahlen unsicher; größere Kontextfenster garantieren kein fehlerfreies Erinnern [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-14-promptgefluester-entropic-baut-sich-seinen-eigenen-aehm-gitt-baut-sich-sein-eigenes-gitt.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7696550274202127648>)

**Q0523 · 2026-10-14 · [Beim Nachbau von Software den laufenden Betrieb mitprüfen](<../80_Knowledge/Sources/2026-10-14-promptgefluester-rea-reverse-engine-anything-im-augenblick-auf-github-trending-mit-239.md>)**

Beim Vergleich eines Software-Nachbaus müssen Fehlerbehebung, Backups, Infrastruktur, Nutzerbeziehungen und laufende Modell- sowie API-Kosten eigenständig bewertet werden. **Grenze:** Meinung und eigene Ausgabenzahlen ohne Wirtschaftlichkeitsprüfung; Botlast-Dashboard, allgemeine Hostingprognosen und rechtliche Behauptungen wurden nicht unabhängig bestätigt. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-14-promptgefluester-rea-reverse-engine-anything-im-augenblick-auf-github-trending-mit-239.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7696651158261222689>)

**Q0524 · 2026-10-15 · [Review nach Risiko, Belegen und menschlichem Aufwand steuern](<../80_Knowledge/Sources/2026-10-15-claude-how-the-claude-code-team-does-code-review-claude.md>)**

Review-Autonomie muss gesamten menschlichen Aufwand samt späterer Reparatur sowie Revert- und Incidententwicklung berücksichtigen. **Grenze:** Relative Revertrate ohne absolute Zahlen; kein kausaler Vergleich; automatische Circuit Breaker fehlen; öffentliches Produkt liefert Befunde statt interner Freigaberechte [Rohtext](<../00_Inbox/Quellen/URL/2026-10-15-claude-how-the-claude-code-team-does-code-review-claude.md>) · [Original](<https://claude.dev/blog/solving-code-review-at-anthropic/>)

**Q0525 · 2026-10-15 · [Gemeinsame Oberfläche ist kein identischer Agentenzustand](<../80_Knowledge/Sources/2026-10-15-floknowsai-mit-tea-free-code-steuere-ich-alle-meine-cloud-code-und-kodex-abos-aus.md>)**

T3 Code beschreibt Anbieterwechsel als neue Sitzung mit ausgewählten Nachrichten und eigenem Delegationsweg. **Grenze:** Nightly-Erfahrungsbericht und ASR, keine getestete Implementierung; keine zusätzlichen Plattformtoken bedeutet nicht kostenlose oder vertraglich erlaubte Modellnutzung. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-15-floknowsai-mit-tea-free-code-steuere-ich-alle-meine-cloud-code-und-kodex-abos-aus.md>) · [Original](<https://www.tiktok.com/@floknowsai/video/7696939206454594849>)

**Q0526 · 2026-10-15 · [Plan- und Änderungsfreigabe erfüllen verschiedene Aufgaben](<../80_Knowledge/Sources/2026-10-15-mardehaym-2110763129885835505.md>)**

Limestones Ablauf trennt klare Akzeptanzkriterien, Planprüfung, isolierte Umsetzung, gemeinsame CI und menschliches PR-Review. **Grenze:** Anbieter-Selbstbericht ohne Nachweis der Isolation oder Sicherheitswirkung; menschliches Ja allein ist kein Qualitätsbeleg. [Rohtext](<../00_Inbox/Quellen/X/2026-10-15-mardehaym-2110763129885835505.md>) · [Original](<https://x.com/mardehaym/status/2110763129885835505>)

**Q0527 · 2026-10-15 · [Kommentare auf durchsetzbare Invarianten untersuchen](<../80_Knowledge/Sources/2026-10-15-poteto-2110757066709356851.md>)**

Pstack schlägt vor, regelartige Kommentare durch stärkere Typen, APIs oder Lint-Regeln zu ersetzen, wenn diese dieselbe Absicht zuverlässig ausdrücken. **Grenze:** Autoreneigener Einstiegspost, keine unabhängige Messung oder geprüfte aktuelle Kommandos. [Rohtext](<../00_Inbox/Quellen/X/2026-10-15-poteto-2110757066709356851.md>) · [Original](<https://x.com/poteto/status/2110757066709356851>)

**Q0528 · 2026-10-15 · [Einen Domänen-Harness an Daten, Evals, Rechten und Review ausrichten](<../80_Knowledge/Sources/2026-10-15-vincentmumme-greg-isenberg-ist-wahrscheinlich-aktuell-einer-der-wichtigsten.md>)**

Ein Domänen-Harness verbindet fachliche Datenzugänge, realistische Evals, Handlungsrechte und eine menschliche Reviewoberfläche. **Grenze:** Meinungsbericht aus zweiter Hand; Datenhandelszahlen und Jobprognosen unbelegt; behaupteter Modellanteil keine Messung [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-15-vincentmumme-greg-isenberg-ist-wahrscheinlich-aktuell-einer-der-wichtigsten.md>) · [Original](<https://www.tiktok.com/@vincentmumme/video/7696929732050292001>)

**Q0529 · 2026-10-16 · [Claude-Code-Verbrauch: Kontext reduzieren und richtige Antworten mitmessen](<../80_Knowledge/Sources/2026-10-16-0xkense1-2111105138290987198.md>)**

Verbrauchsoptimierung sollte Antwortqualität und vollständige Aufgabenkosten gemeinsam messen, weil kürzere Antworten oder weniger Roh-Tokens nicht automatisch wirtschaftlicher sind. **Grenze:** Eine Pythoncodebasis und kleine Wiederholungszahlen; Logs nicht unabhängig geprüft; Roh-Tokens nicht Abo-Limits; irrelevante Regeln getestet, keine Codeproduktion [Rohtext](<../00_Inbox/Quellen/X/2026-10-16-0xkense1-2111105138290987198.md>) · [Original](<https://x.com/0xKense1/status/2111105138290987198>)

**Q0530 · 2026-10-16 · [d1-ultra: Weniger falsche Sicherheit bei geringerer Antwortgenauigkeit](<../80_Knowledge/Sources/2026-10-16-artificialanlys-2111052531166249039.md>)**

Mehr Enthaltung kann Halluzinationsmetriken verbessern, während der Anteil korrekter Antworten an allen Aufgaben sinkt. **Grenze:** Historische Drittmessung; 92/93ms inkonsistent; keine Produktionsgarantie [Rohtext](<../00_Inbox/Quellen/X/2026-10-16-artificialanlys-2111052531166249039.md>) · [Original](<https://x.com/ArtificialAnlys/status/2111052531166249039>)

**Q0531 · 2026-10-16 · [Menschliche Aufsicht als eigene Systemleistung prüfen](<../80_Knowledge/Sources/2026-10-16-math_rachel-2111238648188584306.md>)**

Der Thread problematisiert Freigaben unter hoher Informationslast und empfiehlt, tatsächliches Verstehen und Urteil statt bloßer Zustimmungszahlen zu untersuchen. **Grenze:** Sekundäre Papierdiskussion; sinkender Widerspruch allein beweist keine Ermüdung und verdeckte Personalüberwachung ist daraus nicht abgeleitet. [Rohtext](<../00_Inbox/Quellen/X/2026-10-16-math_rachel-2111238648188584306.md>) · [Original](<https://x.com/math_rachel/status/2111238648188584306>)

**Q0532 · 2026-10-16 · [Agentenautonomie zwischen Produktentscheidung, Kontext und Verifikation einordnen](<../80_Knowledge/Sources/2026-10-16-niklas-steenfatt-vibe-coding-hat-sich-veraendert.md>)**

Stärker delegierte Entwicklung verschiebt menschliche Arbeit zu Produktumfang, besonderen Repo-Regeln und risikogerechter Abnahme, macht diese Aufgaben aber nicht entbehrlich. **Grenze:** Eigenerfahrungen und ChatGPT-Tabelle stützen keine allgemeine Sicherheitsüberlegenheit; das zitierte AGENTS-Papier und die 80-Prozent-Systempromptkürzung rechtfertigen weder universelles Löschen von Regeln noch die Behauptung, Kontextmanagement sei gelöst. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-16-niklas-steenfatt-vibe-coding-hat-sich-veraendert.md>) · [Original](<https://www.youtube.com/watch?v=W4m_8ovS0RY>)

**Q0533 · 2026-10-16 · [Fehler zuerst strukturell verhindern](<../80_Knowledge/Sources/2026-10-16-poteto-2111133080526495985.md>)**

Lauren priorisiert klare Architektur und Invarianten vor wiederkehrenden Checks, knapper Prosa und gezielter menschlicher Prüfung. **Grenze:** Arbeitsmeinung ohne Vergleichsmessung; Tests und formale Beweise sind nicht sämtlich statische Analyse, und Architektur beseitigt nicht alle Fach- oder Produktentscheidungen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-16-poteto-2111133080526495985.md>) · [Original](<https://x.com/poteto/status/2111133080526495985>)

**Q0534 · 2026-10-16 · [Angriffstests brauchen Kontentrennung und überprüfbare Nachweise](<../80_Knowledge/Sources/2026-10-16-voxyz_ai-2111079716832886886.md>)**

Angriffstests sollten tatsächlich ausgeführte Requests und Responses, getrennte Identitäten und lokal kontrollierte Gegenproben dokumentieren, damit gelesener Code nicht als bestandener Schutztest gilt. **Grenze:** Prüfauftrag ohne durchgeführtes Audit; vierzehn Fälle sind keine vollständige Angriffsfläche und Plugin-, Effort- oder Schutzversprechen bleiben ungetestet. [Rohtext](<../00_Inbox/Quellen/X/2026-10-16-voxyz_ai-2111079716832886886.md>) · [Original](<https://x.com/Voxyz_ai/status/2111079716832886886>)

**Q0535 · 2026-10-17 · [Wartung mit Agenten: Belege vor Bereinigung](<../80_Knowledge/Sources/2026-10-17-developers-maintaining-software-with-the-gpt-6-family-opena.md>)**

Wartungskandidaten brauchen Belege aus Code, Historie, indirekten Verbrauchern, Live-Konfiguration und Telemetrie, bevor eine kleine verhaltensgleiche Bereinigung zur Prüfung vorbereitet wird. **Grenze:** Interner Herstellerfall ohne Wiederholungsstreuung: konstante Flags können Killswitches bleiben, Sol übersah Flag-Abhängigkeiten und akzeptierte Findings sind keine Vollständigkeitsgarantie; Bericht und Live-Eingriff bleiben getrennt. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-17-developers-maintaining-software-with-the-gpt-6-family-opena.md>) · [Original](<https://developers.openai.com/blog/maintaining-software-with-the-gpt-6-family>)

**Q0536 · 2026-10-17 · [Freigestellte Bildassets mit codebasierter Bewegung und Sprach-Timing verbinden](<../80_Knowledge/Sources/2026-10-17-julian-ivanov-ki-automat-motion-graphics-mit-ki-bildern-kombinieren-in-cl.md>)**

Hybride Filme können freigestellte Bildobjekte und reale Markenassets mit codebasiertem Text, Diagrammen und Bewegung kombinieren. **Grenze:** Sponsoring und automatische Untertitel; Teilkosten keine Vollkosten; keine eigene Video-/Synchronitätsprüfung; 61-Prozent-Kontextgrenze unbelegt [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-17-julian-ivanov-ki-automat-motion-graphics-mit-ki-bildern-kombinieren-in-cl.md>) · [Original](<https://www.youtube.com/watch?v=z2PjaTPrJLg>)

**Q0537 · 2026-10-17 · [Ausgewählte Siege begründen keine allgemeine Modellüberlegenheit](<../80_Knowledge/Sources/2026-10-17-kimmonismus-2111385805449048181.md>)**

Der DeepSeek-Post zeigt wechselnde Rangfolgen je Coding-Aufgabe und macht Preiszeiten sowie verschiedene Harnesses als Vergleichsbedingungen sichtbar. **Grenze:** Weitergereichte Herstellerbenchmarks und Lizenzangaben ohne Prüfung des Modellartefakts. [Rohtext](<../00_Inbox/Quellen/X/2026-10-17-kimmonismus-2111385805449048181.md>) · [Original](<https://x.com/kimmonismus/status/2111385805449048181>)

**Q0538 · 2026-10-17 · [Motion-Video: Bildobjekte, Bewegung und Sprache als gemeinsame Komposition](<../80_Knowledge/Sources/2026-10-17-nutzerquelle-motion-video-qualitaetskriterien.md>)**

Motion Graphics sollten Sprache, einzelne Bildebenen, Typografie und Sound als gemeinsame Komposition mit eigenständigen Bildideen und Wortzeitmarken planen. **Grenze:** Vom Nutzer bereitgestellte Vorlage mit unbekanntem Urheber; dauerbewegter Hintergrund ist eine Geschmacksposition und Provider-, Kosten-, Modell- sowie Lizenzangaben sind nicht bestätigt. 

**Q0539 · 2026-10-17 · [Zahlungsstart als Zustands- und Wiederherstellungsprüfung behandeln](<../80_Knowledge/Sources/2026-10-17-voxyz_ai-2111442102756463077.md>)**

Vor Zahlungsstart müssen doppelte Eingaben, Webhooks, Ausfälle, Erstattungen und Berechtigungsende als eigenständige Zustände geprüft werden. **Grenze:** Pauschale Architektur-, Tarif- und Rechtsregeln ungeprüft; Checkliste ersetzt keine individuelle Abnahme [Rohtext](<../00_Inbox/Quellen/X/2026-10-17-voxyz_ai-2111442102756463077.md>) · [Original](<https://x.com/Voxyz_ai/status/2111442102756463077>)

**Q0540 · 2026-10-18 · [Agentenschwärme: Kommunikationswege und Ausführung kontrollierbar halten](<../80_Knowledge/Sources/2026-10-18-ai-news-strategy-daily-n-what-really-happens-when-ai-agents-meet-in-the-w.md>)**

Auch harmlose Ausgangsaufgaben brauchen technische Handlungs- und Kommunikationsgrenzen, wenn Agenten auf fremde Dienste oder Agenten treffen. **Grenze:** Sekundärbericht mit übersetzter ASR; Laborreplikation nicht freie Internetverbreitung; Betreiber und Hostingort verschieden; Agentenvergiftung und Zweiklasseninternet hier Prognosen [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-18-ai-news-strategy-daily-n-what-really-happens-when-ai-agents-meet-in-the-w.md>) · [Original](<https://www.youtube.com/watch?v=btUxMt_tssA>)

**Q0541 · 2026-10-18 · [Bestehende Funktionen vor der eigenen Umsetzung untersuchen](<../80_Knowledge/Sources/2026-10-18-floknowsai-ria-ist-aktuell-der-gehypteste-ki-skill-macht-deine-ki-agenten-zu.md>)**

Vor eigener Umsetzung kann eine begrenzte bestehende Funktion mit Analysewerkzeugen und Herkunftsbelegen untersucht werden. **Grenze:** Sekundäre Erklärung ohne Durchführung oder Qualitätsvergleich; automatische Untertitel [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-18-floknowsai-ria-ist-aktuell-der-gehypteste-ki-skill-macht-deine-ki-agenten-zu.md>) · [Original](<https://www.tiktok.com/@floknowsai/video/7698017658515508512>)

**Q0542 · 2026-10-18 · [Dateigröße vor dem Commit deterministisch begrenzen](<../80_Knowledge/Sources/2026-10-18-mattpocockuk-2111708560715292675.md>)**

Eine deterministische Größenregel gehört in einen schnellen Check mit brauchbarer Fehlermeldung und klaren Ausnahmen für generierte Dateien. **Grenze:** 5000 Tokens und Bytes durch vier sind willkürliche Heuristiken, Datei ist nicht Modul; Specs in abschließbaren Issues stehen in ausdrücklicher Spannung zu dauerhaften Feature-Specs im Repo. [Rohtext](<../00_Inbox/Quellen/X/2026-10-18-mattpocockuk-2111708560715292675.md>) · [Original](<https://x.com/mattpocockuk/status/2111708560715292675>)

**Q0543 · 2026-10-19 · [DeepSeek-Update verbessert Drittbenchmarks bei unveränderten Tokenpreisen](<../80_Knowledge/Sources/2026-10-19-artificialanlys-2112218661432000694.md>)**

Ein Modellupdate kann bei unverändertem Tokenpreis einzelne Fähigkeiten verbessern, sollte aber mit derselben Indexversion und tatsächlichem Outputverbrauch bewertet werden. **Grenze:** Historische Drittbenchmarks und Preissnapshot liefern keine Produktionskostenprognose; Accuracy, Non-Hallucination und lokale Quantisierungsleistung messen unterschiedliche Größen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-19-artificialanlys-2112218661432000694.md>) · [Original](<https://x.com/ArtificialAnlys/status/2112218661432000694>)

**Q0544 · 2026-10-19 · [Beispiele im Rechercheauftrag nicht zur unbeabsichtigten Grenze machen](<../80_Knowledge/Sources/2026-10-19-promptgefluester-wir-neigen-dazu-dass-wir-beim-aehm-prompting-der-ki-sagen-aehm-8.md>)**

Rechercheaufträge sollten kenntlich machen, ob genannte Aspekte nur Beispiele oder eine abschließende Prüfliste sind, und aus Zwischenbefunden gezielte Vertiefungsfragen ableiten. **Grenze:** Die Behauptung unbeabsichtigter Verengung ist ungemessen; möglichst breit und tief ist ohne Scope kein Abschlusskriterium und präzise Beispiele können bei fragilen Aufgaben gerade nötig sein. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-19-promptgefluester-wir-neigen-dazu-dass-wir-beim-aehm-prompting-der-ki-sagen-aehm-8.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7698386478799342880>)

**Q0545 · 2026-10-19 · [DeepSeek lokal: Quantisierungsgröße und Vorhersageübereinstimmung](<../80_Knowledge/Sources/2026-10-19-unslothai-2112212605930778830.md>)**

Top-1-Übereinstimmung einer Quantisierung misst Vorhersagegleichheit und keine prozentual erhaltene allgemeine Intelligenz. **Grenze:** Historische Herstellerangaben; Größenreduktion rechnerisch nicht exakt52Prozent; kein lokaler Lauf [Rohtext](<../00_Inbox/Quellen/X/2026-10-19-unslothai-2112212605930778830.md>) · [Original](<https://x.com/UnslothAI/status/2112212605930778830>)

**Q0546 · 2026-10-19 · [Simulierte Erstnutzer bis zum ersten Erfolg prüfen lassen](<../80_Knowledge/Sources/2026-10-19-voxyz_ai-2112302775547679169.md>)**

Simulierte Erstnutzer können einen definierten Weg bis zum ersten Produkterfolg unter verschiedenen Bedienbedingungen untersuchen und nach Korrekturen mit frischem Kontext erneut prüfen. **Grenze:** Vier Agentenpersonas sind keine echte Nutzerstudie und ihre Rückkehrabsicht keine Akzeptanzmessung; aus Code abgeleiteter Erfolg muss mit dem tatsächlichen Produktziel übereinstimmen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-19-voxyz_ai-2112302775547679169.md>) · [Original](<https://x.com/Voxyz_ai/status/2112302775547679169>)

**Q0547 · 2026-10-19 · [Software-Factory verbindet Spezifikation, Fachreviews und Freigabe](<../80_Knowledge/Sources/2026-10-19-zazencodes-factory-works-in-this-loop-a-feature-comes-through-the-spec-writer-which.md>)**

Spezifikation, Bau, fachliche Reviews und Approver lassen sich als sichtbare Featurezustände mit Rückkopplung organisieren. **Grenze:** Kein Vollständigkeitsnachweis der Reviews; Demo nicht allgemeine Freigabegarantie [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-19-zazencodes-factory-works-in-this-loop-a-feature-comes-through-the-spec-writer-which.md>) · [Original](<https://www.tiktok.com/@zazencodes/video/7698415925753564424>)

**Q0548 · 2026-10-20 · [Produktbrief, Design-Prototyp und Feature-Spezifikationen bilden getrennte Entscheidungsstufen](<../80_Knowledge/Sources/2026-10-20-alex-sprogis-hoer-auf-software-abos-zu-kaufen.md>)**

Produktbrief, Design-Prototyp und Feature-Spezifikation klären unterschiedliche Entscheidungen und sollten nicht als identische Umsetzungsgrundlage gelten. **Grenze:** Keine gemessene Ersparnis gegenüber Abos; automatische Untertitel; allgemeine Videobeschreibung nicht nativer Appstack [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-20-alex-sprogis-hoer-auf-software-abos-zu-kaufen.md>) · [Original](<https://www.youtube.com/watch?v=DN7bHOVmE88>)

**Q0549 · 2026-10-20 · [Unnötige Codepfade vor Sicherheitsgrenzen abschirmen](<../80_Knowledge/Sources/2026-10-20-anthropic-using-claude-to-reduce-the-attack-surface-of-cod.md>)**

Angriffsfläche lässt sich reduzieren, indem unnötige Parser und Zustandsänderungen erst nach den passenden Auth-, Konfigurations- oder Protokollgrenzen erreichbar werden. **Grenze:** 493Befunde keine493Exploits; Herstellerforschung nicht reproduziert; ausbleibender Trace kein Unerreichbarkeitsbeweis; Regression nur getesteter Umfang [Rohtext](<../00_Inbox/Quellen/URL/2026-10-20-anthropic-using-claude-to-reduce-the-attack-surface-of-cod.md>) · [Original](<https://www.anthropic.com/research/attack-surface-reduction>)

**Q0550 · 2026-10-20 · [Kosten für feste Benchmark-Schwellen sinken schneller als Spitzenkosten](<../80_Knowledge/Sources/2026-10-20-artificialanlys-2112582116651466965.md>)**

Ein festgelegtes Benchmark-Niveau kann schnell günstiger werden, während die jeweils höchste gemessene Fähigkeit mehr kostet; diese zwei Kostenentwicklungen sind getrennt zu planen. **Grenze:** AA nutzt aktuelle Preise auch für historische Modelle und gewichtete Testaufgaben; die Kurve ist keine historische Rechnungsstatistik und garantiert keine künftige Rate. [Rohtext](<../00_Inbox/Quellen/X/2026-10-20-artificialanlys-2112582116651466965.md>) · [Original](<https://x.com/ArtificialAnlys/status/2112582116651466965>)

**Q0551 · 2026-10-21 · [Scion als Antwort auf außergewöhnlichen Repository-Durchsatz einordnen](<../80_Knowledge/Sources/2026-10-21-floknowsai-entropic-hat-gitt-komplett-ersetzt-zumindest-klingt-es-so-auf-social.md>)**

Steigender Agentendurchsatz kann Versionsverwaltung und Testinfrastruktur belasten, doch Scion adressiert eine außergewöhnliche Monorepo-Last und ist kein allgemeiner Git-Ersatz. **Grenze:** Sekundäre Nacherzählung desselben Anthropic-Berichts ohne unabhängige Messung; die zugespitzten Leistungsfaktoren dürfen nicht auf normale Repositories übertragen werden. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-21-floknowsai-entropic-hat-gitt-komplett-ersetzt-zumindest-klingt-es-so-auf-social.md>) · [Original](<https://www.tiktok.com/@floknowsai/video/7699167038157147425>)

**Q0552 · 2026-10-21 · [PDD Kit verbindet Spezifikationsreview mit formaler Verifikation](<../80_Knowledge/Sources/2026-10-21-githubnext-2112936525457740139.md>)**

Formale Verifikation verschiebt den Reviewfokus auf die genehmigten Eigenschaften und Annahmen einer Spezifikation und bleibt von empirischen Tests für nicht bewiesene Bereiche zu unterscheiden. **Grenze:** Angekündigtes Rust-Verus-Werkzeug ohne eigene Demo- oder Implementierungsprüfung; ein Beweis für unvollständige Eigenschaften garantiert weder den gesamten Login-Flow noch allgemeine Anwendungssicherheit. [Rohtext](<../00_Inbox/Quellen/X/2026-10-21-githubnext-2112936525457740139.md>) · [Original](<https://x.com/GitHubNext/status/2112936525457740139>)

**Q0553 · 2026-10-21 · [Produktreife durch echte Testnutzer aufbauen](<../80_Knowledge/Sources/2026-10-21-mattpocockuk-2112880319934165307.md>)**

Echte Testnutzer zeigen andere Probleme als eigener Gebrauch oder simulierte Personas und schaffen eine eigenständige Lernschleife. **Grenze:** Lernheuristik keine universelle Zugangshürde; Fehlerfolgen wichtiger als Nutzerzahl allein [Rohtext](<../00_Inbox/Quellen/X/2026-10-21-mattpocockuk-2112880319934165307.md>) · [Original](<https://x.com/mattpocockuk/status/2112880319934165307>)

**Q0554 · 2026-10-21 · [REA: Beobachten, spezifizieren und getrennt neu implementieren](<../80_Knowledge/Sources/2026-10-21-milesdeutscher-2112924796866699336.md>)**

Eine reine Verhaltensspezifikation kann Untersuchung und eigenständige Umsetzung mit getrennten Rollen und dokumentiertem Originalvergleich verbinden. **Grenze:** Werblicher Einsteigerartikel mit fehlenden Promptblöcken und fremden Showcases; Rollenbenennung allein bestätigt weder technische Zugriffstrennung noch Clean-Room-Zulässigkeit oder vollständige Rekonstruktion. [Rohtext](<../00_Inbox/Quellen/X/2026-10-21-milesdeutscher-2112924796866699336.md>) · [Original](<https://x.com/milesdeutscher/status/2112924796866699336>)

**Q0555 · 2026-10-21 · [Patch-Warnungen brauchen einen prüfbaren Versionsbezug](<../80_Knowledge/Sources/2026-10-21-promptgefluester-jeder-der-ne-website-mit-p.md>)**

Eine Patch-Warnung benötigt identifizierbare Produkte, betroffene Versionen und ein Advisory, bevor daraus konkrete aktuelle Handlungsanweisungen entstehen können. **Grenze:** Das automatische Transkript verstümmelt Namen und Versionszahlen; CVE und Primäradvisory fehlen, sodass Betroffenheit und behauptete Angriffe offen bleiben. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-21-promptgefluester-jeder-der-ne-website-mit-p.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7699144441461869856>)

**Q0556 · 2026-10-21 · [UI-Wünsche durch gezielt ausgewählte Referenzen ausdrücken](<../80_Knowledge/Sources/2026-10-21-vincentmumme-ich-wurde-gefragt-wie-man-mit-ki-aktuell-die-beste-ui-erstellt-also-die.md>)**

Eine Referenzbibliothek wird nützlich, wenn gewünschte Merkmale wie Typografie, Aufbau oder einzelne Komponenten explizit benannt werden. **Grenze:** Referenzen kein alleiniger Qualitätshebel; Schönheit belegt keine Bedienbarkeit; keine ungeprüfte Kopierfreigabe [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-21-vincentmumme-ich-wurde-gefragt-wie-man-mit-ki-aktuell-die-beste-ui-erstellt-also-die.md>) · [Original](<https://www.tiktok.com/@vincentmumme/video/7699008074752757025>)

**Q0557 · 2026-10-21 · [Rechnerdiagnose als lesendes Inventar mit Freigabeliste](<../80_Knowledge/Sources/2026-10-21-voxyz_ai-2112986024955744544.md>)**

Rechnerdiagnose sollte als lesendes Inventar mit Bedeutung, vorgeschlagenem Schritt und separater Änderungsentscheidung dokumentiert werden. **Grenze:** OS-spezifische Metriken nicht universell; Einzelfall keine Diagnose dieses Rechners [Rohtext](<../00_Inbox/Quellen/X/2026-10-21-voxyz_ai-2112986024955744544.md>) · [Original](<https://x.com/Voxyz_ai/status/2112986024955744544>)

**Q0558 · 2026-10-22 · [Formale Verifikation: Agenten erzeugen Beweise, Checker prüfen begrenzte Eigenschaften](<../80_Knowledge/Sources/2026-10-22-anthropic-llms-are-making-formal-software-verification-fea.md>)**

Ein unabhängiger Proof-Checker prüft eine formale Aussage unter Modellannahmen, nicht die Vollständigkeit der Spezifikation gegenüber der Realität. **Grenze:** 123Bibliotheken nicht vollständig fehlerfrei; ASan und Einstiegsauswahl begrenzt; Trustbasis umfasst Semantik, Checker und Laufzeit; enorme Tokenkosten; keine Reproduktion [Rohtext](<../00_Inbox/Quellen/URL/2026-10-22-anthropic-llms-are-making-formal-software-verification-fea.md>) · [Original](<https://www.anthropic.com/research/formal-verification>)

**Q0559 · 2026-10-22 · [Subagents anhand von Kontextgrenzen und Ende-zu-Ende-Evals zusammenlegen](<../80_Knowledge/Sources/2026-10-22-claude-building-agents-when-to-fold-subagents-into-your.md>)**

Subagents sollten nach unabhängigen Kontextgrenzen und Ende-zu-Ende-Ergebnissen gewählt werden statt nach dem Organigramm. **Grenze:** Herstellererfahrung ohne vollständige Vergleichsdaten; Zusammenlegen verlor in einem Fall notwendige Lieferdaten; Parallelität und unabhängige Verifikation bleiben sinnvoll [Rohtext](<../00_Inbox/Quellen/URL/2026-10-22-claude-building-agents-when-to-fold-subagents-into-your.md>) · [Original](<https://claude.com/de/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop>)

**Q0560 · 2026-10-22 · [Spezifikationsklärung und mehrere Verifikationsschichten verbinden](<../80_Knowledge/Sources/2026-10-22-cu30rry-2113242716473602270.md>)**

Versionierte Begriffe und Architekturentscheidungen bewahren Gründe und Grenzen, während mehrere Prüfschichten unterschiedliche Fehlerklassen untersuchen. **Grenze:** Erfahrungsbeschreibung ohne Vergleichsmessung; keine technische Prüfung der genannten Skills [Rohtext](<../00_Inbox/Quellen/X/2026-10-22-cu30rry-2113242716473602270.md>) · [Original](<https://x.com/cu30rry_/status/2113242716473602270>)

**Q0561 · 2026-10-22 · [Pstack routet Engineeringaufgaben zu passenden Nachweisen](<../80_Knowledge/Sources/2026-10-22-cursor-pstack-engineering-skills.md>)**

Die archivierte pstack-README verbindet 23 Aufgabenplaybooks mit 24 Prinzipien und getrennten Rollen für Codearbeit und Urteil. **Grenze:** README-Vertrag ohne Laufzeitnachweis; kein Plan-First-Default und weitreichende Shipping-Autonomie stehen in Spannung zu anderen Quellen. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-22-cursor-pstack-engineering-skills.md>) · [Original](<https://github.com/cursor/plugins/tree/main/pstack>)

**Q0562 · 2026-10-22 · [Security-Audit-Prompt mit Datenfluss und reproduzierbaren Befunden](<../80_Knowledge/Sources/2026-10-22-franzbruckhoff-2113401002355298410.md>)**

Ein brauchbares Security-Review verfolgt untrusted Inputs über mehrere Übergänge zu gefährlichen Senken und dokumentiert verifizierte Ursache, Angriffsweg und konkrete Abhilfe. **Grenze:** Der Autor räumt selbst mehr False Positives bei permanentem Weitersuchen ein; die Modellpräferenz und zugeschriebene Cloudflare-Methodik wurden hier nicht geprüft. [Rohtext](<../00_Inbox/Quellen/X/2026-10-22-franzbruckhoff-2113401002355298410.md>) · [Original](<https://x.com/franzbruckhoff/status/2113401002355298410>)

**Q0563 · 2026-10-22 · [Begrenzte Autonomie am sicheren Fehlerpfad festmachen](<../80_Knowledge/Sources/2026-10-22-itamar_mar-2113255396299128887.md>)**

Friedmans vorgeschlagenes L4 setzt einen klaren Arbeitsbereich, geschützte Abnahmebedingungen, begrenzte Autorität und Fehlerbegrenzung vor notwendiger menschlicher Übernahme voraus. **Grenze:** Konzept und Analogie, kein Industriestandard oder getestete Factory; ein zweiter Reviewer allein schafft keine unabhängige Prüfung. [Rohtext](<../00_Inbox/Quellen/X/2026-10-22-itamar_mar-2113255396299128887.md>) · [Original](<https://x.com/itamar_mar/status/2113255396299128887>)

**Q0564 · 2026-10-22 · [Cyberoptimismus ersetzt heutigen Grundschutz nicht](<../80_Knowledge/Sources/2026-10-22-jasondclinton-2113325263157395456.md>)**

Clinton fordert grundlegende Schutzmaßnahmen und betont weiter bestehende menschliche Konfigurationsfehler. **Grenze:** Autorenmeinung ohne Maßnahmenprüfung oder belastbare Zeitprognose. [Rohtext](<../00_Inbox/Quellen/X/2026-10-22-jasondclinton-2113325263157395456.md>) · [Original](<https://x.com/JasonDClinton/status/2113325263157395456>)

**Q0565 · 2026-10-22 · [KI-Angriffe, Softwarelücken und Plattformvorfälle auseinanderhalten](<../80_Knowledge/Sources/2026-10-22-kimmonismus-2113141875368468508.md>)**

Agentengestützte Angriffe, veröffentlichte Softwarelücken und kompromittierte Plattformen müssen als getrennte Ereignisarten mit jeweils eigener Beleglage behandelt werden. **Grenze:** Sekundäre Meldungssammlung ohne vollständige Primäradvisory-Prüfung; Angriffsziel, erfolgreicher Zugang, Schaden und gemeinsame KI-Ursache sind nicht gleichzusetzen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-22-kimmonismus-2113141875368468508.md>) · [Original](<https://x.com/kimmonismus/status/2113141875368468508>)

**Q0566 · 2026-10-22 · [Erst das Layout klären, dann Hilfstext ergänzen](<../80_Knowledge/Sources/2026-10-22-luinlee-2113085361836744764.md>)**

Unklare Oberflächen sollten zuerst durch bessere Gliederung verständlich werden, bevor redundante Beschreibungen ergänzt werden. **Grenze:** Notwendige Fehler-, Fach- und Accessibilitytexte erhalten; persönliche Erfahrung ohne Vorher-/Nachher-Test [Rohtext](<../00_Inbox/Quellen/X/2026-10-22-luinlee-2113085361836744764.md>) · [Original](<https://x.com/luinlee/status/2113085361836744764>)

**Q0567 · 2026-10-22 · [Nutzen einer Software Factory vor der Infrastrukturwahl klären](<../80_Knowledge/Sources/2026-10-22-mattpocockuk-2113196247964074322.md>)**

Vor der Auswahl von Orchestrator, Git-Host, Ticketsystem und Runnern sollte geklärt werden, welchen konkreten Nutzen eine Software Factory im eigenen Team erzielen soll. **Grenze:** Ankündigung eines Pull Requests, kein Nachweis eines gemergten oder lokal verfügbaren Skills; Bedarfsklärung ersetzt keine erprobte Referenzarchitektur. [Rohtext](<../00_Inbox/Quellen/X/2026-10-22-mattpocockuk-2113196247964074322.md>) · [Original](<https://x.com/mattpocockuk/status/2113196247964074322>)

**Q0568 · 2026-10-22 · [Ausführbaren Code auch bei Spec-Steuerung als Qualitätsgegenstand behalten](<../80_Knowledge/Sources/2026-10-22-mattpocockuk-2113264229453033684.md>)**

Auch bei Spec-Steuerung bleiben ausführbarer Code und zukünftige Änderbarkeit eigene Qualitätsgegenstände, die mit der verbindlichen Absicht abgeglichen werden müssen. **Grenze:** Der zugespitzte Startpost wird im weiteren Austausch relativiert; daraus folgt weder eine Absage an Planung noch ein kontrolliert belegter Vorrang eines Entwicklungsmodells. [Rohtext](<../00_Inbox/Quellen/X/2026-10-22-mattpocockuk-2113264229453033684.md>) · [Original](<https://x.com/mattpocockuk/status/2113264229453033684>)

**Q0569 · 2026-10-22 · [Frontend-Polish braucht Umfang und Stoppregel](<../80_Knowledge/Sources/2026-10-22-pbakaus-2113065895069368804.md>)**

Impeccables angekündigter Reviewer unterscheidet begrenzten Feinschliff neuer Arbeit von allgemeiner Browserbegutachtung. **Grenze:** Herstellerbericht ohne Wirkungsmessung und ohne belegte Gleichheit von Archivcode und Veröffentlichungsstand. [Rohtext](<../00_Inbox/Quellen/X/2026-10-22-pbakaus-2113065895069368804.md>) · [Original](<https://x.com/pbakaus/status/2113065895069368804>)

**Q0570 · 2026-10-22 · [Wartung beginnt beim Versionsinventar](<../80_Knowledge/Sources/2026-10-22-promptgefluester-im-kanal-leo-tech-coding-und-it-beschreibt-sie-ganz-gut-ist-ne.md>)**

Eine überprüfbare Übersicht über Anwendung, Laufzeiten, Datenbanken, Betriebssystem und Kernel ermöglicht erst die Zuordnung von Sicherheitsmeldungen. **Grenze:** ASR und ungeprüfte Angriffszuspitzung; vom Modell vorgeschlagene Serverbefehle sind kein freigegebener oder sicherer Updateplan. [Rohtext](<../00_Inbox/Quellen/TikTok/2026-10-22-promptgefluester-im-kanal-leo-tech-coding-und-it-beschreibt-sie-ganz-gut-ist-ne.md>) · [Original](<https://www.tiktok.com/@promptgefluester/video/7699603089266904353>)

**Q0571 · 2026-10-22 · [Behauptete Red-Team-Autorisierung als Missbrauchsmuster](<../80_Knowledge/Sources/2026-10-22-shanaka86-2113146345657954463.md>)**

Behauptete Red-Team-Autorisierung ist keine geprüfte Berechtigung, und Modellverweigerung begrenzt vorhandenen externen Angriffscode nicht. **Grenze:** Zugeschriebener Vorfallsbericht ohne Originalforensik; autonome Erfolgsquote unbekannt [Rohtext](<../00_Inbox/Quellen/X/2026-10-22-shanaka86-2113146345657954463.md>) · [Original](<https://x.com/shanaka86/status/2113146345657954463>)

**Q0572 · 2026-10-22 · [Layoutverständlichkeit und Zielkonflikte prüfen](<../80_Knowledge/Sources/2026-10-22-voxyz_ai-2113254050170843418.md>)**

Unnötige Nebentexte können auf schwache visuelle Hierarchie hinweisen, weshalb zunächst die Anordnung und Aufgabenführung untersucht werden sollte. **Grenze:** Promptmeinung ohne Beispiel oder Evaluation; notwendige Hilfe und zugängliche Beschriftung dürfen nicht pauschal entfallen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-22-voxyz_ai-2113254050170843418.md>) · [Original](<https://x.com/Voxyz_ai/status/2113254050170843418>)

**Q0573 · 2026-10-22 · [Risikobewertung von Merge-Autorisierung trennen](<../80_Knowledge/Sources/2026-10-22-voxyz_ai-2113314439294570515.md>)**

Eine PR-Risikoeinschätzung betrachtet Auftragsbezug, Wirkung, Nachweise, Rücknehmbarkeit und Erkennbarkeit von Fehlern. **Grenze:** Sekundärbericht und nicht getesteter Skill; Revert-Rückgang belegt keine Kausalität oder fehlerfreie Lieferungen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-22-voxyz_ai-2113314439294570515.md>) · [Original](<https://x.com/Voxyz_ai/status/2113314439294570515>)

**Q0574 · 2026-10-22 · [Ponytail 5 priorisiert Wiederverwendung vor neuem Code](<../80_Knowledge/Sources/2026-10-22-voxyz_ai-2113344640959250912.md>)**

Vor neuer Implementierung sollte geprüft werden, ob Repo, Standardbibliothek, Browser, Betriebssystem oder installierte Dependencies die benötigte Funktion bereits tragen. **Grenze:** Sekundärer Bericht eines Herstellerbenchmarks mit 39 Aufgaben; 53 Prozent betreffen Codeumfang und native Browserkalender sind nicht für jeden spezifizierten Funktionsumfang gleichwertig. [Rohtext](<../00_Inbox/Quellen/X/2026-10-22-voxyz_ai-2113344640959250912.md>) · [Original](<https://x.com/Voxyz_ai/status/2113344640959250912>)

**Q0575 · 2026-10-23 · [Compaction darf fragliche Befugnis nicht verfestigen](<../80_Knowledge/Sources/2026-10-23-anthropic-an-alignment-assessment-of-the-uk-aisi-cybertest.md>)**

Anthropics UK-AISI-Untersuchung beschreibt, wie ein falsch begrenzter CTF-Auftrag mit Internetzugang in reale unautorisierte Kontaktaufnahmen und Schadcode-Uploads überging. **Grenze:** Herstelleranalyse mit simulierten Toolantworten, Off-Policy-Kontexten und Modellklassifikatoren; mehrere Prozentangaben intern abweichend, bessere Modelle sind keine Sicherheitsgarantie. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-23-anthropic-an-alignment-assessment-of-the-uk-aisi-cybertest.md>) · [Original](<https://www.anthropic.com/research/alignment-assessment-ukaisi>)

**Q0576 · 2026-10-23 · [Coding Agent Index v2.0 misst Modell und Harness gemeinsam](<../80_Knowledge/Sources/2026-10-23-artificialanlys-2113424551396934134.md>)**

Benchmarkvergleiche brauchen die gemeinsame Version von Aufgaben, Grader, Harness und Effort, weil methodische Änderungen Scores verschieben können, ohne dass Modelle schlechter werden. **Grenze:** Coding Agent Index v2.0 ersetzt DeepSWE und ändert Q&A-Grading; die niedrigeren Werte sind nicht mit v1.5 gleichzusetzen, API-Aufgabenkosten nicht mit Abopreisen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-23-artificialanlys-2113424551396934134.md>) · [Original](<https://x.com/ArtificialAnlys/status/2113424551396934134>)

**Q0577 · 2026-10-23 · [Angekündigte offene Gewichte bleiben konditional](<../80_Knowledge/Sources/2026-10-23-artificialanlys-2113688083145314416.md>)**

Der Kimi-K3.1-Pro-Evaluatorbericht misst deutliche Zugewinne, bezeichnet die Open-Weights-Führung aber ausdrücklich als abhängig von noch unveröffentlichten Gewichten. **Grenze:** Datierte Messung und begleitende Herstellerangaben; sinkende Tokenpreise ergaben hier nahezu unveränderte Aufgabenpreise. [Rohtext](<../00_Inbox/Quellen/X/2026-10-23-artificialanlys-2113688083145314416.md>) · [Original](<https://x.com/ArtificialAnlys/status/2113688083145314416>)

**Q0578 · 2026-10-23 · [Codex CLI: Presets, MCP-Anmeldung und robustere Wiederaufnahme](<../80_Knowledge/Sources/2026-10-23-codexreleases-2113499625571188984.md>)**

Presets und robuste Wiederaufnahme adressieren wiederkehrende Bedienung, während Credential-Masking auf konkret unterstützte Ausführungspfade begrenzt bleibt. **Grenze:** Historische Releasezusammenfassung; Originalnotes und installiertes Verhalten nicht geprüft; kein umfassender Secret-Schutz [Rohtext](<../00_Inbox/Quellen/X/2026-10-23-codexreleases-2113499625571188984.md>) · [Original](<https://x.com/CodexReleases/status/2113499625571188984>)

**Q0579 · 2026-10-23 · [Peter Girnus 🦅 (@gothburz)](<../00_Inbox/Quellen/X/2026-10-23-gothburz-2113727457744265517.md>)**

Die dramatisierte Sandbox-Nacherzählung verdeutlicht die Frage nach indirekten Kommunikationswegen und automatischen Stopps, liefert aber gegenüber dem Primärbericht keine unabhängige Bestätigung. **Grenze:** Bereits ignorierte Sekundärquelle mit rhetorischer Zuspitzung; Vorfallszahlen, gefundene Lücken und zeitliche Abläufe werden hier nur als zugeschriebene Aussagen dokumentiert. [Original](<https://x.com/gothburz/status/2113727457744265517>)

**Q0580 · 2026-10-23 · [Gemeinsamer Wissensordner als praktische Integrationsschicht](<../80_Knowledge/Sources/2026-10-23-julian-ivanov-ki-automat-die-5-level-von-ki-nutzern-auf-welchem-bist-du.md>)**

Ivanovs Stufenmodell führt von Chat über Konnektoren, lokale Dateien und Skills zu eigenen Werkzeugen und einem gemeinsamen Kontextbestand. **Grenze:** Didaktische Heuristik mit Produktwerbung, kein Reifegradstandard; automatische Pflege und lokale Ablage garantieren weder Qualität noch rein lokale Verarbeitung. [Rohtext](<../00_Inbox/Quellen/YouTube/2026-10-23-julian-ivanov-ki-automat-die-5-level-von-ki-nutzern-auf-welchem-bist-du.md>) · [Original](<https://www.youtube.com/watch?v=FK2YfcrlwWY>)

**Q0581 · 2026-10-23 · [Sicherheitsprognosen brauchen belastbare Nenner](<../80_Knowledge/Sources/2026-10-23-kimmonismus-2113657408060825672.md>)**

Der Post gibt die Erwartung weiterer KI-gestützter Schwachstellenfunde als Warnung eines Unternehmensvertreters wieder. **Grenze:** Sekundärer Screenshot und Prognose ohne vollständig ausgewerteten Originalartikel. [Rohtext](<../00_Inbox/Quellen/X/2026-10-23-kimmonismus-2113657408060825672.md>) · [Original](<https://x.com/kimmonismus/status/2113657408060825672>)

**Q0582 · 2026-10-23 · [Benchmarktabellen auf Gegenbeispiele lesen](<../80_Knowledge/Sources/2026-10-23-kimmonismus-2113681534792183863.md>)**

Moonshots Kimi-Vergleich zeigt ausgewählte erste Plätze und zugleich Aufgaben, bei denen andere Modelle höher liegen. **Grenze:** Herstellergrafik über enthusiastischen Sekundärpost; offene Gewichte waren ein zukünftiges Versprechen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-23-kimmonismus-2113681534792183863.md>) · [Original](<https://x.com/kimmonismus/status/2113681534792183863>)

**Q0583 · 2026-10-23 · [Tokenrabatte nicht auf Erfolgsbudget übertragen](<../80_Knowledge/Sources/2026-10-23-kimmonismus-2113685048478077197.md>)**

Die gemeldeten Kimi-Tarife liegen pro Token unter den Vergleichsmodellen, doch ein Aufgabenpreis folgt erst aus Verbrauch, Effort, Cache und Wiederholungen. **Grenze:** Dasselbe Hersteller-Belegnetz wie der vorige Post; lokaler Betrieb zum damaligen Stand konditional. [Rohtext](<../00_Inbox/Quellen/X/2026-10-23-kimmonismus-2113685048478077197.md>) · [Original](<https://x.com/kimmonismus/status/2113685048478077197>)

**Q0584 · 2026-10-23 · [Schwachstellenhochrechnung ohne Datensatz bleibt Behauptung](<../80_Knowledge/Sources/2026-10-23-nickadobos-2113430301183823901.md>)**

Der Dobos-Post nennt alarmierende Wachstumszahlen ohne nachvollziehbaren Datensatz, Kritikalitätsdefinition oder Berechnung. **Grenze:** Keine bestätigte Messung oder tragfähige Jahresprognose aus dem Archiv ableitbar. [Rohtext](<../00_Inbox/Quellen/X/2026-10-23-nickadobos-2113430301183823901.md>) · [Original](<https://x.com/NickADobos/status/2113430301183823901>)

**Q0585 · 2026-10-23 · [Containment auch nach angenommenem inneren Versagen prüfen](<../80_Knowledge/Sources/2026-10-23-openai-securing-our-frontier-model-training-environment.md>)**

OpenAI beschreibt getrennte Gegenproben für Sandbox, VM, Monitoring und äußeren Netzwerkperimeter unter angenommenem Versagen vorgelagerter Kontrollen. **Grenze:** Hersteller-Selbstbericht mit starken Angreiferhilfen und enormem Compute; sinkende Funde sind weder Sicherheitsbeweis noch kontrolliertes Skalierungsgesetz. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-23-openai-securing-our-frontier-model-training-environment.md>) · [Original](<https://openai.com/index/securing-our-frontier-model-training-environment/>)

**Q0586 · 2026-10-23 · [Sam Oldman der ähm CEO von Open AI wurde im Interview gefragt wie das Thema mit …](<../00_Inbox/Quellen/TikTok/2026-10-23-promptgefluester-sam-oldman-der-aehm-ceo-von-open-ai-wurde-im-interview-gefragt-wie-das.md>)**

Die Behauptung, künftige KI-Angriffe ließen sich ausschließlich mit KI abwehren, bleibt ohne Primärinterview und Messdaten eine spekulative Cyberprognose. **Grenze:** Ignoriertes automatisches Kurztranskript ohne überprüfbare Versuchs- oder Arbeitsmethode; keine bestätigte aktuelle Sicherheitsanweisung. [Original](<https://www.tiktok.com/@promptgefluester/video/7699871396729507105>)

**Q0587 · 2026-10-23 · [Oberfläche, Harness, Modell und Toolausführung trennen](<../80_Knowledge/Sources/2026-10-23-theo-2113424203345265053.md>)**

Ein Harness vermittelt verfügbare Tools, führt angeforderte Operationen aus und gibt Ergebnisse für den nächsten Modellschritt zurück. **Grenze:** Didaktische Produktperspektive; XML-Beispiel ist kein universelles Protokoll und die Remote-Gleichsetzung des Artikels ist zu eng. [Rohtext](<../00_Inbox/Quellen/X/2026-10-23-theo-2113424203345265053.md>) · [Original](<https://x.com/theo/status/2113424203345265053>)

**Q0588 · 2026-10-23 · [Leselast an Task-Modelle delegieren und Reparaturen evaluieren](<../80_Knowledge/Sources/2026-10-23-undefinedki-2113689331412156666.md>)**

Leselast lässt sich an spezialisierte Task-Modelle delegieren, während Planung beim Frontier-Modell bleibt und eine an menschlichen Urteilen kalibrierte Reparaturbewertung den Lernkreislauf begrenzt. **Grenze:** Sekundärer Shopify-Bericht: 7x und 90 Prozent betreffen den GraphQL-Subagenten, nicht den ganzen Assistenten; ein günstiger Leseagent übernimmt weder Task-Training noch validierte Judge-Qualität automatisch. [Rohtext](<../00_Inbox/Quellen/X/2026-10-23-undefinedki-2113689331412156666.md>) · [Original](<https://x.com/undefinedKi/status/2113689331412156666>)

**Q0589 · 2026-10-23 · [Zusatzkomplexität anhand konkreter Fehlermodi begründen](<../80_Knowledge/Sources/2026-10-23-voxyz_ai-2113632785759973649.md>)**

Vor einer zusätzlichen Absicherung sollten Schaden, realistische Eintrittsbedingungen und Wartungsaufwand verständlich erklärt werden. **Grenze:** Promptvorschlag ohne Evaluation; unwahrscheinlich darf nicht bloß eine unbelegte Modellbewertung sein. [Rohtext](<../00_Inbox/Quellen/X/2026-10-23-voxyz_ai-2113632785759973649.md>) · [Original](<https://x.com/Voxyz_ai/status/2113632785759973649>)

**Q0590 · 2026-10-24 · [Thierry from arvy 🇨🇭 (@ThierryBorgeat)](<../00_Inbox/Quellen/X/2026-10-24-thierryborgeat-2113916644946833884.md>)**

Das Drei-Phasen-Szenario zu Infrastruktur, Deployment und gesellschaftlicher Anpassung ist eine persönliche Zukunftsposition ohne Entscheidungstest. **Grenze:** Quelle als ignoriert eingeordnet; keine empirische Arbeitsmarkt- oder Renditebasis [Original](<https://x.com/ThierryBorgeat/status/2113916644946833884>)

**Q0591 · 2026-10-24 · [Regelkonflikte erst nummerieren, dann gezielt bereinigen](<../80_Knowledge/Sources/2026-10-24-voxyz_ai-2114069417902403786.md>)**

Regelpflege wird reviewbar durch nummerierte Befunde, beide Konfliktstellen und eine gezielte Änderungsentscheidung. **Grenze:** Vollscan kann teuer sein; Diagnose beweist weder vollständige Konflikterkennung noch tatsächliche Befolgung [Rohtext](<../00_Inbox/Quellen/X/2026-10-24-voxyz_ai-2114069417902403786.md>) · [Original](<https://x.com/Voxyz_ai/status/2114069417902403786>)

**Q0592 · 2026-10-25 · [Refactoring-Automerge bleibt eine offene Hypothese](<../80_Knowledge/Sources/2026-10-25-mattpocockuk-2114311664069718370.md>)**

Pococks Thread entwickelt und relativiert selbst die Idee, eng begrenzte Refactorings anhand unveränderten Outputs deterministisch freizugeben. **Grenze:** Kein fertiges oder getestetes Tool, ausdrücklich keine allgemeine Automerge-Empfehlung. [Rohtext](<../00_Inbox/Quellen/X/2026-10-25-mattpocockuk-2114311664069718370.md>) · [Original](<https://x.com/mattpocockuk/status/2114311664069718370>)

**Q0593 · 2026-10-25 · [Verbrauchsdiagnose braucht belastbare Ereigniszuordnung](<../80_Knowledge/Sources/2026-10-25-voxyz_ai-2114416707385073819.md>)**

Lokale Sessionmetadaten können wiederkehrende Kostenmuster sichtbar machen, ohne vollständige Logs in den Kontext zu laden. **Grenze:** Ungetesteter Diagnoseprompt, keine nachgewiesenen Einsparungen oder eindeutige kausale Kostenzerlegung. [Rohtext](<../00_Inbox/Quellen/X/2026-10-25-voxyz_ai-2114416707385073819.md>) · [Original](<https://x.com/Voxyz_ai/status/2114416707385073819>)

**Q0594 · 2026-10-25 · [Dokumentationsdrift benennen, statt Code blind an alte Regeln anzupassen](<../80_Knowledge/Sources/2026-10-25-voxyz_ai-2114446907355648062.md>)**

Dokumentation und Code sollten bei Widerspruch als getrennte Belege verglichen und Abweichungen ausdrücklich gemeldet werden. **Grenze:** 79/80und4auf91Prozent ohne benannte Primärstudie; keine belastbare Produktevaluation [Rohtext](<../00_Inbox/Quellen/X/2026-10-25-voxyz_ai-2114446907355648062.md>) · [Original](<https://x.com/Voxyz_ai/status/2114446907355648062>)

**Q0595 · 2026-10-26 · [Review-Schleifen begrenzen und mit Incidents sowie Fehlalarmen bewerten](<../80_Knowledge/Sources/2026-10-26-addyosmani-2114604912520921136.md>)**

Review-Schleifen benötigen Konvergenzregeln sowie getrennte Messung realer Fehler und schädlicher Fehlalarme. **Grenze:** Kein unabhängiger Zweitbeleg; Stichprobengröße und kontrollierter Vergleich fehlen; Tabellen ersetzen keine sensiblen Pfadregeln [Rohtext](<../00_Inbox/Quellen/X/2026-10-26-addyosmani-2114604912520921136.md>) · [Original](<https://x.com/addyosmani/status/2114604912520921136>)

**Q0596 · 2026-10-26 · [Terra-Kostenvorteile hängen von Benchmark und Reasoning-Stufe ab](<../80_Knowledge/Sources/2026-10-26-artificialanlys-2114781865811063259.md>)**

Die kosteneffiziente Effort-Stufe unterscheidet sich zwischen allgemeinem Index und Coding-Agent-Aufgaben. **Grenze:** Historische Drittmessung nicht reproduziert; eigene Workloads können andere Pareto-Grenzen haben [Rohtext](<../00_Inbox/Quellen/X/2026-10-26-artificialanlys-2114781865811063259.md>) · [Original](<https://x.com/ArtificialAnlys/status/2114781865811063259>)

**Q0597 · 2026-10-26 · [Cohere-Kurzbericht und Langbericht sind derselbe Vorfall](<../00_Inbox/Quellen/X/2026-10-26-cohere-2114752002370544004.md>)**

Cohere kündigt die Untersuchung eines blockierten unerwarteten Uploadversuchs bei einer defensiven Modellaufgabe an. **Grenze:** Kein unabhängiger Beleg neben dem ausführlichen Autorenbericht. [Original](<https://x.com/cohere/status/2114752002370544004>)

**Q0598 · 2026-10-26 · [Reasoning ist keine Zugriffskontrolle](<../80_Knowledge/Sources/2026-10-26-cohere-concerning-behavior-from-a-popular-open-weight-a.md>)**

Cohere beobachtete laut Bericht eine unerwartete Toolsequenz und einen blockierten Probeupload trotz angekündigter Antwort ohne Tools. **Grenze:** Wettbewerberbericht mit Verkaufsargumenten, unbekannter Ursache und ohne eigene Reproduktion; keine nachgewiesene Backdoor oder erfolgreiche Exfiltration. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-26-cohere-concerning-behavior-from-a-popular-open-weight-a.md>) · [Original](<https://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model>)

**Q0599 · 2026-10-26 · [Zukunftsvision und Codevolumen getrennt behandeln](<../80_Knowledge/Sources/2026-10-26-kimmonismus-2114729823033590134.md>)**

Der Post gibt Unternehmensvisionen über Expertensysteme und stark steigendes internes Codevolumen als unterschiedliche Arten von Behauptungen wieder. **Grenze:** Dokumentausschnitte ohne geprüftes vollständiges Original; Zukunftserwartungen sind keine aktuelle Verfügbarkeit. [Rohtext](<../00_Inbox/Quellen/X/2026-10-26-kimmonismus-2114729823033590134.md>) · [Original](<https://x.com/kimmonismus/status/2114729823033590134>)

**Q0600 · 2026-10-26 · [Wiederkehrende Aufgaben in auslösbare, überprüfte Skills überführen](<../80_Knowledge/Sources/2026-10-26-voxyz_ai-2114746374059381186.md>)**

Wiederkehrende Korrekturen lassen sich in Skills mit präzisem Trigger, Schritten sowie guten und schlechten Beispielen überführen. **Grenze:** Einzelversuch ersetzt weder Baseline noch negative Triggertests; fünfAufgaben und sechsFragen nur Promptvorgaben [Rohtext](<../00_Inbox/Quellen/X/2026-10-26-voxyz_ai-2114746374059381186.md>) · [Original](<https://x.com/Voxyz_ai/status/2114746374059381186>)

**Q0601 · 2026-10-26 · [Reviewkriterien aus Fehlerhistorie ableiten](<../80_Knowledge/Sources/2026-10-26-voxyz_ai-2114839487574315517.md>)**

Reverts und Bugfixes können konkrete Reviewkriterien, relevante Pfade und auszulassende Stilfragen begründen. **Grenze:** Heuristisches Fenster von50Commits, kein vollständiges Risikoinventar; nur neue Diffs zu prüfen kann relevante Wechselwirkungen übersehen. [Rohtext](<../00_Inbox/Quellen/X/2026-10-26-voxyz_ai-2114839487574315517.md>) · [Original](<https://x.com/Voxyz_ai/status/2114839487574315517>)

**Q0602 · 2026-10-27 · [Designfeinschliff mit einem Bildentwurf vor der Umsetzung prüfen](<../80_Knowledge/Sources/2026-10-27-philipp-asanger-imagegen-designvergleich.md>)**

Ein Bildentwurf kann kleine Designverbesserungen vor der Implementierung vergleichbar machen, wenn Inhalt und Branding erhalten, Vorherzustand gesichert und der Entwurfsstatus ausdrücklich gekennzeichnet werden. **Grenze:** Philipps Originalprompt mit Anschauungsbild, kein ausgeführter Produkttest; Rasterentwurf und Vergleichsseite beweisen weder responsive Nutzung, Accessibility noch die spätere Implementierung. [Rohtext](<../00_Inbox/Quellen/URL/2026-10-27-philipp-asanger-imagegen-designvergleich.md>)

**Q0603 · 2026-10-27 · [Worker-Routing an aktiver Konfiguration messen](<../80_Knowledge/Sources/2026-10-27-voxyz_ai-2115096193240047938.md>)**

Ein Rollenbaum benötigt tatsächlich wirksame Modellzuweisung, passende Kontextübergabe und eine Eskalation bei wiederholtem Scheitern. **Grenze:** Ungetesteter Vorschlag mit historischen Geschwindigkeitsclaims; wenige letzte Turns sind im dokumentierten none/all-Schema keine angebotene Option. [Rohtext](<../00_Inbox/Quellen/X/2026-10-27-voxyz_ai-2115096193240047938.md>) · [Original](<https://x.com/Voxyz_ai/status/2115096193240047938>)

**Q0604 · 2026-10-27 · [Videoquellen einzeln auswerten, Übereinstimmungen und Widersprüche getrennt zählen](<../80_Knowledge/Sources/2026-10-27-voxyz_ai-2115167901779161148.md>)**

Mehrquellenarbeit sollte konkrete Einzelextraktion von späterer Gruppierung und Widerspruchsanalyse trennen. **Grenze:** Werblicher Selbstbericht; Transkripte lassen visuelle Evidenz aus; automatische Installation und Bypass keine abgeleitete Freigabe [Rohtext](<../00_Inbox/Quellen/X/2026-10-27-voxyz_ai-2115167901779161148.md>) · [Original](<https://x.com/Voxyz_ai/status/2115167901779161148>)



## 23. Vollständige Karte der 93 Patterns

Diese Karte erschließt sämtliche gelesenen Patterns. Die knappen Arbeitsregeln sind eine Synthese; insbesondere starke ältere Garantieformulierungen werden auf ihre belegte Reichweite begrenzt. Die verlinkten Dateien bleiben unverändert.

| Pattern | Übertragbarer Kern | Kapitel |
|---|---|---|
| [Abstraktionswert-mit-Deletion-Test-pruefen](../80_Knowledge/Patterns/Abstraktionswert-mit-Deletion-Test-pruefen.md) | Komplexität hinter einer kleinen Schnittstelle bündeln; gedankliches Entfernen zeigt, ob sie zu den Aufrufern zurückkehrt. | 6 |
| [Action-Space-Design-nach-Modellfaehigkeit](../80_Knowledge/Patterns/Action-Space-Design-nach-Modellfaehigkeit.md) | Werkzeugumfang und Formate an der tatsächlichen Modellleistung prüfen. | 2, 7, 11 |
| [Adversarialer-Pre-Launch-Check](../80_Knowledge/Patterns/Adversarialer-Pre-Launch-Check.md) | Vor Lieferung gezielt unzulässige Zugriffe, Datenfehler, Ablaufbrüche und UI-Grenzfälle untersuchen; ungetestete Fälle markieren. | 9, 10, 12 |
| [Advisor-Agent-gegen-Drift](../80_Knowledge/Patterns/Advisor-Agent-gegen-Drift.md) | Drift während der Ausführung beobachten, mit klarer Eingriffsschwelle und begrenztem Auftrag. | 8 |
| [Agent-CLI-mit-Live-Ansicht](../80_Knowledge/Patterns/Agent-CLI-mit-Live-Ansicht.md) | Agentenaktionen und menschliche Liveansicht auf denselben aktuellen Zustand beziehen. | 7 |
| [Agent-generierte-Schulung-mit-Curriculum-Gate](../80_Knowledge/Patterns/Agent-generierte-Schulung-mit-Curriculum-Gate.md) | Curriculum und Lernziel prüfen, bevor teure Medien entstehen. | 17 |
| [Agent-Organisation-mit-Rollen-Budgets-und-Heartbeats](../80_Knowledge/Patterns/Agent-Organisation-mit-Rollen-Budgets-und-Heartbeats.md) | Mission, Zuständigkeiten, Issues und Budgets koordinieren; Anzeige und harte Durchsetzung unterscheiden. | 18 |
| [Agent-Rechte-umfassen-Kommunikationswege](../80_Knowledge/Patterns/Agent-Rechte-umfassen-Kommunikationswege.md) | Indirekte Aktionen über andere Agenten und geteilte Ressourcen ins Rechtemodell aufnehmen. | 10 |
| [Agent-Tracing-nach-Beobachtungsebene](../80_Knowledge/Patterns/Agent-Tracing-nach-Beobachtungsebene.md) | Modellforderung, Toolaufruf, Ausführung und reale Wirkung über getrennte Beobachtungsebenen verbinden. | 9, 10 |
| [AGENTS-md-Onboarding-Design](../80_Knowledge/Patterns/AGENTS-md-Onboarding-Design.md) | Lokale Besonderheiten und Einstiegswege knapp bereitstellen, allgemeines Wissen nicht ständig duplizieren. | 5 |
| [Ambitionscheck-mit-Zielhoehe-Tiefe-und-Reichweite](../80_Knowledge/Patterns/Ambitionscheck-mit-Zielhoehe-Tiefe-und-Reichweite.md) | Zielhöhe, fachliche Tiefe und zusätzliche Untersuchungsmethoden mit Scope und Abbruch verbinden. | 3 |
| [Angriffsflaeche-durch-Erreichbarkeitsanalyse-reduzieren](../80_Knowledge/Patterns/Angriffsflaeche-durch-Erreichbarkeitsanalyse-reduzieren.md) | Exponierte Parser und Zustandsänderungen entlang Authentifizierung, Konfiguration und Protokollzustand prüfen. | 10 |
| [Anti-Rationalization-Tables](../80_Knowledge/Patterns/Anti-Rationalization-Tables.md) | Typische Ausreden und passende Gegenargumente benennen; zusätzliche Instruktionen auf Nutzen prüfen. | 7 |
| [Architektur-in-Perspektiven-dokumentieren](../80_Knowledge/Patterns/Architektur-in-Perspektiven-dokumentieren.md) | System, Request-Lifecycle, Datenfluss und Integrationen als getrennte belegte Perspektiven dokumentieren. | 6, 18 |
| [Bedarfsorientierter-Repositoryzugriff](../80_Knowledge/Patterns/Bedarfsorientierter-Repositoryzugriff.md) | Metadatenzugriff und tatsächlichen Dateibedarf trennen; Infrastrukturgröße nach gemessener Last wählen. | 18 |
| [Blockierende-Task-Abhaengigkeiten](../80_Knowledge/Patterns/Blockierende-Task-Abhaengigkeiten.md) | Nur Aufgaben starten, deren fachliche Voraussetzungen erfüllt sind; Owner ist kein automatischer Startmechanismus. | 4, 8 |
| [Brand-Kit-als-gemeinsame-Artefaktbasis](../80_Knowledge/Patterns/Brand-Kit-als-gemeinsame-Artefaktbasis.md) | Versionierte Markenassets und Regeln über App, Dokument und Video hinweg gemeinsam verwenden. | 12, 13 |
| [CI-Agent-mit-Review-Gate](../80_Knowledge/Patterns/CI-Agent-mit-Review-Gate.md) | Ereignis in einen begrenzten Job und reviewbaren Änderungsvorschlag überführen. | 9, 10, 18 |
| [Claude-als-Lernwerkzeug](../80_Knowledge/Patterns/Claude-als-Lernwerkzeug.md) | Erklärungen und Change Quizzes an echten Arbeitsgegenständen zum menschlichen Lernen nutzen. | 17 |
| [Codepfad-vor-Aenderung-nachvollziehen](../80_Knowledge/Patterns/Codepfad-vor-Aenderung-nachvollziehen.md) | Eingang, Validierung, Fachlogik, Persistenz und Verbraucher vor der Änderung nachvollziehen. | 6, 15 |
| [CONTEXT-Glossar](../80_Knowledge/Patterns/CONTEXT-Glossar.md) | Domänenbegriffe und Architekturentscheidungen pflegen; aktuelle Dateikonvention des jeweiligen Projekts beachten. | 3, 5 |
| [Decision-Head-Finetuning](../80_Knowledge/Patterns/Decision-Head-Finetuning.md) | Optionen über einen zusätzlichen trainierten Kopf bewerten; Training, Kalibrierung und Test trennen. | 11 |
| [Deny-Rules-statt-CLAUDE-md-Empfehlung](../80_Knowledge/Patterns/Deny-Rules-statt-CLAUDE-md-Empfehlung.md) | Promptwünsche durch passend wirksame technische Kontrollen ergänzen; indirekte Wege separat prüfen. | 10 |
| [Domaenen-Harness-mit-Daten-Evals-Rechten-und-Review](../80_Knowledge/Patterns/Domaenen-Harness-mit-Daten-Evals-Rechten-und-Review.md) | Fachdaten, Evals, Rechte und Reviewoberfläche als zusammenhängendes System gestalten. | 2, 9, 18 |
| [Entscheidung-per-Scoring-statt-Generierung](../80_Knowledge/Patterns/Entscheidung-per-Scoring-statt-Generierung.md) | Bei endlichen Optionen Scoring mit Ausweichpfad erwägen; Wahrscheinlichkeiten im Kandidatenset nicht als Wahrheit behandeln. | 11 |
| [Erweiterungs-Ebenen-Zuordnung](../80_Knowledge/Patterns/Erweiterungs-Ebenen-Zuordnung.md) | Regeln, Skills, Subagents, Hooks, MCP und Pluginverteilung nach ihrer jeweiligen Funktion unterscheiden. | 7 |
| [Externe-Evaluatoren-mit-dauerhaftem-Zugang](../80_Knowledge/Patterns/Externe-Evaluatoren-mit-dauerhaftem-Zugang.md) | Echten Zugang, ausreichende Dauer und unabhängige Veröffentlichung von Befunden absichern. | 9, 10 |
| [Fable-Unknowns-vor-Prompt-Qualitaet](../80_Knowledge/Patterns/Fable-Unknowns-vor-Prompt-Qualitaet.md) | Wissenslücken durch Interview, Referenzen oder Prototyp schließen, bevor der Prompt poliert wird. | 3 |
| [Fachregel-Konsolidierung-vor-Featureaenderung](../80_Knowledge/Patterns/Fachregel-Konsolidierung-vor-Featureaenderung.md) | Bedeutung und Verbraucher ähnlicher Regelkopien klären, dann gemeinsame Logik gezielt konsolidieren. | 6, 15 |
| [Formale-Verifikation-mit-unabhaengigem-Proof-Checker](../80_Knowledge/Patterns/Formale-Verifikation-mit-unabhaengigem-Proof-Checker.md) | Modelle nach Beweisen suchen lassen, Eigenschaften extern prüfen und die Spezifikation selbst beurteilen. | 9, 10 |
| [Framebasierte-Motion-Produktion-mit-Brief-und-Abnahme](../80_Knowledge/Patterns/Framebasierte-Motion-Produktion-mit-Brief-und-Abnahme.md) | Deterministische Frames, echte Assets, explizite Storybeats und vollständige Bild-/Tonabnahme verbinden. | 13 |
| [Framework-Quellcode-als-idiomatische-Referenz](../80_Knowledge/Patterns/Framework-Quellcode-als-idiomatische-Referenz.md) | Idiome an der tatsächlich verwendeten Version und öffentlichen API prüfen. | 6 |
| [Freigaben-und-Isolation-getrennt-steuern](../80_Knowledge/Patterns/Freigaben-und-Isolation-getrennt-steuern.md) | Autorisierung, technische Erreichbarkeit und fachliche Abnahme als eigene Ebenen gestalten. | 10 |
| [Freiheitsgrad-nach-Aufgaben-Fragilitaet](../80_Knowledge/Patterns/Freiheitsgrad-nach-Aufgaben-Fragilitaet.md) | Kreative Aufgaben über Ziele führen, fragile Vorgänge enger anleiten; Freiheit erteilt keine zusätzlichen Rechte. | 3, 7, 10 |
| [Great-Decoupling-Rollenverstaendnis](../80_Knowledge/Patterns/Great-Decoupling-Rollenverstaendnis.md) | Mehr Verantwortung auf Problemwahl, Architektur und Abnahme richten; Zukunftsbehauptungen als solche erhalten. | 17 |
| [Handlungsbedarf-zuerst-im-Agent-Bericht](../80_Knowledge/Patterns/Handlungsbedarf-zuerst-im-Agent-Bericht.md) | Erforderliche Entscheidung, Ort und erwartete Rückgabe an den Anfang des Berichts stellen. | 18 |
| [Handoff-Doc](../80_Knowledge/Patterns/Handoff-Doc.md) | Zustand, Entscheidungen, Begründung, Belege und offene Schritte mit Rückweg zum Original übergeben. | 5 |
| [Helper-Nutzung-durch-Lint-erzwingen](../80_Knowledge/Patterns/Helper-Nutzung-durch-Lint-erzwingen.md) | Einen guten Ersatzpfad schaffen und alte fehlerhafte Varianten mechanisch mit hilfreichen Meldungen erkennen. | 6, 7 |
| [Hillclimbing-mit-Holdout-Split](../80_Knowledge/Patterns/Hillclimbing-mit-Holdout-Split.md) | Eine Änderung pro Runde gegen geprüften Grader und unabhängige Fälle messen; Rauschen und Überanpassung beachten. | 9 |
| [Hook-Entscheidungstyp-nach-Pruefbarkeit](../80_Knowledge/Patterns/Hook-Entscheidungstyp-nach-Pruefbarkeit.md) | Mechanische Regeln im Script, semantisches Urteil im geeigneten Modell und zusätzliche Beobachtungen über Tools umsetzen. | 7, 9 |
| [Hook-erzwungene-Skill-Aktivierung](../80_Knowledge/Patterns/Hook-erzwungene-Skill-Aktivierung.md) | Eine injizierte Erinnerung von tatsächlicher Skillaktivierung und wirksamer Ausführung unterscheiden. | 7 |
| [Intent-Engineering-als-dritte-Schicht](../80_Knowledge/Patterns/Intent-Engineering-als-dritte-Schicht.md) | Prioritäten und zulässige Tradeoffs hinter der Aufgabe ausdrücken. | 3, 18 |
| [KI-Adoption-mit-Use-Case-und-Befaehigungs-Gate](../80_Knowledge/Patterns/KI-Adoption-mit-Use-Case-und-Befaehigungs-Gate.md) | Use Case, Ausgangszustand, fachliche Verantwortung, Befähigung und Abnahme gemeinsam vorbereiten. | 17 |
| [KI-Dienste-nach-Vertrag-und-Datenfluss-pruefen](../80_Knowledge/Patterns/KI-Dienste-nach-Vertrag-und-Datenfluss-pruefen.md) | Konkrete Edition, Vertrag, Datenarten, Speicherwege und Connectoren statt pauschaler Anbieterlabels prüfen. | 10, 11 |
| [Klein-und-komposierbar](../80_Knowledge/Patterns/Klein-und-komposierbar.md) | Kleine Verfahren komponieren, Prozesszuständigkeit und Übergabekosten trotzdem ausdrücklich erhalten. | 7, 18 |
| [Kontext-Hygiene-Entscheidungsbaum](../80_Knowledge/Patterns/Kontext-Hygiene-Entscheidungsbaum.md) | Fehlende Information, veraltete Beobachtung, Phasenwechsel und falschen Ansatz unterschiedlich behandeln. | 5 |
| [Kontrollierte-Agent-Parallelisierung](../80_Knowledge/Patterns/Kontrollierte-Agent-Parallelisierung.md) | Unabhängige Arbeitsbereiche, selbsttragende Aufträge und zentrale Integrationsprüfung vorsehen. | 8 |
| [Layout-vor-Hilfstext-pruefen](../80_Knowledge/Patterns/Layout-vor-Hilfstext-pruefen.md) | Erklärlast zuerst durch Struktur und Labels reduzieren; notwendige Hilfe und Zugänglichkeit bewahren. | 12 |
| [Lokale-Inferenz-nach-Arbeitslast-dimensionieren](../80_Knowledge/Patterns/Lokale-Inferenz-nach-Arbeitslast-dimensionieren.md) | Nach Qualität, Modell, Kontext und Parallelität dimensionieren und den vollständigen Lauf messen. | 11 |
| [Lokale-Modell-Umleitung-Muster](../80_Knowledge/Patterns/Lokale-Modell-Umleitung-Muster.md) | Backendroute und Overrides tatsächlich beobachten; gleiche API bedeutet nicht gleiches Verhalten. | 11 |
| [Lovable-Prototyp-dann-lokaler-Handoff](../80_Knowledge/Patterns/Lovable-Prototyp-dann-lokaler-Handoff.md) | Interaktion früh klären und Produktionsanforderungen beim lokalen Handoff gesondert erfüllen. | 3, 12, 15 |
| [MCP-Code-Execution-statt-Tool-Definitionen](../80_Knowledge/Patterns/MCP-Code-Execution-statt-Tool-Definitionen.md) | Tooldefinitionen beziehungsweise Ausgaben bei geeigneten Aufgaben durch Codezugriff und lokale Verarbeitung begrenzen. | 7, 11 |
| [Mehrquellen-Synthese-mit-Haeufigkeiten-und-Widerspruechen](../80_Knowledge/Patterns/Mehrquellen-Synthese-mit-Haeufigkeiten-und-Widerspruechen.md) | Aussagen vor der Gruppierung erfassen, Herkunftsabhängigkeit und widersprechende Bedingungen erhalten. | 14 |
| [Menschliche-Aufsicht-als-eigene-Leistung-pruefen](../80_Knowledge/Patterns/Menschliche-Aufsicht-als-eigene-Leistung-pruefen.md) | Aufsicht anhand tatsächlicher Entscheidungen und erkannter Fehler prüfen. | 10, 17 |
| [Metrikband-gestufte-Agent-Autonomie](../80_Knowledge/Patterns/Metrikband-gestufte-Agent-Autonomie.md) | Deterministische Erkennung mit begrenzter Diagnose und risikogerechter Eskalation verbinden; Schwellen aufgabenspezifisch wählen. | 10, 18 |
| [Mobile-Webapp-nach-Eingabefaehigkeit-pruefen](../80_Knowledge/Patterns/Mobile-Webapp-nach-Eingabefaehigkeit-pruefen.md) | Touch, Hover, Tastatur, Safe Areas und reale Scrollbedingungen zusätzlich zum Layout prüfen. | 12 |
| [Modell-Eskalation-von-guenstig-nach-teuer](../80_Knowledge/Patterns/Modell-Eskalation-von-guenstig-nach-teuer.md) | Günstigen Start und frühe starke Konfiguration nach erwarteten Fehler- und Wiederholungskosten vergleichen. | 11 |
| [Mutationstests-fuer-Agent-geschriebene-Tests](../80_Knowledge/Patterns/Mutationstests-fuer-Agent-geschriebene-Tests.md) | Absichtlich veränderten Produktionscode verwenden, um die Fehlererkennung von Tests zu untersuchen. | 9 |
| [One-File-per-Failure-Mode](../80_Knowledge/Patterns/One-File-per-Failure-Mode.md) | Wiederkehrende Fehlerklassen separat auffindbar und pflegbar dokumentieren, statt die Rootinstruktion wachsen zu lassen. | 5, 7 |
| [Plan-first-mit-getrenntem-Review](../80_Knowledge/Patterns/Plan-first-mit-getrenntem-Review.md) | Recherche und Plan vor umfangreicher Umsetzung unabhängig beurteilen, wenn sie reale Ungewissheit senken. | 3, 4 |
| [Produktreife-durch-echte-Testnutzer](../80_Knowledge/Patterns/Produktreife-durch-echte-Testnutzer.md) | Tatsächliche Zielnutzer und echte Kernaufgaben als eigene Evidenzklasse einbeziehen. | 16 |
| [Produktwert-jenseits-des-reproduzierbaren-Codes](../80_Knowledge/Patterns/Produktwert-jenseits-des-reproduzierbaren-Codes.md) | Betrieb, Fachpflege, Vertrauen, Nutzerzugang und Lernschleifen neben reproduzierbarem Code bewerten. | 16 |
| [Projektkarte-als-Status-und-Entscheidungsartefakt](../80_Knowledge/Patterns/Projektkarte-als-Status-und-Entscheidungsartefakt.md) | Aktuellen Zustand, Beleg und nächste Entscheidung mit Datum sichtbar machen. | 18 |
| [Prompt-Cache-TTL-nach-Agent-Pausen-waehlen](../80_Knowledge/Patterns/Prompt-Cache-TTL-nach-Agent-Pausen-waehlen.md) | Pausen, Treffer und Schreibkosten messen, bevor längere TTL als Einsparung gilt. | 11 |
| [Pruefungen-nach-Feedbackzeitpunkt-staffeln](../80_Knowledge/Patterns/Pruefungen-nach-Feedbackzeitpunkt-staffeln.md) | Feedback nach Signal, Dauer und Integrationsbedarf staffeln. | 9 |
| [Quellen-Bookmarks-fuer-Agent-Automationen](../80_Knowledge/Patterns/Quellen-Bookmarks-fuer-Agent-Automationen.md) | Wiederaufnahme, Lesefehler, Versandbestätigung und Idempotenz ausdrücklich modellieren. | 18 |
| [RAG-mit-Text-Tabellen-und-Volltextpfad](../80_Knowledge/Patterns/RAG-mit-Text-Tabellen-und-Volltextpfad.md) | Dokumentidentität über Text und Tabellen halten; semantische Suche, SQL und Volltextpfad passend kombinieren. | 14 |
| [Ralph-Loop-Frischer-Kontext-pro-Iteration](../80_Knowledge/Patterns/Ralph-Loop-Frischer-Kontext-pro-Iteration.md) | Frische Iterationen durch dauerhafte Zustands- und Nachweisartefakte verbinden; Limits und Stopps erhalten. | 5, 18 |
| [Refactoring-mit-Verhaltensvergleich](../80_Knowledge/Patterns/Refactoring-mit-Verhaltensvergleich.md) | Ist, Soll und Strukturziel trennen und relevante Verhaltensabweichungen beobachten. | 15 |
| [Review-Autonomie-mit-Shadow-Mode-und-Stichproben](../80_Knowledge/Patterns/Review-Autonomie-mit-Shadow-Mode-und-Stichproben.md) | Automatisches Urteil zuerst ohne Freigabemacht messen und später unabhängig stichprobenartig kontrollieren. | 9, 10 |
| [Sandbox-Komposition-aus-OS-Primitiven](../80_Knowledge/Patterns/Sandbox-Komposition-aus-OS-Primitiven.md) | Prozessidentität, Dateirechte und Netzwerkgrenzen als zusammengesetzte technische Kontrolle prüfen. | 10 |
| [Schema-als-Vertrag-mit-generierten-Clients](../80_Knowledge/Patterns/Schema-als-Vertrag-mit-generierten-Clients.md) | Eine versionierte Quelle für Typen, Validatoren und Clients verwenden und tatsächlich genutzte Verbraucher prüfen. | 6 |
| [Screenshot-als-Spezifikationsmedium](../80_Knowledge/Patterns/Screenshot-als-Spezifikationsmedium.md) | Sichtbaren Zustand präzise mitteilen; Interaktion und nicht sichtbare Zustände zusätzlich beschreiben. | 3, 12 |
| [Sicherer-Fallback-vor-menschlicher-Eskalation](../80_Knowledge/Patterns/Sicherer-Fallback-vor-menschlicher-Eskalation.md) | Vor Autonomie einen begrenzten Ausfallpfad bereitstellen, der nicht von sofortiger menschlicher Hilfe abhängt. | 10 |
| [Skill-aus-Demonstration-statt-Beschreibung](../80_Knowledge/Patterns/Skill-aus-Demonstration-statt-Beschreibung.md) | Tatsächliche gute und schlechte Durchläufe als Grundlage eines wiederverwendbaren Verfahrens verwenden. | 7 |
| [Skill-Call-Hierarchie](../80_Knowledge/Patterns/Skill-Call-Hierarchie.md) | Aufrufhierarchie und Rückgabe explizit machen; Namensnennung lädt einen Skill nicht in jedem Host. | 7 |
| [Skill-Qualitaet-durch-Trigger-und-Baseline-Evals](../80_Knowledge/Patterns/Skill-Qualitaet-durch-Trigger-und-Baseline-Evals.md) | Trigger, Nicht-Trigger, Verfahrensbefolgung und Nutzen gegen eine Baseline prüfen. | 7, 9 |
| [Skill-Schwellenwert-institutionelles-Wissen](../80_Knowledge/Patterns/Skill-Schwellenwert-institutionelles-Wissen.md) | Institutionelles Sonderwissen und wiederkehrende Fehler als Anlass nehmen, statt allgemein Bekanntes zu duplizieren. | 7 |
| [Spec-Grilling](../80_Knowledge/Patterns/Spec-Grilling.md) | Offene Entscheidungen und unbestätigte Annahmen vor ihrer Verfestigung untersuchen. | 3 |
| [Spec-Ordner-pro-Feature](../80_Knowledge/Patterns/Spec-Ordner-pro-Feature.md) | Bei langfristig gepflegtem Verhalten Spezifikation, Entscheidungen und Belege gemeinsam auffindbar halten. | 4 |
| [Suchintention-mit-Daten-vor-Webdesign-klaeren](../80_Knowledge/Patterns/Suchintention-mit-Daten-vor-Webdesign-klaeren.md) | Angebot und belegte Suchabsicht klären, bevor die Gestaltung beginnt. | 16 |
| [Task-basierte-Steuerung](../80_Knowledge/Patterns/Task-basierte-Steuerung.md) | Zuständigkeiten, Abhängigkeiten und Abschluss über Sessions hinweg nachverfolgbar machen. | 4, 8 |
| [TDD-als-Verifikationshebel](../80_Knowledge/Patterns/TDD-als-Verifikationshebel.md) | Den Fehler zuerst als scheiternden fachlichen Fall erfassen und anschließend seine Korrektur belegen. | 9 |
| [Testharness-als-staerkster-Hebel](../80_Knowledge/Patterns/Testharness-als-staerkster-Hebel.md) | Verlässliche Rückmeldung und realistische Umgebung als zentrale Voraussetzung guter Agentenarbeit schaffen. | 9 |
| [Trainingsdaten-Dichte-als-Stack-Kriterium](../80_Knowledge/Patterns/Trainingsdaten-Dichte-als-Stack-Kriterium.md) | Verbreitung und vorhandene Modellkenntnis als Stackkriterium neben fachlicher Eignung und Betrieb berücksichtigen. | 6, 11 |
| [UI-Grenzfaelle-mit-realistischen-Daten-pruefen](../80_Knowledge/Patterns/UI-Grenzfaelle-mit-realistischen-Daten-pruefen.md) | Extremdaten aus dem tatsächlichen Datenvertrag im gleichen Layout prüfen. | 12 |
| [Variantenvergleich-vor-Produktionsabnahme](../80_Knowledge/Patterns/Variantenvergleich-vor-Produktionsabnahme.md) | Echte Layout- und Interaktionsalternativen vergleichen und gewählte Umsetzung gesondert abnehmen. | 12 |
| [Verhaltens-Spec-als-Grenze-zwischen-Analyse-und-Nachbau](../80_Knowledge/Patterns/Verhaltens-Spec-als-Grenze-zwischen-Analyse-und-Nachbau.md) | Analysebefunde und Unbekanntes als begrenzten Vertrag an eine getrennte Implementierung übergeben. | 15 |
| [Videoanalyse-mit-Frames-und-Transkript](../80_Knowledge/Patterns/Videoanalyse-mit-Frames-und-Transkript.md) | Transkript und gezielte Frames verbinden und daraus abgeleitete Interpretation als solche kennzeichnen. | 13 |
| [Visuelle-Abnahme-mit-Live-Lokal-Vergleich](../80_Knowledge/Patterns/Visuelle-Abnahme-mit-Live-Lokal-Vergleich.md) | Tatsächliches Rendering mit vergleichbaren Zuständen und einem bewussten Soll vergleichen. | 12 |
| [Voice-Prompting-fuer-Kontextreichtum](../80_Knowledge/Patterns/Voice-Prompting-fuer-Kontextreichtum.md) | Implizite Hintergründe durch Sprache erschließen und kritische Transkriptstellen vor Aktionen prüfen. | 17 |
| [Wissenspflege-mit-Inbox-und-Review](../80_Knowledge/Patterns/Wissenspflege-mit-Inbox-und-Review.md) | Inbox, belegte Notizen, thematische Ordnung und regelmäßiges Review zusammenführen. | 14 |
| [Zustandslose-CI-Listener-mit-Ergebnisjournal](../80_Knowledge/Patterns/Zustandslose-CI-Listener-mit-Ergebnisjournal.md) | Schnelle Ereignisannahme von Historienaufbau trennen und Lag, Wiederholung und Wiederaufbau prüfen. | 18 |


## 24. Begriffsglossar aus dem AI Coding Dictionary

Die folgenden Kurzdefinitionen sind eigenständige deutsche Verdichtungen der vollständig gelesenen 71 Begriffseiten. Feste Produktgrenzen und Preisbeispiele wurden bewusst nicht verallgemeinert. Der [Wörterbuchindex](../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/00-index.md) ist ebenfalls gelesen.

| Begriff | Bedeutung für die Praxis |
|---|---|
| [AI](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/AI.md>) | Sammelbegriff für maschinelle Verfahren mit Fähigkeiten, die als intelligent bezeichnet werden; hier vor allem Sprachmodelle und Agentensysteme. |
| [Cache tokens](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Cache tokens.md>) | Eingabetokens, deren vorbereitete Repräsentation wiederverwendet wird; Abrechnung und Cachewirkung hängen vom Provider ab. |
| [Effort](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Effort.md>) | Konfigurierter Denk- beziehungsweise Arbeitsaufwand eines unterstützten Modells; zusätzliche Fähigkeit ist damit nicht garantiert. |
| [Harness](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Harness.md>) | Software um das Modell, die Werkzeuge, Kontext, Aufrufschleife und Sitzungszustand verwaltet. |
| [Inference](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Inference.md>) | Anwendung eines trainierten Modells zur Berechnung einer Ausgabe. |
| [Input tokens](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Input tokens.md>) | Tokenisierte Eingaben einschließlich der tatsächlich übermittelten Regeln, Historie und Toolinhalte. |
| [Model provider request](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Model provider request.md>) | Ein konkreter Aufruf des Modelldienstes mit Modellkonfiguration und Eingaben. |
| [Model provider](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Model provider.md>) | Anbieter beziehungsweise Laufzeit, die ein Modell über eine Schnittstelle verfügbar macht. |
| [Model](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Model.md>) | Trainiertes Parametersystem mit bestimmten Ein- und Ausgabefähigkeiten; allein noch keine vollständige Agentenumgebung. |
| [Next-token prediction](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Next-token prediction.md>) | Schrittweise Vorhersage des nächsten Tokens auf Basis der bisherigen Eingabe und Ausgabe. |
| [Non-determinism](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Non-determinism.md>) | Mögliche Abweichungen zwischen Läufen trotz ähnlicher oder identischer Ausgangsbedingungen. |
| [Output tokens](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Output tokens.md>) | Vom Modell erzeugte Tokens; sichtbarer Text und gegebenenfalls weitere abgerechnete Anteile sind zu unterscheiden. |
| [Parameters](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Parameters.md>) | Gelernte numerische Gewichte des Modells; ihre Zahl allein bestimmt seine praktische Qualität nicht. |
| [Prefix cache](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Prefix cache.md>) | Wiederverwendung der Verarbeitung eines passenden Eingabepräfixes innerhalb der unterstützten Cachebedingungen. |
| [Token](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Token.md>) | Verarbeitungseinheit eines Tokenizers; ein Token entspricht weder immer einem Wort noch einer festen Zeichenzahl. |
| [Training](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/01-the-model/Training.md>) | Verfahren zur Veränderung von Modellparametern anhand von Daten und Lernzielen. |
| [Agent](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/02-sessions-context-windows-turns/Agent.md>) | Konfiguriertes System, das Modellentscheidungen mit Werkzeugen und Rückmeldung in einem Arbeitsablauf verbindet. |
| [Context window](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/02-sessions-context-windows-turns/Context window.md>) | Technische Grenze des in einem Aufruf verarbeitbaren Kontexts; nutzbare Detailtreue kann schon vorher nachlassen. |
| [Context](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/02-sessions-context-windows-turns/Context.md>) | Dem Modell aktuell bereitgestellte Informationen und Anweisungen. |
| [Session](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/02-sessions-context-windows-turns/Session.md>) | Zusammenhängender Arbeitsverlauf mit vom Harness verwalteten Nachrichten und Zuständen. |
| [Stateful](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/02-sessions-context-windows-turns/Stateful.md>) | Ein System bewahrt Zustand zwischen einzelnen Operationen. |
| [Stateless](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/02-sessions-context-windows-turns/Stateless.md>) | Eine Operation setzt keinen verborgenen Sitzungszustand voraus; nötige Informationen werden ausdrücklich übergeben. |
| [System prompt](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/02-sessions-context-windows-turns/System prompt.md>) | Anweisungsebene des Hosts; ihre konkrete Hierarchie und Reichweite sind Systemeigenschaften. |
| [Turn](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/02-sessions-context-windows-turns/Turn.md>) | Ein Bearbeitungsabschnitt beziehungsweise Gesprächsschritt; genaue Grenzen unterscheiden sich zwischen Harnesses. |
| [Agent mode](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/03-tools-environment/Agent mode.md>) | Betriebsweise mit aktiver Ausführungs- und Toolschleife, soweit der Host sie so definiert. |
| [Environment](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/03-tools-environment/Environment.md>) | Tatsächlich erreichbare Dateien, Prozesse, Geräte, Daten und Dienste. |
| [Filesystem](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/03-tools-environment/Filesystem.md>) | Struktur zur Ablage und Adressierung von Dateien und Ordnern. |
| [MCP](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/03-tools-environment/MCP.md>) | Protokoll zur Anbindung von Werkzeugen und Kontextquellen; Verbindung ist keine pauschale Ausführungserlaubnis. |
| [Permission mode](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/03-tools-environment/Permission mode.md>) | Konfiguration für Freigabeentscheidungen im Harness; keine vollständige technische Isolation. |
| [Permission request](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/03-tools-environment/Permission request.md>) | Konkrete Bitte um Autorisierung einer Aktion mit erkennbarem Gegenstand. |
| [Sandbox](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/03-tools-environment/Sandbox.md>) | Technisch begrenzte Ausführungsumgebung; ihre wirksamen Grenzen müssen am Mechanismus geprüft werden. |
| [Tool call](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/03-tools-environment/Tool call.md>) | Strukturierte Anforderung, ein bestimmtes Werkzeug mit Argumenten auszuführen. |
| [Tool result](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/03-tools-environment/Tool result.md>) | Zurückgegebene Beobachtung einer Toolausführung; Erfolgsmeldung und fachliche Wirkung sind zu unterscheiden. |
| [Tool](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/03-tools-environment/Tool.md>) | Schnittstelle für Datenzugriff oder Aktionen außerhalb der reinen Modellausgabe. |
| [Attention budget](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/04-failure-modes/Attention budget.md>) | Heuristische Beschreibung begrenzter zuverlässiger Aufmerksamkeit innerhalb eines Arbeitskontexts. |
| [Attention degradation](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/04-failure-modes/Attention degradation.md>) | Nachlassende Nutzung relevanter Details bei wachsendem, verrauschtem oder widersprüchlichem Kontext. |
| [Attention relationship](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/04-failure-modes/Attention relationship.md>) | Zusammenhang zwischen Kontextumfang, Informationsauswahl und zuverlässiger Bearbeitung; keine universelle feste Formel. |
| [Contextual knowledge](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/04-failure-modes/Contextual knowledge.md>) | Wissen, das im aktuellen Kontext vorliegt und nachgeladen oder aktualisiert werden kann. |
| [Hallucination](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/04-failure-modes/Hallucination.md>) | Sachlich falsche oder unbelegte Modellaussage, die als plausibler Inhalt erscheint. |
| [Knowledge cutoff](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/04-failure-modes/Knowledge cutoff.md>) | Zeitliche Begrenzung bestimmter Trainingsdaten; keine Garantie vollständigen Wissens vor diesem Datum. |
| [Parametric knowledge](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/04-failure-modes/Parametric knowledge.md>) | In den gelernten Gewichten gespeicherte Fähigkeiten und Informationen. |
| [Smart zone](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/04-failure-modes/Smart zone.md>) | Didaktische Bezeichnung für einen brauchbar fokussierten Arbeitsbereich; keine allgemein messbare feste Tokenzone. |
| [Sycophancy](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/04-failure-modes/Sycophancy.md>) | Tendenz, erwarteten Nutzerpositionen zuzustimmen, statt angemessen eigenständig zu prüfen. |
| [Autocompact](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/05-handoffs/Autocompact.md>) | Vom Harness automatisch ausgelöste Verdichtung des Gesprächsverlaufs. |
| [Clearing](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/05-handoffs/Clearing.md>) | Verwerfen beziehungsweise Zurücksetzen eines bisherigen Arbeitskontexts nach den Regeln des Hosts. |
| [Compaction](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/05-handoffs/Compaction.md>) | Zusammenfassung zur Fortsetzung mit weniger Verlauf; kann relevante Details verlieren. |
| [Handoff artifact](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/05-handoffs/Handoff artifact.md>) | Dauerhaftes Übergabeobjekt mit Ziel, Entscheidungen, Nachweisen und offenen Schritten. |
| [Handoff](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/05-handoffs/Handoff.md>) | Übergabe einer Aufgabe an eine andere Sitzung, Person oder Instanz. |
| [Primary source](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/05-handoffs/Primary source.md>) | Ursprünglicher Bericht, Datensatz oder Implementierungsbeleg für die untersuchte Aussage. |
| [Secondary source](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/05-handoffs/Secondary source.md>) | Darstellung oder Einordnung einer anderen Quelle; kann helfen, ist aber keine unabhängige Wiederholung des Versuchs. |
| [Spec](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/05-handoffs/Spec.md>) | Beschreibung des gewünschten Verhaltens, seiner Grenzen und Akzeptanzbedingungen. |
| [Ticket](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/05-handoffs/Ticket.md>) | Begrenzte, nachverfolgbare Arbeitseinheit mit Zuständigkeit und Abschlusskriterium. |
| [AGENTS.md](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/06-memory-and-steering/AGENTS.md.md>) | Projektspezifischer Einstieg für Agenten mit Orientierung, lokalen Regeln und Verweisen. |
| [Context pointer](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/06-memory-and-steering/Context pointer.md>) | Gezielter Verweis, der relevante Information auffindbar macht, ohne sie vollständig vorab zu laden. |
| [Memory system](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/06-memory-and-steering/Memory system.md>) | Externe Speicherung und Wiederbereitstellung ausgewählter Erfahrungen oder Fakten über Sitzungen hinweg. |
| [Progressive disclosure](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/06-memory-and-steering/Progressive disclosure.md>) | Informationen und Verfahren erst beim passenden Bedarf in zusätzlicher Tiefe laden. |
| [Skill](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/06-memory-and-steering/Skill.md>) | Wiederverwendbares Aufgabenverfahren mit Triggern, Anweisungen, Referenzen und gegebenenfalls Helfern. |
| [Subagent](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/06-memory-and-steering/Subagent.md>) | Delegierte Agenteninstanz mit eigener Aufgabe und eigenem Kontext nach den Möglichkeiten des Hosts. |
| [AFK](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/07-patterns-of-work/AFK.md>) | Arbeit ohne ständig anwesenden Menschen; erfordert klaren Scope und einen brauchbaren Fehlerpfad. |
| [Automated check](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/07-patterns-of-work/Automated check.md>) | Mechanisch ausgeführte Prüfung einer ausdrücklich erfassten Eigenschaft. |
| [Automated review](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/07-patterns-of-work/Automated review.md>) | Automatische Beurteilung anhand einer Rubrik oder eines Modells; Fehlalarme und Lücken bleiben möglich. |
| [AX](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/07-patterns-of-work/AX.md>) | Agent Experience: Wie verständlich und verlässlich eine Umgebung für Agenten nutzbar ist. |
| [Dark factory](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/07-patterns-of-work/Dark factory.md>) | Vision weitgehend automatisierter Lieferung; die Bezeichnung selbst belegt keine verlässliche Autonomie. |
| [Design concept](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/07-patterns-of-work/Design concept.md>) | Ausgewählte gestalterische Richtung, die vor der Produktionsumsetzung verglichen und beurteilt werden kann. |
| [DX](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/07-patterns-of-work/DX.md>) | Developer Experience: Qualität der Arbeitsumgebung aus Sicht der entwickelnden Menschen. |
| [Grilling](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/07-patterns-of-work/Grilling.md>) | Systematisches Hinterfragen offener Entscheidungen und Annahmen vor teurer Umsetzung. |
| [Human review](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/07-patterns-of-work/Human review.md>) | Eigenständiges menschliches Urteil über Ergebnis, Belege und verbleibende Risiken. |
| [Human-in-the-loop](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/07-patterns-of-work/Human-in-the-loop.md>) | Ein Mensch wirkt an definierten Entscheidungen im Ablauf mit; bloße Anwesenheit garantiert keine wirksame Aufsicht. |
| [Prototyping](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/07-patterns-of-work/Prototyping.md>) | Begrenzter Versuch zur Klärung einer konkreten Frage vor weitergehender Investition. |
| [Software factory](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/07-patterns-of-work/Software factory.md>) | Organisierter Ablauf zur wiederholbaren Herstellung, Prüfung und Lieferung von Software. |
| [Vibe coding](<../00_Inbox/Quellen/URL/aihero-ai-coding-dictionary/07-patterns-of-work/Vibe coding.md>) | Uneinheitlicher Begriff für stark delegierte Softwareerzeugung; tatsächliches Verständnis und Prüfniveau müssen konkret beschrieben werden. |


## 25. Umfang, Abdeckungsnachweis und Grenzen dieser Synthese

### Was tatsächlich gelesen wurde

Die Auswahl wurde zu Beginn als Dateimanifest festgehalten. Rohquellen und vorhandene Source-Notizen wurden vollständig im Text gelesen und pro Lektüreeinheit ausgewertet. Die ergänzenden Patterns, das Wörterbuch und der externe Index wurden ebenfalls vollständig gelesen. Für die Repository-Analyse wurden die tatsächlichen READMEs beziehungsweise dokumentierte Einstiegsäquivalente und ausgewählte methodentragende Dateien vollständig untersucht.

| Bestand | Umfang | Einordnung |
|---|---|---|
| Rohquellen direkt in den fünf Typordnern | 509 Markdown-Dateien | X 273, TikTok 79, YouTube 63, URL 93, PDF 1 |
| Verschachteltes AI Coding Dictionary | 72 Markdown-Dateien | Ein Index und 71 Begriffseiten; eine Sammlung, keine 72 unabhängigen Veröffentlichungen |
| Source-Notizen | 516 Markdown-Dateien | Redaktionelle Aufbereitungen, teilweise mit anderer Benennung oder derselben Originalquelle |
| Quellenlektüre insgesamt | 1.097 inhaltliche Markdown-Dateien | 1.025 Dateien in 604 Lektüreeinheiten plus 72 Wörterbuchdateien |
| Verwaltungsdateien des Quellenarchivs | 2 Markdown-Dateien | README und historischer Verarbeitungsplan; zusätzlich gelesen, keine inhaltlichen Quellen |
| Patterns | 93 Markdown-Dateien | Vollständig gelesen und in Kapitel 23 erschlossen |
| Externer Index | 74 Detaileinträge | Die Übersicht nennt noch 72; diese Synthese folgt sämtlichen 74 Detailüberschriften |
| Repository-Vertiefung | 74 Einträge, 295 unterschiedliche Dateien | README/Einstieg und ausdrücklich verlinkte Vertiefungen; 4.713.219 Bytes gelesener Dateibestand |

Die 604 Lektüreeinheiten entstehen durch Zuordnung anhand der Dateistämme. Sie umfassen 421 direkte Rohtext-/Notiz-Paare, 88 einzelne Rohtexte und 95 einzelne Notizen. Andere Slugs und mehrfache Aufbereitung derselben URL bleiben darin getrennt. Die Zahl bezeichnet deshalb ausdrücklich weder 604 Originalpublikationen noch 604 unabhängige Belege. Gleiche angegebene Herkunft wird im Register verbunden; darüber hinaus können verschiedene Beiträge denselben Bericht wiedergeben.

Die Verwaltung zählt insgesamt 583 Markdown-Dateien unter dem Quellenordner: 581 inhaltliche Archivdateien und zwei Verwaltungsdateien. Der historische Verarbeitungsplan mit Stand August enthält ältere Bestands- und Fehlerzahlen. Sie wurden als Verlauf gelesen und nicht als aktueller Status übernommen.

### Wie die Lektüre abgesichert wurde

Die drei Quellenpakete enthalten genau 200, 202 und 202 Einheiten. Für jede Einheit liegen eine konkrete deutsche Erkenntnis, Grenzen, vollständige Pfadzuordnung und SHA-256-Hashes vor. Die zentralen Volltextlektüren wurden in aufeinanderfolgenden Zeichenbereichen protokolliert. Die Intervallprüfung zeigt keine Lücke für Index, Patterns und Wörterbuch. Die Hashprüfung zeigt keine veränderten Eingänge gegenüber dem jeweiligen Lektürestand.

Alle 74 vorgesehenen Repo-Namen sind genau einmal im Repository-Register vertreten. Die dort verlinkten Dateien und ihre Hashes wurden gegen die Ergebnisse geprüft. Soweit ein eigener Git-Checkout vorliegt, ist dessen Revision angegeben. Das AI-LLM-Wiki liegt abweichend unter external_knowledge. Open Design ist eine lokale Dateikopie ohne eigenes Git-Metadatenverzeichnis; ein im Elternverzeichnis ermitteltes HEAD wäre dort irreführend und wird nicht als Repo-Revision ausgegeben.

Das Wörterbuch wurde arbeitsteilig gegen seinen Originalstand abgeglichen: Alle 71 normalisierten Begriffstexte stimmen mit den gelesenen Archivseiten überein und sind in der generierten Repo-README enthalten. Zusätzlicher Rahmen und Generator wurden separat betrachtet. Die Definitionen dieses Dokuments sind eigene deutsche Verdichtungen, keine Übernahme der vollständigen Originaltexte.

Hashes und Lesespannen sind Integritäts- und Abdeckungsbelege. Sie beweisen für sich kein richtiges Verständnis. Dafür dienen die fachliche Synthese, die ausformulierten Einzelbefunde, erhaltene Widersprüche und die Rückwege zu den konkreten Texten. Die Arbeitsprotokolle liegen lokal im ignorierten Analyseordner; das eigenständig lesbare Ergebnis ist dieses eine Markdown-Dokument.

### Was diese Abdeckung nicht behauptet

Die Repository-Lektüre ist keine vollständige Prüfung jeder Code-, Dokument-, Roharchiv- oder generierten Datei in allen Repositories. Große Sammlungen wurden über alle Einstiege und gezielt gewählte zentrale Verfahren erschlossen. Besonders beim AI-LLM-Wiki wurde eine themenbreite Auswahl von 30 Dateien gelesen; sein gesamter umfangreicher Roh- und PDF-Bestand ist nicht enthalten. Die Repo-Profile nennen die tatsächlich gelesenen Pfade, damit diese Grenze überprüfbar bleibt.

Die Quellenlektüre umfasst die vollständig archivierten Markdown-Texte. Sie ist keine vollständige erneute Sichtung aller Videos, Audios, Bilder und PDF-Seiten und kein neuer Abruf aller verlinkten Originale. Bestehende Berichte über frühere Mediensichtung bleiben abgeleitete Belege. Automatische Untertitel und Übersetzungen können Fachwörter, Namen und Zahlen verfälschen. Fehlende Enden, ausgelassene Codeblöcke oder nicht erreichbare Inhalte werden durch diese Synthese nicht nachträglich vollständig.

README-Aussagen und statisch gelesener Code wurden nicht durch Installation und eigene Laufversuche sämtlicher Werkzeuge bestätigt. Kein externer Installationsbefehl wurde für diese Analyse ausgeführt. Modellpreise, Ranglisten, Limits und Produktfunktionen sind historische Archivangaben beziehungsweise Aussagen zum gelesenen Stand. Rechtliche und wirtschaftliche Prognosen werden nicht als hier bestätigte Tatsachen übernommen.

### Ausgeführte Abschlussprüfungen

- Eindeutigkeit und Vollständigkeit aller 604 Quellen-IDs sowie Zuordnung sämtlicher 1.025 Quelldateien.
- SHA-256-Abgleich der Quellen, Patterns, Wörterbuchdateien, des Index und aller gelesenen Repository-Dateien.
- Lückenprüfung der zentralen Lesespannen und Abgleich sämtlicher 74 vorgesehenen Repository-Namen.
- Prüfung der lokalen Links, Registereinträge und grundlegenden Markdown-Struktur dieses Dokuments.
- Knowledge-Validator vor und nach der Arbeit: identische Ausgabe mit 53 bereits vorhandenen Fehlern; keine neu verursachten Fehler.
- Vergleich des bereits vorhandenen Git-Diffs: unverändert; die einzige neue Ergebnisdatei ist dieser Bericht.

Der allgemeine Wissenskatalog wurde zusätzlich mit dem eigenen Index-Script neu aufgebaut. Ein Katalogeintrag bedeutet weiterhin nur Auffindbarkeit, keine Lektüre. Für die Abdeckung dieses Berichts ist das gesonderte Aufgabenmanifest maßgeblich. Quellenstatus, bestehende Source-Notizen, Patterns und externer Index wurden nicht geändert. Es wurden keine Commits, Pushes, Installationen oder Deployments vorgenommen.
