// Nativer Dialog: Fokus bleibt im Lesemodus/in der Galerie; Escape schließt.
const esc=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export function createViewer({loadDetails,controls}) {
  const dialog=document.getElementById('viewer'), content=document.getElementById('viewer-content'), title=document.getElementById('viewer-title');
  let trigger, request=0, activeEntry, mode='', images=[], imageIndex=0;
  function open(entry,button,type) {
    trigger=button;activeEntry=entry;mode=type;request++;
    dialog.dataset.mode=type;
    title.textContent=entry.source_title||entry.title;
    title.title=title.textContent;
    content.replaceChildren();
    document.getElementById('viewer-status').textContent='';
    document.body.classList.add('viewer-open');
    if(!dialog.open)dialog.showModal();
    dialog.scrollTop=0;
    document.getElementById('viewer-close').focus({preventScroll:true});
    return request;
  }
  async function openReader(entry,button) {
    const current=open(entry,button,'reader');
    content.innerHTML='<p class="muted" role="status">Artikel wird geladen …</p>';
    try {
      const detail=await loadDetails(entry);
      if(current!==request||!dialog.open)return;
      const transcript=!entry.has_source&&!!detail.transcript_html;
      const source=entry.has_source?detail.source_html:detail.transcript_html||detail.original_html;
      const notice=transcript?`<p class="notice">${esc(detail.transcript_info)}<br>${esc(detail.transcript_warning)}</p>`:!entry.has_source&&entry.translation_notice?`<p class="notice">${esc(entry.translation_notice)}</p>`:'';
      content.innerHTML=`<div class="reader-toolbar"><div class="personal-actions" data-viewer-personal>${controls(entry)}</div>${entry.has_source?'<button class="reader-original-toggle" data-reader-original aria-pressed="false">Original daneben</button>':''}${entry.url?`<a href="${esc(entry.url)}" target="_blank" rel="noopener noreferrer">Quelle öffnen ↗</a>`:''}</div><details class="reader-index" hidden><summary>Inhalt</summary><nav aria-label="Inhaltsverzeichnis"></nav></details><div class="reader-shell"><div class="reader-copy prose">${notice}${source||'<p>Kein Text archiviert.</p>'}</div><aside class="reader-original prose" aria-label="Originaltext zum Vergleich" hidden><p class="content-label">${esc(entry.original_label)}</p>${entry.translation_notice?`<p class="notice">${esc(entry.translation_notice)}</p>`:''}${detail.original_html||'<p>Originalinhalt über den Quellenlink öffnen.</p>'}</aside></div>`;
      const headings=[...content.querySelectorAll('.reader-copy h2,.reader-copy h3')];
      const nav=content.querySelector('.reader-index nav');
      headings.forEach((heading,index)=>{
        heading.id=`reader-section-${index}`;
        const button=document.createElement('button');button.type='button';button.dataset.readerSection=heading.id;button.textContent=heading.textContent;
        nav.append(button);
      });
      content.querySelector('.reader-index').hidden=!headings.length;
    }catch{
      if(current===request&&dialog.open)content.innerHTML='<p class="error-message" role="alert">Der Artikel konnte nicht geladen werden. Bitte schließen und erneut öffnen.</p>';
    }
  }
  function drawImage() {
    const media=images[imageIndex];
    content.innerHTML=`<div class="gallery-toolbar"><button data-image-step="-1" aria-label="Vorheriges Bild"${images.length<2?' disabled':''}>←</button><span aria-live="polite">${imageIndex+1} / ${images.length}</span><button data-image-step="1" aria-label="Nächstes Bild"${images.length<2?' disabled':''}>→</button><a href="${esc(media.src)}" target="_blank" rel="noopener">Bilddatei öffnen ↗</a></div><figure class="gallery-figure"><img src="${esc(media.src)}" alt="${esc(media.alt)}"><figcaption>${esc(media.alt==='photo'?'':media.alt)}</figcaption></figure>`;
  }
  function openGallery(entry,button,index=0) {
    images=entry.media.filter(media=>media.kind==='image');
    if(!images.length)return;
    imageIndex=Math.max(0,Math.min(index,images.length-1));
    open(entry,button,'gallery');drawImage();
  }
  function step(amount) {
    // Fokus auf dem Navigationsbutton trotz Bildwechsel erhalten.
    const action=document.activeElement?.dataset.imageStep;
    imageIndex=(imageIndex+amount+images.length)%images.length;drawImage();
    if(action)content.querySelector(`[data-image-step="${action}"]`)?.focus({preventScroll:true});
  }
  dialog.addEventListener('click',event=>{
    const button=event.target.closest('button');
    if(button?.hasAttribute('data-image-step'))step(Number(button.dataset.imageStep));
    if(button?.hasAttribute('data-reader-section'))document.getElementById(button.dataset.readerSection)?.scrollIntoView({block:'start',behavior:'instant'});
    if(button?.hasAttribute('data-reader-original')){
      const show=button.getAttribute('aria-pressed')!=='true';button.setAttribute('aria-pressed',show);
      content.querySelector('.reader-original').hidden=!show;content.querySelector('.reader-shell').classList.toggle('with-original',show);
    }
    if(event.target===dialog){const rect=dialog.getBoundingClientRect();if(event.clientX<rect.left||event.clientX>rect.right||event.clientY<rect.top||event.clientY>rect.bottom)dialog.close();}
  });
  dialog.addEventListener('keydown',event=>{
    if(mode==='gallery'&&['ArrowLeft','ArrowRight'].includes(event.key)){event.preventDefault();step(event.key==='ArrowRight'?1:-1);}
  });
  document.getElementById('viewer-close').addEventListener('click',()=>dialog.close());
  dialog.addEventListener('close',()=>{
    request++;document.body.classList.remove('viewer-open');content.replaceChildren();
    if(trigger?.isConnected)trigger.focus({preventScroll:true});else document.getElementById('search').focus({preventScroll:true});
  });
  return {openReader,openGallery,announce(message){document.getElementById('viewer-status').textContent=message;},refreshPersonal(){if(dialog.open&&mode==='reader'){
    const slot=content.querySelector('[data-viewer-personal]');
    if(slot){const action=document.activeElement?.dataset.personal;slot.innerHTML=controls(activeEntry);if(action)slot.querySelector(`[data-personal="${action}"]`)?.focus({preventScroll:true});}
  }}};
}
