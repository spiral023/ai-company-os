---
url: https://github.com/garrytan/gstack
autor: garrytan
datum: 2026-10-02
erfasst: 2026-10-02
typ: repo
thema: Tools & Releases
zeitkritisch: ja
---

# gstack: `/test-audit` und die „Test Value Bar“ räumen wertlose Tests auf

Laut `CHANGELOG.md` von garrytan/gstack (Repo-Stand Commit `7fca42ad`, Einträge um v1.91.9.0) wenden alle Workflows, die Tests vorschlagen, schreiben, prüfen oder ausliefern, eine gemeinsame „Test Value Bar“ an. Der neue Skill `/test-audit` steht im CHANGELOG, in der Skill-Tabelle der `README.md` und als Ordner `test-audit/` mit `SKILL.md`. Gelesen, nichts ausgeführt.

## Kernaussagen
- Die Regel: Ein Test verdient seinen Platz nur, wenn er Verhalten schützt, das eine echte Regression brechen würde; Testanzahl ist kein Ziel. Das Coverage-Gate von `/ship` zählt nur Tests, die diese Latte nehmen.
- `/test-audit [path ...] [--since <ref>] [--max-candidates N]` findet wertarme, implementierungsgekoppelte und doppelte Tests sowie Exporte, die nur Tests am Leben halten.
- Jeder Kandidat bekommt eine Stilllegungs-Karte (was er erkennt, wer ihn sonst aufruft, welcher stärkere Nachweis bleibt, Historie, Validierung). Ohne deine Freigabe wird nichts geändert; der Bericht landet unter `~/.gstack/projects/<slug>/`.
- Ein Kommentar `gstack:test-value keep reason="..."` markiert einen Test als bewusst behalten.

## Einordnung
Nützlich für gewachsene Testsuiten, die langsam und brüchig werden. Wie gut die Treffer sind, hängt vom Projekt ab; der Skill meldet nur und ändert nach Freigabe.

## Verbindungen
- [[TDD-als-Verifikationshebel]]
- [[Testharness-als-staerkster-Hebel]]
