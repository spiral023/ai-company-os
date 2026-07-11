---
name: knowledge-curator
description: Use when creating, updating, improving, or merging Markdown knowledge articles from URLs, X/Twitter posts or threads, websites, documentation, GitHub repositories, multiple sources, or existing knowledge notes, especially when source images and provenance must be preserved.
---

# Knowledge Curator

## Überblick

Quellen in belegbare, Obsidian-kompatible Source Notes überführen oder vorhandene Notes sicher weiterentwickeln.

**Kernprinzip:** Erst vollständig erfassen und Aussagen, Quellen, Konflikte sowie Medien intern zuordnen; danach adaptiv synthetisieren. Keine Lücke plausibel ergänzen und keine Provenienz verlieren.

## Modi wählen

Eine ausdrückliche Nutzerangabe hat Vorrang. Sonst Auftrag und Bestand auswerten. Nur nach dem Ziel fragen, wenn mehrere Ziele gleich plausibel sind.

| Modus | Ziel | Verhalten bei gleicher normalisierter `sourceURL` |
|---|---|---|
| `create` | Neue Note, neuen Slug und bei Bedarf neuen Asset-Ordner anlegen | Bestehenden Artikel melden und Erstellung stoppen |
| `update` | Neue belegte Informationen einarbeiten und veraltete Aussagen korrigieren | Bestehenden Artikel als Ziel wiederverwenden |
| `improve` | Fachlichen Kern bewahren; Sprache, Struktur, Metadaten, Quellen, Verbindungen und Bilder verbessern | Bestehenden Artikel als Ziel wiederverwenden |
| `merge` | Mehrere Notes oder Quellen in einem festgelegten Ziel konsolidieren | Bestehenden Artikel als mögliches Ziel wiederverwenden; Quellmaterial erst nach allen Prüfungen löschen |

## Verbindlicher Workflow

1. **Projekt prüfen.** Tatsächliches Schema in `src/types/knowledge.ts`, bestehende Artikel- und Assetkonventionen, verfügbare Projektprüfungen und lokale Änderungen untersuchen.
2. **Modus und Ziel bestimmen.** Nutzerwunsch priorisieren; bei Änderungsmodi den aktuellen Arbeitsbaum als schützenswerte Basis behandeln. Nur bei mehreren gleich plausiblen Zielartikeln nachfragen.
3. **Dubletten und Nähe prüfen.** Projektweit normalisierte URL, Titel, Aliases, Topics und Verbindungen auf exakte sowie semantische Überschneidungen durchsuchen. Eine identische `sourceURL` stoppt nur `create`; bei `update`, `improve` oder `merge` den passenden vorhandenen Artikel weiterverwenden.
4. **Aktive Quellenstrategien laden.** Aus `references/source-playbooks.md` nur Schnellübersicht, gemeinsame Regeln und Abschnitte der tatsächlich vorkommenden Quellentypen lesen und anwenden: X/Twitter, Website/Blog, Docs/PDF, GitHub Repository oder bestehendes Markdown.
5. **Quellen vollständig erfassen.** Text, Metadaten und Medien gemäß den aktiven Quellenstrategien aufnehmen; quellentypspezifische Vollständigkeits-, Autor- und Boilerplate-Grenzen einhalten.
6. **Evidenz inventarisieren.** Intern jede tragende Aussage mit Quelle, Datum/Version, Vertrauensgrad und Konflikt verknüpfen; Medienprovenienz und -rechte ebenfalls erfassen. Übereinstimmungen, Ergänzungen und Widersprüche unterscheiden.
7. **Artikelformat laden.** `references/article-format.md` vollständig lesen und für Schema, Stil, adaptive Synthese, Quellen, Verbindungen, Assets und Visualisierungen befolgen.
8. **Adaptiv entwerfen und revidieren.** Kurze Quellen verständlich kontextualisieren, lange fachlich verdichten und mehrere thematisch synthetisieren; Konflikte sichtbar machen und keine Tatsachen erfinden. Natürliches Deutsch mit Du-Ansprache und echten Umlauten schreiben. Mermaid oder Tabellen nur bei materiellem, belegbarem Erklärwert einsetzen.
9. **Assets rechtebasiert sichern.** Die Assetregeln der Format-Referenz befolgen: Rechte vor dem Download klären und Dateien technisch prüfen, bevor Markdown darauf verweist. Lokale Bilder ausschließlich als absolute Pfade unter `/images/knowledge/<slug>/...` und als `png`, `jpg`/`jpeg`, `gif`, `webp` oder `avif` mit zum Suffix passender echter Dateisignatur referenzieren. SVG wird immer abgelehnt; fachlich und rechtlich verwendbares SVG mit einem vertrauenswürdigen Tool in ein erlaubtes Rasterformat konvertieren und das Raster prüfen, sonst die Quelle verlinken oder beschreiben.
10. **Gebündelten Validator ausführen.** Das Skill-Verzeichnis als Verzeichnis der aktuell geladenen `SKILL.md` auflösen, nicht aus Arbeitsverzeichnis oder Repository erraten. Anschließend vom Projektkontext aus ausführen:

    ```text
    node <resolved-skill-directory>/scripts/validate-knowledge-article.mjs <article.md> --project-root <project-root> --additional-source-count <N>
    ```

    Das Skript liegt unter `scripts/validate-knowledge-article.mjs`; `N` ist die Zahl tatsächlich verwendeter Quellen zusätzlich zu `sourceURL`. Es prüft Frontmatter, Enums, Daten, `readTime`, URL-Dubletten, Bilder/Assets, `## Quellen`, `## Verbindungen` und Mermaid-Grundkonsistenz. Jeden Fehler beheben und erneut ausführen.

    Nur beim `merge` in einen **neuen** Zielartikel darf dessen von noch vorhandenen Quellnotes übernommene `sourceURL` vorübergehend freigegeben werden. Für jede exakt betroffene Quellnote, deren Löschung nach erfolgreichem Gate ausdrücklich erlaubt ist, denselben Aufruf um ein wiederholtes `--allow-duplicate-source <source-note.md>` ergänzen. Diese Option nie bei `create`, `update` oder `improve`, nie pauschal und nie für dritte Dubletten verwenden; jede nicht exakt freigegebene Dublette muss ein Fehler bleiben.
