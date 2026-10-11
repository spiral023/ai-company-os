# Agent-Organisation mit Rollen, Budgets und Heartbeats

**Konfidenz:** meinung

## Zweck

Wiederkehrende Arbeit mehrerer Agents über einzelne Coding-Sessions hinaus steuerbar machen: Zuständigkeiten, Aufgaben, Auslöser, Kosten und menschliche Freigaben werden gemeinsam sichtbar.

## Funktionsweise

Stand der Ausarbeitung: 2026-10-11. Die Paperclip-Demos aus April 2026 verbinden eine menschlich festgelegte Mission mit Rollen und projektgebundenen Issues. Ein Issue hält Auftrag, verantwortlichen Agent, Rückmeldungen und Laufhistorie zusammen. Rollen erhalten passende Skills, Modellzugänge und konfigurierte Budgets; eine Board-Rolle genehmigt vorgeschlagene Agents und kann Aufträge korrigieren oder Arbeit pausieren.

Starts durch zugewiesene Aufgaben werden von periodischen Heartbeats getrennt. Wiederkehrende Prüfungen brauchen einen konkreten Zweck und einen passenden Zeitplan; nicht jede Rolle muss regelmäßig aufwachen. Eine Demo richtet den Frontend-Spezialisten ausdrücklich ohne Heartbeat ein.

Als abgeleitete Prüfung müssen Budgetanzeige, Warnung und tatsächlich durchgesetzte Ausgabenbegrenzung unterschieden werden. Auch Arbeitsflächen, Freigaben konkreter Aktionen und Ergebnisabnahme bleiben eigenständige Grenzen. Ein Organigramm ersetzt diese Prüfungen nicht. Die konkreten Adapter und Installationswege sind historische Implementierungsstände.

## Vorteile

- Aufträge und Rückmeldungen bleiben über mehrere Rollen und Läufe nachvollziehbar.
- Wiederkehrende Auslöser und auftragsgesteuerte Arbeit lassen sich getrennt planen.
- Zuständigkeiten und Kostenansichten helfen bei menschlicher Steuerung.

## Nachteile & Grenzen

- Mehr Rollen und häufige Heartbeats erhöhen Koordinations-, Pflege- und Verbrauchsaufwand.
- Die Demos prüfen weder Langzeitbetrieb noch harte Budgetdurchsetzung oder Kollisionsfreiheit.
- Erfolgreiche Run-Meldungen belegen keine fachliche Ergebnisqualität.
- Menschliche Einrichtung, Fehlerbehebung und zusätzliche Aufträge bleiben sichtbar; eine wirtschaftliche menschenlose Firma ist nicht nachgewiesen.

## Wann einsetzen, wann nicht

- Einsetzen: wenn mehrere fachliche Rollen dauerhaft zugewiesene und wiederkehrende Agent-Aufgaben bearbeiten sollen.
- Nicht einsetzen: für einen einzelnen Auftrag, der mit einem Agent einfacher bleibt, oder ohne prüfbare Kosten- und Ergebnisgrenzen.

## Belege

- 2026-04-01 · [[2026-04-01-ai-mit-arnie-claude-code-und-paperclip-aendern-alles]] · meinung — Arnie erprobt Mission, Rollen, Issues und Freigaben, beobachtet aber unbestellte Skripterstellung und ungeprüfte Website-Inhalte. Der Werkzeugversuch misst keine zuverlässige autonome Organisation.
- 2026-04-03 · [[2026-04-03-julian-ivanov-ki-automat-ich-habe-eine-firma-ohne-menschen-gebaut-papercl]] · meinung — Ivanov erläutert projektgebundene Rückfragen, individuell konfigurierte Budgets und getrennte Heartbeat-Anweisungen. Konfiguration und Laufhistorie belegen keine vollständige Kostenkontrolle.
- 2026-04-12 · [[2026-04-12-digitale-profis-so-ersetzt-du-dein-unternehmen-mit-ki-agenten-pa]] · meinung — Die Demo zeigt genehmigte Rollen, delegierte Issues und einen Spezialisten ohne Heartbeat. Ein statischer Website-Prototyp nach menschlicher Arbeit weist keinen vollständigen Unternehmensersatz nach.

## Spannungen & offene Fragen

- 2026-10-11: Proaktive Arbeit kann Aufgaben voranbringen, aber auch unbestellte Ergebnisse erzeugen. Im Arnie-Beispiel genügen Mission und Run-Status weder als Handlungsfreigabe noch als Qualitätsnachweis.
- 2026-10-11: Budgetkonfiguration und Warnungen sind sichtbar; Verhalten beim Erreichen der Grenze und der gesamte Betriebsaufwand bleiben ungeprüft.
- 2026-10-11: Mehrere Demos desselben Werkzeugs sind keine unabhängigen Wirksamkeitsmessungen. Die Konfidenz bleibt `meinung`.

## Verwandte Patterns

- [[Intent-Engineering-als-dritte-Schicht]]
- [[Task-basierte-Steuerung]]
- [[Kontrollierte-Agent-Parallelisierung]]
- [[Agent-Rechte-umfassen-Kommunikationswege]]
