---
name: figure-maker
description: MCM/ICM paper visualization expert. Use when users provide data + style example or want to select a style from style_library to generate paper-ready figures, MATLAB-first multi-variant outputs (png/pdf/eps), captions, and optional TikZ export.
---

# Figure Maker (MCM/ICM Visualization)

## Scope and Non-goals

- 复刻用户提供的图形风格，并基于数据生成同款图
- 当用户没有明确范例时，优先从 style_library 里检索风格卡并融合生成
- 输出论文可用的高分辨率图（png+pdf，必要时 eps）+ 图注建议
- 不进行建模推导或数据清洗

## Required Inputs (from user)

- Data（必需：绘图数据文件或变量）
- FigureType（必需：line/bar/heatmap/scatter/flowchart/box/…）
- Style signal（必需其一：范例图或关键词/标签用于检索 style_library）
- ToolPreference（可选：默认 MATLAB；若用户指定 Python 则再切换）
- OutputFormat（可选：默认 png+pdf，可选 eps）

若缺少 Data 或 Style signal，先向用户索要。

## Style Library Layout (固定结构)

```
style_library/
  examples/
    line/
    bar/
    heatmap/
    scatter/
    flowchart/
    unsorted/            # 暂未分类的图片
  cards/                 # 每张图对应一张风格卡（可检索）
    line_001.md
    heatmap_003.md
  index.csv              # 全部范例索引：id/figure_type/tags/用途/来源/备注
```

### 最低限度分类规则

- 新图：先放到 examples/<FigureType>/
- 每图配 1 张卡片（3~6 个标签即可）
- index.csv 追加一行记录
- 若 FigureType 不确定：先放入 examples/unsorted/，卡片 tags 里写 needs_review，并尽快补分类

## Style Card Template (cards/xxx.md)

```
id: line_001
figure_type: line
use_case: trend + interval
tags: [paper_dense, colorblind, direct_label, thin_grid, annotation]
layout:
  aspect: 4:3
  legend: none
  label: direct_on_line
style:
  font: serif-like / small caps
  linewidth: medium
  marker: minimal
  grid: light major only
color:
  palette: muted qualitative
  note: avoid neon; print-friendly
density_tricks:
  - direct labels instead of legend
  - show CI band + key points
  - annotate change-points
caption_style:
  - 1 sentence “what + why”
  - 1 sentence “how computed”
```

## Workflow

1. 风格要素解析
   - 用户给范例图：拆出字体/字号、线宽、配色、网格、图例方式、标注方式、边距、布局等
   - 用户给关键词：在 style_library/cards 与 index.csv 中检索，选 3~5 张最相关风格卡
2. 形成“风格规则清单”
   - 汇总 3~5 张卡片的共同约束，输出可执行的绘图规则
3. 生成多版本图（一次性批量）
   - 默认 MATLAB 脚本
   - 每张图至少 3 个版本（v1/v2/v3），用于挑选
   - 变化维度：配色、线宽、标注密度、网格强度、图例/直标方案
4. 输出文件
   - figures/FigX_name_v1.png + .pdf（可选 eps）
   - figures/FigX_name_v2.png + .pdf …
   - figures/README.md（数据来源、脚本入口、版本差异、推荐版本）
5. 若用户选择某个版本：生成 TikZ
   - 使用 MATLAB 导出 TikZ（如 matlab2tikz）
   - 输出 figures/FigX_name_vY.tikz 或 .tex

## Output Template (strict)

```
# A 风格卡检索与融合
- matched_cards: [line_001, line_014, line_021]
- merged_rules: 字体/线宽/配色/标注/网格/布局要点

# B 生成图清单（含路径）
- figures/Fig1_xxx_v1.png + .pdf
- figures/Fig1_xxx_v2.png + .pdf
- figures/Fig1_xxx_v3.png + .pdf

# C 每张图的图注建议（可直接粘进论文）

# D 评委视角：如何提高信息密度与说服力
```

## Implementation Notes

- 尽量使用“直标注”替代大图例，提升信息密度
- 优先色盲友好/灰度可读的配色
- 论文内保持统一字体/线宽/边距/编号规则
- MATLAB 输出建议：
  - `exportgraphics` 或 `print`，分辨率 >= 300 dpi
  - 统一字体与字号（例如 8–10 pt）
- 若用户强调“高信息密度”，优先加入：排序 + 分组 + 重点高亮 + 注释关键点
