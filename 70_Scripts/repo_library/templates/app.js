(function(L){
  "use strict";
  L.data=JSON.parse(document.getElementById('libraryData').textContent);
  const initialRepoLink=new URLSearchParams(location.hash.slice(1)).has('repo');
  L.state=L.initialState(L.data);
  const repo=id=>L.data.repos.find(item=>item.id===id);
  const task=id=>L.data.tasks.find(item=>item.id===id);
  const $=id=>document.getElementById(id);
  function refresh(resetList=false){
    const oldList=$('resultList'),scroll=oldList?.scrollTop||0;
    const active=document.activeElement;
    const container=active?.closest('#resultList,#primaryNav,#categoryNav,#mobileDetail,.library-grid>.detail-panel');
    const focusData=active?.dataset;
    const focusKey=focusData&&Object.keys(focusData).find(key=>['open','favorite','compare','category','view','similar','brief','copyPath'].includes(key));
    const scope=container?.id?'#'+container.id:container?.classList.contains('detail-panel')?'.library-grid>.detail-panel':'';
    L.render();
    if($('resultList'))$('resultList').scrollTop=resetList?0:scroll;
    if(scope&&focusKey){
      const attr=focusKey.replace(/[A-Z]/g,char=>'-'+char.toLowerCase());
      document.querySelector(scope+' [data-'+attr+'="'+CSS.escape(focusData[focusKey])+'"]')?.focus({preventScroll:true});
    }
  }
  function resetFilters(){Object.assign(L.state,{query:'',categories:[],type:'',task:'',similar:'',goal:''});}
  function closeRepo(){if($('repoDialog').open)$('repoDialog').close();}
  function openRepo(id){
    if(!repo(id))return;
    if(!L.getResults().some(result=>result.repo.id===id)){L.state.view='explore';resetFilters();}
    L.state.selected=id;
    L.state.recent=[id,...L.state.recent.filter(value=>value!==id)].slice(0,12);
    refresh();
    if(matchMedia('(max-width:1020px)').matches){L.renderMobileDetail();if(!$('repoDialog').open)$('repoDialog').showModal();}
  }
  function openTask(id){
    if(!task(id))return;closeRepo();resetFilters();L.state.task=id;L.state.view='explore';L.state.selected='';refresh(true);$('viewContent').scrollIntoView({block:'start'});
  }
  function brief(id){
    const selected=repo(id);if(!selected)return;
    const selectedTask=task(L.state.task);
    const goal=selectedTask?.title||L.state.query||selected.purpose;
    L.copy('# Arbeitsstart: '+goal+'\n\n## Referenz\n- '+selected.label+': '+selected.url+'\n- Lokale Ablage: '+selected.localPath+'\n- Einstieg: '+(selected.entryPaths.join(', ')||selected.localPath+'README.md')+'\n\n## Erste Schritte\n1. README und die genannte Einordnung lesen.\n2. Relevante Dateien gezielt untersuchen.\n3. Einen kleinen, zum Ziel passenden Ansatz für das eigene Projekt vorschlagen.\n\nDie Quelle ist eine Analyse-Referenz. Eine produktive Übernahme ist separat zu prüfen.\n\n## Einordnung aus dem Index\n'+selected.markdown);
  }
  function copyRoute(id){
    const route=L.data.routes.find(item=>item.id===id);if(!route)return;
    const markdown=route.markdown.replace(/\[([^\]]+)\]\(#([^)]+)\)/g,(all,label,identifier)=>repo(identifier)?'['+label+']('+repo(identifier).url+')':all);
    L.copy('# Arbeitsroute: '+route.title+'\n\n'+markdown+'\n\n## Lokale Einstiegspunkte\n'+route.repoIds.map(id=>'- '+repo(id).label+': '+repo(id).localPath+'README.md').join('\n'));
  }
  document.addEventListener('click',event=>{
    const button=event.target.closest('button,a');if(!button)return;
    const data=button.dataset,s=L.state;
    if(data.close){$(data.close)?.close();return;}
    if(data.view){closeRepo();s.view=data.view;refresh(true);return;}
    if(data.open){openRepo(data.open);return;}
    if(data.task){openTask(data.task);return;}
    if(data.category){
      closeRepo();s.categories=s.categories.includes(data.category)?s.categories.filter(value=>value!==data.category):[...s.categories,data.category];
      if(!['explore','saved','tasks'].includes(s.view))s.view='explore';refresh(true);return;
    }
    if(data.goal){s.goal=s.goal===data.goal?'':data.goal;s.view='tasks';refresh(true);return;}
    if(data.query){closeRepo();resetFilters();s.query=data.query;s.view='explore';refresh(true);$('query').focus();return;}
    if(data.favorite){s.favorites=s.favorites.includes(data.favorite)?s.favorites.filter(value=>value!==data.favorite):[...s.favorites,data.favorite];refresh();return;}
    if(data.compare){
      if(s.compare.includes(data.compare))s.compare=s.compare.filter(value=>value!==data.compare);
      else if(s.compare.length===3){L.notify('Du kannst bis zu drei Repos vergleichen.');return;}
      else s.compare.push(data.compare);
      refresh();return;
    }
    if(data.similar){closeRepo();resetFilters();s.similar=data.similar;s.view='explore';s.selected='';refresh(true);return;}
    if(data.copyPath){L.copy(repo(data.copyPath)?.localPath||'');return;}
    if(data.brief){brief(data.brief);return;}
    if(data.copyRoute){copyRoute(data.copyRoute);return;}
    if(button.id==='themeButton'){s.theme=s.theme==='light'?'dark':'light';refresh();return;}
    if(button.id==='clearQuery'){s.query='';refresh(true);$('query').focus();return;}
    if(button.matches('a[href^="#"]')&&!data.action&&s.view!=='source'){
      const id=decodeURIComponent(button.getAttribute('href').slice(1));
      if(repo(id)){event.preventDefault();openRepo(id);return;}
    }
    if(!data.action)return;
    if(['home','reset'].includes(data.action)){event.preventDefault();closeRepo();resetFilters();s.view='explore';refresh(true);}
    if(data.action==='all-categories'){s.categories=[];refresh(true);}
    if(data.action==='all-tasks'){resetFilters();s.view='tasks';refresh(true);}
    if(data.action==='clear-task'){s.task='';refresh(true);}
    if(data.action==='clear-type'){s.type='';refresh(true);}
    if(data.action==='clear-similar'){s.similar='';refresh(true);}
    if(data.action==='update-help')$('updateDialog').showModal();
    if(data.action==='copy-update')L.copy('python ai.py repos build');
    if(data.action==='copy-source')L.copy(L.data.sourceMarkdown);
    if(data.action==='clear-compare'){s.compare=[];refresh();}
    if(data.action==='show-compare'&&s.compare.length>=2){L.renderComparison();$('compareDialog').showModal();}
  });
  $('query').addEventListener('input',event=>{L.state.query=event.target.value;L.state.task='';L.state.similar='';if(L.state.view==='source')L.state.view='explore';refresh(true);});
  document.addEventListener('change',event=>{
    if(event.target.id==='typeFilter'){L.state.type=event.target.value;refresh(true);}
    if(event.target.id==='sortFilter'){L.state.sort=event.target.value;refresh(true);}
  });
  document.addEventListener('keydown',event=>{
    if((event.ctrlKey||event.metaKey)&&event.key.toLowerCase()==='k'){
      event.preventDefault();if(document.querySelector('dialog[open]'))return;$('query').focus();$('query').select();return;
    }
    if(!['ArrowDown','ArrowUp'].includes(event.key)||document.querySelector('dialog[open]'))return;
    const buttons=[...document.querySelectorAll('#resultList [data-open]')];if(!buttons.length)return;
    const current=buttons.indexOf(document.activeElement);
    if(document.activeElement.id!=='query'&&current<0)return;
    event.preventDefault();const next=current<0?0:(current+(event.key==='ArrowDown'?1:-1)+buttons.length)%buttons.length;
    buttons[next].focus();buttons[next].scrollIntoView({block:'nearest'});
  });
  window.addEventListener('hashchange',()=>{
    if(location.hash.includes('view=')||location.hash.includes('repo=')){L.readHash(L.state,L.data);refresh();if(['explore','saved'].includes(L.state.view)&&matchMedia('(max-width:1020px)').matches&&L.state.selected){L.renderMobileDetail();if(!$('repoDialog').open)$('repoDialog').showModal();}}
  });
  matchMedia('(max-width:1020px)').addEventListener('change',event=>{if(!event.matches)closeRepo();});
  refresh();
  if(initialRepoLink&&['explore','saved'].includes(L.state.view)&&L.state.selected&&matchMedia('(max-width:1020px)').matches){L.renderMobileDetail();$('repoDialog').showModal();}
})(window.RepoLibrary);
