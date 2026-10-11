(function (L) {
  "use strict";
  L.escape = value => String(value ?? "").replace(/[&<>"']/g,char=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[char]));
  const paths = {
    search:'<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 4 4"/>',
    library:'<path d="M4 4h5v16H4zM12 4h3v16h-3zM18 5l3-1 4 15-3 1z"/>',
    tasks:'<path d="M9 6h12M9 12h12M9 18h12M3 6h1M3 12h1M3 18h1"/>',
    route:'<circle cx="5" cy="5" r="2"/><circle cx="19" cy="19" r="2"/><path d="M7 5h8a4 4 0 0 1 0 8H9a4 4 0 0 0 0 8h8"/>',
    bookmark:'<path d="M6 3h12v18l-6-4-6 4z"/>',
    compare:'<path d="M3 5h7v14H3zM14 5h7v14h-7z"/>',
    arrow:'<path d="M5 12h14m-5-5 5 5-5 5"/>',
    external:'<path d="M14 3h7v7M21 3l-9 9M10 3H4v17h17v-6"/>',
    copy:'<path d="M9 9h12v12H9zM15 9V3H3v12h6"/>',
    moon:'<path d="M20.5 14A9 9 0 0 1 10 3.5 9 9 0 1 0 20.5 14z"/>',
    sun:'<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M5 19l1.5-1.5M17.5 6.5 19 5"/>'
  };
  L.icon = name => '<svg viewBox="0 0 24 24" aria-hidden="true">'+(paths[name]||paths.library)+'</svg>';
  const key = "ai-company-os-repo-library-v1";
  L.storageAvailable = true;
  function load() {try{const cache=JSON.parse(localStorage.getItem(key)||"{}");return cache&&typeof cache==='object'&&!Array.isArray(cache)?cache:{};}catch{L.storageAvailable=false;return {};}}
  L.initialState = function(data) {
    const cache=load();const repoIds=new Set(data.repos.map(repo=>repo.id));
    const validViews=["explore","tasks","routes","saved","source"];
    const saved=cache.filters||{};
    const state={view:validViews.includes(saved.view)?saved.view:"explore",query:String(saved.query||""),categories:Array.isArray(saved.categories)?saved.categories.filter(id=>data.categories.some(category=>category.id===id)):[],type:String(saved.type||""),sort:["relevance","name","stars","downloaded","updated"].includes(saved.sort)?saved.sort:"relevance",task:data.tasks.some(task=>task.id===saved.task)?saved.task:"",similar:"",selected:repoIds.has(saved.selected)?saved.selected:"",goal:data.discovery.goals.some(goal=>goal.id===saved.goal)?saved.goal:"",favorites:Array.isArray(cache.favorites)?cache.favorites.filter(id=>repoIds.has(id)):[],recent:Array.isArray(cache.recent)?cache.recent.filter(id=>repoIds.has(id)).slice(0,12):[],compare:[],theme:cache.theme==="dark"?"dark":"light"};
    const types=new Set(data.repos.flatMap(repo=>repo.types));if(!types.has(state.type))state.type='';
    L.readHash(state,data);return state;
  };
  L.readHash = function(state,data) {
    const params=new URLSearchParams(location.hash.slice(1));
    if(!params.has("view")&&!params.has("repo"))return;
    if(["explore","tasks","routes","saved","source"].includes(params.get("view")))state.view=params.get("view");
    state.query=params.get("q")||"";
    state.categories=(params.get("categories")||"").split(",").filter(id=>data.categories.some(category=>category.id===id));
    state.type=data.repos.some(repo=>repo.types.includes(params.get("type")))?params.get("type"):"";
    state.task=data.tasks.some(task=>task.id===params.get("task"))?params.get("task"):"";
    state.similar=data.repos.some(repo=>repo.id===params.get("similar"))?params.get("similar"):"";
    state.selected=data.repos.some(repo=>repo.id===params.get("repo"))?params.get("repo"):"";
    if(["relevance","name","stars","downloaded","updated"].includes(params.get("sort")))state.sort=params.get("sort");
  };
  L.persist = function() {
    const s=L.state;
    try{localStorage.setItem(key,JSON.stringify({favorites:s.favorites,recent:s.recent,theme:s.theme,filters:{view:s.view,query:s.query,categories:s.categories,type:s.type,sort:s.sort,task:s.task,selected:s.selected,goal:s.goal}}));}catch{L.storageAvailable=false;}
    const params=new URLSearchParams({view:s.view});
    for(const [name,value] of [["q",s.query],["repo",s.selected],["categories",s.categories.join(",")],["type",s.type],["task",s.task],["similar",s.similar],["sort",s.sort!=="relevance"?s.sort:""]])if(value)params.set(name,value);
    const hash="#"+params.toString();
    if(location.hash!==hash){try{history.replaceState(null,"",hash);}catch{/* file:// or hardened browsers can deny history writes. */}}
  };
  L.notify = function(message) {
    const toast=document.getElementById("toast");toast.textContent=message;toast.hidden=false;
    clearTimeout(L.toastTimer);L.toastTimer=setTimeout(()=>toast.hidden=true,2800);
  };
  L.copy = async function(text) {
    try{if(!navigator.clipboard?.writeText)throw new Error("clipboard");await navigator.clipboard.writeText(text);L.notify("In die Zwischenablage kopiert.");}
    catch{document.getElementById("copyText").value=text;document.getElementById("copyDialog").showModal();document.getElementById("copyText").focus();document.getElementById("copyText").select();}
  };
  L.localHref = path => encodeURI(L.data.libraryRoot.replace(/\/$/,"")+"/"+path).replace(/#/g,"%23").replace(/\?/g,"%3F");
  L.highlight = function(text) {
    const groups=L.search.groups(L.state.query,L.data.discovery);
    return String(text).split(/([\p{L}\p{N}][\p{L}\p{N}.-]*)/u).map(part=>{
      const normalized=L.search.normalize(part);
      return groups.some(group=>normalized.includes(group.term)||group.aliases.some(alias=>normalized===alias))?"<mark>"+L.escape(part)+"</mark>":L.escape(part);
    }).join("");
  };
})(window.RepoLibrary);
