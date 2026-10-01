import {forward,reset,previous,consumedKey} from './state.mjs';
const frame=document.querySelector('#frame'),stage=document.querySelector('#stage'),pointer=document.querySelector('#pointer'),status=document.querySelector('#status');
const scenes=[...document.querySelectorAll('.scene')],counts=scenes.map(s=>Number(s.dataset.beats));
let state=reset(),animations=[],timers=[],generation=0;
const media=matchMedia('(prefers-reduced-motion: reduce)');
function cancel(){generation++;timers.forEach(clearTimeout);timers=[];animations.forEach(a=>a.cancel());animations=[];}
function endpoint(){
 scenes.forEach((s,i)=>{s.hidden=i!==state.scene;s.setAttribute('aria-hidden',String(i!==state.scene));s.style.opacity='1';
  if(i===state.scene)s.querySelectorAll('[data-beat]').forEach(o=>{o.hidden=Number(o.dataset.beat)>state.beat||o.dataset.failed==='true';o.style.opacity='1';});});
 stage.dataset.scene=scenes[state.scene].id;stage.dataset.beat=String(state.beat);stage.dataset.phase=state.phase;
}
function announce(){const s=scenes[state.scene];status.textContent=s.dataset.description+' '+[...s.querySelectorAll('.text:not([hidden])')].map(x=>x.textContent).join('. ');}
function hold(){cancel();state={...state,phase:'hold'};endpoint();announce();}
function schedule(next){
 const old={...state};cancel();state=next;endpoint();
 if(state.phase==='hold'||media.matches){hold();return;}
 const token=generation;
 const entering=state.scene!==old.scene;
 const target=scenes[state.scene];
 const newObjects=[...target.querySelectorAll('[data-beat]')].filter(o=>Number(o.dataset.beat)===state.beat);
 let duration=entering?350:650;
 if(entering){const prior=scenes[old.scene];prior.hidden=false;prior.setAttribute('aria-hidden','true');
  animations.push(prior.animate([{opacity:1},{opacity:0}],{duration,easing:'linear',fill:'both'}));
  animations.push(target.animate([{opacity:0},{opacity:1}],{duration,easing:'linear',fill:'both'}));
 }else newObjects.forEach(o=>animations.push(o.animate([{opacity:0},{opacity:1}],{duration,easing:'cubic-bezier(0.22,1,0.36,1)',fill:'both'})));
 timers.push(setTimeout(()=>{if(token!==generation)return; state={...state,phase:'settle'};stage.dataset.phase='settle';
  timers.push(setTimeout(()=>{if(token===generation)hold();},200));},duration));
}
addEventListener('keydown',event=>{const key=consumedKey(event);if(!key)return;event.preventDefault();
 if(key==='forward') {if(state.phase!=='hold')hold();else schedule(forward(state,counts));}
 if(key==='reset'){cancel();state=reset();endpoint();announce();}
 if(key==='previous')schedule(previous(state,counts));
 if(key==='fullscreen'){try{const request=document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();Promise.resolve(request).catch(()=>{status.textContent='Fullscreen unavailable. The presentation remains ready.';});}catch{status.textContent='Fullscreen unavailable. The presentation remains ready.';}}
});
function hidePointer(){pointer.hidden=true;frame.classList.remove('pointer-active');}
function fit(){document.documentElement.style.setProperty('--scale',Math.min(innerWidth/1920,innerHeight/1080));hidePointer();}
addEventListener('resize',fit);addEventListener('blur',hidePointer);frame.addEventListener('pointerleave',hidePointer);
frame.addEventListener('pointermove',event=>{if(event.pointerType!=='mouse'){hidePointer();return;}try{
 const r=frame.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom){hidePointer();return;}
 pointer.style.left=event.clientX+'px';pointer.style.top=event.clientY+'px';pointer.hidden=false;if(pointer.isConnected&&pointer.getBoundingClientRect().width===14)frame.classList.add('pointer-active');else hidePointer();
}catch{hidePointer();}});
media.addEventListener('change',()=>{if(media.matches)hold();});
document.querySelectorAll('img[data-fallback]').forEach(img=>{const onError=()=>{if(!img.dataset.fallbackUsed){img.dataset.fallbackUsed='true';img.src=img.dataset.fallback;}else{img.hidden=true;status.textContent='Image unavailable. Restart the presentation.';img.dataset.failed='true';}};img.addEventListener('error',onError);if(img.complete&&!img.naturalWidth)onError();});
fit();endpoint();announce();
