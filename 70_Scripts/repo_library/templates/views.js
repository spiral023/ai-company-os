(function(L){
  "use strict";
  const e=value=>L.escape(value);
  const byId=id=>L.data.repos.find(repo=>repo.id===id);
  const field=(repo,name)=>repo.fields.find(item=>item.label===name);
  const number=value=>value==null?"—":value.toLocaleString("de-DE");
  const categoryNames=repo=>repo.categories.map(id=>L.data.categories.find(item=>item.id===id)?.title).filter(Boolean);
  const date=value=>value&&/^\d{4}-\d{2}-\d{2}$/.test(value)?value.split("-").reverse().join("."):value||"ohne Datumsangabe";
  L.getResults=function(){
    const s=L.state;let results=s.similar?L.search.similar(L.data,s.similar):L.search.repoResults(L.data,s.query);
    const task=L.data.tasks.find(task=>task.id===s.task);
    if(task)results=results.filter(result=>task.repoIds.includes(result.repo.id)).map(result=>({...result,reason:task.title,reasonType:"Aufgabe"}));
    results=results.filter(({repo})=>(!s.categories.length||repo.categories.some(category=>s.categories.includes(category)))&&(!s.type||repo.types.includes(s.type))&&(s.view!=="saved"||s.favorites.includes(repo.id)));
    if(s.sort==="name")results.sort((a,b)=>a.repo.label.localeCompare(b.repo.label,"de"));
    if(s.sort==="stars")results.sort((a,b)=>(b.repo.stars??-1)-(a.repo.stars??-1)||a.repo.label.localeCompare(b.repo.label,"de"));
    if(s.sort==="downloaded"||s.sort==="updated")results.sort((a,b)=>String(b.repo[s.sort]||"").localeCompare(String(a.repo[s.sort]||""))||a.repo.label.localeCompare(b.repo.label,"de"));
    return results;
  };
  function resultCard(result){
    const repo=result.repo,s=L.state;
    const favorite=s.favorites.includes(repo.id),comparison=s.compare.includes(repo.id);
    return '<article class="repo-card '+(s.selected===repo.id?'selected':'')+'" data-repo="'+e(repo.id)+'"><button class="repo-open" type="button" data-open="'+e(repo.id)+'" aria-label="'+e('Repo '+repo.label+' öffnen')+'"><span class="owner">'+e(repo.owner)+'</span><h3>'+L.highlight(repo.name)+'</h3><p>'+L.highlight(repo.purpose)+'</p></button><div class="repo-card-bottom">'+repo.types.slice(0,2).map(type=>'<span class="type-badge">'+e(type)+'</span>').join('')+'<span class="star-count" title="Sterne laut Index, kein Qualitätsscore">☆ '+number(repo.stars)+'</span><button class="mini-button" type="button" data-favorite="'+e(repo.id)+'" aria-label="'+e((favorite?'Aus Merkliste entfernen: ':'Merken: ')+repo.label)+'" aria-pressed="'+favorite+'">'+L.icon('bookmark')+'</button><button class="mini-button" type="button" data-compare="'+e(repo.id)+'" aria-label="'+e('Vergleichen: '+repo.label)+'" aria-pressed="'+comparison+'">'+L.icon('compare')+'</button></div>'+(result.reason?'<div class="match-reason"><span>'+e(result.reasonType)+':</span> '+L.highlight(result.reason)+'</div>':s.query?'<div class="match-reason">Texttreffer im Profil</div>'+(result.excerpt?'<p class="match-excerpt">'+L.highlight(result.excerpt)+'</p>':''):'')+'</article>';
  }
  function detail(repo,mobile=false){
    if(!repo)return '<aside class="detail-panel"><div class="empty-state"><h3>Dein nächster Einstieg</h3><p>Wähle ein Repo aus der Liste, um sein vollständiges Profil zu lesen.</p></div></aside>';
    const fields=repo.fields.filter(item=>item.label!=="URL");
    return '<'+(mobile?'div':'aside')+' class="detail-panel" aria-label="Repo-Detailprofil"><div class="detail-owner">'+e(repo.owner)+'</div><h2'+(mobile?' id="mobileDetailTitle"':'')+'>'+e(repo.name)+'</h2><p class="detail-purpose">'+e(repo.purpose)+'</p><div class="detail-badges">'+[...repo.types,...categoryNames(repo)].map(label=>'<span class="badge">'+e(label)+'</span>').join('')+'</div><div class="detail-actions"><a class="primary-button" href="'+e(repo.url)+'" target="_blank" rel="noopener noreferrer">GitHub öffnen '+L.icon('external')+'</a><button class="secondary-button" type="button" data-favorite="'+e(repo.id)+'">'+L.icon('bookmark')+(L.state.favorites.includes(repo.id)?'Gemerkt':'Merken')+'</button><button class="secondary-button" type="button" data-compare="'+e(repo.id)+'">'+L.icon('compare')+(L.state.compare.includes(repo.id)?'Im Vergleich':'Vergleichen')+'</button></div><h3 class="section-label">VOLLSTÄNDIGE EINORDNUNG</h3><div class="prose">'+repo.html+'</div><div class="detail-meta"><h3 class="section-label">METADATEN AUS DEM INDEX</h3><dl>'+fields.map(item=>'<div class="meta-row"><dt>'+e(item.label)+'</dt><dd>'+item.html+'</dd></div>').join('')+'</dl></div><div class="detail-paths"><h3 class="section-label">LOKALER EINSTIEG</h3><div class="path-box"><code>'+e(repo.localPath)+'</code><button class="mini-button" type="button" data-copy-path="'+e(repo.id)+'" aria-label="Lokalen Repo-Pfad kopieren">'+L.icon('copy')+'</button></div><a class="secondary-button" href="'+e(L.localHref(repo.localPath+'README.md'))+'" target="_blank" rel="noopener">Lokale README öffnen '+L.icon('external')+'</a>'+repo.entryPaths.map(path=>'<p class="muted" style="font-size:10px;margin-top:12px;margin-bottom:0">'+e(path)+'</p>').join('')+'</div><div class="related-actions"><button class="secondary-button" type="button" data-similar="'+e(repo.id)+'">Ähnliche entdecken '+L.icon('arrow')+'</button><button class="secondary-button" type="button" data-brief="'+e(repo.id)+'">Startzettel kopieren '+L.icon('copy')+'</button></div></'+(mobile?'div':'aside')+'>';
  }
  function filters(){
    const s=L.state;
    const chips=s.categories.map(id=>{const category=L.data.categories.find(item=>item.id===id);return '<button class="filter-chip" type="button" data-category="'+e(id)+'">'+e(category?.title)+' ×</button>';});
    if(s.task){const task=L.data.tasks.find(item=>item.id===s.task);chips.push('<button class="filter-chip" type="button" data-action="clear-task">'+e(task?.title)+' ×</button>');}
    if(s.similar)chips.push('<button class="filter-chip" type="button" data-action="clear-similar">Ähnlich zu '+e(byId(s.similar)?.name)+' ×</button>');
    if(s.type)chips.push('<button class="filter-chip" type="button" data-action="clear-type">'+e(s.type)+' ×</button>');
    return chips.length?'<div class="active-filters">'+chips.join('')+'<button class="reset-button" type="button" data-action="reset">Filter zurücksetzen</button></div>':'';
  }
  function selectControls(){
    const s=L.state,types=[...new Set(L.data.repos.flatMap(repo=>repo.types))].sort();
    return '<div class="selects"><select id="typeFilter" aria-label="Repo-Typ"><option value="">Alle Typen</option>'+types.map(type=>'<option value="'+e(type)+'"'+(s.type===type?' selected':'')+'>'+e(type)+'</option>').join('')+'</select><select id="sortFilter" aria-label="Sortierung">'+[['relevance','Passende zuerst'],['name','Name A–Z'],['stars','Sterne im Index'],['downloaded','Neu hinzugefügt'],['updated','Zuletzt aktualisiert']].map(([value,label])=>'<option value="'+value+'"'+(s.sort===value?' selected':'')+'>'+label+'</option>').join('')+'</select></div>';
  }
  function library(){
    const results=L.getResults(),s=L.state;
    if(!results.some(result=>result.repo.id===s.selected))s.selected=results[0]?.repo.id||'';
    const taskSuggestions=s.query&&!s.task&&!s.similar?L.search.taskResults(L.data,s.query).slice(0,3):[];
    const suggestions=taskSuggestions.length?'<div class="task-suggestions"><span class="small-label">PASSENDE AUFGABEN</span>'+taskSuggestions.map(({task})=>'<button class="task-suggestion" type="button" data-task="'+e(task.id)+'">'+L.highlight(task.title)+' '+L.icon('arrow')+'</button>').join('')+'</div>':'';
    let recent='';
    if(s.view==='saved')recent='<div class="saved-heading"><h3 class="section-label">ZULETZT GELESEN</h3><div class="recent-list">'+(s.recent.length?s.recent.map(id=>'<button class="recent-button" type="button" data-open="'+e(id)+'">'+e(byId(id)?.label)+'</button>').join(''):'<span class="muted">Deine zuletzt geöffneten Profile erscheinen hier.</span>')+'</div></div>';
    const empty='<div class="empty-state"><h3>'+(s.view==='saved'?'Dein Regal ist noch frei.':'Noch kein passender Treffer.')+'</h3><p>'+(s.view==='saved'?'Merke interessante Repos mit dem Lesezeichen.':'Versuche eine konkrete Aufgabe oder einen kürzeren Suchbegriff.')+'</p><button class="secondary-button" type="button" data-action="reset">'+(s.view==='saved'?'Bibliothek entdecken':'Alle Profile anzeigen')+'</button></div>';
    return recent+'<div class="workspace-heading"><h2>'+(s.view==='saved'?'Deine Merkliste':'Die Bibliothek')+'<span class="count">'+results.length+' '+(results.length===1?'Profil':'Profile')+'</span></h2>'+selectControls()+'</div>'+filters()+suggestions+'<div class="library-grid"><div id="resultList" class="result-list" aria-label="Repo-Ergebnisse">'+(results.length?results.map(resultCard).join(''):empty)+'</div>'+detail(byId(s.selected))+'</div>';
  }
  function tasks(){
    const s=L.state,goal=L.data.discovery.goals.find(goal=>goal.id===s.goal);
    let taskMatches=L.search.taskResults(L.data,s.query);
    if(goal)taskMatches=taskMatches.filter(({task})=>goal.terms.some(term=>L.search.normalize(task.title).includes(L.search.normalize(term))));
    if(s.categories.length)taskMatches=taskMatches.filter(({task})=>task.repoIds.some(id=>byId(id)?.categories.some(category=>s.categories.includes(category))));
    return '<div class="step-label"><strong>01</strong> Wähle dein Ziel – oder zeige alle Aufgaben.</div><div class="goal-grid">'+L.data.discovery.goals.map(goal=>'<button class="goal-card" type="button" data-goal="'+goal.id+'" aria-pressed="'+(s.goal===goal.id)+'"><strong>'+e(goal.title)+'</strong><span>'+e(goal.description)+'</span></button>').join('')+'</div><div class="workspace-heading"><div class="step-label"><strong>02</strong> Was möchtest du konkret tun? <span class="count">'+taskMatches.length+' Aufgaben</span></div><button class="reset-button" type="button" data-action="all-tasks">Alle Aufgaben</button></div>'+filters()+'<div class="task-grid">'+(taskMatches.length?taskMatches.map(({task})=>'<button type="button" class="task-card" data-task="'+e(task.id)+'"><h3>'+L.highlight(task.title)+'</h3><p>'+L.highlight(task.description)+'</p><span class="task-count">'+task.repoIds.length+' '+(task.repoIds.length===1?'Startpunkt':'Startpunkte')+' entdecken →</span></button>').join(''):'<div class="empty-state"><h3>Keine Aufgaben in dieser Auswahl.</h3><button class="secondary-button" data-action="all-tasks" type="button">Alle Aufgaben anzeigen</button></div>')+'</div>';
  }
  function routes(){
    const queryTerms=L.search.terms(L.state.query,L.data.discovery);
    const routes=L.data.routes.filter(route=>!queryTerms.length||queryTerms.some(term=>L.search.normalize(route.title+' '+route.markdown).includes(term)));
    return '<div class="workspace-heading"><h2>Empfohlene Startpunkte<span class="count">'+routes.length+' Arbeitsrouten</span></h2></div><div class="route-grid">'+routes.map((route,index)=>'<article class="route-card"><div class="route-number">0'+(index+1)+'</div><h2>'+e(route.title)+'</h2><div class="prose">'+route.html+'</div><button class="primary-button" type="button" data-copy-route="'+e(route.id)+'">Arbeitsroute kopieren '+L.icon('copy')+'</button></article>').join('')+'</div>'+(routes.length?'':'<div class="empty-state"><h3>Keine passende Arbeitsroute.</h3><button class="secondary-button" type="button" data-action="reset">Suche zurücksetzen</button></div>');
  }
  function source(){
    return '<div class="source-toolbar"><h2>Der vollständige Originalindex</h2><button class="secondary-button" type="button" data-action="copy-source">Markdown kopieren '+L.icon('copy')+'</button></div><div class="source-toc">'+L.data.general.map(section=>'<a href="#'+e(section.id)+'">'+e(section.title)+'</a>').join('')+'</div><article class="source-document">'+L.data.sourceHtml+'<details><summary>Original-Markdown einschließlich Pflege-Markierungen</summary><pre class="raw-source">'+e(L.data.sourceMarkdown)+'</pre></details></article>';
  }
  L.render=function(){
    const s=L.state,views=[['explore','Entdecken','library'],['tasks','Aufgaben','tasks'],['routes','Arbeitsrouten','route'],['saved','Merkliste','bookmark'],['source','Originalindex','library']];
    document.documentElement.dataset.theme=s.theme;
    document.getElementById('themeButton').innerHTML=L.icon(s.theme==='light'?'moon':'sun');
    document.getElementById('themeButton').setAttribute('aria-label',s.theme==='light'?'Dunkles Design aktivieren':'Helles Design aktivieren');
    document.getElementById('primaryNav').innerHTML=views.map(([view,label,icon])=>'<button class="nav-button" type="button" data-view="'+view+'"'+(s.view===view?' aria-current="page"':'')+' aria-label="'+e(label)+'">'+L.icon(icon)+'<span class="nav-long">'+label+'</span><span class="nav-short">'+({routes:'Routen',source:'Index'}[view]||label)+'</span>'+(view==='saved'?'<span class="nav-count">'+s.favorites.length+'</span>':'')+'</button>').join('');
    document.getElementById('categoryNav').innerHTML='<button class="category-button" type="button" data-action="all-categories" aria-pressed="'+(!s.categories.length)+'"><span class="category-symbol"></span>Alle Themen<span class="category-count">'+L.data.repos.length+'</span></button>'+L.data.categories.map(category=>'<button class="category-button" type="button" data-category="'+e(category.id)+'" aria-pressed="'+s.categories.includes(category.id)+'"><span class="category-symbol"></span>'+e(category.title)+'<span class="category-count">'+category.repoIds.length+'</span></button>').join('');
    document.getElementById('categoryTotal').textContent=String(L.data.categories.length);
    document.getElementById('profileTotal').textContent=String(L.data.repos.length);
    document.getElementById('introCounts').textContent=L.data.tasks.length+' Aufgaben · '+L.data.categories.length+' Themenbereiche';
    document.getElementById('sourceStamp').innerHTML='Index-Stand '+e(date(L.data.sourceDate))+'<br>'+L.data.repos.length+' Profile vollständig enthalten';
    document.getElementById('coverageInfo').textContent=L.data.repos.length+' Profile · '+L.data.tasks.length+' Aufgaben · offline verfügbar';
    document.getElementById('updateCoverage').textContent=L.data.repos.length+' Profile, '+L.data.tasks.length+' Aufgaben, '+L.data.categories.length+' Themen, '+L.data.routes.length+' Arbeitsrouten. Quelle vollständig eingebettet. Index-Stand: '+date(L.data.sourceDate)+'.';
    document.getElementById('query').value=s.query;document.getElementById('clearQuery').hidden=!s.query;
    document.getElementById('searchIcon').innerHTML=L.icon('search');
    document.getElementById('shortcuts').innerHTML=L.data.discovery.shortcuts.map(shortcut=>'<button class="shortcut" type="button" data-query="'+e(shortcut.query)+'">'+e(shortcut.label)+'</button>').join('');
    const titles={explore:['DEIN WERKZEUGREGAL','Gute Werkzeuge.<br><em>Klare nächste Schritte.</em>','Beschreibe dein Ziel. Entdecke passende Quellen.<br>Und finde den richtigen Einstieg für deine Arbeit.'],tasks:['DER WEGFINDER','Was möchtest du <em>tun?</em>','Zwei Schritte vom Vorhaben zu passenden Quellen. Alle Aufgaben stammen aus deinem Index.'],routes:['VOM FUND ZUR ARBEIT','Ein guter <em>Anfang.</em>','Die kuratierten Startpunkte und praktischen Kombinationen aus deinem Index.'],saved:['DEIN PERSÖNLICHES REGAL','Wissen, das <em>bleibt.</em>',L.storageAvailable?'Deine Merkliste und zuletzt gelesene Profile bleiben in diesem Browser gespeichert.':'Deine Merkliste bleibt für diese Sitzung erhalten. Der Browser erlaubt hier keine dauerhafte Speicherung.'],source:['DIE GEMEINSAME QUELLE','Alles. <em>Ungekürzt.</em>','Sämtliche Inhalte der Markdown-Datei, einschließlich Hinweise, Tabellen und Metadaten.']};
    document.getElementById('pageEyebrow').textContent=titles[s.view][0];document.getElementById('pageTitle').innerHTML=titles[s.view][1];document.getElementById('pageDescription').innerHTML=titles[s.view][2];
    document.querySelector('.intro').classList.toggle('compact-intro',s.view!=='explore');
    document.getElementById('viewContent').innerHTML=s.view==='tasks'?tasks():s.view==='routes'?routes():s.view==='source'?source():library();
    const bar=document.getElementById('compareBar');bar.hidden=!s.compare.length;
    bar.innerHTML='<strong>'+s.compare.length+'/3 ausgewählt</strong><span class="compare-labels">'+s.compare.map(id=>e(byId(id)?.name)).join(' · ')+'</span><button class="primary-button" type="button" data-action="show-compare"'+(s.compare.length<2?' disabled':'')+'>Vergleich öffnen '+L.icon('compare')+'</button><button class="icon-button" type="button" data-action="clear-compare" aria-label="Vergleichsauswahl leeren">×</button>';
    if(document.getElementById('repoDialog').open)document.getElementById('mobileDetail').innerHTML=detail(byId(s.selected),true);
    L.persist();
  };
  L.renderMobileDetail=()=>document.getElementById('mobileDetail').innerHTML=detail(byId(L.state.selected),true);
  L.renderComparison=function(){
    const repos=L.state.compare.map(byId).filter(Boolean);
    document.getElementById('compareContent').innerHTML='<div class="compare-grid" style="--compare-count:'+repos.length+'">'+repos.map(repo=>'<article class="compare-card"><div class="detail-owner">'+e(repo.owner)+'</div><h3>'+e(repo.name)+'</h3>'+[['EINSATZZWECK',e(repo.purpose)],['TYP',e(repo.types.join(' / ')||'Nicht eingeordnet')],['THEMEN',e(categoryNames(repo).join(' · ')||'Nicht zugeordnet')],['KONKRET NUTZBAR',e(repo.features.join(' · ')||'Siehe vollständiges Profil')],['STERNE IM INDEX',number(repo.stars)],['LOKALER EINSTIEG','<code>'+e(repo.localPath)+'</code>'],['STRUKTUR',field(repo,'Struktur')?.html||'Nicht angegeben']].map(([label,value])=>'<div class="compare-section"><div class="section-label">'+label+'</div>'+value+'</div>').join('')+'<details><summary>Vollständiges Profil lesen</summary><div class="prose">'+repo.html+'</div></details><a class="secondary-button" href="'+e(repo.url)+'" target="_blank" rel="noopener noreferrer">GitHub öffnen '+L.icon('external')+'</a></article>').join('')+'</div>';
  };
})(window.RepoLibrary);
