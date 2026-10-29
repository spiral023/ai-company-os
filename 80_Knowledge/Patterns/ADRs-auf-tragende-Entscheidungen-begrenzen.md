# ADRs auf tragende Entscheidungen begrenzen

**Konfidenz:** verifiziert

## Zweck

Den Grund einer schwer umkehrbaren, später überraschenden Entscheidung bewahren, ohne Agents bei jeder Session mit Implementierungsdetails und gewöhnlichen Produktanforderungen zu belasten.

## Funktionsweise

Vor einem Architecture Decision Record drei Fragen gemeinsam prüfen: Ist die Entscheidung schwer umkehrbar? Wäre sie ohne Kontext überraschend? Gab es einen tatsächlichen Trade-off mit ernsthaften Alternativen? Im Matt-Pocock-Referenzformat müssen alle drei Bedingungen erfüllt sein. Ein kurzer Absatz mit Kontext, Entscheidung und Grund genügt; zusätzliche Abschnitte verdienen ihren Platz durch benötigte Information.

Das Glossar erklärt die Bedeutung von Fachbegriffen. Der Code zeigt die aktuelle Umsetzung. Ein ADR erklärt einen wichtigen Entscheidungsgrund, den beide sonst nicht bewahren. Eine gewöhnliche Frist oder ein aus dem Code offensichtlicher Ablauf wird dadurch nicht automatisch zum ADR. Beim Review gegen die aktuelle Implementierung prüfen, ob die Entscheidung noch gilt und der Text das Glossar konsistent verwendet.

## Vorteile

- Bewahrt schwer rekonstruierbare Gründe über Sessions und Teamwechsel hinweg.
- Verhindert, dass ein Agent eine bewusste Abweichung als vermeintlichen Fehler korrigiert.
- Begrenzt dauerhaft benötigten Kontext auf Entscheidungen mit eigenständigem Informationswert.

## Nachteile & Grenzen

- Die drei Kriterien erfordern fachliches Urteil; ein automatischer Dateicheck genügt nicht.
- Ein kurzer Text kann einen echten Konflikt verschweigen, wenn er nur das Ergebnis nennt.
- Die Wahl eines Speicherorts und die Behandlung überholter ADRs bleiben projektspezifisch.

## Wann einsetzen, wann nicht

- Einsetzen: Architekturgrenzen, Integrationsentscheidungen oder bewusste Abweichungen mit bleibenden Folgekosten.
- Nicht einsetzen: jede Bibliothekswahl, jede Story oder eine bloße Beschreibung bereits offensichtlichen Codes.

## Belege

- 2026-10-29 · [[2026-10-29-matt-pocock-software-factories-real-engineers]] · meinung — Die HTML-Leseausgabe zeigt ADR-Auswahl und Pruning an einem Kursprodukt; Datum ist der Erfassungstag bei unbekanntem Veröffentlichungsdatum. Die Beispiele unterscheiden Domänenbegriffe, aktuelle Umsetzung und bewahrenswerte Entscheidungsgründe.
- 2026-10-29 · external_repos/mattpocock/skills/skills/engineering/domain-modeling/ADR-FORMAT.md · verifiziert — Die drei gemeinsamen Bedingungen sowie das minimale Absatzformat im lokalen Checkout 59db609eb1e18aaf59b63284d0e52255aff0c63c statisch geprüft. Das bestätigt die dokumentierte Methode, keine gemessene Wirksamkeit.

## Spannungen & offene Fragen

- 2026-10-29: Der Kurs bespricht auch das Entfernen wenig nützlicher ADRs. Bestehende Knowledge-Patterns dieses Repos werden weiterhin ausschließlich ergänzt; daraus entsteht kein Löschauftrag. Für Projekt-ADRs muss vor dem Pruning geklärt sein, welche Historie erhalten bleibt.
- 2026-10-29: ADRs möglichst kurz zu halten steht in Spannung zu ausführlicher Abwägungsdokumentation. Bewahrenswert ist der fehlende Entscheidungsgrund; Kürze allein ist kein Qualitätsbeweis.

## Verwandte Patterns

- [[CONTEXT-Glossar]]
- [[Plan-first-mit-getrenntem-Review]]
- [[Designalternativen-vor-Festlegung-vergleichen]]
