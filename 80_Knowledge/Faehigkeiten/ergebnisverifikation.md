<!-- Generiert aus 80_Knowledge/Factory/pilot.json mit wissen karten. -->
# Fähigkeitskandidat: Ergebnisverifikation

**Stand:** 2026-10-26 · **ID:** `f-ergebnisverifikation` · **Status:** Kandidat, nicht aktiviert

Für eine abgegrenzte Änderung tatsächliches Verhalten gegen einen vorab benannten Prüfvertrag nachweisen.

## Eingaben

- Änderung, Abnahmekriterien, zulässige Prüfumgebung und tatsächlich erreichbare Einstiegsschnittstelle.

## Prüfbare Ausgaben

- Prüfbericht mit Eingaben, Umgebung, beobachtetem Ergebnis, Evidenzpfaden und Grenzen.
- Getrennter Status bestanden, fehlgeschlagen oder nicht prüfbar je Kriterium.

## Einsatzbedingungen

- Die Prüfumgebung und ausgeführten Aktionen sind vom Auftrag gedeckt.
- Abnahmebedingungen und erlaubte Nacharbeit stehen vor dem Lauf fest.

## Vorgehen als Entwurf

- Die reale CLI/API/UI oder passende Testoberfläche wählen.
- Beobachtbare Kriterien und konkrete Nachweise vor dem Lauf benennen.
- Prüfung innerhalb des erlaubten Scopes durchführen und Ergebnisse sichern.
- Entwurf, ausgeführten Lauf und bestandenen Nachweis unterscheiden; begrenzte Nacharbeit dokumentieren.

## Abnahme

- Der Bericht enthält tatsächliche Beobachtungen und lässt unbewiesene Kriterien offen.
- Die produzierende Instanz verschiebt nicht stillschweigend die Abnahmebedingungen.

## Stop und Eskalation

- Nicht erreichbare Oberfläche oder fehlende Berechtigung als nicht prüfbar melden.
- Bei ausgeschöpftem Iterationslimit oder unklarer Abnahme eskalieren.

## Laufzeit und Wirkungen

- Benötigt projektabhängige Test-/CLI-/Browserwerkzeuge.
- Ein Runtime-Adapter muss erlaubte Aktionen konkret festlegen; die Karte führt nichts aus.

## Grenzen und Gegenargumente

- Grüne Checks liefern nur Evidenz für ihre Eingaben, Umgebung und Spezifikation.
- Reviewer-Rolle und erzeugter Verifikationsskill sind für sich kein Unabhängigkeits- oder Erfolgsnachweis.

## Aussagen und Belege

Die IDs verweisen auf die versionierten Belegbereiche in [pilot.json](../Factory/pilot.json). Mehrere Stellen derselben Herkunftsfamilie sind keine unabhängigen Bestätigungen.

- `c14` — pstack fordert Funktionsnachweise an der realen Einstiegsschnittstelle mit sichtbarer Evidenz.
- `c15` — Ein erzeugter Verifikationsskill bleibt ohne bestätigten Prüflauf ein Entwurf.
- `c06` — Unabhängige Abnahme braucht geschützte Kriterien und Zuständigkeit; die Rolle Reviewer allein stellt sie nicht her.
- `c07` — Ein Factory-Loop soll ein prüfbares Erfolgskriterium und ein Iterationslimit erhalten.
- `c19` — In diesem Repo benötigen Commits einen ausdrücklichen Auftrag; Produktions-Deployments benötigen Freigabe. Lokale Entwürfe sind autonom erlaubt.

## Kleinster Versuch

In einer lokalen Testumgebung einen bekannten Defekt und einen nicht startbaren Dienst prüfen. Erwartet werden reproduzierbarer Fehlschlag beziehungsweise nicht prüfbar, jeweils mit Evidenz statt pauschalem Erfolg.

Der Versuch ist vorbereitet. Eine praktische Wirksamkeitsmessung und produktive Übernahme stehen aus. Die bestehende Skill-Registry und die Repo-Freigaberegeln bleiben maßgeblich.
