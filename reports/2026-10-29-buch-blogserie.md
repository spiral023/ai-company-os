# Buchserie: zwölf Beiträge veröffentlicht

**Stand:** 2026-10-29

Zwölf eigenständige Beiträge mit zusammen rund 10.600 Wörtern wurden über die automatische Prüfung freigegeben und direkt auf https://ai-blog.sp23.online veröffentlicht. Pro Buch gibt es drei Beiträge.

## A Philosophy of Software Design

- [Deep Modules: Weniger Aufruferwissen für Coding Agents](https://ai-blog.sp23.online/p/deep-modules-weniger-wissen-fuer-coding-agents/)
- [Gute Kommentare machen API-Verträge sichtbar](https://ai-blog.sp23.online/p/kommentare-api-vertraege-softwaredesign/)
- [TDD und Softwaredesign: Wo Ousterhout widerspricht](https://ai-blog.sp23.online/p/tdd-softwaredesign-ousterhout-pragmatic/)

## Domain-Driven Design

- [Bounded Context: Wo die gemeinsame Fachsprache gilt](https://ai-blog.sp23.online/p/bounded-context-gemeinsame-fachsprache/)
- [Aggregate schützen fachliche Invarianten](https://ai-blog.sp23.online/p/aggregate-fachliche-invarianten-schuetzen/)
- [Core Domain: Agentenarbeit auf den Produktkern richten](https://ai-blog.sp23.online/p/core-domain-agentenarbeit-priorisieren/)

## Beyond Vibe Coding

- [Vibe Coding: Von der Demo zur Produktreife](https://ai-blog.sp23.online/p/vibe-coding-demo-produktreife/)
- [Agentencode prüfen: Wenn alles zur falschen Annahme passt](https://ai-blog.sp23.online/p/agent-code-falsche-fachannahmen-pruefen/)
- [Parallele Agents brauchen freie Reviewkapazität](https://ai-blog.sp23.online/p/parallele-agents-review-kapazitaet/)

## The Pragmatic Programmer

- [Tracer Bullets oder Lernprototyp: Was soll weiterleben?](https://ai-blog.sp23.online/p/tracer-bullets-lernprototyp-entscheiden/)
- [DRY: Welche Fachregel ist wirklich doppelt?](https://ai-blog.sp23.online/p/dry-fachregeln-code-duplikation/)
- [Design by Contract: Erst die Zusage, dann der Code](https://ai-blog.sp23.online/p/design-by-contract-eigenschaften-pruefen/)

## Änderungen

- Zwölf neue Markdown-Beiträge unter `blog/posts/2026-10-29-*.md`; alle durch `build_blog.py --auto-freigeben` freigegeben.
- Glossar um 19 eigene Begriffserklärungen ergänzt.
- Öffentliche Buchbibliografie in `blog/site.yaml` ergänzt. Der Generator verwendet sie für die Quellenanzeige und erhält die ursprünglichen Source-IDs sowie monatsgenaue Erscheinungsangaben. Lokale PDF-Pfade erscheinen nicht in der Veröffentlichung.
- Zwei gezielte Tests für Quellenanzeige und unveränderte Herkunft ergänzt; Bedienung in `blog/README.md` dokumentiert.

## Prüfung und Auslieferung

- Ausgangsbestand 49 Beiträge, jetzt 61; alle zwölf neuen Artikel mit eigenem Thema und einem ausdrücklich hypothetischen Beispiel.
- Redaktionelle Prüfung aller zwölf Texte; fünf generische Schlussformulierungen gekürzt.
- Blog-Prüfung ohne Fehler oder Hinweise; 67 Blogtests bestanden; Python-Syntax und `git diff --check` erfolgreich.
- Lokale Desktop-/Mobilvorschau sowie veröffentlichte Beispiele einschließlich Quellenanzeige geprüft. Bei den geprüften Live-Seiten keine Browserkonsolenfehler und kein horizontaler Seitenüberlauf. Der In-App-Browser war nicht verfügbar; Browserprüfung über Playwright.
- Cloudflare-Deployment `sp23-blog`, Version `7f065847-184a-46c9-ac74-ae212b5205ae`.
- Alle zwölf öffentlichen URLs liefern HTTP 200, korrekte Überschriften, den freigegebenen Inhalt und kein Entwurfsbanner. RSS-Feed und Sitemap enthalten alle zwölf Links und stimmen byteweise mit dem Build überein.
- Cloudflare ergänzt HTML außerhalb des Builds um ein Insights-Script. Nach ausschließlich dieser beobachteten Ergänzung entsprechen alle zwölf Seiten und die Startseite exakt dem geprüften HTML. Das Script wurde durch diesen Auftrag nicht konfiguriert.
- Zehn WebSub-Benachrichtigungen für die Feeds mit HTTP 204 bestätigt.

## Git-Stand und Bestandsschutz

Die direkte Veröffentlichung ist durch den Nutzerauftrag autorisiert und durchgeführt. Im anschließenden Kursauftrag vom 29.10.2026 hat Philipp Commit und Push ausdrücklich beauftragt und auf Nachfrage die gemeinsame Sicherung von Kursauswertung, Buchauswertung und diesen zwölf Blogbeiträgen bestätigt. Die zugehörigen Source-Notizen, Pattern-Ergänzungen, Themenzuordnungen, Buchberichte und Blog-Anpassungen gehören damit zum freigegebenen Git-Umfang. Der tägliche GitHub-Workflow übernimmt den Blog anschließend aus diesem Repository.

Andere bereits vorhandene lokale Änderungen werden getrennt erhalten. Die Themenansichten für Git werden gezielt aus dem freigegebenen Bestand erzeugt, damit sie keine uncommittete fremde Source referenzieren. Prüfprotokolle, Manifest, Live-Abrufe und Screenshots liegen lokal unter `.wissen/analysen/blog-buecher-2026-10-29/`.
