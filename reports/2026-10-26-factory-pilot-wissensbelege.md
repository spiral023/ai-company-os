# Atomare Wissensbelege für den semantischen Factory-Pilot

**Stand:** 2026-10-26. **Umfang:** acht eng begrenzte Aussagen aus vier vorhandenen lokalen Referenz-Repos. HEADs und Working-Tree-Status wurden aktuell gelesen; die genannten Code- und Textbereiche wurden mit Zeilennummern geprüft. Keine Upstream-Aktualisierung, Installation, Ausführung fremden Codes oder Laufzeitprüfung.

Die Aussagen belegen die unten beschriebenen Datenstrukturen, Kontrollflüsse oder dokumentierten Arbeitsweisen. Sie belegen keine Wirksamkeit für Philipps Wissensbestand. Die Pilot-Übertragungen sind eigene Vorschläge.

## Herkunftsfamilien

| Familie | Originalquelle und aktueller lokaler HEAD | Working Tree |
|---|---|---|
| `repo:langchain-ai/openwiki` | `external_repos/langchain-ai/openwiki` · `305599f8e44203f9ca6b74bb6b38eebaf0b0405e` | sauber |
| `repo:Graphify-Labs/graphify` | `external_repos/Graphify-Labs/graphify` · `92741d162b2094ffc2fed58cfbd8ee823e9da62c` | zwei unversionierte Verzeichnisse: `tests/fixtures/obj/`, `tests/fixtures/xaml_viewmodel/obj/` |
| `repo:thedotmack/claude-mem` | `external_repos/thedotmack/claude-mem` · `bab040941390f6c1e82c0508ec806f2fc8255cbb` | sauber |
| `repo:open-gsd/gsd-core` | `external_repos/open-gsd/gsd-core` · `7129a135c7271ccea59df7561df83ac11cbc94bd` | sauber |

Ein Original, seine README, ein daraus erzeugter Source-Artikel, dieser Bericht und eine spätere Pilot-Synthese bleiben für die jeweilige Aussage dieselbe Herkunftsfamilie. Beispielsweise zählen B01 und B02 gemeinsam als Belege aus OpenWiki, nicht als zwei unabhängige Bestätigungen. Verschiedene Repo-Namen sind unterschiedliche Ursprungskennungen, aber ohne Untersuchung ihrer Abstammung ebenfalls kein automatischer Nachweis unabhängiger Forschung oder Bestätigung.

## B01 — Ein OpenWiki-Beleg trennt Ressourcenidentität und Version

