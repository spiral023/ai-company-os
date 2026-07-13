---
url: https://x.com/zodchiii/status/2049779422291460576
autor: "darkzodchi (@zodchiii)"
datum: 2026-04-30
erfasst: 2026-07-13
typ: tweet
---

# darkzodchi zu „Das .env-Setup, das Claude Code von deinen Secrets fernhält“

## Inhalt

Kernthese: Wenn Claude Code Zugriff auf ein Projekt hat, sind `.env`-Dateien und andere Secret-Container ohne echte Zugriffssperren ein direkter Leckpfad, kein „weiches Risiko“. Ein Hinweis in `CLAUDE.md` wie „lies niemals .env“ ist nur Advisory; eine Deny-Regel in `settings.json` ist erzwungene Zugriffskontrolle — der Unterschied zwischen „sollte nicht“ und „kann technisch nicht“ ist der eigentliche Wert des Artikels.

Drei Leckpfade für Secrets werden unterschieden:
1. **Direkter File-Read** (`.env`, `.pem`, `.key`) — der offensichtlichste Fall, leicht mit Deny-Regeln abfangbar.
2. **Runtime-Output-Capture** — Claude startet Tests/App/Script, und im Output landen Auth-Header, Connection Strings oder echte API-Keys im Conversation-Kontext. Wird laut Artikel meist übersehen.
3. **Search-/Grep-Treffer** — Suchwerkzeuge können Secrets sichtbar machen, wenn sie Config-/Credential-Dateien zurückgeben.

Konkrete Maßnahmen: eine globale Deny-Liste in `~/.claude/settings.json` (`Read(**/.env*)`, `Read(**/*.pem)`, `Read(**/secrets/**)`, `Read(**/.ssh/**)` u.a., plus entsprechende `Write`-Deny-Regeln); ein separates `.env.test` mit garantiert falschen Dummy-Werten (`sk_test_not_a_real_key` etc.), damit Runtime-Output nie echte Secrets enthält; ein Pre-Commit-Hook, der nach Secret-Mustern sucht (`sk-ant-`, `sk-live-`, `ghp_`, `AKIA`, `BEGIN.*PRIVATE KEY`); für besonders sensible Projekte Container-Isolation, bei der produktive `.env`-Dateien im Container gar nicht vorhanden sind. Sechs-Punkte-Checkliste am Ende (Deny-Regeln vorhanden? `.env.test` genutzt? Pre-Commit-Scan? Vault statt Plaintext? `.gitignore`? `.env` außerhalb des Projektverzeichnisses?).

## Kernaussagen

- Nur Deny-Regeln in `settings.json` sind technisch erzwungen; ein Hinweis in CLAUDE.md ist reine Empfehlung ohne Durchsetzung → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- Drei Leckpfade für Secrets: direkter File-Read, Runtime-Output-Capture (Tests/Logs), Search/Grep-Treffer — die letzten beiden werden meist übersehen, obwohl Deny-Regeln nur Pfad 1 zuverlässig abdecken → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- Separates `.env.test` mit garantiert falschen Dummy-Werten verhindert, dass Runtime-Output-Capture überhaupt etwas Reales offenlegen kann → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
