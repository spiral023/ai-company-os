# Eval: Wissensbasis für die Software Factory

**Stand:** 2026-10-25 · **Status:** vorbereiteter fachlicher Abnahmekatalog, noch kein gemessener Vergleichslauf.

Ziel ist, die Nutzung des gesamten Wissenszusammenhangs zu prüfen. Ein schneller Suchtreffer genügt nicht. Für den Vergleich dieselbe Frage und denselben Bestandsstand einmal mit bisherigem Vorgehen und einmal mit dem ausgebauten Wissenszugriff beantworten. Bewertende Instanz erhält die Antworten in zufälliger Reihenfolge und prüft die Originalbelege der entscheidenden Aussagen.

## Fragen und erwartete Eigenschaften

| ID | Aufgabe | Erwartete Eigenschaften der Antwort |
|---|---|---|
| W01 | Entwirf aus unserem Bestand einen Feature-Ablauf für eine erste Software Factory. | Verbindet Sprogis/ZazenCodes, eigene Regeln und mindestens eine Repo-Methode; Spec, Build, unabhängige Prüfbedingungen und Freigabe unterscheiden; Demo nicht als Wirksamkeitsnachweis ausgeben |
| W02 | Welche Kombination aus Fähigkeiten verschiedener Repos wäre für einen kleinen Factory-Pilot sinnvoll? | Konkrete Pfade/Versionen, Inputs/Outputs und Voraussetzungen; begrenzte Auswahl statt Vollinstallation mehrerer Frameworks |
| W03 | Welche Methoden widersprechen sich, wenn wir pstack, GSD und Matt-Pocock-Skills gemeinsam verwenden wollen? | Tatsächliche Anweisungen nachlesen; Unterschiede zwischen Workflow-Pflicht, kleinen Methoden und Runtime-Annahmen erklären; Konflikte nicht durch bloßes Aneinanderhängen lösen |
| W04 | Wie verhindern wir, dass fünf Erwähnungen derselben Herstellerankündigung als fünf unabhängige Belege zählen? | Original und Ableitungen zu einer Quellenfamilie verbinden; Zahl der Erwähnungen von unabhängiger Evidenz unterscheiden |
| W05 | Was wissen wir über den Nutzen getrennter Reviewer, und was wissen wir nicht? | Primärbeleg/Erfahrungsbericht/Implementierung unterscheiden; unabhängiger Kontext allein belegt keine unabhängige Abnahme |
| W06 | Kann ein gefundener externer Skill sofort vom Builder verwendet werden? | Auffindbarkeit, Registry-Trust, Import-Review und tatsächliche Aktivierung unterscheiden; bestehende Regeln anwenden |
| W07 | Eine README bleibt gleich, aber ein zugehöriger Prompt ändert sich. Welche Wissensobjekte brauchen Prüfung? | Inhalts-Hash und Commit/Dirty-Stand verwenden; abhängige Fähigkeitskarten/Synthesen/Evals benennen; Grenzen aktueller Implementierung offen nennen |
| W08 | Welche Risiken bleiben bei „alle Tests grün“ als autonomem Abschlusskriterium? | Testharness, Reward Hacking, Spec-Erfüllung, Schutz der Abnahme und Fehlerpfad verbinden |
| W09 | Welche Quellen oder Repos haben bisher keine passende Rolle in unserer Factory, obwohl sie vorhanden sind? | Vom Inventar ausgehen; begründeten Nicht-Einsatz und Lücken dokumentieren, nicht nur bekannte Favoriten durchsuchen |
| W10 | Welche Erkenntnisse fehlen, um eine konkrete Laufzeit und einen Orchestrator auszuwählen? | Aufgabenklasse, Laufartefakte, Runner, Kosten, Wiederanlauf und Integrationen nennen; keine veralteten Produktfakten als aktuell ausgeben |
| W11 | Hat die Gesamtanalyse tatsächlich alle vereinbarten Inhalte abgedeckt? | Snapshot, Passagenstatus, Repo-Fehler und Auslassungen nachweisen; Textindex nicht mit Code-/Videoanalyse gleichsetzen |
| W12 | Leite eine neue prüfbare Factory-Verbesserung aus mindestens drei unterschiedlichen Themen ab. | Belegkette über Themen/Repos hinweg, eigener Schluss als Hypothese markiert, kleinster Versuch, messbares Erfolgskriterium und Gegenargument |

## Bewertung

Je Frage 0–2 Punkte in vier Dimensionen: fachliche Aussage, überprüfbare Herkunft, Zusammenhänge/Gegenargumente und brauchbare Konsequenz. 0 = fehlt/falsch, 1 = teilweise, 2 = nachvollziehbar erfüllt. Maximal 8 Punkte pro Frage. Reale Quellen oder eindeutige „nicht belegt“-Aussagen sind besser als erfundene Vollständigkeit.

Pilotziel als Vorschlag: keine erfundenen Belege, keine unzulässige Skill-Aktivierung, keine vorgetäuschte Vollanalyse und mindestens 6/8 Punkte bei 10 der 12 Fragen. Die Grenze ist ein vorgeschlagenes Abnahmekriterium, keine empirisch kalibrierte Zuverlässigkeitsgarantie. Laufzeit, Anzahl nachgeladener Dokumente, Token-/Modellkosten und notwendige menschliche Korrekturen separat erfassen.

Eine Verbesserung muss an den Antworten sichtbar werden. Größerer Index, mehr Graphkanten oder längere Kontextpakete zählen allein nicht als Erfolg.
