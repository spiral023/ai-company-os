# Verhaltens-Spec als Grenze zwischen Analyse und Nachbau

**Konfidenz:** meinung

## Zweck

Beobachtetes Produktverhalten über eine nachvollziehbare Spezifikation an einen getrennten Builder übergeben. Die Informationsgrenze macht sichtbar, welche Anforderungen aus Beobachtung stammen und welche Details der Builder selbst entscheidet.

## Funktionsweise

1. Ein Scout untersucht das gewünschte Feature und dokumentiert Belege, beobachtbare Ein- und Ausgaben sowie unbekannte Randfälle in `reports.md`.
2. Ein Spec Writer formuliert daraus eine Verhaltensspezifikation in `spec.md`. Sie beschreibt das erforderliche Ergebnis und die bekannten Grenzen der Beobachtung.
3. Ein Builder erhält nur diese Spec und keinen Zugriff auf die Original-App oder das Untersuchungswerkzeug. Er implementiert anhand dieses begrenzten Vertrags.
4. Ein separater Comparator vergleicht Original und Ergebnis. `comparison.md` hält Abweichungen und offene Fälle für die nächste Spezifikations- und Implementierungsrunde fest.

Mehrere Scouts können unabhängige Features untersuchen. Das zentrale Unterscheidungsmerkmal ist die eingeschränkte Informationsübergabe an den Builder; Rollenbezeichnungen allein stellen diese Grenze nicht sicher.

## Vorteile

- Macht Anforderungen, Beobachtungslücken und Implementierungsentscheidungen getrennt prüfbar.
- Erzeugt wiederverwendbare Verhaltensspezifikationen und einen expliziten Abweichungsbericht.

## Nachteile & Grenzen

- Der vorliegende Leitfaden ist werblich gerahmt und liefert keinen reproduzierten Qualitätsvergleich.
- Nicht beobachtete Randfälle können in der Spec fehlen; ein Comparator benötigt geeignete Daten und Vergleichsbedingungen.
- Zusätzliche Rollen und Dokumente kosten Kontext, Zeit und Review-Aufwand.
- Die Rollentrennung ist kein Nachweis rechtlicher Zulässigkeit.

## Wann einsetzen, wann nicht

- Einsetzen: wenn ein klar abgegrenztes Verhalten beschrieben und anschließend unabhängig implementiert werden soll.
- Nicht einsetzen: wenn der Builder direkten Originalkontext benötigt und der zusätzliche Übergabeverlust schwerer wiegt als die Informationsgrenze.

## Belege

- 2026-10-21 · [[2026-10-21-milesdeutscher-2112924796866699336]] · meinung — Beschreibt Scout, Verhaltens-Spec, Builder ohne Originalzugriff und getrennten Originalvergleich mit drei Übergabedateien; kein empirischer Qualitäts- oder Rechtsnachweis.

## Spannungen & offene Fragen

- 2026-10-24: Informationsbegrenzung hilft nur bei ausreichend vollständiger Spec. Sie steht in Spannung zur Einsicht, dass verlustbehaftete Agentenübergaben Qualität kosten können; bei eng gekoppelter Arbeit den zusätzlichen Übergabeschritt prüfen.

## Verwandte Patterns

- [[Plan-first-mit-getrenntem-Review]]
- [[Testharness-als-staerkster-Hebel]]
- [[Kontrollierte-Agent-Parallelisierung]]
