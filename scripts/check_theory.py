#!/usr/bin/env python3
"""Check data integrity, bilingual coverage, local links and illustrative arithmetic.

Passing these checks does not validate the social hypotheses.
"""
import itertools
import json
import math
import re
from pathlib import Path
from urllib.parse import unquote
from explore_theory import unrank

ROOT=Path(__file__).resolve().parents[1]
T=ROOT/'theory'
v=json.loads((T/'data/variables.json').read_text())['variables']
d=json.loads((T/'data/pathways.json').read_text())['pathways']
assert [x['id'] for x in v]==[f'V{i:03}' for i in range(1,129)]
assert [x['id'] for x in d]==[f'D{i:03}' for i in range(1,65)]
assert [sum(x['order']==k for x in d) for k in [2,3,4]]==[32,20,12]
known={x['id'] for x in v}
for item in d:
    assert len(set(item['variables']))==item['order']
    assert set(item['variables'])<=known
    assert item['status']=='H'
    assert set(item['references'])<={f'R{i:02}' for i in range(1,16)}|{'MODEL'}
    for field in ['title','mechanism','branch_a','branch_b','test']:
        assert all(item[field][lang].strip() for lang in ['zh','en'])
for item in v:
    for field in ['name','definition','proxy','trajectory']:
        assert all(item[field][lang].strip() for lang in ['zh','en'])
for stem in ['01-foundations','02-variable-atlas','03-derivation-pool','04-games-and-models','05-research-protocol']:
    a=(T/f'{stem}.zh-CN.md').read_text(); b=(T/f'{stem}.en.md').read_text()
    pattern={'01-foundations':r'### (P\d\d)', '02-variable-atlas':r'\| (V\d{3}) \|','03-derivation-pool':r'### (D\d{3})', '04-games-and-models':r'## (M\d\d)'}.get(stem)
    if pattern: assert re.findall(pattern,a)==re.findall(pattern,b),stem
assert len(re.findall(r'[\u4e00-\u9fff]',(T/'01-foundations.zh-CN.md').read_text()))>=10000
for path in [ROOT/'README.md', ROOT/'README.en.md',*T.rglob('*.md')]:
    text=path.read_text()
    assert text.count('```')%2==0,path
    for target in re.findall(r'\]\(([^)]+)\)',text):
        if re.match(r'^[a-z]+:',target) or target.startswith('#'): continue
        target=unquote(target.split('#',1)[0])
        assert (path.parent/target).exists(),(path,target)
    for target in re.findall(r'<img[^>]+src="([^"]+)"',text):
        assert (path.parent/target).exists(),(path,target)

# Exhaustively compare small enumerations, plus full-catalog boundaries.
for n in range(2,9):
    for k in range(2,min(4,n)+1):
        items=list(range(n))
        for rank,combo in enumerate(itertools.combinations(items,k)):
            assert unrank(items,k,rank)==combo
assert unrank(list(range(128)),4,math.comb(128,4)-1)==(124,125,126,127)
assert [math.comb(128,k) for k in [2,3,4]]==[8128,341376,10668000]
assert sum(math.comb(128,k) for k in [2,3,4])==11017504

# M01 allocation arithmetic.
assert 60/30==2 and 60/60==1
# M02 and M03: enumerate pure Nash equilibria from payoff matrices.
def equilibria(game):
    return [(i,j) for i in range(2) for j in range(2)
            if all(game[i][j][0]>=game[k][j][0] for k in range(2))
            and all(game[i][j][1]>=game[i][k][1] for k in range(2))]
base=[[(3,3),(1,4)],[(4,1),(2,2)]]
assert equilibria(base)==[(1,1)]
for penalty,expected in [(0.5,[(1,1)]),(1,[(0,0),(0,1),(1,0),(1,1)]),(2,[(0,0)])]:
    adjusted=[[(a-penalty*i,b-penalty*j) for j,(a,b) in enumerate(row)] for i,row in enumerate(base)]
    assert equilibria(adjusted)==expected
coord=[[(4,4),(0,2)],[(2,0),(2,2)]]
assert equilibria(coord)==[(0,0),(1,1)] and 4*0.5==2
# M04–M08: thresholds, labor ratios, bargaining, skill stocks, full costs.
assert 2-0.1*10==1 and 2-0.3*10==-1
assert math.isclose(0.5*0.5**-0.5,math.sqrt(0.5))
assert 0.5*0.5**-1==1 and 0.5*0.5**-2==2
assert 0.2*100==20 and 0.6*100==60
assert 2/0.1==20 and 4/0.1==40
assert math.isclose(100*(1+0.2),120) and math.isclose(1000*(0.1+0.2),300)
assert math.isclose(0.6*2,1.2)
print('PASS: 128 variables; 64 cards (32/20/12); bilingual IDs; links; >10,000 Chinese characters; tuple enumeration; eight model examples.')
