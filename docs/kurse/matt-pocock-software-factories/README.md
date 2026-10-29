# Matt Pocock: Software Factories for Real Engineers

**Erfasst:** 29.10.2026. Vom Nutzer lokal bereitgestellter Kurs mit 38 Videos und einer HTML-Leseausgabe. Das ursprüngliche Veröffentlichungsdatum und die Herkunft der zusammengestellten Leseausgabe sind nicht unabhängig belegt. Im HTML lautet der Seitentitel `Domain Language`; die Kapitel behandeln Sprache, Planung und Review.

Die Videos wurden kopiert und per SHA-256 verglichen. Die inhaltliche Analyse bezieht sich auf die **38 HTML-Kapitel**, ihre Übungen und Lösungen sowie ausgewählte Abbildungen. Die Videos wurden dafür nicht inhaltlich ausgewertet oder transkribiert; technische Wiedergabestichproben gehören zur Veröffentlichung des privaten Online-Kurses.

## Lesen und weiterarbeiten

- [Deutsche HTML-Leseausgabe – lokal](../../../00_Inbox/Quellen/URL/lokal/matt-pocock-software-factories-real-engineers/index.de.html)
- [Unverändertes geliefertes HTML – lokal](../../../00_Inbox/Quellen/URL/lokal/matt-pocock-software-factories-real-engineers/index.html)
- [Eigene ausführliche Analyse](../../../reports/2026-10-29-matt-pocock-software-factories-kursanalyse.md)
- [Kompakte Source-Notiz](../../../80_Knowledge/Sources/2026-10-29-matt-pocock-software-factories-real-engineers.md)
- [Abgleich mit Softwarebüchern und Factory-Entwurf](../../../80_Knowledge/Vergleiche/Matt-Pocock-Software-Factories-Kurstransfer.md)
- [Inventar mit Dateigrößen, Kapitelzuordnung und SHA-256](inventar.json)

Die lokalen Links funktionieren auf diesem Rechner. In einem neuen Clone fehlen die ignorierten Kursdateien, bis sie aus einer eigenen vorhandenen Kopie wiederhergestellt werden. Das Inventar enthält die Zuordnung und Prüfsummen, keine Videoinhalte oder Zugangsdaten.

## Lokale Ablage

```text
00_Inbox/Quellen/URL/
  2026-10-29-matt-pocock-software-factories-real-engineers.md
  lokal/matt-pocock-software-factories-real-engineers/
    index.html                 unverändertes geliefertes Original
    index.de.html              deutsche Bearbeitung
    medien/001.png … 156.png    lokal archivierte Kursabbildungen
    videos/                    alle 38 gelieferten MP4-Dateien
```

Die 39 gelieferten Dateien umfassen **1.664.537.099 Bytes**. Alle Kopien wurden mit den Originalen verglichen. Für die 156 im HTML verlinkten Bilder wurden lokale Fassungen in Originalauflösung archiviert und einzeln gehasht.

## Übersetzungsumfang

Die deutsche Bearbeitung übersetzt die erklärende Prosa, Überschriften, Navigation, Übungen, Quiztexte, Bildunterschriften und natürliche Beispielprompts. Fachbegriffe, kanonische Domänenbegriffe, Skill-Namen, Dateinamen und ausführbarer Code bleiben nach Bedarf Englisch. Text innerhalb von Screenshots und Diagrammen bleibt im Original; die beschreibenden Bildunterschriften sind Deutsch.

Das Original bleibt unverändert. Die deutsche Ausgabe verwendet lokale Bildpfade und Systemschriften als Fallback anstelle externer Font-Aufrufe. Kapitelanker, richtige Quizantworten und Aufgaben-IDs bleiben erhalten. Der Browser speichert den Fortschritt der deutschen Ausgabe getrennt vom englischen Original.

Die deutsche Leseansicht zeigt jeweils das gewählte Kapitel. Inhaltsverzeichnis und Vorher-/Weiter-Links wechseln das Kapitel; die Druckansicht enthält alle Kapitel. Feste Bildmaße stabilisieren Ankersprünge, lange Begriffe und Dateinamen brechen auf schmalen Ansichten um. Tabellen und Code können innerhalb ihres eigenen Bereichs horizontal gescrollt werden.

## Verarbeitung und Veröffentlichungsgrenze

Der vorhandene Artikel-Ingest wurde mit der lokalen Datei-URL verwendet. Da er den ersten `article`-Container auswählt, erfasste er zunächst nur Kapitel 1. Vor der Einarbeitung wurde die lokale Rohnotiz mit dem vollständigen Originaltext aller 38 Kapitel ergänzt. Das Original-HTML und das Kapitelinventar erlauben den Abgleich; eine Teilerfassung wird dadurch nicht als Gesamterfassung ausgegeben.

Dieses Repository ist öffentlich. Entsprechend seiner bestehenden Ablageregel für fremde Volltexte bleiben Original, vollständige Übersetzung, Rohtext und Kursmedien in der ignorierten lokalen Ablage. Versioniert werden eigene Auswertung, Source-Notiz, Pattern-Belege und Inventar. Es wurde kein externer Kurscode ausgeführt und kein neuer produktiver Skill aktiviert.

## Privater Online-Kurs

Auf ausdrücklichen Auftrag vom 29.10.2026 wird die deutsche Ausgabe unter <https://pocock.sp23.online/> mit Passwortanmeldung bereitgestellt. Jedes Kapitel enthält sein zugeordnetes Video; die eigene Auswertung ist unter `/analyse/` erreichbar. Auch Bilder und direkte Videozugriffe benötigen eine gültige Sitzung.

Die Medien liegen im privaten Cloudflare-R2-Bucket `sp23-pocock-kurs`; die öffentliche R2-Adresse ist deaktiviert. Volltexte und Binärdateien gelangen weiterhin nicht in das öffentliche Git-Repository. Anwendung, Build, Tests, Betriebsablauf und Sicherheitsgrenzen stehen in [pocock/README.md](../../../pocock/README.md). Das Passwort und die Sitzungsschlüssel werden ausschließlich als Cloudflare-Secrets gepflegt.
