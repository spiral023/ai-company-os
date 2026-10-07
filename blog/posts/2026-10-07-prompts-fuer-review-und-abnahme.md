---
titel: "Vier Prompts für Review und Abnahme: So prüfst du, was der Agent gebaut hat"
datum: 2026-10-08
kategorie: prompts
zusammenfassung: "Vier Review-Prompts für Claude Code aus vier Quellen, auf Deutsch übertragen: Prüfung gegen den Plan, Merge-Blocker im Diff, ein unabhängiger Reviewer und ein Quiz, das du vor dem Merge bestehen musst. Mit Link zum Original."
status: freigegeben
geprueft_am: 2026-10-07
freigabe: automatisch
quellen:
  - 2026-08-04-anthropic-docs-claude-code-best-practices
  - 2026-09-22-claude-getting-the-most-out-of-opus-5-5-in-claude-and-c
  - 2026-09-19-voxyz_ai-2101355643882065971
  - 2026-07-03-trq212-2073100352921215386
---

## Kurz gesagt

- Vier Prompts aus vier Quellen, je einer pro Prüffrage: Ist der Plan umgesetzt? Was blockiert den Merge? Was hat der Umsetzer übersehen? Verstehst du die Änderung selbst?
- Die ersten drei Prompts lassen einen Agent prüfen, der vierte prüft dich.
- Lass das Review in einem Subagent oder einer neuen Session laufen, nicht in der Session, die den Code geschrieben hat.
- Jeder Prompt ist auf Deutsch übertragen, das englische Original ist verlinkt.

## Die vier Prompts im Überblick

| Prompt | Prüft | Ergebnis | Von |
|---|---|---|---|
| Review gegen den Plan | Anforderungen, Tests für Randfälle, Umfang der Änderung | Liste der Lücken | Claude-Code-Dokumentation |
| Merge-Blocker im Diff | Fehler, die einen Merge verhindern | Datei, Zeile, Grund und Nachweis | Addy Osmani (Anthropic) |
| Unabhängiger Reviewer | Änderung gegen die ursprüngliche Anforderung | Befunde mit Ablauf, Auswirkung und Ort | @Voxyz_ai |
| Quiz zur Änderung | Dein eigenes Verständnis | HTML-Bericht mit Quiz | Thariq (Anthropic) |

## 1. Review gegen den Plan

Die Best Practices für Claude Code empfehlen einen eigenen Review-Schritt, in dem ein Subagent den Diff gegen den Plan prüft, nach dem gebaut wurde.{q:1}

```text
Lass einen Subagent den Diff für [Feature, z. B. den Rate Limiter] gegen
PLAN.md prüfen. Er soll kontrollieren, ob jede Anforderung umgesetzt ist, die
aufgeführten Randfälle Tests haben und nichts außerhalb der Aufgabe geändert
wurde. Melde Lücken, keine Stilvorlieben.
```

**Wann:** nach der Umsetzung, sobald es einen Plan oder eine Spezifikation als Datei gibt, etwa aus dem Interview-Prompt im [ersten Teil dieser Reihe](post:prompts-fuer-claude-code-zum-ausprobieren).

**Ergebnis:** eine Liste fehlender Anforderungen, ungetesteter Randfälle und Änderungen außerhalb des Auftrags. Der letzte Satz des Prompts hält Geschmacksfragen aus dem Bericht.{q:1}

