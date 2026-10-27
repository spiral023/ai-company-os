# Methodenbelege für fünf Kandidaten des semantischen Factory-Piloten

**Stand:** 2026-10-26. Primärprüfung direkt an Original-Skills und Playbooks der lokalen Checkouts. Keine Berichte als Belegersatz verwendet. Die Kandidaten unten sind vorgeschlagene fachliche Verträge für den Piloten; sie sind keine aktivierten Skills und kein Nachweis praktischer Wirkung.

## Quellenstand und Herkunftsfamilien

| Familie | Direkt geprüfter lokaler Stand | Status und Lizenzdatei |
|---|---|---|
| `mattpocock/skills` | HEAD `5beb35b040e3de97e54fa9e386d7e42d15c295c2` | `git status --short` leer; `external_repos/mattpocock/skills/LICENSE`, Zeilen 1–3: MIT, Copyright Matt Pocock |
| `cursor/plugins:pstack` | HEAD `99b609a72323b70204eab407c622f436e858e112` | `git status --short` leer; `external_repos/cursor/plugins/pstack/LICENSE`, Zeilen 1–3: MIT, Copyright Lauren Tan |
| Itamar Friedman, Veröffentlichung `2113255396299128887` | Originaltext lokal unter `00_Inbox/Quellen/X/2026-10-22-itamar_mar-2113255396299128887.md`; URL im Frontmatter: `https://x.com/itamar_mar/status/2113255396299128887` | Lokal geändert, deshalb nicht durch Root-HEAD `2b77025c5417ee766a9d933b8bcc9c042623b936` allein identifiziert. SHA-256 des gelesenen Textstands: `bba8ec1c8bedd14453496f7ee796f27a248f79aa03c848c1edfb3615f7edf957`. Keine Lizenz zur Übernahme ermittelt. |

Lizenzangaben geben die jeweilige Datei wieder; Drittbestandteile und konkrete Nutzung wurden nicht geprüft. Fremde Anweisungen wurden ausschließlich gelesen. Kein Pull, keine Installation, Aktivierung, Kopie eines Skills oder Ausführung eines Fremdskripts.

Mehrere Aussagen aus demselben Skill oder Repo sind keine unabhängigen Bestätigungen. Insbesondere stammen Spec-Review und Standards-Review aus demselben `code-review`-Skill. Itamars Rohquelle und die zugehörige redaktionelle Source-Notiz gehören zu einer Veröffentlichung und werden als **eine** Herkunftsfamilie gezählt. ZazenCodes und Sprogis werden für die fünf Verträge nicht benötigt und liefern hier keine zusätzlichen Evidenzstimmen.

## 1. Kandidat: Spec-Klärung

**Ziel:** Unentschiedene Anforderungen und voneinander abhängige Produktentscheidungen sichtbar machen, bevor sie unbemerkt in die Umsetzung eingehen.

**Notwendige Eingaben:** Nutzerziel, vorhandene Anforderungen und Entscheidungen, zugänglicher Repo-Kontext und ein erreichbarer Entscheidungsträger. Für die anschließende Spec-Synthese außerdem eine hinreichend geklärte Unterhaltung, Glossar/ADRs und eine geklärte Tracker-Anbindung.

**Prüfbare Ausgabe im Piloten:** Ein Entscheidungsbaum mit offenen und geklärten Punkten, expliziten Annahmen und Quellen zu recherchierten Fakten; optional eine daraus abgeleitete Spec mit Problem, Lösung, User Stories, Implementierungs- und Testentscheidungen sowie Scope-Grenzen. Der Entscheidungsbaum folgt der Quelle; ein persistiertes Pilot-Artefakt wäre unsere zusätzliche Umsetzung, keine bereits vorhandene Funktion des `grilling`-Skills.

**Belegte Aussagen:**

