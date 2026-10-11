---
url: https://www.youtube.com/watch?v=k2p6WprtzFI
autor: "Julian Ivanov | KI-Automatisierung"
datum: 2026-06-18
erfasst: 2026-10-11
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-06-18-julian-ivanov-ki-automat-bau-dir-dein-ki-betriebssystem-mit-claude-code-k.md
thema: Arbeitsweisen
zeitkritisch: ja
---

# Persönliches KI-Betriebssystem: Wissen, Tools, Skills und Routinen getrennt aufbauen

Julian Ivanov erweitert am 18. Juni 2026 seinen Wissensvault um Tool-Zugriffe, wiederverwendbare Abläufe und zeitgesteuerte Ausführung. Sein Begriff KI-Betriebssystem bezeichnet eine Arbeitsumgebung aus Dateien und Agenten, keine neue Betriebssystemtechnik. Die Demos zeigen konkrete Abläufe; versprochene Produktivitätsgewinne und Dauerverfügbarkeit sind nicht unabhängig gemessen.

## Vier Bausteine mit unterschiedlichen Aufgaben

**Wissen** enthält Projekte, Schreibstil, Branding, Kundenprofil und Entscheidungen als verknüpfte Markdown-Dateien. Eine knappe `CLAUDE.md` erklärt Ablage und Regeln. Der Agent bekommt damit kontextabhängige Referenzen für seine Arbeit. Dieser Baustein führt das frühere [[2026-03-29-julian-ivanov-ki-automat-obsidian-claude-code-so-baust-du-dein-zweites-ge]] fort.

**Verbindungen** ermöglichen den Zugriff auf andere Programme über MCP, CLI oder API. Der Autor zeigt die Vorbereitung eines Workshops: Kontextdateien werden gelesen, verfügbare Google-Workspace-Werkzeuge geprüft und Entwürfe für Agenda, Vergleichstabelle und Präsentation in den Zielprogrammen abgelegt. Die Demo belegt die Erstellung von Artefakten; sie ist keine allgemeine Qualitätsprüfung der Inhalte oder recherchierten Preise.

**Skills** beschreiben wiederkehrende Prozesse und können auf Fachkontext, Tools und Skripte verweisen. Eine Anleitung zum Diagrammaufbau erfüllt eine andere Aufgabe als Branding-Daten oder die Tool-Verbindung. Eigene Skills entstehen laut Autor am besten nach einer gemeinsam durchgeführten Aufgabe: Den erfolgreichen Ablauf anschließend als Anleitung festhalten. Der gezeigte Skill Creator wird für Feedback und Evaluation herangezogen; im Video wird daraus keine vergleichende Wirkungsmessung.

**Routinen** legen fest, wann und wo ein Ablauf startet. Sie rufen einen Skill auf, statt seine Prozessbeschreibung für jeden Zeitplan erneut zu schreiben. Diese Aufteilung ergänzt [[Erweiterungs-Ebenen-Zuordnung]] um die Auslösung wiederkehrender Arbeit.

## Lokale und entfernte Ausführung bewusst wählen

Bei einem lokalen Beispiel landet die Aufzeichnung eines Community-Calls zunächst im Downloadordner. Eine Routine überführt die Datei in die Arbeitsablage und startet den Transkript-Skill. Dieser nutzt laut Autor ein lokales Whisper-Modell und ein lokales Modell für eine Zusammenfassung mit Zeitmarken; das Ergebnis wird im Wissensordner abgelegt. Die anschließende Veröffentlichung nimmt der Autor selbst vor.

Ein weiteres Beispiel ist ein wöchentlicher News-Entwurf. Die entfernte Routine arbeitet mit einem auf GitHub verfügbaren Repository und den dafür eingerichteten Verbindungen. Der Autor unterscheidet ausdrücklich: Der lokale Ablauf benötigt seinen eingeschalteten Rechner, die entfernte Ausführung findet auf Anbieterinfrastruktur statt. Daraus lässt sich als eigene Arbeitsregel ableiten: Ausführungsort nach benötigten Dateien, Modellen und Verbindungen wählen, nicht nur nach dem Kalender.

