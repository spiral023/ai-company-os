---
url: https://x.com/bentossell/status/2006352820140749073
autor: "Ben Tossell (@bentossell)"
datum: 2026-01-20
erfasst: 2026-07-13
typ: tweet
---

# Ben Tossell zu „Wie ich mit Agents code, ohne 'technisch' zu sein“

## Inhalt

Ben Tossell verbrauchte in vier Monaten 3 Mrd. Tokens, um Tools/CLIs/Produkte zu bauen, ohne selbst Code zu lesen — aber er liest den Agenten-Output „religiös“ und nimmt dabei Wissen über Codefunktionsweise, Projektstrukturen und Fehlerursachen auf. Lehnt den Begriff „Vibe Coding“ ab: der Begriff übersehe die Fähigkeiten in der Arbeit selbst (Analogie zu „No-Code“ um 2019) — er betreibt „System Thinking“, eine „neue technische Klasse“.

Arbeitsweise: ausschließlich CLI (Droid, Factory's CLI) statt Web-Interface. Ablauf: Idee/Pain → Kontext füttern → **Spec Mode** (Plan erstellen, aktiv hinterfragen: „Ich verstehe nicht, was das ist“, „Warum brauchen wir das?“) → Docs/Repos verlinken → Modell mit hoher Autonomie laufen lassen, Stream beobachten, bei Bedarf eingreifen → testen/iterieren. Eigene `agents.md` pro Repo-Ordner: was zu tun/nicht zu tun ist, Git-Workflow, welcher GitHub-Account, E2E-Tests (früher nie beachtet, jetzt zentral wichtig). Schaut sich fremde `agents.md`-Dateien an, um Ideen zu übernehmen.

Praktische Lernpunkte: CLIs statt MCPs bevorzugt („MCPs verbrauchen zu viel Kontext und oft brauche ich nur wenige Tools“); Skills eher in Kombination mit Bash-Commands/CLIs genutzt (portable Gmail-CLI, die in jedes Projekt gezogen wird); GitHub-App installiert, damit der Agent PRs selbst reviewen/fixen kann (Coding vom Handy aus möglich). Persönliches Learning-Modell: Bugs sind Erinnerungen an Wissenslücken — die eigene Rolle ist, diese Lücken zu finden und sicherzustellen, dass sie nicht wiederkehren. „Fail forward“: über die eigenen Fähigkeiten hinaus bauen, jeden Fehler hinterfragen. Praktische Regel: nicht zu viele Tools gleichzeitig ausprobieren, sondern eines wählen und das System lernen.

## Kernaussagen

- „Vibe Coding“ trifft die eigentliche Fähigkeit nicht: religiöses Lesen von Agenten-Output baut echtes System-Verständnis auf, auch ohne dass man selbst Code schreibt oder liest — das ist eine neue Lernform, kein Nicht-Denken → [[Great-Decoupling-Rollenverstaendnis]]
- CLIs werden gegenüber MCPs bevorzugt, weil MCPs zu viel Kontext verbrauchen und oft nur wenige Tools tatsächlich gebraucht werden → [[Erweiterungs-Ebenen-Zuordnung]]
- Eigene `agents.md` pro Projektordner mit expliziten Setup-Regeln (Git-Workflow, Account-Wahl, E2E-Tests) wird aktiv gepflegt und von fremden `agents.md`-Dateien inspiriert — E2E-Tests wurden erst durch Agentenarbeit zur zentralen Priorität → [[AGENTS-md-Onboarding-Design]]
