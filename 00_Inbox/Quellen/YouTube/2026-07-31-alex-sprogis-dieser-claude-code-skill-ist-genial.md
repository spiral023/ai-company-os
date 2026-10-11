---
url: https://www.youtube.com/watch?v=LYvSIAB4xxI
titel: "Dieser Claude Code Skill ist GENIAL!"
autor: "Alex Sprogis"
datum: 2026-07-31
erfasst: 2026-10-11
typ: youtube
quelle: youtube
status: verarbeitet
verarbeitet_am: 2026-10-11
source_notiz: 80_Knowledge/Sources/2026-07-31-alex-sprogis-dieser-claude-code-skill-ist-genial.md
video_id: "LYvSIAB4xxI"
transkript: "automatisch"
transkript_quelle: "lokale Audio-Transkription"
transkript_werkzeug: "faster-whisper 1.2.1"
transkript_modell: "large-v3"
transkript_sprache: "de"
transkript_generiert: "ja"
transkript_segmente: "38"
transkript_erfasst: "2026-10-11"
---

# Dieser Claude Code Skill ist GENIAL!

> Metadaten lokal erfasst; Transkript mit `faster-whisper` aus der vollständigen Tonspur erzeugt. Quelle: [https://www.youtube.com/watch?v=LYvSIAB4xxI](https://www.youtube.com/watch?v=LYvSIAB4xxI)

## Videobeschreibung

📌 Links:
Mein AI Engineering Accelerator (Entwickle ein produktives, sicheres SaaS ohne Vorkenntnisse): https://link.alexsprogis.de/55aAn2

Grill-me Skill: https://www.aihero.dev/skills-grill-me
Matt Pocock Skills: https://github.com/mattpocock/skills

Mein Produktivitätstool Nr.1 (alles per Spracheingabe steuern)
Wispr Flow*: https://link.alexsprogis.de/wisprflow

---

Dieser eine Skill hat komplett verändert, wie ich Software mit Claude Code entwickle. Nicht das Entwickeln selbst, sondern die Vorbereitung. In diesem Video zeige ich dir den grill-me Skill von Matt Pocock. Statt der Claude zu erklären, was du willst, dreht der Skill den Spieß um. Claude interviewt DICH so lange, bis ihr wirklich dasselbe Verständnis habt. Das Ergebnis: bessere Ergebnisse, weniger Feedback-Schleifen und spürbar weniger verbrannte Tokens.

Außerdem zeige ich dir die drei nicht ganz so offensichtlichen Probleme, an denen die meisten mit Coding Agents scheitern – und wie du den Skill in einen sauberen Entwicklungs-Workflow einbettest.

---

Kapitel

00:00 Intro
00:36 Probleme mit Claude Code
02:36 Die Lösung: Grill-me
04:11 Reviews des Skills
05:58 Praxisbeispiel 
09:33 Das volle Potenzial entfalten
10:41 Der Skill in meinem Workflow
13:29 AI Engineering Accelerator

---

🛠 Mein Tech Stack:
Editor: VS Code (kostenloser Code Editor)
Coding Agent: Claude Code (Opus 4.7)
Frontend: Next.js / Tailwind
Backend: Supabase
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

Dieser virale Skill hat komplett verändert, wie ich Software mit Cloud Code entwickle. Und ganz ehrlich, solche Hype-Phrasen wirst du von mir nicht häufig hören, deswegen es lohnt sich wirklich dran zu bleiben. Es geht um einen Open Source Skill von einem Entwickler bzw. AI Engineer namens Matt Pocock. Das dazugehörige GitHub Repository hat mittlerweile um die 200.000 Sterne. Und ich zeige dir gleich, was der Skill genau verändert und wie ich ihn in meinem Alltag einsetze. Denn was er bewirkt, sind deutlich schnellere und bessere Ergebnisse mit Cloud Code und anderen Coding Agents. Dazu sparst du dir einen Haufen Token und Cloud ist bei seiner Arbeit viel genauer, statt irgendwie nebenbei noch Sachen umzusetzen, die du gar nicht haben wolltest. Bevor wir uns den Skill gleich anschauen, will ich aber erstmal ganz kurz mit dir auf die Problematiken eingehen, die du wahrscheinlich aktuell haben wirst, wenn du mit Cloud Code Software entwickelst.

Denn wenn du jetzt gerade Cloud Code das erste Mal ausprobierst, dann ist das Tool absolut magisch. Es fühlt sich wirklich an wie Magie. Ergebnisse lassen sich super schnell produzieren und mit wenigen Prompts hat man meistens schon eine augenscheinlich gute erste Version. Und vielleicht hast du auch schon den Plan Mode von Cloud entdeckt und nutzt den vielleicht, um deine Anwendung zu planen, bevor du sie dann überhaupt umsetzen lässt. Dann bist du schon mal deutlich besser dran, als wenn du einfach drauf lospromptest. Es gibt natürlich aber ein großes Aber, denn Cloud Code und andere Coding Agents haben nämlich drei nicht ganz so offensichtliche Probleme, die dir hinten raus ziemlich schnell das Genick brechen können. Ein erstes großes Problem ist, dass Cloud während der Planung und auch während der Umsetzung deiner App Annahmen trifft, und zwar stille Annahmen. Und das kann sehr gefährlich sein. Das heißt, wenn er sich an Stellen unsicher ist oder du ihm nicht genug Informationen gegeben hast, dann trifft Cloud deine Entscheidung für dich. Und das besonders fiese dabei ist, Das macht er am Ende, ohne es dir tatsächlich zu sagen und dann wundert du dich später, warum das Ergebnis nicht dem entspricht, was du eigentlich im Kopf hattest. Zweitens, je größer dein Projekt innerhalb einer Session wird, desto schlechter wird Claudes Performance. Das nennt sich dann auch Context-Rot, ist also ein messbares Phänomen. Nur merkst du das meist erst recht spät und wenn du dann erstmal 80% deiner Anwendung stehen hast, wird der Feinschliff also die letzten 20% zu einer echten Herausforderung.

Das ging mir am Anfang auch komplett genauso. Du willst einfach nur noch eine Kleinigkeit hinzufügen oder was Bestehendes anpassen und plötzlich macht Claude deine App an Stellen kaputt, die eigentlich schon funktionieren oder er vergisst Sachen oder verfängt sich irgendwie in Fehlerschleifen, aus denen du nicht mehr rauskommst und bekommt auch die einfachsten Dinge nicht mehr hin. Und das ist dann extrem frustrierend. Und drittens, manchmal baut Claude einfach Dinge, die du nie beauftragt hast. Also auch das nennt sich Scope Drift und ist auch ein messbares Phänomen. Hatte ich gestern auch wieder erst. Ich stelle eine simple Frage und möchte eine einfache Antwort bekommen und stattdessen baut Claude mir schon irgendwelche Migrationsskripte und sonst was. Und auch das also ein super nerviges Problem. Was dir dabei hilft, Teile dieser Probleme zu beheben, ist, Claude deine Anforderungen besser verstehen zu lassen.

Dabei musst du dir jetzt nicht alle Informationen aus den Fingern saugen und überlegen, okay, also welche Informationen braucht Claude denn jetzt, damit eben das nicht passiert. Sondern du lässt Claude dich einfach explizit zu deinem Produkt oder einem Feature interviewen, sodass ihr am Ende beide eine gemeinsame Wissensbasis habt, auf der ihr dann aufbauen könnt. Ja, das Ziel ist also, dass Claude das gleiche Verständnis hat wie du, damit es dann später eben die Inhalte deutlich gezielter und besser umsetzen kann. Anthropic hat dazu irgendwann schon mal den Plan Mode in Cloud eingeführt, aber das ist nicht ansatzweise das, was es braucht, damit du nicht in diese Probleme läufst. Wenn du den Plan Mode schon mal genutzt hast, dann wirst du feststellen, okay, ja, dann stellt er dir schon mal so vier, fünf oberflächliche Fragen, aber er ist eben auch gefühlt eher darauf aus, dir schnellstmöglichst einen Plan zur Verfügung zu stellen, mit dem er dann weiterarbeiten kann. Und es geht bei weitem nicht so sehr in die Tiefe, wie es eigentlich müsste.

Stattdessen wollen wir uns aber wirklich Zeit nehmen und mehr in die Planung investieren, damit wir uns hinten raus die komplette Iteration und die ganze Fehlerbehebung ersparen können. Dafür hat Matt Pocock den sogenannten Grill-Me-Skill entwickelt. Und ganz ehrlich, das ist nicht nur gut, wenn du Software entwickelst, sondern auch für alle anderen möglichen Aufgabenbereiche, wo Claude einfach ein gutes Verständnis benötigt, um seine Arbeit effektiv erledigen zu können. Das kann so etwas Simples sein, wie du willst eine Urlaubsübergabe machen und du überlegst jetzt, welche Informationen brauchen meine Kollegen jetzt, um meine Arbeit zu übernehmen. Dann nutzt du einfach diesen Skill und lässt dich gezielt interviewen.

Also lass uns den Skill mal anschauen und dann wirst du feststellen, der ist ganz schön kurz, aber auch extrem gut. Das ist der Wahnsinn. Wir sind jetzt hier im Repository und den Link habe ich dir unten in die Videobeschreibung gepackt. Und hier in der Beschreibung sehen wir schon mal genau, worum es geht. Also es geht darum, uns zu einem Plan, zu einer Idee oder zu einer Entscheidung zu interviewen. Und zwar nicht einfach nur so, sondern das Ganze soll sozusagen... unerbittlich auf Herz und Nieren geprüft werden, bis dann am Ende ein gemeinsames Verständnis erreicht ist. Hier heißt es auch, walk down each branch of the decision tree, also das heißt natürlich, Wenn er uns jetzt zu einem Thema befragt und wir eine Antwort geben, dann kann daraus natürlich wieder ein neues Thema entstehen. Und so soll Claude wirklich den Entscheidungsbaum strukturiert abfragen und in die Tiefe gehen, um wirklich alle Aspekte davon zu verstehen. Für jede Frage formuliert Claude dann eine empfohlene Antwort und das wiederum macht die Bedienung für uns super effektiv, weil Claude mich sozusagen auch schon beim Denken unterstützt und ich oftmals mit seiner Empfehlung mitgehen kann oder eben noch zusätzlichen Input dazugeben kann.

So, ask one question at a time, also er fragt wirklich auch nur eine Frage, gibt dann die Empfehlung, wartet auf unser Feedback und macht erst dann auch weiter. Es geht also nicht darum, uns jetzt einfach einen Fragenkatalog hinzuschmeißen und wir klicken uns dann einfach entsprechend durch die Antworten, sondern es geht wirklich darum, in die Tiefe einzusteigen und deswegen macht es natürlich auch Sinn, ihm möglichst viel Input dann eben zu seinen Fragen zu geben. Hier gibt es dann auch noch eine Anweisung für Cloud und zwar, wenn Informationen in der aktuellen Umgebung gefunden werden können, sei es jetzt in einem Softwareprojekt oder vielleicht hast du auch ein Projekt in der Cloud Desktop App angelegt, dann soll Cloud natürlich erstmal da nach den Informationen aus dem System suchen, das herausfiltern, bevor uns dann am Ende die Frage stellt. Da können wir dann eben auch unnötige Fragen mit vorbeugen.

Und am Ende gibt Cloud dir dann irgendwann eine Einschätzung, wenn er der Meinung ist, dass wir ein gemeinsames Verständnis erreicht haben. Aber du gibst das finale Go, wenn das Ziel dann sozusagen erreicht ist. So, wie sieht das Ganze jetzt also in der Praxis aus? Lass uns mal ein kleines Beispiel durchnehmen. Ich nehme jetzt einmal den Befehl hier, um das Ganze gleich zu installieren und switche dann mal rüber in meine Cloud Desktop App. So, hier bin ich in Cloud Code, habe hier schon einen neuen Ordner angelegt. Und müsste jetzt hier eigentlich mal den Terminal starten, um das Ganze hier rein zu installieren. Kann ich eigentlich direkt aus Cloud Code machen, nur das Icon, was ich dafür brauche, sehe ich hier gerade noch nicht. Jetzt ist es da. Wenn irgendwer einen Tipp hat, wie man hier das Terminal-Icon vorher schon bekommt, dann gerne her damit. So, dann installiere ich hier den Skill einmal rein. Bestiege ich einmal mit Yes. So, dann.

So, da haben wir direkt alle seine Skills bekommen, macht aber nichts. Also, schauen wir mal, ob der verfügbar ist. Ja, das sieht gut aus. Dann würde ich sagen, rufen wir den doch mal auf und dann bekommt Cloud von mir die entsprechenden Instruktionen. Ich möchte mit dir eine kleine Web-Anwendung erstellen, um meine persönlichen Finanzen zu managen. So, dann stelle ich jetzt hier gerade nochmal um auf den Plan-Mode. Dass er hier noch nicht anfängt, irgendwas zu entwickeln, einfach um sicher zu gehen und dann legen wir mal los. Genau, also er lädt jetzt hier erstmal alles soweit, startet die Session, schaut sich auch an, was natürlich im Verzeichnis aktuell existiert. Okay, hier kommt der Fragenkatalog.

Und da bin ich jetzt mal gespannt. Also eine Frage von zwölf oder von ungefähr zwölf sagt er hier. Was ist der eigentliche Job dieser App? Das ist die Wurzel des Entscheidungsbaums. Finanzenmanagement ist zu unscharf. Jede der folgenden Antworten führt zu einer komplett anderen Anwendung. Kernzweck. Was ist der primäre Job der App? Also Rückblick, wo geht mein Geld hin? Ich kann auch nur eine Frage hier oder eine Antwort geben. Dann, wo kommen die Transaktionen rein? Manche Formulierungen sind auch echt der Hammer, oder? Das ist die Entscheidung, an der solche Apps sterben. Nicht am Code, an der Erfassungsdisziplin. Auch ein bisschen überdramatisch hier. Also, wie sollen die Transaktionen in die App gelangen? CSV-Import, nur manuelle Erfassung, Bank-ARP. Ja, ich sage mal CSV-Import vom Bankkonto. Ich muss sagen, ich finde die Bedienung tatsächlich im Terminal noch deutlich besser von diesem Skill, weil hier schlägt er mir jetzt natürlich immer die Antworten vor, die Empfehlung.

Aber hier zum Beispiel hat er mich gefragt, welche Konten soll die App abbilden? Bitte Banknamen dazu schreiben. So, jetzt gibt er mir natürlich die Antworten und die kann ich anklicken. Ich kann aber keine weiteren Infos dazu geben. Und das ist jetzt eben auch hier passiert. Du hast die Bank nicht genannt. Ich habe einfach eine Antwort ausgewählt. So, und jetzt fragt er nochmal eine Follow-up-Frage hier. Ja, das heißt, ich müsste jetzt hier sozusagen eigentlich immer ein Sonstiges reingehen. Eine der Musterantworten nennen oder die empfohlene Antwort hier nochmal reingeben plus mein Input. Von daher, das ist hier in der Desktop-App noch nicht so cool gelöst. Was man vielleicht machen könnte, ist den Skill so umzuschreiben, dass Claude dieses User-Ask-Question-Modul, was er hier nutzt, um diese Frageansicht zu verwenden, dass man das sozusagen per Prompt verwehrt in dem Skill. Das könnte man nochmal überprüfen.

So, trotzdem funktioniert das hier eigentlich soweit ganz gut. Wir haben erstmal so den groben Rahmen abgesteckt, haben dann über den Text-Stack gesprochen und gehen jetzt quasi rein in die verschiedenen Funktionen. Das funktioniert soweit ganz gut. Wie ich das Ganze verwende, ist trotzdem ein bisschen anders und das will ich dir gleich nochmal zeigen. Jetzt kannst du den Skill natürlich für sich nutzen, das heißt, du rufst ihn immer dann auf, wenn du mit Cloud an einem Thema arbeiten möchtest und durchläufst dann das Interview. Der Skill bietet aber noch viel mehr Potenzial und zwar dann, wenn du ihn in einen bestehenden Workflow einsetzt. Wenn du mir schon länger folgst, dann weißt du, dass ich meinen Software-Entwicklungsprozess in ein Framework gegossen habe. Also das heißt, ich arbeite so, dass ich mit Cloud erstmal die Spezifikationen erstelle, also Anforderungsdokumente, dann machen wir das Systemdesign, also Wir schauen uns an, welche Seiten und Komponenten wir brauchen. Dann lasse ich Cloud eine Aufgabenliste schreiben, wo dann jeder Punkt, der in der Spezifikation und im Systemdesign geplant ist, auch umgesetzt wird. Und aber auch nur eben das und nicht mehr. Und danach geht es dann in die Entwicklung. Und im Anschluss kommt dann noch eine komplette Qualitätssicherung inklusive automatischer Tests und Testberichten etc. Denn mit so einem Prozess oder mit so einem Vorgehen beugst du dann eben auch noch alle weiteren Probleme vor, die ich eingangs genannt hatte. Und du hast zusätzlich einen wiederholbaren Prozess, der reproduzierbare Ergebnisse erzeugt. Und wo dieser Skill jetzt alles verändert, ist direkt im ersten Schritt und zwar beim Schreiben der Spezifikation, also der Anforderungsdokumente. Und zwar habe ich das Ganze hier in meinen Skill integriert.

Hier ist mein Write-Spec-Skill sozusagen, der mich am Anfang, wenn ich ein neues Feature plane oder eine neue Funktion plane, erstmal unterstützt, die Spezifikation zu schreiben. Das heißt, hier ist erstmal die Einleitung zum Skill und so weiter und so fort. Und dann haben wir hier das Discovery-Interview. Das heißt, hier haben wir exakt die Prinzipien, die eben Matt auch in seinem Skill nutzt. Das heißt, hier Complete Shared Understanding. Wir haben eine Frage zur Zeit, immer mit einer Empfehlung. Und dann soll er eben... Ja, den Entscheidungsbaum abgrasen sozusagen, je nachdem, wo der Fragenkatalog dann eben hinführt. Dann habe ich hier natürlich noch diverse weitere Instruktionen, weil es darum dann eben geht, die Spezifikation zu schreiben und was am Ende dann dabei rauskommt. Das können wir uns auch mal anschauen. Das habe ich dann hier zum Beispiel. Das ist dann eine vollständige Spezifikation eines Features, die ich immer schreibe, bevor ich dann tatsächlich mit Cloud in die Entwicklung gehe. Einfach weil Cloud dann auch während der Entwicklung selber verifizieren kann, habe ich.

Also ist das, was ich da gerade baue, tatsächlich im Scope? Ist das exakt so vorgegeben? Und so kann ich ihn auch so ein bisschen führen, sage ich mal. Ich habe die Leitplanken links und rechts und er kann sich nur dazwischen bewegen sozusagen und sorgt dafür, dass er eben auch nicht noch irgendwie andere Sachen nebenher baut oder eben auch den Fokus verliert. on track bleibt sozusagen. Und der wichtigste Part für Cloud hier in dieser Spezifikation sind die sogenannten Akzeptanzkriterien. Das sind dann tatsächlich Funktionen, die Cloud selber dann auch testen kann, nachdem er gebaut hat. Wenn wir uns das hier mal anschauen, zum Beispiel für das Software as a Service, was ich hier entwickelt habe, ist das eine Guthabenanzeige und so sieht das Ganze dann aus. Angenommen, ein Nutzer ist eingeloggt, wenn er irgendeinen geschützten Bereich aufruft, dann wird sein aktuelles Guthaben dauerhaft als Batch in der Sidebar angezeigt. Genau, das heißt, in meinem SaaS haben die Nutzer Credits, mit denen sie den Service nutzen können und der wird links immer in der Sidebar angezeigt, damit es eben allgegenwärtig ist. So und ich nutze eben das Interview, um genau diese Akzeptanzkriterien dann später von Claude schreiben zu lassen. Und rechts, genau siehst du das dann, wie das funktioniert. Das ist jetzt hier eine Historie.

Zu einem anderen Thema, das ging hier um transaktionale E-Mails. Da sehen wir das hier, Frage 1, wann soll die Welcome-Mail raus und so weiter. Da habe ich hier meine entsprechende Antwort gegeben. Frage 2, Frage 3 und so weiter. Also Cloud steigt hier also recht tief rein, je nachdem wie viel Kontext du ihm eben auch vorher gegeben hast. Ich habe hier zum Beispiel ihm schon ein komplettes Project-Briefing gegeben, ein recht umfangreiches Markdown-File, wo die meisten Daten eben schon drinne standen und dementsprechend hat er sich hier hat er hier meistens eigentlich nur so, ich sag mal, eine Handvoll bis vielleicht zehn Fragen gestellt, um das Feature dann am Ende im Detail besser zu verstehen.

Wenn du selber den nächsten Schritt machen möchtest und echte, produktive und sichere Software-as-a-Service-Apps mit Systemen umsetzen willst, habe ich jetzt was für dich. Und zwar am 17.8. launcht mein AI Engineering Accelerator, der dich vom Vibe-Coder zum echten AI Engineer macht. Das ist ein Programm, bei dem ich dich an die Hand nehme, dich zum Cloud-Code-Experten mache und wir mit einem exklusiven Framework dein erstes sicheres Software-as-a-Service-Produkt entwickeln. Und das Beste ist, du brauchst absolut keine Vorkenntnisse. Mit dem Accelerator bekommst du mehr als 80 kurze, knackige Videolektionen, ein exklusives Framework, mit dem wir arbeiten und deine Software-as-a-Service-App entwickeln und du bekommst Zugang zu einer exklusiven Community, in der du mir und anderen Mitgliedern Fragen stellen kannst. Das Ganze ist erhältlich zu einem einmaligen Preis. Du kannst dich jetzt dafür in die Warteliste eintragen und profitierst dann sogar noch von einem exklusiven Launch-Rabatt. Den Link dazu findest du in der Videobeschreibung.

Ebenfalls in der Videobeschreibung findest du auch den Link zum Grill Me Skill. Also probiere das Ganze mal aus. Wie gesagt, eignet sich nicht nur für App-Entwicklung, sondern eben auch im alltäglichen Doing. Und schreib mir gerne mal in die Kommentare, ob du den bereits kennst oder ausprobiert hast und was deine Erfahrung damit ist. Ansonsten hoffe ich, dass dir das Video gefallen hat. Und wenn ja, dann würde ich mich natürlich über ein Like und ein Abo von dir freuen. Und dann hoffe ich, sehen wir uns beim nächsten Video wieder. Also bis dahin, mach's gut.
