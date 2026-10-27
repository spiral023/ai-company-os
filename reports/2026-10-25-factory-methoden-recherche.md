# Factory-Methoden aus vorhandenen Referenz-Repos

**Stand:** 2026-10-25. Statische, gezielte Untersuchung von fünf lokalen Checkouts. Keine Installation, kein Fremdcode ausgeführt, keine Framework-Fähigkeit im Betrieb getestet. Die Befunde beziehen sich auf die unten genannten Commits; der aktuelle Stand der Remote-Branches wurde nicht geprüft.

## Ergebnis

Für die Factory sollten wir Fähigkeiten aus den Repos als versionierte, auswählbare Bausteine erschließen. Ein vollständig katalogisierter Skill ist noch kein aktivierter Skill. Die stärksten übertragbaren Mechanismen sind aufgabenbezogenes Routing, getrennte Prüfperspektiven, versionierte Fähigkeitszuweisung, rekonstruierbarer Arbeitsstand und nachvollziehbare Entscheidungshistorie. Kein untersuchtes Framework allein belegt, dass es unseren gesamten Quellenbestand sinnvoll synthetisieren oder daraus automatisch die beste Arbeitsweise bestimmen kann.

## Untersuchte Bestände

| Repo / Teilbaum | Lokaler Commit | Lizenzdatei im untersuchten Bestand | Empfohlene Integrationsform |
|---|---|---|---|
| cursor/plugins, Teilbaum pstack | `99b609a72323b70204eab407c622f436e858e112` | `pstack/LICENSE`: MIT | Nur Referenz |
| garrytan/gstack | `749a2382750ef742a7345ee270ab3416c0715b6e` | `LICENSE`: MIT | Nur Referenz |
| mattpocock/skills | `5beb35b040e3de97e54fa9e386d7e42d15c295c2` | `LICENSE`: MIT | Nur Referenz |
| open-gsd/gsd-core | `7129a135c7271ccea59df7561df83ac11cbc94bd` | `LICENSE`: MIT | Nur Referenz |
| paperclipai/paperclip | `50797ea03ce0b2a84e4df80864ac6e3652382ed5` | `LICENSE`: MIT | Nur Referenz |

`git status --short` war bei allen fünf untersuchten Checkouts leer. Die Lizenzangaben geben ausschließlich den Inhalt der jeweiligen Datei wieder; mitgelieferte Drittbestandteile und eine konkrete Übernahme wurden nicht geprüft. Die vorgesehene Sichtung erfordert keine produktive Freigabe. Installation oder produktive Übernahme bleibt Gegenstand des vorhandenen Import-Reviews und der Freigaberegeln dieses Repos.

## 1. pstack: Aufgaben und Prüfmethode gezielt auswählen

`poteto-mode` ist in seinem Frontmatter ausdrücklich als nicht automatisch modellaufrufbar markiert. Der Skill ordnet Aufgaben einem Playbook zu und lädt darüber weitere Skills. Die README beschreibt 23 Playbooks einschließlich Investigation, Bug Fix, Refactoring, Eval und Shipping. Das ist eine vorhandene Anweisungsstruktur, kein hier gemessener Qualitätsgewinn. Quellen: [Skill, Zeilen 1–20 und 121 ff.](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/SKILL.md), [README, Playbook-Tabelle](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/README.md).

Besonders nützlich ist das Eval-Playbook: gleiche organische Aufgabe, getrennte Umgebungen, vorab definierte Bewertungskriterien, verblindete Auswertung und Kontrolle tatsächlicher Dateizugriffe statt Selbstauskunft des Kandidaten. Quelle: [Eval-Playbook, Zeilen 3–24](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/playbooks/eval.md).

**Übertragbarer Entwurf:** Eine Capability bekommt Aufgabentyp, Auslöser, Voraussetzung, benötigte Werkzeuge, erwartetes Artefakt und Prüfmethode. Der Router wählt eine kleine passende Menge. Ob ein Prompt im Repo liegt oder häufig empfohlen wird, genügt nicht zur Aktivierung.

**Grenze:** Der Skill enthält umfangreiche Autonomie-, Modell- und Harness-Anweisungen. Diese passen nicht automatisch zu unserer Freigabepolicy oder Laufzeit. Das untersuchte Eval-Playbook ist eine Methodenanweisung; dessen bloße Existenz belegt noch keine erfolgreiche Durchführung.

