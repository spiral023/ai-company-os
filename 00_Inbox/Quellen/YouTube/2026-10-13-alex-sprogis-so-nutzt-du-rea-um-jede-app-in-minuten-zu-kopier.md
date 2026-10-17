---
url: https://www.youtube.com/watch?v=UGwj6WaZoxQ
titel: "So nutzt du REA, um jede App in Minuten zu kopieren (Reverse Engineer Anything)"
autor: "Alex Sprogis"
datum: 2026-10-13
erfasst: 2026-10-17
typ: youtube
quelle: youtube
status: verarbeitet
verarbeitet_am: 2026-10-17
source_notiz: 80_Knowledge/Sources/2026-10-13-alex-sprogis-so-nutzt-du-rea-um-jede-app-in-minuten-zu-kopier.md
video_id: "UGwj6WaZoxQ"
transkript_sprache: "de"
transkript_generiert: "ja"
transkript_segmente: "309"
---

# So nutzt du REA, um jede App in Minuten zu kopieren (Reverse Engineer Anything)

> Automatisch per `python ai.py ingest` erfasst. Quelle: [https://www.youtube.com/watch?v=UGwj6WaZoxQ](https://www.youtube.com/watch?v=UGwj6WaZoxQ)

## Videobeschreibung

📌 Links:
Mein kostenloser AI Engineering BLUEPRINT: https://link.alexsprogis.de/voggRE

Mein AI Engineering Accelerator (Entwickle ein produktives, sicheres SaaS ohne Vorkenntnisse): https://link.alexsprogis.de/wBUpOz

REA auf Githb: https://github.com/morluto/rea
Photocraft (Photoshop Klon): https://getartcraft.com/apps/photocraft

----

Kann man mit Claude Code eine App analysieren und eine eigene Version davon bauen? Ich zeige dir REA, ein Open-Source-Tool für Reverse Engineering, und teste, ob es wirklich nötig ist.

Wir schauen uns an, was Reverse Engineering überhaupt ist, wie REA zwischen Coding Agent und Analysewerkzeugen sitzt und wie ich das an einem echten Beispiel getestet habe. 

----

Timestamps:

00:00 - Intro
01:00 - So funktioniert Reverse Engineering
02:49 - Was ist REA?
04:15 - Beispiel 1
05:20 - Beispiel 2
06:20 - Braucht es REA überhaupt? 
06:56 - Limitierungen
08:12 - Fazit
-----

🛠 Mein Tech Stack:
Editor: VS Code (kostenloser Code Editor) & T3 Code
Coding Agent: Claude Code (Opus 5.5)
Frontend: Next.js / Tailwind
Backend: Supabase / PostgreSQL
Deployment: Hostinger* (https://www.hostg.xyz/SHJ1Z)
Verwende "ALEXSPROGIS" für 10% Rabatt auf Jahrespläne. 

-----
🔔 Abonnier den Kanal  um kein weiteres Video zu verpassen
-----
📱 Folge mir auch auf anderen Kanälen:
LinkedIn: https://www.linkedin.com/in/alexander-sprogis/
Instagram: https://www.instagram.com/alex.sprogis/
TikTok: https://www.tiktok.com/@alexsprogis
-----

Auf diesem Kanal bekommst du:
- Updates zu den neuesten KI-Tools für Produktentwicklung mit AI
- Best Practices zu AI-Tools wie Claude, Cursor, Supabase und co.  
- Schritt-für-Schritt-Workflows zum Nachbauen
- Einfache Erklärungen, die komplexe KI-Konzepte - verständlich für jeden

Über mich:
Ich bin Alex. Nach 10 Jahren im Produktmanagement und 4,5 Jahren als Agency-Founder (VisualMakers) zeige ich dir hier, wie du sichere und skalierbare Software mit AI baust, auch ohne Vorkenntnisse.

Mehr zu mir findest du auf https://alexsprogis.de

## Transkript

Ein Entwickler namens Brandon Thomas hat diese Woche mit Artraft eine Opource Version von Photoshop veröffentlicht. Dazu kommen nachbauten weitere Adobe Programme unter anderem zu Premiere Pro, Illustrator, Lightroom, After Effects und Co, die alle samt kostenlos verfügbar sein werden. Laut Brandon wurden die Programme als Clean Room Reimplementation umgesetzt, also angeblich ohne den Code der Originale zu verwenden. Zeitgleich ist jetzt ein neues Repository komplett viral gegangen, das ist dir ermöglicht, Funktionen aus bestehenden Apps zu analysieren und in deine eigenen Anwendung zu integrieren. Das Projekt heißt REA, also Reverse Engineer Anything oder Rear, wie ich es im weiteren Verlauf nennen werde und hat in wenigen Tagen über 120.000 Sterne auf Gitter bekommen. Jetzt werden einige Stimmen laut, die sagen, dass die Tage von Closed Software offiziell vorbei sind, weil ich damit jetzt jeder wirklich alles nachbauen kann. In diesem Video wollen wir uns also mal anschauen, wie das Ganze funktioniert und ob man jetzt wirklich jegliche Funktion von bestehenden Apps ganz einfach kopieren kann. Also starten wir rein.

Wahrscheinlich kennst du das auch. du benutzt irgendeine App, siehst de Feature und denkst dir, das würde ich jetzt eigentlich ganz gerne mal nachbauen, vor allen Dingen jetzt mit den Coding Agents, die man zur Verfügung hat. In der Regel hast du aber natürlich keinen Zugriff auf den bestehenden Code dieser Anwendung. Kannst es also nicht einfach ganz kurz nachlesen, sondern du hast am Ende bei dir auf deinem Smartphone, auf deinem Rechner etc. meist nur die fertige App installiert. Das hat folgenden Hintergrund: Entwickler schreiben ihren Code ja in der Sprache, die für Menschen normalerweise lesbar ist, z.B. NC oder JavaScript. Bevor eine App jetzt auf einem Rechner läuft, übersetzt ein Compiler diesen Code in maschinenbaren Code. Damit ist es dann eben für deinen Rechner lesbar, aber für uns dann eben nicht mehr. Reverse Engineering ist dann wiederum quasi der Weg zurück. Das heißt, also du nimmst eine fertige Anwendung und versuchst rauszufinden, was überhaupt da drinne steckt und wie das Ganze im Detail funktioniert. Und dafür gibt es zwei Arten von Werkzeuge.

Das ist einmal der Disassembler, der macht aus dem Maschinencode Assembler, also das ist eine Form, in der ja jeder einzelne Befehl lesbar ist, aber eben sehr technisch bleibt als auch den die Compiler und der geht noch einen Schritt weiter. Der versucht jetzt nämlich aus dem Assembler Code zu rekonstruieren, der dann an eine Hochsprache wie C erinnert. Das nennt man dann auch Pseudo Code. Der ist dann deutlich leichter zu lesen, aber es ist natürlich nie der Originalcode. Das könnte jetzt so aussehen, wenn im Originalcode z.B. folgende Bedingung steht: Ifis mal Menge größer Budget, dann macht der Compiler wahrscheinlich sowas daraus wie if a mal B ist größer als C. Das heißt, die Logik lässt sich dann grundsätzlich nachvollziehen, aber eben Variablennamen, Kommentare etc., die werden z.B. verloren gehen. Solche Werkzeuge sind z.B. Gidra, IDA und Hopper. Also Gidra wurde z.B. von der NSA entwickelt und 2019 als Open Source veröffentlicht und IDA und Hopper sind z.B. kommerziell nutzbar. Bisher waren diese Werkzeuge natürlich nur für Entwickler und Entwicklerin bedienbar, aber jetzt kommt hier eben dieses Rejekt ins Spiel. Reverse Engineer Anything ist ein MCP Server für Reverse Engineering von Binaries, Anwendung und Laufzeitverhalten. Re ist primär also eher eine Schnittstelle für dein Coding Agent, also quasi zwischen deinem Agenten und den Analysewerkzeugen. Wenn du jetzt Rear in deinem Cloud Code Chat nutzt und sagst, recherchier mal, wie Funktion XY von dieser App funktioniert, dann wählt Re sozusagen das passende Werkzeug aus, das über den MCP Server verbunden ist. Das sind dann die eben genannten Deciler, also Hopper, GDRA und IDA. Die drei eignen sich vor allem für native Apps. Bei JavaScript und Electron Apps kommen sogar eigene Analysen zum Einsatz und für Websites nutzt Ria dann einfach Chrome. Am Ende bekommst du das Ergebnis dann eben mit entsprechenden Quellen zurück. Laut Doku kann Ria auch D.netprogramme oder Android Apps und sogar Firmware analysieren. Ra ist Open Source und damit komplett kostenlos nutzbar. Jetzt kommt das große, aber nur weil natürlich etwas technisch möglich ist, ist es nicht auch automatisch erlaubt. Im Repo gibt's dazu ebenfalls einen entsprechenden Disclaimer, der darauf hinweist. Das solltest du auf jeden Fall im Hinterkopf behalten. Für mich ist sowieso der primäre Usecase eher besser zu verstehen, wie ein Feature überhaupt funktioniert und daraus dann eben eine eigene Version zu entwickeln. Was du eben nicht machen solltest, ist Code aus fremden Apps eins zu eins zu übertragen und Lizenzen zu umgehen oder eben Apps zu manipulieren.

Wenn dir das Video bis hierhin gefällt, würde ich mich natürlich sehr über einen Like für das Video und ein Abo für den Kanal freuen. Aktuell haben nämlich ca. 80% der Zuschauer den Kanal noch nicht abonniert und mit dem Einklick würdest du mir sehr weiterhelfen. Also vielen Dank und weiter geht's. Ich habe Ria natürlich direkt an einem echten Projekt getestet. Dafür habe ich eine Diktierapp analysieren lassen, die du wahrscheinlich kennst, aber deren Name ich jetzt mal bewusst nicht nenne. Die Funktion ist wie folgt, du drückst einfach eine Taste, sprichst dann rein und eine KI analysiert dann sozusagen den gesprochenen Text, optimiert ihn und dann landet er eben in einem beliebigen Textfeld. Mein Ziel war zu verstehen, wie das Ganze aufgebaut ist und danach eben eine eigene einfachere Version davon zu bauen. Für diesen Prozess habe ich natürlich keinen bestehenden Code der Anwendung kopiert. Ich habe Re nur die Dateien anschauen lassen, die von der installierten App ohnehin auf meinem Rechner waren. Die App ist mit Electron gebaut, das heißt also der Code steckt im Kern in JavaScript. Das ist natürlich der beste Fall, weil ja der ganz einfach lesbar ist, wobei der in diesem Fall schon sehr stark komprimiert und auf über 180 Dateien verteilt war. Und ehrlicherweise hat Rar hier deutlich weniger geholfen, als ich am Anfang gedacht hatte. Also die erste Analyse über den MCPS Server, die ist erstmal nach 30 Minuten abgebrochen. Über die Kommandozeile lief das gleiche dann innerhalb von 5 Minuten. Und die wichtigsten Informationen hat der Agent dann durch eine einfache Textsuche gefunden. Das heißt also bei diesem Beispiel hat Ria tatsächlich relativ wenig beigetragen. Ich habe dann hier auf meinem Mac eine weitere App mal zum Test analysieren lassen und zwar ist das die Erinnerungsapp von MacOS und da konnte Ra tatsächlich deutlich mehr finden. Der Agent hat direkt GDEve gestartet, um das Ganze einmal zu analysieren und der konnte mir tatsächlich Datenmodell, Berechtigung, Funktionsbereiche, Architektur und so weiter direkt aufzeigen und auch beweisen. Die einzigen Grenzen, die er mir da aufgezeigt hat, war eben, dass die Kernlogik der Anwendung dort nicht enthalten war, weil die liegt dann im gemeinsamen Systemspeicher von MacOS und darauf hatte er in dem Sinne keinen Zugriff. Das heißt, da müsste man noch mal mit Spezialwerkzeugen ran, um die Information da eben rauszuziehen. Aber hier kann man eben ganz deutlich sehen, dass er hier deutlich mehr finden konnte. Ich habe ihn hier auch noch mal die ganzen Funktionen dieser App auflisten lassen und da sieht man also über Start und Lebenszyklus, Entwickler, Debugmenü, Seitenleiste, kann man Board Erinnerung bearbeiten, Schnelleingabe etc. Da hat er einiges gefunden und auch die entsprechenden Stellen dazu, sodass man hier dann tiefer in die Recherche einsteigen könnte. Jetzt natürlich die Frage, wäre ich ohne Rear zum gleichen Ergebnis gekommen? Und ja, das ist ziemlich wahrscheinlich, denn allein das Beschreiben der Funktionalität hätte wahrscheinlich z.B. bei der ersten App schon ausgereicht, um hier mal einen Klon eins zu ein nachbauen zu können.

Letztendlich war das ja auch dann primär der Weg, den OPOS gewählt hat. Letztendlich hatte er ja aus der Analyse gar nicht so viele Daten, von daher hat er einfach mit Hilfe von Annahmen dann eben die fehlenden Informationen ergänzt. Zusätzlich kann man dann eben noch mit Screenshots etc. nachhelfen, damit das Ergebnis dann eben optimiert wird. In dem Beispiel gab es also einfach keine komplexe Logik, die man hätte jetzt irgendwie anhand des Codes rausfinden können. In anderen Beispielen sieht das wahrscheinlich schon wieder deutlich anders aus. Man muss ja aber auch ganz kleine Limitierungen nennen und zwar sobald die Anwendungslogik in einem Backend liegt, dann haben nämlich die Werkzeuge von Ra kein Zugriff darauf und können das dann eben entsprechend auch nicht analysieren. Das heißt, dann ist es eben nicht möglich bestehenden Code zu dekompilieren und daraus eben dann die Funktionsweise abzuleiten. Da kann man das dann maximal über die Benutzeroberfläche vielleicht interpretieren. Aber es ist und das hat man dann im zweiten Beispiel gesehen, gerade für native Apps nettes Werkzeug, um Funktion zu analysieren und dann eben die Funktionsweise besser zu verstehen.

Vielleicht noch ein Hinweis zum Vorgehen. Wenn du bestehende Projekte analysierst, weil du eine Funktion in deine eigene App integrieren willst, dann lass das bitte nicht einfach stumpf eins zu eins umsetzen, sondern lass dir vorher Anforderungsdokumente schreiben, z.B. Spezifikation, planen die Umsetzung vorher und dann wirst du am Ende auch eine viel bessere Qualität erwarten können, denn so ist der Funktionsumfang klar definiert und dein Coding Agent weiß eben auch, wann die Funktion vollständig implementiert ist. Also so ein bisschen die Definition of done. Wenn du mehr zu einem professionellen Entwicklungsworkflow mit AI Agents wissen möchtest, dann kann ich dir meinen kostenlosen AI Engineering Blueprint ans Herz legen. Darin zeige ich dir ganz genau, wie du klassische Stolperfallen mit Coding Agents umgehst und einen sinnvollen Entwicklungsprozess mit Cloud Code, Codex und CO aufsetzt.

Den Link dazu findest du in der Videobeschreibung. Also, was nehme ich jetzt aus dem ganzen mit? Ist Close Software jetzt wirklich am Ende? Na ja, Features aus anderen Apps zu verstehen ist jetzt auf jeden Fall noch mal deutlich zugänglicher geworden. Und wenn man selber ein Appbsiness betreibt, dann hebt dich einzelnes Feature als USP, also als Unique Selling Point, kaum noch von der Konkurrenz ab, weil sich zumindest in der Theorie jeder jetzt quasi alles in Windows alle nachbauen kann. Ehrlicherweise war das aber auch schon vor Re. Sollte dich das jetzt davon abhalten überhaupt anzufangen?

Nein, auf gar keinen Fall. Also bitte, wenn du eine Software entwickeln möchtest, vielleicht auch ein Software Service, dann fang unbedingt an. Denn nur weil jetzt jeder gefühlt alles bauen kann, machen es trotzdem am Ende die wenigsten. Ja, nur weil irgendwie viele Menschen gerne zu Hause kochen, machen sie auch nicht automatisch dem Restaurant in der Nachbarschaft Konkurrenz. Mich wird aber natürlich auch interessieren, wie du das siehst. Hast du Ria schon ausprobiert oder siehst du direkt US Cases, wo du es gerne mal ausprobieren wolltest? Gibt's irgendeine App, die du dir privat schon nachgebaut hast, weil du es leid warst, das Abo dafür zu bezahlen? Schreib mir das gerne mal in die Kommentare. Falls dir das Video gefallen hat, dann lass gerne ein Like für das Video da oder auch ein Abo für den Kanal. Darüber würde ich mich sehr freuen und dann hoffe ich, dass wir uns beim nächsten Video wiedersehen. Also bis dahin.

Mach's gut.
