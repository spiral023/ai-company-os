# Quellenstrategien

Lies nur den Abschnitt für den erkannten Quellentyp. Erfasse vor dem Schreiben eine interne Evidenzliste aus Aussage, Quelle, Datum, Vertrauensgrad und Konflikten. Verfügbare Werkzeuge werden nach Fähigkeit gewählt, nicht nach Produktname.

## Schnellübersicht

| Quelle | Zuerst prüfen | Bevorzugter Zugriff | Typischer Fallback | Vollständig, wenn |
|---|---|---|---|---|
| X/Twitter | Einzelpost oder Thread, Autor, Post-ID, Antworten | Browser mit sichtbarem Verlauf, Scrollen und Snapshots | Websuche plus verifizierbarer Mirror, Repost oder Autorquelle | Alle relevanten Autorposts und Medien in Reihenfolge erfasst sind |
| Website/Blog | Canonical URL, Autor, Datum, Seitenumfang | Browser-Leseansicht oder strukturierte Webextraktion | Websuche, Cache/Archiv oder Druckansicht | Hauptinhalt, Code, Diagramme und nötige Unterseiten abgedeckt sind |
| Docs/PDF | Version, Ausgabe, Seiten/Navigation | Dokumentationsseiten; PDF-Text plus Seitenrendering | Download, Repository-Datei oder offizielle Spiegelquelle | Relevante Kapitel, Version und visuelle Inhalte geprüft sind |
| GitHub Repository | Default Branch, Tag/Release, Lizenz, Status | Repository-Webansicht, API oder CLI | Raw-Dateien, Release-Artefakte oder offizielle Docs | README, gezielte Docs/Releases und aussagetragende Dateien geprüft sind |
| Bestehendes Markdown | Frontmatter, Body, Assets, lokale Änderungen | Direkter Dateizugriff und projektweite Suche | Versionshistorie nur zur Klärung | Schützenswerte Inhalte, Links, Quellen und Assets inventarisiert sind |

Tracking-Parameter für Dublettenvergleiche entfernen, die belegte Canonical URL aber als `sourceURL` erhalten. Zeitabhängige Aussagen stets aktuell verifizieren.

Vor jedem lokalen Kopieren eines Mediums Lizenz oder ausdrückliche Nutzungserlaubnis sowie Attributionspflichten prüfen. In der Evidenzliste Urheber, originale Medien-URL, Lizenz und – sofern vorhanden – Lizenz-URL festhalten. Verlangt die Lizenz Attribution, muss der veröffentlichte Artikel direkt in der Bildunterschrift oder in einem expliziten `## Quellen`-Eintrag sichtbar Urheber, Original-Asset-URL, Lizenzname mit Lizenzlink und Änderungsstatus (`unverändert` oder `bearbeitet`, gegebenenfalls mit Art der Bearbeitung) nennen. Die interne Evidenzliste allein genügt nicht. Sind Rechte oder Pflichten unklar, das Medium nicht kopieren; stattdessen zur Quelle verlinken oder den relevanten Inhalt beschreiben. SVG niemals lokal referenzieren: Ist es fachlich und rechtlich verwendbar, mit einem vertrauenswürdigen Tool in ein erlaubtes Rasterformat konvertieren und das Raster prüfen; andernfalls die Quelle verlinken oder den Inhalt beschreiben.

## X/Twitter

