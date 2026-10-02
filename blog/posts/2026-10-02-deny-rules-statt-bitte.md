---
titel: "„Lies niemals .env“ schützt nichts: fünf Sicherheitsversprechen für Coding-Agents im Check"
datum: 2026-10-02
kategorie: check
zusammenfassung: "Claude Code Sicherheit beginnt dort, wo ein Zugriff technisch blockiert wird. Fünf verbreitete Aussagen zu Secrets, Deny-Rules, Hooks und Sandbox im Check, dazu die Einrichtung für heute."
status: freigegeben
geprueft_am: 2026-10-02
quellen:
  - 2026-04-30-zodchiii-claude-code-env-security
  - 2026-02-01-anthropic-docs-automate-workflows-with-hooks
  - 2026-01-22-hooeem-claude-code-7-schritte-plan
  - 2026-08-04-anthropic-docs-claude-code-best-practices
  - 2026-02-28-openai-codex-rules-guide
  - 2026-02-05-d4m1n-docker-sandboxes
  - 2026-08-18-docker-2089789519788728379
  - 2026-05-13-david-wiesen-openai-codex-windows-sandbox
---

## Kurz gesagt

- Ein Verbot in `CLAUDE.md` oder `AGENTS.md` ist eine Bitte an das Modell. Sperren musst du in `settings.json`.
- Deny-Rules decken nur das direkte Lesen ab. Secrets lecken auch über Test-Output, Suchtreffer und verpackte Shell-Befehle.
- Gib deinen Projekten heute eine globale Deny-Liste, eine `.env.test` mit Dummy-Werten und einen Secret-Scan vor dem Commit.
- Lass den Agent ohne Rückfragen nur in einer Sandbox laufen, in der keine echten Zugangsdaten liegen.

## Das Ergebnis

| Nr. | Aussage | Urteil |
|---|---|---|
| 1 | Eine Zeile in `CLAUDE.md` hält den Agent von `.env` fern | stimmt nicht |
| 2 | Mit Deny-Rules sind die Secrets dicht | stimmt nicht |
| 3 | Ein `PreToolUse`-Hook sperrt so hart wie eine Deny-Regel | stimmt |
| 4 | Auto Mode macht die Deny-Liste überflüssig | stimmt nicht |
| 5 | In einer Docker Sandbox ist der YOLO-Modus unbedenklich | nicht prüfbar |

## 1. „Eine Zeile in CLAUDE.md reicht“

Was behauptet wird: Wer „lies niemals .env“ in die Agent-Datei schreibt, hat seine Secrets geschützt. Was stimmt: Der Satz landet im Kontext und beeinflusst das Verhalten. Was fehlt: jede Durchsetzung. darkzodchi nennt das den Unterschied zwischen „sollte nicht“ und „kann technisch nicht“. Bei komplexen oder mehrdeutigen Aufgaben greift der Agent trotzdem zu {q:1}. Urteil: stimmt nicht.

## 2. „Mit Deny-Rules sind die Secrets dicht“

Was behauptet wird: Eine Deny-Regel in `settings.json` erledigt das Thema. Was stimmt: Den direkten Read auf `.env`, `.pem` oder `.key` fängt sie zuverlässig ab. Was fehlt: zwei weitere Wege, auf denen Secrets in den Kontext geraten {q:1}. Der Agent startet Tests oder die App, und im Output stehen Auth-Header, Connection Strings oder echte API-Keys. Oder eine Suche liefert Treffer aus Config-Dateien.

OpenAI beschreibt in der Codex-Doku einen dritten Weg. Ein Filter, der nur das Präfix eines Befehls prüft, lässt sich umgehen, wenn mehrere Befehle in einem `bash -lc "git add . && rm -rf /"` stecken. Codex zerlegt solche Ketten per Tree-sitter und prüft jeden Teil einzeln. Enthält die Kette Variablen, Wildcards, Umleitungen oder Schleifen, bleibt sie ein Block {q:5}. Urteil: stimmt nicht.

## 3. „Ein Hook sperrt so hart wie eine Deny-Regel“

Was behauptet wird: Ein `PreToolUse`-Hook ist eine echte Sperre. Was stimmt: Er läuft vor dem Tool, bekommt den Aufruf als JSON und blockiert ihn mit Exit-Code 2 {q:2}. Die Begründung gehört nach `stderr`, nur dann sieht der Agent die Blockade und ändert seinen Weg {q:3}.

Was fehlt: Die Logik schreibst du selbst, und damit hängt die Sicherheit an deiner Sorgfalt. Anthropics eigenes Beispiel prüft nur, ob `tool_input.file_path` den Text `.env` enthält, und verhindert so Schreibzugriffe {q:2}. Lesen über andere Tools, Test-Output und verpackte Shell-Befehle bleiben offen. So hart wie eine Deny-Regel ist der Hook nur, wenn du die Prüfung mindestens so breit schreibst wie deine Deny-Liste. Urteil: stimmt.

## 4. „Auto Mode macht die Deny-Liste überflüssig“

