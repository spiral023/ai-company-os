import fs from 'node:fs';
import {extractTweetText, orderThreadChronologically} from './x-ingest.mjs';

export const SOURCE_THREAD_POLICY=JSON.parse(fs.readFileSync(new URL('../config/x-thread-content.json',import.meta.url),'utf8'));
export function replyParent(tweet) {
  return (tweet?.referenced_tweets ?? []).find(reference=>reference.type==='replied_to')?.id ?? null;
}
export function isPromotionOnly(tweet) {
  const text=extractTweetText(tweet).replace(/\s+/g,' ').trim();
  if(tweet?.article || tweet?.attachments?.media_keys?.length || text.length>240)return false;
  return /^(?:I've posted (?:a )?(?:(?:refined|updated|new) )?v\d+\.?\s*)?Follow (?:me )?for more(?: updates)?[!. ]*$/i.test(text)
    || /^If this helped .{0,100}consider sponsoring my research\b/i.test(text)
    || /^(?:Thanks|Thank you|You're welcome|Great|Nice|Awesome|Cool|Exactly|Agreed)[!. ]*$/i.test(text);
}

// Nicht alle Antworten eines Autors in einer conversation_id sind ein Thread.
// Nur lückenlos belegte Selbst-Antworten des Quellenautors bilden Fortsetzungen.
// Fremde Vorfahren dienen höchstens der technischen Auflösung, nie dem Inhalt.
export function filterSourceThread(tweet, candidates, policy=SOURCE_THREAD_POLICY) {
  const byId=new Map((candidates ?? []).filter(t=>t?.id).map(t=>[t.id,t]));
  if(tweet?.id)byId.set(tweet.id,{...byId.get(tweet.id),...tweet});
  const requested=byId.get(tweet?.id) ?? tweet;
  let anchor=requested;
  const visited=new Set();
  while(anchor?.author_id && !visited.has(anchor.id)) {
    visited.add(anchor.id);
    const parent=byId.get(replyParent(anchor));
    if(!parent || parent.author_id!==requested.author_id)break;
    anchor=parent;
  }
  if(!anchor?.id)return {anchor:tweet,thread:[],excluded:[],supplements:[]};
  const accepted=new Set([anchor.id]);
  const posts=orderThreadChronologically([...byId.values()]);
  let changed=true;
  while(changed) {
    changed=false;
    for(const post of posts) {
      if(accepted.has(post.id)||!anchor.author_id||post.author_id!==anchor.author_id||isPromotionOnly(post))continue;
      if(accepted.has(replyParent(post))) {accepted.add(post.id);changed=true;}
    }
  }
  const supplements=[];
  for(const id of policy.supplements?.[anchor.id] ?? []) {
    const post=byId.get(id);
    if(post?.author_id===anchor.author_id&&!accepted.has(id)&&!isPromotionOnly(post)) {accepted.add(id);supplements.push(id);}
  }
  const excluded=posts.filter(post=>!accepted.has(post.id)).map(post=>({id:post.id,
    reason:post.author_id!==anchor.author_id?'foreign-author':isPromotionOnly(post)?'promotion-or-smalltalk':'outside-author-chain'}));
  return {anchor,thread:posts.filter(post=>accepted.has(post.id)),excluded,supplements};
}

export function filterCachedThread(payload, policy=SOURCE_THREAD_POLICY) {
  if(!payload?.thread?.length)return {payload,excluded:[]};
  // Ältere Abrufe können über eine inzwischen einzeln geprüfte Ergänzung
  // eingestiegen sein. Ihr expliziter Quellenanker muss beim Cache-Replay bleiben.
  const reviewedAnchor=payload.thread.find(post=>post.author_id===payload.tweet?.author_id&&policy.supplements?.[post.id]?.includes(payload.tweet?.id));
  const selection=filterSourceThread(reviewedAnchor ?? payload.tweet,payload.thread,policy);
  return {payload:{...payload,thread:selection.thread,threadFilter:policy.version,
    threadSupplements:selection.supplements,
    threadFiltered:(payload.threadFiltered ?? 0)+selection.excluded.length},excluded:selection.excluded};
}