- **Prüfen:** URL/Post-ID, sichtbarer Autor, Zeitstempel, Kennzeichnung als Einzelpost oder Thread sowie eingebettete Zitate. Posts des Thread-Autors bilden den Primärthread; Replies Dritter sind Zusatzquellen und dürfen nicht still als Teil des Threads erscheinen.
- **Bevorzugter Zugriff:** Im Browser den Ausgangspost öffnen, Lazy Loading durch schrittweises Scrollen auslösen und vor, während sowie nach dem Scrollen Snapshots erfassen. Autor, Post-ID und Reihenfolge jedes relevanten Autorposts protokollieren.
- **Fallback:** Bei Login-Wall, Rate Limit oder unvollständiger Darstellung per Websuche nach Post-ID, markanten Textpassagen und Autor suchen. Thread-Reader, Reposts oder Blogfassungen nur übernehmen, wenn Autorzuordnung, Reihenfolge und wesentliche Formulierungen mit mindestens einem unabhängigen Signal oder einer Autorquelle übereinstimmen.
- **Vollständigkeit:** Anfang und erkennbares Ende des Threads, alle dazwischenliegenden Autorposts sowie „show more“-Inhalte prüfen. Lücken, gelöschte Posts und nicht ladbare Teile ausdrücklich vermerken; Replies nur einbeziehen, wenn sie fachlich relevant sind, und als solche kennzeichnen.
- **Medien:** Bilder, Videos, GIF-Poster und verlinkte Diagramme pro Autorpost in sichtbarer Originalreihenfolge inventarisieren. Nur redaktionell relevante Medien speichern; Bildtext und fachlichen Kontext im Alt-Text abbilden. Bei Video ohne speicherbares Original keine unbelegte Transkription erfinden.
- **Provenienz/Konflikte:** Primär-URL bleibt maßgeblich. Fallback-URL und Verifikationsweg in der Evidenzliste halten und bei tatsächlicher Nutzung unter `## Quellen` nennen. Widersprüche zwischen Original, Repost und Replies sichtbar machen.
- **Abbruchbedingungen:** Stoppe vor dem Speichern, wenn die Autorzuordnung unsicher, der Thread wesentlich unvollständig oder die Reihenfolge nicht rekonstruierbar ist. Frage nach oder kennzeichne den Entwurf als unvollständig; behaupte keine Vollständigkeit aufgrund eines einzelnen Mirrors.

## Website/Blog

- **Prüfen:** Canonical URL, Titel, Byline, Veröffentlichungs- und Aktualisierungsdatum, Sprache, Inhaltsverzeichnis, Pagination sowie relevante ausgehende Primärquellen.
- **Bevorzugter Zugriff:** Hauptinhalt semantisch über Browser oder Webextraktion erfassen. Überschriftenhierarchie, Absätze, Listen, Blockquotes, Tabellen, Codeblöcke, Captions und fachlich relevante Bilder erhalten; Navigation, Footer, Cookie-UI, Werbung, Empfehlungen und Newsletter-Boilerplate verwerfen.
- **Fallback:** Lese-/Druckansicht, strukturierte Metadaten, Websuche, Cache/Archiv oder eine vom Autor bereitgestellte Parallelfassung verwenden. Bei mehrseitigen Artikeln nur notwendige Folgeseiten gezielt öffnen.
- **Vollständigkeit:** Einleitung bis Fazit prüfen und eingeklappte Abschnitte laden. Code nicht aus gekürzten Previews rekonstruieren. Diagramm-Aussagen mit Caption und umliegendem Text abgleichen.
- **Medien:** Fachlich erklärende Screenshots, Diagramme und Code-Grafiken sichern; dekorative Hero-Bilder nur bei echtem Kontextwert. Wenn Code als Text verfügbar ist, Text statt Screenshot bevorzugen. Medien in fachlich sinnvoller Originalreihenfolge platzieren.
- **Provenienz/Konflikte:** Aktualisierungsdatum und Versionsbezug festhalten. Behauptungen aus verlinkten Quellen der tatsächlich tragenden Quelle zuordnen; Konflikte zwischen Artikeltext und Primärbeleg benennen.
- **Abbruchbedingungen:** Stoppe, wenn nur Teaser/Paywall sichtbar ist, zentrale Seiten fehlen oder Autor/Datum für eine zeitkritische Aussage nicht verifizierbar sind. Fehlende Passagen nicht aus Such-Snippets ergänzen.

## Docs/PDF

- **Prüfen:** Produkt/Projekt, Dokumentversion, Versionsumschalter, Veröffentlichungsstand, Canonical URL beziehungsweise PDF-Ausgabe sowie relevante Kapitel oder Seiten.
- **Bevorzugter Zugriff:** HTML-Dokumentation über Navigation und gezielte Seiten erfassen. PDFs zuerst als Text auslesen und Seiten mit Tabellen, Diagrammen, Formeln oder auffälligen Layouts zusätzlich rendern und visuell prüfen.
- **Fallback:** Offiziellen Download, Raw-Datei, Repository-Dokumentation, frühere offizielle Version oder Websuche zur Fundstelle nutzen. OCR-Ergebnisse nur nach Sichtprüfung übernehmen.
- **Vollständigkeit:** Nur die für das Thema nötigen Kapitel einbeziehen, dabei Voraussetzungen, Warnungen, Beispiele und Versionsgrenzen nicht abschneiden. Seiten- oder Abschnittsangaben für präzisionskritische Aussagen notieren.
- **Medien:** Erklärende Diagramme und Tabellen mit lesbarer Auflösung sichern. Texttabellen möglichst semantisch nachbauen, sofern Struktur und Werte eindeutig sind; Screenshots nicht als Ersatz für zugänglichen Text verwenden.
- **Provenienz/Konflikte:** Version und Abrufkontext nennen. Neuere und ältere Dokumentation nicht vermischen; Abweichungen zu Release Notes oder Code als versionsabhängigen Konflikt behandeln. `sourceType` ist `docs`.
- **Abbruchbedingungen:** Stoppe, wenn Version oder Seitenzuordnung unklar ist, OCR zentrale Werte nicht zuverlässig erkennt oder benötigte Kapitel fehlen. Keine API-Signaturen aus einer anderen Version einsetzen.

