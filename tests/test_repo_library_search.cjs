const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const root=path.resolve(__dirname,'..');
const context={window:{}};
vm.runInNewContext(fs.readFileSync(path.join(root,'70_Scripts/repo_library/templates/search.js'),'utf8'),context);
const search=context.window.RepoLibrary.search;
const discovery=JSON.parse(fs.readFileSync(path.join(root,'70_Scripts/repo_library/discovery.json'),'utf8'));
const data={discovery,tasks:[{id:'ui',title:'Eine generische Oberfläche aufwerten',description:'Design und Taste',repoIds:['impeccable']},{id:'react',title:'React-Code auf Qualität prüfen',description:'React-Audit',repoIds:['doctor']}],categories:[{id:'design',title:'Design'},{id:'engineering',title:'Engineering'}],repos:[{id:'impeccable',label:'pbakaus/impeccable',purposes:['Generische Frontends aufwerten'],features:['Design und UI'],text:'Polish für Web-Oberflächen',taskIds:['ui'],categories:['design']},{id:'doctor',label:'millionco/react-doctor',purposes:['React-Code prüfen'],features:['React und Qualität'],text:'Technischer React-Audit',taskIds:['react'],categories:['engineering']},{id:'other',label:'owner/builder',purposes:['Unabhängige Infrastruktur'],features:['Shell'],text:'build utility',taskIds:[],categories:['engineering']}]};

test('problem search finds the curated UI task and explains its result',()=>{
  const results=search.repoResults(data,'Meine Oberfläche wirkt generisch');
  assert.equal(results[0].repo.id,'impeccable');
  assert.equal(results[0].reason,'Eine generische Oberfläche aufwerten');
});
test('unknown query does not invent matches',()=>{
  assert.equal(search.repoResults(data,'zxqv987654').length,0);
  assert.equal(search.taskResults(data,'zxqv987654').length,0);
});
test('short tokens respect word boundaries and umlauts normalize',()=>{
  assert.equal(search.repoResults(data,'ui').some(result=>result.repo.id==='other'),false);
  assert.equal(search.normalize('Übersicht Straße'),'ubersicht strasse');
});
test('similarity uses shared source relationships and excludes itself',()=>{
  const results=search.similar(data,'doctor');
  assert.equal(results.length,1);
  assert.equal(results[0].repo.id,'other');
  assert.equal(results[0].reason,'Engineering');
});

test('matching passage comes from the original description',()=>{
  const text='Eine lange Einordnung. Der Scanner verwendet Semgrep für diese Prüfung. Weitere Hinweise.';
  assert.ok(search.excerpt(text,'semgrep',discovery).includes('Semgrep'));
});

test('blocked storage and a null cache do not prevent standalone startup',()=>{
  const source=fs.readFileSync(path.join(root,'70_Scripts/repo_library/templates/state.js'),'utf8');
  for(const getItem of [()=>{throw new Error('Storage disabled');},()=> 'null']){
    const stateContext={window:{RepoLibrary:{}},localStorage:{getItem},location:{hash:''},URLSearchParams};
    vm.runInNewContext(source,stateContext);
    const state=stateContext.window.RepoLibrary.initialState({...data,discovery:{...discovery,goals:[]}});
    assert.equal(state.view,'explore');
    assert.equal(state.favorites.length,0);
  }
});
