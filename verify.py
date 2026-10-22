"""Offline checks for static hosting, cloud views, relative paths, and privacy."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from xml.etree import ElementTree as ET
import json,re
from cloud import PROVIDERS,ROLES,SERVICES,choice
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'dist'
data=json.loads((ROOT/'content.json').read_text())
class Page(HTMLParser):
 def __init__(self,path):
  super().__init__();self.path=path;self.ids=[];self.links=[];self.buttons=[];self.panels=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  assert tag not in {'form','input','textarea','iframe','embed','object'},(self.path,tag)
  if tag=='h1':self.h1+=1
  if 'id' in a:
   assert a['id'] not in self.ids,(self.path,'duplicate id',a['id'])
   self.ids.append(a['id'])
  if tag=='button' and 'data-provider' in a:self.buttons.append(a)
  if 'provider-panel' in a.get('class','').split():self.panels.append(a)
  if tag=='img':assert a.get('alt'),(self.path,'image needs alt text')
  if tag=='script':assert a.get('src') in {'site.js','../../site.js'},(self.path,'unapproved script')
  for key in ('href','src'):
   if key in a:self.links.append(a[key])
pages={}
for path in OUT.rglob('*.html'):
 p=Page(path);p.feed(path.read_text());assert p.h1==1,(path,'exactly one h1 required');pages[path.resolve()]=p
assert len(pages)==29
for path,p in pages.items():
 for link in p.links:
  u=urlsplit(link)
  if u.scheme:assert u.scheme=='https';continue
  assert not link.startswith('/'),(path,link,'must be relative for repository subpaths')
  target=(path.parent/unquote(u.path)).resolve() if u.path else path
  assert target.is_relative_to(OUT.resolve()),(path,link,'outside static artifact')
  assert target.is_file(),(path,link,'broken asset or navigation')
  if u.fragment:assert target in pages and u.fragment in pages[target].ids,(path,link,'broken anchor')
 if p.buttons:
  assert [b['data-provider'] for b in p.buttons]==list(PROVIDERS)
  assert [s['id'] for s in p.panels]==['panel-'+v for v in PROVIDERS]
  assert all('hidden' not in s for s in p.panels),'no-JavaScript fallback must stay visible'
  assert [b['aria-pressed'] for b in p.buttons]==['true','false','false']
  for b in p.buttons:assert b['aria-controls'] in p.ids
assert sum(bool(p.buttons) for p in pages.values())==20
for path in OUT.rglob('*'):
 if not path.is_file():continue
 assert not path.is_symlink(),path
 if path.suffix in {'.html','.css','.js','.svg'}:
  text=path.read_text().lower()
  for pattern in ['document.cookie','localstorage','sessionstorage','googletagmanager','google-analytics','fetch(','xmlhttprequest','sendbeacon','websocket(','@import','url(http']:
   assert pattern not in text,(path,pattern)
for path in (OUT/'diagrams').glob('*.svg'):ET.parse(path)
assert len(list((OUT/'diagrams').glob('*.svg')))==62
ids={x['id'] for x in data['architectures']};assert set(ROLES)==ids
for x in data['architectures']:
 assert len(x['flow'])==len(ROLES[x['id']])==5
 for role in ROLES[x['id']]:assert role in SERVICES and len(SERVICES[role])==3
 for provider in PROVIDERS:
  diagram=(OUT/'diagrams'/f'{x["id"]}-{provider}.svg').read_text()
  for role in ROLES[x['id']]:assert choice(role,provider)['name'].split()[0] in diagram
for category in data['categories']:
 assert any(category['id'] in x['categories'] for x in data['architectures'])
assert (OUT/'.nojekyll').is_file()
yml=(ROOT/'.github/workflows/pages.yml').read_text()
for required in ['path: dist','needs: build','pages: write','id-token: write','name: github-pages','github.event.repository.default_branch',"github.event_name != 'pull_request'"]:
 assert required in yml,required
assert not re.search(r'(?:github_pat_|ghp_)[A-Za-z0-9_]+',yml)
print('PASS: 29 pages; 62 valid SVGs; 20 complete cloud selectors; links, anchors, and assets resolve; relative subpaths; no forms, trackers, visitor storage, external assets, or network-call code; Pages artifact and permissions configured.')
