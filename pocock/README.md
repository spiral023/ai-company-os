# Privater deutscher Pocock-Kurs

Der Cloudflare Worker `sp23-pocock` liefert unter <https://pocock.sp23.online/> die deutsche Leseausgabe, 38 zugeordnete Videos, 156 Abbildungen und unter `/analyse/` die ausführliche eigene Auswertung aus. Alle Kursinhalte kommen aus dem privaten R2-Bucket `sp23-pocock-kurs`. Der Bucket hat weder eine öffentliche `r2.dev`-Adresse noch eine eigene öffentliche Domain.

## Ablage und Build

Original, vollständige Übersetzung und Medien bleiben im ignorierten lokalen [Kursarchiv](../docs/kurse/matt-pocock-software-factories/README.md). Im öffentlichen Git-Repository stehen Anwendungscode, Tests, Metadaten, eigene Auswertung und das eigens erzeugte Portrait-Icon. `content-manifest.mjs` enthält R2-Schlüssel, Größen und Prüfsummen, keine Volltexte oder Zugangsdaten.

```powershell
python -m pip install beautifulsoup4 markdown-it-py
python -X utf8 pocock/build_course.py --browser-upload
node --test pocock/tests/*.test.mjs
python -m unittest discover -s pocock/tests -p 'test_*.py' -v
```

Der Build prüft die lokale HTML-Quelle und jede Mediendatei gegen das Inventar. Er erstellt die beiden HTML-Seiten, das versionierte Inhaltsmanifest und das ignorierte `_site/upload-manifest.json`. HTML-Seiten erhalten einen gemeinsamen Release-Fingerprint; Medien tragen ihre SHA-256-Kennung im Objektnamen. Vorhandene Releases bleiben dadurch nutzbar, bis der Worker auf ein neues Manifest umgestellt wird.

`--browser-upload` erzeugt lokale Upload-Batches mit höchstens 75 Dateien. Medien sind Hardlinks, HTML-Seiten unabhängige Kopien. Im R2-Dashboard beim Datei-Upload immer das zugehörige Präfix öffnen; ein Dateiupload übernimmt nur den Dateinamen. Die Struktur unter `batch-*/kurs/` entspricht den gewünschten R2-Schlüsseln. Falls die Ordnerauswahl keine Dateien überträgt, ausdrücklich **Dateien** wählen und die einzelnen Dateien eines Batches auswählen. Das Dashboard erlaubt höchstens 100 Dateien pro Auswahl.

## Veröffentlichung

1. Build aus dem vollständigen lokalen Archiv erstellen.
2. Alle im Upload-Manifest genannten Objekte in den privaten Bucket hochladen. Ein Token mit ausschließlich Leserechten genügt dafür nicht; die bestehende Dashboard-Anmeldung kann den Upload ausführen.
3. R2-Bestand prüfen:

   ```powershell
   python -X utf8 pocock/verify_r2.py
   ```

4. Tests ausführen, Metadaten und Code committen und pushen. Der Workflow `.github/workflows/pocock.yml` testet den Worker und deployt ihn auf `main`; er benötigt die bereits verwendeten Repository-Secrets `CLOUDFLARE_API_TOKEN` und `CLOUDFLARE_ACCOUNT_ID`. Der CI-Job baut keine privaten Kursdateien und lädt keine Videos aus Git.
5. Nach dem Deployment Anmeldung, direkten Medienzugriff ohne Cookie, Analyse und Videowiedergabe einschließlich Springen prüfen.

Eine reine Codeänderung benötigt keinen erneuten Medienupload. Bei Änderungen an der Übersetzung oder Auswertung müssen die neu erzeugten HTML-Objekte vor dem Manifest-Deployment hochgeladen sein. Für eine Rückkehr zu einem älteren Release dessen Manifest und Code deployen; alte R2-Objekte nicht im selben Schritt löschen.

## Installation auf dem iPhone

1. <https://pocock.sp23.online/> in Safari öffnen.
2. **Teilen → Zum Home-Bildschirm** wählen.
3. **Als Web-App öffnen** aktivieren und **Hinzufügen** antippen.
4. Den neuen Eintrag **Pocock Kurs** öffnen und bei Bedarf mit dem bestehenden Kurs-Passwort anmelden.