| ID | Aussage der Originalanweisung | path | start | end |
|---|---|---|---:|---:|
| K1 | `grilling` modelliert Entscheidungen als Baum und bearbeitet nur die aktuelle Frontier bereits entscheidbarer Fragen in Runden. | `external_repos/mattpocock/skills/skills/productivity/grilling/SKILL.md` | 6 | 8 |
| K2 | Fakten sollen durch Recherche ermittelt werden; Entscheidungen bleiben beim Nutzer. Der Abschluss verlangt eine leere Frontier und Bestätigung gemeinsamen Verständnisses vor dem Handeln. | `external_repos/mattpocock/skills/skills/productivity/grilling/SKILL.md` | 28 | 30 |
| K3 | `to-spec` verlangt keine neue Interviewrunde, sondern Synthese des bereits bekannten Kontexts; Glossar und ADRs sollen berücksichtigt werden. | `external_repos/mattpocock/skills/skills/engineering/to-spec/SKILL.md` | 7 | 13 |
| K4 | Vor der Spec-Publikation sollen Testseams geklärt und mit dem Nutzer abgestimmt werden. | `external_repos/mattpocock/skills/skills/engineering/to-spec/SKILL.md` | 15 | 19 |

**Stop-/Eskalationsgrenze:** Eine Produktentscheidung mit offener Voraussetzung nicht als entschieden ausgeben. Bei ungelösten Nutzerentscheidungen bleibt der Klärungsmodus offen. Der Originalskill fordert Bestätigung vor Handeln; `to-spec` hat zusätzlich einen Check zu Testseams. Diese Quellen erteilen dem Piloten keinerlei Tracker-Schreibrecht.

**Runtime-Abhängigkeit:** `grilling` erwartet Unteragenten für Faktenrecherche und einen Interaktionskanal für Antworten; `to-spec` erwartet Repo-Zugriff und einen konfigurierten Tracker. Ein rein lesender Pilot kann den fachlichen Vertrag prüfen, ohne Tracker oder Unteragenten zu aktivieren.

**Warnung vor Überinterpretation:** Die Anweisungen belegen eine Methode. Sie belegen weder vollständige Anforderungserfassung noch eine messbare Reduktion von Fehlentscheidungen. „Frontier leer“ hängt von der Güte des zuvor erkannten Entscheidungsbaums ab.

## 2. Kandidat: Implementierungsplanung

**Ziel:** Eine geklärte Spec in verifizierbare Arbeitseinheiten und echte Abhängigkeiten übersetzen.

**Notwendige Eingaben:** Spec/Plan oder ausreichender Gesprächskontext, bestehende Architektur und ADRs, Projektvokabular, erkennbare Test-/Demonstrationsmöglichkeiten. Für den Originalworkflow wird eine lokale oder externe Tracker-Konfiguration erwartet; ein großer pstack-Plan setzt zusätzlich Laufzeit- und Verifikationsmöglichkeiten voraus.

**Prüfbare Ausgabe im Piloten:** Tickets mit beobachtbarem Verhalten, Akzeptanzkriterien und expliziten Blockern; eine Reihenfolge, die aus diesen Blockern folgt. Bei einer breiten mechanischen Migration eine begründete Expand–Contract-Folge oder eine Integrationsgrenze anstelle künstlicher vertikaler Slices. Für größere Pläne zusätzlich pro Arbeitseinheit Belege, Voraussetzungen und Ausführungsgrenze.

**Belegte Aussagen:**

| ID | Aussage der Originalanweisung | path | start | end |
|---|---|---|---:|---:|
| P1 | Tickets sollen schmale vollständige vertikale Slices sein, einzeln demonstrierbar/verifizierbar und in einem frischen Kontext bearbeitbar. Blockierende Tickets werden ausdrücklich benannt. | `external_repos/mattpocock/skills/skills/engineering/to-tickets/SKILL.md` | 31 | 38 |
| P2 | Breite mechanische Refactors sind eine erklärte Ausnahme: Expand–Contract und Migrationsbatches; falls Batches nicht selbst grün bleiben können, gemeinsame Integrationsbranch mit finalem Integrate-and-Verify-Ticket. | `external_repos/mattpocock/skills/skills/engineering/to-tickets/SKILL.md` | 40 | 40 |
| P3 | Granularität und Blocker werden dem Nutzer zur Freigabe vorgelegt; erst danach werden Tickets lokal oder im konfigurierten Tracker veröffentlicht. | `external_repos/mattpocock/skills/skills/engineering/to-tickets/SKILL.md` | 50 | 63 |
| P4 | Das pstack-Plan-Playbook definiert den Plan als Liefergegenstand, untersagt Implementierung in diesem Modus und verlangt für dessen Ausführung ein ausdrückliches Go. | `external_repos/cursor/plugins/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md` | 3 | 11 |
| P5 | Jede Checkbox soll nur dann als erledigt gelten, wenn ein benannter Beleg existiert, etwa Datei, Log, Screenshot, Testlauf oder SHA. | `external_repos/cursor/plugins/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md` | 22 | 24 |

