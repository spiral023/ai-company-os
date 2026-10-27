<!-- Generiert aus 80_Knowledge/Factory/pilot.json mit wissen karten. -->
# Fähigkeitskandidat: Spec-Klärung

**Stand:** 2026-10-26 · **ID:** `f-spec-klaerung` · **Status:** Kandidat, nicht aktiviert

Offene Produktentscheidungen klären und belastbare Fakten von gewählten Annahmen trennen.

## Eingaben

- Nutzerziel, vorhandene Anforderungen und bekannte Entscheidungen.
- Zugänglicher Projektkontext und erreichbarer Entscheidungsträger.

## Prüfbare Ausgaben

- Entscheidungsbaum mit offenen und beantworteten Punkten.
- Lokaler Spec-Entwurf mit Akzeptanzkriterien, Annahmen, Quellen und Scope-Grenzen.

## Einsatzbedingungen

- Interviewmodus bei offenen Entscheidungen; Synthesemodus bei ausreichend geklärtem Kontext.

## Vorgehen als Entwurf

- Bestehende Informationen lesen und recherchierbare Fakten selbst prüfen.
- Abhängigkeiten der Entscheidungen ordnen und nur entscheidbare Fragen stellen.
- Antworten und verbleibende Annahmen mit Herkunft dokumentieren.
- Aus geklärtem Kontext einen lokalen Spec-Entwurf formulieren.

## Abnahme

- Offene Entscheidungen sind erkennbar und werden nicht stillschweigend als entschieden behandelt.
- Jedes Akzeptanzkriterium beschreibt beobachtbares Verhalten.

## Stop und Eskalation

- Unbeantwortete Nutzerentscheidung mit wesentlichem Einfluss offen zurückgeben.
- Der Spec-Entwurf erweitert den erteilten Umsetzungsauftrag nicht.

## Laufzeit und Wirkungen

- Benötigt Datei-/Recherchezugriff und bei offenen Fragen einen Antwortkanal.
- Originalskills erwarten teilweise Subagents/Tracker; der Kandidat installiert oder startet diese nicht.

## Grenzen und Gegenargumente

- Ein vollständiger Entscheidungsbaum oder bessere Produktqualität sind nicht belegt.

## Aussagen und Belege

Die IDs verweisen auf die versionierten Belegbereiche in [pilot.json](../Factory/pilot.json). Mehrere Stellen derselben Herkunftsfamilie sind keine unabhängigen Bestätigungen.

- `c13` — Grilling trennt recherchierbare Fakten von Nutzerentscheidungen und klärt die aktuelle Entscheidungsfrontier.
- `c21` — To-spec synthetisiert bereits vorhandenen Kontext und fordert an dieser Stelle kein neues Interview.
- `c19` — In diesem Repo benötigen Commits einen ausdrücklichen Auftrag; Produktions-Deployments benötigen Freigabe. Lokale Entwürfe sind autonom erlaubt.

## Kleinster Versuch

Eine absichtlich mehrdeutige Feature-Idee und eine bereits geklärte Spec vergleichen: Nur der erste Fall soll offene Entscheidungen zurückgeben; beide müssen Annahmen und Fakten unterscheiden.

Der Versuch ist vorbereitet. Eine praktische Wirksamkeitsmessung und produktive Übernahme stehen aus. Die bestehende Skill-Registry und die Repo-Freigaberegeln bleiben maßgeblich.
