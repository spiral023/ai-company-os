---
url: https://developers.openai.com/api/docs/guides/latest-model
autor: OpenAI Developers
datum: 2026-10-02
erfasst: 2026-10-02
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-10-02-developers-using-gpt-6-openai-api.md
thema: Neue Modelle
zeitkritisch: ja
---

# OpenAI-Migrationsleitfaden zur GPT-6-Familie mit Prompting-Hinweisen

Die Entwicklerseite „Using GPT-6“ beschreibt die drei GPT-6-Modelle, neue API-Funktionen und Prompt-Bausteine für Astra. Es ist eine Herstellerdokumentation: Verhaltensbeschreibungen sind Selbstangaben, Preise und Benchmarks stehen auf dieser Seite nicht. Das Veröffentlichungsdatum ist unsicher (Erfassungsdatum übernommen, Stand der Seite 2026-10-02).

## Modellstufen (Stand der Seite)
- `GPT-6 Astra`: höchste Intelligenz für anspruchsvolles Reasoning, Coding und Professional Work. OpenAI nennt „estimated API cost per task“ niedriger als bei Vorgängern trotz höherem Token-Preis, belegt auf der Seite aber nur mit dem Hinweis auf „several evaluations“.
- `GPT-6.1 Sol`: nahe an Astra, geringere Kosten; Empfehlung, auf eigenen Tasks gegen Astra zu vergleichen.
- `GPT-6 Luna`: schnellste und günstigste Stufe für fokussierte Volumenaufgaben.
- Reasoning-Effort: `low`, `medium` (Default), `high`, `xhigh`, `max`. Astra und 6.1 Sol unterstützen `none` und `minimal` nicht; `GPT-6 Sol` und `GPT-6 Luna` unterstützen `none`.
- Fast mode gibt es nicht mit EU-Data-Residency; Ultrafast nur US/global. Fast mode für Astra ohne Latenz-SLA.

## Neue API-Funktionen
Async tool calling (`async: true`), Mid-turn steering über WebSocket, `configuration_update` zum Ändern des Reasoning-Effort ohne Cache-Bruch (nur Single-Agent-Requests), asynchrones Misalignment Monitoring. Beim Wechsel von GPT-5.5 oder früher ersetzt `prompt_cache_options.ttl` (`"30m"`) den Parameter `prompt_cache_retention`; Cache-Writes werden berechnet. Bei Effort ungleich `none` entfallen `temperature`, `top_p`, `top_logprobs`.

## Prompting-Hinweise für Astra
- Initiative: Astra fragt eher nach und kann dort stoppen, wo Nutzer Annahmen erwarten. OpenAI liefert Prompt-Bausteine für Autonomie und dafür, erst ein konkretes, prüfbares Ergebnis zu bauen und dann um Freigabe zu bitten.
- Instruction following: stärker, aber empfindlicher gegenüber Skills und `AGENTS.md`; unklare oder widersprüchliche Skill-Texte können Arbeit früh blockieren. Empfohlen: Vorrang der Nutzeranweisung vor Skills explizit festlegen und Skills/Dateien auditieren.
- Subagents: Astra delegiert seltener als gewünscht; Delegation per Prompt steuern.
- Testing: gründlich, bei kleinen Aufgaben teils zu breit; Testumfang kalibrieren.
- Schreibstil: neigt zu Listen, Tabellen und wiederkehrenden Phrasen.
- Aus dem GPT-5.6-Abschnitt: schlankere Prompts erhöhten in einer Stichprobe interner Coding-Agent-Evals die Scores um etwa 10 bis 15 %, bei 41 bis 66 % weniger Tokens und 33 bis 67 % geringeren Kosten (OpenAI-intern, „directional“).

## Einordnung
Belastbar als Beschreibung der API-Oberfläche und Migrationsschritte, selbstberichtet bei allen Leistungs- und Kostenaussagen. Auffällig ist die Namensführung: Die Seite führt gleichzeitig `GPT-6 Astra`, `GPT-6.1 Sol`, `GPT-6 Luna` und ein früheres `GPT-6 Sol`, daneben GPT-5.6 mit Sol, Terra, Luna; Terra taucht in GPT-6 nicht auf. Der Hinweis, Skills und `AGENTS.md` auf versteckte Steuerungsanweisungen zu prüfen, ist für die eigene Harness relevant, weil mehr Befolgungstreue auch mehr Wirkung schlecht geschriebener Instruktionen heißt.

## Kernaussagen
- Drei Modellstufen mit Effort-Skala erlauben Vergleich auf eigenen Tasks statt Pauschalwahl → [[Modell-Eskalation-von-guenstig-nach-teuer]]
- Nutzeranweisung soll explizit Vorrang vor Skill-Anweisungen haben → [[Skill-Call-Hierarchie]]

## Verbindungen
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
- [[Skill-Call-Hierarchie]]
- [[2026-09-14-developers-rethinking-skills-and-prompts-for-gpt-6-astra-op]]
- [[2026-09-29-openai-rueckblick-auf-den-devday-2026]]
