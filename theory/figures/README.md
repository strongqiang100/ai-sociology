# 论文图版 / Research figures

图 1 呈现理论结构；图 2 说明同样的自动化为何可能带来不同的劳动需求；图 3 展示激励怎样改变博弈结果；图 4 区分相关、因果与治理反馈。各图附中英文说明及可下载文件。

Figure 1 maps the framework; Figure 2 shows why automation can produce different labor-demand outcomes; Figure 3 examines how incentives change equilibria; Figure 4 distinguishes correlation, causation and governance feedback. Bilingual captions and downloadable files accompany each figure.

## 1 · 理论结构与变量领域 / Theoretical architecture and variable domains

![理论结构与变量领域 / Theoretical architecture and variable domains](fig01-framework.png)

a，人的条件、技术供给与制度安排通过资源分配、委托和适应影响生活。箭头仅选取部分待研究的联系，不表示完整因果图。b，16 个领域及其变量编号，每域 8 项。c，原则、变量、假说、模型与经验研究的关系。该图为概念示意，不包含效应估计。

a, Human conditions, technical supply and institutions affect life through allocation, delegation and adaptation. Arrows select proposed links, not a complete causal graph. b, Sixteen domains with eight variables each. c, Relations among principles, variables, hypotheses, models and empirical inquiry. Conceptual schematic; no effect estimates.

[SVG](fig01-framework.svg) · [PDF](fig01-framework.pdf) · [PNG](fig01-framework.png)

## 2 · 自动化后的劳动需求为何分叉 / Why labor demand can diverge after automation

![自动化后的劳动需求为何分叉 / Why labor demand can diverge after automation](fig02-conditional-labor.png)

按 M05 计算，假设每项任务所需人工减半，需求函数不变。a，价格比与需求弹性共同决定总人工小时的变化，黑线表示变化为零，色阶采用对数刻度。b，三种弹性下的曲线；圆点对应价格减半。总人工小时不是岗位数量或个人工资。曲线与色阶上限按图示截取，数值均来自假设模型。

Calculated from M05 with labor per task halved and demand form fixed. a, Price ratios and elasticity determine total labor hours; the black line marks no change and color is logarithmic. b, Three elasticities; markers indicate halved prices. Hours are not job counts or wages. Display ranges are limited as shown; all values come from the assumed model.

[SVG](fig02-conditional-labor.svg) · [PDF](fig02-conditional-labor.pdf) · [PNG](fig02-conditional-labor.png)

## 3 · 刺激竞赛、激励改变与协调 / Stimulation, changing incentives and coordination

![刺激竞赛、激励改变与协调 / Stimulation, changing incentives and coordination](fig03-games.png)

a，M02 的假设收益矩阵，双方升级构成唯一纳什均衡。b，升级的附加代价超过 1 时，克制转为严格占优策略；等于 1 时无差异。c，M03 中对他方采用开放标准的预期超过 1/2 后，开放策略的期望收益更高。这是两类不同博弈，不是平台实测结果。

a, Assumed M02 payoffs yield mutual escalation as the unique Nash equilibrium. b, Restraint strictly dominates when added escalation cost exceeds 1; equality gives indifference. c, In M03, openness yields higher expected payoff when expected counterpart adoption exceeds one half. These are distinct illustrative games, not platform measurements.

[SVG](fig03-games.svg) · [PDF](fig03-games.pdf) · [PNG](fig03-games.png)

## 4 · 因果识别、委托与反馈 / Identification, delegation and feedback

![因果识别、委托与反馈 / Identification, delegation and feedback](fig04-causality-governance.png)

a，既有孤独与支持条件可能同时影响使用及后续孤独，简单相关不能识别中间的目标效应。b，目标授权、服务执行与后果之间，需要可实际使用的审核、申诉和退出。c，供给扩张可以伴随核验改善，也可以扩大未核验信息暴露；信任又可能影响后续采用。实线为假定联系，虚线为治理或反馈联系，均待经验检验。

a, Baseline loneliness and support can affect both use and later loneliness, preventing simple correlation from identifying the target effect. b, Delegation requires usable audit, appeal and exit between authorization, service execution and consequences. c, Expanded supply can accompany better verification or greater unverified exposure; trust may affect subsequent adoption. Solid links are proposed relations; dashed links denote governance or feedback. All require empirical examination.

[SVG](fig04-causality-governance.svg) · [PDF](fig04-causality-governance.pdf) · [PNG](fig04-causality-governance.png)

## 复现 / Reproduction

```bash
python3 -m pip install matplotlib numpy
python3 scripts/render_theory_figures.py
```

在仓库根目录运行。SVG 保留文字，PDF 嵌入字体，PNG 为 300 dpi。图 1、4 是理论示意；图 2、3 来自第四卷的假设模型，未使用经验数据。

Run from the repository root. SVG retains text, PDF embeds fonts, and PNG is 300 dpi. Figures 1 and 4 are conceptual; Figures 2 and 3 use the assumed models in Volume IV. No empirical dataset is used.
