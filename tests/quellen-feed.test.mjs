import test from 'node:test';
import assert from 'node:assert/strict';
import {normalize,dateOf,selectEntries,readState,matchingView,defaultView,topicState,relatedEntries,parseLibrary,togglePersonal} from '../70_Scripts/quellen_feed/model.mjs';
const state={q:'',platform:'',author:'',topic:'',status:'',month:'',sort:'published'};
const entry=(id,published,captured,overrides={})=>({id,published,captured,authors:['vox'],topics:['skills'],statuses:['ignoriert'],platform:'X',searchNormalized:normalize('Originaltext über größere KI Fähigkeiten'),...overrides});
const entries=[entry('old','2026-01-01','2026-10-24'),entry('new','2026-10-22','2026-10-23'),entry('unknown','','2026-10-21')];
test('Originaldatum und Erfassung ergeben unterschiedliche Reihenfolgen',()=>{
  assert.deepEqual(selectEntries(entries,state).map(x=>x.id),['new','unknown','old']);
  assert.deepEqual(selectEntries(entries,{...state,sort:'captured'}).map(x=>x.id),['old','new','unknown']);
  assert.equal(dateOf(entries[2],'published'),'2026-10-21');
});
test('Alle Status sind standardmäßig sichtbar; Filter kombinieren sich',()=>{
  const sample=[...entries,entry('other','2026-10-23','2026-10-24',{platform:'TikTok',authors:['james'],statuses:['verarbeitet']})];
  assert.equal(selectEntries(sample,state).length,4);
  assert.equal(selectEntries(sample,{...state,platform:'X',author:'vox',topic:'skills',status:'ignoriert',month:'2026-10',q:'grossere fahigkeiten'}).length,2);
  assert.equal(selectEntries(sample,{...state,q:'nichtvorhanden'}).length,0);
});
test('URL-Filter akzeptieren nur bekannte Auswahlwerte',()=>{
  const valid={platform:new Set(['X']),author:new Set(['vox']),topic:new Set(),status:new Set(['ignoriert']),month:new Set(['2026-10'])};
  const parsed=readState(new URLSearchParams('platform=X&author=unknown&topic=bad&sort=evil&status=ignoriert&q=KI'),valid);
  assert.deepEqual(parsed,{q:'KI',sort:'published',platform:'X',author:'',topic:'',status:'ignoriert',month:'',library:''});
});
test('Leseposition auch für gefilterte URLs wiederherstellen, fremde Links ausnehmen',()=>{
  const saved={query:'q=KI&author=vox',shown:24,scroll:1800};
  assert.equal(matchingView(new URLSearchParams('author=vox&q=KI'),saved,false),saved);
  assert.equal(matchingView(new URLSearchParams('author=other&q=KI'),saved,false),null);
  assert.equal(matchingView(new URLSearchParams('author=vox&q=KI'),saved,true),null);
});
test('Aufarbeitung ist Standard, unverarbeitete Quellen bleiben als Original sichtbar',()=>{
  assert.equal(defaultView({has_source:true}),'source');
  assert.equal(defaultView({has_source:false}),'original');
});
test('Themenlink zeigt auch andere Autoren und Plattformen statt versteckt leer zu filtern',()=>{
  assert.deepEqual(topicState({...state,q:'abc',author:'vox',platform:'X',month:'2026-10',status:'verarbeitet',sort:'captured',library:'saved'},'skills'),{q:'',platform:'',author:'',topic:'skills',month:'',status:'',library:'',sort:'captured'});
});

test('Persönliche Listen unterscheiden gespeicherte, später zu lesende und gelesene Quellen',()=>{
  const library={old:{saved:true,read:false},new:{saved:true,read:true}};
  assert.deepEqual(selectEntries(entries,{...state,library:'saved'},library).map(e=>e.id),['new','old']);
  assert.deepEqual(selectEntries(entries,{...state,library:'later'},library).map(e=>e.id),['old']);
  assert.deepEqual(selectEntries(entries,{...state,library:'read'},library).map(e=>e.id),['new']);
  assert.equal(entries[0].statuses[0],'ignoriert');
  const changed=togglePersonal(library,'new','saved');
  assert.deepEqual(changed.new,{saved:false,read:true});
  assert.deepEqual(library.new,{saved:true,read:true});
});
test('Beschädigter Browserspeicher verhindert nicht den Start und akzeptiert nur gültige Leseflags',()=>{
  assert.deepEqual(parseLibrary('kaputt'),{});
  assert.deepEqual(parseLibrary('{"version":2,"entries":{}}'),{});
  assert.deepEqual(parseLibrary(JSON.stringify({version:1,entries:{'1234567890abcdef':{saved:true,read:'false'},invalid:{saved:true}}})),{'1234567890abcdef':{saved:true,read:false}});
});
test('Alte Autorenlinks werden auf die bestätigte Identität abgebildet; Leselisten aus URLs validieren',()=>{
  const valid={platform:new Set(),author:new Set(['boris-cherny']),authorAliases:{'X:bcherny':'boris-cherny'},topic:new Set(),status:new Set(),month:new Set()};
  const selected=readState(new URLSearchParams('author=X%3Abcherny&library=later'),valid);
  assert.equal(selected.author,'boris-cherny');assert.equal(selected.library,'later');
  assert.equal(readState(new URLSearchParams('library=arbitrary'),valid).library,'');
});
test('Verbindungen erfordern gemeinsame Themen und priorisieren gemeinsame Hauptthemen',()=>{
  const source={...entry('self','2026-10-22','2026-10-24'),main_topics:['skills'],keywords:['Agent']};
  const otherMain={...entry('main','2026-01-01','2026-10-24'),main_topics:['skills'],keywords:[]};
  const otherSide={...entry('side','2026-10-23','2026-10-24'),main_topics:['review'],keywords:[]};
  const unrelated={...entry('wrong','2026-10-24','2026-10-24'),topics:['review'],keywords:['Agent']};
  const result=relatedEntries(source,[source,otherSide,unrelated,otherMain]);
  assert.deepEqual(result.map(item=>item.entry.id),['main','side']);
  assert.deepEqual(result[0].shared,['skills']);
});