Original: [Best Practices for Claude Code (englisch)](https://www.anthropic.com/engineering/claude-code-best-practices)

## 2. Merge-Blocker im Diff

Im Leitfaden zu Opus 5.5 rät Addy Osmani, das Modell den Diff prüfen zu lassen, bevor ein Mensch ihn liest. Sein Prompt beschränkt die Prüfung auf Probleme, die einen Merge verhindern würden.{q:2}

```text
Prüf den Diff dieses Branches gegen main.
Nenne nur Probleme, für die du den Merge blockieren würdest. Gib zu jedem
Datei und Zeile an, warum es falsch ist und wie man zeigt, dass es
fehlschlägt.
```

**Wann:** vor jedem Pull Request, auch bei kleinen Änderungen. Der Prompt braucht keine Vorbereitung.

**Ergebnis:** eine kurze Liste mit Fundstelle, Begründung und einem Weg, den Fehler nachzuweisen. Die Beschränkung auf Merge-Blocker hält Stilhinweise heraus, und der verlangte Nachweis trennt echte Fehler von Vermutungen. Laut Anthropic berichtete ein früher Tester, dass Opus 5.5 schon bei der niedrigsten Effort-Stufe mehr Bugs fand als Opus 5 bei hoher, mit weniger Fehlalarmen.{q:2} Das ist eine einzelne Rückmeldung, keine Messreihe.

Original: [Getting the most out of Opus 5.5 von Addy Osmani (englisch)](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/)

## 3. Unabhängiger Reviewer

Den Reviewer-Prompt von @Voxyz_ai gibst du laut Autor einer eigenen Konversation oder einem eigenen Review-Agent.{q:3} Maßstab ist die ursprüngliche Anforderung. Der Zusammenfassung des Umsetzers soll der Reviewer ausdrücklich nicht trauen.

```text
Prüf diese Änderung unabhängig: [ÄNDERUNG ODER ORT DER AUFGABE].
Die ursprüngliche Anforderung war: [ANFORDERUNG].

Verlass dich nicht auf die Zusammenfassung des Umsetzers, was er erledigt hat.
Sieh dir das Ergebnis selbst an. Such nach fehlenden Anforderungen, nach
Nutzeraktionen, die zu Fehlern führen können, und nach Änderungen, die bisher
funktionierende Features kaputt machen.

Führ alle Prüfungen aus, die du ausführen kannst. Erklär zu jedem Problem,
wie es entsteht, welche Auswirkung es hat und wo es liegt.

Berichte die Probleme, bevor du etwas änderst. Wenn du nichts findest, das
sich zu beheben lohnt, sag das. Erfinde keine Befunde, um eine Liste zu füllen.
```

**Wann:** wenn ein anderer Agent oder eine andere Session gebaut hat, besonders bei Abläufen, die Nutzer direkt bedienen.

**Ergebnis:** Befunde mit Ablauf, Auswirkung und Fundstelle, noch bevor jemand den Code ändert. Weil der Prompt ein leeres Ergebnis erlaubt, muss der Reviewer keine Liste füllen.{q:3}

Original: [Thread von @Voxyz_ai auf X (englisch)](https://x.com/Voxyz_ai/status/2101355643882065971). Die übrigen Rollen-Prompts daraus stehen im Beitrag [Fünf Rollen-Prompts für Claude Code und Codex](post:rollen-prompts-fuer-claude-code-und-codex).

## 4. Quiz zur Änderung: Prüf dich selbst

Nach langen Sessions hat Claude oft mehr erledigt, als Thariq bewusst ist. Der Diff allein zeigt ihm nur oberflächlich, was passiert, weil vieles von bestehenden Codepfaden abhängt. Er lässt sich deshalb einen Bericht mit Quiz erstellen und merged erst, wenn er das Quiz fehlerfrei besteht.{q:4}

```text
Ich will sicher sein, dass ich alles verstehe, was in dieser Änderung passiert
ist. Erstell mir einen HTML-Bericht über die Änderungen, den ich lesen kann:
mit Kontext, Intuition, was gemacht wurde und so weiter, und unten ein Quiz
zu den Änderungen, das ich bestehen muss.
```

**Wann:** nach langen Sessions und vor dem Merge von Code, den du später selbst warten musst.

**Ergebnis:** ein HTML-Bericht zum Lesen und ein Quiz am Ende. Das Quiz prüft dein Verständnis. Ob der Code korrekt ist, klären die drei Prüfungen davor.

Original: [A Field Guide to Fable von Thariq auf X (englisch)](https://x.com/trq212/status/2073100352921215386)

## Empfehlung

Fang mit dem Merge-Blocker-Prompt an, weil er zu jedem Branch passt. Sobald du mit Plan- oder Spezifikationsdateien arbeitest, ergänze die Prüfung gegen den Plan. Lass beide in einem Subagent oder einer frischen Session laufen. Warum der Agent, der baut, seine eigene Arbeit weniger scharf prüft, steht im Beitrag zu [Agent-Loops, die nicht entgleisen](post:agent-loops-die-nicht-entgleisen).
