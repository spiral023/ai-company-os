---
url: https://www.youtube.com/watch?v=DN7bHOVmE88
titel: "Hör auf, Software-Abos zu kaufen..."
autor: "Alex Sprogis"
datum: 2026-10-20
erfasst: 2026-10-22
typ: youtube
quelle: youtube
status: verarbeitet
verarbeitet_am: 2026-10-22
source_notiz: 80_Knowledge/Sources/2026-10-20-alex-sprogis-hoer-auf-software-abos-zu-kaufen.md
video_id: "DN7bHOVmE88"
transkript_quelle: "Chrome-Export der YouTube-Untertitel"
transkript_sprache: "de"
transkript_generiert: "ja"
transkript_segmente: "363"
videobeschreibung_erfassung: "Sichtbarer Beschreibungstext, Abstände normalisiert; einzelne Links von YouTube verkürzt dargestellt"
metadaten_quelle: "YouTube-Originalseite in Chrome; Datum aus aufgeklappter Beschreibung"
---

# Hör auf, Software-Abos zu kaufen...

> Nach blockiertem Standardabruf über die YouTube-Originalseite in Chrome erfasst; automatisch erzeugte Untertitel. Quelle: [https://www.youtube.com/watch?v=DN7bHOVmE88](https://www.youtube.com/watch?v=DN7bHOVmE88)

## Videobeschreibung

📌 Links:
Mein kostenloser AI Engineering BLUEPRINT: https://link.alexsprogis.de/ZHi0bI

Mein AI Engineering Accelerator (Entwickle ein produktives, sicheres SaaS ohne Vorkenntnisse): https://link.alexsprogis.de/Y7qSXR

Prompt & Template: https://www.alexsprogis.de/blog/macos...

-----

Mit Claude Code eine eigene macOS-App entwickeln und ohne Swift-Kenntnisse? Kein Problem. Ich zeige dir, wie ich mir eine Companion entwickelt habe, also eine Menüleisten-App, die meine System-Performance überwacht und mir hilft, meinen Festplattenspeicher aufzuräumen.

Wir gehen einmal den kompletten Ablauf durch. Welche Werkzeuge du brauchst, wie du mit dem Grill-Me-Skill ein Produkt-Briefing erarbeitest, warum ich das Aussehen zuerst in Claude Design als Prototyp teste und wie Spezifikationen dafür sorgen, dass dein Coding Agent auch bei größeren Projekten den Überblick behält.

-----

TIMESTAMPS:
00:00 Intro
00:34 Das Problem
01:24 Das Vorgehen
02:05 Werkzeuge
03:09 Briefing
04:09 Konzeption
05:16 Entwicklungsprozess
07:40 Spezifikationen
09:35 Abschluss

-----

🛠 Mein Tech Stack:
Editor: VS Code (kostenloser Code Editor)
Coding Agent: Claude Code (Opus 4.7)
Frontend: Next.js / Tailwind
Backend: Supabase
Deployment: Hostinger* (https://www.hostg.xyz/SHJ1Z)
Verwende "ALEXSPROGIS" für 10% Rabatt auf Jahrespläne.

-----
🔔 Abonnier den Kanal um kein weiteres Video zu verpassen
-----
📱 Folge mir auch auf anderen Kanälen:
LinkedIn: /alexander-sprogis
Instagram: /alex.sprogis
TikTok: /alexsprogis
-----

Auf diesem Kanal bekommst du:
Updates zu den neuesten KI-Tools für Produktentwicklung mit AI
Best Practices zu AI-Tools wie Claude, Cursor, Supabase und co.
Schritt-für-Schritt-Workflows zum Nachbauen
Einfache Erklärungen, die komplexe KI-Konzepte - verständlich für jeden

Über mich:
Ich bin Alex. Nach 10 Jahren im Produktmanagement und 4,5 Jahren als Agency-Founder (VisualMakers) zeige ich dir hier, wie du sichere und skalierbare Software mit AI baust, auch ohne Vorkenntnisse.
Mehr zu mir findest du auf https://alexsprogis.de

## Transkript

Wir sind mittlerweile in der Ära von Personal Software angekommen. Das heißt also, statt sich irgendwie Standard Software einzukaufen, baut sich einfach jeder seine eigenen kleinen Lösungen mit Cloud Code, Codex und Co. Das gilt auch für mich und ich möchte dir heute mal zeigen, wie ich vorgegangen bin, um mir selber eine eigene macOS App zu entwickeln, die meine Systemperformance überwacht, meinen Festplattenspeicher optimiert und mir diverse Shortcuts für den alltäglichen Bedarf bereitstellt. Ich zeig dir einmal den kompletten Prozess, worauf du achten solltest und wie du sowas ohne Vorkenntnisse professionell entwickeln kannst. Also kurz zum Hintergrund, die letzten Monate hat sich bei mir einiges an Rohmaterial von Content auf meiner lokalen Festplatte angesiedelt und ich bin immer wieder kurz vor der Kapazitätsgrenze meines Festplattenspeichers angekommen.

Selbst mit externen Festplatten und Co. sammelt sich, ja, über die Zeit einfach extrem viel Datenmüll an, auch wenn es immer nur wieder kleine Video Snippets sind, die ich kurz mal brauche und dann eigentlich verwerfen kann. Müllt das Ganze dann Stück für Stück meinen Rechner zu. Ich habe mir im Laufe der Zeit natürlich immer wieder Lösungen am Markt angeschaut. Es gibt da super viele kostenlose Tools, die deinen Festplattenspeicher aufräumen, Festplattenkarten erstellen, um zu gucken, okay, wo wird denn der meiste Speicherplatz belegt und so weiter. Aber am Ende kommen dann doch wieder irgendwelche Abos, die du abschließen musst oder irgendwelche Premiumfunktionen, die sich hinter einer Paywall verstecken. Und ja, da habe ich natürlich selber keine Lust mehr drauf und deswegen dachte ich mir, okay, mir reicht's jetzt, ich entwickle mir meine eigene App für mich selbst. Jetzt kann man natürlich so vorgehen, das Ganze einfach los zu prompten in Cloud Code und der wird dir dann irgendwie schon so eine App entwickeln. Aber mit diesem Ansatz läufst du zwangsläufig in verschiedene Probleme, gerade wenn alle Informationen über dein Produkt quasi nur im Chatverlauf liegen. Denn dann verliert der Coding Agent zwangsweise irgendwann den kompletten Überblick, genauso wie du selbst und du merkst das dann vor allem, wenn sich Cloud oder Codex immer wieder in Fehlerschleifen verfängt, Entscheidungen vergisst, die ihr mal getroffen habt oder auch eben bestimmte Features wieder kaputt macht, die eigentlich schon funktioniert haben.

In diesem Video möchte ich dir also mal ein strukturiertes Vorgehen zeigen, mit dem du Software KI-gestützt entwickeln solltest, um eben direkt solche Probleme von Anfang an vermeiden zu können. Fangen wir erstmal damit an, welche Werkzeuge du überhaupt für eine Mac OS App brauchst. Natürlich brauchst du einmal einen Coding Agent, das kann Cloud Code sein, das kann Codex sein, das kann Cursor sein oder oder oder, das ist eigentlich ziemlich egal. Ich persönlich nutze z.B. einmal den Max Plan von Cloud Code, als auch den Max Plan von ChatGPT und komme damit eigentlich wunderbar klar. Je nachdem, wie umfangreich deine App werden soll, reicht gegebenenfalls auch der Pro Plan, dann musst du vielleicht nur hier und da eine kleine Pause einlegen, wenn dein Limit ausgeschöpft ist. Dann brauchst du Xcode, das ist quasi die Entwicklungsumgebung von Apple. Die erlaubt es dir nämlich, native Mac OS und iOS Apps zu entwickeln. Es gibt noch andere Frameworks, mit denen du Mac OS Apps entwickeln kannst, das geht auch z.B. mit JavaScript und Electron. Das ist dann aber ein bisschen hacky, wenn du auf Systemfunktionen des Betriebssystems zugreifen möchtest, um z.B. eben die Systemperformance, wie in meinem Fall, auszulesen. Am Ende klappt das schon irgendwie, ne, es gibt dafür zusätzliche Bibliotheken, die man dann installieren oder hinzuziehen muss. Ich habe mich jetzt aber dazu entschieden, das mit einer nativen Swift-Entwicklung deutlich schlanker zu gestalten. Also geh am Mac einfach mal am besten in den App Store und lade dir die aktuelle Xcode-Version runter. Bevor ich mit der eigentlichen Entwicklung starte, erarbeite ich erstmal ein Produktbriefing, also ein Dokument, wo erstmal alle Rahmendaten zu meinem Projekt drinne stehen. Das heißt also, ich lege einmal fest, für wen ist das Produkt eigentlich, für welche Plattform möchte ich sie entwickeln, also ist das eine native App oder ist das eine Webanwendung oder sonstiges. Dann welche Funktionen soll die App abdecken und was soll sie vor allem auch nicht sein, denn das ist auch super wichtig, weil Coding Agents nach wie vor immer noch sehr dazu neigen, Overengineering zu betreiben.

Das heißt einfach, sie bauen viel mehr als eigentlich notwendig ist. Und das hier schon mal einzugrenzen, das hilft uns später bei der Entwicklung eben enorm. Jetzt musst du dir dabei natürlich nicht alle Informationen aus den Fingern ziehen. Vielleicht kannst du auch noch gar nicht alles beantworten oder hast noch gar kein ganz genaues Bild deiner Anwendung vor Augen. Ich nutze dafür sehr gerne den Grill me Skill von Matt Pocock, einem AI Engineer und auch äh YouTuber, denn der versucht mit dir ein gemeinsames Verständnis aufzubauen und wird dir in einem Interview sozusagen alle Antworten entlocken, die es braucht, um eben das vollständige Bild der Anwendung zu formen. Wenn ich dieses Briefing habe, dann geht es weiter in eine Konzeptionsphase. Das heißt, hier suche ich mir erstmal ein bisschen Inspiration, schaue mir an, wie meine App am Ende überhaupt aussehen soll und dann gehe ich erstmal in Cloud Design und er arbeite einen Prototyp. Wenn du Cloud nutzt, ist Cloud Design in deinem Abo integriert. Nutz dafür einfach mal die Seite cloud.ai/design.

Warum mache ich das überhaupt und starte nicht direkt in Cloud Code mit der Entwicklung? Also vor allem aus dem Grund, wenn ich jetzt schon direkt anfangen würde, meine echte App zu entwickeln und mir später dann überlege, okay, das Design soll doch anders aussehen, dann kann das am Ende für eine enorme Fehleranfälligkeit sorgen. Wenn ich jetzt einmal die bestehende App auf eine komplett neue Struktur oder ein kompletten neues Aussehen umziehen muss, sozusagen. Das heißt also, ich überlege mir am Anfang einmal direkt, wie soll meine App eigentlich konkret aussehen und kann das Ganze dann eben problemlos in Cloud Design anhand eines Prototyps rausfinden und damit rumspielen. Der Code, der da im Hintergrund geschrieben wird, ist zu dem Zeitpunkt noch überhaupt nicht wichtig, weil es erstmal primär um das Aussehen und eine grobe Funktionalität geht. Wenn dir das Video bis hierhin gefällt, dann würde ich mich sehr über ein Like und ein Abo von dir freuen. Aktuell haben nämlich ca. 80% der Zuschauer den Kanal noch nicht abonniert und mit dem einen Klick würdest du mir wirklich sehr weiterhelfen. Also, vielen Dank und weiter geht's. Wir haben jetzt also einmal das Briefing als auch das Aussehen unserer App. Jetzt ist also dann der Punkt gekommen, um das Ganze von unserem Coding Agent auch umsetzen zu lassen. Das heißt, jetzt startest du deine Cloud oder Codex Desktop App, den Terminal oder welche Oberfläche du auch immer nutzen möchtest. Ich für meinen Teil habe in den letzten Wochen sehr gute Erfahrung mit T3 Code gemacht. Das ist sozusagen ein Harnes für Coding Harnes ist. Ich kann also innerhalb eines Chats ganz einfach meinen Agent von z.B. Opus auf GPT, Astra und Co wechseln und habe zudem eine sehr gute Übersicht über alle meine Projektdateien. Wenn du Xcode installiert hast, dann kannst du aus all diesen Werkzeugen heraus native macOS Apps entwickeln. Der Agent kann die Apps dann auch selbstständig starten und testen, ohne dass du überhaupt Xcode als Entwicklungsumgebung starten musst.

Jetzt kannst du natürlich einfach dein Briefing und dein Prototyp Design dem Coding Agent vor die Füße schmeißen und darauf hoffen, dass er dann ja gute Arbeit leistet und dir am Ende eine fertige App präsentiert. Und um ehrlich zu sein, wenn du diese App nur für dich selber entwickelst, dann kannst du auch genauso vorgehen. Dann würde Claude jetzt wahrscheinlich erstmal ein paar Stunden entwickeln, je nach Umfang meiner Anwendung und dann hast du am Ende eine fertige App. Wenn du jetzt aber möchtest, dass deine App von anderen Nutzern verwendet wird, dann würde ich diesen Ansatz nicht unbedingt empfehlen. Denn sobald andere Nutzer am Spiel sind und du z.B. auch deren Daten verarbeitest, dann braucht es einfach komplett andere Grundvoraussetzungen.

Und das sind dann vielleicht Sachen, die du aktuell vielleicht noch gar nicht auf dem Schirm hast. Für den Fall meiner Companion App habe ich entschieden, dass ich ebenfalls einen Schritt weitergehen möchte, denn gerade wenn es um das Löschen von Dateien geht und ich den Cache leeren möchte oder dass mir die App Empfehlung ausspricht, möchte ich einfach sicher sein, dass hier im Hintergrund die richtigen Dinge passieren und ich die volle Kontrolle darüber behalte. Denn lass uns das mal ganz kurz mit dem Hausbau vergleichen. Mit dem Briefing würdest du jetzt ganz klar sagen: "Hey, bau mir mal bitte eine Stadtvilla. Ich möchte kein Reihenhaus, kein Bungalow, ich hätte gern eine Stadtvilla. Das Ding soll fünf Zimmer haben, 150 qm Wohnfläche und that's it."

Und dann würde Claude jetzt sozusagen dann eben die Umsetzung planen. Das heißt, Architektur Entscheidungen für uns treffen und eben die Reihenfolge seiner zu bearbeitenden Aufgaben festlegen. Und darin sind die Modelle wirklich extrem gut mittlerweile. Was jetzt aber vielleicht noch nicht in unserem Briefing steht, ist, wie groß sollen denn überhaupt die einzelnen Räume sein? Wo sollen Türen und Fenster eingebaut werden und wo genau wollen wir vielleicht auch die Steckdosen in diesem Raum haben? Diese Informationen in dem Detailgrad stehen aktuell noch nicht im Briefing. Und das macht es später auch schwierig für Claude, diese Details immer wieder bei einer Weiterentwicklung aus dem Code rauszuziehen. Außerdem ist es so, dass wenn wir diese Informationen eben nicht mitgeben, der Agent einfach Annahmen trifft und diese Entscheidung für dich festlegt. Und das muss ja natürlich nicht dem entsprechen, was du dir eigentlich darunter vorstellst. Was ich also stattdessen mache ist, ich nehme das Briefing und lass Claude das in einzelne Features runterbrechen. Das heißt, wenn wir wieder an das Haus zurückdenken, an die Stadtvilla, dann lasse ich Claude jetzt jeden einzelnen Raum im Detail planen. Und das mache ich mit Hilfe von Spezifikationen, also Anforderungsdokumenten. Da steht im Detail drinne, was wohin kommt, welche Funktionen vorhanden sein müssen, wie die Funktion geprüft werden können und das wird sozusagen dann unser Vertrag mit Claude, an den er sich unbedingt halten muss. Das hilft uns dann auch wirklich alle Details zu durchdenken, inklusive z.B. Sonderfälle, die im Normalbetrieb nicht auftreten, aber dennoch bedenken müssen. Und es ist gleichzeitig auch eine nachvollziehbare Dokumentation, die wir uns immer wieder klar in Erinnerung rufen können. Ich habe dir mal einen kleinen Prompt inklusive der Struktur von so einer Spezifikation runtergeschrieben, damit du das für dich und dein Projekt eben verwenden kannst. Den Link dazu findest du in der Videobeschreibung. Und auf Basis dessen lasse ich Claude dann am Ende entwickeln. Ich gehe sogar noch einen Schritt weiter, plan sogar noch ein bisschen die Architektur und dann eben den Ablauf der Aufgabenbearbeitung.

Und ich habe am Ende noch eine Qualitätssicherung eingebaut, also ein unabhängiger Agent, der dann eben noch mal gezielt die Ergebnisse prüft und mir dann auch noch mal einen Testbericht liefert, in dem dann auch Bugs etc. dokumentiert sind. Das ist aber natürlich optional für dich. Wenn du Interesse hast, dir auch sowas aufzubauen, also so eine Art Framework, dann kann ich dir meinen kostenlosen AI Engineering Blueprint ans Herz legen. Da habe ich dir einmal alles runtergeschrieben, was du genau dafür benötigst und wie du vorgehst. Den Link findest du ebenfalls in der Videobeschreibung. Jedenfalls sind die Spezifikationen eben das, was du selbst überprüfst, ob das Ganze inhaltlich korrekt ist. Weil wie gesagt, alles andere kann der Coding Agent dann von sich aus übernehmen. Aber das ist eben die Basis für die gesamte Zusammenarbeit mit dem Agent. Und das ist jetzt nichts, was ich mir irgendwie ausgedacht habe oder sowas, sondern das ist das sogenannte Spec Driven Development, also eine Softwareentwicklungsmethode, die in den letzten Jahrzehnten quasi der Standard in der professionellen Softwareentwicklung war und immer noch ist. Ja, und den Rest der Arbeit, den erledigt Claude dann quasi von selbst und am Ende musst du dann nur einmal testen, ob das Ganze dann eben auch so umgesetzt worden ist, wie du es eingangs geplant hast. Und so hast du quasi alle Werkzeuge und Bausteine, die du brauchst, um deine eigene Mac OS App zu entwickeln. Mich würde natürlich auch interessieren, wie du da genau vorgehst.

Also, hast du schon mal eine native App mit Claude Code entwickelt? Und wie bist du dabei vorgegangen? Wie testest du überhaupt die Ergebnisse, die Claude da gebaut hat? Schreib mir das gerne mal in die Kommentare. Wenn dir das Video gefallen hat, dann lass gerne ein Like und ein Abo für den Kanal da, darüber würde ich mich sehr freuen. Und wenn du den Workflow mal selber ausprobieren möchtest, dann schau dir noch mal meinen kostenlosen AI Engineering Blueprint an. Da habe ich dir das Stück für Stück runtergeschrieben, was du brauchst und wie du vorgehst. Den Link dazu findest du in der Videobeschreibung. Also, nochmal vielen Dank fürs Zuschauen und dann hoffe ich, dass wir uns beim nächsten Video wiedersehen. Bis dahin, mach's gut.

## Erfassungsbeleg

Unveränderter Browser-Export mit Zeitmarken: [transkript-browser.txt](medien/2026-10-20-alex-sprogis-hoer-auf-software-abos-zu-kaufen/transkript-browser.txt).

Einzelne Links in der Videobeschreibung wurden von YouTube verkürzt angezeigt; daraus werden keine vollständigen Zieladressen geraten.
