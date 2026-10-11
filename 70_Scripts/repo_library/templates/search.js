(function (L) {
  "use strict";
  const normalize = text => String(text || "").toLowerCase().replace(/ß/g,"ss").normalize("NFKD").replace(/[\u0300-\u036f]/g,"");
  function terms(query, config) {
    const stop = new Set(config.stopwords.map(normalize));
    return [...new Set(normalize(query).match(/[\p{L}\p{N}.-]+/gu) || [])].filter(term => term.length > 1 && !stop.has(term));
  }
  function groups(query, config) {
    return terms(query,config).map(term => {
      const group = config.synonyms.find(values => values.some(value => normalize(value) === term));
      return {term, aliases: group ? group.map(normalize) : []};
    });
  }
  function contains(text, term) {
    if (term.length < 4) return new RegExp("(?:^|[^a-z0-9])" + term.replace(/[.*+?^${}()|[\]\\]/g,"\\$&") + "(?:$|[^a-z0-9])").test(text);
    return text.includes(term);
  }
  function score(text, queryGroups, weight) {
    const normalized = normalize(text);
    return queryGroups.reduce((total, group) => total + (contains(normalized,group.term) ? weight : group.aliases.some(alias => contains(normalized,alias)) ? weight * .28 : 0),0);
  }
  function taskResults(data, query) {
    const queryGroups = groups(query,data.discovery);
    return data.tasks.map(task => ({task,score:score(task.title,queryGroups,12)+score(task.description,queryGroups,3)})).filter(result => !queryGroups.length || result.score > 0).sort((a,b)=>b.score-a.score || a.task.title.localeCompare(b.task.title,"de"));
  }
  function excerpt(text, query, config) {
    const normalized=normalize(text);
    const indices=groups(query,config).flatMap(group=>[group.term,...group.aliases].map(term=>normalized.indexOf(term))).filter(index=>index>=0);
    if(!indices.length)return '';
    const position=Math.min(...indices),start=Math.max(0,position-55),end=Math.min(text.length,position+155);
    return (start?'…':'')+text.slice(start,end)+(end<text.length?'…':'');
  }
  function repoResults(data, query) {
    const queryGroups = groups(query,data.discovery);
    const taskMatches = queryGroups.length ? taskResults(data,query).slice(0,5) : [];
    return data.repos.map(repo => {
      const taskMatch = taskMatches.find(result => result.task.repoIds.includes(repo.id));
      const direct = score(repo.label,queryGroups,15)+score(repo.purposes.join(" "),queryGroups,8)+score(repo.features.join(" "),queryGroups,4)+score(repo.text,queryGroups,1.2);
      return {repo,score:direct+(taskMatch ? taskMatch.score*2.5 : 0),reason:taskMatch ? taskMatch.task.title : "",reasonType:taskMatch ? "Aufgabe" : "Texttreffer",excerpt:queryGroups.length?excerpt(repo.text,query,data.discovery):''};
    }).filter(result=>!queryGroups.length || result.score>0).sort((a,b)=>b.score-a.score || a.repo.label.localeCompare(b.repo.label,"de"));
  }
  function similar(data, id) {
    const basis = data.repos.find(repo=>repo.id===id);
    if (!basis) return [];
    return data.repos.filter(repo=>repo.id!==id).map(repo=>{
      const commonTasks = repo.taskIds.filter(task=>basis.taskIds.includes(task));
      const commonCategories = repo.categories.filter(category=>basis.categories.includes(category));
      const task = data.tasks.find(task=>task.id===commonTasks[0]);
      const category = data.categories.find(category=>category.id===commonCategories[0]);
      return {repo,score:commonTasks.length*12+commonCategories.length*3,reason:task ? task.title : category ? category.title : "",reasonType:task ? "Gemeinsame Aufgabe" : "Gemeinsames Thema"};
    }).filter(result=>result.score>0).sort((a,b)=>b.score-a.score || a.repo.label.localeCompare(b.repo.label,"de"));
  }
  L.search = {normalize,terms,groups,taskResults,repoResults,similar,excerpt};
})(window.RepoLibrary = window.RepoLibrary || {});
