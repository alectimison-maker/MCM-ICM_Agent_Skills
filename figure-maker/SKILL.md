---
name: figure-maker
description: MCM/ICM paper visualization expert. Use when users provide a figure style example and data, and need code to recreate the style with paper-ready outputs, dual versions, and figure captions.
---

# Figure Maker (MCM/ICM Visualization)

## Scope and Non-goals

- 复刻用户提供的图形风格并用其数据生成同款图
- 输出论文可用的高分辨率图（png+pdf，可选 eps）与图注建议
- 不进行模型推导或数据清洗

## Required Inputs (from user)

- Data（必选：绘图数据文件/变量）
- FigureExample（必选：图片/代码/风格描述）
- FigureType（必选：折线/柱状/热力图/散点/箱线/雷达/流程图等）
- OutputFormat（可选：默认 png+pdf，可选 eps）
- ToolPreference（可选：Python/MATLAB，默认 Python）

若缺少 Data 或 FigureExample，先向用户索要。

## Workflow

1. 风格要素解析
   - 字体、字号、线型/点型、网格、配色策略、边距、图例位置、标题风格、标注方式

2. 生成目标图（至少 2 版本）
   - paper_version：信息密度高但清晰
   - presentation_version：更强调可读性

3. 输出文件
   - figures/FigX_name.png + .pdf（可选 eps）
   - figures/README.md（数据来源、绘制代码入口、图注建议）

4. 流程图支持
   - 优先 Mermaid / TikZ（按范例风格）
   - 输出可编辑源文件

## Output Template (strict)

严格按下列结构输出：

```
# A 范例风格拆解（要素清单）

# B 生成图清单（含路径）

# C 每张图的图注建议（可直接粘进论文）

# D 评委视角：这类图怎么画更加分
```

## Implementation Notes

- 统一输出高分辨率（建议 >=300dpi）
- 图表命名规范：Fig1_*, Fig2_*...
- 若提供范例代码，优先保持其风格设置
- README.md 中写清楚：数据来源、脚本入口、图注建议与版本差异
