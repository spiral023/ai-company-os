<!-- Generiert aus 80_Knowledge/Factory/pilot.json mit wissen karten. -->
# Fähigkeitskandidat: Standards-Review

**Stand:** 2026-10-26 · **ID:** `f-standards-review` · **Status:** Kandidat, nicht aktiviert

Einen Diff gegen tatsächliche Projektregeln prüfen und Heuristiken erkennbar getrennt halten.

## Eingaben

- Diff, Vergleichspunkt und vorhandene Standards, etwa CODING_STANDARDS.md oder CONTRIBUTING.md.

## Prüfbare Ausgaben

- Findings mit Datei-/Hunkbezug und zitierter Projektregel.
- Getrennte Liste begründeter Heuristiken sowie nicht geprüfter Aspekte.

## Einsatzbedingungen

- Verfügbare Regelquellen und deren Geltungsbereich sind bekannt.

## Vorgehen als Entwurf

- Anwendbare Projektstandards ermitteln und widersprüchliche Vorgaben benennen.
- Dokumentierte Regeln vor allgemeinen Smell-Heuristiken anwenden.
- Bereits technisch geprüfte Eigenschaften nicht als eigene manuelle Erkenntnis verkaufen.
- Standards-Ergebnis getrennt vom Spec-Ergebnis ausgeben.

## Abnahme

- Jede behauptete Regelverletzung hat eine tatsächliche Regelquelle.
- Ohne dokumentierte Regel wird ein Befund als Heuristik bezeichnet.

## Stop und Eskalation

- Unklare Regelpriorität als offene Frage zurückgeben.
- Fehlende Standards werden nicht durch erfundene Projektregeln ersetzt.

## Laufzeit und Wirkungen

- Benötigt lesenden Diff- und Dateizugriff; kein produktiver Schreibzugriff.

## Grenzen und Gegenargumente

- Standards-Konformität belegt weder Anforderungserfüllung noch Funktion oder Sicherheit.
- Die Aufteilung in zwei Kandidaten erzeugt keine zweite unabhängige Quelle.

## Aussagen und Belege

Die IDs verweisen auf die versionierten Belegbereiche in [pilot.json](../Factory/pilot.json). Mehrere Stellen derselben Herkunftsfamilie sind keine unabhängigen Bestätigungen.

- `c08` — Der Code-Review-Skill trennt Spec- und Standards-Ergebnisse bis zur gemeinsamen Ausgabe.
- `c24` — Beim Standards-Review haben dokumentierte Repo-Regeln Vorrang; allgemeine Smells bleiben begründete Heuristiken.
- `c19` — In diesem Repo benötigen Commits einen ausdrücklichen Auftrag; Produktions-Deployments benötigen Freigabe. Lokale Entwürfe sind autonom erlaubt.

## Kleinster Versuch

Einen Diff mit echter Regelverletzung und einem bloßen Code-Smell vorlegen. Erwartet werden unterschiedliche Begründungsarten und keine erfundene Regel.

Der Versuch ist vorbereitet. Eine praktische Wirksamkeitsmessung und produktive Übernahme stehen aus. Die bestehende Skill-Registry und die Repo-Freigaberegeln bleiben maßgeblich.
