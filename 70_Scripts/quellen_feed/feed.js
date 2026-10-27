import {normalize, dateOf, selectEntries, readState, matchingView, defaultView, topicState, relatedEntries,parseLibrary,togglePersonal,matchesLibrary} from './model.mjs';
import {createViewer} from './viewer.mjs';

const $ = id => document.getElementById(id);
const esc = value => String(value ?? '').replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
const external = (url, label = 'Original öffnen ↗', className = '') => url ? `<a class="${className}" href="${esc(url)}" target="_blank" rel="noopener noreferrer"${className === 'external' ? ' aria-label="Originalquelle öffnen"' : ''}>${label}</a>` : '';
const dayFormat = new Intl.DateTimeFormat('de-AT', {day:'numeric',month:'long',year:'numeric'});
const shortFormat = new Intl.DateTimeFormat('de-AT', {day:'2-digit',month:'2-digit',year:'numeric'});
const formatDate = (date, long = false) => date ? (long ? dayFormat : shortFormat).format(new Date(`${date}T12:00:00`)) : 'Datum unbekannt';
const PAGE_SIZE = 12;
let data, state, filtered = [], shown = 0, details = new Map(), xScript;
let filterTimer, currentSource = '', restorePosition = null;
let personal={}, viewer, statusTimer;
const libraryNames={later:'Später lesen',saved:'Merkliste',read:'Gelesen'};
const topicCounts=new Map(), relatedCache=new Map();
const storage = {
  get(key) {try {return localStorage.getItem(`quellenfeed-${key}`);} catch {return null;}},
  set(key,value) {try {localStorage.setItem(`quellenfeed-${key}`,value);return true;} catch {return false;}}
};

function personalControls(entry) {
  const item=personal[entry.id]||{};
  return `<button data-personal="saved" data-entry="${entry.id}" aria-pressed="${!!item.saved}" aria-label="${item.saved?'Nicht mehr merken':'Für später merken'}" title="${item.saved?'Nicht mehr merken':'Für später merken'}">${item.saved?'★ Gemerkt':'☆ Merken'}</button><button data-personal="read" data-entry="${entry.id}" aria-pressed="${!!item.read}" aria-label="${item.read?'Als ungelesen markieren':'Als gelesen markieren'}" title="${item.read?'Als ungelesen markieren':'Als gelesen markieren'}">${item.read?'✓ Gelesen':'○ Als gelesen markieren'}</button>`;
}
function syncPersonal() {
  document.querySelectorAll('[data-personal]').forEach(button=>{
    const item=personal[button.dataset.entry]||{}, active=!!item[button.dataset.personal], saved=button.dataset.personal==='saved';
    button.setAttribute('aria-pressed',active);
    button.textContent=saved?(active?'★ Gemerkt':'☆ Merken'):(active?'✓ Gelesen':'○ Als gelesen markieren');
    button.title=saved?(active?'Nicht mehr merken':'Für später merken'):(active?'Als ungelesen markieren':'Als gelesen markieren');
    button.setAttribute('aria-label',button.title);
  });
  document.querySelectorAll('.card').forEach(card=>card.dataset.read=!!personal[card.dataset.id]?.read);
  document.querySelectorAll('[data-library]').forEach(button=>button.setAttribute('aria-pressed',state.library===button.dataset.library));
  $('all-sources').setAttribute('aria-pressed',!state.library);
  document.querySelectorAll('[data-library-count]').forEach(node=>node.textContent=data.entries.filter(entry=>matchesLibrary(entry,node.dataset.libraryCount,personal)).length);
}
function updatePersonal(entry,field) {
  const before=filtered.findIndex(item=>item.id===entry.id), oldShown=shown, oldScroll=window.scrollY;
  personal=togglePersonal(personal,entry.id,field);
  const persisted=storage.set('library',JSON.stringify({version:1,entries:personal}));
  if(!matchesLibrary(entry,state.library,personal)) {
    render();if(oldShown>shown)appendPage(Math.min(oldShown,filtered.length));
    window.scrollTo({top:oldScroll,behavior:'instant'});
    if(!$('viewer').open){const next=filtered[Math.min(Math.max(before,0),filtered.length-1)];(next?document.getElementById(`quelle-${next.id}`)?.querySelector(`[data-personal="${field}"]`):$('search'))?.focus({preventScroll:true});}
  }
  syncPersonal();
  clearTimeout(statusTimer);
  $('library-status').textContent=persisted?(field==='saved'?(personal[entry.id].saved?'In der Merkliste gespeichert.':'Aus der Merkliste entfernt.'):(personal[entry.id].read?'Als gelesen markiert.':'Als ungelesen markiert.')):'Nur für diese Sitzung gespeichert: Der Browserspeicher ist nicht verfügbar.';
  viewer.announce($('library-status').textContent);
  if(persisted)statusTimer=setTimeout(()=>{$('library-status').textContent='';viewer.announce('');},5000);
}

