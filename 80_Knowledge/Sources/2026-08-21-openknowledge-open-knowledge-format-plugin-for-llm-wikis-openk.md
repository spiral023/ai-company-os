---
url: https://openknowledge.ai/blog/open-knowledge-format-okf-plugin-linter
autor: Serafin Garcia
datum: 2026-08-21
erfasst: 2026-09-14
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-08-21-openknowledge-open-knowledge-format-plugin-for-llm-wikis-openk.md
thema: Tools & Releases
zeitkritisch: ja
---

# Wissensbasis als Markdown-Spezifikation: Der OKF-Linter als Steuerung für Agents

Der Blogpost der App OpenKnowledge stellt ein Plugin vor, das den Open Knowledge Format (OKF, v0.2) prüft und Agents beim Schreiben von Wiki-Dateien korrigiert. Die Quelle ist ein Produkt-Launch-Post des Herstellers. Die Beschreibung der Mechanik ist konkret, Nutzenversprechen („schreibt eine ideale OKF-Wissensbasis“) sind unbelegt. Dass OKF im Juni 2026 von Google veröffentlicht wurde, steht nur hier und ist nicht gegengeprüft.

## Das Format

OKF will Wissensbasen vertrauenswürdig, portabel und für Menschen wie Agents lesbar machen. Es bleibt bei Markdown plus YAML-Frontmatter und ist ausdrücklich kein Linter, Editor oder Registry.

- Einzige Pflicht: ein nicht leeres Feld `type` im Frontmatter. Empfohlen sind `title`, `description`, `tags` (als Liste) und `resource`; unbekannte Keys dürfen nicht abgelehnt werden.
- Provenance-Felder beantworten Herkunft, Vertrauen und Aktualität: `sources`, `generated`, `verified`, `status`, `stale_after`.
- Ein Dokumenttyp „Attested Computation“ beschreibt eine deterministische Berechnung hinter einer Aussage (Runner, Parameter, erwartete Belege). Anleitung und Prüfcode liegen im Bundle, Ergebnisse nicht.
- `index.md` ist auf jeder Ebene für Navigation reserviert (flache Linkliste, gruppiert, kein Frontmatter außer `okf_version` im Root). `log.md` protokolliert Änderungen mit ISO-Datum in Überschriften.
- Portabilität: nur Standard-Links, keine Wiki-Links in Doppelklammer-Syntax, kein `.mdx`.

## Steuerung des Agents durch Warnungen statt Sperren

Jede Regelverletzung wird als Diagnose mit Regel, Schweregrad und Zeile ausgegeben. Schreibt ein Agent per MCP eine Datei, hängen die Warnungen an der Tool-Antwort, ohne den Write zu blockieren und ohne zusätzlichen Tool-Call. Der Agent entscheidet selbst über die Korrektur. Zusätzlich gibt es MCP-Befehle für `lint` und `audit` über das ganze Projekt, womit Agents bestehende Wissensbasen migrieren. Als CLI (`ok lint`, `ok audit`) taugen dieselben Prüfungen als CI-Gate; `ok lint` endet bei Warnungen mit Exit-Code ungleich null, Link- und `.mdx`-Prüfungen brauchen einen laufenden Server. Ein mitgelieferter Skill `okf-knowledge-base` vermittelt dem Agent die Spezifikation. Die Migration ist additiv: Regeln lassen sich einzeln abschalten.

## Einordnung

Belastbar ist die Designentscheidung: Prüfergebnisse im Tool-Ergebnis mitzuliefern, ist eine kostengünstige Rückkopplung, die den Agent nicht ausbremst. Sie weicht von harten Gates ab und braucht deshalb ein separates, bewusst gesetztes CI-Gate, sonst bleiben Warnungen folgenlos. Ob Agents Warnungen zuverlässig befolgen, belegt die Quelle nicht; es gibt keine Messung. Die Frontmatter-Felder `verified` und `stale_after` adressieren das Veralten von Wissen, verlangen aber Pflege. Die Regel „keine Wiki-Links“ steht im Konflikt mit Obsidian-artigen Wissensbasen, die auf Doppelklammer-Links setzen. Der Bezug zum eigenen Repo ist eine Vergleichsfolie für Frontmatter- und Validierungsdesign, kein Migrationsbefund.

## Kernaussagen

- Lint-Warnungen im Tool-Ergebnis steuern Agents ohne Blockade und ohne Extra-Call; harte Durchsetzung bleibt CI. → [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]
- Ein Skill, der die Spezifikation verdichtet, ergänzt den Linter, damit der Agent Regeln vorab kennt. → [[Skill-Call-Hierarchie]]
- Frontmatter mit Herkunft, Verifikation und Ablaufdatum macht Wissen prüfbar. → [[Kontext-Hygiene-Entscheidungsbaum]]

## Verbindungen

- [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]
- [[Skill-Call-Hierarchie]]
- [[2026-08-14-agenticjames-ai-memory-is-trash-heres-some-solutions]]
- [[2026-04-13-wiki-compiler-gute-agents-md-schreiben]]
