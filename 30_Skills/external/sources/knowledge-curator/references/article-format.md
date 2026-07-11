# Article Format

Diese Referenz beschreibt Source Notes in `src/content/knowledge/{slug}.md`. Maßgeblich ist `src/types/knowledge.ts`; der Curator verwendet für neue Source Notes zusätzlich die unten genannten strengeren Pflicht- und Qualitätsregeln.

## Inhalt

- [Unterstütztes Schema](#unterstütztes-schema)
- [Kanonische Source Note](#kanonische-source-note)
- [Adaptive Synthese und Sprache](#adaptive-synthese-und-sprache)
- [Create, Update, Improve und Merge](#create-update-improve-und-merge)
- [Quellen und Verbindungen](#quellen-und-verbindungen)
- [Bilder und Assets](#bilder-und-assets)
- [Validator und Merge-Gate](#validator-und-merge-gate)
- [Mermaid und Tabellen](#mermaid-und-tabellen)

## Unterstütztes Schema

| Feld          | Typ / Enum                                    | Source-Note-Regel                                                                                                          |
| ------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `id`          | `string`                                      | Runtime-/Loader-Feld; nicht ins Frontmatter schreiben, sofern der Loader es aus dem Dateinamen ableitet                    |
| `title`       | `string`                                      | Pflicht, prägnanter deutscher Titel                                                                                        |
| `description` | `string`                                      | Pflicht, ein bis zwei aussagekräftige Sätze                                                                                |
| `category`    | `string`                                      | Pflicht; vorhandene Projektkategorie bevorzugen                                                                            |
| `icon`        | `string`                                      | Pflicht; vorhandenen passenden Lucide-Namen bevorzugen                                                                     |
| `readTime`    | `string \| number`                            | Schema erlaubt beides; neue/kuratierte Artikel verwenden eine ganze Zahl                                                   |
| `tags`        | `string[]`                                    | Pflicht und nicht leer; vorhandene, möglichst hierarchische Tags bevorzugen                                                |
| `connections` | `string[]`                                    | Optionales Schemafeld; fachliche Links werden zusätzlich beziehungsweise bevorzugt im Body unter `## Verbindungen` geführt |
| `aliases`     | `string[]`                                    | Pflicht und nicht leer                                                                                                     |
| `topics`      | `string[]`                                    | Pflicht und nicht leer; Einträge als YAML-gequotete Wikilinks                                                              |
| `type`        | `source \| concept`                           | Für Source Notes Pflicht: `source`                                                                                         |
| `status`      | `seed \| incubating \| evergreen \| archived` | Pflicht                                                                                                                    |
| `up`          | `string`                                      | Optionaler YAML-gequoteter Wikilink zum übergeordneten Konzept                                                             |
| `sourceURL`   | `string`                                      | Pflicht; belegte Primärquelle, vorzugsweise Canonical URL                                                                  |
| `sourceType`  | `tweet \| blog \| thread \| docs`             | Pflicht; GitHub-Repositories und technische Dokumentation sind `docs`                                                      |
| `author`      | `string`                                      | Wenn zuverlässig feststellbar                                                                                              |
| `sourceDate`  | `string`                                      | Wenn zuverlässig feststellbar; `YYYY-MM-DD`                                                                                |
| `addedDate`   | `string`                                      | Pflicht; `YYYY-MM-DD`                                                                                                      |
| `content`     | `string`                                      | Runtime-Feld aus dem Markdown-Body; nicht ins Frontmatter schreiben                                                        |
| `level`       | `beginner \| intermediate \| advanced`        | Optional, wenn sinnvoll bestimmbar                                                                                         |
| `hot`         | `boolean`                                     | Optional; bestehenden Wert bewahren, nicht ohne Anlass setzen                                                              |

Für neue Source Notes sind `title`, `description`, `type`, `status`, `category`, `icon`, `readTime`, `tags`, `aliases`, `topics`, `sourceURL`, `sourceType` und `addedDate` Pflicht. `author` und `sourceDate` ergänzen, soweit feststellbar; `level`, wenn sinnvoll bestimmbar. Keine nicht unterstützten Frontmatter-Felder erfinden.

`readTime` ist `max(1, ceil(Wörter im Markdown-Body / 140))` und wird als Integer ohne Einheit geschrieben. Codeblöcke, URLs und Markdown-Syntax zählen nach Maßgabe des Validators nicht als Fließtext. Nach jeder größeren Textänderung neu berechnen.

## Kanonische Source Note

```markdown
---
title: "Context Engineering für zuverlässige Coding-Agents"
description: "Der Artikel erklärt, wie gezielte Kontextauswahl Coding-Agents verlässlicher macht und welche Grenzen dabei beachtet werden müssen."
type: source
status: seed
category: workflows
icon: BrainCircuit
readTime: 1
tags:
  - workflows/context-engineering
  - tooling/coding-agents
aliases:
  - "Kontext für Coding-Agents"
topics:
  - "[[Context Engineering]]"
  - "[[Coding Agents]]"
up: "[[Agent Workflows]]"
sourceURL: "https://example.com/context-engineering"
sourceType: blog
author: "Ada Beispiel"
sourceDate: "2026-07-01"
addedDate: "2026-07-11"
level: intermediate
---

![Diagramm zur Auswahl relevanten Kontexts](/images/knowledge/context-engineering-coding-agents/context-selection.png)

Coding-Agents benötigen nicht möglichst viel, sondern den für die Aufgabe richtigen Kontext. Dieser Artikel ordnet die wichtigsten Auswahlentscheidungen ein und zeigt, wo zusätzliche Informationen die Ausführung verbessern oder unnötig belasten.

## Kontext gezielt auswählen

Erkläre zuerst das Konzept und seinen Nutzen. Ordne anschließend belegte Details nach Lernlogik statt nach der Reihenfolge der Quelle ein. Englische Tech-Termini wie Context Window, Tool Calling oder Retrieval bleiben erhalten, wenn eine Übersetzung unpräzise wäre.

## Grenzen und praktische Anwendung

Trenne Aussagen der Quelle von ergänzendem Erklärungskontext. Kennzeichne Unsicherheiten und benenne Versions- oder Quellenkonflikte, statt Lücken plausibel klingend zu schließen.

## Quellen

- [Primärartikel](https://example.com/context-engineering) — Grundlage für Konzept und Empfehlungen.
- [Ergänzende Dokumentation](https://docs.example.com/context) — belegt die versionsabhängige Implementierung.

## Verbindungen

- [[Context Engineering]]
- [[Coding Agents]]
- [[Agent Workflows]]
```

Das Beispiel demonstriert die vollständige Form, ist aber kein Längentemplate. Die verbindlichen Sektionsregeln stehen unter [Quellen und Verbindungen](#quellen-und-verbindungen).

## Adaptive Synthese und Sprache

- Kurze Quellen: Kernaussage vollständig erhalten und nur den Kontext ergänzen, der Begriffe, Nutzen, Voraussetzungen oder Grenzen verständlich macht. Ergänzung nicht als Aussage der Quelle ausgeben.
- Lange Quellen: Nach Konzepten, Lernlogik und Relevanz verdichten. Zentrale Begründungen, Einschränkungen, Beispiele und Gegenargumente erhalten; nicht mechanisch Abschnitt für Abschnitt paraphrasieren.
- Mehrere Quellen: Übereinstimmungen zusammenführen, komplementäre Perspektiven zuordnen und Widersprüche mit Quelle, Datum oder Version benennen. Die Struktur folgt dem Thema, nicht der Quellenreihenfolge.
- Professionelles, natürliches Deutsch mit Du-Ansprache verwenden. Englische Tech-Termini, Code, Prompts, API-Namen und präzisionskritische Formulierungen im Original belassen.
- Echte Umlaute (`ä`, `ö`, `ü`, `Ä`, `Ö`, `Ü`) und `ß` im Fließtext verwenden; keine ASCII-Umschreibungen. Direkte Zitate sparsam und kurz einsetzen, sonst paraphrasieren.
- Mit einem kurzen Einstieg zu Thema, Nutzen und Kontext beginnen. `##` und `###` nach fachlicher Hierarchie verwenden; eine zusätzliche H1 ist nicht nötig, weil `title` den Artikeltitel liefert.

## Create, Update, Improve und Merge

- **create:** Exakte normalisierte URL-Dubletten und thematische Überschneidungen prüfen. Neuen Slug und Asset-Ordner nur anlegen, wenn der Artikel wirklich neu ist; bei exakter Dublette den vorhandenen Artikel melden.
- **update:** Neue belegte Informationen und korrigierte zeitabhängige Aussagen einarbeiten. Weiterhin richtige Inhalte, manuelle Ergänzungen, Metadaten, Wikilinks und Assets bewahren. Quellenmetadaten nur ändern, wenn der neue Beleg dies trägt.
- **improve:** Fachlichen Kern erhalten und Sprache, Struktur, Frontmatter, Verbindungen, Quellen, Bilder und Lesbarkeit verbessern. Keine neuen Tatsachen ohne Quelle und keine nützlichen Details allein zugunsten kürzerer Prosa entfernen.
- **merge:** Zielartikel vorab festlegen, Inhalte und Provenienz aller Eingaben inventarisieren, Redundanzen entfernen und Konflikte sichtbar integrieren. Quelldateien sowie verwaiste Assets erst nach erfolgreicher Zielvalidierung löschen.

Bei den Änderungsmodi `update`, `improve` und `merge` ist der aktuelle Arbeitsbaum die schützenswerte Basis. Unklare lokale Änderungen nicht überschreiben; bei nicht auflösbaren Konflikten vor destruktiven Schritten stoppen.

## Quellen und Verbindungen

Unter `## Quellen` jede zusätzlich verwendete Quelle als beschreibenden Markdown-Link aufführen und knapp angeben, was sie belegt. `sourceURL` bleibt die Primärquelle. Eine Quelle darf nur Aussagen stützen, die dort tatsächlich enthalten sind; bei Aktualität oder Versionsbezug erneut prüfen.

Der Abschnitt ist erforderlich, sobald neben `sourceURL` mindestens eine weitere Quelle tatsächlich verwendet wurde; bei nur einer Primärquelle darf er entfallen. Unter `## Verbindungen` immer mindestens zwei einzigartige, fachlich relevante Entitäten und Konzepte als Wikilinks aufführen, keine bloßen Keywords. Links müssen zum Artikelkern passen; bestehende Knoten und konsistente Namen bevorzugen. Vorhandene relevante Verbindungen bei `update`, `improve` und `merge` erhalten.

## Bilder und Assets

- Nur redaktionell relevante Bilder übernehmen: erklärende Diagramme, Screenshots, Illustrationen oder Medien, auf die der Text fachlich Bezug nimmt. Avatare, Tracking-Pixel, Emojis, UI-Dekoration und Logos ohne Erklärwert verwerfen.
- Vor jedem lokalen Kopieren Lizenz oder ausdrückliche Nutzungserlaubnis und sämtliche Attributionspflichten prüfen. In der Evidenzliste Urheber, originale Medien-URL, Lizenz und – sofern vorhanden – Lizenz-URL festhalten. Verlangt die Lizenz Attribution, muss der veröffentlichte Artikel direkt in der Bildunterschrift oder in einem expliziten `## Quellen`-Eintrag sichtbar Urheber, Original-Asset-URL, Lizenzname mit Lizenzlink und Änderungsstatus (`unverändert` oder `bearbeitet`, gegebenenfalls mit Art der Bearbeitung) nennen. Die interne Evidenzliste allein genügt nicht. Sind Rechte oder Pflichten unklar, das Medium nicht kopieren; stattdessen zur Quelle verlinken oder den relevanten Inhalt beschreiben.
- Dateien unter `public/images/knowledge/{slug}/` ablegen. Stabile beschreibende Namen wie `context-selection.png` statt laufender Zufallsnamen verwenden.
- Lokale Bilder ausschließlich in den Rasterformaten `png`, `jpg`/`jpeg`, `gif`, `webp` oder `avif` speichern. Dateiendung aus dem tatsächlichen Dateityp ableiten und MIME-Typ, Dateigröße, Lesbarkeit sowie zum Suffix passende Dateisignatur prüfen. SVG wird vom Validator immer abgelehnt: Ist es fachlich und rechtlich verwendbar, mit einem vertrauenswürdigen Tool in ein erlaubtes Rasterformat konvertieren und anschließend das Raster prüfen; andernfalls die Quelle verlinken oder den Inhalt beschreiben.
- Markdown ausschließlich mit absoluten, zum Artikelslug passenden Public-Pfaden referenzieren: `![Aussagekräftiger Alt-Text](/images/knowledge/{slug}/datei.png)`. Keine relativen Pfade, Query-Strings oder Fragmente verwenden.
- Alt-Text beschreibt Inhalt und fachlichen Zweck, nicht nur „Bild“ oder einen Dateinamen. Captions oder begleitende Prosa ergänzen, wenn die Herkunft oder Interpretation sonst unklar bleibt.
- Originalreihenfolge bewahren, sofern die fachliche Lernlogik keinen begründeten anderen Platz verlangt. Bilder nahe der zugehörigen Erklärung einfügen; nicht pauschal alles als Header verwenden.
- Provenienz muss über Primärquelle und Kontext eindeutig sein. Stammt ein Asset aus einer Zusatzquelle, diese unter `## Quellen` nennen.
- Nur erfolgreich gespeicherte und geprüfte Assets referenzieren. Keine kaputten Pfade; keinen leeren Asset-Ordner behalten. Bei Updates relevante vorhandene Assets nicht ungefragt ersetzen.

## Validator und Merge-Gate

Das Skill-Verzeichnis als Verzeichnis der geladenen `SKILL.md` auflösen und den gebündelten Validator vom Projektkontext aus ausführen:

```text
node <resolved-skill-directory>/scripts/validate-knowledge-article.mjs <article.md> --project-root <project-root> --additional-source-count <N>
```

`N` bezeichnet die Zahl tatsächlich verwendeter Quellen zusätzlich zu `sourceURL`. Fehler beheben und erneut prüfen.

Nur für `merge` in einen **neuen** Zielartikel darf eine übernommene `sourceURL` vorübergehend mit wiederholtem `--allow-duplicate-source <source-note.md>` freigegeben werden. Jeden Schalter ausschließlich für eine exakt benannte, noch vorhandene Quellnote setzen, deren Löschung nach erfolgreicher Zielvalidierung und Projektprüfung ausdrücklich erlaubt ist. Die Option nie bei `create`, `update` oder `improve`, nie für pauschale Verzeichnisse und nie für dritte Dubletten verwenden.

Nach bestandenem Allowlist-Prüflauf und erfolgreicher Projektprüfung nur die freigegebenen Quellnotes und verwaisten Assets bereinigen. Danach den Zielartikel ohne `--allow-duplicate-source` erneut validieren; erst dieser erfolgreiche Lauf schließt das Merge-Gate.

## Mermaid und Tabellen

Mermaid nur verwenden, wenn Abläufe, Architektur, Abhängigkeiten, Zustände oder Entscheidungen dadurch materiell verständlicher werden. Unterstützt sind ausschließlich:

`flowchart`, `graph`, `sequenceDiagram`, `classDiagram`, `stateDiagram`, `stateDiagram-v2`, `erDiagram`, `journey`, `timeline`, `mindmap`, `quadrantChart`, `xychart-beta`, `sankey-beta`.

Der erste nichtleere Token im `mermaid`-Codeblock muss einer dieser Typen sein. Diagramme kompakt halten und nur belegbare Beziehungen zeigen. Der Text muss ohne Diagramm verständlich bleiben.

Tabellen nur für echte Vergleiche, Zuordnungen oder strukturierte Referenzdaten verwenden. Keine dekorativen Visualisierungen und keine Wiederholung bereits klarer Prosa. Wenn Tabelle oder Diagramm keinen zusätzlichen Erklärwert liefert, weglassen.