**Stop-/Eskalationsgrenze:** Ein Plan ist noch keine Implementierungsfreigabe. Ungeklärte Blocker oder fehlende Prüfmöglichkeit sichtbar lassen. Bei einer offensichtlichen Änderung an ein bis zwei Dateien verlangt pstack ausdrücklich, den großen Plan auszulassen und zu stoppen; siehe denselben Pfad, `start: 5`, `end: 5`.

**Runtime-Abhängigkeit:** `to-tickets` kann lokale Dateien oder einen echten Tracker verwenden. pstack erwartet unter anderem eigene Unteragententypen, weitere Skills und `check-plan.mjs`. Diese Abhängigkeiten sind hier nur registriert und wurden nicht ausgeführt. Die strengen Live-/Perf-/VM-Vorgaben des großen pstack-Plans sind keine Voraussetzung jedes denkbaren Factory-Plans.

**Warnung vor Überinterpretation:** Ein vollständiger Abhängigkeitsgraph beweist keine korrekte Schätzung, gute Architektur oder funktionierende Umsetzung. Die Ausnahme P2 darf nicht als Freibrief verstanden werden, beliebige Zwischenstände ohne überprüfbare Integrationsgrenze abzugeben.

## 3. Kandidat: Spec-Review

**Ziel:** Den konkreten Diff auf Erfüllung der ausdrücklich vorliegenden Spec prüfen und fehlende Anforderungen, Scope-Erweiterung und falsche Umsetzung getrennt sichtbar machen.

**Notwendige Eingaben:** Auflösbarer Vergleichspunkt, nichtleerer Diff, Commitliste sowie eine identifizierbare Spec mit zitierbaren Anforderungen. Der vollständige Originalskill erwartet zusätzlich Tracker-Konfiguration und einen getrennten Standards-Prüfer.

**Prüfbare Ausgabe im Piloten:** Findings mit genauem Diff-/Dateibezug, zugehöriger Spec-Zeile und Einordnung als fehlend/teilweise, nicht beauftragt oder offenbar falsch umgesetzt. Bei fehlender Spec der Status `nicht geprüft: Spec fehlt`; bei vorhandenem, aber unzureichendem Nachweis eine offene Frage anstelle erfundener Akzeptanz.

**Belegte Aussagen:**

| ID | Aussage der Originalanweisung | path | start | end |
|---|---|---|---:|---:|
| S1 | Der Vergleichspunkt muss auflösbar und der Diff nichtleer sein; Fehler sollen vor dem Start der beiden Reviews auffallen. | `external_repos/mattpocock/skills/skills/engineering/code-review/SKILL.md` | 19 | 23 |
| S2 | Die Spec wird über Commitreferenzen, Nutzerpfad oder passende Dateien gesucht. Wenn keine vorliegt, wird der Spec-Prüfer übersprungen und dies ausdrücklich berichtet. | `external_repos/mattpocock/skills/skills/engineering/code-review/SKILL.md` | 27 | 32 |
| S3 | Der Spec-Prüfer erhält Diff und Spec und soll fehlende/teilweise Anforderungen, Scope Creep und offenbar falsche Implementierung melden; jedes Finding soll die Spec-Zeile zitieren. | `external_repos/mattpocock/skills/skills/engineering/code-review/SKILL.md` | 68 | 74 |

**Stop-/Eskalationsgrenze:** Ungültiger Vergleichspunkt oder leerer Diff verhindern diesen Reviewauftrag. Fehlende Spec bedeutet fehlende Prüfung dieser Achse, keine Freigabe. Unklare Requirements müssen als solche zurückgegeben werden; die Quelle beschreibt keinen Mechanismus, sie durch Reviewer-Intuition zu ersetzen.