## Gerätewechsel und Serverbetrieb ergänzen den Prozess

Der Autor verteilt den Arbeitsordner über ein privates GitHub-Repository auf Rechner, Laptop und Server. Ein SSH-Zugang verbindet seine Bedienoberfläche mit der Agent-Instanz auf dem Server. Remote Control dient als zusätzliche Bedienmöglichkeit vom Handy. Ein Dashboard ist eine optionale Oberfläche, die bestehende Skills und Agent-Sessions startet.

Für die Synchronisation steht in seiner `CLAUDE.md`, vor der Arbeit zu pullen und danach zu pushen. Zusätzlich demonstriert er das Obsidian-Git-Plugin mit periodischen Commit-, Pull- und Push-Vorgängen. Diese Schritte beschreiben einen damaligen Betriebsansatz. Sie garantieren keine konfliktfreie Synchronisation: Die [offizielle Git-Dokumentation](https://git-scm.com/docs/git-pull) behandelt ausdrücklich unterschiedliche Historien sowie Konflikte beim Zusammenführen. Eine lokale Arbeitskopie kann deshalb trotz Zeitplan vom gewünschten Stand abweichen.

Die Behauptung, eine durch `tmux` gehaltene Agent-Session überlebe Server-Neustarts, geht ebenfalls über den beschriebenen Mechanismus hinaus. Laut [offizieller tmux-Einführung](https://github.com/tmux/tmux/wiki/Getting-Started) läuft der Zustand in einem Serverprozess; Detach und Reattach schützen laufende Programme bei Verbindungsabbrüchen. Daraus folgt keine Wiederaufnahme derselben Prozesse nach einem Betriebssystem-Neustart.

## Einordnung

Eigene Bewertung: Die stärkste Ergänzung gegenüber dem März-Vault ist die klare Trennung von Information, Vorgehen, Tool-Zugriff und Auslösung. Sie erlaubt, denselben Wissensbestand und Skill für manuelle Arbeit oder eine Routine zu verwenden. Die vorhandene [[2026-03-21-sourfraser-claude-obsidian-ai-employee]] beschreibt bereits einen Memory Loop; hier wird dieser um Ausführungsorte und konkrete Artefaktablage erweitert. Tarif-, Plugin-, Desktop- und Serverangaben bleiben der Stand vom Juni 2026, während die geprüften Git- und tmux-Grenzen gesonderte heutige Einordnung sind. Lokale Modellschritte und ein privates Repository belegen für sich keine vollständig lokale Datenverarbeitung oder geprüfte Rechtevergabe. Dauerbetrieb benötigt zusätzlich beobachtbare Ergebnisse und Fehlerbehandlung; ein Zeitplan ist noch kein Nachweis erfolgreicher Ausführung.

## Kernaussagen

- Wissen, Skills, Tool-Verbindungen und Routinen getrennt pflegen; siehe [[Erweiterungs-Ebenen-Zuordnung]].
- Einen gelungenen Ablauf zuerst gemeinsam durchführen und daraus einen Skill ableiten; siehe [[Skill-aus-Demonstration-statt-Beschreibung]].
- Den Ausführungsort anhand der benötigten Ressourcen bestimmen und erzeugte Artefakte prüfen.
- Git-Synchronisation, erreichbare Session und Wiederanlauf nach Neustart sind verschiedene Betriebsaufgaben.

## Verbindungen

- [[2026-03-29-julian-ivanov-ki-automat-obsidian-claude-code-so-baust-du-dein-zweites-ge]] — Inbox, Tageslogs und Reviews als Wissenspflege.
- [[2026-03-21-sourfraser-claude-obsidian-ai-employee]] — bereits bekannter persistenter Kontext und Memory Loop.
- [[Erweiterungs-Ebenen-Zuordnung]] — Verantwortlichkeiten der Bausteine begrenzen.
- [[Skill-aus-Demonstration-statt-Beschreibung]] — Arbeitsabläufe aus einem gezeigten Ergebnis ableiten.
- [[Wissenspflege-mit-Inbox-und-Review]]