## GitHub Repository

- **Prüfen:** Repository-Eigentümer, Default Branch, relevanter Tag/Commit/Release, letzte Aktivität, Archivierungsstatus, Lizenz und Links zu offiziellen Docs. Forks und Mirrors eindeutig kennzeichnen.
- **Bevorzugter Zugriff:** Repository-Webansicht, GitHub-kompatible API oder CLI nutzen. Zuerst README, dann gezielt `docs/`, Releases und nur jene Source-, Config- oder Beispiel-Dateien lesen, die konkrete Aussagen tragen.
- **Fallback:** Raw-Dateien, Release-Artefakte, Paketregistry oder offizielle Projektdokumentation heranziehen. Wenn dynamische Ansichten fehlen, einzelne bekannte Pfade statt eines ungezielten Vollimports abrufen.
- **Vollständigkeit:** Architektur, Installation, zentrale APIs, typische Anwendung und Grenzen nur behandeln, wenn sie für das Thema relevant und belegt sind. Keine blinde Vollrepo-Zusammenfassung. Behauptungen möglichst an Tag-, Commit- oder Release-Stand binden und für stabile Belege Permalinks verwenden.
- **Medien:** Erklärende README-/Docs-Diagramme und Screenshots sichern; Badges, Avatare und Logos ohne Erklärwert auslassen. Relative Medienpfade gegen den belegten Ref auflösen.
- **Provenienz/Konflikte:** README, Docs, Releases und Code können auseinanderlaufen. Im Konflikt den jeweiligen Stand nennen, ausführbaren Code nicht automatisch als dokumentierte öffentliche API behandeln und Lizenz-/Projektstatus nur aufnehmen, wenn relevant. `sourceType` ist `docs`.
- **Abbruchbedingungen:** Stoppe, wenn private/fehlende Dateien eine Kernaussage verhindern, der relevante Ref unbekannt ist oder Lizenz beziehungsweise Status nicht zuverlässig feststellbar sind. Keine Schlüsse aus Dateinamen allein ziehen.

## Bestehendes Markdown

- **Prüfen:** Frontmatter, kompletter Body, `## Quellen`, `## Verbindungen`, Wikilinks, lokale Bilder, Asset-Ordner, eingebettete Code-/Mermaid-Blöcke und erkennbare manuelle Ergänzungen. Zielmodus (`update`, `improve`, `merge`) explizit festhalten.
- **Bevorzugter Zugriff:** Datei direkt lesen und projektweit nach `sourceURL`, Titel, Aliases, Topics und Verbindungen suchen. Verlinkte Assets auf Existenz und tatsächliche Nutzung prüfen.
- **Fallback:** Versionshistorie oder verwandte Artikel nur zur Herkunfts- und Konfliktklärung heranziehen; der aktuelle Arbeitsbaum bleibt die schützenswerte Ausgangsbasis.
- **Vollständigkeit:** Vor Änderungen ein Inventar aus belegten Aussagen, Eigenanteilen, Metadaten, Quellen, Links und Assets bilden. Bei Merge alle Quellartikel vollständig prüfen, nicht nur Frontmatter oder Diff.
- **Medien:** Vorhandene relevante Assets und ihre Reihenfolge erhalten. Umbenennen oder verschieben nur mit aktualisierten Referenzen; verwaiste Assets erst nach erfolgreicher Zielvalidierung entfernen.
- **Provenienz/Konflikte:** Lokale Ergänzungen nicht einer Webquelle zuschreiben. Neue Belege den passenden Aussagen zuordnen, widersprüchliche Fassungen offen zusammenführen und `sourceURL` auf die Primärquelle des Zielartikels beschränken.
- **Abbruchbedingungen:** Stoppe bei unklarer Zielversion, nicht auflösbaren Nutzeränderungen oder destruktiven Merge-Schritten vor erfolgreicher Validierung. Keine Quelldatei und kein Asset allein wegen vermeintlicher Redundanz löschen.