function initials(name) {return name.replace(/^@/, '').split(/[\s_-]+/).slice(0,2).map(x=>x[0] || '').join('').toUpperCase();}
function avatar(name, authorId) {const src=data.author_images?.[authorId];return `<span class="avatar" aria-hidden="true"><span>${esc(initials(name))}</span>${src ? `<img src="${esc(src)}" alt="" width="35" height="35" loading="lazy" decoding="async">` : ''}</span>`;}
function authorLink(label, entry) {return entry.profile_url ? `<a class="author-profile-link" href="${esc(entry.profile_url)}" target="_blank" rel="noopener noreferrer" title="Profil von ${esc(entry.author)} öffnen">${esc(label)}</a>` : esc(label);}
function topicLink(topic, counted=false) {
  const name=data.topics[topic] || topic;
  const query=new URLSearchParams({topic});if(state?.sort==='captured')query.set('sort','captured');
  return `<a class="topic-tag topic-link" href="?${query}" data-topic-link="${esc(topic)}" title="Weitere Quellen zum Thema ${esc(name)}">${esc(name)}${counted ? `<span class="topic-count">${topicCounts.get(topic)||0}</span>` : ''}</a>`;
}
function topicTags(entry, counted=false) {return entry.topics.map(t=>topicLink(t,counted)).join('');}
function connections(entry) {
  if(!entry.topics.length)return '';
  if(!relatedCache.has(entry.id))relatedCache.set(entry.id,relatedEntries(entry,data.entries));
  const related=relatedCache.get(entry.id);
  if(!related.length)return '';
  const link=item=>`<a class="related-source" href="#quelle=${item.entry.id}" title="${esc((item.sharedMain.length?'Gemeinsames Hauptthema: ':'Gemeinsames Thema: ')+item.shared.map(t=>data.topics[t]||t).join(' · '))}"><strong>${esc(item.entry.source_title || item.entry.title)}</strong><span>${esc(item.entry.author)} · ${esc(item.entry.platform)} · <small>${esc(data.topics[item.sharedMain[0]||item.shared[0]])}</small></span></a>`;
  return `<section class="connections" aria-label="Verbindungen dieser Quelle"><h3>Passend dazu</h3>${related.slice(0,2).map(link).join('')}${related.length>2?`<details class="more-connections"><summary>Weitere Verbindung</summary>${related.slice(2).map(link).join('')}</details>`:''}</section>`;
}
function info(entry) {
  return `<dl class="source-info"><dt>Thema</dt><dd class="topic-tags">${topicTags(entry) || 'Ohne Zuordnung'}</dd><dt>Veröffentlicht</dt><dd>${formatDate(entry.published)}${entry.uncertain_date ? ' · unsicher' : ''}</dd><dt>Erfasst</dt><dd>${formatDate(entry.captured)}</dd>${entry.segment ? `<dt>Ausschnitt</dt><dd>${esc(entry.segment)}</dd>` : ''}<dt>Quelle</dt><dd>${external(entry.url) || 'Lokal archiviert'}</dd></dl>`;
}
function placeholder(entry) {
  const poster = entry.media.find(m=>m.kind === 'image');
  return `<div class="embed-placeholder${entry.shorts || entry.platform === 'TikTok' ? ' portrait-frame' : ''}">${poster ? `<img src="${poster.src}" alt="${esc(poster.alt)}" loading="lazy">` : ''}<button class="play-button" data-action="embed"><span class="play-triangle" aria-hidden="true">▶</span> ${esc(entry.platform)}-Video laden</button><strong>${esc(entry.title)}</strong><p>Originalvideo direkt im Feed ansehen.</p></div>`;
}
function localVideo(entry, video) {
  const poster = entry.media.find(m=>m.kind === 'image');
  return `<div class="video-slot"><video class="local-video" controls playsinline preload="none" src="${video.src}"${poster ? ` poster="${poster.src}"` : ''} aria-label="${esc(entry.title)}"></video><div class="video-caption">Originalvideo aus dem Archiv${entry.platform === 'TikTok' && entry.video_id ? ' · <button data-action="embed">TikTok-Player laden</button>' : ''}</div></div>`;
}
function preview(entry) {
  if (!entry.preview_html) return `<p class="muted small">Kein Originaltext archiviert. ${entry.has_transcript ? 'Das erfasste Transkript findest du im Reiter „Transkript“.' : 'Die Originalquelle lässt sich über den Link öffnen.'}</p>`;
  return `<div class="preview prose">${entry.preview_html}</div><button class="read-more" data-action="expand">Vollständigen Inhalt lesen ↓</button>`;
}
function gallery(entry) {
  const images = entry.media.filter(m=>m.kind === 'image'), first=images[0];
  return images.length ? `<div class="gallery"><button class="gallery-cover" data-action="gallery" aria-label="${images.length} ${images.length===1?'Bild':'Bilder'} öffnen"><img src="${first.src}" alt="${esc(first.alt)}" loading="lazy" decoding="async" width="${first.width}" height="${first.height}"><span>${images.length>1?`+${images.length-1} Bilder`:'Bild vergrößern'} ↗</span></button></div>` : '';
}
function original(entry, companion=false) {
  const video = entry.media.find(m=>m.kind === 'video');
  const label = `<p class="content-label">${esc(entry.original_label)}</p>`;
  const note = !companion && entry.has_source ? `<button class="source-note" data-action="source"><strong>↳ Deutsche Aufarbeitung</strong><span>${esc(entry.source_title || entry.title)}</span></button>` : '';
  const warning = entry.translated ? `<p class="notice" lang="de">${esc(entry.translation_notice)}</p>` : entry.secondary ? '<div class="notice">Dieser Archiveintrag enthält eine ältere Aufarbeitung. Ein Originaltext ist hier nicht separat archiviert; die Originalquelle bleibt über den Link erreichbar.</div>' : '';
  let content;
  if (entry.platform === 'TikTok' && (video || entry.video_id)) {
    content = companion ? `${video ? localVideo(entry,video) : `<div class="video-slot">${placeholder(entry)}</div>`}<details class="thread-section"><summary>Original-Caption und Quelldetails</summary>${label}${preview(entry)}${info(entry)}</details>` : `<div class="content-row">${video ? localVideo(entry,video) : `<div class="video-slot">${placeholder(entry)}</div>`}<div class="content-context">${label}${preview(entry)}${info(entry)}${note}</div></div>`;
  } else if (entry.platform === 'YouTube' && entry.video_id) {
    content = `${placeholder(entry)}<div class="card-actions"><span class="muted small">${entry.segment ? `Ausschnitt ab ${Math.floor(entry.start/3600)}:${String(Math.floor(entry.start%3600/60)).padStart(2,'0')}:${String(entry.start%60).padStart(2,'0')}` : 'Originalvideo · YouTube'}</span>${external(entry.url)}</div><details class="thread-section"><summary>Originalbeschreibung und Quelldetails</summary>${label}${preview(entry)}${info(entry)}</details>`;
  } else {
    const pdf = entry.media.find(m=>m.kind === 'pdf');
    content = `${label}${preview(entry)}${pdf ? `<p>${external(pdf.src, 'Original-PDF öffnen ↗','source-link')}</p>` : ''}${gallery(entry)}${video ? localVideo(entry, video) : ''}<div class="card-actions"><span class="topic-tags">${topicTags(entry)}</span><span>${entry.platform === 'X' && entry.url && !entry.translated ? '<button class="read-more" data-action="embed">Originalpost einbetten</button>' : external(entry.url)}</span></div>`;
  }
  if (entry.thread_posts > 1) content += `<details class="thread-section" data-thread><summary>${entry.thread_posts} Quellenposts ansehen</summary><p class="muted small">Hauptpost und Fortsetzungen des Autors; einzeln geprüfte fachliche Ergänzungen sind gekennzeichnet. Die Anzahl belegt keine vollständige Erfassung.</p><div class="thread-content prose"></div></details>`;
  return warning + content;
}
function card(entry) {
  const view=defaultView(entry);
  const tabs=[...(entry.has_source ? [['source','Aufarbeitung']] : []),['original','Original'],...(entry.has_transcript ? [['transcript','Transkript']] : []),['archive','Archivfassung']];
  const headerDate=entry.published || entry.captured;
  const handle=entry.handle && normalize(entry.handle)!==normalize(entry.author) ? `<span>${authorLink(entry.handle,entry)}</span><span>·</span>` : '';
  const title=entry.source_title || entry.title;
  const avatarHtml=entry.profile_url ? `<a class="avatar-profile-link" href="${esc(entry.profile_url)}" target="_blank" rel="noopener noreferrer" aria-label="Profil von ${esc(entry.author)} öffnen">${avatar(entry.author,entry.authors[0])}</a>` : avatar(entry.author,entry.authors[0]);
  return `<article class="card" id="quelle-${entry.id}" data-id="${entry.id}" data-kind="${esc(entry.platform)}" data-read="${!!personal[entry.id]?.read}" aria-label="${esc(title)}">
    <header class="card-header">${avatarHtml}<div><div class="card-author">${authorLink(entry.author,entry)}</div><div class="card-meta">${handle}<span class="platform-icon">${esc(entry.platform)}</span><span>·</span><time datetime="${headerDate}">${formatDate(headerDate)}</time>${entry.uncertain_date ? '<span>Datum unsicher</span>' : ''}</div></div>${external(entry.url,'↗','external')}</header>
    ${entry.show_title ? `<h2 class="card-title">${esc(title)}</h2>` : ''}
    ${entry.topics.length ? `<nav class="entry-topics topic-tags" aria-label="Themen dieser Quelle">${topicTags(entry,true)}</nav>` : ''}
    <div class="tabbar" role="tablist" aria-label="Quellenansicht">${tabs.map(([id,name])=>`<button class="tab-button" id="tab-${entry.id}-${id}" role="tab" aria-selected="${id===view}" aria-controls="${id==='original'?'original':'panel'}-${entry.id}" tabindex="${id===view ? '0' : '-1'}" data-tab="${id}">${name}</button>`).join('')}<span class="status-badge" title="Status der Quellenverarbeitung im Wissensarchiv">${entry.statuses.map(esc).join(' / ')}</span></div>
    <div class="reading-layout" data-view="${view}">
      <div class="panel prose" id="panel-${entry.id}" role="tabpanel" aria-labelledby="tab-${entry.id}-${view}"${view==='original'?' hidden':''}></div>
      <div class="original-body" id="original-${entry.id}"${entry.display_language?` lang="${esc(entry.display_language)}"`:''} role="${view==='source'?'region':'tabpanel'}" ${view==='source'?'aria-label="Originalquelle neben der Aufarbeitung"':`aria-labelledby="tab-${entry.id}-original"`}>${original(entry,view==='source')}</div>
    </div>
    <footer class="personal-actions">${entry.has_source||entry.preview_html||entry.has_transcript?'<button data-action="reader">Lesemodus ↗</button>':''}${personalControls(entry)}</footer>
    ${!entry.has_source ? '<p class="muted small unprocessed-note">Für diese Quelle liegt noch keine Aufarbeitung vor.</p>' : ''}
  </article>`;
}
function entryFor(element) {return data.entries.find(e=>e.id === element.closest('[data-id]')?.dataset.id);}
async function loadDetails(entry) {
  if (!details.has(entry.id)) details.set(entry.id, fetch(`data/${entry.id}.json`).then(r=>{if(!r.ok)throw Error('Quelldetails nicht erreichbar');return r.json();}).catch(error=>{details.delete(entry.id);throw error;}));
  return details.get(entry.id);
}
async function switchTab(article, tab) {
  const entry=entryFor(article), panel=article.querySelector('.panel'), body=article.querySelector('.original-body'), layout=article.querySelector('.reading-layout');
  const previous=layout.dataset.view;
  const focusFromBody=body.contains(document.activeElement);
  article.querySelectorAll('[role=tab]').forEach(button=>{const active=button.dataset.tab===tab;button.setAttribute('aria-selected',active);button.tabIndex=active?0:-1;});
  if(previous!==tab){
    article.querySelectorAll('video').forEach(video=>video.pause());
    if(tab==='source'||tab==='original'||article.dataset.embedLoaded){body.innerHTML=original(entry,tab==='source');delete article.dataset.embedLoaded;setupVideos();}
  }
  layout.dataset.view=tab;
  body.hidden=!['source','original'].includes(tab);
  body.setAttribute('role',tab==='source'?'region':'tabpanel');
  if(tab==='source'){body.removeAttribute('aria-labelledby');body.setAttribute('aria-label','Originalquelle neben der Aufarbeitung');}
  else{body.removeAttribute('aria-label');body.setAttribute('aria-labelledby',`tab-${entry.id}-original`);}
  if(focusFromBody)article.querySelector(`[data-tab="${tab}"]`).focus();
  panel.hidden=tab==='original';panel.setAttribute('aria-labelledby',`tab-${entry.id}-${tab}`);
  if(tab==='original')return;
  if(tab==='source') {
    panel.innerHTML=`<p class="content-label">${esc(entry.summary_label||'Deutsche Aufarbeitung')}</p><div class="source-copy is-summary">${entry.summary_html||'<p>Die vollständige Aufarbeitung ist im Lesemodus verfügbar.</p>'}</div><button class="read-more" data-action="source-expand" aria-expanded="false">Aufarbeitung weiterlesen ↓</button>${connections(entry)}`;
    return;
  }
  panel.textContent='Inhalt wird geladen …';
  try {
    const content=await loadDetails(entry);
    if(article.querySelector('[aria-selected=true]').dataset.tab!==tab)return;
    {
      const notice=tab==='transcript'?`<div class="notice"><strong>Erfasstes Transkript · ${esc(content.transcript_info)}</strong>${esc(content.transcript_warning)}</div>`:`<p class="content-label">${entry.versions>1?`${entry.versions} archivierte Fassungen derselben Originalquelle`:'Gespeicherte Archivfassung'}</p>`;
      panel.innerHTML=notice+(content[`${tab}_html`]||'<p>Kein Inhalt vorhanden.</p>');
    }
  }catch{panel.innerHTML='<p class="error-message">Inhalt konnte nicht geladen werden. Bitte den lokalen Server prüfen und den Reiter erneut öffnen.</p>';}
}
function syncControls() {
  $('search').value = state.q;
  for(const key of ['author','topic','month','status','sort']) $(key).value = state[key];
  document.querySelectorAll('[data-platform]').forEach(button=>button.setAttribute('aria-pressed',button.dataset.platform === state.platform));
  document.querySelectorAll('[data-author]').forEach(button=>button.setAttribute('aria-pressed',button.dataset.author === state.author));
  document.querySelectorAll('[data-topic]').forEach(button=>button.setAttribute('aria-pressed',button.dataset.topic === state.topic));
  const names = {platform:state.platform,author:data.authors[state.author],topic:data.topics[state.topic],month:state.month,status:state.status,library:libraryNames[state.library],q:state.q ? `Suche: ${state.q}` : ''};
  $('active-filters').innerHTML=Object.entries(names).filter(([key,value])=>state[key] && value).map(([key,value])=>`<button class="filter-chip" data-clear="${key}" aria-label="Filter entfernen: ${esc(value)}">${esc(value)} ×</button>`).join('');
  const overview=$('topic-overview');overview.hidden=!state.topic;
  const topic=data.topic_details?.[state.topic]||{};
  $('page-title').textContent=state.topic?data.topics[state.topic]:libraryNames[state.library]||'Quellenfeed';
  $('page-eyebrow').textContent=state.topic?'Themenbibliothek':state.library?'Deine Leselisten':'Deine Quellenbibliothek';
  $('page-intro').textContent=state.topic?(topic.description?.match(/^.*?[.!?](?:\s|$)/)?.[0].trim()||topic.description||'Quellen zu diesem Thema.'):state.library==='later'?'Gemerkte Quellen, die du noch nicht als gelesen markiert hast.':state.library==='saved'?'Deine gemerkten Quellen – lokal in diesem Browser gespeichert.':state.library==='read'?'Quellen, die du selbst als gelesen markiert hast.':'Originalposts, Videos und Artikel aus deinem Archiv.';
  $('archive-count').hidden=!!(state.topic||state.library);
  if(state.topic)overview.innerHTML=topic.related?.length?`<span class="muted small">Verwandt</span><div class="topic-tags">${topic.related.map(t=>topicLink(t,true)).join('')}</div>`:'';
  if(state.topic&&!topic.related?.length)overview.hidden=true;
  document.title=state.topic||state.library?`${$('page-title').textContent} · Quellenfeed`:'Quellenfeed · AI Company OS';
  syncPersonal();
}
function saveState() {
  const params=new URLSearchParams();
  for(const [key,value] of Object.entries(state))if(value && !(key==='sort' && value==='published'))params.set(key,value);
  history.replaceState(null,'',`${location.pathname}${params.size ? '?'+params : ''}${location.hash}`);
  storage.set('view',JSON.stringify({query:params.toString(),shown,scroll:window.scrollY}));
}
function appendPage(target = shown + PAGE_SIZE) {
  const slice = filtered.slice(shown, target);
  let lastDay = shown ? dateOf(filtered[shown-1],state.sort) : null;
  let markup = '';
  for(const entry of slice) {
    const day = dateOf(entry,state.sort);
    if(day !== lastDay) {markup += `<h2 class="day-heading">${formatDate(day,true)}</h2>`;lastDay=day;}
    markup += card(entry);
  }
  $('feed').insertAdjacentHTML('beforeend',markup);
  shown += slice.length;
  $('more').hidden = shown >= filtered.length;
  $('more').textContent = `Weitere ${Math.min(PAGE_SIZE,filtered.length-shown)} Quellen laden`;
  setupVideos();
  $('feed').querySelectorAll('.card:not([data-initialized])').forEach(article=>{article.dataset.initialized='true';const entry=entryFor(article);if(defaultView(entry)==='source')switchTab(article,'source');});
}
function render(reset = true) {
  filtered = selectEntries(data.entries,state,personal);
  if(reset){shown=0;$('feed').replaceChildren();}
  syncControls();
  $('result-count').textContent = `${filtered.length} ${filtered.length===1 ? 'Quelle' : 'Quellen'}${state.q ? ' gefunden' : ' im Feed'}`;
  if(!filtered.length){$('feed').innerHTML=`<div class="empty"><h2>${state.library?'Hier ist noch keine passende Quelle':'Keine passenden Quellen'}</h2><p>${state.library?'Mit „Merken“ und „Als gelesen markieren“ an den Quellen pflegst du deine Listen. Weitere aktive Filter kannst du oben entfernen.':'Versuche einen anderen Suchbegriff oder setze die Filter zurück.'}</p><button class="play-button" data-reset>Alle Quellen ansehen</button></div>`;$('more').hidden=true;}
  else appendPage();
  saveState();
}
function change(key,value) {state[key]=value;currentSource='';history.replaceState(null,'',location.pathname+location.search);render();if(innerWidth<=760){$('sidebar').classList.remove('open');$('mobile-filters').setAttribute('aria-expanded','false');}window.scrollTo({top:0,behavior:'instant'});}
function setupVideos() {
  document.querySelectorAll('video:not([data-ready])').forEach(video=>{
    video.dataset.ready='true';
    video.addEventListener('loadedmetadata',()=>{
      const row=video.closest('.content-row');
      if(row)row.classList.toggle('landscape-row',video.videoWidth>video.videoHeight);
    });
    video.addEventListener('play',()=>document.querySelectorAll('video').forEach(other=>{if(other!==video)other.pause();}));
    video.addEventListener('error',()=>{const slot=video.closest('.video-slot');if(slot&&!slot.querySelector('.error-message'))slot.insertAdjacentHTML('beforeend','<p class="error-message small">Video nicht abspielbar. Öffne die Originalquelle oder die Archivfassung.</p>');});
  });
}
function loadXScript() {
  if(!xScript)xScript=new Promise((resolve,reject)=>{
    if(window.twttr?.widgets){resolve();return;}
    const script=document.createElement('script');script.src='https://platform.twitter.com/widgets.js';script.async=true;
    script.onload=()=>window.twttr?.ready ? window.twttr.ready(resolve) : reject(Error('X nicht verfügbar'));
    script.onerror=()=>{script.remove();xScript=null;reject(Error('X konnte nicht geladen werden'));};document.head.append(script);
  });
  return xScript;
}
async function embed(entry,article,button) {
  if(article.dataset.embedLoaded || (entry.platform==='X'&&entry.translated))return;
  button.disabled=true;
  try {
    if(entry.platform==='X') {
      const target=document.createElement('div');target.className='x-embed';
      const quote=document.createElement('blockquote');quote.className='twitter-tweet';quote.dataset.theme=document.documentElement.dataset.theme||'light';quote.dataset.conversation='none';
      const link=document.createElement('a');link.href=entry.url;link.textContent='Originalpost auf X';quote.append(link);target.append(quote);
      article.querySelector('.x-embed')?.remove();
      article.querySelector('.original-body').prepend(target);
      await Promise.race([loadXScript(),new Promise((_,reject)=>setTimeout(()=>reject(Error('Zeitüberschreitung')),12000))]);
      const archive=article.querySelector('.original-body');
      const observer=new MutationObserver(()=>{
        const frame=target.querySelector('iframe');
        if(!frame||frame.getBoundingClientRect().height<100)return;
        observer.disconnect();
        for(const child of [...archive.children])if(child!==target)child.hidden=true;
        archive.insertAdjacentHTML('beforeend','<button class="read-more" data-action="restore">Archivansicht anzeigen</button>');
      });
      observer.observe(target,{childList:true,subtree:true,attributes:true,attributeFilter:['style','height']});
      setTimeout(()=>observer.disconnect(),20000);
      window.twttr.widgets.load(target);
    } else {
      if(!entry.video_id)throw Error('Keine Video-ID');
      const frame=document.createElement('iframe');frame.className='video-frame'+(entry.platform==='TikTok'||entry.shorts?' portrait-frame':'');frame.title=entry.title;
      const params=new URLSearchParams({autoplay:'0'});
      if(entry.platform==='YouTube') {
        if(entry.start)params.set('start',entry.start);
        if(entry.end)params.set('end',entry.end);
        params.set('rel','0');frame.src=`https://www.youtube.com/embed/${encodeURIComponent(entry.video_id)}?${params}`;
      } else {params.set('description','1');params.set('music_info','1');frame.src=`https://www.tiktok.com/player/v1/${encodeURIComponent(entry.video_id)}?${params}`;}
      frame.allow='accelerometer; encrypted-media; fullscreen; picture-in-picture';frame.allowFullscreen=true;frame.loading='lazy';frame.referrerPolicy='strict-origin-when-cross-origin';
      let slot=article.querySelector('.video-slot') || article.querySelector('.embed-placeholder');
      if(slot.classList.contains('embed-placeholder')){const wrapper=document.createElement('div');wrapper.className='video-slot';slot.replaceWith(wrapper);slot=wrapper;}
      slot.querySelectorAll('video').forEach(video=>video.pause());slot.replaceChildren(frame);
      slot.insertAdjacentHTML('beforeend',`<p class="embed-status">Falls der Player nicht verfügbar ist: ${external(entry.url,'Original öffnen ↗')}. <button class="read-more" data-action="restore">Archivansicht anzeigen</button></p>`);
    }
    article.dataset.embedLoaded='true';button.hidden=true;
  } catch {button.disabled=false;button.textContent='Erneut versuchen';article.querySelector('.original-body').insertAdjacentHTML('beforeend',`<p class="embed-status">Original-Embed nicht erreichbar. Die Archivfassung bleibt verfügbar. ${external(entry.url)}</p>`);}
}
function authorList(query='') {
  const counts=new Map();data.entries.forEach(e=>e.authors.forEach(a=>counts.set(a,(counts.get(a)||0)+1)));
  const authors=Object.keys(data.authors).filter(a=>counts.has(a)&&normalize([data.authors[a],...Object.entries(data.author_aliases||{}).filter(([,id])=>id===a).map(([alias])=>alias)].join(' ')).includes(normalize(query))).sort((a,b)=>(counts.get(b)-counts.get(a)) || data.authors[a].localeCompare(data.authors[b],'de'));
  $('author-list').innerHTML=authors.slice(0,query?15:6).map(a=>`<button class="filter-item" data-author="${esc(a)}" aria-pressed="${state.author===a}">${avatar(data.authors[a],a)}<span class="filter-name">${esc(data.authors[a])}</span><span class="count">${counts.get(a)}</span></button>`).join('') || '<p class="muted small">Kein Autor gefunden</p>';
}
function configureFilters() {
  for(const [key,items] of [['author',data.authors],['topic',data.topics]]) {
    const used=new Set(data.entries.flatMap(e=>key==='author'?e.authors:e.topics));
    Object.entries(items).filter(([id])=>used.has(id)).sort((a,b)=>a[1].localeCompare(b[1],'de')).forEach(([id,name])=>$(key).add(new Option(name,id)));
  }
  const topicCounts=new Map();data.entries.forEach(e=>e.topics.forEach(t=>topicCounts.set(t,(topicCounts.get(t)||0)+1)));
  $('topic-list').innerHTML=[...topicCounts].sort((a,b)=>b[1]-a[1]).slice(0,5).map(([id,count])=>`<button class="filter-item" data-topic="${esc(id)}" aria-pressed="false"><span class="topic-dot"></span><span class="filter-name">${esc(data.topics[id])}</span><span class="count">${count}</span></button>`).join('');
  const months=[...new Set(data.entries.flatMap(e=>[e.published?.slice(0,7),e.captured?.slice(0,7)]).filter(Boolean))].sort().reverse();
  months.forEach(month=>$('month').add(new Option(new Intl.DateTimeFormat('de-AT',{month:'long',year:'numeric'}).format(new Date(`${month}-01T12:00:00`)),month)));
  return {platform:new Set(data.entries.map(e=>e.platform)),author:new Set(Object.keys(data.authors)),authorAliases:data.author_aliases,topic:new Set(Object.keys(data.topics)),status:new Set(['verarbeitet','ignoriert','neu']),month:new Set(months)};
}
async function openHash() {
  const id=new URLSearchParams(location.hash.slice(1)).get('quelle');
  if(!id||id===currentSource)return;
  const entry=data.entries.find(e=>e.id===id);
  if(!entry)return;
  currentSource=id;
  if(!filtered.some(e=>e.id===id)){state={q:'',platform:'',author:'',topic:'',month:'',status:'',library:'',sort:state.sort};render();}
  const index=filtered.findIndex(e=>e.id===id);
  if(index>=shown)appendPage(index+1);
  document.getElementById(`quelle-${id}`)?.scrollIntoView({block:'start'});
}
function bindEvents() {
  document.addEventListener('click',event=>{
    const link=event.target.closest('a[data-topic-link]');
    if($('viewer').open&&event.target.closest('#viewer a[href^="#quelle="]'))$('viewer').close();
    if(!link||event.button!==0||event.ctrlKey||event.metaKey||event.shiftKey||event.altKey)return;
    if($('viewer').open)$('viewer').close();
    event.preventDefault();state=topicState(state,link.dataset.topicLink);currentSource='';history.pushState(null,'',link.getAttribute('href'));render();$('sidebar').classList.remove('open');$('mobile-filters').setAttribute('aria-expanded','false');window.scrollTo({top:0,behavior:'instant'});
  });
  document.addEventListener('error',event=>{if(event.target.matches?.('.avatar img'))event.target.hidden=true;},true);
  $('search').addEventListener('input',()=>{clearTimeout(filterTimer);filterTimer=setTimeout(()=>change('q',$('search').value),180);});
  $('author-search').addEventListener('input',()=>authorList($('author-search').value));
  for(const key of ['author','topic','month','status','sort'])$(key).addEventListener('change',()=>change(key,$(key).value));
  const reset=()=>{state={q:'',platform:'',author:'',topic:'',month:'',status:'',library:'',sort:'published'};$('author-search').value='';authorList();currentSource='';history.replaceState(null,'',location.pathname);render();window.scrollTo({top:0});};
  $('reset').addEventListener('click',reset);$('all-sources').addEventListener('click',reset);
  $('more').addEventListener('click',()=>{appendPage();saveState();});
  $('theme').addEventListener('click',()=>{const theme=document.documentElement.dataset.theme==='dark'?'light':'dark';document.documentElement.dataset.theme=theme;storage.set('theme',theme);$('theme').setAttribute('aria-label',theme==='dark'?'Helles Farbschema':'Dunkles Farbschema');});
  $('mobile-filters').addEventListener('click',()=>{const open=$('sidebar').classList.toggle('open');$('mobile-filters').setAttribute('aria-expanded',open);});
  document.addEventListener('click',async event=>{
    const button=event.target.closest('button');if(!button)return;
    if(button.hasAttribute('data-reset'))return reset();
    if(button.hasAttribute('data-library')){state={q:'',platform:'',author:'',topic:'',month:'',status:'',library:button.dataset.library,sort:state.sort};currentSource='';history.replaceState(null,'',location.pathname);render();$('sidebar').classList.remove('open');$('mobile-filters').setAttribute('aria-expanded','false');window.scrollTo({top:0,behavior:'instant'});return;}
    if(button.hasAttribute('data-personal')){const item=data.entries.find(entry=>entry.id===button.dataset.entry);if(item)return updatePersonal(item,button.dataset.personal);}
    for(const key of ['platform','author','topic'])if(button.hasAttribute(`data-${key}`)){change(key,button.dataset[key]);return;}
    if(button.dataset.clear)return change(button.dataset.clear,'');
    const article=button.closest('[data-id]');if(!article)return;
    const entry=entryFor(article);
    if(button.dataset.action==='reader')return viewer.openReader(entry,button);
    if(button.dataset.action==='gallery')return viewer.openGallery(entry,button);
    if(button.dataset.tab)return switchTab(article,button.dataset.tab);
    if(button.dataset.action==='source')return switchTab(article,'source');
    if(button.dataset.action==='embed')return embed(entry,article,button);
    if(button.dataset.action==='restore'){article.querySelector('.original-body').innerHTML=original(entry,article.querySelector('.reading-layout').dataset.view==='source');delete article.dataset.embedLoaded;setupVideos();return;}
    if(button.dataset.action==='source-expand'){
      const copy=article.querySelector('.source-copy'), expanded=button.getAttribute('aria-expanded')==='true';
      if(expanded){copy.innerHTML=entry.summary_html;copy.className='source-copy is-summary';article.querySelector('.panel>.content-label').textContent=entry.summary_label||'Deutsche Aufarbeitung';button.setAttribute('aria-expanded','false');button.textContent='Aufarbeitung weiterlesen ↓';return;}
      button.disabled=true;
      try{const content=await loadDetails(entry);if(!button.isConnected||article.querySelector('[aria-selected=true]')?.dataset.tab!=='source')return;copy.innerHTML=content.source_html;copy.className='source-copy is-expanded';article.querySelector('.panel>.content-label').textContent='Deutsche Aufarbeitung';button.setAttribute('aria-expanded','true');button.textContent='Weniger anzeigen ↑';}
      catch{button.textContent='Laden fehlgeschlagen · Erneut versuchen';}finally{button.disabled=false;}return;
    }
    if(button.dataset.action==='expand') {
      if(button.dataset.expanded){article.querySelector('.preview').innerHTML=entry.preview_html;article.querySelector('.preview').style.maxHeight='';button.textContent='Vollständigen Inhalt lesen ↓';delete button.dataset.expanded;return;}
      button.disabled=true;
      try{const content=await loadDetails(entry);const target=article.querySelector('.preview');target.innerHTML=content.original_html;target.style.maxHeight='none';button.textContent='Weniger anzeigen ↑';button.dataset.expanded='true';}catch{button.textContent='Laden fehlgeschlagen · Erneut versuchen';}finally{button.disabled=false;}
    }
  });
  document.addEventListener('toggle',async event=>{
    const target=event.target;if(!target.hasAttribute?.('data-thread')||!target.open||target.dataset.loaded)return;
    const panel=target.querySelector('.thread-content');panel.textContent='Gesprächsverlauf wird geladen …';
    try{const content=await loadDetails(entryFor(target));panel.innerHTML=content.thread_html||'<p>Kein Gesprächsverlauf archiviert.</p>';target.dataset.loaded='true';}catch{panel.textContent='Gesprächsverlauf konnte nicht geladen werden. Zum erneuten Versuch schließen und öffnen.';}
  },true);
  document.addEventListener('keydown',event=>{
    if((event.ctrlKey||event.metaKey)&&event.key.toLowerCase()==='k'){event.preventDefault();$('search').focus();}
    if(event.key==='Escape'){$('sidebar').classList.remove('open');$('mobile-filters').setAttribute('aria-expanded','false');}
    if(event.target.matches('[role=tab]')&&['ArrowLeft','ArrowRight','Home','End'].includes(event.key)){
      event.preventDefault();const tabs=[...event.target.closest('[role=tablist]').querySelectorAll('[role=tab]')];let index=tabs.indexOf(event.target);
      index=event.key==='Home'?0:event.key==='End'?tabs.length-1:(index+(event.key==='ArrowRight'?1:-1)+tabs.length)%tabs.length;tabs[index].focus();switchTab(tabs[index].closest('[data-id]'),tabs[index].dataset.tab);
    }
  });
  $('to-top').addEventListener('click',()=>window.scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'}));
  let scrollTimer;window.addEventListener('scroll',()=>{$('to-top').hidden=window.scrollY<600;clearTimeout(scrollTimer);scrollTimer=setTimeout(saveState,250);},{passive:true});
  window.addEventListener('pagehide',saveState);
  window.addEventListener('hashchange',openHash);
  window.addEventListener('popstate',()=>{state=readState(new URLSearchParams(location.search),validFilters);render();currentSource='';openHash();});
  window.addEventListener('storage',event=>{if(event.key==='quellenfeed-library'){personal=parseLibrary(event.newValue);render();viewer.refreshPersonal();}});
}
let validFilters;
async function init() {
  try {
    const response=await fetch('index.json');if(!response.ok)throw Error('Quellenindex nicht erreichbar');
    data=await response.json();
    personal=parseLibrary(storage.get('library'));
    viewer=createViewer({loadDetails,controls:personalControls});
    data.entries.forEach(entry=>entry.topics.forEach(topic=>topicCounts.set(topic,(topicCounts.get(topic)||0)+1)));
    for(const entry of data.entries){entry.searchNormalized=normalize([entry.title,entry.author,entry.handle,entry.platform,entry.search,...entry.keywords,...entry.topics.map(t=>data.topics[t])].join(' '));delete entry.search;}
    validFilters=configureFilters();
    let params=new URLSearchParams(location.search), savedView;
    try{savedView=JSON.parse(storage.get('view'));}catch{}
    if(!params.size&&!location.hash&&savedView?.query)params=new URLSearchParams(savedView.query);
    restorePosition=matchingView(params,savedView,!!location.hash);
    state=readState(params,validFilters);
    authorList();
    $('total-count').textContent=data.entries.length;
    $('archive-count').textContent=`${data.counts.files} Archiveinträge · ${data.counts.unique} Quellen`;
    if(!['localhost','127.0.0.1','::1',''].includes(location.hostname))$('local-badge').hidden=true;
    $('platforms').innerHTML=[['','Alle'],['X','X'],['YouTube','YouTube'],['TikTok','TikTok'],['URL','Artikel'],['PDF','PDF']].map(([id,name])=>`<button class="platform-button" data-platform="${id}" aria-pressed="${state.platform===id}">${name}</button>`).join('');
    bindEvents();render();
    if(Number.isFinite(restorePosition?.shown)&&restorePosition.shown>shown)appendPage(Math.min(restorePosition.shown,filtered.length));
    if(Number.isFinite(restorePosition?.scroll)&&restorePosition.scroll>0)requestAnimationFrame(()=>window.scrollTo({top:restorePosition.scroll}));
    await openHash();
  } catch(error) {$('result-count').textContent='Quellen konnten nicht geladen werden.';$('feed').innerHTML='<div class="empty"><h2>Der Quellenfeed braucht einen lokalen Server</h2><p>Im Repository <code>python ai.py quellen feed</code> starten und die angezeigte lokale Adresse öffnen.</p></div>';console.error(error);}
}
init();