Was behauptet wird: Der neue Auto Mode prüft jeden Befehl, also braucht es keine festen Sperren mehr. Was stimmt: Ein eigenes Klassifikator-Modell bewertet laut Anthropic jeden Befehl und blockiert, was riskant wirkt, etwa Aktionen, die feindlicher Inhalt ausgelöst hat {q:4}. Was fehlt: Ein Modell kann sich irren, eine fest verdrahtete Regel nicht. Anthropic führt Auto Mode als dritten Mechanismus neben Allowlist und Sandbox. Urteil: stimmt nicht.

## 5. „In der Docker Sandbox ist YOLO sicher“

Was behauptet wird: Mit `docker sandbox run claude .` darf der Agent ohne Rückfragen arbeiten, der Host bleibt unberührt {q:6}. Was stimmt: Jede Sandbox ist eine Micro-VM mit eigenem Kernel und eigenem Docker-Daemon, und Docker meldet, dass die Claude-Code-Docs sie als Isolation empfehlen {q:7}. Das ist bisher nur eine Herstellermeldung.

Was fehlt: Die Sandbox schützt den Host. Was du hineinlegst, liegt dort offen. Für den Start meldest du dich einmal in deinem Account an {q:6}, und liegt die produktive `.env` im Projekt, ist sie auch in der Sandbox. darkzodchi rät deshalb zu Containern, in denen produktive `.env`-Dateien gar nicht existieren {q:1}. Außerdem hält eine Sandbox nur so dicht wie ihre schwächste Schicht. OpenAI hat Codex auf Windows zuerst nur über Proxy-Variablen vom Netz getrennt, und Programme mit eigenem Socket-Stack sind daran vorbeigekommen {q:8}. Urteil: nicht prüfbar.

## Was du heute einrichtest

### Deny-Liste in settings.json

Die globale Liste gehört in `~/.claude/settings.json`, damit sie in jedem Projekt gilt. darkzodchi nennt diese Pfade und dazu dieselben Muster als `Write`-Regeln {q:1}:

```json
{
  "permissions": {
    "deny": [
      "Read(**/.env*)",
      "Read(**/*.pem)",
      "Read(**/secrets/**)",
      "Read(**/.ssh/**)",
      "Write(**/.env*)",
      "Write(**/*.pem)",
      "Write(**/secrets/**)",
      "Write(**/.ssh/**)"
    ]
  }
}
```

Dazu kommt eine `.env.test` mit garantiert falschen Werten wie `sk_test_not_a_real_key`, gegen die Tests laufen. Dann kann im Output nichts Echtes stehen. Ein Pre-Commit-Hook sucht nach `sk-ant-`, `sk-live-`, `ghp_`, `AKIA` und `BEGIN.*PRIVATE KEY` {q:1}. Die Liste musst du pflegen: Jeder neue Ort für Secrets braucht eine neue Regel.

Wer Codex nutzt, legt die Entsprechung als `prefix_rule()` in `~/.codex/rules/` an. Bei mehreren Treffern gewinnt der strengste, `forbidden` vor `prompt` vor `allow`. Mit `codex execpolicy check` testest du eine Regel an einem konkreten Befehl, bevor sie scharf ist {q:5}.

### PreToolUse-Hook als zweite Schicht

Der Hook fängt ab, was die Liste nicht kennt. Grenze ihn per `matcher` auf die Tools ein, die zählen, etwa `"Bash"` oder `"Edit|Write"` {q:2}. Prüfe nicht nur Schreibzugriffe wie im Anthropic-Beispiel, sondern auch Lese- und Suchaufrufe, deren Pfad `.env` enthält. Beende das Skript dann mit Exit-Code 2 und schreib den Grund nach `stderr` {q:3}.

### Sandbox für lange Läufe

Für Läufe ohne Rückfragen ist `docker sandbox run claude .` der kürzeste Weg. Mit `docker sandbox list` und `docker sandbox exec -it <name> bash` siehst du jederzeit hinein {q:6}. Wie das in einer Schleife über Nacht aussieht, steht im Beitrag zu [Agent-Loops, die nicht entgleisen](post:agent-loops-die-nicht-entgleisen).

Eine eigene Sandbox aus Bordmitteln zu bauen, lohnt sich für die meisten nicht. OpenAI hat für Codex auf Windows AppContainer, Windows Sandbox und Mandatory Integrity Control einzeln verworfen. Die fertige Lösung kombiniert eingeschränkte Prozess-Tokens, zwei eigens angelegte lokale Nutzer mit Firewall-Regeln und ein separates Setup-Programm mit Admin-Rechten. Schreibrechte auf `.git`, `.codex` und `.agents` bleiben gesperrt {q:8}. Jede dieser Entscheidungen wägt harte Durchsetzung gegen einen Workflow ab, in dem der Agent noch an deinen echten Checkout kommt.

Setze heute die Deny-Liste global, stelle Tests auf `.env.test` um und aktiviere den Secret-Scan. Den YOLO-Modus schaltest du erst ein, wenn der Agent in einer Sandbox ohne produktive Zugangsdaten läuft. Was danach an der App selbst zu prüfen ist, zeigt der [Pre-Launch-Check](post:pre-launch-app-angreifen).
