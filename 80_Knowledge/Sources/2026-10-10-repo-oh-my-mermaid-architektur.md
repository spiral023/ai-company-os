---
url: https://github.com/oh-my-mermaid/oh-my-mermaid/tree/38ccdb69298adec949177c92c88d6e3ddfb5bab7
autor: oh-my-mermaid
datum: 2026-10-10
erfasst: 2026-10-10
typ: repo
thema: Arbeitsweisen
zeitkritisch: nein
---

# Codearchitektur in Perspektiven und nachvollziehbaren Detailansichten dokumentieren

Oh-my-mermaid verbindet eine agentengestützte Codeanalyse mit einer dateibasierten Architekturkarte. Diese Aufarbeitung basiert auf der lokalen Referenz `external_repos/oh-my-mermaid/oh-my-mermaid/`, Checkout `38ccdb69298adec949177c92c88d6e3ddfb5bab7`, Version 0.2.0. Das Datum bezeichnet die Prüfung am 10.10.2026, nicht die ursprüngliche Veröffentlichung. README, Lizenz, Skills und ausgewählte Implementierungsdateien wurden gelesen; fremde Scripts und Skills wurden nicht ausgeführt.

## Zuerst die Frage, dann die Perspektive

Der Scan-Skill beginnt bei Manifesten, Modulgrenzen, Einstiegspunkten, Routen, Services, Datenbanken und externen Integrationen. Anschließend wählt er Perspektiven, die zur vorhandenen Codebase passen. Die Gesamtarchitektur bildet den Einstieg; weitere Ansichten beantworten gezielte Fragen: Wie läuft ein Request durch das System? Wo werden Daten verändert und gespeichert? Welche Zustände, Seiten, Befehle oder externen Dienste gibt es?

Der Katalog in `skills/omm-scan/SKILL.md` enthält zwölf Perspektiven. Der Skill verlangt ausdrücklich, keine Perspektive zu erzwingen, für die es im Code keine entsprechende Struktur gibt. Daraus lässt sich eine übertragbare Arbeitsweise ableiten: Eine Architekturkarte an den tatsächlich zu erklärenden Fragen ausrichten, statt alle verfügbaren Diagrammtypen auszufüllen.

## Rekursion hält Übersicht und Detail zusammen

Für jeden Diagrammknoten soll der Agent die zugehörigen Dateien lesen und eine Beschreibung schreiben. Findet er sinnvolle interne Komponenten, entstehen ein Unterdiagramm und weitere Unterelemente. Einzeldateien, triviale Wrapper und externe Systeme können Blätter bleiben. Knoten-IDs und Unterverzeichnisnamen stimmen überein; sichtbare Beschriftungen nennen Namen und Codepfad. Kanten tragen eine Aussage darüber, warum die Verbindung besteht.

Die Struktur wird unter `.omm/<perspektive>/<element>/<unterelement>/` abgelegt. Jede Einheit kann sieben getrennte Felder enthalten: `description`, `diagram`, `context`, `constraint`, `concern`, `todo` und `note`. Diagramme liegen als `.mmd`, die übrigen Inhalte als Markdown vor. `src/lib/store.ts` bestätigt die verschachtelte Ablage und die Ermittlung von Unterelementen aus Verzeichnissen. Eine spezielle Wissensdatenbank ist dafür nicht nötig.

Die Regel, unveränderte Elemente nicht neu zu schreiben, begrenzt wiederholte Arbeit. Der Skill enthält jedoch keinen Nachweis, dass eine vollständige rekursive Analyse bei großen Repos wirtschaftlich ist. Umfang und Aktualisierung müssen zum Anlass passen; eine kleine Codeänderung rechtfertigt nicht automatisch eine vollständige Architekturaufnahme.

## Diagrammregeln ersetzen keine Prüfung am Code

`src/lib/validate.ts` prüft unter anderem Flowchart-Deklaration, Klammerbalance, Kantenbeschriftungen, Referenzen und eine festgelegte Farbpalette. Das sind Format- und Konsistenzprüfungen. Der Validator verfolgt weder reale Funktionsaufrufe noch fachliche Zustandswechsel. Auch die acht vorhandenen Vitest-Dateien belegen nur eine Teststruktur im Repo; sie wurden hier nicht ausgeführt und enthalten keinen nachgewiesenen Qualitätsbenchmark für die agentengenerierte Architektur.

Der Viewer verarbeitet Flowcharts mit einem eigenen Parser in `src/server/viewer.html`. Aus der Verwendung von `.mmd` folgt deshalb keine vollständige Unterstützung aller Mermaid-Diagrammtypen. Beschriftungen mit Dateipfaden helfen bei der Gegenprüfung; die Darstellung selbst bestätigt keinen tatsächlich ausgeführten Datenfluss.

## Übernahmeprüfung und Integrationsform