**Runtime-Abhängigkeit:** Git-/Diff-Lesezugriff, Zugriff auf Spec oder Tracker und im Original parallel ausführbare Unteragenten. Die fachliche Spec-Achse ist im Original Teil eines gemeinsamen Zwei-Achsen-Skills. Ihre Abbildung als eigener Pilotkandidat ist unsere Modellierung, kein zweiter unabhängig belegter Skill.

**Warnung vor Überinterpretation:** Das beschriebene Diff-Review ist lesende Analyse. Es liefert weder Laufzeitbeweis noch Testabdeckung oder eine unabhängige Release-Freigabe. Ein separater Reviewer kann dieselbe falsche Annahme wie der Builder teilen.

## 4. Kandidat: Standards-Review

**Ziel:** Einen konkreten Diff gegen dokumentierte Projektstandards prüfen und allgemeine Code-Smell-Heuristiken klar davon trennen.

**Notwendige Eingaben:** Auflösbarer Vergleichspunkt, nichtleerer Diff, Commitliste und verfügbare Standarddokumente. `CODING_STANDARDS.md` und `CONTRIBUTING.md` werden berücksichtigt, falls vorhanden. Wenn keine Projektregeln dokumentiert sind, bleibt der ausdrücklich benannte heuristische Baseline-Teil möglich; es werden keine Projektregeln erfunden.

**Prüfbare Ausgabe im Piloten:** Findings mit Datei/Hunk, präziser Fundstelle der Projektregel und Trennung zwischen dokumentierter Regelverletzung und begründeter Heuristik. Nicht geprüfte Aspekte ausdrücklich benennen; Standards- und Spec-Ergebnis getrennt erhalten.

**Belegte Aussagen:**

| ID | Aussage der Originalanweisung | path | start | end |
|---|---|---|---:|---:|
| T1 | Vorhandene Standarddokumente werden gesucht. Dokumentierte Repo-Standards haben Vorrang vor der allgemeinen Smell-Baseline; Smells sind Heuristiken und keine automatischen Regelverstöße. | `external_repos/mattpocock/skills/skills/engineering/code-review/SKILL.md` | 36 | 41 |
| T2 | Der Standards-Prüfer erhält Diff und Standardquellen; dokumentierte Verstöße und Smells sollen unterschieden, technisch bereits erzwungene Prüfungen übersprungen werden. | `external_repos/mattpocock/skills/skills/engineering/code-review/SKILL.md` | 62 | 66 |
| T3 | Die Aggregation soll Standards- und Spec-Bericht getrennt darstellen und weder Befunde noch Rangfolge achsenübergreifend verschmelzen. | `external_repos/mattpocock/skills/skills/engineering/code-review/SKILL.md` | 76 | 80 |

**Stop-/Eskalationsgrenze:** Ungültiger Vergleichspunkt oder leerer Diff wie bei S1. Bei widersprüchlichen Standardquellen muss der Pilot die Regelpriorität klären oder den Befund als ungeklärt behandeln; dies ist eine vorgeschlagene Pilotgrenze, kein expliziter Konfliktresolver des Originalskills. Eine Baseline-Heuristik darf nicht als feste Projektregel ausgegeben werden.

**Runtime-Abhängigkeit:** Git-/Dateizugriff und im Original ein Unteragent für diese Review-Achse. Tracker ist Teil der übergeordneten Skillkonfiguration. Für die standardspezifische Prüfung genügen lesbare Regeln und ein Diff; deren semantische Übertragung ist noch kein installierter Adapter.

**Warnung vor Überinterpretation:** Standards-Konformität beweist weder Anforderungserfüllung noch Funktion, Wartbarkeit oder Security. Spec-Review und Standards-Review stammen aus derselben Datei und Herkunftsfamilie; zwei getrennte Reports verdoppeln nicht die Zahl unabhängiger Quellen.

## 5. Kandidat: Ergebnisverifikation

**Ziel:** Ein behauptetes Ergebnis an der tatsächlichen Oberfläche und seinem beobachtbaren Zustand prüfen; Nachweis und verbleibende Ungewissheit erhalten.

