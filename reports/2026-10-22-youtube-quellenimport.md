# YouTube-Quellenlauf und Abrufdiagnose vom 22.10.2026

## Ergebnis

Neun übergebene URLs entsprechen neun eindeutigen Video-IDs. Acht Videos wurden neu archiviert und verarbeitet; das Lanz-und-Precht-Video `sFxhYEmaamA` war bereits verarbeitet und blieb unverändert. Nach dem Lauf gibt es keine offenen Inbox-Quellen mehr: 383 verarbeitet, 47 begründet ignoriert.

Es entstanden acht deutsche Source-Notizen und zwei Patterns: [[Mutationstests-fuer-Agent-geschriebene-Tests]] sowie [[Pruefungen-nach-Feedbackzeitpunkt-staffeln]]. 17 Belegzeilen ergänzen bestehende Patterns; die neuen Patterns enthalten je einen eigenen Beleg. Sieben datierte Spannungen halten Grenzen und Gegenpositionen fest. Keine neuen Faktenregisterzeilen: qualitative Empfehlungen, Prognosen und ungeprüfte Vorfallsberichte werden nicht zu Messdaten umgedeutet.

| Video | Originaldatum | Untertitelsegmente | Letzte Zeitmarke | Archiv und Ausarbeitung |
|---|---|---|---|---|
| [A0scuiiGBC4](https://www.youtube.com/watch?v=A0scuiiGBC4) | 2026-07-17 | 50 | 1:28 | [Rohquelle](../00_Inbox/Quellen/YouTube/2026-07-17-matt-pocock-kill-your-memory-md.md) / [Source](../80_Knowledge/Sources/2026-07-17-matt-pocock-kill-your-memory-md.md) |
| [btUxMt_tssA](https://www.youtube.com/watch?v=btUxMt_tssA) | 2026-10-18 | 724 | 23:21 | [Rohquelle](../00_Inbox/Quellen/YouTube/2026-10-18-ai-news-strategy-daily-n-what-really-happens-when-ai-agents-meet-in-the-w.md) / [Source](../80_Knowledge/Sources/2026-10-18-ai-news-strategy-daily-n-what-really-happens-when-ai-agents-meet-in-the-w.md) |
| [djSbndoByr8](https://www.youtube.com/watch?v=djSbndoByr8) | 2026-10-14 | 34 | 0:57 | [Rohquelle](../00_Inbox/Quellen/YouTube/2026-10-14-matt-pocock-mutation-testing-is-awesome.md) / [Source](../80_Knowledge/Sources/2026-10-14-matt-pocock-mutation-testing-is-awesome.md) |
| [DN7bHOVmE88](https://www.youtube.com/watch?v=DN7bHOVmE88) | 2026-10-20 | 363 | 10:25 | [Rohquelle](../00_Inbox/Quellen/YouTube/2026-10-20-alex-sprogis-hoer-auf-software-abos-zu-kaufen.md) / [Source](../80_Knowledge/Sources/2026-10-20-alex-sprogis-hoer-auf-software-abos-zu-kaufen.md) |
| [zgy8_ApYNDk](https://www.youtube.com/watch?v=zgy8_ApYNDk) | 2026-10-13 | 49 | 1:29 | [Rohquelle](../00_Inbox/Quellen/YouTube/2026-10-13-matt-pocock-stop-running-your-checks-in-harness-hooks.md) / [Source](../80_Knowledge/Sources/2026-10-13-matt-pocock-stop-running-your-checks-in-harness-hooks.md) |
| [eEjBhVI9Qok](https://www.youtube.com/watch?v=eEjBhVI9Qok) | 2026-07-16 | 69 | 2:10 | [Rohquelle](../00_Inbox/Quellen/YouTube/2026-07-16-matt-pocock-do-software-fundamentals-still-matter.md) / [Source](../80_Knowledge/Sources/2026-07-16-matt-pocock-do-software-fundamentals-still-matter.md) |
| [Yn8h5Ip-L9c](https://www.youtube.com/watch?v=Yn8h5Ip-L9c) | 2026-07-20 | 76 | 1:57 | [Rohquelle](../00_Inbox/Quellen/YouTube/2026-07-20-matt-pocock-do-you-even-need-human-review.md) / [Source](../80_Knowledge/Sources/2026-07-20-matt-pocock-do-you-even-need-human-review.md) |
| [W4m_8ovS0RY](https://www.youtube.com/watch?v=W4m_8ovS0RY) | 2026-10-16 | 648 | 18:21 | [Rohquelle](../00_Inbox/Quellen/YouTube/2026-10-16-niklas-steenfatt-vibe-coding-hat-sich-veraendert.md) / [Source](../80_Knowledge/Sources/2026-10-16-niklas-steenfatt-vibe-coding-hat-sich-veraendert.md) |

Bereits vorhanden: [Lanz + Precht](../80_Knowledge/Sources/2026-10-02-zdfheute-nachrichten-videopodcast-droht-die-ki-apokalypse-lanz-precht.md), veröffentlicht am 02.10.2026. Der angefragte Einstieg bei `W4m_8ovS0RY` bleibt als 963 Sekunden dokumentiert; verarbeitet wurde das ganze Untertitelarchiv. Tracking-, Playlist- und Startparameter erzeugen keine zusätzlichen Quellen.

## Was den Abruf tatsächlich blockiert hat

Der Standardweg `python ai.py ingest <URL>` scheiterte bei allen acht neuen IDs mit `RequestBlocked`. Auch die erste Anfrage war bereits blockiert. Ein isolierter Abruf der Originalseite lieferte zwar HTTP 200, im Player aber `LOGIN_REQUIRED` und ausdrücklich den Bot-Hinweis. Titel und Kanal waren weiterhin über oEmbed lesbar. Fehlende Player-Metadaten bedeuteten deshalb hier weder ein kaputtes Datumsparsing noch nachweislich fehlende Untertitel.

Eine reine, alle Clients betreffende IP-Sperre ist damit nicht bewiesen. Nachgewiesen ist eine Bot-/Zugriffsabfrage für die direkten anonymen Clients. Ob IP-Reputation, Session, Client-Erkennung oder deren Kombination den Ausschlag gab, lässt sich aus YouTubes Antwort nicht bestimmen. In der lokalen Python-Konfiguration war kein Systemproxy hinterlegt; die öffentliche IP und Browser-Cookies wurden nicht protokolliert.

Die [YouTube-Hilfe](https://support.google.com/youtube/answer/3037019) beschreibt Einschränkungen für nicht angemeldete Zugriffe. Die [Dokumentation von youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api#working-around-ip-bans-requestblocked-or-ipblocked-exception) nennt insbesondere Cloud-IP-Adressen und hohe Abrufmengen als mögliche Auslöser und weist auf die undokumentierte Schnittstelle hin. Diese allgemeinen Ursachen beweisen nicht, welche davon in diesem Lauf zutraf.

## Gezielte Vergleichstests

| Hypothese | Beobachtung | Schluss |
|---|---|---|
| Falsche URL oder Trackingparameter | Kanonische IDs, gleicher Fehler bei acht unterschiedlichen Videos | Kein Hinweis auf einen Fehler der übergebenen URLs |
| Veraltete Transkriptbibliothek | Installiert und auf PyPI aktuell: `youtube-transcript-api 1.2.4` | Kein verfügbares Update als unmittelbare Lösung |
| Veralteter Audio-Downloader | Installiert war `yt-dlp 2026.8.19`; isolierter Test mit `2026.10.21` und `yt-dlp-ejs 0.8.0` erhielt dieselbe Bot-Abfrage | Aktualisierung sinnvoll, beseitigt diesen Fehler aber nicht |
| Fehlende JavaScript-Laufzeit | Aktueller Vergleichstest erkannte `node-24.20.0` und den Node-Challenge-Provider | Fehlende Runtime erklärt die weiterhin vorhandene Bot-Abfrage nicht |
| Fehler im Datumsparser | Bestehender und alternativer JSON-Parser lesen dieselbe eingeschränkte Playerantwort ohne Video-Metadaten | Hier kein nachgewiesener Parserfehler |
| Bereits vorhandener Browserzugang | Alle acht Transkripte ließen sich im verbundenen normalen Chrome exportieren | Funktionierender alternativer Erfassungsweg |

Ein direkter `yt-dlp`-CLI-Test ohne Runtime-Aktivierung hatte zunächst eine zusätzliche Warnung erzeugt. Der vorhandene lokale Audio-Workflow aktiviert Node und Deno bereits; der kontrollierte aktuelle Test aktivierte Node ausdrücklich. Die [EJS-Anleitung](https://github.com/yt-dlp/yt-dlp/wiki/EJS) verlangt die passende Runtime und Solver-Komponente. Veraltete Werkzeugstände wurden somit geprüft, aber nicht vorschnell zur alleinigen Ursache erklärt.

Die optionale lokale Transkriptionsumgebung wurde anschließend auf `yt-dlp[default]==2026.10.21` aktualisiert und die Installationsanleitung nachgezogen. Die globale Python-Umgebung wurde nicht verändert. [Offizielles Release](https://github.com/yt-dlp/yt-dlp/releases/tag/2026.10.21).

## Funktionierender Erfassungsweg und seine Grenzen

Nach erfolglosem Standardabruf wurde jedes Originalvideo im bereits verbundenen Chrome geöffnet. Das konkrete Veröffentlichungsdatum stammt aus der aufgeklappten Beschreibung. Der integrierte Browserexport schrieb UTF-8-Dateien mit Video-ID, Sprache, Erzeugungskennzeichnung und Zeitmarken. Diese liegen unverändert in den typgleichen Medienordnern; die Rohnotizen enthalten daraus lesbare Absätze und einen Link zum Export. Beschreibungstexte stammen aus der sichtbaren Oberfläche, mit normalisierten Abständen und teilweise von YouTube verkürzt angezeigten Links. Verkürzte Zieladressen wurden nicht geraten.

Sechs Exporte verwenden deutsche automatisch erzeugte Spuren ursprünglich englischer Videos mit automatischer Synchronisation. Sie sind als mögliche Übersetzungs-/ASR-Fassung markiert, nicht als wortgetreues englisches Original. Die englische Memory-Spur wurde zusätzlich im sichtbaren Transkript gegengelesen. Es fand keine vollständige Hör- oder Bildprüfung aller Videos statt. Es wurden keine Sitzungscookies exportiert, keine CAPTCHAs gelöst und keine kostenpflichtigen Abrufdienste eingerichtet. Details des wiederholbaren Vorgehens stehen in [der Quellen-README](../00_Inbox/Quellen/README.md).

## Eigener Fehler und Korrektur

`ingest_source.py` fasste bislang jeden Abruffehler als fehlendes Transkript zusammen. Das war irreführend. Der Import unterscheidet jetzt `RequestBlocked` einschließlich `IpBlocked` von `TranscriptsDisabled` und sonstigen Abruffehlern. Bei einer Blockade sagt er ausdrücklich, dass die Untertitelverfügbarkeit nicht feststellbar ist, und verweist auf den Browserweg. Drei Regressionstests reproduzierten die falsche Einstufung zunächst und bestehen nach der Korrektur. Die acht schnellen ersten Batch-Versuche werden nicht als sinnvolle Retry-Strategie übernommen; bei bekannter Blockade sollen weitere automatische Aufrufe anhalten.

## Inhaltliche Einordnung

- Auto-Memory: Pococks Ablehnung ungeprüft gesammelter Präferenzen unterscheidet sich von bewusst gepflegten Repo-Regeln; kein pauschaler Löschauftrag.
- Tests: Mutation Testing prüft die Tests selbst. Überlebende Mutanten bleiben fachlich zu bewerten; ein Score allein ist kein Qualitätsnachweis.
- Feedback: Kurze Pre-Commit-Checks und umfangreiche CI betreffen den Zeitpunkt. Die Drei-Sekunden-Angabe bleibt eine Autorenheuristik aus der automatischen Spur.
- Review: Kleine Diffs beweisen kein kleines Risiko; die Wahl menschlicher Kontrollpunkte ersetzt keine Produktionsfreigabe.
- Sprogis: Product Brief, Design-Prototyp, Feature-Spezifikation und Prüfung sind getrennte Entscheidungen. Die Demo belegt keine allgemeine Abo- oder Kostenersparnis.
- Steenfatt: Der Primärabgleich des [AGENTS.md-Papiers](https://arxiv.org/abs/2602.11988) und des [Anthropic-Beitrags](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) begrenzt pauschale Aussagen über überflüssigen Kontext oder sichere Modelle.
- Jones: Laborberichte, Beobachtungen, persönliche Gespräche und Prognosen bleiben getrennt. Für das konkret skizzierte Szenario einer Agent-zu-Agent-Vergiftung nennt der Autor selbst keine dokumentierten Fälle.

## Prüfung und Git-Abgrenzung

- Vier erwartete und vier übernommene Reports; acht von acht neuen Quellen verarbeitet.
- Quellenpipeline konsistent, keine offenen Quellen.
- Acht Sources und zwei neue Patterns mit fachlich nachgeschärften Themenkeywords; beide Patterns zusätzlich mit Synonymen. Themenhubs regeneriert.
- 73 Tests für Quellenimport und lokale Transkriptergänzung bestanden; Python-Syntaxprüfung bestanden.
- Knowledge-Validator: exakt dieselben 53 vorbestehenden Fehler, keine neuen Fehler.
- Company-OS-Healthcheck: OK. Zwei neue Patterns separat geprüft, ohne erhebliche Befunde.
- Die vorhandenen Motion-, Video- und Berichtsvorarbeiten bleiben außerhalb dieses Commits; gemeinsame Index-/Themen-Dateien werden nur im beauftragten Umfang gestagt.