11. **Prüfen.** Die für geänderte Inhalte relevante Projektprüfung beziehungsweise den Build ausführen. Nur Fehler beheben, die durch die aktuellen Artikel- oder Assetänderungen verursacht wurden. Bei vorbestehenden oder sachfremden Fehlern exakten Befehl und Ausgabe als Evidenz bewahren, die Einschränkung melden, keinen fremden Repository-Code ändern und keinen sauberen Prüflauf behaupten.
12. **Erst danach aufräumen.** Nur ausdrücklich freigegebene Quelldateien, redundante Merge-Notes, verwaiste Assets oder temporäre Dateien entfernen. Bei einem Merge mit Duplicate-Allowlist erst nach erfolgreicher Zielvalidierung und Projektprüfung bereinigen, anschließend den Zielartikel ohne `--allow-duplicate-source` erneut erfolgreich validieren. Niemals vorher destruktiv bereinigen.

## Fehler-Gates

- Bei blockierter Primärquelle Fallback und Verifikationsweg festhalten; nur inhaltlich und hinsichtlich Zuordnung gleichwertige Alternativen verwenden. Sonst stoppen oder den Entwurf ausdrücklich als unvollständig kennzeichnen.
- Bei wesentlich unvollständigem X-Thread, unsicherer Autorzuordnung/Reihenfolge, fehlenden aussagetragenden Repo-Dateien oder unklarer Dokumentversion nicht stillschweigend ergänzen.
- Bei nicht auflösbaren Quellenkonflikten widersprüchliche Positionen sichtbar lassen; vor einer entscheidenden Festlegung rückfragen.
- Bei fehlgeschlagenem oder rechtlich ungeklärtem Medium keine lokale Referenz erzeugen. Keine kaputten Bildlinks, nicht referenzierten Assets oder leeren Asset-Ordner hinterlassen.
- Bei `update`, `improve` und `merge` weiterhin richtige Inhalte, manuelle Ergänzungen, Metadaten, Links und relevante Assets bewahren. Unklare Nutzeränderungen nicht überschreiben.
- Erfolg niemals melden, bevor Validator und relevante Prüfung erfolgreich waren. Merge-Bereinigung niemals vor diesen Gates beginnen.
- `--allow-duplicate-source` niemals als allgemeine Dubletten-Ausnahme verwenden; der abschließende Merge-Prüflauf muss nach dem Cleanup ohne Allowlist bestehen.

## Schnellreferenz

| Entscheidung | Regel |
|---|---|
| Eine Quelle | `sourceURL` als Primärquelle; `## Quellen` optional |
| Zusätzliche Quellen | Im Body unter `## Quellen` mit tatsächlicher Belegfunktion aufführen; Validator mit korrektem `N` starten |
| GitHub oder technische Docs | Nur relevante README-, Docs-, Release-, Code- oder Config-Belege prüfen; `sourceType: docs` |
| Bilder | Rechte → erlaubtes Raster mit echter Signatur → absoluter Artikelpfad → Provenienz |
| Merge in neues Ziel | Exakte löschbare Quellnotes allowlisten → validieren → Projekt prüfen → freigegeben bereinigen → ohne Allowlist revalidieren |

## Häufige Fehler

- Bei jeder URL-Dublette abbrechen statt nur bei `create`.
- X-Scrollen mit Thread-Vollständigkeit oder Replies Dritter mit Autorposts verwechseln.
- Website-Bilder ohne Boilerplate-Filter, Inline-Zuordnung, Alt-Text, Rechte oder Provenienz übernehmen.
- Multi-Source-Text entlang der Quellenreihenfolge schreiben oder Konflikte glätten.
- GitHub pauschal zusammenfassen, statt Aussagen an relevante Dateien, Releases, Tags oder Commits zu binden.
- Schema- oder Quellenregeln aus dem Gedächtnis rekonstruieren, statt die beiden Referenzen zu laden.

## Abschlusscheckliste

- [ ] Modus, Ziel sowie exakte und semantische Dubletten geprüft
- [ ] Aktive Quellen vollständig erfasst; Evidenz- und Konfliktinventar erstellt
- [ ] Bestehender manueller Inhalt und lokale Änderungen erhalten
- [ ] Adaptive Synthese ohne erfundene Tatsachen; Quellen und Verbindungen nachvollziehbar
- [ ] Medienrechte, Attribution, Alt-Texte, Dateien und Referenzen geprüft
- [ ] Validator mit korrekter Zusatzquellenzahl erfolgreich
- [ ] Relevante Prüfung oder Build erfolgreich
- [ ] Freigegebene Bereinigung erst danach erfolgt; keine leeren Ordner oder kaputten Links
