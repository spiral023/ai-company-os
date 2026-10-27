<!-- Generiert aus 80_Knowledge/Factory/pilot.json mit wissen karten. -->
# Fähigkeitskandidat: Spec-Review

**Stand:** 2026-10-26 · **ID:** `f-spec-review` · **Status:** Kandidat, nicht aktiviert

Anforderungserfüllung und Scope eines konkreten Diffs nachvollziehbar prüfen.

## Eingaben

- Auflösbarer Vergleichspunkt, Diff und identifizierbare Spec mit zitierbaren Anforderungen.

## Prüfbare Ausgaben

- Findings mit Datei-/Diffbezug und genauer Anforderungsreferenz.
- Expliziter Status pro geprüfter Anforderung sowie fehlende oder unklare Eingaben.

## Einsatzbedingungen

- Der Vergleichspunkt ist gültig; der Diff enthält relevante Änderungen.

## Vorgehen als Entwurf

- Spec und Diff auf den gleichen Arbeitsauftrag beziehen.
- Fehlende, teilweise und nicht beauftragte Änderungen getrennt benennen.
- Jedes Finding an die konkrete Anforderung und Fundstelle binden.
- Offene Runtime-Fragen an die Verifikation weitergeben.

## Abnahme

- Bei fehlender Spec lautet das Ergebnis nicht geprüft statt erfüllt.
- Jedes Finding ist aus der Spec nachvollziehbar; unklare Anforderungen bleiben offene Fragen.

## Stop und Eskalation

- Fehlender Vergleichspunkt oder Spec verhindert eine vollständige Aussage über Spec-Erfüllung.

## Laufzeit und Wirkungen

- Benötigt lesenden Git-/Spec-Zugriff.
- Der Ursprungsworkflow verwendet Tracker und parallele Prüfer; der fachliche Kandidat ist ein lokaler Lesevertrag.

## Grenzen und Gegenargumente

- Lesendes Review beweist kein Laufzeitverhalten und keine unabhängige Release-Freigabe.
- Spec- und Standards-Review stammen hier aus derselben Herkunftsfamilie.

## Aussagen und Belege

Die IDs verweisen auf die versionierten Belegbereiche in [pilot.json](../Factory/pilot.json). Mehrere Stellen derselben Herkunftsfamilie sind keine unabhängigen Bestätigungen.

- `c08` — Der Code-Review-Skill trennt Spec- und Standards-Ergebnisse bis zur gemeinsamen Ausgabe.
- `c09` — Fehlt die Spec, soll der Spec-Review ausdrücklich als ausgelassen berichtet werden.
- `c06` — Unabhängige Abnahme braucht geschützte Kriterien und Zuständigkeit; die Rolle Reviewer allein stellt sie nicht her.
- `c19` — In diesem Repo benötigen Commits einen ausdrücklichen Auftrag; Produktions-Deployments benötigen Freigabe. Lokale Entwürfe sind autonom erlaubt.

## Kleinster Versuch

Einen bekannten Diff mit einer absichtlich fehlenden Anforderung und einmal ohne Spec prüfen: Erwartet werden eine belegte Lücke beziehungsweise ausdrücklich nicht geprüfte Spec-Erfüllung.

Der Versuch ist vorbereitet. Eine praktische Wirksamkeitsmessung und produktive Übernahme stehen aus. Die bestehende Skill-Registry und die Repo-Freigaberegeln bleiben maßgeblich.
