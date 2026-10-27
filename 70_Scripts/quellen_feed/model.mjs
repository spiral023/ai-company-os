// Reine Auswahlfunktionen: derselbe Vertrag im Browser und in den Node-Tests.
export const normalize = value => String(value || '').normalize('NFKD').replace(/\p{M}/gu, '').toLocaleLowerCase('de').replaceAll('ß', 'ss');
export function dateOf(entry, sort) {
  return entry[sort === 'captured' ? 'captured' : 'published'] || entry.captured || '';
}
export const LIBRARY_VIEWS = new Set(['saved','later','read']);
export function parseLibrary(value) {
  try {
    const data=JSON.parse(value);
    if(data?.version!==1||!data.entries||typeof data.entries!=='object')return {};
    return Object.fromEntries(Object.entries(data.entries).filter(([id,item])=>/^[a-f0-9]{16}$/.test(id)&&item&&typeof item==='object')
      .map(([id,item])=>[id,{saved:item.saved===true,read:item.read===true}]));
  } catch {return {};}
}
export function togglePersonal(library, id, field) {
  const item={saved:false,read:false,...library[id]};
  if(!['saved','read'].includes(field))return library;
  return {...library,[id]:{...item,[field]:!item[field]}};
}
export function matchesLibrary(entry, view, library={}) {
  const item=library[entry.id]||{};
  return view==='saved'?!!item.saved:view==='later'?!!item.saved&&!item.read:view==='read'?!!item.read:true;
}
export function selectEntries(entries, state, library={}) {
  const terms = normalize(state.q).split(/\s+/).filter(Boolean);
  return entries.filter(entry =>
    matchesLibrary(entry,state.library,library) &&
    (!state.platform || entry.platform === state.platform) &&
    (!state.author || entry.authors.includes(state.author)) &&
    (!state.topic || entry.topics.includes(state.topic)) &&
    (!state.status || entry.statuses.includes(state.status)) &&
    (!state.month || dateOf(entry, state.sort).startsWith(state.month)) &&
    terms.every(term => entry.searchNormalized.includes(term))
  ).sort((a, b) => dateOf(b, state.sort).localeCompare(dateOf(a, state.sort)) || a.id.localeCompare(b.id));
}
export function readState(params, valid) {
  const result = {q: params.get('q') || '', sort: params.get('sort') === 'captured' ? 'captured' : 'published'};
  for (const key of ['platform', 'author', 'topic', 'status', 'month']) {
    const candidate=key==='author'?(valid.authorAliases?.[params.get(key)]||params.get(key)):params.get(key);
    result[key] = valid[key].has(candidate) ? candidate : '';
  }
  result.library=LIBRARY_VIEWS.has(params.get('library'))?params.get('library'):'';
  return result;
}
export function matchingView(params, saved, hasHash) {
  if(hasHash || !saved || typeof saved.query !== 'string')return null;
  const current=new URLSearchParams(params), previous=new URLSearchParams(saved.query);
  current.sort();previous.sort();
  return current.toString()===previous.toString() ? saved : null;
}
export function defaultView(entry) {
  return entry.has_source ? 'source' : 'original';
}
export function topicState(state, topic) {
  return {q:'',platform:'',author:'',topic,month:'',status:'',library:'',sort:state.sort || 'published'};
}
export function relatedEntries(entry, entries, limit=3) {
  const topics=new Set(entry.topics), keywords=new Set(entry.keywords.map(normalize));
  return entries.filter(other=>other.id!==entry.id).map(other=>{
    const shared=other.topics.filter(topic=>topics.has(topic));
    const sharedMain=(other.main_topics || []).filter(topic=>(entry.main_topics || []).includes(topic));
    const commonKeywords=other.keywords.filter(word=>keywords.has(normalize(word)));
    return {entry:other,shared,sharedMain,score:shared.length+sharedMain.length*3+Math.min(commonKeywords.length,3)};
  }).filter(item=>item.shared.length).sort((a,b)=>b.score-a.score || dateOf(b.entry,'published').localeCompare(dateOf(a.entry,'published')) || a.entry.id.localeCompare(b.entry.id)).slice(0,limit);
}
