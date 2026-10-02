---
url: https://github.com/mattpocock/skills
autor: mattpocock
datum: 2026-10-02
erfasst: 2026-10-02
typ: repo
thema: Tools & Releases
zeitkritisch: ja
---

# mattpocock/skills: implement-spec, pr und retro sind stabil, CONTEXT.md heißt jetzt GLOSSARY.md

Im Klon von mattpocock/skills (Stand Commit `d81f3a18`) liegen `implement-spec`, `pr` und `retro` unter `skills/engineering/`. Die Changesets `graduate-implement-spec.md`, `graduate-pr.md`, `graduate-retro.md` und `rename-context-to-glossary.md` im Ordner `.changeset/` beschreiben die Beförderung und die Umbenennung. `package.json` und `CHANGELOG.md` stehen noch bei 1.2.3, die Versionsnummer 1.3 ist im Klon also nicht bestätigt. Gelesen, nichts ausgeführt.

## Kernaussagen
- `implement-spec` setzt das Ergebnis von `/to-spec` und `/to-tickets` auf einem Integrationsbranch um und löst die Tickets im Issue-Tracker (`skills/engineering/implement-spec/SKILL.md`).
- `pr` ist eine Vorlage für den PR-Text; `retro` führt eine Retrospektive über eine Coding-Sitzung und schlägt Verbesserungen an der Agent-Umgebung vor.
- `CONTEXT.md` und `CONTEXT-MAP.md` heißen nun `GLOSSARY.md` und `GLOSSARY-MAP.md`. Laut Changeset suchen die Skills nur noch den neuen Namen, bestehende Dateien daher per `git mv CONTEXT.md GLOSSARY.md` umbenennen.

## Einordnung
Wer die Skills nutzt und ein `CONTEXT.md` hat, muss die Datei umbenennen, sonst finden die Skills sie nicht. Neu dazu kommt ein Ablauf von der Spec bis zum PR.

## Verbindungen
- [[CONTEXT-Glossar]]
- [[Spec-Ordner-pro-Feature]]