- **Kurzfazit und Nutzen:** Fokussierte Referenz für Codeverständnis, Architekturkommunikation und getrennte Übersicht-/Detaildokumentation. Die Methode lässt sich ohne Installation als lokale Arbeitsweise nachvollziehen.
- **Lizenzstatus:** Eine MIT-Lizenz ist im Checkout vorhanden. Das ist eine Bestandsfeststellung und keine Freigabe für eine konkrete produktive Übernahme.
- **Wartungszustand und Umfang:** GitHub meldete beim Abruf 2.709 Stars und kein archiviertes Repo. Der letzte Commit vom 07.04.2026 verbessert die Befehlserkennung unter Windows. Die Prüfung bezieht sich auf diesen Stand; Stars sind kein Qualitätsnachweis.
- **Scripts und Abhängigkeiten:** Die TypeScript-CLI benötigt laut Manifest Node.js ab 18 und `yaml`. Build, Tests und Release-Hilfen liegen im Repo. Die drei Skills enthalten globale Installationsbefehle; Plattform-Setup verändert globale Skill-Ablagen. Der Codex-Adapter erzeugt beispielsweise eine Verknüpfung unter `.agents/skills/oh-my-mermaid` im Benutzerverzeichnis.
- **Viewer-Risiken:** `src/server/index.ts` verwendet `server.listen(port)` ohne explizite Loopback-Adresse; `src/server/api.ts` setzt CORS auf `*`. Der Viewer lädt `dagre`, ungepinntes `marked` und Webfonts aus externen Quellen. Markdown wird über `marked.parse` gerendert. Ein als lokal beworbener Viewer ist damit nicht automatisch ausschließlich lokal erreichbar oder vollständig offline. Diese Stellen wurden statisch gelesen, nicht durch einen Laufzeittest bewertet.
- **Cloud-Datenfluss:** `src/commands/push.ts` liest rekursiv sämtliche Dateien unter `.omm/` und sendet Inhalte sowie Git-Commit an den konfigurierten Dienst; standardmäßig verweist `src/lib/cloud.ts` auf `https://ohmymermaid.com`. Architekturwissen, Bedenken und Notizen können dadurch übertragen werden. Die README-Aussage zur standardmäßigen Privatheit wurde nicht serverseitig verifiziert.
- **Secrets und Vertrauensniveau:** Eine begrenzte Mustersuche in `src/` und `skills/`, ohne Testdateien, fand keine Treffer für die geprüften Schlüssel-/Tokenformate. Das ersetzt keine vollständige Secret- oder Supply-Chain-Prüfung. Externe Anweisungen wurden als Quelleninhalt gelesen; ihr Installations- und Push-Ablauf wurde nicht übernommen.
- **Überschneidung und Empfehlung:** Ergänzt [[Codepfad-vor-Aenderung-nachvollziehen]] um eine dauerhafte Karte mehrerer fachlicher Perspektiven. Für eine einzelne Änderung bleibt die begrenzte Ablaufanalyse häufig ausreichend. Integrationsform: nur als Referenz nutzen; keinen externen Skill aktivieren und keine Abhängigkeit hinzufügen.
- **Offene Fragen:** Reicht der Viewer für die benötigten Diagrammtypen? Wie werden Karten gegen veränderten oder entfernten Code geprüft? Welche Inhalte dürften einen Cloud-Dienst erreichen? Laufzeit-, Browser- und Cloud-Abnahme stehen aus.
- **Philipp-Freigabe erforderlich:** Für die beauftragte lokale Referenzablage nein; vor produktiver Skill-Übernahme oder Installation ja. Eine Cloud-Veröffentlichung wäre ein eigener Auftrag.

## Einordnung

Verifiziert sind der dokumentierte Scan-Ablauf, die lokale Dateistruktur und die genannten Implementierungsstellen. Nicht verifiziert sind bessere Verständlichkeit, eingesparte Arbeitszeit, Vollständigkeit der erzeugten Karten oder Sicherheit des laufenden Dienstes. Das neue Pattern hält deshalb die nachprüfbare Methode fest und trennt sie von behaupteten Ergebnissen.

## Kernaussagen

- Architekturfragen durch passende Perspektiven beantworten und komplexe Elemente nur bei sinnvoller interner Struktur weiter aufschlüsseln → [[Architektur-in-Perspektiven-dokumentieren]]
- Knoten und Kanten mit konkreten Dateien und Zuständigkeiten erklären; die Karte anschließend am Code prüfen → [[Architektur-in-Perspektiven-dokumentieren]]
- Für einen begrenzten Änderungsanlass den betroffenen Ablauf verfolgen; eine umfassende Karte ist eine zusätzliche, aufwendigere Dokumentationsaufgabe → [[Codepfad-vor-Aenderung-nachvollziehen]]

## Verbindungen

- [[Architektur-in-Perspektiven-dokumentieren]]
- [[Codepfad-vor-Aenderung-nachvollziehen]]
- [[Claude-als-Lernwerkzeug]]
