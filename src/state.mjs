/** Pure state transitions. Timing belongs to the renderer, never narration. */
export function forward(state, counts) {
  if (state.phase !== 'hold') return {...state, phase:'hold'};
  if (state.beat + 1 < counts[state.scene]) return {...state, beat:state.beat+1, phase:'reveal'};
  if (state.scene + 1 < counts.length) return {scene:state.scene+1,beat:0,phase:'transition'};
  return state;
}
export const reset = () => ({scene:0,beat:0,phase:'hold'});
export function previous(state,counts) { const scene=Math.max(0,state.scene-1); return {scene,beat:scene===0?0:counts[scene]-1,phase:'hold'}; }
export function consumedKey(event) {
  if(event.repeat || event.ctrlKey || event.altKey || event.metaKey || event.shiftKey) return null;
  const target=event.target;
  if(target?.isContentEditable || target?.closest?.('input,textarea,select,[contenteditable]')) return null;
  return ({' ':'forward','r':'reset','R':'reset','ArrowLeft':'previous','f':'fullscreen','F':'fullscreen'})[event.key] ?? null;
}