Das Manifest definiert die Standalone-Ansicht, den App-Namen und Icons in 192 und 512 Pixeln. Ein Apple-Touch-Icon mit 180 Pixeln und ein mehrstufiges Favicon ergänzen die Browser-Unterstützung. Die Anmeldeseite enthält dieselbe kurze Installationshilfe; in der Standalone-Ansicht wird sie ausgeblendet. Der tatsächliche Installationsdialog liegt beim iPhone und lässt sich von der Website nicht automatisch bestätigen. [Apple-Anleitung](https://support.apple.com/guide/iphone/open-as-web-app-iphea86e5236/ios), [Installierbarkeit laut MDN](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable).

Der Kurs benötigt eine Internetverbindung. Es wird kein Service Worker registriert, und es werden keine Kursseiten oder Videos in einen Offline-Cache geschrieben. Öffentlich abrufbar und cachebar sind ausschließlich die sieben in `pwa.mjs` aufgeführten Manifest- und Icon-Dateien. `assets.run_worker_first: true` stellt sicher, dass auch diese URLs die explizite Worker-Freigabe durchlaufen; die öffentliche Ablage enthält keine Kursdateien.

Login, Kurs und Analyse referenzieren dieselben App-Metadaten. Für Kurs und Analyse ergänzt der Worker den HTML-Head nach erfolgreicher Anmeldung mit Cloudflares HTMLRewriter; die privaten R2-Originale und ihre Script-Inhalte bleiben unverändert. Diese HTML-Antworten haben weder den ETag noch die Content-Length der unveränderten Eingabedatei. Ein bytegenauer Vergleich mit dem R2-Build entfernt zunächst ausschließlich den Zusatz zwischen `<!--pocock-pwa:start-->` und `<!--pocock-pwa:end-->`. Video-Bytebereiche und ihre ETags bleiben unverändert.

Das mit Imagegen erzeugte [Icon-Original und der vollständige Prompt](assets/README.md) sind versioniert. Mit `python -m pip install pillow` und `python pocock/build_icons.py` lassen sich alle Größen reproduzieren. Das gezeichnete Portrait ist eine eigene Illustration für diesen Kurszugang und kein offizielles Autorenlogo.

## Anmeldung und Grenzen

Die Worker-Secrets `PASSWORD_VERIFIER` und `SESSION_KEY` werden direkt in Cloudflare gepflegt und nicht im Repository gespeichert. Der Passwortverifier hat das Format `pbkdf2_sha256$100000$<16-Byte-Salt als Hex>$<32-Byte-Hash als Hex>`, berechnet mit PBKDF2-HMAC-SHA256. Der Sitzungsschlüssel besteht aus mindestens 32 zufälligen Bytes. Beide Werte können über die Standardeingabe von `wrangler secret bulk` gesetzt werden; Klartextpasswort, Verifier und Sitzungsschlüssel gehören weder in Shell-History noch in Dateien oder Logs.

Ein Austausch eines dieser Secrets macht bestehende Sitzungen ungültig. Das signierte Cookie gilt acht Stunden und hat `Secure`, `HttpOnly`, `SameSite=Strict` und das `__Host-`-Präfix. Login und Logout prüfen den Origin. `Referrer-Policy: same-origin` unterbindet Referrer an fremde Websites und bewahrt den Origin nativer Form-POSTs; `no-referrer` würde diesen auf `null` setzen und die Anmeldung blockieren. Der Login nutzt Cloudflares Rate-Limit-Binding mit fünf Versuchen pro Minute und IP; dessen Zähler sind standortbezogen und näherungsweise, kein weltweites hartes Kontingent.

Auch Kursbilder, Video-Bytebereiche, HEAD- und bedingte Anfragen prüfen zuerst die Sitzung. Kursantworten sind `private, no-store`; es gibt keine öffentliche R2-Ausweichadresse. Fehlende Secrets, fehlende Objekte oder unpassende Dateigrößen führen zu einem geschlossenen Fehlerzustand. Videos werden gestreamt und unterstützen einzelne Bytebereiche für natives Springen im Player.

Das gemeinsame Passwort ist eine Zugangsschranke für diesen privaten Lesebereich. Es gibt keine Benutzerkonten, Einzelberechtigungen oder serverseitige Widerrufsliste pro Sitzung. Wer angemeldet ist, kann ausgelieferte Inhalte speichern. Lernfortschritt bleibt im Browser; die Videos wurden für die inhaltliche Auswertung nicht vollständig angesehen oder transkribiert.

Primärdokumentation: [R2 Workers API](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/), [R2-Objektliste](https://developers.cloudflare.com/api/resources/r2/subresources/buckets/subresources/objects/methods/list/), [Workers Rate Limiting](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/), [Referrer-Policy und Form-POSTs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy#effect_on_the_origin_header).
