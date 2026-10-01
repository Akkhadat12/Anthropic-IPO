import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {forward,reset,previous,consumedKey} from '../src/state.mjs';
const scenes=JSON.parse(fs.readFileSync(new URL('../references/visual-scenes.json',import.meta.url)));
const counts=scenes.map(s=>s.beats.length);
test('complete forward route visits exactly 23 endpoints and never wraps',()=>{
 let state=reset(),visited=[`${state.scene}:${state.beat}`];
 for(let i=0;i<22;i++){state=forward(state,counts);assert.notEqual(state.phase,'hold');const settling=forward(state,counts);assert.equal(settling.scene,state.scene);assert.equal(settling.beat,state.beat);state=settling;visited.push(`${state.scene}:${state.beat}`);}
 assert.equal(new Set(visited).size,23);assert.deepEqual(state,{scene:8,beat:2,phase:'hold'});assert.deepEqual(forward(state,counts),state);
});
test('reset and back are deterministic settled endpoints',()=>{assert.deepEqual(reset(),{scene:0,beat:0,phase:'hold'});assert.deepEqual(previous({scene:0,beat:0},counts),reset());assert.deepEqual(previous({scene:3,beat:1},counts),{scene:2,beat:2,phase:'hold'});});
test('ignore held keys, modifiers, and editable targets',()=>{for(const prop of ['repeat','ctrlKey','metaKey','altKey','shiftKey'])assert.equal(consumedKey({key:' ',[prop]:true}),null);assert.equal(consumedKey({key:' ',target:{isContentEditable:true}}),null);assert.equal(consumedKey({key:'r',target:{closest:()=>({})}}),null);assert.equal(consumedKey({key:' '}),'forward');assert.equal(consumedKey({key:'r'}),'reset');assert.equal(consumedKey({key:'p'}),null);});