**Notwendige Eingaben:** Genau bezeichnetes Zielartefakt/-build, erwartetes Verhalten, startfähige Testumgebung, reale Nutzeroberfläche oder Service-Schnittstelle, notwendige Seed-/Auth-Daten, zulässige Interaktionen und eine isolierte Evidenzablage. Unbekannte Voraussetzungen werden zunächst recherchiert.

**Prüfbare Ausgabe im Piloten:** Ein Nachweis mit ausgeführtem Szenario, beobachtetem Ergebnis, relevanten Nebenwirkungen, Build-/Umgebungsbezug und verbleibenden Lücken. Die Primärquelle fordert außerdem bei neu erzeugten Verifikationsskills einen End-to-End-Probelauf und dauerhaft erhaltene Beweisartefakte. Das ist nicht gleichbedeutend mit einer Pflicht, im lesenden semantischen Piloten bereits fremde Verifikationsskills zu erzeugen oder auszuführen.

**Belegte Aussagen:**

| ID | Aussage der Originalanweisung | path | start | end |
|---|---|---|---:|---:|
| V1 | Das Ergebnis soll direkt am tatsächlichen Artefakt geprüft werden; Proxies, Selbstauskunft und bloßes Kompilieren reichen nach diesem Prinzip nicht. | `external_repos/cursor/plugins/pstack/skills/principle-prove-it-works/SKILL.md` | 9 | 16 |
| V2 | Wenn möglich soll die Prüfung als erneut ausführbares deterministisches Skript mit erhaltenem Output vorliegen. | `external_repos/cursor/plugins/pstack/skills/principle-prove-it-works/SKILL.md` | 18 | 22 |
| V3 | Die Repo-Erkundung soll Oberfläche, Start, Interaktion, Beobachtung und Isolation bestimmen. Ein kaputter Checkout wird zunächst repariert oder präzise gemeldet; eine gemeinsam genutzte Instanz nicht unkontrolliert doppelt gesteuert. | `external_repos/cursor/plugins/pstack/skills/create-verification-skill/SKILL.md` | 13 | 21 |
| V4 | Der generierte Skill soll Aktion und resultierenden Zustand sowie Nebenwirkungen am realen Nutzerpfad prüfen; Cleanup erhält die Beweisartefakte. | `external_repos/cursor/plugins/pstack/skills/create-verification-skill/SKILL.md` | 27 | 31 |
| V5 | Der Verifikationsskill muss einmal Ende zu Ende mit einer gemappten Funktion durchlaufen werden. Nicht ausgeführte Skills sind Entwürfe; Stellvertreterumgebungen lassen ausdrücklich ungetestete Zielschritte offen. | `external_repos/cursor/plugins/pstack/skills/create-verification-skill/SKILL.md` | 38 | 40 |

**Stop-/Eskalationsgrenze:** Nicht startfähige Basis, fehlende Isolation, fehlende Voraussetzung oder ungeeignete Beobachtung nicht als PASS ausgeben. Der Originalgenerator erlaubt teils Reparaturen und Scaffolding; der Pilot erhält dadurch keine Reparatur- oder Schreibrechte. Ein erfolgreicher Lauf einer Funktion deckt weder alle gemappten Funktionen noch eine andere Zielumgebung ab.

**Runtime-Abhängigkeit:** Je nach Oberfläche bestehender Browser-/CLI-/PTY-/HTTP-Harness, Prozess- und Dateizugriff, gegebenenfalls Seed-Daten und Auth. Der Originalgenerator schreibt `.cursor/skills/verify-<app>/`; eine andere Runtime braucht einen geprüften Adapter. Das abstrakte Prüfprinzip ist davon trennbar.

**Warnung vor Überinterpretation:** Die vorhandene Anweisung ist kein ausgeführter Test und kein Nachweis, dass eine Anwendung korrekt ist. Auch ein tatsächlicher PASS gilt nur für Szenario, Build, Umgebung und Beobachtung; deterministische Wiederholbarkeit allein beweist nicht die Richtigkeit des Prüfkriteriums.

## Zwei tatsächlich belegte Methodenspannungen

### A. Klären durch Rückfragen oder bereits geklärten Kontext synthetisieren?