- **Atomare Aussage:** OpenWiki modelliert einen Beleg mit einer stabilen, vom Resolver verantworteten Ressourcenidentität und einem gesonderten undurchsichtigen Versionstoken.
- **Familie:** `repo:langchain-ai/openwiki`.
- **Aktueller lokaler HEAD:** `305599f8e44203f9ca6b74bb6b38eebaf0b0405e`.
- **Repo-relativer Pfad:** `src/claims/core/types.ts`.
- **Tragender Bereich:** Start **4**, Ende **14**.
- **Original:** [Evidence-Typ, Zeilen 4–14](https://github.com/langchain-ai/openwiki/blob/305599f8e44203f9ca6b74bb6b38eebaf0b0405e/src/claims/core/types.ts#L4-L14).
- **Tatsächlicher Befund:** Das Interface `Evidence` besitzt `resource: string` und `version: string`; die Kommentare weisen Identität und Version dem Resolver zu.
- **Grenze:** Der Typ schreibt weder ein konkretes Hashverfahren noch die Wahrheit einer darauf gestützten Aussage fest. Das ist ein Datenvertrag, keine durch diese Stelle bewiesene Laufzeitgarantie für alle Connectoren.
- **Pilot-Übertragung:** Eine Quelle braucht eine dauerhafte ID und einen konkreten Inhaltsstand. Das Datum eines Syntheseartikels allein genügt nicht als Aktualitätsbeleg.

## B02 — OpenWiki unterscheidet fehlende und veränderte Evidenz

- **Atomare Aussage:** Der Claims-Preflight erzeugt für nicht auflösbare Belege `unresolved` und für geänderte Belegversionen `stale`.
- **Familie:** `repo:langchain-ai/openwiki`.
- **Aktueller lokaler HEAD:** `305599f8e44203f9ca6b74bb6b38eebaf0b0405e`.
- **Repo-relativer Pfad:** `src/claims/brains/code/preflight.ts`.
- **Tragender Bereich:** Start **63**, Ende **96**.
- **Original:** [Auflösung und Klassifizierung, Zeilen 63–96](https://github.com/langchain-ai/openwiki/blob/305599f8e44203f9ca6b74bb6b38eebaf0b0405e/src/claims/brains/code/preflight.ts#L63-L96).
- **Tatsächlicher Befund:** Der Resolver erhält Ressourcen-ID und bisherige Version. Ein fehlendes Ergebnis kommt in `unresolvedResources`; eine abweichende Version in `changedResources`. Die anschließende Verzweigung priorisiert `unresolved` vor `stale`. Fehler außer `EvidenceSecurityError` werden weitergereicht.
- **Grenze:** Die Prüfung erkennt Änderungen oder fehlende Auflösbarkeit. Sie entscheidet nicht, ob die neue Quelle eine Aussage bestätigt oder widerlegt. Ein vorübergehender sonstiger Resolverfehler wird an dieser Stelle nicht als fehlende Quelle ausgegeben.
- **Pilot-Übertragung:** Geänderte Quellen lösen einen Prüfbedarf für abhängige Aussagen aus; ein Quellenfehler darf keine automatische inhaltliche Widerlegung erzeugen.

## B03 — Graphify markiert explizite und aufgelöste Symbolreferenzen unterschiedlich

- **Atomare Aussage:** Graphifys Markdown-Resolver gibt für pfadqualifizierte Symbolverweise `EXTRACTED` und für eindeutig aufgelöste Verweise ohne Pfad `INFERRED` zurück.
- **Familie:** `repo:Graphify-Labs/graphify`.
- **Aktueller lokaler HEAD:** `92741d162b2094ffc2fed58cfbd8ee823e9da62c`.
- **Repo-relativer Pfad:** `graphify/markdown_resolution.py`.
- **Tragender Bereich:** Start **198**, Ende **217**.
- **Original:** [Resolver-Zweig, Zeilen 198–217](https://github.com/Graphify-Labs/graphify/blob/92741d162b2094ffc2fed58cfbd8ee823e9da62c/graphify/markdown_resolution.py#L198-L217).
- **Tatsächlicher Befund:** Ein vorhandener `path` führt zur dateibezogenen Auflösung mit dem Label `EXTRACTED`. Ohne Pfad werden Kandidaten über Namen und Qualifizierer eingeschränkt; nur bei exakt einem Kandidaten wird dessen ID zurückgegeben. Mehrdeutige Treffer liefern `None`. Die Rückgabewerte enthalten fest gesetzte Zahlen `1.0` beziehungsweise `0.95`.
- **Grenze:** Auch der hier `INFERRED` genannte Zweig ist deterministischer Resolver-Code; das Label bedeutet an dieser Stelle keine LLM-Synthese. Die festen Zahlen sind kein Beleg einer kalibrierten Erfolgswahrscheinlichkeit.
- **Pilot-Übertragung:** Herkunft einer Beziehung getrennt ausweisen: explizit im Original, deterministisch aufgelöst oder semantisch vorgeschlagen. Ein bloßes Konfidenzlabel ersetzt diese Unterscheidung nicht.

## B04 — Graphify trennt AST- und semantische Cachebereiche

- **Atomare Aussage:** Graphify legt AST-Cacheeinträge in einem Versions-/Schema-/Grammar-Namespace ab und kann semantische Cacheeinträge zusätzlich nach Promptfingerprint unterscheiden.
- **Familie:** `repo:Graphify-Labs/graphify`.
- **Aktueller lokaler HEAD:** `92741d162b2094ffc2fed58cfbd8ee823e9da62c`.
- **Repo-relativer Pfad:** `graphify/cache.py`.
- **Tragender Bereich:** Start **1016**, Ende **1045**.
- **Original:** [Cacheverzeichnisse, Zeilen 1016–1045](https://github.com/Graphify-Labs/graphify/blob/92741d162b2094ffc2fed58cfbd8ee823e9da62c/graphify/cache.py#L1016-L1045).
- **Tatsächlicher Befund:** Für `kind == "ast"` wird ein Unterverzeichnis mit `_EXTRACTOR_VERSION`, `_AST_CACHE_SCHEMA` und `_grammar_fingerprint()` angehängt. Bei einem anderen Kind wird nur dann `p{prompt_fp}` angehängt, wenn `prompt_fp` übergeben wurde. `ast`, `semantic` und etwa `semantic-deep` bilden getrennte Bereiche.
- **Grenze:** Die Stelle beweist nicht, dass jeder Aufrufer einen Promptfingerprint übergibt. Ohne diesen Parameter bleibt das historische flache Layout möglich. Ein Cachetreffer belegt Wiederverwendbarkeit nach dem Schlüssel, keine fachliche Richtigkeit der Extraktion.
- **Pilot-Übertragung:** Semantische Ableitungen mindestens an Quellstand, Extraktionsschema und Promptversion binden. Deterministisch extrahierte Struktur getrennt von Modellableitungen speichern.

## B05 — Claude-Mem implementiert Suche, Kontextauswahl und Detailabruf als getrennte Schritte

- **Atomare Aussage:** Der hier geprüfte progressive Suchpfad lädt Details erst nach einer Suche und einer Auswahl aus dem Timeline-Kontext nach.
- **Familie:** `repo:thedotmack/claude-mem`.
- **Aktueller lokaler HEAD:** `bab040941390f6c1e82c0508ec806f2fc8255cbb`.
- **Repo-relativer Pfad:** `src/shared/progressive-search.ts`.
- **Tragender Bereich:** Start **205**, Ende **227**.
- **Original:** [Suchfolge, Zeilen 205–227](https://github.com/thedotmack/claude-mem/blob/bab040941390f6c1e82c0508ec806f2fc8255cbb/src/shared/progressive-search.ts#L205-L227).
- **Tatsächlicher Befund:** Auf `backend.search` folgen Kandidatenauswahl, gegebenenfalls eine begrenzte Query-Verfeinerung, `this.context`, erneute Auswahl und `this.details`. `trace` protokolliert die Operationen `search`, `timeline` und `fetch`. Bei fehlenden Kandidaten oder fehlendem Kontext wird vor dem Detailabruf zurückgegeben.
- **Grenze:** Das ist der ausdrücklich einfache Suchpfad; seine Auswahl ist kein Nachweis semantischer Gesamtsynthese. Die Stelle zeigt außerdem keinen vollständigen oder ausgewogenen Abruf aller relevanten Wissenspositionen.
- **Pilot-Übertragung:** Erst Fundstellen liefern, dann angrenzenden Kontext und ausgewählte Originalabschnitte nachladen. Ein Gesamtreview benötigt zusätzlich eine explizite Abdeckungsstrategie jenseits dieser Trefferfolge.

## B06 — Claude-Mem begrenzt progressive Antworten und macht Kürzungen sichtbar

- **Atomare Aussage:** Claude-Mems progressive Ergebnisfunktion entfernt oder kürzt Inhalte, solange das serialisierte Ergebnis sein Bytebudget überschreitet.
- **Familie:** `repo:thedotmack/claude-mem`.
- **Aktueller lokaler HEAD:** `bab040941390f6c1e82c0508ec806f2fc8255cbb`.
- **Repo-relativer Pfad:** `src/shared/progressive-search.ts`.
- **Tragender Bereich:** Start **150**, Ende **167**.
- **Original:** [Antwortbegrenzung, Zeilen 150–167](https://github.com/thedotmack/claude-mem/blob/bab040941390f6c1e82c0508ec806f2fc8255cbb/src/shared/progressive-search.ts#L150-L167).
- **Tatsächlicher Befund:** Die Funktion prüft die UTF-8-Länge der JSON-Antwort. Ohne Beobachtungsdetails entfernt sie überzählige Indexeinträge und setzt `index_truncated`; andernfalls halbiert sie den größten Detailtext und setzt dessen `truncated` auf `true`. Ist keine weitere Kürzung möglich, entsteht `response_too_large`.
- **Grenze:** Das Budget erzwingt keine semantisch verlustfreie Kompression. Eine begrenzte Antwort darf deshalb nicht als vollständige Betrachtung des Bestands ausgegeben werden.
- **Pilot-Übertragung:** Begrenzungen, ausgelassene Quellen und nötige Fortsetzungsschritte im Ergebnisvertrag ausdrücklich ausweisen.

## B07 — GSD dokumentiert die Rekonstruktion fehlenden Arbeitsstatus aus Artefakten

- **Atomare Aussage:** Der GSD-Resume-Workflow sieht vor, eine fehlende `STATE.md` aus vorhandenen Projekt-, Roadmap-, Summary-, Todo- und Fortsetzungsartefakten zu rekonstruieren.
- **Familie:** `repo:open-gsd/gsd-core`.
- **Aktueller lokaler HEAD:** `7129a135c7271ccea59df7561df83ac11cbc94bd`.
- **Repo-relativer Pfad:** `gsd-core/workflows/resume-project.md`.
- **Tragender Bereich:** Start **322**, Ende **333**.
- **Original:** [Rekonstruktionsanweisung, Zeilen 322–333](https://github.com/open-gsd/gsd-core/blob/7129a135c7271ccea59df7561df83ac11cbc94bd/gsd-core/workflows/resume-project.md#L322-L333).
- **Tatsächlicher Befund:** Der Workflow benennt `PROJECT.md` für Ziel und Kernwert, `ROADMAP.md` für Phasen und Position, `*-SUMMARY.md` für Entscheidungen und Bedenken, offene Todos und `.continue-here` für Fortsetzungskontext. Danach soll der Status neu geschrieben werden.
- **Grenze:** Das ist eine Agent-Arbeitsanweisung, kein an dieser Stelle implementierter deterministischer Rekonstruktionsalgorithmus. Sie kann nur vorhandene Artefakte auswerten und belegt nicht, dass unausgesprochene Entscheidungen wiederherstellbar sind.
- **Pilot-Übertragung:** Technischen Inventar- und Arbeitsstatus aus beobachtbaren Artefakten ableiten. Fehlende inhaltliche Entscheidungen als fehlend markieren, nicht aus Dateistruktur erfinden.

## B08 — GSD trennt eine aktuelle Entscheidungszusammenfassung vom vollständigen Entscheidungslog

- **Atomare Aussage:** GSDs `STATE.md`-Referenz beschreibt den Decisions-Bereich als Zusammenfassung aktueller relevanter Entscheidungen und verweist für den vollständigen Log auf `PROJECT.md`.
- **Familie:** `repo:open-gsd/gsd-core`.
- **Aktueller lokaler HEAD:** `7129a135c7271ccea59df7561df83ac11cbc94bd`.
- **Repo-relativer Pfad:** `docs/reference/state-md.md`.
- **Tragender Bereich:** Start **230**, Ende **236**.
- **Original:** [Accumulated Context, Zeilen 230–236](https://github.com/open-gsd/gsd-core/blob/7129a135c7271ccea59df7561df83ac11cbc94bd/docs/reference/state-md.md#L230-L236).
- **Tatsächlicher Befund:** Die Referenz weist dem aktuellen Status eine Entscheidungszusammenfassung zu und nennt `gsd-tools state add-decision` als Eintragsweg. Offene Todos und Blocker werden daneben als eigene Kontextelemente beschrieben.
- **Grenze:** Die Dokumentation belegt diese vorgesehene Aufgabenteilung. Sie beweist nicht die Vollständigkeit tatsächlich gepflegter Logs und macht keine Aussage, dass jede Entscheidung menschlich geprüft sei. „Kuratierte Entscheidungen“ ist deshalb unsere vorgeschlagene Qualitätseigenschaft, keine hier automatisch belegte Produkteigenschaft.
- **Pilot-Übertragung:** Ein rekonstruierbarer Status-/Katalogstand und ein bewusst gepflegter Entscheidungsbestand brauchen getrennte Zuständigkeiten. Eine gekürzte Laufzeitansicht darf auf den vollständigen Entscheidungsbeleg zurückführen.

## Konsolidierung für den Pilot

Die acht Aussagen ergeben vier Herkunftsfamilien und keine acht unabhängigen Bestätigungen. Die eigene Synthese daraus lautet: Quellidentität und Inhaltsstand trennen; Änderungen und Unauflösbarkeit unterscheiden; deterministische Struktur, deterministische Ableitung und semantischen Vorschlag sichtbar halten; Treffer erst nach Auswahl vertiefen; gekürzte Antworten als gekürzt kennzeichnen; rekonstruierbaren Zustand von bewusst gepflegten Entscheidungen unterscheiden.

Diese Synthese bleibt eine aus den genannten Quellen abgeleitete Architekturhypothese. Der Pilot muss gesondert messen, ob sie bessere fachübergreifende Antworten und belastbarere Methodenauswahl ermöglicht.

## Ausgeführte Prüfung

- Aktuelle lokale HEADs und `git status --short` der vier genannten Kopien gelesen.
- Alle acht tragenden Bereiche mit nummerierten Originalzeilen geprüft.
- Ausschließlich diesen Bericht neu angelegt; keine Originaldateien, Registry oder sonstigen Dateien geändert.
- Keine fremden Programme ausgeführt, keine Installationen oder Pulls, keine repo-weiten Validatoren, keine Commits oder Veröffentlichungen.