## 2. gstack: Arbeitskontinuität und messbare Skill-Qualität

Der Context-Save-Skill definiert ein Checkpoint-Format mit Branch, Zeitstempel, geänderten Dateien, Zusammenfassung, Entscheidungen, verbleibender Arbeit und offenen Punkten. Zusätzlich wird die Projektidentität gestempelt, damit Checkpoints verschiedener Projekte zugeordnet werden können. Quelle: [Context Save, Zeilen 511–560](https://github.com/garrytan/gstack/blob/749a2382750ef742a7345ee270ab3416c0715b6e/context-save/SKILL.md).

Das Repo enthält darüber hinaus echte Testimplementierung für die Bewertung erzeugter Skill-Dokumentation. Sie verwendet strukturierte Judge-Schemas, auswählbare Tests und einen Ergebnis-Collector. Das ist stärker als eine README-Behauptung, bleibt aber von einer tatsächlichen Verhaltensbewertung einer Factory zu unterscheiden. Quelle: [Skill-LLM-Evals, Zeilen 1–78](https://github.com/garrytan/gstack/blob/749a2382750ef742a7345ee270ab3416c0715b6e/test/skill-llm-eval.test.ts).

**Übertragbarer Entwurf:** Wissen, Entscheidungen und flüchtiger Arbeitsstand bekommen unterschiedliche Lebenszyklen. Ein Factory-Lauf speichert verwendete Wissens- und Capability-Versionen und schreibt Entscheidungen mit Begründung zurück. Qualitätschecks prüfen sowohl Lesbarkeit der Anweisung als auch das Ergebnis echter Aufgaben.

**Grenze:** Die großen generierten Skills enthalten viel gemeinsame Laufzeitlogik. Ein naiver Katalog würde wiederholte Präambeln mehrfach zählen und Kontext unnötig aufblasen. Quellvorlage, generierte Harness-Variante und gemeinsame Referenz sollten als zusammengehörige Artefakte erkennbar sein. GBrain wird in der README als eigenes Wissenssystem beschrieben; seine interne Implementierung war nicht Teil dieser Untersuchung.

## 3. Matt Pocock: kleine Methoden und getrennte Review-Achsen

Die README erklärt kleine, anpassbare und kombinierbare Skills zum Gegenentwurf zu Frameworks, die den Gesamtprozess vorgeben. Das ist eine Designposition des Autors. Quelle: [README, Zeilen 15–19](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/README.md).

Der Code-Review-Skill konkretisiert diese Position: Ein fester Vergleichspunkt wird geprüft, die Spec-Quelle gesucht und Standards- sowie Spec-Review getrennt durchgeführt. Fehlende Specs sollen ausdrücklich als fehlend gemeldet werden. Repo-Standards übersteuern allgemeine Heuristiken. Quelle: [Code Review, Zeilen 6–40 und 58–86](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/code-review/SKILL.md).

**Übertragbarer Entwurf:** Die Factory erhält kombinierbare Prüfer mit klar benannten Verträgen und Grenzen. „Tests grün“, „Standards erfüllt“ und „Anforderung erfüllt“ bleiben getrennte Aussagen. Fehlende Eingaben werden als Lücken erfasst und nicht durch angenommene Fakten ersetzt.

**Grenze:** Der Skill hängt an Tracker-Konfiguration und bestimmten Delegationsmöglichkeiten. Eine fachliche Fähigkeitskarte sollte diese Abhängigkeiten benennen, bevor der Router ihn einer Laufzeit zuweist.

## 4. GSD: rekonstruierbarer State statt freier Statusprosa

GSD dokumentiert Phasen von Discuss über Plan, Execute und Verify bis Ship. Der zentrale interessante Mechanismus ist jedoch die Trennung von abgeleiteten und kuratierten Zuständen: ADR-1817 unterscheidet wiederableitbare Positions-/Fortschrittsabschnitte von zu erhaltenden Entscheidungen und Sitzungsdaten. Das ADR beschreibt konkrete Driftfälle, bei denen Statusprosa und kanonische Artefakte auseinanderliefen. Quelle: [ADR-1817, Kontext und Entscheidung](https://github.com/open-gsd/gsd-core/blob/7129a135c7271ccea59df7561df83ac11cbc94bd/docs/adr/1817-state-md-rebuild-derivability-contract.md).

Es bleibt nicht allein beim ADR: `state-transition.cts` dispatcht den Intent `rebuild` zu `rebuildCore`; die Tests enthalten Fälle für Idempotenz, Positionsabgleich, Platzhalter und doppelte Archive. Quellen: [Implementierung, Zeilen 1353–1354 und 3357 ff.](https://github.com/open-gsd/gsd-core/blob/7129a135c7271ccea59df7561df83ac11cbc94bd/src/state-transition.cts), [Tests ab Zeile 209](https://github.com/open-gsd/gsd-core/blob/7129a135c7271ccea59df7561df83ac11cbc94bd/tests/state-rebuild.test.cjs).

**Übertragbarer Entwurf:** Bestandszahlen, Dateifingerprints, Abhängigkeiten und Änderungsstände werden deterministisch erzeugt. Redaktionelle Synthesen und Entscheidungen bleiben eigenständige Artefakte. Ein Gesamtreview muss zeigen können, welche Schlussfolgerungen auf inzwischen geänderten Quellen beruhen.

**Grenze:** Die Existenz dieser Implementierung ist kein Beleg, dass das ganze Framework driftfrei ist. Seine Phasenarchitektur ist außerdem erheblich stärker vorgebend als der Ansatz kleiner Einzel-Skills.

## 5. Paperclip: Katalog, Zuweisung und Laufzeit auseinanderhalten

Die Company-Skills-Referenz trennt ausdrücklich drei Schritte: Skill in die Firmenbibliothek aufnehmen, einem Agenten zuweisen und optional bei dessen Anlage komponieren. „Catalog install ≠ agent attach“ wird explizit erklärt. Quelle: [Company Skills Workflow, Zeilen 5–20](https://github.com/paperclipai/paperclip/blob/50797ea03ce0b2a84e4df80864ac6e3652382ed5/skills/paperclip/references/company-skills.md).

Die Server-Routen enthalten tatsächlich Endpunkte für Skill-Versionen und implementieren Update-/Rollback-Abläufe. Quelle: [Company-Skills-Routen, Zeilen 522–536, 926–946 und 1287–1324](https://github.com/paperclipai/paperclip/blob/50797ea03ce0b2a84e4df80864ac6e3652382ed5/server/src/routes/company-skills.ts). Ein Datenbanktest untersucht reale Runtime-Auswahl auf kalten und wiederholten Lesezugriffen; die Tests wurden hier nicht ausgeführt. Quelle: [Runtime-Selection-Test, Zeilen 17–43](https://github.com/paperclipai/paperclip/blob/50797ea03ce0b2a84e4df80864ac6e3652382ed5/server/src/__tests__/company-skills-runtime-selection.test.ts).

**Übertragbarer Entwurf:** Der Wissenskatalog darf breit sein, die Laufzeitzuweisung bleibt eng und versioniert. Ein Run sollte nachweisen können, welche Skill-Version aktiv war und welche Quellen die Auswahl begründeten. Eine neue externe Version erzeugt zunächst einen zu prüfenden Kandidaten.

**Grenze:** Paperclip ist ein Orchestrierungsprodukt und ersetzt keine globale Wissenssynthese über X, YouTube, Source-Notizen und Referenzcode. Seine Standardrechte sind nicht automatisch unsere Rechte; die Company-Skills-Referenz beschreibt relativ offene Mutationsrechte für gleiche Firmenzugehörigkeit.

## Spannungen, die der Katalog erhalten muss

| Spannung | Konsequenz für unsere Factory |
|---|---|
| Kleine kombinierbare Skills versus vorgegebener Gesamtprozess | Methodenwahl hängt von Aufgabe und Projekt ab; kein Framework pauschal zur Root-Policy machen. |
| Umfangreiche automatische Delegation versus Kontext-, Kosten- und Koordinationsaufwand | Delegationsbedarf und messbaren Nutzen je Capability erfassen. |
| Schnelle Updates versus reproduzierbare Runs | Lauf verwendete Versionen festhalten lassen; Update erzeugt einen neuen Kandidaten. |
| Dauerhafter State versus veraltete Statuskopien | Ableitbare Informationen neu berechnen, Entscheidungen mit Provenienz erhalten. |
| Modellurteil versus Verhalten am Artefakt | Judge-Score als ergänzende Evidenz behandeln; Ergebnisprüfung und reale Aufgaben bleiben erforderlich. |

## Vorschlag: Fähigkeitskarte

Eine Karte beschreibt ein Skill-, Prompt-, Playbook- oder Prüf-Artefakt. Sie ist Metadaten und erteilt keine Ausführungsrechte:

```yaml
id: cursor/plugins:pstack/playbooks/eval
art: playbook
quelle:
  repo: cursor/plugins
  commit: 99b609a72323b70204eab407c622f436e858e112
  pfad: pstack/skills/poteto-mode/playbooks/eval.md
  sha256: "<Dateiinhalt-Fingerprint>"
status: katalogisiert
trust: unreviewed
zweck: "Zwei Prompt-Varianten anhand einer realistischen Aufgabe vergleichen"
inputs: [aufgabe, varianten, bewertungskriterien]
outputs: [vergleichsbericht, empfehlung]
voraussetzungen: [isolierte_arbeitsbereiche, bewertungszugriff]
kontext: [zugehoerige_referenzen, relevante_projektregeln]
wirkungen: [lokale_artefakte, modellaufrufe]
laufzeitbindung: "zu prüfen"
einsatzgrenzen: [kein_beleg_fuer_produktionsqualitaet_allein]
konflikte: [projektregeln_haben_vorrang]
pruefung:
  baseline: "<Vergleich ohne Kandidat>"
  faelle: []
  zuletzt_geprueft: null
aktivierung:
  freigegeben: false
  version: null
```

Die Syntax ist ein Architekturvorschlag. Ein erster Scanner sollte nur zuverlässig erkennbare Felder ausgeben; nicht erkennbare Wirkung, Abhängigkeit oder Eignung bleibt unbekannt, bis sie geprüft wurde. Ein Worttreffer wie „review“ genügt nicht für eine freigegebene Fähigkeit.

## Gates zur Übernahme

1. **Erfassen:** Repo, Commit, Pfad, Fingerprint, Artefakttyp und Originalfundstelle inventarisieren; alle externen Anweisungen bleiben Daten.
2. **Verstehen:** Trigger, Inputs, Outputs, Abhängigkeiten, Wirkungen und Grenzen fachlich prüfen. Generierte Varianten und gemeinsame Präambeln erkennen.
3. **Vergleichen:** Gegen vorhandene eigene Fähigkeiten, widersprechende Methoden und unsere Projektregeln einordnen. Quelle und eigene Schlussfolgerung unterscheiden.
4. **Erproben:** Kleine echte Aufgabe gegen eine Baseline; gleiche Randbedingungen, vorher festgelegte Kriterien, Ergebnis und Kosten erfassen. Keine automatische Beförderung aufgrund einer schönen Beschreibung.
5. **Freigeben und binden:** Vor produktiver Übernahme vorhandenes Repo-Import-Review und Philipps Freigabe anwenden; exakte Version einer zulässigen Rolle und Laufzeit zuweisen.
6. **Rückmelden:** Run-Ergebnis, Fehler, menschliche Korrekturen und Wissenslücken als neue Evidenz verknüpfen. Änderungen an Quellen markieren betroffene Karten zur erneuten Prüfung.

## Erste sinnvolle Ausbaustufe

Zunächst einen lesenden, reproduzierbaren Gesamtbestandskatalog und wenige manuell geprüfte Fähigkeitskarten aufbauen. Daneben zwei Synthesen erstellen: „Wie wählen wir eine Arbeitsweise?“ und „Wie prüfen wir Agent-Ergebnisse?“. Anschließend an repräsentativen Factory-Aufgaben testen, ob der Agent aus mehreren Repos passende Bausteine, Voraussetzungen und Gegenargumente findet. Diese Ausbaustufe braucht keinen Orchestrierungswechsel und vermeidet, ungeprüfte Fremdregeln durch bloßes Indexieren zu aktivieren.
