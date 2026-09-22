#!/usr/bin/env python3
"""Original scientific figures for research edition 0.1.0.

Requires matplotlib and numpy. No external or empirical datasets are used.
Exports editable SVG, vector PDF and 300-dpi PNG. See theory/figures/README.md.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm

OUT=Path(__file__).resolve().parents[1]/'theory/figures'
OUT.mkdir(parents=True,exist_ok=True)
BLUE='#0072B2'; TEAL='#009E73'; ORANGE='#D55E00'; GOLD='#E69F00'
INK='#22272E'; GRAY='#66717E'; LIGHT='#DDE2E7'; PURPLE='#8875A5'
plt.rcParams.update({'font.family':'sans-serif','font.sans-serif':['Arial','DejaVu Sans'],
 'font.size':7,'axes.titlesize':8,'axes.labelsize':7,'xtick.labelsize':6.5,'ytick.labelsize':6.5,
 'axes.linewidth':0.6,'lines.linewidth':1.3,'text.color':INK,'axes.labelcolor':INK,
 'xtick.color':INK,'ytick.color':INK,'svg.fonttype':'none','pdf.fonttype':42,'savefig.facecolor':'white'})

def canvas(fig,rect):
 ax=fig.add_axes(rect);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off');return ax
def label(ax,letter,title):
 ax.text(0,1.035,letter,transform=ax.transAxes,fontsize=9,fontweight='bold',va='bottom')
 ax.text(.055,1.035,title,transform=ax.transAxes,fontsize=8,fontweight='bold',va='bottom')
def box(ax,x,y,w,h,text,color=BLUE,fs=7,fill=True):
 p=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.008,rounding_size=0.015',
    linewidth=.65,edgecolor=color,facecolor=color+'12' if fill else 'white',zorder=3)
 p.set_clip_on(False)
 ax.add_patch(p);ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fs,zorder=4,linespacing=1.3)
def arrow(ax,start,end,color=GRAY,style='-',rad=0,lw=.8):
 ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=7,linewidth=lw,
   color=color,linestyle=style,connectionstyle=f'arc3,rad={rad}',zorder=2,clip_on=False))
def tidy(ax):
 ax.spines[['top','right']].set_visible(False);ax.tick_params(width=.6,length=3)
def save(fig,stem):
 for ext in ['svg','pdf','png']:fig.savefig(OUT/f'{stem}.{ext}',dpi=300)
 svg=OUT/f'{stem}.svg'
 svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
 plt.close(fig)

# Figure 1: logical architecture and a complete domain map.
fig=plt.figure(figsize=(7.2,6.15))
a=canvas(fig,[.045,.585,.91,.35]);label(a,'a','From constraints and institutions to conditional outcomes')
xs=[.01,.36,.71]; w=.28
for x,text,color in zip(xs,['Human constraints\nTime · attention · recovery','Technical possibilities\nCapability · cost · deployment','Social arrangements\nGoals · rights · institutions'],[BLUE,TEAL,ORANGE]):
 box(a,x,.74,w,.22,text,color)
for x,text in zip(xs,['Allocation\nSelection · prices · access','Delegation\nAuthority · verification · exit','Adaptation\nLearning · comparison · feedback']):
 box(a,x,.39,w,.19,text,GRAY)
for x,text in zip(xs,['Time and agency','Work and distribution','Trust and relationships']):
 box(a,x,.05,w,.16,text,GRAY,fill=False)
for x in xs:
 arrow(a,(x+w/2,.73),(x+w/2,.59));arrow(a,(x+w/2,.38),(x+w/2,.22))
arrow(a,(.30,.48),(.345,.48));arrow(a,(.65,.48),(.695,.48))
fig.text(.045,.545,'Proposed links; effects depend on context. The diagram is selective, not a complete causal graph.',fontsize=6.3,color=GRAY)
b=canvas(fig,[.045,.205,.91,.295]);label(b,'b','Construct coverage: 16 domains, 8 variables per domain')
domains=['Time & embodiment','Attention & cognition','Affect & motivation','Desire & status',
 'Skills & learning','AI & deployment','Costs & engineering','Content & aesthetics',
 'Truth & trust','Relationships & networks','Labor & organization','Markets & capital',
 'Platforms & delegation','Institutions & governance','Space & ecology','Meaning & generations']
for i,name in enumerate(domains):
 row,col=divmod(i,4);x=col*.255;y=.755-row*.25
 color=[BLUE,TEAL,PURPLE,ORANGE][row]
 box(b,x,y,.235,.19,f'{i+1:02d}  {name}\nV{i*8+1:03d}–V{i*8+8:03d}',color,fs=6.3)
c=canvas(fig,[.045,.045,.91,.10]);label(c,'c','Research architecture: distinguish definitions, models and evidence')
for i,(text,color) in enumerate([('16 principles',BLUE),('128 variables',TEAL),('64 hypotheses',PURPLE),('8 models',ORANGE),('Empirical inquiry',GRAY)]):
 x=i*.205;box(c,x,.14,.175,.5,text,color,fs=6.8)
 if i<4:arrow(c,(x+.18,.39),(x+.20,.39))
fig.text(.045,.014,'Conceptual architecture · no empirical effect sizes · research edition 0.1.0',fontsize=6,color=GRAY)
save(fig,'fig01-framework')

# Figure 2: phase boundary and response curves from exactly the M05 equation.
fig=plt.figure(figsize=(7.2,3.9))
ax=fig.add_axes([.09,.30,.37,.59]);label(ax,'a','Conditional labor-demand regimes')
p=np.linspace(.2,1,250);eps=np.linspace(0,2.5,250);P,E=np.meshgrid(p,eps)
ratio=.5*P**(-E)
cmap=LinearSegmentedColormap.from_list('balanced',[BLUE,'#F7F7F4',ORANGE])
im=ax.pcolormesh(P,E,np.log2(ratio),cmap=cmap,norm=TwoSlopeNorm(vmin=-1,vcenter=0,vmax=3),shading='auto',rasterized=True)
ax.contour(P,E,ratio,levels=[1],colors=INK,linewidths=.85)
ax.set(xlabel=r'Task price ratio, $p_1/p_0$',ylabel=r'Demand elasticity, $\varepsilon$',xlim=(.2,1),ylim=(0,2.5))
ax.text(.78,.35,'Less labor',ha='center',fontsize=6.5)
ax.text(.31,2.12,'More labor',ha='center',fontsize=6.5)
ax.text(.52,1.28,r'$L_1/L_0=1$',rotation=44,fontsize=6.5,bbox=dict(facecolor='white',edgecolor='none',alpha=.8,pad=1))
tidy(ax)
cax=fig.add_axes([.09,.14,.37,.032]);cb=fig.colorbar(im,cax=cax,orientation='horizontal',ticks=[-1,0,1,2,3]);cb.ax.set_xticklabels(['0.5','1','2','4','8']);cb.set_label('Total labor-hours ratio (logarithmic color scale)',fontsize=6)
bx=fig.add_axes([.615,.30,.34,.59]);label(bx,'b','Same labor saving, different demand')
for elastic,col,ls in [(0.5,BLUE,'-'),(1,GRAY,'--'),(2,ORANGE,'-.')]:
 bx.plot(p,.5*p**(-elastic),color=col,ls=ls,label=fr'$\varepsilon={elastic:g}$')
 bx.plot([.5],[.5*.5**(-elastic)],'o',color=col,ms=3)
bx.axhline(1,color=GRAY,lw=.65,ls=':');bx.axvline(.5,color=LIGHT,lw=.7)
bx.set(xlabel=r'Task price ratio, $p_1/p_0$',ylabel=r'Total labor-hours ratio, $L_1/L_0$',xlim=(.2,1),ylim=(0,4))
bx.legend(frameon=False,fontsize=6.5,loc='upper right',handlelength=2.7);tidy(bx)
bx.text(.99,.02,'Curve above 4 is clipped',transform=bx.transAxes,ha='right',fontsize=6,color=GRAY)
fig.text(.615,.145,r'$L_1/L_0=0.5\,(p_1/p_0)^{-\varepsilon}$',fontsize=9)
fig.text(.045,.02,'M05 model calculation · labor per task is halved · fixed demand form · hours are not jobs or wages',fontsize=6,color=GRAY)
save(fig,'fig02-conditional-labor')

# Figure 3: explicit payoff structure and two different equilibrium mechanisms.
fig=plt.figure(figsize=(7.2,3.2))
a=canvas(fig,[.045,.22,.285,.64]);label(a,'a','Stimulation game (M02)')
a.text(.6,.89,'Producer 2',ha='center',fontsize=7)
a.text(.03,.45,'Producer 1',ha='center',va='center',rotation=90,fontsize=7)
for j,s in enumerate(['R','E']):a.text(.40+j*.32,.77,s,ha='center',fontsize=7)
for i,s in enumerate(['R','E']):a.text(.16,.60-i*.29,s,ha='center',va='center',fontsize=7)
for i,row in enumerate([[(3,3),(1,4)],[(4,1),(2,2)]]):
 for j,val in enumerate(row):
  x=.24+j*.32;y=.455-i*.29
  a.add_patch(Rectangle((x,y),.32,.29,facecolor=ORANGE+'20' if i==j==1 else '#F4F6F8',edgecolor='white',lw=2))
  a.text(x+.16,y+.145,str(val),ha='center',va='center',fontsize=8)
a.text(.57,.04,'E, E: unique equilibrium',ha='center',fontsize=6.5)
a.text(.03,-.05,'R = restraint; E = escalation\nAssumed private utility, not measured welfare',fontsize=6,color=GRAY)
b=fig.add_axes([.40,.27,.24,.57]);label(b,'b','Changing incentives')
p=np.linspace(0,2,100);b.plot(p,1-p,color=ORANGE)
b.axhline(0,color=GRAY,lw=.6);b.axvline(1,color=GRAY,lw=.6,ls=':')
b.set(xlabel='Added escalation cost, p',ylabel='Payoff advantage of E over R',xlim=(0,2),ylim=(-1.2,1.2),xticks=[0,1,2],yticks=[-1,0,1])
b.text(.18,.72,'E dominates',fontsize=6.3);b.text(1.13,-.77,'R dominates',fontsize=6.3);tidy(b)
c=fig.add_axes([.735,.27,.235,.57]);label(c,'c','Coordination (M03)')
q=np.linspace(0,1,100);c.plot(q,4*q,color=BLUE,label='Open: 4q');c.plot(q,0*q+2,color=GRAY,ls='--',label='Proprietary: 2')
c.axvline(.5,color=LIGHT,lw=.7);c.plot([.5],[2],'o',color=INK,ms=3)
c.set(xlabel='Expected open adoption, q',ylabel='Expected private payoff',xlim=(0,1),ylim=(0,4.2),xticks=[0,.5,1],yticks=[0,2,4]);tidy(c)
c.legend(frameon=False,fontsize=5.9,loc='upper left',handlelength=1.8)
fig.text(.045,.035,'Illustrative games · equilibrium depends on specified payoffs · Nash equilibrium does not imply social optimality',fontsize=6,color=GRAY)
save(fig,'fig03-games')

# Figure 4: identification and governance. Solid/dashed arrows have distinct roles.
fig=plt.figure(figsize=(7.2,4.75))
a=canvas(fig,[.045,.53,.43,.37]);label(a,'a','A causal identification problem')
box(a,.25,.77,.48,.18,'Baseline loneliness',BLUE)
box(a,.02,.34,.35,.18,'AI use',TEAL)
box(a,.61,.34,.36,.18,'Later loneliness',ORANGE)
box(a,.25,.0,.48,.18,'Support and resources',PURPLE)
arrow(a,(.39,.76),(.2,.53));arrow(a,(.63,.76),(.78,.53))
arrow(a,(.39,.19),(.2,.33));arrow(a,(.63,.19),(.78,.33))
arrow(a,(.38,.43),(.60,.43),color=INK,lw=1.1)
a.text(.49,.56,'Target effect',ha='center',fontsize=6.3)
b=canvas(fig,[.545,.53,.41,.37]);label(b,'b','Delegation and governance')
for y,text,color in [(.77,'User goals and authorization',BLUE),(.43,'Provider / application / model',TEAL),(.09,'Actions and consequences',ORANGE)]:
 box(b,.05,y,.68,.18,text,color,fs=6.7)
arrow(b,(.36,.76),(.36,.62));arrow(b,(.36,.42),(.36,.28))
arrow(b,(.75,.18),(.75,.86),style='--',rad=.45,color=PURPLE)
b.text(.92,.51,'Audit · appeal · exit',rotation=90,ha='center',va='center',fontsize=6.5)
b.text(.40,-.02,'Control requires information, capacity and authority',ha='center',fontsize=6.2,color=GRAY)
c=canvas(fig,[.045,.11,.91,.29]);label(c,'c','Competing feedback paths under expanded generation')
box(c,.0,.35,.19,.30,'Cheaper\ngeneration',TEAL)
box(c,.265,.35,.19,.30,'More tasks\nand content',GRAY)
box(c,.535,.66,.19,.27,'Verification\ncapacity',BLUE)
box(c,.535,.04,.19,.27,'Unverified\nexposure',ORANGE)
box(c,.80,.35,.19,.30,'Trust and\nusable outcomes',PURPLE)
arrow(c,(.20,.50),(.255,.50));arrow(c,(.465,.54),(.525,.78));arrow(c,(.465,.45),(.525,.19))
arrow(c,(.735,.78),(.79,.59));arrow(c,(.735,.18),(.79,.42))
c.text(.845,.86,'May support',fontsize=6,ha='center');c.text(.86,.04,'May undermine',fontsize=6,ha='center')
c.plot([.9,.9,.12,.12],[.33,-.09,-.09,.15],color=PURPLE,ls='--',lw=.8,clip_on=False,zorder=2)
arrow(c,(.12,.15),(.12,.32),style='--',color=PURPLE)
fig.text(.045,.061,'Trust can alter subsequent adoption; all directions require testing.',fontsize=6.2,color=GRAY)
fig.text(.045,.015,'Conceptual causal hypotheses · solid: proposed link · dashed: governance or feedback · no estimated causal effects',fontsize=6,color=GRAY)
save(fig,'fig04-causality-governance')
print('Rendered 4 original figures in SVG, PDF and PNG')
