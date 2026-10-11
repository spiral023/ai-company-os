# Architektur in Perspektiven dokumentieren

**Konfidenz:** verifiziert

## Zweck

Eine Codebase durch getrennte Architekturfragen verständlich machen und zwischen Überblick und konkreten Implementierungsstellen navigieren können.

## Funktionsweise

1. Manifeste, Modulgrenzen und relevante Einstiegspunkte lesen.
2. Eine Gesamtansicht und nur die fachlich vorhandenen Perspektiven wählen, etwa Request-Lifecycle, Datenfluss oder externe Integrationen.
3. Knoten an konkrete Codepfade binden, ihre Zuständigkeit beschreiben und Kanten mit der Bedeutung ihrer Verbindung beschriften.
4. Elemente mit sinnvollen internen Komponenten in Unteransichten aufschlüsseln; triviale Elemente als Blätter belassen. Knoten-IDs und Ablagestruktur konsistent halten.
5. Diagramm, Kontext, Einschränkungen und offene Bedenken in getrennten lesbaren Dateien speichern. Unveränderte Elemente nicht ohne Anlass neu schreiben.
6. Formatprüfung und fachlichen Abgleich am Code getrennt durchführen. Eine korrekt gezeichnete Kante belegt keinen tatsächlichen Lauf.

## Vorteile

- Überblick und Details bleiben über dieselbe Elementstruktur verbunden.
- Dateien in Markdown und Mermaid bleiben unabhängig von einem bestimmten Viewer lesbar.
- Dateipfade und beschriftete Beziehungen schaffen Ansatzpunkte für eine gezielte Gegenprüfung.

## Nachteile & Grenzen

- Rekursive Analyse und dauerhafte Pflege können bei großen Repos erheblichen Aufwand verursachen.
- Agenten können Abhängigkeiten und Zuständigkeiten falsch ableiten; Formatvalidatoren erkennen das nicht zuverlässig.
- Ein Viewer mit eigenem Flowchart-Parser unterstützt nicht automatisch jeden Mermaid-Diagrammtyp.
- Für Oh-my-mermaid ist die Methode im Skill und Code verifiziert; ein praktischer Qualitäts- oder Zeitvorteil wurde nicht getestet.

## Wann einsetzen, wann nicht

- Einsetzen: Onboarding, Architekturgespräche und wiederkehrende Analysen eines komplexeren Systems.
- Nicht einsetzen: bekannte triviale Änderung oder einmalige Frage, für die ein kurzer nachvollzogener Codepfad genügt.

## Belege

- 2026-10-10 · [[2026-10-10-repo-oh-my-mermaid-architektur]] · verifiziert — lokale Prüfung von Scan-Skill und Implementierung am Checkout `38ccdb69298adec949177c92c88d6e3ddfb5bab7`; keine CLI-Ausführung oder Qualitätsmessung.
- 2026-10-10 · external_repos/oh-my-mermaid/oh-my-mermaid/skills/omm-scan/SKILL.md · verifiziert — Perspektivenkatalog, gezielte Codelektüre, rekursive Detailanalyse, Dateipfade und beschriftete Kanten sind ausdrücklich vorgegeben.
- 2026-10-10 · external_repos/oh-my-mermaid/oh-my-mermaid/src/lib/store.ts · verifiziert — verschachtelte Verzeichnisse und getrennte Dokumentationsfelder bilden die Architekturkarte lokal ab.
- 2026-10-10 · external_repos/oh-my-mermaid/oh-my-mermaid/src/lib/validate.ts · verifiziert — Diagrammregeln prüfen Format und Referenzen, aber keine semantische Übereinstimmung mit dem Anwendungscode.
- 2026-03-26 · [[2026-03-26-alex-sprogis-gsd-framework-fuer-claude-code-version-1-2-im-pr]] · meinung — Die historische Bestandsanalyse dokumentiert Stack, Architektur, Struktur, Konventionen, Tests, Integrationen und bekannte Problemstellen als lesbare Gesprächsgrundlage. Vollständigkeit und fachliche Richtigkeit dieser Analyse wurden hier nicht unabhängig geprüft; ein erzeugtes Dokument ersetzt keine Validierung am Bestandsprojekt.

## Spannungen & offene Fragen

- 2026-10-10: Der Scan verlangt die Analyse jedes Knotens, während [[Codepfad-vor-Aenderung-nachvollziehen]] den Umfang am konkreten Änderungsanlass begrenzt. Eine umfassende Karte ist für wiederkehrendes Onboarding sinnvoller als für jeden kleinen Fix.
- 2026-10-10: Lesbare lokale Dateien sind vom Betrieb eines Viewers oder Cloud-Abgleichs zu unterscheiden. Die Referenz enthält Netzwerk- und Installationsschritte; eine produktive Übernahme braucht deren eigene Prüfung.
- 2026-10-10: Wie werden fachlich veraltete Ansichten nach Codeänderungen erkannt? Das vorgegebene selektive Schreiben allein beantwortet diese Frage nicht.

## Verwandte Patterns

- [[Codepfad-vor-Aenderung-nachvollziehen]]
- [[Claude-als-Lernwerkzeug]]
- [[Klein-und-komposierbar]]
