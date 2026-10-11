# Visuelle-Abnahme-mit-Live-Lokal-Vergleich

**Konfidenz:** meinung

## Zweck

Visuelle Codeänderungen am tatsächlich gerenderten Ergebnis prüfen, bevor die Arbeit als fertig gemeldet wird. Der Vergleich mit dem bisherigen Live-Zustand hilft, neu verursachte Fehler von bestehenden Auffälligkeiten zu unterscheiden.

## Funktionsweise

Dem Prüfagenten betroffene URLs, Seiten, Änderungen und erwarteten Soll-Zustand übergeben. Live- und lokale Version mit vergleichbaren Daten öffnen; ohne Live-Version nur lokal prüfen. Auf tatsächlichen Seiteninhalt warten und lange Seiten abschnittsweise per Screenshot erfassen. Unterschiede dokumentieren und nach Ursache zuordnen. Nur durch die Änderung verursachte Defekte korrigieren und anschließend erneut prüfen. Die Quelle begrenzt die Schleife auf zwei Runden; offene Befunde werden danach gemeldet.

Die Prüfung findet im freigegebenen Browser statt. Bestehende Tabs bleiben unberührt; neue Tabs werden geschlossen. Passworteingaben, Senden und Bezahlaktionen gehören nicht zur Prüfung. Der Bericht benennt auch unerreichbare Seiten, fehlende Zugänge und abgebrochene Schritte.

## Vorteile

- Erfasst Layout, Überlappungen und leere Bereiche, die ein Code-Review allein übersehen kann.
- Liefert konkrete Befunde vor der Fertigmeldung und begrenzt automatische Korrekturschleifen.

## Nachteile & Grenzen

- Abweichende Daten, Feature-Flags, Browserzustände und Veröffentlichungsstände können den Vergleich verfälschen.
- Beabsichtigte Änderungen brauchen einen Soll-Zustand; Gleichheit mit Live ist kein allgemeines Qualitätsziel.
- Screenshots belegen weder funktionale Korrektheit noch mobile Nutzung oder Barrierefreiheit.
- Wirksamkeit und Kostenersparnis sind in der Quelle nicht gemessen; die genannte Integration wurde hier nicht getestet.

## Wann einsetzen, wann nicht

- Einsetzen: Änderungen an Layout, Darstellung und visuellen Interaktionszuständen mit erreichbaren Testseiten.
- Nicht einsetzen: rein interne Änderungen ohne sichtbare Wirkung; produktive Schreibaktionen bleiben außerhalb dieser Prüfung.

## Belege

- 2026-10-06 · [[2026-10-06-voxyz_ai-2107576635578855461]] · meinung — Vox schlägt gerenderte Live-/Lokal-Prüfung vor der Fertigmeldung vor, mit Zuordnung neuer Defekte, maximal zwei Korrekturrunden und begrenzten Browseraktionen; Wirksamkeit und konkrete Integration sind nicht gemessen.
- 2026-10-08 · [[2026-10-08-voxyz_ai-2108324058739745228]] · meinung — Desktop und Mobile vollständig durchscrollen und auf Überdeckung sowie horizontalen Überlauf prüfen; der Post berichtet keinen tatsächlich durchgeführten Vergleich oder Test.
- 2026-09-14 · [[2026-09-14-voxyz_ai-2099528601557496220]] · meinung — Abnahmekriterien in beobachtbare Handlungen und Ergebnisse übersetzen, Designreferenz mit gerenderter Seite vergleichen und Screenshots samt Prüfgrenzen berichten; der Post liefert keine eigene ausgeführte Abnahme oder Zeitmessung.
- 2026-09-15 · [[2026-09-15-emilkowalski-2099948779864793303]] · meinung — Gewählte Animationen nach Iteration auf Performance, Accessibility und Mobile prüfen; der Thread nennt Kategorien, berichtet aber keine konkreten Browserprüfungen oder Messergebnisse.
- 2026-07-23 · [[2026-07-23-colebemis-2080392348836790395]] · meinung — Annotierte PR-Screenshots erklären betroffene UI-Bereiche für Reviewer. Das Beispiel ist ein Review-Artefakt mit berichteten Checks; es belegt selbst keinen vollständigen Live/Lokal-Vergleich oder Produktionszustand.
- 2026-09-26 · [[2026-09-26-ai-mit-arnie-gpt-6-kann-endlich-design]] · meinung — Der Autor beschreibt eine lokale Browserprüfung in mehreren Bildschirmgrößen und gespeicherte Screenshots, bevor er die Vorschau selbst durchgeht. Ein vorheriger Live-Zustand und ein systematischer Nachweis aller Prüfergebnisse fehlen; die Demo ist keine Produktionsabnahme.
- 2026-10-09 · [[2026-10-09-julian-ivanov-ki-automat-websites-mit-ki-bauen-die-gut-aussehen-und-perfo]] · meinung — Ein gesonderter Prüfagent meldet mobile Darstellungsfehler, der Builder korrigiert sie und legt sie erneut zur Prüfung vor. Berichtete Lighthouse-Werte und positive Agentenurteile wurden hier nicht reproduziert; ein Vergleich mit einem bisherigen Live-Zustand fehlt.
- 2026-09-30 · [[2026-09-30-flxrnc-2105311836190978392]] · meinung — Florence ergänzt Contact Sheets um dichte Framefolgen an schnellen Übergängen und wenige lokale Korrekturen je Runde. Die Produktionszeiten und 71 numerischen Maskottchenchecks sind Selbstberichte; Bildstichproben belegen weder nahtfreien Lauf noch Tonqualität.
- 2026-10-01 · [[2026-10-01-0xwhrrari-2105643919119696297]] · meinung — rari überträgt sichtbare Abnahme auf wichtige Beats und schnelle Übergänge, ergänzt um Sound und eigene Layoutprüfung je Ausgabeformat. Contact Sheets sind Stichproben; der Artikel enthält keinen abgenommenen Film oder gemessenen Erfolg des vorgeschlagenen Verfahrens.
- 2026-10-09 · [[2026-10-09-beamnxw-2108616740846420354]] · meinung — Eine Motion-Korrektur benennt Ort, beobachteten Fehler, konkrete Änderung und unveränderliche Elemente; danach werden Zwischenframes, benachbarte Szenengrenzen und Playback geprüft. Drei Stills helfen der Richtungsklärung, beweisen aber weder Timing noch Audioqualität oder einen fehlerfreien Gesamtfilm.

## Spannungen & offene Fragen

- Zwei Runden sind ein Budget des Quellenprompts, keine empirisch begründete Obergrenze für Fehlerbehebung.
- Ein Screenshot kann einen plausiblen Zustand zeigen, während Datenfluss oder Interaktion weiterhin fehlerhaft sind.

## Verwandte Patterns

- [[Screenshot-als-Spezifikationsmedium]]
- [[Testharness-als-staerkster-Hebel]]
- [[Plan-first-mit-getrenntem-Review]]
