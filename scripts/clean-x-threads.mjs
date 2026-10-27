// Bestehende X-Notizen gezielt aus ihren API-Caches bereinigen. Kein Netzwerk.
// Standard ist Vorschau; --apply schreibt nach lokaler Sicherung.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {extractTweetText, orderThreadChronologically} from './lib/x-ingest.mjs';
import {filterSourceThread,filterCachedThread,SOURCE_THREAD_POLICY} from './lib/x-thread-source.mjs';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const audit=path.join(root,`tmp/quellen-lauf/x-thread-bereinigung-${new Date().toISOString().slice(0,10)}`);
const apply=process.argv.includes('--apply');
const norm=value=>value.replace(/\r\n/g,'\n').replace(/\s+/g,' ').trim();
export function sections(text) {
  // Englische ##-Überschriften können zum Originalpost (etwa AGENTS.md) gehören.
  const headers=[...text.matchAll(/^## (Thread|Erfassungsnachweis[^\n]*|Ergänzende Thread-[^\n]*|Ergänz(?:te|ungen aus) Artikel-[^\n]*|Eingebettete Tweets|Zitierte Posts innerhalb der Einbettungen|Weitere Zitatverweise aus der API-Antwort|Archivierungsstand und Grenzen|Archivierte Bilder aus dem Thread|Folge-Post \(nachgetragen\)|Medien des geteilten Posts|Medien der Thread-Fortsetzungen)\n/gm)];
  return headers.map((match,index)=>({title:match[1].trim(),start:match.index,bodyStart:match.index+match[0].length,end:headers[index+1]?.index??text.length}));
}
export function threadBlocks(text, section) {
  const body=text.slice(section.bodyStart,section.end), headings=[...body.matchAll(/^### (\d+)\/(\d+)[^\n]*\n/gm)];
  return headings.map((match,index)=>({heading:match[0],text:body.slice(match.index+match[0].length,headings[index+1]?.index??body.length).trim()}));
}
function mediaPostId(heading) {
  const plain=heading.match(/^### (?:Post |Medien aus Post )(\d+)(?:[ \t].*)?$/);
  if(plain)return plain[1];
  const linked=heading.match(/^### \[(?:Post |Medien aus Post )(\d+)\]\((https?:\/\/[^)]+)\)(?:[ \t].*)?$/);
  const target=linked?.[2].match(/^https?:\/\/(?:www\.)?(?:x|twitter)\.com\/[^/]+\/status\/(\d+)(?:[/?#].*)?$/);
  return linked && target?.[1]===linked[1] ? linked[1] : null;
}

function cleanMediaSections(text, keep, removed, warnings) {
  // Nur Archiv-Medienabschnitte bearbeiten, nie Überschriften im Originalpost.
  const media=sections(text).filter(section=>/Medien|Bilder/.test(section.title));
  for(const section of media.reverse()) {
    const body=text.slice(section.bodyStart,section.end);
    const headings=[...body.matchAll(/^#{2,3} [^\n]+\n/gm)];
    let replacement=body.slice(0,headings[0]?.index??body.length);
    if(/!\[|<(?:video|audio)\b/.test(replacement))warnings.push(`${section.title}: Medien ohne Post-Zuordnung unverändert erhalten.`);
    for(let index=0;index<headings.length;index++) {
      const heading=headings[index];
      // Ein unbekannter Hauptabschnitt ist keine Fortsetzung des Medienblocks.
      if(heading[0].startsWith('## ')) {
        replacement+=body.slice(heading.index);
        break;
      }
      const block=body.slice(heading.index,headings[index+1]?.index??body.length);
      const id=mediaPostId(heading[0].trimEnd());
      if(id && removed.has(id))continue;
      replacement+=block;
      if(!id || !keep.has(id))warnings.push(`${section.title}: unklare Post-Zuordnung bei ${heading[0].trim()}; Medien unverändert erhalten.`);
    }
    text=text.slice(0,section.bodyStart)+replacement+text.slice(section.end);
  }
  return text;
}

export function cleanThreadNote(original, posts, selected, {warnings=[]}={}) {
  const thread=sections(original).find(section=>section.title==='Thread');
  const blocks=threadBlocks(original,thread);
  const keep=new Set(selected.thread.map(post=>post.id)), removed=new Set(selected.excluded.map(post=>post.id));
  const retained=posts.map((post,index)=>({post,block:blocks[index]})).filter(item=>keep.has(item.post.id));
  const replacement=retained.length>1?'## Thread\n\n'+retained.map((item,index)=>`### ${index+1}/${retained.length}${selected.supplements.includes(item.post.id)?' · Geprüfte Ergänzung des Autors':''}\n\n${item.block.text}\n`).join('\n')+'\n':'';
  let updated=original.slice(0,thread.start)+replacement+original.slice(thread.end);
  updated=updated.replace(/^thread_posts:\s*\d+/m,`thread_posts: ${retained.length}`);
  if(!/^thread_filter:/m.test(updated))updated=updated.replace(/^thread_methode:[^\n]*/m,match=>match+`\nthread_filter: ${SOURCE_THREAD_POLICY.version}`);
  updated=updated.split('\n').filter(line=>!/^\s*- \[Post \d+\]/.test(line)||![...removed].some(id=>line.includes(`[Post ${id}]`))).join('\n');
  updated=updated.replace(/Im API-Abruf enthalten: \d+ Post\(s\)\.[^\n]*/g,`Für diese Quelle übernommen: ${retained.length} Post(s). Gesprächsantworten außerhalb der Inhaltsauswahl wurden entfernt; dies ist kein Vollständigkeitsnachweis.`);
  updated=cleanMediaSections(updated,keep,removed,warnings);
  return updated.trimEnd()+'\n';
}

export function runCleanup() {
const cacheDir=path.join(root,'scripts/.ingest');
const caches=fs.readdirSync(cacheDir).filter(name=>name.endsWith('.json')).map(name=>{
  const file=path.join(cacheDir,name);return {file,payload:JSON.parse(fs.readFileSync(file,'utf8'))};
});
const report={policy:SOURCE_THREAD_POLICY.version,apply,notes:[],unmatched:[],cacheChanges:[],counts:{notes:0,removedPosts:0,cacheFiles:0,mediaWarnings:0}};
const planned=[];
for(const name of fs.readdirSync(path.join(root,'00_Inbox/Quellen/X')).filter(name=>name.endsWith('.md'))) {
  const file=path.join(root,'00_Inbox/Quellen/X',name), original=fs.readFileSync(file,'utf8').replace(/\r\n/g,'\n');
  const thread=sections(original).find(section=>section.title==='Thread');
  if(!thread)continue;
  const blocks=threadBlocks(original,thread);
  if(blocks.length<2)continue;
  const id=original.match(/^tweet_id:\s*["']?(\d+)/m)?.[1]??original.match(/^url:.*\/status\/(\d+)/m)?.[1];
  const candidates=caches.filter(item=>[item.payload.tweet,...(item.payload.thread??[])].some(post=>post?.id===id));
  let matched;
  for(const candidate of candidates) {
    const posts=orderThreadChronologically(candidate.payload.thread??[]);
    if(posts.length===blocks.length&&blocks.every((block,index)=>norm(block.text).startsWith(norm(extractTweetText(posts[index]))))) {matched={posts,payload:candidate.payload};break;}
  }
  if(!matched) {
    // Einzelne Notizen enthalten nur einen Ausschnitt einer größeren Cache-Kette.
    const posts=new Map(candidates.flatMap(item=>[item.payload.tweet,...(item.payload.thread??[])]).filter(Boolean).map(post=>[post.id,post]));
    const mapped=blocks.map(block=>[...posts.values()].filter(post=>norm(extractTweetText(post))===norm(block.text)));
    if(mapped.every(list=>list.length===1)&&new Set(mapped.map(list=>list[0].id)).size===blocks.length)matched={posts:mapped.map(list=>list[0]),payload:candidates[0].payload};
  }
  const anchor=matched?.posts.find(post=>post.id===id)??(matched?.payload.tweet.id===id?matched.payload.tweet:null);
  if(!matched||!anchor) {report.unmatched.push({file:path.relative(root,file),id,posts:blocks.length});continue;}
  const selected=filterSourceThread(anchor,matched.posts);
  if(!selected.excluded.length&&!selected.supplements.length)continue;
  const warnings=[];
  const updated=cleanThreadNote(original,matched.posts,selected,{warnings});
  if(updated===original)continue;
  const removedPosts=matched.posts.filter(post=>selected.excluded.some(item=>item.id===post.id)).map(post=>({id:post.id,text:extractTweetText(post),reason:selected.excluded.find(item=>item.id===post.id).reason}));
  report.notes.push({file:path.relative(root,file),id,before:blocks.length,after:selected.thread.length,
    supplements:selected.supplements,removed:removedPosts,warnings,source:original.match(/^source_notiz:\s*(.+)$/m)?.[1]??''});
  planned.push({file,updated});
  report.counts.notes+=1;report.counts.removedPosts+=removedPosts.length;
  report.counts.mediaWarnings+=warnings.length;
}
for(const item of caches) {
  const filtered=filterCachedThread(item.payload);
  if(!filtered.excluded.length)continue;
  report.cacheChanges.push({file:path.relative(root,item.file),before:item.payload.thread.length,after:filtered.payload.thread.length,removed:filtered.excluded});
  planned.push({file:item.file,updated:JSON.stringify(filtered.payload,null,2)+'\n'});
  report.counts.cacheFiles+=1;
}
fs.mkdirSync(audit,{recursive:true});
if(apply) {
  for(const item of planned) {
    const backup=path.join(audit,'backups',path.relative(root,item.file));
    if(!fs.existsSync(backup)){fs.mkdirSync(path.dirname(backup),{recursive:true});fs.copyFileSync(item.file,backup);}
    fs.writeFileSync(item.file,item.updated,'utf8');
  }
}
fs.writeFileSync(path.join(audit,apply?'applied.json':'plan.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({mode:apply?'apply':'preview',...report.counts,unmatched:report.unmatched.length,report:path.relative(root,audit)},null,2));
return report;
}
if(process.argv[1] && path.resolve(process.argv[1])===fileURLToPath(import.meta.url))runCleanup();
