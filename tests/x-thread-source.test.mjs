import test from 'node:test';
import assert from 'node:assert/strict';
import {formatInboxNote} from '../scripts/lib/inbox-store.mjs';
import {filterSourceThread, filterCachedThread} from '../scripts/lib/x-thread-source.mjs';
import {cleanThreadNote, sections, threadBlocks} from '../scripts/clean-x-threads.mjs';

const root={id:'1',author_id:'a',conversation_id:'1',text:'Useful original article',created_at:'2026-10-22T10:00:00Z'};
test('Gesprächsantwort des Autors wird nicht als Artikel-Fortsetzung archiviert',()=>{
  const reply={id:'3',author_id:'a',conversation_id:'1',text:"@Serocu You're welcome! Let me know how it worked for you.",referenced_tweets:[{type:'replied_to',id:'2'}]};
  const note=formatInboxNote({tweet:root,author:{id:'a',username:'original',name:'Original'},slug:'test',thread:[root,reply],fetchedAt:'2026-10-25T00:00:00Z'});
  assert.ok(!note.includes("@Serocu You're welcome!"));
});

const reply=(id,parent,text='Inhaltliche Fortsetzung',author='a')=>({id,author_id:author,text,referenced_tweets:[{type:'replied_to',id:parent}]});
test('Echte Selbst-Antwortkette bleibt auch bei Einstieg über den letzten Post erhalten',()=>{
  const middle=reply('2','1','@reader Hier folgt der vollständige technische Ablauf.');
  const end=reply('4','2');
  const foreign=reply('3','1','Fremder Kommentar','b');
  const qa=reply('5','3','Danke für die Rückfrage');
  const result=filterSourceThread(end,[qa,end,foreign,middle,root]);
  assert.equal(result.anchor.id,'1');
  assert.deepEqual(result.thread.map(t=>t.id),['1','2','4']);
  assert.deepEqual(result.excluded.map(t=>t.id),['3','5']);
});
test('Explizit angefragte Antwort bleibt eigenständige Quelle ohne fremde Vorgänger',()=>{
  const foreign={...root,author_id:'b'};
  const own=reply('2','1','Eigenständige fachliche Aussage');
  assert.deepEqual(filterSourceThread(own,[foreign,own]).thread.map(t=>t.id),['2']);
});
test('Reine Werbung und deren Folgeantworten werden entfernt, fachlicher Inhalt bleibt',()=>{
  const ad=reply('2','1',"I've posted a refined v2. Follow for more updates!");
  const child=reply('3','2');
  const useful=reply('4','1','Follow the data from user input to database writes; verify authorization at each boundary.');
  const result=filterSourceThread(root,[root,ad,child,useful]);
  assert.deepEqual(result.thread.map(t=>t.id),['1','4']);
});
test('Fehlende Autor- und Antwortmetadaten reichen nicht als Thread-Nachweis',()=>{
  const unknown={id:'2',text:'Nicht verifizierbar'};
  const quote={id:'3',author_id:'a',text:'Zitat',referenced_tweets:[{type:'quoted',id:'1'}]};
  assert.deepEqual(filterSourceThread(root,[root,unknown,quote]).thread.map(t=>t.id),['1']);
});
test('Geprüfte Ergänzung wird einzeln übernommen und gekennzeichnet',()=>{
  const supplement=reply('3','2','Nützliche fachliche Einschränkung');
  const child=reply('4','3','Weitere Gesprächsantwort');
  const policy={version:'test',supplements:{'1':['3']}};
  const result=filterSourceThread(root,[root,supplement,child],policy);
  assert.deepEqual(result.thread.map(t=>t.id),['1','3']);
  assert.deepEqual(result.supplements,['3']);
});
test('Cache-Filter ist bei erneutem Import idempotent',()=>{
  const payload={tweet:root,thread:[root,reply('2','9','Gesprächsantwort')]};
  const once=filterCachedThread(payload);
  const twice=filterCachedThread(once.payload);
  assert.deepEqual(twice.payload,once.payload);
  assert.equal(twice.excluded.length,0);
  assert.equal(once.payload.threadFiltered,1);
});
test('Cache-Einstieg über eine geprüfte Ergänzung behält den redaktionellen Quellenanker',()=>{
  const supplement=reply('3','2','Fachliche Ergänzung');
  const foreign=reply('2','1','Fremde Zwischenfrage','b');
  const policy={version:'test',supplements:{'1':['3']}};
  const payload=filterCachedThread({tweet:supplement,thread:[root,foreign,supplement]},policy).payload;
  assert.deepEqual(payload.thread.map(post=>post.id),['1','3']);
  assert.deepEqual(filterCachedThread(payload,policy).payload,payload);
});
test('Archivbereinigung erhält Status, Original-Überschriften und manuelle Ergänzungen',()=>{
  const second=reply('2','1','# AGENTS.md\n\n## Ground rules\nKeep the source intact.');
  const noise=reply('3','9','@user Danke!');
  const note='---\nstatus: verarbeitet\nsource_notiz: 80_Knowledge/Sources/test.md\nthread_posts: 3\nthread_methode: recent-search\n---\n\n## Post-Text\n\nUseful original article\n\n## Thread\n\n### 1/3\n\nUseful original article\n\n### 2/3\n\n'+second.text+'\n\n### 3/3\n\n'+noise.text+'\n\n## Erfassungsnachweis\n\nIm API-Abruf enthalten: 3 Post(s). Kein Vollständigkeitsnachweis.\n- [Post 1](https://x.com/a/status/1)\n- [Post 3](https://x.com/a/status/3)\n\n## Ergänzende Thread-Medien\n\n### Post 2\n\n![gut](local.png)\n\n### Post 3\n\n![noise](noise.png)\n\n## Archivierungsstand und Grenzen\n\nManueller Archivierungshinweis.\n';
  const posts=[root,second,noise], selected=filterSourceThread(root,posts);
  const result=cleanThreadNote(note,posts,selected);
  assert.match(result,/status: verarbeitet\nsource_notiz: 80_Knowledge\/Sources\/test.md/);
  assert.match(result,/thread_posts: 2/);
  assert.match(result,/### 2\/2\n\n# AGENTS.md\n\n## Ground rules/);
  assert.match(result,/!\[gut\]\(local.png\)/);
  assert.match(result,/Manueller Archivierungshinweis/);
  assert.doesNotMatch(result,/@user Danke|Post 3|noise.png/);
  assert.equal(threadBlocks(result,sections(result).find(s=>s.title==='Thread')).length,2);
  assert.equal(cleanThreadNote(result,[root,second],selected),result);
});

test('Medien der Thread-Fortsetzungen bleiben unabhängig vom letzten entfernten Post',()=>{
  const second=reply('2','1','Technische Fortsetzung');
  const noise=reply('3','9','Gesprächsantwort');
  const posts=[root,second,noise], selected=filterSourceThread(root,posts);
  const note='---\nstatus: verarbeitet\nsource_notiz: 80_Knowledge/Sources/test.md\nthread_posts: 3\nthread_methode: recent-search\n---\n\n## Thread\n\n### 1/3\n\n'+root.text+'\n\n### 2/3\n\n'+second.text+'\n\n### 3/3\n\n'+noise.text+'\n\n## Medien der Thread-Fortsetzungen\n\n### [Post 2](https://x.com/a/status/2)\n\n![gültiges Chart](chart.png)\n\n### [Post 3](https://x.com/a/status/3)\n\n![Gesprächsbild](noise.png)\n\n### Ohne belegte Post-Zuordnung\n\n![manuelles Bild](unknown.png)\n\n## Archivierungsstand und Grenzen\n\nManueller Hinweis.\n';
  const warnings=[];
  const result=cleanThreadNote(note,posts,selected,{warnings});
  assert.match(result,/chart\.png/);
  assert.doesNotMatch(result,/noise\.png|Gesprächsantwort/);
  assert.match(result,/unknown\.png/);
  assert.match(result,/Manueller Hinweis/);
  assert.match(result,/status: verarbeitet\nsource_notiz: 80_Knowledge\/Sources\/test.md/);
  assert.equal(warnings.length,1);
  assert.match(warnings[0],/Zuordnung/);
  assert.equal(cleanThreadNote(result,[root,second],selected),result);
});

test('Widersprüchliche Medien-IDs werden erhalten und zur Prüfung gemeldet',()=>{
  const noise=reply('3','9','Gesprächsantwort');
  const posts=[root,noise], selected=filterSourceThread(root,posts);
  const note='---\nthread_posts: 2\nthread_methode: recent-search\n---\n\n## Thread\n\n### 1/2\n\n'+root.text+'\n\n### 2/2\n\n'+noise.text+'\n\n## Medien der Thread-Fortsetzungen\n\n### [Post 3](https://x.com/a/status/1)\n\n![unklare Zuordnung](keep.png)\n';
  const warnings=[];
  const result=cleanThreadNote(note,posts,selected,{warnings});
  assert.match(result,/keep\.png/);
  assert.equal(warnings.length,1);
});