`grilling` verlangt wiederholte Entscheidungsrunden bis zur leeren Frontier und Bestätigung vor Handeln: `external_repos/mattpocock/skills/skills/productivity/grilling/SKILL.md`, `start: 6`, `end: 8` und `start: 28`, `end: 30`. `to-spec` verlangt ausdrücklich, **kein** neues Interview zu führen, sondern bereits besprochenes Wissen zu synthetisieren: `external_repos/mattpocock/skills/skills/engineering/to-spec/SKILL.md`, `start: 7`, `end: 7`.

**Spannung:** Beide Anweisungen wären als gleichzeitig aktive Root-Regeln gegensätzlich. Es handelt sich um zwei sinnvoll unterscheidbare Arbeitsmodi, nicht um einen Beleg, dass eine Methode überlegen ist. **Vorgeschlagene Auflösung im Piloten:** Bei offenen Produktentscheidungen Klärung; bei hinreichend geklärtem Gespräch Synthese. Der Seam-Check von `to-spec` bleibt ein eigener expliziter Check und macht aus dem Synthesemodus kein vollständiges Grilling.

### B. Stabiles Verhaltensziel oder dateigenaue Ausführungsanleitung?

`to-tickets` verlangt, spezifische Dateipfade und Codesnippets grundsätzlich zu vermeiden, weil sie schnell veralten; eine enge Ausnahme gilt für entscheidungstragende Prototypsnippets: `external_repos/mattpocock/skills/skills/engineering/to-tickets/SKILL.md`, `start: 105`, `end: 105`. Der große pstack-Plan verlangt dagegen unter jedem PR einen Files- und Build-Block mit konkreten Dateipfaden und Symbolen: `external_repos/cursor/plugins/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md`, `start: 78`, `end: 94`.

**Spannung:** Beständigkeit und Implementierungsfreiheit stehen gegen unmittelbar ausführbare Präzision. Die Artefakte haben unterschiedliche Zwecke; die Quellen behaupten keine universelle Auflösung. **Vorgeschlagene Auflösung im Piloten:** Verhaltensvertrag und blockierende Ergebnisse im langlebigen Ticket erhalten; einen dateigenauen Ausführungsplan separat an den untersuchten Commit binden. Änderungen am Repo markieren diesen Plan zur erneuten Prüfung, ohne dadurch automatisch das fachliche Ziel zu ändern.

## Ergänzende Grenze aus der eigenen Primärquelle

Itamar Friedman verlangt geschützte Abnahmekriterien und getrennte Zuständigkeit; ein zweiter Agent mit Reviewer-Titel sei noch kein unabhängiger Prüfer: `00_Inbox/Quellen/X/2026-10-22-itamar_mar-2113255396299128887.md`, `start: 62`, `end: 65`. Der Originaltext nennt die Anforderung, Prüfungen, Constraints und Restunsicherheit als Bestandteile eines nachvollziehbaren Laufs und verwirft universelle Korrektheitsbeweise: gleicher Pfad, `start: 69`, `end: 72`.

Dies ist eine Entwurfsposition des Autors, kein gemessener Beleg. Sie begrenzt die Interpretation der fünf Kandidaten: Mehrere Review-Achsen oder ein schöner Evidenzbericht erlauben keine Behauptung unabhängiger Abnahme. Für den Piloten sollten die Herkunft der Akzeptanzbedingungen und die Befugnis, sie zu ändern, explizit modelliert werden. Rohquelle und Source-Notiz zählen dabei weiterhin nur einmal.

## Konsolidierung für den Hauptagenten

- Alle fünf Kandidaten haben mindestens zwei direkte Originalbelege; Spec- und Standards-Review teilen absichtlich eine Ursprungsskilldatei.
- Die Verträge sind noch keine freigegebenen, installierten oder durch praktische Aufgaben evaluierten Fähigkeiten.
- Claim-Evidenz wird auf kurze `path/start/end`-Bereiche zurückgeführt; Repo-Commit und Herkunftsfamilie stehen separat, damit mehrere Textstellen nicht als unabhängige Stimmen gezählt werden.
- Für Ergebnisverifikation sind vorhandenes Prüfprinzip, Verifikationsgenerator und erfolgreicher echter Testlauf drei verschiedene Status.
- Nur diese neue Berichtsdatei wurde geschrieben. Keine repo-weiten Checks, keine Bestandsdateien verändert.
