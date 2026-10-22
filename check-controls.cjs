const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const providers = ['aws', 'gcp', 'azure'];
const panels = providers.map(id => ({id: 'panel-' + id, hidden: false}));
const buttons = providers.map(provider => ({dataset: {provider}, attributes: {}, events: {}, setAttribute(k,v) {this.attributes[k]=v;}, addEventListener(k,v) {this.events[k]=v;}}));
const source = fs.readFileSync(__dirname + '/site.js', 'utf8');
vm.runInNewContext(source, {document: {querySelectorAll(s) {return s==='[data-provider]' ? buttons : panels;}}});
function verify(id) {
  assert.deepEqual(panels.filter(p=>!p.hidden).map(p=>p.id), ['panel-'+id]);
  assert.deepEqual(buttons.filter(b=>b.attributes['aria-pressed']==='true').map(b=>b.dataset.provider), [id]);
}
verify('aws');
for (const id of ['gcp','azure','aws','gcp','azure']) {buttons.find(b=>b.dataset.provider===id).events.click();verify(id);}
vm.runInNewContext(source, {document: {querySelectorAll() {return [];}}});
console.log('PASS: initial and repeated provider selections, accessible state, exactly one visible panel, safe on index pages.');
